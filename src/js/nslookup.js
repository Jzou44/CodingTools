(function () {
  'use strict';

  const form = document.getElementById('dns-form');
  const input = document.getElementById('dns-name');
  const type = document.getElementById('dns-type');
  const status = document.getElementById('dns-status');
  const results = document.getElementById('dns-results');
  const answers = document.getElementById('dns-answers');
  const types = { 1: 'A', 2: 'NS', 5: 'CNAME', 6: 'SOA', 12: 'PTR', 13: 'HINFO', 15: 'MX', 16: 'TXT', 28: 'AAAA', 33: 'SRV', 257: 'CAA' };
  const rcodes = { 1: 'FORMERR', 2: 'SERVFAIL', 4: 'NOTIMP', 5: 'REFUSED' };
  let active;

  function reverseAddress(name) {
    if (/^\d{1,3}(\.\d{1,3}){3}$/.test(name)) {
      const parts = name.split('.');
      if (parts.some(part => Number(part) > 255 || String(Number(part)) !== part)) throw new Error();
      return parts.reverse().join('.') + '.in-addr.arpa';
    }
    if (!name.includes(':')) return name;
    // URL normalizes an IPv6 literal (including an embedded IPv4 address).
    if (!/^[0-9a-f:.]+$/i.test(name)) throw new Error();
    const literal = new URL('https://[' + name + ']').hostname.slice(1, -1);
    const [left, right] = literal.split('::');
    const head = left ? left.split(':') : [];
    const tail = right ? right.split(':') : [];
    const words = [...head, ...Array(8 - head.length - tail.length).fill('0'), ...tail];
    return words.map(word => word.padStart(4, '0')).join('').split('').reverse().join('.') + '.ip6.arpa';
  }

  function queryName(value, recordType) {
    let name = value.trim().replace(/[\u3002\uff0e\uff61]/g, '.');
    if (recordType === 'PTR') name = reverseAddress(name);
    if (name === '.' || name === '*') return name;
    name = name.replace(/\.$/, '');
    if (!name || /[\s:/\\?#@%\[\]\x00-\x1f\x7f]/u.test(name)) throw new Error();
    // The fixed suffix prevents the URL parser from rewriting numeric DNS labels as IPv4.
    // Browsers percent-encode a wildcard when normalizing an international name.
    const wildcard = name.startsWith('*.');
    const hostname = new URL('https://' + (wildcard ? name.slice(2) : name) + '.invalid').hostname;
    if (!hostname.endsWith('.invalid')) throw new Error();
    const ascii = hostname.slice(0, -8);
    const fullName = wildcard ? '*.' + ascii : ascii;
    if (fullName.length > 253 || !ascii.split('.').every(label =>
      /^[a-z0-9_](?:[a-z0-9_-]{0,61}[a-z0-9_])?$/i.test(label))) throw new Error();
    return fullName;
  }

  function clearQuery() {
    if (active) active.abort();
    active = null;
    status.textContent = '';
    answers.replaceChildren();
    results.hidden = true;
    input.removeAttribute('aria-invalid');
  }

  function render(records) {
    const fragment = document.createDocumentFragment();
    for (const record of records) {
      const row = document.createElement('tr');
      for (const field of [record.name, types[record.type] || 'TYPE' + record.type, record.TTL, record.data]) {
        const cell = row.insertCell();
        cell.textContent = String(field);
      }
      fragment.appendChild(row);
    }
    answers.replaceChildren(fragment);
    results.hidden = records.length === 0;
  }

  form.addEventListener('input', clearQuery);
  form.addEventListener('change', clearQuery);
  form.addEventListener('submit', async function (event) {
    event.preventDefault();
    clearQuery();
    const recordType = type.value;
    let name;
    try {
      name = queryName(input.value, recordType);
    } catch {
      status.textContent = form.dataset.invalid;
      input.setAttribute('aria-invalid', 'true');
      input.focus();
      return;
    }

    const controller = new AbortController();
    active = controller;
    const timeout = setTimeout(() => controller.abort(), 10000);
    status.textContent = form.dataset.loading;
    try {
      const url = new URL('https://dns.google/resolve');
      url.search = new URLSearchParams({ name, type: recordType, edns_client_subnet: '0.0.0.0/0' });
      const response = await fetch(url, { signal: controller.signal, credentials: 'omit', referrerPolicy: 'no-referrer' });
      if (!response.ok) throw new Error();
      const data = await response.json();
      if (active !== controller) return;
      if (!data || !Number.isInteger(data.Status) || data.TC) throw new Error();
      if (data.Status === 3) {
        status.textContent = form.dataset.nxdomain;
        return;
      }
      if (data.Status !== 0) {
        status.textContent = form.dataset.rcode + ' ' + (rcodes[data.Status] || data.Status);
        return;
      }
      const records = data.Answer === undefined ? [] : data.Answer;
      if (!Array.isArray(records) || !records.every(record => record && typeof record.name === 'string'
          && Number.isInteger(record.type) && Number.isInteger(record.TTL) && typeof record.data === 'string')) throw new Error();
      render(records);
      const hasAnswer = records.some(record => recordType === 'ANY' || types[record.type] === recordType);
      status.textContent = hasAnswer ? form.dataset.complete : form.dataset.empty;
      if (hasAnswer && window.ToolCommon) window.ToolCommon.trackToolSuccess('lookup');
    } catch {
      if (active === controller) status.textContent = form.dataset.failed;
    } finally {
      clearTimeout(timeout);
      if (active === controller) active = null;
    }
  });
})();

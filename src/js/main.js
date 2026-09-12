/* Accessible homepage search and category filtering. */
(function () {
  'use strict';
  var input = document.getElementById('tool-search');
  if (!input) return;
  var cards = Array.from(document.querySelectorAll('.tool-card'));
  var sections = Array.from(document.querySelectorAll('.category-section'));
  var filters = Array.from(document.querySelectorAll('[data-filter]'));
  var status = document.getElementById('search-status');
  var empty = document.getElementById('search-empty');
  var selected = 'all';
  function normalize(value) { return value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[-_]/g, ' '); }
  var searchText = cards.map(function (card) { return normalize(card.textContent + ' ' + card.dataset.search); });
  function filter() {
    var words = normalize(input.value).trim().split(/\s+/).filter(Boolean);
    var count = 0;
    cards.forEach(function (card, index) {
      var matches = (selected === 'all' || card.closest('[data-category]').dataset.category === selected) && words.every(function (word) { return searchText[index].includes(word); });
      card.hidden = !matches;
      if (matches) count += 1;
    });
    sections.forEach(function (section) { section.hidden = !section.querySelector('.tool-card:not([hidden])'); });
    filters.forEach(function (button) {
      var active = button.dataset.filter === selected;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    status.textContent = status.dataset.template.replace('{count}', count);
    empty.hidden = count !== 0;
  }
  input.addEventListener('input', filter);
  input.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') { input.value = ''; filter(); }
    if (event.key === 'Enter' && !event.isComposing) {
      var matches = cards.filter(function (card) { return !card.hidden; });
      if (matches.length === 1) matches[0].click();
    }
  });
  filters.forEach(function (button) { button.addEventListener('click', function () { selected = button.dataset.filter; filter(); }); });
  document.querySelector('.reset-search').addEventListener('click', function () { input.value = ''; selected = 'all'; filter(); input.focus(); });
  document.addEventListener('keydown', function (event) {
    if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey || event.isComposing) return;
    if (event.target.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(event.target.tagName)) return;
    event.preventDefault(); input.focus();
  });
  window.addEventListener('hashchange', function () {
    if (sections.some(function (section) { return '#' + section.id === location.hash; })) {
      selected = 'all'; input.value = ''; filter(); document.getElementById(location.hash.slice(1)).scrollIntoView();
    }
  });
  document.querySelector('.category-filters').hidden = false;
  filter();
})();

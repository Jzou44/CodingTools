---
name: coding-tools-nslookup
description: "Use when Codex needs to run the Coding.Tools DNS Lookup (nslookup) MCP tool (nslookup) through tools/list and tools/call for Look up public DNS records for a domain using Google Public DNS in your browser."
---

# DNS Lookup (nslookup)

Use the Coding.Tools MCP tool `nslookup` when the user needs: Look up public DNS records for a domain using Google Public DNS in your browser.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `nslookup`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `nslookup`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "nslookup"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "DNS Lookup (nslookup) runs in the browser. tools/call returns a web UI resource link.",
  "properties": {},
  "additionalProperties": false,
  "examples": [
    {}
  ]
}
```

## Argument Guidance

This browser-only tool is listed by MCP for discovery. Use an empty arguments object `{}`; the call intentionally returns `isError: true` plus a `resource_link` to the web UI.

## Output Schema

```json
{
  "type": "object",
  "description": "DNS Lookup (nslookup) returns isError=true with a resource_link to the browser UI."
}
```

## Example Arguments

```json
{}
```

## Example tools/call

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "nslookup",
    "arguments": {}
  }
}
```

## Notes

This is a browser-only tool in MCP. `tools/call` returns `isError: true` with a `resource_link` to https://coding.tools/nslookup.html.

Web UI: https://coding.tools/nslookup.html

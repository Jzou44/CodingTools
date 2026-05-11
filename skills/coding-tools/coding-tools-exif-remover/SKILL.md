---
name: coding-tools-exif-remover
description: "Use when Codex needs to run the Coding.Tools EXIF Remover MCP tool (exif-remover) through tools/list and tools/call for Strip all EXIF metadata from images to protect your privacy."
---

# EXIF Remover

Use the Coding.Tools MCP tool `exif-remover` when the user needs: Strip all EXIF metadata from images to protect your privacy.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `exif-remover`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `exif-remover`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "exif-remover"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "EXIF Remover needs browser image APIs. tools/call does not process image bytes server-side; it returns a web UI resource link.",
  "properties": {},
  "additionalProperties": false,
  "examples": [
    {}
  ]
}
```

## Argument Guidance

This tool is exposed in MCP so clients can discover it, but server-side MCP calls do not process image bytes for this browser-only workflow. Use an empty arguments object `{}`; the call intentionally returns `isError: true` plus a `resource_link` to the web UI.

## Output Schema

```json
{
  "type": "object",
  "description": "EXIF Remover returns isError=true with a resource_link to the browser UI because server-side image processing is not available."
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
    "name": "exif-remover",
    "arguments": {}
  }
}
```

## Notes

This is a browser-only image tool in MCP. `tools/call` returns `isError: true` with a `resource_link` to https://coding.tools/exif-remover.html instead of processing image bytes server-side.

Web UI: https://coding.tools/exif-remover.html

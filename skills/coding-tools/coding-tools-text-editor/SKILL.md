---
name: coding-tools-text-editor
description: "Use when Codex needs to run the Coding.Tools Text Editor Online MCP tool (text-editor) through tools/list and tools/call for Edit text online with line numbers, word wrap, and character counting."
---

# Text Editor Online

Use the Coding.Tools MCP tool `text-editor` when the user needs: Edit text online with line numbers, word wrap, and character counting.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `text-editor`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `text-editor`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "text-editor"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for Text Editor Online.",
  "properties": {
    "input": {
      "type": "string",
      "description": "Text to echo back with line and character counts."
    },
    "options": {
      "type": "object",
      "description": "Optional per-tool settings.",
      "additionalProperties": true
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "input": "Release notes\n- Fix login\n- Add MCP endpoint"
    }
  ]
}
```

## Argument Guidance

Pass only the JSON object shown in Example Arguments as `tools/call.params.arguments`; do not include the outer JSON-RPC envelope inside `arguments`.

Use `input` for the value being converted, formatted, counted, hashed, or tested.

Omit `options` unless the discovered `inputSchema` lists a setting you need.

The demo values are synthetic and safe for testing the remote endpoint; replace them with user data only after the privacy check above is satisfied.

## Output Schema

```json
{
  "type": "object",
  "description": "Text echo plus simple text metrics.",
  "properties": {
    "text": {
      "type": "string"
    },
    "characters": {
      "type": "integer"
    },
    "lines": {
      "type": "integer"
    }
  },
  "required": [
    "text",
    "characters",
    "lines"
  ],
  "additionalProperties": false
}
```

## Example Arguments

```json
{
  "input": "Release notes\n- Fix login\n- Add MCP endpoint"
}
```

## Example tools/call

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "text-editor",
    "arguments": {
        "input": "Release notes\n- Fix login\n- Add MCP endpoint"
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/text-editor.html

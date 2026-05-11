---
name: coding-tools-character-count
description: "Use when Codex needs to run the Coding.Tools Character Count MCP tool (character-count) through tools/list and tools/call for Count characters, words, lines, and UTF-8 bytes with Twitter limit tracker."
---

# Character Count

Use the Coding.Tools MCP tool `character-count` when the user needs: Count characters, words, lines, and UTF-8 bytes with Twitter limit tracker.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `character-count`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `character-count`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "character-count"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for Character Count.",
  "properties": {
    "input": {
      "type": "string",
      "description": "Text to count characters, UTF-8 bytes, words, and lines."
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
      "input": "MCP endpoint is ready for tool automation."
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
  "description": "Character, byte, word, and line counts.",
  "properties": {
    "characters": {
      "type": "integer"
    },
    "charactersNoSpaces": {
      "type": "integer"
    },
    "bytesUtf8": {
      "type": "integer"
    },
    "words": {
      "type": "integer"
    },
    "lines": {
      "type": "integer"
    }
  },
  "required": [
    "characters",
    "charactersNoSpaces",
    "bytesUtf8",
    "words",
    "lines"
  ],
  "additionalProperties": false
}
```

## Example Arguments

```json
{
  "input": "MCP endpoint is ready for tool automation."
}
```

## Example tools/call

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "character-count",
    "arguments": {
        "input": "MCP endpoint is ready for tool automation."
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/character-count.html

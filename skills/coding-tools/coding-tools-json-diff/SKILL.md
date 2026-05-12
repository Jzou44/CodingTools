---
name: coding-tools-json-diff
description: "Use when Codex needs to run the Coding.Tools JSON Diff MCP tool (json-diff) through tools/list and tools/call for Compare two JSON documents and highlight structural differences."
---

# JSON Diff

Use the Coding.Tools MCP tool `json-diff` when the user needs: Compare two JSON documents and highlight structural differences.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `json-diff`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `json-diff`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "json-diff"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for JSON Diff.",
  "properties": {
    "input": {
      "type": "string",
      "description": "Original JSON string. Pass the changed JSON string in options.compareTo."
    },
    "options": {
      "type": "object",
      "properties": {
        "compareTo": {
          "type": "string",
          "description": "Changed JSON string to compare against the input JSON."
        },
        "includeUnchanged": {
          "type": "boolean",
          "default": false,
          "description": "Include unchanged paths in the diff output."
        }
      },
      "required": [
        "compareTo"
      ],
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "input": "{\"user\":{\"name\":\"Alice\",\"role\":\"admin\"}}",
      "options": {
        "compareTo": "{\"user\":{\"name\":\"Alice\",\"role\":\"editor\"}}"
      }
    }
  ]
}
```

## Argument Guidance

Pass only the JSON object shown in Example Arguments as `tools/call.params.arguments`; do not include the outer JSON-RPC envelope inside `arguments`.

Use `input` for the value being converted, formatted, counted, hashed, or tested.

Use `options` for tool settings such as regex patterns, indentation, alpha values, or generation settings.

The demo values are synthetic and safe for testing the remote endpoint; replace them with user data only after the privacy check above is satisfied.

## Output Schema

```json
{
  "type": "object",
  "description": "Machine-readable result. The same value is also available as content[0].text for human-readable MCP clients.",
  "properties": {
    "result": {
      "type": "string",
      "description": "Path-by-path JSON diff summary."
    }
  },
  "required": [
    "result"
  ],
  "additionalProperties": false
}
```

## Example Arguments

```json
{
  "input": "{\"user\":{\"name\":\"Alice\",\"role\":\"admin\"}}",
  "options": {
    "compareTo": "{\"user\":{\"name\":\"Alice\",\"role\":\"editor\"}}"
  }
}
```

## Example tools/call

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "json-diff",
    "arguments": {
        "input": "{\"user\":{\"name\":\"Alice\",\"role\":\"admin\"}}",
        "options": {
            "compareTo": "{\"user\":{\"name\":\"Alice\",\"role\":\"editor\"}}"
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/json-diff.html

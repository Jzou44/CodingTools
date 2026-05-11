---
name: coding-tools-regex-replace
description: "Use when Codex needs to run the Coding.Tools Regex Replace MCP tool (regex-replace) through tools/list and tools/call for Find and replace text using regular expressions with backreference support."
---

# Regex Replace

Use the Coding.Tools MCP tool `regex-replace` when the user needs: Find and replace text using regular expressions with backreference support.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `regex-replace`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `regex-replace`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "regex-replace"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for Regex Replace.",
  "properties": {
    "input": {
      "type": "string",
      "description": "Text to search and replace using options.pattern."
    },
    "options": {
      "type": "object",
      "properties": {
        "pattern": {
          "type": "string",
          "description": "Regular expression pattern without slash delimiters."
        },
        "replacement": {
          "type": "string",
          "default": "",
          "description": "Replacement text. JavaScript backreferences such as $1 are supported."
        },
        "flags": {
          "type": "string",
          "default": "g",
          "description": "JavaScript regex flags, for example g, i, m, s, u, y."
        }
      },
      "required": [
        "pattern"
      ],
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "input": "Ticket ABC-123 is ready for review",
      "options": {
        "pattern": "[A-Z]{3}-\\d{3}",
        "replacement": "[ticket-id]",
        "flags": "g"
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
      "description": "Result from Regex Replace."
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
  "input": "Ticket ABC-123 is ready for review",
  "options": {
    "pattern": "[A-Z]{3}-\\d{3}",
    "replacement": "[ticket-id]",
    "flags": "g"
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
    "name": "regex-replace",
    "arguments": {
        "input": "Ticket ABC-123 is ready for review",
        "options": {
            "pattern": "[A-Z]{3}-\\d{3}",
            "replacement": "[ticket-id]",
            "flags": "g"
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/regex-replace.html

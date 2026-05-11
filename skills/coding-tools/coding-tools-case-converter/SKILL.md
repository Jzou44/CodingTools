---
name: coding-tools-case-converter
description: "Use when Codex needs to run the Coding.Tools Case Converter MCP tool (case-converter) through tools/list and tools/call for Convert text to uppercase, lowercase, sentence case, title case, or invert case."
---

# Case Converter

Use the Coding.Tools MCP tool `case-converter` when the user needs: Convert text to uppercase, lowercase, sentence case, title case, or invert case.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `case-converter`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `case-converter`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "case-converter"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for Case Converter.",
  "properties": {
    "input": {
      "type": "string",
      "description": "Text whose case should be converted."
    },
    "options": {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "all",
            "uppercase",
            "lowercase",
            "title",
            "sentence",
            "inverted"
          ],
          "default": "all",
          "description": "Case conversion mode."
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "input": "quarterly revenue report",
      "options": {
        "mode": "title"
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
  "oneOf": [
    {
      "type": "object",
      "description": "All case conversions when options.mode is all.",
      "properties": {
        "uppercase": {
          "type": "string"
        },
        "lowercase": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "sentence": {
          "type": "string"
        },
        "inverted": {
          "type": "string"
        }
      },
      "required": [
        "uppercase",
        "lowercase",
        "title",
        "sentence",
        "inverted"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "description": "Single case conversion when options.mode selects one mode.",
      "properties": {
        "mode": {
          "type": "string"
        },
        "result": {
          "type": "string"
        }
      },
      "required": [
        "mode",
        "result"
      ],
      "additionalProperties": false
    }
  ]
}
```

## Example Arguments

```json
{
  "input": "quarterly revenue report",
  "options": {
    "mode": "title"
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
    "name": "case-converter",
    "arguments": {
        "input": "quarterly revenue report",
        "options": {
            "mode": "title"
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/case-converter.html

---
name: coding-tools-hex-to-rgba
description: "Use when Codex needs to run the Coding.Tools Hex to RGBA MCP tool (hex-to-rgba) through tools/list and tools/call for Convert hex color codes to RGBA format with opacity control."
---

# Hex to RGBA

Use the Coding.Tools MCP tool `hex-to-rgba` when the user needs: Convert hex color codes to RGBA format with opacity control.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `hex-to-rgba`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `hex-to-rgba`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "hex-to-rgba"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for Hex to RGBA.",
  "properties": {
    "input": {
      "type": "string",
      "description": "Hex color such as #3366CC or #3366CCAA."
    },
    "options": {
      "type": "object",
      "properties": {
        "alpha": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Alpha value to use when the hex input does not include one."
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "input": "#3366CC",
      "options": {
        "alpha": 0.65
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
  "description": "RGBA channel object. The CSS rgba(...) string is also available in content[0].text.",
  "properties": {
    "r": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "g": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "b": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "a": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "r",
    "g",
    "b",
    "a"
  ],
  "additionalProperties": false
}
```

## Example Arguments

```json
{
  "input": "#3366CC",
  "options": {
    "alpha": 0.65
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
    "name": "hex-to-rgba",
    "arguments": {
        "input": "#3366CC",
        "options": {
            "alpha": 0.65
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/hex-to-rgba.html

---
name: coding-tools-rgb-to-hex
description: "Use when Codex needs to run the Coding.Tools RGB to Hex MCP tool (rgb-to-hex) through tools/list and tools/call for Convert RGB color values to hex color codes with live preview."
---

# RGB to Hex

Use the Coding.Tools MCP tool `rgb-to-hex` when the user needs: Convert RGB color values to hex color codes with live preview.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `rgb-to-hex`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `rgb-to-hex`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "rgb-to-hex"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for RGB to Hex.",
  "properties": {
    "input": {
      "oneOf": [
        {
          "type": "string",
          "description": "CSS rgb(...) or rgba(...) color string."
        },
        {
          "type": "object",
          "description": "RGB color object.",
          "properties": {
            "r": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255,
              "description": "Red channel."
            },
            "g": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255,
              "description": "Green channel."
            },
            "b": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255,
              "description": "Blue channel."
            }
          },
          "required": [
            "r",
            "g",
            "b"
          ],
          "additionalProperties": false
        }
      ]
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
      "input": {
        "r": 51,
        "g": 102,
        "b": 204
      }
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
  "description": "Machine-readable result. The same value is also available as content[0].text for human-readable MCP clients.",
  "properties": {
    "result": {
      "type": "string",
      "description": "Hex color string in #RRGGBB format."
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
  "input": {
    "r": 51,
    "g": 102,
    "b": 204
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
    "name": "rgb-to-hex",
    "arguments": {
        "input": {
            "r": 51,
            "g": 102,
            "b": 204
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/rgb-to-hex.html

---
name: coding-tools-image-to-base64
description: "Use when Codex needs to run the Coding.Tools Image to Base64 MCP tool (image-to-base64) through tools/list and tools/call for Convert any image to a Base64 encoded data URI string."
---

# Image to Base64

Use the Coding.Tools MCP tool `image-to-base64` when the user needs: Convert any image to a Base64 encoded data URI string.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `image-to-base64`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `image-to-base64`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "image-to-base64"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for Image to Base64.",
  "properties": {
    "input": {
      "oneOf": [
        {
          "type": "string",
          "description": "Public image URL, data URI, or raw Base64 image bytes."
        },
        {
          "type": "object",
          "description": "Image input object.",
          "properties": {
            "url": {
              "type": "string",
              "description": "Public http/https image URL."
            },
            "imageUrl": {
              "type": "string",
              "description": "Alias for url."
            },
            "base64": {
              "type": "string",
              "description": "Raw Base64 image bytes."
            },
            "data": {
              "type": "string",
              "description": "Raw Base64 image bytes or data URI."
            },
            "mimeType": {
              "type": "string",
              "description": "MIME type for raw Base64 image bytes."
            }
          },
          "additionalProperties": false
        }
      ]
    },
    "options": {
      "type": "object",
      "properties": {
        "mimeType": {
          "type": "string",
          "description": "MIME type to use when input is raw Base64 bytes, for example image/png."
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "input": {
        "url": "https://coding.tools/assets/img/photo2pixel-demo.png"
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
      "description": "Image data URI string."
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
    "url": "https://coding.tools/assets/img/photo2pixel-demo.png"
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
    "name": "image-to-base64",
    "arguments": {
        "input": {
            "url": "https://coding.tools/assets/img/photo2pixel-demo.png"
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/image-to-base64.html

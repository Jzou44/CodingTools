---
name: coding-tools-url-encode
description: "Use when Codex needs to run the Coding.Tools URL Encode MCP tool (url-encode) through tools/list and tools/call for Percent-encode URL text, query values, paths, or full URLs."
---

# URL Encode

Use the Coding.Tools MCP tool `url-encode` when the user needs: Percent-encode URL text, query values, paths, or full URLs.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `url-encode`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `url-encode`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "url-encode"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for URL Encode.",
  "properties": {
    "input": {
      "type": "string",
      "description": "Text, URL component, path, query value, or full URL to percent-encode."
    },
    "options": {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "component",
            "uri"
          ],
          "default": "component",
          "description": "Use component for query values; use uri to preserve full URL separators."
        },
        "spaceAsPlus": {
          "type": "boolean",
          "default": false,
          "description": "Convert encoded spaces from %20 to + for form-style query strings."
        },
        "lineByLine": {
          "type": "boolean",
          "default": false,
          "description": "Encode each input line independently."
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "input": "hello world & tea=green",
      "options": {
        "mode": "component",
        "spaceAsPlus": false
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
      "description": "Percent-encoded URL text."
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
  "input": "hello world & tea=green",
  "options": {
    "mode": "component",
    "spaceAsPlus": false
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
    "name": "url-encode",
    "arguments": {
        "input": "hello world & tea=green",
        "options": {
            "mode": "component",
            "spaceAsPlus": false
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/url-encode.html

---
name: coding-tools-password-generator
description: "Use when Codex needs to run the Coding.Tools Password Generator MCP tool (password-generator) through tools/list and tools/call for Generate strong random passwords with customizable options."
---

# Password Generator

Use the Coding.Tools MCP tool `password-generator` when the user needs: Generate strong random passwords with customizable options.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `password-generator`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `password-generator`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "password-generator"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Arguments for Password Generator.",
  "properties": {
    "options": {
      "type": "object",
      "description": "Password generation settings.",
      "properties": {
        "length": {
          "type": "integer",
          "minimum": 8,
          "maximum": 128,
          "default": 16,
          "description": "Password length."
        },
        "uppercase": {
          "type": "boolean",
          "default": true,
          "description": "Include uppercase letters A-Z."
        },
        "lowercase": {
          "type": "boolean",
          "default": true,
          "description": "Include lowercase letters a-z."
        },
        "numbers": {
          "type": "boolean",
          "default": true,
          "description": "Include digits 0-9."
        },
        "symbols": {
          "type": "boolean",
          "default": true,
          "description": "Include punctuation symbols."
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "examples": [
    {
      "options": {
        "length": 20,
        "symbols": true
      }
    }
  ]
}
```

## Argument Guidance

Pass only the JSON object shown in Example Arguments as `tools/call.params.arguments`; do not include the outer JSON-RPC envelope inside `arguments`.

This tool is controlled by `options`; omit `input` unless a future `tools/list` schema adds it.

Use `options` for tool settings such as regex patterns, indentation, alpha values, or generation settings.

The demo values are synthetic and safe for testing the remote endpoint; replace them with user data only after the privacy check above is satisfied.

## Output Schema

```json
{
  "type": "object",
  "description": "Generated password result.",
  "properties": {
    "password": {
      "type": "string",
      "description": "Generated password."
    },
    "generated": {
      "type": "boolean",
      "description": "True when generation succeeded."
    }
  },
  "required": [
    "password",
    "generated"
  ],
  "additionalProperties": false
}
```

## Example Arguments

```json
{
  "options": {
    "length": 20,
    "symbols": true
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
    "name": "password-generator",
    "arguments": {
        "options": {
            "length": 20,
            "symbols": true
        }
    }
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/password-generator.html

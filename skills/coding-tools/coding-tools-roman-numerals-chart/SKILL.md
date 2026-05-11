---
name: coding-tools-roman-numerals-chart
description: "Use when Codex needs to run the Coding.Tools Roman Numerals Chart MCP tool (roman-numerals-chart) through tools/list and tools/call for View a complete Roman numerals reference chart from 1 to 1000."
---

# Roman Numerals Chart

Use the Coding.Tools MCP tool `roman-numerals-chart` when the user needs: View a complete Roman numerals reference chart from 1 to 1000.

## Endpoint

Use `https://coding.tools/mcp` for production. If the user is testing a local Docker container, use `http://localhost:8080/mcp`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool `roman-numerals-chart`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as `http://localhost:8080/mcp`.

## Workflow

1. Connect to the MCP endpoint.
2. Call `tools/list`.
3. Find the tool whose `name` is `roman-numerals-chart`.
4. Build `tools/call.params.arguments` from the discovered `inputSchema`. Start from the example below when the user does not provide a more specific value.
5. Call `tools/call` with `params.name = "roman-numerals-chart"`.
6. If `result.isError` is `false`, read `result.content[0].text` for display and `result.structuredContent` for programmatic parsing.
7. If `result.isError` is `true`, report the error text and include the returned `resource_link` when present.

## Input Schema

```json
{
  "type": "object",
  "description": "Roman Numerals Chart does not require arguments.",
  "properties": {},
  "additionalProperties": false,
  "examples": [
    {}
  ]
}
```

## Argument Guidance

This is a fixed reference tool and does not need user input. Use an empty arguments object `{}`; the returned `structuredContent` contains the reference rows.

## Output Schema

```json
{
  "type": "array",
  "description": "Roman numeral reference rows.",
  "items": {
    "type": "object",
    "properties": {
      "value": {
        "type": "integer"
      },
      "numeral": {
        "type": "string"
      }
    },
    "required": [
      "value",
      "numeral"
    ],
    "additionalProperties": false
  }
}
```

## Example Arguments

```json
{}
```

## Example tools/call

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "roman-numerals-chart",
    "arguments": {}
  }
}
```

## Notes

This tool can run directly through MCP. Prefer `result.structuredContent` for downstream automation and `result.content[0].text` for human-readable output.

Web UI: https://coding.tools/roman-numerals-chart.html

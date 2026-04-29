---
name: custom-debug-skill
description: Use when the user wants to debug or test a local web page by stopping the current dev server, starting a fresh one, opening it in Chrome DevTools MCP, and running tests or inspections on the page.
---

# Debug Skill

## Overview

A workflow for restarting a local dev server and testing a specific page using Chrome DevTools MCP. Ensures a clean server state before browser-based testing.

## When to Use

- User asks to "debug", "test", or "check" a local web page
- User wants to restart the dev server and inspect a page
- User mentions Chrome DevTools MCP for testing
- User wants to verify translations, UI, or functionality on a local page

## Workflow

### Step 1: Stop existing server on port 5500

```bash
# Kill any process using port 5500
lsof -ti:5500 | xargs kill -9 2>/dev/null || true
# Windows alternative:
# powershell "Get-NetTCPConnection -LocalPort 5500 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"
```

### Step 2: Start dev server

```bash
npm run dev
```

Wait for the server to be ready (look for "Server at http://localhost:5500" in output). Use `run_in_background` so it doesn't block.

### Step 3: Open page with Chrome DevTools MCP

Use `navigate_page` or `new_page` to open the target URL:

```
mcp__plugin_chrome-devtools-mcp_chrome-devtools__navigate_page
  type: "url"
  url: "http://localhost:5500/<path>"
```

### Step 4: Test / Inspect

Depending on the task:
- **Translation check**: `take_snapshot` → review text content for untranslated strings
- **Visual check**: `take_screenshot` → review layout/rendering
- **Interaction test**: `click`, `fill`, `type_text` → verify behavior
- **Console errors**: `list_console_messages` → check for JS errors
- **Network issues**: `list_network_requests` → check for failed requests

## Quick Reference

| Task | Tool |
|------|------|
| Stop server | `lsof -ti:5500 \| xargs kill -9` |
| Start server | `npm run dev` (background) |
| Open page | `navigate_page` (url) |
| Read page content | `take_snapshot` |
| Visual inspection | `take_screenshot` |
| Check for errors | `list_console_messages` |
| Check network | `list_network_requests` |
| Interact | `click`, `fill`, `type_text` |

## Common Mistakes

- **Server not ready**: Wait for "Server at" message before opening browser
- **Wrong port**: Project uses port 5500, not 3000 or 8080
- **Snapshot stale**: Take a fresh snapshot after any page interaction
- **Forgetting background**: Use `run_in_background` for `npm run dev` to avoid blocking

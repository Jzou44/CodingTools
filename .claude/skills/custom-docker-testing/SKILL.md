---
name: custom-docker-testing
description: Use when the user wants to build, run, or test the Coding.Tools Docker container locally
---

# Docker Testing

Build and run the Coding.Tools Docker container locally for testing and preview.

## Overview

This skill provides a workflow for testing the Docker deployment locally. It builds the static site with Eleventy, packages it with nginx, and serves it on localhost.

## When to Use

- User asks to test Docker build
- User wants to preview the site in Docker
- User needs to verify Docker deployment works
- Before pushing Docker changes to production

## Quick Reference

| Command | Description |
|---------|-------------|
| `npm run docker:build` | Build Docker image |
| `npm run docker:run` | Run container on port 8080 |
| `npm run docker:stop` | Stop and remove container |
| `npm run docker:test` | Build and run (combined) |

## Implementation

### Step 1: Build the image

```bash
docker build -t coding-tools .
```

### Step 2: Run the container

```bash
docker run -d --name coding-tools-test -p 8080:80 coding-tools
```

### Step 3: Verify it's running

```bash
docker ps | grep coding-tools-test
```

### Step 4: Open in browser

Navigate to: http://localhost:8080

### Step 5: View logs (if needed)

```bash
docker logs -f coding-tools-test
```

### Step 6: Stop and cleanup

```bash
docker stop coding-tools-test && docker rm coding-tools-test
```

## Common Mistakes

**Port already in use:**
```bash
# Use a different port
docker run -d --name coding-tools-test -p 3000:80 coding-tools
```

**Build fails:**
- Check that `src/` directory exists
- Verify `package.json` has correct dependencies
- Run `npm install` locally first

**Container won't start:**
```bash
# Check container logs
docker logs coding-tools-test

# Enter container shell for debugging
docker exec -it coding-tools-test sh
```

## Rebuild and Restart

One command to rebuild and restart:

```bash
docker stop coding-tools-test 2>/dev/null; docker rm coding-tools-test 2>/dev/null; docker build -t coding-tools . && docker run -d --name coding-tools-test -p 8080:80 coding-tools
```

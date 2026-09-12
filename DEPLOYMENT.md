# GitHub Actions Deployment

Production deploys are handled by `.github/workflows/deploy.yml`.

## Flow

1. A push to `master` or a manual `workflow_dispatch` run starts the workflow.
2. The `build` job runs `npm ci` and `npm run build` on a GitHub-hosted runner.
3. The `deploy` job connects to the VPS over SSH.
4. The VPS checks out the exact Git commit that triggered the workflow.
5. The VPS runs `npm ci` and `npm run build`.
6. The generated `dist/` files are synced to the nginx web root.
7. The `coding-tools-a2a` systemd service is installed or restarted.
8. nginx is reloaded to serve static files and proxy `/a2a/*` and `/mcp` to the runtime.
9. The workflow verifies local nginx, `/.well-known/agent-card.json`, `/a2a/healthz`, MCP `tools/call`, and the public URL.

## Static asset optimization

`npm run build` minifies CSS/JavaScript and rewrites generated HTML to use
content-hashed filenames. `dist/asset-manifest.json` maps the source URLs to
their optimized URLs. Stable filenames remain available for dynamic loaders.
Deploy the entire `dist/` directory, including the hashed files. Development
with `npm run dev` continues to serve readable source assets.

Both nginx configurations enable gzip, cache hashed CSS/JS for one year,
cache unversioned static assets for one hour, and revalidate HTML/JSON.
The agent card keeps its existing five-minute cache. Apply the nginx config
as well as the generated files to get compression and caching improvements.
Google Fonts loads asynchronously so the initial render can use fallback fonts.

`npm run test:assets` checks minification, browser globals, localized resource
rewriting, and cache invalidation; it also runs as part of `npm run check`.

## Required Repository Secret

- `VPS_SSH_KEY`: private SSH key that can log in to the VPS user.

## Optional Repository Secrets

Defaults match the current Google Cloud VPS:

- `VPS_HOST`: default `35.239.243.94`
- `VPS_USER`: default `bylearner`
- `VPS_PORT`: default `22`
- `VPS_PATH`: default `/home/bylearner/app/CodingTools`
- `WEB_ROOT`: default `/var/www/coding-tools`
- `PUBLIC_URL`: default `http://35.239.243.94/`

## VPS Requirements

- The VPS user can pull `git@github.com:Jzou44/CodingTools.git`.
- Node.js and npm are available, either globally or through `~/.nvm/nvm.sh`.
- `rsync` is installed on the VPS.
- The VPS user has passwordless sudo for `nginx -t`, `systemctl reload nginx`, and managing the `coding-tools-a2a` systemd service.
- nginx is installed and listens on port 80.

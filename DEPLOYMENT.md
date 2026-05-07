# GitHub Actions Deployment

Production deploys are handled by `.github/workflows/deploy.yml`.

## Flow

1. A push to `master` or a manual `workflow_dispatch` run starts the workflow.
2. The `build` job runs `npm ci` and `npm run build` on a GitHub-hosted runner.
3. The `deploy` job connects to the VPS over SSH.
4. The VPS checks out the exact Git commit that triggered the workflow.
5. The VPS runs `npm ci` and `npm run build`.
6. The generated `dist/` files are synced to the nginx web root.
7. nginx is reloaded to serve the synced static files directly.
8. The workflow verifies both local nginx on the VPS and the public URL.

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
- The VPS user has passwordless sudo for `nginx -t` and `systemctl reload nginx`.
- nginx is installed and listens on port 80.

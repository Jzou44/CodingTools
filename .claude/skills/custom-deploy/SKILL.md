---
name: custom-deploy
description: Use when the user wants to deploy CodingTools to the remote VPS — handles SSH login, nvm env sourcing, Eleventy server start on port 8080, and nginx reverse proxy on port 80.
---

# Custom Deploy Skill

## Overview

Deploy CodingTools to the Google Cloud VPS. Starts Eleventy dev server on port 8080 and configures nginx to reverse proxy port 80 → 8080.

## When to Use

- User asks to "deploy", "push to VPS", "deploy to google-vps", or "restart server on VPS"
- User wants to set up the CodingTools site on the remote instance

## Prerequisites

- SSH key: `~/.ssh/id_ed25519`
- Remote user: `bylearner`
- VPS IP: `35.239.243.94` (may change after reboot — ask user if connection fails)
- Project path on VPS: `~/app/CodingTools`
- nvm installed at `~/.nvm/nvm.sh`

## Workflow

### Step 1: Test SSH and sudo

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "sudo whoami"
```

Expected output: `root`. If `Permission denied (publickey)`, instruct the user to add their public key via Google Cloud Console SSH.

### Step 2: Kill existing Eleventy process on port 8080

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "pkill -f 'eleventy.*serve' 2>/dev/null; echo DONE"
```

### Step 3: Pull latest code on VPS

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "cd ~/app/CodingTools && git pull 2>&1"
```

Expected: `Already up to date.` or a list of updated files. If `git pull` fails due to unstaged changes, run:
```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "cd ~/app/CodingTools && git checkout -- . && git pull"
```

### Step 4: Start Eleventy on port 8080

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 'bash -c "source ~/.nvm/nvm.sh && cd ~/app/CodingTools && nohup npx @11ty/eleventy --serve --port=8080 > /tmp/eleventy.log 2>&1 &"'
```

Wait ~5 seconds, then verify:

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "curl -s -o /dev/null -w 'HTTP_%{http_code}' http://localhost:8080/"
```

Expected: `HTTP_200`.

### Step 5: Configure nginx reverse proxy

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "sudo tee /etc/nginx/sites-available/default << 'EOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection \"upgrade\";
    }
}
EOF
"
```

### Step 6: Test and reload nginx

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "sudo nginx -t 2>&1 && sudo systemctl reload nginx 2>&1"
```

### Step 7: Verify end-to-end

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no bylearner@35.239.243.94 "curl -s -o /dev/null -w 'HTTP_%{http_code}' http://localhost:80/"
```

Expected: `HTTP_200`.

## Quick Reference

| Step | Command |
|------|---------|
| Stop old server | `pkill -f 'eleventy.*serve'` |
| Pull latest | `cd ~/app/CodingTools && git pull` |
| Start Eleventy 8080 | `source ~/.nvm/nvm.sh && npx @11ty/eleventy --serve --port=8080` (background) |
| Nginx config | `/etc/nginx/sites-available/default` → proxy_pass 8080 |
| Reload nginx | `sudo nginx -t && sudo systemctl reload nginx` |
| Verify | `curl http://localhost:80/` → 200 |

## Common Mistakes

- **nvm not sourced**: Non-interactive SSH shells don't load nvm. Always use `bash -c "source ~/.nvm/nvm.sh && ..."` or `bash -l -c`.
- **Eleventy not ready**: Wait a few seconds after starting before checking port 8080.
- **Nginx port conflict**: Port 80 must not be occupied by another process. If needed, kill first: `sudo fuser -k 80/tcp`.
- **VPS IP changed**: Google Cloud instances may get new IPs after reboot. Check/update or ask user for the new IP.
- **Background commands**: Use `run_in_background` for Eleventy start to avoid blocking.

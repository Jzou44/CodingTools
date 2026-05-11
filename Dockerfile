# Stage 1: Build static site
FROM node:24-alpine AS builder

WORKDIR /app
ARG SITE_BASE_URL=https://coding.tools
ENV SITE_BASE_URL=$SITE_BASE_URL

# Install dependencies
COPY package.json package-lock.json ./
RUN npm ci

# Copy source files
COPY .eleventy.js ./
COPY scripts/ scripts/
COPY server/ server/
COPY skills/ skills/
COPY src/ src/

# Build static site
RUN npm run build

# Stage 2: Serve static files with nginx and run the A2A runtime
FROM node:24-alpine

RUN apk add --no-cache nginx

WORKDIR /app
ARG SITE_BASE_URL=https://coding.tools
ENV SITE_BASE_URL=$SITE_BASE_URL

# Copy runtime files and built static files
COPY server/ server/
COPY src/_data/ src/_data/
COPY scripts/docker-entrypoint.sh scripts/docker-entrypoint.sh
COPY docker/nginx.conf /etc/nginx/http.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

RUN mkdir -p /run/nginx

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD wget -q -O /dev/null http://127.0.0.1/ && wget -q -O /dev/null http://127.0.0.1/a2a/healthz || exit 1

CMD ["sh", "/app/scripts/docker-entrypoint.sh"]

#!/bin/sh
set -eu

A2A_HOST="${HOST:-127.0.0.1}"
A2A_PORT="${PORT:-5510}"

HOST="$A2A_HOST" PORT="$A2A_PORT" node /app/server/a2a-runtime.js &
a2a_pid="$!"

nginx -g "daemon off;" &
nginx_pid="$!"

shutdown() {
  kill "$nginx_pid" 2>/dev/null || true
  kill "$a2a_pid" 2>/dev/null || true
  wait "$nginx_pid" 2>/dev/null || true
  wait "$a2a_pid" 2>/dev/null || true
}

trap shutdown INT TERM

set +e
wait -n
status="$?"
set -e

shutdown
exit "$status"

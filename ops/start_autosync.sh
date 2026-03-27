#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE_DIR="$REPO_ROOT/state"
PID_FILE="$STATE_DIR/git_autosync.pid"
RUNNER="$REPO_ROOT/ops/git_autosync_loop.sh"
INTERVAL_SEC="${INTERVAL_SEC:-30}"

mkdir -p "$STATE_DIR"

if [[ -f "$PID_FILE" ]]; then
  existing_pid="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [[ -n "${existing_pid}" ]] && kill -0 "$existing_pid" >/dev/null 2>&1; then
    echo "autosync already running pid=${existing_pid}"
    exit 0
  fi
fi

nohup /bin/bash "$RUNNER" >/dev/null 2>&1 &
pid="$!"
echo "$pid" > "$PID_FILE"

echo "autosync started pid=${pid}"
echo "status: bash ops/status_autosync.sh"

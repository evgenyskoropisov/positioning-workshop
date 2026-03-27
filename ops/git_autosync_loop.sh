#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INTERVAL_SEC="${INTERVAL_SEC:-30}"
RUNNER="${RUNNER:-$REPO_ROOT/ops/git_autosync.sh}"
LOG_FILE="${LOG_FILE:-$REPO_ROOT/state/git_autosync.loop.log}"

mkdir -p "$(dirname "$LOG_FILE")"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] autosync loop started interval=${INTERVAL_SEC}s runner=${RUNNER}" >> "$LOG_FILE"

while true; do
  /bin/bash "$RUNNER" >> "$LOG_FILE" 2>&1 || true
  sleep "$INTERVAL_SEC"
done

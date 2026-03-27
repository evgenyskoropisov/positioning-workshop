#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_FILE="$REPO_ROOT/state/git_autosync.pid"

if [[ ! -f "$PID_FILE" ]]; then
  echo "autosync is not running"
  exit 0
fi

pid="$(cat "$PID_FILE" 2>/dev/null || true)"
if [[ -n "$pid" ]] && kill -0 "$pid" >/dev/null 2>&1; then
  kill "$pid"
  echo "autosync stopped pid=${pid}"
else
  echo "autosync pid file existed, but process was not running"
fi

rm -f "$PID_FILE"

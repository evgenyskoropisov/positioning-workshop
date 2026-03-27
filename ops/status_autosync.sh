#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE_DIR="$REPO_ROOT/state"
PID_FILE="$STATE_DIR/git_autosync.pid"

if [[ -f "$PID_FILE" ]]; then
  pid="$(cat "$PID_FILE" 2>/dev/null || true)"
else
  pid=""
fi

echo "repo: ${REPO_ROOT}"
echo "pid file: ${PID_FILE}"
echo "logs:"
echo "  ${STATE_DIR}/git_autosync.log"
echo "  ${STATE_DIR}/git_autosync.loop.log"
echo

if [[ -n "$pid" ]] && kill -0 "$pid" >/dev/null 2>&1; then
  echo "autosync running pid=${pid}"
else
  echo "autosync not running"
fi

echo
tail -n 40 "${STATE_DIR}/git_autosync.loop.log" 2>/dev/null || echo "no loop log yet"

#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
TARGET_BRANCH="${TARGET_BRANCH:-main}"
DRY_RUN="${DRY_RUN:-0}"
GIT_BIN="${GIT_BIN:-/usr/bin/git}"
LOG_FILE="${LOG_FILE:-$REPO_ROOT/state/git_autosync.log}"
export PATH="${PATH:-/usr/bin:/bin:/usr/sbin:/sbin}"
export TMPDIR="${TMPDIR:-/tmp}"
export HOME="${HOME:-/Users/$(id -un)}"
cd "$HOME" 2>/dev/null || cd /

mkdir -p "$(dirname "$LOG_FILE")"

log() {
  printf '%s %s\n' "[$(date '+%Y-%m-%d %H:%M:%S')]" "$*" >> "$LOG_FILE"
}

contains_stdin_pattern() {
  local pattern="$1"
  if command -v rg >/dev/null 2>&1; then
    rg -q -e "$pattern"
  else
    grep -E -q "$pattern"
  fi
}

repo_check_output="$("$GIT_BIN" -C "$REPO_ROOT" rev-parse --is-inside-work-tree 2>&1 || true)"
if [[ "$repo_check_output" != "true" ]]; then
  log "skip: repo unavailable rev_parse=${repo_check_output}"
  exit 0
fi

cd "$REPO_ROOT"

current_branch="$("$GIT_BIN" branch --show-current 2>/dev/null || true)"
if [[ "$current_branch" != "$TARGET_BRANCH" ]]; then
  log "skip: current branch '$current_branch' is not target '$TARGET_BRANCH'"
  exit 0
fi

if ! "$GIT_BIN" remote get-url origin >/dev/null 2>&1; then
  log "skip: remote origin is not configured"
  exit 0
fi

"$GIT_BIN" add -A -- .

if "$GIT_BIN" diff --cached --quiet; then
  log "no changes to sync"
  exit 0
fi

if "$GIT_BIN" diff --cached --name-only | contains_stdin_pattern '(^|/)\.env($|\.)'; then
  log "blocked: staged .env detected; unstaging"
  "$GIT_BIN" reset >/dev/null
  exit 1
fi

if "$GIT_BIN" diff --cached | contains_stdin_pattern '(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA|EC|OPENSSH|PRIVATE) KEY-----|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})'; then
  log "blocked: potential secret pattern detected; unstaging"
  "$GIT_BIN" reset >/dev/null
  exit 1
fi

commit_message="chore(sync): auto update $(date '+%Y-%m-%d %H:%M:%S %z')"

if [[ "$DRY_RUN" == "1" ]]; then
  log "dry-run: would commit and push"
  "$GIT_BIN" diff --cached --name-status >> "$LOG_FILE"
  "$GIT_BIN" reset >/dev/null
  exit 0
fi

"$GIT_BIN" commit -m "$commit_message" --no-verify >> "$LOG_FILE" 2>&1
"$GIT_BIN" push origin "$TARGET_BRANCH" >> "$LOG_FILE" 2>&1

log "sync complete"

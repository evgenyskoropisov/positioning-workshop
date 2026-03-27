#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.evgenyskoropisov.positioning_workshop.autosync"
PLIST_PATH="$HOME/Library/LaunchAgents/${LABEL}.plist"
RUNNER_HOME="$HOME/.local/bin/positioning_workshop_git_autosync.sh"
STATE_DIR="$REPO_ROOT/state"

echo "label: ${LABEL}"
echo "plist: ${PLIST_PATH}"
echo "runner: ${RUNNER_HOME}"
echo "repo:  ${REPO_ROOT}"
echo "logs:"
echo "  ${STATE_DIR}/git_autosync.log"
echo "  ${STATE_DIR}/git_autosync.out.log"
echo "  ${STATE_DIR}/git_autosync.err.log"
echo
launchctl print "gui/$(id -u)/${LABEL}" | sed -n '1,160p'

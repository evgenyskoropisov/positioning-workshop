#!/usr/bin/env bash
set -euo pipefail

LABEL="com.evgenyskoropisov.positioning_workshop.autosync"
PLIST_PATH="$HOME/Library/LaunchAgents/${LABEL}.plist"
RUNNER_HOME="$HOME/.local/bin/positioning_workshop_git_autosync.sh"

launchctl bootout "gui/$(id -u)" "$PLIST_PATH" >/dev/null 2>&1 || true
rm -f "$PLIST_PATH"
rm -f "$RUNNER_HOME"

echo "removed ${LABEL}"

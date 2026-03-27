#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.evgenyskoropisov.positioning_workshop.autosync"
PLIST_PATH="$HOME/Library/LaunchAgents/${LABEL}.plist"
RUNNER_HOME="$HOME/.local/bin/positioning_workshop_git_autosync.sh"
HOME_LOG_DIR="$HOME/.local/state/positioning-workshop-autosync"

echo "label: ${LABEL}"
echo "plist: ${PLIST_PATH}"
echo "runner: ${RUNNER_HOME}"
echo "repo:  ${REPO_ROOT}"
echo "logs:"
echo "  ${HOME_LOG_DIR}/git_autosync.log"
echo "  ${HOME_LOG_DIR}/git_autosync.out.log"
echo "  ${HOME_LOG_DIR}/git_autosync.err.log"
echo
launchctl print "gui/$(id -u)/${LABEL}" | sed -n '1,160p'

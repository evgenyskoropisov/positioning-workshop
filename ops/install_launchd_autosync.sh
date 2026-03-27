#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.evgenyskoropisov.positioning_workshop.autosync"
PLIST_PATH="$HOME/Library/LaunchAgents/${LABEL}.plist"
STATE_DIR="$REPO_ROOT/state"
RUNNER_SOURCE="$REPO_ROOT/ops/git_autosync.sh"
RUNNER_HOME="$HOME/.local/bin/positioning_workshop_git_autosync.sh"
OUT_LOG="$STATE_DIR/git_autosync.out.log"
ERR_LOG="$STATE_DIR/git_autosync.err.log"
INTERVAL_SEC="${INTERVAL_SEC:-30}"

mkdir -p "$HOME/Library/LaunchAgents" "$HOME/.local/bin" "$STATE_DIR"
cp "$RUNNER_SOURCE" "$RUNNER_HOME"
chmod +x "$RUNNER_SOURCE" "$RUNNER_HOME"

cat > "$PLIST_PATH" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${RUNNER_HOME}</string>
  </array>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key>
    <string>${HOME}</string>
    <key>REPO_ROOT</key>
    <string>${REPO_ROOT}</string>
    <key>TMPDIR</key>
    <string>/tmp</string>
    <key>TARGET_BRANCH</key>
    <string>main</string>
    <key>LOG_FILE</key>
    <string>${STATE_DIR}/git_autosync.log</string>
  </dict>
  <key>RunAtLoad</key>
  <true/>
  <key>StartInterval</key>
  <integer>${INTERVAL_SEC}</integer>
  <key>StandardOutPath</key>
  <string>${OUT_LOG}</string>
  <key>StandardErrorPath</key>
  <string>${ERR_LOG}</string>
</dict>
</plist>
PLIST

launchctl bootout "gui/$(id -u)" "$PLIST_PATH" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$(id -u)" "$PLIST_PATH"
launchctl kickstart -k "gui/$(id -u)/${LABEL}"

echo "installed ${LABEL}"
echo "plist: ${PLIST_PATH}"
echo "runner: ${RUNNER_HOME}"
echo "logs:  ${OUT_LOG}"
echo "       ${ERR_LOG}"

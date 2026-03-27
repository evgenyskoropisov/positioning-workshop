# Positioning Workshop

This workspace contains a standalone positioning product that can run as a Codex plugin and as a Claude Desktop extension.

The goal is to help founders, PMM, and GTM teams choose a sharper market position using evidence, tradeoffs, and team alignment instead of vague brand language.

## What exists now

- A repo-local Codex plugin scaffold
- A Claude Desktop extension source package
- A first working version of the core positioning skill
- Product principles and roadmap notes

## Product direction

The plugin is built around five priorities:

1. Evidence before opinion
2. Strategic tradeoffs before polish
3. Facts and bets kept separate
4. Team alignment made visible
5. Outputs that can be reused across website, sales, and investor workflows

## Current shape

The current version is centered on a core workshop skill plus a follow-on variants skill. Together they:

- reviews source material
- maps the competitive field and substitutes
- forces hard strategic choices
- generates multiple positioning routes
- turns the selected route into reusable messaging assets
- adapts a chosen position across segments and channels without losing the core spine
- persists workshop artifacts for reuse and later iteration

## Project docs

- [product-principles.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/product-principles.md)
- [roadmap.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/roadmap.md)
- [plugin-spec.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/plugin-spec.md)
- [artifact-pipeline.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/artifact-pipeline.md)
- [first-run-walkthrough.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/first-run-walkthrough.md)

## Example case

- [IncidentBridge example](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/examples/incidentbridge/README.md)

## Validation

Run:

```bash
python3 plugins/positioning-workshop/scripts/validate_plugin.py
```

## Install

### Codex

The Codex plugin lives at:

- [plugin.json](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/.codex-plugin/plugin.json)
- [plugin README](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/README.md)

### Claude Desktop

Build the Claude Desktop extension bundle:

```bash
python3 plugins/positioning-workshop/scripts/build_claude_extension.py
```

This writes two equivalent install artifacts to `plugins/positioning-workshop/dist/`:

- `positioning-workshop-claude-extension-v0.2.0.mcpb`
- `positioning-workshop-claude-extension-v0.2.0.dxt`

Recommended install flow:

1. Install or update Claude Desktop.
2. Open `Settings > Extensions`.
3. Open `Advanced settings`.
4. In `Extension Developer`, click `Install Extension...`
5. Select the generated `.dxt` file from `plugins/positioning-workshop/dist/`.
6. If Claude asks for a workshop directory, keep the default or choose your own writable folder.
7. Restart Claude Desktop if the extension appears installed but tools are not visible yet.

After install, Claude should have access to:

- workshop prompts
- workshop bootstrap and save tools
- bundled templates and fictional example references

Start here after install:

```text
Walk me through the built-in IncidentBridge example as if this were my first real use of the plugin.
```

## Claude Desktop build

Build a shareable `.mcpb` bundle for Claude Desktop:

```bash
python3 plugins/positioning-workshop/scripts/build_claude_extension.py
```

The build artifacts are written to `plugins/positioning-workshop/dist/`.

## Workshop bootstrap

Create a working folder for a company:

```bash
python3 plugins/positioning-workshop/scripts/bootstrap_workshop.py "Acme Cloud"
```

## Git Autosync

This repo includes a repo-local autosync loop that stages, commits, and pushes local changes on `main` every 30 seconds when there is something new to sync.

Start it with:

```bash
bash ops/start_autosync.sh
```

Check status with:

```bash
bash ops/status_autosync.sh
```

Stop it with:

```bash
bash ops/stop_autosync.sh
```

There is also an optional `launchd` setup under `ops/install_launchd_autosync.sh`, but the background loop is the reliable default for this repo right now.

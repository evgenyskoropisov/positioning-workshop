# Positioning Workshop Plugin

`positioning-workshop` is a structured market-positioning product that currently ships in two forms:

- a local Codex plugin
- a Claude Desktop extension source package that builds into an `.mcpb` bundle

It is designed for:

- founders refining a wedge
- PMM teams sharpening category language
- sales leaders needing a cleaner narrative
- early-stage teams aligning around one believable promise

## Core ideas

- start from source material and market signals
- treat substitutes and no-decision as real competition
- force one primary answer per strategic question
- score confidence in claims instead of hand-waving
- produce messaging assets that can actually be used

## First-release scope

- one workshop skill
- one variants skill
- source and market review
- strategic choice prompts
- route generation
- team alignment prompt pack
- final messaging pack
- persisted workshop artifacts
- reference templates for each workshop stage
- segment and channel variant generation
- local validation script for plugin integrity

## Next milestones

- confidence scoring by claim
- segment-specific variants
- optional citation mode
- lightweight templates for homepages and decks
- public-ready install polish for both clients

## Local validation

From the repo root:

```bash
python3 plugins/positioning-workshop/scripts/validate_plugin.py
```

## Install In Claude Desktop

Build the install bundle:

```bash
python3 plugins/positioning-workshop/scripts/build_claude_extension.py
```

This generates two equivalent bundle files under `plugins/positioning-workshop/dist/`:

- `positioning-workshop-claude-extension-v0.2.0.mcpb`
- `positioning-workshop-claude-extension-v0.2.0.dxt`

Use the `.dxt` file for the smoothest Claude Desktop install flow:

1. Open Claude Desktop.
2. Go to `Settings > Extensions`.
3. Open `Advanced settings`.
4. In `Extension Developer`, click `Install Extension...`
5. Choose the generated `.dxt` file.
6. Confirm the workshop directory setting if Claude prompts for it.
7. Restart Claude Desktop if the extension installs but its tools are not visible yet.

## Build Claude Desktop Extension

Create installable Claude Desktop bundles:

```bash
python3 plugins/positioning-workshop/scripts/build_claude_extension.py
```

The generated files land in `plugins/positioning-workshop/dist/`.

## Bootstrap a workshop

Create a reusable workshop folder from the reference templates:

```bash
python3 plugins/positioning-workshop/scripts/bootstrap_workshop.py "Acme Cloud"
```

This creates a numbered working pack under `plugins/positioning-workshop/workshops/<slug>/`.

## Example

A filled fictional example lives here:

- [incidentbridge/README.md](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/examples/incidentbridge/README.md)

## First-run walkthrough

If you want to see how the product should behave right after install, start here:

- [first-run-walkthrough.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/first-run-walkthrough.md)

It uses the fictional `IncidentBridge` example and includes:

- a copy-paste first prompt
- what the assistant should do next
- what result you should expect
- which files matter most after the run

## Artifact outputs

The workshop now persists four reusable artifacts under each workshop folder:

- `artifacts/decision-log.md`
- `artifacts/workshop-summary.json`
- `artifacts/claim-ledger.json`
- `artifacts/route-recommendation.md`

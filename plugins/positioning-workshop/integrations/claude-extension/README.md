# Positioning Workshop for Claude Desktop

This directory contains the Claude Desktop extension source for `positioning-workshop`.

It is packaged as an MCP bundle so the same product can be shared across:

- Codex, through the local plugin manifest
- Claude Desktop, through a one-click installable MCP extension

## What the extension includes

- a stdio MCP server implemented in Python stdlib
- bundled workshop docs, skills, templates, example output, and validated reference material
- prompts for full workshop runs and variant adaptation
- tools for bootstrapping workshops, listing workshops, and saving workshop files

## Build

From the repo root:

```bash
python3 plugins/positioning-workshop/scripts/build_claude_extension.py
```

The build artifact is written to `plugins/positioning-workshop/dist/`.

The build currently emits both:

- `.mcpb` as the canonical MCP bundle artifact
- `.dxt` as a Claude Desktop compatibility alias with identical contents

## Install in Claude Desktop

1. Build the bundle from the repo root.
2. Open Claude Desktop.
3. Go to `Settings > Extensions`.
4. Open `Advanced settings`.
5. In the `Extension Developer` section, click `Install Extension...`
6. Select the generated `.dxt` bundle from `plugins/positioning-workshop/dist/`
7. Review the extension settings and choose a writable workshop directory if Claude prompts for one.
8. Restart Claude Desktop if the extension installs but the tools do not show up immediately.

## First thing to test after install

Use the walkthrough here:

- [first-run-walkthrough.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/first-run-walkthrough.md)

That document gives you a clean first-run prompt, an expected outcome, and the key files to inspect after the walkthrough.

## Runtime notes

- The extension uses the local Python runtime.
- The manifest targets Python `>=3.8,<4.0`.
- User-created workshop files are stored outside the bundle in a writable workshop directory.
- The workshop directory defaults to `${HOME}/Documents/positioning-workshop-workshops` unless the Claude install flow overrides it.

## Included MCP surfaces

### Tools

- `bootstrap_workshop`
- `list_workshops`
- `save_workshop_file`

### Prompts

- `run_positioning_workshop`
- `adapt_positioning_variants`

### Resources

- product docs
- both skill definitions
- all workshop reference templates
- the IncidentBridge example
- the validated Mercuryo workshop

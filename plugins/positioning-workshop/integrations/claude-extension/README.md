# Positioning Workshop for Claude Desktop

This directory contains the Claude Desktop extension source for `positioning-workshop`.

It is packaged as an MCP bundle (`.mcpb`) so the same product can be shared across:

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

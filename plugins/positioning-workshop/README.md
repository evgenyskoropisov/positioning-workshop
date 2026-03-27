# Positioning Workshop Plugin

`positioning-workshop` is a local Codex plugin for structured market-positioning work.

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
- reference templates for each workshop stage
- segment and channel variant generation
- local validation script for plugin integrity

## Next milestones

- confidence scoring by claim
- segment-specific variants
- saved workshop outputs
- optional citation mode
- lightweight templates for homepages and decks

## Local validation

From the repo root:

```bash
python3 plugins/positioning-workshop/scripts/validate_plugin.py
```

## Bootstrap a workshop

Create a reusable workshop folder from the reference templates:

```bash
python3 plugins/positioning-workshop/scripts/bootstrap_workshop.py "Acme Cloud"
```

This creates a numbered working pack under `plugins/positioning-workshop/workshops/<slug>/`.

## Example

A filled fictional example lives here:

- [incidentbridge/README.md](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/examples/incidentbridge/README.md)

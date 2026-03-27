# Positioning Workshop

This workspace contains a standalone positioning plugin for Codex.

The goal is to help founders, PMM, and GTM teams choose a sharper market position using evidence, tradeoffs, and team alignment instead of vague brand language.

## What exists now

- A repo-local Codex plugin scaffold
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

## Project docs

- [product-principles.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/product-principles.md)
- [roadmap.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/roadmap.md)
- [plugin-spec.md](/Users/evgenyskoropisov/Documents/New%20project%2011/docs/plugin-spec.md)

## Example case

- [IncidentBridge example](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/examples/incidentbridge/README.md)

## Validation

Run:

```bash
python3 plugins/positioning-workshop/scripts/validate_plugin.py
```

## Workshop bootstrap

Create a working folder for a company:

```bash
python3 plugins/positioning-workshop/scripts/bootstrap_workshop.py "Acme Cloud"
```

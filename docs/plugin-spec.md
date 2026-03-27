# Plugin Spec

## Product summary

Positioning Workshop is a cross-client positioning product for turning scattered company context into a credible market position and a reusable messaging pack.

The initial supported surfaces are:

- a local Codex plugin
- a Claude Desktop extension built as an MCP bundle

## Primary users

- founders preparing a sharper narrative
- PMM teams refining category and wedge
- sales leaders improving top-of-funnel story
- early-stage teams aligning on what to say and what to stop saying

## Core job

Help a team choose one believable market position under evidence and market pressure.

## Input surface

The product should work with:

- plain-language company descriptions
- website URLs
- decks
- memos
- notes
- pasted team replies

## Main workflow

1. Build an evidence file from user input and source material.
2. Build a market pressure map across competitors, substitutes, and no-decision.
3. Force a strategic spine across buyer, trigger, wedge, proof, category, and boundary.
4. Generate three narrative routes.
5. Run a friction test on believability, repeatability, and exclusion.
6. Create a team pulse packet.
7. Produce a final messaging pack.
8. Adapt the approved position across segments or channels without breaking the core narrative.
9. Persist reusable workshop artifacts for resumption, audit, and downstream use.

## Client packaging

### Codex

- local plugin manifest under `.codex-plugin/plugin.json`
- skills exposed from `plugins/positioning-workshop/skills/`

### Claude Desktop

- installable `.mcpb` bundle
- stdio MCP server implemented in Python stdlib
- built-in tools for workshop bootstrap, workshop listing, and file persistence
- built-in prompts for full workshop runs and variant adaptation
- bundled static resources for docs, templates, example output, and validated workshop references

## Output contract

The default final pack should include:

1. one-line market position
2. category sentence
3. primary wedge
4. evidence ledger
5. homepage hero
6. three support bullets
7. sales opener
8. investor description
9. messaging guardrails

The workshop should also persist:

1. `artifacts/decision-log.md`
2. `artifacts/workshop-summary.json`
3. `artifacts/claim-ledger.json`
4. `artifacts/route-recommendation.md`

## Quality constraints

- claims must be tied to proof or marked as bets
- language should be buyer-readable
- substitutes must be treated as competition
- final positioning line must stay under 30 words
- outputs should be reusable without heavy rewriting

## Non-goals for v0.2

- not a brand voice system
- not a visual brand framework
- not a full copywriting suite
- not a CRM or research database

## Near-term build goals

- public-ready packaging for Codex and Claude
- stronger support for iterative revisions
- lightweight citation mode for evidence-backed claims
- short-form output packs for websites and decks

## Example artifact

The repo should include at least one filled end-to-end example so users can see the expected quality bar without running a live workshop first.

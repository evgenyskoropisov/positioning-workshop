# Plugin Spec

## Product summary

Positioning Workshop is a Codex plugin for turning scattered company context into a credible market position and a reusable messaging pack.

## Primary users

- founders preparing a sharper narrative
- PMM teams refining category and wedge
- sales leaders improving top-of-funnel story
- early-stage teams aligning on what to say and what to stop saying

## Core job

Help a team choose one believable market position under evidence and market pressure.

## Input surface

The plugin should work with:

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

## Non-goals for v0.1

- not a brand voice system
- not a visual brand framework
- not a full copywriting suite
- not a CRM or research database

## Near-term build goals

- structured reference templates for each stage
- validation script for plugin integrity
- workshop bootstrap script for session folders
- variants skill for segment and channel adaptation
- examples and reusable artifacts
- stronger support for iterative revisions

## Example artifact

The repo should include at least one filled end-to-end example so users can see the expected quality bar without running a live workshop first.

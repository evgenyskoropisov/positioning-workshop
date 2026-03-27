# Mercuryo Validation Notes

## Context

- Validation date: 2026-03-27
- Company used for the real-world run: Mercuryo.io
- Goal: test whether the positioning-workshop plugin can handle a multi-product, real-company web3 infrastructure business without collapsing into generic fintech language

## What worked

- The evidence-first flow forced a clean separation between public proof and attractive-but-weak brand language.
- The new artifact layer was useful in practice. `decision-log.md`, `workshop-summary.json`, `claim-ledger.json`, and `route-recommendation.md` made it much easier to hold decisions together than relying on a single messaging pack.
- The route scorecard was especially useful for Mercuryo because it exposed the core tension between safe proof-led messaging and sharper wedge-led messaging.

## What got messy

- Multi-product companies need an explicit "core offer" decision earlier in the workflow.
- Public-source validation made source handling matter more than the current templates do. Right now the proof is captured, but source attribution is still manual.
- The workflow can produce too much category language if the company already uses broad phrases like "engine", "gateway", or "infrastructure" without a concrete buyer outcome.

## Improvements worth making next

- Add an optional `company-brief.md` and `source-notes.md` step to the bootstrap flow.
- Add a strategic-spine decision for `Core offer` or `Primary job to be done` so broad product portfolios do not dominate the narrative.
- Consider extending `claim-ledger.json` with optional source URLs or source IDs.
- Add a short reminder in the main skill for multi-product companies: lead with one buyer problem, then let portfolio breadth support it.

## Net result

- The plugin handled Mercuryo well enough to produce a credible route recommendation and messaging pack.
- The real-world run strengthened the case for the artifact pipeline.
- The next plugin improvement should focus on source attribution and multi-product compression, not on generating more copy.

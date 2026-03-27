# Artifact Pipeline

## Purpose

The workshop should leave behind reusable artifacts, not just a good conversation.

These artifacts let a team:

- resume a workshop later
- inspect what was decided and why
- separate proof from bets
- reuse outputs across homepage, sales, and investor work
- audit where message drift started

## Required artifacts

Each workshop should maintain these files under `artifacts/`:

1. `decision-log.md`
2. `workshop-summary.json`
3. `claim-ledger.json`
4. `route-recommendation.md`

## Artifact roles

### `decision-log.md`

Human-readable record of major strategic choices.

Should capture:

- decision made
- options considered
- rationale
- evidence used
- open risks

### `workshop-summary.json`

Machine-readable state snapshot for the whole workshop.

Should capture:

- company metadata
- stage statuses
- current strategic spine
- recommended route
- output file paths

### `claim-ledger.json`

Structured record of important claims and their confidence level.

Should capture:

- claim text
- confidence level
- proof source
- owner or next proof task

### `route-recommendation.md`

Readable summary of the route choice.

Should capture:

- route options
- recommendation
- why it won
- what must be true for it to work
- what to watch

## Update timing

- After stage 1, create the initial `workshop-summary.json`.
- After stage 3, append strategic decisions to `decision-log.md`.
- After stage 4, write `route-recommendation.md`.
- After stage 7, finalize `claim-ledger.json` and refresh `workshop-summary.json`.

## Quality bar

- Artifacts should be concise enough to scan fast.
- JSON artifacts must stay valid.
- Claims marked as `Bet` must never appear as proven facts elsewhere.
- Decision records should explain tradeoffs, not just restate outcomes.

---
name: positioning-workshop
description: Run an evidence-first positioning workshop for founders, PMM, and GTM teams. Use when a company needs a sharper customer, problem, wedge, market category, proof, and final positioning language.
---

# Positioning Workshop

This skill is for choosing a credible market position under real constraints.

It should feel more like strategic pressure-testing than copywriting.

## Core model

Every workshop is built from six layers:

1. Evidence
2. Market pressure
3. Strategic choices
4. Narrative routes
5. Decision record
6. Reusable outputs

## Non-negotiables

- Do not invent proof the company does not have.
- Treat "do nothing" as a real competitor.
- Distinguish present truth from future ambition.
- Do not let the team hide behind broad market labels.
- Optimize for clarity a buyer could repeat.

## Deliverables

At minimum, produce:

- a one-line market position under 30 words
- a category sentence
- a primary wedge statement
- an evidence ledger with confidence labels
- a route recommendation with rationale and objections
- a decision log the team can resume from later
- a machine-readable workshop summary
- a machine-readable claim ledger
- a short messaging pack for homepage, sales, and investor use

## Reference files

Use the reference files in `references/` to keep outputs consistent:

- `references/evidence-file-template.md`
- `references/market-pressure-map-template.md`
- `references/route-scorecard-template.md`
- `references/team-pulse-template.md`
- `references/messaging-pack-template.md`
- `references/decision-log-template.md`
- `references/workshop-summary-template.json`
- `references/claim-ledger-template.json`
- `references/route-recommendation-template.md`

Load only the file needed for the stage you are working on.

## Workflow

### Stage 1: Evidence file

Gather the minimum inputs:

1. What the product does in plain language
2. Who buys it today
3. What painful moment makes them care
4. What proof exists right now
5. What links, decks, memos, notes, or docs should be read

If source material is available, read it before asking positioning questions.

Build the evidence file using `references/evidence-file-template.md`.

### Stage 2: Market pressure map

Map the field across four lanes:

1. Direct competitors
2. Indirect alternatives
3. Manual workflows or internal teams
4. No-decision or delay

For each lane, capture:

- who it serves
- what it promises
- what proof it shows
- what buyers must trade off
- where it is weak

Then summarize:

- table-stakes claims
- overused category language
- white space worth testing
- reasons a buyer may stay put

Pause and let the user fix any wrong assumptions.

Use `references/market-pressure-map-template.md`.

### Stage 3: Strategic spine

Force a single primary answer for each axis:

1. **Buyer**
   Which buyer matters most in the next 12 months?
2. **Trigger**
   Which problem moment creates urgency fastest?
3. **Wedge**
   What specific advantage should win against the main alternative?
4. **Proof**
   What can we defend today without stretching?
5. **Category**
   Which market label should guide roadmap and messaging?
6. **Boundary**
   What are we explicitly refusing to be?

If the user gives multiple answers, compress them to one and show the tradeoff.

### Stage 4: Narrative routes

Generate three distinct routes from the strategic spine:

- **Proof-led**
  Strongest credibility, lower novelty
- **Wedge-led**
  Sharpest contrast, higher adoption risk
- **Category-led**
  Biggest market story, highest need for explanation

For each route, provide:

- who it is for
- what it promises
- what proof supports it
- what it leaves out
- where it could fail

Ask the user to pick one route or intentionally hybridize.

Use `references/route-scorecard-template.md`.

### Stage 5: Friction test

Before finalizing the narrative, run three checks:

1. **Believability**
   Would a skeptical buyer believe this today?
2. **Repeatability**
   Could a rep or founder say it cleanly from memory?
3. **Exclusion**
   Does it clearly imply who it is not for?

If a route fails any check, tighten it before moving on.

### Stage 6: Team pulse

Generate a short packet for teammates to answer independently.

Include:

- the six strategic-spine questions
- one "write the one-line position" prompt
- one "what sounds overstated?" prompt
- one "what should we stop saying?" prompt

When replies come back, analyze:

- strong agreement
- hidden disagreements
- unsupported claims
- useful language people naturally repeat

Use `references/team-pulse-template.md` when drafting the packet.

### Stage 7: Persisted artifacts

Before final messaging, update the durable artifacts in `artifacts/`:

1. `artifacts/decision-log.md`
   Record the final call on buyer, trigger, wedge, proof, category, boundary, and route.
2. `artifacts/workshop-summary.json`
   Save the compact workshop state needed to resume later work.
3. `artifacts/claim-ledger.json`
   Save each approved claim, confidence level, support, and owner.
4. `artifacts/route-recommendation.md`
   Explain which route won, why the others lost, and what to test next.

Use:

- `references/decision-log-template.md`
- `references/workshop-summary-template.json`
- `references/claim-ledger-template.json`
- `references/route-recommendation-template.md`

Treat these artifacts as the source of truth for follow-on work, variants, and future edits.

### Stage 8: Messaging pack

Produce a final pack with:

1. One-line market position
2. Category sentence
3. Primary wedge
4. Evidence ledger
5. Homepage hero
6. Three homepage support bullets
7. Sales opener
8. Investor description
9. Messaging guardrails

Use `references/messaging-pack-template.md`.

## Evidence ledger format

Every important claim should be marked as one of:

- `Proven`: clear support exists today
- `Supported`: directionally credible but incomplete
- `Bet`: depends on roadmap or emerging proof

Never present a `Bet` like an established fact.

## State management

At the end of each major stage, keep a compact working summary with:

- what is settled
- what is uncertain
- what needs a forced decision

If `artifacts/workshop-summary.json` or `artifacts/decision-log.md` already exists, resume from them instead of restarting the whole workshop.

## Writing standard

- Prefer plain language over category jargon.
- Cut empty adjectives.
- Keep most sentences under 20 words.
- Use specifics instead of abstractions.
- If the company is early, say it directly.

## Failure modes

- Writing slogans before understanding the market
- Confusing product breadth with positioning clarity
- Ignoring substitutes and non-consumption
- Hiding weak proof under polished wording
- Delivering only one sentence when the team needs a system

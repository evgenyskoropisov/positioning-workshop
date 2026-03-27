# IncidentBridge: 01 Evidence File

## Product snapshot

- What the product does: Builds a causal incident timeline across deploys, flags, logs, support signals, and on-call actions.
- Current buyer: Head of Platform, Director of Engineering, or engineering manager owning reliability.
- Urgent problem moment: An incident is active, teams have alerts, but nobody can quickly reconstruct what changed and what likely caused the impact.
- Sales motion: Founder-led, top-down sale into engineering leadership with a pilot-first motion.
- Stage: Seed.

## ICP candidates

| Candidate | Why they fit | Urgency trigger | Confidence |
| --- | --- | --- | --- |
| B2B SaaS teams with 50-300 engineers | Enough complexity to feel tool sprawl, not enough staff to absorb slow investigations | Customer-facing outage or degraded release | High |
| Product-heavy SaaS teams using feature flags heavily | Need product and infra context in one thread | Incident tied to a feature rollout | High |
| Larger enterprise engineering orgs | Have serious pain, but buying cycles and integration expectations are heavier | Executive pressure after a visible incident | Medium |

## Pain inventory

| Pain | Who feels it | How often it shows up | Evidence |
| --- | --- | --- | --- |
| Too much time spent reconstructing what changed | On-call engineers and incident leads | Every serious incident | Strong |
| Product and infra evidence live in separate tools | Platform and product engineering managers | Frequent | Strong |
| Postmortems miss causality because the timeline is incomplete | Engineering leadership | After major incidents | Medium |

## Capability inventory

| Capability | Customer value | Differentiated or table stakes | Confidence |
| --- | --- | --- | --- |
| Cross-tool causal timeline | Gives one shared view of what changed and when | Differentiated | High |
| Correlates deploys, feature flags, and support spikes | Helps teams test the right hypothesis faster | Differentiated | Medium |
| Suggests next checks during investigation | Reduces analyst thrash | Emerging | Medium |
| Incident notes and exportable timeline | Improves handoff into postmortem | Table stakes | Medium |

## Proof inventory

| Claim | Evidence today | Confidence | Notes |
| --- | --- | --- | --- |
| Teams investigate incidents faster | Median investigation time fell by 42 percent across 3 paid pilots | `Supported` | Good early proof, still small sample |
| Product and infra context in one timeline improves coordination | Qualitative feedback from 9 design partners | `Supported` | Clear signal, not yet broad proof |
| IncidentBridge can become the system of record for incidents | No durable evidence yet | `Bet` | Too broad for current stage |
| Teams use the product weekly once deployed | 7 of 9 design partners used it during live incidents in the last month | `Supported` | Strong for stage |

## Pricing and packaging clues

- Pricing signal: Likely annual platform fee with tiering by engineering org size.
- Packaging signal: Sold as an incident investigation layer, not a full reliability platform.
- What the market may infer from pricing: Must show meaningful time savings fast or buyers will keep using existing tooling.

## Language already in use

- Repeated category words: incident investigation, causal timeline, engineering reliability
- Repeated promise words: faster diagnosis, less thrash, faster postmortems
- Words that sound inflated: autonomous root cause analysis, single source of truth for reliability

## Working summary

- Settled: The strongest pain is slow causal reconstruction after alerts fire.
- Uncertain: How broad the category story should be beyond investigation.
- Decision to force next: Whether to position narrowly on investigation or broadly on incident intelligence.

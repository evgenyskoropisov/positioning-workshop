# IncidentBridge: Decision Log

## Current state

- Selected route: Wedge-led
- Workshop status: Ready for variants and channel adaptation
- Decision owner: Founder plus GTM lead
- Last updated: 2026-03-27

## Strategic decisions

| Axis | Decision | Why this won | Alternatives rejected | Confidence |
| --- | --- | --- | --- | --- |
| Buyer | Head of Platform or engineering leader responsible for reliability in a B2B SaaS company | Pain is acute, measurable, and already visible in paid pilots | Broader CTO audience was too abstract for the current stage | High |
| Trigger | Live incident investigation when evidence is fragmented across tools | It is the fastest path to urgency and budget justification | Postmortem workflow was too retrospective and less urgent | High |
| Wedge | Causal cross-tool timeline for incident investigation | Strongest contrast versus dashboard-first observability and process-heavy incident tools | Generic AI diagnosis language was less credible and less ownable | High |
| Proof | Median investigation time reduced by 42 percent in paid pilots | Best quantified proof already available today | Broader claims about reliability outcomes need more time and data | Medium |
| Category | Incident investigation layer | Clear enough to explain the role without pretending to replace adjacent tools | Incident intelligence layer was more ambitious than the current proof supports | Medium |
| Boundary | Not a full observability suite and not an incident response orchestration tool | Keeps the story believable and avoids platform drift | Full-platform framing would inflate scope and invite wrong comparisons | High |
| Route | Wedge-led | Best balance of believability, contrast, and repeatability | Proof-led felt safer but less memorable; category-led overreached | High |

## Open questions

| Question | Why it matters | Owner | Next check |
| --- | --- | --- | --- |
| Which segment converts faster: 50 to 150 engineers or 150 to 300 engineers? | Affects ICP focus and outbound priority | GTM lead | After next 10 qualified opportunities |
| Which integration matters most in late-stage deals? | Shapes roadmap and enterprise objections | Founder | During pilot retrospectives |
| Can "incident investigation layer" be repeated without explanation on first touch? | Determines whether category language helps or slows adoption | PMM | In homepage and outbound tests |

## Risks to monitor

- Buyers may still assume this is just another observability add-on.
- Category language may drift broader than the product can defend today.
- Team may overstate AI or automation before proof is ready.

## Revisions

| Date | What changed | Why |
| --- | --- | --- |
| 2026-03-27 | Chose wedge-led route as default position | It offered the cleanest contrast without stretching proof |
| 2026-03-27 | Locked category to incident investigation layer | It stays focused while leaving room to mature later |

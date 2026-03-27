# First-Run Walkthrough

This is the fastest way to understand what `positioning-workshop` actually does after a fresh install.

Use this walkthrough before testing your own company.

## Goal

Start from a clean install and run one real example so you can see:

- what prompt to use
- what the assistant should do next
- what files it should create
- what kind of positioning output you should expect

## Recommended demo brand

Use `Mercuryo.io`.

Why this is a good first run:

- the repo already contains a validated workshop for it
- the company has enough product breadth to make the workflow interesting
- the resulting position is clear enough to judge quickly

## What a clean install gives you

After installing the plugin in Codex or the extension in Claude Desktop, the product should have access to:

- the workshop method
- the variants method
- the built-in reference templates
- the IncidentBridge example
- the Mercuryo validation workshop
- workshop bootstrap and file-save tools in Claude Desktop

## First-run prompt

Open a fresh conversation and paste this:

```text
Run a positioning workshop for Mercuryo.io.

Use the existing Mercuryo validation materials in the plugin as reference context, but act like this is my first live walkthrough.

I want you to:
1. explain the workflow as you go,
2. show me the main strategic decision points,
3. summarize the winning route in plain English,
4. show me the final one-line position, category sentence, and primary wedge,
5. tell me which files matter most if I want to inspect the result afterward.

Keep it practical and easy to follow.
```

## What should happen next

On a healthy run, the assistant should roughly do this:

1. Explain that it will start from evidence and market pressure before jumping to copy.
2. Read the existing Mercuryo workshop materials or bootstrap a fresh workshop if none exists.
3. Walk through the core tradeoffs:
   - buyer
   - trigger
   - wedge
   - proof
   - category
   - boundary
4. Compare multiple narrative routes.
5. Choose one route and explain why it won.
6. Produce a messaging pack you could actually reuse.

## What the winning answer should roughly sound like

The validated Mercuryo result currently lands here:

- One-line position: Mercuryo helps web3 apps keep users in-product across buy, sell, and spend through one crypto payment engine.
- Category: `web3 payment engine`
- Primary wedge: one embedded payment layer across buy, sell, and spend
- Winning route: `Wedge-led`

The core idea is that Mercuryo is strongest when framed as the embedded payment layer that keeps user activity inside the partner product, instead of as just another on-ramp provider.

## Which files matter most after the run

If you only inspect four files, make it these:

- [route-recommendation.md](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/workshops/mercuryo-io/artifacts/route-recommendation.md)
- [workshop-summary.json](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/workshops/mercuryo-io/artifacts/workshop-summary.json)
- [messaging-pack.md](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/workshops/mercuryo-io/05-messaging-pack.md)
- [variant-matrix.md](/Users/evgenyskoropisov/Documents/New%20project%2011/plugins/positioning-workshop/workshops/mercuryo-io/06-variant-matrix.md)

What each file tells you:

- `route-recommendation.md`: the strategic call and why the other routes lost
- `workshop-summary.json`: the compact source of truth
- `05-messaging-pack.md`: the reusable external-language output
- `06-variant-matrix.md`: how the core message flexes without drifting

## If you want to run your own brand next

After the Mercuryo walkthrough, open a new conversation and paste:

```text
Run a positioning workshop for [COMPANY NAME].

Start from evidence, not slogans.
If you need a model for the workflow and output quality, use the Mercuryo walkthrough pattern from the plugin.

I want:
1. an evidence file,
2. a market pressure map,
3. three route options,
4. one recommended route,
5. a final messaging pack,
6. the key artifact files updated so I can continue later.

Here is the source material:
[PASTE URLS, NOTES, DECK SUMMARY, OR RAW PRODUCT DESCRIPTION]
```

## What to judge on the first run

A good first run should feel like:

- it got narrower, not broader
- it forced a real tradeoff
- it separated proof from ambition
- it gave you a line a buyer could repeat
- it left behind files you can actually continue from

If the run only produces polished copy without a clear strategic choice, the workflow has drifted and should be tightened before broader use.

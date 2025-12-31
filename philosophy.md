# Philosophy

**Define how AI-assisted coding should think about HTMX.**

This repository is not a collection of snippets.  
It is not a tutorial.  
It is not a framework.

It is a set of **behavioral patterns (“skills”)** that encode correct, disciplined, and repeatable HTMX usage for large language models and humans alike.

---

## Core Belief

**HTMX works best when the server is responsible for state and flow.**

When AI assistants default to JavaScript-heavy solutions, they are not being clever; they are compensating for a lack of clear constraints.

This repository provides those constraints.

---

## Why Skills (Not Examples)

Examples show *what* to do.  
Skills define *how to think*.

AI models do not fail because they cannot write HTMX.
They fail because they lack:
- interaction discipline
- route responsibility clarity
- confidence in server-driven UI patterns

Each skill in this repository represents:
- a **single user intent**
- a **cohesive interaction flow**
- a **repeatable architectural decision**

---

## Server-Driven UI Is Not Optional Here

This repository assumes:
- HTML is the primary UI representation
- The server owns state transitions
- Routes have single, clear responsibilities
- UI updates are declarative, not imperative

If an interaction can be expressed as:
- “request → response → swap”

then JavaScript is unnecessary and therefore disallowed by default.

---

## JavaScript Policy

**JavaScript is forbidden by default.**

Not discouraged.  
Not optional.  
Forbidden.

Why:
- JavaScript hides state transitions
- JavaScript encourages client-side orchestration
- JavaScript becomes the escape hatch for unclear thinking

JavaScript may only appear when:
- HTMX primitives are provably insufficient
- The interaction cannot be modeled as server-rendered HTML swaps
- The exception is explicitly documented

If JavaScript feels “easier,” the design is usually wrong.

---

## No JSON APIs for UI Composition

Skills in this repository:
- do not return JSON for UI rendering
- do not rely on client-side templating
- do not require client-side state reconciliation

HTML is the contract.

If a response updates the UI, it returns HTML.

---

## Routes Are Part of the UI

In HTMX, routes are not a backend detail.

They define:
- interaction boundaries
- state transitions
- UI lifecycle

Each skill explicitly defines:
- which routes exist
- what each route is responsible for
- what each route must *not* do

Violating route discipline is considered a broken implementation.

---

## One Skill = One User Intent

Skills are not split by:
- HTTP method
- number of requests
- number of fragments
- implementation complexity

Skills are split by **user intent**.

If the user perceives an interaction as “one thing,” it is one skill.

---

## Skill Shape (At a Glance)

Each skill should make explicit:
- intent (what the user wants)
- constraints (what the solution must avoid)
- routes (what each endpoint owns)
- UI structure (fragments and swaps)
- success and failure states

Ambiguity is the enemy; the skill should remove it.

---

## What This Repository Is Not

This repository intentionally does **not** provide:
- full applications
- framework integrations
- CSS systems
- UI design guidance
- client-side state libraries

Those concerns distract from the core goal:
**teaching AI to behave correctly with HTMX**.

---

## Vendor Neutrality

Skills in this repository are:
- model-agnostic
- vendor-neutral
- expressed in plain language and structure

Adapters may exist for:
- Codex
- Claude
- OpenAI Chat
- MCP-based agents

Adapters translate skills.
They do not redefine them.

---

## Contribution Guidelines (Philosophical)

A contribution is acceptable if:
- it encodes a clear interaction pattern
- it can be applied repeatedly
- it removes the need for JavaScript
- it improves AI behavior, not just human convenience

A contribution will be rejected if:
- it introduces JS “just in case”
- it relies on frontend frameworks
- it obscures server responsibility
- it weakens the constraints of existing skills

Consistency matters more than completeness.

---

## The Goal

The ultimate goal of this repository is simple:

> If an AI model internalizes these skills,  
> it should **stop reaching for JavaScript by default**  
> and **start trusting the server again**.

Everything else is secondary.

# htmx-skills

**Opinionated, server-driven HTMX interaction skills for AI-assisted coding.**

`htmx-skills` is a collection of reusable interaction patterns (“skills”) designed to guide AI coding assistants toward **clean, server-driven HTMX solutions**, without defaulting to JavaScript or frontend frameworks.

This repository encodes *how to think* about HTMX—not just how to write it.

---

## Why This Exists

Modern coding assistants are extremely capable, but they have strong defaults:
- client-side JavaScript
- JSON APIs for UI composition
- frontend frameworks for state and flow

HTMX takes a different approach.

When asked to implement common interactions (modals, inline edits, confirmations, form flows), AI assistants often reach for JavaScript even when a **simpler, more maintainable HTMX-native solution exists**.

This repository exists to correct that behavior.

---

## What Are “Skills”?

A **skill** is a repeatable interaction pattern defined by:
- a single user intent
- clear constraints
- explicit route responsibilities
- server-rendered HTML fragments
- declarative HTMX swaps

Skills are **not snippets** and **not full applications**.  
They are behavioral contracts that both humans and AI models can follow.

---

## Core Principles

- **Server-driven UI**
- **HTML as the primary contract**
- **No JavaScript by default**
- **Clear route responsibilities**
- **One skill = one user intent**
- **Progressive enhancement friendly**

These principles are enforced intentionally and consistently.

For deeper rationale, see [`philosophy.md`](./philosophy.md).

---

## Repository Structure
htmx-skills/
├── skills/        # Canonical skill definitions (one file per skill)
├── adapters/      # Vendor-specific adapters (Codex, Claude, MCP, etc.)
├── templates/     # Templates for new skills and adapters
├── philosophy.md  # Design and governance principles
└── README.md

---

## Skills

Each skill:
- is expressed in plain language and structured markdown
- includes intent, constraints, UI structure, and route contracts
- avoids framework- or language-specific assumptions

### Example Skill
- `htmx_modal_form_flow`  
  A complete modal-based form submission pattern using pure HTMX, server-rendered partials, and out-of-band swaps—no JavaScript required.

---

## Adapters

Skills are **model-agnostic** by design.

Adapters translate the same skill definition into formats understood by:
- Codex
- Claude
- OpenAI Chat
- MCP-based agent frameworks

Adapters **do not redefine skills**.  
They only adapt them.

---

## What This Repository Is Not

This repository intentionally does **not** include:
- frontend frameworks
- JavaScript helpers
- full demo applications
- CSS systems or UI kits
- client-side state management

Those concerns distract from the core goal:
**teaching AI-assisted coding tools to behave correctly with HTMX.**

---

## Who This Is For

This repository is for:
- Developers who already use HTMX
- Teams frustrated by AI-generated JavaScript
- Anyone designing server-driven interfaces
- People who care about architectural discipline

It is *not* a beginner tutorial.

---

## Contributing

Contributions are welcome, but intentionally constrained.

A good contribution:
- encodes a clear interaction pattern
- removes the need for JavaScript
- improves AI behavior, not just convenience
- respects the philosophy of the repository

A contribution may be rejected if it:
- introduces JavaScript without necessity
- relies on frontend frameworks
- weakens existing constraints
- blurs server/client responsibilities

See [`philosophy.md`](./philosophy.md) before contributing.

---

## License

MIT License.  
Patterns should be shared freely.
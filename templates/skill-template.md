# Skill: <skill_name>

## Intent

Describe the single user intent this skill serves in one or two sentences.
State what the user wants to accomplish, not how.

---

## Core Principles

- Server-driven UI
- HTML as the primary contract
- No custom JavaScript by default
- Clear route responsibilities
- One skill = one user intent
- Progressive enhancement friendly

---

## Constraints (Non-Negotiable)

- NO: custom JavaScript unless explicitly justified in this skill
- NO: frontend frameworks or client-side state management
- NO: JSON responses for UI composition
- YES: server-rendered HTML fragments
- YES: hx-* attributes for interaction and swaps
- YES: one route per responsibility

If JavaScript seems "easier," stop and redesign using HTMX primitives.

---

## Required Inputs

List the parameters a caller must provide to apply this skill.

- <input_1> - what it represents
- <input_2> - what it represents
- Use semantic names
- Avoid implementation-specific assumptions
- Thes inputs should make the skill reusable

Example: 
- target_container_id
- entity_name
- submit_endpoint

---

## UI Structure

### Persistent Elements

Describe the always-present elements and the fragments the server returns.

### Static Placeholder (always present)

```html
<div id="<placeholder_id>"></div>
```

### Trigger Element

```html
<button
  hx-get="/<open_endpoint>"
  hx-target="#<placeholder_id>"
  hx-swap="innerHTML">
  <trigger_label>
</button>
```

---

## Fragment: GET /<open_endpoint>

Return the UI fragment needed to start the interaction.

```html
<div class="<container_class>">
  <h2><title></h2>
  <form
    hx-post="/<submit_endpoint>"
    hx-target="#<main_target_id>"
    hx-swap="<swap_behavior>">
    <!-- fields -->
    <button type="submit"><submit_label></button>
  </form>
</div>
```

Notes:
- Use server-rendered HTML only
- No client-side orchestration

---

## Response: POST /<submit_endpoint>

Describe what the server must return on submit.
If multiple fragments are required, spell them out separately.

### Main UI Update

```html
<div>
  <!-- updated content -->
</div>
```

### Cleanup / State Reset (optional, OOB)

```html
<div id="<placeholder_id>" hx-swap-oob="true"></div>
```

---

## Route Responsibilities

### GET /<open_endpoint>

- Returns a fragment only
- No side effects
- Idempotent

### POST /<submit_endpoint>

- Validates input
- Persists state
- Returns required fragments

---

## Interaction Flow (Mental Model)

1. User triggers the interaction
2. Server returns the fragment and swaps it in
3. User submits the form or action
4. Server processes and returns HTML
5. UI updates declaratively (and any cleanup occurs via OOB swap)

No JS. No client-side state.

---

## Validation and Error States

Define how validation errors are rendered as HTML and where they swap.
Make the error path as explicit as the success path.

---

## Common Mistakes (Explicitly Forbidden)

- Adding JS to manage UI state
- Returning JSON and rendering client-side
- Combining multiple responsibilities into one route
- Hiding/showing UI with client-side toggles instead of swaps

---

## Why This Skill Exists

Explain the default AI failure mode this skill corrects
and why the HTMX-first approach is superior.

---

## Skill Completeness Criteria

This skill is correctly applied when:

- No custom JavaScript is present
- Routes have clear, single responsibilities
- UI updates are server-driven and declarative
- The interaction is understandable by reading HTML alone

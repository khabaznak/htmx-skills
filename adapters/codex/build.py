#!/usr/bin/env python3
"""
Generate Codex-installable skills from canonical markdown in /skills.

Input:
  skills/*.md  (canonical, vendor-neutral skill definitions)

Output:
  adapters/codex/dist/.codex/skills/<skill_name>/SKILL.md
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
CANON_SKILLS_DIR = REPO_ROOT / "skills"
DIST_DIR = REPO_ROOT / "adapters" / "codex" / "dist" / ".codex" / "skills"


def slugify(name: str) -> str:
    # stable folder naming: lowercase snake_case-ish
    s = name.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s-]+", "_", s)
    return s


def parse_skill_name(md: str) -> str:
    """
    Preferred patterns:
      '# Skill: <name>'
    Fallback:
      first H1 line '# <name>'
    """
    m = re.search(r"^\s*#\s*Skill:\s*(.+?)\s*$", md, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()

    m = re.search(r"^\s*#\s*(.+?)\s*$", md, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()

    raise ValueError("Could not find skill name. Expected a '# Skill: ...' H1.")


def parse_intent(md: str) -> str:
    """
    Extract the first paragraph under '## Intent' as a description seed.
    """
    # Capture content after '## Intent' until next '## ' heading
    m = re.search(r"^##\s+Intent\s*\n(.*?)(?=^\s*##\s|\Z)", md, flags=re.MULTILINE | re.DOTALL)
    if not m:
        return ""

    block = m.group(1).strip()
    # Remove markdown separators / horizontal rules if present at start
    block = re.sub(r"^\s*---\s*$", "", block, flags=re.MULTILINE).strip()

    # First non-empty paragraph (stop at blank line)
    parts = [p.strip() for p in re.split(r"\n\s*\n", block) if p.strip()]
    return parts[0] if parts else ""


def first_sentence(text: str) -> str:
    """
    Crude but good enough: first sentence-ish chunk.
    """
    t = re.sub(r"\s+", " ", text).strip()
    if not t:
        return ""
    # Split on . ! ? followed by space/end
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    return m.group(1).strip() if m else (t[:140].strip())


def strip_canonical_header(md: str) -> str:
    """
    Remove the top H1 '# Skill: ...' or '# ...' line.
    Keep the rest intact.
    """
    lines = md.splitlines()
    out = []
    skipped_h1 = False
    for i, line in enumerate(lines):
        if not skipped_h1 and re.match(r"^\s*#\s+", line):
            skipped_h1 = True
            continue
        # Also skip an immediate blank line after the H1 for cleanliness
        if skipped_h1 and len(out) == 0 and line.strip() == "":
            continue
        out.append(line)
    return "\n".join(out).strip() + "\n"


def build_skill(md_path: Path) -> Tuple[str, str, str]:
    md = md_path.read_text(encoding="utf-8")
    name = parse_skill_name(md)
    intent = parse_intent(md)
    desc = first_sentence(intent) or f"HTMX skill: {name}"
    body = strip_canonical_header(md)

    return name, desc, body


def main() -> int:
    if not CANON_SKILLS_DIR.exists():
        print(f"ERROR: Missing canonical skills directory: {CANON_SKILLS_DIR}", file=sys.stderr)
        return 2

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(CANON_SKILLS_DIR.glob("*.md"))
    if not md_files:
        print(f"ERROR: No skills found in: {CANON_SKILLS_DIR}", file=sys.stderr)
        return 2

    generated = 0

    for md_path in md_files:
        name, desc, body = build_skill(md_path)
        folder = DIST_DIR / slugify(name)
        folder.mkdir(parents=True, exist_ok=True)
        out_path = folder / "SKILL.md"

        # Codex requires YAML front matter with name + description.
        out = (
            "---\n"
            f"name: {slugify(name)}\n"
            f"description: {desc}\n"
            "---\n\n"
            f"{body}"
        )

        out_path.write_text(out, encoding="utf-8")
        generated += 1
        print(f"Generated: {out_path.relative_to(REPO_ROOT)}")

    print(f"\nDone. Generated {generated} Codex skill(s) into: {DIST_DIR.relative_to(REPO_ROOT)}")
    print("Next: copy dist/.codex/skills/* to either <repo>/.codex/skills/ or ~/.codex/skills/ and restart Codex.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
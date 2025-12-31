# Codex Adapter

This adapter generates Codex-installable skills (`SKILL.md`) from canonical definitions in `/skills`.

## Generate
From repo root:

```bash
python3 adapters/codex/build.py
```

## Install (repo-scoped)

mkdir -p .codex/skills
cp -R adapters/codex/dist/.codex/skills/* .codex/skills/


## Install (user-scoped)
mkdir -p ~/.codex/skills
cp -R adapters/codex/dist/.codex/skills/* ~/.codex/skills/

## Restart Codex, then verify with /skills

Generated files live in dist/ and are intentionally not committed.
# DOGSGAME — Claude Instructions

**Status:** EXPLORATION phase. No build commitment yet. Read this first, then `ROUTING.md`.

## What this project is

A text-first dog life simulator based on Ted's four real dogs (Okie, Tex, Attila, Crockett) in their real yard in Sultan, WA. Treated as a **universe to poke at**, not yet a committed game design. Eventual v1 target: a minimal Okie-in-yard prototype, but that is not approved for build as of 2026-04-24.

## Project phases

1. **Exploration (current)** — workshopping mechanics, spectacles, voice. Output is markdown planning docs, not code.
2. **Build v1** — when Ted says "build v1," scope is frozen per `design/ARCHITECTURE.md` §"v1 minimum viable slice."
3. **Renderers v2+** — Ultima5 / Sims / NES lenses become viable.

Do NOT skip ahead. Do not generate game code before Ted approves v1 build.

## Where to look

- `ROUTING.md` — decision table: which file answers which question. Read this second.
- `CEAUDIT.md` — full context-engineering rationale for this layout.
- `canon/` — **immutable facts** about dogs, yard, behaviors. Treat as source-of-truth.
- `design/` — **speculation**: architecture, mockups, team dialogues. Subject to revision.
- `data/` — (planned) SQLite + optional vector store.
- `code/`, `tests/` — empty until v1 is approved.

## Convention: directory = status

- Anything under `canon/` is CANON. Edits require deliberation.
- Anything under `design/` is SPECULATIVE. Edits are cheap.
- Anything under `code/` is executable truth.

Don't move files between these without understanding the shift.

## When Ted mentions a new dog observation

1. Create `canon/behaviors/B###_<dog>_<short>.md` using the template (see any existing file).
2. Fill all four era proposals: TEXT, ULTIMA5, SIMS, NES.
3. Cross-reference related behaviors.
4. Update `canon/behaviors/INDEX.md`.
5. If a new idea emerges that's NOT an observation but a design proposal → it goes in `design/`, not canon.

## When Ted proposes adding to v1 scope

Run `/plan-abendsen-parking`. Log the idea in `design/PARKING.md` (create if absent). Do not silently expand scope.

## When Ted asks for design work

Treat as speculation. Put it in `design/`. Never promote design material to canon without explicit confirmation.

## When Ted says "build v1"

1. Run `/plan-steiner-gate`.
2. Confirm v1 scope hasn't drifted (see `design/ARCHITECTURE.md` §v1).
3. Only implement B001 behavior + TEXT renderer + Python stdlib.
4. Log every session's events to `data/dogsim.db` (schema in `data/schema.sql` once created).

## Workflow rules

- Canon edits = prose. After any canon change, re-seed DB (once `tools/seed_db.py` exists): `python tools/seed_db.py`.
- Use `ROUTING.md`; don't grep blindly.
- Project-level cross-session notes live in `MEMORY_LOCAL.md` (this repo), not user memory.
- User-profile facts live in `~/.claude/projects/C--Dev/memory/`.

## Parent-project discipline

This project sits under `C:\Dev`, which has its own `CLAUDE.md` mandating the PKD planning skills. Those apply here. Use `/plan-abendsen-parking`, `/plan-steiner-gate`, `/plan-arctor-retro` as appropriate. Do NOT author DOGSGAME-specific skills yet.

# ROUTING — Which file answers which question

Decision table. Agent reads `CLAUDE.md` first, then this, then loads only the specific files it needs.

## Quick index

| Question | Look here |
|----------|-----------|
| Who are the four dogs? What are their traits, breeds, quirks? | `canon/dogs.md` |
| What does the yard look like? Tile types? | `canon/yard.md` |
| What does dog X do in situation Y? | `canon/behaviors/INDEX.md`, then the specific `B###_*.md` |
| What's the list of known behaviors? | `canon/behaviors/INDEX.md` |
| How does the game engine work? Event bus? Kernel? | `design/ARCHITECTURE.md` |
| What would scene Z look like in era W? | `design/MOCKUPS.md` |
| Should we build feature F? What are the trade-offs? | `design/DIALOGUES/INDEX.md`, then specific dialogue |
| Why is the project organized this way? | `CEAUDIT.md` |
| What are the current ground rules? | `CLAUDE.md` |
| What was decided in previous sessions? | `MEMORY_LOCAL.md` |
| What was logged in session N? | `data/dogsim.db` → `events` table (once DB exists) |
| What flavor lines exist for event E? | `data/dogsim.db` → `flavor_banks` (once DB exists) |
| What's parked / out of scope? | `design/PARKING.md` (create if absent) |

## Canonical file purposes

### `canon/` — facts about the universe

| File | Contains |
|------|----------|
| `canon/dogs.md` | The four dogs: roster, traits, physical descriptions, health flags |
| `canon/yard.md` | Yard geography, tile map, tile-type enum |
| `canon/behaviors/B###_*.md` | One behavior per file: real-world description, trigger, era proposals, design notes |
| `canon/behaviors/INDEX.md` | Numeric index with one-line summaries |

### `design/` — speculation and proposals

| File | Contains |
|------|----------|
| `design/ARCHITECTURE.md` | Engine design: kernel, event bus, renderers, narrative director |
| `design/MOCKUPS.md` | Scene mockups across four rendering eras |
| `design/DIALOGUES/INDEX.md` | Index of team-dialogue files |
| `design/DIALOGUES/NN_*.md` | Dialogues between narrative designer, historian, programmer |
| `design/PARKING.md` | Parked ideas (create on first parking) |

### Root

| File | Contains |
|------|----------|
| `CLAUDE.md` | Ground rules for agents working on this project |
| `ROUTING.md` | This file |
| `CEAUDIT.md` | Context-engineering audit / rationale for layout |
| `MEMORY_LOCAL.md` | Project-level cross-session conventions |
| `BEHAVIORS.md` | Behavior-systems taxonomy (12 systems; not the per-dog log) |

### `code/` — playable prototypes

| File | Contains |
|------|----------|
| `code/dogsim.py` | Encounter-based terminal game; numbered menus; noir voice; `--test` mode |
| `code/showcase.html` | Four-era visual mockup (TEXT / ULTIMA V / SIMS / NES); browser-only |
| `code/README.md` | How to run + how to extend |

## When to load what

- **Ted adds new dog observation** → `CLAUDE.md` + `canon/behaviors/INDEX.md` + one template sibling. Load < 3 files.
- **Ted wants to build v1** → `CLAUDE.md` + `design/ARCHITECTURE.md` + `canon/yard.md` + `canon/behaviors/B001_*.md`. Load 4 files.
- **Ted asks for narration help** → `CLAUDE.md` + relevant `canon/behaviors/B###_*.md`. Query flavor DB once it exists.
- **Ted asks a design question** → `CLAUDE.md` + the specific `design/*` file(s). Canon not needed.
- **Debugging an existing session** → `CLAUDE.md` + SQL query. Never load canon — it's about what *happened*, not what *exists*.

## Load-budget goal

Most agent tasks should touch ≤ 5 files. If you're loading 10+ files "just to be safe," stop and re-read this document.

# DOGSGAME — Context Engineering Audit (CEAUDIT)

**Author:** Claude (advisor role)
**Date:** 2026-04-24
**Scope:** How this project's artifacts, data stores, skills, and memory should be structured so that an LLM agent coding on DOGSGAME is *strategically exposed* to the right context at the right time — without drowning.

---

## 0. What "context engineering" means here

Three tiers of knowledge will exist in DOGSGAME:

1. **Always-loaded context** — read into the model every session. Must be short, stable, and load-bearing. (E.g., `CLAUDE.md`, `MEMORY.md` index.)
2. **Discoverable context** — lives in files / DBs, fetched on demand. Must be well-named and indexed. (E.g., `BEHAVIORS.md`, `YARD.md`, future SQLite tables.)
3. **Computed context** — produced by tools/queries against structured data. The agent doesn't read 10 MB of events — it queries for "what happened in the last session between Okie and Crockett" and gets a tight summary. (E.g., SQL views, vector searches.)

An LLM that has all three tiers wired correctly can work on DOGSGAME productively for months. One that only has tier 1 (+ grep) will regress as the project grows.

---

## 1. Current artifact inventory

```
C:\Dev\DOGSGAME\
  ARCHITECTURE.md               — engine design (layer diagram, kernel types)
  BEHAVIORS.md                  — B001..B010 behavior log + proposals
  YARD.md                       — geography + tile map draft
  MOCKUPS.md                    — 4-era scene mockups
  DIALOGUE_01_first_meeting.md  — narrative-designer / historian / programmer workshop
  CEAUDIT.md                    — (this file)
```

**Verdict so far:** good for the exploration phase. Bad for the agentic-coding phase that's coming. Specifically:

- No `CLAUDE.md` in the project root — agents won't auto-orient.
- No index / routing doc — an agent has to read everything to know where to look.
- No separation between *canon* (facts about the dogs / yard) and *speculation* (proposals, dialogues). An agent could easily confuse "B007 flashback mechanic" (proposed) with "B001 bush-kill" (v1 canon).
- No machine-readable data yet — everything is prose. Fine for planning, bad for code generation and querying.

---

## 2. Proposed structure — the "three-tier" layout

```
C:\Dev\DOGSGAME\
  CLAUDE.md                     ← tier 1: always loaded (routing + v1 scope + rules)
  ROUTING.md                    ← tier 1: "which file answers which question"
  canon/                        ← tier 2: facts, immutable without discussion
    dogs.md                     ← the four dogs (stats, breeds, histories)
    yard.md                     ← geography (moved from YARD.md)
    behaviors/                  ← one file per behavior entry
      B001_okie_pee_bush.md
      B002_tex_belly_roll.md
      ...
  design/                       ← tier 2: speculation, living docs
    ARCHITECTURE.md
    MOCKUPS.md
    DIALOGUES/
      01_first_meeting.md
      ...
  data/                         ← tier 3: structured / queryable
    dogsim.db                   ← SQLite: behaviors, scenes, narration banks
    chroma/                     ← vector store (optional): narrative flavor snippets
    schema.sql                  ← authoritative schema
  code/                         ← v1 and beyond
    kernel/
    renderers/
    main.py
  tests/
  sessions/                     ← gameplay session logs (replayable)
  tools/                        ← scripts: seed db, export markdown, regenerate indexes
  MEMORY_LOCAL.md               ← project-specific cross-session notes (not the user memory)
```

**Why this structure:**

- `canon/` vs. `design/` is the single most important split. Canon facts get referenced in code generation and flavor text; design proposals don't. An agent should be able to tell which is which at a glance.
- One file per behavior under `canon/behaviors/` means: agent can read a single file to understand B005 without loading all ten. Also makes each behavior individually version-controllable.
- `data/` is the tier-3 substrate. The prose docs are *source*; the SQLite DB is *derived*. A script (`tools/seed_db.py`) keeps them in sync.
- `sessions/` gives the agent a *history* to draw on — "last session, Okie banked 7 bones." This is context that doesn't fit in prose.

---

## 3. Database strategy

### Why two databases

**SQLite (`dogsim.db`)** — structured, queryable, small, zero-install, stdlib-accessible from Python.

Tables (draft):

| Table | Purpose |
|-------|---------|
| `dogs` | canonical dog roster (id, name, breed, age, size, traits) |
| `tiles` | yard tile types + attributes |
| `behaviors` | B### registry: id, name, preconditions (JSON), effect (JSON), era_proposals (JSON) |
| `events` | every game event ever logged: tick, kind, actor, target, data (JSON) |
| `sessions` | one row per playthrough: seed, start, end, final_state |
| `flavor_banks` | narration templates keyed by (era, event_kind, context_tags) |
| `scenes` | authored scenes (title, behavior_refs, mockup_refs) |

Why this beats prose alone:
- Agents can run `SELECT * FROM events WHERE actor='okie' AND kind='pee'` instead of grepping.
- Replay + debugging is trivial.
- Behavior registry is both human-readable (canon/) AND machine-queryable (DB).

**Vector store (Chroma, optional)** — for *narrative* and *flavor* retrieval, not for facts.

Collection: `narration_snippets`
- Each doc: a flavor line + metadata (era, tone, behavior_ref, tags)
- Query: "find me three Infocom-voice flavor lines for a bush-death event in a melancholic tone"
- Returns: top-k similarity hits, agent picks one or remixes.

Why vector: narrative voice is fuzzy. SQL queries on tags work for 80% of cases; vector search handles the 20% where you want tonal similarity rather than exact tag matches. **Start without it. Add only when flavor banks exceed ~200 entries.**

### Sync strategy

Canon markdown files are **source of truth**. DB is **rebuilt** from them via `tools/seed_db.py`. This is cheaper than maintaining DB-as-source because:
- Markdown diffs read cleanly in git.
- Regenerating a small DB is fast.
- If an agent edits canon, it re-runs seed.

Game-generated data (events, sessions) is DB-native — never goes back to markdown.

---

## 4. `CLAUDE.md` — what the always-loaded context should contain

Draft (to be created as a separate file):

```markdown
# DOGSGAME — Claude Instructions

## What this project is
A text-first dog life simulator based on Ted's four real dogs. Treated as a universe
to poke at, not yet a committed game design. v1 target: minimal Okie-in-yard prototype.

## Where to look
- Canon (facts): canon/
- Design (speculation): design/
- Data: data/dogsim.db
- Current phase: EXPLORATION (no build commitment yet)

Read ROUTING.md to decide which file answers which question.

## Scope rules
- Do not build v1 code until Ted says "let's build v1."
- If Ted adds a new observation: log it to canon/behaviors/B###_*.md with all 4 era proposals filled in.
- If Ted adds a new idea: check against v1 scope; if it's out, note it in design/PARKING.md.

## v1 scope (frozen, reference only — not yet approved for build)
- Single dog: Okie
- Grid: yard tile map from canon/yard.md
- One rule: B001 (pee on blueberry bush → dies)
- Renderer: text only
- Stack: Python stdlib, single file

## Workflow
- Canon edits = prose. Rebuild DB with `python tools/seed_db.py` after.
- Use ROUTING.md; don't grep blindly.
- Check MEMORY_LOCAL.md for project-specific conventions that don't fit here.
```

---

## 5. `ROUTING.md` — the context-expansion index

This is the file an agent reads *second*, to decide which tier-2 file to load.

```markdown
# ROUTING — Which file answers which question

| Question | Look here |
|----------|-----------|
| Who are the dogs? | canon/dogs.md |
| What does the yard look like? | canon/yard.md |
| What does dog X do in situation Y? | canon/behaviors/B*.md |
| How does the game engine work? | design/ARCHITECTURE.md |
| What would scene Z look like in era W? | design/MOCKUPS.md |
| Should we build feature F? | design/DIALOGUES/ |
| What was logged in session N? | SQL: data/dogsim.db, events table |
| What flavor lines exist for event E? | SQL or vector query, data/ |
| Why are we doing this? | CLAUDE.md, then CEAUDIT.md |
```

Agent reads CLAUDE.md first (30 lines). Then ROUTING.md (20 lines). Then decides what to load. **Fifty lines of always-on context routes the agent to every other file in the project.** That's the win.

---

## 6. Skills integration (PKD skills + DOGSGAME)

Ted's `C:\Dev` CLAUDE.md mandates planning skills. For DOGSGAME specifically:

| Situation | Skill |
|-----------|-------|
| Ted adds new dog observation | (no skill — direct canon edit) |
| Ted proposes new feature in v1 | `/plan-abendsen-parking` — park unless scope re-frozen |
| Agent about to start coding v1 | `/plan-steiner-gate` — verify scope + prereqs |
| Agent wants to refactor post-v1 | `/plan-bulero-refactor` |
| Weekly / post-session review | `/plan-arctor-retro` |
| Architecture doubts | `/plan-deckard-boundary` for LLM-in-the-loop decisions |

DOGSGAME's `CLAUDE.md` should **reference the /Dev skills but not duplicate them**. The parent CLAUDE.md handles the general planning discipline; the child CLAUDE.md handles project-specific overlays.

---

## 7. Memory system integration

The global user memory at `C:\Users\PC\.claude\projects\C--Dev\memory\` already has a `project_dogsim.md` entry (now stale — it points to the old path). This must be updated to:

- Path: `C:\Dev\DOGSGAME\`
- Link to CEAUDIT.md as the canonical entry for "how this project is organized"
- Dog roster (already captured)
- v1 scope (already captured)

**Separately**, the project should keep a `MEMORY_LOCAL.md` in the repo root — *project-level* cross-session notes (not user-profile notes). E.g., "last session we decided the pig and cow are cosmetic skins, not distinct objects." These facts belong with the project, not the user.

---

## 8. Strategic context exposure — the agentic patterns

How the agent actually *uses* this structure during a coding session:

### Pattern 1: "Ted mentions a new dog behavior"
1. Agent reads CLAUDE.md (always loaded).
2. Agent recognizes "new behavior" → reads routing → creates new `canon/behaviors/B###_*.md`.
3. Agent re-runs `tools/seed_db.py` to update DB.
4. Agent updates `canon/behaviors/INDEX.md` (behavior list).
5. Done. Minimal context load: CLAUDE.md + one template + the new file.

### Pattern 2: "Ted asks to build v1 feature"
1. Agent reads CLAUDE.md → sees scope rules.
2. Agent loads `design/ARCHITECTURE.md` + the relevant `canon/behaviors/B001.md`.
3. Agent loads `canon/yard.md` for the grid.
4. Agent generates code under `code/`, tests under `tests/`.
5. Does NOT load mockups, dialogues, CEAUDIT — irrelevant for build.

### Pattern 3: "Ted wants narration help"
1. Agent reads CLAUDE.md.
2. Agent queries vector store (or SQL `flavor_banks`) for matching-tone lines.
3. Agent returns candidates, never regenerates the whole flavor bank.

### Pattern 4: "Debugging a logged session"
1. Agent reads CLAUDE.md.
2. Agent queries `events` table for the session in question.
3. Agent returns a timeline of the last N ticks for that session.
4. Does NOT load canon — it's about what *happened*, not what *exists*.

Each pattern loads < 5 files on average. Without this structure, an agent would load 10+ files ("just in case") and burn context on irrelevance.

---

## 9. Sub-agent delegation map

The `C:\Dev` environment has Explore, Plan, and general-purpose sub-agents. For DOGSGAME:

| Task | Delegate to |
|------|-------------|
| "Find every behavior involving Crockett" | Explore (quick) |
| "Draft a design for how save/load should work" | Plan |
| "Rewrite all B### files to match the new template" | general-purpose |
| "Log a new dog observation" | main agent (it's small and atomic) |
| "Run a full audit on behavior coverage vs. real dog stories" | Plan + Explore |

Sub-agent calls should **always receive a specific file list or query**, not "look around the project." Sub-agents without tight scope waste context the same way the main agent would.

---

## 10. Migration plan — getting to the three-tier layout

What we have now is a flat prose dump. To reach the proposed structure:

**Phase A — Zero-cost reorganization (1 session):**
1. Create `canon/`, `design/`, `data/`, `code/`, `tests/`, `sessions/`, `tools/` directories.
2. Move existing files: `YARD.md → canon/yard.md`, `ARCHITECTURE.md` + `MOCKUPS.md` → `design/`, `DIALOGUE_01_*.md → design/DIALOGUES/01_first_meeting.md`.
3. Split `BEHAVIORS.md` into one file per B### under `canon/behaviors/`.
4. Write `CLAUDE.md`, `ROUTING.md`, `MEMORY_LOCAL.md`.
5. Write a `canon/dogs.md` extracted from the roster table already in BEHAVIORS.md.

**Phase B — Database bootstrap (1 session):**
1. Write `data/schema.sql`.
2. Write `tools/seed_db.py` to parse canon markdown into DB.
3. Run it; verify round-trip.
4. Add a `tools/query_examples.md` for common queries.

**Phase C — First code (when Ted approves build):**
1. Build v1 kernel per ARCHITECTURE.md.
2. Implement B001 only.
3. Text renderer.
4. Save/load via DB.
5. Log all events to `events` table.

**None of A or B requires writing game code.** They're pure organizational work. A few hours of an agent's time, net huge context-engineering win.

---

## 11. Risks and failure modes

1. **Over-engineering the substrate before building the game.** Biggest risk. The three-tier layout is useful *only if* the game actually gets built. Don't spend three sessions building tooling and zero building game.
   - **Mitigation:** Cap Phase A + B at one session each. If they bloat, stop.

2. **Canon/design drift.** A behavior proposed in `design/` accidentally gets treated as canon.
   - **Mitigation:** Every `canon/*` file has a header `Status: CANON | Last updated: <date>`. Every `design/*` file has `Status: SPECULATIVE`.

3. **DB rebuild lag.** Markdown updated, DB not re-seeded, agent queries stale data.
   - **Mitigation:** A git hook or manual rule: "if canon/ edited, re-run seed_db before commit." Cheap to enforce.

4. **Context bloat from dialogue files.** `DIALOGUE_XX.md` files are enjoyable but large. An agent that loads all dialogues has burned 10k+ tokens on opinion.
   - **Mitigation:** `design/DIALOGUES/INDEX.md` with one-line summary per dialogue. Agent loads INDEX first, loads specific dialogues only when needed.

5. **Memory staleness.** `MEMORY.md` points at old paths after the rename.
   - **Mitigation:** Update the user memory now (this turn), and add a "check memory paths vs. repo paths" step to the retro skill.

6. **Skill proliferation.** The PKD skill registry is already 33 skills. Adding DOGSGAME-specific skills risks tipping into unmaintainable.
   - **Mitigation:** Use existing skills only. Don't author DOGSGAME-specific skills until the same workflow has repeated 3+ times.

---

## 12. Summary — the minimum context-engineering discipline

If only three things get done:

1. **Write `CLAUDE.md` and `ROUTING.md`.** Fifty lines total. Single biggest agent-productivity investment.
2. **Split `canon/` from `design/`.** Prevents proposal-as-fact contamination.
3. **Commit to SQLite now, vector store later.** Start with the cheap, useful, universal data store.

Everything else in this audit is optimization. These three are structure — and you can't optimize what you haven't structured.

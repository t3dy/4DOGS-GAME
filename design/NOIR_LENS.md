# NOIR_LENS — Deja Vu / Police Quest / K-9 aesthetic proposal

**Status:** SPECULATIVE — strong candidate. Introduced 2026-04-24 by Ted as a unifying tonal/visual lens for DOGSGAME.

---

## The pitch

Render DOGSGAME in the aesthetic lineage of:

- **Deja Vu** (ICOM Simulations, 1985 Mac / 1988 NES) — first-person noir detective, monochrome + red accent, heavy prose, click-driven verbs (EXAMINE, OPEN, HIT, CONSUME, OPERATE, GO, SPEAK), long cynical narration.
- **Police Quest** (Sierra, 1987) — procedural cop adventure, strict-realism police work, EGA pixel art, keyword-driven, attention to radio codes and protocol.
- **K-9 fantasy frame** — where Ted wistfully imagines his dogs as police dogs. The dogs get to be professional, dignified, effective. (Contrast: their real behavior.)

The resulting DOGSGAME lens is **noir dog ownership** — a hardboiled narrator takes us through the life of four dogs and the man who cleans up after them. Funny, tender, cynical. The dogs don't talk, but the narrator gives them weight. The crimes are small (killed a bush, stole a toy, bit a neighbor's dog). The stakes are comically low. The prose is comically high.

---

## Why this is a strong candidate lens

1. **Tonal fit.** Most of the observed behaviors already have a noir inflection when described honestly: Okie is a *bone banker*, Crockett is a *thief*, the gate incident is a *shakedown*, Attila's whine is a *confession*. Ted's own descriptions are already noir.
2. **Unifies the four eras.** Deja Vu was released across Mac and NES. Police Quest was Sierra on DOS/AGI. The aesthetic spans the period we've been discussing without committing to one specific hardware constraint.
3. **Answers open tonal questions.** Dark-comedy vs. tender = BOTH, via noir's comfortable mixture of cynicism and unexpected warmth. Feel-bad-about-bush vs. laugh-at-bush = both, in sequence, noir-style.
4. **Gate incident B016 already reads as a Deja Vu chapter.** Pregnant Woman. Cop Husband. $200 cash. Ted running through the suburb. You could screenshot that scene.
5. **Playable in Claude Code terminal.** Deja Vu was text-heavy — text-first play fits. The pastiche isn't locked to graphics.

---

## What this lens looks like concretely

### The narrator

First-person. Ted (or a Ted-shaped detective figure) speaks. World-weary, but the subject is dogs, so the gravity keeps undercutting itself:

> It was the kind of morning where the grass looked guilty. The bush was dead, and we all knew who did it, but Okie wasn't talking. He never does. He's a dog.

### The verb menu

Deja Vu had a verb grid. DOGSGAME version:

```
┌────────────────────────────────────┐
│  EXAMINE   SPEAK TO   OPERATE      │
│  CALL      PET        CORRECT      │
│  FEED      LEASH      OPEN GATE    │
│  GO        WAIT       SLEEP        │
└────────────────────────────────────┘
```

Plus a contextual verb slot: `CONFRONT` appears when a Pregnant Woman is onscreen.

### The palette

- Monochrome + red accent (classic Deja Vu NES)
- Alternative: EGA 16-color for Police Quest pastiche

### The case structure

Episodic. Each session is a *case* or *incident*. Sample case list:

- **Case 1: The Blueberry** — B001 as a noir mystery. Suspect: Okie. Evidence: yellow leaves, a familiar stain.
- **Case 2: The Gate Open** — B016 played as a full Deja Vu chapter.
- **Case 3: The Squeaker** — B003 + B004 as toy-theft noir.
- **Case 4: The Nighttime Deposit** — B008 procedural. Cop humor.
- **Case 5: The Bone Vault** — B005 uncovers Okie's hoard. Discovery, not prosecution.

Ambient life (B002 belly-roll, B011 bed session) continues between cases as "downtime" scenes — the detective's domestic life.

### The K-9 fantasy sidebar

Rare dream-sequences where the dogs are a crack K-9 team. Police Quest pastiche. Radio codes. Okie as the seasoned veteran. Tex as the big reliable partner. Attila as the unintimidating-but-terrifying rookie. Crockett as the retired legend brought back for one last case.

Fantasies, not canon. But they provide a *contrast* that makes the real dogs funnier and more tender.

---

## How this maps onto the engine architecture

`design/ARCHITECTURE.md` still applies. The noir aesthetic is a **renderer + narrative flavor bank**, not a kernel change.

- `renderers/noir.py` — text renderer with verb grid, monochrome ASCII, noir framing of the game map.
- `narrative/banks/noir.py` — flavor lines for every event kind, written in Ted-as-detective voice.
- `narrative/banks/policequest.py` — alternative bank for K-9 fantasy scenes.

Same kernel, different flavor bank + renderer chrome. Swap is ~200 lines of Python.

---

## What this lens does NOT require

- No new kernel features (yet).
- No graphics. The aesthetic survives as pure text + optional ASCII/pixel ornaments.
- No new behaviors. B001–B016 all fit.

## What this lens would benefit from

- A **case writer** — some behaviors form *arcs* (B001, B003+B004, B016) suitable for noir framing; others are *ambient* (B002, B011, B015). Splitting the canon into "case-worthy" and "ambient" would help.
- A **flavor bank starter** — 10–20 sample noir lines for common events (pee, bark, whine, steal) to prove the voice is viable.
- A **verb grid mockup** — ASCII mockup of the Deja Vu interface applied to DOGSGAME, showing what the player actually sees.

---

## Proposed next exploration step (when Ted wants to advance)

Write **one case** end-to-end in noir voice as a scene script:

> **CASE 1: THE BLUEBERRY.** Opening narration → examine the bush → speak to Okie → confront the evidence → resolution.

Scope: one markdown file. ~200 lines of prose and verb-prompts. Demonstrates the lens without committing to code.

---

## Decision pending from Ted

1. Adopt noir lens as **primary** for v1, or one of several eras to switch between?
2. Case-based session structure, or ambient open-ended, or both?
3. K-9 fantasy scenes: in or out of v1?
4. Ted-as-detective voice, or an invented narrator character?

No action required now. This file is a speculative proposal to develop if/when Ted wants to commit.

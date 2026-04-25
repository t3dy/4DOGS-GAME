# PARKING — Parked ideas

Ideas that are explicitly out-of-scope for the current phase but worth not losing. Managed per `/plan-abendsen-parking`.

Format: `P### — <title>`, one paragraph on what it is and why it's parked. Promote to an active design doc when the phase warrants it.

---

## Parked items

### P001 — Graphics layer swap

Swap text renderer for sprite-based renderer (Ultima 5 / Sims-style / NES). Parked because the text kernel must be stable first. Implicit in `design/ARCHITECTURE.md` renderer-protocol design.

### P002 — NES cartridge port

Actual 6502-assembly NES ROM output. Parked until the game exists in any form. Fun in the abstract, premature in practice.

### P003 — Dog-interview onboarding mode

Game-startup flow that asks the player about each dog to populate traits. Parked because the dog roster is already canonical in `canon/dogs.md` — the interview only makes sense if we ship this to players who aren't Ted.

### P004 — Shamanic voyages / astral ceremonial-magic adventures

See `design/SHAMANIC_VOYAGES.md`. Parked explicitly by Ted on 2026-04-24 pending further thought.

### P005 — K-9 fantasy Police Quest scenes

Sub-proposal in `design/NOIR_LENS.md`. Parked unless/until the noir lens is adopted and we want a contrast layer.

### P006 — Historical dogs roster (Dalamar etc.)

A `canon/historical_dogs.md` file with Ted's previous dogs (currently only Dalamar the border collie referenced in `B014_tennis_ball_disappointment.md`). Parked until more historical dogs are named.

### P007 — Multi-location world

The yard is v1. The dog park (B015), the walks, the vet, the car trip, the neighborhood (B016) are all legitimate locations. Parked until the yard works.

### P008 — Persistent multi-session saves

World state that survives across Claude Code sessions. Parked until v1 proves the session-local state machine.

### P009 — Dedicated DOGSGAME skills

Custom PKD-style skills for logging behaviors, generating noir narration, etc. Parked — do not author until the same workflow has repeated 3+ times (per CEAUDIT §11 risk mitigation).

### P010 — Interactive animated prototypes

Ted asked earlier for clickable mockup prototypes across the four eras. Parked — biggest single scope jump on the table. Requires explicit go-ahead and a choice of target (HTML/canvas? Python curses? Pygame?).

### P011 — Vector store for narrative flavor

Chroma or similar for tonal-similarity retrieval of flavor lines. Parked until the flavor bank exceeds ~200 entries (per CEAUDIT §3).

### P012 — DIALOGUE_02 mechanics workshop

Promised at the end of `design/DIALOGUES/01_first_meeting.md`. Parked pending Ted's preference: continue exploring behaviors, or pause and workshop the ones we have?

### P013 — Case-based session structure

From `design/NOIR_LENS.md`: sessions as episodic detective cases rather than open-ended sims. Parked until noir lens is adopted.

### P014 — Coprophagia-induced quests

Joke entry but partly serious: the scoop-the-yard mechanic (B012) could become its own chore loop. Parked as an anti-pattern to watch for — cleaning-as-gameplay is a particular genre commitment.

### P015 — K9_PATROL roguelike (companion game)

FTL-inspired roguelike. Police car + K-9 unit + partner. See `design/K9_PATROL_ROGUELIKE.md`. Parked until DOGSGAME v1 ships AND noir lens is adopted. Would spawn a new project directory (`C:\Dev\K9PATROL\`), not live inside DOGSGAME.

### P016 — Neighborhood / suburb map for B016 arc

The gate-open incident requires a suburb map beyond the yard. Parked — v1 is yard-only. Revisit when noir lens is adopted, since B016 is the prototypical noir case.

---

## How to use this file

- When Ted suggests a feature that isn't v1, add a `P###` entry here and keep building.
- When Ted wants to revisit a parked item, reference it by P### and move it into an active design doc.
- When a parked item becomes irrelevant (e.g., superseded by a different approach), mark it `OBSOLETE` with a one-line note — don't delete.

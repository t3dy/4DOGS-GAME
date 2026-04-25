# B006 — Okie — Anxious garage-seeking

**Status:** CANON.

## Real-world

Okie is "very anxious." He explicitly asks to be let into the garage — the garage functions as his refuge, not a punishment.

## Trigger

`anxiety` stat rises above threshold, or a stressor event fires (loud noise, unfamiliar person, humans leaving, etc.).

## Proposals

- **TEXT:** Ambient message: `[Okie is pacing. He nudges the garage door with his nose.]` Player can `> let okie in garage` (lowers anxiety over N turns) or ignore (anxiety continues to rise; may trigger B007 flashback).
- **ULTIMA5:** Okie's `anxiety` is a visible stat bar. At ≥ threshold he emits a speech-balloon `♥︎?` over his sprite while facing the garage door. NPC human (player avatar) can toggle the door. Resting in the garage decays anxiety.
- **SIMS:** `anxiety` is a continuous stat fed by world events (human_leaves_house, loud_noise, storm). Above threshold → autonomy seeks `safe_space` tagged objects; the garage kiddie-pool beds are the highest-weighted safe_space in the household. Resting there decays anxiety faster than resting elsewhere.
- **NES:** Anxiety is a 4-bit value. At 0xC+, Okie's idle animation changes to "pacing" (3-frame sprite cycle). Garage door interactable → animation change, anxiety tick-down resumes.

## Design notes

- Anxiety is the **emotional-state axis** of the game. Without it, Okie is just a position on a grid.
- Flag: this stat creates an implicit *time pressure* — sessions will feel different if anxiety ticks up. Could be a v2 addition rather than v1 (keep v1 pure state machine: pee → bush dies).

## Cross-references

- `B005` — bone-banking is Okie's garage activity once inside.
- `B007` — if anxiety unresolved, triggers flashback (legacy bed-destruction memory).
- `B008` — Okie sleeping in garage (his preference) is chronic anxiety-lowering, not acute.

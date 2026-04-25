# B013 — Attila — Bed-petting demand + command-resistance

**Status:** CANON.

## Real-world

Attila is *allowed* on the bed (unlike the Aussies). But when he's with Ted on the bed, he will usually only stay if **continuously petted**. If Ted stops petting, Attila will **paw at him** to ask for more. When Ted is ready for Attila to leave the bed, it sometimes takes **multiple commands** to get Attila to jump down.

The Aussies exhibit a similar petting-demand pattern in the rare bed-session (B011), but they compound it with face-lick attempts (B012), requiring firmer boundaries from Ted.

## Trigger

Attila on bed + pet-stroke interval > threshold → paw action.
Ted issues `down` command + Attila's reluctance stat > threshold → command ignored / partial compliance.

## Proposals

- **TEXT:** Micro-dialog: `[You stop petting Attila. He looks at you. He lifts a massive paw and places it on your chest. The message is clear.]`. `> continue petting` or `> tell him down`. The `down` command may require 1–3 repetitions with escalating firmness.
- **ULTIMA5:** Attila has a `petting_timer` that decays. At zero, his sprite plays a "paw" animation. `down` command fires as a dialogue option with a probabilistic success check (70%, 85%, 95% on repetitions 1/2/3).
- **SIMS:** Continuous `petting_need` stat; when unsatisfied and in bed-context, paw-animation fires. Command-compliance is a dog-level trait (Attila: medium-low when comfortable). Repeated commands raise an implicit "firmness" score that eventually exceeds his reluctance.
- **NES:** Timer bar above Attila's head when on bed. Drains every frame not petting. At zero, sprite pose changes to "paw lift" (single-frame swap). Down-command as B-button prompt; RNG check for success with increasing odds per press.

## Design notes

- **Compliance-is-work as a mechanic.** Refutes the "press button → dog obeys" pattern. Dogs negotiate. Good.
- Opens a **firmness/softness axis** — how insistent the player is with commands. Probably shouldn't be an explicit stat; let the *number of presses* be the stat.
- Attila's bed-permission is a key asymmetry: he's the "bed-legal" dog. This creates a small emotional privilege worth acknowledging in flavor text.
- Contrast with B012: Attila's pet-demand is warm; the Aussies' pet-demand is compounded by the face-lick problem.

## Cross-references

- `B011` (bed session) — the primary context.
- `B012` (face-lick risk) — parallel behavior for the Aussies on the bed.

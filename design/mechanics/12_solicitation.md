# Mechanic 12 — Solicitation Behaviors

**Research:** `design/behaviorresearch.md` §12
**Canon:** `canon/behaviors/B003_attila_squeaky.md`, `B013_attila_bed_petting_demand.md`
**Live encounters:** `squeak_steal` (#7), `attila_bed_petting` (#12)

## What this is

Solicitation = the dog asking for something via a learned operant. Attila's two big solicitations are:
- **Squeaky pig as attention signal** — works the toy when he wants you in the room.
- **Paw-on-chest** — when you stop petting him on the bed.

Both are deliberate and contextual. Both work *because* you respond. Both escalate if ignored.

## Implementation now

- `squeak_steal` handles the squeaky-as-signal solicitation. Player can engage, ignore, intercept (pet Crockett first), or watch.
- `attila_bed_petting` handles the paw-request. Stopping petting → paw appears → you resume. The encounter can loop on `stop` until you commit.

## Levers the player has

- Engage / ignore / redirect for each solicitation.
- In `attila_bed_petting`, the `down` command path requires multiple repetitions (canon: takes 2-3 commands).

## Levers the player does NOT have (yet)

- A `request_intensity` stat that rises across ignored solicitations and triggers escalation (paw-tap → paw-press → step on you).
- Cross-encounter solicitations. Attila currently solicits only in his dedicated encounters. Could add ambient interrupts: "Attila is staring at you from the kitchen doorway."
- Other dogs' distinct solicitation styles. Okie's is anxious leaning; Tex's is the belly-roll (Mechanic 06).

## Future expansion

- **Unified solicitation system:** a per-dog `unmet_need` value. Each tick without resolution adds to it. At threshold, an interrupt fires (the dog appears with a specific solicitation pose). Granted = reset; refused = continues climbing until the dog gives up.
- **Solicitation library:** Attila has paw + squeak. Add: leaning, blocking-the-doorway, sustained-eye-contact. Each is canon-able from real life (ask Ted).
- **Refusal cost:** repeated refusals over a session lower a `dog_satisfaction` aggregate that affects the debrief tone.

## Voice rules

Plain. Attila's paw is huge — that's a fact, write it as a fact. "I stopped. Three seconds later the paw landed on my chest." Don't compare it to anything. The fact itself is the comedy. Same with the squeak: "He works the squeaky pig when he wants attention."

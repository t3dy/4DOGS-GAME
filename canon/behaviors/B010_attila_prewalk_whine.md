# B010 — Attila — Pre-walk whine (thunderous bark → pitiful whine)

**Status:** CANON.

## Real-world

Attila can produce a thunderous loud bark, but ironically emits a **miserable whine** when being leashed up for a walk. The whine *continues* as the garage door opens — pure impatient hype.

## Trigger

Player action `get_leash` OR `open_garage_door` while Attila is present and a walk is imminent.

## Proposals

- **TEXT:** `> get leash` → `[Attila begins to whine. It is an astonishing sound from a 100-pound dog. As you clip the leash on, the whine crescendos. The garage door rises; the whine does not stop.]` Continues for N turns or until the walk begins.
- **ULTIMA5:** Attila's sprite changes to "whine" pose when player holds leash item. Speech balloon: `♪~~~`. Persists through door-open animation.
- **SIMS:** Attila has two separate vocalization stats: `bark_power` (high) and `vocal_restraint` (low when anticipation > 80%). Walk-anticipation event triggers whine cycle; ignored autonomy for the duration.
- **NES:** Two-sprite vocal: frame A (mouth closed), frame B (mouth open + `♪` effect-tile). APU ch2 triangle wave for whine (low-pitched sustained tone), contrasted with the noise-channel bark saved for B009.

## Design notes

- **Juxtaposition is the joke.** Big dog, tiny voice, unexpected pitch. The engine should preserve this contrast — vocalizations are NOT a single generic "make sound" action; they're per-context.
- Confirms dogs have a **vocalization repertoire** (bark, whine, silence). Candidate for a shared sub-system across B003, B009, B010.

## Cross-references

- `B003` (Attila squeaky) — another Attila vocalization context.
- `B009` (bark chain) — the *bark* side of Attila's range.

# Mechanic 10 — Tool Use / Problem-Solving

**Research:** `design/behaviorresearch.md` §10
**Canon:** `canon/behaviors/B005_okie_bone_banker.md` (updated 2026-04-25 with the blanket-rearrangement detail)
**Live encounter:** **UPDATED** — `garage_bone_pack` (#5) now offers `prepare_blanket` as a two-stage prep action

## What this is

Dogs aren't traditional tool-users, but they do solve problems and modify their environment. Cache-modification — pawing the substrate, rearranging cover — is documented. Okie does this with the kiddie-pool blanket: he upsets it deliberately to make a better hide before stashing.

This is the cleanest example we have of *prepare-then-act* sequencing. Worth modeling well because it generalizes — any future "set up before doing" mechanic can use the same shape.

## Implementation now

`garage_bone_pack` gains an option: `prepare_blanket`. Each invocation:
- Increments `world.cache_quality` (0 → 1 → 2 → 3, capped)
- Costs nothing else
- Narration shows the blanket getting rumpled

`inspect` resolution now reads cache_quality:
- quality 0: "I lifted the blanket. The bones are right there."
- quality 1-2: "I lifted the blanket. Found the bones after a second."
- quality 3: "I lifted the blanket. Took me a minute to find them."

`stash_bone` (one or three) does NOT auto-reset cache_quality — Okie's prep persists across deposits within the encounter.

`world.cache_quality` resets between cases (initialWorld).

## Levers the player has

- Whether to prep before stashing (does it matter? See below.)
- How many bones to deposit per visit.

## Levers the player does NOT have (yet)

- An actual *consequence* of cache_quality. Right now it changes inspect-narration and that's it. The mechanic exists; the stake doesn't.
- Watching Okie do the prep on his own. Currently the *player* triggers prep. Could become an autonomous Okie action when cache_quality is low and bones are available.

## Future expansion (priority — this mechanic needs a stake to matter)

- **Discovery risk:** Tex enters the garage in a future scene. Probability of finding-and-chewing a bone = inverse of cache_quality. High prep = safe; low prep = bone loss.
- **Okie autonomy:** at certain ticks, an ambient interrupt fires: "Okie's pawing at the kiddie pool blanket." Auto-increments cache_quality without player input.
- **Generalize the pattern:** add a `prepared` flag to other actions where prep matters (e.g., a pre-walk encounter where you can pre-leash quietly to reduce Attila's whine onset).

## Voice rules

Don't anthropomorphize. Okie isn't "thinking ahead." He's pawing the blanket because pawing the blanket works. Describe the action. "He pawed the blanket up and folded it back." Not "He prepared his hide with the methodical patience of a banker."

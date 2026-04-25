# B004 — Crockett — Toy theft

**Status:** CANON.

## Real-world

When Attila is playing with the squeaky, Crockett sometimes steals it from him.

## Trigger

Another dog actively using a `squeaky_toy` while Crockett is within sight.

## Proposals

- **TEXT:** Ambient interrupt during/after B003's squeak loop: `[Crockett pads in, tail low. The squeaking stops abruptly. Attila blinks.]` Toy ownership flag flips to Crockett. Attila's `frustration` rises.
- **ULTIMA5:** Toy is an inventory-able item with an `owner` field. Crockett's AI, when idle and near Attila+toy, runs a `steal_toy` action that retargets ownership. Attila's sprite plays a brief "🤨" reaction frame.
- **SIMS:** Crockett has a `mischief` or `resource_competition` drive. On B003 broadcast, Crockett's autonomy weighs `steal_toy` vs. `ignore` based on age/energy (arthritis penalty may make him fail or give up). If successful, toy's `possessor` attribute updates; Attila's autonomy may re-acquire or escalate.
- **NES:** Toy is a single sprite with an `owner_id` byte. On steal, sprite attaches to Crockett's position. Squeak SFX stops. Brief "🎵→✂️" animation (2 frames, cheap). Possession contest can be modeled as a coin-flip interrupt in the overworld AI loop.

## Design notes

- Crockett's age should **modulate** this: arthritis means he sometimes *tries* to steal but fails (slow, gives up). Cognitive-decline flavor: occasionally forgets mid-steal and walks away.
- This is the first **inter-dog interaction**. Good flag that v1 (Okie-only) is a proper constraint, not a limitation — multi-dog dynamics belong in v2+.

## Cross-references

- `B003` (Attila squeaky) — the broadcast event this behavior subscribes to.

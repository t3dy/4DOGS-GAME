# B002 — Tex — Belly-roll for rubs

**Status:** CANON.

## Real-world

Tex flops onto his back and lifts his legs, explicitly offering the belly for a rub. Okie does NOT do this — the behavior is a clear distinctiveness marker between the two Aussies.

## Trigger

Player proximity + idle Tex + sufficient bond/trust.

## Proposals

- **TEXT:** `> approach tex` → "Tex collapses theatrically onto his back, legs in the air like an upended beetle." New verb unlocked: `> rub belly`. Each rub raises a `bond` counter.
- **ULTIMA5:** Tex has a "greeting" schedule entry. When the player sprite steps adjacent, Tex's sprite swaps to `belly_up` and a dialogue prompt offers `[R]ub / [L]eave`. Rubbing grants a stat buff ("Content: +2 hours").
- **SIMS:** Belly-roll is an autonomous *solicitation* animation Tex emits when his `social` need is below threshold AND a household human is within 3 tiles. Player can satisfy the ask (rub) or ignore it (decay continues; Tex seeks the next human).
- **NES:** Two sprite poses: `standing` and `belly_up`. `belly_up` uses 4 sprites in a 2×2 arrangement. Player presses A while adjacent → rub animation (brief frame-swap, 1-channel noise "pat pat" SFX).

## Design notes

- This is a **distinctiveness mechanic** — highlights Tex ≠ Okie despite same breed.
- Later: bond counter could gate co-op behaviors (Tex fetches things for you once bond ≥ N).

## Cross-references

- Contrast with `B001` (Okie-only pee behavior) — both are Aussie-specific distinguishing behaviors.

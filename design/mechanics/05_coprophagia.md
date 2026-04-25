# Mechanic 05 — Coprophagia

**Research:** `design/behaviorresearch.md` §5
**Canon:** `canon/dogs.md` (trait flags on Okie/Tex/Crockett); `canon/behaviors/B012_face_lick_risk.md`
**Live encounter:** `bed_face_lick` (#11)

## What this is

Coprophagia is common in dogs (~16% regularly). Causes are debated and usually behavioral. For game purposes: it's the source of the face-lick risk mechanic and a household-management problem (yard-scoop discipline).

## Implementation now

`world.scoop_days_ago` (0 today / 1 yesterday / 99 "I don't want to think about it") modulates the outcome of accepting Okie's face-lick:
- `today` → warm, low-cost
- `yesterday` → mild regret
- `99` → explicit consequence

Player can `dodge`, `accept`, `think` (loops to force commitment), or `eject`.

The `scoop` option in `morning_briefing` resets it to 0.

Coprophagia is a per-dog trait — Attila does NOT have it (his face-licks are safe). Currently the game only invokes the trait via Okie's bedroom encounter.

## Levers the player has

- Scoop the yard at morning briefing (reset to 0).
- Choose whether to accept the lick.
- "Think" to surface scoop status as an in-fiction prompt.

## Levers the player does NOT have (yet)

- Yard-state tracking with actual waste-tile count. Currently `scoop_days_ago` is a single integer, not a tile-level count.
- Attila-as-safe-licker option in any encounter. Could add an Attila bedroom scene where the face-lick is unproblematic.
- Coprophagia patrol: an autonomy where coprophagic dogs sometimes seek out the yard on dirty-yard days.

## Future expansion

- **Yard tile waste:** turn `scoop_days_ago` into a per-tile count of dog-waste objects. Scoop action removes them by tile.
- **Other dogs invoking the same calculation:** if Tex jumps on the bed, the same think-then-decide menu fires.
- **Catching them in the act:** a yard encounter where you can call a dog off mid-action.

## Voice rules

Plain and slightly resigned. Don't overplay the gross-out. "He eats poop. He's about to lick me." That's enough. The "I don't want to think about it" option is the joke; the resolution can stay short.

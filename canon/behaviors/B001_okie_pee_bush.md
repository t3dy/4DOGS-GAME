# B001 — Okie — Territorial pee / bush-kill

**Status:** CANON. Primary v1 behavior.

## Real-world

Okie peed on the blueberry bush that Ted and partner had planted. The bush died.

## Trigger

Player command `pee` on a tile containing a living plant (v1: only the blueberry bush).

## Proposals

- **TEXT:** `> pee on bush` → "Okie lifts a leg. A dark stain spreads. Somewhere, a blueberry bush begins to consider its mortality." Bush tile mutates `alive → yellowing → dead` over N turns. Player can see status via `> look bush`.
- **ULTIMA5:** Tile flag `plant_health: 0–3`. Pee action decrements by 1 per hit; at 0 the tile swaps sprite to `dead_bush`. NPC (human) reacts with scripted dialogue if they witness it within line-of-sight.
- **SIMS:** Okie has a `territoriality` drive that rises on a timer. When high, autonomy picks the nearest *marked* vertical object; if that's the blueberry bush, the bush's `health` attribute drops. Player's only intervention is redirection (call Okie, close gate, put up temporary fence object).
- **NES:** Bush is a 2×2 metatile with three states encoded in 2 bits. Pee action writes to a palette-swap attribute byte; after 3 writes the attribute flips to the "dead" palette. Cheap, fits the mapper.

## Design notes

- Bush-kill is probably a **dark-comedy win condition** for v1, not a loss. Single-dog, single-rule prototype hangs off this behavior.
- Open question: bladder as a resource meter or pee as free action?
- Open question: feel-bad vs. laugh-at tone?

## Cross-references

- `B005` (bone banker) — also Okie, different yard-context behavior.
- `B006` (anxiety) — anxiety may trigger territorial marking.

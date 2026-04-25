# B015 — All four dogs — Dog park zoomies / open-space engagement

**Status:** CANON.

## Real-world

When taken to a dog park, the dogs *do* run around. They engage. Open space + new environment = motion. Contrast with B014 (tennis ball in home yard = nothing).

## Trigger

Location change to `dog_park` (or similar open-space tagged area).

## Proposals

- **TEXT:** Location transition: `> go dog park`. Upon arrival: `[The gate clicks shut behind you. Something changes. Okie's stance shifts. Tex is already moving. Attila surveys. Crockett picks his spot.]` Subsequent turns: dogs have autonomous `run` actions with higher frequency, reducing anxiety (Okie), raising energy (Attila), exhausting Crockett.
- **ULTIMA5:** Dog park is a larger, flat, open map. Dogs' autonomy selects `wander` or `sprint` on a high-frequency timer. Player observes; can call individual dogs to return.
- **SIMS:** Open-space environment raises every dog's `stimulation` stat. Dogs enter `zoomies` autonomous state — a high-energy loop. Player's role is ambient (bring water, watch, call home).
- **NES:** New scrolling background (park). Four dog sprites with idle → run animation swaps. Scroll speed increases as dogs move. Music track swap (from ambient yard to upbeat park).

## Design notes

- **Environment as the hidden mechanic.** Objects fail (B014), environments succeed (B015). The engine should model location as having first-class effects on dog autonomy.
- Validates the **yard as constrained space** — the home yard is where the anxious/comic behaviors happen; the dog park is where the *healthy* behaviors happen.
- Opens multi-location design. The yard is v1, but park/walk/vet/car-trip are natural v2 expansions.

## Cross-references

- Contrast: `B014` (tennis ball disappointment) — objects don't engage.
- `B006` (Okie anxiety) — dog park may lower anxiety; worth testing in-game.
- `B010` (Attila pre-walk whine) — the whine ENDS when the walk begins; park-arrival would be the resolution.

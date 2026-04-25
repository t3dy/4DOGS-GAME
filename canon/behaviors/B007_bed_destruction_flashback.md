# B007 — (historical) — Dog-bed destruction / "flashback" mechanic

**Status:** CANON (as historical fact) / SPECULATIVE (as game mechanic — flashback framing is Ted's proposal).

## Real-world

The dogs used to rip up their dog beds when frustrated. Ted and partner have since switched to kiddie-pool beds with blankets (harder to destroy). Ted explicitly proposed rendering this as a **flashback** mechanic in the game.

## Trigger

Narrative beat — frustration / confinement stressor crosses threshold, OR player inspects a specific object.

## Proposals

- **TEXT:** Italicized interrupt. `[*A memory: shredded foam across the living room floor. A torn bed lining. The dog's tail, low.*]` Triggers when anxiety or confinement pressure spike OR on command `> remember beds`. Non-interactive — purely atmospheric.
- **ULTIMA5:** Cutscene overlay with a desaturated palette swap. Static image of a shredded bed + 2 lines of text. Player clicks through. Can fire stochastically when confinement-duration > N.
- **SIMS:** Modeled as a `trait: bed_destroyer` on each dog, disabled by default in the current era but activatable in a "history mode" setting. When on, high-stress confinement → destruction animation, household inventory loss. Good toggle for players who want chaos.
- **NES:** Single-screen flashback: grayscale palette swap, still image (PPU-efficient — reuse existing tiles with alt attribute table), 2–3 text boxes. A-button advances. Returns to normal play.

## Design notes

- Genuinely **narrative**, not mechanical — about the *emotional register* of the game, not a resource to manage.
- **Tonal risk:** flashbacks risk whiplash in a "cute dog pee game." Open question: dark-comedy tone throughout, or oscillating tender/absurd?
- Good candidate for the FIRST narrative feature after core mechanics stabilize. Parked for v2.

## Cross-references

- `B006` (anxiety) — threshold for triggering this flashback.
- `B005` (kiddie-pool beds) — the *replacement* object is canonical; the flashback makes its replacement meaningful.

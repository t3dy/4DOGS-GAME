# B018 — Okie — Roughhouse solicitation toward Tex

**Status:** CANON. Observed 2026-04-25.

## Real-world

Okie is the one who's always trying to start a roughhousing session with Tex. Approaches with play-bow energy, paws, mouths, body-checks. Tex doesn't always reciprocate.

This is Okie's solicitation behavior — counterpart to Tex's belly-roll (B002), which is solicitation for *contact*. Okie's is solicitation for *play*. Different ask, different dog.

## Trigger

Okie's energy/play-need above threshold + Tex within sight + Tex not actively engaged with something else.

## Proposals

- **TEXT:** Encounter where Okie is pawing at Tex who's just trying to lie there. Player options: let them work it out / call Okie off / encourage / separate.
- **ULTIMA5:** Per-dog `play_need` stat. When Okie's exceeds threshold and Tex is in line-of-sight, autonomy queues `solicit_play(Tex)` action — animation: Okie does the play-bow pose at Tex's tile.
- **SIMS:** Solicitation autonomy with target. Tex has a `tolerance_for_okie` value that decays during the solicitation; at zero, Tex disengages (cross-ref B019).
- **NES:** Two-sprite play-bow animation at Tex's position. Tex's response is a frame-flag (engage / ignore / get up and leave).

## Design notes

- Tex's reciprocation isn't guaranteed — sometimes he plays, sometimes he leaves. Tolerance probably depends on time-of-day, recent engagement, ambient stress.
- Roughhousing is usually fine but in a small house can knock things over / wake people / escalate to uncovered scrap.
- Player intervention can be welcomed (when Tex wants out) or unwelcome (when they were going to play anyway).

## Cross-references

- `B002` — Tex's belly-roll. Different solicitation, same dog as the *target* here.
- `B017` — Okie's garage-avoidance. Possibly an awareness that he's the pesterer.
- `B019` — Tex's retreat. The flip side of this behavior.

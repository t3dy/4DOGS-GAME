# Mechanic 06 — Belly Exposure / Solicitation

**Research:** `design/behaviorresearch.md` §6
**Canon:** `canon/behaviors/B002_tex_belly_roll.md`
**Live encounter:** `tex_belly_roll` (#4)

## What this is

A dog rolling onto its back and exposing the belly is, in Tex's case, solicitation — an active ask for contact, not submission. Confident, secure-attachment behavior. Okie does not do this (per canon).

## Implementation now

`tex_belly_roll` offers four options: rub, rub-and-call-Okie-over (which fails because Okie won't), ignore (step over), photograph-then-rub.

No state mutation beyond `comedies_endured` for the comedic options. The encounter is short and warm.

## Levers the player has

- Engagement intensity (rub vs. photo-then-rub).
- Distinctiveness call-out (call Okie to compare — Tex does this, Okie doesn't).
- Refusal (step over).

## Levers the player does NOT have (yet)

- Bond accumulation. Tex's belly-rub could increment a `tex_bond` stat that gates a future co-op behavior.
- Time-of-day variation. Tex might roll more at certain times.
- Repeat-solicitation if you ignore. The encounter is one-shot.

## Future expansion

- **Bond stat:** tex_bond accrues per rub. At threshold, Tex unlocks a "follow you to the kitchen" autonomy that becomes a positive ambient interrupt.
- **Solicitation ladder:** if first solicitation ignored, Tex re-solicits with a paw-tap (escalation), then a sigh (giving up).
- **Other dogs witnessing:** "Crockett watched the rub from across the room with mild envy. Crockett does not roll."

## Voice rules

Tex's belly-roll is the warmest mechanic in the game. Keep it warm but plain. "Tex flopped onto his back, legs in the air. This is his thing. Okie doesn't do this." The contrast with Okie is the point — make it factual, not analytical.

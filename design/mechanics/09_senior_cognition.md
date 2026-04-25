# Mechanic 09 — Senior Cognition (CDS / Sundowning)

**Research:** `design/behaviorresearch.md` §9
**Canon:** `canon/dogs.md` (Crockett's traits: arthritis, hyperthyroidism, shaking, possible cognitive decline)
**Live encounter:** **NEW** — `crockett_sundowning` (#16 in updated scene index)

## What this is

Canine Cognitive Dysfunction Syndrome (CDS) appears in ~28% of dogs aged 11-12, increasing sharply with age. Symptoms include disorientation, altered sleep-wake cycles, house-soiling regression, reduced response to commands, and confusion at night ("sundowning"). Crockett is 11 and shows possible early signs.

This is also the only mechanic centered on Crockett. Until now he only appeared as the toy-thief in `squeak_steal`. He needed a scene of his own.

## Implementation now

NEW encounter `crockett_sundowning` — late-night, fires from `nighttime_choice` if the player picks "garage" or "house" (not "late_out"). Crockett is up around 2 AM, standing in the hallway, possibly disoriented.

Options:
- **Lead him back to bed** — gentle redirect, success.
- **Sit on the floor with him** — co-regulation, takes longer but settles him.
- **Offer water** — sometimes works; sometimes he forgets why he's there.
- **Leave him be** — he wanders back eventually or doesn't.

State touched: `world.crockett_episodes` increments per occurrence. Could be referenced in debrief.

## Levers the player has

- Intervention style (active redirect, passive co-regulation, indirect via water, hands-off).
- Whether to even run this encounter (player chose nighttime sleep arrangement).

## Levers the player does NOT have (yet)

- Vet referral / medication paths (real-world: SAM-e, selegiline, dietary changes — but DOGSGAME is not a medical sim).
- Day-time signs of decline (CDS isn't only nighttime). Could add to morning_briefing variations.
- Crockett's command-response decline. Currently no encounter exercises commands with him.

## Future expansion

- **Daytime CDS markers:** Crockett occasionally fails to respond when called by name (named in ambient interrupts).
- **Scoring:** a `crockett_settled_count` that affects debrief tone — caring for him well unlocks a tender ending variant.
- **Linked to `B004` toy-theft:** at high crockett_episodes, theft attempts sometimes fail because he loses focus mid-action ("Crockett walked toward the pig, stopped, sat down, forgot what he was doing").

## Voice rules

This is the most tender mechanic. Easy to tip into sentimentality — don't. Plain. "Crockett's standing in the hallway. He doesn't seem to know what he's doing." Period. The reader fills in the feeling. The dog is real. The decline is real.

NEVER write Crockett as comic relief in this scene. The toy-theft scene can be funny. This one is not. Different register, same plain voice.

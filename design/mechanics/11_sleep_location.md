# Mechanic 11 — Sleep Location & Housetraining Regression

**Research:** `design/behaviorresearch.md` §11
**Canon:** `canon/behaviors/B008_okie_nighttime_accident.md`
**Live encounter:** `nighttime_choice` (#15)

## What this is

Okie shits in the house at night if left inside. The garage is the management solution AND his preference. This is real — confining a known indoor-shitter to an easy-clean space is documented best practice, not punishment. And the dog often prefers it (low-stim, predictable, his own space).

## Implementation now

`nighttime_choice` offers four sleep arrangements: garage (canon, no consequence), house (sets `sleep_location: house`, raises `comedies_endured`, foreshadows morning trouble), bedroom-floor (also sets `house`, with the snoring/4 AM detail), late-out (one-more-trip, then loops back to the choice).

`world.sleep_location` is set. `morning_briefing` reads it next morning to vary the opening line.

## Levers the player has

- Where Okie sleeps tonight (4 options).
- Whether to take him out one more time first.

## Levers the player does NOT have (yet)

- A morning-after encounter that actually shows the indoor mess. The current implementation foreshadows it; doesn't render the consequence.
- Per-dog sleep arrangement. Crockett, Tex, Attila don't have sleep-location options.
- Multi-night patterns. Each session resets.

## Future expansion

- **Morning consequence encounter:** if `sleep_location === "house"` at start of a new case, fire a `morning_clean_up` encounter that costs time and rules out a different morning option.
- **Senior-related: Crockett's sleep location matters too.** Sundowning + sleeping in a far room = night-wandering risk (link to Mechanic 09).
- **All-four sleep choice:** end-of-day encounter where you place each dog. Weight implications.

## Voice rules

The reality framing — "he prefers the garage anyway" — is canonical and important. Don't write the garage as banishment. Don't write the house-sleep as a treat. Both are pragmatic. Ted's framing in real conversation: "we've started having him sleep in the garage which is what he seems to prefer anyway." Match that flatness.

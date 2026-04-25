# Mechanic 04 — Resource Guarding & Inter-dog Theft

**Research:** `design/behaviorresearch.md` §4
**Canon:** `canon/behaviors/B003_attila_squeaky.md`, `B004_crockett_toy_theft.md`
**Live encounter:** `squeak_steal` (#7)

## What this is

Dogs guard items they value. Theft attempts often happen on opportunity (owner distracted, item momentarily unattended). Crockett's pig-theft from Attila is a classic case: he doesn't grab when Attila is engaged with it, he waits until the squeaking stops or Attila looks away.

## Implementation now

`squeak_steal` resolves four ways:
- `engage` — sit with Attila → no theft.
- `ignore` — don't engage → Crockett pads in, takes the pig.
- `intercept` — pet Crockett first → defers but doesn't prevent.
- `watch` — observe → theft happens around second 47.

The pig-as-object isn't currently modeled with `owner` / `guard_value` fields — the theft outcome is hardcoded in the encounter resolution.

## Levers the player has

- Whether to engage Attila's solicitation (which is what stops the theft loop).
- Whether to redirect Crockett's attention.

## Levers the player does NOT have (yet)

- Attila contesting the theft. In real life he doesn't push back; we could model that.
- Multi-toy economy (pink pig vs. blue cow). Currently treated as one toy.
- Theft of Okie's bones. The bone bank is currently theft-immune. Could become risk-bearing.

## Future expansion

- **Object model:** every carryable thing gets `{owner, value, guard_strength}`. Theft is a probabilistic action calculated from (thief boldness − owner guard_strength). Crockett: high boldness, doesn't fight back if contested.
- **Guarding warning:** in scenes where guarding could fire, add an option `take it from him` that triggers a guard reaction (growl, freeze, tooth-bared). Important: Ted's dogs may not actually guard. Don't write this without confirming.
- **Pig vs. cow distinction:** different attention values for each toy. Cow sometimes ignored, pig always works.

## Voice rules

Theft is not adversarial here. It's just what Crockett does. "Crockett got up and stole the pig." Not "Crockett executed a calculated raid." Plain.

# Mechanic 15 — Breed-Typical Behaviors

**Research:** `design/behaviorresearch.md` §15
**Canon:** `canon/dogs.md` (per-dog breed + trait listings)
**Live encounters:** none dedicated; breed-traits cross-cut every other encounter

## What this is

Breed carries tendencies, not destinies. Aussies (Okie + Tex) are herders by selection — high stimulation needs, anxiety when under-exercised, territorial marking, bark-prone. Bernese mountain dogs and crosses (Attila) are typically slow, gentle, lean-into-people, mild. Senior dogs of any breed run hotter on age effects than breed effects (Crockett).

This is a *cross-cutting* mechanic. It doesn't deserve its own encounter; it should bias every other encounter.

## Implementation now

Currently breed-typical behaviors are baked into the encounter narration directly:
- Aussie aggression-towards-bush (B001) — Okie's territorial marking is breed-influenced.
- Bark chain (B009) — both Aussies, both bark-prone.
- Attila's mild-mannered framing in `bed_face_lick` and `attila_bed_petting`.
- Crockett's age-effects in flavor lines and the new `crockett_sundowning` encounter.

There's no shared `breed_traits: list[str]` or `breed_bias` system. Each encounter hardcodes the relevant trait.

## Levers the player has

- None directly. Breed is descriptive, not actionable.

## Levers the player does NOT have (yet)

- Choosing a different POV dog. Currently Okie is implicitly the protagonist. A "play as Tex" mode would surface Aussie traits differently.
- A breed-bias system that probabilistically modulates encounter outcomes (e.g., Aussies twice as likely to instigate bark chains, Bernese rarely).

## Future expansion

- **Breed_bias dict per dog:** `{aussie: {bark_chain_propensity: 0.8, herding: 0.5, marking: 0.7}, bernese: {leaning: 0.9, vocal_restraint: 0.6}}`. Other mechanics consult this dict.
- **Per-dog POV mode:** entire alternate runs from Tex's, Attila's, or Crockett's perspective. Same encounters, different protagonist, different available actions.
- **Aussie herding scene:** if Ted confirms either Aussie herds the household, add an encounter (currently flagged as unobserved in `behaviorresearch.md` §"Behaviors NOT yet observed").

## Voice rules

Breed talk in narration is risky — easy to slip into trope. Stick to specific behaviors, not breed labels. "Okie barks more than Attila" is fine. "As an Australian shepherd, Okie's herding instinct..." is not.

Ted's own framing: "the Aussies don't try to get up on the bed very often" is the right register. Plural-first ("the Aussies") to mark the breed grouping, then describe what they do.

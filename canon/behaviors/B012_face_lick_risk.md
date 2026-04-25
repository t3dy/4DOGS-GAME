# B012 — Okie (+ Tex, Crockett) — Face-lick attempt / poop-eating risk calculation

**Status:** CANON. Mechanically rich — Ted has proposed specific game mechanics for this.

## Real-world

Sometimes when Ted is lying down in bed in the afternoon (not sleeping), Okie will come and join him on the bed. Ted avoids letting Okie, Tex, or Crockett lick him — because they eat poop. Okie and Tex *always* try to lick his face when presented the opportunity. Attila does not carry the coprophagia flag and is safer.

Ted's proposed mechanic: the player decides whether to dodge the lick or accept it, based on a **self-honesty calculation about yard-scoop discipline** — "have I scooped the yard today?"

## Trigger

Face proximity (player lying down, dog approaching head) + dog has high social drive + coprophagic flag.

## Proposals

- **TEXT:** When Okie approaches on the bed: `[Okie's tongue deploys. You have approximately two seconds.] > _`. Available verbs: `dodge`, `accept`, `think`. `> think` gives a reflective prompt: `How long has it been since you scooped the yard? [today / yesterday / I don't want to talk about it]`. The answer modulates the outcome.
  - `today` → accept = warm moment, no consequence.
  - `yesterday` → accept = mild "you regret this" text.
  - `I don't want to talk about it` → accept = explicit consequence ("You will taste this for hours").
- **ULTIMA5:** Face-lick attempt fires a menu: `[D]odge / [A]ccept / [T]hink`. `[T]hink` opens a reflection overlay with the yard-scoop status pulled from world state (actual tile counts of `dog_waste` objects). No lying to yourself — the game knows.
- **SIMS:** The mechanic becomes objective. `yard_cleanliness` is a world variable. Face-lick quality is a function of it. Player dodge-rate success is a function of dog social drive + reflexes. Coprophagia is a dog-level trait surfaced in inspector.
- **NES:** Simple risk/reward dialog. Face-lick attempt freezes the screen, shows a 2-frame lick animation starting, then A=dodge / B=accept. A timer (6 frames) forces the decision. Outcome screen uses yard-scoop state to pick one of three text strings. Minimal memory, high comedy.

## Design notes

- **This is a best-in-class mechanic.** It ties a physical-world action (scoop the yard) to a social interaction (accept the lick) to a moment of self-honesty (do I want to know?). Compact, comic, real.
- **Ted's "I don't want to talk about it" option is the gem.** The game acknowledges willful ignorance as a choice. This is a narrative mood move, not just a mechanic.
- Design question: does `think` *show* the true state, or let the player self-report and honor whatever they say? Ted's framing ("hope he hasn't eaten poop lately") suggests the player *might not know* — the uncertainty is the interesting part. Probably: in SIMS and ULTIMA5 show the truth; in TEXT let the player self-report and resolve to the honest answer when possible.
- Cross-system: `yard_scoop` state is a new world variable. Would need B001's tile model extended with a `waste_count` per tile.

## Cross-references

- `B008` (nighttime indoor-shit) — feeds the indoor-waste case.
- `B011` (bed session) — primary context in which this mechanic fires.
- `B013` (Attila bed-petting) — contrast: Attila does not face-lick, pets differently.
- `canon/dogs.md` — coprophagia flag on Okie, Tex, Crockett.

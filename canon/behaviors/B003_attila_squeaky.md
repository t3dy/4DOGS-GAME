# B003 — Attila — Squeaky-toy attention-signal

**Status:** CANON.

## Real-world

Attila has two chew toys — a pink pig and a blue cow. Sometimes he just plays with them. But when he wants attention from a human, he *deliberately* works the squeak to summon you. It's a signal, not just play.

## Trigger

Attila's `attention_need` rising above threshold while a human is in the house but not engaging with him.

## Proposals

- **TEXT:** Ambient interrupt. Between player turns, the parser injects: `[From the living room: SQUEAK. SQUEAK. SQUEAK.]` Ignoring it N turns raises Attila's frustration. `> find attila` or `> go living room` satisfies it; engaging gives an `attention_given` reward and silences the squeaks.
- **ULTIMA5:** Attila is a scheduled NPC with a "request attention" state. When active, a speech-balloon overlay with a `♪` icon follows his sprite. Adjacent-and-interact clears the state; ignoring too long triggers a "disappointed" schedule branch (sulks on dog bed).
- **SIMS:** Most direct fit. `attention_need` is a float that fills on a timer. When high AND a toy is within reach, Attila's autonomy chooses `play_squeaky` with elevated broadcast radius — other agents (humans + dogs) receive the "attention solicitation" signal. Player engagement lowers the need; Crockett receiving the signal may trigger B004.
- **NES:** Squeak is a 1-channel pulse-wave SFX (roughly 2 frames, pitch bend up). A tiny `♪` icon appears over Attila's sprite. The signal is broadcast to any NPC within a fixed tile radius — Crockett's AI has a hook that triggers the steal behavior (B004) on receipt.

## Design notes

- First **multi-object, multi-dog, agent-broadcast** behavior. Milestone moment in the design.
- Pig vs cow: cosmetic skins on a single `squeaky_toy` object in v1. Distinct only if we later decide differentiation matters.
- Opens: toy ownership, toy location persistence, toy theft (see B004).

## Cross-references

- `B004` (Crockett toy-theft) — subscribes to this broadcast.
- `B010` (Attila pre-walk whine) — different vocalization context; confirms Attila has a full vocal repertoire.

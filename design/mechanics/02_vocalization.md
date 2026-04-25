# Mechanic 02 — Vocalization Repertoire

**Research:** `design/behaviorresearch.md` §2
**Canon:** `canon/behaviors/B003_attila_squeaky.md`, `B009_okie_tex_bark_chain.md`, `B010_attila_prewalk_whine.md`
**Live encounters:** `squeak_steal` (#7), `yard_passerby` (#3), `attila_whine` (#8)

## What this is

Dogs produce structurally different vocalizations for different contexts. Bark, whine, growl, howl, alert-bark, play-bark, squeak-via-toy — each signals different things. Treating them as one "make sound" verb misses the whole point.

## Implementation now

Each vocalization has its own narration in its own encounter:
- **Squeak (Attila / pig)** in `squeak_steal` — deliberate signal.
- **Bark chain (Okie + Tex)** in `yard_passerby` — feedback-amplified.
- **Whine (Attila)** in `attila_whine` — pre-walk, pitch-rising.

Journal records the vocalization type when it happens.

## Levers the player has

- In `squeak_steal`: respond, ignore, intercept, watch. Each changes who ends up with the toy.
- In `yard_passerby`: shush, listen, join. The listen path scores a "comedy endured."
- In `attila_whine`: leash, wait, abandon, bring Okie. Whine continues or stops based on choice.

## Levers the player does NOT have (yet)

- A unified vocalization sub-system that can fire per-context vocals from any dog. Currently each vocal lives inside its own encounter. Refactoring is parked.
- Volume / pitch metering. Currently boolean: vocal is happening or not.

## Future expansion

- **Sound enable in browser:** distinct audio cue per vocal type (whine = triangle wave, bark = noise burst, squeak = short pulse). Optional toggle.
- **Vocal interruption mechanic:** an ongoing whine or bark-chain blocks the player from picking some options ("can't think over the noise").
- **Calling encounter:** a new encounter where the player must identify which dog is making which sound from offscreen.

## Voice rules

Don't editorialize the sound itself. Plain description. "Attila whined. He's 100 pounds and the whine sounds ridiculous." NOT "the whine has become a matter of principle." The juxtaposition is in the facts, not in the narration.

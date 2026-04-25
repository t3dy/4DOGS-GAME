# Mechanic 13 — Co-regulation / Bonding

**Research:** `design/behaviorresearch.md` §13
**Canon:** `canon/behaviors/B011_four_dog_bed_session.md`, `B006_okie_anxiety_garage.md` (the comfort path), `B010_attila_prewalk_whine.md` (bring-Okie path)
**Live encounters:** `four_dog_bed_session` (#14), comfort branches in `garage_okie_anxious` and `attila_whine`

## What this is

Mutual gaze, co-resting, proximity → mutual oxytocin and downward arousal regulation. A calm dog calms an anxious dog. A calm human calms a sensitive dog. The four-dog bed session is the central image: everybody in proximity, nobody fully watching the movie, anxiety drops across the board.

## Implementation now

Co-regulation effects appear in three places:
- **`garage_okie_anxious` → `comfort` option:** sitting with Okie drops his anxiety by 3 (the biggest single drop).
- **`attila_whine` → `bring_okie` option:** Attila stops whining when Okie is leashed up too; Okie's anxiety drops by 1.
- **`four_dog_bed_session` → `hold` option:** drops Okie's anxiety by 2 with all four present.

`world.okie_anxiety` is the only inter-character regulated stat right now. The other dogs don't have anxiety values yet.

## Levers the player has

- Choose comfort over distraction.
- Bring multiple dogs together for proximity effects.
- Allow the bed session even when Aussies are normally banned.

## Levers the player does NOT have (yet)

- Per-dog anxiety (so co-regulation could lower more than just Okie's).
- Time-locked proximity (must be in the same scene for N ticks for the effect to fire).
- Negative co-regulation (if the player's stress-state were modeled, it could spike Okie's anxiety).

## Future expansion

- **Per-dog anxiety:** add `tex_anxiety`, `attila_anxiety`, `crockett_anxiety` (each with their own baselines). Co-regulation drifts each pair toward the lower value.
- **Bonded-pair table:** a matrix of bond values between every pair of dogs. Strong bonds amplify co-regulation; weak bonds blunt it.
- **Player as anxiety source:** an optional toggle where the player's recent choice quality affects the anxiety floor. Would require a "calm vs. frantic" inference on player actions.

## Voice rules

The four-dog bed session is the warmest scene. Plain WARM. "I stayed there. Hand on Attila, foot near Tex, elbow on Crockett, Okie's chin on my arm." This is canonical: list the dogs, list the touch points, don't editorialize. The tenderness is in the inventory.

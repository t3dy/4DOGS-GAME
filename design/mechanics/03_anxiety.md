# Mechanic 03 — Anxiety / Stress Signaling

**Research:** `design/behaviorresearch.md` §3
**Canon:** `canon/behaviors/B006_okie_anxiety_garage.md`, `B007_bed_destruction_flashback.md`
**Live encounters:** `garage_okie_anxious` (#6), auto-triggered `bed_destruction_flashback` (#13)

## What this is

Dogs signal stress through pacing, panting, hypervigilance, displacement behaviors (lip-licking, yawning out of context, ground-sniffing), and seeking enclosed spaces. The garage-as-bunker for Okie is textbook safe-space-seeking.

## Implementation now

`world.okie_anxiety` (0-10, baseline 3) is a real first-class stat:
- **Decays** toward 3 each tick (`tickWorld()`)
- **Risen** by ignoring his pacing in `garage_okie_anxious`, by scenes that imply confinement
- **Lowered** by comfort, toy distraction, scoop-diversion, dog park (B015), four-dog bed session (B011)
- **Auto-triggers `bed_destruction_flashback`** when it crests 8 (one-shot per run)
- **Modulates narration** in `bed_face_lick` when ≥ 6 ("Okie's been pacing all morning")

HUD bar shows current anxiety. Journal logs the flashback trigger.

## Levers the player has

- Direct: comfort, toy, ignore, scoop-diversion, take-to-park, group-bed-session.
- Indirect: how long the player leaves Okie alone in the garage before checking.

## Levers the player does NOT have (yet)

- Acute stressor events (storm, loud noise, stranger arriving). The anxiety floor is currently driven only by player choice, not by world events.
- Anxiety contagion to other dogs. Real households have one anxious dog winding the others up.
- Calming-signal narration (yawn, lip-lick) as ambient cues — could be added to `AMBIENTS` pool.

## Future expansion

- **Storm encounter:** rare external event raises every dog's anxiety, gates several normal options ("Okie won't leave the garage").
- **Calming signals as ambient:** add yawn-out-of-context lines to the AMBIENTS pool, weighted by current anxiety value.
- **Anxiety thresholds for option availability:** very high anxiety could grey out "go to dog park" with the rationale "he won't get in the car."

## Voice rules

Describe behavior, not the dog's internal experience. "He paced." "He pressed against my leg." NOT "the anxiety crested and he sought refuge." The science word `anxiety` is fine in stat names but should not appear in narration except where Ted would naturally use it.

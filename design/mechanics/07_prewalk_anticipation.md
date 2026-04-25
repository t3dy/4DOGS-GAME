# Mechanic 07 — Pre-Walk Anticipation

**Research:** `design/behaviorresearch.md` §7
**Canon:** `canon/behaviors/B010_attila_prewalk_whine.md`
**Live encounter:** `attila_whine` (#8)

## What this is

Anticipatory arousal at threshold cues (leash, door) is often disproportionate to the walk reward itself. Attila's whine is the canonical example: small voice, big body, escalates as the door rises, and continues *after* the door is open. The whine is about the threshold, not the walk.

## Implementation now

`attila_whine` offers leash-now, wait-quiet, abandon, or bring-Okie (gated by Okie's anxiety ≤ 4). The whine doesn't stop on its own — `wait_quiet` loops back. `leash_now` and `bring_okie` set `world.leashed` and `world.garage_door_open` true.

## Levers the player has

- Leash and go (whine continues briefly into the walk).
- Wait (futile).
- Abandon (Attila stops, but a wronged silence follows).
- Bring Okie (compounds the situation; Okie's anxiety eases).

## Levers the player does NOT have (yet)

- The actual walk. There's no walk encounter; the whine is the only walk-related scene.
- Leash-cue conditioning over many sessions (a dog who eventually stops whining if you reliably never abandon).
- Other dogs reacting to the whine from inside the house.

## Future expansion

- **Walk encounter:** what actually happens on the walk. Could include B015-style park transition, bark-at-other-dog encounters, or the gate-incident-style consequence path if a leash slips.
- **Whine intensity meter:** visible 0-10 number that climbs through the leash → door sequence.
- **Conditioning curve:** a long-term `attila_walk_predictability` stat — if it's high (player reliably walks when leash comes out), whine onset is faster but resolution is faster too.

## Voice rules

The juxtaposition is the joke (big dog, small voice). Don't punch the joke — let the facts carry it. "He's 100 pounds and the whine sounds ridiculous coming out of him." Period. No "pitched like a kettle."

# Mechanic 08 — Bark Contagion

**Research:** `design/behaviorresearch.md` §8
**Canon:** `canon/behaviors/B009_okie_tex_bark_chain.md`
**Live encounter:** `yard_passerby` (#3)

## What this is

In multi-dog households, one dog's alert bark sets off others. The chorus often outlives the trigger — Ted has clocked Okie + Tex going six more seconds after the truck is past. Setting: 15th Ave in Sultan, WA (real road, real traffic).

## Implementation now

`yard_passerby` fires after `yard_bush` if the player chose `call_off`. It offers shush, listen, or join. Listen is the canon path (Ted's "I count the principles" = real observation).

No `peace` stat or neighbor reaction yet — the encounter is self-contained.

## Levers the player has

- Intervene (shush)
- Observe (listen)
- Participate (join)

## Levers the player does NOT have (yet)

- Bark trigger on demand (no "another truck passed" interrupt later in the case).
- A `neighbor_goodwill` stat that erodes with chorus events.
- Time-of-day variation. Real bark chains at 2 AM are a different kind of problem; the encounter doesn't model that.

## Future expansion

- **Random passerby interrupts:** add to ambient interrupt pool. Small chance per tick when scene location is "yard" or "garage": car passes, dogs bark, ambient passes.
- **Neighbor goodwill stat:** a `peace` value that depletes with bark events and recovers slowly. Unlocks a "neighbor knocks on the door" rare encounter at low peace.
- **Time-aware variants:** the same bark chain at noon ("they're being dogs") vs. at 2 AM ("oh no"). Different score outcomes.

## Voice rules

Plain truck. Plain bark. Six-second count is canon — keep it. "I listened. They went six more seconds after the truck was gone." Don't poetize the dog logic; Ted's deadpan IS the joke.

# B019 — Tex — Garage retreat from Okie's pestering

**Status:** CANON. Observed 2026-04-25.

## Real-world

Tex sometimes wants to go into the garage and it almost seems like he's trying to get away from Okie. He'll pad in there when Okie's been working him for play (B018), and once inside he settles. Attila often comes too.

This re-frames the garage. For Okie it's a refuge from anxiety (B006). For Tex it's a refuge from a specific dog. Same room, two functions.

## Trigger

Okie's roughhouse solicitation (B018) sustained past Tex's tolerance + garage door open.

## Proposals

- **TEXT:** Encounter from Tex's POV (or Ted's-observing): Okie's been at Tex for a while, Tex gets up and walks to the garage. Player options: open the door for him / block / let him try other rooms / pick up Okie.
- **ULTIMA5:** Tex has a `tolerance_for_okie` stat. When it bottoms out, Tex's autonomy queues `seek_garage`. Path-finds to the garage door tile. Sprite waits if door is closed.
- **SIMS:** Refuge-seeking autonomy. Triggers on `(annoyance_source detected) AND (refuge_available)`. The garage tile has `refuge_value` for Tex.
- **NES:** Tex sprite turns and walks to the garage door. Door-open animation if the door's open; halt-and-wait if closed.

## Design notes

- This explains B017 if you read it sideways: the others may go in *because* of Okie's behavior, and Okie's avoidance may be him reading that he's the cause.
- Attila sometimes follows Tex, suggesting Attila's preference is for "wherever Tex is calm" rather than the garage per se.
- Player can intervene by managing Okie's energy upstream — walks (B015), attention (B003-style engagement) — or by opening/closing doors.

## Cross-references

- `B006` — Okie's anxiety refuge. Same room, opposite emotional purpose.
- `B017` — Okie's avoidance. The other half of this dynamic.
- `B018` — the cause. Okie's solicitation pushed past Tex's tolerance.

# B011 — All four dogs — Monthly TV/movie bed session

**Status:** CANON.

## Real-world

Ted and partner usually discourage the Aussies (Okie, Tex) from getting on the bed. It's hard to get them to lie down and stay still. However, roughly **once a month**, Ted and partner do a deliberate TV/movie session in bed with *all four* dogs hanging out together. It's a rare, deliberate, chaotic event.

## Trigger

Player-initiated (command-based or time-of-day-based). Not autonomous.

## Proposals

- **TEXT:** `> invite all dogs on bed` → "You pat the comforter and say the magic words. The Aussies, usually banished, look suspicious. Attila bounds up first. Crockett takes several attempts." Then a multi-turn segment where the player tries to hold an equilibrium: dogs shift, demand pets, consider leaving, consider licking (see B012, B013).
- **ULTIMA5:** Event-triggered cutscene that transitions to an interior "bedroom" map with all four dogs loaded. Player in center tile; dogs orbit. Time-compressed turn system while on the bed.
- **SIMS:** Special "household bonding" mode. Normally Aussies have a `bed_allowed` flag = false. This mode temporarily flips it. All four dogs enter a `bed_occupy` state. Satisfaction of all four ticking up; exit condition is player-driven ("movie ends").
- **NES:** A rare unlockable screen (monthly cadence). Single-screen static background (bedroom + TV glow). Four dog sprites arranged on the bed with idle animations. A-button = pet the dog the cursor is on, increments a "family bond" counter.

## Design notes

- This is an **equilibrium-maintenance mechanic**, not a progression mechanic. The fun is in keeping it going without it collapsing.
- Cross-system pressure: on the bed, B012 (face-lick risk) and B013 (Attila paw-request) both activate. B011 is the *container* in which those behaviors become frequent.
- "Once a month" is canonical cadence — might be a rare feature unlock, a monthly calendar event, or seasonal flavor.
- Tonal note: this is the *warm* behavior. Other behaviors trend comic/chaotic. This one is the emotional counterweight. Miriam (narrative designer) would flag this as important.

## Cross-references

- `B012` (face-lick risk) — activates during bed proximity.
- `B013` (Attila bed-petting demand + command-resistance) — central to bed-session chaos.
- `B006` (Okie anxiety) — bed-session may serve as anxiety-lowering via social contact.

## Household-rule implications

See `canon/dogs.md` §"Household rules": Aussies normally off the bed. This behavior is the documented exception.

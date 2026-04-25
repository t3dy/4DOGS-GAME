# B009 — Okie + Tex — Garage bark chain / traffic reactivity

**Status:** CANON.

## Real-world

Okie and Tex, together in the garage, will egg each other on barking as neighbors or cars pass. Setting: 15th Ave, Sultan, WA, off Basin Hill Rd — quiet rural road with intermittent traffic (logging trucks, neighbor SUVs, mail carrier).

## Trigger

External `passerby_event` fires (car, neighbor, other dog being walked) + 2+ dogs in garage.

## Proposals

- **TEXT:** Ambient interrupt during garage scenes: `[A car rumbles up 15th Ave. Okie barks. Tex barks back. They amplify.]` Flavor text varies with passerby type. Peaks if ignored; ends when the passerby timer expires.
- **ULTIMA5:** Scheduled NPC traffic on the street tile edge of the map. Dog sprites in garage gain a "barking" state on proximity. Neighbor NPC may emit a `:(` bubble if it's 2am.
- **SIMS:** **World-level `passerby_spawn` event on a Poisson timer** seeded by time-of-day (more during commuter hours, sparse at night). Each dog in garage has `reactivity` (Okie: high, Tex: medium-high). Combined reactivity = feedback-multiplied; bark_duration scales non-linearly with dog-count in shared space. Good test of agent-to-agent amplification.
- **NES:** Street runs along top of garage scroll-screen. Car sprites scroll L→R periodically. On pass, dog-sprite frame flips to "barking"; APU noise channel plays short 8-frame bark, ch1 pulse overlay for Tex's deeper bark.

## Design notes

- **External world hook** — proves the engine isn't a closed yard. 15th Ave traffic is the first scheduled world-event.
- Open: does barking raise or lower Okie's anxiety? (Instinct: spikes then crashes.)
- **"Sultan, WA" is canonical location flavor.** Bake into background narration.

## Cross-references

- `B006` (Okie anxiety) — bark chain affects anxiety trajectory.
- `B010` (Attila whine) — different vocalization, proves the engine needs a per-context vocal repertoire.

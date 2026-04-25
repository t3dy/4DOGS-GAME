# B008 — Okie — Nighttime indoor-shit / garage-sleep preference

**Status:** CANON.

## Real-world

Even when let out late, Okie will shit on the floor overnight if left inside. Ted and partner now have him sleep in the garage, which Okie actually prefers.

## Trigger

Night-time tick + Okie inside the house + bowel timer above threshold.

## Proposals

- **TEXT:** On `> sleep` command or end-of-day, prompt: `Where does Okie sleep? [house / garage]`. If house → morning event: `[You wake to a familiar smell. Okie looks up at you, unrepentant.]` If garage → morning event: `[The garage is undisturbed. Okie emerges, relaxed.]`
- **ULTIMA5:** Day/night cycle. Okie has a sleep-location attribute. Indoor sleep + bowel-timer expired → map dirty-tile spawn on a random interior square. Garage sleep = no event.
- **SIMS:** `bowel` stat integrates over time. Housetrain-reliability is an Okie-specific trait (low). At night, bowel_full + house_location → accident object spawns. Resolves player frustration; drives the design of the "sleep in garage" affordance.
- **NES:** Morning screen-transition has two branches based on last night's sleep-location byte. Sprite swap: clean-floor tile vs. stinky-floor tile (palette + attribute change).

## Design notes

- First genuinely **negative feedback loop** against keeping Okie inside. The player *learns* garage-preference is the correct solution.
- Okie's preference aligns with the practical solution — design should make this discoverable, not punishing.
- Real-world: Ted scoops the yard periodically. If he's been lax, the yard accumulates dog waste. This affects B012 (face-lick risk calculation) — cross-system interaction.

## Cross-references

- `B006` (anxiety) — garage is also anxiety-lowering.
- `B005` (bone bank) — garage is also where Okie banks bones. Three reasons Okie wants to be in the garage.
- `B012` (face-lick risk) — coprophagia in the yard interacts with scoop-discipline.

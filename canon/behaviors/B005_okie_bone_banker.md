# B005 — Okie — Bone banker

**Status:** CANON.

## Real-world

Okie asks to be let into the garage specifically to **stash rawhide bones** under the blankets of the kiddie-pool dog beds. Bones come in 12–20 count packs, Old Roy brand from Walmart. He is the designated bone banker of the household.

## Trigger

Okie possesses a bone + garage is accessible + `anxiety` or `hoarding` drive above threshold.

## Proposals

- **TEXT:** `> ask to go in garage` → door opens (if human agrees). Inside: `> stash bone under blanket`. Bone inventory persists in a hidden `bone_cache` list tied to the kiddie-pool bed object. `> look under blanket` reveals the count, which grows over the session. Bone cache is a scorable endgame stat — "Okie banked 14 bones this week."
- **ULTIMA5:** Garage is a separate map. Kiddie-pool bed is an interactable container tile. Bones are inventory items with stack count. Okie has a scheduled action `bank_bone` that fires when `held_bone == true` and pathing to the garage is clear. Container can be opened by the player for a nostalgic "count the hoard" moment.
- **SIMS:** `hoarding` drive rises when a fresh bone enters the household (player unpacks the 20-pack → event broadcast). Okie's autonomy selects `carry_bone → seek_garage → stash`. Bone count on the kiddie-pool object is publicly inspectable; other dogs' autonomy may run a raid action (future candidate).
- **NES:** Garage as a separate room (scroll transition). Kiddie-pool bed is a 2×2 metatile with an "under blanket" bit. Bones are a counter in WRAM (single byte, caps at 255 — plenty). Icon in corner of HUD shows current cache when Okie is in the garage.

## Design notes

- **Hoarding / scoring mechanic.** Could become the primary secondary objective alongside B001 bush-kill.
- **"Old Roy 20-pack from Walmart"** is canonical flavor — must appear in flavor text somewhere.
- Open: do bones *do* anything (currency, trade, chewed-over-time consumable) or are they purely collected? Cleanest v1 answer: pure collection, nostalgic ritual.
- Miriam (narrative designer) flagged this as the most interesting mechanic so far: the dog *chooses* to hide bones, unmotivated. Character mechanic, not goal mechanic.

## Cross-references

- `B006` (anxiety) — the *reason* Okie goes to the garage.
- `B005` is *what he does there*.

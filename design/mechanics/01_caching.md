# Mechanic 01 — Caching / Hoarding

**Research:** `design/behaviorresearch.md` §1
**Canon:** `canon/behaviors/B005_okie_bone_banker.md`
**Live encounter(s):** `garage_bone_pack` (#5 in scene index)

## What this is

Dogs cache surplus food and revisit hides. Some dogs *modify the cache substrate* — pawing dirt, rearranging blankets — which is a planning behavior, not pure instinct. Okie does both.

## Implementation now

`garage_bone_pack` lets the player give Okie 1 or 3 bones, watch him stash them under the kiddie-pool blanket, inspect the cache, or close the bag.

State: `world.bones_in_pack`, `world.bone_cache`. Both persist across encounters. Cache shows up in HUD.

Plus (new): `world.cache_quality` (0-3) raised by the `prepare_blanket` option — see Mechanic 10 (Tool use).

## Levers the player has

- Number of bones to deposit (1 vs. 3 vs. close-bag).
- Whether to prepare the blanket first (raises hide quality).
- Whether to inspect the cache (mostly flavor; could become a "Okie sees you snooping" risk).

## Levers the player does NOT have (yet)

- Other dogs raiding Okie's cache. The science says cache theft happens; the game currently has only Crockett-on-Attila theft (B004), not Okie-targeted theft.
- Okie re-caching when disturbed. If we wanted, "inspect" could trigger Okie to move the bones later in the session.
- Long-term cache memory across days. Multi-day persistence is parked.

## Future expansion

- **Cache discovery:** if Tex enters the garage with Okie's cache_quality < 2, small chance Tex finds and chews a bone. Costs Okie 1 cache, raises Okie's anxiety.
- **Cache forgetting:** rare, but documented in canids — they sometimes can't find their own cache. Would be an emergent comedy moment.
- **Bone economy:** introduce a `bones_chewed_by_other_dogs` counter as the antagonist to `bone_cache`.

## Voice rules

Okie does NOT plan in human terms. Don't write him as a banker doing math. He prepares blankets because it works. Describe what he does, not what he thinks. ("He pawed the blanket up first. Then he put the bone under.")

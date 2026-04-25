# Mechanics — Index

Per-topic documentation for each behavior category in `behaviorresearch.md`. Each doc maps research to live encounter, lists levers the player has, lists levers we haven't built yet, and proposes future expansion. Each ends with **voice rules** specific to that mechanic.

| # | Topic | Doc | Live encounter(s) | Status |
|---|-------|-----|--------------------|--------|
| 01 | Caching / Hoarding | [01_caching.md](01_caching.md) | `garage_bone_pack` (#5) | live + new prep stage |
| 02 | Vocalization Repertoire | [02_vocalization.md](02_vocalization.md) | `squeak_steal` (#7), `yard_passerby` (#3), `attila_whine` (#8) | live, distributed |
| 03 | Anxiety / Stress Signaling | [03_anxiety.md](03_anxiety.md) | `garage_okie_anxious` (#6), auto-flashback (#13) | live |
| 04 | Resource Guarding & Theft | [04_resource_guarding.md](04_resource_guarding.md) | `squeak_steal` (#7) | live, hardcoded |
| 05 | Coprophagia | [05_coprophagia.md](05_coprophagia.md) | `bed_face_lick` (#11) | live |
| 06 | Belly Exposure / Solicitation | [06_belly_exposure.md](06_belly_exposure.md) | `tex_belly_roll` (#4) | live |
| 07 | Pre-Walk Anticipation | [07_prewalk_anticipation.md](07_prewalk_anticipation.md) | `attila_whine` (#8) | live |
| 08 | Bark Contagion | [08_bark_contagion.md](08_bark_contagion.md) | `yard_passerby` (#3) | live |
| 09 | Senior Cognition (CDS) | [09_senior_cognition.md](09_senior_cognition.md) | **NEW** `crockett_sundowning` | shipping this round |
| 10 | Tool Use / Problem-Solving | [10_tool_use.md](10_tool_use.md) | `garage_bone_pack` + new `prepare_blanket` action | shipping this round |
| 11 | Sleep Location | [11_sleep_location.md](11_sleep_location.md) | `nighttime_choice` (#15) | live |
| 12 | Solicitation Behaviors | [12_solicitation.md](12_solicitation.md) | `squeak_steal`, `attila_bed_petting` | live |
| 13 | Co-regulation / Bonding | [13_co_regulation.md](13_co_regulation.md) | distributed across comfort branches + `four_dog_bed_session` | live |
| 14 | Play Preference (incl. Dalamar echo) | [14_play_preference.md](14_play_preference.md) | `tennis_ball` (#10), `dog_park` (#9) | live |
| 15 | Breed-Typical Traits | [15_breed_traits.md](15_breed_traits.md) | cross-cuts every encounter | distributed, no system |

## Conventions used in every doc

- **Research / canon / live encounter** — what already exists.
- **What this is** — short science recap.
- **Implementation now** — current code state.
- **Levers the player has** — what the user can do.
- **Levers the player does NOT have (yet)** — honest gap list.
- **Future expansion** — bounded next-step proposals (not aspiration).
- **Voice rules** — Ted's voice, specifically as it applies to this mechanic.

## How to use these docs

When a mechanic needs revision:
1. Read its doc.
2. Edit the live encounter (in `code/noir.html`).
3. Update the doc to reflect the change.
4. If the change is substantial, note it in `MEMORY_LOCAL.md`.

When proposing a NEW mechanic that doesn't fit any of these 15:
1. Check `behaviorresearch.md` to see if the science is captured.
2. If not, add it there first (with citation-grade caution).
3. Then create a new mechanics doc following the convention above.
4. Then build the encounter.

Don't build mechanics for behaviors not in `canon/`. If we want a herding scene for the Aussies, ask Ted whether they actually herd before writing it. (See `behaviorresearch.md` "Behaviors NOT yet observed.")

# B017 — Okie — Garage avoidance when others are inside

**Status:** CANON. Observed 2026-04-25.

## Real-world

Okie won't go into the garage if Attila and Tex have gone in first. He stops at the door. Doesn't whine, doesn't push — just won't enter. If you carry him in or block them from going in first, he's fine.

This is interesting because the garage is normally his preferred space — bone bank (B005), anxiety refuge (B006), sleep location (B008). The avoidance is *social*, not spatial.

## Trigger

Okie at garage threshold + Attila and/or Tex already inside + no human present in garage.

## Proposals

- **TEXT:** Encounter at the garage door. Okie is here, the others are already inside. Player options: let him decide / carry him in / call others out first / leave him outside.
- **ULTIMA5:** Tile flag `garage_occupants > 0` modifies Okie's pathing — he routes around if possible, halts at threshold if not.
- **SIMS:** Social-pressure stat. Okie's `enter_garage` autonomy gates on `(other_dogs_inside == 0) OR (human_inside)`. Override via player command.
- **NES:** Sprite halt animation at the door tile. Player must press B to coax him through.

## Design notes

- Reads as either: (a) deference to a small in-group already formed, (b) avoidance of being the third wheel, or (c) avoidance of being cornered in a small space with two dogs he wants to play with but knows he shouldn't pester (cross-ref B018).
- The "carry him in" option is real — Ted has done this. Worth modeling.
- Cross-ref B019 (Tex retreat): the others' presence in the garage may be *because* of Okie; Okie's avoidance may be reading that he's the cause.

## Cross-references

- `B005` — bone bank. Okie's main reason to go in.
- `B006` — anxiety refuge. Same.
- `B018` — roughhouse solicitation. The cause of B019, indirectly the cause of B017.
- `B019` — Tex's garage retreat from Okie.

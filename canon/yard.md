# DogSim — Yard Geography

The real yard, captured as structured data for the game map. Updates here are authoritative; they override anything sketched in BEHAVIORS.md.

---

## Real-world layout (Ted's description)

- **Patio strip** — a few feet wide, wraps the house and extends around to the driveway so trash cans can be wheeled through.
- **Lawn** — roughly 10 ft deep from patio edge, grass.
- **Slope** — yard goes **downhill** from the lawn.
- **Lower strip** — 4 ft of dirt / gravel / ground cover.
- **Trees** — plum tree + one other fruit tree (species TBD).
- **Bushes** — surviving blackberry bush (the blueberry bush is the dead one from B001).
- **Potted plants** — several, close to the house. Not individually modeled in v1.
- **Driveway** — exits via the patio strip.
- **Garage** — attached; critical interior location (see B005/B006 — Okie's bone bank + anxiety refuge).

---

## Proposed v1 tile map (draft — confirm with Ted)

A 6×5 grid feels right for terminal rendering. Okie starts on the patio.

```
    0    1    2    3    4    5
0  [H]  [H]  [H]  [H]  [H]  [G]       H = house wall (impassable)
1  [P]  [P]  [P]  [P]  [P]  [D]       G = garage door
2  [.]  [.]  [.]  [.]  [.]  [D]       P = patio (paved)
3  [,]  [B]  [,]  [T]  [,]  [D]       D = driveway (paved, slopes to gate)
4  [~]  [~]  [x]  [~]  [F]  [F]       . = lawn (grass)
                                      , = dirt/gravel strip (downhill)
                                      ~ = groundcover
                                      T = plum tree
                                      F = fruit tree (TBD species)
                                      B = blackberry bush (survives pee? TBD)
                                      x = DEAD BLUEBERRY BUSH (memorial tile)
```

**Design notes:**
- The memorial dead-bush tile `x` is a real-world fact and gives the yard a "place where Okie sinned" permanent feature. Good flavor.
- Driveway column acts as the exit to the outside world (parked for v2+).
- Slope is cosmetic in TEXT mode but becomes a movement modifier in ULTIMA5 and a sprite-scroll cue in NES.

---

## Tile-type enum (v1)

| Symbol | Name | Walkable? | Pee effect | Notes |
|--------|------|-----------|------------|-------|
| H | house_wall | no | — | blocks movement |
| G | garage_door | yes (enter) | — | gateway to interior (see INTERIORS.md later) |
| P | patio | yes | inert | paved, pee has no target |
| D | driveway | yes | inert | paved, slopes |
| . | lawn | yes | yellows grass | healthy → yellow → dead (3 states) |
| , | dirt | yes | inert | already bare |
| ~ | groundcover | yes | damages slowly | |
| T | plum_tree | no | tree unaffected; dog marks trunk | pee is "allowed" — flavor only |
| F | fruit_tree | no | same as plum | |
| B | blackberry_bush | no | survives ONE pee, dies on second | canon: it survived once already |
| x | dead_bush | no | — | memorial, immutable |

---

## Interior locations (parked — not v1)

- **Garage** — Okie's bone bank, kiddie-pool dog beds (B005), anxiety refuge (B006).
- Living room, kitchen, etc. — parked until multi-dog v2+.

---

## Questions still open

1. Which direction does the slope actually run — away from the house (down toward the fruit trees) or parallel to it? I've drawn "away from house = downhill." Correct?
2. Is there a fence at the lower edge of the yard, or does it blend into something else?
3. The "other fruit tree" — any idea what it is? (Apple, pear, fig, peach?)
4. Where is the gate / exit to the street — end of driveway or somewhere else?

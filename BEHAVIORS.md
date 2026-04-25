# BEHAVIORS — Systems Taxonomy

> **Note:** This file catalogs the *systems* needed to simulate dog behavior. For the **list of specific observed behaviors** in Ted's four dogs (B001–B016+), see `canon/behaviors/INDEX.md`. This file is the engineering substrate; that file is the content.

**Status:** SPECULATIVE. Living design document. Revised as observations accumulate.

---

## 0. Framing

Every behavior in `canon/behaviors/` is the *tip of a system*. Behind "Okie stashes bones" is a whole scaffold: hoarding drives, inventory semantics, path-finding to a safe-space, the bone-supply event, the kiddie-pool container. You can't simulate dogs without these substrates.

This file enumerates the **twelve systems** DOGSGAME needs (or will need) to simulate the behaviors already observed. For each system:

- **Purpose** — what it's for.
- **State it owns** — the variables that live in this system.
- **Events it emits / subscribes to** — its place in the event bus.
- **Behaviors fed by it** — which `B###` entries rely on it.
- **Realization per era** — how it surfaces in TEXT / ULTIMA5 / SIMS / NES.
- **Minimum viable form** — the skeleton needed for v1, if any.

---

## 1. NEEDS SYSTEM

**Purpose:** Model a dog's basic somatic needs that build over time and drive actions.

**State owned:** `bladder`, `bowel`, `hunger`, `thirst`, `sleep`, `energy` — one integer/float per dog, bounded.

**Events emitted:** `need_threshold_crossed` (e.g., `bladder > 7`). **Subscribes to:** tick, sleep, feeding, location changes.

**Behaviors fed:** B001 (pee), B008 (indoor accident), B015 (dog park recovers energy).

**Per era:**
- **TEXT:** Stats shown on status line; thresholds surface as ambient text (`[Okie is eyeing the door.]`).
- **ULTIMA5:** Visible stat bars in sidebar.
- **SIMS:** Core loop — pie-chart or meter cluster. The genre-native expression.
- **NES:** 4-bit meters drawn with `▮▮▯▯` cells on HUD.

**MVP for v1:** optional. Probably skip in v1 — make pee a free action for the scope-frozen bush-kill prototype. Introduce needs in v2 so there's time pressure.

---

## 2. DRIVES SYSTEM

**Purpose:** Model emotional/social drives that are less somatic than needs — the "why" behind non-survival actions.

**State owned:** `anxiety`, `attention_need`, `hoarding_drive`, `territoriality`, `social_need`, `mischief`, `petting_need`, `reactivity`, `curiosity`.

**Events emitted:** `drive_threshold_crossed`. **Subscribes to:** world events (human_leaves, passerby, loud_noise), other dogs' events.

**Behaviors fed:** B003 (attention_need), B004 (mischief), B005 (hoarding), B006 (anxiety), B010 (anticipation), B013 (petting_need), B009 (reactivity).

**Per era:**
- **TEXT:** Surface through the narrator — "Okie is pacing." Not as a meter.
- **ULTIMA5:** Visible bars (anxiety, happiness) in sidebar.
- **SIMS:** Full inspector. Maxis-native.
- **NES:** Limited to 1–2 visible drives (probably anxiety). Rest are internal state influencing animation.

**MVP for v1:** none. Drives are the v2 axis that transforms v1's state machine into a dynamic sim.

---

## 3. TRAITS SYSTEM

**Purpose:** Per-dog immutable or slow-changing dispositional attributes. Configure which systems apply and how strongly.

**State owned:** per-dog trait set — e.g., Okie has `{anxious, coprophagic, hoarder, territorial, face_licker}`, Attila has `{mild_mannered, obedient, communicator, bed_permitted}`.

**Events emitted:** none (read-only). **Subscribes to:** none.

**Behaviors fed:** every B###. Traits are the "config file" for each dog.

**Per era:** invisible in all eras; surfaces through filtered event behavior.

**MVP for v1:** yes. Even v1 needs Okie's `{coprophagic=true, territorial=true}` so the pee-on-bush rule fires correctly.

**Canonical source:** `canon/dogs.md`.

---

## 4. LOCATION / SPATIAL SYSTEM

**Purpose:** Represent *where* dogs and humans are — tiles, rooms, areas. Enable adjacency, line-of-sight, pathing.

**State owned:** `pos: (x, y)` per agent; `tile_map: Grid[TileKind]`; `rooms: dict[room_id, bounds]`.

**Events emitted:** `agent_moved`, `agent_entered_room`. **Subscribes to:** action results.

**Behaviors fed:** B001 (bush tile), B005 (garage → kiddie-pool bed), B006 (seek garage), B009 (in garage), B015 (dog park map).

**Per era:**
- **TEXT:** ASCII grid + compass-direction movement.
- **ULTIMA5:** Tile-sprite overworld.
- **SIMS:** Isometric or top-down room-based.
- **NES:** Tile map with scroll.

**MVP for v1:** yes. The grid from `canon/yard.md`.

---

## 5. SCHEDULES / TIME SYSTEM

**Purpose:** Time-of-day, day-of-week, season. NPC (dog) schedules. Periodic world events.

**State owned:** `tick`, `hour`, `day`, `season`; per-agent schedule tables.

**Events emitted:** `hour_rolled`, `day_rolled`, `scheduled_event_fires`. **Subscribes to:** tick.

**Behaviors fed:** B008 (night-time), B009 (traffic density by hour), B011 (monthly cadence).

**Per era:**
- **TEXT:** "It is 2:14 am."
- **ULTIMA5:** Day/night visual cycle (palette shift).
- **SIMS:** Calendar UI + clock.
- **NES:** Clock HUD (digit tiles).

**MVP for v1:** no, unless bush-death arc requires day-turn progression.

---

## 6. VOCALIZATIONS SYSTEM

**Purpose:** Dogs have a per-context vocal repertoire. Bark, whine, silence, growl, howl. Not a single "make sound" action.

**State owned:** per-dog vocal-repertoire table (which vocalizations they can produce) + current-mood-to-vocalization mapping.

**Events emitted:** `vocalization_fired(actor, kind, volume, context)`. **Subscribes to:** drive thresholds, external triggers.

**Behaviors fed:** B003 (squeak-as-signal), B009 (bark chain), B010 (whine), plus all future growls, howls, etc.

**Per era:**
- **TEXT:** Spelled-out vocalization text + formatting (ALLCAPS = bark, italic = whine).
- **ULTIMA5:** Speech balloons with `♪` / `♫` / `!` / `~` glyphs by kind.
- **SIMS:** Layered audio + thought-bubble icon.
- **NES:** APU multi-channel — pulse for bark, triangle for whine, noise for growl. A full system, not ad-hoc SFX.

**MVP for v1:** no (v1 is silent).

---

## 7. SOCIAL / INTER-AGENT SYSTEM

**Purpose:** Dogs interact with each other and with humans. Includes broadcast signals, imitation, dominance, co-operation, theft, bond strength.

**State owned:** per-pair relationship matrix (bond, dominance); global broadcast bus.

**Events emitted:** `broadcast(signal, radius, source)`, `bond_changed(a, b, delta)`. **Subscribes to:** vocalization events, proximity, actions.

**Behaviors fed:** B003 → B004 (broadcast/subscribe), B009 (bark amplification), B011 (group dynamics), B013 (pet-demand negotiation).

**Per era:**
- **TEXT:** Narrator articulates: "Tex barks back. They amplify."
- **ULTIMA5:** NPC reaction-sprites and scripted dialogue.
- **SIMS:** Genre-native: visible social interactions with animations and result deltas.
- **NES:** Animation changes + maybe a 4-color bond heart icon.

**MVP for v1:** no (v1 is single-dog).

---

## 8. OBJECTS / INVENTORY SYSTEM

**Purpose:** World contains things dogs and humans can carry, use, hide, break, or steal. Toys, bones, leashes, food, dog waste.

**State owned:** `object_id → {kind, owner_id, location, state}`. Inventory per-agent.

**Events emitted:** `object_moved`, `object_destroyed`, `owner_changed`. **Subscribes to:** actions.

**Behaviors fed:** B003 (squeaky toy), B004 (toy theft), B005 (bone bank), B010 (leash), B012 (yard waste), B014 (tennis ball).

**Per era:**
- **TEXT:** `> take bone`, `> stash bone under blanket`, inventory list.
- **ULTIMA5:** Keyword-driven (`get`, `use`, `give`).
- **SIMS:** Drag-drop or click-activate objects.
- **NES:** HUD item icons.

**MVP for v1:** yes, minimally — the blueberry bush is an "object" (a tile with state). Expand in v2 for bones and toys.

---

## 9. COMMANDS / OBEDIENCE SYSTEM

**Purpose:** Humans issue commands (sit, down, come, stay) and dogs may or may not comply. Compliance is probabilistic and trait-modulated.

**State owned:** per-dog compliance-rate table (per command); optional escalation-counter for repeated commands.

**Events emitted:** `command_issued`, `command_obeyed`, `command_ignored`, `command_escalated`. **Subscribes to:** player actions.

**Behaviors fed:** B013 (Attila ignoring `down`), future sit/stay/come/leave-it behaviors.

**Per era:**
- **TEXT:** `> tell attila down`. Response varies.
- **ULTIMA5:** Dialogue option — probabilistic success.
- **SIMS:** Autonomy override mechanic.
- **NES:** B-button contextual verb.

**MVP for v1:** no.

---

## 10. ENVIRONMENT / WORLD-EVENTS SYSTEM

**Purpose:** Things outside the household: traffic, weather, wildlife, people passing, seasons, storms.

**State owned:** passerby-spawn queue; weather state; noise events.

**Events emitted:** `passerby_spawned`, `weather_changed`, `noise_event`. **Subscribes to:** schedule.

**Behaviors fed:** B009 (15th Ave traffic), B016 (neighborhood drama), future storm-anxiety events.

**Per era:**
- **TEXT:** Ambient italicized line: `[A car rumbles up 15th Ave.]`
- **ULTIMA5:** Scheduled NPC traffic on map edge.
- **SIMS:** Poisson-timer world events.
- **NES:** Scrolling-sprite car at top of screen.

**MVP for v1:** no. But designing it early makes v2 traffic cheap.

---

## 11. HOUSEHOLD RULES SYSTEM

**Purpose:** Capture meta-rules the humans enforce — who may go on the bed, who is fed what, sleep-location assignments.

**State owned:** rule set (permission flags per dog per zone); active/exception states.

**Events emitted:** `rule_violated`, `rule_exception_granted`. **Subscribes to:** agent actions + human commands.

**Behaviors fed:** B011 (bed-session exception), B012 (bed access = Attila-only default), B008 (sleep-location assignment).

**Per era:**
- **TEXT:** Narrated rules ("The Aussies do not belong on the bed. Usually.").
- **ULTIMA5:** Visible rule list in status screen.
- **SIMS:** Rule UI with toggles per dog per zone.
- **NES:** Small icon on HUD ("bed: attila-only").

**MVP for v1:** no.

**Canonical source:** `canon/dogs.md` §"Household rules" + future `canon/household.md` once 3+ rules.

---

## 12. NARRATIVE / MEMORY SYSTEM

**Purpose:** Historical incidents, flashbacks, case arcs, season-to-season storytelling. What the game *remembers* about previous sessions.

**State owned:** `incident_log`, `active_cases`, `unlocked_flashbacks`, `historical_dog_references`.

**Events emitted:** `incident_logged`, `case_opened`, `case_closed`, `flashback_triggered`. **Subscribes to:** threshold crossings + player actions.

**Behaviors fed:** B007 (flashback), B014 (Dalamar reference), B016 (gate incident as first case), future case arcs.

**Per era:**
- **TEXT:** Italicized flashback lines. Case ledger visible in a journal command.
- **ULTIMA5:** Cutscene overlays. Journal menu.
- **SIMS:** Family-history panel.
- **NES:** Dedicated password/save screens showing cases solved.

**MVP for v1:** no.

---

## System dependency graph

```
  TRAITS ────────────────┐
      │                   │
      v                   v
  NEEDS ──► DRIVES ──► COMMANDS
      │       │           │
      │       │           │
      v       v           v
  LOCATION ◄─SCHEDULES ◄─ENVIRONMENT
      │       │
      v       v
  OBJECTS ◄──SOCIAL ──► VOCALIZATIONS
                │
                v
          HOUSEHOLD-RULES
                │
                v
            NARRATIVE
```

Systems closer to the root (TRAITS, LOCATION) are more foundational. Systems closer to the leaves (NARRATIVE, VOCALIZATIONS) layer on top.

---

## V1 minimum-viable system stack

For the frozen v1 scope (Okie + yard + bush-kill), the required systems are:

1. **TRAITS** (Okie's coprophagia/territoriality flags, even if cosmetic)
2. **LOCATION** (the yard grid)
3. **OBJECTS** (the bush as a stateful tile)
4. Maybe a minimal **NARRATIVE** (to narrate the bush's death in three stages)

Everything else is v2+ design surface, **prepared for** by the architecture but **not built**.

---

## How this file relates to `canon/behaviors/`

- `canon/behaviors/B###_*.md` = *observations* ("Okie banks bones") + era-specific mechanic *proposals*.
- `BEHAVIORS.md` (this file) = the *systems* those observations all share.

Cross-reference direction: behaviors cite systems ("this needs the Drives system"), and systems cite behaviors ("fed by B001, B005, B006").

If a new B### is logged that doesn't fit any system here, add a new system. If it fits cleanly, just cross-reference and move on.

---

## Revision log

- **2026-04-24 (rev 1):** Initial drafting from B001–B016. Twelve systems identified. V1 stack pinned to TRAITS/LOCATION/OBJECTS/minimal-NARRATIVE. Revision cadence: after every ~5 new behaviors, re-audit whether the system taxonomy still holds.

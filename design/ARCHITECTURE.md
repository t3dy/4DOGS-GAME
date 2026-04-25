# DogSim — Engine Architecture

Goal: a **text-first** game that treats the text renderer as one of several pluggable views on a single, stable game-state kernel. This way the Ultima-V, Sims, and NES ports are renderer swaps, not rewrites.

---

## Design principles

1. **Kernel first.** Game state is a pure data structure. Nothing in the kernel knows about rendering, input, or narrative flavor. Deterministic, testable, replayable.
2. **Events, not polling.** Every state change emits an `Event`. Renderers and narrative subscribe; nothing reaches into kernel internals.
3. **Renderer is a plugin.** The text UI is a renderer. The NES cart, someday, is another renderer over the same kernel.
4. **Narrative is a separate layer.** The "ripping yarn" voice lives in a `NarrativeDirector` that reads events and emits flavor. Replace it to change tone without touching the kernel.
5. **Tick is the heartbeat.** One `Tick` = one in-game minute (or equivalent). Player input produces actions that schedule kernel effects at the next tick. World events (traffic, time-of-day, bowel timers) also tick.
6. **No hidden randomness in the kernel.** The RNG is explicit and seedable. Replay logs = reproducible sessions.

---

## Layers

```
┌───────────────────────────────────────────────────────────┐
│ Renderers (TEXT, ULTIMA5, SIMS, NES)                      │  ← swap freely
├───────────────────────────────────────────────────────────┤
│ NarrativeDirector                                          │  ← flavor voice
│   subscribes to Events, emits narration lines              │
├───────────────────────────────────────────────────────────┤
│ Event Bus                                                  │  ← observable stream
├───────────────────────────────────────────────────────────┤
│ Kernel                                                     │  ← pure, deterministic
│   - World (grid, tiles, objects)                           │
│   - Agents (dogs, humans, traffic)                         │
│   - BehaviorRegistry (B001..B010)                          │
│   - Scheduler (tick loop)                                  │
│   - RNG (seeded)                                           │
├───────────────────────────────────────────────────────────┤
│ Input adapters (stdin parser; later GUI controls)         │
└───────────────────────────────────────────────────────────┘
```

---

## Kernel: core types

```python
# pseudocode, Python stdlib target

@dataclass
class Tile:
    kind: TileKind            # lawn, patio, bush_blueberry, ...
    state: dict               # {"health": 3}, {"squeak_count": 2}, ...
    contents: list[ObjectId]  # items or dogs on the tile

@dataclass
class Agent:
    id: AgentId
    name: str                 # "Okie"
    kind: AgentKind           # DOG, HUMAN, TRAFFIC
    pos: Tuple[int, int]
    stats: dict               # {"anxiety": 4, "bladder": 7, ...}
    traits: set[str]          # {"hoarder", "belly_roller"}
    inventory: list[ObjectId]

@dataclass
class World:
    grid: Grid
    agents: dict[AgentId, Agent]
    objects: dict[ObjectId, GameObject]
    tick: int
    rng: Random
    scheduled_events: PriorityQueue

@dataclass
class Event:
    kind: str                 # "pee", "stash_bone", "passerby", "bark"
    actor: Optional[AgentId]
    target: Optional[...]
    data: dict
    tick: int
```

**Key rule:** mutations to `World` happen only through `apply_action(world, action) -> list[Event]`. Nothing else writes.

---

## Behavior registry

Each `B###` entry in `BEHAVIORS.md` corresponds to one registered behavior. A behavior is a tuple:

```python
Behavior(
    id="B001",
    name="okie_pee_bush_kill",
    preconditions=lambda w, a: a.kind == DOG and tile_at(w, a.pos).kind == BUSH_BLUEBERRY,
    effect=lambda w, a: [
        ModifyTile(a.pos, health=-1),
        EmitEvent("pee", actor=a.id, target=a.pos),
    ],
    cooldown_ticks=3,
)
```

The registry is a flat list. The **scheduler** calls `behavior.effect` either in response to a player action (`PlayerAction.Pee`) or from agent autonomy (SIMS-mode).

New behaviors = new registry entries. **Never modify the kernel to add a behavior.**

---

## Event bus

A ring-buffer of the last N events + a pub/sub for live subscribers. Two subscribers ship in v1:

1. **NarrativeDirector** — takes `Event` → emits `NarrationLine` (flavor text).
2. **Renderer** — takes `Event` + `World snapshot` → updates display.

Adding a fourth subscriber (e.g., a `LogRecorder` for replay) is a one-liner.

---

## Game loop

```
while not game_over(world):
    action = input_adapter.get_player_action(world)   # blocks on stdin (text mode)
    events = kernel.apply_action(world, action)
    for e in events: event_bus.publish(e)

    world.tick += 1
    autonomous_events = kernel.run_autonomy_tick(world)  # traffic, bowel timers, dog autonomy
    for e in autonomous_events: event_bus.publish(e)

    renderer.draw(world)
```

Two subtleties:

- **Time-of-day** advances inside `run_autonomy_tick`. Day/night drives B006 anxiety, B008 sleep, B009 traffic density.
- **Player "end turn" vs. real-time.** Text version is turn-based. Sims/NES modes can re-use the same kernel with a real-time wrapper that calls `apply_action` on a 100ms timer — the kernel doesn't care.

---

## NarrativeDirector: the "ripping yarn" layer

Flavor text is NOT hardcoded in kernel effects. Example:

- Kernel emits: `Event(kind="pee", actor=okie, target=(3,1))`
- NarrativeDirector receives event, checks `world.tiles[3,1]` → `bush_blueberry, health=2`
- Looks up flavor bank for `pee + bush_blueberry + health_2` → emits:
  > *"Okie circles once, then assumes the posture of quiet conviction. The blueberry bush, which has seen this before, steels itself."*

Flavor banks are just dicts of templates, swappable per era (terse for v1, ornate later). This is how the same event yields *Zork*-voice in TEXT mode and *Sims*-neutral-narrator in SIMS mode.

---

## External world: scheduled events

For B009 traffic:

```python
world.schedule(
    event=Event(kind="passerby", data={"type": "car", "direction": "uphill"}),
    at_tick=world.tick + rng.expovariate(TRAFFIC_RATE_BY_HOUR[current_hour(world)]),
)
```

When the scheduled tick arrives, autonomy tick pops and dispatches. Dogs in the garage subscribe to `passerby` in their own reaction logic (B009's bark chain).

---

## Renderer protocol

```python
class Renderer(Protocol):
    def draw(self, world: World) -> None: ...
    def show_narration(self, line: NarrationLine) -> None: ...
    def prompt_input(self, world: World) -> PlayerAction: ...
```

- **TextRenderer** (v1): ASCII grid, status line, printed narration, `input()` parser.
- **Ultima5Renderer** (later): pygame / web canvas, tile sprites, 16-color palette, keyword dialogue.
- **SimsRenderer** (later): isometric-ish tilemap, autonomous agents, pie-menu interactions.
- **NesRenderer** (later): actual NES PPU emulation target, or approximation via pixel-perfect 2D canvas.

The kernel never sees these. A renderer swap is a CLI flag: `python dogsim.py --renderer=text`.

---

## Narrative game loop stability guarantees

1. **Determinism.** Given the same RNG seed and action log, the kernel produces the same events.
2. **Replayability.** Action logs replay to the same world state. Debuggable. Testable.
3. **Save/load.** World state is serializable (dataclasses → JSON). No save format change when we add behaviors — just new fields.
4. **No narration in critical paths.** The kernel can run headless (no renderer, no narrator) for tests and automated playthroughs.
5. **Event schemas are append-only.** New event kinds don't break old subscribers. Deprecation > breaking changes.

---

## v1 minimum viable slice

The Layer 3 spec from HiroPlantagenet, now concrete:

- `okie.py` (single file for v1 — refactor to package only if needed)
- Kernel types: `World`, `Tile`, `Agent`, `Event`
- One behavior: `B001` (pee-on-bush)
- One renderer: `TextRenderer`
- One narrative flavor bank: terse Zork-voice
- Commands: `move N/S/E/W`, `pee`, `look`, `quit`
- Game over: blueberry bush dies OR player quits

Everything else in this document is **architecturally prepared for** but **not built in v1**. The file structure is the only future-proofing that matters:

```
dogsim/
  kernel/
    world.py     # Tile, Agent, World, event dataclasses
    actions.py   # apply_action + behaviors registered here
    scheduler.py # run_autonomy_tick
  events.py      # EventBus
  narrative.py   # NarrativeDirector + flavor banks
  renderers/
    text.py      # v1 renderer
  main.py        # game loop
```

That's the whole architecture. We can build B001 in this skeleton and every later behavior slots into `actions.py` without touching the other files.

# DogSim — Scene Mockups Across Four Eras

Three scenes rendered four ways each. These are **static mockups** (text / ASCII art) — no interactive code yet. Read them as concept art for what the engine described in `ARCHITECTURE.md` should produce when a given renderer is plugged in.

**Rendering eras:**
- **TEXT** — Infocom / Zork terminal
- **ULTIMA5** — 16-color tile RPG with keyword dialogue and status HUD
- **SIMS** — isometric-ish autonomous-agent sim with pie menus and thought bubbles
- **NES** — 8-bit NES puzzle/sim (pixel constraints, APU SFX, tight HUD)

**Scenes covered:**
1. The Yard at dawn (idle establishing shot)
2. Okie pees on the blueberry bush (v1 climax — B001)
3. Attila's pre-walk whine (B010)
4. Garage bark chain as a car passes (B009) — bonus, shows external world

Plus: a title screen + main menu mockup for each era, and a save/load/transition example.

---

## SCENE 1 — The Yard at Dawn

Establishing shot. Okie on patio, blueberry bush present, plum tree looming, morning.

### TEXT

```
─────────────────────────────────────────────────────────
                    THE BACK YARD
─────────────────────────────────────────────────────────

A thin Sultan morning leaks across the patio. The air
smells of wet cedar and the faintest trace of something
blueberry-adjacent. The lawn slopes away from the house
toward a stand of fruit trees. A blueberry bush sits in
the middle distance, aggressively alive.

Okie is here, on the patio, blinking.

   ╔════════════════════════════╗
   ║ H H H H H H G ║       H: house
   ║ P P P P P[O]D ║       P: patio
   ║ . . . . . . D ║       .: lawn
   ║ , B , T , , D ║       B: blueberry
   ║ ~ ~ x ~ F F F ║       T: plum
   ╚════════════════════════════╝    F: fruit tree
                                     x: (memorial)
 Okie  |  bladder 3/10  |  07:12 am  |  cloudy

> _
```

### ULTIMA5

```
┌──────────────── DOGSIM ────────────────┐  ┌── STATS ──┐
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │ OKIE      │
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓│  │ HP  ▰▰▰▰▰ │
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  │ BLD ▰▰▰░░ │
│░░░░░░░░░░░░░░░🐕░░░░░░░░░░░░░░░░░░░░░░│  │ ANX ▰▰░░░ │
│,,,,,,,♣,,,,,,Ψ,,,,,,,,,,,,,,,,,,,,,,,,│  │ BOND      │
│,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,│  │ TEX  ▰▰▰░░│
│ϟϟϟ†ϟϟϟϟ†ϟϟϟϟΨΨΨΨΨΨΨΨΨΨΨΨΨΨΨΨΨΨΨ        │  │ ATT  ▰░░░░│
│                                        │  │ CRO  ▰▰░░░│
│ DAWN   Sultan Falls  Spring  Day 1    │  │           │
└────────────────────────────────────────┘  │ ACTIONS:  │
                                             │ (M)ove    │
 "The yard smells of morning and sleep."     │ (L)ook    │
                                             │ (P)ee     │
 Press key-command for action:               │ (T)alk    │
  (M)ove  (L)ook  (P)ee  (T)alk  (B)ark       │ (B)ark   │
                                             │ (S)tats   │
                                             └───────────┘
```
Legend: `█` house, `░` patio, `,` lawn, `Ψ` ground-cover, `♣` blueberry bush, `†` fruit tree, `🐕` Okie.

### SIMS

```
┌─────────────────────────────────────────────────────────┐
│       TIME 07:12  ☀ Cloudy  Day 1  Sultan, WA          │
├─────────────────────────────────────────────────────────┤
│               .   .   .   .   .                         │
│              ╱ ╲ ╱ ╲ ╱ ╲ ╱ ╲ ╱ ╲                        │
│             ╱ H ╳ H ╳ H ╳ H ╳ G ╲    [house]            │
│            ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳   [garage]            │
│           ╱ ╳ 🐕 ╳ ▚ ╳ ▚ ╳ ▚ ╳ ▚ ╳ ╲  ┌─────────┐        │
│          ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ ╳ │ OKIE    │        │
│           ╲ ╳ ≋ ╳ ♣ ╳ ≋ ╳ † ╳ ≋ ╳ ╱  │ 🍖🍖🍖  │        │
│            ╲ ╳ ≋ ╳ ✖ ╳ † ╳ † ╳ ╱   │ Mood: ▇░░│        │
│             `-----------------`    │ Need:    │        │
│                                    │ 💧 Bladder│        │
│   💭 Okie: "bladder... moderate."   │    ▇▇▇▁▁│        │
│                                    └─────────┘        │
│   [⌒] Interact    [►] Fast-forward    [⏸] Pause        │
└─────────────────────────────────────────────────────────┘
```
Pie menu appears when you click Okie: `[ Pee | Bark | Belly-roll | Go to garage | Play ]`.

### NES

```
  ┌──────────────────────────────────┐
  │ SCORE  00000    TIME 07:12        │
  ├──────────────────────────────────┤
  │ █ █ █ █ █ █ █ █ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ │  pattern table: house + garage
  │ █ █ █ █ █ █ █ █ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ │
  │ · · · · · · · · · · · · · · · · │  patio (pavement tile, palette 0)
  │ · · · · 🐶 · · · · · · · · · · · │  sprite 0 = Okie
  │ , , , , , , , , , , , , , , , , │  lawn tile (palette 1)
  │ , , , ♣ , , , , 🌳 , , , , , , ,│  blueberry (bg), plum (bg)
  │ , , , , , , , , , , , , , , , , │
  │ ~ ~ ~ x ~ ~ ~ ~ 🌳 ~ ~ ~ ~ ~ ~ ~│  groundcover + memorial tile
  │ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═│  fence
  ├──────────────────────────────────┤
  │ OKIE  BLD ▮▮▮▯▯▯▯▯▯▯   DAY  1   │
  └──────────────────────────────────┘
        A: pee      B: bark
      ←↑→↓: move    START: menu
```

---

## SCENE 2 — Okie Pees on the Blueberry Bush (B001)

The v1 climax. Okie steps onto the bush tile and the player presses `pee`.

### TEXT

```
> move south

You step onto the dirt strip. The blueberry bush is
just there, smug and thriving.

> pee on bush

Okie circles once, then assumes the posture of quiet
conviction.

                . · . · .
              .  ╱|   |╲  .
              ·  ╲|   |╱  ·
                · · · · ·

The blueberry bush, which has seen this before,
steels itself.

             [blueberry bush: YELLOWING]

> look bush

The leaves have gone the color of regret. You give it
three more days. Maybe two.

 Okie  |  bladder 1/10  |  07:14 am  |  game-over pending

> _
```

### ULTIMA5

```
                                               ┌── STATS ──┐
      ,,,,,,,♣,,,,,,Ψ,,,,,,,                   │ OKIE      │
      ,,,,,,,🐕,,,,,,,,,,,,,,                  │ HP  ▰▰▰▰▰ │
                                               │ BLD ▰░░░░ │
  ┌──────────────── OKIE ─────────────────────┐│ ANX ▰▰▰░░ │
  │ Thou performest an unseemly marking.      ││           │
  │                                           ││ BUSH      │
  │ The bush regardeth thee balefully.        ││ hp ░░░░░  │
  │                                           ││ status:   │
  │ "Y" to confirm, "N" to withdraw with      ││ WILTING   │
  │  dignity.                                 │└───────────┘
  └───────────────────────────────────────────┘
```
Keyword verbs are Ultima-V standard: `pray`, `pull`, `look`, `talk`, `ignite`, `jimmy` — "pee" gets treated as `yank` or added as custom verb `yield`. We can make the Ultima flavor register specifically 16th-century for comic effect.

### SIMS

```
   ╳ ╳ ♣ ╳ ╳     ← blueberry bush (hovered: "Blueberry Bush — Alive")
   ╳ 🐕 ╳ ╳ ╳    ← Okie
   ╳ ╳ ╳ ╳ ╳

 ▶ Click-drag Okie onto bush tile → context pie:

        ┌─────────────────┐
        │   PEE  BARK     │
        │                 │
        │  SNIFF  DIG      │
        │                 │
        │    (cancel)     │
        └─────────────────┘

 After PEE:
        ┌─── Okie ───┐
        │ 💭 "mine." │
        └───────────┘
        ┌─── Bush ───┐
        │ 💭 "..."    │
        │ hp: 2 → 1   │
        └────────────┘

 Achievement Unlocked: "Territorial Gesture"  +5 pts
```

### NES

```
     frame 1 (approach):        frame 2 (pee):        frame 3 (after):
     ┌───────────────┐         ┌───────────────┐      ┌───────────────┐
     │ ,,,,,,,,,,,, │         │ ,,,,,,,,,,,, │      │ ,,,,,,,,,,,, │
     │ ,,,♣,,,,,,,, │    →    │ ,,,♣,,,,,,,, │ →   │ ,,,✖,,,,,,,, │
     │ ,,,🐶,,,,,,, │         │ ,,💧🐶,,,,,, │      │ ,,,🐶,,,,,,, │
     │ ,,,,,,,,,,,, │         │ ,,,,,,,,,,,, │      │ ,,,,,,,,,,,, │
     └───────────────┘         └───────────────┘      └───────────────┘
     MSG: "APPROACH"           MSG: (no text)         MSG: "BUSH: YIKES"
     APU: ——                   APU: ch1 short         APU: ch3 sad
                                    trill (pee SFX)         descending blip
```
The `✖` tile is a single palette-swap from `♣`, so the "death" is a 1-byte attribute write, which is both canonical NES and beautiful.

---

## SCENE 3 — Attila's Pre-Walk Whine (B010)

Player grabs the leash. Attila is a 100-lb bernese/golden mountain cross whining in falsetto.

### TEXT

```
> get leash

You lift the leash from the hook. Attila, who has been
asleep in the garage, is suddenly not asleep.

    He whines.

    He is ONE HUNDRED POUNDS and he whines like a
    kettle coming to the boil.

> clip leash to attila

The whine rises in pitch.

> open garage door

The garage door rises with its usual mechanical
dignity. The whine does not stop. The whine
has become a matter of principle.

Attila has pulled the slack out of the leash. He
is no longer, strictly, whining — he is
broadcasting.

> walk

─────────────  OFF TO 15TH AVE  ─────────────

[... walk sequence to be designed ...]
```

### ULTIMA5

```
┌─── ATTILA ───────────────────────────┐
│ ATT   ♪~~~~~~~~~~~~~~~~              │  ← musical-note speech balloon
│ HP ▰▰▰▰▰▰▰▰                           │  ← big dog, big HP bar
│ HYPE ▰▰▰▰▰▰▰▰▰▰ (MAX)                │
│                                      │
│ ATTILA's eyes are bright.             │
│ His voice, however, is small.         │
│                                      │
│ "I WILL WAIT," quoth ATTILA.          │
│ "BUT NOT SILENTLY."                    │
└──────────────────────────────────────┘

 Commands: (W)alk  (S)it  (T)reat  (P)atience
```

### SIMS

```
   ┌── ATTILA ──┐      Actions queued:
   │ 💭 🚶🚶🚶! │      1. 🦴 Chew squeaky (cancelled)
   │ Mood: ▇▇▇▇│      2. 🚶 Walk (in progress)
   │ 🗯 "♪~~~" │      
   └───────────┘      Whine-meter: ▇▇▇▇▇▇▇▇▇▇
                      
   ┌── PLAYER ──┐      Hidden stat:
   │ ⏳ Getting │      BARK-TO-WHINE-RATIO
   │   leash... │      Current: 0.02 (all whine)
   └────────────┘
```

### NES

```
  ┌──────────────────────────────────┐
  │ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪ ♪│  ← ♪ tiles cycle
  │ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █│
  │ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █│  ← garage interior
  │ █ █ █ █ █ 🐕 █ █ █ 🚪🚪🚪🚪 █ █│  ← Attila sprite, door rising
  │ █ █ █ █ █ ⬛ █ █ █ 🚪🚪🚪🚪 █ █│
  │ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _│
  │ ⟪WHINE⟫ — HIT B TO OPEN DOOR  │
  └──────────────────────────────────┘
  APU: ch3 triangle wave, slow up-pitch
       ch4 noise pops on every ♪ tile
```

---

## SCENE 4 — Garage Bark Chain (B009) — bonus

Car passes on 15th Ave. Okie and Tex are in the garage. Chaos.

### TEXT

```
[A low diesel rumble rolls up 15th Ave.]
[Somebody's pickup, probably. Outbound.]

Okie's head lifts.

Tex's head lifts.

They look at each other. A contract is signed.

    Okie: "WOOF."
    Tex:  "WOOF WOOF."
    Okie: "WOOF WOOF WOOF!"
    Tex:  "(BIGGER) WOOF!"

The truck is gone. They continue for six more
seconds, on principle. You count.

─────────  it's 2:14 am.  ─────────
```

### NES

```
  Street (top strip, 3 tiles tall):
  ──────────────────────────────────
  ─ ─ ─ ─ 🚗 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ← car sprite scrolling L→R
  ──────────────────────────────────
  ┌── GARAGE INTERIOR ──┐
  │ 🐕          🐕      │             ← Okie + Tex
  │ 🗯WOOF  🗯WOOF      │
  └─────────────────────┘
  APU: ch1 pulse bark (okie), ch2 bass bark (tex),
       ch4 noise engine (car), layered.
  REACTION: +anxiety(okie), -sleep(neighbor NPC ☹)
```

---

## Title Screens & Menus

### TEXT title

```
        ╔════════════════════════════════════════╗
        ║                                        ║
        ║              D O G S I M               ║
        ║                                        ║
        ║     A yard.  A blueberry bush.         ║
        ║     A dog named Okie.                  ║
        ║                                        ║
        ║     [N]ew   [L]oad   [Q]uit            ║
        ║                                        ║
        ╚════════════════════════════════════════╝
```

### NES title

```
  ┌──────────────────────────────────┐
  │           ▰▰▰ DOGSIM ▰▰▰         │
  │                                  │
  │       🐕 🐕 🐕 🐕                │
  │                                  │
  │       ▶ NEW GAME                 │
  │         LOAD                     │
  │         OPTIONS                  │
  │                                  │
  │       © 2026 HAND COMPUTING      │
  └──────────────────────────────────┘
```

### Ultima5 load menu

```
┌──────────────── LOAD ──────────────┐
│ Scroll 1  Day 3    Okie at patio   │
│ Scroll 2  Day 7    Bush wilting    │
│ Scroll 3  Day 9    Bush DECEASED   │
│                                     │
│ Press 1-3 to load or ESC to return. │
└─────────────────────────────────────┘
```

### Sims transition screen

```
  ┌──────────────────────────────────────┐
  │  ◯ Loading...                         │
  │  ░░░░░░░░░▓▓▓▓▓▓▓▓▓░░░░░░░░░░░      │
  │                                      │
  │  TIP: Okie can bank rawhide bones    │
  │       in the garage. Let him         │
  │       express himself.                │
  └──────────────────────────────────────┘
```

---

## Save/load model (era-agnostic)

Because the kernel is pure state, save files are shared across eras:

```json
{
  "seed": 2026042401,
  "tick": 482,
  "world": { "agents": { ... }, "tiles": { ... } },
  "action_log": [ ["move", "S"], ["pee"], ["move", "N"], ... ]
}
```

A TEXT save loads in NES mode and plays identically. That's the architecture earning its keep.

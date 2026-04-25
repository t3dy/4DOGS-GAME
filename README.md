# 4DOGS-GAME

A noir text-adventure prototype based on four real dogs in Sultan, WA.

> **▶ Play it: [t3dy.github.io/4DOGS-GAME](https://t3dy.github.io/4DOGS-GAME/)**
>
> *(Pages may take a minute or two to publish on the first push.)*

---

## What this is

A browser-playable encounter game. 17 numbered scenes, six cases, scene-warp,
persistent state in `localStorage`. No install — open the site, pick a case,
make decisions for Okie.

The game is built from real-world dog behaviors. Every encounter
(`canon/behaviors/B###_*.md`) corresponds to something one of these dogs
actually does. The blueberry bush is dead in real life; Okie really did kill it.

## The dogs

| Dog | Breed | Signature |
|-----|-------|-----------|
| **Okie** | Australian shepherd | Anxious, territorial, bone-banker, killed the bush |
| **Tex** | Australian shepherd, larger | Belly-roll specialist; bark-chain partner with Okie |
| **Attila** | Black Bernese / golden mountain cross, ~100 lb | Mild-mannered, communicates via squeaky pig + pre-walk whine |
| **Crockett** | Senior, 11 | Toy-thief, arthritic, occasionally cognitively elsewhere |

## How to play

1. Open the [live site](https://t3dy.github.io/4DOGS-GAME/).
2. Pick a case from the sidebar — *FULL DAY* runs all 17 scenes in day-cycle order.
3. Each encounter offers 2-5 numbered choices. Pick one. The world updates.
4. Use the **WARP TO SCENE** input to jump directly to any scene (1-18).
5. State persists between reloads — your bush stays dead.

## Two front doors

- **[`code/noir.html`](code/noir.html)** — the encounter game (Deja Vu / Police Quest aesthetic)
- **[`code/showcase.html`](code/showcase.html)** — multi-era mockup showing the same dogs in TEXT / ULTIMA V / SIMS / NES rendering styles

## Repository layout

```
.
├── index.html                — Pages landing
├── README.md                 — this file
├── CLAUDE.md                 — agent ground rules
├── ROUTING.md                — file-routing index
├── CEAUDIT.md                — context-engineering audit
├── BEHAVIORS.md              — systems taxonomy
├── MEMORY_LOCAL.md           — project cross-session notes
│
├── code/
│   ├── noir.html             — main browser game
│   ├── showcase.html         — four-era mockup
│   ├── dogsim.py             — terminal Python version (companion)
│   └── README.md             — code-folder docs
│
├── canon/                    — facts (immutable without discussion)
│   ├── dogs.md               — the four-dog roster
│   ├── yard.md               — geography + tile map
│   └── behaviors/            — one B### file per observed behavior
│       ├── INDEX.md
│       ├── B001_okie_pee_bush.md
│       └── ... (B002 through B016)
│
└── design/                   — speculation (subject to revision)
    ├── ARCHITECTURE.md       — engine design (kernel / event bus / renderers)
    ├── MOCKUPS.md            — scene mockups across four rendering eras
    ├── NOIR_LENS.md          — Deja Vu / Police Quest aesthetic proposal
    ├── K9_PATROL_ROGUELIKE.md — sibling-game stub (FTL-inspired)
    ├── SHAMANIC_VOYAGES.md   — stub, parked
    ├── PARKING.md            — parked ideas
    └── DIALOGUES/            — narrative-designer / historian / programmer transcripts
```

## Behavior index (in-game)

The game's encounters cover these behaviors from `canon/behaviors/`:

| # | Encounter | Behavior |
|---|-----------|----------|
| 1 | Morning Briefing | (session opening) |
| 2 | The Blueberry | B001 — territorial pee, bush-kill |
| 3 | Traffic / Bark Chain | B009 — Okie + Tex barking at 15th Ave traffic |
| 4 | Belly Roll | B002 — Tex offers the belly |
| 5 | The Bone Bank | B005 — Okie's Old Roy hoarding ritual |
| 6 | Anxiety | B006 — Okie pacing at the garage door |
| 7 | Squeak & Steal | B003 + B004 — Attila's pig signal, Crockett's theft |
| 8 | Pre-Walk Whine | B010 — Attila's leash-whine paradox |
| 9 | The Dog Park | B015 — open-space zoomies |
| 10 | The Tennis Ball | B014 — failed experiment, Dalamar echo |
| 11 | Face-Lick | B012 — coprophagia / yard-scoop self-honesty |
| 12 | Bed-Petting | B013 — Attila's paw-request + command resistance |
| 13 | Flashback | B007 — the bed-destruction years |
| 14 | Four-Dog Bed Session | B011 — the rare warm one |
| 15 | Where Does Okie Sleep | B008 — nighttime sleep-location decision |
| 16 | The Gate Was Open | B016 — escape incident, $200 settlement |
| 17 | Recovery | B016b — picking up the pieces |
| 18 | Debrief | (session closing, score tally) |

## Status

**Phase:** Exploration. v1 is not yet committed; the browser game is a playable
prototype that demonstrates the encounter system + noir voice. See
[`design/PARKING.md`](design/PARKING.md) for what's intentionally not built yet.

## Stack

- Vanilla HTML / CSS / JS — single-file, no build, no dependencies
- State in `localStorage`
- Companion Python prototype in `code/dogsim.py` (stdlib only)

## License

Personal project. All dog likenesses used with the dogs' tacit consent
(they signed nothing).

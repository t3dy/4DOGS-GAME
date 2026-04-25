# DOGSGAME — code/

Two prototypes live here. Both are no-install: Python stdlib for the game,
plain HTML/CSS/JS for the showcase.

---

## `dogsim.py` — the terminal game

Encounter-based. Numbered menus (2-5 options per turn). Noir voice per
`design/NOIR_LENS.md`. Single file, Python 3.7+, stdlib only.

### Run interactively

```
python dogsim.py                # plays the default case (CASE 1: A MORNING IN SULTAN)
python dogsim.py --case bush    # one-encounter run: just kill the bush
python dogsim.py --case garage  # bone-bank + anxiety case
python dogsim.py --case bed     # face-lick decision case
```

### Run scripted (no stdin — useful for CI / verification)

```
python dogsim.py --test
```

Runs three scripts demonstrating: bush-kill ending, bone-bank session,
face-lick branches.

### Architecture (single-file but layered)

The file mirrors `design/ARCHITECTURE.md`:

| Layer | Where |
|-------|-------|
| Kernel — `World` dataclass | top of file |
| Encounters — `Encounter`, `Option`, `Resolution` | middle |
| Encounter library — `enc_*()` functions | middle |
| Catalog + Cases — `CATALOG`, `CASES` dicts | middle |
| Renderer — `TextRenderer` | bottom |
| Sequencer — `Sequencer` (drives the queue) | bottom |
| Game loop — `play()` | bottom |

**To add a new encounter:**
1. Write `enc_my_thing()` returning an `Encounter`.
2. Register it in `CATALOG`.
3. Either reference its id from another encounter's `Resolution.follow_ups`,
   or seed it directly from a `Case`.

**To add a new case:**
Add an entry to `CASES`. A case is just a title + opening narration +
seed encounter list.

### Encounters currently implemented

| Encounter id | Behavior canon | Options |
|--------------|---------------|---------|
| `morning_briefing` | (session opening) | 3-4 |
| `yard_bush` | B001 | 2-4 (depends on bush state) |
| `yard_passerby` | B009 | 3 |
| `garage_bone_pack` | B005 | 3-4 |
| `garage_okie_anxious` | B006 | 3-4 |
| `bed_face_lick` | B012 | 4 |
| `debrief` | (session closing) | 2 |

---

## `showcase.html` — four-era visual mockup

Open in any browser. No build, no dependencies. Click through the four era
tabs to play the same game-world with four different rendering aesthetics:

- **TEXT (Deja Vu)** — verb-grid noir. Click verbs in any order. Pee three
  times to kill the bush.
- **ULTIMA V** — 16-color tile grid with HUD. Walk Okie to the bush, press P.
- **SIMS** — isometric-ish bedroom. Click Okie for the action pie.
- **NES** — pixel CRT styling. A = leash, B = door. Whine cycle visible.

The four scenes don't share state — each is an independent mockup of
how a single moment from the canon would surface in that aesthetic.

---

## What's NOT here yet

- A unified kernel that the four eras all share. Currently `dogsim.py` is
  the kernel-bearing prototype and `showcase.html` is presentation-only.
- Save/load. The session is in-memory.
- Sound. Even the NES scene is silent in the browser.
- Multiple dogs. Okie only. Per v1 scope freeze.
- Interior household map beyond the garage stub.

These are intentional gaps — see `design/PARKING.md` for the full list.

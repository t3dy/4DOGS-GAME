# B014 — All four dogs — Tennis ball disappointment / "Dalamar echo"

**Status:** CANON (real-world fact). Mechanically a **failed-experiment / negative-space** behavior.

## Real-world

Ted cannot get any of the four dogs interested in playing with a tennis ball. They may chase briefly, but none of them care. This is notable because Ted's **previous dog, Dalamar, a border collie** (from Ted's teens/20s), was obsessed with the ball — a foundational dog-memory that colors Ted's expectations.

Ted proposed simulating this as "disappointing experiments": the player tries a thing, the dogs refuse to engage, the player is reminded of a dog who would have loved it.

## Trigger

Player command `throw tennis ball` (or equivalent). Dogs evaluate + reject.

## Proposals

- **TEXT:** `> throw tennis ball` → `[The ball arcs into the lawn. Okie blinks at you. Tex blinks at the ball. Attila is busy. Crockett is asleep.]` followed by an optional flashback-style italicized line: `[*In another yard, a border collie named Dalamar would have been on it before it landed.*]` Triggering the flashback is probabilistic / rate-limited.
- **ULTIMA5:** Tennis ball is an inventory item with an `interest_rating` per dog (all 4 near zero). Throw action spawns ball as a world object; dogs run the "investigate" routine and return zero-interest. Player gets a text box with neutral observation.
- **SIMS:** Toy preferences are dog-level attribute arrays. Ball-interest = 0 for all four. Throwing a ball produces no autonomy response. Game's inspector surfaces the *absence* of interest — "not everything is a mechanic; some toys just don't work."
- **NES:** Throw-ball as an unlockable action. Ball sprite travels in an arc. Dogs' reaction frames remain in idle state. A text box: "THEY AREN'T INTERESTED." Optional: after N failed attempts, unlock a Dalamar cutscene — sepia-tinted screen, border collie sprite, one line of text, returns.

## Design notes

- **Negative-space mechanic.** Games usually reward experimentation with a response; this one rewards it with *recognition of loss*. Risky, beautiful.
- **Dalamar as historical character.** Not in the playable roster but present in flavor banks. Maybe `canon/historical_dogs.md` eventually.
- The disappointment is Ted's, not the dogs'. Narration should make this clear — the Aussies aren't *wrong* to be uninterested; they're just themselves.
- Good test of the narrative layer: can the engine express "nothing happened, and that *meant* something"?

## Cross-references

- Contrast with `B015` (dog park zoomies) — proves the dogs can be engaged; the issue is *what* engages them (environment > object).
- `B002` (Tex belly-roll) — Tex is interactable; just not via tennis ball.

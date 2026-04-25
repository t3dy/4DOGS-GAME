# DOGSGAME — Project Memory (local, cross-session)

Project-level notes that should persist between sessions but don't belong in user-profile memory. Update as decisions are made.

---

## Canonical decisions (stable)

- **Name:** DOGSGAME (renamed from DogSim on 2026-04-24).
- **Phase:** EXPLORATION. No code yet. Toy-first, not game-first.
- **v1 scope frozen at:** Okie in yard, B001 bush-kill as single rule, TEXT renderer, Python stdlib.
- **Layout:** three-tier (canon / design / data + code) per `CEAUDIT.md`.
- **Status convention:** directory dictates status (`canon/` = CANON, `design/` = SPECULATIVE).
- **Pig vs cow squeaky toys:** cosmetic skins on a single `squeaky_toy` object in v1. Distinct in v2+ if useful.
- **Dead blueberry bush:** canonical real-world fact. Appears in `canon/yard.md` as memorial tile `x`.
- **Setting:** Sultan, WA, 15th Ave off Basin Hill Rd. Canonical location flavor.

## Open questions (awaiting Ted)

From `DIALOGUE_01_first_meeting.md` Round 5:

1. Feel-bad-about-the-bush vs. laugh-at-the-bush (tone commitment)?
2. Dogs as characters with interiority, or creatures with behaviors?
3. Yard as *place* (Animal Crossing) or *level* (Boulder Dash)?
4. Era-switching visible or invisible?
5. Is Sultan, WA a setting or a subject?
6. Minimum session length: 5 min / 30 min / hours?
7. Ship target: terminal / browser / both?

Still from earlier scoping:

8. Yard slope: does it run away from the house, or parallel?
9. Is there a fence at the lower yard edge?
10. Species of the second fruit tree?
11. Gate / exit location — end of driveway?
12. Okie's other signature move besides peeing?
13. Bladder as a resource meter, or pee as free action?

## Conventions adopted (avoid re-debating)

- Behaviors are numbered `B###` and live one-per-file under `canon/behaviors/`.
- Era proposals always include all four: TEXT / ULTIMA5 / SIMS / NES. Even if brief; the NES constraint is especially diagnostic.
- Kernel is renderer-agnostic. Flavor text lives in narrative-director layer, never in kernel effects.
- Real-world dog names and breeds are canonical. Do not rename or breed-swap without Ted's consent.
- Every behavior file cross-references related behaviors (e.g., B003 ↔ B004, B005 ↔ B006).

## Session log (brief)

- **2026-04-24 session 1:** Scope freeze, HiroPlantagenet decomposition, behaviors B001–B004 logged (Okie pee, Tex belly-roll, Attila squeaky, Crockett theft). Mockups + architecture drafted. Four-era lens established.
- **2026-04-24 session 2 (same day, continued):** Added B005–B010 (bone banker, anxiety, bed destruction flashback, nighttime indoor-shit, bark chain, pre-walk whine). Ted requested architecture doc → ARCHITECTURE.md written. Mockups requested → MOCKUPS.md written. Pivoted to exploration mode — no game design committed. Team-dialogue format introduced in DIALOGUE_01. CEAUDIT.md written. Project renamed DogSim → DOGSGAME. Three-tier layout migrated.
- **2026-04-24 session 2 (continuing):** Added B011 (bed-session with all four dogs, rare) and B012 (Okie afternoon bed-joining + face-lick avoidance / poop-eating flag).
- **2026-04-24 session 2 (Phase A migration + behavior burst):** Executed Phase A migration to three-tier layout (canon/ design/ data/ code/). Wrote CLAUDE.md, ROUTING.md, MEMORY_LOCAL.md. Split behaviors into per-file canon entries. Added B013 (Attila bed-petting + command resistance), B014 (tennis ball disappointment + Dalamar echo), B015 (dog park zoomies), B016 (gate-open escape incident with Pregnant Woman / Cop Husband / $200 shakedown). Created `design/NOIR_LENS.md` (Deja Vu / Police Quest / K-9 aesthetic proposal) and `design/SHAMANIC_VOYAGES.md` (stub, parked per Ted). Created `design/K9_PATROL_ROGUELIKE.md` (FTL-inspired companion game, parked). Wrote new root `BEHAVIORS.md` as systems taxonomy (12 systems). Deleted original flat BEHAVIORS.md. Updated Attila's canon/dogs.md entry: "most mild-mannered / attentive / obedient."

## Tonal frontrunners (as of 2026-04-24)

- **Noir lens** (`design/NOIR_LENS.md`) has become the frontrunner aesthetic. Ted introduced Deja Vu + Police Quest + K-9 fantasy in one sequence of messages, suggesting unified direction.
- B016 (gate incident) reads as pre-written noir case script.
- Shamanic voyages + K9 Patrol are OUT-of-DOGSGAME (parked as future concepts).

## Decisions still open
- Noir lens as v1 primary? Or one of multiple rendering lenses?
- Case-based session structure or ambient open-ended?
- Dalamar enters flavor banks as historical foil?

## Items to promote to canon next

- Poop-eating trait (coprophagia) — should be a dog-level trait on Okie, Tex, Crockett (NOT Attila per Ted's implication). Put in `canon/dogs.md`. Affects face-lick interactions + any future "kiss" verbs.
- Bed-permission rule: Aussies discouraged from the bed; exception is rare TV/movie group-session. This is a *household rule*, not a behavior — probably belongs in a new `canon/household.md` file when we have 3+ household rules.

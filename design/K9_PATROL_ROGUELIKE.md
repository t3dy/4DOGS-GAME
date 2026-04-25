# K9_PATROL_ROGUELIKE — Speculative companion game

**Status:** SPECULATIVE. Companion / sibling project to DOGSGAME. Separate concept, overlapping assets and aesthetic.

## The pitch

Ted has a running comedy routine in which his four dogs are a police K-9 unit. This proposal:

**An FTL-inspired roguelike where you patrol a map in a police car with your K-9 unit and a human partner.**

- **Ship → Police Car.** Hull/shields/fuel become chassis-condition / siren-status / gas.
- **Crew → K-9 unit + human partner.** The four dogs + one human (Ted as a rookie cop, or a fictional protagonist).
- **Sector map → Patrol beat.** Branching map of zones in the city/town. Pick your route.
- **Encounters → Calls.** Domestic disturbance, loose dog, traffic stop, suspicious package, missing cat. Noir-comedy tone.
- **NPCs → Animal control, desk sergeant, suspects, citizens, that one annoying detective.**
- **No aliens.** There is no invading force pushing you across the map. Patrol is open-ended, session-paced.

## Why this is distinct from DOGSGAME

- **Genre:** DOGSGAME is a life-sim / text adventure. K9_PATROL is a roguelike.
- **Scope:** DOGSGAME is one yard. K9_PATROL is a town of nodes.
- **Player identity:** DOGSGAME player is Ted at home. K9_PATROL player is Ted (or a proxy) on the job.
- **Stakes:** DOGSGAME has no external jeopardy. K9_PATROL has encounters that can injure dogs / cost the car / end a shift.

## Why this shares assets with DOGSGAME

- Same dogs, same personalities. Okie as anxious operational liability. Tex as steady big-brother. Attila as mild-mannered best-boy (fits a working-dog role really well). Crockett as grizzled veteran brought back for one last case.
- Same voice (noir-comedic per `NOIR_LENS.md`).
- Same kernel *in theory* — if the DOGSGAME kernel has traits / drives / commands systems, K9_PATROL can reuse them.

## Core loop (sketch)

1. Shift briefing. Desk sergeant assigns territory.
2. Pick a patrol route (branching node map).
3. Drive to node → encounter fires.
4. Encounter resolution (dialogue, K-9 command, physical action). Success / partial / failure.
5. Resource state updates (gas, dog stamina, car damage, paperwork).
6. Continue to next node OR return to station for resupply.
7. Shift ends at a fixed tick budget. Score = cases resolved, civilian goodwill, paperwork backlog.

## Sample encounters

- **Stray dog chase.** Send Okie (too anxious, fails). Send Tex (catches). Send Attila (negotiates). Send Crockett (gives sage advice).
- **Noise complaint.** Knock, take statements, decide to write up or let slide.
- **Lost child at park.** Deploy Attila's mild-mannered vibe. Success.
- **Traffic stop.** Generic. Occasional twist: the suspect's dog is in the car and a whole new subplot fires.
- **Animal control backup call.** Work with the animal control NPC (recurring). He's grumpy and knows all four of your dogs by name.
- **Interdepartmental politics.** The detective (from DOGSGAME's NOIR_LENS — maybe the same cop who shook Ted down in B016) resurfaces.

## Aesthetic

Matches `NOIR_LENS.md`. Deja Vu noir + Police Quest procedural = comedy baseline. ASCII / pixel / mixed. Heavy radio-code flavor. Every encounter has a 10-code reference.

## What would be hard

- FTL's core loop has a push (pursuer, sector-advance pressure). Without a pursuer, patrol can feel directionless. Needs a replacement pressure: **time (shift budget)** + **paperwork compounding** + **chief's mood**.
- Encounter variety must scale. FTL has ~200 encounters. K9_PATROL would need similar volume — a content-authoring problem, not a code problem.
- Balancing the dogs. Okie as operational liability is funny but the player must still have reasons to use him. Maybe Okie has one or two surprising strengths (scenting, say — his territoriality maps to tracking).

## Parking rationale

This is a separate game. DOGSGAME v1 is nowhere near shipped. Building K9_PATROL would fork the effort.

**Parked in `design/PARKING.md` as P015.** Revisit only if:
1. DOGSGAME v1 ships, AND
2. The noir lens is adopted, AND
3. Ted still has energy for the K-9 fantasy after shipping.

If those three conditions are met, this doc becomes the seed for a new project directory (`C:\Dev\K9PATROL\`), not a subfolder of DOGSGAME.

## Minimum exploration step (if Ted wants to poke at this)

- Write one encounter in prose-script form, full noir voice, with dog commands as menu options. ~80 lines of markdown. Proves the tone + loop works without any code commitment.

---

## Notes log

**2026-04-24 — Initial stub.** Ted proposed the concept: FTL-inspired roguelike, police car + K-9 unit + partner, patrol a map, no aliens. Parked pending DOGSGAME progress.

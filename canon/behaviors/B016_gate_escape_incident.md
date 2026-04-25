# B016 — Okie + Tex — Gate-open escape incident / neighborhood sequel

**Status:** CANON. Single historical incident, promoted to canon because it's too good not to model.

## Real-world

Ted left the yard gate open once. Tex and Okie escaped into the suburban neighborhood. Ted ran around searching. Outcomes:
- One neighbor had **caught Tex** (Tex was recoverable).
- A **pregnant woman holding her baby** claimed her dog had been **bitten by Okie**.
- Her husband, a **police officer**, demanded **$200 cash** for a vet bill. Ted paid.

This is a real-world event with the structure of a Police Quest or Deja Vu chapter: the player's mistake, the chase, the confrontation, the shakedown.

## Trigger

Gate state = `open` + dog proximity to gate + curiosity drive crosses threshold. Escape can be spontaneous or player-caused (forgetting the gate).

## Proposals

- **TEXT:** First turn: `[You notice the yard is quiet. Too quiet. The gate swings in the breeze.]` Player must `> search neighborhood`. Multi-area map (suburb) unlocked temporarily. Escalating turn-based stakes: find Tex, find Okie, confront neighbor. Final menu: `[P]ay / [A]rgue / [L]eave`. Arguing may escalate; paying resolves but hits a `cash` stat (if tracked).
- **ULTIMA5:** Open-world segment with the suburb as a procedural or fixed street map. Dogs are fugitive sprites. Player must catch both. Neighbor NPCs have schedules; encountering the Pregnant Woman NPC triggers the scripted incident with dialogue tree. Gold stat drops by 200 if paid.
- **SIMS:** Gate `open` is a world flag. Dogs' autonomy re-evaluates: if `outside_available`, they go. Outside the yard, their state moves onto the neighborhood map. Neighbor NPCs are simulated households. The incident is an *emergent* Sims encounter that the game dramatizes when it happens.
- **NES:** **This behavior is made for Deja Vu / Police Quest style.** See `design/NOIR_LENS.md`. Chapter-structured: Chapter 1 — "The Gate." Chapter 2 — "Suburban Manhunt." Chapter 3 — "The Shakedown." Monochrome + red noir palette. Heavy prose in text boxes. Menu verbs: EXAMINE / SPEAK / PAY / FLEE / CALL OKIE.

## Design notes

- **First story arc candidate.** Most behaviors are ambient; this is a *case*. It has beginning, middle, end.
- Tonal fit with noir aesthetic is almost perfect. The Pregnant Woman / Cop Husband scene is practically a Deja Vu script.
- **Real-money-extortion comedy.** The $200 is a canonical sum; don't round it. It's the joke.
- Design question: is this a **tutorial-sequel** (played early to teach story-mode mechanics) or a **rare incident** (fires once per playthrough under specific conditions)?
- Open: if the player *argues*, does the cop escalate? Do you get arrested? This is where noir absurdity can expand.

## Cross-references

- `design/NOIR_LENS.md` (to be written) — aesthetic proposal around Deja Vu / Police Quest / K-9 fantasy.
- `B009` (bark chain) — shows dogs already engage with the world beyond the yard (via traffic). This escape is the world engaging with them back.

## Canonical characters (for this incident)

- **Ted** — protagonist. Runs around the neighborhood. Eventually pays.
- **Tex** — escaped, caught by a neighbor. Recovered without incident.
- **Okie** — escaped, allegedly bit a neighbor's dog. Recovered after payment.
- **The Neighbor Who Caught Tex** — generic helpful NPC. Name unknown.
- **The Pregnant Woman** — held a baby, claimed Okie bit her dog. Key witness / victim.
- **The Cop Husband** — extracted $200. Possibly exploits pregnancy for leverage. Morally ambiguous.
- **The Bitten Dog (offscreen)** — alleged victim. Never directly seen.

Treat these as characters with names-TBD. Ted can fill in details later.

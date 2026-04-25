# DogSim — Team Dialogue 01: First Meeting

Ted has hired a small, opinionated team to help him figure out what DogSim is.

---

## Cast

- **Miriam Ashe** — Narrative Designer. Tabletop RPG background, published some interactive fiction (*The Vintner's Daughter*, *Four Letters*). Obsessive about tone and character voice. Suspicious of mechanics that exist only to be "engaging."
- **Dr. Tomas Vaszary** — Game Historian. Teaches a seminar on the computer game as cultural artifact. Can tell you the difference between Wizardry III's combat grid and Ultima IV's without reaching for a reference. Loves the Maxis "toy, not game" philosophy.
- **Kai Pak** — Programmer. Ex-gameplay engineer, now freelance. Allergic to scope creep. Will ask "what does the state machine look like" three times in one meeting.

They're meeting in a small conference room with a whiteboard and too much coffee. Ted is on a laptop.

---

## Round 1 — What are we actually making?

**Ted:** I don't know yet. I have four real dogs and a yard and a lot of behaviors. I want to turn it into something. A text game. Maybe also a Sims thing. Maybe an NES cartridge. I don't have a *game* yet — I have a universe.

**Miriam:** Oh, thank god. I was afraid you were going to tell us you had a 40-page design doc.

**Kai:** *(visibly relaxing)* This is the correct starting posture. Most projects die because someone wrote the 40-page doc first.

**Tomas:** "A universe, not a game" — that's a Will Wright quote, approximately. He called *SimCity* a toy before it was a game. A toy is a thing you can poke and get interesting responses from. A game is a toy with a goal bolted on. I'd argue you don't need to pick a goal today. You need to build a **good toy**.

**Miriam:** I agree with half of that. The toy needs to have a *voice*, or it won't be interesting to poke. A silent toy is a physics engine. A toy that talks back — that's the start of something.

**Kai:** Fine, but "voice" can't be the architecture. The architecture has to be: things happen, events fire, something listens. Voice is a subscriber.

**Ted:** This is what I wanted. Keep going.

---

## Round 2 — The four-era strategy

**Tomas:** The text / Ultima / Sims / NES thing — this is not a scope problem. It's a *lens* problem. Each of those eras prioritized a different kind of player attention.

- Text (Infocom era): the parser was the interface; the *language* was the gameplay. You read.
- Ultima V: tile-based RPGs treated the world as a *schedule*. NPCs had day/night routines. You could visit Lord British in his bedchamber at 3am.
- Sims (Maxis): autonomous agents. The fun is *watching*. The player is a gardener, not a driver.
- NES (first-party Nintendo + clones): hardware constraints *were* the aesthetic. 4-color sprites, 8×8 tiles, APU, 2-button controller.

Each of these is actually asking a different question about dogs:
- Text asks: "How do I narrate dog-ness?"
- Ultima asks: "What is a dog's schedule?"
- Sims asks: "What does a dog want?"
- NES asks: "What is the minimum legible dog?"

**Miriam:** I love that framing. And it means we don't have to pick one. The *kernel* answers all four. The *renderer* picks a lens.

**Kai:** Which is exactly what the architecture doc already says, incidentally. State is state. You point a lens at it.

**Ted:** So the universe is: the yard, four dogs, their behaviors. And the question "what game is this" becomes "which of these lenses makes the dogs most alive?"

**Tomas:** Or — and I think this is more interesting — *different lenses for different scenes*. The whine-before-walk is a Sims moment. The bush-kill is an Infocom moment. The bark-chain is NES-era pure feedback loop. You could make a game that deliberately era-shifts.

**Miriam:** Oh. Oh, that's good.

**Kai:** That's also significantly more expensive.

**Miriam:** Of course it is. Everything good is.

---

## Round 3 — Spectacle vs. mechanic vs. experience

**Ted:** I want to build mechanics, interactions, experiences, *or* spectacles. I'm not sure which those even are, separately.

**Miriam:** Okay, working definitions:
- A **mechanic** is a rule the system enforces. "Peeing on a plant damages it."
- An **interaction** is what the player does to trigger a mechanic. "Press P on a plant tile."
- An **experience** is what the player *feels* as the mechanic plays out. "The creeping guilt of watching the bush yellow over three days."
- A **spectacle** is a moment the game engineers for the player to *witness*. The dogs barking at 2am. The garage door rising while Attila whines. You're not making a choice, you're watching a thing happen.

**Tomas:** Spectacle is underrated. Half of *Shadow of the Colossus* is spectacle. All of *Animal Crossing* is spectacle — "oh look the fish moved."

**Kai:** Spectacles are also the cheapest to prototype. You don't need a win condition. You need a scripted moment.

**Ted:** So if I want to explore, spectacle is the right unit of exploration?

**Miriam:** Spectacle plus one *small* mechanic. If a spectacle has no player handle, it's a cutscene. A good explorable unit is: one spectacle + one player verb that changes it.

**Kai:** Scene 2 from the mockups is an almost-perfect example. Blueberry bush exists. Bush has state. Player pees. Bush changes state. That is the entire exploration. Everything else is decoration.

**Tomas:** And it's recognizable as "a game." Will Wright would approve.

---

## Round 4 — What to explore next

**Ted:** So what do we actually build? Not commit to — just poke?

**Miriam:** I'd poke at **voice**. Write the same event — Okie pees on the bush — in five tones. Dry clinical, Infocom-poetic, Ultima-archaic, Sims-neutral, NES-minimal. See which one makes the scene sing. Voice is cheap to prototype; it's just a flavor bank.

**Tomas:** I'd poke at **scheduling**. What do the dogs do when no human is present? Does Attila carry the pig around the empty house? Does Crockett nap in the sun patch that moves across the floor? If the toy is alive when you're not playing, it's interesting.

**Kai:** I'd poke at **one mechanic in isolation**. Not "the game" — a single verb + single effect, runnable, testable. The bush-kill is fine. Or the bone-bank. Or the bark-chain. Pick one, build the minimum kernel that makes it work, see if it's fun in a terminal.

**Miriam:** The bone-bank is actually the most interesting mechanic we've talked about.

**Tomas:** Why?

**Miriam:** Because it's unmotivated. The dog *chooses* to hide bones. There's no reward. It's just what he does. That's a *character* mechanic, not a goal mechanic. Infocom would have found that beautiful.

**Kai:** It also has persistence, which means state, which means save/load has to work from day one. Good design pressure.

**Ted:** I was leaning toward the bush but now you're making me like the bone-bank.

---

## Round 5 — Ted's homework

**Miriam:** Here's what I'd ask Ted before we meet again:
1. Do you want the player to *feel bad* about the bush, or *laugh* at it? Dark tones and cute tones want different engines.
2. Are the dogs characters with interiority, or creatures with behaviors? (Different narrative commitments.)
3. Is the yard a *place* or a *level*? If place, you're making *Animal Crossing*. If level, you're making *Boulder Dash*.

**Tomas:** And I'd ask:
4. Do you want to reference the eras directly — visible era-switching, deliberate pastiche — or do you want a modern game that *uses* era-thinking invisibly?
5. Is the location (Sultan, WA, 15th Ave) a setting or a subject?

**Kai:** And from me:
6. What's the minimum session length? 5 minutes, 30 minutes, hours? This changes *everything* about persistence, pacing, and save systems.
7. Where does the game actually run? Terminal, browser, both? Ship target changes whether we reach for Python stdlib, a web stack, or something else.

**Ted:** *(typing)* ...okay.

**Miriam:** We reconvene when you've answered three of those.

**Kai:** Four.

**Miriam:** Fine, four.

**Tomas:** I brought pastries. Can we eat now?

---

*End of session.*

Next dialogue file workshops specific behaviors through the three-lens critique. See `DIALOGUE_02_mechanics_workshop.md`.

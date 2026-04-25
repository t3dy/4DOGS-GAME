# Dog Behavior Research — for DOGSGAME mechanics

**Status:** SPECULATIVE / reference. Not canon — these are general findings about dogs that we can pick from when designing new mechanics. For the four specific dogs, see `canon/dogs.md` and `canon/behaviors/`.

This file pairs **established behavior science** with **proposed mechanics** for both the text version and a hypothetical graphical version. Each entry is short on purpose. If something here turns into a real mechanic, it gets a `B###` in canon and stops being speculative.

Voice convention: when describing what Ted's dogs do, plain first-person. When summarizing science, neutral.

---

## 1. Caching / food hoarding

**Science.** Caching is well-documented across canids — wolves and coyotes cache surplus food and revisit hides. Domestic dogs retain the behavior even when fed reliably. Caching often involves *re-caching* (moving the item if disturbed) and *cache modification* (working the substrate to better conceal the item). The latter shows planning.

**In Ted's pack.** Okie is the bone banker (B005). He stashes Old Roy rawhides under the kiddie-pool blankets in the garage. As of 2026-04-25, we know he also **rearranges the blankets first** to improve the hide — that's tool use / problem-solving, not just instinct.

**TEXT mechanic.** Two-stage action: `prepare hide` (rearranges blanket, costs a tick, increases hide-quality) → `stash bone` (deposits, hide-quality determines how visible the cache is to other dogs). Inspecting a poor cache reveals it; a well-prepared cache shows only "nothing visible."

**GRAPHICAL mechanic.** Cache spot has a `quality` attribute (0-3). Each `prepare` action adds a fold-pattern to the sprite and increments quality. Other dogs' AI rolls against quality to decide whether to investigate. Visible "rumpled blanket" tile vs. "smooth blanket" tile.

---

## 2. Vocalization repertoire (per-context vocal types)

**Science.** Dogs produce structurally different vocalizations for different contexts: alert barks (short, high-pitched), territorial barks (lower, longer), play barks (atonal), whines (high, sustained), howls (long, modulated), growls (resource guarding vs. play growls — measurably different). Context-blind "make sound" is not how it works.

**In Ted's pack.** Attila's thunderous bark vs. his pre-walk whine (B010). Okie + Tex's bark-chain at traffic (B009). Attila's deliberate squeak-as-signal (B003). Crockett's occasional sleep-bark.

**TEXT mechanic.** Vocalization is not one verb. Each is its own narration template tied to context. The journal records *which kind* of sound was emitted (`bark / whine / growl / squeak`).

**GRAPHICAL mechanic.** Distinct sprite mouth-pose per vocalization + distinct audio sample. Visual indicator (♪ for whine, ! for alert bark, ?! for excited bark) above the dog's head.

---

## 3. Anxiety, stress signaling, calming signals

**Science.** Turid Rugaas catalogued ~30 "calming signals" dogs use to defuse social tension: lip-licking (without food), yawning out of context, head-turning, slow movement, sudden ground-sniffing. Anxiety symptoms include pacing, panting outside heat, shaking, hypervigilance, displacement scratching, and seeking enclosed spaces.

**In Ted's pack.** Okie's anxious garage-seeking (B006). Crockett's shaking. Tex and Okie's bark amplification (B009 — bark-chains often spike then crash anxiety in both dogs).

**TEXT mechanic.** `anxiety` stat already exists. Add micro-events that surface a calming signal between encounters when anxiety > 5: *"Okie yawned. He wasn't tired."* / *"Okie kept stopping to sniff the same patch of grass."*

**GRAPHICAL mechanic.** Sprite animations for pacing, panting, lip-licking, head-turn. A faint stress aura when anxiety crosses thresholds.

---

## 4. Resource guarding & inter-dog theft

**Science.** Resource guarding is contextual — dogs guard differently around different individuals, different items, different locations. Guarding intensity correlates with perceived value (high-value chew > kibble) and security (room with one exit > open yard). Theft attempts often happen when the owner is mid-action: it's deliberate timing, not random.

**In Ted's pack.** Crockett steals the squeaky pig from Attila (B004). Okie does NOT guard his bone bank against theft as far as we've observed — possibly because the bank is hidden, possibly because he's confident no one has noticed.

**TEXT mechanic.** Each carryable object has an `owner` field and a `guard_value` (how hard the owner contests theft). Theft attempts succeed based on (thief boldness − owner guard_value). Crockett: high boldness, low guard_value (won't fight back if his theft is contested).

**GRAPHICAL mechanic.** Visible possession tag (small icon over the holding dog). Theft animation: tail-low approach → grab → carry-away. Owner dog plays a brief reaction frame (raised eyebrows, single blink for Attila per B004).

---

## 5. Coprophagia (poop-eating)

**Science.** Coprophagia is common (~16% of dogs do it regularly), with multiple proposed causes: nutritional, behavioral (boredom, anxiety), evolutionary (clean-den hypothesis — wolves eat pup feces to keep the den clean). It rarely indicates actual deficiency in well-fed dogs. It's also extremely hard to extinguish once established.

**In Ted's pack.** Okie, Tex, Crockett are all coprophagic. Attila is not (per implication). This drives the face-lick risk mechanic (B012).

**TEXT mechanic.** Already implemented as B012's scoop-vs-honesty decision. Could expand: yard cleanliness becomes a real world variable that changes face-lick risk for every dog flagged coprophagic. Bring Attila in for face-licks; avoid the others on dirty-yard days.

**GRAPHICAL mechanic.** Visible waste sprites in the yard (count). Scoop action removes them. Each coprophagic dog has an opportunistic "patrol" autonomy when yard waste > 0.

---

## 6. Belly exposure & social signaling

**Science.** A belly-up posture is not always submission. It can be solicitation (asking for play / contact), trust display, or even a counter-tactic during play (kicking from below). Context tells the difference. Dogs that consistently solicit belly rubs from humans are typically secure-attachment dogs in the bonded relationship.

**In Ted's pack.** Tex (B002). Always solicitation in his case. Okie does not do this.

**TEXT mechanic.** Tex's `solicit_belly` autonomy fires when his social need is below threshold AND a known human is nearby. Player may rub (raises bond), step over (mild bond drop), or photograph-then-rub (combo).

**GRAPHICAL mechanic.** Belly-up sprite pose. A heart icon when rub is offered; the icon fades over a few seconds (you have to act).

---

## 7. Pre-walk anticipation behaviors

**Science.** Dogs build conditioned expectations from leash-cues, door-cues, and human routines. The behavior at the *threshold* moment (just before the walk starts) is often disproportionate to the walk itself — this is anticipatory arousal, not the walk's actual reward value.

**In Ted's pack.** Attila's pre-walk whine (B010) — the whine is loudest at the leash + door-rising moment, not during the walk.

**TEXT mechanic.** A pre-walk encounter that gates the actual walk encounter. Player can leash-and-go (whine continues briefly), wait (whine doesn't stop), or abandon. The walk encounter (if reached) is *quieter* than the pre-walk — the threshold is the loud moment.

**GRAPHICAL mechanic.** Whine intensity meter rises as leash → door sequence progresses. Once outside, it drops to zero. Sound design: whine pitch climbs slightly through the threshold sequence.

---

## 8. Bark contagion / barking chains

**Science.** Bark-contagion is documented in multi-dog households. One dog's alert bark triggers others; the chorus often outlives the trigger by 5-15 seconds. Similar to laughter contagion in humans. Volume scales non-linearly with dog count in the same space.

**In Ted's pack.** Okie + Tex in the garage (B009). The chorus continues for ~6 seconds after the truck is gone.

**TEXT mechanic.** Already implemented as B009. Could add: a `peace` stat for the household that recovers slowly after each bark-chain. High-peace days unlock different morning briefings.

**GRAPHICAL mechanic.** Visible sound waves emanating from each barking dog; overlap intensity drives a brief "neighbors annoyed" indicator in the corner.

---

## 9. Senior cognition (CDS / sundowning)

**Science.** Canine Cognitive Dysfunction Syndrome (CDS) appears in ~28% of dogs aged 11-12 and ~68% by 15-16. Symptoms: disorientation, altered sleep-wake cycles, house-soiling regression, reduced response to commands, confusion at night ("sundowning" — analogous to human dementia). Some dogs respond to enrichment, diet (SAM-e, antioxidants), or selegiline.

**In Ted's pack.** Crockett, 11, has shaking, possible cognitive decline, possible nighttime confusion.

**TEXT mechanic.** Crockett's encounter availability changes by time-of-day. Late at night, Crockett's options include "stand staring at the wall" / "wander into the wrong room" / "settle eventually." Theft attempts (B004) sometimes fail because he forgets mid-action.

**GRAPHICAL mechanic.** Crockett's pathfinding occasionally pauses, head-down, while he reorients. A shaking idle animation. At night, his sprite may stop in unexpected map locations.

---

## 10. Tool use & problem-solving

**Science.** Dogs are not typical tool-users compared to corvids or primates, but they do exhibit problem-solving: opening latches by paw, manipulating objects to retrieve treats, modifying their environment to suit a goal. Cache-modification (digging the hole deeper, kicking dirt over a stash) qualifies. Border collies in particular show extended problem-solving sequences.

**In Ted's pack.** **Okie's blanket trick (new, 2026-04-25)** — he upsets the blankets in the kiddie pool to make better hiding spots before stashing. That's a planning sequence: prepare-then-act, not just act.

**TEXT mechanic.** Two-stage actions for any prepared behavior. `prepare X` followed by `do Y(X)`. Quality of preparation modulates the success of the action. Scorable as "Okie's preparation index."

**GRAPHICAL mechanic.** Distinct animations for `prepare` (digging at blanket, pawing it up) vs. `act` (depositing the bone). Visible state on the cache spot.

---

## 11. Sleep location preference & housetraining regression

**Science.** Adult dogs strongly prefer consistent sleep locations. Some dogs have housetraining failures only at night (overnight bowel/bladder capacity exceeded, or lack of access to elimination area). Confining a known indoor-shitter to an easy-clean space is a documented and effective management strategy — not punishment.

**In Ted's pack.** Okie shits in the house at night if left inside, prefers the garage anyway (B008). The garage is also his anxiety refuge (B006) and his bone bank (B005). Three reasons converge on the same place.

**TEXT mechanic.** Already in B008. Could add: morning encounter narration changes if a different dog soiled instead (rare event). Sleep-location persistence across days when we add multi-day.

**GRAPHICAL mechanic.** Day-transition cinematic showing where each dog slept and a brief morning floor-state check. Visible mess sprites in the indoor-sleep failure case.

---

## 12. Solicitation behaviors (paw, nose, vocalization)

**Science.** Soliciting attention is a learned operant. The dog tries a behavior, the human responds, the dog repeats. Common solicitation forms: paw-on-leg, nose-poke, deliberate object-interaction (squeaking a toy where the human can hear), staring, leaning. Persistent solicitations indicate the human reinforced the behavior at some point — even unintentionally.

**In Ted's pack.** Attila pawing for more pets when Ted stops (B013). Attila working the squeaky pig as an attention signal (B003).

**TEXT mechanic.** Solicitation builds when an unmet need stays unmet. Each tick without resolution adds a `request_intensity`; at threshold, an interrupt fires (paw, nose-poke, squeak). Player can grant (resets intensity) or refuse (intensity continues to climb until the dog gives up at a high threshold).

**GRAPHICAL mechanic.** Solicitation-pose sprites. Intensity meter optional. Some solicitations are visible-and-cute (paw lift); some are audio (squeak from offscreen).

---

## 13. Bonding / co-regulation / oxytocin loop

**Science.** Mutual gaze between dogs and humans triggers oxytocin release in both — a bonding loop similar to mother-infant attachment. Co-sleeping, co-resting, and synchronized breathing are documented in well-bonded pairs. Dogs in proximity to a calm human often regulate their own arousal downward (and the reverse: an anxious human spikes a sensitive dog).

**In Ted's pack.** The four-dog bed session (B011). Okie pressing against Ted's leg when comforted (B006). The whole "bring Okie too" branch in B010 — Okie's anxiety drops when Tex/Attila are with him, not because of Ted alone.

**TEXT mechanic.** Co-regulation: when two named characters share a tile / scene for N ticks with no stress event, both characters drift toward the calmer one's anxiety value. The four-dog bed session can drop everyone's anxiety simultaneously.

**GRAPHICAL mechanic.** Proximity-bond effect — a faint shared-glow when two bonded characters share a space. Persistent bond meter between any two characters.

---

## 14. Play preferences & individual differences

**Science.** Toy preferences are individual. Many dogs are uninterested in fetch despite the cultural assumption. Border collies and retrievers are over-represented in fetch-loving populations because of breed selection. A dog uninterested in a tennis ball is not broken; the toy doesn't match the dog. Environment dramatically changes engagement: a dog uninterested in objects at home may engage with novelty in a new location.

**In Ted's pack.** No one cares about the tennis ball (B014). Ted's previous border collie Dalamar was obsessed. All four dogs run around at the dog park (B015) — environment matters.

**TEXT mechanic.** Already in B014/B015. Could expand: individual toy-preference table per dog (Attila: pink pig YES, tennis ball NO). Try-and-fail experiments with different toys give different flavor lines.

**GRAPHICAL mechanic.** Toy inventory with per-dog interest icons (heart / shrug / no). Throwing an unloved toy yields a clear visual non-response.

---

## 15. Breed-typical behaviors

**Science.** Breeds carry tendencies, not destinies. Aussies and other herding breeds (border collies, heelers) often herd household members, show high stimulation needs, and develop anxiety when under-exercised. Bernese mountain dogs and golden mountain crosses are typically slow-paced, gentle, lean-into-people. Smaller dogs and seniors run hotter on territoriality. Individual variation within a breed exceeds between-breed averages — useful as a starting bias, not a script.

**In Ted's pack.**
- **Okie + Tex (Aussies):** territorial pee (B001), bark-chains (B009), high anxiety baseline. We have not yet logged herding behavior — open question whether either herds the household.
- **Attila (Bernese cross):** mild-mannered, leans on people, deliberate communicator. Matches breed expectations.
- **Crockett (breed TBD, senior):** the breed-typical signals are dominated by age effects.

**TEXT mechanic.** Each dog has a `breed_traits` list that biases probabilistic behavior choices. Aussies more likely to instigate bark-chains. Attila more likely to lean / press against humans. Doesn't gate behavior; just weights it.

**GRAPHICAL mechanic.** Breed-distinct sprites. Idle animations differ — Aussies pace; Bernese-types lie down with head on paws.

---

## Behaviors NOT yet observed but suggested by the science

These are behaviors common in dogs that we haven't logged for Ted's specific pack. Worth asking about; could become future B### entries:

- **Herding behavior in the Aussies.** Do they round up the other dogs? Cut off humans at doorways?
- **Lip-licking / yawning as calming signals.** Have any of the dogs been seen doing context-displaced yawns? (Stress indicator.)
- **Play-bow as social invitation.** Front-end-down, back-end-up. Universal play signal.
- **Tail-language nuances.** Position, speed, direction (asymmetric tail-wags carry valence — right-bias = positive, left-bias = negative).
- **Resource-guarding the kiddie pool itself** (vs. just the bones in it).
- **Pre-storm anxiety / barometric pressure sensitivity.** Common, especially in anxious dogs.
- **Social referencing.** Looking at the human's face when uncertain about a novel object.
- **Door-scratching / latch-pawing as escape attempts** (related to gate incident B016).
- **Counter-surfing.** Stealing food off counters.
- **Greeting rituals when humans return** — typically dramatic, involve specific behaviors per dog.

---

## How to use this file

When designing a new mechanic:
1. Skim the relevant section.
2. If the mechanic exists in the science and matches an observed behavior in `canon/`, build it.
3. If it exists in the science but we haven't observed it yet, ask Ted before adding — we want to keep canon real.
4. If it's pure speculation (not in this file, not in canon), put it in `design/PARKING.md` instead.

When a behavior here graduates to a real mechanic, link it from the relevant section here AND create a `canon/behaviors/B###_*.md` entry.

---

## Sources / further reading (general)

Not citations — just where to dig if you want depth on any of the above.

- Patricia McConnell — *The Other End of the Leash* (general behavior, very accessible)
- Turid Rugaas — *On Talking Terms with Dogs: Calming Signals*
- Alexandra Horowitz — *Inside of a Dog* (cognition + perception)
- Stanley Coren — *How Dogs Think* (cognition, decision-making)
- Patricia McConnell — *For the Love of a Dog* (emotion, attachment)
- Brian Hare & Vanessa Woods — *The Genius of Dogs* (cognition + evolution)
- *Applied Animal Behaviour Science* (journal — primary research)
- *Journal of Veterinary Behavior* (journal — clinical + research)
- AKC's breed-trait write-ups for breed-typical baselines
- The Whole Dog Journal for current management practice

Don't pretend to citations we haven't actually read in detail. If a mechanic claim hinges on a specific finding, look it up before shipping.

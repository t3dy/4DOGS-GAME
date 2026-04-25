# Mechanic 14 — Individual Play Preferences

**Research:** `design/behaviorresearch.md` §14
**Canon:** `canon/behaviors/B014_tennis_ball_disappointment.md`, `B015_dog_park_zoomies.md`
**Live encounters:** `tennis_ball` (#10), `dog_park` (#9)

## What this is

Toy preferences are individual, not universal. None of Ted's four care about tennis balls. Dalamar (Ted's previous border collie) was obsessed. Environment also matters — the same dogs who ignore objects at home will run around at the dog park.

The mechanic captures *negative space* (the failed experiment) and *environmental override* (the park works because the place changes everything).

## Implementation now

- `tennis_ball`: throw, roll, squeeze, or pocket. All four resolutions show the dogs failing to engage. The Dalamar memory option is its own beat.
- `dog_park`: unleash, keep close, observe, head home. All four resolutions show the dogs DOING things. Anxiety drops most under unleash.

The contrast is intentional: side-by-side these two encounters teach the player that "what works for these dogs" is environmental, not object-based.

## Levers the player has

- Try-and-fail experiments at home (tennis ball).
- Take the dogs to a place where they engage (dog park).
- Compare to Dalamar's history (narrative beat, not mechanical).

## Levers the player does NOT have (yet)

- Other toys with individual preferences. Pink pig works for Attila; tennis ball works for nobody. We could populate a per-dog preference matrix.
- Other locations. Park works; what about a hike? A friend's house? A car ride?
- Persistent disappointment as an emotional cost — currently `comedies_endured` increments, but no real player consequence.

## Future expansion

- **Toy preference matrix:** every toy has a per-dog interest score 0-3. Throw / roll / hand-over actions resolve based on the score. Pink pig: Attila 3, Crockett 2, Okie 1, Tex 0. Tennis ball: all 0.
- **Location library:** add hike, car ride, friend's yard. Each modifies anxiety and engagement.
- **Dalamar-as-flavor:** add ambient interrupt lines that surface Dalamar's memory at random. "You thought about Dalamar for a second."

## Voice rules

The tennis ball failure is funny but not cruel. Don't write the dogs as broken or inadequate. They're just not into it. "I threw it. Okie watched it go. Tex blinked at it." Short. Each dog gets one verb. No commentary.

Dalamar should be invoked with affection, not nostalgia. "I had a border collie named Dalamar in my 20s who was obsessed with the ball." Period.

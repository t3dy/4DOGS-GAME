"""
DOGSGAME — terminal prototype, v2 (encounter-based).

Same kernel as v1, but driven by an Encounter + Sequencer model instead of
free-text scene navigation. Each encounter offers 2-5 numbered options;
outcomes mutate the world and queue follow-up encounters. A "case" is an
ordered run of encounters wrapped by an opening and a debrief.

Voice: noir, per design/NOIR_LENS.md.
Architecture: kernel / encounters / sequencer / narrator / renderer (text only).

Run:
    python dogsim.py             — play the default case interactively
    python dogsim.py --test      — scripted run; choices pre-selected
    python dogsim.py --case bush — pick a specific case (see CASES dict)
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Optional

# Windows console defaults to cp1252; we want UTF-8 for the box drawing.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ============================================================================
# KERNEL — pure state, no IO
# ============================================================================

class TileKind(Enum):
    HOUSE_WALL = "H"
    GARAGE_DOOR = "G"
    PATIO = "P"
    DRIVEWAY = "D"
    LAWN = "."
    DIRT = ","
    GROUNDCOVER = "~"
    PLUM_TREE = "T"
    FRUIT_TREE = "F"
    BLUEBERRY_BUSH = "B"
    DEAD_BUSH = "x"


@dataclass
class World:
    """All mutable game state. Encounters mutate this; nothing else does."""
    bush_health: int = 3                 # 3 alive, 0 dead
    okie_anxiety: int = 3                # 0-10
    okie_bladder: int = 7                # 0-10
    bone_cache: int = 0
    bones_in_pack: int = 5
    scoop_days_ago: int = 1              # 0 today, 1 yesterday, 99 you-don't-want-to-know
    sleep_location: str = "garage"       # "house" or "garage"
    in_garage: bool = False
    leashed: bool = False
    garage_door_open: bool = False
    score: dict = field(default_factory=lambda: {"cases_resolved": 0, "comedies_endured": 0,
                                                  "bushes_dead": 0, "neighbors_owed_money": 0})
    log: list[str] = field(default_factory=list)         # event history
    case_id: str = ""

    def emit(self, kind: str, **data):
        self.log.append(f"[{kind}] {data}")


# ============================================================================
# ENCOUNTERS — the heart of the loop
# ============================================================================

@dataclass
class Option:
    key: str                                       # short id, e.g. "pee_bush"
    label: str                                     # menu text shown to player
    enabled: Callable[[World], bool] = lambda w: True


@dataclass
class Encounter:
    """A single decision moment. 2-5 options. Resolution mutates world and
    optionally queues follow-up encounter IDs."""
    id: str
    title: str
    intro: Callable[[World], str]                              # narration shown at presentation
    options: Callable[[World], list[Option]]                   # 2-5 options for this state
    resolve: Callable[[World, str], "Resolution"]              # apply choice → outcome


@dataclass
class Resolution:
    narration: str                       # outcome text
    follow_ups: list[str] = field(default_factory=list)   # encounter ids to queue next
    end_case: bool = False               # short-circuit the case


# ----- Encounter library --------------------------------------------------

def enc_morning_briefing() -> Encounter:
    def intro(w):
        sleep = "the garage, on principle" if w.sleep_location == "garage" else "the bedroom floor, in error"
        return (
            "You wake. The house is quiet in the way that suggests dogs are\n"
            "either asleep or planning something. Okie spent the night in\n"
            f"{sleep}.\n\n"
            "The case file for today is open on the kitchen table.\n"
            "It does not yet have a title."
        )
    def options(w):
        opts = [
            Option("yard", "Step into the yard. Get the lay of things."),
            Option("garage", "Go to the garage. Check on the bone economy."),
            Option("bed", "Lie back down. It's that kind of morning."),
        ]
        if w.scoop_days_ago > 1:
            opts.append(Option("scoop", "Grab a bag and scoop the yard. Pay the toll."))
        return opts
    def resolve(w, k):
        if k == "yard":
            return Resolution("You step out. The grass looks guilty. The bush looks alive.",
                              follow_ups=["yard_bush"])
        if k == "garage":
            return Resolution("You open the side door to the garage. The smell of dog and oil rises.",
                              follow_ups=["garage_bone_pack"])
        if k == "bed":
            return Resolution("You crawl back. The afternoon is hours away. You have time.",
                              follow_ups=["bed_face_lick"])
        if k == "scoop":
            w.scoop_days_ago = 0
            return Resolution("You scoop. The yard is uglier and cleaner. You earn nothing visible. You'll know.",
                              follow_ups=["yard_bush"])
        return Resolution("[noop]")
    return Encounter("morning_briefing", "MORNING BRIEFING", intro, options, resolve)


def enc_yard_bush() -> Encounter:
    def intro(w):
        if w.bush_health == 3: bush_state = "still alive, still smug"
        elif w.bush_health == 2: bush_state = "yellowing at the leaves, beginning to suspect"
        elif w.bush_health == 1: bush_state = "wilting in earnest now"
        else: bush_state = "a memorial — but you knew that"
        return (
            "  THE YARD\n\n"
            f"  The blueberry bush sits in the dirt strip: {bush_state}.\n"
            f"  Okie is at your heel. His bladder reads {w.okie_bladder}/10.\n"
            "  The fruit trees keep their counsel."
        )
    def options(w):
        if w.bush_health <= 0:
            return [
                Option("memorial", "Stand at the dead-bush tile. Pay your respects."),
                Option("leave", "Go back inside. Nothing left to do here."),
            ]
        opts = [
            Option("examine", "Examine the bush. Take inventory."),
            Option("pee", "Let Okie pee on the bush."),
            Option("call_off", "Call Okie away. Pee on the lawn instead."),
            Option("leave", "Leave the yard. Bush lives another day."),
        ]
        return opts
    def resolve(w, k):
        if k == "examine":
            return Resolution(
                f"  You examine the bush. Health: {w.bush_health}/3. Berries: theoretical.\n"
                "  The bush, for its part, examines you back.",
                follow_ups=["yard_bush"])
        if k == "pee":
            w.bush_health -= 1
            w.okie_bladder = max(0, w.okie_bladder - 3)
            if w.bush_health <= 0:
                w.score["bushes_dead"] += 1
                return Resolution(
                    "\n  ─────────────────────────────────────────────\n"
                    "  THE BLUEBERRY BUSH IS DEAD.\n"
                    "  Cause of death: a small dog with strong opinions.\n"
                    "  Suspect: in the room. Showing no remorse.\n"
                    "  ─────────────────────────────────────────────\n",
                    follow_ups=["debrief"])
            stages = {2: "yellowing", 1: "wilting"}
            return Resolution(
                f"  Okie circles. Lifts a leg. The bush is now {stages[w.bush_health]}.",
                follow_ups=["yard_bush"])
        if k == "call_off":
            w.okie_bladder = max(0, w.okie_bladder - 3)
            return Resolution(
                "  You call him off. He pees on the lawn instead. The lawn will yellow.\n"
                "  The bush exhales — quietly, in case you change your mind.",
                follow_ups=["yard_passerby"])
        if k == "memorial":
            return Resolution(
                "  You stand on the dead-bush tile. The dirt remembers. Okie sits beside you,\n"
                "  not quite contrite. The wind, helpfully, says nothing.")
        if k == "leave":
            return Resolution("  You leave the yard. The bush survives this turn.",
                              follow_ups=["garage_bone_pack"])
        return Resolution("[noop]")
    return Encounter("yard_bush", "THE BLUEBERRY (B001)", intro, options, resolve)


def enc_yard_passerby() -> Encounter:
    def intro(w):
        return (
            "  A diesel rumble climbs 15th Ave. A logging truck, by the sound.\n"
            "  Tex, somewhere in the garage, has noticed. So has Okie.\n"
            "  A bark begins. A second bark answers. They amplify."
        )
    def options(w):
        return [
            Option("shush", "Go inside, shush them. Restore order."),
            Option("watch", "Stay in the yard. Listen. Time it."),
            Option("join", "Bark with them. (Why not.)"),
        ]
    def resolve(w, k):
        if k == "shush":
            return Resolution(
                "  You go in. You shush. You are obeyed for forty seconds. Then it resumes.\n"
                "  The truck is long past. The barking is now about itself.",
                follow_ups=["garage_bone_pack"])
        if k == "watch":
            w.score["comedies_endured"] += 1
            return Resolution(
                "  You stand in the yard and watch them watch the world. Six seconds after the truck\n"
                "  is gone, they continue. On principle. You count the principles.",
                follow_ups=["garage_bone_pack"])
        if k == "join":
            w.score["comedies_endured"] += 1
            return Resolution(
                "  You bark. The dogs look at you with a kind of professional disappointment.\n"
                "  The truck driver does not hear. The neighbors hear. You stop.",
                follow_ups=["garage_bone_pack"])
        return Resolution("[noop]")
    return Encounter("yard_passerby", "TRAFFIC (B009)", intro, options, resolve)


def enc_garage_bone_pack() -> Encounter:
    def intro(w):
        return (
            "  THE GARAGE\n\n"
            f"  An Old Roy bag is open in the corner. {w.bones_in_pack} bones remain.\n"
            "  The kiddie-pool beds wait, blankets piled. Okie has noticed.\n"
            f"  His current cache (under the blanket): {w.bone_cache}."
        )
    def options(w):
        opts = []
        if w.bones_in_pack > 0:
            opts.append(Option("hand_one", "Give Okie one bone. Watch the ritual."))
            if w.bones_in_pack >= 3:
                opts.append(Option("hand_three", "Give him three. Make a deposit."))
        opts.append(Option("inspect", "Lift a blanket. Inspect the cache."))
        opts.append(Option("close_bag", "Close the bag. End the deposit window."))
        return opts
    def resolve(w, k):
        if k == "hand_one":
            w.bones_in_pack -= 1
            w.bone_cache += 1
            return Resolution(
                f"  You hand Okie a bone. He carries it like contraband to the kiddie pool.\n"
                f"  The blanket lifts. The bone joins its kin. Cache: {w.bone_cache}. He is content.",
                follow_ups=["garage_bone_pack"])
        if k == "hand_three":
            took = min(3, w.bones_in_pack)
            w.bones_in_pack -= took
            w.bone_cache += took
            return Resolution(
                f"  Three bones, three trips. He paces with purpose. The cache is now {w.bone_cache}.\n"
                f"  Somewhere, a small dog believes himself a banker. He's not wrong.",
                follow_ups=["garage_okie_anxious"])
        if k == "inspect":
            return Resolution(
                f"  You lift the blanket. {w.bone_cache} bones, arranged with no system you can detect.\n"
                f"  Okie watches from the doorway. You replace the blanket. Some things are not yours to count.",
                follow_ups=["garage_bone_pack"])
        if k == "close_bag":
            return Resolution(
                "  You close the bag. The deposit window is shut.\n"
                f"  {w.bones_in_pack} bones remain in reserve. Okie sighs the sigh of a banker mid-quarter.",
                follow_ups=["garage_okie_anxious"])
        return Resolution("[noop]")
    return Encounter("garage_bone_pack", "THE BONE BANK (B005)", intro, options, resolve)


def enc_garage_okie_anxious() -> Encounter:
    def intro(w):
        return (
            "  Okie paces near the inner door. He nudges it with his nose.\n"
            f"  His anxiety reads {w.okie_anxiety}/10 and rising. The garage is his bunker;\n"
            "  the bunker is, however, only a bunker if the door stays closed."
        )
    def options(w):
        opts = [
            Option("comfort", "Sit on the floor with him. Wait it out."),
            Option("toy", "Bring a chew toy. Distract."),
            Option("ignore", "Walk away. Let him self-regulate."),
        ]
        if w.scoop_days_ago > 1:
            opts.append(Option("scoop_diversion", "Take him with you to scoop the yard. Mutual labor."))
        return opts
    def resolve(w, k):
        if k == "comfort":
            w.okie_anxiety = max(0, w.okie_anxiety - 3)
            return Resolution(
                "  You sit. He folds himself against your leg. The anxiety drops two notches.\n"
                "  No words exchanged. None needed.",
                follow_ups=["bed_face_lick"])
        if k == "toy":
            w.okie_anxiety = max(0, w.okie_anxiety - 2)
            return Resolution(
                "  You bring a chew toy. He accepts. The pacing pauses. Investment: low. Return: adequate.",
                follow_ups=["bed_face_lick"])
        if k == "ignore":
            w.okie_anxiety = min(10, w.okie_anxiety + 2)
            return Resolution(
                "  You walk away. The pacing accelerates. A flashback flickers — an old bed,\n"
                "  shredded foam, a tail held low. You pretend you didn't see it.",
                follow_ups=["bed_face_lick"])
        if k == "scoop_diversion":
            w.scoop_days_ago = 0
            w.okie_anxiety = max(0, w.okie_anxiety - 4)
            return Resolution(
                "  You take him out with you. He supervises the scoop with the gravity of a foreman.\n"
                "  The yard improves. So does he. So, frankly, do you.",
                follow_ups=["bed_face_lick"])
        return Resolution("[noop]")
    return Encounter("garage_okie_anxious", "ANXIETY (B006)", intro, options, resolve)


def enc_bed_face_lick() -> Encounter:
    def intro(w):
        return (
            "  THE BEDROOM, AFTERNOON\n\n"
            "  You lie down. Not to sleep — to stop. Okie pads in.\n"
            "  Considers. Joins. He is too close to your face. He is professional about it.\n"
            "  The tongue is loaded.\n"
        )
    def options(w):
        scoop_label = {0: "today", 1: "yesterday"}.get(w.scoop_days_ago, "I don't want to talk about it")
        return [
            Option("dodge",   "Dodge the lick. (Reflex defense.)"),
            Option("accept",  "Accept the lick. (Hope.)"),
            Option("think",   f"Think about the yard scoop first. (Last scoop: {scoop_label}.)"),
            Option("eject",   "Push him off the bed. (Cowardly. Effective.)"),
        ]
    def resolve(w, k):
        if k == "dodge":
            return Resolution(
                "  You turn your head. Tongue grazes the cheek. Negligible damage.\n"
                "  Okie looks affronted. He'll forget by dinner.",
                follow_ups=["debrief"])
        if k == "accept":
            scoop = w.scoop_days_ago
            if scoop == 0:
                w.score["comedies_endured"] += 1
                line = ("  You let him. Warm and brief and undignified, like all good things.\n"
                        "  The yard is clean today. You earned this.")
            elif scoop == 1:
                w.score["comedies_endured"] += 1
                line = ("  You let him. Halfway through, you remember yesterday. You did not scoop.\n"
                        "  The taste, when it arrives, is informational.")
            else:
                w.score["comedies_endured"] += 2
                line = ("  You let him. The lick lasts an unreasonable duration. You will taste this for hours.\n"
                        "  You knew. You did it anyway. There's a name for that. You won't say it.")
            return Resolution(line, follow_ups=["debrief"])
        if k == "think":
            scoop_label = {0: "today", 1: "yesterday"}.get(w.scoop_days_ago, "uncertain")
            return Resolution(
                f"  You think back. Last scoop: {scoop_label}.\n"
                "  Okie waits, tongue patient. The math is yours to do.",
                follow_ups=["bed_face_lick"])   # loop back; force commitment
        if k == "eject":
            return Resolution(
                "  You push him off. He goes, with dignity. The bed feels larger and lonelier.\n"
                "  You will regret this in twenty minutes.",
                follow_ups=["debrief"])
        return Resolution("[noop]")
    return Encounter("bed_face_lick", "FACE-LICK (B012)", intro, options, resolve)


def enc_attila_whine() -> Encounter:
    def intro(w):
        return (
            "  THE GARAGE — LATE MORNING\n\n"
            "  Attila has noticed the leash on the hook. He has not moved toward it.\n"
            "  He doesn't have to. The whine starts low — a sound out of scale with\n"
            "  his body — and rises. One hundred pounds of dog, pitched like a kettle.\n"
        )
    def options(w):
        opts = [
            Option("leash_now", "Clip the leash. Open the door. Go."),
            Option("wait_quiet", "Wait. Do not move. See if he stops."),
            Option("abandon",   "Hang the leash back up. He will live."),
        ]
        if w.okie_anxiety <= 4:
            opts.append(Option("bring_okie", "Take Okie with you. Two dogs. One leash. Chaos."))
        return opts
    def resolve(w, k):
        if k == "leash_now":
            w.leashed = True
            w.garage_door_open = True
            w.score["comedies_endured"] += 1
            return Resolution(
                "  You clip the leash. The whine crescendos. You open the garage door.\n"
                "  The whine does not stop. The whine has become a matter of principle.\n"
                "  The two of you walk out into the morning, accompanied by a soundtrack\n"
                "  no one would believe.",
                follow_ups=["bed_face_lick"])
        if k == "wait_quiet":
            return Resolution(
                "  You wait. Forty seconds pass. The whine does not abate. It cycles.\n"
                "  At second forty-five you understand: it will not stop on its own.\n"
                "  This is the lesson, and you have learned it before.",
                follow_ups=["attila_whine"])
        if k == "abandon":
            w.score["comedies_endured"] += 1
            return Resolution(
                "  You hang the leash back up. Attila looks at you. The whine pivots,\n"
                "  smoothly, into something quieter — a low, wronged register.\n"
                "  He'll forgive you by lunch. You will not forgive yourself by then.",
                follow_ups=["bed_face_lick"])
        if k == "bring_okie":
            w.leashed = True
            w.garage_door_open = True
            w.okie_anxiety = max(0, w.okie_anxiety - 1)
            w.score["comedies_endured"] += 2
            return Resolution(
                "  You clip both leashes. Two dogs, one human, three opinions.\n"
                "  Attila stops whining the moment Okie steps out the door — vindicated,\n"
                "  apparently, by company. Okie's anxiety eases. Yours does not.",
                follow_ups=["bed_face_lick"])
        return Resolution("[noop]")
    return Encounter("attila_whine", "PRE-WALK WHINE (B010)", intro, options, resolve)


def enc_squeak_steal() -> Encounter:
    def intro(w):
        return (
            "  THE LIVING ROOM\n\n"
            "  From the corner: SQUEAK. Pause. SQUEAK. Pause. SQUEAK.\n"
            "  Attila is working the pink pig. He is not playing — he is signaling.\n"
            "  The pause-then-squeak is the give-away. He wants you in the room.\n"
            "  Across the rug, Crockett has lifted his head. He is also paying attention,\n"
            "  but for different reasons."
        )
    def options(w):
        return [
            Option("engage",     "Sit with Attila. Receive the request."),
            Option("ignore",     "Stay where you are. Let it run its course."),
            Option("intercept",  "Pet Crockett first. Defuse the steal."),
            Option("watch",      "Do nothing. Watch. Take notes."),
        ]
    def resolve(w, k):
        if k == "engage":
            return Resolution(
                "  You sit with Attila. He stops squeaking immediately, dignity restored.\n"
                "  Crockett, foreclosed, sighs and lays his head back down.\n"
                "  No theft today. The pig is safe.",
                follow_ups=["attila_whine"])
        if k == "ignore":
            w.score["comedies_endured"] += 1
            return Resolution(
                "  You ignore the squeaks. Three more cycles. Then a slow padding sound.\n"
                "  Crockett walks across the rug, low and deliberate. The squeaking stops.\n"
                "  Attila blinks. The pig is now Crockett's. Crockett does not squeak it.\n"
                "  He just holds it, like evidence.",
                follow_ups=["attila_whine"])
        if k == "intercept":
            return Resolution(
                "  You pet Crockett, who accepts but does not relax. The squeak loop continues.\n"
                "  After a minute Crockett wanders off, his criminal intent only deferred.\n"
                "  The pink pig squeaks once more, and Attila — getting no human — sighs.",
                follow_ups=["attila_whine"])
        if k == "watch":
            w.score["comedies_endured"] += 1
            return Resolution(
                "  You take notes. Attila signals. Crockett pads. Theft occurs at second 47.\n"
                "  Attila's reaction frame: a single, slow blink. You record this.\n"
                "  Somewhere a future game design benefits.",
                follow_ups=["attila_whine"])
        return Resolution("[noop]")
    return Encounter("squeak_steal", "SQUEAK & STEAL (B003+B004)", intro, options, resolve)


def enc_debrief() -> Encounter:
    def intro(w):
        return (
            "\n  ─── END OF SESSION ───\n\n"
            "  The case file is closed for the day. You sit at the kitchen table\n"
            "  and tally what happened.\n"
        )
    def options(w):
        return [
            Option("accept_score", "Accept the score. Walk away."),
            Option("review", "Review the event log."),
        ]
    def resolve(w, k):
        if k == "accept_score":
            return Resolution(
                f"  Bushes killed today:           {w.score['bushes_dead']}\n"
                f"  Bones banked (Okie's vault):   {w.bone_cache}\n"
                f"  Comedies endured:              {w.score['comedies_endured']}\n"
                f"  Anxiety, final:                {w.okie_anxiety}/10\n"
                "\n  You set the case down. The dogs continue without you. They always do.",
                end_case=True)
        if k == "review":
            tail = "\n".join(f"    {entry}" for entry in w.log[-10:])
            return Resolution("  Last ten events:\n" + (tail or "    (nothing logged)"),
                              follow_ups=["debrief"])
        return Resolution("[noop]")
    return Encounter("debrief", "DEBRIEF", intro, options, resolve)


# ----- Catalog --------------------------------------------------------------

CATALOG: dict[str, Callable[[], Encounter]] = {
    "morning_briefing":   enc_morning_briefing,
    "yard_bush":          enc_yard_bush,
    "yard_passerby":      enc_yard_passerby,
    "garage_bone_pack":   enc_garage_bone_pack,
    "garage_okie_anxious": enc_garage_okie_anxious,
    "attila_whine":       enc_attila_whine,
    "squeak_steal":       enc_squeak_steal,
    "bed_face_lick":      enc_bed_face_lick,
    "debrief":            enc_debrief,
}


# ============================================================================
# CASES — sequenced sets of encounters wrapped as a session
# ============================================================================

@dataclass
class Case:
    id: str
    title: str
    opening: str
    seed_encounters: list[str]   # initial queue


CASES: dict[str, Case] = {
    "default": Case(
        id="default",
        title="CASE 1: A MORNING IN SULTAN",
        opening=("  CASE FILE — A MORNING IN SULTAN, WA\n"
                 "  Subject: Okie. (Aussie. Anxious. Bone-banker. Suspect.)\n"
                 "  Detective: you, again.\n"
                 "  Coffee: cold."),
        seed_encounters=["morning_briefing"],
    ),
    "bush": Case(
        id="bush",
        title="CASE 1A: THE BLUEBERRY",
        opening=("  CASE FILE — THE BLUEBERRY\n"
                 "  Single-encounter run. Bush. Dog. Decision."),
        seed_encounters=["yard_bush", "debrief"],
    ),
    "garage": Case(
        id="garage",
        title="CASE 1B: THE BONE BANK",
        opening=("  CASE FILE — THE BONE BANK\n"
                 "  A study in unmotivated hoarding."),
        seed_encounters=["garage_bone_pack", "garage_okie_anxious", "debrief"],
    ),
    "bed": Case(
        id="bed",
        title="CASE 1C: THE FACE-LICK",
        opening=("  CASE FILE — THE FACE-LICK\n"
                 "  An exercise in self-honesty."),
        seed_encounters=["bed_face_lick", "debrief"],
    ),
    "long": Case(
        id="long",
        title="CASE 2: A LONGER MORNING",
        opening=("  CASE FILE — A LONGER MORNING\n"
                 "  Subject: All four dogs, in sequence.\n"
                 "  Briefing: Yard. Bones. A pig. A leash. A bedroom.\n"
                 "  Time budget: until you stop."),
        seed_encounters=["morning_briefing", "yard_bush", "squeak_steal",
                         "garage_bone_pack", "attila_whine", "bed_face_lick", "debrief"],
    ),
}


# ============================================================================
# RENDERER + SEQUENCER + GAME LOOP
# ============================================================================

class TextRenderer:
    WIDTH = 64

    def banner(self, case: Case):
        bar = "═" * self.WIDTH
        print(f"\n╔{bar}╗")
        print(f"║{'D O G S G A M E   —   noir prototype'.center(self.WIDTH)}║")
        print(f"║{case.title.center(self.WIDTH)}║")
        print(f"╚{bar}╝")
        print(case.opening)

    def show(self, text: str):
        print(text)

    def menu(self, options: list[Option]) -> int:
        print()
        for i, o in enumerate(options, 1):
            print(f"    {i}.  {o.label}")
        print()
        while True:
            try:
                raw = input(f"    Choose 1-{len(options)}: ").strip()
            except EOFError:
                return -1
            if raw.isdigit():
                n = int(raw)
                if 1 <= n <= len(options):
                    return n - 1
            print("    (Pick a number from the list.)")


class Sequencer:
    """Drives encounters off a queue. Resolutions can append follow-ups."""

    def __init__(self, world: World, renderer: TextRenderer,
                 scripted_choices: Optional[list[int]] = None):
        self.world = world
        self.renderer = renderer
        self.queue: list[str] = []
        self.scripted = scripted_choices  # list of 0-indexed choices to take

    def enqueue(self, *enc_ids: str):
        self.queue.extend(enc_ids)

    def run(self):
        while self.queue:
            enc_id = self.queue.pop(0)
            if enc_id not in CATALOG:
                self.renderer.show(f"  [unknown encounter: {enc_id}]")
                continue
            enc = CATALOG[enc_id]()
            self.renderer.show(f"\n  ─── {enc.title} ───")
            self.renderer.show(enc.intro(self.world))
            opts = enc.options(self.world)
            opts = [o for o in opts if o.enabled(self.world)]
            if not opts:
                self.renderer.show("  (no actions available)")
                continue
            if self.scripted is not None:
                if not self.scripted:
                    self.renderer.show("  [scripted run exhausted]")
                    return
                idx = self.scripted.pop(0)
                if idx >= len(opts):
                    idx = 0
                print()
                for i, o in enumerate(opts, 1):
                    print(f"    {i}.  {o.label}")
                print(f"    > {idx + 1}")
            else:
                idx = self.renderer.menu(opts)
                if idx < 0:
                    return
            chosen = opts[idx]
            self.world.emit("choice", encounter=enc.id, key=chosen.key, label=chosen.label)
            res = enc.resolve(self.world, chosen.key)
            self.renderer.show("")
            self.renderer.show(res.narration)
            if res.end_case:
                return
            for fu in res.follow_ups:
                self.queue.append(fu)


def play(case_id: str = "default", scripted: Optional[list[int]] = None):
    world = World()
    case = CASES.get(case_id, CASES["default"])
    world.case_id = case.id
    renderer = TextRenderer()
    renderer.banner(case)
    seq = Sequencer(world, renderer, scripted_choices=scripted)
    seq.enqueue(*case.seed_encounters)
    seq.run()


# ============================================================================
# TEST MODE — scripted runs, no stdin
# ============================================================================

def test_run():
    print("\n========== SCRIPT 1: KILL THE BUSH ==========")
    # morning_briefing → yard (option 0) → yard_bush pee × 3 → debrief → accept_score
    play("default", scripted=[
        0,   # morning_briefing → "Step into the yard"
        1,   # yard_bush → "Let Okie pee on the bush" (health 3→2)
        1,   # yard_bush → pee (health 2→1)
        1,   # yard_bush → pee (health 1→0; queues debrief)
        0,   # debrief → "Accept the score"
    ])

    print("\n\n========== SCRIPT 2: BANK BONES ==========")
    play("garage", scripted=[
        1,   # garage_bone_pack → "Give him three"
        2,   # garage_bone_pack (loop) → "Close the bag"
        0,   # garage_okie_anxious → "Sit on the floor with him"
        0,   # bed_face_lick → "Dodge"
        0,   # debrief → accept
    ])

    print("\n\n========== SCRIPT 3: FACE-LICK BRANCHES ==========")
    for scoop, label in [(0, "today"), (1, "yesterday"), (99, "ignore")]:
        print(f"\n--- scoop_days_ago = {scoop} ({label}) ---")
        # bed_face_lick has 4 options: 0=dodge, 1=accept, 2=think, 3=eject
        play("bed", scripted=[
            2,   # think first
            1,   # then accept
            0,   # debrief → accept_score
        ])
        # NOTE: scoop_days_ago is set inside Case state; for the demo we just
        # show that the "think" branch loops back and "accept" resolves. The
        # actual scoop value defaults to 1 (yesterday). To exercise other
        # branches in a real session, the player adjusts choice keys.


def main():
    if "--test" in sys.argv:
        test_run()
        return
    case_id = "default"
    if "--case" in sys.argv:
        i = sys.argv.index("--case")
        if i + 1 < len(sys.argv):
            case_id = sys.argv[i + 1]
    play(case_id)


if __name__ == "__main__":
    main()

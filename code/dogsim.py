"""
DOGSGAME v1 — Okie pees on the blueberry bush. That's it.

Single dog, one behavior (B001), TEXT renderer, one event row to data/dogsim.db.

    python code/dogsim.py
"""
import sqlite3
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "dogsim.db"

# Yard map from canon/yard.md. 6 wide x 5 tall.
YARD = [
    "HHHHHG",   # house wall + garage door
    "PPPPPD",   # patio + driveway
    "....DD",   # lawn
    ",B,T,D",   # dirt + blueberry bush + plum
    "~~x~FF",   # groundcover + dead-bush memorial + fruit trees
]
BUSH = (1, 3)


def render(okie, bush_health):
    states = {3: "alive", 2: "yellowing", 1: "wilting", 0: "DEAD"}
    print()
    for y, row in enumerate(YARD):
        line = "  "
        for x, ch in enumerate(row):
            if (x, y) == okie:
                line += "O "
            elif (x, y) == BUSH and bush_health == 0:
                line += "x "
            else:
                line += ch + " "
        print(line)
    print(f"\n  Bush: {states[bush_health]}")


def say(line):
    print(f"  {line}")


def main():
    DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id    INTEGER PRIMARY KEY,
            ts    TEXT NOT NULL,
            kind  TEXT NOT NULL,
            actor TEXT,
            data  TEXT
        )
    """)

    okie = (4, 1)         # patio
    bush_health = 3

    print("\n  ==== DOGSGAME v1 — A morning in Sultan, WA ====\n")
    say("Okie steps off the patio. The blueberry bush is in sight.")
    render(okie, bush_health)

    okie = BUSH
    say("He picks his way down to the dirt strip and stops at the bush.")
    render(okie, bush_health)

    for _ in range(3):
        bush_health -= 1
        if bush_health > 0:
            stage = ("wilting", "yellowing")[bush_health - 1]
            say(f"Okie lifts a leg. The bush is now {stage}.")
        else:
            say("Okie lifts a leg. The blueberry bush dies. He shows no remorse.")
        render(okie, bush_health)

    conn.execute(
        "INSERT INTO events (ts, kind, actor, data) VALUES (?, ?, ?, ?)",
        (time.strftime("%Y-%m-%dT%H:%M:%S"), "bush_dead", "okie", "B001"),
    )
    conn.commit()

    cnt = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    print(f"\n  ==== END ====")
    print(f"  Logged 1 event to {DB.relative_to(ROOT)}  (total rows: {cnt})")


if __name__ == "__main__":
    main()

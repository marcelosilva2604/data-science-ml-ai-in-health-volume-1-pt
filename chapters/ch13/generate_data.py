"""Generate the Chapter 13 population: the schoolchildren of one municipality.

One row is one enrolled child. Columns: child_id, school (S01 to S48), school_type (private or public),
dmft (number of decayed, missing, or filled teeth; a count that starts at 0).
Schools S01-S12 are private and S13-S48 are public; S01 to S03 are the three schools closest to the municipal dental clinic.
dmft is Poisson with a mean that depends on the school type and on a school effect, times a child effect (gamma), which gives
many zeros and a long right tail, capped at 20 (a child has 20 primary teeth, so dmft cannot exceed 20), and children of the same school resemble each other (clustering).
Teaching values, not estimates for a real municipality. Seed 13. Running time: about one second.
"""
from pathlib import Path
import csv
import math
import random


def poisson(rng, lam):
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(13)
    rows, n = [], 0
    for s in range(1, 49):
        private = s <= 12
        size = rng.randint(200, 400)
        school_effect = rng.gauss(0, 0.20)
        base = 1.05 if private else 2.25
        for _ in range(size):
            n += 1
            lam = base * math.exp(school_effect) * rng.gammavariate(1.0 / 0.9, 0.9)
            rows.append({"child_id": f"K{n:05d}", "school": f"S{s:02d}", "school_type": "private" if private else "public",
                         "dmft": min(poisson(rng, lam), 20)})
    with open(output_dir / "schoolchildren.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "children written")


if __name__ == "__main__":
    generate()

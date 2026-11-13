"""Generate the Chapter 11 register: 5,000 deliveries in one public maternity unit.

One row is one delivery. Columns: delivery_id, cesarean, hemorrhage, infection (yes/no).
The rates are chosen to be close to published figures for cesarean delivery, postpartum
hemorrhage, and puerperal infection; they are teaching values, not estimates for a real unit.
Seed 11. Running time: about one second.
"""
from pathlib import Path
import csv
import random


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(11)
    yn = lambda x: "yes" if x else "no"
    rows = []
    for i in range(1, 5001):
        cesarean = rng.random() < 0.26
        hemorrhage = rng.random() < (0.075 if cesarean else 0.054)
        p_infection = (0.06 if cesarean else 0.015) * (2.5 if hemorrhage else 1.0)
        infection = rng.random() < p_infection
        rows.append({"delivery_id": f"D{i:04d}", "cesarean": yn(cesarean),
                     "hemorrhage": yn(hemorrhage), "infection": yn(infection)})
    with open(output_dir / "deliveries.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "deliveries written")


if __name__ == "__main__":
    generate()

"""Generate the Chapter 3 data: one synthetic day of an adult emergency department triage log.

data/triage.csv: 200 adult visits, one row per visit, 12 columns (visit_id, arrived_at, seen_at, arrival_route, sex, age_years,
triage_level, pain, temp_c, heart_rate, prior_visits, admitted). Three low-acuity visits have no time seen (the patient left before
being seen) and four temperatures are missing. data/triage_check.csv: the first 12 rows with three planted recording problems
(a triage level of 6, an age of 430, a missing temperature), used by the validation step.
The pattern is constructed for teaching and is not a model of how emergency departments behave. Seed 3. Standard library only.
Run: python generate_data.py
"""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

FIELDS = ["visit_id", "arrived_at", "seen_at", "arrival_route", "sex",
          "age_years", "triage_level", "pain", "temp_c", "heart_rate",
          "prior_visits", "admitted"]
PAIN = ["none", "mild", "moderate", "severe"]


def pick(rng, values, weights):
    return rng.choices(values, weights=weights, k=1)[0]


def make_log(seed=3, n=200):
    rng = random.Random(seed)
    start = datetime(2026, 3, 9, 0, 0)
    minutes = sorted(rng.randrange(0, 24 * 60) for _ in range(n))
    rows = []
    for i, minute in enumerate(minutes, start=1):
        level = pick(rng, [1, 2, 3, 4, 5], [2, 12, 40, 34, 12])
        # 1 direct walk-in; 2 direct ambulance; 3 interfacility transfer
        # regardless of transport. Direct arrivals exclude transfers.
        route = pick(rng, [1, 2, 3],
                    {1: [20, 70, 10], 2: [45, 45, 10]}.get(level, [80, 12, 8]))
        age = min(95, max(18, int(rng.gauss(52, 19))))
        fever = rng.random() < (0.30 if level <= 3 else 0.12)
        temp = round(rng.uniform(38.0, 40.2) if fever else rng.uniform(36.0, 37.6), 1)
        hr = int(rng.gauss(84 + (14 if fever else 0) + (6 - level) * 3, 12))
        pain = pick(rng, PAIN, [15, 30, 35, 20] if level <= 3 else [30, 40, 22, 8])
        prior = pick(rng, [0, 1, 2, 3, 4, 5, 6], [45, 25, 13, 8, 5, 3, 1])
        low, high = {1: (0, 5), 2: (5, 25), 3: (20, 95), 4: (40, 180), 5: (60, 240)}[level]
        arrived = start + timedelta(minutes=minute)
        seen = arrived + timedelta(minutes=rng.randint(low, high))
        admitted = rng.random() < {1: .95, 2: .60, 3: .28, 4: .07, 5: .02}[level]
        rows.append({
            "visit_id": f"V{i:04d}",
            "arrived_at": arrived.isoformat(timespec="minutes"),
            "seen_at": seen.isoformat(timespec="minutes"),
            "arrival_route": route, "sex": pick(rng, ["F", "M"], [52, 48]),
            "age_years": age, "triage_level": level, "pain": pain,
            "temp_c": f"{temp:.1f}", "heart_rate": hr,
            "prior_visits": prior, "admitted": "yes" if admitted else "no"})
    # Missing observations: three low-acuity visits left before being seen,
    # four temperatures were not recorded.
    low_acuity = [r for r in rows if r["triage_level"] >= 4 and r["admitted"] == "no"]
    for r in rng.sample(low_acuity, 3):
        r["seen_at"] = ""
    for r in rng.sample(rows, 4):
        r["temp_c"] = ""
    return rows


def make_check_file(rows):
    sample = [dict(r) for r in rows[:12]]
    sample[3]["triage_level"] = 6      # not a level of the scale
    sample[7]["age_years"] = 430       # typing error
    sample[9]["temp_c"] = ""           # not recorded
    return sample


def write(path, rows):
    with open(path, "w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    log = make_log()
    write(output_dir / "triage.csv", log)
    write(output_dir / "triage_check.csv", make_check_file(log))
    return log


if __name__ == "__main__":
    log = generate()
    print(len(log), "visits written")

"""Generate the synthetic March 2026 triage log (seed 60, day seeds 101-131).
The variables follow Chapter 3. These are newly generated visits, not copies
of its March 9 records. No length-of-stay variable is generated.
"""
import csv, json, random
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
FIELDS = ["visit_id", "date", "arrived_at", "seen_at", "arrival_route", "sex", "age_years",
          "triage_level", "pain", "temp_c", "heart_rate", "prior_visits", "admitted"]
PAIN = ["none", "mild", "moderate", "severe"]

def pick(rng, values, weights):
    return rng.choices(values, weights=weights, k=1)[0]

def make_day(day, seed, n):
    rng = random.Random(seed)
    start = datetime(2026, 3, day, 0, 0)
    minutes = sorted(rng.randrange(0, 24 * 60) for _ in range(n))
    rows = []
    for minute in minutes:
        level = pick(rng, [1, 2, 3, 4, 5], [2, 12, 40, 34, 12])
        route = pick(rng, [1, 2, 3], {1: [20, 70, 10], 2: [45, 45, 10]}.get(level, [80, 12, 8]))
        age = min(95, max(18, int(rng.gauss(52, 19))))
        fever = rng.random() < (0.30 if level <= 3 else 0.12)
        temp = round(rng.uniform(38.0, 40.2) if fever else rng.uniform(36.0, 37.6), 1)
        hr = int(rng.gauss(84 + (14 if fever else 0) + (6 - level) * 3, 12))
        pain = pick(rng, PAIN, [15, 30, 35, 20] if level <= 3 else [30, 40, 22, 8])
        prior = pick(rng, [0, 1, 2, 3, 4, 5, 6], [45, 25, 13, 8, 5, 3, 1])
        low, high = {1: (0, 5), 2: (5, 25), 3: (20, 95), 4: (40, 180), 5: (60, 240)}[level]
        arrived = start + timedelta(minutes=minute)
        seen = arrived + timedelta(minutes=rng.randint(low, high))
        # admission depends on level and rises with age
        p_adm = {1: .95, 2: .60, 3: .28, 4: .07, 5: .02}[level] * (1.35 if age >= 65 else 1.0)
        admitted = rng.random() < min(p_adm, .98)
        rows.append({"date": start.date().isoformat(),
                     "arrived_at": arrived.isoformat(timespec="minutes"),
                     "seen_at": seen.isoformat(timespec="minutes"),
                     "arrival_route": route, "sex": pick(rng, ["F", "M"], [52, 48]),
                     "age_years": age, "triage_level": level, "pain": pain,
                     "temp_c": f"{temp:.1f}", "heart_rate": hr,
                     "prior_visits": prior, "admitted": "yes" if admitted else "no"})
    return rows

def make_month():
    rows = []
    rng = random.Random(60)
    for day in range(1, 32):
        n = rng.randint(30, 50) if day % 7 in (0, 6) else rng.randint(36, 46)
        rows += make_day(day, seed=100 + day, n=n)
    for i, r in enumerate(rows, 1):
        r["visit_id"] = f"M{i:04d}"
    return [{k: r[k] for k in FIELDS} for r in rows]

if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    rows = make_month()
    with open(DATA / "triage_month.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    print(len(rows), "visits")

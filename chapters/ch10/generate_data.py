"""Synthetic data for Chapter 10: ten hypertension clinics over 24 months, one table (clinic_patients.csv).

Timeline (months of enrollment):
  1-6    before: every clinic prescribes the separate tablets
  7-12   individual trial: each arriving adult is randomized to single pill or separate tablets
  13-24  rollout: five clinics (chosen by lot) offer the single pill from month 13, the other five from month 19
Outcome: blood pressure not controlled at the 12-week visit. Receipt of the single pill multiplies the
risk by 0.70 for the adult who takes it. Seed 33. Run: python3 generate_data.py
"""
import csv
import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLINICS = [f"C{i:02d}" for i in range(1, 11)]


def generate_data(output_dir=HERE / "data", seed=33):
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    clinic_effect = {c: rng.uniform(0.90, 1.10) for c in CLINICS}
    early = set(rng.sample(CLINICS, 5))
    rows = []
    pid = 0
    for month in range(1, 25):
        for c in CLINICS:
            for _ in range(rng.randint(22, 34)):
                pid += 1
                age = int(min(90, max(30, rng.gauss(61, 11))))
                diabetes = rng.random() < 0.25
                ckd = rng.random() < 0.14
                sbp = int(min(200, max(140, rng.gauss(157, 12))))
                if month <= 6:
                    offer = "separate tablets"; period = "before"
                elif month <= 12:
                    offer = rng.choice(["single pill", "separate tablets"]); period = "trial"
                else:
                    on = (c in early and month >= 13) or month >= 19
                    offer = "single pill" if on else "separate tablets"; period = "rollout"
                received = rng.random() < (0.92 if offer == "single pill" else 0.03)
                risk = (0.26 + 0.011 * (sbp - 150) + 0.05 * diabetes + 0.05 * ckd) * clinic_effect[c] * (0.986 ** month)
                if received:
                    risk *= 0.70
                risk = min(max(risk, 0.02), 0.95)
                rows.append({"patient_id": f"A{pid:05d}", "clinic": c, "month": month, "period": period,
                             "clinic_start_month": 13 if c in early else 19,
                             "diabetes": "yes" if diabetes else "no", "baseline_sbp": sbp,
                             "allocated": offer, "received": "yes" if received else "no",
                             "uncontrolled_12w": "yes" if rng.random() < risk else "no"})
    with open(out / "clinic_patients.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print("rows:", len(rows), "early clinics:", sorted(early))


if __name__ == "__main__":
    generate_data()

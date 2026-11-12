"""Generate the synthetic Chapter 11 register: 5,000 deliveries in one maternity unit.

One row is one delivery. All values are synthetic; no real patients.
Columns: delivery_id, age_years, gestational_diabetes, cesarean, hemorrhage,
readmission (within 42 days), return_to_theatre, stay_days, acidemia (cord
arterial pH below 7.10), monitor_alert (fetal-monitoring alert during labor).
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
        age = min(48, max(16, int(rng.gauss(29, 6))))
        gdm = rng.random() < 0.16
        cesarean = rng.random() < (0.38 if gdm else 0.28)
        p_h = 0.045 * (1.6 if cesarean else 1.0) * (1.5 if gdm else 1.0)
        hemorrhage = rng.random() < p_h
        # readmission depends strongly on hemorrhage; return to theatre on hemorrhage and cesarean
        p_r = 0.05 * (1.3 if cesarean else 1.0) * (1.4 if gdm else 1.0) * (8.0 if hemorrhage else 1.0)
        readmission = rng.random() < min(p_r, 0.95)
        p_t = 0.004 * (2.0 if cesarean else 1.0) * (30.0 if hemorrhage else 1.0)
        theatre = rng.random() < min(p_t, 0.95)
        stay = 1.5 + (1.8 if cesarean else 0.0) + (1.0 if gdm else 0.0) \
            + (2.0 if hemorrhage else 0.0) + (3.0 if theatre else 0.0)
        stay = max(1, round(stay + rng.gauss(1.0, 1.0)))
        acidemia = rng.random() < 0.05
        alert = (acidemia and rng.random() < 0.80) or ((not acidemia) and rng.random() < 0.10)
        # An alert keeps the mother in a bed for one more day (newborn observation),
        # whether or not acidemia is real. Added after the draws so that every
        # other column is unchanged.
        if alert:
            stay += 1
        rows.append({"delivery_id": f"D{i:04d}", "age_years": age,
                     "gestational_diabetes": yn(gdm), "cesarean": yn(cesarean),
                     "hemorrhage": yn(hemorrhage), "readmission": yn(readmission),
                     "return_to_theatre": yn(theatre), "stay_days": stay,
                     "acidemia": yn(acidemia), "monitor_alert": yn(alert)})
    with open(output_dir / "deliveries.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(len(rows), "deliveries written")


if __name__ == "__main__":
    generate()

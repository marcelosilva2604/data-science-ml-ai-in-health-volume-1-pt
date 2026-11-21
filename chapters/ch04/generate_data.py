"""Generate the Chapter 4 cohort: 300 adults admitted to one hospital in 2025 with community-acquired pneumonia.

data/cohort.csv: one row per patient, 11 columns (patient_id, admitted_on, sex, age_years, ward, severity, comorbidities, sbp_mmhg,
spo2_pct, crp_mg_l, los_days). Two long stays (62 and 47 days) are recorded correctly and kept. The distributions are constructed
for teaching and are not estimates for any real population. Seed 4. Run: python generate_data.py
"""
import math
import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd


def make_cohort(seed=4, n=300):
    rng = random.Random(seed)
    rows = []
    month_w = [14, 13, 10, 7, 5, 4, 4, 4, 6, 8, 11, 14]
    for i in range(1, n + 1):
        age = int(min(97, max(19, rng.gauss(69, 14))))
        sev = rng.choices(["low", "moderate", "high"],
                          weights=[40, 40, 20] if age < 70 else [22, 46, 32])[0]
        ward = rng.choices(["medicine", "respiratory", "geriatrics", "intensive care"],
                           weights={"low": [60, 28, 11, 1], "moderate": [48, 30, 18, 4],
                                    "high": [30, 25, 17, 28]}[sev])[0]
        comorb = rng.choices(range(7), weights=[14, 24, 25, 18, 11, 6, 2])[0]
        sbp = int(round(rng.gauss(126, 18)))
        spo2 = int(round(min(100, 100 - rng.gammavariate(2.2, 2.3))))
        crp = round(math.exp(rng.gauss(4.3, 0.85)), 0)
        base = {"low": 1.35, "moderate": 1.75, "high": 2.25}[sev]
        los = max(1, int(round(math.exp(rng.gauss(base, 0.62)))))
        month = rng.choices(range(1, 13), weights=month_w)[0]
        admitted = date(2025, month, 1) + timedelta(days=rng.randrange(28))
        rows.append({"patient_id": f"C{i:03d}", "admitted_on": admitted.isoformat(),
                     "sex": rng.choices(["F", "M"], weights=[46, 54])[0],
                     "age_years": age, "ward": ward, "severity": sev,
                     "comorbidities": comorb, "sbp_mmhg": sbp, "spo2_pct": spo2,
                     "crp_mg_l": int(crp), "los_days": los})
    # two long stays, recorded correctly (complicated courses), kept in the data
    rows[57]["los_days"], rows[211]["los_days"] = 62, 47
    return pd.DataFrame(rows)


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    df = make_cohort()
    df.to_csv(output_dir / "cohort.csv", index=False)
    return df


if __name__ == "__main__":
    print(len(generate()), "patients written")

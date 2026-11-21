"""Reproduce the original 2,400-row teaching cohort (seed 7).

SSI and complications are ascertained through 30 days from surgery.
Readmission observation begins at discharge and stops at first readmission or
an independently generated administrative cutoff, at most 90 days. Integer
days are rounded and floored at one day, retaining the original teaching data.
Random assignments here are a simulation recipe, not clinical efficacy evidence.
"""
import csv
import random
from pathlib import Path

random.seed(7)
N = 2400
rows = []
for i in range(1, N + 1):
    age = min(95, max(18, int(random.gauss(58, 15))))
    sex = random.choice(["F", "M"])
    diabetes = random.random() < 0.25
    smoker = random.random() < 0.30
    # Deliberately unequal surgery-class mixtures; no clinical scheduling mechanism is asserted.
    p_clean = 0.80 if smoker else 0.30
    surgery_class = "clean" if random.random() < p_clean else "contaminated"
    bundle = random.random() < 0.50   # decolonization bundle, independent of the rest
    # SSI risk: diabetes x2.5 on a base that depends on class, smoking and bundle
    base = 0.020 if surgery_class == "clean" else 0.080
    p_ssi = base * (2.5 if diabetes else 1.0) * (2.0 if smoker else 1.0) * (0.5 if bundle else 1.0)
    p_ssi = min(p_ssi, 0.95)
    ssi = random.random() < p_ssi
    # any 30-day complication: common outcome
    p_comp = 0.45 if diabetes else 0.25
    complication = ssi or (random.random() < p_comp)
    # 90-day readmission with censoring: exponential times, rate ratio 2 for diabetes
    rate = (0.0040 if diabetes else 0.0020)  # per day
    t_event = random.expovariate(rate)
    t_censor = 90 if random.random() < 0.80 else random.uniform(10, 90)
    if t_event <= t_censor:
        followup_days, readmitted = round(t_event), True
    else:
        followup_days, readmitted = round(t_censor), False
    followup_days = max(1, followup_days)
    rows.append({
        "patient_id": f"S{i:04d}", "age_years": age, "sex": sex,
        "diabetes": "yes" if diabetes else "no",
        "smoker": "yes" if smoker else "no",
        "surgery_class": surgery_class,
        "bundle": "yes" if bundle else "no",
        "ssi_30d": "yes" if ssi else "no",
        "complication_30d": "yes" if complication else "no",
        "followup_days": followup_days,
        "readmitted_90d": "yes" if readmitted else "no",
    })

output = Path(__file__).resolve().parent / "data/surgery_cohort.csv"
output.parent.mkdir(parents=True, exist_ok=True)
with output.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(len(rows), "patients written")

"""Regenerate the original synthetic data without changing its random sequence.

Chapter analyses are in chapter8.py. Regeneration is opt-in.
"""
from pathlib import Path
import csv
import random


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    rng_primary = random.Random(8)
    N = 24000
    HOSPITALS = [f"H{i:02d}" for i in range(1, 13)]
    # hospital case-mix (share of contaminated surgery) and month of bundle adoption
    contaminated_share = {h: 0.25 + 0.05 * i for i, h in enumerate(HOSPITALS)}   # 0.25 .. 0.80
    # hospitals with more contaminated surgery (more infections) adopted the bundle EARLIER
    adoption_month = {h: m for h, m in zip(HOSPITALS, [99, 99, 99, 21, 19, 17, 15, 13, 13, 11, 9, 7])}
    hospital_effect = {h: rng_primary.uniform(0.85, 1.15) for h in HOSPITALS}

    rows = []
    for i in range(1, N + 1):
        hospital = rng_primary.choice(HOSPITALS)
        month = rng_primary.randint(1, 24)
        age = min(95, max(18, int(rng_primary.gauss(58, 15))))
        sex = rng_primary.choice(["F", "M"])
        diabetes = rng_primary.random() < 0.25
        smoker = rng_primary.random() < 0.30
        # self-reported smoking: 20% of smokers deny, 2% of non-smokers affirm
        smoker_reported = (smoker and rng_primary.random() > 0.20) or ((not smoker) and rng_primary.random() < 0.02)
        contaminated = rng_primary.random() < contaminated_share[hospital]
        surgery_class = "contaminated" if contaminated else "clean"
        # bundle: only after the hospital adopted it; then given preferentially to high-risk patients
        if month >= adoption_month[hospital]:
            p_bundle = 0.85 if (contaminated or diabetes) else 0.35
        else:
            p_bundle = 0.0
        bundle = rng_primary.random() < p_bundle
        # registry documentation of the bundle: 12% of bundle recipients have the field blank
        bundle_recorded = ("yes" if bundle else "no") if (not bundle or rng_primary.random() > 0.12) else ""
        # TRUE 30-day SSI risk: base by class, x2.5 diabetes, x2 smoking, hospital effect,
        # secular decline of 0.8% per month, and the bundle halves it
        base = 0.030 if contaminated is False else 0.110
        p = base * (2.5 if diabetes else 1.0) * (2.0 if smoker else 1.0) * hospital_effect[hospital]
        p *= (1 - 0.008) ** (month - 1)
        if bundle:
            p *= 0.50
        ssi = rng_primary.random() < min(p, 0.95)
        # two wound assessors: sensitivity 0.85/0.80, specificity 0.97/0.98, errors independent conditional on true status
        a = (ssi and rng_primary.random() < 0.85) or ((not ssi) and rng_primary.random() < 0.03)
        b = (ssi and rng_primary.random() < 0.80) or ((not ssi) and rng_primary.random() < 0.02)
        # follow-up: infected patients WITHOUT the bundle are more often lost; no reason for loss is recorded
        p_lost = 0.05
        if ssi and not bundle:
            p_lost = 0.30
        elif ssi and bundle:
            p_lost = 0.08
        followup_complete = rng_primary.random() > p_lost
        los = max(1, int(rng_primary.lognormvariate(1.3 if not ssi else 2.2, 0.5)))
        rows.append({
            "patient_id": f"P{i:05d}", "hospital": hospital, "month": month,
            "age_years": age, "sex": sex,
            "diabetes": "yes" if diabetes else "no",
            "smoker": "yes" if smoker else "no",
            "smoker_reported": "yes" if smoker_reported else "no",
            "surgery_class": surgery_class,
            "bundle": "yes" if bundle else "no",
            "bundle_recorded": bundle_recorded,
            "ssi_30d": "yes" if ssi else "no",
            "ssi_assessor_a": "yes" if a else "no",
            "ssi_assessor_b": "yes" if b else "no",
            "followup_complete": "yes" if followup_complete else "no",
            "los_days": los,
        })

    with open(output_dir / "population.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open(output_dir / "hospitals.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["hospital", "contaminated_share", "bundle_adoption_month"])
        for h in HOSPITALS:
            w.writerow([h, round(contaminated_share[h], 2), adoption_month[h] if adoption_month[h] < 99 else ""])
    print(len(rows), "operations written")

    # --- Measurement sub-study (its own random stream, so the population above is unchanged) ---
    # 400 patients of the network had capillary blood glucose measured at admission by the
    # ward's point-of-care meter and, from the same sample, by the central laboratory.
    rng = random.Random(82)
    with open(output_dir / "glucose_pairs.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["patient_id", "glucose_lab", "glucose_meter"])
        for i in range(1, 401):
            lab = max(60, rng.gauss(118, 32))
            meter = lab + 6 + rng.gauss(0, 9)          # the meter reads 6 mg/dL high on average
            w.writerow([f"G{i:03d}", round(lab), round(meter)])
    print("400 glucose pairs written")


if __name__ == "__main__":
    generate()

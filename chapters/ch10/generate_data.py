"""Generate the synthetic Chapter 10 files (antihypertensive single-pill case).

Three files, all synthetic and independent of other chapters:
  trial.csv    individually randomized teaching trial, 1,200 adults at one hypertension clinic
  cluster.csv  practice-randomized teaching trial, 1,800 adults in 18 family practices
  monthly.csv  practice-month summary of a 24-month hypertension register
Outcome: blood pressure not controlled (>=140/90 mmHg) at the 12-week visit.
Nominal receipt probabilities in the patient trial are 90% (assigned to the single
pill) and 5% (assigned to the two-tablet regimen); realized proportions vary.
Taking the single pill multiplies each patient's risk of uncontrolled pressure by 0.70.
Seed 10. Running time: a few seconds.
"""
from pathlib import Path
import csv
import random

HERE = Path(__file__).resolve().parent
PRACTICES = [f"P{i:02d}" for i in range(1, 19)]


def generate_data(output_dir=HERE / "data"):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(10)
    # share of patients with a baseline systolic pressure of 160 mmHg or higher, by practice
    high_share = {p: 0.18 + 0.02 * i for i, p in enumerate(PRACTICES)}
    practice_effect = {p: rng.uniform(0.88, 1.12) for p in PRACTICES}

    def patient(practice, month, trend=0.992, effect=1.0):
        age = min(88, max(35, int(rng.gauss(62, 11))))
        diabetes = rng.random() < 0.25
        ckd = rng.random() < 0.15
        high = rng.random() < high_share[practice]
        sbp = rng.randint(160, 185) if high else rng.randint(140, 159)
        base = 0.62 if high else 0.36
        p = base * (1.30 if diabetes else 1.0) * (1.20 if ckd else 1.0) * effect
        p *= trend ** (month - 1)
        return age, diabetes, ckd, sbp, p

    def uncontrolled(p, received):
        if received:
            p *= 0.70
        return rng.random() < min(p, 0.95)

    def yn(x):
        return "yes" if x else "no"

    def group(sbp):
        return "stage 2 (160+)" if sbp >= 160 else "stage 1 (140-159)"

    # --- individually randomized trial, one hypertension clinic ---
    rows = []
    for i in range(1, 1201):
        age, diabetes, ckd, sbp, p = patient(rng.choice(PRACTICES), 25)
        allocated = rng.random() < 0.5
        received = (rng.random() > 0.10) if allocated else (rng.random() < 0.05)
        unc = uncontrolled(p, received)
        rows.append({"patient_id": f"T{i:04d}", "age_years": age,
                     "diabetes": yn(diabetes), "kidney_disease": yn(ckd),
                     "baseline_sbp": sbp, "sbp_group": group(sbp),
                     "allocated": "single pill" if allocated else "two tablets",
                     "received": yn(received), "uncontrolled_12w": yn(unc)})
    with open(output_dir / "trial.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    # --- practice-randomized trial: nine practices drawn by lot adopt single-pill-first prescribing ---
    pill_practices = set(rng.sample(PRACTICES, 9))
    rows = []
    for i in range(1, 1801):
        practice = rng.choice(PRACTICES)
        age, diabetes, ckd, sbp, p = patient(practice, 25, effect=practice_effect[practice])
        received = practice in pill_practices
        unc = uncontrolled(p, received)
        rows.append({"patient_id": f"C{i:04d}", "practice": practice,
                     "age_years": age, "diabetes": yn(diabetes), "kidney_disease": yn(ckd),
                     "baseline_sbp": sbp, "sbp_group": group(sbp),
                     "arm": "single pill first" if received else "usual prescribing",
                     "uncontrolled_12w": yn(unc)})
    with open(output_dir / "cluster.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    # --- 24-month register, aggregated by practice and month ---
    # Register codes M01-M18 are a different set of practices from the trial codes P01-P18.
    # M18 adopts single-pill-first prescribing in month 7; M09 in month 13; others never.
    adopt = {"P18": 7, "P09": 13}
    counts = {}
    for practice in PRACTICES:
        for month in range(1, 25):
            n = rng.randint(80, 110)
            c = {"patients": n, "uncontrolled": 0, "single_pill": 0}
            for _ in range(n):
                age, diabetes, ckd, sbp, p = patient(practice, month, trend=0.985,
                                                      effect=practice_effect[practice])
                on = practice in adopt and month >= adopt[practice]
                received = on and (rng.random() < (0.90 if sbp >= 160 else 0.70))
                c["single_pill"] += received
                c["uncontrolled"] += uncontrolled(p, received)
            counts[(practice, month)] = c
    with open(output_dir / "monthly.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["practice", "month", "patients", "uncontrolled", "single_pill"])
        for (pr, m) in sorted(counts):
            c = counts[(pr, m)]
            w.writerow(["M" + pr[1:], m, c["patients"], c["uncontrolled"], c["single_pill"]])
    print("written; single-pill practices:", sorted(pill_practices))


if __name__ == "__main__":
    generate_data()

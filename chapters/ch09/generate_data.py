"""Chapter 9: synthetic data with a planted truth (seed 8).

Three files in data/:
  accuracy_cohort.csv   1,200 consecutive 30-day follow-up visits drawn from the
                        Chapter 8 surgical population, with a synthetic wound biomarker
                        (ng/mL), the rapid test read at the device cutoff of 30 ng/mL,
                        a clinical sign, the true infection status (reference standard),
                        the Chapter 8 assessor A as an imperfect reference, and a flag
                        for the partial-verification study.
  two_gate.csv          100 deep infections and 100 healthy volunteers (a two-gate,
                        case-control accuracy study of the same biomarker).
  screening_cohort.csv  10,000 women followed 20 years; preclinical onset, sojourn time,
                        clinical diagnosis, death, and screen detection under a biennial
                        program whose only effect is to move the date of diagnosis.
The accuracy cohort draws visits from the population of Chapter 8 (chapters/ch08/data/population.csv), so that file must exist to regenerate it.
Regeneration is opt-in. Seed 8. Run: python generate_data.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
OUT = HERE / "data"
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(8)

pop = pd.read_csv(HERE / "../ch08/data/population.csv")

# ---- 1. Accuracy cohort: consecutive follow-up visits, months 19-24, follow-up complete
elig = pop[(pop["month"] >= 19) & (pop["followup_complete"] == "yes")]
idx = rng.choice(elig.index.to_numpy(), size=1200, replace=False)
coh = elig.loc[np.sort(idx)].copy()
inf = (coh["ssi_30d"] == "yes").to_numpy()
# depth of infection among the infected: 30% deep or organ-space, 70% superficial
depth = np.where(inf, np.where(rng.random(len(coh)) < 0.30, "deep", "superficial"), "none")
# planted biomarker: log-normal, sd 0.6 on the log scale, means 2.8 / 3.7 / 4.4
mu = np.select([depth == "none", depth == "superficial", depth == "deep"], [2.8, 3.7, 4.4])
logm = rng.normal(mu, 0.6)
marker = np.round(np.exp(logm), 1)
# clinical sign (purulent discharge), more likely with a higher marker
p_sign = np.where(inf, 1 / (1 + np.exp(-(-4.0 + 1.2 * logm))), 1 / (1 + np.exp(-(-7.0 + 1.0 * logm))))
sign = rng.random(len(coh)) < p_sign
rapid = marker >= 30.0
# partial verification: every positive is verified; a 30% random sample of negatives
verified = rapid | (rng.random(len(coh)) < 0.30)
out = pd.DataFrame({
    "patient_id": coh["patient_id"].to_numpy(),
    "hospital": coh["hospital"].to_numpy(),
    "age_years": coh["age_years"].to_numpy(),
    "sex": coh["sex"].to_numpy(),
    "diabetes": coh["diabetes"].to_numpy(),
    "surgery_class": coh["surgery_class"].to_numpy(),
    "ssi": np.where(inf, "yes", "no"),
    "ssi_depth": depth,
    "assessor_a": coh["ssi_assessor_a"].to_numpy(),
    "marker_ng_ml": marker,
    "rapid_test": np.where(rapid, "positive", "negative"),
    "discharge_sign": np.where(sign, "yes", "no"),
    "verified": np.where(verified, "yes", "no"),
})
out.to_csv(OUT / "accuracy_cohort.csv", index=False)

# ---- 2. Two-gate study: deep infections from outside the cohort, healthy volunteers
others = pop[(pop["ssi_30d"] == "yes") & (~pop["patient_id"].isin(out["patient_id"]))]
cases = others.loc[np.sort(rng.choice(others.index.to_numpy(), size=100, replace=False))]
case_marker = np.round(np.exp(rng.normal(4.4, 0.6, 100)), 1)
ctrl_marker = np.round(np.exp(rng.normal(2.5, 0.5, 100)), 1)
tg = pd.DataFrame({
    "subject_id": list(cases["patient_id"]) + [f"V{i:03d}" for i in range(1, 101)],
    "group": ["deep infection"] * 100 + ["healthy volunteer"] * 100,
    "ssi": ["yes"] * 100 + ["no"] * 100,
    "marker_ng_ml": np.concatenate([case_marker, ctrl_marker]),
})
tg["rapid_test"] = np.where(tg["marker_ng_ml"] >= 30.0, "positive", "negative")
tg.to_csv(OUT / "two_gate.csv", index=False)

# ---- 3. Screening cohort: 10,000 women, 20 years, a program that only moves diagnosis
n = 10000
develops = rng.random(n) < 0.12
onset = np.where(develops, rng.uniform(0, 20, n), np.nan)
ttype = np.where(develops, np.where(rng.random(n) < 0.5, "slow", "fast"), "none")
sojourn = np.where(ttype == "slow", rng.exponential(4.0, n), rng.exponential(1.0, n))
sojourn = np.where(develops, sojourn, np.nan)
t_clin = onset + sojourn
surv = np.where(ttype == "slow", rng.exponential(12.0, n), rng.exponential(4.0, n))
t_death = t_clin + surv                     # unchanged by screening
# biennial screens at years 2, 4, ..., 20; sensitivity 0.85 per screen in the preclinical phase
t_screen = np.full(n, np.nan)
for s in np.arange(2.0, 20.1, 2.0):
    in_phase = develops & (onset <= s) & (s < t_clin) & np.isnan(t_screen)
    hit = in_phase & (rng.random(n) < 0.85)
    t_screen[hit] = s
sc = pd.DataFrame({
    "woman_id": np.arange(1, n + 1),
    "cancer": np.where(develops, "yes", "no"),
    "tumor_type": ttype,
    "t_onset": np.round(onset, 2),
    "t_clinical": np.round(t_clin, 2),
    "t_death": np.round(t_death, 2),
    "t_screen_detected": t_screen,
})
sc.to_csv(OUT / "screening_cohort.csv", index=False)
print(out["ssi"].value_counts().to_dict(), tg.shape, sc["cancer"].value_counts().to_dict())

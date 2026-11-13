"""Check the key numbers quoted in the Chapter 10 text against the data. Run: python tests/test_ch10.py"""
from pathlib import Path
import pandas as pd

d = pd.read_csv(Path(__file__).resolve().parents[1] / "chapters/ch10/data/clinic_patients.csv")
d["y"] = d["uncontrolled_12w"].eq("yes")
trial = d[d.period == "trial"]
roll = d[d.month.between(13, 18)]
early = d.clinic_start_month.eq(13)
def pooled(rows):
    return int(rows.y.sum()), len(rows)
sp, st = trial[trial.allocated == "single pill"], trial[trial.allocated == "separate tablets"]
risk = lambda e, lo, hi: d[e & d.month.between(lo, hi)].y.mean()
checks = {
    "rows": (len(d), 6744),
    "trial": (pooled(trial), (478, 1716)),
    "arms": (pooled(sp) + pooled(st), (199, 857, 279, 859)),
    "stage 2 baseline": ((int(sp.baseline_sbp.ge(160).sum()), int(st.baseline_sbp.ge(160).sum())), (341, 331)),
    "receipt": ((int((sp.received == "no").sum()), int((st.received == "yes").sum())), (75, 31)),
    "cluster arms": (pooled(roll[roll.allocated == "single pill"]) + pooled(roll[roll.allocated == "separate tablets"]), (179, 819, 236, 852)),
    "clinics per arm": (tuple(roll.groupby("allocated").clinic.nunique()), (5, 5)),
    "before-after, adopters": (pooled(d[early & d.month.between(1, 6)]) + pooled(d[early & d.month.between(13, 18)]), (311, 830, 179, 819)),
    "comparison clinics": (pooled(d[~early & d.month.between(1, 6)]) + pooled(d[~early & d.month.between(13, 18)]), (310, 868, 236, 852)),
    "stepped-wedge contrast": (round(100*((risk(~early, 19, 24)-risk(~early, 13, 18))-(risk(early, 19, 24)-risk(early, 13, 18))), 1), -4.3),
    "did": (round(100*((risk(early, 13, 18)-risk(early, 1, 6))-(risk(~early, 13, 18)-risk(~early, 1, 6))), 1), -7.6),
    "first adopter month": (pooled(d[early & d.month.eq(1)]), (54, 134)),
    "whole service": (pooled(d[d.month.between(1, 6)]) + pooled(d[d.month.between(19, 24)]), (621, 1698, 336, 1659)),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

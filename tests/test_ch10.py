"""Check the key numbers quoted in the Chapter 10 text against the data. Run: python tests/test_ch10.py"""
from pathlib import Path
import pandas as pd

D = Path(__file__).resolve().parents[1] / "chapters/ch10/data"
trial, cluster, monthly = (pd.read_csv(D / f"{n}.csv") for n in ["trial", "cluster", "monthly"])
yes = lambda s: s.eq("yes")
def pair(df, col, a, b):
    return (int(yes(df.loc[df[col].eq(a), "uncontrolled_12w"]).sum()), int(df[col].eq(a).sum()),
            int(yes(df.loc[df[col].eq(b), "uncontrolled_12w"]).sum()), int(df[col].eq(b).sum()))
def pooled(rows):
    return int(rows.uncontrolled.sum()), int(rows.patients.sum())
m18 = monthly[monthly.practice == "M18"]; m09 = monthly[monthly.practice == "M09"]
ctl = monthly[monthly.practice.isin(["M01", "M02", "M03"])]
checks = {
    "trial size and events": ((len(trial), int(yes(trial.uncontrolled_12w).sum())), (1200, 424)),
    "arms": (pair(trial, "allocated", "single pill", "two tablets"), (184, 596, 240, 604)),
    "stage 2 baseline": (tuple(int(trial[trial.allocated == a].baseline_sbp.ge(160).sum()) for a in ["single pill", "two tablets"]), (205, 223)),
    "cluster arms": (pair(cluster, "arm", "single pill first", "usual prescribing"), (271, 876, 395, 924)),
    "practices per arm": (tuple(cluster.groupby("arm").practice.nunique()), (9, 9)),
    "M18 before/after": (pooled(m18[m18.month < 7]) + pooled(m18[m18.month >= 7]), (298, 586, 533, 1693)),
    "comparison M01-M03": (pooled(ctl[ctl.month < 7]) + pooled(ctl[ctl.month >= 7]), (743, 1698, 1984, 5209)),
    "M09 before/after": (pooled(m09[m09.month < 13]) + pooled(m09[m09.month >= 13]), (501, 1069, 340, 1136)),
    "register halves": (pooled(monthly[monthly.month <= 12]) + pooled(monthly[monthly.month >= 13]), (9497, 20414, 7763, 20595)),
    "practice codes": ((sorted(cluster.practice.unique())[0], sorted(monthly.practice.unique())[0]), ("P01", "M01")),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

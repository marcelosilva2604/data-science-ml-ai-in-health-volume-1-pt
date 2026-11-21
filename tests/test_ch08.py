"""Check the key numbers quoted in the Chapter 8 text against the data. Run: python tests/test_ch08.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "chapters/ch08/data"
df = pd.read_csv(D / "population.csv", keep_default_na=False)
hosp = pd.read_csv(D / "hospitals.csv", keep_default_na=False)
g = pd.read_csv(D / "glucose_pairs.csv")
adopt = {r.hospital: (int(r.bundle_adoption_month) if r.bundle_adoption_month else 99) for r in hosp.itertuples()}
cohort = df[df["month"] >= df["hospital"].map(adopt)]
t = pd.crosstab(cohort["bundle"], cohort["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
diff = g["glucose_meter"] - g["glucose_lab"]
checks = {
    "population": ((len(df), round((df["ssi_30d"] == "yes").mean(), 4)), (24000, 0.1011)),
    "cohort": ((len(cohort), t.to_numpy().tolist()), (8240, [[444, 5463], [232, 2101]])),
    "risk ratio": (round((t.loc["yes", "yes"] / t.loc["yes"].sum()) / (t.loc["no", "yes"] / t.loc["no"].sum()), 2), 0.76),
    "complete follow-up": (int((cohort["followup_complete"] == "yes").sum()), 7736),
    "blank fields": (int((cohort["bundle_recorded"] == "").sum()), 745),
    "glucose": ((round(diff.mean(), 1), round(diff.std(), 1)), (6.6, 8.7)),
}


def same(a, b):
    try:
        return bool(np.allclose(np.array(a, dtype=float), np.array(b, dtype=float)))
    except (TypeError, ValueError):
        return a == b


bad = {k: v for k, v in checks.items() if not same(v[0], v[1])}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["24000", "0.1011", "H04", "21", "26.2", "9.8", "0.72", "8240", "444 5463 232 2101", "0.76", "0.36", "0.45", "0.49", "0.44", "7736", "406 5185 152 1993", "1.02", "0.345", "0.086", "676", "444 969 232 383", "444 337 232 1015", "5.76", "745", "0.126", "0.81", "2.06", "1.81", "16232", "1557", "5854", "0.8", "1721", "1009", "703", "20567", "0.929", "0.808", "0.63", "0.863", "0.971", "0.96", "6.6", "8.7", "-10.5", "23.6", "0.35", "2.52", "1.18", "0.99", "0.79", "0.83", "0.61", "0.85", "0.54", "0.74", "7988", "0.89", "46.6", "29.5", "63.6"]
for name in ("ch08_observational_designs_en.ipynb", "ch08_delineamentos_observacionais_pt.ipynb"):
    path = ROOT / "chapters/ch08" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

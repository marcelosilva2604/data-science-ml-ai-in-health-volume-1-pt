"""Check the key numbers quoted in the Chapter 7 text against the data. Run: python tests/test_ch07.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "chapters/ch07/data/surgery_cohort.csv")
t = pd.crosstab(df["diabetes"], df["ssi_30d"]).reindex(index=["yes", "no"], columns=["yes", "no"])
p1, p0 = t.loc["yes", "yes"] / t.loc["yes"].sum(), t.loc["no", "yes"] / t.loc["no"].sum()
b = pd.crosstab(df["bundle"], df["ssi_30d"]).reindex(index=["yes", "no"], columns=["yes", "no"])
checks = {
    "rows": (len(df), 2400),
    "diabetes table": (t.to_numpy().tolist(), [[81, 519], [111, 1689]]),
    "risks": ((round(p1, 4), round(p0, 4), round(p1 / p0, 3)), (0.135, 0.0617, 2.189)),
    "odds ratio": (round((81 * 1689) / (519 * 111), 3), 2.375),
    "bundle table": (b.to_numpy().tolist(), [[67, 1147], [125, 1061]]),
    "bundle risks": ((round(67 / 1214, 4), round(125 / 1186, 4)), (0.0552, 0.1054)),
    "readmissions": ((int(df.loc[df["diabetes"] == "yes", "readmitted_90d"].eq("yes").sum()), int(df.loc[df["diabetes"] == "yes", "followup_days"].sum())), (153, 40615)),
}


def same(a, c):
    try:
        return bool(np.allclose(np.array(a, dtype=float), np.array(c, dtype=float)))
    except (TypeError, ValueError):
        return a == c


bad = {k: v for k, v in checks.items() if not same(v[0], v[1])}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["81", "519", "111", "1689", "0.135", "0.0617", "0.0733", "7.33", "73.3", "2.189", "118.9", "67 1147 125 1061", "0.524", "47.6", "2.0", "2.375", "1.847", "2.882", "153", "40615", "3.77", "253", "136144", "1.86", "2.027", "0.0502", "20", "105", "100", "37", "44", "54.3", "22.9", "32 570 10 458", "2.49", "29 128 121 1052", "1.79", "5.6", "11.0", "12.2", "8.0", "81 179 111 589", "2.401", "0.312", "0.159", "7.53", "8.48", "-0.953", "192", "90760", "214", "85999", "0.85", "2.129", "2.158", "43.2", "45.1", "81 98 111 286", "2.13", "0.453", "0.28"]
for name in ("ch07_association_and_impact_en.ipynb", "ch07_associacao_e_impacto_pt.ipynb"):
    path = ROOT / "chapters/ch07" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

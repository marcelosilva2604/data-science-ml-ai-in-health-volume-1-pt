"""Check the key numbers quoted in the Chapter 4 text against the data. Run: python tests/test_ch04.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "chapters/ch04/data/cohort.csv")
los = df["los_days"]
q1, q3 = los.quantile(0.25), los.quantile(0.75)
checks = {
    "shape": (df.shape, (300, 11)),
    "severity": (df["severity"].value_counts().reindex(["low", "moderate", "high"]).tolist(), [97, 129, 74]),
    "ward": (df["ward"].value_counts().tolist(), [136, 88, 49, 27]),
    "mean median": ((round(los.mean(), 2), los.median(), los.min(), los.max()), (7.75, 6.0, 1, 62)),
    "sd": (round(los.std(), 2), 7.40),
    "quartiles": ((q1, q3, q3 + 1.5 * (q3 - q1), int((los > q3 + 1.5 * (q3 - q1)).sum())), (3.0, 9.25, 18.625, 23)),
    "skew kurt": ((round(los.skew(), 2), round(los.kurt(), 2)), (3.16, 14.23)),
    "typo": (round(los.replace(62, 620).mean(), 2), 9.61),
    "age": ((round(df["age_years"].mean(), 1), round(df["age_years"].std(), 1)), (68.5, 13.8)),
    "sex": ((df["sex"] == "M").sum(), 166),
    "crp": ((round(df["crp_mg_l"].mean(), 1), df["crp_mg_l"].max(), round(df["crp_mg_l"].skew(), 2)), (108.7, 982, 3.34)),
}
def same(a, b):
    try:
        return bool(np.allclose(np.array(a, dtype=float), np.array(b, dtype=float)))
    except (TypeError, ValueError):
        return a == b


bad = {k: v for k, v in checks.items() if not same(v[0], v[1])}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["136", "49", "7.46", "7.98", "6.97", "11.37", "300", "11", "97", "129", "74", "32.33", "43.0", "24.67", "75.33", "8, 16, 53, 77, 79, 50, 17", "37.8", "61.0", "78.0", "89.0", "96.3", "148, 93, 32, 10, 5, 5", "5.8", "7.75", "8.44", "5.5", "9.61", "196", "39, 40, 32, 16, 7, 14, 8, 19, 13, 29, 33, 50", "24.0", "medicine", "133", "126.0", "7.75", "11.0", "9.25", "14.0", "6.25", "-6.375", "18.625", "28.0", "3.16", "-1.42", "-0.06", "14.23", "2.54", "-0.24", "68.5", "13.8", "126.1", "18.8", "95.2", "3.5", "108.7", "112.0", "982.0", "44.7", "55.3", "3.34", "268.875", "197", "74.1", "67.0", "183.5", "147.8", "45.3", "29.3", "16.3", "9.0"]
for name in ("ch04_describing_one_variable_en.ipynb", "ch04_descrevendo_uma_variavel_pt.ipynb"):
    path = ROOT / "chapters/ch04" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

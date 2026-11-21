"""Check the key numbers quoted in the Chapter 6 text against the data. Run: python tests/test_ch06.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "chapters/ch06/data/triage_month.csv")
observed = pd.crosstab(df["arrival_route"], df["admitted"])
chi2 = chi2_contingency(observed, correction=False)[0]
chi2_levels = chi2_contingency(pd.crosstab(df["triage_level"], df["admitted"]), correction=False)[0]
checks = {
    "rows": (len(df), 1263),
    "route by admission": (observed.to_numpy().tolist(), [[722, 199], [152, 81], [74, 35]]),
    "chi-square": ((round(chi2, 2), round((chi2 / len(df)) ** 0.5, 3), round(chi2_levels, 1), round((chi2_levels / len(df)) ** 0.5, 3)), (20.47, 0.127, 388.2, 0.554)),
    "heart rate temperature": ((round(df["heart_rate"].cov(df["temp_c"]), 2), round(df["heart_rate"].corr(df["temp_c"]), 3)), (6.25, 0.427)),
    "first eight": ((round(df.head(8)["heart_rate"].cov(df.head(8)["temp_c"]), 2), round(df.head(8)["heart_rate"].corr(df.head(8)["temp_c"]), 2)), (4.61, 0.18)),
    "age by admission": ((round(df.groupby("admitted")["age_years"].mean()["no"], 1), round(df.groupby("admitted")["age_years"].mean()["yes"], 1)), (51.7, 55.2)),
}


def same(a, b):
    try:
        return bool(np.allclose(np.array(a, dtype=float), np.array(b, dtype=float)))
    except (TypeError, ValueError):
        return a == b


bad = {k: v for k, v in checks.items() if not same(v[0], v[1])}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["1263", "722", "199", "921", "948", "315", "78.4", "21.6", "34.8", "32.1", "691.3", "20.47", "0.127", "388.2", "0.554", "0.871", "0.11867", "97.4", "2.6", "51.7", "55.2", "84.0", "93.0", "102.0", "87.5", "97.0", "107.5", "123, 76, 0, 1", "4.61", "6.25", "0.18", "0.427", "-0.47", "-0.25", "-0.27", "16.7", "33.1", "22.0", "0.132", "37.25", "37.47", "0.82", "-0.22", "-0.14", "11.25", "0.444", "0.5, 12.1, 42.3, 83.8"]
for name in ("ch06_describing_two_variables_en.ipynb", "ch06_descrevendo_duas_variaveis_pt.ipynb"):
    path = ROOT / "chapters/ch06" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

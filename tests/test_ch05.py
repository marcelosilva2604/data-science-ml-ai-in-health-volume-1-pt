"""Check the key numbers quoted in the Chapter 5 text against the data. Run: python tests/test_ch05.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "chapters/ch05/data"
cohort = pd.read_csv(D / "diabetes_cohort.csv", parse_dates=["entered", "exited"])
m = pd.read_csv(D / "mortality.csv")
cases = pd.read_csv(D / "surveillance.csv")
py = (cohort["exited"] - cohort["entered"]).dt.days.sum() / 365.25
rate_a, rate_b = m["deaths_a"] / m["population_a"], m["deaths_b"] / m["population_b"]
std = m["population_a"] + m["population_b"]
checks = {
    "cohort": ((len(cohort), int(cohort["diagnosed"].sum()), round(py, 1)), (1200, 31, 1135.8)),
    "incidence": ((round(100 * 31 / 1200, 2), round(1000 * 31 / py, 1)), (2.58, 27.3)),
    "cases": ((len(cases), int(cases["hospitalized"].sum()), int(cases["died"].sum())), (1000, 93, 3)),
    "deaths": ((int(m["deaths_a"].sum()), int(m["deaths_b"].sum())), (1512, 1859)),
    "crude": ((round(1000 * m["deaths_a"].sum() / m["population_a"].sum(), 2), round(1000 * m["deaths_b"].sum() / m["population_b"].sum(), 2)), (7.56, 12.39)),
    "standardized": ((round(1000 * (rate_a * std).sum() / std.sum(), 2), round(1000 * (rate_b * std).sum() / std.sum(), 2)), (10.39, 9.40)),
    "smr": (round(m["deaths_b"].sum() / (rate_a * m["population_b"]).sum(), 3), 0.875),
    "districts": ((int((cases["district"] == "north").sum()), int((cases["district"] == "south").sum())), (552, 448)),
}


def same(a, b):
    return bool(np.allclose(np.array(a, dtype=float), np.array(b, dtype=float)))


bad = {k: v for k, v in checks.items() if not same(v[0], v[1])}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["1200", "31", "1135.8", "2.58", "27.3", "104.0", "31.9", "25.0", "23.3", "7.56", "12.39", "10.39", "9.4", "1859", "2124", "0.875", "84.0", "7.5", "40.9", "501.8", "497.8", "3.9", "2.4", "7.16"]
for name in ("ch05_measures_of_frequency_en.ipynb", "ch05_medidas_de_frequencia_pt.ipynb"):
    path = ROOT / "chapters/ch05" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

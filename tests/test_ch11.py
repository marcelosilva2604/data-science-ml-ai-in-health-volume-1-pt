"""Check the key numbers quoted in the Chapter 11 notebook against the data. Run: python tests/test_ch11.py"""
import json
from math import comb
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "chapters/ch11/data/deliveries.csv")
C, H, I = (df[c].eq("yes") for c in ["cesarean", "hemorrhage", "infection"])
checks = {
    "rows": (len(df), 5000), "cesarean": (int(C.sum()), 1313), "hemorrhage": (int(H.sum()), 290), "infection": (int(I.sum()), 130),
    "H and I": (int((H & I).sum()), 19), "H or I": (int((H | I).sum()), 401), "neither": (int((~(H | I)).sum()), 4599),
    "I|C": ((int((I & C).sum()), int(C.sum())), (87, 1313)), "I|notC": ((int((I & ~C).sum()), int((~C).sum())), (43, 3687)),
    "C,H,I": ((int((C & H).sum()), int((C & H & I).sum())), (95, 14)),
    "running 10": (round(C.iloc[:10].mean(), 4), 0.5), "running 100": (round(C.iloc[:100].mean(), 4), 0.27),
    "P20": (round(1 - comb(4870, 20) / comb(5000, 20), 4), 0.4102),
    "min sample": (next(m for m in range(1, 5001) if 10 * comb(4870, m) <= comb(5000, m)), 87),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

# The executed notebook outputs must carry the numbers quoted in the book
expected = ["26.26%", "5.80%", "= 8.02%", "0.6692", "0.900950", "2,432,902,008,176,640,000", "0.0494", "0.0028", "0.4102"]
expected_pt = [e.replace(",", "") if e.startswith("2,") else e for e in expected]
for name, items in (("ch11_probability_en.ipynb", expected), ("ch11_probabilidade_pt.ipynb", expected_pt)):
    path = ROOT / "chapters/ch11" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [i for i in items if i not in text]
    assert not missing, (name, missing)
print("notebook outputs carry the expected numbers")

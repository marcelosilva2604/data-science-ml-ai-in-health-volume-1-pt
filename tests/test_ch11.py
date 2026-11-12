"""Check the key numbers quoted in the Chapter 11 notebook text against the data. Run: python tests/test_ch11.py"""
from math import comb
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).resolve().parents[1] / "chapters/ch11/data/deliveries.csv")
X = df.stay_days > 4
D, C, H, R, T, A, F = (df[c].eq("yes") for c in ["gestational_diabetes", "cesarean", "hemorrhage", "readmission", "return_to_theatre", "acidemia", "monitor_alert"])
E = H | R | T
base = df.stay_days - F.astype(int)
checks = {
    "long stays": (int(X.sum()), 1216), "P(X)": (round(X.mean(), 4), 0.2432),
    "X|D": ((int((X & D).sum()), int(D.sum())), (396, 809)), "X|notD": ((int((X & ~D).sum()), int((~D).sum())), (820, 4191)),
    "X|C": ((int((X & C).sum()), int(C.sum())), (851, 1499)), "X|notC": ((int((X & ~C).sum()), int((~C).sum())), (365, 3501)),
    "X|any": ((int((X & E).sum()), int(E.sum())), (335, 592)),
    "tree": ((int((A & F).sum()), int((A & ~F).sum()), int((~A & F).sum()), int((~A & ~F).sum())), (197, 47, 465, 4291)),
    "alerts": (int(F.sum()), 662), "extra beyond 4": (int(((df.stay_days - 4).clip(lower=0) - (base - 4).clip(lower=0)).sum()), 282),
    "cross": (int((F & (base <= 4) & X).sum()), 138), "bed-days": (int(df.stay_days.sum()), 17666),
    "mean": (round(df.stay_days.mean(), 2), 3.53), "H,R,T": ((int(H.sum()), int(R.sum()), int(T.sum())), (299, 398, 83)),
    "HD": (int((H & D).sum()), 72), "min traces": (next(n for n in range(1, 401) if 1 - comb(388, n) / comb(400, n) >= .9), 69),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

# The published result lines must carry the right numbers (EN and PT notebooks)
import json
nbdir = Path(__file__).resolve().parents[1] / "chapters/ch11"
expected = {"ch11_probability_en.ipynb": ["1,216 of 5,000", "0.1184", "396/809", "851/1,499", "335/592", "662 alerts", "465", "282", "138",
                                          "(1,499/5,000) × (114/1,499) × (29/114) = 29/5,000 = 0.0058", "69 traces", "17,666", "3.53"],
            "ch11_probabilidade_pt.ipynb": ["1.216 de 5.000", "0,1184", "396/809", "851/1.499", "335/592", "662 alertas", "465", "282", "138",
                                            "(1.499/5.000) × (114/1.499) × (29/114) = 29/5.000 = 0,0058", "69 traçados", "17.666", "3,53"]}
for name, items in expected.items():
    if not (nbdir / name).exists():
        continue
    text = " ".join("".join(c["source"]) for c in json.load(open(nbdir / name))["cells"] if c["cell_type"] == "markdown")
    missing = [i for i in items if i not in text]
    assert not missing, (name, missing)
print("notebook result lines carry the expected numbers")

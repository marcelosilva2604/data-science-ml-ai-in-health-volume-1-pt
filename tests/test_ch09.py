"""Check the key numbers quoted in the Chapter 9 text against the data. Run: python tests/test_ch09.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "chapters/ch09/data"
d = pd.read_csv(D / "accuracy_cohort.csv")
inf = d["ssi"] == "yes"
pos = d["rapid_test"] == "positive"
tp, fn, fp, tn = (pos & inf).sum(), (~pos & inf).sum(), (pos & ~inf).sum(), (~pos & ~inf).sum()
s = pd.read_csv(D / "screening_cohort.csv")
checks = {
    "rows": (len(d), 1200),
    "cells": ((tp, fp, fn, tn), (67, 193, 27, 913)),
    "sens spec": ((round(tp / (tp + fn), 3), round(tn / (tn + fp), 3)), (0.713, 0.825)),
    "predictive": ((round(tp / (tp + fp), 3), round(tn / (tn + fn), 3)), (0.258, 0.971)),
    "likelihood ratios": ((round((tp / (tp + fn)) / (1 - tn / (tn + fp)), 2), round((1 - tp / (tp + fn)) / (tn / (tn + fp)), 2)), (4.08, 0.35)),
    "auc": (round(roc_auc_score(inf.to_numpy(), d["marker_ng_ml"].to_numpy()), 3), 0.876),
    "screening": (len(s), 10000),
}


def same(a, b):
    try:
        return bool(np.allclose(np.array(a, dtype=float), np.array(b, dtype=float)))
    except (TypeError, ValueError):
        return a == b


bad = {k: v for k, v in checks.items() if not same(v[0], v[1])}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["67", "193", "27", "913", "0.713", "0.825", "0.258", "0.971", "0.614", "0.794", "0.802", "0.847", "0.208", "0.314", "0.959", "0.98", "0.04", "0.996", "0.112", "0.989", "0.505", "0.92", "0.731", "0.812", "4.08", "0.35", "0.18", "0.88", "5.8", "39.22", "78", "56", "161", "0.257", "0.029", "0.768", "0.015", "0.636", "0.13", "60.5", "55.2", "59.9", "115.2", "97", "129", "0.48", "506.6", "568", "18.9", "0.413", "0.564", "0.95", "0.372", "0.984", "315", "0.876", "0.0235", "0.83", "0.922", "27.7", "75.6", "289.5", "359", "0.522", "0.798", "0.734", "0.606", "0.927", "0.861", "0.789", "0.933", "0.882", "0.821", "0.943", "136.1", "1142", "202.8", "231", "2284", "820", "2.96", "0.659", "0.378", "688", "0.333", "0.077"]
for name in ("ch09_diagnostic_tests_en.ipynb", "ch09_testes_diagnosticos_pt.ipynb"):
    path = ROOT / "chapters/ch09" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

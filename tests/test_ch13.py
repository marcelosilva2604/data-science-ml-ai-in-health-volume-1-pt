"""Check the key numbers quoted in the Chapter 13 text against the data. Run: python tests/test_ch13.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from math import sqrt
from scipy import stats

d = pd.read_csv(Path(__file__).resolve().parents[1] / "chapters/ch13/data/schoolchildren.csv")
y = d.dmft.values; N = len(y); mu = y.mean(); sigma = y.std(ddof=0)
srs = d.sample(n=600, random_state=13); x = srs.dmft.values
pri = d.school_type.eq("private").values
checks = {
    "rows": (N, 14299), "schools": (d.school.nunique(), 48),
    "mean sd": ((round(mu, 3), round(sigma, 3)), (1.870, 2.389)), "free": ((int((y == 0).sum()), round(100 * (y == 0).mean(), 1)), (5109, 35.7)),
    "types": ((int(pri.sum()), int((~pri).sum()), round(y[pri].mean(), 2), round(y[~pri].mean(), 2)), (3448, 10851, 1.0, 2.15)),
    "convenience": ((round(y[:600].mean(), 3), round(100 * (y[:600] == 0).mean(), 1)), (1.295, 44.0)),
    "srs": ((round(x.mean(), 3), round(x.std(ddof=1), 3), round(x.std(ddof=1) / sqrt(600), 4)), (1.847, 2.373, 0.0969)),
    "t interval": ((round(x.mean() - stats.t.ppf(.975, 599) * x.std(ddof=1) / sqrt(600), 3), round(x.mean() + stats.t.ppf(.975, 599) * x.std(ddof=1) / sqrt(600), 3)), (1.656, 2.037)),
    "shares": ((int((x == 0).sum()), int((x >= 8).sum())), (229, 27)),
    "fpc": (round(sqrt((N - 600) / (N - 1)), 3), 0.979),
    "sample size": ((round((1.959964 * sigma / .15) ** 2, 1),), (974.0,)),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["1.847", "0.0969", "1.656", "2.037", "229", "0.0934", "0.0912", "0.1123", "974.0", "527.7", "1.295", "1.718", "2.12", "0.84", "2.63", "1.72", "2.04", "1.82", "1.95", "0.19", "0.08", "455.3", "144.7", "0.0934", "87.5", "97.3", "975", "933", "892", "876", "838", "0.145"]
for name in ("ch13_sampling_estimation_en.ipynb", "ch13_amostragem_estimacao_pt.ipynb"):
    path = Path(__file__).resolve().parents[1] / "chapters/ch13" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

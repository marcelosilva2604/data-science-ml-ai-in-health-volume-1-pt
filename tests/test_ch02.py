"""Check the key numbers quoted in the Chapter 2 text against the data. Run: python tests/test_ch02.py"""
from pathlib import Path
import csv
import json
import random
import statistics
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
with open(ROOT / "chapters/ch02/data/register.csv", newline="") as stream:
    population = list(csv.DictReader(stream))


def wait(row):
    return (datetime.fromisoformat(row["departed_at"]) - datetime.fromisoformat(row["formalized_at"])).total_seconds() / 3600


for row in population:
    row["w"] = wait(row)
delayed = lambda rows: sum(1 for r in rows if r["w"] > 2)
s1 = random.Random(11).sample(population, 120)
w1 = [r["w"] for r in s1]
inc = [dict(r) for r in s1]
known = inc[12:]
checks = {
    "rows": (len(population), 1200), "patients": (len({r["patient_id"] for r in population}), 1080),
    "register delayed": (delayed(population), 216), "sample 1 delayed": (delayed(s1), 24),
    "median longest": ((statistics.median(w1), max(w1)), (1.5, 8.0)),
    "two hours or more": (sum(1 for w in w1 if w >= 2), 45),
    "samples 17 and 42": ((delayed(random.Random(17).sample(population, 120)), delayed(random.Random(42).sample(population, 120))), (22, 18)),
    "incomplete": ((len(known), 120 - len(known), delayed(known)), (108, 12, 23)),
    "known share": (round(100 * delayed(known) / len(known), 1), 21.3),
    "range": ((round(100 * delayed(known) / 120, 1), round(100 * (delayed(known) + 12) / 120, 1)), (19.2, 29.2)),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["120", "24", "20.0", "1.5", "8.0", "45", "37.5", "216", "18.00", "22", "18.33", "18", "15.00", "108", "12", "23", "21.3", "19.2", "29.2", "150.0", "50.0"]
for name in ("ch02_populations_samples_data_en.ipynb", "ch02_populacoes_amostras_dados_pt.ipynb"):
    path = ROOT / "chapters/ch02" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

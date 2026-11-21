"""Check the key numbers quoted in the Chapter 3 text against the data. Run: python tests/test_ch03.py"""
from pathlib import Path
import csv
import json
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
with open(ROOT / "chapters/ch03/data/triage.csv", newline="") as stream:
    visits = list(csv.DictReader(stream))


def count(name, value):
    return sum(1 for r in visits if r[name] == value)


waits = [(datetime.fromisoformat(r["seen_at"]) - datetime.fromisoformat(r["arrived_at"])).total_seconds() / 60 for r in visits if r["seen_at"]]
temps = [float(r["temp_c"]) for r in visits if r["temp_c"]]
checks = {
    "rows": (len(visits), 200), "fields": (len(visits[0]), 12),
    "route": ((count("arrival_route", "1"), count("arrival_route", "2"), count("arrival_route", "3")), (155, 32, 13)),
    "levels": (tuple(count("triage_level", str(k)) for k in range(1, 6)), (5, 23, 85, 72, 15)),
    "pain": (tuple(count("pain", p) for p in ("none", "mild", "moderate", "severe")), (38, 80, 51, 31)),
    "sex admitted": ((count("sex", "F"), count("sex", "M"), count("admitted", "yes")), (102, 98, 54)),
    "route average": ((sum(int(r["arrival_route"]) for r in visits) / 200, sum({"1": 3, "2": 1, "3": 2}[r["arrival_route"]] for r in visits) / 200), (1.29, 2.615)),
    "level average": ((sum(int(r["triage_level"]) for r in visits) / 200, sum({"1": 1, "2": 2, "3": 4, "4": 8, "5": 16}[r["triage_level"]] for r in visits) / 200), (3.345, 6.035)),
    "waits": ((len(waits), sum(1 for r in visits if not r["seen_at"])), (197, 3)),
    "fever": ((len(temps), sum(1 for t in temps if t >= 38.0)), (196, 44)),
    "frequent": (sum(1 for r in visits if int(r["prior_visits"]) >= 3), 29),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["200", "12", "1.29", "2.615", "3.345", "6.035", "87.0", "25.0", "V0025", "V0050", "V0093", "37.6", "38.2", "40.0", "155", "32", "13", "102", "98", "54", "146", "44", "152", "5", "23", "85", "72", "15", "38", "80", "51", "31", "1.054", "1.037", "1.006", "98.6", "100.4", "102.2", "310.15", "311.15", "312.15", "430", "28", "14.0", "16.0", "27.0", "196", "22.4", "82", "41.0", "29", "14.5"]
for name in ("ch03_variables_scales_en.ipynb", "ch03_variaveis_escalas_pt.ipynb"):
    path = ROOT / "chapters/ch03" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

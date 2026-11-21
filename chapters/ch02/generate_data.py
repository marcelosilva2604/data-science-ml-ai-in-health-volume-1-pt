"""Generate the Chapter 2 register: the January discharges to home of a 500-bed hospital.

One row is one discharge episode (1,200 episodes, 1,080 distinct invented patients). Columns: episode_id, patient_id,
formalized_at (when the discharge was formalized), departed_at (when the patient left), delayed (True when the wait is more than 2 hours).
Synthetic teaching data: no patient data are used. No random numbers are involved: every episode is built from its row number.
Running time: under a second. Run: python generate_data.py
"""
from datetime import datetime, timedelta
from pathlib import Path
import csv

TARGET_HOURS = 2  # the audit's rule: delayed means MORE than 2 hours


def delay_status(row):
    """True or False from the documented times; missing times give None (never zero)."""
    if not row["formalized_at"] or not row["departed_at"]:
        return None
    formalized = datetime.fromisoformat(row["formalized_at"])
    departed = datetime.fromisoformat(row["departed_at"])
    hours = (departed - formalized).total_seconds() / 3600
    if hours < 0:
        raise ValueError("Departure precedes formalized discharge")
    return hours > TARGET_HOURS


def make_register():
    records = []
    for i in range(1200):
        number = i + 1
        patient = i % 1080 + 1
        day = 4 if i < 120 else 25 if i >= 1080 else i % 31 + 1
        formalized = datetime(2026, 1, day, 8) + timedelta(minutes=15 * (i % 4))
        hours = 5 + i % 4 if i % 50 < 9 else 0.5 * (1 + i % 4)
        departure = formalized + timedelta(hours=hours)
        records.append({
            "episode_id": f"A{number:04d}",
            "patient_id": f"P{patient:04d}",
            "formalized_at": formalized.isoformat(timespec="minutes"),
            "departed_at": departure.isoformat(timespec="minutes"),
            "delayed": None,
        })
        records[-1]["delayed"] = delay_status(records[-1])
    return records


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    register = make_register()
    with (output_dir / "register.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(register[0]))
        writer.writeheader()
        writer.writerows(register)
    return register


if __name__ == "__main__":
    register = generate()
    print(len(register), "episodes;", sum(r["delayed"] for r in register), "delayed")

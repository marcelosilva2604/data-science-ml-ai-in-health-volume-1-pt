"""Generate the Chapter 5 tables: a synthetic municipality of 200,000 inhabitants in 2025.

data/surveillance.csv: 1,000 residents with the disease under surveillance (one row per case). data/diabetes_cohort.csv: 1,200 adults followed
for incidence (one row per person: entry, exit, diagnosis). data/mortality.csv: deaths and population by age group in town A and in town B.
The other teaching counts of the chapter (vaccination, hospital) are stated in the text. All figures are synthetic and constructed for teaching;
none describes a real place. Seeds 5 and 51. Run: python generate_data.py
"""
import random
from datetime import date, timedelta
from pathlib import Path
import pandas as pd

rng = random.Random(5)

# --- population by age group (mid-year estimate), two districts
AGE = ["0-4", "5-14", "15-29", "30-44", "45-59", "60-74", "75+"]
pop_share = [0.062, 0.135, 0.235, 0.225, 0.180, 0.118, 0.045]
population = {a: round(200_000 * s) for a, s in zip(AGE, pop_share)}
population["0-4"] += 200_000 - sum(population.values())  # exact total
birth_cohort = 2_400            # children who turned one year old during 2025 (target for the 12-month vaccine)
doses_given = 2_496             # DTP doses (all dose numbers) recorded by the program in 2025, includes children from outside and duplicates
children_3_doses, children_2_doses = 600, 200     # resident children with exactly 3 and exactly 2 doses (the rest have 1; 3*600+2*200+97 = 2,297 valid doses)
doses_outside = 138             # residents of neighboring towns vaccinated here
doses_duplicate = 61            # second entries for the same child
survey_n, survey_vaccinated = 420, 98   # DTP3 coverage survey (equal-probability sample), 12-23 months, card or recall

# --- surveillance: one disease, 2025, line list
cases = []
month_w = [22, 30, 41, 36, 18, 8, 4, 3, 3, 5, 9, 14]
for i in range(1, 1_001):
    age = rng.choices(AGE, weights=[5, 12, 24, 22, 18, 13, 6])[0]
    month = rng.choices(range(1, 13), weights=month_w)[0]
    hosp = rng.random() < 0.09
    died = hosp and rng.random() < {"75+": .25, "60-74": .12}.get(age, .03)
    cases.append({"case_id": f"S{i:04d}", "month": month, "age_group": age,
                  "district": rng.choices(["north", "south"], weights=[55, 45])[0],
                  "hospitalized": hosp, "died": died})
cases = pd.DataFrame(cases)
# prevalence survey on 1 July: households, chronic condition (hypertension), adults 30+
prev_survey = {"adults_examined": 1_500, "hypertensive": 447}
# cohort for incidence: 1,200 adults 45+ without diabetes followed in primary care, person-years and new cases
cohort = {"n": 1_200, "new_cases": 31, "at_risk_start": 1_200, "lost": 96}
# outbreak: school, 480 pupils, 96 ill after lunch; households of 50 primary cases, 168 contacts, 39 secondary
outbreak = {"exposed": 480, "ill": 96, "primary": 50, "contacts": 168, "secondary": 39}
# deaths 2025 by age group (all causes) and by the disease
deaths_all = {"0-4": 18, "5-14": 6, "15-29": 41, "30-44": 78, "45-59": 196, "60-74": 402, "75+": 771}
# the same deaths in A by sex (teaching count; no random draw, so the tables below are unchanged)
deaths_by_sex = {"men": 812, "women": 700}
assert sum(deaths_by_sex.values()) == sum(deaths_all.values())
# comparison town B: 150,000 inhabitants, older
pop_b = {"0-4": 6_000, "5-14": 13_500, "15-29": 27_000, "30-44": 30_000, "45-59": 30_000, "60-74": 27_000, "75+": 16_500}
deaths_b = {"0-4": 15, "5-14": 6, "15-29": 33, "30-44": 68, "45-59": 187, "60-74": 486, "75+": 1_064}
# hospital: 300 beds, 2025
hospital = {"beds": 300, "days": 365, "occupied_bed_days": 91_980, "discharges_and_deaths": 12_264}

def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    cases.to_csv(output_dir / "surveillance.csv", index=False)
    # A separate stream keeps surveillance and follow-up independently reproducible.
    followup_rng = random.Random(51)
    diagnosed_ids = set(followup_rng.sample(range(1, 1201), 31))
    eligible = [i for i in range(1, 1201) if i not in diagnosed_ids]
    lost_ids = set(followup_rng.sample(eligible, 96))
    start, end = date(2025, 1, 1), date(2026, 1, 1)
    records = []
    for i in range(1, 1201):
        reason = "diagnosis" if i in diagnosed_ids else "lost" if i in lost_ids else "year_end"
        exit_date = start + timedelta(days=followup_rng.randint(20, 364)) if reason != "year_end" else end
        records.append({"person_id": f"D{i:04d}", "entered": start.isoformat(),
                        "exited": exit_date.isoformat(), "diagnosed": i in diagnosed_ids,
                        "exit_reason": reason})
    pd.DataFrame(records).to_csv(output_dir / "diabetes_cohort.csv", index=False)
    pd.DataFrame({"age_group": AGE, "population_a": [population[a] for a in AGE],
                  "deaths_a": [deaths_all[a] for a in AGE],
                  "population_b": [pop_b[a] for a in AGE], "deaths_b": [deaths_b[a] for a in AGE]}
                 ).to_csv(output_dir / "mortality.csv", index=False)


if __name__ == "__main__":
    generate()
    print("surveillance.csv, diabetes_cohort.csv, and mortality.csv written")

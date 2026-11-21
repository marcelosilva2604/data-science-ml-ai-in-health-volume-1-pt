"""All code cells of the Chapter 3 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions. Only the standard
library is used (csv, datetime). The cells are written once in English; the Portuguese cell is the same code with the comments and printed text
translated through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the log: every cell arrives as text, the age included", "# 1. Ler o registro: toda célula chega como texto, inclusive a idade"),
 ("The log has", "O arquivo tem"),
 ("records (one per visit) and", "registros (um por atendimento) e"),
 ("fields.", "campos."),
 ("Type of age_years as read:", "Tipo de age_years ao ler:"),
 ("# 2. The identifier distinguishes the records and finds any of them; it measures nothing", "# 2. O identificador distingue os registros e encontra qualquer um deles; ele não mede nada"),
 ("Distinct visit_id:", "visit_id distintos:"),
 ("# 3. The report's average: what the system did with the arrival route codes (two numberings of the same categories)", "# 3. A média do relatório: o que o sistema fez com os códigos da via de chegada (duas numerações das mesmas categorias)"),
 ("Average route with the numbering", "Média da via com a numeração"),
 ("# 4. The same for triage level, which is ordinal: the order is kept, the spacing changes", "# 4. O mesmo para o nível de triagem, que é ordinal: a ordem é mantida, o espaçamento muda"),
 ("Average level with the spacing", "Média do nível com o espaçamento"),
 ("# 5. Derived variables: time to be seen (minutes) and fever; a visit with no time seen left before being seen", "# 5. Variáveis derivadas: tempo até ser atendido (minutos) e febre; um atendimento sem horário de atendimento é de quem saiu antes de ser atendido"),
 ("Time to be seen, V0001:", "Tempo até ser atendido, V0001:"),
 ("\"minutes; V0002:\"", "\"minutos; V0002:\""),
 ("\"minutes\")", "\"minutos\")"),
 ("Left before being seen:", "Saíram antes de ser atendidos:"),
 ("\"visits\"", "\"atendimentos\""),
 ("\"Visit\"", "\"Atendimento\""),
 ("\"- temperature\"", "\"- temperatura\""),
 ("\"- fever:\"", "\"- febre:\""),
 ("# 6. The scale of each variable decides the summary: counts for categories", "# 6. A escala de cada variável decide o resumo: contagens para categorias"),
 ("# The counts of the nominal and ordinal variables, in the order of the scale (missing values are counted apart)", "# As contagens das variáveis nominais e ordinais, na ordem da escala (valores faltantes são contados à parte)"),
 ("Counts of", "Contagens de"),
 ("# 7. Interval and ratio: the same three temperatures in three units, and the same two ages in two units", "# 7. Intervalar e razão: as mesmas três temperaturas em três unidades e as mesmas duas idades em duas unidades"),
 ("- ratio of the last to the first:", "- razão do último para o primeiro:"),
 ("Age ratio, 80 years against 40 years:", "Razão de idades, 80 anos contra 40 anos:"),
 ("\"; in months:\"", "\"; em meses:\""),
 ("# 8. The dictionary's rules, applied to a small file typed by hand", "# 8. As regras do dicionário, aplicadas a um arquivo pequeno digitado à mão"),
 ("\"missing\"", "\"faltante\""),
 ("\"identifier\"", "\"identificador\""),
 ("\"interval\"", "\"intervalar\""),
 ("\"ratio\"", "\"razão\""),
 ("not allowed:", "não permitido:"),
 ("For review:", "Para revisão:"),
 ("V0004 triage level after validation:", "Nível de triagem de V0004 após a validação:"),
 ("# 9. The summaries that the next section reports", "# 9. Os resumos que a próxima seção relata"),
 ("Triage levels 1 and 2:", "Níveis de triagem 1 e 2:"),
 ("Direct ambulance:", "Ambulância direta:"),
 ("Admitted:", "Internados:"),
 ("\"of\"", "\"de\""),
 ("\"visits =\"", "\"atendimentos =\""),
 ("Fever:", "Febre:"),
 ("\"visits with a recorded temperature =\"", "\"atendimentos com temperatura registrada =\""),
 ("# 1. Count the pain categories in the order of the scale and the visits of patients with three or more prior visits", "# 1. Contar as categorias de dor na ordem da escala e os atendimentos de pacientes com três ou mais atendimentos anteriores"),
 ("Pain counts:", "Contagens de dor:"),
 ("# 2. The two proportions", "# 2. As duas proporções"),
 ("At least moderate pain:", "Dor pelo menos moderada:"),
 ("Three or more visits in the preceding 12 months:", "Três ou mais atendimentos nos 12 meses anteriores:"),
 ("# 1. The rule for heart rate: limits that trigger review (plausibility limits, not the boundaries of possible heart rates)", "# 1. A regra para a frequência cardíaca: limites que acionam revisão (limites de plausibilidade, não as fronteiras das frequências possíveis)"),
 ("\"convert\"", "\"converter\""),
 ("\"low\"", "\"minimo\""),
 ("\"high\"", "\"maximo\""),
 ("# 2. Apply it to the 200 records", "# 2. Aplicá-la aos 200 registros"),
 ("Missing heart rates:", "Frequências cardíacas faltantes:"),
 ("Heart rates not allowed:", "Frequências cardíacas não permitidas:"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


LOAD = '''# 1. Read the log: every cell arrives as text, the age included
import csv
from datetime import datetime

with open("data/triage.csv", newline="") as stream:
    visits = list(csv.DictReader(stream))
print("The log has", len(visits), "records (one per visit) and", len(visits[0]), "fields.")
print("Type of age_years as read:", type(visits[0]["age_years"]).__name__)

# 2. The identifier distinguishes the records and finds any of them; it measures nothing
by_id = {}
for row in visits:
    by_id[row["visit_id"]] = row
print("Distinct visit_id:", len(by_id))
'''

AVG = '''# 3. The report's average: what the system did with the arrival route codes (two numberings of the same categories)
route_a = {"1": 1, "2": 2, "3": 3}
route_b = {"1": 3, "2": 1, "3": 2}
total_a = 0
total_b = 0
for row in visits:
    total_a = total_a + route_a[row["arrival_route"]]
    total_b = total_b + route_b[row["arrival_route"]]
print("Average route with the numbering 1-2-3:", total_a / len(visits))
print("Average route with the numbering 3-1-2:", total_b / len(visits))

# 4. The same for triage level, which is ordinal: the order is kept, the spacing changes
level_a = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
level_b = {"1": 1, "2": 2, "3": 4, "4": 8, "5": 16}
total_a = 0
total_b = 0
for row in visits:
    total_a = total_a + level_a[row["triage_level"]]
    total_b = total_b + level_b[row["triage_level"]]
print("Average level with the spacing 1-2-3-4-5:", total_a / len(visits))
print("Average level with the spacing 1-2-4-8-16:", total_b / len(visits))
'''

DERIVED = '''# 5. Derived variables: time to be seen (minutes) and fever; a visit with no time seen left before being seen
for row in visits:
    row["wait_min"] = None
    if row["seen_at"] != "":
        arrived = datetime.fromisoformat(row["arrived_at"])
        seen = datetime.fromisoformat(row["seen_at"])
        row["wait_min"] = (seen - arrived).total_seconds() / 60
    row["fever"] = None
    if row["temp_c"] != "":
        if float(row["temp_c"]) >= 38.0:
            row["fever"] = "yes"
        else:
            row["fever"] = "no"
print("Time to be seen, V0001:", by_id["V0001"]["wait_min"], "minutes; V0002:", by_id["V0002"]["wait_min"], "minutes")
left = []
for row in visits:
    if row["wait_min"] is None:
        left.append(row["visit_id"])
print("Left before being seen:", len(left), "visits", left)
for visit_id in ["V0074", "V0026", "V0174"]:
    print("Visit", visit_id, "- temperature", by_id[visit_id]["temp_c"], "- fever:", by_id[visit_id]["fever"])
'''

SCALES = '''# 6. The scale of each variable decides the summary: counts for categories
SCALE = {"visit_id": "identifier", "arrival_route": "nominal", "sex": "nominal",
         "admitted": "nominal", "fever": "nominal", "triage_level": "ordinal",
         "pain": "ordinal", "arrived_at": "interval", "seen_at": "interval",
         "temp_c": "interval", "age_years": "ratio", "heart_rate": "ratio",
         "prior_visits": "ratio", "wait_min": "ratio"}
for scale in ["identifier", "nominal", "ordinal", "interval", "ratio"]:
    names = []
    for name in SCALE:
        if SCALE[name] == scale:
            names.append(name)
    print(scale + ":", ", ".join(names))

# The counts of the nominal and ordinal variables, in the order of the scale (missing values are counted apart)
ORDER = {"arrival_route": ["1", "2", "3"], "sex": ["F", "M"],
         "admitted": ["yes", "no"], "fever": ["yes", "no"],
         "triage_level": ["1", "2", "3", "4", "5"],
         "pain": ["none", "mild", "moderate", "severe"]}
for variable in SCALE:
    if SCALE[variable] in ("nominal", "ordinal"):
        counts = {}
        for value in ORDER[variable]:
            counts[value] = 0
        counts["missing"] = 0
        for row in visits:
            value = row[variable]
            if value is None or value == "":
                value = "missing"
            counts[value] = counts[value] + 1
        shown = {}
        for value in counts:
            if counts[value] > 0:
                shown[value] = counts[value]
        print("Counts of", variable, "(" + SCALE[variable] + "):", shown)
'''

INTERVAL = '''# 7. Interval and ratio: the same three temperatures in three units, and the same two ages in two units
celsius = [37.0, 38.0, 39.0]
fahrenheit = []
kelvin = []
for c in celsius:
    fahrenheit.append(round(1.8 * c + 32, 1))
    kelvin.append(round(c + 273.15, 2))
print("Celsius", celsius, "- ratio of the last to the first:", round(celsius[2] / celsius[0], 3))
print("Fahrenheit", fahrenheit, "- ratio of the last to the first:", round(fahrenheit[2] / fahrenheit[0], 3))
print("Kelvin", kelvin, "- ratio of the last to the first:", round(kelvin[2] / kelvin[0], 3))
print("Age ratio, 80 years against 40 years:", 80 / 40, "; in months:", (80 * 12) / (40 * 12))
'''

VALID = '''# 8. The dictionary's rules, applied to a small file typed by hand
rules = {
    "age_years": {"convert": int, "low": 18, "high": 110},
    "triage_level": {"convert": int, "low": 1, "high": 5},
    "temp_c": {"convert": float, "low": 30.0, "high": 43.0},
}
with open("data/triage_check.csv", newline="") as stream:
    check = list(csv.DictReader(stream))

validated = []
issues = []
for row in check:
    clean = {"visit_id": row["visit_id"]}
    for name in rules:
        rule = rules[name]
        text = row[name]
        clean[name] = None
        if text == "":
            print(row["visit_id"], name, "missing")
        else:
            value = rule["convert"](text)
            if rule["low"] <= value <= rule["high"]:
                clean[name] = value
            else:
                issues.append((row["visit_id"], name, text))
                print(row["visit_id"], name, "not allowed:", value)
    validated.append(clean)
print("For review:", issues)
checked = {}
for record in validated:
    checked[record["visit_id"]] = record
print("V0004 triage level after validation:", checked["V0004"]["triage_level"])
'''

SUMMARY = '''# 9. The summaries that the next section reports
n = len(visits)
urgent = 0
ambulance = 0
admitted = 0
fever_yes = 0
fever_no = 0
for row in visits:
    if row["triage_level"] == "1" or row["triage_level"] == "2":
        urgent = urgent + 1
    if row["arrival_route"] == "2":
        ambulance = ambulance + 1
    if row["admitted"] == "yes":
        admitted = admitted + 1
    if row["fever"] == "yes":
        fever_yes = fever_yes + 1
    if row["fever"] == "no":
        fever_no = fever_no + 1
known = fever_yes + fever_no
print("Triage levels 1 and 2:", urgent, "of", n, "visits =", round(100 * urgent / n, 1), "%")
print("Direct ambulance:", ambulance, "of", n, "visits =", round(100 * ambulance / n, 1), "%")
print("Admitted:", admitted, "of", n, "visits =", round(100 * admitted / n, 1), "%")
print("Fever:", fever_yes, "of", known, "visits with a recorded temperature =", round(100 * fever_yes / known, 1), "%")
'''

EX12 = '''# 1. Count the pain categories in the order of the scale and the visits of patients with three or more prior visits
order = ["none", "mild", "moderate", "severe"]
pain_counts = {}
for category in order:
    pain_counts[category] = 0
frequent = 0
for row in visits:
    pain_counts[row["pain"]] = pain_counts[row["pain"]] + 1
    if int(row["prior_visits"]) >= 3:
        frequent = frequent + 1
print("Pain counts:", pain_counts)

# 2. The two proportions
at_least_moderate = pain_counts["moderate"] + pain_counts["severe"]
print("At least moderate pain:", at_least_moderate, "of", len(visits), "visits =", round(100 * at_least_moderate / len(visits), 1), "%")
print("Three or more visits in the preceding 12 months:", frequent, "of", len(visits), "visits =", round(100 * frequent / len(visits), 1), "%")
'''

EX13 = '''# 1. The rule for heart rate: limits that trigger review (plausibility limits, not the boundaries of possible heart rates)
rule = {"convert": int, "low": 30, "high": 220}

# 2. Apply it to the 200 records
missing = 0
flagged = []
for row in visits:
    text = row["heart_rate"]
    if text == "":
        missing = missing + 1
    else:
        value = rule["convert"](text)
        if not (rule["low"] <= value <= rule["high"]):
            flagged.append(row["visit_id"])
print("Missing heart rates:", missing)
print("Heart rates not allowed:", len(flagged))
'''


def cells(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    code = lambda c: c if en else tr(c)
    S = []

    def sec(num, title_en, title_pt, q_en=None, q_pt=None):
        S.append(("md", "### " + num + " " + T(title_en, title_pt) + (("\n\n*" + T(q_en, q_pt) + "*") if q_en else "")))

    def cell(c):
        S.append(("code", code(c)))

    sec("3.1", "Introduction: the data", "Introdução: os dados")
    cell(LOAD)
    sec("3.7", "The triage log and its dictionary", "O registro de triagem e seu dicionário",
        "What does the report's average of codes mean, and how is each variable's scale recorded so that a program can apply it?",
        "O que significa a média de códigos do relatório, e como a escala de cada variável é registrada para que um programa possa aplicá-la?")
    cell(AVG)
    cell(DERIVED)
    cell(SCALES)
    cell(INTERVAL)
    cell(VALID)
    cell(SUMMARY)
    exs = [(12, "", EX12), (13, "", EX13)]
    return S, [(k, title, code(block)) for k, title, block in exs]

"""All code cells of the Chapter 5 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions. The Portuguese cell
is the same code with the comments and printed text translated through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the follow-up table: one row per person, with the dates of entry and exit and whether the exit was a diagnosis", "# 1. Ler a tabela de seguimento: uma linha por pessoa, com as datas de entrada e de saída e se a saída foi um diagnóstico"),
 ("# 2. Follow-up of each person in whole days, and the person-years (the sum of the days divided by 365.25)", "# 2. Seguimento de cada pessoa em dias completos e as pessoas-ano (a soma dos dias dividida por 365,25)"),
 ("Persons:", "Pessoas:"),
 ("; new cases:", "; casos novos:"),
 ("; person-years:", "; pessoas-ano:"),
 ("# 3. The observed diagnosis fraction (cases divided by persons) and the incidence rate (cases divided by person-time)", "# 3. A fração de diagnósticos observada (casos divididos por pessoas) e a taxa de incidência (casos divididos pelo tempo-pessoa)"),
 ("Observed diagnosis fraction:", "Fração de diagnósticos observada:"),
 ("Incidence rate:", "Taxa de incidência:"),
 ("\"per 1,000 person-years\"", "\"por 1.000 pessoas-ano\""),
 ("# 1. The counts of the program, each kept with its own denominator", "# 1. As contagens do programa, cada uma mantida com o seu próprio denominador"),
 ("# 2. The administrative estimate: doses divided by children", "# 2. A estimativa administrativa: doses divididas por crianças"),
 ("Administrative coverage (doses over children):", "Cobertura administrativa (doses sobre crianças):"),
 ("# 3. The audited dose coverage: valid doses over the three doses that each child needs", "# 3. A cobertura de doses auditada: doses válidas sobre as três doses de que cada criança precisa"),
 ("Audited dose coverage (valid doses over 3 doses per child):", "Cobertura de doses auditada (doses válidas sobre 3 doses por criança):"),
 ("# 4. The proportion of children with three doses", "# 4. A proporção de crianças com três doses"),
 ("Children with three doses:", "Crianças com três doses:"),
 ("# 5. The survey estimate: 98 vaccinated among 420 children", "# 5. A estimativa do inquérito: 98 vacinadas entre 420 crianças"),
 ("Survey estimate:", "Estimativa do inquérito:"),
 ("# 1. Read the deaths and the populations by age group of towns A and B", "# 1. Ler os óbitos e as populações por faixa etária dos municípios A e B"),
 ("# 2. Crude rates per 1,000: all deaths over the whole population", "# 2. Taxas brutas por 1.000: todos os óbitos sobre a população inteira"),
 ("Crude rate, town A:", "Taxa bruta, município A:"),
 ("; town B:", "; município B:"),
 ("# 3. Direct standardization: the age-specific rates of each town applied to the combined population of A and B (the standard)", "# 3. Padronização direta: as taxas específicas por idade de cada município aplicadas à população combinada de A e B (o padrão)"),
 ("Standardized rate, town A:", "Taxa padronizada, município A:"),
 ("# 4. Indirect standardization: deaths expected in B under the age-specific rates of A, and the ratio of observed to expected deaths", "# 4. Padronização indireta: óbitos esperados em B sob as taxas específicas por idade de A e a razão entre óbitos observados e esperados"),
 ("Observed deaths in B:", "Óbitos observados em B:"),
 ("; expected:", "; esperados:"),
 ("Standardized mortality ratio of B (observed over expected):", "Razão de mortalidade padronizada de B (observados sobre esperados):"),
 ("# 1. The year of a 300-bed hospital: beds, days, occupied bed-days, and stays that ended", "# 1. O ano de um hospital de 300 leitos: leitos, dias, leitos-dia ocupados e internações encerradas"),
 ("# 2. The three indicators", "# 2. Os três indicadores"),
 ("Occupancy:", "Taxa de ocupação:"),
 ("Period stay indicator:", "Indicador de permanência do período:"),
 ("\"days\")", "\"dias\")"),
 ("Turnover:", "Giro:"),
 ("\"stays per bed\")", "\"internações por leito\")"),
 ("# 3. Turnover from the identity: days times occupancy divided by the period stay indicator", "# 3. O giro pela identidade: dias vezes ocupação divididos pelo indicador de permanência do período"),
 ("Turnover from the identity:", "Giro pela identidade:"),
 ("# 1. Incidence per 100,000 by district: the cases of each district divided by its own population", "# 1. Incidência por 100.000 por distrito: os casos de cada distrito divididos pela sua própria população"),
 ("Incidence per 100,000 by district:", "Incidência por 100.000 por distrito:"),
 ("# 2. Case fatality (%) among the hospitalized cases of each district", "# 2. Letalidade (%) entre os casos hospitalizados de cada distrito"),
 ("Case fatality among hospitalized cases, % by district:", "Letalidade entre os casos hospitalizados, % por distrito:"),
 ("# 1. Standardization with the population of town A as the standard", "# 1. Padronização com a população do município A como padrão"),
 ("Standardized rate with A as the standard - town A:", "Taxa padronizada com A como padrão - município A:"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


INC = '''# 1. Read the follow-up table: one row per person, with the dates of entry and exit and whether the exit was a diagnosis
import pandas as pd

cohort = pd.read_csv("data/diabetes_cohort.csv", parse_dates=["entered", "exited"])

# 2. Follow-up of each person in whole days, and the person-years (the sum of the days divided by 365.25)
days = (cohort["exited"] - cohort["entered"]).dt.days
person_years = days.sum() / 365.25
new_cases = cohort["diagnosed"].sum()
print("Persons:", len(cohort), "; new cases:", new_cases, "; person-years:", round(person_years, 1))

# 3. The observed diagnosis fraction (cases divided by persons) and the incidence rate (cases divided by person-time)
print("Observed diagnosis fraction:", round(100 * new_cases / len(cohort), 2), "%")
print("Incidence rate:", round(1000 * new_cases / person_years, 1), "per 1,000 person-years")
'''

COV = '''# 1. The counts of the program, each kept with its own denominator
doses = 2496
cohort_size = 2400
outside = 138
duplicated = 61
children_3 = 600
valid = doses - outside - duplicated

# 2. The administrative estimate: doses divided by children
print("Administrative coverage (doses over children):", round(100 * doses / cohort_size, 1), "%")

# 3. The audited dose coverage: valid doses over the three doses that each child needs
print("Audited dose coverage (valid doses over 3 doses per child):", round(100 * valid / (3 * cohort_size), 1), "%")

# 4. The proportion of children with three doses
print("Children with three doses:", round(100 * children_3 / cohort_size, 1), "%")

# 5. The survey estimate: 98 vaccinated among 420 children
print("Survey estimate:", round(100 * 98 / 420, 1), "%")
'''

STD = '''# 1. Read the deaths and the populations by age group of towns A and B
import pandas as pd

m = pd.read_csv("data/mortality.csv")

# 2. Crude rates per 1,000: all deaths over the whole population
print("Crude rate, town A:", round(1000 * m["deaths_a"].sum() / m["population_a"].sum(), 2), "; town B:", round(1000 * m["deaths_b"].sum() / m["population_b"].sum(), 2))

# 3. Direct standardization: the age-specific rates of each town applied to the combined population of A and B (the standard)
rate_a = m["deaths_a"] / m["population_a"]
rate_b = m["deaths_b"] / m["population_b"]
standard = m["population_a"] + m["population_b"]
print("Standardized rate, town A:", round(1000 * (rate_a * standard).sum() / standard.sum(), 2), "; town B:", round(1000 * (rate_b * standard).sum() / standard.sum(), 2))

# 4. Indirect standardization: deaths expected in B under the age-specific rates of A, and the ratio of observed to expected deaths
expected_b = (rate_a * m["population_b"]).sum()
print("Observed deaths in B:", m["deaths_b"].sum(), "; expected:", round(expected_b))
print("Standardized mortality ratio of B (observed over expected):", round(m["deaths_b"].sum() / expected_b, 3))
'''

HOSP = '''# 1. The year of a 300-bed hospital: beds, days, occupied bed-days, and stays that ended
beds = 300
days = 365
occupied_bed_days = 91980
ended_stays = 12264

# 2. The three indicators
occupancy = occupied_bed_days / (beds * days)
period_stay = occupied_bed_days / ended_stays
turnover = ended_stays / beds
print("Occupancy:", round(100 * occupancy, 1), "%")
print("Period stay indicator:", round(period_stay, 1), "days")
print("Turnover:", round(turnover, 1), "stays per bed")

# 3. Turnover from the identity: days times occupancy divided by the period stay indicator
print("Turnover from the identity:", round(days * occupancy / period_stay, 1), "stays per bed")
'''

EX13 = '''# 1. Incidence per 100,000 by district: the cases of each district divided by its own population
cases = pd.read_csv("data/surveillance.csv")
population = {"north": 110000, "south": 90000}
by_district = cases.groupby("district").size()
print("Incidence per 100,000 by district:", (1e5 * by_district / pd.Series(population)).round(1).to_dict())

# 2. Case fatality (%) among the hospitalized cases of each district
admitted = cases[cases["hospitalized"]].groupby("district")
print("Case fatality among hospitalized cases, % by district:", (100 * admitted["died"].sum() / admitted.size()).round(1).to_dict())
'''

EX14 = '''# 1. Standardization with the population of town A as the standard
standard = m["population_a"]
rate_a = m["deaths_a"] / m["population_a"]
rate_b = m["deaths_b"] / m["population_b"]
print("Standardized rate with A as the standard - town A:", round(1000 * (rate_a * standard).sum() / standard.sum(), 2), "; town B:", round(1000 * (rate_b * standard).sum() / standard.sum(), 2))
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

    sec("5.4", "Incidence", "Incidência", "How often do new cases of diabetes appear in the cohort?", "Com que frequência aparecem casos novos de diabetes na coorte?")
    cell(INC)
    sec("5.9", "Program coverage", "Cobertura do programa", "Was DTP vaccine coverage really 104%?", "A cobertura da vacina DTP foi mesmo de 104%?")
    cell(COV)
    sec("5.10", "Crude and standardized rates", "Taxas brutas e padronizadas", "Is mortality really higher in the neighboring municipality?", "A mortalidade é mesmo maior no município vizinho?")
    cell(STD)
    sec("5.11", "Hospital service indicators", "Indicadores de serviços hospitalares", "How are the beds of the 300-bed hospital used?", "Como são usados os leitos do hospital de 300 leitos?")
    cell(HOSP)
    exs = [(13, "", EX13), (14, "", EX14)]
    return S, [(k, title, code(block)) for k, title, block in exs]

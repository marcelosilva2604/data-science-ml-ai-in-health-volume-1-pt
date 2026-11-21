"""All code cells of the Chapter 7 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions (the four cells of a table are
read inline each time). The Portuguese cell is the same code with the comments and printed text translated through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the surgery register: one row per patient", "# 1. Ler o registro cirúrgico: uma linha por paciente"),
 ("# 2. The two-by-two table of diabetes (rows) and infection within 30 days (columns), \"yes\" first", "# 2. A tabela dois por dois de diabetes (linhas) e infecção em 30 dias (colunas), \"yes\" primeiro"),
 ("# 3. The risk of infection in each row: the infections divided by the patients of the row", "# 3. O risco de infecção em cada linha: as infecções divididas pelos pacientes da linha"),
 ("Risk with diabetes:", "Risco com diabetes:"),
 ("; without diabetes:", "; sem diabetes:"),
 ("# 1. The risk difference as a proportion, in percentage points, and per 1,000 patients", "# 1. A diferença de riscos como proporção, em pontos percentuais e por 1.000 pacientes"),
 ("Risk difference:", "Diferença de riscos:"),
 ("\"percentage points =\"", "\"pontos percentuais =\""),
 ("\"per 1,000 patients\"", "\"por 1.000 pacientes\""),
 ("# 1. The risk ratio of diabetes and the relative increase in %", "# 1. A razão de riscos do diabetes e o aumento relativo em %"),
 ("Risk ratio of diabetes:", "Razão de riscos do diabetes:"),
 ("; relative increase:", "; aumento relativo:"),
 ("# 2. The decolonization bundle: the four cells (infected and not infected, with and without the bundle)", "# 2. O pacote de descolonização: as quatro células (infectados e não infectados, com e sem o pacote)"),
 ("Cells a, b, c, d:", "Células a, b, c, d:"),
 ("# 3. The risk ratio of the bundle and the relative reduction in %", "# 3. A razão de riscos do pacote e a redução relativa em %"),
 ("Risk ratio of the bundle:", "Razão de riscos do pacote:"),
 ("; relative reduction:", "; redução relativa:"),
 ("# 1. Prevalence in each shift of a cross-sectional snapshot, and the prevalence ratio", "# 1. Prevalência em cada turno de um retrato transversal e a razão de prevalências"),
 ("Prevalence ratio, night against day:", "Razão de prevalências, noite contra dia:"),
 ("# 1. Risk ratio and odds ratio of diabetes for two outcomes: infection and any complication within 30 days", "# 1. Razão de riscos e razão de chances do diabetes para dois desfechos: infecção e qualquer complicação em 30 dias"),
 (": risk ratio\"", ": razão de riscos\""),
 ("; odds ratio", "; razão de chances"),
 ("# 1. First readmissions and follow-up days in each group, and the rate per 1,000 patient-days", "# 1. Primeiras reinternações e dias de seguimento em cada grupo, e a taxa por 1.000 pacientes-dia"),
 ("\"Diabetes\"", "\"Diabetes\""),
 ("\"readmissions in\"", "\"reinternações em\""),
 ("\"patient-days =\"", "\"pacientes-dia =\""),
 ("\"per 1,000 patient-days\"", "\"por 1.000 pacientes-dia\""),
 ("# 2. The rate ratio", "# 2. A razão de taxas"),
 ("Rate ratio:", "Razão de taxas:"),
 ("# 1. The bundle: the absolute risk reduction and the number needed to treat (the reciprocal, rounded up)", "# 1. O pacote: a redução absoluta de risco e o número necessário para tratar (o inverso, arredondado para cima)"),
 ("Absolute risk reduction:", "Redução absoluta de risco:"),
 ("; number needed to treat:", "; número necessário para tratar:"),
 ("# 2. A lower-risk scenario: baseline risk of 2%, with the risk ratio of the bundle", "# 2. Um cenário de menor risco: risco basal de 2%, com a razão de riscos do pacote"),
 ("Number needed to treat at a baseline risk of 2%:", "Número necessário para tratar com risco basal de 2%:"),
 ("# 3. The harm example: 20 against 10 events per 1,000, and the number needed to harm", "# 3. O exemplo de dano: 20 contra 10 eventos por 1.000 e o número necessário para causar dano"),
 ("Number needed to harm:", "Número necessário para causar dano:"),
 ("# 1. Infections expected among the 600 patients with diabetes at the risk of those without, and the excess", "# 1. Infecções esperadas entre os 600 pacientes com diabetes ao risco dos sem diabetes e o excesso"),
 ("Expected infections:", "Infecções esperadas:"),
 ("; excess infections:", "; infecções em excesso:"),
 ("# 2. The attributable fraction among the exposed", "# 2. A fração atribuível entre os expostos"),
 ("Attributable fraction among the exposed:", "Fração atribuível entre os expostos:"),
 ("# 1. The population attributable fraction by the direct comparison and by the formula with the exposure prevalence", "# 1. A fração atribuível populacional pela comparação direta e pela fórmula com a prevalência da exposição"),
 ("Population attributable fraction, direct:", "Fração atribuível populacional, direta:"),
 ("\"%; by the formula:\"", "\"%; pela fórmula:\""),
 ("# 1. Smoking and infection within each surgery class: the four cells and the risk ratio of the class", "# 1. Tabagismo e infecção dentro de cada classe de cirurgia: as quatro células e a razão de riscos da classe"),
 ("\"Class\"", "\"Classe\""),
 (": cells", ": células"),
 ("; risk ratio", "; razão de riscos"),
 ("# 1. Two hospitals: crude mortality and mortality with a common case mix (half severe, half mild)", "# 1. Dois hospitais: mortalidade bruta e mortalidade com uma mistura de casos comum (metade graves, metade leves)"),
 ("\"Hospital\"", "\"Hospital\""),
 (": crude mortality", ": mortalidade bruta"),
 ("\"%; with a common case mix\"", "\"%; com mistura de casos comum\""),
 ("# 1. All the cases of infection and four controls per case drawn at random from the patients without infection (seed 7)", "# 1. Todos os casos de infecção e quatro controles por caso sorteados entre os pacientes sem infecção (semente 7)"),
 ("# 2. The table of diabetes and case status in the case-control sample", "# 2. A tabela de diabetes e situação de caso na amostra de caso-controle"),
 ("# 3. The odds ratio, and the row fractions (which are not population risks)", "# 3. A razão de chances e as frações das linhas (que não são riscos populacionais)"),
 ("Odds ratio:", "Razão de chances:"),
 ("Row fractions with diabetes and without:", "Frações das linhas com diabetes e sem diabetes:"),
 ("# 1. Infection risk by sex, in %: men and women", "# 1. Risco de infecção por sexo, em %: homens e mulheres"),
 ("Risk in men and in women (%):", "Risco em homens e em mulheres (%):"),
 ("# 2. The risk difference between men and women, in percentage points", "# 2. A diferença de riscos entre homens e mulheres, em pontos percentuais"),
 ("Risk difference, men minus women:", "Diferença de riscos, homens menos mulheres:"),
 ("# 1. First readmissions and follow-up days with and without the bundle", "# 1. Primeiras reinternações e dias de seguimento com e sem o pacote"),
 ("\"Bundle\"", "\"Pacote\""),
 ("# 2. The rate ratio of the bundle", "# 2. A razão de taxas do pacote"),
 ("Rate ratio of the bundle:", "Razão de taxas do pacote:"),
 ("# 1. The risk ratio of diabetes within each surgery class", "# 1. A razão de riscos do diabetes dentro de cada classe de cirurgia"),
 (": risk ratio of diabetes", ": razão de riscos do diabetes"),
 ("# 2. The percentage of clean operations among patients with and without diabetes", "# 2. A porcentagem de operações limpas entre pacientes com e sem diabetes"),
 (": clean operations", ": operações limpas"),
 ("# 1. All the cases and two controls per case, drawn at random from the patients without infection (seed 7)", "# 1. Todos os casos e dois controles por caso, sorteados entre os pacientes sem infecção (semente 7)"),
 ("# 2. The table of diabetes and case status", "# 2. A tabela de diabetes e situação de caso"),
 ("# 3. The odds ratio and the row fractions", "# 3. A razão de chances e as frações das linhas"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


TABLE = '''# 1. Read the surgery register: one row per patient
import pandas as pd

df = pd.read_csv("data/surgery_cohort.csv")

# 2. The two-by-two table of diabetes (rows) and infection within 30 days (columns), "yes" first
table = pd.crosstab(df["diabetes"], df["ssi_30d"])
table = table.reindex(index=["yes", "no"], columns=["yes", "no"], fill_value=0)
print(table)

# 3. The risk of infection in each row: the infections divided by the patients of the row
p1 = table.loc["yes", "yes"] / table.loc["yes"].sum()
p0 = table.loc["no", "yes"] / table.loc["no"].sum()
print("Risk with diabetes:", round(p1, 4), "; without diabetes:", round(p0, 4))
'''

RD = '''# 1. The risk difference as a proportion, in percentage points, and per 1,000 patients
rd = p1 - p0
print("Risk difference:", round(rd, 4), "=", round(100 * rd, 2), "percentage points =", round(1000 * rd, 1), "per 1,000 patients")
'''

RR = '''# 1. The risk ratio of diabetes and the relative increase in %
rr = p1 / p0
print("Risk ratio of diabetes:", round(rr, 3), "; relative increase:", round(100 * (rr - 1), 1), "%")

# 2. The decolonization bundle: the four cells (infected and not infected, with and without the bundle)
bundle_table = pd.crosstab(df["bundle"], df["ssi_30d"])
bundle_table = bundle_table.reindex(index=["yes", "no"], columns=["yes", "no"], fill_value=0)
a = int(bundle_table.at["yes", "yes"])
b = int(bundle_table.at["yes", "no"])
c = int(bundle_table.at["no", "yes"])
d = int(bundle_table.at["no", "no"])
print("Cells a, b, c, d:", a, b, c, d)

# 3. The risk ratio of the bundle and the relative reduction in %
bundle_p1 = a / (a + b)
bundle_p0 = c / (c + d)
bundle_rr = bundle_p1 / bundle_p0
print("Risk ratio of the bundle:", round(bundle_rr, 3), "; relative reduction:", round(100 * (1 - bundle_rr), 1), "%")
'''

PR = '''# 1. Prevalence in each shift of a cross-sectional snapshot, and the prevalence ratio
night_prevalence = 80 / 400
day_prevalence = 40 / 400
print("Prevalence ratio, night against day:", night_prevalence / day_prevalence)
'''

OR = '''# 1. Risk ratio and odds ratio of diabetes for two outcomes: infection and any complication within 30 days
for outcome in ["ssi_30d", "complication_30d"]:
    outcome_table = pd.crosstab(df["diabetes"], df[outcome])
    outcome_table = outcome_table.reindex(index=["yes", "no"], columns=["yes", "no"], fill_value=0)
    a = int(outcome_table.at["yes", "yes"])
    b = int(outcome_table.at["yes", "no"])
    c = int(outcome_table.at["no", "yes"])
    d = int(outcome_table.at["no", "no"])
    exposed_risk = a / (a + b)
    comparison_risk = c / (c + d)
    risk_ratio = exposed_risk / comparison_risk
    odds_ratio = (a * d) / (b * c)
    print(outcome + ": risk ratio", round(risk_ratio, 3), "; odds ratio", round(odds_ratio, 3))
'''

RATE = '''# 1. First readmissions and follow-up days in each group, and the rate per 1,000 patient-days
rates = {}
for group in ["yes", "no"]:
    part = df.loc[df["diabetes"] == group]
    events = int(part["readmitted_90d"].eq("yes").sum())
    days = int(part["followup_days"].sum())
    rates[group] = events / days
    print("Diabetes", group + ":", events, "readmissions in", days, "patient-days =", round(1000 * rates[group], 2), "per 1,000 patient-days")

# 2. The rate ratio
print("Rate ratio:", round(rates["yes"] / rates["no"], 3))
'''

NNT = '''# 1. The bundle: the absolute risk reduction and the number needed to treat (the reciprocal, rounded up)
import math

bundle_arr = bundle_p0 - bundle_p1
print("Absolute risk reduction:", round(bundle_arr, 4), "; number needed to treat:", math.ceil(1 / bundle_arr))

# 2. A lower-risk scenario: baseline risk of 2%, with the risk ratio of the bundle
scenario_arr = 0.02 * (1 - bundle_rr)
print("Number needed to treat at a baseline risk of 2%:", math.ceil(1 / scenario_arr))

# 3. The harm example: 20 against 10 events per 1,000, and the number needed to harm
harm_increase = 20 / 1000 - 10 / 1000
print("Number needed to harm:", math.ceil(1 / harm_increase))
'''

AF = '''# 1. Infections expected among the 600 patients with diabetes at the risk of those without, and the excess
expected_exposed = 600 * p0
excess_exposed = 81 - expected_exposed
print("Expected infections:", round(expected_exposed), "; excess infections:", round(excess_exposed))

# 2. The attributable fraction among the exposed
af_exposed = (p1 - p0) / p1
print("Attributable fraction among the exposed:", round(100 * af_exposed, 1), "%")
'''

PAF = '''# 1. The population attributable fraction by the direct comparison and by the formula with the exposure prevalence
population_risk = 192 / 2400
exposure_prevalence = 600 / 2400
paf_direct = (population_risk - p0) / population_risk
paf_formula = exposure_prevalence * (rr - 1) / (1 + exposure_prevalence * (rr - 1))
print("Population attributable fraction, direct:", round(100 * paf_direct, 1), "%; by the formula:", round(100 * paf_formula, 1), "%")
'''

STRATA = '''# 1. Smoking and infection within each surgery class: the four cells and the risk ratio of the class
for surgery_class, part in df.groupby("surgery_class", sort=True):
    class_table = pd.crosstab(part["smoker"], part["ssi_30d"])
    class_table = class_table.reindex(index=["yes", "no"], columns=["yes", "no"], fill_value=0)
    a = int(class_table.at["yes", "yes"])
    b = int(class_table.at["yes", "no"])
    c = int(class_table.at["no", "yes"])
    d = int(class_table.at["no", "no"])
    stratum_rr = (a / (a + b)) / (c / (c + d))
    print("Class", surgery_class + ": cells", a, b, c, d, "; risk ratio", round(stratum_rr, 2))
'''

SIMPSON = '''# 1. Two hospitals: crude mortality and mortality with a common case mix (half severe, half mild)
for name, severe_n, severe_deaths, mild_n, mild_deaths in [
    ("A", 200, 40, 800, 16),
    ("B", 800, 120, 200, 2),
]:
    crude = (severe_deaths + mild_deaths) / (severe_n + mild_n)
    common_mix = 0.5 * severe_deaths / severe_n + 0.5 * mild_deaths / mild_n
    print("Hospital", name + ": crude mortality", round(100 * crude, 1), "%; with a common case mix", round(100 * common_mix, 1), "%")
'''

CC = '''# 1. All the cases of infection and four controls per case drawn at random from the patients without infection (seed 7)
cases = df.loc[df["ssi_30d"] == "yes"]
noncases = df.loc[df["ssi_30d"] == "no"]
controls = noncases.sample(n=4 * len(cases), random_state=7)
case_control = pd.concat([cases, controls], ignore_index=True)

# 2. The table of diabetes and case status in the case-control sample
cc_table = pd.crosstab(case_control["diabetes"], case_control["ssi_30d"])
cc_table = cc_table.reindex(index=["yes", "no"], columns=["yes", "no"], fill_value=0)
a = int(cc_table.at["yes", "yes"])
b = int(cc_table.at["yes", "no"])
c = int(cc_table.at["no", "yes"])
d = int(cc_table.at["no", "no"])
print("Cells a, b, c, d:", a, b, c, d)

# 3. The odds ratio, and the row fractions (which are not population risks)
print("Odds ratio:", round(a * d / (b * c), 3))
print("Row fractions with diabetes and without:", round(a / (a + b), 3), round(c / (c + d), 3))
'''

EX3 = '''# 1. Infection risk by sex, in %: men and women
sex_table = pd.crosstab(df["sex"], df["ssi_30d"])
sex_table = sex_table.reindex(index=["M", "F"], columns=["yes", "no"])
sex_risks = sex_table["yes"] / sex_table.sum(axis=1)
print("Risk in men and in women (%):", (100 * sex_risks).round(2).tolist())

# 2. The risk difference between men and women, in percentage points
print("Risk difference, men minus women:", round(100 * (sex_risks["M"] - sex_risks["F"]), 3), "percentage points")
'''

EX7 = '''# 1. First readmissions and follow-up days with and without the bundle
bundle_rates = {}
for group in ["yes", "no"]:
    part = df.loc[df["bundle"] == group]
    events = int(part["readmitted_90d"].eq("yes").sum())
    days = int(part["followup_days"].sum())
    bundle_rates[group] = events / days
    print("Bundle", group + ":", events, "readmissions in", days, "patient-days")

# 2. The rate ratio of the bundle
print("Rate ratio of the bundle:", round(bundle_rates["yes"] / bundle_rates["no"], 3))
'''

EX12 = '''# 1. The risk ratio of diabetes within each surgery class
for surgery_class, part in df.groupby("surgery_class", sort=True):
    tab = pd.crosstab(part["diabetes"], part["ssi_30d"])
    risks = tab["yes"] / tab.sum(axis=1)
    print("Class", surgery_class + ": risk ratio of diabetes", round(risks["yes"] / risks["no"], 3))

# 2. The percentage of clean operations among patients with and without diabetes
for group in ["yes", "no"]:
    part = df.loc[df["diabetes"] == group]
    print("Diabetes", group + ": clean operations", round(100 * part["surgery_class"].eq("clean").mean(), 1), "%")
'''

EX14 = '''# 1. All the cases and two controls per case, drawn at random from the patients without infection (seed 7)
cases = df.loc[df["ssi_30d"] == "yes"]
noncases = df.loc[df["ssi_30d"] == "no"]
controls = noncases.sample(n=2 * len(cases), random_state=7)
selected = pd.concat([cases, controls], ignore_index=True)

# 2. The table of diabetes and case status
tab = pd.crosstab(selected["diabetes"], selected["ssi_30d"])
a = int(tab.at["yes", "yes"])
b = int(tab.at["yes", "no"])
c = int(tab.at["no", "yes"])
d = int(tab.at["no", "no"])
print("Cells a, b, c, d:", a, b, c, d)

# 3. The odds ratio and the row fractions
print("Odds ratio:", round(a * d / (b * c), 3))
print("Row fractions with diabetes and without:", round(a / (a + b), 3), round(c / (c + d), 3))
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

    sec("7.2", "The two-by-two table", "A tabela dois por dois", "What fraction of the patients with and without diabetes had an infection?", "Que fração dos pacientes com e sem diabetes teve infecção?")
    cell(TABLE)
    sec("7.4", "Risk difference", "Diferença de riscos", "By how much does diabetes raise the risk of infection, in absolute terms?", "Em quanto o diabetes eleva o risco de infecção, em termos absolutos?")
    cell(RD)
    sec("7.5", "Risk ratio", "Razão de riscos", "How many times higher is the risk, and what does the bundle do to it?", "Quantas vezes maior é o risco, e o que o pacote faz com ele?")
    cell(RR)
    sec("7.6", "Prevalence ratio", "Razão de prevalências", "In a cross-sectional study, how do the prevalences compare?", "Em um estudo transversal, como se comparam as prevalências?")
    cell(PR)
    sec("7.7", "Odds ratio", "Razão de chances", "How do the odds compare, and when do they differ from the risks?", "Como se comparam as chances, e quando elas diferem dos riscos?")
    cell(OR)
    sec("7.8", "Rate ratio", "Razão de taxas", "How do the readmission rates compare over the follow-up time?", "Como se comparam as taxas de reinternação ao longo do seguimento?")
    cell(RATE)
    sec("7.9", "Number needed to treat and number needed to harm", "Número necessário para tratar e número necessário para causar dano", "How many patients must be treated to prevent one infection?", "Quantos pacientes precisam ser tratados para evitar uma infecção?")
    cell(NNT)
    sec("7.10", "Attributable fraction among the exposed", "Fração atribuível entre os expostos", "What fraction of the infections among the exposed is attributable to diabetes?", "Que fração das infecções entre os expostos é atribuível ao diabetes?")
    cell(AF)
    sec("7.11", "Population attributable fraction", "Fração atribuível populacional", "What fraction of all the infections is attributable to diabetes?", "Que fração de todas as infecções é atribuível ao diabetes?")
    cell(PAF)
    sec("7.12", "Stratification and confounding", "Estratificação e confusão", "How does the association of smoking and infection behave within each surgery class?", "Como a associação entre tabagismo e infecção se comporta dentro de cada classe de cirurgia?")
    cell(STRATA)
    sec("7.13", "Simpson's paradox", "Paradoxo de Simpson", "Can a crude comparison reverse when the case mix is equalized?", "Uma comparação bruta pode se inverter quando a mistura de casos é igualada?")
    cell(SIMPSON)
    sec("7.14", "What a case-control study can estimate", "O que um estudo de caso-controle pode estimar", "What can a case-control study estimate?", "O que um estudo de caso-controle pode estimar?")
    cell(CC)
    exs = [(3, "", EX3), (7, "", EX7), (12, "", EX12), (14, "", EX14)]
    return S, [(k, title, code(block)) for k, title, block in exs]

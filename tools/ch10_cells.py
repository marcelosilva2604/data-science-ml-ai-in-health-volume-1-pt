"""All code cells of the Chapter 10 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. Beginner-friendly Python: print with commas, round(), no f-strings, no helper functions.
The cells are written once in English; the Portuguese cell is the same code with the comments and printed text translated
through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the record: one row is one adult", "# 1. Ler o registro: cada linha é um adulto"),
 ("# 2. Count rows and columns", "# 2. Contar linhas e colunas"),
 ("# 3. A True/False column that is True when the pressure is still uncontrolled at 12 weeks (used from here on)", "# 3. Uma coluna Verdadeiro/Falso que é True quando a pressão continua não controlada em 12 semanas (usada daqui em diante)"),
 ("The record has", "O registro tem"), ("rows (one per adult) and", "linhas (uma por adulto) e"), ("columns.", "colunas."),
 ("# The first five rows", "# As cinco primeiras linhas"),
 ("# 1. The trial months are the rows with period \"trial\" (months 7-12)", "# 1. Os meses do ensaio são as linhas com period \"trial\" (meses 7-12)"),
 ("# 2. Count the adults and those with uncontrolled pressure at 12 weeks", "# 2. Contar os adultos e os com pressão não controlada em 12 semanas"),
 ("# 3. Divide the count by all the adults of the trial", "# 3. Dividir a contagem por todos os adultos do ensaio"),
 ("Adults in the trial months:", "Adultos nos meses do ensaio:"),
 ("Uncontrolled at 12 weeks:", "Não controlados em 12 semanas:"), ('"of"', '"de"'),
 ("Overall risk:", "Risco geral:"),
 ("# 1. Take each assigned arm and count its adults", "# 1. Pegar cada braço alocado e contar seus adultos"),
 ("# 2. Count the adults with baseline systolic pressure of at least 160 mmHg", "# 2. Contar os adultos com pressão sistólica basal de pelo menos 160 mmHg"),
 ("# 3. Count the adults with diabetes", "# 3. Contar os adultos com diabetes"),
 ("adults;", "adultos;"), ("with baseline pressure of at least 160 mmHg =", "com pressão basal de pelo menos 160 mmHg ="),
 ("with diabetes =", "com diabetes ="),
 ("# 1. In each assigned arm, count the adults and those uncontrolled", "# 1. Em cada braço alocado, contar os adultos e os não controlados"),
 ("# 2. Risk = uncontrolled adults / all adults of the arm", "# 2. Risco = adultos não controlados / todos os adultos do braço"),
 ("# 3. Risk difference (percentage points) and risk ratio", "# 3. Diferença de riscos (pontos percentuais) e razão de riscos"),
 ("# 4. Standard error and 95% interval of the difference (normal approximation)", "# 4. Erro padrão e intervalo de 95% da diferença (aproximação normal)"),
 ("# 5. The ratio is handled on the logarithm scale, then back with exp", "# 5. A razão é tratada na escala do logaritmo e depois volta com exp"),
 ("Single pill:", "Pílula única:"), ("Separate tablets:", "Comprimidos separados:"),
 ("Risk difference:", "Diferença de riscos:"), ("percentage points", "pontos percentuais"), ("Risk ratio:", "Razão de riscos:"),
 ("Standard error:", "Erro padrão:"), ("normal multiplier:", "multiplicador normal:"),
 ("Difference:", "Diferença:"), ("95% CI", "IC de 95%"), ("Ratio:", "Razão:"), ('"to"', '"a"'),
 ("# 1. Keep only the adults whose treatment received matches the assigned arm", "# 1. Manter só os adultos cujo tratamento recebido coincide com o braço alocado"),
 ("# 2. In this restricted group, count events and adults in each arm", "# 2. Neste grupo restrito, contar eventos e adultos em cada braço"),
 ("# 3. Restricted risk ratio and its 95% interval (logarithm scale)", "# 3. Razão de riscos restrita e seu intervalo de 95% (escala do logaritmo)"),
 ("Retained adults:", "Adultos mantidos:"), ("events/total:", "eventos/total:"), ("Restricted ratio:", "Razão restrita:"),
 ("# 1. Use the interval of the intention-to-treat analysis (section 10.4.2)", "# 1. Usar o intervalo da análise por intenção de tratar (seção 10.4.2)"),
 ("# 2. Superiority: the whole interval lies below zero", "# 2. Superioridade: o intervalo inteiro fica abaixo de zero"),
 ("# 3. Noninferiority: the upper limit lies below the margin (illustrative margins)", "# 3. Não inferioridade: o limite superior fica abaixo da margem (margens ilustrativas)"),
 ("# 4. Equivalence: the interval lies inside the margin on both sides (illustrative margins)", "# 4. Equivalência: o intervalo fica dentro da margem nos dois lados (margens ilustrativas)"),
 ("Upper limit of the 95% interval:", "Limite superior do intervalo de 95%:"),
 ("Superiority (upper limit below zero):", "Superioridade (limite superior abaixo de zero):"),
 ("Noninferiority with margin", "Não inferioridade com margem"), ("Equivalence with margin", "Equivalência com margem"), ("points:", "pontos:"),
 ("# 1. Months 13-18: the rows of the clinics that adopted at random in month 13 or stayed on separate tablets", "# 1. Meses 13-18: as linhas dos ambulatórios que adotaram ao acaso no mês 13 ou ficaram com comprimidos separados"),
 ("# 2. Pooled by patient: events and adults in each arm", "# 2. Agrupando por paciente: eventos e adultos em cada braço"),
 ("# 3. Risk of each clinic, then the average of the clinic risks in each arm", "# 3. Risco de cada ambulatório e depois a média dos riscos dos ambulatórios em cada braço"),
 ("# 4. Welch interval for the difference of the clinic averages (each clinic is one observation)", "# 4. Intervalo de Welch para a diferença das médias dos ambulatórios (cada ambulatório é uma observação)"),
 ("clinics;", "ambulatórios;"), ("Pooled risk ratio:", "Razão de riscos agrupada:"),
 ("Mean clinic risks:", "Médias dos riscos dos ambulatórios:"), ("degrees of freedom:", "graus de liberdade:"), ("t multiplier:", "multiplicador t:"),
 ("# 1. Risk in each group of clinics and period (the clinics that switched in month 13 and in month 19)", "# 1. Risco em cada grupo de ambulatórios e período (os que trocaram no mês 13 e no mês 19)"),
 ("# 2. Change in each group from months 13-18 to months 19-24", "# 2. Mudança em cada grupo dos meses 13-18 para os meses 19-24"),
 ("# 3. Stepped-wedge contrast: the change of the late clinics minus the change of the early clinics", "# 3. Contraste em degraus escalonados: a mudança dos ambulatórios tardios menos a dos precoces"),
 ("Switched in month 13:", "Trocaram no mês 13:"), ("Switched in month 19:", "Trocaram no mês 19:"),
 ("Changes:", "Mudanças:"), ('"points"', '"pontos"'), ("Stepped-wedge contrast:", "Contraste em degraus escalonados:"),
 ("# 1. The clinics that adopted in month 13: months 1-6 (before) and months 13-18 (after)", "# 1. Os ambulatórios que adotaram no mês 13: meses 1-6 (antes) e meses 13-18 (depois)"),
 ("# 2. Pool the counts before dividing", "# 2. Somar as contagens antes de dividir"),
 ("Before:", "Antes:"), ("After:", "Depois:"), ("After/before ratio:", "Razão depois/antes:"),
 ("# 1. The four risks: adopting clinics (month 13) and comparison clinics (month 19), before and after", "# 1. Os quatro riscos: ambulatórios que adotaram (mês 13) e de comparação (mês 19), antes e depois"),
 ("# 2. Difference in differences = change of the adopting clinics minus change of the comparison clinics", "# 2. Diferença em diferenças = mudança dos que adotaram menos mudança dos de comparação"),
 ("# 3. The path assumed without adoption and the ratio of ratios", "# 3. O caminho suposto sem adoção e a razão de razões"),
 ("Adopting clinics:", "Ambulatórios que adotaram:"), ("Comparison clinics:", "Ambulatórios de comparação:"),
 ("Difference in differences:", "Diferença em diferenças:"), ("Assumed endpoint without adoption:", "Ponto final suposto sem adoção:"),
 ("Ratio of ratios:", "Razão de razões:"),
 ("# 1. Monthly counts for the clinics that adopted in month 13", "# 1. Contagens mensais dos ambulatórios que adotaram no mês 13"),
 ("# 2. Number of months before, during the trial, and after adoption", "# 2. Número de meses antes, durante o ensaio e depois da adoção"),
 ("# 3. The first monthly risk, with its own denominator", "# 3. O primeiro risco mensal, com seu próprio denominador"),
 ("Months before the trial:", "Meses antes do ensaio:"), ("Trial months:", "Meses do ensaio:"), ("Months after adoption:", "Meses depois da adoção:"),
 ("First month:", "Primeiro mês:"),
 ("# 1. Months 1-6 and months 19-24 for the whole service", "# 1. Meses 1-6 e meses 19-24 para o serviço inteiro"),
 ("# 2. In each period: adults, uncontrolled, and those who received the single pill", "# 2. Em cada período: adultos, não controlados e os que receberam a pílula única"),
 ('": uncontrolled"', '": não controlados"'), ('"%; uptake"', '"%; uso da pílula única"'),
 ("# 1. The stepped-wedge contrast (section 10.6.2) and the cluster comparison of months 13-18 pooled by patient", "# 1. O contraste em degraus escalonados (seção 10.6.2) e a comparação por conglomerados dos meses 13-18 agrupada por paciente"),
 ("Cluster comparison (pooled by patient):", "Comparação por conglomerados (agrupada por paciente):"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


LOAD = '''# 1. Read the record: one row is one adult
import pandas as pd
from math import sqrt, log, exp
from statistics import NormalDist
from scipy.stats import t

df = pd.read_csv("data/clinic_patients.csv")

# 2. Count rows and columns
rows, columns = df.shape
print("The record has", rows, "rows (one per adult) and", columns, "columns.")

# 3. A True/False column that is True when the pressure is still uncontrolled at 12 weeks (used from here on)
df["y"] = df["uncontrolled_12w"] == "yes"
df.head()                                      # The first five rows
'''

C_COMPARISON = '''# 1. The trial months are the rows with period "trial" (months 7-12)
trial = df[df["period"] == "trial"]

# 2. Count the adults and those with uncontrolled pressure at 12 weeks
n_trial = len(trial)
events = trial["y"].sum()

# 3. Divide the count by all the adults of the trial
print("Adults in the trial months:", n_trial)
print("Uncontrolled at 12 weeks:", events, "of", n_trial, "=", round(100 * events / n_trial, 1), "%")
print("Overall risk:", round(events / n_trial, 4))
'''

C_BALANCE = '''# 1. Take each assigned arm and count its adults
for arm in ["single pill", "separate tablets"]:
    group = trial[trial["allocated"] == arm]
    n = len(group)

    # 2. Count the adults with baseline systolic pressure of at least 160 mmHg
    high = (group["baseline_sbp"] >= 160).sum()

    # 3. Count the adults with diabetes
    diabetes = (group["diabetes"] == "yes").sum()
    print(arm + ":", n, "adults;", high, "with baseline pressure of at least 160 mmHg =", round(100 * high / n, 1), "%;",
          diabetes, "with diabetes =", round(100 * diabetes / n, 1), "%")
'''

C_ITT = '''# 1. In each assigned arm, count the adults and those uncontrolled
single = trial[trial["allocated"] == "single pill"]
separate = trial[trial["allocated"] == "separate tablets"]
a, n = single["y"].sum(), len(single)
b, m = separate["y"].sum(), len(separate)
print("Single pill:", a, "of", n)
print("Separate tablets:", b, "of", m)

# 2. Risk = uncontrolled adults / all adults of the arm
p = a / n
q = b / m

# 3. Risk difference (percentage points) and risk ratio
d = 100 * (p - q)
print("Risk difference:", round(d, 1), "percentage points")
print("Risk ratio:", round(p / q, 2))

# 4. Standard error and 95% interval of the difference (normal approximation)
z = NormalDist().inv_cdf(0.975)
se = 100 * sqrt(p * (1 - p) / n + q * (1 - q) / m)
itt_lower = d - z * se
itt_upper = d + z * se
print("Standard error:", round(se, 4), "; normal multiplier:", round(z, 4))
print("Difference:", round(d, 1), "; 95% CI", round(itt_lower, 1), "to", round(itt_upper, 1))

# 5. The ratio is handled on the logarithm scale, then back with exp
se_log = sqrt(1 / a - 1 / n + 1 / b - 1 / m)
print("Ratio:", round(p / q, 2), "; 95% CI", round(exp(log(p / q) - z * se_log), 2), "to", round(exp(log(p / q) + z * se_log), 2))
'''

C_PERPROTOCOL = '''# 1. Keep only the adults whose treatment received matches the assigned arm
matches = (trial["allocated"] == "single pill") == (trial["received"] == "yes")
kept = trial[matches]

# 2. In this restricted group, count events and adults in each arm
single = kept[kept["allocated"] == "single pill"]
separate = kept[kept["allocated"] == "separate tablets"]
a, n = single["y"].sum(), len(single)
b, m = separate["y"].sum(), len(separate)
print("Retained adults:", len(kept), "; events/total:", a, "/", n, ",", b, "/", m)

# 3. Restricted risk ratio and its 95% interval (logarithm scale)
ratio = (a / n) / (b / m)
se_log = sqrt(1 / a - 1 / n + 1 / b - 1 / m)
print("Restricted ratio:", round(ratio, 2), "; 95% CI", round(exp(log(ratio) - z * se_log), 2), "to", round(exp(log(ratio) + z * se_log), 2))
'''

C_NI = '''# 1. Use the interval of the intention-to-treat analysis (section 10.4.2)
print("Upper limit of the 95% interval:", round(itt_upper, 1), "percentage points")

# 2. Superiority: the whole interval lies below zero
print("Superiority (upper limit below zero):", itt_upper < 0)

# 3. Noninferiority: the upper limit lies below the margin (illustrative margins)
for margin in [2, 5, 10]:
    print("Noninferiority with margin", margin, "points:", itt_upper < margin)

# 4. Equivalence: the interval lies inside the margin on both sides (illustrative margins)
for margin in [5, 10, 15]:
    print("Equivalence with margin", margin, "points:", (itt_lower > -margin) and (itt_upper < margin))
'''

C_CLUSTER = '''# 1. Months 13-18: the rows of the clinics that adopted at random in month 13 or stayed on separate tablets
rollout = df[df["month"].between(13, 18)]

# 2. Pooled by patient: events and adults in each arm
for arm in ["single pill", "separate tablets"]:
    group = rollout[rollout["allocated"] == arm]
    print(arm + ":", group["clinic"].nunique(), "clinics;", group["y"].sum(), "of", len(group))
single = rollout[rollout["allocated"] == "single pill"]
separate = rollout[rollout["allocated"] == "separate tablets"]
print("Pooled risk ratio:", round((single["y"].sum() / len(single)) / (separate["y"].sum() / len(separate)), 2))

# 3. Risk of each clinic, then the average of the clinic risks in each arm
clinic_risk = rollout.groupby(["allocated", "clinic"])["y"].mean()
p_clinic = clinic_risk.loc["single pill"]
q_clinic = clinic_risk.loc["separate tablets"]
print("Mean clinic risks:", round(p_clinic.mean(), 4), ",", round(q_clinic.mean(), 4))

# 4. Welch interval for the difference of the clinic averages (each clinic is one observation)
u = p_clinic.var() / len(p_clinic)
v = q_clinic.var() / len(q_clinic)
dof = (u + v) ** 2 / (u * u / (len(p_clinic) - 1) + v * v / (len(q_clinic) - 1))
d_clinic = 100 * (p_clinic.mean() - q_clinic.mean())
se_clinic = 100 * sqrt(u + v)
cut = t.ppf(0.975, dof)
print("Standard error:", round(se_clinic, 4), "; degrees of freedom:", round(dof, 2), "; t multiplier:", round(cut, 4))
print("Difference:", round(d_clinic, 1), "; 95% CI", round(d_clinic - cut * se_clinic, 1), "to", round(d_clinic + cut * se_clinic, 1))
'''

C_STEPPED = '''# 1. Risk in each group of clinics and period (the clinics that switched in month 13 and in month 19)
early = df[df["clinic_start_month"] == 13]
late = df[df["clinic_start_month"] == 19]
early_first = early[early["month"].between(13, 18)]["y"].mean()
early_second = early[early["month"].between(19, 24)]["y"].mean()
late_first = late[late["month"].between(13, 18)]["y"].mean()
late_second = late[late["month"].between(19, 24)]["y"].mean()
print("Switched in month 13:", round(100 * early_first, 1), "%,", round(100 * early_second, 1), "%")
print("Switched in month 19:", round(100 * late_first, 1), "%,", round(100 * late_second, 1), "%")

# 2. Change in each group from months 13-18 to months 19-24
change_early = early_second - early_first
change_late = late_second - late_first
print("Changes:", round(100 * change_late, 1), ",", round(100 * change_early, 1), "points")

# 3. Stepped-wedge contrast: the change of the late clinics minus the change of the early clinics
print("Stepped-wedge contrast:", round(100 * (change_late - change_early), 1), "points")
'''

C_BEFORE = '''# 1. The clinics that adopted in month 13: months 1-6 (before) and months 13-18 (after)
adopters = df[df["clinic_start_month"] == 13]
before = adopters[adopters["month"].between(1, 6)]
after = adopters[adopters["month"].between(13, 18)]

# 2. Pool the counts before dividing
risk_before = before["y"].sum() / len(before)
risk_after = after["y"].sum() / len(after)
print("Before:", before["y"].sum(), "/", len(before), "=", round(100 * risk_before, 1), "%")
print("After:", after["y"].sum(), "/", len(after), "=", round(100 * risk_after, 1), "%")
print("After/before ratio:", round(risk_after / risk_before, 2))
'''

C_DID = '''# 1. The four risks: adopting clinics (month 13) and comparison clinics (month 19), before and after
comparison = df[df["clinic_start_month"] == 19]
a0 = adopters[adopters["month"].between(1, 6)]["y"].mean()
a1 = adopters[adopters["month"].between(13, 18)]["y"].mean()
b0 = comparison[comparison["month"].between(1, 6)]["y"].mean()
b1 = comparison[comparison["month"].between(13, 18)]["y"].mean()
print("Adopting clinics:", round(100 * a0, 1), "%,", round(100 * a1, 1), "%")
print("Comparison clinics:", round(100 * b0, 1), "%,", round(100 * b1, 1), "%")

# 2. Difference in differences = change of the adopting clinics minus change of the comparison clinics
print("Changes:", round(100 * (a1 - a0), 1), ",", round(100 * (b1 - b0), 1), "points")
print("Difference in differences:", round(100 * ((a1 - a0) - (b1 - b0)), 1), "points")

# 3. The path assumed without adoption and the ratio of ratios
print("Assumed endpoint without adoption:", round(100 * (a0 + b1 - b0), 1), "%")
print("Ratio of ratios:", round((a1 / a0) / (b1 / b0), 2))
'''

C_ITS = '''# 1. Monthly counts for the clinics that adopted in month 13
monthly = adopters.groupby("month")["y"].agg(["sum", "size"])

# 2. Number of months before, during the trial, and after adoption
print("Months before the trial:", (monthly.index < 7).sum())
print("Trial months:", ((monthly.index >= 7) & (monthly.index <= 12)).sum())
print("Months after adoption:", (monthly.index >= 13).sum())

# 3. The first monthly risk, with its own denominator
first = monthly.iloc[0]
print("First month:", first["sum"], "/", first["size"], "=", round(100 * first["sum"] / first["size"], 1), "%")
'''

EX1 = C_BALANCE
EX3 = '''# 1. The risks, the difference, and the ratio with their intervals (as in section 10.4.2)
single = trial[trial["allocated"] == "single pill"]
separate = trial[trial["allocated"] == "separate tablets"]
a, n = single["y"].sum(), len(single)
b, m = separate["y"].sum(), len(separate)
p = a / n
q = b / m
d = 100 * (p - q)
se = 100 * sqrt(p * (1 - p) / n + q * (1 - q) / m)
se_log = sqrt(1 / a - 1 / n + 1 / b - 1 / m)
print("Risks:", round(p, 4), ",", round(q, 4))
print("Difference:", round(d, 1), "; 95% CI", round(d - z * se, 1), "to", round(d + z * se, 1))
print("Ratio:", round(p / q, 2), "; 95% CI", round(exp(log(p / q) - z * se_log), 2), "to", round(exp(log(p / q) + z * se_log), 2))

# 2. How many adults received what they were assigned
matches = (trial["allocated"] == "single pill") == (trial["received"] == "yes")
print("Receipt matches assignment in", matches.sum(), "of", len(trial), "adults")
'''
EX6 = '''# 1. Each clinic in months 13-18: uncontrolled adults, adults, and risk
table = rollout.groupby(["allocated", "clinic"])["y"].agg(["sum", "size"])
table.columns = ["uncontrolled", "patients"]
table["risk (%)"] = round(100 * table["uncontrolled"] / table["patients"], 1)
display(table)

# 2. The Welch interval of the equal-clinic difference (as in section 10.6.1)
print("Difference:", round(d_clinic, 1), "; 95% CI", round(d_clinic - cut * se_clinic, 1), "to", round(d_clinic + cut * se_clinic, 1))
'''
EX7 = '''# 1. Months 1-6 and months 19-24 for the whole service
periods = [("months 1-6", df[df["month"].between(1, 6)]), ("months 19-24", df[df["month"].between(19, 24)])]

# 2. In each period: adults, uncontrolled, and those who received the single pill
for name, rows_in_period in periods:
    n = len(rows_in_period)
    uncontrolled = rows_in_period["y"].sum()
    uptake = (rows_in_period["received"] == "yes").sum()
    print(name + ": uncontrolled", uncontrolled, "/", n, "=", round(100 * uncontrolled / n, 1), "%; uptake", uptake, "/", n, "=", round(100 * uptake / n, 1), "%")
'''
EX8 = '''# 1. The stepped-wedge contrast (section 10.6.2) and the cluster comparison of months 13-18 pooled by patient
print("Stepped-wedge contrast:", round(100 * (change_late - change_early), 1), "points")
print("Cluster comparison (pooled by patient):", round(100 * (early_first - late_first), 1), "points")
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

    sec("10.1", "Introduction: the data", "Introdução: os dados")
    cell(LOAD)
    sec("10.2", "The comparison and the outcome risk", "A comparação e o risco do desfecho",
        "What exactly is compared, and what is the risk of uncontrolled pressure in the trial?",
        "O que exatamente é comparado e qual é o risco de pressão não controlada no ensaio?")
    cell(C_COMPARISON)
    sec("10.3.1", "Randomization and baseline balance", "Randomização e equilíbrio basal",
        "How can the two groups be made comparable and kept so?", "Como tornar os dois grupos comparáveis e mantê-los assim?")
    cell(C_BALANCE)
    sec("10.4.2", "Intention to treat and uncertainty", "Intenção de tratar e incerteza",
        "How is the trial analyzed, and what does its difference mean?", "Como o ensaio é analisado e o que significa sua diferença?")
    cell(C_ITT)
    sec("10.4.3", "Per-protocol questions and treatment received", "Perguntas por protocolo e tratamento recebido")
    cell(C_PERPROTOCOL)
    sec("10.5.3", "Superiority, noninferiority, and equivalence", "Superioridade, não inferioridade e equivalência",
        "Which other designs could have answered the director's question?", "Que outros delineamentos poderiam responder à pergunta do diretor?")
    cell(C_NI)
    sec("10.6.1", "Cluster-randomized trials", "Ensaios randomizados por conglomerados",
        "Can the clinics themselves be assigned at random, even in steps?", "Os próprios ambulatórios podem ser alocados ao acaso, até em etapas?")
    cell(C_CLUSTER)
    sec("10.6.2", "Stepped-wedge cluster trials", "Ensaios por conglomerados em degraus escalonados")
    cell(C_STEPPED)
    sec("10.7.1", "Before-and-after comparisons and secular trends", "Comparações antes e depois e tendências seculares",
        "What can the records show without random assignment?", "O que os registros mostram sem alocação aleatória?")
    cell(C_BEFORE)
    sec("10.7.2", "Controlled comparisons and difference in differences", "Comparações controladas e diferença em diferenças")
    cell(C_DID)
    sec("10.7.3", "Interrupted time series", "Série temporal interrompida")
    cell(C_ITS)
    exs = [("Baseline balance", "Equilíbrio basal", EX1), ("Assignment and adherence questions", "Perguntas sobre alocação e adesão", EX3),
           ("Clinics within the allocated groups", "Ambulatórios dentro dos grupos alocados", EX6),
           ("The whole-service change", "A mudança no serviço inteiro", EX7),
           ("The stepped-wedge contrast against the cluster comparison", "O contraste em degraus escalonados contra a comparação por conglomerados", EX8)]
    nums = [1, 3, 6, 7, 8]
    return S, [(nums[i], T(a, b), code(c)) for i, (a, b, c) in enumerate(exs)]

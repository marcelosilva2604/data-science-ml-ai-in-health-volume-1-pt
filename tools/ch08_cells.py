"""All code cells of the Chapter 8 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions (the two-by-two table and the
risk ratio are computed inline each time). The book draws the figures; the notebook prints the same numbers. The Portuguese cell is the same code with the comments
and printed text translated through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the population of 24,000 operations in 12 hospitals (blank registry fields are kept as empty text, not as missing values)", "# 1. Ler a população de 24.000 operações em 12 hospitais (campos em branco do registro ficam como texto vazio, não como valores faltantes)"),
 ("Operations:", "Operações:"),
 ("; share followed by infection within 30 days:", "; proporção seguida de infecção em 30 dias:"),
 ("# 2. The 12 hospitals: share of contaminated operations and month of adoption of the bundle (empty when it was never adopted)", "# 2. Os 12 hospitais: proporção de operações contaminadas e mês de adoção do pacote (vazio quando nunca foi adotado)"),
 ("# 1. One row per hospital: the share of contaminated operations, of patients with the bundle, and of infections (in %)", "# 1. Uma linha por hospital: a proporção de operações contaminadas, de pacientes com o pacote e de infecções (em %)"),
 ("# 2. The correlation across hospitals between the bundle share and the infection share", "# 2. A correlação entre hospitais da proporção com o pacote e da proporção de infecções"),
 ("Correlation between the bundle share and the infection share:", "Correlação entre a proporção com o pacote e a proporção de infecções:"),
 ("# 1. The cohort: the operations on or after the month each hospital adopted the bundle (99 for the three that never did)", "# 1. A coorte: as operações a partir do mês em que cada hospital adotou o pacote (99 para os três que nunca adotaram)"),
 ("# 2. The two-by-two table of the bundle and infection in the cohort, and the risk ratio of the bundle", "# 2. A tabela dois por dois do pacote e da infecção na coorte e a razão de riscos do pacote"),
 ("Operations in the cohort:", "Operações na coorte:"),
 ("; cells a, b, c, d:", "; células a, b, c, d:"),
 ("; risk ratio:", "; razão de riscos:"),
 ("# 3. The risk ratio of the bundle within each combination of surgery class and diabetes", "# 3. A razão de riscos do pacote dentro de cada combinação de classe de cirurgia e diabetes"),
 ("\"Class\"", "\"Classe\""),
 ("\"; diabetes\"", "\"; diabetes\""),
 ("\": risk ratio\"", "\": razão de riscos\""),
 ("# 4. Only the patients with complete follow-up: the cells and the risk ratio", "# 4. Só os pacientes com seguimento completo: as células e a razão de riscos"),
 ("Complete records:", "Registros completos:"),
 ("# 5. The share of patients with and without complete follow-up, by bundle and infection", "# 5. A proporção de pacientes sem e com seguimento completo, por pacote e infecção"),
 ("# 1. All the cases of infection in the cohort, and two controls per case drawn from the cohort patients without infection (seed 8)", "# 1. Todos os casos de infecção na coorte e dois controles por caso sorteados entre os pacientes da coorte sem infecção (semente 8)"),
 ("Cases:", "Casos:"),
 ("; odds ratio:", "; razão de chances:"),
 ("# 2. The invalid comparison: the same number of controls drawn from the whole population, hospitals that never adopted the bundle included", "# 2. A comparação inválida: o mesmo número de controles sorteados da população inteira, incluindo hospitais que nunca adotaram o pacote"),
 ("Invalid controls - cells a, b, c, d:", "Controles inválidos - células a, b, c, d:"),
 ("# 1. Recode every blank of the registry bundle field as \"no\", and count the blanks first (the silent decision made visible)", "# 1. Recodificar todo branco do campo de pacote do registro como \"no\", contando antes os brancos (a decisão silenciosa tornada visível)"),
 ("Blank fields:", "Campos em branco:"),
 ("; share of blanks among the patients who did receive the bundle:", "; proporção de brancos entre os pacientes que receberam o pacote:"),
 ("# 2. The risk ratio of the bundle with the registry field", "# 2. A razão de riscos do pacote com o campo do registro"),
 ("Risk ratio with the registry field:", "Razão de riscos com o campo do registro:"),
 ("# 1. The risk ratio of smoking for infection in the whole population, with true smoking and with reported smoking", "# 1. A razão de riscos do tabagismo para infecção na população inteira, com o tabagismo verdadeiro e com o relatado"),
 ("Risk ratio of smoking, using", "Razão de riscos do tabagismo, usando"),
 ("# 2. True against reported smoking: the misclassification table that an investigator does not see", "# 2. Tabagismo verdadeiro contra relatado: a tabela de classificação errada que um investigador não vê"),
 ("# 3. The risk ratio of the bundle in the cohort with the infection classified by assessor A", "# 3. A razão de riscos do pacote na coorte com a infecção classificada pelo avaliador A"),
 ("Risk ratio of the bundle with assessor A:", "Razão de riscos do pacote com o avaliador A:"),
 ("# 1. The table of the two assessors, and the observed agreement", "# 1. A tabela dos dois avaliadores e a concordância observada"),
 ("# 2. The agreement expected by chance from the marginal proportions of each assessor, and kappa", "# 2. A concordância esperada ao acaso a partir das proporções marginais de cada avaliador e o kappa"),
 ("Observed agreement:", "Concordância observada:"),
 ("; expected by chance:", "; esperada ao acaso:"),
 ("# 3. The validity of assessor A against the known infection status: sensitivity and specificity", "# 3. A validade do avaliador A contra a situação de infecção conhecida: sensibilidade e especificidade"),
 ("Sensitivity of assessor A:", "Sensibilidade do avaliador A:"),
 ("; specificity:", "; especificidade:"),
 ("# 1. Paired glucose readings: the meter and the laboratory", "# 1. Leituras pareadas de glicose: o glicosímetro e o laboratório"),
 ("Correlation between the laboratory and the meter:", "Correlação entre o laboratório e o glicosímetro:"),
 ("# 2. Bland-Altman: the mean difference and the limits of agreement (mean plus or minus 1.96 standard deviations)", "# 2. Bland-Altman: a diferença média e os limites de concordância (média mais ou menos 1,96 desvio padrão)"),
 ("Mean difference:", "Diferença média:"),
 ("; standard deviation:", "; desvio padrão:"),
 ("; limits:", "; limites:"),
 ("\"to\"", "\"a\""),
 ("# 1. Across hospitals: the correlation between the diabetes share and the infection share", "# 1. Entre hospitais: a correlação entre a proporção com diabetes e a proporção de infecções"),
 ("Correlation across hospitals:", "Correlação entre hospitais:"),
 ("# 2. Within patients: the risk ratio of diabetes for infection", "# 2. Entre pacientes: a razão de riscos do diabetes para infecção"),
 ("Risk ratio of diabetes:", "Razão de riscos do diabetes:"),
 ("# 1. The risk ratio of the bundle within each hospital of the cohort", "# 1. A razão de riscos do pacote dentro de cada hospital da coorte"),
 ("\"Hospital\"", "\"Hospital\""),
 ("# 1. Trace half of the patients lost to follow-up (seed 8) and add them to the complete records", "# 1. Rastrear metade dos pacientes perdidos no seguimento (semente 8) e juntá-los aos registros completos"),
 ("# 2. The risk ratio of the bundle among the known records", "# 2. A razão de riscos do pacote entre os registros conhecidos"),
 ("Known records:", "Registros conhecidos:"),
 ("# 1. Recode the blank registry field as \"no\" and then as \"yes\", and compare the risk ratios of the bundle", "# 1. Recodificar o campo em branco do registro como \"no\" e depois como \"yes\", e comparar as razões de riscos do pacote"),
 ("Blanks recoded as", "Brancos recodificados como"),
 ("# 1. Forty milligrams added to every meter reading: the correlation, the mean difference, and the limits of agreement", "# 1. Quarenta miligramas somados a cada leitura do glicosímetro: a correlação, a diferença média e os limites de concordância"),
 ("Correlation:", "Correlação:"),
 ("; mean difference:", "; diferença média:"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


LOAD = '''# 1. Read the population of 24,000 operations in 12 hospitals (blank registry fields are kept as empty text, not as missing values)
import pandas as pd

df = pd.read_csv("data/population.csv", keep_default_na=False)
print("Operations:", len(df), "; share followed by infection within 30 days:", round((df["ssi_30d"] == "yes").mean(), 4))

# 2. The 12 hospitals: share of contaminated operations and month of adoption of the bundle (empty when it was never adopted)
hosp = pd.read_csv("data/hospitals.csv", keep_default_na=False)
print(hosp.to_string(index=False))
'''

ECO = '''# 1. One row per hospital: the share of contaminated operations, of patients with the bundle, and of infections (in %)
flags = pd.DataFrame({"hospital": df["hospital"],
                      "contaminated": df["surgery_class"] == "contaminated",
                      "bundle": df["bundle"] == "yes",
                      "infection": df["ssi_30d"] == "yes"})
by_hospital = flags.groupby("hospital").mean()
print((100 * by_hospital).round(1).head(3))

# 2. The correlation across hospitals between the bundle share and the infection share
print("Correlation between the bundle share and the infection share:", round(by_hospital["bundle"].corr(by_hospital["infection"]), 2))
'''

COHORT1 = '''# 1. The cohort: the operations on or after the month each hospital adopted the bundle (99 for the three that never did)
adopt = {}
for row in hosp.itertuples():
    if row.bundle_adoption_month:
        adopt[row.hospital] = int(row.bundle_adoption_month)
    else:
        adopt[row.hospital] = 99
cohort = df[df["month"] >= df["hospital"].map(adopt)]

# 2. The two-by-two table of the bundle and infection in the cohort, and the risk ratio of the bundle
t = pd.crosstab(cohort["bundle"], cohort["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
a, b = t.loc["yes"]
c, d = t.loc["no"]
risk_ratio = (a / (a + b)) / (c / (c + d))
print("Operations in the cohort:", len(cohort), "; cells a, b, c, d:", int(a), int(b), int(c), int(d), "; risk ratio:", round(risk_ratio, 2))

# 3. The risk ratio of the bundle within each combination of surgery class and diabetes
for cls in ["clean", "contaminated"]:
    for dm in ["yes", "no"]:
        stratum = cohort[(cohort["surgery_class"] == cls) & (cohort["diabetes"] == dm)]
        t = pd.crosstab(stratum["bundle"], stratum["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
        a, b = t.loc["yes"]
        c, d = t.loc["no"]
        print("Class", cls, "; diabetes", dm, ": risk ratio", round((a / (a + b)) / (c / (c + d)), 2))
'''

COHORT2 = '''# 4. Only the patients with complete follow-up: the cells and the risk ratio
complete = cohort[cohort["followup_complete"] == "yes"]
t = pd.crosstab(complete["bundle"], complete["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
a, b = t.loc["yes"]
c, d = t.loc["no"]
print("Complete records:", len(complete), "; cells a, b, c, d:", int(a), int(b), int(c), int(d), "; risk ratio:", round((a / (a + b)) / (c / (c + d)), 2))

# 5. The share of patients with and without complete follow-up, by bundle and infection
lost = pd.crosstab([cohort["bundle"], cohort["ssi_30d"]], cohort["followup_complete"], normalize="index")
print(lost.round(3))
'''

CC = '''# 1. All the cases of infection in the cohort, and two controls per case drawn from the cohort patients without infection (seed 8)
cases = cohort[cohort["ssi_30d"] == "yes"]
controls = cohort[cohort["ssi_30d"] == "no"].sample(n=2 * len(cases), random_state=8)
sample = pd.concat([cases, controls])
t = pd.crosstab(sample["bundle"], sample["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
a, b = t.loc["yes"]
c, d = t.loc["no"]
print("Cases:", len(cases), "; cells a, b, c, d:", int(a), int(b), int(c), int(d), "; odds ratio:", round(a * d / (b * c), 2))

# 2. The invalid comparison: the same number of controls drawn from the whole population, hospitals that never adopted the bundle included
wrong = df[df["ssi_30d"] == "no"].sample(n=2 * len(cases), random_state=8)
sample = pd.concat([cases, wrong])
t = pd.crosstab(sample["bundle"], sample["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
a, b = t.loc["yes"]
c, d = t.loc["no"]
print("Invalid controls - cells a, b, c, d:", int(a), int(b), int(c), int(d), "; odds ratio:", round(a * d / (b * c), 2))
'''

REG = '''# 1. Recode every blank of the registry bundle field as "no", and count the blanks first (the silent decision made visible)
registry = cohort.copy()
registry["bundle_registry"] = registry["bundle_recorded"].replace("", "no")
print("Blank fields:", (cohort["bundle_recorded"] == "").sum(), "; share of blanks among the patients who did receive the bundle:", round((cohort.loc[cohort["bundle"] == "yes", "bundle_recorded"] == "").mean(), 3))

# 2. The risk ratio of the bundle with the registry field
t = pd.crosstab(registry["bundle_registry"], registry["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
a, b = t.loc["yes"]
c, d = t.loc["no"]
print("Risk ratio with the registry field:", round((a / (a + b)) / (c / (c + d)), 2))
'''

BIAS = '''# 1. The risk ratio of smoking for infection in the whole population, with true smoking and with reported smoking
for column in ["smoker", "smoker_reported"]:
    t = pd.crosstab(df[column], df["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
    a, b = t.loc["yes"]
    c, d = t.loc["no"]
    print("Risk ratio of smoking, using", column + ":", round((a / (a + b)) / (c / (c + d)), 2))

# 2. True against reported smoking: the misclassification table that an investigator does not see
print(pd.crosstab(df["smoker"], df["smoker_reported"]))

# 3. The risk ratio of the bundle in the cohort with the infection classified by assessor A
assessed = cohort.assign(ssi_30d=cohort["ssi_assessor_a"])
t = pd.crosstab(assessed["bundle"], assessed["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
a, b = t.loc["yes"]
c, d = t.loc["no"]
print("Risk ratio of the bundle with assessor A:", round((a / (a + b)) / (c / (c + d)), 2))
'''

KAPPA = '''# 1. The table of the two assessors, and the observed agreement
t = pd.crosstab(df["ssi_assessor_a"], df["ssi_assessor_b"]).loc[["yes", "no"], ["yes", "no"]]
print(t)
n = len(df)
p_o = (t.loc["yes", "yes"] + t.loc["no", "no"]) / n

# 2. The agreement expected by chance from the marginal proportions of each assessor, and kappa
row = t.sum(axis=1) / n
col = t.sum(axis=0) / n
p_e = row["yes"] * col["yes"] + row["no"] * col["no"]
print("Observed agreement:", round(p_o, 3), "; expected by chance:", round(p_e, 3), "; kappa:", round((p_o - p_e) / (1 - p_e), 2))

# 3. The validity of assessor A against the known infection status: sensitivity and specificity
v = pd.crosstab(df["ssi_assessor_a"], df["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
print("Sensitivity of assessor A:", round(v.loc["yes", "yes"] / v["yes"].sum(), 3), "; specificity:", round(v.loc["no", "no"] / v["no"].sum(), 3))
'''

BA = '''# 1. Paired glucose readings: the meter and the laboratory
g = pd.read_csv("data/glucose_pairs.csv")
diff = g["glucose_meter"] - g["glucose_lab"]
print("Correlation between the laboratory and the meter:", round(g["glucose_lab"].corr(g["glucose_meter"]), 2))

# 2. Bland-Altman: the mean difference and the limits of agreement (mean plus or minus 1.96 standard deviations)
print("Mean difference:", round(diff.mean(), 1), "; standard deviation:", round(diff.std(), 1), "; limits:", round(diff.mean() - 1.96 * diff.std(), 1), "to", round(diff.mean() + 1.96 * diff.std(), 1))
'''

EX3 = '''# 1. Across hospitals: the correlation between the diabetes share and the infection share
flags = pd.DataFrame({"hospital": df["hospital"], "diabetes": df["diabetes"] == "yes", "infection": df["ssi_30d"] == "yes"})
by_h = flags.groupby("hospital").mean()
print("Correlation across hospitals:", round(by_h["diabetes"].corr(by_h["infection"]), 2))

# 2. Within patients: the risk ratio of diabetes for infection
t = pd.crosstab(df["diabetes"], df["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
print("Risk ratio of diabetes:", round((t.loc["yes", "yes"] / t.loc["yes"].sum()) / (t.loc["no", "yes"] / t.loc["no"].sum()), 2))
'''

EX4 = '''# 1. The risk ratio of the bundle within each hospital of the cohort
for h in sorted(cohort["hospital"].unique()):
    sub = cohort[cohort["hospital"] == h]
    t = pd.crosstab(sub["bundle"], sub["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
    print("Hospital", h + ": risk ratio", round((t.loc["yes", "yes"] / t.loc["yes"].sum()) / (t.loc["no", "yes"] / t.loc["no"].sum()), 2))
'''

EX5 = '''# 1. Trace half of the patients lost to follow-up (seed 8) and add them to the complete records
lost = cohort[cohort["followup_complete"] == "no"]
traced = lost.sample(frac=0.5, random_state=8)
known = pd.concat([cohort[cohort["followup_complete"] == "yes"], traced])

# 2. The risk ratio of the bundle among the known records
t = pd.crosstab(known["bundle"], known["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
print("Known records:", len(known), "; risk ratio:", round((t.loc["yes", "yes"] / t.loc["yes"].sum()) / (t.loc["no", "yes"] / t.loc["no"].sum()), 2))
'''

EX7 = '''# 1. Recode the blank registry field as "no" and then as "yes", and compare the risk ratios of the bundle
registry = cohort.copy()
for value in ["no", "yes"]:
    registry["b"] = registry["bundle_recorded"].replace("", value)
    t = pd.crosstab(registry["b"], registry["ssi_30d"]).loc[["yes", "no"], ["yes", "no"]]
    print("Blanks recoded as", value + ": risk ratio", round((t.loc["yes", "yes"] / t.loc["yes"].sum()) / (t.loc["no", "yes"] / t.loc["no"].sum()), 2))
'''

EX10 = '''# 1. Forty milligrams added to every meter reading: the correlation, the mean difference, and the limits of agreement
meter = g["glucose_meter"] + 40
diff = meter - g["glucose_lab"]
print("Correlation:", round(g["glucose_lab"].corr(meter), 2), "; mean difference:", round(diff.mean(), 1), "; standard deviation:", round(diff.std(), 1), "; limits:", round(diff.mean() - 1.96 * diff.std(), 1), "to", round(diff.mean() + 1.96 * diff.std(), 1))
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

    sec("8.3", "The population we built", "A população que construímos", "How many operations, how many infections, and when did each hospital adopt the bundle?", "Quantas operações, quantas infecções e quando cada hospital adotou o pacote?")
    cell(LOAD)
    sec("8.5", "The ecological study", "O estudo ecológico", "Do the hospitals that adopted the bundle have more or fewer infections?", "Os hospitais que adotaram o pacote têm mais ou menos infecções?")
    cell(ECO)
    sec("8.6", "The cohort study", "O estudo de coorte", "Among the patients followed from the adoption of the bundle, is it associated with fewer infections?", "Entre os pacientes acompanhados desde a adoção do pacote, ele se associa a menos infecções?")
    cell(COHORT1)
    cell(COHORT2)
    sec("8.7", "The case-control study", "O estudo de caso-controle", "What does a case-control study of the same data give, and what if the controls come from the wrong source?", "O que um estudo de caso-controle dos mesmos dados fornece, e e se os controles vierem da fonte errada?")
    cell(CC)
    sec("8.8", "Real-world data and registries", "Dados do mundo real e registros", "What happens when the blanks of a registry are read as no treatment?", "O que acontece quando os brancos de um registro são lidos como ausência de tratamento?")
    cell(REG)
    sec("8.9", "The three families of systematic error", "As três famílias de erro sistemático", "How do selection, information, and confounding change the estimate?", "Como seleção, informação e confusão mudam a estimativa?")
    cell(BIAS)
    sec("8.11", "Agreement between raters: percent agreement and kappa", "Concordância entre avaliadores: concordância percentual e kappa", "How well do two assessors agree, and how valid is each?", "Quão bem dois avaliadores concordam, e quão válido é cada um?")
    cell(KAPPA)
    sec("8.12", "Agreement between methods: Bland-Altman analysis", "Concordância entre métodos: análise de Bland-Altman", "Do the glucose meter and the laboratory agree?", "O glicosímetro e o laboratório concordam?")
    cell(BA)
    exs = [(3, "", EX3), (4, "", EX4), (5, "", EX5), (7, "", EX7), (10, "", EX10)]
    return S, [(k, title, code(block)) for k, title, block in exs]

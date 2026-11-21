"""All code cells of the Chapter 6 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions. The book draws the
figures; the notebook prints the same numbers. The Portuguese cell is the same code with the comments and printed text translated through the TR table
(exact substrings, longest first)."""

TR = [
 ("# 1. Read the March triage log: one row per visit", "# 1. Ler o registro de triagem de março: uma linha por atendimento"),
 ("# 2. The contingency table of arrival route and admission, with the totals (margins)", "# 2. A tabela de contingência de via de chegada e internação, com os totais (margens)"),
 ("# 3. Row profiles: the percentage of each row (arrival route) that falls in each column", "# 3. Perfis das linhas: a porcentagem de cada linha (via de chegada) que cai em cada coluna"),
 ("# 1. Counts of each arrival route by admission, admitted visits first (the book draws the grouped bars)", "# 1. Contagens de cada via de chegada por internação, internados primeiro (o livro desenha as barras agrupadas)"),
 ("# 2. Row profiles in %, which scale every stacked bar to 100 (the book draws the stacked bars)", "# 2. Perfis das linhas em %, que levam cada barra empilhada a 100 (o livro desenha as barras empilhadas)"),
 ("# 1. Expected counts if arrival route and admission were independent, and the chi-square statistic (no continuity correction)", "# 1. Contagens esperadas se via de chegada e internação fossem independentes, e a estatística qui-quadrado (sem correção de continuidade)"),
 ("Expected counts (columns: discharged, admitted):", "Contagens esperadas (colunas: alta, internado):"),
 ("# 2. Chi-square and Cramer's V for arrival route", "# 2. Qui-quadrado e V de Cramér para a via de chegada"),
 ("Arrival route: chi-square", "Via de chegada: qui-quadrado"),
 ("; Cramer's V", "; V de Cramér"),
 ("# 3. The same for triage level and admission", "# 3. O mesmo para o nível de triagem e a internação"),
 ("Triage level: chi-square", "Nível de triagem: qui-quadrado"),
 ("# 1. Row profiles of arrival route by triage level, and the share of each triage level in the whole log", "# 1. Perfis das linhas da via de chegada por nível de triagem e a participação de cada nível de triagem no registro inteiro"),
 ("# 2. Chi-square distance between the profiles of walk-in (1) and ambulance (2) visits, and the total inertia (chi-square divided by n)", "# 2. Distância qui-quadrado entre os perfis dos atendimentos de demanda espontânea (1) e de ambulância (2) e a inércia total (qui-quadrado dividido por n)"),
 ("Distance between the walk-in and ambulance profiles:", "Distância entre os perfis de demanda espontânea e ambulância:"),
 ("; total inertia:", "; inércia total:"),
 ("# 3. Correspondence analysis by hand: standardized residuals and their singular value decomposition", "# 3. Análise de correspondência à mão: resíduos padronizados e sua decomposição em valores singulares"),
 ("# 4. The share of the inertia carried by each axis, and the distance between walk-in and ambulance on the map", "# 4. A parte da inércia carregada por cada eixo e a distância entre demanda espontânea e ambulância no mapa"),
 ("Inertia carried by the first and second axes (%):", "Inércia carregada pelo primeiro e pelo segundo eixo (%):"),
 ("Distance between walk-in and ambulance on the map:", "Distância entre demanda espontânea e ambulância no mapa:"),
 ("# 1. Age by admission status: count, mean, standard deviation, and median (the book draws the boxplots)", "# 1. Idade por situação de internação: contagem, média, desvio padrão e mediana (o livro desenha os boxplots)"),
 ("# 2. Heart rate: the three quartiles in each group", "# 2. Frequência cardíaca: os três quartis em cada grupo"),
 ("# 1. Heart rate and temperature in classes (the book draws the scatter plot): the count of each combination", "# 1. Frequência cardíaca e temperatura em classes (o livro desenha o diagrama de dispersão): a contagem de cada combinação"),
 ("Counts by heart-rate class (rows) and temperature class (columns):", "Contagens por classe de frequência cardíaca (linhas) e de temperatura (colunas):"),
 ("# 1. Sample covariance of heart rate and temperature: the first eight visits (hand calculation) and the full month", "# 1. Covariância amostral de frequência cardíaca e temperatura: os oito primeiros atendimentos (cálculo manual) e o mês inteiro"),
 ("Covariance, first eight visits:", "Covariância, oito primeiros atendimentos:"),
 ("Covariance, full month:", "Covariância, mês inteiro:"),
 ("# 1. Pearson correlation of heart rate and temperature: the first eight visits and the full month", "# 1. Correlação de Pearson de frequência cardíaca e temperatura: os oito primeiros atendimentos e o mês inteiro"),
 ("Correlation, first eight visits:", "Correlação, oito primeiros atendimentos:"),
 ("Correlation, full month:", "Correlação, mês inteiro:"),
 ("# 2. The correlation matrix of age, heart rate, and temperature", "# 2. A matriz de correlações de idade, frequência cardíaca e temperatura"),
 ("# 1. Pain categories as codes in the order of the scale (only to rank them; the steps are not claimed to be equal)", "# 1. Categorias de dor como códigos na ordem da escala (só para ordená-las; não se afirma que os degraus sejam iguais)"),
 ("# 2. Spearman correlation of triage level with pain: the first eight visits and the full month", "# 2. Correlação de Spearman do nível de triagem com a dor: os oito primeiros atendimentos e o mês inteiro"),
 ("Spearman, triage level and pain, first eight visits:", "Spearman, nível de triagem e dor, oito primeiros atendimentos:"),
 ("Spearman, triage level and pain, full month:", "Spearman, nível de triagem e dor, mês inteiro:"),
 ("# 3. Spearman correlation of triage level with heart rate", "# 3. Correlação de Spearman do nível de triagem com a frequência cardíaca"),
 ("Spearman, triage level and heart rate:", "Spearman, nível de triagem e frequência cardíaca:"),
 ("# 1. Row profiles (%) of admission by pain, in the order of the scale", "# 1. Perfis das linhas (%) da internação por dor, na ordem da escala"),
 ("# 1. Chi-square and Cramer's V of pain and of triage level against admission", "# 1. Qui-quadrado e V de Cramér da dor e do nível de triagem contra a internação"),
 ("col + \": chi-square\"", "col + \": qui-quadrado\""),
 ("# 1. Temperature by admission status: mean and standard deviation", "# 1. Temperatura por situação de internação: média e desvio padrão"),
 ("# 2. Pain by admission status: counts and percentages of each column", "# 2. Dor por situação de internação: contagens e porcentagens de cada coluna"),
 ("\"Pain\"", "\"Dor\""),
 ("\"%); discharged\"", "\"%); alta\""),
 ("\": admitted\"", "\": internados\""),
 ("# 1. Waiting time in minutes, and the correlation matrix of age, heart rate, temperature, and waiting time", "# 1. Tempo de espera em minutos e a matriz de correlações de idade, frequência cardíaca, temperatura e tempo de espera"),
 ("# 2. Spearman correlation of triage level with waiting time", "# 2. Correlação de Spearman do nível de triagem com o tempo de espera"),
 ("Spearman, triage level and waiting time:", "Spearman, nível de triagem e tempo de espera:"),
 ("# 1. Temperature in Fahrenheit, and the covariance and correlation of heart rate with each unit", "# 1. Temperatura em Fahrenheit e a covariância e a correlação da frequência cardíaca com cada unidade"),
 ("Covariance, Celsius:", "Covariância, Celsius:"),
 ("; Fahrenheit:", "; Fahrenheit:"),
 ("Correlation, Celsius:", "Correlação, Celsius:"),
 ("# 1. Distance between the profiles of transfer (3) and walk-in (1) visits by triage level", "# 1. Distância entre os perfis dos atendimentos de transferência (3) e de demanda espontânea (1) por nível de triagem"),
 ("Distance between the transfer and walk-in profiles:", "Distância entre os perfis de transferência e demanda espontânea:"),
 ("# 1. Joint classes of heart rate and temperature", "# 1. Classes conjuntas de frequência cardíaca e temperatura"),
 ("Counts:", "Contagens:"),
 ("# 2. The share of each heart-rate class with a temperature of 38 or more (%)", "# 2. A parte de cada classe de frequência cardíaca com temperatura de 38 ou mais (%)"),
 ("Share with temperature of 38 or more, by heart-rate class (%):", "Parte com temperatura de 38 ou mais, por classe de frequência cardíaca (%):"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


CT = '''# 1. Read the March triage log: one row per visit
import pandas as pd

df = pd.read_csv("data/triage_month.csv")

# 2. The contingency table of arrival route and admission, with the totals (margins)
table = pd.crosstab(df["arrival_route"], df["admitted"], margins=True)
print(table)

# 3. Row profiles: the percentage of each row (arrival route) that falls in each column
rows = pd.crosstab(df["arrival_route"], df["admitted"], normalize="index")
print((100 * rows).round(1))
'''

GRAPH = '''# 1. Counts of each arrival route by admission, admitted visits first (the book draws the grouped bars)
counts = pd.crosstab(df["arrival_route"], df["admitted"]).reindex(columns=["yes", "no"])
print(counts)

# 2. Row profiles in %, which scale every stacked bar to 100 (the book draws the stacked bars)
profiles = 100 * pd.crosstab(df["arrival_route"], df["admitted"], normalize="index")
print(profiles.reindex(columns=["yes", "no"]).round(1))
'''

CV = '''# 1. Expected counts if arrival route and admission were independent, and the chi-square statistic (no continuity correction)
from scipy.stats import chi2_contingency

observed = pd.crosstab(df["arrival_route"], df["admitted"])
chi2, _, _, expected = chi2_contingency(observed, correction=False)
print("Expected counts (columns: discharged, admitted):")
print(expected.round(1))

# 2. Chi-square and Cramer's V for arrival route
n = len(df)
print("Arrival route: chi-square", round(chi2, 2), "; Cramer's V", round((chi2 / n) ** 0.5, 3))

# 3. The same for triage level and admission
levels = pd.crosstab(df["triage_level"], df["admitted"])
chi2_levels = chi2_contingency(levels, correction=False)[0]
print("Triage level: chi-square", round(chi2_levels, 1), "; Cramer's V", round((chi2_levels / n) ** 0.5, 3))
'''

PMAP1 = '''# 1. Row profiles of arrival route by triage level, and the share of each triage level in the whole log
route_level = pd.crosstab(df["arrival_route"], df["triage_level"])
row_profiles = route_level.div(route_level.sum(axis=1), axis=0)
column_share = route_level.sum(axis=0) / len(df)

# 2. Chi-square distance between the profiles of walk-in (1) and ambulance (2) visits, and the total inertia (chi-square divided by n)
difference = row_profiles.loc[1] - row_profiles.loc[2]
distance = ((difference ** 2 / column_share).sum()) ** 0.5
chi2_map = chi2_contingency(route_level, correction=False)[0]
print("Distance between the walk-in and ambulance profiles:", round(distance, 3), "; total inertia:", round(chi2_map / len(df), 5))
'''

PMAP2 = '''# 3. Correspondence analysis by hand: standardized residuals and their singular value decomposition
import numpy as np

p = route_level.to_numpy(dtype=float) / len(df)
r = p.sum(axis=1)
c = p.sum(axis=0)
expected_share = r[:, None] * c[None, :]
s = (p - expected_share) / np.sqrt(expected_share)
u, singular, vt = np.linalg.svd(s, full_matrices=False)
row_xy = u[:, :2] * singular[:2] / np.sqrt(r[:, None])
column_xy = vt.T[:, :2] * singular[:2] / np.sqrt(c[:, None])

# 4. The share of the inertia carried by each axis, and the distance between walk-in and ambulance on the map
axis_share = 100 * singular[:2] ** 2 / (singular ** 2).sum()
print("Inertia carried by the first and second axes (%):", axis_share.round(1).tolist())
print("Distance between walk-in and ambulance on the map:", round(np.sqrt(((row_xy[0] - row_xy[1]) ** 2).sum()), 3))
'''

GROUP = '''# 1. Age by admission status: count, mean, standard deviation, and median (the book draws the boxplots)
by_group = df.groupby("admitted")
print(by_group["age_years"].agg(["count", "mean", "std", "median"]).round(1))

# 2. Heart rate: the three quartiles in each group
print(by_group["heart_rate"].quantile([0.25, 0.5, 0.75]).round(1))
'''

SCAT = '''# 1. Heart rate and temperature in classes (the book draws the scatter plot): the count of each combination
hr_class = pd.cut(df["heart_rate"], [-np.inf, 80, 100, 120, np.inf], right=False)
temp_class = pd.cut(df["temp_c"], [-np.inf, 37, 38, 39, np.inf], right=False)
joint = pd.crosstab(hr_class, temp_class)
print("Counts by heart-rate class (rows) and temperature class (columns):", joint.to_numpy().tolist())
'''

COV = '''# 1. Sample covariance of heart rate and temperature: the first eight visits (hand calculation) and the full month
first = df.head(8)
print("Covariance, first eight visits:", round(first["heart_rate"].cov(first["temp_c"]), 2))
print("Covariance, full month:", round(df["heart_rate"].cov(df["temp_c"]), 2))
'''

PEARSON = '''# 1. Pearson correlation of heart rate and temperature: the first eight visits and the full month
print("Correlation, first eight visits:", round(first["heart_rate"].corr(first["temp_c"]), 2))
print("Correlation, full month:", round(df["heart_rate"].corr(df["temp_c"]), 3))

# 2. The correlation matrix of age, heart rate, and temperature
print(df[["age_years", "heart_rate", "temp_c"]].corr().round(2))
'''

RANK = '''# 1. Pain categories as codes in the order of the scale (only to rank them; the steps are not claimed to be equal)
pain_code = df["pain"].map({"none": 0, "mild": 1, "moderate": 2, "severe": 3})

# 2. Spearman correlation of triage level with pain: the first eight visits and the full month
print("Spearman, triage level and pain, first eight visits:", round(first["triage_level"].corr(pain_code.head(8), method="spearman"), 2))
print("Spearman, triage level and pain, full month:", round(df["triage_level"].corr(pain_code, method="spearman"), 2))

# 3. Spearman correlation of triage level with heart rate
print("Spearman, triage level and heart rate:", round(df["triage_level"].corr(df["heart_rate"], method="spearman"), 2))
'''

EX2 = '''# 1. Row profiles (%) of admission by pain, in the order of the scale
order = ["none", "mild", "moderate", "severe"]
pain = pd.Categorical(df["pain"], categories=order, ordered=True)
print((100 * pd.crosstab(pain, df["admitted"], normalize="index")).round(1))
'''

EX4 = '''# 1. Chi-square and Cramer's V of pain and of triage level against admission
n = len(df)
for col in ["pain", "triage_level"]:
    chi2 = chi2_contingency(pd.crosstab(df[col], df["admitted"]), correction=False)[0]
    print(col + ": chi-square", round(chi2, 1), "; Cramer's V", round((chi2 / n) ** 0.5, 3))
'''

EX7 = '''# 1. Temperature by admission status: mean and standard deviation
temp = df.groupby("admitted")["temp_c"].agg(["mean", "std"]).round(2)
print(temp)

# 2. Pain by admission status: counts and percentages of each column
counts = pd.crosstab(pain, df["admitted"])
share = (100 * pd.crosstab(pain, df["admitted"], normalize="columns")).round(1)
for level in order:
    print("Pain", level + ": admitted", counts.loc[level, "yes"], "(" + str(share.loc[level, "yes"]) + "%); discharged", counts.loc[level, "no"], "(" + str(share.loc[level, "no"]) + "%)")
'''

EX9 = '''# 1. Waiting time in minutes, and the correlation matrix of age, heart rate, temperature, and waiting time
df["wait"] = (pd.to_datetime(df["seen_at"]) - pd.to_datetime(df["arrived_at"])).dt.total_seconds() / 60
print(df[["age_years", "heart_rate", "temp_c", "wait"]].corr().round(2))

# 2. Spearman correlation of triage level with waiting time
print("Spearman, triage level and waiting time:", round(df["triage_level"].corr(df["wait"], method="spearman"), 2))
'''

EX11 = '''# 1. Temperature in Fahrenheit, and the covariance and correlation of heart rate with each unit
temp_f = 1.8 * df["temp_c"] + 32
print("Covariance, Celsius:", round(df["heart_rate"].cov(df["temp_c"]), 2), "; Fahrenheit:", round(df["heart_rate"].cov(temp_f), 2))
print("Correlation, Celsius:", round(df["heart_rate"].corr(df["temp_c"]), 3), "; Fahrenheit:", round(df["heart_rate"].corr(temp_f), 3))
'''

EX13 = '''# 1. Distance between the profiles of transfer (3) and walk-in (1) visits by triage level
route_level = pd.crosstab(df["arrival_route"], df["triage_level"])
profiles = route_level.div(route_level.sum(axis=1), axis=0)
column_share = route_level.sum(axis=0) / len(df)
difference = profiles.loc[3] - profiles.loc[1]
print("Distance between the transfer and walk-in profiles:", round(((difference ** 2 / column_share).sum()) ** 0.5, 3))
'''

EX14 = '''# 1. Joint classes of heart rate and temperature
hr_class = pd.cut(df["heart_rate"], [-np.inf, 80, 100, 120, np.inf], right=False)
temp_class = pd.cut(df["temp_c"], [-np.inf, 37, 38, 39, np.inf], right=False)
joint = pd.crosstab(hr_class, temp_class)
print("Counts:", joint.to_numpy().tolist())

# 2. The share of each heart-rate class with a temperature of 38 or more (%)
print("Share with temperature of 38 or more, by heart-rate class (%):", (100 * joint.iloc[:, 2:].sum(axis=1) / joint.sum(axis=1)).round(1).tolist())
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

    sec("6.2", "The contingency table", "A tabela de contingência", "How does admission differ across the arrival routes?", "Como a internação difere entre as vias de chegada?")
    cell(CT)
    sec("6.3", "Graphs for two qualitative variables", "Gráficos para duas variáveis qualitativas", "How can the two variables be shown together?", "Como as duas variáveis podem ser mostradas juntas?")
    cell(GRAPH)
    sec("6.5", "Phi and Cramér's V", "Phi e V de Cramér", "How strong is the association, on a scale from 0 to 1?", "Quão forte é a associação, em uma escala de 0 a 1?")
    cell(CV)
    sec("6.6", "Perceptual maps and correspondence analysis", "Mapas perceptuais e análise de correspondência", "How can a table with many categories be drawn as a map?", "Como uma tabela com muitas categorias pode ser desenhada como um mapa?")
    cell(PMAP1)
    cell(PMAP2)
    sec("6.7", "A quantitative variable described by group", "Uma variável quantitativa descrita por grupo", "How do age and heart rate differ between admitted and discharged visits?", "Como idade e frequência cardíaca diferem entre atendimentos com internação e com alta?")
    cell(GROUP)
    sec("6.8", "The scatter plot", "O diagrama de dispersão", "How do heart rate and temperature move together?", "Como frequência cardíaca e temperatura se movem juntas?")
    cell(SCAT)
    sec("6.9", "Covariance", "Covariância", "Do heart rate and temperature rise together, and by how much?", "Frequência cardíaca e temperatura sobem juntas, e quanto?")
    cell(COV)
    sec("6.10", "Pearson's correlation coefficient", "Coeficiente de correlação de Pearson", "How strong is the linear association, free of the units?", "Quão forte é a associação linear, livre das unidades?")
    cell(PEARSON)
    sec("6.11", "Rank correlation for ordered variables", "Correlação de postos para variáveis ordenadas", "How are two ordered variables related?", "Como duas variáveis ordenadas se relacionam?")
    cell(RANK)
    exs = [(2, "", EX2), (4, "", EX4), (7, "", EX7), (9, "", EX9), (11, "", EX11), (13, "", EX13), (14, "", EX14)]
    return S, [(k, title, code(block)) for k, title, block in exs]

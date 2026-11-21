"""All code cells of the Chapter 4 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions. The chapter
teaches pandas, so pandas is used; the book draws the figures and the notebook prints the same numbers. The Portuguese cell is the same code with the
comments and printed text translated through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. The route of the standard library: a dictionary collects the stays of each ward, and every value is converted from text to a whole number", "# 1. O caminho da biblioteca padrão: um dicionário reúne as permanências de cada enfermaria, e cada valor é convertido de texto para número inteiro"),
 ("# 2. A loop averages each list", "# 2. Um laço calcula a média de cada lista"),
 ("Ward", "Enfermaria"),
 ("\"patients, mean length of stay\"", "\"pacientes, permanência média\""),
 ("\"days\")", "\"dias\")"),
 ("# 3. The route of pandas: the whole table in one object (a DataFrame), one row per patient and one column per variable", "# 3. O caminho do pandas: a tabela inteira em um objeto (um DataFrame), uma linha por paciente e uma coluna por variável"),
 ("The cohort has", "A coorte tem"),
 ("rows (one per patient) and", "linhas (uma por paciente) e"),
 ("columns.", "colunas."),
 ("Storage type of los_days:", "Tipo de armazenamento de los_days:"),
 ("; of severity:", "; de severity:"),
 ("# 4. The first three records", "# 4. Os três primeiros registros"),
 ("# 1. Frequency distribution of severity, in the order of the scale: absolute (F), relative in % (Fr), cumulative (Fac), and cumulative relative in % (Frac)", "# 1. Distribuição de frequências da gravidade, na ordem da escala: absoluta (F), relativa em % (Fr), acumulada (Fac) e relativa acumulada em % (Frac)"),
 ("# 2. Ages grouped into ten-year classes, closed on the left: 30-39, 40-49, and so on", "# 2. Idades agrupadas em classes de dez anos, fechadas à esquerda: 30-39, 40-49 e assim por diante"),
 ("Patients in each age class:", "Pacientes em cada classe de idade:"),
 ("# 1. The heights of the bars of the severity chart are the counts of each class, in the order of the scale (the book draws them)", "# 1. As alturas das barras do gráfico de gravidade são as contagens de cada classe, na ordem da escala (o livro as desenha)"),
 ("Bar heights:", "Alturas das barras:"),
 ("# 1. The bars of the wards, from the most to the least frequent (the book draws them)", "# 1. As barras das enfermarias, da mais à menos frequente (o livro as desenha)"),
 ("Patients by ward, from the most to the least frequent:", "Pacientes por enfermaria, da mais à menos frequente:"),
 ("# 1. Reasons for delay, from the most to the least frequent, and their cumulative percentages (the book draws the chart)", "# 1. Motivos de atraso, do mais ao menos frequente, e suas porcentagens acumuladas (o livro desenha o gráfico)"),
 ("Cumulative percentages:", "Porcentagens acumuladas:"),
 ("# 1. Counts of length of stay in classes of five days: 1-5, 6-10, and so on up to 66 (the book draws the histogram)", "# 1. Contagens da permanência em classes de cinco dias: 1-5, 6-10 e assim por diante até 66 (o livro desenha o histograma)"),
 ("Counts of the first six classes:", "Contagens das seis primeiras classes:"),
 ("# 1. Stem-and-leaf display of the first 30 systolic pressures: the stem is the tens, the leaf is the units", "# 1. Diagrama de ramo e folhas das 30 primeiras pressões sistólicas: o ramo é a dezena, a folha é a unidade"),
 ("# 2. One line per stem", "# 2. Uma linha por ramo"),
 ("# 1. Mean length of stay: the first ten patients (hand calculation) and the 300 patients", "# 1. Permanência média: os dez primeiros pacientes (cálculo manual) e os 300 pacientes"),
 ("Mean of the first ten stays:", "Média das dez primeiras permanências:"),
 ("\"days; of the 300 stays:\"", "\"dias; das 300 permanências:\""),
 ("# 2. By ward: the simple mean of the ward means against the weighted mean (the mean of the cohort)", "# 2. Por enfermaria: a média simples das médias das enfermarias contra a média ponderada (a média da coorte)"),
 ("Simple mean of the ward means:", "Média simples das médias das enfermarias:"),
 ("\"days; weighted mean:\"", "\"dias; média ponderada:\""),
 ("# 1. Median length of stay: the first ten patients (hand calculation) and the 300 patients", "# 1. Mediana da permanência: os dez primeiros pacientes (cálculo manual) e os 300 pacientes"),
 ("Median of the first ten stays:", "Mediana das dez primeiras permanências:"),
 ("# 2. A typing error in a copy of the column: 620 days typed instead of 62", "# 2. Um erro de digitação em uma cópia da coluna: 620 dias digitados no lugar de 62"),
 ("With the typing error: mean", "Com o erro de digitação: média"),
 ("\"days; median\"", "\"dias; mediana\""),
 ("# 3. Patients whose stays are shorter than the mean", "# 3. Pacientes cujas permanências são menores que a média"),
 ("Patients with stays shorter than the mean:", "Pacientes com permanência menor que a média:"),
 ("# 1. Admissions in each month of 2025 and their median (the book draws the line chart)", "# 1. Internações em cada mês de 2025 e sua mediana (o livro desenha o gráfico de linhas)"),
 ("Admissions by month, January to December:", "Internações por mês, de janeiro a dezembro:"),
 ("Median of the twelve monthly counts:", "Mediana das doze contagens mensais:"),
 ("# 1. The mode of the ward and of the stay (a method that returns every value tied for the highest frequency)", "# 1. A moda da enfermaria e da permanência (um método que devolve todos os valores empatados na maior frequência)"),
 ("Modal ward:", "Enfermaria modal:"),
 ("; modal length of stay:", "; permanência modal:"),
 ("# 2. The mode of a finely measured variable against its median", "# 2. A moda de uma variável medida com precisão contra a sua mediana"),
 ("Modal systolic pressure:", "Pressão sistólica modal:"),
 ("\"mmHg; median:\"", "\"mmHg; mediana:\""),
 ("\"mmHg\")", "\"mmHg\")"),
 ("# 1. Quartiles and the 90th percentile of the first ten stays (hand calculation)", "# 1. Quartis e percentil 90 das dez primeiras permanências (cálculo manual)"),
 ("First ten stays - quartile 1, quartile 3, and 90th percentile:", "Dez primeiras permanências - quartil 1, quartil 3 e percentil 90:"),
 ("# 2. The 10th, 25th, 50th, 75th, and 90th percentiles of the 300 stays", "# 2. Os percentis 10, 25, 50, 75 e 90 das 300 permanências"),
 ("300 stays - percentiles 10, 25, 50, 75, and 90:", "300 permanências - percentis 10, 25, 50, 75 e 90:"),
 ("# 1. Quartiles, interquartile range, and the two fences (1.5 and 3 times the interquartile range above the third quartile)", "# 1. Quartis, intervalo interquartil e as duas cercas (1,5 e 3 vezes o intervalo interquartil acima do terceiro quartil)"),
 ("Interquartile range:", "Intervalo interquartil:"),
 ("\"days; lower fence:\"", "\"dias; cerca inferior:\""),
 ("\"days; upper fence:\"", "\"dias; cerca superior:\""),
 ("\"days; extreme fence:\"", "\"dias; cerca extrema:\""),
 ("# 2. The upper whisker and the flagged stays", "# 2. O bigode superior e as permanências sinalizadas"),
 ("Longest stay inside the fence:", "Maior permanência dentro da cerca:"),
 ("Stays beyond the upper fence:", "Permanências além da cerca superior:"),
 ("; beyond the extreme fence:", "; além da cerca extrema:"),
 ("# 1. Skewness (adjusted for samples) of three variables: positive for a longer right tail, negative for a longer left tail", "# 1. Assimetria (ajustada para amostras) de três variáveis: positiva para cauda direita mais longa, negativa para cauda esquerda mais longa"),
 ("Skewness of", "Assimetria de"),
 ("# 1. Excess kurtosis (adjusted for samples) of the same three variables: zero for the normal distribution", "# 1. Curtose em excesso (ajustada para amostras) das mesmas três variáveis: zero para a distribuição normal"),
 ("Excess kurtosis of", "Curtose em excesso de"),
 ("# 1. Non-missing values and summary of the numeric columns of Table 1", "# 1. Valores não faltantes e resumo das colunas numéricas da Tabela 1"),
 ("Non-missing values of each column:", "Valores não faltantes de cada coluna:"),
 ("# 2. Counts and percentages of the categories", "# 2. Contagens e porcentagens das categorias"),
 ("Sex (F, M): counts", "Sexo (F, M): contagens"),
 ("; percentages", "; porcentagens"),
 ("Severity (low, moderate, high): counts", "Gravidade (baixa, moderada, alta): contagens"),
 ("# 1. C-reactive protein: summary, adjusted skewness, upper fence, and values beyond it", "# 1. Proteína C reativa: resumo, assimetria ajustada, cerca superior e valores além dela"),
 ("Adjusted skewness:", "Assimetria ajustada:"),
 ("Upper fence:", "Cerca superior:"),
 ("\"; upper fence:\"", "\"; cerca superior:\""),
 ("\"mg/L; values beyond it:\"", "\"mg/L; valores além dela:\""),
 ("# 1. Waiting times of the triage log of Chapter 3 (a copy of the file is in data/triage.csv), in minutes; visits with no time seen are left out", "# 1. Tempos de espera do registro de triagem do Capítulo 3 (há uma cópia do arquivo em data/triage.csv), em minutos; atendimentos sem horário de atendimento ficam de fora"),
 ("Known waiting times:", "Tempos de espera conhecidos:"),
 ("\"minutes; median:\"", "\"minutos; mediana:\""),
 ("\"; mean:\"", "\"; média:\""),
 ("\"minutes\")", "\"minutos\")"),
 ("# 2. Quartiles, upper fence, candidate outliers, and the 90th percentile", "# 2. Quartis, cerca superior, possíveis outliers e percentil 90"),
 ("Quartiles:", "Quartis:"),
 ("\"and\"", "\"e\""),
 ("\"minutes; waits beyond it:\"", "\"minutos; esperas além dela:\""),
 ("\"; 90th percentile:\"", "\"; percentil 90:\""),
 ("# 1. Counts and percentages of the wards, and the number of missing ward values", "# 1. Contagens e porcentagens das enfermarias e o número de valores faltantes de enfermaria"),
 ("Patients by ward:", "Pacientes por enfermaria:"),
 ("Percentages:", "Porcentagens:"),
 ("Missing ward values:", "Valores faltantes de enfermaria:"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


LOAD1 = '''# 1. The route of the standard library: a dictionary collects the stays of each ward, and every value is converted from text to a whole number
import csv

stays = {}
with open("data/cohort.csv", newline="") as file:
    for row in csv.DictReader(file):
        if row["ward"] not in stays:
            stays[row["ward"]] = []
        stays[row["ward"]].append(int(row["los_days"]))

# 2. A loop averages each list
for ward in stays:
    days = stays[ward]
    print("Ward", ward + ":", len(days), "patients, mean length of stay", round(sum(days) / len(days), 2), "days")
'''

LOAD2 = '''# 3. The route of pandas: the whole table in one object (a DataFrame), one row per patient and one column per variable
import pandas as pd

df = pd.read_csv("data/cohort.csv")
print("The cohort has", df.shape[0], "rows (one per patient) and", df.shape[1], "columns.")
print("Storage type of los_days:", df.dtypes["los_days"], "; of severity:", df.dtypes["severity"])

# 4. The first three records
print(df.head(3))
'''

FREQ = '''# 1. Frequency distribution of severity, in the order of the scale: absolute (F), relative in % (Fr), cumulative (Fac), and cumulative relative in % (Frac)
order = ["low", "moderate", "high"]
table = pd.DataFrame({"F": df["severity"].value_counts().reindex(order)})
table["Fr"] = (100 * table["F"] / len(df)).round(2)
table["Fac"] = table["F"].cumsum()
table["Frac"] = (100 * table["Fac"] / len(df)).round(2)
print(table)

# 2. Ages grouped into ten-year classes, closed on the left: 30-39, 40-49, and so on
limits = [30, 40, 50, 60, 70, 80, 90, 100]
age_class = pd.cut(df["age_years"], bins=limits, right=False)
print("Patients in each age class:", age_class.value_counts().sort_index().tolist())
'''

DRAW = '''# 1. The heights of the bars of the severity chart are the counts of each class, in the order of the scale (the book draws them)
counts = df["severity"].value_counts().reindex(order)
print("Bar heights:", counts.tolist())
'''

BAR = '''# 1. The bars of the wards, from the most to the least frequent (the book draws them)
wards_count = df["ward"].value_counts()
print("Patients by ward, from the most to the least frequent:", wards_count.tolist())
'''

PARETO = '''# 1. Reasons for delay, from the most to the least frequent, and their cumulative percentages (the book draws the chart)
reasons = pd.Series({"radiograph": 31, "not suspected": 19,
                     "late assessment": 14, "drug unavailable": 9,
                     "venous access": 6, "other": 3})
cumulative = 100 * reasons.cumsum() / reasons.sum()
print("Cumulative percentages:", cumulative.round(1).tolist())
'''

HIST = '''# 1. Counts of length of stay in classes of five days: 1-5, 6-10, and so on up to 66 (the book draws the histogram)
import numpy as np

counts, limits = np.histogram(df["los_days"], bins=range(1, 67, 5))
print("Counts of the first six classes:", counts[:6].tolist())
'''

STEM = '''# 1. Stem-and-leaf display of the first 30 systolic pressures: the stem is the tens, the leaf is the units
values = sorted(df["sbp_mmhg"].head(30))
stems = {}
for value in values:
    stem = value // 10
    if stem not in stems:
        stems[stem] = []
    stems[stem].append(value % 10)

# 2. One line per stem
for stem in sorted(stems):
    leaves = ""
    for leaf in stems[stem]:
        leaves = leaves + str(leaf) + " "
    print(str(stem).rjust(3), "|", leaves)
'''

MEAN = '''# 1. Mean length of stay: the first ten patients (hand calculation) and the 300 patients
print("Mean of the first ten stays:", df["los_days"].head(10).mean(), "days; of the 300 stays:", round(df["los_days"].mean(), 2), "days")

# 2. By ward: the simple mean of the ward means against the weighted mean (the mean of the cohort)
wards = df.groupby("ward")["los_days"].agg(["count", "mean"])
weighted = (wards["count"] * wards["mean"]).sum() / wards["count"].sum()
print("Simple mean of the ward means:", round(wards["mean"].mean(), 2), "days; weighted mean:", round(weighted, 2), "days")
'''

MEDIAN = '''# 1. Median length of stay: the first ten patients (hand calculation) and the 300 patients
print("Median of the first ten stays:", df["los_days"].head(10).median(), "days; of the 300 stays:", df["los_days"].median(), "days")

# 2. A typing error in a copy of the column: 620 days typed instead of 62
typo = df["los_days"].replace(62, 620)
print("With the typing error: mean", round(typo.mean(), 2), "days; median", typo.median(), "days")

# 3. Patients whose stays are shorter than the mean
print("Patients with stays shorter than the mean:", (df["los_days"] < df["los_days"].mean()).sum())
'''

LINE = '''# 1. Admissions in each month of 2025 and their median (the book draws the line chart)
month = pd.to_datetime(df["admitted_on"]).dt.month
monthly = month.value_counts().sort_index()
print("Admissions by month, January to December:", monthly.tolist())
print("Median of the twelve monthly counts:", monthly.median())
'''

MODE = '''# 1. The mode of the ward and of the stay (a method that returns every value tied for the highest frequency)
print("Modal ward:", df["ward"].mode().tolist(), "; modal length of stay:", df["los_days"].mode().tolist(), "days")

# 2. The mode of a finely measured variable against its median
print("Modal systolic pressure:", df["sbp_mmhg"].mode().tolist(), "mmHg; median:", df["sbp_mmhg"].median(), "mmHg")
'''

QUANT = '''# 1. Quartiles and the 90th percentile of the first ten stays (hand calculation)
print("First ten stays - quartile 1, quartile 3, and 90th percentile:", df["los_days"].head(10).quantile([0.25, 0.75, 0.90]).tolist())

# 2. The 10th, 25th, 50th, 75th, and 90th percentiles of the 300 stays
print("300 stays - percentiles 10, 25, 50, 75, and 90:", df["los_days"].quantile([0.10, 0.25, 0.50, 0.75, 0.90]).tolist())
'''

BOX = '''# 1. Quartiles, interquartile range, and the two fences (1.5 and 3 times the interquartile range above the third quartile)
los = df["los_days"]
q1 = los.quantile(0.25)
q3 = los.quantile(0.75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr
extreme = q3 + 3 * iqr
print("Interquartile range:", iqr, "days; lower fence:", q1 - 1.5 * iqr, "days; upper fence:", upper, "days; extreme fence:", extreme, "days")

# 2. The upper whisker and the flagged stays
print("Longest stay inside the fence:", los[los <= upper].max(), "days")
print("Stays beyond the upper fence:", (los > upper).sum(), "; beyond the extreme fence:", (los > extreme).sum())
'''

SKEW = '''# 1. Skewness (adjusted for samples) of three variables: positive for a longer right tail, negative for a longer left tail
for name in ["los_days", "spo2_pct", "sbp_mmhg"]:
    print("Skewness of", name + ":", round(df[name].skew(), 2))
'''

KURT = '''# 1. Excess kurtosis (adjusted for samples) of the same three variables: zero for the normal distribution
for name in ["los_days", "spo2_pct", "sbp_mmhg"]:
    print("Excess kurtosis of", name + ":", round(df[name].kurt(), 2))
'''

TABLE1 = '''# 1. Non-missing values and summary of the numeric columns of Table 1
cols = ["age_years", "sex", "severity", "comorbidities", "sbp_mmhg", "spo2_pct", "crp_mg_l"]
print("Non-missing values of each column:", df[cols].count().tolist())
print(df[cols].describe().round(1))

# 2. Counts and percentages of the categories
sex_counts = df["sex"].value_counts().reindex(["F", "M"])
print("Sex (F, M): counts", sex_counts.tolist(), "; percentages", (100 * sex_counts / len(df)).round(1).tolist())
severity_counts = df["severity"].value_counts().reindex(["low", "moderate", "high"])
print("Severity (low, moderate, high): counts", severity_counts.tolist(), "; percentages", (100 * severity_counts / len(df)).round(1).tolist())
'''

EX16 = '''# 1. C-reactive protein: summary, adjusted skewness, upper fence, and values beyond it
crp = df["crp_mg_l"]
print(crp.describe().round(1))
print("Adjusted skewness:", round(crp.skew(), 2))
q1 = crp.quantile(0.25)
q3 = crp.quantile(0.75)
upper = q3 + 1.5 * (q3 - q1)
print("Upper fence:", upper, "mg/L; values beyond it:", (crp > upper).sum())
'''

EX17 = '''# 1. Waiting times of the triage log of Chapter 3 (a copy of the file is in data/triage.csv), in minutes; visits with no time seen are left out
log = pd.read_csv("data/triage.csv", parse_dates=["arrived_at", "seen_at"])
wait = ((log["seen_at"] - log["arrived_at"]).dt.total_seconds() / 60).dropna()
print("Known waiting times:", len(wait), "; mean:", round(wait.mean(), 1), "minutes; median:", wait.median(), "minutes")

# 2. Quartiles, upper fence, candidate outliers, and the 90th percentile
q1 = wait.quantile(0.25)
q3 = wait.quantile(0.75)
upper = q3 + 1.5 * (q3 - q1)
print("Quartiles:", q1, "and", q3, "; upper fence:", upper, "minutes; waits beyond it:", (wait > upper).sum(), "; 90th percentile:", round(wait.quantile(0.9), 1), "minutes")
'''

EX19 = '''# 1. Counts and percentages of the wards, and the number of missing ward values
ward_counts = df["ward"].value_counts()
print("Patients by ward:", ward_counts.tolist())
print("Percentages:", (100 * ward_counts / len(df)).round(1).tolist())
print("Missing ward values:", len(df) - df["ward"].count())
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

    sec("4.2", "A first look at the data with pandas", "Um primeiro olhar sobre os dados com o pandas",
        "How can the cohort file be read and inspected, and what does the library assume about each column?",
        "Como o arquivo da coorte pode ser lido e inspecionado, e o que a biblioteca supõe sobre cada coluna?")
    cell(LOAD1)
    cell(LOAD2)
    sec("4.4", "Frequency distribution", "Distribuição de frequências", "How often does each value occur?", "Com que frequência cada valor ocorre?")
    cell(FREQ)
    sec("4.5", "Drawing with matplotlib", "Desenhando com o matplotlib", "How is a variable drawn in Python?", "Como uma variável é desenhada em Python?")
    cell(DRAW)
    sec("4.6", "Bar chart", "Gráfico de barras", "How should the categories be shown in a bar chart?", "Como as categorias devem ser mostradas em um gráfico de barras?")
    cell(BAR)
    sec("4.7", "Pareto chart", "Gráfico de Pareto", "Which reasons account for most of the delays?", "Quais motivos respondem pela maior parte dos atrasos?")
    cell(PARETO)
    sec("4.8", "Histogram", "Histograma", "What shape does length of stay take?", "Que forma a permanência toma?")
    cell(HIST)
    sec("4.9", "Stem-and-leaf display", "Diagrama de ramo e folhas", "Can the values themselves be shown while keeping the shape?", "Os próprios valores podem ser mostrados mantendo a forma?")
    cell(STEM)
    sec("4.10", "Arithmetic mean", "Média aritmética", "What is the center of the stays, measured by the arithmetic mean?", "Qual é o centro das permanências, medido pela média aritmética?")
    cell(MEAN)
    sec("4.11", "Median", "Mediana", "What is the median stay, and does it resist unusual values?", "Qual é a mediana da permanência, e ela resiste a valores incomuns?")
    cell(MEDIAN)
    sec("4.12", "Line chart", "Gráfico de linhas", "How did admissions vary over the twelve months?", "Como as internações variaram ao longo dos doze meses?")
    cell(LINE)
    sec("4.13", "Mode", "Moda", "Which value occurs most often?", "Qual valor ocorre com mais frequência?")
    cell(MODE)
    sec("4.14", "Quantiles: quartiles, deciles, and percentiles", "Quantis: quartis, decis e percentis", "Which values split the stays into quarters and tenths?", "Quais valores dividem as permanências em quartos e décimos?")
    cell(QUANT)
    sec("4.15", "Boxplot and outliers", "Boxplot e outliers", "Which stays are outliers?", "Quais permanências são outliers?")
    cell(BOX)
    sec("4.21", "Skewness", "Assimetria", "Is the distribution symmetric?", "A distribuição é simétrica?")
    cell(SKEW)
    sec("4.22", "Kurtosis", "Curtose", "How heavy are the tails?", "Quão pesadas são as caudas?")
    cell(KURT)
    sec("4.23", "Table 1: describing the sample", "Tabela 1: descrevendo a amostra",
        "How is the whole cohort described in the first table of the manuscript?", "Como a coorte inteira é descrita na primeira tabela do manuscrito?")
    cell(TABLE1)
    exs = [(16, "", EX16), (17, "", EX17), (19, "", EX19)]
    return S, [(k, title, code(block)) for k, title, block in exs]

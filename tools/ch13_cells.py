"""All code cells of the Chapter 13 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. Beginner-friendly Python: print with commas, round(), no f-strings, no helper functions.
The cells are written once in English; the Portuguese cell is the same code with the comments and printed text translated
through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the file: one row is one enrolled child (dmft is known in real life only after the examination)", "# 1. Ler o arquivo: cada linha é uma criança matriculada (o dmft só é conhecido, na vida real, depois do exame)"),
 ("# 2. Count rows and columns", "# 2. Contar linhas e colunas"),
 ("The list has", "A lista tem"), ("rows (one per child) and", "linhas (uma por criança) e"), ("columns.", "colunas."),
 ("# The first five rows", "# As cinco primeiras linhas"),
 # 13.2
 ("# 1. The whole list: population mean, standard deviation, and share free of decay", "# 1. A lista inteira: média populacional, desvio padrão e parcela livre de cárie"),
 ("Population: mean", "População: média"), ("; standard deviation", "; desvio padrão"), ("; free of decay:", "; livres de cárie:"), ('"%;", N, "children")', '"%;", N, "crianças")'),
 ("# 2. By type of school", "# 2. Por tipo de escola"),
 ("# 3. A convenience sample: the first 600 children of the list", "# 3. Uma amostra de conveniência: as primeiras 600 crianças da lista"),
 ("Convenience sample: mean", "Amostra de conveniência: média"), ("; schools:", "; escolas:"),
 # 13.3
 ("# 1. One simple random sample of 600 children (seed 13)", "# 1. Uma amostra aleatória simples de 600 crianças (semente 13)"),
 ("Simple random sample: mean", "Amostra aleatória simples: média"), ("; schools:", "; escolas:"), ("; private:", "; particulares:"),
 ("# 2. Systematic sample: every 24th child from a random start, repeated 5,000 times", "# 2. Amostra sistemática: uma criança a cada 24 a partir de um início sorteado, repetida 5.000 vezes"),
 ("Systematic: standard deviation of the means", "Sistemática: desvio padrão das médias"), ("; simple random sample standard error", "; erro padrão da amostra aleatória simples"),
 # 13.4
 ("# 1. 2,000 simple random samples of 600 children: the sampling distribution of the mean", "# 1. 2.000 amostras aleatórias simples de 600 crianças: a distribuição amostral da média"),
 ("# 2. Standard error by the formula, without and with the finite population correction", "# 2. Erro padrão pela fórmula, sem e com a correção para população finita"),
 ("Means: mean", "Médias: média"), ("; standard deviation of the means", "; desvio padrão das médias"),
 ("Standard error: sigma/sqrt(n) =", "Erro padrão: sigma/raiz(n) ="), ("; with the correction", "; com a correção"), ("; correction factor", "; fator de correção"),
 ("# 3. Variance dividing by n and by n - 1, in 5,000 samples of 10 children", "# 3. Variância dividindo por n e por n - 1, em 5.000 amostras de 10 crianças"),
 ("Population variance", "Variância populacional"), ("; dividing by n", "; dividindo por n"), ("; dividing by n - 1", "; dividindo por n - 1"),
 ("# 4. Mean of the first n children in 20 random orders of the list", "# 4. Média das n primeiras crianças em 20 ordens aleatórias da lista"),
 ("# 5. Half-width of the population mean plus and minus 1.96 standard errors", "# 5. Meia-largura da média populacional mais e menos 1,96 erros padrão"),
 ("Number of children:", "Número de crianças:"), ("; the 20 means range from", "; as 20 médias vão de"), ("up to", "até"),
 ("; band half-width (1.96 standard errors):", "; meia-largura da faixa (1,96 erros padrão):"),
 # 13.5
 ("# 1. Sample means for samples of 5, 30, and 600 children (2,000 samples each)", "# 1. Médias amostrais para amostras de 5, 30 e 600 crianças (2.000 amostras cada)"),
 ("Samples of", "Amostras de"), ("skewness of the means", "assimetria das médias"), ("; standard deviation", "; desvio padrão"),
 # 13.6
 ("# 1. The sample of 600: mean, standard deviation, and standard error", "# 1. A amostra de 600: média, desvio padrão e erro padrão"),
 ("# 2. 95% confidence interval for the mean with the t multiple", "# 2. Intervalo de confiança de 95% para a média com o múltiplo t"),
 ("Sample: mean", "Amostra: média"), ("; standard error", "; erro padrão"),
 ("t multiple:", "Múltiplo t:"), ("; 95% CI:", "; IC de 95%:"), ('"to", round(', '"a", round('), ("; contains the population mean:", "; contém a média populacional:"),
 ("# 3. Coverage of the interval in 2,000 samples of 600 children", "# 3. Cobertura do intervalo em 2.000 amostras de 600 crianças"),
 ("Coverage with 600 children:", "Cobertura com 600 crianças:"),
 ("# 4. Samples of 15 children: intervals with 1.96 and with the t multiple, 5,000 samples", "# 4. Amostras de 15 crianças: intervalos com 1,96 e com o múltiplo t, 5.000 amostras"),
 ("Coverage with 15 children: 1.96", "Cobertura com 15 crianças: 1,96"), ("; t multiple", "; múltiplo t"),
 # 13.7
 ("# 1. Shares in the sample of 600: free of decay and dmft of 8 or more", "# 1. Parcelas na amostra de 600: livres de cárie e dmft de 8 ou mais"),
 ("Free of decay:", "Livres de cárie:"), ("; share", "; parcela"), ("; standard error", "; erro padrão"),
 ("Severe (dmft 8 or more):", "Graves (dmft 8 ou mais):"),
 ("# 2. Wald and Wilson 95% intervals", "# 2. Intervalos de Wald e de Wilson de 95%"),
 ('count, "of", n', 'count, "de", n'), ("Wald:", "Wald:"), ("; Wilson:", "; Wilson:"),
 ("# 3. Exact coverage of both intervals for samples of 100 children drawn without replacement (hypergeometric) when the true share is that of severe decay", "# 3. Cobertura exata dos dois intervalos para amostras de 100 crianças sorteadas sem reposição (hipergeométrica) quando a parcela verdadeira é a de cárie grave"),
 ("True share:", "Parcela verdadeira:"), ("; coverage Wald:", "; cobertura Wald:"), ("; Wilson:", "; Wilson:"),
 # 13.8
 ("# 1. The two strata: sizes, weights, means, and standard deviations", "# 1. Os dois estratos: tamanhos, pesos, médias e desvios padrão"),
 ("# 3. The proportional allocation by the formula: 600 times the weight of each stratum", "# 3. A alocação proporcional pela fórmula: 600 vezes o peso de cada estrato"),
 ("Proportional allocation by the formula: public", "Alocação proporcional pela fórmula: públicas"), ("and private", "e particulares"),
 ("# 2. Standard error of the municipality mean and of each stratum mean for three allocations", "# 2. Erro padrão da média do município e da média de cada estrato para três alocações"),
 ("Proportional", "Proporcional"), ("Optimal", "Ótima"), ("Equal", "Igual"), ('"allocation", allocation', '"alocação", allocation'), ("Public:", "Públicas:"), ("Private:", "Particulares:"), ("children; mean", "crianças; média"),
 ("; SE overall", "; EP total"), ("; SE public", "; EP públicas"), ("; SE private", "; EP particulares"),
 # 13.9
 ("# 1. 10,000 samples of 20 schools (equal probability) with 30 children each", "# 1. 10.000 amostras de 20 escolas (mesma probabilidade) com 30 crianças cada"),
 ("Schools: standard deviation of the means", "Escolas: desvio padrão das médias"), ("; mean of the means", "; média das médias"), ("; design effect", "; efeito de delineamento"), ("; effective sample size", "; tamanho efetivo da amostra"),
 ("# 2. Intracluster correlation (analysis of variance) and the rule of thumb for 30 children per school", "# 2. Correlação intraconglomerado (análise de variância) e a regra prática para 30 crianças por escola"),
 ("Intracluster correlation:", "Correlação intraconglomerado:"), ("; rule of thumb 1 + (30 - 1) rho:", "; regra prática 1 + (30 - 1) rho:"),
 ("# 3. Schools chosen with probability proportional to size (10,000 samples)", "# 3. Escolas sorteadas com probabilidade proporcional ao tamanho (10.000 amostras)"),
 ("Mean of the 48 school means:", "Média das 48 médias escolares:"), ("; population child mean:", "; média populacional das crianças:"),
 ("Proportional to size: mean of the means", "Proporcional ao tamanho: média das médias"),
 # 13.10
 ("# 1. Quota sample: the first 150 private and the first 450 public children of the list", "# 1. Amostra por cotas: as primeiras 150 crianças particulares e as primeiras 450 públicas da lista"),
 ("Quota sample: mean", "Amostra por cotas: média"),
 # 13.11
 ("# 1. Sample size for the mean (margin 0.15), without and with the finite population correction", "# 1. Tamanho da amostra para a média (margem 0,15), sem e com a correção para população finita"),
 ("Mean:", "Média:"), ("; with the correction", "; com a correção"),
 ("# 2. Sample size for the share free of decay (margin 0.03) and for p = 0.5", "# 2. Tamanho da amostra para a parcela livre de cárie (margem 0,03) e para p = 0,5"),
 ("Share:", "Parcela:"), ("; p = 0.5:", "; p = 0,5:"),
 ("# 3. Stratified (proportional and optimal) and cluster designs, margin 0.15", "# 3. Delineamentos estratificados (proporcional e ótimo) e por conglomerados, margem 0,15"),
 ("# 3. Stratified designs (proportional and optimal), margin 0.15, without and with the finite population correction", "# 3. Delineamentos estratificados (proporcional e ótimo), margem 0,15, sem e com a correção para população finita"),
 ("Without the correction: simple random", "Sem a correção: aleatória simples"), ("; proportional", "; proporcional"), ("With the correction: simple random", "Com a correção: aleatória simples"), ("; optimal", "; ótima"),
 ("# 5. Visit all 48 schools and examine 20 or 30 children in each (school means weighted by school size)", "# 5. Visitar as 48 escolas e examinar 20 ou 30 crianças em cada uma (médias das escolas ponderadas pelo tamanho)"),
 ("All 48 schools,", "Todas as 48 escolas,"), ("children in each:", "crianças em cada:"), ("children; margin", "crianças; margem"),
 ("# 4. Margin of error with 600 children: simple random sample and 20 schools of 30", "# 4. Margem de erro com 600 crianças: amostra aleatória simples e 20 escolas de 30"),
 ("Margin of error: simple random sample", "Margem de erro: amostra aleatória simples"), ("; schools", "; escolas"),
 # Part B
 ("# 1. First 600 children and the whole list", "# 1. As primeiras 600 crianças e a lista inteira"),
 ("First 600: mean", "Primeiras 600: média"), ("; free of decay", "; livres de cárie"), ("Whole list: mean", "Lista inteira: média"),
 ("# 1. The sample of 600 with seed 13", "# 1. A amostra de 600 com semente 13"),
 ("# 1. Means of 2,000 samples against the standard error formulas", "# 1. Médias de 2.000 amostras contra as fórmulas do erro padrão"),
 ("# 1. Variances in 5,000 samples of 10 children", "# 1. Variâncias em 5.000 amostras de 10 crianças"),
 ("# 1. Skewness of the means for each sample size", "# 1. Assimetria das médias para cada tamanho de amostra"),
 ("# 1. Interval for the sample of 600 and coverage in 2,000 samples", "# 1. Intervalo para a amostra de 600 e cobertura em 2.000 amostras"),
 ("# 1. Wald and Wilson intervals for both shares", "# 1. Intervalos de Wald e de Wilson para as duas parcelas"),
 ("# 1. Standard errors for the three allocations", "# 1. Erros padrão para as três alocações"),
 ("# 1. Design effect and effective sample size of 20 schools of 30 children", "# 1. Efeito de delineamento e tamanho efetivo de 20 escolas de 30 crianças"),
 ("# 1. The quota sample", "# 1. A amostra por cotas"),
 ("# 1. Sample sizes for the mean (margin 0.20) and the share (margin 0.04)", "# 1. Tamanhos de amostra para a média (margem 0,20) e a parcela (margem 0,04)"),
 ("# 1. Margins of error of two designs with 800 children", "# 1. Margens de erro de dois delineamentos com 800 crianças"),
 ("Share free of decay:", "Parcela livre de cárie:"), ("Severe:", "Grave:"),
 ("Margin: 800 at random", "Margem: 800 ao acaso"), ("; 20 schools of 40 (design effect 2.3)", "; 20 escolas de 40 (efeito de delineamento 2,3)"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


LOAD = '''# 1. Read the file: one row is one enrolled child (dmft is known in real life only after the examination)
import numpy as np
import pandas as pd
from math import sqrt
from scipy import stats

df = pd.read_csv("data/schoolchildren.csv")

# 2. Count rows and columns
rows, columns = df.shape
print("The list has", rows, "rows (one per child) and", columns, "columns.")
df.head()                                      # The first five rows
'''

C_FRAME = '''# 1. The whole list: population mean, standard deviation, and share free of decay
dmft = df["dmft"].values
N = len(dmft)
mu = dmft.mean()
sigma = dmft.std(ddof=0)
print("Population: mean", round(mu, 3), "; standard deviation", round(sigma, 3), "; free of decay:", round(100 * (dmft == 0).mean(), 1), "%;", N, "children")

# 2. By type of school
display(df.groupby("school_type")["dmft"].agg(["size", "mean", "std"]).round(3))

# 3. A convenience sample: the first 600 children of the list
first600 = df.iloc[:600]
print("Convenience sample: mean", round(first600["dmft"].mean(), 3), "; free of decay:", round(100 * (first600["dmft"] == 0).mean(), 1), "%; schools:", first600["school"].nunique())
'''

C_SRS = '''# 1. One simple random sample of 600 children (seed 13)
srs = df.sample(n=600, random_state=13)
print("Simple random sample: mean", round(srs["dmft"].mean(), 3), "; schools:", srs["school"].nunique(), "; private:", round(100 * (srs["school_type"] == "private").mean(), 1), "%")

# 2. Systematic sample: every 24th child from a random start, repeated 5,000 times
rng = np.random.default_rng(13)
systematic_means = []
for repetition in range(5000):
    start = rng.integers(0, 24)
    systematic_means.append(dmft[np.arange(start, N, 24)].mean())
srs_se = sigma / sqrt(600) * sqrt((N - 600) / (N - 1))
print("Systematic: standard deviation of the means", round(np.std(systematic_means), 4), "; simple random sample standard error", round(srs_se, 4))
'''

C_SE = '''# 1. 2,000 simple random samples of 600 children: the sampling distribution of the mean
rng = np.random.default_rng(13)
means600 = []
for repetition in range(2000):
    means600.append(dmft[rng.choice(N, 600, replace=False)].mean())
means600 = np.array(means600)
print("Means: mean", round(means600.mean(), 3), "; standard deviation of the means", round(means600.std(), 4))

# 2. Standard error by the formula, without and with the finite population correction
fpc = sqrt((N - 600) / (N - 1))
print("Standard error: sigma/sqrt(n) =", round(sigma / sqrt(600), 4), "; with the correction", round(sigma / sqrt(600) * fpc, 4), "; correction factor", round(fpc, 3))

# 3. Variance dividing by n and by n - 1, in 5,000 samples of 10 children
rng = np.random.default_rng(13)
variances_n = []
variances_n1 = []
for repetition in range(5000):
    small = dmft[rng.choice(N, 10, replace=False)]
    variances_n.append(small.var(ddof=0))
    variances_n1.append(small.var(ddof=1))
print("Population variance", round(sigma ** 2, 3), "; dividing by n", round(np.mean(variances_n), 3), "; dividing by n - 1", round(np.mean(variances_n1), 3))

# 4. Mean of the first n children in 20 random orders of the list
rng = np.random.default_rng(13)
paths = []
for order in range(20):
    paths.append(np.cumsum(dmft[rng.permutation(N)]) / np.arange(1, N + 1))
paths = np.array(paths)
for n_children in (30, 600, 3000):
    column = paths[:, n_children - 1]
    print("Number of children:", n_children, "; the 20 means range from", round(column.min(), 2), "up to", round(column.max(), 2))

# 5. Half-width of the population mean plus and minus 1.96 standard errors
for n_children in (600, 3000):
    half_width = 1.96 * sigma / sqrt(n_children) * sqrt((N - n_children) / (N - 1))
    print("Number of children:", n_children, "; band half-width (1.96 standard errors):", round(half_width, 2))
'''

C_CLT = '''# 1. Sample means for samples of 5, 30, and 600 children (2,000 samples each)
for n_children in (5, 30, 600):
    rng = np.random.default_rng(13)
    sample_means = []
    for repetition in range(2000):
        sample_means.append(dmft[rng.choice(N, n_children, replace=False)].mean())
    print("Samples of", n_children, ": skewness of the means", round(stats.skew(sample_means), 2), "; standard deviation", round(np.std(sample_means), 3), "; sigma/sqrt(n):", round(sigma / sqrt(n_children), 3))
'''

C_CIMEAN = '''# 1. The sample of 600: mean, standard deviation, and standard error
x = srs["dmft"].values
n = len(x)
xbar = x.mean()
s = x.std(ddof=1)
se = s / sqrt(n)
print("Sample: mean", round(xbar, 3), "; standard deviation", round(s, 3), "; standard error", round(se, 4))

# 2. 95% confidence interval for the mean with the t multiple
t_multiple = stats.t.ppf(0.975, n - 1)
low = xbar - t_multiple * se
high = xbar + t_multiple * se
print("t multiple:", round(t_multiple, 3), "; 95% CI:", round(low, 3), "to", round(high, 3), "; contains the population mean:", low <= mu <= high)

# 3. Coverage of the interval in 2,000 samples of 600 children
rng = np.random.default_rng(13)
hits = 0
for repetition in range(2000):
    sample = dmft[rng.choice(N, 600, replace=False)]
    margin = t_multiple * sample.std(ddof=1) / sqrt(600)
    if abs(sample.mean() - mu) <= margin:
        hits = hits + 1
print("Coverage with 600 children:", round(100 * hits / 2000, 1), "%")

# 4. Samples of 15 children: intervals with 1.96 and with the t multiple, 5,000 samples
rng = np.random.default_rng(13)
hits_z = 0
hits_t = 0
for repetition in range(5000):
    sample = dmft[rng.choice(N, 15, replace=False)]
    se15 = sample.std(ddof=1) / sqrt(15)
    if abs(sample.mean() - mu) <= 1.96 * se15:
        hits_z = hits_z + 1
    if abs(sample.mean() - mu) <= stats.t.ppf(0.975, 14) * se15:
        hits_t = hits_t + 1
print("Coverage with 15 children: 1.96", round(100 * hits_z / 5000, 1), "%; t multiple", round(100 * hits_t / 5000, 1), "%")
'''

C_CIPROP = '''# 1. Shares in the sample of 600: free of decay and dmft of 8 or more
z = 1.959964
for label, count in (("Free of decay:", int((x == 0).sum())), ("Severe (dmft 8 or more):", int((x >= 8).sum()))):
    share = count / n
    se_share = sqrt(share * (1 - share) / n)

    # 2. Wald and Wilson 95% intervals
    wald_low = share - z * se_share
    wald_high = share + z * se_share
    centre = (share + z ** 2 / (2 * n)) / (1 + z ** 2 / n)
    half = z * sqrt(share * (1 - share) / n + z ** 2 / (4 * n ** 2)) / (1 + z ** 2 / n)
    print(label, count, "of", n, "; share", round(100 * share, 1), "%; standard error", round(se_share, 4))
    print("Wald:", round(100 * wald_low, 1), "to", round(100 * wald_high, 1), "; Wilson:", round(100 * (centre - half), 1), "to", round(100 * (centre + half), 1))

# 3. Exact coverage of both intervals for samples of 100 children drawn without replacement (hypergeometric) when the true share is that of severe decay
p_true = (dmft >= 8).mean()
counts = np.arange(0, 101)
shares = counts / 100
wald_l = shares - z * np.sqrt(shares * (1 - shares) / 100)
wald_h = shares + z * np.sqrt(shares * (1 - shares) / 100)
wilson_c = (shares + z ** 2 / 200) / (1 + z ** 2 / 100)
wilson_h = z * np.sqrt(shares * (1 - shares) / 100 + z ** 2 / 40000) / (1 + z ** 2 / 100)
probabilities = stats.hypergeom.pmf(counts, N, int((dmft >= 8).sum()), 100)
print("True share:", round(100 * p_true, 2), "%; coverage Wald:", round(100 * probabilities[(wald_l <= p_true) & (p_true <= wald_h)].sum(), 1), "%; Wilson:", round(100 * probabilities[(wilson_c - wilson_h <= p_true) & (p_true <= wilson_c + wilson_h)].sum(), 1), "%")
'''

C_STRATA = '''# 1. The two strata: sizes, weights, means, and standard deviations
public = df[df["school_type"] == "public"]["dmft"].values
private = df[df["school_type"] == "private"]["dmft"].values
sizes = np.array([len(public), len(private)])
weights = sizes / N
sds = np.array([public.std(ddof=0), private.std(ddof=0)])
print("Public:", sizes[0], "children; mean", round(public.mean(), 3), "; standard deviation", round(sds[0], 3))
print("Private:", sizes[1], "children; mean", round(private.mean(), 3), "; standard deviation", round(sds[1], 3))

# 2. Standard error of the municipality mean and of each stratum mean for three allocations
optimal = np.round(600 * weights * sds / (weights * sds).sum())
for name, allocation in (("Proportional", np.round(600 * weights)), ("Optimal", optimal), ("Equal", np.array([300, 300]))):
    variance = (weights ** 2 * sds ** 2 / allocation * (1 - allocation / sizes)).sum()
    se_h = sds / np.sqrt(allocation) * np.sqrt(1 - allocation / sizes)
    print(name, "allocation", allocation, "; SE overall", round(sqrt(variance), 4), "; SE public", round(se_h[0], 3), "; SE private", round(se_h[1], 3))

# 3. The proportional allocation by the formula: 600 times the weight of each stratum
exact = 600 * weights
print("Proportional allocation by the formula: public", round(exact[0], 1), "and private", round(exact[1], 1))
'''

C_CLUSTER = '''# 1. 10,000 samples of 20 schools (equal probability) with 30 children each
schools = np.array(sorted(df["school"].unique()))
rows_of = {}
for school in schools:
    rows_of[school] = np.where(df["school"].values == school)[0]
rng = np.random.default_rng(13)
school_means = []
for repetition in range(10000):
    chosen = rng.choice(schools, 20, replace=False)
    children = np.concatenate([rng.choice(rows_of[school], 30, replace=False) for school in chosen])
    school_means.append(dmft[children].mean())
school_means = np.array(school_means)
deff = (school_means.std() / srs_se) ** 2
print("Schools: standard deviation of the means", round(school_means.std(), 4), "; mean of the means", round(school_means.mean(), 3), "; design effect", round(deff, 2), "; effective sample size", round(600 / deff))

# 2. Intracluster correlation (analysis of variance) and the rule of thumb for 30 children per school
by_school = df.groupby("school")["dmft"].agg(["mean", "size"])
between = ((by_school["mean"] - mu) ** 2 * by_school["size"]).sum() / (len(schools) - 1)
within = ((df["dmft"] - df.groupby("school")["dmft"].transform("mean")) ** 2).sum() / (N - len(schools))
m0 = (N - (by_school["size"] ** 2).sum() / N) / (len(schools) - 1)
rho = (between - within) / (between + (m0 - 1) * within)
print("Intracluster correlation:", round(rho, 3), "; rule of thumb 1 + (30 - 1) rho:", round(1 + 29 * rho, 2))

# 3. Schools chosen with probability proportional to size (10,000 samples)
school_sizes = by_school["size"].reindex(schools).values
print("Mean of the 48 school means:", round(by_school["mean"].mean(), 3), "; population child mean:", round(mu, 3))
rng = np.random.default_rng(13)
pps_means = []
for repetition in range(10000):
    chosen = rng.choice(schools, 20, replace=True, p=school_sizes / school_sizes.sum())
    children = np.concatenate([rng.choice(rows_of[school], 30, replace=False) for school in chosen])
    pps_means.append(dmft[children].mean())
print("Proportional to size: mean of the means", round(np.mean(pps_means), 3), "; standard deviation", round(np.std(pps_means), 3), "; design effect", round((np.std(pps_means) / srs_se) ** 2, 2))
'''

C_QUOTA = '''# 1. Quota sample: the first 150 private and the first 450 public children of the list
private_rows = np.where(df["school_type"].values == "private")[0]
public_rows = np.where(df["school_type"].values == "public")[0]
quota = np.concatenate([dmft[private_rows[:150]], dmft[public_rows[:450]]])
print("Quota sample: mean", round(quota.mean(), 3), "; free of decay:", round(100 * (quota == 0).mean(), 1), "%; schools:", df.iloc[np.concatenate([private_rows[:150], public_rows[:450]])]["school"].nunique())
'''

C_SIZE = '''# 1. Sample size for the mean (margin 0.15), without and with the finite population correction
z = 1.959964
n0 = (z * sigma / 0.15) ** 2
n_corrected = n0 / (1 + (n0 - 1) / N)
print("Mean:", round(n0, 1), "; with the correction", round(n_corrected, 1))

# 2. Sample size for the share free of decay (margin 0.03) and for p = 0.5
p_free = (dmft == 0).mean()
n_share = z ** 2 * p_free * (1 - p_free) / 0.03 ** 2
print("Share:", round(n_share, 1), "; p = 0.5:", round(z ** 2 * 0.25 / 0.03 ** 2, 1))

# 3. Stratified designs (proportional and optimal), margin 0.15, without and with the finite population correction
n_proportional = (z / 0.15) ** 2 * (weights * sds ** 2).sum()
n_optimal = (z / 0.15) ** 2 * (weights * sds).sum() ** 2
n_proportional_c = n_proportional / (1 + n_proportional / N)
n_optimal_c = (weights * sds).sum() ** 2 / (0.15 ** 2 / z ** 2 + (weights * sds ** 2).sum() / N)
print("Without the correction: simple random", int(np.ceil(n0)), "; proportional", int(np.ceil(n_proportional)), "; optimal", int(np.ceil(n_optimal)))
print("With the correction: simple random", int(np.ceil(n_corrected)), "; proportional", int(np.ceil(n_proportional_c)), "; optimal", int(np.ceil(n_optimal_c)))

# 4. Margin of error with 600 children: simple random sample and 20 schools of 30
print("Margin of error: simple random sample", round(z * srs_se, 3), "; schools", round(z * school_means.std(), 3))

# 5. Visit all 48 schools and examine 20 or 30 children in each (school means weighted by school size)
school_sd = df.groupby("school")["dmft"].std(ddof=0).values
school_n = df.groupby("school").size().values
for m in (20, 30):
    variance_m = ((school_n / N) ** 2 * school_sd ** 2 / m * (1 - m / school_n)).sum()
    print("All 48 schools,", m, "children in each:", 48 * m, "children; margin", round(z * sqrt(variance_m), 3))
'''

EX1 = '''# 1. First 600 children and the whole list
print("First 600: mean", round(dmft[:600].mean(), 3), "; free of decay", round(100 * (dmft[:600] == 0).mean(), 1), "%; schools", list(df["school"].iloc[:600].unique()))
print("Whole list: mean", round(mu, 3), "; free of decay", round(100 * (dmft == 0).mean(), 1), "%")
'''
EX2 = '''# 1. The sample of 600 with seed 13
print("Mean:", round(x.mean(), 3), "; standard deviation:", round(x.std(ddof=1), 3), "; standard error:", round(x.std(ddof=1) / sqrt(600), 4))
'''
EX3 = '''# 1. Means of 2,000 samples against the standard error formulas
print("Mean of the means:", round(means600.mean(), 3), "; standard deviation:", round(means600.std(), 4), "; sigma/sqrt(n):", round(sigma / sqrt(600), 4), "; with the correction:", round(srs_se, 4))
'''
EX4 = '''# 1. Variances in 5,000 samples of 10 children
print("Population variance:", round(sigma ** 2, 3), "; dividing by n:", round(np.mean(variances_n), 3), "; dividing by n - 1:", round(np.mean(variances_n1), 3))
'''
EX5 = '''# 1. Skewness of the means for each sample size
for n_children in (5, 30, 600):
    rng = np.random.default_rng(13)
    sample_means = []
    for repetition in range(2000):
        sample_means.append(dmft[rng.choice(N, n_children, replace=False)].mean())
    print("Samples of", n_children, ": skewness", round(stats.skew(sample_means), 2))
'''
EX6 = '''# 1. Interval for the sample of 600 and coverage in 2,000 samples
print("95% CI:", round(low, 3), "to", round(high, 3), "; contains", mu.round(3), ":", low <= mu <= high, "; coverage in 2,000 samples:", round(100 * hits / 2000, 1), "%")
'''
EX7 = '''# 1. Wald and Wilson intervals for both shares
for label, count in (("Share free of decay:", int((x == 0).sum())), ("Severe:", int((x >= 8).sum()))):
    share = count / 600
    wald = z * sqrt(share * (1 - share) / 600)
    centre = (share + z ** 2 / 1200) / (1 + z ** 2 / 600)
    half = z * sqrt(share * (1 - share) / 600 + z ** 2 / 1440000) / (1 + z ** 2 / 600)
    print(label, round(100 * share, 1), "%; Wald", round(100 * (share - wald), 1), "to", round(100 * (share + wald), 1), "; Wilson", round(100 * (centre - half), 1), "to", round(100 * (centre + half), 1))
'''
EX8 = '''# 1. Standard errors for the three allocations
for name, allocation in (("Proportional", np.round(600 * weights)), ("Optimal", optimal), ("Equal", np.array([300, 300]))):
    variance = (weights ** 2 * sds ** 2 / allocation * (1 - allocation / sizes)).sum()
    se_h = sds / np.sqrt(allocation) * np.sqrt(1 - allocation / sizes)
    print(name, "allocation", allocation, "; SE overall", round(sqrt(variance), 4), "; SE public", round(se_h[0], 3), "; SE private", round(se_h[1], 3))
'''
EX9 = '''# 1. Design effect and effective sample size of 20 schools of 30 children
print("Standard deviation of the means:", round(school_means.std(), 4), "; design effect:", round(deff, 2), "; effective sample size:", round(600 / deff))
'''
EX10 = '''# 1. The quota sample
print("Mean:", round(quota.mean(), 3), "; free of decay:", round(100 * (quota == 0).mean(), 1), "%")
'''
EX11 = '''# 1. Sample sizes for the mean (margin 0.20) and the share (margin 0.04)
n_mean = (z * sigma / 0.20) ** 2
n_share2 = z ** 2 * p_free * (1 - p_free) / 0.04 ** 2
print("Mean:", round(n_mean, 1), "; with the correction", round(n_mean / (1 + (n_mean - 1) / N), 1), "; share:", round(n_share2, 1), "; with the correction", round(n_share2 / (1 + (n_share2 - 1) / N), 1))
'''
EX12 = '''# 1. Margins of error of two designs with 800 children
se800 = sigma / sqrt(800) * sqrt((N - 800) / (N - 1))
print("Margin: 800 at random", round(z * se800, 3), "; 20 schools of 40 (design effect 2.3)", round(z * se800 * sqrt(2.3), 3))
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

    sec("13.1", "Introduction: the data", "Introdução: os dados")
    cell(LOAD)
    sec("13.2", "Whom does the survey describe?", "Quem o levantamento descreve?",
        "Whom does the survey describe, and does the way the children are chosen change what the result means?",
        "Quem o levantamento descreve, e o modo de escolher as crianças muda o significado do resultado?")
    cell(C_FRAME)
    sec("13.3", "Drawing the children at random", "Sorteando as crianças",
        "How are 600 children drawn at random, and by what other rules can a probability sample be drawn?",
        "Como sortear 600 crianças ao acaso, e com que outras regras se pode tirar uma amostra probabilística?")
    cell(C_SRS)
    sec("13.4", "How much does the average change from sample to sample?", "Quanto a média muda de amostra para amostra?",
        "How much would the average dmft change from one sample to another?", "Quanto o dmft médio mudaria de uma amostra para outra?")
    cell(C_SE)
    sec("13.5", "What shape does the variation of the average take?", "Qual é o formato da variação da média?",
        "Do the averages of the samples spread in a bell shape, even though the dmft of the children does not have that shape?", "As médias das amostras se espalham em forma de sino, mesmo que o dmft das crianças não tenha esse formato?")
    cell(C_CLT)
    sec("13.6", "The average dmft and a confidence interval", "O dmft médio e um intervalo de confiança",
        "What is the average dmft in the municipality, and how sure are we?", "Qual é o dmft médio no município, e quão seguros estamos?")
    cell(C_CIMEAN)
    sec("13.7", "Shares of children and the Wald and Wilson intervals", "Parcelas de crianças e os intervalos de Wald e de Wilson",
        "What share of the children is free of decay, or has severe decay, and how sure are we?",
        "Que parcela das crianças está livre de cárie, ou tem cárie grave, e quão seguros estamos?")
    cell(C_CIPROP)
    sec("13.8", "Stratifying by type of school", "Estratificando pelo tipo de escola",
        "Should private and public schools be sampled separately?", "As escolas particulares e públicas devem ser amostradas separadamente?")
    cell(C_STRATA)
    sec("13.9", "Sampling schools instead of children", "Sorteando escolas em vez de crianças",
        "Can the survey visit only some of the schools?", "O levantamento pode visitar só algumas das escolas?")
    cell(C_CLUSTER)
    sec("13.10", "When there is no list of children", "Quando não há lista de crianças",
        "When there is no list of children, what can be done?", "Quando não há lista de crianças, o que se pode fazer?")
    cell(C_QUOTA)
    sec("13.11", "How many children must be examined?", "Quantas crianças precisam ser examinadas?",
        "How many children must be examined?", "Quantas crianças precisam ser examinadas?")
    cell(C_SIZE)
    exs = [("The first 600 children", "As primeiras 600 crianças", EX1), ("One simple random sample", "Uma amostra aleatória simples", EX2),
           ("Many simple random samples", "Muitas amostras aleatórias simples", EX3), ("Dividing by n or by n - 1", "Dividir por n ou por n - 1", EX4),
           ("Skewness of the means", "Assimetria das médias", EX5), ("Confidence interval for the mean", "Intervalo de confiança para a média", EX6),
           ("Wald and Wilson intervals", "Intervalos de Wald e de Wilson", EX7), ("Allocations", "Alocações", EX8),
           ("Sampling schools", "Sorteando escolas", EX9), ("A quota sample", "Uma amostra por cotas", EX10),
           ("Sample sizes", "Tamanhos de amostra", EX11), ("Two designs with 800 children", "Dois delineamentos com 800 crianças", EX12)]
    nums = list(range(1, 13))
    return S, [(nums[i], T(a, b), code(c)) for i, (a, b, c) in enumerate(exs)]

"""All code cells of the Chapter 11 notebook (Q1 to Q6 and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. English uses 5,000 and 0.0663; Portuguese uses 5.000 and 0,0663."""

HELP = {
 "en": '''def num(x): return f"{x:,}"                    # 5,000
def dec(x, d=4): return f"{x:.{d}f}"           # 0.0663
def pct(x): return f"{x:.2%}"                  # 26.26%''',
 "pt": '''def num(x): return f"{x:,}".replace(",", ".")                 # 5.000
def dec(x, d=4): return f"{x:.{d}f}".replace(".", ",")       # 0,0663
def pct(x): return f"{x:.2%}".replace(".", ",")              # 26,26%''',
}

PLOT = '''
import matplotlib.pyplot as plt

plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(5, 2.6))
ax.plot(range(1, n + 1), running, color="#222222", linewidth=.9)
ax.axhline(C.mean(), color="#8a8a8a", linewidth=.8, linestyle="--")
ax.set(xscale="log", xlabel="XLABEL", ylabel="YLABEL")
plt.show()'''


def cells(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    Q = {}
    Q["Q1"] = T('''import pandas as pd

df = pd.read_csv("data/deliveries.csv")

HELP

# 1. Take all the rows: one row is one delivery
n = len(df)
print(f"The register has {num(n)} deliveries.")

# 2. In each row, look at the column: is it "yes"?
C = df["cesarean"] == "yes"
H = df["hemorrhage"] == "yes"
I = df["infection"] == "yes"
n_c, n_h = int(C.sum()), int(H.sum())
print(f"Of the {num(n)} deliveries, {num(n_c)} were cesarean and {num(n - n_c)} were not.")

# 3. Count the "yes" rows and divide by all the rows
print(f"Cesarean:   {num(n_c)} of {num(n)} deliveries = {pct(n_c / n)}")
print(f"Hemorrhage: {num(n_h)} of {num(n)} deliveries = {pct(n_h / n)}")

# 4. Read the register in order: does the fraction of cesareans settle?
running = C.cumsum() / range(1, n + 1)      # cesareans so far / rows read so far
print("\\nReading the register in order:")
for k in (10, 50, 100, 500, 1000, 5000):
    print(f"  after {num(k):>5} rows: {num(int(C.iloc[:k].sum())):>5} cesareans = {dec(running.iloc[k - 1])}")
''', '''import pandas as pd

df = pd.read_csv("data/deliveries.csv")

HELP

# 1. Pegar todas as linhas: cada linha é um parto
n = len(df)
print(f"O registro tem {num(n)} partos.")

# 2. Em cada linha, olhar a coluna: está "yes"?
C = df["cesarean"] == "yes"
H = df["hemorrhage"] == "yes"
I = df["infection"] == "yes"
n_c, n_h = int(C.sum()), int(H.sum())
print(f"Dos {num(n)} partos, {num(n_c)} foram cesáreas e {num(n - n_c)} não.")

# 3. Contar as linhas "yes" e dividir por todas as linhas
print(f"Cesárea:    {num(n_c)} de {num(n)} partos = {pct(n_c / n)}")
print(f"Hemorragia: {num(n_h)} de {num(n)} partos = {pct(n_h / n)}")

# 4. Ler o registro em ordem: a fração de cesáreas se estabiliza?
running = C.cumsum() / range(1, n + 1)      # cesáreas até agora / linhas lidas até agora
print("\\nLendo o registro em ordem:")
for k in (10, 50, 100, 500, 1000, 5000):
    print(f"  após {num(k):>5} linhas: {num(int(C.iloc[:k].sum())):>5} cesáreas = {dec(running.iloc[k - 1])}")
''')
    Q["Q2"] = T('''# 1. Cross the two columns: each delivery falls in exactly one of four cells
print("Hemorrhage (rows) by infection (columns):")
print(pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Add the two groups, then correct for the mothers counted twice
hemorrhage, infection, both = int(H.sum()), int(I.sum()), int((H & I).sum())
print(f"{hemorrhage} mothers had a hemorrhage and {infection} had an infection.")
print(f"Adding the two gives {hemorrhage + infection}, but the {both} mothers with both were counted twice.")
print(f"Hemorrhage or infection: {hemorrhage} + {infection} - {both} = {hemorrhage + infection - both} mothers.\\n")

# 3. Check by counting directly, and count the mothers with neither
either = H | I                              # True when the row has at least one of the two
print(f"Counted directly: {int(either.sum())} of {num(n)} mothers = {pct(either.mean())}.")
print(f"With neither:     {num(int((~either).sum()))} of {num(n)} mothers = {pct((~either).mean())}.")
''', '''# 1. Cruzar as duas colunas: cada parto cai em exatamente uma de quatro células
print("Hemorragia (linhas) por infecção (colunas):")
print(pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Somar os dois grupos e corrigir as mães contadas duas vezes
hemorrhage, infection, both = int(H.sum()), int(I.sum()), int((H & I).sum())
print(f"{hemorrhage} mães tiveram hemorragia e {infection} tiveram infecção.")
print(f"Somando as duas dá {hemorrhage + infection}, mas as {both} mães com ambas foram contadas duas vezes.")
print(f"Hemorragia ou infecção: {hemorrhage} + {infection} - {both} = {hemorrhage + infection - both} mães.\\n")

# 3. Conferir contando diretamente e contar as mães sem nenhuma das duas
either = H | I                              # True quando a linha tem ao menos uma das duas
print(f"Contando direto: {int(either.sum())} de {num(n)} mães = {pct(either.mean())}.")
print(f"Sem nenhuma:     {num(int((~either).sum()))} de {num(n)} mães = {pct((~either).mean())}.")
''')
    Q["Q3"] = T('''# 1. Split the deliveries by type: cesarean, and vaginal (not cesarean)
groups = {"cesarean": C, "vaginal": ~C}

# 2. Within each group, count the infections and divide by the size of that group
for name, group in groups.items():
    infected, size = int((group & I).sum()), int(group.sum())
    print(f"Infection among {name} deliveries: {infected} of {num(size)} = {dec(infected / size)} ({pct(infected / size)})")

# 3. The same 87 infected cesareans over ALL deliveries (a different denominator)
print(f"\\nCesarean and infection, among all deliveries: {int((C & I).sum())} of {num(n)} = {dec((C & I).mean())}")

# 4. Infection over all deliveries, whatever the delivery type
print(f"Infection, among all deliveries:               {int(I.sum())} of {num(n)} = {dec(I.mean())}")
''', '''# 1. Separar os partos por tipo: cesárea e vaginal (não cesárea)
groups = {"por cesárea": C, "vaginais": ~C}

# 2. Dentro de cada grupo, contar as infecções e dividir pelo tamanho desse grupo
for name, group in groups.items():
    infected, size = int((group & I).sum()), int(group.sum())
    print(f"Infecção entre os partos {name}: {infected} de {num(size)} = {dec(infected / size)} ({pct(infected / size)})")

# 3. As mesmas 87 cesáreas infectadas sobre TODOS os partos (outro denominador)
print(f"\\nCesárea e infecção, entre todos os partos: {int((C & I).sum())} de {num(n)} = {dec((C & I).mean())}")

# 4. Infecção sobre todos os partos, qualquer que seja o tipo
print(f"Infecção, entre todos os partos:           {int(I.sum())} de {num(n)} = {dec(I.mean())}")
''')
    Q["Q4"] = T('''# 1. If hemorrhage and infection were independent, P(H and I) would equal P(H) x P(I)
expected = H.mean() * I.mean()
print(f"Expected if independent: {dec(H.mean())} x {dec(I.mean())} = {dec(expected, 6)}")

# 2. What the register shows
print(f"Observed, both together: {int((H & I).sum())} of {num(n)} = {dec((H & I).mean())}\\n")

# 3. Infection within the mothers with and without hemorrhage
print(f"Infection among mothers with hemorrhage:    {int((H & I).sum())} of {int(H.sum())} = {dec(I[H].mean())}")
print(f"Infection among mothers without hemorrhage: {int((~H & I).sum())} of {num(int((~H).sum()))} = {dec(I[~H].mean())}\\n")

# 4. Multiplying while keeping the conditions: cesarean, then hemorrhage, then infection
print(f"Of {num(int(C.sum()))} cesareans, {int((C & H).sum())} had a hemorrhage, and {int((C & H & I).sum())} of those also had an infection.")
chain = C.mean() * H[C].mean() * I[C & H].mean()
print(f"P(C) x P(H|C) x P(I|C and H) = {dec(chain)}, the same as the direct count ({dec((C & H & I).mean())}).")
''', '''# 1. Se hemorragia e infecção fossem independentes, P(H e I) seria igual a P(H) x P(I)
expected = H.mean() * I.mean()
print(f"Esperado se independentes: {dec(H.mean())} x {dec(I.mean())} = {dec(expected, 6)}")

# 2. O que o registro mostra
print(f"Observado, as duas juntas: {int((H & I).sum())} de {num(n)} = {dec((H & I).mean())}\\n")

# 3. Infecção entre as mães com e sem hemorragia
print(f"Infecção entre as mães com hemorragia:    {int((H & I).sum())} de {int(H.sum())} = {dec(I[H].mean())}")
print(f"Infecção entre as mães sem hemorragia:    {int((~H & I).sum())} de {num(int((~H).sum()))} = {dec(I[~H].mean())}\\n")

# 4. Multiplicar mantendo as condições: cesárea, depois hemorragia, depois infecção
print(f"De {num(int(C.sum()))} cesáreas, {int((C & H).sum())} tiveram hemorragia, e {int((C & H & I).sum())} delas também tiveram infecção.")
chain = C.mean() * H[C].mean() * I[C & H].mean()
print(f"P(C) x P(H|C) x P(I|C e H) = {dec(chain)}, igual à contagem direta ({dec((C & H & I).mean())}).")
''')
    Q["Q5"] = T('''# 1. The table: rows are the delivery type, columns are infection
print("Delivery type (rows) by infection (columns):")
print(pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Rebuild the overall infection fraction from the two groups
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"P(I) = P(I|C) P(C) + P(I|not C) P(not C) = {dec(p_i)}")

# 3. Reverse the condition (Bayes): from infection among cesareans to cesareans among infections
p_c_given_i = I[C].mean() * C.mean() / p_i
print(f"P(C|I) = P(I|C) P(C) / P(I) = {dec(p_c_given_i)}")

# 4. Check by counting directly among the infected mothers
print(f"\\nCounting directly: {int((C & I).sum())} of the {int(I.sum())} infections followed a cesarean = {pct(C[I].mean())}.")
''', '''# 1. A tabela: linhas são o tipo de parto, colunas são a infecção
print("Tipo de parto (linhas) por infecção (colunas):")
print(pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Reconstruir a fração geral de infecção a partir dos dois grupos
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"P(I) = P(I|C) P(C) + P(I|não C) P(não C) = {dec(p_i)}")

# 3. Inverter a condição (Bayes): da infecção entre as cesáreas para as cesáreas entre as infecções
p_c_given_i = I[C].mean() * C.mean() / p_i
print(f"P(C|I) = P(I|C) P(C) / P(I) = {dec(p_c_given_i)}")

# 4. Conferir contando diretamente entre as mães infectadas
print(f"\\nContando direto: {int((C & I).sum())} das {int(I.sum())} infecções vieram depois de cesárea = {pct(C[I].mean())}.")
''')
    Q["Q6"] = T('''from math import comb, factorial, perm

N, K = n, int(I.sum())        # N charts in the register, K of them with infection

# 1. In how many ways can 20 charts be chosen? (order does not matter)
sets = comb(N, 20)
print(f"There are {sets} different sets of 20 charts ({len(str(sets))} digits).")

# 2. Orders of the 20 selected charts, and of the first two slots
print(f"The 20 chosen charts can be put in {num(factorial(20))} orders; the first two slots, in {perm(20, 2)}.")

# 3. Chance of at least one infection = 1 - chance of none (all 20 from the N - K without infection)
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)
print(f"\\nChance that 20 charts include at least one infection: {dec(p_at_least_one(20))} ({pct(p_at_least_one(20))})")

# 4. Smallest sample with at least 90% (integer test: no infection is at most 1/10 of all sets)
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
print(f"With {m - 1} charts the chance is {dec(p_at_least_one(m - 1), 6)}; with {m} charts it is {dec(p_at_least_one(m), 6)}.")
print(f"So {m} is the smallest sample with at least 90%.")
''', '''from math import comb, factorial, perm

N, K = n, int(I.sum())        # N prontuários no registro, K deles com infecção

# 1. De quantas maneiras se escolhem 20 prontuários? (a ordem não importa)
sets = comb(N, 20)
print(f"Há {sets} conjuntos diferentes de 20 prontuários ({len(str(sets))} algarismos).")

# 2. Ordens dos 20 prontuários escolhidos, e dos dois primeiros lugares
print(f"Os 20 prontuários escolhidos podem ser postos em {num(factorial(20))} ordens; os dois primeiros lugares, em {perm(20, 2)}.")

# 3. Chance de ao menos uma infecção = 1 - chance de nenhuma (os 20 dos N - K sem infecção)
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)
print(f"\\nChance de 20 prontuários incluírem ao menos uma infecção: {dec(p_at_least_one(20))} ({pct(p_at_least_one(20))})")

# 4. Menor amostra com ao menos 90% (teste com inteiros: nenhuma infecção é no máximo 1/10 dos conjuntos)
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
print(f"Com {m - 1} prontuários a chance é {dec(p_at_least_one(m - 1), 6)}; com {m} prontuários é {dec(p_at_least_one(m), 6)}.")
print(f"Logo {m} é a menor amostra com ao menos 90%.")
''')
    ex = []
    A = lambda title_en, title_pt, en_code, pt_code: ex.append((T(title_en, title_pt), T(en_code, pt_code)))
    A("Records and event descriptions", "Registros e descrições de eventos", '''from itertools import product

# 1. The sample space: one of the 5,000 identifiers
print(f"{num(n)} records, {num(df['delivery_id'].nunique())} distinct identifiers.")

# 2. The eight descriptions (C, H, I), 1 = yes and 0 = no
print("The eight descriptions:", " ".join("".join(map(str, bits)) for bits in product((0, 1), repeat=3)))
''', '''from itertools import product

# 1. O espaço amostral: um dos 5.000 identificadores
print(f"{num(n)} registros, {num(df['delivery_id'].nunique())} identificadores distintos.")

# 2. As oito descrições (C, H, I), 1 = sim e 0 = não
print("As oito descrições:", " ".join("".join(map(str, bits)) for bits in product((0, 1), repeat=3)))
''')
    A("Running fractions and order", "Frações acumuladas e ordem", '''# 1. Fraction of cesareans among the first k records
for k in (10, 50, 100, 500, 1000, 5000):
    print(f"First {num(k):>5} records: {dec(C.iloc[:k].mean())}")

# 2. Reverse the register order: first 100 records, and all 5,000
reverse = C.iloc[::-1]
print(f"\\nReversed order: first 100 records {dec(reverse.iloc[:100].mean())}; all {num(n)} records {dec(reverse.mean())}")
''', '''# 1. Fração de cesáreas entre os k primeiros registros
for k in (10, 50, 100, 500, 1000, 5000):
    print(f"Primeiros {num(k):>5} registros: {dec(C.iloc[:k].mean())}")

# 2. Inverter a ordem do registro: primeiros 100 registros e todos os 5.000
reverse = C.iloc[::-1]
print(f"\\nOrdem invertida: primeiros 100 registros {dec(reverse.iloc[:100].mean())}; todos os {num(n)} registros {dec(reverse.mean())}")
''')
    A("Count the overlap once", "Contar a sobreposição uma vez", '''# 1. The four groups: hemorrhage only, infection only, both, neither
names = ("hemorrhage only", "infection only", "both", "neither")
for name, group in zip(names, (H & ~I, ~H & I, H & I, ~(H | I))):
    print(f"{name:<16} {num(int(group.sum())):>5} mothers = {dec(group.mean())}")

# 2. Addition rule, and the same count done directly
union = H.sum() + I.sum() - (H & I).sum()
print(f"\\nAddition rule: {int(union)} mothers with hemorrhage or infection ({dec(union / n)})")
print(f"Direct count:  {int((H | I).sum())} mothers; probability of neither = {dec(1 - (H | I).mean())}")
''', '''# 1. Os quatro grupos: só hemorragia, só infecção, ambas, nenhuma
names = ("só hemorragia", "só infecção", "ambas", "nenhuma")
for name, group in zip(names, (H & ~I, ~H & I, H & I, ~(H | I))):
    print(f"{name:<14} {num(int(group.sum())):>5} mães = {dec(group.mean())}")

# 2. Regra da adição, e a mesma contagem feita diretamente
union = H.sum() + I.sum() - (H & I).sum()
print(f"\\nRegra da adição: {int(union)} mães com hemorragia ou infecção ({dec(union / n)})")
print(f"Contagem direta: {int((H | I).sum())} mães; probabilidade de nenhuma = {dec(1 - (H | I).mean())}")
''')
    A("Name the denominator", "Nomear o denominador", '''# 1. The five fractions, each with its meaning and denominator
fractions = (("(a) infection among cesareans", I[C].mean()),
             ("(b) cesarean and infection, among all", (C & I).mean()),
             ("(c) infection, among all", I.mean()),
             ("(d) cesarean among infections", C[I].mean()),
             ("(e) hemorrhage among cesareans", H[C].mean()))

# 2. Print each one
for label, value in fractions:
    print(f"{label:<40} {dec(value)}")
''', '''# 1. As cinco frações, cada uma com seu significado e denominador
fractions = (("(a) infecção entre as cesáreas", I[C].mean()),
             ("(b) cesárea e infecção, entre todos", (C & I).mean()),
             ("(c) infecção, entre todos", I.mean()),
             ("(d) cesárea entre as infecções", C[I].mean()),
             ("(e) hemorragia entre as cesáreas", H[C].mean()))

# 2. Imprimir cada uma
for label, value in fractions:
    print(f"{label:<40} {dec(value)}")
''')
    A("Compare within delivery types", "Comparar dentro dos tipos de parto", '''# 1. Infection in each delivery type, and the ratio of the two proportions
print(f"Infection: cesarean {dec(I[C].mean())} versus vaginal {dec(I[~C].mean())}; ratio {dec(I[C].mean() / I[~C].mean())}")

# 2. Hemorrhage in each delivery type: count, group size, proportion
for name, group in (("cesarean", C), ("vaginal", ~C)):
    print(f"Hemorrhage, {name}: {int((H & group).sum())} of {num(int(group.sum()))} = {dec(H[group].mean())}")
''', '''# 1. Infecção em cada tipo de parto, e a razão das duas proporções
print(f"Infecção: cesárea {dec(I[C].mean())} versus vaginal {dec(I[~C].mean())}; razão {dec(I[C].mean() / I[~C].mean())}")

# 2. Hemorragia em cada tipo de parto: contagem, tamanho do grupo, proporção
for name, group in (("cesárea", C), ("vaginal", ~C)):
    print(f"Hemorragia, {name}: {int((H & group).sum())} de {num(int(group.sum()))} = {dec(H[group].mean())}")
''')
    A("Dependence and overlap", "Dependência e sobreposição", '''# 1. Product of the marginals versus the observed joint fraction
print(f"Product of the marginals: {dec(H.mean() * I.mean(), 6)}; observed joint fraction: {dec((H & I).mean())}")

# 2. Infection with and without hemorrhage, and the number with both
print(f"Infection with hemorrhage: {dec(I[H].mean())}; without hemorrhage: {dec(I[~H].mean())}")
print(f"Mothers with both: {int((H & I).sum())}")
''', '''# 1. Produto das marginais versus a fração conjunta observada
print(f"Produto das marginais: {dec(H.mean() * I.mean(), 6)}; fração conjunta observada: {dec((H & I).mean())}")

# 2. Infecção com e sem hemorragia, e o número com ambas
print(f"Infecção com hemorragia: {dec(I[H].mean())}; sem hemorragia: {dec(I[~H].mean())}")
print(f"Mães com ambas: {int((H & I).sum())}")
''')
    A("Two routes to the same joint probability", "Dois caminhos para a mesma probabilidade conjunta", '''# 1. Two ways to order the conditions: C, H, I and H, C, I
first = C.mean() * H[C].mean() * I[C & H].mean()
second = H.mean() * C[H].mean() * I[C & H].mean()

# 2. The counts along the way, and the three results (they must agree)
print(f"Counts: {num(int(C.sum()))} cesareans, {int(H.sum())} hemorrhages, {int((C & H).sum())} with both, {int((C & H & I).sum())} with all three.")
print(f"Route C, H, I: {dec(first)} | route H, C, I: {dec(second)} | direct count: {dec((C & H & I).mean())}")
''', '''# 1. Duas ordens para as condições: C, H, I e H, C, I
first = C.mean() * H[C].mean() * I[C & H].mean()
second = H.mean() * C[H].mean() * I[C & H].mean()

# 2. As contagens pelo caminho e os três resultados (devem coincidir)
print(f"Contagens: {num(int(C.sum()))} cesáreas, {int(H.sum())} hemorragias, {int((C & H).sum())} com ambas, {int((C & H & I).sum())} com as três.")
print(f"Caminho C, H, I: {dec(first)} | caminho H, C, I: {dec(second)} | contagem direta: {dec((C & H & I).mean())}")
''')
    A("Total probability and reversal", "Probabilidade total e inversão", '''# 1. Total probability of infection from the two delivery types
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"Total probability of infection: {dec(p_i)}")

# 2. Bayes: cesareans among the infected, and vaginal deliveries among the infected
bayes = I[C].mean() * C.mean() / p_i
print(f"Among the infected: cesarean {dec(bayes)} (direct count {dec(C[I].mean())}), vaginal {dec((~C)[I].mean())}")
''', '''# 1. Probabilidade total de infecção a partir dos dois tipos de parto
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"Probabilidade total de infecção: {dec(p_i)}")

# 2. Bayes: cesáreas entre as infectadas e partos vaginais entre as infectadas
bayes = I[C].mean() * C.mean() / p_i
print(f"Entre as infectadas: cesárea {dec(bayes)} (contagem direta {dec(C[I].mean())}), vaginal {dec((~C)[I].mean())}")
''')
    A("Orders of the selected charts", "Ordens dos prontuários selecionados", '''from math import factorial, perm

# 1. Orders of 20 charts, and ordered first two slots
print(f"20! = {num(factorial(20))} orders; first two slots: {perm(20, 2)} ordered choices")

# 2. Chance that a given chart is first, and that two given charts are first and second
print(f"A given chart is first with chance {dec(factorial(19) / factorial(20))}")
print(f"Two given charts are first and second with chance {dec(factorial(18) / factorial(20), 6)}")
''', '''from math import factorial, perm

# 1. Ordens de 20 prontuários, e dois primeiros lugares ordenados
print(f"20! = {num(factorial(20))} ordens; dois primeiros lugares: {perm(20, 2)} escolhas ordenadas")

# 2. Chance de um prontuário dado ser o primeiro, e de dois dados serem o primeiro e o segundo
print(f"Um prontuário dado é o primeiro com chance {dec(factorial(19) / factorial(20))}")
print(f"Dois prontuários dados são o primeiro e o segundo com chance {dec(factorial(18) / factorial(20), 6)}")
''')
    A("A sample including an infection", "Uma amostra que inclui uma infecção", '''from math import comb

N, K = n, int(I.sum())

# 1. Chance of at least one infection in a sample of m charts
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)

# 2. Smallest sample with at least 90%, and its neighbour below
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
for size in (20, m - 1, m):
    print(f"{size:>3} charts: chance of at least one infection = {dec(p_at_least_one(size), 6)}")
''', '''from math import comb

N, K = n, int(I.sum())

# 1. Chance de ao menos uma infecção em uma amostra de m prontuários
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)

# 2. Menor amostra com ao menos 90% e a vizinha abaixo
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
for size in (20, m - 1, m):
    print(f"{size:>3} prontuários: chance de ao menos uma infecção = {dec(p_at_least_one(size), 6)}")
''')
    A("Alternative marginal probabilities (alt.)", "Probabilidades marginais alternativas (alt.)", '''# 1. Alternative marginals: P(H) = 0.02 and P(I) = 0.03
p_h, p_i = 0.02, 0.03

# 2. Smallest and largest possible joint probability, and P(H or I) if independent
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print(f"The joint probability must lie between {dec(lower)} and {dec(upper)}.")
print(f"If the events were independent, P(H or I) = {dec(p_h + p_i - p_h * p_i)}.")
''', '''# 1. Marginais alternativas: P(H) = 0,02 e P(I) = 0,03
p_h, p_i = 0.02, 0.03

# 2. Menor e maior probabilidade conjunta possível, e P(H ou I) se independentes
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print(f"A probabilidade conjunta deve estar entre {dec(lower)} e {dec(upper)}.")
print(f"Se os eventos fossem independentes, P(H ou I) = {dec(p_h + p_i - p_h * p_i)}.")
''')
    A("Returning charts between draws (alt.)", "Devolver prontuários entre sorteios (alt.)", '''from math import comb

N, K = n, int(I.sum())

# 1. Chance of at least one infection in 20 draws, with and without returning the chart
with_replacement = 1 - ((N - K) / N) ** 20
without_replacement = 1 - comb(N - K, 20) / comb(N, 20)
print(f"Returning each chart: {dec(with_replacement, 6)} | not returning: {dec(without_replacement, 6)}")

# 2. The difference between the two procedures
print(f"The difference is only {dec(without_replacement - with_replacement, 6)}.")
''', '''from math import comb

N, K = n, int(I.sum())

# 1. Chance de ao menos uma infecção em 20 sorteios, com e sem devolver o prontuário
with_replacement = 1 - ((N - K) / N) ** 20
without_replacement = 1 - comb(N - K, 20) / comb(N, 20)
print(f"Devolvendo cada prontuário: {dec(with_replacement, 6)} | sem devolver: {dec(without_replacement, 6)}")

# 2. A diferença entre os dois procedimentos
print(f"A diferença é de apenas {dec(without_replacement - with_replacement, 6)}.")
''')
    return Q, ex

"""All code cells of the Chapter 11 notebook (Q1 to Q6 and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. Beginner-friendly Python: print with commas, round(), no f-strings."""

HELP = {"en": "", "pt": ""}

PLOT = '''
import matplotlib.pyplot as plt

running = C.expanding().mean()        # fraction of cesareans among the rows read so far
plt.plot(range(1, n + 1), running)
plt.xscale("log")
plt.xlabel("XLABEL")
plt.ylabel("YLABEL")
plt.show()'''
PLOT_PT = PLOT.replace("# fraction of cesareans among the rows read so far", "# fração de cesáreas entre as linhas lidas até agora")


def cells(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    Q = {}
    Q["Q1"] = T('''import pandas as pd

df = pd.read_csv("data/deliveries.csv")

# 1. Take all the rows: one row is one delivery
n = len(df)
print("The register has", n, "deliveries.")

# 2. In each row, look at the column: is it "yes"?
C = df["cesarean"] == "yes"        # True for each cesarean delivery
H = df["hemorrhage"] == "yes"
I = df["infection"] == "yes"
n_cesarean = C.sum()
print("Of the", n, "deliveries,", n_cesarean, "were cesarean and", n - n_cesarean, "were not.")

# 3. Count the "yes" rows and divide by all the rows
n_hemorrhage = H.sum()
print("Cesarean:", n_cesarean, "of", n, "deliveries =", round(100 * n_cesarean / n, 2), "%")
print("Hemorrhage:", n_hemorrhage, "of", n, "deliveries =", round(100 * n_hemorrhage / n, 2), "%")

# 4. Read the register in order: does the fraction of cesareans settle?
for k in [10, 50, 100, 500, 1000, 5000]:
    first_k = C.iloc[:k]           # the first k rows
    print("After", k, "rows:", first_k.sum(), "cesareans =", round(first_k.mean(), 4))
''', '''import pandas as pd

df = pd.read_csv("data/deliveries.csv")

# 1. Pegar todas as linhas: cada linha é um parto
n = len(df)
print("O registro tem", n, "partos.")

# 2. Em cada linha, olhar a coluna: está "yes"?
C = df["cesarean"] == "yes"        # True para cada parto cesárea
H = df["hemorrhage"] == "yes"
I = df["infection"] == "yes"
n_cesarean = C.sum()
print("Dos", n, "partos,", n_cesarean, "foram cesáreas e", n - n_cesarean, "não.")

# 3. Contar as linhas "yes" e dividir por todas as linhas
n_hemorrhage = H.sum()
print("Cesárea:", n_cesarean, "de", n, "partos =", round(100 * n_cesarean / n, 2), "%")
print("Hemorragia:", n_hemorrhage, "de", n, "partos =", round(100 * n_hemorrhage / n, 2), "%")

# 4. Ler o registro em ordem: a fração de cesáreas se estabiliza?
for k in [10, 50, 100, 500, 1000, 5000]:
    first_k = C.iloc[:k]           # as k primeiras linhas
    print("Após", k, "linhas:", first_k.sum(), "cesáreas =", round(first_k.mean(), 4))
''')
    Q["Q2"] = T('''# 1. Cross the two columns: each delivery falls in exactly one of four cells
print("Hemorrhage (rows) by infection (columns):")
print(pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total"))

# 2. Add the two groups, then correct for the mothers counted twice
n_hemorrhage = H.sum()
n_infection = I.sum()
n_both = (H & I).sum()             # "&" means "and": both at the same time
print()
print(n_hemorrhage, "mothers had a hemorrhage and", n_infection, "had an infection.")
print("Adding the two gives", n_hemorrhage + n_infection, "but the", n_both, "mothers with both were counted twice.")
print("Hemorrhage or infection:", n_hemorrhage, "+", n_infection, "-", n_both, "=", n_hemorrhage + n_infection - n_both, "mothers.")

# 3. Check by counting directly, and count the mothers with neither
either = H | I                     # "|" means "or": at least one of the two
n_either = either.sum()
print()
print("Counted directly:", n_either, "of", n, "mothers =", round(100 * n_either / n, 2), "%")
print("With neither:", n - n_either, "of", n, "mothers =", round(100 * (n - n_either) / n, 2), "%")
''', '''# 1. Cruzar as duas colunas: cada parto cai em exatamente uma de quatro células
print("Hemorragia (linhas) por infecção (colunas):")
print(pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total"))

# 2. Somar os dois grupos e corrigir as mães contadas duas vezes
n_hemorrhage = H.sum()
n_infection = I.sum()
n_both = (H & I).sum()             # "&" significa "e": as duas ao mesmo tempo
print()
print(n_hemorrhage, "mães tiveram hemorragia e", n_infection, "tiveram infecção.")
print("Somando as duas dá", n_hemorrhage + n_infection, "mas as", n_both, "mães com ambas foram contadas duas vezes.")
print("Hemorragia ou infecção:", n_hemorrhage, "+", n_infection, "-", n_both, "=", n_hemorrhage + n_infection - n_both, "mães.")

# 3. Conferir contando diretamente e contar as mães sem nenhuma das duas
either = H | I                     # "|" significa "ou": ao menos uma das duas
n_either = either.sum()
print()
print("Contando direto:", n_either, "de", n, "mães =", round(100 * n_either / n, 2), "%")
print("Sem nenhuma:", n - n_either, "de", n, "mães =", round(100 * (n - n_either) / n, 2), "%")
''')
    Q["Q3"] = T('''# 1. Split the deliveries by type: cesarean, and vaginal (not cesarean)
n_cesarean = C.sum()
n_vaginal = (~C).sum()             # "~" means "not"

# 2. Within each group, count the infections and divide by the size of that group
infected_cesarean = (C & I).sum()
infected_vaginal = (~C & I).sum()
print("Infection among cesarean deliveries:", infected_cesarean, "of", n_cesarean, "=", round(infected_cesarean / n_cesarean, 4))
print("Infection among vaginal deliveries:", infected_vaginal, "of", n_vaginal, "=", round(infected_vaginal / n_vaginal, 4))

# 3. The same 87 infected cesareans over ALL deliveries (a different denominator)
print()
print("Cesarean and infection, among all deliveries:", infected_cesarean, "of", n, "=", round(infected_cesarean / n, 4))

# 4. Infection over all deliveries, whatever the delivery type
print("Infection, among all deliveries:", I.sum(), "of", n, "=", round(I.sum() / n, 4))
''', '''# 1. Separar os partos por tipo: cesárea e vaginal (não cesárea)
n_cesarean = C.sum()
n_vaginal = (~C).sum()             # "~" significa "não"

# 2. Dentro de cada grupo, contar as infecções e dividir pelo tamanho desse grupo
infected_cesarean = (C & I).sum()
infected_vaginal = (~C & I).sum()
print("Infecção entre os partos cesárea:", infected_cesarean, "de", n_cesarean, "=", round(infected_cesarean / n_cesarean, 4))
print("Infecção entre os partos vaginais:", infected_vaginal, "de", n_vaginal, "=", round(infected_vaginal / n_vaginal, 4))

# 3. As mesmas 87 cesáreas infectadas sobre TODOS os partos (outro denominador)
print()
print("Cesárea e infecção, entre todos os partos:", infected_cesarean, "de", n, "=", round(infected_cesarean / n, 4))

# 4. Infecção sobre todos os partos, qualquer que seja o tipo
print("Infecção, entre todos os partos:", I.sum(), "de", n, "=", round(I.sum() / n, 4))
''')
    Q["Q4"] = T('''# 1. If hemorrhage and infection were independent, P(H and I) would equal P(H) x P(I)
p_h = H.sum() / n
p_i = I.sum() / n
print("Expected if independent:", round(p_h, 4), "x", round(p_i, 4), "=", round(p_h * p_i, 6))

# 2. What the register shows
n_both = (H & I).sum()
print("Observed, both together:", n_both, "of", n, "=", round(n_both / n, 4))

# 3. Infection within the mothers with and without hemorrhage
print()
print("Infection among mothers with hemorrhage:", n_both, "of", H.sum(), "=", round(n_both / H.sum(), 4))
print("Infection among mothers without hemorrhage:", (~H & I).sum(), "of", (~H).sum(), "=", round((~H & I).sum() / (~H).sum(), 4))

# 4. Multiplying while keeping the conditions: cesarean, then hemorrhage, then infection
n_c, n_ch, n_chi = C.sum(), (C & H).sum(), (C & H & I).sum()
print()
print("Of", n_c, "cesareans,", n_ch, "had a hemorrhage, and", n_chi, "of those also had an infection.")
chain = (n_c / n) * (n_ch / n_c) * (n_chi / n_ch)
print("P(C) x P(H|C) x P(I|C and H) =", round(chain, 4), "; direct count:", round(n_chi / n, 4))
''', '''# 1. Se hemorragia e infecção fossem independentes, P(H e I) seria igual a P(H) x P(I)
p_h = H.sum() / n
p_i = I.sum() / n
print("Esperado se independentes:", round(p_h, 4), "x", round(p_i, 4), "=", round(p_h * p_i, 6))

# 2. O que o registro mostra
n_both = (H & I).sum()
print("Observado, as duas juntas:", n_both, "de", n, "=", round(n_both / n, 4))

# 3. Infecção entre as mães com e sem hemorragia
print()
print("Infecção entre as mães com hemorragia:", n_both, "de", H.sum(), "=", round(n_both / H.sum(), 4))
print("Infecção entre as mães sem hemorragia:", (~H & I).sum(), "de", (~H).sum(), "=", round((~H & I).sum() / (~H).sum(), 4))

# 4. Multiplicar mantendo as condições: cesárea, depois hemorragia, depois infecção
n_c, n_ch, n_chi = C.sum(), (C & H).sum(), (C & H & I).sum()
print()
print("De", n_c, "cesáreas,", n_ch, "tiveram hemorragia, e", n_chi, "delas também tiveram infecção.")
chain = (n_c / n) * (n_ch / n_c) * (n_chi / n_ch)
print("P(C) x P(H|C) x P(I|C e H) =", round(chain, 4), "; contagem direta:", round(n_chi / n, 4))
''')
    Q["Q5"] = T('''# 1. The table: rows are the delivery type, columns are infection
print("Delivery type (rows) by infection (columns):")
print(pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total"))

# 2. Rebuild the overall infection fraction from the two groups
p_c = C.sum() / n                                  # P(C)
p_i_given_c = (C & I).sum() / C.sum()              # P(I|C)
p_i_given_not_c = (~C & I).sum() / (~C).sum()      # P(I|not C)
p_i = p_i_given_c * p_c + p_i_given_not_c * (1 - p_c)
print()
print("P(I) = P(I|C) P(C) + P(I|not C) P(not C) =", round(p_i, 4))

# 3. Reverse the condition (Bayes): from infection among cesareans to cesareans among infections
p_c_given_i = p_i_given_c * p_c / p_i
print("P(C|I) = P(I|C) P(C) / P(I) =", round(p_c_given_i, 4))

# 4. Check by counting directly among the infected mothers
print("Counting directly:", (C & I).sum(), "of the", I.sum(), "infections followed a cesarean =", round(100 * (C & I).sum() / I.sum(), 2), "%")
''', '''# 1. A tabela: linhas são o tipo de parto, colunas são a infecção
print("Tipo de parto (linhas) por infecção (colunas):")
print(pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total"))

# 2. Reconstruir a fração geral de infecção a partir dos dois grupos
p_c = C.sum() / n                                  # P(C)
p_i_given_c = (C & I).sum() / C.sum()              # P(I|C)
p_i_given_not_c = (~C & I).sum() / (~C).sum()      # P(I|não C)
p_i = p_i_given_c * p_c + p_i_given_not_c * (1 - p_c)
print()
print("P(I) = P(I|C) P(C) + P(I|não C) P(não C) =", round(p_i, 4))

# 3. Inverter a condição (Bayes): da infecção entre as cesáreas para as cesáreas entre as infecções
p_c_given_i = p_i_given_c * p_c / p_i
print("P(C|I) = P(I|C) P(C) / P(I) =", round(p_c_given_i, 4))

# 4. Conferir contando diretamente entre as mães infectadas
print("Contando direto:", (C & I).sum(), "das", I.sum(), "infecções vieram depois de cesárea =", round(100 * (C & I).sum() / I.sum(), 2), "%")
''')
    Q["Q6"] = T('''from math import comb, factorial, perm

total = n                          # charts in the register
with_infection = I.sum()           # charts with an infection

# 1. In how many ways can 20 charts be chosen? (order does not matter)
sets = comb(total, 20)
print("There are", sets, "different sets of 20 charts,", len(str(sets)), "digits.")

# 2. Orders of the 20 selected charts, and of the first two slots
print("The 20 chosen charts can be put in", factorial(20), "orders; the first two slots, in", perm(20, 2))

# 3. Chance of at least one infection = 1 - chance of none (all 20 from the charts without infection)
without_infection = total - with_infection
chance_none = comb(without_infection, 20) / comb(total, 20)
print()
print("Chance that 20 charts include at least one infection:", round(1 - chance_none, 4))

# 4. Smallest sample with at least 90%: try sizes 1, 2, 3, ... until the chance of none is at most 10%
size = 1
while 10 * comb(without_infection, size) > comb(total, size):     # compares whole numbers, no rounding
    size = size + 1
for m in [size - 1, size]:
    print("With", m, "charts the chance is", round(1 - comb(without_infection, m) / comb(total, m), 6))
print("So", size, "is the smallest sample with at least 90%.")
''', '''from math import comb, factorial, perm

total = n                          # prontuários no registro
with_infection = I.sum()           # prontuários com infecção

# 1. De quantas maneiras se escolhem 20 prontuários? (a ordem não importa)
sets = comb(total, 20)
print("Há", sets, "conjuntos diferentes de 20 prontuários,", len(str(sets)), "algarismos.")

# 2. Ordens dos 20 prontuários escolhidos, e dos dois primeiros lugares
print("Os 20 prontuários escolhidos podem ser postos em", factorial(20), "ordens; os dois primeiros lugares, em", perm(20, 2))

# 3. Chance de ao menos uma infecção = 1 - chance de nenhuma (os 20 entre os prontuários sem infecção)
without_infection = total - with_infection
chance_none = comb(without_infection, 20) / comb(total, 20)
print()
print("Chance de 20 prontuários incluírem ao menos uma infecção:", round(1 - chance_none, 4))

# 4. Menor amostra com ao menos 90%: testar tamanhos 1, 2, 3, ... até a chance de nenhuma ser no máximo 10%
size = 1
while 10 * comb(without_infection, size) > comb(total, size):     # compara números inteiros, sem arredondar
    size = size + 1
for m in [size - 1, size]:
    print("Com", m, "prontuários a chance é", round(1 - comb(without_infection, m) / comb(total, m), 6))
print("Logo", size, "é a menor amostra com ao menos 90%.")
''')
    ex = []
    A = lambda te, tp, ce, cp: ex.append((T(te, tp), T(ce, cp)))
    A("Records and event descriptions", "Registros e descrições de eventos", '''from itertools import product

# 1. The sample space: one of the 5,000 identifiers
print(n, "records,", df["delivery_id"].nunique(), "distinct identifiers.")

# 2. The eight descriptions (C, H, I), 1 = yes and 0 = no
print("The eight descriptions:")
for bits in product([0, 1], repeat=3):
    print(bits)
''', '''from itertools import product

# 1. O espaço amostral: um dos 5.000 identificadores
print(n, "registros,", df["delivery_id"].nunique(), "identificadores distintos.")

# 2. As oito descrições (C, H, I), 1 = sim e 0 = não
print("As oito descrições:")
for bits in product([0, 1], repeat=3):
    print(bits)
''')
    A("Running fractions and order", "Frações acumuladas e ordem", '''# 1. Fraction of cesareans among the first k records
for k in [10, 50, 100, 500, 1000, 5000]:
    print("First", k, "records:", round(C.iloc[:k].mean(), 4))

# 2. Reverse the register order: first 100 records, and all 5,000
reverse = C.iloc[::-1]             # the same rows, from last to first
print()
print("Reversed order: first 100 records", round(reverse.iloc[:100].mean(), 4), "; all", n, "records", round(reverse.mean(), 4))
''', '''# 1. Fração de cesáreas entre os k primeiros registros
for k in [10, 50, 100, 500, 1000, 5000]:
    print("Primeiros", k, "registros:", round(C.iloc[:k].mean(), 4))

# 2. Inverter a ordem do registro: primeiros 100 registros e todos os 5.000
reverse = C.iloc[::-1]             # as mesmas linhas, da última para a primeira
print()
print("Ordem invertida: primeiros 100 registros", round(reverse.iloc[:100].mean(), 4), "; todos os", n, "registros", round(reverse.mean(), 4))
''')
    A("Count the overlap once", "Contar a sobreposição uma vez", '''# 1. The four groups: hemorrhage only, infection only, both, neither
only_h = (H & ~I).sum()
only_i = (~H & I).sum()
both = (H & I).sum()
neither = (~H & ~I).sum()
print("Hemorrhage only:", only_h, "mothers =", round(only_h / n, 4))
print("Infection only:", only_i, "mothers =", round(only_i / n, 4))
print("Both:", both, "mothers =", round(both / n, 4))
print("Neither:", neither, "mothers =", round(neither / n, 4))

# 2. Addition rule, and the same count done directly
print()
print("Addition rule:", H.sum() + I.sum() - both, "mothers with hemorrhage or infection =", round((H.sum() + I.sum() - both) / n, 4))
print("Direct count:", (H | I).sum(), "mothers")
''', '''# 1. Os quatro grupos: só hemorragia, só infecção, ambas, nenhuma
only_h = (H & ~I).sum()
only_i = (~H & I).sum()
both = (H & I).sum()
neither = (~H & ~I).sum()
print("Só hemorragia:", only_h, "mães =", round(only_h / n, 4))
print("Só infecção:", only_i, "mães =", round(only_i / n, 4))
print("Ambas:", both, "mães =", round(both / n, 4))
print("Nenhuma:", neither, "mães =", round(neither / n, 4))

# 2. Regra da adição, e a mesma contagem feita diretamente
print()
print("Regra da adição:", H.sum() + I.sum() - both, "mães com hemorragia ou infecção =", round((H.sum() + I.sum() - both) / n, 4))
print("Contagem direta:", (H | I).sum(), "mães")
''')
    A("Name the denominator", "Nomear o denominador", '''# 1. The five fractions: the numerator and the denominator of each
print("(a) infection among cesareans:", (C & I).sum(), "/", C.sum(), "=", round((C & I).sum() / C.sum(), 4))
print("(b) cesarean and infection, among all:", (C & I).sum(), "/", n, "=", round((C & I).sum() / n, 4))
print("(c) infection, among all:", I.sum(), "/", n, "=", round(I.sum() / n, 4))
print("(d) cesarean among infections:", (C & I).sum(), "/", I.sum(), "=", round((C & I).sum() / I.sum(), 4))
print("(e) hemorrhage among cesareans:", (C & H).sum(), "/", C.sum(), "=", round((C & H).sum() / C.sum(), 4))
''', '''# 1. As cinco frações: o numerador e o denominador de cada uma
print("(a) infecção entre as cesáreas:", (C & I).sum(), "/", C.sum(), "=", round((C & I).sum() / C.sum(), 4))
print("(b) cesárea e infecção, entre todos:", (C & I).sum(), "/", n, "=", round((C & I).sum() / n, 4))
print("(c) infecção, entre todos:", I.sum(), "/", n, "=", round(I.sum() / n, 4))
print("(d) cesárea entre as infecções:", (C & I).sum(), "/", I.sum(), "=", round((C & I).sum() / I.sum(), 4))
print("(e) hemorragia entre as cesáreas:", (C & H).sum(), "/", C.sum(), "=", round((C & H).sum() / C.sum(), 4))
''')
    A("Compare within delivery types", "Comparar dentro dos tipos de parto", '''# 1. Infection in each delivery type, and the ratio of the two proportions
p_cesarean = (C & I).sum() / C.sum()
p_vaginal = (~C & I).sum() / (~C).sum()
print("Infection: cesarean", round(p_cesarean, 4), "versus vaginal", round(p_vaginal, 4), "; ratio", round(p_cesarean / p_vaginal, 4))

# 2. Hemorrhage in each delivery type: count, group size, proportion
print("Hemorrhage, cesarean:", (C & H).sum(), "of", C.sum(), "=", round((C & H).sum() / C.sum(), 4))
print("Hemorrhage, vaginal:", (~C & H).sum(), "of", (~C).sum(), "=", round((~C & H).sum() / (~C).sum(), 4))
''', '''# 1. Infecção em cada tipo de parto, e a razão das duas proporções
p_cesarean = (C & I).sum() / C.sum()
p_vaginal = (~C & I).sum() / (~C).sum()
print("Infecção: cesárea", round(p_cesarean, 4), "versus vaginal", round(p_vaginal, 4), "; razão", round(p_cesarean / p_vaginal, 4))

# 2. Hemorragia em cada tipo de parto: contagem, tamanho do grupo, proporção
print("Hemorragia, cesárea:", (C & H).sum(), "de", C.sum(), "=", round((C & H).sum() / C.sum(), 4))
print("Hemorragia, vaginal:", (~C & H).sum(), "de", (~C).sum(), "=", round((~C & H).sum() / (~C).sum(), 4))
''')
    A("Dependence and overlap", "Dependência e sobreposição", '''# 1. Product of the marginals versus the observed joint fraction
p_h, p_i = H.sum() / n, I.sum() / n
print("Product of the marginals:", round(p_h * p_i, 6), "; observed joint fraction:", round((H & I).sum() / n, 4))

# 2. Infection with and without hemorrhage, and the number with both
print("Infection with hemorrhage:", round((H & I).sum() / H.sum(), 4), "; without hemorrhage:", round((~H & I).sum() / (~H).sum(), 4))
print("Mothers with both:", (H & I).sum())
''', '''# 1. Produto das marginais versus a fração conjunta observada
p_h, p_i = H.sum() / n, I.sum() / n
print("Produto das marginais:", round(p_h * p_i, 6), "; fração conjunta observada:", round((H & I).sum() / n, 4))

# 2. Infecção com e sem hemorragia, e o número com ambas
print("Infecção com hemorragia:", round((H & I).sum() / H.sum(), 4), "; sem hemorragia:", round((~H & I).sum() / (~H).sum(), 4))
print("Mães com ambas:", (H & I).sum())
''')
    A("Two routes to the same joint probability", "Dois caminhos para a mesma probabilidade conjunta", '''# 1. The counts along the way
n_c, n_h, n_ch, n_chi = C.sum(), H.sum(), (C & H).sum(), (C & H & I).sum()
print("Counts:", n_c, "cesareans,", n_h, "hemorrhages,", n_ch, "with both,", n_chi, "with all three.")

# 2. Two ways to order the conditions: C, H, I and H, C, I (they must agree)
first = (n_c / n) * (n_ch / n_c) * (n_chi / n_ch)
second = (n_h / n) * (n_ch / n_h) * (n_chi / n_ch)
print("Route C, H, I:", round(first, 4), "| route H, C, I:", round(second, 4), "| direct count:", round(n_chi / n, 4))
''', '''# 1. As contagens pelo caminho
n_c, n_h, n_ch, n_chi = C.sum(), H.sum(), (C & H).sum(), (C & H & I).sum()
print("Contagens:", n_c, "cesáreas,", n_h, "hemorragias,", n_ch, "com ambas,", n_chi, "com as três.")

# 2. Duas ordens para as condições: C, H, I e H, C, I (devem coincidir)
first = (n_c / n) * (n_ch / n_c) * (n_chi / n_ch)
second = (n_h / n) * (n_ch / n_h) * (n_chi / n_ch)
print("Caminho C, H, I:", round(first, 4), "| caminho H, C, I:", round(second, 4), "| contagem direta:", round(n_chi / n, 4))
''')
    A("Total probability and reversal", "Probabilidade total e inversão", '''# 1. Total probability of infection from the two delivery types
p_c = C.sum() / n
p_i_given_c = (C & I).sum() / C.sum()
p_i_given_not_c = (~C & I).sum() / (~C).sum()
p_i = p_i_given_c * p_c + p_i_given_not_c * (1 - p_c)
print("Total probability of infection:", round(p_i, 4))

# 2. Bayes: cesareans among the infected, and vaginal deliveries among the infected
bayes = p_i_given_c * p_c / p_i
print("Among the infected: cesarean", round(bayes, 4), "; vaginal", round(1 - bayes, 4))
print("Direct count among the infected: cesarean", round((C & I).sum() / I.sum(), 4))
''', '''# 1. Probabilidade total de infecção a partir dos dois tipos de parto
p_c = C.sum() / n
p_i_given_c = (C & I).sum() / C.sum()
p_i_given_not_c = (~C & I).sum() / (~C).sum()
p_i = p_i_given_c * p_c + p_i_given_not_c * (1 - p_c)
print("Probabilidade total de infecção:", round(p_i, 4))

# 2. Bayes: cesáreas entre as infectadas e partos vaginais entre as infectadas
bayes = p_i_given_c * p_c / p_i
print("Entre as infectadas: cesárea", round(bayes, 4), "; vaginal", round(1 - bayes, 4))
print("Contagem direta entre as infectadas: cesárea", round((C & I).sum() / I.sum(), 4))
''')
    A("Orders of the selected charts", "Ordens dos prontuários selecionados", '''from math import factorial, perm

# 1. Orders of 20 charts, and ordered first two slots
print("20! =", factorial(20), "orders; first two slots:", perm(20, 2), "ordered choices")

# 2. Chance that a given chart is first, and that two given charts are first and second
print("A given chart is first with chance", round(factorial(19) / factorial(20), 4))
print("Two given charts are first and second with chance", round(factorial(18) / factorial(20), 6))
''', '''from math import factorial, perm

# 1. Ordens de 20 prontuários, e dois primeiros lugares ordenados
print("20! =", factorial(20), "ordens; dois primeiros lugares:", perm(20, 2), "escolhas ordenadas")

# 2. Chance de um prontuário dado ser o primeiro, e de dois dados serem o primeiro e o segundo
print("Um prontuário dado é o primeiro com chance", round(factorial(19) / factorial(20), 4))
print("Dois prontuários dados são o primeiro e o segundo com chance", round(factorial(18) / factorial(20), 6))
''')
    A("A sample including an infection", "Uma amostra que inclui uma infecção", '''from math import comb

total, without_infection = n, n - I.sum()

# 1. Smallest sample with at least 90% chance of including an infection
size = 1
while 10 * comb(without_infection, size) > comb(total, size):
    size = size + 1

# 2. The chance for a sample of 20, for the size just below, and for the smallest size
for m in [20, size - 1, size]:
    print(m, "charts: chance of at least one infection =", round(1 - comb(without_infection, m) / comb(total, m), 6))
''', '''from math import comb

total, without_infection = n, n - I.sum()

# 1. Menor amostra com ao menos 90% de chance de incluir uma infecção
size = 1
while 10 * comb(without_infection, size) > comb(total, size):
    size = size + 1

# 2. A chance para uma amostra de 20, para o tamanho logo abaixo e para o menor tamanho
for m in [20, size - 1, size]:
    print(m, "prontuários: chance de ao menos uma infecção =", round(1 - comb(without_infection, m) / comb(total, m), 6))
''')
    A("Alternative marginal probabilities (alt.)", "Probabilidades marginais alternativas (alt.)", '''# 1. Alternative marginals: P(H) = 0.02 and P(I) = 0.03
p_h = 0.02
p_i = 0.03

# 2. Smallest and largest possible joint probability, and P(H or I) if independent
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print("The joint probability must lie between", lower, "and", upper)
print("If the events were independent, P(H or I) =", round(p_h + p_i - p_h * p_i, 4))
''', '''# 1. Marginais alternativas: P(H) = 0,02 e P(I) = 0,03
p_h = 0.02
p_i = 0.03

# 2. Menor e maior probabilidade conjunta possível, e P(H ou I) se independentes
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print("A probabilidade conjunta deve estar entre", lower, "e", upper)
print("Se os eventos fossem independentes, P(H ou I) =", round(p_h + p_i - p_h * p_i, 4))
''')
    A("Returning charts between draws (alt.)", "Devolver prontuários entre sorteios (alt.)", '''from math import comb

total, without_infection = n, n - I.sum()

# 1. Chance of at least one infection in 20 draws, with and without returning the chart
with_replacement = 1 - (without_infection / total) ** 20
without_replacement = 1 - comb(without_infection, 20) / comb(total, 20)
print("Returning each chart:", round(with_replacement, 6), "| not returning:", round(without_replacement, 6))

# 2. The difference between the two procedures
print("The difference is only", round(without_replacement - with_replacement, 6))
''', '''from math import comb

total, without_infection = n, n - I.sum()

# 1. Chance de ao menos uma infecção em 20 sorteios, com e sem devolver o prontuário
with_replacement = 1 - (without_infection / total) ** 20
without_replacement = 1 - comb(without_infection, 20) / comb(total, 20)
print("Devolvendo cada prontuário:", round(with_replacement, 6), "| sem devolver:", round(without_replacement, 6))

# 2. A diferença entre os dois procedimentos
print("A diferença é de apenas", round(without_replacement - with_replacement, 6))
''')
    return Q, ex

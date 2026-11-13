"""All code cells of the Chapter 11 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. Beginner-friendly Python: print with commas, round(), no f-strings."""

HELP = {"en": "", "pt": ""}

PLOTCELL = {
 "en": """# Read the register in order: does the fraction of cesareans settle?
for k in [10, 50, 100, 500, 1000, 5000]:
    first_k = C.iloc[:k]           # the first k rows
    print("After", k, "rows:", first_k.sum(), "cesareans =", round(100 * first_k.mean(), 2), "%")""",
 "pt": """# Ler o registro em ordem: a fração de cesáreas se estabiliza?
for k in [10, 50, 100, 500, 1000, 5000]:
    first_k = C.iloc[:k]           # as k primeiras linhas
    print("Após", k, "linhas:", first_k.sum(), "cesáreas =", round(100 * first_k.mean(), 2), "%")""",
}


def cells(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    S = []   # Part A: list of (kind, text) in the order of the book's sections

    def sec(num, title_en, title_pt, question_en=None, question_pt=None):
        S.append(("md", "### " + num + " " + T(title_en, title_pt) + (("\n\n*" + T(question_en, question_pt) + "*") if question_en else "")))

    def cell(en_code, pt_code):
        S.append(("code", T(en_code, pt_code)))

    sec("11.1", "Introduction: the data", "Introdução: os dados")
    cell("""import pandas as pd

df = pd.read_csv("data/deliveries.csv")

# The size of the register: rows (deliveries) and columns
rows, columns = df.shape
print("The register has", rows, "rows (one per delivery) and", columns, "columns.")
df.head()                          # the first five rows
""", """import pandas as pd

df = pd.read_csv("data/deliveries.csv")

# O tamanho do registro: linhas (partos) e colunas
rows, columns = df.shape
print("O registro tem", rows, "linhas (uma por parto) e", columns, "colunas.")
df.head()                          # as cinco primeiras linhas
""")

    sec("11.2", "Fractions in the register", "Frações no registro",
        "What fraction of deliveries were cesarean, and what fraction had a hemorrhage?",
        "Que fração dos partos foi cesárea e que fração teve hemorragia?")
    cell("""# 1. Take all the rows: one row is one delivery
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
""", """# 1. Pegar todas as linhas: cada linha é um parto
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
""")
    sec("11.2.1", "Experiment, sample space, and event", "Experimento, espaço amostral e evento")
    cell("""# The sample space is the 5,000 records; the events H and C are the records with hemorrhage and with cesarean
# With every record equally likely: P(event) = records in the event / all records
p_hemorrhage = n_hemorrhage / n
p_cesarean = n_cesarean / n
print("P(H) =", round(p_hemorrhage, 4), "and P(C) =", round(p_cesarean, 4))
print("Chance that the next mother admitted has a hemorrhage:", round(100 * p_hemorrhage, 2), "%")
""", """# O espaço amostral são os 5.000 registros; os eventos H e C são os registros com hemorragia e com cesárea
# Com todos os registros igualmente prováveis: P(evento) = registros no evento / todos os registros
p_hemorrhage = n_hemorrhage / n
p_cesarean = n_cesarean / n
print("P(H) =", round(p_hemorrhage, 4), "e P(C) =", round(p_cesarean, 4))
print("Chance de a próxima mãe admitida ter hemorragia:", round(100 * p_hemorrhage, 2), "%")
""")
    sec("11.2.2", "Why are many cases needed in a data analysis?", "Por que muitos casos são necessários em uma análise de dados?")
    S.append(("plotcell", None))

    sec("11.3", "Hemorrhage or infection: count each mother once", "Hemorragia ou infecção: contar cada mãe uma vez",
        "What is the chance that the next mother admitted has a hemorrhage or an infection?", "Qual a chance de a próxima mãe admitida ter hemorragia ou infecção?")
    cell("""# 1. Cross the two columns: each delivery falls in exactly one of four cells
table = pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total")
table.index = ["No hemorrhage", "Hemorrhage", "Total"]      # rows
table.columns = ["No infection", "Infection", "Total"]      # columns
display(table)                                             # shows the table formatted

# 2. Count the mothers with each complication, and with both
n_infection = I.sum()
n_both = (H & I).sum()             # "&" means "and": both at the same time
print()
print(n_hemorrhage, "mothers had a hemorrhage and", n_infection, "had an infection.")
print("Adding the two gives", n_hemorrhage + n_infection, "but the", n_both, "mothers with both were counted twice.")
""", """# 1. Cruzar as duas colunas: cada parto cai em exatamente uma de quatro células
table = pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total")
table.index = ["Sem hemorragia", "Hemorragia", "Total"]      # linhas
table.columns = ["Sem infecção", "Infecção", "Total"]        # colunas
display(table)                                             # mostra a tabela formatada

# 2. Contar as mães com cada complicação e com ambas
n_infection = I.sum()
n_both = (H & I).sum()             # "&" significa "e": as duas ao mesmo tempo
print()
print(n_hemorrhage, "mães tiveram hemorragia e", n_infection, "tiveram infecção.")
print("Somando as duas dá", n_hemorrhage + n_infection, "mas as", n_both, "mães com ambas foram contadas duas vezes.")
""")
    sec("11.3.1", "Rules for combining the counts", "Regras para combinar as contagens")
    cell("""# 1. Addition rule: count the mothers with both only once
print("Hemorrhage or infection:", n_hemorrhage, "+", n_infection, "-", n_both, "=", n_hemorrhage + n_infection - n_both, "mothers.")

# 2. Check by counting directly
either = H | I                     # "|" means "or": at least one of the two
n_either = either.sum()
print("Counted directly:", n_either, "of", n, "mothers =", round(100 * n_either / n, 2), "%")

# 3. Complement: the mothers with neither
print("With neither:", n - n_either, "of", n, "mothers =", round(100 * (n - n_either) / n, 2), "%")
""", """# 1. Regra da adição: contar as mães com ambas uma única vez
print("Hemorragia ou infecção:", n_hemorrhage, "+", n_infection, "-", n_both, "=", n_hemorrhage + n_infection - n_both, "mães.")

# 2. Conferir contando diretamente
either = H | I                     # "|" significa "ou": ao menos uma das duas
n_either = either.sum()
print("Contando direto:", n_either, "de", n, "mães =", round(100 * n_either / n, 2), "%")

# 3. Complemento: as mães sem nenhuma das duas
print("Sem nenhuma:", n - n_either, "de", n, "mães =", round(100 * (n - n_either) / n, 2), "%")
""")

    sec("11.4", "Infection within each delivery group", "Infecção dentro de cada grupo de parto",
        "Is infection more frequent after a cesarean?", "A infecção é mais frequente após cesárea?")
    cell("""# 1. Split the deliveries by type: cesarean, and vaginal (not cesarean)
n_vaginal = (~C).sum()             # "~" means "not"

# 2. Within each group, count the infections and divide by the size of that group
infected_cesarean = (C & I).sum()
infected_vaginal = (~C & I).sum()
print("Infection among cesarean deliveries:", infected_cesarean, "of", n_cesarean, "=", round(infected_cesarean / n_cesarean, 4))
print("Infection among vaginal deliveries:", infected_vaginal, "of", n_vaginal, "=", round(infected_vaginal / n_vaginal, 4))
""", """# 1. Separar os partos por tipo: cesárea e vaginal (não cesárea)
n_vaginal = (~C).sum()             # "~" significa "não"

# 2. Dentro de cada grupo, contar as infecções e dividir pelo tamanho desse grupo
infected_cesarean = (C & I).sum()
infected_vaginal = (~C & I).sum()
print("Infecção entre os partos cesárea:", infected_cesarean, "de", n_cesarean, "=", round(infected_cesarean / n_cesarean, 4))
print("Infecção entre os partos vaginais:", infected_vaginal, "de", n_vaginal, "=", round(infected_vaginal / n_vaginal, 4))
""")
    sec("11.4.1", "The same count can answer different questions", "A mesma contagem pode responder a perguntas diferentes")
    cell("""# 1. A mother admitted here has a vaginal delivery and, after that, an infection: two steps
p_vaginal = n_vaginal / n                                  # step 1: vaginal delivery
p_infection_after_vaginal = infected_vaginal / n_vaginal   # step 2: infection, among vaginal deliveries
print("Vaginal delivery:", round(100 * p_vaginal, 2), "% of the mothers; infection among them:", round(100 * p_infection_after_vaginal, 2), "%")
print("Vaginal delivery and then infection:", round(p_vaginal, 4), "x", round(p_infection_after_vaginal, 4), "=", round(p_vaginal * p_infection_after_vaginal, 4), "(", infected_vaginal, "of", n, ")")

# 2. Another mother has a cesarean and, after that, an infection: the two steps change
p_cesarean = n_cesarean / n                                # step 1: cesarean
p_infection_after_cesarean = infected_cesarean / n_cesarean  # step 2: infection, among cesareans
print()
print("Cesarean:", round(100 * p_cesarean, 2), "% of the mothers; infection among them:", round(100 * p_infection_after_cesarean, 2), "%")
print("Cesarean and then infection:", round(p_cesarean, 4), "x", round(p_infection_after_cesarean, 4), "=", round(p_cesarean * p_infection_after_cesarean, 4), "(", infected_cesarean, "of", n, ")")

# 3. Total probability: the two paths added give the chance of an infection over all deliveries
total_probability = p_vaginal * p_infection_after_vaginal + p_cesarean * p_infection_after_cesarean
print()
print("Total probability of infection:", round(total_probability, 4), "; direct count:", n_infection, "of", n, "=", round(n_infection / n, 4))
""", """# 1. Uma mãe admitida aqui tem um parto vaginal e, depois disso, uma infecção: dois passos
p_vaginal = n_vaginal / n                                  # passo 1: parto vaginal
p_infection_after_vaginal = infected_vaginal / n_vaginal   # passo 2: infecção, entre os partos vaginais
print("Parto vaginal:", round(100 * p_vaginal, 2), "% das mães; infecção entre elas:", round(100 * p_infection_after_vaginal, 2), "%")
print("Parto vaginal e depois infecção:", round(p_vaginal, 4), "x", round(p_infection_after_vaginal, 4), "=", round(p_vaginal * p_infection_after_vaginal, 4), "(", infected_vaginal, "de", n, ")")

# 2. Outra mãe tem uma cesárea e, depois disso, uma infecção: os dois passos mudam
p_cesarean = n_cesarean / n                                # passo 1: cesárea
p_infection_after_cesarean = infected_cesarean / n_cesarean  # passo 2: infecção, entre as cesáreas
print()
print("Cesárea:", round(100 * p_cesarean, 2), "% das mães; infecção entre elas:", round(100 * p_infection_after_cesarean, 2), "%")
print("Cesárea e depois infecção:", round(p_cesarean, 4), "x", round(p_infection_after_cesarean, 4), "=", round(p_cesarean * p_infection_after_cesarean, 4), "(", infected_cesarean, "de", n, ")")

# 3. Probabilidade total: somar os dois caminhos dá a chance de infecção entre todos os partos
total_probability = p_vaginal * p_infection_after_vaginal + p_cesarean * p_infection_after_cesarean
print()
print("Probabilidade total de infecção:", round(total_probability, 4), "; contagem direta:", n_infection, "de", n, "=", round(n_infection / n, 4))
""")

    sec("11.5", "Do hemorrhage and infection occur independently?", "Hemorragia e infecção ocorrem de forma independente?",
        "Does knowing that the next mother admitted had a hemorrhage change her chance of an infection?",
        "Saber que a próxima mãe admitida teve hemorragia muda a chance de ela ter infecção?")
    cell("""# 1. An identifier is only a label: is "identifier in the first half of the register" independent of hemorrhage?
number = df["delivery_id"].str[1:].astype(int)       # D0001 -> 1
F = number <= 2500                                    # True for D0001 to D2500
n_first = F.sum()
n_first_hemorrhage = (F & H).sum()
print("Expected if independent:", round(n_first / n, 4), "x", round(n_hemorrhage / n, 4), "=", round(n_first / n * n_hemorrhage / n, 4))
print("Observed, both together:", n_first_hemorrhage, "of", n, "=", round(n_first_hemorrhage / n, 4))
print("Hemorrhage in the first half:", round(n_first_hemorrhage / n_first, 4), "; in the second half:", round((~F & H).sum() / (~F).sum(), 4))

# 2. The contrast: hemorrhage and infection
p_h = n_hemorrhage / n
p_i = n_infection / n
print()
print("Expected if independent:", round(p_h, 4), "x", round(p_i, 4), "=", round(p_h * p_i, 6))
print("Observed, both together:", n_both, "of", n, "=", round(n_both / n, 4))

# 3. Infection within the mothers with and without hemorrhage
print("Infection among mothers with hemorrhage:", n_both, "of", n_hemorrhage, "=", round(n_both / n_hemorrhage, 4))
print("Infection among mothers without hemorrhage:", (~H & I).sum(), "of", (~H).sum(), "=", round((~H & I).sum() / (~H).sum(), 4))
""", """# 1. Um identificador é só um rótulo: "identificador na primeira metade do registro" é independente de hemorragia?
number = df["delivery_id"].str[1:].astype(int)       # D0001 -> 1
F = number <= 2500                                    # True para D0001 a D2500
n_first = F.sum()
n_first_hemorrhage = (F & H).sum()
print("Esperado se independentes:", round(n_first / n, 4), "x", round(n_hemorrhage / n, 4), "=", round(n_first / n * n_hemorrhage / n, 4))
print("Observado, os dois juntos:", n_first_hemorrhage, "de", n, "=", round(n_first_hemorrhage / n, 4))
print("Hemorragia na primeira metade:", round(n_first_hemorrhage / n_first, 4), "; na segunda metade:", round((~F & H).sum() / (~F).sum(), 4))

# 2. O contraste: hemorragia e infecção
p_h = n_hemorrhage / n
p_i = n_infection / n
print()
print("Esperado se independentes:", round(p_h, 4), "x", round(p_i, 4), "=", round(p_h * p_i, 6))
print("Observado, as duas juntas:", n_both, "de", n, "=", round(n_both / n, 4))

# 3. Infecção entre as mães com e sem hemorragia
print("Infecção entre as mães com hemorragia:", n_both, "de", n_hemorrhage, "=", round(n_both / n_hemorrhage, 4))
print("Infecção entre as mães sem hemorragia:", (~H & I).sum(), "de", (~H).sum(), "=", round((~H & I).sum() / (~H).sum(), 4))
""")

    sec("11.6", "Among infections, how many followed cesareans?", "Entre as infecções, quantas ocorreram após cesáreas?",
        "Among the mothers with infection, what fraction had a cesarean?", "Entre as mães com infecção, que fração teve cesárea?")
    cell("""# 1. The table: rows are the delivery type, columns are infection
table = pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total")
table.index = ["Vaginal", "Cesarean", "Total"]              # rows
table.columns = ["No infection", "Infection", "Total"]      # columns
display(table)                                             # shows the table formatted

# 2. Counting directly among the infected mothers
print()
print("Among the", n_infection, "infections,", infected_cesarean, "followed a cesarean =", round(100 * infected_cesarean / n_infection, 2), "%")

# 3. The same by reversing the condition (Bayes): P(C|I) = P(I|C) P(C) / P(I)
print("Reversal:", round(infected_cesarean / n_cesarean, 4), "x", round(n_cesarean / n, 4), "/", round(total_probability, 4), "=", round((infected_cesarean / n_cesarean) * (n_cesarean / n) / total_probability, 4))
""", """# 1. A tabela: linhas são o tipo de parto, colunas são a infecção
table = pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total")
table.index = ["Vaginal", "Cesárea", "Total"]                # linhas
table.columns = ["Sem infecção", "Infecção", "Total"]        # colunas
display(table)                                             # mostra a tabela formatada

# 2. Contando diretamente entre as mães infectadas
print()
print("Entre as", n_infection, "infecções,", infected_cesarean, "vieram depois de cesárea =", round(100 * infected_cesarean / n_infection, 2), "%")

# 3. O mesmo invertendo a condição (Bayes): P(C|I) = P(I|C) P(C) / P(I)
print("Inversão:", round(infected_cesarean / n_cesarean, 4), "x", round(n_cesarean / n, 4), "/", round(total_probability, 4), "=", round((infected_cesarean / n_cesarean) * (n_cesarean / n) / total_probability, 4))
""")
    sec("11.7", "Choosing charts for review", "Escolher prontuários para revisão",
        "In how many ways can 20 charts be chosen, and how likely is the sample to include an infection?",
        "De quantas maneiras se escolhem 20 prontuários e qual a chance de a amostra incluir uma infecção?")
    cell("""from math import comb, factorial, perm

total = n                          # charts in the register
without_infection = n - n_infection

# In how many ways can 20 charts be chosen? (order does not matter)
sets = comb(total, 20)
print("There are", sets, "different sets of 20 charts,", len(str(sets)), "digits.")
""", """from math import comb, factorial, perm

total = n                          # prontuários no registro
without_infection = n - n_infection

# De quantas maneiras se escolhem 20 prontuários? (a ordem não importa)
sets = comb(total, 20)
print("Há", sets, "conjuntos diferentes de 20 prontuários,", len(str(sets)), "algarismos.")
""")
    sec("11.7.1", "Does order matter?", "A ordem importa?")
    cell("""# Orders of the 20 selected charts, and of the first two slots
print("The 20 chosen charts can be put in", factorial(20), "orders; the first two slots, in", perm(20, 2))
""", """# Ordens dos 20 prontuários escolhidos, e dos dois primeiros lugares
print("Os 20 prontuários escolhidos podem ser postos em", factorial(20), "ordens; os dois primeiros lugares, em", perm(20, 2))
""")
    sec("11.7.2", "Use the sample with no infections as the complement", "Usar a amostra sem infecções como complementar")
    cell("""# 1. Chance of at least one infection = 1 - chance of none (all 20 from the charts without infection)
chance_none = comb(without_infection, 20) / comb(total, 20)
print("Chance that 20 charts include at least one infection:", round(1 - chance_none, 4))

# 2. Smallest sample with at least 90%: try sizes 1, 2, 3, ... until the chance of none is at most 10%
size = 1
while 10 * comb(without_infection, size) > comb(total, size):     # compares whole numbers, no rounding
    size = size + 1
for m in [size - 1, size]:
    print("With", m, "charts the chance is", round(1 - comb(without_infection, m) / comb(total, m), 6))
print("So", size, "is the smallest sample with at least 90%.")
""", """# 1. Chance de ao menos uma infecção = 1 - chance de nenhuma (os 20 entre os prontuários sem infecção)
chance_none = comb(without_infection, 20) / comb(total, 20)
print("Chance de 20 prontuários incluírem ao menos uma infecção:", round(1 - chance_none, 4))

# 2. Menor amostra com ao menos 90%: testar tamanhos 1, 2, 3, ... até a chance de nenhuma ser no máximo 10%
size = 1
while 10 * comb(without_infection, size) > comb(total, size):     # compara números inteiros, sem arredondar
    size = size + 1
for m in [size - 1, size]:
    print("Com", m, "prontuários a chance é", round(1 - comb(without_infection, m) / comb(total, m), 6))
print("Logo", size, "é a menor amostra com ao menos 90%.")
""")
    ex = []
    A = lambda te, tp, ce, cp: ex.append((T(te, tp), T(ce, cp)))
    A("Experiment, sample space, and marginal probabilities", "Experimento, espaço amostral e probabilidades marginais", '''# 1. The sample space is the 5,000 records; the events H, C, and I are the records with each "yes"
print("Records:", n)
print("P(H) =", n_hemorrhage, "/", n, "=", round(n_hemorrhage / n, 4))
print("P(C) =", n_cesarean, "/", n, "=", round(n_cesarean / n, 4))
print("P(I) =", n_infection, "/", n, "=", round(n_infection / n, 4))
''', '''# 1. O espaço amostral são os 5.000 registros; os eventos H, C e I são os registros com cada "yes"
print("Registros:", n)
print("P(H) =", n_hemorrhage, "/", n, "=", round(n_hemorrhage / n, 4))
print("P(C) =", n_cesarean, "/", n, "=", round(n_cesarean / n, 4))
print("P(I) =", n_infection, "/", n, "=", round(n_infection / n, 4))
''')
    A("Why many cases are needed", "Por que muitos casos são necessários", '''# 1. Fraction of hemorrhage among the first k records
for k in [10, 50, 100, 500, 1000, 5000]:
    first_k = H.iloc[:k]
    print("After", k, "rows:", first_k.sum(), "hemorrhages =", round(100 * first_k.mean(), 2), "%")

# 2. Change from 10 to 100 records and from 1,000 to 5,000 records, in percentage points
print()
print("From 10 to 100 records:", round(100 * (H.iloc[:100].mean() - H.iloc[:10].mean()), 2), "points")
print("From 1000 to 5000 records:", round(100 * (H.mean() - H.iloc[:1000].mean()), 2), "points")
''', '''# 1. Fração de hemorragia entre os k primeiros registros
for k in [10, 50, 100, 500, 1000, 5000]:
    first_k = H.iloc[:k]
    print("Após", k, "linhas:", first_k.sum(), "hemorragias =", round(100 * first_k.mean(), 2), "%")

# 2. Mudança de 10 a 100 registros e de 1.000 a 5.000 registros, em pontos percentuais
print()
print("De 10 a 100 registros:", round(100 * (H.iloc[:100].mean() - H.iloc[:10].mean()), 2), "pontos")
print("De 1000 a 5000 registros:", round(100 * (H.mean() - H.iloc[:1000].mean()), 2), "pontos")
''')
    A("OR, AND, NOT, and mutually exclusive events", "OU, E, NÃO e eventos mutuamente exclusivos", '''# 1. The four groups: hemorrhage only, infection only, both, neither
only_h = (H & ~I).sum()
only_i = (~H & I).sum()
both = (H & I).sum()
neither = (~H & ~I).sum()
print("Hemorrhage only:", only_h, "mothers =", round(only_h / n, 4))
print("Infection only:", only_i, "mothers =", round(only_i / n, 4))
print("Both:", both, "mothers =", round(both / n, 4))
print("Neither:", neither, "mothers =", round(neither / n, 4))

# 2. Addition rule for "hemorrhage or infection", and the direct count
print()
print("Addition rule:", n_hemorrhage + n_infection - both, "mothers =", round((n_hemorrhage + n_infection - both) / n, 4))
print("Direct count:", (H | I).sum(), "mothers")

# 3. Mutually exclusive events cannot occur together: count the records with both
print()
print("Cesarean and vaginal together:", (C & ~C).sum(), "records")
print("Hemorrhage and infection together:", both, "records")
''', '''# 1. Os quatro grupos: só hemorragia, só infecção, ambas, nenhuma
only_h = (H & ~I).sum()
only_i = (~H & I).sum()
both = (H & I).sum()
neither = (~H & ~I).sum()
print("Só hemorragia:", only_h, "mães =", round(only_h / n, 4))
print("Só infecção:", only_i, "mães =", round(only_i / n, 4))
print("Ambas:", both, "mães =", round(both / n, 4))
print("Nenhuma:", neither, "mães =", round(neither / n, 4))

# 2. Regra da adição para "hemorragia ou infecção", e a contagem direta
print()
print("Regra da adição:", n_hemorrhage + n_infection - both, "mães =", round((n_hemorrhage + n_infection - both) / n, 4))
print("Contagem direta:", (H | I).sum(), "mães")

# 3. Eventos mutuamente exclusivos não podem ocorrer juntos: contar os registros com ambos
print()
print("Cesárea e parto vaginal juntos:", (C & ~C).sum(), "registros")
print("Hemorragia e infecção juntas:", both, "registros")
''')
    A("Marginal, joint, and conditional fractions", "Frações marginais, conjuntas e condicionais", '''# 1. The five fractions: the numerator and the denominator of each
print("(a) infection among cesareans:", (C & I).sum(), "/", n_cesarean, "=", round((C & I).sum() / n_cesarean, 4))
print("(b) cesarean and infection, among all:", (C & I).sum(), "/", n, "=", round((C & I).sum() / n, 4))
print("(c) infection, among all:", n_infection, "/", n, "=", round(n_infection / n, 4))
print("(d) hemorrhage among cesareans:", (C & H).sum(), "/", n_cesarean, "=", round((C & H).sum() / n_cesarean, 4))
print("(e) vaginal delivery and infection, among all:", (~C & I).sum(), "/", n, "=", round((~C & I).sum() / n, 4))
''', '''# 1. As cinco frações: o numerador e o denominador de cada uma
print("(a) infecção entre as cesáreas:", (C & I).sum(), "/", n_cesarean, "=", round((C & I).sum() / n_cesarean, 4))
print("(b) cesárea e infecção, entre todos:", (C & I).sum(), "/", n, "=", round((C & I).sum() / n, 4))
print("(c) infecção, entre todos:", n_infection, "/", n, "=", round(n_infection / n, 4))
print("(d) hemorragia entre as cesáreas:", (C & H).sum(), "/", n_cesarean, "=", round((C & H).sum() / n_cesarean, 4))
print("(e) parto vaginal e infecção, entre todos:", (~C & I).sum(), "/", n, "=", round((~C & I).sum() / n, 4))
''')
    A("Two-step chances and total probability", "Chances em dois passos e probabilidade total", '''# 1. Vaginal delivery, then infection; cesarean, then infection: first step times second step
n_vaginal = (~C).sum()
path_vaginal = (n_vaginal / n) * ((~C & I).sum() / n_vaginal)
path_cesarean = (n_cesarean / n) * ((C & I).sum() / n_cesarean)
print("Vaginal delivery, then infection:", round(path_vaginal, 4), "(direct count:", round((~C & I).sum() / n, 4), ")")
print("Cesarean, then infection:", round(path_cesarean, 4), "(direct count:", round((C & I).sum() / n, 4), ")")

# 2. The two paths added are the total probability of infection, and their ratio
print()
print("Total probability of infection:", round(path_vaginal + path_cesarean, 4), "; direct count:", round(n_infection / n, 4))
print("Cesarean path divided by vaginal path:", round(path_cesarean / path_vaginal, 2))
''', '''# 1. Parto vaginal e depois infecção; cesárea e depois infecção: primeiro passo vezes segundo passo
n_vaginal = (~C).sum()
path_vaginal = (n_vaginal / n) * ((~C & I).sum() / n_vaginal)
path_cesarean = (n_cesarean / n) * ((C & I).sum() / n_cesarean)
print("Parto vaginal e depois infecção:", round(path_vaginal, 4), "(contagem direta:", round((~C & I).sum() / n, 4), ")")
print("Cesárea e depois infecção:", round(path_cesarean, 4), "(contagem direta:", round((C & I).sum() / n, 4), ")")

# 2. Os dois caminhos somados são a probabilidade total de infecção, e sua razão
print()
print("Probabilidade total de infecção:", round(path_vaginal + path_cesarean, 4), "; contagem direta:", round(n_infection / n, 4))
print("Caminho da cesárea dividido pelo caminho vaginal:", round(path_cesarean / path_vaginal, 2))
''')
    A("Independence", "Independência", '''# 1. O = the identifier is an odd number: compare P(O and C) with P(O) x P(C)
O = number % 2 == 1
print("O and C:", (O & C).sum(), "of", n, "=", round((O & C).sum() / n, 4), "; P(O) x P(C) =", round(O.mean() * C.mean(), 4))
print("Cesarean among odd identifiers:", round(C[O].mean(), 4), "; among even identifiers:", round(C[~O].mean(), 4))

# 2. Cesarean and hemorrhage
print()
print("C and H:", (C & H).sum(), "of", n, "=", round((C & H).sum() / n, 4), "; P(C) x P(H) =", round(C.mean() * H.mean(), 4))
print("Hemorrhage among cesareans:", round(H[C].mean(), 4), "; among vaginal deliveries:", round(H[~C].mean(), 4))
''', '''# 1. O = o identificador é um número ímpar: comparar P(O e C) com P(O) x P(C)
O = number % 2 == 1
print("O e C:", (O & C).sum(), "de", n, "=", round((O & C).sum() / n, 4), "; P(O) x P(C) =", round(O.mean() * C.mean(), 4))
print("Cesárea entre identificadores ímpares:", round(C[O].mean(), 4), "; entre pares:", round(C[~O].mean(), 4))

# 2. Cesárea e hemorragia
print()
print("C e H:", (C & H).sum(), "de", n, "=", round((C & H).sum() / n, 4), "; P(C) x P(H) =", round(C.mean() * H.mean(), 4))
print("Hemorragia entre as cesáreas:", round(H[C].mean(), 4), "; entre os partos vaginais:", round(H[~C].mean(), 4))
''')
    A("Reversing a condition", "Inverter uma condição", '''# 1. Among the mothers with hemorrhage, what fraction had a cesarean? Direct count
print("Direct count:", (C & H).sum(), "of", n_hemorrhage, "=", round((C & H).sum() / n_hemorrhage, 4))

# 2. The same by reversing the condition: P(C|H) = P(H|C) P(C) / P(H)
p_h_given_c = (C & H).sum() / n_cesarean
print("Reversal:", round(p_h_given_c, 4), "x", round(n_cesarean / n, 4), "/", round(n_hemorrhage / n, 4), "=", round(p_h_given_c * (n_cesarean / n) / (n_hemorrhage / n), 4))

# 3. Compare with P(C), and look at the vaginal share among the infections
print()
print("P(C) =", round(n_cesarean / n, 4))
print("Vaginal deliveries among the infections:", (~C & I).sum(), "of", n_infection, "=", round((~C & I).sum() / n_infection, 4))
''', '''# 1. Entre as mães com hemorragia, que fração teve cesárea? Contagem direta
print("Contagem direta:", (C & H).sum(), "de", n_hemorrhage, "=", round((C & H).sum() / n_hemorrhage, 4))

# 2. O mesmo invertendo a condição: P(C|H) = P(H|C) P(C) / P(H)
p_h_given_c = (C & H).sum() / n_cesarean
print("Inversão:", round(p_h_given_c, 4), "x", round(n_cesarean / n, 4), "/", round(n_hemorrhage / n, 4), "=", round(p_h_given_c * (n_cesarean / n) / (n_hemorrhage / n), 4))

# 3. Comparar com P(C), e ver a parcela de partos vaginais entre as infecções
print()
print("P(C) =", round(n_cesarean / n, 4))
print("Partos vaginais entre as infecções:", (~C & I).sum(), "de", n_infection, "=", round((~C & I).sum() / n_infection, 4))
''')
    A("Counting a review of 10 charts", "Contar uma revisão de 10 prontuários", '''# 1. Sets of 10 charts, and orders of the 10 chosen charts
sets_10 = comb(total, 10)
print("Sets of 10 charts:", sets_10, "(", len(str(sets_10)), "digits )")
print("Orders of the 10 chosen charts:", factorial(10))

# 2. Chance that 10 charts include at least one infection (complement)
print("Chance of at least one infection in 10 charts:", round(1 - comb(without_infection, 10) / comb(total, 10), 4))

# 3. Smallest sample with at least a 50% chance
size = 1
while 2 * comb(without_infection, size) > comb(total, size):
    size = size + 1
print("Smallest sample with at least 50%:", size, "charts (", round(1 - comb(without_infection, size - 1) / comb(total, size - 1), 4), "with", size - 1, ")")
''', '''# 1. Conjuntos de 10 prontuários, e ordens dos 10 prontuários escolhidos
sets_10 = comb(total, 10)
print("Conjuntos de 10 prontuários:", sets_10, "(", len(str(sets_10)), "algarismos )")
print("Ordens dos 10 prontuários escolhidos:", factorial(10))

# 2. Chance de 10 prontuários incluírem ao menos uma infecção (complementar)
print("Chance de ao menos uma infecção em 10 prontuários:", round(1 - comb(without_infection, 10) / comb(total, 10), 4))

# 3. Menor amostra com ao menos 50% de chance
size = 1
while 2 * comb(without_infection, size) > comb(total, size):
    size = size + 1
print("Menor amostra com ao menos 50%:", size, "prontuários (", round(1 - comb(without_infection, size - 1) / comb(total, size - 1), 4), "com", size - 1, ")")
''')
    A("Alternative marginal probabilities (alt.)", "Probabilidades marginais alternativas (alt.)", '''# 1. Alternative marginals: P(H) = 0.02 and P(I) = 0.03
p_h = 0.02
p_i = 0.03

# 2. Smallest and largest possible value of P(H or I), and its value if H and I were independent
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print("P(H or I) must lie between", lower, "and", upper)
print("If the events were independent, P(H or I) =", round(p_h + p_i - p_h * p_i, 4))
''', '''# 1. Marginais alternativas: P(H) = 0,02 e P(I) = 0,03
p_h = 0.02
p_i = 0.03

# 2. Menor e maior valor possível de P(H ou I), e seu valor se H e I fossem independentes
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print("P(H ou I) deve estar entre", lower, "e", upper)
print("Se os eventos fossem independentes, P(H ou I) =", round(p_h + p_i - p_h * p_i, 4))
''')
    A("Returning charts between draws (alt.)", "Devolver prontuários entre sorteios (alt.)", '''# 1. Chance of at least one infection in 20 draws, with and without returning the chart
with_replacement = 1 - (without_infection / total) ** 20
without_replacement = 1 - comb(without_infection, 20) / comb(total, 20)
print("Returning each chart:", round(with_replacement, 6), "| not returning:", round(without_replacement, 6))

# 2. The difference between the two procedures
print("The difference is only", round(without_replacement - with_replacement, 6))
''', '''# 1. Chance de ao menos uma infecção em 20 sorteios, com e sem devolver o prontuário
with_replacement = 1 - (without_infection / total) ** 20
without_replacement = 1 - comb(without_infection, 20) / comb(total, 20)
print("Devolvendo cada prontuário:", round(with_replacement, 6), "| sem devolver:", round(without_replacement, 6))

# 2. A diferença entre os dois procedimentos
print("A diferença é de apenas", round(without_replacement - with_replacement, 6))
''')
    return S, ex

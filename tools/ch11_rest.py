"""Cells for Q3 to Q6 and Part B of the Chapter 11 notebook: one cell each, reasoning as numbered comments."""


def cells(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    Qs = {}
    Qs["Q3"] = T('''# 1. Split the deliveries by type: cesarean, and vaginal (not cesarean)
groups = {"cesarean": C, "vaginal": ~C}

# 2. Within each group, count the infections and divide by the size of that group
for name, group in groups.items():
    infected, size = int((group & I).sum()), int(group.sum())
    print(f"Infection among {name:<9} {infected:>3} of {size:>5,} = {infected / size:.4f}")

# 3. The same 87 infected cesareans over ALL deliveries (a different denominator)
print(f"Cesarean and infection, among all deliveries: {int((C & I).sum())} of {n:,} = {(C & I).mean():.4f}")

# 4. Infection over all deliveries, whatever the delivery type
print(f"Infection, among all deliveries:              {int(I.sum())} of {n:,} = {I.mean():.4f}")
''', '''# 1. Separar os partos por tipo: cesárea e vaginal (não cesárea)
groups = {"cesárea": C, "vaginal": ~C}

# 2. Dentro de cada grupo, contar as infecções e dividir pelo tamanho desse grupo
for name, group in groups.items():
    infected, size = int((group & I).sum()), int(group.sum())
    print(f"Infecção entre {name:<8} {infected:>3} de {size:>5} = {infected / size:.4f}")

# 3. As mesmas 87 cesáreas infectadas sobre TODOS os partos (outro denominador)
print(f"Cesárea e infecção, entre todos os partos: {int((C & I).sum())} de {n} = {(C & I).mean():.4f}")

# 4. Infecção sobre todos os partos, qualquer que seja o tipo
print(f"Infecção, entre todos os partos:           {int(I.sum())} de {n} = {I.mean():.4f}")
''')
    Qs["Q4"] = T('''# 1. If hemorrhage and infection were independent, P(H and I) would equal P(H) x P(I)
expected = H.mean() * I.mean()
print(f"Expected under independence: {H.mean():.4f} x {I.mean():.4f} = {expected:.6f}")

# 2. What the register shows
print(f"Observed, both together:     {int((H & I).sum())} of {n:,} = {(H & I).mean():.4f}")

# 3. Infection within the mothers with and without hemorrhage
print(f"Infection among hemorrhage:    {int((H & I).sum())} of {int(H.sum())} = {I[H].mean():.4f}")
print(f"Infection among no hemorrhage: {int((~H & I).sum())} of {int((~H).sum()):,} = {I[~H].mean():.4f}\\n")

# 4. Multiplying while keeping the conditions: cesarean, then hemorrhage, then infection
print(f"Cesareans: {int(C.sum()):,} | with hemorrhage: {int((C & H).sum())} | with infection too: {int((C & H & I).sum())}")
chain = C.mean() * H[C].mean() * I[C & H].mean()
print(f"P(C) x P(H|C) x P(I|C and H) = {chain:.4f}   (direct count: {(C & H & I).mean():.4f})")
''', '''# 1. Se hemorragia e infecção fossem independentes, P(H e I) seria igual a P(H) x P(I)
expected = H.mean() * I.mean()
print(f"Esperado sob independência: {H.mean():.4f} x {I.mean():.4f} = {expected:.6f}")

# 2. O que o registro mostra
print(f"Observado, as duas juntas:  {int((H & I).sum())} de {n} = {(H & I).mean():.4f}")

# 3. Infecção entre as mães com e sem hemorragia
print(f"Infecção entre hemorragia:     {int((H & I).sum())} de {int(H.sum())} = {I[H].mean():.4f}")
print(f"Infecção entre sem hemorragia: {int((~H & I).sum())} de {int((~H).sum())} = {I[~H].mean():.4f}\\n")

# 4. Multiplicar mantendo as condições: cesárea, depois hemorragia, depois infecção
print(f"Cesáreas: {int(C.sum())} | com hemorragia: {int((C & H).sum())} | também com infecção: {int((C & H & I).sum())}")
chain = C.mean() * H[C].mean() * I[C & H].mean()
print(f"P(C) x P(H|C) x P(I|C e H) = {chain:.4f}   (contagem direta: {(C & H & I).mean():.4f})")
''')
    Qs["Q5"] = T('''# 1. The table: rows are the delivery type, columns are infection
print(pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Rebuild the overall infection fraction from the two groups
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"P(I) = P(I|C) P(C) + P(I|not C) P(not C) = {p_i:.4f}")

# 3. Reverse the condition (Bayes): from infection among cesareans to cesareans among infections
p_c_given_i = I[C].mean() * C.mean() / p_i
print(f"P(C|I) = P(I|C) P(C) / P(I) = {p_c_given_i:.4f}")

# 4. Check by counting directly among the infected mothers
print(f"Counting directly: {int((C & I).sum())} of {int(I.sum())} = {C[I].mean():.4f}  ({C[I].mean():.1%})")
''', '''# 1. A tabela: linhas são o tipo de parto, colunas são a infecção
print(pd.crosstab(df["cesarean"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Reconstruir a fração geral de infecção a partir dos dois grupos
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"P(I) = P(I|C) P(C) + P(I|não C) P(não C) = {p_i:.4f}")

# 3. Inverter a condição (Bayes): da infecção entre as cesáreas para as cesáreas entre as infecções
p_c_given_i = I[C].mean() * C.mean() / p_i
print(f"P(C|I) = P(I|C) P(C) / P(I) = {p_c_given_i:.4f}")

# 4. Conferir contando diretamente entre as mães infectadas
print(f"Contando direto: {int((C & I).sum())} de {int(I.sum())} = {C[I].mean():.4f}  ({C[I].mean():.1%})")
''')
    Qs["Q6"] = T('''from math import comb, factorial, perm

N, K = n, int(I.sum())        # N charts in the register, K of them with infection

# 1. In how many ways can 20 charts be chosen? (order does not matter)
sets = comb(N, 20)
print(f"Sets of 20 charts: {sets}  ({len(str(sets))} digits)")

# 2. Orders of the 20 selected charts, and of the first two slots
print(f"Orders of the 20 charts: {factorial(20):,}   First two slots: {perm(20, 2)}")

# 3. Chance of at least one infection = 1 - chance of none (all 20 from the N - K without infection)
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)
print(f"At least one infection in 20 charts: {p_at_least_one(20):.4f}")

# 4. Smallest sample with at least 90% (integer test: no infection is at most 1/10 of all sets)
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
for size in (m - 1, m):
    print(f"{size} charts: {p_at_least_one(size):.6f}")
''', '''from math import comb, factorial, perm

N, K = n, int(I.sum())        # N prontuários no registro, K deles com infecção

# 1. De quantas maneiras se escolhem 20 prontuários? (a ordem não importa)
sets = comb(N, 20)
print(f"Conjuntos de 20 prontuários: {sets}  ({len(str(sets))} dígitos)")

# 2. Ordens dos 20 prontuários escolhidos, e dos dois primeiros lugares
print(f"Ordens dos 20 prontuários: {factorial(20)}   Dois primeiros lugares: {perm(20, 2)}")

# 3. Chance de ao menos uma infecção = 1 - chance de nenhuma (os 20 dos N - K sem infecção)
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)
print(f"Ao menos uma infecção em 20 prontuários: {p_at_least_one(20):.4f}")

# 4. Menor amostra com ao menos 90% (teste com inteiros: nenhuma infecção é no máximo 1/10 dos conjuntos)
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
for size in (m - 1, m):
    print(f"{size} prontuários: {p_at_least_one(size):.6f}")
''')
    ex = []
    ex.append((T("Records and event descriptions", "Registros e descrições de eventos"), T('''from itertools import product

# 1. The sample space: one of the 5,000 identifiers
print(n, df["delivery_id"].nunique())

# 2. The eight descriptions (C, H, I), 1 = yes and 0 = no
print(" ".join("".join(map(str, bits)) for bits in product((0, 1), repeat=3)))
''', '''from itertools import product

# 1. O espaço amostral: um dos 5.000 identificadores
print(n, df["delivery_id"].nunique())

# 2. As oito descrições (C, H, I), 1 = sim e 0 = não
print(" ".join("".join(map(str, bits)) for bits in product((0, 1), repeat=3)))
''')))
    ex.append((T("Running fractions and order", "Frações acumuladas e ordem"), T('''# 1. Fraction of cesareans among the first k records
for k in (10, 50, 100, 500, 1000, 5000):
    print(k, f"{C.iloc[:k].mean():.4f}")

# 2. Reverse the register order: first 100 records, and all 5,000
reverse = C.iloc[::-1]
print(f"{reverse.iloc[:100].mean():.4f}", f"{reverse.mean():.4f}")
''', '''# 1. Fração de cesáreas entre os k primeiros registros
for k in (10, 50, 100, 500, 1000, 5000):
    print(k, f"{C.iloc[:k].mean():.4f}")

# 2. Inverter a ordem do registro: primeiros 100 registros e todos os 5.000
reverse = C.iloc[::-1]
print(f"{reverse.iloc[:100].mean():.4f}", f"{reverse.mean():.4f}")
''')))
    ex.append((T("Count the overlap once", "Contar a sobreposição uma vez"), T('''# 1. The four groups: hemorrhage only, infection only, both, neither
for group in (H & ~I, ~H & I, H & I, ~(H | I)):
    print(int(group.sum()), f"{group.mean():.4f}")

# 2. Addition rule, and the same count done directly
union = H.sum() + I.sum() - (H & I).sum()
print(int(union), f"{union / n:.4f}")
print(int((H | I).sum()), f"{1 - (H | I).mean():.4f}")
''', '''# 1. Os quatro grupos: só hemorragia, só infecção, ambas, nenhuma
for group in (H & ~I, ~H & I, H & I, ~(H | I)):
    print(int(group.sum()), f"{group.mean():.4f}")

# 2. Regra da adição, e a mesma contagem feita diretamente
union = H.sum() + I.sum() - (H & I).sum()
print(int(union), f"{union / n:.4f}")
print(int((H | I).sum()), f"{1 - (H | I).mean():.4f}")
''')))
    ex.append((T("Name the denominator", "Nomear o denominador"), T('''# 1. The five fractions, in the order (a) to (e)
values = (I[C].mean(), (C & I).mean(), I.mean(), C[I].mean(), H[C].mean())

# 2. Print each one
for letter, value in zip("abcde", values):
    print(letter, f"{value:.4f}")
''', '''# 1. As cinco frações, na ordem (a) a (e)
values = (I[C].mean(), (C & I).mean(), I.mean(), C[I].mean(), H[C].mean())

# 2. Imprimir cada uma
for letter, value in zip("abcde", values):
    print(letter, f"{value:.4f}")
''')))
    ex.append((T("Compare within delivery types", "Comparar dentro dos tipos de parto"), T('''# 1. Infection in each delivery type, and the ratio of the two proportions
print(f"{I[C].mean():.4f}", f"{I[~C].mean():.4f}")
print(f"{I[C].mean() / I[~C].mean():.4f}")

# 2. Hemorrhage in each delivery type: count, group size, proportion
for group in (C, ~C):
    print(int((H & group).sum()), int(group.sum()), f"{H[group].mean():.4f}")
''', '''# 1. Infecção em cada tipo de parto, e a razão das duas proporções
print(f"{I[C].mean():.4f}", f"{I[~C].mean():.4f}")
print(f"{I[C].mean() / I[~C].mean():.4f}")

# 2. Hemorragia em cada tipo de parto: contagem, tamanho do grupo, proporção
for group in (C, ~C):
    print(int((H & group).sum()), int(group.sum()), f"{H[group].mean():.4f}")
''')))
    ex.append((T("Dependence and overlap", "Dependência e sobreposição"), T('''# 1. Product of the marginals versus the observed joint fraction
print(f"{H.mean() * I.mean():.6f}", f"{(H & I).mean():.4f}")

# 2. Infection with and without hemorrhage, and the number with both
print(f"{I[H].mean():.4f}", f"{I[~H].mean():.4f}")
print(int((H & I).sum()))
''', '''# 1. Produto das marginais versus a fração conjunta observada
print(f"{H.mean() * I.mean():.6f}", f"{(H & I).mean():.4f}")

# 2. Infecção com e sem hemorragia, e o número com ambas
print(f"{I[H].mean():.4f}", f"{I[~H].mean():.4f}")
print(int((H & I).sum()))
''')))
    ex.append((T("Two routes to the same joint probability", "Dois caminhos para a mesma probabilidade conjunta"), T('''# 1. Two ways to order the conditions: C, H, I and H, C, I
first = C.mean() * H[C].mean() * I[C & H].mean()
second = H.mean() * C[H].mean() * I[C & H].mean()

# 2. The counts along the way, and the three results (they must agree)
print(int(C.sum()), int(H.sum()), int((C & H).sum()), int((C & H & I).sum()))
print(f"{first:.4f}", f"{second:.4f}", f"{(C & H & I).mean():.4f}")
''', '''# 1. Duas ordens para as condições: C, H, I e H, C, I
first = C.mean() * H[C].mean() * I[C & H].mean()
second = H.mean() * C[H].mean() * I[C & H].mean()

# 2. As contagens pelo caminho e os três resultados (devem coincidir)
print(int(C.sum()), int(H.sum()), int((C & H).sum()), int((C & H & I).sum()))
print(f"{first:.4f}", f"{second:.4f}", f"{(C & H & I).mean():.4f}")
''')))
    ex.append((T("Total probability and reversal", "Probabilidade total e inversão"), T('''# 1. Total probability of infection from the two delivery types
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"{p_i:.4f}")

# 2. Bayes: cesareans among the infected, and vaginal deliveries among the infected
bayes = I[C].mean() * C.mean() / p_i
print(f"{bayes:.4f}", f"{C[I].mean():.4f}")
print(f"{(~C)[I].mean():.4f}")
''', '''# 1. Probabilidade total de infecção a partir dos dois tipos de parto
p_i = I[C].mean() * C.mean() + I[~C].mean() * (~C).mean()
print(f"{p_i:.4f}")

# 2. Bayes: cesáreas entre as infectadas e partos vaginais entre as infectadas
bayes = I[C].mean() * C.mean() / p_i
print(f"{bayes:.4f}", f"{C[I].mean():.4f}")
print(f"{(~C)[I].mean():.4f}")
''')))
    ex.append((T("Orders of the selected charts", "Ordens dos prontuários selecionados"), T('''from math import factorial, perm

# 1. Orders of 20 charts, and ordered first two slots
print(factorial(20), perm(20, 2))

# 2. Chance that a given chart is first, and that two given charts are first and second
print(f"{factorial(19) / factorial(20):.4f}")
print(f"{factorial(18) / factorial(20):.6f}")
''', '''from math import factorial, perm

# 1. Ordens de 20 prontuários, e dois primeiros lugares ordenados
print(factorial(20), perm(20, 2))

# 2. Chance de um prontuário dado ser o primeiro, e de dois dados serem o primeiro e o segundo
print(f"{factorial(19) / factorial(20):.4f}")
print(f"{factorial(18) / factorial(20):.6f}")
''')))
    ex.append((T("A sample including an infection", "Uma amostra que inclui uma infecção"), T('''from math import comb

N, K = n, int(I.sum())

# 1. Chance of at least one infection in a sample of m charts
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)

# 2. Smallest sample with at least 90%, and its neighbour below
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
for size in (20, m - 1, m):
    print(size, f"{p_at_least_one(size):.6f}")
''', '''from math import comb

N, K = n, int(I.sum())

# 1. Chance de ao menos uma infecção em uma amostra de m prontuários
def p_at_least_one(m):
    return 1 - comb(N - K, m) / comb(N, m)

# 2. Menor amostra com ao menos 90% e a vizinha abaixo
m = next(m for m in range(1, N + 1) if 10 * comb(N - K, m) <= comb(N, m))
for size in (20, m - 1, m):
    print(size, f"{p_at_least_one(size):.6f}")
''')))
    ex.append((T("Alternative marginal probabilities (alt.)", "Probabilidades marginais alternativas (alt.)"), T('''# 1. Alternative marginals: P(H) = 0.02 and P(I) = 0.03
p_h, p_i = 0.02, 0.03

# 2. Smallest and largest possible joint probability, and P(H or I) if independent
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print(f"{lower:.4f}", f"{upper:.4f}")
print(f"{p_h + p_i - p_h * p_i:.4f}")
''', '''# 1. Marginais alternativas: P(H) = 0,02 e P(I) = 0,03
p_h, p_i = 0.02, 0.03

# 2. Menor e maior probabilidade conjunta possível, e P(H ou I) se independentes
lower = max(p_h, p_i)
upper = min(1, p_h + p_i)
print(f"{lower:.4f}", f"{upper:.4f}")
print(f"{p_h + p_i - p_h * p_i:.4f}")
''')))
    ex.append((T("Returning charts between draws (alt.)", "Devolver prontuários entre sorteios (alt.)"), T('''from math import comb

N, K = n, int(I.sum())

# 1. Chance of at least one infection in 20 draws, with and without returning the chart
with_replacement = 1 - ((N - K) / N) ** 20
without_replacement = 1 - comb(N - K, 20) / comb(N, 20)
print(f"{with_replacement:.6f}", f"{without_replacement:.6f}")

# 2. The difference between the two procedures
print(f"{without_replacement - with_replacement:.6f}")
''', '''from math import comb

N, K = n, int(I.sum())

# 1. Chance de ao menos uma infecção em 20 sorteios, com e sem devolver o prontuário
with_replacement = 1 - ((N - K) / N) ** 20
without_replacement = 1 - comb(N - K, 20) / comb(N, 20)
print(f"{with_replacement:.6f}", f"{without_replacement:.6f}")

# 2. A diferença entre os dois procedimentos
print(f"{without_replacement - with_replacement:.6f}")
''')))
    return Qs, ex

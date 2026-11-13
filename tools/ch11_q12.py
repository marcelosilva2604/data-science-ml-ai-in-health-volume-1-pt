"""One cell each for Q1 and Q2 of the Chapter 11 notebook: the reasoning is in the comments."""

PLOT = '''
import matplotlib.pyplot as plt

plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(5, 2.6))
ax.plot(range(1, n + 1), running, color="#222222", linewidth=.9)
ax.axhline(C.mean(), color="#8a8a8a", linewidth=.8, linestyle="--")
ax.set(xscale="log", xlabel="XLABEL", ylabel="YLABEL")
plt.show()'''

Q1_EN = '''import pandas as pd

df = pd.read_csv("data/deliveries.csv")

# 1. Take all the rows: one row is one delivery
n = len(df)
print(f"Deliveries in the register: {n:,}")

# 2. In each row, look at the column: is it "yes"?
C = df["cesarean"] == "yes"
H = df["hemorrhage"] == "yes"
I = df["infection"] == "yes"
print(df["cesarean"].value_counts().to_string(), "\\n")

# 3. Count the "yes" rows and divide by all the rows
for name, event in (("cesarean", C), ("hemorrhage", H)):
    count = int(event.sum())
    print(f"{name:<11} {count:>5,} of {n:,} deliveries = {count / n:.2%}")

# 4. Read the register in order: does the fraction of cesareans settle?
running = C.cumsum() / range(1, n + 1)   # cesareans so far / rows read so far
checkpoints = [10, 50, 100, 500, 1000, 5000]
print()
print(pd.DataFrame({"rows read": checkpoints,
                    "cesareans so far": [int(C.iloc[:k].sum()) for k in checkpoints],
                    "fraction": [round(running.iloc[k - 1], 4) for k in checkpoints]}).to_string(index=False))
''' 
Q1_PT = '''import pandas as pd

df = pd.read_csv("data/deliveries.csv")

# 1. Pegar todas as linhas: cada linha é um parto
n = len(df)
print(f"Partos no registro: {n}")

# 2. Em cada linha, olhar a coluna: está "yes"?
C = df["cesarean"] == "yes"
H = df["hemorrhage"] == "yes"
I = df["infection"] == "yes"
print(df["cesarean"].value_counts().to_string(), "\\n")

# 3. Contar as linhas "yes" e dividir por todas as linhas
for name, event in (("cesarean", C), ("hemorrhage", H)):
    count = int(event.sum())
    print(f"{name:<11} {count:>5} de {n} partos = {count / n:.2%}")

# 4. Ler o registro em ordem: a fração de cesáreas se estabiliza?
running = C.cumsum() / range(1, n + 1)   # cesáreas até agora / linhas lidas até agora
checkpoints = [10, 50, 100, 500, 1000, 5000]
print()
print(pd.DataFrame({"linhas lidas": checkpoints,
                    "cesáreas até agora": [int(C.iloc[:k].sum()) for k in checkpoints],
                    "fração": [round(running.iloc[k - 1], 4) for k in checkpoints]}).to_string(index=False))
'''
Q2_EN = '''# 1. Cross the two columns: each delivery falls in exactly one of four cells
print(pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Add the two groups, then correct for the mothers counted twice
hemorrhage, infection, both = int(H.sum()), int(I.sum()), int((H & I).sum())
print(f"Hemorrhage:               {hemorrhage:>4}")
print(f"Infection:                {infection:>4}")
print(f"Adding the two:           {hemorrhage + infection:>4}   (the {both} mothers with both are counted twice)")
print(f"Both:                     {both:>4}")
print(f"Hemorrhage or infection:  {hemorrhage + infection - both:>4}   = {hemorrhage} + {infection} - {both}\\n")

# 3. Check by counting directly, and count the mothers with neither
either = H | I                           # True when the row has at least one of the two
print(f"Counted directly:  {int(either.sum())} of {n:,} = {either.mean():.2%}")
print(f"With neither:      {int((~either).sum()):,} of {n:,} = {(~either).mean():.2%}")
'''
Q2_PT = '''# 1. Cruzar as duas colunas: cada parto cai em exatamente uma de quatro células
print(pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total"), "\\n")

# 2. Somar os dois grupos e corrigir as mães contadas duas vezes
hemorrhage, infection, both = int(H.sum()), int(I.sum()), int((H & I).sum())
print(f"Hemorragia:               {hemorrhage:>4}")
print(f"Infecção:                 {infection:>4}")
print(f"Somando as duas:          {hemorrhage + infection:>4}   (as {both} mães com ambas foram contadas duas vezes)")
print(f"Ambas:                    {both:>4}")
print(f"Hemorragia ou infecção:   {hemorrhage + infection - both:>4}   = {hemorrhage} + {infection} - {both}\\n")

# 3. Conferir contando diretamente e contar as mães sem nenhuma das duas
either = H | I                           # True quando a linha tem ao menos uma das duas
print(f"Contando direto:  {int(either.sum())} de {n} = {either.mean():.2%}")
print(f"Sem nenhuma:      {int((~either).sum())} de {n} = {(~either).mean():.2%}")
'''
EN = {"Q1": [("code", Q1_EN + "\n" + PLOT.strip("\n"))], "Q2": [("code", Q2_EN)]}
PT = {"Q1": [("code", Q1_PT + "\n" + PLOT.strip("\n"))], "Q2": [("code", Q2_PT)]}

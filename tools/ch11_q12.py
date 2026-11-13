"""Step-by-step cells for Q1 and Q2 of the Chapter 11 notebook (reasoning in code, readable output)."""

SETUP = '''import pandas as pd

df = pd.read_csv("data/deliveries.csv")
n = len(df)
C = df["cesarean"] == "yes"
H = df["hemorrhage"] == "yes"
I = df["infection"] == "yes"'''

EN = {
 "Q1": [
  ("md", "**Step 1.** Take all the rows. One row is one delivery."),
  ("code", SETUP + '\n\nprint(f"Deliveries in the register: {n:,}")'),
  ("md", "**Step 2.** In each row, look at the `cesarean` column: is it `yes`?"),
  ("code", 'df["cesarean"].value_counts()'),
  ("md", "**Step 3.** Count the `yes` rows and divide by all the rows. Do the same for `hemorrhage`."),
  ("code", '''for name, event in (("cesarean", C), ("hemorrhage", H)):
    count = int(event.sum())
    print(f"{name:<11} {count:>5,} of {n:,} deliveries = {count / n:.2%}")'''),
  ("md", "**Step 4.** Read the register in order. Does the fraction of cesareans settle as more rows are read?"),
  ("code", '''running = C.cumsum() / range(1, n + 1)   # cesareans so far / rows read so far
checkpoints = [10, 50, 100, 500, 1000, 5000]
pd.DataFrame({"rows read": checkpoints,
              "cesareans so far": [int(C.iloc[:k].sum()) for k in checkpoints],
              "fraction": [round(running.iloc[k - 1], 4) for k in checkpoints]})'''),
  ("plot", None),
  ("md", "**Answer to Q1.** 1,313 of the 5,000 deliveries were cesarean (26.26%) and 290 had a hemorrhage (5.80%)."),
 ],
 "Q2": [
  ("md", "**Step 1.** Cross the two columns. Each delivery falls in exactly one of four cells."),
  ("code", '''table = pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total")
table'''),
  ("md", "**Step 2.** Add the two groups, then correct for the mothers who were counted twice."),
  ("code", '''hemorrhage, infection, both = int(H.sum()), int(I.sum()), int((H & I).sum())
print(f"Hemorrhage:               {hemorrhage:>4}")
print(f"Infection:                {infection:>4}")
print(f"Adding the two:           {hemorrhage + infection:>4}   (the {both} mothers with both are counted twice)")
print(f"Both:                     {both:>4}")
print(f"Hemorrhage or infection:  {hemorrhage + infection - both:>4}   = {hemorrhage} + {infection} - {both}")'''),
  ("md", "**Step 3.** Check by counting directly, and count the mothers with neither."),
  ("code", '''either = H | I                         # True when the row has at least one of the two
print(f"Counted directly:  {int(either.sum())} of {n:,} = {either.mean():.2%}")
print(f"With neither:      {int((~either).sum()):,} of {n:,} = {(~either).mean():.2%}")'''),
  ("md", "**Answer to Q2.** 401 mothers had a hemorrhage or an infection (8.02%); 4,599 had neither."),
 ],
}

PT = {
 "Q1": [
  ("md", "**Passo 1.** Pegar todas as linhas. Cada linha é um parto."),
  ("code", SETUP + '\n\nprint(f"Partos no registro: {n}")'),
  ("md", "**Passo 2.** Em cada linha, olhar a coluna `cesarean`: está `yes`?"),
  ("code", 'df["cesarean"].value_counts()'),
  ("md", "**Passo 3.** Contar as linhas `yes` e dividir por todas as linhas. Fazer o mesmo para `hemorrhage`."),
  ("code", '''for name, event in (("cesarean", C), ("hemorrhage", H)):
    count = int(event.sum())
    print(f"{name:<11} {count:>5} de {n} partos = {count / n:.2%}")'''),
  ("md", "**Passo 4.** Ler o registro em ordem. A fração de cesáreas se estabiliza à medida que mais linhas são lidas?"),
  ("code", '''running = C.cumsum() / range(1, n + 1)   # cesáreas até agora / linhas lidas até agora
checkpoints = [10, 50, 100, 500, 1000, 5000]
pd.DataFrame({"linhas lidas": checkpoints,
              "cesáreas até agora": [int(C.iloc[:k].sum()) for k in checkpoints],
              "fração": [round(running.iloc[k - 1], 4) for k in checkpoints]})'''),
  ("plot", None),
  ("md", "**Resposta à P1.** 1.313 dos 5.000 partos foram cesárea (26,26%) e 290 tiveram hemorragia (5,80%)."),
 ],
 "Q2": [
  ("md", "**Passo 1.** Cruzar as duas colunas. Cada parto cai em exatamente uma de quatro células."),
  ("code", '''table = pd.crosstab(df["hemorrhage"], df["infection"], margins=True, margins_name="Total")
table'''),
  ("md", "**Passo 2.** Somar os dois grupos e corrigir as mães contadas duas vezes."),
  ("code", '''hemorrhage, infection, both = int(H.sum()), int(I.sum()), int((H & I).sum())
print(f"Hemorragia:               {hemorrhage:>4}")
print(f"Infecção:                 {infection:>4}")
print(f"Somando as duas:          {hemorrhage + infection:>4}   (as {both} mães com ambas foram contadas duas vezes)")
print(f"Ambas:                    {both:>4}")
print(f"Hemorragia ou infecção:   {hemorrhage + infection - both:>4}   = {hemorrhage} + {infection} - {both}")'''),
  ("md", "**Passo 3.** Conferir contando diretamente e contar as mães sem nenhuma das duas."),
  ("code", '''either = H | I                         # True quando a linha tem ao menos uma das duas
print(f"Contando direto:  {int(either.sum())} de {n} = {either.mean():.2%}")
print(f"Sem nenhuma:      {int((~either).sum())} de {n} = {(~either).mean():.2%}")'''),
  ("md", "**Resposta à P2.** 401 mães tiveram hemorragia ou infecção (8,02%); 4.599 não tiveram nenhuma das duas."),
 ],
}

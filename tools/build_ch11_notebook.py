"""Build the Chapter 11 companion notebooks (English and Portuguese).

Companion, not the book: code, data, figures, and numeric results only. Definitions, derivations,
and explanations stay in the book. Run from the repository root:  python tools/build_ch11_notebook.py
"""
from pathlib import Path
import nbformat as nbf

BASE = Path(__file__).resolve().parents[1] / "chapters" / "ch11"
FILES = {"en": "ch11_probability_en.ipynb", "pt": "ch11_probabilidade_pt.ipynb"}


def build(lang):
    pt = lang == "pt"
    T = lambda en, p: p if pt else en
    cells = []
    md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
    code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))

    md(T(r"""
# Chapter 11 · Probability: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**; no real patients appear.

**Part A** follows the chapter's case, a public maternity unit with 5,000 delivery records, through the director's four questions. **Part B** gives the code and result for each of the twelve chapter exercises (statements are in the book). Run the cells in order.
""", r"""
# Capítulo 11 · Probabilidade: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos**; nenhum paciente real aparece.

A **Parte A** percorre o caso do capítulo, uma maternidade pública com 5.000 registros de partos, pelas quatro perguntas do diretor. A **Parte B** traz o código e o resultado de cada um dos doze exercícios do capítulo (os enunciados estão no livro). Execute as células em ordem. As saídas do código usam ponto decimal.
"""))

    md(T(r"""
## Part A. The case

**Data.** `data/deliveries.csv`: one row per delivery. `stay_days` is the initial postnatal stay (readmission days are not included); the allowance of 4 days is a hypothetical assumption. Each fetal-monitoring alert adds one maternal bed-day, already inside `stay_days`. `acidemia` is a binary flag (cord arterial pH below 7.10); there are no measured pH values.

**Director's questions.** Q1 how often a stay exceeds 4 days · Q2 who has long stays · Q3 what the alert adds in bed-days · Q4 fair selection and sampling · then the bed plan.
""", r"""
## Parte A. O caso

**Dados.** `data/deliveries.csv`: uma linha por parto. `stay_days` é a internação puerperal inicial (dias de reinternação não entram); os 4 dias financiados são uma hipótese didática. Cada alerta de monitorização fetal acrescenta um dia-leito materno, já incluído em `stay_days`. `acidemia` é um indicador binário (pH arterial do cordão abaixo de 7,10); não há valores medidos de pH.

**Perguntas do diretor.** P1 com que frequência a internação passa de 4 dias · P2 quem tem internação longa · P3 o que o alerta acrescenta em dias-leito · P4 seleção e amostragem justas · depois, o plano de leitos.
"""))

    code(r"""
import random
from math import comb, factorial, perm

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False,
                     "font.size": 9, "axes.titlesize": 10})
INK, MUTED = "#222222", "#8a8a8a"

df = pd.read_csv("data/deliveries.csv")
X = df["stay_days"] > 4                      # long stay
D = df["gestational_diabetes"] == "yes"
C = df["cesarean"] == "yes"
H = df["hemorrhage"] == "yes"
R = df["readmission"] == "yes"
T = df["return_to_theatre"] == "yes"
A = df["acidemia"] == "yes"
F = df["monitor_alert"] == "yes"
any_event = H | R | T
print(df.shape)
df.head()
""")

    md(T("### Q1. How often does the stay exceed 4 days?", "### P1. Com que frequência a internação passa de 4 dias?"))
    code(r"""
print(len(df), int(X.sum()), round(X.mean(), 4))
running = X.cumsum() / range(1, len(df) + 1)
checkpoints = (10, 50, 100, 500, 1000, 5000)
print([float(round(running.iloc[k - 1], 4)) for k in checkpoints])
""")
    code(T(r"""
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(np.arange(1, len(df) + 1), running, color=INK, lw=0.9)
ax.axhline(X.mean(), color=MUTED, lw=0.8, ls=(0, (4, 2)))
ax.set(xscale="log", xlim=(1, 5000), ylim=(0, 0.36), xlabel="Deliveries included so far (log scale)",
       ylabel="Fraction with stay > 4 days", title="Running fraction of long stays")
plt.show()
""", r"""
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(np.arange(1, len(df) + 1), running, color=INK, lw=0.9)
ax.axhline(X.mean(), color=MUTED, lw=0.8, ls=(0, (4, 2)))
ax.yaxis.set_major_formatter(__import__("matplotlib.ticker", fromlist=["FuncFormatter"]).FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",")))
ax.set(xscale="log", xlim=(1, 5000), ylim=(0, 0.36), xlabel="Partos incluídos até então (escala log)",
       ylabel="Fração com internação > 4 dias", title="Fração acumulada de internações longas")
plt.show()
"""))
    md(T("**Result:** 1,216 of 5,000 deliveries (0.2432).", "**Resultado:** 1.216 de 5.000 partos (0,2432)."))
    code(r"""
print(int(H.sum()), int(R.sum()), int(T.sum()))
print(int((H & R).sum()), int((H & T).sum()), int(any_event.sum()))
p_h, p_r, p_t = H.mean(), R.mean(), T.mean()
p_hr, p_ht, p_rt, p_hrt = (H & R).mean(), (H & T).mean(), (R & T).mean(), (H & R & T).mean()
print(round(p_h + p_r + p_t, 4))
print(round(p_h + p_r + p_t - p_hr - p_ht - p_rt + p_hrt, 4))
print(round(any_event.mean(), 4), round((~any_event).mean(), 4))
""")
    md(T("**Result:** sum of the three probabilities 0.1560; with overlaps removed 0.1184 (direct count 0.1184); complement 0.8816.",
         "**Resultado:** soma das três probabilidades 0,1560; com as sobreposições removidas 0,1184 (contagem direta 0,1184); complemento 0,8816."))

    md(T("### Q2. Who has long stays?", "### P2. Quem tem internação longa?"))
    code(r"""
groups = [("D", D), ("not D", ~D), ("C", C), ("not C", ~C),
          ("any H/R/T", any_event), ("no H/R/T", ~any_event)]
for name, group in groups:
    print(name, int(group.sum()), int((X & group).sum()), f"{X[group].mean():.4f}")
print("D and X", f"{(D & X).mean():.4f}")
""")
    code(T(r"""
labels = [g[0] for g in groups]
vals = [X[g[1]].mean() for g in groups]
fig, ax = plt.subplots(figsize=(6, 2.8))
bars = ax.barh(labels[::-1], vals[::-1], color=[MUTED, INK] * 3)
ax.axvline(X.mean(), color="black", lw=0.8, ls=(0, (4, 2)))
for b, v in zip(bars, vals[::-1]):
    ax.text(v + 0.01, b.get_y() + b.get_height() / 2, f"{v:.3f}", va="center")
ax.set(xlim=(0, 0.7), xlabel="P(stay > 4 days | group)", title="Long stays by group (dashed: whole register)")
plt.show()
""", r"""
names_pt = {"D": "Diabetes gestacional", "not D": "Sem diabetes", "C": "Cesárea", "not C": "Parto vaginal",
            "any H/R/T": "Algum evento (H/R/T)", "no H/R/T": "Nenhum evento (H/R/T)"}
labels = [names_pt[g[0]] for g in groups]
vals = [X[g[1]].mean() for g in groups]
fig, ax = plt.subplots(figsize=(6, 2.8))
bars = ax.barh(labels[::-1], vals[::-1], color=[MUTED, INK] * 3)
ax.axvline(X.mean(), color="black", lw=0.8, ls=(0, (4, 2)))
for b, v in zip(bars, vals[::-1]):
    ax.text(v + 0.01, b.get_y() + b.get_height() / 2, f"{v:.3f}".replace(".", ","), va="center")
ax.xaxis.set_major_formatter(__import__("matplotlib.ticker", fromlist=["FuncFormatter"]).FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",")))
ax.set(xlim=(0, 0.7), xlabel="P(internação > 4 dias | grupo)", title="Internação longa por grupo (tracejado: registro todo)")
plt.show()
"""))
    code(r"""
print(f"{H.mean() * R.mean():.8f}", f"{(H & R).mean():.4f}")
print(f"{R[H].mean():.4f}", f"{R[~H].mean():.4f}")
chain = D.mean() * H[D].mean() * R[D & H].mean()
print(f"{chain:.4f}", f"{(D & H & R).mean():.4f}")
""")
    code(r"""
p_x = X[D].mean() * D.mean() + X[~D].mean() * (~D).mean()
print(f"{p_x:.4f}")
for name, group in [("D", D), ("C", C)]:
    posterior = X[group].mean() * group.mean() / p_x
    print(name, f"{posterior:.4f}", f"{group[X].mean():.4f}")
""")
    md(T("**Result:** long stay in 396/809 with diabetes vs 820/4,191 without; 851/1,499 cesareans vs 365/3,501 vaginal births; 335/592 with any recorded adverse event. Among long stays: 396/1,216 diabetes, 851/1,216 cesarean.",
         "**Resultado:** internação longa em 396/809 com diabetes vs 820/4.191 sem; 851/1.499 cesáreas vs 365/3.501 partos vaginais; 335/592 com algum evento adverso registrado. Entre as internações longas: 396/1.216 com diabetes, 851/1.216 cesáreas."))

    md(T("### Q3. What does the alert add in bed-days?", "### P3. O que o alerta acrescenta em dias-leito?"))
    code(r"""
print(int((A & F).sum()), int((A & ~F).sum()), int((~A & F).sum()), int((~A & ~F).sum()))
sens = F[A].mean()
spec = (~F)[~A].mean()
prior = A.mean()
posterior = sens * prior / (sens * prior + (1 - spec) * (1 - prior))
print(f"{sens:.4f}", f"{spec:.4f}", f"{prior:.4f}")
print(f"{posterior:.4f}", f"{A[F].mean():.4f}")
""")
    code(T(r"""
cell = pd.crosstab(A.map({True: "Acidemia", False: "No acidemia"}), F.map({True: "Alert", False: "No alert"}))
cell = cell.loc[["Acidemia", "No acidemia"], ["Alert", "No alert"]]
fig, ax = plt.subplots(figsize=(6, 2.2)); ax.axis("off")
t = ax.table(cellText=[[f"{v:,}" for v in row] + [f"{row.sum():,}"] for _, row in cell.iterrows()],
             rowLabels=cell.index, colLabels=list(cell.columns) + ["Total"], loc="center", cellLoc="center")
t.scale(1, 1.6); ax.set_title("Natural frequencies: 5,000 deliveries")
plt.show()
""", r"""
cell = pd.crosstab(A.map({True: "Acidemia", False: "Sem acidemia"}), F.map({True: "Alerta", False: "Sem alerta"}))
cell = cell.loc[["Acidemia", "Sem acidemia"], ["Alerta", "Sem alerta"]]
fig, ax = plt.subplots(figsize=(6, 2.2)); ax.axis("off")
t = ax.table(cellText=[[f"{v:,}".replace(",", ".") for v in row] + [f"{row.sum():,}".replace(",", ".")] for _, row in cell.iterrows()],
             rowLabels=cell.index, colLabels=list(cell.columns) + ["Total"], loc="center", cellLoc="center")
t.scale(1, 1.6); ax.set_title("Frequências naturais: 5.000 partos")
plt.show()
"""))
    code(r"""
base_stay = df["stay_days"] - F.astype(int)
added_days = df["stay_days"] - base_stay
excess_added = ((df["stay_days"] - 4).clip(lower=0) - (base_stay - 4).clip(lower=0))
crossed = F & (base_stay <= 4) & X
print(int(added_days.sum()), int(added_days[~A].sum()))
print(int(excess_added.sum()), int(crossed.sum()))
print(int((F & X).sum()), int(F.sum()), f"{X[F].mean():.3f}")
print(int((~F & X).sum()), int((~F).sum()), f"{X[~F].mean():.3f}")
""")
    md(T("**Result:** 662 alerts add 662 maternal bed-days, 465 of them after births without acidemia; 282 added days fall beyond day 4; 138 stays cross 4 days because of the added day. The register has no treatment effects, so these counts do not show whether the observation was needed.",
         "**Resultado:** 662 alertas acrescentam 662 dias-leito maternos, 465 deles após partos sem acidemia; 282 dias acrescentados caem além do 4º dia; 138 internações passam de 4 dias por causa do dia acrescentado. O registro não tem efeitos de tratamento, então estas contagens não mostram se a observação era necessária."))

    md(T("### Q4. Fair selection and sampling (hypothetical design inputs)", "### P4. Seleção e amostragem justas (insumos de planejamento hipotéticos)"))
    code(r"""
print(comb(12, 6), 2 * comb(9, 3))
print(f"{2 * comb(9, 3) / comb(12, 6):.4f}")
print(factorial(12), perm(12, 2))
none = comb(388, 20) / comb(400, 20)
print(f"{none:.4f}", f"{1 - none:.4f}")
""")
    code(T(r"""
n = np.arange(1, 201)
p_detect = 1 - np.array([comb(388, k) / comb(400, k) for k in n])
fig, ax = plt.subplots(figsize=(6, 2.8))
ax.plot(n, p_detect, color=INK, lw=1); ax.axhline(0.9, color=MUTED, lw=0.8, ls=(0, (4, 2)))
ax.plot([20], [1 - none], "o", color=INK)
ax.set(xlabel="Traces sampled (of 400)", ylabel="P(at least one disagreement)", ylim=(0, 1.02),
       title="Assuming 12 of 400 traces disagree with an expert reading")
plt.show()
""", r"""
n = np.arange(1, 201)
p_detect = 1 - np.array([comb(388, k) / comb(400, k) for k in n])
fig, ax = plt.subplots(figsize=(6, 2.8))
ax.plot(n, p_detect, color=INK, lw=1); ax.axhline(0.9, color=MUTED, lw=0.8, ls=(0, (4, 2)))
ax.plot([20], [1 - none], "o", color=INK)
ax.yaxis.set_major_formatter(__import__("matplotlib.ticker", fromlist=["FuncFormatter"]).FuncFormatter(lambda v, _: f"{v:g}".replace(".", ",")))
ax.set(xlabel="Traçados amostrados (de 400)", ylabel="P(pelo menos uma discordância)", ylim=(0, 1.02),
       title="Supondo 12 de 400 traçados discordantes de uma leitura especialista")
plt.show()
"""))
    md(T("**Result:** 924 pilot draws, 168 keeping three named teams together (0.1818); 479,001,600 training orders; 20 of 400 traces finds a disagreement with probability 0.4644.",
         "**Resultado:** 924 sorteios do piloto, 168 mantendo três equipes nomeadas juntas (0,1818); 479.001.600 ordens de treinamento; 20 de 400 traçados encontram uma discordância com probabilidade 0,4644."))

    md(T("### Bed plan", "### Plano de leitos"))
    code(r"""
mean_stay = df["stay_days"].mean()
print(int(df["stay_days"].sum()))
print(f"{mean_stay:.2f}", f"{4 - mean_stay:.2f}")
""")
    md(T("**Result:** 17,666 initial-stay bed-days; mean 3.53 days, 0.47 below the hypothetical allowance. This is arithmetic only, not evidence of spare capacity.",
         "**Resultado:** 17.666 dias-leito de internação inicial; média de 3,53 dias, 0,47 abaixo do limite hipotético. É apenas aritmética, não evidência de capacidade sobrando."))

    md(T("## Part B. Exercise solutions\n\nStatements are in the book. Exercises marked *alt.* use an alternative scenario defined in the statement.",
         "## Parte B. Soluções dos exercícios\n\nOs enunciados estão no livro. Os exercícios marcados *alt.* usam um cenário alternativo definido no enunciado."))

    def ex(n, title_en, title_pt, src=None, res_en=None, res_pt=None):
        md(f"### {T('Exercise', 'Exercício')} {n}. {T(title_en, title_pt)}")
        if src:
            if pt:
                src = (src.replace('"Alert"', '"Alerta"').replace('"No alert"', '"Sem alerta"')
                          .replace('"Acidemia present"', '"Acidemia"').replace('"Acidemia absent"', '"Sem acidemia"'))
            code(src)
        if res_en:
            md(T("**Result:** " + res_en, "**Resultado:** " + res_pt))

    ex(1, "Sample space", "Espaço amostral", None,
       "conceptual exercise; the answer is in the book.", "exercício conceitual; a resposta está no livro.")
    ex(2, "The eight probabilities", "As oito probabilidades", r"""
counts = df.groupby(["hemorrhage", "readmission", "return_to_theatre"]).size()
for outcome, count in counts.items():
    code_ = "".join("Y" if item == "yes" else "N" for item in outcome)
    print(code_, int(count), f"{count / len(df):.4f}")
print("Total", int(counts.sum()), f"{counts.sum() / len(df):.4f}")
""", "readmission alone is the most common description with an adverse event (264, 0.0528), then hemorrhage alone (144, 0.0288).",
       "reinternação isolada é a descrição mais comum com evento adverso (264, 0,0528), depois hemorragia isolada (144, 0,0288).")
    ex(3, "Hemorrhage or return to theatre", "Hemorragia ou retorno ao centro cirúrgico", r"""
print(int((H | T).sum()), f"{(H | T).mean():.4f}")
print(f"{H.mean() * T.mean():.8f}", f"{(H & T).mean():.4f}")
""", "328 deliveries (0.0656); product under independence 0.00099 vs observed 0.0108.",
       "328 partos (0,0656); produto sob independência 0,00099 vs observado 0,0108.")
    ex(4, "Delivery type and long stays", "Tipo de parto e internação longa", r"""
p_x_c = X[C].mean()
p_x_not_c = X[~C].mean()
p_x = p_x_c * C.mean() + p_x_not_c * (~C).mean()
print(f"{p_x_c:.4f}", f"{p_x_not_c:.4f}", f"{p_x_c / p_x_not_c:.2f}")
print(f"{p_x_c * C.mean() / p_x:.4f}", f"{C[X].mean():.4f}")
""", "0.5677 vs 0.1043 (ratio 5.45); P(C|X) = 851/1,216 = 0.6998 by Bayes and by count.",
       "0,5677 vs 0,1043 (razão 5,45); P(C|X) = 851/1.216 = 0,6998 por Bayes e por contagem.")
    ex(5, "Three events in sequence", "Três eventos em sequência", r"""
chain = C.mean() * H[C].mean() * T[C & H].mean()
print(int(C.sum()), int((C & H).sum()), int((C & H & T).sum()))
print(f"{chain:.4f}", f"{(C & H & T).mean():.4f}")
""", "(1,499/5,000) × (114/1,499) × (29/114) = 29/5,000 = 0.0058.", "(1.499/5.000) × (114/1.499) × (29/114) = 29/5.000 = 0,0058.")
    ex(6, "Alternative alert (alt.)", "Alerta alternativo (alt.)", r"""
scenarios = [(0.95, A.mean()), (0.95, 0.20), (0.80, A.mean())]
for sensitivity, prevalence in scenarios:
    ppv = sensitivity * prevalence / (sensitivity * prevalence + 0.10 * (1 - prevalence))
    print(f"{sensitivity:.2f}", f"{prevalence:.4f}", f"{ppv:.4f}")
""", "PPV 0.3277, 0.7037, and 0.2910 under the assumed performance values.", "VPP 0,3277, 0,7037 e 0,2910 sob os desempenhos supostos.")
    ex(7, "Scaled natural frequencies", "Frequências naturais reescaladas", r"""
scale = 10_000 / len(df)
table = pd.DataFrame({"Alert": [(A & F).sum() * scale, (~A & F).sum() * scale],
                      "No alert": [(A & ~F).sum() * scale, (~A & ~F).sum() * scale]},
                     index=["Acidemia present", "Acidemia absent"]).round().astype(int)
table["Total"] = table.sum(axis=1)
table.loc["Total"] = table.sum()
table
""", "1,324 alerts per 10,000 deliveries: 394 with acidemia, 930 without (930 added bed-days).",
       "1.324 alertas por 10.000 partos: 394 com acidemia, 930 sem (930 dias-leito acrescentados).")
    ex(8, "Ordering four selected teams", "Ordem de quatro equipes selecionadas", r"""
from itertools import permutations
orders = list(permutations(["T9", "T10", "T11", "T12"]))
first = sum(o[0] == "T12" for o in orders)
first_second = sum(o[0] == "T12" and o[1] == "T11" for o in orders)
last_two = sum(set(o[2:]) == {"T11", "T12"} for o in orders)
print(len(orders), first / len(orders), first_second / len(orders), last_two / len(orders))
""", "24 orders; 1/4, 1/12, and 1/6.", "24 ordens; 1/4, 1/12 e 1/6.")
    ex(9, "Minimum trace sample", "Amostra mínima de traçados", r"""
for n in range(1, 401):
    detection = 1 - comb(388, n) / comb(400, n)
    if detection >= 0.90:
        print(n, f"{detection:.5f}")
        previous = 1 - comb(388, n - 1) / comb(400, n - 1)
        print(n - 1, f"{previous:.5f}")
        break
""", "69 traces (0.90047); 68 gives 0.89674.", "69 traçados (0,90047); 68 dá 0,89674.")
    ex(10, "Alternative marginals (alt.)", "Marginais alternativas (alt.)", None,
       "conceptual exercise; the answer is in the book.", "exercício conceitual; a resposta está no livro.")
    ex(11, "Five years of 200 deliveries (alt.)", "Cinco anos de 200 partos (alt.)", r"""
rng = random.Random(10)
probability = float(X.mean())
annual_counts = [sum(rng.random() < probability for _ in range(200)) for _ in range(5)]
cumulative = 0
for year, count in enumerate(annual_counts, start=1):
    cumulative += count
    print(year, count, f"{count / 200:.4f}", f"{cumulative / (200 * year):.4f}")
""", "annual proportions 0.2150, 0.2750, 0.2350, 0.2050, 0.2250; cumulative 0.2150, 0.2450, 0.2417, 0.2325, 0.2310.",
       "proporções anuais 0,2150, 0,2750, 0,2350, 0,2050, 0,2250; acumuladas 0,2150, 0,2450, 0,2417, 0,2325, 0,2310.")
    ex(12, "Kinds of probability", "Tipos de probabilidade", r"""
print(int((H & D).sum()), int(D.sum()), int(H.sum()), int((A & F).sum()), int(F.sum()))
""", "the counts behind the five statements are printed above (H and D, D, H, A and F, F); the classification is in the book.",
       "as contagens por trás das cinco afirmações estão impressas acima (H e D, D, H, A e F, F); a classificação está no livro.")

    md(T("---\n*Synthetic data (seed 11, `generate_data.py`). Teaching assumptions only; nothing here is a clinical recommendation or an estimate for a real unit.*",
         "---\n*Dados sintéticos (semente 11, `generate_data.py`). Apenas hipóteses didáticas; nada aqui é recomendação clínica nem estimativa para uma unidade real.*"))

    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    out = BASE / FILES[lang]
    nbf.write(nb, out)
    print("wrote", out.name, len(cells), "cells")


if __name__ == "__main__":
    # one language per repository: tools/LANG holds "en" or "pt"
    build((Path(__file__).resolve().parent / "LANG").read_text().strip())

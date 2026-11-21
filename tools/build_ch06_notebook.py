"""Build the Chapter 6 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch06_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch06_cells import cells as all_cells
from ch06_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch06"
FILES = {"en": "ch06_describing_two_variables_en.ipynb", "pt": "ch06_descrevendo_duas_variaveis_pt.ipynb"}

HEAD = {
 "en": """# Chapter 6 · Describing Two Variables: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, one month of the triage log of an emergency department, through the director's questions; only the sections with a calculation appear (6.2, 6.3, and 6.5 to 6.11). The book draws the figures; the notebook prints the same numbers. **Part B** gives the written solution of every chapter exercise (1 to 14, and the technical note on the coordinates of the perceptual maps; statements are in the book) and, for the exercises whose solution needs a calculation (2, 4, 7, 9, 11, 13, and 14), its code and result. The code is Python 3 with pandas. Run the cells in order.

## Part A. The case

**Data.** `data/triage_month.csv`: 1,263 rows, one per emergency visit in March 2026, and 13 columns: `visit_id`, `date`, `arrived_at`, `seen_at`, `arrival_route` (1 walk-in, 2 ambulance, 3 transfer), `sex`, `age_years`, `triage_level` (1 most urgent to 5 least urgent), `pain`, `temp_c`, `heart_rate`, `prior_visits`, and `admitted`. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 6 · Descrevendo duas variáveis: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, um mês do registro de triagem de um pronto-socorro, pelas perguntas da diretoria; aparecem só as seções com cálculo (6.2, 6.3 e 6.5 a 6.11). O livro desenha as figuras; o caderno imprime os mesmos números. A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 14, e a nota técnica sobre as coordenadas dos mapas perceptuais; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (2, 4, 7, 9, 11, 13 e 14), o código e o resultado. O código é Python 3 com pandas. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/triage_month.csv`: 1.263 linhas, uma por atendimento de emergência em março de 2026, e 13 colunas: `visit_id`, `date`, `arrived_at`, `seen_at`, `arrival_route` (1 demanda espontânea, 2 ambulância, 3 transferência), `sex`, `age_years`, `triage_level` (1 mais urgente a 5 menos urgente), `pain`, `temp_c`, `heart_rate`, `prior_visits` e `admitted`. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, seed 60). Teaching values only; nothing here is an estimate for a real department.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, semente 60). Valores apenas didáticos; nada aqui é estimativa para um departamento real.*"}


def build(lang):
    cells = []
    md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
    code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))
    md(HEAD[lang])
    part_a, exs = all_cells(lang)
    for kind, text in part_a:
        (md if kind == "md" else code)(text)
    md("## Part B. Exercise solutions" if lang == "en" else "## Parte B. Soluções dos exercícios")
    code_of = {k: block for k, title, block in exs}
    for k in sorted(SOL[lang]):
        title, text = SOL[lang][k]
        if title.lower().startswith(("technical note", "nota técnica")):
            md(f"### 6.14 {title}")
        else:
            md(f"### 6.14 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
        md(text)
        if k in code_of:
            code(code_of[k])
    md(FOOT[lang])
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    out = BASE / FILES[lang]
    nbf.write(nb, out)
    print("wrote", out.name, len(cells), "cells")


if __name__ == "__main__":
    build((Path(__file__).resolve().parent / "LANG").read_text().strip())

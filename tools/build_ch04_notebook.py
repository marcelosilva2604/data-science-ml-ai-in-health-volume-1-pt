"""Build the Chapter 4 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch04_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch04_cells import cells as all_cells
from ch04_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch04"
FILES = {"en": "ch04_describing_one_variable_en.ipynb", "pt": "ch04_descrevendo_uma_variavel_pt.ipynb"}

HEAD = {
 "en": """# Chapter 4 · Describing One Variable: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, a cohort of 300 adults admitted with community-acquired pneumonia, through the author's questions; only the sections with a calculation appear (4.2, 4.4 to 4.15, 4.21, 4.22, and 4.23). The book draws the figures; the notebook prints the same numbers. **Part B** gives the written solution of every chapter exercise (1 to 19; statements are in the book) and, for the exercises whose solution needs a calculation (16, 17, and 19), its code and result. The code is Python 3 with pandas. Run the cells in order.

## Part A. The case

**Data.** `data/cohort.csv`: 300 rows, one per patient admitted in 2025, and 11 columns: `patient_id`, `admitted_on`, `sex`, `age_years`, `ward` (medicine, respiratory, geriatrics, intensive care), `severity` (low, moderate, high), `comorbidities`, `sbp_mmhg`, `spo2_pct`, `crp_mg_l`, and `los_days` (length of stay). `data/triage.csv` is a copy of the triage log of Chapter 3, used only by Exercise 17. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 4 · Descrevendo uma variável: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, uma coorte de 300 adultos internados com pneumonia adquirida na comunidade, pelas perguntas do autor; aparecem só as seções com cálculo (4.2, 4.4 a 4.15, 4.21, 4.22 e 4.23). O livro desenha as figuras; o caderno imprime os mesmos números. A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 19; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (16, 17 e 19), o código e o resultado. O código é Python 3 com pandas. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/cohort.csv`: 300 linhas, uma por paciente internado em 2025, e 11 colunas: `patient_id`, `admitted_on`, `sex`, `age_years`, `ward` (medicine, respiratory, geriatrics, intensive care), `severity` (low, moderate, high), `comorbidities`, `sbp_mmhg`, `spo2_pct`, `crp_mg_l` e `los_days` (permanência). `data/triage.csv` é uma cópia do registro de triagem do Capítulo 3, usada só pelo Exercício 17. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, seed 4). Teaching values only; nothing here is an estimate for a real hospital.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, semente 4). Valores apenas didáticos; nada aqui é estimativa para um hospital real.*"}


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
        md(f"### 4.25 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

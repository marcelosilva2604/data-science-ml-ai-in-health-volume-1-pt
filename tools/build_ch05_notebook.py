"""Build the Chapter 5 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch05_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch05_cells import cells as all_cells
from ch05_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch05"
FILES = {"en": "ch05_measures_of_frequency_en.ipynb", "pt": "ch05_medidas_de_frequencia_pt.ipynb"}

HEAD = {
 "en": """# Chapter 5 · Measures of Frequency in Health: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, the annual report of the health department of a municipality of 200,000 inhabitants, through the department's questions; only the sections with a calculation appear (5.4, 5.9, 5.10, and 5.11). **Part B** gives the written solution of every chapter exercise (1 to 14; statements are in the book) and, for the exercises whose solution needs a calculation (13 and 14), its code and result. The code is Python 3 with pandas. Run the cells in order.

## Part A. The case

**Data.** `data/diabetes_cohort.csv`: 1,200 adults followed in primary care in 2025, one row per person (`person_id`, `entered`, `exited`, `diagnosed`, `exit_reason`). `data/mortality.csv`: population and deaths by age group (7 groups) in municipality A and in neighboring municipality B. `data/surveillance.csv`: 1,000 notified cases of an arbovirus infection (`case_id`, `month`, `age_group`, `district`, `hospitalized`, `died`), used by Exercise 13. The counts of the vaccination program and of the hospital are written in the cells. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 5 · Medidas de frequência em saúde: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, o relatório anual da secretaria de saúde de um município de 200.000 habitantes, pelas perguntas da secretaria; aparecem só as seções com cálculo (5.4, 5.9, 5.10 e 5.11). A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 14; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (13 e 14), o código e o resultado. O código é Python 3 com pandas. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/diabetes_cohort.csv`: 1.200 adultos acompanhados na atenção primária em 2025, uma linha por pessoa (`person_id`, `entered`, `exited`, `diagnosed`, `exit_reason`). `data/mortality.csv`: população e óbitos por faixa etária (7 faixas) no município A e no município vizinho B. `data/surveillance.csv`: 1.000 casos notificados de uma arbovirose (`case_id`, `month`, `age_group`, `district`, `hospitalized`, `died`), usado pelo Exercício 13. As contagens do programa de vacinação e do hospital estão escritas nas células. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, seeds 5 and 51). Teaching values only; nothing here is an estimate for a real municipality.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, sementes 5 e 51). Valores apenas didáticos; nada aqui é estimativa para um município real.*"}


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
        md(f"### 5.14 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

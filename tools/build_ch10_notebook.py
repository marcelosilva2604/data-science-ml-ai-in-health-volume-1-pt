"""Build the Chapter 10 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch10_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch10_cells import cells as all_cells

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch10"
FILES = {"en": "ch10_experimental_designs_en.ipynb", "pt": "ch10_delineamentos_experimentais_pt.ipynb"}

HEAD = {
 "en": """# Chapter 10 · Experimental and Quasi-Experimental Designs in Health: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only; they have no correlation with the real world.

**Part A** follows the chapter's case, the record of a hypertension service with ten outpatient clinics, through the director's seven questions. **Part B** gives the code and result of each chapter exercise that needs code (statements are in the book). Run the cells in order.

## Part A. The case

**Data.** `data/clinic_patients.csv`: 6,744 rows, one per adult starting treatment over 24 months, and ten columns: `patient_id`, `clinic`, `month`, `period`, `clinic_start_month`, `diabetes`, `baseline_sbp`, `allocated`, `received`, `uncontrolled_12w`. Each cell carries the number of the book's section (10.1, 10.2, ...), so you can follow the chapter and the notebook side by side.""",
 "pt": """# Capítulo 10 · Delineamentos experimentais e quase-experimentais em saúde: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática; não possuem correlação com o mundo real.

A **Parte A** percorre o caso do capítulo, o registro de um serviço de hipertensão com dez ambulatórios, pelas sete perguntas do diretor. A **Parte B** traz o código e o resultado de cada exercício do capítulo que exige código (os enunciados estão no livro). Execute as células em ordem. As saídas do código usam ponto decimal.

## Parte A. O caso

**Dados.** `data/clinic_patients.csv`: 6.744 linhas, uma por adulto que iniciou o tratamento ao longo de 24 meses, e dez colunas: `patient_id`, `clinic`, `month`, `period`, `clinic_start_month`, `diabetes`, `baseline_sbp`, `allocated`, `received`, `uncontrolled_12w` (sim/não escritos `yes`/`no`). Cada célula leva o número da seção do livro (10.1, 10.2, ...), para você acompanhar o capítulo e o caderno lado a lado."""}
FOOT = {"en": "---\n*Synthetic data (seed 33, `generate_data.py`). Teaching values only; nothing here is a clinical recommendation or an estimate for a real service.*",
        "pt": "---\n*Dados sintéticos (semente 33, `generate_data.py`). Valores apenas didáticos; nada aqui é recomendação clínica nem estimativa para um serviço real.*"}


def build(lang):
    cells = []
    md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
    code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))
    md(HEAD[lang])
    part_a, exs = all_cells(lang)
    for kind, text in part_a:
        (md if kind == "md" else code)(text)
    md("## Part B. Exercise solutions" if lang == "en" else "## Parte B. Soluções dos exercícios")
    for k, title, block in exs:
        md(f"### 10.10 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
        code(block)
    md(FOOT[lang])
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    out = BASE / FILES[lang]
    nbf.write(nb, out)
    print("wrote", out.name, len(cells), "cells")


if __name__ == "__main__":
    build((Path(__file__).resolve().parent / "LANG").read_text().strip())

"""Build the Chapter 13 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch13_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch13_cells import cells as all_cells

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch13"
FILES = {"en": "ch13_sampling_estimation_en.ipynb", "pt": "ch13_amostragem_estimacao_pt.ipynb"}

HEAD = {
 "en": """# Chapter 13 · Sampling and Estimation: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, the list of schoolchildren of a municipality and an oral-health survey, through the secretary's ten questions. **Part B** gives the code and result of each chapter exercise (statements are in the book). Run the cells in order.

## Part A. The case

**Data.** `data/schoolchildren.csv`: 14,299 rows, one per enrolled child, and four columns: `child_id`, `school` (S01 to S48), `school_type` (`private` or `public`), which the education office's list holds, and `dmft`, which in real life is known only after the examination and is included here for every child so that each method can be checked against the truth. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 13 · Amostragem e estimação: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, a lista de escolares de um município e um levantamento de saúde bucal, pelas dez perguntas do secretário. A **Parte B** traz o código e o resultado de cada exercício do capítulo (os enunciados estão no livro). Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/schoolchildren.csv`: 14.299 linhas, uma por criança matriculada, e quatro colunas: `child_id`, `school` (S01 a S48), `school_type` (`private` ou `public`), que a lista da secretaria de educação traz, e `dmft`, que na vida real só é conhecido depois do exame e aqui vem para todas as crianças, para que cada método possa ser conferido contra a verdade. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (seed 13, `generate_data.py`). Teaching values only; nothing here is an estimate for a real municipality.*",
        "pt": "---\n*Dados sintéticos (semente 13, `generate_data.py`). Valores apenas didáticos; nada aqui é estimativa para um município real.*"}


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
        md(f"### 13.12 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

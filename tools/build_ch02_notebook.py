"""Build the Chapter 2 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch02_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch02_cells import cells as all_cells
from ch02_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch02"
FILES = {"en": "ch02_populations_samples_data_en.ipynb", "pt": "ch02_populacoes_amostras_dados_pt.ipynb"}

HEAD = {
 "en": """# Chapter 2 · Populations, Samples, and Data: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, the January register of discharges to home of a 500-bed hospital, through the manager's questions; only the sections with a calculation appear (2.7, 2.9, and 2.10). **Part B** gives the written solution of every chapter exercise (1 to 9; statements are in the book) and, for the exercises whose solution needs a calculation (7, 8, and 9), its code and result. The code is plain Python 3 with its standard library only. Run the cells in order.

## Part A. The case

**Data.** `data/register.csv`: 1,200 rows, one per discharge episode of January 2026, and five columns: `episode_id`, `patient_id`, `formalized_at` (when the discharge was formalized), `departed_at` (when the patient left), and `delayed` (already computed from the two times; the first cell computes it again). Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 2 · Populações, amostras e dados: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, a base de altas para casa de janeiro de um hospital de 500 leitos, pelas perguntas do gestor; aparecem só as seções com cálculo (2.7, 2.9 e 2.10). A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 9; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (7, 8 e 9), o código e o resultado. O código é Python 3 simples, só com a biblioteca padrão. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/register.csv`: 1.200 linhas, uma por episódio de alta de janeiro de 2026, e cinco colunas: `episode_id`, `patient_id`, `formalized_at` (quando a alta foi formalizada), `departed_at` (quando o paciente saiu) e `delayed` (já calculada a partir dos dois horários; a primeira célula a calcula de novo). Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, no random numbers). Teaching values only; nothing here is an estimate for a real hospital.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, sem números aleatórios). Valores apenas didáticos; nada aqui é estimativa para um hospital real.*"}


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
        md(f"### 2.13 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

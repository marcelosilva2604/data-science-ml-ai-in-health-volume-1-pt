"""Build the Chapter 9 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch09_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch09_cells import cells as all_cells
from ch09_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch09"
FILES = {"en": "ch09_diagnostic_tests_en.ipynb", "pt": "ch09_testes_diagnosticos_pt.ipynb"}

HEAD = {
 "en": """# Chapter 9 · Evaluating Diagnostic Tests and Screening: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, the evaluation of a rapid test and of a wound biomarker for surgical-site infection, through the quality directorate's questions; only the sections with a calculation appear (9.3 to 9.7). The book draws the figures; the notebook prints the same numbers. **Part B** gives the written solution of every chapter exercise (1 to 12; statements are in the book) and, for the exercises whose solution needs a calculation (3, 4, 7, 8, 9, 11, and 12), its code and result. The code is Python 3 with pandas, statsmodels, scikit-learn, and scipy. Run the cells in order.

## Part A. The case

**Data.** `data/accuracy_cohort.csv`: 1,200 consecutive 30-day follow-up visits, with the wound biomarker (`marker_ng_ml`), the rapid test (`rapid_test`), the true infection (`ssi`, the reference standard), and other fields. `data/two_gate.csv`: 100 deep infections and 100 healthy volunteers. `data/screening_cohort.csv`: 10,000 women followed for 20 years, with the times of preclinical onset, clinical diagnosis, and death. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 9 · Avaliação de testes diagnósticos e rastreamento: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, a avaliação de um teste rápido e de um biomarcador de ferida para infecção de sítio cirúrgico, pelas perguntas da diretoria de qualidade; aparecem só as seções com cálculo (9.3 a 9.7). O livro desenha as figuras; o caderno imprime os mesmos números. A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 12; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (3, 4, 7, 8, 9, 11 e 12), o código e o resultado. O código é Python 3 com pandas, statsmodels, scikit-learn e scipy. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/accuracy_cohort.csv`: 1.200 visitas consecutivas de seguimento em 30 dias, com o biomarcador da ferida (`marker_ng_ml`), o teste rápido (`rapid_test`), a infecção verdadeira (`ssi`, o padrão de referência) e outros campos. `data/two_gate.csv`: 100 infecções profundas e 100 voluntários saudáveis. `data/screening_cohort.csv`: 10.000 mulheres acompanhadas por 20 anos, com os momentos do início pré-clínico, do diagnóstico clínico e da morte. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, seed 8). Teaching values only; nothing here is an estimate for a real service.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, semente 8). Valores apenas didáticos; nada aqui é estimativa para um serviço real.*"}


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
            md(f"### 9.15 {title}")
        else:
            md(f"### 9.15 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

"""Build the Chapter 8 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch08_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch08_cells import cells as all_cells
from ch08_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch08"
FILES = {"en": "ch08_observational_designs_en.ipynb", "pt": "ch08_delineamentos_observacionais_pt.ipynb"}

HEAD = {
 "en": """# Chapter 8 · Observational Study Design in Health: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, a population of 24,000 operations in 12 hospitals that adopted an infection-prevention bundle at different times, through the quality directorate's questions; only the sections with a calculation appear (8.3, 8.5 to 8.9, 8.11, and 8.12). The book draws the figures; the notebook prints the same numbers. **Part B** gives the written solution of every chapter exercise (1 to 12; statements are in the book) and, for the exercises whose solution needs a calculation (3, 4, 5, 7, and 10), its code and result. The code is Python 3 with pandas. Run the cells in order.

## Part A. The case

**Data.** `data/population.csv`: 24,000 rows, one per operation, with the hospital, the month, the patient's diabetes and smoking (true and reported), the surgery class, the bundle (true and as recorded in the registry), the infection within 30 days (true and as classified by two assessors), and whether follow-up was complete. `data/hospitals.csv`: the 12 hospitals, with the share of contaminated operations and the month of adoption of the bundle (empty when never adopted). `data/glucose_pairs.csv`: paired glucose readings from a meter and a laboratory. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 8 · Delineamento de estudos observacionais em saúde: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, uma população de 24.000 operações em 12 hospitais que adotaram um pacote de prevenção de infecção em momentos diferentes, pelas perguntas da diretoria de qualidade; aparecem só as seções com cálculo (8.3, 8.5 a 8.9, 8.11 e 8.12). O livro desenha as figuras; o caderno imprime os mesmos números. A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 12; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (3, 4, 5, 7 e 10), o código e o resultado. O código é Python 3 com pandas. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/population.csv`: 24.000 linhas, uma por operação, com o hospital, o mês, o diabetes e o tabagismo do paciente (verdadeiro e relatado), a classe da cirurgia, o pacote (verdadeiro e como registrado), a infecção em 30 dias (verdadeira e como classificada por dois avaliadores) e se o seguimento foi completo. `data/hospitals.csv`: os 12 hospitais, com a proporção de operações contaminadas e o mês de adoção do pacote (vazio quando nunca adotado). `data/glucose_pairs.csv`: leituras pareadas de glicose de um glicosímetro e de um laboratório. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, seed 8). Teaching values only; nothing here is an estimate for a real hospital network.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, semente 8). Valores apenas didáticos; nada aqui é estimativa para uma rede hospitalar real.*"}


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
            md(f"### 8.16 {title}")
        else:
            md(f"### 8.16 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

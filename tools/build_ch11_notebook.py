"""Build the Chapter 11 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code, data, figure, and numeric results only. Definitions, derivations,
and explanations stay in the book. Code blocks come from tools/ch11_blocks.json.
Run from the repository root:  python tools/build_ch11_notebook.py
"""
import json
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch11_cells import cells as all_cells, PLOTCELL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch11"
FILES = {"en": "ch11_probability_en.ipynb", "pt": "ch11_probabilidade_pt.ipynb"}
BLOCKS = json.loads((Path(__file__).resolve().parent / "ch11_blocks.json").read_text())

HEAD = {
 "en": """# Chapter 11 · Probability: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only; they have no correlation with the real world.

**Part A** follows the chapter's case, the delivery register of a public maternity unit, through the committee's six questions. **Part B** gives the code and result of each of the twelve chapter exercises (statements are in the book). Run the cells in order.

## Part A. The case

**Data.** `data/deliveries.csv`: 5,000 rows, one per delivery, and four columns: `delivery_id`, `cesarean`, `hemorrhage`, `infection` (yes/no). Each cell carries the number of the book's section (11.1, 11.2, ...), so you can follow the chapter and the notebook side by side.""",
 "pt": """# Capítulo 11 · Probabilidade: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática; não possuem correlação com o mundo real.

A **Parte A** percorre o caso do capítulo, o registro de partos de uma maternidade pública, pelas seis perguntas do comitê. A **Parte B** traz o código e o resultado de cada um dos doze exercícios do capítulo (os enunciados estão no livro). Execute as células em ordem. As saídas do código usam ponto decimal.

## Parte A. O caso

**Dados.** `data/deliveries.csv`: 5.000 linhas, uma por parto, e quatro colunas: `delivery_id`, `cesarean`, `hemorrhage`, `infection` (sim/não, escritos `yes`/`no`). Cada célula leva o número da seção do livro (11.1, 11.2, ...), para você acompanhar o capítulo e o caderno lado a lado."""}
Q = {
 "en": ["Q1. What fraction of deliveries were cesarean, and what fraction had a hemorrhage?",
        "Q2. How many mothers had a hemorrhage or an infection?",
        "Q3. Is infection more frequent after a cesarean?",
        "Q4. Do hemorrhage and infection come together or independently?",
        "Q5. Among the mothers with infection, what fraction had a cesarean?",
        "Q6. In how many ways can 20 charts be chosen, and how likely is the sample to include an infection?"],
 "pt": ["P1. Que fração dos partos foi cesárea e que fração teve hemorragia?",
        "P2. Quantas mães tiveram hemorragia ou infecção?",
        "P3. A infecção é mais frequente após cesárea?",
        "P4. Hemorragia e infecção vêm juntas ou de modo independente?",
        "P5. Entre as mães com infecção, que fração teve cesárea?",
        "P6. De quantas maneiras se escolhem 20 prontuários e qual a chance de a amostra incluir uma infecção?"]}
AXES = {"en": ("Deliveries included so far (log scale)", "Fraction cesarean"),
        "pt": ("Partos incluídos até então (escala log)", "Fração de cesáreas")}
FOOT = {"en": "---\n*Synthetic data (seed 11, `generate_data.py`). Teaching values only; nothing here is a clinical recommendation or an estimate for a real unit.*",
        "pt": "---\n*Dados sintéticos (semente 11, `generate_data.py`). Valores apenas didáticos; nada aqui é recomendação clínica nem estimativa para uma unidade real.*"}


def build(lang):
    i = 0 if lang == "en" else 1
    cells = []
    md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
    code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))
    md(HEAD[lang])
    part_a, exs = all_cells(lang)
    for kind, text in part_a:
        if kind == "md":
            md(text)
        elif kind == "code":
            code(text)
        else:
            code(PLOTCELL[lang])
    md("## Part B. Exercise solutions" if lang == "en" else "## Parte B. Soluções dos exercícios")
    for k, (title, block) in enumerate(exs, start=1):
        md(f"### 11.9 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

"""Build the Chapter 7 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch07_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch07_cells import cells as all_cells
from ch07_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch07"
FILES = {"en": "ch07_association_and_impact_en.ipynb", "pt": "ch07_associacao_e_impacto_pt.ipynb"}

HEAD = {
 "en": """# Chapter 7 · Measures of Association and Impact in Health: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, a register of 2,400 elective-surgery patients behind the draft of an abstract, through the research fellow's questions; only the sections with a calculation appear (7.2 and 7.4 to 7.14). **Part B** gives the written solution of every chapter exercise (1 to 16; statements are in the book) and, for the exercises whose solution needs a calculation (3, 7, 12, and 14), its code and result. The code is Python 3 with pandas. Run the cells in order.

## Part A. The case

**Data.** `data/surgery_cohort.csv`: 2,400 rows, one per patient, and 11 columns: `patient_id`, `age_years`, `sex`, `diabetes`, `smoker`, `surgery_class` (clean or contaminated), `bundle` (preoperative decolonization bundle), `ssi_30d` (surgical-site infection within 30 days), `complication_30d`, `followup_days`, and `readmitted_90d`. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 7 · Medidas de associação e impacto em saúde: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, um registro de 2.400 pacientes de cirurgia eletiva por trás do rascunho de um resumo, pelas perguntas do pesquisador; aparecem só as seções com cálculo (7.2 e 7.4 a 7.14). A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 16; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (3, 7, 12 e 14), o código e o resultado. O código é Python 3 com pandas. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/surgery_cohort.csv`: 2.400 linhas, uma por paciente, e 11 colunas: `patient_id`, `age_years`, `sex`, `diabetes`, `smoker`, `surgery_class` (limpa ou contaminada), `bundle` (pacote de descolonização pré-operatório), `ssi_30d` (infecção de sítio cirúrgico em 30 dias), `complication_30d`, `followup_days` e `readmitted_90d`. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, seed 7). Teaching values only; nothing here is an estimate for a real hospital.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, semente 7). Valores apenas didáticos; nada aqui é estimativa para um hospital real.*"}


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
            md(f"### 7.17 {title}")
        else:
            md(f"### 7.17 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

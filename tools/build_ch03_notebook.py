"""Build the Chapter 3 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch03_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch03_cells import cells as all_cells
from ch03_solutions import SOL

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch03"
FILES = {"en": "ch03_variables_scales_en.ipynb", "pt": "ch03_variaveis_escalas_pt.ipynb"}

HEAD = {
 "en": """# Chapter 3 · Variables and Measurement Scales: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, one synthetic day of the triage log of an adult emergency department, through the clinical team's questions; only the sections with a calculation appear (3.1 and 3.7). **Part B** gives the written solution of every chapter exercise (1 to 13; statements are in the book) and, for the exercises whose solution needs a calculation (12 and 13), its code and result. The code is plain Python 3 with its standard library only. Run the cells in order.

## Part A. The case

**Data.** `data/triage.csv`: 200 rows, one per visit of March 9, 2026, and 12 columns: `visit_id`, `arrived_at`, `seen_at` (empty when the patient left before being seen), `arrival_route` (1 walk-in, 2 ambulance, 3 transfer), `sex`, `age_years`, `triage_level` (1 most urgent to 5 least urgent), `pain` (none, mild, moderate, severe), `temp_c` (empty when not recorded), `heart_rate`, `prior_visits`, and `admitted`. `data/triage_check.csv`: the first 12 visits as they were first typed, with three recording problems planted for the validation step. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 3 · Variáveis e escalas de medida: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, um dia sintético do registro de triagem de um pronto-socorro de adultos, pelas perguntas da equipe clínica; aparecem só as seções com cálculo (3.1 e 3.7). A **Parte B** traz a resolução escrita de todos os exercícios do capítulo (1 a 13; os enunciados estão no livro) e, nos exercícios cuja resolução precisa de cálculo (12 e 13), o código e o resultado. O código é Python 3 simples, só com a biblioteca padrão. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/triage.csv`: 200 linhas, uma por atendimento de 9 de março de 2026, e 12 colunas: `visit_id`, `arrived_at`, `seen_at` (vazio quando o paciente saiu antes de ser atendido), `arrival_route` (1 demanda espontânea, 2 ambulância, 3 transferência), `sex`, `age_years`, `triage_level` (1 mais urgente a 5 menos urgente), `pain` (nenhuma, leve, moderada, intensa), `temp_c` (vazia quando não registrada), `heart_rate`, `prior_visits` e `admitted`. `data/triage_check.csv`: os 12 primeiros atendimentos como foram digitados pela primeira vez, com três problemas de registro plantados para a etapa de validação. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (`generate_data.py`, seed 3). Teaching values only; nothing here is an estimate for a real department.*",
        "pt": "---\n*Dados sintéticos (`generate_data.py`, semente 3). Valores apenas didáticos; nada aqui é estimativa para um departamento real.*"}


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
        md(f"### 3.9 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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

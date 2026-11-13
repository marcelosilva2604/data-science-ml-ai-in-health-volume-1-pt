"""Build the Chapter 10 companion notebook (one language per repository: tools/LANG holds "en" or "pt").

Companion, not the book: code, data and numeric results only. The code cells are the chapter's own code blocks
and the worked-solution code blocks, taken in order from the chapter source; the book's explanations stay in the book.
Run from the repository root:  python tools/build_ch10_notebook.py [path-to-chapter-folder]
"""
import re
import sys
from pathlib import Path
import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
LANG = (Path(__file__).resolve().parent / "LANG").read_text().strip()
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Desktop/Volume 1 - Foundations of Data Analysis in Health/Cap10-Experimental-and-Quasi-Experimental-Designs-in-Health"
OUT = ROOT / "chapters" / "ch10" / {"en": "ch10_experimental_designs_en.ipynb", "pt": "ch10_delineamentos_experimentais_pt.ipynb"}[LANG]
pt = LANG == "pt"
T = lambda en, p: p if pt else en
tex = SRC / ("pt/cap10.tex" if pt else "cap10.tex")
sol = SRC / ("pt/solutions.tex" if pt else "solutions.tex")
BLOCK = re.compile(r"\\begin\{minted\}\{python\}\n(.*?)\\end\{minted\}", re.S)
clean = lambda s: re.sub(r"\\texorpdfstring\{(.*?)\}\{.*?\}", r"\1", s)

def sections(path, pattern):
    """Yield (title, [code blocks]) for each heading matching pattern."""
    text = path.read_text()
    marks = [(m.start(), m.end(), clean(m.group(1))) for m in re.finditer(pattern, text)]
    for i, (s, e, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        yield title, [b.strip("\n") for b in BLOCK.findall(text[e:end])]

cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))

md(T(r"""
# Chapter 10 · Experimental and Quasi-Experimental Designs in Health: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the chapter's code on the case and check the numbers. All data are **synthetic**; no real patients appear.

**The case.** A hypertension clinic and its 18 referring practices decide whether to offer two antihypertensive drugs as a single pill instead of separate tablets; the outcome is uncontrolled blood pressure at 12 weeks. Three files represent three alternative evaluations of that one decision (they are not linked follow-up of the same patients): `data/trial.csv` (individually randomized trial, 1,200 adults), `data/cluster.csv` (practice-randomized trial, 1,800 adults in practices P01-P18) and `data/monthly.csv` (24-month register, practices M01-M18).

**Part A** runs the chapter's code section by section. **Part B** gives the code and result for the chapter exercises that need code (statements are in the book). Run the cells in order.
""", r"""
# Capítulo 10 · Delineamentos experimentais e quase-experimentais em saúde: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa o código do capítulo sobre o caso e confere os números. Todos os dados são **sintéticos**; nenhum paciente real aparece.

**O caso.** Um ambulatório de hipertensão e seus 18 consultórios de referência decidem se oferecem dois anti-hipertensivos em uma pílula única em vez de comprimidos separados; o desfecho é a pressão arterial não controlada em 12 semanas. Três arquivos representam três avaliações alternativas dessa mesma decisão (não são seguimento vinculado dos mesmos pacientes): `data/trial.csv` (ensaio randomizado individual, 1.200 adultos), `data/cluster.csv` (ensaio randomizado por consultórios, 1.800 adultos nos consultórios P01-P18) e `data/monthly.csv` (registro de 24 meses, consultórios M01-M18).

A **Parte A** executa o código do capítulo seção por seção. A **Parte B** traz o código e o resultado dos exercícios do capítulo que exigem código (os enunciados estão no livro). Execute as células em ordem. As saídas do código usam ponto decimal.
"""))

md(T("## Part A. The case", "## Parte A. O caso"))
for title, blocks in sections(tex, r"\\section\{(.*?)\}\n"):
    if not blocks:
        continue
    md(f"### {title}")
    for b in blocks:
        code(b)

md(T("## Part B. Exercise solutions", "## Parte B. Soluções dos exercícios"))
md(T("Exercises without code (conceptual answers) are answered in the book.", "Os exercícios sem código (respostas conceituais) são respondidos no livro."))
for title, blocks in sections(sol, r"\\subsection\*\{(.*?)\}\n"):
    if not blocks:
        continue
    md(f"### {T('Exercise', 'Exercício')} {title}")
    for b in blocks:
        code(b)

md(T("---\n*Synthetic data (seed 10, `generate_data.py`). Teaching assumptions only; nothing here is a clinical recommendation or an estimate for a real service.*",
     "---\n*Dados sintéticos (semente 10, `generate_data.py`). Apenas hipóteses didáticas; nada aqui é recomendação clínica nem estimativa para um serviço real.*"))

nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
OUT.parent.mkdir(parents=True, exist_ok=True)
nbf.write(nb, OUT)
print("wrote", OUT.name, len(cells), "cells")

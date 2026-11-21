"""Execute every chapter notebook and export it to docs/<chapter>.html, then rebuild docs/index.html.

Run from the repository root:  python tools/build_site.py
"""
from pathlib import Path
import html
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CHAPTERS = [
    ("ch02_pt", "pt", "Capítulo 2", "Populações, amostras e dados",
     "Caso: o gestor de um hospital de 500 leitos audita uma amostra das altas para casa de janeiro para saber com que frequência a alta atrasa.", "chapters/ch02/ch02_populacoes_amostras_dados_pt.ipynb"),
    ("ch03_pt", "pt", "Capítulo 3", "Variáveis e escalas de medida",
     "Caso: um médico assistente começa o plantão da manhã de um pronto-socorro de adultos e lê um registro de triagem de 200 atendimentos.", "chapters/ch03/ch03_variaveis_escalas_pt.ipynb"),
    ("ch04_pt", "pt", "Capítulo 4", "Descrevendo uma variável",
     "Caso: um autor descreve uma coorte de 300 adultos internados com pneumonia adquirida na comunidade para a primeira tabela de um manuscrito.", "chapters/ch04/ch04_descrevendo_uma_variavel_pt.ipynb"),
    ("ch05_pt", "pt", "Capítulo 5", "Medidas de frequência em saúde",
     "Caso: a secretaria de saúde de um município de 200.000 habitantes confere os números de destaque do seu relatório anual.", "chapters/ch05/ch05_medidas_de_frequencia_pt.ipynb"),
    ("ch06_pt", "pt", "Capítulo 6", "Descrevendo duas variáveis",
     "Caso: o diretor médico de um pronto-socorro estuda um mês do registro de triagem: via de chegada, nível de triagem, internação e espera.", "chapters/ch06/ch06_descrevendo_duas_variaveis_pt.ipynb"),
    ("ch10_pt", "pt", "Capítulo 10", "Delineamentos experimentais e quase-experimentais em saúde",
     "Caso: um serviço de hipertensão com dez ambulatórios decide se oferece pílula única em vez de comprimidos separados.", "chapters/ch10/ch10_delineamentos_experimentais_pt.ipynb"),
    ("ch11_en", "en", "Chapter 11", "Probability: The Language of Uncertainty",
     "Case: the infection-control committee of a public maternity unit reviews a register of 5,000 deliveries.", "chapters/ch11/ch11_probability_en.ipynb"),
    ("ch11_pt", "pt", "Capítulo 11", "Probabilidade: a linguagem da incerteza",
     "Caso: o comitê de controle de infecção de uma maternidade pública revisa um registro de 5.000 partos.", "chapters/ch11/ch11_probabilidade_pt.ipynb"),
    ("ch13_pt", "pt", "Capítulo 13", "Amostragem e estimação",
     "Caso: uma secretaria de saúde sorteia escolares para um levantamento de saúde bucal, a partir de uma lista de 14.299 crianças em 48 escolas.", "chapters/ch13/ch13_amostragem_estimacao_pt.ipynb"),
]
PARTS = {"en": ("Part A. The case", "Part B. Exercise solutions", "#Part-A.-The-case", "#Part-B.-Exercise-solutions"),
         "pt": ("Parte A. O caso", "Parte B. Soluções dos exercícios", "#Parte-A.-O-caso", "#Parte-B.-Solu%C3%A7%C3%B5es-dos-exerc%C3%ADcios")}

NAV_CSS = """
<style>
.vol-bar{position:sticky;top:0;z-index:50;background:#1f2933;color:#fff;font:14px/1.4 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;
 padding:10px 24px;display:flex;gap:22px;align-items:center;flex-wrap:wrap}
.vol-bar a{color:#cfe3ff;text-decoration:none}.vol-bar a:hover{text-decoration:underline}
.vol-bar .grow{flex:1}
.jp-Notebook{max-width:980px;margin:0 auto}
</style>"""

def bar(title, lang):
    a, b, ha, hb = PARTS[lang]
    return (f'<div class="vol-bar"><a href="index.html"><b>Volume 1</b></a><span>{html.escape(title)}</span><span class="grow"></span>'
            f'<a href="{ha}">{a}</a><a href="{hb}">{b}</a></div>')

def build(ch, lang, label, title, blurb, rel):
    nb_path = ROOT / rel
    nb = nbformat.read(nb_path, as_version=4)
    ep = ExecutePreprocessor(timeout=300, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": str(nb_path.parent)}})
    nbformat.write(nb, nb_path)                       # keep outputs in the committed notebook
    body, _ = HTMLExporter(template_name="lab").from_notebook_node(nb)
    body = body.replace("</head>", NAV_CSS + "</head>", 1)
    body = body.replace('<html lang="en"', f'<html lang="{lang}"', 1)
    import re
    body = re.sub(r"<title>.*?</title>", f"<title>{html.escape(label)}. {html.escape(title)}</title>", body, count=1, flags=re.S)
    body = body.replace("<body", "<body", 1)
    i = body.find(">", body.find("<body")) + 1
    body = body[:i] + bar(f"{label}. {title}", lang) + body[i:]
    (DOCS / f"{ch}.html").write_text(body, encoding="utf-8")
    print("built", ch)

def index():
    items = "".join(
        f'<li><a href="{ch}.html"><b>{html.escape(label)}. {html.escape(title)}</b></a><br><span>{html.escape(blurb)}</span></li>'
        for ch, lang, label, title, blurb, rel in CHAPTERS)
    if LANG == "pt":
        head = "Fundamentos da Análise de Dados em Saúde"
        sub = "Dados, Delineamento de Estudos, Probabilidade e Inferência Clássica · Volume 1 · cadernos complementares"
        blurb = "Cadernos complementares ao livro (não o reproduzem): a Parte A percorre o caso do capítulo; a Parte B traz o código e o resultado de cada exercício. Todos os dados são sintéticos."
        foot = "Novos capítulos serão acrescentados à medida que ficarem prontos. Cada capítulo é autônomo: lê apenas os próprios dados."
        doc_lang, doc_title = "pt", "Fundamentos da Análise de Dados em Saúde, Volume 1: cadernos complementares"
    else:
        head = "Foundations of Data Analysis in Health"
        sub = "Data, Study Design, Probability, and Classical Inference · Volume 1 · companion notebooks"
        blurb = "Companion notebooks to the book (they do not reproduce it): Part A follows the chapter's case, Part B gives the code and result of each exercise. All data are synthetic."
        foot = "More chapters will be added as they are finished. Each chapter is self-contained: it reads only its own data."
        doc_lang, doc_title = "en", "Foundations of Data Analysis in Health, Volume 1: companion notebooks"
    page = f"""<!DOCTYPE html><html lang="{doc_lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{doc_title}</title>
<style>body{{font:16px/1.55 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:760px;margin:40px auto;padding:0 20px;color:#1f2933}}
h1{{font-size:26px;margin-bottom:4px}}li{{margin:16px 0}}a{{color:#0b5cad}}p.s{{color:#52606d}}</style></head><body>
<h1>{head}</h1><p class="s">{sub}</p>
<p class="s">{blurb}</p>
<ul>{items}</ul>
<p class="s">{foot}</p></body></html>"""
    (DOCS / "index.html").write_text(page, encoding="utf-8")

LANG = (Path(__file__).resolve().parent / "LANG").read_text().strip()
CHAPTERS = [c for c in CHAPTERS if c[1] == LANG]

if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    for c in CHAPTERS:
        build(*c)
    index()

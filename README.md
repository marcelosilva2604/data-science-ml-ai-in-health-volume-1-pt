# Fundamentos da Análise de Dados em Saúde, Volume 1: cadernos complementares (português)

*Dados, Delineamento de Estudos, Probabilidade e Inferência Clássica.* Parte da obra **Ciência de Dados e Inteligência Artificial em Saúde**.

Cadernos complementares ao livro, um por capítulo. Eles **não reproduzem o livro**: definições, deduções e explicações ficam no livro. Cada caderno roda da primeira à última célula e tem duas partes:

- **Parte A. O caso**: o caso único do capítulo, com os cálculos e as figuras.
- **Parte B. Soluções dos exercícios**: o código e o resultado numérico de cada exercício (os enunciados estão no livro).

Todos os dados são **sintéticos**; nenhum paciente real aparece. Cada capítulo é autônomo e lê apenas os próprios dados.

## Capítulos

| Capítulo | Caso | Caderno | Página |
|---|---|---|---|
| 11. Probabilidade: a linguagem da incerteza | Maternidade pública, 5.000 partos | `chapters/ch11/ch11_probabilidade_pt.ipynb` | `docs/ch11_pt.html` |

## Estrutura

```
chapters/chNN/   caderno, data/, generate_data.py (tudo o que o capítulo precisa)
docs/            páginas HTML (index.html + uma página por capítulo), prontas para o GitHub Pages
tools/           build_ch11_notebook.py (escreve o caderno), build_site.py (executa e exporta o HTML), LANG
tests/           test_ch11.py (confere os números citados no texto contra os dados)
```

## Como executar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
(cd chapters/ch11 && jupyter lab ch11_probabilidade_pt.ipynb)      # ou abra o caderno no VS Code
```

Reconstruir as páginas: `python tools/build_ch11_notebook.py && python tools/build_site.py`. Conferir os números: `python tests/test_ch11.py`.

## Revisão

Os cadernos do Capítulo 11 seguem o rascunho revisado do capítulo de 12/11/2026 (caso da maternidade). Alguns insumos dos exercícios, como a prevalência exata de acidemia 0,0488 no Exercício 6 e a proporção exata de internações longas 0,2432 no Exercício 11, seguem esse rascunho.

## Observações

Os dados sintéticos e as hipóteses didáticas (os 4 dias financiados, a regra de um dia por alerta) estão declarados no caderno. Nada aqui é recomendação clínica nem estimativa para uma unidade real. As saídas do código usam ponto decimal.

## Online

Páginas: https://marcelosilva2604.github.io/data-science-ml-ai-in-health-volume-1-pt/ · Repositório: https://github.com/marcelosilva2604/data-science-ml-ai-in-health-volume-1-pt

**O nome do repositório e o ramo `main` estão impressos nos QR codes do livro. Não os renomeie, mova nem apague.** Se as páginas mudarem de lugar (por exemplo, para o site da editora), atualize os links deste README; os QR codes continuam apontando para cá.

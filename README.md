# Fundamentos da Análise de Dados em Saúde, Volume 1: cadernos complementares (português)

*Dados, Delineamento de Estudos, Probabilidade e Inferência Clássica.* Parte da obra **Ciência de Dados e Inteligência Artificial em Saúde**.

Cadernos complementares ao livro, um por capítulo. Eles **não reproduzem o livro**: definições, deduções e explicações ficam no livro. Cada caderno roda da primeira à última célula e tem duas partes:

- **Parte A. O caso**: o caso único do capítulo, com os cálculos e as figuras.
- **Parte B. Soluções dos exercícios**: o código e o resultado numérico de cada exercício (os enunciados estão no livro).

Todos os dados são **sintéticos**; nenhum paciente real aparece. Cada capítulo é autônomo e lê apenas os próprios dados.

## Capítulos

| Capítulo | Caso | Caderno | Página |
|---|---|---|---|
| 2. Populações, amostras e dados | Hospital de 500 leitos: auditoria de uma amostra das altas para casa de janeiro | `chapters/ch02/ch02_populacoes_amostras_dados_pt.ipynb` | `docs/ch02_pt.html` |
| 3. Variáveis e escalas de medida | Pronto-socorro de adultos: registro de triagem de 200 atendimentos | `chapters/ch03/ch03_variaveis_escalas_pt.ipynb` | `docs/ch03_pt.html` |
| 4. Descrevendo uma variável | Coorte de 300 adultos internados com pneumonia: descrição da amostra | `chapters/ch04/ch04_descrevendo_uma_variavel_pt.ipynb` | `docs/ch04_pt.html` |
| 5. Medidas de frequência em saúde | Município de 200.000 habitantes: o relatório anual da secretaria de saúde | `chapters/ch05/ch05_medidas_de_frequencia_pt.ipynb` | `docs/ch05_pt.html` |
| 6. Descrevendo duas variáveis | Pronto-socorro: um mês do registro de triagem, 1.263 atendimentos | `chapters/ch06/ch06_descrevendo_duas_variaveis_pt.ipynb` | `docs/ch06_pt.html` |
| 10. Delineamentos experimentais e quase-experimentais em saúde | Serviço de hipertensão com dez ambulatórios: pílula única ou comprimidos separados | `chapters/ch10/ch10_delineamentos_experimentais_pt.ipynb` | `docs/ch10_pt.html` |
| 11. Probabilidade: a linguagem da incerteza | Comitê de controle de infecção de uma maternidade pública, 5.000 partos | `chapters/ch11/ch11_probabilidade_pt.ipynb` | `docs/ch11_pt.html` |
| 13. Amostragem e estimação | Secretaria de saúde faz levantamento de saúde bucal de escolares: lista de 14.299 crianças em 48 escolas | `chapters/ch13/ch13_amostragem_estimacao_pt.ipynb` | `docs/ch13_pt.html` |

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

O caderno do Capítulo 11 segue o capítulo revisado de 13/11/2026 (registro da maternidade com quatro colunas e seis perguntas do comitê).

## Observações

Os dados são sintéticos e os valores têm apenas finalidade didática; não possuem correlação com o mundo real. Nada aqui é recomendação clínica nem estimativa para uma unidade real. As saídas do código usam ponto decimal.

## Online

Páginas: https://marcelosilva2604.github.io/data-science-ml-ai-in-health-volume-1-pt/ · Repositório: https://github.com/marcelosilva2604/data-science-ml-ai-in-health-volume-1-pt

**O nome do repositório e o ramo `main` estão impressos nos QR codes do livro. Não os renomeie, mova nem apague.** Se as páginas mudarem de lugar (por exemplo, para o site da editora), atualize os links deste README; os QR codes continuam apontando para cá.

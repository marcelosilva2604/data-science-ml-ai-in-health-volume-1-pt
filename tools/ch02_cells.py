"""All code cells of the Chapter 2 notebook (Part A by book section, and Part B): one cell each. Chapter 2 is the first contact with Python,
so the code is the plain standard-library program the chapter explains (csv, random, statistics, datetime), with its comments as numbered steps.
The cells are written once in English; the Portuguese cell is the same code with the comments and printed text translated
through the TR table (exact substrings, longest first)."""

TR = [
 ("# AUDIT PROGRAM: how long did the sampled patients wait after the", "# PROGRAMA DE AUDITORIA: quanto esperaram os pacientes sorteados depois de a"),
 ("# discharge was formalized, and how many waited more than 2 hours?", "# alta ser formalizada, e quantos esperaram mais de 2 horas?"),
 ("# Pseudocode", "# Pseudocódigo"),
 ("#   1. Read the register of January discharges, one record per episode.", "#   1. Ler a base de altas de janeiro, um registro por episódio."),
 ("#   2. For each episode, compute the wait in hours, from the formalized", "#   2. Para cada episódio, calcular a espera em horas, da alta formalizada"),
 ("#      discharge to the departure. A missing time leaves it unknown.", "#      até a saída. Um horário faltante deixa a espera desconhecida."),
 ("#   3. Mark the episode as delayed if the wait is MORE than 2 hours.", "#   3. Marcar o episódio como atrasado se a espera for MAIOR que 2 horas."),
 ("#   4. Draw the audit sample: 120 episodes, at random, without replacement.", "#   4. Sortear a amostra da auditoria: 120 episódios, ao acaso, sem reposição."),
 ("#   5. Report on the sample: delayed, percentage, median, longest, unknown.", "#   5. Relatar sobre a amostra: atrasados, porcentagem, mediana, maior, desconhecidos."),
 ("#   6. Count again under the rule \"2 hours or more\", to see what", "#   6. Contar de novo pela regra \"2 horas ou mais\", para ver o que"),
 ("#      changes when a wait of exactly 2 hours counts as delayed.", "#      muda quando uma espera de exatamente 2 horas conta como atraso."),
 ("# the audit's rule: delayed means MORE than 2 hours", "# a regra da auditoria: atrasado significa MAIS de 2 horas"),
 ("# 1. Read the register.", "# 1. Ler a base."),
 ("# 2-3. Compute each wait and mark the delays.", "# 2-3. Calcular cada espera e marcar os atrasos."),
 ("Check timestamps:", "Conferir horários:"),
 ("# 4. Draw the sample; the seed (11) makes the draw reproducible.", "# 4. Sortear a amostra; a semente (11) torna o sorteio reproduzível."),
 ("# 5. Report on the sample.", "# 5. Relatar sobre a amostra."),
 ("Episodes reviewed:", "Episódios revisados:"),
 ("Wait unknown:", "Espera desconhecida:"),
 ("Percentage over 2 hours:", "Porcentagem acima de 2 horas:"),
 ("Over 2 hours:", "Acima de 2 horas:"),
 ("\"of\"", "\"de\""),
 ("Median wait (hours):", "Espera mediana (horas):"),
 ("Longest wait (hours):", "Maior espera (horas):"),
 ("# 6. The same waits under the rule \"2 hours or more\".", "# 6. As mesmas esperas pela regra \"2 horas ou mais\"."),
 ("Percentage 2 hours or more:", "Porcentagem de 2 horas ou mais:"),
 ("2 hours or more:", "2 horas ou mais:"),
 ("# SAMPLING VARIATION: do different random draws give the same proportion?", "# VARIAÇÃO AMOSTRAL: sorteios aleatórios diferentes dão a mesma proporção?"),
 ("#   1. Count the delayed episodes in the whole register (possible only", "#   1. Contar os episódios atrasados na base inteira (só é possível"),
 ("#      because the data are synthetic; an audit team would not have it).", "#      porque os dados são sintéticos; uma equipe de auditoria não a teria)."),
 ("#   2. Draw three samples of 120 episodes, each with a different seed.", "#   2. Sortear três amostras de 120 episódios, cada uma com uma semente diferente."),
 ("#   3. For each sample, count the delayed episodes and the percentage.", "#   3. Em cada amostra, contar os episódios atrasados e a porcentagem."),
 ("Number of records whose delay status is True (unknown is not counted).", "Número de registros cuja situação de atraso é True (desconhecida não é contada)."),
 ("# 1. The whole register.", "# 1. A base inteira."),
 ("Whole register:", "Base inteira:"),
 (" delayed of ", " atrasados de "),
 ("# 2-3. Three samples; the seeds 11, 17, and 42 make the draws reproducible.", "# 2-3. Três amostras; as sementes 11, 17 e 42 tornam os sorteios reproduzíveis."),
 ("Sample {sample_number}:", "Amostra {sample_number}:"),
 ("# MISSING OBSERVATIONS: what can the team report when times are missing?", "# OBSERVAÇÕES FALTANTES: o que a equipe pode relatar quando faltam horários?"),
 ("#   1. Make a separate copy of the 120 sampled records.", "#   1. Fazer uma cópia separada dos 120 registros sorteados."),
 ("#   2. In the copy, hide the delay status of the first 12 episodes, as if", "#   2. Na cópia, esconder a situação de atraso dos 12 primeiros episódios, como se"),
 ("#      their formalized discharge time had not been recorded.", "#      o horário da alta formalizada não tivesse sido registrado."),
 ("#   3. Count the selected, known, and unknown statuses and the known delays.", "#   3. Contar as situações selecionadas, conhecidas e desconhecidas e os atrasos conhecidos."),
 ("#   4. Report the proportion delayed among the known statuses.", "#   4. Relatar a proporção de atrasos entre as situações conhecidas."),
 ("#   5. Report the range for all 120 selected episodes: every unknown status", "#   5. Relatar a faixa dos 120 episódios selecionados: toda situação desconhecida"),
 ("#      timely (lowest) or every unknown status delayed (highest).", "#      no prazo (mínimo) ou toda situação desconhecida atrasada (máximo)."),
 ("# 1-2. Copy the records (the originals stay intact) and hide 12 statuses.", "# 1-2. Copiar os registros (os originais ficam intactos) e esconder 12 situações."),
 ("# 3. Counts.", "# 3. Contagens."),
 ("# 4-5. Results.", "# 4-5. Resultados."),
 ("Selected:", "Selecionados:"),
 ("Known status:", "Situação conhecida:"),
 ("Unknown status:", "Situação desconhecida:"),
 ("Known delays:", "Atrasos conhecidos:"),
 ("Delayed among known:", "Atrasados entre os conhecidos:"),
 ("All selected:", "Todos os selecionados:"),
 ("% to ", "% a "),
 ("Known statuses:", "Situações conhecidas:"),
 ("Selected group:", "Grupo selecionado:"),
 ("# Known statuses: 21.3%", "# Situações conhecidas: 21.3%"),
 ("# Selected group: 19.2%-29.2%", "# Grupo selecionado: 19.2%-29.2%"),
 ("# 1. The six events of one synthetic bed-vacating episode (from Figure 2.2)", "# 1. Os seis eventos de um episódio sintético de desocupação de leito (da Figura 2.2)"),
 ("\"vacated\"", "\"leito desocupado\""),
 ("\"cleaning requested\"", "\"limpeza solicitada\""),
 ("\"cleaning started\"", "\"limpeza iniciada\""),
 ("\"cleaning finished\"", "\"limpeza concluída\""),
 ("\"bed ready\"", "\"leito pronto\""),
 ("\"next patient in\"", "\"próximo paciente entra\""),
 ("# 2. Minutes between each event and the next, with the longest interval", "# 2. Minutos entre cada evento e o seguinte, com o maior intervalo"),
 ("\"to\"", "\"até\""),
 ("\" to \" + name_b", "\" até \" + name_b"),
 ("\"minutes\"", "\"minutos\""),
 ("Total from bed vacating to the next patient:", "Total da desocupação do leito até a entrada do próximo paciente:"),
 ("Longest interval:", "Maior intervalo:"),
 ("\"(\" + str(longest_minutes) + \" minutes)\"", "\"(\" + str(longest_minutes) + \" minutos)\""),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


AUDIT = '''# AUDIT PROGRAM: how long did the sampled patients wait after the
# discharge was formalized, and how many waited more than 2 hours?
#
# Pseudocode
#   1. Read the register of January discharges, one record per episode.
#   2. For each episode, compute the wait in hours, from the formalized
#      discharge to the departure. A missing time leaves it unknown.
#   3. Mark the episode as delayed if the wait is MORE than 2 hours.
#   4. Draw the audit sample: 120 episodes, at random, without replacement.
#   5. Report on the sample: delayed, percentage, median, longest, unknown.
#   6. Count again under the rule "2 hours or more", to see what
#      changes when a wait of exactly 2 hours counts as delayed.

import csv
import random
import statistics
from datetime import datetime

TARGET_HOURS = 2  # the audit's rule: delayed means MORE than 2 hours

# 1. Read the register.
with open("data/register.csv", newline="") as stream:
    population = list(csv.DictReader(stream))

# 2-3. Compute each wait and mark the delays.
for row in population:
    row["wait"] = None
    row["delayed"] = None
    if row["formalized_at"] and row["departed_at"]:
        formalized = datetime.fromisoformat(row["formalized_at"])
        departed = datetime.fromisoformat(row["departed_at"])
        wait = (departed - formalized).total_seconds() / 3600
        if wait >= 0:
            row["wait"] = wait
            row["delayed"] = wait > TARGET_HOURS
        else:
            print("Check timestamps:", row["episode_id"])

# 4. Draw the sample; the seed (11) makes the draw reproducible.
sample = random.Random(11).sample(population, 120)

# 5. Report on the sample.
waits = [row["wait"] for row in sample if row["wait"] is not None]
delayed = [wait for wait in waits if wait > TARGET_HOURS]
print("Episodes reviewed:", len(sample))
print("Wait unknown:", len(sample) - len(waits))
print("Over 2 hours:", len(delayed), "of", len(waits))
print("Percentage over 2 hours:", 100 * len(delayed) / len(waits))
print("Median wait (hours):", statistics.median(waits))
print("Longest wait (hours):", max(waits))

# 6. The same waits under the rule "2 hours or more".
at_least_two = [wait for wait in waits if wait >= TARGET_HOURS]
share = 100 * len(at_least_two) / len(waits)
print("2 hours or more:", len(at_least_two), "of", len(waits))
print("Percentage 2 hours or more:", share)
'''

VARIATION = '''# SAMPLING VARIATION: do different random draws give the same proportion?
#
# Pseudocode
#   1. Count the delayed episodes in the whole register (possible only
#      because the data are synthetic; an audit team would not have it).
#   2. Draw three samples of 120 episodes, each with a different seed.
#   3. For each sample, count the delayed episodes and the percentage.

def count_delayed(records):
    """Number of records whose delay status is True (unknown is not counted)."""
    count = 0
    for row in records:
        if row["delayed"] is True:
            count = count + 1
    return count

# 1. The whole register.
N = len(population)
K = count_delayed(population)
print(f"Whole register: {K} delayed of {N} ({100 * K / N:.2f}%)")

# 2-3. Three samples; the seeds 11, 17, and 42 make the draws reproducible.
sample_number = 0
for seed in [11, 17, 42]:
    sample_number = sample_number + 1
    draw = random.Random(seed).sample(population, 120)
    k = count_delayed(draw)
    n = len(draw)
    print(f"Sample {sample_number}: {k} delayed of {n} ({100 * k / n:.2f}%)")
'''

MISSING = '''# MISSING OBSERVATIONS: what can the team report when times are missing?
#
# Pseudocode
#   1. Make a separate copy of the 120 sampled records.
#   2. In the copy, hide the delay status of the first 12 episodes, as if
#      their formalized discharge time had not been recorded.
#   3. Count the selected, known, and unknown statuses and the known delays.
#   4. Report the proportion delayed among the known statuses.
#   5. Report the range for all 120 selected episodes: every unknown status
#      timely (lowest) or every unknown status delayed (highest).

# 1-2. Copy the records (the originals stay intact) and hide 12 statuses.
incomplete = [dict(row) for row in sample]
for row in incomplete[:12]:
    row["delayed"] = None

# 3. Counts.
selected = len(incomplete)
known = [row for row in incomplete if row["delayed"] is not None]
unknown = selected - len(known)
known_delays = count_delayed(known)

# 4-5. Results.
print("Selected:", selected)
print("Known status:", len(known))
print("Unknown status:", unknown)
print("Known delays:", known_delays)
print(f"Delayed among known: {100 * known_delays / len(known):.1f}%")
lowest = 100 * known_delays / selected
highest = 100 * (known_delays + unknown) / selected
print(f"All selected: {lowest:.1f}% to {highest:.1f}%")
'''

EX7 = '''for seed in [11, 17, 42]:
    draw = random.Random(seed).sample(population, 120)
    identifiers = set()
    for row in draw:
        identifiers.add(row["episode_id"])
    assert len(draw) == len(identifiers) == 120
assert len(population) == 1200
assert K == 216
'''

EX8 = '''sample = random.Random(11).sample(population, 120)
incomplete = []
for row in sample:
    incomplete.append(dict(row))
for row in incomplete[:12]:
    row["delayed"] = None

known_n = 0
known_delays = 0
for row in incomplete:
    if row["delayed"] is not None:
        known_n = known_n + 1
        if row["delayed"] is True:
            known_delays = known_delays + 1
selected_n = len(incomplete)
missing_n = selected_n - known_n
print(selected_n, known_n, missing_n, known_delays)
# 120 108 12 23
print(f"Known statuses: {100 * known_delays / known_n:.1f}%")
# Known statuses: 21.3%
lower = 100 * known_delays / selected_n
upper = 100 * (known_delays + missing_n) / selected_n
print(f"Selected group: {lower:.1f}%-{upper:.1f}%")
# Selected group: 19.2%-29.2%
'''

EX9 = '''# 1. The six events of one synthetic bed-vacating episode (from Figure 2.2)
events = [
    ("vacated", "2026-01-04T13:00"),
    ("cleaning requested", "2026-01-04T13:20"),
    ("cleaning started", "2026-01-04T14:10"),
    ("cleaning finished", "2026-01-04T14:40"),
    ("bed ready", "2026-01-04T14:50"),
    ("next patient in", "2026-01-04T15:30"),
]

# 2. Minutes between each event and the next, with the longest interval
total = 0
longest_name = ""
longest_minutes = 0
for i in range(len(events) - 1):
    name_a, time_a = events[i]
    name_b, time_b = events[i + 1]
    minutes = (datetime.fromisoformat(time_b) - datetime.fromisoformat(time_a)).total_seconds() / 60
    print(name_a, "to", name_b + ":", minutes, "minutes")
    total = total + minutes
    if minutes > longest_minutes:
        longest_minutes = minutes
        longest_name = name_a + " to " + name_b
print("Total from bed vacating to the next patient:", total, "minutes")
print("Longest interval:", longest_name, "(" + str(longest_minutes) + " minutes)")
'''


def cells(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    code = lambda c: c if en else tr(c)
    S = []

    def sec(num, title_en, title_pt, q_en=None, q_pt=None):
        S.append(("md", "### " + num + " " + T(title_en, title_pt) + (("\n\n*" + T(q_en, q_pt) + "*") if q_en else "")))

    def cell(c):
        S.append(("code", code(c)))

    sec("2.7", "Defining the event to be counted", "Definindo o evento a ser contado",
        "When does a discharge count as delayed, and how many of the 120 sampled episodes were?",
        "Quando uma alta conta como atrasada, e quantos dos 120 episódios sorteados foram?")
    cell(AUDIT)
    sec("2.9", "Sampling variation", "Variação amostral",
        "Would another random draw of 120 episodes give the same proportion?",
        "Outro sorteio aleatório de 120 episódios daria a mesma proporção?")
    cell(VARIATION)
    sec("2.10", "Missing observations", "Observações faltantes",
        "What can the team report when the time of the formalized discharge is missing for 12 of the 120 records?",
        "O que a equipe pode relatar quando falta o horário da alta formalizada em 12 dos 120 registros?")
    cell(MISSING)
    exs = [
        (7, T("Three draws from one target population", "Três sorteios de uma população-alvo"), EX7),
        (8, T("An incomplete sample", "Uma amostra incompleta"), EX8),
        (9, T("Define the next process audit", "Definir a próxima auditoria de processo"), EX9),
    ]
    return S, [(k, title, code(block)) for k, title, block in exs]

"""All code cells of the Chapter 2 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions. Chapter 2 is the first
contact with Python, so only the standard library is used (csv, random, statistics, datetime).
The cells are written once in English; the Portuguese cell is the same code with the comments and printed text translated
through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the register: one row is one discharge episode", "# 1. Ler a base: cada linha é um episódio de alta"),
 ("# 2. Count rows and columns", "# 2. Contar linhas e colunas"),
 ("The register has", "A base tem"),
 ("rows (one per discharge episode) and", "linhas (uma por episódio de alta) e"),
 ("columns.", "colunas."),
 ("# 3. The first five rows", "# 3. As cinco primeiras linhas"),
 ("# 1. The audit's rule: delayed means MORE than 2 hours between the formalized discharge and the departure", "# 1. A regra da auditoria: atrasado significa MAIS de 2 horas entre a alta formalizada e a saída"),
 ("# 2. For each episode, compute the wait in hours and mark the delay (a missing time leaves the wait unknown, never zero)", "# 2. Para cada episódio, calcular a espera em horas e marcar o atraso (um horário faltante deixa a espera desconhecida, nunca zero)"),
 ("Check the times of episode", "Conferir os horários do episódio"),
 ("# 3. Draw the audit sample: 120 episodes at random, without replacement (seed 11, so the draw can be repeated)", "# 3. Sortear a amostra da auditoria: 120 episódios ao acaso, sem reposição (semente 11, para o sorteio poder ser repetido)"),
 ("# 4. The waits of the sample (an unknown wait is left out)", "# 4. As esperas da amostra (uma espera desconhecida fica de fora)"),
 ("Episodes reviewed:", "Episódios revisados:"),
 ("Episodes with unknown wait:", "Episódios com espera desconhecida:"),
 ("# 5. Delayed: wait of MORE than 2 hours", "# 5. Atrasados: espera de MAIS de 2 horas"),
 ("Delayed (more than 2 hours):", "Atrasados (mais de 2 horas):"),
 ("\"of\"", "\"de\""),
 ("\"episodes, which is\"", "\"episódios, ou seja\""),
 ("Median wait (hours):", "Espera mediana (horas):"),
 ("Longest wait (hours):", "Maior espera (horas):"),
 ("# 6. The same waits under the rule 2 hours or more", "# 6. As mesmas esperas pela regra 2 horas ou mais"),
 ("With the rule 2 hours or more:", "Pela regra 2 horas ou mais:"),
 ("\"The\"", "\"Os\""),
 ("\"episodes of difference waited exactly 2 hours.\"", "\"episódios de diferença esperaram exatamente 2 horas.\""),
 ("# 1. Count the delayed episodes in the whole register (possible only because the data are synthetic)", "# 1. Contar os episódios atrasados na base inteira (só é possível porque os dados são sintéticos)"),
 ("Whole register:", "Base inteira:"),
 ("\"delayed of\"", "\"atrasados de\""),
 ("# 2. Draw three samples of 120 episodes, each with a different seed (11, 17, and 42), and count the delayed ones", "# 2. Sortear três amostras de 120 episódios, cada uma com uma semente diferente (11, 17 e 42), e contar os atrasados"),
 ("\"Sample\"", "\"Amostra\""),
 ("\"has\"", "\"tem\""),
 ("# 1. Make a separate copy of the 120 sampled records (the originals stay intact)", "# 1. Fazer uma cópia separada dos 120 registros sorteados (os originais ficam intactos)"),
 ("# 2. In the copy, hide the delay status of the first 12 episodes, as if the formalized discharge time had not been recorded", "# 2. Na cópia, esconder a situação de atraso dos 12 primeiros episódios, como se o horário da alta formalizada não tivesse sido registrado"),
 ("# 3. Count the selected, known, and unknown statuses and the known delays", "# 3. Contar as situações selecionadas, conhecidas e desconhecidas e os atrasos conhecidos"),
 ("Selected episodes:", "Episódios selecionados:"),
 ("Known status:", "Situação conhecida:"),
 ("Unknown status:", "Situação desconhecida:"),
 ("Known delays:", "Atrasos conhecidos:"),
 ("# 4. The proportion delayed among the known statuses", "# 4. A proporção de atrasos entre as situações conhecidas"),
 ("Delayed among the known statuses:", "Atrasados entre as situações conhecidas:"),
 ("# 5. The range for all selected episodes: every unknown status timely (lowest) or every unknown status delayed (highest)", "# 5. A faixa para todos os episódios selecionados: toda situação desconhecida no prazo (mínimo) ou toda situação desconhecida atrasada (máximo)"),
 ("\"Among all\"", "\"Entre os\""),
 ("\"selected episodes:\"", "\"episódios selecionados:\""),
 ("\"% to\"", "\"% a\""),
 ("# 1. For each seed, check that the draw has 120 distinct episodes (a set keeps each value once)", "# 1. Para cada semente, conferir que o sorteio tem 120 episódios distintos (um conjunto guarda cada valor uma vez)"),
 ("\"Seed\"", "\"Semente\""),
 ("\"episodes,\"", "\"episódios,\""),
 ("\"distinct\"", "\"distintos\""),
 ("# 2. The register still has 1,200 episodes, 216 of them delayed", "# 2. A base continua com 1.200 episódios, 216 deles atrasados"),
 ("Register:", "Base:"),
 ("\"episodes, of which\"", "\"episódios, dos quais\""),
 ("\"delayed.\"", "\"atrasados.\""),
 ("# 1. Recreate Sample 1 and make a separate copy", "# 1. Recriar a Amostra 1 e fazer uma cópia separada"),
 ("# 2. Hide the first 12 statuses", "# 2. Esconder as 12 primeiras situações"),
 ("# 3. Count the known statuses and the known delays", "# 3. Contar as situações conhecidas e os atrasos conhecidos"),
 ("Selected:", "Selecionados:"),
 ("\"; known:\"", "\"; conhecidas:\""),
 ("\"; unknown:\"", "\"; desconhecidas:\""),
 ("\"; known delays:\"", "\"; atrasos conhecidos:\""),
 ("# 4. The proportion among the known statuses and the two bounds for all selected episodes", "# 4. A proporção entre as situações conhecidas e os dois limites para todos os episódios selecionados"),
 ("Among the known statuses:", "Entre as situações conhecidas:"),
 ("# 1. The six events of one synthetic bed-vacating episode (from Figure 2.2)", "# 1. Os seis eventos de um episódio sintético de desocupação de leito (da Figura 2.2)"),
 ("\"vacated\"", "\"leito desocupado\""),
 ("\"cleaning requested\"", "\"limpeza solicitada\""),
 ("\"cleaning started\"", "\"limpeza iniciada\""),
 ("\"cleaning finished\"", "\"limpeza concluída\""),
 ("\"bed ready\"", "\"leito pronto\""),
 ("\"next patient in\"", "\"próximo paciente entra\""),
 ("# 2. Minutes between each event and the next, with the longest interval", "# 2. Minutos entre cada evento e o seguinte, com o maior intervalo"),
 ("\" to \" + name_b", "\" até \" + name_b"),
 ("\"to\"", "\"até\""),
 ("\"minutes\"", "\"minutos\""),
 ("Total from bed vacating to the next patient:", "Total da desocupação do leito até a entrada do próximo paciente:"),
 ("Longest interval:", "Maior intervalo:"),
 ("\"(\" + str(longest_minutes) + \" minutes)\"", "\"(\" + str(longest_minutes) + \" minutos)\""),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


LOAD = '''# 1. Read the register: one row is one discharge episode
import csv
import random
import statistics
from datetime import datetime

with open("data/register.csv", newline="") as stream:
    population = list(csv.DictReader(stream))

# 2. Count rows and columns
print("The register has", len(population), "rows (one per discharge episode) and", len(population[0]), "columns.")

# 3. The first five rows
for row in population[:5]:
    print(row["episode_id"], row["patient_id"], row["formalized_at"], row["departed_at"])
'''

AUDIT = '''# 1. The audit's rule: delayed means MORE than 2 hours between the formalized discharge and the departure
TARGET_HOURS = 2

# 2. For each episode, compute the wait in hours and mark the delay (a missing time leaves the wait unknown, never zero)
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
            print("Check the times of episode", row["episode_id"])

# 3. Draw the audit sample: 120 episodes at random, without replacement (seed 11, so the draw can be repeated)
sample = random.Random(11).sample(population, 120)

# 4. The waits of the sample (an unknown wait is left out)
waits = []
for row in sample:
    if row["wait"] is not None:
        waits.append(row["wait"])
print("Episodes reviewed:", len(sample))
print("Episodes with unknown wait:", len(sample) - len(waits))

# 5. Delayed: wait of MORE than 2 hours
delayed = 0
for wait in waits:
    if wait > TARGET_HOURS:
        delayed = delayed + 1
print("Delayed (more than 2 hours):", delayed, "of", len(waits), "episodes, which is", round(100 * delayed / len(waits), 1), "%")
print("Median wait (hours):", statistics.median(waits))
print("Longest wait (hours):", max(waits))

# 6. The same waits under the rule 2 hours or more
at_least_two = 0
for wait in waits:
    if wait >= TARGET_HOURS:
        at_least_two = at_least_two + 1
print("With the rule 2 hours or more:", at_least_two, "of", len(waits), "episodes, which is", round(100 * at_least_two / len(waits), 1), "%")
print("The", at_least_two - delayed, "episodes of difference waited exactly 2 hours.")
'''

VARIATION = '''# 1. Count the delayed episodes in the whole register (possible only because the data are synthetic)
N = len(population)
K = 0
for row in population:
    if row["delayed"] is True:
        K = K + 1
print("Whole register:", K, "delayed of", N, "episodes, which is", round(100 * K / N, 2), "%")

# 2. Draw three samples of 120 episodes, each with a different seed (11, 17, and 42), and count the delayed ones
sample_number = 0
for seed in [11, 17, 42]:
    sample_number = sample_number + 1
    draw = random.Random(seed).sample(population, 120)
    k = 0
    for row in draw:
        if row["delayed"] is True:
            k = k + 1
    print("Sample", sample_number, "has", k, "delayed of", len(draw), "episodes, which is", round(100 * k / len(draw), 2), "%")
'''

MISSING = '''# 1. Make a separate copy of the 120 sampled records (the originals stay intact)
incomplete = []
for row in sample:
    incomplete.append(dict(row))

# 2. In the copy, hide the delay status of the first 12 episodes, as if the formalized discharge time had not been recorded
for row in incomplete[:12]:
    row["delayed"] = None

# 3. Count the selected, known, and unknown statuses and the known delays
selected = len(incomplete)
known_n = 0
known_delays = 0
for row in incomplete:
    if row["delayed"] is not None:
        known_n = known_n + 1
        if row["delayed"] is True:
            known_delays = known_delays + 1
unknown = selected - known_n
print("Selected episodes:", selected)
print("Known status:", known_n)
print("Unknown status:", unknown)
print("Known delays:", known_delays)

# 4. The proportion delayed among the known statuses
print("Delayed among the known statuses:", round(100 * known_delays / known_n, 1), "%")

# 5. The range for all selected episodes: every unknown status timely (lowest) or every unknown status delayed (highest)
lowest = 100 * known_delays / selected
highest = 100 * (known_delays + unknown) / selected
print("Among all", selected, "selected episodes:", round(lowest, 1), "% to", round(highest, 1), "%")
'''

EX7 = '''# 1. For each seed, check that the draw has 120 distinct episodes (a set keeps each value once)
for seed in [11, 17, 42]:
    draw = random.Random(seed).sample(population, 120)
    identifiers = set()
    for row in draw:
        identifiers.add(row["episode_id"])
    print("Seed", seed, "has", len(draw), "episodes,", len(identifiers), "distinct")

# 2. The register still has 1,200 episodes, 216 of them delayed
print("Register:", len(population), "episodes, of which", K, "delayed.")
'''

EX8 = '''# 1. Recreate Sample 1 and make a separate copy
sample = random.Random(11).sample(population, 120)
incomplete = []
for row in sample:
    incomplete.append(dict(row))

# 2. Hide the first 12 statuses
for row in incomplete[:12]:
    row["delayed"] = None

# 3. Count the known statuses and the known delays
known_n = 0
known_delays = 0
for row in incomplete:
    if row["delayed"] is not None:
        known_n = known_n + 1
        if row["delayed"] is True:
            known_delays = known_delays + 1
selected_n = len(incomplete)
missing_n = selected_n - known_n
print("Selected:", selected_n, "; known:", known_n, "; unknown:", missing_n, "; known delays:", known_delays)

# 4. The proportion among the known statuses and the two bounds for all selected episodes
print("Among the known statuses:", round(100 * known_delays / known_n, 1), "%")
lower = 100 * known_delays / selected_n
upper = 100 * (known_delays + missing_n) / selected_n
print("Among all", selected_n, "selected episodes:", round(lower, 1), "% to", round(upper, 1), "%")
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

    sec("2.1", "Introduction: the data", "Introdução: os dados")
    cell(LOAD)
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
    exs = [(7, "", EX7), (8, "", EX8), (9, "", EX9)]
    return S, [(k, title, code(block)) for k, title, block in exs]

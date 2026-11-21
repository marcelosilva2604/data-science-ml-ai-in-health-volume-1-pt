"""All code cells of the Chapter 9 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered comments, output as plain
sentences. Beginner-friendly Python in the style of Chapters 10 to 17: print with commas, round(), no f-strings, no helper functions (the predictive values and
the post-test probabilities are computed inline in loops). The book draws the figures; the notebook prints the same numbers. The Portuguese cell is the same
code with the comments and printed text translated through the TR table (exact substrings, longest first)."""

TR = [
 ("# 1. Read the accuracy cohort: 1,200 follow-up visits, with the rapid test (index test) and the true infection (reference standard)", "# 1. Ler a coorte de acurácia: 1.200 visitas de seguimento, com o teste rápido (teste índice) e a infecção verdadeira (padrão de referência)"),
 ("# 2. The four cells of the two-by-two table: a Boolean column summed is a count", "# 2. As quatro células da tabela dois por dois: uma coluna booleana somada é uma contagem"),
 ("True positives:", "Verdadeiros positivos:"),
 ("; false positives:", "; falsos positivos:"),
 ("; false negatives:", "; falsos negativos:"),
 ("; true negatives:", "; verdadeiros negativos:"),
 ("# 3. Sensitivity, specificity, and the predictive values", "# 3. Sensibilidade, especificidade e os valores preditivos"),
 ("Sensitivity:", "Sensibilidade:"),
 ("; specificity:", "; especificidade:"),
 ("; positive predictive value:", "; valor preditivo positivo:"),
 ("; negative predictive value:", "; valor preditivo negativo:"),
 ("# 4. Wilson 95% intervals of the four proportions", "# 4. Intervalos de Wilson de 95% das quatro proporções"),
 ("(\"Sensitivity\",", "(\"Sensibilidade\","),
 ("(\"Specificity\",", "(\"Especificidade\","),
 ("(\"Positive predictive value\",", "(\"Valor preditivo positivo\","),
 ("(\"Negative predictive value\",", "(\"Valor preditivo negativo\","),
 ("\"(95% CI\"", "\"(IC de 95%\""),
 ("\"to\"", "\"a\""),
 ("# 1. Predictive values of the rapid test at different prevalences, from its sensitivity and specificity", "# 1. Valores preditivos do teste rápido em diferentes prevalências, a partir de sua sensibilidade e especificidade"),
 ("\"Prevalence\"", "\"Prevalência\""),
 ("\": positive predictive value\"", "\": valor preditivo positivo\""),
 ("\"; negative predictive value\"", "\"; valor preditivo negativo\""),
 ("# 1. The likelihood ratios of the binary test", "# 1. As razões de verossimilhança do teste binário"),
 ("Positive likelihood ratio:", "Razão de verossimilhança positiva:"),
 ("; negative likelihood ratio:", "; razão de verossimilhança negativa:"),
 ("# 2. The likelihood ratio of each band of the biomarker (ng/mL), from the counts of infected and not infected patients in the band", "# 2. A razão de verossimilhança de cada faixa do biomarcador (ng/mL), a partir das contagens de pacientes infectados e não infectados na faixa"),
 ("\"Band\"", "\"Faixa\""),
 ("\": infected\"", "\": infectados\""),
 ("\"; not infected\"", "\"; não infectados\""),
 ("\"; proportions\"", "\"; proporções\""),
 ("\"; likelihood ratio\"", "\"; razão de verossimilhança\""),
 ("# 1. Natural frequencies: 1,000 patients at a pre-test probability of 7.8%", "# 1. Frequências naturais: 1.000 pacientes com probabilidade pré-teste de 7,8%"),
 ("Infected:", "Infectados:"),
 ("; true positives:", "; verdadeiros positivos:"),
 ("# 2. Post-test probability from the pre-test probability and a likelihood ratio, in the odds form", "# 2. Probabilidade pós-teste a partir da probabilidade pré-teste e de uma razão de verossimilhança, na forma de chances"),
 ("\"7.8%, positive strip\"", "\"7,8%, fita positiva\""),
 ("\"7.8%, negative strip\"", "\"7,8%, fita negativa\""),
 ("\"7.8%, top band\"", "\"7,8%, faixa superior\""),
 ("\"7.8%, bottom band\"", "\"7,8%, faixa inferior\""),
 ("\"30%, positive strip\"", "\"30%, fita positiva\""),
 ("\"30%, negative strip\"", "\"30%, fita negativa\""),
 ("\"Pre-test\"", "\"Pré-teste\""),
 ("\": post-test probability\"", "\": probabilidade pós-teste\""),
 ("# 3. A simulation of 12 months of admissions screened for MRSA (seed 8): carriers, true positives, and false positives each month", "# 3. Uma simulação de 12 meses de internações rastreadas para MRSA (semente 8): portadores, verdadeiros positivos e falsos positivos em cada mês"),
 ("Monthly means - carriers:", "Médias mensais - portadores:"),
 ("; positives:", "; positivos:"),
 ("\"Positives range from\"", "\"Os positivos variam de\""),
 ("\"to\"", "\"a\""),
 ("; share of the positives that are true carriers:", "; parcela dos positivos que são portadores verdadeiros:"),
 ("# 4. Isolation bed-days: 7 days for a true carrier, 2 days for a false positive (until the culture result)", "# 4. Leitos-dia de isolamento: 7 dias para um portador verdadeiro, 2 dias para um falso positivo (até o resultado da cultura)"),
 ("Isolation bed-days per month - mean:", "Leitos-dia de isolamento por mês - média:"),
 ("; maximum:", "; máximo:"),
 ("\"beds in a 30-day month\"", "\"leitos em um mês de 30 dias\""),
 ("# 1. Sensitivity and specificity of the biomarker at four cutoffs", "# 1. Sensibilidade e especificidade do biomarcador em quatro pontos de corte"),
 ("\"Cutoff\"", "\"Ponto de corte\""),
 ("\": sensitivity\"", "\": sensibilidade\""),
 ("\"; specificity\"", "\"; especificidade\""),
 ("# 2. The ROC curve, the area under it, and the Mann-Whitney count divided by n1 times n0", "# 2. A curva ROC, a área sob ela e a contagem de Mann-Whitney dividida por n1 vezes n0"),
 ("Retained thresholds:", "Limiares retidos:"),
 ("; area under the curve:", "; área sob a curva:"),
 ("; Mann-Whitney count over n1 times n0:", "; contagem de Mann-Whitney sobre n1 vezes n0:"),
 ("# 3. The Hanley-McNeil standard error and the 95% interval of the area", "# 3. O erro padrão de Hanley-McNeil e o intervalo de 95% da área"),
 ("Standard error of the area:", "Erro padrão da área:"),
 ("; 95% interval:", "; intervalo de 95%:"),
 ("# 1. Wilson 95% intervals for the dipstick: 204 of 240 and 312 of 400", "# 1. Intervalos de Wilson de 95% para a fita: 204 de 240 e 312 de 400"),
 ("\"of\"", "\"de\""),
 ("# 1. The dipstick (sensitivity 0.85, specificity 0.78) in two settings with different prevalence", "# 1. A fita (sensibilidade 0,85, especificidade 0,78) em dois cenários com prevalência diferente"),
 ("# 1. Screening 1,500 admissions a month for a resistant organism (seed 8): carriers, true positives, false positives", "# 1. Rastrear 1.500 internações por mês para um organismo resistente (semente 8): portadores, verdadeiros positivos, falsos positivos"),
 ("# 2. Isolation bed-days: 5 days for a true carrier, 2 days for a false positive", "# 2. Leitos-dia de isolamento: 5 dias para um portador verdadeiro, 2 dias para um falso positivo"),
 ("; isolation bed-days:", "; leitos-dia de isolamento:"),
 ("; worst month:", "; pior mês:"),
 ("Share of the bed-days generated by false positives:", "Parte dos leitos-dia gerada por falsos positivos:"),
 ("# 1. Sensitivity and specificity of the biomarker at cutoffs of 25 and 40 ng/mL (counts and proportions)", "# 1. Sensibilidade e especificidade do biomarcador em pontos de corte de 25 e 40 ng/mL (contagens e proporções)"),
 ("# 2. The area under the ROC curve in patients with and without diabetes, with the Mann-Whitney check and the 95% interval", "# 2. A área sob a curva ROC em pacientes com e sem diabetes, com a conferência de Mann-Whitney e o intervalo de 95%"),
 ("\"Diabetes\"", "\"Diabetes\""),
 ("\"; not infected\"", "\"; não infectados\""),
 ("\"; area\"", "\"; área\""),
 ("\"; 95% interval\"", "\"; intervalo de 95%\""),
 ("# 1. The cutoff that maximizes the weighted sensitivity when a false positive costs one fifth of a missed case", "# 1. O ponto de corte que maximiza a sensibilidade ponderada quando um falso positivo custa um quinto de um caso perdido"),
 ("Weight:", "Peso:"),
 ("; cutoff:", "; ponto de corte:"),
 ("# 2. The Youden cutoff (equal costs)", "# 2. O ponto de corte de Youden (custos iguais)"),
 ("Youden cutoff:", "Ponto de corte de Youden:"),
 ("# 3. The same with a prevalence of 30%", "# 3. O mesmo com prevalência de 30%"),
 ("# 1. Sample size for a rapid influenza test: patients with influenza for the sensitivity, and the enrollment at 12% prevalence", "# 1. Tamanho da amostra para um teste rápido de influenza: pacientes com influenza para a sensibilidade e o recrutamento com prevalência de 12%"),
 ("Patients with influenza:", "Pacientes com influenza:"),
 ("; febrile patients to enroll at 12% prevalence:", "; pacientes febris a recrutar com prevalência de 12%:"),
 ("# 2. Patients without influenza for the specificity, and the enrollment", "# 2. Pacientes sem influenza para a especificidade e o recrutamento"),
 ("Patients without influenza:", "Pacientes sem influenza:"),
 ("; febrile patients to enroll:", "; pacientes febris a recrutar:"),
 ("# 3. In a mild season at 6% prevalence", "# 3. Em uma temporada leve, com prevalência de 6%"),
 ("Febrile patients to enroll at 6% prevalence:", "Pacientes febris a recrutar com prevalência de 6%:"),
 ("# 1. Annual screening in the synthetic cohort of 10,000 women followed for 20 years (seed 8): each year, 85% of the tumors in their detectable phase are found", "# 1. Rastreamento anual na coorte sintética de 10.000 mulheres acompanhadas por 20 anos (semente 8): a cada ano, 85% dos tumores em sua fase detectável são encontrados"),
 ("# 2. Detected tumors, their share, and the mean lead time (years)", "# 2. Tumores detectados, sua parte e o tempo de antecipação médio (anos)"),
 ("Screen-detected tumors:", "Tumores detectados no rastreamento:"),
 ("; share:", "; parte:"),
 ("; mean lead time:", "; tempo de antecipação médio:"),
 ("\"years\")", "\"anos\")"),
 ("# 3. Survival beyond 5 years from diagnosis among the screen-detected and the clinically detected, and deaths within 20 years", "# 3. Sobrevida além de 5 anos do diagnóstico entre os detectados no rastreamento e os detectados clinicamente, e óbitos em 20 anos"),
 ("Survival beyond 5 years - screen-detected:", "Sobrevida além de 5 anos - detectados no rastreamento:"),
 ("; clinically detected:", "; detectados clinicamente:"),
 ("; deaths within 20 years:", "; óbitos em 20 anos:"),
 ("# 4. The treatment threshold from the harm of 0.04 of treating a patient without the condition and the benefit of 0.08, and the test threshold", "# 4. O limiar de tratamento a partir do dano de 0,04 de tratar um paciente sem a condição e do benefício de 0,08, e o limiar de teste"),
 ("Treatment threshold:", "Limiar de tratamento:"),
 ("; test threshold with a likelihood ratio of 6:", "; limiar de teste com razão de verossimilhança 6:"),
 ("\"; with 0.2:\"", "\"; com 0,2:\""),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


TABLE = '''# 1. Read the accuracy cohort: 1,200 follow-up visits, with the rapid test (index test) and the true infection (reference standard)
import pandas as pd
from statsmodels.stats.proportion import proportion_confint

d = pd.read_csv("data/accuracy_cohort.csv")
inf = d["ssi"] == "yes"
pos = d["rapid_test"] == "positive"

# 2. The four cells of the two-by-two table: a Boolean column summed is a count
tp = (pos & inf).sum()
fn = (~pos & inf).sum()
fp = (pos & ~inf).sum()
tn = (~pos & ~inf).sum()
print("True positives:", tp, "; false positives:", fp, "; false negatives:", fn, "; true negatives:", tn)

# 3. Sensitivity, specificity, and the predictive values
se = tp / (tp + fn)
sp = tn / (tn + fp)
ppv = tp / (tp + fp)
npv = tn / (tn + fn)
print("Sensitivity:", round(se, 3), "; specificity:", round(sp, 3), "; positive predictive value:", round(ppv, 3), "; negative predictive value:", round(npv, 3))

# 4. Wilson 95% intervals of the four proportions
for name, k, n in [("Sensitivity", tp, tp + fn), ("Specificity", tn, tn + fp), ("Positive predictive value", tp, tp + fp), ("Negative predictive value", tn, tn + fn)]:
    lo, hi = proportion_confint(k, n, alpha=0.05, method="wilson")
    print(name + ":", round(k / n, 3), "(95% CI", round(lo, 3), "to", round(hi, 3), ")")
'''

PRED = '''# 1. Predictive values of the rapid test at different prevalences, from its sensitivity and specificity
for prev in [0.01, 0.03, 0.078, 0.20, 0.40]:
    ppv_prev = prev * se / (prev * se + (1 - prev) * (1 - sp))
    npv_prev = (1 - prev) * sp / ((1 - prev) * sp + prev * (1 - se))
    print("Prevalence", prev, ": positive predictive value", round(ppv_prev, 3), "; negative predictive value", round(npv_prev, 3))
'''

LR = '''# 1. The likelihood ratios of the binary test
lr_pos = se / (1 - sp)
lr_neg = (1 - se) / sp
print("Positive likelihood ratio:", round(lr_pos, 2), "; negative likelihood ratio:", round(lr_neg, 2))

# 2. The likelihood ratio of each band of the biomarker (ng/mL), from the counts of infected and not infected patients in the band
bands = [(0, 20), (20, 40), (40, 80), (80, float("inf"))]
n_inf = inf.sum()
n_not = (~inf).sum()
for lo, hi in bands:
    in_band = (d["marker_ng_ml"] >= lo) & (d["marker_ng_ml"] < hi)
    a = (in_band & inf).sum()
    b = (in_band & ~inf).sum()
    print("Band", lo, "to", hi, ": infected", a, "; not infected", b, "; proportions", round(a / n_inf, 3), round(b / n_not, 3), "; likelihood ratio", round((a / n_inf) / (b / n_not), 2))
'''

POST1 = '''# 1. Natural frequencies: 1,000 patients at a pre-test probability of 7.8%
n = 1000
infected = round(n * 0.078)
print("Infected:", infected, "; true positives:", round(infected * se), "; false positives:", round((n - infected) * (1 - sp)))

# 2. Post-test probability from the pre-test probability and a likelihood ratio, in the odds form
cases = [("7.8%, positive strip", 0.078, lr_pos), ("7.8%, negative strip", 0.078, lr_neg),
         ("7.8%, top band", 0.078, 39.22), ("7.8%, bottom band", 0.078, 0.18),
         ("30%, positive strip", 0.30, lr_pos), ("30%, negative strip", 0.30, lr_neg)]
for label, prev, lr in cases:
    pre_odds = prev / (1 - prev)
    post_odds = pre_odds * lr
    print("Pre-test", label + ": post-test probability", round(post_odds / (1 + post_odds), 3))
'''

POST2 = '''# 3. A simulation of 12 months of admissions screened for MRSA (seed 8): carriers, true positives, and false positives each month
import numpy as np

rng = np.random.default_rng(8)
adm = 2000
prev_mrsa = 0.03
se_m = 0.90
sp_m = 0.97
carriers = rng.binomial(adm, prev_mrsa, size=12)
true_pos = rng.binomial(carriers, se_m)
false_pos = rng.binomial(adm - carriers, 1 - sp_m)
positives = true_pos + false_pos
print("Monthly means - carriers:", round(carriers.mean(), 1), "; true positives:", round(true_pos.mean(), 1), "; false positives:", round(false_pos.mean(), 1), "; positives:", round(positives.mean(), 1))
print("Positives range from", positives.min(), "to", positives.max(), "; share of the positives that are true carriers:", round((true_pos / positives).mean(), 3))

# 4. Isolation bed-days: 7 days for a true carrier, 2 days for a false positive (until the culture result)
iso_days = true_pos * 7 + false_pos * 2
print("Isolation bed-days per month - mean:", round(iso_days.mean(), 1), "; maximum:", iso_days.max(), "=", round(iso_days.max() / 30, 1), "beds in a 30-day month")
'''

ROC = '''# 1. Sensitivity and specificity of the biomarker at four cutoffs
from sklearn.metrics import roc_curve, roc_auc_score
from scipy import stats

x = d["marker_ng_ml"].to_numpy()
y = inf.to_numpy()
for c in [15, 30, 45, 60]:
    print("Cutoff", c, ": sensitivity", round((x[y] >= c).mean(), 3), "; specificity", round((x[~y] < c).mean(), 3))

# 2. The ROC curve, the area under it, and the Mann-Whitney count divided by n1 times n0
fpr, tpr, thr = roc_curve(y, x)
auc = roc_auc_score(y, x)
u = stats.mannwhitneyu(x[y], x[~y], alternative="two-sided").statistic
n1 = y.sum()
n0 = (~y).sum()
print("Retained thresholds:", len(thr), "; area under the curve:", round(auc, 3), "; Mann-Whitney count over n1 times n0:", round(u / (n1 * n0), 3))

# 3. The Hanley-McNeil standard error and the 95% interval of the area
q1 = auc / (2 - auc)
q2 = 2 * auc ** 2 / (1 + auc)
se_auc = np.sqrt((auc * (1 - auc) + (n1 - 1) * (q1 - auc ** 2) + (n0 - 1) * (q2 - auc ** 2)) / (n1 * n0))
print("Standard error of the area:", round(se_auc, 4), "; 95% interval:", round(auc - 1.96 * se_auc, 3), "to", round(auc + 1.96 * se_auc, 3))
'''

EX3 = '''# 1. Wilson 95% intervals for the dipstick: 204 of 240 and 312 of 400
for k, n in [(204, 240), (312, 400)]:
    lo, hi = proportion_confint(k, n, alpha=0.05, method="wilson")
    print(k, "of", n, ":", round(k / n, 3), "(95% CI", round(lo, 3), "to", round(hi, 3), ")")
'''

EX4 = '''# 1. The dipstick (sensitivity 0.85, specificity 0.78) in two settings with different prevalence
for prev in [0.55, 0.10]:
    ppv_prev = prev * 0.85 / (prev * 0.85 + (1 - prev) * (1 - 0.78))
    npv_prev = (1 - prev) * 0.78 / ((1 - prev) * 0.78 + prev * (1 - 0.85))
    print("Prevalence", prev, ": positive predictive value", round(ppv_prev, 3), "; negative predictive value", round(npv_prev, 3))
'''

EX7 = '''# 1. Screening 1,500 admissions a month for a resistant organism (seed 8): carriers, true positives, false positives
rng = np.random.default_rng(8)
adm = 1500
prev_c = 0.02
se_c = 0.92
sp_c = 0.95
carriers = rng.binomial(adm, prev_c, size=12)
true_pos = rng.binomial(carriers, se_c)
false_pos = rng.binomial(adm - carriers, 1 - sp_c)

# 2. Isolation bed-days: 5 days for a true carrier, 2 days for a false positive
iso_days = true_pos * 5 + false_pos * 2
print("Monthly means - true positives:", round(true_pos.mean(), 1), "; false positives:", round(false_pos.mean(), 1), "; isolation bed-days:", round(iso_days.mean(), 1), "; worst month:", iso_days.max())
print("Share of the bed-days generated by false positives:", round((false_pos * 2).sum() / iso_days.sum(), 3))
'''

EX8 = '''# 1. Sensitivity and specificity of the biomarker at cutoffs of 25 and 40 ng/mL (counts and proportions)
for c in [25, 40]:
    print("Cutoff", c, ": sensitivity", (x[inf] >= c).sum(), round((x[inf] >= c).mean(), 3), "; specificity", (x[~inf] < c).sum(), round((x[~inf] < c).mean(), 3))

# 2. The area under the ROC curve in patients with and without diabetes, with the Mann-Whitney check and the 95% interval
for g in ["yes", "no"]:
    m = (d["diabetes"] == g).to_numpy()
    yy = inf[m]
    xx = x[m]
    auc_g = roc_auc_score(yy, xx)
    n1_g = yy.sum()
    n0_g = (~yy).sum()
    u_g = stats.mannwhitneyu(xx[yy], xx[~yy]).statistic
    q1_g = auc_g / (2 - auc_g)
    q2_g = 2 * auc_g ** 2 / (1 + auc_g)
    se_g = np.sqrt((auc_g * (1 - auc_g) + (n1_g - 1) * (q1_g - auc_g ** 2) + (n0_g - 1) * (q2_g - auc_g ** 2)) / (n1_g * n0_g))
    print("Diabetes", g + ": infected", n1_g, "; not infected", n0_g, "; area", round(auc_g, 3), "; Mann-Whitney", round(u_g / (n1_g * n0_g), 3), "; 95% interval", round(auc_g - 1.96 * se_g, 3), "to", round(auc_g + 1.96 * se_g, 3))
'''

EX9 = '''# 1. The cutoff that maximizes the weighted sensitivity when a false positive costs one fifth of a missed case
fpr, tpr, thr = roc_curve(inf, x)
prev = inf.mean()
w = (1 - prev) / (prev * 5)
k = np.argmax(tpr - w * fpr)
j = np.argmax(tpr - fpr)
print("Weight:", round(w, 2), "; cutoff:", round(thr[k], 1), "; sensitivity:", round(tpr[k], 3), "; specificity:", round(1 - fpr[k], 3))

# 2. The Youden cutoff (equal costs)
print("Youden cutoff:", round(thr[j], 1), "; sensitivity:", round(tpr[j], 3), "; specificity:", round(1 - fpr[j], 3))

# 3. The same with a prevalence of 30%
w2 = 0.70 / (0.30 * 5)
k2 = np.argmax(tpr - w2 * fpr)
print("Weight:", round(w2, 3), "; cutoff:", round(thr[k2], 1), "; sensitivity:", round(tpr[k2], 3), "; specificity:", round(1 - fpr[k2], 3))
'''

EX11 = '''# 1. Sample size for a rapid influenza test: patients with influenza for the sensitivity, and the enrollment at 12% prevalence
z = 1.96
n_inf = z ** 2 * 0.85 * 0.15 / 0.06 ** 2
print("Patients with influenza:", round(n_inf, 1), "->", int(np.ceil(n_inf)), "; febrile patients to enroll at 12% prevalence:", int(np.ceil(np.ceil(n_inf) / 0.12)))

# 2. Patients without influenza for the specificity, and the enrollment
n_not = z ** 2 * 0.95 * 0.05 / 0.03 ** 2
print("Patients without influenza:", round(n_not, 1), "->", int(np.ceil(n_not)), "; febrile patients to enroll:", int(np.ceil(np.ceil(n_not) / 0.88)))

# 3. In a mild season at 6% prevalence
print("Febrile patients to enroll at 6% prevalence:", int(np.ceil(np.ceil(n_inf) / 0.06)))
'''

EX12A = '''# 1. Annual screening in the synthetic cohort of 10,000 women followed for 20 years (seed 8): each year, 85% of the tumors in their detectable phase are found
import pandas as pd

s = pd.read_csv("data/screening_cohort.csv")
c = s[s["cancer"] == "yes"].copy()
rng = np.random.default_rng(8)
onset = c["t_onset"].to_numpy()
t_clin = c["t_clinical"].to_numpy()
t_death = c["t_death"].to_numpy()
t_screen = np.full(len(c), np.nan)
for sc in np.arange(1.0, 20.1, 1.0):
    in_phase = (onset <= sc) & (sc < t_clin) & np.isnan(t_screen)
    hit = in_phase & (rng.random(len(c)) < 0.85)
    t_screen[hit] = sc

# 2. Detected tumors, their share, and the mean lead time (years)
det = ~np.isnan(t_screen)
t_dx = np.where(det, t_screen, t_clin)
print("Screen-detected tumors:", det.sum(), "; share:", round(det.mean(), 3), "; mean lead time:", round((t_clin - t_screen)[det].mean(), 2), "years")

# 3. Survival beyond 5 years from diagnosis among the screen-detected and the clinically detected, and deaths within 20 years
print("Survival beyond 5 years - screen-detected:", round(((t_death - t_dx) > 5)[det].mean(), 3), "; clinically detected:", round(((t_death - t_dx) > 5)[~det].mean(), 3), "; deaths within 20 years:", int((t_death <= 20).sum()))
'''

EX12B = '''# 4. The treatment threshold from the harm of 0.04 of treating a patient without the condition and the benefit of 0.08, and the test threshold
treat_thr = 0.04 / (0.04 + 0.08)
print("Treatment threshold:", round(treat_thr, 3), "; test threshold with a likelihood ratio of 6:", round(treat_thr / (treat_thr + (1 - treat_thr) * 6), 3), "; with 0.2:", round(treat_thr / (treat_thr + (1 - treat_thr) * 0.2), 3))
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

    sec("9.3", "The two-by-two table of a test: sensitivity and specificity", "A tabela dois por dois de um teste: sensibilidade e especificidade", "How well does the rapid test detect infection and rule it out?", "Quão bem o teste rápido detecta a infecção e a descarta?")
    cell(TABLE)
    sec("9.4", "Predictive values and prevalence", "Valores preditivos e prevalência", "What does a positive or a negative result mean at different prevalences?", "O que significa um resultado positivo ou negativo em diferentes prevalências?")
    cell(PRED)
    sec("9.5", "Likelihood ratios", "Razões de verossimilhança", "How much does each result change the odds of infection?", "Quanto cada resultado muda as chances de infecção?")
    cell(LR)
    sec("9.6", "From pre-test to post-test probability: natural frequencies and odds", "Da probabilidade pré-teste à pós-teste: frequências naturais e chances", "What is the probability of infection after the test, starting from the probability before it?", "Qual é a probabilidade de infecção depois do teste, partindo da probabilidade antes dele?")
    cell(POST1)
    cell(POST2)
    sec("9.7", "Choosing a cutoff: the ROC curve and the area under it", "Escolhendo um ponto de corte: a curva ROC e a área sob ela", "How does a continuous biomarker perform across cutoffs?", "Como um biomarcador contínuo se comporta ao longo dos pontos de corte?")
    cell(ROC)
    exs = [(3, "", EX3), (4, "", EX4), (7, "", EX7), (8, "", EX8), (9, "", EX9), (11, "", EX11), (12, "", EX12A + "\n" + EX12B)]
    return S, [(k, title, code(block)) for k, title, block in exs]

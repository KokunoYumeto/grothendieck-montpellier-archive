# Second pass, block MPL_16+47+54+44_16-001-16-018 (Claude Opus 5.5 at effort max, 17 Nov 2026).
# Applies the checked corrections to the first-pass page files and writes the corrected files
# to second_pass/out/MPL_16+47+54+44/. Each change must match exactly once.
# Tags: 'own' = settled or marked from the ink alone; 'hua' = after consulting Michel Hua's
# transcription (batch-01.fr.tex) as a second witness.
import os, re, sys

BASE = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + r"/returns/MPL_16+47+54+44_unzipped/pages"
OUT = BASE + r"/second_pass/out/MPL_16+47+54+44"
SCANS = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

C = [
 (3, 'hua', r"(\unsure{comm.})", r"(\unsure{commut.|comm.})"),
 (3, 'own', r"\inserted{du module \unsure{non-gradué} \unsure{(le produit)}}",
            r"\inserted{du module \unsure{ss-jacent|non-gradué} \unsure{(sans graduation)|(le produit)}}"),
 (3, 'hua', r"\deleted{\unsure{u}}\quad\operatorname{pr}", r"\deleted{\unsure{u|\mathrm{gr}}}\quad\operatorname{pr}"),
 (3, 'hua', r"\inserted{\unsure{intrinsèque|intrinsèquement}}", r"\inserted{\unsure{intrinsèquement|intrinsèque}}"),
 (4, 'hua', r"sur $\unsure{\mathcal E^*|\mathcal E^{(\nu)}}$ une structure", r"sur $\mathcal E^{(\nu)}$ une structure"),
 (4, 'own', r"par un \uline{\unsure{groupe|gr.}} quelconque}", r"par un \unsure{gr.\ \uline{ab.}|\uline{gr.}|\uline{groupe}} quelconque}"),
 (4, 'hua', r"que $(1.4)$ est valable, car", r"que $(1.4)$ \unsure{est valable|sont valables}, car"),
 (5, 'hua', r"l'on \unsure{voudra|considère} que", r"l'on \unsure{voudra|considère|suppose} que"),
 (5, 'hua', r"car on connaît les\\$\pi_\alpha$ pour $\alpha\neq n$, d'où on conclut $\pi_n",
            r"car on connaît déjà les\\$\pi_\alpha$ pour $\alpha\neq n$, d'où aussi $\pi_n"),
 (5, 'hua', r"\unsure{Restons}\\donc pour", r"\unsure{Restons|Reste|Mais}\\donc pour"),
 (6, 'own', r"\inserted{resp. $(3.2)_i$}", r"\inserted{\unsure{resp.|ou v.} $(3.2)_i$}"),
 (7, 'hua', r"en utilisant la deuxième relation", r"en utilisant la \unsure{deuxième|dernière} relation"),
 (7, 'own', r"partons encore de la situation $M^*$,", r"partons encore \unsure{du cas particulier|d'un cas particulier|de la situation} $M^*$,"),
 (8, 'hua', r"\unsure{sur-anneau|sous-anneau}", r"sur-anneau"),
 (8, 'hua', r"\inserted{on a $\varphi_i,\psi_{2n-i}\in\mathcal E$, \unsure{d'où|donc}}",
            r"\inserted{\unsure{on a|comme} $\varphi_i,\psi_{2n-i}\in\mathcal E$, \unsure{d'où|donc|et}}"),
 (8, 'hua', r"et \uline{comme} \deleted{\unsure{donc}}", r"et \unsure{\uline{comme}|\deleted{comme}} \deleted{\unsure{donc}}"),
 (9, 'hua', r"équivalent [en termes intrinsèques", r"équivaut [en termes intrinsèques"),
 (9, 'hua', r"{\inserted{(en vertu des\\ n° 4, 5)}}", r"{\inserted{(\unsure{en vertu des|comme on a vu aux}\\ n° 4, 5)}}"),
 (10, 'hua', r"(\unsure{défin.|défini|définit} $\Lambda$)", r"(\unsure{défin.|défini|définit|définissant} $\Lambda$)"),
 (10, 'hua', r"\inserted{\unsure{a déjà dit|a déjà dit que}}", r"\inserted{\unsure{a déjà dit|a déjà indiqué}}"),
 (11, 'own', r"par récurrence \unsure{ascendante|descendante} sur $i\leq n$", r"par récurrence ascendante sur $i\leq n$"),
 (12, 'hua', r"il faut, \unsure{égalt} $\pi_{2n-i,\alpha}", r"il faut, \unsure{égalt|de même} $\pi_{2n-i,\alpha}"),
 (13, 'own', r"(\text{si }i\unsure{\leq|<}n-1)", r"(\text{si }i\leq n-1)"),
 (13, 'own', r"\Lambda\in\mathcal E^{\unsure{(2)|(-2)}}", r"\Lambda\in\mathcal E^{(2)}"),
 (14, 'own', r"{cf. ci-\unsure{†|dessus}\\pour l'anneau", r"{cf. n\textsuperscript{o} 7\\pour l'anneau"),
 (14, 'hua', r"satisfait à la condition de $(6.1)\unsure{(i)|_i}$", r"satisfait à la condition de $(6.1)\unsure{(i)|_i|(\omega)}$"),
 (14, 'hua', r"est l'opérateur associé défini par $(6.5)$.", r"est l'opérateur associé défini par $(6.\unsure{5|15})$."),
 (15, 'hua', r"\unsure{devront}", r"\unsure{devraient|devront}"),
 (15, 'hua', r"La multiplication des bases \unsure{ne}", r"La multiplication des \unsure{élts de base|élts de cette base|bases} \unsure{ne}"),
 (15, 'hua', r"(\unsure{qui au fond} \unsure{unique est}", r"(\unsure{qui au fond|ni du fait} \unsure{unique est}"),
 (15, 'hua', r"comme au n\textsuperscript{o} 6, et de $\mathcal E$", r"comme au n\textsuperscript{o} 1, et de $\mathcal E$"),
 (15, 'own', r"\deleted{\unsure{sous-algèbre}}\inserted{anneau} gradué de", r"ss-\deleted{algèbre}\inserted{anneau} \unsure{graduée|gradué} de"),
 (15, 'own', r"\unsure{(iii)|(ii)} Il existe un hom", r"(ii) Il existe un hom"),
 (16, 'hua', r"appliquant $\mathbf L_0$ sur $L$,", r"appliquant $\mathbf L_0$ en $L$,"),
 (16, 'hua', r"(donc $\pi_i\in\mathcal E$)", r"(\unsure{donc|des} $\pi_i\in\mathcal E$)"),
 (16, 'hua', r"\deleted{\unsure{respectant la graduation de} $\mathcal E$ \unsure{par les} $\pi_i$}.",
             r"\deleted{\unsure{exprimant|respectant} la graduation de $\mathcal E$ par $(1.3)$}."),
 (17, 'hua', r"la vérification, pour tt", r"la validité, pour tt"),
 (17, 'hua', r"la graduation de $\mathcal E$ :", r"la graduation de $\mathcal E$ : \unsure{primo,|a priori,}"),
 (17, 'hua', r"{(elle sera définie à posteriori par", r"{(elle sera \unsure{définie|obtenue} à posteriori par"),
 (17, 'hua', r"\margin{On a aussi : $\exists$", r"\margin{\unsure{On a aussi|Ou encore|On convient} : $\exists$"),
 (17, 'own', r"Il faut donc se donner en même temps \uline{$L$ et les $\pi_i$}.", r"Il faut donc se donner en $=$ temps \uline{$L$ et les $\pi_i$}."),
 (18, 'own', r"{\unsure{déjà pour}}", r"{\unsure{déjà pour $n$}}"),
]

def macro_args(text, name):
    out = []
    pat = "\\" + name + "{"
    i = 0
    while True:
        j = text.find(pat, i)
        if j < 0:
            return out
        k = j + len(pat); d = 1; s = k
        while d and k < len(text):
            if text[k] == '{': d += 1
            elif text[k] == '}': d -= 1
            k += 1
        out.append(text[s:k-1]); i = k

def has_alt(arg):
    d = 0
    for ch in arg:
        if ch == '{': d += 1
        elif ch == '}': d -= 1
        elif ch == '|' and d == 0: return True
    return False

def counts(text):
    u = macro_args(text, 'unsure')
    alt = sum(1 for a in u if has_alt(a))
    ill = len(macro_args(text, 'illegible'))
    return len(u), alt, ill

def name(n): return "MPL_16+47+54+44_16_scan%03d.tex" % n

orig = {n: open(os.path.join(SRC, name(n)), encoding='utf-8').read() for n in SCANS}
stages = {'first': dict(orig), 'own': dict(orig), 'all': dict(orig)}
for (n, tag, old, new) in C:
    for st in (['own', 'all'] if tag == 'own' else ['all']):
        t = stages[st][n]
        c = t.count(old)
        if c != 1:
            sys.exit("change on scan %d matches %d times: %r" % (n, c, old))
        stages[st][n] = t.replace(old, new)

os.makedirs(OUT, exist_ok=True)
for n in SCANS:
    with open(os.path.join(OUT, name(n)), 'w', encoding='utf-8', newline='') as f:
        f.write(stages['all'][n])

tot = {k: [0, 0, 0] for k in stages}
print("scan  first(unsure,alt,illeg)  own  all   changes")
for n in SCANS:
    row = []
    for k in ('first', 'own', 'all'):
        c = counts(stages[k][n]); row.append(c)
        for m in range(3): tot[k][m] += c[m]
    nch = sum(1 for x in C if x[0] == n)
    print("%3d   %s  %s  %s  %d" % (n, row[0], row[1], row[2], nch))
print("TOTAL first", tot['first'], "own", tot['own'], "all", tot['all'], "changes", len(C),
      "own", sum(1 for x in C if x[1] == 'own'), "hua", sum(1 for x in C if x[1] == 'hua'))
# braces balanced check
for n in SCANS:
    t = stages['all'][n]
    if t.count('{') != t.count('}'):
        print("BRACE MISMATCH scan", n, t.count('{'), t.count('}'))

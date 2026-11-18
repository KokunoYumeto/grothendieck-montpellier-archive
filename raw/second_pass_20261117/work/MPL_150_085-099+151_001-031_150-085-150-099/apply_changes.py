"""Apply the second-pass corrections (Claude Opus 5.5 at effort max, 17 Nov 2026) to the first-pass
page files of cote 150, scans 085-099, and write the corrected files to the block's output folder.
Every old string must occur exactly once in its file; otherwise the script stops."""
import os
import re
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
SRC = os.path.join(BASE, "returns", "MPL_150_085-099+151_001-031_unzipped", "pages")
OUT = os.path.join(BASE, "second_pass", "out", "MPL_150_085-099+151_001-031")
NAME = "MPL_150_085-099+151_001-031_150_scan%03d.tex"
NL = "\n"

CH = [
    # 085
    (85, r"$\Sigma_J^{\unsure{L|*}}$", r"$\Sigma_J^{L}$"),
    (85, r"\[\deleted{\unsure{\bigcup_{j\in J}\Sigma_j}}\quad X_J^{\deleted{\unsure{*}}}",
         r"\[\deleted{\Vert}\ \text{\uline{NB}}\ \deleted{\unsure{\bigcup_{j\in J}\Sigma_j}}\quad X_J^{\deleted{\unsure{*}}}"),
    (85, r"idéal \unsure{engendré} par", r"idéal engendré par"),
    (85, r"\exists j\in J\ \unsure{avec}\ i\leq j", r"\exists j\in J\ \text{avec}\ i\leq j"),
    (85, r"X_j^*\unsure{\equiv}X_{\bar J}^*", r"X_j^*\unsure{\equiv|=}X_{\bar J}^*"),
    (85, r"d\text{ avec au moins 2 termes}", r"d\text{ \unsure{ayant|avec} au moins 2 termes}"),
    # 086
    (86, r"\uline{disjoints}", r"\uline{\unsure{disjointes|disjoints}}"),
    (86, r"on a une inclusion d'idéaux", r"on a une \unsure{suite|inclusion} d'idéaux"),
    (86, r"T_J^{\mathrm{eff}}&=\deleted{", r"T_J&\overset{\mathrm{déf}}{=}\deleted{"),
    (86, r"\Sigma_{I'}\arrow[d,equal]\\", r"\Sigma_{I'}\arrow[d,equal,\"\unsure{?}\"]\\".replace('\\"', '"')),
    (86, r"\text{él. final}\in L", r"\text{él. final \deleted{\illegible{1}}}\in L"),
    # 087
    (87, r"\bar T_{\Sigma_J,\Sigma_{I'}}=\Sigma_{I'}\cap\bigcup_{j\in J}\bar T_j",
         r"T_{\Sigma_J,\Sigma_{I'}}=\Sigma_{I'}\cap\bigcup_{j\in J}T_j"),
    (87, r"avec la \unsure{construction} ci-dessous", r"avec la notation ci-dessous"),
    (87, r"\underbrace{\mathring T_{\unsure{\bar J'}}}_{\displaystyle\bigcup_{\deleted{\unsure{\forall}}j\in\unsure{\bar J'}}\mathring T_j}",
         r"\underbrace{\mathring T_{\unsure{\bar J'|J'}}}_{\displaystyle\bigcup_{\deleted{\unsure{\forall}}j\in\unsure{\bar J'|J'}}\mathring T_j}"),
    # 088
    (88, r"utilise les \deleted{structures \unsure{de}\ \unsure{coniques}} \inserted{\unsure{fibrations}} locales.",
         r"utilise les \deleted{structures} \inserted{\unsure{fibrations|rétractions}} \inserted{\deleted{\unsure{de ri.}}} \deleted{coniques} locales."),
    (88, r"dans \unsure{la géom. algéb.|les géométries}", r"dans \unsure{le cas équisingulier|la géom. algéb.}"),
    # 089
    (89, r"\unsure{Soit} $\unsure{A|J}\subset I$", r"\deleted{\unsure{Si}} \unsure{Soit} $\unsure{A|J}\subset I$"),
    (89, r"On a donc pour toute partie $A$ de $I$", r"On a donc pour \unsure{tte|une} partie $A$ de $I$"),
    (89, r"\inserted{\uline{Pour}} Une partie", r"\inserted{Pour} Une partie"),
    # 090
    (90, r"i.e. $I'\subset\bar K$ et $I'\subset\widetilde J$", r"i.e. $I'\unsure{\subset|=}\bar K$ et $I'\subset\widetilde J$"),
    (90, r"et \unsure{ainsi} $I'=\widetilde J\cap\bar K$", r"et \unsure{ainsi|on a} $I'=\widetilde J\cap\bar K$"),
    # 091
    (91, r"\deleted{Une stratification \inserted{\deleted{indicielle}} de type $I$}",
         r"\deleted{Une \unsure{filtration|stratification} \inserted{\deleted{\unsure{ordinaire|indicielle}}} de type $I$}"),
    (91, r"Une \uline{stratification indicielle}, de type", r"Une \uline{stratification \unsure{ordinaire|indicielle}}, de type"),
    (91, r"\deleted{\unsure{Pour ces conditions}}", r"\deleted{\unsure{Pour ces conditions|Posons les conditions}}"),
    (91, r"alors \deleted{\unsure{les}} $X_d{}_{d\in\mathrm{Drap}I}$ forment un \deleted{\unsure{objet}} espace",
         r"alors \deleted{\unsure{$\varinjlim$|les}} $X_d{}_{d\in\mathrm{Drap}I}$ forment un \deleted{\unsure{syst.|objet}} espace"),
    (91, r"``résolution'' semi-simpliciale de $X$", r"``résolution'' semi-simpl. de $X$"),
    # 092
    (92, r"i.e. $j<i\Rightarrow X_j$ \uline{non} dense dans $X_i$.", r"i.e. $j<i\Rightarrow X_j$ \uline{rare} dans $X_i$."),
    (92, r"\deleted{\unsure{Cet axiome de fidélité implique}}",
         r"\deleted{\unsure{Stratifications de fidélité implique|Cet axiome de fidélité implique}}"),
    (92, r"donc on aura, si $i,j\in I$", r"donc on aura, si $i,j\in J$"),
    # 093
    (93, r"$X_{\unsure{J'}}^*$", r"$X_{\unsure{?|J'}}^*$"),
    # 094
    (94, r"(\text{si str. fidèle})", r"(\text{si strat. fidèle})"),
    (94, r"cela s'exprime par l'exigence plus fort", r"cela s'exprime par l'axiome plus fort"),
    (94, r"X_{J\cup K}^*=X_J^*\cup\unsure{X_K^*}$.}", r"X_{J\cup K}^*=X_J^*\cup X_K^*$.}"),
    # 095
    (95, r"\deleted{\unsure{la réciproque}} réciproque est vraie", r"la \deleted{\illegible{1}} \inserted{réciproque} est vraie"),
    (95, r"($X$ \unsure{métrisable})", r"($X$ métrisable)"),
    (95, r"\Longleftrightarrow X_i^*\cap\overline{X_j^*}", r"\unsure{\Longleftarrow|\Longleftrightarrow} X_i^*\cap\overline{X_j^*}"),
    (95, r"\text{pro-vois ouvert de $X$ est normal}",
         r"\text{\unsure{partie ouverte|pro-vois ouvert} de $X$ est \unsure{normale|normal}}"),
    # 096
    (96, r"\margin{$^*$(et les \unsure{protopos} \unsure{homotopes} $\mathcal V_{i_0\ldots i_n}^{\unsure{Z}}$, \unsure{cf.} plus bas)}",
         r"\margin{$^*$(et \unsure{des|les} protopos homotopes $\mathcal V_{i_0,\ldots,i_n}^{Z}$ plus bas)}"),
    # 097
    (97, r"qui contient \inserted{$X_{i_n}^*$ (on sait que $\unsure{X_{i_n}^*\cap\mathcal V_{i_0\ldots i_n}}\overset{(\overset h\sim)}{\hookrightarrow}\mathcal V_{i_0\ldots i_n}$)}",
         r"qui contient \deleted{\illegible{2}} $X_{i_n}^*$ \inserted{(\unsure{de sorte que|on sait que} $X_{i_n}\unsure{\overset{(\overset h\sim)}{\hookrightarrow}}\mathcal V_{i_n}^{Z}\overset{(\overset h\sim)}{\hookrightarrow}\mathcal V_{i_n}$)}"),
    # 098
    (98, r"\mathcal V_{J\deleted{,L}}^L&=", r"\mathcal V_{J\deleted{,L}}^{L\deleted{\unsure{\flat|\natural}}}&="),
    (98, r"\subset\mathcal V_{J,L}\cap X_L^*=\mathcal V_{J,L}^{\deleted{\unsure{Z}}}",
         r"\unsure{\subset|=}\mathcal V_{J,L}\cap X_L^*=\mathcal V_{J,L}^{\deleted{\unsure{Z}}X_L^*}"),
    # 099
    (99, r"donc si \inserted{$J,L$ des bandes et $J\prec L$, et si} $Z$ contient $\deleted{\unsure{X_J^*\cap}}X_L^*$, on aura" + NL + r"\deleted{clairement}",
         r"\deleted{clairement} \inserted{donc si} \inserted{$J,L$ des bandes et $J\prec L$, et si} $Z$ contient $\deleted{\unsure{X_J^*\cap}}X_L^*$, on aura" + NL
         + r"% second pass: the struck word stands at the head of this line, with ``donc si'' written above it"),
]

os.makedirs(OUT, exist_ok=True)
pat = re.compile(r"\\unsure\{|\\illegible\{")
tot_in = tot_out = 0
for n in range(85, 100):
    with open(os.path.join(SRC, NAME % n), encoding="utf-8", newline="") as f:
        txt = f.read()
    crlf = "\r\n" in txt
    work = txt.replace("\r\n", "\n")
    before = len(pat.findall(work))
    bal0 = work.count("{") - work.count("}")
    for scan, old, new in CH:
        if scan != n:
            continue
        c = work.count(old)
        if c != 1:
            sys.exit("scan %03d: old string found %d times: %s" % (n, c, old[:80]))
        work = work.replace(old, new)
    if work.count("{") - work.count("}") != bal0:
        sys.exit("scan %03d: the corrections changed the brace balance" % n)
    if bal0:
        print("scan %03d: note, first-pass file already has brace balance %d (unchanged)" % (n, bal0))
    after = len(pat.findall(work))
    tot_in += before
    tot_out += after
    if crlf:
        work = work.replace("\n", "\r\n")
    with open(os.path.join(OUT, NAME % n), "w", encoding="utf-8", newline="") as f:
        f.write(work)
    print("scan %03d: %d changes, unsure/illegible %d -> %d" % (n, sum(1 for s, _, _ in CH if s == n), before, after))
print("total replacements", len(CH), "| unsure/illegible marks", tot_in, "->", tot_out)

"""Apply the second-pass corrections to the first-pass pages of block MPL_16+47+54+44 16-037-16-053.
Each replacement is exact and asserted by its count; nothing else in a page changes."""
import os

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
SRC = BASE + "returns/MPL_16+47+54+44_unzipped/pages/"
OUT = BASE + "second_pass/out/MPL_16+47+54+44/"
NAME = "MPL_16+47+54+44_16_scan%03d.tex"
N = "\n"

E = {}  # scan -> list of (old, new, expected count)
E[37] = [(r"$\overline{\{\unsure{X|x}\}}$", r"$\overline{\{X\}}$", 2)]
E[38] = [
    (r"\deleted{\unsure{A}} Moyennant l'isom $(\unsure{\alpha})$", r"A Moyennant l'isom $(\alpha)$", 1),
    (r"i,j\geq0}}L_X^jP^i(X)," + N, r"i,j\geq0}}L_X^jP^{\unsure{j|i}}(X)," + N, 1),
    (r"\uline{L_X^jP^i(X)}\oplus E^{(n-1)}" + N + r"=\coprod_{i\geq n+1}P^{\unsure{j|i}}(X)\oplus E^{n-1}",
     r"\uline{L_X^jP^j(X)}\oplus E^{(n-1)}" + N + r"=\coprod_{i\geq n+1}P^j(X)\oplus E^{(n-1)}", 1),
    (r"\[\coprod_{\substack{i+j\leq n-1\\i,j\geq0}}L_X^jP^i(X)\]", r"\[\coprod_{\substack{i+j=n-1\\i,j\geq0}}L_X^jP^i(X)\]", 1),
    (r"P^i(X)+E^{n-1}=\coprod_{0\leq i\leq\unsure{n+1|n-1}}P^i(Y)", r"P^i(X)+E^{n-1}\simeq\coprod_{0\leq i\leq\unsure{n+1|n-1}}P^i(Y)", 1),
    (r"\margin{\[\Longleftarrow\quad\Lambda_Y^m\varphi^*=\varphi^*\Lambda_X^m(\operatorname{id}-\bar\Sigma)\]",
     r"\margin{\[\Lambda_Y^m\varphi^*=\varphi^*\Lambda_X^m(\operatorname{id}-\bar\Sigma)\quad\Longleftarrow\]", 1),
]
E[40] = [
    (r"\substack{L_X\Lambda_X\\=\\\operatorname{id}_X", r"\substack{L_X\Lambda_X\\\Vert\\\operatorname{id}_X", 1),
    (r"\inserted{\unsure{L|\Lambda}}", r"\inserted{\unsure{\Lambda|L}}", 1),
]
E[42] = [
    (r"\text{égal à }\Lambda_X\varphi_i\mid H^i(Y)", r"\text{égal : }\Lambda_X\varphi_{\unsure{i|*}}\mid H^i(Y)", 1),
    (r"(car $p_n^X\varphi_*=0$)", r"(car $p_{\unsure{n}}^X\varphi_*=0$)", 1),
    (r"\deleted{$X\unsure{\sim}Y,\ \unsure{Y_\alpha}$}", r"\deleted{$X\times Y,\ Y\times$}", 1),
    (r"les uns sont \unsure{des sections} des autres, hyperplans non singuliers.",
     r"\unsure{pour une suite décroissante de sections hyperplanes non singulières|les uns sont des sections des autres, hyperplans non singuliers}.", 1),
    (r"\unsure{Condor|Cordor|Concorde}", r"Gevaert", 42),
]
E[43] = [
    (r"\margin{\uline{\unsure{Virer|Vider}} (ii) sauf \unsure{raison} sérieuse !}", r"\margin{\uline{\unsure{Vider|Virer}} (ii) sauf raison sérieuse !}", 1),
    (r"$p$ est l'homomorphisme canonique ;", r"$p$ est l'homomorphisme \unsure{canpnique|canonique} ;", 1),
]
E[45] = [
    (r"then $\unsure{A|Q}_{\unsure{\ell|\chi}}(X,", r"then $A_{\unsure{\ell|\chi}}(X,", 1),
    (r"(verieté \uline{polarisée})", r"(varieté \uline{polarisée})", 1),
    (r"suite décroissante de sections hyperplanes", r"suite décorissante de sections hyperplanes", 1),
]
E[46] = [
    (r"(X\times Y)^0+A_{\unsure{\ell|\chi}}(Y\times Z)^0", r"(X\mathrm{x}Y)^0+A_{\unsure{\ell|\chi}}(Y\mathrm{x}Z)^0", 1),
    (r"$(\mathrm{i})\longrightarrow(\mathrm{iii})$", r"$(\mathrm{i})\Longrightarrow(\mathrm{iii})$", 1),
    (r"in arbitrary dimension", r"in arbitray dimension", 2),
    (r"\phi", r"\varphi", 6),
]
E[47] = [
    (r"the $\pi_1$ for a surface", r"the $\pi_i$ for a surface", 1),
    (r"Kleimann's", r"Kleiman\deleted{n}'s", 1),
    (r"$X\times Y$", r"$X\mathrm{x}Y$", 1),
]
E[48] = [
    (N + "6.1.1966" + N, N + r"\margin{6.1.1966}" + N, 1),
    (r"``motive-theoretically''", r"``motive-theor\deleted{\unsure{i}}etically''", 1),
    (r"the following conditions:", r"the follwing conditions:", 1),
    (r"\unsure{the} algebraic isomorphism", r"\unsure{the|an} algebraic isomorphism", 1),
]
E[49] = [
    (r"preliminaray", r"preliminar\deleted{\unsure{a}}y", 1),
    (r"\unsure{\delta|d}", r"\unsure{\delta|d|j}", 3),
    (r"\phi", r"\varphi", 1),
    (r"$I(X\times X)$", r"$I(X\mathrm{x}X)$", 1),
]
E[50] = [
    (r"\unsure{crittcal|critical}", r"\unsure{crittval|critical}", 1),
    (r"follows from the conjunction of", r"follows from the conjuction of", 1),
    (r"if $2j\geq n-1$", r"if $2\unsure{j|i}\geq n-1$", 1),
    (r"$H^{j+2}(X)$ is", r"$H^{\unsure{j|i}+2}(X)$ is", 1),
    (r"\phi", r"\varphi", 2),
    (r"\times", r"\mathrm{x}", 11),
]
E[51] = [
    (r"du groupe abélien", r"du \unsure{gpe|groupe} abélien", 1),
    (r"sur les facteurs \unsure{élémentaires} $\unsure{\xi^j|\xi_j}P^i$", r"sur les facteurs élémentaires $\xi^jP^i$", 1),
    (r"il suffit de regarder les $\unsure{\xi^j|\xi_j}P^i$", r"il suffit de regarder les $\xi^jP^i$", 1),
    (r"facteurs \unsure{décomposition|élémentaires} de", r"facteurs \unsure{élémentaires|décomposition} de", 1),
    (r"(et vice \unsure{versa})", r"(et vice versa)", 1),
]
E[52] = [
    (r"\unsure{Filting|Fitting}", r"Filting", 3),
    (r":" + N + r"\margin{\unsure{!}}" + N + N + "si", ":" + N + N + "si", 1),
    (r"une algèbre de p. f. sur $A$", r"une algèbre de \margin{\unsure{!}}p. f. sur $A$", 1),
]
E[53] = [
    (r"sont $\in\unsure{\operatorname{Alg}|A}$", r"sont $\in\operatorname{Alg}$", 1),
    (r"si $k'\unsure{\leq|<}k$", r"si $k'\leq k$", 1),
    (r"est nul sur $H^{\unsure{j|i}}$", r"est nul sur $H^j$", 1),
    (r"donc $u_{\unsure{k|n}}\xi^{n-k}T_k", r"donc $u_k\xi^{n-k}T_k", 1),
    (r"\deleted{\unsure{ainsi}}", r"\deleted{\unsure{ainsi|aussitôt}}", 1),
    (r"\inserted{de noyau $N$,}", r"\inserted{\unsure{de noyau|des mêmes} $N$,}", 1),
    (r"\deleted{\unsure{coïncide à} $\unsure{1}$}", r"\deleted{\unsure{coïncide à|coïncide avec} $\unsure{1}$}", 1),
]
# Convention: a plain dash without arrowhead as on scans 42 and 45 (\mathbin{-}).
DASH = {46: 3, 48: None, 49: None, 51: None, 53: None}

os.makedirs(OUT, exist_ok=True)
tot_fp = tot_new = 0
for scan in range(37, 54):
    src = open(SRC + NAME % scan, encoding="utf-8").read()
    txt = src
    for old, new, cnt in E.get(scan, []):
        c = txt.count(old)
        assert c == cnt, (scan, old, c, cnt)
        txt = txt.replace(old, new)
    if scan in DASH:
        c = txt.count(r"\mathrel{-}")
        print("scan %d: \\mathrel{-} -> \\mathbin{-} x%d" % (scan, c))
        txt = txt.replace(r"\mathrel{-}", r"\mathbin{-}")
    open(OUT + NAME % scan, "w", encoding="utf-8", newline="").write(txt)
    a, b = src.count(r"\unsure{"), txt.count(r"\unsure{")
    ell_a = src.count(r"\unsure{\ell|")
    ell_b = txt.count(r"\unsure{\ell|")
    tot_fp += a
    tot_new += b
    print("scan %d: unsure first pass %d -> now %d (of which ell|chi/l/1: %d -> %d); illegible %d" % (
        scan, a, b, ell_a, ell_b, txt.count(r"\illegible{")))
print("TOTAL unsure first pass", tot_fp, "now", tot_new)

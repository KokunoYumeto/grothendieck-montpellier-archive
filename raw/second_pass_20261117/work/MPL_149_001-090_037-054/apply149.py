"""Apply the second-pass corrections to MPL_149_001-090, scans 037-054.

Reads the first-pass page files, applies each (old -> new) replacement, checks that every old string occurs
exactly once in its page, and writes every page of the block (changed or not) to second_pass/out/MPL_149_001-090/.
usage: python -I -B apply149.py
"""
import os
import sys

ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
SRC = ROOT + "returns/MPL_149_001-090_unzipped/pages/MPL_149_001-090_scan{:03d}.tex"
OUT = ROOT + "second_pass/out/MPL_149_001-090/MPL_149_001-090_scan{:03d}.tex"

CHANGES = {
    37: [
        (r"OPS que $G$ est la jacobienne", r"OPS que $G$ est \unsure{la} jacobienne"),
        (r"$u\in J_Y^0(K)$", r"$u\in J_Y^0(k)$"),
        (r"de $U$ en $Y$ est l'identité", r"de $U$ dans $Y$ est l'identité"),
        (r"Ceci résulte p.ex.", r"\unsure{Cela|Cet} résulte p.ex."),
        (r"partie abélienne de $J_Y^0(K)$ est nulle", r"partie abélienne de $J_Y^0(k)$ est nulle"),
        (r"(\mathbb G_m^I/\mathbb G_m)(K)", r"(\mathbb G_m^I/\mathbb G_m)(k)"),
    ],
    38: [
        (r"}}$ déduite de $\widehat Y$ en contractant $I$ en un pt, en identifiant",
         r"}}$ (déduite de $\widehat Y$ en contractant $I$ en un pt) en identifiant"),
        (r"\inserted{de $J_Y^1$}", r"\inserted{\unsure{dans|de} $J_Y^1$}"),
        (r"\deleted{(pour un genre $g\geq1$)}", r"\deleted{(pour un genre $g\neq1$)}"),
        (r"\inserted{\unsure{si comme|comme} l'image", r"\inserted{\unsure{et|si} comme l'image"),
        (r"Si $g=0$, alors $r=\operatorname{card}I\geq3$", r"Si $g=0$, donc $\nu=\operatorname{card}I\geq3$"),
        (r"de $I$ à deux éléments", r"de $I$ à deux élts"),
        (r"\deleted{projections} \inserted{applications}", r"\deleted{applications} \inserted{morphismes}"),
        (r"$U\xrightarrow{i}Y$, don-", r"$U\xrightarrow{i}Y$, \unsure{inclusion}"),
    ],
    39: [
        (r"de $H_1(U)$ sont", r"dans $H_1(U)$ sont"),
        (r"\deleted{\unsure{que}} implique", r"\deleted{\unsure{on a} $f(J)$)} implique"),
    ],
    40: [
        (r"Alors en remplaçant $Y=", r"\unsure{Idem}, en remplaçant $Y="),
    ],
    42: [
        (r"n'auront pas de sens", r"\unsure{n'auraient|n'auront} pas de sens"),
        (r"\unsure{Pour|Or} il est essentiel", r"\unsure{Donc|Or} il est essentiel"),
    ],
    43: [
        (r"ce qui nous intéresse", r"ce \unsure{que|qui} nous intéresse"),
    ],
    45: [
        (r"E_{K'}^\circ\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}",
         r"E_{K'}^{\unsure{\circ}}\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}"),
        (r"\deleted{$\Gamma_{\mathbb Q}$, \unsure{soit}}", r"\deleted{$\Gamma_{\mathbb Q}$, \unsure{soit} \illegible{1}}"),
    ],
    46: [
        (r"dont on suppose d'avance", r"dont on \unsure{décrète} d'avance"),
        (r"\unsure{elles|tels}", r"\unsure{tels|elles}"),
    ],
    47: [
        (r"dès que $V$ est plongé dans une VA", r"dès que $V$ \unsure{se plonge|est plongé} dans une VA"),
        (r"\unsure{types|topos}", r"\unsure{topos|types}"),
    ],
    48: [
        (r"\inserted{$V$ \deleted{\unsure{disjoint}} \unsure{supposé}}",
         r"\inserted{$V$ \deleted{\unsure{séparés}} \unsure{séparés}}"),
    ],
    49: [
        (r"\Pi_U^{\unsure{\Gamma'^\circ}}", r"\Pi_U^{\Gamma'^\circ}"),
        (r"\inserted{\unsure{adaptés pour $U$}}", r"\inserted{(\unsure{complètes} pour $U$)}"),
    ],
    50: [
        (r"(morphismes de transition affines\inserted{ \unsure{imm. ouvertes}}, sans plus)",
         r"(morphismes de transition \inserted{\unsure{imm. ouvertes}} affines sans plus)"),
        (r"et tels que l'image soit ouverte", r"et \unsure{telles} que l'image soit ouverte"),
    ],
    51: [
        (r"J'ai en vue avant tout des", r"J'ai en vue surtout des"),
        (r"on reconstruira par recollement", r"on reconstruirait par recollement"),
    ],
    52: [
        (r"\unsure{Qcts|Dcts}", r"\unsure{lacets|Qcts}"),
        (r"soient isomorphes", r"soient \unsure{ég|$fg$} isomorphes"),
    ],
    53: [
        (r"$E_K$. Ce qui signifie", r"$E_K$ (ce qui signifie"),
        (r"\text{Classes d'isomorphisme}", r"\text{Classes d'isomorphie}"),
        (r"\unsure{on a pour} $\forall\ i", r"\unsure{on a} que pour $\forall\ i"),
        (r"$E_U,E_{\unsure{K}}$", r"$E_U,E_K$"),
    ],
    54: [
        (r"\inserted{(en plus)}", r"\inserted{(de plus)}"),
    ],
}

errors = []
total = 0
result = {}
for n in range(37, 55):
    with open(SRC.format(n), encoding="utf-8", newline="") as fh:
        text = fh.read()
    for old, new in CHANGES.get(n, []):
        c = text.count(old)
        if c != 1:
            errors.append("scan {:03d}: {!r} occurs {} times".format(n, old, c))
            continue
        text = text.replace(old, new)
        total += 1
    result[n] = text
if errors:
    print("\n".join(errors))
    sys.exit(1)
for n, text in result.items():
    with open(OUT.format(n), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
print("applied", total, "changes; wrote", len(result), "files")

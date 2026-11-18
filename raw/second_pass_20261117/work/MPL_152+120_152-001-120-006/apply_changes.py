"""Apply the second-pass corrections of block MPL_152+120_152-001-120-006 to the first-pass page files.

Each change is an exact string replacement that must match exactly once (or the stated count).
Unchanged files are copied as they are. Output: second_pass/out/MPL_152+120/.
"""
import os, sys

BASE = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + "/returns/MPL_152+120_unzipped/pages"
OUT = BASE + "/second_pass/out/MPL_152+120"

FILES = ["152_scan%03d" % i for i in range(1, 14)] + ["120_scan%03d" % i for i in range(1, 7)]

C = {}  # name -> list of (old, new, count)


def ch(name, old, new, count=1):
    C.setdefault(name, []).append((old, new, count))


# ---------------- cote 152 ----------------
ch("152_scan002", r"{\unsure{Sommet} \unsure{principal}}", r"{\unsure{Sommet principal|sommets principaux}}")

ch("152_scan003", r"\text{disques\inserted{or.}\uline{\unsure{linéarisés}}}\arrow[r,leftrightarrow]&",
   r"\begin{gathered}\text{disques\inserted{or.} découpés}\\\text{par cordes}\end{gathered}\arrow[r,leftrightarrow]&")
ch("152_scan003", r"\begin{gathered}\text{\unsure{ordres}}\\\text{à involuti.}\\\text{\unsure{sans} pt fixe}\end{gathered}",
   r"\begin{gathered}\text{contours}\\\text{à involuti.}\\\text{\unsure{sans} pt fixe}\end{gathered}")
ch("152_scan003", r"\text{(: bouts libres)}", r"\text{(à bouts libres)}")
ch("152_scan003", r"\begin{gathered}\text{\unsure{ordres}}\\\text{à inv.}\\\text{\unsure{cpt.} \unsure{lin.}}\\\text{sans pt fixe}\\\text{\unsure{mais}}\\\text{\unsure{pointés}.}\end{gathered}",
   r"\begin{gathered}\text{contours}\\\text{à inv.}\\\text{\unsure{cpt.} \unsure{lin.}}\\\text{sans pt fixe}\\\text{\unsure{non|mais}}\\\text{\unsure{pénétrante|pointés}}\end{gathered}")
ch("152_scan003", r"de long. $n$ équivaut à la cat. isotopique des systèmes \unsure{formés|finis} d'un disque $D$ \inserted{en général orienté} \unsure{d'une|d'un} ``découpage en cordes'' de ce disque, avec au moins un sommet sur chaque \unsure{cpt.} découpée sur",
   r"de long. $n$ équivaut : la cat. \unsure{isotypique|isotopique} des systèmes formés d'un disque $D$ \inserted{en général orienté} d'un ``découpage par cordes'' de ce disque, avec au moins un sommet sur chaque \unsure{arête|cpt.} découpée sur")
ch("152_scan003", r"\uline{Type de mot \unsure{totalitaire}}", r"\uline{Type de mot \unsure{totalitaire|réduit}}")
ch("152_scan003", r"(\unsure{non} trivial)", r"(\unsure{non|i.e.} trivial)")

ch("152_scan004", r"Structure : Graphe \unsure{segment}, avec", r"Structure : Graphe \unsure{segment|segmenté}, avec")
ch("152_scan004", r"\text{orbite }\inserted{\xi}\text{ de }", r"\text{orbite }\inserted{\unsure{\varepsilon|\xi}}\text{ de }")
ch("152_scan004", r"\uline{et} le graphe déduit de $\Gamma$ par contraction en 1 point de l'une des \deleted{\unsure{deux}} arêtes $\in\xi$,",
   r"\uline{et} le graphe \inserted{$\Gamma'$} déduit de $\Gamma$ par contraction en 1 point de l'une des \deleted{\unsure{deux}} arêtes $\in\unsure{\varepsilon|\xi}$,")
ch("152_scan004", r"(ceux d'ordre 1 aussi)", r"(ceux d'1 aussi)")

ch("152_scan005", r"d'ordre $\leq\unsure{1|2}$, il y en a", r"d'ordre $\leq1$, il y en a")

ch("152_scan008", r"$\vec A(C)$ s'identifie à", r"$\vec A(C)$ s'identifie :")
ch("152_scan008", r"\unsure{\sigma_\Gamma|\mathrm{id}}\times\tau", r"\unsure{\sigma_\Gamma|\mathrm{id}|\sigma_0}\times\tau")

ch("152_scan009", r"\mspage{\unsure{8|2}}", r"\mspage{8}")

ch("152_scan010", r"Ces deux données \deleted{\unsure{par}} sur le contour $C$", r"Ces deux données \unsure{pour} le contour $C$")
ch("152_scan010", r"\uline{déploiement} \unsure{du} graphe", r"\uline{déploiement} du graphe")
ch("152_scan010", r"pour \unsure{la circ\({}^{\mathrm{on}}\) actuelle définie|le contour actuel défini} par",
   r"pour la \unsure{carte} \unsure{actuelle définie|actuel défini} par")
ch("152_scan010", r"\unsure{leur position|la partition} est n.p.", r"\unsure{composition|leur position} est n.p.")

ch("152_scan011", r"non \unsure{pénétrante} sur", r"non pénétrante sur")
ch("152_scan011", r"l'arête $\sigma_Ca$,", r"l'arête $\sigma_C^a$,")

ch("152_scan013", r"les régions se rencontrent suivant", r"les régions se \unsure{raccordent} suivant")
ch("152_scan013", r"\inserted{(pas néc. plans orientés)} est équivalente \unsure{à|:} la catégorie isotopique des disques",
   r"\inserted{(pas néc. plus orientés)} est équivalente : la catégorie \unsure{isotypique|isotopique} des disques")

# ---------------- cote 120 ----------------
ch("120_scan002", r"\margin{\unsure{1/18|118}}", r"\margin{\unsure{1978|1778} \illegible{1}}")

ch("120_scan003", r"\forall \unsure{B|A}\in\mathcal M_n,\text{ on a }u^{*-1}(\unsure{B|A})\in\mathcal M_m.",
   r"\forall B\in\mathcal M_n,\text{ on a }u^{*-1}(B)\in\mathcal M_m.")
ch("120_scan003", r"\Longleftrightarrow\unsure{u_*|u^*}(A)\in\mathcal M_n$}", r"\Longleftrightarrow u_*(A)\in\mathcal M_n$}")
ch("120_scan003", r"$u\in\unsure{\mathfrak S_n}$", r"$u\in\mathfrak S_n$")
ch("120_scan003", r"\deleted{\unsure{et en} seulement les \unsure{projections} \unsure{dans}}",
   r"\deleted{et \unsure{$\overline{\mathrm m}$} seulement les \unsure{opérations} \unsure{stand.|dans}}")
ch("120_scan003", r"les $\unsure{\mathfrak S_n|\mathcal M_n}$ sont stables", r"les $\mathfrak S_n$ sont stables")
ch("120_scan003", r"A,B\in\unsure{\mathfrak S_n|\mathcal M_n}\Longrightarrow A\cap B\in\unsure{\mathfrak S_n|\mathcal M_n}",
   r"A,B\in\mathfrak S_n\Longrightarrow A\cap B\in\mathfrak S_n")
ch("120_scan003", r"\inserted{(uniquement $M1$, $M2$, $M4$)}", r"\inserted{(moyennant $M1$, $M2$, $M4$)}")

ch("120_scan004", r"$\forall n\in\mathbb N^{\unsure{0|*}}$", r"$\forall n\in\mathbb N^{*}$")
ch("120_scan004", r"$\unsure{M1|M4}$ implique", r"$M1$ implique")
ch("120_scan004", r"\unsure{n'étant|n'était} vérifiée, les présents", r"\unsure{n'étant|n'était} vérifiée, alors posant")

ch("120_scan005", "\\[\nR_0^I=\\{x\\in R^I\\mid\\{x\\}\\in\\mathcal M_I\\}\n\\]\n\\inserted{$\\widehat R^I$}\n",
   "\\[\n\\begin{array}{l}\nR_0^I=\\{x\\in R^I\\mid\\{x\\}\\in\\mathcal M_I\\}\\\\\n\\unsure{\\cap|\\wedge}\\\\\nR^I\n\\end{array}\n\\]\n")
ch("120_scan005", r"$I,J\ne\varnothing$}", r"$I,J\ne\varnothing$ \ldots}")

ch("120_scan006", r"Aucun de ces exemples n'est particulièrement \unsure{passionnant}.",
   r"Aucun de ces \unsure{exemples} \unsure{n'est} \illegible{2} pour nous!")
ch("120_scan006", r"I\unsure{\cup|\amalg}J", r"I\cup J", count=2)
ch("120_scan006", r"\margin{\unsure{via|vu} $M2$}", r"\margin{via $M2$}")
ch("120_scan006", r"\mathcal M_{\unsure{K|n}}", r"\mathcal M_{K}")
ch("120_scan006", r"\inserted{(on prend $(I,A\in\mathcal M_I)$)}", r"\inserted{(on \unsure{prend|précise} $(I,A\in\mathcal M_I)$)}")
ch("120_scan006", r"équivalente à : $\mathrm{Mod}_{\mathcal M_*}$", r"équivalente : $\mathrm{Mod}_{\mathcal M_*}$")


def main():
    os.makedirs(OUT, exist_ok=True)
    n_rep = 0
    for f in FILES:
        name = "MPL_152+120_" + f + ".tex"
        with open(os.path.join(SRC, name), encoding="utf-8", newline="") as fh:
            t = fh.read()
        crlf = "\r\n" in t
        if crlf:
            t = t.replace("\r\n", "\n")
        for old, new, count in C.get(f, []):
            k = t.count(old)
            if k != count:
                print("MISMATCH", f, k, "expected", count, ":", old[:90])
                sys.exit(1)
            t = t.replace(old, new)
            n_rep += count
        if crlf:
            t = t.replace("\n", "\r\n")
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as fh:
            fh.write(t)
    print("files written:", len(FILES), "replacements:", n_rep)


if __name__ == "__main__":
    main()

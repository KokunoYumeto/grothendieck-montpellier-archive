# Second pass MPL_148_029-072, scans 059-072: apply the corrections to the first-pass page files.
# Each (old, new, n) must match exactly n times, or the script stops without writing.
import os, sys

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
SRC = BASE + "returns/MPL_148_029-072_unzipped/pages/"
OUT = BASE + "second_pass/out/MPL_148_029-072/"

R = {}
R["059"] = [
 (r'''de les oublier \inserted{\unsure{les|ces} marquages} --- même s'ils y sont bel et bien!''',
  r'''de les oublier \inserted{\unsure{ces|les} marquages} --- \deleted{même} s'ils y sont bel et bien!''', 1),
 (r'''C'est la plus cruciale, la moins tautologique''',
  r'''C'est la plus \unsure{cruciale|essentielle}, la moins tautologique''', 1),
 (r'''à classes de cardinal 2) $\sigma'$ sur $A'$.''',
  r'''à classes de cardinal 2) $\sigma'$ de \deleted{$\unsure{\{c,c'\}}$} $A'$.''', 1),
 (r'''b) Pour \deleted{$\{a,a'\}\in\unsure{A'_l}$} \unsure{toute} orbite''',
  r'''b) Pour \deleted{$\{a,a'\}\in\unsure{A'_l|A'_2}$} \unsure{toute|tout} orbite''', 1),
]
R["060"] = [
 (r'''uniformes d'un côté et d'autre)''', r'''uniformes de côté et d'autre)''', 1),
 (r'''l'\deleted{\unsure{auto}} antiisomorphisme''', r'''l'\deleted{\unsure{autre|auto}} antiisomorphisme''', 1),
]
R["061"] = [
 (r'''\inserted{$(0^\circ)$ Somme disjointe}''', r'''\inserted{$(0^\circ)$ Somme \unsure{disjointe|directe}}''', 1),
 (r'''se trouvant sur un cercle de recollement \inserted{$C_a$}, ou''',
  r'''se trouvant sur un cercle \inserted{\unsure{$C_a$}} de recollement \inserted{\unsure{les|$C_a$}}, ou''', 1),
 (r'''\textcircled{$4^\circ$} gommage du cercle de découpage''', r'''\textcircled{$4^\circ$} gommage de cercle de découpage''', 1),
 (r'''\textcircled{$5^\circ$} bouchage du trou''', r'''\textcircled{$5^\circ$} bouchage de trou''', 1),
 (r'''réversible = anodin si $r_a\unsure{\ge|>}1$.}''', r'''réversible = anodin si $r_a\ge1$.}''', 1),
 (r'''\margin{$r_a=r_{a'}\unsure{\ge|>}1$\quad réversible = anodin.}''', r'''\margin{$r_a=r_{a'}\ge1$\quad réversible = anodin.}''', 1),
]
R["062"] = [
 (r'''\inserted{avec le foncteur $\Gamma$ dans $(\mathrm{Gr.pond.rep})$ et $\chi$ dans $[\pm1]$, et}''',
  r'''\inserted{avec le foncteur $\Gamma$ dans $(\mathrm{Gr.pond.}\unsure{\mathrm{rep}|\mathrm{top}})$ et $\unsure{\chi|f}$ dans $[\pm1]$, et}''', 1),
 (r'''\margin{(on \unsure{siglera|notera} $S\mathcal T_{g\nu}^\pm$)}''',
  r'''\margin{(\unsure{on siglera|on notera|ou simplement} $S\mathcal T_{g\nu}^\pm$)}''', 1),
 ('\\inserted{bipondéré} de\n$\\deleted', '\\inserted{bipondéré} des\n$\\deleted', 1),
 (r'''pour reconstituer les opérations Notamment''', r'''pour \unsure{reconstituer|avoir toutes} les opérations Notamment''', 1),
 (r'''\inserted{\unsure{``ou''}} \unsure{structures} \unsure{$\mathcal T_{g,\infty}$})''',
  r'''\inserted{\unsure{``ou''|l'introd.}} \unsure{structures} \unsure{$\mathcal T_{g,\infty}$|$\mathcal T_{g,\nu}$})''', 1),
]
R["063"] = [
 ('(disons) $\\underline\\Gamma$, le\n$\\mathcal T_{\\mathrm{top}}^\\pm(\\underline\\Gamma)$,',
  '(disons) $\\underline\\Gamma$, le\n\\unsure{groupoïde|groupoïdes} $\\mathcal T_{\\mathrm{top}}^\\pm(\\underline\\Gamma)$,', 1),
 (r'''\deleted{à repères donné} \inserted{repères} (disons)''', r'''\deleted{à repères donné} \inserted{\unsure{repères|repéré}} (disons)''', 1),
 (r'''que pour les $\unsure{S}\mathcal T_{g,\nu}^\pm$ et $\mathcal T_{g,\nu}^\pm$ \unsure{ci-dessus}),''',
  r'''que pour les $\unsure{S}\mathcal T_{g,\nu}^\pm$ et $S\mathcal T_{g,\nu}^\pm$ \unsure{ci-dessus|connus}),''', 1),
 (r'''\deleted{\unsure{des 7 opérations}} \inserted{des cas}''', r'''\deleted{des opérations} \inserted{des cas}''', 1),
 (r'''\deleted{analogues des}''', r'''\deleted{\unsure{analogues des|catégories, ou}}''', 1),
 (r'''\inserted{structures} ``élémentaires'' à déterminer.''', r'''\inserted{structures} ``élémentaires'' \unsure{à déterminer|: diminution}.''', 1),
 (r'''\&\deleted{S}\mathcal T_{g,\nu-\nu'}''', r'''\&\deleted{S}\mathcal T_{g,\nu\unsure{-|+}\nu'}''', 1),
]
R["064"] = [
 (r'''à des $\mathcal T_{g',\nu'}$ avec $g'<g$''', r'''à des $\mathcal T_{g',\nu}$ avec $g'<g$''', 1),
 (r'''Déjà dans le cas de $S_1\mathcal T_{0,3}$''', r'''Déjà dans le cas de $S_2\mathcal T_{0,3}$''', 1),
]
R["065"] = [
 (r'''\uline{toutes les \unsure{cartes|cordes}}''', r'''\uline{toutes les \unsure{cordes|cartes}}''', 1),
 (r'''avec les modèles qu'on \unsure{désire|cherche}''', r'''avec \unsure{les modèles|le modèle} qu'on \unsure{désire|cherche}''', 1),
]
R["067"] = [
 (r'''(\mathrm{NB}\ \pi(\unsure{i|j})=\text{nb d'arêtes qui relient $j$ et $k$, $i\ne j\ne k$})''',
  r'''(\mathrm{NB}\ \pi(j)=\text{nb d'arêtes qui relient $j$ et $k$, \unsure{où} $i\ne j\ne k$})''', 1),
 (r'''\node[gray] at (.8,2.55) {$\unsure{0}$};''', r'''\draw[gray,->] (.95,2.6) arc (10:320:.16);''', 1),
 (r'''\node at (1,-3.1) {$\unsure{[1,\gamma]\amalg[1,\beta)}$};''', r'''\node at (1,-3.1) {$\unsure{[0,\alpha][1,\beta)|[1,\gamma][1,\beta)}$};''', 1),
 (r'''d'ordre $1$ éventuellement), et avec une pondération des''',
  r'''d'ordre $1$ éventuellement), et avec une \inserted{\unsure{de types $0,1$}} pondération des''', 1),
 ("\\unsure{\\gamma'_s|\\sigma'_s}", "\\gamma'_s", 2),
 ("\\unsure{\\gamma'_t|\\sigma'_t}", "\\gamma'_t", 2),
 ("\\unsure{\\gamma_s|\\sigma_s}", "\\gamma_s", 1),
 ("\\unsure{\\gamma_t|\\sigma_t}", "\\gamma_t", 1),
 ("\\unsure{\\gamma'|\\sigma'}", "\\gamma'", 8),
 ("\\unsure{\\gamma|\\sigma}", "\\gamma", 10),
 (r'''$\alpha',\beta',\gamma'$ \unsure{OK} ssi''', r'''$\alpha',\beta',\gamma'$ \unsure{OK|$\in\mathbb N$} ssi''', 1),
]
R["070"] = [
 (r'''\& \unsure{S\mathcal TS_{\mathrm{top}}^\pm} \arrow[u]\\''', r'''\& S\mathcal TS_{\mathrm{top}}^\pm \arrow[u]\\''', 1),
]
R["071"] = [
 (r'''\deleted{\unsure{Trois}} \uline{Variantes}''', r'''\deleted{\unsure{Vari|Trois}} \uline{Variantes}''', 1),
 (r'''$2^\circ)$ $\boxed{S\mathcal T_{\mathrm{top}}^\pm}$''', r'''$\unsure{2^\circ|1^\circ})$ $\boxed{S\mathcal T_{\mathrm{top}}^\pm}$''', 1),
 (r'''\arrow[r,"\unsure{\chi}","\text{(signature)}"']''', r'''\arrow[r,"\unsure{\chi|\varepsilon}","\text{(signature)}"']''', 1),
 (r'''\unsure{le|la} \deleted{noyau}''', r'''le \deleted{noyau}''', 1),
 (r'''On définit de $=$ $\unsure{\mathcal TS_{\mathrm{top}}^\pm}$''', r'''On définit de $=$ $\mathcal TS_{\mathrm{top}}^\pm$''', 1),
 (r'''groupoïde de Teichmüller bi-orienté dévissé topologique''', r'''groupoïde de Teichmüller biorienté dévissé topologique''', 1),
]
R["072"] = [
 (r'''\node at (1590,850) {$\unsure{15|25}$};''', r'''\node at (1590,850) {$15$};''', 1),
 (r'''\node at (1980,789) {$\unsure{7|4}$};''', r'''\node at (1980,789) {$7$};''', 1),
]

scans = ["%03d" % n for n in range(59, 73)]
results = {}
for s in scans:
    name = "MPL_148_029-072_148_scan%s.tex" % s
    with open(SRC + name, encoding="utf-8", newline="") as f:
        text = f.read()
    crlf = "\r\n" in text
    work = text.replace("\r\n", "\n")
    nlines0 = work.count("\n")
    for old, new, n in R.get(s, []):
        c = work.count(old)
        if c != n:
            sys.exit("scan %s: expected %d match(es), found %d for: %r" % (s, n, c, old[:90]))
        work = work.replace(old, new)
    if work.count("\n") != nlines0:
        sys.exit("scan %s: line count changed" % s)
    if crlf:
        work = work.replace("\n", "\r\n")
    results[name] = (work, len(R.get(s, [])))

os.makedirs(OUT, exist_ok=True)
for name, (work, k) in results.items():
    with open(OUT + name, "w", encoding="utf-8", newline="") as f:
        f.write(work)
    print(name, "replacement rules applied:", k)

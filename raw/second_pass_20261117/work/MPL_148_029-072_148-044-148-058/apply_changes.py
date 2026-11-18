# apply_changes.py: write the corrected page files of block 148-044..148-058 (second pass, 17 Nov 2026).
import os
SRC = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/returns/MPL_148_029-072_unzipped/pages/"
DST = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_148_029-072/"
F = "MPL_148_029-072_148_scan%03d.tex"
R = {
44: [
 (r"\unsure{tout pris en détail}, \unsure{au} point de vue" + "\n" + r"\unsure{œcuménique}",
  r"\unsure{tout pris en détail|pour \illegible{1} travaux}, \unsure{au point de vue" + "\n" + r"œcuménique|\illegible{1} ultérieurs}"),
 (r"il semble que c'est le cas $\mathcal T^\pm$ qui offre" + "\n" + r"le plus \unsure{utilité};",
  r"il semble que \unsure{c'est le cas} $\mathcal T^\pm$ qui \unsure{offre|soit}" + "\n" + r"le plus \unsure{utilisé};"),
 (r"\unsure{aura} donc ici", r"\unsure{mérite} donc ici"),
 (r"et le \unsure{groupe} orienté s'appelle $\mathcal T^+$.}",
  r"et le \unsure{groupoïde|groupe} orienté \unsure{s'appelle|s'appellera} $\mathcal T^+$.}"),
 (r"\margin{\unsure{Ceci n'a un sens} \unsure{qu'}à des surfaces connexes!}",
  r"\margin{\unsure{Canulé}, \unsure{si on ne se borne|n'a un sens} à des surfaces connexes!}"),
],
45: [(r"$\unsure{g|\gamma}$", r"$\gamma$")],
46: [
 (r"\margin{$X,\unsure{\partial X},\Sigma,S$}", r"\margin{$X,\deleted{\unsure{\partial X}},\Sigma,S$}"),
 (r"On peut considérer que $R$ rigidifie $\widetilde\Sigma$ :" + "\n" + r"que $R$ ``découpe'' $\widetilde\Sigma$.}",
  r"On peut considérer que $R$ rigidifie, \illegible{1} $\widetilde\Sigma$\ldots{}" + "\n" + r"\unsure{par|que} $R$ ``\unsure{découpage|découpe}''}"),
 (r"\text{\inserted{ou \uline{rigidifiés}} (topologiques orientés))}",
  r"\text{\inserted{(ou \uline{rigidifiés})} (topologiques orientés))}"),
 (r"\mathcal TD_{\mathrm{top}}\quad\text{et}\quad\mathcal T^\pm D_{\mathrm{top}}&",
  r"\mathcal T_{\deleted{\unsure{\mathrm{top}}}}D_{\mathrm{top}}\quad\text{et}\quad\mathcal TD^\pm_{\mathrm{top}}&"),
 (r"\pi_0((S_*\mathcal TD)^\pm_{\mathrm{top}})$.", r"\pi_0(S_*\mathcal TD^\pm_{\mathrm{top}})$."),
],
47: [
 (r"\inserted{(``\unsure{non attachées}'' aux \unsure{2})}", r"\inserted{(``sommets'', ``\unsure{trous|arcs}'')}"),
 (r"$o:\vec A\longrightarrow S$ appel. ``origine''.", r"$o:\vec A\longrightarrow S$ appl. ``origine''."),
 (r'\arrow[r,"\unsure{r\rho_2|\rho}"]', r'\arrow[r,"r\deleted{\unsure{\rho_2}}"]'),
 (r"(i.e. $\in S$) et les \unsure{trous}" + "\n", r"(i.e. $\in S$) et ``\unsure{libres}''" + "\n"),
],
48: [
 (r"$C\deleted{\in A}\inserted{\in\pi_0(\widetilde\Sigma)}$, et où",
  r"$C$ \deleted{\unsure{est un}}\inserted{$\in\pi_0(\widetilde\Sigma)$}, et où"),
 (r"alors $\omega$" + "\n" + r"est l'orientation induite", r"alors $\omega$" + "\n" + r"soit l'orientation induite"),
],
49: [
 (r"plus généralement \unsure{donner} le \uline{genre total} est", r"plus généralement le \uline{genre total} est"),
 (r"\unsure{indice de connexion} du graphe" + "\n" + r"$=\deleted{\unsure{\chi}}\unsure{\mathrm{rg}\,H^1(\Gamma)}$.}",
  r"\unsure{indice de connexion|ordre de connexion} du graphe" + "\n" + r"$=\deleted{\unsure{\chi}}\mathrm{rg}\,H^1(\Gamma)$.}"),
 (r'A\ (\simeq\vec A=\vec A^\sigma)\arrow[r,"\unsure{r|\rho}"]', r'A\ (\simeq\vec A=\vec A^\sigma)\arrow[r,"r"]'),
 (r"correspond à faire $\rho=0$,", r"correspond à \unsure{choisir|faire} $\rho=0$,"),
 (r"A=\unsure{A_0|A_\ell}\arrow[d]", r"A=A_0\arrow[d]"),
 (r"est \deleted{\unsure{homéomorphisme}}\inserted{caractérisé}" + "\n" + r"par la donnée des deux entiers",
  r"est \deleted{\unsure{Déterminé}}\inserted{caractérisé}" + "\n" + r"par \deleted{\unsure{le genre}} la donnée des deux entiers"),
],
50: [
 (r"si nous désignons l'\unsure{ens} des", r"si $\omega(a)$ désigne l'\unsure{un|ens} des"),
 (r"et de donnée d'une famille de torseurs", r"et \unsure{la|à la} donnée d'une famille de torseurs"),
 (r"$\mathbb Z/r(a)\mathbb Z\mathbin{\wedge}_{\{\pm1\}}\omega(a)$.", r"$\mathbb Z/r(a)\mathbb Z\mathbin{\wedge}^{\omega(a)}_{\{\pm1\}}$."),
 (r"\deleted{et $p$ \unsure{déduit de} \unsure{$(\widetilde\Sigma_a)$} \unsure{sur} $R_a$.}",
  r"\deleted{et $p$ déduit de l'ordre circulaire \unsure{dans|sur} les $R_a$.}"),
 (r"$r(\unsure{\omega|a})=1$ ou $r(\unsure{\omega|a})=2$", r"$r(\omega)=1$ ou $r(\omega)=2$"),
],
51: [(r"définissant une orientation du contour correspondant.", r"définissant une orientation \unsure{du contour|des contours} correspondant.")],
52: [],
53: [
 (r"alors on aura par \unsure{cela} aussi", r"alors on \unsure{aura|devra} \unsure{par|pouvoir} donc aussi"),
 (r"\unsure{sauf si|si} pour une composante", r"si pour une composante"),
 (r"Il faudrait \unsure{distinguer les deux cas}, pour distinguer ces", r"Il faudrait \unsure{séparer} les deux cas, pour distinguer ces"),
 (r"\unsure{essentielles|anodines}", r"essentielles"),
],
54: [
 (r"$\pi_0(\unsure{\Sigma'|\Sigma})=A_0$", r"$\pi_0(\Sigma')=A_0$"),
 (r"Au niveau des \deleted{repères} \inserted{sommets},", r"Au niveau des sommets \inserted{(repères)},"),
 (r"$\in\unsure{A'_{0a}|A'_0}$.", r"$\in A'_0$."),
],
55: [(r"qui est à la fois ouverte et fermée", r"qui soit à la fois ouverte et fermée")],
56: [
 (r"\deleted{\uline{\unsure{raffinement} de}}", r"\deleted{\uline{affaiblissement de}}"),
 (r"(\uline{NB} \unsure{elle est réunion|elles se déduisent} des cercles eff. marqués, et non des intervalles ouverts)",
  r"(\uline{NB} \unsure{elle est réunion|elles se déduisent|elles sont les intersections} des cercles eff. marqués, et \unsure{non|sont} des intervalles ouverts)"),
],
57: [
 (r"par une opération de contraction des groupes", r"par une opération de \unsure{contraction|restriction} des groupes"),
 (r"$\mathbb Z_a/\unsure{r''(a)|r'(a)}$, où $\unsure{r''(a)|r'(a)}$", r"$\mathbb Z_a/r''(a)$, où $r''(a)$"),
],
58: [],
}
total = 0
for n, reps in R.items():
    with open(SRC + F % n, encoding="utf-8") as fh:
        t = fh.read()
    for old, new in reps:
        c = t.count(old)
        assert c == 1, ("scan %d: %d matches for %r" % (n, c, old[:60]))
        t = t.replace(old, new)
        total += 1
    with open(DST + F % n, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)
    print(n, len(reps), "changes written")
print("total replacements", total)

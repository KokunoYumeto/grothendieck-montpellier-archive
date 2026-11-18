"""Second pass MPL_147_003-047, scans 018-032: apply the corrections to the first-pass page files.

Reads returns/MPL_147_003-047_unzipped/pages/, writes second_pass/out/MPL_147_003-047/.
Every replacement must match exactly once; otherwise nothing is written.
"""
import os, re, sys

ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = ROOT + "/returns/MPL_147_003-047_unzipped/pages/MPL_147_003-047_scan%03d.tex"
DST = ROOT + "/second_pass/out/MPL_147_003-047/MPL_147_003-047_scan%03d.tex"

R = {
18: [
 (r"des courbes standard $G$-épinglées. Pour tt $\alpha\in S$",
  r"des courbes standart $G$-épinglées. Pour $\forall\ \alpha\in S$"),
],
19: [
 (r"La donnée d'une courbe \unsure{standard|standart} $G$ épinglée",
  r"La donnée d'une courbe standart $G$ épinglée"),
 (r"$Y_\alpha$ sur $\mathcal S$, de genre relatif",
  r"$Y_\alpha$ \unsure{sur} $\mathcal S$, de genre relatif"),
 (r"désigne le groupoïde des courbes \unsure{standard|standart} $G$-épinglées",
  r"désigne le groupoïde des courbes standart $G$-épinglées"),
],
20: [
 (r"qu'il en soit de $\unsure{=|\overline m}$ des",
  r"qu'il en soit de $=$ des"),
 (r"\mathcal S\longrightarrow\mathcal M_{g_\alpha,\widehat I_\alpha}(\mathcal S),",
  r"\mathcal S\;\text{---}\;\mathcal M_{g_\alpha,\widehat I_\alpha}(\mathcal S),"),
],
21: [
 (r"correspondante, \deleted{que} de sorte",
  r"correspondante, \deleted{\unsure{qui|que}} de sorte"),
 (r"des courbes \unsure{standard|standart} relatives",
  r"des courbes standart relatives"),
],
22: [
 (r"Il en est donc de $\unsure{=|\overline m}$ de",
  r"Il en est donc de $=$ de"),
 (r"un \deleted{courbe} schéma relatif",
  r"une \deleted{courbe} schéma relatif"),
],
23: [
 (r"sur $\unsure{k(s)|\kappa(s)}$",
  r"sur $k(s)$"),
 (r"($\unsure{=|\overline m}$ sur une base",
  r"($=$ sur une base"),
],
24: [
 (r"(24)\qquad\mathcal S\longmapsto",
  r"(\unsure{24})\qquad\mathcal S\longmapsto"),
 (r"le vraiment \unsure{mirifique} théorème",
  r"le vraiment mirifique théorème"),
 (r"\uline{Théorème de Mumford-Deligne} : Le",
  r"\uline{Théorème} de \uline{Mumford-Deligne} : Le"),
 (r"\inserted{D'autre part $\mathcal M^!_{g,\nu}$ est un}",
  r"\inserted{D'autre part $\unsure{\mathcal M^!_{g,\nu}|\mathcal M'_{g,\nu}}$ est un}"),
],
25: [
 (r"\deleted{\unsure{la}} \unsure{connexité} en car.",
  r"\deleted{\unsure{la}} connexité en car."),
 (r"les courbes \unsure{standard|standart} de type $[G]$",
  r"les courbes standart de type $[G]$"),
],
26: [
 (r"de type numérique $g,\nu)$)",
  r"de type numérique $(g,\nu)$)"),
 (r"une réunion finie de $\mathcal M_{[G']}$",
  r"une réunion finie de\deleted{\unsure{s}} $\mathcal M_{[G']}$"),
],
27: [
 (r"dans l'ens des classes d'iso.",
  r"dans l'ens des Classes d'iso."),
 (r"{\unsure{\widetilde\mu_\alpha}}",
  r"{\widetilde\mu_\alpha}"),
],
28: [
 (r"(\unsure{28})\qquad", r"(28)\qquad"),
 (r"(\unsure{29})\qquad", r"(29)\qquad"),
 (r"des courbes \unsure{standard|standart} de type $G$",
  r"des courbes standart de type $G$"),
 (r"\mu(G)&=\sum_{\alpha\in S}(3g_\alpha-1)+\widehat\nu_\alpha)=",
  r"\mu(G)&=\sum_{\alpha\in S}(3(g_\alpha-1)+\widehat\nu_\alpha)="),
],
29: [
 (r"Du pt de vue \unsure{structure} de graphe associé au type numérique $g,\nu)$, c'est",
  r"Du pt de vue structure de graphe associé au type numérique $(g,\nu)$), c'est"),
 (r"nulle, \unsure{ou} d'une codimension",
  r"nulle, \unsure{ie|ou} d'une codimension"),
],
30: [
 (r"courbe \deleted{\unsure{standard|standart}\inserted{MD}} sur",
  r"courbe \deleted{standart}\inserted{MD} sur"),
 (r"courbe \deleted{\unsure{standard|standart} sur $\mathcal S$} MD sur",
  r"courbe \deleted{standart sur $\mathcal S$} MD sur"),
],
31: [
 (r'"{\unsure{\wr|=}\ \mathrm{déf}}"', r'"{\wr\ \mathrm{déf}}"'),
 (r'"{\unsure{\wr|=}}"', r'"{\wr}"'),
 (r"fermée cette \unsure{fois|fois-ci},", r"fermée cette fois-ci,"),
 (r"Ainsi se trouve \unsure{explicité|explicitée} l'adhérence",
  r"Ainsi se trouve explicité l'adhérence"),
 (r"En $\unsure{=|\overline m}$ temps", r"En $=$ temps"),
],
32: [
 (r"\uline{Spécialisation \deleted{et générisation} de MD-graphes.}",
  r"\uline{Spécialisation \deleted{et générisation} \unsure{de|des} MD-graphes.}"),
 (r"&\deleted{\unsure{I_{(\alpha)}\amalg\widetilde A_{(\alpha)}\to S_{(\alpha)}\xrightarrow{g_\alpha}\mathbb N}}\\",
  r"&\deleted{\unsure{\widehat I_{(\alpha)}\amalg\widetilde A_{(\alpha)}\to S_{(\alpha)}}\xrightarrow{\unsure{\sigma_\alpha|g_\alpha}}\mathbb N}\\"),
 (r"\xrightarrow{\unsure{g_\alpha|\sigma_\alpha}}\mathbb N})",
  r"\xrightarrow{\unsure{\sigma_\alpha|g_\alpha}}\mathbb N})"),
],
}

out = {}
nrep = 0
for scan in range(18, 33):
    with open(SRC % scan, encoding="utf-8") as f:
        text = f.read()
    for old, new in R.get(scan, []):
        c = text.count(old)
        if c != 1:
            sys.exit("scan %03d: %d matches for %r" % (scan, c, old))
        text = text.replace(old, new)
        nrep += 1
    bare = re.sub(r"\\[{}]", "", text)  # escaped braces such as \left\{ do not count
    if bare.count("{") != bare.count("}"):
        sys.exit("scan %03d: unbalanced braces" % scan)
    out[scan] = text

for scan, text in out.items():
    with open(DST % scan, "w", encoding="utf-8", newline="") as f:
        f.write(text)

print("replacements:", nrep)
tot = 0
for scan, text in out.items():
    u = len(re.findall(r"\\unsure\{", text)); i = len(re.findall(r"\\illegible\{", text))
    tot += u + i
    print("scan %03d: unsure %d, illegible %d" % (scan, u, i))
print("total marked doubts:", tot)

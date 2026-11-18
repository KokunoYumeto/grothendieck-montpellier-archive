# Apply the second-pass corrections of block MPL_144_168-184+148_001-028_148-016-148-028
# to the first-pass page files and write the corrected files to the output folder.
# Each replacement must occur exactly the stated number of times, or the script stops.
import os, sys

BASE = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + r"/returns/MPL_144_168-184+148_001-028_unzipped/pages"
OUT = BASE + r"/second_pass/out/MPL_144_168-184+148_001-028"
NAME = "MPL_144_168-184+148_001-028_148_scan%03d.tex"

R = {
16: [],
17: [
 (r"M_{\unsure{0\,4|0,4}}", r"M_{0\,4}", 1),
],
18: [
 (r"\margin{\unsure{voir aussi} cf verso (\unsure{barycentres de} \unsure{triangulation})}",
  r"\margin{mieux cf verso (subdivision barycentrique)}", 1),
 (r"s_1&=12+4.\unsure{8|9}=48", r"s_1&=12+4.\unsure{9|8}=48", 1),
 (r"\margin{ça fait $2^4-1=15$ \unsure{possibilités} \unsure{d'inversion} \unsure{des faces choisies} \unsure{en} \unsure{des} \unsure{bords} !}",
  r"\margin{ça fait $2^4-1=15$ \unsure{possibilités|positions} \unsure{d'inversion|limites} \unsure{des faces choisies|invariantes possibles} \unsure{en des bords|\illegible{3} de vue} !}", 1),
 (r"$\bullet$ $3$ structures carrées, sur $I$ (ou $J$)",
  r"$\bullet$ $3$ structures carrées sur $I$ (ou $J$)", 1),
 (r"$2$ structures \unsure{tétraèdres|tétraédriques} $=$ \unsure{orientation des faces}",
  r"$2$ structures \unsure{tétraédrales|tétraédriques|tétraèdres} $=$ \unsure{orientation|orientations} des faces", 1),
 (r"\unsure{appariées|opposées} (maillot ceinturé) (carrée $+$ codiagonale \unsure{$J$} $\simeq$ repère de $J$)",
  r"\unsure{opposées|appariées} (maillot ceinturé) (carrée $+$ codiagonale) $\simeq$ repère de $J$)", 1),
 (r"$\bullet$ $6$ structures pantaloniques de \unsure{quasi-gss} (\unsure{quart de tore})",
  r"$\bullet$ $6$ structures pantaloniques de \unsure{quasi-gois|quasi-gss|genre gois} (quart de \unsure{sorte|tore|tour})", 1),
 (r"\margin{$\omega_I=\unsure{{}^{6J}\omega_J}$}",
  r"\margin{$\omega_I\unsure{={}^{6J}\omega_J|\overset{\sim}{=}\omega_J}$}", 1),
 (r"on voit à la fois la \unsure{p.r.q.} du tétraèdre : la configuration-carré, et : la configuration bien \unsure{pantalonnée} du \unsure{quasi-gss}.}",
  r"on voit à la fois la \unsure{p.r.q.|proj.} du tétraèdre : la configuration-carré, et : la configuration bien \unsure{pantalonique|pantalonnée} du \unsure{quasi-gois|quasi-gss|genre gois}.}", 1),
 (r"a) ``\unsure{quart de} twist''", r"a) ``quart de twist''", 1),
 (r"(ici encore deux pts de vue possibles)", r"(ici encore, deux pts de vue possibles)", 1),
],
19: [
 (r"Pour avoir le passage \unsure{aux autres} structures pantaloniques, il faut introduire la \deleted{\unsure{double}}\unsure{subdivision} barycentrique",
  r"Pour avoir le passage \unsure{aux|à} \unsure{aux|deux|autres} structures pantaloniques, il faut introduire la \deleted{\unsure{double}}subdivision barycentrique", 1),
 (r"dans les deux cas \inserted{``\unsure{spéciaux}''} non dégénérés (carré, tétraèdre) les frontières adjacentes sont \deleted{\unsure{toutes}} ``contenues",
  r"dans les deux cas \inserted{``spéciaux''} non \unsure{digons} (carré, tétraèdre) les positions adjacentes sont toutes ``contenues", 1),
 (r"cette carte \inserted{\unsure{commune}}", r"cette carte \inserted{\unsure{commune|nouveau}}", 1),
 (r"des trois \unsure{coins|cas} ``carrés'' associés", r"des trois \unsure{cas|cartes|coins} ``carrés'' associés", 1),
],
20: [
 (r"I&=I_Q=\coprod_{d\in D_Q}d", r"I&=\unsure{S_Q|I_Q}=\coprod_{d\in D_Q}d", 1),
 ("\\[\n\\underbrace{",
  "\\margin{\\unsure{tétraèdre $+$ b} \\illegible{2} \\unsure{(carré $+$}}\n\n\\[\n\\underbrace{", 1),
 (r"\margin{$\unsure{\omega_I\times J}$}", r"\margin{$\unsure{\omega_I\times J|\deleted{\omega_I\times J}}$}", 1),
 (r"\unsure{\mathfrak S_I}\arrow[r]&\unsure{\mathfrak S_J}", r"\mathfrak S_I\arrow[r]&\mathfrak S_J", 1),
 ("1\\arrow[r]&\n\\unsure{\\Gamma|\\mathcal T}_{0,4}^{!}", "\\unsure{1}\\arrow[r]&\n\\mathcal T_{0,4}^{!}", 1),
 (r"\unsure{\Gamma|\mathcal T}", r"\mathcal T", 4),
 (r"\unsure{\mathfrak S_4}", r"\mathfrak S_4", 2),
 (r"\unsure{\mathfrak S_3}", r"\mathfrak S_3", 2),
 (r"\unsure{\widetilde{\mathfrak S}_3}", r"\widetilde{\mathfrak S}_3", 2),
 (r"\Pi_{0,3}\arrow[r,very thick]", r"\Pi_{0,3}\arrow[r,Rightarrow]", 1),
 (r"\Pi_{0,\unsure{3|5}}^{\unsure{2}}\arrow[r,very thick]",
  r"\Pi_{0,\unsure{3|5}}\unsure{^{2}|(2,\mathbb Z)}\arrow[r,Rightarrow]", 1),
],
21: [
 ("\\scanpage{21}\n", "\\scanpage{21}\n\n\\scalebox{-1}[1]{\\texttt{\\unsure{//* GUTS 0055 I}}}\n", 1),
 (r"\unsure{\mathtt{55|35}}", r"\mathtt{55}", 6),
],
22: [
 (r"\text{NPL PLN1A}", r"\text{NPL PLN1.A}", 1),
],
23: [
 (r"\deleted{\unsure{4|6}\text{ hexagones}}", r"\deleted{\deleted{6}\inserted{4}\text{ hexagones}}", 1),
 (r"\unsure{A_4|\mathfrak S_4}", r"\unsure{\mathfrak A_4|A_4|\mathfrak S_4|G_4}", 1),
 (r"\unsure{\mu_6|\mathbb H_6}", r"\mu_6", 1),
 (r"\unsure{\mu_4|\mathbb H_4}", r"\mu_4", 1),
 (r"$4$ carrés", r"$\deleted{2}\inserted{4}$ carrés", 1),
 (r"E_{\varepsilon+}", r"E_{\varepsilon,+}", 1),
],
24: [
 (r"on fait \(3\times2=6\) courbes \unsure{elliptiques} de type",
  r"on fait \(3\times2=6\) \unsure{courbes|cartes} \unsure{elliptiques} de type", 1),
 (r"\unsure{on} trouve \(\unsure{17|14}\) \unsure{points|ponts} \unsure{or|ou} canoniques",
  r"\unsure{on} \unsure{peut} \unsure{trouver|trouve} \(\unsure{17|14}\) \unsure{cartes|points|ponts} \unsure{on|ou|or} canoniques", 1),
 (r"dont deux tétraèdres,", r"dont deux \unsure{tétraédrales|tétraèdres},", 1),
],
25: [
 (r"\unsure{A|\Delta}&\text{triangle}", r"A&\text{triangle}", 1),
 (r"\vec T&\text{tétraèdre orienté}", r"\unsure{\vec I|\vec T}&\text{tétraèdre orienté}", 1),
 (r"\unsure{\bar Q|\bar E}&", r"\unsure{\bar Q|\bar E|\vec{\mathbb Q}}&", 1),
 ("\\figure{\\begin{tikzpicture}[x=.75cm,y=.75cm,line cap=round]",
  "% the two dashed lines below stand level with (0,5) and (1,2) of the right-hand list: blank name slots (@536)\n\\figure{\\begin{tikzpicture}[x=.75cm,y=.75cm,line cap=round]", 1),
],
26: [
 (r"\margin{\(\unsure{\mathrm{or}^{t}}\)}", r"\margin{\unsure{\(\mathrm{or}^{t}\)|orient.}}", 1),
 (r"\margin{\(\deleted{\unsure{\mathbf Z}}\unsure{n-}\)}",
  r"\margin{\unsure{\(\deleted{\mathbf Z}n-\)|\(\deleted{\mathbf Z/n}\)}}", 1),
 (r"\node at (50,-47) {\(\unsure{\circlearrowleft|J}\)};", r"\node at (50,-47) {\(\circlearrowleft\)};", 1),
 (r"\deleted{\unsure{cartes sphériques} \unsure{d}}", r"\deleted{\unsure{variétés} algébriques d}", 1),
 (r"\(\mathbb R\)-cartes \unsure{rigidifiées}", r"\(\mathbb R\)-\unsure{courbes|cartes} algébriques", 1),
 (r"\quad \unsure{ses} pts fixes}", r"\quad \unsure{ses|sans} pts fixes}", 1),
],
27: [
 (r"16\ \unsure{\text{côtés}|\text{arêtes}}", r"16\text{ arêtes}", 1),
 (r"&\deleted{\unsure{1|4}\times4\text{ d'ordre}}\ 4",
  r"&\deleted{\unsure{\text{dont }4|1\times4|4\times4}\text{ d'ordre}}\ 4", 1),
],
28: [
 (r"\node at (18,243) {\(\unsure{2'|1'}\)};", r"\node at (18,243) {\(2'\)};", 1),
 (r"\node at (148,278) {\(\unsure{6|b}\)};", r"\node at (148,278) {\(6\)};", 1),
],
}

def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for scan in sorted(R):
        src = os.path.join(SRC, NAME % scan)
        with open(src, encoding="utf-8", newline="") as f:
            t = f.read()
        crlf = "\r\n" in t
        if crlf:
            t = t.replace("\r\n", "\n")
        for old, new, n in R[scan]:
            c = t.count(old)
            if c != n:
                sys.exit("scan %03d: expected %d of %r, found %d" % (scan, n, old[:70], c))
            t = t.replace(old, new)
            total += n
        if crlf:
            t = t.replace("\n", "\r\n")
        dst = os.path.join(OUT, NAME % scan)
        with open(dst, "w", encoding="utf-8", newline="") as f:
            f.write(t)
        print("scan %03d: %d replacement rules applied -> %s" % (scan, len(R[scan]), os.path.basename(dst)))
    print("total replacements:", total)

main()

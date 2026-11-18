# Second pass, block MPL_150_044-084_150-044-150-057 (cote 150, scans 44-57).
# Applies the image-checked corrections to the first-pass page files and writes the corrected files once.
# Every replacement must match exactly once in its file, or the script stops without writing anything.
import os, re, sys

BASE = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + r"/returns/MPL_150_044-084_unzipped/pages"
OUT = BASE + r"/second_pass/out/MPL_150_044-084"

R = {}
R[44] = [
 (r"\unsure{précisément}, \unsure{on a} de plus une application croiss. et continue",
  r"précisément, on a de plus une application croiss. et continue"),
 (r"\deleted{\unsure{immersement}}", r"\deleted{\unsure{immersion|immersement}}"),
 (r"(25\unsure{$^*$|$^\circ$})", r"(25$^*$)"),
 (r"\deleted{au} dessous de $i$", r"\unsure{\deleted{au}|au} \unsure{dessus|dessous} de $i$"),
 (r"\margin{\unsure{via} $\Sigma_*^{\leq 2}\longrightarrow I^{\leq 2}$ \unsure{injectif}}",
  r"\margin{\unsure{i.e.|via} $\Sigma_*^{\leq \unsure{z|2}}\longrightarrow I^{\leq \unsure{j|2}}$ \unsure{injectif}}"),
 (r"\deleted{On suppose de plus que pour $z\in$ $\unsure{i}\leq j\leq k$, $\unsure{\Sigma_i}$}",
  r"\unsure{On|Car} \deleted{suppose de plus que pour $z\in$} \deleted{$\unsure{i}\leq j\leq k$,}"),
 (r"""(27)\qquad \uline{\Sigma(n)}=\text{ens des drapeaux stricts de longueur }n\text{ de }\Sigma
\]
ou""",
  r"""(27)\qquad \Sigma(n)=\text{ens des drapeaux stricts de longueur }n\text{ de }\Sigma
\]
\deleted{$\Sigma_i$}
ou"""),
]
R[45] = [
 (r"(\inserted{\unsure{qui par $1^\circ$}} induit une application",
  r"(\inserted{qui par \unsure{\textcircled{a}|$1^\circ$}} induit une application"),
 (r"\Sigma_{*\unsure{\leq}z}\unsure{\hookrightarrow|\longleftrightarrow} I_{\leq k}",
  r"\Sigma_{*\leq z}\hookrightarrow I_{\leq k}"),
 (r"(29)\qquad (\Sigma_*)_{\leq z}\unsure{\hookrightarrow|\longleftrightarrow} I_{\leq k}",
  r"(29)\qquad (\Sigma_*)_{\leq z}\hookrightarrow I_{\leq k}"),
 (r"(grâce : \unsure{(30)}\inserted{et 28,})", r"(grâce à \unsure{(30)}\inserted{et 28,})"),
 (r"$d=(i_0,\!\ldots\!i_n,k)$", r"$d=(i_0,--i_n,k)$"),
 (r"$\Sigma_{i_0k},\Sigma_{i_1k}\ \ldots\ \Sigma_{i_n,k}$", r"$\Sigma_{i_0k},\Sigma_{i_1k}-\Sigma_{i_n,k}$"),
 (r"(i.e. but pour $d'\supsetneqq d$, et \unsure{$l_i$} bord.\inserted{$d'=d\cup\{i\}$} \unsure{qui sont} toutes pour un drapeau de $d'$) dans $\Sigma_d$ \unsure{lisses}.}",
  r"(i.e. but pour $d'\supsetneqq d$, et $d$ cofinal dans $d'$) \unsure{ce qui} \unsure{les} bord.\inserted{$d'=d\cup\{i\}$} \unsure{qui sont} toutes pour un drapeau de $d'$ dans $\Sigma_d$ \unsure{lisses}.}"),
]
R[46] = [
 (r"dans le cas des strates \unsure{non-singulières} on suppose",
  r"dans le cas des strates \deleted{\illegible{1}} non-singulières on suppose"),
 (r"(\deleted{$j<i$} \unsure{tq-précédemment})", r"(\deleted{$j<i$} \unsure{tq-précédemment|toujours distinctes})"),
 (r"définissent (\inserted{\unsure{en dépit la cond$^{\mathrm n}$ d')} }) une stratification cylindrique",
  r"\unsure{forment|définissent} (\inserted{\unsure{les} \illegible{1} \unsure{de} codim $1$ \unsure{d'}}) une stratification cylindrique"),
 (r"$\Sigma_d=\Sigma_{i_1\ldots i_n}$", r"$\Sigma_d=\Sigma_{i_1,--i_n}$"),
 (r"forment une stratification cylindrique du bord \deleted{de $\dot\Sigma_d$} de $\Sigma_*$.",
  r"forment une stratification cylindrique du bord \deleted{de} $\dot\Sigma_d$ de $\Sigma_d$."),
 (r"Dans le cas d'équisingularité non-singulière, on suppose", r"Dans le cas équisingulier-non-singulier, on suppose"),
]
R[47] = [
 (r"\inserted{(top.\unsure{C$^\infty$})}", r"\inserted{(\unsure{top.|hyp.}\unsure{C$^\infty$|C.I})}"),
 (r"(pour que $\Sigma_{d''}\longrightarrow\Sigma_{d'}$ soit \unsure{fibrant})",
  r"(pour que $\Sigma_{d''}\longrightarrow\unsure{\Sigma_{d'}|\Sigma_d}$ soit \unsure{fibrant})"),
 (r"\deleted{\unsure{alors $d''$ est de la forme}} $d'=d\coprod d'_0$",
  r"\deleted{\unsure{alors $d''$ est de la forme}} d'où $d'=d\coprod d'_0$"),
 (r"$d'_0=(i_{p+1},i_{p+2}\ldots i_n)$", r"$d'_0=(i_{p+1},i_{p+2}--i_n)$"),
 (r"contenant \deleted{\unsure{les}} strictement", r"contenant \deleted{\unsure{$d_0$|les}} strictement"),
 (r"\coprod I_{i_{p+1}<\cdot<i_{p+2}}\coprod\ldots\coprod", r"\coprod I_{i_{p+1}<\cdot<i_{p+2}}\coprod--\coprod"),
]
R[48] = [
 (r"\deleted{\unsure{pour}} la suite $i_p\ i_{p+1}\ldots i_n$", r"\deleted{\unsure{pour|$i_p$}} la suite $i_p\ i_{p+1}--i_n$"),
 (r"est \unsure{saturée}, i.e.", r"est \unsure{stricte|saturée}, i.e."),
 (r"le complémentaire de l'image, où l'on a une des inégalités strictes $i<j$.",
  r"le complémentaire de l'image, i.e. l'ens \unsure{où} une des inégalités strictes $i<j$."),
 (r"$i_0<i_1\ldots<i_n$", r"$i_0<i_1--<i_n$"),
 (r"\deleted{\unsure{sont forment|forment}} un espace \inserted{pré}\unsure{semi}-simplicial",
  r"\deleted{\unsure{sont}} \unsure{forment} un espace \inserted{pré}\deleted{semi}-simplicial"),
]
R[49] = [
 (r"où les $\varphi_0,\varphi_1,\ldots\varphi_n$ sont bordantes.", r"où les $\varphi_0,\varphi_1,\ \varphi_{n-1}$ sont bordantes."),
 (r"\margin{Plus précisément nous voulons que pour", r"\margin{Plus précisément \unsure{nous voulons|on veut} que pour"),
 (r"images locales des $\Sigma^{<}(1)$ en $z_\alpha$, que ces germes", r"images locales des $\Sigma^{<}(1)$ en les $z_\alpha$, que ces germes"),
]
R[50] = [
 (r"\inserted{dans $\Sigma^{<}(i_n)\simeq\Sigma(0)$}", r"\inserted{dans $\Sigma^{<}(\{i_n\})\simeq\Sigma(0)$}"),
 (r"qu'il satisfait la même condition de transversalité.", r"qu'il satisfait la $=$ condition de transversalité."),
]
R[51] = [
 (r"\inserted{$\Sigma^{<}(1)\xrightarrow{\mathrm{but}}\Sigma^{<}(0)$ a comme image son bord.}",
  r"\inserted{$\Sigma^{<}(1)\overset{\mathrm{but}}{\hookrightarrow}\Sigma^{<}(0)$ a comme image son bord.}"),
 (r"\unsure{déterminer le bord}, de $=$ dim", r"\unsure{déterminer le bord|de dimension $<$ bord}, de $=$ dim"),
 (r"$I=\unsure{\{1,2,3\}|\{0,1,2\}}$", r"$I=\unsure{\{0,1,2\}|\{1,2,3\}}$"),
 (r"$\{0,2\}\longleftrightarrow\{0,1,2\}$", r"$\{0,2\}\hookrightarrow\{0,1,2\}$"),
]
R[52] = [
 (r"images par $b$ des germes", r"images par $\uline{b}$ des germes"),
 (r"\deleted{$1\leq d\leq n$, \unsure{les}} $1\leq d\leq n$, considérons",
  r"\deleted{$1\leq d\leq n$, \unsure{les}} $1<d\leq n$, considérons"),
 (r"\{0,1,\ldots,d\}", r"\{0,1,--,d\}"),
 (r"([0,\ldots,n-1])", r"([0,--,n-1])"),
 (r"$\Delta_d=\{0,\ldots d\}$", r"$\Delta_d=\{0,--d\}$"),
]
R[53] = [
 (r"$\Delta_n=\{0,\ldots,n\}$", r"$\Delta_n=\{0,-,n\}$"),
 (r"dont la donnée équivaut \inserted{\unsure{qui est}} à celle des $\Sigma^{<}(n)$ avec les appl. simpliciales",
  r"dont la donnée équivaut à celle des $\Sigma^{<}(n)$ avec les \deleted{\illegible{2}} appl. simpliciales"),
]
R[54] = [
 (r"\inserted{\unsure{qu'on}} identifiés", r"\inserted{\unsure{germes|qu'on}} identifiés"),
 (r"\deleted{grâce à la structure", r"\deleted{(grâce à la structure"),
 (r"\inserted{\unsure{en un même}} $x$", r"\inserted{\unsure{en un}} \unsure{$=$|$\ni$} $x$"),
 (r"peut reconstituer les espaces de drapeaux", r"\unsure{peut|pour} reconstituer les espaces de drapeaux"),
]
R[55] = [
 (r"\inserted{en un pt,}", r"\inserted{en un $=$ \unsure{point|pt},}"),
 (r"\inserted{\unsure{uniquement}}", r"\inserted{\unsure{uniquement|suffit}}"),
 (r"i.e. une section de $\Gamma_0\times_\Sigma\Gamma_0\setminus\text{diag}$ au dessus",
  r"i.e. une section de $\Gamma_0\times_\Sigma\Gamma_0\setminus\text{diag}$ \unsure{\deleted{au}|au} dessus"),
]
R[56] = [
 (r"\unsure{bousillé}", r"\unsure{bousillé|bafouillé}"),
 (r"avec leur interprétation semi-simpliciale", r"avec \unsure{\deleted{leur}|leur} interprétation semi-simpliciale"),
 (r"\xrightarrow{b:\operatorname{pr}_2}", r"\xrightarrow{\uline{b}\unsure{=|:}\operatorname{pr}_2}"),
]
R[57] = [
 (r"$\mathfrak P_d(\{1,\ldots,N(x)\})$", r"$\mathfrak P_d(\{1,--,N(x)\})$"),
 (r"(x_0<\cdots<x_d)", r"(x_0<--<x_d)"),
 (r"(par $\Sigma^{<}(1)\xrightarrow{b}\Sigma$)", r"(par $\Sigma^{<}(1)\overset{b}{\unsure{-|\longrightarrow}}\Sigma$)"),
 (r"\operatorname{card}(\Sigma_{<x})", r"\operatorname{card}(\Sigma_{\unsure{<|\leq}x})"),
]

def count_doubts(t):
    return len(re.findall(r"\\unsure\{", t)) + len(re.findall(r"\\illegible\{", t))

def main():
    results = {}
    for scan in range(44, 58):
        name = "MPL_150_044-084_150_scan%03d.tex" % scan
        raw = open(os.path.join(SRC, name), "rb").read().decode("utf-8")
        crlf = "\r\n" in raw
        text = raw.replace("\r\n", "\n")
        before = count_doubts(text)
        for old, new in R.get(scan, []):
            n = text.count(old)
            if n != 1:
                sys.exit("STOP: scan %d: pattern found %d times: %r" % (scan, n, old[:80]))
            text = text.replace(old, new)
        results[scan] = (name, text, crlf, before, count_doubts(text), len(R.get(scan, [])))
    os.makedirs(OUT, exist_ok=True)
    tb = ta = tr = 0
    for scan, (name, text, crlf, b, a, nrep) in sorted(results.items()):
        out = text.replace("\n", "\r\n") if crlf else text
        with open(os.path.join(OUT, name), "wb") as f:
            f.write(out.encode("utf-8"))
        tb += b; ta += a; tr += nrep
        print("scan %03d: replacements %2d, doubt tokens first pass %2d -> corrected %2d%s" % (scan, nrep, b, a, " (CRLF)" if crlf else ""))
    print("TOTAL replacements %d; doubt tokens (\\unsure + \\illegible) first pass %d -> corrected %d" % (tr, tb, ta))

main()

"""Apply the second-pass corrections for block MPL_150_085-099+151_001-031_151-001-151-017.

Copies each first-pass page file, applies the listed replacements (each old string must
occur exactly once), and writes the corrected file under second_pass/out/<package>/.
"""
import os
import sys

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + "/returns/MPL_150_085-099+151_001-031_unzipped/pages"
OUT = BASE + "/second_pass/out/MPL_150_085-099+151_001-031"
PREFIX = "MPL_150_085-099+151_001-031_151_scan"
SCANS = ["001", "002", "003", "004", "005", "006", "007", "008", "009",
         "011", "012", "013", "014", "015", "017"]

LETTER = [
    (r"\uline{OBJET} : Projets d'Action Educative Collège\\",
     r"\uline{OBJET} : Projets d'Action Educative Collège.\\"),
    (r"\unsure{Roux}", r"\illegible{1}"),
]

R = {
    "003": [
        (r"\delta_{\unsure{3|2}}(x,y)&=(x,x,y)\\", r"\delta_3(x,y)&=(x,x,y)\\"),
        (r"\quad $\unsure{=}$\\$\sigma_3\delta_3$}", r"\quad $=$\\$\sigma_3\delta_3$}"),
        (r"\deleted{\[\unsure{p_{12}=p_{23}}\]}", r"\deleted{\[p_{12}=p_{23}\]}"),
        (r"\deleted{\[(x,y,z)\quad(y,z,x)\quad(y,x,z)\]}",
         r"\deleted{\[(x,y,z)\longrightarrow(y,z,x)\longrightarrow(y,z)\]}"),
        (r"Il suffit de \unsure{avoir} $p_0", r"Il suffit de \unsure{avoir|donner} $p_0"),
        (r"\underbrace{\delta_3}_{\rho\deleted{\unsure{\sigma}}\delta_1}",
         r"\underbrace{\delta_3}_{\rho\deleted{\unsure{{}^2|\sigma}}\delta_1}"),
        (r"\overset{??}{\ne}p_{12}(\underbrace{\rho\delta_1}_{\delta_3})",
         r"\overset{??}{\ne}\unsure{p_{23}|p_{22}|p_{12}}(\underbrace{\rho\delta_1}_{\unsure{\delta_2|\delta_3}})"),
        (r"\boxed{\sigma_{\unsure{3|1}}\delta_1=\delta_1}", r"\boxed{\sigma_3\delta_1=\delta_1}"),
        (r"\deleted{$\unsure{\mathrm{ens}}$}", r"\deleted{$\unsure{(\mathrm{Ens})|\mathrm{ens}}$}"),
    ],
    "004": LETTER,
    "006": LETTER,
    "008": LETTER,
    "005": [
        (r"\margin{$\boxed{\deleted{p_0,p_1}}$", r"\margin{$\boxed{\deleted{p_0/p_1}}$"),
        (r"\boxed{p_0p_{12}\sigma_{\unsure{1}}=\underbrace{p_0p_{12}}_{q_1}}",
         r"\boxed{p_0p_{12}\sigma_{\unsure{1|3}}=\underbrace{p_0p_{12}}_{\unsure{q_1|p_1}}}"),
    ],
    "007": [
        (r"Si $E_0$ est réduit à un pt, les $E_1,E_2$ deviennent",
         r"Si $E_0$ est réduit à un pt, \unsure{donc|les} par $\delta_0,\delta_1\delta_0$ $E_1,E_2$ deviennent"),
        ("\\margin{par $\\delta_0,\\delta_1\\delta_0$}\n", ""),
        (r"\deleted{On a.}", r"\deleted{\unsure{Donc.|On a.}}"),
        (r"\deleted{\unsure{qui respecte les}}", r"\deleted{\unsure{qui|$\delta_1$} respecte les}"),
        (r"\unsure{Ainsi|Alors}, en plus", r"\unsure{Donc|Dans|Ainsi|Alors}, en plus"),
    ],
    "009": [
        (r"(une relation \deleted{\unsure{par}} supplémentaire",
         r"(une relation \deleted{\unsure{par|pour}} supplémentaire"),
        (r"\sigma(x)x=1\\[.5em]", r"\sigma(x).x=1\\[.5em]"),
        (r"F_\alpha\arrow[r,hook,no head]\&F\times F", r'F_\alpha\arrow[r,phantom,"\subset"]\&F\times F'),
        ("\\[E_2(\\alpha)\\ni\\delta_1(\\alpha)=\\delta_1\\sigma(\\alpha)\\]\n"
         "\\[\\pi_0(F_\\alpha\\times_F F_\\alpha)=\\overbrace{p_{12}^{-1}(\\alpha)\\cap p_{13}^{-1}(\\alpha)}\\qquad",
         "\\[\\unsure{\\Pi|\\pi}_0(F_\\alpha\\times_F F_\\alpha)=\\overbrace{p_{12}^{-1}(\\alpha)\\cap p_{13}^{-1}(\\alpha)}"
         "^{E_2(\\alpha)\\ni\\delta_1(\\alpha)=\\delta_1\\sigma(\\alpha)}\\qquad"),
    ],
    "011": [
        (r"inspirées par la \unsure{coho} \inserted{``\unsure{Cechiste}''} des recouvrements",
         r"inspirées par \unsure{la|le} yoga \inserted{``\unsure{Cechiste|\v{C}echiste}''} des recouvrements"),
        (r"le raffinement de ce \unsure{p.d.v.|p.d.} suggéré par Cartan",
         r"le raffinement de ce y.g. suggéré par Cartier"),
        (r"satisfait à Hyp 1, l'ens. des flèches", r"satisfait à Hyp 1, i.e. l'ens. des flèches"),
    ],
    "012": [
        ("est couvrant.\n", "\\unsure{reste|est|soit} couvrant.\n"),
        (r"\uline{Hyp 2}\unsure{a} Pour", r"\uline{Hyp 2}\unsure{a|.} Pour"),
        (r"donne une famille couvrant $U_\alpha", r"donne une famille \unsure{couvrante|couvrant} $U_\alpha"),
        (r"\mathbb N^{\deleted{\unsure{*}}}", r"\mathbb N^{\deleted{*}}"),
        (r"$n\geq1$. On voit", r"$n\geq1$ ? On voit"),
        (r"\inserted{$+$} Hyp 2\unsure{a}", r"\inserted{$+$} Hyp 2\unsure{a|.}"),
    ],
    "013": [
        (r"(en termes de $\alpha_0,\alpha_1,\ldots,\alpha_n$)", r"(en termes de $\alpha_0,\alpha_1,\ldots\alpha_n$)"),
        (r"$A_{/\alpha_0}\longrightarrow\mathcal X_{/\alpha_0}$",
         r"$A_{/\alpha_0}\unsure{\longrightarrow|\twoheadrightarrow}\mathcal X_{/\alpha_0}$"),
    ],
    "015": [
        (r"Hyp $\unsure{1|2}'$.)", r"Hyp $\unsure{2|1}'$.)"),
        (r"soit $=$ ex. à gauche ?", r"soit $=$ ex.\textsuperscript{t} à gauche ?"),
    ],
    "017": [
        (r"\margin{$\delta_nK_n\overset{\mathrm{def}}=\rho_{n+1}$ (projection",
         r"\margin{$\delta_nK_n\overset{\text{déf}}{=}\unsure{p_{n+1}|\rho_{n+1}}$ (projection"),
        (r"\text{pour }n\geq2\\", r"\text{pour }n\geq\unsure{2|1}\\"),
        (r"\text{pour }n\geq3\\", r"\text{pour }n\geq\unsure{2|3}\\"),
        (r"\margin{où $i'_n=i_n i_{n-1}:", r"\margin{où $i'_n\underset{\unsure{\text{déf}}}{=}i_n i_{n-1}:"),
        (r"K_n^*\sigma_{\unsure{n}}&=", r"K_n^*\unsure{\sigma|\sigma_n}&="),
        (r"\delta'_m:\mathbb E_{\deleted{\unsure{m+1}}m}", r"\delta'_n:\mathbb E_{\deleted{\unsure{m+1}}m}"),
    ],
}


def main():
    os.makedirs(OUT, exist_ok=True)
    errors = 0
    for s in SCANS:
        name = PREFIX + s + ".tex"
        with open(os.path.join(SRC, name), encoding="utf-8", newline="") as f:
            text = f.read()
        crlf = "\r\n" in text
        if crlf:
            text = text.replace("\r\n", "\n")
        n_applied = 0
        for old, new in R.get(s, []):
            c = text.count(old)
            if c != 1:
                print("ERROR", s, "count", c, "for", repr(old[:70]))
                errors += 1
                continue
            text = text.replace(old, new)
            n_applied += 1
        if crlf:
            text = text.replace("\n", "\r\n")
        dest = os.path.join(OUT, name)
        if "--dry" not in sys.argv:
            with open(dest, "w", encoding="utf-8", newline="") as f:
                f.write(text)
        print(s, "replacements", n_applied, "crlf" if crlf else "lf")
    print("errors", errors)
    return errors


if __name__ == "__main__":
    sys.exit(main())

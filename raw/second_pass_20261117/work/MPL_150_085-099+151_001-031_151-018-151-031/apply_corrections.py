"""Apply the second-pass corrections for block 151-018..151-031.

Reads each first-pass page file, applies exact string replacements (each must
occur exactly the stated number of times, or the script stops), and writes the
corrected file under second_pass/out/MPL_150_085-099+151_001-031/.
"""
import os
import sys

BASE = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + "/returns/MPL_150_085-099+151_001-031_unzipped/pages"
OUT = BASE + "/second_pass/out/MPL_150_085-099+151_001-031"
PFX = "MPL_150_085-099+151_001-031_151_scan"

LH_ACC = ("\\begin{center}\n\\uline{ACADÉMIE D'AIX-MARSEILLE}\\\\\nINSPECTION ACADÉMIQUE\\\\\n"
          "\\uline{DE VAUCLUSE}\n\\end{center}")
LH = ("\\begin{center}\n\\uline{ACADEMIE D'AIX-MARSEILLE}\\\\\nINSPECTION ACADEMIQUE\\\\\n"
      "\\uline{DE VAUCLUSE}\n\\end{center}")
LH_NEW = ("\\textbf{ACADEMIE D'AIX-MARSEILLE}\\\\\n\\rule{3cm}{.4pt}\\\\\n\\textbf{INSPECTION ACADEMIQUE}\\\\\n"
          "\\textbf{DE VAUCLUSE}\\\\\n\\rule{1cm}{.4pt}")

V = "\\unsure{\\mathcal V_{Y,X}|V_{Y,X}}"
VS = "\\unsure{\\mathcal V_{Y,X}^*|V_{Y,X}^*}"

# (old, new, expected count); count None = replace all, at least one
R = {
    18: [
        (LH_ACC, LH_NEW, 1),
        ("{$\\unsure{\\int}E_p$}", "{$\\{E_p$}", 1),
        ("{$\\unsure{\\int}E'_q$}", "{$\\{E'_q$}", 1),
        ("{$\\unsure{\\int}E\\setminus\\{\\alpha\\}$}", "{$\\{E\\setminus\\{\\alpha\\}$}", 1),
        ("\\margin{$\\unsure{p\\geq}$}", "\\margin{$\\unsure{p\\geqq|p\\geq}$}", 1),
        ("\"\\unsure{u}=\\varphi^*\"'", "\"u=\\varphi^*\"'", 1),
        ("\"\\unsure{v}=\\varphi_!\"'", "\"v=\\varphi_!\"'", 1),
        ("{$\\unsure{u|v}(F)=", "{$u(F)=", 1),
        ("{$\\unsure{v|u}(G)=", "{$v(G)=", 1),
    ],
    19: [
        (LH, LH_NEW, 1),
        ("K\\arrow[r]\\&\\unsure{\\bullet|K'}\\arrow[r,dash]\\&\\bullet",
         "K\\arrow[r]\\&\\deleted{\\unsure{K'}}\\arrow[r,dash]\\&\\bullet", 1),
        ("X'_2\\arrow[l,dash]\\arrow[u]", "X'_2\\arrow[l]\\arrow[u]", 1),
        ("I'\\arrow[r,hook]\\&J'=I'\\amalg K", "I'\\arrow[r,hook,dash]\\&J'=I'\\amalg K", 1),
        ("X(\\unsure{I})\\&", "X(\\unsure{I|J})\\&", 1),
        ("X(\\unsure{I'})\\arrow[u]", "X(\\unsure{I'|J'})\\arrow[u]", 1),
        ("&p=1,q=2&\\\\", "&p=\\unsure{1|4},q=2&\\\\", 1),
    ],
    20: [
        (LH, LH_NEW, 1),
        ("\"{(p_{12},\\unsure{q_3})\\ \\text{épi}}\"", "\"{(p_{12},\\unsure{q_3|p_{13}})\\ \\text{épi}}\"", 1),
        ("X_3\\arrow[r,two heads,\"\\unsure{p_1|\\delta_1}\"]", "X_3\\arrow[r,\"\\unsure{p_1|\\delta_1}\"]", 1),
        ("\\mathbb E_2\\arrow[r,dash,\"\\delta_{\\unsure{3|2}}\"]", "\\mathbb E_2\\arrow[r,\"\\delta_{\\unsure{3|2}}\"]", 1),
        ("\\&\\deleted{X_2}\\arrow[l,shift right=1.5,\"\\delta_1^*\"']", "\\&X_2\\arrow[l,shift right=1.5,\"\\delta_1^*\"']", 1),
        ("\\unsure{structures|ponctuations}", "\\unsure{ponctuations|pointations|structures}", 1),
    ],
    21: [
        ("(y,x,\\unsure{x|n})", "(y,x,x)", 1),
    ],
    22: [
        (LH, LH_NEW, 1),
        ("[\\rho^i d(\\unsure{\\zeta|\\xi})=\\rho^{i'}d(\\unsure{\\zeta'|\\xi'})]",
         "[\\rho^i d(\\unsure{\\zeta|\\xi}\\deleted{\\unsure{'}})=\\rho^{i'}d(\\unsure{\\zeta'|\\xi'})]", 1),
        ("\\rho^{i\\deleted{\\unsure{'}}-i'}d(\\unsure{\\zeta|\\xi})]",
         "\\rho^{i\\deleted{\\unsure{'}}-i'}d(\\unsure{\\zeta|\\xi}\\deleted{\\unsure{'}})]", 1),
        ("d(\\unsure{\\zeta'|\\xi'})=\\rho^j d(\\unsure{\\zeta|\\xi})",
         "d(\\unsure{\\zeta'|\\xi'})=\\rho^j d(\\unsure{\\zeta|\\xi}\\deleted{\\unsure{'}})", 1),
        ("&\\text{donc}\\quad\\unsure{\\zeta|\\xi}=\\unsure{\\zeta'|\\xi'}=e_2\\\\",
         "&\\text{donc}\\quad\\unsure{\\zeta|\\xi}\\deleted{\\unsure{'}}=\\unsure{\\zeta'|\\xi'}=e_2\\\\", 1),
    ],
    23: [
        ("(avec la représentation régulière de", "(dans la représentation régulière de", 1),
        ("s'écrit canoniquement\n\\[",
         "s'écrit canoniquement\n% second pass: the group letter after \"régulière de\" above and the one inside the\n"
         "% parenthesis of the display below are each crossed by an X-shaped stroke\n"
         "% (overwriting or cancellation; unresolved, see the changes table).\n\\[", 1),
        ("X_3^*\\arrow[r,two heads,\"p^*=p\\mid X_3^*\"]", "X_3^*\\arrow[r,\"p^*=p\\mid X_3^*\"]", 1),
    ],
    24: [
        (LH, LH_NEW, 1),
        ("et l'intersection de deux \\unsure{quelconques} des trois est égale à",
         "dont l'intersection de deux \\unsure{quelconques des|parmi les} trois est égale à", 1),
        ("S'il y a \\deleted{\\unsure{donc}} au moins", "S'il y a \\deleted{\\unsure{deux|donc}} au moins", 1),
    ],
    25: [
        ("\\inserted{pour $\\unsure{\\zeta|\\xi},\\unsure{\\zeta'|\\xi'}\\in X_2$,}",
         "\\inserted{pour} $\\unsure{\\zeta|\\xi},\\unsure{\\zeta'|\\xi'}\\in X_2$,", 1),
        ("\\inserted{$(=\\delta_3)$}.", "\\inserted{$(=\\delta_3=$}.", 1),
        ("X_3\\arrow[l,\"p=p_{12}\"']", "X_3\\arrow[l,\"p=p_{\\unsure{1|3}2}\"']", 1),
    ],
    27: [
        ("\\unsure{ça|ce} devienne des topos", "\\unsure{ça|ce} \\unsure{deviennent|devienne} des topos", 1),
        ("de $y$ \\unsure{et} un espace $Z$", "de $y$ et un espace $Z$", 1),
        (V, "\\mathcal V_{Y,X}", None),
    ],
    28: [
        ("techniquement simple.", "techniquement \\unsure{simple|souple}.", 1),
        ("$Y$ et $X-Y=X^*$ des variétés", "$Y$ et $X-Y=X^*$ \\deleted{des} variétés", 1),
        ("\\deleted{\\unsure{et que}} alors que", "\\deleted{\\unsure{$Z^*$ est|et que}} alors que", 1),
        ("de vouloir reconstruire $X$", "de vouloir reconstituer $X$", 1),
        (V, "\\mathcal V_{Y,X}", None),
    ],
    29: [
        ("de toute hypothèse de locale trivialité normale, ou de lissité",
         "de toute hypothèse \\unsure{$=$|--} de locale trivialité normale, \\unsure{$=$|--|ou} de lissité", 1),
        ("comme \\deleted{\\unsure{espace}} espace-topos $\\varinjlim$",
         "comme \\deleted{\\unsure{en|espace}} \\unsure{espace-topos|espace ou topos} $\\varinjlim$", 1),
        (VS, "\\mathcal V_{Y,X}^*", None),
        (V, "\\mathcal V_{Y,X}", None),
    ],
    30: [
        ("\\deleted{topos}\\inserted{``espaces''}", "\\deleted{\\unsure{types|topos}}\\inserted{``espaces''}", 1),
        ("``tuant les $\\pi_i$ pour $i\\geq2$''", "``tuant les $\\unsure{\\pi|\\Pi}_i$ pour $i\\geq2$''", 1),
        (VS, "\\mathcal V_{Y,X}^*", None),
        (V, "\\mathcal V_{Y,X}", None),
    ],
    31: [
        ("\\unsure{\\pi|\\Pi}", "\\Pi", None),
        ("il \\unsure{resterait} encore", "il \\unsure{resterait|vaudrait} encore", 1),
        ("moy\\textsuperscript{t}} d'un choix suppl.", "moy\\textsuperscript{t}} \\unsure{d'un choix|des choix} suppl.", 1),
        (VS, "\\mathcal V_{Y,X}^*", None),
        (V, "\\mathcal V_{Y,X}", None),
    ],
}

SCANS = [18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31]


def main():
    os.makedirs(OUT, exist_ok=True)
    for s in SCANS:
        name = f"{PFX}{s:03d}.tex"
        with open(os.path.join(SRC, name), encoding="utf-8") as f:
            text = f.read()
        for old, new, n in R.get(s, []):
            c = text.count(old)
            if (n is None and c < 1) or (n is not None and c != n):
                sys.exit(f"scan {s}: expected {n} of {old!r}, found {c}")
            text = text.replace(old, new)
            print(f"scan {s}: replaced {c}x {old[:50]!r}")
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print("done")


if __name__ == "__main__":
    main()

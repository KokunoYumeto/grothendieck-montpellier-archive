# Exact replacements per scan, applied at the end to the first-pass files: (old, new, expected count)
EDITS = {}
EDITS[161] = [
    (r"\operatorname{Pic}(A)^{\unsure{\mathrm{abs}|\mathrm{ab}}}", r"\operatorname{Pic}(A)^{\mathrm{abs}}", 1),
    (r"\text{\unsure{réseaux} de Hodge}", r"\text{réseaux de Hodge}", 2),
]
EDITS[163] = [
    (r"Si $\widetilde\xi$ est réelle", r"Si $\widetilde\xi$ \deleted{est} réelle", 1),
    (r"\deleted{\text{\unsure{Vecteurs}}}", r"\deleted{\text{\unsure{Vectoriels|Vecteurs}}}", 1),
    (r"muni de \deleted{une} structure", r"muni des \deleted{\unsure{une}} structure", 1),
]
EDITS[165] = [
    (r"H_\xi(\unsure{W|V})^{(p)}", r"H_\xi(W)^{(p)}", 1),
    (r"\margin{\unsure{coh. de De Rham}}", r"\margin{coh. de De Rham}", 1),
    (r"\uline{$\unsure{K_\xi}$-linéaire}", r"\uline{$\frac12$-linéaire}", 1),
]
EDITS[166] = [
    (r"\unsure{\leq}1\leq j\leq n_i", r"\leq 1\leq j\leq n_i", 1),
]
EDITS[168] = [
    (r"$K=\mathbf Q(\unsure{\zeta})$", r"$K=\mathbf Q(\zeta)$", 1),
]
EDITS[173] = [
    (r"\text{si }n\neq0,\quad\text{pour tous }i", r"\text{si }n\neq0,\quad\text{\unsure{quel que soit|pour tous} }i", 1),
    (r"H^i(\operatorname{Spec}\mathbf Z,\mathbf Z(1))", r"\mathbb H^i(\operatorname{Spec}\mathbf Z,\mathbf Z(1))", 1),
    (r"\unsure{\mathbb H|H}^i(\operatorname{Spec}\mathbf Z,\mathbf Z)", r"\mathbb H^i(\operatorname{Spec}\mathbf Z,\mathbf Z)", 1),
    (r"\mathbf Z/l^{\unsure{v_l|\nu_l}(1-q^n)}", r"\mathbf Z/l^{v_l(1-q^n)}", 1),
]
EDITS[174] = [
    (r"\margin{\unsure{pas de miracle}, car si $i\geq4$, les deux \unsure{mbs} doivent être $=0$.}", r"\margin{pas de miracle, car si $i\geq4$, les deux mbs doivent être $=0$.}", 1),
    (r"[\unsure{est-on|est-ce} nul ??]", r"[\unsure{est-ce|est-on} nul ??]", 1),
    (r"\unsure{où on trouve} $\mathbf Q$ !", r"où on trouve $\mathbf Q$ !", 1),
]
EDITS[176] = [
    (r"\unsure{localisés|locaux}", r"localisés", 1),
    (r"\uline{\unsure{D|Z}^0}_X", r"\uline{\unsure{\mathrm{Div}|D^0}}_X", 1),
    (r"Si $X$ est un schéma \unsure{loc|local}, \unsure{et}", r"Si $X$ est un schéma local, et", 1),
    (r"\unsure{un|une} \deleted{extension} morphisme", r"\deleted{une extension} morphisme", 1),
    (r"\deleted{\unsure{splitte} $\xi$}", r"\deleted{splitte $\xi$}", 1),
]
EDITS[177] = [
    (r"\margin{\unsure{pas de miracle}, car les deux sont nuls.}", r"\margin{pas de miracle, car les deux sont nuls.}", 1),
]

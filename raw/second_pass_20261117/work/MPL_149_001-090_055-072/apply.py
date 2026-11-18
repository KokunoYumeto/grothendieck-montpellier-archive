"""Apply the second-pass corrections to scans 055-072 of MPL_149_001-090.

Reads the first-pass page files, replaces each first-pass string (which must occur exactly once in its file)
by the corrected reading, and writes every page of the block to second_pass/out/MPL_149_001-090/.
Nothing is written if any check fails.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SRC = os.path.join(ROOT, 'returns', 'MPL_149_001-090_unzipped', 'pages')
OUT = os.path.join(ROOT, 'second_pass', 'out', 'MPL_149_001-090')

RULE = r"\margin{\figure{\begin{tikzpicture}\draw (0,0)--(0,-1.9);\draw (0.12,-0.5)--(0.12,-1.8);\end{tikzpicture}}}"

CHANGES = {
    55: [
        (r"$(0,3)$, \deleted{\unsure{car}} car en bouchant deux trous on tombe",
         r"$(0,3)$, --- car en bouchant deux trous, on tombe"),
        (r"\margin{À énoncer parmi les conjectures-clefs\ldots}",
         RULE + "\n" + r"\margin{À énoncer parmi les conjectures-clefs\ldots}"),
    ],
    56: [
        (r"\margin{Il y a \uline{\unsure{de plus}} les précisions",
         r"\margin{Il y a \inserted{\unsure{de plus}} plus d'\illegible{1} les précisions"),
        (r"$E_L\longrightarrow E_K$ ($E_L$ peut",
         r"$E_L\longrightarrow \unsure{E|B}_K$ ($E_L$ peut"),
        (r"que tout scindage de cette extension",
         r"que toute scindage de cette extension"),
    ],
    57: [
        (r"se grouperaient donc \deleted{dans de} par paquets",
         r"se grouperaient \unsure{donc|dans} \unsure{\inserted{classes de}|\deleted{dans de}} "
         r"\deleted{\unsure{par}\ \illegible{1}} paquets"),
        (r"pour $\forall$ ext. finie",
         r"pour tt ext. finie"),
        (r"la structure $E_L\longrightarrow E_K$ qui",
         r"la structure $E_L\unsure{-|\longrightarrow}E_K$ qui"),
        (r"en disant que \unsure{tt}",
         r"en disant que tt"),
    ],
    58: [
        (r"noter $\widetilde X$, car que justement",
         r"noter $\widetilde X$, \unsure{car|vu} que justement"),
    ],
    59: [
        (r"\inserted{\unsure{topologique|topologisons}}",
         r"\inserted{\unsure{compatibles avec|topologique|topologisons}}"),
        (r"sur $\bar K$, identifié à la clôture",
         r"sur $\bar K$, \unsure{identifié|s'identifie} à la clôture"),
        (r"sur $\unsure{\widetilde U|\bar U}$, et continue",
         r"sur $\widetilde U$, et continue"),
        (r"Considérons alors la",
         r"Considérons donc la"),
        (r"\unsure{th.3} du",
         r"th.3 du"),
    ],
    61: [
        (r"cas du pt fixe à l'infini",
         r"cas de pt fixe à l'infini"),
    ],
    62: [
        (r"\uline{courbes de Poincaré}",
         r"\uline{courbes} de \uline{Poincaré}"),
    ],
    63: [
        (r"\uline{Conjecture B'} Soit $K$",
         r"\uline{Conjecture B'} \unsure{Soient|Soit} $K$"),
        (r"\Gamma_{\bar K/K}",
         r"\Gamma_{\bar K|K}"),
    ],
    64: [
        (r"(4')\quad\diagram",
         r"\unsure{(5)|(4')}\quad\diagram"),
    ],
    67: [
        (r"$\unsure{\longleftarrow}$",
         r"$\unsure{\longleftarrow|\deleted{(}}$"),
    ],
    70: [
        (r"ou des courbes à $\pi_1$ non nul",
         r"ou du moins à $\pi_1$ non nul"),
    ],
    72: [
        (r"\unsure{1|2}",
         r"\unsure{2|1}"),
    ],
}


def main():
    pages = {}
    bad = []
    n = 0
    for scan in range(55, 73):
        name = 'MPL_149_001-090_scan%03d.tex' % scan
        with open(os.path.join(SRC, name), encoding='utf-8', newline='') as f:
            text = f.read()
        for old, new in CHANGES.get(scan, []):
            c = text.count(old)
            if c != 1:
                bad.append((scan, old, c))
                continue
            text = text.replace(old, new)
            n += 1
        pages[name] = text
    if bad:
        for b in bad:
            print('NOT EXACTLY ONCE:', b)
        sys.exit(1)
    os.makedirs(OUT, exist_ok=True)
    for name, text in pages.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
            f.write(text)
    print('replacements applied:', n, '; files written:', len(pages))


if __name__ == '__main__':
    main()

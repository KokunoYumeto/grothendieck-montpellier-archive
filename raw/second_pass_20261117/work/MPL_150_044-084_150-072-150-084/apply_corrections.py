"""Apply the second-pass corrections of block 150-072..084 to the first-pass page files.

Each replacement must match exactly once in its file, or the script stops.
Reads:  returns/MPL_150_044-084_unzipped/pages/MPL_150_044-084_150_scanNNN.tex
Writes: second_pass/out/MPL_150_044-084/MPL_150_044-084_150_scanNNN.tex
"""
import os
import sys

ROOT = 'C:/Users/user/Documents/grothendieck_archive_transcription_20261110'
SRC = ROOT + '/returns/MPL_150_044-084_unzipped/pages'
OUT = ROOT + '/second_pass/out/MPL_150_044-084'

R = {
    72: [
        (r"\Sigma_{\unsure{*|0}}=\Sigma_{(0)}",
         r"\Sigma_{\deleted{\unsure{*|0}}}=\Sigma_{(0)}"),
        (r"c) Si $x,y\in\Sigma$ sont ds une",
         r"c) Si $x,y\in\Sigma$ \unsure{\deleted{sont}|sont} \unsure{ds|dans} une"),
        (r"\unsure{de la notion|la notion} de déploiement",
         r"\unsure{un contexte|un certain|de la notion|la notion} de déploiement"),
        ("on peut appliquer la sorite\nsur $\\widetilde I",
         "on peut appliquer \\unsure{le|la} \\unsure{sorite|sortie}\n\\unsure{du|des} $\\widetilde I"),
        (r"cela revient à \unsure{remplacer|raffiner} la stratification",
         r"cela revient à remplacer la stratification"),
    ],
    73: [
        (r"\inserted{``standart'' $T_{<i}$} fermé de",
         r"\inserted{``standart'' $T_{<i}$} \deleted{\unsure{fermé}} de"),
        (r"\bigcup_{k<i}X_i$, et on prend",
         r"\bigcup_{k<i}\unsure{X_i|X_k}$, et on prend"),
        (r"lui-m\textsuperscript{e}, et de prendre donc",
         r"lui $\unsure{\overline{\mathrm m}}$, et de prendre donc"),
        (r"\bigcup_{\unsure{i<k<j|i\leq k<j}}X_{jk}$",
         r"\bigcup_{\unsure{i<k<j|i\leq k<j}}\unsure{X_{jk}|X_k}$"),
        (r"(cela est vide si $j$ est un successeur de $i$)",
         r"(\unsure{donc c'est} vide si $j$ est un successeur de $i$)"),
        (r"On \deleted{prend}\inserted{aura} alors",
         r"On \deleted{\unsure{prendra}}\inserted{aura} alors"),
    ],
    74: [
        (r"ajusté de façon cohérente les choix",
         r"ajusté de façon évidente les choix"),
        (r"\deleted{Cette construction \unsure{devra}}",
         r"\deleted{Cette construction \unsure{devra|donne}}"),
        (r"X^{(2)}\subset X\setminus X_{(1)}",
         r"X^{(2)}\subset X-X_{(1)}"),
    ],
    75: [
        (r"\margin{NB $T_d=",
         r"\margin{OPS $T_d="),
        (r"\bigcup_{\uline{\alpha}<d}X_i\cap",
         r"\bigcup_{\underset{\sim}{\alpha}<d}X_i\cap"),
    ],
    76: [
        (r"$(\Sigma_i,(\Sigma_j),$",
         r"$((\Sigma_i),(\Sigma_{ij}),$"),
    ],
    77: [
        (r"On désigne par $V_i^{\unsure{\deleted{*}|*}}$ le",
         r"On désigne par $V_i^{\unsure{\deleted{*}|*}}$ \unsure{\deleted{le}|le}"),
        (r"Si $\unsure{\forall i,j|(i,j)}$ $i<j$, on pose",
         r"Si $i<j$, on pose"),
        (r"V_{ij}^{\unsure{b}}=V_i\cap X_j^*\arrow[r,hook]&{}",
         r"V_{ij}^{\unsure{b}}=V_i\cap X_j^*\arrow[r,hook]&\unsure{V_{ij}}"),
        (r'\arrow[d,leftrightarrow,"s_{ij}"]',
         r'\arrow[d,hook,"s_{ij}"]'),
        (r'\arrow[r,"{\substack{(w)\\\sim}}"]',
         r'\arrow[r,"{\substack{\unsure{(w)|(h)}\\\sim}}"]'),
        (r"V_{ij},\deleted{\unsure{\}}}\ b_{ij}",
         r"V_{ij},\unsure{\deleted{\}}|\rightrightarrows}\ b_{ij}"),
    ],
    78: [
        (r"V_{i_0\ldots i_n}^Z=V_{i_0\ldots i_n}\cap Z",
         r"V_{i_0-i_n}^Z=V_{i_0-i_n}\cap Z"),
    ],
    79: [
        (r"V_{j_0\ldots j_n}^J",
         r"V_{j_0-j_n}^J"),
        (r"=V_{j_0\ldots j_n}^Z",
         r"=V_{j_0-j_n}^Z"),
    ],
    80: [],
    81: [
        (r"On s'intéresse aux \unsure{protopos} de la forme",
         r"On s'intéresse aux \unsure{protopos|proespaces|provoisinages} de la forme"),
        (r"élément de $J$ est majoré par un élément de $L$, \unsure{tt}",
         r"élément de $J$ majoré par un élément de $L$, \unsure{tt}"),
    ],
    82: [
        (r"\inserted{la bande $I'$ de b) est unique, \unsure{plus petite}} petite bande",
         r"\inserted{la bande $I'$ de b) est unique,} \unsure{et|c'est} la plus petite petite bande"),
    ],
    83: [
        (r"(69)\qquad V_J^L=\bigcup",
         r"V_J^L=\bigcup"),
        (r"soient normaux, voire $X$ métrisable",
         r"soient normaux, p.ex. $X$ métrisable"),
    ],
    84: [],
}


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for scan, reps in R.items():
        name = f'MPL_150_044-084_150_scan{scan:03d}.tex'
        with open(os.path.join(SRC, name), 'rb') as f:
            raw = f.read().decode('utf-8')
        crlf = '\r\n' in raw
        text = raw.replace('\r\n', '\n')
        for old, new in reps:
            n = text.count(old)
            if n != 1:
                sys.exit(f'scan {scan}: expected 1 match, found {n}: {old!r}')
            text = text.replace(old, new)
            total += 1
        if crlf:
            text = text.replace('\n', '\r\n')
        with open(os.path.join(OUT, name), 'wb') as f:
            f.write(text.encode('utf-8'))
        print(scan, len(reps), 'replacements', 'CRLF' if crlf else 'LF')
    print('total replacements', total)


if __name__ == '__main__':
    main()

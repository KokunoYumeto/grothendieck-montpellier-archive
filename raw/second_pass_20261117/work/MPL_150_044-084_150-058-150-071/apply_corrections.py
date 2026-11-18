"""Apply the second-pass corrections of block MPL_150_044-084_150-058-150-071.

Reads the first-pass page files, applies exact single-occurrence replacements
(asserted), and writes the corrected page files to second_pass/out/MPL_150_044-084/.
Unchanged pages are written as they are. Prints counts of doubt macros before/after.
"""
import os
import re

ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = ROOT + "/returns/MPL_150_044-084_unzipped/pages"
OUT = ROOT + "/second_pass/out/MPL_150_044-084"
NAME = "MPL_150_044-084_150_scan{:03d}.tex"

R = {
    58: [
        (r'''\xrightarrow{\uline{s}=\operatorname{pr}_1}''', r'''\xrightarrow{\uline{s}=p_1}'''),
        (r'''qui est injective \deleted{et croissante} sur chaque fibre \inserted{$b^{-1}(x)$}''',
         r'''qui soit injective \deleted{et croissante} sur chaque fibre \inserted{$\uline{b}^{-1}(x)$}'''),
        (r'''(i.e. $\Sigma^{<}(1)\xrightarrow{(s,b)}\Sigma\times\Sigma$ inj.''',
         r'''(i.e. $\Sigma^{<}(1)\xrightarrow{(\uline{s},\uline{b})}\Sigma\times\Sigma$ inj.'''),
        (r'''(i.e. $\operatorname{Im}(s,b)\cap''', r'''(i.e. $\operatorname{Im}(\uline{s},\uline{b})\cap'''),
        (r'''\Sigma^{<}(2)\arrow[r,"p_2"] & \Sigma^{*}(1)''', r'''\Sigma^{<}(2)\arrow[r,"\varphi_2"] & \Sigma^{*}(1)'''),
        (r'''\margin{NB la donnée de $p_2$ équivaut''', r'''\margin{NB la donnée de $\unsure{\varphi_2|p_2}$ équivaut'''),
    ],
    59: [
        (r'''\Sigma^{<}(1)\arrow[d,"p_1=s"]''', r'''\Sigma^{<}(1)\arrow[d,"p_1=\uline{s}"]'''),
        (r'''\uline{transversal} p. v. à l'immersion bordante''', r'''\uline{transversal} p.r. à l'immersion bordante'''),
    ],
    60: [
        (r'''p_1u=x,\quad\underbrace''', r'''\deleted{\unsure{s}}p_1u=x,\quad\underbrace'''),
    ],
    61: [
        (r'''\margin{``stratification cylindrique localt ordonnée''}''',
         r'''\margin{``stratification cylindrique loc${}^t$. tot${}^t$ ordonnée''}'''),
        (r'''diagonale \inserted{$\forall\ u''', r'''diagonale \inserted{i.e. $\forall\ u'''),
    ],
    62: [
        (r'''est (fini) \uline{tot.} \uline{ordonné}.''', r'''est (fini) \uline{tot${}^t$.} \uline{ordonné}.'''),
    ],
    63: [
        (r'''\inserted{la famille} germes \inserted{en $x$}''', r'''\inserted{la famille} des germes \inserted{en $x$}'''),
        (r'''\uline{transversal} p.v. à l'immersion''', r'''\uline{transversal} p.r. à l'immersion'''),
    ],
    65: [
        (r'''\uline{\Sigma_{ijk}\deleted{\unsure{\ne}}\subset\deleted{\unsure{\Sigma_{ik}}}\unsure{b_{ij}^{-1}|s_{jk}^{-1}}(\Sigma_{ij})}''',
         r'''\uline{\Sigma_{ijk}\deleted{\unsure{\ne|\subset}}=\deleted{\unsure{\Sigma_{ik}}}b_{ij}^{-1}(\Sigma_{ij})}'''),
        (r'''$\Sigma_{<x}$ est induite par celle de $I_{<i}$).}''', r'''$\Sigma_{<x}$ soit induite par celle de $I_{<i}$).}'''),
    ],
    66: [
        (r'''est transversal p.v. au système trans-''', r'''est transversal p.r. au système trans-'''),
    ],
    67: [
        (r'''satisfait la condition c) du Scholie (p. $27$).''', r'''(satisfait la condition c) du Scholie (p. $27$).'''),
        (r'''la réunion des $\Sigma_{kij}$ et $\Sigma_{ijk}$ --- mais''', r'''la réunion des $\Sigma_{kij}$ et $\Sigma_{ikj}$ --- mais'''),
        (r''':\unsure{\Sigma_{jk}|\Sigma_{ik}}\longrightarrow\Sigma_j$ est''', r''':\unsure{\Sigma_{ik}|\Sigma_{jk}}\longrightarrow\Sigma_j$ est'''),
        (r'''"\unsure{\text{cpl.}|\text{appl.}}"''', r'''"\unsure{\text{cpl.}|\text{compl.}|\text{appl.}}"'''),
    ],
    68: [
        (r'''\inserted{[\unsure{anglicisme}]}''', r'''\inserted{[\unsure{morphisme|anglicisme})}'''),
    ],
    69: [
        (r'''de la catégorie topologique $\uline{\Sigma}$''', r'''de \unsure{cette|la} catégorie topologique $\uline{\Sigma}$'''),
        (r'''une imm. v.v., on doit avoir aussi''', r'''une imm. rare, on doit avoir aussi'''),
    ],
    70: [
        (r'''(correspondant \inserted{localement} à un déploiement''', r'''(correspondant \inserted{\unsure{moralement}} à un déploiement'''),
        (r'''Considérons alors le \deleted{foncteur}\inserted{morphisme}''',
         r'''Considérons alors \unsure{la|le} \deleted{\unsure{factorisation}}\inserted{morphisme}'''),
    ],
    71: [
        (r'''deux éléments $\unsure{x_i}$ et $y$ de $\Sigma$,''', r'''deux éléments $\unsure{x_i}$ et $x_j$ de $\Sigma$,'''),
    ],
}

DOUBT = re.compile(r"\\(unsure|illegible)\{")


def main():
    os.makedirs(OUT, exist_ok=True)
    tot_b = tot_a = nrep = 0
    for n in range(58, 72):
        with open(os.path.join(SRC, NAME.format(n)), encoding="utf-8") as f:
            text = f.read()
        before = len(DOUBT.findall(text))
        for old, new in R.get(n, []):
            c = text.count(old)
            assert c == 1, (n, c, old)
            text = text.replace(old, new)
            nrep += 1
        after = len(DOUBT.findall(text))
        tot_b += before
        tot_a += after
        with open(os.path.join(OUT, NAME.format(n)), "w", encoding="utf-8", newline="") as f:
            f.write(text)
        print(f"scan {n:03d}: replacements {len(R.get(n, []))}, doubt macros {before} -> {after}")
    print(f"total replacements {nrep}; doubt macros first pass {tot_b}, corrected {tot_a}")


if __name__ == "__main__":
    main()

# Applies the second-pass corrections of block MPL_152+120_120-007-120-025 (cote 120, scans 7-25)
# to the first-pass page files and writes the corrected files to second_pass/out/MPL_152+120/.
# Every replacement must match exactly once; otherwise the script stops without writing anything.
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SRC = os.path.join(BASE, 'returns', 'MPL_152+120_unzipped', 'pages')
OUT = os.path.join(BASE, 'second_pass', 'out', 'MPL_152+120')
NL = '\n'

R = {
7: [
 (r'\mspage{6}\hfill\mspage{3}', r'\mspage{6}\hfill\mspage{\unsure{3}}'),
 (r'\deleted{produits \unsure{fibrés|finis}, et des produits (de deux objets),',
  r'\deleted{produits \unsure{fibrés|finis} \inserted{\unsure{\deleted{(de deux objets}|(de deux objets} sur un troisième)}, et des produits (de deux objets),'),
 (r"(\unsure{M5'|M5})\qquad R_0\ne\varnothing", r'(M5)\qquad R_0\ne\varnothing'),
 (r'\inserted{(\deleted{\unsure{pas des objets}} \unsure{sans restriction})}' + NL, ''),
 (r'et le foncteur $X\longmapsto|X|$ commute.', r'et le foncteur $X\longmapsto|X|$ y commute.'),
 (r"\margin{\unsure{trivialité de} \unsure{celui} \illegible{1} d'un \illegible{1} \unsure{des} \unsure{lois} \illegible{2} des \unsure{foncteurs}}",
  r"\margin{\unsure{trivialité de|existence} \unsure{celui|unicité} \illegible{1} d'un \illegible{1} \unsure{des lois|tandis que} \illegible{2} des \unsure{foncteurs}}"),
 (r'pour $\forall I$ fini' + NL + r'\[', r'pour $\forall I$ fini \inserted{dans}' + NL + r'\['),
 (r"\unsure{l'axiome} $(M1)$", r"\unsure{l'axiome} $\unsure{(M1)|(M11)}$"),
],
8: [
 (r'(en tant que modèle $\subset R^1=R$)', r'(en \unsure{tant|\deleted{tant}} que modèle $\subset R^1=R$)'),
 (r"comme l'ens des sous-objets \inserted{\unsure{sous-ens.} de $R^n$ \unsure{correspondants dans Ens}} (dans $\mathcal E$)",
  r"comme l'ens des \inserted{\unsure{sous-ens.} de $R^n$ \unsure{correspondant aux|correspondants dans Ens}} sous-objets (dans $\mathcal E$)"),
 (r'tel que $\forall$ objet de $\unsure{R|\mathcal E}$ se plonge', r'tel que \unsure{tt|$\forall$} objet de $R$ se plonge'),
 (r"d'un espace modéré \unsure{correspondant} aux sous-objets", r"d'un espace modéré correspondant aux sous-objets"),
 (r'\unsure{Je verrai} $(M)_0$', r'\unsure{Je verrai} \uline{\unsure{bien}} $(M1)_0$'),
],
9: [
 (r'\margin{\unsure{le donner} \uline{après}', r'\margin{le donner \uline{après}'),
 (r'\deleted{$\mathcal E$ \unsure{est}, \unsure{a des} sommes finies} \unsure{(uniquement} et $X\mapsto|X|$ y commute.' + NL + NL
  + r'\figure{\begin{tikzpicture}\node[draw,ellipse] {$M5$};\end{tikzpicture}}' + NL,
  r'\deleted{$\mathcal E$ il y a des sommes finies} (moyennant \figure{\begin{tikzpicture}[baseline=(m.base)]\node[draw,ellipse,inner sep=1pt] (m) {$M5$};\end{tikzpicture}}) et $X\mapsto|X|$ y commute.' + NL + NL),
],
10: [
 (r'Sur $\varnothing$ il $\exists$ une structure', r'Sur $\varnothing$ il y a une structure'),
 (r'\uline{Proposition} Soit $X$ un espace modéré', r'\uline{Proposition} \unsure{Soient|Soit} $X$ un espace modéré'),
 (r'&\unsure{Y|Z}\arrow[dl]\arrow[dr]&\\', r"&\unsure{Z|Y}\arrow[dl,hook']\arrow[dr,hook]&\\"),
],
11: [
 (r"il \unsure{f. et s.} qu'il existe", r"il f. et s. qu'il existe"),
 (r'f_\alpha(\unsure{i_1|z_1}(z))=g_\alpha(i_2(z))\qquad\forall\alpha\in\unsure{I|A},\ z\in Z',
  r'f_\alpha(i_1(z))=g_\alpha(i_2(z))\qquad\forall\alpha\in A,\ z\in Z'),
 (r'X_1\longrightarrow R^I\qquad(X_2\longrightarrow R^I)', r'X_1\longrightarrow R^I\qquad(X_2\longrightarrow R^A)'),
 (r'(f_\alpha:i\in I\qquad f_{\alpha i}:X_i', r'(f_{\alpha i}\,{}_{i\in I}\qquad f_{\alpha i}:X_i'),
 (r'déterminant des', r'\unsure{obtenant|déterminant|définissant} des'),
],
12: [
 (r'Il nous reste à prouver que cela implique', r'Il est évident : \unsure{prouvons|prouver} que cela implique'),
 (r'et \deleted{donc} leur réunion aussi.', r'et donc leur réunion aussi.'),
],
13: [
 (r'De plus, \unsure{OPS} que les', r'De plus, OPS que les'),
 (r'\unsure{ce qui est} \uline{équivalent} au fait que', r'\unsure{ce qui|ce que} \uline{\unsure{équivaut|équivalent|signifiant}} au fait que'),
 (r'qui prolonge' + NL, r'qui prolonge \unsure{$f$}' + NL),
 (r'et commutent au foncteur oubli.', r'et commutent au foncteur oubli\ldots'),
],
14: [],
15: [
 (r'\margin{on suppose $M5$ mais pas $M6$ \unsure{et} $M7$}', r'\margin{on suppose $M5$ mais pas $M6$ \unsure{et|ni} $M7$\ldots}'),
 (r'Si $R_0\ne\varnothing$ (i.e. dans', r'Si $R_0\ne\varnothing$ (idem dans'),
 (r'\inserted{(infinies !)}', r'\inserted{\unsure{(infinies !)|(en principe !)}}'),
],
16: [
 (r'etc de $=$', r'et de $=$'),
 (r'au sens (et commute à $X\mapsto|X|$)', r'au sens (et commute \unsure{:|à} $X\mapsto|X|$)'),
],
17: [
 (r"Supposons $R$ muni d'une topologie, donc les", r"Supposons $R$ muni d'une topologie, \inserted{\unsure{et}} donc les"),
],
18: [],
19: [
 (r"il \unsure{faut s.} qu'elle", r"il \unsure{faut s.|f. et s.} qu'elle"),
 (r'(cela \deleted{\unsure{faut}} dans le contexte', r'(cela \unsure{vaut|\deleted{faut}|résulte} dans le contexte'),
 (r'avec $\unsure{(M1)_0|(M1)}$, $(M2)$', r'avec $(M1)_0$, $(M2)$'),
],
20: [
 (r'qui est \deleted{\unsure{esp.}} modéré', r'qui est \deleted{\unsure{cpt|esp.}} modéré'),
 (r'qui forment donc un antifiltre cofinal à celui des parties compactes.',
  r'qui forment donc un \unsure{antifiltre|ens. filtrant} cofinal : celui des parties compactes.'),
],
21: [
 (r'a) $0$ et $1$ sont $\in R_0$', r'a) $0$ \unsure{et|$\ne$} $1$ sont $\in R_0$'),
 (r'\margin{\deleted{(\unsure{NB}\ \unsure{OPS|OB}\ $B\supset A^{-1}$)}}', r'\margin{\deleted{(\unsure{OPS|OB|NB} OPS $B=A^{-1}$\,!)}}'),
 (r'\unsure{(OPS $B=A^{-1}$)}.', r'(OPS $B=A^{-1}$\,!).'),
],
22: [
 (r'(si $R$ est réunion de ses parties', r'(si $R$ est réunion \deleted{des} de ses parties'),
 (r'i.e. \inserted{les $R^I$} sont des espaces', r'i.e. \inserted{les $R^I$} \unsure{sont|\deleted{sont}} des espaces'),
 (r"inv. \unsure{(dans|dans} l'anneau", r"inv. dans l'anneau"),
 (r'$x\mapsto x^{-1}$ à $A$', r'$x\mapsto x^{-1}$ \unsure{:|à} $A$'),
],
23: [
 (r'on \unsure{gagne}, car', r'on gagne, car'),
 (r'$f_\alpha-e_\alpha$, \unsure{OPS} les', r'$f_\alpha-e_\alpha$, OPS les'),
],
24: [
 (r'Si on a M1 à \unsure{M4} et M11', r'Si on a M1 : M7 et M11'),
 (r'pour \unsure{$\forall$|tte} partie \deleted{\unsure{telle}}', r'pour $\forall$ partie \deleted{\unsure{telle|fermée}}'),
],
25: [
 (r"(Z_i)_{i\in\underbrace{\pi_0(Y\setminus Y')}_{I}}=(U_i)_{i\in I}", r"(Z_i)_{i\in}\underbrace{\pi_0(Y\setminus Y')}_{I}=(U_i)_{i\in I}"),
 (r'les $\unsure{\overline U_i|U_i}$ sont', r'les $\overline U_i$ sont'),
 (r'au dessus de $Y$ ?', r'au dessus de $Y$ \unsure{?!|??}'),
],
}

def counts(t):
    return len(re.findall(r'\\unsure\{', t)), len(re.findall(r'\\illegible\{', t))

def main():
    results = {}
    errors = []
    for n in range(7, 26):
        name = 'MPL_152+120_120_scan%03d.tex' % n
        with open(os.path.join(SRC, name), encoding='utf-8') as f:
            old = f.read()
        new = old
        for a, b in R[n]:
            k = new.count(a)
            if k != 1:
                errors.append('scan %d: %d matches for %r' % (n, k, a[:70]))
                continue
            new = new.replace(a, b)
        # brace balance check
        if new.count('{') - new.count('}') != old.count('{') - old.count('}'):
            errors.append('scan %d: brace balance changed' % n)
        results[name] = (old, new)
    if errors:
        print('\n'.join(errors)); sys.exit(1)
    os.makedirs(OUT, exist_ok=True)
    tot = [0, 0, 0, 0]
    for name, (old, new) in results.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
            f.write(new)
        u0, i0 = counts(old); u1, i1 = counts(new)
        tot = [tot[0] + u0, tot[1] + i0, tot[2] + u1, tot[3] + i1]
        print(name, 'unsure %d->%d illegible %d->%d changed=%s' % (u0, u1, i0, i1, old != new))
    print('TOTAL unsure %d->%d illegible %d->%d' % tuple([tot[0], tot[2], tot[1], tot[3]]))
    print('replacements', sum(len(v) for v in R.values()))

if __name__ == '__main__':
    main()

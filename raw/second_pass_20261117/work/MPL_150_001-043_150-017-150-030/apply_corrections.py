"""Second pass, MPL_150_001-043, scans 17-30: apply the checked corrections to the first-pass page files.

Each replacement must match the first-pass text exactly the stated number of times, or the script stops.
Reads returns/MPL_150_001-043_unzipped/pages/, writes second_pass/out/MPL_150_001-043/ (same file names).
"""
import os
import sys
import difflib

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
SRC = os.path.join(ROOT, 'returns', 'MPL_150_001-043_unzipped', 'pages')
DST = os.path.join(ROOT, 'second_pass', 'out', 'MPL_150_001-043')
NAME = 'MPL_150_001-043_150_scan%03d.tex'

CUPU = r'\arrow[u,phantom,"\cup" description]'

R = {
    17: [
        (r"(\unsure{13|12})\qquad", r"(13)\qquad"),
        (r"$\unsure{X'{}^*|X'_*}\cap E$", r"$X'{}^*\cap E$"),
        (r"\inserted{fermée} $X'$ de $X$ est", r"\inserted{fermée} $X'$ \unsure{dans|de} $X$ est"),
        (r"\margin{plutôt : \uline{transversale ?}}", r"\margin{plutôt : \uline{transversale} \unsure{?|!}}"),
        (r"On fera attention que la définition de la", r"On fera attention que la définition dans la"),
        (r"particulier de celle de la \deleted{\unsure{en}}\inserted{compatibilité}",
         r"particulier de celle dans la \deleted{\unsure{cas|en}}\inserted{compatibilité}"),
        (r"\inserted{plus exigeante : correspond au cas où on \unsure{lui demandait}",
         r"\inserted{\unsure{plus|bien} exigeante \deleted{\unsure{que}} : correspond au cas où on \unsure{lui demandait|\ldots\ devait}"),
        (r"$\bar T'\cap Y=0.\dot T'$}", r"$T'\cap Y=0.\dot T'$}"),
    ],
    18: [
        (r"$(X_i\cap\bar T=I.X_i\cap\dot T-)$", r"$(X_i\cap T=I.X_i\cap\dot T-)$"),
        (r"de $X_i\cap\bar T$, mais aussi)", r"de $X_i\cap T$, mais aussi)"),
        (r"\unsure{désir : transversalité}", r"\unsure{dire|désir} : \unsure{transversalité}"),
        (r"si $\dot T\longrightarrow Y$ est une", r"si $\dot T\unsure{-|\longrightarrow}Y$ est une"),
        (r"Revenons à $Y\subset X$", r"Revenons \unsure{à|:} $Y\subset X$"),
    ],
    19: [
        (r"de $Y$ est \deleted{globalement} loc. triviale.",
         r"de $Y$ est \unsure{\deleted{globalement}|\uline{globalement}} loc. triviale."),
        (r"\inserted{conique} $\bar T$ de $Y$ dans $X$ :", r"\inserted{conique} $T$ de $Y$ dans $X$ :"),
        (r"il est équisingulier p.r. à $(X_i)$, si $\bar T$", r"il est équisingulier p.r. à $(X_i)$, si $T$"),
        (r"l'est par rapport à $(X_i\cap\bar T\subset\bar T)_i$.", r"l'est par rapport à $(X_i\cap T\subset T)_i$."),
        (r"implique \inserted{\unsure{f ?}} que si", r"implique que si"),
        (r"\unsure{alors}, si $Y$ est connexe", r"\unsure{alors|et}, si $Y$ est connexe"),
        (r"(14)\qquad X_i\cap\bar T=\varnothing\quad\underline{\text{ou}}\quad X_i\supset Y",
         r"(14)\qquad X_i\cap\unsure{\bar T|T}=\varnothing\quad\underline{\text{ou}}\quad X_i\supset Y\ ."),
        (r"Si $\bar T$ équisingulier p.r. à $(X_i)$,", r"Si $T$ équisingulier p.r. à $(X_i)$,"),
        (r"$\lambda\bar T$ l'est strictement", r"$\lambda T$ l'est strictement"),
        (r"\deleted{\unsure{de}} $\bar T$ de $Y$ dans $X$", r"\deleted{\unsure{de}} $\unsure{\dot T|\bar T|T}$ de $Y$ dans $X$"),
        (r"auquel cas les $\lambda\bar T$", r"auquel cas les $\lambda T$"),
    ],
    20: [
        (r"\deleted{\unsure{\}}},\bar T)$ où", r"\deleted{\unsure{\}}},T)$ où"),
        (r"$\bar T$ voisinage conique de $\unsure{Y|X_i}$", r"$T$ voisinage conique de $\unsure{Y|X_i}$"),
        (r"(X^*,\dot X,(X_i^*),\unsure{Y},", r"(X^*,\dot X,(X_i^*),Y,"),
        (r"$X^*,Y$ espaces top., $\dot X,X_i^*$, parties fermées de $X$,",
         r"$X^*,Y$ espaces top., $\dot X$ et $X_i^*$, parties fermées de $X$,"),
        (r"\inserted{transversal à} $X_i$,", r"\inserted{transversal aux} $X_i$,"),
        (r"(\dot X_i)\arrow[u,hook]&", r"(\dot X_i)" + CUPU + "&"),
    ],
    21: [
        (r"Pour faire \deleted{des} intervenir", r"Pour faire des récurrences"),
        (r"\inserted{(resp. avec $\dot X$)} de", r"\inserted{(\unsure{comp.|resp.} avec $\dot X$)} (de"),
        (r"\deleted{\unsure{équitable}}\inserted{soit}",
         r"\deleted{\unsure{égalité|équitable}}\inserted{\unsure{$\subset$}}\inserted{soit}"),
    ],
    22: [
        (r"\inserted{$\bar T,\bar T'$} de $Y$ dans", r"\inserted{$T,T'$} de $Y$ dans"),
        (r"que $\lambda\bar T=\lambda'\bar T'$ (égalité", r"que $\lambda T=\lambda'T'$ (égalité"),
        ("\\margin{$\\varepsilon\\in]0,1[$, alors pour\n$\\varepsilon\\lambda\\bar T=\\varepsilon\\lambda'\\bar T'$}",
         "\\margin{donc pour $\\varepsilon\\in]0,1[$,\n$\\varepsilon\\lambda T=\\varepsilon\\lambda'T'$}"),
        (r"représenté par $\bar T$,", r"représenté par $T$,"),
        (r"compatible avec $\lambda\bar T$", r"compatible avec $\lambda T$"),
        (r"(donc aussi avec $\lambda'\bar T$", r"(donc aussi avec $\lambda'T$"),
        (r"Si $\bar T$ et $\bar T'$ sont", r"Si $T$ et $T'$ sont"),
        ("\n$\\bar T$ est\n", "\n$T$ est\n"),
        (r"ssi $\bar T'$ l'est", r"ssi $T'$ l'est"),
        (r"et celle \inserted{de}", r"et \inserted{celle} de"),
        (r"\unsure{\tilde X|\tilde X^*}", r"\tilde X^*"),
        (r"\unsure{fibrant ?|fibrant}.", r"fibrant."),
    ],
    23: [
        (r"\deleted{\unsure{Alors} Alors}", r"\deleted{\unsure{Comme} Alors}"),
        (r"\deleted{triples}\inserted{systèmes}", r"\deleted{\unsure{triples|couples}}\inserted{systèmes}"),
        (r"Il y a lieu alors de remplacer", r"Il y a lieu alors de \unsure{remplacer|compléter}"),
    ],
    24: [
        (r"X'=\operatorname{Im}\underbrace{(\widetilde X'\hookrightarrow\widetilde X\to X)}",
         r"X'=\operatorname{Im}\underbrace{(\widetilde X'\ \text{par}\ \widetilde X\to X)}"),
        (r"voisinage cylindrique de $X_0$, \unsure{et} $T$ voisinage", r"voisinage cylindrique de $X_0$, et $T$ voisinage"),
        (r"\margin{\unsure{donc} stable par", r"\margin{donc stable par"),
        (r"\overline T\cap E \arrow[u,phantom", r"\unsure{\dot T|\overline T}\cap E \arrow[u,phantom"),
        (CUPU + r" \arrow[d] &", CUPU + r" &"),
        (r"Y_0\times I &", r"Y_0\times I " + CUPU + r" &"),
    ],
    25: [
        (r"\deleted{\unsure{et où}}", r"\deleted{\unsure{et où|i.e.}}"),
        (r"\dot T_0=\dot T\cap X_0,\qquad", r"\unsure{\dot T_0|T_0}=\dot T\cap X_0,\qquad"),
        (r"\unsure{s'identifie} sur $\overline T_E$", r"\unsure{s'identifie|induite|standarde} sur $\overline T_E$"),
    ],
    26: [
        (r"les \inserted{les} $(X_0,\mathcal E)$", r"\unsure{lors|alors|les} \inserted{les} $(X_0,\mathcal E)$"),
        (r"\overset{\unsure{p|\beta}}", r"\overset{p}"),
        (r"E_{\dot X}\simeq\dot X_0\times I,\qquad", r"E_{\dot X}=\dot X_0\times I,\qquad"),
    ],
    27: [
        (r"tout $J\subset I$, $\unsure{I|J}$ fini", r"tout $J\subset I$, $I$ fini"),
        (r"est celle de $B_J\times I^J$, la $\lambda$-homothétie", r"est celle de $B_J\times I^J$, l'homothétie"),
        (r"$\dot B_J=\bigcap_{j\in J}\dot E_j", r"$\dot B_J=\bigcap_{i\in J}\dot E_{\unsure{j|i}}"),
        (r"On dit que les familles précédentes \uline{et}",
         r"On dit que \unsure{la famille précédente|les familles précédentes} \uline{et}"),
        (r"\unsure{transversaux|transverses} \deleted{compatibles}", r"transversaux \deleted{compatibles}"),
        ("\\[\nE_J\\cap T\\simeq\\overline T_J\\times I^J\n\\qquad(\\text{où }\\overline T_J=T\\cap B_J)\n\\]",
         "\\[\n\\begin{array}{l}\nE_J\\cap T\\simeq\\overline T_J\\times I^J\n\\qquad(\\text{où }\\overline T_J=T\\cap B_J)\\\\\n\\cup\n\\end{array}\n\\]"),
        (r"E_J\cap\dot T\simeq\dot T_J\times I^J", r"\unsure{\dot E_J|E_J}\cap\dot T\simeq\dot T_J\times I^J"),
    ],
    28: [
        (r"une structure cônique sur $(\overline T_J,Y_J)$, ayant", r"une structure cônique sur $(T_J,Y_J)$, ayant"),
        (r"\unsure{Relations|Relatifs} aux", r"Relations aux"),
        (r"$\forall j'\unsure{\leftrightarrow|<}j$", r"$\forall j'\leftrightarrow j$"),
        (r"$\forall i\unsure{\leftrightarrow|\le}j$", r"$\forall i\leftrightarrow j$"),
        (r"i.e. des éléments maximaux de", r"i.e. des éléments \unsure{maximaux|minimaux} de"),
        (r"et si pour $k\in I_{i,j}$, on désigne", r"et si pour \unsure{$\forall$} $k\in I_{i,j}$, on désigne"),
        (r"\deleted{l'ens des} parties $s_k\subset S$", r"\deleted{l'ens des}\inserted{la} parties $s_k\subset S$"),
        (r"$\unsure{j\ge s_k|j\ge k}$", r"$j\ge s_k$"),
        (r"l'intersection dans $X_j$\ldots", r"l'intersection \unsure{des $X_k$|dans $X_j$}\ldots"),
    ],
    29: [
        (r"mais non $\unsure{\le|<}j'$", r"mais non $\le j'$"),
        (r'\arrow[d,phantom,"{\unsure{\downarrow}}" description]',
         r'\arrow[d,phantom,"{\unsure{\downarrow|\geq}}" description]', 2),
        (r"de la forme $\mathcal P(\sigma)$,", r"de la forme $\mathcal P(\unsure{\sigma|F})$,"),
    ],
    30: [
        (r"\inserted{$X=\bigcup_{i\in I}X_i$}", r"\inserted{b) $X=\bigcup_{i\in I}X_i$}"),
        (r"cela implique qu'on a", r"cela implique que l'on a"),
        (r"Soit $I_0\subset I$ une partie de $I_0$ formée", r"Soit $I_0\subset I$ une partie de $\unsure{I_0|I}$ formée"),
        (r"$T_i$ ($i\in I_0$) mutuellement disjoints dans $X$. ---",
         r"$T_i$ ($i\in I_0$) mutuellement disjoints \unsure{dans $X$|des $X_i$}. ---"),
    ],
}


def main():
    os.makedirs(DST, exist_ok=True)
    total = 0
    for scan in range(17, 31):
        with open(os.path.join(SRC, NAME % scan), encoding='utf-8', newline='') as fh:
            old_text = fh.read()
        crlf = '\r\n' in old_text
        text = old_text
        for rep in R.get(scan, []):
            old, new = rep[0], rep[1]
            want = rep[2] if len(rep) > 2 else 1
            if crlf:
                old = old.replace('\n', '\r\n')
                new = new.replace('\n', '\r\n')
            got = text.count(old)
            if got != want:
                sys.exit('scan %d: expected %d match(es), found %d: %r' % (scan, want, got, old))
            text = text.replace(old, new)
            total += 1
        out = os.path.join(DST, NAME % scan)
        if os.path.exists(out):
            sys.exit('refusing to overwrite existing ' + out)
        with open(out, 'w', encoding='utf-8', newline='') as fh:
            fh.write(text)
        diff = [l for l in difflib.unified_diff(old_text.splitlines(), text.splitlines(), lineterm='', n=0)
                if l[:1] in '+-' and not l.startswith(('+++', '---'))]
        print('scan %03d: %d replacements, %d diff lines, crlf=%s' % (scan, len(R.get(scan, [])), len(diff), crlf))
    print('total replacements', total)


if __name__ == '__main__':
    main()

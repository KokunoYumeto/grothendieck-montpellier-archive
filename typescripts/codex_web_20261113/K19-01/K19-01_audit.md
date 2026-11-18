# Second reading

The times are UTC. The word lists were recorded from the three overlapping crops before reopening each page file. Line numbers below refer to that page’s audited LaTeX file. The formula register includes diagram cells and arrow labels. Repetitions in the index register correspond to separate written occurrences.

## Scan 2

2026-11-18T07:41:52Z to 2026-11-18T07:42:44Z

**Words and accents read before comparison**

Résolutions (acute on é), standarts / standards, foncteurs adjoints, Tapis Cartier. A very faint 9, then p, +, 14 and p. Isolated 1 low at left.

**Comparison with the page**

The pencil enlargement separates both p descenders from the numerals and the cross from the foot of 1. All three lines of the ink title survive. The final two strokes of the first adjective remain uncertain. The remaining field is blank; the lower-left 1 is the archive foliation. No cancellation or authorial page number.

**Formulas, including diagram cells and arrow labels**

Line 7, inline

~~~tex
9_{\mathrm p}+14_{\mathrm p}
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L7 · margin · `$9_{\mathrm p}+14_{\mathrm p}$`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
\unsure{9 p + 14 p}
->
$9_{\mathrm p}+14_{\mathrm p}$
~~~

## Scan 4

2026-11-18T07:42:45Z to 2026-11-18T07:47:08Z · Additional comparison 2026-11-18T08:06:31Z

**Words and accents read before comparison**

Tapis Cartier; adjoint à [droite retouché], d’où morphismes d’adjonction; On pose; On a donc; où; satisfait, conditions de Godement; unitarité, associativité, commutatif; définit, catégorie, comme formée des couples; satisfaisant les conditions de commutation; foncteur naturel; vérifier compatibilité. Endings of morphismes, conditions and naturel extend into fine horizontal strokes.

**Comparison with the page**

The line across Alors starts inside the capital and cuts the middle rather than running underneath it. In (1.8) the small boxed segment has a blunt right end. Compared it with the pointed arrow in the bottom map. Two curly braces link the renumbered rows (1.10), (1.9). The mark over X, the old numerals, the suffix on the upper arrow of (1.5), the writing under droite and the first f on the final line all have crossing strokes. The lower-right instruction ends in (1.9). The category letters A, B and K have independent pen strokes. The arrowhead at the left of the top pair belongs to g. The second brace alongside the pair of objects, independent of the one beside the equation numbers, has been drawn explicitly.

**Formulas, including diagram cells and arrow labels**

Line 5, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&]
 A \arrow[r,shift left,"f"] \& B \arrow[l,shift left,"g"]
\end{tikzcd}
~~~

Line 8, inline

~~~tex
g
~~~

Line 8, inline

~~~tex
f
~~~

Line 9, display

~~~tex
\mathrm{id}_A\xrightarrow{\beta}gf,\qquad fg\mathrel{\overset{\alpha}{\unsure{-|\to}}}\mathrm{id}_B \tag*{(1.1)}
~~~

Line 13, display

~~~tex
\varphi=fg:\ B\mathrel{\unsure{-|\to}} B \tag*{(1.2)}
~~~

Line 17, display

~~~tex
\boxed{\varphi\xrightarrow{\alpha}\mathrm{id}_B,\quad\varphi\xrightarrow{\lambda}\varphi^2} \tag*{(1.3)}
~~~

Line 21, display

~~~tex
\lambda\deleted{\unsure{=}}:fg\longrightarrow fgfg\qquad \lambda=f*\beta*g \tag*{(1.4)}
~~~

Line 24, inline

~~~tex
\varphi
~~~

Line 26, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \text{(1.5) (\uline{unitarité})} \& \varphi \arrow[r,"\lambda"] \arrow[rr,bend right=30,"\mathrm{id}_{\varphi}"'] \&
 \varphi^2 \arrow[r,shift left,"\varphi*\alpha\deleted{\unsure{*\varphi}}"] \arrow[r,shift right,"\alpha*\varphi"'] \& \varphi
\end{tikzcd}
~~~

Line 30, inline

~~~tex
(\varphi*\alpha)\circ\lambda=\mathrm{id}_{\varphi}
~~~

Line 32, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \text{(1.6) (\uline{associativité})} \& \varphi\arrow[r,"\lambda"] \& \varphi^2
 \arrow[r,shift left,"\varphi*\lambda"] \arrow[r,shift right,"\lambda*\varphi"'] \& \varphi^3
\end{tikzcd}
~~~

Line 36, inline

~~~tex
(\varphi*\lambda)\circ\lambda=(\lambda*\varphi)\circ\lambda
~~~

Line 39, display

~~~tex
K=K(\varphi,\alpha,\lambda) \tag*{(1.7)}
~~~

Line 43, display

~~~tex
(X,u)\qquad X\in\mathrm{Ob}\,B,\quad \boxed{u:X\mathrel{\unsure{-|\to}}\varphi(X)} \tag*{(1.8)}
~~~

Line 47, diagram

~~~tex
\resizebox{\linewidth}{!}{\(\left\{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=large]
 \text{(\deleted{\unsure{1.9}}1.10)} \& {}\arrow[d,phantom,"{\left\{\vphantom{\rule{0pt}{2cm}}\right.}" description] \& X\arrow[r,"u"] \& \varphi(\deleted{\unsure{Y}}X)
 \arrow[r,shift left,"\varphi(u)"] \arrow[r,shift right,"\lambda(X)"'] \& \varphi^2(X)
 \& \lambda\circ u=\varphi(u)\circ u \quad\text{``associativité''}\\
 \text{(\deleted{\unsure{1.10}}1.9)} \& {} \& X\arrow[r,"u"] \& \varphi(X)\arrow[r,"\alpha(X)"] \& X
 \& \alpha(X)\circ u=\mathrm{id}_X\quad\text{``unitarité''}
\end{tikzcd}\right.\)}
~~~

Line 55, display

~~~tex
\boxed{h:A\longrightarrow K(\varphi,\alpha,\lambda)} \tag*{(1.\unsure{11})}
~~~

Line 59, display

~~~tex
Y\longmapsto \bigl(\deleted{\unsure{f}}f(Y),\quad f(Y)\xrightarrow{f*\beta}\varphi f(Y)=fgf(Y)\bigr).
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · uline · `Tapis Cartier`
- L8 · deleted · `\unsure{gauche}`
- L22 · deleted · `\unsure{=}`
- L24 · deleted · `\unsure{Alors}`
- L24 · uline · `conditions de Godement`
- L27 · uline · `unitarité`
- L28 · deleted · `\unsure{*\varphi}`
- L33 · uline · `associativité`
- L48 · deleted · `\unsure{1.9}`
- L48 · deleted · `\unsure{Y}`
- L51 · deleted · `\unsure{1.10}`
- L60 · deleted · `\unsure{f}`
- L62 · margin · `vérifier compatibilité (1.9)`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
\unsure{Alors}
->
\deleted{\unsure{Alors}}
~~~

~~~tex
\boxed{u:X\longrightarrow\varphi(X)}
->
\boxed{u:X\mathrel{\unsure{-|\to}}\varphi(X)}
~~~

~~~tex
\diagram{\(\left\{\begin{tikzcd}
->
\diagram{\resizebox{\linewidth}{!}{\(\left\{\begin{tikzcd}
~~~

~~~tex
\unsure{1.9}}1.10)} \& X
->
\unsure{1.9}}1.10)} \& {}\arrow[d,phantom,"{\left\{\vphantom{\rule{0pt}{2cm}}\right.}" description] \& X
~~~

~~~tex
\unsure{1.10}}1.9)} \& X
->
\unsure{1.10}}1.9)} \& {} \& X
~~~

~~~tex
\end{tikzcd}\right.\)}
->
\end{tikzcd}\right.\)}}
~~~

## Scan 5

2026-11-18T07:47:08Z to 2026-11-18T07:48:06Z

**Words and accents read before comparison**

Théorème, Cartier; Si; doubles flèches, existent, y commute, alors, essentiellement surjectif; équivalence, fidèle, suffit, conservatif, exacte, soit; partir d’une catégorie; satisfaisant, conditions, sans ces restrictions, définir, ci-dessus; canonique; Question, Quand, admet-il, adjoint à droite; assurent, tout à l’heure? / tomber bien dans; évidemment. Upper left and the two lines slanting down the margin switch reading direction.

**Comparison with the page**

Read the two sloping notes with the sheet turned. The first ends in underlined existe. A separate parenthesis below it ends in a looped c/C. Two strokes underline passage au quotient in the longer note, one under each line. In the definition of g(X), the raised character has the same hook and foot as the 2 in the upper-middle display. The long question is cut through on both lines, including the underlined Question. The two Hom groups, the crossed final object and the numeral at the left belong to a second canceled block. Retained the little perpendicular strokes above its X. The surrounding et on a évidemment is below the strike.

**Formulas, including diagram cells and arrow labels**

Line 2, inline

~~~tex
A
~~~

Line 2, inline

~~~tex
\mathrm{Ker}
~~~

Line 2, inline

~~~tex
^{*}
~~~

Line 2, inline

~~~tex
f
~~~

Line 2, inline

~~~tex
(*)
~~~

Line 4, inline

~~~tex
*
~~~

Line 4, inline

~~~tex
u,v
~~~

Line 4, inline

~~~tex
\mathrm{Ker}(f(u),f(v))
~~~

Line 5, inline

~~~tex
h
~~~

Line 5, inline

~~~tex
f
~~~

Line 5, inline

~~~tex
(u,v)
~~~

Line 5, inline

~~~tex
A
~~~

Line 5, inline

~~~tex
\mathrm{Ker}(f(u),f(v))
~~~

Line 5, inline

~~~tex
\mathrm{Ker}(u,v)
~~~

Line 5, inline

~~~tex
f
~~~

Line 9, inline

~~~tex
h
~~~

Line 11, inline

~~~tex
B
~~~

Line 12, display

~~~tex
\varphi:B\mathrel{\unsure{-|\to}}B, \tag*{(2.1)}
~~~

Line 17, display

~~~tex
\varphi\mathrel{\overset{\alpha}{\unsure{-|\to}}}\mathrm{id}_B,\qquad\varphi\xrightarrow{\lambda}\varphi^2 \tag*{(2.2)}
~~~

Line 21, display

~~~tex
A=K(\varphi,\alpha,\lambda) \tag*{(2.3)}
~~~

Line 25, display

~~~tex
A\xrightarrow{f}B \tag*{(2.4)}
~~~

Line 28, inline

~~~tex
(X,u)\longmapsto X
~~~

Line 28, inline

~~~tex
f
~~~

Line 28, inline

~~~tex
g
~~~

Line 28, inline

~~~tex
\varphi\simeq fg
~~~

Line 29, display

~~~tex
g:B\longrightarrow A \tag*{(2.5)}
~~~

Line 33, display

~~~tex
g(X)=\bigl(\varphi(X),\quad\varphi(X)\xrightarrow{\lambda(X)}\varphi^{2}(X)\bigr) \tag*{(2.6)}
~~~

Line 36, inline

~~~tex
K(\varphi,\alpha,\lambda)
~~~

Line 38, display

~~~tex
\deleted{\mathrm{Hom}_A\bigl((X,u),g(Y)\bigr)\simeq\mathrm{Hom}_B\bigl(\underset{\shortparallel\,X}{f(X,u)},\unsure{Y|X}\bigr)} \tag*{\deleted{(2.7)}}
~~~

Line 42, display

~~~tex
fg=\varphi \tag*{(2.7)}
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · uline · `Théorème`
- L2 · deleted · `Supposons que`
- L2 · inserted · `a) Si`
- L2 · deleted · `que`
- L2 · inserted · `si`
- L4 · margin · `$*$ il suffit de regarder les doubles flèches $u,v$ telles que $\mathrm{Ker}(f(u),f(v))$ \uline{existe}`
- L4 · uline · `existe`
- L5 · deleted · `\unsure{et}`
- L5 · inserted · `b)`
- L5 · uline · `$h$`
- L5 · deleted · `de la forme`
- L5 · uline · `conservatif`
- L5 · inserted · `$(u,v)$`
- L5 · uline · `et`
- L7 · margin · `(condition \unsure{c|C})`
- L9 · margin · `améliorer a), en explicitant que $h$ est un \uline{passage au quotient}`
- L9 · uline · `passage au quotient`
- L15 · deleted · `satisfaisant les conditions (1.5),`
- L16 · deleted · `(2.1`
- L28 · deleted · ```de \unsure{réduction}'' \unsure{en}`
- L28 · deleted · `\uline{Question} Quand $f$ admet-il un adjoint à droite $g$, de telle façon que \unsure{l'on ait} $\varphi\simeq fg$`
- L28 · uline · `Question`
- L28 · deleted · `\unsure{objet}`
- L36 · inserted · `\textcircled{\scriptsize 1.5}`
- L37 · deleted · `Je dis qu'on a une relation d'adjonction,`
- L39 · deleted · `\mathrm{Hom}_A\bigl((X,u),g(Y)\bigr)\simeq\mathrm{Hom}_B\bigl(\underset{\shortparallel\,X}{f(X,u)},\unsure{Y|X}\bigr)`
- L39 · deleted · `(2.7)`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
$\uline{$h$}$
->
\uline{$h$}
~~~

~~~tex
\varphi^{\unsure{2}}(X)
->
\varphi^{2}(X)
~~~

~~~tex
(condition c)
->
(condition \unsure{c|C})
~~~

## Scan 6

2026-11-18T07:48:06Z to 2026-11-18T07:49:57Z

**Words and accents read before comparison**

Considérons alors, fournit, homomorphisme d’adjonction, définir aussi, en posant, tt; commutativité étant assurée par la condition, sur les objets; vérifie, inverses l’un de l’autre, En effet, résulte facilement, de; canceled identité and séquence. Donc, adjoints, redonnent, bien sûr/sur, par la formule du N°1; foncteur, conservatif, satisfait.

**Comparison with the page**

In the canceled (2.9′), the open loop beside alpha is on the baseline. It is the composition sign. There is no detached prime there. The small letters before Y share an ascending stroke and crossbar (tt). In the square the u marked at the left points down and the right edge is dotted. The raised 2 stands above the second phi, distinct from its argument. The side mark near the top Y is faint. The circled references have overlapping numerals. Below them the long crossing lines continue through the X → φ(X) → X diagram, the words l’identité and the calculations, stopping above Donc. The last open mark has a detached short lower stroke. The underlined procédé has a rising last accent.

**Formulas, including diagram cells and arrow labels**

Line 3, display

~~~tex
fg\xrightarrow{\alpha}\mathrm{id} \tag*{(2.8)}
~~~

Line 7, display

~~~tex
\begin{aligned}
 &\inserted{v\longmapsto\alpha\deleted{\unsure{(Y)}}\circ f(v):}\\
 &\deleted{\unsure{\mathrm{Hom}(fX,Y)\longleftarrow}}\alpha':\mathrm{Hom}_A(X,g(Y))\longrightarrow\mathrm{Hom}_B(f(X),Y)
 \end{aligned} \tag*{(2.9)}
~~~

Line 14, display

~~~tex
\deleted{v\longmapsto\alpha\circ f(\unsure{u|v})} \tag*{\deleted{(2.9')}}
~~~

Line 17, display

~~~tex
\deleted{\unsure{g}}\beta:\mathrm{id}_K\longrightarrow gf \tag*{(2.\deleted{\unsure{9}}10)}
~~~

Line 20, inline

~~~tex
Y=(X,u)
~~~

Line 20, inline

~~~tex
K
~~~

Line 21, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&]
 X\arrow[r,"u"]\arrow[d,"u"'] \& \varphi(X)\arrow[d,dashed,"\varphi(u)"] \& \unsure{\leftarrow}Y,\\
 \varphi(X)\arrow[r,"\lambda(X)"'] \& \varphi^2(X) \& g\deleted{\unsure{g}}f(Y)
\end{tikzcd}
~~~

Line 25, inline

~~~tex
K
~~~

Line 26, display

~~~tex
\beta':\mathrm{Hom}_B(fX,Y)\longrightarrow\mathrm{Hom}_A(X,g(Y))
 \qquad v\longmapsto g(v)\circ\beta(X) \tag*{(2.11)}
~~~

Line 30, inline

~~~tex
\beta'\alpha'=\mathrm{id}
~~~

Line 30, inline

~~~tex
\alpha'\beta=\mathrm{id}
~~~

Line 31, inline

~~~tex
(X,u)
~~~

Line 31, inline

~~~tex
A
~~~

Line 32, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&,every arrow/.append style={dash pattern=on 2pt off 0pt}]
 \deleted{X}\arrow[r,"{\deleted{u}}"] \& \deleted{\varphi(X)}\arrow[r,"{\deleted{\alpha(X)}}"] \& \deleted{X}
\end{tikzcd}
~~~

Line 35, inline

~~~tex
u=\mathrm{id}_{\varphi(X)}u
 \overset{1.5}{=}\varphi(\alpha(X))\lambda(X)u\overset{1.9}{=}\varphi(\alpha(X))\varphi(u)u
 =\varphi(\alpha(X)u)
~~~

Line 37, inline

~~~tex
\varphi(u)\circ u=\lambda(X)\circ u:X\longrightarrow\varphi^2(X)
~~~

Line 38, inline

~~~tex
\lambda(X)
~~~

Line 39, inline

~~~tex
\underbrace{\lambda(X)\varphi(u)}\circ u=\underbrace{\lambda(X)\lambda(X)}u
~~~

Line 41, inline

~~~tex
f
~~~

Line 41, inline

~~~tex
g
~~~

Line 41, inline

~~~tex
(\varphi,\alpha,\lambda)
~~~

Line 43, inline

~~~tex
f
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L9 · inserted · `v\longmapsto\alpha\deleted{\unsure{(Y)}}\circ f(v):`
- L9 · deleted · `\unsure{(Y)}`
- L10 · deleted · `\unsure{\mathrm{Hom}(fX,Y)\longleftarrow}`
- L13 · deleted · `\unsure{par}`
- L15 · deleted · `v\longmapsto\alpha\circ f(\unsure{u|v})`
- L15 · deleted · `(2.9')`
- L18 · deleted · `\unsure{g}`
- L18 · deleted · `\unsure{9}`
- L23 · deleted · `\unsure{g}`
- L25 · uuline · `condition`
- L25 · deleted · `\unsure{9}`
- L30 · uline · `inverses l'un de l'autre`
- L30 · inserted · `résulte de \textcircled{\scriptsize (1.\deleted{\unsure{10}}9)}.`
- L30 · deleted · `\unsure{10}`
- L31 · deleted · `équivaut à ceci : Pour \unsure{tout} objet $(X,u)$ de $A$, le composé`
- L33 · deleted · `X`
- L33 · deleted · `u`
- L33 · deleted · `\varphi(X)`
- L33 · deleted · `\alpha(X)`
- L33 · deleted · `X`
- L35 · deleted · `est \uline{l'identité}. Or \unsure{on a} (1.9) $u=\mathrm{id}_{\varphi(X)}u \overset{1.5}{=}\varphi(\alpha(X))\lambda(X)u\overset{1.9}{=}\varphi(\alpha(X))\varphi(u)u =\varphi(\alpha(X)u)$ et (1.5) $\varphi(u)\circ u=\lambda(X)\circ u:X\longrightarrow\varphi^2(X)$ d'où, en composant à gauche avec $\lambda(X)$ $\underbrace{\lambda(X)\varphi(u)}\circ u=\underbrace{\lambda(X)\lambda(X)}u$`
- L35 · uline · `l'identité`
- L41 · uline · `redonnent bien sûr`
- L41 · deleted · `\unsure{par le}`
- L41 · uline · `par le procédé du`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
v\longmapsto\alpha'\circ f(\unsure{u|v})
->
v\longmapsto\alpha\circ f(\unsure{u|v})
~~~

~~~tex
\unsure{par} prenant, pour \unsure{le|tt}
->
\unsure{par|en} \unsure{prenant|posant}, pour tt
~~~

~~~tex
\unsure{c|e} \ldots
->
\unsure{?|c|e} \ldots
~~~

## Scan 7

2026-11-18T07:49:57Z to 2026-11-18T07:51:19Z

**Words and accents read before comparison**

Conclusion; donnée (pour B fixé), catégorie, couple, adjoint, conservatif, satisfaisant la condition C de 1.12, équivalent essentiellement à, données de Godement; Corollaire, pleinement fidèle, ssi, iso; Compléments sur propriétés d’exactitude; représentables, représentables dans B, commute, crée; limites written lim with two orientations of arrow; exactitude est vraie, Ex., propriétés d’exactitude; Théorème, Supposons, topos, morphisme, surjectif? / conservatif, exact à gauche et accessible, essentiel, produits infinis, adjoint à gauche.

**Comparison with the page**

Read the oblique note after rotation. A long descending stroke cuts the first version beginning Si de plus. There is a lower horizontal cancellation just after les couples, and a surrounding bracket. In the corollary, f has the lower hook of the f in conservatif, while the upper edge of the line cancels the preceding De plus. After the boxed equivalence, a small bracketed abbreviation sits above a separate alors. In a) arrows under lim run left. In b) they run right. In c) the left limit has J below and the right one I. Lower left vertical ruling beside the theorem does not cross its text; the struck phrase after phi lies beneath the insertion. A second numeral before Théorème is blotted.

**Formulas, including diagram cells and arrow labels**

Line 2, inline

~~~tex
B
~~~

Line 2, inline

~~~tex
A
~~~

Line 2, inline

~~~tex
f,g
~~~

Line 3, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&] A\arrow[r,shift left,"f"] \& B\arrow[l,shift left,"g"]\end{tikzcd}
~~~

Line 4, inline

~~~tex
f
~~~

Line 4, inline

~~~tex
\varphi
~~~

Line 4, inline

~~~tex
B
~~~

Line 4, inline

~~~tex
\alpha,\lambda
~~~

Line 6, inline

~~~tex
f
~~~

Line 6, inline

~~~tex
\alpha
~~~

Line 8, inline

~~~tex
f
~~~

Line 9, inline

~~~tex
\alpha*\varphi\text{ isom}\Longleftrightarrow\lambda\text{ isom}
~~~

Line 9, inline

~~~tex
\lambda
~~~

Line 9, inline

~~~tex
\alpha
~~~

Line 13, inline

~~~tex
(f,g)
~~~

Line 13, inline

~~~tex
\exists
~~~

Line 13, inline

~~~tex
B
~~~

Line 13, inline

~~~tex
f
~~~

Line 15, inline

~~~tex
\varprojlim
~~~

Line 15, inline

~~~tex
B
~~~

Line 15, inline

~~~tex
\varphi
~~~

Line 15, inline

~~~tex
\varprojlim
~~~

Line 15, inline

~~~tex
A
~~~

Line 15, inline

~~~tex
f
~~~

Line 15, inline

~~~tex
\varphi
~~~

Line 17, inline

~~~tex
\varinjlim
~~~

Line 17, inline

~~~tex
B
~~~

Line 17, inline

~~~tex
A
~~~

Line 17, inline

~~~tex
f
~~~

Line 17, inline

~~~tex
\underline{\varinjlim}
~~~

Line 19, inline

~~~tex
B
~~~

Line 19, inline

~~~tex
\varprojlim_J
~~~

Line 19, inline

~~~tex
J
~~~

Line 19, inline

~~~tex
\varinjlim_I
~~~

Line 19, inline

~~~tex
\lim
~~~

Line 19, inline

~~~tex
B
~~~

Line 19, inline

~~~tex
\varphi
~~~

Line 19, inline

~~~tex
\varprojlim_J
~~~

Line 19, inline

~~~tex
A
~~~

Line 21, inline

~~~tex
B
~~~

Line 21, inline

~~~tex
(B_k)
~~~

Line 23, inline

~~~tex
B
~~~

Line 23, inline

~~~tex
A
~~~

Line 23, inline

~~~tex
f
~~~

Line 23, inline

~~~tex
f_0^*
~~~

Line 23, inline

~~~tex
B\longrightarrow A
~~~

Line 23, inline

~~~tex
\varphi
~~~

Line 23, inline

~~~tex
\varprojlim
~~~

Line 23, inline

~~~tex
f_0
~~~

Line 23, inline

~~~tex
\varphi
~~~

Line 23, inline

~~~tex
\varprojlim
~~~

Line 23, inline

~~~tex
\varphi
~~~

Line 23, inline

~~~tex
\psi
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · uline · `Conclusion`
- L4 · uline · `conservatif`
- L4 · deleted · `tel que, \unsure{pour les}`
- L4 · deleted · `commutant aux noyaux de doubles \unsure{doubles} flèches`
- L6 · deleted · `De plus, $f$ est pleinement fidèle ssi $\alpha$ est un isomorphisme,`
- L8 · uline · `Corollaire`
- L8 · deleted · `\unsure{\Longleftrightarrow}`
- L11 · uline · `Compléments sur propriétés d'exactitude`
- L13 · margin · `\deleted{Si de plus les \unsure{noyaux}} \uline{Pour} les couples $(f,g)$ \deleted{\unsure{de foncteurs}} adjoints, où \unsure{$\exists$ ds $B$} les Ker \unsure{resp.}, $f$ conservatif et commute aux Ker`
- L13 · deleted · `Si de plus les \unsure{noyaux}`
- L13 · uline · `Pour`
- L13 · deleted · `\unsure{de foncteurs}`
- L15 · deleted · `et auxquelles $\varphi$ commute,`
- L15 · deleted · `existent`
- L15 · inserted · `si et seulement si $\varphi$ y commute.`
- L17 · uline · `toutes`
- L19 · deleted · `\unsure{faisant}`
- L19 · deleted · `de type $J$`
- L19 · deleted · `\unsure{typ.}`
- L19 · uline · `Ex.`
- L21 · deleted · `d) Supposons que $B$ soit une \unsure{filtration} \inserted{du topos} \unsure{continue} $(B_k)$,`
- L21 · inserted · `du topos`
- L22 · deleted · `\unsure{d)}`
- L23 · uline · `Théorème`
- L23 · deleted · `commute aux \unsure{$\varprojlim$}`
- L23 · inserted · `est exact à gauche \uline{et accessible}`
- L23 · uline · `et accessible`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
condition \unsure{c|e}
->
condition \unsure{C|c|e}
~~~

~~~tex
[\unsure{alrs} $\lambda$
->
[\unsure{alrs|NB} alors $\lambda$
~~~

~~~tex
$(f,g)$ de \unsure{foncteurs} adjoints
->
$(f,g)$ \deleted{\unsure{de foncteurs}} adjoints
~~~

## Scan 8

2026-11-18T07:51:20Z to 2026-11-18T07:52:33Z

**Words and accents read before comparison**

Supposons; Donc f est donné par une famille de; connu quand on connaît les adjoints; Le composé, alors, une liaison; est connu quand on connaît; On trouve; Soit; et supposons, commutent aux produits; du type I (p. ex. f_j exact à g. et I fini). On a alors; les données, reviennent à celles de; i.e. Look especially at the 2 diagrams of a phi with a barred Greek letter and the double-index below lambda.

**Comparison with the page**

The upper g_i and f_i take a dotted short i. The projection in the middle is pr_j, with a descender. For (3.5) read pr_j, X_i, f_j, i∈I, g_i, X_i in sequence. The two appearances of (3.6) both finish as a looped 6. Their factor order is f_j g_i then φ_ji(X_i), with the j descending in φ. The first (3.8) has overwritten indices on the left and under the right product. The terminal line has α below the product, kα on φ, α on X, and k,j,i under the barred λ. The right side reads kj, ji, i in order. The two lines with ∏ B_i have no added index under a product unless one is visible. The proposed hom has one initial tall stroke and scant ink to distinguish its trailing stop.

**Formulas, including diagram cells and arrow labels**

Line 3, display

~~~tex
\boxed{B=\prod_{i\in I}B_i}. \tag*{(3.1)}
~~~

Line 6, inline

~~~tex
f
~~~

Line 7, display

~~~tex
f_i:A\longrightarrow B_i \tag*{(3.2)}
~~~

Line 10, inline

~~~tex
g
~~~

Line 11, display

~~~tex
g_i:B_i\longrightarrow A, \tag*{(3.3)}
~~~

Line 15, display

~~~tex
g\bigl((X_i)_{i\in I}\bigr)=\prod_{i\in I}g_i(X_i) \tag*{(3.4)}
~~~

Line 18, inline

~~~tex
\varphi=fg
~~~

Line 19, display

~~~tex
\varphi:\prod B_i\longrightarrow\prod B_i
~~~

Line 23, display

~~~tex
\mathrm{pr}_{j}\,\varphi:\prod_i B_i\mathrel{\unsure{-|\to}}B_j
~~~

Line 27, display

~~~tex
\mathrm{pr}_j\,\varphi((X_i))=f_j\left(\prod_{i\in I}g_i(X_i)\right). \tag*{(3.5)}
~~~

Line 31, display

~~~tex
\varphi_{ji}\overset{\text{déf}}{=}f_jg_i\deleted{\unsure{g_j f_i}}:\ B_i\longrightarrow B_j \tag*{(3.6)}
~~~

Line 34, inline

~~~tex
f_j
~~~

Line 34, inline

~~~tex
I
~~~

Line 34, inline

~~~tex
f_j
~~~

Line 34, inline

~~~tex
I
~~~

Line 35, display

~~~tex
\mathrm{pr}_j\,\varphi((X_i))\simeq\prod_{i\in I}\varphi_{ji}(X_i) \tag*{(3.6)}
~~~

Line 38, inline

~~~tex
\alpha,\lambda
~~~

Line 39, display

~~~tex
\prod_i\varphi_{ki}(X_i)\xrightarrow{\bar\alpha_{\deleted{\unsure{j}}k}}X_{\deleted{\unsure{j}}k} \tag*{(3.7)}
~~~

Line 42, display

~~~tex
\prod_i\varphi_{\deleted{\unsure{j}}ki}(X_i)\xrightarrow{\bar\lambda_k}
 \prod_{\deleted{\unsure{j}}i,j}\varphi_{kj}\varphi_{ji}(X_i) \tag*{(3.8)}
~~~

Line 47, display

~~~tex
\prod_\alpha\varphi_{k\alpha}(X_\alpha)\xrightarrow{\bar\lambda_{k,j,i}}\varphi_{kj}\varphi_{ji}(X_i)
~~~

**Indices and exponents containing i or j**

L4 `_{i\in I}`, L4 `_i`, L8 `_i`, L8 `_i`, L12 `_i`, L12 `_i`, L16 `_i`, L16 `_{i\in I}`, L16 `_{i\in I}`, L16 `_i`, L16 `_i`, L20 `_i`, L20 `_i`, L24 `_{j}`, L24 `_i`, L24 `_i`, L24 `_j`, L28 `_j`, L28 `_i`, L28 `_j`, L28 `_{i\in I}`, L28 `_i`, L28 `_i`, L32 `_{ji}`, L32 `_j`, L32 `_i`, L32 `_j`, L32 `_i`, L32 `_i`, L32 `_j`, L34 `_j`, L34 `_j`, L36 `_j`, L36 `_i`, L36 `_{i\in I}`, L36 `_{ji}`, L36 `_i`, L40 `_i`, L40 `_{ki}`, L40 `_i`, L43 `_i`, L43 `_i`, L44 `_{kj}`, L44 `_{ji}`, L44 `_i`, L48 `_{k,j,i}`, L48 `_{kj}`, L48 `_{ji}`, L48 `_i`.

**Cancellations, insertions, marginalia and underlining**

- L32 · deleted · `\unsure{g_j f_i}`
- L40 · deleted · `\unsure{j}`
- L40 · deleted · `\unsure{j}`
- L43 · deleted · `\unsure{j}`
- L44 · deleted · `\unsure{j}`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
un \unsure{hom}
->
un \unsure{hom|hom.}
~~~

## Scan 9

2026-11-18T07:52:34Z to 2026-11-18T07:54:09Z

**Words and accents read before comparison**

qui s’expliquent/s’explicitent, en termes des, correspondants, ainsi; sont reliés par des conditions exprimant, qui vont s’expliciter par, en les plus intéressants, celui où, sont des isom., les g_i plt fidèles; Dans ce cas, on peut supposer; On constate (!), dans les cas où deux indices … sont égaux, de sorte que l’un des facteurs … est l’identité, on trouve … l’identité; à examiner, distincts. A separate small bracketed writing says Pour i=j=k. Left sloping note starts notamment.

**Comparison with the page**

Turned the left note and read the indices i,j,k, then kji below λ and i below the final λ. In (3.9) k/k/k are above the k,j,i row; the right projection on the second line has short i. Two short parallel ticks sit under each side of (3.10); the arrow beneath the underbrace points upwards from id towards the middle g_j f_j. In the line following the box the sole stroke at the foot of φ looks i, whereas λ has three strokes with a central descender. In (3.11b) it is i=k≠j, with ij followed by ji. The addition consécutifs is above the line, and the scribbled initial letter in the smaller Pour note is distinct from the following live i=j=k. The word underlined on the right is identité. Four separate rule strokes end this page.

**Formulas, including diagram cells and arrow labels**

Line 2, inline

~~~tex
\varphi_i=f_i g_i
~~~

Line 2, inline

~~~tex
\alpha_i,\lambda_i
~~~

Line 3, display

~~~tex
\left\{\begin{aligned}
 \bar\alpha_k&=\alpha_k(X_k)\circ\mathrm{pr}_k\\
 \bar\lambda_{k,j,i}&=\lambda_{kji}(X_i)\circ\mathrm{pr}_i
 \end{aligned}\right. \tag*{(3.9)}
~~~

Line 9, diagram

~~~tex
\((3.10)\quad\boxed{\begin{tikzcd}[ampersand replacement=\&,column sep=1.3em,row sep=.25em]
 \lambda_{kji}: \& \varphi_{ki}\arrow[r] \& \varphi_{kj}\circ\varphi_{ji}\\
 \& \shortparallel \& \shortparallel\\
 \& f_k g_i \& f_k\underbrace{g_j f_j}g_i\\
 \& \& \mathrm{id}\arrow[u]
 \end{tikzcd}}\)
~~~

Line 15, inline

~~~tex
(\varphi_i,\lambda_{ijk})
~~~

Line 15, inline

~~~tex
i=j=k
~~~

Line 15, inline

~~~tex
\lambda_{kji}
~~~

Line 15, inline

~~~tex
\lambda_i
~~~

Line 15, inline

~~~tex
\varphi_i
~~~

Line 15, inline

~~~tex
\alpha_i
~~~

Line 15, inline

~~~tex
g_i
~~~

Line 17, inline

~~~tex
i,j,k
~~~

Line 17, inline

~~~tex
\lambda_{kji}
~~~

Line 17, inline

~~~tex
\lambda_i
~~~

Line 19, inline

~~~tex
\varphi_i=\mathrm{id}_{B_i}
~~~

Line 19, inline

~~~tex
\alpha_i=\mathrm{id}_{\mathrm{id}_{B_i}}
~~~

Line 19, inline

~~~tex
\lambda_i=\mathrm{id}
~~~

Line 19, inline

~~~tex
i,j,k
~~~

Line 19, inline

~~~tex
i=j
~~~

Line 19, inline

~~~tex
j=k
~~~

Line 19, inline

~~~tex
\varphi_{kj}\varphi_{ji}
~~~

Line 19, inline

~~~tex
\lambda_{kji}
~~~

Line 22, display

~~~tex
\left\{\begin{aligned}
 \text{a)}\ &\deleted{\unsure{i\ne j,\ j\ne k,\ i\ne{}}}\quad i,j,k\ \text{tous différents}\\
 \text{b)}\ &i=k\ne j\qquad\mathrm{id}_{B_i}\longrightarrow\varphi_{ij}\circ\varphi_{ji}\qquad(i\ne j)
 \end{aligned}\right. \tag*{(3.11)}
~~~

**Indices and exponents containing i or j**

L2 `_i`, L2 `_i`, L2 `_i`, L2 `_i`, L2 `_i`, L6 `_{k,j,i}`, L6 `_{kji}`, L6 `_i`, L6 `_i`, L10 `_{kji}`, L10 `_{ki}`, L10 `_{kj}`, L10 `_{ji}`, L12 `_i`, L12 `_j`, L12 `_j`, L12 `_i`, L15 `_i`, L15 `_{ijk}`, L15 `_{kji}`, L15 `_i`, L15 `_i`, L15 `_i`, L15 `_i`, L17 `_{kji}`, L17 `_i`, L19 `_i`, L19 `_{B_i}`, L19 `_i`, L19 `_{\mathrm{id}_{B_i}}`, L19 `_i`, L19 `_{kj}`, L19 `_{ji}`, L19 `_{kji}`, L25 `_{B_i}`, L25 `_{ij}`, L25 `_{ji}`.

**Cancellations, insertions, marginalia and underlining**

- L15 · inserted · `Pour \deleted{\unsure{k}}$i=j=k$, $\lambda_{kji}$ n'est autre que $\lambda_i$.`
- L15 · deleted · `\unsure{k}`
- L15 · deleted · `\unsure{$\varphi_i$}`
- L17 · margin · `notons que si deux des indices $i,j,k$ coïncident, alors $\lambda_{kji}$ est trivialement donné en termes des $\lambda_i$ --`
- L19 · deleted · `il est`
- L19 · inserted · `dans`
- L19 · inserted · `consécutifs`
- L19 · inserted · `$\lambda_{kji}$`
- L19 · uline · `identité`
- L24 · deleted · `\unsure{i\ne j,\ j\ne k,\ i\ne{}}`
- L28 · deleted · `Si \unsure{nous}`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
\[
 \boxed{\begin{aligned}
 \lambda_{kji}:{}&\varphi_{ki}\longrightarrow\varphi_{kj}\circ\varphi_{ji}\\[-2pt]
 &\phantom{\varphi_{ki}}\llap{\(\shortparallel\)}\hspace{3.7em}\shortparallel\\[-2pt]
 &f_k g_i\hspace{2em} f_k\underbrace{g_jf_j}_{\substack{\uparrow\\\mathrm{id}}}g_i
 \end{aligned}} \tag*{(3.10)}
\]
->
\diagram{\((3.10)\quad\boxed{\begin{tikzcd}[ampersand replacement=\&,column sep=1.3em,row sep=.25em]
 \lambda_{kji}: \& \varphi_{ki}\arrow[r] \& \varphi_{kj}\circ\varphi_{ji}\\
 \& \shortparallel \& \shortparallel\\
 \& f_k g_i \& f_k\underbrace{g_j f_j}g_i\\
 \& \& \mathrm{id}\arrow[u]
 \end{tikzcd}}\)}
~~~

~~~tex
\unsure{pl} fidèles
->
\unsure{pl|plt} fidèles
~~~

## Scan 10

2026-11-18T07:54:10Z to 2026-11-18T07:55:19Z

**Words and accents read before comparison**

avec les conditions, qu’on n’explicite pas; Prenons le cas, alors les données sont, si on pose maintenant, Supposons de plus, pl. fidèles; est connu quand on connaît; la donnée, revient à celle des; huit, triviaux, donc restent 6 non triviaux; on peut se présenter, Il reste donc des données; Il faudrait encore … expliciter dans ce cas les conditions, sont égaux ?; cf. 1.5 semble OK.; Par contre, il semble que …; Explicitons la catégorie A en termes de, Elle est formée des couples, définissons. Compare the little primes on both sides of each long product.

**Comparison with the page**

The first two B subscripts differ in the density of added pen strokes, and the prime after the first B is not a secure count. The little word group after supposons has a descending stroke on the left. In the lowest tuple, the second letter has a closed small oval and right branch; the first has crossed strokes. Put alpha first for the second. The two arrows in the right third are parallel and point right, with sont égaux ? pointing to the pair. In the huge canceled computation each of (3.10) and (3.11), the pair of component arrows, the stray X below, and the sentence about eight λ’s is crossed through. Verified the prime counts in both rows of (3.14) and (3.15), the prime of each starred map in the lower box, and the two crossed phi-like traces. The cf. 1.5 note is separate and slants upward slightly.

**Formulas, including diagram cells and arrow labels**

Line 4, inline

~~~tex
B=B'\times B''
~~~

Line 4, inline

~~~tex
f=(f',f'')
~~~

Line 4, inline

~~~tex
g(X',X'')=g'(X')\times g''(X'')
~~~

Line 4, inline

~~~tex
\alpha
~~~

Line 4, inline

~~~tex
f'g'\simeq\mathrm{id}_{B^{\unsure{''|'}}}
~~~

Line 4, inline

~~~tex
f'g'
~~~

Line 4, inline

~~~tex
f''g''\simeq\mathrm{id}_{B''}
~~~

Line 4, inline

~~~tex
g',g''
~~~

Line 4, inline

~~~tex
\varphi
~~~

Line 5, display

~~~tex
\boxed{\varphi'':B'\longrightarrow B'',\qquad \varphi':B''\mathrel{\unsure{-|\to}}B'} \tag*{(3.13)}
~~~

Line 8, inline

~~~tex
\alpha
~~~

Line 8, inline

~~~tex
\lambda_{kji}
~~~

Line 9, display

~~~tex
\deleted{X'\times\varphi'(\deleted{\unsure{B}}X'')\longrightarrow X'} \tag*{\deleted{(3.10)}}
~~~

Line 12, display

~~~tex
\deleted{\varphi''(X')\times X''\longrightarrow X''} \tag*{\deleted{(3.11)}}
~~~

Line 15, display

~~~tex
\deleted{\left\{\begin{aligned}
 X'&\longrightarrow\varphi'\varphi''(X')\qquad X''\mathrel{\unsure{-|\to}}\varphi''\varphi'(X'')\\
 &\unsure{X'}
 \end{aligned}\right.}
~~~

Line 21, inline

~~~tex
\lambda_{kji}
~~~

Line 21, inline

~~~tex
2^3
~~~

Line 21, inline

~~~tex
i=j=k
~~~

Line 21, inline

~~~tex
\lambda_{1,1,2}:
~~~

Line 22, display

~~~tex
\boxed{\left\{\begin{aligned}
 \mathrm{id}_{B'}&\xrightarrow{\lambda'}\varphi'\varphi''\\
 \mathrm{id}_{B''}&\xrightarrow{\lambda''}\varphi''\varphi'
 \end{aligned}\right.} \tag*{(3.14)}
~~~

Line 30, diagram

~~~tex
\resizebox{\linewidth}{!}{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \varphi(X',X'')\arrow[r,"\lambda"] \& \varphi^2(X',X'')\arrow[r,shift left,"\text{sont égaux ?}"]\arrow[r,shift right] \& \varphi(X',X'')\\[-8pt]
 \shortparallel \& \shortparallel \& \shortparallel\\[-8pt]
 (X'\times\varphi'(X''),X''\times\varphi''(X'))\arrow[r] \&
 \begin{gathered}\bigl(X'\times\varphi'(X'')\times\varphi'(X'')\times\varphi'\varphi''X',\\[-2pt]
 X''\times\varphi''(X')\times\varphi''(X')\times\varphi''\varphi'(X'')\bigr)\end{gathered} \&
 \begin{gathered}(X'\times\varphi'(X''),\\ X''\times\varphi''(X'))\end{gathered}
\end{tikzcd}}
~~~

Line 39, inline

~~~tex
\lambda',\lambda''
~~~

Line 41, display

~~~tex
\boxed{\begin{aligned}
 \varphi''*\lambda'&=\deleted{\unsure{\varphi}}\lambda''*\varphi'':\varphi''\longrightarrow\varphi''\varphi'\varphi''\,;\\
 \lambda'*\varphi'&=\varphi'*\lambda'':\varphi'\deleted{\unsure{\varphi}}\longrightarrow\varphi'\varphi''\varphi'
 \end{aligned}}
~~~

Line 47, inline

~~~tex
A
~~~

Line 47, inline

~~~tex
\varphi',\varphi'',\lambda',\lambda''
~~~

Line 49, inline

~~~tex
(X',\unsure{\alpha''|X''},u',u'')
~~~

Line 50, display

~~~tex
X'\xrightarrow{u'}\varphi'(X''),\qquad X''\xrightarrow{u''}\varphi''(X') \tag*{(3.15)}
~~~

Line 53, inline

~~~tex
X'\xrightarrow{\unsure{u'}}
~~~

**Indices and exponents containing i or j**

L8 `_{kji}`, L21 `_{kji}`.

**Cancellations, insertions, marginalia and underlining**

- L2 · deleted · `avec des conditions (1.5) (1.6) qu'on n'explicite pas.`
- L4 · deleted · `alors les données sont, si on pose concernant $\alpha$`
- L4 · deleted · `\unsure{$f'g'$}`
- L8 · deleted · `et la donnée des $\alpha$ \unsure{revient à} $\lambda_{kji}$ revient à celle des`
- L10 · deleted · `X'\times\varphi'(\deleted{\unsure{B}}X'')\longrightarrow X'`
- L10 · deleted · `\unsure{B}`
- L10 · deleted · `(3.10)`
- L13 · deleted · `\varphi''(X')\times X''\longrightarrow X''`
- L13 · deleted · `(3.11)`
- L16 · deleted · `\left\{\begin{aligned} X'&\longrightarrow\varphi'\varphi''(X')\qquad X''\mathrel{\unsure{-|\to}}\varphi''\varphi'(X'')\\ &\unsure{X'} \end{aligned}\right.`
- L21 · deleted · `Il y a huit $\lambda_{kji}$ ($2^3$), dont deux triviaux ($i=j=k$), donc reste 6 non triviaux $\lambda_{1,1,2}:$`
- L28 · deleted · `vérifier`
- L38 · margin · `cf. 1.5 semble O.K.`
- L39 · deleted · `Par contre, il semble que 1.6 impose des restrictions à $\lambda',\lambda''$`
- L40 · deleted · `\unsure{ne}`
- L40 · deleted · `pas`
- L40 · deleted · `pas`
- L43 · deleted · `\unsure{\varphi}`
- L44 · deleted · `\unsure{\varphi}`
- L53 · deleted · `$X'\xrightarrow{\unsure{u'}}$`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
supposons que $f'g'
->
supposons \unsure{que|de plus} $f'g'
~~~

~~~tex
\unsure{X''|\alpha''}
->
\unsure{\alpha''|X''}
~~~

~~~tex
X''\mathrel{-}\varphi''\varphi'
->
X''\mathrel{\unsure{-|\to}}\varphi''\varphi'
~~~

## Scan 11

2026-11-18T07:55:19Z to 2026-11-18T07:56:33Z · Additional comparison 2026-11-18T08:06:31Z

**Words and accents read before comparison**

soumis aux conditions; définissant … ce qui exprime déjà (1.9), soumises / soumis à la condition de commutativité de (1.10). via, can; Il semble qu’on trouve la commutativité des diagrammes; Exemple, Si … sont des foncteurs constants de valeur un objet final de B′ resp. B″, les conditions … sont oiseuses/vides, et on trouve simplement …; Image ess. de, un isom. Bottom two lines mark u double-prime then u single-prime.

**Comparison with the page**

At the top right of the long diagram, part of the last factor runs to the edge. The preceding X argument has at least one raised stroke. Above the parallel arrows φ is clear but the small line after it has no securely separated letters. Both arrows have a pointed right end, with a small trace also at the left of the upper one. In (3.16), the first curved arrow is λ′(X′), and the second has double primes on both λ and X. The two central labels use the opposite prime on u. The stroke through the first attempt below the long diagram spans its outgoing arrow. The adjective after sont in the example reads vides (a dot and d loop). In 3.17, the top projection has a short bar at its tail; the second has none. 3.18 has double prime on u opposite g′ and single prime opposite g″. The isolated bottom-left perpendicular-like stroke stands apart from the sheet number. The long brace grouping the projection maps and both right adjoints has been sized to the line.

**Formulas, including diagram cells and arrow labels**

Line 4, inline

~~~tex
X'\longleftarrow(\mathrm{id}_{X'}
~~~

Line 4, inline

~~~tex
X'\xrightarrow{(\mathrm{id}_{X'},u')}X'\times\varphi'(X'')
~~~

Line 4, inline

~~~tex
X''\xrightarrow{(\mathrm{id}_{X''},u'')} \deleted{\unsure{X'}}X''\times\varphi''(X')
~~~

Line 5, diagram

~~~tex
\resizebox{\linewidth}{!}{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
 (X',X'')\arrow[r,"*","{\text{via }u',u''}"'] \&
 (X'\times\varphi'(X''),X''\times\varphi''(X'))\arrow[r,shift left,"{\varphi\,\unsure{(u)|(*)|\text{de }*}}"]\arrow[r,shift right,"{\substack{\text{can}\\\text{via }\lambda',\lambda''}}"'] \&
 \begin{gathered}\bigl(X'\times\varphi'(X'')\times\varphi'(X'')\times\varphi'\varphi''(X'),\\
 X''\times\varphi''(X')\times\varphi''(\unsure{X'|X''})\times\varphi''\varphi'(X'')\bigr)\end{gathered}
\end{tikzcd}}
~~~

Line 11, display

~~~tex
\deleted{\unsure{X'}\quad X'\xrightarrow{\mathrm{id},u'}X'\times\varphi'(X'')\longrightarrow}
~~~

Line 15, diagram

~~~tex
\(\boxed{\text{(3.16)}}\left\{\begin{tikzcd}[ampersand replacement=\&,row sep=huge]
 X'\arrow[r,"u'"]\arrow[rr,bend right=20,"{\lambda'(X')}"'] \& \varphi'(X'')\arrow[r,"{\varphi'(u'')}"] \& \varphi'\varphi''(X')\\
 X''\arrow[r,"u''"]\arrow[rr,bend right=20,"{\lambda''(X'')}"'] \& \varphi''(X')\arrow[r,"{\varphi''(u')}"] \& \varphi''\varphi'(X'')
\end{tikzcd}\right.\)
~~~

Line 20, inline

~~~tex
\varphi''\varphi'
~~~

Line 20, inline

~~~tex
\varphi'\varphi''
~~~

Line 20, inline

~~~tex
B'
~~~

Line 20, inline

~~~tex
B''
~~~

Line 22, display

~~~tex
\resizebox{.91\linewidth}{!}{\(\displaystyle\left\{\begin{aligned}
 &\left(X',X'',X'\xrightarrow{u'}\varphi'(X''),X''\xrightarrow{u''}\varphi''(X')\right)
 \quad \begin{aligned}&\overset{f'}{\longmapsto}X'\\[-2pt]&\xrightarrow{f''}X''\end{aligned}\\
 &g'(X')=\left(X',\varphi''(X'),X'\xrightarrow{\lambda'(X')}\varphi'\varphi''(X'),\varphi''(X')\xrightarrow{\mathrm{id}}\varphi''(X')\right)\\
 &g''(X'')=\left(\varphi'(X''),X'',\varphi'(X'')\xrightarrow{\mathrm{id}}\varphi'(X''),\deleted{\unsure{\varphi}}X''\xrightarrow{\lambda''(X'')}\varphi''\varphi'(X'')\right)
 \end{aligned}\right.\)} \tag*{3.17}
~~~

Line 30, inline

~~~tex
g'f'
~~~

Line 31, display

~~~tex
\left\{\begin{aligned}
 \text{Image ess. de }g' &: \quad u''\ \text{\uline{un isom}}\\
 \text{Image ess. de }g'' &: \quad u'\ \text{\uline{un isom}}
 \end{aligned}\right. \tag*{3.18}
~~~

Line 37, inline

~~~tex
\unsure{\perp|1}
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · deleted · `soumis aux conditions`
- L4 · deleted · `\unsure{$X'\longleftarrow(\mathrm{id}_{X'}$}`
- L4 · deleted · `\unsure{X'}`
- L4 · deleted · `\unsure{e}`
- L12 · deleted · `\unsure{X'}\quad X'\xrightarrow{\mathrm{id},u'}X'\times\varphi'(X'')\longrightarrow`
- L20 · uline · `Exemple`
- L27 · deleted · `\unsure{\varphi}`
- L30 · deleted · `\unsure{$g'f'$}`
- L33 · uline · `un isom`
- L34 · uline · `un isom`
- L37 · margin · `$\unsure{\perp|1}$`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
{\varphi\,\unsure{\text{de }*}}
->
{\varphi\,\unsure{(u)|(*)|\text{de }*}}
~~~

~~~tex
\varphi''(\unsure{X'|X})
->
\varphi''(\unsure{X'|X''})
~~~

~~~tex
\left\{\begin{aligned}
->
\resizebox{.91\linewidth}{!}{\(\displaystyle\left\{\begin{aligned}
~~~

~~~tex
\end{aligned}\right. \tag*{3.17}
->
\end{aligned}\right.\)} \tag*{3.17}
~~~

## Scan 12

2026-11-18T07:56:34Z to 2026-11-18T07:57:50Z

**Words and accents read before comparison**

adjonction; et β″ analogue; Question Quand β′ est-il un épimorphisme pour tout X ? Cela signifie, moyennant des conditions d’exactitude, devant / demandant … sur; tjrs un épimorphisme; L’intersection des images essentielles de … est formée; pour lesquels … sont des isom.; catégorie, équivaut à l’image inverse par, sous-catégorie pleine, formée des; Conditions équivalentes, catégorie finale, est équivalente à la … catégorie finale, Idem pour.

**Comparison with the page**

The sign after exactitude has two detached points above each other. The last dash before catégorie is clear to the right of the crossed word. The terminal stroke of final(e) is indistinct. The title of the central question and the word épimorphisme carry separate underlines. In the top diagram, the initial vertical split has a little separate adjonction label with a curved pointer. The circles are around the first id and u″, and do not enclose the vertical arrows. Checked the double/single-prime pattern on every vertical label, the unheaded downward strokes, the overwriting on upper u″, and the separate β″ beside the diagram. An isolated crossed start Cette catégorie precedes the live phrase. There is no item (iii) after (ii bis).

**Formulas, including diagram cells and arrow labels**

Line 3, diagram

~~~tex
\resizebox{\linewidth}{!}{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=huge]
 X\arrow[d,"{\beta'}"'] \& = \& (X'\arrow[d,"{\textcircled{\scriptsize id}}"'] \& ,X''\arrow[d,"{\textcircled{\scriptsize $u''$}}"] \& ,X'\arrow[r,"u'"]\arrow[d,no head,"\mathrm{id}"] \& \varphi'(X'')\arrow[d,no head,"{\varphi'(u'')}"] \& ,X''\arrow[r,"{\deleted{\unsure{\varphi}}u''}"]\arrow[d,"u''"] \& \varphi''(X'))\arrow[d,no head,"\mathrm{id}"]\\
 g'f'(X) \& = \& (X' \& ,\varphi''(X') \& ,X'\arrow[r,"{\lambda'(X')}"] \& \varphi'\varphi''(X') \& ,\varphi''(X')\arrow[r,"\mathrm{id}"] \& \varphi''(X'))
\end{tikzcd}}
~~~

Line 4, inline

~~~tex
u''
~~~

Line 8, inline

~~~tex
\beta''
~~~

Line 10, inline

~~~tex
\beta'
~~~

Line 10, inline

~~~tex
X
~~~

Line 10, inline

~~~tex
\varphi',\varphi''
~~~

Line 10, inline

~~~tex
u'':X''\longrightarrow\varphi''(X')
~~~

Line 12, inline

~~~tex
g'
~~~

Line 12, inline

~~~tex
g''
~~~

Line 12, inline

~~~tex
(X',X'',u',u'')
~~~

Line 12, inline

~~~tex
g'
~~~

Line 12, inline

~~~tex
u'
~~~

Line 12, inline

~~~tex
g''
~~~

Line 12, inline

~~~tex
u''
~~~

Line 12, inline

~~~tex
g'
~~~

Line 12, inline

~~~tex
g''_{\mathrm{ess}}(B'')
~~~

Line 12, inline

~~~tex
B'
~~~

Line 12, inline

~~~tex
X'
~~~

Line 12, inline

~~~tex
\lambda'(X')
~~~

Line 16, inline

~~~tex
g'_{\mathrm{ess}}(B')\wedge g''_{\mathrm{ess}}(B'')\simeq\text{catégorie finale}
~~~

Line 18, inline

~~~tex
B'
~~~

Line 18, inline

~~~tex
X'
~~~

Line 18, inline

~~~tex
\lambda'(X')
~~~

Line 20, inline

~~~tex
\lambda''
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L4 · deleted · `\unsure{\varphi}`
- L7 · margin · `adjonction`
- L10 · uline · `Question`
- L10 · uline · `épimorphisme`
- L10 · deleted · `\unsure{implique}`
- L10 · inserted · `signifie`
- L12 · deleted · `\unsure{$g'$}`
- L12 · uline · `et`
- L12 · deleted · `\unsure{$g''$}`
- L12 · deleted · `Cette catégorie \unsure{i.}`
- L12 · inserted · `str`
- L18 · deleted · `sous`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
d'exactitude \unsure{:|à}
->
d'exactitude :
~~~

~~~tex
\deleted{sous-}catégorie finale
->
\deleted{sous}-catégorie \unsure{finale|final}
~~~

## Scan 14

2026-11-18T07:57:50Z to 2026-11-18T07:59:03Z

**Words and accents read before comparison**

Résolution standart/standard et thèmes reliés (?) ; Draft, G adjoint …; Posons, d’où, satisfaisant les relations de Godement, d’où un objet (co)simplicial; dans Hom, et augmentation; On devrait trouver une interprétation naturelle par théorie de la descente; On pose de même (abbreviated); Notons les … inégalités ?, signif…; pour tt, La deuxième relation est vraie plus généralement si on a un foncteur et une liaison h telle que; alors; cf Godement; La formule (i) se vérifie sans doute de même par des formules explicites; Application, Supposons, abéliennes, additifs, exact et fidèle, résolution; b) Si Γ est un foncteur.

**Comparison with the page**

The upper-left pencil word under F starts with a large open loop, descends in the middle, and ends in a tall t-like stroke. The printed-looking heavy E and the two isolated F and G are separate handwritten capitals. In the title the last two words have separate rising accents or dots and read théories relatives. The circled co sits above simplicial. Contrasted the upper n at E-hat with the lower n at E′-hat in the second construction and retained the correction. The two saturated blocks after (i) and (ii) have diagonal hatching; their strokes do not extend into the G or F formulas. The relation sign has three tiers, and its typography remains uncertain. In h∘(T*φ) the round mark and the star differ. Rechecked both struck patches on the Application lines; continuous black ink prevents a word count beyond an estimate. In the last line, Γ has no long lower curl to establish a script T.

**Formulas, including diagram cells and arrow labels**

Line 4, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&]
 C'\arrow[r,shift left,"G"] \& C\arrow[l,shift left,"F"]
\end{tikzcd}
~~~

Line 11, display

~~~tex
\mathrm{Hom}(F(X),X')\xrightarrow{\sim}\mathrm{Hom}(X,G(X'))
 \qquad F\quad G
~~~

Line 16, display

~~~tex
E=GF:C\longrightarrow C
~~~

Line 20, display

~~~tex
\varphi:\mathrm{id}_C=E^0\longrightarrow E,\qquad \chi:E^2\longrightarrow E
~~~

Line 23, inline

~~~tex
\widehat E
~~~

Line 23, inline

~~~tex
(C,C)
~~~

Line 23, inline

~~~tex
\varphi
~~~

Line 23, inline

~~~tex
\chi
~~~

Line 24, display

~~~tex
\widehat E^{\,n}=E^{n+1}\ \deleted{\unsure{n}}\ \ldots\ldots\quad
 \text{et \uline{augmentation}}\quad X\longrightarrow\widehat E(X)
~~~

Line 29, display

~~~tex
E'=FG:C\longrightarrow C
~~~

Line 33, display

~~~tex
\varphi':E'\longrightarrow\mathrm{id}_{C'}=E'^{\,0},\qquad
 \chi':E'\mathrel{\unsure{-|\to}}E'^{\,2}
~~~

Line 37, inline

~~~tex
\widehat E'
~~~

Line 37, inline

~~~tex
(C',C')
~~~

Line 38, display

~~~tex
\widehat E'^{\deleted{\unsure{n}}}_{n}=E'^{\,n+1}\qquad\text{---}
~~~

Line 42, display

~~~tex
\begin{aligned}
 \text{(i)}\quad &G(X')\mathrel{\unsure{\approxeq|\approx}}\widehat E(G(X'))\ \deleted{\unsure{\simeq0}}
       &&\text{pour tt }X'\in\mathrm{ob}\,C'\\
 \text{(ii)}\quad &F(X)\approxeq F(\widehat E(X))\ \deleted{\unsure{\simeq0}}
       &&\text{pour tt }X\in\mathrm{ob}\,C
 \end{aligned}
~~~

Line 50, inline

~~~tex
T:C\longrightarrow D
~~~

Line 51, display

~~~tex
h:T\circ E\longrightarrow T
~~~

Line 55, display

~~~tex
h\circ(T*\varphi)=\mathrm{id}_T
~~~

Line 59, display

~~~tex
T\widehat E(X)\approxeq 0\qquad\text{pour tt }X\in\mathrm{ob}\,C
~~~

Line 64, inline

~~~tex
C,C'
~~~

Line 64, inline

~~~tex
F,\unsure{G|C}
~~~

Line 64, inline

~~~tex
F
~~~

Line 64, inline

~~~tex
\widehat E(X)
~~~

Line 64, inline

~~~tex
X
~~~

Line 64, inline

~~~tex
X
~~~

Line 66, inline

~~~tex
\unsure{\Gamma|\mathscr T}
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · uline · `\unsure{Résolutions|Résolution} standard et théories relatives.`
- L8 · margin · `\uline{\unsure{Dont|Droit|Donné}}`
- L8 · uline · `\unsure{Dont|Droit|Donné}`
- L10 · margin · `\unsure{Godement|G-préfaisc.|G-faisc.}`
- L23 · inserted · `\textcircled{\scriptsize co}`
- L23 · uline · `simplicial`
- L23 · deleted · `dans`
- L23 · uline · `Hom`
- L23 · deleted · `\unsure{$\varphi$ et $\chi$ où}`
- L25 · deleted · `\unsure{n}`
- L26 · uline · `augmentation`
- L37 · uline · `simplicial`
- L37 · uline · `Hom`
- L39 · deleted · `\unsure{n}`
- L41 · deleted · `\unsure{isomorphismes} \unsure{fonctoriels}`
- L41 · inserted · `\unsure{résultats suivants}`
- L44 · deleted · `\unsure{\simeq0}`
- L46 · deleted · `\unsure{\simeq0}`
- L64 · uline · `Application`
- L64 · deleted · `\illegible{2}`
- L64 · deleted · `\illegible{1}`
- L64 · uline · `exact`
- L64 · uline · `fidèle`
- L64 · uline · `résolution`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
\unsure{G-préfaisc.|G-faisc.}
->
\unsure{Godement|G-préfaisc.|G-faisc.}
~~~

~~~tex
\inserted{résultats suivants}
->
\inserted{\unsure{résultats suivants}}
~~~

~~~tex
\uline{\unsure{Droit|Dont}}
->
\uline{\unsure{Dont|Droit|Donné}}
~~~

## Scan 15

2026-11-18T07:59:04Z to 2026-11-18T08:00:37Z · Additional comparison 2026-11-18T08:06:31Z

**Words and accents read before comparison**

Cohomologies relatives (un cas spécial), Caractérisation des foncteurs; Soit C une catégorie, Pour tout, foncteur, des ensbles/en sem bles; contravariant en B, à valeurs dans la catégorie des foncteurs; En effet, on définit la flèche inverse … en associant; élément … l’image … l’élément unité; additive, additif, exact à gauche, isomorphisme, valable, limitant, identifer/identifier; sous-catégorie de la catégorie Fonc. add.; générateur, satisfasse à AB 3,4,5; Tout … transforme les ind … inductives en limites projectives, est exact à gauche; On va donner une réciproque. Tout d’abord, deux foncteurs contr[avariants], ayant.

**Comparison with the page**

The lighter title in the upper right has one underline; the qualifier un cas spécial is on two lines below it. In (*) the lower C has an eye inside the upper curve; a separate exponent o cannot be established. The marks before contravariant include a low dot and a taller stroke. The lower Hom attached to the identity has a tiny subscript with an open bowl. The endpoints in the bracketed calculation read h_B(B) then h_B(B′) as penned. The superior faint note exact à g. lies at the far right of additif. Compared the capital in Fonc.add. and both occurrences of the final category letter. Near AB the raised replacement begins with T, the word below is crossed through. The first word on the next line is h_B. At the bottom contr. has an insertion mark, and there is a blotted raised sign on C. A further enlargement of the lower line shows one word between transforme and inductives, namely limites.

**Formulas, including diagram cells and arrow labels**

Line 4, inline

~~~tex
A\longrightarrow\mathrm{Hom}(A,B)
~~~

Line 6, inline

~~~tex
C
~~~

Line 6, inline

~~~tex
B\in C
~~~

Line 6, inline

~~~tex
h_B
~~~

Line 6, inline

~~~tex
C
~~~

Line 7, display

~~~tex
h_B(A)=\mathrm{Hom}(A,B)
~~~

Line 10, inline

~~~tex
h_B
~~~

Line 10, inline

~~~tex
B
~~~

Line 10, inline

~~~tex
C\longrightarrow\unsure{\mathcal E|E}
~~~

Line 11, display

~~~tex
\alpha:\mathrm{Hom}_C(B,B')\xrightarrow{\sim}\mathrm{Hom}(h_B,h_{B'}) \tag*{(*)}
~~~

Line 14, inline

~~~tex
\beta
~~~

Line 14, inline

~~~tex
u\in\mathrm{Hom}(h_B,h_{B'})
~~~

Line 14, inline

~~~tex
\beta(u)
~~~

Line 14, inline

~~~tex
\mathrm{Hom}_C(B,B')
~~~

Line 14, inline

~~~tex
u_B
~~~

Line 14, inline

~~~tex
h_B(B)=\mathrm{Hom}_{\unsure{C|a}}(B,B)
~~~

Line 14, inline

~~~tex
h_B(B')=\mathrm{Hom}_C(B,B')
~~~

Line 16, inline

~~~tex
C
~~~

Line 16, inline

~~~tex
C
~~~

Line 16, inline

~~~tex
h_B
~~~

Line 16, inline

~~~tex
B\longrightarrow h_B
~~~

Line 16, inline

~~~tex
(*)
~~~

Line 16, inline

~~~tex
B\longrightarrow h_B
~~~

Line 16, inline

~~~tex
C
~~~

Line 16, inline

~~~tex
\mathrm{Fonc.add.}(C^o,\unsure{\mathscr G|\mathfrak G})
~~~

Line 18, inline

~~~tex
C
~~~

Line 18, inline

~~~tex
U
~~~

Line 18, inline

~~~tex
h_B
~~~

Line 18, inline

~~~tex
h,h'
~~~

Line 18, inline

~~~tex
C^{\deleted{\unsure{o}}}\longrightarrow\mathscr G
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · uline · `Cohomologies relatives`
- L4 · uline · `Caractérisation des foncteurs`
- L14 · deleted · `\unsure{tout}`
- L14 · deleted · `\unsure{un}`
- L16 · deleted · `Si dans $C$ il y a \unsure{assez de sommes}`
- L16 · inserted · `\uline{exact à g.}`
- L16 · uline · `exact à g.`
- L16 · uline · `à gauche`
- L16 · uline · `additifs`
- L16 · deleted · `\unsure{est}`
- L18 · deleted · `que`
- L18 · deleted · `\unsure{Comme}`
- L18 · inserted · `\unsure{Tout|Tjs est}`
- L18 · deleted · `\unsure{alors}`
- L18 · deleted · `\unsure{par suite} \unsure{aussi}`
- L18 · inserted · `est exact`
- L18 · inserted · `contr.`
- L18 · deleted · `\unsure{o}`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
\unsure{.l} contravariant
->
\unsure{.l|,!} contravariant
~~~

~~~tex
\inserted{Tjs est}
->
\inserted{\unsure{Tout|Tjs est}}
~~~

~~~tex
transforme limites inductives
->
transforme \unsure{les|{}} limites inductives
~~~

~~~tex
transforme \unsure{les|{}} limites
->
transforme limites
~~~

## Scan 16

2026-11-18T08:00:38Z to 2026-11-18T08:02:33Z

**Words and accents read before comparison**

ces propriétés, on montre que, posant, on … a; où R°, anneau inverse de R; Pour le voir, on définit un hom.; Détails laissés au lecteur. Donc le foncteur … identifie la catégorie des foncteurs envisagés à une sous-catégorie; R-mod … à droite; On va définir un “foncteur inverse”, envisagée; On va définir directement le foncteur; ce sera simplement; on va montrer que, est “surjectif”, donc … sont des “équivalences”, On doit donc montrer que; ce qui est laissé au soin des lecteurs; Ainsi, les foncteurs contravariants exacts à gauche, limites inductives en limites projectives, sont essentiellement.

**Comparison with the page**

The lowest word in the transfer-to-the-reader clause has a definite rising initial l. The little group between au and du has a heavy final stroke. In the left diagram, two arrows point down from C and the functor category. The long curved arrow rises on the left towards C. The two injunction-looking labels actually have paired quotation strokes around inj. At the right of the second node some letters after qui are faint. The exponents on R and on the module-category symbol are raised open o’s. In M=T′T(T″M), the first T has one prime, the inner T two. The short canceled word after on and the overwritten capital before the domain of T″ are both in ink. The long line through the hypothesis beginning si h stops below the raised formula. A lead-in stroke at the foot takes des h_B from the left into the concluding words.

**Formulas, including diagram cells and arrow labels**

Line 2, inline

~~~tex
M(h)=h(U)
~~~

Line 3, display

~~~tex
\alpha':\mathrm{Hom}(h,h')\xrightarrow{\sim}\mathrm{Hom}_{R^o}(\deleted{\unsure{h}}M(h),M(h'))
~~~

Line 6, inline

~~~tex
R=\mathrm{Hom}_C(U,U)
~~~

Line 6, inline

~~~tex
R^o=
~~~

Line 6, inline

~~~tex
R
~~~

Line 9, display

~~~tex
\beta':\mathrm{Hom}_{R^o}(M(h),M(h'))\longrightarrow\mathrm{Hom}(h,h')
~~~

Line 12, inline

~~~tex
T':h\longrightarrow M(h)
~~~

Line 12, inline

~~~tex
\unsure{\mathscr G|\mathfrak G}^{R^o}
~~~

Line 12, inline

~~~tex
R
~~~

Line 12, inline

~~~tex
M\longrightarrow h_M
~~~

Line 12, inline

~~~tex
\mathscr G^{R^o}
~~~

Line 12, inline

~~~tex
T'':\deleted{\unsure{C}}\mathscr G^{R^o}\longrightarrow C
~~~

Line 13, display

~~~tex
T''(M)=M\otimes_R U
~~~

Line 16, margin note

~~~tex
\begin{tikzcd}[ampersand replacement=\&,row sep=small]
 C\arrow[d,"{T\ \text{``inj''}}"]\\
 \substack{\text{foncteurs contr.}\\ C\to\mathscr G\ \text{qui }\unsure{\text{tr}|\text{ch}}}\arrow[d,"{T'\ \text{``inj''}}"]\\
 \mathscr G^{R^o}\arrow[uu,bend left=65,"T''"]
\end{tikzcd}
~~~

Line 21, inline

~~~tex
h
~~~

Line 21, inline

~~~tex
C^o\longrightarrow\mathscr G
~~~

Line 21, inline

~~~tex
M=T'T(T''M)
~~~

Line 21, inline

~~~tex
T'T
~~~

Line 21, inline

~~~tex
T
~~~

Line 21, inline

~~~tex
T'
~~~

Line 22, display

~~~tex
\left\{\begin{aligned}
 &\mathrm{Hom}_C(U,M\otimes_R U)\simeq M\\
 &\text{si}\quad R=\mathrm{Hom}_C(U,U)\\
 &\phantom{\text{si}\quad} M\in\mathscr G^{R^o}
 \end{aligned}\right.
~~~

Line 31, inline

~~~tex
C\longrightarrow\mathscr G
~~~

Line 31, inline

~~~tex
h_B
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · deleted · `\unsure{est}`
- L4 · deleted · `\unsure{h}`
- L12 · deleted · `Posons donc, pour \unsure{les}`
- L12 · deleted · `\unsure{C}`
- L16 · margin · `\begin{tikzcd}[ampersand replacement=\&,row sep=small] C\arrow[d,"{T\ \text{``inj''}}"]\\ \substack{\text{foncteurs contr.}\\ C\to\mathscr G\ \text{qui }\unsure{\text{tr}|\text{ch}}}\arrow[d,"{T'\ \text{``inj''}}"]\\ \mathscr G^{R^o}\arrow[uu,bend left=65,"T''"] \end{tikzcd}`
- L21 · deleted · `si $h$ est un foncteur $C^o\longrightarrow\mathscr G$ du type envisagé, alors`
- L21 · inserted · `$M=T'T(T''M)$`
- L31 · deleted · `\unsure{L}`
- L31 · deleted · `\unsure{covariants}`
- L31 · inserted · `\unsure{contravariant|contravariants}`
- L31 · deleted · `transformant \unsure{une}`
- L31 · inserted · `des $h_B$`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
au soin du lecteur
->
au \unsure{soin|soins} du lecteur
~~~

~~~tex
\inserted{contravariant}
->
\inserted{\unsure{contravariant|contravariants}}
~~~

~~~tex
C\to\mathscr G\ \text{qui tr}
->
C\to\mathscr G\ \text{qui }\unsure{\text{tr}|\text{ch}}
~~~

## Scan 17

2026-11-18T08:02:34Z to 2026-11-18T08:03:57Z

**Words and accents read before comparison**

Soient … deux catégories additives, foncteur additif, de … dans; On suppose que pour … le foncteur … est un foncteur du type …, où B dépend de X, mais de façon essentiellement fonctorielle, donc on a; où … est un foncteur covariant exact à gauche; Les conditions sont satisfaites notamment si … satisfont à AB 1,3,4,5, si … un générateur, et si de plus … exact à droite (car … est exact à gauche). En particulier; Donc faisant … on trouve un élément canonique; D’autre part, on tire de (1), faisant; et en particulier; sloping upper-left note about rôle symétrique and long upright note about isomorphismes; watch accents in réciproque and élément.

**Comparison with the page**

With the left edge horizontal, the shorter note reads Mettre en évidence le rôle symétrique joué par C et C′°; the long note has Hom_C(A,T(X)) followed by two right arrows. Its last A has no secure tilde. Compared the two live isomorphism arrows in (1) and (2) with these right arrows; those in (1) and (2) point left. At AB, two adjacent uprights and a short low mark intervene before 3; the first could be the beginning parenthesis and the second a 1. The long strike spans all of the first (4) including its number. Beside it, the first two letters of the live composite touch an overwritten parenthesis. The conspicuous bar above X∈C is straight, whereas some of the former category letters elsewhere have a wavy tilde above them. In (5) a separate equivalence sign follows the closing parenthesis and ends the display.

**Formulas, including diagram cells and arrow labels**

Line 2, inline

~~~tex
C,\deleted{\unsure{\widetilde C}}C'
~~~

Line 2, inline

~~~tex
S:\deleted{\unsure{A\longrightarrow\widetilde A}}C\longrightarrow C'
~~~

Line 2, inline

~~~tex
C
~~~

Line 2, inline

~~~tex
\deleted{\unsure{\widetilde C}}C'
~~~

Line 2, inline

~~~tex
A\in C
~~~

Line 2, inline

~~~tex
X\in\bar C
~~~

Line 2, inline

~~~tex
A\mathrel{\unsure{-|\to}}\mathrm{Hom}_{C'}(S(A),X)
~~~

Line 2, inline

~~~tex
\mathrm{Hom}(A,
~~~

Line 2, inline

~~~tex
h_B
~~~

Line 2, inline

~~~tex
B
~~~

Line 2, inline

~~~tex
X
~~~

Line 4, inline

~~~tex
C
~~~

Line 4, inline

~~~tex
C'^{o}
~~~

Line 5, display

~~~tex
\mathrm{Hom}_{\bar C}(S(\deleted{\unsure{\widetilde A}}A),X)\xleftarrow{\sim}\mathrm{Hom}_C(A,T(X)) \tag*{(1)}
~~~

Line 8, inline

~~~tex
T:\deleted{\unsure{\widetilde C}}C'\longrightarrow C
~~~

Line 8, inline

~~~tex
\deleted{\unsure{\widetilde C}}C'
~~~

Line 8, inline

~~~tex
C
~~~

Line 8, inline

~~~tex
C
~~~

Line 8, inline

~~~tex
\deleted{\unsure{\widetilde C}}C'
~~~

Line 8, inline

~~~tex
\mathrm{AB}\unsure{(1,|1,|(}3,4,5)
~~~

Line 8, inline

~~~tex
C
~~~

Line 8, inline

~~~tex
A\longmapsto\widetilde A
~~~

Line 8, inline

~~~tex
S
~~~

Line 8, inline

~~~tex
A\mathrel{-}\mathrm{Hom}_C(\deleted{\unsure{\widetilde A}}S(A),X)
~~~

Line 10, inline

~~~tex
X=S(\deleted{\unsure{\widetilde B}}B)
~~~

Line 11, display

~~~tex
\mathrm{Hom}_C(A,B)\longrightarrow\mathrm{Hom}_{C'}(\deleted{\unsure{\widetilde A}}S(A),\deleted{\unsure{\widetilde B}}S(B))\xleftarrow{\sim}\mathrm{Hom}_C(A,TS(B)) \tag*{(2)}
~~~

Line 14, inline

~~~tex
A=B
~~~

Line 15, display

~~~tex
\varphi(A)\in\mathrm{Hom}(A,TS(\deleted{\unsure{\widetilde A}}A))\qquad\text{i.e.} \tag*{(3)}
~~~

Line 18, display

~~~tex
\varphi:\mathrm{id}_C\longrightarrow TS \tag*{(3 bis)}
~~~

Line 21, inline

~~~tex
A=T(Y)
~~~

Line 22, display

~~~tex
\deleted{\mathrm{Hom}_{\widetilde C}(\widetilde A,X)\xrightarrow{\sim}\mathrm{Hom}_C(A,T(X))\longrightarrow\mathrm{Hom}_{\widetilde C}(\widetilde A,\widetilde{T(X)})} \tag*{\deleted{(4)}}
~~~

Line 25, display

~~~tex
\mathrm{Hom}_{C'}(\unsure{TS|ST}(\deleted{\unsure{\widetilde Y}}Y),X)\simeq\mathrm{Hom}_C(T(Y),T(X)) \tag*{(4)}
~~~

Line 28, inline

~~~tex
X=Y
~~~

Line 29, display

~~~tex
\psi(X)\in\mathrm{Hom}_{C'}(ST\deleted{\unsure{\widetilde{\phantom X}}}(X),X)\simeq \tag*{(5)}
~~~

Line 32, display

~~~tex
\psi:ST\longrightarrow\deleted{\unsure{\varphi}}\mathrm{id}_{\widetilde C} \tag*{(5 bis)}
~~~

Line 36, inline

~~~tex
\psi(X)
~~~

Line 36, inline

~~~tex
\mathrm{Hom}_C(A,T(X))\longrightarrow\mathrm{Hom}_{\widetilde C}(\widetilde A,\widetilde{T(X)})\longrightarrow\mathrm{Hom}_{\widetilde C}(A,X)
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · deleted · `\unsure{\widetilde C}`
- L2 · deleted · `additives, abéliennes`
- L2 · inserted · `additives`
- L2 · deleted · `\unsure{A\longrightarrow\widetilde A}`
- L2 · deleted · `\unsure{\widetilde C}`
- L2 · deleted · `tout`
- L2 · deleted · `\unsure{$A\in C$}`
- L2 · deleted · `$\mathrm{Hom}(A,$`
- L4 · margin · `Mettre en évidence le rôle symétrique joué par $C$ et $C'^{o}$`
- L6 · deleted · `\unsure{\widetilde A}`
- L8 · deleted · `\unsure{\widetilde C}`
- L8 · deleted · `\unsure{\widetilde C}`
- L8 · deleted · `\unsure{\widetilde C}`
- L8 · deleted · `\unsure{$A\longmapsto\widetilde A$}`
- L8 · deleted · `\unsure{\widetilde A}`
- L8 · deleted · `En particulier,`
- L10 · deleted · `\unsure{\widetilde B}`
- L12 · deleted · `\unsure{\widetilde A}`
- L12 · deleted · `\unsure{\widetilde B}`
- L16 · deleted · `\unsure{\widetilde A}`
- L23 · deleted · `\mathrm{Hom}_{\widetilde C}(\widetilde A,X)\xrightarrow{\sim}\mathrm{Hom}_C(A,T(X))\longrightarrow\mathrm{Hom}_{\widetilde C}(\widetilde A,\widetilde{T(X)})`
- L23 · deleted · `(4)`
- L26 · deleted · `\unsure{\widetilde Y}`
- L28 · deleted · `\unsure{A}`
- L30 · deleted · `\unsure{\widetilde{\phantom X}}`
- L33 · deleted · `\unsure{\varphi}`
- L36 · margin · `C'est la donnée des $\psi(X)$ qui précise l'homomorphisme (1), puisqu'on a $\mathrm{Hom}_C(A,T(X))\longrightarrow\mathrm{Hom}_{\widetilde C}(\widetilde A,\widetilde{T(X)})\longrightarrow\mathrm{Hom}_{\widetilde C}(A,X)$`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
\mathrm{AB}\unsure{(}3,4,5)
->
\mathrm{AB}\unsure{(1,|1,|(}3,4,5)
~~~

## Scan 18

2026-11-18T08:03:57Z to 2026-11-18T08:04:58Z

**Words and accents read before comparison**

En plus, on … connaître l’homom.; Considérons … d’où, par suite … d’autre part, on a aussi; Ceci dit; identité; en d’autres termes … s’identifie par … à un facteur direct de … la projection naturelle étant; De même, on a le diagramme commutatif; qui identifie … à un facteur direct de; Pour que l’homomorphisme fonctoriel soit injectif (i.e. les … injectifs) il faut et il suffit que les homomorphismes … soient injectifs; cel[a] signifie aussi que le foncteur S est “injectif”; Cel résulte de la commutativité du/des.

**Comparison with the page**

Four heavy A/X over-writings appear in the second triangle, including the one in T(ψ(X)). Supplied the braces around the four doubtful old A’s. A line with a left-facing point extends through the parenthesised TS in the middle. The high arrow in the first triangle points right; the second triangle and its identity arc point left. In the final Hom diagram the map from the last object points left and the long curved map below points right. A small pen stroke under the central Hom is crossed. The terminal word injectif is between paired high quote marks. No typed additions appear on this page.

**Formulas, including diagram cells and arrow labels**

Line 4, inline

~~~tex
A\in C
~~~

Line 4, inline

~~~tex
\widetilde A\in\widetilde C
~~~

Line 4, inline

~~~tex
i_A:\deleted{\unsure{A\longrightarrow T\widetilde A}}\inserted{A\mathrel{\unsure{-|\to}}TSA}
~~~

Line 4, inline

~~~tex
\widetilde A
~~~

Line 4, inline

~~~tex
S(i_A):SA\longrightarrow STSA
~~~

Line 4, inline

~~~tex
(ST)(SA)\xrightarrow{\unsure{e_{SA}|\varepsilon_{SA}}}(SA)
~~~

Line 5, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&]
 SA\arrow[r,"{S(\varphi(A))}"]\arrow[rr,bend right=17,"\text{identité}"']
 \& S(TS(A))=(ST)(SA)\arrow[r,"{\psi(SA)}"] \& SA
\end{tikzcd}
~~~

Line 9, inline

~~~tex
S(A)
~~~

Line 9, inline

~~~tex
S(\varphi(A))
~~~

Line 9, inline

~~~tex
(ST)(S(A))
~~~

Line 9, inline

~~~tex
\deleted{e_{S(A)}}\psi(S(A))
~~~

Line 10, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&]
 T(\deleted{\unsure{A}}X) \& T(ST(\deleted{\unsure{A}}X))\deleted{\unsure{\leftarrow}}=\deleted{\unsure{(TS)}}(T(\deleted{\unsure{A}}X))\arrow[l,"{T(\psi(\deleted{\unsure{A}}X))}"'] \&
 T(X)\arrow[l,"{\varphi(T(\unsure{X|A}))}"']\arrow[ll,bend left=13,"\text{identité}"]
\end{tikzcd}
~~~

Line 14, inline

~~~tex
T(X)
~~~

Line 14, inline

~~~tex
(TS)(T(X))
~~~

Line 16, inline

~~~tex
\varphi:\mathrm{id}_C\longrightarrow TS
~~~

Line 16, inline

~~~tex
\varphi(A):A\mathrel{-}TS(A)
~~~

Line 17, display

~~~tex
S(A,B):\mathrm{Hom}_C(A,B)\longrightarrow\mathrm{Hom}_{C'}(SA,SB)
~~~

Line 20, inline

~~~tex
S
~~~

Line 21, diagram

~~~tex
\begin{tikzcd}[ampersand replacement=\&]
 \mathrm{Hom}_C(A,B)\arrow[r]\arrow[rr,bend right=12,"{\deleted{\unsure{u}}}"']
 \&\mathrm{Hom}_{C'}(SA,SB) \& \mathrm{Hom}_C(A,TSB)\arrow[l,"\sim"']
\end{tikzcd}
~~~

**Indices and exponents containing i or j**

None.

**Cancellations, insertions, marginalia and underlining**

- L2 · deleted · `En plus, on \illegible{1} \unsure{considère} l'\unsure{homom.}`
- L4 · deleted · `pour`
- L4 · deleted · `$\widetilde A\in\widetilde C$ et`
- L4 · deleted · `\unsure{A\longrightarrow T\widetilde A}`
- L4 · inserted · `A\mathrel{\unsure{-|\to}}TSA`
- L4 · deleted · `\unsure{$\widetilde A$,}`
- L9 · deleted · `e_{S(A)}`
- L11 · deleted · `\unsure{A}`
- L11 · deleted · `\unsure{A}`
- L11 · deleted · `\unsure{\leftarrow}`
- L11 · deleted · `\unsure{(TS)}`
- L11 · deleted · `\unsure{A}`
- L11 · deleted · `\unsure{A}`
- L20 · deleted · `\unsure{fi}`
- L22 · deleted · `\unsure{u}`

The sheet is handwritten throughout.

**Changes, before -> after**

~~~tex
\unsure A
->
\unsure{A}
~~~

~~~tex
\unsure A
->
\unsure{A}
~~~

~~~tex
\unsure A
->
\unsure{A}
~~~

~~~tex
\unsure A
->
\unsure{A}
~~~

~~~tex
=(TS)(T(\deleted
->
=\deleted{\unsure{(TS)}}(T(\deleted
~~~


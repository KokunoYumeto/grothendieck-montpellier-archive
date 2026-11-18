# Cote 76 · second reading

Times are UTC. Locations identify the manuscript lines or the position on the sheet. The formula registers preserve the state of the independent reading, before comparison with the witness. Each diagram is given as one register entry so that its objects, arrows, labels, primes and indices stay together.

## Scan 3

Started 2026-11-18T06:59:25Z. Ended 2026-11-18T07:01:00Z.

**Image notes recorded before reopening the transcription**

Title shows a cap over the first o in côniques; cellular-looking word below is struck. ‘qu...ensembles’ has a leading g/q with an underline. Underlined Axiome 1, Incidence, surjectif with single j descender. ssi near the left brace, él. minimaux, ordonnés, condition des chaines (accent uncertain), totᵗ ordonnés, Verifier at a steep angle. Celà or Cela above the square bracket. Long blank rules after F_1 and F_i. ‘longueur’ underlined, non vide underlined. Lower-left pencil 2. Upper-left margin ends surjectif. Dense right margin and bottom run-on need a closer view.

**Comparison with the transcription**

The rotated left edge has a question, Axiome 1′ and the second projection ending surjectif. The right-hand note runs across two punched holes. In the order definition the relation at the left looks like a strict angle; the first branch actually says x=y. The dot in i and the long tail of j in surjectif are distinct. The bars after F₁ and Fᵢ are repetition lines, not cancellation. The lower text has a live inserted specification over a cancelled one; maxima has its own stroke. The slanted vérifier has an underline. Plain F and I were compared with the low star and the script capital of the flag set. There is no typewriting.

**Changes**

- `(F_\alpha\ \text{ens.` -> `(\unsure{F|I}_\alpha\ \text{ens.`
- `Pour \unsure{ne plus avoir|éviter} ces considérations` -> `Pour une \unsure{partie} de ces considérations`
- `de fixer un $n$ de \unsure{référence}` -> `de fixer un \unsure{$n$ de référence|ordre inverse}`
- `z_{\alpha\unsure{+|-}1}` -> `z_{\alpha\unsure{-|+}1}`
- `F_{\alpha\unsure{+|-}1}` -> `F_{\alpha\unsure{-|+}1}`
- `$F_\alpha$) sont de` -> `$F_{\unsure{\alpha|*}}$) sont de`
- `$I$. longueur` -> `$I$. \uline{longueur}`

**Formulas and diagram register**

2, overwritten list, then above it.


~~~latex
\[
\begin{aligned}
&\inserted{F_0\quad F_1\qquad F_n}\\
&\deleted{I_0\quad I_1\quad I_n}\qquad\text{ensembles \inserted{(finis?)}}\quad(\unsure{F|I}_\alpha\ \text{ens. des }\alpha\text{-faces})
\end{aligned}
\]
~~~


3, incidence.


~~~latex
\[
\forall\ 0\leq\alpha\leq n-1,\quad I_\alpha\subset F_\alpha\times F_{\alpha+1}\qquad\text{(relation d'incidence)}
\]
~~~


4, axiom.

- `$I_\alpha\to F_{\alpha+1}$`
- `$I_\alpha\to F_\alpha$`

4, left edge.

- `$1'$`
- `$I_\alpha\to F_\alpha$`

5, order.

- `$F_*=\displaystyle\coprod_{0\leq\alpha\leq n}F_\alpha$`

6–9, braced alternatives.


~~~latex
\[
\begin{aligned}
\underset{\substack{\rotatebox{90}{$\scriptstyle\ni$}\\F_\alpha}}{x}
<\underset{\substack{\rotatebox{90}{$\scriptstyle\ni$}\\F_\beta}}{y}
\quad\text{ssi}\quad
\left\{\begin{aligned}
&\text{ou bien }x=y\quad(\text{donc }\alpha=\beta)\\
&\text{ou bien }\alpha<\beta,\ \text{et }\exists\ z_\alpha=x\inserted{\in F_\alpha},z_{\alpha\unsure{-|+}1}\in F_{\alpha+1},\ldots,z_{\beta-1}\in F_{\beta-1}\\
&\hspace{2em} z_\beta\deleted{\unsure{\in}}=y\in F_\beta,\quad\text{tels que }\forall\alpha\leq i<\beta,\\
&\hspace{3em}z_i\ \text{et }z_{i+1}\ \text{soient incidents}
\end{aligned}\right.
\end{aligned}
\]
~~~


10–12, NB.

- `$(F_\alpha)_{0\leq\alpha\leq n}$`
- `$I_\alpha$`
- `$(0\leq\alpha\leq n-1)$`
- `$F_*$`

13–16, successive minima and long repetition strokes.


~~~latex
\[
\begin{aligned}
 F_0&=\text{ens des él. minimaux de }F_*\\
 F_1&=\rule{7em}{.35pt}\quad F_*-F_0\\
 &\unsure{\cdots}\\
 F_i&=\rule{7em}{.35pt}\quad F_*-F_0-\ldots-F_{i-1}\qquad(i\leq n)
\end{aligned}
\]
~~~


13–16, right edge opposite the minima.

- `$n$`

17, recovered incidence.


~~~latex
\[
 I_\alpha\subset F_\alpha\times F_{\alpha\unsure{-|+}1}\qquad
 I_\alpha=\bigl((x,y)\mid x\in F_\alpha,\ y\in F_{\alpha+1},\ x\leq y\bigr\}
\]
~~~


18, bracketed line.

- `$I_\alpha\unsure{-|\to} F_{\alpha+1}$`

19–23, chain condition.

- `$F_*$`
- `$F_{\unsure{\alpha|*}}$`
- `$F_*$`
- `$\leq n$`
- `$=n$`
- `$F_n\neq\varnothing$`

24–27, flags.

- `$I$`
- `$\in\mathscr P[0,n]$`
- `$[1,n]$`

26–27, lower right.

- `$\mathscr D(F_*)$`
- `$\subseteq$`

28–29, continues at foot.

- `$F_*$`
- `$x\leq y$`
- `$F_*$`

**Corrections, marginal writing and cancellations**

- 1, heading — `\deleted{cellulaires}`, `\inserted{\unsure{côniques|cômiques}}`, `\deleted{\unsure{g}}`
- 2, overwritten list, then above it — `\inserted{F_0\quad F_1\qquad F_n}`, `\deleted{I_0\quad I_1\quad I_n}`, `\inserted{(finis?)}`
- 4, axiom — `\deleted{et \unsure{$I_\alpha\to F_\alpha$}}`
- 4, left edge — `\margin{\unsure{faudr.t-il|faudrait-il} ? \uline{Axiome $1'$} $I_\alpha\to F_\alpha$ surjectif.}`
- 6–9, braced alternatives — `\inserted{\in F_\alpha}`, `\deleted{\unsure{\in}}`
- 13–16, right edge opposite the minima — `\margin{\uline{NB} Pour une \unsure{partie} de ces considérations, il est \unsure{opportun} de fixer un \unsure{$n$ de référence|ordre inverse}.}`
- 19–23, chain condition — `\inserted{les chaines (= ss-ens. \unsure{totalemt} ordonnés de $F_{\unsure{\alpha|*}}$) sont de}`, `\deleted{les chaines croissantes \inserted{de ens. ordonnés} d'éléments de $F_*$}`, `\inserted{de ens. ordonnés}`, `\deleted{maxima}`
- 19–20, left beside chain condition — `\margin{\uline{vérifier}}`
- 24–27, flags — `\deleted{\unsure{Ai}}`
- 26–27, lower right — `\margin{Ens $\mathscr D(F_*)$ des drapeaux, \unsure{Ordonné} $\subseteq$}`

**Index and exponent register**

- 6–9, braced alternatives — `_i`, `_{i+1}`
- 13–16, successive minima and long repetition strokes — `_i`, `_{i-1}`


## Scan 4

Started 2026-11-18T07:01:01Z. Ended 2026-11-18T07:02:38Z.

**Image notes recorded before reopening the transcription**

Two columns on ruled staves. Left oblique reads au passage à l’ordre inverse près; l’un renversé over F_*; “maximaux...” and “maximaux,”. Axiome 2, Axiome 3 underlined. ‘définissons’ struck, ‘incidentes’, ‘caractérisé’, facultatif, ‘pour n fixé’. Right contains ‘On va voir maintenant’, ‘reconstituer’ underlined; a crossed beginning before Mais; ‘s.s.’ drawn like ‘sic.’; ‘consécutifs.’ superscripted. Two raised addenda around Axiome 4/5; ‘évidemment’, ‘Pour la bijectivité’, ‘injection’, ‘trivial’, ‘généralemᵗ’, ‘bijectif’. The right column's final question extends below the last equation.

**Comparison with the transcription**

Ruled musical staves run unbroken under the ink in both columns. They do not cancel the live text. Under Axiome 2 the argument of the second F has a heavy lowered stroke resembling 1, with alpha a possible reading. The overwriting of the end of F in ‘Pour tout x’ is separate from the insertion above ‘Il satisfait’. The raised $2≤α≤n$ belongs to the first condition. The two slanted brackets carry rank restrictions. The right gutter note reads ‘le … naturel’. The second D-like initial in the left column is the start of the deleted Défin… word. The initial of the flag set has two rising strokes; the group G has a loop and is not double-struck. Checked α against β, the prime at n and at 0, the i in xᵢ, Fᵢ, σᵢ and the two inequalities in the right column. An apparent reference to Axiome 2 remains as written.

**Changes**

- `? Le fait de \inserted` -> `? \unsure{En fait|Il faut} \unsure{donc} \inserted`
- `F(x_{\unsure{1}|\alpha})` -> `F(x_{\unsure{1|\alpha}})`
- `le card. des \unsure{$\widehat{\text{mes}}$} des` -> `le \unsure{cardinal|card.} de l'ens des`
- `\deleted{\unsure{Définir}}` -> `\deleted{\unsure{Définissons|Définir}}`
- `$x_{\alpha-2}\in F(x)_{\alpha-2}$` -> `$x_{\alpha-2}\in F(x_{\unsure{\alpha|{}}})_{\alpha-2}$`
- `\deleted{$d,d'$ \unsure{\ldots}}` -> `\deleted{$d,d'$ \illegible{1}}`
- `\uline{\text{et}}` -> `\text{\uline{et}}`
- `\uline{\text{et}}` -> `\text{\uline{et}}`

Additional crop or encoding check at 2026-11-18T07:16:07Z.
At highest enlargement there is one covered group after the crossed pair of d’s. Its individual letters cannot be recovered. The underlined et was moved into a text box in both displays.

**Formulas and diagram register**

L1–7, continuation on the left.

- `$x$`
- `$y$`
- `$F_*$`
- `$\mathcal A$`

L8–9, F(x).

- `$F_\alpha$`
- `$x\in F_{\deleted{\unsure{*}}\inserted{\alpha}}$`
- `$F(x)$`
- `$y<x$`
- `$F_*$`
- `$n$`
- `$\alpha-1$`
- `$\alpha$`
- `$\geq 1$`
- `$\neq0$`

L10–11, first numbered condition.

- `$2\leq\alpha\leq n$`
- `$x_\alpha\in F_\alpha$`
- `$x_{\alpha-2}\in F(x_{\unsure{\alpha|{}}})_{\alpha-2}$`
- `$y_{\alpha-1}\in F(x_{\unsure{1|\alpha}})_{\alpha-1}$`
- `$x_{\alpha-2}$`

L10–11, left bracket.

- `$n\geq2$`

L12–13, second condition.

- `$x_1\in F_1$`
- `$y_0\in\deleted{\unsure{F_0,\ x}}\ F(x)_0$`
- `$x$`

L12–13, second left bracket.

- `$n\geq1$`

L14–18, maximal flags.

- `$\mathcal A$`
- `$\mathcal A$`
- `$\sigma_\alpha$`
- `$(0\leq\alpha\leq n\deleted{\unsure{\}}}-1)$`
- `$d=(x_0,x_1,\ldots,x_\nu)$`
- `$(\nu\leq n)$`
- `$x_i\in F_i$`
- `$(0\leq i\leq\nu)$`

L19–21, first operator.


~~~latex
\[
\begin{aligned}
\sigma_0(d)&=(x'_0,x_1,\ldots,x_\nu)\qquad\deleted{\text{où }x'_0\text{ est}}\ \text{caractérisé \unsure{par} la condition}\\
&\hspace{7em}x'_0\ne x_0\ \big[\text{\uline{et}}\quad(x'_0,x_1,\ldots x_\nu)\ \text{un drapeau}\\
&\hspace{7em}\text{i.e. }x'_0\in F(x_1)_0\big]\qquad\text{cf Axiome 2}
\end{aligned}
\]
~~~


L22–23, remaining operators.


~~~latex
\[
\begin{aligned}
1\leq\alpha\leq n-1\quad \sigma_\alpha(d)&=(x_0,\ldots x_{\alpha-1},x'_\alpha,x_{\alpha+1},\ldots)\quad\text{caractérisé par }x'_\alpha\ne x_\alpha\\
&\hspace{8em}\text{\uline{et}}\ \text{que }\sigma_\alpha(d)\ \text{est un drapeau.})
\end{aligned}
\]
~~~


L24–26, optional axiom.

- `$3'$`
- `$\forall x_{n-1}\in F_{n-1}$`
- `$y\in F_n$`
- `$x_{n-1}$`

L25–27, outer left bracket.

- `$n\geq1$`

L27–28, last operator.


~~~latex
\[
\sigma_n(d)=(x_0,\ldots,x_{n-1},x'_n),\quad \deleted{\text{où }x'_n\text{ est le}}\ \inserted{\text{caractérisé par }x'_n\ne x_n\quad\text{\unsure{(et\ldots)}}}
\]
~~~


L29–30, foot of left column.

- `$F(x)$`
- `$x\in F_\alpha$`
- `$1,2,3$`
- `$4$`
- `$n$`
- `$\alpha-1$`

R1–3, head of right column.

- `$1'$`
- `$3'$`
- `$2'$`
- `$\mathcal A$`
- `$F_*$`
- `$(F_\alpha),(I_\alpha)$`

R4–6, commutations.


~~~latex
\[
 \sigma_\alpha\sigma_\beta=\sigma_\beta\sigma_\alpha\qquad\text{si }|\beta-\alpha|\ne1\quad\text{i.e. }\alpha,\beta\ \text{non consécutifs.}
\]
~~~


R7–11, group and subgroup.

- `$G_n$`
- `$\sigma_\alpha$`
- `$(0\leq\alpha\leq n)$`
- `$\mathcal A$`
- `$G_n$`
- `$\sigma_\alpha$`
- `$G_n^{(\alpha)}$`
- `$(0\leq\alpha\leq n)$`
- `$G_n$`
- `$\sigma_\beta$`
- `$\beta\ne\alpha$`

R12–13, orbit map.


~~~latex
\[
 \mathcal A/G_n^{(\alpha)}\longrightarrow F_\alpha\qquad\unsure{(\text{si }\alpha\leq n-1)}
\]
~~~


R14–20, fourth axiom with justification.

- `$d=(x_0,\ldots x_n)$`
- `$d'=(\unsure{x_0|x'_0},\ldots x'_n)$`
- `$d,d'$`
- `$x_\alpha=x'_\alpha$`
- `$d$`
- `$d'$`
- `$\sigma_\beta$`
- `$\beta\ne\alpha$`

R21–24, a general type.

- `$\delta\subset[0,n]$`
- `$\delta\ne\varnothing$`
- `$G_n^{(\delta)}$`
- `$G_n$`
- `$\sigma_i$`
- `$i\in\complement_{[0,n]}\delta$`

R25, lower right.


~~~latex
\[
 \mathcal A/G_n^{(\unsure{\alpha|\delta})}\unsure{-|\to}\mathcal A_\delta\quad\text{(drapeaux de type }\delta\text{)}
\]
~~~


**Corrections, marginal writing and cancellations**

- L1–7, continuation on the left — `\inserted{l'ens ordonné}`, `\inserted{\deleted{\unsure{à is. près avec son ordre}} et des \unsure{paires} des drapeaux \unsure{maj. par} un drapeau}`, `\deleted{\unsure{à is. près avec son ordre}}`
- L1–4, extreme left — `\margin{au passage à l'ordre inverse près \ldots}`
- L8–9, F(x) — `\deleted{\unsure{$F_\alpha$}}`, `\deleted{\unsure{*}}`, `\inserted{\alpha}`, `\inserted{Il satisfait les m\textsuperscript{es} conditions que $F_*$, avec $n$ remplacé par $\alpha-1$ si $\alpha$\unsure{$\geq 1$|$\neq0$}.}`, `\deleted{On posera l'axiome}`
- L10–11, first numbered condition — `\inserted{$2\leq\alpha\leq n$}`, `\deleted{\unsure{Il}}`
- L10–11, left bracket — `\margin{\unsure{admettre|à mettre} seulement si $n\geq2$}`
- L12–13, second condition — `\deleted{\unsure{F_0,\ x}}`, `\deleted{incidents à $x$}`
- L12–13, second left bracket — `\margin{à \unsure{mettre} si $n\geq1$}`
- L14–18, maximal flags — `\deleted{\unsure{Définissons|Définir}}`, `\deleted{\unsure{de G}}`, `\deleted{\unsure{\}}}`
- L19–21, first operator — `\deleted{\text{où }x'_0\text{ est}}`
- L24–26, optional axiom — `\deleted{drapeaux}`
- L25–27, outer left bracket — `\margin{pour $n\geq1$ fixé}`
- L27–28, last operator — `\deleted{\text{où }x'_n\text{ est le}}`, `\inserted{\text{caractérisé par }x'_n\ne x_n\quad\text{\unsure{(et\ldots)}}}`
- R1–3, head of right column — `\inserted{et un axiome 4 plus bas}`
- R4–6, commutations — `\deleted{On \unsure{vérifie}}`, `\deleted{Les}`
- R7–11, group and subgroup — `\deleted{\unsure{rela\textsuperscript{ts}}}`, `\inserted{$(0\leq\alpha\leq n)$}`
- R14–20, fourth axiom with justification — `\deleted{\unsure{Proposition}}`, `\inserted{\uline{Axiome 4}}`, `\inserted{par l'axiome 1}`, `\deleted{$d,d'$ \illegible{1}}`, `\deleted{\unsure{op}}`
- R14–15, in the gutter — `\margin{le \unsure{rendre} naturel}`
- R21–24, a general type — `\inserted{$\delta\ne\varnothing$}`

**Index and exponent register**

- L14–18, maximal flags — `_i`, `_i`
- R21–24, a general type — `_i`


## Scan 5

Started 2026-11-18T07:02:39Z. Ended 2026-11-18T07:03:47Z.

**Image notes recorded before reopening the transcription**

Ceci dit, ‘naturelles’, parenthesis with two lowered n's and δ, δ′. Tiny interlinear after d’incidence. ‘De façon précise’, ‘Prop’, ‘cellulaires’, ‘renforcé ?’, ‘pl. fidèle’, ‘Il faudrait déterminer l’image essentielle.’ A separator with rising and horizontal strokes. ‘Réalisation géom.’, ‘le seul axiome 1’, ‘combinatoire’, ‘parties (finies) totᵗ ordonnées’. Final F has a heavy baseline with a lowered star. Archive 4.

**Comparison with the transcription**

In G the nearly closed rounded stroke and short horizontal return recur in the two copies under the inclusion; the right-hand δ has a prime. No indexed i or j. The tiny addition runs from d’incidence above ‘entre’; a long lead from the addition is distinct from the word entre. A darkened symbol precedes divers. The line under pl. fidèle ends after the last e, and does not strike the words. The bottom insertion (finies) points to parties. Two readings of the initial words in the parenthesis before ‘1’ remain possible. Both the D-like initial of the proposition and the separator were reviewed on the crops.

**Changes**

- `les deux axiomes 1` -> `\unsure{les deux axiomes|le seul axiome} 1`
- `tot. ordonnées` -> `\unsure{totᵗ|tot.} ordonnées`
- `totᵗ` -> `tot\textsuperscript{t}`

Additional crop or encoding check at 2026-11-18T07:16:07Z.
The raised t was encoded with a standard LaTeX command.

**Formulas and diagram register**

1–8, inclusion and incidence.

- `$G_n^\delta$`
- `$G_n^\delta\subset G_n^{\delta'}$`
- `$\delta'\subset\delta$`
- `$\delta$`
- `$\delta$`
- `$F_\alpha$`

10–14, proposition.

- `$(F_*)\unsure{\mapsto|\vdash}(\mathcal A)$`
- `$1,1',2,2',3,4$`
- `$G_n$`

after 16, separator.


~~~latex
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (-.95,0) -- (.95,.03); \draw (-.52,-.12) -- (.54,-.11) -- (.13,.16) -- (.13,-.43);\end{tikzpicture}}
~~~


17–21, geometric realization.

- `$F_{\unsure{\alpha|*}}$`
- `$F$`
- `$F_*$`

**Corrections, marginal writing and cancellations**

- 1–8, inclusion and incidence — `\inserted{(= \unsure{prolonger et restreindre|prolongement et restriction})}`, `\deleted{\unsure{$\delta$}}`
- 17–21, geometric realization — `\inserted{(finies)}`, `\deleted{\unsure{$F$}}`

**Index and exponent register**



## Scan 6

Started 2026-11-18T07:04:02Z. Ended 2026-11-18T07:04:53Z.

**Image notes recorded before reopening the transcription**

No running French prose. Aut, SA, SÃ, ST and S with tilde over T; strong differences between a separate tilde over ∂X and one over A. Z with a doubled diagonal in the grids, raised I. I=π₀(∂X) at right. Lone lower 1 under each of the first two middle columns, a very heavy 1 at bottom right. Pencilled diagonal from upper left to lower right across three distinct blocks. Side diagram has X at left and p on a vertical arrow. Archive 5.

**Comparison with the transcription**

Five structures were checked in order: upper extension, small hook and p, pairs equation, middle grid and bottom grid. The diagonal in the grids is a single thin manuscript stroke crossing the formula and intermediate white space, unlike the two dashed arrows. It does not individually obliterate the letters it crosses. The cross and double diagonal distinguish ℤ from Z; exponent I has no dot. Tildes lie over Aut, ∂X, A and T in different cells. The punctuation after p∘ṽ at the right is open. The small marks above X in the definition are unresolved. At the bottom the M and the apparent closing parenthesis are clearer than the opening. There is no identifiable lowercase j subscript; the isolated mark above X might be i. The far-right note reads I=π₀(∂X), with the subscript still marked.

**Changes**

- `\uline{$\mathrm{Aut}$}` -> `\text{\uline{Aut}}`
- `S\unsure{\mathcal M|\mathcal A^\circ}(X)` -> `S\unsure{\mathcal A^\circ|\mathcal M}(X)`
- `\mathcal M\unsure{(\widetilde{\partial X})|\partial X)}` -> `\mathcal M\unsure{\partial X)|(\partial X)|(\widetilde{\partial X})}`
- `\unsure{\prime\prime|i}` -> `\unsure{\prime\prime|i|\ast}`

**Formulas and diagram register**

top, automorphisms and vertical extension.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\& \& 1\\
1\arrow[r] \& {\text{\uline{Aut}}(X,\mathrm{id}_{\partial X})}\arrow[r] \& \mathrm{Aut}(X)\arrow[u]\arrow[r,dash] \& \mathrm{Aut}(\partial X)\arrow[r,dash] \& 1\\
\& {}\arrow[r] \& \widetilde{\mathrm{Aut}}(X)\arrow[u]\\
\& \& \mathbb Z^I\arrow[u]\\
\& \&1\arrow[u]
\end{tikzcd}}
~~~


upper left, boundary and projection.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
\& \widetilde{\partial X}\arrow[d,"p"]\\
 X\&\partial X\arrow[l,hook]
\end{tikzcd}}
~~~


upper middle, pairs of automorphisms.


~~~latex
\[
\begin{aligned}
\underset{\substack{\rotatebox{90}{$\scriptstyle\subset$}\\
\mathrm{Aut}(X)\times\mathrm{Aut}(\widetilde{\partial X})}}{\widetilde{\mathrm{Aut}}(\overset{\unsure{\prime\prime|i|\ast}}{X})}
=\bigl\{(u,\widetilde v)\mid u\in\mathrm{Aut}(X),\widetilde v\in\mathrm{Aut}(\widetilde{\partial X}),\
(u\mathbin{\upharpoonright}\partial X)\circ p=p\circ\widetilde v
\end{aligned}
\]
~~~


middle, grid with dashed diagonal.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small,execute at end picture={\draw[thin] ([xshift=-4pt,yshift=3pt]\tikzcdmatrixname-1-3.north west) -- ([xshift=2pt]\tikzcdmatrixname-5-3.south east);}]
\&1\&1\\
1\arrow[r,dash]\& S\mathcal A(X)\arrow[u]\arrow[r]\arrow[dr,dashed]\&\mathcal A(X)\arrow[u]\arrow[r]\&\mathcal A(\partial X)\arrow[r,dash]\&1\\
1\arrow[r,dash]\& \underset{S\mathcal A(X)\times\mathbb Z^I}{S\widetilde{\mathcal A}(X)}\arrow[u]\arrow[r]\&\widetilde{\mathcal A}(X)\arrow[u]\arrow[r]\&\mathcal A(\widetilde{\partial X})\arrow[u,"\unsure{1|\wr}"]\arrow[r,dash]\&1\\
1\arrow[r,dash]\&\mathbb Z^I\arrow[u]\arrow[r,Rightarrow]\&\mathbb Z^I\arrow[u]\arrow[r,dash]\&1\arrow[u]\arrow[r,dash]\&1\\
\&1\arrow[u]\&1\arrow[u]
\end{tikzcd}}
~~~


middle grid, far right.

- `$I=\pi_{\unsure{0|n}}(\partial X)$`

bottom, grid with quotients.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small,execute at end picture={\draw[thin] (\tikzcdmatrixname-1-3.south east) -- (\tikzcdmatrixname-5-4.south east);}]
\&1\&\unsure{1|\wedge}\&1\\
1\arrow[r,dash]\&ST(X)\arrow[u]\arrow[r]\arrow[dr,dashed]\&\mathcal A(X)/S\mathcal A^\circ(X)\arrow[u]\arrow[r,dash]\&\mathcal A(\partial X)\arrow[u]\arrow[r,dash]\&1\\
1\arrow[r]\&\underset{\unsure{\simeq}ST(X)\times\mathbb Z^I}{S\widetilde T(X)}\arrow[u]\arrow[r]\&\widetilde{\mathcal A}(X)/S\unsure{\mathcal A^\circ|\mathcal M}(X)\arrow[u]\arrow[r,dash]\&\mathcal M\unsure{\partial X)|(\partial X)|(\widetilde{\partial X})}\arrow[u,"\unsure{\sim|2}"]\arrow[r,dash]\&1\\
1\arrow[r,dash]\&\mathbb Z^I\arrow[u]\arrow[r,Rightarrow]\&\mathbb Z^I\arrow[u]\arrow[r]\&\unsure{1|?}\arrow[u]\arrow[r,dash]\&1\\
\&1\arrow[u]\&1\arrow[u]\&\deleted{\unsure{1|?}}1\arrow[u]
\end{tikzcd}}
~~~


**Corrections, marginal writing and cancellations**

- middle grid, far right — `\margin{$I=\pi_{\unsure{0|n}}(\partial X)$}`
- bottom, grid with quotients — `\deleted{\unsure{1|?}}`

**Index and exponent register**



## Scan 7

Started 2026-11-18T07:04:54Z. Ended 2026-11-18T07:05:57Z.

**Image notes recorded before reopening the transcription**

‘réalisent une partition’, parenthetical ‘à structure conique’ high to right, ‘simplexes subdivision’ and ‘d’autre’, ‘équivalence de catégories’, ‘version objets combinatoires’, ‘à dégager’. Underlined Prop, ‘top.’ and added ‘petit x’ or ‘petit …’; two lists of numbered axioms, one includes 3′. ‘il f. et s.’, ‘sphère’, square bracket ‘en fait’, ‘si on a l’hyp. de Poincaré’, ‘simplemᵗ connexe’, superscript-shaped 3,4 after α, added threshold beneath the crossed one. Bottom drawing between sections. X₀, X₁, Xₙ, Xᵢ, ‘fibré/filtré’, ‘réunion de boules B’, quotation pair round drapeaux, ‘à définir avec soin’.

**Comparison with the transcription**

At the correction over the homology phrase the cancellation runs through ait; the long loop that follows leads to the interlinear insertion and leaves l’homologie live. A small numeral with a heavy top after ≥ looks like 5; the earlier threshold is overwritten. At top, the first line can be read ‘comme parties’; the lead from the parenthesis ascends over parties. The return stroke beside the proposition is a bracket. The sign in front of i=0 in the last section has its own crossing. Each i in X and the superscript of D is distinct from the upright 1. F is plain, and the flag set has a looped capital. The sheet has staves but no typed corrections.

**Changes**

- `[la ré. à` -> `[\unsure{la ré.|la réᵒ} à`
- `\inserted{pure}` -> `\inserted{\unsure{pure|petit}}`
- `\deleted{ait l'homologie} \inserted{pour $\alpha\geq5$, il ait de plus} d'une` -> `\deleted{ait} \inserted{pour $\alpha\geq5$, il ait de plus} l'homologie d'une`
- `On suppose \unsure{\ldots} est` -> `On suppose \unsure{$X$} est`
- `réᵒ` -> `ré\textsuperscript{o}`

Additional crop or encoding check at 2026-11-18T07:16:07Z.
The cancelled material after suppose appears to end with the two arms of an X. Superscript o is encoded explicitly.

**Formulas and diagram register**

1–7, realization of elements.

- `$F_\alpha$`
- `$|F_*|$`
- `$x\in F_{\unsure{n|\alpha}}$`
- `$\leq x$`

8–10, proposition beside vertical rule.

- `$|F_*|$`
- `$n$`
- `$(F_\alpha)$`
- `$\deleted{\unsure{I}}1,1',2,\unsure{2'|2},3,4$`

10–14, more precise criterion.

- `$(F_*)$`
- `$n$`
- `$(F_*)$`
- `$1,1',2,2',3,3',4$`
- `$\forall x\in F_\alpha$`
- `$(\alpha\geq3)$`
- `$F(x)$`

14–18, nested qualification.

- `$\alpha\geq\unsure{3,4|3?}$`
- `$|F(x)|$`
- `$\alpha\geq5$`

after 18, divider.


~~~latex
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (-1.55,.3)--(1.5,.44); \draw (-1,-.02).. controls (.7,.12) and (.65,.05) ..(.45,.4).. controls (.11,.86) and (.25,.72) ..(.16,.15)--(.16,-.58)--(-.54,-.4)--(.98,-.33);\end{tikzpicture}}
~~~


19–20, filtered space.

- `$X$`

~~~latex
\[
 X_0\subset X_1\subset\ldots\subset X_n=X.
\]
~~~

- `$X$`
- `$X$`
- `$n$`

21–23, successive differences.

- `$\forall i=0,\ldots,n-1$`
- `$X_{i+1}$`
- `$X_i$`
- `$D^{i+1}$`

23–26, flags of the filtration.

- `$\mathcal A$`
- `$G_{n\unsure{(+1)|+1}}$`
- `$G_n$`
- `$X$`
- `$n$`

**Corrections, marginal writing and cancellations**

- 1–7, realization of elements — `\inserted{(à structure \unsure{cônique|conique})}`, `\deleted{fermés}`, `\inserted{\unsure{corresp}}`, `\deleted{\unsure{top.}}`
- 8–10, proposition beside vertical rule — `\inserted{\unsure{pure|petit}}`, `\deleted{\unsure{I}}`
- 10–14, more precise criterion — `\inserted{$(\alpha\geq3)$}`
- 14–18, nested qualification — `\deleted{\unsure{et}}`, `\deleted{pour $\alpha\geq\unsure{3,4|3?}$}`, `\deleted{ait}`, `\inserted{pour $\alpha\geq5$, il ait de plus}`
- 19–20, filtered space — `\inserted{(\unsure{compact ?})}`, `\deleted{On suppose \unsure{$X$} est}`, `\inserted{$X$ \unsure{var.} de dim $n$}`
- 21–23, successive differences — `\deleted{une variété}`, `\inserted{homéomorphe}`, `\deleted{boule de di\unsure{m}}`, `\inserted{une}`
- 23–26, flags of the filtration — `\deleted{\unsure{resp. =}}`

**Index and exponent register**

- 21–23, successive differences — `_{i+1}`, `_i`, `^{i+1}`


## Scan 8

Started 2026-11-18T07:05:58Z. Ended 2026-11-18T07:06:57Z.

**Image notes recorded before reopening the transcription**

‘ss pt fixe.’ Eight-line question about image essentielle: ‘admettre l’hyp. de Poincaré au besoin’, ‘cellulaires se réalisant suivant une variété topologique....’. Des ‘variétés de dim n’ raised above X filtrés. Darker second half ‘n-Variété combinatoire’, ‘finie’ inserted above title, ‘fini’ over Dₙ, ‘autom. invol.’, ‘deux σᵢ non consécutifs’, ‘op. sans pts fixes’. Next heading ‘n-complexe combinatoire fini’. List Dₙ through D₀ and a small downward definition of D₀. Bottom has i and j in same inequality, specifically i≥j+2≥j≥0, and a crossed start before that inequality.

**Comparison with the transcription**

The separate descending pointer beneath D₀ ends beside a quoted word. Its attachment was moved from ‘Gᵢ₋₁-ensemble’ to D₀; the pointed word remains doubtful. Finis above ‘ens’ and finie above the heading have different endings. The lower Dᵢ is an insertion after chaque, and the darker Dᵢ before G is cancelled. Subscripts i in σ and D have a dot without descender; j in the last inequality descends. The group index changes from i−1 to i−2 in the last statement. The printed-looking rules visible on earlier sheets do not appear here. Plain D and G, no double stroke on either heading.

**Changes**

- `\unsure{mettant|moyennant}` -> `\unsure{admettre|mettre|moyennant}`
- `D_1,D_0$ d'ens` -> `D_1,\underset{\substack{\downarrow\\\text{``\unsure{spécial|points}''}}}{D_0}$ d'ens`
- `\inserted{``spécial''} (` -> `(`

**Formulas and diagram register**

1, continuation.

- `$\sigma_i$`

2–5, proposition.

- `$n$`
- `$X$`
- `$G_n$`
- `$\sigma_i$`

12–16, combinatorial variety.

- `$n$`
- `$D_n$`
- `$\sigma_i$`
- `$(0\leq i\leq n)$`
- `$\sigma_i$`
- `$D_n$`
- `$G_n$`
- `$\sigma_i$`
- `$(0\leq i\leq n)$`

17–20, combinatorial complex.

- `$n$`
- `$D_n,D_{n-1},\ldots,D_1,\underset{\substack{\downarrow\\\text{``\unsure{spécial|points}''}}}{D_0}$`
- `$D_i\ (1\leq i\leq n)$`
- `$D_i$`
- `$G_{i-1}$`
- `$\sigma_\alpha$`

21, sequence of applications.


~~~latex
\[
 D_n\to D_{n-1}\longrightarrow D_{n-2}\longrightarrow\ldots\longrightarrow D_1\longrightarrow D_0
\]
~~~


22–23, compatibility, continues.

- `$\forall\,2\leq i\leq n$`
- `$D_i\to D_{i-1}$`
- `$G_{i-2}$`
- `$\deleted{\unsure{2\leq j\geq{}}}i\geq j+2\geq j\geq0$`

**Corrections, marginal writing and cancellations**

- 2–5, proposition — `\inserted{variétés de dim $n$}`
- 12–16, combinatorial variety — `\inserted{\uline{finie}}`, `\inserted{fini}`
- 17–20, combinatorial complex — `\inserted{finis}`, `\inserted{$D_i\ (1\leq i\leq n)$}`, `\deleted{\unsure{$D_i$}}`, `\deleted{\unsure{à él\textsuperscript{ts}}}`
- 22–23, compatibility, continues — `\deleted{\unsure{2\leq j\geq{}}}`

**Index and exponent register**

- 1, continuation — `_i`
- 2–5, proposition — `_i`
- 12–16, combinatorial variety — `_i`, `_i`, `_i`
- 17–20, combinatorial complex — `_i`, `_i`, `_{i-1}`
- 22–23, compatibility, continues — `_i`, `_{i-1}`, `_{i-2}`


## Scan 9

Started 2026-11-18T07:06:57Z. Ended 2026-11-18T07:07:44Z.

**Image notes recorded before reopening the transcription**

‘l’application composée’, ‘soit invariante’, ‘n-variété combinatoire’, ‘Gₙ-ens.’; near the next line bord written above barred word, closure/piece ‘∂(…(Xᵢ/Xᵢ₋₁))’; D vs δ as initial in the four successive rows. Distinct right-hand j in Dⱼ, Gⱼ₋₁, σⱼ₊₁. Under the crossed lines: ‘On définira par récurrence la cat. …’, ‘complexes’, ‘triangulations’, ‘de son cercle’? arrows to an interlinear note; C₀, ‘ens finis’, ‘catégorie’, ‘obj’, iₙ₋₁, φ: … . Far-right third contains only staves and punches.

**Comparison with the transcription**

The cancellation begins below the aligned δ rows. It crosses the whole later definition including the final open parenthesis. The added cartes, cat. des and the hooked side definition are themselves within the cancelled draft; the separate insertions and deletions remain recorded inside it. The horizontal staves leave the upper conditions and boundary rows live. Rechecked every i and j in Dᵢ, Dⱼ, Gⱼ₋₁, σⱼ₊₁ and the decreasing σ subscripts in each row. Small italic i in the crossed functor differs from j at the head. The handwritten C and V of the categories are less distinct than D. Numeral 8 in the lower corner is separate from the draft.

**Changes**

- `bord du \unsure{$i$-découpage|$i$-découpé}` -> `bord \unsure{du le|de la|du} \unsure{$i$-découpage|$i$-découpé}`

**Formulas and diagram register**

1–3, continuation.

- `$D_i\unsure{-|\to}D_j$`
- `$G_{j-1}$`
- `$\sigma_{i-1},\ldots,\sigma_{j+1}$`

4, equivalence.

- `$n$`
- `$\leftrightarrow G_n$`
- `$D_n$`

5–6, boundary.

- `$0\leq i\leq n$`
- `$(i-1)$`
- `$i$`
- `$i$`
- `$\delta_{i-1}$`
- `$\partial(\unsure{\mathrm{Déc}|\mathrm{déc}}(X_i/X_{i-1})$`
- `$i-1$`

7–11, successive boundary objects.


~~~latex
\[
\begin{aligned}
\delta_{n-1}&=(D_n\,;\sigma_0,\ldots\sigma_{n-1})\\
\delta_{n-2}&=(D_n/\sigma_n\,;\sigma_0,\ldots,\sigma_{n-2})\\
\delta_{n-3}&=(D_n/(\sigma_n,\sigma_{n-1})\,;\sigma_0,\ldots,\sigma_{n-3})\\
&\ldots\\
\delta_{i-1}&=(D_n/(\sigma_n,\ldots\sigma_{i+1})\,;\sigma_0,\ldots\sigma_{i-1})
\end{aligned}
\]
~~~


12–13, beginning of crossed block.

- `$n$`
- `$\mathcal C_n$`
- `$n$`
- `$i_n:\mathcal C_n\to\mathcal V_n$`

13–14, at right of crossed block.

- `$n$`

14–18, crossed definitions.


~~~latex
\[
\begin{aligned}
&\deleted{\mathcal C_0=\deleted{0\text{-complexes}}\inserted{0\text{-\unsure{espaces}}}\ \text{comb.}=\text{ens finis}}\\
&\deleted{\ldots}\\
&\deleted{\mathcal C_n=\inserted{\text{cat. des}}\ \{X_{n-1},S_{n-1},p\}\quad\text{où}\quad X_{n-1}\in\operatorname{Ob}\mathcal C_{n-1}}\\
&\hspace{13em}\deleted{S_{n-1}\in\operatorname{Ob}\unsure{\mathcal V_{n-2}|\mathcal V_{n-1}},\ \deleted{\text{\unsure{convient}}}}\\
&\hspace{13em}\deleted{\varphi:i_{n-1}(\unsure{S_{n-1}|b_{n-1}})\to X_{n-1}}
\end{aligned}
\]
~~~


19–21, crossed functor and unfinished expression.

- `$i_n:\unsure{\mathcal V_n|\mathcal C_n}\to\mathcal C_n$`

~~~latex
\[
 \deleted{i_n(\underset{\substack{\searrow\\G_n\text{-ens.}}}{D_n})=(}
\]
~~~


**Corrections, marginal writing and cancellations**

- 5–6, boundary — `\deleted{\unsure{$(i-1)$-découpé}}`, `\inserted{bord \unsure{du le|de la|du} \unsure{$i$-découpage|$i$-découpé}}`, `\inserted{$\partial(\unsure{\mathrm{Déc}|\mathrm{déc}}(X_i/X_{i-1})$}`
- 12–13, beginning of crossed block — `\deleted{On définit par réc. sur $n$ la cat. $\mathcal C_n$ des $n$-\deleted{\unsure{complexes}}\inserted{cartes} combinatoires, \deleted{en posant} \inserted{(finies) et foncteur \unsure{$i_n:\mathcal C_n\to\mathcal V_n$}}}`, `\deleted{\unsure{complexes}}`, `\inserted{cartes}`, `\deleted{en posant}`, `\inserted{(finies) et foncteur \unsure{$i_n:\mathcal C_n\to\mathcal V_n$}}`
- 13–14, at right of crossed block — `\margin{\deleted{$n$-var. comb.}}`, `\deleted{$n$-var. comb.}`
- 14–18, crossed definitions — `\deleted{\mathcal C_0=\deleted{0\text{-complexes}}\inserted{0\text{-\unsure{espaces}}}\ \text{comb.}=\text{ens finis}}`, `\deleted{0\text{-complexes}}`, `\inserted{0\text{-\unsure{espaces}}}`, `\deleted{\ldots}`, `\deleted{\mathcal C_n=\inserted{\text{cat. des}}\ \{X_{n-1},S_{n-1},p\}\quad\text{où}\quad X_{n-1}\in\operatorname{Ob}\mathcal C_{n-1}}`, `\inserted{\text{cat. des}}`, `\deleted{S_{n-1}\in\operatorname{Ob}\unsure{\mathcal V_{n-2}|\mathcal V_{n-1}},\ \deleted{\text{\unsure{convient}}}}`, `\deleted{\text{\unsure{convient}}}`, `\deleted{\varphi:i_{n-1}(\unsure{S_{n-1}|b_{n-1}})\to X_{n-1}}`
- 19–21, crossed functor and unfinished expression — `\deleted{$i_n:\unsure{\mathcal V_n|\mathcal C_n}\to\mathcal C_n$ défini par}`, `\deleted{i_n(\underset{\substack{\searrow\\G_n\text{-ens.}}}{D_n})=(}`

**Index and exponent register**

- 1–3, continuation — `_i`, `_j`, `_{j-1}`, `_{i-1}`, `_{j+1}`
- 5–6, boundary — `_{i-1}`, `_i`, `_{i-1}`
- 7–11, successive boundary objects — `_{i-1}`, `_{i+1}`, `_{i-1}`


## Scan 10

Started 2026-11-18T07:07:44Z. Ended 2026-11-18T07:08:39Z.

**Image notes recorded before reopening the transcription**

Cartes coniques, cartes cellulaires, et ens. à opérateurs. ‘Une n-carte conique (finie)’, ‘top., X compact’, ‘filtration croissante’, ‘fermées’ underlined. ‘i.e. discret’, ‘Déc’, ‘découpage’, ‘induisant’, ‘isom.’, ‘nb fini’, ‘comp. connexes’, ‘hom. au cône’. ‘morphisme fini’, ‘équisingul…’, note with question near c/d. Cas n=0 espaces finis discrets, cas n=1 X=X₁⊃X₀ with ‘cpt’ below. Numerous dotted and barred Z’s, tiny primes in restriction note, mixed x and X labels. A loop, two segments, Y, tiny diagonal segment, three/four curved arcs and a shaded angle. Lower left 9.

**Comparison with the transcription**

Checked both cancellations of complexes in the title and the independent line through cellulaires. The two leaders place finie after conique and par des parties fermées after croissante. In condition b, upper bars on Z and dots on Z are not interchangeable. The superscript alpha is separate from the lowered i in the cone equation. The fine insertion at équisingulière contains j and i−1. The descending part of j also appears in the difference of strata. In the schematic rows, lowercase x and uppercase X differ by size and stroke; several superseded x-like labels remain unresolved. The last two sides of the right-hand restriction diagram appear as lines without heads. The shaded sector has short internal hatch marks. No double-struck capital was found in either heading.

**Changes**

- `est isom. au cône` -> `est \unsure{isom.|hom.} au cône`
- `est \unsure{constant} sur chaque \unsure{comp.} de` -> `est \unsure{constant|constante} sur \unsure{les|une} \unsure{comp.|c.c.} de`
- `\unsure{Soit} image` -> `\unsure{Soit|Soit l'} image`

**Formulas and diagram register**

2–5, filtered space.

- `$n$`
- `$X$`

~~~latex
\[
 X_0\subset X_1\subset\ldots\subset X_{n-1}\subset X_n=X
\]
~~~


6, first condition.

- `$X_0$`

7–12, second condition.

- `$1\leq i\leq n$`
- `$\bar Z_i={}$`
- `$\operatorname{Déc}(X_i/X_{i-1})\deleted{=\bar Z_i}$`
- `$X_i$`
- `$X_{i-1}$`
- `$\dot Z_i=\bar Z_i\mid X_{i-1}$`
- `$Z_i\to X_i$`
- `$\bar Z_i-\dot Z_i\longrightarrow X_i-X_{i-1}$`
- `$\bar Z_i$`
- `$\bar Z_i^\alpha$`
- `$\dot Z_i^\alpha=\bar Z_i^\alpha\cap\dot Z_i$`
- `$\dot Z_i^\alpha\ne\varnothing$`

13, finite morphism.

- `$\dot Z_i\to X_{i-1}$`

14, fourth condition and interline.

- `$X$`
- `$\Leftrightarrow\bar Z_i\to X_{\unsure{j|i}-1}$`
- `$X_j-X_{j-1}$`
- `$(j\leq i-1)$`

14–16, right of examples.

- `$X'_{i-1}$`
- `$\bar Z_i$`
- `$X_{i-1}$`
- `$X'_i$`
- `$X'_{i-1}=\overline{X'_{i-1}\cap\complement X_{i-2}}$`

15–16, small dimensions.

- `$n=0$`
- `$n=1$`
- `$\underbrace{X=X_1}_{\text{cpt}}\supset X_0$`

lower left, decomposition in dimension one.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=tiny]
\dot Z_1\arrow[d]\&{}=\coprod_\alpha\dot Z_1^\alpha\\
X_0
\end{tikzcd}}
~~~


lower right, dimensions zero to three.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=1ex]
\overset{\deleted{\unsure{x}}}{\dot x_0}\in\overset{\deleted{\unsure{x}}}{y_1}\&\&\overset{\deleted{\unsure{x}}}{\dot x_1}\quad y_2\\
\dot Z_1\arrow[d]\arrow[r,phantom,"\subset" description]\&\overset{\deleted{\unsure{m}}}{\bar Z_1}\arrow[d]\&\dot Z_2\arrow[dl]\arrow[r,phantom,"\subset" description]\&\bar Z_2\arrow[d]\&\dot Z_3\arrow[dl]\arrow[r,phantom,"\subset" description]\&\bar Z_3\arrow[d]\\
 X_0\arrow[r,phantom,"\subset" description]\&X_1\arrow[rr,phantom,"\subset" description]\&\&X_2\arrow[rr,phantom,"\subset" description]\&\&X_3\\
 x_0\arrow[r,phantom,"\subset" description]\&x_1\arrow[rr,phantom,"\subset" description]\&\&x_2\arrow[rr,phantom,"\subset" description]\&\&x_3
\end{tikzcd}}
~~~


lower left, loop with a point.


~~~latex
\figure{\begin{tikzpicture}[scale=.65]\draw (0,0)..controls (.2,.8) and (1.2,1.15)..(1.44,.66)..controls (1.55,.33) and (.45,-.16)..(0,0);\fill (0,0) circle (.055);\end{tikzpicture}}
~~~


lower left, sloping interval.


~~~latex
\figure{\begin{tikzpicture}[scale=.75]\draw (0,0)--(1.22,.6);\fill (0,0) circle (.09) (.61,.29) circle (.025) (1.22,.6) circle (.1);\end{tikzpicture}}
~~~


lower left, nearly horizontal interval.


~~~latex
\figure{\begin{tikzpicture}[scale=.75]\draw (0,0)--(1.85,.14);\fill (0,0) circle (.12) (1.85,.14) circle (.065);\end{tikzpicture}}
~~~


lower right, general ranks.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=1ex]
\dot x_{i+1}\&\dot Z_{i+1}\arrow[d]\arrow[r,phantom,"\subset" description]\& Z_{i+1}\arrow[d,dash]\&\dot Z_{i+2}\arrow[dl]\arrow[r,phantom,"\subset" description]\&\bar Z_{i+2}\arrow[d]\\
X_{i-1}\arrow[r,phantom,"\subset" description]\&X_i\arrow[r,phantom,"\subset" description]\& X_{i+1}\arrow[rr,phantom,"\subset" description]\&\&X_{i+2}\\
\&x_i\&\&\&x_{i+2}
\end{tikzcd}}
~~~


lower left, three branches.


~~~latex
\figure{\begin{tikzpicture}[scale=.75]\draw (-.63,.65)--(0,0)--(.82,.55) (0,0)--(-.08,-.74); \draw (-.63,.65) to[bend right=18](-.25,.24); \fill (-.63,.65) circle(.09) (.82,.55) circle(.09) (-.08,-.74) circle(.1);\end{tikzpicture}}
~~~


beside three branches, short stroke.


~~~latex
\figure{\begin{tikzpicture}[scale=.7]\draw[line width=1.2pt](0,0)--(.45,.47);\fill(.45,.47)circle(.055);\end{tikzpicture}}
~~~


bottom left, curved arcs.


~~~latex
\figure{\begin{tikzpicture}[scale=.8]\draw (0,0)..controls (.14,.48) and (.77,.68)..(1.09,.73)..controls (.92,.42) and (.45,.08)..(.14,.02); \draw (0,0)..controls (.82,-.1) and (1.16,.34)..(1.17,.72)..controls (1.59,.47) and (1.61,-.9)..(0,0);\fill (0,0)circle(.055);\end{tikzpicture}}
~~~


bottom middle, sector and rays.


~~~latex
\figure{\begin{tikzpicture}[scale=.8]\draw[thick](.61,.8)--(0,0)--(.76,-.7); \draw (-1.04,.24)--(0,0)--(-.28,-.61); \fill(0,0)circle(.11); \foreach \x/\y in {.52/.58,.41/.45,.34/.3,.31/.14,.31/-.02,.35/-.2,.48/-.35,.6/-.49}{\draw (\x,\y)--++(.19,-.02);}\end{tikzpicture}}
~~~


bottom right, restricted terms.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
{\dot Z_{i+2}|X_{i-1}}\arrow[d,dash]\arrow[r,phantom,"\subset" description]\&{\dot Z_{i+2}|X_i}\arrow[d]\arrow[r,dash]\&\bar Z_{i+2}\arrow[d]\\
X_{i-1}\arrow[r,phantom,"\subset" description]\&X_i\arrow[r,phantom,"\subset" description]\&X_{i+2}
\end{tikzcd}}
~~~


bottom left, dimension-one square.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=tiny,column sep=small]
\dot Z_1\arrow[d]\arrow[r,phantom,"\subset" description]\&\bar Z_1\arrow[d]\\
X_0\arrow[r,phantom,"\subset" description]\&X_1
\end{tikzcd}}
~~~


**Corrections, marginal writing and cancellations**

- 1, title — `\deleted{Complexes}`, `\inserted{Cartes}`, `\deleted{complexes}`, `\inserted{cartes}`, `\deleted{cellulaires}`
- 2–5, filtered space — `\inserted{(finie)}`, `\inserted{par des parties \uline{fermées}}`
- 7–12, second condition — `\inserted{soit $\bar Z_i={}$}`, `\deleted{=\bar Z_i}`, `\deleted{les composantes}`, `\inserted{$\bar Z_i$ a un n\textsuperscript{b} \uline{fini} de comp. connexes,}`
- 13, finite morphism — `\deleted{dont l'image}`
- 14, fourth condition and interline — `\deleted{\unsure{c)}}`, `\inserted{[$\Leftrightarrow\bar Z_i\to X_{\unsure{j|i}-1}$ est \unsure{constant|constante} sur \unsure{les|une} \unsure{comp.|c.c.} de $X_j-X_{j-1}$ $(j\leq i-1)$]}`
- 14–16, right of examples — `\margin{d) \unsure{Soit|Soit l'} image \inserted{$X'_{i-1}$} de $\bar Z_i$ ds $X_{i-1}$ \deleted{\unsure{$X'_i$}} Alors $X'_{i-1}=\overline{X'_{i-1}\cap\complement X_{i-2}}$}`, `\inserted{$X'_{i-1}$}`, `\deleted{\unsure{$X'_i$}}`
- lower right, dimensions zero to three — `\deleted{\unsure{x}}`, `\deleted{\unsure{x}}`, `\deleted{\unsure{x}}`, `\deleted{\unsure{m}}`

**Index and exponent register**

- 7–12, second condition — `_i`, `_i`, `_{i-1}`, `_i`, `_i`, `_{i-1}`, `_i`, `_i`, `_{i-1}`, `_i`, `_i`, `_i`, `_i`, `_i`, `_{i-1}`, `_i`, `_i`, `_i`, `_i`, `_i`, `_i`
- 13, finite morphism — `_i`, `_{i-1}`
- 14, fourth condition and interline — `_i`, `_{\unsure{j|i}-1}`, `_j`, `_{j-1}`
- 14–16, right of examples — `_{i-1}`, `_i`, `_{i-1}`, `_i`, `_{i-1}`, `_{i-1}`, `_{i-2}`
- lower right, general ranks — `_{i+1}`, `_{i+1}`, `_{i+1}`, `_{i+2}`, `_{i+2}`, `_{i-1}`, `_i`, `_{i+1}`, `_{i+2}`, `_i`, `_{i+2}`
- bottom right, restricted terms — `_{i+2}`, `_{i-1}`, `_{i+2}`, `_i`, `_{i+2}`, `_{i-1}`, `_i`, `_{i+2}`


## Scan 12

Started 2026-11-18T07:08:39Z. Ended 2026-11-18T07:09:31Z.

**Image notes recorded before reopening the transcription**

‘Ens ordonné des cellules … ass. Xᵢ’, X with bar above the lower pair. ‘Géométrie des drapeaux de dim ≤ n’, ‘Ex’, ‘épi !!’ in the first fork, ‘si i=Sup I i.e. i∈I⊂[0,i]’. Pyramids of D with subscripts 0,1,2 and 0,1,2,3; D₀₁₂(P/F), disjoint scribbles to its left, two heavy bars or intervals at its right. ‘Dσ—Dσ′ épi si σ′⊂σ est segment final de σ’, σ double-prime and smaller-than. D₃ beside striped wedge, nested u/n subscript j and sum over j<i. Four lines in each bottom column with mixed headed and bare horizontal strokes. Ink weight varies greatly; the mid-upper sheet rectangle is a fold.

**Comparison with the transcription**

Followed the dark arrows to D₃ and the thin arcs back to D₀₁ and D₂. In the lower large diagram the short horizontal bar between D₀₁₂ and D₀₃ has no visible head; the bent arrow terminates beside D₂. These are separate strokes. The upper and lower copies of the three-level fork have different line weights and heads. A double underline belongs to épi beside D_I; a single underline and two exclamation strokes belong to the first fork. At left, the vertical beneath D₁₂₃ points to D₁₃; the repetition lower down has a line across its top. Lower wedge and interval captions are particularly difficult. The lowered j below the sum has a tail, unlike i in nᵢ. Plain D has a single outline even at the headings. No typed text.

**Changes**

- `\unsure{1?|2?}` -> `\unsure{13|23|1?}`
- `\arrow[ddrr,bend left=65]` -> `\arrow[dd,bend left=65]\arrow[rr,dash]`
- `\arrow[dl,]` -> `\arrow[dl]`
- `$i=\operatorname{Sup} I$` -> `$\unsure{i|1}=\operatorname{Sup} I$`

**Formulas and diagram register**

1, opening.

- `$X_i$`

2–3, two lines of X terms.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=tiny]
\bar X_{i-1}\arrow[d,dash]\\ X_{i-1}\quad X_i\&X_i
\end{tikzcd}}
~~~


4, heading.

- `$\leq n$`

5, examples.

- `$n=0$`
- `$D_0$`

6–7, first fork.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
n=1\&\&D_{01}\arrow[dl]\arrow[dr,"\text{\uline{épi} !!}"]\\
\&D_0\&\&D_1
\end{tikzcd}}
~~~


7–8, scratched repetition to the left.

- `$\deleted{\bar X_{i-1}}\quad\deleted{X_{i-1}\ X_i}$`
- `$n=2$`

8–10, three levels below the long line.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=0.4em,row sep=small]
\&\& D_{012}\arrow[dl,dash]\arrow[d,dash]\arrow[dr,"\text{épi}",dash]\\
\&D_{01}\arrow[dl,dash]\arrow[dr,"\text{épi}"']\&D_{02}\arrow[dll,dash]\arrow[drr,dash]\&D_{12}\arrow[dl,dash]\arrow[dr,"\text{épi}",dash]\\
 D_0\&\&D_1\&\&D_2
\end{tikzcd}}
~~~


8–10, right of the triangle.

- `$D_{01\ldots i}\to D_I$`
- `$\unsure{i|1}=\operatorname{Sup} I$`
- `$i\in I\subset[0,i]$`

11, central label.

- `$D_I$`

12–15, central fork with F labels.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=.5em]
\&\&D_{012}(\unsure{F|f})\arrow[ddl,dash]\arrow[d]\arrow[dr,"\text{épi}"]\\
\&\&D_{02}(F)\arrow[ddll,dash,bend left=15]\arrow[ddrr,dash,bend right=10]\&D_{12}(F)\arrow[ddl,bend right=12]\arrow[ddr,"\unsure{e}"]\\
\&D_{01}\arrow[dl,dash]\arrow[dr]\\
D_0\&\&D_1\&\&\unsure{\{M\}|\{m\}}
\end{tikzcd}}
~~~


12–14, separate square at right.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
D_{012}\arrow[r]\arrow[d]\&D_{12}\arrow[d,dash]\\
D_{02}\arrow[r]\&D_2
\end{tikzcd}}
~~~


14–16, left-hand scratch.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=tiny,column sep=small]
j\quad j{+}1\&D_{123}\arrow[d]\\
\deleted{D_{j\ldots j}}\&D_{13}\\
\&\overline{D_{13}}
\end{tikzcd}}
~~~


15–16, central bracket.


~~~latex
\figure{\begin{tikzpicture}[scale=.65]\draw[line width=2pt](-.7,.28)--(.83,.28); \foreach \x in {0,.42,.83}{\draw[thick](\x,.28)--(\x,.1);} \foreach \x/\v in {0/2,.42/3,.83/4,1.28/5}{\node at (\x,-.12){$\v$};} \draw[very thick](0,-.41)--(0,-.48)--(1.28,-.48)--(1.28,-.38);\end{tikzpicture}}
~~~


15–16, pair of intervals at right.


~~~latex
\figure{\begin{tikzpicture}[scale=.8]\draw (0,0)--(1.35,0) (0,-.15)--(0,.18) (1.35,-.14)--(1.35,.13); \node at (.78,-.57){$\unsure{13|23|1?}$}; \draw(1.94,0)--(3.16,-.06) (1.94,-.15)--(1.94,.15) (3.16,-.17)--(3.16,.09); \draw[very thick](1.95,0)--(2.5,0);\fill(2.5,0)ellipse(.07 and .115);\end{tikzpicture}}
~~~


17–20, left repeated triangle.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=0.4em,row sep=small]
\&\& D_{012}\arrow[dl,dash]\arrow[d,very thick,dash]\arrow[dr,"\text{épi}",dash]\\
\&D_{01}\arrow[dl]\arrow[dr,"\text{épi}"']\&D_{02}\arrow[dll,dash]\arrow[drr,dash]\&D_{12}\arrow[dl,dash]\arrow[dr,"\text{épi}",dash]\\
 D_0\&\&D_1\&\&D_2
\end{tikzcd}}
~~~


17–21, right-hand criterion.

- `$D_\sigma\unsure{-|\to}D_{\sigma'}$`
- `$\sigma'\subset\sigma$`
- `$\sigma$`
- `$\sigma=\sigma''\cup\sigma'$`
- `$\sigma''<\sigma'$`

17, isolated mark above the lower diagram.

- `$\unsure{7|\urcorner}$`

19–24, large diagram.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=0.05em]
\&\&\&\&\&\&D_{0123}\arrow[dlll]\arrow[d]\arrow[dr,very thick]\\
\&\&\&D_{013}\arrow[ddll,bend right=20]\arrow[dr]\arrow[drr,very thick]\&\&\&D_{023}\arrow[dll,dashed]\arrow[dr,very thick]\&D_{123}\arrow[dll]\arrow[d,very thick]\\
\&\&D_{012}\arrow[dl,dashed]\arrow[d]\arrow[dr,very thick,"\text{épi}"]\arrow[dd,bend left=65]\arrow[rr,dash]\&\&D_{03}\arrow[ddr,very thick]\&D_{13}\arrow[dd,very thick]\&\&D_{23}\arrow[ddll,very thick]\\
\&D_{01}\arrow[dl]\arrow[d,very thick]\&D_{02}\arrow[dll,dashed]\arrow[d,very thick]\&D_{12}\arrow[dll,dashed]\arrow[dl,very thick,"\text{épi}"]\\
D_0\&D_1\&D_2\&\&\&D_3
\end{tikzcd}}
~~~


25–28, two columns at foot.


~~~latex
\[
\begin{aligned}
D_{01}&\mathbin{-}D_1 &D_{013}&\mathbin{-}D_{13}\\
D_{012}&\to D_{\unsure{12|+2}} &D_{0123}&\mathbin{-}D_{123}\\
D_{12}&\mathbin{-}D_2 &D_{123}&\mathbin{-}D_{23}\\
D_{02}&\mathbin{-}D_2 &D_{23}&\mathbin{-}D_3
\end{aligned}
\]
~~~


bottom right, ruled wedge with indices.


~~~latex
\figure{\begin{tikzpicture}[x=.95cm,y=.7cm]\draw (0,0)..controls (-.04,2) and (.9,2.8)..(2.21,2.8)--(5.7,2.8)--(.07,-.03); \draw (.34,1.7)--(1.83,2.52) (.17,1.14)--(2.72,2.52) (.12,.56)--(3.61,2.65) (.13,.05)--(4.47,2.65); \node at (3,3.12){$-D_3$}; \foreach \x/\v in {1.21/0,1.67/1,2.1/2,2.5/3}{\node at (\x,1.48){$\v$};} \node at (1.73,.93){$D_1$}; \node at (1.8,.48){$D_2$};\end{tikzpicture}}
~~~


bottom, numerical working.


~~~latex
\[
\begin{aligned}
&1\quad 1+1\quad 1+2+\\[-1pt]
&\hspace{3em}\shortparallel\\[-1pt]
 n_i&=\sum_{j<i}n_j+1\qquad 2
\end{aligned}
\]
~~~


**Corrections, marginal writing and cancellations**

- 1, opening — `\deleted{\unsure{f.}}`
- 7–8, scratched repetition to the left — `\deleted{\bar X_{i-1}}`, `\deleted{X_{i-1}\ X_i}`
- 14–16, left-hand scratch — `\deleted{D_{j\ldots j}}`

**Index and exponent register**

- 1, opening — `_i`
- 2–3, two lines of X terms — `_{i-1}`, `_{i-1}`, `_i`, `_i`
- 7–8, scratched repetition to the left — `_{i-1}`, `_{i-1}`, `_i`
- 8–10, right of the triangle — `_{01\ldots i}`
- 14–16, left-hand scratch — `_{j\ldots j}`
- bottom, numerical working — `_i`, `_{j<i}`, `_j`


## Scan 13

Started 2026-11-18T07:09:32Z. Ended 2026-11-18T07:10:21Z.

**Image notes recorded before reopening the transcription**

Numbers 1) 2) 3) 4), with a heavily barred third fork to the left, then the live forked R₁′ at right. ‘épi’, ‘décomposition cellulaire …’, ‘ordonné des drapeaux’, ‘type 0’, ‘type 1’, ‘type (0,1)’. Graph with open rings and filled vertices, several parallel arcs at right. F₀ repeated beside 4). Lower half Φ(C)=Catégorie des … familles finies, ‘de morphismes de C de mᵉ but’, ‘Un foncteur’, ‘implique un foncteur’, topological cone expression, ‘Si les … sont finis, de = les …’; ‘fidèle (resp. pl. fidèle)’, ‘mod isotopie’ underlined. Φ(Φ(C))→Top. Archive 12.

**Comparison with the transcription**

In the upper right the words l’ens and ordonné straddle the crossed line ‘complexe … sommets = F₀ … F₁’. Their connection was corrected. The left-hand attempt at 3) is cancelled and the version at its right is live. Each repeated fork has separate verticals, long oblique lines and primed upper entries. The lower fork has a small A-like stroke near F₂. Counted the ringed vertices and retraced the several arcs at the right of the drawing. In the cone formula the left indices of X and the coproduct are dotted i. Φ is broad with a cross-stroke; its resemblance to script P is marked at its first occurrence. The alteration over ‘familles finies’ is independent of the deletion above the arrow in Φ(C)→Top. Last ‘mod isotopie’ is underlined.

**Changes**

- `cellulaire \unsure{?} \deleted{drapeaux} \inserted{correspond : ? on}` -> `cellulaire \deleted{drapeaux} \inserted{correspond : l'ens}`
- `a \unsure{donc|demi} des drapeaux` -> `ordonné des drapeaux`
- `de $C$ de $=$ but` -> `de $C$ de \unsure{$=$|m\textsuperscript{e}} but`

**Formulas and diagram register**

1, upper left.

- `$F_0$`

2, first diagram.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\&R_1\arrow[dl]\arrow[dr,"\text{épi}"]\\
2)\ F_0\&\&F_1
\end{tikzcd}}
~~~


3, cancelled first attempt.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=tiny,row sep=tiny,execute at end picture={\draw[thick] (\tikzcdmatrixname-1-2.west) -- (\tikzcdmatrixname-2-1.west) -- (\tikzcdmatrixname-1-2.east) -- (\tikzcdmatrixname-3-1.east) -- (\tikzcdmatrixname-2-3.north) -- (\tikzcdmatrixname-3-3.west);}]
\&\deleted{R'_1}\arrow[dl]\arrow[dr,"\deleted{\text{épi}}"]\\
3)\ \deleted{F'_0}\arrow[d]\&\deleted{R_1}\arrow[dl]\arrow[dr,"\deleted{\text{épi}}"]\&\deleted{F'_1}\arrow[d]\\
F_0\&\&F_1\&F_2
\end{tikzcd}}
~~~


3, second drawing beside crossed version.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
\& R'_1\arrow[dl,very thick]\arrow[dr,two heads]\arrow[dd,very thick]\arrow[dddrr,dashed]\\
F'_0\arrow[dd,very thick]\arrow[ddrrr,dashed]\&\& F'_1\arrow[dd,very thick]\arrow[ddr]\\
\&R_1\arrow[dl]\arrow[dr,two heads]\\
F_0\&\&F_1\&F_2
\end{tikzcd}}
~~~


top right, decomposition and list.

- `$=F_0\amalg F_1$`

~~~latex
\[
\begin{aligned}
\text{type }0 &:F_0\\
\text{type }1 &:F_1\\
\text{type }(0,1)&:R_1
\end{aligned}
\]
~~~


top right, marked points and loops.


~~~latex
\figure{\begin{tikzpicture}[x=1.02cm,y=1.02cm]
\coordinate (a) at (.8,1.25); \coordinate (b) at (2.66,-.34); \coordinate (c) at (4.09,.62); \coordinate (d) at (5.04,1.94);
\draw (0,.57)--(a)--(.45,.6) (a)--(1.04,.6) (a) to[bend left=6](2.98,.59)--(b)--(2.15,.61) (b)--(c);
\draw (c)..controls (3.79,.96) and (3.89,1.32)..(4.18,1.61)--(d);
\draw (c)..controls (3.85,1) and (3.85,1.3)..(4.18,1.61);
\draw (c)..controls (4.21,.8) and (4.21,1.22)..(4.4,1.35)--(d);
\draw (c)..controls (4.36,.63) and (4.59,.83)..(4.7,1.02)--(d);
\foreach \p in {(0,.57),(.45,.6),(1.04,.6),(2.15,.61),(2.37,.19),(2.86,.27),(2.98,.59),(3.5,.19),(c),(4.18,1.61),(4.4,1.35),(4.7,1.02)}{\fill \p circle(.055);}
\foreach \p in {a,b,d}{\draw[thick](\p)circle(.14); \fill(\p)circle(.035);}
\end{tikzpicture}}
~~~


4, below left.

- `$F_0$`

4, below the isolated F.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
\& R'_1\arrow[dl,very thick]\arrow[dr,two heads]\arrow[dd,very thick]\arrow[dddrr,dashed]\\
F'_0\arrow[dd,dash]\arrow[ddrrr,dashed]\&\& F'_1\arrow[dd,very thick]\arrow[ddr]\\
\&R_1\arrow[dl]\arrow[dr,two heads]\\
F_0\&\&F_1\&\unsure{A}F_2
\end{tikzcd}}
~~~


lower left, initial categories.

- `$\deleted{C_0=\unsure{\mathrm{Ens}_f|\mathrm{Ens} f}}$`
- `$C_1={}$`

lower half, definition of family category.

- `$\unsure{\Phi|\mathscr P}(C)={}$`
- `$I,$`
- `$\{(f_i)_{i\in I}\}$`
- `$C$`
- `$=$`
- `$I$`

below definition, induced functor.

- `$C\xrightarrow{\unsure{r|\varphi}}(\mathrm{Top}\ \deleted{\unsure{isotop.}})$`

~~~latex
\[
 \begin{aligned}
 \Phi(C)&\xrightarrow{\deleted{\unsure{\varphi}}\Phi(r)}\mathrm{Top}\\
 (X_i\overset{\unsure{f_i}}{\to} X)_{i\in I}&\longmapsto
 \coprod_i\underbrace{\operatorname{cône}}_{\mathord{\hookrightarrow}}\deleted{\unsure{F}}r(X_i)
 \underset{\coprod\Phi(X_i)}{\amalg}r(X)
 \end{aligned}
\]
~~~


near bottom, finiteness.

- `$r(f)$`
- `$(f\in\mathrm{Fl}(C))$`
- `$=$`
- `$\Phi(r)(f)$`
- `$(f\in\mathrm{Fl}(\Phi(C)))$`

near bottom, faithfulness.

- `$r$`
- `$\Phi(r)$`

last line.


~~~latex
\[
 \Phi(\Phi(C))\longrightarrow\mathrm{Top}
\]
~~~


**Corrections, marginal writing and cancellations**

- 3, cancelled first attempt — `\deleted{R'_1}`, `\deleted{\text{épi}}`, `\deleted{F'_0}`, `\deleted{R_1}`, `\deleted{\text{épi}}`, `\deleted{F'_1}`
- top right, decomposition and list — `\deleted{drapeaux}`, `\inserted{correspond : l'ens}`, `\deleted{\unsure{complexe simplicial} sommets $=F_0\amalg F_1$}`
- lower left, initial categories — `\deleted{C_0=\unsure{\mathrm{Ens}_f|\mathrm{Ens} f}}`
- lower half, definition of family category — `\deleted{\unsure{couples|triples}}`, `\deleted{\unsure{$I,$}}`, `\inserted{familles finies}`, `\deleted{\unsure{$I$, ens. fin.}}`
- below definition, induced functor — `\deleted{\unsure{isotop.}}`, `\deleted{\unsure{\varphi}}`, `\deleted{\unsure{F}}`
- near bottom, faithfulness — `\deleted{\unsure{pl.}}`

**Index and exponent register**

- lower half, definition of family category — `_i`, `_{i\in I}`
- below definition, induced functor — `_i`, `_i`, `_{i\in I}`, `_i`, `_i`, `_i`


## Scan 14

Started 2026-11-18T07:10:22Z. Ended 2026-11-18T07:11:19Z.

**Image notes recorded before reopening the transcription**

Overwritten opening before ‘paratriangulation’ or plural; ‘paracartes’, ‘foncteurs’, upper right ‘segment final’, ‘paracartes nièquedimensionelles’/‘ni-équidemensionelles’, ‘tjrs épi’. ‘strates équidimensielles’, ‘Sup σ=Sup σ′’, ‘paracartes spéciales’, ‘birecellules’ cancelled/overwritten. Interlinear 0≤j≤i; lower j−1, j+1 and i. Heading ‘Question’, two question marks after degré 2, ‘p. ex D₁₂₃→D₁₃ degré 2…’. ‘d’où groupe Gᵢ₋₁ engendré …’, ‘récupérer’ underlined. At bottom ℛᵢ and Gᵢ₋₁ and a final open arrow or dash. Last third blank except pencil 13.

**Comparison with the transcription**

In σ′⊂σ the prime sits on the smaller set; in the next paragraph the unreversed σ⊂σ′ is retained. ‘Sup σ=Sup σ′’ is crossed out in the first block and live in the following one. The point/cross between the two j's in the open question is unclear. The left arrow before D(0,…,i) has a heavily filled head. In the small diagram both arrows from D₀₁₂ end at the lower entries, D₁₂ on the left and D₀₂ on the right. Subscripts i₀, i₁, iₚ at the foot were distinguished from j in the deletion formula. The curved opening stroke of Rᵢ leaves a script reading possible. Underlining under ‘de degré 2’, ‘Question’ and ‘récupère’ is independent of cancellations.

**Changes**

- `}(N)\xrightarrow` -> `}(\unsure{\mathbb N|N})\xrightarrow`
- `\text{précédentes : équidim}` -> `\text{\unsure{précédentes|bicellules} : équidim}`
- `Question} : t-on \unsure{\ldots}` -> `Question} : \unsure{a-t-on|t-on}`
- `opérant sur $R_i$` -> `opérant sur $\unsure{R|\mathscr R}_i$`
- `\unsure{verrait|veut}` -> `\unsure{veut|verrait}`

**Formulas and diagram register**

1–3, paratriangulations and paracartes.

- `$\unsure{\mathscr P_f^*|\mathscr P_f^\wedge}(\unsure{\mathbb N|N})\xrightarrow{D}(\mathrm{Ens})$`
- `$\sigma'\subset\sigma$`
- `$\Rightarrow D(\sigma)\to D(\sigma')$`

4–6, n-equidimensional case.

- `$n$`
- `$\big\{D(\sigma)\mathbin{-}D(\sigma')$`
- `$\operatorname{Sup}\sigma=\operatorname{Sup}\sigma'$`
- `$\sigma\subset\sigma'\subset\Delta_n$`
- `$D(\{i\})=0$`
- `$i>n$`

7–9, strata.

- `$D(\unsure{\Delta_i|\Delta_n})\mathbin{-}D(\sigma')$`
- `$\operatorname{Sup}\sigma=\operatorname{Sup}\sigma'$`
- `$D([0,i])\to D(\sigma)$`
- `$i=\operatorname{Sup}\sigma$`

10–13, special paracartes.

- `$\left\{\begin{aligned} &\text{\unsure{précédentes|bicellules} : équidim}\\ &\forall\ \deleted{i\ \text{\unsure{tel que}}\ D(\{i\})\ne\varnothing,\ \text{\unsure{le}}}\ \inserted{0\leq j\leq i}\\ &D(0,\ldots,j-1,j+1,\ldots i)\longleftarrow D(0,\ldots,i)\\ &\hspace{5em}\text{\uline{de degré 2}} \end{aligned}\right.$`

11–13, small examples at left.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=tiny]
D_{01}\arrow[d]\&\&D_{012}\arrow[dl]\arrow[dr]\\
D_1\&D_{12}\&\&D_{02}
\end{tikzcd}}
~~~


14–16, question.

- `$D(\ldots j-1,j\unsure{+|,}j+1\ldots)\mathbin{-}D(\deleted{\unsure{j\ldots}}j-1,j+1,\ldots)$`
- `$D_{123}\to D_{13}$`

17–20, groups and reconstruction.

- `$G_{i-1}$`
- `$\sigma_0\ldots\sigma_{i-1}$`
- `$\unsure{R|\mathscr R}_i$`

~~~latex
\[
 \underset{\unsure{\shortparallel}}{R_i}\qquad D(0,\ldots,i)
\]
~~~

- `$D(i_0,i_1\ldots i_p)$`
- `$g$`
- `$(R_i,G_{i-1})$`
- `$R_{i+1}\mathbin{-}R_i\mathbin{-}\ldots$`

**Corrections, marginal writing and cancellations**

- 1–3, paratriangulations and paracartes — `\deleted{\unsure{espaces}}`, `\inserted{segment final}`
- 4–6, n-equidimensional case — `\deleted{$\operatorname{Sup}\sigma=\operatorname{Sup}\sigma'$}`
- 7–9, strata — `\deleted{\unsure{filtra}}`
- 10–13, special paracartes — `\deleted{i\ \text{\unsure{tel que}}\ D(\{i\})\ne\varnothing,\ \text{\unsure{le}}}`, `\inserted{0\leq j\leq i}`
- 14–16, question — `\deleted{\unsure{j\ldots}}`
- 17–20, groups and reconstruction — `\deleted{\unsure{g}}`, `\deleted{\unsure{$g$}}`

**Index and exponent register**

- 7–9, strata — `_i`
- 17–20, groups and reconstruction — `_{i-1}`, `_{i-1}`, `_i`, `_i`, `_i`, `_{i-1}`, `_{i+1}`, `_i`


## Scan 16

Started 2026-11-18T07:11:19Z. Ended 2026-11-18T07:12:20Z.

**Image notes recorded before reopening the transcription**

‘Un ens ordonné D est appelé “géométrie de drapeaux”’, ‘dessous’ with addition ‘initial’?, ‘simplexe ordonné’, ‘parties finies ≠∅’, NB en/de sorte I_d≠∅ in left edge writing. I_d can be identified with minimal elements of D(d), ‘longueur’ of the drapeau. [D_*] ≃ coproduct, ‘contrafoncteur’, ‘connaissance’, ‘évidente. Ainsi’. Caption in left margin ‘Φ est tjrs l’ens des sommets d’un ens … simplicial, mais … n’est pas déterminé par celui-ci…’. ‘géom de drapeaux stricte’, supremum over i∈I_d; lower ‘parties finies ponctuelles’, ‘ens ≠∅ plus petits’, ‘craquelettes’ or ‘…quelettes simpliciales’. ‘D est … le … foncteur … final i.e.’. Last ends card D(σ)∈{0,1}.

**Comparison with the transcription**

In D(d) the primes are on each d′ in the defining set, never on the terminal d. The small upward link after I_d is separate from the letter. The upper-right note explains the starred parts, and the far-left NB adds nonemptiness. In the middle equivalence the rightmost singleton-cardinality digit has a strong crossing; the earlier 1 does not. The later quantified index looks like I although the functor above is on Φ. In the side note the word maquette recurs in the strict equivalence after the supremum. In the final line the additions above and below foncteur overlap earlier struck text. Retained the equality sign in the definition of Φ as doubtful. The raised o on the functor domain is smaller than a zero. There is no indexed j; i in the supremum is dotted.

**Changes**

- `avec $\subset$ relation` -> `avec \unsure{la|$\subset$} relation`
- `\inserted{\unsure{isom. à un}} foncteur` -> `\inserted{\unsure{sous|isom. à un}} foncteur`
- `(ens. ordonné abs.)` -> `(ens. ordonné \unsure{abs.|avec})`
- `\operatorname{Card}D(\sigma)` -> `\operatorname{card}D(\sigma)`

**Formulas and diagram register**

1–3, definition.

- `$D$`
- `$d\in D$`
- `$D(d)=\{d'\in D\mid d'\leq d\}$`
- `$\unsure{\mathscr P^*|\mathcal P^*}(I_d)$`

2–3, upper right, directed to the power set.

- `$\ne\varnothing$`

3–4, outer left.

- `$I_d\ne\varnothing$`

4–8, minimal elements and length.

- `$I_d$`
- `$D(d)$`
- `$\Phi\unsure{=|.}D(\underline{1})$`
- `$D$`
- `$\operatorname{card}(I_d)$`
- `$d$`

8–11, antifacteur.

- `$\sigma$`
- `$\Phi$`
- `$D(\sigma)$`
- `$d\in D$`
- `$\deleted{\unsure{\sigma\subset}}I_d\deleted{\unsure{\ni}}=\sigma$`

~~~latex
\[
 (\text{parties finies \inserted{$\ne\varnothing$} de }\Phi)^o\xrightarrow{D}(\mathrm{Ens})\qquad
 \text{tel que }\operatorname{card}D(\{i\})=1\quad\forall i\in\Phi
\]
~~~


12–14, reconstruction.

- `$D_{\unsure{*}}$`

~~~latex
\[
 D_{\unsure{*}}\simeq\coprod_{\sigma\in\mathscr P_f^*(\Phi)}D(\sigma)
\]
~~~

- `$\subset$`

15–18, equivalence.


~~~latex
\[
\begin{aligned}
\left\{\begin{array}{l}\text{géométrie de drapeaux}\\\text{(ens. ordonné \unsure{abs.|avec})}\end{array}\right.
 &\Longleftrightarrow \begin{array}{l}
 \text{Couple }(\Phi,D)\text{ d'un ens}\\
 \Phi\text{ et d'un foncteur}\\
 \underline{\mathscr P_f^*}(\Phi)^o\mathbin{-}(\mathrm{Ens})\\
 \text{tel que }\operatorname{card}D(\{i\})=\unsure{4|1}\quad\forall i\in\unsure{I|\Phi}
 \end{array}
\end{aligned}
\]
~~~


17–19, lower left of equivalence.

- `$\Phi$`
- `$D$`

19–20, strictness.

- `$D$`
- `$\forall d\in D$`

~~~latex
\[
 d=\mathop{\rm Sup}_{i\in I_d}i
\]
~~~


21–24, subsets.

- `$D$`
- `$\ne\varnothing$`
- `$\Phi$`
- `$\ne\varnothing$`

25, correspondence.


~~~latex
\[
 \left(\begin{array}{c}\text{géom. de drapeaux}\\\text{stricte}\end{array}\right)
 \Longleftrightarrow
 \left(\begin{array}{c}\text{maquettes}\\\text{simpliciales}\end{array}\right)
\]
~~~


26–28, functor formulation.

- `$D:\mathscr P_f^{\unsure{\triangle|*}}(\Phi)^o\mathbin{-}(\mathrm{Ens})$`
- `$D$`
- `$\sigma$`
- `$\forall\sigma,$`
- `$\operatorname{card}D(\sigma)\leq1$`
- `$\operatorname{card}D(\sigma)\in\{0,1\}$`

**Corrections, marginal writing and cancellations**

- 1–3, definition — `\inserted{$D$}`, `\deleted{\unsure{dessous|dessiné}}`, `\inserted{\unsure{induit|initial}}`
- 2–3, upper right, directed to the power set — `\margin{parties finies $\ne\varnothing$}`
- 3–4, outer left — `\margin{\uline{NB} on aura donc $I_d\ne\varnothing$}`
- 8–11, antifacteur — `\deleted{\unsure{\sigma\subset}}`, `\deleted{\unsure{\ni}}`, `\inserted{$\ne\varnothing$}`
- 17–19, lower left of equivalence — `\margin{\uline{NB} $\Phi$ est tjrs l'ens des sommets d'une maquette simpliciale, mais bien sûr $D$ n'est pas déterminé par celle-ci\ldots}`
- 19–20, right of supremum formula — `\margin{géom de drapeaux stricte}`
- 21–24, subsets — `\inserted{$\ne\varnothing$}`
- 26–28, functor formulation — `\deleted{le}`, `\inserted{\unsure{sous|isom. à un}}`, `\deleted{\unsure{prenant}}`, `\inserted{du foncteur}`, `\inserted{final i.e.}`, `\deleted{qui \unsure{en chaque} $\sigma$, \unsure{a pour}}`

**Index and exponent register**

- 19–20, strictness — `_{i\in I_d}`


## Scan 17

Started 2026-11-18T07:12:21Z. Ended 2026-11-18T07:13:08Z.

**Image notes recorded before reopening the transcription**

‘Soit I un ens et’ attached before Supposons; ‘sans condition de la forme’, singleton D unprimed before the equality, ‘néanmoins’, lifted cancellation after drapeaux. ‘On a donc une application’, ‘dim’ in double quotes, ‘injective’, ‘Inversement, étant donné une géom de drapeaux’, ‘de de Φ=D(1)’. First functor has raised o; next one lacks an o. In final coproduct lower condition ‘t.q. δ|σ′ : σ′ … σ’; superscript at P either wedge or star with a long f; ‘Bref’ after restored pair. 16 at bottom left.

**Comparison with the transcription**

The underlined P at the top has a wedge-like high mark; the one at the bottom has a short cross-like stroke. The top arrow is labelled D′. Singleton D is unprimed in the stated condition but primed at the bottom of the next two coproducts. The earlier lower index in the second coproduct is struck, with i∈I immediately beneath it. The repeated trial restriction is crossed before the separate live display. D(1) at the start of the converse has no visible underlining under 1. On the bottom line in the coproduct the tilde over a short bar has no clear arrowhead; the domain visibly resembles I. The sole uncertain punctuation after I_d remains in the transcription. There are no sideways margin notes or typed forms.

**Changes**

- `\sigma'\overset{\sim}{\longrightarrow}\sigma` -> `\sigma'\unsure{\simeq|\overset{\sim}{\to}}\sigma`
- `$(I,D')$. Donc` -> `$(I,D')$. \unsure{Donc|Bref}`

**Formulas and diagram register**

1–3, opening and functor.

- `$I$`

~~~latex
\[
 \underline{\unsure{\mathscr P_f^\wedge|\mathscr P_f^*}}(I)^o\xrightarrow{D'}(\mathrm{Ens})
\]
~~~


4–7, flag geometry.

- `$\operatorname{card}D(\{i\})=1$`
- `$\unsure{\forall i\in I|\text{lorsque}}\unsure{)}$`

~~~latex
\[
 D=\coprod_{\sigma\in\mathscr P_f^*(I)}D'(\sigma)
\]
~~~


8–11, minimal elements and map.


~~~latex
\[
 \Phi=\coprod_{\substack{\deleted{\unsure{\sigma\in\mathscr P_f^*}}\\\inserted{i\in I}}}D'(\{i\})
\]
~~~


~~~latex
\[
 \Phi\xrightarrow{\delta}I
\]
~~~


12–16, restriction.

- `$\delta$`
- `$d\in D$`
- `$\delta|I_d:\unsure{d\ldots}$`

~~~latex
\[
 \delta\mid I_d\unsure{.}\ :\ I_d\longrightarrow I
\]
~~~


16–20, converse.

- `$D$`
- `$\delta$`
- `$\Phi=D(1)$`
- `$D$`
- `$I$`

21–23, associated functor.


~~~latex
\[
\begin{aligned}
 &D':\underline{\mathscr P_f^{\unsure{+|*}}}(I)\to(\mathrm{Ens})\qquad\text{par}\\
 &D'(\sigma)=\coprod_{\substack{\sigma'\in\mathscr P_f^*(\unsure{I|\Phi})\\\text{t.q. }\delta|\sigma':\sigma'\unsure{\simeq|\overset{\sim}{\to}}\sigma}}D(\sigma')
\end{aligned}
\]
~~~


24–25, recovery.

- `$(D,I,\delta)$`
- `$(I,D')$`

**Corrections, marginal writing and cancellations**

- 1–3, opening and functor — `\inserted{Soit $I$ un ens et}`
- 4–7, flag geometry — `\deleted{dont l'ens des}`
- 8–11, minimal elements and map — `\deleted{\unsure{\sigma\in\mathscr P_f^*}}`, `\inserted{i\in I}`
- 12–16, restriction — `\deleted{\unsure{$\delta$}}`, `\deleted{$\delta|I_d:\unsure{d\ldots}$}`

**Index and exponent register**



## Scan 18

Started 2026-11-18T07:13:09Z. Ended 2026-11-18T07:14:11Z.

**Image notes recorded before reopening the transcription**

‘géom. de drapeaux’, ‘fonction dimension’, ‘él. min.’, equivalence barred both sides. ‘Posant I₀’, ‘géométr. simpl.’, ‘ayant comme simplexes’, ‘NB I₀=δ(Φ)’. ‘plus particulièrement’, ‘s’appelle’, ‘Si celle-ci est finie’, ‘souvent avantage’. ‘Plus gén.’, ‘pour une géom de drapeaux D donnée’, ‘simplexe’, ‘ordre total’, ‘mutuellement’; ‘totᵗ ordonné’, ‘pré’ written twice over ordre. ‘image inverse...’, ‘Alors, posant pour n∈ℕ (n≥0)’. D[n] with I_d of size n+1 and an alternative formula ‘ou …’ above/below equals sign; Φ in first lower index and I in second. Pencil 17.

**Comparison with the transcription**

The small mark beneath Φ points down to ‘él. min.’. Two rules delimit the equivalence. The right-hand NB includes both I₀ and the inserted identity I₀=δ(Φ); the note is read left to right across a join. The dimension line visibly reads δ(I) after the barred R subscript, even though the domain of δ in the head diagram is Φ. The word before simplexe is cancelled and pré is raised twice. There is a dot after the i in I_d's index only when it is a separate i elsewhere; the subscript in I_d itself is d. The crossed/trailing f-like mark on the part-symbol at the foot appears before n+1 in both copies. In the parenthetical equality the shortened word after ou begins with an apparent s and apostrophe. No typed correction.

**Changes**

- `\substack{\uparrow\\\text{él. min.}}` -> `\substack{\downarrow\\\text{él. min.}}`
- `\unsure{m. géométr. simpl.}` -> `\unsure{maquette simpl.|m. géométr. simpl.}`
- `\text{ou seulement}` -> `\text{ou \unsure{s'ident.|seulement}}`
- `\mathscr P_{n+1}(\Phi)` -> `\mathscr P_{\unsure{f\,n+1|n+1}}(\Phi)`
- `\mathscr P_{n+1}(I)` -> `\mathscr P_{f\,n+1}(I)`

**Formulas and diagram register**

1–4, equivalence at head.


~~~latex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
\left.\begin{gathered}
 \text{géom. de drapeaux } D\\[-2pt]
 {}+\text{ ``\deleted{\unsure{application}}\inserted{fonction} dimension''}\\
 \delta:\underset{\substack{\downarrow\\\text{él. min.}}}{\Phi}\longrightarrow I
\end{gathered}\right| \arrow[r,Leftrightarrow] \&
\left|\ \text{foncteur }D'/\underline{\unsure{\mathscr P_f^*|\mathcal P_f^*}}(I)^o\to(\mathrm{Ens})\right.
\end{tikzcd}}
~~~


3–6, below right-hand member and across middle.

- `$I_0=\{i\in I\mid D'(\{i\})\ne\varnothing\}$`
- `$I_0$`
- `$\sigma$`
- `$D'(\sigma)\ne\varnothing$`
- `$I_0=\delta(\Phi)$`

7–9, case of the natural numbers.


~~~latex
\[
 I=\mathbb N
\]
~~~


10–14, dimension.

- `$\delta$`
- `$\Phi/I$`
- `$\sup_{\overline{\mathbb R}}\delta(I)$`
- `$D$`
- `$n$`
- `$\mathbb N$`
- `$[0,n]_{\mathbb N}$`

15–20, general construction.

- `$D$`
- `$\sigma\subset\underline{\Phi}$`
- `$\sigma\in\mathscr P_f^*(\Phi)$`
- `$I_d$`
- `$\sigma$`

20–27, orders and preorders.

- `$\delta:\underline{\Phi}\to I$`
- `$I$`
- `$I$`
- `$I$`
- `$n\in\mathbb N$`
- `$n\geq0$`

28–30, D[n].


~~~latex
\[
 \begin{aligned}
 D[n]&=\{d\in D\mid\operatorname{card}I_d=n+1\}\\
 &=\coprod_{\sigma\in\mathscr P_{\unsure{f\,n+1|n+1}}(\Phi)}D(\sigma)\\
 &\left(\underset{\text{ou \unsure{s'ident.|seulement}}}{=}\
 \coprod_{\sigma\in\mathscr P_{f\,n+1}(I)}D'(\sigma)\right)
 \end{aligned}
\]
~~~


**Corrections, marginal writing and cancellations**

- 1–4, equivalence at head — `\deleted{\unsure{application}}`, `\inserted{fonction}`
- 3–6, below right-hand member and across middle — `\margin{\uline{NB} Posant $I_0=\{i\in I\mid D'(\{i\})\ne\varnothing\}$ on a sur $I_0$ une structure de \unsure{maquette simpl.|m. géométr. simpl.}, ayant comme simplexes les $\sigma$ tels que $D'(\sigma)\ne\varnothing$. \inserted{(NB $I_0=\delta(\Phi)$).}}`, `\inserted{(NB $I_0=\delta(\Phi)$).}`
- 10–14, dimension — `\deleted{\unsure{$\Phi/I$}}`, `\deleted{\unsure{prend le nom}}`, `\inserted{s'appelle}`, `\deleted{\unsure{avec sa dimension}}`, `\inserted{(munie de sa}`
- 15–20, general construction — `\inserted{(pour une géom. de drapeaux $D$ donnée)}`, `\deleted{\unsure{partie}}`
- 20–27, orders and preorders — `\inserted{pré}`, `\deleted{\unsure{induisant}}`, `\inserted{pré}`

**Index and exponent register**



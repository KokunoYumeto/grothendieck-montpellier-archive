# Second reading

The location numbers below are lines in each individual page fragment at the freeze. The image observations were recorded before reopening that fragment. The mathematical ledger includes the array cells and the labels inside the drawings.

The recorded second readings ranged from 1 minute 4 seconds to 6 minutes 47 seconds per sheet. The separate cross-page comparison recorded at the end also took place before the freeze.

## Scan 104

Second reading, UTC: 2026-11-18T09:11:19Z to 2026-11-18T09:12:41Z.

### Before reopening the transcription

“tels que l'on ait” is the only extended phrase. Low horizontal ink between l and ait is very thin. No accents over these words. No prose belongs to the little mark above the triples unless the crossing obscures it. At the upper left the initial parenthetic capital is open, with a short horizontal stroke; the upper and lower terminals may be G/C. The centre-left last tuple has r′, not r alone. At the foot a raised barred a and a tiny low 0 sit over the first alpha column. The implied relation after the upper-right divider has two separate right-facing points. The first circle and long returning curve meet beside ρ.

### Ink, corrections, lettering and margins

The short head at the end of the long right connector points down beside “ait”; its other extremity has a free tail under the table. Upper enclosures and the connected underline have been redrawn. There is no alphabetic i/j index. The tiny marks beneath alpha/beta/gamma are 1–4. Distinguished the undulating tildes from flat bars by comparing the three aligned lists. The downward r′/r″ entry has too little ink for its number of primes to be secure. The near-vertical stroke from the P row and the six column separators do not strike words. Crosses remain over upper-left possible bracketings, two triples, the beginning of the corrected triple, two signs in the grouped six-column display, the list end and the two existential trials. The entire page is handwritten; the archive 105 is in the corner.

### Changes

```text
\tau{}|ι -> \tau{}|\iota
```

```text
\boxed{\vphantom{\big|}(\overline{\pi{}},\widetilde{r''},\rho{})} -> \tikz[baseline=(v.base)]{\node[inner sep=2pt](v){$(\overline{\pi{}},\widetilde{r''},\rho{})$};\draw (v.center) ellipse[x radius=2.8em,y radius=1.2em];\draw[overlay] (v.east)..controls +(0,-1.5em) and +(-1em,-1.2em)..++(13em,.15em);}
```

```text
% The enclosure of the third-row middle triple is oval. A long curved stroke runs from it below the rightmost equivalence. -> % The tail joins the oval to the right extremity of this line.
```

```text
\& (r'') \& (r') -> \& (\unsure{r'|r''}) \& (r')
```

```text
\pi{}&r'&r'&\sigma{}&\underline{\pi{}} -> \pi{}&r'&\multicolumn{2}{c|}{\underline{r'\hspace{1.2em}\sigma{}}}&\underline{\pi{}}
```

```text
\arrow[dddd,bend left=45,leftrightarrow] -> \arrow[dddd,bend left=45]
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

```text
multiline gathered nodes -> braced multiline gathered nodes (matrix syntax)
```

### Formula ledger

L3

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=1ex,column sep=1em]
 \& \unsure{G|C} \&\\
 \& \deleted{\unsure{g}}\Psi(C)\arrow[u]\arrow[dl]\arrow[dr] \&\\
 G \& \& G
\end{tikzcd}}
```

L9

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=1em,row sep=.5em]
 \& P\quad a_0\;\overline{r},\overline{\pi},\overline{r'} \&\\
 \& {\underset{\gamma_0}{\Gamma}}\arrow[u]\arrow[dl]\arrow[dr] \&\\
 {\underset{c_0}{R}} \& \& {Q\quad b_0\;\widetilde{r'}\;\widetilde{r''}\;\widetilde{\sigma}}
 \arrow[from=1-2,to=3-3,dash,end anchor=north,start anchor=east]
\end{tikzcd}}
```

L16

```tex
\[
\left.
\begin{gathered}
 \deleted{\unsure{\rho}}\\
 \deleted{\unsure{r,r',r''}}\\[-2pt]
 \deleted{\unsure{\pi\;\sigma}}\\
 \deleted{(rr')r''}
\end{gathered}\right\}
\begin{gathered}
 \overbrace{\overbrace{r,r'}^{\pi},r''}^{\rho}\\[-2pt]
 \underbrace{\phantom{r,}r',r''}_{\sigma}\\[-2pt]
 \underbrace{\phantom{r,r',r''}}_{\unsure{\tau|\iota}}
\end{gathered}
\qquad
\deleted{r(r'r'')}
\]
```

L32

```tex
\[
\begin{array}{ccc|l}
\deleted{\unsure{a_0,b_0}}&&&\\
\deleted{(\overline{r},b_0,r)}&(\overline{\pi},b_0,\pi)&(\overline{r'},b_0,r')&\\
(a_0,\widetilde{r'},r')&\deleted{(a_0,\widetilde{r''},r'')}&\deleted{\unsure{a_0,r''}}\inserted{(a_0},\widetilde{\sigma},\sigma)&\Rightarrow\\
(\overline{r},\widetilde{r'},\pi)&\tikz[baseline=(v.base)]{\node[inner sep=2pt](v){$(\overline{\pi},\widetilde{r''},\rho)$};\draw (v.center) ellipse[x radius=2.8em,y radius=1.2em];\draw[overlay] (v.east)..controls +(0,-1.5em) and +(-1em,-1.2em)..++(13em,.15em);}&(\overline{r'},\widetilde{r''},\sigma)&(\overline{r},\widetilde{\sigma},\rho)\Leftrightarrow
\end{array}
\]
```

L41

```tex
\[
\begin{aligned}
&a_0,\overline{r'},\overline{r},\overline{\pi}\\
&b_0,\widetilde{r'},\widetilde{r''},\widetilde{\sigma}\\[3pt]
&r,r',r'',\pi,\sigma,\rho
\end{aligned}
\]
```

L48

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.65em,column sep=.6em]
 \overline{r}\arrow[d] \& \widetilde{r'}\arrow[d] \& \overline{\pi}\arrow[ddll,bend left=15]
 \& \widetilde{r''}\arrow[d] \& \overline{r'}\arrow[d] \& \widetilde{\sigma}\arrow[ddll,bend left=22]\\
 (r) \& (r')\arrow[rrr,leftrightarrow,yshift=1.2ex] \& \& (\unsure{r'|r''}) \& (r') \&\\
 \pi \& \rho \& \& \sigma \& \&
\end{tikzcd}}
```

L54

```tex
\[
\begin{array}{ll}
\alpha_1=a_0 & \alpha_2=\overline{r}\\
\beta_2=\widetilde{r'} & \beta_1=\widetilde{\sigma}\\
\gamma_2=r' & \gamma_1=\sigma
\end{array}
\]
```

L61

```tex
\[
\begin{aligned}
&\underline{a_0},\underline{\overline{r}},\underline{\overline{\pi}},\underline{\overline{r'}}\\
&\underline{b_0},\underline{\widetilde{r'}}\;\widetilde{r''}\;\deleted{\unsure{b}}\widetilde{\sigma}\\
&\underline{r'},\underline{\pi},\underline{\sigma},\underline{\rho}
\end{aligned}
\]
```

L68

```tex
\diagram{\(\displaystyle
\left\{\begin{array}{c|c|c|c|c|c}
 \overline{\pi}&\overline{r'}&a_0&a_0&\overline{r}&\overline{r'}\\
 b_0&b_0&\widetilde{r'}&\widetilde{\sigma}&\widetilde{r'}&\widetilde{r''}\\
 \pi&r'&\multicolumn{2}{c|}{\underline{r'\hspace{1.2em}\sigma}}&\underline{\pi}&\sigma
\end{array}\right\}
\deleted{\unsure{\ne}}\;
\left\{\left(\begin{array}{c}\overline{\pi}\\\widetilde{r''}\\\rho\end{array}\right)
\deleted{\unsure{\Rightarrow}}\;\left(\begin{array}{c}\overline{r}\\\widetilde{\sigma}\\\underline{\rho}\end{array}\right)\right\}
\)}
```

L79

```tex
\[
 a_0,b_0,\overline{r},\underset{\deleted{\unsure{r''}}}{\widetilde{r''}},\overline{r'},\deleted{\unsure{\widetilde{r'}}}
 \ \bigg|\ \overset{\widetilde{r'},r'}{\overbrace{\pi,\sigma}},\rho,\overline{\pi},\widetilde{\sigma}
\]
```

L83

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.25em,row sep=.5em]
 \& \& \& \& \& \phantom{\rho}\arrow[dddd,bend left=45]\\[-1.2em]
 {\forall\ \begin{gathered} a_0,\overline{r},\overline{r'}\in P\\ b_0,\widetilde{r''}\in Q\end{gathered}}
 \& \exists \& {\begin{gathered}\deleted{\unsure{r',\overline{\pi}\in Q}}\\\deleted{\unsure{r',\pi,\sigma,\rho}}\end{gathered}}
 \& {\begin{gathered}\overline{\pi}\in P\\ \widetilde{r'},\widetilde{\sigma}\in Q\\r',\pi,\sigma,\rho\in R\end{gathered}}
 \& \text{tels que l'on ait} \&\\
 \&\&\&\&\&\\ \&\&\&\&\&\\ \&\&\&\&\&\phantom{\rho}
\end{tikzcd}}
```

L91

```tex
\diagram{\(\displaystyle
\begin{array}{cccc}
 \unsure{\overline{a_{0}}}&&&\\[-4pt]\Vert&&&\\
 \alpha_1&\alpha_2&\alpha_3&\alpha_4\\
 \beta_1&\beta_2&\beta_3&\beta_4\\
 \gamma_1&\gamma_2&\gamma_3&\gamma_4
\end{array}\qquad
\begin{array}{cccccccc}
 \alpha_1&\alpha_1&\alpha_2&\alpha_2&\alpha_3&\alpha_3&\alpha_4&\alpha_4\\
 \beta_1&\beta_2&\beta_1&\beta_2&&&&\\
 \gamma_1&\gamma_2&\gamma_3&\gamma_4&&&&
\end{array}
\)}
```

### Indices and exponents containing i or j

No alphabetic i or j appears in a subscript or superscript in the adopted reading.

## Scan 106

Second reading, UTC: 2026-11-18T09:12:41Z to 2026-11-18T09:14:48Z.

### Before reopening the transcription

“dim”, “racines” (very weak medial letters), “56 indéterminé…” terminal stroke very short, accent at right; “permutations paires de [1,7]” with the intervening letters reduced. In the heading the capital has three horizontal strokes. The first pair of index constraints is 1≤i≤7 then 1≤i<h≤7. Under the first sum a j actually extends below the line. The differential at the far right lies against the page boundary. In the left margin the looped digit or G is separate from the bare 12 immediately below. Lower two-thirds have no continuation of the quartic.

### Ink, corrections, lettering and margins

There is a looped ascender on the last summation index, overwritten or retraced on the right; both h and k remain possible. The factor following y_j starts with an a-like loop, unlike the conspicuous cross in x near the next sum. The plus before the last sum has three strokes meeting at the centre. Compared x_ih, y_ih, x_hi and y_hi in the table, then x_i, y_j, the two paired h subscripts in the quartic and both i,h subscripts of each differential. In the permutation list the long downward strokes belong to Greek rho and not j. The parenthetic 126 has a clear final 6. The script initial at End has a loop up and down its stem, unlike the E of E₇. One small superfluous summation sign is crossed, whereas the long line below the differential and the line below the product are underlines. The left “8/g” and 12 are upright; there is no text in the bottom third apart from archival 107.

### Changes

```text
indéterminés|indéterminées -> indéterminé|indéterminés|indéterminées
```

```text
\sum_{i,j,h=1} -> \sum_{i,j,\unsure{k|h}=1}
```

```text
+\sum\bigl -> \unsure{+|\ast}\sum\bigl
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\[
 \dim E_7=133\quad(126\ \text{\unsure{racines}})
\]
```

L5

```tex
\[
\left.\begin{array}{llll}
 x_i\quad y_{\unsure{i}} &1\le i\le7&14&\\
 x_{ih}&1\le i<h\le7&21&x_{ih}=-x_{hi}\\
 y_{ih}&1\le i<h\le7&21&y_{ih}=-y_{hi}
\end{array}\right\}\quad56\ \text{\unsure{indéterminé|indéterminés|indéterminées}}
\]
```

L12

```tex
\[
\begin{aligned}
 &\sum_{i,j,\unsure{k|h}=1}^{7}\deleted{\sum}x_i y_j\unsure{a_{ih}|x_{ih}}y_{jh}
 +\tfrac14\sum_{\lambda,\mu,\nu,\rho=1}^{7}x_{\lambda\mu}x_{\nu\rho}y_{\mu\nu}y_{\lambda\rho}
 \unsure{+|\ast}\sum\bigl(\underline{x_i y_{\lambda\mu}y_{\nu\rho}y_{\sigma\tau}}\\[-2pt]
 &\hspace{22em}{}+y_i x_{\lambda\mu}x_{\nu\rho}x_{\sigma\tau}\bigr)
\end{aligned}
\]
```

L20

```tex
\[
 \left\{\begin{gathered}
 i,\lambda,\mu,\nu,\rho,\sigma,\tau\quad\text{permutations}\\
 \text{paires de }[1,7]
 \end{gathered}\right.
\]
```

L26

```tex
\[
\unsure{\mathscr L|\mathcal L}\quad\text{---}\quad \operatorname{End} V_{56}
\qquad
\underline{\sum(x_i\,dy_i-y_i\,dx_i)+
 \sum_{i,h=1}^{7}(x_{ih}\,dy_{ih}-y_{ih}\,dx_{ih})}
\]
```

L32

```tex
\[
\begin{aligned}
 &\unsure{8|g}\quad\text{---}\\
 &12
\end{aligned}
\]
```

### Indices and exponents containing i or j

- L7: `x_i`, `x_i\quad y_{\unsure{i}}`.

- L8: `x_{ih}`, `i<h\le7&21&x_{ih}`, `&21&x_{ih}=-x_{hi}`.

- L9: `y_{ih}`, `i<h\le7&21&y_{ih}`, `&21&y_{ih}=-y_{hi}`.

- L14: `&\sum_{i,j,\unsure{k\|h}=1}`, `eleted{\sum}x_i`, `ed{\sum}x_i y_j`, `y_j\unsure{a_{ih}`, `sure{a_{ih}\|x_{ih}`, `{ih}\|x_{ih}}y_{jh}`.

- L16: `(\underline{x_i`.

- L17: `ace{22em}{}+y_i`.

- L29: `erline{\sum(x_i`, `{\sum(x_i\,dy_i`, `m(x_i\,dy_i-y_i`, `,dy_i-y_i\,dx_i`.

- L30: `\sum_{i,h=1}`, `{i,h=1}^{7}(x_{ih}`, `7}(x_{ih}\,dy_{ih}`, `h}\,dy_{ih}-y_{ih}`, `h}-y_{ih}\,dx_{ih}`.

## Scan 108

Second reading, UTC: 2026-11-18T09:14:49Z to 2026-11-18T09:16:51Z.

### Before reopening the transcription

Top “groupe comm.” and “appl. somme”. “correspondant à une trivialisation” has a visible accent on à and a very faint middle in the long noun. “catég. des systèmes”, “trivialisation t de leur produit de torseurs”, “vers les quadruplets”, “est pl. fidèle.” The tail of “symétrie” is faint on the lower right. After “Se donner” a first conjunction has been crossed. “Les pᵢⱼ sont des iso” has two separate underlines. The first abbreviation at the lower left of the final displays looks like “et de =”, the last doubled stroke standing for même. There is a ker beside s (open capital K).

### Ink, corrections, lettering and margins

Two raised inserts, G and P_i, belong after “gpe” and “tors.” respectively. The properly dotted i of each p_i is short; the j of p_ij and P_ij has a low leftward tail. In “Notons” the shafts have at most a terminal dot, in contrast to the definite triangular head below π₃. The last horizontal φ₁₃₂ stroke ends squarely. Condition (1) is underlined on both sides of p_ij. The crooked line beside the deleted tail after P₃ covers an earlier continuation. No cross through the brace or through the lower pair of variable assignments. The text at the right of the final Isom is upright and ends “par symétrie”. Read the open G in G-torseurs against the distinctly angular Γ in the membership display. Baer starts with a two-part capital; its last letters run together.

### Changes

```text
allant des systèmes -> \unsure{allant} des systèmes
```

```text
produit de Baer -> produit de \unsure{Baer}
```

```text
\unsure{plt|ple} fidèle -> \unsure{pl.|plt} fidèle
```

```text
p_i:\Gamma{}\longrightarrow P_i,\quad p_{ij}:\Gamma{}\longrightarrow P_{ij} -> p_i:\Gamma{}\unsure{\relbar\joinrel\relbar|\longrightarrow} P_i,\quad p_{ij}:\Gamma{}\relbar\joinrel\relbar P_{ij}
```

```text
P_1\xrightarrow{\varphi{}_{132}} -> P_1\overset{\varphi{}_{132}}{\relbar\joinrel\relbar}
```

```text
\inserted{\(G\)} -> \inserted{G}
```

```text
\inserted{\(P_i\)} -> \inserted{P_i}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\(G\)
```

L4

```tex
\(P_1\ P_2\ P_3\)
```

L4

```tex
\(G\)
```

L4

```tex
\(\quad s:G\times G\times G\longrightarrow G\quad\)
```

L5

```tex
\[
 P_1\times P_2\times P_3\supset \Gamma\qquad\text{un sous-torseur sous }\operatorname{Ker}s
\]
```

L8

```tex
\(\unsure{\Gamma_1|P_1}\wedge \Gamma_2\wedge \Gamma_3\overset{t}{\simeq}\mathbb{1}_{\unsure{\mathrm{TORS}(G)|\mathrm{Tors}(G)}}\)
```

L11

```tex
\[
 \{G,P_1,P_2,P_3,t\}\longrightarrow(P_1,P_2,P_3,\Gamma)
\]
```

L14

```tex
\(3\)
```

L14

```tex
\(G\)
```

L14

```tex
\(t\)
```

L14

```tex
\(3\)
```

L14

```tex
\(P_1,P_2,P_3\)
```

L14

```tex
\(\Gamma\)
```

L14

```tex
\(P_1\times P_2\times P_3\)
```

L16

```tex
\(p_i:\Gamma\unsure{\relbar\joinrel\relbar|\longrightarrow} P_i,\quad p_{ij}:\Gamma\relbar\joinrel\relbar P_{ij}\quad(i\ne j)\)
```

L18

```tex
\(p_{ij}\)
```

L20

```tex
\((P_1,P_2,P_3\deleted{\unsure{;\Gamma}})\deleted{\unsure{\longrightarrow}}\)
```

L20

```tex
\(\Gamma\subset P_1\times P_2\times P_3\)
```

L21

```tex
\[
 P_1\times P_2\xrightarrow{\pi_3}P_3
\]
```

L25

```tex
\[
 \left\{\begin{aligned}
 \forall\,x_1\in P_1,\quad x_2&\longmapsto \pi_3(x_1,x_2)& P_2&\xrightarrow{\sim}P_3\\
 \forall\,\unsure{x_2|x_3}\in P_2,\quad x_1&\longmapsto \pi_3(x_1,x_2)& P_1&\xrightarrow{\sim}P_3
 \end{aligned}\right.
\]
```

L32

```tex
\[
 P_1\xrightarrow{\unsure{\varphi_{123}|\varphi_{1\,23}}}\operatorname{Isom}(P_2,P_3)
\]
```

L35

```tex
\(=\)
```

L36

```tex
\[
 P_1\overset{\varphi_{132}}{\relbar\joinrel\relbar}\operatorname{Isom}(P_3,P_2)
\]
```

### Indices and exponents containing i or j

- L14: `. \inserted{P_i`.

- L16: `Notons \(p_i`, `rightarrow} P_i`, `} P_i,\quad p_{ij}`, `nrel\relbar P_{ij}`.

- L18: `line{Les} \(p_{ij}`.

## Scan 109

Second reading, UTC: 2026-11-18T09:16:52Z to 2026-11-18T09:18:07Z.

### Before reopening the transcription

“noyau formé des … tels que”, accent on formé weak; no punctuation after que. “Aut”, “int”, “Int” and “Aut G” recur with different capital strokes. The first K to the right of the kernel condition is round at the top as well as being retraced. The inverse exponents are two strokes, short minus then upright 1; in two overwritten lines the raised marks merge with the staff. The lower expression has empty braces drawn under Aut G · (G×G×G). Numerous thin parallel lines touch every word: they are the printed staves. The heavy bend across the top product and the oblique diagonal across the two rows beneath the kernel are separate marks. At the left, between computations, is a solitary open G with an extra short limb.

### Ink, corrections, lettering and margins

The triple of target capitals has a broad upper loop and a doubled lower return, in contrast to the almost rectangular Γ in the quotient. All three have subscripts; the middle is especially open. The mapping stroke ends with a small dot. The first tau subscript has a deep descender, the second has been overwritten near its foot. Prime marks on the translated taus are separate from their lower indices. The four factors and inverse exponents are listed below; no i or j occurs as an index. The line crossing the two inner-automorphism calculations passes through the second calculation and obscures the superscripts on the first. The rising (=g) is an addition after γ, independent of that crossing. A single short horizontal second slot in the middle right and empty denominator braces below are present in the ink. Neither was filled. The lower Γ has a distinct hat on the final line; a heavy previous capital is still visible on the preceding line.

### Changes

```text
\mathscr G_G|\mathcal G_G -> \mathscr G_G|\mathcal G_G|\mathfrak S_G
```

```text
&\longmapsto(\tau_ -> &\unsure{\longmapsto|\relbar\joinrel\relbar}(\tau_
```

```text
\unsure{N|P} -> \unsure{N|P|\mathcal N}
```

```text
g^{-1}(g^{\unsure{-1}} -> \unsure{g|g^{-1}}(g^{\unsure{-1}}
```

```text
\unsure{\Pi{}} -> \unsure{\Pi{}|\Gamma{}}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\[
 u,\alpha,\beta
\]
```

L5

```tex
\[
\begin{aligned}
 &(u,1,1,1)(\deleted{\unsure{\alpha}}1,\deleted{\unsure{\beta}}\alpha,\beta,\unsure{\gamma|\sigma})\inserted{(u^{-1},1,1,1)}
 =(u,u(\alpha),u(\beta),u(\gamma))(u^{-1},1,1,1)\\
 &(1,\alpha,\beta,\gamma)\,(\text{---}\\[-2pt]
 &\hspace{9em}=(\deleted{\unsure{u}}1,u(\alpha),u(\beta),\deleted{\unsure{u}}u(\gamma))
\end{aligned}
\]
```

L13

```tex
\[
\begin{aligned}
 \operatorname{Aut}(G)\mathbin{.}(G\times G\times G)&\longrightarrow
 \unsure{\mathscr G_G|\mathcal G_G|\mathfrak S_G}\times\mathscr G_{\unsure{G|C}}\times\mathscr G_G\\
 (u,\alpha,\beta,\gamma)&\unsure{\longmapsto|\relbar\joinrel\relbar}(\tau_{\unsure{\rho|\beta}}\tau'_{\unsure{\beta|\gamma}}u,\tau_\gamma\tau'_\alpha u,\tau_\alpha\tau'_\beta u)
\end{aligned}
\]
```

L20

```tex
\((u,\alpha,\beta,\gamma)\)
```

L21

```tex
\[
 \alpha=\beta=\gamma\inserted{(=g)},\quad u=\operatorname{int}(g)^{\unsure{-1}}.
 \quad \unsure{N|P|\mathcal N}=\{(\operatorname{int}(g),g^{-1},g^{-1},g^{-1})\mid g\in G\}
\]
```

L25

```tex
\[
\begin{aligned}
 &(\operatorname{int}(g)^{\unsure{-1}},g^{-1})(\operatorname{int}(g')^{\unsure{-1}},{g'}^{-1})
 =(\operatorname{int}(g)^{\unsure{-1}}\deleted{\unsure{\operatorname{int}(g')}}\,,
 \unsure{g|g^{-1}}(g^{\unsure{-1}}{g'}^{\unsure{-1}}g^{-1}))\\
 &\hspace{13em}\deleted{(\operatorname{int}(g'g)^{-1},\,g'g)}
\end{aligned}
\]
```

L33

```tex
\(\unsure{G|G_1}\)
```

L34

```tex
\[
\begin{aligned}
 &(u,\alpha,\beta,\gamma)(\operatorname{int}(g),g^{-1},g^{-1},g^{-1})
 (u^{-1},u^{-1}(\alpha^{-1}),u^{-1}(\beta^{-1}),u^{-1}(\gamma^{-1}))\\
 &u\operatorname{int}(g),\alpha u(g)^{-1},\beta u(g)^{-1},\gamma u(g)^{-1})\ (\text{--------})\\
 &\underbrace{u\operatorname{int}(g)u^{-1}}_{\operatorname{int}u(g)},\
 \alpha u(g)^{-1}\deleted{\unsure{u}}(u\operatorname{int}(g))(u^{-1}(\alpha^{-1})),\ldots\quad)\\
 &\hspace{6em}\underbrace{\alpha u(g^{-1})\,u(gu^{-1}(\alpha^{-1})g^{-1})}_{\unsure{\alpha\alpha^{-1}u(g)^{-1}}}
\end{aligned}
\]
```

L44

```tex
\[
 G\mathbin{.}(G\times G\times G)
\]
```

L47

```tex
\[
 \frac{(\operatorname{Int}G)\mathbin{.}(G\times G\times G)}
 {\{\operatorname{int}(g),g^{-1},g^{-1},g^{-1}\}}
 \simeq\deleted{\unsure{\Pi|\Gamma}}\Gamma(G)
\]
```

L52

```tex
\[
 \frac{\deleted{\unsure{\operatorname{Int}}}\operatorname{Aut}G\mathbin{.}(G\times G\times G)}
 {\{\hspace{4em}\}}\simeq\widehat \Gamma(G)
\]
```

### Indices and exponents containing i or j

- L39: `nt}(g)u^{-1}}_{\operatorname{int}u(g)}`.

## Scan 110

Second reading, UTC: 2026-11-18T09:18:07Z to 2026-11-18T09:19:34Z.

### Before reopening the transcription

“moyennant ceci, on peut identifier donc les Gᵢ au = groupe G, les Pᵢ aux bitorseurs triviaux sous G,G”; “Γ à” at left. “qu'on peut résoudre en x,y,z” has a faint and upward-stroked beginning. “La condition (A) signifie que Γ est … donné par” contains replacement words, with a crossing distinctly below “donné par”. “Si γ … est remplacé par … alors les iso. … sont remplacés par”. Check the last e/és independently, especially the plural in remplacés. The last three rows use lowercase int even when it has a long vertical stroke; superscript minuses sit on the last factors. An isolated dark mark occurs above the set of triples.

### Ink, corrections, lettering and margins

The first line is particularly pale: both proposed readings have the same small initial c, but the connection before the final i is interrupted. G_i and Q_i/P_i have short i; the rest of the indices are numbers 1, 2 and 3. At the first Γ the lowered mark is looped and black; the initial capital is angular, unlike curving G. The condition xyz=1 and the three inverse pairs retain their displayed order. One exponent above the first g₂ is hatched. The central heavy strokes cover older g's under the alpha entries; the loops and descenders remain. The inserted triple has its own curved lead-in to γ; the words inserted over the struck line before the big set have a different baseline from the cancelled words. On the last three lines primes are beside the tilded a, and the exponent −1 is beyond the closing parenthesis of the last int. The underlined stroke near “signifie” belongs to the descending loop of g. No side note other than isolated ink and the archive number.

### Changes

```text
\unsure{ceux-ci} -> \unsure{ceux-ci|ceci}
```

```text
\(Q_i\) -> \(\unsure{Q_i|P_i}\)
```

```text
\unsure{0|e} -> \unsure{0|e|G}
```

```text
\inserted{\unsure{nécess.}} -> \inserted{\text{\unsure{nécess.}}}
```

```text
\inserted{donnée par} -> \inserted{\text{\unsure{donné|donnée} par}}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\(G_i\)
```

L2

```tex
\(=\)
```

L2

```tex
\(G\)
```

L2

```tex
\(\unsure{Q_i|P_i}\)
```

L2

```tex
\(G,G\)
```

L2

```tex
\(\Gamma\)
```

L3

```tex
\[
 \Gamma_{\unsure{0|e|G}}=\{(x,y,z)\in G\deleted{\unsure{^3}}\times G\times G\mid xyz=1\}
\]
```

L6

```tex
\(x,y,z\)
```

L7

```tex
\[
\begin{aligned}
 x&=z^{-1}y^{-1}\\
 y&=x^{-1}z^{-1}\\
 z&=y^{-1}x^{-1}
\end{aligned}\hspace{9em}\biggr)
\]
```

L15

```tex
\(\Gamma\)
```

L16

```tex
\[
 \Gamma=\{(g_2^{\deleted{\unsure{-1}}}\deleted{\unsure{g}}g_3^{-1},g_3g_1^{-1},g_1g_2^{-1})
 \in G\times G\times G\mid g_1,g_2,g_3\in G\}
\]
```

L20

```tex
\(\gamma\inserted{=(a_1,a_2,a_3)}\)
```

L21

```tex
\[
\begin{aligned}
 \gamma'&=\sigma(\deleted{g}\unsure{\alpha_1|g_1},\deleted{g}\alpha_2,\deleted{g}\alpha_3)(\gamma)\\
 &=(\deleted{g}\alpha_2 a_1\deleted{g}\alpha_3^{-1},\deleted{g}\alpha_3 a_2\deleted{g}\alpha_1^{-1},
 \deleted{g}\alpha_1 a_3\deleted{g}\alpha_2^{-1})
\end{aligned}
\]
```

L28

```tex
\(\widetilde{a_{1}},\widetilde{a_{2}},\widetilde{a_{3}}\)
```

L29

```tex
\[
 \deleted{\operatorname{int}(\unsure{g_3|\alpha_3})^{\unsure{-1}}\widetilde{a_{1}}\operatorname{int}(\unsure{g_2|\alpha_2})}
\]
```

L32

```tex
\[
 \left\{\begin{aligned}
 \widetilde a'_1&=\operatorname{int}(\alpha_3)\widetilde a_1\operatorname{int}(\alpha_2)^{-1}\\
 \widetilde a'_2&=\operatorname{int}(\alpha_1)\widetilde a_2\operatorname{int}(\alpha_3)^{-1}\\
 \widetilde a'_3&=\operatorname{int}(\alpha_2)\widetilde a_3\operatorname{int}(\alpha_1)^{-1}
 \end{aligned}\right.
\]
```

### Indices and exponents containing i or j

- L2: `donc les \(G_i`, `s \(\unsure{Q_i`, `\unsure{Q_i\|P_i`.

## Scan 111

Second reading, UTC: 2026-11-18T09:19:35Z to 2026-11-18T09:20:47Z.

### Before reopening the transcription

Upside down in the archive. There is almost no French. “Aut” under Δ×Δ→Δ; the last line of the right brace may end “bijectif” following a crossed word. The arrow at the top right is accompanied by a lone question mark. At the other question the text is “=x₂ ?”. Several handwritten 2s and z's have identical flat bases; the z after x+y= looks especially like 2. Distinguish a physical cross-through from the tilted stroke of an x and the repetitive five-line staff. The bottom three braces of relations show a circle in some lines, a cross/plus in others. Two separate underbrackets under sums at the top.

### Ink, corrections, lettering and margins

Read s3, s2, s1 after a half-turn. A diagonal approaches the initial x in x∘bar x=0 but ends on its left, so the expression is live. A separate stroke really crosses the trial x*y directly underneath. The right-hand stack at the writing top has a descending arrow and a possible question mark. Compared all 16 interior entries of each table to the ink, including the dark u₁ row and the underlined final 1. The last digit of u₁ looks closed with a long downward stem; positional context would favour 0. In the right-hand disjoint equalities a z and 2 both have a horizontal foot; the sign after x+y= is written like 2. The short line under 0 near the bottom is a bar above it, followed by an arrow- or equality-like sign. There are no alphabetic i/j subscripts. Distinguished x₂ and x₃ in all three upper rows, staff lines under every u, the cancelled alternate assignment and the single dark τ in the bracket. No text written on a typed sheet.

### Changes

```text
\end{aligned}\ \bigg\downarrow -> \end{aligned}\ \bigg\downarrow\unsure{?}
```

```text
\unsure{@0\to{}} -> \overline{0}\,\unsure{\to3|=\,?}
```

```text
\deleted{x\circ \overline{x}=0} -> x\circ \overline{x}=0
```

```text
x+y=\unsure{z|2} -> x+y=\unsure{2|z}
```

```text
\unsure{0|9} -> \unsure{9|0}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L3

```tex
\[
\begin{aligned}
 &\deleted{x_2\longrightarrow-x_2-a_1}\\
 &\deleted{x_3\longmapsto-x_3-a_2=x_2+a_1-a_2}\\
 &\deleted{x_1\longmapsto-x_1-a_3=-\underline{x_2-a_1}+a_2-\underline{a_3}}\\
 &\hspace{7em}\deleted{=x_2\ ?}
\end{aligned}\qquad
\begin{aligned}
 a_1+x_2+x_3&=0\\
 x_1+a_2+x_3&=0\\
 x_1+x_2+a_3&=0
\end{aligned}\ \bigg\downarrow\unsure{?}
\]
```

L16

```tex
\[
\begin{aligned}
 &\deleted{a_2-x_2=a_1+x_2+a_3}\qquad a_1+a_2+a_3=0\\
 &\deleted{2x_2=a_2\underline{-a_1-a_3}=a_2+a_2=2a_2}\\
 &\deleted{2(x_2-a_2)=0}
\end{aligned}
\]
```

L23

```tex
\[
\begin{aligned}
 &\deleted{\unsure{-x}}\quad &&x+y+z=0\\
 &\deleted{x\quad -x}&&y\longmapsto-x-y\\
 &&&y\longrightarrow-y\\
 &&&x\longmapsto-x
\end{aligned}
\]
```

L31

```tex
\[
 \Delta\times \Delta\longrightarrow \Delta\qquad
 \begin{aligned}
 y&\longmapsto-x-y\\
 (x,y)&\longmapsto-x,-y
 \end{aligned}\quad
 \begin{aligned}
 x+y+z&=0\\
 -x-y-z&=0
 \end{aligned}
\]
```

L42

```tex
\[
\begin{aligned}
 &x\\
 &\Delta\in\operatorname{Aut}(\Delta)
\end{aligned}\qquad
\begin{aligned}
 &\deleted{(x,y)}\quad x\circ y=-x-y\\
 &(x\circ y)\circ z=x+y-z\\
 &x\circ(y\circ z)=\deleted{\unsure{+}}-x+y+z
\end{aligned}
\]
```

L53

```tex
\diagram{\(\displaystyle\begin{array}{c|c|c|c|c}
 &0&1&2&3\\\hline
 u_0&0&1&2&3\\\hline
 u_1&1&\unsure{2}&3&\unsure{9|0}\\\hline
 u_2&2&3&0&1\\\hline
 u_3&3&0&1&2\\\hline
\end{array}\)}
```

L60

```tex
\[
\begin{aligned}
 &x\circ x=\quad\deleted{2x- \unsure{2z|2x}}\\
 &\unsure{\pi_{u}|u_1}\\
 &\deleted{x\circ y=x*y}
\end{aligned}
\]
```

L67

```tex
\[
\begin{aligned}
 &\deleted{\unsure{x+x}}\quad u_1\,0\qquad &&\deleted{x\circ x'=0}\\
 &0'\qquad x+y=\unsure{2|z}&&\deleted{(x,x',0)}\\
 &x\unsure{*|+}y
\end{aligned}
\]
```

L74

```tex
\diagram{\(\displaystyle u_{\unsure{1}}^{\prime}\qquad
\begin{array}{c|c|c|c|c}
 &0&1&2&3\\\hline
 0&0&1&2&3\\\hline
 \deleted{x+y}\;\unsure{1}&1&0&3&2\\\hline
 \unsure{x}\;2&2&3&1&0\\\hline
 3&3&2&0&\underline{1}\\\hline
\end{array}\)}
```

L82

```tex
\[
\begin{aligned}
 &x\circ y &&x\circ \overline{x}=0 &&\overline{x\circ y}=x*y\\
 &&&\overline{0}\,\unsure{\to3|=\,?} &&\overline{x}*\overline{y}=\overline{\overline{x}\circ \overline{y}}\\
 &\deleted{x*y} &&x*y &&
 \left\{\begin{aligned}
 x*y&=y*x\\ 0*y&=y\\x*0&=x\\
 \tau_x&\ \deleted{\unsure{\text{est}}}\ \text{\unsure{bijectif}}
 \end{aligned}\right.
\end{aligned}
\]
```

L93

```tex
\[
 x\circ y=\overline{x*y}\qquad
 \begin{gathered}\deleted{\unsure{\tau_x\quad x\circ x=0}}\\ 0\circ y=\overline{y}\end{gathered}
\]
```

### Indices and exponents containing i or j

No alphabetic i or j appears in a subscript or superscript in the adopted reading.

## Scan 112

Second reading, UTC: 2026-11-18T09:20:48Z to 2026-11-18T09:22:06Z.

### Before reopening the transcription

No prose or accent that can be ascribed to a word. At writing top the three first symbols have little horizontal or wavy caps. Underneath are x₁ x₂ x₃. In the right column the thick final operand of the second triple looks like u₃, followed by ∈ Γ, and the next one begins with an oval. The four in the left edge is followed by a curved mark. In the tables several 0s are loops filled with ink and several 3s have their lower curves redrawn. Read “0,14” and “02” beside the sideways diagram separately; the comma-like sign before 4 is small. Pairs in the sideways display are separated by wedges. No explanatory phrase accompanies the scribbled end of the first column.

### Ink, corrections, lettering and margins

The first three looped letters in writing orientation carry real caps, particularly the third, on which the pen rises again. In the independent quarter-turn reading, o₁ is above P₁; G₂, G₃ flank P₁, P₃ and P₂ have a short dash between them, G₁ is below. A single diagonal cuts through P₁ and the equivalence on the following line. Two large round enclosures and the roof-shaped line belong to the drawing itself. A 4-like upright with a curved second trace is at the far edge of the table. Re-read the two ruled five-by-five grids by rows and columns. Row 4 of the first ends in a blank crossed by a slant; the second grid is crossed as a whole. The short unruled list has overdrawn 2, 3, 4 and a final vertical scribble; its trailing empty positions are present on the paper. There is no i or j index. Rechecked u/v/w, O/0/o, the unmatched left parenthesis and dot at the right and raised −1 in the rejected trial.

### Changes

```text
\unsure{o_1|0_1},&o_2,&o_3) -> \unsure{\overline{a}_1|\overline{o}_1|o_1},&\unsure{\overline{a}_2|\overline{o}_2},&\unsure{\widetilde{a}_3|\widetilde{o}_3})
```

```text
(\,
\end{aligned} -> (\,\cdot
\end{aligned}
```

```text
\margin{\(0,1,4\quad 0\,2\)} -> \margin{\unsure{4)|4.}}\margin{\(0,\unsure{1,4|14}\quad 0\,2\)}
```

```text
P_1\arrow[dl,dash] -> \deleted{\unsure{P_1}}\arrow[dl,dash]
```

```text
\wedge}P_3\simeq\mathbb{1}_{G_2} -> \wedge}P_3\deleted{\simeq}\mathbb{1}_{G_2}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L3

```tex
\[
 \begin{array}{ccc}
 (\deleted{\unsure{x}} \unsure{\overline{a}_1|\overline{o}_1|o_1},&\unsure{\overline{a}_2|\overline{o}_2},&\unsure{\widetilde{a}_3|\widetilde{o}_3})\in \Gamma\\
 x_1&x_2&x_3
 \end{array}
\]
```

L9

```tex
\[
\begin{aligned}
 &\deleted{\unsure{a_1}}\ x_2\in P_2 \xrightarrow[\sim]{\widetilde o_1}P_3
 &\qquad \widetilde o_1(x_1)&=\unsure{\zeta_1|\xi_1}\\
 &\hspace{4em}o_2\qquad o_3 &&\deleted{x_1=\widetilde o_1^{-1}\bigl(}\\
 &\deleted{x_1\in P_1\xrightarrow[\sim]{\unsure{\widetilde b_2|\widetilde o_2}}P_3}\\
 &\hspace{4em}o_{\unsure{1|2}}\qquad o_2
\end{aligned}
\]
```

L18

```tex
\[
\begin{aligned}
 (o_1,o_2,o_3)&\in \Gamma\\
 (x_1,o_2,\unsure{u_3|y_3})&\in \Gamma\\
 (o_1,x_2,v_3)&\in \Gamma\\
 \unsure{u_{12}|u_2}\qquad w_3&\in P_3\\[2pt]
 (x_1,\deleted{\unsure{y}}x_2,\deleted{\unsure{u}}y_3)&\in \Gamma\\
 (z_1,o_2,y_3)&\in \Gamma\\
 (z_1,w_3,p_3)&\in \Gamma\\
 (\,\cdot
\end{aligned}
\]
```

L30

```tex
\[
 \begin{aligned}
 P_3\times P_3&\longrightarrow P_3\\
 &P_3\times P_3\times \Gamma\\
 &P_3\times \Gamma
 \end{aligned}
\]
```

L37

```tex
\diagram{\(\displaystyle\begin{array}{c|c|c|c|c|c}
 &0&1&2&3&4\\\hline
 0&\deleted{0}&1&2&3&4\\\hline
 1&\deleted{1}&0&3&4&2\\\hline
 2&2&3&4&\unsure{1|0}&\unsure{0|1}\\\hline
 3&3&4&\unsure{1|0}&0&2\\\hline
 4&4&2&\deleted{\unsure{1}}0&2&\\\hline
\end{array}\)}
```

L45

```tex
\(0,\unsure{1,4|14}\quad 0\,2\)
```

L47

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.7em,row sep=.2em]
 \&\& o_1\arrow[ddll,dash,bend right=8]\arrow[ddrr,dash,bend left=8]\&\&\\
 \&G_2\&\deleted{\unsure{P_1}}\arrow[dl,dash]\arrow[dr,dash]\&G_3\&\\
 o_3\arrow[rr,dash,bend right=90]\&P_3\arrow[rr,dash]\&{}\&P_2\&o_2\arrow[ll,dash,bend left=90]\\
 \&\&G_1\&\&
\end{tikzcd}}
```

L53

```tex
\[
 \begin{gathered}
 P_1\underset{G_3}{\wedge}P_2\underset{G_1}{\wedge}P_3\deleted{\simeq}\mathbb{1}_{G_2}\\[-2pt]
 G_2\ \raisebox{.3ex}{\(\scriptscriptstyle-\)}\hspace{12em} G_{\unsure{2|\,}}\\
 P_2\wedge P_3\wedge P_1\simeq
 \end{gathered}
\]
```

L61

```tex
\diagram{\(\displaystyle\begin{array}{ccccc}
 0&1&2&3&4\\
 1&2&3&4&3\\
 2&\deleted{\unsure{2}}3&4&&\\
 3&\unsure{0}4&&&\\
 4&\deleted{\unsure{3}}4\,0&&&\\
 \unsure{\uparrow|1}&&&&
\end{array}
\qquad
\deleted{\begin{array}{c|ccccc}
 &0&1&2&3&4\\\hline
 0&0&1&2&3&4\\
 1&1&2&3&4&0\\
 2&2&3&4&0&1\\
 3&3&4&0&1&2\\
 4&4&0&1&2&3
\end{array}}\)}
```

### Indices and exponents containing i or j

No alphabetic i or j appears in a subscript or superscript in the adopted reading.

## Scan 113

Second reading, UTC: 2026-11-18T09:22:07Z to 2026-11-18T09:28:54Z.

### Before reopening the transcription

“bitorseur sous”, the plural-looking terminal is faint; “opposé de P₁” above and to the right of P₁°; “etc.” above the two slanted divider strokes; abbreviated “bitors.” at the right product. “tel que” follows nonempty Γ. “NB”, “opère”, “l'axiome envisagé, c'est que Γ est une orbite sous…”, “induite par prᵢ”, “Supposons fixé un p[oin]t”, “d'où des iso.”. Either “ssi” or three short waved strokes beside g₂a₁. At the foot “C'est un syst. transitif d'iso, car” runs to the right as an unfinished sentence. Superscript small open o's on all the opposite factors, some with dots. No acute accent on the large initial capitals.

### Ink, corrections, lettering and margins

There are two strokes dividing the prose at the top of the product list. The separate black double-vertical trace between the arrays is included. In the six products, the o is visibly high, not a subscript zero; the unit has two downstrokes and a foot. Compared the group on each side of every unit, including the obscured prefix at upper right. The long “tel que” insertion curve starts before the words and points up to Γ≠∅. The x near the third slot of σ is reduced to a hook; compare numeral 3 against descending j. In the p_i projection, pr_i and a_i=p_i(γ), the short index has no descender. Re-examined the left crossed triangle, the scratched word beside “Supposons”, and the cancelled last exponent in g₂. The second of the three bottom shafts lacks a visible head; the third has two heads. The foot trails off after a very faint connective.

### Changes

```text
\text{etc.}\ / -> \text{etc.}\ /\!/
```

```text
\text{\unsure{bit. ss}} -> \text{\unsure{bit. ss|bitors. ss}}
```

```text
&\deleted{\unsure{P}}P_1 -> \quad\deleted{\unsure{\mathbb{1}|1}}&\deleted{\unsure{P}}P_1
```

```text
\overset{\widetilde a_2}{\longrightarrow} -> \overset{\widetilde a_2}{\relbar\joinrel\relbar}
```

```text
\xleftrightarrow{\widetilde a_3} -> \overset{\widetilde a_3}{\longleftrightarrow}
```

```text
d'iso, \unsure{i.e.} -> d'iso, \unsure{donc|car|i.e.}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.55em,row sep=.65em]
 \&\deleted{\unsure{G'_1}\ P_1\ G_1}\arrow[dl,dash]\arrow[dr,dash]\&\&\&P_1\arrow[dl,dash,"G_2"']\arrow[dr,dash,"G_3"]\&\\
 \deleted{G_2\ P_2}\arrow[rr,dash,"\deleted{\unsure{G_2\,G_3}}"']\&\&\deleted{P_3\,G'_3}\&
 P_3\arrow[rr,dash,"G_1"']\&\&P_2
\end{tikzcd}}
```

L7

```tex
\[
\begin{array}{lll@{\qquad}lll}
 P_1&\text{bitorseur sous}&G_2,G_3&P_1^{\mathrm o}&\text{bitorseur sous}&G_3,G_2\\
 P_2&\text{-------------}&G_3,G_1&P_2^{\mathrm o}&\text{---------}&G_1,G_3\\
 P_3&\text{-------------}&G_1,G_2&P_3^{\mathrm o}&\text{---------}&G_2,G_1
\end{array}
\]
```

L14

```tex
\(P_1^{\mathrm o}\nearrow\)
```

L14

```tex
\(P_1\)
```

L15

```tex
\[
 P_1\wedge P_2\wedge P_3\quad\text{bitorseur sous }G_2,G_2\quad\text{etc.}\ /\!/\quad
 P_3^{\mathrm o}\wedge P_2^{\mathrm o}\wedge P_1^{\mathrm o}\quad\text{\unsure{bit. ss|bitors. ss}}\,G_{\unsure{1|2}},G_2
\]
```

L19

```tex
\[
\begin{aligned}
 P_1\wedge P_2\wedge P_3&\xrightarrow[\sim]{\unsure{\varphi_2}}\deleted{\unsure{G_2}}{}_{G_2}\mathbb{1}_{G_2}
 &P_3^{\mathrm o}\wedge P_2^{\mathrm o}\wedge P_1^{\mathrm o}&\overset{\varphi_2^{\mathrm o}}{\simeq}\deleted{\unsure{\operatorname{bit}}}{}_{G_2}\mathbb{1}_{G_2}\\
 P_2\wedge P_3\wedge P_1&\overset{\varphi_3}{\simeq}{}_{G_3}\mathbb{1}_{G_3}
 \quad\deleted{\unsure{\mathbb{1}|1}}&\deleted{\unsure{P}}P_1^{\mathrm o}\wedge P_2^{\mathrm o}\wedge P_3^{\mathrm o}&\overset{\varphi_3^{\mathrm o}}{\simeq}{}_{G_3}\mathbb{1}_{G_3}\\
 P_3\wedge P_1\wedge P_2&\overset{\varphi_1}{\simeq}{}_{G_1}\mathbb{1}_{G_1}
 &P_2^{\mathrm o}\wedge P_1^{\mathrm o}\wedge P_3^{\mathrm o}&\overset{\varphi_1^{\mathrm o}}{\simeq}{}_{G_1}\mathbb{1}_{G_1}
\end{aligned}
\]
```

L29

```tex
\[
 \Gamma\subset P_1\times P_2\times P_3\quad\inserted{\Gamma\ne\varnothing}\quad\text{tel que}
\]
```

L32

```tex
\[
 \left\{\begin{aligned}
 x=(x_1,x_2,x_3)&\in P_1\times P_2\times P_3\\
 g_1\in G_1,\ g_2&\in G_2,\ g_3\in G_3
 \end{aligned}\right.
 \Rightarrow\left(\begin{aligned}
 &(x_1,x_2,x_3)\in \Gamma\\
 &\Longleftrightarrow g_2x_1g_3^{-1},g_3x_2g_1^{-1},g_1x_3g_2^{-1}\\
 &\hspace{12em}\in \Gamma
 \end{aligned}\right)
 \tag*{(A)}
\]
```

L44

```tex
\(\ G_1\times G_2\times G_3\)
```

L44

```tex
\(P_1\times P_2\times P_3\)
```

L45

```tex
\[
 \sigma(g_1,g_2,g_3)\mathbin{:}(x_1,x_2,\unsure{x_3|x_j})
 =(g_2x_1g_3^{-1},g_3x_2g_1^{-1},g_1x_3g_2^{-1})
\]
```

L49

```tex
\(\Gamma\)
```

L49

```tex
\(G_1\times G_2\times G_3\)
```

L50

```tex
\[
 \Gamma\xrightarrow{p_i}P_i\quad\text{induite par \unsure{pr.}$_i$}
\]
```

L53

```tex
\(\gamma\in \Gamma\)
```

L53

```tex
\(a_i=p_i(\gamma)\)
```

L54

```tex
\[
\begin{aligned}
 G_2&\xrightarrow{\widetilde a_1}G_3&
 &g_2\text{ et }g_3\text{ se correspondent}\\
 &&&\text{ssi}\quad g_2a_1=a_1g_3\\
 G_3&\overset{\widetilde a_2}{\relbar\joinrel\relbar} G_1&
 &g_3\text{ et }g_1\quad\text{---}\qquad g_3a_2=a_2g_1\\
 G_1&\overset{\widetilde a_3}{\longleftrightarrow}G_2&
 &g_1\text{ et }g_2\quad\text{---}\qquad g_1a_3=a_3g_2^{\deleted{\unsure{-1}}}
\end{aligned}
\]
```

### Indices and exponents containing i or j

- L46: `\unsure{x_3\|x_j`.

- L51: `xrightarrow{p_i`, `htarrow{p_i}P_i`, `\unsure{pr.}$_i`.

- L53: `ù des pts \(a_i`, `s pts \(a_i=p_i`.

## Scan 114

Second reading, UTC: 2026-11-18T09:28:55Z to 2026-11-18T09:30:02Z.

### Before reopening the transcription

“Soit”, “V vectoriel de dim 2 sur F₂”, “I ens de card. 3”, “une famille de V-torseurs”, “(torseur trivial) un isom.”. “formé des … tels que”, “(ens. à 16 éléments)”; “un rev. d'ordre 2”; “autom d'ordre 2 noté σ” follows a bar at the right. “de rev. de Γ” with “associé” below. “Soit … (de cardinal 3×8=24)”; “On introduit dans P une structure de graphe”; “liés ssi”, “ou bien” twice. “NB le γ est unique – donc si on…”, lightly written end. “Question” is crossed and underlined. “Axiome”, “injectif”, “sous-groupe”, “opérant”, “devient”, “sous-ent…”, “injections”, “des images disjointes”. Inverted title at the foot reads “Assemblée Gén. Ex”, acute accents on the ends of Assemblée and on Gén. Two very small marks between these words and Ex may be abbreviating punctuation.

### Ink, corrections, lettering and margins

The P after “dans” and the P in the raised admission condition appear plain even though the disjoint union above has a tilde. A single hook leads that insertion between the coordinate pair and “liés”. In the second branch the relation between i and the long descending j has two parallel strokes and a dark right end; a slash cannot be securely separated. In α_ji, α_jh, π_i, p_j, P_i and P_j a short dotted stroke contrasts with the much deeper ending of j. Checked every index within the group power, section set and projection. The black marks through “section”, the discarded first existential test, “Question”, “tout x”, “fait”, “devient”, and a word before “de” are separate from the x-height strokes on the live next line. Papery straight bars separate alternatives and the two covering maps. The F in the field has a double downstroke; 1 at the unit has its separately drawn foot. At the very bottom “Assemblée Gén. Ex” is the other way up; the last two capitals may be an abbreviation. No printed form or typewriting.

### Changes

```text
\unsure{\longrightarrow|\text{---}} -> \unsure{\relbar\joinrel\relbar|\longrightarrow}
```

```text
\inserted{\in\widetilde P\ (x\ne y)} -> \inserted{\in P\ (x\ne y)}
```

```text
\text{ avec }i\ne j -> \text{ avec }i\unsure{=|\ne} j
```

```text
\unsure{déf. d'arêtes|déf. d'étiq.} -> \unsure{déf. de lien|déf. d'arêtes|déf. d'étiq.}
```

```text
qui \deleted{devient} un torseur -> qui \deleted{devient}) un torseur
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\(V\)
```

L2

```tex
\(2\)
```

L2

```tex
\(\mathbb F_2\)
```

L4

```tex
\(I\)
```

L4

```tex
\(3\)
```

L6

```tex
\((P_i)_{i\in I}\)
```

L6

```tex
\(V\)
```

L8

```tex
\(\bigwedge_{i\in I}P_i\overset{\varphi}{\simeq}\mathbb{1}\)
```

L10

```tex
\(\Gamma\subset\prod_{i\in I}P_i\)
```

L10

```tex
\((x_i)_{i\in I}\)
```

L10

```tex
\(\bigwedge_{i\in I}x_i=0\)
```

L14

```tex
\[
 \begin{aligned}
 \forall i\in I,\quad \widetilde P_i&\xrightarrow{\pi_i}P_i&&\text{un rev. d'ordre 2}\\
 \widetilde \Gamma&\xrightarrow{\pi}\Gamma&&\text{un rev d'ordre 2}
 \end{aligned}\ \bigg|\quad\text{\unsure{autom.} d'ordre 2 noté }\sigma
\]
```

L20

```tex
\(\forall i\in I\)
```

L20

```tex
\(\widetilde \Gamma\simeq \Gamma\times_{P_i}\widetilde P_i\)
```

L20

```tex
\(\Gamma\)
```

L20

```tex
\(\widetilde p_i:\widetilde \Gamma\,\unsure{\relbar\joinrel\relbar|\longrightarrow}\,\widetilde P_i\)
```

L22

```tex
\(\widetilde P=\coprod_{i\in I}\widetilde P_i\)
```

L22

```tex
\(3\times8=24\)
```

L24

```tex
\(P\)
```

L26

```tex
\(\widetilde x,\widetilde y\inserted{\in P\ (x\ne y)}\)
```

L27

```tex
\[
 \left|\begin{aligned}
 &\text{ou bien }\exists i\in I\text{ avec }x,y\in\widetilde P_i,\quad y=\sigma x\quad\text{i.e. }\pi_i(x)=\pi_i(y)\\
 &\text{ou bien }\deleted{\exists\widetilde \gamma\in\widetilde \Gamma\ \unsure{\text{et}}}
 x\in\widetilde P_i,\ y\in\widetilde P_j\text{ avec }i\unsure{=|\ne} j,\text{ et }\exists \gamma\in\widetilde \Gamma\text{ avec}\\
 &\hspace{8em}x_{\unsure{1|i}}=\widetilde p_i(\gamma),\ y=\widetilde p_j(\gamma)
 \end{aligned}\right.
\]
```

L35

```tex
\(\gamma\)
```

L39

```tex
\(i\ne j\)
```

L39

```tex
\(x\)
```

L39

```tex
\(\forall\,\widetilde x_i\in\widetilde P_i\)
```

L39

```tex
\(y_j\in P_j\)
```

L39

```tex
\(\exists!\,\widetilde y_j\in\widetilde P_j\)
```

L39

```tex
\(y_j\)
```

L39

```tex
\(\widetilde x_i\)
```

L41

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=2em,row sep=1em]
 \widetilde P_i\arrow[d]\&\widetilde P_j\arrow[d]\\P_i\&P_j
\end{tikzcd}}
```

L44

```tex
\(\widetilde P_i\xrightarrow{\alpha_{ji}}\Gamma(\widetilde P_j/P_j)\)
```

L44

```tex
\(\unsure{+|t}(P_j)=\operatorname{Ker}(\mathbb F_2^{P_j}\xrightarrow[\text{\unsure{add.} somme}]{}\mathbb F_2)\)
```

L44

```tex
\(\mathbb F_2^{P_j}\)
```

L44

```tex
\(\Gamma(\widetilde P_j/P_j)\)
```

L46

```tex
\(\alpha_{ji},\alpha_{jh}\)
```

L46

```tex
\(\widetilde P_i\)
```

L46

```tex
\(\widetilde P_h\)
```

L46

```tex
\(\Gamma(\unsure{\overline P_j|\widetilde P_j}/P_j)\)
```

### Indices and exponents containing i or j

- L6: `\((P_i`, `\((P_i)_{i\in I}`.

- L8: `\(\bigwedge_{i\in I}`, `dge_{i\in I}P_i`.

- L10: `a\subset\prod_{i\in I}`, `rod_{i\in I}P_i`, `ormé des \((x_i`, `é des \((x_i)_{i\in I}`, `e \(\bigwedge_{i\in I}`, `dge_{i\in I}x_i`.

- L16: `\widetilde P_i`, `ightarrow{\pi_i`, `arrow{\pi_i}P_i`.

- L20: `\Gamma\times_{P_i}`, `amma\times_{P_i`, `}\widetilde P_i`, `(\widetilde p_i`, `,\widetilde P_i`.

- L22: `lde P=\coprod_{i\in I}`, `}\widetilde P_i`.

- L29: `n\widetilde P_i`, `ext{i.e. }\pi_i`, `}\pi_i(x)=\pi_i`.

- L31: `n\widetilde P_i`, `n\widetilde P_j`.

- L32: `\hspace{8em}x_{\unsure{1\|i}}`, `=\widetilde p_i`, `=\widetilde p_j`.

- L39: `,\widetilde x_i`, `n\widetilde P_i`, `nsure{tt} \(y_j`, `t} \(y_j\in P_j`, `,\widetilde y_j`, `n\widetilde P_j`, `P_j\) sur \(y_j`, `(\widetilde x_i`.

- L42: `\widetilde P_i`, `&\widetilde P_j`, `j\arrow[d]\\P_i`, `ow[d]\\P_i\&P_j`.

- L44: `(\widetilde P_i`, `tarrow{\alpha_{ji}`, `(\widetilde P_j`, `detilde P_j/P_j`, `unsure{+\|t}(P_j`, `}(\mathbb F_2^{P_j}`, `mathbb F_2^{P_j`, `\(\mathbb F_2^{P_j}`, `mathbb F_2^{P_j`, `(\widetilde P_j`, `detilde P_j/P_j`.

- L46: `ions \(\alpha_{ji}`, `a_{ji},\alpha_{jh}`, `(\widetilde P_i`, `e{\overline P_j`, `\|\widetilde P_j`, `etilde P_j}/P_j`.

## Scan 115

Second reading, UTC: 2026-11-18T09:30:03Z to 2026-11-18T09:31:19Z.

### Before reopening the transcription

The phrase in the middle is “groupe libre … engendré par”; a small word before engendré is cancelled. “id” has a clear accent-like dot on i. On this sheet uppercase X/Y and lowercase x/y can be very close; the tops of X on the left fork and in the deletion of the two coordinate lines are inked over. “21/42” low on the right is separated by a long oblique bar. At the foot the bracket is above both x₁ and a₂ in one parenthesis. The left of the two factors within the last comparison is definitely E, with two fairly long horizontal arms. Stars at α are higher than the x,y subscripts. Most of the horizontal lines are printed staff ruling, but the low brace below the polynomial is drawn separately.

### Ink, corrections, lettering and margins

A high bar with small turned-down extremities spans the single ordered pair at the triangle. The bold second coordinate still permits a or x. In the square, the diagonal runs into the x₂ label and merges with the oblique of x. There is no independent deletion crossing it. The two vertical labels have the curved foot of 2; both alternatives have been retained. The last subscript of the second α* reads a,b, including a round first letter, although x,b would make a symmetric normalization. The star is separated from id's i. Re-examined the dark letters under the excluded row and column generators, the first E at E_y, the cross before xy and the cut-through comparison at the end. Only a_i and P_i at the foot take the little alphabetic i; the other small straight marks are 1 within a pair or an inverse. The first and final E have two arms and a foot without a separate repeated stem. The two Greek capitals Γ have an angular shoulder. Two copies of γ∈Γ occur on different sides of the long separator.

### Changes

```text
\&\&\deleted{\unsure{x_2}}\& -> \&\&\unsure{x_2}\&
```

```text
(\overline{\unsure{x_1,a_2|x_1}},\unsure{a_2|x_2}) -> (\overline{x_1,\unsure{a_2|x_2}})
```

```text
\unsure{\text{NB}} -> \unsure{\text{NB}|\text{où}}
```

```text
X\times Y-\{a\}\times Y-X\times\{b\} -> X\times Y-\deleted{\unsure{X}}\{a\}\times Y-\deleted{\unsure{Y}}X\times\{b\}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.6em,column sep=.5em]
 \&P_3\&\&\&\&\&\&x_1\\
 \&\Gamma\arrow[u]\arrow[dl]\arrow[dr]\&\&\&P_1\times P_2\arrow[dl]\arrow[dr]\&\&
 {(x_1,x_2)}\arrow[ur,"\sim"]\arrow[dr,dash,"\sim"']\&\\
 P_1\&\&P_2\&\underset{a_1}{P_1}\&\&\underset{a_2}{P_2}\&\&x_2
\end{tikzcd}}
```

L8

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.2em,column sep=.8em]
 \&{(x_1,x_2)}\arrow[rr,"\sim"]\arrow[dl,"\sim"']\arrow[dd,"\unsure{2|\sim}"]\&\&{(a_1,x_2)}\arrow[dl,dash]\arrow[dd,"\unsure{2|\sim}"]\\
 x_1\arrow[dd,equal]\&\&\unsure{x_2}\&\\
 \&{(x_1,a_2)}\arrow[dl,"\sim"']\arrow[rr,"\sim"]\&\&{(a_1,a_2)}\\
 x_1\&\&\&
\end{tikzcd}}
```

L14

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.5em,column sep=1em]
 \&\deleted{\unsure{Y}}X\times Y\arrow[dl]\arrow[dr]\&\\
 \underset{a}{X}\&\&\underset{b}{Y}
\end{tikzcd}}
```

L18

```tex
\[
 x\xrightarrow[\sim]{\alpha_{x,y}}y\qquad
 \begin{aligned}x&\simeq b\\y&\simeq a\end{aligned}
 \qquad\begin{aligned}E_a&\simeq E_b\\\deleted{\unsure{E}}E_y&\simeq E_a\end{aligned}
 \qquad E_a\simeq E_b\simeq E
\]
```

L24

```tex
\[
 \frac{\unsure{6|5}\cdot16\cdot2}{N}\qquad x\qquad
 \begin{aligned} E_x&\simeq E\\E_y&\simeq E\end{aligned}
\]
```

L28

```tex
\[
\begin{aligned}
 &\alpha_{xy}^{*}:E\longrightarrow E\\
 &\unsure{\text{NB}|\text{où}}\quad \alpha_{a,y}^{*}=\alpha_{a,b}^{*}=\mathrm{id}
\end{aligned}
\]
```

L34

```tex
\(\alpha_{xy}^{*}\quad
(x,y)\in \deleted{\unsure{Y}}X\times Y-\deleted{\unsure{X}}\{a\}\times Y-\deleted{\unsure{Y}}X\times\{b\}\)
```

L37

```tex
\[
\begin{aligned}
 X\times Y&\xrightarrow{\pi} Z\\
 E_{x,y}&\simeq E_{\deleted{\unsure{z}}\pi(x,y)}
\end{aligned}
\qquad
\begin{aligned}
 &\deleted{\unsure{xy}}\quad xy=x'y'=\pi\\
 &(e,\pi)\quad(\unsure{\pi|x},e)\\
 &y=x^{-1}\pi\\
 &\deleted{\unsure{\in}}\quad x\ne e
\end{aligned}
\]
```

L50

```tex
\[
 \underset{\substack{\Vert\\E}}{E_{e,\pi}}
 \overset{\varphi_{\pi;x}}{\simeq}
 \underset{\substack{\Vert\\E}}{E_{x,x^{-1}\pi}}
\]
```

L55

```tex
\[
 \begin{aligned}
 &n^2-2n+1\\
 &{}+(n-1)n=\underbrace{2n^2-3n+1}
 \end{aligned}
 \qquad \gamma\in \Gamma\qquad 21\;/\;42
\]
```

L62

```tex
\[
 \gamma\in \Gamma\qquad a_i\in P_i
\]
```

L65

```tex
Drawing labels: (\overline{x_1,\unsure{a_2|x_2}})
```

L69

```tex
\[
 \underset{\substack{\Vert\\E_\gamma}}{E_{x_1}}\deleted{\simeq E_{x_2}}
\]
```

### Indices and exponents containing i or j

- L63: `Gamma\qquad a_i`, `quad a_i\in P_i`.

## Scan 116

Second reading, UTC: 2026-11-18T09:31:20Z to 2026-11-18T09:33:11Z.

### Before reopening the transcription

Only a few French letters: “moyennant” at middle right, trailing-off and very pale. “s” attached to the origin point of Γ; “pᵢ(s)=aᵢ”. The coordinate to the right of the little fork is a₂. The letters u, v, w sit on different arrows. Around Γ split into five pieces the stars, small circles, and the arrows down from the cardinalities sit at three different heights. The first and last symbols in the lower line of P's are starred P₂ and starred Γ. Under the boxed expression there is a heavily stroked trial. Before “(n−1)” in the box a black patch precedes the parenthesis. In the final two fraction-like lines distinguish the stem of ξ from ζ and the long tail of η.

### Ink, corrections, lettering and margins

At p_i(s), a_i, E_{p_i(γ)}, Γ_i and under the intersection, the small i is distinct from the following parenthesis or from an inverse −1 above the adjacent p. The small tick just below Γ₁ was absent in the first pass. The round sign over the last Γ has its own baseline independent of the star at its right. Rechecked the three E projections in each fork, which way arrows point, and the translation labels u,v,w. The box really has an over-written dark patch between 3 and (n−1). Counted n², the sign at 1 and the two separate subtractions in the curly-braced partition; the very pale last coefficient in the box remains marked independently. Two polynomial trials above and below are crossed. The nonsuperscript n in 2n−3n+1 and the apparently ordinary plus at the end of a→a+b are retained. No additional paragraph follows the last two inverse relations.

### Changes

```text
{\Gamma{}_1\cup \Gamma{}_2\cup \Gamma{}_3} -> {\underset{\unsure{1|i}}{\Gamma{}_1}\cup \Gamma{}_2\cup \Gamma{}_3}
```

```text
\mathbin{.}\unsure{2|1}(n-1) -> \mathbin{.}\deleted{\unsure{2|1}}(n-1)
```

```text
\Gamma{}^{\unsure{\circ *|*}} -> \overset{\unsure{\circ|o}}{\Gamma{}}^{*}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

```text
\unsure{…}_i^a -> {\unsure{…}}_i^a (grouped to keep following scripts on the base)
```

### Formula ledger

L2

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.5em,column sep=.8em]
 \&P_3\&\\
 \&\Gamma\quad s\arrow[u]\arrow[dl]\arrow[dr]\&\\
 P_1\&\&P_2
\end{tikzcd}}
```

L7

```tex
\[
 p_i(s)=a_i\qquad E=E_s\simeq E_{a_i}
\]
```

L10

```tex
\[
 x_1\in P_1\qquad \gamma\longrightarrow(x_1,a_2)
\]
```

L13

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.35em]
 E_\gamma\arrow[r,"\sim"]\arrow[d,"\unsure{2|\sim}"]\& E_{x_1}\\
 E_{a_2}\&\\
 E=E_s\arrow[u,"\sim"']\&
\end{tikzcd}}
```

L18

```tex
\[
 \begin{aligned}E_{x_1}&\simeq E\\ E_{x_2}&\simeq E\\E_{x_3}&\simeq E\end{aligned}
 \qquad E_\gamma\simeq E_{p_i(\gamma)}
\]
```

L22

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.4em,column sep=1em]
 \&\unsure{24}\& E\\
 E\&E_\gamma\arrow[l,"u"']\arrow[ur,"v"]\arrow[dr,"w"]\&\\
 \&\&E
\end{tikzcd}}
```

L27

```tex
\[
 E_\gamma\longrightarrow E\quad\text{\unsure{moyennant}}
\]
```

L30

```tex
\[
 \gamma\ne s\qquad {\unsure{\zeta|\xi}}_1^\gamma+\zeta_2^\gamma+\unsure{\eta_3^\gamma|\zeta_3^\gamma}=0
 \qquad \gamma\longrightarrow a_1,x_2,x_3
\]
```

L34

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.4em,column sep=.55em]
 E_{x_3}^{\deleted{\unsure{\zeta}}}\&\&\\
 \&E_\gamma\arrow[ul,"\sim"']\arrow[r,"\sim"]\arrow[d,"\sim"]\&E_{x_2}\arrow[ddl,bend left=17]\\
 \&E_{a_1}\arrow[d,"\sim"]\&\\
 \&E\&
\end{tikzcd}}
```

L40

```tex
\[
 \deleted{2n^2-1}
\]
```

L43

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.55em]
 \widetilde \Gamma\arrow[d]\\\Gamma\subset G\times G\times G
\end{tikzcd}}
```

L46

```tex
\[
 \unsure{g_1+g_2+g_3=0}\qquad p_i^{-1}(a_i)
\]
```

L49

```tex
\[
 \overset{\phantom{1}}{\Gamma}=
 \overset{1}{\{s\}}\ \cup\
 \overset{\overbrace{\phantom{\Gamma_1\ \cup\ \Gamma_2\ \cup\ \Gamma_3}}^{n^{\deleted{\unsure{2}}}-1}}
 {\underset{\unsure{1|i}}{\Gamma_1}\cup \Gamma_2\cup \Gamma_3}\ \cup\
 \overset{\overbrace{\phantom{\Gamma^{*}}}^{n^2-3(n-1)-1=n^2-3n+2}}
 {\overset{\unsure{\circ|o}}{\Gamma}^{*}}
\]
```

L57

```tex
\[
 \Gamma_i=p_i^{\unsure{-1}}\{a_i\}-\{s\}
 \qquad\begin{aligned}
 \overset{\circ}{\Gamma}&=\bigcap_i p_i^{-1}(P_i-\{a_i\})\\
 &=\Gamma-\bigcup \Gamma_i-\{s\}.
 \end{aligned}
\]
```

L64

```tex
\[
 \begin{aligned}
 x&\xrightarrow{\sim}y\\0&\longrightarrow y-x\\0&\longrightarrow a\\
 0&\longrightarrow b\qquad a\longrightarrow a+b
 \end{aligned}
 \qquad
 \boxed{3\mathbin{.}\deleted{\unsure{2|1}}(n-1)+2(n^2-\unsure{3|6}n+2)}
\]
```

L72

```tex
\[
 \begin{aligned}
 &\deleted{\unsure{n^2\!+2}}\\
 &2n-3n+1\qquad 3n-3=3(n-1)
 \end{aligned}
\]
```

L78

```tex
\[
 P_2^{*},P_3^{*},P_1^{*},\quad \Gamma^{*}\qquad
 \begin{aligned}
 vu^{-1}&=\zeta\\wu^{-1}&=\eta
 \end{aligned}
 \qquad
 \left\{\begin{aligned}uv^{-1}&=\zeta^{-1}\\wv^{-1}&=\eta\zeta^{-1}\end{aligned}\right.
\]
```

### Indices and exponents containing i or j

- L8: `p_i`, `p_i(s)=a_i`, `E=E_s\simeq E_{a_i}`, `_s\simeq E_{a_i`.

- L20: `gamma\simeq E_{p_i(\gamma)}`, `ma\simeq E_{p_i`.

- L47: `_3=0}\qquad p_i`, `ad p_i^{-1}(a_i`.

- L58: `\Gamma_i`, `\Gamma_i=p_i`, `nsure{-1}}\{a_i`.

- L60: `mma}&=\bigcap_i`, `&=\bigcap_i p_i`, `_i p_i^{-1}(P_i`, `^{-1}(P_i-\{a_i`.

- L61: `bigcup \Gamma_i`.

## Scan 117

Second reading, UTC: 2026-11-18T09:33:12Z to 2026-11-18T09:35:13Z.

### Before reopening the transcription

No sustained prose. “int” occurs in the bracket following the struck preliminary “int(α…)”. Capitals in the first display look like A₁ in places and like a₁ in others; the heavily retraced subscript after the first alpha has a low straight foot. In the top fork the right diagonal points back towards Γ. “ab=c” below the first normalization and “abc=1” at the right of the other version are distinct. All three of φ′(1), ψ′(1), χ′(1) use primes. There is a little isolated φ under the closing equality. In the three-column rewriting under abc each label is separated by two short vertical lines; the product of three parenthesised factors has a long underline beneath the internal factors only.

### Ink, corrections, lettering and margins

The second factor of the primed implication is forked psi, with no closed oval as in the preceding phi. Rechecked the third subscript of a on the first equality and retained alternatives to the numeral. All lowered coordinates of g, a and α in the top computation are numerals; no alphabetic i/j index. In the diagram one downstroke has a previous φ under the new label. The lower source object has an overdrawn subscript. Re-examined ab, aφ, the trial with xyz=1, the start of the bracket formula, the extra χ′ before the repeated equality and the term at the right before abc; these are crossed. The little old letters directly under the equalities for φ(1), ψ(1) were darkened and are now marked. The superscript marks in the three-column array remain variously curved or wedge-like. The separator after z is an ordinary closing parenthesis. There is one φ on the left after the string of equalities, and three ordinary u's in the row above the final τ's.

### Changes

```text
\unsure{\varphi{}'(y)|\psi{}'(y)} -> \psi{}'(y)
```

```text
ab\unsure{c|e}= -> ab\unsure{c|e|\in}=
```

```text
t{\beta{}\gamma{}^{-1}}{\Vert} -> t{\deleted{\unsure{\beta{}}}\beta{}\gamma{}^{-1}}{\Vert}
```

```text
t{\gamma{}\alpha{}^{-1}}{|} -> t{\deleted{\unsure{\alpha{}}}\gamma{}\alpha{}^{-1}}{|}
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\[
\begin{aligned}
 g_2(\alpha_2a_1\alpha_3^{-1})g_3^{-1}&=\alpha_2a_{\unsure{2|1}}\alpha_3^{-1}\\
 (\alpha_2^{-1}g_2\alpha_2)a_1(\alpha_3^{-1}g_3\alpha_3)^{-1}&=a_1\\
 \alpha_3^{-1}g_3\alpha_3&=\widetilde a_1(\alpha_2^{-1}g_2\alpha_2)\\
 \deleted{\operatorname{int}(\alpha_2}g_3&=[\operatorname{int}(\alpha_3)\,\widetilde a_1\,\operatorname{int}(\alpha_2)^{-1}](g_2)
\end{aligned}
\]
```

L10

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.65em,row sep=.6em]
 \&P_1\&\\
 \&\Gamma\arrow[u]\arrow[dl,dash]\&\\
 P_2\&\&P_3\arrow[ul]
\end{tikzcd}}
```

L15

```tex
\[
 P_2\times P_3\ \text{---}\ P_1\quad\deleted{\unsure{\times}}
\]
```

L18

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.4em,row sep=1.8em]
 G\arrow[d,"\varphi"']\&{}\times\&G\arrow[d,"\deleted{\unsure{\varphi}}\,\psi"]\arrow[r]\&G\arrow[d,"\chi"']\ \unsure{y}\\
 G_{\deleted{\unsure{1}}}\&{}\times\&G\arrow[r,dash]\&G
\end{tikzcd}}
```

L22

```tex
\[
\begin{aligned}
 \varphi(x)\psi(y)&=\chi(xy).\\
 \varphi(1)=a,\quad \psi(1)&=b,\quad \chi(1)=c\\
 ab&=c
\end{aligned}
\]
```

L29

```tex
\[
 \deleted{ab}\qquad\deleted{a\varphi(\unsure{x})}\qquad
 \begin{aligned}
 &\deleted{a\varphi}\qquad \varphi(x)\psi(\unsure{x}\\
 &\deleted{\unsure{\sigma(x)\varphi(x)}}\quad \deleted{xyz=1\Rightarrow}\\
 &\unsure{\tau.}\ \varphi(\underline{x})\psi(y)\chi(z)=1\\
 &\varphi(1)\psi(1)\chi(1)=\unsure{1|d}\\
 &\underset{\deleted{\unsure{\beta}}\beta\gamma^{-1}}{\Vert}\qquad\underset{\deleted{\unsure{\alpha}}\gamma\alpha^{-1}}{|}\qquad \alpha\beta^{-1}
 \end{aligned}
\]
```

L39

```tex
\[
\begin{aligned}
 &\varphi'(1)=1,\quad \psi'(1)=1,\quad \chi'(1)=1\\
 &xyz=1\Rightarrow \varphi'(x)\psi'(y)\chi'(z)=1\\
 &yz=1\Rightarrow \psi'(y)\chi'(z)=1\\
 &\chi'(z)=\psi'(y)^{-1}\\
 &\chi'(y^{-1})=\psi'(y)^{-1}\\
 &\psi'(y)=\chi'(y^{-1})^{-1}\\
 &\deleted{\unsure{\chi'}}\quad \varphi'=\psi'=\chi'\\
 &\varphi
\end{aligned}
\qquad
\begin{aligned}
 &abc=1\\
 &a=\beta\gamma^{-1}\quad b=\gamma\alpha^{-1}\\
 &\deleted{\beta\gamma^{-1}b}\quad ab\unsure{c|e|\in}=\beta\alpha^{-1}c
\end{aligned}
\]
```

L57

```tex
\[
 \deleted{\unsure{\operatorname{int}\beta\,\tau_\alpha}}
\]
```

L60

```tex
\[
 \begin{array}{c|c|c}
 \tau_{\beta}^{-1}\varphi\tau_{\gamma}^{\unsure{d|*}}&
 \tau_{\gamma^{-1}}\psi\tau_{\alpha}^{\unsure{d|*}}&
 \tau_{\alpha^{\unsure{-1}}}^{\unsure{G|g}}\chi\tau_{\beta}^{\unsure{d|1}}\\
 \Vert&\Vert&\Vert\\ \varphi'&\psi'&\chi'
 \end{array}
\]
```

L68

```tex
\[
 (\beta^{-1}\varphi(x)\,\underline{\gamma)(\gamma^{-1}\psi(y)\alpha)(\alpha^{-1}\chi(z)}\,\beta)=1
\]
```

L71

```tex
\[
 \begin{gathered}
 (u\times u\times u)\\
 (\tau_\beta u{\tau'_\gamma}^{-1},\tau_\gamma u{\tau'_\alpha}^{-1},\tau_\alpha u{\tau'_\beta}^{-1})
 \end{gathered}
\]
```

### Indices and exponents containing i or j

No alphabetic i or j appears in a subscript or superscript in the adopted reading.

## Scan 118

Second reading, UTC: 2026-11-18T09:34:42Z to 2026-11-18T09:37:12Z.

### Before reopening the transcription

“12 arêtes”, twice; acute or circumflex over the vowel of arêtes faint. “liés à”, “lié”, “lié à”, “et”, “ici … ?”, “i.e.” on the other orientation. Each system in the right column begins afresh. The marks after several numbers 1,2,3,4 are primes, not commas, and the comma often comes immediately after the prime. The boxed α₁/β₁ pair and α₁/γ₄ are separated. Lower left β double prime, a single dark crossed α, and the little w is above an unfinished open path. Along the right margin a₁∧a₂∧a₃=1. At the foot the arrows on the two g–a relations point down in the orientation of those relations; a question mark is next to g₁a₃=a₃g₂.

### Ink, corrections, lettering and margins

Followed the large diagonal through the four sets of arms and the written edge lists, then inspected the point labels in the lower-left fork. Left tips have α, right tips β, top tips γ; plain and primed partners are placed individually at the two corners of each lobe. The outer b₃ brace has no visible letters on the incident tips. The first table of neighbours has one exceptional prime in each of its first three rows; the fourth row repeats primes on its first three β's. The indexed i's in the two incidence rules have dots and no tails. At the outer edge, after rotating, letters 2 and 3 in the short wedge product resemble x more than a; the shallow bracket below them has upturned ends. The narrow box has a separate left-pointing arrow below. The two diagonals through the second twelve-edge list and the smaller contour are distinct. In the group calculation the mark after the last right parenthesis is a raised touch, not a full exponent 1. The whole last set of equalities has a separate half-turn orientation; the query is left of, not below, the double arrow. The circled and overwritten b₁ and a₃ at the foot remain uncertain. The right margin includes a contracted product on a different baseline; the G subscripts were read in that orientation.

### Changes

```text
a_1\wedge\underline{a_2\wedge a_3}=1 -> a_1\wedge\underbrace{\unsure{x_2|a_2}\wedge\unsure{x_3|a_3}}=1
```

```text
\quad\boxed{\alpha{}_1\text{ lié à }\gamma{}'_4} -> \quad\underset{\longleftarrow}{\boxed{\alpha{}_1\text{ lié à }\gamma{}'_4}}
```

```text
&\text{lié} -> \alpha{}_1&\text{lié}
```

```text
\widetilde a_1(\alpha{}_2)^{\unsure{1}} -> \widetilde a_1(\alpha{}_2)\unsure{'|,}
```

```text
\underset{?}{\Downarrow}\quad -> ?\ \Downarrow\quad
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,execute at end picture={
 \begin{scope}[x=.012cm,y=-.012cm,every node/.style={font=\scriptsize,inner sep=.5pt}]
 \coordinate (u) at (327,380); \coordinate (v) at (497,387); \coordinate (w) at (410,265);
 \draw (u)--(w)--(v)--cycle;
 \node[below right] at (u) {$u$};\node[below left] at (v) {$v$};\node[right] at (w) {$w$};
 \draw (u)--(87,314)--(79,354)--cycle (u)--(86,394)--(95,437)--cycle
       (u)--(145,501)--(166,532)--cycle (u)--(217,549)--(258,567)--cycle;
 \draw (v)--(679,311)--(677,352)--cycle (v)--(667,420)--(657,447)--cycle
       (v)--(657,504)--(635,528)--cycle (v)--(549,549)--(520,560)--cycle;
 \draw (w)--(264,168)--(290,133)--cycle (w)--(329,120)--(347,100)--cycle
       (w)--(409,100)--(445,101)--cycle (w)--(554,131)--(574,151)--cycle;
 \node[left] at (81,310) {$\alpha'_4$};\node[left] at (78,353) {$\alpha_4$};
 \node[left] at (89,391) {$\alpha'_3$};\node[left] at (94,435) {$\alpha_3$};
 \node[left] at (145,498) {$\alpha'_{\unsure{2}}$};\node[below] at (159,532) {$\alpha_2$};
 \node[left] at (217,553) {$\alpha'_1$};\node[right] at (252,570) {$\alpha_1$};
 \node at (36,332) {$a_4\big\{$};\node at (39,422) {$a_3\big\{$};
 \node at (91,551) {$a_2\big\{$};\node[below] at (218,584) {$\underbrace{\hspace{2em}}_{a_1}$};
 \node[right] at (677,311) {$\beta_1$};\node[right] at (677,347) {$\beta'_1$};
 \node[right] at (667,416) {$\beta_2$};\node[right] at (657,444) {$\beta'_2$};
 \node at (756,335) {$\big\}b_1$};\node at (770,439) {$\big\}b_2$};\node at (720,548) {$\big\}b_3$};
 \node[below] at (511,560) {$\unsure{\beta'_4|\beta'_3}$};\node[right] at (546,551) {$\unsure{\beta_4|\beta_3}$};
 \node[below] at (572,589) {$\underbrace{\hspace{2em}}_{b_4}$};
 \node[left] at (265,167) {$\gamma_1$};\node[left] at (289,131) {$\gamma'_1$};
 \node[above] at (324,121) {$\gamma_2$};\node[above] at (351,100) {$\gamma'_2$};
 \node[above] at (407,99) {$\gamma_3$};\node[above] at (455,102) {$\gamma'_3$};
 \node[above] at (556,129) {$\deleted{\unsure{\alpha}}\gamma_4$};
 \node[right] at (574,154) {$\gamma'_4$};
 \node[rotate=45] at (194,123) {$c_1\big\{$};
 \node at (337,44) {$\overbrace{\hspace{2em}}^{c_2}$};
 \node at (443,29) {$\overbrace{\hspace{2em}}^{c_3}$};\node at (681,94) {$\big\}c_4$};
 \draw[thin] (128,66)--(278,230)--(505,579);
 \end{scope}}]\phantom{.}\end{tikzcd}}
```

L34

```tex
\[
 12\ \text{arêtes}\ \left\{\begin{array}{lll}
 \alpha_1,\alpha_2,\alpha_3,\alpha_4&\text{\unsure{liés|liées} à}&\beta_4\\
 \beta_1,\beta_2,\beta_3,\beta_4&\text{-------}&\gamma_4\\
 \gamma_1,\gamma_2,\gamma_3,\gamma_4&\text{-------}&\alpha_4
 \end{array}\right.
\]
```

L41

```tex
\[
 \deleted{12\ \text{arêtes}\ \left\{\begin{array}{lll}
 \alpha_i&\text{lié à}&\alpha'_i\\\beta_i&\text{lié à}&\beta'_i\\\gamma_i&\text{lié à}&\gamma'_i
 \end{array}\right.\quad 1\le i\le\unsure{4|7}}
\]
```

L46

```tex
\[
 12\left\{\begin{array}{ll}
 \alpha'_i\ \text{liés à}&\beta'_4\\ \beta'_i\ \text{------}&\gamma'_4\\ \gamma'_i\ \text{------}&\alpha'_4
 \end{array}\right.
\]
```

L52

```tex
\(a_1\wedge\underbrace{\unsure{x_2|a_2}\wedge\unsure{x_3|a_3}}=1\)
```

L53

```tex
\[
 \left\{\begin{array}{lll}
 \alpha_1&\text{lié à}&\beta'_1,\beta_2,\beta_3,\beta_4\\
 \alpha_2&\text{------}&\beta_1,\beta'_2,\beta_3,\beta_4\\
 \alpha_3&\text{------}&\beta_1,\beta_2,\beta'_3,\beta_4\\
 \alpha_4&\text{------}&\beta'_1,\beta'_2,\beta'_3,\beta_4
 \end{array}\right.
 \quad
 \begin{gathered}\alpha'_1\ \text{lié à}\ \beta_1,\beta'_2,\beta'_3,\beta'_4\\\text{----}\end{gathered}
\]
```

L64

```tex
\({}_{G_2}P_1\underset{G_3}{\wedge}(\unsure{U}P_2\underset{G_3}{\wedge}P_3)_{G_2}\)
```

L65

```tex
\[
 \boxed{\begin{aligned}\alpha_1&\text{ lié à }\beta'_1\\ \alpha_{\unsure{1}}&\text{ lié à }\beta_2\end{aligned}}
 \quad\underset{\longleftarrow}{\boxed{\alpha_1\text{ lié à }\gamma'_4}}
 \quad
 \begin{aligned}
 \alpha_{\unsure{3|1}}&\text{ lié à }\deleted{\unsure{\gamma}}\beta_4\text{ et }\gamma'_4\\
 \beta_1&\text{ lié à }\gamma_4\text{ et }\beta'_4\\
 (\alpha_1&\text{ lié à }\beta_1)\Rightarrow\\
 \alpha_1&\text{lié}
 \end{aligned}
\]
```

L76

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.8em,column sep=.6em]
 \&\&w\&\&\\
 \&u\arrow[ur]\arrow[rr,dash]\arrow[dl,dash]\arrow[d,dash]\&\&v\arrow[ul,dash]\arrow[d,dash]\arrow[dr,dash]\arrow[drr,dash]\&\&\\
 \unsure{\alpha|v}\&\unsure{\alpha'}\&\&\beta\&\beta'\&\beta''\\
 {\Vert}\&{\Vert}\&\&{\Vert}\&{\Vert}\&\\
 \unsure{\alpha_1}\&\alpha'_2\&\&\beta'_1\&\beta_2\&
\end{tikzcd}}
```

L83

```tex
\[
 \left\{\begin{array}{lll}
 \alpha_1&\beta'_1,&\gamma'_4\\\alpha_1,&\beta_2,&\gamma_{\unsure{2|3}}\\
 \alpha'_2,&\beta'_1,&\gamma'_3\\\alpha'_2,&\beta_2,&\gamma_4
 \end{array}\right.
\]
```

L90

```tex
\[
\begin{aligned}
 &\deleted{g_2a_1g_3^{-1}=1}\\
 &g_2(\alpha_2a_1\alpha_3^{-1})g_3^{-1}=\alpha_2a_1\alpha_3\\
 &(g_2\alpha_2)a_1(\deleted{\unsure{\alpha}}g_3\alpha_3)^{-1}=\alpha_2a_1\alpha_3\\
 &g_3\alpha_3=\widetilde a_1(g_2\alpha_2)\\
 &\widetilde a_1(g_2)\widetilde a_1(\alpha_2)\unsure{'|,}=g_3\alpha_3\\
 &g_3=\\
 &\widetilde A_1(g_2)\alpha_3=\widetilde a_1(g_2)\deleted{\unsure{\alpha}}\widetilde a_1(\alpha_2)\\
 &\widetilde A_1(g_2)=\widetilde a_1(g_2)\widetilde a_1(\alpha_2)\alpha_3^{-1}
\end{aligned}
\]
```

L102

```tex
Drawing without alphabetic labels.
```

L109

```tex
\[
\begin{aligned}
 &g_2a_1=a_1g_3\deleted{=b_1}&&\text{i.e. }g_2a_1g_3^{-1}=a_1\\
 &g_3a_2=a_2g_1=b_2&&\text{i.e. }g_3a_2g_1^{-1}=a_2\\
 ?\ \Downarrow\quad&g_1a_3=a_3g_2&&a_1,a_2,
\end{aligned}
\]
```

L116

```tex
\[
 \underbrace{(g_1,g_2,g_3)\underbrace{(a_1,a_2,a_3)}_{\in \Gamma}}_{\in \Gamma}
       =(a_1,a_2,\unsure{a_3|a'_3})
\]
```

### Indices and exponents containing i or j

- L43: `\alpha_i`, `ié à}&\alpha'_i`, `pha'_i\\\beta_i`, `lié à}&\beta'_i`, `ta'_i\\\gamma_i`, `ié à}&\gamma'_i`.

- L48: `\alpha'_i`, `a'_4\\ \beta'_i`, `'_4\\ \gamma'_i`.

## Scan 119

Second reading, UTC: 2026-11-18T09:37:13Z to 2026-11-18T09:38:17Z.

### Before reopening the transcription

“Aut(G)” and the earlier struck “u∈Aut G” are the only words. Small strokes after u, γ, ψ in the upper-left formula are not all at the same height: some are primes, others are the −1 of an inverse. The first of the three primed maps on the right is φ, the second has a struck and rewritten ψ, the third is χ. The little terminal at the right after their product looks round, like 0. In the middle a completely cancelled tuple starts with (u,β,γ…; the second occurrence of u(xγ⁻¹) on the right is crossed. Bottom expansions have two large, running brackets and a wavy continuation, then an inverse tuple that ends the page without an equals sign.

### Ink, corrections, lettering and margins

The rightmost χ on the line ending in 0 has a plainly separate prime; the high mark on ψ abuts the following parenthesis. Nothing to the right of the open 0 supplies a 1. Inspected the remaining top-row inverses independently, in particular the crossed superscript after γ in φ′. The arrowhead of the highest fork branch is much broader than the other two; the top u is written separately. Checked the overstruck middle tau subscript and the black superscript above the same branch. The product rule has only one closing parenthesis visible at its right edge. In the next line the separator at the right of the triple product is two dark dots with a very short bar. An entire quadruple and u(xγ⁻¹) above the fan are deleted, as is the old β/γ to the left of the expansion. The small strokes on the α's, β's, γ's, and u's in the associativity rows are primes, double primes, or raised −1; no index i/j is present. The big lower underbrace is connected to its own abbreviated product, ending in a wavy horizontal stroke.

### Changes

```text
)\psi{}(\unsure{b|y})\chi{}(\unsure{c|z})&=0 -> )\unsure{\psi{}'|\psi{}}(\unsure{b|y})\chi{}'(\unsure{c|z})&=0
```

```text
\mathbin{:}\bigl(uu'u'' -> \unsure{\mathbin{:}|=}\bigl(uu'u''
```

```text
\gamma{}u(\gamma{}'))\\ -> \gamma{}u(\gamma{}')\\
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L2

```tex
\[
\begin{aligned}
 &\deleted{u\in\operatorname{Aut}G}\\
 &\tau_\beta u\tau'_{\gamma^{-1}}\quad \tau_{\gamma'}u'\tau'_{\gamma'}{}^{-1}\\
 &\deleted{\beta u(x)\gamma^{-1}}\quad u'(x{\gamma'}^{-1})\\
 &\beta u(x\gamma^{-1})\\
 &\beta'u'(\deleted{\unsure{\gamma}}\beta u(x\gamma^{-1}){\gamma'}^{-1})\\
 &\beta'u'(\beta)\,\underline{u'u}(x)
\end{aligned}\qquad
\begin{aligned}
 \varphi(1)&=\beta\gamma^{-1}\\
 \varphi'(x)&=\beta^{-1}\varphi(x)\gamma^{\deleted{\unsure{-1}}}\\
 \deleted{\unsure{\varphi}}\psi'(x)&=\gamma^{-1}\psi(\unsure{z|x})\deleted{\unsure{\beta}}\alpha\\
 \chi'(x)&=\deleted{\unsure{\beta}}\alpha^{-1}\chi(x)\beta\\
 \varphi'(\unsure{a|x})\unsure{\psi'|\psi}(\unsure{b|y})\chi'(\unsure{c|z})&=0\\
 \varphi&=\beta u(x)\gamma^{-1}
\end{aligned}
\]
```

L20

```tex
\[
 \begin{gathered}
 \operatorname{Aut}(G)\\G\times G\\
 \deleted{(u,\beta,\gamma,\beta}\quad\deleted{u,\beta,}
 \end{gathered}
 \qquad \deleted{u(x\gamma^{-1})}
\]
```

L27

```tex
\[
 (u,\alpha,\beta,\gamma)(x,y,z)=
\]
```

L30

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.65em,column sep=1.5em]
 \&{\overset{u}{\tau_\beta}\tau'_{\deleted{\unsure{\alpha}}\gamma}u^{\deleted{\unsure{*}}}}\\
 {(u,\alpha,\beta,\gamma)}\arrow[ur]\arrow[r]\arrow[dr]\&{\tau_\gamma\tau'_{\deleted{\unsure{\beta}}\alpha}u}\\
 \&{\tau_{\unsure{\alpha|2}}\tau'_\beta u}
\end{tikzcd}}
```

L35

```tex
\[
 \begin{aligned}
 &(\tau_\beta\tau'_\gamma u)(\tau_{\beta'}\tau'_{\gamma'}u')\\
 &\beta u(x)\gamma^{-1}=x\\
 &\beta=\gamma
 \end{aligned}
\]
```

L42

```tex
\[
\begin{aligned}
 &\deleted{\unsure{\beta\gamma}}\beta u(\beta'u'(x){\gamma'}^{-1})\gamma^{-1}=\\
 &\hspace{2em}\beta u(\beta')uu'(x)\bigl(\gamma u(\gamma')\bigr)^{-1}\\
 &\hspace{18em}u(\alpha')=\alpha^{-1}\\
 &\hspace{18em}\alpha'=u^{-1}(\alpha^{-1})
\end{aligned}
\]
```

L50

```tex
\[
\begin{aligned}
 &(u,\alpha,\beta,\gamma)(u',\alpha',\beta',\gamma')=(uu',\alpha u(\alpha'),\beta u(\beta'),\gamma u(\gamma')\\
 &\bigl((u,\alpha,\beta,\gamma)\,(u',\alpha',\beta',\gamma')\bigr)(u'',\alpha'',\beta'',\gamma'')
 \unsure{\mathbin{:}|=}\bigl(uu'u'',\alpha u(\alpha')uu'(\alpha''),\text{---}\bigr)\\
 &\hspace{6em}\bigl(\underbrace{\hspace{6em}}_{u'u'',\,\alpha'u'(\alpha'')\,\text{---}}\bigr)
 \qquad\bigl(u\,u'u'',\,\alpha u(\alpha'u'(\alpha''))\\
 &(u,\alpha,\beta,\gamma)(u^{-1},u^{-1}(\alpha)^{-1},u^{-1}(\beta)^{-1},u^{-1}(\gamma^{-1})
\end{aligned}
\]
```

### Indices and exponents containing i or j

No alphabetic i or j appears in a subscript or superscript in the adopted reading.

## Scan 120

Second reading, UTC: 2026-11-18T09:38:18Z to 2026-11-18T09:39:27Z.

### Before reopening the transcription

The words are “diag”, then a small “antidi…” preceding an equals sign, “1-hom” or “1-hom(…”, “Tr p”. No continuous prose. At the right of the two ruled-off exclusions the group symbol after π₁ has the bars of Z. Star above C on a separate baseline. The underlined O in O(1) is different from the single round terminal 0; O(−2) is independently underlined. At writing foot the inequality is between ℝu and ℝa, ℝb. Two of the bodies of arrows on the sphere intersect at one point; a second, mostly blank horizontal shaft leaves the little projection. In the line under u⁺ u⁻ there is a literal query at the right. Five-line musical staves are horizontal throughout. Large corner-to-corner oblique strokes are separately drawn.

### Ink, corrections, lettering and margins

Read s3→s2→s1 with the writing upright. The vertical C*, P, S² sequence and the horizontal equality share the single centre object; their positions now follow that junction. The two π-index 1's are digits; no alphabetic i or j occurs as a lowered index. The first and second homotopy-group arguments have S¹ and the round C with a partly raised stroke. The E fork has F below and to the left of E. Both the upper and lower O's have a separate short underline at their left side. Near the top-left oval the ink pools obscure the older symbols completely in places; their positions are indicated in the drawn contour. The last sign in the u⁺ relation is a definite question mark; a crescent or an equals sign before it is less certain. Marks behind the diagram, the diagonal exclusions, the crossed projective-power string and the cancellation before u⁺ have been distinguished from the printed staves. Rechecked the loop crossings, the ticks of the small upper oval, the arrows on the large ellipses, the thickened meridian, 1/2/3 on the partitioned sphere, and the dotted open loop at the foot. The TikZ remains an approximation of these freehand drawings.

### Changes

```text
\end{tikzpicture}}
\[
\deleted{\unsure{P|p}} -> \fill (.66,-.44) ..controls(.4,-.09)and(.69,-.04)..(.83,-.31)..controls(1.05,-.24)and(1.14,-.6)..(1.33,-.58)..controls(1.5,-.85)and(1.09,-.95)..(.97,-.65)--cycle;
\foreach \x/\y/\r in {1.44/-.48/.08,1.84/-.65/.065,.95/-1.31/.17,1.17/-1.58/.11,1.39/-1.81/.2,1.5/-1.98/.14}{\fill (\x,\y) circle (\r);}
\end{tikzpicture}}
\[
\deleted{\unsure{P|p}}
```

```text
\[
  \deleted{S^2\times S^2-\mathrm{diag}-\unsure{\mathrm{antidiag}|\mathrm{antid}}\ }=
  \unsure{\mathbb P|P}
  \qquad (x,y)\quad \begin{array}{l}\deleted{\unsure{y}=x}\\ y=-x\end{array}
\]
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
 {}\&\unsure{\mathbb C|C}^{*}\arrow[d]\&\pi_1(S^1)=\mathbb Z\arrow[d,"2"']\\
 {}\&\unsure{\mathbb P|P}\arrow[d]\&\pi_1(C^1)=\mathbb Z\arrow[d]\\
 {}\&{}\&\pi_1(\unsure{\mathbb P|P})\arrow[d]\\
 S^1\arrow[r]\&S^2\&\pi_1(S^2)=0
\end{tikzcd}} -> \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.55em]
 {}\&{}\&\pi_1(S^1)=\mathbb Z\arrow[d,"2"']\\
 {}\&{\unsure{\mathbb C|C}}^{*}\arrow[d]\&\pi_1(C^{\unsure{*|1}})=\mathbb Z\arrow[d]\\
 {\deleted{S^2\times S^2-\mathrm{diag}-\unsure{\mathrm{antidiag}|\mathrm{antid}}} =}\&\unsure{\mathbb P|P}\arrow[d]\&\pi_1(\unsure{\mathbb P|P})\arrow[d]\\
 S^1\arrow[r]\&S^2\&\pi_1(S^2)=0
\end{tikzcd}}
\[
 (x,y)\qquad\begin{array}{l}\deleted{\unsure{y}=x}\\ y=-x\end{array}
\]
```

```text
X\times\&{}\& L\\
 F\arrow[ur,dash]\arrow[rr,"\sim"']\& E\arrow[ur]\arrow[dr]\&{}\\
 {}\&{}\& L' -> {}\&{}\& L\\
 X\times\&E\arrow[ur]\arrow[dr]\&{}\\
 F\arrow[ur,dash]\arrow[rr,"\sim"']\&{}\& L'
```

```text
\underline{1\text{-}\mathrm{hom}}\,(h,F) -> \underline{1\text{-}\mathrm{hom}}\,(\unsure{h|u},F)
```

```text
u-u^+=u^+\unsure{?} -> u-u^+\unsure{\in|=}u^+?
```

```text
\Gamma{} etc. (control-word terminator) -> \Gamma etc. (no empty nucleus before a following index)
```

### Formula ledger

L4

```tex
Drawing without alphabetic labels.
```

L15

```tex
\[
\deleted{\unsure{P|p}}\quad \Gamma\longrightarrow S^1
\]
```

L18

```tex
\[
 S^2\times S^2-\mathrm{diag}\qquad
 {\displaystyle S^2\times S^2/\mathord{\pm}1}\ \deleted{\unsure{-|/}}\Delta
\]
```

L22

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.55em]
 {}\&{}\&\pi_1(S^1)=\mathbb Z\arrow[d,"2"']\\
 {}\&{\unsure{\mathbb C|C}}^{*}\arrow[d]\&\pi_1(C^{\unsure{*|1}})=\mathbb Z\arrow[d]\\
 {\deleted{S^2\times S^2-\mathrm{diag}-\unsure{\mathrm{antidiag}|\mathrm{antid}}} =}\&\unsure{\mathbb P|P}\arrow[d]\&\pi_1(\unsure{\mathbb P|P})\arrow[d]\\
 S^1\arrow[r]\&S^2\&\pi_1(S^2)=0
\end{tikzcd}}
```

L28

```tex
\[
 (x,y)\qquad\begin{array}{l}\deleted{\unsure{y}=x}\\ y=-x\end{array}
\]
```

L31

```tex
Drawing labels: \unsure{\lambda(t)|\lambda(1)}, \unsure{u(t)|v(t)}, a, b, u_0(t), -a, x
```

L51

```tex
\[
 \unsure{\theta|\Theta}(t): S^1\longrightarrow S^2 \qquad
 \deleted{{\unsure{P|p}}^1\times P^1-P^1}
\]
```

L55

```tex
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small]
 {}\&{}\& L\\
 X\times\&E\arrow[ur]\arrow[dr]\&{}\\
 F\arrow[ur,dash]\arrow[rr,"\sim"']\&{}\& L'
\end{tikzcd}}
```

L60

```tex
\[
 \underline{1\text{-}\mathrm{hom}}\,(\unsure{h|u},F)\qquad E\simeq L\oplus L'
 \qquad \boxed{p^2=p\quad\mathrm{Tr}\,p=1}
\]
```

L64

```tex
\[
 0\longrightarrow F\longrightarrow E_p\longrightarrow\underline{\mathcal O}(1)\longrightarrow0
\]
```

L67

```tex
\[
 F\oplus\mathcal O(1)\simeq \unsure{\mathcal O|0}\qquad
 F\simeq\mathcal O(-1)\qquad \underline{\mathcal O}(-2)
\]
```

L71

```tex
Drawing labels: u^+\quad u^-, \\
```

L83

```tex
Drawing labels: 1, 2, 3, a, \mathbb R u\ne\mathbb R a,\mathbb R b
```

### Indices and exponents containing i or j

No alphabetic i or j appears in a subscript or superscript in the adopted reading.

## Cross-page notation reading

Two details from each sheet were compared together after the page-by-page readings. In 104 and 108 the Γ of the ternary relation has a straight top and downstroke, also seen in 110, 112–116 and 118. The ψ-shaped opening sign of 104 and the curving script targets of 109 have different outlines. The flags on Γ in 109 and 116 are independently visible and have different shapes. In 106 the heading E has a conspicuous lower stroke; the F of 114 has no lower arm and the extra vertical belongs to the field letter. The fibre letters E in 115–116 have long lower arms. On 120 the bowed capital next to the two vertical sequences is a different shape, and its alphabet remains doubtful.

On 110, 113 and 117, a wavy mark over a lower-case a stops over that letter; an upper prime next to it is separate. On 111 a short overbar changes the handwritten binary expression. It does not have the hooked corners of the spanning bar on the ordered pair in 115. The o-shaped origin letters of 112 can have dark caps; the small circles in the opposite torsors on 113 are unmistakably raised. Compared the numerals and primes with the labels at the tips of the graph in 118 and the table of maps on 119. Finally, in 120 a star on C and a numeral on S each attach to the upper right, unlike the 1 lowered on π. The smaller letter at the second C remains unresolved.

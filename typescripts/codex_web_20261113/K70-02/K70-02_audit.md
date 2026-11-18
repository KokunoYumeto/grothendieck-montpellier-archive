# Second reading audit

All times are actual UTC timestamps. Crop observations were saved before opening each corresponding page file for comparison. No OCR, external transcription, compilation or parallel reader was used.

## Scan 17
Start (UTC): 2026-11-17T21:05:53+00:00  
Independent crop notes saved (UTC): 2026-11-17T21:06:21+00:00  
End (UTC): 2026-11-17T21:07:00+00:00

### Independent words and accents from the crops
Crop-first words: ‘hyperplan’, ‘d’équation’, ‘n’est un hyperplan que si’, ‘i.e.’, ‘conséquence’, ‘en plus’, ‘conditions’, ‘exprimant’, ‘Sur un corps’, ‘comme’, ‘alors car ≠2’, ‘indépendantes’, ‘sous-variété linéaire’, ‘codim’, ‘Donc on doit avoir’. Accents visible in équation/équations, conséquence, indépendantes, variété, linéaire; the cancelled verbal middle remains weak.

### Independent visual observations
The upper coordinate formula, first fixed-point system and following paragraph are diagonally cancelled together. An exclamation below underlined swapped coordinates is visible. The four live H_i rows use i+2 to n+1; a small cancelled prefix precedes lambda_ii. The parenthetic bound begins with a blob more like 0 than 1. In the lower system the top coordinate-zero line is live, and three coefficient rows are struck. In the next paragraph a long cancellation crosses a parenthesis; the displayed count [n+1−(i+1)]+1=n−i+1 is above it. No independent margin note, script capital, or double striking. Lower corner archive number16.

### Comparison and changes
`1|0` at the lower bound -> `0|1` (the initial blob is closed). `Si l’on est sur un corps` -> a tentative cancelled `Si`, followed by `Sur un corps` (detail crop resolves the actually present words). `conséquences` -> `conséquence|conséquences` (terminal s not resolved).

### Detailed checks
Compared the entire cancelled coordinate formula, both H_i systems, the parenthetic sigma_i squared relation, the field argument, the lower system, count and concluding coefficient. In particular checked i−1/i+1/i+2, j in the range, n+1, square 2 and all inequality directions. The lower xi=xi+1 is live after a cancelled coefficient prefix; the upper three text blocks remain cancelled. The line through the equation-count paragraph is not applied to ‘indépendantes’. H is roman with a visible prime; Sigma/barred-Sigma remains unresolved at its first appearance. No handwritten material on type, no diagram or separate marginal note.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
\deleted{\sigma_i(x_1,\ldots,x_{n+1})=(x_1,\ldots,x_{i-1},\underset{!}{\underline{x_{i+1}}},x_i,\lambda_{i,i+2}x_{i+2},\lambda_{i,i+2}x_{i+3},\ldots,\lambda_{i,i+2}x_{n+1})}
```

Formula 2 (display):
```latex
\deleted{H_i:\left\{\begin{aligned}
x_i&=x_{i+1}\\
(\lambda_{i,i+2}-1)x_{i+2}&=\cdots=(\lambda_{i,i+2}-1)x_{n+1}=0
\end{aligned}\right.}
```

Formula 3 (inline):
```latex
H'_i
```

Formula 4 (inline):
```latex
x_i=x_{i+1}
```

Formula 5 (inline):
```latex
H_i\subset H'_i
```

Formula 6 (inline):
```latex
H_i
```

Formula 7 (inline):
```latex
H_i=H'_i
```

Formula 8 (inline):
```latex
(\lambda_{i,i+2}-1)x_{i+2}=\cdots=(\lambda_{i,i+2}-1)x_{n+1}=0
```

Formula 9 (inline):
```latex
x_i=x_{i+1}
```

Formula 10 (inline):
```latex
\lambda_{i,\unsure{i+1|i+2}}=1
```

Formula 11 (display):
```latex
\left\{\begin{aligned}
&\lambda_{i,1}(x_{i+2}+\cdots+x_{n+1})=\lambda_{i,2}(x_{i+2}+\cdots+x_{n+1})=\cdots\ \lambda_{i,i-1}(x_{i+2}+\cdots+x_{n+1})=0\\
&\deleted{\unsure{x_{i+1}}}\lambda_{i,i}(x_{i+2}+\cdots+x_{n+1})=x_i-x_{i+1}\\
&\lambda_{i,i+1}(x_{i+2}+\cdots+x_{n+1})=x_{i+1}-x_i\\
&(\lambda_{i,i+2}-1)x_{i+2}=\cdots=(\lambda_{i,i+2}-1)x_{n+1}=0
\end{aligned}\right.\tag*{$(H_i)$}
```

Formula 12 (inline):
```latex
\lambda_{i,j}
```

Formula 13 (inline):
```latex
\unsure{0|1}\leq j\leq i+2
```

Formula 14 (inline):
```latex
\sigma_i^2=\mathrm{id}\ \ldots
```

Formula 15 (inline):
```latex
\lambda_{i,i+2}\ne1
```

Formula 16 (inline):
```latex
\lambda_{i,i+2}^2=1
```

Formula 17 (inline):
```latex
\lambda_{i,i+2}=-1\ne1
```

Formula 18 (inline):
```latex
\ne2
```

Formula 19 (inline):
```latex
H_i
```

Formula 20 (display):
```latex
\left\{\begin{aligned}
&x_{i+2}=\cdots=x_{n+1}=0\\
&\deleted{\lambda_{i,1}\unsure{\overline{\Sigma}_i|\Sigma_i}(x)=\cdots=\lambda_{i,i-1}\overline{\Sigma}_i(x)=0}\quad\deleted{:\ \overline{\Sigma}_i(x)=x_{i+2}+\cdots+x_{n+1}}\\
&\deleted{\lambda_{i,i}\overline{\Sigma}_i(x)=}\ x_i=x_{i+1}\ \unsure{\}}\\
&\deleted{\lambda_{i,i+1}\overline{\Sigma}_i(x)=x_{i+1}-x_i}
\end{aligned}\right.
```

Formula 21 (inline):
```latex
[n+1-(i+1)]+1=n-i+1
```

Formula 22 (inline):
```latex
i\leq n+1
```

Formula 23 (inline):
```latex
n+1-i
```

Formula 24 (inline):
```latex
i\leq n-1
```

Formula 25 (inline):
```latex
\geq2
```

Formula 26 (inline):
```latex
\lambda_{i,i+2}=1
```

Formula 27 (inline):
```latex
H_i
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 1-9: block cancelled by long diagonal strokes:
```latex
\sigma_i(x_1,\ldots,x_{n+1})=(x_1,\ldots,x_{i-1},\underset{!}{\underline{x_{i+1}}},x_i,\lambda_{i,i+2}x_{i+2},\lambda_{i,i+2}x_{i+3},\ldots,\lambda_{i,i+2}x_{n+1})
```

`\deleted` — lines 1-9: block cancelled by long diagonal strokes:
```latex
H_i:\left\{\begin{aligned}
x_i&=x_{i+1}\\
(\lambda_{i,i+2}-1)x_{i+2}&=\cdots=(\lambda_{i,i+2}-1)x_{n+1}=0
\end{aligned}\right.
```

`\deleted` — lines 1-9: block cancelled by long diagonal strokes:
```latex
Si $H'_i$ est l'\unsure{hyperplan} d'équation $x_i=x_{i+1}$, on a $H_i\subset H'_i$, donc $H_i$ n'est un \unsure{hyperplan} que si $H_i=H'_i$, i.e. les équations $(\lambda_{i,i+2}-1)x_{i+2}=\cdots=(\lambda_{i,i+2}-1)x_{n+1}=0$ sont \unsure{conséquence|conséquences} de $x_i=x_{i+1}$, ce qui bien sûr n'est le cas que si $\lambda_{i,\unsure{i+1|i+2}}=1$.
```

`\deleted` — lines 10-13:
```latex
\unsure{x_{i+1}}
```

`\deleted` — lines 14-16:
```latex
\unsure{disant que}
```

`\deleted` — lines 17-19:
```latex
\lambda_{i,1}\unsure{\overline{\Sigma}_i|\Sigma_i}(x)=\cdots=\lambda_{i,i-1}\overline{\Sigma}_i(x)=0
```

`\deleted` — lines 17-19:
```latex
:\ \overline{\Sigma}_i(x)=x_{i+2}+\cdots+x_{n+1}
```

`\deleted` — lines 17-19:
```latex
\lambda_{i,i}\overline{\Sigma}_i(x)=
```

`\deleted` — lines 17-19:
```latex
\lambda_{i,i+1}\overline{\Sigma}_i(x)=x_{i+1}-x_i
```

`\deleted` — lines 24-29:
```latex
\unsure{Si} $i\leq n+1$, les premières équations \unsure{étant} $n+1-i$
```
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _{i-1} ; _{i+1} ; _i ; _{i,i+2} ; _{i+2} ; _{i,i+2} ; _{i+3} ; _{i,i+2} ; _i ; _i ; _{i+1} ; _{i,i+2} ; _{i+2} ; _{i,i+2} ; _i ; _i ; _{i+1} ; _i ; _i ; _i ; _i ; _i ; _{i,i+2} ; _{i+2} ; _{i,i+2} ; _i ; _{i+1} ; _{i,1} ; _{i+2} ; _{i,2} ; _{i+2} ; _{i,i-1} ; _{i+2} ; _{i+1} ; _{i,i} ; _{i+2} ; _i ; _{i+1} ; _{i,i+1} ; _{i+2} ; _{i+1} ; _i ; _{i,i+2} ; _{i+2} ; _{i,i+2} ; _i ; _{i,j} ; _i ; _{i,i+2} ; _{i,i+2} ; _{i,i+2} ; _i ; _{i+2} ; _{i,1} ; _i ; _i ; _{i,i-1} ; _i ; _i ; _{i+2} ; _{i,i} ; _i ; _i ; _{i+1} ; _{i,i+1} ; _i ; _{i+1} ; _i ; _{i,i+2} ; _i
```

## Scan 18
Start (UTC): 2026-11-17T21:07:01+00:00  
Independent crop notes saved (UTC): 2026-11-17T21:07:24+00:00  
End (UTC): 2026-11-17T21:08:24+00:00

### Independent words and accents from the crops
Crop-first words/accents: ‘Si donc les’, ‘ne sont pas nuls’, ‘alors ces équations se réduisent’, ‘Ce sont deux équations linéaires indépendantes’, ‘donc H_i serait de codim 2’, ‘pas un hyperplan’, ‘On doit donc’, ‘les équations se réduisent alors’, ‘Les relations exprimant’, ‘se réduisent ici à’, ‘de sorte qu’il reste un seul paramètre’, ‘et on trouve’. Acute strokes in équations, réduisent, indépendantes, paramètre; the cancelled attempted sentence is ‘Si on … / On avait …, ces équations’ with heavy strike-through.

### Independent visual observations
First lambda range appears 1≤j≤i−1. Capital Sigma has a thick doubled-looking upper stroke but no stable separation from its body, so bar/no-bar remains a candidate issue. The two reduced equations have Sigma_i(x)=0 and xi−xi+1=0. A cancelled line precedes ‘Les relations’. The matrix has left group sizes i−1,2,n−i,1; top identity block, central 0/1 swap block, two rows −(1+alpha_i) and +(1+alpha_i), a lower identity pattern and bottom zeros with last1. Several overwritten entries and a crossed initial sigma_i at the matrix top. No script or double-struck capitals; no verbal margin note.

### Comparison and changes
`On a` -> `On veut|On doit`: enlarged crop shows a longer word ending in t, with veut favoured by the first curved strokes. Restored the visible inner parentheses around the 2×2 exchange block of the large matrix; no matrix coefficient changed.

### Detailed checks
Read all six displayed systems/relations and every inline lambda range and involution relation, then the matrix from its top-left identity entries to its bottom-right1. Checked lambda_{i,j} with j descending, i−1 and i+1 distinct; retained missing i on several Sigma occurrences. Matrix cancellations at the first attempted sigma, the two coefficient prefixes, the lower diagonal and right zeros remain marked. The prose just above the matrix is live despite a horizontal fold. The two cancelled prose starts remain cancelled. No separate margin prose or handwritten additions to type. E/F and Greek/script confusion does not arise; H is roman, alpha has its own loop, Sigma’s extra upper stroke remains unresolved.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
\left\{\begin{aligned}
\lambda_{i,1}\unsure{\overline{\Sigma}_i|\Sigma_i}(x)&=\cdots=\lambda_{i,i-1}\overline{\Sigma}_i(x)=0\\
\lambda_{i,i}\overline{\Sigma}(x)&=x_i-x_{i+1}\\
\lambda_{i,i+1}\overline{\Sigma}(x)&=x_{i+1}-x_i
\end{aligned}\right.
\qquad :\quad\overline{\Sigma}(x)=x_{i+2}+\cdots+x_{n+1}
```

Formula 2 (inline):
```latex
\lambda_{i,j}
```

Formula 3 (inline):
```latex
1\leq j\leq i-1
```

Formula 4 (display):
```latex
\left\{\begin{aligned}
\overline{\Sigma}_i(x)&=0\\
x_i-x_{i+1}&=0
\end{aligned}\right.
```

Formula 5 (inline):
```latex
H_i
```

Formula 6 (inline):
```latex
2
```

Formula 7 (display):
```latex
\lambda_{i,1}=\cdots=\lambda_{i,i-1}=0
```

Formula 8 (display):
```latex
\lambda_{i,i}\overline{\Sigma}_i(x)=-\lambda_{i,i+1}\overline{\Sigma}_i(x)=x_i-x_{i+1}
```

Formula 9 (inline):
```latex
\lambda_{i,i}=\lambda_{i,i+1}=0
```

Formula 10 (inline):
```latex
\sigma_i^2=\mathrm{id}
```

Formula 11 (inline):
```latex
\lambda_{i,i}+\lambda_{i,i+1}=0
```

Formula 12 (inline):
```latex
\lambda_{i,i+1}=1+\alpha_i
```

Formula 13 (display):
```latex
\left\{\begin{aligned}
&\deleted{\sigma_i=}\\[-1.5ex]
\sigma_i={}&
\begin{array}{c@{\,}l}
\begin{array}{r}
\left.\vphantom{\begin{matrix}1\\1\\1\end{matrix}}\right\}\unsure{i-1}\\
\left.\vphantom{\begin{matrix}1\\1\end{matrix}}\right\}2\\
\left.\vphantom{\begin{matrix}1\\1\\1\\1\end{matrix}}\right\}\deleted{\unsure{n-i}}\\
1
\end{array}
&\left(\begin{array}{cccccccccc}
1&&0&&&&&&&0\\
&1&&&&&0&&&0\\
0&&\ddots&&&&&&&\vdots\\
&&&1&&&&&&\\
&&&&\multicolumn{2}{c}{\left(\begin{matrix}0&1\\1&0\end{matrix}\right)}&\begin{matrix}-(1+\alpha_i)\deleted{\unsure{x}}\\(1+\alpha_i)\deleted{\unsure{x}}\end{matrix}&\begin{matrix}-(1+\alpha_i)\\(1+\alpha_i)\end{matrix}&\begin{matrix}\cdots\;-(1+\alpha_i)\\\cdots\;(1+\alpha_i)\end{matrix}&\begin{matrix}0\\0\end{matrix}\\
&&&&&&\deleted{\unsure{1}}&&&\deleted{\unsure{0}}\\
&&&&&&1&&0&0\\
&&&&&&&1&\deleted{\unsure{\cdots}}&\unsure{0}\\
&&&&&&&&\ddots\ \deleted{\unsure{0}}&\vdots\\
&&&&&&&&1&0\\
0&0&\cdots&0&0&0&0&\cdots&0&1
\end{array}\right)
\end{array}
\end{aligned}\right.
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 12-13:
```latex
\unsure{se}
```

`\deleted` — lines 14-18:
```latex
Si on a
```

`\deleted` — lines 14-18:
```latex
\unsure{On avait} $\lambda_{i,i}=\lambda_{i,i+1}=0$, ces équations
```

`\deleted` — bottom matrix:
```latex
\sigma_i=
```

`\deleted` — bottom matrix:
```latex
\unsure{n-i}
```

`\deleted` — bottom matrix:
```latex
\unsure{x}
```

`\deleted` — bottom matrix:
```latex
\unsure{x}
```

`\deleted` — bottom matrix:
```latex
\unsure{1}
```

`\deleted` — bottom matrix:
```latex
\unsure{0}
```

`\deleted` — bottom matrix:
```latex
\unsure{\cdots}
```

`\deleted` — bottom matrix:
```latex
\unsure{0}
```
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_{i,1} ; _i ; _i ; _{i,i-1} ; _i ; _{i,i} ; _i ; _{i+1} ; _{i,i+1} ; _{i+1} ; _i ; _{i+2} ; _{i,j} ; _i ; _i ; _{i+1} ; _i ; _{i,1} ; _{i,i-1} ; _{i,i} ; _i ; _{i,i+1} ; _i ; _i ; _{i+1} ; _{i,i} ; _{i,i+1} ; _i ; _{i,i} ; _{i,i+1} ; _{i,i+1} ; _i ; _i ; _i ; _i ; _i ; _i ; _i ; _i ; _i
```

## Scan 19
Start (UTC): 2026-11-17T23:41:06+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:41:26+00:00  
End (UTC): 2026-11-17T23:42:13+00:00

### Independent words and accents from the crops
Crop-first words/accents: ‘Ces résultats marchent aussi sur tt anneau réduit.’ ‘Sur un anneau quelconque’ and an opening bracket; ‘il y a lieu’, ‘de faire’, ‘poser’, ‘nilpotent’; ‘en car rés. ≠2’; ‘Comme devant. Il reste: examinons ce qui se passe en car. rés. 2 (sur un anneau entier, 2 non unité), où on trouve’. Acute marks in résultats, réduit, rés., unité and où. The word under the first (2+nu) looks like ‘nilpotent’, but its ending is compressed. The cancelled verbal passage before car rés. is only partly resolved.

### Independent visual observations
Upper sigma_i formula and H_i equation share a brace; two last indices resemble n+2 while final unchanged coordinate is n+1. Lone cancelled mark above the formula. Middle system has nu=0, lambda_i1 through lambda_i,i−1=0 and a long relation with crossed nu terms; the next consequence line is entirely struck. Lower system has (2+nu) times each early lambda, lambda_ii+lambda_i,i+1=−nu lambda_ii=−nu lambda_i,i+1, nu²+2nu=0, and nu(2+nu)=0. The diagonal implication arrow points down-left to the final relations. Underbrace at bottom has −(2+nu)lambda_ii and a cancelled continuation. No blackboard or script capitals. nu/v remains a recurring ambiguous glyph.

### Comparison and changes
`inversible` beneath (2+nu) -> `nilpotent|inversible`; the short word has a raised middle stroke and compact ending, and the former reading was too definite about its letters. Changed its TeX positioning from a brace to an underline with a label, matching the flat source line. No other change.

### Detailed checks
Compared the top two-line coordinate tuple and H_i equation term by term, both relation systems, their crossed portions, the implication arrow and both bottom consequences. The n+2/n+1 alternatives remain in the two last sums; i+2/i+1 remains in the definition of lambda. Every i,j pairing and all exponent2 positions were checked. The final bracket visibly has lambda_i, with one lower i, while the underbrace has lambda_{i,i}; preserved this difference. The cancelled ‘faire’, cancelled relation introduction, nu terms and consequence line remain cancelled. The solitary nu after ‘deviennent’ is tentative. No handwritten addition on a typescript, no separate marginal prose, no script/blackboard capital. A large H with index i and ordinary lambda/sigma/alpha strokes are distinct.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (inline):
```latex
\unsure{\sigma}
```

Formula 2 (display):
```latex
\left\{\begin{aligned}
\sigma_i(x_1,\ldots,x_{n+1})={}&(x_1,\ldots,x_{i-1},x_{i+1}-(1+\alpha_i)(x_{i+2}+\cdots+x_{n+1}),x_i+(1+\alpha_i)(x_{i+2}+\cdots+x_{\unsure{n+2|n+1}}),\\
&\hspace{6em}x_{i+2},\ldots,x_{n+1})\\[2ex]
H_i:\quad &x_i-x_{i+1}+(1+\alpha_i)(x_{i+2}+\cdots+x_{\unsure{n+2|n+1}})=0
\end{aligned}\right.
```

Formula 3 (display):
```latex
\lambda_{i,\unsure{i+2|i+1}}=1+\unsure{\nu|v}\qquad \nu\ \text{nilpotent}
```

Formula 4 (inline):
```latex
\ne2
```

Formula 5 (inline):
```latex
\sigma_i^2=\mathrm{id}
```

Formula 6 (inline):
```latex
\nu
```

Formula 7 (display):
```latex
\left\{\begin{aligned}
&\inserted{\nu=0}\\[-.5ex]
&\lambda_{i,1}=\cdots=\lambda_{i,i-1}=0\\
&\lambda_{i,i}\deleted{\unsure{\nu}}+\lambda_{i,i+1}\deleted{+\nu\lambda_{i,i}}=\lambda_{i,i}+\lambda_{i,i+1}\deleted{+\nu\lambda_{i,i+1}}=0\\
&\deleted{\unsure{\nu^2+\nu}}
\end{aligned}\right.
```

Formula 8 (inline):
```latex
\lambda_{i,i}+\lambda_{i,i+1}=-\nu\lambda_{i,i}=-\nu(\lambda_{i,i+1})
```

Formula 9 (inline):
```latex
2
```

Formula 10 (inline):
```latex
2
```

Formula 11 (display):
```latex
\left\{\begin{aligned}
&\underset{\text{\unsure{nilpotent|inversible}}}{\underline{(2+\nu)}}\lambda_{i,1}=(2+\nu)\lambda_{i,2}\ \cdots=(2+\nu)\lambda_{i,i-1}=0\\
&\lambda_{i,i}+\lambda_{i,i+1}=-\nu\lambda_{i,i}=-\nu\lambda_{i,i+1}\quad\deleted{\unsure{\nu\lambda_i}}\\
&\deleted{\unsure{\nu}}\ \nu^2+2\nu=0\qquad\text{i.e.}\quad\nu(2+\nu)=0
\end{aligned}\right.
```

Formula 12 (display):
```latex
\begin{aligned}
\swarrow\quad&\\[-1ex]
\lambda_{i,i+1}&=-(1+\nu)\lambda_{i,i}\quad\deleted{\unsure{-\nu\lambda_{i,i}=}}\qquad
\nu\underbrace{[\lambda_{i,i+1}-\lambda_i]}_{-(2+\nu)\lambda_{i,i}\ \deleted{\unsure{\nu}}}=0
\end{aligned}
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — top cancellation and lines 1-3:
```latex
$\unsure{\sigma}$
```

`\deleted` — lines 4-7:
```latex
faire
```

`\deleted` — lines 8-12:
```latex
et les relations
```

`\deleted` — lines 8-12:
```latex
\unsure{\nu}
```

`\deleted` — lines 8-12:
```latex
+\nu\lambda_{i,i}
```

`\deleted` — lines 8-12:
```latex
+\nu\lambda_{i,i+1}
```

`\deleted` — lines 8-12:
```latex
\unsure{\nu^2+\nu}
```

`\deleted` — lines 8-12:
```latex
donc $\lambda_{i,i}+\lambda_{i,i+1}=-\nu\lambda_{i,i}=-\nu(\lambda_{i,i+1})$
```

`\deleted` — lines 13-16:
```latex
\unsure{et}
```

`\deleted` — lines 13-16:
```latex
\unsure{\nu\lambda_i}
```

`\deleted` — lines 13-16:
```latex
\unsure{\nu}
```

`\deleted` — bottom consequences; arrow from the system to the left equation:
```latex
\unsure{-\nu\lambda_{i,i}=}
```

`\deleted` — bottom consequences; arrow from the system to the left equation:
```latex
\unsure{\nu}
```

`\inserted` — lines 8-12:
```latex
\nu=0
```
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _{i-1} ; _{i+1} ; _i ; _{i+2} ; _i ; _i ; _{i+2} ; _{i+2} ; _i ; _i ; _{i+1} ; _i ; _{i+2} ; _i ; _{i,1} ; _{i,i-1} ; _{i,i} ; _{i,i+1} ; _{i,i} ; _{i,i} ; _{i,i+1} ; _{i,i+1} ; _{i,i} ; _{i,i+1} ; _{i,i} ; _{i,i+1} ; _{i,1} ; _{i,2} ; _{i,i-1} ; _{i,i} ; _{i,i+1} ; _{i,i} ; _{i,i+1} ; _i ; _{i,i+1} ; _{i,i} ; _{i,i} ; _{i,i+1} ; _i ; _{i,i}
```

## Scan 20
Start (UTC): 2026-11-17T23:42:13+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:42:46+00:00  
End (UTC): 2026-11-17T23:43:40+00:00

### Independent words and accents from the crops
Crop-first words: ‘Reprenons les équations de H_i. H_i est contenu dans l’hyperplan H_i′ d’équation’; ‘Si’ and a cancelled ‘on avait’; ‘H_i était un hyperpl.’; ‘on aurait’, ‘les autres équations’, ‘conséquence de la précédente’, ‘Ce n’est possible manifestement que si’, ‘OK…’. NB is underlined. ‘ne change que la première coordonnée’, ‘que la ième et (i+1)ième’, ‘Ceci implique’ (above a struck word), ‘que … commutent si’. Accents in équations, équation, précédente, première, coordonnée; the ordinals are abbreviated as on the page.

### Independent visual observations
Top system repeats three relations, then a detached closing bracket at the right; a small bent arrow is above. H_i prime is visible. The coefficient conclusions use i,1 through i,i−1; i,i plus i,i+1; and i,i+2. A double separator stroke follows OK. In the lower sigma0 sigma1 tuple two attempted x glyphs are crossed, and the coefficient of Sigma1 is crossed with an explicit replacement underneath: (1+alpha1+2alpha0+alpha0 alpha1). The expansion’s alpha0 term has its own parentheses and inner sum; the right edge is cut by the scan. The p-th iterate uses F_p and G_p, roman capitals, followed by unchanged x3 through xn+1. Final ‘Donc’ leads to an unfinished equivalence with =id inserted. No independent marginal prose or script capitals.

### Comparison and changes
`était un hyperplan` -> `était un hyperpl.` (doubt retained on the abbreviated ending). Removed the reconstructed xn+1 and closing parenthesis beyond the visible right edge of the first sigma0 expansion; only the visible trailing continuation mark is transcribed there. In G_p’s first coordinate argument, `x_1` -> `x_1|alpha_0`, because the overwritten loop supports both readings.

### Detailed checks
Checked each top relation and H_i/H_i′ occurrence, including the detached closing bracket and tiny top arrow. Checked the three inline lambda conclusions, sigma0/sigma_i NB, the i range and descending j in the commutation condition. In all four lines of the product calculation, read signs, alpha subscripts, parentheses and each Sigma1 separately. The first tuple’s cancelled x marks and the replaced coefficient remain at their exact positions. The replacement coefficient reads 1+alpha1+2alpha0+alpha0alpha1. Checked F_p/G_p arguments and superscript p against the edge enlargement; did not restore text wholly outside the image. The bottom equivalence is unfinished in the source, with =id inserted. The separator is a double horizontal stroke, not a deletion of the preceding text. Roman F and G are not script or double struck; first Sigma/barred-Sigma and nu/v on this page remain marked. No separate marginal note or handwritten addition on type.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
\unsure{\Downarrow}\quad
\left\{\begin{aligned}
(2+\unsure{\nu|v})\lambda_{i,1}&=\cdots=(2+\nu)\lambda_{i,i-1}=0\\
\lambda_{i,i+1}&=-(1+\nu)\lambda_{i,i}\\
\nu(2+\nu)&=0
\end{aligned}\right.\quad\biggr]
```

Formula 2 (inline):
```latex
H_i
```

Formula 3 (inline):
```latex
H_i
```

Formula 4 (inline):
```latex
H'_i
```

Formula 5 (display):
```latex
\lambda_{i,i}\unsure{\overline{\Sigma}_i|\Sigma_i}(x)=x_i-x_{i+1}
```

Formula 6 (inline):
```latex
H_i
```

Formula 7 (inline):
```latex
H_i=H'_i
```

Formula 8 (inline):
```latex
H_i
```

Formula 9 (inline):
```latex
\lambda_{i,1}=\cdots=\lambda_{i,i-1}=0
```

Formula 10 (inline):
```latex
\lambda_{i,i}+\lambda_{i,i+1}=0
```

Formula 11 (inline):
```latex
\lambda_{i,i+2}=1
```

Formula 12 (inline):
```latex
\ldots
```

Formula 13 (inline):
```latex
\sigma_0
```

Formula 14 (inline):
```latex
\sigma_i
```

Formula 15 (inline):
```latex
1\leq i\leq\unsure{n-1|n}
```

Formula 16 (inline):
```latex
i
```

Formula 17 (inline):
```latex
(i+1)
```

Formula 18 (inline):
```latex
\sigma_i
```

Formula 19 (inline):
```latex
\sigma_j
```

Formula 20 (inline):
```latex
j\geq i+2
```

Formula 21 (display):
```latex
\begin{aligned}
\sigma_0\sigma_1(\deleted{\unsure{x}}x_1,x_2,x_3,\deleted{\unsure{x}}\ldots,x_{n+1})
&=\sigma_0(x_2-(1+\alpha_1)\Sigma_1,x_1+(1+\alpha_1)\Sigma_1,x_3,\unsure{\ldots}\\
&=(1-x_2+(1+\alpha_1)\Sigma_1+\alpha_0\unsure{(}x_1+(1+\alpha_1)\Sigma_1+\Sigma_1),x_1+(1+\alpha_1)\unsure{\Sigma_1},\\
&\hspace{4em}x_3,\ldots,x_{n+1})\\
&\deleted{\unsure{\ne}}\\[-1.2ex]
&=(1+\alpha_0x_1-x_2+\deleted{\unsure{[(1+\alpha_0)(1+\alpha_1)+\alpha_0]}}\inserted{(1+\alpha_1+2\alpha_0+\alpha_0\alpha_1)}\Sigma_1,x_1+(1+\alpha_1)\Sigma_1,x_3,\unsure{\ldots,x_{n+1})}
\end{aligned}
```

Formula 22 (display):
```latex
\begin{aligned}
(\sigma_0\sigma_1)^p(x_1,x_2,\ldots,x_{n+1})={}&(F_p(\alpha_0,\alpha_1;x_1,\ldots,x_{n+1}),G_p(\alpha_0,\alpha_1;\unsure{x_1|\alpha_0},\ldots,\unsure{x_{n+1}}),\\
&\hspace{6em}x_3,\ldots,x_{n+1})
\end{aligned}
```

Formula 23 (inline):
```latex
(\sigma_0\sigma_1)^{\unsure{p}}\inserted{=\mathrm{id}}\Longleftrightarrow
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 7-11:
```latex
on avait
```

`\deleted` — lines 12-15:
```latex
\unsure{montre}
```

`\deleted` — lines 16-19: right ends reach the paper edge:
```latex
\unsure{x}
```

`\deleted` — lines 16-19: right ends reach the paper edge:
```latex
\unsure{x}
```

`\deleted` — lines 16-19: right ends reach the paper edge:
```latex
\unsure{\ne}
```

`\deleted` — lines 16-19: right ends reach the paper edge:
```latex
\unsure{[(1+\alpha_0)(1+\alpha_1)+\alpha_0]}
```

`\inserted` — lines 12-15:
```latex
implique que
```

`\inserted` — lines 16-19: right ends reach the paper edge:
```latex
(1+\alpha_1+2\alpha_0+\alpha_0\alpha_1)
```

`\inserted` — bottom line:
```latex
=\mathrm{id}
```
- `\margin`: none.
- `\handwritten`: none.

`\uline` — lines 12-15:
```latex
NB
```
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_{i,1} ; _{i,i-1} ; _{i,i+1} ; _{i,i} ; _i ; _i ; _i ; _{i,i} ; _i ; _i ; _i ; _{i+1} ; _i ; _i ; _i ; _i ; _{i,1} ; _{i,i-1} ; _{i,i} ; _{i,i+1} ; _{i,i+2} ; _i ; _i ; _j
```

## Scan 21
Start (UTC): 2026-11-17T23:43:40+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:43:57+00:00  
End (UTC): 2026-11-17T23:44:14+00:00

### Independent words and accents from the crops
Only verbal phrases are ‘échange des coordonnées’ and ‘échange de’. Acute accents are visible on échange and the ending of coordonnées. The mathematical questions are question marks above equality signs; the second mark has a 2-like curved head. No other prose in the lower half.

### Independent visual observations
Four brace groups occupy the upper portion. First: sigma_i on f_i−1=id; on (f_i+1/f_i−1) exchanges xi,xi+1; on E/f_i+1=id, with (i≥1) at left. Second: sigma0 on f1 exchanges b0,b1 (possibly s0,s1); on E/f1=id. Third: sigma_i sigma_i+1 on f_i−1=id, on f_i+2/f_i−1 has a question above equals, on E/f_i+2=id; (i≥1) at left beside a slanted crossed mark. Fourth: sigma0sigma1 on f2 has question above equals, on E/f2=id. E has three arms; f is a looped ascender/descender and its alphabet remains uncertain. Archive20 only at bottom; the remainder is blank.

### Comparison and changes
No reading change. Removed the second b/s doubt wrapper on b_1: the recurring b/s ambiguity is marked at b_0 and recorded once in the notation table, as required.

### Detailed checks
All ten restriction formulas checked individually, including the parentheses in the first quotient, the absence of parentheses in the later quotients, both i≥1 qualifiers, all i−1/i+1/i+2 distinctions, the xi/xi+1 coordinate pair and both question marks above equals. There are no j indices. The slanted cancelled mark at the far left remains a tentative i≥0; the visible live i≥1 beside it is separate. No other deletion or insertion is visible. E is roman, not F or blackboard; the f/fraktur-f and b/s candidates remain unresolved. No typed text or handwritten additions to type. The bottom third is blank except archive20.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
(i\geq1)\quad\left\{\begin{aligned}
\sigma_i\mid\unsure{f_{i-1}|\mathfrak f_{i-1}}&=\mathrm{id}\\
\sigma_i\mid(f_{i+1}/f_{i-1})&=\text{échange des coordonnées}\quad x_i,x_{i+1}\\
\sigma_i\mid E/f_{i+1}&=\mathrm{id}
\end{aligned}\right.
```

Formula 2 (display):
```latex
\left\{\begin{aligned}
\sigma_0\mid f_1&=\text{échange de}\quad\unsure{b_0|s_0},b_1\\
\sigma_0\mid E/f_1&=\mathrm{id}
\end{aligned}\right.
```

Formula 3 (inline):
```latex
i\geq0
```

Formula 4 (display):
```latex
(i\geq1)\quad\left\{\begin{aligned}
\sigma_i\sigma_{i+1}\mid f_{i-1}&=\mathrm{id}\\
\sigma_i\sigma_{i+1}\mid f_{i+2}/f_{i-1}&\overset{?}{=}\\
\sigma_i\sigma_{i+1}\mid E/f_{i+2}&=\mathrm{id}
\end{aligned}\right.
```

Formula 5 (display):
```latex
\left\{\begin{aligned}
\sigma_0\sigma_1\mid f_2&\overset{?}{=}\\
\sigma_0\sigma_1\mid E/f_2&=\mathrm{id}
\end{aligned}\right.
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — left margin beside lines 6-8:
```latex
\unsure{$i\geq0$}
```

`\margin` — left margin beside lines 6-8:
```latex
\deleted{\unsure{$i\geq0$}}
```
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _{i-1} ; _{i-1} ; _i ; _{i+1} ; _{i-1} ; _i ; _{i+1} ; _i ; _{i+1} ; _i ; _{i+1} ; _{i-1} ; _i ; _{i+1} ; _{i+2} ; _{i-1} ; _i ; _{i+1} ; _{i+2}
```

## Scan 22
Start (UTC): 2026-11-17T23:44:14+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:44:52+00:00  
End (UTC): 2026-11-17T23:46:36+00:00

### Independent words and accents from the crops
Crop-first words and accents: ‘Soit G l’image de G_n dans Aut.Aff(E)’, ‘on suppose maintenant que k est un corps’, ‘la’ before struck ‘polyèdre’, inserted ‘n-carte’, underlined ‘régulière’, struck ‘primitive’, ‘correspondante’. ‘On a donc une représentation régulière de Π.’ A following word looks ‘Correspondant’ or ‘Correspondent’; then ‘une représentation fidèle de’, ‘et une application injective’. ‘Les applications … sont elles aussi injectives – en d’autres termes, si …’. Lower live text: ‘g f_i=f_i, g est-il dans le groupe engendré par … ? Ce n’est pas évident du tout – et c’est pourquoi il n’est pas clair que des résultats sur les … ordres des polygones associés à la réalisation … de Π, impliquent quelque chose sur les ordres des sigma_i sigma_i+1 !’. Accents on régulière, représentation, fidèle, coordonnées? (not present as a complete word), évident, résultats, associés. Abbreviation réal. in the lower sentence; exact cancelled and added words require closer inspection.

### Independent visual observations
The first capital G and later G_n have different degrees of looping; the latter might be script. Pi is a clear horizontal bar with two legs. Three underlines under régulière, fidèle, injective. Mapping D_i(Pi) → Grass.aff_i(E) has a crossed prefix at the target. The middle paragraph contains two long cancelled lines, an inserted phrase over a cancellation and a hat over sigma_i in the generator list. The group membership glyph before G is overwritten. The final prose has a short crossed word ‘les’ or ‘des’ after ‘sur les’, and inserted words over ‘de’ near Π. The bottom third has only that prose, no further formula or diagram.

### Comparison and changes
`Correspondant à` -> `Correspondant|Correspondent:`: the two dots are a colon, not à. `correspondant` -> `correspondante|correspondant` because the final stroke may be e. Removed an extra closing prose parenthesis after Drap.max(E). Reversed max candidates to baseline .max first, subscript max second. `g et g′ se correspondent` -> tentative `g et g′ coïncident`; the enlarged cancellation has the shorter word and a dotted interior. `envisagée` -> `associée|envisagée` in the lower insertion. Added roman/script alternatives to G_n and le/G to the opening of the cancelled parenthesis. Moved the recurring f/fraktur-f ambiguity to the first f occurrence in the cancelled line.

### Detailed checks
Checked all inline expressions: G, G_n, both AutAff(E), k, Pi, G=Aut(Pi), both flag names, D_i(Pi) mapping and its arrow, g∈G⊂AutAff(E), both struck generator/flag lists, gf_i=f_i and the final sigma_i sigma_i+1. In the live generator list, i−1, hatted i and i+1 are separate and the hat remains over sigma_i. No j occurs. Rechecked the crossed polyèdre/inserted n-carte, primitive, et, Esp prefix, attempted sigma pair, overwritten g′, two cancelled prose lines and their internal addition, deleted ordres and de, and added associée candidate. The long stroke near ‘engendré’ in the live question belongs to the letters, not a block cancellation. Underlines under régulière, fidèle and injective remain. There is no independent margin note or typed hand. The most insecure content is still the two cancelled prose lines; it remains explicitly tentative. Pi’s bar and legs are distinct from the looped G; no blackboard alphabet is visible.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (inline):
```latex
G
```

Formula 2 (inline):
```latex
\unsure{G_n|\mathscr G_n}
```

Formula 3 (inline):
```latex
\mathrm{Aut.\,Aff}(E)
```

Formula 4 (inline):
```latex
k
```

Formula 5 (inline):
```latex
\Pi
```

Formula 6 (inline):
```latex
n
```

Formula 7 (inline):
```latex
\Pi
```

Formula 8 (inline):
```latex
G=\mathrm{Aut}(\Pi)
```

Formula 9 (inline):
```latex
\mathrm{Aut\,Aff}(E)
```

Formula 10 (inline):
```latex
\unsure{\mathrm{Drap}(\Pi)|\mathrm{Rep}(\Pi)}
```

Formula 11 (inline):
```latex
\unsure{\mathrm{Drap.\,max}(E)|\mathrm{Drap}_{\max}(E)}
```

Formula 12 (inline):
```latex
D_i(\Pi)\longrightarrow\deleted{\unsure{\mathrm{Esp.}}}\unsure{\mathrm{Grass.aff}_i(E)|\mathrm{Grass}_i(E)}
```

Formula 13 (inline):
```latex
\unsure{\sigma,\sigma'}\in
```

Formula 14 (inline):
```latex
g\deleted{,\unsure{g'}}\in G\subset\mathrm{Aut.\,Aff}(E)
```

Formula 15 (inline):
```latex
\sigma_0,\ldots,\sigma_n
```

Formula 16 (inline):
```latex
g\cdot\unsure{f_0|\mathfrak f_0},\unsure{f_1},\ldots,\unsure{f_n}
```

Formula 17 (inline):
```latex
gf_i=f_i
```

Formula 18 (inline):
```latex
g
```

Formula 19 (inline):
```latex
\sigma_0\,\cdots\,\sigma_{i-1}\,\widehat{\sigma_i}\,\sigma_{i+1}\,\cdots\,\sigma_n
```

Formula 20 (inline):
```latex
\Pi
```

Formula 21 (inline):
```latex
\sigma_i\sigma_{i+1}
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 1-7:
```latex
polyèdre
```

`\deleted` — lines 1-7:
```latex
\unsure{primitive}
```

`\deleted` — lines 1-7:
```latex
\unsure{et}
```

`\deleted` — lines 8-10:
```latex
\unsure{\mathrm{Esp.}}
```

`\deleted` — lines 8-10:
```latex
$\unsure{\sigma,\sigma'}\in$
```

`\deleted` — lines 8-10:
```latex
,\unsure{g'}
```

`\deleted` — lines 11-12: cancelled wording and its interlinear addition:
```latex
(\unsure{le|G} \unsure{engendré par} $\sigma_0,\ldots,\sigma_n$) \unsure{est tel}
```

`\deleted` — lines 11-12: cancelled wording and its interlinear addition:
```latex
\unsure{g et g' coïncident} \inserted{\unsure{fixant le drapeau}} \unsure{en un même} $g\cdot\unsure{f_0|\mathfrak f_0},\unsure{f_1},\ldots,\unsure{f_n}$
```

`\deleted` — lines 13-20:
```latex
\unsure{ordres}
```

`\deleted` — lines 13-20:
```latex
de
```

`\inserted` — lines 1-7:
```latex
$n$-carte
```

`\inserted` — lines 11-12: cancelled wording and its interlinear addition:
```latex
\unsure{fixant le drapeau}
```

`\inserted` — lines 13-20:
```latex
\unsure{associée|envisagée}
```
- `\margin`: none.
- `\handwritten`: none.

`\uline` — lines 1-7:
```latex
régulière
```

`\uline` — lines 1-7:
```latex
régulière
```

`\uline` — lines 1-7:
```latex
fidèle
```

`\uline` — lines 1-7:
```latex
injective
```
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _i ; _i ; _i ; _i ; _{i-1} ; _i ; _{i+1} ; _i ; _{i+1}
```

## Scan 23
Start (UTC): 2026-11-17T23:46:36+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:47:03+00:00  
End (UTC): 2026-11-17T23:48:03+00:00

### Independent words and accents from the crops
No lexical prose or accents: this is a calculation sheet. The only letter-like labels are a, b, pi, alpha, Sigma and the coordinate variables. The upper last coordinate in the input appears x_n, without a clearly visible +1. The side note reads alpha_0=−1.

### Independent visual observations
Top sigma0sigma1 is underbraced as pi, with a and b expanded below vertical equality strokes. A cancelled attempted inverse follows. Pi² is written in two coordinates over two lines, then expanded again; small underlines occur under several terms of the first expansion. Pi³ continues across multiple lines to the right edge. A long curved arrow from the second coordinate carries it into the simplified tuple below. At the right edge an abandoned coefficient is struck; another crossed addition follows (alpha0+1)(a alpha0−b). Below are three scalar conditions: alpha0(1+alpha0)=0, alpha0(alpha0²−2)=1, alpha0²=1, then a vertical separator and alpha0=−1. A left brace includes a cancelled 2a-like start underneath. Lower third otherwise blank. No i/j indices, no script or double-struck capital.

### Comparison and changes
At the end of the cancelled inverse line, `0` -> `sigma|0`: the enlarged glyph has a horizontal head and lower loop. In the crossed addition after (alpha0+1)(a alpha0−b), `+alpha0−1` -> `+b−a|+alpha0−1`; the compressed under-strokes admit the shorter reading.

### Detailed checks
Compared the top tuple and both vertically attached definitions, the cancelled inverse line, each line of pi² and pi³, the simplified coefficient, the side alpha0=−1 and all three scalar conditions. Confirmed the source’s x_n endpoints, all alpha indices0/1, superscripts−1/2/3 and every sign before x1,x2,Sigma1. There are no i/j indices. The short underlines in pi² remain under their individual terms, and the long underbrace/forwarding arrow remains separate from cancellation. The diagram contains the curved downward forwarding arrow and the long coefficient calculation. The margin note is horizontal and reads alpha0=−1. Cancelled inverse, tentative +alpha, abandoned edge coefficient, crossed addition and bottom 2a are all present. No textual accents, typescript corrections, script or blackboard capitals; pi/Pi is still marked at its first occurrence.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
\underbrace{\sigma_0\sigma_1}_{\unsure{\pi|\Pi}}(x_1,\unsure{x_2},x_3,\ldots,x_n)
=(1+\alpha_0x_1-x_2+\underset{\substack{\Vert\\1+\alpha_1+2\alpha_0+\alpha_0\alpha_1}}{a}\Sigma_1,
x_1+\underset{\substack{\Vert\\1+\alpha_1}}{b}\Sigma_1,x_3,\ldots)
```

Formula 2 (display):
```latex
\deleted{\unsure{\pi^{-1}}=\sigma_1\sigma_0(x_1,\unsure{x_2},\ldots,\unsure{x_n})=\unsure{\sigma|0}}
```

Formula 3 (display):
```latex
\begin{aligned}
\pi^2(x_1,\ldots,x_n)={}&\underline{1}+\alpha_0(\underline{1}+\underline{\alpha_0x_1}-\underline{x_2}+\underline{a\Sigma_1})-\underline{x_1}-\underline{b\Sigma_1}+\underline{a\Sigma_1},\\
&1+\alpha_0x_1-x_2+a\Sigma_1+b\Sigma_1,x_3,\ldots)\\
={}&((1+\alpha_0)+(\alpha_0^2-1)x_1-\alpha_0x_2+(a\alpha_0+a-b)\Sigma_1,\\
&1+\alpha_0x_1-x_2+(a+b)\Sigma_1,x_3,\ldots)
\end{aligned}
```

Formula 4 (display):
```latex
\begin{aligned}
\pi^3(x_1,\ldots,x_n)={}&1+\alpha_0(1+\alpha_0)+\alpha_0(\alpha_0^2-1)x_1-\alpha_0^2x_2+\alpha_0(a\alpha_0+a-b)\Sigma_1\\
&-1\deleted{\unsure{+\alpha}}-\alpha_0x_1+x_2-(a+b)\Sigma_1+a\unsure{\Sigma_1},\\
&\underbrace{(1+\alpha_0)+(\alpha_0^2-1)x_1-\alpha_0x_2+\unsure{[}a(\alpha_0+1)\Sigma_1}_{\phantom{(1+\alpha_0)+(\alpha_0^2-1)x_1}} ,x_3,\unsure{\ldots}
\end{aligned}
```

Formula 5 (inline):
```latex
\alpha_0=-1
```

Formula 6 (display):
```latex
\left\{\begin{aligned}
\alpha_0(1+\alpha_0)&=0\qquad\alpha_0(\alpha_0^2-2)=1\qquad\alpha_0^2=1\quad\bigm|\quad\alpha_0=-1\\[2ex]
&\deleted{\unsure{2a}}
\end{aligned}\right.
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — line 3, cancelled:
```latex
\unsure{\pi^{-1}}=\sigma_1\sigma_0(x_1,\unsure{x_2},\ldots,\unsure{x_n})=\unsure{\sigma|0}
```

`\deleted` — lines 8-10:
```latex
\unsure{+\alpha}
```

`\deleted` — lines 11-12; curved forwarding arrow reproduced at right:
```latex
\unsure{1+}
```

`\deleted` — lines 11-12; curved forwarding arrow reproduced at right:
```latex
\unsure{a\alpha_0^2+a\alpha_0}
```

`\deleted` — lines 11-12; curved forwarding arrow reproduced at right:
```latex
\unsure{+b-a|+\alpha_0-1}
```

`\deleted` — lines 13-14:
```latex
\unsure{2a}
```

`\margin` — left note alongside final calculation:
```latex
$\alpha_0=-1$
```
- `\handwritten`: none.

`\diagram` — lines 11-12; curved forwarding arrow reproduced at right:
```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
{}\&{}\arrow[dd,bend left=20]\&{}\\
{\begin{aligned}
=\deleted{\unsure{1+}}\ \alpha_0(1+\alpha_0)+\alpha_0(\alpha_0^2-2)x_1+(1-\alpha_0^2)x_2
+\unsure{(}\deleted{\unsure{a\alpha_0^2+a\alpha_0}}\qquad\qquad\\
(\alpha_0+1)(a\alpha_0-b)\deleted{\unsure{+b-a|+\alpha_0-1}})\Sigma_1,
\end{aligned}}\&{}\&{}\\
{}\&{}\&{}
\end{tikzcd}
```
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
No i/j-bearing index or exponent.
```

## Scan 24
Start (UTC): 2026-11-17T23:48:03+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:48:38+00:00  
End (UTC): 2026-11-17T23:50:00+00:00

### Independent words and accents from the crops
Crop-first words: cancelled heading ‘Incidence?’ or ‘Invariants?’; right note ‘pt à l’infini de la … dr(s_0 s_1)’ with a crossed ‘droite’. No other lexical prose. The note’s accent on à and apostrophe in l’infini are visible; its last parentheses reach the edge.

### Independent visual observations
Top attempted u(x,y)=sigma0sigma1(x,y)= is crossed, followed by a diagonally cancelled two-row sigma0/sigma1 system with nu-like parameters. Another heavily hatched product line follows. Live coordinate formulas for sigma0, sigma_i and sigma_n; the next unchanged coordinate after the changed pair resembles x_{i+3}. Cancelled quadratic f has both a_i² and x_i². The boxed H0,D0,H_i,D_i block is crossed diagonally; H0’s last glyph is z-shaped, and D0/D_i also contain z=0. H_i has an overwritten initial coordinate and a bracket overwritten at the end. In the bottom homogeneous sigma0 formula, z is identified above as x0, the coordinate tuple is underbraced as bar x, and a cancelled prefix precedes the e′ bracket. That bracket visibly has e0′−e1′, with no2. Tensor products are circled crosses. General sigma_i formula has a left qualifier1≤i≤n; the final sigma_n line is separate. e′ indices and e indices are visually distinct. No double-struck capitals.

### Comparison and changes
In the cancelled quadratic expression, moved the overwritten j to the subscript of a_i and restored a following tentative a_j|x_j after x_i²; the former reading reduced this to a deleted j. Included the visible top/left/bottom border around the cancelled H/D block. Added doubt to the heavily overwritten final bracket of H_i. Nested ‘la droite’, rather than only ‘droite’, inside its local cancellation. Added b0b1 as another candidate in the marginal line-name.

### Detailed checks
Compared every coordinate of the three live transformations, the three cancelled trial displays, every term and summation bound of f, all four H/D lines and all three homogeneous/tensor formulas. Kept the visibly questionable i+3 coordinate, first quadratic lower bound0|1, and e0′−e1′ without inserting an expected2. Rechecked every i/j in d_ij, xi xj, summation1≤i<j, i−1/i+1/i+2/i+3 and the prime on each dual e. The first sigma_i qualifier ends n−1; the lower barred-sigma qualifier ends n as written. z and x0 are linked by the visible equality annotation, with the tuple underbraced as bar x. Margin note read independently along its two horizontal lines; a diagonal cancellation traverses the entire H/D block and that note. Underline on the uncertain heading is preserved. No script or blackboard letters; nu/v remains unresolved in the first cancelled system. The tensor-circle in the first line is heavily inked and remains marked.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
\deleted{u(x,y)=\sigma_0\sigma_1(x,y)=}
```

Formula 2 (display):
```latex
\deleted{\left\{\begin{aligned}
\sigma_0(x,y)&=(1-(1+\unsure{\nu_0|v_0})x+\alpha_0y,y)\\
\sigma_1(x,y)&=(-\nu_1y,x+(\nu_1+1)y)
\end{aligned}\right.}
```

Formula 3 (display):
```latex
\deleted{\unsure{u(x,y)=\sigma_0\sigma_1(x,y)=}}
```

Formula 4 (display):
```latex
\sigma_0(x_1,\ldots,x_{n+1})=(1-x_1+\alpha_0\Sigma_0,x_2,\ldots,x_{n+1})
```

Formula 5 (display):
```latex
\sigma_i(x_1,\ldots,x_{n+1})=(x_1,\ldots,x_{i-1},x_{i+1}-(1+\alpha_i)\Sigma_i,x_i+(1+\alpha_i)\Sigma_i,x_{\unsure{i+3|i+2}},\ldots,x_{n+1})\tag*{$1\leq i\leq n-1$}
```

Formula 6 (display):
```latex
\sigma_n(x_1,\ldots,x_{n+1})=(x_1,\ldots,x_{n-1},x_{n+1},x_n)
```

Formula 7 (display):
```latex
\deleted{f(x_1,\ldots,x_{n+1})=\sum_{\unsure{0|1}\leq i\leq n}a_{\deleted{\unsure{j}}i}^2x_i^2\unsure{a_j|x_j}+\sum_{1\leq i<j\leq\unsure{n+1}}\unsure{d_{ij}|a_{ij}}x_ix_j+\sum_{1\leq i\leq n+1}c_ix_i}
```

Formula 8 (display):
```latex
\begin{array}{|l}\hline
\deleted{\begin{aligned}
H_0:\quad&2x_1\unsure{-|+}\alpha_0(x_2+\cdots+x_{n+1})=z\\
D_0:\quad&x_2=x_3=\cdots=x_{n+1}=z=0\\[2ex]
H_i:\quad&x_i-x_{i+1}+(1+\alpha_i)(x_{i+2}\deleted{\unsure{=0}}+x_{i+3}+\cdots+x_{n+1}\unsure{\}|)}=0\\
D_i:\quad&\{x_1=\cdots\ x_{i-1}=x_{i+2}=\cdots=x_{n+1}=z=0
\end{aligned}}\\\hline
\end{array}
```

Formula 9 (inline):
```latex
\unsure{\mathrm{dr}(s_0s_1)|\mathrm{dr}(b_0b_1)|\mathrm{dr}(s_0,s_1)}
```

Formula 10 (display):
```latex
\begin{aligned}
\overline{\sigma}_0(\underbrace{x_1,\ldots,x_{n+1},\overset{x_0}{\overset{=}{z}}}_{\overline{x}})
&=(x_0-x_1+\alpha_0(x_2+\cdots+x_{n+1}),x_2,\ldots,x_{n+1},x_0)\\
&=\overline{x}+\deleted{\unsure{e_1}}[e'_0-e'_1+\alpha_0(e'_2+\cdots+e'_{n+1})]\unsure{\otimes}e_1
\end{aligned}
```

Formula 11 (display):
```latex
\overline{\sigma}_i(\overline{x})=\overline{x}+[e'_i-e'_{i+1}+(1+\alpha_i)(e'_{i+2}+\cdots+e'_{n+1})]\otimes(-e_i+e_{i+1})\tag*{$(1\leq i\leq n)$}
```

Formula 12 (display):
```latex
\overline{\sigma}_n(\overline{x})=\overline{x}+(e'_n-e'_{n+1})\otimes(-e_n+e_{n+1})
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 1-4, cancelled trials:
```latex
u(x,y)=\sigma_0\sigma_1(x,y)=
```

`\deleted` — lines 1-4, cancelled trials:
```latex
\left\{\begin{aligned}
\sigma_0(x,y)&=(1-(1+\unsure{\nu_0|v_0})x+\alpha_0y,y)\\
\sigma_1(x,y)&=(-\nu_1y,x+(\nu_1+1)y)
\end{aligned}\right.
```

`\deleted` — lines 1-4, cancelled trials:
```latex
\unsure{u(x,y)=\sigma_0\sigma_1(x,y)=}
```

`\deleted` — line 8, cancelled quadratic expression:
```latex
f(x_1,\ldots,x_{n+1})=\sum_{\unsure{0|1}\leq i\leq n}a_{\deleted{\unsure{j}}i}^2x_i^2\unsure{a_j|x_j}+\sum_{1\leq i<j\leq\unsure{n+1}}\unsure{d_{ij}|a_{ij}}x_ix_j+\sum_{1\leq i\leq n+1}c_ix_i
```

`\deleted` — line 8, cancelled quadratic expression:
```latex
\unsure{j}
```

`\deleted` — lines 9-14: boxed block cancelled with diagonal strokes:
```latex
\uline{\unsure{Incidence|Invariants}?}
```

`\deleted` — lines 9-14: boxed block cancelled with diagonal strokes:
```latex
\begin{aligned}
H_0:\quad&2x_1\unsure{-|+}\alpha_0(x_2+\cdots+x_{n+1})=z\\
D_0:\quad&x_2=x_3=\cdots=x_{n+1}=z=0\\[2ex]
H_i:\quad&x_i-x_{i+1}+(1+\alpha_i)(x_{i+2}\deleted{\unsure{=0}}+x_{i+3}+\cdots+x_{n+1}\unsure{\}|)}=0\\
D_i:\quad&\{x_1=\cdots\ x_{i-1}=x_{i+2}=\cdots=x_{n+1}=z=0
\end{aligned}
```

`\deleted` — lines 9-14: boxed block cancelled with diagonal strokes:
```latex
\unsure{=0}
```

`\deleted` — lines 9-14: boxed block cancelled with diagonal strokes:
```latex
(pt à l'infini de \deleted{la droite} $\unsure{\mathrm{dr}(s_0s_1)|\mathrm{dr}(b_0b_1)|\mathrm{dr}(s_0,s_1)}$\unsure{)}
```

`\deleted` — lines 9-14: boxed block cancelled with diagonal strokes:
```latex
la droite
```

`\deleted` — lines 15-16:
```latex
\unsure{e_1}
```

`\margin` — lines 9-14: boxed block cancelled with diagonal strokes:
```latex
\deleted{(pt à l'infini de \deleted{la droite} $\unsure{\mathrm{dr}(s_0s_1)|\mathrm{dr}(b_0b_1)|\mathrm{dr}(s_0,s_1)}$\unsure{)}}
```
- `\handwritten`: none.

`\uline` — lines 9-14: boxed block cancelled with diagonal strokes:
```latex
\unsure{Incidence|Invariants}?
```
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _{i-1} ; _{i+1} ; _i ; _i ; _i ; _i ; _i ; _i ; _j ; _j ; _{ij} ; _{ij} ; _i ; _j ; _{1\leq i\leq n+1} ; _i ; _i ; _i ; _i ; _{i+1} ; _i ; _{i+2} ; _{i+3} ; _i ; _{i-1} ; _{i+2} ; _i ; _i ; _{i+1} ; _i ; _{i+2} ; _i ; _{i+1}
```

## Scan 25
Start (UTC): 2026-11-17T23:50:00+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:50:21+00:00  
End (UTC): 2026-11-17T23:50:41+00:00

### Independent words and accents from the crops
Crop-first words: ‘z variable d’homogénéité’, ‘pt à l’infini dans la direction de’ (twice). The superscript-like t in pt is small; à has its accent, and l’infini its apostrophe. The middle letters/accents of homogénéité are compressed.

### Independent visual observations
H0: x0−2x1+alpha0(x2+...+xn+1)=0; z with a vertical equality is attached above x0. A D-shaped old label underlies delta0, followed by direction e1=s1−s0. H_i: xi−xi+1+(1+alpha_i)(xi+2+...+xn+1)=0. Delta_i direction e_i+1−e_i=s_i+1−s_i is broken over two lines. A left note gives1≤i≤n. A short horizontal separator lies below; all remaining thirds are blank except faint paper/pen traces and archive24. E-like capitals are H, lower point label is delta or d; s differs from the b-like forms of scan21.

### Comparison and changes
Added a doubt wrapper to homogénéité: the label is readable as that word, but its compressed middle and accents are not individually secure. No mathematical reading changed.

### Detailed checks
Checked H0 and its z=x0 attachment, the overwritten D0/delta0 label, e1=s1−s0, H_i, the left range1≤i≤n and both lines of e_i+1−e_i=s_i+1−s_i. All i/i+1/i+2 and n+1 positions were compared; no j appears. The rightmost e_i remains doubtful because it is overwritten or thickened. The margin range is horizontal and not crossed. Apart from D0 there is no legible deleted content; the separator does not cross any word. H is roman; delta/d is the recorded candidate pair, and s and e have distinct bodies. No type, no handwritten correction on type, no further drawing or text in the blank lower thirds.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
H_0:\quad\overset{\substack{z\ \text{variable d'\unsure{homogénéité}}\\\Vert}}{x_0}-2x_1+\alpha_0(x_2+\cdots+x_{n+1})=0
```

Formula 2 (inline):
```latex
\deleted{D_0}\unsure{\delta_0|d_0}:
```

Formula 3 (inline):
```latex
e_1=s_1-s_0
```

Formula 4 (display):
```latex
H_i:\quad x_i-x_{i+1}+(1+\alpha_i)(x_{i+2}+\cdots+x_{n+1})=0
```

Formula 5 (inline):
```latex
1\leq i\leq n
```

Formula 6 (inline):
```latex
\delta_i:
```

Formula 7 (display):
```latex
\begin{aligned}
e_{i+1}-\unsure{e_i}&\\[-1ex]
&=s_{i+1}-s_i
\end{aligned}
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — line 2:
```latex
D_0
```

`\margin` — left of lines 3-5:
```latex
$1\leq i\leq n$
```
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _i ; _{i+1} ; _i ; _{i+2} ; _i ; _{i+1} ; _i ; _{i+1} ; _i
```

## Scan 26
Start (UTC): 2026-11-17T23:50:41+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:51:10+00:00  
End (UTC): 2026-11-17T23:52:01+00:00

### Independent words and accents from the crops
Crop-first words: the boxed heading is ‘Pour 0≤i≤n’; the case labels are ‘si’. No accents or other lexical prose. The top qualifier is i≥2, and the box’s last condition visibly uses a strict less-than sign after i+2.

### Independent visual observations
Read the landscape sheet left-to-right using the three vertical crops. Top sigma0s_i=−(1+alpha_i)s0+(1+alpha_i)s1+s_i, followed by a commutation calculation for sigma0s_i+1. Middle unboxed sigma_i actions, including the i−1 zero-coordinate brace in sigma_i s_i+2 and the two equivalent affine expressions. Large box gives four cases for sigma_i s_j; bottom-right gives four cases for sigma_i s_j−s_j. Bottom-left box is sigma_i−id=h_i tensor(s_i+1−s_i), with h_i=s_i′−s_i+1′+(1+alpha_i)(s_i+2′+...+s_n+1′). The first alpha index is i-like despite sigma0 context; h/l remains ambiguous. Several crossed starts occur above the large box and beside the two bottom formulas. The prime strokes on s′ are above the body, while i,j subscripts lie below; j has a long descender.

### Comparison and changes
Bottom-right zero case: `0≤j≤i−1` -> `i|0≤j≤i−1`; the enlarged crop has an i-like body with a dot, partly crossed by the box border. Kept i first despite the expected0. Added the visible opening brace at the end of the cancelled start near the lower box.

### Detailed checks
Compared the landscape formulas across crop overlaps, including both long top equalities, all three middle action equations, the coordinate tuple and its i−1 brace, both affine rewrites, all four boxed cases, the tensor expression and its linear form, and all four bottom-right difference cases. Checked every i and j against its dot/descender, including sigma_j in a cancelled heading, i≥2, i+2<j≤n+1 in the box and j≥i+2 below. The strict/weak difference is retained. All primes on s′ are superscript strokes, not index marks; h/l remains unresolved. The large and small boxes are enclosures, not cancellations; the three crossed starts are marked separately. No separate margin note, no type, no accents or script capital. The top alpha_i/alpha0 candidate is not forced by the sigma0 context.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (display):
```latex
\sigma_0\unsure{s_i}=-(1+\unsure{\alpha_i|\alpha_0})s_0+(1+\alpha_i)s_1+s_i
```

Formula 2 (display):
```latex
i\geq2
```

Formula 3 (display):
```latex
\sigma_0s_{i+1}=\sigma_0\sigma_is_i=\sigma_i\sigma_0s_i=-(1+\alpha_i)s_0+(1+\alpha_i)s_1+s_{i+1}
```

Formula 4 (display):
```latex
\begin{aligned}
\sigma_is_j&=s_j\qquad 0\leq j\leq i-1\\
\sigma_is_i&=s_{i+1}\\
\sigma_is_{i+1}&=s_i
\end{aligned}
```

Formula 5 (display):
```latex
\begin{aligned}
\sigma_is_{i+2}&=(\underbrace{0,\ldots,0}_{i-1},-(1+\alpha_i),(1+\alpha_i),1,0,0,\ldots)=s_{i+2}+(1+\alpha_i)(s_{i+1}-s_i)\\
&=-(1+\alpha_i)s_i+(1+\alpha_i)s_{i+1}+s_{i+2}
\end{aligned}
```

Formula 6 (inline):
```latex
\unsure{\sigma_j|\sigma_i}s_{i+2}
```

Formula 7 (inline):
```latex
0\leq i\leq n
```

Formula 8 (display):
```latex
\boxed{\sigma_is_j=\left\{\begin{aligned}
&s_j&&\text{si }0\leq j\leq i-1\\
&s_{i+1}&&\text{si }j=i\\
&s_i&&\text{si }j=i+1\\
&-(1+\alpha_i)s_i+(1+\alpha_i)s_{i+1}+s_j&&\text{si }i+2<j\leq n+1
\end{aligned}\right.}
```

Formula 9 (inline):
```latex
\sigma_is_j-s_j=
```

Formula 10 (display):
```latex
\boxed{\begin{aligned}
\sigma_i-\mathrm{id}&=\unsure{h_i|l_i}\otimes(s_{i+1}-s_i)\qquad\deleted{\unsure{\sigma_i s_j=x-x}\{}\\
h_i&=s'_i-s'_{i+1}+(1+\alpha_i)(s'_{i+2}+\cdots+s'_{n+1})
\end{aligned}}
```

Formula 11 (display):
```latex
\sigma_is_j-s_j=\left\{\begin{aligned}
&0&&\text{si }\unsure{i|0}\leq j\leq i-1\\
&s_{i+1}-s_i&&\text{si }j=i\\
&-(s_{i+1}-s_i)&&\text{si }j=i+1\\
&(1+\alpha_i)(s_{i+1}-s_i)&&\text{si }j\geq i+2
\end{aligned}\right.
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lower box heading:
```latex
$\unsure{\sigma_j|\sigma_i}s_{i+2}$
```

`\deleted` — bottom left box, lines 13-14:
```latex
$\sigma_is_j-s_j=$
```

`\deleted` — bottom left box, lines 13-14:
```latex
\unsure{\sigma_i s_j=x-x}\{
```
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _i ; _i ; _i ; _{i+1} ; _i ; _i ; _i ; _i ; _i ; _i ; _{i+1} ; _i ; _j ; _j ; _i ; _i ; _{i+1} ; _i ; _{i+1} ; _i ; _i ; _{i+2} ; _{i-1} ; _i ; _i ; _{i+2} ; _i ; _{i+1} ; _i ; _i ; _i ; _i ; _{i+1} ; _{i+2} ; _j ; _i ; _{i+2} ; _i ; _j ; _j ; _{i+1} ; _i ; _i ; _i ; _i ; _{i+1} ; _j ; _i ; _j ; _j ; _i ; _i ; _i ; _{i+1} ; _i ; _i ; _j ; _i ; _i ; _{i+1} ; _i ; _{i+2} ; _i ; _j ; _j ; _{i+1} ; _i ; _{i+1} ; _i ; _i ; _{i+1} ; _i
```

## Scan 27
Start (UTC): 2026-11-17T23:52:01+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:52:31+00:00  
End (UTC): 2026-11-17T23:52:46+00:00

### Independent words and accents from the crops
Crop-first spellings/accents: ‘à’, ‘manière’, ‘décisive’, ‘économique’, ‘privé’, ‘maître’, ‘réduisant’, ‘efficacité’; ‘déception’, ‘inquiétude’, ‘placé’, ‘électorale’, ‘succès’, ‘anti-monopoliste’, ‘désavouer’, ‘française’, ‘socio-démocrates’; ‘immédiate’, ‘actualisé’, ‘c’est-à-dire’, ‘ajusté’, ‘très’, ‘aggravée’; ‘Universités’, ‘responsabilités’, ‘dépend’; ‘désormais’, ‘fidèles’, ‘portée’, ‘transformatrice’. Capitals PS and MRG; Parti Socialiste; Parti Communiste; François? The issuer clearly reads Français, with ç. The announcement spells DECEMBRE without an accent and A in uppercase, followed later by lowercase à. Date10 DECEMBRE1977, time15 H. ‘rassemblement aux Arceaux’ in parentheses.

### Independent visual observations
Five typed body paragraphs, then the slogan POUR LE CHANGEMENT PAR L’UNION SUR UN BON PROGRAMME, the demonstration announcement, parenthetic assembly location and issuer. No bold type, mathematical symbols, handwritten correction, cancellation, insertion, underlining or margin note. Archive26 alone is handwritten at the lower right. The hyphen in socio-démocrates is at the line break but belongs to the compound; anti-monopoliste and c’est-à-dire also retain their hyphens. No quotation marks are present.

### Comparison and changes
No change.

### Detailed checks
Read all five typed paragraphs word by word against the file, including accents, apostrophes, plural endings, commas and sentence stops. Confirmed socio-démocrates (not social-démocrates), anti-monopoliste, c’est-à-dire, uppercase Universités/Parti Socialiste/Parti Communiste, and both occurrences of1972. The headline and issuer capitals are ordinary type, without bold or double striking. Announcement is10 DECEMBRE1977 A15 H à MONTPELLIER; DECEMBRE/A remain unaccented capitals, while à is lowercase and accented. Location parentheses and Français’s cedilla are retained. No display or inline mathematical formula, i/j index, diagram, drawing, cancellation, insertion, marginal content or handwritten correction. Archive26 is a comment only.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

### Corrections, margins and line-adjacent text ledger
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
No i/j-bearing index or exponent.
```

## Scan 29
Start (UTC): 2026-11-17T23:52:46+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:53:10+00:00  
End (UTC): 2026-11-17T23:53:20+00:00

### Independent words and accents from the crops
Crop-first: pencil ‘(8 p)’ near the top centre. Ink title ‘n-quasi-polyèdres’; parenthetic ‘vieille rédaction’ (plural endings cannot be excluded confidently). Grave-looking mark on polyèdres, acute-looking mark on rédaction. No date.

### Independent visual observations
Only the two-line upper-right title and separate pencilled count are present. Lower two thirds are blank, apart from archive28 in the lower left. No formula other than the leading n, no line cancellation, insertion, underline or diagram. The count is in a lighter and less identifiable hand than the title.

### Comparison and changes
No change.

### Detailed checks
Checked the pencil8, p and enclosing parentheses independently of the ink title. Checked both title hyphens, n, polyèdres and the second line’s parentheses; the singular/plural alternatives remain. No i/j index, superscript, double-struck/script candidate, margin note, crossed text or handwritten material on type. The pencil count is transcribed as content, while archive28 remains a comment. No inference is made that this package itself contains8 pages.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (inline):
```latex
n
```

### Corrections, margins and line-adjacent text ledger
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
No i/j-bearing index or exponent.
```

## Scan 30
Start (UTC): 2026-11-17T23:53:20+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:54:08+00:00  
End (UTC): 2026-11-17T23:55:24+00:00

### Independent words and accents from the crops
Crop-first heading: ‘n-Quasi-polyèdres réguliers en coordonnées can.’ underlined. Words: ‘E affine de rang n+1’, ‘drapeau de E’, ‘Prop’, ‘une base affine’, ‘Par induction (on va prouver que … est affᵗ/aff. libre et (5)(6). Trivial si i=0. Supposons … prouvé pour j<i. Il faut prouver’; ‘par hyp. réc’, ‘Si on avait’, ‘comme’, ‘par réc’, ‘contrairement à (3 b), OK.’, ‘On a, comme’, ‘Enfin, on a’, final ‘OK.’ Accents visible on réguliers, coordonnées, prouvé, réc; shortened affine/hypothèse/récurrence forms need preserving.

### Independent visual observations
Numbered(1)–(6). Commutation formula starts sigma_j sigma_i; its condition includes the redundant i≤i+2. Flag E0={s0}⊂E1⊂…⊂En. Action on E_j for j≠i and nonfixing E_i. Recursive s_i definition spans1≤i≤n+1. Proposition uses Env.aff and a second sigma_k s_i=s_i claim; a small crossed +1-like suffix lies after the final n, and an underlined addition ‘pour0≤i≤n+1’ is beneath. Proof has i≥1 et inserted above ‘prouvé’, then three target relations, with the third interlinear. Contradiction display has equality labels under the first two transformed points and a membership label beneath the last. A source subset sign appears after sigma_i−1(s_i−1), although a point is being discussed. Final commutation chain has ‘réc’ above an equality. k/h-shaped indices are small and need enlarged comparison. Roman E is consistent; Env/Ens abbreviation remains uncertain.

### Comparison and changes
Flag label `(2)` -> `(1|2)` with1 first: the enlarged digit has a straight downstroke and no visible foot. Restored a tentative i and comma in the underlined ‘pour i,0≤i≤n+1’ addition. In the interlinear proof target and final proof chain, k -> h, marking h|k at the first occurrence; the proposition’s branched k is retained. Updated the notation table to record the difference.

### Detailed checks
Checked (1), the flag display, both relations (3), each row of (4), proposition (5)/(6), the induction targets, contradiction display and full final equality chain. In particular checked all i/j/k/h subscripts, j≠i, i−1/i−2/i+1, the n/n+1 endpoints, nonmembership and subset directions, source (3 b), and the annotation under each transformed point. Preserved the redundant bound0≤i≤i+2≤j≤n and the point subset sign in the prose. Insertions ‘pour i,…’, ‘i≥1 et’, the extra target and the replacement range are placed where the source connects them. The crossed +1 at the proposition range and crossed h>i are retained. Title/Prop underlines are not cancellations. The bold-looking Env initial is overwritten handwriting, not enough evidence for blackboard or script E; the Env/Ens letter ambiguity remains. No typescript correction, diagram or independent margin note.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (inline):
```latex
n
```

Formula 2 (display):
```latex
\left\{\begin{aligned}
&\sigma_0,\ldots,\sigma_n\in\mathrm{Aff}(E)\qquad E\ \text{affine de rang }n+1\\
&\sigma_j\sigma_i=\sigma_i\sigma_j\quad\text{si }0\leq i\leq i+2\leq j\leq n
\end{aligned}\right.\tag*{(1)}
```

Formula 3 (display):
```latex
E_0=\{s_0\}\subset E_1\subset\cdots\subset E_n\qquad\text{drapeau de }E\tag*{(\unsure{1|2})}
```

Formula 4 (display):
```latex
\left\{\begin{aligned}
\sigma_iE_j&=E_j\quad\text{si }j\ne i\\
\sigma_iE_i&\ne E_i
\end{aligned}\right.\tag*{(3)}
```

Formula 5 (display):
```latex
\left\{\begin{aligned}
&s_0\\
&s_1=\sigma_0s_0\\
&\cdots\\
&s_i=\sigma_{i-1}s_{i-1}\qquad(1\leq i\leq n+1)\\
&\cdots\\
&s_{n+1}=\sigma_ns_n
\end{aligned}\right.\tag*{(4)}
```

Formula 6 (inline):
```latex
(s_0,\ldots,s_{n+1})
```

Formula 7 (inline):
```latex
E
```

Formula 8 (display):
```latex
E_i=\unsure{\mathrm{Env.aff}|\mathrm{Ens.aff}}(s_0,\ldots,s_i)\tag*{(5)}
```

Formula 9 (display):
```latex
\sigma_ks_i=s_i\quad\text{si }0\leq i<k\leq n\deleted{\unsure{+1}}\tag*{(6)}
```

Formula 10 (inline):
```latex
\unsure{i}
```

Formula 11 (inline):
```latex
0\leq i\leq n+1
```

Formula 12 (inline):
```latex
(s_0,\ldots,s_i)
```

Formula 13 (inline):
```latex
i=0
```

Formula 14 (inline):
```latex
i\geq1
```

Formula 15 (inline):
```latex
j<i
```

Formula 16 (display):
```latex
\left\{\begin{aligned}
&s_i\notin E_{i-1}(=\mathrm{Env}(s_0,\ldots,s_{i-1})\ \text{par hyp. réc})\\
&E_i=\mathrm{Env}(E_{i-1},s_i)
\end{aligned}\right.
```

Formula 17 (inline):
```latex
\sigma_{\unsure{h|k}}s_i=s_i
```

Formula 18 (inline):
```latex
i<h\leq n
```

Formula 19 (inline):
```latex
s_i\in E_{i-1}
```

Formula 20 (inline):
```latex
\sigma_{i-1}s_{i-1}\in E_{i-1}
```

Formula 21 (inline):
```latex
\sigma_{i-1}s_j=s_j
```

Formula 22 (inline):
```latex
0\leq j\leq i-2
```

Formula 23 (inline):
```latex
E_{i-1}=\mathrm{Env}(s_0,\ldots,s_{i-1})
```

Formula 24 (display):
```latex
\sigma_{i-1}E_{i-1}=\mathrm{Env}(\underset{\substack{\Vert\\s_0}}{\sigma_{i-1}s_0},\ldots,\underset{\substack{\Vert\\s_{i-2}}}{\sigma_{i-1}s_{i-2}},\underset{\substack{\uparrow\\E_{i-1}}}{\sigma_{i-1}s_{i-1}})\subset E_{i-1}
```

Formula 25 (inline):
```latex
\sigma_{i-1}E_{i-1}=E_{i-1}
```

Formula 26 (inline):
```latex
\sigma_{i-1}E_i=E_i
```

Formula 27 (inline):
```latex
s_{i-1}\in E_{i-1}
```

Formula 28 (inline):
```latex
\subset E_i
```

Formula 29 (inline):
```latex
\sigma_{i-1}(s_{i-1})\subset E_i
```

Formula 30 (inline):
```latex
s_i\in E_i
```

Formula 31 (inline):
```latex
s_i\notin E_{i-1}
```

Formula 32 (inline):
```latex
E_i=\mathrm{Env}(E_{i-1},s_i)
```

Formula 33 (inline):
```latex
h>i
```

Formula 34 (inline):
```latex
i<h\leq n
```

Formula 35 (display):
```latex
\sigma_hs_i=\sigma_h\sigma_{i-1}s_{i-1}=\sigma_{i-1}(\sigma_hs_{i-1})\overset{\text{réc}}{=}\sigma_{i-1}(s_{i-1})=s_i
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 11-14:
```latex
\unsure{+1}
```

`\deleted` — lines 25-28:
```latex
$h>i$
```

`\inserted` — lines 11-14:
```latex
\uline{pour $\unsure{i}$, $0\leq i\leq n+1$}
```

`\inserted` — lines 15-17:
```latex
$i\geq1$ et
```

`\inserted` — lines 18-20:
```latex
$\sigma_{\unsure{h|k}}s_i=s_i$ pr $i<h\leq n$
```

`\inserted` — lines 25-28:
```latex
$i<h\leq n$
```
- `\margin`: none.
- `\handwritten`: none.

`\uline` — top heading:
```latex
$n$-Quasi-polyèdres réguliers en coordonnées can.
```

`\uline` — lines 11-14:
```latex
Prop
```

`\uline` — lines 11-14:
```latex
pour $\unsure{i}$, $0\leq i\leq n+1$
```
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_j ; _i ; _i ; _j ; _i ; _j ; _j ; _i ; _i ; _i ; _i ; _{i-1} ; _{i-1} ; _i ; _i ; _i ; _i ; _i ; _i ; _{i-1} ; _{i-1} ; _i ; _{i-1} ; _i ; _i ; _i ; _i ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _j ; _j ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-2} ; _{i-1} ; _{i-2} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _i ; _i ; _{i-1} ; _{i-1} ; _i ; _{i-1} ; _{i-1} ; _i ; _i ; _i ; _i ; _{i-1} ; _i ; _{i-1} ; _i ; _i ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _{i-1} ; _i
```

## Scan 31
Start (UTC): 2026-11-17T23:55:25+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:55:58+00:00  
End (UTC): 2026-11-17T23:58:55+00:00

### Independent words and accents from the crops
Crop-first prose: ‘On utilise les s_i … comme base de E, de/donc s0 comme origine, et les’; ‘comme base de l’espace des translations V de E.’ ‘On veut expliciter les matrices (à n+2 lignes et n+2 colonnes) des sigma_i … Revient à la connaissance des sigma_i s_j … Je dis qu’il suffit de connaître’; ‘Car on a’ with a crossed short continuation; ‘Car … donc’; ‘Posons’; ‘de sorte qu’on obtient si j≥i+3’; ‘i.e.’. Accents on à and connaître; translations has compressed medial letters, but a long initial t and final tions.

### Independent visual observations
Displays(7),(8),(9), and two labelled(10). u_i is inserted above the first equality in(8), with sigma_i²s_i below; v_i/nu_i is ambiguous. Five rows in(9), with two affine-envelope conditions to the right and an arrow inserting0≤i≤n−1 beside the v_i row. The j≥i+3 qualifier has an overwritten start. A cancelled sigma_i s_i+1=s0+ precedes the coordinate definitions. Component sums start at1 in the definitions but0 in the next two displayed expansions. One v component looks v_i,k while its paired basis factor is e_h. In the final coordinate tuple j is written above the displaced v_i,i+2. The first tuple component’s last index is small and must be enlarged to distinguish1/j. A cancelled trailing letter follows the last e_j. No margin prose or script/blackboard capital.

### Comparison and changes
No further changes after the independent crop comparison. Enlargements confirm the first tuple component as v_{i,1}; the overwritten final bound is i+2, while the earlier bound is marked unsure i+3. The cancelled mark after the final e_j remains an unsure n.

### Detailed checks
Compared every sentence, accent, inline expression and displayed row. Checked all i/j/h/k indices, comma indices, the u/v distinction, the annotation sigma_i^2 s_i, the inserted bound 0<=i<=n-1, and every cancelled fragment. The two lower summation bounds 0, the k|h coefficient index, and the repeated equation label (10) are retained exactly; no correction from the preceding definitions was made. No margin text or diagram is present apart from line-adjacent insertions already recorded.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (inline):
```latex
s_i
```

Formula 2 (inline):
```latex
0\leq i\leq n+1
```

Formula 3 (inline):
```latex
E
```

Formula 4 (inline):
```latex
s_0
```

Formula 5 (display):
```latex
e_i=s_i-s_0\qquad1\leq i\leq n+1\tag*{(7)}
```

Formula 6 (inline):
```latex
V
```

Formula 7 (inline):
```latex
E
```

Formula 8 (inline):
```latex
n+2
```

Formula 9 (inline):
```latex
n+2
```

Formula 10 (inline):
```latex
\sigma_i
```

Formula 11 (inline):
```latex
0\leq i\leq n
```

Formula 12 (inline):
```latex
\sigma_is_j
```

Formula 13 (inline):
```latex
0\leq i\leq n
```

Formula 14 (inline):
```latex
0\leq j\leq n+1
```

Formula 15 (display):
```latex
\underset{\substack{\Vert\\\sigma_i^2s_i}}{\sigma_is_{i+1}}=\inserted{u_i},\quad\sigma_is_{i+2}=\unsure{v_i|\nu_i}\tag*{(8)}
```

Formula 16 (display):
```latex
\left\{\begin{aligned}
&\sigma_is_j=s_j\quad\text{si }0\leq j<i\\
&\sigma_is_i=s_{i+1}\\
&\sigma_is_{i+1}=u_i\in E_{i+1}\qquad E_{i+1}=\mathrm{Env}(E_{i-1},s_{i+1},u_i)\\
&\sigma_is_{i+2}=v_i\in E_{i+2}\qquad E_{i+2}=\mathrm{Env}(E_{i+1},v_i)\quad\inserted{(0\leq i\leq n-1)}\\
&\sigma_is_j=\sigma_{j-1}\cdots\sigma_{i+2}(v_i)\quad\deleted{\unsure{k}}\ \text{si }\unsure{i+3}\leq j\leq n+1
\end{aligned}\right.\tag*{(9)}
```

Formula 17 (inline):
```latex
s_j=\sigma_{j-1}\cdots\sigma_{i+2}s_{i+2}
```

Formula 18 (display):
```latex
\sigma_is_j=\sigma_i\sigma_{j-1}\cdots\sigma_{i+2}s_{i+2}=\sigma_{j-1}\cdots\sigma_{i+2}\underset{v_i}{\underline{\sigma_is_{i+2}}}
```

Formula 19 (display):
```latex
\deleted{\sigma_is_{i+1}=s_0+}
```

Formula 20 (display):
```latex
\left\{\begin{aligned}
u_i&=(u_{i,1},\ldots,u_{i,i+1})=s_0+\sum_{1\leq\deleted{\unsure{k}}h\leq i+1}u_{i,h}e_h\\
v_i&=(v_{i,1},\ldots,v_{i,i+2})=s_0+\sum_{1\leq h\leq i+2}v_{i,h}e_h
\end{aligned}\right.\tag*{(10)}
```

Formula 21 (inline):
```latex
j\geq i+3
```

Formula 22 (display):
```latex
\begin{aligned}
\sigma_is_j&=\sigma_{j-1}\cdots\sigma_{i+2}(s_0+v_{i,1}e_1+\cdots+v_{i,i+1}e_{i+1}+v_{i,i+2}e_{i+2})\\
&=s_0+\sum_{0\leq h\leq i+1}v_{i,\unsure{k|h}}e_h+v_{i,i+2}e_j
\end{aligned}
```

Formula 23 (display):
```latex
\left\{\begin{aligned}
\sigma_is_j&=(v_{i,1},\ldots,v_{i,i+1},0,\ldots,0,\overset{j}{v_{i,i+2}},0,\ldots,0)\\
&=s_0+\sum_{0\leq h\leq i+1}v_{i,h}e_h+v_{i,i+2}e_j\deleted{\unsure{n}}\qquad\text{si }i+2\leq j\leq n+1
\end{aligned}\right.\tag*{(10)}
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 11-15:
```latex
\unsure{a}
```

`\deleted` — lines 11-15:
```latex
\unsure{k}
```

`\deleted` — lines 18-20:
```latex
\sigma_is_{i+1}=s_0+
```

`\deleted` — lines 18-20:
```latex
\unsure{k}
```

`\deleted` — bottom, lines 24-26:
```latex
\unsure{n}
```

`\inserted` — lines 9-10:
```latex
u_i
```

`\inserted` — lines 11-15:
```latex
(0\leq i\leq n-1)
```
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _i ; _i ; _i ; _i ; _j ; _i ; _i ; _i ; _{i+1} ; _i ; _i ; _{i+2} ; _i ; _i ; _i ; _j ; _j ; _i ; _i ; _{i+1} ; _i ; _{i+1} ; _i ; _{i+1} ; _{i+1} ; _{i-1} ; _{i+1} ; _i ; _i ; _{i+2} ; _i ; _{i+2} ; _{i+2} ; _{i+1} ; _i ; _i ; _j ; _{j-1} ; _{i+2} ; _i ; _j ; _{j-1} ; _{i+2} ; _{i+2} ; _i ; _j ; _i ; _{j-1} ; _{i+2} ; _{i+2} ; _{j-1} ; _{i+2} ; _i ; _i ; _{i+2} ; _i ; _{i+1} ; _i ; _{i,1} ; _{i,i+1} ; _{i,h} ; _i ; _{i,1} ; _{i,i+2} ; _{1\leq h\leq i+2} ; _{i,h} ; _i ; _j ; _{j-1} ; _{i+2} ; _{i,1} ; _{i,i+1} ; _{i+1} ; _{i,i+2} ; _{i+2} ; _{0\leq h\leq i+1} ; _{i,i+2} ; _j ; _i ; _j ; _{i,1} ; _{i,i+1} ; _{i,i+2} ; _{0\leq h\leq i+1} ; _{i,h} ; _{i,i+2} ; _j
```

## Scan 32
Start (UTC): 2026-11-17T23:58:55+00:00  
Independent crop notes saved (UTC): 2026-11-17T23:59:38+00:00  
End (UTC): 2026-11-18T00:00:42+00:00

### Independent words and accents from the crops
Read independently: 'compte tenu que, pr'; 'On a plus explicitement'; cancelled heading resembling 'Commutation'; 'Points fixes de'; 'C’est une réflexion projective ssi les dernières relations sont conséquence de la première homogénéisée, ou encore ssi'; 'Il reste pour'; 'les paramètres libres'; 'soit'. Accents inspected on réflexion, dernières, conséquence, première, homogénéisée and paramètres; the middles and endings of the final prose are compressed and require explicit doubt where unresolved. No quotation marks; bottom-corner 31 is archival only.

### Independent visual observations
The upper (11) is one long brace with several internal braces and a separate bracket around the sigma_0 e_{i+2} block. The first row has 1<=j<i; the second has (si i>=1) and cancelled marks. A u_i-s_0 attempt is cancelled before the two branches; u_0-s_1=(u_0-s_0)-e_1 in the i=0 branch. The bracketed block visibly starts sigma_0 e_{i+2}, then has v_0-s_1 and a second v_0-like index before the general sum. Last branch condition i+2<=j<=n+1 is inserted below with a curved pointer. Middle matrix has row/column numbers, repeated v_01-1 entries, a terminal 1, zeros and v_02 diagonal entries, crossed overwrites and a horizontal separator. Equation (13) annotates Sigma_0 by x_2+...+x_{n+1}; (14) visibly has Sigma_1. Equation (15) returns to Sigma_0, annotated again. Boxed v_02=1; lambda_0 and mu_0 are named parameters. No double-struck alphabet or handwriting on type, no independent margin note.

### Comparison and changes
Cancelled sigma_i e_{i+2}=v_0-s_1 -> cancelled sigma_i e_{i+2}={v_0-s_1: restored the visible opening brace. The v_0|nu_0 recurring-glyph doubt was moved to that first occurrence, and its later repeated occurrence now uses v_0. Matrix column labels 1, 2, n+1, n+2 -> underlined labels, matching their visible horizontal strokes. No other change.

### Detailed checks
Compared all prose and every row of (11), including the 0/i index discrepancy, cancelled attempts, plus-sign overwrite, internal brackets and inserted terminal range. Read matrix (12) row by row, including seven written rows, the blank continuation column, all zeros, diagonal v_02 entries, overwritten marks, row labels and horizontal separator. Compared (13)-(15), the Sigma_0 annotations and the apparently different Sigma_1 in (14). Checked all i/j indices, u/v shapes, Greek lambda and mu, accents and the final boxed condition. The compressed homogénéisée remains unsure. No typed addition, independent marginal note, diagram or drawing.

### Formula ledger
Every inline formula and display below was compared with the crops in this reading. Indices remain visible in the literal TeX; no algebraic normalization has been applied.

Formula 1 (inline):
```latex
0\leq i\leq n\deleted{\unsure{+1}}
```

Formula 2 (inline):
```latex
\sigma_i e_i=e_{i+1}
```

Formula 3 (display):
```latex
\left\{\begin{aligned}
&\sigma_i e_j=e_j\quad\text{si }1\leq j<i\\
&\sigma_i e_i=e_{i+1}\ \deleted{\unsure{s}}\quad(\text{si }i\geq1)\deleted{\unsure{\leq n}}\\
&\sigma_i e_{i+1}=\deleted{\unsure{u_i-s_0}}\left\{\begin{aligned}
&u_0-s_1=(u_0-s_0)\deleted{\unsure{+}}-e_1=(u_{01}-1)e_1&&\text{si }i=0\\
&u_i-s_0=\sum_{1\leq h\leq i+1}\deleted{\unsure{u_{i,1}}}u_{i,h}e_h&&\text{si }i\geq1
\end{aligned}\right.\\
&\deleted{\unsure{\sigma_i e_{i+2}}=\{\unsure{v_0|\nu_0}-s_1}\\
&\left[\sigma_0 e_{i+2}=\left\{\begin{aligned}
&v_0-s_1=(v_0-s_0)-e_1=(v_{01}-1)e_1+v_{02}e_2&&\text{si }i=0\\
&\unsure{v_0|v_i}-s_0=\sum_{1\leq h\leq i+2}v_{i,h}e_h&&\text{si }i\geq1
\end{aligned}\right.\right]\\
&\sigma_i e_j=\left.\left\{\begin{aligned}
&(v_{01}-1)e_1+v_{02}e_j\ \deleted{\unsure{+}}&&\text{si }i=0\\
&\deleted{\unsure{v_{i,1}}}\sum_{1\leq h\leq i+1}v_{i,h}e_h+v_{i,i+2}e_j&&\text{si }i\geq1
\end{aligned}\right.\right\}\ \deleted{\unsure{j}}\ \inserted{\text{si }i+2\leq j\leq n+1}
\end{aligned}\right.\tag*{(11)}
```

Formula 4 (inline):
```latex
\sigma_0
```

Formula 5 (display):
```latex
\deleted{\unsure{\overline{\sigma}_0}=}\quad\sigma_0=
\begin{array}{r@{}l}
&\begin{array}{ccccccc}\underline{1}&\underline{2}&&&&\underline{n+1}&\underline{n+2}\end{array}\\[-.5ex]
\begin{array}{r}1\\2\\\\\\\\n+1\\n+2\end{array}&
\left(\begin{array}{ccccccc}
u_{01}-1&v_{01}-1&v_{01}-1&v_{01}-1&&v_{01}-1&1\\
0&v_{02}&\deleted{\unsure{u_{01}}}0&0&&0&0\\
\deleted{\unsure{1}}0&0&v_{02}&0&&0&0\\
0&\unsure{0}&0&v_{02}&&0&0\\
\hline
0&0&0&0&&\deleted{\unsure{1}}0&0\\
0&0&0&0&&v_{02}&0\\
0&0&0&0&&0&1
\end{array}\right)
\end{array}\tag*{(12)}
```

Formula 6 (display):
```latex
\sigma_0(x_1,\ldots,x_{n+1})=\bigl(1+(u_{01}-1)x_1+(v_{01}-1)\overset{\substack{x_2+\cdots+x_{n+1}\\\Vert}}{\Sigma_0},v_{02}x_2,\ldots,v_{02}x_{n+1}\bigr)\tag*{(13)}
```

Formula 7 (display):
```latex
H_0:\left\{\begin{aligned}
&1+(u_{01}-2)x_1+(v_{01}-1)\Sigma_1=0\\
&(v_{02}-1)x_2=\cdots=(v_{02}-1)x_{n+1}=0
\end{aligned}\right.\tag*{(14)}
```

Formula 8 (inline):
```latex
\boxed{v_{02}=1}
```

Formula 9 (inline):
```latex
\sigma_0
```

Formula 10 (inline):
```latex
u_{01},v_{01}
```

Formula 11 (inline):
```latex
\lambda_0
```

Formula 12 (inline):
```latex
\mu_0
```

Formula 13 (display):
```latex
\sigma_0(x_1,\ldots,x_{n+1})=\bigl(1+(\lambda_0-1)x_1+(\mu_0-1)\overset{\substack{x_2+\cdots+x_{n+1}\\\Vert}}{\Sigma_0},x_2,\ldots,x_{n+1}\bigr)\tag*{(15)}
```

### Corrections, margins and line-adjacent text ledger

`\deleted` — lines 1-2:
```latex
\unsure{+1}
```

`\deleted` — lines 3-11:
```latex
\unsure{s}
```

`\deleted` — lines 3-11:
```latex
\unsure{\leq n}
```

`\deleted` — lines 3-11:
```latex
\unsure{u_i-s_0}
```

`\deleted` — lines 3-11:
```latex
\unsure{+}
```

`\deleted` — lines 3-11:
```latex
\unsure{u_{i,1}}
```

`\deleted` — lines 3-11:
```latex
\unsure{\sigma_i e_{i+2}}=\{\unsure{v_0|\nu_0}-s_1
```

`\deleted` — lines 3-11:
```latex
\unsure{+}
```

`\deleted` — lines 3-11:
```latex
\unsure{v_{i,1}}
```

`\deleted` — lines 3-11:
```latex
\unsure{j}
```

`\deleted` — lines 12-13:
```latex
\unsure{Commutation}
```

`\deleted` — matrix, lines 14-20:
```latex
\unsure{\overline{\sigma}_0}=
```

`\deleted` — matrix, lines 14-20:
```latex
\unsure{u_{01}}
```

`\deleted` — matrix, lines 14-20:
```latex
\unsure{1}
```

`\deleted` — matrix, lines 14-20:
```latex
\unsure{1}
```

`\inserted` — lines 3-11:
```latex
\text{si }i+2\leq j\leq n+1
```
- `\margin`: none.
- `\handwritten`: none.
- `\diagram`: none.
- `\figure`: none.

### Index and alphabet record
All i/j-bearing subscripts and superscripts appearing in the formula ledger were checked in place. The following exact strings preserve repeats and surrounding punctuation:
```text
_i ; _i ; _{i+1} ; _i ; _j ; _j ; _i ; _i ; _{i+1} ; _i ; _{i+1} ; _i ; _i ; _{1\leq h\leq i+1} ; _{i,1} ; _{i,h} ; _i ; _{i+2} ; _{i+2} ; _i ; _{1\leq h\leq i+2} ; _{i,h} ; _i ; _j ; _j ; _{i,1} ; _{1\leq h\leq i+1} ; _{i,h} ; _{i,i+2} ; _j
```


## Supplementary reconciliation: scans 17–18

Start: see progress.log supplementary reconciliation entry. End (UTC): 2026-11-18T00:02:12+00:00

All six thirds were re-viewed, with particular attention to the cancelled prose, the first equations, accents, bars on Sigma, indices and the crowded lower matrix on scan 18. Scan 17 correction: `\unsure{Si l'on est sur un corps}` -> `\deleted{\unsure{Si}} Sur un corps`. The earlier audit recorded this intended correction, but the literal page file still contained the earlier reading; the change is now applied and verified. The crop shows a cancelled short word followed by “Sur un corps”. No other change. Scan 18: no change; checked every inline formula and the display rows against the existing formula ledger, the lower i omitted on some Sigmas, the paired lambda indices, the alpha index and signs in both matrix rows, the dimension annotations and crossed entries.

## Final notation and inventory reconciliation

Completed (UTC): 2026-11-18T00:06:02+00:00

Compared the recurring sigma/lambda/alpha, barred or unbarred Sigma, u/v/nu, f/fraktur f, b/s, delta/d, h/l, and h/k records across their cited page crops and audit ledgers. Kept the image-supported differences: Greek nu first on scans 19, 20 and 24; Latin v first on scans 31–32; k in scan 30’s proposition but h|k in the proof. Refreshed the table’s scan-21 b_1 entry to match the first-occurrence-only rule. No additional transcription change. All inventory rows were regenerated from the final page files, including every display, diagram and state macro, and ordered by their source positions; the final inventory has 251 elements, all marked yes. No authorial page numbers or double-struck typed letters were identified.

Final inventory boundary check (2026-11-18T00:07:02+00:00): trailing paragraphs at page ends are included; 251 rows, all yes.

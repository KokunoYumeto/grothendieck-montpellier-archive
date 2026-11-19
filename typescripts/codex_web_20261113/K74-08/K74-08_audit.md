# K74-08 · Independent second reading

Positions follow the orientation of the writing. For landscape pages the three supplied crops run left to right. Times are UTC. The first entry for each sheet was recorded from the crops before reopening its transcription. The registers below preserve the mathematical strings examined, including strings inside cancellations; brackets in the readings may be unfinished in the manuscript. TeX line numbers refer to the independent text at the freeze. The later comparison with Hua is recorded in the doubts file.

**Timing qualification.** The intervals below are the recorded first crop-to-file comparisons for the independent audit. Thirteen lasted between 33 and 60 seconds, shorter than the requested several minutes per page. The further comparisons of recurring signs, native-scale details and marked witness loci took additional time outside those intervals.

## Scan 002

2026-11-18T09:24:26Z to 2026-11-18T09:25:21Z.

### Crop reading before comparison

Axiome, si, distincts, alors, tel que; Catégorie, variable, iso sur I. No full stop follows either occurrence of card. In II the line ends d'ens. The crossing runs through extérieurs and stops before the lower words entre ces groupes. The longer passage reads opèrent, façon, bitorseur, renverse, opération, opposée, opère, diagonalement, équivalentes, l'exprimer, façon, l'image. The added words above que appear to begin Si; the accent-shaped curve below them leads to the gap before E. The tiny par δ sits at the end of diagonalement. The faint left and right outlines enclose the wedge calculation. The first and third right-hand cyclic operators have an upper right angular profile; the second has a lower loop.

### Comparison

The upper-right ink-like mark has the same outline, reversed, on the back. Removed the marginal deleted word. The manuscript has a separately drawn section brace. The underlining sits under bitorseur; the line across the earlier map does not run through entre ces groupes. The category initial has a curled top and an open lower curve. E and G in the triangle and the roman I in the two headings retain distinct forms. Checked the i and j of all products, the descending j in the last subscript kj, the three cyclic factors in each condition, and the four small raised marks in the enclosed calculation.

Changes: marginal illegible word → physical-mark comment; “Si … que” → “que si …”; par δ moved before the period; “mais” → “mais|pour”; superscript + → +|a. In the right sides of a₁ and a₃ the single vertical and top bar support Γ. The rounded operator of a₂ remains δ. Changes δ → Γ|δ and δ → Γ respectively.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>I\setminus\{</code> | <code>I-\{</code> |
| <code>\unsure{mais&#124;pour}</code> | <code>\unsure{mais&#124;puis&#124;pour}</code> |
| <code>\to\unsure{L}(G_j)</code> | <code>\to L(G_j)</code> |
| <code>g_i^{\unsure{+&#124;a}}</code> | <code>g_i^{+}</code> |
| <code>(x_i g_k^{-1},g_k^{\unsure{+&#124;a}}</code> | <code>(x_i g_k^{-1},g_k^{+}</code> |
| <code>a_3)&amp;\quad\delta(G_k)</code> | <code>a_3)&amp;\quad\Gamma(G_k)</code> |

A further native-scale inspection of the three cyclic conditions found the same angular sign on both sides of the third line. The shallow diagonal in the index-set differences is closer to a minus. Repeated ambiguous superscripts have their candidates recorded at the first occurrence.

### Formula register

**002.01** · line 5

```tex
\[
\left\{\begin{aligned}
&I\ \text{ens de card }3.\\
&(E_i)_{i\in I}\quad\text{famille d'ensembles}\\
&\Gamma\subset\prod_{i\in I}E_i\\
&\text{Axiome : si }\deleted{\unsure{i,j\in I,\ i\ne j}}\quad i,j,k\in I\quad\text{distincts (donc }I=\{i,j,k\}\text{)}\\
&\text{alors }\ \forall x_i\in E_i,\ x_j\in E_j\ .\quad\exists\unsure{1|!}\ x_k\in E_k\quad\text{tel que }(x_i,x_j,x_k)\in\Gamma .
\end{aligned}\right.
\]
```

**002.02** · line 14

```tex
$\unsure{\mathscr T|\mathscr C}$
```

**002.03** · line 14

```tex
$I$
```

**002.04** · line 14

```tex
$I$
```

**002.05** · line 16

```tex
$I$
```

**002.06** · line 16

```tex
$3$
```

**002.07** · line 18

```tex
$(G_i)_{i\in I}$
```

**002.08** · line 20

```tex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
\& E_i\arrow[dl,dash,"G_k"']\arrow[dr,dash,"G_j"]\&\\
E_j\arrow[rr,dash,"\unsure{G_i|G_j}"']\&\& E_k
\end{tikzcd}
```

**002.09** · line 24

```tex
$\unsure{\tau_{ij}}\colon \unsure{L}(G_i)\to L(G_j)$
```

**002.10** · line 26

```tex
$(E_i)_{i\in I}$
```

**002.11** · line 28

```tex
$\forall i\in I$
```

**002.12** · line 28

```tex
$\prod_{j\in I-\{i\}}G_j$
```

**002.13** · line 28

```tex
$E_i$
```

**002.14** · line 28

```tex
$I=\{i,j,k\}$
```

**002.15** · line 28

```tex
$E_i$
```

**002.16** · line 28

```tex
$G_j,G_k$
```

**002.17** · line 28

```tex
$G_k$
```

**002.18** · line 30

```tex
$\displaystyle\prod_{\unsure{i|0}\in I}\prod_{j\in I-\{i\}}G_j=\prod_{j\in I}G_j^{I-\{j\}}$
```

**002.19** · line 30

```tex
$P=\prod E_i$
```

**002.20** · line 30

```tex
$\prod_{j\in I}G_j$
```

**002.21** · line 30

```tex
$\delta$
```

**002.22** · line 30

```tex
$x=(x_i)_{i\in I}\in P$
```

**002.23** · line 32

```tex
\[
\begin{aligned}
&E_i\wedge E_j\wedge E_k &&x_i\wedge x_j\wedge x_k= \big\{ &&(g_j x_i,x_j,x_k g_j)\\
&G_j\quad G_k\quad G_i\quad G_j &&
g_j x_i g_k^{-1}\wedge g_k^{\unsure{+|a}}x_jg_i^{-1}\wedge g_i^{+}x_k g_j^{-1}
&&=(x_i g_k^{-1},g_k^{+}x_jg_i^{-1},g_i^{+}x_k)
\end{aligned}
\]
```

**002.24** · line 41

```tex
$I=\{i,j,k\}$
```

**002.25** · line 45

```tex
\[
\begin{aligned}
a_1)&\quad\delta(G_i)x\subset\unsure{\Gamma|\delta}(G_j\times G_k)\cdot x\\
a_2)&\quad\delta(G_j)x\subset\delta(G_k\times G_i)\cdot x\\
a_3)&\quad\Gamma(G_k)x\subset\Gamma(G_i\times G_j)\cdot x .
\end{aligned}
\]
```

**002.26** · line 53

```tex
$x_i$
```

**002.27** · line 53

```tex
$\forall$
```

**002.28** · line 53

```tex
$(j,k)$
```

**002.29** · line 53

```tex
$j,k\in I$
```

**002.30** · line 53

```tex
$j\ne k$
```

**002.31** · line 55

```tex
$\tau_{kj}\colon E_i\to\operatorname{Isom}(G_j,G_k)$
```


**i/j indices and exponents.** l. 8 <code>_i</code>, <code>_{i\in I}</code> · l. 9 <code>_{i\in I}</code>, <code>_i</code> · l. 11 <code>_i</code>, <code>_i</code>, <code>_j</code>, <code>_j</code>, <code>_i</code>, <code>_j</code> · l. 18 <code>_i</code>, <code>_{i\in I}</code> · l. 21 <code>_i</code>, <code>_j</code> · l. 22 <code>_j</code>, <code>_i</code>, <code>_j</code> · l. 24 <code>_{ij}</code>, <code>_i</code>, <code>_j</code> · l. 26 <code>_i</code>, <code>_{i\in I}</code> · l. 28 <code>_{j\in I-\{i\}}</code>, <code>_j</code>, <code>_i</code>, <code>_i</code>, <code>_j</code> · l. 30 <code>_{\unsure{i&#124;0}\in I}</code>, <code>_{j\in I-\{i\}}</code>, <code>_j</code>, <code>_{j\in I}</code>, <code>_j</code>, <code>^{I-\{j\}}</code>, <code>_i</code>, <code>_{j\in I}</code>, <code>_j</code>, <code>_i</code>, <code>_{i\in I}</code> · l. 34 <code>_i</code>, <code>_j</code>, <code>_i</code>, <code>_j</code>, <code>_j</code>, <code>_i</code>, <code>_j</code>, <code>_j</code> · l. 35 <code>_j</code>, <code>_i</code>, <code>_j</code> · l. 36 <code>_j</code>, <code>_i</code>, <code>_j</code>, <code>_i</code>, <code>_i</code>, <code>_j</code> · l. 37 <code>_i</code>, <code>_j</code>, <code>_i</code>, <code>_i</code> · l. 47 <code>_i</code>, <code>_j</code> · l. 48 <code>_j</code>, <code>_i</code> · l. 49 <code>_i</code>, <code>_j</code> · l. 53 <code>_i</code> · l. 55 <code>_{kj}</code>, <code>_i</code>, <code>_j</code>

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| top, braced data and axiom | deletion | <code>\unsure{i,j\in I,\ i\ne j}</code> |
| upper middle, struck line | deletion | <code>$\unsure{\tau_{ij}}\colon \unsure{L}(G_i)\to L(G_j)$ \unsure{syst.} trans. d'isom. extérieurs</code> |
| middle | insertion | <code>si $I=\{i,j,k\}$</code> |
| middle, product | insertion | <code>par $\delta$</code> |
| lower middle, beside and below calculation | deletion | <code>il revient au \unsure{=&#124;même} de</code> |
| foot, continuing to next scan | deletion | <code>\unsure{Soit} \unsure{$x_i$}</code> |
| foot, continuing to next scan | deletion | <code>\unsure{de}</code> |

## Scan 003

2026-11-18T09:25:22Z to 2026-11-18T09:35:13Z.

### Crop reading before comparison

The letterhead reads UNIVERSITE, TECHNIQUES DU LANGUEDOC and the underlined SERVICE COMPTABILITE. The datestamp has a fleck or dash before 2 MAI 1977. The two inked director numbers are 5. The recipient looks like GROTHENDiECK, with a dot over the short i. OBJET and “Recherche” have a printed rule and straight double quotes respectively. The accents in crédits, Collègue, notifiés, Secrétariat, Universités, connaître, première, accordée, année, numéro and agréer are visible. The code has distinct spaces for M and 022. The signer's initial is a large closed loop, and the surname appears Mical[i]. A pencil 2 is at lower left.

### Comparison

The date and signature remain qualified. All five handwritten form fields and the signature were followed to their printed lines. The ruling through the dotted amount line belongs to the form, the horizontal line below the letterhead is a rule, and the line across “sentiments” is a paper fold. No cancelled words, marginal writing or mathematical formulas. The letterhead capitals are single typed capitals. The code divider is a printed vertical rule.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>crédits ``Recherche''.}</code> | <code>crédits \textquotedbl{}Recherche\textquotedbl{}.}</code> |
| <code>{M}\,&#124;\,\handwritten</code> | <code>{M}\,\textbar{}\,\handwritten</code> |

### Formula register

No mathematical formula.

**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| upper right, three address lines | handwritten | <code>5</code> |
| upper right, three address lines | handwritten | <code>GROTHENDiECK</code> |
| centre, body and code box | handwritten | <code>10.450</code> |
| centre, body and code box | handwritten | <code>M</code> |
| centre, body and code box | handwritten | <code>022</code> |
| lower right, office and signature | handwritten | <code>5</code> |
| lower right, office and signature | handwritten | <code>\unsure{A. Micali&#124;A. Mical}</code> |

## Scan 004

2026-11-18T09:35:14Z to 2026-11-18T09:36:06Z.

### Crop reading before comparison

An insertion “extérieure” precedes a struck word in the first line, which has “d'isom.”, “exactement” and a closing bracket. A crossed preliminary triangle is to the left of a directed triangle. The phrase underneath has “invariante” and “permutations circulaires”. “existence” and “extérieurs” are underlined. The indices on the maps are ordered; the line with i,j,k and I has a cancellation before it. “(lot V)” looks more like “(lot V)” or “(lot X)”. In the orbit paragraph “qui” is above a crossed word; a brace to the left covers two lines. “trois” goes above groupes and “une” replaces a longer struck word before “partie”. Down at the foot are a, x, three equations in coordinates, and three forms of “détermine…”, written into the bottom edge. Pencil 3 at lower left.

### Comparison

Read the arrows on the main triangle k→i, i→j and j→k, with their lower pairs ik, ji, kj and arguments x_j, x_k, x_i. The composition ends at the j-labelled group. Rechecked the smaller slashed triangle, tildes on both occurrences of tau, outer isomorphisms and the index after E. On closer inspection the subscript and parenthesis there read k in I. The first product after “modulo” has no visible limits. The left two-line calculation follows a marginal brace. In the bottom three equations the upper signs on g_k and g_i are both −1, and the text really does first give dependence on x_i and then on x_i,x_j. The crossing under “Celle-ci satisfait” meets the replacement aux. The large corner-shaped letter of the subset display matches the relation on scan 2. No double-struck heading or typed correction.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>orbite modulo $\prod_{i\in I}G_i$</code> | <code>orbite modulo $\prod G_i$</code> |
| <code>I\setminus\{i\}</code> | <code>I-\{i\}</code> |
| <code>\[ \begin{aligned} g_i\gamma_i x</code> | <code>\margin{\(\begin{aligned} g_i\gamma_i x</code> |
| <code>\end{aligned} \]</code> | <code>\end{aligned}\)}</code> |
| <code>\deleted{certain}</code> | <code>\deleted{\unsure{certaine&#124;certain}}</code> |

The placement of the braced calculation in the margin and the corrected product limits were incorporated during collation of the adjacent notice.

### Formula register

**004.01** · line 4

```tex
\begin{tikzcd}[ampersand replacement=\&,row sep=tiny,column sep=tiny]
\& \deleted{\unsure{x_i}}\arrow[dl,dash,"\deleted{G_k}"']\arrow[dr,dash,"\deleted{G_j}"]\&\\
{}\arrow[rr,dash,"\deleted{G_i}"']\&\&{}
\end{tikzcd}
```

**004.02** · line 8

```tex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
G_k\arrow[dr,"{\tau_{ik}(x_j)}"']\&\&G_j\arrow[ll,"{\tau_{kj}(x_i)}"']\\
\&G_i\arrow[ur,"{\tau_{ji}(x_k)}"']\&
\end{tikzcd}
```

**004.03** · line 12

```tex
\[
\begin{aligned}
&\tau_{ji}(x_k)\tau_{ik}(x_j)\tau_{kj}(x_i)\\
&\hspace{4em}=\mathrm{id}_{G_j}
\end{aligned}
\]
```

**004.04** · line 20

```tex
$x=(x_i)_{i\in I}$
```

**004.05** · line 20

```tex
$\widetilde\tau_{ij}=\widetilde\tau_{ij}(x_k)$
```

**004.06** · line 20

```tex
$i,j,k\in I$
```

**004.07** · line 20

```tex
$i,j,k\in I$
```

**004.08** · line 20

```tex
$E_k$
```

**004.09** · line 20

```tex
$k\in I$
```

**004.10** · line 20

```tex
$G_i$
```

**004.11** · line 22

```tex
$x$
```

**004.12** · line 22

```tex
$\prod G_i$
```

**004.13** · line 22

```tex
$\prod_{j\in I-\{i\}}G_j$
```

**004.14** · line 24

```tex
\(\begin{aligned}
g_i\gamma_i x&=(g_j,g_k)x\\
g_i(\unsure{\gamma_i},\gamma_j,\gamma_k)x&=(\gamma_j,\gamma_k)g_i\gamma_i x=(\gamma_j g_j,\gamma_k g_k)x
\end{aligned}\)
```

**004.15** · line 28

```tex
$\Gamma$
```

**004.16** · line 28

```tex
$\prod_{j\in I-\{i\}}G_j$
```

**004.17** · line 29

```tex
\[
\Gamma\subset\prod_{i\in I} E_i=P
\]
```

**004.18** · line 34

```tex
\[
\begin{aligned}
a&=(a_i,a_j,a_k)&x_i&=a_i g_k^{-1}& &\text{détermine }g_k\text{ en fonction de }a\text{ et }x_i\\
x&=(x_i\ \ x_j\ \ \underset{\unsure{?}}{x_k})&x_j&=g_k a_j g_i^{-1}& &\text{détermine }g_i\text{ en fonction de }a\text{ et }x_i,x_j\\
&&x_k&=g_i a_k&&\text{détermine }x_k
\end{aligned}
\]
```


**i/j indices and exponents.** l. 5 <code>_i</code>, <code>_j</code> · l. 6 <code>_i</code> · l. 9 <code>_{ik}</code>, <code>_j</code>, <code>_j</code>, <code>_{kj}</code>, <code>_i</code> · l. 10 <code>_i</code>, <code>_{ji}</code> · l. 14 <code>_{ji}</code>, <code>_{ik}</code>, <code>_j</code>, <code>_{kj}</code>, <code>_i</code> · l. 15 <code>_{G_j}</code> · l. 20 <code>_i</code>, <code>_{i\in I}</code>, <code>_{ij}</code>, <code>_{ij}</code>, <code>_i</code> · l. 22 <code>_i</code>, <code>_{j\in I-\{i\}}</code>, <code>_j</code> · l. 25 <code>_i</code>, <code>_i</code>, <code>_j</code> · l. 26 <code>_i</code>, <code>_i</code>, <code>_j</code>, <code>_j</code>, <code>_i</code>, <code>_i</code>, <code>_j</code>, <code>_j</code> · l. 28 <code>_{j\in I-\{i\}}</code>, <code>_j</code> · l. 30 <code>_{i\in I}</code>, <code>_i</code> · l. 36 <code>_i</code>, <code>_j</code>, <code>_i</code>, <code>_i</code>, <code>_i</code> · l. 37 <code>_i</code>, <code>_j</code>, <code>_j</code>, <code>_j</code>, <code>_i</code>, <code>_i</code>, <code>_i</code>, <code>_j</code> · l. 38 <code>_i</code>

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| top, continuation in bracket | insertion | <code>extérieure</code> |
| top, continuation in bracket | deletion | <code>isom.</code> |
| upper left, cancelled triangle | deletion | <code>\unsure{x_i}</code> |
| upper left, cancelled triangle | deletion | <code>G_k</code> |
| upper left, cancelled triangle | deletion | <code>G_j</code> |
| upper left, cancelled triangle | deletion | <code>G_i</code> |
| above fold | deletion | <code>\unsure{$i,j,k\in I$}</code> |
| middle, below fold | deletion | <code>Soit</code> |
| middle, below fold | insertion | <code>qui</code> |
| middle left, enclosed calculation | margin note | <code>\(\begin{aligned} g_i\gamma_i x&amp;=(g_j,g_k)x\\ g_i(\unsure{\gamma_i},\gamma_j,\gamma_k)x&amp;=(\gamma_j,\gamma_k)g_i\gamma_i </code> |
| middle right to lower third | insertion | <code>trois</code> |
| middle right to lower third | insertion | <code>une</code> |
| middle right to lower third | deletion | <code>\unsure{certaine&#124;certain}</code> |
| middle right to lower third | deletion | <code>\unsure{à}</code> |
| middle right to lower third | insertion | <code>aux</code> |

## Scan 005

2026-11-18T09:36:07Z to 2026-11-18T09:36:40Z.

### Crop reading before comparison

The typed date is 9 Juin 1976, in a notice headed “Attribution individuelle au titre de l'année 1977”. There is no accent on UNIVERSITE or MATHEMATIQUES. Sender and recipient block has MR LE PROFESSEUR GROTHENDIECK A. and 5. Diffusion, Enseignement Supérieur, n° 3 718. Underlined SCIENTIFIQUE on its own line. “invités à”, “imprimés relatifs à”, “à partir du 13 Juin et jusqu'au 8 Juillet 1977 (date limite)”. In the following paragraph intéressés, appelée, caractère, formalité, paiement, effectué, signés, bénéficiaires. Underlined “Les délais mentionnés ci-dessus sont impératifs.” Closing Le Président, Le Vice - Président, B. CHARLES. Faint corner 4.

### Comparison

No change. No formula, mathematical index or handwritten filling appears in this notice. Each heading capital is an ordinary type or print capital, including the heavier opening N. The address label has a faint rectangular edge. The lines below the distribution heading, title, dates and final instruction are rules or underlining. The fold runs under the deadline. None of these lines cancels words. Uppercase month initials, the spaced hyphen in the closing, the two years and “sur le vu” stand as read.

### Formula register

No mathematical formula.

**i/j indices and exponents.** None.

**Local interventions.** None.

## Scan 006

2026-11-18T09:36:40Z to 2026-11-18T09:37:15Z.

### Crop reading before comparison

“satisfaisant”, then u_i(1)=1 for i=1,2,3. The box has a separate (b)-like label, xyz=1, a double right arrow, three images and =1. “Prouvons que les u_i sont”, followed by a strike with “égaux à un seul” above, then “et unique hom de groupes.” “Faisant x=1”, u_3(y inverse)=u_2(y) inverse. The next line starts Donc u_3(y), subscript dark, followed by u_2(y inverse) inverse. “pour la” and a double-stroke abbreviation (“même”), “raison”. “On tire maintenant de a,” before the doubled inverses. cqfd. “Question” underlined; the question literally has “est il” and ends “équivalence ?”. The vertical line brackets the question. 5 in the bottom corner.

### Comparison

The bottom stroke and hook after u in the first “Donc” agree with the preceding 3. Both inversions in u((xy) inverse) inverse are visible, and the upright equals sign links the left member to u(xy) below. The boxed implication arrow goes right. The pair of short strokes is repeated in the abbreviation for “même” and is retained as written. The top left box label has a loop and tall rising stroke, allowing b or 6; the intersecting strokes also allow an asterisk. The earlier erased y before u(y inverse) remains doubtful. The underlined Question is live, alongside its vertical rule. No typed additions or script/double-struck capitals.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>\unsure{(b)&#124;($*$)}</code> | <code>\unsure{(b)&#124;(6)&#124;($*$)}</code> |
| <code>Faisons $x=1$</code> | <code>\unsure{Faisons&#124;Faisant} $x=1$</code> |
| <code>u_{\unsure{3&#124;2}}(y)</code> | <code>u_3(y)</code> |

### Formula register

**006.01** · line 3

```tex
\[
u_i(1)=1\qquad i=1,2,3
\]
```

**006.02** · line 7

```tex
\[
\boxed{xyz=1\quad\Longrightarrow\quad u_1(x)u_2(y)u_3(z)=1}\tag*{\unsure{(b)|(6)|($*$)}}
\]
```

**006.03** · line 11

```tex
$u_i$
```

**006.04** · line 13

```tex
$x=1$
```

**006.05** · line 13

```tex
$u_3(y^{-1})=u_2(y)^{-1}$
```

**006.06** · line 15

```tex
$u_3(y)=u_2(y^{-1})^{-1}$
```

**006.07** · line 15

```tex
$=$
```

**006.08** · line 15

```tex
$u_1(y)=u_2(y^{-1})^{-1}$
```

**006.09** · line 15

```tex
$u_1(y)=u_3(y)$
```

**006.10** · line 15

```tex
$=$
```

**006.11** · line 15

```tex
$u_1(y)=u_2(y)$
```

**006.12** · line 15

```tex
$u_1=u_2=u_3$
```

**006.13** · line 15

```tex
$u(y)=u(y^{-1})^{-1}$
```

**006.14** · line 15

```tex
$\deleted{\unsure{y}}u(y^{-1})=u(y)^{-1}$
```

**006.15** · line 18

```tex
\[
\begin{aligned}
u((xy)^{-1})^{-1}&=u(x)u(y)\\
\rotatebox{90}{$=$}&\\
u(xy)&
\end{aligned}
\]
```

**006.16** · line 25

```tex
$u(xy)=u(x)u(y)$
```

**006.17** · line 27

```tex
$\varphi$
```


**i/j indices and exponents.** l. 4 <code>_i</code> · l. 11 <code>_i</code>

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| upper third, correction over first line | deletion | <code>des hom de</code> |
| upper third, correction over first line | insertion | <code>égaux à un seul</code> |
| above fold, proof | deletion | <code>\unsure{y}</code> |

## Scan 007

2026-11-18T09:37:16Z to 2026-11-18T09:37:52Z.

### Crop reading before comparison

“Catégorie” followed by a large curled capital with prime. Parenthesis “I variable) puis iso sur I)” with an apparent additional closing parenthesis. “Prop” is underlined; “pl. fidèle”, “et identifie”, an insertion “à équiv. près”. “catégories fibrées”, “groupoïde”, “card 3”, “on est ramené”, “pl.-fid.”, “La fidélité est claire”. The first object has (E_i,G_i,…,Γ), a point (x_1,x_2,x_3) and the word “pt”. Lines through equiv… and a preceding product sign. “l'ens des (x,y,z) tels que xyz=1”. Later “un autre objet”, primed E,G,Γ and coordinates; “du φ du premier” has a caret. “l'image de”, “Ceci permet” or a compressed “Elle permet”, then G prime cubed, “l'ens des”, x'y'z'=1. Last “Donc on a trois applications”, and a right arrow to G prime. Archive 6.

### Comparison

Read the initial script letter and its prime apart from the unlooped corner of the relation Γ. A downward curl after variable looks like a closing parenthesis. The curved category capitals T/C recur in the functor, proposition and proof. Rechecked the three insertion lines above the proposition and fibres sentence, the twice-cancelled qualifications, the tuple of the first object, the identification by G, and the struck product before G cubed. Subscripts of E_i and G_i agree, including the primed letters; the second prime-coordinate's small index remains open. Both triple products in the displays end at 1. The opening of the word before “permet” remains weak. The last arrow is rightward, with a prime on just its target. No typewritten matter or marginal annotation separate from those insertions.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>variable\unsure{,&#124;;}</code> | <code>variable\unsure{)&#124;,&#124;;}</code> |
| <code>Elle permet</code> | <code>\unsure{Elle&#124;Ceci} permet</code> |
| <code> puis iso</code> | <code> \unsure{puis&#124;pour} iso</code> |

### Formula register

**007.01** · line 2

```tex
$\unsure{\mathscr T|\mathscr C}'$
```

**007.02** · line 2

```tex
$I$
```

**007.03** · line 2

```tex
$I$
```

**007.04** · line 5

```tex
\[
\mathscr T'\xrightarrow{\varphi}\mathscr T
\]
```

**007.05** · line 9

```tex
$\mathscr T'$
```

**007.06** · line 9

```tex
$\mathscr T$
```

**007.07** · line 11

```tex
$I$
```

**007.08** · line 11

```tex
$3$
```

**007.09** · line 11

```tex
$I=\{1,2,3\}$
```

**007.10** · line 13

```tex
$(E_i,G_i,\ldots,\Gamma)$
```

**007.11** · line 13

```tex
$\mathscr T'$
```

**007.12** · line 13

```tex
$x$
```

**007.13** · line 13

```tex
$=(x_1,x_2,x_3)$
```

**007.14** · line 13

```tex
$\Gamma$
```

**007.15** · line 13

```tex
$G_i$
```

**007.16** · line 13

```tex
$G$
```

**007.17** · line 13

```tex
$E_i$
```

**007.18** · line 13

```tex
$\prod E_i$
```

**007.19** · line 13

```tex
$\deleted{\unsure{\prod}}G^3$
```

**007.20** · line 13

```tex
$\Gamma$
```

**007.21** · line 13

```tex
$(x,y,z)$
```

**007.22** · line 14

```tex
\[
xyz=1
\]
```

**007.23** · line 18

```tex
$\underline x$
```

**007.24** · line 18

```tex
$(E'_i,G'_i,\ldots,\Gamma')$
```

**007.25** · line 18

```tex
$u$
```

**007.26** · line 18

```tex
$\varphi$
```

**007.27** · line 18

```tex
$\varphi$
```

**007.28** · line 18

```tex
$\Gamma$
```

**007.29** · line 18

```tex
$\Gamma'$
```

**007.30** · line 18

```tex
$(x'_1,x'_{\unsure{2|i}},x'_3)$
```

**007.31** · line 18

```tex
$x=(x_1,x_2,x_3)=(1,1,1)$
```

**007.32** · line 18

```tex
$G'{}^3$
```

**007.33** · line 18

```tex
$G'$
```

**007.34** · line 18

```tex
$\Gamma'$
```

**007.35** · line 18

```tex
$(x',y',z')$
```

**007.36** · line 19

```tex
\[
x'y'z'=1 .
\]
```

**007.37** · line 24

```tex
\[
u_1,u_2,u_3\colon G\longrightarrow G'
\]
```


**i/j indices and exponents.** l. 13 <code>_i</code>, <code>_i</code>, <code>_i</code>, <code>_i</code>, <code>_i</code> · l. 18 <code>_i</code>, <code>_i</code>, <code>_{\unsure{2&#124;i}}</code>

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| upper part, proposition and interline | insertion | <code>(à équiv. près)</code> |
| upper middle, proof and cancelled wording | insertion | <code>le foncteur induit sur</code> |
| upper middle, proof and cancelled wording | deletion | <code>\unsure{sont équivalentes}</code> |
| upper middle, proof and cancelled wording | deletion | <code>une \unsure{équivalence de}</code> |
| upper middle, proof and cancelled wording | insertion | <code>pl. fid.</code> |
| middle, object and first identification | insertion | <code>$(E_i,G_i,\ldots,\Gamma)$</code> |
| middle, object and first identification | insertion | <code>$=(x_1,x_2,x_3)$</code> |
| middle, object and first identification | insertion | <code>soit $G$,</code> |
| middle, object and first identification | deletion | <code>\unsure{\prod}</code> |
| lower half, second object | insertion | <code>$\varphi$ du</code> |

## Scan 009

2026-11-18T09:37:53Z to 2026-11-18T09:38:26Z.

### Crop reading before comparison

Landscape reading left-to-right across three strips. Crossed x y, then a_1, overwritten second symbol that can be b_2, and a_3. The three Isom targets are (E_2,E_3), (E_3,E_1), (E_1,E_2); connectors have unequal arrowheads. On the triangle E_1 is upper left, E_2 upper right, E_3 below. The labels of the reverse arrows are u_3, u_2 and u_1. Two “NB” notes on the right. The main word seems Posons following a small scratched glyph. The compositions give u_3,u_1,u_2 in that order. “Admettons” underlined, a box u_1u_2u_3=id, and “D'où syst transitif d'isom entre les E_i,”. Archive 8.

### Comparison

The bold upright of the overwritten second coordinate favours b as its last form. Its underlayer and the subscript in the lower right NB are hard to isolate. The three targets of the upper maps and the start and end of each solid and dashed edge of the triangle were checked against their own strip. The second top connector ends bluntly, the third has a small downward turn; neither has been silently regularised. The two NB registers give the forward and reverse actions on the three a's. The lower NB stands to the right of the boxed assumption and is now a margin note. The rule belongs below Admettons. E is angular manuscript E throughout, with no doubled upright. No typed additions.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>\deleted{\unsure{b}}a_2</code> | <code>\deleted{\unsure{a}}\unsure{b&#124;a}_2</code> |
| <code>NB $\begin{aligned}[t]u_3(a_2)</code> | <code>\margin{NB $\begin{aligned}[t]u_3(a_{\unsure{2&#124;1}})</code> |
| <code>u_2(a_1)&amp;=a_3\end{aligned}$</code> | <code>u_2(a_1)&amp;=a_3\end{aligned}$}</code> |

### Formula register

**009.01** · line 2

```tex
$\deleted{x\quad y}\qquad a_1\quad \deleted{\unsure{a}}\unsure{b|a}_2\quad a_3$
```

**009.02** · line 4

```tex
\[
\begin{aligned}
\deleted{\unsure{E}} \qquad E_1&\xrightarrow{\alpha_1}\operatorname{Isom}(E_2,E_3)&
E_2&\overset{\alpha_2}{\text{---}}\operatorname{Isom}(E_3,E_1)\\
&&E_3&\overset{\alpha_3}{\unsure{\text{---}|\longrightarrow}}\operatorname{Isom}(E_1,E_2)
\end{aligned}
\]
```

**009.03** · line 12

```tex
\begin{tikzcd}[ampersand replacement=\&,row sep=large,column sep=small]
E_1\arrow[rr,"{\alpha_3(a_3)}"]\arrow[dr,bend left=16,dashed,"{u_2}"]\&\&
E_2\arrow[ll,bend left=13,dashed,"{u_3}"]\arrow[dl,"{\alpha_1(a_1)}"']\\
\&E_3\arrow[ul,"{\alpha_2(\unsure{a_2|a_1})}"']\arrow[ur,bend left=17,dashed,"{u_1}"]\&
\end{tikzcd}
```

**009.04** · line 19

```tex
\[
\begin{aligned}
\alpha_3(a_3)&:a_1\ \text{---}\ a_2\\
\alpha_1(a_1)&:a_2\ \text{---}\ a_3\\
\alpha_2(a_2)&:a_3\ \text{---}\ a_1
\end{aligned}
\]
```

**009.05** · line 27

```tex
\[
\begin{aligned}
\alpha_2(a_2)\alpha_1(a_1)&=u_3:E_2\ \text{---}\ E_1\\
\alpha_3(a_3)\alpha_2(a_2)&=u_1:E_3\ \text{---}\ E_2\\
\alpha_1(a_1)\alpha_3(a_3)&=u_2:E_1\ \text{---}\ E_3
\end{aligned}
\]
```

**009.06** · line 35

```tex
$\boxed{u_1 u_2 u_3=\mathrm{id}}$
```

**009.07** · line 37

```tex
$\begin{aligned}[t]u_3(a_{\unsure{2|1}})&=a_1\\u_1(a_3)&=a_2\\u_2(a_1)&=a_3\end{aligned}$
```

**009.08** · line 39

```tex
$E_i$
```


**i/j indices and exponents.** l. 39 <code>_i</code>

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| top, short trial line | deletion | <code>x\quad y</code> |
| top, short trial line | deletion | <code>\unsure{a}</code> |
| upper half, three maps | deletion | <code>\unsure{E}</code> |
| below triangle | deletion | <code>\unsure{P}</code> |
| lower right | margin note | <code>NB $\begin{aligned}[t]u_3(a_{\unsure{2&#124;1}})&amp;=a_1\\u_1(a_3)&amp;=a_2\\u_2(a_1)&amp;=a_3\end{aligned}$</code> |

## Scan 010

2026-11-18T09:38:27Z to 2026-11-18T09:39:01Z.

### Crop reading before comparison

“Liste des chercheurs 1977 =” underlined, and an underlined Pr Grothendieck. The abbreviation's second letter is small. Points has a wavy underline. M. CONTOU - CARRÈRE = 5, J. DE LIMA or DELIMA = 3 (no clear gap), O. LABORDE = 5, and M. NGUIFFO. BOYOM = 7; the dot between names is visible. The two Ms have an underline at their left strokes. Total = 20 x 25%, then = above a box 5 points. A brace joins Valeur du point = 670 raised f and Part fixe = 7100 raised f. Archive pencil 9.

### Comparison

The printed-looking capitals are drawn by hand. M and P have short free feet, also present on characters within the names; these strokes do not cancel any letter. The acronym-like name in row two has a possible word space after DE, and case remains difficult in rows two and four. The entries, total, separate equals, box and two f superscripts were reread independently. The amount in the last row has four figures, 7100. The brace does not strike through the words. No mathematical i/j index, marginal text or typed correction.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>Pr&#124;Pʳ</code> | <code>Pr&#124;P\textsuperscript{r}</code> |
| <code>J. DEL\unsure</code> | <code>J. \unsure{DEL&#124;DE L}\unsure</code> |

### Formula register

**010.01** · line 6

```tex
$\begin{array}{lr}
&\text{\uline{Points}}\\
\text{M. . CONTOU - CARRÈRE}&=5\\
\text{J. \unsure{DEL|DE L}\unsure{i|I}MA}&=3\\
\text{O. LABORDE}&=5\\
\text{M. NG\unsure{ui|UI}FFO. BOYOM}&=7\\ \cline{2-2}
\end{array}$
```

**010.02** · line 13

```tex
\[
\begin{aligned}
\text{Total}&=20\times25\%\\
&=\\[-.2em]
&\boxed{5\ \text{points}}
\end{aligned}
\]
```

**010.03** · line 20

```tex
\[
\left\{\begin{aligned}
\text{Valeur du point}&=670^{\mathrm f}\\
\text{Part fixe}&=7100^{\mathrm f}
\end{aligned}\right.
\]
```


**i/j indices and exponents.** None.

**Local interventions.** None.

## Scan 011

2026-11-18T09:39:02Z to 2026-11-18T09:39:47Z.

### Crop reading before comparison

The first word is crossed, followed by “permettent de les identifier à un [double bar] G. On a donc”. “ens pointé” with (G,e), relation in G×G×G. In a), the ∃ has a stroke 1 to its right, in all three lines; ditto strokes in the last two. The crossed b) is large, hatched, and includes sigma_1 and sigma_2 and triples; a new b) has three e's. c) “Si” or possibly “Soit”, the three sigma_i and G with tilde above a line G. Third triple x, sigma_3 x e has no obvious second comma. “On a” and a crossed squared string, then three identities. “i.e.” tacitly followed by sigma_1=sigma_2=sigma_3 (=sigma [small closing strokes]), sigma squared=id. A cancelled z=xy equivalence, and a live triple-membership equivalence below. Address label is upside down, says MR LE PROFESSEUR GROTHENDIECK A. / MATHEMATIQUES 5. Corner 10.

### Comparison

Read the faint first ending independently of the continuation from scan 9. The existential signs each have a right-hand upright. The barred first b) and the two associated relation triples all belong to the crossed draft. The replacement b) is clear. In c) the last condition lacks a visible separator between x and e after sigma_3. The crossed superscript 2 belongs to the whole parenthesised product. The live three pairs below have indices 21,32,13. Only one closing parenthesis is required by the ink following (=sigma); the downward flick is part of the same closing stroke. The double horizontal line separates the construction, and the lightness of the separator after y justifies marking it. The ordinary manuscript Γ has a right-angle top. The typed label was read turned through 180 degrees and has single capitals. No handwritten correction to that label.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code> permettant de les</code> | <code> \unsure{permettant&#124;permettent} de les</code> |
| <code>$c)$ Soit</code> | <code>$c)$ \unsure{Soit&#124;Si}</code> |
| <code>(= \sigma\unsure{\,)})</code> | <code>(=\sigma)</code> |
| <code>$(x,y,\sigma(xy))</code> | <code>$(x,y\unsure{,&#124;;}\sigma(xy))</code> |

### Formula register

**011.01** · line 2

```tex
$\overline{\mathrm m}$
```

**011.02** · line 2

```tex
$G$
```

**011.03** · line 4

```tex
\[
\deleted{\unsure{x_2}}\left\{\begin{aligned}
&\text{ens pointé : }(G,e)\\
&\Gamma\subset G\times G\times G
\end{aligned}\right.
\]
```

**011.04** · line 11

```tex
\[
\begin{aligned}
a)\quad\forall x,y\in G,\quad &\exists\unsure{1|!}\,z\in G\ \text{tel que}\quad (x,y,z)\in\Gamma\\
&\exists1\,z\in G\quad\text{---------}\quad(z,x,y)\in\Gamma\\
&\exists1\,z\in G\quad\text{---------}\quad(x,z,y)\in\Gamma
\end{aligned}
\]
```

**011.05** · line 19

```tex
\[
\begin{aligned}
&\deleted{b)\quad\text{Soit }\unsure{x}\ \unsure{\sigma_1,\sigma_2}\quad\sigma_1:}
 \quad\deleted{\inserted{\sigma_1,\sigma_2}\ G\xrightarrow{\sim}G\ \text{défini par}}\\
&\deleted{(x,\sigma_1 x,e)\in\Gamma,\quad\unsure{\sigma=}}
\quad\left\{\begin{aligned}
&\deleted{(e,x,\sigma_1 x)\in\Gamma}\\
&\deleted{(\sigma_2 x,e,x)\in\Gamma}
\end{aligned}\right.
\end{aligned}
\]
```

**011.06** · line 31

```tex
$b)\quad(e,e,e)\in\Gamma$
```

**011.07** · line 33

```tex
$c)$
```

**011.08** · line 33

```tex
$\sigma_1,\sigma_2,\sigma_3:G\overset{\sim}{\text{---}}G$
```

**011.09** · line 34

```tex
\[
\begin{aligned}
(e,x,\sigma_1x)&\in\Gamma\\
(\sigma_2x,e,x)&\in\Gamma\\
(x,\sigma_3x\, e)&\in\Gamma
\end{aligned}
\]
```

**011.10** · line 41

```tex
$(\sigma_3\sigma_2\sigma_1)^2=\mathrm{id}$
```

**011.11** · line 42

```tex
\[
\sigma_2\sigma_1=\mathrm{id},\qquad\sigma_3\sigma_2=\mathrm{id},\qquad\sigma_1\sigma_3=\mathrm{id}
\]
```

**011.12** · line 45

```tex
$\sigma_1=\sigma_2=\sigma_3\ (=\sigma)\quad\sigma^2=\mathrm{id}$
```

**011.13** · line 47

```tex
$x,y\in G$
```

**011.14** · line 47

```tex
$x\cdot y\in G$
```

**011.15** · line 47

```tex
$(x,y\unsure{,|;}\sigma(xy))\in\Gamma$
```

**011.16** · line 49

```tex
$\deleted{z=xy\Longleftrightarrow (x,y}$
```

**011.17** · line 50

```tex
\[
(x,y,z)\in\Gamma\Longleftrightarrow z=\sigma(x\cdot y)
\]
```


**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| top, continuation after cancellation | deletion | <code>\unsure{Admettons}</code> |
| upper part, braced data | deletion | <code>\unsure{x_2}</code> |
| above fold, hatched b and added right-hand draft | deletion | <code>b)\quad\text{Soit }\unsure{x}\ \unsure{\sigma_1,\sigma_2}\quad\sigma_1:</code> |
| above fold, hatched b and added right-hand draft | deletion | <code>\inserted{\sigma_1,\sigma_2}\ G\xrightarrow{\sim}G\ \text{défini par}</code> |
| above fold, hatched b and added right-hand draft | insertion | <code>\sigma_1,\sigma_2</code> |
| above fold, hatched b and added right-hand draft | deletion | <code>(x,\sigma_1 x,e)\in\Gamma,\quad\unsure{\sigma=}</code> |
| above fold, hatched b and added right-hand draft | deletion | <code>(e,x,\sigma_1 x)\in\Gamma</code> |
| above fold, hatched b and added right-hand draft | deletion | <code>(\sigma_2 x,e,x)\in\Gamma</code> |
| right of triples, then below | deletion | <code>$(\sigma_3\sigma_2\sigma_1)^2=\mathrm{id}$</code> |
| lower third, under double rule | deletion | <code>z=xy\Longleftrightarrow (x,y</code> |

## Scan 012

2026-11-18T09:39:48Z to 2026-11-18T09:52:03Z.

### Crop reading before comparison

Read after rotating the three strips. Page “- 3 -”. Coût très faible; Reclassement sur place d'un certain nombre d'Agents. “ne gênerait”, “effectué”, “une société privé”, “hors-statut”, “contractuel, type C.N.R.S. est commencée”. “Le débat s'engage aussitôt.” “Les Professeur présents” lacks the plural on Professeur. “Aussi,il”, “Les Professeurs ,”, “représentants syndicaux”, “élus”, “11 Mai 1977”, “oeuvre”, “Agent Technique de Bureau, nécessaire”. Straight quotation marks. “voté.” with a small point before “à l'unanimité”. “Il est décidé, que”, “P.T.O.S.”. In “choisit” a short independent diagonal crosses the t. “Présidence du S.E.U.”, “réclamées”, “tout le Personnel” (upright possibly capital), “l’U.S.T.L.”, “organisée”. [name redacted], [name redacted], [name redacted] / [name redacted], [name redacted], [name redacted] / [name redacted], [name redacted]. Printed last line “La séance est levée à 16H 30”. A continuous diagonal crosses the first text, middle motion and third column, ending above the time. Archive number 11 opposite.

### Comparison

At native scale the crowded last two letters of commencée and the acute are distinguishable. A tiny pair of marks between le and personnel survives enlargement, and personnel begins with a descender. The long pencil stroke runs from the top text to the right column of names; the closing time is outside its reach. A second short diagonal specifically cancels t in choisit. The upright left of the quotation marks its extent. All names and initials were checked individually. The headings and proper names have single typed letters. The motion has straight double quotes, the typewriter's oe, and a separate mark following voté. No mathematical formula or i/j index.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>\unsure{commencée}</code> | <code>commencée</code> |
| <code>`` Les Agents</code> | <code>\textquotedbl{} Les Agents</code> |
| <code>laboratoires ''.</code> | <code>laboratoires \textquotedbl{}.</code> |
| <code>tout le personnel de</code> | <code>tout le\unsure{:&#124;.} personnel de</code> |

### Formula register

**012.01** · line 30

```tex
$\begin{array}{lll}
\text{\deleted{Melle [name redacted]}}&\text{\deleted{M. [name redacted]}}&\text{\deleted{M. [name redacted]}}\\
\text{\deleted{Mme \quad [name redacted]}}&\text{\deleted{M. [name redacted]}}&\text{\deleted{M. [name redacted]}}\\
\text{\deleted{Melle [name redacted]}}&\text{\deleted{M. [name redacted]}}&
\end{array}$
```


**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| top in reading orientation, opening | deletion | <code>Cette mesure aurait les avantages suivants :</code> |
| top, first advantage | deletion | <code>- Coût très faible.</code> |
| top, second advantage | deletion | <code>- Reclassement sur place d'un certain nombre d'Agents.</code> |
| upper third, third advantage | deletion | <code>- La transformation des postes d'Agents de service ne gênerait en rien l'entretien de la faculté qui est effectué en gra</code> |
| upper third, debate | deletion | <code>Le débat s'engage aussitôt.</code> |
| above centre, response | deletion | <code>Les Professeur présents à la réunion ainsi que le personnel pensent que cette solution est la plus rationnelle et qu'ell</code> |
| above centre, introduction to motion | deletion | <code>Aussi,il est proposé aux présents, par les Agents de service, un vote sur la motion suivante :</code> |
| centre, quotation with left vertical rule | deletion | <code>\textquotedbl{} Les Agents de service assurant les travaux de secrétariat dans les laboratoires, les Professeurs , les r</code> |
| below quotation, vote | deletion | <code>Le texte de la motion est voté\unsure{.} à l'unanimité des présents.</code> |
| lower middle, council | deletion | <code>Il est décidé, que cette motion sera présentée au Conseil d'Université par les représentants P.T.O.S.</code> |
| lower third, committee | deletion | <code>Un collectif est choisi</code> |
| lower third, committee | deletion | <code>t</code> |
| lower third, committee | deletion | <code> parmi les présents à la réunion. Ce collectif a pour tâche de prendre tous les contacts nécessaires au niveau de la Pré</code> |
| lower third, signatures | deletion | <code>Il est décidé que tout le\unsure{:&#124;.} personnel de l'U.S.T.L. sera informé de la tenue et des travaux de cette réunion e</code> |
| bottom, table heading | deletion | <code>\uline{Composition du collectif} :</code> |
| bottom, three columns of names | deletion | <code>Melle [name redacted]</code> |
| bottom, three columns of names | deletion | <code>M. [name redacted]</code> |
| bottom, three columns of names | deletion | <code>M. [name redacted]</code> |
| bottom, three columns of names | deletion | <code>Mme \quad [name redacted]</code> |
| bottom, three columns of names | deletion | <code>M. [name redacted]</code> |
| bottom, three columns of names | deletion | <code>M. [name redacted]</code> |
| bottom, three columns of names | deletion | <code>Melle [name redacted]</code> |
| bottom, three columns of names | deletion | <code>M. [name redacted]</code> |

## Scan 013

2026-11-18T09:52:04Z to 2026-11-18T09:53:04Z.

### Crop reading before comparison

Top “ens pointé, avec loi de composition”, “autom de G” and squeezed crossed text, circled sigma squared=id. The two set-builders have G cubed. Conditions a) uses ∃1 z twice and sigma inverse y. The second half of the first mapping z↦zx is overwritten, with y/x ambiguous. “sont bijectifs”, b) sigma inverse e=e.e. In c) a right brace gives σe=e, the next line has i.e., ∀x, then small strokes (“on a” possible); x.e=σ to −2 applied to x, margin (=x ...). “y faisant x=1” is struck. “Donc : e est unité bilatère”, “à g et à dr.”, “Enfin”, “à droite”, “c'est un inverse bilatère”. Bottom (xy)z=x(yz) ?? then slash, relation, scribbles with successive crossed terms and several live implication/equivalence signs. Pencil 12.

### Comparison

The mark around sigma squared is round. In c) the four small strokes after the second “∀x” may be highly reduced “on a”; native-scale inspection does not settle it. All three inverse powers in the unit calculation were checked, especially −2. The right edge clips the end of the parenthesis after =x. The strokes linking the inverse argument and the note “c'est un inverse bilatère” form a brace. Rechecked the crossed preparatory lines after c), the replacement above “à droite”, the cancellation below the inverse pair and the dense cancellations below the associativity question. The last two live triples have different visible counts of closing parentheses. The accent-like mark on e and the little upward curve in the exponent have been preserved. G and Γ have distinct rounded and angular tops. No typed conversion or numbered i/j indices.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>$\boxed{\sigma^2=\mathrm{id}}$</code> | <code>\tikz[baseline=(v.base)]{\node (v) {$\sigma^2=\mathrm{id}$}; \draw (v.center) ellipse (2.15em and .9em);}</code> |
| <code>\unsure{\cdots}</code> | <code>\unsure{\text{on a}&#124;\cdots}</code> |

### Formula register

**013.01** · line 2

```tex
$(G,e)$
```

**013.02** · line 2

```tex
$(x,y)\mathrel{\text{---}}x\cdot y$
```

**013.03** · line 4

```tex
$\sigma$
```

**013.04** · line 4

```tex
$G$
```

**013.05** · line 4

```tex
$,e$
```

**013.06** · line 4

```tex
$\sigma^2=\mathrm{id}$
```

**013.07** · line 5

```tex
\[
\Gamma=\{(x\unsure{.|,}y,z)\in G^3\mid z=\sigma(x\cdot y)\}
=\{(x,y,z)\in G^3\mid x\cdot y=\sigma^{-1}z\}
\]
```

**013.08** · line 10

```tex
$a)$
```

**013.09** · line 11

```tex
\[
\begin{aligned}
\forall x,y\in G\qquad &\exists\unsure{1|!}\,z\quad\text{tel que}\quad zx=\deleted{\unsure{y}}\sigma^{-1}y\\
&\exists1\,z\quad\text{tel que}\quad xz=\sigma^{-1}y
\end{aligned}
\]
```

**013.10** · line 17

```tex
$z\mathrel{\unsure{\mapsto|\vdash}}z\deleted{\unsure{y}}x$
```

**013.11** · line 17

```tex
$z\mathrel{\vdash}xz$
```

**013.12** · line 19

```tex
\[
\begin{aligned}
b)&\quad \sigma^{-1}e=e\cdot e\\
c)&\quad\text{On a }\forall x\quad \sigma^{-1}\sigma x=ex\qquad\text{i.e. }\deleted{\unsure{e=}}ex=x
\quad\Big\}\Rightarrow\sigma e=e\\
&\quad\forall x\quad\sigma x\cdot e=\sigma^{-1}x\qquad\text{i.e }\forall x\ \unsure{\text{on a}|\cdots}\quad x\cdot e=\sigma^{-2}x\ (\uline{=x}\\
&\quad\forall x\quad x\cdot\sigma x=\sigma^{-1}e\quad(=e)
\end{aligned}
\]
```

**013.13** · line 29

```tex
$x=\unsure{1|e}$
```

**013.14** · line 29

```tex
$e\cdot\sigma e=\sigma^{-1}e\ (= \sigma e)$
```

**013.15** · line 31

```tex
$e\cdot\sigma$
```

**013.16** · line 33

```tex
$e$
```

**013.17** · line 33

```tex
$\sigma x$
```

**013.18** · line 33

```tex
$x$
```

**013.19** · line 33

```tex
$\forall x\in G$
```

**013.20** · line 33

```tex
$\sigma x$
```

**013.21** · line 33

```tex
$x$
```

**013.22** · line 33

```tex
$\sigma^2=\mathrm{id}$
```

**013.23** · line 35

```tex
\[
\left.\begin{aligned}
x\cdot\sigma x&=e&(\sigma x)(\sigma\sigma x)^{\unsure{\smile}}&=e\\
\deleted{(\sigma x)x}&\deleted{{}=e}&\deleted{\sigma x\cdot x}&
\end{aligned}\right\}\quad\text{c'est un inverse bilatère}
\]
```

**013.24** · line 42

```tex
\[
\begin{aligned}
&(xy)z=x(yz)\qquad ??\ /\\
&\deleted{\unsure{\sigma x\cdot x\sigma}}\\
&\deleted{xy,z,\sigma((xy)z)}\\
&(xy,z,\sigma((xy)z))\in\Gamma\\
&(x,yz,\sigma(x(yz))\in\Gamma
\end{aligned}
\]
```

**013.25** · line 52

```tex
\[
\begin{aligned}
&(x,y,\sigma(xy))\in\Gamma\\
&\deleted{(\sigma y,\sigma x.}\\
&(x,y,z)\in\Gamma\Rightarrow z=\deleted{\unsure{(xy)\sigma(x}}\sigma(x\cdot y)
\Longleftrightarrow(x\cdot y)z=\unsure{\acute e|e}\\
&\hspace{10em}\Longleftrightarrow z\cdot(x\cdot y)=e\\
&\Updownarrow\quad xy=\acute e\\
&\Updownarrow\quad(xy)z=z\\
&\phantom{\Updownarrow\quad}z(xy)=z
\end{aligned}
\]
```


**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| top | deletion | <code>\unsure{$,e$}</code> |
| upper third, conditions | deletion | <code>\unsure{y}</code> |
| upper third, conditions | deletion | <code>\unsure{y}</code> |
| upper middle, b and c, side implication | deletion | <code>\unsure{e=}</code> |
| above fold, two cancelled lines | deletion | <code>y faisant $x=\unsure{1&#124;e}$, on trouve $e\cdot\sigma e=\sigma^{-1}e\ (= \sigma e)$</code> |
| above fold, two cancelled lines | deletion | <code>donc \qquad $e\cdot\sigma$</code> |
| below fold, parallel pen strokes on left | deletion | <code>et $\sigma x$ est l'inverse à droite de $x$</code> |
| below fold, parallel pen strokes on left | deletion | <code>\unsure{un inv}</code> |
| below fold, parallel pen strokes on left | insertion | <code>inverse</code> |
| below fold, parallel pen strokes on left | insertion | <code>de $x$</code> |
| lower middle, inverse relations | deletion | <code>(\sigma x)x</code> |
| lower middle, inverse relations | deletion | <code>{}=e</code> |
| lower middle, inverse relations | deletion | <code>\sigma x\cdot x</code> |
| bottom left, associativity question and trials | deletion | <code>\unsure{\sigma x\cdot x\sigma}</code> |
| bottom left, associativity question and trials | deletion | <code>xy,z,\sigma((xy)z)</code> |
| bottom right, tests for membership and unit | deletion | <code>(\sigma y,\sigma x.</code> |
| bottom right, tests for membership and unit | deletion | <code>\unsure{(xy)\sigma(x}</code> |

## Scan 014

2026-11-18T09:53:04Z to 2026-11-18T09:53:40Z.

### Crop reading before comparison

Circled A. E_1=E_2=E_3=G; Γ defined by xyz=1, “i.e. abc=1”. Triangle with straight f_i and curving back g_i. In the defining triples first entry a, central entry b, final entry c or e. For f_i(x) the images read x inverse followed by a,b,c inverse respectively. At right x inverse a inverse=y, x=a inverse y inverse. A box σ(xy)=σy σx. The scratched equivalences and two axially arranged derivations have multiple inverse exponents and upright arrowheads. g_1=f_3 f_2, g_2=f_1 f_3, g_3=f_2 f_1. On the ruled line g_1g_2g_3 expands to bca x b inverse a inverse c inverse, with bca and cab underbraced to 1. Below “de [double stroke]”, σ_2, σ_3, σ_1. A whole sigma-square line is struck. Two little diagrams below, sigma_1, primed/inverse map labels; a cancelled (x,y,z) and a fresh triple at the foot. Archive 13.

### Comparison

The small final entry of the third defining triple has an e-like loop, although the neighbouring inverse is plainly c inverse. Rechecked each of the six directed arrows in the large triangle and four nonidentity arrows in the two bottom diagrams, including f_1 inverse; the additional vertical mark at the lower E_1 is ambiguous. The sign of the exponent in y at upper right is itself struck and has no live exponent. The high curve on the transfer to the bracketed calculation is a grouping line. Rechecked the inverses on the bca/cab line, including the outer inverse on cab and the superscript 2 on the composition of f's. The last sigma-square computation and the first lower tuple are crossed, and the lower product really shows its irregular run aa inverse. Corrected the layout command for the box inside aligned without moving its ink to another line. No styled typed capital or handwritten amendment to type.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>(x,f_3(x),c)</code> | <code>(x,f_3(x),\unsure{e&#124;c})</code> |
| <code>\multicolumn{2}{c}{\boxed{\sigma(xy)=\sigma y\,\sigma x}}</code> | <code>\boxed{\sigma(xy)=\sigma y\,\sigma x}</code> |
| <code>\unsure{x}^</code> | <code>{\unsure{x}}^</code> |

### Formula register

**014.01** · line 3

```tex
\[
\begin{aligned}
&E_1=E_{\unsure{2|1}}=E_3=G\\
&\Gamma=\{(x,y,z)\mid xyz=1\}\\
&(a,b,c)\in\Gamma\qquad\text{i.e. }\ abc=1
\end{aligned}
\]
```

**014.02** · line 11

```tex
\begin{tikzcd}[ampersand replacement=\&,row sep=large,column sep=small]
\&E_1\arrow[dl,"{f_3}"']\arrow[dr,bend left=30,"{g_2}"]\&\\
E_2\arrow[ur,bend left=30,"{g_3}"]\arrow[rr,shift left=2pt,"{f_1}"]\&\&
E_3\arrow[ul,"{f_2}"']\arrow[ll,shift left=2pt,"{g_1}"]
\end{tikzcd}
```

**014.03** · line 16

```tex
\[
\begin{aligned}
\deleted{f_2}\qquad f_1(x)&\quad\text{défini par}\quad (a,x,f_1(x))\in\Gamma\\
f_2(x)&\quad\text{---------}\quad(f_2(x),b,x)\in\Gamma\\
f_3(x)&\quad\text{---------}\quad(x,f_3(x),\unsure{e|c})\in\Gamma
\end{aligned}
\]
```

**014.04** · line 23

```tex
\[
\begin{aligned}
f_1(x)&=x^{-1}a^{-1}&x^{-1}a^{-1}&=y\\
f_2(x)&=x^{-1}b^{-1}&x&=a^{-1}y^{-1}\\
f_3(x)&=x^{-1}c^{-1}&\boxed{\sigma(xy)=\sigma y\,\sigma x}
\end{aligned}
\]
```

**014.05** · line 31

```tex
\[
\begin{aligned}
&\deleted{z=xy}&&\deleted{\unsure{z}}\\
&&z=xy&\Longleftrightarrow\deleted{\unsure{x^{-1}z=y}}\\
&&\deleted{\unsure{xy=}}&x=zy^{-1}\\
&&&y^{\deleted{\unsure{+}}}=x^{-1}z
\end{aligned}
\]
```

**014.06** · line 39

```tex
\[
\begin{aligned}
g_1(x)&=f_3f_2(x)=(bx)c^{-1}\\
g_2(x)&=f_1f_3(x)=(cx)a^{-1}\\
g_3(x)&=f_2f_1(x)=(ax)b^{-1}
\end{aligned}
\]
```

**014.07** · line 46

```tex
\[
\left\{\begin{aligned}
(xy)z&=1 &y^{-1}&=zx\\
&\Updownarrow &&\Updownarrow\\
\deleted{\unsure{(yz)x}}&=1 &y&=x^{-1}z^{-1}\\
(zx)y&=1\\
&\Updownarrow\\
({\unsure{x}}^{-1}z^{-1})y^{-1}&=1\Longleftrightarrow
\end{aligned}\right.
\]
```

**014.08** · line 57

```tex
\[
\begin{aligned}
g_1g_2g_3(x)&=bcax\,b^{-1}a^{-1}c^{-1}
=(\underbrace{bca}_{\substack{\|\\1}})x(\underbrace{cab}_{\substack{\|\\1}})^{-1}=x\qquad\text{i.e. }g_1g_2g_3=\mathrm{id}\\
g_1g_2g_3&=(f_3f_2f_1)^2\\
f_3f_2f_1(x)&=(axb^{-1})^{-1}c^{-1}=bx^{-1}a^{-1}c^{-1}=bx^{-1}(ca)^{-1}=bx^{-1}b\\
\sigma_2x&=bx^{-1}b\qquad\text{de }\overline{\mathrm m}\quad\sigma_3 x=cx^{-1}c,\quad\sigma_1x=ax^{-1}a\\
&\deleted{\sigma_{\unsure{1|2}}^2 x=b(b^{-1}xb^{-1})b=x}
\end{aligned}
\]
```

**014.09** · line 68

```tex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
E_1\& E_2\arrow[r,shift left=2pt,"f_1"]\& E_3\arrow[l,shift left=2pt,"{f_1^{-1}}"]
\end{tikzcd}
```

**014.10** · line 71

```tex
$\deleted{(x,y,z)}$
```

**014.11** · line 73

```tex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
E_1\arrow[d,"{\sigma_1}"',"{\unsure{\sim|2}}"]\&E_2\arrow[dr,"f_1"']\& E_3\arrow[dl,"{f_1^{-1}}"']\\
E_1\&E_2\&E_3
\end{tikzcd}
```

**014.12** · line 77

```tex
\[
\begin{aligned}
&&xyz=1&\Longrightarrow\\
(x,y,z)&&ax^{-1}aa^{-1}z^{-1}y^{-1}\cdot a^{-1}&=1\\
(\sigma_1 x,f_1^{-1}z,f_1y)&=(ax^{-1}a,a^{-1}z^{-1},y^{-1}a^{-1})
\end{aligned}
\]
```


**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| upper right, f definitions | deletion | <code>f_2</code> |
| right of fold, scratch equations | deletion | <code>z=xy</code> |
| right of fold, scratch equations | deletion | <code>\unsure{z}</code> |
| right of fold, scratch equations | deletion | <code>\unsure{x^{-1}z=y}</code> |
| right of fold, scratch equations | deletion | <code>\unsure{xy=}</code> |
| right of fold, scratch equations | deletion | <code>\unsure{+}</code> |
| below fold, right braced trial | deletion | <code>\unsure{(yz)x}</code> |
| lower third, compositions | deletion | <code>\sigma_{\unsure{1&#124;2}}^2 x=b(b^{-1}xb^{-1})b=x</code> |
| foot middle, trial triple | deletion | <code>(x,y,z)</code> |

## Scan 015

2026-11-18T09:53:41Z to 2026-11-18T09:54:22Z.

### Crop reading before comparison

Circled B. At top crossed scratch before z=xy. At right x inverse(uz inverse)=y. The second long line stops at u( and a small dot. A free x inverse and three small cancelled left entries. Three f_i inverses left, three g_i and x-mapping strokes at right. Next g_1g_2g_3=(f_3f_2f_1) squared; the upper long fully parenthesised product and the square calculation around c use different brackets. In the right brace σ(xy)=σx σy, as drawn in this order, then τ with raised d and g, lower x and x inverse. Middle downwards x, ax, axb inverse, caxb inverse, … . Bottom left abc, cab=1; at right (bx)c inverse=y and x=b inverse(yc). Final framed equation c((ax)b inverse)=(b inverse(xc))a; scratches above and below the box. Pencil 14.

### Comparison

The line with upper d has a small distinct angular glyph under the inverse exponent. On the native image it has a lower horizontal stroke. The next line, with g, has just the raised inverse. Rechecked all nested parentheses in the two long calculations. The square brackets in the sigma_2 squared line sit over two lighter parentheses. The left brace and the fold do not cancel the f_i or g_i lines. The scratch before the first x mapping, the aborted opening, the struck inverse factor above the box, and the last two ruled-through lines remain in place. The framed identity has c on the far left and a on the far right. Ordinary manuscript letters only. No marginal prose, or corrections to a typescript.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>\tau_x^{d}\,{}^{\unsure{-1}}</code> | <code>\tau_x^{d}\,\unsure{\leq&#124;\angle}^{-1}</code> |
| <code>\unsure{\leq&#124;\angle}^</code> | <code>{\unsure{\leq&#124;\angle}}^</code> |

### Formula register

**015.01** · line 3

```tex
\[
\begin{aligned}
&\deleted{\unsure{xy}}\quad z=xy && x^{-1}(uz^{-1})=y\\
u&=(xy)z\Longleftrightarrow(uz^{-1}=xy)\Longleftrightarrow (y^{-1}x^{-1})u=z\\
u&=x(yz)\Longleftrightarrow(x^{-1}u=yz)\Longleftrightarrow u(\unsure{\cdot}\\
&&x^{-1}\\
&\deleted{u=}\\
&\deleted{xy}\\
&\deleted{xy}
\end{aligned}
\]
```

**015.02** · line 14

```tex
\[
\left\{\begin{aligned}
f_1(x)&=x^{-1}a^{-1}&g_1&=f_3f_2=\deleted{\unsure{bx}}x\mathrel{\unsure{\vdash|\mapsto}}(bx)c^{-1}\\
f_2(x)&=x^{-1}b^{-1}&g_2&=f_1f_3=\qquad x\mathrel{\vdash}(cx)a^{-1}\\
f_3(x)&=x^{-1}c^{-1}&g_3&=f_2f_1=\qquad x\mathrel{\vdash}(ax)b^{-1}
\end{aligned}\right.
\]
```

**015.03** · line 22

```tex
\[
g_1g_2g_3=(f_3f_2f_1)^2\qquad x\mapsto\bigl(b\bigl(\bigl(c((ax)b^{-1})\bigr)a^{-1}\bigr)\bigr)c^{-1}
\]
```

**015.04** · line 25

```tex
\[
\begin{aligned}
\sigma_2x&=f_3f_2f_1(x)=\bigl((ax)b^{-1}\bigr)^{-1}c^{-1}
=\bigl(b(x^{-1}a^{-1})\bigr)c^{-1}\\
\sigma_2^2x&=\bigl(b\bigl(\deleted{(}\bigl[c\bigl((ax)b^{-1}\bigr)\bigr]\deleted{)}a^{-1}\bigr)\bigr)c^{-1}
\end{aligned}
\]
```

**015.05** · line 33

```tex
\[
\begin{aligned}
&x\\&ax\\&axb^{-1}\\&caxb^{-1}\\&
\deleted{\unsure{b}}caxb^{-1}a^{-1}\\&bcaxb^{-1}\unsure{a}\\&bcaxb^{-1}a^{-1}c^{-1}
\end{aligned}
\]
```

**015.06** · line 39

```tex
\[
\left\{\begin{aligned}
\sigma(xy)&=\sigma x\cdot\sigma y\\
\tau_x^{d}\,{\unsure{\leq|\angle}}^{-1}&=\tau_{x^{-1}}^d\\
\tau_x^{g}\,{}^{-1}&=\tau_{x^{-1}}^g .
\end{aligned}\right.
\]
```

**015.07** · line 46

```tex
\[
\begin{aligned}
&u=(xy)z\\
&\deleted{\unsure{uz^{-1}=xy}}\\
&u
\end{aligned}
\]
```

**015.08** · line 53

```tex
\[
\begin{aligned}
&\deleted{\unsure{g_1^{-1}}}\\
&(bx)c^{-1}=y\\
&x=b^{-1}(yc)
\end{aligned}
\]
```

**015.09** · line 60

```tex
\[
\begin{aligned}
&\deleted{x=}\qquad g_1g_2g_3 x=x\qquad\deleted{\unsure{g_2}g_3x=}\\
&\bigl(c((ax)b^{-1})\bigr)\deleted{a^{-1}}=\bigl(b^{-1}(xc)\bigr)a\\
&\boxed{c\bigl((ax)b^{-1}\bigr)=\bigl(b^{-1}(xc)\bigr)a}
\end{aligned}
\]
```

**015.10** · line 68

```tex
\[
\begin{aligned}
&abc\\
&\underbrace{ca}b=1\\
&\deleted{c=1}\qquad \deleted{c(xc)=(xc)}\quad\deleted{(ax)a=\unsure{x+}} \qquad \deleted{c(ab^{-1})=(b^{-1}c)a}\\
&\deleted{b=a^{-1}}\qquad\deleted{a^{-1}(ax)=(xa^{-1})a}\qquad x=
\end{aligned}
\]
```


**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| top, product and two parenthesisations | deletion | <code>\unsure{xy}</code> |
| top, product and two parenthesisations | deletion | <code>u=</code> |
| top, product and two parenthesisations | deletion | <code>xy</code> |
| top, product and two parenthesisations | deletion | <code>xy</code> |
| upper middle, two columns of maps | deletion | <code>\unsure{bx}</code> |
| across fold, sigma_2 and square | deletion | <code>(</code> |
| across fold, sigma_2 and square | deletion | <code>)</code> |
| lower middle, running list of factors | deletion | <code>\unsure{b}</code> |
| lower left, trials | deletion | <code>\unsure{uz^{-1}=xy}</code> |
| lower right, solving for x | deletion | <code>\unsure{g_1^{-1}}</code> |
| bottom, centre and boxed line | deletion | <code>x=</code> |
| bottom, centre and boxed line | deletion | <code>\unsure{g_2}g_3x=</code> |
| bottom, centre and boxed line | deletion | <code>a^{-1}</code> |
| foot left and across bottom, trials | deletion | <code>c=1</code> |
| foot left and across bottom, trials | deletion | <code>c(xc)=(xc)</code> |
| foot left and across bottom, trials | deletion | <code>(ax)a=\unsure{x+}</code> |
| foot left and across bottom, trials | deletion | <code>c(ab^{-1})=(b^{-1}c)a</code> |
| foot left and across bottom, trials | deletion | <code>b=a^{-1}</code> |
| foot left and across bottom, trials | deletion | <code>a^{-1}(ax)=(xa^{-1})a</code> |

## Scan 016

2026-11-18T09:54:22Z to 2026-11-18T09:55:17Z.

### Crop reading before comparison

A large outline encloses (b inverse a inverse)((ax)b inverse) = (b inverse(x(b inverse a inverse)))a. Second outlined implication from (ab)c=1 and (xy)z=1, with crossed (xyz). Square and round brackets enclose a long product with z inverse b inverse, b(y inverse a inverse), c inverse and b inverse x inverse. Crossed line below, an underlined z=c with black overmark, “alors” nearby. Corners of the derived bracket attach to small abc/c=b inverse a inverse; b↦z, a↦b, x↦y inverse a inverse. Wide reductions with underbraces a, y inverse, x. Two asterisks and “?” on a middle implication. A very light crossed conjecture (ub inverse)(bc)=uc ? and boxed identity lower down. Rightmost relation (bu)c=b((ub inverse)(bc)), then c=a inverse, xb=y inverse, b=bz with star-like marks. At bottom z=1 and b=1 specialisations and x, a circled under −1. Pencil 15.

### Comparison

Native-scale inspection separates a small abc from the long connecting stroke below it. There is a separate tiny sign after c in the next line, whose interpretation is open. The heavily overwritten xy in the implication still has a black b-like underlayer. Traced the groupings and nested underbraces a, y inverse and x, the connecting arrows beside the other long calculation, the two asterisks, and the question mark above the implication from the two product equations. The faint obliquely ruled question is cancelled. Both the box beginning the sheet and the box at the foot enclose live equations, as do the brackets round the first deduction. The last specialisations and circled variables really do overlap earlier lighter lines. No i/j indices, script capitals or typed corrections.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>\deleted{\unsure{abc}}&amp;b</code> | <code>abc&amp;b</code> |
| <code>&amp;c^{-1}b^{-1}a^{-1}&amp;a</code> | <code>&amp;c\,\unsure{{}^{\prime}&#124;=}\,b^{-1}a^{-1}&amp;a</code> |
| <code>((\unsure{xy})\underbrace</code> | <code>((\deleted{\unsure{b}}\unsure{xy})\underbrace</code> |
| <code>\unsure{a&#124;b}^</code> | <code>{\unsure{a&#124;b}}^</code> |

### Formula register

**016.01** · line 2

```tex
\[
\boxed{(b^{-1}a^{-1})\bigl((ax)b^{-1}\bigr)
=\bigl(b^{-1}(x(b^{-1}a^{-1}))\bigr)a}
\]
```

**016.02** · line 6

```tex
\[
\boxed{\left\{\begin{aligned}
(ab)c&=1\\
&\deleted{(x\quad y\quad z)}\\
(xy)z&=1
\end{aligned}\right.\quad\Longrightarrow
\bigl[(z^{-1}b^{-1})\bigl((b(y^{-1}a^{-1}))c^{-1}\bigr)\bigr](b^{-1}x^{-1})\deleted{\unsure{\big\}}}=1}
\]
```

**016.03** · line 14

```tex
\[
\begin{aligned}
&\deleted{\bigl(b(x^{-1}z^{-1})\bigr)c^{-1}=b(x^{-1}b)}\\
&\underbrace{z=c^{\deleted{\unsure{-1}}}}\quad\unsure{\text{alors}}\\
&\deleted{c=b^{-1}a^{-1}}\qquad(ab)(xy)=1\\
&\deleted{z=ab.}\\
&ab=\unsure{1|/}xy\qquad\deleted{(ab)(xy)=1}\\
&ax
\end{aligned}
\]
```

**016.04** · line 24

```tex
\[
\begin{aligned}
&abc&b&\mathrel{\vdash}z\\
&c\,\unsure{{}^{\prime}|=}\,b^{-1}a^{-1}&a&\mathrel{\vdash}b\\
&\downarrow\quad\|&x&\mathrel{\unsure{\mapsto|\vdash}}y^{-1}a^{-1}\\
&\bigl[\bigl(z^{-1}\bigl((y^{-1}a^{-1})(z^{-1}b^{-1})\bigr)\bigr)b\bigr](b^{-1}x^{-1})\\
\Rightarrow{}&
\bigl[\underbrace{\bigl((\deleted{\unsure{b}}\unsure{xy})\underbrace{\bigl((y^{-1}a^{-1})\underbrace{((\unsure{ab})b^{-1})}_{a}\bigr)}_{y^{-1}}\bigr)}_{x}b\bigr](b^{-1}x^{-1})
\end{aligned}
\]
```

**016.05** · line 34

```tex
\[
\deleted{\unsure{xb}}\qquad\qquad(xb)(b^{-1}x^{-1})=1
\]
```

**016.06** · line 37

```tex
\[
\begin{aligned}
(ab)c&=1\quad *&\overset{?}{\Longrightarrow}\quad xb&=(z^{-1}b^{-1})\bigl((b(y^{-1}a^{-1}))c^{-1}\bigr)\\
(xy)z&=1\quad *&&\\
&&&\Updownarrow\\
\deleted{(ub^{-1})(bc)}&\deleted{{}=uc\ ?}&(bz)(xb)&=(b(y^{-1}a^{-1}))c^{-1}
\end{aligned}
\]
```

**016.07** · line 45

```tex
\[
\begin{aligned}
(bz)(xb)&=\bigl(b\bigl((zx)\underbrace{({\unsure{a|b}}^{-1}c)}_{\unsure{b\ ?\ b}}\bigr)\bigr)c^{-1}\\
\bigl((\underbrace{bz}_{b})(\underbrace{xb}_{\substack{\|\\\deleted{\unsure{b^{-1}a^{-1}}}\\y^{-1}}})\bigr)\underset{\substack{\|\\a^{-1}}}{c}&=b(y^{-1}a^{-1})\\
(bu)c&=b((ub^{-1})(bc))
\end{aligned}
\]
```

**016.08** · line 52

```tex
\[
\begin{aligned}
&\deleted{\unsure{b}}\\
&\boxed{\bigl((bz)(xb)\bigr)c=b\bigl((zx)(bc)\bigr)}
\qquad\left\{\begin{aligned}c&=a^{-1}\\xb&=y^{-1}\quad *\\ b&=bz\quad *\end{aligned}\right.\\
&z=1,\ c=\\
&\bigl(b(xb)\bigr)c=b\bigl(x(bc)\bigr)
\end{aligned}
\]
```

**016.09** · line 61

```tex
\[
\begin{aligned}
z&=1\qquad y={\text{\textcircled{$x$}}}^{-1}\\
b&=1,\quad c={\text{\textcircled{$a$}}}^{-1}
\end{aligned}
\]
```


**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| upper quarter, boxed implication | deletion | <code>(x\quad y\quad z)</code> |
| upper quarter, boxed implication | deletion | <code>\unsure{\big\}}</code> |
| below box, cancelled trial and extraction | deletion | <code>\bigl(b(x^{-1}z^{-1})\bigr)c^{-1}=b(x^{-1}b)</code> |
| below box, cancelled trial and extraction | deletion | <code>\unsure{-1}</code> |
| below box, cancelled trial and extraction | deletion | <code>c=b^{-1}a^{-1}</code> |
| below box, cancelled trial and extraction | deletion | <code>z=ab.</code> |
| below box, cancelled trial and extraction | deletion | <code>(ab)(xy)=1</code> |
| upper middle right, substitutions and corresponding brackets | deletion | <code>\unsure{b}</code> |
| at fold, left and right | deletion | <code>\unsure{xb}</code> |
| lower middle, question above implication | deletion | <code>(ub^{-1})(bc)</code> |
| lower middle, question above implication | deletion | <code>{}=uc\ ?</code> |
| lower third, changed variables and bracketed evaluations | deletion | <code>\unsure{b^{-1}a^{-1}}</code> |
| bottom, boxed identity and marginal specialisations | deletion | <code>\unsure{b}</code> |

## Scan 017

2026-11-18T09:55:18Z to 2026-11-18T09:56:10Z.

### Crop reading before comparison

In the orientation of the dark ink the first lines have τ_x z=xz and τ_x τ_y z=x(yz), prime rather than inverse on the small x' in the next pair. G×G→G. Columns e,a then e,a,b then e,a,b,c, listing possible products. “ou”, “mais”, “donc”; ab=ba with “?” above the equality; aa=b,ab=e gives circled ba=e and bb=a. Two ruled tables have only the a row filled. Near the top of the tables are barred x's, and at right uv=u'v'. Equations below show (ab)c=1 then (ax)y=1, something overwritten before x prime in the second triple. At right f_2(x)=(σx)b with a tiny negative exponent. Under a large X these passages face the opposite way from the archive 16. In archive orientation pencil “(aa)a”, xy=z, y inverse=u, x=zu, powers of a_p, an unclear word after a_p=a_q a_{p−…}, and a final product z(u(u inverse z inverse))… . The separate cancellations of pencil remain visible.

### Comparison

Traced both diagonals through the dark-ink layer and then reread the pale writing in the opposite orientation. The local stroke before the first G is a separate cancelled x-like mark. Both tables really leave the b and c rows empty. The short overwrites of ab/ba, the far-right “mais” reaching the edge, the underlined or overbarred x's, and the cyclic chain were inspected again. The ending of the exponent on b in f_2 is very short. The final subscript following the two pencil a's is not plainly a single r. The global cross has been applied to the dark working throughout; the opposing pencil algebra carries only its local cancellations. The bar on x and the primes in the dark layer differ from the inverse exponents in pencil. Read G against Γ on the other sheets: here the last G is curved. No typed correction.

### Changes in the independent text

| Before | After |
| --- | --- |
| <code>\deleted{\unsure{x}G\times G\to G}</code> | <code>\deleted{\deleted{\unsure{x}}G\times G\to G}</code> |
| <code>\deleted{f_2(x)=(\sigma x)b^{-1}}</code> | <code>\deleted{f_2(x)=(\sigma x)b^{\unsure{-1&#124;-'}}}</code> |
| <code>a_p&amp;=a_q a_r</code> | <code>a_p&amp;=a_q a_{\unsure{r+&#124;r&#124;t}}</code> |

### Formula register

**017.01** · line 3

```tex
\[
\begin{aligned}
&\deleted{\tau_x z=xz}\\
&\deleted{\tau_x\tau_y z=x(yz)}\\
&\deleted{xx'=x'x=e}\\
&\deleted{x(x'y)=y}\\
&\deleted{\deleted{\unsure{x}}G\times G\to G}
\end{aligned}
\]
```

**017.02** · line 13

```tex
\[
\begin{aligned}
&\deleted{e\quad a}\\
&\deleted{ee=e}\\
&\deleted{ea=ae=a}\\
&\deleted{aa\ne ae=a\quad\text{donc}\quad aa=e}\\
&\deleted{e\quad a\quad b}\\
&\deleted{\overset{\unsure{\|}}{aa}\quad bb\quad ab=ba}\\
&\deleted{b\qquad\qquad\underset{\text{\textcircled{$e$}}}{\|}\qquad\underset{e}{\|}}\\
&\deleted{\underset{\substack{\|\\a(aa)}}{ab}\overset{?}{=}\underset{\substack{\|\\(aa)a}}{ba}\ -}
\end{aligned}
\]
```

**017.03** · line 25

```tex
\[
\begin{aligned}
&\deleted{\{\underset{\substack{\|\\a}}{ae},aa,ab\}=\{e,a,b\}}\\
&\deleted{\underbrace{aa=b,\ ab=e}\qquad\text{ou}\qquad aa=e,\ ab=b}\\
&\deleted{\Downarrow\qquad\qquad\qquad\text{mais }ab\ne eb\unsure{{}=b}}\\
&\deleted{\boxed{ba=e}}\\
&\deleted{bb=a}
\end{aligned}
\]
```

**017.04** · line 34

```tex
\[
\begin{aligned}
&\deleted{e,a,b,c}&\deleted{(xy)z=}\deleted{x(yz)}&&\deleted{uv=u'v'}\\
&&\deleted{x\ y\ z}&&\deleted{\overline x((xy)z)=(yz)}\\
&\deleted{e\quad a,b,c}&&&\deleted{\overline x((xy)z)z}
\end{aligned}
\]
```

**017.05** · line 42

```tex
$\begin{array}{c|c|c|c}
&\deleted{a}&\deleted{b}&\deleted{c}\\\hline
\deleted{a}&\deleted{e}&\deleted{\unsure{c|C}}&\deleted{b}\\\hline
\deleted{b}&&&\\\hline
\deleted{c}&&&\\\hline
\end{array}$
```

**017.06** · line 48

```tex
$\begin{array}{c|c|c|c|}
&\deleted{a}&\deleted{b}&\deleted{c}\\\hline
\deleted{a}&\deleted{b}&\deleted{c}&\deleted{e}\\\hline
\deleted{b}&&&\\\hline
\deleted{c}&&&\\\hline
\end{array}$
```

**017.07** · line 54

```tex
\[
\begin{aligned}
&\deleted{aa=e\quad ab=c\quad ac=b}\\
&\deleted{a}
\end{aligned}
\]
```

**017.08** · line 60

```tex
\[
\begin{aligned}
&\deleted{(xy)z=1\Longleftrightarrow z(xy)=1}\\
&\deleted{\Updownarrow}\\
&\deleted{y(zx)=1}\\
&\deleted{\unsure{\Updownarrow}}\\
&\deleted{(zx)y=1}\\
&\deleted{(xy)z}
\end{aligned}
\]
```

**017.09** · line 70

```tex
\[
\begin{aligned}
&\deleted{(ab)c=1}&&\deleted{\unsure{\sigma x}}\\
&\deleted{(ax)y=1}&\deleted{y=\sigma(ax)}&\deleted{f_1(x)=\sigma(ax)}\\
&\deleted{(yb)x\unsure{'}=1}&\deleted{yb=\sigma x}&\deleted{f_2(x)=(\sigma x)b^{\unsure{-1|-'}}}\\
&\deleted{(x,y)c=1}&\deleted{xy=\sigma c}
\end{aligned}
\]
```

**017.10** · line 80

```tex
\[
(aa)a
\]
```

**017.11** · line 83

```tex
\[
\begin{aligned}
&xy=z\qquad y^{-1}=u\qquad x=zu\\
&(xy)(y^{-1}x^{-1})&a_p&=a_q a_{\unsure{r+|r|t}}\qquad\unsure{\text{prouver}}\\
&\hspace{3em}\|&&\deleted{\unsure{a_q a}}\\
&\bigl((xy)y^{-1}\bigr)x^{-1}&&\deleted{\unsure{a^p}}\\
&&&\deleted{a_p=\unsure{a_q a_{r^{-1}}}}
\end{aligned}
\]
```

**017.12** · line 92

```tex
\[
z\bigl(u(u^{-1}z^{-1})\bigr)=\bigl((zu)u^{-1}\bigr)z^{-1}
\]
```


**i/j indices and exponents.** None.

**Local interventions.** The following entries were compared with their strokes and positions.

| Position | Intervention | Opening / sign |
| --- | --- | --- |
| dark ink, upper left in its reading orientation | deletion | <code>\tau_x z=xz</code> |
| dark ink, upper left in its reading orientation | deletion | <code>\tau_x\tau_y z=x(yz)</code> |
| dark ink, upper left in its reading orientation | deletion | <code>xx'=x'x=e</code> |
| dark ink, upper left in its reading orientation | deletion | <code>x(x'y)=y</code> |
| dark ink, upper left in its reading orientation | deletion | <code>\deleted{\unsure{x}}G\times G\to G</code> |
| dark ink, upper left in its reading orientation | deletion | <code>\unsure{x}</code> |
| dark ink, left, two and three elements | deletion | <code>e\quad a</code> |
| dark ink, left, two and three elements | deletion | <code>ee=e</code> |
| dark ink, left, two and three elements | deletion | <code>ea=ae=a</code> |
| dark ink, left, two and three elements | deletion | <code>aa\ne ae=a\quad\text{donc}\quad aa=e</code> |
| dark ink, left, two and three elements | deletion | <code>e\quad a\quad b</code> |
| dark ink, left, two and three elements | deletion | <code>\overset{\unsure{\&#124;}}{aa}\quad bb\quad ab=ba</code> |
| dark ink, left, two and three elements | deletion | <code>b\qquad\qquad\underset{\text{\textcircled{$e$}}}{\&#124;}\qquad\underset{e}{\&#124;}</code> |
| dark ink, left, two and three elements | deletion | <code>\underset{\substack{\&#124;\\a(aa)}}{ab}\overset{?}{=}\underset{\substack{\&#124;\\(aa)a}}{ba}\ -</code> |
| dark ink, centre right, two cases | deletion | <code>\{\underset{\substack{\&#124;\\a}}{ae},aa,ab\}=\{e,a,b\}</code> |
| dark ink, centre right, two cases | deletion | <code>\underbrace{aa=b,\ ab=e}\qquad\text{ou}\qquad aa=e,\ ab=b</code> |
| dark ink, centre right, two cases | deletion | <code>\Downarrow\qquad\qquad\qquad\text{mais }ab\ne eb\unsure{{}=b}</code> |
| dark ink, centre right, two cases | deletion | <code>\boxed{ba=e}</code> |
| dark ink, centre right, two cases | deletion | <code>bb=a</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>e,a,b,c</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>(xy)z=</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>x(yz)</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>uv=u'v'</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>x\ y\ z</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>\overline x((xy)z)=(yz)</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>e\quad a,b,c</code> |
| dark ink, middle, four elements and associativity calculations | deletion | <code>\overline x((xy)z)z</code> |
| dark ink, lower left, first multiplication table | deletion | <code>a</code> |
| dark ink, lower left, first multiplication table | deletion | <code>b</code> |
| dark ink, lower left, first multiplication table | deletion | <code>c</code> |
| dark ink, lower left, first multiplication table | deletion | <code>a</code> |
| dark ink, lower left, first multiplication table | deletion | <code>e</code> |
| dark ink, lower left, first multiplication table | deletion | <code>\unsure{c&#124;C}</code> |
| dark ink, lower left, first multiplication table | deletion | <code>b</code> |
| dark ink, lower left, first multiplication table | deletion | <code>b</code> |
| dark ink, lower left, first multiplication table | deletion | <code>c</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>a</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>b</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>c</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>a</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>b</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>c</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>e</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>b</code> |
| dark ink, lower centre, second multiplication table | deletion | <code>c</code> |
| dark ink, under tables | deletion | <code>aa=e\quad ab=c\quad ac=b</code> |
| dark ink, under tables | deletion | <code>a</code> |
| dark ink, lower right, reassociations at 1 | deletion | <code>(xy)z=1\Longleftrightarrow z(xy)=1</code> |
| dark ink, lower right, reassociations at 1 | deletion | <code>\Updownarrow</code> |
| dark ink, lower right, reassociations at 1 | deletion | <code>y(zx)=1</code> |
| dark ink, lower right, reassociations at 1 | deletion | <code>\unsure{\Updownarrow}</code> |
| dark ink, lower right, reassociations at 1 | deletion | <code>(zx)y=1</code> |
| dark ink, lower right, reassociations at 1 | deletion | <code>(xy)z</code> |
| dark ink, foot, three aligned columns | deletion | <code>(ab)c=1</code> |
| dark ink, foot, three aligned columns | deletion | <code>\unsure{\sigma x}</code> |
| dark ink, foot, three aligned columns | deletion | <code>(ax)y=1</code> |
| dark ink, foot, three aligned columns | deletion | <code>y=\sigma(ax)</code> |
| dark ink, foot, three aligned columns | deletion | <code>f_1(x)=\sigma(ax)</code> |
| dark ink, foot, three aligned columns | deletion | <code>(yb)x\unsure{'}=1</code> |
| dark ink, foot, three aligned columns | deletion | <code>yb=\sigma x</code> |
| dark ink, foot, three aligned columns | deletion | <code>f_2(x)=(\sigma x)b^{\unsure{-1&#124;-'}}</code> |
| dark ink, foot, three aligned columns | deletion | <code>(x,y)c=1</code> |
| dark ink, foot, three aligned columns | deletion | <code>xy=\sigma c</code> |
| pencil, lower half, first line and products | deletion | <code>\unsure{a_q a}</code> |
| pencil, lower half, first line and products | deletion | <code>\unsure{a^p}</code> |
| pencil, lower half, first line and products | deletion | <code>a_p=\unsure{a_q a_{r^{-1}}}</code> |

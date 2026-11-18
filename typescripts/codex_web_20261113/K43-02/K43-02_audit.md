# K43-02 — second visual reading

Each page was reread from its three supplied crops before opening its page file. Crop notes were saved first. Times are actual UTC times. The formula register includes uncertain and cancelled material; uncertainty marks are retained rather than silently resolved. No OCR or compilation was used.

## Scan 17

Start: 2026-11-17T20:57:30+00:00; crop notes saved before opening the page: 2026-11-17T20:58:20+00:00; end: 2026-11-17T20:59:15+00:00.

### Words and accents read independently from the crops

From the crops, before opening the source: “0 cycles”, “G_m-répartitions”, “proalgébriques”, “pts adéliques = répartitions”, “fts rationnelles = rép. principales”, “bicomplexe”, “Cohomologie”, quoted “torsion”, “diviseurs”, “pts rationnels de G”, “en l’occurrence”, “d’où”, “adèles entiers”, “classes d’adèles”, “G-diviseurs principaux”, “qui peuvent aussi s’exprimer à l’aide de quotients locaux -----”. Accents checked: ré-, adéliques, cohomologie without accent, è in adèles, ù in d’où. The middle aggregation sign contains both vertical and zigzag strokes: sum/product/coproduct candidates; lower index could be x or n. No prose spelling error securely identifiable.

### Visual checks

All top-strip objects and the oblique cancellation were reread, including the prime on C′, Δ_C, Alb, Pic and 0 cycles/G_m-répartitions. All four corners of both left squares were compared: upper product with cancelled loc, hats on O and K, ξ versus x, 0 and 1 superscripts. The middle aggregation sign was enlarged: vertical strokes coexist with a zigzag, so the candidate set was widened and sum placed first, rather than silently imposing a coproduct. The lower H^0 argument order was enlarged separately and marked doubtful. The right spectral-sequence display, both stars, Roman I/II, H_x^0=0 and the final two-term complex were compared symbol by symbol. No i/j indices occur; Roman I is not i. Labels beside the diagrams were read in their normal horizontal direction; “pts rationnels” replaces the earlier extra g. The entire top strip remains deleted; the small loc under the first product remains deleted. Live words near enclosing rules are not cancellations. The curved enclosure of the lower diagrams is now represented in TikZ. Structure-sheaf O retains script/plain alternatives at its first occurrence. No typed material or handwritten corrections on type occur. Final quotient wording remains uncertain.

### Changes (before → after)

```diff
--- before
+++ after
@@ -14,10 +14,10 @@
 \end{tikzcd}}
 \margin{\unsure{bicomplexe} $DD(G)$}
 \margin{Cohomologie $H^0(C,G)$ et $H^1(C,G)$}
-% L9--13: second square; the large coproduct signs are unusually formed.
+% L9--13: second square; the aggregation signs have superposed vertical and zigzag strokes.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\text{``\unsure{torsion}''}\quad\unsure{\coprod|\prod}_{x}H_x^0(G)\arrow[d] \& 0\arrow[l]\arrow[d]\\
-\text{diviseurs}\quad\coprod_x H_x^1(G) \& \underset{\text{\unsure{gpts rationnels} de $G$}}{H_\xi^0(G)}\arrow[l]
+\text{``\unsure{torsion}''}\quad\unsure{\sum|\prod|\coprod}_{\unsure{x|n}}H_x^0(G)\arrow[d] \& 0\arrow[l]\arrow[d]\\
+\text{diviseurs}\quad\sum_x H_x^1(G) \& \underset{\text{\unsure{pts rationnels} de $G$}}{H_\xi^0(G)}\arrow[l]
 \end{tikzcd}}
 \[
 \begin{aligned}
@@ -36,10 +36,10 @@
 \underbrace{\prod_{\unsure{x|\alpha}} H_x^1(G)}_{G\text{-diviseurs}}
 \]
 % L14--19: lower left group, enclosed on the sheet by a curved outline.
-\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\underset{\phantom{a}}{\overset{\text{\unsure{adèles entiers}}}{\prod G(\hat{\mathcal O}_x)}}\arrow[d] \& 0\arrow[l]\arrow[d] \& G(C)=H^0(C,G) \& 0\\
+\diagram{\begin{tikzpicture}\node[draw,rounded corners=7mm,inner sep=6pt]{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
+\underset{\phantom{a}}{\overset{\text{\unsure{adèles entiers}}}{\prod G(\hat{\mathcal O}_x)}}\arrow[d] \& 0\arrow[l]\arrow[d] \& G(C)=H^0(\unsure{C,C|G,C|C,G}) \& 0\\
 \underbrace{(\prod_{\mathrm{loc}}G(\hat K_x))/G(K_\xi)}_{\text{\unsure{classes d'adèles}}} \& 0\arrow[l] \& H^1(C,G) \& 0\\
 H_{\mathrm{II}}DD(G) \& \& H_{\mathrm I}H_{\mathrm{II}}DD(G)
-\end{tikzcd}}
+\end{tikzcd}};\end{tikzpicture}}
 % L20--21.
 qui peuvent aussi \unsure{s'exprimer} à l'aide de \unsure{quotients locaux} -----
```

### Formula and diagram register checked against the crops

1. Source line 5:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
\deleted{C\times C'} \& \deleted{C\times C} \& \deleted{C}\arrow[r,no head] \& \deleted{\mathrm{Alb}} \& \deleted{\text{$0$ cycles}/G_m\text{-répartitions}}\\
\deleted{\cup} \& \deleted{\cup} \& \& \deleted{\mathrm{Pic}}\\
\deleted{D} \& \deleted{\Delta_C}
\end{tikzcd}
```

2. Source line 11:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\text{\unsure{proalgébriques}}\quad\prod_{\deleted{\unsure{\mathrm{loc}}}}G(\unsure{\hat{\mathcal O}_x|\hat O_x})\arrow[d] \& 0\arrow[l]\arrow[d]\\
\substack{\text{\unsure{pts. adéliques}}\\=\text{\unsure{répartitions}}}\quad\prod_{\mathrm{loc}}G(\hat K_x) \& \underset{\substack{\text{\unsure{fts rationnelles}}\\=\text{rép. principales}}}{G(K_\xi)}\arrow[l]
\end{tikzcd}
```

3. Source line 15:

```latex
$DD(G)$
```

4. Source line 16:

```latex
$H^0(C,G)$
```

5. Source line 16:

```latex
$H^1(C,G)$
```

6. Source line 18:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\text{``\unsure{torsion}''}\quad\unsure{\sum|\prod|\coprod}_{\unsure{x|n}}H_x^0(G)\arrow[d] \& 0\arrow[l]\arrow[d]\\
\text{diviseurs}\quad\sum_x H_x^1(G) \& \underset{\text{\unsure{pts rationnels} de $G$}}{H_\xi^0(G)}\arrow[l]
\end{tikzcd}
```

7. Source line 22:

```latex
\[
\begin{aligned}
H_{\mathrm I}(DD(G))&\\[-3pt]
={}&E_1^{**}(G)\Rightarrow H^*(C,G)
\end{aligned}
\]
```

8. Source line 28:

```latex
$H_x^0(G)=0$
```

9. Source line 29:

```latex
\[
H^*(C,G)=\text{cohomologie}
\]
```

10. Source line 33:

```latex
\[
\underbrace{H_\xi^0(G)}_{\substack{G\text{-diviseurs}\\\text{principaux}}}
\unsure{\longrightarrow|\text{---}}
\underbrace{\prod_{\unsure{x|\alpha}} H_x^1(G)}_{G\text{-diviseurs}}
\]
```

11. Source line 39:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\underset{\phantom{a}}{\overset{\text{\unsure{adèles entiers}}}{\prod G(\hat{\mathcal O}_x)}}\arrow[d] \& 0\arrow[l]\arrow[d] \& G(C)=H^0(\unsure{C,C|G,C|C,G}) \& 0\\
\underbrace{(\prod_{\mathrm{loc}}G(\hat K_x))/G(K_\xi)}_{\text{\unsure{classes d'adèles}}} \& 0\arrow[l] \& H^1(C,G) \& 0\\
H_{\mathrm{II}}DD(G) \& \& H_{\mathrm I}H_{\mathrm{II}}DD(G)
\end{tikzcd}
```


## Scan 18

Start: 2026-11-17T20:59:15+00:00; crop notes saved before opening the page: 2026-11-17T20:59:58+00:00; end: 2026-11-17T21:00:40+00:00.

### Words and accents read independently from the crops

Before opening source: “jacobienne de C”; struck “La chose spéciale et surprenante, c’est que”; “l’on a aussi”; “si on prend le complexe”; “diviseurs ordinaires”; “Il faut aussi expliquer le rôle du J_x*”; live “La chose … primordiale : primo, c’est que”; “ou plutôt”; “n’est autre que”; “moyennant un abus de notations,, écrire” (two descending punctuation strokes after notations); cancelled “ce qui suggère que l’on ait”. Accents: spéciale, plutôt, rôle, rép-like letter not present, écrire has acute; no date. Plain J capitals with different bottom curves; first product and top arrow sharp; ξ has descender distinct from x.

### Visual checks

The top product, parenthesized 0 exponent, x, ξ, J_1, J_0=J_{K/k} and star on J_{C/k} were reread separately; the forms are J with a lower hook, not Greek Gamma. Both long diagonals and the enclosing cancellation apply to the entire central paragraph, including the Hom, K-star-to-divisors line and the sentence about J_x-star. No piece of that block was restored to live text. The underlining of H^1 is retained. The visible hat on O_x in the cancelled formula is retained, with its alphabet alternatives. The two lower complexes have a short horizontal connector whose head remains uncertain. Roman I and II, both DD, G_m and the underline under H_II DD were compared in the final equality. No i/j index occurs. The label du/de before J_x-star remains a marked alternative. The two punctuation descenders after notations were enlarged and both copied. The short final sentence is separately crossed out. There are no independent marginal notes, typed passages or corrections on type. The compact word before primordiale remains non/un; its sense has not been used to change the reading.

### Changes (before → after)

```diff
--- before
+++ after
@@ -16,13 +16,13 @@
 \]
 \deleted{] et que $J_x^{(0)}(k)=G_m(\unsure{\hat{\mathcal O}_x|\hat O_x})$.}
 
-\deleted{Il faut aussi expliquer le rôle de $J_x^*$.}
+\deleted{Il faut aussi expliquer le rôle \unsure{du|de} $J_x^*$.}
 % L13--19.
 La chose \unsure{non|un} \unsure{primordiale|principale} : \unsure{primo}, c'est que le complexe
 \[
 J_1\unsure{\longrightarrow|\text{---}}J_0
 \]
-(ou plutôt $J_1(k)\unsure{\longrightarrow|\text{---}}J_0(k)$) \unsure{n'est} autre que $H_{\mathrm{II}}DD(G_m)$, on peut donc, \unsure{moyennant} un abus de \unsure{notations}, écrire
+(ou plutôt $J_1(k)\unsure{\longrightarrow|\text{---}}J_0(k)$) \unsure{n'est} autre que $H_{\mathrm{II}}DD(G_m)$, on peut donc, \unsure{moyennant} un abus de \unsure{notations},, écrire
 \[
 H_{\mathrm I}DD(G)=\operatorname{Hom}\bigl(\underline{H_{\mathrm{II}}DD}(G_m),G\bigr)
 \]
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
\prod J_x^{(0)}\arrow[r]\arrow[d,equal] \& J_\xi^*\\
J_1 \& J_0=J_{K/k}
\end{tikzcd}
```

2. Source line 9:

```latex
\[
\deleted{\unsure{\mathrm{gr}}}\quad J_{C/k}^*\quad\text{jacobienne de }C
\]
```

3. Source line 13:

```latex
$J_{C/k}^*\simeq\underline{H}^1(C,G_m)$
```

4. Source line 13:

```latex
$\operatorname{Hom}_{k\text{-}\unsure{\mathrm{gr}}}(\unsure{J_*|J^*},G_m)$
```

5. Source line 14:

```latex
\[
\deleted{K^*\longrightarrow\substack{\text{diviseurs}\\\text{\unsure{ordinaires}}}}
\]
```

6. Source line 17:

```latex
$J_x^{(0)}(k)=G_m(\unsure{\hat{\mathcal O}_x|\hat O_x})$
```

7. Source line 19:

```latex
$J_x^*$
```

8. Source line 22:

```latex
\[
J_1\unsure{\longrightarrow|\text{---}}J_0
\]
```

9. Source line 25:

```latex
$J_1(k)\unsure{\longrightarrow|\text{---}}J_0(k)$
```

10. Source line 25:

```latex
$H_{\mathrm{II}}DD(G_m)$
```

11. Source line 26:

```latex
\[
H_{\mathrm I}DD(G)=\operatorname{Hom}\bigl(\underline{H_{\mathrm{II}}DD}(G_m),G\bigr)
\]
```


## Scan 19

Start: 2026-11-17T21:00:40+00:00; crop notes saved before opening the page: 2026-11-17T21:01:04+00:00; end: 2026-11-17T21:01:54+00:00.

### Words and accents read independently from the crops

Crop-first readings: “G-diviseur sur X” (singular appears possible), “i.e. on veut que cela corresponde à un G-diviseur véritable sur X”, “[sinon … le complexe continuerait-il ---]”; below the wavy separator all text is crossed: “G-répartition”, “Div premiers”, “classe de”, “Donc … est défini”, “Je dis que … existe. En effet la question étant locale, on est ramené au cas où … est formé d’unités,”. Accents read: répartition, véritable, défini, étant, ramené, où, formé, unités. x and ξ are distinct, D capital. The summed sign in the final paragraph is the same overwritten-looking zigzag/vertical form seen on 17.

### Visual checks

Every corner of the two upper squares was checked, including 0, the lower G(K), both hatted local fields and the lower H^1(X,G)/H^0(X,G). The right vertical strokes are wavy and remain squiggly arrows. The tiny note below the left square was enlarged again: ça/cela and the extra compressed word after sinon are now explicit alternatives; the rest remains marked where uncertain. The G-diviseur(s) label has an uncertain final plural and is now marked. All lower text lies below a separator and under three cancelling diagonals; every line remains deleted. The brace grouping, x∈X, D∈Div premiers, ξ_D∈J-star, x∈D, f_x, all K_D/O_D indices, quotient parentheses and superscript (1), Hom target G(k), the pairing subscript x and the summation index x∈|D| were reread. The isolated aggregation sign was reconciled with scan 17: sum/product/coproduct alternatives, not a confident product. No i/j index occurs. O is calligraphic/plain ambiguous, J has the same lower turn as on 18, ξ is not a script capital. The crossed denominator is a separate cancellation inside an already cancelled passage. The prose below the sum is cancelled too; the final comma is retained. No independent margin note, type, or addition to type occurs.

### Changes (before → after)

```diff
--- before
+++ after
@@ -3,15 +3,15 @@
 % L1--3, upper diagrams.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 \prod_x G(\unsure{\hat{\mathcal O}_x|\hat O_x})\arrow[d] \& 0\arrow[l]\arrow[d] \& 0\arrow[d,rightsquigarrow] \& 0\arrow[l]\arrow[d,rightsquigarrow]\\
-\prod_{\mathrm{local}}G(\hat K_x) \& G(K)\arrow[l] \& G\text{-diviseurs sur }X \& G(K)\arrow[l]\\
+\prod_{\mathrm{local}}G(\hat K_x) \& G(K)\arrow[l] \& G\text{-\unsure{diviseur|diviseurs} sur }X \& G(K)\arrow[l]\\
 \& \& H^1(X,G) \& H^0(X,G)
 \end{tikzcd}}
 % L4--9, small note below the first square.
-i.e. on \unsure{veut} que \unsure{ça corresponde} à un $G$-diviseur \unsure{véritable} sur $X$ [\unsure{sinon} le complexe \unsure{continuerait-il} ---]
+i.e. on \unsure{veut} que \unsure{ça corresponde|cela corresponde} à un $G$-diviseur \unsure{véritable} sur $X$ [\unsure{sinon donc|sinon dont} le complexe \unsure{continuerait-il} ---]
 % The horizontal rule between the two portions is a page separator.
 \par\medskip\hrule\medskip
 % L10--20: whole lower portion crossed by three oblique strokes.
-\[\deleted{\unsure{\prod|\sum}}\]
+\[\deleted{\unsure{\sum|\prod|\coprod}}\]
 \[
 \left\{\begin{aligned}
 &\deleted{(f_x)_{x\in X}}\quad\deleted{\text{$G$-répartition}}\\
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\prod_x G(\unsure{\hat{\mathcal O}_x|\hat O_x})\arrow[d] \& 0\arrow[l]\arrow[d] \& 0\arrow[d,rightsquigarrow] \& 0\arrow[l]\arrow[d,rightsquigarrow]\\
\prod_{\mathrm{local}}G(\hat K_x) \& G(K)\arrow[l] \& G\text{-\unsure{diviseur|diviseurs} sur }X \& G(K)\arrow[l]\\
\& \& H^1(X,G) \& H^0(X,G)
\end{tikzcd}
```

2. Source line 10:

```latex
$G$
```

3. Source line 10:

```latex
$X$
```

4. Source line 14:

```latex
\[\deleted{\unsure{\sum|\prod|\coprod}}\]
```

5. Source line 15:

```latex
\[
\left\{\begin{aligned}
&\deleted{(f_x)_{x\in X}}\quad\deleted{\text{$G$-répartition}}\\
&\deleted{(\xi_D)_{D\in\mathrm{Div}\,\text{\unsure{premiers}}}}\qquad
\deleted{\xi_D\in J_{\underline{\mathcal O}_D/k}^*}
\end{aligned}\right.
\]
```

6. Source line 22:

```latex
\[
\begin{aligned}
\deleted{x\in D}\qquad
\deleted{f_x\in G(K_x)}&\deleted{\longrightarrow\text{\unsure{classe de} }G(K_D)/\deleted{\unsure{G(\mathcal O_D)}}}\quad
\deleted{\unsure{\simeq|\longrightarrow}\ G(K_D)/G(\mathcal O_D)^{(1)}}\\
&\deleted{\hspace{4em}\simeq\operatorname{Hom}(J_{\underline{\mathcal O}_D/k}^*,G(k))}
\end{aligned}
\]
```

7. Source line 30:

```latex
$(f_x,\xi_D)_x\in G(k)$
```

8. Source line 32:

```latex
$\sum_{x\in|D|}(f_x,\xi_D)$
```

9. Source line 32:

```latex
$(f_x)$
```


## Scan 20

Start: 2026-11-17T21:01:54+00:00; crop notes saved before opening the page: 2026-11-17T21:02:27+00:00; end: 2026-11-17T21:04:04+00:00.

### Words and accents read independently from the crops

Before opening source: this page is diagrams throughout. Textual labels read “Alb”, cancelled “Alb”, “Diviseurs” cancelled, “local” under products, and “Div”. All 0 superscripts are small round loops; stars have separate rays. J has a long low hook, except the far lower-right form which may be gamma-like. No accented prose or date. Question marks occur in the crossed top diagonals and in the two lower proposed sequences. G(C) at the left of the penultimate diamond is not itself crossed through; the nearby branch strokes are crossed. The last aggregation sign resembles the sum/product overlay on 17 and 19.

### Visual checks

The page was reread as seven diagram units: (1) both top sequences and their crossed diagonals; (2) X → product → J_K/k^0 → J_X/k^0 → 0 with cancelled superscript and Alb; (3) question-mark sequence with parentheses and outer 0; (4) circled question mark and cancelled Diviseurs; (5) the two-level square, including upward directions and the headless lower connector; (6) the R_G^0 diamond; (7) the final product/Jacobian diamond. Every 0 versus star, D, K/k, k(D)/k, local/loc label and question mark was compared in the formula register. No i/j index occurs; J_1 has digit 1. The penultimate diamond was enlarged separately: its oblique strokes enclose the internal nodes and intersect connectors, but do not strike the three labels through. Their erroneous deleted wrappers were removed. This remains the least certain graphic-state interpretation on this page and is recorded in the doubts. Other crossed items (Alb, exponent and Diviseurs) remain deleted. The last aggregation glyph was reconciled with 17/19 by adding product to its alternatives; the final J/gamma-like capital is now marked. Z is not confidently double struck; it remains plain Z. O retains the first-occurrence alphabet doubt. No prose margins, typing or additions to type occur.

### Changes (before → after)

```diff
--- before
+++ after
@@ -24,16 +24,16 @@
 \prod_{\unsure{\mathrm{loc}}}J_{\underline{\mathcal O}_D/k}^0\arrow[u]\arrow[r,no head] \& \prod J_{\underline{\mathcal O}_D/k}^0\arrow[u]
 \end{tikzcd}}
 \par\medskip\hrule\medskip
-% L9--11: diamond, with the left diamond crossed out on the sheet.
+% L9--11: diamond; oblique quadrilateral around the left internal nodes.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\&\deleted{\prod G(\underline{\mathcal O}_x)}\arrow[dr,no head]\&\&J_G^0\arrow[dr,no head]\\
-\deleted{G(C)}\arrow[ur,no head]\arrow[dr]\&\&R_G^0\arrow[ur,no head]\arrow[dr]\&\&H^1(X,G)^0\\
-\&\deleted{G(K)}\arrow[ur,no head]\&\&\mathrm{Div}_G^0\arrow[ur,no head]
+\&\prod G(\underline{\mathcal O}_x)\arrow[dr,no head]\&\&J_G^0\arrow[dr,no head]\\
+G(C)\arrow[ur,no head]\arrow[dr]\&\&R_G^0\arrow[ur,no head]\arrow[dr]\&\&H^1(X,G)^0\\
+\&G(K)\arrow[ur,no head]\&\&\mathrm{Div}_G^0\arrow[ur,no head]
 \end{tikzcd}}
 \par\medskip\hrule\medskip
 % L12--14: final diamond. Question marks are manuscript text.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 \&J_1=\prod J_{\underline{\mathcal O}_D/k}^0\arrow[dr]\&\&J_{K/k}^0\arrow[dr]\\
-?\arrow[ur]\arrow[dr]\&\&(\prod_{\substack{D\\\mathrm{local}}}J_{\underline{\mathcal O}_D/k}^*)^0\arrow[ur]\arrow[dr]\&\&J_{X/k}^0\\
-\&?\arrow[ur]\&\&(\unsure{\sum|\coprod}_{D}\deleted{\unsure{\mathrm{loc}}}J_{k(D)/k}^*)^0\arrow[ur]
+?\arrow[ur]\arrow[dr]\&\&(\prod_{\substack{D\\\mathrm{local}}}J_{\underline{\mathcal O}_D/k}^*)^0\arrow[ur]\arrow[dr]\&\&\unsure{J|\gamma}_{X/k}^0\\
+\&?\arrow[ur]\&\&(\unsure{\sum|\prod|\coprod}_{D}\deleted{\unsure{\mathrm{loc}}}J_{k(D)/k}^*)^0\arrow[ur]
 \end{tikzcd}}
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
0\arrow[r] \& N\arrow[r]\arrow[dr,"?","{\times}" description] \& Z^0\arrow[r] \& \mathrm{Alb}^0\arrow[r] \&0\\
0\arrow[r,no head] \& \dfrac{\prod G(\unsure{\underline{\mathcal O}_x|\underline O_x})}{G(C)}\arrow[r]\arrow[ur,no head] \& R_G^0/G(K)\arrow[r,no head] \& H^1(X,G)^0\arrow[r,no head] \&0
\end{tikzcd}
```

2. Source line 9:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
X\arrow[r] \& \prod_D J_{\underline{\mathcal O}_D/k}^{\deleted{\unsure{*}}0}\arrow[r] \& J_{K/k}^0\arrow[r,no head,"\vert" description] \& \deleted{\mathrm{Alb}^0}J_{X/k}^0\arrow[r,no head] \&0
\end{tikzcd}
```

3. Source line 13:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
?\arrow[r] \& (\prod_D J_{\underline{\mathcal O}_D/k}^*)^0\arrow[r,"\vert" description] \& J_{X/k}^0\arrow[r,no head] \&0
\end{tikzcd}
```

4. Source line 18:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
\text{\textcircled{?}}\arrow[r] \& \underset{\deleted{\unsure{\mathrm{Diviseurs}}}}{\prod J_{k(D)/k}^*}\arrow[r] \& J_{X/k}^*
\end{tikzcd}
```

5. Source line 22:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\prod_{\mathrm{local}}J_{\underline{\mathcal O}_D/k}^*\arrow[r] \& J_{K/k}^*\\
\prod_{\unsure{\mathrm{loc}}}J_{\underline{\mathcal O}_D/k}^0\arrow[u]\arrow[r,no head] \& \prod J_{\underline{\mathcal O}_D/k}^0\arrow[u]
\end{tikzcd}
```

6. Source line 28:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\&\prod G(\underline{\mathcal O}_x)\arrow[dr,no head]\&\&J_G^0\arrow[dr,no head]\\
G(C)\arrow[ur,no head]\arrow[dr]\&\&R_G^0\arrow[ur,no head]\arrow[dr]\&\&H^1(X,G)^0\\
\&G(K)\arrow[ur,no head]\&\&\mathrm{Div}_G^0\arrow[ur,no head]
\end{tikzcd}
```

7. Source line 35:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\&J_1=\prod J_{\underline{\mathcal O}_D/k}^0\arrow[dr]\&\&J_{K/k}^0\arrow[dr]\\
?\arrow[ur]\arrow[dr]\&\&(\prod_{\substack{D\\\mathrm{local}}}J_{\underline{\mathcal O}_D/k}^*)^0\arrow[ur]\arrow[dr]\&\&\unsure{J|\gamma}_{X/k}^0\\
\&?\arrow[ur]\&\&(\unsure{\sum|\prod|\coprod}_{D}\deleted{\unsure{\mathrm{loc}}}J_{k(D)/k}^*)^0\arrow[ur]
\end{tikzcd}
```


## Scan 21

Start: 2026-11-17T21:04:04+00:00; crop notes saved before opening the page: 2026-11-17T21:05:27+00:00; end: 2026-11-17T21:06:16+00:00.

### Words and accents read independently from the crops

Before opening source: “cup” twice, both underlined (the upper label doubly); “projectif”, “résolution”, “Γ-hom”, “ss-groupe”, “fibré principal sous A”, “Pic”. Accents: résolution acute, fibré acute, no other prose accent. Three plain A/prime forms; Z has visibly doubled diagonal in several positions. Γ is angular with no script loop. The right Ext operators have tall connected terminal strokes that can be t or a t followed by an exponent; i/1 and j/1 must remain unresolved rather than inferred from the degree equations. The two equations are i+j+1=2 and i+j=1: i has dot and short stem, j has dot and descender. The circled right expression reads 1-j, with j descender. Bottom 2 and -1 are separate. The upper homological display uses a semicolon after A′_L; the first stacked Ext uses a semicolon after Z, the second a comma.

### Visual checks

The two upper pairing factors, the equality A_K beneath H^0 and the corrected K→L in H^2 were checked symbol by symbol. The relative Ext base was enlarged: its opening stroke is curved, so Z(Γ)/Z is now first, with square brackets retained as an alternative. The operators in the stacked Ext block were enlarged independently: some supposed exponents are inseparable from the terminal t. Whole-operator alternatives now include no exponent, rather than asserting a degree from context. The third operator has a 2/1/i+j doubt; the later explicit 2 exponents are distinct. All semicolons versus commas were checked, especially Z;A_L versus Z,A′_L and the pairings with L-star. Every i/j is in the degree equations or the marked Ext candidates: j has a descender, i a dot without descender; the circled expression is 1-j, not a silently corrected 1-i. The A_1/A_2 resolutions, primes, stars on L/M, Γ invariants, tensor Z subscripts, P/Q exponents, lower tilde, arrows and equal sign in the tensor square were reread. Bottom fraction, norm L/k, subgroup H^1, isolated K,L,Z,A,P and Pic_{P/S} were checked. Cancelled K/G at top, star after A′_L, P,Q above the square and H^1( at bottom remain deleted. Live heavy A and L are not treated as bold; doubled diagonals on Z are rendered mathbb. Script L and M retain candidate alphabets. There are no independent marginal notes, typescripts or handwritten additions to type. Underlines beneath cup/projectif/résolution/Pic remain.

### Changes (before → after)

```diff
--- before
+++ after
@@ -13,7 +13,7 @@
 A_K\arrow[u,equal]
 \end{tikzcd}}
 \[
-\operatorname{Ext}_{\unsure{\mathbb Z[\Gamma]/\mathbb Z|\mathbb Z(\Gamma)/\mathbb Z}}^1(A_L,A'_L\deleted{\unsure{*}};L^*)
+\unsure{\operatorname{Ext}|\operatorname{Ext}^1}_{\unsure{\mathbb Z(\Gamma)/\mathbb Z|\mathbb Z[\Gamma]/\mathbb Z}}(A_L,A'_L\deleted{\unsure{*}};L^*)
 \]
 % L4--8: left resolution sketch, crossed diagonals drawn without arrowheads.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
@@ -27,8 +27,8 @@
 \]
 % L4--10: right product and composition diagram.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=large]
-\begin{gathered}\operatorname{Ext}_\Gamma^{\unsure{i|1}}(\mathbb Z;A_L)\\\times\\\operatorname{Ext}_\Gamma^{\unsure{j|1}}(\mathbb Z,A'_L)\end{gathered}\arrow[d]\\
-\operatorname{Ext}_\Gamma^{\unsure{1|i+j}}(\mathbb Z,\mathbb Z;A_L,A'_L)\times\operatorname{Ext}_\Gamma^1(A_L,A'_L;L^*)\arrow[d]\\
+\begin{gathered}\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i}}_\Gamma(\mathbb Z;A_L)\\\times\\\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{j}}_\Gamma(\mathbb Z,A'_L)\end{gathered}\arrow[d]\\
+\unsure{\operatorname{Ext}^{2}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i+j}}_\Gamma(\mathbb Z,\mathbb Z;A_L,A'_L)\times\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}}_\Gamma(A_L,A'_L;L^*)\arrow[d]\\
 \operatorname{Ext}_\Gamma^2(\mathbb Z,\mathbb Z;L^*)\arrow[d,"{\text{\uuline{\unsure{cup}}}}"]\\
 \unsure{\operatorname{Ex}|\operatorname{Ext}}_\Gamma^2(\mathbb Z,L^*)
 \end{tikzcd}}
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
\[
\begin{array}{cc}
A&A'\\
k&\deleted{\unsure{K}}L\\
\multicolumn{2}{c}{\overline{\deleted{\unsure{G}}\Gamma}}
\end{array}
\]
```

2. Source line 11:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
H^0(\Gamma,A_L)\times H^1(\Gamma,A'_L)\arrow[r] \& H^2(\Gamma,\deleted{\unsure{K}}L^*)\\
A_K\arrow[u,equal]
\end{tikzcd}
```

3. Source line 15:

```latex
\[
\unsure{\operatorname{Ext}|\operatorname{Ext}^1}_{\unsure{\mathbb Z(\Gamma)/\mathbb Z|\mathbb Z[\Gamma]/\mathbb Z}}(A_L,A'_L\deleted{\unsure{*}};L^*)
\]
```

4. Source line 19:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
A\&A'\\
A_1\arrow[u]\arrow[dr,no head]\&A'_1\arrow[u]\\
A_2\arrow[u]\arrow[ur,no head]\&A'_2\arrow[u]\\
0\arrow[u]\&0\arrow[u]
\end{tikzcd}
```

5. Source line 25:

```latex
\[
\unsure{\mathcal L_*|\mathscr L_*}\qquad \mathcal L'_*
\]
```

6. Source line 29:

```latex
\begin{tikzcd}[ampersand replacement=\&,row sep=large]
\begin{gathered}\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i}}_\Gamma(\mathbb Z;A_L)\\\times\\\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{j}}_\Gamma(\mathbb Z,A'_L)\end{gathered}\arrow[d]\\
\unsure{\operatorname{Ext}^{2}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i+j}}_\Gamma(\mathbb Z,\mathbb Z;A_L,A'_L)\times\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}}_\Gamma(A_L,A'_L;L^*)\arrow[d]\\
\operatorname{Ext}_\Gamma^2(\mathbb Z,\mathbb Z;L^*)\arrow[d,"{\text{\uuline{\unsure{cup}}}}"]\\
\unsure{\operatorname{Ex}|\operatorname{Ext}}_\Gamma^2(\mathbb Z,L^*)
\end{tikzcd}
```

7. Source line 36:

```latex
\[
\operatorname{Hom}(\mathcal L_*,\mathcal L'_*;L^*)
\]
```

8. Source line 39:

```latex
\[
\begin{aligned}
&H^1\bigl(\operatorname{Hom}(\mathcal L_*\otimes_{\mathbb Z}\mathcal L'_*,G)^\Gamma\bigr)\\
&H^1\bigl(\operatorname{Hom}(\unsure{M_*|\mathcal M_*},\mathcal L_*)^\Gamma\bigr)\\
&H^1\bigl(\operatorname{Hom}(M_*,\mathcal L'_*)^\Gamma\bigr)
\end{aligned}
\]
```

9. Source line 46:

```latex
\[
\begin{aligned}i+j+1&=2\\i+j&=1\end{aligned}
\qquad
\begin{array}{cc}\text{\textcircled{$i$}}&\text{\textcircled{$1-j$}}\\2&-1\end{array}
\]
```

10. Source line 52:

```latex
\begin{tikzcd}[ampersand replacement=\&]
M_*\arrow[r,no head,"{\Gamma\text{-}\unsure{\mathrm{hom}}}"]\&\mathcal L_*\\
M_*\arrow[r,no head,"{\Gamma\text{-}\mathrm{hom}}"]\&\mathcal L'_*
\end{tikzcd}
```

11. Source line 56:

```latex
\[\deleted{P,Q}\]
```

12. Source line 57:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
\text{\uline{\unsure{projectif}}}\quad\mathcal L_*^P\otimes\mathcal L_*^Q\arrow[r,no head]\arrow[d] \& P\otimes Q\arrow[d,equal]\\
\text{\uline{résolution}}\quad\tilde{\mathcal L}_*^{P\otimes Q}\arrow[r]\&P\otimes Q
\end{tikzcd}
```

13. Source line 62:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
M_*\otimes_{\mathbb Z}M_*\arrow[r,"{\Gamma\text{-}\mathrm{hom}}"]\&\mathcal L_*\otimes_{\mathbb Z}\mathcal L'_*\arrow[r,"{\Gamma\text{-}\mathrm{hom}}"]\&G\\
M_*\arrow[u,"{\text{\uuline{\unsure{cup}}}\ 2}"]
\end{tikzcd}
```

14. Source line 66:

```latex
\[
\frac{1}{A_K/N_{L/k}A_L\ /\ \substack{\text{\unsure{ss-groupe}}\\\text{de }H^1(\Gamma,A'_L)}}
\]
```

15. Source line 70:

```latex
\[
K,L\qquad\mathbb Z\qquad A\quad P\quad\text{fibré principal sous }A
\]
```

16. Source line 73:

```latex
\[
\deleted{H^1(}\qquad\underline{\operatorname{Pic}}_{P/S}
\]
```


## Scan 22

Start: 2026-11-17T21:06:16+00:00; crop notes saved before opening the page: 2026-11-17T21:07:21+00:00; end: 2026-11-17T21:07:52+00:00.

### Words and accents read independently from the crops

Crop-first words: “X complet” underlined; “Z de codim 2”; “Div” repeatedly crossed; “Im”, “Ker u”; tiny qualifier below equals resembles “pl.-isib.”; “Ex. Néron-Severi”; boxed “A-t-on égalité ???”; slanted “Aucun accouplement convenable ne semble exister…..”; “Quel était l’accouplement -étique de Tate ???” (suffix could -adique, but the middle letter looks t). Accents: Néron, égalité, était. The right margin was rotated and reread. The standalone Div_G and G(K)/G(C) share one cancelling line. A small dot is visible just after the vertical bar before Ker u. Final aggregate has a plain sigma shape, unlike the composite sign on 17.

### Visual checks

All objects, headless connectors, crossing diagonals and vertical bars in both pairs of sequences were compared. Particular attention went to codimension 2 under the first product, the map label u, the underline and question mark beneath the next product, and all external 0 exponents. Both Hom definitions were reread without supplying a missing second Hom argument. The qualifier under equals remains unresolved; its candidates now include the more literal pl.-isib. The small dot after the vertical bar before Ker u was restored. The arrow from Im to Ker, both boxed inclusions, H_1 subscripts (digit 1, not i), J_* stars, cancelled (k), G_m and A/A′/A″ were checked. No i/j variable index occurs. The standalone Div_G and quotient are both inside the same deleted block. The right slanted note was rotated; its compressed words retain doubts, and the count of terminal dots is now explicitly uncertain. The final Tate word was enlarged and reordered to -étique|-adique, based on its visible t-like stroke, without replacing it by expected terminology. Script/plain O and the gamma-like J_X/k remain marked. No typed page or addition to type occurs. The lower curve beside the two sequences is an enclosing annotation, not a deletion of the sequences.

### Changes (before → after)

```diff
--- before
+++ after
@@ -12,7 +12,7 @@
 \deleted{\unsure{Div c Div}}
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 (G\text{-}\mathrm{Div})=\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0/\&\operatorname{Im}(\prod_{Z\text{ cod., }2}J_{\underline{\mathcal O}_Z/k})\bigr)\arrow[d]\\
-(G\text{-}\mathrm{Div})^0\underset{\text{\unsure{pl.-isom}}}{=}\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0\&\mid\operatorname{Ker}u\bigr)
+(G\text{-}\mathrm{Div})^0\underset{\text{\unsure{pl.-isib.|pl.-isom}}}{=}\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0\&\mid .\operatorname{Ker}u\bigr)
 \end{tikzcd}}
 % L7--9: boxed statements.
 \[
@@ -32,6 +32,6 @@
 0\arrow[r,no head]\&?\arrow[r,no head]\arrow[ur,"?"]\&(\sum_D J_{k(D)/k}^*)^0\arrow[r,no head]\&J_{X/k}^0\arrow[r,no head]\&0
 \end{tikzcd}}
 % slanted
-\margin{\unsure{Aucun} \unsure{accouplement} \unsure{convenable} \unsure{ne semble} \unsure{exister} ....}
+\margin{Aucun \unsure{accouplement} \unsure{convenable} \unsure{ne semble} \unsure{exister} \unsure{.....|....}}
 \[G(L)\]
-\unsure{Quel} était l'accouplement \unsure{-adique|-étique} de Tate ???
+\unsure{Quel} était l'accouplement \unsure{-étique|-adique} de Tate ???
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
0\arrow[r,no head]\&G(K)/G(C)\arrow[r]\arrow[dr,no head]\&\mathrm{Div}_G^0\arrow[r,no head,"\vert" description]\&\deleted{\unsure{D}}H^1(X,G)^0\arrow[r,no head]\&0\\
\prod_{\substack{Z\text{ de}\\\text{codim }2}}J_{\unsure{\underline{\mathcal O}_Z|\underline O_Z}/k}\arrow[r]\&\underset{?}{\underline{\prod J_{\underline{\mathcal O}_D/k}^0}}\arrow[r,"u"']\arrow[ur,no head]\&J_{K/k}^0\arrow[r,"\vert" description]\&\unsure{J|\gamma}_{X/k}^0\arrow[r,no head]\&0
\end{tikzcd}
```

2. Source line 8:

```latex
$X$
```

3. Source line 10:

```latex
\[\deleted{\mathrm{Div}_G\qquad G(K)/G(C)}\]
```

4. Source line 13:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
(G\text{-}\mathrm{Div})=\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0/\&\operatorname{Im}(\prod_{Z\text{ cod., }2}J_{\underline{\mathcal O}_Z/k})\bigr)\arrow[d]\\
(G\text{-}\mathrm{Div})^0\underset{\text{\unsure{pl.-isib.|pl.-isom}}}{=}\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0\&\mid .\operatorname{Ker}u\bigr)
\end{tikzcd}
```

5. Source line 18:

```latex
\[
\boxed{(G\text{-}\mathrm{Div})/(G\text{-}\mathrm{Div})^0\subset\operatorname{Hom}(H_1(J_*),G\deleted{\unsure{(k)}})}
\]
```

6. Source line 21:

```latex
\[
\boxed{\text{Ex. Néron-Severi}\ \subset\operatorname{Hom}(H_1(J_*),G_m)}
\]
```

7. Source line 25:

```latex
\begin{tikzcd}[ampersand replacement=\&]
0\arrow[r]\&A'\arrow[r,no head]\arrow[d,no head]\&A\arrow[r,no head]\arrow[d,no head]\&A''\arrow[r]\arrow[d,no head]\&0\\
\&\phantom{A'}\&\phantom A\&\phantom{A''}
\end{tikzcd}
```

8. Source line 30:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
0\arrow[r,no head]\&\dfrac{\prod G(\underline{\mathcal O}_x)}{G(C)}\arrow[r]\arrow[dr,"?","\times" description]\&J_G^0\arrow[r]\&H^1(X,G)^0\arrow[r,no head]\&0\\
0\arrow[r,no head]\&?\arrow[r,no head]\arrow[ur,"?"]\&(\sum_D J_{k(D)/k}^*)^0\arrow[r,no head]\&J_{X/k}^0\arrow[r,no head]\&0
\end{tikzcd}
```

9. Source line 36:

```latex
\[G(L)\]
```


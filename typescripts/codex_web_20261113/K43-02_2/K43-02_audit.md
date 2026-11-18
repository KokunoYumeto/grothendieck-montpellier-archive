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


## Scan 23

Start: 2026-11-17T23:40:50+00:00; crop notes saved before opening the page: 2026-11-17T23:44:05+00:00; end: 2026-11-17T23:44:30+00:00.

### Words and accents read independently from the crops

G-diviseur; circled insertion ordinaire/bilatéral (strokes cross the word); horizontal rel. à la projection; transforme 0-cycles de X en G-diviseurs sur Y; noyau d’Albanese; principaux (?). Cancelled Diviseur. Noyau de Albanese; 0-cycles de deg 0; Albanese de X; au. alg.ᵗ équiv. à 0 (first abbreviation uncertain); classes de fibrés alg. équiv. à 0. Accents à, équiv., fibrés checked. Ext terminal t / superscript 1 uncertain. Last looped capital differs from plain J: script J, J, gamma candidates. K_Y has Y below K. No indexed i/j visible.

### Visual checks

All formulas and both rows of the main diagram reread from the crops: stars on the two Picard expressions, absence/presence of G, Z_X^0, J_X/k^0, K_Y/k, Div^0 and Pic^0, all zeros, parentheses and arrows. The last capital has a descending loop with an upward diagonal: script J is added and placed first; plain J/gamma remain possible. No indexed i or j. The isolated Diviseur and the first G are crossed; Y is written over X in Div. The circled insertion is reproduced with an enclosure, though strokes through its first letters leave the cancellation state uncertain; this is recorded as a reading issue, not a confident deletion. The curve touching the first Pic is an incoming arrow, not treated as a strike. No typed corrections or marginal prose. Accent and ending checks include principaux, fibrés and équiv.; the compressed au. alg. qualifier remains unsure. Ext terminal t cannot confidently be separated from superscript 1, so the no-exponent candidate is added. All source formulas follow below.

### Changes (before → after)

```diff
--- before
+++ after
@@ -1,9 +1,9 @@
 \scanpage{23}
 % archive sheet number: 22
 % L1.
-\[X\times Y\qquad A\quad\operatorname{Ext}^1(A,G)\]
+\[X\times Y\qquad A\quad\unsure{\operatorname{Ext}|\operatorname{Ext}^1}(A,G)\]
 % L2--5.
-$D$ \deleted{\unsure{G}} $G$-diviseur \inserted{\unsure{ordinaire|bilatéral}} sur $X\times Y$, \unsure{horizontal} \unsure{rel.} à \unsure{la projection} $X\times Y\longrightarrow X$ transforme $0$-cycles de $X$ en $G$-diviseurs sur $Y$, et $0$-cycles du noyau d'Albanese en $G$-diviseurs principaux (?).
+$D$ \deleted{\unsure{G}} $G$-diviseur \inserted{\tikz[baseline=(w.base)]{\node[draw,rounded corners=12pt,inner sep=2pt] (w) {\unsure{ordinaire|bilatéral}};}} sur $X\times Y$, \unsure{horizontal} \unsure{rel.} à \unsure{la projection} $X\times Y\longrightarrow X$ transforme $0$-cycles de $X$ en $G$-diviseurs sur $Y$, et $0$-cycles du noyau d'Albanese en $G$-diviseurs principaux (?).
 
 \deleted{\unsure{Diviseur}}
 % L6--8.
@@ -21,5 +21,5 @@
 \end{tikzcd}}
 % L15, bottom sequence.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
-0\arrow[r,no head]\&\text{Noyau}\arrow[r]\&J_{K_Y/k}^0\arrow[r,no head]\&\unsure{J|\gamma}_{Y/k}^0\arrow[r]\&0
+0\arrow[r,no head]\&\text{Noyau}\arrow[r]\&J_{K_Y/k}^0\arrow[r,no head]\&\unsure{\mathscr J|J|\gamma}_{Y/k}^0\arrow[r]\&0
 \end{tikzcd}}
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
\[X\times Y\qquad A\quad\unsure{\operatorname{Ext}|\operatorname{Ext}^1}(A,G)\]
```

2. Source line 6:

```latex
$D$
```

3. Source line 6:

```latex
$G$
```

4. Source line 6:

```latex
$X\times Y$
```

5. Source line 6:

```latex
$X\times Y\longrightarrow X$
```

6. Source line 6:

```latex
$0$
```

7. Source line 6:

```latex
$X$
```

8. Source line 6:

```latex
$G$
```

9. Source line 6:

```latex
$Y$
```

10. Source line 6:

```latex
$0$
```

11. Source line 6:

```latex
$G$
```

12. Source line 10:

```latex
\begin{tikzcd}[ampersand replacement=\&]
X\times Y\arrow[dr]\\
\&\unsure{\operatorname{Pic}^*(Y)}
\end{tikzcd}
```

13. Source line 14:

```latex
\begin{tikzcd}[ampersand replacement=\&]
J_{X/k}^*\arrow[r]\&\operatorname{Pic}_G^*(Y)
\end{tikzcd}
```

14. Source line 18:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
0\arrow[r,no head]\&\substack{\text{Noyau de}\\\text{Albanese}}\arrow[r,no head]\arrow[d]\&\underset{\substack{0\text{-cycles}\\\text{de deg }0}}{Z_X^0}\arrow[r]\arrow[d]\&\underset{\text{Albanese de }X}{J_{X/k}^0}\arrow[r,no head]\arrow[d]\&0\\
0\arrow[r,no head]\&G(K)/G(Y)\arrow[r]\&\underset{\substack{\text{\unsure{au. alg.\textsuperscript{t}}}\\\text{équiv. à }0}}{\mathrm{Div}^0(\deleted{\unsure{X}}Y,G)}\arrow[r]\&\underset{\substack{\text{classes de fibrés}\\\text{alg. équiv. à }0}}{\operatorname{Pic}^0(Y,G)}\arrow[r]\&0
\end{tikzcd}
```

15. Source line 23:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
0\arrow[r,no head]\&\text{Noyau}\arrow[r]\&J_{K_Y/k}^0\arrow[r,no head]\&\unsure{\mathscr J|J|\gamma}_{Y/k}^0\arrow[r]\&0
\end{tikzcd}
```


## Scan 24

Start: 2026-11-17T23:44:30+00:00; crop notes saved before opening the page: 2026-11-17T23:44:44+00:00; end: 2026-11-17T23:44:49+00:00.

### Words and accents read independently from the crops

Théorie de Rosenlicht, sole upper-right title. Accent on Théorie and compressed middle letters remain uncertain. Lower-left pencil 23 is the archive number. Middle and bottom crops otherwise blank; no date or page count.

### Visual checks

The only text is the upper-right title; all three crops inspected for faint additions. Théorie remains unsure, and Rosenlicht agrees with its separately read title on scan 25. No formulas, indices, script capitals, margins, corrections or deletions. No change. This mostly blank cover necessarily has a short audit; no extended prose is implied.

### Changes (before → after)

No change.

### Formula and diagram register checked against the crops


## Scan 25

Start: 2026-11-17T23:44:49+00:00; crop notes saved before opening the page: 2026-11-17T23:45:28+00:00; end: 2026-11-17T23:45:53+00:00.

### Words and accents read independently from the crops

Théorie de Rosenlicht; Existence des Picard pour les courbes. Soit X un Y-schéma, avec; Y loc. noethérien; X propre sur Y (faut-il même: loc. projectif ?); X plat sur Y. Les fibres de X sur S sont des courbes algébriques absolument; crowded revisions connexes / irréductibles / réduites, then et absolument connexes above struck réduites; [ce dernier pt n’est pas essentiel---]. Le nb de composantes [struck word] irré d./irré d. absolues des fibres de X sur Y est loc constant sur Y. Slanted: si on abandonne cette hypothèse, on tombe aux phénomènes à la Néron ?! (compressed words doubtful). Alors le S/f-schéma P_X/Y relatif existe, et est simple sur Y. De plus; composantes irréductibles absolues; revêtement; étale; degré; références in margin. Sur Y′ devient isomorphe à Z^n; augmentation, struck surjective et propre, fidèlement plate; noyau sera noté P^c; d’où la suite exacte. Noter que l’on a un homomorphisme canonique; donc une augmentation. Accents Théorie, schéma, noethérien, même, algébriques, réduites, irréductibles, phénomènes, Néron, à, étale, degré, fidèlement, noté checked, unresolved at overwritten spots.

### Visual checks

Read all hypotheses and the additions in their actual positions. Condition d has connexes and irréductibles struck, reduced-word stack retained as unsure where overwritten; lower réduites is struck and connexes inserted above it. Condition e has a fully obliterated word (one-word estimate). The slanted Néron note was reread in its rotated crop; the compressed trouve des / tombe aux segment is now marked rather than confidently resolved. The underlined marginal références remains tentative. The deleted Y before étale and crossed surjective et propre are included; the small cancelled sign after the first augmentation remains a symbol doubt. No i/j index; n, c, Y′, Y and S individually checked: c remains open, not a zero; condition d and S/f-schéma are not normalized to Y. Script/calligraphic P alternatives retained; the doubled diagonal in every integer Z supports mathbb, unlike the P. All four displays and inline formulas reread, including product subscript Y′/Y, Hom subscript Y, its arguments, the sequence and both final augmentations. A terminal segment before zero in the sequence has no secure arrowhead and is marked arrow/dash. The heavy stroke on the middle P may be retracing rather than cancellation; no confident deletion inferred. No typed additions.

### Changes (before → after)

```diff
--- before
+++ after
@@ -16,7 +16,7 @@
 \item Le nb de composantes \deleted{\illegible{1}} irréd. absolues des fibres de $X$ sur $Y$ est loc. constant sur $Y$
 \end{enumerate}
 % slanted
-\margin{si on abandonne cette hypothèse, on trouve des \unsure{phénomènes} à la Néron ?!}
+\margin{si on abandonne cette hypothèse, on \unsure{trouve des|tombe aux} \unsure{phénomènes} à la Néron ?!}
 % L10.
 Alors le \unsure{$S$|$f$}-schéma $\unsure{\mathscr P_{X/Y}|\mathcal P_{X/Y}}$ relatif existe, et est \uline{simple} sur $Y$.
 % L11--17.
```

### Formula and diagram register checked against the crops

1. Source line 9:

```latex
$X$
```

2. Source line 9:

```latex
$Y$
```

3. Source line 12:

```latex
$Y$
```

4. Source line 13:

```latex
$X$
```

5. Source line 13:

```latex
$Y$
```

6. Source line 14:

```latex
$X$
```

7. Source line 14:

```latex
$Y$
```

8. Source line 15:

```latex
$X$
```

9. Source line 15:

```latex
$S$
```

10. Source line 16:

```latex
$X$
```

11. Source line 16:

```latex
$Y$
```

12. Source line 16:

```latex
$Y$
```

13. Source line 21:

```latex
$S$
```

14. Source line 21:

```latex
$f$
```

15. Source line 21:

```latex
$\unsure{\mathscr P_{X/Y}|\mathcal P_{X/Y}}$
```

16. Source line 21:

```latex
$Y$
```

17. Source line 23:

```latex
$n$
```

18. Source line 23:

```latex
$Y$
```

19. Source line 23:

```latex
$Y'$
```

20. Source line 23:

```latex
$n$
```

21. Source line 23:

```latex
$Y$
```

22. Source line 23:

```latex
$\mathbb Z_{Y'/Y}$
```

23. Source line 23:

```latex
$\prod_{Y'/Y}(\mathbb Z_{Y'})=\underline{\operatorname{Hom}}_Y(Y',\mathbb Z_Y)$
```

24. Source line 23:

```latex
$Y$
```

25. Source line 23:

```latex
$Y'$
```

26. Source line 23:

```latex
$Y'$
```

27. Source line 23:

```latex
$\mathbb Z^n$
```

28. Source line 25:

```latex
\[
\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}\quad\deleted{\unsure{\infty}}
\]
```

29. Source line 28:

```latex
$\mathscr P_{X/Y}^c$
```

30. Source line 29:

```latex
\[
0\longrightarrow\mathscr P_{X/Y}^c\longrightarrow\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}\longrightarrow0
\]
```

31. Source line 34:

```latex
\[
\mathbb Z_{Y'/Y}\longrightarrow\mathbb Z_Y
\]
```

32. Source line 38:

```latex
\[
\mathscr P_{X/Y}\longrightarrow\mathbb Z_Y
\]
```


## Scan 26

Start: 2026-11-17T23:45:53+00:00; crop notes saved before opening the page: 2026-11-17T23:46:46+00:00; end: 2026-11-17T23:47:13+00:00.

### Words and accents read independently from the crops

Les fibres de P^0_X/S sont connexes, et propres si celles de X sont simples; Soit [struck schéma] X−S l’ens./ouv. des pts de X qui sont non simples sur Y (non is visually possible despite the context). On va définir un morphisme; exposant 1; composante d’augmentation 1; Je reviens / Il revient à en donner fonctoriellement; inserted pour le changement de base, une application; struck application. Γ/script T(X−S/Y) → P^1(X/S). Or on note qu’une section de X−S sur Y définit un diviseur sur X−S (transverse à X/Y), d’où un fibré inversible dont on constate que le [struck word] degré est +1; [car on peut supposer Y/S=Spec k, le degré ...]. Margin vérifier/référence ?? . II Partons d’un X propre et simple sur Y/S, dont les fibres sont de dim 1; struck Soit X_i; (et abs! connexes) (donc abs! irréductibles). Soit S un sous-schéma fermé; crossed X plat sur Y et; ne contenant aucune fibre de X/Y; donc fini sur Y, et plat sur Y. Soit glyph with three horizontal strokes (Ξ, script I, calligraphic I) le faisceau d’idéaux définissant Y. Alors on prouve facilement ... localement libre. Bracket c’est purement local; un faisceau coh sur X plat rel. à Y et qui ... fibres ... plat sur X. Slanted margin: fibres abs! connexes est une condition peut-être vide. Accents définir, morphisme, où, fonctoriellement, définit, à, fibré, degré, fermé, idéaux and localement checked; heavily compressed clause remains doubtful.

### Visual checks

Both displays and every inline formula reread: P has a looping script cross-stroke, c from the preceding page is not silently substituted for the visible 0 here; superscript 1 occurs in both maps and augmentation discussion. P_{X/S} and P(X/S) are distinct written forms; the section-expression base is Y. Γ has a firm right-angle top, but script T remains a candidate. The ideal glyph has three horizontal strokes, a curved right join, and no secure upright I stem: Xi now comes first, with both I alphabets retained. Underlined localement libre is not a cancellation. In the deleted Soit X_i, i is short and does not have a j-descender; no other indexed i/j. Reread both oblique notes in their direction, including abs!, peut-être and vide; the first note now favours vérifier by its v-like initial stroke, with référence retained. All crossings checked: schéma, repeated application, diviseur, Soit X_i, and X plat sur Y et. Insertions pour le changement de base, degré, fermé and the bottom est follow their pointers. No handwriting on type. The surprising non and définissant Y remain as written/marked; the compressed final local-criterion clause is not mathematically repaired. Rechecked accents and punctuation against the prereading list; no further confident resolution.

### Changes (before → after)

```diff
--- before
+++ after
@@ -15,9 +15,9 @@
 % L9--13
 or on note qu’une section de $X-S$ sur $Y$ \uline{définit un diviseur sur} $X-S$ \unsure{(transverse à $X/Y$)} d’où un fibré inversible, dont on constate que le \deleted{\unsure{diviseur}} \inserted{degré} est $+1$ [car on peut supposer $\unsure{Y|S}=\operatorname{Spec}k$, \unsure{le degré clair}].
 % margin note written slanted, rising toward the text
-\margin{\unsure{référence|vérifier}??}
+\margin{\unsure{vérifier|référence}??}
 
 % L14--23
-II) Partons d’un $X$ \uline{propre} et \uline{simple} sur $\unsure{Y|S}$, dont les fibres sont de dim $1$, \deleted{\unsure{Soit} $X_i$} \unsure{(et abs! connexes)} (donc abs! irréductibles). Soit $S$ un sous-schéma \inserted{fermé} de \deleted{$X$ plat sur $Y$ et} ne contenant aucune fibre de $X/\unsure{Y|S}$, donc \uline{fini} sur $\unsure{Y|S}$, et plat sur $Y$. Soit $\unsure{\mathcal I|\mathscr I|\Xi}$ le faisceau d’idéaux définissant $Y$. Alors on prouve facilement que $\mathcal I$ est \uline{localement libre} [c’est purement local : un faisceau coh. sur $X$ plat rel. à $Y$ et qui \unsure{est inversible|est un module} dans fibres \inserted{\unsure{est}} est plat sur $X$.---]
+II) Partons d’un $X$ \uline{propre} et \uline{simple} sur $\unsure{Y|S}$, dont les fibres sont de dim $1$, \deleted{\unsure{Soit} $X_i$} \unsure{(et abs! connexes)} (donc abs! irréductibles). Soit $S$ un sous-schéma \inserted{fermé} de \deleted{$X$ plat sur $Y$ et} ne contenant aucune fibre de $X/\unsure{Y|S}$, donc \uline{fini} sur $\unsure{Y|S}$, et plat sur $Y$. Soit $\unsure{\Xi|\mathscr I|\mathcal I}$ le faisceau d’idéaux définissant $Y$. Alors on prouve facilement que $\Xi$ est \uline{localement libre} [c’est purement local : un faisceau coh. sur $X$ plat rel. à $Y$ et qui \unsure{est inversible|est un module} dans fibres \inserted{\unsure{est}} est plat sur $X$.---]
 % margin note written slanted, read after rotating clockwise
 \margin{\unsure{fibres abs! connexes est une condition} \unsure{peut-être} \uline{\unsure{vide}}.}
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
$\unsure{\mathscr P|\mathcal P}^0_{X/S}$
```

2. Source line 4:

```latex
$X$
```

3. Source line 4:

```latex
$X-S$
```

4. Source line 4:

```latex
$X$
```

5. Source line 4:

```latex
$Y$
```

6. Source line 6:

```latex
\[
\boxed{X-S\longrightarrow\mathscr P^1_{X/S}}.
\]
```

7. Source line 10:

```latex
$1$
```

8. Source line 10:

```latex
$1$
```

9. Source line 12:

```latex
\[
\unsure{\Gamma|\mathscr T}(X-S/Y)\longrightarrow\mathscr P^1(X/S)
\]
```

10. Source line 16:

```latex
$X-S$
```

11. Source line 16:

```latex
$Y$
```

12. Source line 16:

```latex
$X-S$
```

13. Source line 16:

```latex
$X/Y$
```

14. Source line 16:

```latex
$+1$
```

15. Source line 16:

```latex
$\unsure{Y|S}=\operatorname{Spec}k$
```

16. Source line 21:

```latex
$X$
```

17. Source line 21:

```latex
$\unsure{Y|S}$
```

18. Source line 21:

```latex
$1$
```

19. Source line 21:

```latex
$X_i$
```

20. Source line 21:

```latex
$S$
```

21. Source line 21:

```latex
$X$
```

22. Source line 21:

```latex
$Y$
```

23. Source line 21:

```latex
$X/\unsure{Y|S}$
```

24. Source line 21:

```latex
$\unsure{Y|S}$
```

25. Source line 21:

```latex
$Y$
```

26. Source line 21:

```latex
$\unsure{\Xi|\mathscr I|\mathcal I}$
```

27. Source line 21:

```latex
$Y$
```

28. Source line 21:

```latex
$\Xi$
```

29. Source line 21:

```latex
$X$
```

30. Source line 21:

```latex
$Y$
```

31. Source line 21:

```latex
$X$
```


## Scan 27

Start: 2026-11-17T23:47:13+00:00; crop notes saved before opening the page: 2026-11-17T23:47:46+00:00; end: 2026-11-17T23:48:38+00:00.

### Words and accents read independently from the crops

donc, struck il s’ensuit / repeated il s’ensuit and fac., facile, que les ideal-glyph powers sont tels que O_X/ideal-power sont encore plats sur Y. Soit [cancelled symbol] S_n le sous-schéma de X défini par ideal-power, et soit X_n=X amalg_{S_n} Y le Y-schéma obtenu en «contractant S_n en S» (double quote strokes). Crossed Soit / de sorte X_ξ=X−S. Donc X_0=X, et les X_i forment un système [projectif struck, inductif inserted]. Live square: S_n→X, f_i_n?/f i_n down to Y, p_n down to X_n, ε_n right; cancelled preceding square. Left sequence …X_2←X_1←X_0=X. Donc les P_X_n/S forment un système [inductif struck] projectif, d’où un pro-(S-préschéma en groupes), noté P_S,X/Y; partie fermée S de X/Y; au moins, si Y est noethérien; résultera d’ailleurs de la construction qu’on en donnera plus bas. Les morphismes canoniques X−S→P^1_X_n/Y définissent à la limite un morphisme, boxed φ_S: X−S→P^1_S,X/Y relation subset/element P_S,X/Y. Accents défini, schéma, système, où, préschéma, noté, fermée, noethérien, résultera, définissent, à checked; no confident correction of the quoted S.

### Visual checks

All three ideal powers compared in the enlarged top crop: each has a short horizontal elevated stroke before a filled n-like ending; the possible minus was missing and is restored with -n/n/-m/m alternatives at first occurrence. Xi/script I/calligraphic I ordering reconciled with 26 from its strokes, not the ideal-sheaf context. O is underlined with plain/calligraphic alternatives. The amalgamation, n subscripts, X_0=X, X_i, Picard subscripts X_n/S and X_n/Y, and final S,X/Y all checked separately. i in X_i and i_n has no descender; f i_n has a visible intervening space rather than a safely distinct composition circle; ε_n is small rounded epsilon, no forced membership reading. The old square is crossed out; its objects remain deleted and its diagonal cancellation stroke is retained without the spurious slash-label used in the first draft. The replacement square has arrows right/down/right/down with labels i_n, f i_n, p_n, ε_n. Rechecked the leftward sequence and final boxed map, including subset/in ambiguity and phi alphabet. Corrections projectif→inductif and inductif deletion in the Picard paragraph retained; no omitted marginal prose. The quoted S in contracting S_n en S remains unchanged. In the bottom prose compressed future/present endings are now explicit alternatives résultera/résulte and donnera/donne. All accents from crop notes checked. No typed additions.

### Changes (before → after)

```diff
--- before
+++ after
@@ -1,22 +1,22 @@
 \scanpage{27}
 % archive sheet number: 26
 % L1--4
-donc \deleted{\unsure{il s’ensuit}} \inserted{\unsure{il s’ensuit}} \deleted{\unsure{fac.}} \unsure{facile} que les $\unsure{\mathcal I|\mathscr I|\Xi}^{\unsure{n|m}}$ sont tels que $\unsure{\underline{\mathcal O}|\underline O}_X/\mathcal I^n$ sont encore plats sur $Y$. Soit $\deleted{\unsure{Y}}S_n$ le sous-schéma de $X$ défini par $\mathcal I^n$, et soit $X_n=X\amalg_{S_n}Y$ le $\deleted{S}Y$-schéma obtenu en ``\unsure{contractant} $S_n$ en $S$''.
+donc \deleted{\unsure{il s’ensuit}} \inserted{\unsure{il s’ensuit}} \deleted{\unsure{fac.}} \unsure{facile|facilement} que les $\unsure{\Xi|\mathscr I|\mathcal I}^{\unsure{-n|n|-m|m}}$ sont tels que $\unsure{\underline{\mathcal O}|\underline O}_X/\Xi^{-n}$ sont encore plats sur $Y$. Soit $\deleted{\unsure{Y}}S_n$ le sous-schéma de $X$ défini par $\Xi^{-n}$, et soit $X_n=X\amalg_{S_n}Y$ le $\deleted{S}Y$-schéma obtenu en ``\unsure{contractant} $S_n$ en $S$''.
 % L5--6
 \deleted{\unsure{Soit}} \deleted{\unsure{de sorte} $X_{\unsure{S|\xi}}=X-S$.} Donc $X_0=X$, et les $X_i$ forment un \uline{système} \uline{\deleted{projectif}\inserted{inductif}}.
 % left, cancelled square and replacement square
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
-\deleted{\unsure{S}_n}\arrow[r,no head]\arrow[d]\arrow[dr,no head,"\deleted{\unsure{/}}" description] \& \deleted X\arrow[d] \& S_n\arrow[r,"i_n"]\arrow[d,"f i_n"'] \& X\arrow[d,"p_n"]\\
+\deleted{\unsure{S}_n}\arrow[r,no head]\arrow[d]\arrow[dr,no head] \& \deleted X\arrow[d] \& S_n\arrow[r,"i_n"]\arrow[d,"f i_n"'] \& X\arrow[d,"p_n"]\\
 \deleted Y\arrow[r,no head] \& \deleted{X_n} \& Y\arrow[r,"\varepsilon_n"'] \& X_n
 \end{tikzcd}}
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
 \cdots\& X_2\arrow[l,no head]\&X_1\arrow[l]\&X_0=X\arrow[l]
 \end{tikzcd}}
 % L7--14
-Donc les $\unsure{\mathscr P|\mathcal P}_{X_n/S}$ forment un système \deleted{\uline{inductif}} projectif, d’où un pro-($S$-préschéma en groupes) noté $\mathscr P_{S,X/Y}$, et qui ne dépend que de la \uline{partie fermée} $S$ de $X/Y$, comme on constate facilement (du moins, si $Y$ est noethérien) --- cel\unsure{a} résulte d’ailleurs \unsure{de} la ``construction'' qu’on en donne plus bas.
+Donc les $\unsure{\mathscr P|\mathcal P}_{X_n/S}$ forment un système \deleted{\uline{inductif}} projectif, d’où un pro-($S$-préschéma en groupes) noté $\mathscr P_{S,X/Y}$, et qui ne dépend que de la \uline{partie fermée} $S$ de $X/Y$, comme on constate facilement (du moins, si $Y$ est noethérien) --- cel\unsure{a} \unsure{résultera|résulte} d’ailleurs \unsure{de} la ``construction'' qu’on en \unsure{donnera|donne} plus bas.
 
 % L15--17
 Les morphismes canoniques $X-S\longrightarrow\mathscr P^1_{X_n/Y}$ définissent à la limite un morphisme
 \[
-\boxed{\unsure{\varphi|\phi}_S:X-S\longrightarrow\mathscr P^1_{S,X/Y}\subset\mathscr P_{S,X/Y}}.
+\boxed{\unsure{\varphi|\phi}_S:X-S\longrightarrow\mathscr P^1_{S,X/Y}\unsure{\subset|\in}\mathscr P_{S,X/Y}}.
 \]
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
$\unsure{\Xi|\mathscr I|\mathcal I}^{\unsure{-n|n|-m|m}}$
```

2. Source line 4:

```latex
$\unsure{\underline{\mathcal O}|\underline O}_X/\Xi^{-n}$
```

3. Source line 4:

```latex
$Y$
```

4. Source line 4:

```latex
$\deleted{\unsure{Y}}S_n$
```

5. Source line 4:

```latex
$X$
```

6. Source line 4:

```latex
$\Xi^{-n}$
```

7. Source line 4:

```latex
$X_n=X\amalg_{S_n}Y$
```

8. Source line 4:

```latex
$\deleted{S}Y$
```

9. Source line 4:

```latex
$S_n$
```

10. Source line 4:

```latex
$S$
```

11. Source line 6:

```latex
$X_{\unsure{S|\xi}}=X-S$
```

12. Source line 6:

```latex
$X_0=X$
```

13. Source line 6:

```latex
$X_i$
```

14. Source line 8:

```latex
\begin{tikzcd}[ampersand replacement=\&]
\deleted{\unsure{S}_n}\arrow[r,no head]\arrow[d]\arrow[dr,no head] \& \deleted X\arrow[d] \& S_n\arrow[r,"i_n"]\arrow[d,"f i_n"'] \& X\arrow[d,"p_n"]\\
\deleted Y\arrow[r,no head] \& \deleted{X_n} \& Y\arrow[r,"\varepsilon_n"'] \& X_n
\end{tikzcd}
```

15. Source line 12:

```latex
\begin{tikzcd}[ampersand replacement=\&]
\cdots\& X_2\arrow[l,no head]\&X_1\arrow[l]\&X_0=X\arrow[l]
\end{tikzcd}
```

16. Source line 16:

```latex
$\unsure{\mathscr P|\mathcal P}_{X_n/S}$
```

17. Source line 16:

```latex
$S$
```

18. Source line 16:

```latex
$\mathscr P_{S,X/Y}$
```

19. Source line 16:

```latex
$S$
```

20. Source line 16:

```latex
$X/Y$
```

21. Source line 16:

```latex
$Y$
```

22. Source line 19:

```latex
$X-S\longrightarrow\mathscr P^1_{X_n/Y}$
```

23. Source line 20:

```latex
\[
\boxed{\unsure{\varphi|\phi}_S:X-S\longrightarrow\mathscr P^1_{S,X/Y}\unsure{\subset|\in}\mathscr P_{S,X/Y}}.
\]
```


## Scan 28

Start: 2026-11-17T23:48:38+00:00; crop notes saved before opening the page: 2026-11-17T23:49:09+00:00; end: 2026-11-17T23:49:52+00:00.

### Words and accents read independently from the crops

Théorème. Soit G un Y-schéma en groupes [commu inserted] de type fini [sur Y struck], et P^1 un fibré principal homogène sous G [devenant trivial par extension fid. plate quasi-compacte], d’où un schéma en groupes Z-augmenté P, avec P^(1)=P^1, P^(0)=G. Considérons l’application canonique u↦u∘φ_S. Hom subscripts Y-schémas en groupes Z-augmentés, script P_S,X/Y to plain P; target Hom_Y(X−S,P^1). Cette application est bijective (underlined). (Th. de Rosenlicht). Corollaire 1: Hom groups to Hom_Y(X−S,G), isomorphism tilde above arrow. Corollaire 2: Considérons inserted; Le [homomorphisme de struck] foncteur φ_S*, de la catégorie des schémas extensions [en groupes commutatifs inserted] de plain P_S,X/Y par des Y-schémas en groupes commutatifs de type fini G sur Y, dans la catégorie [qui struck]. Margin: il faut faire attention aux définitions de “fibré” et “extension” ? G plat sur Y/S ??; double quote strokes checked. Accents Théorème (both accents), schéma, fibré, homogène, où, augmenté, Considérons, catégorie, définitions and à/aux checked; commu abbreviation not expanded.

### Visual checks

Reread theorem and both corollaries in full. All P superscripts (1), 1, (0), and both Hom domains/codomains checked. The first and second Picard capitals have the script loop; the corollary-2 P lacks that loop and remains plain, with no unification by context. Integer Z has a doubled diagonal. The inline map from u has no reliably separable mapsto tail: long arrow/mapsto alternatives added, while direction is clearly rightward. The corollary-1 arrow carries a tilde; the star on phi_S in corollary 2 is multipronged, not a dot. No indexed i/j. Insertions commu., Considérons, foncteur and (en groupes commutatifs) traced to their positions; cancelled sur Y/S, homomorphisme de and qui retained. The marginal note was read again in the rotated crop: attention aux définitions remains tentative, double quote pairs and final question marks preserved. The long strokes beside the statement and lower paragraph are emphasis rules, not strike-throughs; now rendered as vertical rules instead of merely commented. Accents and word endings match prereading list; no typed corrections.

### Changes (before → after)

```diff
--- before
+++ after
@@ -1,7 +1,9 @@
 \scanpage{28}
 % archive sheet number: 27
 % L1--7; vertical emphasis stroke beside the statement
-\uline{Théorème} Soit $G$ un $Y$-schéma en groupes \inserted{\unsure{commu.}} de type fini \deleted{sur $\unsure{Y|S}$}, et $P^1$ un fibré principal homogène sous $G$ [devenant trivial par extension fid. plate quasi-compacte\unsure{---}], d’où un schéma en groupes $\mathbb Z$-augmenté $P$, avec $P^{(1)}=P^1$, $P^{(0)}=G$. Considérons l’application canonique $u\mapsto u\circ\unsure{\varphi|\phi}_S$
+\noindent\vrule\hspace{.6em}\begin{minipage}{.93\linewidth}
+\uline{Théorème} Soit $G$ un $Y$-schéma en groupes \inserted{\unsure{commu.}} de type fini \deleted{sur $\unsure{Y|S}$}, et $P^1$ un fibré principal homogène sous $G$ [devenant trivial par extension fid. plate quasi-compacte\unsure{---}], d’où un schéma en groupes $\mathbb Z$-augmenté $P$, avec $P^{(1)}=P^1$, $P^{(0)}=G$. Considérons l’application canonique $u\unsure{\longrightarrow|\mapsto}u\circ\unsure{\varphi|\phi}_S$
+\end{minipage}\par
 \[
 \operatorname{Hom}_{\substack{Y\text{-schémas en groupes}\\\mathbb Z\text{-augmentés}}}
 (\unsure{\mathscr P|\mathcal P}_{S,X/Y},P)\longrightarrow\operatorname{Hom}_Y(X-S,P^1)
@@ -17,6 +19,9 @@
 \operatorname{Hom}_{Y\text{-schémas en groupes}}(\mathscr P_{S,X/Y},G)\xrightarrow{\sim}\operatorname{Hom}_Y(X-S,G)
 \]
 % L11--15; vertical emphasis stroke beside lower paragraph
-\uline{Corollaire 2} \inserted{Considérons} Le \deleted{\unsure{homomorphisme de}} \inserted{foncteur} $\varphi_S^*$, de la catégorie des schémas \uline{extensions} \inserted{(en groupes commutatifs)} de $P_{S,X/Y}$ par des $Y$-schémas en groupes commutatifs de type fini $G$ sur $Y$, dans la catégorie \deleted{\unsure{qui}}
+\uline{Corollaire 2}
+\noindent\vrule\hspace{.6em}\begin{minipage}{.93\linewidth}
+\inserted{Considérons} Le \deleted{\unsure{homomorphisme de}} \inserted{foncteur} $\varphi_S^*$, de la catégorie des schémas \uline{extensions} \inserted{(en groupes commutatifs)} de $P_{S,X/Y}$ par des $Y$-schémas en groupes commutatifs de type fini $G$ sur $Y$, dans la catégorie \deleted{\unsure{qui}}
+\end{minipage}\par
 % margin note written slanted, read after rotating clockwise
 \margin{il faut faire \unsure{attention aux définitions} de ``fibré'' et ``extension'' ? $G$ plat sur $\unsure{Y|S}$??}
```

### Formula and diagram register checked against the crops

1. Source line 5:

```latex
$G$
```

2. Source line 5:

```latex
$Y$
```

3. Source line 5:

```latex
$\unsure{Y|S}$
```

4. Source line 5:

```latex
$P^1$
```

5. Source line 5:

```latex
$G$
```

6. Source line 5:

```latex
$\mathbb Z$
```

7. Source line 5:

```latex
$P$
```

8. Source line 5:

```latex
$P^{(1)}=P^1$
```

9. Source line 5:

```latex
$P^{(0)}=G$
```

10. Source line 5:

```latex
$u\unsure{\longrightarrow|\mapsto}u\circ\unsure{\varphi|\phi}_S$
```

11. Source line 7:

```latex
\[
\operatorname{Hom}_{\substack{Y\text{-schémas en groupes}\\\mathbb Z\text{-augmentés}}}
(\unsure{\mathscr P|\mathcal P}_{S,X/Y},P)\longrightarrow\operatorname{Hom}_Y(X-S,P^1)
\]
```

12. Source line 18:

```latex
\[
\operatorname{Hom}_{Y\text{-schémas en groupes}}(\mathscr P_{S,X/Y},G)\xrightarrow{\sim}\operatorname{Hom}_Y(X-S,G)
\]
```

13. Source line 24:

```latex
$\varphi_S^*$
```

14. Source line 24:

```latex
$P_{S,X/Y}$
```

15. Source line 24:

```latex
$Y$
```

16. Source line 24:

```latex
$G$
```

17. Source line 24:

```latex
$Y$
```

18. Source line 27:

```latex
$G$
```

19. Source line 27:

```latex
$\unsure{Y|S}$
```


## Scan 29

Start: 2026-11-17T23:49:52+00:00; crop notes saved before opening the page: 2026-11-17T23:50:31+00:00; end: 2026-11-17T23:51:07+00:00.

### Words and accents read independently from the crops

des fibrés principaux homogènes sur X−S de groupes de tels G. Ce foncteur est pleinement fidèle. Soient Q,Q′ deux telles extensions, de groupes G,G′. Un hom de Q′ en Q′/Q (overwritten prime) est [inserted un couple formé d’un hom u:G′→G et d’] une [crossed isom de Q″=Q×_{G′}G avec; several overwritten words and Hom_{S,u}(G′,Q) or Q′,Q; qui est un fibré crossed]; right insertion isom de Q″=Q′×_{G′}G; Q′ [small crossed word] (on ... par extension de groupe ... G′/G); Il y en a ... ssi Q′ et Q″ sont isomorphes. Diagram X−S→script P_S,X/S, dashed arrow up to Q, slanted plain segment Q to P, isolated Q″. Ext terminal exponent 1 uncertain as in 21/23, target Ext crossed under H^1. étant un hom de groupes, pour prouver qu’il est injectif (i.e. Q et Q′ isom ssi φ*(Q) et φ*(Q″) le sont) on est ramené à prouver que le noyau est nul, donc que si φ*(Q) est trivial, alors Q l’est. Cela résulte [facilement struck] aussitôt du th. de Rosenlicht. Comme [φ* est fidèle car inserted] (le groupe étant donné), [est struck] on ... . Margins: il faut pouvoir définir les fibrés associés, Attention!; Attention, il faut bien préciser les définitions d’addition / opérations d’addition des fibrés etc. Accents fibrés, homogènes, fidèle, formé, défin ir, associés, préciser, définitions, étant, ramené, à, résulte, aussitôt, donné checked; cancellation region remains low confidence.

### Visual checks

Entire cancellation block reread enlarged, including both versions of Q-double-prime product; the large central isom/equation is crossed, not live. The right insertion carries a high stroke after Q, so the prime-bearing product is preferred there only; older crossed product stays unprimed. The overwritten target Q after Un hom and parenthetical Q′/Q″ retain local differences, with no repair to make the argument consistent. Every star and prime checked individually; there is no i/j index. Ext/Ext^1 ambiguity added because of its connected terminal stroke; target H^1 is written over Ext-like letters, which remain deleted. The Picard subscript in the diagram is X/S, not X/Y; the display subscript remains doubtful. Diagram contains the isolated Q″, dashed rising arrow, solid right arrow and unheaded descending segment. Both oblique margin notes reread from rotated crops, retaining compressed pouvoir and opérations d’addition as unsure. facilement is struck and aussitôt inserted; final est is struck and on/en now marked. The bracket/caret after Comme places phi-star est fidèle car before the parenthesis. Initial vertical rule added as a rendered rule. No typed material. All prose accents/endings and every listed formula compared; the dense crossed block is still the least certain area.

### Changes (before → after)

```diff
--- before
+++ after
@@ -1,7 +1,9 @@
 \scanpage{29}
 % archive sheet number: 28
 % L1--3, continuation of Corollaire 2
- des fibrés principaux homogènes sur $X-S$ de groupes de tels $G$. Ce foncteur est pleinement fidèle.
+\noindent\vrule\hspace{.6em}\begin{minipage}{.93\linewidth}
+des fibrés principaux homogènes sur $X-S$ de groupes de tels $G$. Ce foncteur est pleinement fidèle.
+\end{minipage}\par
 
 % L4--9
 Soient $Q,Q'$ deux telles extensions, de groupes $G,G'$. Un hom. de $Q'$ en $\unsure{Q'|Q}$ est \inserted{un couple formé d’un hom. $u:G'\longrightarrow G$ et d’} un\unsure{e} \deleted{isom. de $Q''=Q\times_{G'}G$ avec} \deleted{\unsure{élément de} $\operatorname{Hom}_{\unsure{S,u}}(\unsure{Q'|G'},Q)$, \unsure{avec}} \deleted{qui est un fibré} \inserted{\unsure{isom. de} $Q''=\unsure{Q\times_{G'}G|Q'\times_{G'}G}$} $Q'$ \deleted{\unsure{ou}} (on \unsure{entend} par extension de groupe \uline{donné} $G'$). Il y en a \unsure{ssi} $\unsure{Q'|Q}$ et $Q''$ sont isomorphes. Or
@@ -14,11 +16,11 @@
 \end{tikzcd}}
 % L10 displayed, overwritten letters retained
 \[
-\operatorname{Ext}^1(\unsure{\mathscr P|\mathcal P}_{\unsure{S}},G)\longrightarrow\deleted{\unsure{\operatorname{Ext}}}\unsure{H|\mathrm H}^1(X-S,G)
+\unsure{\operatorname{Ext}|\operatorname{Ext}^1}(\unsure{\mathscr P|\mathcal P}_{\unsure{S}},G)\longrightarrow\deleted{\unsure{\operatorname{Ext}}}\unsure{H|\mathrm H}^1(X-S,G)
 \]
 % L11--17
 étant un hom. de groupes, pour prouver qu’il est injectif (i.e. $Q$ et $Q'$ isom. ssi $\unsure{\varphi|\phi}^*(Q)$ et $\varphi^*(Q'')$ le sont) on est ramené à prouver que le noyau est nul, i.e. que si $\varphi^*(Q)$ est trivial, alors $Q$ l’est. Cela résulte \deleted{facilement} \inserted{\unsure{aussitôt}} du th. de Rosenlicht.
 % margin note written slanted, read in its own direction
 \margin{Attention, il faut bien préciser les définitions \unsure{d’opérations d’addition} de fibrés etc}
 % L18, unfinished sentence at foot
-Comme \inserted{$\varphi^*$ est fidèle car} (\unsure{le groupe étant donné}), \deleted{\unsure{est}} en
+Comme \inserted{$\varphi^*$ est fidèle car} (\unsure{le groupe étant donné}), \deleted{\unsure{est}} \unsure{on|en}
```

### Formula and diagram register checked against the crops

1. Source line 5:

```latex
$X-S$
```

2. Source line 5:

```latex
$G$
```

3. Source line 9:

```latex
$Q,Q'$
```

4. Source line 9:

```latex
$G,G'$
```

5. Source line 9:

```latex
$Q'$
```

6. Source line 9:

```latex
$\unsure{Q'|Q}$
```

7. Source line 9:

```latex
$u:G'\longrightarrow G$
```

8. Source line 9:

```latex
$Q''=Q\times_{G'}G$
```

9. Source line 9:

```latex
$\operatorname{Hom}_{\unsure{S,u}}(\unsure{Q'|G'},Q)$
```

10. Source line 9:

```latex
$Q''=\unsure{Q\times_{G'}G|Q'\times_{G'}G}$
```

11. Source line 9:

```latex
$Q'$
```

12. Source line 9:

```latex
$G'$
```

13. Source line 9:

```latex
$\unsure{Q'|Q}$
```

14. Source line 9:

```latex
$Q''$
```

15. Source line 13:

```latex
\begin{tikzcd}[ampersand replacement=\&]
\&Q\arrow[d,no head]\&Q''\\
X-S\arrow[ur,dashed]\arrow[r]\&\unsure{\mathscr P|\mathcal P}_{S,X/S}
\end{tikzcd}
```

16. Source line 18:

```latex
\[
\unsure{\operatorname{Ext}|\operatorname{Ext}^1}(\unsure{\mathscr P|\mathcal P}_{\unsure{S}},G)\longrightarrow\deleted{\unsure{\operatorname{Ext}}}\unsure{H|\mathrm H}^1(X-S,G)
\]
```

17. Source line 22:

```latex
$Q$
```

18. Source line 22:

```latex
$Q'$
```

19. Source line 22:

```latex
$\unsure{\varphi|\phi}^*(Q)$
```

20. Source line 22:

```latex
$\varphi^*(Q'')$
```

21. Source line 22:

```latex
$\varphi^*(Q)$
```

22. Source line 22:

```latex
$Q$
```

23. Source line 26:

```latex
$\varphi^*$
```


## Scan 30

Start: 2026-11-17T23:51:07+00:00; crop notes saved before opening the page: 2026-11-17T23:51:36+00:00; end: 2026-11-17T23:51:58+00:00.

### Words and accents read independently from the crops

est ainsi ramené à prouver que Hom(Q,Q)→Hom(φ*(Q),φ*(Q)) est bijectif. Or les deux s’identifient resp. à Hom_{grps sur Y/S}(P_S,G) et [crossed E/H] Hom_Y(X−S,G), donc sont isomorphes. En particulier Corollaire 3 Si G est un schéma en groupes commu. de type fini sur Y, on a un hom canonique injectif (double underline). Ext_{schémas en groupes sur Y/S}(P_S,X/S,G)→H^1(X−S,G); Ext has a connected final stroke, no separate elevated 1 visible here. Margin préciser la signification ... . Il semble que c’est bijectif/surjectif (overwritten beginning) chaque fois que S→Y est surjectif, i.e. que les fibres de X/Y sont non propres, donc affines. Dans le cas où S=empty, G=G_m, on ne sera/serait déjà pas surjectif. Accents ramené, à, s’identifient, schéma, déjà, où checked; resp. and commu. abbreviations preserved. No Q primes seen, both arguments resemble plain Q.

### Visual checks

All three displays and inline formulas reread: both Hom arguments Q are unprimed; both phi-star factors have stars, not exclamation marks; the script Picard P has subscript S in the upper Hom but S,X/S in the lower Ext. Base Y/S under the two group categories remains overwritten and unsure. Ext here has no distinct separate exponent; H has a clear elevated 1. No i/j indices; m in G_m is a small multi-hump stroke, and the empty-set sign is a slashed circle. The crossed E/H before Hom is deleted; no extra live cohomology operator supplied. The marginal préciser la signification was read in its slanted direction and remains marked. The canonical injectif has two underlines and the conjectural bijectif/surjectif remains overwritten and unsure. A tall punctuation stroke after resp is not securely distinguishable from an abbreviation point, so resp!/resp. is now marked. The corollary-side vertical rule is rendered. The surprising X/Y in the non-proper-fibres clause is retained, not changed to X−S. Checked accents and the sera/serait ending again. No typed corrections.

### Changes (before → after)

```diff
--- before
+++ after
@@ -5,7 +5,7 @@
 \[
 \operatorname{Hom}(Q,Q)\longrightarrow\operatorname{Hom}(\unsure{\varphi|\phi}^*(Q),\varphi^*(Q))
 \]
-est bijectif. Or les deux s’identifient resp! à
+est bijectif. Or les deux s’identifient \unsure{resp!|resp.} à
 % L4--5
 \[
 \operatorname{Hom}_{\substack{\text{grps}\\\text{sur }\unsure{Y|S}}}(\unsure{\mathscr P|\mathcal P}_S,G)
@@ -17,7 +17,9 @@
 % L6--9
 En particulier
 
+\noindent\vrule\hspace{.6em}\begin{minipage}{.93\linewidth}
 \uline{Corollaire 3} Si $G$ est un schéma en groupes commu. de type fini sur $Y$, on a un hom. canonique \uuline{injectif}
+\end{minipage}\par
 \[
 \operatorname{Ext}_{\substack{\text{schémas en groupes}\\\text{sur }\unsure{Y|S}}}(\mathscr P_{S,X/S},G)\longrightarrow H^1(X-S,G)
 \]
```

### Formula and diagram register checked against the crops

1. Source line 5:

```latex
\[
\operatorname{Hom}(Q,Q)\longrightarrow\operatorname{Hom}(\unsure{\varphi|\phi}^*(Q),\varphi^*(Q))
\]
```

2. Source line 10:

```latex
\[
\operatorname{Hom}_{\substack{\text{grps}\\\text{sur }\unsure{Y|S}}}(\unsure{\mathscr P|\mathcal P}_S,G)
\quad\text{et}\quad
\deleted{\unsure{E|H}}\operatorname{Hom}_Y(X-S,G)
\]
```

3. Source line 21:

```latex
$G$
```

4. Source line 21:

```latex
$Y$
```

5. Source line 23:

```latex
\[
\operatorname{Ext}_{\substack{\text{schémas en groupes}\\\text{sur }\unsure{Y|S}}}(\mathscr P_{S,X/S},G)\longrightarrow H^1(X-S,G)
\]
```

6. Source line 29:

```latex
$S\longrightarrow Y$
```

7. Source line 29:

```latex
$X/Y$
```

8. Source line 29:

```latex
$S=\varnothing$
```

9. Source line 29:

```latex
$G=G_m$
```


## Scan 31

Start: 2026-11-17T23:51:58+00:00; crop notes saved before opening the page: 2026-11-17T23:52:35+00:00; end: 2026-11-17T23:53:24+00:00.

### Words and accents read independently from the crops

Il semble néanmoins que dans le cas général, pour prouver qu’un fibré principal E sur X−S provient d’une [fibré principal struck] extension de P_S par G, il suffit (utilisant le théorème de la descente) de le vérifier en remplaçant S par les spectres des complétés des anneaux locaux; de plus, utilisant la géométrie formelle [lorsque G est bien plongé dans le groupe [H struck] linéaire] on est ramené à le/la vérifier formellement. On revient au cas d’un anneau de base Artinien (all compressed). Travaillant de proche en proche, on est ramené à le/la vérifier pour ... pour/sur les corps résiduels de S (underlined pour; compressed preceding noun uncertain). Utilisant à nouveau la descente on serait ramené à le/la vérifier ... sur les clôtures algébriques des corps résiduels ... . On peut sans doute s’en tirer plus astucieusement. Accents néanmoins, général, fibré, théorème, vérifier, complétés, géométrie, plongé, linéaire, ramené, à, résiduels, clôtures, algébriques checked, although several letters are waves. No dates, headings, indices i/j, or separate margin notes.

### Visual checks

All text reread including the faint left starts of lines and the compressed final lines. The parenthetical descent phrase permits la théorie/le théorème, now explicitly marked rather than silently choosing the first-pass reading. The underlined preposition before les corps résiduels looks sur/pour and now retains both; pour les courbes remains tentative rather than replaced from the expected reduction. amené/ramené likewise marked after comparing the first stroke. The full word astucieusement is joined across the handwritten line end, still unsure. E has three bars; no F alternative needed. Script/calligraphic P_S is checked afresh; G, S and X−S are plain, with no extra double stroke. No i/j indices or exponents, displays, diagrams, typed additions or margin notes. The crossed fibré principal and H-like symbol before linéaire remain deleted; underlines on complétés and formellement remain live. All inline mathematical objects are listed below and checked against the crops. Accent checks match the independently recorded list; the densest clause on the artinian/remainder-field reduction stays low confidence.

### Changes (before → after)

```diff
--- before
+++ after
@@ -1,10 +1,10 @@
 \scanpage{31}
 % archive sheet number: 30
 % L1--7
-Il semble néanmoins que dans le cas général, pour prouver qu’un fibré principal $E$ sur $X-S$ provient d’une \deleted{fibré principal} extension de $\unsure{\mathscr P|\mathcal P}_S$ par $G$, il suffit (utilisant la théorie de la descente) de le vérifier en \unsure{remplaçant} $S$ par les spectres des \uline{complétés} de ses anneaux locaux.
+Il semble néanmoins que dans le cas général, pour prouver qu’un fibré principal $E$ sur $X-S$ provient d’une \deleted{fibré principal} extension de $\unsure{\mathscr P|\mathcal P}_S$ par $G$, il suffit (utilisant \unsure{la théorie|le théorème} de la descente) de le vérifier en \unsure{remplaçant} $S$ par les spectres des \uline{complétés} de ses anneaux locaux.
 % L8--10
 De plus, utilisant la géométrie formelle [lorsque $G$ est bien plongé dans le groupe \deleted{\unsure{H|\mathrm H}} linéaire] on est ramené à le vérifier \uline{formellement}.
 % L11--14
-Cela revient au cas d’un \unsure{anneau} de base \unsure{Artinien}. Travaillant de proche en proche, on est ramené à le vérifier \unsure{pour les courbes} \uline{\unsure{sur}} les corps résiduels de $S$.
+Cela revient au cas d’un \unsure{anneau} de base \unsure{Artinien}. Travaillant de proche en proche, on est ramené à le vérifier \unsure{pour les courbes} \uline{\unsure{sur|pour}} les corps résiduels de $S$.
 % L15--19
-Utilisant à nouveau la descente on serait amené à le vérifier à nouveau sur les clôtures algébriques des corps résiduels\unsure{...---} On peut sans doute s’en tirer plus \unsure{astucieusement}.
+Utilisant à nouveau la descente on serait \unsure{amené|ramené} à le vérifier à nouveau sur les clôtures algébriques des corps résiduels\unsure{...---} On peut sans doute s’en tirer plus \unsure{astucieusement}.
```

### Formula and diagram register checked against the crops

1. Source line 4:

```latex
$E$
```

2. Source line 4:

```latex
$X-S$
```

3. Source line 4:

```latex
$\unsure{\mathscr P|\mathcal P}_S$
```

4. Source line 4:

```latex
$G$
```

5. Source line 4:

```latex
$S$
```

6. Source line 6:

```latex
$G$
```

7. Source line 8:

```latex
$S$
```


## Cross-page reconciliation and final layout review

Actual UTC: 2026-11-17T23:54:53+00:00. Scans 20 s3, 22 s1/s3 and the already enlarged scan 23 last-line crop were compared again. The recurring looped capital has the same descending loop and rising diagonal; script J is now first, with plain J and gamma alternatives at the first occurrence on each affected page. The lower scan-22 J_G has no visible zero above it; the first-pass superscript 0 is removed rather than propagated from scan 20. The outline around scan 20’s penultimate diamond and the large right bracket on scan 22 are now drawn in TikZ; their geometry is an approximation of the freehand strokes, with the objects and connectors retained. The former is not recast as a confident deletion.

### Scan 20 changes

```diff
--- before reconciliation
+++ after reconciliation
@@ -25,15 +25,15 @@
 \end{tikzcd}}
 \par\medskip\hrule\medskip
 % L9--11: diamond; oblique quadrilateral around the left internal nodes.
-\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\&\prod G(\underline{\mathcal O}_x)\arrow[dr,no head]\&\&J_G^0\arrow[dr,no head]\\
-G(C)\arrow[ur,no head]\arrow[dr]\&\&R_G^0\arrow[ur,no head]\arrow[dr]\&\&H^1(X,G)^0\\
-\&G(K)\arrow[ur,no head]\&\&\mathrm{Div}_G^0\arrow[ur,no head]
+\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large,execute at end picture={\draw ([xshift=-2em]p20.west)--([yshift=2em]p20.north)--([xshift=2em]r20.east)--([xshift=1em,yshift=-1.5em]k20.south east)--([xshift=-2em]k20.south west)--([yshift=-.1em]c20.east)--cycle;}]
+\&|[alias=p20]|\prod G(\underline{\mathcal O}_x)\arrow[dr,no head]\&\&J_G^0\arrow[dr,no head]\\
+|[alias=c20]|G(C)\arrow[ur,no head]\arrow[dr]\&\&|[alias=r20]|R_G^0\arrow[ur,no head]\arrow[dr]\&\&H^1(X,G)^0\\
+\&|[alias=k20]|G(K)\arrow[ur,no head]\&\&\mathrm{Div}_G^0\arrow[ur,no head]
 \end{tikzcd}}
 \par\medskip\hrule\medskip
 % L12--14: final diamond. Question marks are manuscript text.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 \&J_1=\prod J_{\underline{\mathcal O}_D/k}^0\arrow[dr]\&\&J_{K/k}^0\arrow[dr]\\
-?\arrow[ur]\arrow[dr]\&\&(\prod_{\substack{D\\\mathrm{local}}}J_{\underline{\mathcal O}_D/k}^*)^0\arrow[ur]\arrow[dr]\&\&\unsure{J|\gamma}_{X/k}^0\\
+?\arrow[ur]\arrow[dr]\&\&(\prod_{\substack{D\\\mathrm{local}}}J_{\underline{\mathcal O}_D/k}^*)^0\arrow[ur]\arrow[dr]\&\&\unsure{\mathscr J|J|\gamma}_{X/k}^0\\
 \&?\arrow[ur]\&\&(\unsure{\sum|\prod|\coprod}_{D}\deleted{\unsure{\mathrm{loc}}}J_{k(D)/k}^*)^0\arrow[ur]
 \end{tikzcd}}
```
### Scan 22 changes

```diff
--- before reconciliation
+++ after reconciliation
@@ -3,7 +3,7 @@
 % L1--3.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 0\arrow[r,no head]\&G(K)/G(C)\arrow[r]\arrow[dr,no head]\&\mathrm{Div}_G^0\arrow[r,no head,"\vert" description]\&\deleted{\unsure{D}}H^1(X,G)^0\arrow[r,no head]\&0\\
-\prod_{\substack{Z\text{ de}\\\text{codim }2}}J_{\unsure{\underline{\mathcal O}_Z|\underline O_Z}/k}\arrow[r]\&\underset{?}{\underline{\prod J_{\underline{\mathcal O}_D/k}^0}}\arrow[r,"u"']\arrow[ur,no head]\&J_{K/k}^0\arrow[r,"\vert" description]\&\unsure{J|\gamma}_{X/k}^0\arrow[r,no head]\&0
+\prod_{\substack{Z\text{ de}\\\text{codim }2}}J_{\unsure{\underline{\mathcal O}_Z|\underline O_Z}/k}\arrow[r]\&\underset{?}{\underline{\prod J_{\underline{\mathcal O}_D/k}^0}}\arrow[r,"u"']\arrow[ur,no head]\&J_{K/k}^0\arrow[r,"\vert" description]\&\unsure{\mathscr J|J|\gamma}_{X/k}^0\arrow[r,no head]\&0
 \end{tikzcd}}
 \margin{\uline{$X$ complet}}
 % L4, cancelled line.
@@ -27,9 +27,9 @@
 \&\phantom{A'}\&\phantom A\&\phantom{A''}
 \end{tikzcd}}
 % L10--13: two lower sequences and crossing question-marked diagonals.
-\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-0\arrow[r,no head]\&\dfrac{\prod G(\underline{\mathcal O}_x)}{G(C)}\arrow[r]\arrow[dr,"?","\times" description]\&J_G^0\arrow[r]\&H^1(X,G)^0\arrow[r,no head]\&0\\
-0\arrow[r,no head]\&?\arrow[r,no head]\arrow[ur,"?"]\&(\sum_D J_{k(D)/k}^*)^0\arrow[r,no head]\&J_{X/k}^0\arrow[r,no head]\&0
+\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large,execute at end picture={\draw ([xshift=.5em,yshift=1em]r22a.north east) .. controls ([xshift=4em]r22a.east) and ([xshift=4em]r22b.east) .. ([xshift=.5em,yshift=-1em]r22b.south east);}]
+0\arrow[r,no head]\&\dfrac{\prod G(\underline{\mathcal O}_x)}{G(C)}\arrow[r]\arrow[dr,"?","\times" description]\&J_G\arrow[r]\&H^1(X,G)^0\arrow[r,no head]\&|[alias=r22a]|0\\
+0\arrow[r,no head]\&?\arrow[r,no head]\arrow[ur,"?"]\&(\sum_D J_{k(D)/k}^*)^0\arrow[r,no head]\&\mathscr J_{X/k}^0\arrow[r,no head]\&|[alias=r22b]|0
 \end{tikzcd}}
 % slanted
 \margin{Aucun \unsure{accouplement} \unsure{convenable} \unsure{ne semble} \unsure{exister} \unsure{.....|....}}
```

### Applying two audit replacements verified against saved files

2026-11-17T23:55:47+00:00. The earlier attempted string substitutions for scan 25’s terminal segment and scan 29’s inserted primed product did not match the source apostrophes. The following diffs apply the already documented visual decisions.

Scan 25:

```diff
--- before
+++ after
@@ -27,7 +27,7 @@
 \]
 dont le noyau sera noté $\mathscr P_{X/Y}^c$, d'où la suite exacte
 \[
-0\longrightarrow\mathscr P_{X/Y}^c\longrightarrow\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}\longrightarrow0
+0\longrightarrow\mathscr P_{X/Y}^c\longrightarrow\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}\unsure{\longrightarrow|\text{---}}0
 \]
 % L18--22.
 \unsure{Noter} que l'on a un \uline{homomorphisme \unsure{canon.|canonique}}
```
Scan 29:

```diff
--- before
+++ after
@@ -6,7 +6,7 @@
 \end{minipage}\par
 
 % L4--9
-Soient $Q,Q'$ deux telles extensions, de groupes $G,G'$. Un hom. de $Q'$ en $\unsure{Q'|Q}$ est \inserted{un couple formé d’un hom. $u:G'\longrightarrow G$ et d’} un\unsure{e} \deleted{isom. de $Q''=Q\times_{G'}G$ avec} \deleted{\unsure{élément de} $\operatorname{Hom}_{\unsure{S,u}}(\unsure{Q'|G'},Q)$, \unsure{avec}} \deleted{qui est un fibré} \inserted{\unsure{isom. de} $Q''=\unsure{Q\times_{G'}G|Q'\times_{G'}G}$} $Q'$ \deleted{\unsure{ou}} (on \unsure{entend} par extension de groupe \uline{donné} $G'$). Il y en a \unsure{ssi} $\unsure{Q'|Q}$ et $Q''$ sont isomorphes. Or
+Soient $Q,Q'$ deux telles extensions, de groupes $G,G'$. Un hom. de $Q'$ en $\unsure{Q'|Q}$ est \inserted{un couple formé d’un hom. $u:G'\longrightarrow G$ et d’} un\unsure{e} \deleted{isom. de $Q''=Q\times_{G'}G$ avec} \deleted{\unsure{élément de} $\operatorname{Hom}_{\unsure{S,u}}(\unsure{Q'|G'},Q)$, \unsure{avec}} \deleted{qui est un fibré} \inserted{\unsure{isom. de} $Q''=\unsure{Q'\times_{G'}G|Q\times_{G'}G}$} $Q'$ \deleted{\unsure{ou}} (on \unsure{entend} par extension de groupe \uline{donné} $G'$). Il y en a \unsure{ssi} $\unsure{Q'|Q}$ et $Q''$ sont isomorphes. Or
 % margin note written slanted, rising to the right
 \margin{il faut \unsure{pouvoir} définir les fibrés associés, Attention!}
 % left-middle diagram
```

### Margin placement reconciliation, scan 25

2026-11-17T23:57:54+00:00. The bracketed comment below condition d is placed in the margin, agreeing with its inventory position; its wording is unchanged.

```diff
--- before
+++ after
@@ -12,7 +12,7 @@
 \item $Y$ loc. noethérien
 \item $X$ propre sur $Y$ (\unsure{faut-il} même : loc. projectif ?)
 \item $X$ plat sur $Y$
-\item Les fibres de $X$ sur $S$ sont des courbes algébriques \uline{absolument} \deleted{\unsure{connexes}} \deleted{\unsure{irréductibles}} \uline{réduites} et absolument \deleted{réduites}\inserted{connexes} [ce dernier pt n'est pas essentiel ---]
+\item Les fibres de $X$ sur $S$ sont des courbes algébriques \uline{absolument} \deleted{\unsure{connexes}} \deleted{\unsure{irréductibles}} \uline{réduites} et absolument \deleted{réduites}\inserted{connexes} \margin{[ce dernier pt n'est pas essentiel ---]}
 \item Le nb de composantes \deleted{\illegible{1}} irréd. absolues des fibres de $X$ sur $Y$ est loc. constant sur $Y$
 \end{enumerate}
 % slanted
```

## Syntax-only grouping before freeze

2026-11-17T23:57:54+00:00. The supplied `\unsure` macro itself emits a superscript question mark in math mode. Each invocation is enclosed in an ordinary TeX group so a following manuscript exponent cannot produce a double-superscript error. No argument, reading, candidate order, or mark count changes. This is a static source repair; no compilation was attempted.

### K43-02_43_scan017.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -9,15 +9,15 @@
 \end{tikzcd}}
 % L4--8: upper left square and its labels.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\text{\unsure{proalgébriques}}\quad\prod_{\deleted{\unsure{\mathrm{loc}}}}G(\unsure{\hat{\mathcal O}_x|\hat O_x})\arrow[d] \& 0\arrow[l]\arrow[d]\\
-\substack{\text{\unsure{pts. adéliques}}\\=\text{\unsure{répartitions}}}\quad\prod_{\mathrm{loc}}G(\hat K_x) \& \underset{\substack{\text{\unsure{fts rationnelles}}\\=\text{rép. principales}}}{G(K_\xi)}\arrow[l]
+\text{{\unsure{proalgébriques}}}\quad\prod_{\deleted{{\unsure{\mathrm{loc}}}}}G({\unsure{\hat{\mathcal O}_x|\hat O_x}})\arrow[d] \& 0\arrow[l]\arrow[d]\\
+\substack{\text{{\unsure{pts. adéliques}}}\\=\text{{\unsure{répartitions}}}}\quad\prod_{\mathrm{loc}}G(\hat K_x) \& \underset{\substack{\text{{\unsure{fts rationnelles}}}\\=\text{rép. principales}}}{G(K_\xi)}\arrow[l]
 \end{tikzcd}}
-\margin{\unsure{bicomplexe} $DD(G)$}
+\margin{{\unsure{bicomplexe}} $DD(G)$}
 \margin{Cohomologie $H^0(C,G)$ et $H^1(C,G)$}
 % L9--13: second square; the aggregation signs have superposed vertical and zigzag strokes.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\text{``\unsure{torsion}''}\quad\unsure{\sum|\prod|\coprod}_{\unsure{x|n}}H_x^0(G)\arrow[d] \& 0\arrow[l]\arrow[d]\\
-\text{diviseurs}\quad\sum_x H_x^1(G) \& \underset{\text{\unsure{pts rationnels} de $G$}}{H_\xi^0(G)}\arrow[l]
+\text{``{\unsure{torsion}}''}\quad{\unsure{\sum|\prod|\coprod}}_{{\unsure{x|n}}}H_x^0(G)\arrow[d] \& 0\arrow[l]\arrow[d]\\
+\text{diviseurs}\quad\sum_x H_x^1(G) \& \underset{\text{{\unsure{pts rationnels}} de $G$}}{H_\xi^0(G)}\arrow[l]
 \end{tikzcd}}
 \[
 \begin{aligned}
@@ -29,17 +29,17 @@
 \[
 H^*(C,G)=\text{cohomologie}
 \]
-du \unsure{complexe}
+du {\unsure{complexe}}
 \[
 \underbrace{H_\xi^0(G)}_{\substack{G\text{-diviseurs}\\\text{principaux}}}
-\unsure{\longrightarrow|\text{---}}
-\underbrace{\prod_{\unsure{x|\alpha}} H_x^1(G)}_{G\text{-diviseurs}}
+{\unsure{\longrightarrow|\text{---}}}
+\underbrace{\prod_{{\unsure{x|\alpha}}} H_x^1(G)}_{G\text{-diviseurs}}
 \]
 % L14--19: lower left group, enclosed on the sheet by a curved outline.
 \diagram{\begin{tikzpicture}\node[draw,rounded corners=7mm,inner sep=6pt]{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\underset{\phantom{a}}{\overset{\text{\unsure{adèles entiers}}}{\prod G(\hat{\mathcal O}_x)}}\arrow[d] \& 0\arrow[l]\arrow[d] \& G(C)=H^0(\unsure{C,C|G,C|C,G}) \& 0\\
-\underbrace{(\prod_{\mathrm{loc}}G(\hat K_x))/G(K_\xi)}_{\text{\unsure{classes d'adèles}}} \& 0\arrow[l] \& H^1(C,G) \& 0\\
+\underset{\phantom{a}}{\overset{\text{{\unsure{adèles entiers}}}}{\prod G(\hat{\mathcal O}_x)}}\arrow[d] \& 0\arrow[l]\arrow[d] \& G(C)=H^0({\unsure{C,C|G,C|C,G}}) \& 0\\
+\underbrace{(\prod_{\mathrm{loc}}G(\hat K_x))/G(K_\xi)}_{\text{{\unsure{classes d'adèles}}}} \& 0\arrow[l] \& H^1(C,G) \& 0\\
 H_{\mathrm{II}}DD(G) \& \& H_{\mathrm I}H_{\mathrm{II}}DD(G)
 \end{tikzcd}};\end{tikzpicture}}
 % L20--21.
-qui peuvent aussi \unsure{s'exprimer} à l'aide de \unsure{quotients locaux} -----
+qui peuvent aussi {\unsure{s'exprimer}} à l'aide de {\unsure{quotients locaux}} -----
```
### K43-02_43_scan018.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -5,24 +5,24 @@
 \prod J_x^{(0)}\arrow[r]\arrow[d,equal] \& J_\xi^*\\
 J_1 \& J_0=J_{K/k}
 \end{tikzcd}}
-\unsure{ou}
+{\unsure{ou}}
 \[
-\deleted{\unsure{\mathrm{gr}}}\quad J_{C/k}^*\quad\text{jacobienne de }C
+\deleted{{\unsure{\mathrm{gr}}}}\quad J_{C/k}^*\quad\text{jacobienne de }C
 \]
 % L4--12: crossed block. All its readable content is retained as deleted.
-\deleted{La chose \unsure{spéciale|précise} et surprenante, c'est que l'on a aussi $J_{C/k}^*\simeq\underline{H}^1(C,G_m)$, \unsure{et} [si on \unsure{prend} le complexe $\operatorname{Hom}_{k\text{-}\unsure{\mathrm{gr}}}(\unsure{J_*|J^*},G_m)$, on trouve}
+\deleted{La chose {\unsure{spéciale|précise}} et surprenante, c'est que l'on a aussi $J_{C/k}^*\simeq\underline{H}^1(C,G_m)$, {\unsure{et}} [si on {\unsure{prend}} le complexe $\operatorname{Hom}_{k\text{-}{\unsure{\mathrm{gr}}}}({\unsure{J_*|J^*}},G_m)$, on trouve}
 \[
-\deleted{K^*\longrightarrow\substack{\text{diviseurs}\\\text{\unsure{ordinaires}}}}
+\deleted{K^*\longrightarrow\substack{\text{diviseurs}\\\text{{\unsure{ordinaires}}}}}
 \]
-\deleted{] et que $J_x^{(0)}(k)=G_m(\unsure{\hat{\mathcal O}_x|\hat O_x})$.}
+\deleted{] et que $J_x^{(0)}(k)=G_m({\unsure{\hat{\mathcal O}_x|\hat O_x}})$.}
 
-\deleted{Il faut aussi expliquer le rôle \unsure{du|de} $J_x^*$.}
+\deleted{Il faut aussi expliquer le rôle {\unsure{du|de}} $J_x^*$.}
 % L13--19.
-La chose \unsure{non|un} \unsure{primordiale|principale} : \unsure{primo}, c'est que le complexe
+La chose {\unsure{non|un}} {\unsure{primordiale|principale}} : {\unsure{primo}}, c'est que le complexe
 \[
-J_1\unsure{\longrightarrow|\text{---}}J_0
+J_1{\unsure{\longrightarrow|\text{---}}}J_0
 \]
-(ou plutôt $J_1(k)\unsure{\longrightarrow|\text{---}}J_0(k)$) \unsure{n'est} autre que $H_{\mathrm{II}}DD(G_m)$, on peut donc, \unsure{moyennant} un abus de \unsure{notations},, écrire
+(ou plutôt $J_1(k){\unsure{\longrightarrow|\text{---}}}J_0(k)$) {\unsure{n'est}} autre que $H_{\mathrm{II}}DD(G_m)$, on peut donc, {\unsure{moyennant}} un abus de {\unsure{notations}},, écrire
 \[
 H_{\mathrm I}DD(G)=\operatorname{Hom}\bigl(\underline{H_{\mathrm{II}}DD}(G_m),G\bigr)
 \]
```
### K43-02_43_scan019.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -2,31 +2,31 @@
 % archive sheet number: 18
 % L1--3, upper diagrams.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-\prod_x G(\unsure{\hat{\mathcal O}_x|\hat O_x})\arrow[d] \& 0\arrow[l]\arrow[d] \& 0\arrow[d,rightsquigarrow] \& 0\arrow[l]\arrow[d,rightsquigarrow]\\
-\prod_{\mathrm{local}}G(\hat K_x) \& G(K)\arrow[l] \& G\text{-\unsure{diviseur|diviseurs} sur }X \& G(K)\arrow[l]\\
+\prod_x G({\unsure{\hat{\mathcal O}_x|\hat O_x}})\arrow[d] \& 0\arrow[l]\arrow[d] \& 0\arrow[d,rightsquigarrow] \& 0\arrow[l]\arrow[d,rightsquigarrow]\\
+\prod_{\mathrm{local}}G(\hat K_x) \& G(K)\arrow[l] \& G\text{-{\unsure{diviseur|diviseurs}} sur }X \& G(K)\arrow[l]\\
 \& \& H^1(X,G) \& H^0(X,G)
 \end{tikzcd}}
 % L4--9, small note below the first square.
-i.e. on \unsure{veut} que \unsure{ça corresponde|cela corresponde} à un $G$-diviseur \unsure{véritable} sur $X$ [\unsure{sinon donc|sinon dont} le complexe \unsure{continuerait-il} ---]
+i.e. on {\unsure{veut}} que {\unsure{ça corresponde|cela corresponde}} à un $G$-diviseur {\unsure{véritable}} sur $X$ [{\unsure{sinon donc|sinon dont}} le complexe {\unsure{continuerait-il}} ---]
 % The horizontal rule between the two portions is a page separator.
 \par\medskip\hrule\medskip
 % L10--20: whole lower portion crossed by three oblique strokes.
-\[\deleted{\unsure{\sum|\prod|\coprod}}\]
+\[\deleted{{\unsure{\sum|\prod|\coprod}}}\]
 \[
 \left\{\begin{aligned}
 &\deleted{(f_x)_{x\in X}}\quad\deleted{\text{$G$-répartition}}\\
-&\deleted{(\xi_D)_{D\in\mathrm{Div}\,\text{\unsure{premiers}}}}\qquad
+&\deleted{(\xi_D)_{D\in\mathrm{Div}\,\text{{\unsure{premiers}}}}}\qquad
 \deleted{\xi_D\in J_{\underline{\mathcal O}_D/k}^*}
 \end{aligned}\right.
 \]
 \[
 \begin{aligned}
 \deleted{x\in D}\qquad
-\deleted{f_x\in G(K_x)}&\deleted{\longrightarrow\text{\unsure{classe de} }G(K_D)/\deleted{\unsure{G(\mathcal O_D)}}}\quad
-\deleted{\unsure{\simeq|\longrightarrow}\ G(K_D)/G(\mathcal O_D)^{(1)}}\\
+\deleted{f_x\in G(K_x)}&\deleted{\longrightarrow\text{{\unsure{classe de}} }G(K_D)/\deleted{{\unsure{G(\mathcal O_D)}}}}\quad
+\deleted{{\unsure{\simeq|\longrightarrow}}\ G(K_D)/G(\mathcal O_D)^{(1)}}\\
 &\deleted{\hspace{4em}\simeq\operatorname{Hom}(J_{\underline{\mathcal O}_D/k}^*,G(k))}
 \end{aligned}
 \]
 \deleted{Donc $(f_x,\xi_D)_x\in G(k)$ est défini.}
 
-\deleted{Je dis que $\sum_{x\in|D|}(f_x,\xi_D)$ existe. En effet la question étant locale, on est \unsure{ramené au cas} où $(f_x)$ est formé d'unités,}
+\deleted{Je dis que $\sum_{x\in|D|}(f_x,\xi_D)$ existe. En effet la question étant locale, on est {\unsure{ramené au cas}} où $(f_x)$ est formé d'unités,}
```
### K43-02_43_scan020.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -3,11 +3,11 @@
 % L1--3: two sequences, with a crossed diagonal between them.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 0\arrow[r] \& N\arrow[r]\arrow[dr,"?","{\times}" description] \& Z^0\arrow[r] \& \mathrm{Alb}^0\arrow[r] \&0\\
-0\arrow[r,no head] \& \dfrac{\prod G(\unsure{\underline{\mathcal O}_x|\underline O_x})}{G(C)}\arrow[r]\arrow[ur,no head] \& R_G^0/G(K)\arrow[r,no head] \& H^1(X,G)^0\arrow[r,no head] \&0
+0\arrow[r,no head] \& \dfrac{\prod G({\unsure{\underline{\mathcal O}_x|\underline O_x}})}{G(C)}\arrow[r]\arrow[ur,no head] \& R_G^0/G(K)\arrow[r,no head] \& H^1(X,G)^0\arrow[r,no head] \&0
 \end{tikzcd}}
 % L4: overstruck superscript and discarded Alb.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
-X\arrow[r] \& \prod_D J_{\underline{\mathcal O}_D/k}^{\deleted{\unsure{*}}0}\arrow[r] \& J_{K/k}^0\arrow[r,no head,"\vert" description] \& \deleted{\mathrm{Alb}^0}J_{X/k}^0\arrow[r,no head] \&0
+X\arrow[r] \& \prod_D J_{\underline{\mathcal O}_D/k}^{\deleted{{\unsure{*}}}0}\arrow[r] \& J_{K/k}^0\arrow[r,no head,"\vert" description] \& \deleted{\mathrm{Alb}^0}J_{X/k}^0\arrow[r,no head] \&0
 \end{tikzcd}}
 % L5.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
@@ -16,12 +16,12 @@
 \par\hrule\medskip
 % L6.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
-\text{\textcircled{?}}\arrow[r] \& \underset{\deleted{\unsure{\mathrm{Diviseurs}}}}{\prod J_{k(D)/k}^*}\arrow[r] \& J_{X/k}^*
+\text{\textcircled{?}}\arrow[r] \& \underset{\deleted{{\unsure{\mathrm{Diviseurs}}}}}{\prod J_{k(D)/k}^*}\arrow[r] \& J_{X/k}^*
 \end{tikzcd}}
 % L7--8.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 \prod_{\mathrm{local}}J_{\underline{\mathcal O}_D/k}^*\arrow[r] \& J_{K/k}^*\\
-\prod_{\unsure{\mathrm{loc}}}J_{\underline{\mathcal O}_D/k}^0\arrow[u]\arrow[r,no head] \& \prod J_{\underline{\mathcal O}_D/k}^0\arrow[u]
+\prod_{{\unsure{\mathrm{loc}}}}J_{\underline{\mathcal O}_D/k}^0\arrow[u]\arrow[r,no head] \& \prod J_{\underline{\mathcal O}_D/k}^0\arrow[u]
 \end{tikzcd}}
 \par\medskip\hrule\medskip
 % L9--11: diamond; oblique quadrilateral around the left internal nodes.
@@ -34,6 +34,6 @@
 % L12--14: final diamond. Question marks are manuscript text.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 \&J_1=\prod J_{\underline{\mathcal O}_D/k}^0\arrow[dr]\&\&J_{K/k}^0\arrow[dr]\\
-?\arrow[ur]\arrow[dr]\&\&(\prod_{\substack{D\\\mathrm{local}}}J_{\underline{\mathcal O}_D/k}^*)^0\arrow[ur]\arrow[dr]\&\&\unsure{\mathscr J|J|\gamma}_{X/k}^0\\
-\&?\arrow[ur]\&\&(\unsure{\sum|\prod|\coprod}_{D}\deleted{\unsure{\mathrm{loc}}}J_{k(D)/k}^*)^0\arrow[ur]
+?\arrow[ur]\arrow[dr]\&\&(\prod_{\substack{D\\\mathrm{local}}}J_{\underline{\mathcal O}_D/k}^*)^0\arrow[ur]\arrow[dr]\&\&{\unsure{\mathscr J|J|\gamma}}_{X/k}^0\\
+\&?\arrow[ur]\&\&({\unsure{\sum|\prod|\coprod}}_{D}\deleted{{\unsure{\mathrm{loc}}}}J_{k(D)/k}^*)^0\arrow[ur]
 \end{tikzcd}}
```
### K43-02_43_scan021.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -4,16 +4,16 @@
 \[
 \begin{array}{cc}
 A&A'\\
-k&\deleted{\unsure{K}}L\\
-\multicolumn{2}{c}{\overline{\deleted{\unsure{G}}\Gamma}}
+k&\deleted{{\unsure{K}}}L\\
+\multicolumn{2}{c}{\overline{\deleted{{\unsure{G}}}\Gamma}}
 \end{array}
 \]
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
-H^0(\Gamma,A_L)\times H^1(\Gamma,A'_L)\arrow[r] \& H^2(\Gamma,\deleted{\unsure{K}}L^*)\\
+H^0(\Gamma,A_L)\times H^1(\Gamma,A'_L)\arrow[r] \& H^2(\Gamma,\deleted{{\unsure{K}}}L^*)\\
 A_K\arrow[u,equal]
 \end{tikzcd}}
 \[
-\unsure{\operatorname{Ext}|\operatorname{Ext}^1}_{\unsure{\mathbb Z(\Gamma)/\mathbb Z|\mathbb Z[\Gamma]/\mathbb Z}}(A_L,A'_L\deleted{\unsure{*}};L^*)
+{\unsure{\operatorname{Ext}|\operatorname{Ext}^1}}_{{\unsure{\mathbb Z(\Gamma)/\mathbb Z|\mathbb Z[\Gamma]/\mathbb Z}}}(A_L,A'_L\deleted{{\unsure{*}}};L^*)
 \]
 % L4--8: left resolution sketch, crossed diagonals drawn without arrowheads.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
@@ -23,14 +23,14 @@
 0\arrow[u]\&0\arrow[u]
 \end{tikzcd}}
 \[
-\unsure{\mathcal L_*|\mathscr L_*}\qquad \mathcal L'_*
+{\unsure{\mathcal L_*|\mathscr L_*}}\qquad \mathcal L'_*
 \]
 % L4--10: right product and composition diagram.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=large]
-\begin{gathered}\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i}}_\Gamma(\mathbb Z;A_L)\\\times\\\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{j}}_\Gamma(\mathbb Z,A'_L)\end{gathered}\arrow[d]\\
-\unsure{\operatorname{Ext}^{2}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i+j}}_\Gamma(\mathbb Z,\mathbb Z;A_L,A'_L)\times\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}}_\Gamma(A_L,A'_L;L^*)\arrow[d]\\
-\operatorname{Ext}_\Gamma^2(\mathbb Z,\mathbb Z;L^*)\arrow[d,"{\text{\uuline{\unsure{cup}}}}"]\\
-\unsure{\operatorname{Ex}|\operatorname{Ext}}_\Gamma^2(\mathbb Z,L^*)
+\begin{gathered}{\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i}}}_\Gamma(\mathbb Z;A_L)\\\times\\{\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}|\operatorname{Ext}^{j}}}_\Gamma(\mathbb Z,A'_L)\end{gathered}\arrow[d]\\
+{\unsure{\operatorname{Ext}^{2}|\operatorname{Ext}^{1}|\operatorname{Ext}^{i+j}}}_\Gamma(\mathbb Z,\mathbb Z;A_L,A'_L)\times{\unsure{\operatorname{Ext}|\operatorname{Ext}^{1}}}_\Gamma(A_L,A'_L;L^*)\arrow[d]\\
+\operatorname{Ext}_\Gamma^2(\mathbb Z,\mathbb Z;L^*)\arrow[d,"{\text{\uuline{{\unsure{cup}}}}}"]\\
+{\unsure{\operatorname{Ex}|\operatorname{Ext}}}_\Gamma^2(\mathbb Z,L^*)
 \end{tikzcd}}
 % L9--13: left formulas.
 \[
@@ -39,7 +39,7 @@
 \[
 \begin{aligned}
 &H^1\bigl(\operatorname{Hom}(\mathcal L_*\otimes_{\mathbb Z}\mathcal L'_*,G)^\Gamma\bigr)\\
-&H^1\bigl(\operatorname{Hom}(\unsure{M_*|\mathcal M_*},\mathcal L_*)^\Gamma\bigr)\\
+&H^1\bigl(\operatorname{Hom}({\unsure{M_*|\mathcal M_*}},\mathcal L_*)^\Gamma\bigr)\\
 &H^1\bigl(\operatorname{Hom}(M_*,\mathcal L'_*)^\Gamma\bigr)
 \end{aligned}
 \]
@@ -50,21 +50,21 @@
 \]
 % L14--17.
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
-M_*\arrow[r,no head,"{\Gamma\text{-}\unsure{\mathrm{hom}}}"]\&\mathcal L_*\\
+M_*\arrow[r,no head,"{\Gamma\text{-}{\unsure{\mathrm{hom}}}}"]\&\mathcal L_*\\
 M_*\arrow[r,no head,"{\Gamma\text{-}\mathrm{hom}}"]\&\mathcal L'_*
 \end{tikzcd}}
 \[\deleted{P,Q}\]
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
-\text{\uline{\unsure{projectif}}}\quad\mathcal L_*^P\otimes\mathcal L_*^Q\arrow[r,no head]\arrow[d] \& P\otimes Q\arrow[d,equal]\\
+\text{\uline{{\unsure{projectif}}}}\quad\mathcal L_*^P\otimes\mathcal L_*^Q\arrow[r,no head]\arrow[d] \& P\otimes Q\arrow[d,equal]\\
 \text{\uline{résolution}}\quad\tilde{\mathcal L}_*^{P\otimes Q}\arrow[r]\&P\otimes Q
 \end{tikzcd}}
 % L18--20.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
 M_*\otimes_{\mathbb Z}M_*\arrow[r,"{\Gamma\text{-}\mathrm{hom}}"]\&\mathcal L_*\otimes_{\mathbb Z}\mathcal L'_*\arrow[r,"{\Gamma\text{-}\mathrm{hom}}"]\&G\\
-M_*\arrow[u,"{\text{\uuline{\unsure{cup}}}\ 2}"]
+M_*\arrow[u,"{\text{\uuline{{\unsure{cup}}}}\ 2}"]
 \end{tikzcd}}
 \[
-\frac{1}{A_K/N_{L/k}A_L\ /\ \substack{\text{\unsure{ss-groupe}}\\\text{de }H^1(\Gamma,A'_L)}}
+\frac{1}{A_K/N_{L/k}A_L\ /\ \substack{\text{{\unsure{ss-groupe}}}\\\text{de }H^1(\Gamma,A'_L)}}
 \]
 % L21--22: bottom isolated items.
 \[
```
### K43-02_43_scan022.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -2,21 +2,21 @@
 % archive sheet number: 21
 % L1--3.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
-0\arrow[r,no head]\&G(K)/G(C)\arrow[r]\arrow[dr,no head]\&\mathrm{Div}_G^0\arrow[r,no head,"\vert" description]\&\deleted{\unsure{D}}H^1(X,G)^0\arrow[r,no head]\&0\\
-\prod_{\substack{Z\text{ de}\\\text{codim }2}}J_{\unsure{\underline{\mathcal O}_Z|\underline O_Z}/k}\arrow[r]\&\underset{?}{\underline{\prod J_{\underline{\mathcal O}_D/k}^0}}\arrow[r,"u"']\arrow[ur,no head]\&J_{K/k}^0\arrow[r,"\vert" description]\&\unsure{\mathscr J|J|\gamma}_{X/k}^0\arrow[r,no head]\&0
+0\arrow[r,no head]\&G(K)/G(C)\arrow[r]\arrow[dr,no head]\&\mathrm{Div}_G^0\arrow[r,no head,"\vert" description]\&\deleted{{\unsure{D}}}H^1(X,G)^0\arrow[r,no head]\&0\\
+\prod_{\substack{Z\text{ de}\\\text{codim }2}}J_{{\unsure{\underline{\mathcal O}_Z|\underline O_Z}}/k}\arrow[r]\&\underset{?}{\underline{\prod J_{\underline{\mathcal O}_D/k}^0}}\arrow[r,"u"']\arrow[ur,no head]\&J_{K/k}^0\arrow[r,"\vert" description]\&{\unsure{\mathscr J|J|\gamma}}_{X/k}^0\arrow[r,no head]\&0
 \end{tikzcd}}
 \margin{\uline{$X$ complet}}
 % L4, cancelled line.
 \[\deleted{\mathrm{Div}_G\qquad G(K)/G(C)}\]
 % L5--6, two definitions and the small arrow from Im towards Ker.
-\deleted{\unsure{Div c Div}}
+\deleted{{\unsure{Div c Div}}}
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 (G\text{-}\mathrm{Div})=\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0/\&\operatorname{Im}(\prod_{Z\text{ cod., }2}J_{\underline{\mathcal O}_Z/k})\bigr)\arrow[d]\\
-(G\text{-}\mathrm{Div})^0\underset{\text{\unsure{pl.-isib.|pl.-isom}}}{=}\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0\&\mid .\operatorname{Ker}u\bigr)
+(G\text{-}\mathrm{Div})^0\underset{\text{{\unsure{pl.-isib.|pl.-isom}}}}{=}\operatorname{Hom}\bigl(\prod J_{\underline{\mathcal O}_D/k}^0\&\mid .\operatorname{Ker}u\bigr)
 \end{tikzcd}}
 % L7--9: boxed statements.
 \[
-\boxed{(G\text{-}\mathrm{Div})/(G\text{-}\mathrm{Div})^0\subset\operatorname{Hom}(H_1(J_*),G\deleted{\unsure{(k)}})}
+\boxed{(G\text{-}\mathrm{Div})/(G\text{-}\mathrm{Div})^0\subset\operatorname{Hom}(H_1(J_*),G\deleted{{\unsure{(k)}}})}
 \]
 \[
 \boxed{\text{Ex. Néron-Severi}\ \subset\operatorname{Hom}(H_1(J_*),G_m)}
@@ -32,6 +32,6 @@
 0\arrow[r,no head]\&?\arrow[r,no head]\arrow[ur,"?"]\&(\sum_D J_{k(D)/k}^*)^0\arrow[r,no head]\&\mathscr J_{X/k}^0\arrow[r,no head]\&|[alias=r22b]|0
 \end{tikzcd}}
 % slanted
-\margin{Aucun \unsure{accouplement} \unsure{convenable} \unsure{ne semble} \unsure{exister} \unsure{.....|....}}
+\margin{Aucun {\unsure{accouplement}} {\unsure{convenable}} {\unsure{ne semble}} {\unsure{exister}} {\unsure{.....|....}}}
 \[G(L)\]
-\unsure{Quel} était l'accouplement \unsure{-étique|-adique} de Tate ???
+{\unsure{Quel}} était l'accouplement {\unsure{-étique|-adique}} de Tate ???
```
### K43-02_43_scan023.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -1,15 +1,15 @@
 \scanpage{23}
 % archive sheet number: 22
 % L1.
-\[X\times Y\qquad A\quad\unsure{\operatorname{Ext}|\operatorname{Ext}^1}(A,G)\]
+\[X\times Y\qquad A\quad{\unsure{\operatorname{Ext}|\operatorname{Ext}^1}}(A,G)\]
 % L2--5.
-$D$ \deleted{\unsure{G}} $G$-diviseur \inserted{\tikz[baseline=(w.base)]{\node[draw,rounded corners=12pt,inner sep=2pt] (w) {\unsure{ordinaire|bilatéral}};}} sur $X\times Y$, \unsure{horizontal} \unsure{rel.} à \unsure{la projection} $X\times Y\longrightarrow X$ transforme $0$-cycles de $X$ en $G$-diviseurs sur $Y$, et $0$-cycles du noyau d'Albanese en $G$-diviseurs principaux (?).
+$D$ \deleted{{\unsure{G}}} $G$-diviseur \inserted{\tikz[baseline=(w.base)]{\node[draw,rounded corners=12pt,inner sep=2pt] (w) {{\unsure{ordinaire|bilatéral}}};}} sur $X\times Y$, {\unsure{horizontal}} {\unsure{rel.}} à {\unsure{la projection}} $X\times Y\longrightarrow X$ transforme $0$-cycles de $X$ en $G$-diviseurs sur $Y$, et $0$-cycles du noyau d'Albanese en $G$-diviseurs principaux (?).
 
-\deleted{\unsure{Diviseur}}
+\deleted{{\unsure{Diviseur}}}
 % L6--8.
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
 X\times Y\arrow[dr]\\
-\&\unsure{\operatorname{Pic}^*(Y)}
+\&{\unsure{\operatorname{Pic}^*(Y)}}
 \end{tikzcd}}
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
 J_{X/k}^*\arrow[r]\&\operatorname{Pic}_G^*(Y)
@@ -17,9 +17,9 @@
 % L9--14.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
 0\arrow[r,no head]\&\substack{\text{Noyau de}\\\text{Albanese}}\arrow[r,no head]\arrow[d]\&\underset{\substack{0\text{-cycles}\\\text{de deg }0}}{Z_X^0}\arrow[r]\arrow[d]\&\underset{\text{Albanese de }X}{J_{X/k}^0}\arrow[r,no head]\arrow[d]\&0\\
-0\arrow[r,no head]\&G(K)/G(Y)\arrow[r]\&\underset{\substack{\text{\unsure{au. alg.\textsuperscript{t}}}\\\text{équiv. à }0}}{\mathrm{Div}^0(\deleted{\unsure{X}}Y,G)}\arrow[r]\&\underset{\substack{\text{classes de fibrés}\\\text{alg. équiv. à }0}}{\operatorname{Pic}^0(Y,G)}\arrow[r]\&0
+0\arrow[r,no head]\&G(K)/G(Y)\arrow[r]\&\underset{\substack{\text{{\unsure{au. alg.\textsuperscript{t}}}}\\\text{équiv. à }0}}{\mathrm{Div}^0(\deleted{{\unsure{X}}}Y,G)}\arrow[r]\&\underset{\substack{\text{classes de fibrés}\\\text{alg. équiv. à }0}}{\operatorname{Pic}^0(Y,G)}\arrow[r]\&0
 \end{tikzcd}}
 % L15, bottom sequence.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
-0\arrow[r,no head]\&\text{Noyau}\arrow[r]\&J_{K_Y/k}^0\arrow[r,no head]\&\unsure{\mathscr J|J|\gamma}_{Y/k}^0\arrow[r]\&0
+0\arrow[r,no head]\&\text{Noyau}\arrow[r]\&J_{K_Y/k}^0\arrow[r,no head]\&{\unsure{\mathscr J|J|\gamma}}_{Y/k}^0\arrow[r]\&0
 \end{tikzcd}}
```
### K43-02_43_scan024.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -1,4 +1,4 @@
 \scanpage{24}
 % archive sheet number: 23
 % L1, upper right title; the rest of the sheet is blank.
-\unsure{Théorie} de Rosenlicht
+{\unsure{Théorie}} de Rosenlicht
```
### K43-02_43_scan025.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -10,27 +10,27 @@
 
 \begin{enumerate}[label=\alph*)]
 \item $Y$ loc. noethérien
-\item $X$ propre sur $Y$ (\unsure{faut-il} même : loc. projectif ?)
+\item $X$ propre sur $Y$ ({\unsure{faut-il}} même : loc. projectif ?)
 \item $X$ plat sur $Y$
-\item Les fibres de $X$ sur $S$ sont des courbes algébriques \uline{absolument} \deleted{\unsure{connexes}} \deleted{\unsure{irréductibles}} \uline{réduites} et absolument \deleted{réduites}\inserted{connexes} \margin{[ce dernier pt n'est pas essentiel ---]}
+\item Les fibres de $X$ sur $S$ sont des courbes algébriques \uline{absolument} \deleted{{\unsure{connexes}}} \deleted{{\unsure{irréductibles}}} \uline{réduites} et absolument \deleted{réduites}\inserted{connexes} \margin{[ce dernier pt n'est pas essentiel ---]}
 \item Le nb de composantes \deleted{\illegible{1}} irréd. absolues des fibres de $X$ sur $Y$ est loc. constant sur $Y$
 \end{enumerate}
 % slanted
-\margin{si on abandonne cette hypothèse, on \unsure{trouve des|tombe aux} \unsure{phénomènes} à la Néron ?!}
+\margin{si on abandonne cette hypothèse, on {\unsure{trouve des|tombe aux}} {\unsure{phénomènes}} à la Néron ?!}
 % L10.
-Alors le \unsure{$S$|$f$}-schéma $\unsure{\mathscr P_{X/Y}|\mathcal P_{X/Y}}$ relatif existe, et est \uline{simple} sur $Y$.
+Alors le {\unsure{$S$|$f$}}-schéma ${\unsure{\mathscr P_{X/Y}|\mathcal P_{X/Y}}}$ relatif existe, et est \uline{simple} sur $Y$.
 % L11--17.
-De plus, si le nb des composantes irréductibles absolues est $n$, il y a un revêtement \deleted{$Y$} étale $Y'$ de degré $n$ de $Y$ et si $\mathbb Z_{Y'/Y}$ est le schéma en groupes \inserted{$\prod_{Y'/Y}(\mathbb Z_{Y'})=\underline{\operatorname{Hom}}_Y(Y',\mathbb Z_Y)$} sur $Y$ défini par $Y'$ (qui sur $Y'$ devient isomorphe à $\mathbb Z^n$) on a une augmentation \deleted{\unsure{surjective} et \unsure{propre}} fidèlement plate
-\margin{\uline{\unsure{références}}}
+De plus, si le nb des composantes irréductibles absolues est $n$, il y a un revêtement \deleted{$Y$} étale $Y'$ de degré $n$ de $Y$ et si $\mathbb Z_{Y'/Y}$ est le schéma en groupes \inserted{$\prod_{Y'/Y}(\mathbb Z_{Y'})=\underline{\operatorname{Hom}}_Y(Y',\mathbb Z_Y)$} sur $Y$ défini par $Y'$ (qui sur $Y'$ devient isomorphe à $\mathbb Z^n$) on a une augmentation \deleted{{\unsure{surjective}} et {\unsure{propre}}} fidèlement plate
+\margin{\uline{{\unsure{références}}}}
 \[
-\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}\quad\deleted{\unsure{\infty}}
+\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}\quad\deleted{{\unsure{\infty}}}
 \]
 dont le noyau sera noté $\mathscr P_{X/Y}^c$, d'où la suite exacte
 \[
-0\longrightarrow\mathscr P_{X/Y}^c\longrightarrow\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}\unsure{\longrightarrow|\text{---}}0
+0\longrightarrow\mathscr P_{X/Y}^c\longrightarrow\mathscr P_{X/Y}\longrightarrow\mathbb Z_{Y'/Y}{\unsure{\longrightarrow|\text{---}}}0
 \]
 % L18--22.
-\unsure{Noter} que l'on a un \uline{homomorphisme \unsure{canon.|canonique}}
+{\unsure{Noter}} que l'on a un \uline{homomorphisme {\unsure{canon.|canonique}}}
 \[
 \mathbb Z_{Y'/Y}\longrightarrow\mathbb Z_Y
 \]
```
### K43-02_43_scan026.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -1,23 +1,23 @@
 \scanpage{26}
 % archive sheet number: 25
 % L1--3
-Les fibres de $\unsure{\mathscr P|\mathcal P}^0_{X/S}$ sont connexes, et propres si celles de $X$ sont \uline{simples}. Soit \deleted{\unsure{schéma}} $X-S$ l’\unsure{ens.|ouv.} des pts de $X$ qui sont \unsure{non} simples sur $Y$. On va définir un morphisme
+Les fibres de ${\unsure{\mathscr P|\mathcal P}}^0_{X/S}$ sont connexes, et propres si celles de $X$ sont \uline{simples}. Soit \deleted{{\unsure{schéma}}} $X-S$ l’{\unsure{ens.|ouv.}} des pts de $X$ qui sont {\unsure{non}} simples sur $Y$. On va définir un morphisme
 % L4
 \[
 \boxed{X-S\longrightarrow\mathscr P^1_{X/S}}.
 \]
 % L5--8
-où l’exposant $1$ indique qu’on est dans la composante d’augmentation $1$. \unsure{Je reviens|Il revient} \unsure{à en donner} \uline{fonctoriellement} \inserted{pour le changement de base} une application
-\deleted{\unsure{application}}
+où l’exposant $1$ indique qu’on est dans la composante d’augmentation $1$. {\unsure{Je reviens|Il revient}} {\unsure{à en donner}} \uline{fonctoriellement} \inserted{pour le changement de base} une application
+\deleted{{\unsure{application}}}
 \[
-\unsure{\Gamma|\mathscr T}(X-S/Y)\longrightarrow\mathscr P^1(X/S)
+{\unsure{\Gamma|\mathscr T}}(X-S/Y)\longrightarrow\mathscr P^1(X/S)
 \]
 % L9--13
-or on note qu’une section de $X-S$ sur $Y$ \uline{définit un diviseur sur} $X-S$ \unsure{(transverse à $X/Y$)} d’où un fibré inversible, dont on constate que le \deleted{\unsure{diviseur}} \inserted{degré} est $+1$ [car on peut supposer $\unsure{Y|S}=\operatorname{Spec}k$, \unsure{le degré clair}].
+or on note qu’une section de $X-S$ sur $Y$ \uline{définit un diviseur sur} $X-S$ {\unsure{(transverse à $X/Y$)}} d’où un fibré inversible, dont on constate que le \deleted{{\unsure{diviseur}}} \inserted{degré} est $+1$ [car on peut supposer ${\unsure{Y|S}}=\operatorname{Spec}k$, {\unsure{le degré clair}}].
 % margin note written slanted, rising toward the text
-\margin{\unsure{vérifier|référence}??}
+\margin{{\unsure{vérifier|référence}}??}
 
 % L14--23
-II) Partons d’un $X$ \uline{propre} et \uline{simple} sur $\unsure{Y|S}$, dont les fibres sont de dim $1$, \deleted{\unsure{Soit} $X_i$} \unsure{(et abs! connexes)} (donc abs! irréductibles). Soit $S$ un sous-schéma \inserted{fermé} de \deleted{$X$ plat sur $Y$ et} ne contenant aucune fibre de $X/\unsure{Y|S}$, donc \uline{fini} sur $\unsure{Y|S}$, et plat sur $Y$. Soit $\unsure{\Xi|\mathscr I|\mathcal I}$ le faisceau d’idéaux définissant $Y$. Alors on prouve facilement que $\Xi$ est \uline{localement libre} [c’est purement local : un faisceau coh. sur $X$ plat rel. à $Y$ et qui \unsure{est inversible|est un module} dans fibres \inserted{\unsure{est}} est plat sur $X$.---]
+II) Partons d’un $X$ \uline{propre} et \uline{simple} sur ${\unsure{Y|S}}$, dont les fibres sont de dim $1$, \deleted{{\unsure{Soit}} $X_i$} {\unsure{(et abs! connexes)}} (donc abs! irréductibles). Soit $S$ un sous-schéma \inserted{fermé} de \deleted{$X$ plat sur $Y$ et} ne contenant aucune fibre de $X/{\unsure{Y|S}}$, donc \uline{fini} sur ${\unsure{Y|S}}$, et plat sur $Y$. Soit ${\unsure{\Xi|\mathscr I|\mathcal I}}$ le faisceau d’idéaux définissant $Y$. Alors on prouve facilement que $\Xi$ est \uline{localement libre} [c’est purement local : un faisceau coh. sur $X$ plat rel. à $Y$ et qui {\unsure{est inversible|est un module}} dans fibres \inserted{{\unsure{est}}} est plat sur $X$.---]
 % margin note written slanted, read after rotating clockwise
-\margin{\unsure{fibres abs! connexes est une condition} \unsure{peut-être} \uline{\unsure{vide}}.}
+\margin{{\unsure{fibres abs! connexes est une condition}} {\unsure{peut-être}} \uline{{\unsure{vide}}}.}
```
### K43-02_43_scan027.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -1,22 +1,22 @@
 \scanpage{27}
 % archive sheet number: 26
 % L1--4
-donc \deleted{\unsure{il s’ensuit}} \inserted{\unsure{il s’ensuit}} \deleted{\unsure{fac.}} \unsure{facile|facilement} que les $\unsure{\Xi|\mathscr I|\mathcal I}^{\unsure{-n|n|-m|m}}$ sont tels que $\unsure{\underline{\mathcal O}|\underline O}_X/\Xi^{-n}$ sont encore plats sur $Y$. Soit $\deleted{\unsure{Y}}S_n$ le sous-schéma de $X$ défini par $\Xi^{-n}$, et soit $X_n=X\amalg_{S_n}Y$ le $\deleted{S}Y$-schéma obtenu en ``\unsure{contractant} $S_n$ en $S$''.
+donc \deleted{{\unsure{il s’ensuit}}} \inserted{{\unsure{il s’ensuit}}} \deleted{{\unsure{fac.}}} {\unsure{facile|facilement}} que les ${\unsure{\Xi|\mathscr I|\mathcal I}}^{{\unsure{-n|n|-m|m}}}$ sont tels que ${\unsure{\underline{\mathcal O}|\underline O}}_X/\Xi^{-n}$ sont encore plats sur $Y$. Soit $\deleted{{\unsure{Y}}}S_n$ le sous-schéma de $X$ défini par $\Xi^{-n}$, et soit $X_n=X\amalg_{S_n}Y$ le $\deleted{S}Y$-schéma obtenu en ``{\unsure{contractant}} $S_n$ en $S$''.
 % L5--6
-\deleted{\unsure{Soit}} \deleted{\unsure{de sorte} $X_{\unsure{S|\xi}}=X-S$.} Donc $X_0=X$, et les $X_i$ forment un \uline{système} \uline{\deleted{projectif}\inserted{inductif}}.
+\deleted{{\unsure{Soit}}} \deleted{{\unsure{de sorte}} $X_{{\unsure{S|\xi}}}=X-S$.} Donc $X_0=X$, et les $X_i$ forment un \uline{système} \uline{\deleted{projectif}\inserted{inductif}}.
 % left, cancelled square and replacement square
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
-\deleted{\unsure{S}_n}\arrow[r,no head]\arrow[d]\arrow[dr,no head] \& \deleted X\arrow[d] \& S_n\arrow[r,"i_n"]\arrow[d,"f i_n"'] \& X\arrow[d,"p_n"]\\
+\deleted{{\unsure{S}}_n}\arrow[r,no head]\arrow[d]\arrow[dr,no head] \& \deleted X\arrow[d] \& S_n\arrow[r,"i_n"]\arrow[d,"f i_n"'] \& X\arrow[d,"p_n"]\\
 \deleted Y\arrow[r,no head] \& \deleted{X_n} \& Y\arrow[r,"\varepsilon_n"'] \& X_n
 \end{tikzcd}}
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
 \cdots\& X_2\arrow[l,no head]\&X_1\arrow[l]\&X_0=X\arrow[l]
 \end{tikzcd}}
 % L7--14
-Donc les $\unsure{\mathscr P|\mathcal P}_{X_n/S}$ forment un système \deleted{\uline{inductif}} projectif, d’où un pro-($S$-préschéma en groupes) noté $\mathscr P_{S,X/Y}$, et qui ne dépend que de la \uline{partie fermée} $S$ de $X/Y$, comme on constate facilement (du moins, si $Y$ est noethérien) --- cel\unsure{a} \unsure{résultera|résulte} d’ailleurs \unsure{de} la ``construction'' qu’on en \unsure{donnera|donne} plus bas.
+Donc les ${\unsure{\mathscr P|\mathcal P}}_{X_n/S}$ forment un système \deleted{\uline{inductif}} projectif, d’où un pro-($S$-préschéma en groupes) noté $\mathscr P_{S,X/Y}$, et qui ne dépend que de la \uline{partie fermée} $S$ de $X/Y$, comme on constate facilement (du moins, si $Y$ est noethérien) --- cel{\unsure{a}} {\unsure{résultera|résulte}} d’ailleurs {\unsure{de}} la ``construction'' qu’on en {\unsure{donnera|donne}} plus bas.
 
 % L15--17
 Les morphismes canoniques $X-S\longrightarrow\mathscr P^1_{X_n/Y}$ définissent à la limite un morphisme
 \[
-\boxed{\unsure{\varphi|\phi}_S:X-S\longrightarrow\mathscr P^1_{S,X/Y}\unsure{\subset|\in}\mathscr P_{S,X/Y}}.
+\boxed{{\unsure{\varphi|\phi}}_S:X-S\longrightarrow\mathscr P^1_{S,X/Y}{\unsure{\subset|\in}}\mathscr P_{S,X/Y}}.
 \]
```
### K43-02_43_scan028.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -2,11 +2,11 @@
 % archive sheet number: 27
 % L1--7; vertical emphasis stroke beside the statement
 \noindent\vrule\hspace{.6em}\begin{minipage}{.93\linewidth}
-\uline{Théorème} Soit $G$ un $Y$-schéma en groupes \inserted{\unsure{commu.}} de type fini \deleted{sur $\unsure{Y|S}$}, et $P^1$ un fibré principal homogène sous $G$ [devenant trivial par extension fid. plate quasi-compacte\unsure{---}], d’où un schéma en groupes $\mathbb Z$-augmenté $P$, avec $P^{(1)}=P^1$, $P^{(0)}=G$. Considérons l’application canonique $u\unsure{\longrightarrow|\mapsto}u\circ\unsure{\varphi|\phi}_S$
+\uline{Théorème} Soit $G$ un $Y$-schéma en groupes \inserted{{\unsure{commu.}}} de type fini \deleted{sur ${\unsure{Y|S}}$}, et $P^1$ un fibré principal homogène sous $G$ [devenant trivial par extension fid. plate quasi-compacte{\unsure{---}}], d’où un schéma en groupes $\mathbb Z$-augmenté $P$, avec $P^{(1)}=P^1$, $P^{(0)}=G$. Considérons l’application canonique $u{\unsure{\longrightarrow|\mapsto}}u\circ{\unsure{\varphi|\phi}}_S$
 \end{minipage}\par
 \[
 \operatorname{Hom}_{\substack{Y\text{-schémas en groupes}\\\mathbb Z\text{-augmentés}}}
-(\unsure{\mathscr P|\mathcal P}_{S,X/Y},P)\longrightarrow\operatorname{Hom}_Y(X-S,P^1)
+({\unsure{\mathscr P|\mathcal P}}_{S,X/Y},P)\longrightarrow\operatorname{Hom}_Y(X-S,P^1)
 \]
 % L8--9
 \uline{Cette application est bijective}.
@@ -21,7 +21,7 @@
 % L11--15; vertical emphasis stroke beside lower paragraph
 \uline{Corollaire 2}
 \noindent\vrule\hspace{.6em}\begin{minipage}{.93\linewidth}
-\inserted{Considérons} Le \deleted{\unsure{homomorphisme de}} \inserted{foncteur} $\varphi_S^*$, de la catégorie des schémas \uline{extensions} \inserted{(en groupes commutatifs)} de $P_{S,X/Y}$ par des $Y$-schémas en groupes commutatifs de type fini $G$ sur $Y$, dans la catégorie \deleted{\unsure{qui}}
+\inserted{Considérons} Le \deleted{{\unsure{homomorphisme de}}} \inserted{foncteur} $\varphi_S^*$, de la catégorie des schémas \uline{extensions} \inserted{(en groupes commutatifs)} de $P_{S,X/Y}$ par des $Y$-schémas en groupes commutatifs de type fini $G$ sur $Y$, dans la catégorie \deleted{{\unsure{qui}}}
 \end{minipage}\par
 % margin note written slanted, read after rotating clockwise
-\margin{il faut faire \unsure{attention aux définitions} de ``fibré'' et ``extension'' ? $G$ plat sur $\unsure{Y|S}$??}
+\margin{il faut faire {\unsure{attention aux définitions}} de ``fibré'' et ``extension'' ? $G$ plat sur ${\unsure{Y|S}}$??}
```
### K43-02_43_scan029.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -6,21 +6,21 @@
 \end{minipage}\par
 
 % L4--9
-Soient $Q,Q'$ deux telles extensions, de groupes $G,G'$. Un hom. de $Q'$ en $\unsure{Q'|Q}$ est \inserted{un couple formé d’un hom. $u:G'\longrightarrow G$ et d’} un\unsure{e} \deleted{isom. de $Q''=Q\times_{G'}G$ avec} \deleted{\unsure{élément de} $\operatorname{Hom}_{\unsure{S,u}}(\unsure{Q'|G'},Q)$, \unsure{avec}} \deleted{qui est un fibré} \inserted{\unsure{isom. de} $Q''=\unsure{Q'\times_{G'}G|Q\times_{G'}G}$} $Q'$ \deleted{\unsure{ou}} (on \unsure{entend} par extension de groupe \uline{donné} $G'$). Il y en a \unsure{ssi} $\unsure{Q'|Q}$ et $Q''$ sont isomorphes. Or
+Soient $Q,Q'$ deux telles extensions, de groupes $G,G'$. Un hom. de $Q'$ en ${\unsure{Q'|Q}}$ est \inserted{un couple formé d’un hom. $u:G'\longrightarrow G$ et d’} un{\unsure{e}} \deleted{isom. de $Q''=Q\times_{G'}G$ avec} \deleted{{\unsure{élément de}} $\operatorname{Hom}_{{\unsure{S,u}}}({\unsure{Q'|G'}},Q)$, {\unsure{avec}}} \deleted{qui est un fibré} \inserted{{\unsure{isom. de}} $Q''={\unsure{Q'\times_{G'}G|Q\times_{G'}G}}$} $Q'$ \deleted{{\unsure{ou}}} (on {\unsure{entend}} par extension de groupe \uline{donné} $G'$). Il y en a {\unsure{ssi}} ${\unsure{Q'|Q}}$ et $Q''$ sont isomorphes. Or
 % margin note written slanted, rising to the right
-\margin{il faut \unsure{pouvoir} définir les fibrés associés, Attention!}
+\margin{il faut {\unsure{pouvoir}} définir les fibrés associés, Attention!}
 % left-middle diagram
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
 \&Q\arrow[d,no head]\&Q''\\
-X-S\arrow[ur,dashed]\arrow[r]\&\unsure{\mathscr P|\mathcal P}_{S,X/S}
+X-S\arrow[ur,dashed]\arrow[r]\&{\unsure{\mathscr P|\mathcal P}}_{S,X/S}
 \end{tikzcd}}
 % L10 displayed, overwritten letters retained
 \[
-\unsure{\operatorname{Ext}|\operatorname{Ext}^1}(\unsure{\mathscr P|\mathcal P}_{\unsure{S}},G)\longrightarrow\deleted{\unsure{\operatorname{Ext}}}\unsure{H|\mathrm H}^1(X-S,G)
+{\unsure{\operatorname{Ext}|\operatorname{Ext}^1}}({\unsure{\mathscr P|\mathcal P}}_{{\unsure{S}}},G)\longrightarrow\deleted{{\unsure{\operatorname{Ext}}}}{\unsure{H|\mathrm H}}^1(X-S,G)
 \]
 % L11--17
-étant un hom. de groupes, pour prouver qu’il est injectif (i.e. $Q$ et $Q'$ isom. ssi $\unsure{\varphi|\phi}^*(Q)$ et $\varphi^*(Q'')$ le sont) on est ramené à prouver que le noyau est nul, i.e. que si $\varphi^*(Q)$ est trivial, alors $Q$ l’est. Cela résulte \deleted{facilement} \inserted{\unsure{aussitôt}} du th. de Rosenlicht.
+étant un hom. de groupes, pour prouver qu’il est injectif (i.e. $Q$ et $Q'$ isom. ssi ${\unsure{\varphi|\phi}}^*(Q)$ et $\varphi^*(Q'')$ le sont) on est ramené à prouver que le noyau est nul, i.e. que si $\varphi^*(Q)$ est trivial, alors $Q$ l’est. Cela résulte \deleted{facilement} \inserted{{\unsure{aussitôt}}} du th. de Rosenlicht.
 % margin note written slanted, read in its own direction
-\margin{Attention, il faut bien préciser les définitions \unsure{d’opérations d’addition} de fibrés etc}
+\margin{Attention, il faut bien préciser les définitions {\unsure{d’opérations d’addition}} de fibrés etc}
 % L18, unfinished sentence at foot
-Comme \inserted{$\varphi^*$ est fidèle car} (\unsure{le groupe étant donné}), \deleted{\unsure{est}} \unsure{on|en}
+Comme \inserted{$\varphi^*$ est fidèle car} ({\unsure{le groupe étant donné}}), \deleted{{\unsure{est}}} {\unsure{on|en}}
```
### K43-02_43_scan030.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -3,14 +3,14 @@
 % L1--3, continuation
 est ainsi ramené à prouver que
 \[
-\operatorname{Hom}(Q,Q)\longrightarrow\operatorname{Hom}(\unsure{\varphi|\phi}^*(Q),\varphi^*(Q))
+\operatorname{Hom}(Q,Q)\longrightarrow\operatorname{Hom}({\unsure{\varphi|\phi}}^*(Q),\varphi^*(Q))
 \]
-est bijectif. Or les deux s’identifient \unsure{resp!|resp.} à
+est bijectif. Or les deux s’identifient {\unsure{resp!|resp.}} à
 % L4--5
 \[
-\operatorname{Hom}_{\substack{\text{grps}\\\text{sur }\unsure{Y|S}}}(\unsure{\mathscr P|\mathcal P}_S,G)
+\operatorname{Hom}_{\substack{\text{grps}\\\text{sur }{\unsure{Y|S}}}}({\unsure{\mathscr P|\mathcal P}}_S,G)
 \quad\text{et}\quad
-\deleted{\unsure{E|H}}\operatorname{Hom}_Y(X-S,G)
+\deleted{{\unsure{E|H}}}\operatorname{Hom}_Y(X-S,G)
 \]
 donc sont isomorphes.
 
@@ -21,9 +21,9 @@
 \uline{Corollaire 3} Si $G$ est un schéma en groupes commu. de type fini sur $Y$, on a un hom. canonique \uuline{injectif}
 \end{minipage}\par
 \[
-\operatorname{Ext}_{\substack{\text{schémas en groupes}\\\text{sur }\unsure{Y|S}}}(\mathscr P_{S,X/S},G)\longrightarrow H^1(X-S,G)
+\operatorname{Ext}_{\substack{\text{schémas en groupes}\\\text{sur }{\unsure{Y|S}}}}(\mathscr P_{S,X/S},G)\longrightarrow H^1(X-S,G)
 \]
 % margin note written slanted
-\margin{\unsure{préciser la signification}\unsure{...}}
+\margin{{\unsure{préciser la signification}}{\unsure{...}}}
 % L10--15
-Il \uline{semble} que c’est \uline{\unsure{bijectif|surjectif}} chaque fois que $S\longrightarrow Y$ est \uline{surjectif}, i.e. que les fibres de $X/Y$ sont non propres, donc \uline{affines}. Dans le cas où $S=\varnothing$, $G=G_m$, on ne \unsure{sera|serait} déjà pas surjectif.
+Il \uline{semble} que c’est \uline{{\unsure{bijectif|surjectif}}} chaque fois que $S\longrightarrow Y$ est \uline{surjectif}, i.e. que les fibres de $X/Y$ sont non propres, donc \uline{affines}. Dans le cas où $S=\varnothing$, $G=G_m$, on ne {\unsure{sera|serait}} déjà pas surjectif.
```
### K43-02_43_scan031.tex

```diff
--- before syntax grouping
+++ after syntax grouping
@@ -1,10 +1,10 @@
 \scanpage{31}
 % archive sheet number: 30
 % L1--7
-Il semble néanmoins que dans le cas général, pour prouver qu’un fibré principal $E$ sur $X-S$ provient d’une \deleted{fibré principal} extension de $\unsure{\mathscr P|\mathcal P}_S$ par $G$, il suffit (utilisant \unsure{la théorie|le théorème} de la descente) de le vérifier en \unsure{remplaçant} $S$ par les spectres des \uline{complétés} de ses anneaux locaux.
+Il semble néanmoins que dans le cas général, pour prouver qu’un fibré principal $E$ sur $X-S$ provient d’une \deleted{fibré principal} extension de ${\unsure{\mathscr P|\mathcal P}}_S$ par $G$, il suffit (utilisant {\unsure{la théorie|le théorème}} de la descente) de le vérifier en {\unsure{remplaçant}} $S$ par les spectres des \uline{complétés} de ses anneaux locaux.
 % L8--10
-De plus, utilisant la géométrie formelle [lorsque $G$ est bien plongé dans le groupe \deleted{\unsure{H|\mathrm H}} linéaire] on est ramené à le vérifier \uline{formellement}.
+De plus, utilisant la géométrie formelle [lorsque $G$ est bien plongé dans le groupe \deleted{{\unsure{H|\mathrm H}}} linéaire] on est ramené à le vérifier \uline{formellement}.
 % L11--14
-Cela revient au cas d’un \unsure{anneau} de base \unsure{Artinien}. Travaillant de proche en proche, on est ramené à le vérifier \unsure{pour les courbes} \uline{\unsure{sur|pour}} les corps résiduels de $S$.
+Cela revient au cas d’un {\unsure{anneau}} de base {\unsure{Artinien}}. Travaillant de proche en proche, on est ramené à le vérifier {\unsure{pour les courbes}} \uline{{\unsure{sur|pour}}} les corps résiduels de $S$.
 % L15--19
-Utilisant à nouveau la descente on serait \unsure{amené|ramené} à le vérifier à nouveau sur les clôtures algébriques des corps résiduels\unsure{...---} On peut sans doute s’en tirer plus \unsure{astucieusement}.
+Utilisant à nouveau la descente on serait {\unsure{amené|ramené}} à le vérifier à nouveau sur les clôtures algébriques des corps résiduels{\unsure{...---}} On peut sans doute s’en tirer plus {\unsure{astucieusement}}.
```

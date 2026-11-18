# Second reading audit

All timestamps are actual UTC checkpoints. Each second reading began with the three supplied thirds, before opening that page’s first-pass source. The pre-comparison observations below were recorded before that opening. Additional enlarged or rotated views are described in the checks. Later reconciliation sessions are separately dated; they do not extend the original audit times retrospectively.

The first attempted audit of scan 158 was interrupted by loss of the workspace execution environment. It has no completed end time. The resumed audit restarted from all three crops; the unavailable interval is not counted as reading time.

No OCR, text recognition, external source, or LaTeX compilation was used. The inventory was rebuilt after all reading and syntax changes. Inline and displayed formulas below are the final source forms checked, including cancellations; diagram blocks list every object and arrow label.

## Scan 149

Start: **2026-11-17T20:48:28.240526+00:00**. End: **2026-11-17T20:49:54.915243+00:00**.

Crop observations recorded: 2026-11-17T20:48:52.621319+00:00.

From the crops, before opening the page file: “Application” (singular); “th.”; “Lefschetz local”; “Cf.”; “commentaires”; “hypothèses”; “locaux”; “loc. de type fini”; “str. local hensélien” (last word compressed); “sache” after que l'on; “à titre d'hypothèse” cancelled; “gén. stricte”; “voisinage”; “conditions”; “imposant”; “conclure”; “Notons”; “déjà”; “i.e.”; “Par suite”; “condition”; “aussitôt”; “Théorème” replacing Proposition; “n'importe”; “générisation”. Accents on déjà, gén./générisation, Théorème and hypothèses read as acute/grave where visible. The short reduced words before condition and after On are uncertain. XIV in heading has an overwritten middle stroke. No date. Own number V.21; archive 148.

### Checks

Read s1, s2 and s3 line by line, then enlarged 5.0/5.1, the recurrence paragraph and the start of 5.2. Compared all displayed and inline expressions listed below: f:X→S; x∈X0; m′∈Z; every Phi stalk, x/x′ and bar; the unprimed m in (*); the cancelled H comparison, its strict i<m′; H_x^i, tilde X and the h-directed limit; the ≥ m′+1 depth bound; dim O and r; Z and X0−Z. Every cohomological exponent is a dotted i without a descender; none was normalized to j. Read the cancellation strokes across the first hypothesis, On, the cancelled display and label, short reduced phrases, and the Proposition/Théorème correction. The added n'importe is placed before Supposons, following its loop. No separate margin note or diagram. Phi/varphi, nu/v, O alphabets and h/k remain marked. Z is double-stroked. The disputed word read initially as voisinage remains an alternative to récurrence, rather than a confident contextual repair. The numerical reference 3.3/3.2 is now marked. The visibly missing closing parenthesis in prof ét_x(X(h) is retained.

### Every inline formula

1. `\overline{\underline{\unsure{\mathrm{XIV}\|\mathrm{XV}}}}`
2. `f:X\longrightarrow S`
3. `S`
4. `x\in X_0`
5. `m'\in\mathbb{Z}`
6. `x`
7. `X_0`
8. `i\leq m'`
9. `H^i_x(X(h),\Lambda_\nu)=0`
10. `i\leq m'`
11. `\forall h`
12. `\dim{\unsure{\mathscr{O}\|\mathcal{O}}}_{X_0,x}=r`
13. `Z`
14. `X_0`
15. `\forall`
16. `x'`
17. `x`
18. `X_0`
19. `x`
20. `X_0-Z`

### Every display

Display 1:

```latex
({\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}})_{\bar{x}'}=0
\quad\text{pour tt \unsure{gén. stricte} de $x$ dans $X_0$, et $i\leq m'$.}
\tag*{\tikz[baseline=(n.base)]{\node[inner sep=1pt] (n) {5.1.1};\draw (n.center) ellipse (0.62cm and 0.22cm);}}
```

Display 2:

```latex
(\underline{\Phi}^{i})_{\bar{x}}=0\quad\text{si}\quad i\leq m.
\tag*{(*)}
```

Display 3:

```latex
\deleted{H^i(\bar{V},\Lambda_\nu)\xrightarrow{\sim}H^i(\unsure{\widetilde{X}_{\bar{\eta}}|\widetilde{X}_{\bar{y}}},\Lambda_\nu)\quad\text{si}\quad i<m'}
\tag*{\deleted{(5.1.1)}}
```

Display 4:

```latex
(\underline{\Phi}^i_\nu)_{\bar{x}}=H^i_x(\widetilde{X},\Lambda_\nu)
=\varinjlim_{\unsure{h|k}} H^i_x(X(h),\Lambda_\nu)
\quad\text{pour}\quad i\leq m'.
\tag*{(5.1.2)}
```

Display 5:

```latex
\operatorname{prof\,ét}_x(X(h)\geq m'+1\quad\text{pour}\quad\forall\unsure{k|h}.
\tag*{\tikz[baseline=(n.base)]{\node[inner sep=1pt] (n) {5.1.3};\draw (n.center) ellipse (0.62cm and 0.22cm);}}
```

Display 6:

```latex
(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\text{si}\quad i\leq m',
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

- Source line 11: `derline{\varphi}}}^i_{\unsure{\nu\|v}})_{\b`
- Source line 11: `rline{\varphi}}}^i_{\unsure{\nu\|v}})_{\bar{x}'}=0 \quad\t`
- Source line 18: ` (\underline{\Phi}^{i})_{\bar{x}}=0\quad\tex`
- Source line 24: `ique \[ \deleted{H^i(\bar{V},\Lambda_\nu)\`
- Source line 24: `xrightarrow{\sim}H^i(\unsure{\widetilde{X}`
- Source line 29: ` (\underline{\Phi}^i_\nu)_{\bar{x}}=H^i_x(`
- Source line 29: `\underline{\Phi}^i_\nu)_{\bar{x}}=H^i_x(\wid`
- Source line 29: `i_\nu)_{\bar{x}}=H^i_x(\widetilde{X},\Lamb`
- Source line 29: `\nu)_{\bar{x}}=H^i_x(\widetilde{X},\Lambda`
- Source line 30: `m_{\unsure{h\|k}} H^i_x(X(h),\Lambda_\nu) \`
- Source line 30: `{\unsure{h\|k}} H^i_x(X(h),\Lambda_\nu) \qu`
- Source line 35: ` de la relation $H^i_x(X(h),\Lambda_\nu)=0`
- Source line 35: `e la relation $H^i_x(X(h),\Lambda_\nu)=0$ `
- Source line 47: ` (\underline{\Phi}^i_\nu)_{\bar{x}'}=0\qua`
- Source line 47: `\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\te`

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

- Source line 43: `Théorème`
- Source line 43: `\unsure{n'importe}.`

**deleted**

- Source line 9: `(à titre d'hypothèse`
- Source line 16: `On`
- Source line 16: `\unsure{un}`
- Source line 24: `H^i(\bar{V},\Lambda_\nu)\xrightarrow{\sim}H^i(\unsure{\widetilde{X}_{\bar{\eta}}\|\widetilde{X}_{\bar{y}}},\Lambda_\nu)\quad\text{si}\quad i<m'`
- Source line 25: `(5.1.1)`
- Source line 27: `\unsure{en vertu de}`
- Source line 35: `\unsure{si on}`
- Source line 35: `\unsure{équivaut}`
- Source line 35: `\unsure{(5.1.3)}`
- Source line 41: `\illegible{2}`
- Source line 41: `\unsure{en}`
- Source line 43: `\unsure{Proposition}`
- Source line 43: `pour`
- Source line 45: `\unsure{distinct de $x$, on}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -5,7 +5,7 @@
 
 5. \uline{Application des th. de Lefschetz local} (SGA 2 \unsure{XIV|XV} 4).
 
-5.0. Cf. les commentaires dans 3.3. pour les hypothèses faites quand nous \unsure{utiliserons} les théorèmes de Lefschetz locaux.
+5.0. Cf. les commentaires dans \unsure{3.3|3.2}. pour les hypothèses faites quand nous \unsure{utiliserons} les théorèmes de Lefschetz locaux.
 
 5.1. Soit $f:X\longrightarrow S$ loc. de type fini, $S$ str. loc. \unsure{hensélien}, et soit $x\in X_0$. Soit $m'\in\mathbb{Z}$ et supposons que l'on \unsure{sache} \deleted{(à titre d'hypothèse}
 \[
@@ -14,7 +14,7 @@
 \tag*{(5.1.1)}
 \]
 
-\deleted{On} Nous \unsure{considérons} cette hypothèse comme une hypothèse de récurrence, et nous proposons de donner des conditions moyennant \deleted{\unsure{un}} \unsure{quoi} on conclura
+\deleted{On} Nous \unsure{considérons} cette hypothèse comme une hypothèse de \unsure{récurrence|voisinage}, et nous proposons de donner des conditions moyennant \deleted{\unsure{un}} \unsure{quoi} on conclura
 \[
 (\underline{\Phi}^{i})_{\bar{x}}=0\quad\text{si}\quad i\leq m.
 \tag*{(*)}
```

### Supplementary reading

Start: 2026-11-17T23:52:58.844412+00:00. End: 2026-11-17T23:54:35.516178+00:00.

All three thirds re-read again, plus two prose enlargements and fresh highest-zoom cancellation. Heading Roman numeral has upper/lower bars. Labels 5.1.1 and 5.1.3 are oval-enclosed, unlike ordinary parenthesized labels. Cancelled three-word trace above 5.1.2 permits en vertu de, at low confidence. Bottom cancellation remains physically unreadable.

```diff
--- before
+++ after
@@ -3,7 +3,7 @@
 \mspage{V.21}
 % archive sheet number: 148
 
-5. \uline{Application des th. de Lefschetz local} (SGA 2 \unsure{XIV|XV} 4).
+5. \uline{Application des th. de Lefschetz local} (SGA 2 $\overline{\underline{\unsure{\mathrm{XIV}|\mathrm{XV}}}}$ 4).
 
 5.0. Cf. les commentaires dans \unsure{3.3|3.2}. pour les hypothèses faites quand nous \unsure{utiliserons} les théorèmes de Lefschetz locaux.
 
@@ -11,7 +11,7 @@
 \[
 (\unsure{\underline{\Phi}|\underline{\varphi}}^i_{\unsure{\nu|v}})_{\bar{x}'}=0
 \quad\text{pour tt \unsure{gén. stricte} de $x$ dans $X_0$, et $i\leq m'$.}
-\tag*{(5.1.1)}
+\tag*{\tikz[baseline=(n.base)]{\node[inner sep=1pt] (n) {5.1.1};\draw (n.center) ellipse (0.62cm and 0.22cm);}}
 \]
 
 \deleted{On} Nous \unsure{considérons} cette hypothèse comme une hypothèse de \unsure{récurrence|voisinage}, et nous proposons de donner des conditions moyennant \deleted{\unsure{un}} \unsure{quoi} on conclura
@@ -25,7 +25,7 @@
 \deleted{H^i(\bar{V},\Lambda_\nu)\xrightarrow{\sim}H^i(\unsure{\widetilde{X}_{\bar{\eta}}|\widetilde{X}_{\bar{y}}},\Lambda_\nu)\quad\text{si}\quad i<m'}
 \tag*{\deleted{(5.1.1)}}
 \]
-\deleted{\illegible{3}}
+\deleted{\unsure{en vertu de}}
 \[
 (\underline{\Phi}^i_\nu)_{\bar{x}}=H^i_x(\widetilde{X},\Lambda_\nu)
 =\varinjlim_{\unsure{h|k}} H^i_x(X(h),\Lambda_\nu)
@@ -36,7 +36,7 @@
 Par suite, \deleted{\unsure{si on}} la relation (*) \deleted{\unsure{équivaut}} \unsure{résultera} de la relation $H^i_x(X(h),\Lambda_\nu)=0$ pour $i\leq m'$, $\forall h$, i.e. \deleted{\unsure{(5.1.3)}} de la relation
 \[
 \operatorname{prof\,ét}_x(X(h)\geq m'+1\quad\text{pour}\quad\forall\unsure{k|h}.
-\tag*{(5.1.3)}
+\tag*{\tikz[baseline=(n.base)]{\node[inner sep=1pt] (n) {5.1.3};\draw (n.center) ellipse (0.62cm and 0.22cm);}}
 \]
 
 \unsure{Donc} On \deleted{\illegible{2}} \deleted{\unsure{en}} en conclut aussitôt, par récurrence sur $\dim\unsure{\mathscr{O}|\mathcal{O}}_{X_0,x}=r$ :
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -1,4 +1,3 @@
-\cotefile{34}
 \scanpage{149}
 \mspage{V.21}
 % archive sheet number: 148
@@ -9,7 +8,7 @@
 
 5.1. Soit $f:X\longrightarrow S$ loc. de type fini, $S$ str. loc. \unsure{hensélien}, et soit $x\in X_0$. Soit $m'\in\mathbb{Z}$ et supposons que l'on \unsure{sache} \deleted{(à titre d'hypothèse}
 \[
-(\unsure{\underline{\Phi}|\underline{\varphi}}^i_{\unsure{\nu|v}})_{\bar{x}'}=0
+({\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}})_{\bar{x}'}=0
 \quad\text{pour tt \unsure{gén. stricte} de $x$ dans $X_0$, et $i\leq m'$.}
 \tag*{\tikz[baseline=(n.base)]{\node[inner sep=1pt] (n) {5.1.1};\draw (n.center) ellipse (0.62cm and 0.22cm);}}
 \]
@@ -39,7 +38,7 @@
 \tag*{\tikz[baseline=(n.base)]{\node[inner sep=1pt] (n) {5.1.3};\draw (n.center) ellipse (0.62cm and 0.22cm);}}
 \]
 
-\unsure{Donc} On \deleted{\illegible{2}} \deleted{\unsure{en}} en conclut aussitôt, par récurrence sur $\dim\unsure{\mathscr{O}|\mathcal{O}}_{X_0,x}=r$ :
+\unsure{Donc} On \deleted{\illegible{2}} \deleted{\unsure{en}} en conclut aussitôt, par récurrence sur $\dim{\unsure{\mathscr{O}|\mathcal{O}}}_{X_0,x}=r$ :
 
 \uline{\deleted{\unsure{Proposition}}\inserted{Théorème} 5.2.} Soit $Z$ une partie de $X_0$, \inserted{\unsure{n'importe}.} Supposons que : \deleted{pour}
```

## Scan 150

Start: **2026-11-17T20:49:54.952331+00:00**. End: **2026-11-17T20:51:37.308230+00:00**.

Crop observations recorded: 2026-11-17T20:50:21.913811+00:00.

Before opening: “c'est le cas si on suppose p.ex.”; “l'ens des pts”; “en lesquels”; “générisation”; “entier” added above a crossed word before h; “Alors on a”; “i.e.”; “loc.”; “acyclique”; “donc si f est propre”; “un isom si”; “mon. si”; “Corollaire”; “Supposons” struck, “Soit”; “un entier”; “posons”; “Supposons que l'on ait”; “Pour toute générisation”; “Résulte formellement”; “en y faisant”; “la condition a)”; “satisfaite”; “en vertu de”; “la condition b) résultant de”. Broad cancellation crosses the complete lower draft. Accents on générisation, Résulte and résultant. Tiny symbols in the depth formula and cancelled stalk bounds remain unclear; m′ has a prime in the live top half.

### Checks

Full crop reading plus close examination of top, overwritten sup/depth lines and lower cancellations. Checked every expression listed below, including all expressions inside the cancelled draft: depth at barred x′, X(h), m′+1; Phi at x without an added bar; the heavy sign in m′[cancelled sign]1; H^i(X0) dash H^i(Xbar eta), with strict i<m′ and mon. at i=m′; d as sup, closure braces and generisation restriction; the earlier m-line; 1+m and both h-indexed operations; both competing Phi lines and their m−d bound; X−Z and x in closure; depth conditions on X0 and X_eta; added +1; the cancelled local acyclicity sentence. All i exponents are dotted short stems, not j. The entire lower draft is cancelled, including its last incomplete sentence; internal deletions remain nested. The black square between m′ and 1 has been treated as a cancellation, since it has no separable live sign. Sup/inf, depth superscripts and the cropped-over letters remain low-confidence readings. No diagram or separate margin. The added entier and m are anchored at the crossed words. First eta/y doubt is now explicit. Read the final prose again; formellement is preferred to facilement, with both retained. No confident repair of the mathematical bounds.

### Every inline formula

1. `Z`
2. `X_0`
3. `f`
4. `x'`
5. `x`
6. `Z`
7. `\unsure{h\|k}`
8. `f`
9. `(m'\deleted{\unsure{-\|+}}1)`
10. `x`
11. `\{\ell\}`
12. `f`
13. `i<m'`
14. `i=m'`
15. `Z`
16. `X_0`
17. `m`
18. `x'`
19. `x`
20. `X_0`
21. `f`
22. `(m-d)`
23. `x`
24. `\{\ell\}`
25. `m'=m-d`

### Every display

Display 1:

```latex
\operatorname{prof\,ét}_{\bar{x}'}(X(h))\geq m'+1,
```

Display 2:

```latex
({\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}})_x\unsure{=}0\quad\text{si}\quad i\leq m'
\tag*{(5.2.1)}
```

Display 3:

```latex
H^i(X_0,\Lambda_\nu)\unsure{-|\longrightarrow}H^i(X_{\bar{\unsure{\eta|y}}},\Lambda_\nu)
\quad\text{un isom si $i<m'$, mon. si $i=m'$.}
\tag*{(5.2.2)}
```

Display 4:

```latex
\deleted{\left\{\begin{aligned}
d&=\sup_{\substack{x'\in Z\,\deleted{\unsure{\cap X_{\bar{x}}}}\\x'\text{ générise }x}}\dim\overline{\{x'\}},\\
\deleted{m}&\deleted{=\unsure{\operatorname{prof\,ét}^{*}_Z}}\\
1+m&=\sup_h\unsure{\operatorname{prof\,ét}^{*}_Z(X(h))}\;\unsure{\in|\text{et}}\;{\unsure{\sup|\inf}}_h\unsure{\operatorname{prof\,ét}^{*}(X(h))}-\dim\overline{\{\unsure{x'|x}\}}
\end{aligned}\right.}
\tag*{\deleted{\unsure{(5.3.1)}}}
```

Display 5:

```latex
\deleted{\deleted{(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\text{si}\quad i\leq}}
```

Display 6:

```latex
\deleted{\text{a)}\quad(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\text{si}\quad i\unsure{\leq|<}m-d\deleted{\unsure{+1}},\quad\text{pour }x'\in X-Z,\quad x\in\overline{\{x'\}},}
\tag*{\deleted{\deleted{(5.3.2)}}}
```

Display 7:

```latex
\deleted{\deleted{(\underline{\Phi}_{\unsure{\bar{x}|x}})=0\quad\text{si}\quad i\leq m-d}}
```

Display 8:

```latex
\deleted{\operatorname{prof\,ét}^{*}_{x'}(X_0)\geq m\inserted{+1}\quad\text{si }x'\in X_0\quad(\text{resp. }\operatorname{prof\,ét}^{*}_{x'}(X_\eta)=0\quad\text{si }x'\in X_\eta).}
\tag*{\deleted{(5.3.3)}}
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

- Source line 14: `derline{\varphi}}}^i_{\unsure{\nu\|v}})_x\u`
- Source line 14: `rline{\varphi}}}^i_{\unsure{\nu\|v}})_x\unsure{=}0\quad\te`
- Source line 19: ` propre, on a \[ H^i(X_0,\Lambda_\nu)\unsu`
- Source line 19: `\|\longrightarrow}H^i(X_{\bar{\unsure{\eta\|`
- Source line 37: `{(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\qua`
- Source line 37: `\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\te`
- Source line 40: `d(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\qua`
- Source line 40: `\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\te`

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

- Source line 7: `entier`
- Source line 25: `$m$`
- Source line 51: `+1`

**deleted**

- Source line 7: `\unsure{soit}`
- Source line 7: `\unsure{entier}`
- Source line 11: `(ce qui est le cas`
- Source line 17: `\unsure{-\|+}`
- Source line 17: `\unsure{les}`
- Source line 25: `\uline{Corollaire} 5.3. \deleted{Supposons} Soit $Z$ une partie de $X_0$, \deleted{\unsure{soit}}\inserted{$m$} un entier, \deleted{Supposons} posons`
- Source line 25: `Supposons`
- Source line 25: `\unsure{soit}`
- Source line 25: `Supposons`
- Source line 27: `\left\{\begin{aligned} d&=\sup_{\substack{x'\in Z\,\deleted{\unsure{\cap X_{\bar{x}}}}\\x'\text{ générise }x}}\dim\overline{\{x'\}},\\ \deleted{m}&\deleted{=\unsure{\operatorname{prof\,ét}^{*}_Z}}\\ 1+m&=\sup_h\unsure{\operatorname{prof\,ét}^{*}_Z(X(h))}\;\unsure{\in\|\text{et}}\;{\unsure{\sup\|\inf}}_h\unsure{\operatorname{prof\,ét}^{*}(X(h))}-\dim\overline{\{\unsure{x'\|x}\}} \end{aligned}\right.`
- Source line 28: `\unsure{\cap X_{\bar{x}}}`
- Source line 29: `m`
- Source line 29: `=\unsure{\operatorname{prof\,ét}^{*}_Z}`
- Source line 32: `\unsure{(5.3.1)}`
- Source line 35: `\deleted{Alors on a} Supposons que l'on ait`
- Source line 35: `Alors on a`
- Source line 37: `\deleted{(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\text{si}\quad i\leq}`
- Source line 37: `(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\text{si}\quad i\leq`
- Source line 40: `\text{a)}\quad(\underline{\Phi}^i_\nu)_{\bar{x}'}=0\quad\text{si}\quad i\unsure{\leq\|<}m-d\deleted{\unsure{+1}},\quad\text{pour }x'\in X-Z,\quad x\in\overline{\{x'\}},`
- Source line 40: `\unsure{+1}`
- Source line 41: `\deleted{(5.3.2)}`
- Source line 41: `(5.3.2)`
- Source line 44: `\deleted{Alors on a aussi}`
- Source line 44: `Alors on a aussi`
- Source line 46: `b) Pour toute générisation $x'$ de $x$ dans $X_0$, on a`
- Source line 48: `\deleted{(\underline{\Phi}_{\unsure{\bar{x}\|x}})=0\quad\text{si}\quad i\leq m-d}`
- Source line 48: `(\underline{\Phi}_{\unsure{\bar{x}\|x}})=0\quad\text{si}\quad i\leq m-d`
- Source line 51: `\operatorname{prof\,ét}^{*}_{x'}(X_0)\geq m\inserted{+1}\quad\text{si }x'\in X_0\quad(\text{resp. }\operatorname{prof\,ét}^{*}_{x'}(X_\eta)=0\quad\text{si }x'\in X_\eta).`
- Source line 52: `(5.3.3)`
- Source line 55: `\deleted{i.e. $f$ est localement $(m-d)$-acyclique en $x$, pour $\{\ell\}$.}`
- Source line 55: `i.e. $f$ est localement $(m-d)$-acyclique en $x$, pour $\{\ell\}$.`
- Source line 57: `Alors`
- Source line 59: `Résulte \unsure{formellement\|facilement} de 5.2, en y faisant $m'=m-d$, la condition a) de 5.2 est satisfaite \unsure{par\|en} vertu de (5.3.2), et la condition b) résultant de`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -4,7 +4,7 @@
 
 (c'est le cas si on suppose p.ex. que $Z$ est l'ens des \unsure{pts} de $X_0$ en lesquels $f$ n'est pas lisse).
 
-b) Pour toute générisation $x'$ de $x$ dans $Z$, \deleted{\unsure{soit}} \unsure{on} et tt \deleted{\unsure{entier}}\inserted{entier} $\unsure{h|k}$, on a
+b) Pour toute générisation $x'$ de $x$ dans $Z$, \deleted{\unsure{soit}} \unsure{on|ou} et tt \deleted{\unsure{entier}}\inserted{entier} $\unsure{h|k}$, on a
 \[
 \operatorname{prof\,ét}_{\bar{x}'}(X(h))\geq m'+1,
 \]
@@ -14,9 +14,9 @@
 (\unsure{\underline{\Phi}|\underline{\varphi}}^i_{\unsure{\nu|v}})_x\unsure{=}0\quad\text{si}\quad i\leq m'
 \tag*{(5.2.1)}
 \]
-i.e. $f$ est loc. $(m'\unsure{-|+}1)$-acyclique en $x$, pour \deleted{\unsure{les}} $\{\ell\}$, donc si $f$ est propre, on a
+i.e. $f$ est loc. $(m'\deleted{\unsure{-|+}}1)$-acyclique en $x$, pour \deleted{\unsure{les}} $\{\ell\}$, donc si $f$ est propre, on a
 \[
-H^i(X_0,\Lambda_\nu)\unsure{-|\longrightarrow}H^i(X_{\bar{\eta}},\Lambda_\nu)
+H^i(X_0,\Lambda_\nu)\unsure{-|\longrightarrow}H^i(X_{\bar{\unsure{\eta|y}}},\Lambda_\nu)
 \quad\text{un isom si $i<m'$, mon. si $i=m'$.}
 \tag*{(5.2.2)}
 \]
@@ -56,4 +56,4 @@
 
 \deleted{Alors}
 
-\deleted{Résulte facilement de 5.2, en y faisant $m'=m-d$, la condition a) de 5.2 est satisfaite par vertu de (5.3.2), et la condition b) résultant de}
+\deleted{Résulte \unsure{formellement|facilement} de 5.2, en y faisant $m'=m-d$, la condition a) de 5.2 est satisfaite \unsure{par|en} vertu de (5.3.2), et la condition b) résultant de}
```

### Supplementary reading

Start: 2026-11-17T23:54:35.516315+00:00. End: 2026-11-17T23:55:20.439589+00:00.

All three thirds re-read, cancelled 5.3.1 enlarged. Checked the first Phi/nu/h/eta markers, index i versus j, cancelled sign between m′ and 1, plain dash in 5.2.2, all superscripts and cancellation boundaries. No additional reading change; the multiply cancelled inf/sup and in/et candidates remain unresolved.

```diff
no change
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -11,7 +11,7 @@
 \deleted{(ce qui est le cas}
 Alors on a
 \[
-(\unsure{\underline{\Phi}|\underline{\varphi}}^i_{\unsure{\nu|v}})_x\unsure{=}0\quad\text{si}\quad i\leq m'
+({\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}})_x\unsure{=}0\quad\text{si}\quad i\leq m'
 \tag*{(5.2.1)}
 \]
 i.e. $f$ est loc. $(m'\deleted{\unsure{-|+}}1)$-acyclique en $x$, pour \deleted{\unsure{les}} $\{\ell\}$, donc si $f$ est propre, on a
@@ -27,7 +27,7 @@
 \deleted{\left\{\begin{aligned}
 d&=\sup_{\substack{x'\in Z\,\deleted{\unsure{\cap X_{\bar{x}}}}\\x'\text{ générise }x}}\dim\overline{\{x'\}},\\
 \deleted{m}&\deleted{=\unsure{\operatorname{prof\,ét}^{*}_Z}}\\
-1+m&=\sup_h\unsure{\operatorname{prof\,ét}^{*}_Z(X(h))}\;\unsure{\in|\text{et}}\;\unsure{\sup|\inf}_h\unsure{\operatorname{prof\,ét}^{*}(X(h))}-\dim\overline{\{\unsure{x'|x}\}}
+1+m&=\sup_h\unsure{\operatorname{prof\,ét}^{*}_Z(X(h))}\;\unsure{\in|\text{et}}\;{\unsure{\sup|\inf}}_h\unsure{\operatorname{prof\,ét}^{*}(X(h))}-\dim\overline{\{\unsure{x'|x}\}}
 \end{aligned}\right.}
 \tag*{\deleted{\unsure{(5.3.1)}}}
 \]
```

## Scan 151

Start: **2026-11-17T20:51:37.340920+00:00**. End: **2026-11-17T20:56:00.198063+00:00**.

Crop observations recorded: 2026-11-17T20:52:06.619694+00:00.

Before opening: top “Cf. 5.0. sur les hypothèses préliminaires”; boxed “Supposons la condit. a) de 5.2 satisfaite”; “Corollaire”; “La condition b)”; addition “et la conclusion 5.2.1”; “satisfaite”; “cas suivants (i) et (ii)”; “où on a posé”; “parcourt les générisations”; “Cas I”; “Pour toute générisation”; “ce qui est le cas si on fait”; “un entier tel que”; “Cas II”; “Le morphisme f est plat en x”; “Cf SGA 2 XIV 5.3”; “notion de profondeur géométrique”; “Démonstration”; “stables”; added “générisation et”; “changement”; “il suffit de vérifier”; “entraînent”; “Or la deuxième des relations”; “s'écrit”; bottom “où x̄′ est un pt de X′ au-dessus de x′, donc on peut/voit”. Acute accents in préliminaires, générisations, géométrique, vérifier; circumflex in entraîne/entraînent. Several letters in the depth definitions and all deeply overwritten symbols need separate checking.

### Checks

- **prose:** Reread all three thirds, then enlarged top, Case II, proof and formula regions. Final word is closer to peut than voit; retained both. The opening inserted hypothesis follows its linking stroke. Abbreviations condit., tt gén., pt remain unexpanded.
- **indices:** Every displayed bound compared: m prime in 5.3.1; m-d-1 in the prose; star/alpha distinction between 5.3.1 and 5.3.2 preserved. x and x prime, geometric bar x prime, X prime and X_eta ambient superscripts checked independently. No degree i/j appears here.
- **deletions:** Cancelled supremum subscript, (i), +1, -d, duplicate m, opening Case II sentence, on a, abandoned depth condition, two unreadable proof words, peut aussi/s écrire, and old inequality remain marked. The thick -d after the Case II depth is particularly uncertain in both reading and cancellation extent.
- **margins:** Top Cf. 5.0 note and deleted Si le cas; boxed Supposons insertion; inserted générisation et; definition dimension added to right; equality in right margin reread from enlarged images.
- **alphabets:** Ordinary H absent. Depth stars and alpha-like signs compared. First generic-point eta now carries y alternative. No double-struck capital newly introduced.

### Every inline formula

1. `d=\sup_{\deleted{\unsure{x'\in Z}}}\dim\overline{\{x'\}}`
2. `x'`
3. `x`
4. `X_0`
5. `x'`
6. `x`
7. `X`
8. `m'=m-d-1`
9. `m`
10. `m`
11. `x'\in Z`
12. `x`
13. `x'`
14. `x`
15. `X`
16. `x'\in X_\eta`
17. `x'`
18. `x`
19. `Z`
20. `f`
21. `x`
22. `\overline{\underline{\mathrm{XIV}}}`
23. `m'=m-d`
24. `m`
25. `X`
26. `X(\unsure{h\|k})`
27. `=\dim\overline{\{x\}}+\dim\overline{\{\bar{x}'\}}^{(X')}`
28. `\bar{x}'`
29. `X'`
30. `x'`

### Every display

Display 1:

```latex
\left\{\begin{aligned}
\operatorname{prof\,ét}^{\unsure{*|\alpha}}_{x'}(X_0)&\geq m'+1&&\text{si }x'\in Z\\
\operatorname{prof\,ét}^{*}_{x'}(X_{\bar{\unsure{\eta|y}}})&\geq m'\deleted{\unsure{+1}}+\dim\overline{\{x\}}&&\text{si }x'\in X_\eta,
\end{aligned}\right.
\tag*{(5.3.1)}
```

Display 2:

```latex
\left\{\begin{aligned}
\operatorname{prof\,ét}^{\unsure{\alpha|*}}_{x'}(X_0)&\geq m&&\text{pour toute \inserted{générisation} $x'\in Z$ de $x$}\\
\operatorname{prof\,ét}^{\alpha}_{x'}(X_{\bar{\eta}})&\geq m\deleted{\unsure{-d}}-1&&\text{pour tt gén. $x'$ de $x$ dans $X$, avec $x'\in X_\eta$.}
\end{aligned}\right.
\tag*{(5.3.2)}
```

Display 3:

```latex
m'=\operatorname{prof\,géom}^{*}_x(X_0)\deleted{\unsure{-d}},\quad\text{où}\quad
\operatorname{prof\,géom}^{*}_x(X_0)\overset{\mathrm{df}}{=}\operatorname{prof\,géom}_x(X_0)+\inserted{\dim\overline{\{x\}}}
```

Display 4:

```latex
\deleted{\operatorname{prof\,géom}^{*}_x(X)}
```

Display 5:

```latex
\operatorname{prof\,ét}_x(X)\geq m'+1.
\tag*{(*)}
```

Display 6:

```latex
\operatorname{prof\,ét}_{x'}(X')\deleted{\unsure{\geq m'}}+\dim\overline{\{x'\}}^{(\unsure{X_\eta|X})}\geq m'+\dim\overline{\{x\}},
```

Display 7:

```latex
\dim\overline{\{x'\}}^{(X_\eta)}=\dim\overline{\{x'\}}^{X}-1=\dim\overline{\{x\}}+\dim\overline{\{\bar{x}'\}}^{(X')}-1
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

none; other i/j occurrences, if any, are enumerations or baseline variables in the formulas above.

### Margins, insertions and cancellations listed in full

**margin**

- Source line 5: `(Cf. 5.0. sur les hypothèses préliminaires) \deleted{\unsure{Si le cas}}`
- Source line 46: `$=\dim\overline{\{x\}}+\dim\overline{\{\bar{x}'\}}^{(X')}$`

**inserted**

- Source line 6: `Supposons la condit. a) de 5.2. satisfaite.`
- Source line 6: `de 5.2. (et donc la conclusion 5.2.1)`
- Source line 19: `générisation`
- Source line 25: `\deleted{On a} Le morphisme $f$ est plat en $x$, et on a`
- Source line 28: `\dim\overline{\{x\}}`
- Source line 37: `générisation et`
- Source line 42: `s'écrit`

**deleted**

- Source line 5: `\unsure{Si le cas}`
- Source line 6: `\unsure{x'\in Z}`
- Source line 8: `\unsure{(i)}`
- Source line 12: `\unsure{+1}`
- Source line 16: `$m$`
- Source line 20: `\unsure{-d}`
- Source line 25: `Pour toute générisation $x'$ de $x$ dans $Z$,`
- Source line 25: `On a`
- Source line 25: `on a`
- Source line 27: `\unsure{-d}`
- Source line 30: `ce qui est le cas si on fait $m'=m-d$, avec $m$ un entier tel que`
- Source line 32: `\operatorname{prof\,géom}^{*}_x(X)`
- Source line 37: `\illegible{2}`
- Source line 42: `\unsure{peut aussi}`
- Source line 42: `s'écrire`
- Source line 44: `\unsure{\geq m'}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -9,7 +9,7 @@
 \[
 \left\{\begin{aligned}
 \operatorname{prof\,ét}^{\unsure{*|\alpha}}_{x'}(X_0)&\geq m'+1&&\text{si }x'\in Z\\
-\operatorname{prof\,ét}^{*}_{x'}(X_{\bar{\eta}})&\geq m'\deleted{\unsure{+1}}+\dim\overline{\{x\}}&&\text{si }x'\in X_\eta,
+\operatorname{prof\,ét}^{*}_{x'}(X_{\bar{\unsure{\eta|y}}})&\geq m'\deleted{\unsure{+1}}+\dim\overline{\{x\}}&&\text{si }x'\in X_\eta,
 \end{aligned}\right.
 \tag*{(5.3.1)}
 \]
@@ -48,4 +48,4 @@
 \[
 \dim\overline{\{x'\}}^{(X_\eta)}=\dim\overline{\{x'\}}^{X}-1=\dim\overline{\{x\}}+\dim\overline{\{\bar{x}'\}}^{(X')}-1
 \]
-où $\bar{x}'$ est un pt de $X'$ au dessus de $x'$, donc on voit
+où $\bar{x}'$ est un pt de $X'$ au dessus de $x'$, donc on \unsure{peut|voit}
```

### Reference-numeral reconciliation

Upper and lower bars rechecked from the enlarged reference.

```diff
--- before
+++ after
@@ -27,7 +27,7 @@
 m'=\operatorname{prof\,géom}^{*}_x(X_0)\deleted{\unsure{-d}},\quad\text{où}\quad
 \operatorname{prof\,géom}^{*}_x(X_0)\overset{\mathrm{df}}{=}\operatorname{prof\,géom}_x(X_0)+\inserted{\dim\overline{\{x\}}}
 \]
-Cf. SGA 2 XIV 5.3 pour la notion de profondeur géométrique). \deleted{ce qui est le cas si on fait $m'=m-d$, avec $m$ un entier tel que}
+Cf. SGA 2 $\overline{\underline{\mathrm{XIV}}}$ 5.3 pour la notion de profondeur géométrique). \deleted{ce qui est le cas si on fait $m'=m-d$, avec $m$ un entier tel que}
 \[
 \deleted{\operatorname{prof\,géom}^{*}_x(X)}
 \]
```

## Scan 152

Start: **2026-11-17T20:56:00.199053+00:00**. End: **2026-11-17T20:57:07.846657+00:00**.

Crop observations recorded: 2026-11-17T20:56:19.176606+00:00.

['l’interpréter en disant que', 'ce qui par le th. de Lefschetz local', 'SGA 1 XIV 4.5 (the numeral looks like 1, not 2)', 'implique que', 'bijectif / injectif', 'il suffirait ... sauf dans le cas où ... (slanted margin, must enlarge)', 'donc [cancelled] équivaut à', 'première des ... relations (5.3.1)', 'Le fait que les relations (5.3.2) impliquent les relations (5.3.1) est d’autre part immédiat.', 'Cas II — De même, l’hypothèse est évidemment stable par passage', 'il suffit donc de prouver (inserted)', 'pour tte gén. x′ de x dans Z. Or on a', 'Lemme 5.3.3 (i) plus bas', 'donc, comme', 'D’autre part, Lemme 5.3.3 (ii) plus bas', 'donc on en conclut']

### Checks

- **prose:** Read all thirds before opening source, then top/middle/bottom enlargements. The citation is SGA 1 XIV 4.5 and remains so. The later small label may be 5.3.2 or 5.3.8, now marked. The shortened words th., tt gén. remain.
- **indices:** Checked all displays and inline bounds, the two H superscripts i (no descending j), m prime minus 1 twice, x prime versus x and their closures, X0 versus X, the starred depth, codimension sign and final m prime. The arrow between H terms has a small right tip in the enlarged image and is retained.
- **margins:** Made a new wider rotated crop of the slanted left note, including previously clipped final =1. Read il suffirait / que ce soit / bijectif / injectif / sauf dans le cas où m prime=1. Doubt retained on compressed opening words.
- **deletions:** Overwritten X prime under V in both formulas; cancelled +1 and dimension term; the proof wording crossed through around inserted la relation; deleted prof; Case II superseded sentence and depth displays; à dégager ! replaced by lemma reference; hatched dimension term all retained. No typed corrections on this handwritten page.
- **alphabets:** Ordinary H, X and V; bold-looking V is overlapping ink, not a new blackboard alphabet. First eta marked with y alternative. Geometric depth star is distinct.

### Every inline formula

1. `x'\in X'_{\unsure{\eta\|y}}=X'-X'_0`
2. `\overline{\underline{\mathrm{XIV}}}`
3. `i<m'-1`
4. `i=m'-1`
5. `i<m'-1`
6. `i=m'-1`
7. `m'=1`
8. `\operatorname{prof\,ét}_x(X_0)\geq m'+1`
9. `X`
10. `X(\unsure{h\|k})`
11. `x'`
12. `x`
13. `Z`
14. `\operatorname{codim}(\bar{x},\bar{x}')=\dim\overline{\{x'\}}-\dim\overline{\{x\}}\unsure{\geq\|\leq}d-\dim\overline{\{x\}}`

### Every display

Display 1:

```latex
\operatorname{prof\,ét}_{x'}(\deleted{\unsure{X'}}V)+\dim\overline{\{x'\}}^{(V)}\geq m'\deleted{\unsure{+1+\dim\overline{\{x\}}}},
```

Display 2:

```latex
H^i(\deleted{\unsure{X'}}V)\longrightarrow H^i(V_s)\quad\text{est bijectif pour $i<m'-1$,}
```

Display 3:

```latex
\deleted{\operatorname{prof\,ét}_{x'}(X)\geq m'+1}
\tag*{\unsure{(**)}}
```

Display 4:

```latex
\deleted{\operatorname{prof\,ét}_{x'}(X)\geq\operatorname{prof\,ét}_{x'}}
```

Display 5:

```latex
\operatorname{prof\,géom}_{x'}(X_0)\geq\operatorname{prof\,géom}_{x}(X)\unsure{-|\deleted{+}}\operatorname{codim}(\bar{x},\bar{x}')
```

Display 6:

```latex
\operatorname{prof\,géom}_{x'}(X_0)\geq\operatorname{prof\,géom}^{*}_x(X_0)\deleted{\unsure{+\dim\overline{\{x\}}}}-d=m'.
```

Display 7:

```latex
\operatorname{prof\,géom}_{x'}(X)\geq\operatorname{prof\,géom}_{x'}(X_0)+\underset{\substack{\Vert\\\operatorname{prof\,géom}_s(S)}}{1},
```

Display 8:

```latex
\operatorname{prof\,géom}_{x'}(X)\geq m'+1.
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

- Source line 11: ` implique que \[ H^i(\deleted{\unsure{X'}}`
- Source line 11: `)\longrightarrow H^i(V_s)\quad\text{est bi`

### Margins, insertions and cancellations listed in full

**margin**

- Source line 15: `il \unsure{suffirait} \unsure{que ce soit} bijectif pour $i<m'-1$, injectif pour $i=m'-1$, sauf dans le cas où $m'=1$`

**inserted**

- Source line 13: `injectif pour $i=m'-1$`
- Source line 17: `la relation`
- Source line 19: `évidemment`
- Source line 19: `Il suffit donc de prouver`
- Source line 24: `5.3.3 (i) (plus bas)`

**deleted**

- Source line 7: `\unsure{X'}`
- Source line 7: `\unsure{+1+\dim\overline{\{x\}}}`
- Source line 11: `\unsure{X'}`
- Source line 17: `il suffit pour établir`
- Source line 17: `de prouver que l'on a`
- Source line 17: `\unsure{prof}`
- Source line 19: `de plus elle est stable par générisation, comme on constate aussitôt que`
- Source line 21: `\operatorname{prof\,ét}_{x'}(X)\geq m'+1`
- Source line 24: `à dégager !`
- Source line 26: `\operatorname{prof\,ét}_{x'}(X)\geq\operatorname{prof\,ét}_{x'}`
- Source line 29: `+`
- Source line 33: `\unsure{+\dim\overline{\{x\}}}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -2,7 +2,7 @@
 \mspage{V.24}
 % archive sheet number: 151
 
-l'\unsure{interpréter} en disant que pour $x'\in X'_\eta=X'-X'_0$, on a
+l'\unsure{interpréter} en disant que pour $x'\in X'_{\unsure{\eta|y}}=X'-X'_0$, on a
 \[
 \operatorname{prof\,ét}_{x'}(\deleted{\unsure{X'}}V)+\dim\overline{\{x'\}}^{(V)}\geq m'\deleted{\unsure{+1+\dim\overline{\{x\}}}},
 \]
@@ -12,9 +12,9 @@
 \]
 \inserted{injectif pour $i=m'-1$}
 % slanted
-\margin{il \unsure{suffirait} que ce soit bijectif pour $i<m'-1$, injectif pour $i=m'-1$, sauf dans le cas où $m'=1$}
+\margin{il \unsure{suffirait} \unsure{que ce soit} bijectif pour $i<m'-1$, injectif pour $i=m'-1$, sauf dans le cas où $m'=1$}
 
-donc \deleted{il suffit pour établir} \inserted{la relation} (*) \deleted{de prouver que l'on a} équivaut à $\operatorname{prof\,ét}_x(X_0)\geq m'+1$, ce qui est la première des \deleted{\unsure{prof}} relations (5.3.1). Le fait que les relations (5.3.2) impliquent les relations (5.3.1) est d'autre part immédiat.
+donc \deleted{il suffit pour établir} \inserted{la relation} (*) \deleted{de prouver que l'on a} équivaut à $\operatorname{prof\,ét}_x(X_0)\geq m'+1$, ce qui est la première des \deleted{\unsure{prof}} relations (5.3.1). Le fait que les relations (\unsure{5.3.2|5.3.8}) impliquent les relations (5.3.1) est d'autre part immédiat.
 
 \uline{Cas II} De même, l'hypothèse est \inserted{évidemment} stable par passage de $X$ à $X(\unsure{h|k})$, \deleted{de plus elle est stable par générisation, comme on constate aussitôt que} \inserted{Il suffit donc de prouver} qu'elle implique (*)
 \[
```

### Supplementary reading

Start: 2026-11-17T23:55:20.439598+00:00. End: 2026-11-17T23:56:39.021088+00:00.

All three thirds re-read and slanted note viewed again in rotated enlargement. The printed-looking SGA reference visibly says 1, not 2; retained. Codimension inequality direction and minus/overwritten-plus left marked. Reference numeral XIV has separate upper and lower bars; represented explicitly. No other formula or wording changes.

```diff
--- before
+++ after
@@ -6,7 +6,7 @@
 \[
 \operatorname{prof\,ét}_{x'}(\deleted{\unsure{X'}}V)+\dim\overline{\{x'\}}^{(V)}\geq m'\deleted{\unsure{+1+\dim\overline{\{x\}}}},
 \]
-ce qui par le th. de Lefschetz local SGA 1 XIV 4.5 implique que
+ce qui par le th. de Lefschetz local SGA 1 $\overline{\underline{\mathrm{XIV}}}$ 4.5 implique que
 \[
 H^i(\deleted{\unsure{X'}}V)\longrightarrow H^i(V_s)\quad\text{est bijectif pour $i<m'-1$,}
 \]
```

## Scan 153

Start: **2026-11-17T20:57:07.847661+00:00**. End: **2026-11-17T20:59:25.973206+00:00**.

Crop observations recorded: 2026-11-17T20:57:40.870014+00:00.

['D’autre part le th. de Lefschetz local entraîne', 'SGA 1 XIV 5.6 (last digit has a loop; recheck)', 'd’où ... cqfd.', 'Il reste à regarder un', 'Lemme 5.3.3 (i) Soit A un anneau local noethérien', 'un idéal premier', '(ii) Soit A — B un hom. local d’anneaux locaux noethériens', 'avec B plat sur A', 'corps résiduel ... celui de B', 'formellement lisse sur k', 'condition satisfaite en tous cas', 'extension de type fini', 'Donner démonstrations, ! (plural and punctuation uncertain)', '(*) Cette condition est peut-être inutile. Pour une reformulation de cette condition, cf EGA 0 IV 22.2.2']

### Checks

- **prose:** All three thirds read before the file; intro, both lemma parts and bottom footnote enlarged again. Confirmed SGA 1 XIV 5.6, with a looped 6. Il reste à regarder un stays uncertain; Donner démonstrations/démonstration retains plural doubt and the comma before !. EGA reference and peut-être inutile reread.
- **indices:** Checked first inequality with x prime at both depths, localization A_p, quotient A/p, and final B tensor over A with k. No i/j degree occurs; (i) and (ii) are enumeration labels. Inequality signs all point greater-than-or-equal. The A-to-B connector remains dash/arrow uncertain.
- **alphabets:** A B C K are ordinary capitals, k lower-case; p has a looped descending form, Gothic/roman ambiguity retained. No doubled stems justify blackboard capitals. Both geometric-depth occurrences retain the same reading.
- **deletions:** Deleted par after d’où, and sur k, de corps after C checked against their crossing strokes. Underline under plat is emphasis, not cancellation. No typed material or handwritten correction to type.
- **margins:** Bottom (*) note read independently from its enlargement: condition peut-être inutile, reformulation, EGA 0_IV 22.2.2. No sideways note or diagram.

### Every inline formula

1. `\overline{\underline{\mathrm{XIV}}}`
2. `A`
3. `\unsure{\mathfrak{p}\|p}`
4. `A`
5. `A\unsure{-\|\longrightarrow}B`
6. `B`
7. `A`
8. `k`
9. `A`
10. `K`
11. `B`
12. `C`
13. `k`
14. `k`
15. `K`
16. `K`
17. `k`
18. `0_{\mathrm{IV}}`

### Every display

Display 1:

```latex
\operatorname{prof\,ét}_{x'}(X)\geq\operatorname{prof\,géom}_{x'}(X),
```

Display 2:

```latex
\operatorname{prof\,géom}A_{\mathfrak{p}}\geq\operatorname{prof\,géom}A-\dim A/\mathfrak{p}
```

Display 3:

```latex
\operatorname{prof\,géom}B\geq\operatorname{prof\,géom}A+\operatorname{prof\,géom}B\otimes_A k.
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

none; other i/j occurrences, if any, are enumerations or baseline variables in the formulas above.

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

none

**deleted**

- Source line 9: `par`
- Source line 18: `sur $k$, de corps`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
no change
```

### Reference-numeral reconciliation

Upper and lower bars rechecked from the enlarged reference.

```diff
--- before
+++ after
@@ -2,7 +2,7 @@
 \mspage{V.25}
 % archive sheet number: 152
 
-D'autre part, le th de Lefschetz local entraîne (SGA 1 XIV 5.6)
+D'autre part, le th de Lefschetz local entraîne (SGA 1 $\overline{\underline{\mathrm{XIV}}}$ 5.6)
 \[
 \operatorname{prof\,ét}_{x'}(X)\geq\operatorname{prof\,géom}_{x'}(X),
 \]
```

## Scan 154

Start: **2026-11-17T20:59:25.974925+00:00**. End: **2026-11-17T21:01:10.747582+00:00**.

Crop observations recorded: 2026-11-17T21:00:01.282801+00:00.

['Voici un corollaire du Cas II :', 'Corollaire 5.4', 'Supposons [X plat sur S et added] X0 loc. une intersection complète et purement de dimension n.', 'où d est la dimension du lieu Z des pts de X0 en lesquels f est non lisse', 'En particulier, si d=0', 'donc l’homomorphisme', 'isomorphisme / monomorphisme / épimorphisme', 'de plus L’action du groupe d’inertie I', 'est triviale (cancelled once, then live on next line)', '5.5. Pour terminer le présent paragraphe, nous allons donner un ... des résultats précédents pour la cohomologie non commutative', 'loc. 1-acyclique pour L', 'distinctes de x (right insertion)', 'en terme des conditions de local-asphéricité en x', 'l’ens. de nb premiers', 'Je dis que pour tout ... groupe fini G', 'premier à ... (cancelled)']

### Checks

- **prose:** All thirds and enlarged top, middle, bottom prose checked. In 5.5 the ink reads asphéricité (p/h and following strokes), not the first-pass acyclicité; locale/local ending remains uncertain. Compressed variante and proposons-nous/proposons now marked. Kept abbreviations ens, pts, grp, tt, nbs.
- **indices:** Compared all six displays and inline degree ranges: first interval n-d+1,n+1; second n-d+1,n+d+1; d=0 pair has no i on the second Phi and is preserved. H target lacks its closing parenthesis in the ink; no parenthesis supplied. Isomorphism excludes n,n+1; mono at n, epi n+1; inertia statement excludes n. Final i<=1 and label 5.5.1 checked. All H degrees are i, not j.
- **margins:** Flatness insertion joins after Supposons. Added de plus belongs before L’action. pour L and distinctes de x follow insertion strokes. Lower left diagram: V above X prime, inclusion mark, vertical arrow to S; V--bar V has no head; bar V vertical has no head; bottom right bar S/bar eta points left to S.
- **deletions:** Old interval and following bound crossed through; donc struck; small de before I struck; est triviale cancelled then rewritten; donner cancelled; prime-set expression hatched; premier à blackboard L crossed out. Final blackboard L has two clear stems, so earlier ell/L uncertainty removed there.
- **alphabets:** Phi underline distinction preserved; first nu/v and eta/y marked; blackboard Z has a doubled diagonal; L has two stems in the later insertion and cancelled phrase, while the first L remains alphabet-uncertain. Ordinary I inertia capital has top and bottom bars.

### Every inline formula

1. `X`
2. `S`
3. `X_0`
4. `n`
5. `d`
6. `Z`
7. `X_0`
8. `f`
9. `d=0`
10. `i\neq n,n+1`
11. `i=n`
12. `i=n+1`
13. `I`
14. `H^i(X_{\bar{\eta}},\Lambda_\nu)`
15. `H^i(X_{\bar{\eta}},\mathbb{Z}_\ell)`
16. `i\neq n`
17. `f`
18. `1`
19. `\unsure{\mathbb{L}\|L}`
20. `x`
21. `x`
22. `1`
23. `x`
24. `\unsure{\ell\in\mathbb{P}-\{p\}}`
25. `\mathbb{L}`
26. `G`
27. `\mathbb{L}`

### Every display

Display 1:

```latex
{\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}}=0\quad\text{pour}\quad
\deleted{i\notin[n-d+1,n+1]\quad\unsure{i\leq m'}}\inserted{i\notin[n-d+1,n+1]},
```

Display 2:

```latex
\Phi^i_\nu=0\quad\text{si}\quad i\notin[n-d+1,n+d+1]
```

Display 3:

```latex
\begin{aligned}
\underline{\Phi}^i_\nu&=0\quad\text{si}\quad i\neq n+1\\
\Phi_\nu&=0\quad\text{si}\quad i\neq n+1,
\end{aligned}
```

Display 4:

```latex
H^i(X_0,\Lambda_\nu)\longrightarrow H^i(X_{\bar{\unsure{\eta|y}}},\Lambda_\nu,
```

Display 5:

```latex
H^i(\bar{V},G)\xrightarrow{\sim}H^i(V_{\bar{\eta}},G)\quad\text{si}\quad i\leq1.
\tag*{(5.5.1)}
```

### Diagram objects, arrows and decorations

Diagram 1, source line 30:

```latex
\begin{tikzcd}[ampersand replacement=\&]
V \arrow[r,no head] \arrow[d,phantom,"\cap" description] \& \bar{V}\arrow[dd,no head]\\
X'\arrow[d] \& \\
S \& \unsure{\bar{S}|\bar{\eta}}\arrow[l]
\end{tikzcd}
```

### i and j in scripts, and scripted i/j maps

- Source line 9: `derline{\varphi}}}^i_{\unsure{\nu\|v}}=0\qu`
- Source line 9: `rline{\varphi}}}^i_{\unsure{\nu\|v}}=0\quad\text{pour}\qua`
- Source line 14: `d{donc} et \[ \Phi^i_\nu=0\quad\text{si}\q`
- Source line 14: `donc} et \[ \Phi^i_\nu=0\quad\text{si}\quad `
- Source line 19: `} \underline{\Phi}^i_\nu&=0\quad\text{si}\`
- Source line 19: `\underline{\Phi}^i_\nu&=0\quad\text{si}\quad`
- Source line 20: `d i\neq n+1\\ \Phi_\nu&=0\quad\text{si}\quad`
- Source line 25: `homomorphisme \[ H^i(X_0,\Lambda_\nu)\long`
- Source line 25: `)\longrightarrow H^i(X_{\bar{\unsure{\eta\|`
- Source line 27: `re{de}} $I$ sur $H^i(X_{\bar{\eta}},\Lambd`
- Source line 27: `riviale} ou sur $H^i(X_{\bar{\eta}},\mathb`
- Source line 37: `bb{L}$}, on a \[ H^i(\bar{V},G)\xrightarro`
- Source line 37: `xrightarrow{\sim}H^i(V_{\bar{\eta}},G)\qua`

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

- Source line 7: `$X$ plat sur $S$ et`
- Source line 10: `i\notin[n-d+1,n+1]`
- Source line 27: `de plus`
- Source line 29: `pour $\unsure{\mathbb{L}\|L}$`
- Source line 29: `distinctes de $x$`
- Source line 35: `$\mathbb{L}$-`

**deleted**

- Source line 10: `i\notin[n-d+1,n+1]\quad\unsure{i\leq m'}`
- Source line 12: `donc`
- Source line 27: `\unsure{de}`
- Source line 27: `est triviale`
- Source line 29: `donner`
- Source line 29: `$\unsure{\ell\in\mathbb{P}-\{p\}}$`
- Source line 35: `premier à $\mathbb{L}$`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -22,17 +22,17 @@
 \]
 donc l'homomorphisme
 \[
-H^i(X_0,\Lambda_\nu)\longrightarrow H^i(X_{\bar{\eta}},\Lambda_\nu,
+H^i(X_0,\Lambda_\nu)\longrightarrow H^i(X_{\bar{\unsure{\eta|y}}},\Lambda_\nu,
 \]
 est un isomorphisme si $i\neq n,n+1$, un monomorphisme pour $i=n$, un épimorphisme pour $i=n+1$; \inserted{de plus} L'action du grp d'inertie \deleted{\unsure{de}} $I$ sur $H^i(X_{\bar{\eta}},\Lambda_\nu)$ \deleted{est triviale} ou sur $H^i(X_{\bar{\eta}},\mathbb{Z}_\ell)$ est triviale si $i\neq n$.
 
-5.5. Pour terminer le présent paragraphe, nous allons donner une variante des résultats précédents pour la cohomologie non commutative. Supposons $f$ loc. $1$-acyclique \inserted{pour $\unsure{\mathbb{L}|L}$} en toutes les générisations de $x$, \inserted{distinctes de $x$} et proposons de \deleted{donner} trouver des conditions de locale $1$-acyclicité en $x$, pour l'ens de nbs premiers \deleted{$\unsure{\ell\in\mathbb{P}-\{p\}}$}.
+5.5. Pour terminer le présent paragraphe, nous allons donner une \unsure{variante} des résultats précédents pour la cohomologie non commutative. Supposons $f$ loc. $1$-acyclique \inserted{pour $\unsure{\mathbb{L}|L}$} en toutes les générisations de $x$, \inserted{distinctes de $x$} et \unsure{proposons-nous|proposons} de \deleted{donner} trouver des conditions de \unsure{locale|local} $1$-asphéricité en $x$, pour l'ens de nbs premiers \deleted{$\unsure{\ell\in\mathbb{P}-\{p\}}$}.
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
 V \arrow[r,no head] \arrow[d,phantom,"\cap" description] \& \bar{V}\arrow[dd,no head]\\
 X'\arrow[d] \& \\
 S \& \unsure{\bar{S}|\bar{\eta}}\arrow[l]
 \end{tikzcd}}
-Je dis que pour tt \inserted{$\mathbb{L}$-}grp fini $G$, \deleted{premier à $\unsure{\ell|L}$}, on a
+Je dis que pour tt \inserted{$\mathbb{L}$-}grp fini $G$, \deleted{premier à $\mathbb{L}$}, on a
 \[
 H^i(\bar{V},G)\xrightarrow{\sim}H^i(V_{\bar{\eta}},G)\quad\text{si}\quad i\leq1.
 \tag*{(5.5.1)}
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -6,7 +6,7 @@
 
 \uline{Corollaire} 5.4 Supposons \inserted{$X$ plat sur $S$ et} $X_0$ loc. une intersection complète et purement de dimension $n$. Alors on a
 \[
-\unsure{\underline{\Phi}|\underline{\varphi}}^i_{\unsure{\nu|v}}=0\quad\text{pour}\quad
+{\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}}=0\quad\text{pour}\quad
 \deleted{i\notin[n-d+1,n+1]\quad\unsure{i\leq m'}}\inserted{i\notin[n-d+1,n+1]},
 \]
 où $d$ est la dimension de l'ens $Z$ des pts de $X_0$ en lesquels $f$ est non lisse, \deleted{donc} et
```

## Scan 155

Start: **2026-11-17T21:01:10.748787+00:00**. End: **2026-11-17T21:03:24.621084+00:00**.

Crop observations recorded: 2026-11-17T21:01:47.576414+00:00.

['Donc pour avoir la locale 1-asphéricité pour L en x', 'il suffit de supposer que l’on a, pour tt tel G', 'On sait [cancelled phrase] que cette condition est vérifiée lors...', 'intersections complètes de dim >=3 en x', 'et sans doute dès que leur prof géom en x est >=3 (small insertion)', 'Lorsque f est plat en x, cela signifie aussi que', 'X0 est une inters. cplète de dimension >=2 en x', 'Utilisant le th de locale 1-asphéricité pour L des morphismes lisses', 'Théorème 5.6', 'Supposons ... non lisse ... codimension >=2', 'localement 1-asphérique', 'En particulier si f est propre ... alors', 'd’ordre (insertion)', 'l’hom de spécialisation ... est un isomorphisme', 'Remarque 5.7. a) Il semble qu’il doive être possible de remplacer', 'cela résulterait d’une solution affirmative à SGA 1 XIV 6.3']

### Checks

- **prose:** Read thirds before source, enlarged rewritten first paragraph, theorem, top and remark. All three first-pass acyclicité/acyclique readings changed to asphéricité/asphérique from the p-h-er strokes. First paragraph remains uncertain: les/lors, cancelled pour/que, X(h) cancellation extent, est/sont, des/les; alternatives explicitly retained instead of reconstructing a grammatical sentence.
- **indices:** Checked H^i V(h), h/k, overwritten X under V, bound <=1/<1, label 5.5.1/5.5.2, dimensions >=3 and >=2, codimension >=2, prime-set definition with an unclear small subscript at the equality, H^1/i specialization and final depth >=2. Dotted H degree i has no descender; specialization 1/i remains doubtful. Generic eta/y now marked on first actual X occurrence.
- **margins:** Small parenthesis et sans doute dès que leur prof géom en x est >=3 read above Lorsque. de X insertion after points; alors after propre; d’ordre before premier à p all checked.
- **deletions:** Crossed opening phrase, rewritten X(h) sentence and overwritten X in the first H argument retained. No strike crosses live theorem or remark; underline under Théorème and Remarque is emphasis.
- **alphabets:** L doubled stem in theorem, P doubled upright; initial L alphabet ambiguous. Z locus ordinary. G ordinary, not a script capital. No diagrams on this page.

### Every inline formula

1. `1`
2. `\unsure{\mathbb{L}\|L}`
3. `x`
4. `G`
5. `\unsure{\deleted{X(h)}\|X(h)}`
6. `\geq3`
7. `x`
8. `x`
9. `\geq3`
10. `f`
11. `x`
12. `X_0`
13. `\geq2`
14. `x`
15. `1`
16. `\mathbb{L}`
17. `f:X\longrightarrow S`
18. `Z`
19. `X`
20. `f`
21. `\geq2`
22. `X_0`
23. `f`
24. `1`
25. `\mathbb{L}_{\unsure{\eta\|s}}=\mathbb{P}-\{p\}`
26. `f`
27. `\forall`
28. `G`
29. `p`
30. `X_0`
31. `x\in Z`
32. `\operatorname{prof\,géom}_x(X_0)\geq2`
33. `\overline{\underline{\mathrm{XIV}}}`

### Every display

Display 1:

```latex
H^i(\deleted{\unsure{X}}V(\unsure{h|k}),G)=0\quad\text{si}\quad i\unsure{\leq|<}1
\tag*{\unsure{(5.5.1)|(5.5.2)}}
```

Display 2:

```latex
H^{\unsure{1|i}}(X_0,G)\unsure{-|\longrightarrow}H^1(X_{\bar{\unsure{\eta|y}}},G)
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

- Source line 7: ` tt tel $G$ : \[ H^i(\deleted{\unsure{X}}V`
- Source line 16: `pécialisation \[ H^{\unsure{1\|i}}(X_0,G)\unsure{-\|\long`

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

- Source line 10: `(et sans doute dès que leur prof géom en $x$ est $\geq3$)`
- Source line 14: `de $X$`
- Source line 14: `alors,`
- Source line 14: `d'ordre`

**deleted**

- Source line 7: `\unsure{X}`
- Source line 10: `\unsure{par suite de\|par vertu de}`
- Source line 10: `\unsure{pour\|que}`
- Source line 10: `X(h)`
- Source line 10: `\unsure{est\|sont}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -2,18 +2,18 @@
 \mspage{V.27}
 % archive sheet number: 154
 
-Donc pour avoir la locale $1$-acyclicité pour $\unsure{\mathbb{L}|L}$ en $x$, il suffit de supposer que l'on a, pour tt tel $G$ :
+Donc pour avoir la locale $1$-asphéricité pour $\unsure{\mathbb{L}|L}$ en $x$, il suffit de supposer que l'on a, pour tt tel $G$ :
 \[
-H^i(\deleted{\unsure{X}}V(\unsure{h|k}),G)=0\quad\text{si}\quad i\leq1
+H^i(\deleted{\unsure{X}}V(\unsure{h|k}),G)=0\quad\text{si}\quad i\unsure{\leq|<}1
 \tag*{\unsure{(5.5.1)|(5.5.2)}}
 \]
-On sait \deleted{\unsure{par suite de}} que cette condition est vérifiée \unsure{lors} \deleted{\unsure{que}} $X(h)$ \deleted{est} \unsure{des} intersections complètes de dim $\geq3$ en $x$, \inserted{(et sans doute dès que leur prof géom en $x$ est $\geq3$)}, lorsque $f$ est plat en $x$, cela signifie aussi que $X_0$ est une int. compl. de dimension $\geq2$ en $x$.
+On sait \deleted{\unsure{par suite de|par vertu de}} que cette condition est vérifiée \unsure{les|lors} \deleted{\unsure{pour|que}} $\unsure{\deleted{X(h)}|X(h)}$ \deleted{\unsure{est|sont}} \unsure{des|les} intersections complètes de dim $\geq3$ en $x$, \inserted{(et sans doute dès que leur prof géom en $x$ est $\geq3$)}, lorsque $f$ est plat en $x$, cela signifie aussi que $X_0$ est une int. compl. de dimension $\geq2$ en $x$.
 
-Utilisant le th de locale $1$-acyclicité pour $\mathbb{L}$ des morphismes lisses, on trouve ainsi le
+Utilisant le th de locale $1$-asphéricité pour $\mathbb{L}$ des morphismes lisses, on trouve ainsi le
 
-\uline{Théorème} 5.6. Supposons que $f:X\longrightarrow S$ soit plat, que l'ens $Z$ des points \inserted{de $X$} en lesquels $f$ est non lisse est de codimension $\geq2$, et que $X_0$ soit une intersection complète locale en tous ses points. Alors $f$ est localement $1$-acyclique pour $\mathbb{L}_{\unsure{\eta|s}}=\mathbb{P}-\{p\}$. En particulier si $f$ est propre, \inserted{alors,} pour $\forall$ groupe fini $G$ \inserted{d'ordre} premier à $p$, l'hom de spécialisation
+\uline{Théorème} 5.6. Supposons que $f:X\longrightarrow S$ soit plat, que l'ens $Z$ des points \inserted{de $X$} en lesquels $f$ est non lisse est de codimension $\geq2$, et que $X_0$ soit une intersection complète locale en tous ses points. Alors $f$ est localement $1$-asphérique pour $\mathbb{L}_{\unsure{\eta|s}}=\mathbb{P}-\{p\}$. En particulier si $f$ est propre, \inserted{alors,} pour $\forall$ groupe fini $G$ \inserted{d'ordre} premier à $p$, l'hom de spécialisation
 \[
-H^{\unsure{1|i}}(X_0,G)\unsure{-|\longrightarrow}H^1(X_{\bar{\eta}},G)
+H^{\unsure{1|i}}(X_0,G)\unsure{-|\longrightarrow}H^1(X_{\bar{\unsure{\eta|y}}},G)
 \]
 est un isomorphisme.
```

### Reference-numeral reconciliation

Upper and lower bars rechecked from the enlarged reference.

```diff
--- before
+++ after
@@ -17,4 +17,4 @@
 \]
 est un isomorphisme.
 
-\uline{Remarque} 5.7. a) Il semble qu'il doive être possible de remplacer l'hypothèse que $X_0$ est une intersection complète par celle que pour tt $x\in Z$, on ait $\operatorname{prof\,géom}_x(X_0)\geq2$; cela résulterait d'une \unsure{solution|réponse} affirmative à SGA 1 XIV 6.3
+\uline{Remarque} 5.7. a) Il semble qu'il doive être possible de remplacer l'hypothèse que $X_0$ est une intersection complète par celle que pour tt $x\in Z$, on ait $\operatorname{prof\,géom}_x(X_0)\geq2$; cela résulterait d'une \unsure{solution|réponse} affirmative à SGA 1 $\overline{\underline{\mathrm{XIV}}}$ 6.3
```

## Scan 156

Start: **2026-11-17T21:03:24.622152+00:00**. End: **2026-11-17T21:04:58.031523+00:00**.

Crop observations recorded: 2026-11-17T21:03:54.327360+00:00.

['b) Les résultats précédents suggèrent la conjecture suivante', '(au moins pour A,B excellents) added top right', 'Soit f ... un morphisme plat de schémas noethériens', 'stricts locaux (inserted)', 's le point fermé de S', 'Supposons', 'géométrique / géométriquement (crossed wording)', 'pour tte extension finie k′ de k=k(s)', 'l’ens. singulier ... de dim <= d', 'et supposons ... m=prof géom B', 'Alors f est loc. (m-d-1)-acyclique', 'p car résiduelle en A', 'loc. 1-asphérique', 'Cela (struck) Il est plausible que', 'cela soit démontrable comme conséquence de la conjecture déjà citée SGA 1 XIV 6.3', 'résolution des singularités pour les schémas finis sur ... (last base letter uncertain)']

### Checks

- **prose:** All three thirds, enlarged cancelled draft and last paragraph, then whole sheet reread. Final loc. 1-asphérique corrected from acyclique; the earlier parenthesized degree statement does read acyclique. Last finis and base S/eta now marked. The opening cancelled grammar remains literal with added alternatives.
- **indices:** All inline formulas checked: X=Spec B, S=Spec A, f inverse image exponent -1; R_d twice and later cancelled R_1/d (different stroke); k prime versus k; tensor over k; dim<=d; m=prof geom B; m-d plus/minus 1; overwritten lower bound 3/1; L=P-{p}; m-d-1>=1 and m-d>=2. No i/j degrees, no displays or diagrams.
- **margins:** Top-right au moins pour A,B excellents is linked to the conjecture. Spec B/A inserted above X/S; stricts locaux and closed-point definition inserted over the cancelled line; singulier de and soit de dim<=d followed to their anchors.
- **deletions:** R_d hypotheses and residue-field draft all read through strike; nested X0 cancellation retained; one physically unreadable final word remains illegible. Cancelled m=prof géom, condition R_1/d, et supposons and threshold clause retained. Cela is struck before Il est plausible.
- **alphabets:** Ordinary R in R_d, double stems in L and P, ordinary A/B. The last base letter is angular S but eta remains possible. Bottom third contains no additional text apart from archive number 155.

### Every inline formula

1. `A,B`
2. `f:X\inserted{=\operatorname{Spec}B}\unsure{-\|\longrightarrow}S\inserted{=\operatorname{Spec}A}`
3. `s`
4. `S`
5. `X_0=f^{-1}(s)`
6. `(R_d)`
7. `X_0`
8. `k`
9. `X_0`
10. `(R_d)`
11. `k'`
12. `k=k(s)`
13. `m=\operatorname{prof\,géom}`
14. `X_0\otimes_k k'`
15. `R_{\unsure{1\|d}}`
16. `\leq d`
17. `m=\operatorname{prof\,géom}B`
18. `f`
19. `(m-d\unsure{-\|+}1)`
20. `m-d\unsure{-\|+}1\geq\deleted{\unsure{3}}1`
21. `\unsure{\mathbb{L}\|L}=\mathbb{P}-\{p\}`
22. `p`
23. `A`
24. `m-d-1\geq1`
25. `m-d\geq2`
26. `f`
27. `1`
28. `\mathbb{L}`
29. `\overline{\underline{\mathrm{XIV}}}`
30. `\unsure{S\|\eta}`

### Every display

none

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

none; other i/j occurrences, if any, are enumerations or baseline variables in the formulas above.

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

- Source line 5: `(au moins pour $A,B$ \uline{excellents})`
- Source line 7: `=\operatorname{Spec}B`
- Source line 7: `=\operatorname{Spec}A`
- Source line 7: `stricts locaux, $s$ le point fermé de $S$. $X_0=f^{-1}(s)$.`
- Source line 7: `singulier de`
- Source line 7: `soit de dim $\leq d$`

**deleted**

- Source line 7: `\unsure{et à les\|et à la} fibres géométriques \unsure{satisfaisant\|satisfassant} à la condition $(R_d)$,`
- Source line 7: `Soit \deleted{$X_0$} $k$ le corps \unsure{rés. du pt} \illegible{1},`
- Source line 7: `$X_0$`
- Source line 7: `$X_0$ soit géométriquement $(R_d)$, et que`
- Source line 7: `$m=\operatorname{prof\,géom}$`
- Source line 7: `satisfasse la condition $R_{\unsure{1\|d}}$, et supposons`
- Source line 7: `et si $m-d\unsure{-\|+}1\geq\deleted{\unsure{3}}1$`
- Source line 7: `\unsure{3}`
- Source line 7: `Cela`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -4,4 +4,4 @@
 
 b) Les résultats précédents suggèrent la conjecture suivante \inserted{(au moins pour $A,B$ \uline{excellents})}
 
-Soit $f:X\inserted{=\operatorname{Spec}B}\unsure{-|\longrightarrow}S\inserted{=\operatorname{Spec}A}$ un morphisme \uline{plat} de schémas noethériens, \inserted{stricts locaux, $s$ le point fermé de $S$. $X_0=f^{-1}(s)$.} \deleted{et à les fibres géométriques satisfaisant à la condition $(R_d)$,} \deleted{Soit \deleted{$X_0$} $k$ le corps \unsure{rés. du pt} \illegible{1},} Supposons que \deleted{$X_0$ soit géométriquement $(R_d)$, et que} pour tt extension finie $k'$ de $k=k(s)$, l'ens. \deleted{$m=\operatorname{prof\,géom}$}\inserted{singulier de} $X_0\otimes_k k'$ \deleted{satisfasse la condition $R_d$, et supposons} \inserted{soit de dim $\leq d$} et $m=\operatorname{prof\,géom}B$. Alors $f$ est loc. $(m-d\unsure{-|+}1)$-acyclique, \deleted{et si $m-d\unsure{-|+}1\geq\deleted{\unsure{3}}1$} pour $\unsure{\mathbb{L}|L}=\mathbb{P}-\{p\}$, ($p$. car résiduelle de $A$), et si $m-d-1\geq1$ i.e. $m-d\geq2$, $f$ est loc. $1$-acyclique pour $\mathbb{L}$. \deleted{Cela} Il est plausible que cela soit démontrable comme conséquence de la conjecture déjà citée SGA 1 XIV 6.3, et de la résolution des singularités pour les schémas finis sur $S$,
+Soit $f:X\inserted{=\operatorname{Spec}B}\unsure{-|\longrightarrow}S\inserted{=\operatorname{Spec}A}$ un morphisme \uline{plat} de schémas noethériens, \inserted{stricts locaux, $s$ le point fermé de $S$. $X_0=f^{-1}(s)$.} \deleted{\unsure{et à les|et à la} fibres géométriques \unsure{satisfaisant|satisfassant} à la condition $(R_d)$,} \deleted{Soit \deleted{$X_0$} $k$ le corps \unsure{rés. du pt} \illegible{1},} Supposons que \deleted{$X_0$ soit géométriquement $(R_d)$, et que} pour tt extension finie $k'$ de $k=k(s)$, l'ens. \deleted{$m=\operatorname{prof\,géom}$}\inserted{singulier de} $X_0\otimes_k k'$ \deleted{satisfasse la condition $R_{\unsure{1|d}}$, et supposons} \inserted{soit de dim $\leq d$} et $m=\operatorname{prof\,géom}B$. Alors $f$ est loc. $(m-d\unsure{-|+}1)$-acyclique, \deleted{et si $m-d\unsure{-|+}1\geq\deleted{\unsure{3}}1$} pour $\unsure{\mathbb{L}|L}=\mathbb{P}-\{p\}$, ($p$. car résiduelle de $A$), et si $m-d-1\geq1$ i.e. $m-d\geq2$, $f$ est loc. $1$-asphérique pour $\mathbb{L}$. \deleted{Cela} Il est plausible que cela soit démontrable comme conséquence de la conjecture déjà citée SGA 1 XIV 6.3, et de la résolution des singularités pour les schémas \unsure{finis} sur $\unsure{S|\eta}$,
```

### Reference-numeral reconciliation

Upper and lower bars rechecked from the enlarged reference.

```diff
--- before
+++ after
@@ -4,4 +4,4 @@
 
 b) Les résultats précédents suggèrent la conjecture suivante \inserted{(au moins pour $A,B$ \uline{excellents})}
 
-Soit $f:X\inserted{=\operatorname{Spec}B}\unsure{-|\longrightarrow}S\inserted{=\operatorname{Spec}A}$ un morphisme \uline{plat} de schémas noethériens, \inserted{stricts locaux, $s$ le point fermé de $S$. $X_0=f^{-1}(s)$.} \deleted{\unsure{et à les|et à la} fibres géométriques \unsure{satisfaisant|satisfassant} à la condition $(R_d)$,} \deleted{Soit \deleted{$X_0$} $k$ le corps \unsure{rés. du pt} \illegible{1},} Supposons que \deleted{$X_0$ soit géométriquement $(R_d)$, et que} pour tt extension finie $k'$ de $k=k(s)$, l'ens. \deleted{$m=\operatorname{prof\,géom}$}\inserted{singulier de} $X_0\otimes_k k'$ \deleted{satisfasse la condition $R_{\unsure{1|d}}$, et supposons} \inserted{soit de dim $\leq d$} et $m=\operatorname{prof\,géom}B$. Alors $f$ est loc. $(m-d\unsure{-|+}1)$-acyclique, \deleted{et si $m-d\unsure{-|+}1\geq\deleted{\unsure{3}}1$} pour $\unsure{\mathbb{L}|L}=\mathbb{P}-\{p\}$, ($p$. car résiduelle de $A$), et si $m-d-1\geq1$ i.e. $m-d\geq2$, $f$ est loc. $1$-asphérique pour $\mathbb{L}$. \deleted{Cela} Il est plausible que cela soit démontrable comme conséquence de la conjecture déjà citée SGA 1 XIV 6.3, et de la résolution des singularités pour les schémas \unsure{finis} sur $\unsure{S|\eta}$,
+Soit $f:X\inserted{=\operatorname{Spec}B}\unsure{-|\longrightarrow}S\inserted{=\operatorname{Spec}A}$ un morphisme \uline{plat} de schémas noethériens, \inserted{stricts locaux, $s$ le point fermé de $S$. $X_0=f^{-1}(s)$.} \deleted{\unsure{et à les|et à la} fibres géométriques \unsure{satisfaisant|satisfassant} à la condition $(R_d)$,} \deleted{Soit \deleted{$X_0$} $k$ le corps \unsure{rés. du pt} \illegible{1},} Supposons que \deleted{$X_0$ soit géométriquement $(R_d)$, et que} pour tt extension finie $k'$ de $k=k(s)$, l'ens. \deleted{$m=\operatorname{prof\,géom}$}\inserted{singulier de} $X_0\otimes_k k'$ \deleted{satisfasse la condition $R_{\unsure{1|d}}$, et supposons} \inserted{soit de dim $\leq d$} et $m=\operatorname{prof\,géom}B$. Alors $f$ est loc. $(m-d\unsure{-|+}1)$-acyclique, \deleted{et si $m-d\unsure{-|+}1\geq\deleted{\unsure{3}}1$} pour $\unsure{\mathbb{L}|L}=\mathbb{P}-\{p\}$, ($p$. car résiduelle de $A$), et si $m-d-1\geq1$ i.e. $m-d\geq2$, $f$ est loc. $1$-asphérique pour $\mathbb{L}$. \deleted{Cela} Il est plausible que cela soit démontrable comme conséquence de la conjecture déjà citée SGA 1 $\overline{\underline{\mathrm{XIV}}}$ 6.3, et de la résolution des singularités pour les schémas \unsure{finis} sur $\unsure{S|\eta}$,
```

## Scan 157

Start: **2026-11-17T21:04:58.032586+00:00**. End: **2026-11-17T21:07:12.239788+00:00**.

Crop observations recorded: 2026-11-17T21:05:29.928311+00:00.

['6. Cas d’un point de non lissité maximal', 'dans X0 inserted; de X0 cancelled', '(6.1) Soit x∈X0, et ... reprenons les notations du §4.', 'Nous supposons que l’on a pour tout i', 'Condition satisfaite en particulier si x est un point maximal de l’ensemble Z des pts de X0 en lesquels f n’est pas lisse', 'cancelled clause around (4.4.3), difficult', 'L’inclusion ... définit donc un isomorphisme', 'i.e. des isomorphismes', 'On peut ... à opérateurs π (compressed phrase)', 'Donc, au point de vue de leur structure cohomologique/chomologique', 'la situation des 5 schémas (4.2) se réduit aux quatre schémas', '(6.2) L’inclusion ... donne donc un homomorphisme', 'compte tenu que π opère trivialement sur ... (left box)', 'qui [cancelled] s’insère dans le triangle distingué']

### Checks

- **prose:** Read thirds before source, then heading, cancelled clause, middle and final triangle enlargements. Added the visible à before opérateurs; en sus and compter/considérer remain uncertain. Spelling candidate chomologique placed before cohomologique because the first o is not independently visible. Cancelled prose after non lisse made explicitly uncertain rather than silently grammatical.
- **indices:** Checked restriction Phi^i_nu|V, stalk at bar x prime after overwritten bar x, x prime !=x, all 6.1.2-4 functors/arguments, four V variants, u with two starred/bulleted positions and pi subscript, L/K/R bullet degrees. Every H has i without descender. 6.1.4 final comma/closing parenthesis newly marked. Circled K/kappa with bullet/prime checked from enlargement.
- **diagram:** 6.2.2 all three objects checked in full, including coefficient subscript V_bar_eta,bar V. Arrow top to lower left, lower left to lower right, lower right to top, no arrow labels; R bullet and K bullet at bottom, L bullet triv at top.
- **margins:** Heading dans X0 insertion; circled K/kappa insertion and L bullet triv parenthesis above 6.2.1; left box compte tenu que pi opère trivialement sur V_bar_s=V_s read letter by letter. Diagram top is not part of boxed 6.2.1.
- **deletions:** de X0 in heading, suppo, overwritten stalk, cancelled concluding en, long cancelled clause containing 4.4.3, donne before s’écrit, par le before s’insère all retained.
- **alphabets:** Double-stem derived R checked independently in each formula; ordinary R bullet at diagram bottom. Gamma has a right-angle top, but script T remains possible and is marked at first occurrence. Pi/Pi-capital, Phi/varphi, nu/v and eta/y first occurrences marked. K and kappa not globally conflated.

### Every inline formula

1. `X_0`
2. `X_0`
3. `x\in X_0`
4. `i`
5. `x`
6. `Z`
7. `X_0`
8. `f`
9. `X`
10. `x`
11. `\unsure{\pi\|\Pi}`
12. `V_s\simeq V_{\bar s},V,V_\eta,V_{\bar\eta}`
13. `V_{\bar s}\longrightarrow\bar V`
14. `{\unsure{K\|\kappa}}^{\unsure{\bullet\|\prime}}`
15. `(L^\bullet)^{\mathrm{triv}}`
16. `L^\bullet=\mathbb{R}\Gamma(V_s,\Lambda_\nu)`
17. `\pi`
18. `V_{\bar s}=V_s`

### Every display

Display 1:

```latex
\tag*{(6.1.1)}
{\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}}|V=0,\quad\text{i.e. }(\underline{\Phi}^i_\nu)_{\deleted{\unsure{\bar{x}}}\bar{x}'}=0\quad\text{pour tte gén. }x'\ne x\text{ dans }X_0\ \deleted{\unsure{en}}.
```

Display 2:

```latex
V_{\bar{\unsure{\eta|y}}}\longleftarrow\bar V
```

Display 3:

```latex
\tag*{(6.1.2)}
\mathbb{R}\unsure{\Gamma|\mathscr{T}}(\bar V,\Lambda_\nu)\xrightarrow{\sim}\mathbb{R}\Gamma(V_{\bar\eta},\Lambda_\nu)
```

Display 4:

```latex
\tag*{(6.1.3)}H^i(\bar V,\Lambda_\nu)\simeq H^i(V_{\bar\eta},\Lambda_\nu),
```

Display 5:

```latex
\tag*{(6.1.4)}\mathbb{R}(\Gamma,\pi)(\bar V,\Lambda_\nu)\xrightarrow{\sim}\mathbb{R}(\Gamma,\pi)(V_{\bar\eta},\Lambda_\nu\unsure{,|)}.
```

Display 6:

```latex
\tag*{(6.2.1)}
\boxed{u=(\kappa_\pi^{\unsure{*|\bullet}})^{\unsure{*|\bullet}}:\mathbb{R}(\Gamma,\pi)(V_{\bar\eta},\Lambda_\nu)\longrightarrow\mathbb{R}(\Gamma,\pi)(V_{\bar s},\Lambda_\nu),}
```

Display 7:

```latex
\tag*{(6.2.2)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}(\Gamma,\pi)(V_{\bar s},\Lambda_\nu)\simeq\mathbb{R}\Gamma(V_s,\Lambda_\nu)^{\mathrm{triv}}=L^{\bullet\,\mathrm{triv}}}\arrow[dl] \& \\
{R^\bullet=\mathbb{R}(\Gamma,\pi)(\bar V,(\Lambda_\nu)_{V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}(\Gamma,\pi)(V_{\bar\eta},\Lambda_\nu)=K^\bullet}\arrow[ul]
\end{tikzcd}
```

### Diagram objects, arrows and decorations

Diagram 1, source line 41:

```latex
\[
\tag*{(6.2.2)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}(\Gamma,\pi)(V_{\bar s},\Lambda_\nu)\simeq\mathbb{R}\Gamma(V_s,\Lambda_\nu)^{\mathrm{triv}}=L^{\bullet\,\mathrm{triv}}}\arrow[dl] \& \\
{R^\bullet=\mathbb{R}(\Gamma,\pi)(\bar V,(\Lambda_\nu)_{V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}(\Gamma,\pi)(V_{\bar\eta},\Lambda_\nu)=K^\bullet}\arrow[ul]
\end{tikzcd}
\]
```

### i and j in scripts, and scripted i/j maps

- Source line 10: `derline{\varphi}}}^i_{\unsure{\nu\|v}}\|V=0,`
- Source line 10: `rline{\varphi}}}^i_{\unsure{\nu\|v}}\|V=0,\quad\text{i.e. }`
- Source line 10: `}(\underline{\Phi}^i_\nu)_{\deleted{\unsur`
- Source line 10: `\underline{\Phi}^i_\nu)_{\deleted{\unsure{\b`
- Source line 25: `\[ \tag*{(6.1.3)}H^i(\bar V,\Lambda_\nu)\s`
- Source line 25: `ambda_\nu)\simeq H^i(V_{\bar\eta},\Lambda_`
- Source line 37: `oxed{u=(\kappa_\pi^{\unsure{*\|\bullet}})^{\unsure{*\|\bullet}}`

### Margins, insertions and cancellations listed in full

**margin**

- Source line 39: `compte tenu que $\pi$ opère trivialement sur $V_{\bar s}=V_s$`

**inserted**

- Source line 5: `dans $X_0$`
- Source line 33: `${\unsure{K\|\kappa}}^{\unsure{\bullet\|\prime}}$`
- Source line 34: `($(L^\bullet)^{\mathrm{triv}}$, où $L^\bullet=\mathbb{R}\Gamma(V_s,\Lambda_\nu)$)`

**deleted**

- Source line 5: `\unsure{de $X_0$}`
- Source line 7: `suppo`
- Source line 10: `\unsure{\bar{x}}`
- Source line 10: `\unsure{en}`
- Source line 12: `\unsure{et lorsque plus il en est\|et lorsque plus il a} (4.4.3) \unsure{une comp.}\ \unsure{conn.}\ point de $X$ \unsure{dominant et contenant} $x$`
- Source line 27: `\unsure{donne}`
- Source line 40: `par le`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -9,7 +9,7 @@
 \tag*{(6.1.1)}
 \unsure{\underline{\Phi}|\underline{\varphi}}^i_{\unsure{\nu|v}}|V=0,\quad\text{i.e. }(\underline{\Phi}^i_\nu)_{\deleted{\unsure{\bar{x}}}\bar{x}'}=0\quad\text{pour tte gén. }x'\ne x\text{ dans }X_0\ \deleted{\unsure{en}}.
 \]
-Condition satisfaite en particulier si $x$ est un point maximal de l'ensemble $Z$ des pts de $X_0$ en lesquels $f$ n'est pas lisse, \deleted{et lorsque plus il \unsure{a|est} (4.4.3) \unsure{une comp.}\ \unsure{conn.}\ point de $X$ \unsure{dominant et contenant} $x$}.
+Condition satisfaite en particulier si $x$ est un point maximal de l'ensemble $Z$ des pts de $X_0$ en lesquels $f$ n'est pas lisse, \deleted{\unsure{et lorsque plus il en est|et lorsque plus il a} (4.4.3) \unsure{une comp.}\ \unsure{conn.}\ point de $X$ \unsure{dominant et contenant} $x$}.
 
 L'inclusion
 \[
@@ -24,13 +24,13 @@
 \[
 \tag*{(6.1.3)}H^i(\bar V,\Lambda_\nu)\simeq H^i(V_{\bar\eta},\Lambda_\nu),
 \]
-On peut en sus \unsure{compter|compter les} opérateurs $\unsure{\pi|\Pi}$, (6.1.2) \deleted{\unsure{donne}} s'écrit
+On peut \unsure{en sus} \unsure{compter|considérer} à opérateurs $\unsure{\pi|\Pi}$, (6.1.2) \deleted{\unsure{donne}} s'écrit
 \[
-\tag*{(6.1.4)}\mathbb{R}(\Gamma,\pi)(\bar V,\Lambda_\nu)\xrightarrow{\sim}\mathbb{R}(\Gamma,\pi)(V_{\bar\eta},\Lambda_\nu).
+\tag*{(6.1.4)}\mathbb{R}(\Gamma,\pi)(\bar V,\Lambda_\nu)\xrightarrow{\sim}\mathbb{R}(\Gamma,\pi)(V_{\bar\eta},\Lambda_\nu\unsure{,|)}.
 \]
-Donc, au point de vue de leur structure \unsure{cohomologique|chomologique}, la situation des 5 schémas (4.2) se réduit aux quatre schémas $V_s\simeq V_{\bar s},V,V_\eta,V_{\bar\eta}$.
+Donc, au point de vue de leur structure \unsure{chomologique|cohomologique}, la situation des 5 schémas (4.2) se réduit aux quatre schémas $V_s\simeq V_{\bar s},V,V_\eta,V_{\bar\eta}$.
 
-(6.2) L'inclusion $V_{\bar s}\longrightarrow\bar V$ donne donc un homomorphisme \inserted{$\unsure{\kappa|K}^{\bullet}$}
+(6.2) L'inclusion $V_{\bar s}\longrightarrow\bar V$ donne donc un homomorphisme \inserted{$\unsure{K|\kappa}^{\unsure{\bullet|\prime}}$}
 \inserted{($(L^\bullet)^{\mathrm{triv}}$, où $L^\bullet=\mathbb{R}\Gamma(V_s,\Lambda_\nu)$)}
 \[
 \tag*{(6.2.1)}
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -7,7 +7,7 @@
 (6.1) Soit $x\in X_0$, et \deleted{suppo} reprenons les notations du § 4. Nous supposons que l'on a pour tt $i$
 \[
 \tag*{(6.1.1)}
-\unsure{\underline{\Phi}|\underline{\varphi}}^i_{\unsure{\nu|v}}|V=0,\quad\text{i.e. }(\underline{\Phi}^i_\nu)_{\deleted{\unsure{\bar{x}}}\bar{x}'}=0\quad\text{pour tte gén. }x'\ne x\text{ dans }X_0\ \deleted{\unsure{en}}.
+{\unsure{\underline{\Phi}|\underline{\varphi}}}^i_{\unsure{\nu|v}}|V=0,\quad\text{i.e. }(\underline{\Phi}^i_\nu)_{\deleted{\unsure{\bar{x}}}\bar{x}'}=0\quad\text{pour tte gén. }x'\ne x\text{ dans }X_0\ \deleted{\unsure{en}}.
 \]
 Condition satisfaite en particulier si $x$ est un point maximal de l'ensemble $Z$ des pts de $X_0$ en lesquels $f$ n'est pas lisse, \deleted{\unsure{et lorsque plus il en est|et lorsque plus il a} (4.4.3) \unsure{une comp.}\ \unsure{conn.}\ point de $X$ \unsure{dominant et contenant} $x$}.
 
@@ -30,7 +30,7 @@
 \]
 Donc, au point de vue de leur structure \unsure{chomologique|cohomologique}, la situation des 5 schémas (4.2) se réduit aux quatre schémas $V_s\simeq V_{\bar s},V,V_\eta,V_{\bar\eta}$.
 
-(6.2) L'inclusion $V_{\bar s}\longrightarrow\bar V$ donne donc un homomorphisme \inserted{$\unsure{K|\kappa}^{\unsure{\bullet|\prime}}$}
+(6.2) L'inclusion $V_{\bar s}\longrightarrow\bar V$ donne donc un homomorphisme \inserted{${\unsure{K|\kappa}}^{\unsure{\bullet|\prime}}$}
 \inserted{($(L^\bullet)^{\mathrm{triv}}$, où $L^\bullet=\mathbb{R}\Gamma(V_s,\Lambda_\nu)$)}
 \[
 \tag*{(6.2.1)}
@@ -38,10 +38,10 @@
 \]
 \margin{compte tenu que $\pi$ opère trivialement sur $V_{\bar s}=V_s$}
 qui \deleted{par le} s'insère dans le triangle distingué
-\[
+\diagram{\[
 \tag*{(6.2.2)}
-\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
+\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \& {\mathbb{R}(\Gamma,\pi)(V_{\bar s},\Lambda_\nu)\simeq\mathbb{R}\Gamma(V_s,\Lambda_\nu)^{\mathrm{triv}}=L^{\bullet\,\mathrm{triv}}}\arrow[dl] \& \\
 {R^\bullet=\mathbb{R}(\Gamma,\pi)(\bar V,(\Lambda_\nu)_{V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}(\Gamma,\pi)(V_{\bar\eta},\Lambda_\nu)=K^\bullet}\arrow[ul]
-\end{tikzcd}}
-\]
+\end{tikzcd}
+\]}
```

## Scan 158

Start: **2026-11-17T23:40:48.009578+00:00**. End: **2026-11-17T23:42:10.637116+00:00**.

Crop observations recorded: 2026-11-17T23:41:16.447439+00:00.

['L’homomorphisme u, (... le triangle (6.2.2) correspondant)', 'ou ce qui revient au même (inserted)', 'domine l’étude cohomologique des quatre schémas', 'en ce sens qu’il permet de retrouver formellement la cohomologie (à coefficients constants) des schémas envisagés', 'Appliquant le foncteur ``oubli de π’’ à 6.2.2, on trouve le triangle exact', 'qui donne la cohomologie (sans opérateurs) de ...', 'l’hom du premier dans le second défini par l’inclusion', 'D’autre part, appliquant le foncteur ... à (6.2.1), (6.2.2), on trouve', 'left oblique instruction about remonter/remettre the diagram and commenting it', 'avec des notations légèrement changées/modifiées p.r. à (4.2)', 'compte tenu que, par la structure précise de π=I, on a', 'twist de Tate / transl. des degrés', 'L’homomorphisme ... définit ainsi un (cancelled)', 'Ainsi on retrouve ... et l’hom h* déduit de ... n’est autre que l’hom naturel ``d’inclusion’’', 'De plus, l’hom ... se décompose en', 'Resumed independent crop reading: envisagés, triangle exact, défini par l’inclusion, structure spéciale/précise, dégén. formule (needs enlargement), naturel d’inclusion; no accent emendation inferred from grammar.']

### Checks

- **prose:** Restarted full three-crop reading after workspace recovery; earlier interrupted attempt retained separately. Compared every paragraph, the cancelled sentence and shortened words. Added doubt to appliquons/appliquant, spéciale/précise, défini/définit. Enlarged annotation is closer to dégager la formule than dégén. formule; both retained.
- **indices:** All expressions listed below compared, including R/K bullet oub, derived tensor L over Lambda_nu, pi superscripts, shift [-1], Tate twist (-1), alpha/beta and final cramped [-1]/(-1). Bars over s and eta checked separately. Arrow labels bar i (short dotted upright) and j_s/j_eta/j (descender) kept distinct; h_eta and kappa/k/h checked.
- **diagrams:** Both triangles cycle top->lower left->lower right->top. First upper right arrow has kappa*. Inclusion diagram: V_bar_s ->bar_i bar V <-coh.~ V_bar_eta, dashed curved kappa from first to third. Marginal square: V_eta points left to V, lower objects point upward, lower dashed arrow points right. Cancelled labels read beneath their strokes. Every displayed object and coefficient argument retained.
- **margins:** Slanted note reread in rotated crop: remonter/remettre ce/le diagramme et le commenter !; caption avec des notations légèrement changées p.r. à (4.2). Boxed lower right identification and its attached dégager la formule reading retained. twist de Tate and transl. des degrés are distinct annotations.
- **deletions:** et after u; overwritten R Gamma before L bullet; erased g/h_s/coh./g on square; cancelled homomorphism and unfinished arrow; cancelled R Gamma before braces K bullet. No strike interpreted as a live superscript.
- **alphabets:** Each derived R has two upright strokes; ordinary R bullet has one. Gamma/script T and pi/Pi first occurrences carry doubt, nu/v and eta/y likewise. K and L ordinary, bullet degrees distinct from starred morphisms.

### Every inline formula

1. `u`
2. `V_s\simeq V_{\bar s},V,V_{\unsure{\eta\|y}},V_{\bar\eta}`
3. `\unsure{\pi\|\Pi}`
4. `V_{\bar\eta}`
5. `V_s`
6. `\mathbb{R}\Gamma^\pi`
7. `\pi=I`
8. `\mathbb{R}\Gamma^\pi(\kappa^*)`
9. `\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)\longrightarrow`
10. `\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)`
11. `h^*`
12. `V_{\bar\eta}\xrightarrow{h}V_\eta`
13. `\mathbb{R}\Gamma^\pi(K^\bullet)\longrightarrow\deleted{\unsure{\mathbb{R}\Gamma}}\{K^\bullet\}`
14. `\mathbb{R}\Gamma^\pi(\kappa^*)`

### Every display

Display 1:

```latex
\tag*{(6.2.3)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}\unsure{\Gamma|\mathscr{T}}(V_s,\Lambda_{\unsure{\nu|v}})=L^\bullet}\arrow[dl] \& \\
{R^{\bullet\,\mathrm{oub}}=\mathbb{R}\Gamma(\bar V,\Lambda_{\nu\unsure{,|\,}V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_{\bar\eta},\Lambda_\nu)=K^{\bullet\,\mathrm{oub}}}\arrow[ul,"{\unsure{\kappa|k|h}}^*"]
\end{tikzcd}
```

Display 2:

```latex
\begin{tikzcd}[ampersand replacement=\&]
V_{\bar s}\arrow[r,"\bar i"]\arrow[rr,bend right=25,dashed,"\kappa"'] \& \bar V \& V_{\bar\eta}\arrow[l,"\sim"',"\mathrm{coh.}"]
\end{tikzcd}
```

Display 3:

```latex
\tag*{(6.2.4)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}\Gamma(V_s,\Lambda_\nu)\mathbin{\mathop{\otimes}^{\mathrm L}}_{\Lambda_\nu}\mathbb{R}\Gamma^\pi(\Lambda_\nu)\simeq\deleted{\unsure{\mathbb{R}\Gamma}}L^\bullet\oplus L^\bullet[-1]}\arrow[dl] \& \\
{\mathbb{R}\Gamma^\pi(R^\bullet)}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)\simeq\mathbb{R}\Gamma^\pi(K^\bullet)}\arrow[ul,"\mathbb{R}\Gamma^\pi(\kappa^*)\unsure{=|\sim}"]
\end{tikzcd}
```

Display 4:

```latex
\tag*{(6.2.5)}\mathbb{R}\Gamma^\pi(\Lambda_\nu)\simeq\Lambda_\nu\oplus\underbrace{\Lambda_\nu(-1)}_{\text{twist de Tate}}\overbrace{[-1]}^{\text{transl. des degrés}}.
```

Display 5:

```latex
\tag*{(6.2.6)}\mathbb{R}\Gamma^\pi(\kappa^*)=(\alpha,\beta):\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)=\mathbb{R}\Gamma^\pi(K^\bullet)\longrightarrow\mathbb{R}\Gamma(V_s,\Lambda_\nu)+\mathbb{R}\Gamma(V_s,\Lambda_\nu)\unsure{[-1]|(-1)}
```

### Diagram objects, arrows and decorations

Diagram 1, source line 6:

```latex
\[
\tag*{(6.2.3)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}\unsure{\Gamma|\mathscr{T}}(V_s,\Lambda_{\unsure{\nu|v}})=L^\bullet}\arrow[dl] \& \\
{R^{\bullet\,\mathrm{oub}}=\mathbb{R}\Gamma(\bar V,\Lambda_{\nu\unsure{,|\,}V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_{\bar\eta},\Lambda_\nu)=K^{\bullet\,\mathrm{oub}}}\arrow[ul,"{\unsure{\kappa|k|h}}^*"]
\end{tikzcd}
\]
```

Diagram 2, source line 14:

```latex
\[
\begin{tikzcd}[ampersand replacement=\&]
V_{\bar s}\arrow[r,"\bar i"]\arrow[rr,bend right=25,dashed,"\kappa"'] \& \bar V \& V_{\bar\eta}\arrow[l,"\sim"',"\mathrm{coh.}"]
\end{tikzcd}
\]
```

Diagram 3, source line 20:

```latex
\[
\tag*{(6.2.4)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}\Gamma(V_s,\Lambda_\nu)\mathbin{\mathop{\otimes}^{\mathrm L}}_{\Lambda_\nu}\mathbb{R}\Gamma^\pi(\Lambda_\nu)\simeq\deleted{\unsure{\mathbb{R}\Gamma}}L^\bullet\oplus L^\bullet[-1]}\arrow[dl] \& \\
{\mathbb{R}\Gamma^\pi(R^\bullet)}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)\simeq\mathbb{R}\Gamma^\pi(K^\bullet)}\arrow[ul,"\mathbb{R}\Gamma^\pi(\kappa^*)\unsure{=|\sim}"]
\end{tikzcd}
\]
```

Diagram 4, source line 30:

```latex
\begin{tikzcd}[ampersand replacement=\&]
V \& V_\eta\arrow[l,"\deleted{\unsure{g}}\unsure{j_s|j_\eta|j}"]\\
{V_s\simeq V_{\bar s}}\arrow[u,"\deleted{\unsure{h_s}}i"]\arrow[r,dashed,"\kappa"] \& {\bar V\overset{\deleted{\unsure{\mathrm{coh.}}}}\simeq V_{\bar\eta}}\arrow[u,"h_\eta\deleted{\unsure{g}}"']
\end{tikzcd}
```

### i and j in scripts, and scripted i/j maps

- Source line 31: `nsure{g}}\unsure{j_s\|j_\eta\|j}"]\\ {V_s\si`
- Source line 31: `e{g}}\unsure{j_s\|j_\eta\|j}"]\\ {V_s\simeq V_{`

### Margins, insertions and cancellations listed in full

**margin**

- Source line 29: `\unsure{remonter\|remettre} \unsure{ce\|le} diagramme et le commenter ! \diagram{\begin{tikzcd}[ampersand replacement=\&] V \& V_\eta\arrow[l,"\deleted{\unsure{g}}\unsure{j_s\|j_\eta\|j}"]\\ {V_s\simeq V_{\bar s}}\arrow[u,"\deleted{\unsure{h_s}}i"]\arrow[r,dashed,"\kappa"] \& {\bar V\overset{\deleted{\unsure{\mathrm{coh.}}}}\simeq V_{\bar\eta}}\arrow[u,"h_\eta\deleted{\unsure{g}}"'] \end{tikzcd}} (avec des notations légèrement changées p.r. à (4.2))`

**inserted**

- Source line 5: `ou ce qui revient au même,`
- Source line 19: `à (6.2.1), (6.2.2)`
- Source line 27: `\unsure{dégager la formule\|dégén. formule}`

**deleted**

- Source line 5: `et`
- Source line 23: `\unsure{\mathbb{R}\Gamma}`
- Source line 31: `\unsure{g}`
- Source line 32: `\unsure{h_s}`
- Source line 32: `\unsure{\mathrm{coh.}}`
- Source line 32: `\unsure{g}`
- Source line 39: `L'homomorphisme $\mathbb{R}\Gamma^\pi(\kappa^*)$ \unsure{défini\|définit} se décompose en $\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)\longrightarrow$`
- Source line 41: `\unsure{\mathbb{R}\Gamma}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -7,7 +7,7 @@
 \tag*{(6.2.3)}
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \& {\mathbb{R}\unsure{\Gamma|\mathscr{T}}(V_s,\Lambda_{\unsure{\nu|v}})=L^\bullet}\arrow[dl] \& \\
-{R^{\bullet\,\mathrm{oub}}=\mathbb{R}\Gamma(\bar V,\Lambda_{\nu\unsure{,|\,}V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_{\bar\eta},\Lambda_\nu)=K^{\bullet\,\mathrm{oub}}}\arrow[ul,"\unsure{\kappa|k}^*"]
+{R^{\bullet\,\mathrm{oub}}=\mathbb{R}\Gamma(\bar V,\Lambda_{\nu\unsure{,|\,}V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_{\bar\eta},\Lambda_\nu)=K^{\bullet\,\mathrm{oub}}}\arrow[ul,"\unsure{\kappa|k|h}^*"]
 \end{tikzcd}}
 \]
 qui donne la cohomologie (sans opérateurs) de $V_{\bar\eta}$ et $V_s$ et l'hom du premier dans le second défini par l'inclusion
@@ -16,7 +16,7 @@
 V_{\bar s}\arrow[r,"\bar i"]\arrow[rr,bend right=25,dashed,"\kappa"'] \& \bar V \& V_{\bar\eta}\arrow[l,"\sim"',"\mathrm{coh.}"]
 \end{tikzcd}}.
 \]
-D'autre part, appliquons le foncteur $\mathbb{R}\Gamma^\pi$ \inserted{à (6.2.1), (6.2.2)}, on trouve
+D'autre part, \unsure{appliquons|appliquant} le foncteur $\mathbb{R}\Gamma^\pi$ \inserted{à (6.2.1), (6.2.2)}, on trouve
 \[
 \tag*{(6.2.4)}
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
@@ -24,19 +24,19 @@
 {\mathbb{R}\Gamma^\pi(R^\bullet)}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)\simeq\mathbb{R}\Gamma^\pi(K^\bullet)}\arrow[ul,"\mathbb{R}\Gamma^\pi(\kappa^*)\unsure{=|\sim}"]
 \end{tikzcd}}
 \]
-\inserted{dégén. formule}
+\inserted{\unsure{dégager la formule|dégén. formule}}
 % margin note written slanted
 \margin{\unsure{remonter|remettre} \unsure{ce|le} diagramme et le commenter !
 \diagram{\begin{tikzcd}[ampersand replacement=\&]
-V \& V_\eta\arrow[l,"\deleted{\unsure{g}}\unsure{j_\eta|j}"]\\
+V \& V_\eta\arrow[l,"\deleted{\unsure{g}}\unsure{j_s|j_\eta|j}"]\\
 {V_s\simeq V_{\bar s}}\arrow[u,"\deleted{\unsure{h_s}}i"]\arrow[r,dashed,"\kappa"] \& {\bar V\overset{\deleted{\unsure{\mathrm{coh.}}}}\simeq V_{\bar\eta}}\arrow[u,"h_\eta\deleted{\unsure{g}}"']
 \end{tikzcd}}
 (avec des notations légèrement changées p.r. à (4.2))}
-compte tenu que, par la structure spéciale de $\pi=I$, on a
+compte tenu que, par la structure \unsure{spéciale|précise} de $\pi=I$, on a
 \[
 \tag*{(6.2.5)}\mathbb{R}\Gamma^\pi(\Lambda_\nu)\simeq\Lambda_\nu\oplus\underbrace{\Lambda_\nu(-1)}_{\text{twist de Tate}}\overbrace{[-1]}^{\text{transl. des degrés}}.
 \]
-\deleted{L'homomorphisme $\mathbb{R}\Gamma^\pi(\kappa^*)$ \unsure{défini} se décompose en
+\deleted{L'homomorphisme $\mathbb{R}\Gamma^\pi(\kappa^*)$ \unsure{défini|définit} se décompose en
 $\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)\longrightarrow$}
 Ainsi on retrouve $\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)$, et l'hom $h^*$ déduit de $V_{\bar\eta}\xrightarrow{h}V_\eta$ n'est autre que l'hom naturel ``d'inclusion'' $\mathbb{R}\Gamma^\pi(K^\bullet)\longrightarrow\deleted{\unsure{\mathbb{R}\Gamma}}\{K^\bullet\}$. De plus, l'hom $\mathbb{R}\Gamma^\pi(\kappa^*)$ se décompose en
 \[
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -3,27 +3,27 @@
 % archive sheet number: 157
 
 L'homomorphisme $u$, (\deleted{et} \inserted{ou ce qui revient au même,} le triangle (6.2.2) correspondant) domine l'étude cohomologique des quatre schémas $V_s\simeq V_{\bar s},V,V_{\unsure{\eta|y}},V_{\bar\eta}$, en ce sens qu'il permet de retrouver formellement la cohomologie (à coefficients constants) des schémas envisagés. Appliquant le foncteur ``oubli de $\unsure{\pi|\Pi}$'' à 6.2.2, on trouve le triangle exact
-\[
+\diagram{\[
 \tag*{(6.2.3)}
-\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
+\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \& {\mathbb{R}\unsure{\Gamma|\mathscr{T}}(V_s,\Lambda_{\unsure{\nu|v}})=L^\bullet}\arrow[dl] \& \\
-{R^{\bullet\,\mathrm{oub}}=\mathbb{R}\Gamma(\bar V,\Lambda_{\nu\unsure{,|\,}V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_{\bar\eta},\Lambda_\nu)=K^{\bullet\,\mathrm{oub}}}\arrow[ul,"\unsure{\kappa|k|h}^*"]
-\end{tikzcd}}
-\]
+{R^{\bullet\,\mathrm{oub}}=\mathbb{R}\Gamma(\bar V,\Lambda_{\nu\unsure{,|\,}V_{\bar\eta},\bar V})}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_{\bar\eta},\Lambda_\nu)=K^{\bullet\,\mathrm{oub}}}\arrow[ul,"{\unsure{\kappa|k|h}}^*"]
+\end{tikzcd}
+\]}
 qui donne la cohomologie (sans opérateurs) de $V_{\bar\eta}$ et $V_s$ et l'hom du premier dans le second défini par l'inclusion
-\[
-\diagram{\begin{tikzcd}[ampersand replacement=\&]
+\diagram{\[
+\begin{tikzcd}[ampersand replacement=\&]
 V_{\bar s}\arrow[r,"\bar i"]\arrow[rr,bend right=25,dashed,"\kappa"'] \& \bar V \& V_{\bar\eta}\arrow[l,"\sim"',"\mathrm{coh.}"]
-\end{tikzcd}}.
-\]
+\end{tikzcd}
+\]}.
 D'autre part, \unsure{appliquons|appliquant} le foncteur $\mathbb{R}\Gamma^\pi$ \inserted{à (6.2.1), (6.2.2)}, on trouve
-\[
+\diagram{\[
 \tag*{(6.2.4)}
-\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
+\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \& {\mathbb{R}\Gamma(V_s,\Lambda_\nu)\mathbin{\mathop{\otimes}^{\mathrm L}}_{\Lambda_\nu}\mathbb{R}\Gamma^\pi(\Lambda_\nu)\simeq\deleted{\unsure{\mathbb{R}\Gamma}}L^\bullet\oplus L^\bullet[-1]}\arrow[dl] \& \\
 {\mathbb{R}\Gamma^\pi(R^\bullet)}\arrow[rr] \& \& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)\simeq\mathbb{R}\Gamma^\pi(K^\bullet)}\arrow[ul,"\mathbb{R}\Gamma^\pi(\kappa^*)\unsure{=|\sim}"]
-\end{tikzcd}}
-\]
+\end{tikzcd}
+\]}
 \inserted{\unsure{dégager la formule|dégén. formule}}
 % margin note written slanted
 \margin{\unsure{remonter|remettre} \unsure{ce|le} diagramme et le commenter !
```

## Scan 159

Start: **2026-11-17T23:42:10.638393+00:00**. End: **2026-11-17T23:43:45.479413+00:00**.

Crop observations recorded: 2026-11-17T23:42:43.128602+00:00.

['où α ... est donné par', 'tandis que β est un hom. de degré 1', 'Cet homomorphisme peut s’interpréter, par la proposition suivante', 'qui en même temps/toujours donne un calcul de ... en termes de la donnée fondamentale', 'Proposition 6.3 a) On a', 'en d’autres termes on a', 'd’où un isom.', 'b) Considérons le triangle canonique (can. inserted)', 'Alors la flèche ∂ dans ce triangle s’identifie [via l’isomorphisme (6.3.3)] à β', 'signe ? (left margin)', 'Corollaire 6.4', 'À des signes et shifts près (inserted)', 'le triangle ... n’est autre que le triangle distingué des ``mapping-cylindres’’ du β de (6.2.8)']

### Checks

- **prose:** Three thirds read before source; prose, crossed formulas, triangle and end enlarged. Recovered cancelled avec/autre un mode de and isomorphe as uncertain readings rather than illegible words. Added en u/en de. The word shifts is legible; removed twists alternative. mapping-cylindres remains uncertain.
- **indices:** All displays and inline mathematics below compared: alpha=kappa* h*, beta/rho arrow, both (-1)[-1] at 6.2.8; cancelled +1 twist versus live -1; i !=2 and i=2; (-1)[-2] in 6.3.2 and 6.3.3; local underline H/Gamma versus global Gamma. All H degrees i have dots/no descender; j* in triangle has descender and i_* is short. Bar eta and coefficient nu/v marked first.
- **diagram:** Top R Gamma(V_eta,Lambda_nu); top->lower left partial; lower left->lower right i_*; lower right->top j*. Entire lower-left identification retained including overwritten V_s and doubtful twist/shift. Small reference under equality looks 6.3.8; 6.3.3 retained as alternative, not silently corrected.
- **margins:** signe ? read independently in left margin. Added can. at isomorphism and À des signes et shifts près at corollary followed their links.
- **deletions:** est un after alpha; cancelled Proposition heading and old calculation wording; cancelled two support-cohomology assertions with (1); middle si i row; overwritten V_s; Donc and abandoned R Gamma/isomorphe phrase; separate R Gamma fragment; construit avec before inserted des. Every crossing stroke checked against live text.
- **alphabets:** Double-stem R in all derived functors, ordinary H; Gamma/script T ambiguity first marked, kappa/k similarly. No new blackboard alphabet in heading. Bullet/star confusion does not affect the clear stars on kappa,h,j.

### Every inline formula

1. `\alpha`
2. `\beta`
3. `\mathbb{R}\Gamma(V,\Lambda_\nu)`
4. `\underline{H}^i_{V_s}(\unsure{V_s\|V},\Lambda_{\nu V})=0`
5. `i\ne2`
6. `\underline{H}^2_{V_s}(\Lambda_{\nu V})\simeq\Lambda_{\nu V_s}(1)`
7. `\partial`
8. `\beta`
9. `\mathbb{R}\Gamma(V,\Lambda_\nu)`
10. `\mathbb{R}\Gamma(V,\Lambda_\nu)`
11. `\beta`

### Every display

Display 1:

```latex
\tag*{(6.2.7)}\alpha={\unsure{\kappa|k}}^*h^*,
```

Display 2:

```latex
\tag*{(6.2.8)}\unsure{\beta|\rho}:\mathbb{R}\unsure{\Gamma|\mathscr{T}}(V_{\unsure{\eta|y}},\Lambda_{\unsure{\nu|v}})\longrightarrow\mathbb{R}\Gamma(V_s,\Lambda_\nu)(-1)[-1].
```

Display 3:

```latex
\tag*{(6.3.1)}\underline{H}^i_{V_s}(\Lambda_{\nu V})\simeq\begin{cases}
0&\text{si }i\ne2\\
\deleted{\text{si }i}&\\
\Lambda_{\nu V_s}(-1)&\text{si }i=2,
\end{cases}
```

Display 4:

```latex
\tag*{(6.3.2)}\mathbb{R}\underline\Gamma_{V_s}(\Lambda_{\nu V})\simeq\Lambda_{\nu V_s}(-1)[-2],
```

Display 5:

```latex
\tag*{(6.3.3)}\mathbb{R}\Gamma_{V_s}(V,\Lambda_\nu)\simeq\mathbb{R}\Gamma(V_s,\Lambda_\nu)(-1)[-2]\inserted{\text{ can.}}
```

Display 6:

```latex
\tag*{(6.3.4)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)}\arrow[dl,"\partial"'] \& \\
{\mathbb{R}\Gamma(V_s,\Lambda_\nu)\unsure{(-1)[-2]|[1][-2]}\underset{\text{par (\unsure{6.3.8|6.3.3})}}\simeq\mathbb{R}\Gamma_{V_s}(\deleted{\unsure{V_s}}V,\Lambda_{\nu V})}\arrow[rr,"i_*"] \& \& {\mathbb{R}\Gamma(V,\Lambda_\nu)}\arrow[ul,"j^*"]
\end{tikzcd}
```

### Diagram objects, arrows and decorations

Diagram 1, source line 33:

```latex
\[
\tag*{(6.3.4)}
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)}\arrow[dl,"\partial"'] \& \\
{\mathbb{R}\Gamma(V_s,\Lambda_\nu)\unsure{(-1)[-2]|[1][-2]}\underset{\text{par (\unsure{6.3.8|6.3.3})}}\simeq\mathbb{R}\Gamma_{V_s}(\deleted{\unsure{V_s}}V,\Lambda_{\nu V})}\arrow[rr,"i_*"] \& \& {\mathbb{R}\Gamma(V,\Lambda_\nu)}\arrow[ul,"j^*"]
\end{tikzcd}
\]
```

### i and j in scripts, and scripted i/j maps

- Source line 16: `ted{$\underline{H}^i_{V_s}(\unsure{V_s\|V},`
- Source line 16: `d{$\underline{H}^i_{V_s}(\unsure{V_s\|V},\Lambd`
- Source line 18: `3.1)}\underline{H}^i_{V_s}(\Lambda_{\nu V}`
- Source line 18: `1)}\underline{H}^i_{V_s}(\Lambda_{\nu V})\sime`
- Source line 37: `u V})}\arrow[rr,"i_*"] \& \& {\mathbb{R}\G`
- Source line 37: `_\nu)}\arrow[ul,"j^*"] \end{tikzcd} \]}. A`

### Margins, insertions and cancellations listed in full

**margin**

- Source line 41: `signe ?`

**inserted**

- Source line 30: `\text{ can.}`
- Source line 44: `À des signes et shifts près,`
- Source line 44: `des`

**deleted**

- Source line 5: `\unsure{est un}`
- Source line 13: `\uline{\unsure{Proposition}}`
- Source line 13: `\unsure{avec\|autre} \unsure{un mode de}`
- Source line 13: `\unsure{en u\|en de}`
- Source line 16: `$\underline{H}^i_{V_s}(\unsure{V_s\|V},\Lambda_{\nu V})=0$ pour $i\ne2$, et $\underline{H}^2_{V_s}(\Lambda_{\nu V})\simeq\Lambda_{\nu V_s}(1)$,`
- Source line 20: `\text{si }i`
- Source line 37: `\unsure{V_s}`
- Source line 40: `Donc $\mathbb{R}\Gamma(V,\Lambda_\nu)$ \unsure{s'identifie à} \unsure{isomorphe}`
- Source line 42: `$\mathbb{R}\Gamma(V,\Lambda_\nu)$`
- Source line 44: `construit avec`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -10,7 +10,7 @@
 \[
 \tag*{(6.2.8)}\unsure{\beta|\rho}:\mathbb{R}\unsure{\Gamma|\mathscr{T}}(V_{\unsure{\eta|y}},\Lambda_{\unsure{\nu|v}})\longrightarrow\mathbb{R}\Gamma(V_s,\Lambda_\nu)(-1)[-1].
 \]
-\deleted{\uline{\unsure{Proposition}}} Cet homomorphisme peut s'interpréter, par la proposition suivante, qui en \unsure{même temps|toujours} donne un \deleted{\unsure{autre} \illegible{2}} calcul de $\mathbb{R}\Gamma(V,\Lambda_\nu)$, en termes de la donnée fondamentale \deleted{\unsure{en de}} (6.2.1) :
+\deleted{\uline{\unsure{Proposition}}} Cet homomorphisme peut s'interpréter, par la proposition suivante, qui en \unsure{même temps|toujours} donne un \deleted{\unsure{avec|autre} \unsure{un mode de}} calcul de $\mathbb{R}\Gamma(V,\Lambda_\nu)$, en termes de la donnée fondamentale \deleted{\unsure{en u|en de}} (6.2.1) :
 
 \uline{Proposition} 6.3 a) On a
 \deleted{$\underline{H}^i_{V_s}(\unsure{V_s|V},\Lambda_{\nu V})=0$ pour $i\ne2$, et $\underline{H}^2_{V_s}(\Lambda_{\nu V})\simeq\Lambda_{\nu V_s}(1)$,}
@@ -34,11 +34,11 @@
 \tag*{(6.3.4)}
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)}\arrow[dl,"\partial"'] \& \\
-{\mathbb{R}\Gamma(V_s,\Lambda_\nu)\unsure{(-1)[-2]|[1][-2]}\underset{\text{par (6.3.3)}}\simeq\mathbb{R}\Gamma_{V_s}(\deleted{\unsure{V_s}}V,\Lambda_{\nu V})}\arrow[rr,"i_*"] \& \& {\mathbb{R}\Gamma(V,\Lambda_\nu)}\arrow[ul,"j^*"]
+{\mathbb{R}\Gamma(V_s,\Lambda_\nu)\unsure{(-1)[-2]|[1][-2]}\underset{\text{par (\unsure{6.3.8|6.3.3})}}\simeq\mathbb{R}\Gamma_{V_s}(\deleted{\unsure{V_s}}V,\Lambda_{\nu V})}\arrow[rr,"i_*"] \& \& {\mathbb{R}\Gamma(V,\Lambda_\nu)}\arrow[ul,"j^*"]
 \end{tikzcd}}.
 \]
-Alors la flèche $\partial$ du dit triangle s'identifie [via l'isomorphisme (6.3.3)] à $\beta$. \deleted{Donc $\mathbb{R}\Gamma(V,\Lambda_\nu)$ \unsure{s'identifie à} \illegible{1}}
+Alors la flèche $\partial$ du dit triangle s'identifie [via l'isomorphisme (6.3.3)] à $\beta$. \deleted{Donc $\mathbb{R}\Gamma(V,\Lambda_\nu)$ \unsure{s'identifie à} \unsure{isomorphe}}
 \margin{signe ?}
 \deleted{$\mathbb{R}\Gamma(V,\Lambda_\nu)$}
 
-\uline{Corollaire} 6.4 \inserted{À des signes et \unsure{shifts|twists} près,} Le triangle (6.3.4) n'est autre que le triangle distingué \deleted{construit avec} \inserted{des} ``\unsure{mapping-cylindres}'' du $\beta$ de (6.2.8).
+\uline{Corollaire} 6.4 \inserted{À des signes et shifts près,} Le triangle (6.3.4) n'est autre que le triangle distingué \deleted{construit avec} \inserted{des} ``\unsure{mapping-cylindres}'' du $\beta$ de (6.2.8).
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -4,7 +4,7 @@
 
 où $\alpha$ \deleted{\unsure{est un}} est donné par
 \[
-\tag*{(6.2.7)}\alpha=\unsure{\kappa|k}^*h^*,
+\tag*{(6.2.7)}\alpha={\unsure{\kappa|k}}^*h^*,
 \]
 tandis que $\beta$ est un hom. de degré 1 :
 \[
@@ -30,15 +30,15 @@
 \tag*{(6.3.3)}\mathbb{R}\Gamma_{V_s}(V,\Lambda_\nu)\simeq\mathbb{R}\Gamma(V_s,\Lambda_\nu)(-1)[-2]\inserted{\text{ can.}}
 \]
 b) Considérons le triangle canonique
-\[
+\diagram{\[
 \tag*{(6.3.4)}
-\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
+\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 \& {\mathbb{R}\Gamma(V_\eta,\Lambda_\nu)}\arrow[dl,"\partial"'] \& \\
 {\mathbb{R}\Gamma(V_s,\Lambda_\nu)\unsure{(-1)[-2]|[1][-2]}\underset{\text{par (\unsure{6.3.8|6.3.3})}}\simeq\mathbb{R}\Gamma_{V_s}(\deleted{\unsure{V_s}}V,\Lambda_{\nu V})}\arrow[rr,"i_*"] \& \& {\mathbb{R}\Gamma(V,\Lambda_\nu)}\arrow[ul,"j^*"]
-\end{tikzcd}}.
-\]
+\end{tikzcd}
+\]}.
 Alors la flèche $\partial$ du dit triangle s'identifie [via l'isomorphisme (6.3.3)] à $\beta$. \deleted{Donc $\mathbb{R}\Gamma(V,\Lambda_\nu)$ \unsure{s'identifie à} \unsure{isomorphe}}
 \margin{signe ?}
 \deleted{$\mathbb{R}\Gamma(V,\Lambda_\nu)$}
 
-\uline{Corollaire} 6.4 \inserted{À des signes et shifts près,} Le triangle (6.3.4) n'est autre que le triangle distingué \deleted{construit avec} \inserted{des} ``\unsure{mapping-cylindres}'' du $\beta$ de (6.2.8).
+\uline{Corollaire} 6.4 \inserted{À des signes et shifts près,} Le triangle (6.3.4) n'est autre que le triangle distingué \deleted{construit avec} \inserted{des} ``{\unsure{mapping-cylindres}}'' du $\beta$ de (6.2.8).
```

## Scan 160

Start: **2026-11-17T23:43:45.481337+00:00**. End: **2026-11-17T23:47:34.457270+00:00**.

Crop observations recorded: 2026-11-17T23:44:22.141128+00:00.

['Démonstration le a.', 'et induisant sur Vs ← V, et prenant les invariants par ... (all cancelled)', 'car ... (small right note)', 'd’où', 'd’où aussitôt 6.3 a), en utilisant les relations habituelles entre les ... et les ...', 'Compatibilité b) laissée au rédacteur/aux rédacteurs en forme !', 'Lower third blank except archival number 159.']

### Checks

- **formulas:** All four displays, both diagrams and both inline formulas checked from the three thirds and enlarged calculation. The apparent V coefficient in i*Rj* is retained before Lambda as the alternative; the small dash before the direct-sum sign remains uncertain. Every bar, star, twist (-1), shift [-1], pi superscript and subscript 0 checked separately.
- **indices i j:** Diagram i, bar i, j and bar j: arrows and stars checked individually. Final H has exponent i, support V_s; final double-stem R has exponent i and j_* follows. These i have no descender; j does.
- **alphabets:** All derived R stems are visibly doubled. Gamma has an angular top with uncertain script-T alternative at its first occurrence; pi/Pi marked at first occurrence. Lambda and the exceptional V-shaped coefficient distinguished.
- **deletions:** The first triangle and two following draft calculations, including the open final parenthesis, are cancelled. Crossed prose et induisant ... on a retained. Live calculation below has no cancellation through its exponents.
- **margins insertions:** Small car explanation at right belongs to the fourth line of the first live calculation. No sideways note. The lower third is blank apart from archive number 159.
- **words accents:** Démonstration, où, aussitôt, habituelles, Compatibilité and laissée checked. Last enlarged phrase favours aux rédacteurs over au rédacteur; alternatives retained.
- **typed corrections:** None: manuscript throughout.

### Every inline formula

1. `V_s\unsure{\leftarrow\|\hookleftarrow}V`
2. `\underline H^i_{V_s}(\Lambda_V)`
3. `\mathbb{R}^ij_*(\Lambda_{V_\eta})`

### Every display

Display 1:

```latex
\deleted{\mathbb{R}g_*(\Lambda_{V_{\bar\eta}})\unsure{\simeq|\ne}\mathbb{R}j_*\overbrace{\mathbb{R}h_*(\Lambda_{V_{\bar\eta}})}^{h_*(\Lambda_{V_{\bar\eta}})}}
```

Display 2:

```latex
\deleted{\mathbb{R}g_*(\Lambda_{V_{\bar\eta}})\simeq\mathbb{R}j_*\mathbb{R}h_*(}
```

Display 3:

```latex
\begin{aligned}
\mathbb{R}j_*(\Lambda_{V_\eta})&\simeq\mathbb{R}j_*\mathbb{R}{\unsure{\Gamma|\mathscr{T}}}^{\unsure{\pi|\Pi}}\mathbb{R}h_*(\Lambda_{V_{\bar\eta}})\\
&\simeq\mathbb{R}\Gamma^\pi\mathbb{R}j_*\mathbb{R}h_*(\Lambda_{V_{\bar\eta}})\\
&\simeq\mathbb{R}\Gamma^\pi\mathbb{R}g_*\mathbb{R}\bar j_*(\Lambda_{V_{\bar\eta}})\\
&\xrightarrow{\sim}\mathbb{R}\Gamma^\pi\mathbb{R}g_*(\Lambda_{\bar V})\qquad\text{car }\Lambda_{\bar V}\simeq\mathbb{R}\bar j_*\Lambda_{V_{\bar\eta}}
\end{aligned}
```

Display 4:

```latex
\begin{aligned}
i^*\mathbb{R}j_*(\unsure{V_{V_\eta}|\Lambda_{V_\eta}})&\simeq\mathbb{R}\underline\Gamma^\pi i^*\mathbb{R}g_*(\Lambda_{\bar V})\\
&\simeq\mathbb{R}\underline\Gamma^\pi\mathbb{R}g_{0*}(\Lambda_{V_{\bar s}})\\
&\simeq\mathbb{R}\underline\Gamma^\pi(\Lambda_{V_s})^{\mathrm{triv}}\\
&\simeq\Lambda_{V_s}\unsure{-|\,}\oplus\Lambda_{V_s}(-1)[-1]
\end{aligned}
```

### Diagram objects, arrows and decorations

Diagram 1, source line 8:

```latex
\begin{tikzcd}[ampersand replacement=\&]
\deleted{V_{\bar{\unsure{\eta|y}}}}\arrow[d,"\deleted{h}"']\arrow[dr,"\deleted{g}"] \& \\
\deleted{V_\eta}\arrow[r,"\deleted{j}"'] \& \deleted{V}
\end{tikzcd}
```

Diagram 2, source line 20:

```latex
\begin{tikzcd}[ampersand replacement=\&]
V_{\bar s}\arrow[r,"\bar i"]\arrow[d,"g_0"'] \& \bar V\arrow[d,"g"] \& V_{\bar\eta}\arrow[l,"\bar j"']\arrow[d,"h"]\\
V_s\arrow[r,"i"'] \& V \& V_\eta\arrow[l,"j"]
\end{tikzcd}
```

### i and j in scripts, and scripted i/j maps

- Source line 13: `eq\|\ne}\mathbb{R}j_*\overbrace{\mathbb{R}h`
- Source line 17: `)\simeq\mathbb{R}j_*\mathbb{R}h_*(} \]  \d`
- Source line 26: `igned} \mathbb{R}j_*(\Lambda_{V_\eta})&\si`
- Source line 26: `&\simeq\mathbb{R}j_*\mathbb{R}{\unsure{\Ga`
- Source line 27: `mma^\pi\mathbb{R}j_*\mathbb{R}h_*(\Lambda_`
- Source line 28: `_*\mathbb{R}\bar j_*(\Lambda_{V_{\bar\eta}`
- Source line 29: `eq\mathbb{R}\bar j_*\Lambda_{V_{\bar\eta}}`
- Source line 35: ` \begin{aligned} i^*\mathbb{R}j_*(\unsure{`
- Source line 35: `ed} i^*\mathbb{R}j_*(\unsure{V_{V_\eta}\|\L`
- Source line 35: `erline\Gamma^\pi i^*\mathbb{R}g_*(\Lambda_`
- Source line 41: ` les $\underline H^i_{V_s}(\Lambda_V)$ et `
- Source line 41: `es $\underline H^i_{V_s}(\Lambda_V)$ et les $\`
- Source line 41: `et les $\mathbb{R}^ij_*(\Lambda_{V_\eta})$`
- Source line 41: `les $\mathbb{R}^ij_*(\Lambda_{V_\eta})$.  `

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

none

**deleted**

- Source line 9: `V_{\bar{\unsure{\eta\|y}}}`
- Source line 9: `h`
- Source line 9: `g`
- Source line 10: `V_\eta`
- Source line 10: `j`
- Source line 10: `V`
- Source line 13: `\mathbb{R}g_*(\Lambda_{V_{\bar\eta}})\unsure{\simeq\|\ne}\mathbb{R}j_*\overbrace{\mathbb{R}h_*(\Lambda_{V_{\bar\eta}})}^{h_*(\Lambda_{V_{\bar\eta}})}`
- Source line 15: `et induisant sur $V_s\unsure{\leftarrow\|\hookleftarrow}V$, et prenant les invariants on a`
- Source line 17: `\mathbb{R}g_*(\Lambda_{V_{\bar\eta}})\simeq\mathbb{R}j_*\mathbb{R}h_*(`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -40,4 +40,4 @@
 \]
 d'où aussitôt 6.3. a), en utilisant les relations habituelles entre les $\underline H^i_{V_s}(\Lambda_V)$ et les $\mathbb{R}^ij_*(\Lambda_{V_\eta})$.
 
-Compatibilité b) laissée \unsure{au rédacteur|aux rédacteurs} en forme !
+Compatibilité b) laissée \unsure{aux rédacteurs|au rédacteur} en forme !
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -23,7 +23,7 @@
 \end{tikzcd}}
 \[
 \begin{aligned}
-\mathbb{R}j_*(\Lambda_{V_\eta})&\simeq\mathbb{R}j_*\mathbb{R}\unsure{\Gamma|\mathscr{T}}^{\unsure{\pi|\Pi}}\mathbb{R}h_*(\Lambda_{V_{\bar\eta}})\\
+\mathbb{R}j_*(\Lambda_{V_\eta})&\simeq\mathbb{R}j_*\mathbb{R}{\unsure{\Gamma|\mathscr{T}}}^{\unsure{\pi|\Pi}}\mathbb{R}h_*(\Lambda_{V_{\bar\eta}})\\
 &\simeq\mathbb{R}\Gamma^\pi\mathbb{R}j_*\mathbb{R}h_*(\Lambda_{V_{\bar\eta}})\\
 &\simeq\mathbb{R}\Gamma^\pi\mathbb{R}g_*\mathbb{R}\bar j_*(\Lambda_{V_{\bar\eta}})\\
 &\xrightarrow{\sim}\mathbb{R}\Gamma^\pi\mathbb{R}g_*(\Lambda_{\bar V})\qquad\text{car }\Lambda_{\bar V}\simeq\mathbb{R}\bar j_*\Lambda_{V_{\bar\eta}}
```

## Scan 161

Start: **2026-11-17T23:47:34.463051+00:00**. End: **2026-11-17T23:48:48.974216+00:00**.

Crop observations recorded: 2026-11-17T23:47:58.921631+00:00.

6.5. Utilisons maintenant les résultats du § 2, qui indiquent, [cancelled n=dim O_X0,x, preceding small strokes uncertain] pour; 6.5.1 n=dim O_X0,x; que l’on a; first vanishing H^i(V_bar eta), cancelled coefficient. Complétons cancelled; Utilisons les inserted; deux/des and la crossed; suites exactes déduites de crossed 6.3.4, la suite spectrale de Hochschild–Serre. [déduite de R Gamma ...] bracket. on trouve donc; cancelled Utilisons then Écrivons la suite exacte déduite de 6.3.4; on [cancelled trouve] voit que 6.5.4 s’exprime aussi par les relations; isom. / épimorph. and heavily cancelled bounds in 6.5.6. Independent 6 at bottom; archive 160 only.

### Checks

- **formulas:** All eight displays and two inline formulas checked, including the cancelled unfinished H line and bracketed derived-functor relation. The spectral-sequence arrow points left; colon after E_2 retained. In 6.5.3 first token 0/colon and two plain-dash/arrow alternatives preserved. 6.5.5 begins at exponent i-2 (alternative 1); no missing twist supplied in the later H^{i-1}(V_s).
- **indices i j:** Every H^i, H^{i-1}, H^{i+1}, H^{i+2}, i>n, i>n+1 and i=n read independently. In 6.5.6 source exponent is overwritten; visible i live, possible i-2 deleted. Target subscript s/eta is cancelled, not live. No index j occurs.
- **alphabets:** Local-ring O has script/calligraphic alternatives at first occurrence; all derived R have doubled left stems. Gamma/script-T, pi/Pi, star/t, eta/y candidates recorded separately. Last-source parentheses appear to contain V_s, Lambda, so that is now first candidate before (V_s)(-1).
- **deletions:** Initial si n=dim O clause, coefficient after 6.5.2, Complétons, la, 6.3.4, unfinished H line, Utilisons, formula fragment in 6.5.5, trouve, old source exponent, target subscript, old comparison and both tail corrections in 6.5.6 all checked. Dense hatch marks remain uncertain readings.
- **margins insertions:** Utilisons les inserted above cancelled Complétons. No side note; isolated bottom glyph 6 retained as uncertain. Archive 160 only in comment.
- **words accents:** résultats, déduites, Écrivons, épimorph., s’exprime checked. Added impliquent/indiquent and la relation/les relations because reduced medial/final strokes do not settle them.
- **typed corrections:** None: wholly handwritten.

### Every inline formula

1. `n=\dim{\unsure{\mathscr{O}\|\mathcal{O}}}_{X_0,x}`
2. `\mathbb{R}\unsure{\Gamma\|\mathscr{T}}(V_\eta)\simeq\mathbb{R}\Gamma^\pi\mathbb{R}\Gamma(V_{\bar\eta})`

### Every display

Display 1:

```latex
\tag*{(6.5.1)}n=\dim\mathscr{O}_{X_0,x}
```

Display 2:

```latex
\tag*{(6.5.2)}H^i(V_{\bar{\unsure{\eta|y}}})\deleted{\unsure{\Lambda|\Lambda_\nu}}=0\quad\text{si }i>n.
```

Display 3:

```latex
\deleted{H^i(V)\unsure{-|\longrightarrow}H^i(V_{\bar\eta}}
```

Display 4:

```latex
H^{\unsure{*|t}}(V_\eta)\Longleftarrow E_2^{pq}:H^p(\unsure{\pi|\Pi},H^q(V_{\bar\eta}))
```

Display 5:

```latex
\tag*{(6.5.3)}\unsure{0|:}\unsure{-|\longrightarrow}H^{i\unsure{-|+}1}(V_{\bar\eta})_\pi\longrightarrow H^i(V_\eta)\unsure{-|\longrightarrow}H^i(V_{\bar\eta})^\pi\longrightarrow0,
```

Display 6:

```latex
\tag*{(6.5.4)}H^i(V_\eta)=0\quad\text{si }i>n+1.
```

Display 7:

```latex
\tag*{(6.5.5)}\longrightarrow H^{i-\unsure{2|1}}(V_s)(-1)\deleted{\unsure{\longrightarrow H^i(V)}}\longrightarrow H^i(V)\longrightarrow H^i(V_\eta)\longrightarrow H^{i-1}(V_s)\longrightarrow H^{i\unsure{+|-}1}(V)\longrightarrow\cdots,
```

Display 8:

```latex
\tag*{(6.5.6)}\begin{aligned}
i_*:H^{\deleted{\unsure{i-2}}i}\unsure{(V_s,\Lambda)|(V_s)(-1)}&\longrightarrow H^{i+2}(V_{\deleted{\unsure{s|\eta}}})\quad\text{un isom. si }i\deleted{\unsure{\geq}}>n\deleted{\unsure{-1|+1}}\\
&\qquad\text{un épimorph. si }i=n\deleted{\unsure{-1|+1}}
\end{aligned}
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

- Source line 11: `\[ \tag*{(6.5.2)}H^i(V_{\bar{\unsure{\eta\|`
- Source line 15: `erre \[ \deleted{H^i(V)\unsure{-\|\longrigh`
- Source line 15: `\|\longrightarrow}H^i(V_{\bar\eta}} \] \[ H`
- Source line 22: `\|\longrightarrow}H^{i\unsure{-\|+}1}(V_{\bar\eta})_\pi\lon`
- Source line 22: `i\longrightarrow H^i(V_\eta)\unsure{-\|\lon`
- Source line 22: `\|\longrightarrow}H^i(V_{\bar\eta})^\pi\lon`
- Source line 26: `\[ \tag*{(6.5.4)}H^i(V_\eta)=0\quad\text{s`
- Source line 30: `}\longrightarrow H^{i-\unsure{2\|1}}(V_s)(-1)\deleted{\uns`
- Source line 30: `{\longrightarrow H^i(V)}}\longrightarrow H`
- Source line 30: `}\longrightarrow H^i(V)\longrightarrow H^i`
- Source line 30: `)\longrightarrow H^i(V_\eta)\longrightarro`
- Source line 30: `)\longrightarrow H^{i-1}(V_s)\longrightarrow H`
- Source line 30: `)\longrightarrow H^{i\unsure{+\|-}1}(V)\longrightarrow\cdo`
- Source line 35: `}\begin{aligned} i_*:H^{\deleted{\unsure{i`
- Source line 35: `gin{aligned} i_*:H^{\deleted{\unsure{i-2}}i}\unsure{(V_s,\Lambda)\|`
- Source line 35: `&\longrightarrow H^{i+2}(V_{\deleted{\unsure{s`

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

- Source line 13: `Utilisons les`

**deleted**

- Source line 5: `\unsure{si} $n=\dim{\unsure{\mathscr{O}\|\mathcal{O}}}_{X_0,x}$`
- Source line 11: `\unsure{\Lambda\|\Lambda_\nu}`
- Source line 13: `\unsure{Complétons}`
- Source line 13: `la`
- Source line 13: `6.3.4`
- Source line 15: `H^i(V)\unsure{-\|\longrightarrow}H^i(V_{\bar\eta}`
- Source line 28: `Utilisons`
- Source line 30: `\unsure{\longrightarrow H^i(V)}`
- Source line 32: `trouve`
- Source line 35: `\unsure{i-2}`
- Source line 35: `\unsure{s\|\eta}`
- Source line 35: `\unsure{\geq}`
- Source line 35: `\unsure{-1\|+1}`
- Source line 36: `\unsure{-1\|+1}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -2,7 +2,7 @@
 \mspage{V.33}
 % archive sheet number: 160
 
-6.5. Utilisons maintenant les résultats du § 2, qui impliquent, \deleted{\unsure{si} $n=\dim\unsure{\mathscr{O}|\mathcal{O}}_{X_0,x}$} pour
+6.5. Utilisons maintenant les résultats du § 2, qui \unsure{impliquent|indiquent}, \deleted{\unsure{si} $n=\dim\unsure{\mathscr{O}|\mathcal{O}}_{X_0,x}$} pour
 \[
 \tag*{(6.5.1)}n=\dim\mathscr{O}_{X_0,x}
 \]
@@ -29,10 +29,10 @@
 \[
 \tag*{(6.5.5)}\longrightarrow H^{i-\unsure{2|1}}(V_s)(-1)\deleted{\unsure{\longrightarrow H^i(V)}}\longrightarrow H^i(V)\longrightarrow H^i(V_\eta)\longrightarrow H^{i-1}(V_s)\longrightarrow H^{i\unsure{+|-}1}(V)\longrightarrow\cdots,
 \]
-on \deleted{trouve} voit que 6.5.4 s'exprime aussi par la relation :
+on \deleted{trouve} voit que 6.5.4 s'exprime aussi par \unsure{la relation|les relations} :
 \[
 \tag*{(6.5.6)}\begin{aligned}
-i_*:\unsure{H^{\deleted{\unsure{i-2}}i}(V_s)(-1)|H^i(V_s,\Lambda)}&\longrightarrow H^{i+2}(V_{\deleted{\unsure{s|\eta}}})\quad\text{un isom. si }i\deleted{\unsure{\geq}}>n\deleted{\unsure{-1|+1}}\\
+i_*:H^{\deleted{\unsure{i-2}}i}\unsure{(V_s,\Lambda)|(V_s)(-1)}&\longrightarrow H^{i+2}(V_{\deleted{\unsure{s|\eta}}})\quad\text{un isom. si }i\deleted{\unsure{\geq}}>n\deleted{\unsure{-1|+1}}\\
 &\qquad\text{un épimorph. si }i=n\deleted{\unsure{-1|+1}}
 \end{aligned}
 \]
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -2,7 +2,7 @@
 \mspage{V.33}
 % archive sheet number: 160
 
-6.5. Utilisons maintenant les résultats du § 2, qui \unsure{impliquent|indiquent}, \deleted{\unsure{si} $n=\dim\unsure{\mathscr{O}|\mathcal{O}}_{X_0,x}$} pour
+6.5. Utilisons maintenant les résultats du § 2, qui \unsure{impliquent|indiquent}, \deleted{\unsure{si} $n=\dim{\unsure{\mathscr{O}|\mathcal{O}}}_{X_0,x}$} pour
 \[
 \tag*{(6.5.1)}n=\dim\mathscr{O}_{X_0,x}
 \]
```

## Scan 162

Start: **2026-11-17T23:48:48.980318+00:00**. End: **2026-11-17T23:50:42.867023+00:00**.

Crop observations recorded: 2026-11-17T23:49:12.981875+00:00.

6.6. Utilisant les résultats du § 5, on trouve; 6.6.1 des isom. si i≤n−2, des mon. si i=n−1; a small limit H^i(V(m)) inserted below middle group. En toute générisation [stricte ... cancelled] x′ de x dans V−V_s=V_eta; X équidimensionnel (de dim n+1) en x. Repeated H^0(V_s) in both top vanishing rows. 6.7 cancelled Supposons, then Supposons [cancelled en plus?] x point maximal de l’un des points de non-lissité de f dans X, donc ... X régulier en toute générisation stricte de x. Lower Poincaré sentence heavily revised: satisfont, deleted à la dualité, inserted sont/ont des espaces, pour les dim; both en dim and de dim struck. Par suite si X est une int. compl. en x, de plus inserted; on déduit de 6.6.2; final n-dependent ranges and parenthetical top degrees inserted to right. Blank lower area except archive number 161.

### Checks

- **formulas:** Three numbered displays and both inserted cohomology displays checked symbol by symbol, plus all inline variables and cohomology expressions. In 6.6.1 restored visible dot after V as V./V doubt, small vertical comparison above the limit as wr/Vert, and rightward limit arrow (no m subscript is visible). In 6.6.2 retained repeated H^0(V_s) in the second row, restored right-hand separator bar and circled si. All zero, degree ranges, twists and n≥ bounds individually checked.
- **indices i j:** All H exponents i and 0 have no descenders. The q/bullet in the prose is separately doubtful; later q is retained as first candidate. Degrees n−1,n,n+1,2n−1,2n+1 inspected individually. No j index.
- **alphabets:** Ordinary H, X, V and Lambda, with eta/y at first barred occurrence. X_0/X at the right of 6.6.2 is cramped and remains marked. No derived R or Gamma appears on this page.
- **deletions:** Cancelled strict-generation words at far right enlarged, including two densely hatched X_0 candidates. Initial Supposons, enfin, à la dualité, de dim, en dim, on trouve and the old conditions beside inserted final groups retained. No sign hidden under cancellation promoted to live text.
- **margins insertions:** The caret for de plus points between est and une; moved there. Inserted sont des espaces/ont des espaces retains both candidates and preceding live satisfont. pour les dim is attached before dimensions. Both bottom insertions retained with their brackets; first has no visible terminal closing bracket, rendered with invisible right delimiter.
- **words accents:** Utilisant, résultats, générisation, équidimensionnel, complète, régulier, Poincaré, à fortiori checked from enlarged prose. l’ens and non lissité retained without expansion/hyphen normalization.
- **syntax only:** Changed the second inserted display’s first right delimiter to middle so its final right bracket is syntactically paired; first inserted bracket uses invisible right delimiter after the separator.
- **typed corrections:** None: entirely handwritten.

### Every inline formula

1. `x`
2. `f`
3. `X`
4. `X`
5. `x`
6. `H^{\unsure{q\|\bullet}}(V_s)`
7. `H^q(V)`
8. `2n-1`
9. `2n+1`
10. `X`
11. `x`
12. `\left[\begin{aligned}&\text{et }H^0(V_s)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq2}}\\&H^{2n-1}(V_s)\simeq\Lambda(-n\unsure{+\|-}1)\ \deleted{\unsure{\text{et}}}\end{aligned}\middle\|\text{si }n\geq2\right.`
13. `\left[\begin{aligned}&\text{et }H^0(V)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq1}}\\&H^{2n+1}(V)\simeq\Lambda(-n-1)\end{aligned}\middle\|\text{si }n\geq1\right]`

### Every display

Display 1:

```latex
\tag*{(6.6.1)}\left\{\begin{aligned}
&H^i(\unsure{V.|V})\longrightarrow\underset{\inserted{\begin{gathered}\unsure{\wr|\Vert}\\(\varinjlim H^i(V(m)))\end{gathered}}}{H^i(V_{\bar{\unsure{\eta|y}}})}\longrightarrow H^i(V_s)\qquad\begin{array}{l}\text{des isom si }i\leq n-2\\\text{des mon si }i=n-1\end{array}\\
&\text{\textcircled{si}}\ X\text{ est une intersection complète en toute générisation}\ \deleted{\unsure{stricte}~\unsure{x}\ \unsure{X_0}}\\
&\qquad\inserted{x'\text{ de }x\text{ dans }V-V_s=V_\eta}\ \deleted{\unsure{X_0}}\\
&\text{et si }X\text{ est équidimensionnel (de dim }n+1)\text{ en }x
\end{aligned}\right.
```

Display 2:

```latex
\tag*{(6.6.2)}\left\{\begin{aligned}
H^i(V_s)&=0\quad\text{si }0<i\leq n-2\qquad(H^0(V_s)\simeq\Lambda\text{ si }n\geq2)\\
H^i(V)&=0\quad\text{si }0<i\leq n-1\qquad(H^0(V_s)\simeq\Lambda\text{ si }n\geq1)\\
H^i(V_{\bar\eta})&=0\quad\text{si }i\ne0,n\\
H^i(V_\eta)&=0\quad\text{si }i\ne0,1,n,n+1
\end{aligned}\right|\quad\text{\textcircled{si}}\ \unsure{X_0|X}\text{ intersection complète en }x
```

Display 3:

```latex
\tag*{(6.7.1)}\left\{\begin{aligned}
H^i(V_s)&=0\quad\text{si }i\ne0,n-1,n,2n-1\\
H^i(V)&=0\quad\text{si }i\ne0,n,n+1,2n+1
\end{aligned}\right.
```

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

- Source line 8: `\begin{aligned} &H^i(\unsure{V.\|V})\longri`
- Source line 8: `rt}\\(\varinjlim H^i(V(m)))\end{gathered}}`
- Source line 8: `\end{gathered}}}{H^i(V_{\bar{\unsure{\eta\|`
- Source line 8: `}\longrightarrow H^i(V_s)\qquad\begin{arra`
- Source line 16: `{\begin{aligned} H^i(V_s)&=0\quad\text{si `
- Source line 17: `t{ si }n\geq2)\\ H^i(V)&=0\quad\text{si }0`
- Source line 18: `t{ si }n\geq1)\\ H^i(V_{\bar\eta})&=0\quad`
- Source line 19: `xt{si }i\ne0,n\\ H^i(V_\eta)&=0\quad\text{`
- Source line 27: `{\begin{aligned} H^i(V_s)&=0\quad\text{si `
- Source line 28: `ne0,n-1,n,2n-1\\ H^i(V)&=0\quad\text{si }i`

### Margins, insertions and cancellations listed in full

**margin**

none

**inserted**

- Source line 8: `\begin{gathered}\unsure{\wr\|\Vert}\\(\varinjlim H^i(V(m)))\end{gathered}`
- Source line 10: `x'\text{ de }x\text{ dans }V-V_s=V_\eta`
- Source line 24: `\unsure{sont des espaces\|ont des espaces}`
- Source line 24: `\unsure{pour les dim}`
- Source line 24: `de plus`
- Source line 31: `$\left[\begin{aligned}&\text{et }H^0(V_s)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq2}}\\&H^{2n-1}(V_s)\simeq\Lambda(-n\unsure{+\|-}1)\ \deleted{\unsure{\text{et}}}\end{aligned}\middle\|\text{si }n\geq2\right.$`
- Source line 32: `$\left[\begin{aligned}&\text{et }H^0(V)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq1}}\\&H^{2n+1}(V)\simeq\Lambda(-n-1)\end{aligned}\middle\|\text{si }n\geq1\right]$`

**deleted**

- Source line 9: `\unsure{stricte}~\unsure{x}\ \unsure{X_0}`
- Source line 10: `\unsure{X_0}`
- Source line 23: `Supposons`
- Source line 24: `enfin`
- Source line 24: `à la dualité`
- Source line 24: `\unsure{de dim}`
- Source line 24: `en dim`
- Source line 24: `\unsure{on trouve}`
- Source line 31: `\text{si }\unsure{n\geq2}`
- Source line 31: `\unsure{\text{et}}`
- Source line 32: `\text{si }\unsure{n\geq1}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -5,8 +5,8 @@
 6.6. Utilisant les résultats du § 5, on trouve
 \[
 \tag*{(6.6.1)}\left\{\begin{aligned}
-&H^i(V)\longrightarrow\underset{\inserted{(\underset m{\lim}\,H^i(V(m)))}}{H^i(V_{\bar{\unsure{\eta|y}}})}\longrightarrow H^i(V_s)\qquad\begin{array}{l}\text{des isom si }i\leq n-2\\\text{des mon si }i=n-1\end{array}\\
-&\text{si }X\text{ est une intersection complète en toute générisation}\ \deleted{\unsure{stricte}~\unsure{x}\ \unsure{X_0}}\\
+&H^i(\unsure{V.|V})\longrightarrow\underset{\inserted{\begin{gathered}\unsure{\wr|\Vert}\\(\varinjlim H^i(V(m)))\end{gathered}}}{H^i(V_{\bar{\unsure{\eta|y}}})}\longrightarrow H^i(V_s)\qquad\begin{array}{l}\text{des isom si }i\leq n-2\\\text{des mon si }i=n-1\end{array}\\
+&\text{\textcircled{si}}\ X\text{ est une intersection complète en toute générisation}\ \deleted{\unsure{stricte}~\unsure{x}\ \unsure{X_0}}\\
 &\qquad\inserted{x'\text{ de }x\text{ dans }V-V_s=V_\eta}\ \deleted{\unsure{X_0}}\\
 &\text{et si }X\text{ est équidimensionnel (de dim }n+1)\text{ en }x
 \end{aligned}\right.
@@ -17,16 +17,16 @@
 H^i(V)&=0\quad\text{si }0<i\leq n-1\qquad(H^0(V_s)\simeq\Lambda\text{ si }n\geq1)\\
 H^i(V_{\bar\eta})&=0\quad\text{si }i\ne0,n\\
 H^i(V_\eta)&=0\quad\text{si }i\ne0,1,n,n+1
-\end{aligned}\right.\quad\text{si }\unsure{X_0|X}\text{ intersection complète en }x
+\end{aligned}\right|\quad\text{\textcircled{si}}\ \unsure{X_0|X}\text{ intersection complète en }x
 \]
 
 \deleted{Supposons}
-6.7. Supposons \deleted{enfin} $x$ point maximal de l'ens des points de non lissité de $f$ \uline{dans $X$}, donc à fortiori $X$ régulier en toute générisation stricte de $x$. Alors $H^{\unsure{q|\bullet}}(V_s)$ et $H^q(V)$ satisfont \deleted{à la dualité} \inserted{\unsure{ont des espaces|sont des espaces}} de Poincaré, \deleted{\unsure{de dim}}\inserted{\unsure{pour les dim}} \deleted{en dim} $2n-1$ et $2n+1$ resp ; Par suite si $X$ est une \inserted{de plus} int. compl. en $x$, on déduit de 6.6.2 ; \deleted{\unsure{on trouve}}
+6.7. Supposons \deleted{enfin} $x$ point maximal de l'ens des points de non lissité de $f$ \uline{dans $X$}, donc à fortiori $X$ régulier en toute générisation stricte de $x$. Alors $H^{\unsure{q|\bullet}}(V_s)$ et $H^q(V)$ satisfont \deleted{à la dualité} \inserted{\unsure{sont des espaces|ont des espaces}} de Poincaré, \deleted{\unsure{de dim}}\inserted{\unsure{pour les dim}} \deleted{en dim} $2n-1$ et $2n+1$ resp ; Par suite si $X$ est \inserted{de plus} une int. compl. en $x$, on déduit de 6.6.2 ; \deleted{\unsure{on trouve}}
 \[
 \tag*{(6.7.1)}\left\{\begin{aligned}
 H^i(V_s)&=0\quad\text{si }i\ne0,n-1,n,2n-1\\
 H^i(V)&=0\quad\text{si }i\ne0,n,n+1,2n+1
 \end{aligned}\right.
 \]
-\inserted{$\left[\begin{aligned}&\text{et }H^0(V_s)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq2}}\\&H^{2n-1}(V_s)\simeq\Lambda(-n\unsure{+|-}1)\ \deleted{\unsure{\text{et}}}\end{aligned}\right|\text{si }n\geq2$}
-\inserted{$\left[\begin{aligned}&\text{et }H^0(V)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq1}}\\&H^{2n+1}(V)\simeq\Lambda(-n-1)\end{aligned}\right|\text{si }n\geq1\right]$}
+\inserted{$\left[\begin{aligned}&\text{et }H^0(V_s)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq2}}\\&H^{2n-1}(V_s)\simeq\Lambda(-n\unsure{+|-}1)\ \deleted{\unsure{\text{et}}}\end{aligned}\middle|\text{si }n\geq2\right.$}
+\inserted{$\left[\begin{aligned}&\text{et }H^0(V)\simeq\Lambda\ \deleted{\text{si }\unsure{n\geq1}}\\&H^{2n+1}(V)\simeq\Lambda(-n-1)\end{aligned}\middle|\text{si }n\geq1\right]$}
```

## Scan 164

Start: **2026-11-17T23:50:42.872444+00:00**. End: **2026-11-17T23:52:02.642418+00:00**.

Crop observations recorded: 2026-11-17T23:51:04.383134+00:00.

New numbered section VI/VII, singular Groupe de monodromie et groupe fondamental, with (*) and handwritten page 1. Dans les exposés précédents nous avons étudié; val. discr. str. local; Il y a lieu également d’étudier; topologique; Dans le présent exposé nous nous intéresserons surtout ... relativement à un pt géom.; Énoncé des résultats over cancelled Résultats. Pour un groupe profini pi, nous désignerons par la suite par pi^(p′) le plus grand quotient profini de pi premier à p; soit p′=P−{p}, et p est l’exp.; i.e. k de car. nulle; autrement c’est le quotient par le sous-groupe fermé distingué engendré par un/son p-ss-groupe de Sylow; formation évidemment fonctorielle. Last line stops after autos intérieurs de pi. Sideways starred footnote requires rotated reading.

### Checks

- **formulas:** Every inline formula checked, including cancelled pi_1 exponent p/p′ and X_K, inertia I=Gal(bar K/K), fundamental-group basepoint xi/zeta, all pi^(p′), p′=blackboard P−{p}, k=k(V), p=1. Parentheses and prime positions kept. No display or diagram on this page.
- **indices i j:** Only numerical subscript 1 on pi; no i/j exponent. I has long capital top and bottom bars, not lower-case l.
- **alphabets:** First pi/Pi and xi/zeta marked; remaining occurrences follow the first candidates. The prime-number P is visibly double-stemmed. K is roman with bars where visible; I is ordinary roman capital. Section numeral VI/VII remains uncertain after close inspection.
- **deletions:** Initial dense hatch physically obscures approximately one word even enlarged; illegible{1} retained. Crossed l’ac, les gpes, associés, Nous désignerons ... le, and Résultats retained, no crossed word left live.
- **margins insertions:** Sideways starred note rotated and read letter by letter: Le présent exposé n’est pas nécessaire pour la compréhension du reste du séminaire. Both p′ and characteristic-zero explanations are insertions attached by long guide curves. First insertion’s lead abbreviation uncertain i.e./soit.
- **words accents:** exposés, précédents, étudié, également, présent, Énoncé, désignerons, fermé, engendré, évidemment, intérieurs, compréhension and séminaire checked. Added missing underline on first engendré. Final discr. punctuation uncertain. Singular title and incomplete final sentence retained.
- **typed corrections:** None: entirely handwritten.

### Every inline formula

1. `(*)`
2. `X`
3. `K`
4. `V`
5. `I=\operatorname{Gal}(\bar K/K)`
6. `X_{\bar K}`
7. `I`
8. `X_{\bar K}`
9. `I`
10. `{\unsure{\pi\|\Pi}}_1(X_{\bar K},\unsure{\xi\|\zeta})`
11. `\xi`
12. `\bar K`
13. `\pi_1^{(\unsure{p\|p'})}(X_K,\xi)`
14. `\pi`
15. `\pi^{(p')}`
16. `\pi`
17. `p`
18. `p'=\mathbb{P}-\{p\}`
19. `p`
20. `k=k(V)`
21. `p=1`
22. `k`
23. `\pi^{(p')}=\pi`
24. `\pi^{(p')}`
25. `\pi`
26. `p`
27. `\pi`
28. `p`
29. `\pi`
30. `(*)`
31. `\pi^{(p')}`
32. `\pi`
33. `\pi`

### Every display

none

### Diagram objects, arrows and decorations

none

### i and j in scripts, and scripted i/j maps

- Source line 7: `signerons par $\pi_1^{(\unsure{p\|p'})}(X_K`
- Source line 11: ` la suite par $\pi^{(p')}$ le plus grand quotie`
- Source line 11: ` nulle,} on a $\pi^{(p')}=\pi$, sinon $\pi^{(p'`
- Source line 11: `}=\pi$, sinon $\pi^{(p')}$ est le quotient de $`
- Source line 15: ` formation de $\pi^{(p')}$ est évidemment fonct`

### Margins, insertions and cancellations listed in full

**margin**

- Source line 13: `$(*)$ Le présent exposé n'est pas nécessaire pour la compréhension du reste du séminaire.`

**inserted**

- Source line 11: `(\unsure{i.e.\|soit} $p'=\mathbb{P}-\{p\}$, et)`
- Source line 11: `i.e. $k$ de car. nulle,`

**deleted**

- Source line 7: `\illegible{1}`
- Source line 7: `l'ac`
- Source line 7: `les gpes`
- Source line 7: `\unsure{associés}`
- Source line 7: `Nous désignerons par $\pi_1^{(\unsure{p\|p'})}(X_K,\xi)$ le`
- Source line 9: `\unsure{Résultats}`

No typed-page handwritten corrections: this scan is handwritten throughout.

### Reading changes (before → after)

```diff
--- before
+++ after
@@ -4,11 +4,11 @@
 
 \unsure{VI|VII} \uline{Groupe de monodromie et groupe fondamental} $(*)$.
 
-\deleted{\illegible{1}} Dans les exposés précédents, nous avons étudié, \deleted{l'ac} pour un schéma de type fini $X$ sur $K$ (corps des fractions de l'anneau de val. discr. str. local $V$), l'action du groupe d'inertie $I=\operatorname{Gal}(\bar K/K)$ sur les gpes de cohomologie de $X_{\bar K}$. Il y a lieu également d'étudier l'action de $I$ sur \deleted{les gpes} d'autres invariants de nature topologique \deleted{\unsure{associés}} de $X_{\bar K}$. Dans le présent exposé, nous nous intéresserons surtout, à l'action de $I$ sur le groupe fondamental $\unsure{\pi|\Pi}_1(X_{\bar K},\unsure{\xi|\zeta})$ (relativement à un pt géom $\xi$ de $\bar K$). \deleted{Nous désignerons par $\pi_1^{(\unsure{p|p'})}(X_K,\xi)$ le}
+\deleted{\illegible{1}} Dans les exposés précédents, nous avons étudié, \deleted{l'ac} pour un schéma de type fini $X$ sur $K$ (corps des fractions de l'anneau de val. \unsure{discr.|discr} str. local $V$), l'action du groupe d'inertie $I=\operatorname{Gal}(\bar K/K)$ sur les gpes de cohomologie de $X_{\bar K}$. Il y a lieu également d'étudier l'action de $I$ sur \deleted{les gpes} d'autres invariants de nature topologique \deleted{\unsure{associés}} de $X_{\bar K}$. Dans le présent exposé, nous nous intéresserons surtout, à l'action de $I$ sur le groupe fondamental $\unsure{\pi|\Pi}_1(X_{\bar K},\unsure{\xi|\zeta})$ (relativement à un pt géom $\xi$ de $\bar K$). \deleted{Nous désignerons par $\pi_1^{(\unsure{p|p'})}(X_K,\xi)$ le}
 
 1. \deleted{\unsure{Résultats}}\uline{Énoncé des résultats}.
 
-1.1. Pour un groupe profini $\pi$, nous désignerons par la suite par $\pi^{(p')}$ le plus grand quotient pro-fini de $\pi$ premier à $p$ \inserted{(i.e. $p'=\mathbb{P}-\{p\}$, et)} (où $p$ est l'exp. car. de $k=k(V)$). Donc si $p=1$, \inserted{i.e. $k$ de car. nulle,} on a $\pi^{(p')}=\pi$, sinon $\pi^{(p')}$ est le quotient de $\pi$ par le ss-gpe invariant fermé engendré par \unsure{un|son} $p$-ss-groupe de Sylow, i.e. le quotient de $\pi$ par le ss-gpe engendré par les $p$-ss-groupes de Sylow de $\pi$.
+1.1. Pour un groupe profini $\pi$, nous désignerons par la suite par $\pi^{(p')}$ le plus grand quotient pro-fini de $\pi$ premier à $p$ \inserted{(\unsure{i.e.|soit} $p'=\mathbb{P}-\{p\}$, et)} (où $p$ est l'exp. car. de $k=k(V)$). Donc si $p=1$, \inserted{i.e. $k$ de car. nulle,} on a $\pi^{(p')}=\pi$, sinon $\pi^{(p')}$ est le quotient de $\pi$ par le ss-gpe invariant fermé \uline{engendré} par \unsure{un|son} $p$-ss-groupe de Sylow, i.e. le quotient de $\pi$ par le ss-gpe engendré par les $p$-ss-groupes de Sylow de $\pi$.
 % margin note written sideways
 \margin{$(*)$ Le présent exposé n'est pas nécessaire pour la compréhension du reste du séminaire.}
```

### Syntax / assembly preparation

Timestamp: 2026-11-17T23:58:47.071603+00:00. Grouping and diagram-wrapper changes do not select a different reading. Cote marker moved to the assembly header on scan 149.

```diff
--- before
+++ after
@@ -4,7 +4,7 @@
 
 \unsure{VI|VII} \uline{Groupe de monodromie et groupe fondamental} $(*)$.
 
-\deleted{\illegible{1}} Dans les exposés précédents, nous avons étudié, \deleted{l'ac} pour un schéma de type fini $X$ sur $K$ (corps des fractions de l'anneau de val. \unsure{discr.|discr} str. local $V$), l'action du groupe d'inertie $I=\operatorname{Gal}(\bar K/K)$ sur les gpes de cohomologie de $X_{\bar K}$. Il y a lieu également d'étudier l'action de $I$ sur \deleted{les gpes} d'autres invariants de nature topologique \deleted{\unsure{associés}} de $X_{\bar K}$. Dans le présent exposé, nous nous intéresserons surtout, à l'action de $I$ sur le groupe fondamental $\unsure{\pi|\Pi}_1(X_{\bar K},\unsure{\xi|\zeta})$ (relativement à un pt géom $\xi$ de $\bar K$). \deleted{Nous désignerons par $\pi_1^{(\unsure{p|p'})}(X_K,\xi)$ le}
+\deleted{\illegible{1}} Dans les exposés précédents, nous avons étudié, \deleted{l'ac} pour un schéma de type fini $X$ sur $K$ (corps des fractions de l'anneau de val. \unsure{discr.|discr} str. local $V$), l'action du groupe d'inertie $I=\operatorname{Gal}(\bar K/K)$ sur les gpes de cohomologie de $X_{\bar K}$. Il y a lieu également d'étudier l'action de $I$ sur \deleted{les gpes} d'autres invariants de nature topologique \deleted{\unsure{associés}} de $X_{\bar K}$. Dans le présent exposé, nous nous intéresserons surtout, à l'action de $I$ sur le groupe fondamental ${\unsure{\pi|\Pi}}_1(X_{\bar K},\unsure{\xi|\zeta})$ (relativement à un pt géom $\xi$ de $\bar K$). \deleted{Nous désignerons par $\pi_1^{(\unsure{p|p'})}(X_K,\xi)$ le}
 
 1. \deleted{\unsure{Résultats}}\uline{Énoncé des résultats}.
```

## Reconciliation and structural check

First-occurrence doubt markers were reconciled across the sequence for Phi/varphi, nu/v, eta/y, script/calligraphic O, Gamma/script T, pi/Pi, the covering parameter, and the prime-set alphabet. Distinctly drawn star/alpha, ordinary R versus derived double-stem R, map kappa versus complex K, and visible deviations were not forced to agree. The complete notation table is at the top of K34-09_doubts.md.

The structural checker passed every page, the assembly and standalone wrapper. It checks braces, display delimiters, dollar pairs, nested environments, left/right counts and tikzcd ampersand replacement. It does not compile, verify page layout or prove mathematical correctness. See K34-09_balance.json and the included read-only check script.

# Independent second reading

Each section records a fresh image-first reading before opening that page’s draft, then comparison and changes. All times are UTC. No OCR or compilation was used. Archive numbering is recorded only in TeX comments. All sheets are handwritten; there are no corrections on typed text.

## Scan 083

Start: 2026-11-17T23:45:24.910244+00:00  
End: 2026-11-17T23:46:32.321458+00:00

### Observations recorded before opening the page file

Image-first notes: virtually no prose or accents; Dr and Pl are two-letter forms, not expanded. The two struck connectors before matrices look like et:/d'où (still doubtful). Top flag's third glyph looks h or joined f2. s3 has a true prime, upper-right drawing has two primes. The factor before lambda in the parenthesized s3' formula is nu/gamma-shaped. Numeric subscripts throughout, no i or j. All point/vector maps point right. The crossed term after s3'= with a question above remains opaque. Last column of sigma0 has a heavily overwritten top entry. Lower vector parenthesis is visibly unfinished. Archive 82.

### Comparison, corrections, and nearby strokes

Compared all flag constraints, point maps, vector maps, both drawings, and three 4 by 4 matrices. The top flag f2/h ambiguity remains. The small apparent equality after s3 prime has a question above and a cancellation below; the cancellation is not live. The underlining under -e1+e3 is retained. Rechecked the crossed connector before each of the first two matrices and the overwritten top-right sigma0 entry; none became secure. No prose accents to normalize. The unfinished parenthesis after the sigma1 vector formula is preserved. Both drawings retain all six labels on the larger sketch, the three sigma labels, dashed continuations, central point, and the smaller drawing's heavy edges.

### Indices and exponents

All numeric 0,1,2,3 subscripts in constraints and point/vector actions checked independently. No i or j index occurs. s3 prime and double prime in the drawing are separate from the lower 3. Squaring does not occur. Matrix rows checked as written, including the uncertain last entry of row 1 of sigma0.

### Margins, insertions, and handwriting

No textual marginal note. Cancelled connectors, the cancelled e0/e2, and questioned cancelled s3-expression all remain inside deleted. Dr and Pl are live, with no line crossing them.

### Alphabet candidates

R is plain roman-shaped, not script or double struck. Dr/Pl capitals plain. The final flag glyph permits f2/h; nu versus gamma before lambda remains explicit. No capital alphabet change.

### Changes

No change.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 5:

```latex
\[
R=(\unsure{f_0},\unsure{f_1},\unsure{f_2|h})
\qquad
\left\{\begin{aligned}
\sigma_0f_0&\ne f_0,\quad \sigma_0f_1=f_1,\quad \sigma_0f_2=f_2\\
\sigma_1f_0&=f_0,\quad \sigma_1f_1\ne f_1,\quad \sigma_1f_2=f_2\\
\sigma_2f_0&=f_0,\quad \sigma_2f_1=f_1
\end{aligned}\right.
\]
```

2. TeX line 21:

```latex
$s_0$
```

3. TeX line 21:

```latex
$s_1$
```

4. TeX line 23:

```latex
\[
\begin{aligned}
s_0,\quad s_1&=\sigma_0s_0\\
s_2&=\sigma_1s_1\\
s_3&=\sigma_2s_2
\end{aligned}
\qquad
\begin{aligned}
f_1&=\mathrm{Dr}(s_0,s_1)\\
f_2&=\mathrm{Pl}(s_0,s_1,s_2)
\end{aligned}
\]
```

5. TeX line 44:

```latex
$s_0$
```

6. TeX line 44:

```latex
$s_1$
```

7. TeX line 44:

```latex
$s_2$
```

8. TeX line 45:

```latex
$s_3$
```

9. TeX line 45:

```latex
$s'_3$
```

10. TeX line 45:

```latex
$s''_3$
```

11. TeX line 46:

```latex
$\sigma_1$
```

12. TeX line 46:

```latex
$\sigma_0$
```

13. TeX line 46:

```latex
$\sigma_2$
```

14. TeX line 48:

```latex
\[
\left\{\begin{aligned}e_1&=s_1-s_0\\e_2&=s_2-s_0\\e_3&=s_3-s_0\end{aligned}\right.
\qquad
\begin{aligned}
\sigma_0:\quad&s_0\mapsto s_1\\&s_1\mapsto s_0\\&s_2\mapsto s_2\\&s_3\mapsto s_3\\[3pt]
\sigma_1:\quad&s_0\mapsto s_0\\&s_1\mapsto s_2\\&s_2\mapsto s_1\\&s_3\mapsto s'_3\overset{?}{=}\deleted{\unsure{s_3-|2s_3-}}\\[3pt]
\sigma_2:\quad&s_0\mapsto s_0\\&s_1\mapsto s_1\\&s_2\mapsto s_3\\&s_3\mapsto s_2
\end{aligned}
\]
```

15. TeX line 57:

```latex
\[
s'_3=s_0+\lambda e_1+\mu e_2+\nu e_3
\quad(=s_0+\lambda e_1-\unsure{\nu\lambda|\gamma\lambda}e_2+\nu e_3)
\]
```

16. TeX line 62:

```latex
\[
\sigma_0:\left\{\begin{aligned}e_1&\mapsto-e_1\\e_2&\mapsto-e_1+e_2\\e_3&\mapsto\underline{-e_1+e_3}\end{aligned}\right.
\qquad
\deleted{\unsure{\text{et :}}}\quad
\sigma_0=\begin{pmatrix}-1&-1&-1&\unsure{1|0}\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
\]
```

17. TeX line 68:

```latex
\[
\sigma_1:\left\{\begin{aligned}e_1&\mapsto\deleted{\unsure{e_0|e_2}}\ e_2\\e_2&\mapsto e_1\\e_3&\mapsto\lambda e_1+\mu e_2+\nu e_3\\&\quad(=\lambda e_1-\lambda e_2+e_3\end{aligned}\right.
\qquad
\deleted{\unsure{\text{d'où}}}\quad
\sigma_1=\begin{pmatrix}0&1&\lambda&0\\1&0&\mu&0\\0&0&\nu&0\\0&0&0&1\end{pmatrix}
\]
```

18. TeX line 74:

```latex
\[
\sigma_2:\left\{\begin{aligned}e_1&\mapsto e_1\\e_2&\mapsto e_3\\e_3&\mapsto e_2\end{aligned}\right.
\qquad
\sigma_2=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix}.
\]
```


## Scan 084

Start: 2026-11-17T23:46:32.341495+00:00  
End: 2026-11-17T23:47:43.233649+00:00

### Observations recorded before opening the page file

Image-first words/accents: Écrivons; la relation/les relations; évidentes; Il suffit d'écrire; Les conditions sont; compte tenu de 2°; qui résulte de 1°; Sur un corps; se décomposent; deux possibilités; Notons que; donc si on veut; (i.e. si on veut sigma1 une réflexion); On aura alors; crossed donc; On posera; de sorte qu'on aura. In the slanted note: On peut prouver en tous les cas nu=1, en écrivant u^3=id; the ending chains remain weak. Formula after sigma1²(s3) has a tiny superscript looking star/4/prime. The inserted difference visibly has a plus-shaped separator but could be a crossed minus. First two conditions boxed together; third outside. No i/j indices. Archive 83.

### Comparison, corrections, and nearby strokes

Read all three thirds, then the slanted note rotated into its writing direction and an enlarged lower prose crop. Checked the involution/commutation preface, sigma1²(s3), each expanded coefficient, all three conditions and their degree labels, both cases, determinant formula, underbraced difference, and (1),(2). The tiny upper mark on s3 remains * /4/prime. The inserted difference separator looks plus-shaped; its alternative remains minus. The visibly inconsistent signs lambda(e2-e1)=-lambda(s2-s1) were not corrected.

### Indices and exponents

Every sigma subscript 0,1,2, every s subscript 0,3, vector subscripts 1,2,3, and all squares checked. No i or j index. 1° and 2° are degree-style enumeration marks. s3 prime in the last marginal equation is now explicitly uncertain against unprimed s3.

### Margins, insertions, and handwriting

Rotated slanted note: prouver remains uncertain, as do u and its power, the relation between sigma0(s3 prime) and sigma0sigma1s3, and the final chain. The separate right-margin lambda mu nu is live. The crossed condition mu+nu lambda=0, cancelled preliminary expansion, cancelled det, crossed donc, and deleted lambda e1+mu e2 all remain cancelled. The line under the boxed conditions and guide over compte tenu are not word cancellations.

### Alphabet candidates

Greek lambda/mu/nu compared with scan 83: nu has a v/y shape, while alpha and alpha prime below have a closed loop. No double-struck or script capital.

### Changes

On aura donc -> On aura alors; On pose -> On unsure{posera|pose}; c.à.d.|Ceci. -> i.e.|c.à.d.|Ceci.; difference separator unsure{-|+} -> unsure{+|-}; final marginal s3 prime -> unsure{s3 prime|s3}. Other readings unchanged.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 4:

```latex
\[
\sigma_1^2=\mathrm{id}\qquad\unsure{\leftarrow}
\]
```

2. TeX line 7:

```latex
$\sigma_0^2=\sigma_2^2=\mathrm{id}$
```

3. TeX line 7:

```latex
$\sigma_0\sigma_2=\sigma_2\sigma_0$
```

4. TeX line 8:

```latex
\[
\sigma_1^2(s_3)=s_3^{\unsure{*|4|' }}\qquad\text{i.e.}\qquad\sigma_1(s'_3)=s_3\qquad\text{or}
\]
```

5. TeX line 11:

```latex
\[
\begin{aligned}
\sigma_1(s'_3)&=\sigma_1s_0+\deleted{\unsure{\sigma_1e_3=s_0+\lambda}}\inserted{\lambda\sigma_1e_1+\mu\sigma_1e_2+\nu\sigma_1e_3}\\
&=s_0+\lambda e_2+\mu e_1+\nu(\lambda e_1+\mu e_2+\nu e_3)\\
&=s_0+(\mu+\nu\lambda)e_1+(\lambda+\nu\mu)e_2+\nu^2e_3
\end{aligned}
\]
```

6. TeX line 18:

```latex
$\lambda\ \mu\ \nu$
```

7. TeX line 21:

```latex
\[
\left\{\begin{aligned}
\boxed{\begin{aligned}\nu^2&=1\\\mu&=-\nu\lambda\end{aligned}}
&\quad\begin{aligned}\deleted{\unsure{\mu+\nu\lambda=0}}\quad &(1^\circ)\\ &(2^\circ)\end{aligned}\\
\lambda=-\nu\mu\quad&\text{ou encore}\quad
\overset{\text{(compte tenu de }2^\circ\text{)}}{\lambda=\nu^2\lambda}\quad\text{qui résulte de }1^\circ,
\end{aligned}\right.
\]
```

8. TeX line 31:

```latex
\[
\left\{\begin{aligned}\nu&=1,\ \mu=-\lambda\\\nu&=-1,\ \mu=\lambda\end{aligned}\right.
\]
```

9. TeX line 35:

```latex
$\nu=1$
```

10. TeX line 35:

```latex
$\unsure{u^3}=\mathrm{id}$
```

11. TeX line 35:

```latex
$\unsure{u}s''_3=s'_3$
```

12. TeX line 35:

```latex
$s''_3=\sigma_0(s'_3)$
```

13. TeX line 35:

```latex
$\unsure{\ne|=}$
```

14. TeX line 35:

```latex
$\sigma_0\sigma_1s_3$
```

15. TeX line 35:

```latex
$\sigma_1s''_3=s'_3$
```

16. TeX line 35:

```latex
$\sigma_1\sigma_0\sigma_1(s_3)=\sigma_0\sigma_1(\unsure{s'_3|s_3})$
```

17. TeX line 38:

```latex
\[
\det\sigma_1=\deleted{\unsure{\det}}-\nu
\]
```

18. TeX line 41:

```latex
$\det\sigma_1=-1$
```

19. TeX line 41:

```latex
$\sigma_1$
```

20. TeX line 41:

```latex
$\nu=1$
```

21. TeX line 41:

```latex
$\mu=-\lambda$
```

22. TeX line 44:

```latex
\[
s'_3-s_3=\deleted{\unsure{\lambda e_1+\mu e_2}}\inserted{\underbrace{(s'_3-s_0)}_{\unsure{u(e_3)}}\unsure{+|-}\underbrace{(s_3-s_0)}_{e_3}}=\lambda(e_2-e_1)=-\lambda(s_2-s_1)
\]
```

23. TeX line 48:

```latex
\[
-\lambda=(1+\alpha)\qquad\lambda=-(1+\alpha)=\alpha'\tag*{(1)}
\]
```

24. TeX line 52:

```latex
\[
s'_3-s_3=(1+\alpha)(s_2-s_1)\tag*{(2)}
\]
```


## Scan 085

Start: 2026-11-17T23:47:43.256895+00:00  
End: 2026-11-17T23:48:26.873781+00:00

### Observations recorded before opening the page file

Image-first words/accents: Et la matrice de sigma1 est.; Posons; à calculer; crossed Notons que s0,s1,s2,s3; On aura; donc; Ou encore; Notons/Calculons u(s3') utilisant (2); Enfin, on trouve de = par (6). No accent on the shorthand equals sign is supplied. Numerical label under the equality to s3 looks (5), possibly (6). First u cycle ends in s1-like glyph, not confidently s0. Both u/v names have dense cancelled trailing marks. Two e2 terms were revised from parenthesized differences; retain crossed -e1 and bracket traces. Bottom line reaches the paper edge. Archive 84.

### Comparison, corrections, and nearby strokes

Compared all 32 entries of the two matrices, (4) and both action chains, each expansion of s3 double prime, (5),(6), both calculations of u(s3 prime), and the bottom u(s3 double prime) calculation. Signs in e2-e1 and both braces checked directly. The dark initial-cycle final index remains 1/0. The labelled equality to s3 remains (5)/(6). The bottom displayed line was checked at the edge rather than inferred from the next page.

### Indices and exponents

Only 0,1,2,3 numeric subscripts and the cancelled possible 4; no i/j. Prime and double prime checked on every s3. Both 1 and 2 remain candidates in the intermediate s-index after us0+ue3. Matrix alpha prime signs checked row by row.

### Margins, insertions, and handwriting

à calculer and its up-left guide are retained. Entire Notons que line, the preliminary us3 prime calculation, the two bracket/-e1 corrections, cancelled trailing labels on u/v, au, and the two cancelled (7) marks checked as struck. Live Posons, On aura, donc, Ou encore, and Enfin are not crossed.

### Alphabet candidates

Plain Latin u and v distinguished from nu; alpha and alpha prime match scan 84. No script or double-struck capitals. Et remains marked because the initial letter is stylized.

### Changes

ou encore -> Ou encore (visible initial capital). All other readings unchanged.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 3:

```latex
$\sigma_1$
```

2. TeX line 4:

```latex
\[
\sigma_1=\begin{pmatrix}0&1&-(1+\alpha)&0\\1&0&1+\alpha&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
=\begin{pmatrix}0&1&\alpha'&0\\1&0&-\alpha'&0\\0&0&1&0\\0&0&0&1\end{pmatrix}\tag*{(3)}
\]
```

3. TeX line 9:

```latex
\[
\left\{\begin{aligned}
u_{\deleted{\unsure{0|1}}}&=\sigma_0\sigma_1
& s_0\mapsto s_1\mapsto s_2\mapsto\unsure{s_1|s_0},\ s_3\mapsto s''_3\deleted{\unsure{4}}\\
v_{\deleted{\unsure{1|2}}}&=\sigma_1\sigma_2
& s_0\mapsto s_0,\ s_3\mapsto s_1\mapsto s_2\mapsto s'_3
\end{aligned}\right.\tag*{(4)}
\]
```

4. TeX line 17:

```latex
$\unsure{\nwarrow}$
```

5. TeX line 18:

```latex
$\unsure{s_0},s_1,s_2,s_3$
```

6. TeX line 21:

```latex
\[
\begin{aligned}
s''_3&=us_0+ue_3=s_{\unsure{1|2}}+\sigma_0(\sigma_1(e_3))=s_0+e_1+\sigma_0\bigl[(1+\alpha)(e_2-e_1)\\
&\hspace{10cm}+e_3\bigr]\\
&=s_0+e_1+(1+\alpha)\deleted{\unsure{(}}e_2\deleted{\unsure{-e_1)}}+e_3-e_1
\end{aligned}
\]
```

7. TeX line 29:

```latex
\[
s''_3=s_0+(1+\alpha)\deleted{\unsure{(}}e_2\deleted{\unsure{-e_1)}}+e_3=s_3+(1+\alpha)e_2\tag*{(5)}
\]
```

8. TeX line 33:

```latex
\[
s''_3-s_3=(1+\alpha)(s_2-s_0)\tag*{(6)}
\]
```

9. TeX line 36:

```latex
$u(s'_3)$
```

10. TeX line 37:

```latex
\[
\deleted{us'_3=us_0+ue_3=s_1+\sigma_0\sigma_1\bigl((1+\alpha)(e_2-e_1)+e_3\bigr)=s_1+(1+\alpha)u(s_2-s_1}
\]
```

11. TeX line 40:

```latex
\[
\begin{aligned}
u(s'_3)&=u(s_3)+(1+\alpha)\underbrace{u(s_2-s_1)}_{s_0-s_2=-e_2}=s''_3-(1+\alpha)e_2\\
&\underset{\unsure{(5)|(6)}}{=}s_3
\end{aligned}
\]
```

12. TeX line 46:

```latex
$\unsure{=|\text{même}}$
```

13. TeX line 47:

```latex
\[
\deleted{\unsure{(7)}}\qquad\deleted{\unsure{u(s_3)\quad s_3\longrightarrow s'}}
\]
```

14. TeX line 50:

```latex
\[
\begin{aligned}
\deleted{\unsure{(7)}}\quad u(s''_3)&=u(s_3)+(1+\alpha)\overbrace{u(s_2-s_0)}^{s_0-s_1=-e_1}=s''_3-(1+\alpha)e_1\\
&=s_0+(1+\alpha)(e_2-e_1)+e_3
\end{aligned}
\]
```


## Scan 086

Start: 2026-11-17T23:48:26.894468+00:00  
End: 2026-11-17T23:49:21.999207+00:00

### Observations recorded before opening the page file

Image-first words/accents: donc; Donc on trouve; bien sûr (right edge); Notons que; un = plan; celui d'équation; stable; Un calcul connu/comme montre que; Donc si G est le groupe; Aut(icosaèdre comb. épinglé...); alors sous réserve que; groupe fini G; opère affinement; Montrons que; transformés; forme un icosaèdre géométrique ?; Cela signifie que; les seules relations d'incidence. s3 in the first point list is a 3, and the final Pl argument looks s3, not s2. Commutation relation ends sigma2 sigma1. E has two vertical strokes. Underlining/deletion near aussi, u/v; insertions fini and affinement. Archive 85.

### Comparison, corrections, and nearby strokes

Compared (7),(8),(9), every relation in (10), the plane equation and all inline point/line/plane expressions. The commutation relation visibly ends sigma2sigma1 and the Pl triple ends s3; both are retained. Read the full prose with the insertions and the final line at the lower edge. Enlarged the short word before corps: two upright strokes sharing a crossbar suggest tt more than le; neither expanded. The question after géométrique is retained.

### Indices and exponents

0,1,2,3 subscripts checked; powers 2,3,5 checked separately. No i/j index. The 3 on E is superscript. Prime/double-prime order in (7) agrees with the crop.

### Margins, insertions, and handwriting

No separate prose margin note. Right edge bien sûr is readable with edge contact. The crossed u²=1, aussi, u, and droites remain struck. fini and affinement attach to groupe and opère respectively. The inserted v=sigma1sigma2 attaches after par, not to the preceding parenthesis.

### Alphabet candidates

E explicitly double-stroked, kept mathbb E. G plain, Aut plain A. No script/Greek capital ambiguity. v is Latin; alpha Greek with an upper 2.

### Changes

unsure{le} corps -> unsure{tt|le} corps after enlarged crop. No mathematical correction.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 4:

```latex
\[
u:\quad s_3\mapsto s''_3\mapsto s'_3\mapsto s_3\tag*{(7)}
\]
```

2. TeX line 8:

```latex
\[
u^3=\mathrm{id}\qquad\deleted{\unsure{u^2=1}}\quad(u\ne\mathrm{id}\ \text{bien sûr})\tag*{(8)}
\]
```

3. TeX line 11:

```latex
$s_3,s_1,s_2,s'_3$
```

4. TeX line 11:

```latex
$=$
```

5. TeX line 11:

```latex
$x+y+z=1$
```

6. TeX line 11:

```latex
$\sigma_1$
```

7. TeX line 11:

```latex
$\sigma_2$
```

8. TeX line 11:

```latex
$v=\sigma_1\sigma_2$
```

9. TeX line 11:

```latex
$\unsure{u}$
```

10. TeX line 11:

```latex
$v=\sigma_1\sigma_2$
```

11. TeX line 12:

```latex
\[
v^5=\mathrm{id}\quad\Longleftrightarrow\quad\boxed{\alpha^2+\alpha-1=0}\tag*{(9)}
\]
```

12. TeX line 15:

```latex
$G$
```

13. TeX line 16:

```latex
\[
\begin{aligned}
G&=\left\{\sigma_0,\sigma_1,\sigma_2\ \middle|\ \begin{aligned}&\sigma_0^2=\sigma_1^2=\sigma_2^2=1,\quad\sigma_0\sigma_2=\sigma_2\sigma_1,\\&(\sigma_0\sigma_1)^3=1,\ (\sigma_1\sigma_2)^5=1\end{aligned}\right\}\\
&=\mathrm{Aut}(\text{icosaèdre comb. épinglé}\ldots)
\end{aligned}\tag*{(10)}
\]
```

14. TeX line 22:

```latex
$\alpha^2+\alpha-1=0$
```

15. TeX line 22:

```latex
$G$
```

16. TeX line 22:

```latex
$\mathbb{E}^3$
```

17. TeX line 22:

```latex
$s_0$
```

18. TeX line 22:

```latex
$\mathrm{Dr}(s_0,s_1)$
```

19. TeX line 22:

```latex
$\mathrm{Pl}(s_0,s_1,s_3)$
```


## Scan 087

Start: 2026-11-17T23:49:22.022058+00:00  
End: 2026-11-17T23:49:41.869674+00:00

### Observations recorded before opening the page file

Image-first: only de l'icosaèdre near the top. The middle letters and grave-accent reading of icosaèdre remain compressed. No period visible. The other thirds contain no manuscript text; archive 86 at bottom left. A small isolated dark spot in the top crop is not a letter or formula.

### Comparison, corrections, and nearby strokes

Read the entire short continuation and examined both blank thirds. The uncertain icosaèdre remains marked; no completion from the following page was added.

### Indices and exponents

None; no formulas.

### Margins, insertions, and handwriting

No marginal note, correction, deletion, insertion, or live text near a cancellation.

### Alphabet candidates

No mathematical alphabet candidate.

### Changes

No change. This exceptionally sparse sheet requires less reading time than the full manuscript pages.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.


## Scan 088

Start: 2026-11-17T23:49:41.890912+00:00  
End: 2026-11-17T23:50:31.645469+00:00

### Observations recorded before opening the page file

Image-first words/accents: de l'icosaèdre combinatoire.; Si nous admettons; fini inserted; stabilisateur; engendré; cyclique d'ordre 5; diédral; produit 1/2 direct; nb; diviseur; six points déjà écrits; distincts underlined; coordonnées; Il est clair; tous distincts; comparer; dernière coordonnée; l'un ou l'autre inserted; même condition néc. et suff. The first list's s3 prime is inked like a star. Last coordinate-row subscript under the double-prime s resembles 2 as well as 3. Margin says alpha prime=-(alpha+1)=-alpha inverse, with double quotation marks around l'autre racine. Deletions in last paragraph include Il, voir, sont, ne peuvent être, que ssi, and 1+alpha=0. Archive 87.

### Comparison, corrections, and nearby strokes

Compared the order-120 argument, every inline group expression, six listed vertices, all six coordinate rows and two curved arrows, marginal root identity, and the revised final paragraph. The table's last lower digit has the flat lower stroke of 2 as well as a possible compressed 3; now marked instead of silently using the expected vertex name. All coordinate signs, ones and zeros were checked independently. The two quotation marks on either side of l'autre racine are retained.

### Indices and exponents

0,1,2,3 point subscripts; 1 on sigma; exponent -1 on alpha and 2 in the quadratic. The last displayed double-prime subscript is now unsure{2|3}. No i or j index. Prime versus star in the first inline vertex list remains marked.

### Margins, insertions, and handwriting

Right-margin alpha identity reread word and symbol by symbol. fini and Z insertions attach to est and groupe. In the final paragraph, struck Il, voir, sont, ne peuvent être, que ssi/que si and 1+alpha=0 remain deleted; sont, l'un ou l'autre à, i.e. alpha=-1 and donc remain insertions. Under distincts is an underline, not cancellation.

### Alphabet candidates

Z may be plain or double stroked; first occurrence remains Z|mathbb Z. G plain. No script capital candidate. Diédral remains unsure because its middle strokes are compressed.

### Changes

Last coordinate-row s3 double prime -> s_{unsure{2|3}} double prime. All other readings unchanged.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 5:

```latex
$G$
```

2. TeX line 5:

```latex
$120$
```

3. TeX line 5:

```latex
$s_0$
```

4. TeX line 5:

```latex
$\unsure{Z|\mathbb{Z}}$
```

5. TeX line 5:

```latex
$v$
```

6. TeX line 5:

```latex
$5$
```

7. TeX line 5:

```latex
$\sigma_1$
```

8. TeX line 5:

```latex
$\{1,\sigma_1\}.Z$
```

9. TeX line 5:

```latex
$1/2$
```

10. TeX line 5:

```latex
$120/10=12$
```

11. TeX line 5:

```latex
$s_0,s_1,s_2,s_3,\unsure{s'_3|s_3^*},s''_3$
```

12. TeX line 6:

```latex
\((11)\quad\left\{\begin{gathered}\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
s_0=(0,0,0)\arrow[d,bend left=60,leftrightarrow]\\
s_1=(\unsure{1|0},0,0)\\
s_2=(0,1,0)\arrow[d,bend left=60,leftrightarrow]\\
s_3=(0,0,1)\\
s'_3=(-(1+\alpha),1+\alpha,1)=(\deleted{\unsure{+}}\alpha',-\alpha',1)\\
s''_{\unsure{2|3}}=(0,1+\alpha,1)=(0,-\alpha',1)
\end{tikzcd}\end{gathered}\right.\)
```

13. TeX line 14:

```latex
$\alpha'=-(\alpha+1)=-\alpha^{-1}$
```

14. TeX line 14:

```latex
$\alpha^2+\alpha-1=0$
```

15. TeX line 16:

```latex
$s_0$
```

16. TeX line 16:

```latex
$s_3$
```

17. TeX line 16:

```latex
$s'_3,s''_3$
```

18. TeX line 16:

```latex
$s'_3,s''_3$
```

19. TeX line 16:

```latex
$1$
```

20. TeX line 16:

```latex
$\ne s_0,s_1,s_2$
```

21. TeX line 16:

```latex
$s_3$
```

22. TeX line 16:

```latex
$1+\alpha=0$
```

23. TeX line 16:

```latex
$\alpha=-1$
```

24. TeX line 16:

```latex
$s'_3=s''_3$
```

25. TeX line 16:

```latex
$1+\alpha=0$
```

26. TeX line 16:

```latex
$\alpha=-1$
```


## Scan 089

Start: 2026-11-17T23:50:31.666330+00:00  
End: 2026-11-17T23:51:31.469192+00:00

### Observations recorded before opening the page file

Image-first words/accents: l'équation; devient -1=0; jamais vérifiée; sur une base non vide !; Cela implique (replaces signifie); nb de sommets; au moins six; égal à six ou douze; Si c'était [douze] six; stabilisateur; groupe d'ordre 20; diédral; un seul; produit; centre; antipodisme; cela signifierait; par homogénéité; Nous allons donc calculer; antipodiques; six points déjà marqués; pour faire ra-/pide; liste de 12 pts!; On va d'abord déterminer le centre; défini (s'il existe) comme l'unique (?) pt fixe sous G. The centre symbol is a curly z/3-shaped letter, plain z also possible. Only the set's a is clearly underlined; the later as0 and as3 look un-underlined. Archive 88.

### Comparison, corrections, and nearby strokes

Read all prose and inline formulas, including the split ra-/pide parenthesis and the final centre paragraph enlarged. Compared quadratic, -1=0, order 20, D5, the centre set and both fixed-point equalities. The small preposition after nb and the abbreviated-looking word before G are now marked. Retained the conditions s'il existe and (?) without converting them to assertions.

### Indices and exponents

Only the lower 5 in D5 and lower 0,3 in s0/s3; squared alpha checked. No i/j index. a in the centre set alone has a clear underline; later as0 and as3 remain plain a, as in the crop.

### Margins, insertions, and handwriting

The hook under a leads to antipodisme, included as an insertion. implique replaces crossed signifie; sommets est replaces crossed pts est; six follows crossed douze; a dark E-like mark before s0 remains deleted and unsure. centre is underlined, not struck. No sideways note.

### Alphabet candidates

Curly centre symbol kept mathfrak z|z, first occurrence. D and G are plain, not doubled or script. No implicit normalization of a underlines.

### Changes

nb des -> nb unsure{de|des}; fixe sous G -> fixe unsure{ss|sous} G. Other readings unchanged.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 3:

```latex
$\alpha^2+\alpha-1=0$
```

2. TeX line 3:

```latex
$-1=0$
```

3. TeX line 3:

```latex
$E$
```

4. TeX line 3:

```latex
$s_0$
```

5. TeX line 3:

```latex
$20$
```

6. TeX line 3:

```latex
$D_5$
```

7. TeX line 3:

```latex
$D_5$
```

8. TeX line 3:

```latex
$\unsure{\mathfrak{z}|z}=\{1,\underline{a}\}$
```

9. TeX line 3:

```latex
$as_0=s_0$
```

10. TeX line 3:

```latex
$as_3=s_3$
```

11. TeX line 3:

```latex
$=$
```

12. TeX line 5:

```latex
$6$
```

13. TeX line 5:

```latex
$12$
```

14. TeX line 7:

```latex
$G$
```


## Scan 090

Start: 2026-11-17T23:51:31.489316+00:00  
End: 2026-11-17T23:52:05.220621+00:00

### Observations recorded before opening the page file

Image-first: no prose, accents or unusual words. Six rows of identities at lower right, including two braced pairs at the right of the first rows. First row alpha=-(alpha prime+1) has dark overwritten alpha prime. Slanted division strokes in the second pair. Rightmost (1+alpha)(1+alpha prime) has an alpha that looks like 2. Last row has 2alpha-1 in each factor, right-hand -1. Both upper thirds otherwise blank. Archive 89.

### Comparison, corrections, and nearby strokes

Compared all six rows and both two-line braced pairs: sum, product, both reciprocal expressions, products with 1-alpha, the two root-times-successor identities and side product, products with alpha+2, and final 2alpha-1 factors. Checked every minus sign and every prime. The dark alpha prime and right-side alpha/2 ambiguity remain marked. Blank upper and middle areas examined.

### Indices and exponents

No indices, no i/j. Primes only on the second root; no inverse exponent because the manuscript uses slash fractions here. All 2s in the final two rows are numerals.

### Margins, insertions, and handwriting

No marginal text or insertions. No visible struck block; the dark alpha prime is overwritten but its underlying form cannot be securely separated. The trailing small dot is retained.

### Alphabet candidates

Only Greek alpha; the one numeral-like alpha is explicitly alpha|2. No capital alphabet candidate.

### Changes

No change. Sparse formula sheet; no prose to audit.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 4:

```latex
\[
\alpha+\alpha'=-1\qquad
\left\{\begin{aligned}\alpha&=-(\unsure{\alpha'}+1)\\\alpha'&=-(\alpha+1)\end{aligned}\right.
\]
```

2. TeX line 8:

```latex
\[
\alpha\alpha'=-1\qquad
\left\{\begin{aligned}\alpha&=-1/\alpha'\\\alpha'&=-1/\alpha\end{aligned}\right.
\]
```

3. TeX line 12:

```latex
\[
(1-\alpha)(1-\alpha')=1
\]
```

4. TeX line 15:

```latex
\[
(1+\alpha)\alpha=(1+\alpha')\alpha'=1\qquad(1+\unsure{\alpha|2})(1+\alpha')=-1
\]
```

5. TeX line 18:

```latex
\[
(\alpha+2)(\alpha'+2)=1
\]
```

6. TeX line 21:

```latex
\[
(2\alpha-1)(2\alpha'-1)=-1.
\]
```


## Scan 091

Start: 2026-11-17T23:52:05.244511+00:00  
End: 2026-11-17T23:53:03.591498+00:00

### Observations recorded before opening the page file

Image-first words/accents: pts fixes définis par (three times); (si 2 inv); cancelled NB en car.2, c'est l'hyperplan à l'infini; (id. en x,y,z) after the underlined plane equation; Centre o de coordonnées; NB underlined; l'équation alpha²+alpha-1, without =0; implique alpha inv.; et [en fait =>] elle s'écrit; On a alpha-2 pas inv. struck; en fait; sera inv.; ssi 5 est inv.; Ainsi, en car.≠2; donné par les coordonnées (15); en car.2; sans doute inserted; le pt à l'infini dans la direction. Right-side working and two cancelled centre forms are dense. The final bracket ends with dots and ]. Archive 90.

### Comparison, corrections, and nearby strokes

Compared (12)-(16), every coordinate entry, all fixed-point equations, the right-side solution working, both cancelled centre expressions, the live centre expression, the product of invertible factors, and the final direction. Enlarged the four cancellation/working regions. The upper cancelled centre expression may contain an additional inner 1/2 before alpha prime; added this first candidate without removing the former alternative. The numerator of the inserted marginal y-coordinate has a possible leading minus, now marked. The NB lacks =0 in its quadratic and this absence is retained.

### Indices and exponents

sigma indices 0,1,2 checked; 12-16 labels checked. All squares, primes, fractions 1/2 and denominator 2alpha checked separately. No i/j index. The centre is lowercase o, not zero.

### Margins, insertions, and handwriting

Cancelled NB read along the two horizontal lines including the right edge. Right margin x,y,z working read line by line, including cancelled alpha-prime squared fraction, replacement (1-alpha prime)/2, the comparison with 1/2 and crossed x=alpha/2, y=z=-1/(2alpha). Underlined fixed plane and Centre are live. Cancelled en fait arrow, On a alpha-2 pas inv., two centre forms and their bracket traces remain deleted. (2alpha-1) and sans doute are insertions at their visible guides.

### Alphabet candidates

All coefficients Greek alpha, not Latin a. o distinguished from 0 by its role and round handwritten form. NB plain capitals, no double-struck/script candidate.

### Changes

Cancelled 1/2(alpha prime,1,1) -> unsure{1/2(1/2 alpha prime,1,1)|1/2(alpha prime,1,1)}; marginal inserted numerator 1-alpha prime -> unsure{1-alpha prime|-1-alpha prime}; tiny or -> unsure{or|ou}.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 3:

```latex
\[
\left\{\begin{aligned}
\sigma_0(x,y,z)&=(\unsure{1-(x+y+z)},y,z)\\
\text{pts fixes définis par}\quad&\deleted{\unsure{x=-\tfrac12(y+z-1)}}\inserted{2x+y+z-1=0}\quad\text{(si }2\text{ inv)}
\end{aligned}\right.\tag*{(12)}
\]
```

2. TeX line 9:

```latex
$2$
```

3. TeX line 10:

```latex
\[
\left\{\begin{aligned}
\sigma_1(x,y,z)&=(y-(1+\alpha)z,x+(1+\alpha)z,z)=(y+\alpha'z,x-\alpha'z,z)\\
\text{pts fixes définis par}\quad&\left\{\begin{aligned}
\underline{x+(1+\alpha)z=y}&\qquad\text{(\unsure{id.} en }x,y,z\text{)}\\
\deleted{\unsure{x-\alpha'z=y}}&\\
x-y-\alpha'z&=0
\end{aligned}\right.
\end{aligned}\right.\tag*{(13)}
\]
```

4. TeX line 20:

```latex
\[
\left\{\begin{aligned}\sigma_2(x,y,z)&=(x,z,y)\\\text{pts fixes définis par}\quad&y=z\end{aligned}\right.\tag*{(14)}
\]
```

5. TeX line 23:

```latex
$x=\frac12\alpha',\ y=\alpha'x=\deleted{\unsure{\frac{\alpha'^2}{2}}}\inserted{\frac{\unsure{1-\alpha'|-1-\alpha'}}2},\ z=y\unsure{\ne|=}\frac12$
```

6. TeX line 23:

```latex
$\unsure{x=\frac\alpha2,\ y=z=-\frac1{2\alpha}}$
```

7. TeX line 25:

```latex
$o$
```

8. TeX line 26:

```latex
\[
\deleted{\unsure{\tfrac12(\tfrac12\alpha',1,1)|\tfrac12(\alpha',1,1)}}
\]
```

9. TeX line 29:

```latex
\[
\deleted{\unsure{o=(\tfrac12,-\tfrac1{2\alpha},-\tfrac1{2\alpha})=\tfrac12(-1,-\tfrac1\alpha,-\tfrac1\alpha)}}
\]
```

10. TeX line 32:

```latex
\[
o=\frac12(\alpha',1-\alpha',1-\alpha')=\frac12(-(1+\alpha),2+\alpha,2+\alpha)\tag*{(15)}
\]
```

11. TeX line 36:

```latex
$\alpha^2+\alpha-1$
```

12. TeX line 36:

```latex
$\alpha$
```

13. TeX line 36:

```latex
$\unsure{\Rightarrow|=}$
```

14. TeX line 37:

```latex
\[
\boxed{\alpha(\alpha+1)=1}\qquad\unsure{\text{or}|\text{ou}}\tag*{(16)}
\]
```

15. TeX line 40:

```latex
$\alpha-2$
```

16. TeX line 42:

```latex
$\alpha(\alpha+1)(\alpha-1)(\alpha+2)\inserted{(2\alpha-1)}$
```

17. TeX line 42:

```latex
$\unsure{\ldots\}}$
```

18. TeX line 42:

```latex
$(\alpha-2)$
```

19. TeX line 42:

```latex
$5$
```

20. TeX line 44:

```latex
$\ne2$
```

21. TeX line 44:

```latex
$2$
```

22. TeX line 44:

```latex
$(-1,\frac1\alpha,\frac1\alpha)$
```


## Scan 092

Start: 2026-11-17T23:53:03.619026+00:00  
End: 2026-11-17T23:54:34.565191+00:00

### Observations recorded before opening the page file

Image-first words/accents: Ceci dit; on doit pouvoir sans mal vérifier ceci; Prop underlined; l'antipodisme a est la symétrie par r. au pt o donné par (15), si 2 inv. inserted; formule; unique pt fixe; n'étant pas fixes sous/ss G; En car. [zéro] 2; translation par le vecteur; donc n'a pas de pt fixe (à distance finie). NB En car.2 les solutions: low horizontal line could be cancellation or underline. ext. alg. clos. K; deux éléments; ext. quadratique; Si on pose; corps des racines primitives 3èmes de l'unité; donnée; satisfaisant; équivaut; F4-structure; morphisme; Notons que; autre él. underlined. Field names in NB are heavily altered; distinguish tilde K from plain K without repairing the statement. s_i has dotted i with no descender. Archive 91.

### Comparison, corrections, and nearby strokes

Compared proposition, revised (17) and cancelled coordinate triple, both characteristic cases, every finite-field and scheme expression, and final alpha identity. Re-read the enlarged field-name corrections without replacing K by the mathematically expected name. Found a small annotation above the defining equality, enlarged separately: reads déf/dfn; now included. The ambiguous state of les solutions is now represented as deletion/underline alternatives rather than assuming a certain cancellation. Translation vector (alpha prime,1,1) remains as written.

### Indices and exponents

The s_i has an i with dot and no descender, not j. This is the only letter index on the page. Point subscripts 3, field subscripts 2,4 and uncertain 2/p, power 2 on alpha and T, and 3èmes checked. T is a plain capital with crossbar; no Gamma reading.

### Margins, insertions, and handwriting

sans mal follows pouvoir; si 2 inv. follows (15); alg. clos. K follows ext. The revised underlined a replaces a cancelled a. Deleted s3, zéro, old coordinate triple and field-name mark remain struck. Prop, NB and autre are underlined. The definition annotation above = is now inventoried as handwritten.

### Alphabet candidates

F has a visible double vertical stroke each time, retained mathbb F. K plain and tilde K are not merged; S plain. T has the same ordinary capital form in T² and T. Underlined a only where visible.

### Changes

deleted unsure{les solutions} -> unsure{deleted{les solutions}|uline{les solutions}}; F4=F2[T]/... -> F4 overset{unsure{déf|dfn}}{=} F2[T]/..., restoring the omitted annotation. Added its inventory row.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 5:

```latex
$\underline{a}$
```

2. TeX line 5:

```latex
$o$
```

3. TeX line 5:

```latex
$2$
```

4. TeX line 6:

```latex
\[
\underline{a}(x,y,z)=(\alpha'-x,(1-\alpha')-y,(1-\alpha')-z)\tag*{(17)}
\]
```

5. TeX line 9:

```latex
\[
\deleted{\unsure{=(\alpha'-x,-(1+\alpha)-y,\alpha+2-z)}}
\]
```

6. TeX line 12:

```latex
$2$
```

7. TeX line 12:

```latex
$\unsure{a}$
```

8. TeX line 12:

```latex
$\underline{a}$
```

9. TeX line 12:

```latex
$o$
```

10. TeX line 12:

```latex
$s_i,\deleted{\unsure{s_3}},s'_3,s''_3$
```

11. TeX line 12:

```latex
$\ne o$
```

12. TeX line 12:

```latex
$G$
```

13. TeX line 12:

```latex
$2$
```

14. TeX line 12:

```latex
$\underline{a}$
```

15. TeX line 12:

```latex
$(\alpha',1,1)$
```

16. TeX line 14:

```latex
$2$
```

17. TeX line 14:

```latex
$\alpha^2+\alpha-1=0$
```

18. TeX line 14:

```latex
$K$
```

19. TeX line 14:

```latex
$\mathbb{F}_2$
```

20. TeX line 14:

```latex
$\deleted{\unsure{\mathbb{F}_4}}\unsure{\mathbb{F}_4}.\ \unsure{\widetilde{K}\setminus K}$
```

21. TeX line 14:

```latex
$\unsure{K|\widetilde{K}}$
```

22. TeX line 14:

```latex
$\mathbb{F}_2$
```

23. TeX line 14:

```latex
$K$
```

24. TeX line 15:

```latex
\[
\mathbb{F}_4\overset{\unsure{\text{déf}|\text{dfn}}}{=}\mathbb{F}_2[T]/(T^2+T+1)=\begin{gathered}\text{corps des racines}\\\text{primitives }3^{\text{èmes}}\text{ de}\\\text{l'unité sur }\unsure{\mathbb{F}_2|\mathbb{F}_p}\end{gathered}
\]
```

25. TeX line 18:

```latex
$\alpha$
```

26. TeX line 18:

```latex
$S/\mathbb{F}_2$
```

27. TeX line 18:

```latex
$\alpha^2+\alpha-1=0$
```

28. TeX line 18:

```latex
$\mathbb{F}_4$
```

29. TeX line 18:

```latex
$S$
```

30. TeX line 18:

```latex
$S\longrightarrow\operatorname{Spec}\mathbb{F}_4$
```

31. TeX line 18:

```latex
$\alpha^2=\frac1\alpha=\alpha+1$
```

32. TeX line 18:

```latex
$\mathbb{F}_4\setminus\mathbb{F}_2$
```


## Scan 093

Start: 2026-11-17T23:54:34.585651+00:00  
End: 2026-11-17T23:57:42.419164+00:00

### Observations recorded before opening the page file

Image-first observations, before reopening the transcription: the sheet is music-ruled stationery; the only semantic handwriting is the six-row coordinate table at the top, under one left brace labelled (18). The operator a is underlined in every row. Read the points in order as s_0, s_1, s_2, s_3, s'_3, s''_3. Primes occur throughout on alpha; no blackboard or script letters occur. The first four rows read (alpha',1-alpha',1-alpha'), (alpha'-1,1-alpha',1-alpha'), (alpha',-alpha',1-alpha'), (alpha',1-alpha',-alpha'). In each of the last two rows the middle coordinate has a clear surviving 1 and a heavily cancelled following expression; the first coordinate is respectively 0 and alpha', and the last -alpha'. A separate cancellation between those rows has very weak remaining characters, plausibly ending 2 alpha + 3. The middle and lower thirds contain no further words or formulae; the pencil 92 is an archive number. No French accents or prose words occur.

### Comparison, corrections, and nearby strokes

Checked the six coordinates, surviving primes, six underlined operators, the large brace and label (18), three full stops, and all three cancelled portions. The two sparse thirds are blank apart from stationery, the archive number and isolated nonsemantic pen traces. No change.

### Indices and exponents

The subscripts are 0,1,2,3,3,3; the last two point names have one and two primes. No i or j occurs in an index or exponent. Alpha has a prime in every live occurrence; the separate cancelled expression remains explicitly doubtful.

### Margins, insertions, and handwriting

No marginal verbal note or insertion. The two cancelled middle-coordinate suffixes and the separate heavily cancelled expression remain deleted and uncertain. No live word is crossed by a line; the staff lines are printed ruling.

### Alphabet candidates

Plain Greek alpha, ordinary s, and underlined ordinary a. No script, Gothic or double-struck candidate. No French prose or accents.

### Changes

No change. The separate cancellation remains \unsure{1-2\alpha+3|2\alpha+3}; neither its upper stroke nor its left edge supports a confident further reading.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 3:

```latex
\[
\left\{\begin{aligned}
\underline a s_0&=(\alpha',1-\alpha',1-\alpha')\\
\underline a s_1&=(\alpha'-1,1-\alpha',1-\alpha')\\
\underline a s_2&=(\alpha',-\alpha',1-\alpha').\\
\underline a s_3&=(\alpha',1-\alpha',-\alpha')\\
\underline a s_3'&=(0,1\deleted{\unsure{-\alpha'}},-\alpha').\\
&\deleted{\unsure{1-2\alpha+3|2\alpha+3}}\\
\underline a s_3''&=(\alpha',1\deleted{\unsure{-\alpha'}},-\alpha').
\end{aligned}\right.
\tag*{(18)}
\]
```


## Scan 094

Start: 2026-11-17T23:57:42.441538+00:00  
End: 2026-11-17T23:59:08.323696+00:00

### Observations recorded before opening the page file

Image-first observations before opening the page file: Écrivons has a visible acute on the capital; antipodiques, distincts, alignés, vérifications, à faire and à son antipodique are read with their visible endings and accents. The top coordinate table, including its heading, is crossed by long diagonal cancellation strokes; the six a operators are underlined and the label is (18). Several entries are rewritten heavily; in particular the last coordinate form in the third row begins with a dark 1/alpha-prime-like shape. The lower prose has numerous additions: (sur un corps de base quelc.), sommets over cancelled pts, a very cramped parenthesis below the first line, ds over sur, combinatoirement above a deleted line, géomt over two places, and par suite. The cramped parenthesis is not confidently legible: its opening looks more like ce qui implique than the expected geometric qualifier; its right end looks like d'une arête, and the second short line like par un pt donné. This needs explicit candidates. The margin has a question mark, C'est en tous cas faux en car. 2! and two point/ray sketches. The bottom paragraph keeps the unusual combination aucun ... sont non prop.; the word after au in the last full line looks capitalized Centre, although vecteur is another possible reading. The bottom correction 10 and (x,y,z) have insertion guides. The first case label is weak (a) / a dot). The last denominator looks alpha-prime but is low on the edge. Archive pencil 93 only; no manuscript page number.

### Comparison, corrections, and nearby strokes

Re-read the cancelled heading and all six triples in (18), including the two differently signed final second coordinates in the last two rows; retained their visible signs rather than making them agree. Compared every lower prose word, accent, punctuation mark, addition guide and the final two coordinate formulae. The dense parenthesis cannot be resolved confidently. Every surviving candidate remains explicit; no omitted text is supplied from the geometry.

### Indices and exponents

The cancelled heading has s_i; i has no descender and no j appears. The six table subscripts are 0,1,2,3,3,3, with primes on the final two point names. In the bottom line the first excluded point has a digit with a lower hook: s_3 is now the first candidate, s_0 the contextual alternative. Every prime on alpha and the final denominator was checked separately.

### Margins, insertions, and handwriting

The margin question mark, the note C'est en tous cas faux en car. 2 !, and the two sketches are present. The long separator with its left arrow is drawn. The entire upper table and heading remain deleted. Lower deletions: pts, sur, appartiennent à une face, elle, tq, and the superseded last triple. Lower insertions: base-field parenthesis, sommets, the cramped qualifying parenthesis, ds, combinatoirement, two géomt, par suite, 10 and (x,y,z). The horizontal line near alignés is the inserted-text guide, not a cancellation of alignés; the line through the old face phrase is a cancellation. Underlining of sauf and faux is retained.

### Alphabet candidates

Ordinary s and Greek alpha; ordinary underlined a. No double-struck, Gothic or script capital. The word Centre has a capital-shaped C and is not silently replaced by the expected vecteur. Acute É, é in alignés/vérifications/géomt and grave à were checked against the enlarged crops; the abbreviated quelc. remains uncertain.

### Changes

Cramped parenthesis: non antipodiques -> ce qui implique|non antipodiques; provenant d'une arête -> provenant d'une arête|incidents à une arête. Bottom: aucun des -> unsure{aucun des|aucun que les}; s_0 in distincts de -> unsure{s_3|s_0}; au vecteur|au Centre -> au Centre|au vecteur. These changes mark ink uncertainty; they do not assert that the resulting sentence is mathematically or grammatically correct.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 2:

```latex
$s_i,s_3',s_3''$
```

2. TeX line 3:

```latex
\[
\left\{\begin{aligned}
&\deleted{\underline a s_0=(1,-\frac1\alpha,-\frac1\alpha)=(1,-1-\alpha,-1-\alpha)=(1,\unsure{\alpha'},\alpha')}\\
&\deleted{\underline a s_1=(0,-\frac1\alpha,-\frac1\alpha)=(0,-1-\alpha,-1-\alpha)=(0,\alpha',\alpha')}\\
&\deleted{\underline a s_2=(1,-\frac1\alpha-1,-\frac1\alpha)=(1,-2-\alpha,-1-\alpha)=(\unsure{1|\alpha'},\alpha'-1,\alpha')}\\
&\deleted{\underline a s_3=(1,-\frac1\alpha,-\frac1\alpha-1)=(1,-1-\alpha,-2-\alpha)=(1,\alpha',\alpha'-1)}\\
&\deleted{\underline a s_3'=(2+\alpha,-2(1+\alpha),-(2+\alpha))=(1-\alpha',-2\alpha',\alpha'-1)}\\
&\deleted{\underline a s_3''=(1,-2(1+\alpha),-(2+\alpha))=(1,2\alpha',\alpha'-1)}
\end{aligned}\right.
\tag*{\deleted{(18)}}
\]
```

3. TeX line 17:

```latex
$=$
```

4. TeX line 17:

```latex
$=$
```

5. TeX line 24:

```latex
$s_0$
```

6. TeX line 24:

```latex
$\underline a s_0$
```

7. TeX line 24:

```latex
$(x,y,z)$
```

8. TeX line 24:

```latex
$\unsure{s_3|s_0},\underline a s_0$
```

9. TeX line 25:

```latex
\[
\underline a s_0=(\alpha',1-\alpha',1-\alpha')\deleted{\unsure{=(1,-1-\alpha,-1-\alpha)}}
\]
```

10. TeX line 29:

```latex
\[
\frac1{\unsure{\alpha'}}\underline a s_0=(1,\alpha',\alpha')
\]
```


## Scan 095

Start: 2026-11-17T23:59:08.350357+00:00  
End: 2026-11-17T23:59:51.700930+00:00

### Observations recorded before opening the page file

Image-first observations: the short opening is an underlined, dark OK/Or followed by C'est vrai.; a small star-like sign stands in the left margin. Cases b) and c) both say La droite joignant, with the descender of j plainly visible; it is not an i. The first names s_0 and s_1; the second s_0 and s''_3, with two primes throughout. The initial vecteurs before -sommets is struck. Each case ends C'est vrai. The shorthand in case c) looks aut. som.; the two coordinates are (0,1+alpha,1) and (0,-alpha',1). Lower words and accents: deuxième pt, fastidieux, seulement, intéressé, distincts (inserted above the line), à ceci, Aucune/Aucun (the final shape is n), coordonnée, nulle, heureux! The sentence preserves the abbreviated pts and i.e.; face is singular. The formula near the end is just coordinate z, not a Greek letter. Lower third is otherwise blank; archive pencil 94. No date or page number in the manuscript's own hand.

### Comparison, corrections, and nearby strokes

Read both complete cases, their triples and all intervening prose, then the face-plane paragraph. Checked the three occurrences of C'est vrai, the case labels b) and c), the hyphen left before sommets after cancelling vecteurs, singular face, the final dash and exclamation mark. No change.

### Indices and exponents

The point indices 0,1,3 and 2 are digits. Every s_3 in case c) has two primes. The only j is in the prose word joignant, with a clear descender; there is no i/j index or exponent. The alpha in the first triple is unprimed and that in the second is primed; z in the final paragraph is ordinary z.

### Margins, insertions, and handwriting

The uncertain star-like margin mark is retained. The sole verbal deletion is vecteurs; the sole insertion is distincts above the lower paragraph, placed after 4 pts. The underline under OK/Or is reproduced; the long descenders under joignant and engendrent are not mistaken for cancellations or underlines. The bottom third has no further manuscript text.

### Alphabet candidates

Ordinary s, z and Greek alpha. No script or double-struck letter. The uncertain opening OK|Or, aut. som. and seulement remain explicitly marked. Checked accents on deuxième, intéressé, ramené, coordonnée and à against their strokes.

### Changes

No change.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 3:

```latex
$\unsure{*}$
```

2. TeX line 5:

```latex
$s_0$
```

3. TeX line 5:

```latex
$s_1$
```

4. TeX line 5:

```latex
$s_0,s_1$
```

5. TeX line 5:

```latex
$s_1=(1,0,0)$
```

6. TeX line 9:

```latex
$s_0$
```

7. TeX line 9:

```latex
$s_3''$
```

8. TeX line 9:

```latex
$s_0,s_3''$
```

9. TeX line 10:

```latex
\[
s_3''=(0,1+\alpha,1)
=(0,-\alpha',1)
\]
```

10. TeX line 18:

```latex
$s_0,s_1,s_2$
```

11. TeX line 18:

```latex
$z$
```


## Scan 096

Start: 2026-11-17T23:59:51.724293+00:00  
End: 2026-11-18T00:01:26.311128+00:00

### Observations recorded before opening the page file

Image-first observations: heading Fonctions quadr. invariantes; quadr. has tightly overwritten strokes. Comme les ctes sont invariantes, SPS d=0; ctes has raised tes and SPS is tightly written. L'invariance par sigma_2 ... signifie; Faisons la substitution sigma_0; d'où; i.e.; comme v=a; several ok. No prose accent requiring normalization. Greek lambda, mu, nu occur alongside ordinary coefficient v; their similar strokes require candidates at the first v. The yz and zx in the initial general polynomial are overwritten. The two mapping arrows have a clear starting bar but weak terminal heads. In the reduced polynomial and in the expansion, large crosses pass through the complete b(y^2+z^2), u yz and mu(y+z) summands; they are not merely changes of the coefficients. Underbraces remain visible under the crossed summands in the reduced line. The v-product in the expansion has visible 1-(x+y+z), then a closing parenthesis, then (y+z); nested working braces span parts of it. Detached checking crosses occur under seven expanded terms and over/under each x,y,z in the linear sums. The gathered line has a small inserted -v/+v over b+a, a cancelled mark after 2a, a damaged opening parenthesis before 2a-v, a small circle after the x term, inserted +v over mu, and a cancelled u/v in the constant. Below, the boxed v=a, 2v=2a ok, 2a-v=v ok, -2a-lambda=lambda, partial box 2(lambda+a)=0, and mu comparison lead to boxed lambda=-a. A curved arrow points to two damaged/cancelled equations at right. The subsequent a+v+lambda=0 line is crossed through; v has a small equivalence-to-a note underneath. In the lower f line, -ax is inserted just before the surviving +mu(y+z), not as its coefficient. Two preliminary rewrites are cancelled. A boxed 2a=0 stands at right. Final live line is f(x,y,z)=ax(x+y+z-1)+b(y^2+z^2)+uyz+mu(y+z). Archive pencil 95 only.

### Comparison, corrections, and nearby strokes

Compared the general polynomial, the two substitutions, every expanded and collected monomial, all boxes and working marks, and the last three rewrites. The complete crossed summands were already enclosed in deleted in the saved draft; their state is confirmed. Fixed the transcription's product parentheses and the placement of the inserted -ax from the visible ink, not by deriving the formula. The plus-shaped insertion over b+a remains first even though the alternative minus would fit the computation.

### Indices and exponents

Only sigma_2 and sigma_0 have numeric subscripts; every quadratic exponent is 2. There is no i or j in an index or exponent. Read every x,y,z independently, including the overwritten yz/zx at the top. The three detached crosses over x,y,z and the seven below the expansion are checking marks, not exponents or cancellations of the terms.

### Margins, insertions, and handwriting

The right boxed 2a=0 is retained as a doubtful margin note. Cancellations checked: three complete summands in the reduced polynomial; three complete summands in the expansion; b, u, the small mark after 2a, mu and the constant u/v in the collected line; the two damaged equations at the curved arrow; the full a+v+lambda line with its underside annotation; and the two preliminary bottom rewrites. Insertions checked: coefficient +v|-v, linear +v, the comparison-line +v, and -ax before the surviving +mu(y+z). The small circle after the collected x term is retained. The curved arrow and its endpoint equations are typeset as a diagram.

### Alphabet candidates

Ordinary coefficient v and Greek nu cannot be securely distinguished by this rounded handwritten form, so the first v carries both candidates. Lambda and mu are Greek, f and coefficients a,b,c,d,u,w are ordinary italic. The heading's F is an ordinary initial, not a script symbol; no blackboard/Gothic letter. Mapping bars are clear but arrowheads are not: first candidate is the headless bar-and-stroke vdash, with longmapsto as alternative at the first occurrence.

### Changes

sigma_2 longmapsto -> unsure{vdash|longmapsto}; sigma_0 longmapsto -> vdash (same recurring sign). In the v-product, misplaced braces/parentheses -> visible v(1-(x+y+z))(y+z), with the working over/underbraces retained. Inserted -v|+v -> +v|-v. Right cancelled boxed lambda+2a=0 -> unsure{2lambda+2a=0|lambda+2a=0}. Cancelled v+lambda -> v unsure{+|=} lambda; cancelled lambda=-2a -> lambda=unsure{2a|-2a}. Lower +inserted{-ax}mu(y+z) -> inserted{-ax}+mu(y+z), following the insertion guide.

### Formula checklist

The following displays, inline formulas, and diagram labels were compared symbol by symbol with the crops; the items are recorded verbatim from the resulting page file. Retained doubt marks remain unresolved.

1. TeX line 3:

```latex
\[
f(x,y,z)=ax^2+by^2+cz^2+u\unsure{yz}+\unsure{v|\nu}\unsure{zx}+wxy+\lambda x+\mu y+\nu z+d
\]
```

2. TeX line 6:

```latex
$d=0$
```

3. TeX line 8:

```latex
$\sigma_2:(x,y,z)\unsure{\vdash|\longmapsto}(x,z,y)$
```

4. TeX line 8:

```latex
$b=c$
```

5. TeX line 8:

```latex
$v=w$
```

6. TeX line 8:

```latex
$\mu=\nu$
```

7. TeX line 9:

```latex
\[
f(x,y,z)=ax^2+\deleted{b\underbrace{(y^2+z^2)}}+\deleted{u\underbrace{yz}}+vx(y+z)+\lambda x+\deleted{\mu\underbrace{(y+z)}}
\]
```

8. TeX line 12:

```latex
$\sigma_0:(x,y,z)\vdash(1-(x+y+z),y,z)$
```

9. TeX line 13:

```latex
\[
\begin{aligned}
f\circ\sigma_0(x,y,z)
&=a(\underset{\unsure{\times|\checkmark}}1+\underset{\times}{x^2}+\underset{\times}{y^2}+\underset{\times}{z^2}+\underset{\times}{2yz}+\underset{\times}{2zx}+\underset{\times}{2xy}-2(\overset{\times}x+\overset{\times}y+\overset{\times}z))\\
&\quad+\deleted{b(y^2+z^2)}+\deleted{uyz}+v(1-\overbrace{(x+\underbrace{y+\underbrace{z))(y}+z}})\\
&\quad+\lambda(1-(\underset{\times}x+\underset{\times}y+\underset{\times}z))+\deleted{\mu(y+z)}\\
&=ax^2+(\deleted b+a\inserted{\unsure{+v|-v}})(y^2+z^2)+(\deleted u+2a\deleted{\unsure{y|v}}-2v)yz\\
&\quad+\unsure{(}2a-v)x(y+z)+(-2a-\lambda)x\unsure{\circ|0}\\
&\qquad+(-2a-\lambda+\deleted\mu\inserted{+v})(y+z)+(a+\deleted{\unsure{u|v}}+\lambda)
\end{aligned}
\]
```

10. TeX line 25:

```latex
\[
\begin{aligned}
&\boxed{\unsure{v}=a}\\
&2v=2a\quad\text{ok}\\
&2a-v=v\quad\text{ok}\\
&-2a-\lambda=\lambda\quad\text{i.e.}\quad\lfloor\underline{2}(\lambda+a)=0\\
&\mu=-2a-\lambda\inserted{+v}+\mu\quad\text{i.e.}\quad\boxed{\lambda=-a}\quad\underset{\text{(comme }v=a\text{)}}{}
\end{aligned}
\]
```

11. TeX line 34:

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
{}\arrow[r,bend right=15]\&\deleted{\unsure{2\lambda+2a=0}}\quad\boxed{\deleted{\unsure{2\lambda+2a=0|\lambda+2a=0}}}
\end{tikzcd}
```

12. TeX line 37:

```latex
\[
\deleted{a+\underset{\substack{\parallel\\a}}v\unsure{+|=}\lambda=0\quad\lambda=\unsure{2a|-2a}\quad\text{ok}}
\]
```

13. TeX line 40:

```latex
\[
f(x,y,z)=ax^2+b(y^2+z^2)+uyz+ax(y+z)\inserted{-ax}+\mu(y+z)
\]
```

14. TeX line 43:

```latex
$\boxed{\unsure{2a=0}}$
```

15. TeX line 44:

```latex
\[
\begin{aligned}
&\deleted{=ax(x+y+z)+b(y^2+z^2)+uyz+\mu(y+z)}\\
&\deleted{\unsure{=a[x^2+x(y+z)-x]}}
\end{aligned}
\]
```

16. TeX line 50:

```latex
\[
f(x,y,z)=ax(x+y+z-1)+b(y^2+z^2)+uyz+\mu(y+z)
\]
```


## Final notation and annotation reconciliation

The image-derived notation records for scans 083–096 were compared with the final page fragments. Ordinary R/G/D/S/T, double-stroked E/F, the Z alphabet doubt, the Gothic-z candidate, Greek lambda/mu/nu/alpha, the distinct coefficient v on 096, underlined versus plain a, primes/double primes, degree signs, quotation marks and shorthand equals signs were reconciled. Local ink differences remain local doubts: the subscript 2|3 on 088, alpha|2 on 090, the field letters on 092 and the headless mapping sign on 096 were not normalized from their context. No heading letter was assigned an alphabet from a body-text convention.

Additional annotation check on scan 094: `géomt` -> `géom\textsuperscript{t}` at both insertions, preserving the visibly raised final t recorded during the first reading. The drawn guide from the marginal objection to the vertical stroke beside the questioned paragraph was added to the existing two-point sketch. These are placement/annotation corrections, not mathematical emendations. No other page reading changed during reconciliation.

Reconciliation completed: 2026-11-18T00:08:59.639495+00:00 (UTC).

The final inventory contains 262 rows. Grouped checkpoint annotations were split into individual deletion/insertion/margin elements and ordered by their place in the final fragments. All are marked yes. The doubt register contains all 138 uncertainty occurrences.

For scan 083, the co-located coordinate definitions, flag constraints, point actions, vector actions and matrices were also separated into their individual manuscript blocks rather than treated as one large TeX display.

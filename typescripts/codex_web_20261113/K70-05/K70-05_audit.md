# K70-05 — second reading audit

The observations under “Crop reading before opening the page file” were recorded before reopening that page’s transcription in this pass. Times are actual UTC timestamps. Formula lists reproduce the checked transcription, including doubt and deletion marks; they are not assertions of mathematical correctness. The same reader performed both passes.

## Scan 067

Start: 2026-11-17T21:15:40+00:00; end: 2026-11-17T21:16:35+00:00.

Crop observations recorded: 2026-11-17T21:15:59+00:00.

### Crop reading before opening the page file

From crops before reopening: “Ce n’est pas un … plan sauf si”, “cas d’un corps de base” (corps underlined), “c’est un hyperplan ssi”, “coplanaires ssi somme des coord.”, “il suffit” (suffit underlined), “On suppose par la suite”, “et on pose”. Prefix before plan is crossed over. The first S subscript of the coplanarity line is not a clear 0. Tall ξ-like and broad ζ-like signs remain distinct. Formula separators are commas; matrices have subscripts 0,1,2, no i/j. Last matrix three thick zeroes are not exponents. A curved linking arrow joins parts of the coplanarity equality; there is no second copy of that equality on the page.

### Checks and changes

Checked all three crops, with an extra enlarged coplanarity crop. The two fixed-point systems, all coordinate triples, every entry of the three 4×4 matrices, affine expressions, λ and η definitions and boxed assumptions were compared. Subscripts: σ0,σ1,σ2; S3/S2 ambiguity at the first vertex, S1,S2,S3 double-prime elsewhere; no i/j. ξ versus ζ, η, μ, λ checked against their own shapes; no double-struck/script capitals. Cross-outs: initial word, hyper prefix, third σ1 condition, repeated c’est un, coplanarity continuation and final mark after β. The underline under corps and the box/curved arrow are not deletions. No sideways margin note; right parenthesis “cas d’un corps de base” is live.

Changes: duplicated coplanarity expressions in a separate arrow diagram -> one diagram containing the equality once and its curved arrow; first S_3 -> S_{\unsure{3|2}}; “supposera” -> \unsure{supposera|suppose}. Remaining readings unchanged.

### Formulas checked, in transcription order

1.

```latex

\[
\begin{aligned}
&\sigma_0(x,y,z)=(x,y,z)\\
&\Updownarrow\\
&\mu y=y,\ \mu z=z,\ 2x+(1-\lambda)(y+z)=1
\end{aligned}
\]

```

2.

```latex

$\mu=1$

```

3.

```latex

\[
\begin{aligned}
&\sigma_1(x,y,z)=(x,y,z)\\
&\Updownarrow\\
&-x+y+\unsure{\xi|\zeta}z=0,\ -x+y-\eta z=0,\ \deleted{\unsure{(1+\zeta)z}}\unsure{\zeta|\xi}z=0
\end{aligned}
\]

```

4.

```latex

$\zeta=0,\ \xi=-\eta$

```

5.

```latex

$S_{\unsure{3|2}},S_1,S_2,S''_3$

```

6.

```latex

$S''_3=1$

```

7.

```latex

\begin{tikzcd}[ampersand replacement=\&,row sep=small]
\Updownarrow\&\\
\xi+\eta\deleted{\unsure{+\zeta=0}}=\zeta\arrow[r,bend right=25]\& (=\xi\zeta=\eta\zeta)
\end{tikzcd}

```

8.

```latex

$\zeta=0$

```

9.

```latex

$\left[\vphantom{\begin{matrix}1\\1\end{matrix}}\right.$

```

10.

```latex

$\boxed{\zeta=0,\ \mu=1}$

```

11.

```latex

\[
\left\{\begin{aligned}
\lambda&=1+\beta\deleted{\unsure{\alpha}}\\
\eta&=1+\alpha
\end{aligned}\right.
\]

```

12.

```latex

\[
\sigma_0=\begin{pmatrix}
-1&\beta&\beta&1\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}
\qquad
\sigma_0(x,y,z)=(1-x+\beta(y+z),y,z)
\]

```

13.

```latex

\[
\sigma_1=\begin{pmatrix}
0&1&-(1+\alpha)&0\\
1&0&1+\alpha&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}
\qquad
\sigma_1(x,y,z)=(y-(1+\alpha)z,x+(1+\alpha)z,z)
\]

```

14.

```latex

\[
\sigma_2=\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix}
\qquad
\sigma_2(x,y,z)=(x,z,y)
\]

```

### Supplementary source check

2026-11-17T21:35:44+00:00

All three thirds reread during notation reconciliation. Checked tall xi, broad zeta, eta, mu, lambda and sigma against the original strokes; all 48 matrix entries and affine coordinate maps checked once more. The initial S subscript remains 3/2; the ink does not justify replacing it by the expected 0.

No further change.

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{ssi} -> \unsure{ssi|ss}

## Scan 068

Start: 2026-11-17T21:16:35+00:00; end: 2026-11-17T21:17:51+00:00.

Crop observations recorded: 2026-11-17T21:17:03+00:00.

### Crop reading before opening the page file

Crop-only observations: heading “Forme quadratique invariante” with possible final s; hyphenated “…mi-cyclotomique” (initial letter requires zoom); “Conditions sur les coeff.”; “Comme les ctes sont inv. OPS d=0”; “L’invariance p.r. à”; “d’autre part”; “i.e. symétrie en y,z”; “On va exprimer”; “en notant”; “d’où la forme ou la … quadratique fondamentale”. A word before quadratique is struck and a shortened form is added. Exact-order side conditions are additions above the equivalences. Fp,Fq are ordinary capitals, not script or double struck. In ρ subscripts, s and f differ; exponent d not i, and “id” is ordinary text. Cross-outs run through whole intermediate prose lines and two formulas, but the final formula for u remains live.

### Checks and changes

Both ρ products and exact-order insertions checked: s,f subscripts; p,q,d exponents; strict 0<d<p and 0<d<q. No i or j index/exponent: id is the word id. Checked all ten general quadratic coefficients, z=0, a=b=-p=-q, w=-βa with retained β² alternative, c=b,v=w,r=q; the f display, uy z, the two σ labels in prose, cancelled a[...] and both final u lines. The added minus before βx(y+z) is now explicitly doubtful. All cancellations under the invariance argument were compared with the crop; the underline in the heading and the coefficient-group strokes are not cancellations. Fp/Fq are plain F, and the second annotation is a pair of ditto marks. No sideways margin or handwritten-on-typescript addition. Enlargements used for demi-cyclotomique and the final overwritten prose.

Changes: “semi-cyclotomique” -> “demi-cyclotomique”; inserted -βx(y+z) -> \unsure{-βx(y+z)|βx(y+z)}. Other text, formulas and deletion state unchanged.

### Formulas checked, in transcription order

1.

```latex

\[
\rho_s=\sigma_1\sigma_2\qquad\rho_f=\sigma_0\sigma_1
\]

```

2.

```latex

\[
\begin{aligned}
\rho_s^p=\mathrm{id}\ \inserted{\rho_s^d\ne\mathrm{id}\text{ si }0<d<p}
&\Longleftrightarrow\deleted{\unsure{\Phi}}F_p(\alpha)=0
&&F_p\text{ polynôme demi-cyclotomique}\\
\rho_f^q=\mathrm{id},\ \inserted{\rho_f^d\ne\mathrm{id}\text{ si }0<d<q}
&\Longleftrightarrow F_q(\beta)=0
&&F_q\quad\text{``}
\end{aligned}
\]

```

3.

```latex

$x,y,z,t$

```

4.

```latex

\[
\underline{ax^2+by^2}+cz^2+\underline{uyz}+\underline{vzx}+\underline{wxy}+\underline{px+qy+rz}+d
\]

```

5.

```latex

$d=0$

```

6.

```latex

$\sigma_0,\sigma_1$

```

7.

```latex

$xy$

```

8.

```latex

$(z=0)$

```

9.

```latex

$a=b=-p=-q$

```

10.

```latex

$w=-\unsure{\beta|\beta^2}a$

```

11.

```latex

$\sigma_2$

```

12.

```latex

$y,z$

```

13.

```latex

$c=b,v=w,r=q$

```

14.

```latex

\[
f(x,y,z)=a\bigl[x^2+y^2+z^2\deleted{\unsure{-\beta xy-\beta xz}}\inserted{\unsure{-\beta x(y+z)|\beta x(y+z)}}-x-y-z\bigr]+uyz
\]

```

15.

```latex

$\sigma_0\inserted{\text{ puis }}\sigma_1$

```

16.

```latex

$uyz$

```

17.

```latex

$\sigma_0$

```

18.

```latex

\[
\deleted{a[x^2+y^2-\unsure{\alpha|\beta}xy-x-y]}
\]

```

19.

```latex

$a[\text{---}]$

```

20.

```latex

$z=0$

```

21.

```latex

$\sigma_1$

```

22.

```latex

$\sigma_0,\sigma_1$

```

23.

```latex

$u=$

```

24.

```latex

\[
\begin{aligned}
&\deleted{u=-a(\beta+2(1+\alpha)+}\\
&u=-a(2+2(\alpha+\beta)+\alpha\beta)
\end{aligned}
\]

```

### Supplementary source check

2026-11-17T21:37:30+00:00

All thirds reread for rho_s/rho_f, sigma indices 0/1/2, p/q/d exponents, the demi-cyclotomique wording, handwritten insertion puis, and the overwritten beta coefficient. Read every line of the derivation again, including the cancelled lower draft.

No further change; sign in the inserted beta term remains doubtful.

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{les ctes} -> \unsure{les ctes|les cte}; \unsure{fon.} -> \unsure{fon.|form.}

## Scan 069

Start: 2026-11-17T21:17:51+00:00; end: 2026-11-17T21:19:16+00:00.

Crop observations recorded: 2026-11-17T21:18:12+00:00.

### Crop reading before opening the page file

Crop-only: “Les fonctions sous-quadratiques inv. par … sont donc les combinaisons linéaires de f et de la constante 1. Celles qui s’annulent sur les sommets du polyèdre, i.e. en S0=(0,0,0), sont les multiples de f.” “Matrice de f0” and parenthesis resembling “pratiquement”; “discr. divisé”; “Dans cas ico.”; “OK !”; “il est inv …”; “L’unique pt invariant …”; “l’antipodisme est donné par”. Sideways note starts NB and contains f0; needs rotated inspection. The determinant note in the right margin has a long downward arrow. The small bottom note refers to p, q, sommets and faces. No i/j indices; 0 in f0, S0 and o (centre) require separate checks. Capital group letter could be Γ or script G; f is not script. All determinant primes and squared factors are distinct.

### Checks and changes

Full quadratic polynomial checked including the underbrace γ=(α+2)(β+2)-2. Every entry of both matrices compared (3×3: 2,-β,-β / -β,2,-γ / -β,-γ,2; 4×4 adds -1 row/column and lower-right 0). δ′ formula and factorization, both γ expressions, δ(f), norm note and all invertibility conditions checked. Centre o and all three denominators 2(α+β), then all antipodism components and denominators α+β checked individually. No i/j index: subscript 0 in S0,f0,σ0 and ordinary i.e. only. Group capital remains Γ|script G; field letters in the norm are double-stroke candidates retained as Q. Every right marginal note reread; bottom p/q and finite qualifier remain doubtful. Left sideways NB note rotated -45,-65,-90 degrees: it appears to have a second-line f preceding the bilinear word, with no clearly separate trailing word. Slanted invertibility notes were reread separately. Cross-outs: sign in α condition, initial sign before -α-3, sign before cos, sign before centre numerator. Underlines, circled norm and matrix grouping brace are live graphical marks.

Changes: “partie homog” -> \unsure{partie hom|partie homog}; sideways “… bilinéaire|bilinéarisée [illeg.1]” -> “… f bilinéaire|bilinéarisée|bilinéarisation”, with f doubtful; duplicated contents of the long-arrow diagram -> empty endpoints, retaining each margin note once. Remaining readings unchanged.

### Formulas checked, in transcription order

1.

```latex

\[
f(x,y,z)=x^2+y^2+z^2-\underbrace{(2+2(\alpha+\beta)+\alpha\beta)}_{\gamma=(\alpha+2)(\beta+2)-2}yz-\beta zx-\beta xy-(x+y+z)
\]

```

2.

```latex

$\unsure{\Gamma|\mathscr{G}}$

```

3.

```latex

$f$

```

4.

```latex

$1$

```

5.

```latex

$S_0=(0,0,0)$

```

6.

```latex

$f$

```

7.

```latex

\[
\left\{\begin{aligned}
\text{Matrice de }f_0\ \text{(\unsure{partie hom|partie homog|partie hom.})}&=\begin{pmatrix}
2&-\beta&-\beta\\-\beta&2&-\gamma\\-\beta&-\gamma&2
\end{pmatrix}\\
\delta'\ (\text{discr. divisé})&=4-\beta^2(\gamma+2)-\gamma^2\\
&=-(\alpha+2)(\beta+2)^2(\alpha+\beta)
\end{aligned}\right.
\]

```

8.

```latex

$\alpha^2\unsure{+|-}\alpha-1=0$

```

9.

```latex

$\beta=-1$

```

10.

```latex

$\gamma=\alpha$

```

11.

```latex

$\delta'=1$

```

12.

```latex

\[
\left[\begin{aligned}
\text{inv. ssi }&\alpha\text{ partout }\ne\deleted{\unsure{+}}-2\\
&\beta\text{ partout }\ne-2\\
&\alpha+\beta:\text{ partout }\ne0
\end{aligned}\right]
\]

```

13.

```latex

$\alpha=\unsure{2\cos\frac{\pi}{p},q|2\cos\frac{\pi}{p,q}}$

```

14.

```latex

\[
\gamma=2(1+\alpha+\beta)+\alpha\beta
\]

```

15.

```latex

$f_0$

```

16.

```latex

$\unsure{f}$

```

17.

```latex

\[
\text{Matrice de }f=\begin{pmatrix}
2&-\beta&-\beta&-1\\
-\beta&2&-\gamma&-1\\
-\beta&-\gamma&2&-1\\
-1&-1&-1&0
\end{pmatrix}
\]

```

18.

```latex

\[
\delta(f)=(\gamma+2)(\gamma-4\beta-6)=(\alpha+2)(\alpha-2)(\beta+2)^2
\]

```

19.

```latex

$\delta(f)=\deleted{\unsure{4}}-\alpha-3$

```

20.

```latex

$N_{\mathbb{Q}(\alpha)/\mathbb{Q}}\delta(f)=5$

```

21.

```latex

\begin{tikzcd}[ampersand replacement=\&]
{}\arrow[d,bend left=15]\\{}
\end{tikzcd}

```

22.

```latex

$\alpha$

```

23.

```latex

$\ne\pm2$

```

24.

```latex

$\deleted{\unsure{4}}\unsure{2\cos\frac{\pi}{p}}$

```

25.

```latex

$\beta$

```

26.

```latex

$\ne-2$

```

27.

```latex

$\unsure{2\cos\frac{\pi}{q}}$

```

28.

```latex

$p=\unsure{n}$

```

29.

```latex

$q:$

```

30.

```latex

$p,q$

```

31.

```latex

$\sigma_0,\sigma_1,\sigma_2$

```

32.

```latex

$\Gamma$

```

33.

```latex

\[
o=\left(\frac{\deleted{\unsure{-}}\alpha}{2(\alpha+\beta)},\frac{-1}{2(\alpha+\beta)},\frac{-1}{2(\alpha+\beta)}\right)
\]

```

34.

```latex

$2(\alpha+\beta)$

```

35.

```latex

\[
\underline{a}(x,y,z)=\left(\frac{\alpha}{\alpha+\beta}-x,\frac{-1}{\alpha+\beta}-y,\frac{-1}{\alpha+\beta}-z\right)
\]

```

36.

```latex

$\alpha+\beta$

```

### Supplementary source check

2026-11-17T21:35:44+00:00

Enlarged the marginal icosahedron polynomial independently of the table on scan 70. The first sign has a short bent/right-descending stroke unlike the following straight minus; + is now the first reading, with - retained as an alternative because the tiny stroke is weak. The two matrices and gamma definition were also compared again.

alpha²-alpha-1=0 -> alpha² unsure{+|-} alpha-1=0. This was an earlier reading error, not an authorial slip established by calculation.

### Supplementary source check

2026-11-17T21:37:30+00:00

Bottom third reread in full, including the norm field, cosine fractions, p/q marginal note, centre o and both slanted invertibility conditions. The short group capital is not forced to match the clearer form on scan 81.

No additional change.

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{partie hom|partie homog} -> \unsure{partie hom|partie homog|partie hom.}

## Scan 070

Start: 2026-11-17T21:19:16+00:00; end: 2026-11-17T21:20:49+00:00.

Crop observations recorded: 2026-11-17T21:19:34+00:00.

### Crop reading before opening the page file

Crop-only observations: “On vérifie que f est invariante par a, et”; faint line below, then cancelled f(o) fraction and boxed (2-α)/(4(α+β)). “C’est nul ssi α=2” begins a heavily revised paragraph; visible “sommets”, “circonscrite”/“circonscrit”, “singulière”. Table names: Cas tétraèdre; cube written above a cancelled octaèdre; octaèdre above a cancelled cube; icosaèdre; dodécaèdre; pentagramme (last word less secure). Repeated phrases “centre à l’inf”, “f0 singulier”, “tjrs régulier”, “f sing.”, “birég.” and “dist. finie”; row conditions need numeral-by-numeral comparison. Final “Il y a … un pol. rég. … birégulier mais son dual ne l’est pas … car. 3 … 3(ico),5(dodéc)”. A question-like isolated mark and cancellations stand at the left of this last remark. Script/capital Q with E subscript remains a notation candidate; signs under it are not primes. The α,β equations include both +α-1 and -α-1 on different rows.

### Checks and changes

Each of the six table rows checked against its own crop, without importing values from adjacent rows. Checked f(o), its cancelled fraction and α=2; tetra α=β=-1,δ′2,δ-3; cube α-1,β0,δ′+4,δ-12; octa α0,β-1,δ′2,δ-4; ico quadratic,β-1,δ′1,δ-α-3,N5; dodeca quadratic and all cancelled calculations,δ′β+2,N1,δ expression and -9β-15,N9; pentagramme λ polynomial,αβ-1,β=-1/α=-1-α,δ′α+2,N1,δ4α-3,N5. Every characteristic condition and Q_E entry checked individually (2,3,5 are not standardized). f0 subscripts and δ primes checked; no i/j. E/barE uncertainty remains at first Q occurrence. Cube/octa labels are overwritten; underlines beneath names remain live. Final insertion fini, cancelled aside and cancelled numerals all retained. Extra enlargements of dodeca factor, initial prose and final paragraph used.

Changes: dodeca (β+2)² -> (\unsure{β-1|β+1})²; omitted doubtful word after “la qu.” -> \unsure{d’origine}; singulière gains its underline; extra cube/octa text in arrow-only diagram removed; marginal ! -> doubtful ?; encore -> enfin|encore; c’est le cas -> c’est le cas|c’est. The surprising subsequent -9β-15 remains unchanged.

### Formulas checked, in transcription order

1.

```latex

$f$

```

2.

```latex

$\underline{a}$

```

3.

```latex

\[
\deleted{f(o)=\frac{-\alpha^2-\alpha\beta+2(\alpha+\beta)}{4(\alpha+\beta)^2}}
\qquad\boxed{f(o)=\frac{2-\alpha}{4(\alpha+\beta)}}.
\]

```

4.

```latex

$\alpha=2$

```

5.

```latex

$p>0$

```

6.

```latex

\(\begin{array}{ll|l}
\begin{gathered}
\text{\uline{Cas tétraèdre}}\quad\alpha=\beta=-1\\
\delta'=2\quad\delta=-3
\end{gathered}
&\begin{gathered}
\text{centre : à l'}\infty\text{ ssi car. }2\\
f_0\text{ singulier ssi car }2\\
f\text{ singulier ssi car }\deleted{\unsure{2}}3
\end{gathered}
&\begin{gathered}
Q_{\unsure{E|\overline E}}\text{ birégulière ssi}\\
\text{car. }\ne2,3\\
\text{(alors le centre est}\\
\text{à dist. finie)}
\end{gathered}
\end{array}\)

```

7.

```latex

\(\begin{array}{ll|l}
\begin{gathered}
\deleted{\text{\uline{\unsure{Cas octaèdre}}}}\ \inserted{\text{cube}}\quad\alpha=-1,\beta=0\\
\delta'=+4,\quad\delta=-12
\end{gathered}
&\begin{gathered}
\text{centre : à l'}\infty\text{ ssi car. }2\\
f_0\text{ singulier ssi car }2\\
f\text{ singulier ssi car }2,3
\end{gathered}
&\begin{gathered}
Q_E\text{ birég ssi}\\
\text{car}\ne2,3\\
\text{(alors centre à dist.}\\
\text{finie)}
\end{gathered}
\end{array}\)

```

8.

```latex

\(\begin{array}{ll|l}
\begin{gathered}
\deleted{\text{\uline{cube}}}\ \inserted{\text{octaèdre}}\quad\alpha=0,\beta=-1\\
\delta'=2,\quad\delta=-4
\end{gathered}
&\begin{gathered}
\text{centre à l'}\infty\text{ ssi car. }2\\
f_0\text{ sing. ssi car. }2\\
f\text{ sing. ssi car. }2
\end{gathered}
&\begin{gathered}
Q_E\text{ birég ssi}\\
\text{car. }\ne2\\
\text{(alors centre à}\\
\text{dist. finie)}
\end{gathered}
\end{array}\)

```

9.

```latex

\begin{tikzcd}[ampersand replacement=\&]
{}\\{}\arrow[u,bend left=45]
\end{tikzcd}

```

10.

```latex

\(\begin{array}{ll|l}
\begin{gathered}
\text{\uline{icosaèdre}}\quad\left\{\begin{aligned}
&\alpha\text{ satisfaisant }\alpha^2+\alpha-1=0\\
&\beta=-1
\end{aligned}\right.\\
\delta'=1\deleted{\unsure{\alpha}},\quad\delta=-\alpha-3\\
N(\delta)=5
\end{gathered}
&\begin{gathered}
\text{centre à l'}\infty\text{ ssi car. }2\\
f_0\text{ tjrs régulier}\\
f\text{ sing. ssi car. }5
\end{gathered}
&\begin{gathered}
Q_E\text{ birég ssi}\\
\text{car. }\ne5\\
\text{(le centre peut}\\
\text{être à l'}\infty\text{ !)}
\end{gathered}
\end{array}\)

```

11.

```latex

\(\begin{array}{ll|l}
\begin{gathered}
\text{\uline{dodécaèdre}}\quad\alpha=-1,\ \beta\text{ satisfaisant }\deleted{\unsure{\beta^2+\beta=0}}\\
\beta^2+\beta-1=0\\
\deleted{\delta'=\unsure{\beta^2+\beta}}\quad\deleted{N(\delta')=\unsure{5|9}\,!}\\
\deleted{\unsure{\delta}=}\quad\delta'=\beta+2\quad N(\delta')=1\\
\delta=-3(\unsure{\beta+1|\beta-1|\beta+2})^2\quad N(\delta)=9\\
=-9\beta-15
\end{gathered}
&\begin{gathered}
\text{centre à l'}\infty\text{ ssi car }2\\
f_0\text{ tjrs régulier}\\
f\text{ sing. ssi car }3
\end{gathered}
&\begin{gathered}
Q_E\text{ bir}\unsure{\text{ég}}\text{ ssi}\\
\text{car. }\ne3\\
\text{(le centre peut}\\
\text{être à l'}\infty\text{)}
\end{gathered}
\end{array}\)

```

12.

```latex

\(\begin{array}{ll|l}
\begin{gathered}
\text{\uline{\unsure{pentagramme|pentagone}}}\quad\alpha,\beta\text{ solutions de}\\
\lambda^2+\lambda-1=0,\quad\alpha\beta=-1\\
\beta=-1/\alpha=-1-\alpha\\
\delta'=\deleted{\unsure{\beta}}\alpha+2\quad N(\delta')=1\\
\delta=4\alpha-3\quad N(\delta)=5
\end{gathered}
&\begin{gathered}
\text{centre : à l'}\infty\text{ ssi car }2\\
f_0\text{ tjrs régulier}\\
f\text{ singulier ssi car }5
\end{gathered}
&\begin{gathered}
Q_E\text{ birég ssi}\\
\text{car. }\ne5\\
\text{(le centre peut}\\
\text{être à l'}\infty\text{)}
\end{gathered}
\end{array}\)

```

13.

```latex

$\ne0$

```

14.

```latex

$3\deleted{\unsure{,5,6}}$

```

15.

```latex

$3$

```

16.

```latex

$5$

```

### Supplementary source check

2026-11-17T21:35:44+00:00

Enlarged both polynomial lines. The icosahedron and dodecahedron first signs both have a visible vertical stub on a horizontal stroke, unlike the second minus. Rechecked the disputed factor in the dodecahedron row: beta+1 has the best outline, beta-1 and beta+2 remain allowed. The following expansion was not altered.

alpha²-alpha-1=0 -> alpha²+alpha-1=0; beta²-beta-1=0 -> beta²+beta-1=0; factor alternatives beta-1|beta+1 -> beta+1|beta-1|beta+2.

### Supplementary source check

2026-11-17T21:37:30+00:00

Top and bottom thirds reread in full: f(o), the origin/circumscribed-quadric wording, six characteristic conditions, the cancelled case names, the duality sentence and marginal question mark.

No additional change beyond the explicitly logged polynomial signs and factor alternatives.

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{invariante} -> \unsure{invariante|invariant}; \unsure{pentagramme} -> \unsure{pentagramme|pentagone}

## Scan 071

Start: 2026-11-17T21:20:49+00:00; end: 2026-11-17T21:21:48+00:00.

Crop observations recorded: 2026-11-17T21:21:20+00:00.

### Crop reading before opening the page file

Before opening: boxed F(X,Y,Z) and denominator 4(α+2); prose “(Origine reportée à o)” lies directly on the box border, so deletion status needs reconsideration. No other prose. Strict inequalities -2<α<2 and 0<4(α+2)<16. The change-of-variable rows have U, W, V with heavy overwriting. Underbrace to the constant ends in λ>0 after a cancelled prior label. Middle G/E capital is open and crossed, not safely distinguishable. One later relation uses visibly smaller u,v,w. Cancelled ρ,σ,0; cancelled W²-ρUV+σ=0 and ρUV=W²+σ; bottom has YZ variants of those and a live W²=U²+V²+1. Two axes drawings, first heavily cancelled, second clean; lowercase w/u versus capital U/W requires doubt. No i/j or numerical indices.

### Checks and changes

Compared every term of boxed F, the constant’s underbrace and prior label; both strict inequalities; 4YZ identity; each of the three substitution equations including old W,V and final U,W,V. Compared G|E, all squared letters, the cancelled coefficient and fraction, the surviving 1, the cancelled ρ/σ condition, both small middle equations, and all four cancelled UV/YZ expressions. No i/j or numerical subscripts. Final W²=U²+V²+1 checked. Drawings checked for the horizontal, vertical and sloping axes, dots, cancellation strokes and every label. Second drawing w,V,u|U preserves case as seen. The large top F is plain roman, not double struck; G|E remains ambiguous. The box-border line through Origine is not treated as an independent deletion. There is no typed text or marginal prose.

Changes: deleted (Origine reportée à o) -> live parenthesis with a comment documenting the box border and an uncertainty entry for its state; cancelled ρUW -> ρ\unsure{UW|UV}. All other formulas and drawn labels unchanged.

### Formulas checked, in transcription order

1.

```latex

\[
\boxed{F(X,Y,Z)=(-X+Y+Z)^2-4(\alpha+2)YZ+\underbrace{\frac{2-\alpha}{4(\alpha+2)}}_{\deleted{\unsure{\beta''|\rho''}}\ \lambda>0}}
\]

```

2.

```latex

$o$

```

3.

```latex

\[
\begin{aligned}
-2<\alpha<2\\
0<4(\alpha+2)<16
\end{aligned}
\]

```

4.

```latex

\[
4YZ=(Y+Z)^2-(Y-Z)^2
\qquad
\left\{\begin{aligned}
\deleted{\unsure{\rho}}-X+Y+Z&=\deleted{\unsure{W}}U\sqrt{\lambda}\\
\sqrt{\alpha+2}(Y+Z)&=\deleted{V}W\sqrt{\lambda}\\
\sqrt{\alpha+2}(Y-Z)&=\deleted{W}V\sqrt{\lambda}
\end{aligned}\right.
\]

```

5.

```latex

\[
\unsure{G|E}(U,V,W)=U^2\deleted{\unsure{-}}+\deleted{\unsure{\frac{(\alpha+2)}{\rho}}}(\deleted{\unsure{W}}V^2-\deleted{\unsure{V}}W^2)+\deleted{\underbrace{\frac{2-\alpha}{4(\alpha+\unsure{2|\beta})}}_{\lambda}}1
\]

```

6.

```latex

\[
\deleted{\rho,\unsure{\sigma}\ge0}
\qquad\begin{aligned}
U^2+V^2-W^2+\deleted{\lambda}1&=0\\
u^2&=v^2+w^2+\unsure{\lambda}
\end{aligned}
\]

```

7.

```latex

\[
\deleted{W^2-\rho UV+\sigma=0}\qquad\deleted{\rho\unsure{UW|UV}=W^2+\sigma}
\]

```

8.

```latex

\[
\deleted{W^2-\rho U\deleted{W}V}\qquad
\deleted{\unsure{\rho}\quad W^2-\rho YZ+\sigma=0}
\]

```

9.

```latex

\[
\deleted{\rho YZ=W^2+\sigma}
\qquad W^2=U^2+V^2+1
\]

```

10.

```latex

$\unsure{u}$

```

11.

```latex

$\unsure{v|z}$

```

12.

```latex

$\deleted{\unsure{w}}$

```

13.

```latex

$\deleted{\unsure{u|w}}$

```

14.

```latex

$w$

```

15.

```latex

$V$

```

16.

```latex

$\unsure{u|U}$

```

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\deleted{\underbrace{\frac{2-\alpha}{4(\alpha+2)}} -> \deleted{\underbrace{\frac{2-\alpha}{4(\alpha+\unsure{2|\beta})}}}; u^2&=v^2+w^2+\lambda -> u^2&=v^2+w^2+\unsure{\lambda}

### Supplementary source check

2026-11-17T21:41:35+00:00

All three thirds reread, followed by an enlargement of the cancelled constant. The denominator character is covered by diagonal strokes, so 2/beta is now explicit. The smaller u,v,w line is visibly lower case; the last lambda may be touched by a cancellation and is now doubtful. Rechecked all drawing labels and axis strokes.

Cancelled denominator 2 -> unsure{2|beta}; lambda in the smaller line -> unsure{lambda}.

### Supplementary source check

2026-11-17T21:44:07+00:00

Static balance check found one extra closing brace introduced while adding the denominator alternative.

Removed the extra brace before the underbrace subscript; syntax only, no reading changed.

## Scan 072

Start: 2026-11-17T21:21:48+00:00; end: 2026-11-17T21:22:51+00:00.

Crop observations recorded: 2026-11-17T21:22:14+00:00.

### Crop reading before opening the page file

Crop-only: the entire opening block has large diagonal cancellation lines. Words: “Nous allons examiner de plus près le cas où”, “racines de polynômes ½ cyclotomiques”, “sans exclure”, “correspondent”, “aux valeurs”, “le cas réel” (réel underlined), “Si on veut obtenir une … de la réalisation topologique de la carte combinatoire”, “pour p resp. q finis ≥3”, “d’autre part”, “croisements”, “il faut”. Local cancellations are visible within the already struck block. Lower uncancelled text: “qui n’est nul que si α=-2, cas que nous avons exclu…”. δ′ and f0 subscripts checked visually; ζ/η root glyph and n/η exponent denominator are candidates, not i/j. R has an extra stroke. In the lower first f0 equality the marker after the triple is heavily inked; second f0 final form is clear.

### Checks and changes

The opening paragraph remains wholly inside deleted, including its locally inserted resp., et, plongement and ou β=-2 and its locally cancelled words. Checked α,β; Fp and Fq|s; p,q≥1; cases 1,2; values 2,-2; k=R; C_{p,q}; finite p/q≥3; ζ+ζ^-1; ζ=exp 2iπ/n with explicit i; n=p resp.q; α=-2,β=-2; both infinity cases and resulting 2 values. There are no i/j subscripts or exponents; the i is a factor in the exponential argument, not silently omitted. In the live calculation checked β=2,α≠-2, both γ equalities and γ+2, all four δ′ expressions, the -16 factor, both f0 lines, the cancelled xy and final completed-square expression. R is doubled, F and C plain capitals. No diagrams or separate margins. Accent on près and réel, and paragraph-ending ellipsis, retained.

Changes: “racines des polynômes” -> “racines de polynômes”; “obtenir un” -> “obtenir \unsure{une|un}”. No mathematical changes.

### Formulas checked, in transcription order

1.

```latex

$\alpha,\beta$

```

2.

```latex

$\frac12$

```

3.

```latex

$F_p(\alpha)=0,F_{\unsure{q|s}}(\beta)=0$

```

4.

```latex

$p,q\ge1$

```

5.

```latex

$1,2$

```

6.

```latex

$2,-2$

```

7.

```latex

$\alpha,\beta\ldots$

```

8.

```latex

$k=\mathbb{R}$

```

9.

```latex

$C_{p,q}$

```

10.

```latex

$p$

```

11.

```latex

$q$

```

12.

```latex

$\ge3$

```

13.

```latex

$\alpha$

```

14.

```latex

$\beta$

```

15.

```latex

$\unsure{\zeta|\eta}+\zeta^{-1}$

```

16.

```latex

$\zeta=\exp 2i\pi/n$

```

17.

```latex

$n=p$

```

18.

```latex

$q$

```

19.

```latex

$\alpha=-2\inserted{\text{ ou }\beta=-2}$

```

20.

```latex

$p=\infty$

```

21.

```latex

$\alpha=2$

```

22.

```latex

$q=\infty$

```

23.

```latex

$\beta=2$

```

24.

```latex

\[
\beta=2\qquad\alpha\ne-2
\]

```

25.

```latex

\[
\gamma=2(3+\alpha)+2\alpha=2(2\alpha+3)
\qquad\gamma+2=2(2\alpha+4)=4(\alpha+2)
\]

```

26.

```latex

\[
\begin{aligned}
\delta'&=4-4(\gamma+2)-\gamma^2=-(\gamma^2+4\gamma+4)=-(\gamma+2)^2\\
&=-16(\alpha+2)^2
\end{aligned}
\]

```

27.

```latex

$\alpha=-2$

```

28.

```latex

\[
\begin{aligned}
f_0(x,y,z)&=x^2+y^2+z^2-2(2\alpha+3)yz-2zx-2xy\\
&=\deleted{\unsure{xy|uxy}}(-x+y+z)^2-2(2\alpha+4)yz
\end{aligned}
\]

```

29.

```latex

\[
f_0(x,y,z)=(-x+y+z)^2-4(\alpha+2)yz
\]

```

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{homéomorphisme} -> \unsure{homéomorphisme|homéomorphie}; \unsure{xy} -> \unsure{xy|uxy}

### Supplementary source check

2026-11-17T21:41:35+00:00

All three thirds reread: the initial paragraph is cancelled as a whole, including later insertions; the imaginary i in exp 2i pi/n is not an index. Rechecked p/q, zeta/eta, R, all alpha/beta/gamma signs and the two completed-square displays.

Only the expanded lexical alternatives logged above; no formula was completed or mathematically repaired.

## Scan 074

Start: 2026-11-17T21:22:51+00:00; end: 2026-11-17T21:23:13+00:00.

Crop observations recorded: 2026-11-17T21:23:04+00:00.

### Crop reading before opening the page file

Cover crops: “Calculs en coordonnées universelles”, “(icosaèdre)”, “vieille rédaction”. Accents on coordonnées, icosaèdre and rédaction inspected. Faint parenthesized number at left appears (32), with (22) possible. Small isolated C-like stroke above Calculs. Middle and bottom thirds otherwise blank apart from archive number 73; no date or count of pages visible.

### Checks and changes

All three crops inspected, including blank regions. No formulas, i/j, deletions, insertions, diagrams or typescript corrections. The isolated C-like stroke is separate from title text and remains doubtful. The faint (32)|(22) is retained as manuscript numbering; archive 73 stays in a comment. The sheet is a cover in the inventory. Title accents and lowercase vieille rédaction verified.

No change.

### Formulas checked, in transcription order

## Scan 075

Start: 2026-11-17T21:23:13+00:00; end: 2026-11-17T21:24:33+00:00.

Crop observations recorded: 2026-11-17T21:23:42+00:00.

### Crop reading before opening the page file

Crop-only: almost all content is mathematical. Prose labels “en car. 2”, “(car. ≠2)”, “hom”, “centre”, “Antipodisme”. First σ0 mapping is overwritten and a small S0→S1 is above it. Three σ matrices and coordinate formulas; α′ versus α in the σ1 basis-vector image. In H equations, subscripts 0,1,2; in Δ and D formulas, primes and numerical subscripts only, no i/j. O_S has a separate underline-like stroke. D2 z coefficient/homogeneous coefficient look signed 3, with heavy ink. Centre’s continuation is struck. Bottom numerical line includes half, -1+√5, and a separate radical expression; no missing numbers may be supplied. Both drawings include many S3 primes/double primes, barred S labels and aS labels; their labels require dedicated zoom.

### Checks and changes

First drawing checked edge-by-edge against enlarged source: solid central triangles, six outer vertices, dashed outer edges and faint longer diagonals, S0–S3, S3′/S3″, six aS labels and σ1,σ0,σ2 interior labels. Second drawing checked outer barred S1,S0,S2 triangle, inner barred S3 and barred primed vertices, central S0,S1,S2,S3, all visible connectors and faint secondary triangle. Bar/prime uncertainties remain marked. All σ0,σ1,σ2 vertex and basis mappings, all 48 matrix entries, all three boxed triples, H0/H1/H2, Δ0/Δ1/Δ2, D0/D1/D2, homogeneous directions, centre and antipodism compared symbol by symbol. No i/j indices; all indices are numeric or S. α primes checked independently, including α (unprimed) in D2. Both signed-3 coefficients remain doubtful. The tiny O symbols have a separate lower stroke and now use underline O first consistently with scan81. Extra bottom crop inspected: the last numerical line may contain a literal author question mark; it remains unresolved. Local overwrites, centre continuation and stray deleted equality retained; no handwritten-on-typescript content.

Changes: first O_S candidate mathcal O -> underline O, subsequent occurrences updated consistently; bottom closing punctuation and negative numeral -> explicit )|? and ?|2|1 alternatives. The coordinate formulas and drawing topology otherwise remain unchanged.

### Formulas checked, in transcription order

1.

```latex

$S_0$

```

2.

```latex

$S_1$

```

3.

```latex

$S_2$

```

4.

```latex

$S_3$

```

5.

```latex

$S'_3$

```

6.

```latex

$S''_3$

```

7.

```latex

$aS_1$

```

8.

```latex

$aS_0$

```

9.

```latex

$\underline aS_2$

```

10.

```latex

$\underline aS_3$

```

11.

```latex

$\underline aS'_3$

```

12.

```latex

$aS''_3$

```

13.

```latex

$\sigma_1$

```

14.

```latex

$\sigma_0$

```

15.

```latex

$\sigma_2$

```

16.

```latex

\[
\sigma_0:\quad\begin{aligned}
\inserted{S_0\longrightarrow S_1}\\
\unsure{S_1|S_0}\longleftrightarrow S_0\\
S_2\longmapsto S_2\\S_3\longmapsto S_3
\end{aligned}
\qquad\begin{aligned}
e_1&\longmapsto-e_1\\e_2&\longmapsto-e_1+e_2\\e_3&\longmapsto-e_1+e_3
\end{aligned}
\]

```

17.

```latex

\[
\sigma_0=\begin{pmatrix}-1&-1&-1&1\\0&+1&0&0\\0&0&+1&0\\0&0&0&1\end{pmatrix}
\]

```

18.

```latex

\[
\boxed{\sigma_0(x,y,z)=\deleted{\unsure{\mathrm{id}}}(1-(x+y+z),y,z)}
\]

```

19.

```latex

$\overline S_1$

```

20.

```latex

$\overline S_0$

```

21.

```latex

$\overline S_2$

```

22.

```latex

$\overline S_3$

```

23.

```latex

$S'_3$

```

24.

```latex

$S''_3$

```

25.

```latex

$\unsure{\overline{S''_3}|S''_3}$

```

26.

```latex

$\unsure{\overline{S'_3}|\overline S_3}$

```

27.

```latex

$S_0$

```

28.

```latex

$S_1$

```

29.

```latex

$\unsure{S_2}$

```

30.

```latex

$S_3$

```

31.

```latex

\[
\sigma_1:\quad\begin{aligned}
S_0&\longmapsto S_0\\S_1&\longmapsto S_2\\S_2&\longmapsto S_1\\S_3&\longmapsto S'_3=S_0+(1+\alpha)(e_2-e_1)+e_3
\end{aligned}
\qquad\begin{aligned}
e_1&\longmapsto e_2\\e_2&\longmapsto e_1\\e_3&\longmapsto(1+\alpha)(e_2-e_1)\inserted{+e_3}\\
&=\alpha'e_1-\alpha'e_2+e_3
\end{aligned}
\]

```

32.

```latex

\[
\sigma_1=\begin{pmatrix}0&1&\alpha'&0\\1&0&-\alpha'&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
\qquad\boxed{\sigma_1(x,y,z)=(y+\alpha'z,x-\alpha'z,z)}
\]

```

33.

```latex

\[
\sigma_2:\quad\begin{aligned}
S_0&\longmapsto S_0\\S_1&\longmapsto S_1\\S_2&\longmapsto S_3\\S_3&\longmapsto S_2
\end{aligned}
\qquad\begin{aligned}
e_1&\longmapsto e_1\\e_2&\longmapsto e_3\\e_3&\longmapsto e_2
\end{aligned}
\]

```

34.

```latex

\[
\sigma_2=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix}
\quad\deleted{\unsure{=}}\boxed{\sigma_2(x,y,z)=(x,z,y)}
\]

```

35.

```latex

\[
\left\{\begin{aligned}
H_0:&\quad2x+y+z-1=0\\H_1:&\quad x-y-\alpha'z=0\\H_2:&\quad y-z=0
\end{aligned}\right.
\qquad\left\{\begin{aligned}
\Delta_0:&\quad y=z=0&&\text{i.e. }\Delta_0=\unsure{\underline O_S|\mathcal O_S}\cdot e_1\\
\Delta_1:&\quad z=0,x+y=0&&\text{i.e. }\Delta_{\unsure{1|p}}=\underline O_S(e_1-e_2)\\
\Delta_2:&\quad x=0,y+z=0&&\text{i.e. }\Delta_2=\underline O_S(e_2-e_3)
\end{aligned}\right.
\]

```

36.

```latex

$2$

```

37.

```latex

$H_2\parallel H_0$

```

38.

```latex

\[
\left\{\begin{aligned}
D_0=H_1\cap H_2:&\quad y=z=\alpha'x\\
D_1=H_2\cap H_0:&\quad y=z=\underbrace{\tfrac12-x}_{\text{(car}\ne2\text{)}}\\
D_2=H_0\cap H_1:&\quad y=\deleted{\unsure{\alpha}}(1-3\alpha)x+\alpha,\quad z=\unsure{-3|3}(1-\alpha)x+(1-\alpha)
\end{aligned}\right.
\]

```

39.

```latex

\[
\begin{aligned}
D_0&=\underline O_S(1,\alpha',\alpha')=\underline O_S(-\alpha,1,1)\\
\underline{\mathrm{hom}\,D_1}:\ (y=z=-x)&=\underline O_S(1,-1,-1)\\
\underline{\mathrm{hom}}(D_2)&=\underline O_S(1,1-3\alpha,\unsure{-3|3}(1-\alpha))
\end{aligned}
\]

```

40.

```latex

$o=\frac12(\alpha',1-\alpha',1-\alpha')=\deleted{\unsure{\frac12\alpha'}}$

```

41.

```latex

\[
\underline a(x,y,z)=(\alpha'-x,(1-\alpha')-y\unsure{\},},(1-\alpha')-z\unsure{\}})
\]

```

42.

```latex

\[
\tfrac12(-1+\sqrt5\quad\unsure{)|?}=-\unsure{?|2|1}+\unsure{\sqrt5|\sqrt\gamma}
\]

```

### Supplementary source check

2026-11-17T21:37:30+00:00

Bottom third compared again: H/D/Delta subscripts, underlined O_S, alpha primes, D2 sign ambiguity, centre, antipodism and the numerical scratch line with question-mark-like hooks.

No further change; the last numerical line remains low confidence.

### Supplementary source check

2026-11-17T21:41:35+00:00

Top and middle crops reread for both drawings, all vertex labels and all three matrices. Checked the extra e3 and its insertion under the sigma1 map. The underlined O has the same separated lower stroke as on scan 81.

No further change.

## Scan 076

Start: 2026-11-17T21:24:33+00:00; end: 2026-11-17T21:25:31+00:00.

Crop observations recorded: 2026-11-17T21:24:58+00:00.

### Crop reading before opening the page file

Crop-only: “centre”; “en car.2”; “Si e est un vecteur arête (tel que S1-S0=e1)”; f line uses a repetition stroke and “coarête”; “c’est la normalisation de q !”; “En coordonnées distinguées”; “les 12 sommets de l’icosaèdre”; “dans le cas réel, d’icosaèdre convexe”; “et si on prend x,y>0, on trouve”; “Matrice non singulière sauf en car.2, où le noyau … est engendré”; “NB … ce qui exprime la non-singularité de q0 en car.2”. S3′ last coordinate resembles 2 or a curved 1; do not infer it from antipodes. S3″ and aS3″ y entries visibly -α′ and 1-2α′. The x-like coefficient in q0 looks large X. The last matrix entry is overwritten. Small diagram labels S1,S0,-S0,-S1,x,y. No i/j indices.

### Checks and changes

Checked all twelve coordinate triples, the a(x,y,z) expression, c and u=2c (including terminal homogeneous coordinate 2), every α prime and the cancelled addition in aS3′. In aS3″ the written 1-2α′ is retained. Checked q0 polynomial and complete characteristic-2 bracket, both edge/coedge differences (lowercase s as written there), q(e),q(f) and their ratio. Checked all three distinguished-coordinate families and the two vertex-pair comparisons. Rectangle: four corner labels and x,y positions checked; no added arrowheads. Checked cancelled ratio calculation, live q(f)/q(e),4y²/4x²,(y/x)²,α′²,±α′; both golden-root values and positive x,y; δ′(q0), all nine φ entries, all three versions of u and q0(u)=α′≠0. No i/j indices; all numerical subscripts, q0 and primes checked separately. Plain X|x in q0 and varphi|phi remain uncertain. Last matrix entry retains old 0 under final 2. No margin or typed material.

Changes: S3′ last coordinate 1 -> \unsure{2|1}; missing article before icosaèdre convexe -> \unsure{l’icosaèdre|d’icosaèdre}; nonsingularité -> explicit hyphen/no-hyphen alternatives. Other calculations and drawing unchanged.

### Formulas checked, in transcription order

1.

```latex

\(\begin{array}{ll|l}
S_0=(0,0,0)&\underline aS_0=(\alpha',1-\alpha',1-\alpha')&\underline a(x,y,z)=(\alpha'-x,(1-\alpha')-y,(1-\alpha')-z)\\
S_1=(1,0,0)&\underline aS_1=(\alpha'-1,1-\alpha',1-\alpha')&c=\frac12(\alpha',1-\alpha',1-\alpha')\\
S_2=(0,1,0)&\underline aS_2=(\alpha',\unsure{-\alpha'|-\alpha'_2},1-\alpha')&\text{centre}\\
S_3=(0,0,1)&\underline aS_3=(\alpha',1-\alpha',-\alpha')&u=2c=(\alpha',1-\alpha',1-\alpha',2)\\
S'_3=(\alpha',-\alpha',\unsure{2|1})&\underline aS'_3=(0,1\deleted{\unsure{+\alpha'|-\alpha'}},-\alpha')&\\
S''_3=(0,-\alpha',1)&\underline aS''_3=(\alpha',1-2\alpha',-\alpha')&
\end{array}\)

```

2.

```latex

\[
\begin{aligned}
q_0(x,y,z)&=x^2+y^2+z^2-\alpha yz+\unsure{X|x}(y+z)-(x+y+z)\\
\bigl[&=(\text{en car. }2)\quad\alpha'\bigl[(x-\alpha y)^2+\alpha'(x-\alpha y)(x-\alpha z)+(x-\alpha z)^2\bigr]\\
&\hspace{7em}-(x+y+z)\bigr]
\end{aligned}
\]

```

3.

```latex

$e$

```

4.

```latex

$s_1-s_0=e_1$

```

5.

```latex

\[
f\quad\text{---}\quad\text{coarête}\quad(\text{tel que }s_3-s_2=e_3-e_2)
\]

```

6.

```latex

\[
\left\{\begin{aligned}
q(e)&=1\quad\text{(c'est la normalisation de }q\text{ !)}\\
q(f)&=\alpha+2\\
q(f)/q(e)&=\alpha+2=(\alpha+1)^2=\alpha'^2
\end{aligned}\right.
\]

```

7.

```latex

$(\pm x,\pm y,0),(\deleted{\unsure{+}}\pm y,0,\pm x),(0,\pm x,\pm y)$

```

8.

```latex

$12$

```

9.

```latex

$(x,y,0)$

```

10.

```latex

$(-x,y,\unsure{0})$

```

11.

```latex

$(x,y,0)$

```

12.

```latex

$(x,-y,0)$

```

13.

```latex

$S_1$

```

14.

```latex

$S_0$

```

15.

```latex

$-S_0$

```

16.

```latex

$-S_1$

```

17.

```latex

$y$

```

18.

```latex

$x$

```

19.

```latex

\[
\deleted{\unsure{\frac{4y^2}{4x^2}=\lambda\left(\frac yx\right)^2}}\deleted{\unsure{\alpha}}\frac{q(f)}{q(e)}=\frac{4y^2}{4x^2}=\left(\frac yx\right)^2=\alpha'^2\quad\text{donc}\quad\frac yx=\pm\alpha'
\]

```

20.

```latex

$\alpha=\frac12(-1+\sqrt5)$

```

21.

```latex

$\alpha'=\frac12(-1-\sqrt5)$

```

22.

```latex

$x,y>0$

```

23.

```latex

$y/x=-\alpha'=\frac12(1+\sqrt5)$

```

24.

```latex

\[
\delta'(q_0)=1\qquad\text{Matrice }\unsure{\varphi|\phi}_{q_0}=\begin{pmatrix}2&1&1\\1&2&-\alpha\\1&-\alpha&\deleted{\unsure{0}}2\end{pmatrix}
\]

```

25.

```latex

$2$

```

26.

```latex

$\varphi_{q_0}$

```

27.

```latex

$u=(\alpha',1-\alpha',1-\alpha')=(\alpha',\alpha,\alpha)=(1+\alpha,\alpha,\alpha)$

```

28.

```latex

$q_0(u)=\alpha'\ne0$

```

29.

```latex

$q_0$

```

30.

```latex

$2$

```

### Supplementary source check

2026-11-17T21:37:30+00:00

Coordinate table reread against the adjacent antipodism map. S3′ final entry still looks more like 2 than 1; retained both. The live S3″ second coordinate -alpha′ and aS3″ coordinate 1-2alpha′ are visibly different and have not been harmonized. Read all q0 coefficients and the first characteristic-two expression again.

No further change; the apparent coordinate inconsistency is retained for the notes.

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{+\alpha'} -> \unsure{+\alpha'|-\alpha'}

## Scan 077

Start: 2026-11-17T21:25:31+00:00; end: 2026-11-17T21:27:07+00:00.

Crop observations recorded: 2026-11-17T21:26:05+00:00.

### Crop reading before opening the page file

Crop-only before page file: title “vecteurs remarquables” with added “de directions remarquables”, “cas car.≠2”; “On suppose 2 inversible”; “son centre o identifiant E et l’espace des translations V”; “Utilisant la forme quadratique”; “directions de droites”, “directions de plans”. Lists “12 vecteurs … sommets”, “30 vecteurs arêtes”, “15 paires de vecteurs opp.”; coarêtes; “les milieux d’arêtes”; barycentres des faces and cofaces; “triples (ou hexuples…)”; “homothétiquement”, “Dodécaèdres”, “contreicosaèdre associé”; “multipliés par 10”; “intersection des plans des faces adjacentes à une face”; “it.”; “quintuples” and “pentagones inscrits aux sommets”. Marginal S,Δ,Δ′,script A/A′,Φ/Φ′,Ψ/Ψ′,Σ. Index pairs i,j are written with separate dots/descenders; the third index in the face triple looks h, not j. λ=2α-1 has a minus-like final stroke. The sum before 3c and membership prime in Δ′ need direct comparison. Several crossed coefficients occur at the starts of barycentre formulas.

### Checks and changes

Checked all 12/30/15/20 counts, the centred vertex difference, both edge differences and every {i,j} membership. i has no descender; j has a long descender. In face memberships and barycentre formula the third index is h (tall stem), not a second j; all i,j,h appearances compared independently. Checked Δ′=α′Δ and Δ=αΔ′, midpoint factors and all A/A′ relations, both repeated Δ′ memberships, all Φ/λ formulas and Norm(λ), all Ψ/ν/μ relations and Norm(μ), μ²=5 and μ′=-μ, all five S subscripts in the pentagon sum, Σ/ρ relations and Trρ=0. The face formula’s three signs were enlarged; each unresolved operator is now marked, with minus/plus first as seen rather than from the barycentre interpretation. Script A differs from plain membership A; Φ,Ψ,Σ and Π/Π′ remain distinct. V check and P double strokes checked. All marginal set labels and NB text reread; tiny right marginal reference remains doubtful. Repetition lines are kept as dashes, not expanded words. Crossed doubles, coefficient halves/thirds, les vecteurs, λ norm sign and cancelled μ/ρ formulas all retained. Small four-arrow square has arrows right/up, no labels.

Changes: unmarked conventional signs in (Si+Sj+Sh-3c -> explicit +|-, -|+, +|- alternatives; marginal 2 triples -> 26 bis|2 triples|2 trpls; idem -> it.|idem. No algebraic normalization.

### Formulas checked, in transcription order

1.

```latex

$\ne2$

```

2.

```latex

$2$

```

3.

```latex

$o$

```

4.

```latex

$E$

```

5.

```latex

$V$

```

6.

```latex

$V$

```

7.

```latex

$\check V$

```

8.

```latex

$\check{\mathbb P}(V)$

```

9.

```latex

$E$

```

10.

```latex

$\mathbb P(V)$

```

11.

```latex

$E$

```

12.

```latex

$S$

```

13.

```latex

$12$

```

14.

```latex

$\boxed{S_i-\underline aS_i}$

```

15.

```latex

$\Delta$

```

16.

```latex

$30$

```

17.

```latex

$S_i-S_j$

```

18.

```latex

$(\{i,j\}\in A)$

```

19.

```latex

$15$

```

20.

```latex

$\Delta'$

```

21.

```latex

$30$

```

22.

```latex

$S_i-S_j$

```

23.

```latex

$(\{i,j\}\in A')$

```

24.

```latex

$\unsure{\pm}\alpha'u$

```

25.

```latex

$(u\in\Delta')$

```

26.

```latex

$\unsure{\Delta}$

```

27.

```latex

\[
\boxed{\Delta'=\alpha'\Delta,\quad\Delta=\alpha\Delta'}
\]

```

28.

```latex

\begin{tikzcd}[ampersand replacement=\&]
{}\arrow[r]\&{}\\
{}\arrow[u]\arrow[r]\&{}\arrow[u]
\end{tikzcd}

```

29.

```latex

$\left[\begin{matrix}\mathcal A\\\mathcal A'\end{matrix}\right.$

```

30.

```latex

$30$

```

31.

```latex

$\deleted{\tfrac12}(S_i+S_j-2c)$

```

32.

```latex

$(\{i,j\}\in A)$

```

33.

```latex

$30$

```

34.

```latex

$\frac12(S_i+S_j)$

```

35.

```latex

$(\{i,j\}\in A')$

```

36.

```latex

\[
\begin{aligned}
\Delta&=\deleted{\unsure{\xi}}2\mathcal A'&\left\{\begin{aligned}\mathcal A&=\alpha'\mathcal A'\\\mathcal A'&=\alpha\mathcal A\end{aligned}\right.\\
\Delta'&=\deleted{\unsure{\xi}}\unsure{2}\mathcal A
\end{aligned}
\]

```

37.

```latex

$\Delta$

```

38.

```latex

$S_i+S_j$

```

39.

```latex

$(\{i,j\}\in A')$

```

40.

```latex

\[
\Delta'\quad\text{---}\qquad(\{i,j\}\in A)
\]

```

41.

```latex

$\Phi$

```

42.

```latex

$20$

```

43.

```latex

$\deleted{\tfrac13}(S_i\unsure{+|-}S_j\unsure{-|+}S_h\unsure{+|-}3c$

```

44.

```latex

$(\{i,j,h\}\in F)$

```

45.

```latex

$\Phi'$

```

46.

```latex

$20$

```

47.

```latex

$(\{i,j,h\}\in F')$

```

48.

```latex

$\unsure{26\text{ bis}|2\text{ triples}|2\text{ trpls}}$

```

49.

```latex

\[
\Phi'=\lambda\Phi,\quad\Phi=\lambda'\Phi'\qquad(\lambda\lambda'=\mathrm{Norm}(\lambda)=\deleted{\unsure{-}}1)\qquad\lambda=2\alpha-1
\]

```

50.

```latex

$\Phi$

```

51.

```latex

$\Phi'$

```

52.

```latex

$\Pi$

```

53.

```latex

$\Pi'$

```

54.

```latex

$\Psi$

```

55.

```latex

$20$

```

56.

```latex

$10$

```

57.

```latex

$\Pi$

```

58.

```latex

$\Psi'$

```

59.

```latex

$\Pi'$

```

60.

```latex

\[
\Psi'=\unsure{\nu|\mu}\Psi,\quad\Psi=\nu'\Psi'\qquad\deleted{\mu\mu'=\mathrm{Norm}(\mu)=1}\quad\nu=-\lambda
\]

```

61.

```latex

\[
\boxed{\Psi=\mu\Phi,\quad\Psi'=\mu'\Phi'}
\qquad\begin{aligned}
\mu&=1+2\alpha=-(1+2\alpha')\\
(\mu\mu'&=-5),\quad\mu^2=5\text{ i.e. }\mu=\sqrt5
\end{aligned}
\]

```

62.

```latex

$\mu'=-\mu$

```

63.

```latex

$\Sigma$

```

64.

```latex

$12$

```

65.

```latex

\[
2(S_1+S_2+S_3+S_4+S_0)-2c
\]

```

66.

```latex

\[
\begin{aligned}
\Sigma&=\rho S=\rho'S\qquad\rho'=-\rho\quad\text{i.e. }\deleted{\rho=\rho+\rho'c}\inserted{\mathrm{Tr}\rho=0}\\
\rho&=\mu=1+2\alpha\ldots
\end{aligned}
\]

```

### Supplementary source check

2026-11-17T21:37:30+00:00

All three thirds reread for every i/j/h, primes on A/F/Phi/Psi and Greek scale factors. i has no descender, j does; h in the face triple is retained. The marginal possible 26 bis, the overwritten norm sign, incomplete barycentre parenthesis and all cross-outs were checked again.

No further change; no completion or sign correction inferred from the geometry.

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{ou hexuples} -> \unsure{ou hexuples|ou hexagones}; \unsure{quintuples} -> \unsure{quintuples|quadruples}

## Scan 078

Start: 2026-11-17T21:27:07+00:00; end: 2026-11-17T21:27:42+00:00.

Crop observations recorded: 2026-11-17T21:27:33+00:00.

### Crop reading before opening the page file

Upright crops read before file: émet, à l’orientation, difficulté, présidence, Président, Université, ès qualité, élus, personnalités extérieures, U.S.T.L., nommées, élues, Académie, associées, C.N.R.S., docteurs d’Etat (unaccented E), comité, collège électoral, président (lowercase in the bullet), Ecole (unaccented E), supérieure, ingénieurs, établie, Président (uppercase), élection, conformément, présents, Collège, composé, exerçant, professeurs (plural), directeur (singular), maître, conférences, maître-assistant, chargé, équivalent, inscrits, éligibles. Punctuation: first two bullets end periods; Académie and docteurs d’Etat bullets end commas; next two end periods. n,2n,10%,articles9,11,12 and typed page -2-. Plain capitals in heading, no double striking or handwritten corrections.

### Checks and changes

Line-by-line comparison of all three upright crops completed. Accents and case from the pre-file list retained, including Etat/Ecole without accent and capital Président only where typed. Membership counts n,2n,10%,article references9,11,12 checked; no mathematical display or i/j index. All four category bullets and the full electoral-college list checked, including professeurs/directeur number and maître-assistant hyphen. Underlines are live emphasis, not deletions. Heading capitals independently inspected: plain type, no bold or double striking. No handwritten corrections, margin text or cancellations; only excluded archive numbering. Hyphenated line endings joined, including nationales and maître.

No change.

### Formulas checked, in transcription order

1.

```latex

$\cdot$

```

## Scan 079

Start: 2026-11-17T21:27:42+00:00; end: 2026-11-17T21:30:49+00:00.

Crop observations recorded: 2026-11-17T21:30:19+00:00.

### Crop reading before opening the page file

Crop reading: Directions remarquables; directions de sommet(s), final plural stroke uncertain; arêtes has a circumflex, faces; nb de pts du plan projectif sur F with a doubled vertical stroke and subscript 5. conique; sécantes; découpant un diviseur; décomposé inserted above a cancelled arrow; connexes /F5. vecteurs remarquables en car. 5. 1+12+60+40=11 with an overwritten last digit; 125=1+24+60+40, the first 1 annotated by an infinity sign. pts sur la conique = 2×12 (deux ico.). The short block under the first sum is heavily cancelled: les/des, quinze overwritten by 25, droites/doubles non isotropes, associated arêtes/faces wording, 20 aux faces — elles sont, donc below. In the drawing: S0′ upper left, S1′ upper right, S1 lower left, S0 lower right, c; x²+y² crossed out at right. The bottom crop also has an isolated angular pen stroke above the archive number, to retain as a drawing.

### Checks and changes

Read all three crops including the largely blank lower third, enlarged cancellation area, all direction counts, both finite-field sums, primes/subscripts on all four vertices and c, every arrow and short stroke. No i or j occurs as an index. Double-stroked F is mathbb; all S are ordinary capitals. Deletion/insertion connections in the prose and cancelled block remain explicitly uncertain where ink is covered. No handwritten additions to type; this is manuscript throughout.

sommets -> unsure{sommet|sommets} twice; underline around the whole heading -> underline only car. 5; unsure{deleted{distincts}} -> deleted{unsure{dist.|distincts}}; omitted angular stroke -> TikZ drawing. The uncertain cancellation sequence has not been silently resolved. Subsequent comparison with scan 80: the peripheral angular mark repeats outside the text in the archive orientation; its TikZ rendering was replaced by an archive/scan comment, with attribution uncertainty documented.

### Formulas checked, in transcription order

1.

```latex

\[
\begin{aligned}
\unsure{6}&\quad\text{directions de \unsure{sommet|sommets}}\\
15&\quad\text{--- d'arêtes}\\
\underline{10}&\quad\text{directions de faces}\\
31&=5^2+5+1\quad\text{nb de pts du plan projectif sur }\mathbb F_5
\end{aligned}
\]

```

2.

```latex

$\unsure{\to}$

```

3.

```latex

$/\mathbb F_5$

```

4.

```latex

$/\mathbb F_5$

```

5.

```latex

\[
1+12+60+40=11\deleted{\unsure{2}}3
\qquad
125=\underset{\infty}{1}+\underbrace{24}_{\substack{\text{pts sur}\\\text{la conique}\\=2\times12\\\text{(deux ico.)}}}+60+40
\]

```

6.

```latex

$S_1$

```

7.

```latex

$S_0$

```

8.

```latex

$S'_0$

```

9.

```latex

$S'_1$

```

10.

```latex

$c$

```

11.

```latex

$\deleted{x^2+y^2}$

```

## Scan 080

Start: 2026-11-17T21:30:49+00:00; end: 2026-11-17T21:31:29+00:00.

Crop observations recorded: 2026-11-17T21:31:13+00:00.

### Crop reading before opening the page file

Read the three thirds rotated to upright, starting with original s3. UNIVERSITE has no accent in the title; TECHNIQUES, LANGUEDOC. Article 20; Nouvelle rédaction approuvée; Université; le 29 juin 1977. CONSEIL SCIENTIFIQUE is boxed, with ordinary type capitals. I.- MISSION. Conformément, dispositions, article 13, orientation, enseignement supérieur, détermine, répartit, crédits. équipes, s'insérant, internationaux, nationaux et régionaux. établit; politique; potentiel; définie; organismes; affectés; façon. attribuée, encadrement, utilisée; équipements d'intérêt collectif; reconnaîtra; opérations susceptibles d'être soutenues et relayées; C.N.R.S., D.G.R.S.T., etc. The hyphens in orientation, nationaux, politique are line-break hyphens. Four outer dash items, two dot subitems, four inner dash items. No handwritten correction or mathematical formula. The margin has the same angular registration-like mark as scan 79; it is outside the document text.

### Checks and changes

Compared every typed line with the upright crops, including capitals, accents, punctuation, four/two/four list structure and the final organizational abbreviations. Checked no manuscript correction is present in the body or heading. No doubled or script capital, i/j index, formula, deletion or marginal note belongs to the typescript. The centered short dash and title box are retained. The repeated peripheral mark is treated as an archive/scan mark, not an authorial drawing.

No transcription reading changed; added an archive/scan mark comment.

### Formulas checked, in transcription order

1.

```latex

$\cdot$

```

## Scan 081

Start: 2026-11-17T21:31:29+00:00; end: 2026-11-17T21:33:21+00:00.

Crop observations recorded: 2026-11-17T21:32:06+00:00.

### Crop reading before opening the page file

Crops read independently: ou, OK, e1 followed by a reduced word (non. possible), Il suffit de donner. y=z; x=(1+alpha′)y=-alpha y; y=alpha′x. Coordinates (-alpha y,y,y), (x,alpha′x,alpha′x), (-alpha,1,1), (1,alpha′,alpha′). The question mark is above the equality for alpha′, not a prime. Barred S0, S1; the next S subscript looks like 1/2. The marginal rejection ends -1=0 and a small infinity-like mark. The orbit symbol has a separate underline under an O; not confidently calligraphic. The group symbol has heavy squared strokes resembling Gamma but script G/T cannot be excluded; SO has an upward-pointing superscript, plus also possible. The central cocycle equation uses two different g occurrences and a prime on the second g. f(sigma1)=f(sigma2)=0; the next initial letter resembles C/f. q0(e)=1 boxed. The lower calculations use u, u², u³; e1 wedge e2 wedge e3; sigma0 and sigma2, not i/j indices. A boxed sigma0 sigma2 e relation is struck; the bottom fifth-degree sum and an adjacent sum are also struck. The small two-dot intersecting-line drawing and the S0--S1 with isolated S2 drawing both have to be retained. All alpha primes, S bars, 0/1/2/3 subscripts, and equality/implication directions have been reread.

### Checks and changes

Full crop comparison, then separate enlarged readings of the group/curl and Gamma-to-E arrow. Checked all alpha primes and squares; barred S indices and numeric indices of sigma/e; no i or j index occurs. Checked all f arguments and g primes in the cocycle equation; the incomplete f(u³)=e+ue+ stays incomplete. Both margin calculations and their cancellations were read in their written horizontal direction. The lines enclosing formulas are boxes or grouping marks unless a separate strike crosses the symbols; cancelled boxes and overwritten q/sigma2/alpha remain marked. E has three ordinary strokes, not a double-struck capital. Gamma remains a notation-table ambiguity, and O has a visible underline. No typed text or handwritten correction to type. Drawing directions, isolated dots, the unconnected S2 and all lower boxes were checked.

SO^{unsure{+|uparrow}} -> SO^{unsure{uparrow|+}}; generic self-loop over SO -> two-stroke TikZ curl without an invented arrowhead; Gamma longrightarrow E -> Gamma overset{unsure{f}}{longrightarrow} E. No mathematical correction made.

### Formulas checked, in transcription order

1.

```latex

\[
y=z\qquad x=(1+\alpha')y=-\alpha y\qquad y=\alpha'x
\]

```

2.

```latex

\[
\begin{aligned}
\underline{(-\alpha y,y,y)}&\quad\text{ou}\quad(x,\alpha'x,\alpha'x)\\
(-\alpha,1,1)&\qquad(1,\alpha',\alpha')\\
-\alpha&=\alpha'(1-\alpha')=\alpha'-\alpha'^2\\
\alpha'&\overset{?}{=}-\alpha(1-\alpha')=-\alpha-1\quad\text{OK}
\end{aligned}
\]

```

3.

```latex

$\begin{aligned}1-(2-\alpha)\\\alpha-1\\\alpha=\tfrac12\\\tfrac14+\tfrac12-1=0\\1+2-4=0\\-1=0\\\unsure{\infty}\end{aligned}$

```

4.

```latex

\[
e_1\ \unsure{\text{non.}}\qquad
\left\{\begin{aligned}
\bar S_0&=(-\alpha,1,1)\\
\bar S_1&=\sigma_0\bar S_0=(\alpha-1,1,1)\\
\deleted{\unsure{e}}\quad\bar S_{\unsure{1|2}}-\bar S_0&=(\underline{2\alpha-1},0,0)
\end{aligned}\right.
\]

```

5.

```latex

\[
\unsure{\alpha'^2|\alpha^2}=1-\alpha'\qquad \alpha+\alpha'=-1
\]

```

6.

```latex

$\begin{aligned}\deleted{2\alpha}\ 2\\2\alpha-1=2\alpha+2-3\\\deleted{\unsure{\alpha-2}}
\end{aligned}$

```

7.

```latex

\[
\unsure{\underline{O}_S|\mathcal O_S}\quad(-\alpha,1,1)
\]

```

8.

```latex

\[
\begin{aligned}y+z+1&=0\\x+y+\alpha z&=0\\y&\underline{=z}\end{aligned}
\qquad f(0)=f(\sigma_1\sigma_2)=0
\]

```

9.

```latex

\[
\begin{aligned}f(\sigma_0^2)&=f(\sigma_0)+\sigma_0f(\sigma_0)=0\\
e+\sigma_0e&=0\\\boxed{\sigma_0e=-e}
\end{aligned}
\]

```

10.

```latex

\begin{tikzcd}[ampersand replacement=\&]
\&\begin{tikzpicture}[scale=.4]
\draw (1.4,0) .. controls (-.8,-.3) and (-.9,1.8) .. (.3,2.1) .. controls (.7,2.1) and (1,1.4) .. (1.7,1.6);
\draw (.3,2.1)--(-.2,1.1) .. controls (.6,1.4) and (.7,1) .. (.45,.8);
\end{tikzpicture}\\
\unsure{\Gamma|\mathscr G}\arrow[r]\&SO^{\unsure{\uparrow|+}}(q)
\end{tikzcd}

```

11.

```latex

$+\ 1$

```

12.

```latex

\[
\left\{\begin{aligned}
\Gamma&\overset{\unsure{f}}{\longrightarrow} E\\
f(gg')&=f(g)+gf(g')
\end{aligned}\right.
\]

```

13.

```latex

\[
f(\sigma_1)=f(\sigma_2)=0\qquad \unsure{C|f}(\sigma_0)=e\deleted{\unsure{q}}
\qquad\boxed{q_0(e)=1}
\]

```

14.

```latex

\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\&S_2\&\\S_0\arrow[rr,no head]\&\&S_1
\end{tikzcd}

```

15.

```latex

\[
\begin{aligned}S_2-S_0\\=\\e_2-e_3\\(0,1,-1)\end{aligned}
\]

```

16.

```latex

\[
\sigma_0\sigma_2\sigma_0\sigma_2
\]

```

17.

```latex

\[
\begin{aligned}f(\sigma_0\sigma_2)&=\deleted{\unsure{e+}}e\\
f&\qquad e+\sigma_0\sigma_2e=0\\
\deleted{\boxed{\sigma_0\sigma_2e=\deleted{\unsure{\sigma_2}}-e}}\\
&=\sigma_0e\\
\sigma_0(\sigma_2e-e)&=0
\end{aligned}
\]

```

18.

```latex

\[
\sigma_0\sigma_1=u\qquad
\begin{aligned}
f(u)&=e\\f(u^2)&=e+ue\\f(u^3)&=e+ue+
\end{aligned}
\]

```

19.

```latex

\[
\left\{\begin{aligned}\underline{e_1\wedge e_2\wedge e_3}\\q\end{aligned}\right.
\qquad
\begin{aligned}
f(u^3)&=f(uu^2)=\\&e+u(e+ue)\\&=e+ue+u^2e=0
\end{aligned}
\]

```

20.

```latex

\[
1+1+\alpha=2+\alpha=\deleted{\unsure{\alpha}}1-\alpha'=\boxed{\alpha'^2}
\]

```

21.

```latex

\[
\boxed{\left\{\begin{aligned}\sigma_0e&=-e\\\sigma_2e&=e\end{aligned}\right.}
\quad\begin{aligned}\Longleftrightarrow(1+\sigma_0)e&=0\\\Longleftrightarrow(1+\sigma_0\sigma_2)e&=0\end{aligned}
\qquad\boxed{(1+u+u^2)e=0}
\]

```

22.

```latex

\[
\deleted{\unsure{(1+u+u^2)e}}\qquad
\deleted{(1+u+u^2+u^3+u^4)e=0}\quad\unsure{\zeta|\}}
\]

```

### Supplementary source check

2026-11-17T21:41:35+00:00

Final comparison of visible alternatives with the doubt register; alternatives supported by the inspected strokes are made explicit in place. No first candidate is replaced by an expected mathematical expression.

\unsure{\zeta} -> \unsure{\zeta|\}}

## Scan 082

Start: 2026-11-17T21:33:21+00:00; end: 2026-11-17T21:34:08+00:00.

Crop observations recorded: 2026-11-17T21:33:44+00:00.

### Crop reading before opening the page file

Letterhead: THE UNIVERSITY OF ROCHESTER; Department of Mathematics and Mathematical Sciences Building in small capitals; ROCHESTER, NEW YORK 14627. Charles E. Watts, Chairman (Chairman italic); Phone 716-275-4413. September 21, 1977. Professor A. Grothendieck; Institut des Hautes Études Scientifiques (capital É bears an acute); 91440 Bures-sur-Yvette; France. Dear Professor Grothendieck: (colon). Saul Lubkin; 1974, 1976, January 31, 1978; one-year, two-year, (tenure-track), five years; scientific and professional accomplishment (singular), potential. reprints and preprints; post card (two words); assistance, difficult but essential professional task; apologize, shortness. Sincerely,; handwritten Charles E. Watts and the same name typed beneath; CEW:rec; Enclosure. No manuscript correction to the typed body. No mathematical expressions, indices or script/double-struck capitals. Signature is in a different hand from the manuscript notes.

### Checks and changes

Compared every line of the printed heading, date, address, salutation, both body paragraphs, closing, signature, typed name, initials and enclosure. Checked the capital acute in Études, hyphens in the address and appointment terms, singular accomplishment and separate post card. The handwritten signature is legible and wrapped only in handwritten; inventory element 9 is other hand. No correction, cancellation, margin note, formula, i/j index or double-struck/script mathematical capital occurs. Archive number appears only as a comment.

No change.

### Formulas checked, in transcription order

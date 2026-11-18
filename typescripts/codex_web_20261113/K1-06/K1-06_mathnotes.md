# K1-06 · Mathematical notes

## What the pages do

**U01 · A power series on ℓ¹ (122).** The sheet finishes an estimate for the nth root of $n!\alpha_n$. It writes down the symmetric multilinear form associated with $\alpha_n$ and bounds its norm by $1/n!$. On a vector with its first $m$ coordinates equal to $1/m$, the coefficient $n!\alpha_n$ tends to 1 for fixed $n$. The values of $S$ on these unit vectors grow without bound. The last live line identifies the two radii at the origin, $R_0=R_1=1$.

**U02 · Exterior products and mixed coefficients (124).** The canonical decomposition of each $u_i$ provides two families of factors, written $a$ and $b$. The author expands the exterior product, bounds its trace norm, and compares the sums of squared wedge norms with the unprimed and primed absolute operators. The last step invokes « Cauchy-Schwartz ». Corollary 1 gives an arithmetic-mean bound. Corollary 2 expands $\alpha_n(A+B)$ with $k$ arguments of one kind and $n-k$ of the other.

**U03 · Determinant bounds for a sum (125–126).** Corollary 3 combines the two determinant terms associated with the absolute operators. Corollary 4 bounds $|\det(1+A+B)|$ by $\det(1+|A|)\det(1+|B|)$. The proof reduces to positive hermitian operators and introduces $H=1/(1+h)$. In the lower portion of 125, functoriality of the exterior power and the bound on the norm of $H$ control the coefficients. The boxed Corollary 5 has $\det(1+|A+B|)$ on its left.

**U04 · The unitary argument (126).** After the upper text repeated from 125, a different strip of writing compares the two determinant corollaries. The author writes $|A+B|=U(A+B)$ with $U$ unitary, qualified by « en général » in quotation marks. The final two lines use invariance under unitary conjugation for the determinant factors. The precise convention for $|A|$ matters to this argument.

**U05 · A theorem on operator ideals (127).** Part 1 states the adjoint and ideal estimates (1)–(2), the norm assertions (3), and an additive bound (4) for $S_p(A)=\|A\|_p^p$. The author also states completeness and a failure of local convexity for $p<1$ in infinite dimension. Part of the pencil apparatus refers to duality and reflexivity. The remaining assertions bound the sum of powers of the moduli of eigenvalues by $S_p(A)$, give monotonicity for positive hermitian operators, and state the product estimate (6) under $1/p+1/q\geq1/r$.

**U06 · Adjoint, ideal and dual estimates (128–129).** The proof of (1) appeals to Riesz. For (2) the author compares eigenvalues of the positive absolute operators attached to $A$ and to its products by $B$, with multiplicities and decreasing order specified. He invokes (6) for one side of the trace-supremum formula. A partial isometry, the spectral decomposition of $|A|$ and a Hölder equality are used to reach (7), which gives the triangle inequality through a supremum of seminorms. The assignment to $B$ on 129 creates a difficulty recorded under S03.

**U07 · The integral identity (129–130).** For nonnegative $\alpha_i$, the product $f(z)=\prod(1+\alpha_i z)$ relates $\sum\alpha_i^p$ to an integral of $\log f(r)$, with coefficient $p\sin(\pi p)/\pi$ and $0<p<1$. The lemma allows infinite values. The corollary applies it to $\det(1+z|A|)$ and obtains (9) for $S_p(A)$ in terms of $M_{|A|}$.

**U08 · The inequality below exponent one (130).** The author applies the determinant estimate to $|A+B|$. With the product reading of the blurred sign in (10), taking logarithms produces two integrals. A second application of (9) gives (4). The figure in the parenthetical reference after the determinant estimate is left open.

**U09 · The eigenvalue estimate (130–132).** The text introduces $s_p(A)=\sum|\alpha_i|^p$ for the eigenvalues. For $p<1$ it uses an estimate on the zeros of an entire determinant to compare $s_p(A)$ with $S_p(A)$ up to $p\pi/\sin(p\pi)$. Applying this at exponent $p/n$ to $A^n$ uses (6) to bound its norm. The factor tends to 1 as $n$ tends to infinity, giving (5). The change of letter size between $s$ and $S$ is essential on these sheets.

**U10 · Monotonicity and a discarded proof (132).** Monotonicity for $0\leq H\leq K$ is deduced from the componentwise comparison of their decreasing eigenvalue lists, with a reference to their extremal characterization. Below the fold, a crossed version of the proof of (6) introduces $L$, changes the exponents by division by $2m$, and rewrites (9) as an integral. The diagonal cancellations run through the final display.

**U11 · The dyadic product estimate (133–134).** A fresh proof of (6) begins with $r=1$. Formula (11) bounds the trace norm of a product of $2^n$ factors by the product of their $2^n$-norms. The induction groups neighbouring factors in pairs. The calculation on 134 rewrites a power of $ABB^*A^*$ inside a trace, moves the end factors around it, and applies the induction hypothesis to the alternating factors $A^*A$ and $BB^*$. The proposed extension to other traces is discussed in the opening parenthesis.

**U12 · From dyadic to conjugate exponents (135).** With $A=UH$ and $B=KV$, the positive factors are written as powers $h^\alpha$ and $k^\beta$, where $\alpha+\beta=2^n$. Applying the repeated-factor estimate gives a bound for dyadic reciprocal exponents. The passage to the limit introduces general conjugate exponents. The arrowed line extends the estimate to several factors with reciprocal sum 1. The lower paragraph returns to the dual supremum and the triangle inequality before a line of conditions ending at the edge of the sheet.

**U13 · An auxiliary lemma for (6) (136).** The author sets $H=A^*A$, $K=B^*B$ and $L=(AB)^*(AB)$. Formula (12) compares the $\alpha_n$ coefficients for powers of these operators. Passing to the exterior powers reduces the argument to $n=1$. The trace of the product is then compared with a product of norms using $2m$ factors. This sheet ends « d'où résulte le lemme ».

## Statements left without proof

| ID | Scan | Words on the page | What is supplied here |
|---|---|---|---|
| P01 | 127–128 | « est complet pour cette norme », « métrisable et complet, non localement convexe »; « conséquences très faciles » | The properties are stated and called consequences. The text deals explicitly with the inequalities, without a separate completeness or non-local-convexity argument on these scans. |
| P02 | 128 | « on sait (théorème de Riesz) »; « loc cité, page …, lemme … » | Unitary equivalence and an eigenvalue comparison are invoked. The latter reference has empty slots. |
| P03 | 129 | « Lemme 1 … Alors on a »; « les deux membres pouvant éventuellement être infinis » | Formula (8) is stated and used on 130. Its proof does not appear between statement and application. |
| P04 | 131–132 | « d'après une formule de majoration classique »; « caractérisation extrémale … classique » | The entire-function estimate and the extremal characterization of eigenvalues are both invoked without derivation. |
| P05 | 131, 133, 136 | « la formule (6), qui sera démontrée plus bas »; « comme nous le ferons plus bas »; « qui nous permettra de démontrer la formule (6) en … généralité » | The dyadic and conjugate-exponent arguments and the auxiliary lemma appear. These sheets end before a conclusion establishing all of (6). |
| P06 | 133 | « devoir s'appliquer sans modification au cas d'une trace … au sens de von Neumann - Dixmier » | The extension is announced in a parenthesis. A separate proof with the stated general trace is not written here. |

## Questions and conjectures

| ID | Scan | Words on the page | Scope |
|---|---|---|---|
| Q01 | 127 | « dire … quelles parties du théorème … sont connues »; « généralisation aux normes de Schatten? » | The first is an editorial question of attribution, the second a proposed extension. |
| Q02 | 128 | « Montrer qu'on peut se ramener à la dimension finie »; « unitairement équivalents » followed nearby by « (?) » or « (2) » | The marginal imperative requests a reduction. The second mark could be a query or a reference number. |
| Q03 | 133 | « ?? Il n'est d'ailleurs pas difficile … d'étendre alors le même … énoncé au cas où r≥1 » | The marginal double question mark qualifies the suggested extension. |

## Slips

| ID | Scan | Written reading and possible correction | Assessment |
|---|---|---|---|
| S01 | 127 | The introduction to (4) says $0<p\leq\infty$; the display says $0<p\leq1$. Use the displayed restriction for the $S_p$ triangle bound. | High. At $p=2$, $A=B=1$ gives $4>2$ in the proposed wider range. |
| S02 | 125–126 | In the positive factorization, the middle expression multiplies a determinant by $1+k/(1+h)$. A determinant around that second factor would keep the middle expression scalar. | Low for the intended correction. A letter in the quotient is doubtful. With the k reading, the scalar and operator expressions have different types in dimension two. |
| S03 | 129 | « $B=UA$ » would need $B=HU$ for the nearby $\operatorname{Tr}(HUA)$ and the stated bound involving $H$ and $U$. The reference « (formule (1)) » points to the adjoint identity; (2) is the product bound. | High for the mismatch. For scalar $A=2$, $U=H=1$, the written $B$ has norm 2; $HU$ has norm 1 and supplies the required trace. |
| S04 | 130 | $M_A(r)$ is defined with a supremum of $\det(1+zA)$ on a circle. Modulus bars around that determinant would give the real quantity later compared and placed under a real logarithm. | High for the ordering problem in the definition as written. Already for $A=1$ on the unit circle the values include $2$ and $1+i$. |
| S05 | 130–131 | The function estimate on 130 and the comparison of $s_p$ with $S_p$ on 131 both carry (10). | High. The subsequent reference on 131 uses the comparison containing sine. No new number is assigned here. |
| S06 | 131 | The second integral appears to have $r^{p-1}$ below the line. The comparison with (9) calls for $r^{p+1}$. | Low. The sign in the second integral is doubtful. |
| S07 | 135 | « or (lemme 1) » before the product of norms points mathematically to the repeated-factor bound (11) on 133. | High within this packet. The lemma headed 1 on 129 is an integral identity. |
| S08 | 135 | The limiting bound uses $H$ in both trace factors. The preceding decomposition requires $K$ in the second. In the earlier bound on the $K^\mu$ term, $1/\mu$ would match the exponent definitions. | Low for the written exponents and the proposed repairs. A scalar example distinguishes the two positive factors even when both exponents are 2. |
| S09 | 127 | Two occurrences of $\mathcal L^p(A)$ are surrounded by $\mathcal L^p$ with the Hilbert space as argument. | Medium. The difference in letter form is visible. The Hilbert space is the consistent domain in the statement. |

## Pointers

| ID | Scan | Words on the page | Referent |
|---|---|---|---|
| T01 | 124 | « de Cauchy-Schwartz » | The named inequality. The manuscript spelling includes t. |
| T02 | 127 | « Le déterminant de Fredholm »; « normes de Schatten? » | A faint heading and a slanted question about another family of norms. |
| T03 | 128 | « théorème de Riesz »; « comme dans [ ] »; « loc cité, page …, lemme … » | Riesz is named. The other two references are incomplete and identify no work or page. |
| T04 | 129 | « th. de Hölder classique sur les espaces » | The scalar or function-space Hölder result used with the spectral decomposition. |
| T05 | 131–132 | « formule de majoration classique »; « caractérisation extrémale … classique » | General results invoked without an author or bibliographic entry in these passages. |
| T06 | 133 | « au sens de von Neumann - Dixmier »; « Au N° suivant » | A notion of trace and an internal pointer to a later discussion. Neither supplies a publication title here. |

## Remarks of the model

**M01 · Model, high confidence (122).** The finite-vector example separates a coefficient limit from a norm bound on the whole ball. As a check on the displayed factorial expression, $m=5$, $n=3$ gives $12/25$ in both its factorial and product forms.

**M02 · Model, high confidence for the single-factor check (129).** With one nonzero $\alpha_i=1$ and $p=1/2$, numerical integration on $(0,1)$ and $(1,\infty)$ gives the right side of (8) within $3\times10^{-31}$ of 1. This tests the placement of the sine factor in one case.

**M03 · Model, low confidence as an editorial correction (128).** If « unitairement équivalents » means on the whole Hilbert space, the kernels deserve attention. For $Ae_j=2^{-j}e_{j+1}$, $A^*A$ has zero kernel whereas $AA^*$ kills $e_1$. Restriction to the complements of the kernels removes this obstruction. The phrase is interlined beside a doubtful mark, so the author’s intended scope remains open.

**M04 · Model, low confidence (130).** Multiplication at the knot in (10) fits both the determinant product above it and the addition of logarithms below. The ink itself admits a dot or a plus.

**M05 · Model, medium confidence (132–136).** Scan 133 restarts the paragraph numbered 3) with a two-factor grouping argument after the cancelled approach on 132. Scan 136 returns to powers of positive operators and the reduction to $n=1$. This is a relationship between arguments visible on these sheets; it does not establish the missing end of the general proof.

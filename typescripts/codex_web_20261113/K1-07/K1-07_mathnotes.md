# K1-07 · Mathematical notes

## What the pages do

**Scans 137–138, a trace estimate.** To prove formula (6), the author reduces to finite exponents with $1/p+1/q=1/r$. He introduces $L=(AB)^*(AB)$, $H=A^*A$ and $K=B^*B$. A coefficient bound for $M_{L^m}$, integrated against a power of $\rho$, gives an estimate involving $S_p(A)$ and $S_q(B)$. A change of variable in each integral produces the sine factors. Letting $m$ increase gives the boxed additive estimate (14).

**Scans 139–140, minimization.** Independent rescaling of $A$ and $B$ converts (14) into a minimization of $\alpha ax+\beta by$ under $x^\alpha y^\beta=1$, where $\alpha=r/p$ and $\beta=r/q$. Differentiation gives $ax=by$. The value $a^\alpha b^\beta$ appears both in the slanted working note and at the end of the proof. The inequality signs at those two places differ.

**Scan 142, convergence of Hermitian operators.** A proposition pairs convergence of the $p$-norms with a condition on spectral subspaces in intervals about a spectral value. Their dimensions eventually agree and $h_i$ tends to $h_0$. The first corollary gives a version using convergence in $L^\infty(\mathscr H)$ and convergence of the $p$-norms.

**Scans 142–143, continuity of powers.** The second corollary factors $A\mapsto |A|^r$ through $A\mapsto A^*A$ and $H\mapsto H^{r/2}$. The verification for the positive argument reduces to finite-dimensional spectral summands. The page writes their coefficients and vectors separately, then forms the sum with powered coefficients.

**Scan 143, weak convergence and a power inequality.** The first remark proposes weak convergence plus convergence of norms as a criterion in a stated range of $p$, then asks about uniform convexity. The second asks how $S_p|H^r-K^r|^{1/r}$ varies with $r$. An operator norm bound for $r<1$ would sharpen the preceding corollary.

**Scan 144, two bounds for $\rho$.** In the product estimate the author pulls a subspace of the intermediate space back by $u$ and intersects it with a subspace of the domain. A supremum on the intersection gives the displayed upper bound. For the sum, he again restricts the argument to an intersection. A separate question below the rule asks about an estimate for a single eigenvalue.

**Scan 145, spectral convergence and continuity.** The sheet starts with convergence of compact operators on a Banach space, then specializes to Hermitian operators. The author lists a norm condition and spectral convergence, with a parenthesis about checking the latter near each nonzero spectral value. The corollaries return to $u\mapsto|u|^r$ and weak convergence. He asks about extending continuity on the positive cone to all of $L(E)^+$.

**Scan 146, two questions.** The first concerns convexity of $L^p(E,F)$. The second relates continuity of $h\mapsto h^r$ to a bound for $h^r-k^r$ and to monotonicity of $S_{p/r}(h^r-k^r)$. The page specifies positive Hermitian $h,k$ and mentions $p=1$ separately. In the first inequality the power follows the closing norm strokes.

**Scan 147, the theorem and its cutoff lemma.** The theorem passes from $A_i\to A$ in $L^p$ to $\widehat A_i\to\widehat A$ in $\Sigma_p$. The lemma seeks a common small cutoff $\rho$ controlling the $p$-sum over $r_\nu(A_i)\leq\rho$. A function equal to $e^{pt}$ up to $\log\rho$ and linear above it compares the two sequences denoted $r_\nu$ and $s_\nu$. The page then reduces to positive operators. The hats and $\Sigma_p$ receive no separate definition on this sheet.

**Scans 147–148, the two parts of the cutoff argument.** Part a) rewrites a logarithmic sum using $dn(r)$ and integration by parts. This leaves $\rho^p n(\rho)$ and a weighted integral. Part b) subtracts the contribution above the cutoff from $S_p(A_i)$, takes the indicated limit, then chooses $\rho$ and $i$ in that order. The two lettered statements on 147 are crossed. The proof paragraphs remain live.

**Scan 149, the determinant and its coefficients.** The opening formulas relate $R(u)$ to $\det(1+u)/(1+u)$ and to a series of $P_n(u)$. The theorem compares the absolute values of $P_n(u)$ and $R(u)$ with the corresponding expressions at $|u|$. For positive $u$, a second assertion concerns the individual terms in a formula for $P_n(u)$. The corollary gives operator norm bounds involving $\det(1+|u|)$ and $\|u\|_1^n/n!$.

**Scans 149–150, the diagonal computation and the lower bound.** For a diagonal expansion of $u$, the coefficient at the $i$th basis vector is written as a sum of products over sets of indices excluding $i$. A recurrence is sketched. The author then writes the associated product $\prod_{j\ne i}(1+\lambda_j)$ for an eigenvalue of $R(u)$. On 150 the argument uses small $\lambda_i$ to derive a lower bound by $|\det(1+u)|$ and claims equality in the positive case.

## Statements left without proof

| Scan | Words on the sheet | What is left to the reader |
|---|---|---|
| 137 | « en vertu du lemme 2 »; « en vertu de la formule (9) » | The coefficient comparison and the integral identity are used from earlier material. |
| 139 | « Or on vérifie aussitôt que la … borne inférieure du second membre est atteinte » | The compactness argument indicates attainment. It does not discuss all boundary cases in the definition of the infimum. |
| 142 | « il faut et il suffit que »; « Les deux conditions suivantes sont néc. et suffis. » | The equivalence in the proposition and the first corollary are stated here. The proof sketch that follows concerns powers of positive operators. |
| 142–143 | « en vertu d'une proposition préliminaire »; « condition 1 triviale » | The assertion about topologies is referred back; the first condition is treated as immediate. |
| 143 | « il faut et il suffit qu'elle converge faiblement »; « ceci est connu au cas hilbertien » | No proof of the claimed range of the weak-convergence criterion is supplied on this sheet. |
| 144 | « Or il existe »; « On peut avoir » $\limsup \lvert\lambda_i(u)\rvert/\rho_i(u)=+\infty$ | The choice of extremizing subspaces and the example for the limsup assertion are not exhibited here. |
| 145 | « De plus, convergence des projecteurs spectraux »; « il est nécessaire et suffisant que » | The first convergence statement stops short of a precise formulation. The Hermitian criterion and the final corollary are restated without a new proof. |
| 145 | « ce dernier … se vérifie spectralement » | The spectral verification of continuity is indicated, without details. The noun after « dernier » is doubtful. |
| 147 | « Cela résulte facilement du »; « et il est bien connu » | The deduction from the cutoff lemma and the counting-function estimate $\rho^p n(\rho)\to0$ are invoked. |
| 148 | « il suffit de prendre … puis $i$ assez grand » | The displayed convergence of the large-value part is used with no separate discussion of a value exactly at the cutoff. |
| 149 | « par récurrence on obtient »; « 2) Se vérifie sur les valeurs propres de façon immédiate » | The intermediate recurrence and the asserted monotonicity check are abbreviated. |

## Questions and conjectures

| Scan | Author's words | Subject |
|---|---|---|
| 142, margin | « faux ds le cas non hermitien » (tentative) | A possible objection to extending the spectral proposition beyond the Hermitian case. |
| 143 | « Est-ce vrai si $p<+\infty$ ? Uniforme convexité de $L^p$ ? » | Extending the weak-convergence criterion. |
| 143 | « Est-ce que … est fonction croissante de $r$ »; « Il suffirait de savoir que $r<1$ implique » | Monotonicity of the power expression and a sufficient norm estimate. |
| 144 | « Majorations individuelles pour … ou analogue ? » | A proposed upper bound for $\lvert\lambda_i(u)\rvert$ in terms of a $\rho$ with a changed index. |
| 145 | « c'est sans doute vrai aussi de $L(E)^+$ dans $L(E)$ ? Inégalités précises ? » | Extension from compact positive operators and quantitative control. |
| 146 | « Question » … « pour $0<p<\infty$ ? Pas d'importance. » | Convexity of $L^p(E,F)$. The intervening words have several readings. |
| 146 | « Il semble possible que »; « est fonction croissante de $r$ »; « On peut faire aussi $p=1$. » | Power differences of positive Hermitian operators and a possible special case. |

## Slips

The IDs also identify the comparisons in the check-event ledger. Confidence concerns the proposed correction. Where a doubtful or overwritten reading is involved, confidence is low.

| ID | Scan | As written, possible correction and reason | Confidence |
|---|---|---|---|
| S01 | 137, lines 1–2 | Both memberships start with $A$. The subsequent argument pairs $A\in L^p$ with $B\in L^q$. | High |
| S02 | 137, line 9; 138, lines 11–16 | $p,q\leq 2m$ permits a zero sine denominator. **S02-R.** Choose $m$ strictly larger than $p/2$ and $q/2$ for this computation. | High |
| S03 | 138, line 2 | The last factor is $M_H$. The sum above it and the integral in (13) use $K^m$ in the corresponding position. | High |
| S04 | 138, line 3 | « compte tenu de (12) » may point to (11) on 137. A reference to a different formula outside the selection remains possible. | Low |
| S05 | 138, lines 17–20 | $\leq+\infty$ does not itself assert finiteness. The finite bound in the preceding display suggests $<+\infty$. The subscript on $S$ is doubtful. | Low |
| S06 | 139, lines 6–7 | $c=S_r(C)$ has an unintroduced $C$. The preceding left side involves $AB$. The subscript on $S$ is uncertain. | Low |
| S07 | 139, lines 18–19 | The denominator $\alpha x^{\alpha-1}y$ omits the power $\beta$ on $y$ that appears in the differential immediately above. | High |
| S08 | 140, line 3 | The final $c<a^\alpha b^\beta$ should permit equality (**S08-R**, $c\leq a^\alpha b^\beta$). With $a=b=c=x=y=1$ and $\alpha=\beta=1/2$, the preceding bound is attained. | High |
| S09 | 143, lines 9–12 | The first norm has $K_i$. The convergence statement has only introduced $H_i$ at this point. | Medium |
| S10 | 144, line 3 | The first Inf is indexed by $E_{m+n-1}$. With the page's later $E_{p-1}$ convention for $\rho_p$, the trial-space index would be $m+n-2$. | Medium |
| S11 | 144, lines 8–9 and 13 | The codimension comparisons point $\geq$. **S11-R.** The upper bound requires $\leq$. Two coincident lines in a plane have intersection of codimension one, while the individual codimensions sum to two. | High for the intersection inequality; low for the separate reading of the overwritten line in the sum case |
| S12 | 145, lines 14–15 | The first map changes letters between the variable $U$ or $u$ and $\lvert A\rvert$. The next map is consistently $u\mapsto\lvert u\rvert^r$. | Low |
| S13 | 147, line 10 | The two pieces of the sum have cutoffs $\leq\rho$ and $\geq\rho$. An entry equal to $\rho$ contributes twice to this split. One side should be strict for an exact splitting. | Low, because the cutoff signs are closely written or thickened |
| S14 | 148, line 2 | The prefactor changes from $p\rho^p$ on 147 to $p\rho^\alpha$. Keeping $p$ as the exponent would continue the preceding estimate. | Medium |
| S15 | 148, line 2 | The displayed upper bound uses $\int_0^\infty n(r)\,dr/r$. A single positive entry makes this integral infinite. Keep the positive lower cutoff and estimate the weighted integral itself. | High for the line with lower limit 0; the earlier lower limit on line 1 is a separate doubt |
| S16 | 148, lines 6–7 | The leading power in part b) looks like $r$ or $p$. The subtraction from $S_p$ uses $p$-powers. | Low |
| S17 | 149, lines 6–8 | The displayed polynomial has all plus signs. The exclusion-of-$i$ formula and the later alternating expression suggest the alternating version **S17-R**, with a factor $(-1)^k$ on $\alpha_{n-k}(u)u^k$. At degree one the sign changes the scalar answer. | High for the discrepancy at degree one |
| S18 | 149, lines 18–21 | The $\alpha_2$ term repeats $u^{n-1}$. The degree and the next general expression indicate $u^{n-2}$. | Medium |
| S19 | 149, lines 20–21 | The last product in the recurrence ends with $i_k$. The preceding degree-$n$ exclusion formula ends with $i_n$. The upper limit of the recurrence is doubtful. | Low |
| S20 | 150, lines 1–2 | The quotient numerator could read $\det(1+\lambda)$ or $\det(1+u)$. The continuation of 149 favours $u$. | Low |

## Pointers

- **137–138.** « démontrons la formule (6) », « les formules (2) », « comme dans le lemme 2 », « en vertu de la formule (9) », and « compte tenu de (12) ». The sheets also label (11), (13) and (14). The marginal « sur les fonctions entières » appears to call for another lemma or a reference.
- **142–143.** « une proposition préliminaire sur l'identité de … ces topologies », « les conditions de la prop. 1 », and « dans le corollaire 1 ». The struck diagonal note on 143 appears to end « de Murray ». Its preceding words do not securely identify a work or result.
- **145.** « se vérifie spectralement » points back to the spectral convergence discussion without naming a text.
- **147–150.** « Preuve de a) » and « Preuve de b » link the two sheets of the cutoff calculation. « partie de $***$ » and « l'inégalité $***$ a) » on 150 point to the corollary on 149. There is no explicit cote number or bibliographic citation in this selection.

## Remarks of the model

- **M01 · Scans 139–140 · High confidence.** My check of the weighted minimum gives equality when $a=b=x=y=1$. The strict sign at the end affects even this simplest case.
- **M02 · Scans 147–148 · High confidence for the example.** My one-entry check has $n(r)=1$ for $0<r<1$. The weighted tail for $p=1$ is $\rho\log(1/\rho)$, which tends to zero although the proposed integral from zero diverges. This example locates the faulty comparison without deciding the general convergence theorem.
- **M03 · Scan 149 · Medium confidence about the scope of statement 2.** If « la suite des termes » means increasing $k$ as in the adjacent sum, a single positive eigenvalue $t$ gives terms $0,t^2,t^2$ at $n=2$. They fail to decrease in that order. The sheet may group or order the terms differently.
- **M04 · Scans 149–150 · Low confidence about the hypothesis.** In dimension one with $u=1$, the determinant quotient gives $R(u)=1$, while $\det(1+u)=2$. The lower bound on 150 depends on a hypothesis. The nearby appeal to arbitrarily small eigenvalues makes the faint reference to infinite dimension material.

**Reading questions recorded after the final transcription hash**

| Scan and line | Frozen reading | Other reading considered | Reason |
|---|---|---|---|
| 147, left of « Preuve de a) », lines 19–20 | No separate sign at this position | A double check mark, or crossed trial strokes | Two short arms meet oblique rising strokes. They have no clear attachment to a letter or to the display. |
| 149, line 3, between the label and the box | No separate sign between the doubtful label and the first norm | A cancelled equals sign, or strokes reinforcing the box edge | Two short horizontal strokes cross an upright that also forms the left edge of the box. |

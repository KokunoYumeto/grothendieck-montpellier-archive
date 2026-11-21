# A097. Independent review of the fixed-second-part construction

## Scope and result

**PASS after the explicit distinct-shape clarification in G040 §7.** I read the whole saved report `work/root/fixed_second_part_report.md`, FS.1–FS.18 and all eight sections, including the amended restriction–induction formula. The review covers the actual maps, every finite-degree endpoint, the positive basis construction and the claimed fixed-parameter bit bounds. General execution of the proposed algorithm has not been performed in this audit, and no generic execution receipt is asserted.

The effective outer label is changed by the actual determinant pairing already checked in the stable balanced chart. For the parameters in FS.1, the first partition gap is nonnegative: at the smallest allowed $n=a+t$ it is $(m-2)a-b\ge0$. The second gap is $a-b\ge0$. Thus the transport applies to every displayed input, including $m=3$, $a=b$ and $t=0$.

## 1. Complete transfer and cokernel

The map is the actual multiplication–derivative map
$$
\phi_b(f\otimes v_1\cdots v_b)
 =\sum_i fv_i\otimes\prod_{j\ne i}v_j.
$$
For source first-factor degree $u$, the two-row Pieri summands have highest vectors
$x^{u-i}X^{b-i}(xY-yX)^i$.
The derivative $x\partial_X+y\partial_Y$ annihilates the bracket and multiplies the remaining highest vector by $b-i$. In the target, the same summand occurs precisely in the corresponding Pieri range. It follows that the kernel is zero for $u<b$, and is exactly $S_{(u,b)}W$ for $u\ge b$. For target first-factor degree $j\le b-1$, the one missing summand is $S_{(b-1,j)}W$; for $j\ge b$ there is none. This proves the complete finite cokernel in FS.4, including degree $b-1$, the last degree $2b-2$, and the two-dimensional standard module at $m=3$.

Writing $L=2b-2$, its smallest nonzero degree is $b-1$. Therefore every $e_i$ with $i\ge b$ kills that actual cokernel: its image would have degree at least $2b-1$. The tightened choice $B=\min(m,b-1)$, $J=\mathbb Q[e_2,\ldots,e_B]$ and $Y=(e_{B+1},\ldots,e_m)$ is valid. The low-variable action is induced from multiplication on the first symmetric factor of the displayed map. It is not chosen from a character calculation.

## 2. Finite covariants and rational size bounds

Every required raw symmetric-factor degree is bounded in terms of $b$. Hence the raw matrix dimensions are polynomial in $m$ for fixed $b$. The centered permutation action and the elementary invariant formulas have polynomially many rational coefficients of polynomial bit length in the basis $e_i-e_m$.

The near-row test $\nu_1\ge m-L$ is justified by an injection through rational Young projectors into $W^{\otimes e}\subset(\mathbb Q^m)^{\otimes e}$. A word orbit with $l$ different letters is the coset representation for $S_{m-l}$; its one-box induction chains contain the row $(m-l)$. Thus no discarded label can occur in the finite cokernel.

For a surviving label, at most $L$ letters lie outside its first row in a row tabloid. Its tabloid realization has polynomial dimension. Every nonsingleton column contains a lower box; there are at most $2L$ boxes in all nonsingleton columns, so the size of the column group depends only on $b$. The orbit-span algorithm can retain actual integer orbit polytabloids, rather than repeatedly replacing them by rational combinations. Their coefficients remain bounded by that fixed column-group size. All adjacent-permutation matrices can then be obtained by solving against a single retained orbit basis. This gives the stated polynomial coefficient heights as well as polynomial dimensions; repeated elimination does not require an unsupported bound on exponentially growing intermediate rational vectors.

The equations $T\rho_\nu(s_i)=\rho_C(s_i)T$ compute the covariant spaces exactly because the adjacent transpositions generate $S_m$. The invariant multiplications commute with those transpositions and descend to those exact solution spaces. The number of low degrees and low invariant variables is bounded by $b$, so their quotient and intertwining computations have polynomial bit size. When $m\le L$, any finite dimension absorbed in this argument is bounded by a function of $b$.

## 3. Minimal covers and actual free cancellation

Choose the generator basis of $C_\nu/J_+C_\nu$ and homogeneous lifts. Each generator degree is at most $L$. The greedy normal-monomial argument can be performed separately in each weighted degree; multiplication preserves the chosen module term order. Consequently the retained monomials form the complement of the initial relation module and have weight at most $L$.

No basis vector of the minimal cover is a leading relation with constant coefficient: that would contradict minimality in $C_\nu/J_+C_\nu$. Every minimal monomial in the leading relation module therefore has a variable divisor whose removal is normal. Its weight is at most $L+B$. The corresponding relation has a remainder consisting of earlier retained monomials in the same weighted degree. These leading terms generate the entire initial module, so the relations generate the full kernel. This proves the finite degree bound used to obtain $F_1\to F_0$.

Over $I=J[Y]$, the relations are generated by the low relations and $y_i$ times the generators of $F_0$. At $Y$-degree zero, their minimality is the minimality of $F_1$. At a single high-variable degree, it is the independence of the free-generator residues of $F_0$. Higher $Y$-degrees add no generators. Thus FS.8 is the actual minimal first pair of covers of $C_\nu$.

The two cover cancellations from G039 apply without any additional freeness assertion about the relation module. In the first cancellation, a basis of the target free module is adapted to its minimal cokernel generator residues; subtracting homogeneous combinations of those selected generators makes the complementary basis vectors have zero image. They can be lifted through the transfer, and their free pairs cancel. In the remaining domain, a basis is adapted to the minimal relation residues. Complementary images are positive-degree combinations of the selected relations and are killed by the corresponding triangular basis change. Both changes are invertible homogeneous changes of free bases. Their complementary free summand has precisely FS.11 as its basis polynomial. Its coefficientwise nonnegativity follows from these actual cancellations, including the case $C_\nu=0$.

## 4. The high-variable kernel decomposition

For a fixed nonzero high-variable exponent vector $\beta$, put $S=\{j:\beta_j>0\}$ and choose its first element $i$. The degree-$\beta$ map is exactly
$$
F_1\oplus F_0^S\longrightarrow F_0,\qquad
(u,(v_j))\longmapsto d_Ju+\sum_jv_j.
$$
The inverse pair displayed in FS.13 is literal:
$$
(u,(v_j)_{j\ne i})\longmapsto
(u,-d_Ju-\sum_{j\ne i}v_j,(v_j)_{j\ne i}),
$$
and its inverse reads the unrestricted coordinates. Multiplying the first component by $y^\beta$ and the $j$th relation component by $y^{\beta-e_j}$ preserves all weighted degrees and gives polynomial vectors. This verifies the exact decomposition even when $d_J$ has a kernel.

At $\beta=0$ the remaining module is $K_J$. For $\beta\ne0$ the free choices are one copy of $F_1$ and $|S|-1$ copies of $F_0$. The latter choices are exactly the previously checked least-support star-cycle basis. This proves FS.14, with both high terms zero for an empty variable list and the cycle term zero for a one-variable list.

## 5. Primary degree bounds and their exact use

I opened and read Aschenbrenner, *Ideal membership in polynomial rings over the integers*, §3 through Theorem 3.2, including the complete homogeneous reduction, its recurrence and finite-field descent. The precise locator is PDF pp.13–16, Theorem 3.2 on printed/PDF p.16:

https://www.mat.univie.ac.at/~maschenbrenner/pdf/ideal2.pdf

The theorem bounds generators of the solution module of an $r_0$-row polynomial matrix of degree at most $\delta$ over a field by $(2r_0\delta)^{2^\ell}$. This is exactly the use in FS.15 after taking harmless maxima for zero ranks. In the proof's division paragraph, the free coordinates are the coordinates $r+1,\ldots,n$ associated to its displayed vectors (3.1); the isolated printed range $n-r+1,\ldots,n$ is an indexing slip and is not used literally in this audit.

I also opened Liang, *Degree bounds for Gröbner bases of modules*, arXiv:1905.07517v3; I read the statements and intervening proof passage containing Theorem 37/Corollary 38, §8, Theorems 40–41 and Corollary 42, and visually checked Corollary 42 on PDF p.19 (printed p.19):

https://arxiv.org/pdf/1905.07517

Corollary 42 bounds the reduced basis degree by $2(Dr)^{2^\ell}$ for a submodule of a rank-$r$ free module generated in degrees at most $D$, with any module monomial order. Here ordinary basis degrees are deliberately set to zero. Applying it with $D=H$, $r=r_1$ gives exactly FS.16. The zero and full kernels are treated directly. This use does not identify the ordinary grading with the original weighted grading.

These are source checks of the stated passages; this audit does not claim to reconstruct every earlier theorem in Liang's paper.

## 6. A polynomial bit algorithm, not only a degree existence bound

For fixed $b$, the tightened bound $\ell=B-1\le b-2$ is fixed, and $r_0,r_1$ and their coefficient heights are polynomial in $m$. At $b=2$, $J=\mathbb Q$, $F_0=C_\nu$ and $F_1=K_J=0$; the high-variable formula reduces to the ordinary weighted-star cycle term. I reread this amendment in the author's report. Therefore $H$ and $G$ are polynomial in $m$, with computable exponents depending only on $b$. The ambient coefficient system for all vector polynomials of ordinary degree at most $G$ has polynomial dimensions:
$$
r_1\binom{G+\ell}{\ell}
\quad\hbox{unknowns, and at most}\quad
r_0\binom{G+\delta+\ell}{\ell}
\quad\hbox{coefficient equations}.
$$
Its entries are the already bounded coefficients of $d_J$. Exact rational nullspace and row-reduction operations have polynomial bit complexity; the final numerator and denominator heights are bounded by minors of these polynomial-size matrices.

Every element of the full reduced Gröbner basis lies in this solution space. Row reduction followed by divisibility-minimal leading-term selection therefore finds its leading generators. More explicitly, each globally reduced basis element has no trailing term in the full initial module; hence it has no trailing pivot in this finite solution space. Its pivot row is consequently the same unique reduced row in that space. This justifies the proposed finite search even for a term order that is not ordinary-degree-compatible.

Weighted-homogeneous components are preserved by the matrix equation and never increase ordinary degree. The reduced basis may therefore be chosen weighted homogeneous. All its ordinary exponent cuts are at most $G$.

The high- and low-degree character calculations do not require constructing exponentially large Specht modules for arbitrary $\nu$. For the free input characters, the number of distinct shapes at distance at most $b$ is polynomial in $m$; all small LR tableaux have at most $b$ boxes. Fake-degree polynomials have degree at most $\binom m2$ and coefficients bounded by the finite representation dimensions, whose binary lengths are polynomial in $m$. The signed arithmetic used to calculate the free numerator is separate from its positive basis interpretation proved above.

## 7. Correction to the restriction–induction enumeration

The initial wording about corner-removal paths could have counted a skew branching multiplicity twice. I requested an explicit distinct-shape convention. The author inserted it, and I reread the amended paragraph.

For the orbit indexed by $\rho$, let $l=\ell(\rho)$ and let $\sigma_d\vdash m_d(\rho)$ be the small-factor labels. Each shape $\eta\subseteq\nu$ of size $m-l$ is enumerated once. For each output $\kappa\supseteq\eta$ of size $m$, its multiplicity contribution is
$$
c^\nu_{\eta,\sigma_1,\sigma_2,\ldots}
c^\kappa_{\eta,\sigma_1,\sigma_2,\ldots}.
$$
Summing over the displayed distinct shapes and labels is exactly restriction followed by induction through
$S_{m-l}\times\prod_d S_{m_d(\rho)}$, under the tensor–coset map. Intermediate shapes for the ordered subgroup factors are counted inside the iterated LR coefficient. The order in which individual corner boxes were removed supplies no further factor.

The complete primary LR proof and the executable reading convention were independently read for A096 at Macdonald I§9, pp.142–147. The amended formula uses that precise coefficient and fixes the only counting ambiguity found here.

## 8. Positive bases, polytopes, exact values and scope

The exponent-grid construction counts monomials **inside** the initial kernel module. Cutting each axis at every generator exponent makes divisibility constant in a box. There are at most $(s+1)^\ell$ boxes per component, and both $s$ and the number of components are polynomial in $m$ for fixed $b$.

In each weighted degree, choose the first Gröbner element dividing an initial monomial and multiply it to that leading monomial. Distinct resulting leading terms prove independence. Gröbner reduction proves spanning and terminates within the finite weighted degree. Thus these lattice points index actual kernel vectors through a triangular basis lift; they do not merely reproduce a formal Hilbert series.

All weights are positive. Intersecting the boxes with FS.17 makes the pieces bounded, with the stated floor bounds. The other three types of terms are the nonnegative free numerator, the $F_1$ term with a distinguished first positive high exponent, and the $F_0$ least-support cycle term. Their tags are disjoint, and the inverse in §4 supplies the exact vector for every high-variable tag. The variable bound $3m+2b$ is a safe upper bound on every type.

For exact evaluation, use the original unbounded geometric series for the infinite box intervals, extracting only the requested degree. The finite cutoffs have polynomial size and create at most $2^\ell$ numerator shifts. The final degree-dependent upper bounds used to display bounded polytopes need not be inserted into these generating-series numerators. The rational-function degrees and coefficient heights are polynomial in $m$ for fixed $b$. The previously proved parity-extraction method in G037 then gives polynomial bit time in these sizes and $\log(D+1)$. The output coefficients themselves have polynomial binary length by the same finite-variable rational-series bound. Equality to zero decides support because the formula has already been carried to positive basis pieces.

The actual balanced chart, determinant map, transfer, finite quotient, cover changes, high-variable inverse and initial-term lift all preserve the asserted gradings. No scheme-theoretic pullback exactness or characteristic-$p$ rank assertion is needed. The result is a proved and specified finite algorithm for every fixed $b$, with general-purpose implementation still a separate task. This independent audit records a whole-proof and primary-source check, not an unexecuted computation.

# Final-draft SDP, residual-image and source audit

Auditor: agent `/root/grothendieck_sdp`, GPT-6 Astra Pro. Reasoning-effort setting is not exposed. Run: GCT_GINEQ. Review record completed at 2026-11-20 23:35:41 UTC, following final source and draft reads beginning at 23:32 UTC. The TSV timestamp is the observed clock time at completion of this review batch, not a claimed exact time for each intermediate read. This records human-readable mathematical checking by a model, not proof-assistant verification. Main TeX was not edited by this agent.

## Actual draft F-09–F-12: full targeted proof checks

The complete statements and proofs in `deliverable/GCT_GINEQ.tex` were read, including the intervening exact certificate. All four pass.

### F-09: directional SDP certificate — PASS

The block matrix has the required factor of one half, so its trace pairing with the Gram matrix is precisely the bipartite vector objective. The primal Gram factor supplies a lower bound $L\leq S$A$$. For a feasible dual slack, the trace pairing with a positive semidefinite Gram matrix is nonnegative; the unit diagonal makes the remaining pairing equal to the sum of dual coordinates. Thus $S$A$\leq U$. The Grothendieck inequality then gives $L/K\leq Q$A$\leq U$, with the division on the lower-bound side. No assertion of strong duality or numerical SDP exactness is needed.

### F-10: cube/Hilbert limitation and natural maps — PASS

Grouping pure unit test vectors bounds the complex Hilbert injective norm by the chosen matrix operator norm. A real matrix has equal real and complex operator norms, and real Euclidean unit vectors lie in the real coordinate cube, yielding the next inequality. Independent signs have squared objective expectation equal to the Frobenius norm squared, proving $Q$A$\geq\|A\|_F$. Thin-SVD left and right singular-vector rows have norms at most one and give vector objective equal to the nuclear norm; padding the two families by disjoint private coordinates restores unit norms without changing cross inner products.

The consequences have the correct dual direction: $S(F(W))\leq1$ implies matrix nuclear norm at most one, so the witness pairing with $T$ is at most the matrix operator norm of $F$T$$. Real witnesses still give valid complex tensor nuclear lower bounds, because the first inequality certifies their complex injective norm. The resulting direct support-norm rank bound is at most one. This conclusion is correctly confined to the specified unscaled relaxation.

The natural-map statement uses the sign-factorized disjoint blocks proved in F-03. Simultaneously removable row and column signs reduce determinant flattenings to nonnegative matrices. For a nonnegative matrix all equal vectors attain the sum of entries, while no individual inner product exceeds one. Matrix multiplication and both permanent forms are already nonnegative. Hence $Q=S=\sum|a_{ij}|$, with no dimension-sensitive Grothendieck gap on these maps. This does not assert the same for arbitrary preconditioning or arbitrary Koszul maps.

### F-11: matrix-rank-sensitive Grothendieck test — PASS

An optimum exists in dimension at most the number of row and column vectors. For an optimum, the span of the vectors $w_i=\sum_j a_{ij}v_j$ has dimension at most the matrix rank $q$. Optimizing each $u_i$ in its $w_i$ direction preserves the global optimum; zero $w_i$ can be assigned a unit vector in the same nonzero span. Reoptimizing each $v_j$ against the new $u_i$'s then places both families in that span. The zero cases are explicitly handled. The span is nonzero because a nonzero matrix has positive sign optimum.

This gives $S$A$\leq K_G^{\mathbb R}$q$Q$A$$. Monotonicity of the dimension-specific constants and independently certified $L,Q\leq U,\kappa_s$ prove the stated strict rank test. (Here the intended hypotheses are $L\leq S$A$$, $Q$A$\leq U$, and $\kappa_s\geq K_G^{\mathbb R}(s)$, as correctly printed in the draft.) A real matrix has the same rank over the reals and complexes, so the pure-atom rank-cost minor argument transfers the test to complex CP border rank. The observation that the universal constant or the same SDP upper bound cannot create the strict violation is valid.

The worked rational example and Boolean SOS identity also agree with the previously executed exact computation in `agent_sdp_checks.py`: objective $14/5$, sign optimum $2$, and $f^2-4=H_0$. No uniform small SOS certificate is asserted.

### F-12: Koszul cost and dimension ceiling — PASS

For a nonzero pure tensor, contraction in the $B$ factor has rank one and tensoring by a nonzero $C$ vector preserves rank. Wedge multiplication by a nonzero $A$ vector has rank $\binom{a-1}{p}$, including the endpoint cases $p=0,a-1$. Thus the pure-atom rank cost is positive. Source and target dimensions are $b\binom ap$ and $c\binom a{p+1}$. Dividing by the atom cost gives $ba/(a-p)$ and $ca/(p+1)$, exactly as printed. Rank subadditivity and determinantal closedness give the border bound. The nuclear/operator ratio certificates cannot exceed the actual matrix-rank certificate, by the proved singular-value bounds in F-02. These are fixed-map conclusions.

## Actual draft F-23: exact residual reduction — PASS

The complete actual F-23 statement and proof were read at 23:32 UTC. The claimed equality of the residual minimum is valid over the complexes, and separately for real Euclidean border rank with a consistent field.

For a row tensor residual image, the basis consists of squarefree alternating or symmetric tensors labeled by a $b$-element subset $I\subseteq[n]$. In a nonzero linear combination choose a nonzero coefficient. Project every remaining factor onto the coordinates of that subset. Any other subset of the same size contains an outside coordinate, so every basis monomial for it is killed. The chosen vector becomes a nonzero scalar multiple of the corresponding $b\times b$ row tensor.

For a polynomial residual image, labels are pairs $(I,J)$ of $b$-element row and column sets, and the basis elements are normalized coefficient tensors of minors or permanents. Projection of every factor onto the coordinate entries in $I\times J$ kills every other label: a different row or column set forces an outside variable in every monomial. It retains the selected normalized $b\times b$ polynomial tensor up to a nonzero scalar. There is no factorial problem: over the stated fields all normalization scalars are nonzero, and changing the scalar does not change border rank.

A tensor product of linear maps cannot increase border rank. This proves that every nonzero residual vector has border rank at least that of the smaller family member. Conversely the residual image contains a basis vector that is an embedded copy of the smaller tensor. Inclusion and the coordinate projection back are inverse on that smaller space; applying both proves equality of its border rank in the two ambient spaces. Therefore

\[
\min_{0\ne u\in U_{n,b}}\underline R(u)=\underline R(T_b),\qquad
\underline R(T_n)\geq\binom nb^s+\underline R(T_b)-1,
\]

with $s=1$ for row tensors and $s=2$ for polynomial tensors. This uses the independently checked F-13 image-substitution lemma.

Both normalized quadratic polynomial coefficient matrices have two disjoint nonzero off-diagonal $2\times2$ blocks, hence rank four. The quadratic consequence $\binom n2^2+3$, and its value $39$ at $n=4$, follow. Using a CP border-rank seed of $17$ for the cubic determinant yields $116$ and $416$ at $n=5,6$. The newly verified CP seed $16$ for the cubic permanent yields $115$ and $415$. A merely symmetric-border-rank lower bound is not an admissible CP seed; the draft explicitly and correctly says so. These are proved consequences, with no novelty or global-record claim.

## QI-01 candidate in `agent_quadric_image_candidate.md` — PASS

The entire candidate proof was checked independently. Quotienting the polar form by its radical gives a nondegenerate symmetric bilinear form of rank $\rho$. In either minor or permanent space, every single-row and single-column coordinate subspace is totally isotropic. If $0<\rho\leq3$, its image has dimension at most one. A nonzero coordinate vector therefore spans both its row image and its column image.

If two such vectors lie on distinct lines, they cannot share a row or column. The two crossed coordinate vectors lie in intersections of distinct one-dimensional row/column images and vanish. The minor/permanent coefficient relation then makes the original two vectors orthogonal. Their distinct isotropic lines would span a two-dimensional totally isotropic subspace, impossible for a nondegenerate symmetric form of rank at most three. Hence all nonzero coordinate images lie on one isotropic line, contradicting surjectivity and nondegeneracy. Rank is therefore at least four. A single minor or permanent has rank four, proving equality.

The proof is correctly scoped to characteristic zero here; it is not a characteristic-two polar-form argument. The F-23 coordinate restriction proof is a simpler proof of this particular rank-four consequence and extends to higher residual degree.

## Grothendieck source and wording audit

### B-03 and B-08 — PASS as cited background

The stated dictionary is correct: $Q$ is the injective norm on $\ell_1^m\otimes\ell_1^n$, equivalently the bilinear-form norm on $\ell_\infty^m\times\ell_\infty^n$; $S=\gamma_2^*$ under the usual factorization convention. Its polar compares $\gamma_2$ with the projective norm on the two $\ell_\infty$ spaces. This is distinct from Hilbert operator/injective norms and from higher-order Hilbert projective norms. Pisier's Theorems 2.4 and 3.1 are the relevant cited formulations.

The cut-norm references to Alon–Naor, Lemma 2.1, Theorem 4.3 and §4.4, and the bipartite XOR correlation references to Pisier, Theorem 12.12 and §19, support the qualitative claims as scoped. Normalizing an arbitrary nonzero coefficient matrix by the sum of its absolute entries gives the corresponding game biases. No CP-rank interpretation is asserted. Literature proofs were not reproduced here.

### B-06 — PASS after an applied wording correction

The initial wording excluded polynomial-time approximation solely from UGC. I requested the logically precise formulation: under UGC, approximation with any fixed loss factor below $K_G^{\mathbb R}$ is NP-hard; polynomial-time exclusion additionally uses $\mathsf P\ne\mathsf{NP}$. The actual draft reread at 23:32 UTC contains this correction.

Raghavendra–Steurer, *Towards Computing the Grothendieck Constant*, Theorem 1.1, is the hardness source; the source is https://www.dsteurer.org/paper/grothendieck.pdf . The algorithm proof at §3.3, (3.5)–(3.7), has the correctly directed reciprocal guarantee approaching $1/K_G$ from below. The printed Theorem 1.2's loss-factor sign discrepancy is recorded accurately in the draft. Theorem 1.3 concerns computability of the constant to prescribed accuracy. This check does not resolve UGC or certify an exact constant.

### Current numerical bounds — PASS as explicitly qualified source reports

The stated intervals are supported by the primary sources already inspected in this run, and the real lower and complex interval statements were reopened successfully at 23:33 UTC:

* Heilman–Jones–Malavolta, *Primal/Dual Method for the Grothendieck Constant*, arXiv:2610.10477v2, 14 November 2026, Theorem 1.1 on printed p.1: $1.773\leq K_G^{\mathbb R}\leq1.7799$. Theorems 4.1–4.2 are the certification components. URL: https://arxiv.org/pdf/2610.10477 .
* Bo Peng, *Certified Fourier rounding for the real Grothendieck inequality*, arXiv:2610.24417v1, 17 October 2026, Theorem 1.1 and §6, (41)–(43): $K_G^{\mathbb R}<44496791/25000000=1.77987164$. Author-posted full text had been opened and inspected earlier in this run at https://hub.valency.io/works/W_uhkyapjd ; the final direct reopen timed out, but primary indexed text was retrieved again at https://hub.valency.io/works/W_uhkyapjd_v1 and the arXiv abstract at https://arxiv.org/abs/2610.24417 .
* Heilman–Jones–Malavolta, *Sharper Bounds for the Complex Grothendieck Constant*, Theorem 1.1, equation (1.2), printed p.2: $1.4<K_G^{\mathbb C}<1.404898554746$. Author PDF dated 24 September 2026: https://www.stevenheilman.org/~heilman/papers/grothcx.pdf .

The large numerical certificates in these papers were not rerun. The paper correctly calls these date-specific preprint reports and declines to call the interval an exhaustive global record, in light of the unverified stronger Ren report mentioned by Peng. None of the newly proved rank arguments depends on those numerical endpoints.

## Newly confirmed permanent source

Austin Conner, Hang Huang, J. M. Landsberg, *Bad and good news for Strassen's laser method: Border rank of the 3x3 permanent and strict submultiplicativity*, arXiv:2009.11391v1, 23 September 2020.

Primary record: https://arxiv.org/abs/2009.11391 . Primary PDF: https://arxiv.org/pdf/2009.11391 .

**Exact locator:** Theorem 1.1, printed p.3 (PDF zero-based page 2), states the border rank of the Kronecker square of the small $q=2$ Coppersmith–Winograd tensor is 16. The sentence immediately following identifies that tensor with the $3\times3$ permanent tensor. The proof is in §5. Printed p.2 defines ordinary rank and border rank through the Segre variety, then separately defines Waring rank and Waring border rank. Thus the theorem supplies the required **ordinary complex CP border-rank equality** for the normalized symmetric polynomial tensor as well, because normalization changes only a nonzero scalar.

Theorem 1.1 is not marked as a numerical conjecture or numerical-only result. The explicit numerical caveat nearby belongs to the separate Theorem 1.3 about a different tensor. This distinction was checked. The arXiv record lists v1 only and the authors Conner, Huang, Landsberg. No journal publication metadata is asserted here. The source statement, scope and locator were verified; its full border-apolarity proof was not independently reproduced.

Web retrieval references useful for the root's own reopen: `turn186695470view0` (permanent PDF), `turn425430425view0` (arXiv record), `turn162589250view0` (real constant), `turn162589250view2` (complex constant), `turn824402334search3` (Peng author-posted version), `turn824402334academia6` (Peng arXiv abstract).

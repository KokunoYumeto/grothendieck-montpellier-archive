# F18: uniform subspace norm bounds combined with border substitution

Reviewer/reprover: `/root/tensor_norms`, GPT-6 Astra Pro (inherited); effort not exposed. Run `GCT_GINEQ/tensor_norms`. This note independently reconstructs the parent's proposed F18 and records a necessary proof repair and field distinction. No novelty is claimed for the substitution lemma or the resulting classical matrix-multiplication lower bound.

## F18a. Image-substitution lemma

Let `K=C`, or let `K=R` with **Euclidean real border rank** throughout. Let

`T in A_1 tensor ... tensor A_k tensor B_1 tensor ... tensor B_b`

be nonzero, `k,b>=1`. Put `A=A_1 tensor ... tensor A_k`, `B=B_1 tensor ... tensor B_b`. View the regrouped tensor as a linear map `T_A:A* -> B`. Let `U=im(T_A)` and `q=dim_K U`. Rank of `T` refers to its original `k+b` factors; rank of `u in B` refers to the `b` factors `B_i`. Then

`border R(T) >= q + min_{0!=u in U} border R(u) - 1`.

**Complete proof.** Set `r=border R(T)`. Choose tensors `T_nu -> T` with CP rank at most r. For each `nu`, a rank-at-most-r decomposition in the original factors becomes

`T_nu = sum_{j=1}^{r} a_{nu,j} tensor z_{nu,j}`,

where every `z_{nu,j}` is simple in `B_1 tensor ... tensor B_b`; zero summands can be omitted. Define `S_nu=span{z_{nu,j}:1<=j<=r}`. Then `im((T_nu)_A) subset S_nu` and `s_nu=dim S_nu<=r`.

Choose fixed functionals `f_1,...,f_q in A*` such that `T_A(f_1),...,T_A(f_q)` form a basis of U. Their approximating images `u_{nu,i}=(T_nu)_A(f_i)` converge to those independent vectors, so they are independent for all sufficiently large `nu`. Put `U_nu=span{u_{nu,1},...,u_{nu,q}}`. Thus `dim U_nu=q`, `U_nu subset S_nu`, and `U_nu -> U` in the Grassmannian. The latter also follows directly by convergence of the basis matrices and their orthogonal projection matrices. In particular `s_nu>=q`.

Select a basis `z'_{nu,1},...,z'_{nu,s_nu}` of S_nu from its simple generating atoms. Let `H_nu` be the span of its first `s_nu-q+1` members. Since both H_nu and U_nu lie in S_nu,

`dim(H_nu intersect U_nu) >= (s_nu-q+1)+q-s_nu = 1`.

Choose a unit vector `v_nu` in this intersection. It is a linear combination of at most `s_nu-q+1 <= r-q+1` simple B-atoms, hence `R(v_nu)<=r-q+1`. By compactness of the finite-dimensional unit sphere, a subsequence converges to a unit vector v. Since `v_nu in U_nu` and `U_nu -> U`, we have `v in U`; in particular v is nonzero. Definition of border rank yields `border R(v)<=r-q+1`. Rearranging proves the assertion. QED.

**Necessary repair to the proposed proof.** One cannot generally choose a pure-atom basis of `im((T_nu)_A)`: the image need not contain its decomposition's individual right-hand atoms. For example, `e_0 tensor I_2=e_0 tensor e_0 tensor e_0+e_0 tensor e_1 tensor e_1` has first flattening image `span{I_2}`, which contains no nonzero rank-one matrix, although its decomposition has two simple right-hand atoms. The proof must instead use `S_nu`, the span of those atoms, which contains the image and has dimension at most r. The corrected intersection argument above proves exactly the desired conclusion.

Over C, the usual algebraic border rank agrees with the Euclidean approximation definition: the rank-at-most-r locus is a constructible image of the polynomial decomposition map, and its Euclidean and Zariski closures coincide. Thus the sequence proof gives the standard complex algebraic statement.

The proof does not require the entire approximating flattening image to have constant dimension q. Fixed independent source columns select the q-dimensional subspace U_nu even when the full image has larger rank.

## F18b. Uniform norm certificate for the minimum

Assume `b>=2`, use the Hilbert tensor norms over the same field K, and suppose that for some `alpha>0`,

`sigma_K(u)^2 <= alpha ||u||_F^2` for every `u in U`.

N-01 applied to the b-factor tensor u gives

`border R_K(u) >= ceil[(||u||_F/sigma_K(u))^(2/(b-1))] >= ceil[alpha^(-1/(b-1))]`.

Consequently

`border R_K(T) >= q + ceil[alpha^(-1/(b-1))] - 1`.

This genuinely can improve upon the matrix rank q of the chosen ordinary flattening. Its extra information is a **uniform norm inequality on every nonzero element of the flattening image**, combined with border substitution. It is not merely a scalar norm comparison applied to the original tensor, and it does not contradict the earlier dominance statements about that narrower conversion.

The field quantifier is essential: to certify complex border rank of a real tensor, the bound must hold for every `u in U_C=U_R tensor_R C`, with the complex injective norm. A bound proved only on U_R gives the real Euclidean result.

## F18c. Matrix multiplication specialization, exact norm computation

Let

`M_n=sum_{i,j,k=1}^n E_ij tensor E_jk tensor E_ki`.

Contract its first matrix factor with coefficients `X=(x_ij)`. The resulting two-factor tensor is

`u_X=sum_{i,j,k} x_ij E_jk tensor E_ki`.

As a coefficient matrix it has rows `(j,k)` and columns `(k',i)`, with entry `delta_(k,k') x_ij`. Reorder the rows as `(k,j)`. It becomes the block-diagonal matrix `I_n tensor X^T` (with the analogous compatible column ordering). These are orthonormal basis permutations, so all matrix singular values and norms are unchanged. The map X to u_X is injective; therefore `q=n^2`.

Every singular value of X is repeated n times in u_X. Over both R and C,

`||u_X||_F^2 = n ||X||_F^2`,

`sigma(u_X)=||u_X||op=||X||op`,

and hence

`sigma(u_X)^2 / ||u_X||_F^2 <= 1/n`.

Equality holds whenever X is nonzero of rank one, so this uniform constant is exact. With `b=2`, F18b gives

`border R_C(M_n) >= n^2+n-1`.

The same bound holds for real Euclidean border rank. It improves the ordinary mode-flattening bound n^2 for n>=2. It is substantially weaker than known Koszul/substitution lower bounds and is not a new record. Equivalently, every nonzero u_X has matrix rank `n rank(X)>=n`, and the minimum is n; the stable-rank norm proof exactly recovers this minimum.

**Rectangular check.** For `M_(a,b,c)` in dimensions `ab,bc,ca`, contraction of the ab-dimensional first factor gives `I_c tensor X^T`. Thus `border R >= ab+c-1`, and cyclically

`border R(M_(a,b,c)) >= max{ab+c,bc+a,ca+b}-1`.

This specialization includes n=1 correctly and does not use a grouped-tensor-norm multiplicativity assumption.

## F18d. Explicit field counterexample to an overbroad real formulation

Let

`I=[[1,0],[0,1]]`, `J=[[0,-1],[1,0]]`, and `T=e_0 tensor I + e_1 tensor J in (R^2)^{tensor3}`.

Its flattening image is `U_R=span_R{I,J}` and q=2. Every nonzero real matrix `aI+bJ` satisfies

`(aI+bJ)^T(aI+bJ)=(a^2+b^2)I`.

Thus its matrix rank is 2 and `sigma^2/F^2=1/2`. The real Euclidean version of F18 gives `border R_R(T)>=3`.

Over C, the matrices `P_+=(I-iJ)/2` and `P_-=(I+iJ)/2` each have rank one, and

`T=(e_0+i e_1) tensor P_+ + (e_0-i e_1) tensor P_-`.

Hence `R_C(T)=border R_C(T)=2` (the flattening rank gives the matching lower bound). The norm bound `alpha=1/2` fails on U_C, which contains nonzero rank-one matrices. This explicitly refutes transfer of a merely real-uniform norm certificate to complex border rank.

It also refutes the same real-minimum substitution inequality if "real border rank" is instead defined using **real Zariski closure**. The real rank-at-most-two locus in `(R^2)^{tensor3}` is Zariski dense in the whole ambient space: at the decomposition `e_0^{tensor3}+e_1^{tensor3}`, the differential of the two-summand decomposition map spans all eight coordinate tensors (the first tangent spans entries with at most one 1, and the second those with at least two 1s). Thus its image contains a Euclidean open subset, and no nonzero real polynomial vanishes on all rank-at-most-two tensors. T therefore has real-Zariski border rank 2, whereas `q+min_{u in U_R}rank(u)-1=3`.

For the intended complex algebraic F18 statement, none of this causes a problem; use U_C and complex norms from the outset.

## Exact primary-source locators for the known substitution method

1. Landsberg--Michalek, *A 2n^2-log_2(n)-1 lower bound for the border rank of matrix multiplication*, arXiv:1608.07486; author PDF https://people.tamu.edu/~jml/LMsubmmult160825.pdf, **Proposition 2.3, p.3**. For an A-concise three-factor tensor it states `border R(T)>=min_{A' in Gr(a',A*)}border R(T|_(A' tensor B* tensor C*))+a-a'`. Setting `a'=1` after passage to the concise A-support yields F18a for three factors. Our full atom-span proof establishes the same assertion with any number of ungrouped remaining factors.
2. Landsberg--Michalek, *On the geometry of border rank algorithms for matrix multiplication and other tensors with symmetry*, arXiv:1601.08229v1, https://arxiv.org/pdf/1601.08229, **Section 5, Lemma 5.2, p.12**, gives the one-hyperplane border-substitution lemma. The paper specifies complex vector spaces in its notation on p.2.

The literature citations identify the known method; the full proof above is independently supplied and does not rely on inaccessible hypotheses or an unverified computational theorem.

## Completed check events

Model for all rows: GPT-6 Astra Pro (inherited); effort not exposed. Run `GCT_GINEQ/tensor_norms`. Timestamp: 2026-11-20T23:21Z. No formal theorem prover was used.

| ID | Actual event type | Outcome |
|---|---|---|
| F18-original-image-basis | refuted, corrected proof supplied | The proposed pure basis of the flattening image is unjustified; replace the image by the span S_nu of decomposition atoms. |
| F18a | independent re-proof | PASS over C and real Euclidean closure. Reconstructed selection of fixed independent columns, ambient atom span, dimension intersection, normalized compact limit, and border-rank conclusion. |
| F18b | targeted proof check | PASS with b>=2 and a same-field uniform bound on every u. Exponent and ceiling checked against N-01. |
| F18c | independent re-proof | PASS. Derived every coefficient of the contraction matrix, singular-value repetition, exact alpha=1/n, and n^2+n-1 bound over C/R. |
| F18d-real-transfer | refuted, explicit counterexample | Real pencil span{I,J} has alpha_R=1/2 but contains complex rank-one points after scalar extension; complex tensor rank2 contradicts the overbroad real-only inference. |
| F18d-real-Zariski | refuted, explicit counterexample | Same pencil contradicts real-minimum formulation for real Zariski border; full-rank derivative proves the rank2 real locus is Zariski dense. |
| B-border-substitution | used and rechecked in this run | Exact Proposition 2.3 and Lemma 5.2 statements/field read in primary PDFs; related three-factor method identified. |

Independent adversarial cross-check received from `/root/grothendieck_sdp`: the corrected atom-span argument passes over C; fixed q source columns avoid rank-jump trouble, and the real/complex distinction is necessary. That check should be recorded separately under that reviewer's own event if desired.

## Final LaTeX draft whole-proof audit: F-13 and F-14

At 2026-11-20T23:24Z, reviewer `/root/tensor_norms` read the **actual full final-draft statements and proofs** F-13 and F-14 in `deliverable/GCT_GINEQ.tex`, rather than relying only on intermediate notes. Section snapshot SHA-256 (from the start of F-13 through the end of F-14's proof): `bbbf632c5c88a5aaa805dbe21c2c93dfe9dd255d48aefb81c46493a81b5ef9ac`. Model GPT-6 Astra Pro (inherited), effort not exposed, run `GCT_GINEQ/tensor_norms`.

**F-13: PASS.** The proof contains the corrected atom-span argument, keeps fixed q independent columns through possible flattening rank jumps, and uses normalized compact subsequences. Its alpha identity follows from projection duality and exchanging compact maxima. The operator tensor lives in the remaining factors and their conjugates; positivity yields its injective norm equal to alpha. This is compatible with arbitrary complex product inputs. The exponent `1/(b-1)` and ceiling follow from the already checked support bound. Real Euclidean closure is expressly distinguished, and the complex image quantifier is stated. No grouped-rank or symmetric-rank substitution is smuggled into the proof.

**F-14: PASS.** Every displayed alpha and lower bound was independently checked against the final proof:

- Matrix multiplication gives exact alpha `1/n` via the repeated singular values of `I_n tensor X`.
- The alternating projection has product-vector squared norm `det Gram/b!`, so alpha is exactly `1/b!`. The stronger mode operator/Frobenius inequality has the correct `1/b` factor: contraction of a normalized wedge basis vector has coefficient `1/sqrt(b)`. Applying a common unitary to all b factors preserves this alternating subspace, so the bound is complex-uniform and implies minimum residual border rank at least b.
- For row permanent, normalized squarefree basis vectors have `sqrt(b!)` polynomial coefficients, giving `b! e_b(|x_i|^2)` with no missing factorial. Its simplex maximum is the displayed value, attained at constant moduli.
- For symmetric determinant polynomial tensors, every normalized minor tensor has `(b!)^2` nonzero coefficients of modulus `1/b!`, so has Hilbert norm one. Different row/column supports are disjoint. The exterior-power SVD gives the sum of squared minors equal to `e_b` of squared singular values over C, and equality occurs at `I/sqrt(n)`. Thus alpha is `binom(n,b)/n^b`.
- For symmetric permanent polynomial tensors, the larger symmetric row-squarefree subspace gives a valid upper bound, not an unsupported equality. Since the input `X^{tensor b}` is symmetric, projecting to that subspace retains exactly the distinct-row ordered patterns, whose total squared norm is `b! e_b(r_i)`. Hermitian row norms make the argument complex-uniform.
- The strict inequality `b!binom(n,b)/n^b<1` for `b>=2` gives the claimed plus-one bounds, while the determinant polynomial ceiling gives 38 for n=4. All conclusions concern CP border rank and therefore also symmetric border rank when the tensor is symmetric; no Comon-type equality is used.

Two small wording improvements were sent to the author: specify the **same unitary in all b factors** in the alternating proof, and choose **a largest and a smallest coordinate** for the repeated averaging argument. For the latter, if V is the sum of squared deviations from the mean, one averaging step reduces V by half the squared range; since `V<=n*(range)^2`, V contracts by at least the factor `1-1/(2n)`, proving convergence to the constant vector. These clarifications do not alter any formula or conclusion.

| ID | Timestamp | Actual event type | Outcome |
|---|---|---|---|
| F-13-finaldraft | 2026-11-20T23:24Z | targeted proof check | PASS; full finaldraft proof, field quantifiers, conjugate projector factors, and norm exponent checked. |
| F-14-finaldraft | 2026-11-20T23:24Z | targeted proof check | PASS; whole finaldraft proof, all five target image estimates, every factorial and complex/Sym^b step checked. Two wording clarifications recommended. |

**Updated whole-proof check, 2026-11-20T23:35:49Z:** reread the actual complete F-13 and F-14 after the common-unitary and largest/smallest averaging clarifications were integrated. Both **PASS**. The finding-plus-proof hashes are respectively `76d2cc2dbd60a88f25e7a60ecf2f38db0bde0c9f9a0f47504cd5b6cf731003c1` and `121660d8606294bf969ec422b1a18910dc3477bed32c802e9ad89da981169c49`. Actual event type: targeted proof check; same reviewer/model/effort/run. No formula changed and no further gap was found.

# F-23 candidate: recursive border-rank bounds from coordinate restrictions

Author/reviewer: `/root/tensor_norms`, GPT-6 Astra Pro (inherited); effort not exposed. Run `GCT_GINEQ/tensor_norms`. Time: 2026-11-20T23:33Z. This independently proves the parent's simplifying image-restriction lemma and supplies an alternative proof of the geometry agent's QI-01. It is an algebraic refinement using the known border-substitution principle, not a consequence of a full-tensor norm ratio and not a historical-priority or rank-record claim.

## Proposed statement for F-23

Let `2<=b<=n-1` and take complex CP border rank, or real Euclidean CP border rank, consistently throughout. Then

`border R(D_n) >= binom(n,b) + border R(D_b) - 1`,

`border R(P_n) >= binom(n,b) + border R(P_b) - 1`,

`border R(S_det_n) >= binom(n,b)^2 + border R(S_det_b) - 1`,

`border R(S_per_n) >= binom(n,b)^2 + border R(S_per_b) - 1`.

In fact, for the `(n-b)|b` flattening image U in each case,

`min_(0!=u in U) border R(u) = border R(the corresponding b-sized tensor)`.

The residual rank is always ordinary CP border rank in its b ungrouped factors. Since the polynomial tensors are symmetric, the displayed CP lower bounds also hold for their symmetric border rank. One must not replace a smaller tensor's CP border rank by its Waring border rank in these inequalities.

## Complete proof of the exact residual minimum

Use the image descriptions established by F-03. For the row determinant and permanent, the image U is spanned by the b-index coordinate copies of `D_b` and `P_b`, respectively. These basis tensors have pairwise disjoint ordered-coordinate supports. Normalize them, if desired, by their common Hilbert norm `sqrt(b!)`; this nonzero scalar does not affect ranks.

Take any nonzero `u=sum_I c_I Q_I in U`, where Q is either row family, and choose a b-subset `I_0` with `c_(I_0)!=0`. Let `p_(I_0):K^n -> K^b` select the coordinates in I_0 in increasing order. In every monomial of Q_I, all b coordinates in I appear. Therefore

`p_(I_0)^(tensor b)(Q_I)=0` if `I!=I_0`,

while `p_(I_0)^(tensor b)(Q_(I_0))` is `Q_b`, up to the chosen nonzero normalization scalar. Indeed, if `I!=I_0`, equal cardinalities force some coordinate of I outside I_0, so every basis word is killed. Consequently `p_(I_0)^(tensor b)(u)` is a nonzero scalar multiple of Q_b.

For the polynomial determinant and permanent images, the basis consists of the symmetric coefficient tensors Q_(I,J) of all b by b minors/permanents, where I,J are b-subsets of rows and columns. Let `u=sum_(I,J)c_(I,J)Q_(I,J)!=0` and choose a nonzero coefficient at `(I_0,J_0)`. Define `p_(I_0,J_0):Mat_n(K)->Mat_b(K)` by retaining that coordinate block. Every monomial of Q_(I,J) uses every row in I and every column in J. Unless both `I=I_0` and `J=J_0`, at least one required row or column lies outside the retained block. Thus the common projection in all b factors kills every other basis tensor, and

`p_(I_0,J_0)^(tensor b)(u)=c_(I_0,J_0) Q_b`

under the standard polynomial normalization. This coefficient is nonzero.

A product of linear maps cannot increase CP rank: it maps every pure tensor to a pure tensor or zero. It therefore cannot increase CP border rank, by continuity for Euclidean closures, or by the same continuity over C with the equivalent algebraic definition. Nonzero scalar multiplication preserves rank and border rank. These projections prove

`border R(u)>=border R(Q_b)`

for every nonzero image element u, in all four cases.

Conversely, a single basis element Q_I or Q_(I,J) is the image of Q_b under coordinate injections in every factor, up to a nonzero scalar. Those injections have the selected-coordinate projections as left inverses. Applying monotonicity in both directions shows that this basis element has exactly the same border rank as Q_b. Thus the minimum is attained and equals `border R(Q_b)`.

Finally, F-13 gives `border R(Q_n)>=q+min border R(u)-1`. The dimensions q are `binom(n,b)` for the row families and `binom(n,b)^2` for the polynomial families. This proves every displayed recursive bound. QED.

All maps and basis tensors in this proof are real and rational. The proof therefore applies directly to real Euclidean rank/border rank with real residual minima, and independently to the complex versions. It does not use a real-only norm estimate for a complex minimum. The same coordinate-isolation proof establishes the analogous exact image minimum for ordinary CP rank; no such additional rank theorem is needed for the stated border-rank consequence.

## Quadratic consequence, including the n=2 endpoint

The symmetric coefficient tensors of `det_2=ad-bc` and `per_2=ad+bc` are matrices with two invertible 2 by 2 off-diagonal blocks, whose off-diagonal entries are `+/-1/2`. Each has matrix rank, hence CP border rank, exactly 4 over R and C. Therefore, for n>=3, choosing b=2 gives

`border R(S_det_n), border R(S_per_n) >= binom(n,2)^2+3`.

At n=2 the same formula equals 4 and holds by the direct matrix computation, so the consequence can be stated for every n>=2. It gives 12 at n=3, 39 at n=4, and 103 at n=5. These are lower bounds, not exact rank assertions.

For n>=4, the complex theorem `border R(S_det_3)=17` of Conner--Harper--Landsberg (Forum Math. Pi 11:e17, 2023, Theorem 1.2, p.4) also gives

`border R_C(S_det_n)>=binom(n,3)^2+16`.

For example this yields 116 at n=5 and 416 at n=6. The same numerical lower bound holds for real Euclidean border rank by complexification, without asserting that the smaller tensor has real border rank 17. These values should be compared with the central catalecticant and other known bounds rather than presented as uniformly strongest or new records.

## Independent second review of QI-01

Source reviewed completely: `work/agent_quadric_image_candidate.md`, SHA-256 `3a77841b01fae507c93a5b95652a5bae64f87f2df1146762dfc95b524e27b9d7`.

The geometry agent's entire quotient/isotropic-line proof is correct. Each coordinate row/column image is totally isotropic; if the nondegenerate quotient has rank at most three its isotropic subspaces have dimension at most one. Two distinct nonzero entry-image lines force the crossed entries to vanish, and the plus/minus coefficient identity forces those two lines to be mutually orthogonal, contradicting the same dimension bound. The one-generator upper bound is rank four. Every field and polarization factor used there is sound over C.

The coordinate restriction just proved gives a substantially shorter independent reproof. If the coefficient c of one 2 by 2 block is nonzero, restrict the quadratic form to its four matrix-entry variables. All other generators vanish; the restricted form is exactly c times that minor or permanent. Its symmetric coefficient matrix consists of two 2 by 2 off-diagonal blocks with entries `+/-c/2`, so its determinant is `c^4/16!=0`. Hence the whole symmetric coefficient matrix has rank at least four, and a single generator attains four. This independently proves QI-01 without isotropic-space theory.

## Completed check events

All events below: GPT-6 Astra Pro (inherited); effort not exposed; run `GCT_GINEQ/tensor_norms`; 2026-11-20T23:33Z. No formal theorem prover was used.

| ID | Actual type | Outcome |
|---|---|---|
| QI-01 | targeted proof check | PASS; whole quotient/isotropic-line proof checked, including both signs and the nondegenerate quotient. |
| QI-01-coordinate-proof | independent re-proof | PASS; isolated 4-variable coordinate restriction has determinant c^4/16 and proves minimum rank4 directly. |
| F-23-residual-minimum | independent re-proof | PASS; independent coordinate-isolation proof for all four image families, rank monotonicity, scalar normalization, and matching embedded-basis upper bound. |
| F-23-recursion | targeted proof check | PASS; F-13 plus the exact minima gives each displayed recursive inequality with correct q and minus-one shift. |
| F-23-quadratic | targeted proof check | Exact symbolic 4 by 4 determinant evaluated by block algebra as c^4/16; hand algebraic calculation. |

**Executed exact computation, 2026-11-20T23:34:05Z.** The updated `work/check_tensor_decompositions.py` independently expanded the 4 by 4 determinants using all permutation terms with exact `Fraction` arithmetic. Both normalized coefficient matrices (`det_2` and `per_2`) have determinant `1/16`. The same execution reran the earlier exact Strassen, row D3, and rational-margin checks; all passed. Event ID `F-23-quadratic-exact`, actual type **computation or formal certificate** (computation only, not theorem-prover formalization), model and run as above.

The requested main TeX was not edited by this agent. The primary known-method attribution remains Landsberg--Michalek, arXiv:1608.07486, Proposition 2.3, p.3, as in F-13; the restriction argument above is fully supplied, and no historical priority claim is made.

## Actual final-draft F-23 check

At 2026-11-20T23:35:11Z I read the actual complete F-23 statement and proof now in `deliverable/GCT_GINEQ.tex`, including its subsequent recursive numerical examples. **PASS.** The theorem-plus-proof SHA-256 is `7cfa6f0f9d72bc3ad2c75f2f009bb2ff6a605e4a2c3fb1487b0c7aaf80517046`. Actual event type: targeted proof check, same model/effort/run as above. Both same-field minima, all normalizations, split inclusion/projector inequalities, and the n=2 direct case are correct. Its warning against substituting symmetric border rank for CP border rank is essential and correctly included.

Also reopened the primary Conner--Huang--Landsberg paper arXiv:2009.11391v1, *Bad and good news for Strassen's laser method: Border rank of perm_3 and strict submultiplicativity*. **Theorem 1.1 and the immediately following identification, p.3**, give complex ordinary CP border rank of the 3 by 3 permanent polynomial tensor equal to16. Therefore the additional final-draft examples 115 for n=5 and 415 for n=6 are correct. This source theorem is **carried as background without fault found**, not independently reproved; its substantial apolarity computations were not rerun. The field is C, and the numeric lower bounds transfer to real Euclidean border rank by complexification. Combined with the already independently proved 16-term real symmetric upper decomposition, it also confirms symmetric border/Waring rank16 for this small polynomial tensor. This is distinct from row P3, whose rank/border rank is4.

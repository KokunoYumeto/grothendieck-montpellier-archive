# Independent reviewer audit of SDP notes

Reviewer: `/root/tensor_norms`; author being reviewed: `/root/grothendieck_sdp`.
Model: GPT-6 Astra Pro (inherited). Effort setting: not exposed by runtime.
Timestamp: 2026-11-20T23:15Z. Run: `GCT_GINEQ/tensor_norms`.
Source reviewed: the complete statements and proofs of S-01--S-08 in `work/agent_sdp.md`, including the latest S-08 and preceding Banach-space dictionary. This review read each whole proof; it did not merely inspect a conclusion or one line. These are mathematical proof checks, not formal theorem-prover verification. Literature computations elsewhere in the author's notes were not audited here.

## Overall result

All eight proofs pass a full targeted check. Two harmless hypothesis cleanups should be made in final statements: `c` in S-03/S-04 is a positive integer, and the bounded-weight formula S-06 assumes `U,B>0` and `delta>=0`. These conditions are already implicit in their use. No other gap was identified.

## Dictionary preceding S-01

For `A=sum a_ij e_i tensor e_j` in `ell_1^m tensor ell_1^n`, the injective definition maximizes the pairing over the dual `ell_infinity` unit balls; vertices suffice, so it equals Q(A). The operator `ell_infinity^n -> ell_1^m` norm has the same sign maximization. The defined gamma_2 unit ball is exactly the set of cross-Gram matrices of vectors of norms at most one, so its Hilbert--Schmidt dual is S(A). The dual of the `ell_1` injective norm is the `ell_infinity` projective norm in finite dimensions. Polarity of `Q<=S<=KQ` gives `gamma_2<=pi_infinity<=K gamma_2` with the stated direction. The distinction from Hilbert matrix operator/nuclear norms is correctly retained.

## S-01: directional primal/dual certificate

Checked the factor `1/2` in the off-diagonal block matrix: its trace pairing with the symmetric Gram matrix counts both cross blocks, producing exactly the desired objective. Gram realization establishes the primal lower bound. The dual upper bound follows from PSD trace nonnegativity, so no unwarranted strong-duality or rational-optimum assumption is used. `L/K<=Q<=U` has the correct inequality directions, including when `L<0`. The assertion that approximate optimizer values alone are insufficient is correct. **Pass.**

## S-02: Hilbert/cube mismatch

Checked the complex-field point specifically. Grouping complex unit factors gives complex unit vectors, so their tensor contraction is bounded by the complex operator norm of the real flattening matrix; that operator norm equals its real one. Bounding the real operator norm by the sign maximum is then valid. For `Q>=F`, independent sign averaging cancels all mixed second moments. For `S>=nuclear`, thin SVD rows have norm at most one, and adding private coordinates on disjoint left/right supports makes them unit while leaving every cross inner product unchanged. The resulting objective is exactly the sum of singular values. Consequently a witness with `S(flat W)<=1` has matrix nuclear norm at most one, and Hilbert operator/nuclear duality yields the claimed upper limit on its pairing. The full norm-conversion conclusions follow from these inequalities. The projective `ell_infinity` norm example for `I_N` is also valid. **Pass.**

## S-03: arbitrary linear flattening

For a positive integer `c`, rank subadditivity gives `rank Phi(T)<=cr` on CP-rank-at-most-r tensors; `(cr+1)`-minors are polynomial equations, hence extend to the indicated border closure. The three scalar singular-value inequalities are, respectively, Cauchy--Schwarz, bounding each squared singular value by the squared maximum, and bounding each singular value by the maximum. Substitution of lower N / upper U retains their directions. The integer ceiling and the comparison with `ceil(rank M/c)` are sound. Both block-PSD certificates have the correct orientations and dimensions; Schur complement gives the claimed operator bound, and `Re tr(Z* M)` is the correct complex nuclear dual pairing. **Pass, with `c in Z_{>0}` made explicit.**

## S-04: rank-sensitive Grothendieck certificate

Checked the entire two-stage replacement argument. The span of `w_i=sum_j a_ij v_j` has dimension at most the row rank q. Replacing u_i by their aligned vectors in this span preserves the global maximum; the span is nonzero because a nonzero real matrix has positive Q and hence positive S. Replacing the v_j in the same manner keeps every vector in this span and preserves the optimum. Thus the optimum is realized in dimension at most q, including zero individual w_i or z_j. Monotonicity of `K_G(s)` proves the strict-gap implication. Real and complex matrix ranks agree for real coefficient matrices. For a real linear map whose simple-tensor cost is initially proved on real atoms, vanishing of its `(c+1)`-minors as polynomials in real atom coordinates also extends that cost to complex atoms. This justifies the complex border-rank use if needed. The stated limitations of a global K_G or the same basic SDP as Q upper bound are correct. **Pass.**

## S-05: rational CHSH/SOS example

All four vectors are unit and the objective is `3/5+3/5+4/5+4/5=14/5`. Enumeration of the two possible patterns `y_1=+/- y_2` gives Q=2. The rank-sensitive certificate with `K_G(1)=1` proves rank greater than one. Independently expanded the displayed polynomial identity: the first two terms of H_0 give `x_1^2(y_1+y_2)^2+x_2^2(y_1-y_2)^2-2(y_1^2+y_2^2)`; the remaining terms add `2(y_1^2+y_2^2)-4+2x_1x_2(y_1^2-y_2^2)`, hence precisely `f^2-4`. Substitution into `((2-f)^2-H_0)/4` gives `2-f`. Its square coefficient is positive, so this is a legitimate degree-four Boolean SOS certificate. **Pass.**

## S-06: bounded-weight and approximation certificate

Triangle inequality plus nuclear duality gives `|<Z,T'>|<=UrB`; Hilbert Cauchy--Schwarz bounds the approximation contribution by `delta F(Z)`. Rearranging and clipping a negative numerator to zero gives the claimed bound. For the divergence assertion, a bounded subsequence of total normalized weights bounds every coefficient and allows simultaneous subsequences of all finitely many unit atoms. Continuity then gives a rank-at-most-r limiting decomposition, contradicting the stated limiting rank. The same compactness argument works over R and C. **Pass, with `U,B>0` and `delta>=0` explicit.**

## S-07: tensor-power obstruction

The full proof agrees with independently established N-02. It uses the explicit regrouping identity for matrix multiplication tensors and exact independently known norms of each M_n, so it does not assume multiplicativity of grouped nuclear/injective tensor norms. The bound `rank<=7^k` and ratio `8^k` contradict every fixed-constant repair, also for border rank. **Pass.**

## S-08: natural-target signability

Read and checked the entire block/sign argument. Nonnegative matrices attain both Q and S at all-positive/equal choices, and row/column sign switches preserve the two optima. Matrix multiplication and permanents are coefficientwise nonnegative. For a row determinant bipartition, each row tuple identifies a unique support subset S and each column tuple identifies its complement; all nonzero entries lie in disjoint support blocks. The full permutation sign splits as the shuffle sign times the two internal tuple signs, so independent row/column switches are globally compatible. Noncontiguous factor groupings only add a fixed determinant sign.

For the symmetric determinant tensor, each partial matching has a unique pair `(R,C)` and pairs only with complementary matchings. The parity of reordering rows into `R,R^c` is `sum R-k(k+1)/2`, and columns into `C,C^c` has the analogous parity. Their sum is congruent to `sum R+sum C` since `k(k+1)` is even. The reordered permutation is block diagonal. Thus the source's Laplace sign factorization and switches are correct. Ordered-tensor, monomial, orthonormal symmetric and differential catalecticant normalizations contribute only positive factors and cannot alter signability. It follows that Q=S=sum absolute entries exactly, precluding the strict S-04 gap on the claimed natural matrices. No claim is improperly extended to arbitrary preconditioning or Koszul maps. **Pass.**

## Completed check-event table

Every row below is a completed whole-proof targeted check by a reviewer other than the proof's author. Model/effort/run/timestamp are as given above. Calling these checks does not assert independent formalization or independent rerunning of literature computations.

| ID | Actual type | Outcome |
|---|---|---|
| S-dictionary | targeted proof check | PASS; exact coefficient norms and polar directions verified. |
| S-01 | targeted proof check | PASS; SDP normalization and directions checked. |
| S-02 | targeted proof check | PASS; complex-field issue, SVD witness and nuclear obstruction checked. |
| S-03 | targeted proof check | PASS after explicit c positive integer; complete proof and PSD certificates checked. |
| S-04 | targeted proof check | PASS; dimension-q reduction reconstructed in full and zero-vector cases checked. |
| S-05 | targeted proof check | PASS; rational objective and full SOS polynomial identity expanded by hand. |
| S-06 | targeted proof check | PASS after explicit positive U,B and nonnegative delta; compactness argument checked. |
| S-07 | targeted proof check | PASS; compared to independently established N-02 proof. |
| S-08 | targeted proof check | PASS; all target signability cases and basis normalizations checked. |

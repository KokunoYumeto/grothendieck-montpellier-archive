# Independent whole-proof review

Date: 2026-11-21 UTC. Run: ARCH_ALG. Reviewer: GPT-6 Astra Pro, inherited effort not exposed, /root/cote123.

## ARCH-136-ARITH-BOUND — PASS

Reviewed the whole written proof in `work/cote136/arithmetic_improvement.tex`, not only its earlier outline. The following dependencies and ranges were checked.

1. The source maps `(A_i)_K -> B_N(K)` require only acyclicity of the weight-N_i zero-form row, which follows from N_i>=N. No divisibility N|N_i is needed. The coordinate difference of two coefficient-preserving maps factors through Q with normalization K[1]; the target H_1 vanishing gives the required relative simplicial linear homotopy, which extends by the free differential PD presentation.
2. The path endpoint exact sequence becomes surjective once w>=(q+1)N. Its horizontal acyclicity then uses only the maximum M of the local scales. No sum of those scales enters.
3. For vertical cohomology through d, w>=N(d+2) supplies the horizontal bounds of F through d+1. F has exact coefficient vertical cohomology in every weight. AQ-COMPARISON consequently identifies P_sF through d, uniformly in the simplex. The endpoint image agrees with the target through degree d+1, which is the correct range to identify image-complex cohomology through d. The long exact sequence uses no local N_i bound because all A_i have exact vertical cohomology in every weight.
4. The H^0 map is the arithmetic coefficient difference map after eliminating path constants. Sequence136.S1 is valid for arbitrary k-modules, so no flatness of k is silently assumed. The zero rational ring case is harmless.
5. E_J(C) uses finitely many copies of constituents with the same cutoffs. Cardinality of the finite prime set does not enlarge a maximum. Two-edge concatenation is an actual pullback/gluing of sections with exactly matching common vertex, so it preserves every strict operation and coefficients.
6. Iterated AQ-COSPAN produces strict maps to all original targets. At each step its middle object E_J(C_v) has bounds independent of N_i and of the number of primes. The vertical induction therefore preserves the claimed independence, although the horizontal bound retains maxN_i.
7. The final observation about prescribed B_p models correctly prevents extending this construction by simply taking all primes: weights below p retain nonzero horizontal coefficient H_0.

No divergence or unfilled proof step found. The theorem improves finite arithmetic bounds; it does not prove integral connectedness.

## Written ARCH-136-PATHS / FRACTIONS / HOM-SEMILOCAL — PASS

Reviewed all of `work/cote136/homotopy.tex` after the prior independent conceptual review in `work/cote123/peer_review_136_homotopy.md`.

The written version includes the previously required convention: J has at least one edge and two distinct endpoints. Leaf collapse gives linear simplicial cotensor homotopies, and the relative normalized-cell extension argument uses acyclicity including H_0. The uniform vertical cutoff and finite-degree image-complex step match the prior review. The ambient product is used only to form a strict algebraic limit, with no assertion that it is admissible.

The cancellation proof packages the whole zigzag into one P_JZ before forming E. It therefore does not assume intermediate maps factor through u. Right fractions in the quotient category and the all-arrow universal property give precisely criterion136.HF. The final componentwise thinness argument uses the inherited common-source criterion only inside a connected component and then compares finitely many original parallel arrows; that use is valid. No change of meaning from the explicit homotopy reading to strict equalization occurs.

No divergence from the reviewed argument found.

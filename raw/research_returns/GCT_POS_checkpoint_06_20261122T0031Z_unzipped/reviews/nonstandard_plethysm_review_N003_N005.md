# Independent whole-proof review: N-003–N-005

Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro, effort not exposed. Date: 21 November 2026 UTC. Work reviewed: `branches/nonstandard/nonstandard_results.tex`, the complete N-003, N-004 and N-005 arguments; their verifier scripts; the inherited standard Hecke multiplication/KL conversion implementation used by those verifiers; and the supplied counting consult, Theorems 2 and 5.

**Outcome: PASS within the stated scope.** No mathematical gap was found. This is independent mathematical and computational review, not proof-assistant certification. The inherited generic dimension 114 and standard KL facts remain cited inputs. The cited cancellation theorem was checked at its primary statement and abstract, rather than reproved.

## N-003: positive generic basis and proper integral lattice

Read the full construction and distinction between the fraction-field basis, its integral span, and the entire order. Reran `verify_positive_basis.py`: all114 recursive vectors have nonnegative integer Laurent coefficients and are independent at v=2 modulo1000003. Such specialization proves generic independence; combining with the inherited upper bound114 gives a K-basis. Lower-rank intermediate specialization values are correctly qualified as lower bounds, not assumed equalities over K.

The word changes are unipotent over A, so the corrected and uncorrected words span the same free A-lattice. Verified that the first word is the unit, every other initial word is nonempty, all corrections have D-power0, and no donor has index below31. Hence the augmentation statement used in N-004 is justified, including absence of a concealed unit correction.

Reran `lattice_specialization.py` in exact rational arithmetic. Its158th tested product gives the stated unique P1-coordinate −10656875/4608. The specialized114 words remain independent. Since A→Q at v=2 has image Z[1/2], that coordinate, with uncancelled denominator3, rules out membership in the proposed A-lattice. This proves that this lattice is proper; it does not prove nonfreeness of the full order or rule out another positive basis. The manuscript respects both limitations.

The standard-T replay computes KL elements by triangular correction and uses the inherited simultaneous sign involution to convert fixed P-words to dual-KL coordinates. The sign involution fixes P_i and sends C'_w to (−1)^length(w)C_w; hence this conversion applies to the actual elements under review.

## N-004: the all-degree cone/freeness equivalence

The proof uses the positive generic basis only to construct an element z that is positive in every active ambient coordinate. Because the sum has nonnegative coefficients, a coordinate can vanish on z only if it vanishes on the entire K-span. The trivial×sign augmentation sends P_i to0 and z to1, so under freeness the splitting Az⊕ker(epsilon) is valid and the kernel is stably free of rank113.

Checked the primary source: Abedelfatah, *On stably free modules over Laurent polynomial rings*, arXiv:1012.3540v1, Theorem1.3 and abstract, p.1; https://arxiv.org/pdf/1012.3540. It states that a finitely generated stably free module over R[X,X^-1] of rank greater than dim R is free. With R=Z the rank113 application is valid. In particular the argument does not confuse a two-dimensional Laurent ring with a PID or infer freeness from torsion-freeness.

The completion operation b_j+N(sum_{k=-R}^R v^k)z works: every negative Laurent monomial can be covered by a shift of a fixed positive monomial in the same active coordinate; sufficiently large N removes its finite negative coefficients. The added vector is everywhere nonnegative and creates no new negative terms. The elementary column operations preserve an A-basis because z is an actual basis member. This establishes the conditional integral equivalence.

The rational-coefficient corollary is unconditional: Q[v,v^-1] is a PID; the rational order is finitely generated and torsion-free as a submodule of the finite free ambient tensor algebra. Clearing constant rational denominators multiplies basis vectors by units in this PID and places them in the original integral order. This does not assert that the particular bounded-degree lattice equals the rational order.

## N-005: smaller composing dimension rings

Checked the full algebraic proof. The two displayed2×2 matrices satisfy P_i²=DP_i and P_1P_2P_1=Lambda_i P_1, and their four short alternating words are independent because Lambda_i and D²−Lambda_i are nonzero in Q(D). The product of two matrix algebras and the character and augmentation scalar factors has dimension10. The stated map is injective in the given order: augmentation detects the unit, matrix factors detect the eight cell vectors, and the remaining scalar factor detects Sigma.

Recomputed the residual identities:

- G_i(G_i−aD)/S=U_i.
- G_i(DG_i−aLambda_i)/S=V_i.
- G_1G_2/S=W.

Together with |x|+|y|=|z|+alpha+2beta, these give exactly the two scalar cases of N-12 and prove associativity over Q(D). Polynomial entries then imply all associativity identities over Z[D]. No specialization inference is used for this algebraic step.

Rechecked the coefficientwise statements a=|delta_i|+2 and Lambda_2−lambda_2=2(q²+q+q^-1+q^-2), the nonnegative scalar half-differences, and the unimodality logic. Lambda_2 occurs in the cell term only as aLambda_2, so its isolated failure of unimodality causes no missing case. Products of symmetric unimodal nonnegative Laurent polynomials remain so by centered interval decompositions.

Read and reran `verify_dimension_improvements.py`. It matched all132 inherited true constants, verified1000 associativity triples for each new table by two arithmetic methods, and confirmed every coefficient inequality and parity. Scores were7276/6612 (total/bottom) with24 nonunimodal constants for b=−8, and9040/8376 with zero nonunimodal constants for b=−4. These refute the previous window minima as global minima; no new global optimality assertion is made.

Checked the score expression independently: Sigma-gamma terms contribute20(G1+G2), cross-cell terms200W, the same-cell scalar terms20(U1+U2+V1+V2), and the cell terms2a(7Lambda1+13)+2a(7Lambda2+13) at D=4. The absolute true-cell totals152 and176 and scalar total4096 give4424. Thus the displayed score arithmetic follows.

The effective-pair lift is associative because evaluation at epsilon=±1 is injective on Z[q,q^-1,epsilon]/(epsilon²−1), with image equal-parity pairs. The inherited matrix-category realization is used only in its stated abstract sense. It does not identify a Hecke category or a designated canonical basis, and the manuscript preserves this distinction.

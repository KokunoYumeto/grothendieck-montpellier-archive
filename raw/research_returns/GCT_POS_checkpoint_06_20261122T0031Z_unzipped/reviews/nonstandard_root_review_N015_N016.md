# Whole-proof review: N-015 and N-016

- Date: 2026-11-21, 22:14 UTC.
- Reviewer: `/root`, GPT-6 Astra Pro; effort not exposed; GCT_POS.
- Type: targeted proof check (entire proofs), entire independent-arithmetic verifier reading, and exact replay for N-015.
- Outcome: **PASS**, with the scope restrictions below.

## N-015: the actual polynomial order

I read the whole proof in `polynomial_order_rank4.tex` and the whole independent verifier `verify_polynomial_order_rank4.py`. The row operations use Bezout transformations over the PID Q[D], with determinant one, and rational units only. Thus they preserve the actual polynomial word order; they do not replace it by its generic saturation. The 114 nonzero triangular rows are independent. Replaying the complete straight-line certificate puts every row in the actual word order, while the checked identity vector and closure under the three right generators give the reverse inclusion in all word degrees. No assumed generic dimension is needed for that implication.

The root replay completed successfully in 13.78 seconds: all 900 reconstructed operator columns, 342 basis-generator products and 34,026 straight-line nodes passed. The independent arithmetic path reconstructs the opposite KL multiplication from the standard T basis. This is an exact computation replay by a separate reviewer, not a claim of a formally verified proof assistant result. The returned arithmetic receipt itself retains its original same-author description; the present event records the separate whole-proof review and replay.

## N-016: the explicit bar-fixed repair

I read all of `bar_fixed_finite_cutoff.tex`, including the finite quotient, polynomial degree cutoff, partial-order comparison, and full-domain uniqueness sections, and rechecked its use of the previously reviewed N-013 descent. The current stage and its lower bounds are fixed under an explicitly chosen valid label order. The polynomial intersection module is exact; Smith divisibility gives the finite quotient by the primitive rank-one kernel. The quotient dimension bound applies to polynomial images after clearing a common denominator, without claiming that every ambient polynomial belongs to the order.

For a kernel coefficient of degree greater than the stated bound B, its leading term dominates every nonzero ambient coordinate of the finite complement. Replacing it by the normalized primitive kernel vector lowers every such coordinate and preserves all lower constraints. The current exponent is allowed to change; fixing it would invalidate this step. Finite attainable profiles must be compared under the actual source degree comparator, expressed through all linear extensions; taking one arbitrary lexicographic minimum would not suffice. The proof makes this distinction.

N-013 then reduces existence of a global least degree profile to this polynomial search, and the bounded ambient degree box gives finite linear membership and residue conditions for uniqueness in the full bar-fixed domain, including odd-parity perturbations. These are terminating finite procedures, with no polynomial-time claim. Neither successful completion of all 114 stages nor identification with the defective literal VIII order is proved here.

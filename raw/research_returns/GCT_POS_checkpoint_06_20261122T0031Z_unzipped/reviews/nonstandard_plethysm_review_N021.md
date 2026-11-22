# Complete independent targeted proof review of N-021

Date: 2026-11-22. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read the complete `dimension_degree_cutoff.tex`, including the
small-integer-solution proof, symmetric-unimodal variant, global finite
optimization consequence and unary-budget NP statement. No gap found.
This review reconstructs the mathematical proof, not a duplicate replay
of the source-table extraction. The previously certified example scores
and input totals are treated as the explicitly reported inputs.

Coefficientwise domination and parity give exactly b distinguished
extra cancelling-pair occurrences. Their allocation to slots preserves
unit and prescribed zero constraints. Nonnegative coefficients allow
each associativity identity to be expanded into finite monomial multisets
and matched using an existing solution. A matched equation compares
at most two exponents on each side, so its integer row has l1 norm≤4
and constant term of absolute value≤4d0. New solutions of this particular
system preserve all fixed bijections and therefore associativity. The
proof correctly does not claim a universal matching independent of the
initial solution. Bar and label/opposite symmetries use the same method
with no larger constants.

For the compression lemma, the r independent equations and nonsingular
pivot minor H give integer determinant Delta and adjugate entries bounded
by4^(r−1). Reducing each nonpivot coordinate modulo Delta changes it by
a multiple of Delta, so the solved pivot coordinates remain integers.
All other equations are rational combinations with matching right sides
because the original system is consistent. The infinity-norm estimate
is r4^(r−1)(4d0/Delta+4), which is at most r(d0+1)4^r and hence
B(d0+1)4^B. Rank0 and zero-score cases are separately and correctly
handled. Merging several exponent occurrences does not change the score,
since their positive multiplicities still add.

The symmetric-unimodal estimate uses an actual interval of support
[-a,a] with at least1 in each coefficient, giving coefficient sum≥2a+1.
The uniform entry budget M+2B therefore gives the displayed bound for
every table in that class, not just for a compressed replacement.
Unimodality is explicitly not claimed for general compression.

The application arithmetic checks: K(7276,5)=43656·4^7276 has14568
binary digits, and floor((576+2·9040−1)/2)=9327. An already existing
table gives a finite score ceiling; a minimum score exists by well-ordering,
and the replacement theorem supplies some minimizing table in the finite
box. Exhaustive enumeration therefore terminates, without establishing
that the displayed examples are optimal or providing a canonical rule.

For unary-budget NP membership, a witness lists at most B extra pairs,
their slots and signed binary exponents. The exponent bit length is
O(B+log(d0+1)+log(B+1)); log(d0+1) is bounded by sparse input length.
The resulting sparse table has at most the original number of terms
plus B distinct added terms. Associativity can be checked by sparse
products and sums with binary integer coefficients in polynomial time.
The potentially huge monomial-multiset expansion belongs only to the
existence proof, not the verifier. Bar, prescribed slots and the stated
finite label symmetries are also polynomial checks. No NP statement for
binary-encoded B or efficient optimization is asserted.

The proof concerns associative positive integral Laurent dimension tables
on the specified basis. It does not supply a Hecke-category realization,
an E(4) table, a unique minimizing table or a geometrically natural choice.

# Independent concrete-word audit of the Levi scalar evaluator

**Verdict: pass for the requested finite comparison.** The exact polynomial
scalar evaluator `work/calc_levi_scalar_rows.py` agrees at s=2 with a direct
six-letter tensor calculation on all twelve input vectors. This checks its
orientation, derivation-bracket composition and loop-value conventions in
that realization; it does not assert completeness of the selected mixed
equations or an all-genus kernel conclusion.

The independent program is
`work/code_elliptic/check_levi_scalar_word_realization.py`. Its `.out` and
`.json` preserve every output, start time, hashes of the input and tested
scalar output, and elapsed time. It completed with exit zero in
2.298649285 seconds.

The independent implementation expands each nonnegative diagram edge as
the actual tensor `c d - d c + e f - f e`, while the two fixed letters are
`a,b`. Thus the complement W has dimension four, s=2. It reconstructs the
derivation from

`T(D)=a tensor D(b)-b tensor D(a)+c tensor D(d)-d tensor D(c)+e tensor D(f)-f tensor D(e)`

and verifies that reconstruction exactly. It then checks `D(omega)=0`
on the literal symplectic tensor for each of the twelve vectors.

Five complete contractions are evaluated directly on the expanded words,
at the unsigned matching indices 1,2,3,8,14 used by the tested program.
These are compared with its K matrix evaluated at s=2; all sixty entries
agree.

For the mixed comparison, each degree-one Johnson derivation is formed
directly from

`delta_uvw(x)=<x,u>[v,w]+<x,v>[w,u]+<x,w>[u,v]`.

The two derivation compositions are evaluated word by word, and subtracted
to obtain `[D,delta]`. The five contraction terms of the previously
source-checked MSS2026 Proposition 4.1 operator R are then applied to the
actual length-nine tensor. The compared coefficients are c for
`delta_abc`, a for `delta_acd`, and e for `delta_cde`. All thirty-six
entries agree with the corresponding scalar polynomials at s=2.

None of the tested scalar program's loop evaluator, caps, bracket plans,
gluing rules or canonical-edge orientation routine is used in the
independent implementation. The comparison uses the same twelve verified
input tensors and the same primary R formula, which are the intended
common mathematical inputs. No independence or completeness of these
twelve specialized vectors at s=2 is needed for this sign check.

## Extension to the four selected ES scalar rows

The separate revised certificate
`work/code_elliptic/check_levi_scalar_word_realization_es.py` completed with
exit zero in 5.293699090 seconds. The original R/K-only program and its
2.298649285-second record remain unchanged. The revised `.out` and `.json`
record all twelve rows and all input hashes.

It computes the actual ES7 element by the first-two-slot contraction of
the length-nine special tensor, followed by cyclic word coinvariants.
For each seven-letter cyclic word it sums all seven rotations. It then
contracts the first six slots by matching index 1 or 2, respectively
`((0,1),(2,4),(3,5))` and `((0,1),(2,5),(3,4))`, and pairs the last letter
with the specified dual. The four tests are delta_abc with dual d and both
matchings; delta_acd with dual b and matching 1; and delta_cde with dual f
and matching 1. All 48 entries agree exactly at s=2 with the four selected
polynomial rows in `calc_levi_selected_identity.pickle`. All previous 60 K
and 36 R entries were rechecked in that run as well. This verifies the new
ES sign and contraction convention independently of the diagram plans;
it does not assert the symbolic row-space identity.

## Independent polynomial row-space identity

The additional certificate `check_levi_selected_polynomial_identity.py`
uses the retained exact seven-row M, five-row K, quotient L, numerator N
and denominator d. It verifies all 36 entries of `N M-d L K` as zero
polynomials in Q[s], and checks `ker L=image J` by both ranks and `LJ=0`.
The asserted denominator factorization is checked exactly. Its nonconstant
factors are positive for s>=3; the final quadratic `4s^2+6s-1` is at least
53 there. Therefore d is nonzero at every integer s>=3. The selected
seven-column minor at s=3 is 274545313514835148800. The calculation
completed with exit zero in 4.818296838 seconds; its separate `.out` and
`.json` preserve inputs, hashes and start time.

This proves the exact row-space implication from the supplied polynomial
rows for every integer s>=3. It does not replace the geometric proof that
the chosen rows are necessary on the actual arithmetic image or the
rational invariant-functional map to q6. Those maps are treated in the
separate all-genus argument.

# Whole-proof review: K-018

- Date: 2026-11-21, 21:59 UTC.
- Reviewer: `/root`, GPT-6 Astra Pro; effort not exposed; run GCT_POS.
- Type: targeted proof check, entire proof read; independent exact computation.
- Outcome: **PASS** for the stated diagonal-character and polystability theorem.

I read all of `branches/kronecker/AMPLIFYING_GADGET.tex`, including the exact gadget, positive interval, insertion operation, determinant multiplication, denominator recurrence, character-lattice identification, intermediate dimensions and critical-point argument.

The crucial determinant step is valid. In an old maximal incidence minor with the second and third boundary rows omitted, the removed edge column is the unit column at the first boundary row. After gluing, the old rows other than this boundary row see no gadget columns. The resulting square matrix is block lower triangular. Its two diagonal determinants are the old determinant (up to sign by expansion of that unit column) and the gadget determinant. The primitive left kernel gives equal absolute nonzero maximal incidence minors, so the displayed determinant is the index in the saturated column lattice.

For independent columns, the equation `A q = 1` has a unique rational solution. The order of the determinant-product character in `Z^(3n)/im(A)` is exactly the least positive integer making `q` integral. The selected mass has odd numerator and denominator `2*256^k`, by the recurrence `(131 D - 43 a)/(256 D)`. All other denominators divide the same number. Equality with the torsion order proves cyclicity and faithfulness. A diagonal torus factor splits over the complex numbers; the splitting need not be canonical.

The positive interval and invariant interval prove positivity for every insertion. Freeness is preserved because any old/new edge pair agreeing in two coordinates would agree with the deleted boundary edge in that pair, which old freeness excludes. Margin-one positive square-root coefficients have identity reduced Hermitian matrices, so the established Kempf–Ness criterion applies.

The separate verifier `branches/root/verify_amplifying_gadget.py` was written without importing the search or branch verifier. It reconstructs all incidence matrices from the JSON lists and checks: exact affine margin identities; determinant256; interval endpoints and invariant interval; n=9 positivity, all27 margins, determinant512, primitive determinant exponent219, all729 possible fixed coordinates, and full Lie rank241 modulo10007. It independently constructs four iterations in dimensions9,16,23,30 and checks exact mass denominators, positivity, freeness and incidence rank. These finite induction checks supplement the proof rather than replacing it.

Scope: this refutes the proposed universal `2^(n-1)` bound. It proves no global Hilbert-series pole or positivity/saturation-index bound. Full n=9 stabilizer analysis is a separate K-019 statement. No priority claim is made pending the transportation-polytope literature audit.

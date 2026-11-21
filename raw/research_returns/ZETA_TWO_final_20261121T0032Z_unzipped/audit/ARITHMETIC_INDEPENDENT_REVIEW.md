# Independent review of IA02, IA03, IA07, IA08, IA09

**Outcome: all five complete new proofs pass. No mathematical correction is requested.**

Reviewer: `/root/masullo_cm`, GPT-6 Astra Pro; reasoning effort not exposed.
Date: 21 November 2026, Europe/Berlin.
Reviewed `work/intake_section.tex`, SHA-256
`c9a0dab3b5ae24e08d322f456ab982e6222ea852498a072525b7040bb5a2466a`.
The review read each assigned statement and its entire proof, independently
reconstructed the calculations and transfers, checked the specified literature
inputs below, and executed the inspected arithmetic script. It is not a formal
verification or an independent proof of the cited literature theorems.

## IA02: constants, thresholds, and class numbers — PASS

The definitions of U and V agree term by term with Lamzouri–Li–Soundararajan,
arXiv:1309.3595v3, Theorem 1.5, pp. 3–4. In particular, the reciprocal bound
has coefficient 12 exp(gamma)/pi^2 and the extra term
14 log(log(q))/log(q); both bounds require q at least 10^10. The quadratic
class-number formula multiplies the bounds by sqrt(D)/pi, giving exactly the
displayed lower coefficient pi/(12 exp(gamma)). The discriminant threshold
excludes the exceptional unit counts at discriminants -3 and -4.

Corollary 1.1, p. 2, covers all primes p at least 5 and gives a strict bound
for the least quadratic non-residue. The elementary argument that the least
positive non-residue is prime is valid. Corollary 1.2, p. 3, has exactly q > 3
and gcd(a,q)=1 and gives the displayed weak inequality for the least prime in
the progression. No silent extension of the conductor threshold occurs.

For the abelian-field extension, the residue of zeta_K at 1 is the product of
the nontrivial primitive Dirichlet values, while the analytic class-number
formula has factor 2^r1 (2 pi)^r2/(w_K sqrt(|D_K|)). Taking absolute values
therefore gives exactly the stated product inequalities. The warning that
this bounds h_K R_K, with regulator control still needed for a class-number
upper bound, is mathematically correct.

## IA03: rational versus geometric supersingular counts — PASS

Delfs–Galbraith, arXiv:1310.7789, equation (1), p. 2, states precisely the
three values c_p h(-D_p) used here for the number of supersingular
j-invariants in F_p. Each displayed negative discriminant is fundamental:
-4p when p = 1 mod 4, and -p when p = 3 mod 4. Multiplication of IA02 by
c_p gives the claimed inequalities, with threshold D_p rather than p.

The geometric total in F_(p^2) is instead floor(p/12) plus 0,1,1,2 in the
classes 1,5,7,11 mod 12, as displayed on p. 1 of that same paper. The text
keeps these different counts separate. The unknown ring R in the unattached
A.8c proof remains an explicit source gate; the conditional quadratic-order
transfer made here is valid and does not claim a quaternion class-number
formula.

## IA07: cyclotomic determinant and reduced K_0 — PASS

The residues of powers of 5 run through all nonzero classes mod 23, with
5^11 = -1. Thus odd characters are exactly the evaluations at the eleven
distinct roots of x^11+1. Reducing S modulo this polynomial gives precisely
the eleven coefficients displayed in the statement. Multiplication by T is
diagonalizable over C with eigenvalues T(z) for these roots z, so its
determinant is the product of those evaluations. This fixes the sign without
a resultant-order convention.

The fully inspected `intake_compute.py` was run successfully. Its custom
integer Bareiss elimination and independent SymPy Berkowitz determinant both
give -127262242448329728 = -3072*23^10. The eleven factors -1/23 in the
formula for L(0,chi) give the positive product 3072/23. Multiplication by
46/2^11 then gives h-minus = 3. These are exact rational/integer operations;
the unrelated gamma/logarithm decimals in the output remain numerical
evaluations, not interval certificates.

The relative class-number formula is the one displayed in Thakur, p. 172,
with the cited Washington Theorem 4.17 locator. Miller Theorem 1.1, p. 1,
states unconditionally that the real subfield has class number one for prime
conductor at most 151. Hence h-plus = 1 for conductor 23 and the total class
number is 3. The proof does not mistake the relative calculation for a
calculation of the plus part.

The reduced K_0 identification is consistent with the full ideal class
group, not merely its minus part. Ullom p. 159 cites precisely Rim Theorem
6.24, p. 711, for the projective class group of Z[C_p]; Siviero Lemma 4.5,
equation (16), printed p. 82, states the isomorphism of the locally free
class group with Cl(Z[zeta_p]). As an independent type check, the standard
Milnor pullback square Z[C_p] = Z times_(F_p) Z[zeta_p] has the units
(1-zeta_p^a)/(1-zeta_p) mapping onto all a in F_p^*. Its K-theory exact
sequence therefore gives K_0(Z[C_p]) = Z direct-sum Cl(Z[zeta_p]), hence the
claimed reduced group. The subsequent topological application is correctly
kept separate from this arithmetic and K-theoretic calculation.

The original Rim article could not be read: its JSTOR landing page returned
no article text and its PDF failed retrieval. The original Washington book
was not opened. These two original results remain known background, with
their relevant formulations and locators checked through the specified
scholarly sources. No original-source full-proof check is claimed.

## IA08: the quadratic value and unit — PASS

The finite weighted cosine expansion gives sqrt(5) L(1,chi_5) after Abel
limiting, because the quadratic Gauss sum is sqrt(5). Pairing a with 5-a
gives (2/sqrt(5)) log(sin(2pi/5)/sin(pi/5)); the sine ratio is phi. Thus the
displayed L-value has the correct sign and factor 2. The identity
phi^4 = (7+3sqrt(5))/2 and its numerical value were reproduced. The proof
does not infer a Whitehead-group generator from an absolute value or from
the L-value bound and explicitly preserves the intake's existing verdict.

## IA09: exact second moment and refutation — PASS

Independently summing the Abel-limit sine identity against bar(chi) gives
the absolute-value formula with coefficient pi^2/p^3; the modulus of the
Gauss sum contributes exactly p. Projection onto odd characters gives
(p-1)/2 times the difference of the conditions a=b and a=-b. Dividing by
the number (p-1)/2 of odd characters cancels that factor. Finally,

    2 sum_{a=1}^{p-1} a^2 - p sum_{a=1}^{p-1} a
      = p(p-1)(p-2)/6.

The average squared L-value is therefore exactly
pi^2(p-1)(p-2)/(6p^2), strictly less than pi^2/6, also at p=3.
At least one odd character realizes at most this average. Odd characters
are nonprincipal; nonprincipal characters of prime modulus are primitive.
Infinitely many unbounded prime conductors then contradict a positive
uniform lower bound c log(log(p)) for all primitive characters. No GRH
input is used. The argument is a family refutation, not just a small-modulus
counterexample.

## Source retrieval record

- LLS v3: https://arxiv.org/pdf/1309.3595v3 — `turn110513985view0`,
  `turn374010243view0`; exact theorem/corollary statements checked.
- Delfs–Galbraith: https://arxiv.org/pdf/1310.7789 —
  `turn110513985view1`; pp. 1–2 checked.
- Miller: https://arxiv.org/pdf/1407.2373 — `turn110513985view2`;
  Theorem 1.1's unconditional clause checked, not its later GRH clause.
- Thakur: https://people.math.rochester.edu/faculty/dthakur2/BPCyclotomic.pdf
  — `turn907668347search0` retrieves the exact p. 172 formula and locator;
  direct opening of the PDF failed during this independent review.
- Siviero: https://www.numdam.org/item/10.5802/pmb.13.pdf —
  `turn379711497view1`, `turn484321444view0`; Lemma 4.5, equation (16),
  printed p. 82 checked.
- Ullom: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDAF1160D7312AB5A5E2D32BA8B540FF/S0027763000024521a.pdf/normal-bases-in-galois-extensions-of-number-fields.pdf
  — `turn379711497view2`, `turn484321444view1`; printed p. 159 checked.
- Rim original: https://www.jstor.org/stable/1970033 —
  `turn784435642view0` (landing page without article text),
  `turn784435642view1` (failed PDF retrieval); no original theorem reading.

Computation source SHA-256:
`2650c7f1b28d4f83f1fa47c7f521abb40403795c66b7dceea24a704045d144ec`.
Reproduced output SHA-256:
`b0aadae5e6d30a17357306f1ffcef52010ab72bef5972a29bb520828099774bb`.

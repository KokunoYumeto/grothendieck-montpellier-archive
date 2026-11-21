# C15-MILNE-SIGN: a missing sign in the primitive pairing

Author/checker: GPT-6 Astra Pro, inherited reasoning effort not separately exposed, GHOSTS run `/root/cm_transport`, 21 November 2026.

## Exact source and observation

The supplied J. S. Milne report, *On the Hodge, Tate, and standard conjectures for abelian varieties*, Hexagon2611.00244v1, section3.6, printed and PDF p.8, defines the primitive subspace

    P^r(A) = ker(L^(g-2r+1): A^r(A) -> A^(g-r+1)(A))

and calls the pairing

    (a,b) -> a b xi^(g-2r)

positive definite. Here xi is the polarization class and L is multiplication by xi. The original supplied PDF was rendered and visually inspected, including a fresh inspection during the final audit. The factor (-1)^r is absent from the displayed formula; this is not an OCR omission.

## Complete counterexample to the unsigned display

Let E be an elliptic curve over C and put A=E x E. Let theta_1 and theta_2 be the pullbacks of the origin divisor from the two factors. Intersection theory on the product gives

    theta_1^2 = theta_2^2 = 0,     theta_1 theta_2 = 1.

Indeed, the square of a divisor pulled back from a curve is zero, while the two coordinate divisors meet transversely at the origin. Their sum xi=theta_1+theta_2 is the product principal polarization. Put a=theta_1-theta_2. This is a nonzero rational algebraic divisor class: for example a theta_1=-1. Since g=2 and r=1, primitivity means a xi=0, and

    a xi = theta_1^2-theta_2^2 = 0.

Nevertheless

    a^2 = theta_1^2-2 theta_1 theta_2+theta_2^2 = -2.

Thus the displayed unsigned form is negative on a nonzero primitive algebraic class, and cannot be positive definite as written. This elementary example refutes precisely the unsigned formula, not the report's standard-conjecture theorem.

## Correct formula and normalization

With the usual cycle-class and intersection normalization, the positive primitive form is

    (a,b) -> (-1)^r a b xi^(g-2r).

The sign is the usual Hodge-Riemann sign in degree k=2r and Hodge type (r,r): the type factor i^(r-r) is1, and

    (-1)^(k(k-1)/2) = (-1)^(r(2r-1)) = (-1)^r.

Any normalization by a factorial or a positive power of the polarization volume changes only a positive scalar and does not remove the required sign. In the explicit example the corrected value is (-1)(-2)=2.

The same sign is directly visible in Grothendieck's Serre letter of27 August1965, Montpellier cote14, one-based PDF scan45 / archive folio44: for n=2m its primitive positivity statement uses (-1)^m E(xx'). This is a corroborating source reading, not a claim that the archive proves the theorem used by the report.

## Consequences for this package

* The report's qualitative standard-conjecture consequence is retained as the supplied theorem input; no contradiction to that theorem is claimed.
* Codimension two has positive sign. The fourfold Weil-plane square, the t_star/t_0 calculations, and R10–R12 are unaffected.
* Codimension three has negative sign. R21 and R23 already use the positive norm -integral(tau^2), and the contraction identity -Gamma^2=t^2. The sixfold calculation therefore uses the corrected convention throughout.
* This finding supplies no effectivity or degree estimate for arbitrary cycles. Positivity on primitive cohomological classes is not positivity of an effective-cycle transport operation.
* This is a correction to a supplied mathematical source, not a Grothendieck transcription correction. It must not be entered into `TRANSCRIPTION_NOTES.tsv`.

## Actual check record

`C15-MILNE-SIGN-FULL`,21 November2026, GPT-6 Astra Pro, inherited effort not exposed, `/root/cm_transport`: targeted complete proof check. Read the precise definition and unsigned display on source p.8, visually verified the missing sign, independently proved the E x E counterexample and the sign parity, and checked its use in the final fourfold/sixfold formulas. No formal verification or whole-paper re-proof is claimed.

# Independent whole review: genus-six trace detector

Reviewer: /root/lean_chain, GPT-6 Astra Pro; effort not exposed.

**PASS**, for the complete proof in main_gate/senary_trace_detector.tex,
SHA-256 c20b80e57588b9fb0e62c82f7e6c7fabcbe279f3375e8f628fb6809fb962b5b2.
This is an exact trace identity and a nonimplication example. It supplies
no unit trace, auxiliary-field existence theorem, or new arithmetic
vanishing conclusion.

## Coefficient normalization

Kohnen's author notes define the Eisenstein series on printed p. 14 as
the Siegel parabolic coset sum, with constant coefficient one. The entire
definitions of the signed discriminant, fundamental part, square factor,
and φ(a;T) on pp. 20–21 were read, together with Theorem 21 on p. 22.
The theorem's displayed numerator was also visually checked: it is 2^n.
Here k=(p+9)/2 is even and greater than seven. With n=3 and
det(2T)=|D| fundamental, f_T=1; φ(1;T)=1 follows directly from the
single unimodular coset in its definition. Multiplication by the stated
κ_k therefore gives exactly −β_b(χ_D), without an additional power
of two.

The coefficient theorem is imported. Its full earlier lifting proof is
not reconstructed or claimed checked.

## Genus and full orthogonal mass

Ibukiyama–Williams printed p. 23 gives the specified local genus, its
existence, determinant, and the definition of mass using the full
orthogonal groups. This is the mass needed in the trace; the special
orthogonal mass would differ by two. The complete Proposition 12 proof
on pp. 24–26 was read. Pages 24 and 25 were additionally inspected as
rendered PDF images.

The statement on p. 24 prints 3², but the conclusions of the proof print
3³. The calculation in the new section is internally complete:

1. At odd unramified primes the factor is
   (1−q^−2)(1−q^−4)(1−χ_D(q)q^−3).
2. At each q dividing d, the additional multiplier relative to the
   corresponding Euler factor is 2q.
3. The stated 2-adic local parameters P and E give an additional 2^6
   relative to the usual Euler factor.
4. Thus the inverse local product is ζ(2)ζ(4)L(3,χ_D)/(2^(t+6)d).
5. Combining it with 3d^(7/2)/(2π^9), and the correctly normalized
   odd quadratic functional equation
   d^(5/2)L(3,χ_D)/π^3 = 2B_(3,χ_D)/3, gives
   B_(3,χ_D)/(2^(t−1)·2^9·3^3·5).

This equals β_3(χ_D)/(2^(t−1)23040), as used. The recomputation also
keeps the π-powers in intermediate formulas; it does not rely on the
typographically damaged intermediate displays in the author PDF.

## Integral statements and limits

For p≥31, a finite subgroup of GL_6(Z) has order prime to p: an element
of order p would require a nontrivial rational constituent of dimension
at least p−1. The Bernoulli-polynomial expression is p-integral for
the indices 3 and b≤p−2 with p prime to d. Consequently each trace
summand is p-integral, and the trace is a unit exactly when both
Bernoulli quotients are units.

The three ordinary Bernoulli quotients in κ_k reduce by Kummer to
B_8/8=−1/240, B_6/6=1/252, and B_4/4=−1/120. They are units for
the stated primes. Since k<p−1, the claim κ_k/B_k is a p-unit follows.
The cited small-discriminant class bound actually applies for p≥29,
so its use here with d<4p and p≥31 is within scope.

For the previously certified p=31, D=−79 example, the exact mass is
992/23040=31/720. The common individual coefficient is a unit,
whereas the trace is zero modulo 31. This is actual cancellation in
the specified Eisenstein series and does not depend on a hypothetical
choice of coefficients.

The final analytic non-saturation lemma is correct: every nonzero
coefficient of p(1−p^(−s))ζ(s) is divisible by p, while the residue
at s=1 is p−1. It establishes only that an analytic residue alone
does not supply an integral coefficient detector.

## Primary provenance

- Kohnen, A short course on Siegel modular forms, author-hosted
  https://www.mathi.uni-heidelberg.de/~winfried/siegel2.pdf .
  PDF SHA-256 90b782aaac2da538eb4888bb134157b5dc5cdc5e80a6a551b690743d431d2153.
  Scope read: p. 14 Eisenstein definition and convergence range;
  pp. 20–22 definitions and complete Theorem 21 statement.
- Ibukiyama–Williams, Hermitian modular forms and algebraic modular forms
  on SO(6), author-hosted https://btw-47.github.io/hermitian_orthogonal.pdf .
  PDF SHA-256 351a1018f0cc0cfb04ebf702d41a767f617b604536647368f86989b6bfe98f9c.
  Scope read: p. 23 genus existence, full-O versus SO definitions and
  Lemma 10 proof, Minkowski–Siegel formula; complete Proposition 12
  and proof, pp. 24–26. The general mass and local density theorems
  cited by the authors are imported, not re-proved here.

Rendered primary pages are retained in lean_chain/senary_primary_pages.
No new Lean kernel build or new arithmetic certificate run is claimed.

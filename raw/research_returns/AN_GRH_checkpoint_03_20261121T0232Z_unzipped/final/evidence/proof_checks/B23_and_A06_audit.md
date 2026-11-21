# Independent audit of the explicit theta obstruction

**Date:** 2026-11-21. **Checker:** GPT-6 Astra Pro, `/root/effective_galois`; reasoning effort not exposed.

**Proof-check result:** PASS for the recovered A1-run B.23 argument and the parent’s shorter A06 proof, with the exact scopes distinguished below. This is a targeted mathematical proof check with exact computational replay, not formal verification.

## Sources and artifacts actually read

- The full B.23 statement and proof in `recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`.
- The entire cleaned `work/root/b23_section.tex`, including the scope paragraph.
- `work/root/check_b23_geometry.py`, read in full and executed successfully.
- The retained `work/row_audit/B23_recheck/primitive_conductors.py`, `primitive_191_229.py`, and `primitive_verify.py`, their retained output logs, the full merged manifest, and the decoded-identity verifier replay.
- A separately written standard-library arithmetic check, `work/effective_galois/check_a06_prime_orbit.py`, executed successfully. Its primality and order calculations use trial division and successive powers, independently of the retained conductor-reduction algorithm.

## 1. The finite field and the curve

For

M(Z) = Z^38 + Z^14 + Z^10 + Z^9 + Z^8 + Z^5 + Z^2 + Z + 1,

the three Rabin conditions used in the source are sufficient: Z^(2^38) is Z modulo M, and the gcds with Z^(2^2)-Z and Z^(2^19)-Z are one. The prime divisors of the degree 38 are precisely 2 and 19, so the exponents 19 and 2 are the required proper divisor exponents. The exact binary-polynomial implementation of these checks was read and replayed.

The field therefore has 2^38 elements. Its generator t cannot satisfy t^3 = 1, so d = t^3 + 1 is nonzero. The curve is the smooth proper model of

y² + y = A(u)³, with A(u) = (u²+t²u+t)/d.

Expanding A(u)³ gives nonzero u^5 coefficient t²/d³ and leading u^6 term. Artin–Schreier changes remove even powers without changing that u^5 coefficient: removing u^6 can introduce only a u^3 term. The reduced polynomial has a single pole of odd order five. Consequently the unique point P at infinity is rational, the different exponent is six, and the canonical divisor of du is 2P; Riemann–Hurwitz gives genus two.

The regular differentials du and u du form a basis. Cartier maps the first to zero and the second to du, so its stable rank is zero. Thus the Jacobian has no nonzero geometric 2-primary torsion points. This can alternatively be deduced from the scalar Frobenius calculation below: Frobenius is bijective on algebraic-closure points whereas multiplication by 2^19 would kill such points.

## 2. The elliptic maps and exact scalar Frobenius

Set B(u) = (t u²+u+t²)/d. The displayed cubic identity was checked exactly in the stated field. It proves that

(A(u),y) and (B(u), y+(u³+1)/d)

are maps to E: y²+y=x³. They extend to the smooth proper curve and both take P to the origin. Their joint map is birational onto its image because u = B+tA and y is the first y-coordinate. Therefore that image has normalization of genus two and cannot be contained in a translate of an elliptic subvariety of E². The induced homomorphism J_C to E² has two-dimensional image and is an isogeny.

For this elliptic equation, inversion is (x,y) to (x,y+1), and the tangent formula gives [2](x,y) = (x^4,y^4+1). Therefore fourth-power Frobenius equals [-2]. Raising to the nineteenth power shows that k-Frobenius on E² is [-2^19]. The same equality holds on J_C: composing the difference with the k-isogeny gives zero, and a homomorphism from an abelian variety whose image lies in a finite kernel is zero. No assertion that the unspecified isogeny induces an integral torsion-module isomorphism is needed.

## 3. The locally exact differential theta divisor

In characteristic two the cokernel B of O_C to F_*O_C is a line bundle whose square is the canonical bundle. The local calculation is sufficient: with a change of parameter v = a²+u b², the quotient generator changes by b and dv = b² du. This may be stated with absolute Frobenius, so the line bundle is on C. With relative Frobenius the target is the Frobenius twist; the same construction and scalar-Frobenius argument apply to that twist.

There is a unique geometric theta characteristic, since J_C[2] has one geometric point. As K_C is 2P, it is O(P). The theta condition h0(O(P) tensor L) > 0 therefore says L = O(R-P) for a point R of C. Thus theta is precisely the Abel curve C-P. It contains zero, is defined over k, and is symmetric because R+ιR is linearly equivalent to 2P.

For any nonzero Jacobian difference, at most two ordered pairs of theta points represent it. Equality R1-S1 = R2-S2 gives R1+S2 linearly equivalent to R2+S1. If the divisors coincide, the representations coincide (the excluded zero difference handles the alternative matching). Otherwise this is the unique degree-two hyperelliptic pencil, forcing (R2,S2) = (ιS1,ιR1). This argument controls geometric point pairs, including characteristic two; it does not rely on a reduced intersection scheme or on transversality.

## 4. The shorter A06 obstruction

Suppose a nonzero theta point L has prime order ell and 2 is primitive modulo ell. Since theta is stable under scalar Frobenius -2^19 and under negation, it contains the orbit H L for H = <2^19> in the multiplicative group modulo ell, together with zero.

Put e = gcd(ell-1,19) and m = (ell-1)/e. The orbit has m distinct points. Its m(m+1) ordered nonzero differences lie in a cyclic group with ell-1 nonzero elements, each admitting at most two representations. Thus m(m+1) ≤ 2(ell-1).

For e = 1 this would force ell ≤ 2. For e = 19 it forces m ≤ 37 and ell ≤ 704. Since ell is odd, m is even. Trial division of the eighteen candidates 19m+1 with m = 2,4,...,36 leaves

| ell | 191 | 229 | 419 | 457 | 571 | 647 |
|---|---:|---:|---:|---:|---:|---:|
| order of 2 | 95 | 76 | 418 | 76 | 114 | 323 |

Only 419 remains. The generator 2^19 modulo 419 is 119, of order 22. The pairs

(1,418), (71,69), (350,348)

are distinct pairs in that orbit and all have difference 2. Their displayed exponent witnesses in the cleaned paper were also checked: (g^0,g^11), (g^19,g^20), and (g^9,g^8), respectively. This contradicts the two-representation bound.

The independently written checker confirms all prime candidates, all six orders, the full 22-element orbit, and exactly these three difference-two pairs. Hence the universal primitive-root theta condition is false for this explicit curve over the algebraic closure. This is stronger than observing a gap in a density inference. It is not a counterexample to point-section injectivity, and does not disprove a separately formulated theorem restricted to positive-two-rank curves.

## 5. Audit of the stronger B.23 finite cutoff

For an arbitrary odd conductor n, let f = ord_n(2) and e = gcd(f,19). A cyclic cover with zero primitive two-rank must meet theta in every multiplication-by-two orbit of primitive indices. Each such theta point brings its entire 2^19 orbit into theta. Those orbits have length f/e, while the number of primitive 2-orbits is phi(n)/f. Thus at least M_n = phi(n)/e distinct primitive theta points are forced, in addition to zero.

The same difference count gives M_n(M_n+1) ≤ 2(n-1). For odd n, the multiplicative prime-power estimate phi(n) ≥ (2/3)n^(5/6) is valid. For a prime at least five, (ell-1)^6 ≥ ell^5; higher prime powers improve the ratio. The possible factor at three also satisfies the stated weaker constant. Combining the inequalities yields

n < (9/2)^(3/2) 19³ < 10·19³ = 68590.

The strict cutoff in the program, all odd n from three through 68589, is therefore complete. It gives the thirteen listed conductors. The single-packet test correctly imposes all ordered-difference multiplicities on {0} union H, where H = <2^19,-1>. It leaves 191, 229, 457, and 1257.

For 457, zero primitive two-rank requires a packet in each of six cosets of U = <2,-1>. Changing the cyclic generator normalizes one chosen packet to H. Each of the remaining cosets has nineteen possible H-packets. The depth-first search enumerates every possibility after a monotone necessary pairwise filter, accumulates both internal and cross-packet ordered differences, and rejects exactly when a count exceeds two. The retained levels 1,17,226,879,262,0 therefore prove nonexistence; no transition or branching choice was omitted.

For 1257, the two required U-cosets give disjoint packets of size 22, each with eleven elements in each nonzero residue class modulo three. Their union has residue occupancies (1,22,22), including zero. Hence 924 ordered distinct differences are divisible by three, whereas only 418 nonzero residues divisible by three exist and each permits two representations, giving capacity 836. This excludes the conductor independently of the large polynomial calculations.

## 6. The retained polynomial certificates

The chord-and-tangent recurrence for the rational x-coordinate is valid in characteristic two. For distinct generic P,Q on E, x(P+Q)+x(P-Q) = (x(P)+x(Q))^(-2). With P=[m]R and Q=[m+1]R this gives the stated odd recurrence; the duplication formula gives the even recurrence.

The separately computed reduced rational functions for n=191 and n=229 have coprime numerator and denominator, with the denominator exactly the square of the displayed psi_n. This was replayed by `check_b23_geometry.py`. Thus zeros of psi_n are precisely the finite x-coordinates of nonzero n-torsion; correctness does not depend on applying a division-polynomial formula outside its characteristic hypotheses.

The retained verifier reads all coefficient arrays, checks their SHA-256 hashes, their finite-field encodings, and degrees; reconstructs the two compositions psi_n(A), psi_n(B); and checks the whole Bezout identity. These checks establish the polynomial identities, rather than a random evaluation or a checksum alone.

If a finite point R of C had a nonzero Abel class killed by either remaining conductor, both its elliptic images would be n-torsion. Their x-coordinates are finite because A and B have no finite poles, so neither image is the origin. They would give a common zero of the two composed polynomials, contradicting the identity. P at infinity gives the zero Abel class, which is not primitive. This is the exact geometric implication of the certificates.

The computational replay status and outputs are recorded separately in CHECK_EVENTS.tsv and the retained logs. The proof of the shorter A06 assertion does not depend on these large Bezout certificates.

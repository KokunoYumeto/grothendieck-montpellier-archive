# Independent whole-proof review: P-F28 and P-F31

Reviewer: GPT-6 Astra Pro, inherited/undisclosed effort, `/root/bridges`.
Completed: 2026-11-21 01:33:59 UTC.
Files read in full: `positivity_chain_residue.tex`, `positivity_actual_cubic_pole.tex`; P-F23 was also reread in full for this application.
Outcome: **PASS** for both complete proofs.

## P-F28: exact multiplicity and valuation

The grading stabilizer is exactly the image of the chain's full linear stabilizer, not merely a subgroup of it. The converse follows by choosing a matrix with the prescribed determinant character and correcting it by an SL_n element using uniqueness of the closed orbit in a quotient fiber. The image has order M, including the case 3 divides n.

The reduced chain orbit closure has coordinate ring C[u^d:d in S], where S is the support of evaluations at the chain point. Finite generation and a nonzero discriminant give a nontrivial finitely generated semigroup. The stabilizer calculation gives gcd(S)=M. Dividing degrees by M gives a numerical semigroup with finite complement; each supported degree is one-dimensional. Its Hilbert series differs from 1/(1-z) by a polynomial, so the normalized leading multiplicity is exactly one. The integral finite map A^1 to this monomial curve also proves that its only point outside the grading orbit is its origin.

For the valuation, the shifted 2-power cyclotomic polynomial is Eisenstein. Factoring 1-zeta^(2^j) over the 2^j roots gives valuation 2^j, and an odd exponent contributes a unit geometric-sum factor. Thus v(1-zeta^b)=2^v2(b), as used. This is invariant under dualizing a character or replacing the primitive root by another primitive root.

The moving adjoint weights contribute 2 sum_(i=0)^(n-2) (n-1-i)2^i = 4M-2n-2. The cubic monomial enumeration is exhaustive: the smallest nonzero index occurs once, twice, or three times. In the twice-occurring case, precisely the adjacent chain monomial is fixed; all later partners contribute valuation i+1. The all-zero-weight cube is the remaining fixed monomial. The resulting moving cubic valuation is 7M-(n^2+7n+6)/2. Subtracting the moving orbit representation yields 3M-binomial(n+2,2). The conormal dimension m-n^2 and absence of trivial conormal characters follow from the previously verified smooth quotient and one-dimensional fixed tangent. I independently checked the finite-sum identities by the stated recurrences and their n=2 initial values.

P-F28 correctly labels its coefficient as local; the later P-F31 supplies the global uniqueness that upgrades it to an actual series coefficient.

## P-F31: actual pole and precise PH3 consequence

The canonical ray is the full cubic invariant ring with its coefficient degree divided by d0=n/g, since the central character makes every nonzero ordinary degree divisible by d0. This is an actual graded-algebra identification, not only an equality of multiplicity dimensions.

Every nonzero fixed quotient point has a closed-orbit representative and a finite two-power exact-form lift with determinant of order M, by P-F26. A nonzero homogeneous invariant at that point gives the rational-span condition. P-F30 then forces the actual representative to be the smooth chain, even for originally larger-order lifts and arbitrary mixed support. GL_n action on this quotient is the full grading action because the determinant character is surjective. Thus all nonzero fixed points are precisely the chain grading orbit.

The graded origin is fixed and lies in its closure. Finite-type closed subsets over C are determined by closed points, so the support of the entire fixed scheme is the one irreducible chain curve. This does not assume reducedness or rule out embedded structure at the origin. P-F24 proves ambient and fixed-scheme smoothness off that origin, so the unique component is generically smooth and P-F23 applies.

I reread P-F23's Koszul proof for this application. Generic Koszul homology has the exterior excess-conormal character, and its leading graded term is its trace times e_Y. Contributions supported only at the origin are finite-dimensional and have polynomial Hilbert series. They vanish after multiplication by 1-t^M and cannot cancel the nonzero curve contribution. With P-F28's e_Y=1, the limit asserted in P-F31b is nonzero, giving a simple pole at every primitive Mth root. The additional cyclotomic valuation is the negative of P-F28b, and the differential residue factor -zeta/M follows from differentiating 1-t^M. Both are correct.

A polynomial numerator cannot create a pole where every denominator factor is nonzero. Therefore every displayed rational expression must contain a factor whose weight is divisible by M, irrespective of numerator signs or whether it arises from parameters. The same pole forces every quasipolynomial period to be divisible by M. Since the source parameter is binomial(n+2,3)^2+n+1, exponential M cannot be bounded by any fixed polynomial in that parameter. This refutes the positive-form existence clause as well as the already refuted canonical clause; it does not by itself refute PH2, SH(a), or prove a complexity lower bound.

## Exact source check

Freshly opened both the supplied transcription and the original GCT VI PDF: https://arxiv.org/pdf/0704.0229 . Definition 1.2.7, printed p.15, equation (1.4), defines modular index as the maximum denominator weight. Hypothesis 1.6.7, printed p.25, has first an existence clause and then the stronger canonical clause, with dimension of G and the two heights as the parameters. The draft's attribution and distinction are exact. Own retrieval refs: `turn555734407view0`, `turn238082362view0`, `turn238082362view1`.

No correction was required. In particular, this conclusion uses full fixed-locus uniqueness, not a presumed implication from a universal denominator, purity, or parameter degrees.

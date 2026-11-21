# Independent whole-proof review: A32

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, effort not exposed, `/root/effective_galois`.

**Result: PASS.** This is an independent mathematical reading and an exact finite-computation rerun, not formal verification.

## Exact source and scope

Read the entire statement, all four proof steps, arithmetic implementation justification, and concluding scope paragraph of `work/row_audit/A32_ORDINARY_RATIONAL_WITNESS.tex`, SHA256 `c14a25d7eef5b20f2e81e4d6226809649d4b77922f6667603ac5db311e4ea32c`.

The statement constructs a constant pointed degree-thirteen cover of the A27 curve over F256 with an ordinary twelve-dimensional Prym and odd rational relative class number. Its precise constant-extension criterion is odd relative class number exactly when the extension degree is not divisible by seven. All geometric etale two-torsion becomes rational at degree seven, and no nonzero rational two-torsion appears earlier.

## Complete mathematical reading

1. The reciprocal model, field encoding, Weierstrass base point, Jacobian order 65520 = 13 times 5040, and rational point count 256 are consistent with A27. Because thirteen occurs exactly once in the group order, the verified nonzero generator and multiplication by 5040 define the stated surjective quotient.
2. The Mumford divisor algorithm is justified for repeated and ramified support. Opposite support cancels by principal hyperelliptic fibres. The single affine ramification point can occur only once in a reduced divisor, because the norm polynomial has nonzero linear term there. Remaining repeated support is on an unramified branch and has unique higher-order interpolation. The norm-reduction formula preserves the class and gives degree at most two. Genus-two Riemann--Roch proves uniqueness of the reduced class. The second implementation uses binary linear algebra rather than importing the first implementation's extended-GCD composition.
3. The Lang construction is geometrically connected and split over the marked point by the already checked A12 argument. Its genus is fourteen and Prym dimension twelve. The exact genus-two character polynomial has determinant term 256 because the canonical detector at the marked Weierstrass point is zero.
4. The point-image table gives S(Z) = Z + Z^5 + Z^8 + Z^12 modulo two. Irreducibility of Phi13 and the displayed polynomials imply that none of the twelve character values is zero or one, proving the rational unit assertion.
5. The exponent set is fixed by multiplication by eight. Its three distinct doubling translates partition the nonzero residues modulo thirteen, so beta = S(zeta) lies in F8, has order seven, and has trace one. Its minimal polynomial is Z^3 + Z^2 + 1. The relative reduced zeta numerator is consequently (1 + T + T^3)^4 = 1 + T^4 + T^12.
6. The reduced character determinant comparison is applied with finite-field coefficients of characteristic two, a rank-one lisse sheaf, and a smooth proper curve. These meet the actual cited hypotheses. The coherent operator is the linear extension of the original 256-power Frobenius, not the semilinear operator on an enlarged coefficient field. Each nontrivial coherent character line is one-dimensional and has nonzero scalar, so the new geometric two-rank is twelve.
7. The constant deck action commutes with that linear Frobenius. Its character-line decomposition excludes hidden Jordan blocks despite repeated characteristic-polynomial roots. Every scalar has exact order seven. The full extension rule, first appearance of rational torsion, and complete rationality of the two-torsion at degree seven follow. Dual or inverse conventions preserve both order and fixed-space conclusions.
8. The final scope is correct: this ordinary rational witness need not be a geometric rank-zero witness, and the calculation does not assert absence of other geometric theta points of order thirteen.

## Primary and recovered source checks

Read the complete recovered successor A.20 statement and proof in `recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex`, including the exact coefficient convention, reduced determinant identity, functorial character projector, and stable-part argument.

Opened Deligne, *Fonctions L modulo ell^n et modulo p*, SGA 4 1/2, primary scan at <https://publications.ias.edu/sites/default/files/Number32.pdf>. Read the exact setup in section 2.1, both cases of Theorem 2.2, formula (2.4.1), and Remark 2.7 retaining the reduced-coefficient hypothesis. The relevant printed page is 116. Cached indexed web references: `turn646530826view1`, subsequently reopened as `turn588896538view0`. A direct URL refetch failed because the PDF exceeds the retrieval size limit; the already indexed primary text reopened successfully. No claim is made to have independently reproved Deligne's theorem or read its entire proof.

Opened Katz, *Une formule de congruence pour la fonction zeta*, SGA 7 II, Expose XXII, primary author scan at <https://web.math.princeton.edu/~nmk/old/congzeta.pdf>, web reference `turn646530826view0`. Read the relevant stable-part comparison and its proof, especially Proposition 2.2.5 and the characteristic-polynomial convention of Proposition 2.2.4, together with the preceding stable Artin--Schreier setup. These explicitly distinguish linear coherent Frobenius from the coefficient-semilinear action and identify the inverse arithmetic Galois convention. The functoriality needed to take deck-character summands is available.

## Executed certificate

Fully read the supplied second implementation before running an isolated copy. This was a rerun of that supplied independent implementation, **not a newly authored third arithmetic implementation**.

Execution record: `work/effective_galois/A32_certificate_rerun/EXECUTION_RECORD.json`. Started 2026-11-21T03:56:46.331044+00:00, exit status zero, elapsed 1.2318 seconds. The result and all-point file are byte-identical to the retained originals.

- Script SHA256: `4509aeec3f30b05092c794d75779b64d91e95a228b6daadda91a0bfc9074731c`.
- Result JSON SHA256: `ebf3aa5f670fa58421c904a16b7b1cf95f62bb00bec8cf21f4f0e2cced8d6ba9`.
- All-point JSON SHA256: `c9a60784bfdb35abb09b59079281bc0964818aa7997c676943fbfd34889d02d1`.

No correction to the mathematical source was required.

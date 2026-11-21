# A32 independent whole-proof and certificate review

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Result and exact scope

**PASS.** I read the entire proof in `work/row_audit/A32_ORDINARY_RATIONAL_WITNESS.tex`, SHA256 `646ce399a50b29aa4766a86603a80d700c260486639a04c0d9b62ce972e663c4`, and the entire independent checker `work/row_audit/verify_A27_character13_linear.py`, SHA256 `4509aeec3f30b05092c794d75779b64d91e95a228b6daadda91a0bfc9074731c`. I reran an unchanged copy of that checker under `A32_review_rerun/` in this directory. The geometric, character, and extension-field inferences below were checked as written arguments; this is not a proof-assistant verification.

The result concerns one specified constant, pointed cyclic cover. It does not assert absence of other theta points or of other rank-zero covers. The full new Prym here is ordinary and has an odd number of rational points over the displayed field; those are different properties.

## 1. The exact divisor arithmetic

The change of variables `X=1/t`, `Y=y/t^2` gives exactly `Y^2+X^2Y=uX^5+X^3+uX`. Its point at infinity is the chosen original point over `t=0`. The affine model is smooth: a singular point would have `X=0`, but the derivative of the right side there is the nonzero element `u`. The odd degree-five model has the unique point at infinity with pole orders two and five for `X` and `Y`.

The checker implements its own field products modulo the specified binary polynomial. It finds an inverse for every nonzero encoded element, and finds the specified root `u=188` of `u^2+u+1`. I checked the polynomial division, gcd, binary-linear interpolation, scalar chain, and enumeration logic. It imports no producer arithmetic.

The cancellation by `gcd(U1,U2,V1+V2+X^2)` removes exactly opposite support, with full common multiplicity. At unramified support the two local roots differ by the unit `X^2`, so the same-branch and opposite-branch conditions are distinct and higher root interpolation is unique. At the only affine branch point `(0,0)`, a reduced pair cannot contain multiplicity two: the linear coefficient `u` in the norm equation prevents divisibility by `X^2`. Two occurrences therefore cancel by the principal divisor of `X`.

After cancellation, the stated interpolation equations are genuinely linear over `F2`, including the squared term. Their unique solution represents the correct sum divisor with multiplicities. In reduction, the pole orders of `Y` and `V(X)` have opposite parity, so the norm argument has no hidden leading cancellation. The complementary divisor has degree at most two for the degrees encountered here. Keeping the leading coefficient `u` until monic normalization is correct. The uniqueness argument for reduced genus-two representatives also checks.

The rerun reproduced 256 rational points and the exact generator `((237,80,1),(207,106))`, with thirteen distinct multiples and thirteenth multiple zero. All projected point classes lie in this cycle. The complete point-image counts are

`44,19,18,18,16,19,16,16,19,16,18,18,19`.

The order input `65520=13*5040` is the already checked A27 Frobenius count. Thus the definition by multiplication by 5040 is a surjective group quotient, not only a map on the enumerated points: it kills the other primary components and is invertible on the order-thirteen subgroup. The rerun retains all 256 coordinates and their projected classes.

## 2. The character and geometric-rank conclusions

The Lang-pullback construction from A12 gives a geometrically connected constant cover with split fibre over `W`. Riemann–Hurwitz gives genus fourteen and new-factor dimension twelve. Because `K_C` is linearly equivalent to `2W`, the exact nontrivial genus-two character polynomial is `1+c1*T+256*T^2`.

Reducing the counts gives `S(Z)=Z+Z^5+Z^8+Z^12`. Since two has order twelve modulo thirteen, `Phi_13` is irreducible over `F2`; neither `S` nor `1+S` is zero modulo it. This proves that every character scalar is nonzero and different from one. The latter property gives the odd relative class number.

The set of four exponents is fixed by multiplication by eight, so `beta=S(zeta)` lies in `F8`. It is not zero or one, hence has exact multiplicative order seven. The three doubled exponent sets partition the nonzero residues; therefore `beta+beta^2+beta^4=1`. Its irreducible cubic is `Z^3+Z^2+1`, and its reciprocal factor is `1+T+T^3`. Each of these three scalar conjugates occurs four times among the twelve characters. Hence the full reduced new polynomial is exactly `(1+T+T^3)^4=1+T^4+T^12`.

I reread the entire recovered successor A.20, including its proof, and reopened Katz's primary SGA 7 II Exposé XXII, Propositions 2.2.4–2.2.5 and their comparison argument, printed pages 407–409. The proof correctly uses the linear extension of coherent 256-power Frobenius, not the absolute semilinear operation after adjoining the character values. The stable-part comparison is functorial for the constant deck action, so its use on the character summands is valid. Each of the twelve nontrivial coherent summands has dimension one and has a nonzero Frobenius scalar. Thus all twelve new dimensions are stable, giving ordinary geometric 2-rank twelve.

## 3. Extension fields and possible repeated-root ambiguity

For a degree-`m` constant extension the linear Frobenius eigenvalues are the original scalars raised to `m`. They all have exact order seven, so the rational new-factor order is odd exactly when seven does not divide `m`.

The repeated roots of the total characteristic polynomial do not conceal Jordan blocks. Over a field containing the thirteenth roots, the constant deck action splits the new part into twelve distinct one-dimensional character lines. Frobenius preserves each line. Consequently its seventh power is the identity on the whole new stable part, and no nonzero fixed vector exists for any positive degree less than seven. The functorial comparison, or its dual on étale Jacobian torsion, therefore proves the exact claimed field of rationality for all `2^12` geometric étale 2-torsion points.

## Primary source reopened

N. Katz, *Une formule de congruence pour la fonction ζ*, SGA 7 II, Exposé XXII, Propositions 2.2.4–2.2.5, pp. 407–409:
<https://web.math.princeton.edu/~nmk/old/congzeta.pdf>.

Fresh retrieval reference: `turn883471973view0`; the propositions, definitions of the linear and semilinear extensions, and intervening proof were read in the retrieved primary text. Screenshot retrieval was also requested, but no additional screenshot-inspection claim is needed for this mathematical audit.

## Retained computation

The unchanged rerun script, its result JSON, and `A32_ALL_POINT_IMAGES.json` are in `A32_review_rerun/`. Their hashes and comparison with the author's outputs are recorded in the accompanying manifest and check-event fragment. I did not rerun the original producer and do not claim a third implementation.

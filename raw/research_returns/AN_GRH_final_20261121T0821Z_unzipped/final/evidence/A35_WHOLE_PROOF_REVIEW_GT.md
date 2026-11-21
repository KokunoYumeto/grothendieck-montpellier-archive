# A35 independent whole-proof review

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source: `work/row_audit/A35_TWO_PRIMARY_THETA_FIELD.tex`.

**PASS — independent whole-proof read** of the version initially supplied at SHA256 `e2d54a8b79ad3f30d744ca95513598b324b5730066f0eb994d272505b32c3e6a`. I checked every statement and all three proof steps. No computation or formal-verification claim is made.

## Exact two-torsion intersection

The hyperelliptic branch points number `f+1`, where `f` is the geometric 2-rank. Their nonzero pair differences give precisely the nonzero geometric 2-torsion: one point for rank one and three distinct points for rank two. Distinctness follows from Abel-map injectivity, with signs irrelevant on 2-torsion.

For a fixed difference `T=[Wi−Wj]`, two theta points differing by `T` give the degree-two equivalence `R+Wi ~ S+Wj`. If the divisors are equal, the two points exchange `Wi,Wj`. Otherwise genus-two Riemann–Roch forces the common class to be canonical, so the two divisors are `2Wi` and `2Wj`. This proves the exact intersection on geometric points, not merely an upper bound on its cardinality. Its two points are killed by two because `2Wi~K~2B`.

The use of the actual locally exact differential line bundle `B` on the Frobenius twist is essential and correct. On an ordinary curve `B` is not effective, so the Raynaud theta divisor cannot simply be replaced by an Abel image based at a Weierstrass point. The source keeps this translation explicit throughout.

## The Frobenius powering argument

If `d` kills the Frobenius action on geometric four-torsion, its action on the étale Tate module is `U=I+A` with every entry of `A` divisible by four. For a nonfixed theta point of exact order `2^a`, writing it as `v/2^a` gives a finite minimum valuation `t<a` for `Av`, with `t>=2`.

For `A_j=U^(2^j)−I`, the claimed induction is exact. Its matrix entries have valuation at least `j+2`, while `A_jv` has minimum valuation exactly `t+j`. In `2A_jv+A_j^2v`, the first summand has valuation `t+j+1` and the second at least `t+2j+2`, so cancellation of the leading term is impossible, including the base step. Taking `j=a−t−1` produces a nonzero exact two-torsion difference between two points on the Frobenius-stable theta divisor. The intersection calculation forces the original point to be two-torsion, contradicting its assumed motion under `U`. Hence every geometric two-primary theta point is fixed by `F^d`.

## Field bounds and canonical residue

For rank one the four-torsion automorphism group has order two. For rank two the reduction kernel in `GL2(Z/4)` has exponent two and the group downstairs has element orders one, two, and three. Thus the possible orders upstairs are contained in `{1,2,3,4,6}`. The common degree is twelve, whereas each individual degree is at most six; the source correctly warns that the possible degree-four field is not contained in the degree-six field.

The canonical identity is `kappa_R=−2 z_R`, with `z_R=O(R) B^(−1)`. Since all geometric Jacobian points over a finite field are torsion and multiplication by two is invertible on their odd part, the canonical class is two-primary exactly when `z_R` is. The translated Abel map is defined over the ground field and is injective on geometric points, so rationality of `z_R` forces rationality of `R`. The same argument applies to the hyperelliptic-pair difference `R−iota(R)=2z_R`. It does not apply to arbitrary pairs, and the source explicitly avoids that overstatement.

## Final RM5 source delta

**PASS — targeted final-source delta** at SHA256 `6ca6888caa83acf5b8eb9f26e0bf55a60ed00718ce337b64810fd99f88d93445`. I read the entire appended paragraph and proof of T2F.10, and checked the equation-tag normalization.

The specialization to A33's ordinary targets checks. The integral ring `O5 tensor Z2` is the unramified quadratic discrete valuation ring because two is inert in the discriminant-five quadratic field. The ordinary étale Tate module has rank two over `Z2` and is torsion-free over this quadratic ring: multiplying a putative annihilator by its conjugate would give a nonzero `Z2` annihilator. It is therefore free of rank one over that ring. The ground-field-defined action commutes with Frobenius, which acts by a unit scalar. Modulo four its residue unit has order dividing three, and the congruence kernel has exponent two. Thus the action has order dividing six, removing the general `GL2` possibility of order four. Applying the preceding proof with `F^6` gives both displayed field bounds. The Frobenius twist carries the field-defined action to the Jacobian on which the actual Raynaud theta is defined. The scope correctly leaves odd-primary support and actual separation unresolved.

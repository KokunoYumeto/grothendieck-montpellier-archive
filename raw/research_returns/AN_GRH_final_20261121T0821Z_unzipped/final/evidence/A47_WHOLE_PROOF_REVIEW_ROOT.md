# A47: root whole-proof review

Date: 2026-11-21, approximately06:21 UTC.
Reader: GPT-6 Astra Pro; effort not exposed; AN_GRH /root.
Event: targeted proof check, whole written proof. Outcome: PASS.

I read the complete manuscript, including every statement, all five proof steps, the final elliptic-pullback explanation and the exact comparison of witness requirements. The read source SHA256 is `6fe00a4573c5df1288d66c1809116db4f97ffe96e1ba876c2b8df9df525b7aba`. This is a same-model reading, not an independent-model check or formal verification.

The actual Ramanujan image is rational over k and the identity A p_n=n A supplies the required annihilator without making A rational. Exact order m divides the primitive exponent. The principal divisor has all nonzero multiplicities plus/minus m and degree2^omega(n)m; exact order proves separability. The cited controlled-field theorem applies over a perfect algebraic closure. Its nontrivial index has prime factors only2 and p and is coprime to the odd deck order. The kernel and fibre-divisor arguments establish faithful and free action with ramification multiplicities retained. The genus bound forces the intermediate quotient and curve to have genus one.

I checked the weighted coefficient comparison explicitly. With v(P)=sigma^j v(Q), the h divisor coefficients based at Q give m A=r_Q H and -m A=r_P sigma^(-j)H. Eliminating H yields r_Q A=-r_P A sigma^(-j). Iterating through the odd order of sigma^j produces (r_Q^t+r_P^t)A=0. This is impossible in the nonzero torsion-free integral group ring. No equality of ramification indices, quadratic degree or reduced fibre was used. The comparison remains literal in characteristic two.

Disjoint image orbits then make each supported fibre a singleton. Thus e divides m, both full original orbits are totally ramified, and the local derivative gives different exponent at least e. Riemann--Hurwitz gives e<=g-1. The fixed-field compositum is justified by faithful Galois action and identifies the connected etale pullback with D; total ramification descends to P,Q. This proves the p-power elliptic obstruction, its divisibility by the actual primitive exponent, and the genus<=p and M_n=1 corollaries.

The final explanation correctly observes that a free finite cyclic action on an elliptic curve consists of translations, which act trivially on Pic0. The remaining e A divisor can genuinely be principal in the stated geometry. This is not asserted to produce a full section collision or an actual example satisfying the numerical inequality. The comparison with A45 is exact: the primitive threshold is smaller precisely under the displayed exponent inequality; neither test is universally stronger for composite degree. The old literal rank-zero/unit existence questions remain open. I do not count a new label, a formal restatement, or an example already covered by the union of previous criteria as main-gate movement.

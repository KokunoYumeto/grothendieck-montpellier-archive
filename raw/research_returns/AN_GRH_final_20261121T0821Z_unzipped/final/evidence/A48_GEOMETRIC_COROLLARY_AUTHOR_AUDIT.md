# A48 geometric singular-arrow corollary: author/source audit

Date: 2026-11-21. Reviewer/author: GPT-6 Astra Pro, AN_GRH `/root/row_audit`. Effort is not exposed.

## Checked result and exact version

`A48_GEOMETRIC_SINGULAR_ARROWS_COROLLARY.tex`

SHA256: `621be08cff1bade89a711744b4182984e6e5e04ac2da11cd7df3d89724445714`.

**PASS, targeted proof check.** The complete source was read at its first full version and again after the display/map-name changes. The final narrow correction removes the ambiguous phrase “ordinary cyclic thirteen-cover”: A32 proves that the primitive factor is ordinary, not that its whole covering curve is ordinary. All four proof steps and the conclusion/scope were checked. This is an author whole-proof check, not an independent re-proof or formal verification.

The existing `A48_PULLBACK_ITERATION_SUPPLEMENT.tex` remains fixed at SHA256 `b80961b464066b270cf4edda207647bbf9bf17e4a55423c2292b6d7ca4ca824b`.

## Exact primary source and reading scope

Michel Raynaud, *Revêtements des courbes en caractéristique p > 0 et ordinarité*, Compositio Mathematica 123 (2000), 73–88. DOI: `10.1023/A:1001840726893`.

Retained publisher PDF: `Raynaud2000.pdf`, SHA256 `ad8cd27ee1169d46c9e79e902e02bc40fc66145ffe35b79b4c86f62b381b183f`.

Primary URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16AB72912D3CE32BFC5D012B1025A8E4/S0010437X00000440a.pdf/revetements-des-courbes-en-caracteristique-pandgt0-et-ordinarite.pdf

The following primary passages were read, including their displayed proofs/constructions: §1 setup and Proposition 1 (printed pp.74–75); §3 construction, Lemma 16, Theorem 17, Corollary 18 and the full printed general-case proof of Theorem 2 (printed pp.83–86). The exact group-construction paragraph, Theorem 17/Corollary 18 hypotheses, and the genus-two characteristic-two choice were reopened/read for this corollary. This does not claim a whole-publication audit or an independent proof of all external Mumford/Hirschowitz inputs.

Exact locators:

- Printed p.84: the line bundle has exact order n; the connected cover that trivializes it is Galois with Heisenberg group fitting an extension of J[n] by μ_n.
- Theorem 17 and Corollary 18, printed p.85: n is prime to the characteristic, divides the polarization degree (the usual polarization gives degree g), and g/n ≤ (g−1)/(p−1).
- General-case proof of Theorem 2, printed p.86, case p=2 and g=2: m=5 and n=g′/2=3.
- Proposition 1(4), printed p.75: no-theta representations remain no-theta under the indicated induction.
- Proposition 1(5), printed p.75: one no-theta representation of the Galois group forces the whole pulled-back Jacobian to lie in the theta support upstairs.

Pop–Saïdi, §1.3, printed p.112, was also read for the exact Frobenius-character-kernel interpretation. Retained PDF `../sources/pop_saidi2003.pdf`, SHA256 `6180691f053616b737217f123906698c041ceed4152748db812211cb600054c9`. No new correction to the already-recorded pairwise-coprime qualification is claimed.

## Proof checks

1. The cyclic degree-five cover of a genus-two curve has genus six. Choosing n=3 satisfies 3|6 and 6/3=2≤5. Its Heisenberg group has order 3·3^(2·6)=3^13.
2. The geometric Galois closure over the original curve is not assumed to be the original Heisenberg cover. Over the cyclic degree-five intermediate field, the closure is the compositum of the five conjugate H-extensions. Restriction gives an injection into H^5 and a surjection to H. Thus its order is 3^a with 13≤a≤65 and the degree over the original curve is 5·3^a. In particular it is prime to 13 and to 2.
3. Induction of the no-theta representation factors through that actual Galois closure. Proposition 1(4) preserves the absence of a theta divisor; Proposition 1(5) then yields the whole-Jacobian theta containment. This uses the no-theta conclusion, not merely nonordinarity.
4. The exact-order-thirteen class is chosen on the Frobenius twist by the equivalence of étale covers. Its pullback retains order by norm composed with pullback = [d] and gcd(d,13)=1. This avoids treating an unnormalized Frobenius twist as the same torsion line bundle.
5. Coprime geometric degrees give linear disjointness and a connected cyclic degree-thirteen fibre product. The actual primitive projector/norm argument PI.2 applies with odd degree d; the old geometric two-primary group injects, so the new primitive two-rank is at least twelve.
6. Riemann–Hurwitz gives g(Y)=d+1 and g(D′)=13d+1. The primitive factor has dimension 12d because thirteen is prime. Each of its twelve character spaces has coherent dimension d. All twelve theta incidences give nonzero kernels of their respective Frobenius arrows, so stable rank is at most 12d−12. Together with the lower bound, this proves 12≤f≤12(d−1), hence nonnilpotence despite every arrow being singular.
7. All finite geometric data descend to some finite extension of F256. This preserves geometric connectedness, ranks and theta incidences. A further rational pointing is allowed only after another constant extension; the original A32 odd rational relative class number is not asserted to persist.

## Retained inputs and scope

A32 source: `A32_ORDINARY_RATIONAL_WITNESS.tex`, SHA256 `c14a25d7eef5b20f2e81e4d6226809649d4b77922f6667603ac5db311e4ea32c`. The current statement OR.1–OR.3 was rechecked. Its complete proof and arithmetic had already been read/checked earlier in this run; no new computation or new implementation is counted here.

This proves existence of actual curves over a finite field with the stated property. It does not provide an explicit equation for the large Raynaud cover, enumerate its points, determine its exact primitive two-rank, or exhibit a new primitive-unit witness. The weaker logical inference was already refuted by A04. This corollary is more specific geometric evidence and is **not counted as a new universal main-gate advance**.

The result is saved separately so the existing b809 pullback supplement and the frozen A01–A48 build need not change during their current review.

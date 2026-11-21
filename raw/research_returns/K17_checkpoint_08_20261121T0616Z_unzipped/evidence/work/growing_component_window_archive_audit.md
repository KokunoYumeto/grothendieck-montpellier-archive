# Independent whole-proof/source audit: growing companion exclusion

**PASS.** Reviewed the entire `work/growing_component_window_section.tex`, including K17-BOTH-COMPANIONS, the exact partial-regularity source statement, and K17-GROWING-COMPONENT-WINDOW.

Reviewer: GPT-6 Astra Pro, run `/root/archive_kummer`, 2026-11-21. Reviewed TeX SHA-256: `73e09dd9ebfdcb8806d3a69a578ff0318c164494cf25c9cf6027def2d4feb91a`.

## Actual primary-source inspection

Read Chen et al., *Almost all primes are partially regular*, arXiv2602.05090v1, Theorem1.1 and its exact definition on p2, Corollary1.4 on p3, and every mathematical lemma and proof in §§2–3, pp6–10. The complete local PDF is `work/partial_regularity_2026.pdf`, SHA-256 `16a6068c90c5ef5c43f87ec5da400926c8483a88bddec682828e6e8b4c8ffb20`. Fresh official arXiv retrieval: `https://arxiv.org/abs/2602.05090`, reference `turn632198588view0`, confirms the February4,2026 v1 and the simultaneous partial-regularity statement.

The mathematical counting proof was independently reconstructed. The Bernoulli numerator product has log-size O(m² log m); the primorial argument gives omega(n)=O(log n/log log n); Euler's formula and the factorial lower bound give log log P_m >= log m for all large m. Thus omega(P_m)=O(m²). Eventual monotonicity of sqrt(t)/(log t)^alpha reduces the varying prime cutoff to m=floor(sqrt(x)/(log x)^alpha), giving O_alpha(x/(log x)^(2alpha)). The finite initial primes and small cutoff values are legitimately absorbed in the constant. No Lean artifact was executed or independently certified here. Only the cited counting theorem and reflected class consequence are being used; this audit does not endorse every other corollary or discussion in the source paper.

Freshly reread the exact Sharifi Proposition3.4.7 isomorphism and its proof in the already inspected full notes, p92, while checking the direct-limit character calculation. The finite-layer control and reflector have their separate complete audits.

## Both companion parities

For 2<=a<=p-3 even, Herbrand gives A_0^[1-a]=0 from the Bernoulli unit. The reflected even component is A_0^[a], as also obtained by substituting e=p-1-a in the proved reflector. The characterwise control theorem applies to ALL characters, not just the even ones, so both vanish separately at every finite cyclotomic layer and in the norm inverse limit X.

The proof then correctly forms the extension-of-ideals DIRECT limit A_infinity. Its [1-a] component is zero term by term. The exact Kummer isomorphism `(A_infinity^-)^vee(1) = M^+` therefore makes M^[a] itself zero: duality changes [1-a] to[a-1], and the Tate twist adds1. This is an integral statement and does not replace the direct limit by the norm inverse limit or a pseudoisomorphism.

CC.2 makes M^[1-a] integrally free of rank one. Inside the precise range 2<=a<=p-3, the only excluded even character is a=2; the existing unconditional Coleman calculation covers its odd reflection [-1]. Thus both claimed Lambda-torsion components vanish. For all p>2^31, the complete fixed Bernoulli factor certificate supplies every a=2,4,...,32. The proof correctly avoids extending EVEN-companion vanishing to the small irregular numerator primes merely from Vandiver. The p37,a32 example has exactly the announced scope.

## Growing range and K/Soulé consequences

The source cutoff is the stated floor, with min(cutoff,p-3), and alpha>1/2. The same one set of good primes gives the simultaneous Bernoulli input for every eligible a. Passing to all layers, duals and both companion parities is deterministic, so it adds no exceptions. Dividing the source count by pi(x)~x/log x gives relative prime density zero for the exceptions because 2alpha>1.

For k>0 with k congruent to -a/2 modulo (p-1)/2, the class exponent -2k equals a modulo p-1. Formula(K2) gives the required K4k primary vanishing, and the already checked full-domain Soulé formula has m=2k+1 and 2m-2=4k. Thus the surjectivity statement is indexed correctly and imposes no claim on a deeper filtration subgroup. These consequences are independent of Alpoge. The growing character interval does not cover all residues, so no whole-prime Vandiver/Greenberg or entire-kernel assertion follows.

No mathematical correction requested. No numerical execution beyond the previously recorded exact Bernoulli certificate was required.

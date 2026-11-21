# Independent whole-proof audit: norm families and Pair-NV

**Verdict: PASS for K17-NORM-TORSION, K17-UNIVERSAL-PAIR and the conditional arithmetic corollary K17-WWE-PAIR.** The displayed Wake-Wang-Erickson hypotheses remain assumptions. This audit supplies no arithmetic Triple-NV, non-Greenberg example or new unconditional prime range.

Reviewer: GPT-6 Astra Pro, `/root/tripod_integral`, 2026-11-21. I read the entire `work/universal_cyclotomic_pair_bridge.md` and the entire final `work/universal_cyclotomic_pair_section.tex`, then reconstructed the argument independently. Reviewed SHA256:

- MD: `67dda4c47eb5ea5cff1dbc14ed91679ebaafcf37e3cf19b8910c0864b57f11b8`.
- TeX: `b58631c8a22f385fe0fff168a5fa46e312ca38af0c094e4c2844fc05b471f28c`.

## 1. The finite norm formula

Restriction of a degree-one class to H is an actual continuous homomorphism because H acts trivially on the Tate coefficients. Its value is unaffected by changing the representative cocycle. The cocycle identity makes the restriction equivariant under Gamma to the p^n-th power, with multiplier u to the same power.

In the finite sum defining Phi, multiplication of the argument by gamma shifts its coefficients. The wraparound term is correct: u to the negative power p^n minus one, times the multiplier u to the power p^n, leaves u. This is exactly multiplication by u times the inverse group-ring generator. The restriction of corestriction is also correct with the stated coset representatives: the coefficient action contributes u to the negative coset exponent, and conjugation of the argument contributes the positive exponent. Summing the finer coefficients over one group-ring fiber therefore gives the coarser coefficient, with no normalization or division.

The inverse limit is taken only after these actual homomorphisms have been constructed. There is no unproved cohomology/limit interchange or compatible-cocycle choice. Its target is the underlying domain Lambda with action twisted by the involution gamma maps to u gamma inverse. In the power-series parameter the constant term of this substitution is u minus one, which is p-adically small, so it is a continuous automorphism; applying it twice gives the identity. A nonzero torsion annihilator stays nonzero. The resulting integral domain argument kills all Lambda-torsion. The identity coefficient at every finite level recovers the original restricted class, so the conclusion holds separately for every group and coefficient level.

## 2. Cyclotomic inputs and parity

For a unit exponent, the norm identity for one minus a compatible root of unity is exact. Kummer maps respect that norm, coefficient reduction and corestriction. The corresponding finite classes factor through the maximal pro-p quotient because the cyclotomic coefficient action and the Galois closures of the p-power radical extensions are pro-p over a field containing mu_p. This agrees with the earlier natural degree-one comparison.

For an exponent p^s times a unit, the product over all p^s-th root translates is exactly the desired one-minus-root expression. Every exponent of a factor remains prime to p because the added term is divisible by p. Thus every finite FK input is a sum of restrictions of norm families in the same field. This argument avoids division by a field degree.

Complex-conjugation averaging preserves norm compatibility and the torsion-annihilation conclusion. The ratio of a p-unit and its conjugate is a global unit, because the sole p-prime is fixed and its valuation cancels; all of its archimedean absolute values are one, so it is a root of unity. The negative Kummer component is cyclic. Its square and all mutual products vanish for odd p by alternating cup product. Mixed signs contribute only to the odd target. Therefore the even target uses even Kummer classes whose restrictions annihilate T and factor through Q.

## 3. The actual class-two extension

For odd p the class-two quotient of the free pro-p group has the integral BCH Lie structure. Its central commutator module is the completed exterior square of M. A continuous Zp splitting of M onto the torsion-free compact quotient Q proves that quotienting by the closed brackets with a T input leaves precisely the completed exterior square of Q.

That remaining central module is c-even. The c-odd part of the Lie module therefore maps isomorphically to the c-odd part of M, giving a canonical Gamma-equivariant section. The lift of T-minus is central after the bracket quotient, and is Gamma-stable, so it can be killed. This leaves the odd Q section and the genuine even extension N to E to T-plus. No Gamma-equivariant splitting of the original M onto Q has been assumed. The even companion product becomes the additive characteristic-polynomial error in this quotient because all its torsion-input brackets have been killed. Its free-Q quadratic term agrees with the earlier Magnus companion on the derived element.

## 4. Divisibility, repeated roots and uniform denominators

If every free-Q coefficient vanishes on a root divisor, the integral product-coordinate substitution divides the companion by gamma minus alpha. It preserves a common denominator bound. Because the divisor is symmetric, the quotient remains alternating. Cyclicity gives the nonzero alpha-socle vector q(gamma)/(gamma-alpha) times the cyclic generator, including at a repeated root. Subtracting the divided companion gives a Gamma-eigen lift of that vector.

Intersecting its line with the finite free O-lattice T-plus gives a saturated sublattice. It is a direct summand, so a section can be extended from the equivariant line. There are finitely many basis lifts, and the divided power series has one bounded denominator. A single p-power therefore makes the section and every resulting central coordinate integral. The Gamma-section defect vanishes on the chosen line, and the same denominator bound works for every finite coefficient level and every cup used later.

## 5. The cup primitive and the inverse target

Averaging even cocycles makes them vanish on the Gamma section: conjugation fixes that section while acting by minus one on the coefficient module. Their restrictions factor through Q. The two pieces of the proposed primitive have differentials respectively equal to the symmetric and alternating halves of the desired product. They add to p^b times the actual cup, with the factors of one-half valid for odd p. The Gamma-equivariance defect is the alternating pairing evaluated on the section defect. It therefore vanishes on the split socle. This calculates the cup map itself and does not deduce it merely from a characteristic series.

The Hochschild-Serre identification uses the cohomological-dimension-one properties of H and Gamma. In twist two, all odd parts of M, including odd torsion, have negative conjugation parity. The even target is consequently H1 of Gamma with Hom of T-plus, exactly as claimed. For a procyclic group, normalized generator evaluation gives the displayed coinvariant quotient. Under subgroup corestriction the generator value maps to the same coinvariant class; restriction, not this corestriction, introduces the norm sum. Thus there is no extra p factor in the transition.

The submodules generated by p^n and by B to the p^n-th power minus one are cofinal with the p-adic neighborhoods. Their inverse limit is V. Restriction to the saturated socle lattice is a surjection onto a nonzero torsion-free dual line, with eigenvalue u squared divided by alpha. The Delta character is the coefficient character squared times the inverse source character. Uniform p^b annihilation of all finite cup-generated targets would annihilate this entire nonzero inverse-limit quotient, a contradiction. No compatible expressions of target elements as sums of cups are needed.

## 6. Fresh primary-source scope checks

I freshly read the full setup in Wake-Wang-Erickson, *Pseudo-modularity and Iwasawa theory*, printed pages 2-3, and all of Corollaries 8.1.2-8.1.3 with their proofs on pages 48-49, from `work/wake_wang_erickson_pseudo.txt`. Corollary 8.1.3(2) has exactly the rational cyclicity and rational support conditions in NC.14 and concludes an integral isomorphism after quotienting the modular-symbol source by p-primary torsion. Its proof permits repeated roots; it uses a nilpotence argument rather than requiring the derivative to be a unit. At tame level one the stated primitive-character hypotheses exclude precisely the two indicated even characters. The nonunit running hypothesis is correctly applied only to nonzero target components. Primary URL: https://arxiv.org/pdf/1505.05128v3. A fresh web request was disabled as `turn317702818view0`; the already archived full primary text was used, and the blocked request is not counted as retrieval success.

I freshly read FK sections 7.1.8-7.1.10 in full, with adjoining sections 7.1.3-7.1.7, in the inspected 15 August 2012 author version. Section 7.1.10 uses surjectivity of varpi to give generation by the finite cyclotomic symbols. Section 7.1.9 gives the coefficient reduction and class-group interpretation. At field level n the source index is n+1, and reduction gives the required coefficient level n. The exact allowed exponents are respected. Primary https://www.math.ucla.edu/~sharifi/sharificonj.pdf was freshly retrieved successfully as `turn317702818view1`, 121 pages; the relevant printed locator is page 86.

I freshly read all of the opening of Sharifi's *Reciprocity maps with restricted ramification*, section 2.5, pages 16-17. The inverse group action and corestriction convention agree with the explicit formulas. Primary https://www.math.ucla.edu/~sharifi/selmer.pdf was freshly retrieved as `turn317702818view2`, 47 pages.

I also freshly read Sharifi's complete Proposition 3.4.1 proof, pages 90-91, and Proposition 3.4.7/Corollary 3.4.8 with their proofs on page 92, in `work/sharifi_full_iwasawa.txt`. These supply the minus norm surjections and the twisted, inverted pseudoisomorphism for the even ramified module without a Greenberg assumption. The complete exceptional-character paragraph in WWE, *Ordinary pseudorepresentations and modular forms*, proof of Lemma 5.2.7, page 13, explicitly gives the two zero odd components by Stickelberger. Consequently no excluded target is silently left uncovered. The one-prime, no-real-place Brauer term is zero, and lifting the finite Kummer cup generators through the prior degree-one isomorphism proves surjectivity of the existing degree-two injection on this even target.

## Final scope

Under exactly NC.14, even rational torsion cyclicity and the actual free-Q Pair-NV follow even in the presence of odd Lambda-torsion. NC.14 is a rational support condition; it is not replaced by an untwisted shared-root condition or by a claim that all X-plus is finite. The separate odd torsion cyclicity and arithmetic Triple-NV hypotheses remain necessary to apply the recorded cubic kernel theorem. No new arithmetic verification of those hypotheses is supplied here. No correction is requested to the final TeX.

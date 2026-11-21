# Independent review of P-F40

Reviewer: `/root/bridges`, GPT-6 Astra Pro, inherited/undisclosed effort.
Date: 2026-11-21. Outcome: **PASS** after a primary-source page-locator correction, with no mathematical correction.

I read the entire proof in `positivity_klein_phase.tex`, independently reconstructed every argument, and then read and checked the added exact n=8 example.

The smoothness argument is valid: a zero coordinate propagates around the derivative cycle, while the product of the derivative equations contradicts 2^n != (-1)^n if all coordinates are nonzero. The exact linear lift has order P, fixes all monomials, and has determinant one. The assumption 3 does not divide n gives gcd(P,3)=1 through the congruence (-2)^n=(1-3)^n mod9. This makes all reductions from divisibility by P to divisibility by 3P valid. The fixed-cubic classification correctly handles zero weight and both possible nonzero multiples of Q, and does not confuse linear and projective orders.

The orbit-dimension proof applies the regular-sequence/Koszul argument to the quadratic derivatives in the regular local polynomial ring. A linear coefficient in their ideal is zero because it lies in the square of the maximal ideal. The finite cyclic exact sequence then gives the asserted normal dimension, fixed dimension, and determinant. I checked the determinant of Sym^3 and the inverse-paired adjoint weights directly.

The inversion identity, age formula, phase, and odd-codimension cancellation all follow with the stated dual convention. The asymptotic bulk estimate has the correct moving counts, denominator scale P, remaining O(n^2) factors, and O(n^3) total error. Molien averaging is proved for the cyclic normal model only; the text does not infer a global pole-at-one coefficient or identify the tangent grading with stretching.

For the added n=8 example, I checked the seven cyclic gap representatives, freeness of rotation on degree-three monomials, and all seven residue orbits. I also actually executed exact integer Python enumeration of all 120 cubic monomials and 56 off-diagonal adjoint weights. Every row of the printed table matches, and the two resulting ages are exactly 27 and 28. Thus C_1<0<C_3 is established without a numerical complex approximation. The executed enumeration is reproduced in `verify_klein_phase_table.py`.

Primary sources freshly read: Zheng arXiv:2004.09008v3 Section2.2 printed p3 and Lemma3.1 printed p5; Stacks tags00NQ,02JN,062F. The draft initially used pp2,4, caused by an extracted preceding-page footer. I reported that locator issue; the author corrected it to pp3,5, and I confirmed the correction. Ref IDs: turn861647126view0, turn459501540view1, turn861647126view1, turn861647126view2, turn857899801view0. Known-source proofs are cited premises, not independently reconstructed in full.

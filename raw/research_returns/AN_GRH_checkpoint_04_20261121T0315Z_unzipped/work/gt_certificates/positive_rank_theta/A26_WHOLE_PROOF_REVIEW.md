# Independent whole-proof review: A26 rank-one augmentation criterion

Date: 2026-11-21.
Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source reviewed in full: `work/row_audit/A26_RANK_ONE_AUGMENTATION.tex`.
SHA256: `8b780159d97aaaa3f64574cf4c306b0b85a2498b06b1305a4568c4467a9e3831`.

## Outcome

PASS. No substantive gap was found in the full argument. This was an independent mathematical reading, not a proof-assistant verification. The frozen final paper and its source were not edited.

## Exact source checks

The complete recovered A1 B.1, B.2, and B.3 claims and proofs were read in `recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`, at the block beginning “The exact relative criterion and the missing existence assertion.” B.2's genus-two specialization is exactly the group-ring element used in A26. Its proof obtains the relative class number from the product of all nontrivial unramified character L-values, and identifies the mod-2 value with the degree-at-most-one effective-divisor sum. B.3 explicitly supplies the geometric connectedness argument for Lang pullbacks via the Abel map on geometric abelian fundamental groups. The separate point-section lifting lemma invoked by B.1 is an existing input, not newly reproved in this review.

The complete recovered successor A.10 and A.35 claims and proofs were also read in `recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex`. A.35 is the simultaneous quotient counting criterion; its displayed Fourier identity is the one used in A26. A.10 contains the empty nonzero coset argument. Both retain a pair-count condition in their general setting. A26 removes that condition only under the stated even-N specialization, rather than changing the scope of those earlier results.

The primary Pries–Zhu article was reopened at https://www.numdam.org/item/10.5802/aif.2692.pdf . Lemma 2.6, printed page 712, and its complete short displayed proof were read. The immediately preceding setup identifies reduced pole orders as lower ramification jumps. Web references: turn873491303view0 and turn873491303view1. This check does not claim to reprove all of the cited ramification or Deuring–Shafarevich theory.

## Proof details checked

1. A genus-two curve of 2-rank one has two geometric Artin–Schreier branch points with reduced pole orders 1 and 3. The two different ramification jumps are Galois invariant, so both branch points and their unique points above them are rational. The hyperelliptic involution therefore has exactly two rational fixed points; every other rational point occurs in a two-element orbit. This proves evenness over the given field and every constant extension.

2. For V = J(F_Q)/rJ(F_Q), r odd, the group order is odd. The group-algebra element [0] plus the rational Abel-image sum has augmentation N+1 = 1 in F_2 when N is even. Repeated image points are counted with their multiplicities, as the character criterion requires.

3. If a prime cyclic quotient fails the class-number criterion, one nontrivial character value vanishes. Primitivity of 2 modulo r makes every nontrivial character a Frobenius conjugate, so all those values vanish. Every nontrivial character of the elementary abelian r-group V factors through such a quotient. Therefore failure for every quotient kills every nontrivial Fourier coefficient of the original element.

4. Fourier inversion is valid over an algebraic closure of F_2 because |V| is odd. It forces a constant coefficient function, and augmentation fixes that constant to 1. If |V| > N, some Abel-image coset is empty. It is nonzero because P occupies the zero coset. Its coefficient is 0, contradicting the constant coefficient 1. Thus at least one quotient succeeds, for the arbitrarily prescribed P.

5. Applying the same argument to one quotient F_r proves that every surjection succeeds if r > N. The condition r divides |J(F_Q)| ensures that a surjection exists. No assertion about a kernel-size lower bound is needed.

## Scope retained

The conclusion is odd rational relative class number over the displayed field. It is not a claim that the new Prym has geometric 2-rank zero or that the criterion survives every constant extension. The final separation implication uses the existing B.1 odd-order deck argument. The existence of a primitive-root prime satisfying the remaining finite-group inequality remains a separate requirement; Artin-prime density alone does not establish it.

## Narrow recheck of the final citation clarification

Final source SHA256: `e1985e61154e2eccab66a6e4a0cff1784c3d2dbb6700930326f1e330d2529bed`.
The revised paragraph explicitly cites A12's connected Lang-pullback argument and explains that zero above [P-P]=0 gives the prescribed rational lift; the constant deck group makes the whole fibre split. The final A26 text and A12 Steps 1-2 in `work/effective_galois/lang_weil_criterion.tex` were read. The latter proves connectedness by a hypothetical intermediate etale isogeny, the Jacobian universal property, and multiplicativity of degree. The citation and its application to the untranslated Abel map check. PASS; no substantive mathematical change to the previously whole-reviewed argument.

# K17-MULTI-VK: independent whole-proof audit of the multi-even pole argument

Reviewer: `/root/vandiver_k`, GPT-6 Astra Pro; effort setting not exposed. Date: 2026-11-21 UTC. This is an independent mathematical audit, not a formal proof certificate or a claim of novelty.

## Scope and verdict

**PASS**, relative to the explicitly cited arithmetic inputs and the previously checked actual-image Hain--Matsumoto/Brown comparison. I read the entire current `multieven_pole_candidate.md`, including its finite-denominator exclusion and section 6 parity/source bridge, and independently reconstructed all steps. I also read all of the separate `sharifi_cup_parity_bridge.md` and checked its twists and parities. No remaining logical gap was found in the stated conditional deduction.

Audited candidate SHA256: `3a783a6ac23ede2a23224f4313c927e8cbc6b84a54b3268190c2be2514d3d8c8`.

Audited parity SHA256: `2ace09b7932bae5ad4b461ae4a0f3aacfdb5d56516b153dec064da48910e4535`.

The conclusion has the following precise scope. At an odd prime satisfying Vandiver, surjectivity of the odd-character cup product onto the relation space implies faithfulness of the actual rational tripod representation on the cyclotomic kernel, hence the stated equality of the two kernel fields. The cited cup-product and Vandiver computations supply these hypotheses for all odd primes below 1000. This does not establish the hypotheses at every odd prime, does not prove integral free generation, and does not rely on simple characteristic roots or lambda equal to one.

## 1. Arithmetic module and compact basis

The previously checked Iwasawa/Ferrero--Washington input gives that H is free pro-p; consequently H_ab is torsion-free over Z_p. The weak Leopoldt rank and the minimal generator count under Vandiver show that its odd part is Lambda-free of rank (p-1)/2. The algebra here is exact: a surjection from a free Lambda-module of that rank has a kernel of rank zero, and a submodule of a free module over the domain Lambda cannot be a nonzero torsion module. Character projectors then give one free rank-one module per odd character.

For the even part, Lambda-torsion alone would not imply finite generation over Z_p. The note correctly supplies the Kummer comparison with the involution/Tate twist of the minus unramified Iwasawa module, together with mu=0. Finite kernel and cokernel preserve finite generation over Z_p. Torsion-freeness of H_ab makes each even piece finite free over Z_p. The minimal generator count makes each such piece cyclic over Lambda.

For a cyclic component T with generator v, rank lambda, and characteristic polynomial q of gamma, the vectors v through gamma^(lambda-1)v form a Z_p-basis. Cayley--Hamilton and the unit constant term of q make their span stable under gamma and its inverse. That span is compact, hence closed, and therefore contains the entire Lambda-span of v. The equal-rank surjection from Z_p^lambda is an isomorphism. Continuity of the pro-p Gamma action modulo p gives q(z)=(z-1)^lambda modulo p; no assumption about the roots or the size of lambda enters.

The proposed compact free source has the correct abelianization, by the free compact universal property. Its map to H is Frattini-surjective and thus surjective. Projectivity of the free pro-p group H gives a section. The section's image is a closed Frattini-surjective subgroup of the source, so it is the whole source. This is a valid proof of an isomorphism; it does not appeal to infinite-rank Hopficity. Exact nonlinear Delta eigenlifts and gamma commuting with Delta preserve the prescribed abelian classes.

## 2. Exact presentation and the unit numerator

The companion error E_e lies in the closed commutator subgroup of H because its abelianization is the characteristic-polynomial relation. The finite presentation by the displayed R_e is justified by its universal property. An assignment to gamma, x_a, y_e determines the compact odd orbit and each finite even chain. Compatibility with gamma at the last member of an even chain is exactly the relation R_e; all other compatibilities are tautological. The order of the product is correct: R_e is the companion product followed by E_e inverse.

The important linearization assertion holds before imposing the arithmetic relations. Substitution of the compact free basis into the relative free group sends a commutator word E_e to a relative commutator word. Thus it has zero image in the free relative abelianization, and R_e has image precisely q_e(gamma)Y_e. The entire linear image of the normal relation subgroup is the direct sum of the nonzero ideals q_e(gamma)Lambda Y_e. It is free over Lambda; this does not assert freeness of the full relation module.

The map from R modulo its pth powers and commutators with the ambient free group onto the reduction of this linear image modulo (p,T) is well-defined. Powers map to p-multiples, gamma commutators map to T-multiples, and the other relative conjugations act trivially on the abelianization. Its target has one dimension per even character. Its source is generated by the same number of defining relators. Consequently it is an isomorphism.

The exact eigenlifts induce genuine finite-order automorphisms of the finite free group by unit powers of its free generators. Hence the isomorphism of relation spaces is Delta-equivariant, and the character-e class is the class of R_e. Every R_e is in the Frattini subgroup, since q_e(1) is divisible by p. Passing to descending p-central degree two kills R^p and [R,F]. The companion portion uses only gamma and y_e, so it has no odd--odd bracket term. The odd--odd term is therefore minus the augmented quadratic coefficient of E_e. The assumed nonzero cup coefficient makes one C_(e;a,b)(0,0) a p-adic unit. There is no hidden root-of-unity factor capable of changing this unit condition.

## 3. Target coefficients and repeated roots

The actual-image comparison is essential: density in the free odd rational target ensures that every relevant linear coefficient is nonzero. Weightwise rescaling can therefore normalize these coefficients. Conjugating gamma into the Levi torus makes its action in weight m equal to u^m, and the Delta eigenlift condition gives the matching residue character. The even generators have target length at least two by parity.

At target length two, the actual conjugates y_(e,j) have coefficient z^j B_e, where z=u^(m+n). Thus q_e(z)B_e equals the integral Amice numerator from the companion error. Wrong-character numerators vanish identically: their target coefficients vanish on the whole matching Cartesian grid, and successive one-variable analytic identity theorems imply the power series is zero. This includes the residue bookkeeping required later in the colored separation argument.

The candidate correctly removes possible zero denominators before division. There are only finitely many positive integers w such that u^w is a characteristic root. Taking each odd test weight larger than all these w removes every problematic pair sum. Each fixed residue still has an infinite Cartesian tail with an interior p-adic accumulation point. This restriction therefore leaves every analytic identity argument valid.

Over a finite splitting field L, the strictly proper rational functions z^j/q(z) and the partial fractions 1/(z-alpha)^k are two bases of the same finite-dimensional vector space, including repeated roots. Taking the corresponding invertible linear change of the formal even Magnus letters gives exactly the kernels C/(z-alpha)^k. This is not a change of pro-p generators. At each fixed assigned degree there are only finitely many even letters, so scalar extension introduces only one finite common denominator. Bounded L-valued measure coefficients and injectivity of the Magnus expansion are preserved.

## 4. Ordered patterns and Laurent coefficient isolation

I checked the argument with arbitrary ordered source words, overlapping alternative adjacent pairs, repeated characteristic roots, and incomparable pole-order vectors. The use of maximum number of paired letters followed by a Pareto-maximal order vector is sufficient.

For the selected disjoint pairs, the substitutions S_j=(1+T_j)(1+T_(j+1))-alpha_j define an integral formal change of coordinates, because alpha_j-1 lies in the maximal ideal. The retained base variables consist of one left variable per selected pair and all singleton variables. The original bounded-denominator ring embeds into formal power series in S over the fraction field of the base ring. Every actual denominator in the identity is then invertible after adjoining the inverses of the selected S_j: a different root at the same position has a nonzero constant, and a different position joins independent blocks, giving a nonzero base function as its constant. Wrong even characters give zero numerators for the fixed target types.

This is an embedding for the specific denominator family in use, not a claim that the whole fraction field of a multivariable series ring is a Laurent-series field. The distinction avoids an unjustified multivariable expansion. It is also essential that the original ring is O_L[[T]][1/pi], with bounded denominators, rather than arbitrary formal L-series.

Extract the coefficient with exponent -k_j at every selected S_j. A pattern omitting any selected position/root has no negative power in that variable and cannot contribute. A pattern adding extra pairs would have more paired letters and is absent by maximality. For the same positions and root colors, only a pole vector componentwise at least k can contribute, and Pareto maximality excludes every strictly larger such vector. Thus only the chosen pattern survives.

Its singleton measure transform embeds nontrivially into the base field. Each chosen numerator remains a unit at S=0: its original constant is a unit and the substitution only changes constants by topologically nilpotent quantities. Their product cannot cancel the nonzero coefficient. This proves the required contradiction. No permutation of positions, pair crossing, or same-root higher-order term remains unaccounted for. The zero-even-letter case reduces to ordinary odd moment separation.

## 5. Parity and the verified prime range

The separate parity proof passes in full. For a p-unit v, v/c(v) is a global unit, since there is a single prime above p; all complex absolute values are one. The finite-polynomial argument proves it is a root of unity. Consequently the minus part of p-units modulo pth powers is the one-dimensional mu_p line. Vandiver makes the plus part of the Kummer H1 group equal to the plus p-unit part. The Brauer term vanishes for the totally imaginary field with one omitted finite prime. Thus H2 with the doubled Tate twist is a plus space. Mixed cups vanish by parity, and the cup on the one-dimensional minus line vanishes because p is odd. Untwisting leaves precisely the odd-character cup hypothesis used above. The indices a+b=e are consistent with the H1 dual character and both Tate twists.

I freshly read Sharifi, *Iwasawa theory and the Eisenstein ideal*, arXiv math/0501236v4, Theorem 5.6 and its entire proof on printed pp.25--26, then Theorem 5.7, its complete stated computational method, and Corollaries 5.8--5.9 on printed p.27. Theorem 1.2 on printed p.2 and Corollary 5.9 give exactly the p-unit cup surjectivity for the cited range. The Magma calculation is cited, not rerun, and the target is the p-class group tensor mu_p, not the full p-class group without reduction and twist.

Primary URL: https://arxiv.org/pdf/math/0501236 . Local source: `work/sharifi_eisenstein_2007.pdf/.txt`.

I also freshly opened and read the stated range in Buhler--Harvey, *Irregular primes to 163 million*, arXiv 0912.2121, p.1: Vandiver was verified for all primes below 163,577,356, which contains every prime needed here. This is used as a cited computational theorem, not as a newly replicated computation or an all-prime result.

Primary URL: https://arxiv.org/pdf/0912.2121 .

Combining these sources with the parity lemma and the conditional proof yields the claimed odd-p-below-1000 corollary within the explicitly stated arithmetic and actual-image framework. I have not inferred any integral free-generation consequence from this faithfulness statement.

## 6. Adjacent finite-2 checkpoint

The saved exact integral computation completes cutoffs 14, 16, and 18 in its extended run, with ranks 16, 25, and 40 respectively. Every D, inverse-D, and commutator membership reduction passes exactly, and every graded odd-generation index is zero. Weight 20 did not save a completed record and is not included in the certified range.

I fully read `outer_filtration_saturation.md` (SHA256 `cbb996f46d298df152b7ab26a54f4c3ffcb877cdb3fd0bcb46c83bc72d4b9ad9`). Its integral inner adjustment, exact ad ambiguity, reduction-mod-p primitivity, and induction using the finite-kernel Hain--Matsumoto comparison pass. In particular, the actual integral filtration agrees with the rational pullback in this free geometric case. This closes the scope condition recorded in the earlier finite-2 checkpoint; it makes no assertion for arbitrary geometric fundamental groups. The new primary all-p free-Lie input is Koch--Kukkuk--Labute, *Nilpotent local class field theory*, Theorem 2.1, author-PDF pp.4--5 / journal pp.48--49, whose statement and proof archive independently checked. I checked the derived saturation proof here; I do not claim to have reread that primary proof in this audit.

Primary URL: https://www.math.mcgill.ca/labute/papers/kkl.pdf .

The all-weight integral-2 Newton/Hall induction remains open in this work. The finite results and the scalar Newton valuations do not by themselves prove it.

# Independent full review of the projective word-trace construction

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; reasoning effort not exposed. Date: 21 November 2026 UTC.

**Result: PASS.** Complete target report: agent_projective_word_trace.md, SHA-256 daac39f3a8e64d55b7305a56f96d7b3cda67e5cb8193e081174eb703a8e9c409.

All sections and all equations W1–W15 were read. I independently reconstructed the representation identity, algebraic projector, extension traces, exact twists and shifts, pure-complex convention, and Lefschetz maps. The already proved actual trace formula W1 is a stated input; this is not a new proof of all F43 generator calculations. A separate generated-fragment review is still needed.

## 1. Representation and coefficients

The elementary symmetric-square formula is correct for the actual representation W=V tensor 2s. Its character is D^s, while the doubled-weight character is (D-2)^(2s). Thus half the sum D^(2s)+(D-2)^(2s) is the character of Sym²(W).

Every tensor exponent in W5 is nonnegative since 2s<=L. The first and symmetric-square contributions combine with coefficients16+4=20 and4, leaving the stated middle16 term. The resulting character is exactly W1.

All constituent highest weights have even parity. The characteristic-zero irreducible SL2 characters are centered strings with spacing two; a nonnegative sum of such nested strings gives symmetry and unimodality in v². The report correctly does not assert unimodality after inserting zero coefficients at odd powers of v. At s=0, the symmetric square of the unit is the unit and the total is40 copies of V tensor2L.

## 2. Geometry and the actual projector

X_d is smooth projective of dimension2d. Exchanging two blocks of2s coordinates uses exactly4s coordinates and is a product of2s transpositions, leaving2L-4s coordinates fixed. The construction is defined over the original finite field in every characteristic.

Because the involution squares to the identity, half the sum of its graph with the diagonal is an idempotent under correspondence composition. For an involution, the graph-versus-transposed-graph convention causes no ambiguity. Rational coefficients, rather than an assumption about the characteristic, allow division by two. No assertion about a quotient scheme's smoothness is used.

The Chow-motive image exists in the stated pseudo-abelian category. Its realization is the invariant subspace degree by degree. The report explicitly lists the unequal centering shifts for the two different dimensions, instead of suggesting that a common shift of W9 produces W8.

## 3. Trace and actual Tate multiplicities

The product cohomology basis consists of squarefree products of2d divisor classes. A degree2j class has eigenvalueQ^j. The twist(d) multiplies byQ^-d; the shift[2d] changes the degree but not its parity. This gives D_n^d.

The permutation acts on the subset basis without signs. Fixed coordinates contribute1+Q and paired coordinates contribute1+Q². Its centered twisted trace is therefore Q^-L(1+Q)^(2L-4s)(1+Q²)^(2s), which equals D_n^(L-2s)(D_n-2)^(2s). Averaging with the identity and taking the stated16,16,8 direct sum gives W1 at every extension simultaneously.

Orbit sums form an actual basis of the invariant space in each degree. Frobenius is already scalar on the entire degree, so the projector image is an actual sum of Tate lines, without a hidden arithmetic Jordan or integrality problem. This also explains the denominator two without appealing to a merely formal division of a coefficient count.

## 4. Purity and hard Lefschetz

For the centered complex K_d, cohomological degree2r comes from ordinary degree2(r+d) with twist(d). It is exactly Ql(-r) with the stated binomial multiplicity. Its weight is2r. Odd cohomology vanishes. The projector and direct sums preserve this statement.

I reread BBD5.1.8, printed pages126–127, in the local primary-source text. Its equivalence between pure complex weight w and cohomology weight w+i applies at a point, where the local smoothness conditions in the stated equivalence are automatic. Thus pure complex weight zero is correct; calling the total ungraded Weil representation weight zero would be false, and the report explicitly distinguishes these.

I also reread the hypotheses and complete statement of BBD5.4.10 on printed page144: projective morphism, relatively ample first Chern class, and pure perverse input. The product here is smooth projective, so its shifted constant intersection complex is an allowed input. The product line bundle is ample and invariant under the coordinate exchange.

The hard-Lefschetz exponent2r in W14 is correct: the underlying ordinary source degree is2d-2r and the target degree2d+2r. The Tate twist(2r) makes this a Frobenius-equivariant map. Commutation of the ample class with the involution implies that the isomorphism and its inverse preserve the invariant spaces. Each block has the same centered degree convention, so the block diagonal operator gives the asserted hard-Lefschetz isomorphisms on the whole direct sum.

The injectivity argument below the center is correct, and combined with symmetry gives the second proof of unimodality. The direct tensor-product sl2 calculation gives a valid special-case check without claiming a new proof of the general BBD theorem.

One typographical correction was requested: W14 writes eta_d with exponent “,2r”. The comma should be removed or made a spacing command. The intended exponent2r is mathematically correct.

## 5. Dimension and limits

At v=1, the last term is4 times4^(L-s), and the middle term is16 times4^(L-s), so the total dimension is20*4^L+20*4^(L-s), as claimed. In particular the realization varies with the word; it is not a counterexample to the obstruction for one common finite Weil space in F42.

The construction depends on(L,s), exactly as does the trace polynomial. The report does not supply or claim an algebra action, concatenation compatibility, a distinguished canonical basis, or entrywise hard Lefschetz for all positive action coefficients. The counterexample D-2 with coefficient sequence(1,0,1) in v² correctly prevents such an entrywise conclusion in the chosen basis.

## 6. Primary locator check and review scope

Milne's original author PDF https://www.jmilne.org/math/CourseNotes/LEC.pdf was reopened as version2.21,22 March2013, retrieval turn866609695view0. Theorem23.2, printed pages139–140, was read again via turn866609695view1; its free cohomology basis and projective-bundle hypotheses apply. The report's Example16.3 locator is consistent with the earlier inspected source ledger.

BBD5.1.8 and5.4.10 were read from the local primary text corresponding to the available original PDF. These are checks of exact statements, conventions, and applicable hypotheses; the entire general source proofs are not claimed reverified.

All new special-case algebraic and geometric deductions in this report pass independent reconstruction. The geometry gives an explicit word-dependent coefficient motive and centered Weil complex; it does not identify the original nonstandard action with these correspondences.

## 7. Fresh check of the added summand-preservation obstruction

The updated report SHA-256 6a1f4f17c7fda9d3cb69e941e856112914143a54e35e09b32d830103808c2111 fixes the W14 exponent typo and adds W16–W17 and the following argument in Section6. I read the complete addition and independently reconstructed its proof. **PASS.**

For the actual right-row matrices on N(a), P1P2 has diagonal entries0 and a², so its trace is a². At a=D-2 this is v⁴+2+v⁻⁴. Any characteristic-zero SL2 irreducible with weight4 has even highest weight at least4 and therefore also has weight2. An actual representation cannot have weight4 multiplicity positive and weight2 multiplicity zero. Four copies retain this contradiction.

The selected sector projector is an actual regular commutant endomorphism: the regular direct-sum decomposition from F21 already gives it by conjugating the block projection. This does not place it in the nonsplit regular right algebra. Its inserted full-module trace is exactly four times the rank-two trace.

In the proposed matrix-kernel framework, entries are actual SL2 representations and composition is a finite direct sum of tensor products. Hence every entry of a composite is still an actual representation, and so is the direct sum of its diagonal entries. Its character must equal the trace of the product character matrices. A simultaneous change of basis leaves that scalar trace unchanged, giving the contradiction with W17 in every basis.

This proves exactly the stated summand-preserving restriction. The report correctly leaves open kernels that omit that projector, virtual or signed entries, other categorical operations, and the already constructed word-dependent motive.

## 8. Complete generated-fragment match

The entire finding_F45.tex, SHA-256 763592f7e06e94366e8831a88174ae1a91d0ddd2ec2d7d8f983ff6dbbb9188f7, was subsequently read from its opening subsection through its separate Part III paragraph. **PASS.** It preserves every reviewed proof and qualification, including W16–W17, the correct exponent2r, rational coefficients in characteristic two, unequal centering shifts, and the distinction between a pure complex and its mixed ungraded Weil realization. The archive paragraph attributes only primitive-projector and Lefschetz language to the inspected scans, not the new construction or polarization.

The later framework-only addition of SGA5 III4.7 was read in its complete final paragraph and passes as a trace-formula framework reference. Current fragment SHA256: b6be746c9ca4555ec33b4686b9d31d88e8aab9acb9248703371083c51d9771aa. The paragraph continues to distinguish the explicit projective construction and polarization from the historical archive language. No new mathematical assertion was introduced by this source addition.

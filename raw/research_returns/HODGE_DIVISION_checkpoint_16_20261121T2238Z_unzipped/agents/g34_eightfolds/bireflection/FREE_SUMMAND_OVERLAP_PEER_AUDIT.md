# Independent whole-proof audit of SF-E825

**Verdict: PASS in the stated local-model and determinant-condition scope.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. Actual clock record: **2026-11-21 19:43:44 UTC**. The complete proof reading, independent symbolic computation, and source reading described below were finished before this record time.

The entire frozen draft `agents/sixfolds/rm_free_summand_overlap_draft.md` was read, including every statement, proof, and scope paragraph. Reviewed SHA-256: `34af017d1f0c49a56b9924c68b923052afc003ba953e62e1ff55f6d811079783` (428 lines). The author's complete certificate was also read. The result is a necessary first-overlap determinant condition. It is neither a universal exclusion of the positive-determinant case nor a construction of a semiregular seed.

## 1. The actual bundle on the first infinitesimal neighborhood

The map ell(aI+vb)=a+bv modulo I squared is well defined on the actual unit module F, using the previously proved description of End(F), and is multiplicative. The two displayed free-factorization identities show that every FF map factoring through a free module maps to zero. Thus the full block formula is a unital ring homomorphism End(F^r plus R^s) to M_r(R/I squared), including the free off-diagonal terms of a product.

I checked the potentially delicate line-frame convention. The standard comparison for f_j=t f_i and g_j=t g_i is tI on F generators, with higher lifts t cubed I and t to the fourth. It has identity action on the hull when the hull rows are expressed in their respective frames. One first removes these fixed standard comparisons, then applies ell to the actual transition automorphisms of M. Conjugation by the standard comparisons identifies the ell maps because the row b rescales by t inverse while v rescales by t. The fixed comparisons themselves obey the cocycle relation. Therefore the resulting matrices satisfy an exact cocycle modulo I squared and define the claimed vector bundle Qtilde on S2. This construction does not add an unintended L twist. Reduction modulo I is the intrinsic action on the canonical defect Q. Changes of local identifications give ordinary changes of bundle frames.

## 2. The trace after arbitrary free mixing

I reopened the complete local endomorphism and positive-Ext calculation in UG. The decomposition Ext1(F,F)=U plus V, the annihilation by I, and the zero action of the nilpotent ideal J on both sides of positive Ext are valid in their stated module convention. Ext1(F,R)=R/I, represented by cu, while Ext1(R,F) and Ext1(R,R) vanish. Postcomposition of cu with an arbitrary map R to F exhausts U. The reverse positive-Ext composition is zero. Consequently cyclicity requires U to be killed.

Taking the ordinary matrix trace of only the diagonal FF V components is cyclic under every degree-zero endomorphism. FF terms use the scalar matrix modulo I, nilpotent FF terms act trivially, and the extra off-diagonal terms land in U. This checks every block case. Under the standard frame comparison the two V coefficients transform by t, giving exactly O_S(D) squared. The intrinsic sheaf trace therefore exists without an invariant summand or a global decomposition of M. No trace on the entire derived self-Hom object is inferred.

## 3. The local deformation and the coefficient seven halves

I independently recomputed the star product with arbitrary constant bivector coefficients in four formal coordinates. The correction d_epsilon=vw+(3/2)epsilon P I cancels the complete first-order square. The reduction-exact free complex gives a flat cokernel over the dual numbers by the stated cycle-lifting argument; adding free star modules preserves it.

For the line-frame comparison, both obstruction components and their cycle identity check exactly. Normalizing the first by the inverse source comparison gives U coefficient 1/2 and V coefficient 7/2. The inverse relation between the section coefficients t and the L transition function gives the negative sign in the fixed-unit contribution. Thus the coefficient and sign in E825.16 and E825.3 are consistent.

## 4. Variable b and the actual boundary calculation

The original degree-count explanation was insufficiently explicit for an independent check. I derived the exact derivative terms and sent them to the author and parent. The author independently reconstructed the same formula and inserted E825.13a. The final wording correctly starts the preliminary calculation with b constant, not merely constant in normal directions.

For unrestricted functions b1 and b2 of all four coordinates, all terms differentiating b are exactly (1/2)Aw+vB, with c, A, and B as displayed in E825.13a. Every entry of A and B lies in I. The first term belongs to the actual boundary submodule u(IF), and the second is zero in F because Iv=0. Thus their disappearance is an Ext statement, not a truncation heuristic. The surviving V term is the derivative of a+bv modulo I squared, as claimed. My symbolic certificate retains all tangential and normal derivatives and verifies this identity exactly.

## 5. Normalization, determinant, and choices

After multiplying an obstruction by the inverse of an arbitrary automorphism, the extra term returning to FF factors through a free module and lies in U. The remaining FF scalar matrix is the inverse of ell modulo I. This is valid even with free mixing because ell is a ring homomorphism on the full endomorphism algebra. Its matrix trace is therefore the ordinary logarithmic determinant derivative for each of the two derivations R/I squared to R/I.

The same cyclic trace kills the change produced by changing a local module deformation: after normalization it is the trace of a commutator. Changes of nullhomotopies give Cech coboundaries. This replaces, rather than assumes, the stronger centrality used in the earlier pure-unit case.

## 6. The first-overlap map and the balanced consequence

I reread the relevant complete truncation and Cech construction in E824. Since the self-Hom complex has cohomology sheaves only in degrees zero, one, and two, the first truncation identifies H2 of the lower truncation with the kernel of the local Ext2 edge map. The second supplies its map to H1 of Ext1 with kernel the image of H2 of End. No degeneration of a spectral sequence is needed. Its Cech representative is precisely the lifting obstruction for transition isomorphisms. Applying the cyclic trace gives E825.16.

For B=0, the two balanced Hochschild classes annihilate the entire character, not just one Chern component. Published BF composition/evaluation together with the supplied invariant-to-ordinary compatibility gives ordinary Ext2 vanishing under the stated semiregularity hypothesis. The H2(O) component is in the image of H2(End), hence disappears under kappa.

For rational B, the multiplication isogeny makes its pullback integral. Etale Atiyah functoriality and line tensoring transport ordinary evaluation vanishing; no preservation of semiregularity or of a finite action under pullback is asserted. The pulled-back smooth complete intersection is connected by the negative-ample Koszul resolution and hence integral. The determinant of the actual defect bundle adds r times the line twist. Finite etale trace injects the relevant coherent cohomology pullback, so descent gives the exact rational identity on X.

## 7. Nonvanishing and the simultaneous kernel

The definition of Psi on Pic(S2) is independent of lifted units because {I squared,I} is contained in I, compatible with normal frames, and additive by the logarithmic product rule. For line classes from X it is the Atiyah class followed by the bivector and normal-bundle map.

The complete Koszul sequence and ample/negative-ample vanishing give H1(S,L restricted S)=H2(X,O) squared. I reconstructed the triple-overlap coboundary of the lifted normal components: it is f times, respectively g times, the common contraction of the two line Atiyah cocycles. This proves the kernel equivalence E825.18. The harmless common Cech/Atiyah scalar does not enter the coefficient 7/2 identity.

The independent exterior calculation uses all sixteen entries of a general (1,1) matrix. The simultaneous kernel has exactly codimension ten: the two separate diagonal traces and all eight mixed-block entries vanish. Each Psi_pi(L) is nonzero, and theta cubed paired with C is proportional to the total trace. The flat-determinant exclusion and the stated positive-degree consequence therefore follow in exactly the extension-to-X scope claimed.

## 8. Independent exact certificate

`audit_free_summand_overlap.py` imports no author code. Its actual run passed in **0.601104 seconds**, with output `audit_free_summand_overlap.json`. It checks:

- all six independent bivector coefficients and the full overlap cycle;
- the coefficients 1/2 and 7/2 with their normalization;
- two unrestricted variable functions b, retaining every formal derivative;
- the exact derivative-boundary formula and the derivative of ell;
- free-factorization cancellation and the full FF product with free terms;
- a generic rank-three determinant derivative;
- the full sixteen-variable exterior kernel, its codimension ten, nonvanishing, and degree identity.

This is a symbolic check of explicit formulas. It does not computationally prove global descent, categorical Hochschild compatibility, a finite action, or a semiregular example. Those claims are assessed by the complete mathematical reading above. No TeX compilation is claimed.

## 9. Source boundary

The complete BF2008 Theorem5.1.3 and proof, Proposition5.2.2 and proof, and Corollary5.2.3 were freshly read in the retained original author text, numbered pages24–27. BF2008 Proposition6.2.1, Theorem6.4.2, and the complete Proposition6.4.4 proof retain the earlier full primary-source checks recorded during E819/E822. Publication: Advances in Mathematics217(2008),243–281, DOI10.1016/j.aim.2007.06.013; author copy https://arxiv.org/pdf/math/0606730 . Mumford's abelian-variety vanishing input retains its earlier checked scope at section16, printedpages150–153. The supplied S21 invariant evaluation and ordinary forgetting paragraphs retain their supplied status and exact locators; they are not relabelled as a new refereed theorem. No unrefereed032 proposition, Markman theorem, or Severn theorem is used here.

The positive-degree determinant case, rank-dropping gluing, other local models, singular support, and arbitrary perfect complexes remain open exactly as stated in the final paragraph. No defect was found in this frozen proof.

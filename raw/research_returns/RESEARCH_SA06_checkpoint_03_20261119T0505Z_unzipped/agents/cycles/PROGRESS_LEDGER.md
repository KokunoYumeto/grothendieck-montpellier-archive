# Cycles agent progress ledger

## 2026-11-19 03:18 UTC

This is a checkpoint-state ledger, not the user's three-hour no-progress review. The full task remains active.

| Open row | Current gate | Movement in this run |
|---|---|---|
| C.1 higher classification | Lefschetz maps on higher Griffiths groups plus algebraicity of inverse in homological quotient | Exact divisor cokernel and product counterexamples established; no general classification |
| C.2 | Algebraic lift under Gysin, global pencil reduction with correct field | Affine-vanishing/localization confusion removed; precise conditional positivity proof supplied |
| C.3 | Kernel/cokernel of L on Griffiths; strict local Chow restriction | Exact snake-lemma sequence; J1 criterion and explicit K3 punctured-cone counterexample |
| C.4 nonprincipal low dimension | Actual integral Jacobian-product splitting | Characterization proved; ppav cases and modern counterexamples identified; all-prime positive-characteristic theorem opened |
| C.5 structural4bis=>5 | Relating kernel on arbitrary X to kernels on all abelian parameters | Other missing implication proved; field truth table fully settled |
| E.3 charp | ℓ-adic AJ descends through N^i on families with correct cohomological realization | Existing torsion-only shortcut identified as insufficient |
| E.3 complex converse | Injectivity of P^i_Q→J_a^i_Q | Exact rational equivalence proved; integral finite-component issue separated |
| LeadE4 integral | Torsion components of kernels and difference from rational equivalence of assertions | Rational formulation established; no integral assertion claimed |

E.1 exact classification has changed to proved. R10's denominator claim has changed to refuted with the exact exponent replacement. Fpbar chain truth table and the complex explicit rectangle have changed to proved/refuted, respectively.

## 2026-11-19: subsequent gate movement, C.1f

The universal A-surjectivity row is now settled over C for every (n,i): universal truth holds exactly for i=0 or 2i=n. For 1≤i<n/2, C.1f constructs finite source and infinite target for every ample class. The key new step is an iterated incidence blow-up that shifts the sole Griffiths group upward while preserving an ambient smooth projective variety with Tate Chow motive. The preceding simple-product attempt failed for i≥2, and that failure is retained in the proof and CHECK_EVENTS.tsv.

The exact Chow formula was checked in the opened primary paper Jiang2023, Theorem2.8(3); its four maps were written explicitly. Projective-bundle motives were checked in Stacks Lemma45.6.1, Tag0FGQ. The root and frobenius agents also checked the induction within this same model/run. Seven stages, 49 degree pairs, and the universal local Rees-ideal elimination passed the recorded finite checks. No priority claim is made, and the general statement follows from induction rather than those finite checks.

The remaining C.1 gate is now the full higher A′/A″/B classification and requested independent Griffiths calculation. These are narrower than the first checkpoint's broad universal-surjectivity gate.

Applying the same incidence induction to the explicitly given Fermat quartic K3 settles the universal J-surjectivity classification in C.3d. For each n≥2i≥2, the resulting n-fold has J^i=0 but J^{n+1−i}≠0, whereas the remaining exponent-zero case is the identity. Forty-nine formal degree checks passed. Thus the C.3 gates are now higher injectivity, individual-variety higher kernels/cokernels, and strict local punctures.

## 2026-11-19: subsequent gate movement, E.3e–f

The general positive-characteristic direction of Theorem3.1 is now proved. The decisive repair is to specialize one entire ℓ-primary torsion relation in N^i, with its finite rational-equivalence data, instead of trying to assign Bloch values separately to nontorsion generators. The specialized Albanese comparison is an isogeny of degree prime to ℓ because the integral H1 map is an isomorphism of lisse sheaves. Every specialized parameter zero-cycle is torsion; Roitman kills its ℓ-primary component, so the total relation is both prime-to-ℓ torsion and ℓ-primary and therefore zero. Bloch1979 Propositions3.5,3.8,3.9 and Theorem4.2 complete the argument. The root and frobenius agents independently reviewed this proof; the frobenius agent independently opened those exact primary locators. This is a same-model/run check, not independent-model verification.

For an integral correspondence, rational vanishing of the transpose already implies integral vanishing because its target is H1 of an abelian variety, which is free. The integral hypothesis u_Z=0 is essential: E.3f gives a smooth elliptic curve over F5bar with u_Z⊗Q=0 but identity cohomological action. The remaining E.3 gates are the complex intermediate-codimension converse and the unqualified integral formulation of LeadE4. No identification of P^i with an algebraic representative, and no standard conjecture for middle cohomology, enters the forward proof.

## 2026-11-19 03:57 UTC: explicit line proof, C.1g

The incomplete independent quintic-counterexample row has changed status. C.1g gives an explicit113-parameter equation over Q(t_e), two fixed skew lines, and a complete proof that their difference has infinite order modulo algebraic equivalence. We prove generic inversion using the Calabi–Yau contraction isomorphism and the opened Griffiths1968 period differential. A separate explicit cyclic quintic, built by interpolation through two geometric generic points of a Fermat plane quintic, has non-torsion Abel–Jacobi value. Proper analytic zero loci and finite-data spreading then prove the assertion on the specified geometric generic fibre, and under every embedding into C. This avoids treating analytic loci as Qbar-defined without proof.

The finite script checks114 monomials, both normal-derivative maps, interpolation, coordinate determinant and blow-up ideal charts. A serialization-only failure was corrected and retained in its run log. Root independently read and checked the entire proof, with a refinement to apply Baire on one ball in any chosen Zariski open; that refinement is incorporated. Moreover C.1f needs only one nonzero Griffiths class: source Griffiths vanishing and hard Lefschetz ensure its image misses the nonzero target Griffiths group. Thus C.1g supplies completely specified universal-A counterexamples for every1≤i<n/2; Clemens is retained only for the stronger infinite-dimensional assertion. Parent independently supplied the C.2 pencil/critical-dimension gate movement, and those input files are integrated without duplicate metadata ownership.

## 2026-11-19 04:58 UTC: checkpoint03 movement

C.1h–i now close all universal A′/A″ ranges: the generic Gysin image equals the ample-class image, and explicit degree4c+2 complete intersections in split quadrics supply every non-top counterexample. The proof uses opened effective Nori connectivity, with exact Nagel hypotheses independently checked by root and frobenius. C.1j identifies the strict-positivity gate as the middle Griffiths kernel; it does not pretend that surjectivity counterexamples refute positivity. C.1k classifies the universal finite-rank and cycle-class assertions. C.1l–m give nonzero Jacobson radicals, including a surface C×C with C the specified geometric generic plane quartic. The surface modified-diagonal nonvanishing is a clearly identified classical input, transferred to the specified generic equation by specialization; all-b sandwich vanishing, not mere nilpotence, proves the radical assertion.

Root-owned C.2e–j now include the full extension-stable A′hom⇔Ahom argument and conditional Weil/image theorem. Root-owned C.3e–g close the strict-local passage and give the explicit Fermat quartic local Gysin/restriction failure as well as all proposed high-range local finite-rank counterexamples. This agent independently checked those proofs. Frobenius-owned C.4h–q sharpen the low-dimensional scalar bounds to gcd(2,delta) and gcd(6,delta), and identify the exact limit of curves supported in proper abelian subvarieties. These owned fragments are integrated; their result metadata remain with their authors.

E.3g proves integral pointwise abelian parameterization and regular-map annihilation of N. E.3h uses the opened Ottem–Suzuki finite Walker isogeny to refute integral equality of Albanese and ordinary AJ equivalence. The initially tempting inference from a single finite-kernel point to a whole zero-cohomology family was rejected in E.3i. The extra diagonal-decomposition proof E.3j then establishes the integral family converse on the same fourfold, whose CH0 is supported on an elliptic curve. Thus E.3k actually refutes the literal integral LeadE4 biconditional; its rational formulation remains proved.

E.3l strengthens the result: if CH0(X) is supported on a surface, P^{n−1}(X) is canonically the Walker Jacobian group, integrally. A uniform multiple of the identity factors through Pic0 of resolved support surfaces and Albanese groups of resolved boundary divisors. Ordinary AJ functoriality bounds the exponent of its quotient kernel. ACMV Theorem2.3, opened verbatim by this agent and independently by root, makes the whole Walker kernel divisible. The divisible quotient of bounded exponent must vanish. Root independently checked E.3l, and frobenius independently checked E.3j–k. The remaining general intermediate-codimension family converse has not been inferred from regularity, a universal representative, or Walker's isogeny-lift property.

A countably-constructible-parameterization route from the rational family converse to the integral family converse is currently an investigation only. It needs a complete finite-type parameterization of N-relations, including smooth projective parameter varieties, relative Albanese conditions, intersections, and rational-equivalence witnesses. No result depending on that unfinished construction has been marked proved.

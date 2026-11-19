# Cotes 47, 54 and 44: synthesis for SA19

## Scope and chronology

This workstream reads all 37 assigned entries, MPL_16+47+54+44#44–79 and #85, against their actual passages. The index’s cote 44 label is package metadata: entries #44–64 concern cote 47, #65–70 concern cote 54, #71–78 concern cote 44, and #79 returns to a reused sheet in cote 54. Entry #85 is a bibliography. All 28 pages in these three cotes have been read, including covers, canceled arguments, reused typescripts and editorial commentary. The page ranges are in reading_coverage.tsv.

There are no second-pass corrections for these three cotes in the supplied package; that is not a gap. No archive scans are available, and no diplomatic reading has been changed. Mathematical alarms are recorded separately.

Only the Serre letter in cote 44/8 is explicitly dated **Bures, 12 August 1964**. The programme leaves, Fourier manuscript, duality manuscript and reused sheets are not independently dated by this audit. Publication matches and later receipt or arXiv dates do not date an undated leaf. The CSG transcription of the letter appeared in April 2024; the letter is not a 1964 publication.

## Cote 47: a real Fourier proof and a precisely unfinished comparison

The manuscript starts from perfect complexes on an abelian scheme and a normalized family of degree-zero line bundles. Its first product statement sends Pontryagin convolution to tensor product. The earlier note calls this unproved, but cote 47/4 supplies the base-change, projection-formula and Künneth calculation and ends with “cqfd.” The general marginal extension to three kernels gives binary compatibility, without separately specified associativity and unit coherence (SA19-201–202; CL-SA19-401–402).

The square of the transform evolves from identity to inversion, then to inversion with determinant line and shift:

\[
\Phi_{A^\vee}\Phi_A(F)\simeq(-1_A)^*F\otimes\pi_A^*\det(\operatorname{Lie}A)[-g].
\]

The earlier \(K_0\) formula does not visibly receive the line factor, and an old identity target survives inside the proof. Mukai’s field theorem and Laumon’s relative theorem establish the corrected result. The source’s particular proof still depends on a zero-fibre comparison it explicitly leaves unfinished (Mukai, 1981, Theorem 2.2; Laumon, 1996, Theorem 1.2.4 and Lemma 1.2.5; CL-SA19-403–409).

The audit redoes the regular-zero-section Koszul calculation and separates it from the missing map check. Matching exterior-power dimensions does not show that the source’s constructed map is an isomorphism. The general kernel formula also needs the zero-section pushforward: omitting it loses the actual support and the derived intersection.

The section and translation formulas reveal a sign issue under an explicitly fixed convention. The exponential heuristic has a precise ample-field realization via Mukai’s isogeny pullback. Its displayed total Chern class is correct, but the following expanded coefficients have an extra factor \(\chi(L)\). For a product of complex elliptic curves and a line bundle of degrees \((1, 2)\), the actual \(c_2\)-degree is 1 while the literal expanded formula gives 2. The final integrality multiple nevertheless survives as a signed integer multiple of the actual Chern class. This separates a false expansion, a true restricted consequence and the stronger question of a Fourier operation on the whole integral Chow lattice (CL-SA19-413–417, 467).

Relative Riemann–Roch retains both source and target Todd factors in the reverse product formula. Their product with the determinant character is \(\operatorname{Td}(H^1_{\mathrm{dR}})\). Moonen’s Corollary 2.7(1) proves this class is 1 in its specified smooth-base setting; the separable-polarization assumption belongs to a stronger all-Chern-classes conclusion (Moonen, 2026). Convolution-to-intersection has no parity sign. Kleiman’s exact Lemma 2A12 and Remark2A13 do not confirm the source’s accusation of a missing sign, because they do not state the converse identity to which that sign belongs (Kleiman, 1968, pp. 377–378; CL-SA19-418–422).

The integral question remains scoped. Beckmann and de Gaay Fortman impose additional principal-polarization and symmetric-line-bundle conditions for some equivalences; Hasan et al. invert a factorial and retain characteristic-zero or liftability/base-change hypotheses. Neither verifies an unspecified integral “Gr” for every family (Beckmann & de Gaay Fortman, 2023, Theorem 3.8 and Question3.9; Hasan et al., 2025, §§3–5).

## Cote 54: duality, finite \(p\)-torsion and exact EGA counterparts

The tangent sequence of the universal vector extension of \(A\) is the Hodge sequence of \(A^\vee\). The manuscript’s variance is correct: invariant differentials on \(E(A)\) give \(H^1_{\mathrm{dR}}(A)\), while its tangent gives \(H^1_{\mathrm{dR}}(A^\vee)\). Coleman’s contravariant vector-group convention explains the distinction. Exterior powers give the Hodge-piece dualities, with the differential subscript on the \(B\)-side retained as an ink question (Coleman, 1998, Theorems 1.1 and 2.2(i), §4; CL-SA19-426–428).

The finite-group discussion separates the height-one Frobenius kernel, the full group scheme \(A[p]\), and the restricted Lie extension. Oda’s Corollary 5.11 answers the Hodge-extension reconstruction over a perfect field, preserving the Hodge subspace and semilinear \(F, V\). Cartier dual of a kernel and annihilator inside the full torsion pairing are different constructions. Oda records a June 1967 Harvard dissertation before publication in 1969 (Oda, 1969, Definition 3.5, Proposition 3.13, Theorem 3.19 and Corollary 5.11; CL-SA19-429–431).

The reused flatness material now has exact publication matches:

| Source passage | EGA IV₃ counterpart | Scope |
|---|---|---|
| Cote 54/4 generic-freeness corollary | Corollary 11.4.6, p. 147 | Exact irreducible, possibly nonreduced base statement |
| Original nilpotent Proposition 4.1 | Theorem 11.4.1, pp. 143–145 | Nilpotence is material; the flat-reduction variant needs finitely many tests |
| Invoked “4.1bis” | Corollary 11.4.4, pp. 145–146 | Universal ideal for flat/free base changes |
| Cote 54/6 Proposition A | Proposition 11.4.5, pp. 146–147 | Exact universal stratum and finite-cover freeness; published base irreducible |
| Nonnilpotent direction | Proposition 11.4.7, p. 147 | Published theorem adds equivalent-adic-topology hypotheses |

The source’s merely nonempty base in Proposition A follows by an explicitly separate noetherian-approximation/component-open argument. The canceled nonnilpotent amendment is false under the written hypotheses: \(A=k[t]\), \(I=(t)\), \(A_1=k[t, t^{-1}]\), \(M=k\) passes the reduction and test-algebra conditions but is not flat over \(k[t]/(t^2)\). Noetherianity and ideal separation alone do not rescue it. The exact EGA statements and proofs were read from the complete primary PDF; a flattening-stratification definition was not used as an existence theorem (Grothendieck, 1966, §11.4; CL-SA19-432–434, 458).

The last reused leaf’s locally finite hyperplane-arrangement assertions are checked directly. Its Bourbaki edition and authorship are not assigned without evidence.

## Cote 44: incidence is the strongest historical model

The programme and letter seek abelian varieties from algebraically trivial cycles, with endpoints, an odd-Betti-number bound, complementary duality, realizations, positivity, heights and Lefschetz restriction. The letter admits that “Albanese equivalence” is not well identified. This prevents identifying the proposed variety with a modern object merely from matching dimensions.

The closest later model is the **Picard/incidence quotient**, because the letter actually constructs divisor correspondences from cycle families. Saito proves the all-codimension dimension bound and incidence representative and credits Grothendieck’s argument. Kleiman explicitly identifies the bounded Picard-family mechanism as an unrecorded 1964 observation of Grothendieck. This supports the comparison historically without recovering the missing integral kernel definition (Kleiman, 1971, pp. 446–447; Saito, 1979, Proposition 3.4 and Theorem 3.6; SA19-225–226; CL-SA19-440–442).

Universal regular representatives and algebraic Abel–Jacobi images remain separate. Kahn repairs the codimension-two regular-representative argument; Achter, Casalaina-Martin and Vial give a functorial framework and restricted integral realizations. Ottem and Suzuki exhibit a nonuniversal codimension-three Abel–Jacobi map on a particular complex fourfold. This does not refute the incidence construction or all representative existence. The 2025–2026 updates checked here construct torsors from given regular homomorphisms or motivic descriptions of their kernels; they do not settle universal existence in all codimensions (Kahn, 2021; Achter et al., 2023, 2026; Ottem & Suzuki, 2020; Hernández & Pelaez, 2026).

Saito’s complementary comparison is an **isogeny**, not the literal canonical integral duality. The Tate wording has another logical distinction: an abstract subquotient that is finite free over \(\mathbb Z_\ell\) already embeds noncanonically by lifting a basis. A substantive stronger conjecture must preserve additional geometric structure, unspecified in the letter. Modern equivariant correspondence maps retain exact codimension and prime restrictions (Achter et al., 2023, Proposition 8.2; CL-SA19-443–447).

The incidence construction has four separate steps: divisor degree, symmetry, quotient descent and positivity. The first two are formal. Full-kernel integral descent fails even before positivity. For \(X=T=E/\mathbb C\), \(\operatorname{End}(E)=\mathbb Z\), \(m=1\) and \(z=2c_1(P)\), the symmetric homomorphism is \(-4\). Quotient by its full kernel is \(q=[4]\); integral pullback multiplies a homomorphism by 16, requiring \(-1/4\) for descent. A projective-space factor extends the example to every middle dimension. The reduced neutral abelian radical or rational coefficients are different formulations, explicitly labelled as this run’s refinement (CL-SA19-449–450, 459).

The factor-two statement is valid: graph pullback of Poincaré for symmetric \(f\) gives a line bundle with homomorphism \(f+f^\vee=2f\). It supplies a Néron–Severi class, not ampleness. The primitive-decomposition warning remains substantive. The letter says only that **unspecified unproved assertions** would reduce Hodge positivity to the proposed Jacobian positivity; it does not explicitly call them Lefschetz assertions. Peters’s 2026 primitive-algebraicity criterion gives a conditional comparison. The Caibar–Clemens preprint was finally withdrawn on 19 February 2013 because of an error in its last theorem’s statement and is not a solution (CL-SA19-448, 461–463).

The height programme remains partly formulated. The divisor formula uses vertical corrections and normalization; Künnemann’s higher-cycle result concerns abelian varieties over number fields. Neither is the unrestricted pencil theorem. Weak Lefschetz directly proves the intersection-side vanishing outside the balanced middle case, while the height side needs additional realization data. The finite-kernel phrase in the middle clause of Theorem 6 is crossed out and remains withdrawn (Ulmer, 2014, §4.3 and errata; Künnemann, 2001, Corollary 1.7; CL-SA19-451–453).

If \(\tau\) means torsion-algebraic equivalence, numerical=\(\tau\) is true for divisors and false in higher codimension. FGA records Matsusaka’s divisor theorem; Clemens gives non-torsion homologically trivial codimension-two classes on a very general complex quintic threefold. This conditional refutation does not decide the symbol or authorize adding a divisor qualifier (Grothendieck, 1962, §4, p. 242; Clemens, 1983, Theorem 0.2; CL-SA19-454, 460).

## Other reused mathematics

The completion argument is valid in its precise noetherian graded setting. The ungraded module \(k[x]/(x-1)\), killed by completion at \((x)\), is a boundary test rather than a counterexample to graded faithfulness. The undefined “TF” and cancellation order remain reading questions (CL-SA19-455).

The root draft omits a genuine hypothesis. The roots

\[
\{\pm e_1, \pm e_2, \pm2(e_1+e_2), \pm2(e_1-e_2)\}\subset\mathbb Z^2
\]

are finite, reduced on rational lines, generate the lattice and are preserved by their integral reflection matrices. Yet the coroot of \(2(e_1+e_2)\) is \((1/2, 1/2)\). The program verifies every displayed hypothesis. Assuming primitivity repairs the inference, but the sheet claims primitivity as a consequence. Its alternative paired-lattice description has only rational perfection, weaker than the perfect integral dual lattices of a full root datum (SGA3, Exposé XXI, Definition 1.1.1; CL-SA19-456–457, 464–465). The subsequent mutable “copoids radiciels” terminology cannot be identified without its definitions; exact-phrase searches found no original draft (CL-SA19-466). Reused and canceled material is not promoted into active Jacobian conjectures.

## Counts and verification

Worker records contain **37 entries, 32 items, 63 claim records, 17 problems, 48 reading alarms, 13 checked links, eight ranked directions and 44 references**. Verdicts: **25 kept, seven corrected, five merged**. Classes: **A 3, B 29, C 21, D 0, E 7, F 3**.

Four claim records are separate refinements or historical specializations of this run: **CL-SA19-459, 460, 465, 467**. Excluding them leaves **59 source-targeted claims**, with **A 3, B 26, C 21, D 0, E 6, F 3**. CL-SA19-458 retains the earlier deleted nilpotent formulation and labels the reconstruction of its invoked universal-ideal consequence. Root integration may merge items across packages while preserving these origin distinctions.

There are **194 check events and 63 claim-specific research-log rows**. Every claim has a searched fate, source-status check, references and dated confidence. Bibliographic “verified” means an opened URL; annotations distinguish theorem reading, metadata and withdrawal verification. The original Lieberman chapter remains explicitly unverified. Reading a theorem is not labelled an independent proof. Exact certificates, hypotheses and independent arguments are preserved in computations.md and its executable output.

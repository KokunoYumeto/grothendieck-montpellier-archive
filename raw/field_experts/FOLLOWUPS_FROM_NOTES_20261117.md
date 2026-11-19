# Follow-ups from the research notes of the returned transcription packages (17 Nov 2026)

Written by the follow-ups reader, Claude Opus 5.5 at effort max, launched 17 Nov 2026 by the main session (Claude Opus 5.5 at effort max). The notes read are those of our own transcription runs, GPT-6 Astra (ChatGPT Pro mode). Source: `grothendieck_archive_transcription_20261110/notes_crosslinks_20261117.tsv` and the `<package>_notes.md` files of the returns; working files and scripts in `field_experts/followups_work_20261117/`.

## Scope and method

- Selection: every row of the crosslinks table whose kind starts with "own idea" or "unpursued implication": **1669 entries in 51 packages**. The brief's "about 480" is the count of rows whose kind cell is exactly "own idea." or "unpursued implication." (482); the other rows are the same kinds with more text in the kind cell (for example "own idea. **confidence:** high").
- Entries 1-1125 (in table order) were read in full, from a compressed copy that drops only search logs, file paths and bare kind labels and cuts verbatim quotations to 160 characters. Entries 1126-1669 were read as digests (header, location and the first 260 characters), with the full text read wherever the digest pointed to a possible research item. This change was made at about 715k tokens of context to finish within the window; the rule for each entry is recorded in the working folder's STATE.md.
- Verdicts: (a) research item, stated as an item to prove or refute with cote and scan, assigned to a cluster and ranked 1 (strongest) to 3; (b) edition matter for the second pass (a reading, a convention, an error or gap of the page, a dating fact, a provenance lead, a check the edition should record, such as the root-system tables of cote 33, or a precise cross-reference the companion should carry); (c) nothing further (a comparison that changes nothing, a check that confirms the page, a known result, or an idea folded into a research item elsewhere, which the statement names as "folded into @n").
- "@n" is the entry's number in table order; the TSV gives package and entry id for every number.
- Michel Hua's project (github.com/Commutator-IO/grothendieck-project) is credited wherever a note uses one of its findings.

## Summary

| Verdict | Entries |
|---|---|
| research item | 41 |
| edition matter | 495 |
| nothing further | 1133 |
| total | 1669 |

| Cluster | Research items | rank 1 | rank 2 | rank 3 |
|---|---|---|---|---|
| ANAB: Anabelian successor / points as sections (LM6, SECTIONS_OVER_Q, A1) | 2 | 0 | 1 | 1 |
| GT: GT tower follow-up (EXIT_TOWER, GT_TOWER_CHECK, five-point diagram, structure at infinity) | 16 | 0 | 7 | 9 |
| DER: Dérivateurs successor (localizers, totality, homotopy) | 3 | 0 | 3 | 0 |
| GS: Group schemes and descent (LM1 line) | 1 | 0 | 0 | 1 |
| CRYS: Crystals and de Rham | 2 | 0 | 1 | 1 |
| MOT: Motives and tensor categories | 6 | 0 | 2 | 4 |
| NEW-TAME: New archive cluster: tame topology, stratified spaces and classes of functions (cotes 39, 120, 121, 150, 151; Esquisse §5-6) | 6 | 0 | 3 | 3 |
| NEW-PSEUDO: New archive cluster: pseudoline arrangements and the surface of relative positions (cote 154; Esquisse §8) | 1 | 0 | 1 | 0 |
| NEW-FORMS: New archive cluster: networks, ficelles and forms (cote 156, 1986) | 3 | 0 | 1 | 2 |
| NEW-ANALYSER: New archive cluster: analysers, plethories, binomial rings (cotes 133, 153) | 1 | 0 | 0 | 1 |

Edition matters by package: MPL_105 9; MPL_106+107 3; MPL_11_002-042 15; MPL_11_043-058+56 17; MPL_121_001-048 5; MPL_121_049-073+153+155 26; MPL_131 11; MPL_133 11; MPL_136_047-094 7; MPL_136_189-234 7; MPL_142_001-093 28; MPL_142_094-122 10; MPL_144_001-061 22; MPL_144_168-184+148_001-028 7; MPL_145 4; MPL_146_001-099 26; MPL_146_100-134 1; MPL_147_003-047 9; MPL_147_048-137 13; MPL_147_138-190 4; MPL_148_029-072 7; MPL_14_002-044 12; MPL_150_001-043 7; MPL_150_044-084 2; MPL_151_032-075 10; MPL_152+120 4; MPL_154_077-126 2; MPL_154_127-176 15; MPL_156-1+156-2 12; MPL_15_087-138 3; MPL_15_195-228+18_002-017 5; MPL_16+47+54+44 21; MPL_18_018-062 6; MPL_2 4; MPL_31_002-051 11; MPL_33_002-049_chatB 20; MPL_33_002-049 11; MPL_33_098-146 8; MPL_33_147-181+34_002-017 12; MPL_36_002-052 7; MPL_36_053-085+39 17; MPL_43_094-142 12; MPL_57_271-315 7; MPL_60_036-070 9; MPL_62_002-050 14; MPL_84_097-145 5; MPL_84_146-193 2; MPL_90+91_002-018 2; MPL_91_099-143 3; MPL_93_002-046 10.

## Research items by cluster (strongest first)

### ANAB: Anabelian successor / points as sections (LM6, SECTIONS_OVER_Q, A1)

- **[rank 2] @770, MPL_14_002-044, B04.** Method for the open LM6 A.22 (full CM group): compare the conjugation action N → Aut(C) of the normalizer with χ∘p (cyclotomic character through the projection; the register excerpt gives only openness of p(N)) and apply Stix 2012, Definitions 26, 29, Theorem 30 and Corollary 31 (closed pro-ℓ subgroups contained in inertia recognized by an open normalizer image acting cyclotomically, using Hom_{G_k}(Z_ℓ(1), T_ℓA) = 0), to decide the existence or exclusion asked in LM6 A.22. Arises from cote 14, scans 007, 011, 041 ("motifs effectifs de poids i", "éléments de Frobenius").
- **[rank 3] @1404, MPL_43_094-142, A02.** Point-to-section Kummer compatibility in G.'s generalized-Jacobian bridge (cote 43, scans 113, 132-133): with base point b, modulus 𝔪 and j_b(x) = [x − b] in J_𝔪, prove that the abelianized class of the section of x relative to that of b is δ_n(j_b(x)) in H¹(K, J_𝔪[n]) under G.'s conventions; this is the step the 1983 injectivity argument needs (FLAGGED_149 B5, LM6 F.35).

### GT: GT tower follow-up (EXIT_TOWER, GT_TOWER_CHECK, five-point diagram, structure at infinity)

- **[rank 2] @435, MPL_142_094-122, R27.** G.'s recognition problem for the Galois image (142/090-100): conditions (a) rational points on covers, (b) kernel preservation by a suitable lift, the peripheral "structure à lacets" and the internal profinite conditions. Decide whether these conditions, strengthened by coherence of lifts across morphisms, fibre products and compositions of covers, characterize the automorphisms coming from G_Q, or give an element of the ambient automorphism group (GT̂ or Out) satisfying them that is not Galois; work hypothesis by hypothesis against Hoshi et al. 2025 (Thms A-C, arithmetic Belyi diagrams) and the finite-field model of Tamagawa 1997, Prop. 0.7. Cote 142, scans 090, 095-100.
- **[rank 2] @524, MPL_144_168-184+148_001-028, Q5c.** Prove the identification G. admits on 149/077-079 ("Je présume", "Je vais admettre"): at a boundary point where the pulled-back boundary parameter is uπ^μ, the source inertia maps to μ times the chosen generator κ_i (L_i = κ_i(T)), with μ the length of A/(I_f + I_q), compatibly with the finite Kummer root maps and with specialization; the local computation is done in our notes (144 N005.8), the global identification and specialization compatibility are not. Cote 149, scans 077-079; cote 144, scans 005, 182-183.
- **[rank 2] @603, MPL_146_001-099, R095.** The "meilleur exposant" table of 146/071-073: prove or refute that in characteristic zero the tangent line L_i at a marked point has order (n−1)(n−2) in Pic[M_{0,n}/S_{n−1}] and the total tensor product L = ⊗L_i has order n−1 in Pic[M_{0,n}/S_n], as claimed by Michel Hua's project (Hua 2026, hexagonmath.org 2611.00189; its Lean check covers only the function formulation, not the dictionary to equivariant line bundles and quotient stacks; credit to his project). Our tests to use: the S₅ character at {1,i,−1,−i,∞}, the triple count ν = (n−1)(n−2)/2 with the disputed factor two (2ν|4ν), "60?" as lcm(20,12). Cote 146, scans 071, 073.
- **[rank 2] @605, MPL_146_001-099, R098.** The five-point calculation of 146/074 as equivariant Picard cohomology: for X = M_{0,5} (ordered) compute 0 → k^× → O(X)^× → ⊕_D Z[D] → Pic(X̄) → Pic(X) → 0 with the ten boundary divisors (cote 147, scan 066) and the rank-five unit group generated by x, y, x−1, y−1, x−y; identify G.'s primed lattice (the uncertain P₃(K)-notation) with the kernel of the boundary-class map; compute H¹(S₅, O(X)^×) and the obstruction map to H²(S₅, k^×), extending the U₀,₃ method of LM_140-1 scan 023 (Keel 1992 as framework). Cote 146, scan 074.
- **[rank 2] @672, MPL_147_003-047, N075.** Prove or refute that the action of GT̂ on the profinite mapping class groups (Lochak et al. 2026, preprint arXiv 2602.12462, all positive genera with at most one marking; Hatcher-Lochak-Schneps 2000 for a subgroup) extends to G.'s category of MD-graphs and generization morphisms (147/003 items 9-12, 035-047): outer actions on the component-moduli fundamental groupoids that preserve boundary inertia and commute with every gluing and contraction map. This is the boundary compatibility G. asks for in LM scans 402-403.
- **[rank 2] @684, MPL_147_048-137, N060-04.** G.'s expectation on 147/060 ("donnerait la clef"): the tower is determined by its strata of modular dimension ≤ 2. Build the graph-pinned groupoid with one-dimensional strata as elementary moves, attach the two-dimensional relations keeping stabilizers and the commutation of disjoint moves, and prove that the comparison functor to the fundamental groupoid of the moduli tower is fully faithful and essentially surjective, discrete and profinite (cf. Hatcher-Thurston 1980; EXIT_ONE_TYPE's two-level principle). G.'s "question essentielle" on 148/063 (the tower T_top^±(Γ) "avec sa dépendance fonctorielle" in the graph Γ, IMPL P3) is the same problem; start with S₁T₀,₃ (148/064-065).
- **[rank 2] @731, MPL_147_048-137, R133-04.** G.'s "élément de structure tout à fait non-formel" (147/121-137): prove that the normal-torus torsor groupoids over the starred strata D_d*, with their first-vertex face maps, glue (by a van Kampen/descent theorem on compatible neighbourhoods, or through the Kato-Nakayama log Betti realization and Treumann's exit paths) to the fundamental groupoid of the boundary complement, under the π₂ caveat of 147/130; this is the déploiement of war-game hunch H4 (check against EXIT_ONE_TYPE and EXIT_TOWER, where H4 may be placed).
- **[rank 3] @173, MPL_121_001-048, N69.** Realize the face maps ∂_jV_i°→V_j° and the grids of 121/041-047 by a normal-crossing boundary (as in the tower's boundary strata) and write every flag map; prove compatibility with the punctured normal-line bundles of 147/173-178 and the arithmetic tori T^J of 149/129-136 (EXIT_ONE_TYPE P1a1, P4e; LM6 F.43; war-game hunch H4).
- **[rank 3] @355, MPL_142_001-093, N019.3.** G.'s enlargement problem on 142/018-021 ("en termes de géom. alg. 'abstraite'"): build the category of curves with finite covers and open inclusions algebraically from Hurwitz stacks that keep the branch divisor and ramification profile, with transport by their étale fundamental groupoids; prove that the associated correspondences compose, that the result is independent of auxiliary markings, and that it is equivalent to the isotopy category of 142/019 (compare admissible/twisted covers, Abramovich et al. 2003).
- **[rank 3] @459, MPL_144_001-061, N005.6.** Make precise G.'s "structure 'combinatoire' de Y" at infinity (144/005): prove that boundary data consisting of the incidence complex together with normal-line twisting and the connecting maps π₂(stratum) → π₁(torus fibre) determine the homotopy (and profinite) structure of the moduli space near its boundary, and that the bare incidence complex does not (the obstruction recorded in the cote 149 notes 134.1-135.1; EXIT_ONE_TYPE, LM6 F.43). Cote 144, scan 005.
- **[rank 3] @516, MPL_144_168-184+148_001-028, Q1c.** Five-point word comparison: write the explicit homomorphism from the groupoid presented on 144/177 (relations, boundary labels, orientations) and 148/018-026 to a specified five-labelled boundary presentation of π₁(M_{0,5}), compute the image of each ordered word, and decide whether G.'s relations there are equivalent to the pentagon (cf. LM8 B.28 open; LM7_PUSH E.3 open, E.46; LM3/121-122 substitution g ↦ αgρ(α)^{−1}). Include the effect on fundamental groupoids of the μ-parameter map P¹∖{0,±2,∞} → M_{0,5} that G. asks for on 148/039 ("il y a lieu de regarder l'effet sur les groupoïdes fondamentaux"), and check the words against the finite quotient of LM7_PUSH E.46. Cote 144, scan 177; cote 148, scans 018-026, 031-039.
- **[rank 3] @550, MPL_145, A04.** The extra kernel of the filling map (LM1 D.7, open; IMPL P3): with ψ: A → Aut(π̂), q: Aut → Out and P ≤ A mapping isomorphically onto Inn(π̂), one has ker(qψ) = P·ker ψ and P ∩ ker ψ = 1 (our lemma, 145 A04). Decide whether the Aut-valued map from full profinite peripheral automorphisms after filling a puncture (LM_140-2 scans 367-369, 397-399) has a nontrivial kernel, which is equivalent to an Out-kernel larger than point pushing. Cote 145, scans 004, 025.
- **[rank 3] @553, MPL_146_001-099, R003.** Coherence of G.'s local graph models (146/003, 013, 018): assemble the trivalent lattice-extension models and the four-point moves into a complex of marked decompositions (with boundary markings and lattice twists) and prove that the induced groupoid is independent of the sequence of moves, i.e. that the complex is connected and simply connected after G.'s identifications (literature model: Bakalov-Kirillov 2000).
- **[rank 3] @570, MPL_146_001-099, R034.** Presentation certificate for 146/020-033: attach a 2-cell for every verified mixed relation ("relations mixtes", 027) and fibre relation to the path graph of 020-024 and prove that the resulting 2-complex has the intended fundamental groupoid (compare Salvetti 1988 for complexified real arrangements; the graph groupoid of cote 147 scan 035).
- **[rank 3] @654, MPL_147_003-047, N048.** Check our counterexample to Knudsen 1983, Cor. 3.9(b) read globally: for a stable chain E₁ ∪ E₂ ∪ E₃ of elliptic curves with distinct j-invariants, the separating clutching map β_{1,2}: M̄_{1,1} × M̄_{2,1} → M̄₃ has two distinct preimages of the chain, so it is not a closed immersion (finite unramified, Cor. 3.9(a), unaffected). Settle whether the printed statement needs this qualification before anyone is told. Arises from cote 147, scans 030-031.
- **[rank 3] @679, MPL_147_048-137, N058-02.** G.'s "doit pouvoir" (147/058): prove or refute that every subgroup H ≤ S₄ is the image on the four flags of the automorphism group of some stable decorated graph (with four distinguished flags), e.g. by attaching rigid gadgets to a four-flag core.

### DER: Dérivateurs successor (localizers, totality, homotopy)

- **[rank 2] @4, MPL_105, R21.** Decide whether every fundamental localizer satisfying the strengthened reversibility axiom W7 bis / W8 bis of 105/052 is a homology localizer, or exhibit one that is not (our NEW_RESULTS 7 reports an unreviewed reversible localizer not detected by spectra, NEW_RESULTS 8 says "homology localizers only": the two records must be reconciled). Open rows POLES F.14(1), RESIDUE I.7. Cote 105, scan 052.
- **[rank 2] @8, MPL_105, R32.** Two transitions G. leaves open on cote 105: (i) prove or refute that the interval-generated class TC equals C∩W under explicit smallness/accessibility hypotheses (105/020, 032, 034-040; PATHS D.18/D.22, BISITE A.27/A.28); (ii) repair the reverse square/cube excision axioms (Der 6/Der 8, W7 bis/W8 bis) hypothesis by hypothesis, with the repair required to survive passage to every shifted derivator D_I (105/047, 051-052; TOTASPH A.13, BISITE A.33, RESIDUE I.7).
- **[rank 2] @270, MPL_133, B09.** War-game hunch H6 must be restated before it can be proved: with ordinary finite-dimensional k-local systems, S²→* lies in W_fd (both categories are Vect_fd(k)) but H²(S²;k)=k, so schematization does not invert it. Prove or refute the corrected H6: the class of maps inducing equivalences on derived categories (or cohomology with coefficients) of finite-dimensional local systems is a fundamental localizer and its localization is Toën's schematization/affinization. Cote 133, scans 006-008 ("le topos classifiant", B_{O(n)}); Pursuing Stacks §110, pp. 443-444.

### GS: Group schemes and descent (LM1 line)

- **[rank 3] @254, MPL_131, RN070.** Attack the open LM1 D.11 (integral group-scheme classification; descent datum of the μ₂-extension at 2) through G.'s relative recognition lemma of cote 131 (scan 029 NB, "un hom de foncteurs G→F"; completion descent, scan 005): formulate the classification as a natural transformation with the local and limit properties required there and verify its Artinian tests at 2, or show why the lemma cannot apply. Cote 131, scans 005, 029.

### CRYS: Crystals and de Rham

- **[rank 2] @305, MPL_136_047-094, R054.** G.'s 1976 integral PD de Rham theory of simplicial sets (cote 136, scans 047-094 and 189-234: C^{p,*}_DRpd(X,k) = Hom(X, Φ^{p,*}_*), with the weight algebra k{T}): prove for every simplicial set X and weight w the comparison H^j(C^{*,w}) ≅ H^j(X,k)·T^[w] for j ≤ w, multiplicative with the binomial coefficients of Γ(T); prove or refute that the divided powers descend to operations on cohomology; and decide whether the weighted PD algebra determines the integral homotopy type of connected nilpotent finite-type X (compare Mandell 2006, faithful not full; Horel's cosimplicial binomial rings; Toën 2020). Tests already in our notes: CP² and BC₂ exclude the unweighted reading; Michel Hua's project's finding 136-pd-de-rham-shadows is the related register entry (credit to his project).
- **[rank 3] @304, MPL_136_047-094, R052.** Construct a filtered comparison between G.'s weighted divided-power de Rham model (136/080-083, coefficients Z{T}) and cosimplicial binomial rings (Horel; Toën 2020), extending the algebraic observation gr(Int(Z), degree filtration) ≅ Γ_Z(T), compatible with differentials, simplicial operators and derived realization, or show that no such comparison exists. Cote 136, scans 080-083.

### MOT: Motives and tensor categories

- **[rank 2] @792, MPL_14_002-044, A28.** G.'s Albanese-equivalence quotient P^i(X) (cote 14, scans 024-039: cycles Z_*(ν) with deg ν = 0, S_T(ν) = 0): decide whether the factorization of the Abel-Jacobi map through P^i(X) → J_a^{2i−1}(X) (our A28) is injective, i.e. whether P^i(X) is representable by the algebraic representative, and prove or refute G.'s Theorem 3.1 on the ℓ-adic homomorphism of scan 038 ("ne dépend que de u_Z"), using ACV23 (Prop. 8.2, codimensions 1, 2, dim X; miniversal cycles, Def. 4.2, Lemma 4.7) and Oda 1969, Cor. 5.11-5.12 in characteristic p. The ring structure is Michel Hua's project's finding 14-albanese-equivalence-ring (credit).
- **[rank 2] @1146, MPL_16+47+54+44, D13.** G.'s "A prouver que cette dernière est positive !" (cote 44, scans 008-009): prove or refute that the divisor class D = r_*(p*z·q*z) descended to J = A/N is ample (positive) for his correspondence z, after the primitive-decomposition correction of the margin of 44/008; symmetry and nondegeneracy do not suffice (−λ_L is symmetric), G.'s own example on cote 14/021 gives degree −2d of both signs ("des signes différents !!", our @784), and the test family T = Pic⁰(Y) of 44/009 is the place to fix the sign (war-game hunch H9).
- **[rank 3] @120, MPL_11_002-042, O03.** Prove or refute G.'s "on trouve une équivalence" (11/034-042) in its stated domain: on special bivariant Poincaré power systems with multiplicative gauges, evaluation at the one-point set reflects isomorphisms / is an equivalence onto Poincaré algebras. The unrestricted reading is refuted by our partition counterexample (O03); the restricted statement is Michel Hua's project's conjecture 11-simplicial-bivariant-poincare-equivalence (credit to his project). Cote 11, scans 034, 036, 038, 042.
- **[rank 3] @145, MPL_11_043-058+56, N061.** Transport the local vanishing class and middle pairing of the quadric pages (56/020, 026, 030: pairing factor 2, "classe évanescente") into the global middle cohomology of a Lefschetz pencil and prove compatibility with the Néron/intersection formula ⟨ζ,ζ′⟩=(−1)^m Z·Z′ of cote 44/004 (input to war-game hunch H9). Cote 56, scans 020, 026, 030; cote 44, scan 004.
- **[rank 3] @237, MPL_121_049-073+153+155, T23.** "Exprimer la rigidité de C !" (155/002-010): prove that G.'s pro-ring A = U^∨ with the idealizer-quotient multiplicativity condition (ii) over the noncentral copy of k′ is equivalent to a (left) Hopf algebroid in the sense of Hai 2008 (Thm 2.2.4) / Schauenburg 2017, with rigidity of C corresponding to the antipode (descending evaluation and coevaluation), or exhibit where G.'s data differ. Cote 155, scans 002-010.
- **[rank 3] @247, MPL_131, RN042.** Decide whether G.'s representability criterion of cote 131 (scans 002-042, unramified/locally quasi-finite functors) can be applied to a family-valued functor of algebraically trivial codimension-p cycles modulo a rigidifying equivalence, so that Murre's algebraic representative becomes a representing object, extending the divisorial-correspondence/Picard case of 131/017 (war-game lead WG2 §2.3 #13; the full Picard functor need not be unramified, so the functor must first be identified).

### NEW-TAME: New archive cluster: tame topology, stratified spaces and classes of functions (cotes 39, 120, 121, 150, 151; Esquisse §5-6)

- **[rank 2] @160, MPL_121_001-048, Q3.** Identify G.'s tame-structure axioms with a named theory: prove or refute that the all-arity system M1-M11 of cote 120 (scans 003-025, with the compact layer M9, neighbourhoods M10, field operations M11 and constants R_0) and the one-space axioms a-f of cote 121 (scans 004-024) are realized exactly by o-minimal expansions of the real field (or by Shiota/Nash-geometric families), i.e. construct the reverse map from an M-system to an o-minimal structure or give an M-system that is not one. Known so far (our notes): the definable realization satisfies a-f; the bare a-f admit F={∅,R}, which is not of that form; the compact-model axioms of 121/070-073, and M1-M11 of cote 120 on the branch without the optional M0, are satisfied by all compact subsets (Cantor set: not o-minimal; 121 TC06, 152+120 Q3-02), while 121's clause f) gives the one-dimensional finiteness on the real line (Q3-06), so the item is for the drafts completed by the triangulation axiom of 121/065 (TC08); van den Dries-Miller and Schürmann give the local/global dictionaries.
- **[rank 2] @210, MPL_121_049-073+153+155, TC19.** G.'s "à tirer au clair" (121/073, with the triangulations of 065): prove or refute that, for compact polyhedra, the space (simplicial group) of tame (definable) homeomorphisms is homotopy equivalent to the space of PL homeomorphisms, via a relative, parameter-preserving triangulation theorem for definable families over a parameter space (Shiota 2010/2014 and Shiota-Yokoi 1984 give the single-map and isotopy cases; Shiota's 2014 Supplement, p. 227, as corrected in Shiota 2016, p. 8, and the relative injectivity argument of his 2010 preprint, p. 46, come closest and must be checked first). Cote 121, scans 065, 070-073; cote 150, scans 037-043.
- **[rank 2] @835, MPL_150_001-043, P02.** G.'s equipped conical stratified systems (cote 150, scans 022-043: découpage cônique, strict cones and collars, the inductive pushout (19), the Cat-objet of 041-043): prove (i) existence of the equipped cone-and-collar system for finite stratifications under a non-wildness (tame/o-minimal) hypothesis (150/037); (ii) that the internal nerve or realization of the deployment is weakly equivalent to the exit-path simplicial set (Lurie HA A.9.3-A.9.4; Treumann 2009; Ayala-Francis-Rozenblyum 2019); (iii) the coefficient-level reconstruction. Tests: the sphere of 147/180, a disconnected boundary intersection, a family with changing incidence; settle first the marked-base (R21a) and global-meet (R29a) gaps (cf. EXIT_ONE_TYPE P1a1, P1d1; war-game H4).
- **[rank 3] @168, MPL_121_001-048, N54.** Prove or refute G.'s claim (121/028, 035-036, "doivent aussi être des variétés") in its own setting: for a proper map in the selected piecewise/tame category, locally a product, with manifold source and target, the fibres are manifolds. The bare topological inference fails (Bing 1958: B×R ≅ R⁴ with B not a manifold); the tame/piecewise case with the proper-map premise and the mobility values of 028 is undecided.
- **[rank 3] @935, MPL_152+120, Q4-07.** G.'s question on 120/025 ("Énoncé analogue pour un diagramme fini … ?", "trivial par morceaux"): characterize the finite diagram shapes for which every diagram of compact semialgebraic (or o-minimal) spaces and maps over Y is simultaneously trivial over the pieces of a finite partition. The parallel pair with arrows id and a rotation R_c fails (our counterexample, rotation order is a diagram invariant); Shiota 2010, Lemma 1.1 gives a positive result for diagrams without repeated sources and without directed cycles; decide whether that condition is also necessary.
- **[rank 3] @1387, MPL_36_053-085+39, N68.** G.'s axioms for families (A_n) of formal power series (cote 39, scans 004-020): prove or refute that closure under rank-one flows (axiom g, 39/007) implies the rank-p integration axiom h) (39/016-017), i.e. that normalizing an involutive rank-p distribution stays inside the family; settle with it the hierarchy of the other axioms (Hensel and implicit-function closure, inverse closure H, coefficient descent and unique division, 39/010-020), and compare the resulting classes with Weierstrass systems and Pfaffian closure in o-minimality; Michel Hua's project's conjecture 39-inverse-function-axioms-henselian bears on it.

### NEW-PSEUDO: New archive cluster: pseudoline arrangements and the surface of relative positions (cote 154; Esquisse §8)

- **[rank 2] @944, MPL_154_127-176, P05.** Esquisse §8's surface of relative positions (cote 154, scans 151-176, with the counting sheet 154/120): for a simple arrangement Σ of n projective pseudolines, construct the cellular complex Rel(Σ) of stable and unstable relative positions of an added pseudoline, prove that it is a surface, compute its Euler characteristic and G.'s g = 1 + s₀ − s₂ (stable flag count 2n(n−1), quartic vertices s₁ = 2s₀), and prove that G.'s elementary sweeps ("balayages élémentaires de positions relatives", 155-156) generate all deformations, with a complete list of relations among move sequences. Known input: Sturmfels-Ziegler 1993 (Thm 1.2, Cor. 4.5): the order complex of the extension poset of a rank-three oriented matroid is a homotopy 2-sphere (a surface structure still needs proof; over a fixed straight-line realization the count near a ν-fold contact is 2ν, against 2^ν local pseudoline classes); Michel Hua's project's conjecture 154-generisation-cube (the stable generizations of a position with ν contacts form the vertices of a cube, ν·2^{ν−1} edges; credit to his project) must be reconciled with the surface claim, since a cube adjacency at an interior vertex is incompatible with a regular surface cellulation for ν ≥ 3 (our C04); G.'s own open points: the endpoint reconstruction by "blocage" and "plusieurs choix naturels … pas sûr qu'aucun de ces choix ne marche" (154/151).

### NEW-FORMS: New archive cluster: networks, ficelles and forms (cote 156, 1986)

- **[rank 2] @1008, MPL_156-1+156-2, A29.** Realization of G.'s networks (cote 156-1, scans 024-027, and 156-2 "Réalisations topologiques"): prove or refute that every réseau (model satisfying F1-F6) has a topological realization as a one-dimensional space of ficelles and lieux, unique up to homeomorphism, and characterize the networks so realized (e.g. those coming from tame one-dimensional spaces); our counterexamples to arbitrary restriction (A12), to the F6 equivalence (A24) and the fork order (A22) bound the axioms.
- **[rank 3] @1003, MPL_156-1+156-2, A18.** Orientation of networks (156-1/016-018, "syst. transitif", "exactement deux classes"): prove that the orientation transport of a connected regular network satisfying F1-F6 is trivial around every closed chain of transitions, so that it has exactly two global orientations, or construct a network with nontrivial transport.
- **[rank 3] @1039, MPL_156-1+156-2, P05.** Forms as pro-objects of finite cuttings (cote 156-2, scans 005-019, and the README's conjecture): define a category of cutting systems of a ficelle (lieux, mailles, birives) with refinement maps in which common refinements exist (allowing isotopy, replacement or subdivision of cuts), and prove or refute that the ficelle is recovered from the resulting pro-object (up to homeomorphism, or up to homotopy). Literal systems of mutually disjoint cuts are not cofiltered (crossing cuts in [0,1]²; disjoint but incompatible two-point cuts on a circle).

### NEW-ANALYSER: New archive cluster: analysers, plethories, binomial rings (cotes 133, 153)

- **[rank 3] @215, MPL_121_049-073+153+155, A13.** Decide whether G.'s analysers (153/006: commutative ring with a unital composition monoid, right substitution a ring map) satisfying the optional finite decomposition laws 3) are exactly plethories over Z (Borger-Wieland 2005, monoids in birings), i.e. whether the finite formulas determine compatible co-operations; and whether the composition-stable algebras Ω⊂Q[T] of 153/003-004 admit those decompositions. Cote 153, scans 003-006.

## Edition matters for the second pass, by package

### MPL_105

- @2, R09: Companion cross-reference: "W given beforehand by cohomological criteria" (105/032) parallels Pursuing Stacks VI §125, ms. 530-532.
- @6, R26: Convention: "propre"/"lisse" on 105/045, 051 and condition 4 on 032 mean base-change (cohomological) properness/smoothness, as separated in Pursuing Stacks VII §§136-137.
- @9, R33: Proof obligation on 105/045-047: say which equivalence class contains α and which coefficients it controls when passing beyond constant ξ; cancelled "D-équiv. 2-complète" (047); exponent on W_Ψ^g (045) uncertain.
- @10, R34: Companion cross-reference: the transfinite construction of 105/034-040 matches DER_XV-a §1, ms. 1-12, formula (1.23) and Theorem 1; G.'s own "Il faudrait quand même expliciter la dépendance fonctorielle" (ms. 10).
- @11, R35: Companion cross-reference: "n'a rien de carré" (105/049) anticipates Dérivateurs XII ms. 125-127 (Prop. 13 and corollary, under W(7)), the closest textual match to cote 105's total-category forms.
- @12, R36: Companion cross-reference: "strict Quillen triple" (105/025-032) vs Dérivateurs XIII-a §§1-2, ms. 5-8; do not read "Quillen pair" as a Quillen adjunction.
- @13, R37: Companion cross-reference: accessibility of source and target of g (105/034) vs sources only in Dérivateurs XV-a Theorem 1, ms. 11, and XIX small-object data.
- @54, BISITE A.27: Edition: keep G.'s doubts about retract stability of W (105/025, 028) visible beside the retract argument of 030 (closest manuscript form of BISITE A.27).
- @59, BISITE B.5: Convention: keep the source's variance for "propre" (cofibred replacement) and "lisse et propre" (ρ) on 105/045, 051 explicit in the edition.

### MPL_106+107

- @102, Bounded conclusion: Edition: the section criterion of the modified roof category (106/012-016) holds under Brown cofibrant-object (CF1-CF4) hypotheses (our verification R106-V1); Michel Hua's project's findings register lists it as a candidate conjecture (106-section-criterion-span-faithfulness); G.'s "C1-C3" remain to be identified.
- @103, Own audit observations: ordinary external products: Errors of the page 107/014, 016 (audit O1-O4): the identification Hom(L'⊠M', L⊠M) = Hom(L',L)×Hom(M',M) and the mixed formula L^M = L are false (finite-set counterexamples); separate vs joint continuity confused; parallel objection in Dérivateurs XVIII ms. 63-64 (Lemma 4.2.3).
- @104, Strong W(7), total asphericity, and bounded first-appearance leads: Companion/dating leads: no W(7) or total asphericity in 106+107; W(7 bis)/W(7) first at XII ms. 75-77; "total aspherical ⇒ filtered?" already asked at II ms. 36 (conjecture at 36ter; y\Y → y\X per TOTEX2 D.4); Pursuing Stacks §§60, 62, 64, 69-70 and cotes 117-118 to search; the companion's W(7) counterexample stays attributed to the companion.

### MPL_11_002-042

- @106, MB01: Companion cross-reference: cote 11's category Hom(X,Y)=A(X×Y) and realization ρ (11/003, 011-013) as the source of cote 16's operator rings (16/003, 018).
- @107, MB02: Companion cross-reference: kernel inclusion functor for a stable system A′⊂A (11/021); G. postpones the general equivalence; the marginal classification wording is difficult.
- @108, MB04: Reading question 11/019, 023: "l'ens des f_*(1_Y)" is not a subring (proper degrees give Z≥0), so an additive-closure convention is needed; "l'ens" uncertain.
- @109, MB05: Companion cross-reference: maps of type A′ (11/023-025) give the multilinear closure recipe behind cote 16/015, 018.
- @110, MB07: Companion: degree transport q ↦ q−d(X) (11/027-036) matches cote 16/003's End^(ν); "Mais c'est faux" retraction and remaining signs unresolved.
- @111, MB08: Companion: cote 11 supplies operator rings but not the chosen images L, π_i that cote 16/016-017 calls essential.
- @112, MB09: Companion cross-reference: cote 11's correspondences as kernel data for cote 16/049's motivic programme; comparison with Chow motives (Stacks 0FG9) via r ↦ 2r.
- @115, MB12: Companion: cote 16/051-055 needs a chosen polarization and inverse operators u_i in im(ρ_X); the k|n doubt on 16/051-055 stays.
- @116, CL02: Companion: Hom_{V^A}(X,Y)=A(X×Y) (11/003) frames cote 16/048-049's inverse map w^{-1}u=v^{-1}; operator content matches Kleiman 1968, Prop. 2.3, p. 370.
- @117, CL04: Companion: the quantifiers "pour tous les f:Y→X" (11/023) and "for every T" (CT16/046) must survive any dictionary with printed A(X×X)⇒B(X) (G69, p. 196).
- @121, O04: Literal question "produit fibré ... dim. correctes?" (11/042) answered negatively in the scalar gauge category (O04): base change needs a trace normalization; geometric squares untouched.
- @122, O05: Sign (−1)^{δj} in the margin of 11/034 derived from the projection formula; vanishes under the even-degree restriction of 031.
- @123, O06: Companion: Oda 1969, Cor. 5.11-5.12 (Dieudonné module of _pX ≅ H¹_dR) is the comparison map for the de Rham example of 11/034-042 and cote 54/003-007.
- @124, O07: Companion: the K-class of CT47/003's kernel functor Φ_L is the pull-multiply-push operator of 11/011.
- @125, RT12: Reference: the determinant section on 11/035 is descended by appeal to SGA 8 §1; pullback symbol uncertain.

### MPL_11_043-058+56

- @126, N002: Companion: 11/044 places numerical, homological, Picard and Albanese quotients in the bivariant framework (cf. CT44/002-004).
- @127, N005: Notation: target-first A(I′;I) on 11/046 with coordinate isomorphisms to correspondence composition.
- @128, N017: Check of the tables on 11/051 in the P¹ realization: χ=2 identities hold; Δ₁₂ = y₁ + y₂ there, to compare with the source's "base".
- @130, N021: Notation/provenance: typescript R-partitions (11/049) and handwritten (R,J) (11/055) index different things; no map between them.
- @132, N027: Companion: C(X)⇒C(Y) deduction (CT16/040) and printed B (G69, §3, p. 196) via the action map of 11/044.
- @136, N032: Companion: numerical quotient (11/044) and Jannsen 1992, Thm 1 and Cor. 1 (premise: algebraic Künneth).
- @138, N041: Discrepancy in the table of 56/015: at ν=1 the literal torsion degree is 0, while the conic cone gives H²(E,Z)=Z/2.
- @139, N043: Companion: Braden 2003, §3 Lemma 6 gives an instance of the boxed expectation on 56/017 (cone xy−zw=0).
- @140, N048: Lattice basis change for the index-two pair [ξ^ν,λ_ν] and φ_ν (56/024, 030).
- @142, N052: Sign on 56/026: the positive formula disagrees with the quadric-surface realization (λ₁² = −2ab, ξ² = 2ab); transcription keeps the sign, note records the test.
- @143, N053: Reading: "classe effaçable" (unsure) and "classe évanescente" on 56/026 name a restriction and a pushforward.
- @146, N062: Companion: Oda 1969, Cor. 5.11 answers cote 54/007's "Cette extension peut-elle se déduire de la connaissance de p^A ??" for abelian schemes over a perfect field.
- @148, N072: Companion: Lemma 1.14 on 56/025 (T′=T); the re-edition cites IX 6.8 at this step (p. 125).
- @150, N082: Reading: inserted "et séparé" and "moyennant (i)" in the proof of 1.7(b) on 56/033.
- @151, N084: Companion: Delzant's Q(A) on 56/036 is GW(A).
- @153, N087: Companion: the total-class ring Z×(1+Ĥ⁺) on 56/037 is G.'s "La théorie des classes de Chern" (1958), §4.2, pp. 147-149.
- @158, N100: Error of the page (and of the printed text): Lemma 2.3 on 56/016 with two arbitrary subtori R⊂T is false (SL₄ counterexample: W(R)=C₂, W(T)=1); the checked SGA 3 re-edition (cited [SGA12], Lemma 2.3, pp. 128-129) repeats the wording and uses maximality of T in its proof; the hypothesis must be stated.

### MPL_121_001-048

- @162, N08: G.'s "Est-ce suffisant" (121/007): no, under the α/β-only reading (five-member family on a three-point space).
- @164, N79: Error of the page: "Ceci implique que les feuilles sont ∈F_r" (121/017-018) fails on literal data (two-point space); restriction stability is missing.
- @165, N78: Error of the margin: arbitrary traces (121/019) break condition c) (explicit planar example).
- @172, N64: Edition: the drawings on 121/041-042 mark the shared face V_210; keep boundary attachments in the transcription.
- @174, N68: Reading: faint heading on 121/046, the n_j/n_i label and missing circles on 047 stay uncertain; no general formula to be filled in.

### MPL_121_049-073+153+155

- @175, R121-02: Gap: the proposed first open stage on 121/049 ("la réunion des feuilles ouvertes") needs a complement clause (line with closed set {0}).
- @178, R121-13: Convention: moderate points vs all real constants (121/055-056, M4); the parameter convention must be stated in any o-minimal identification.
- @179, R121-14: Gap: the field/vector-space assertion on 121/056 ("Moyennant 1°,2°") fails without multiplication (D=Q+Q·2^{1/3}).
- @182, R121-21: Edition: record G.'s gluing proof sketch on 121/061-062 (coordinate extension, zero fibre, shared retract; "OK.") as his method; the last arrow reading is uncertain.
- @184, R121-27: Edition: the Chern-class fragment on 121/066 (Grass_n(E), total-class product) is a separate fragment; ranks and conventions unspecified (cf. G., Classes de Chern 1958, §§1-3).
- @187, R121-32: Gap: the C_* draft on 121/070 lists permutations, projections, repetitions, products, so the following intersection proposition needs an extra hypothesis (see @192).
- @188, R121-33: Convention: "un iso. ssi il est bijectif" (121/070-071) concerns graph-admissible morphisms, not arbitrary homeomorphisms.
- @190, R121-38: Gap: the finite closed-cover descent of 121/073 needs the intersection/restriction closure missing from a)-d).
- @192, R121-41: Countermodel: axioms a)-d) on 121/070 do not imply "X∩Y∈C_n" (equality-block family on {0,1,2}).
- @197, TC05: Same gap as @192 (121/070 vs public 120/003, which has inverse-coordinate operations).
- @201, TC09: Convention: field operations, order, parameters and topology are separate data (121/055-058, 070-072); check 056 under the exact numbered hypotheses.
- @203, TC11: Facsimile check of public 120 (003-025): M0 "axiome (facultatif)" (007) not to be combined with M9; 025 marks "À prouver".
- @204, TC12: Correction of the intake reading: 121/004 and 010 do assume complements and finitely many components (condition f).
- @212, A01: Reading (153/002, 006): pointwise product and substitution are distinct; left substitution is not additive, so "anneau" is not two-sided distributivity.
- @217, A17: Convention (153/006): the unit's invariance under right substitution is a separate axiom (axiom 2 speaks of pseudo-ring maps).
- @218, A18: Error of the page: Example 1, Ω_A = App(A,A) (153/008), fails the optional decomposition axiom 3a (rank argument on F = indicator of 0).
- @219, A19: The circled question "(Ω_A)_0 ≃ ΓA?" (153/008) has the formal answer yes (constants factor through the terminal object).
- @222, A23: Companion: binomial and λ-ring analysers (153/010) vs Borger-Wieland 2005, §§2.10, 2.14.
- @223, A26: Error of the margin (153/004): freeness does not give the asserted tensor uniqueness once the ring inclusions are broadened (F_q, T^q−T example).
- @224, T02: Convention (155/002): A = U^∨ is a pro-object; statements on D(A) and M = A need continuity or a pro-category.
- @227, T05: Reading (155/004): U = k′⊗_k k′ is descent data (pair groupoid); G′ is not Aut^⊗_{k′}(F), which is trivial.
- @229, T09: Companion: the diagonal tensor functor of 155/004 is Deligne-Milne 1982 (corr. 2012), (3.10.1) and Prop. 3.11; Deligne 1990, §§1.2, 1.9, 1.12 gives the fibre functor; "Abel" and the pro-ring presentation to be matched.
- @230, T11: Reading of the "OK" on 155/004 ("exact (OK si k′/k est étale) et fidèle"): faithfulness needs the A_{k′}-module structure, not étaleness alone.
- @231, T12: 155/004: for inseparable k′/k the unrestricted diagonal functor is not exact (F_p(t^{1/p}) example).
- @233, T16: The warning "pas néc. k′-linéaires" (155/006) is substantive: k- and k′-duals differ by a choice of functional; the trace can vanish (inseparable case).
- @234, T17: Gap (155/006-008, "Il faut encore que"): the rigidity criterion needs evaluation, coevaluation and the triangle identities, not only A → A^o.

### MPL_131

- @239, RN005: Proof obligation (131/002, 012): the length-one, trivial-residue Artinian exactness test must be shown to generate the finite Artinian descent needed for prorepresentability (cf. Schlessinger 1968, Thm 2.11; Michel Hua's project's finding 131-locally-quasi-finite-representability).
- @240, RN006: Convention (131/002, 014): the finiteness clause (B finite over K, then over Artinian A) is stronger than tangent-space finiteness and must be kept.
- @241, RN014: 131/009, 037: conditions C1 (generization) and C2 (neighbourhoods) are separate inputs; constructibility of the functor-defined locus is the missing geometric step.
- @242, RN020: Test of the compressed reading of 131/016 NR(b): embedded-nilpotent example fails it; scan 007's density insertion excludes it (conditional diagnostic).
- @243, RN029: Second-pass aid: an axiom-dependency table for the lists of 131/002, 014, 016, 025 (keep numberings apart).
- @244, RN032: 131/017 example b ("Classes de Correspondances divisorielles"): equivalence relation, families and rigidity must be specified before the criterion applies.
- @245, RN035: 131/017 "Foncteurs platificateurs": needs proper finitely presented hypotheses (Stacks 05UH; 052F shows finite-level flatness is not effective).
- @250, RN051: Companion: the relative formulation F→G (131/023, 029; direction of letters changes) vs Murre 1966, §2 Lemma 1; the open-immersion variant needs more hypotheses.
- @252, RN057: Convention (131/035): "modulaire local" includes the field-of-definition clause for β.
- @255, RN072: Sign convention (131/008, 010): "sera noté −c(M)", c(T) = −c(χ(T)); keep the sign and orientation.
- @256, RN073: Scope (131/021): χ(M,M′) depends on the hypotheses of n°s 2-5, not retained; not a theorem over arbitrary domains.

### MPL_133

- @266, B05: Companion: Pursuing Stacks §119, pp. 500-503 withdraws the divided-power comparison and asks whether Sym^bin(L^∨) → Maps(L,Z) is a quasi-isomorphism; cote 133/006 ("l'anneau binomial") is the earlier trace.
- @268, B07: Companion: Horel 2025 (Thms 3.7, 5.4, 6.1; Prop. 4.2 for K(Z,n)) answers the delimited PS §119 question; no equivalence constructed in cote 133.
- @269, B08: Companion: Toën 2020 (Hilbert group H = Spec Int(Z); K(H,n) as affinization of K(Z,n)); does not identify the quadratic-form Witt group of 133/006.
- @271, B11: Edition note on Pursuing Stacks §119, p. 502: "all integer-valued functions on Z" is literally false; binomial polynomials span integer-valued polynomials (p. 503 has the intended setting).
- @272, G01: Scope (133/036, "Extension d'un p-divisible par un lisse"): for arbitrary Barsotti-Tate groups the splitting fails (Mazur-Messing 1974, I §1.8); the intended formal category must be identified.
- @276, G11: 133/044 "constructible en général": the y²=x³−x family over Z[1/2] proves non-constructibility; verifies a precise form of Michel Hua's project's finding 133-affine-quotient-not-constructible.
- @277, G12: Correction of the gloss in Michel Hua's project's finding 133-affine-quotient-not-constructible: (G_s)_aff ≃ G_a (133/044) does not mean a split extension.
- @278, G13: Error of the page under its intended reading: the blanket equal-characteristic constructibility on 133/044 fails (Poincaré G_m-extension over A^∨ of a complex elliptic curve).
- @280, G15: 133/047: the corrected centre test with the inserted Z(K) is right for ordinary groups; the uncorrected formula fails (supplement, Appendix C).
- @282, G19: The equivalences marked "Vérifier" on 133/054 hold for ordinary groups (keep the frozen "Vérifier").
- @283, G20: 133/054: the residual epimorphism is not automatic (C_p×C_p); condition c) is needed.

### MPL_136_047-094

- @286, R005: 136/054-056: the induction uses only H^N(A_N)=H^{N−1}(A_N)=0 (and a degree-zero condition for N=1); keep the weaker hypotheses (cf. 067-068).
- @287, R006: Convention (136/054, NB "ne commute pas"): the integrations K_n are not simplicial natural transformations; only the assembled cochain map is.
- @289, R011: 136/060, 064: hypercohomology of F^* needs a totalization convention and the bounded-below hypothesis kept visible.
- @299, R043: Reading (136/094): the crossed-out base-change phrase under "Univ. flasque" is not a completed definition.
- @307, R060: Second-pass audit: check every use of Γ, tensoring and sections on 136/078-094 against PS §111's later retraction (projectivity vs flatness).
- @308, R061: Gap under the literal reading of 136/064 ("sans hypothèse de loc. constance", "à vérifier ce point"): for an arbitrary presheaf on Δ/X (X = Δ¹/∂Δ¹) the tensor resolution does not compute derived sections (H¹ = k).
- @311, R064: Error of the page: the broad flasqueness inequality on 136/075 fails in the constant corner (DR^{0,0} = k_*, simplicial circle), supporting the p ≠ 0 qualification of 076.

### MPL_136_189-234

- @316, R006: 136/215: theorem b's proof stops at "Dém :"; the universal constructions actually present are listed (204, 215, 217, 225-226).
- @319, R015: Convention (136/204, 206): morphisms of triples carry the scale λ (u(t)=λt′); forgetting it loses information at torsion bases.
- @321, R020: 136/212: the last formulas (A_1 = X_0 + f) silently assume φ₀(T) = T, and the displayed sum lacks coefficient symbols.
- @325, R027: Error of the page under the literal reading: the final sentence of 136/222 ("H^n_DR et H_n^Kos sont nuls pour tout n tel que n.1_A inv.") concerns total weight, not cohomological degree (x^{p−1}dx over F_p).
- @327, R036: G.'s "Il est probable que (Λ^iΨ_*)^! = k[i]" (136/227, 229) is verified (split integral normalization of K(Z,1)); record it.
- @328, R037: 136/229 NB b: under the ordinary reading, normalized Γ² and Sym² of K(Z,1) are not K(Z,2); the reading of Ψ^* and the inserted tensor must be settled first.
- @331, R046: Companion: the Cartan-Miller polynomial-form theory (Cenkl-Porter 1982) is the closest comparison for Γ(Φ)⊗Λ(Ψ) and the i ≤ p comparison (136/204, 231, 233); chain-level identification not done.

### MPL_142_001-093

- @340, N005.3: Gap (142/005): the puncturing reduction ("en remplaçant Y′ par Y′∖S′") needs an isotopy relative to the punctures; N007.6 repairs it without one.
- @341, N007.4: Companion: a purely topological proof for G.'s request on 142/007 by fixed-point indices (integral homology; mod n needs level ≥ 3).
- @342, N007.6: Companion: transfer and Euler characteristic give the topological rigidity proof requested on 142/007 and repair the reduction of 005.
- @343, N008.3: Error of the margin (142/008 NB "Tout sous-groupe fini … comme stabilisateur"): the genus-two hyperelliptic involution is no deck group of an unramified cover; free actions are needed.
- @345, N010.1: 142/010 ("Mérite d'être faite avec plus de soin !"): closed arrow stabilizers alone do not make composition continuous; the finite-index hypothesis of 011 is needed (explicit counterexample).
- @347, N012.1: Convention (142/012, formula (17)): the balanced product needs the stabilizer-closure convention (Z ⊂ Ẑ example is non-Hausdorff).
- @349, N013.2: Error of the page: "Et pas de pts isolés" (142/013) fails for U_{0,3}; needs a complexity qualification.
- @351, N016.2: 142/016: the base-extension assertion fails in characteristic p even on hyperbolic curves (Artin-Schreier torsor y^p−y=tx on P¹∖{0,1,∞}).
- @359, N025.2: Margin of 142/025 ("p de la forme 2γ+1"): the endomorphism version allows p ∈ 1+2Ẑ; oddness is necessary, not sufficient.
- @360, N025.5: 142/025 "on retrouve les équations habituelles": the two norm-one equations are the 2- and 3-cycle relations only; no pentagon or four-strand coherence is imposed in type (0,3) (cf. Furusho 2010).
- @366, N032.2: Companion: the profinite verification flagged in LM_140-3 scan 130 (unique order-two coboundary) follows from Herfort-Ribes 1985 via Z*C₂ ≅ F₂⋊C₂ (142/031-032); fails for pro-p versions (Herfort et al. 1995).
- @368, N035.2: Convention (142/035): β′ = β^{−1}, α′ = α^{−1} change the displayed relations; keep left/right corrections apart.
- @370, N037.1: The margin of 142/037 (relations stable under substitution) holds for fixed λ only when [λ, h] = 1; otherwise λ ↦ hλh^{−1}.
- @373, N044.4: Sign convention (142/044, Stokes margin): fix outward-normal-first before comparing signs of ω∧ε∧ω̄ = 1.
- @375, N047.3: Reading (142/047): the star in T_{Σ,R_i}^*/R^{*+} is deletion of the zero vector (rays), not the cotangent dual.
- @378, N050.2: Edition (142/050-051, 055): ω, ε and the surface orientation are distinct torsors; the cancelled (20) on 051 is not live; the roofed omega glyph stays uncertain.
- @381, N060.1: Companion: the boundary pinnings of 142/060-064 are tangential base points (Deligne 1989, §§15.13-15.18); inertia acts by the cyclotomic character.
- @382, N064.2: Second-pass check method for the path tables 142/051-064 ("Le passage à expliciter"): a finite typed groupoid model testing each uncertain index.
- @386, N070.1: Convention (142/070, (8)-(9)): f_l and g_l^{−1} (not g_l) satisfy the 1-cocycle equation; the cancelled g-cocycle discussion of 072 is not to be promoted.
- @395, N076.6: Gap (142/076, "points voisins sur X"): rational points are not dense; representatives in each overlap component are what is needed.
- @401, N080.6: Error of the live claim (142/080, "le th. de Mordell-Weil implique"): over K = Q^ab, allowed on 067, points 1 and −1 of G_m have the same Kummer class; the claim needs K finitely generated over Q (cancelled introduction of 079).
- @404, N082.4: Companion: G.'s "caractéristiques de x" (142/082) compares with Kim's unipotent Albanese map and Selmer varieties (2009); no equivalence of the programmes.
- @414, N087.5: 142/087: the hypotheses "X quasi-projective lisse géom. connexe" include X = Spec K; positive dimension must be assumed.
- @418, N090.3: Reading (142/090, "il existe une puissance Θ^n"): three inequivalent quantifier readings; the cover-dependent one is weakest.
- @419, N090.4: Diagnostic for 142/090: with a cover-dependent exponent the weakened "draconiennes" condition holds automatically (finite labelled covers); only the unpowered or uniform version has content.
- @421, N092.3: Gap in the lemma on 142/092: a finite cover needs H of finite index (open), not just injectivity.
- @422, N093.6: Counterexample to one-point determination for disconnected covers (142/093, margin "sans supposer ... connexe").
- @423, N093.7: Completion of the unfinished "En termes" (142/093): a semilinear lift exists iff θ(H) is conjugate to H; lifts form an N_G(H)/H-torsor.

### MPL_142_094-122

- @426, R06: Quantifier in "pour Θ̃ convenable!" (142/095): one lift for all K-morphisms or a lift per morphism; the frozen X|Y and the prime on Θ stay unnormalized.
- @430, R18: 142/098: image stability of stabilizer classes is insufficient without multiplicities (C₂×C₂ example), supporting the insertion on 098.
- @431, R20: 142/098-100: "j'ai oublié apparemment la plus importante": peripheral compatibility ("structure à lacets") is an additional condition, not a consequence of (a)-(b).
- @439, B02: 142/108: the four-loop relation l_∞l₁l₀l_{−1}=1 lives on the intermediate cover t=z²; "β relevé" and the γ/η labels need a base point and composition convention.
- @441, B10: 142/111: the R_i and Q_i vectors collide mod 2 and mod 3; separate identities over Z from statements after inverting 6.
- @442, B11: Check of a context transcription: γ₂³ − 2γ₃² = 54Δ; the first-pass context's "2γ₃² − γ₂³" and "Δ = γ₂³" (its scan 23) cannot be literal; check that image (142/111, 113).
- @449, C12: 142/117-121: the free-groupoid conclusion needs fixed-point-free adjacency actions or explicit treatment of fixed flags; "redondance" alone does not give it.
- @450, C16: Marginal claim on 142/118: the relations for r and τ₁r agree up to inversion and change of base point, not literally.
- @451, C19: Second-pass consistency certificate for the uncertain formulas of 142/120-121 (edge counts vs Euler characteristic detect a missing redundancy).
- @452, C22: Second-pass proof certificate for "engendré" → "présenté" (142/116-121): explicit functors, reverse functor and natural isomorphisms for the four presentation families.

### MPL_144_001-061

- @457, N005.2: Reading conflict (144/005): "sous-groupe … fermé … engendré" vs "α n'est pas néc. surjectif"; a continuous image is closed, so another meaning (normal generation, pro-object, groupoid) is intended.
- @461, N006.3: Proof obligation (144/006, "pt fixe par accumulation"): the iterated-midpoint drawing needs a centre-of-orbit argument (complete CAT(0) metric) and arbitrary finite groups.
- @462, N007.5: The marked product question on 144/007 is answered for S = ΣH: S×R ≅ S⁴×R (double suspension theorem, Latour 1979); S itself is not a manifold.
- @464, N009.4: 144/009 item 11: before identifying a rank-four trace lattice with E₈, compute integrality, evenness, determinant and definiteness with the scaling stated.
- @465, N010.2: Error of the page (144/010): with c central and x³ = y³ = 1, c³ = 1, so C = ⟨c⟩ is not infinite cyclic (Heisenberg group mod 3); a relation is missing or misread.
- @467, N013.1: Notation (144/013): "!" is the kernel of the permutation of punctures; primes in (2′), (3′), (5′) are equation labels.
- @470, N014.3: Companion: Matsumoto-Tamagawa 2000 (Thm 1.1) and Asada 2001 settle the injectivity readings of 144/013-014 for g=0, ν≥3 and g=1, ν≥1.
- @474, N018.3: Test of P^φ ↔ Q^φ (144/018, (21)): lifting may leave a Π̂/Π ambiguity; a geometric selection or inner-equivalence convention is needed.
- @476, N025.2: Companion: Tamagawa 1997, Thms 0.3-0.4 proves the affine hyperbolic reconstruction sentence of 144/025 over fields finitely generated over Q.
- @477, N027.4: Constants convention (144/027, datum (a)): with a fixed identification of constants the finite-index claim fails for K = Q; the intended reading must be fixed.
- @478, N027.6: 144/027: the "!" and "voir l'append.|cf. l'append." referral have no identified completion.
- @480, N028.3: Footnote of 144/028: Hom(K̄,C)/Aut_K(K̄) ≅ Hom(K,C), so the exception "for every finite extension of Q" is too broad (Q(√2) has two orbits).
- @485, N032.4: 144/032: "NB on peut faire un" is unfinished; record as such.
- @486, N033.2: Second-pass checks for the automorphism formulas of 144/033 (peripheral commutator, outer vs actual, central kernel).
- @488, N037.3: Companion: the "relation fondamentale" of 144/035-040 is the braid relation, not a five-point (pentagon) condition; Furusho 2010, Thm 2 (4) is the comparator for the pentagon.
- @489, N038.1: Error of the page (144/038): "On peut se borner à la seule équation abracadabrante" loses a relation (ε₀ = 1 abelian counterexample).
- @494, N043.2: 144/043: the frozen fixed-point formula (a±2i)/(2c) should be (a±i)/c for trace zero (test matrix (1,−2;1,−1)); reading or slip to check.
- @495, N043.3: Scope (144/043): ±I fix every point with discriminant 0; the criterion Δ < 0 is for non-scalar elements.
- @498, N047.3: 144/047 "bases directes": under the literal column action σ gives negatively oriented bases; a convention is missing.
- @501, N051.1: 144/051: the table of contents lists sections absent from the excerpt; leads for locating further sheets.
- @504, N052.4: 144/052: the literal freeness conditions admit a sphere with one vertex and a loop edge (K ≅ S¹), excluded by the opening definition; the intended category needs an extra condition.
- @508, N057.1: 144/057: folded edges correspond "1-1" to fixed points of ρ₁ only on R⁺; on the full flag set there are two per edge.

### MPL_144_168-184+148_001-028

- @519, Q3b: Edition of LM_140-2 (scans 219-221): the exception lists (1,0),(0,1) and (1,0),(0,2) differ; the comparison square (44) gives the maps to check the tower of 144/180, 148/020.
- @521, Q3f: Companion: LM §35 (scans 491, 493, 496) states injectivity of Γ_Q → Autext_lac(Π̂₀₃) "modulo le lemme 2" and G. stalls on its centre assertion ("je cale", "Consulter Deligne"); the centre and torsion facts are known for free profinite groups, and FLAGGED_149 A3 claims a proof (unreviewed).
- @522, Q4: Companion: a maquette passage exists on 144/182-183 (normalization branches, nodes, markings, weights); no continuation of cote 149's D_J/T^J argument.
- @527, R06: Reading (144/175): the uncertain star in G/Ẑ^{*}; the kernel of π is ζ(Ẑ).
- @531, R17: Test of "R^I ... contenant Z^I" (148/002): on the disk the integer boundary rotation is isotopic to the identity rel boundary, as in LM2/304; the inclusion needs the excluded types removed.
- @536, R35: 148/025: the dimension-two bracket places (0,5) and (1,2) with blank picture and name cells (dimensions 0,1,1,2,2 by 3(g−1)+ν); the five-point slot is left empty on the sheet.
- @538, R39: Second-pass check: finite incidence table for the drawing of 148/028 (doubtful 2′|1′, 6|b, b_a|b_c), side pairings compared via @537; counts 4−6+2 = 0.

### MPL_145

- @540, N02: Reading (145/002): H consists of realized commensurations, not the abstract commensurator; H/π is a set of right classes.
- @543, N11: Reading (145/010-012): π/Ẑ is an orbit set of the gauge action g ↦ l₀^α g l₁^{−α}, not a group quotient.
- @549, F05: Companion: concordance of five kernel/comparison problems (145/004, 023-026, 032-033, 037); the enlarged kernel of 145/025 is not the filling kernel.
- @551, A05: Reading H_n|H_1 (145/002): under H_n the fixed-index locus is not closed under products (lattice example).

### MPL_146_001-099

- @554, R005: Formula (7) on 146/004-005 needs a connected covering group (discrete C₂ counterexample); the R^I → U^I application is unaffected.
- @556, R008: Convention (146/007-008, (16)): Imp^I carries the action k·n = n + 2k (kernel generator is twice the ambient one).
- @558, R011: "Cette extension n'est pas scindable" (146/010) is proved on the page; catalogue it as proved.
- @560, R014: Convention (146/012-015): the lattice map is the unsigned incidence map (loops get 2a_s), not the oriented boundary.
- @567, R028: 146/017: the coordinate vectors collide in characteristics 2 and 3; the picture is for the complex setting only.
- @571, R036: Dating (146/025-041): printed dates (27 Mars 1979, 2 mars 1978, 1979/1980 tables) date the paper, not the mathematics; pair rectos and versos before using them.
- @578, R051: Companion: W = ⟨r², s⟩ gives the I₂(n) reflection arrangement of 146/043-053 (Deligne 1972, K(π,1)); LM scan 460's "voisin d'un groupe de tresses".
- @581, R054: Sign calibration for the Stokes check G. requests (146/044, 047, 049): with z = v₂/v₁ the +i eigenline falls in the hemisphere with the opposite boundary label; the decoration on Ω(V) must be settled.
- @585, R059: 146/046 margin "On peut lever l'ambiguïté": choosing one alternating n-gon kills the central half-turn only for odd n; for even n a parity qualification is needed.
- @587, R066: Sign check (146/051, 053): scalar inversion "renverse" the fibre loop (degree −1 on H₁); fix the orientation of each generator.
- @588, R067: Notation (146/052-053): τ is complex conjugation here but antipodism in LM_140-2 scan 463; do not identify letters across files.
- @589, R068: 146/053, 055: D×μ_m×{1,τ} is a semidirect product (τλτ^{−1} = λ̄); the cardinality 8n² is unaffected.
- @592, R074: Material evidence: the June 1978 Petrich examination (146/072-073) also appears in LM 140-1 scans 005, 007; recurrent paper substrate.
- @593, R075: Second-pass check for the drawings of 146/060, 064: the graph of ten 2-subsets of a 5-set joined when disjoint (S₅-invariant).
- @594, R079: The inserted "on suppose k de car. nulle" (146/063) is used (principal units divisible; 1+t has no p-th root in F_p[[t]]).
- @597, R083: Companion: "équation du monogone, victoire !" (146/065, 067) parametrizes y² = x(x−1) by x = −(z−1)²/(4z).
- @599, R086: 146/067: the relations under "Cartes" have no order-three face relation; LM3's cube relation must not be imported.
- @601, R093: Reading "60?" (146/071): it could come from lcm(20,12) under the inverse forgetful identity; neither premise proved.
- @604, R096: 146/073: the triple count gives ν = (n−1)(n−2)/2; removing the factor two from the squared sections needs a sign argument; the overwritten 2ν|4ν and "6|σ" stay unnormalized.
- @607, R100: 146/077: the counts R = 120, F = 12, A = 30, S = 20, 2×(6+15+10) = 62 fit flags of the icosahedron/dodecahedron; "bidodécagone|bidodécaèdre" stays uncertain.
- @609, R104: Error of the page: the generation assertion after (14) (146/083-087) fails (BC₂⊔BC₂ → BC₂ example); the text also writes T for T̃.
- @613, R111: 146/090, 096: "par suite on a Ũ₀ = Ũ" needs μ discrete and embedded (Q ⊂ R counterexample).
- @615, R115: The revision "groupes commutatifs" → "extension centrale" (146/092-093) is substantive; later uses of E as a constant coefficient group need extra hypotheses.
- @616, R116: 146/097, (21): a free action through Aut(id) forces E abelian; a noncommutative extension needs a band formulation.
- @617, R118: 146/094-095, "on n'a pas utilisé la commutativité de μ": y^{−1}x is not origin-free for nonabelian μ.
- @619, R120: 146/095, (17): the literal equivalence drops the torsor datum E (π = 1 counterexample); a 2-categorical or quotient formulation is needed.

### MPL_146_100-134

- @622, R03: 146/100, "comme … Lim (finie)": finite colimits do not preserve free actions (coequalizer example); a property of this diagram is needed.

### MPL_147_003-047

- @633, N006: 147/007-008: the inserted "(relatif)" is substantive: relative, not absolute, normalization over nonreduced bases.
- @634, N007: Companion: explicit dual-number counterexample for G.'s "faux tel quel !" (147/007-008): x ↦ x + εx³ breaks fullness, also on the three-punctured line.
- @635, N008: Companion: G.'s repair "remplacer X par (X̂,I)" (147/008) works for the constructed class: Y is recovered as End(J), J the Fitting ideal of the nodes.
- @636, N010: 147/007, 017: constructive standard families exclude smoothing directions (uv = ε); the fibrewise clause must keep the "standard" hypothesis.
- @638, N014: Reading (147/010): "boucle fermée" is a self-loop; smooth components do not make the graph a tree.
- @655, N049: Error of the page (147/031, "encore une immersion, fermée cette fois"): the map (37) is not a monomorphism (genus-two curve from P¹ with 0∼∞, 1∼3, marked 7).
- @656, N050: Error of the page (147/031, "propre et lisse … paraît a priori curieux !"): the stratum closure has local equation uv = 0 there, singular also on the coarse space.
- @661, N060: 147/038: the diagonal marginal addition (collapsed arc endpoints with equal image) is indispensable; keep it with (45).
- @665, N064: The cancelled condition 4 on 147/041 is not necessary (theta graph with one edge contracted); its damaged indices stay a reading question.

### MPL_147_048-137

- @682, N060-01: Error of the page: the last row of (74) (147/060, "Γ opère trivialement") fails for two genus-one vertices joined by an edge (factor swap).
- @687, N063-03: 147/063-064, "qui fait de M̂₁,₁ une gerbe": over the compactification the gerbe assertion fails under the ordinary meanings (cusp stabilizers; 5/12 vs 1/6); restrict it to the open part or change the target.
- @688, N064-02: 147/064, "ne se coupent qu'en les pts 2 et 3": the sections j = 0 and j = 1728 meet in Spec Z/1728 (lengths 6 and 3); the reduced statement is meant.
- @698, R074-01: 147/074: the marginal choice g₂ = 1, g₁ = g−2 needs g ≥ 2; g = 1 must be checked separately.
- @700, R075-02: Reading (147/075, "à isom. unique près"): reversal of a total order gives the same unoriented chain; locate the orientation or endpoint convention before sharpening the claim.
- @710, R092-01: Consistency across pages: the lattice is indexed by edges Z^A on 147/080, 085 and by oriented branches Z^{Ã} on 104; one smoothing parameter per node versus paired branches must be reconciled.
- @719, R107.2: 147/107, 109: the cancelled least-element assumption is structural; 111-112 again use e_J; the extension of the codimension function must be specified.
- @720, R109.4: 147/109-110: a two-element antichain shows that d(J) needs a least element or a supporting-intersection datum.
- @723, R116-02: 147/116, axiom c): a finite discrete internal category satisfies the literal a)-c) but not source-target monicity; the intended reading of c) must be fixed.
- @725, R119-02: Convention (147/119, "mono local, qui garde un sens dans tout site"): pointwise injectivity is not enough (cusp t ↦ (t², t³) over dual numbers).
- @726, R121-02: 147/121, "Cette axiomatique inclut des cas tels que": an immersed nodal curve as D₁ with D₂ empty satisfies the axioms but misses the double-point incidence; 127's genuine-divisor hypothesis is needed.
- @732, R134-03: 147/134-135, (220): the degeneracy map is an isomorphism componentwise only; the whole-map claim needs a reduction removing the components (d,e), d > e.
- @734, R137-01: 147/137, (227): check whether "squelette" is the closed union of multiple intersections or its normalization (three coordinate hyperplanes; Deligne 1971, §3.1.4).

### MPL_147_138-190

- @736, 180-02: Reading (147/180): "on ne reconstitue pas" concerns the groupoid colimit (trivial), not the homotopy pushout (S²); do not paraphrase it as an impossibility.
- @737, 180-03: Companion: Treumann 2009, Example 1.4 gives the same single-arrow exit-path category for the stratified sphere of 147/180.
- @738, 180-04: Companion: G.'s "question générale" on 147/180 (homotopy type of a recollement topos) is addressed by the exit-path literature: Treumann 2009 (Example 1.6, Thm 7.14) supplies the missing 2-datum (Z of 2-automorphisms) for tame conical stratifications.
- @741, 181-03: 147/181: "on satisfait à a) b) c)" does not give local finiteness after refinement ({0} ∪ {1/n}); d) is needed.

### MPL_148_029-072

- @753, R07: Reading test (148/031, 034, 036): "Sauf I₄ … 'réelles'" and "contient le cas pyramide carrée" with the real structures z̄ and iz̄ on {1,−1,i,−i,∞}.
- @755, R11: 148/037-039: μ = 0 gives z⁴+1 with distinct roots (the 034 configuration); why 0 is removed from the parameter line is a reading question.
- @757, R13: 148/041: at (g,ν) = (1,0) the three marginal stability expressions give 0 ≥ 0, 0 ≥ 1, 2 ≥ 3; the intended range must be checked.
- @763, R38: 148/067, "OK ssi … pair": even total perimeter can give a negative inverse weight ((1,1,4) ↦ (2,2,−1)); nonnegativity must be checked.
- @764, R40: 148/067: the bigon count gives 11 faces for (3,5,4); the over-annotation α+β+γ−2 (2 uncertain) gives 10.
- @765, R41: Second-pass incidence record for the contour drawings of 148/032, 068-069 (TikZ overlaps kept unresolved).
- @766, R43: 148/072 ("découpage pantalonique d'une carte (triangulée)"): match the red curves to the weighted graph by an explicit incidence map; digits 15|25 and 7|4 uncertain.

### MPL_14_002-044

- @772, M11: Convention (14/009, 013): ε(j(t)) = t², weight +2 for L = Q(−1); Q(1) has character ε^{−1}.
- @776, M24a: Companion: Künnemann 1993, Thms 5.1-5.2 (Lefschetz decomposition in relative Chow motives of abelian schemes) for 14/003, 009.
- @779, M27: Reading of "indép. du foncteur" (14/011): the motivic group acts on L by the Tate character; for P¹ the group G_m cannot contain the Lefschetz sl₂, so no universal inclusion inducing the Lefschetz action exists.
- @780, M28: Companion: Nori-Ayoub comparison G_N ≅ G_A (Choudhury-Gallauer 2017, Thm 9.1) for 14/003, 011.
- @781, M28a: Companion: Arapura 2013, Thm 6.4.1 (pure Nori motives ≅ André's motivated motives) for 14/003.
- @784, A01: Companion: G.'s "des signes différents !!" (14/021): δ*r_*(p*z·q*z) = s_*(z²) links it to the divisor D of cote 44/009; degree −2d gives both signs (war-game H9).
- @785, A03: Companion: the Albanese-equivalence definition (14/024-025) answers cote 44/008's "une relation d'équivalence que je ne sais pas bien identifier"; the ring structure is Michel Hua's project's finding 14-albanese-equivalence-ring.
- @787, A12: 14/030, "On ignore si cet ν est lin. équiv. à 0": on E×E some boxes b(x,y) are rationally nontrivial (Albanese kernel, Mumford) yet Albanese-trivial.
- @790, A22: 14/035, "Si Nφ est alg., φ l'est": false for arbitrary maps (2-torsion example on E); check whether the ambient group is already restricted by condition 1.
- @795, A36: Companion: ACV25 (Thms 1, 12.12) autoduality with −ᵗZ∘Z for 14/019, 037; positivity open in char p (their Conj. 5.1).
- @798, RT2: The letter's A with algebraic equivalence ("Le premier cas qui échappe … i=1, n=3") fails for the very general quintic threefold (Clemens 1983); the printed version with homological classes avoids it.
- @799, RT5: Companion: "a été vérifié pr Mumford" (cote 14/042) matches Tate 1966, §1, p. 134 (Mumford from Deuring).

### MPL_150_001-043

- @803, Q1b: Glossary anchors (150/012-015, 022-023 vs 147/140-142): conical neighbourhood, collar, strictness, "découpage cônique"; none defines "tubulure" or "ombre".
- @804, Q1c: Reading (150/012, 022-023): the uncertain "ombre" cannot be an ordinary formal completion (deleting its support leaves nothing).
- @809, R01: Convention (150/003): upper sets are open here; BISITE G.10 and WG2 B15 use downsets open, so comparisons pass to the opposite poset.
- @810, R05: 150/005, "implique la 'fidélité'": fails without a nonredundancy or density hypothesis (X_a = X_b = X).
- @817, R17: 150/016-017: condition (12b) writes Y where the later description uses Y′; the point {0} in a collar is conical but not cylindrical (purity).
- @820, R21a: 150/020: the displayed tuple loses the data Y_i = X_i ∩ Y (X_i = ∅ vs {0} give the same tuple); scans 023-024 keep a separate Y′.
- @822, R29a: 150/029, "k′ = Inf(k,j′) existe": false from condition c) alone (poset u,v < a,b < j); a relative meaning or a global-meet hypothesis is needed.

### MPL_150_044-084

- @836, N01: 150/044-045: (28) with condition c) does not give the claimed flag property (diamond poset); scan 065 replaces the hypothesis by disjointness for noncomparable indices.
- @842, N08: Convention (150/064, "n'ont … rien de surjectif"): fibrant sources need not be surjective; a restatement must allow empty fibres.

### MPL_151_032-075

- @875, 046-03: Error of the page (151/046, (4)): the absolute closed-graph assertion fails without separation (Sierpiński space).
- @878, 052-02: 151/051-052: after the change to strict flags, formula (20) fails (one-point test: {p}⊔{p} vs {p}); (22) survives.
- @879, 053-03: Error of the page: the closed-embedding conclusion of the corollary on 151/053 fails (triangle faces with a label swap, 19-point example).
- @882, 057-02: 151/055-058: formula (4) needs the optional reduction of 055 first (duplicate pieces X₀ = X₁ = {p}).
- @885, 060-04: 151/060: the containment-selected union of (12) does not agree with (11) after pullback (four-point example); (11) is correct, the rewrite is not.
- @887, 064-02: 151/063-064: under the broad axioms the germs do not detect successor indices (discrete fork); the inserted nonemptiness premise fails.
- @888, 064-03: 151/064: the density premise fails for closed pieces ([0,1/2] ⊂ [0,1]).
- @891, 067-03: 151/067, (24): a degree function need not exist (five-element poset with chains of lengths 2 and 3).
- @894, 071-04: Error of the page: the R formula of 151/057, 060 is not stable under inverse image (four-point Boolean poset pulled back to {b}).
- @898, L-02: Companion: the connecting map "l'image de π₂(Y)" on 151/032-034 is the earlier explicit form of the term behind G.'s hesitation over the left end of (37) on 149/133-135.

### MPL_152+120

- @902, P05: 152/004: σ = (1 3) on three edges satisfies neither alternative of the recursion; a translation to the nonpenetration criterion of 152/010 must treat fixed edges.
- @909, P17: Dating: the printout "19 MAY 82 JOB EXECUTION DATE" (152/009, with 003, 006, 012) dates the paper, not the writing.
- @910, R02: Companion: "un magnifique succès" (151/042-043): gluing two neutral A-gerbes gives H²(S², A) ≅ A via (n,b) ↦ (n, b+na); verified.
- @922, A120-02: Reading (120/004-005): the revision R₀ ≠ ∅ → Card R₀ ≥ 2 is what makes the empty-set argument work; {x} ∈ R^n on 005 stays a reading question.

### MPL_154_077-126

- @938, Classification of the package: Classification of cote 154 (077-126): pseudoline systems and the "surface modulaire" of relative positions of Esquisse §8 (published p. 41); not the 1986 geometry of forms (letter to Brown, 17 June 1986); "tame" only in the motivating sense.
- @939, Failed identifications, collars, and the final counting sheet: Edition of 154/112-125: incidence NB on 112 (supporting lines), withdrawn gluings on 113 ("non ! (le sommet s disparaîtrait !)", "je n'arrive pas à suivre les 'circuits autour d'un trou'"), count changes N′ = N−1 vs N′ = N on 114-115, three question marks on 117, the cancelled collar and recovery proposals on 118, the corrected exceptional-edge criterion, the tuple on 119, g = 1−χ on 120 (not the usual genus), the quartic double count, 2n(n−1) stable flags, the sign (n−2) −|+ (n−3) = 2n−5, the uncertain "?" on 125.

### MPL_154_127-176

- @940, P01: Identification: "surface cellulaire des positions relatives", X* = Rel(Σ) (154/151) is the Esquisse §8 surface (published p. 41).
- @945, D01: Documentary: the 50 scans 127-176 carry marginal pages 126-175 (scan N = page N−1); isolated "1", "4" and "PAGE 1" are not page counts.
- @946, D02: Dating: "1.1.84" and "Compléments et rectifications sur les facettes exceptionnelles de (X|𝒳, K)" lie inside the cancelled passage of 154/160.
- @947, D03: Dating: printout dates (19 AUG 82, 25/8/82, 06/28/82, 08/19/82, DATE = 82.231) date the reused paper (154/128-173), not the writing.
- @948, D04: Catalogue title "[Système de pseudo-droites]" vs local captions (154/136, 153, 155, 160, 166); no cover in this selection.
- @955, M02: 154/157: ρ_s = σ₂σ₁, ρ_f = σ₁σ₀, ρ_sρ_f = σ match Esquisse §3 (119/12); within that convention ρ_sρ_f = σ₂σ₀, so the identification with the manuscript's σ is a consistency check; no product order to be changed.
- @957, M05: Reading (154/142): with the factor n−2 the count is 3·C(n,4) (pairs of disjoint edges of K_n), ~n⁴/8; the asymptotic does not decide n−1|n−2.
- @972, I03: Reading (154/171 (b)): "section du rev. à deux feuillets" (both words uncertain) is global data; a section exists only if the side monodromy is trivial.
- @980, W02: 154/138: "sont principales" is deleted; the replacement reads "de tricalité|criticalité ≥ 2"; record the revision.
- @981, W03: 154/140: the σ₁ description is corrected (a⁺↔b⁺, a⁻↔b⁻); the cancelled σ = σ₁σ′ is not a refutation of that identity.
- @982, W04: 154/133, 151: orientation repairs ("change|fixe" → "fixe" for ω̄; "gauche" → "droite"); the cancelled fragment on 151 belongs to the incomplete construction.
- @983, W05: 154/153: fuseau terminology revised (couloirs, semi-couloirs; "unilatéraux|triviaux" inserted); "Sauf dans cas triviaux" is an exception clause.
- @984, W08: Inventory of cancelled trials and replaced labels on 154/135-172 ("A B C D E F G", 6 ↔ 7 at 172); none is a withdrawn theorem.
- @985, W09: 154/155, 158: "n'est … pas" kept after cancelling "jamais"; "système de trois droites" → "triangle".
- @986, W10: 154/171: replacements in the K,L conditions ("on a L ⊂ X", "1-compl." cancelled; "pair"; ν_a|ℓ_a; ν′_s|ν_s cancelled before ε_s).

### MPL_156-1+156-2

- @1000, A12: Error of the page (156-1/010): restriction to an arbitrary subset does not preserve F4 (ordered set with two middle chains); a closure condition is needed (@1001).
- @1004, A22: G.'s retraction "n'est pas filtrante croissante!" (156-1/021-022) is confirmed by the fork order Q ⊕ (Q ⊔ Q).
- @1006, A24: Error of the page (156-1/023): the two formulations of F6 are not equivalent (singular endpoints u, v above Q ∩ [0,1)).
- @1007, A25: The margin on 156-1/023 ("celles … qui sont régulières") is what makes the equivalence work: regular other endpoints suffice.
- @1010, B07: 156-2/004-005, 011: "Ficelle réduite est connexe" holds for point endpoints; the unrestricted connectedness claim on 011 does not (see @1017).
- @1012, B13: The gluing lemma of 156-2/007 fails literally on Q (no compact cone neighbourhood); the intended covered-space use is unaffected.
- @1015, B18: Reading (156-2/009): the repeated F₁ in the "quintuplets" tuple is doubtful; the prose names F₁, F₂, F₃ with h₂₁, h₃₂.
- @1017, B23: Error of the page (156-2/011, "qu'il soit connexe"): [0,1]×{±1} with A, B the endpoint pairs satisfies Fic a-d but is disconnected.
- @1018, B25: Error of the page (156-2/011): A = {0,1}, B = {1/2} on [0,1] satisfies Fic a-d, so the classification into two oriented classes needs connected endpoints.
- @1019, B27: 156-2/011: a tripod with a leaf arm enlarged witnesses G.'s own retraction of the enlargement statement ("(Connexité)").
- @1034, B52: Proof of the sufficiency assertion of 156-2/011 ("Il y a alors … une structure de ficelle réduite") for connected nontrivial finite polyhedra (two leaves of a spanning tree).
- @1035, B53: Proof of "Si X est un segment cette str. est unique" (156-2/011) for finite polyhedra: the reduced endpoint pair is unique exactly for the arc.

### MPL_15_087-138

- @1052, T12: Error of the page (cote 15/121, 123, "d'indice fini"): the lattice generated by the i − i′ has infinite index in X_*, since ε_* kills it and ε_*(j) = 2; ker ε_* is the candidate target.
- @1055, T18b: Companion: "Giraud?" (cote 15/135): Deligne-Milne, Prop. 5.8 (gerbe of liftings of the canonical section) cites Giraud 1971, IV 3.2.1.
- @1060, T25: Companion: Kahn 2025 (Thm 5.10, Prop. 10.1, Thm 10.2) proves 1 → G_N(k̄) → G_N(k) → Γ_k → 1 for rational Nori motives, the exactness behind "composante neutre" (15/135-137).

### MPL_15_195-228+18_002-017

- @1076, A10: Test for the level formula on 15/205 ("provient d'un sous-motif"): the intersection must be stable under the Hodge decomposition, not only under conjugation.
- @1078, A33: Companion: the margin of 15/223 ("non isomorphes comme anneaux; remplacer Z par R??") is answered existentially by Charles 2009 (conjugate varieties with non-isomorphic real cohomology algebras).
- @1080, P03: Companion: the "cristal filtré" description (18/005) compares with Colmez-Fontaine 2000 (weakly admissible filtered (φ,N)-modules); the sheet states no weak admissibility.
- @1082, P12: Reading (18/011): "Q(φ₁) est indépendant du plongement" may be the reflex field of the Hodge cocharacter's conjugacy class; the final margin is partly illegible.
- @1098, R15: 15/198, 200: the highest-weight corollary and "ajouter la stabilité par les binomiaux (H n)" need their coefficient ring and lattice recovered before comparison with an integral Lefschetz model.

### MPL_16+47+54+44

- @1102, R1: Error of the page (cote 16/014, "sur ℤ !"): in the integral exterior model ξ² = 2·vol (ξⁿ = n!·vol), so hard Lefschetz fails integrally in degree 0; rational coefficients or another lattice are needed.
- @1103, R2: Cote 16/010-014: contraction Λ_std and the unweighted lowering operator differ (ΛL(1) = 2 vs 1); the blank (6.5) must fix the convention.
- @1104, R3: Companion: g_t = 1 + tL (16/016-017) realizes G.'s circled "Non": L fixed, Λ and the projectors moved ("Il faut donc se donner en même temps L et les πᵢ").
- @1107, R6: Cote 16/054: the polynomial argument fails over F₂ (k³ has no algebra generator) unless an infinitude hypothesis was in the antecedent text.
- @1109, R9: Companion: Matlis 1958 (Thm 2.5, Prop. 3.1, Thm 3.10) for the injective-hull statements of the reused typescript (16/039).
- @1111, R13: Companion: Mumford 1961 (p. 6; pp. 10-11) for "en vertu de MUMFORD … définie négative" (16/019); the étale-duality compatibility claimed there needs its own comparison.
- @1115, R22: Cote 16/054, criterion (a)-(c): "B finie sur A et B/m.B étale" does not give étale without flatness (A = k[t], B = A × A/(t)).
- @1129, F5: Cote 47/004-005: the displayed K-theory theorem omits the line class; the corrected composite gives (−1)^g[π_A^*τ_A](−1_A)^*x.
- @1130, F7: Cote 47/008, "à faire une vérification de compatibilité.....": proof plan via perfectness of the Poincaré pushforward and the zero section.
- @1132, F9: Cote 47/006: the first displayed corollary omits the zero-section pushforward e_*τ[−g].
- @1133, F10: Sign test for remarks 1(a)-(c) on 47/008: Φ(F⊗P_t) = T_t^*Φ(F) while convolution by δ_u is T_{−u}^*; the signs of "L_t … τ[−n]e_{−t}" and "*e_t" must agree.
- @1135, F12: Cote 47/009: the total-Chern-class display "(1−D′/χ)^χ", "χ(χ−1)/(2χ)" has a numerical error; correct coefficients c_k = (−1)^k (r−1)…(r−k+1)/(k! r^{k−1}) D′^k.
- @1136, F13: Test of "Elles sont vraies … mod équivalence cohomologique" (47/009) on E₁×E₂.
- @1137, F14: Cote 47/009, "provient d'un cycle à coeff. entiers": the integral coefficient is (−1)^k r c_k(E), not c_k(E).
- @1138, F15: Companion: G.'s "ces formules sont-elles bien vraies mod torsion?" (47/009) compares with Beckmann-de Gaay Fortman 2023, Thm 3.8 (integral Fourier transform).
- @1141, F20: Cote 47/011, remark 4: F̌ versus Φ_L(F)^∨; the dual output needs the duality convention fixed.
- @1142, D02: Companion: Coleman 1998, Thm 1.1 for the boxed duality on 54/003 and 54/005.
- @1144, D07: Cote 44/003, "est exact et fidèle": faithful flatness of completion needs the ideal in the Jacobson radical.
- @1145, D11: Companion: G.'s "Je suis moralement sûr" (44/008) on general intermediate Jacobians: Ottem-Suzuki 2020 (Cor. 1.2, 4.2) obstruct one identification.
- @1148, D16: Cote 16/025, "Condition d'associativité": nondegeneracy of φ and Q alone does not give the algebra (two-dimensional counterexample).
- @1150, D19: Cote 16/029, "4 (ou 6?)": a conditional six-dimensional example decides the dimension under the operator convention.

### MPL_18_018-062

- @1156, RH06: Cote 18/035: the displayed natural isomorphism has a sign defect on tensor products, confirming "n'est pas compatible avec le produit tensoriel".
- @1157, RH07: Cote 18/035, 037, "Il semble": the tensor nonisomorphism is detected on an Artin line, confirming the tentative claim.
- @1159, RH10: Error of the page (18/036, 038, "somme de puissances tensorielles de Q(2)"): the even-Tate converse fails on the Artin-Tate summand.
- @1177, P25: Companion: G.'s own printed transcendence conjecture is the period witness to cite for 18/045, 059.
- @1188, R06: Edition: the Borel argument on reused sheets runs 18/028 (steps 1-3) then 18/024 (step 4), not in scan order.
- @1193, T03: Edition: the printed source pagination ("A-18", "A-20", "2-3" … "2-12") of the reused sheets 18/018-058 recovers three local continuations.

### MPL_2

- @1195, L02: Correction: the displayed relations (2/028-029) do not enforce λ-compatibility; the abbreviated relation list of Michel Hua's project's finding 2-chern-ring-gamma-comparison is too broad.
- @1198, L08: G.'s "Non" on 2/022 (noninjectivity for projective space) has an explicit homogeneous witness; supports Michel Hua's project's finding 2-chern-ring-not-injective-pn.
- @1202, S03: Conditional reconstruction of the full-faithfulness claim Lim_n D_parf(i_n) → D_Z(X) on 2/033 (Noetherian affine case).
- @1204, S08: Construction ambiguity on 2/035 ("en prenant tjrs des cycles sur X à support Φ"): rational equivalence inside the supports vs the image in the Chow group.

### MPL_31_002-051

- @1211, N023: Edition: the construction announced on 31/011 continues on 015, 013, 017 (logical order differs from scan order).
- @1213, N029: The margin "suffit-il … fini ??" (31/020) is answered negatively by a real-closure test.
- @1214, N030: Cote 31/020: the strict "cd(X) < 2 dim X + 1" fails for Spec F₃ (nontrivial Z/2-torsor); SGA 4 X 6.2 prints ≤; drafting slip.
- @1215, N033: Cote 31/022: "cd_r(k′) = cd_r(k) + deg tr k′/k" fails for r = p in characteristic p (F_p(t) over F_p).
- @1219, N048: Companion: the three deletions on 31/028 (page 78 of 0_III 13.7.7) match the printed EGA III₂ errata.
- @1222, N057: Cote 31/038, "donc tout simplexe en un simplexe disjoint": false for closed simplices (Z acting on the simplicial line); open simplices or a subdivision are needed.
- @1225, N073: Reading (31/045, "un corps local … quel"): whether C((t)) is excluded must be decided.
- @1227, N080: Cote 31/049, "car H^1(k,Gl(n))=0": the linear structure is a choice; (x,y) ↦ (x+y^p, y) is an additive, nonlinear automorphism of G_a² over F_p.
- @1230, N089: G.'s question "un vrai isomorphisme?" (31/051) is answered negatively by the note's K = C(t) cocycle killed by the coefficient inclusion.
- @1232, T06: Edition: the typewritten and handwritten numerals of cote 31 are independent numbering systems (scans 012-032).
- @1233, T07: Edition/dating: interior headings and the ENS stationery of cote 31 (scans 004, 021, 035, 039, 047, 051).

### MPL_33_002-049_chatB

- @1236, N06: Cote 33/006: the GAGA margin "équivalence des catégories" needs its (algebraic) constructibility convention recovered.
- @1238, N18: Cote 33/016, 018: the open-immersion extension needs torsion prime to the characteristic (wild coefficients on G_m ⊂ A¹ in characteristic p).
- @1240, N31: Cote 33/034, "fibres conn. non vides": must mean geometrically connected (Spec C → Spec R).
- @1242, N37: Cote 33/006: the nonproper analytic comparison fails for non-constructible F = ⊕ i_{m*}A on A¹_C; finiteness must be kept.
- @1243, N38: Cote 33/010: for f proper smooth the cohomology need not be free over a fixed ring (Z/4 local system on an elliptic curve); a flatness hypothesis is implicit.
- @1246, N45: Cote 33/042: the degree bound needs a quasi-compact base (∐ P^r over ∐ Spec k).
- @1249, N50: Cote 33/048: the boundary test on A²∖{0} → A¹ excludes the stronger partial-range reading only.
- @1250, N53: Error of the page (33/005): the Coxeter contraction definition assigns conflicting values (m′_{hk} = m_{hk} overlaps m′_{ik} = m_{ik} + m_{jk}).
- @1251, N55: Cote 33/013: the type-A endpoint pairing fails at ℓ = 1, which the heading allows.
- @1252, N57: Error of the page (33/023): the E6 exponent equation prints "(12+1)" for (11+1); with exponents 1,5,7,11 the remaining pair is 4, 8 ((m+1)(m′+1) = 45).
- @1253, N58: Cote 33/035: n(u,v) = −1 alone does not give equal lengths and order 3 (B₂ gives order 4); an ordering qualification is needed.
- @1254, N59: Cote 33/033, 035: the global root-length normalization needs irreducibility or a per-component convention.
- @1255, N60: Cote 33/037, 049: the E8 highest-root sign conflicts with the displayed dual bases (α̃ = ω₈ vs α₈ = 2ω₈ − ω₇).
- @1256, N62: Cote 33/037, 049: the E8 weight and ρ tables check out against the dual-coroot convention (record for the second pass).
- @1257, N68: Error of the English typescript (33/041, 043): the product-of-stalks Hom formula fails on the Sierpiński space.
- @1258, N69: Correction (33/041, 043): the adjunction has (P_X F)_x, not F_x, as first stalk object.
- @1259, N72: Repair (33/039): the reflection is proved without the false product-Hom formula, under the stated set and monicity hypotheses.
- @1260, N74: Provenance lead: J. W. Gray's Columbia mimeograph on category-valued sheaves for the English typescript of 33/039-045 (via Kleisli-Wu); unconfirmed.
- @1264, N80: Cote 33/033, 035: the automorphism-quotient claim fails for unequal reducible components ({±e₁, ±√2e₂}).
- @1265, N87: Cote 33/028, 030: the point-class normalization must distinguish rational from arbitrary closed points (inseparable points over imperfect k).

### MPL_33_002-049

- @1268, N05: Cote 33/006: scope of the categorical GAGA margin (analytic graph w = e^z); same matter as @1236.
- @1273, N16: Cote 33/014: "λ ∈ Z/nZ" must be a unit for the rescaled section to stay primitive.
- @1274, N20: Cote 33/020: the quasi-finite vanishing "R^i_!f_*(F) = 0" holds for i > 0 only (f = id, i = 0).
- @1278, N30: Cote 33/028, 030: the relative class diagram needs the support Y proper over the base.
- @1280, N33: Cote 33/028, 034: same as @1240 (geometrically connected fibres).
- @1284, N49: Cote 33/013: rank-one exception; same as @1251.
- @1285, N53: Cote 33/023: E6 exponent product; same as @1252.
- @1286, N54: Cote 33/035: ordered B₂ pair; same as @1253.
- @1287, N55: Cote 33/033, 035: length labels for reducible systems; same as @1254.
- @1288, N57: Cote 33/019, 037, 049: E8 highest-root pairing; same as @1255.
- @1289, N63: Cote 33/041, 043: product-of-stalks Hom; same as @1257.

### MPL_33_098-146

- @1301, N28: Reading of "d'additivité pour un mapping cylindre" (33/132): chain-level data, not additivity for every endomorphism of a distinguished triangle.
- @1303, N31: Cote 33/138, 140: the uniform Tor bound "tout pt géom" must be kept (pointwise bounds do not suffice on infinite disjoint unions).
- @1305, N38: Cote 33/146: "et borné" is deleted in the insertion; the reading has mathematical consequences.
- @1309, N50: Error of the English typescript (33/135): "then R = k[[x₁,…,x_n]]" needs completeness (Q[x,y]_{(x,y)}).
- @1310, N51: English typescript (33/135): equal characteristic alone does not give a coefficient field (Q[x,y]_{(x²−2,y)}).
- @1312, N53: Edition: the cyclic generator-lifting lemma's proof runs across 33/143 then 141 (printed order of the reused typescript).
- @1313, N54: Error of the English typescript (33/145): condition (c) admits k[ε]/ε² → k; m_y = m_x O_y must be required.
- @1314, N56: Provenance leads for the reused English typescripts (33/101-143): Auslander-Rim 1963 and Abhyankar 1960; unverified.

### MPL_33_147-181+34_002-017

- @1315, D11: Cote 33/148, 158: "plats de type fini en chaque degré !" with "bornés" deleted; degreewise finite is not a bounded trace model.
- @1317, D14: Cote 33/160: the "morphisme évident" uses a counit Ru_*u^! → id whose scope (u proper, or Ru_!) is unstated.
- @1319, D20: Companion: "Sujets de recherches" a (33/166), exterior powers in derived categories with λ-rings, is a programme item to set beside the later derived exterior powers (Dold-Puppe; Illusie).
- @1320, D21: Dating lead: "Dualité analytique", cohomological descent and the "site stratifiant" (33/166) as an early mention of stratifications (crystals line).
- @1321, D24: Cote 33/167: F ∈ D^b(X) without "c" cannot give constructible biduality; D^b_c is needed.
- @1322, D30: Cote 33/172: clause (i) must be read with local Ext (global Ext fails at Spec F₇).
- @1323, D33: Cote 33/172, 174: injective stalks do not give an injective sheaf (finite-site model); the reading must fix which is claimed.
- @1324, D36: Cote 33/178: if the uncertain word is "codim", the Ext needs a shift (smooth-curve test).
- @1326, M08: Cote 34/005-006: "surface de degré ≥4" needs "générale" (the Fermat quartic contains a line).
- @1332, M27: Cote 34/017, "centrale": centrality does not give a group-theoretic splitting (C[[t]] test); the reading must not infer one.
- @1333, R02: Edition: the small-to-big Zariski comparison continues from 33/153 (source p. 7) to 33/151 (p. 8): "Tout a été démontré sauf" is answered there.
- @1339, R22: Cote 33/179: "KJρ = Kf" having the same solutions as Jρ = f is an extra regularization step; the continuation is missing.

### MPL_36_002-052

- @1343, N14: Cote 36/006: of the two Dirac normalizations f(e) = 1 and f(e) = #G, the second integrates to 1 under normalized counting measure.
- @1344, N21: Cote 36/006, "générique simple": the deformation counterexample needs a family specializing to E×F with geometrically simple generic fibre; a lifted formal or p-divisible subgroup does not contradict simplicity, an abelian subvariety does.
- @1346, N34: Companion: Deligne 1974, §10.2.1 (biextensions of two-term complexes) for the construction of 36/029-033.
- @1350, N52: Cote 36/040: the vanishing question under the absolute reading fails for Spec R (H²(Spec R, G_m) = Z/2); a geometric reading is needed.
- @1353, N63: Cote 36/045: the Artin-Schreier identification with Frobenius-fixed H¹(A, O_A) needs H⁰(A, O_A)/(F−1) = 0 (base-field term).
- @1361, N85: Companion: the injective-presheaf statement of 36/049, 051 compares with the Stacks Project (tag 03AV as cited by the note).
- @1363, N89: Sign check (36/004, 007, 046): fix one convention for the Poincaré biextension and compute the torsion pairing on an elliptic curve against the cup-product convention.

### MPL_36_053-085+39

- @1366, N09: Error of the page (36/056): "φ(u+v) − φ(u−v) = 2(φ(u)+φ(v))" forces 2φ = 0; the parallelogram law has φ(u+v) + φ(u−v).
- @1368, N13: Error of the reused typescript (36/066): Δ_U ∩ Δ_V = Δ_{U∩V} fails (Z, H = 2Z, U = {0,±2}, V = {0,±3}).
- @1370, N20: Cote 36/061: gcd(μ_i d_i) = gcd(d_i)·gcd(μ_i) fails as algebra (d = 2, 3; μ = 1, 2); the multiplicity shortcut needs the theorem's hypotheses.
- @1371, N23: Cote 36/062, 071: the case formula for R ⊗ Z_ℓ needs a restriction on the ℓ-adic valuation of d′ (d′ = ℓ²).
- @1372, N25: Cote 36/063, "il résulte de (14)": a uniform annihilator does not give lim θ(ℓ^ν) = 0 (constant system Z/p); the transition maps must be used.
- @1373, N26: Cote 36/062-063: the struck restrictions on ℓ leave the twisted ℓ-adic corollary stated for every prime.
- @1377, N44: Cote 36/077: the all-level descent step needs a descended toric/abelian/unipotent filtration with finite multiplication by ℓ; bears on Michel Hua's project's conjecture 36-orthogonality-regular-adic-base.
- @1379, N49: Cote 36/073-079: "φ_ξ(M^I, M_0^I) = 0" gives inclusion in the orthogonal only; equality needs rank and saturation.
- @1381, N53: Cote 36/084: transpose and symmetry are distinct claims; the deleted "parfait" must be kept in the reading.
- @1383, N55: Cote 36/083-084: the rank-one quotient test fixes the sign of the discriminant pairing.
- @1384, N56: Cote 36/084: with residue weights δ_i ≠ 1 the discriminant formula need not give the autoduality on Ψ.
- @1385, N59: Companion: the "autodualité" of 36/083-084 compares with the later intersection-form treatment of Grothendieck's pairing on component groups, under regular-model hypotheses.
- @1389, N74: Repair (39/012, 015): coefficient extraction gives f(t)^{-1} ∈ A_n, completing the unit assertion.
- @1396, N83: Cote 39/015: "en car. 0 c'est équivalent à la stabilité par les ∂/∂x_i" needs the coefficient ring to contain Q.
- @1398, N90: Cote 39/019-020: the preparation theorem is stated for linearly topologized complete rings, without noetherian or local hypothesis; compare at that generality.
- @1401, N96: Cote 39/019-020: the heading "Th. de préparation" is followed by unique division; the normalized preparation factorization follows from it.
- @1402, N97: Companion: SGA 7 I, IX, Remark 2.6(a) for the "démonstration arithmétique" "(partiel!)" of 36/073-079, 084.

### MPL_43_094-142

- @1408, A11: Cote 43/133: "H¹(C, Q/Z) = Hom(T(J), Q/Z)" needs T(J) defined (all-prime Tate module).
- @1412, A23: Edition: the cancelled reciprocity draft (43/113) gives local Galois maps φ_x; its cancellation and its lack of a point-to-section argument must be kept in any comparison (LM6 B.22, F.43; FLAGGED_149 A9).
- @1415, A26: Audit: cote 43/094-142 does not state ∩_n G_m(S)^n = {1} for arithmetic S; only 149/085 is named as its source.
- @1417, D29: Cote 43/136, 140: the boxed support comparison marked "???" is tested in degree zero on P¹ ⊃ A¹ (note D29).
- @1420, F12: Companion: Oda 1969, Thm 1.1 and Cor. 1.3(ii) for the finite-level morphism behind Jacobian self-duality (43/133).
- @1423, F15: Companion: Oda, Cor. 5.11 is the filtered de Rham statement available for 43/133.
- @1425, F17: Cote 43/133: the duality of H¹(C, O_C) must say which semilinear operator (F or V) is paired.
- @1428, F21: Companion: Oda 1969, Prop. 1.8, Def. 1.9, Defs 1.13-1.14 and Prop. 1.15 contain a completed compatibility with its map named, for the self-duality margins of 43/133 and the "vérification de compatibilité" of 47/008.
- @1429, F22: Cote 43/133 "autodualité": the sign of Cartier biduality (Oda, Cor. 1.3(ii), Prop. 1.12) is part of the comparison.
- @1430, R03: Provenance: the reused homotopy typescript of 43/101, 103, 105 matches Atiyah's "Thom complexes" (theorem sequence, final conjecture, bibliography).
- @1431, R06: Error of the page (43/110): "Si l'inégalité est vérifiée, alors F est plat" fails (R = k[[t]], f = id test).
- @1435, R14: Edition: the fine-sheaf embedding runs from typed p. 87 (scan 141) to p. 88 (scan 139), reversed scan order.

### MPL_57_271-315

- @1447, P03: Audit: Michel Hua's project's finding 57-analytic-pic-completion-criterion is only partly witnessed on 57/271-272.
- @1448, P04: Convention: keep Pic/Pic^τ (57/275-277) distinct from Pic(U)/Pic(U)⁰ = NS(U) (16/019).
- @1451, E05: Cote 57/289-290 states ū₀ = p v̄₀ but excludes a global ū = p v̄ (class in the cross-Hom component); compare with Michel Hua's project's finding 57-ns-p-divisibility-generization.
- @1452, D01: Convention (57/291-292): T_p(M) = Hom(M, Q_p/Z_p) is contravariant, T^p(M) = lim M[p^n] covariant (Oda, Prop. 3.9).
- @1453, D02: Cote 57/292 (a)-(c): the equivalence "mod les groupes finis" needs localization on the target side too.
- @1454, D03: Cote 57/292 (i bis): the finite test group H must be nonzero, or the test quantified over all such groups.
- @1469, I05: Edition: locate the numerical criteria cited as (viii′ b′) and (viii e) on 57/314-315 before reading the closedness statements.

### MPL_60_036-070

- @1473, LF03: Cote 60/041, 043: averaging over I/U is not a tensor functor (I = C₂); "Il induit un hom. … virtuel" must be read additively.
- @1475, LF07: Cote 60/039-051: the stated local additivity forces μ to vanish ("mais μx … l'est"); the reading must reconcile the two.
- @1477, LF09: Cote 60/051, 053: weight alone does not give the written self-duality ("Supposons E de poids …, donc"); a finite-order character is a counterexample.
- @1478, LF11: Companion: G.'s "Donner une formule genre … Ogg" (60/047, 055, 059) is met by the Grothendieck-Ogg-Shafarevich conductor formula.
- @1479, LF16: Companion: the local-to-global epsilon problem "c) Donner une formule" (60/055, 059) has later theorems that need extra data.
- @1484, A01: Error of the exercise (cote 60, Hensel exercise 15): the factorization P̄ = Q̄·R̄ needs comaximal factors.
- @1485, A02: Error of the exercise (cote 60, 10a, f): "d_k(M/N) ⊂ d_k(M)" runs the other way.
- @1489, A06: Cote 60 exercise *2: "Montrer alors que F est réflexif" needs a nonzero source module.
- @1506, A24: Edition: the intersection counterexample (ex. 11) and the tensor counterexample of cote 60 use the same ring k[X², XY, Y²].

### MPL_62_002-050

- @1517, A25: Error of the page (62/016): the proper quotient C/Z₂ is not a torsor under an invertible vector bundle; sections must be deleted first.
- @1519, A28: Cote 62/017 N.B., "sans restriction de car": L^{⊗3} → E₃ is defined in every characteristic but is not a complement in characteristic 2.
- @1520, A31: Cote 62/017, "Ce n'est autre que le groupe affine à 1 variable": the displayed group is a central double cover of the affine group.
- @1521, B02: Cote 62/019, "Ext. Kummérienne de gr Z/3": a cube root of a unit gives a μ₃-torsor, not a Z/3-torsor, unless μ₃ is trivialized.
- @1526, B13: Error of the page (62/034): "P¹_S/(Z/3) est can. isomorphe à un fibré principal" holds only after deleting two sections.
- @1529, C09: G.'s "quels i conviennent ??" (62/019, 046): the branch indices give local divisibility tests for i over a DVR.
- @1530, C10: Cote 62/046: codimension-one unramifiedness is not enough on a singular normal base (k[[x,y,z]]/(xy − z²), i = x).
- @1531, C12: Cote 62/048, "H¹(S, Z/3)": the order-three stabilizer is μ₃; the classification at i = 1 carries a cyclotomic twist.
- @1532, C13: Cote 62/048, "si i=0", "si i=1": infinitesimal special fibres are not just stabilizer torsors (dual-number base).
- @1534, C16: Cote 62/016, 042-050: the final classification of genus-0 curves with section and trisection forgets the quadratic twist of the elliptic curve.
- @1543, D04: Error of the page (62/024): "A_pE × A_qF ⊂ A_n(E×F) (p, q ≤ n)" is reversed for a decreasing filtration (k[[u]] test).
- @1545, D09: Cote 62/043: "le composé de deux homomorphismes est un homomorphisme" fails for strict topological homomorphisms.
- @1546, D11: Cote 62/047, 045: "U(g) … noethérien" needs g of finite type.
- @1554, E02: Convention (62/004, 014-017): the Lie line is dual to the invariant-differential line; the "chgt de signe" under inversion must be stated with it.

### MPL_84_097-145

- @1567, A36: Cote 84/119-120: the lemma needs a closed subscheme ("un sous-schéma fermé de X donc à un idéal").
- @1573, B11: Sign test of the cocycle calculation (84/132).
- @1576, B24: Cote 84/144: a shear shows the defining relation as written misses a compatibility.
- @1580, C06: Edition: scan 84/143 carries printed p. 480; the supposed page-480 gap is filled (neighbours 473, 474).
- @1581, C07: Dating: the typed sequence (July 1976, "il y a cinq ans"; 84/131 "il y a quatre ans"; 84/139 August 1979-October 1980) suggests a year for the typing, not for the mathematics.

### MPL_84_146-193

- @1586, E162.1: Cote 84/162: π′ = π − (χ−1)·id leaves an exceptional scalar factor, which qualifies the all-χ reading of Michel Hua's project's finding 84-chi-trivialised-extension-product.
- @1600, R05: Companion: Voight 2016, Construction 3.14 and Remark 3.17 give the quadratic-algebra product law b = b₁b₂, c = b₁²c₂ + b₂²c₁ − 4c₁c₂ of cote 84 (scan 192).

### MPL_90+91_002-018

- @1610, N91-10: Companion: the flattening criterion of 91/011-012 has the published counterpart identified in note N91-10.
- @1613, NCTX-01: Cote 90/016, assertion 4: "tt O_X-G-module … quotient d'un loc. libre de t.f." fails as literally stated (point test).

### MPL_91_099-143

- @1627, RN142-03: Cote 91/142: "det(b_ij) ≠ 0" in the G_n formula over Z fails the integral test; invertibility is needed.
- @1628, RN142-04: Cote 91/140, 142: a nilpotent translation T_f(x) + a conflicts with the written truncation k[t]/(t³).
- @1630, RN119-01: Edition: the exterior-algebra comparison runs 91/119 → 123 → 121 (printed pp. 90, 92, 93, n° 371).

### MPL_93_002-046

- @1637, E11: Cote 93/012, §4: differential rigidification fails in characteristic 2 (the involution of y² + xy = x³ + a₂x² + a₆); the general assertion needs a restriction.
- @1641, E17: Cote 93/018: the margin's "car 3", "car 2" divisibilities hold in equal characteristic only; over W(k) they fail (y² = x³ + x + 1 over Z₃).
- @1645, E26: Companion: "a₁ et ±b₂ sont les invariants de Hasse Witt" (93/023) compares with Katz's Cartier formula on the invariant differential.
- @1646, O01: Provenance: cote 93, scans 027-033 hold M. Wanderley's offprint "Théorie axiomatique de l'orientation des variétés topologiques à bord" with G.'s handwritten orientation axioms, a separate cluster in the cote.
- @1649, A01: Provenance lead: the operator-semigroup typescript of 93/032, 034 (pp. 5-6); unconfirmed.
- @1650, P01: Convention: G(z,f) = (−2f‴/f′ + 3(f″/f′)²) dz² on 93/036 is −2 times the Schwarzian derivative.
- @1655, P07: Companion: Katz 1972, Thm 3.2 (Gauss-Manin p-curvature against Kodaira-Spencer and Hasse-Witt) is the arithmetic bridge to test for 93/004, 018, 036, 044-046, with its extra hypotheses.
- @1657, P09: Edition: a comparison of 93/036 with cotes 159 and 64 must match the normalization of G and the meaning of c_f first.
- @1659, C07: Companion: Problem 1 on 93/039 (full faithfulness of the crystalline Dieudonné functor) must not be recorded as answered affirmatively in general; de Jong's theorems and general-base counterexamples qualify it.
- @1662, C19: Cote 93/043, "sous-cristaux en modules loc. libres": exactness alone does not give local direct summands (Z_p[x,y]/(xy − p)).


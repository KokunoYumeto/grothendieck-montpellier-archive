# The note entries both earlier passes missed: the third part of the follow-ups job (17 Nov 2026)

Written by the gap reader, Claude Opus 5.5 at effort max (the agent that wrote `FOLLOWUPS_FROM_NOTES_20261117.md` and `CLAIMS_FROM_NOTES_20261117.md`), on the brief of the main session (Claude Opus 5.5 at effort max), 17 Nov 2026: `field_experts/BRIEF_GAP_READER_20261117.md`. The notes read are those of our own transcription runs, GPT-6 Astra (ChatGPT Pro mode). Source: `field_experts/NOTES_GAP_ENTRIES_20261117.tsv` (built by `tools_20261113/notes_gap_entries.py`) and the notes files it names; working files in `field_experts/gap_work_20261117/`.

## Scope and method

- Selection: the 1772 entries of the gap list in 62 packages, g1-g1772: g1-g828 carry a kind (own idea, unpursued implication, unproved claim, conjecture) written in the title or in a bold line; g829-g1772 carry none, and for each the TSV says what it is.
- State of this file: 1772 of 1772 entries have a verdict (last g-number done: g1772). Rows not yet read are marked so in the TSV.
- Reading: g1-g840 were read in full, from a compressed copy that drops only search logs and file paths and cuts verbatim quotations to 160 characters. g841-g1772 were read as digests (title and the first 360 characters of the compressed text), with the full text read wherever the digest pointed to a possible research item; the reason is the compute bound (the untyped entries are 2.0M characters).
- Verdicts as in the two earlier passes: (a) research item (statement to prove or refute, cote and scans, G.'s words where they fix it, cluster, rank 1-3); (b) edition matter for the second pass; (c) nothing further (known result named from memory, settled in the notes, duplicate of @n, #n or another g-number, or too local). References for known results are from memory, not searched; check them before citing.
- Before an entry was called new, `notes_headlines/PROGRAMME_MAP.md` and `HEADLINE_RESULTS.md` were searched by grep (for cote 149, the subjects of FLAGGED_149 and ANABELIAN_149_PUSH). "@n" refers to `FOLLOWUPS_FROM_NOTES_20261117.md`, "#n" to `CLAIMS_FROM_NOTES_20261117.md`.
- Michel Hua's project (github.com/Commutator-IO/grothendieck-project) keeps the credit wherever a note uses one of its findings.
- Packages with no entry at all in either earlier pass (so wholly in this gap list): MPL_134-8_043-087 (132 entries); MPL_136_095-141 (9 entries); MPL_136_235-281 (75 entries); MPL_143+141 (50 entries); MPL_144_062-121 (10 entries); MPL_144_122-167 (27 entries); MPL_149_001-090 (214 entries); MPL_149_091-136 (141 entries); MPL_14_087-132 (83 entries); MPL_150_085-099+151_001-031 (57 entries); MPL_22+23_002-016 (56 entries); MPL_45_033-080 (55 entries); MPL_72_035-081 (100 entries); MPL_7_061-072+8_001-078 (80 entries). Their entries up to g840 were read in full; beyond g840 the full text was opened wherever the digests showed claims, conjectures or dates.

## Summary

| Verdict | Entries |
|---|---|
| research item | 6 |
| edition matter | 100 |
| nothing further | 1666 |
| not yet read | 0 |
| total | 1772 |

| Cluster | Research items | rank 1 | rank 2 | rank 3 |
|---|---|---|---|---|
| ANAB: points as sections (anabelian successor) | 1 | 0 | 0 | 1 |
| GT: the tower, structure at infinity | 0 | 0 | 0 | 0 |
| DER: Dérivateurs (localizers, excision, homotopy) | 1 | 0 | 1 | 0 |
| S6: S6 / companion dictionary | 0 | 0 | 0 | 0 |
| TAME: tame topology, stratified spaces, networks, pseudolines (Esquisse §5-6, §8) | 0 | 0 | 0 | 0 |
| CYCLES: cycles, motives, integral PD de Rham, analysers | 2 | 0 | 1 | 1 |
| GS: group schemes, representability and descent (new in the claims pass) | 0 | 0 | 0 | 0 |
| QUAD: quadratic algebras and covers over a general base (new in the claims pass) | 0 | 0 | 0 | 0 |
| POLY: regular polyhedra over rings (Esquisse §4; new in this pass) | 2 | 0 | 1 | 1 |

What the untyped entries (g829-g1772) are: summary 173; own idea 144; reading question 118; claim of his 101; source list 88; implication 73; source comparison 61; claim of his (withdrawn) 28; claim of his (self-flagged) 25; dating 11; claim of his (conjecture) 11; claim of the reused typescript 10; claim of his (question) 5; provenance 4; claim of his (doubt) 1; claims of his (sub-items N01-N69) 1; claims of the reused typescript (R01-R35) 1; own idea (O01-O12) 1; source comparison (L01-L15) 1; claims of his (N01-N13) 1; claims of his (N14-N28) 1; claims of his (N29-N33) 1; claims of his (N34-N44) 1; claims of his (N45-N55) 1; claims of his (self-flagged, U01-U08) 1; claims of his (U09-U16) 1; claims of his (C7.01-C7.02) 1; claims of his (C7.03-C7.04) 1; reading question (C7.06) 1; claim of his (C7.05) 1; claims of his (C7.07-C7.08) 1; implication (C7.09-C7.10) 1; implication (C7.11) 1; reading question (C7.12) 1; claim of his (C7.13-C7.14) 1; claim of his (conjecture, C7.15-C7.19) 1; claim of his (conjecture, C7.20, C7.24-C7.25) 1; own idea (C7.21-C7.23) 1; reading question (ER.01) 1; reading question (E.01-) 1; implication (ER.02-) 1; claim of his (conjecture, E.04-) 1; claim of his (conjecture, withdrawn, E.09-) 1; claim of his (E.10-) 1; reading question (ER.04-) 1; claim of his (E.12-) 1; own idea (E.14-) 1; own idea (ER.05-) 1; claim of his (E.18-) 1; claim of his (E.23-) 1; claim of his (ER.07-) 1; implication (E.28-) 1; reading question (ER.08-) 1; reading question (R.01-) 1; own idea (E.29-) 1; reading question (S.021.1-) 1; own idea (E.32-) 1; claim of the reused typescript (S.023.1-) 1; claim of his (conjecture, L.01-) 1; own idea (L.03-) 1; own idea (L.05-) 1; reading question (L.09-) 1; reading question (S.030.1-) 1; own idea (L.10-) 1; claim of the reused typescript (conjecture, R.02-) 1; own idea (L.12-) 1; implication (R.05-) 1; own idea (L.13-) 1; own idea (R.08-) 1; own idea (L.14-) 1; claim of the reused typescript (S.039.1-) 1; own idea (L.15-) 1; claim of the reused typescript (S.041.1-) 1; own idea (L.16-) 1; own idea (R.06-) 1; own idea (L.18-) 1; implication (L.21-) 1; claim of the reused typescript (S.047.1-) 1; implication (L.24-) 1; implication (R.09-) 1; claim of his (L.26-, conjecture S.050.2) 1; implication (L.28-) 1; claim of the reused typescript (S.053.1-) 1; own idea (L.30-) 1; claim of the reused typescript (S.055.1-) 1; own idea (L.33-) 1; reading question (S.057.1-) 1; reading question (L.38-) 1; reading question (S.059.1-) 1; claim of his (T.01-) 1; reading question (R.10-) 1; claim of his (T.07-) 1; implication (R.11-) 1; reading question (T.14-) 1; claim of the reused typescript (S.066.1-) 1; implication (T.16-) 1; claim of the reused typescript (R.13-) 1; own idea (T.21-) 1; reading question (S.070.1-) 1; own idea (T.20, T.22-) 1; own idea (R.15-) 1; claim of his (T.23-T.24) 1; claim of the reused typescript (S.074.1-) 1; claims of his (conjectures T.25-T.29, S.075.3-S.075.6) 1; own idea (R.14-) 1; claim of his (E.35-) 1.

Edition matters by package: MPL_106+107 2; MPL_133 8; MPL_134-8_043-087 6; MPL_136_047-094 1; MPL_136_095-141 2; MPL_136_235-281 4; MPL_142_094-122 2; MPL_143+141 2; MPL_144_001-061 1; MPL_144_062-121 5; MPL_144_122-167 4; MPL_144_168-184+148_001-028 1; MPL_146_100-134 4; MPL_147_138-190 1; MPL_149_001-090 14; MPL_149_091-136 4; MPL_14_087-132 9; MPL_150_085-099+151_001-031 2; MPL_15_087-138 4; MPL_2 5; MPL_22+23_002-016 5; MPL_45_033-080 4; MPL_60_002-035 3; MPL_72_035-081 4; MPL_7_061-072+8_001-078 2; MPL_84_146-193 1.

## Research items by cluster (strongest first)

### ANAB: points as sections (anabelian successor)

- **[rank 3] g1276, MPL_149_091-136, 120-CJ1.** G.'s converse for elementary U (cote 149, scan 120, ms. p. 60: "A t-on une réciproque ? regarder !", and the margin "Ça devrait être le cas pour U 'élémentaire'" with the underlined types (0,0) and (0,1), whose connecting words are uncertain). Let U be an elementary (anabelian) scheme over a field K of characteristic 0 with function field L, and V a valuation of L trivial on K. Prove or refute: if the inertia group I_V maps trivially into E_U^{L̄} (the arithmetic fundamental group, 149/117), then V has a centre on U. Known in the notes: the forward implication, and the failure for U = A¹ (type (0,1), g1277). The gap reader's check (unchecked): for curves, a valuation without centre on U is centred at a cusp, whose inertia is trivial in π_1 only for type (0,1), so the curve case holds for every other type; the content is in dimension ≥ 2 and for non-divisorial valuations (centres at normal-crossing boundary points: injectivity of the local Ẑ(1)^r into π_1(U), e.g. for M_{0,n}). G. recovers E_U from G_L by killing the inertia of the valuations centred on U (149/121, g1278); the item says that no other inertia dies. PROGRAMME_MAP lists only the counts of ANABELIAN_149_PUSH and FLAGGED_149, so check their rows for 149/120 before sending.

### DER: Dérivateurs (localizers, excision, homotopy)

- **[rank 2] g6, MPL_134-8_043-087, R008.** G.'s "Thm(?)" for linear coefficients (cote 134-8, scans 048-049, with the "Hypothèse-clef" of 048, the "Conditions équivalentes" of 053 and Lemmes 1-3 of 053-054): for a k-linear category 𝓜 with a k-bilinear tensor product, enough projectives and exact limits, and an interval α: 1_𝓜 → J that stays monic after tensoring with every x and has L_iφ(J ⊗ x) = 0 for all i ≥ 0 ("on le veut pour i=0 aussi"), prove or refute that the resolving functor Λ = λ_! and its adjoint λ^* induce quasi-inverse equivalences between the localization of 𝓜 and that of chain complexes (the counit tests of 053); this is the linear case of Pursuing Stacks VII §134's localization question and bears on the open rows GALOIS G.6 and RESIDUE I.7 of our runs.

### CYCLES: cycles, motives, integral PD de Rham, analysers

- **[rank 2] g1048, MPL_136_235-281, N39.** G.'s weight localization and its multiplication (cote 136, scans 244-281: "Généralités sur modules gradués sur certains anneaux gradués" (244), "n'est pas une catégorie à lim filtrantes exactes" (254), "bijectif?" (257), full faithfulness on D⁺(C) "pl. fid." and "compatible avec multiplication" (273), "Th. Le foncteur τ_N i_* est pl. fid." (279)). Setting: S = Γ_k(T) = k{T}, M_0 the nonnegative graded S-modules, i(M) = M ⊗_k S. Settled in our notes: finite-tail full faithfulness (g1031; Michel Hua's project's finding, credit to his project), an exact left adjoint L of i (g1041), the failure of G.'s literal negligible classes (g1034, g1035), and, in a repaired setting (the Gabriel quotient Q by the localizing Serre closure of the bounded-above modules), the derived reconstruction RR Q i(M) ≅ i(M) (g1080), which gives the linear "pl. fid." on D⁺. Open, and the item: "compatible avec multiplication" (273). Construct, naturally in the simplicial set X, a multiplicative structure on the weight-localized PD de Rham complex (at least a ring object in D(k)) that recovers the cup product, or prove that none exists. Starting facts: the naive product [p]_a ⊗ [q]_b ↦ [p ⊗ q]_{a+b} does not descend through L, since C(a+b+m, a+b) ≠ C(a+m, a), and along the cofinal weights a = b = ℓ^r − 1 the factor C(2ℓ^r − 2, ℓ^r − 1) has ℓ-adic valuation r (Kummer) (the gap reader's computation, unchecked); integer combinations of weighted products recover the cup product on cohomology (g1082: 6·C(4,2) − C(7,3) = 1; g1081 for the conditional route); no strict integral PD algebra can carry the cup product (g1019, CP²). Together with @305; bears on the open rows GALOIS E.11 and G.6 of our runs.
- **[rank 3] g1004, MPL_136_095-141, 5.1 Handwritten lecture material and the English donor.** G.'s uniqueness conjecture for admissible integral PD de Rham theories (cote 136, scans 111-121, the lecture material of 095-141): a generalized theory is a bigraded differential PD algebra functor with augmentation, admissible when the augmentation is a quasi-isomorphism after τ_∞ ("cohomologie de De Rham associée", 111-113; "l'augmentation est un quasi-iso", 117); "On aimerait prouver un th. d'unicité" (119), first step "on oublie d'abord la structure p.d." (119); on 121 every allowed morphism is already a τ_∞ quasi-isomorphism ("les hom. … sont déjà des quasi-iso"), and the localized groupoid of admissible theories should be "connexe et simplement connexe ?", through "Conj.? a)" (two admissible theories receive maps from a third) and an equalization condition ("qui égalise"), with "calcul de fractions à droite ???" in the margin. Prove or refute connectedness and simple connectedness, with and without the PD structure. The simple-connectedness half is to be compared with G.'s later classification of the endomorphisms and automorphisms of his PD de Rham functor (#243: a scalar part and a pro-unipotent kernel), and the two automorphism groups of 104-106 ("deux groupes, que nous nous proposons de déterminer") with the same classification. The other sub-items of 095-141 are local, withdrawn on the page, or part of @305 (the comparison: 113-119, "voudrait que ces deux flèches soient des isomorphismes", "On suspecte qu'il faut pouvoir prendre λ indépendant de n").

### POLY: regular polyhedra over rings (Esquisse §4; new in this pass)

- **[rank 2] g1557, MPL_72_035-081, The definition question.** G.'s pinned regular hyperpolyhedra over a base and the equivalence of scan 077 (cote 72, scans 038, 073-077: "hyperpolyèdre régulier … épinglé sur S", τ_i = id + a′_i ⊗ a_i; on 077 "d'une hyperquadrique Q_C de C" and the triple (C, Q_C, φ_G^C)). The object: a projective bundle over S with marked pseudo-reflections T_i(v) = v + φ_i(v)a_i (λ_i = 1 + μ_i units), an admissible pinned flag whose orbit gives the realization, a centre and a distinguished hyperplane; on the finite-centre chart (ρ invertible, 073-074) a rank-(n+1) module with φ_i(a_i) = λ_i − 1, predecessor pairings 1 and successor pairings β_i. Prove or refute G.'s categorical equivalence of 077 for n ≥ 2 over an arbitrary base, after repairing the two normalizations that fail as written ("L_i ⊂ H_{i+1}" against ⟨a_i, a′_{i+1}⟩ = 1 on 074, with "h_i ∉ H_{i+1}" on 076; the normalization of 075 fails on an explicit isotropic pinned line), with descent and the n ≥ 2 caveat (076-077); G.'s own doubts: "∃! … conique Q ⊂ X" with "Peut-être faux" (035), "Cette condition entraîne celles des autres ?" (075). Settled in our notes for the recorded frame: the group law t*s = t + s + ρts on U_ρ = Spec R[t, (1 + ρt)^{-1}] and the linear and projective centralizers (038-043), the invariant quadratic form of the reflection specialization (073), the classification of invariant subspaces with the bound 2(n+2) (080-081), and the split conic and even Clifford algebra for n = 2; Michel Hua's project has the findings 72-automorphisms-deform-gm-to-ga and 72-invariant-subspaces-string (credit to his project). New to our programme (no entry in PROGRAMME_MAP or HEADLINE_RESULTS; cote 72 was missed by both earlier passes); the theme is Esquisse §4 (regular polyhedra over arbitrary rings).
- **[rank 3] g1558, MPL_72_035-081, Bridge B5: what is proved, and the missing source marking.** G.'s regular polyhedron of level N (cote 72, Bridge B5, scans 073-077, and the cote 79 dossier on rank-two modules over Z/nZ and Z, not yet read): prove or refute that the level-N family, with its marked generators, is the principal-congruence Farey map on X(N) and determine its congruence kernel. Proved in our notes for the explicit family n = 2, β = (1, 4), ρ = −2 (trace-zero 2×2 matrices over Z[1/2], T_i = −Ad(R_i), q = −det): the Farey darts H_N∖PSL_2(Z) ≅ G_N = SL_2(Z/N)/⟨−I⟩ map to the adjoint marked flag action with kernel μ_2(Z/N)/⟨−1⟩ at odd levels (at N = 15: degree two through 4I, 1,440 darts to 720, 96 cusps to 48 nilpotent vertices, 24 conic points; edges and triangles to affine lines and planes with degrees 2 and 3). Open: the map from the intended level family's marked flag action and its kernel; first step, read cote 79 for G.'s definition of the level family.

## Edition matters for the second pass, by package

### MPL_106+107

- g854, RQ-01: Attribution: the ink on 106/002 reads "Brown" (categories of fibrant objects), while Michel Hua's project's register entry says "Baues"; the edition keeps "Brown" and the companion should note the discrepancy.
- g869, D.2 Dates on the reused stock: Dating: the reused computer stock under the notes of cotes 106-107 carries DOCUGRA2 output of 24-25 August 1982 and job material of 4 June 1982; a terminus post quem of August 1982 for the handwriting on those sheets.

### MPL_133

- g950, W06: Reading lead: "Laborde|Lazard dixit" on 133/007-008 is supported as "Laborde" by the presence of Olivier Laborde's printed notes in the same cote (133/011-017); the statement ((M, q) ⊕ (M, −q) hyperbolic over an affine scheme) is verified in the notes.
- g960, W16: Companion (context correction): Pursuing Stacks VI §122, p. 517, (18′) claims that 0 → V′ → Sym²(V′) → Λ²(V′) → 0 has no Aut(V)-equivariant splitting for dim V ≥ 2 over F_2; at dim V = 2 the form x² + xy + y² is GL_2(F_2)-invariant with the generator of Λ² as polarization, so the claim needs dim V ≥ 3; to be checked against the Pursuing Stacks edition.
- g961, P01: Provenance: 133/011-017 are two printed notes by Olivier Laborde (a graded Skolem-Noether note, 011-013; a note on quadratic forms, Clifford algebras and signatures, 014-017), not G.'s text.
- g967, F02: Error of the page (133/019): the boxed 2λ²(E) + E = E² cannot hold in the Burnside ring (the free C_2-set u has u² = 2u, which would force 2λ²(u) = u).
- g969, F04: Error of the page (133/021): the operation is "polynomiale … de degré n" but not homogeneous (for G = 1, n = 2 it is r ↦ (r choose 2)).
- g970, F05: Error of the page (133/024-025): the first definition of a special functor includes h_1 ⊔ h_1, which is not a direct summand of any single H_I (evaluation at a singleton).
- g976, F11: Error of the page (133/029): "lin. indép. … si k est un anneau local" fails for k = F_2 (ρ_1² = 2ρ_2 in the Grothendieck group of representations).
- g987, M01: Dating: reused thesis notices in cote 133 are dated "19 juin 1975" (Marie Marteau, animal biology) and "5 Juin 1975" (Marc Nanard, applied mathematics) (133/048, 050); a terminus post quem for leaves written on their reverse.

### MPL_134-8_043-087

- g24, R040: Provenance: the reused sheet 134-8/064 carries instructions for the xerography of "Modelizing Story", pages 259 to 381 (three copies, an extra copy of p. 275, "trois pages de table des matières"; pp. 274-275 typed recto-verso); an August return request without a year.
- g26, R047: Provenance: 134-8/067 is a reused corrections sheet "Problèmes ouverts en théorie des Intersections. A. Grothendieck. Exposé XIV" (SGA 6, XIV), "Corrections à faire après tirage", with five page/line instructions.
- g36, R067: Provenance: the reused production sheet 134-8/078 reads "SGA 7 Exposé VIII … p 95. Cette dernière page est très serrée. Voir pour tirage photo-offset"; a cancelled SGA 7 Exposé IX heading is on 076.
- g40, R075: Provenance: 134-8/080, 083, 087 (typed p. 3) and 082, 085 (typed p. 4) are reused pages of a typed text on Kimchi ("3. Le matériel nécessaire …", "4. La préparation et la conservation du Kimchi …").
- g51, PS05: Edition: the revisions on 134-8/046 (cancelled "On peut prendre J⁺_𝓜 = ℤ_𝓜" and "est projectif"), 048 ("projectif" changed to "plat") and the question on 050 ("sont-ils projectifs ?") record the projectivity obstruction to the tensor-resolution argument (compare Pursuing Stacks VII §139) and must stay as written.
- g992, Printer dates, numeric fields and repeated job headers: Dating: the reused printer stock in cote 134-8 carries job headers "3.04.01 PM 25 AUG 82, JOB 421" (scan 043 and others); a terminus post quem of August 1982 for the handwriting on those sheets, consistent with g869.

### MPL_136_047-094

- g998, Reused titles and pagination: Provenance: the reused sheets in 136/047-094 carry a typed English mathematical text (typed pp. 6, 5, 4 on 049, 051, 053, in reverse order, unattributed) and typed "Chapter IX" pages 130-155 (055-073; "11. C…" on 055), by their numbering the same Exposé IX typescript that the notes of 095-141 identify as SGA 7 I, Exposé IX (see g1003); the edition should name both donors.

### MPL_136_095-141

- g1003, 1.5 Abelian varieties, Chern classes, and Fourier transforms: Provenance: the abelian schemes, Jacobians, biextensions and polarizations of 136/103-124 are on the reused French typescript, identified in the notes with SGA 7 I, Exposé IX, Modèles de Néron et monodromie; its version differences from the printed text are to be collated (R35); the English minimal-model sheet 109 (headed N27) is a second, unattributed donor; no Chern-class or Fourier-transform example of the PD construction occurs.
- g1007, 5.4 Literature and later-context comparisons: Dating and attribution: Cartan (1976, §7, pp. 269-271) attributes his account of PD de Rham complexes to Grothendieck's IHÉS lecture of 12 December 1975; the edition of 136/095-141 should record this witness (page numbers from the note, to be checked). The other comparisons (L02-L15) are context.

### MPL_136_235-281

- g1010, N01: Dating: the reused documents under 136/245, 255, 258 are dated 20 May, 16 June and 24 June 1975, and a thesis notice announces a defence on 10 July 1975: a terminus post quem of late June 1975 for the handwriting on those sheets, not a date of the argument (compare the lecture date of g1063).
- g1025, N16: Provenance: the reused typed sheets in 136/236-280 (Néron models, Raynaud extensions, semistable reduction; internal pp. 76-185, §§6-13.5) are pages of the same Exposé IX typescript as g1003 (SGA 7 I, Exposé IX), not lecture examples; the edition should name the donor and collate it.
- g1029, N20: Reading (136/279): the page defines the cotruncation σ_N(P) = P/τ_{N+1}P ("cotronqué", "tronqué à gauche") and the theorem line is transcribed "Le foncteur τ_N i_* est pl. fid."; check on the scan whether τ_N or σ_N is written before the positive-tail theorem is carried over to this negative-degree model.
- g1063, N54: Dating: Cartan (1976, §7, pp. 269-271) dates G.'s IHÉS lecture to 12 December 1975, which differs from the catalogue's dating of these leaves; the edition of 235-281 should give both (see g1007, g1010).

### MPL_142_094-122

- g1102, A16: Codicology and dating: the heading "Groupoïde fondamental d'une carte trouée" with "(14 pages)" (142/105) and the printed seminar notice dated "24.03.80" (107): establish the sheet pairing, orientation and the numbering restart at scan 114 before the notice is used to date the argument.
- g1103, A17: Reading (142/101): "sous l'action de π|Γ", first reading π; the context favours the listed alternative Γ; check the glyph on the scan.

### MPL_143+141

- g132, N06: Edition: the cancelled "il faut supposer χ = 1" (143/006) is not a standing assumption; the live text keeps the cyclotomic action on the Tate source and the permutation of boundary components.
- g1113, Printed thesis notices and their six calendar dates: Dating: the reused thesis notices in cote 141 are dated 7 and 12 November 1980, for defences on 17 and 18 November 1980 (141/003, 005, 007: Maubert, Michelland, Comte); a terminus post quem of November 1980 for the handwriting on those sheets.

### MPL_144_001-061

- g1129, 8.1. Visible title or boundary sheets: Dating of 144/001-061: "Conversations avec Deligne du 30.5 et 5.6." (003, no year); formulary dated 1981 (034) and 1982 (013, 030, 032); "Juin 1983" (036, month uncertain) and "1983" (040); the reused ministry circular of 15-23 February 1982 (044, 046) is a terminus post quem for the period calculation on 042-047; Barry Mazur's letter "Dear Shurik" (010-011) is undated.

### MPL_144_062-121

- g1138, Cartography, real descent and signatures: scans 062–077: Edition (144/065): the first denominator of the chain before (23) is transcribed with "+1" while the next is (z − 1)² − (z + 1)²; at z = 2 they give 1/10 and −1/8, and the substitution φ(w) = w/(w − 1) supports the second; check the scan (slip of the page or of the reading). The claims of 062-077 (the fully faithful functor from weighted maps to real covers with X′(R) = ∅, 067-068; the criterion cl(X) ∈ H¹(X, Z/3Z) "néc. et suffisante", 076-077; "sauf erreur", 076) parallel LM2/507-508 and LM3/009-010 and are local here.
- g1139, Polygonal mixed groups and the explicit quotient: scans 078–095: Edition (144/086, (89)): the value ρ ↦ ρ_∞ is revised to ρ ↦ ρ_∞^{-1} by the path calculation on 090-091 (as on 073); keep both and mark the revision; the renaming τ_0 → τ_∞ → τ_{a_0} (082, 084) is G.'s own. The polygonal mixed groups (Z/nZ * Z/2Z, 082-084; the faces functor, 092-094; "Sûrement on doit pouvoir généraliser", 095) are local, parallel to LM3/086-090.
- g1140, Doubled polygons and linear lifts: scans 096–101: Reading (144/097): "pour n=6" beside a hexagon with two triangles, where the doubling notation gives n = 3; check the scan. "naturellement" deleted from the splitting statement (097); the odd/even lifting argument (098-099) and the unfinished C*-bundle question (100-101) are local.
- g1141, Loose calculations, reused sheets and Cornu leaves: scans 103–116: Edition: on 144/105 the line 4j̄² + 1 − 4j̄ = 4(j̄² − j̄) loses the constant 1 (error of the page); the leaves 104, 114, 116 are by Cornu (icosahedral construction), not G.; the reused administrative faces 106-112 are dated September-October 1978. The calculations of 103-115 are local.
- g1142, Cover and letters: scans 117–121: Provenance: the cover 144/117 reads "Calculs divers sur Teichmüller" and "Lettre Deligne sur groupes profinis"; the letter on 118-119 is dated "27/3/81" and signed "Pierre", with a Russian paragraph whose doubtful words stay marked; the letter on 120-121 cites Tate's "Number theoretic background", §1. Its mathematics is known (from memory): free profinite groups of rank ≥ 2 and open subgroups of G_Q have trivial centre; finite subgroups of the mapping class group are realized (Kerckhoff 1983); Chevalley's congruence theorem for S-units (1951); Shimura-Taniyama CM theory.

### MPL_144_122-167

- g181, N25: Edition: "formé justement par les opérations … qui sur ∂X sont d'ordre fini" (144/147) is not an exhaustive characterization if it quantifies over the whole group (h_a = σg_{a,1} with a irrational has h_a² = 1); the doubtful insertion "dudit gr|du total gr" decides the scope.
- g186, N35: Edition: the amalgam ⟨τ″, ε_0, ε_1⟩ *_{⟨τ″, ε_1⟩} ⟨τ″, ε_2, ε_1^{-1}⟩ of 144/154 and "[ε_0, ε_2] = 1" on 156 are incompatible if the symbols map as named (normal form in amalgams, Serre, Arbres I §1.2); the ε/ξ readings on 154 must be fixed before either is used.
- g190, N43: Edition: the triangle ω(X′), ω(X″), ω(X′ ∧ X″) on 144/162 is labelled "anticommutatif" with a circled minus sign; the sign is part of the gluing convention and must be kept.
- g1144, Dates on the printed or reused matter: Dating of 144/122-167: the reused printed notices run from 4-5 July 1979 (135-139) to "22.10.80" and 30 October 1980 (167), with "30.10.80" (130) and "Vendredi 31 Octobre" (132; 31 October 1980 was a Friday, the gap reader's check); the computer footer "11.42.58 AM 06 NOV 82" (153) gives a terminus post quem of November 1982 for the handwriting on that sheet; no autograph date.

### MPL_144_168-184+148_001-028

- g1149, T04: Dating: the reused notices of 144/169-184 are dated 14-30 October 1980 and June 1981, those of 148/006-016 14-20 October 1983 (defences 27 October-2 November 1983); the computer output on 148/020-022 carries "09 JUN 82": termini post quem for the handwriting on those sheets (October 1980 to June 1981 for 144/169-184; October 1983 for 148/006-016).

### MPL_146_100-134

- g227, B16: Edition: the cancelled "associé can. … avec ω_J" (146/122) would fail equivariantly (the quarter-turn is an odd permutation), so the cancellation is mathematically meaningful and must stay visible.
- g235, B25: Edition: scan 146/125 ends on an isolated "On" and 126 starts "Graphes MD"; with "j'y reviendrai" (124), the promised square-fibre presentation and the paths between exceptional fibres are not in the surviving pages.
- g252, C20: Convention: "morphisme fini net" (146/133) uses net = unramified (EGA IV 17.1.1); it must not be modernized to finite étale.
- g255, C25: Dating: the printed notices on 146/132 and 134 are dated "Montpellier, le 25 Novembre 1981" (Lorente and Ros thesis defences); a terminus post quem for the mathematics only if it is written on their reverse after printing.

### MPL_147_138-190

- g1172, 164-07: Edition (147/167-174), notation conflicts to check on the scans: A = D*_{I∖I′_1} "plongé dans" the starred R = D*_{I′_0} although (269) makes the I″ coordinates zero on A and nonzero on R (167); (277) gives D × D* the Δ_1-superscript and (281) the Δ_2-superscript (169, 171); "fibré conormal" with an exact sequence in the normal-bundle direction (173); the filtration labels Ň_{d_*,d_i} with rank d_i against the immersion D_{d_*} → D_{d_i} of codimension d_0 − d_i (173); the "quotient canonique" of (286) ordered opposite to (282) (174).

### MPL_149_001-090

- g336, A013.2: Edition: on 149/013 the deduction of "dim coh … égale à n" from elementary fibrations needs hyperbolic fibres (A^n has trivial geometric fundamental group); a hypothesis mismatch, not a refutation of (14).
- g342, A015.1: Edition: the Corollaire on 149/015 ("extension successive de groupes profinis libres") needs free factors of rank ≥ 2 (Ẑ is central); the context (scan 496) supplies the condition.
- g369, B025.3: Error of the page (149/025, item 3°): H_1(X, Z_ℓ) ≅ H_1(J, Z_ℓ) fails for reduced connected X without normality (a one-nodal rational curve has H_1 = Z_ℓ and only constant maps to semiabelian varieties); Corollary 1(a) needs only a surjection onto the universal realization.
- g374, B027.2: Error of the page (149/027): "tjrs vrai pour un morphisme dominant!" fails for the normalization P¹ → C of a one-nodal rational curve (image 1 in Ẑ); the intended normal-target case holds.
- g387, B034.1: Error of the page (149/034): G(K) is not a finitely generated Z-module in general (G_m(Q) = Q^× is not); the valid input is the absence of nonzero infinitely divisible points (Ozeki 2025, Prop. 2.3); the same error is in the context scan 064, and the notes give the repair (g388).
- g392, B035.3: Error of the page (149/035, (**)): prime-to-p injectivity fails on a hyperbolic curve: E/F_5: y² = x³ + 3x + 2, Y = E ∖ {O}, the points (1, 1) and (2, 1) have the same prime-to-5 Kummer class (E(F_5) has order 5).
- g398, B037.3: Error of the page (149/037, lemma): "U + u ⊂ Y" does not force u = 0: Y = E ∖ {O}, U = E ∖ {O, −u} with u ≠ O; the lemma alone is refuted, not 149/024(b).
- g401, B038.3: Error of the page (149/038): the bracketed "(Y + u) ∩ Y = ∅" fails (Y = P¹ ∖ {0, 1, ∞} in G_m² by x ↦ (x, 1 − x), u = (2, 3)); 149/024(b) is not refuted.
- g403, B039.3: Error of the page (149/039-040): the added inequality |I| < |J| − 1 does not remove the exception "de cardinal μ − 1", which concerns the spanning sets J ∖ I and occurs exactly when |I| = 1, however far U is shrunk.
- g413, B044.3: Error of the page (149/044): "π_K^{Γ′} ≠ (1)" is stronger than the negation of the definition on 043, which gives a nontrivial centralizer only for some smaller open Γ″ ⊆ Γ′.
- g422, C047.2: Error of the page (149/047): read as determination by the linear map on geometric H_1 alone, "connu" fails (distinct constant maps to a hyperbolic curve give the same zero map); the splitting class of the abelianized extension is the right datum (context scans 063-064).
- g439, C054.4: Error of the page (149/054-055): the proposition's first clause allows type (0, 2); for U = G_m the cusp packet at 0 contains the point sections, so "distinctes" fails (Stix 2012, Rem. 18(3)); a hyperbolicity hypothesis is needed.
- g484, D12: Edition: the "carré cartésien de groupes profinis" on 149/074 is stated for an arbitrary trait; outside characteristic 0 it needs the prime-to-residue-characteristic (tame) quotient and a good compactification (SGA 1, XIII 2.9-2.10), as 149/079-080 later does.
- g492, D20: Provenance lead: "Je présume … demande à Carlos de me le confirmer" (149/078): "Carlos" is plausibly Carlos Contou-Carrère, G.'s student at Montpellier; to be checked. The formula itself is the local root calculation (Cadman 2007, Prop. 3.3.3).

### MPL_149_091-136

- g526, 123-C3: Error of the page (149/123, NB): "(pas stables par réunions finies)" fails for the opens represented on arbitrary normal proper models (a common refinement represents the union; Temkin 2011, Lemma 3.4.6, Thm. 3.5.1(i)); a narrower class of models would have to be stated.
- g529, 124-CJ1: Edition: the inertia "des T_∞^α essentiellement" indexed by codimension (149/124, "pas néc. une jauge") needs qualification: the formal-curve valuation of the notes (130-O1) has codimension 2 and a single procyclic inertia factor; the T_∞ convention must be fixed.
- g554, 130-CJ2: Error of the page (149/130, item 2°): the inserted "a une image ouverte" fails for an arbitrary valuation: the DVR of the notes (x = t, y = t² + t³h(t), h transcendental) has inertia weights (1, 2), an image of infinite index in Ẑ(1)²; finiteness of the residue field does not repair it.
- g556, 130-O2: Error of the page (149/122, rows 3-6): the tentative assertion that only points of codimension 0 and 1 have noetherian stalks fails for all valuations (the nondivisorial DVR of the notes has codimension 2); it holds for essentially finite-type valuations.

### MPL_14_087-132

- g589, F12: Provenance: cote 14, scans 129 and 127 (typed pp. 24 bis and 25) are a draft of SGA 3, XIII §3 (Thm. 3.1, Cor. 3.2-3.3, Lemma 3.4: regular elements and the generic Cartan subgroup); the typed pages 2-3 on 124, 122 belong to the same S.G.A.D. layer.
- g592, P02: Error of the page (14/094, b″, c″): the threshold "≥ 2" needs a convention on the field of constants: X = P¹_C as an R-scheme with L = O_X has χ and h⁰ equal to 2 for all n though L is not ample.
- g595, P05: Error of the page (14/094, marginal "Critère numérique"): the curve-and-top test is not sufficient in dimension 3 (a Ramanujam-type example on a projective bundle over Mumford's ruled surface; Hartshorne, Ample subvarieties, I.10.8).
- g596, P06: Companion: the "Question" and product formulas of 14/096-100 parallel G.'s letter to Mumford of 31 August 1964, §5, with Mumford's marginal "NO"; a historical comparison, not a date for the sheets.
- g610, L12: Error of the page (14/113): the localization sequence for U = X − Y needs CH^{i−1}(Y) → CH^i(X), not A_r^i(Y), and the punctured affine cone over an n-dimensional variety has dimension n + 1, not 2n + 1.
- g611, L13: Edition: M_a^i = Ker(L^{n−2i}) on 14/113 conflicts with the conjectural isomorphism of 14/112 (it would be finite); the primitive kernel uses L^{n−2i+1}; the exponent is a reading or draft question.
- g615, Z03: Companion: G.'s letter of 20 November 1968 recognizes that the rectangle-product assertion fails modulo rational equivalence already on a product of two elliptic curves; a later contrary witness to 14/118, 126.
- g630, M07: Companion: the standard-conjecture letters of the drafts (14/111-117; C 16/044-049) against the printed ones (Kleiman 1968; Grothendieck 1969): draft C = printed B (inverse Lefschetz), draft D = printed C (Künneth) secure; draft A = printed A, draft B = printed D (homological = numerical) plausible.
- g1291, Z01: Companion (14/118, item 1): the premise that numerically trivial cycles modulo rational equivalence are described by finitely many algebraic families of finite type is false in general (known: Mumford 1969, surfaces with a nonzero holomorphic 2-form); the edition and companion should not present it as a standing fact.

### MPL_150_085-099+151_001-031

- g656, A10: Reading question (150/092): "X_j non dense dans X_i" read as "closure different from X_i" fails the density equality (a three-point discrete example in the notes); the historical sense (empty interior) must be checked before the axiom is used.
- g673, C06: Error of the page (151/015, "et de là, plus généralement"): the epimorphism tests for the terminal object, binary products and pullbacks do not give the condition for all finite diagrams (the orbit functor of BC_2: the equalizer comparison is ∅ → *).

### MPL_15_087-138

- g708, R03: Provenance: the reused sheet 15/089 ("famille conservative", Remark 3.13) is a page of SGA 4, VIII.
- g1342, FR07: Reading (15/100, line 33): "le poids i … est égal à mi′" omits a denominator in its present reading (the note's calculation with q = p^n); check the scan before the base-change weight statement is edited.
- g1349, FR13: Error of the page (15/108): with x² + ax + b = 0 the marginal trace "a = x + σx" has the wrong sign (the trace is −a).
- g1357, FR20: Error of the page (15/094, margin, "real, trivial case"): λ = (q^{1/2})^i misses the sign; λ = −2, q = 4, i = 1 is real; read λ = ±(q^{1/2})^i.

### MPL_2

- g747, A21: Convention (2/003): the product must be the derived (Tor) product: with the ordinary tensor product, O_p ⊗ O_p = O_p on P¹ contradicts "C'est l'annulateur de E_0".
- g752, CC07: Error of the page (2/014, N.B.): annihilation of all C^i(x) implies vanishing after pushforward only for rank zero: x = [O_X] has trivial positive Chern classes but c_r(i_! x) = (−1)^{r−1}(r − 1)! h^r ≠ 0.
- g754, A08: Error of the page (2/016): u^* u_*(F) ≅ F^(G′/G) "fonctoriel non canonique" holds only for underlying modules: for C_3 ⊂ S_3 and a nontrivial character χ, the restriction of the induced module is χ ⊕ χ^{-1}.
- g768, CC18: Error of the page (2/045): the calculation of 044 applies to ν_*O_C̃ for the normalization, not to O_C; c_2(O_C) = c_2(ν_*O_C̃) + [Q] with Q the normalization defect (a nodal plane cubic gives 9 against 8, g769).
- g773, A19: Edition: cote 2 consists of several separate units ("Contre-exemples", "Filtration des λ-anneaux … classes de Chern universelles", "Caractères de Chern covariants … à supports", "R.R. des surfaces"; title scans 002, 009, 020, 032, 040), not one paginated treatise.

### MPL_22+23_002-016

- g729, E08. A direct test of the written logarithm product: Error of the page (23/009): "log gg′ = log g log g′" for commuting group-like elements must read log gg′ = log g + log g′ (in Q[ε]/(ε²) with g = g′ = 1 + ε the written product gives 0 ≠ 2ε).
- g734, E14. Scope of the marginal Cartier checklist: Edition: the marginal "i.e." checklist for a Cartier hyperalgebra on 23/013 omits the filtration axiom of Cartier's definition (Séminaire Cartier, Exposé 2, §1, Def. 1): U = R^{C_3} satisfies the checklist, with no primitives, while dim U = 3.
- g1395, A05: Edition (22/012, Theorem 4.6(ii)): conditions 1-3 read "B est formellement simple", "B satisfait la condition P", "Les B_i sont plats" although B is already assumed and condition 4 concerns u: B → C; the literal list fails (A = Q[ε]/(ε²), B = A, C = Q); check whether C is meant.
- g1413, A27: EGA edition (EGA 0_IV 22.5.10(i), EGA IV-1 printed p. 204, and our transcription, which follows the print): with k = k_0(X, Y) and K = k(X^{1/p} + ZY^{1/p}), the element w = X^{1/p} + ZY^{1/p} is transcendental over k(X^{1/p}, Y^{1/p}), so K ≅ k(T) is separable over k and the printed assertion Υ_{K/k} ≠ 0 fails for the displayed fields (the note: high confidence; no erratum located). The intended example is presumably Mac Lane's K = k(Z, X^{1/p} + ZY^{1/p}) (the gap reader's suggestion, to be checked). The manuscript's own examples (22/027-029; g1411, g1414) are correct. Record in the companion of every EGA IV edition, with the fix or a note.
- g1415, A29: EGA edition, our transcription (the package's context file of EGA 0_IV) against the print (EGA IV-1): in 20.5.7.1 (printed p. 131) our text swaps the labels u_{C/B/A} and v_{C/B/A} (the print: v is Ω_{B/A} ⊗_B C → Ω_{C/A}, u the quotient map); in 20.7.2 (pp. 147-148) it reverses the direction of Hom_C(Ω_{C/A}, L) → Hom_C(Ω_{B/A} ⊗_B C, L); and its proof of 20.7.3 differs from the printed one. Check and correct these places in every language edition of EGA IV.

### MPL_45_033-080

- g789, A10: Reading lead (45/038, margin): "Utilisant" a doubtful "Tôhoku" to construct the "Tchevalley" groups over Z points to Chevalley, Sur certains groupes simples (Tôhoku Math. J., 1955); the ink stays uncertain.
- g817, Q18: Edition: the deletion of "discrètement" in case (e) on 45/078 is mathematically consequential: for a henselian valued field with algebraically closed residue field of characteristic ≠ 2, K*/K*² ≅ Γ/2Γ, so the displayed Z/2Z needs a discrete rank-one valuation.
- g825, R05: Error of the reused typescript (45/058, 060): formula (12) with "+" contradicts formula (8) with "−" (A = C over R, Φ(x, x′) = x x̄′: (12) gives −1, Φ(1, 1) = 1).
- g828, T02: Provenance: the reused typescripts of cote 45 carry printed page numbers and document numbers 246 (scan 033), 239 (046, 048), 269 (050-060) and 371 (067-071), with separate pencil numerals; the document numbers look like Bourbaki rédaction numbers (to be checked); they do not give the length of a handwritten unit.

### MPL_60_002-035

- g1490, F07: Companion (cote 60/002-035): ε changes meaning within the packet: the virtual rank ε(Rf_!(E)) (007, 021, 027) and two normalized determinants, ε(E) = ∏ε_i(E) (023) and ε(E) = δ(E)q^{−χ(E)/2} (027); the edition and companion must keep the three apart (the affine line distinguishes the determinant definitions).
- g1502, F19: Error of convention (60/015): "duaux à valeurs dans Q_ℓ(n)"; with geometric Frobenius acting on Q_ℓ(1) as p^{−1}, the Poincaré target is Q_ℓ(−n) (Deligne 1974, §2.3, from the note); the positive twist also conflicts with the packet's own variable change.
- g1516, F33: Error of the page (60/027): the first box gives δ(Rf_*E)q^{−χ/2} = (δ(Rf_!E)q^{−χ/2})^{−1}, so the next box's equality of both normalized determinants with ε fails in general; it holds when ε² = 1, in particular in the proper case (affine-line test, g1517).

### MPL_72_035-081

- g1573, Reused typed sheets: Dating: the reused thesis notices in cote 72 are dated 26 June to 3 July 1978 (notices 4001, 4060, 4151, 4172, for defences of 29 June to 12 July 1978; 72/060-068), with seminar sessions of May 1978: a terminus post quem of July 1978 for the handwriting on those sheets.
- g1577, A. Short research items: Edition (cote 72): the frozen internal incompatibility on 074 ("L_i ⊂ H_{i+1}" makes ⟨a_i, a′_{i+1}⟩ zero although it is normalized to 1; 076 writes "h_i ∉ H_{i+1}"); the labels change within 080 (Z_n, Z′_n and Z_n^♯ trade places between the preliminary text and the diagram); the vertical containments of the 080 diagram hold only when β_i = 0 (the nearby "NB"; refuted literally over F_3 with n = 1, μ = (1, 1), β = (2)). Keep the text as written and annotate.
- g1591, E-Q045-margin-a1: Edition (cote 72/045-078): the computational checks give exact residuals for about thirty formula and index readings (E-Q045 to E-Q078: summation bounds on 047, recurrence subscripts and arities on 049-053, the product on 050, determinant signs on 053 and 057, coefficients on 069, signs on 071 and 078); check each against the scan, as listed in the package's enumeration_reading_questions.csv, without silently repairing the text.
- g1641, A15. The trigonometric line has a concrete numerical discrepancy: Error of the page or of the reading (72/036): "β_i = α_i + 2" with "4 cos 2θ_i": at θ_i = π/3, α_i = 4cos²θ_i = 1 gives β_i = 3, while 4 cos 2θ_i = −2 (and 4cos²θ + 2 = 4 + 2cos 2θ); check the scan.

### MPL_7_061-072+8_001-078

- g1684, Scan 019: Provenance (cote 8): the reused typed sheets are several separate texts, with the typed heading "Tribu n° 66" and repeated document numbers (8/019, 035-057, 062-076) ("La Tribu" is the name of Bourbaki's internal bulletin: the gap reader's identification from memory, to be checked); published parallels identified in the notes: Lipman 1969, §24 (8/003, typed p. 132), SGA 7 I, IX, Remark 5.13.1 (8/032), SGA 4 XVI §3 and XIX 3.4 (8/062-074, purity); a jet and differentiable-manifold chapter in reverse typed order (8/035-057, pp. 77-84) and a convolution text (8/072, 076). The edition should name each stream and keep it apart from G.'s crystalline handwriting.
- g1694, Scan 031: Edition (cote 8), slips of the page to annotate, not to repair: on 031 the boxed "ω′ − ω = −du/u" has the opposite sign to the first component du/u of the next diagram, whose target is listed as (one-form, function) but whose element is written (φ, ω); on 036 "la somme des rangs des M_ν est h" mixes A-ranks and W-ranks (rank_W M = e Σ s_ν = h = ef); on 044 "ω_{G_0} ≃ Ω/pΩ" has k-dimension e and is not killed by π when e > 1 (p versus π, also in the insertion M ⊗_W k = Σ M_ν ⊗_A k). Conventions to state: ρ_σ(g)x = σ(χ_π(g))x is only the scalar part of the semilinear action (054); the torsor factor in "ũρ = i_1(u^{-1})" (065).

### MPL_84_146-193

- g1757, 8.4. Chronology and the limits of dating reused sheets: Provenance and dating: the reused typed leaves of cote 84 (odd scans 147-193, typed pp. 475-500 with 475 bis) are a draft of Récoltes et Semailles (notes 108-112, dated 6 October to 6 November, with footnotes of 6 and 16 October and 6 November); the year is about 1984 by internal inference (the 9 October recollection of 17 October 1976 as nearly eight years earlier, scan 151). This gives a terminus post quem of autumn 1984 for the handwriting on those sheets; the printed-page order of the leaves is 147, 149, 153, 165, 151, 155, 167, 169, 171, 157, 159, 163, 161, 175, 173, 177, 179, 181, 183, 185, 189, 191, 193, 187.

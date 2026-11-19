# Grothendieck's unproved claims in the research notes: the second half of the follow-ups pass (17 Nov 2026)

Written by the claims reader, Claude Opus 5.5 at effort max (the agent that wrote `FOLLOWUPS_FROM_NOTES_20261117.md`), on the brief of the main session (Claude Opus 5.5 at effort max), 17 Nov 2026 03:35 UTC: `field_experts/BRIEF_CLAIMS_READER_20261117.md`. The notes read are those of our own transcription runs, GPT-6 Astra (ChatGPT Pro mode). Source: `field_experts/GROTHENDIECK_CLAIMS_MAP_20261117.tsv` (built by `grothendieck_archive_transcription_20261110/tools_20261113/claims_map.py`) and the `<package>_notes.md` files of the returns; working files, verdict files and scripts in `field_experts/claims_work_20261117/` (`STATE.md`, `extract_claims.py`, `verdicts/v_k01..v_k31.txt`, `assemble_claims.py`).

## Scope and method

- Selection: the claims map lists 1387 entries of kind "unproved claim" or "conjecture", numbered #1 to #1387 in table order. The scope is the **1137 entries whose `runs` cell is empty, in 50 packages**; the other 250 are tied by their notes to one of our runs.
- Reading: every entry of the scope was read in full in its notes file, from a compressed copy that drops only search logs and file paths and cuts verbatim quotations to 160 characters. There was no switch to digests.
- Verdicts: (a) research item, a statement to prove or refute with cote and scans and G.'s words where they fix it, a cluster and a rank (1 decides a question he marks as central, or a block of a companion; 3 is the weakest); (b) edition matter for the second pass (a reading, a convention, an error of the page, a dating or provenance fact, an audit of a summary, or a cross-reference the companion should carry); (c) nothing further: a standard or known result (named, with a reference), a claim the same notes or the next pages settle, a duplicate of a follow-ups item (@n) or of another entry here (#n), or a step too local to matter.
- References for known results were given from memory, without searching, as the brief asked; they are pointers to check before any of them is cited in a publication.
- Before an entry was called new, `notes_headlines/PROGRAMME_MAP.md` and `notes_headlines/HEADLINE_RESULTS.md` were searched by grep for its subject (mobility, dévissable, stratification, representability, envelope, automorphism, faithfulness, field of moduli, orthogonality, Picard, Hausdorff, Pfaff, preparation, component groups, duality, quadratic algebras, cotes 121, 131, 142); none of the nine research items below is among a run's main results or open rows. Many claims are already items of the follow-ups pass and are marked "part of @n" or "duplicate of @n" there.
- Most of the scope is G.'s drafts of SGA 1-7, EGA, FGA and of his duality, Picard and crystalline work, where the claim on the page is now a theorem in print, and reused typescripts of other authors (Bourbaki drafts and "Tribu" sheets, analysis and topology typescripts, an offprint of M. Wanderley); their provenance leads are edition matters. The autobiographical leaves of cote 84 are marked nothing further without restating them.
- "#n" is the entry's number in the claims map; "@n" is an entry of `FOLLOWUPS_FROM_NOTES_20261117.md`. The TSV gives package, entry and verdict for every number of the scope.
- Michel Hua's project (github.com/Commutator-IO/grothendieck-project) is credited wherever a note uses one of its findings; the credit stays with his project.

## Summary

| Verdict | Entries |
|---|---|
| research item | 9 |
| edition matter | 115 |
| nothing further | 1013 |
| total | 1137 |

| Cluster | Research items | rank 1 | rank 2 | rank 3 |
|---|---|---|---|---|
| ANAB: points as sections (anabelian successor) | 1 | 0 | 0 | 1 |
| GT: the tower, structure at infinity | 2 | 0 | 2 | 0 |
| DER: Dérivateurs (localizers, excision, homotopy) | 0 | 0 | 0 | 0 |
| S6: S6 / companion dictionary | 0 | 0 | 0 | 0 |
| TAME: tame topology, stratified spaces, networks, pseudolines (Esquisse §5-6, §8) | 1 | 1 | 0 | 0 |
| CYCLES: cycles, motives, integral PD de Rham, analysers | 2 | 0 | 1 | 1 |
| GS (new): group schemes, representability and descent (cotes 31, 56, 90, 91, 131; LM1 line) | 2 | 0 | 0 | 2 |
| QUAD (new): quadratic algebras and covers over a general base (cote 84) | 1 | 0 | 0 | 1 |

Edition matters by package: MPL_105 1; MPL_11_002-042 3; MPL_11_043-058+56 7; MPL_121_001-048 2; MPL_121_049-073+153+155 1; MPL_12_150-168+15_002-033 1; MPL_131 8; MPL_133 1; MPL_136_047-094 2; MPL_136_142-188 8; MPL_136_189-234 3; MPL_142_001-093 15; MPL_142_094-122 1; MPL_144_001-061 2; MPL_146_001-099 1; MPL_147_048-137 6; MPL_148_029-072 1; MPL_14_002-044 3; MPL_150_044-084 1; MPL_154_127-176 2; MPL_156-1+156-2 4; MPL_15_087-138 2; MPL_15_195-228+18_002-017 7; MPL_16+47+54+44 1; MPL_2 2; MPL_31_002-051 3; MPL_33_002-049 2; MPL_33_050-097 1; MPL_33_147-181+34_002-017 1; MPL_36_002-052 5; MPL_36_053-085+39 7; MPL_43_094-142 1; MPL_57_271-315 1; MPL_60_002-035 3; MPL_62_002-050 1; MPL_84_097-145 1; MPL_90+91_002-018 1; MPL_91_099-143 2; MPL_93_002-046 1.

## Research items by cluster (strongest first)

No entry of the scope gave a research item in DER or S6.

### ANAB: points as sections (anabelian successor)

- **[rank 3] #468, MPL_142_094-122, R14.** G.'s expectation "Je ne serais pas étonné qu'on ait unicité dans ce cas" (cote 142, scan 096): for a hyperbolic curve X over a field K finitely generated over Q and finite over the field of moduli ("corps modulaire") of X, prove that the outer Galois representation G_K → Out(π̂₁(X_K̄)) is injective (uniqueness of u), with the convention on markings and automorphisms fixed; isotrivial examples show the moduli condition is needed. Check first whether Hoshi-Mochizuki 2011 already covers fields of positive transcendence degree.

### GT: the tower, structure at infinity

- **[rank 2] #309, MPL_142_001-093, N012.3.** G.'s "enveloppe profinie" of the category of hyperbolic surfaces with finite covering maps as arrows (cote 142, scans 009-016): construct the completed category with Hom sets the balanced products (17) and prove that composition by the recipe (20)-(22) is well defined, continuous and associative under the finite-index stabilizer axiom (16), that the completed arrow stabilizer equals the closure of G_u (014 NB, "Il faut savoir interpréter … (ψ̂, φ̂) ∈ Ĝ_u"), that the functor from the discrete category is conservative with dense isomorphisms (014), that completed factorizations are unique given injectivity of the deck group into the completed mapping class group (014, (18)-(19)), and that the result has the algebraic description by finite étale covers and étale path classes in the modular stacks (015, "une 'classe de chemins' … d'une multiplicité modulaire"), with the Aut k action of the programme on 017; the ramified enlargement of 018-021 is @355.
- **[rank 2] #328, MPL_142_001-093, N025.1.** G.'s missing automorphism criterion (cote 142, scan 025, "endomorphismes serait plus exact", "on ne sait pas alors … que u est un automorphisme"; scans 036, 039; LM 140-3 scan 059 (11 bis)): decide whether every endomorphism of the six-object profinite groupoid of 142/024-025 that satisfies his relations with a unit multiplier p is an automorphism, i.e. whether the two loop images then topologically generate F̂₂; in GT̂ terms, whether (λ, f) with λ ∈ Ẑ^× satisfying the defining relations always gives an automorphism x ↦ x^λ, y ↦ f⁻¹y^λf. Check first whether the GT literature (Drinfeld 1990; Ihara; Schneps) settles it.

### TAME: tame topology, stratified spaces, networks, pseudolines (Esquisse §5-6, §8)

- **[rank 1] #133, MPL_121_001-048, N49.** G.'s mobility stratification and his Conjecture 1 (cote 121, scans 026-028 and 034): for spaces of his admissible Boolean families (121/005-024), prove or refute (A) that the locus Y_i of points of exact mobility i is a pure i-manifold along which X is equisingular; (B) that X is locally Y_i × (N, a) with a immobile in N and the type of (N, a) constant on components of Y_i ("N est dévissable?"); (C) that Y_i is "le plus gros germe de sous-variété" carrying equisingularity; (D) Y_ν(Y×N) = Y × Y_{ν−i}(N); Conjecture 1, that a privileged partition into manifold leaves exists with one "plus grossière que toutes les autres"; and its relative form, the "description conjecturale" of the canonical partition of a proper map by recursion over the largest open of the base where it is locally trivial (121/036-037); compare with the intrinsic stratification of polyhedra (Akin 1969) and canonical stratifications of o-minimal sets; with @160 and @168.

### CYCLES: cycles, motives, integral PD de Rham, analysers

- **[rank 2] #243, MPL_136_142-188, N027.** G.'s classification of the endomorphisms and automorphisms of his divided-power de Rham functor (cote 136, scans 162-188: "Théorème … correspondent biunivoquement aux systèmes" (φ₀, A′, B′_i) with 2B′_iJ′ = 0, reconstruction "On reconstitue" (164, 168), completion (174-176), determinant criterion "il f. et s. que son indicateur soit … inversible" (176-178), representing ring Z[(A_jh),(B_ijh)]/(2B_ijh) localized at A₁₀ (178-180), scalar section and fibrewise pro-unipotent kernel (180), action by λ^i on H^i through Δ (180)): state the corrected theorem with the multiplication relations ξ_iξ_j = c_ij ξ_{i+j} of 184 (the notes find the retained parameter list misses them, N029-N031) and prove that the automorphism functor is the group scheme so represented, with the determinant criterion and the pro-unipotent kernel; Michel Hua's project's 136-automorphism-group-scheme concerns the same theorem; companion to @305.
- **[rank 3] #964, MPL_15_195-228+18_002-017, A34.** G.'s classification of places by motivic torsors (cote 15, scans 207-227): decide (i) "si M est pris assez grand" (15/223), whether the map from archimedean places σ of K to isomorphism classes of torsors Isom⊗(ω_σ, ω_σ₀) under the integral motivic group of ⟨M⟩ is injective; (ii) "∀ fibré principal homogène P … provient d'une place" (15/223), which torsors, under the marginal Riemann-Hodge compatibility, come from places; (iii) "que se passe-t-il … structures de Hodge ?" (15/225), whether the Hodge-enriched functor recovers the place, with the j-family on P¹ ∖ {0, 1, ∞} as G.'s test case; the bare-lattice bijection is marked false on 15/207, and the notes' X01-X03 give a conditional argument for (iii).

### GS (new): group schemes, representability and descent (cotes 31, 56, 90, 91, 131; LM1 line)

- **[rank 3] #189, MPL_131, RN022.** G.'s request "Donner l'exemple-type … montrant que (8°) n'est pas surabondant" (cote 131, scan 014): construct a functor over a one-dimensional base that satisfies every other condition of his unramified representability criterion (locality, filtered limits, prorepresentability, separation, local lifting; 131/002-016) and is not representable, or prove that 8° follows from them; joint with @247 and the promised removal of dimension restrictions (131/014 NB).
- **[rank 3] #1039, MPL_31_002-051, N018.** The converse left open in the printed SGA 3 (X §5.11 bis and its editorial note 44) for G.'s criterion on 31/014 ("réunion d'une suite", "aucune restriction sur S"): decide whether a group of multiplicative type whose character object is the union of a sequence of open and closed pieces finite over S is quasi-isotrivial, i.e. which finite étale cover trivializes it.

### QUAD (new): quadratic algebras and covers over a general base (cote 84)

- **[rank 3] #1264, MPL_84_097-145, A37.** G.'s non-étale generalization (84/121, "J'ai envie de vérifier", "sans condition étale", "Ceci doit généraliser"): for quadratic algebras A_1, A_2, A_3 over k and a section ε of their contracted product A_1 * A_2 * A_3, prove or refute that the fibre π^{-1}(ε) of Spec(A_1 ⊗ A_2 ⊗ A_3) carries a biquadratic structure whose three quadratic subalgebras are the A_i, in the enlarged quasi-quadratic setting the next page's nonflatness warning requires; the étale case is the (Z/2)²-torsor classification.

## Edition matters for the second pass, by package

### MPL_105

- #13, R31: Cote 105/016: the argument ending "because the Lawvere object is injective!!!" is the standard injective-interval argument for TF ⊂ W (Cisinski, Astérisque 308, ch. 1); the low-confidence diagonal words must not carry a reconstruction; Michel Hua's project's 105-interval-anodyne-generators is a notation to discuss, not the reading.

### MPL_11_002-042

- #54, H13: G.'s question "Suffit-il que le produit fibré existe … et que les dim. soient correctes?" (11/031) is answered negatively in the literal abstract reading by note O04 (composites id and 2·id): a normalization condition on the gauges is needed.
- #58, H18: Cote 11/040, "Conditions équivalentes": the target membership is weaker than the earlier stable-subspace formulation (RQ03); the statement must be fixed before any proof.
- #62, RT01: Provenance lead: the reused English typescript of cote 11 (internal pp. -2.12- to -3.14-, scans 004-041 and 043-054: linearization of the projective-group action, the flag complex with "Tits has shown", the parabolic chosen "according to a conjecture of Tits", configuration quotients, "arithmetic schemes of moduli of abelian varieties") matches the content of Mumford's Geometric Invariant Theory (1965), ch. 1-3; to be checked against the book.

### MPL_11_043-058+56

- #75, N010: Edition: the "relations" heading of 11/053 is empty; the list gives generators and counts only.
- #79, N035: Cote 56/005: the purity line "R^{n−1}f_* est « pur »…" is unfinished and overwritten; the parity cases and twists must keep the frozen doubts.
- #84, N047: Edition: on 56/022 the slots b′) "Énoncé dual" and e) "Si n pair" are unfinished, and the sentence on the middle extension stops after "par".
- #88, N064: Provenance: cote 56/006-033 is a draft of SGA 3, Exp. XII (maximal tori, Weyl group, reductive centre); the cancelled opening cites "BIBLE" (the Chevalley seminar), Borel conjugacy and "cf No6".
- #89, N069: Cote 56/016, Lemma 2.3 "un quotient d'un sous-groupe de W(T)": the map to W(R) need not be onto for arbitrary subtori (note N100: failure 1 → C₂ in SL₄); maximality, as in the printed proof, is needed.
- #92, N077: Edition: the reductive-centre existence (56/027) points forward to "Exp XIII"; the printed SGA 3 re-edition cites XVII and gives the continuation.
- #93, N081: Edition: the quotient-centre proof (56/031) ends mid-argument; the printed continuation uses Z′ → Hom(G/Z, Z) and G/Z → Hom(Z′, Z).

### MPL_121_001-048

- #113, N21: Cote 121/019 margin: F_A = {B ∩ A} for an arbitrary subset A fails c) (note N78); only the body's construction for A ∈ F stands.
- #141, N83: Provenance: the intrinsic immobile-point construction is attributed on 121/036-037 to the first letter to A'Campo; the letter must be identified. The compatibility obligations themselves are folded into #133.

### MPL_121_049-073+153+155

- #163, A02: Edition: the two right-hand sides "F∘(G+G′) =" and "F∘(GG′) =" on 153/002 are blank.

### MPL_12_150-168+15_002-033

- #179, D23: Cote 15/024, final margin "éliminer ce groupe … polarisation … cristalline": a proposed rigidification of the two residual μ₂ freedoms by real polarization and crystalline data, without comparison maps; record as G.'s proposal.

### MPL_131

- #180, RN002: Companion: Murre 1966 (Sém. Bourbaki, Exposé 294, Thm 1 and Cor. 2; note p. 247) is the printed comparator for the representability criterion of 131/002-016; Michel Hua's project's findings 131-locally-quasi-finite-representability and 131-unramified-and-etale-corollaries.
- #181, RN007: Cote 131/004: "les conditions 1° à 8° sont stables par tte extension de la base" must be read in the numbering of scan 002, not the reordered list of 014; it is not checked for the revised tests.
- #185, RN012: Cote 131/005: the lemma "Alors F est représentable" must be read with the constructibility hypothesis of 006 and Prop. 3 (033), not as unrestricted local-base descent.
- #191, RN025: Cote 131/012, 016-017: generic representability (RG) and generic modularity (8°) are different hypotheses; the end of Remarque 3 (016) is too uncertain to say which is asserted sufficient.
- #195, RN033: Cote 131/017, example c, "Hom [pointés] dans un groupe commutatif": the source scheme and its hypotheses must be stated; fixing a point does not make every mapping functor unramified.
- #196, RN034: Companion: SGA 3, XI §6.6 (Hom_{S-gr}(H, G) for an abelian scheme H: representable and unramified, not étale) for "Hom de V.A. dans un groupe comm." (131/017).
- #197, RN036: Cote 131/017, example f: the connected- and irreducible-component functors need definitions; "même étales" holds for connected components of proper flat maps with geometrically reduced fibres (Stacks 0E0D), not for irreducible components.
- #204, RN054: Cote 131/031: the construction of ξ₁ "grâce à 2°)" needs effectivity if condition 3 refers to the weakened maps of 025; the revised L-labels must be read first.

### MPL_133

- #214, G02: Cote 133/036-038: G.'s "Question DG ∩ Z(G) est-il unipotent ?" and the p-power-torsion claim stay open on the page; Michel Hua's project's finding 133-centre-and-derived-group-from-two-crossed-modules is limited accordingly.

### MPL_136_047-094

- #220, R018: Cote 136/072: in the comparison cube, "homot... fin." and "la quatrième" (arrow count) are uncertain readings; the faces must be enumerated, not repaired from the conclusion.
- #222, R023: Cote 136/077, condition D: "est stable par" is deleted and replaced by "sont nulles"; the graded divided-power convention must be stated.

### MPL_136_142-188

- #234, N013: Cote 136/146-147: "il y a lieu de décomposer M" with an unrestricted index set I needs a finite-support convention for the many-variable tensor expression.
- #240, N021: Cote 136/153-155: "est-il injectif ? Oui, par passage à la limite inductive sur I" proves injectivity for C ⊗ k^(I) → C^I (direct sum), not for the product k^I used just before; over a general ring the product case needs C Mittag-Leffler.
- #244, N028: Cote 136/162-164, 176: Corollary 1 carries an inserted NB qualification (a regular element of J′, an isomorphism, or the marked-generator condition) that must be kept when 2 is inverted; "a′₁ ≡ 1" (163) and "a₁₀ = λ₁" (176) disagree.
- #248, N035: Edition: the automaticity sentence "cette condition tjrs vérifiée si 2 est inv." is cancelled on 136/166, while the margins of 170 and 172 still use invertibility of 2 ("car les B′_i sont nuls!"); both must be recorded.
- #253, N041: Edition: on 136/176 "indicateur" is renamed "discriminant", then "déterminant", while the theorem below still says "indicateur".
- #258, N047: Edition: the hope for mod-2 Steenrod squares (136/180-182, "on peut espérer … carrés de Steenrod", "notamment puiss. de Steenrod") is answered on the same scan by an underlined marginal "Non"; record both, without generalizing the "Non".
- #261, N051: Edition: the second augmentation calculation (136/184, 188) stops at "β(A₁)^(i) = T^(i) … ou encore"; the continuation is outside the package.
- #267, N059: Companion/provenance: "Des résultats inédits de M. RAYNAUD … toujours satisfaite" (136/185, Lemma 5.9.2): Raynaud's result on representability of the pushed-out extension must be located.

### MPL_136_189-234

- #272, R024: Edition/companion: "histoire des opérations, de Cartier ----" (136/219) and "on doit avoir une histoire d'opérations de Cartier ----" (220) are unfinished; the companion can set them beside the Cartier isomorphism for the de Rham complex of a polynomial algebra and its dual for the PD-Koszul complex.
- #279, R055: Provenance: the reused French typescript in cote 136 (scans 142-188, printed pp. 27-134: Swan conductor, panachées extensions, Raynaud's unpublished results, the Néron property 5.7; scans 189-234: Theorem 5.4 on perfect duality of the abelian parts, 5.8 attributed to Raynaud, Cor. 5.10 "C'est le résultat conjecturé dans [8, 4.9]", 14.2 algebraic vs transcendental Tate-module maps) must be identified; SGA 7, Exp. IX (Modèles de Néron et monodromie) is the first candidate to check.
- #286, R065: Provenance: "POINTS DE GORENSTEIN D'UN MORPHISME / par Manuela STOIA" (136/216, 218) is a separate attributed text; its assertions are hers.

### MPL_142_001-093

- #318, N016.1: Error of the page (142/016): "ne change pas à équiv. près par l'extension … du corps de base" is false for the full étale fundamental group of an open curve in characteristic p (Artin-Schreier covers of A¹; Stacks 0A47); it holds for proper curves (0BQC) or in a tame/prime-to-p setting.
- #329, N025.3: Cote 142/025, "en fait, β détermine p…": false without a normalization; the identity and the central reflection τ both give β = 1, with p = 1 and p = −1 (compare Furusho 2010, Thm 2: the multiplier is determined only up to sign).
- #347, N040.1: Cote 142/040: the pairing of the six remaining relators into three independent ones depends on an uncertain marginal index, which must be resolved in the reading.
- #355, N045.2: Cote 142/045: the form x² − xy + y² is correct in the basis R_i, R_j (third vertex (−1, −1)); it must not be "corrected" to x² + xy + y², which belongs to another basis.
- #368, N052.2: Error of the page (142/052, margin): "ce sont des ouverts denses, et pour cette raison connexes" is false in the ordinary topology (R∖{0} in R); connectedness must come from the cut-disc argument.
- #372, N055.2: Reading (142/055): in the doubtful τ_∞(l_∞) = l₀|l₀⁻¹ · l₁, only l₀l₁ is compatible with the other two columns and l_∞ = (l₁l₀)⁻¹; the edition can note this algebraic constraint while keeping the frozen doubt.
- #380, N063.1: Cote 142/063: the label change from R_i^ω to R_{ωi}^ω in the boundary-pinning paragraph must be carried consistently into (44); the pinning depends on the orientation.
- #381, N064.1: Cote 142/064, (44): the doubtful left-hand Π₀|Π₁ and diagonal Ψ|ψ are reading questions; only the Π₁ / pinning reading supports the transition formula (45).
- #392, N072.2: Edition: the paragraph calling g_l "un 1-cocycle sur Γ" and its path-torsor reading (142/072) is deleted; it is not the author's final assertion (the live treatment is on 078-080, with f_l and g_l⁻¹ the cocycles).
- #411, N077.2: Cote 142/077: "un argument de descente … donne le résultat énoncé" for a finite closed cover needs neighbourhood or cofibration hypotheses (Brown 1967); closedness alone does not give van Kampen.
- #420, N079.5: Edition: the paragraph "Le théorème de Mordell-Weil implique" (142/079) is cancelled before its conclusion and restarted on 080-082.
- #424, N080.4: Companion: point separation through a semiabelian G (142/080-081) needs ∩_n nG(K) = 0 (Carlson-Stix 2026, Lemma 3.10), not finite generation of G(K), which fails for G_m over Q; the first-pass context text (scan 064) that says "finitely generated" for torus extensions must be corrected there.
- #427, N082.1: Companion: G.'s hope "on peut espérer donner des formules explicites" for the cocycle of a point (142/082) has partial later answers for the tripod: Ihara's universal power series for Jacobi sums (1986) and Anderson's hyperadelic gamma function (1989) on metabelian quotients.
- #443, N087.6: Edition: the announced "calculs symétriques" (142/087, "Avant de donner un principe …") are not carried out in the surviving section, which ends with the lifting lemma on 093.
- #454, N092.1: Cote 142/092: identifying C′ with a full subgroupoid needs injectivity on objects as well (pair groupoid → terminal groupoid); the syntactically uncertain extra injectivity hypothesis on the page must be carried through.

### MPL_142_094-122

- #472, R25: Companion: G.'s hope (142/100, "de nature trop platonique") for a conjecture in "propriétés internes des groupes profinis" starting from M_{0,4} and M_{0,5|3} is what Drinfeld (1990) and Ihara realized as GT̂, defined by relations on M_{0,4} and M_{0,5}; the uncertain subscript 5|3 must stay as read.

### MPL_144_001-061

- #486, N003.5: Companion: G.'s "Question de définir algébriquement les intersections de 'chemins'" (144/003) compares with Turaev's homotopy intersection form (1978) and the Goldman-Turaev Lie bialgebra (Massuyeau-Turaev 2013); the Galois-equivariant profinite version is the open part.
- #487, N004.2: Cote 144/004: "π₁(M^∞_{g,ν}) = 1 … itou" for the boundary does not follow from simple connectedness of the compactification; components, intersections and stack stabilizers must be accounted for.

### MPL_146_001-099

- #567, R061: Cote 146/047, 049: G.'s "vérifier que cette indexation" of the eigenlines against "la conv. de Stokes" is not resolved anywhere in 146; the edition records the open convention (orientation of P(V), boundary orientation, sign of the quarter-turn).

### MPL_147_048-137

- #635, N065-01: Cote 147/065: "ζ_p = [Spec Z/pZ] = i_{p!}(1)" presupposes a localization-compatible group K_! over Spec Z whose target, Tate element and base-change maps are not specified on the page; the edition records the convention (compare Ekedahl's Grothendieck group of stacks).
- #636, N065-03: Cote 147/065, "+½": the cusp stabilizer in characteristic 2 is the constant group Z/2, not μ₂; the value ½ there needs the weighting convention of 147/063.
- #649, R078-01: Cote 147/078 margin: G.'s doubt "Ce ne sont peut-être que des immersions" is confirmed by the note's genus-2, two-node example with two clutching presentations: the maps are local immersions, not embeddings.
- #651, R079-02: Edition: the reference "[5], n°5, p. 768′" (147/079) for the category of coverings of a germ is unidentified; a bibliographical lead to resolve.
- #657, R082-01: Cote 147/082: "c'est donc un groupoïde connexe" does not follow from connected inputs (the 2-fibre product of two points over BH is discrete on H); surjectivity on isotropy must be stated.
- #709, R116-01: Cote 147/116: G.'s answer to his question "sont mono ?" by invoking condition c) needs an extra hypothesis (the note gives a finite category satisfying the weighted Boolean source-fibre condition with non-monic source-target map); it holds for the geometric germ category.

### MPL_148_029-072

- #767, R23: Cote 148/050, 056, 061: total erasure replaces R_a by the empty set (cardinality 0) while the written quotient at r = 0 is Z/0Z = Z; the empty-mark convention must be stated explicitly.

### MPL_14_002-044

- #780, M09: Cote 14/009: "saturation que nous ne précisons pas ici" leaves the equivalence between intersections of the P(i) and Galois-invariant cones without a definition; G.'s question "est-elle automatiquement satisfaite ?" stays open on the page.
- #789, A10: Edition: "résulte de [ , 1.2.]" (14/029) has a blank citation for the action of correspondences on Albanese-kernel zero-cycles.
- #801, R03: Provenance lead: the typed English Brauer-group fragment in cote 14 (local separability vs central separable stalks, "Theorem III.1", "[5, Theorem A.2]", the sheaf double commutant) must be identified; Auslander-Goldman 1960 is a first candidate.

### MPL_150_044-084

- #837, F06: Cote 150/051, 062, 067: the margins "peut-être conséquence des autres" (transversality, 062), "peut être une conséquence de c) et de d)" (051) and "sans doute une conséquence de la condition précédente" (067) are not proved in 044-084; the conditions must stay separate hypotheses in the edition.

### MPL_154_127-176

- #906, C01: Cote 154/154: the frozen page supports the cube correspondence (stable generizations ↔ vertices, semistable ↔ edges, ν2^{ν−1} edges) but less definitely than Michel Hua's project's finding 154-generisation-cube states (parameter, one-vertex reading, straight-line contrast).
- #909, M03: Cote 154/157-158: the minus sign in ω* = −α* ∧ β* and "mais α′, β′, ω′ non associés" are part of the duality rule and must not be repaired to a global orientation convention.

### MPL_156-1+156-2

- #914, A01: Edition: the cancelled NB "Je présume … au plus deux segments … cercle" (156-1/003) is an abandoned formulation and a continuing question (025-027), not a theorem.
- #917, A08: Cote 156-1/007, 013: the common-initial-segment relation is declared an equivalence without a transitivity proof, and "compléter F3" (uncertain verb) changes the axiom; the version of F3 used must be stated at each appeal.
- #922, A28: Edition: the last intersection proof "Je dis que I∩J={x,y}" (156-1/026-027) breaks off at "on aurait br_t".
- #938, B50: Edition: the package stops at "Je dis que cette condition est en fait symétrique" (156-2/019); the symmetry is unproved.

### MPL_15_087-138

- #940, T01: Companion: G.'s real-fibre-functor criterion (15/117: torus kernel, primitive Tate character, μ₂ obstruction) compares with Deligne-Milne, Tannakian Categories, §§4-5 (polarizations and Weil structures); Michel Hua's project's finding 15-real-fibre-functor-criterion.
- #944, T15: Cote 15/123-125: the reading "Il [ne|me] semble pas" decides G.'s stance on the gerbe involution; it must stay marked.

### MPL_15_195-228+18_002-017

- #948, A09: Companion: the formula "La partie de niveau … le dernier sous-espace … est motivique" (15/205) is a draft of the generalized Hodge conjecture; Grothendieck 1969 ("Hodge's general conjecture is false for trivial reasons") gives the corrected filtration statement to cite beside it.
- #956, A23: Cote 15/215: the correction "géom. connexe" → "irred (pas néc. géom irred)" is a change of hypothesis that the edition must keep.
- #971, P06: Cote 18/006: "Ker u … connu", i.e. ker u = ker χ ∩ ker φ, needs ker u ⊆ ker χ (the Tate character factoring through u); the hypothesis must be stated.
- #973, P15: Companion: the written "Conj. de transcendance forte; alors ?" (18/011: trdeg_k k(α, β) = g + u) is stronger than Grothendieck's period conjecture (Bost-Charles 2016, §2.2); record it as G.'s formulation beside his 1966 note.
- #975, P20: Edition: the cancelled claim that the conjecture "Contient le th. de Schneider" with transcendence degree 3 for four elliptic periods (18/012) is stronger than Schneider's theorem; G.'s 1966 note (p. 102, n. 10) separates the two.
- #976, P22: Companion: the elliptic period conjecture "degré de transcendance égal à dim G (4 ou 2) ?" (18/013): the CM case (degree 2) is Chudnovsky's theorem; the non-CM degree 4 is open.
- #978, P24: Companion: "Peut-on avoir h ∈ Q̄" for the Hodge splitting of a non-CM elliptic curve (18/013) is Katz's later question (Katz 1976, Question 4.0.8); its current status is to be checked.

### MPL_16+47+54+44

- #988, R12: Companion: "canoniquement autodual" (16/019, (8.16)): the compatibility of the discriminant pairing with the cohomological pairings is left unverified in Grothendieck 1968 (Le groupe de Brauer III, Remark 8.5); the edition records it, later literature to be checked.

### MPL_2

- #1025, L10: Edition: on 2/025 the deleted "x^i = 0" is replaced by "(i−1)! x^i = 0"; the integral distinction is real (the note's n = 3 example).
- #1029, S18: Provenance: the cancelled reused bodies on 2/036, 039 ("morphismes de transition affines", "quasi-compacts et quasi-séparés") are from SGA 4, VII (pp. 363-364).

### MPL_31_002-051

- #1044, N034: Companion: the "Corollaire" cd_r(K) ≥ cd_r(k) + dim A (31/023) has the printed counterpart SGA 4, X Cor. 2.4 in its stated scope; this changes the reference status of Michel Hua's project's candidate 31-local-ring-cd-lower-bound; the equal-characteristic and regular-ring extensions need their own check.
- #1056, N077: Cote 31/048: H^i(g, G) ≅ H^i(g, U) for i ≥ 1 needs, in degree one, surjectivity on invariants G^g → (G/U)^g, not only surjectivity of G → G/U.
- #1058, N081: Edition: the arbitrary-field branch "Supposons que k soit quelconque …" (31/049) is left unwritten.

### MPL_33_002-049

- #1065, N71. The support exact and spectral sequences are left as headings: Edition: on 33/012 the support part ends with the bare headings "Suite" "exacte"/"spectrale....."; the sequences are not written.
- #1082, N48. Coxeter realizability is deferred beyond the necessary diagram restrictions: Provenance lead: the reused typescript on Coxeter groups and root systems in cote 33 (scans 005-049: necessary diagram restrictions, "il restera ensuite à voir que ces possibilités sont effectivement réalisées", nine types with data "rassemblées dans les planches II à X", the E6, E7, E8 tables of @1250-@1256) looks like a draft of Bourbaki, Groupes et algèbres de Lie, ch. VI and its Planches; to be checked.

### MPL_33_050-097

- #1094, N50: Provenance: scans 33/081-093 are a typescript of EGA IV, 0_IV §19.7.1 (typed pp. IV-1012-1015); the proof stops inside Lemma (19.7.1.8) on scan 081, its continuation being typed p. IV-1016.

### MPL_33_147-181+34_002-017

- #1144, R21. The global-symbol theorem exceeds the displayed zero-symbol implication: Provenance lead: the reused English analysis typescript of cote 33 (scans 095-097 and 171-179: global symbols on the tangent sphere bundle, completely continuous operators, regularizability, the multiplier i^n π^{m/2} Γ(n/2)/Γ((m+n)/2), references [14], [18a], [20f]) should be identified; Mikhlin's monograph on multidimensional singular integrals is a candidate to check.

### MPL_36_002-052

- #1148, N09: Cote 36/005: in "dim Ker(u_η)=0 ?" the generic subscript η (alternative s) must stay as read; changing it to the special fibre would change the question.
- #1156, N41: Cote 36/030, 032: the mismatched P/Q domains and n/n′ indices in (2.3.1)-(2.3.5) are kept literally; the compatibility proof must match each domain.
- #1161, N61: Edition: the definition of adjoint functors on 36/044 stops at "s'il existe un", and the pointed-Hom sequence below is incomplete.
- #1165, N68: Edition: the live morphism definition in "Je dis que le foncteur … est une équiv. de catégories" (36/048) stops at "tel que φ ∼".
- #1166, N71: Edition: Corollaire 1 at the foot of 36/048 continues on 050, not on the intervening Čech typescript 049.

### MPL_36_053-085+39

- #1173, N05: Provenance lead: the reused English typescript on reductive quotients in cote 36 (scans 053-059: Reynolds operators, affineness and properness with finite stabilizers, "Iwahori [ ]", the footnote "It seems very likely" that algebraicity follows a posteriori) may belong to the GIT draft identified at #62; to be checked.
- #1178, N11: Edition: the restriction calculation after "le double de l'extension canonique … splitte canoniquement" (36/058) is unfinished after "i.e.".
- #1180, N15: Edition: the reused sheet 36/066 ends "On peut montrer que tout groupe de Lie satis-"; the statement is interrupted.
- #1181, N17: Companion/attribution: the defect sequence 0 → _nΓ → H¹(X, μ_n) → H¹(X_η̄, μ_n)^I → Ker(w_n) → 0 (36/061-063) is called on the page "essentiellement une reformulation d'un résultat de M. RAYNAUD"; Michel Hua's project's finding 36-h1-invariant-cycle-defect should carry that attribution (SGA 7, IX).
- #1183, N21: Companion: on 36/061-062 Ker(w) is cyclic of order d′ dividing d, while 36/071 asks whether R is all of Z/dZ; the stronger question must not replace d′ by d, and Michel Hua's project's finding 36-h1-invariant-cycle-defect must be read with d′ (compare @1371).
- #1186, N29: Edition: the special case on 36/065 assumes "un 0-cycle de degré 1", which also removes the Picard/Brauer obstruction in its proof; the variant on 36/071 drops it; the two arguments are kept apart.
- #1187, N39: Edition: after the change from "lisses" to "plats" (36/074), the claim "les ℓ^ν G sont étales de t.f. sép." needs its argument: ℓ invertible makes ℓ^ν G unramified, flatness is the point to justify, compatibly in ν (Michel Hua's project's 36-orthogonality-regular-adic-base).

### MPL_43_094-142

- #1208, D13: Edition: on 43/117 the upper box writes H¹(K, B) as a product, while the diagram below gives only an extension of Ext¹(𝒜′⁰, Q/Z) by Ext(U, Q/Z) terms; no section is written.

### MPL_57_271-315

- #1230, C10: Provenance: 57/299, 301, 303 are leaves of the reused "Tribu 43" typescript (heading dated October 1957); their tasks (p-bases, derivations, differential sequences) belong to that text, not to the Picard notes.

### MPL_60_002-035

- #1231, Haar construction: Edition: in the reused Haar-measure typescript (60/010, 008, 006, 004, read in that order) "que si μ = 0 et f = 0" is false and should read "ou" (one-point group); uniqueness is sent to "Chap. VII" and the text stops on 004 inside the invariance argument. Existence and uniqueness are known (Weil 1940; Bourbaki, Intégration VII).
- #1232, Heights, symbolic degree, and normalization: Error of the reused exercises (60/024, 030): the degree defined by the least m with 𝔓^(m) ⊂ 𝔔 is not a length (cusp C = k[[t², t³]], 𝔔 = t⁴C: degree 3, length 4); so the printed criterion of ex. 1(b) rejects the principal ideal t⁴C, its generator choice fails for 𝔞 = 𝔪, y = t³, and the coefficient of ex. 2(d) inherits the defect.
- #1233, Additional separated exercise obligations: Edition: in the reused commutative-algebra exercises of cote 60, "composante primaire de C" (60/022, ex. 4(b)) must mean a component of πC, and r is defined through ∧^{r+1}E with the variable k (60/032, ex. 23); the other items are standard exercise claims on the different, the conductor and pseudo-invertible ideals (Bourbaki, Algèbre commutative VII) and editorial notes on reused sheets (60/014, 018).

### MPL_62_002-050

- #1241, A15: Edition: on 62/011 "Ici le discriminant s'explicite : -" is followed by no formula; the later "δ ≠ 0" must be read as δ a unit, and the y³ coefficient of the flex model must be a unit.

### MPL_84_097-145

- #1273, D06: Companion: the recollection dated "3 octobre" (cote 84) that on leaving in 1970 G. expected Deligne to prove the Weil conjectures soon (done: Deligne, La conjecture de Weil I, 1974) and the standard conjectures too (still open).

### MPL_90+91_002-018

- #1335, N90-T1: Provenance: the reused typescript leaves 90/003, 005 and 009 (connectedness through normality and punctured spectra, "le th. de Hartshorne", the cancelled "Remarques (18.9.6)") are a draft of EGA IV, §18; to be matched with the printed EGA IV_4.

### MPL_91_099-143

- #1357, RN126-03: Audit: on 91/126 the eventual-pullback criterion for constructible x̄ carries the inserted "(si X_i sont noeths)", which the summary of Michel Hua's project's Greenberg finding (H-G) omits.
- #1358, RN131-01: Audit: 91/131 writes a discrete valuation ring with perfect residue field, not a complete one as in Michel Hua's project's summary (H-G); the inserted "propre sur V" belongs to Y/V.

### MPL_93_002-046

- #1378, C08: Companion: G.'s "structures supplémentaires" on the crystals of finite groups, "que je n'ai pas réussi à dégager encore", "très probablement" a filtration on an object of a derived category (93/039), is the problem taken up by Berthelot-Breen-Messing (Théorie de Dieudonné cristalline II, LNM 930, 1982), Breuil (2000), Kisin (2006) and prismatic Dieudonné theory (Anschütz-Le Bras); the companion should carry this history and not record it as solved over a general base.

# SA19 H6: complete scoped audit of the supplied cote-43 transcriptions

**Finding:** no readable argument proving injectivity of the map from rational points of an open curve to conjugacy classes of sections of its arithmetic fundamental-group exact sequence was found in the supplied cote-43 corpus. This is a completed audit of those readable transcriptions, not a theorem of historical nonexistence and not an inspection of the original handwriting.

## Exact scope and evidence

The lead is `background/sweep3_SA19/HUNCHES.md`, H6. It reports the Pro package's finding on 43:94–142 and explicitly extends that claim to 1–93 and 143–208. The supplied corpus contains **195 separate nonblank transcription files** across that range. The absent scan labels are **14, 39, 44, 83, 88, 99, 111, 127, 157, 166, 175, 179, 194**. The audit does not infer the contents of an absent file. The saved source filenames, SHA-256 hashes, character counts, counts of uncertainty and illegibility macros, reader, topic group, and scope-limited outcome are in `outputs/c43_audit.tsv`; `code/build_c43_audit.py` reproduces this inventory.

DGJ read the full supplied text of all 184 files outside 43:56–66 during this research run. FHI independently re-read all eleven files 43:56–66 and explicitly certified their complete coverage: chain-completion rings, cosimplicial constructions, the theta-squared quotient, and completed residual endomorphism algebras, with no point-to-section injectivity argument. DGJ also inspected the substantive passages in that topic for the separate Part I audit, but the leaf-by-leaf manifest credits FHI for this interval. This division is stated rather than presenting a collective audit as a single reader's visual inspection.

The transcription macros `unsure`, `illegible`, `deleted`, and marginal insertions are retained in the sources. Thus “not found in readable supplied text” does not certify absence in an illegible string, an unresolved alternate reading, an omitted leaf, or another archival item. Keyword searching produced 71 planning matches, saved separately, but the conclusion above follows the complete topic-by-topic reading and does not equate a failed keyword search with a negative proof.

## Positive locators and potentially misleading matches

| Leaves | What is actually present | Why it is not the sought argument |
|---|---|---|
| 43:1–16 | Number-field reciprocity, ideles, local symbols, geometric Lang-style pairings | No rational-point map to fundamental-group sections. |
| 43:17–23 | Adelic divisor complexes, Jacobians, and Albanese-kernel pairings | A Jacobian diagram is not an injectivity-on-points proof. |
| **43:27–30** | The boxed open Abel map at 27; Rosenlicht universal property at 28; **injective Ext-one pullback** in Corollary 3 at 30 | This is the actual injectivity assertion. It concerns extension classes and torsors, not rational points or conjugacy classes of sections. |
| 43:31–35 | Proposed higher Ext/cohomology comparisons and reductions; speculative qualifications | The words “Il semble” and “et sans doute” are not completed proofs of the stronger comparison. |
| 43:36–69 | Big Witt groups, descent, residual complexes, chain completions, and endomorphism algebras | No Abel-map point-to-section argument. |
| 43:71–79 | Local cohomology and local Jacobians; at 77 a rational **torsor section** extends; at 78 a DVR/Galois diagram | “Section” concerns a principal homogeneous bundle, and the fundamental groups belong to a local field/valuation ring. |
| 43:80–82 | Augmented generalized-Jacobian/local-field Ext programme | The augmentation and cohomological comparisons are explicit, but no point-to-section injectivity proof occurs. |
| 43:84–98 | Comparisons of sites and categories; local duality and Néron functors | These are sheaf-theoretic and cohomological statements. |
| **43:101, 103, 105** | Reused printed material on stable homotopy, intrinsic joins and **cross-sections of Stiefel manifolds** | The word “cross-section” has a different topological subject. |
| 43:100–121 | Tate/Serre duality, Greenberg-type functors, and interspersed EGA drafts | At 113 the decomposition and inertia groups generate Galois groups; this is not an injection from rational points. |
| 43:122–142 | Curve duality, support cohomology, Jacobian torsion at 133, and reused sheaf/flatness proofs | Fundamental-group/Jacobian identifications at 133 do not state point-to-section injectivity. |
| **43:143–146** | Local and global duality; at 145 injectivity of a localization map in (H^1) under stated hypotheses | The source and target are cohomology groups, not points and sections. |
| 43:147–159 | Étale ℓ-adic modules, inverse systems of fundamental groups, and Serre Lie algebras | No Abel-map point-to-section proof. |
| **43:160–170** | Hom/Ext tables; at 167–169 injectivity from group extensions to primitive torsor classes | The proof normalizes a torsor section to prove it is multiplicative. This is again Ext-one injectivity. |
| 43:171–202 | Cartier duality, formal and proalgebraic groups, Dieudonné modules, category theory | No point-to-section injectivity argument. |
| **43:203–205** | Tate pairing from a section of the dual abelian scheme and its Brauer obstruction | These are scheme sections defining the Tate pairing. |
| **43:206–208** | Local symbols and an Albanese-kernel pairing, including (X\to\operatorname{Alb}(X)) at 207 | The point map is used to define a zero-cycle kernel and a pairing, with no injectivity claim. |

## The lead's cohomological inference has reversed variance

The lead then says that the derived Ext/cohomology comparison yields injectivity on abelian fundamental groups. The assertion explicitly proved at 43:30 is the injectivity of pullback

\[
\operatorname{Ext}^1(\mathscr P_{S,X/Y},G)\longrightarrow H^1(X-S,G).
\]

Its next sentence only conjectures a stronger direction: “Il semble que c'est [bijectif|surjectif]” when the indicated support covers the base. The two alternate words are unresolved in the supplied transcription; both readings are stronger than injectivity and are qualified by “Il semble.”

Whenever the terms identify with finite-constant torsors, pullback is

\[
\operatorname{Hom}_{\mathrm{cont}}(\pi_1(J)^{\mathrm{ab}},M)
\longrightarrow
\operatorname{Hom}_{\mathrm{cont}}(\pi_1(U)^{\mathrm{ab}},M).
\]

For all finite abelian (M), injectivity of this pullback detects **surjectivity** of the profinite abelian group map (\pi_1(U)^{\mathrm{ab}}\to\pi_1(J)^{\mathrm{ab}}). A proper closed image is separated by a character of a finite quotient. Conversely, a surjection gives injective pullback. The map (\mathbb Z/4\to\mathbb Z/2) is the elementary counterexample to the asserted implication to injectivity: its pullback on characters is injective for every finite coefficient group, but its kernel has order two.

A separately established bijection on all such characters would identify the profinite abelian groups. Neither conclusion, without further arguments, is the sought injectivity of a rational-point-to-section map.

## Final scoped status

- **Supplied readable corpus:** complete negative finding, with the per-file evidence preserved.
- **Precise Ext-one assertion and qualifiers:** textually verified at 43:27–35.
- **The sweep's inference to injectivity of the fundamental-group map:** refuted by the variance argument above.
- **Original scans, unreadable strings, omitted material, and historical nonexistence:** not established by this audit.

This closes the transcription-scope research gate. It does not close any stronger historical question.

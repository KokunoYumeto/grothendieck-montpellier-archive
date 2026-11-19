## Cotes 152 and 120: plane trees (SA20-7) and the axioms of a tame topology (SA20-12)

By Claude Opus 5.5 at effort max (reader 152_120, horizontal sweep 3), 19 Nov 2026.

**What was read:**
- All 38 pages of the package MPL_152+120, in the corrected files of the two second passes of 17 Nov 2026:
  - 152/001-013 and 120/001-006 by this reader, which read them against the scans then;
  - 120/007-025 by the parallel block.
- The first pass's notes and doubts.
- The sweep-2 tables.

Full working: `readings/152_120.md`. Check events, corrections and dependencies are in the TSV files of the same name.

### 1. Cote 152: "Catégorie des types de mots [dont arbres plans]" (after 19 May 1982)

**The paper.** The sheets are pin-feed paper of a computer centre:
- 006, 009 and 012 are IBM job logs and JCL of job PREDONTA/1125, dated "19 MAY 82" (009) and SYS82139.T163912 (006): day 139 of 1982 is 19 May.
- 003 is written over the printout lines, so it is later.

**What he does, in order.**
- **002.** A sheet of drawings: one-, two- and three-letter "systèmes" (u, u^{-1}, uv, …), "syst. u^{-1}u" drawn as a circle cut by a chord between u^{-1} and u, families of pointed trees, and two boxed operations, "composition" and "insertion d'un cycle".
- **003.** The claim: "La cat. des ``types de mots'' de long. n équivaut : la cat. \unsure{isotypique|isotopique} des systèmes formés d'un disque D … d'un ``découpage par cordes'' de ce disque". The data are (D, ω, K, S_0) with n boundary vertices S, and a "reduced order" Σ_{α⊂R_0}(Card(α∩S) − 1).
  - Above it, corrected in the second pass: "disques or. découpés par cordes ⟷ arbres circularisés ⟷ contours à involution sans pt fixe [non pénétrante]". This is the whole correspondence of 010-011, already on the first sheet.
- **004.** "Admissible" graphs: a segment graph with an involution σ on its edges, defined by contracting an edge of an orbit of two consecutive edges.
- **005, "Arbres plans".**
  - Trees as (S, A ⊂ 𝔓_2(S)).
  - Plane trees as germs of embeddings, which are the bicircularisations (ε, c: ε → circ(Γ)).
  - In an oriented surface, circularisations, which depend only on the vertices of degree ≥ 3.
- **007-008.** Cutting a surface along a plane tree gives a polygon. For a general circularised graph one gets a contour on the arcs Ā, with the reversal σ and the rotation ρ. The rewritten formulas for σ_1^C and ρ_C follow.
- **010, "En résumé".**
  - Circularised graphs without isolated vertex ≃ oriented contours with a fixed-point-free involution on the edges.
  - The dictionary: ρ_Γσ_Γ ↤ ρ_C, ρ_Γ ↤ ρ_Cσ_C. The construction is called "déploiement du graphe plan donné".
  - A margin speaks of "la \unsure{carte} actuelle définie par Γ".
  - Boxed: "Γ un arbre ⟺ C est un polygone comb. (non ponctuel), et l'involution σ_C … est totalement non pénétrante".
- **011 and 013.**
  - |Γ| is the quotient of |C| gluing a with σ_C^a, orientations reversed.
  - For trees: C is the boundary of a disc, the paired edges are joined by disjoint chords, regions are vertices and frontiers are edges.
  - "La catégorie des arbres plans (pas néc. plus orientés) est équivalente : la catégorie \unsure{isotypique|isotopique} des disques … munis d'un tel découpage".

**What is proved and checked (re-derived).**
- The count of circularisations, Π_s(card A_s − 1)!, and the bicircularisations as germs.
- The dictionary of 010: faces are the orbits of ρσ, and (σ, ρ) ↦ (σ, ρσ) is invertible. Rows 2-3 force row 1 to read σ_Γ ⟷ σ_C; the ink is unresolved.
- The tree criterion: for a one-face map V − E + 1 = 2 − 2g, so tree ⟺ genus 0 ⟺ the pairing is non-crossing.
- The quotient |C| → |Γ|.
- The disc picture: n disjoint chords give n+1 regions and a tree; both sides are counted by Catalan numbers.
- His "d'ordre ≤ 1, il y en a un et un seul" (005) is the ink and is true. It is weaker than the ≤ 2 his preceding sentence gives.

**What is wrong.**
- **The head of 010 against the dictionary.** The head ("σ_Γ = σ_C, ρ_Γ = ρ_C") contradicts row 3 (ρ_Γ = ρ_Cσ_C) unless σ_C = id. The dictionary is the coherent version. Michel Hua's project notes the same disagreement.
- **The rule of 004.** It does not characterise non-penetrating involutions:
  - Read literally (one edge contracted, its partner left fixed), it admits only involutions whose 2-orbits are consecutive pairs. It rejects the nested (1 4)(2 3), whose chords do not cross.
  - Contracting both edges of the orbit gives the usual test for non-crossing pairings. The struck "deux" in "l'une des \deleted{deux} arêtes" is his hesitation at this point.
  - Fixed edges (σ = (1 3) on three edges) are outside the scan-10 criterion in either reading (the first pass's P05, @902).

**What is open.**
- "Type de mot" is defined nowhere on these pages, so the equivalence of 003 cannot be checked. The obvious reading (chords as cancelling pairs, reduced order as reduced length) does not fit the one-letter case.
- Whether "isotypique" (a category of types) or "isotopique" (isotopy classes) is meant. The user's eye on 003 and 013 decides.
- The operations of 002.

**How it connects.**
- The same objects carry the global tag H00J (SA10-18; not read here).
- The word [the user's words, omitted] for the planar structure, on paper of May 1982 or later, comes two years before the Esquisse's cartes and dessins (hunch H20-152_120-1).
- Cote 152 and cote 120 share a package, not a subject.

### 2. Cote 120: "Topologie modérée" (the axioms, 120/002-025)

**The title sheet (002).** "Topologie [over struck "Structures"] modérée", "(Autour de l'Eloge)", and a faint pencil \unsure{1978|1778}. Michel Hua's project reads 1978, a label rather than the date of writing.

**(I) Models (003-006).**
- **The axioms.** Classes M_n ⊂ 𝔓(Rⁿ) closed under the coordinate maps u^*: images (M1), inverse images under the injective ones (M2), traces u^{*-1}(B) ∩ A (M3), and products (M4). He reduces M1-M3 to generators (004). Re-derived.
- **Intersections.** "M1, M2, M4 impliquent que les [M_n] sont stables par intersection de deux": A∩B = δ^{-1}(A×B). Re-derived, with his inserted "(moyennant M1, M2, M4)". The page writes 𝔖_n for M_n, a slip.
- **The M3 reduction.** The mathematics requires "pour u injectif", since the standard projection is u^* for an injection. The ink, "surjectif|injectif", is open; Michel Hua's project reads "surjectif".
- **Trivial cases.** ∅, {∅} and filter bases are excluded; M′_n = M_n ∪ {∅}; and M_∅ = {∅, {e}}. All re-derived.
- **Points.** R_0 is the set of points x with {x} moderate. The revision "R_0 ≠ ∅" → "Card R_0 ≥ 2" gives ∅ ∈ M_1 (005, confirmed on the ink; @922). His "{x} ∈ Rⁿ" is a slip for M_n.
- **Examples.** Card ≤ 1, finite, all: "Aucun de ces exemples … pour nous!"
- **(II) The category.** Moderate maps are those with moderate graph. Identities, composites ("via M2", fitting the composite) and inverses of bijections are moderate. This gives Esp_{M_*}, with a faithful, conservative and transportable |·|. Finite limits exist with no hypothesis. The final object is the model {e} of R^∅, which is why he struck "(M5) R_0 ≠ ∅ … objet final" on 007.

**The reconstruction (008, 018) is incomplete.**
- His claim: "la donnée d'un M_* est équivalente à la donnée d'un système (E, R, X ↦ |X|)" with finite limits, |·| left exact, and every object embedding in some Rⁿ.
- The forward direction holds. The converse also needs:
  - |·| faithful, conservative and transportable, which he states on 006 and 018 but not here;
  - an image axiom, the categorical M1.
- Finite limits give M2-M4, and M1 only for maps injective on the set.
- Whether full M1 follows is open (package R20-152_120-2).

**Colimits (009-014).**
- **Finite sums** need Card R_0 ≥ 2 and M5 (finite unions; 009, 010). With Card R_0 = 1 the sum 1 ⊔ 1 cannot exist with |·| commuting. So 015's "Si R_0 ≠ ∅ … sommes disjointes" keeps a superseded hypothesis.
- **Colimits with a compatible structure** (009, proved on 012).
- **The amalgam criterion of 011.** For two inclusions X_1 ↩ Z ↪ X_2, the pushout exists iff finitely many pairs of moderate functions agree on Z and separate points. Re-derived both ways; "R^I" is a slip for R^A.
- **M6 (013)** ("Z a common fibre of finitely many functions that separate X∖Z") ⟺ the strict quotient X/Z exists. Re-derived.
- **M7** is the extension of moderate functions from Z to X.
- **"Moyennant M5, M6, M7, les sommes amalgamées … existent"** (014). Re-derived through the explicit embedding x ↦ (a_1, h_1, e_2), (a_2, e_1, h_2).

**Ind-spaces and topology (015-020).**
- **Ind-spaces.** Strict ind-moderate spaces are built under M8, R being the union of its moderate parts. Quotients by locally moderate parts exist (016). His warning that subobjects need not be locally moderate (017) holds: n ↦ 1/n from a countable discrete ind-space to R.
- **Continuity.** With R separated and moderate parts compact, moderate maps are continuous: graph projections. Re-derived.
- **The induced topology (018).** The colimit topology induces each moderate part's own topology. This holds for any directed system of compact Hausdorff pieces; his "ind-dénombrable" is not needed for it (it matters for products).
- **M10** gives moderate neighbourhood bases.
- **Locality (019).** Moderate maps form a sheaf, by compactness and M5. A structure is determined by its moderate functions with (M1)_0-(M4). Re-derived.
- **Locally moderate spaces (020).** "les parties compactes sont les parties contenues dans une partie modérée" is false as written ((0,1) ⊂ [0,1]). It is true for the relatively compact parts.
- **The margin of 020.** "Dire qu'une partie compacte et … d'un espace modéré est modérée" fails in every o-minimal model (the Cantor set) unless it reads "compacte et loc. modérée", which a struck "loc." beside it suggests. One look at the scan decides (hunch H20-152_120-6).

**The field (021-024).**
- **M11:** a) 0 [et|≠] 1 ∈ R_0; b) x−y and xy moderate; c) inverses bounded ("OPS B = A^{-1} !").
- a)-b) ⟺ the moderate functions form a ring. Re-derived.
- R_0 is a subring, and then a subfield (023). His "∈ M_1" for the inverse graph is a slip for M_2.
- **The Proposition of 024.** The zero set Y of finitely many moderate functions can be cut out by functions f_α, f_α g_β that separate X∖Y. Re-derived. "sépare les pts de X" is an overstatement (endpoints of [0,1]). The hypotheses "M1 : M7 et M11" can be reduced to M1-M4 and M11.
- **Consequence (hunch H20-152_120-5).** Under M11, M6 reduces to "moderate parts are common zero sets".

**À prouver (025).**
- Generic triviality of a morphism over the complement of a rare moderate part. This is Hardt's theorem in the o-minimal setting (from memory).
- His "Énoncé analogue pour un diagramme fini … ?!" holds for diagrams of inclusions, his example Z ⊂ X ⊂ Y × [0,1].
- It fails with parallel arrows: a semialgebraic family of rotations of S¹ over (0,1) has a varying rotation number. This agrees with the first pass's Q4-07.

**What is open on 120.**
- The reconstruction.
- Generic triviality (his "À prouver").
- The fragmentary slanted margins of 006-008, 013, 015.
- The reading of the 020 margin.
- The o-minimal comparison (SA20-10, SA20-11), left to the 121 reader with the prompted questions. The axiom list for it, as on the pages: M0 007, M1-M4 003, M5 010, M6-M7 013, M8 015, compactness 017, M10 018, M11 021.

### 3. The transcriptions

| Cote, scans | Passes | Open readings that matter | Ready to edit and translate |
|---|---|---|---|
| 152/001-013 | Pro first pass + audit; Claude second pass (17 Nov, Hua as witness); sweep 3 | 003 isotypique\|isotopique, arête\|cpt., non\|mais pénétrante\|pointés; 004 ε\|ξ; 008 boxed formulas; 010 row 1 (σ_C by the mathematics) | 004-005, 011, 013 yes; 003, 007-008, 010 after the user's eye on these places; 002 after a TikZ check; the printouts 006, 009, 012 (others' job logs) for the user's decision |
| 120/001-006 | the same | 003 surjectif\|injectif (injectif by the mathematics), the heading; 005 I ≠\|= ∅ | yes |
| 120/007-025 | the same (parallel block) | 015, 019, 020 margin, 021 [the user's words, omitted], 025; slanted margins fragmentary | yes, with the marks |

**Corrections to sweep 2.** The PLACEMENT, OBJECTS and CLAIM_LINKS rows of SA20-7 give cote 120 and places like "120/003": they are cote 152. The A120 rows cite context scans of cotes 147 and 149 as "120/1xx".

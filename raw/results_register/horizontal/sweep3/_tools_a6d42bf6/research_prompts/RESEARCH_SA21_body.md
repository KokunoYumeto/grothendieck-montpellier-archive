# RESEARCH_SA21: Grothendieck's axiomatics of forms of 1986 (cote 156): the supports and the orthomodular law, the axiom systems, and the maquettes

**To be settled, in three Parts:**
- **A.** The lattices of supports of his "ateliers" and "magasins": when they are orthomodular, when Boolean, and what his own theorems on them become. A.1 is the main question.
- **B.** His successive axiom systems for "contrées", ateliers and magasins: what implies what, what replaces his false axiom C4, the event-structure dictionary, and the o-minimal model.
- **C.** His oriented "maquettes" in every dimension, against regular cell complexes.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA21`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It is the deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA21_study.zip`: our study of cote 156.**
  - `study/STUDY.md`. §0 gives the state after the readings, §2 the reading of 156-4 in full, §5 the later parts, and at the end the readers' summaries.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the full readings of 156-3, 156-5, 156-6, 156-7 (two readings), 156-8 and 156-9, each with its tables, and the checking programs `156-5_sorite_checks.py` and `156-8_checks.py`.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the topic's items SA21-1 to SA21-15.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA21_transcriptions.zip`: the AI transcriptions (LaTeX) of cote 156.**
  - 156-1 and 156-2 by GPT-6 Astra (ChatGPT Pro mode), with notes and doubts.
  - 156-3 to 156-9 by GPT-6 Astra at reasoning effort max in Codex web, one file per folder of 4 to 12 scans, with the doubts tables.
  - `\scanpage{N}` marks scan N of the cote's PDF; the archive's pencil page is N−1. The transcriptions carry `\unsure{a|b}` marks.
  - The readings above decided some readings on the scan images, and their CORRECTIONS tables give them. Where a step of yours depends on a doubtful reading, say so.
- **`RESEARCH_SA21_literature.zip`:** the LaTeX source of L. Román, "Orthomodular lattices and quantales" (arXiv math/0211133).
  - Fetch the other sources yourself. They are listed under "Sources" below.

## Where this comes from

**The pages.** Cote 156 of the Grothendieck archive at the University of Montpellier ("Vers une géométrie des formes") holds nine parts of handwritten notes, about 700 scans, from 8 June to 15 July 1986. In them Grothendieck axiomatizes "tame" geometric forms without points:
1. the contrées of 156-4, with figures, multistrates, lieux, refinement ≪, subdivision and the supports Σ;
2. the ateliers of 156-6 and 156-7;
3. the magasins of 156-8, with the relation |∘| ("intérieurement disjoints") as primitive;
4. in 156-9, after he swaps the two words on 9 July, the ateliers again, with the supports as ortholattices.

156-3 and 156-5 are the one-dimensional and the set-theoretic models.

**Our reading of them.** Sweep 3 of our horizontal reading (18-19 Nov 2026) read these parts:
- 156-4 in full, by a6d42bf6;
- 156-3, 156-5, 156-6, 156-7 and 156-8 in full, by readers (all Claude Opus 5.5 at effort max);
- 156-9 in full in two rounds, except the drawings of scan 112.

**Other work.** We know of no published study of these pages; check this. Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA21-R8-25).** In a faithful magasin, Σ_M is the algebra of regular open sets of the Alexandrov topology of (M, ≪°). It is a complete Boolean algebra, and Axiome supp 1 (156-8/88) holds.
- **R2 (156-9 reading; SA21-R9-10).** Under divisibility and Mag L2, the magasin is faithful exactly when Σ is Boolean with the lieux as distinct atoms. The plain form "Σ distributive ⇔ faithful" is false: two lieux that are not disjoint give Σ = {∅, M}.
- **R3 (SA21-R9-05 to -08).** His "spatios" (156-9/78-80) are complete ortholattices.
  - His Lemma 1 and Corollary 1 (156-9/109-111) and his "axiome des supports" (156-9/117) are the orthomodular law, for the spatial figures.
  - The law fails on the hexagon O₆, which arises from the fence a′ < a > b < b′; the smallest counterexample has 6 elements.
  - MO₂ is orthomodular but not Boolean.
- **R4.** The support lattice is not distributive in general: his own counterexample is the "ficelle à deux brins" (156-7/82-84).
  - His formal Lemma of 156-7/97-99 is the orthomodular law, and it is false: see the path A′–A–B–B′.
  - Σ ≅ P(L) when the disjointness of lieux is "≠".
- **R5 (SA21-K7b-15, SA21-R7b-21).** The Théorème of 156-7/94 is false under all its hypotheses: relative complements S_{A−B} = S_A ∧ C(S_B), and commutation with infima.
  - An eight-element atelier with a seven-lieu disjointness graph satisfies L1-L3, CL(spac), At D, At supp and At supp 1, and both conclusions fail.
  - The theorem holds where distinct lieux are disjoint.
- **R6 (SA21-K5-01).** 156-4's axiom C4 fails in the set-theoretic model Fig(L) of 156-5: the multistrates have 3 components on 2 points and 5 on 3. His claim on 156-5/13-15 that C4 "est automatique" is false.
- **R7 (156-6 reading).** At 13, "l'axiome du support", makes subdivision equal to maximal refinement. The induced refinement is an infimum for ≪; in 156-6 this is a theorem, where 156-4 had it as an axiom.
- **R8 (SA21-R8-01 to -08).** Mag 1-4 (156-8/8) imply the compatibility-disjunction axioms of 156-6 and 156-7 and the gluing of refinements.
  - The weakened Mag 4′ of 28 June is too weak (maquette countermodel).
  - The Proposition-Scholie of 156-8/16-17 lacks the transitivity of ≪°. There is a five-element countermodel, and the ≪°-form repairs it.
- **R9 (SA21-R8-32, -33).** Oriented maquettes:
  - in dimension ≤ 1 they are Serre's graphs;
  - in dimension 2 they are Serre graphs with 2-cells whose boundary is a vertex-disjoint union of directed cycles;
  - with "∂X connected" added, they are the 2-complexes whose cells are attached along closed edge paths through no vertex twice.
- **R10 (SA21-K7-03).** "Polyédral + At simp 1" (156-7/14-15) does not characterize simplices: the face poset of a square satisfies both.
- **R11 (156-3 reading).** On a totally ordered tronçon L, the tame parts Mod(L) are exactly the finite unions of points and open intervals, the definable sets of the o-minimal structure (L, <).
- **R12 (SA21-C3-05).** The finite contrées of 156-4/62 are the triples (M, ≤, R) with M_{≤x} finite and R reflexive, symmetric and closed downward. Their figures are the finite downward-closed R-cliques.
- **R14 (reader C, round 2: SA21-R9b-01 to -29, SA21-K9b-01 to -09).**
  - Axiome supp 1 holds in the magasin of an ordered set: he proves it for figures inside one flag (156-9/21-22), and it held for all 4,724 figures of the magasins of the connected orders with at most 5 elements.
  - His duality cosupp°Φ = Omb°Φ* (156-9/16) holds.
  - His Question of 156-9/3 holds for magasins of connected ordered sets and fails for local ateliers in general (a path of four lieux; twin lieux).
  - For the comparability disjoncteur of an ordered set, cograph ⇒ orthomodular is proved, and the converse fails: on 5 vertices, 60 non-cographs have orthomodular Σ, one with Σ = 2³.
  - His Lemme 1 of 156-9/72 is false, and his own Prop 4 repairs it.
- **R13 (156-8/90-127, 156-9/5-16).** The magasin of an ordered set L has points and intervals, with the positional order a < I_{a,b} < b.
  - |∘| is the comparability of that order, and the finite figures are the flags of the positional order.
  - It satisfies Mag 1-4 for every L. It is faithful exactly when L is total.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** The finite contrées of R12 are exactly the prime event structures with finite causes (Nielsen-Plotkin-Winskel), with figures as the finite configurations. Refinement, subdivision and Σ become notions of the domain of configurations.
- **L2 (replaces the cograph hunch, which R14 refutes as an equivalence).** For an ordered set, the support lattice of its comparability disjoncteur is orthomodular exactly when every induced fence N lies under a "repair", that is, when the comparability graph is a Dacey graph in Sumner's sense (D. P. Sumner, "Dacey graphs", J. Austral. Math. Soc. 18 (1974)).
- **L3.** In magasins with cords and strands, the failure of distributivity of Σ is measured exactly by the pairs of distinct lieux that are not disjoint.
- **L4.** Oriented maquettes in which every interval of length 2 is a signed diamond and the link of each cell is connected are the face posets of regular CW complexes with an orientation of each cell, after loops are excluded.
- **L5.** The o-minimal model:
  - in an o-minimal structure, the definable cells (or the definable stratifications with the frontier condition) form an atelier that is faithful, so Σ is Boolean by R1;
  - it is "modérée" in the sense of 156-4/70 (any two subdivisions have a common refinement), by the definable triangulation theorem.
- **L6.** Under Mag 1-4, every "facultatif" axiom of 156-6 and 156-7 except At L1, At supp and At 13 is a theorem.
- **L7.** His spatios and their "disjoncteurs" (156-9/61-108) are the orthogonality spaces of Foulis and Randall and of Dacey, and his correspondences of disjoncteurs are their morphisms.

## What the outcome must be

{{OUTCOME}}

## Parts

**A. The supports and the orthomodular law. The main question is A.1.**
- **A.1 (main).** Determine exactly which ordered sets L have an orthomodular support lattice, and exactly which have a Boolean one. Prove both directions of each condition.
  - **For the comparability disjoncteur of L.** R14 gives cograph ⇒ orthomodular, and refutes the converse. Settle L2.
  - **For the magasin M(L) with its segments (R13).** Axiome supp 1 holds there (R14). Decide whether the whole Σ_M is orthomodular.
  - **His 10-element counterexample of 156-9/113** ("Card Σ = 10"). Reconstruct it and check it; the transcribed arrows do not form a lattice.
- **A.2.** Determine the class of magasins satisfying Mag 1-4, Mag L2 and divisibility whose support lattice is orthomodular.
  - Prove or refute, in that generality, that Axiome supp 1 (156-8/88) is equivalent to the orthomodular law for the spatial figures (156-9/117).
  - His margin "Oui !" on 156-8/89 says the axiom fails for some disjunctive magmas, without an example on the page. Give such a magma, or prove that none exists.
- **A.3.** His Question of 156-9/3 asks whether supp°x is an atom of Σ* = Σ ∖ {0} for every lieu x. It holds in faithful divisible magasins and in the magasins of connected ordered sets, and it fails for local ateliers in general (R14). Determine exactly the class of ateliers in which it holds.
- **A.4.** Determine exactly the class of ateliers in which the Théorème of 156-7/94 holds (R5). Settle L3.
- **A.5.** His question of 156-8/88: give a faithful support function that is not fully faithful, or prove that none exists.

**B. The axiom systems.**
- **B.1.** Write every axiom system of cote 156 side by side, with each implication between them proved and each non-implication shown by a model:
  - 156-4: Cont 1-5, C1-C8₀;
  - 156-6: At 1-At 14;
  - 156-7: At CD, At C, At D, At L1-L3, CL, At supp;
  - 156-8: Mag 1-4, Mag 1′-4′, Mog L1-L2, Mog div 3, At 1-At 5, At Fil;
  - 156-9: At 1-4 after the swap of names, At spat 1-3.

  Settle the open implications:
  - At 9_Σ + At 10 ⇒ At 12 (156-6);
  - the uniqueness in At 14 bis (156-6/88: "Je présume qu'on doit pouvoir prouver qu'un tel F′ est unique");
  - the converse of the Théorème-Scholie of 156-6/29-34;
  - L6.
- **B.2.** C4 is false in Fig(L) (R6). Determine the true connectedness statement that holds in Fig(L) and in the o-minimal model of B.4, and prove it.
- **B.3.** Prove or refute L1. If it holds, translate refinement, subdivision and Σ into the theory of event structures and domains. If it fails, determine the class of event structures that the finite contrées are.
- **B.4.** Settle L5.
  - For an o-minimal expansion of a real closed field and a definable set X, define the atelier of definable cells, or of definable stratifications with the frontier condition, of X.
  - Prove which of the axioms of B.1 it satisfies, that it is faithful, and that it is "modérée". Cite the triangulation and refinement theorems you use with exact locators.

**C. The maquettes.**
- **C.1.** Settle L4. Determine the axiom on oriented maquettes (Magor 1-6, ≪° = id, |∘| = ≠, 156-8/4-6) that gives connected cell boundaries. Prove that with it the oriented maquettes of every dimension are exactly the face posets of regular CW complexes with oriented cells, after loops are excluded. Where this is false, give the correct statement with its proof.
- **C.2.** Place within C.1 his "ateliers polyédraux" and "simpliciaux" (At pol 1 + At simp 1, 156-7/14-15) and the flags of 156-9/5-7. Determine the axiom on a maquette that characterizes simplicial complexes; R10 shows that his does not.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- G. Kalmbach, *Orthomodular lattices* (1983). L. Beran, *Orthomodular lattices: algebraic approach* (1985). The Foulis-Holland theorem.
- M. Nielsen, G. Plotkin, G. Winskel, "Petri nets, event structures and domains, part I", Theoret. Comput. Sci. 13 (1981). G. Winskel, "Event structures", LNCS 255 (1987).
- M. C. McCord, Duke Math. J. 33 (1966). A. Björner, "Posets, regular CW complexes and Bruhat order", European J. Combin. 5 (1984). J. A. Barmak, *Algebraic topology of finite topological spaces and applications*, LNM 2032 (2011).
- L. van den Dries, *Tame topology and o-minimal structures*, LMS Lecture Note Series 248 (1998). M. Shiota, *Geometry of subanalytic and semialgebraic sets* (1997). A. Pillay and C. Steinhorn, "Definable sets in ordered structures I", Trans. AMS 295 (1986).
- T. Gallai, "Transitiv orientierbare Graphen" (1967). D. G. Corneil, H. Lerchs, L. Stewart Burlingham, "Complement reducible graphs" (1981).
- J.-P. Serre, *Arbres, amalgames, SL₂*, Astérisque 46 (1977).
- D. J. Foulis and C. H. Randall, "Operational statistics I" (1972). J. R. Dacey, *Orthomodular spaces* (thesis, 1968).

{{RULES}}

{{DELIVER}}

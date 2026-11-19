# SA20: research packages, in concept (sweep 3)

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. These are concepts only; no prompt is written tonight.

## R20-1. Cote 123 against the literature: the simultaneous resolution, the dimension conjecture, the subregular case

- **Question:**
  - How do 123/004–014 (simultaneous resolution over a base, with Pic) and the letter of 22.10.1969 compare with
    Brieskorn (ICM 1970), Slodowy (LNM 815, 1980), Steinberg (LNM 366, 1974; Invent. Math. 36, 1976), Springer (Publ.
    IHÉS 30, 1966), Spaltenstein, and Hesselink (rational singularities)?
  - What in cote 123 is unpublished: the base-S form, the Pic sequence, the remark on 014, the RigKos count?
  - Which of the letter's questions were answered, by whom, and where?
- **Why:** the folder may be the primary source of results known only through others; the letter is a dated statement
  of "Grothendieck's conjecture" (H20-1, H20-2).
- **Rests on:** SA20-W1, W3, W4; 123/004–048; `sweep2/REPORTS/letter_to_kostant_123.md`.
- **Strongest known:**
  - Douglass–Röhrle (arXiv:0802.0764) attribute the dimension formula to a conjecture of Grothendieck.
  - Everything else is from memory.
- **Material:**
  - the five Codex transcriptions and the 48 scan images of cote 123;
  - the papers listed, from open sources (the ICM 1970 proceedings are on mathunion.org; Inventiones 1976 on GDZ or
    EuDML);
  - SGA 3, exposés XIII–XIV.

## R20-2. Computations in the Weyl groups and Lie algebras that his questions ask for

- **Question** (four computations, type by type for all simple types):
  - (a) Does N_W(⟨c⟩) split over ⟨c⟩ (123/002), and does N ∩ N′ split over μ_h × Z (029)?
  - (b) The signs by which outer automorphisms act on 𝔤_ψ and on Kostant's line Δ (034, 042, 035), and whether
    𝔤_ψ ≅ Δ canonically.
  - (c) Which single vanishings in Σ x^α e_α (α ∈ Σ ∪ {−ψ}) give regular nilpotents (047).
  - (d) The map from Dynkin classes to parabolic classes, c ↦ c′: where is it injective, and which classes give a
    Borel (019–020)?
- **Why:** his own open questions on these pages. Each has a finite, checkable answer, and (d) corrects his A₃ margin.
- **Rests on:** 123/002, 019–020, 029, 031, 034–035, 042, 047.
- **Strongest known:**
  - (d) is done for A₂, A₃, A₄ here;
  - (c) is answered in principle by Kac's classification (from memory).
- **Material:**
  - the root data;
  - a computer algebra system (GAP or Sage; or Python with explicit Chevalley bases);
  - the transcriptions K123-02 and K123-03 and C123-01.

## R20-3. Cote 122 against Milnor (1968) and SGA 7: the self-dual triangle and the missing step

- **Question:**
  - (a) Settle the sign in the self-transposition of the triangle (a′) (122/022–026) and his claims that the pairings
    λ and μ are β and α.
  - (b) Prove, in his framework, H^{n−1}(M) = 0 for an isolated singular point with smooth total space, or show what
    the framework lacks for it.
  - (c) Map each statement of 003–035 to Milnor 1968 and to SGA 7 I and XIII–XV: what is there, what is not, and the
    dates.
  - (d) The comparisons of SA20-19 with the research-run rows: done in wave 2 by reader 122_125. No row is advanced, and
    three rest on another author's typescript. R20-122_125-1 merges here.
- **Why:**
  - The pages are a dated (1968 or later) primary source for the topological model behind SGA 7.
  - The research-run rows already touch them (SA20-19).
- **Rests on:** SA20-18, SA20-19; 122/003–035; H20-7.
- **Strongest known reduction:** the six-term sequence of 032 and the vanishing of H^i(M) outside 0, n−1, n (re-derived
  tonight).
- **Material:**
  - MPL_122, with notes and doubts, and the scan images;
  - Milnor, Singular points of complex hypersurfaces (1968);
  - SGA 7 I and XIII–XV as LaTeX from our port.

## Cotes 152 and 120 (reader 152_120: ac69efa38b3a951d7, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max, reader 152_120, horizontal sweep 3, 19 Nov 2026. Concepts only; no prompt is written.

## R20-152_120-1. The combinatorics of cote 152

- **Question:**
  - What is a "type de mot", and what are its morphisms?
  - Is the equivalence of 152/003 true, and in which reading ("isotypique" or "isotopique")?
  - What did the rule of 152/004 intend?
  - How do 152/010-013 compare with the classical theory of maps and unicellular gluings, and with the cartes of the Esquisse?
- **Why:** the folder is a dated (after 19 May 1982) combinatorial study of plane trees and maps just before the Esquisse. Its claims are partly undefined (H20-152_120-1, -2, -3).
- **Rests on:** SA20-7; 152/002-013; the second-pass files of block 152-001-120-006.
- **Strongest known reduction:**
  - the tree criterion and the dictionary are re-derived;
  - the recursion is analysed (both readings);
  - the source category of 003 is undefined.
- **Material:**
  - the 13 scans and corrected transcriptions of cote 152;
  - Michel Hua's 152 text;
  - the Esquisse and the cote-119 dossier;
  - any sheets on words in cotes 150-151 and 154;
  - Walsh-Lehman (1972) and Stanley EC2, ch. 6, from open sources.

## R20-152_120-2. The axioms of cote 120 as a categorical theory

- **Question:**
  - Prove or refute the reconstruction of 120/008 (and the converse of 018): M_* ⟷ (E, R, |·|) with E finitely complete, |·| faithful, conservative, transportable and left exact, and every object embedding in some Rⁿ.
  - Is M1 (images under coordinate projections) a consequence, or must it be added as "E regular and |·| preserves images"?
  - Find a class closed under unique but not general existential quantification, or prove that none exists in this setting.
- **Why:** it is his intended characterisation of tame structures by their categories (H20-152_120-4). The answer fixes what an "espace modéré" category is.
- **Rests on:** 120/003-008, 018; SA20-12.
- **Strongest known reduction:** the forward direction, and M2-M4 from finite limits, are re-derived; M1 is open.
- **Material:**
  - 120/003-008 and 018, corrected transcriptions;
  - regular categories (Johnstone, Elephant A1.3, from memory);
  - van den Dries, Tame topology and o-minimal structures (1998), on definable sets as a category.

## R20-152_120-3. Cote 120 against o-minimality, with the 121 reader

- **Question:** which of M0-M11, with a one-dimensional finiteness axiom, give exactly the compact definable sets of an o-minimal expansion?
  - The roles of M6 and M7 under M11 (H20-152_120-5).
  - The reading of the 020 margin (H20-152_120-6).
  - The generic triviality of 025 (Hardt) and its diagram version (H20-152_120-7).
- **Why:** this is SA20-10 and SA20-11. The 121 reader holds the prompted questions, so this package is to be merged with theirs.
- **Rests on:** SA20-12; the axiom list of the full working, part B3.
- **Strongest known reduction:**
  - the first pass's all-compact (Cantor) model shows finiteness is not implied;
  - the zero-set reduction of M6 is re-derived.
- **Material:** cotes 120 and 121; van den Dries (1998); Hardt (1980); Coste, An introduction to o-minimal geometry; the first pass's Q3/Q4 notes.

## Cote 119, scans 144-161 and 276-281 (reader 119_144-161_276-281: acf08879, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max, reader 119_144-161_276-281, horizontal sweep 3, 18-19 Nov 2026. Concepts only; no
prompt is written. Ids R20-119_144-161_276-281-n.

### R20-119_144-161_276-281-1. The Additif in o-minimal topology: collars, cones, the cascade, tubular neighbourhoods, the canonical filtration

**Question.** In a fixed o-minimal structure (semialgebraic first), with ∞-isotopic categories taken as simplicial
categories of definable homeomorphisms:
- (a) Define "bordant" and prove or refute I a). Compute the definable concordance space of a closed PL manifold and its
  comparison with the PL and TOP ones. Decide whether the space of strict rigidified collars is contractible, and so
  settle I b) and I c) as written and in the fibrewise form.
- (b) Prove II b) (II a) and II c) are known).
- (c) Prove the cascade of 150 with the corrected collar notion: PB ≃ PBCR ≃ EPCR ≃ EP, together with the 2-cells α and
  β and the variants (multipairs, multipointed spaces).
- (d) For tubular neighbourhoods (151–152):
  - the existence and essential uniqueness of Y-admissible rigidifications;
  - whether the condition dim φ⁻¹(y) = c(y) − 1 can always be met and gives uniqueness;
  - the 1° equivalence for equisingular pairs.
- (e) The canonical coarsest regular equidimensional filtration of a tame space (153): existence, and its dévissage
  invariants.

**Why it matters:**
- These six pages are his own formulation, about 1984–86, of a theory that came later: the unzipping of stratified spaces
  and exit-path ∞-categories.
- They tie the Esquisse's "topologie modérée" to cotes 120–121.
- This run found one part false as written (I c)) and several parts true. A run can turn the page into theorems.

**Rests on:**
- SA20-3 and SA20-4, with this run's readings (148: X∖(C∖Ċ); 150: 11 functors; 151: X∖(V∖V̇));
- SA20-12 to SA20-15 (cotes 120–121).

**Strongest known reduction (this run):**
- II c) is proved (the Alexander trick).
- α and β are isomorphisms given collars.
- 151 b) holds, and the construction from f holds below the first bifurcation value.
- The correction plus → moins is necessary.
- I c) fails for closed B with nontrivial π₀ of the concordance space (from memory: Hatcher–Wagoner;
  Burghelea–Lashof–Rothenberg). The forgetful functors PBCR → PBC → PB therefore cannot both be equivalences for such B.

**Material:**
- the Pro transcription, notes and doubts of MPL_119_144-161+119_276-281, the scans 148–153, and this run's
  `119_144-161_276-281.md` §2–3;
- van den Dries, Tame topology and o-minimal structures (1998);
- Coste, An introduction to o-minimal geometry;
- Shiota, Geometry of subanalytic and semialgebraic sets (1997);
- Hatcher–Wagoner, Astérisque 6 (Numdam);
- Ayala–Francis–Tanaka (arXiv 1409.0501);
- Lurie, Higher Algebra, Appendix A;
- Quinn (1988); Hughes (teardrops); King (1985);
- the readings of cotes 120–121 (sweep 3).

### R20-119_144-161_276-281-2. "Géométrie des ensembles finis de cardinal ≤ 6": the Digressions as a finished chapter

**Question.** Write out and prove the chapter his two plans describe (155, 160–161):
- orientations and the contracted product;
- squares and hypercubes;
- the exceptional isomorphisms for 2 to 6 elements;
- the duality S ↔ S* with its dictionary A)–C) and A′)–C′);
- the square torsors (with ω(Q) the orientation of the square);
- the affine plane over 𝔽₃, the triality of the three G_α ≅ S₆ and the bi-ditriades;
- the "trois perspectives" of the skew icosahedron and α(F) ∈ ω(S);
- the hexagram duality "par bihexagones";
- the undefined twist "ε ∧ Q" (Q* ≃ ε ∧ Q, Q* = ε ∧ Q^∨);
- the "réalisations géométriques" his last line asks for.

Also identify "Réflexions t. 4" and the typescript of 158.

**Why it matters:**
- A coherent, checkable piece of his late mathematics (about 1986).
- Every statement checked in this run is right or right after one slip.
- The triality of 156 may be a presentation not found elsewhere (H20-119_144-161_276-281-1).

**Rests on:**
- SA20-5;
- this run's computations (`119_144-161_276-281_checks_fin.py`, `_checks_pgl5.py`, `_checks_out.txt`);
- the Pro notes N36–N58 and N78–N79.

**Strongest known reduction (this run):** computed and checked:
- the dictionary, Ic(S) ≅ S* × ω(S), and the canonical bijection S∖{s} ≅ S*∖{s′};
- A′–C′, the torsor relations, and the three G_α with index 10;
- III.5 and its non-splitting;
- IV.1–IV.2, and 159.

Open: the perspectives, the hexagrams, the twist ε ∧ Q, and the geometric realizations.

**Material:**
- the transcription and scans 155–161 (with 158);
- this run's scripts;
- Howard–Millson–Snowden–Vakil (arXiv:0710.5916);
- Cameron's notes on S₆ and M₁₂;
- Conway's and Coxeter's accounts of the outer automorphism (from memory, to be fetched from open sources);
- the text of Récoltes et Semailles, for "Réflexions" (if in our corpus).

### R20-119_144-161_276-281-3. The quotient topos of a foliation: the theorem C ≃ C′ of 146

**Question.**
- (a) State "Th" precisely:
  - "multiplicité topologique" as an étendue, or a topological stack;
  - the 1- and 2-morphisms of C′;
  - the conditions on R.
  Then prove it or refute it, with the monodromy quotient (145).
- (b) Is Hom(ξ, η) discrete, and by which descent argument?
- (c) The version over a topos ("[ou topos ?]").
- (d) The C^r and analytic variants, and his "Quelles propriétés obtient-on avec des feuilletages ???": which
  multiplicities are quotients of foliated manifolds.

**Why it matters:** a dated (March 1986) statement of his on the topos-theoretic leaf space. Comparing it with SGA 4 IV
9.8.3 (1972) and Kock–Moerdijk (1992, 1996) fixes what was known, and when.

**Rests on:** SA20-2, with this run's reading of the third condition ("et connexes") and the monodromy re-derivation.

**Strongest known reduction:**
- the model case (suspensions) re-derived;
- the discreteness sketched through effective descent;
- the round-trip caveat (Kock–Moerdijk 1992, Remark 6.5, per Pro N77).

**Material:**
- the scans and transcription of 145–146;
- SGA 4 IV (LaTeX from our port, `sga4_port_20261112`);
- Kock–Moerdijk 1992 (author-hosted) and 1996;
- Joyal–Tierney, Memoirs AMS 309 (1984);
- Haefliger, Astérisque 116 (1984);
- Moerdijk's papers on classifying toposes of foliations.

## Cote 121, scans 49-73, cotes 153 and 155 (reader 121_049-073_153_155: aff4deb18a6ec3192, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max (agent aff4deb18a6ec3192), 18 Nov 2026. Concepts only; no prompt is written.

### Cote 121, scans 49-73 (SA20-15)

**R20-121_049-073_153_155-1. A reconstruction theorem for the compact-model axioms of 121/054-073 and 120.**
- **Question:** state and prove (or refute) that the axiom system of 121/065, completed by M′4 (058, with I = [−1, 1]) and
  the triangulation axiom c) with relative extension, is equivalent to an o-minimal expansion of a real closed field
  (through its compact definable subsets of the cubes); decide which of the weaker systems of 054-058, 059-063 and 070-073
  (with intersections added) determine anything o-minimal.
- **Why:** it answers SA20-10 for these drafts with a theorem instead of a comparison, and fixes what "topologie
  modérée" means on these pages.
- **Rests on:** SA20-15 (this reading, §1.2-1.5), SA20-12 (cote 120), the corrections on 056, 058 and 070.
- **Strongest known reduction:** c) gives finiteness in dimension one for compact members (TC08); the all-compact model
  shows nothing short of c) does (TC06); the converse direction is the o-minimal triangulation theorem (from memory).
- **Material:** the transcription, notes and doubts of MPL_121_049-073+153+155; the 120 package (MPL_152+120 with its
  second pass); van den Dries, Tame topology and o-minimal structures (1998); van den Dries and Miller, Geometric
  categories and o-minimal structures (Duke 1996); Shiota, Geometry of subanalytic and semialgebraic sets (1997);
  Schürmann 2002 (cited in the Pro notes TC14).

**R20-121_049-073_153_155-2. The canonical admissible partition of 121/049-052.**
- **Question:** prove the claim of 049 (a coarsest strictly admissible partition adapted to a locally finite closed
  family, commuting with restriction to opens) in each of the named contexts, with "strict" made precise (connected,
  non-singular, equisingular leaves; condition (C) of 051); or give the context where it fails.
- **Why:** it is his opening claim, unfinished on the page, and the base of the incidence-order apparatus that the
  stratified topos (151) and the figures of 156-4 use.
- **Rests on:** 121/049-052, with the corrected first stage X − ∪ Fr(T_α) and the closed-leaf presentation (both
  re-derived here).
- **Strongest known reduction:** the first stage is forced (re-derived); the order is detected locally (050); closed
  leaves are equivalent data (052).
- **Material:** the transcription and notes; the stratification chapters of van den Dries (1998) and of Shiota (1997);
  Teissier's canonical Whitney stratifications (from memory); SA10 (151) and SA21 (156-4) study files.

### Cotes 153 and 155 (SA20-16, SA20-17)

Numbering: -1 to -50 are kept for cote 121, -51 on for cotes 153 and 155.

**R20-121_049-073_153_155-51. Analysers against plethories.**
- **Question:** (a) which analysers satisfying 1)-3) of 153/006 are plethories, and what structure must be added;
  (b) construct the divided-power analyser of 153/010 and its domain of action; (c) for k₀ ⊂ K₀, decide when
  Ω = {F ∈ K₀[T] : F(k₀) ⊂ k₀} carries well-determined coaddition and comultiplication (153/004), beyond the domain
  case re-derived here; (d) when is Ω → App(Ω₀, Ω₀) injective (153/008)?
- **Why:** these are his own open points (002 e)-f), 004, 008), and the pages may be an early, independent formulation
  of plethories.
- **Rests on:** SA20-16 (this reading, §2); Pro notes A01-A26.
- **Strongest known reduction:** the binomial case is complete (computation and Newton interpolation, this reading); the
  free/domain case of 004 is re-derived; A26 bounds the broadened case.
- **Material:** the transcription and notes of 153; Borger and Wieland, Plethystic algebra (2005); Tall and Wraith
  (1970); Elliott on integer-valued polynomials and plethories (2006, 2010; cited in A12); Roby (1963, 1965); Cahen and
  Chabert, Integer-valued polynomials (1997).

**R20-121_049-073_153_155-52. Cote 155 against Deligne (1990) and the bialgebroid literature.**
- **Question:** state and prove the equivalence of 155/002 (an abelian k-linear ⊗-category with an exact faithful
  ⊗-functor to Modf(k′) ⟺ a commutative augmented k′-algebra U whose dual pro-ring is a ×_{k′}-bialgebra), with the
  identification J̃/J = A ×_{k′} A; finish 006-010 (evaluation, coevaluation, the antipode a); and set his question on
  004 against Deligne 1990 (§§1.9-1.12) and Deligne-Milne 1982 (3.10-3.11).
- **Why:** it would place a dated 1984 formulation in the history of non-neutral Tannakian duality between Saavedra
  (1972) and Deligne (1990), and SA22-0's "travail Saavedra en train" shows the subject was his.
- **Rests on:** SA20-17 (this reading, §3); Pro notes T01-T25.
- **Strongest known reduction:** the idealizer identification and the computations of 004, 006, 008 (re-derived here);
  the example Modf(k) works for every finite k′/k (T06).
- **Material:** the transcription and notes of 155; Deligne, Catégories tannakiennes (1990); Deligne and Milne (1982,
  corrected 2012); Saavedra Rivano (LNM 265, 1972); Takeuchi (1977); Hai (2008) and Schauenburg (2017), cited in T23.

## Cote 121, scans 1-48 (reader 121_001-048: a9e0641820ca2be57, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max, reader 121_001-048, horizontal sweep 3, 19 Nov 2026. Concepts only; no prompt is written.
Full working: `121_001-048.md`. The 152_120 reader asked for its R20-152_120-3 to be merged with the 121 reader's
package on o-minimality: R20-121_001-048-1 is that merge, with R20-121_049-073_153_155-1.

**R20-121_001-048-1. His tame-topology axioms against o-minimality: one space, all arities, open cores, regular
partitions.**
- **Question:**
  - (a) Characterize the one-space families F (121/004-024, a)-f), with or without e_n) that arise as the definable
    subsets of a definable set in an o-minimal structure. Give the extra data needed: charts, projections, a definable
    order. Pillay's Remark 1.10 (Pro notes Q3.9) is a model.
  - (b) Prove or refute that cote 120's M0-M11, completed by f) for M_1 ("every moderate part of R is a finite union of
    points and intervals"), characterize the compact definable sets of structures with o-minimal open core. Decide when
    the Boolean-projection closure is o-minimal: the theorem-of-the-complement question.
  - (c) The same for the compact systems of 121/054-073, with the corrections of the 121_049-073 reader (intersections
    as an axiom; I = [-1, 1]).
  - (d) Close the gap of 018: does a coarsest F-regular partition exist for regularity = smooth points of semialgebraic
    sets, with (S) for all closed saturated unions?
- **Why:** it is SA20-10 with a theorem instead of a comparison. It also explains why his two drafts each hold half of
  o-minimality (H20-121_001-048-1).
- **Rests on:** SA20-12, SA20-13, SA20-15; the full working, A.2-A.6 and C.3; R20-152_120-3; R20-121_049-073_153_155-1.
- **Strongest known reduction:**
  - a)-f) are re-derived for o-minimal definable sets (Pro Q3.3) and for Noetherian constructible sets (this run).
  - O-minimality = the projection-closed Boolean structure + f) on the line (checked).
  - The compact axioms cannot see beyond the open core (checked).
  - The all-compact model shows that finiteness must be an axiom.
- **Material:**
  - the transcriptions and notes of MPL_121_001-048, MPL_152+120 (with the second pass) and MPL_121_049-073+153+155;
  - van den Dries, Tame topology and o-minimal structures (1998), chs. 1-4, 8;
  - van den Dries and Miller, Duke 84 (1996);
  - van den Dries, Dense pairs of o-minimal structures (Fund. Math. 1998);
  - Miller and Speissegger, Expansions of the real line by open sets (Fund. Math. 1999);
  - Dolich, Miller and Steinhorn, Structures having o-minimal open core (Trans. AMS 2010);
  - Pillay 1988 (Remark 1.10);
  - EGA 0_III §9 and EGA IV §1.8;
  - Teissier's canonical Whitney stratification.
  - The locators of the last four lines are from memory.

**R20-121_001-048-2. Mobility and the canonical partitions of spaces and proper maps (121/026-037).**
- **Question:**
  - (a) Prove Props A-D of 026-028 in the PL category, or find them in the literature on intrinsic stratifications.
  - (b) Settle A, and B's uniqueness bracket, in TOP (B's first sentence follows from A in any context). Given D's
    failure, is the intrinsic topological filtration still made of manifolds along which X is equisingular? Is the
    transverse germ of B unique in TOP?
  - (c) Prove Conjecture 1 in the PL and the definable contexts: the intrinsic stratification is privileged and coarsest.
  - (d) For Conjecture 2, take first one proper definable map f: X -> Y. Prove or refute:
    - that the largest open set over which f is non-singular and locally trivial is definable, and its complement rare;
    - that the recursion of 036-037 (with finitely many marked closed sets) produces a coarsest privileged partition of
      the map.
  - (e) Decide whether these canonical partitions agree across the piecewise contexts (Shiota).
- **Why:** these are his two conjectures. They are the canonical stratification the Esquisse's tame topology needs, and
  they decide SA20-11 for these questions.
- **Rests on:** SA20-14 (full working B.1-B.3), with the counterexamples in TOP (double suspension, Bing) and the
  re-derived Remarque on proper maps.
- **Strongest known reduction:**
  - D's "<=" (proved); B's first sentence from A by D's "<=", in every context (proved); B's uniqueness bracket open.
  - The image of a leaf under a proper arrow, and local triviality over the target leaf (proved).
  - The fibre-manifold sentence in PL (proved).
  - Rarity of the non-trivial locus by Hardt's theorem (from memory).
- **Material:**
  - the transcription of 026-037 and this working;
  - Armstrong, Annals 86 (1967);
  - Akin, Trans. AMS 143 (1969);
  - Siebenmann, Comment. Math. Helv. 47 (1972);
  - King, Topology Appl. 20 (1985);
  - Hardt, Amer. J. Math. 102 (1980);
  - Coste, An introduction to o-minimal geometry;
  - Shiota, Invent. Math. 196 (2014), and arXiv:1002.1508 and 1310.5489 (as cited in the Pro notes);
  - Cannon, Annals 110 (1979) for the double suspension.
  - The locators are from memory except Shiota's.

**R20-121_001-048-3. Gluing and reconstruction: 121/039-047 against the literature on stratified spaces and against the
remords.**
- **Question:**
  - (a) Write out the recollement of 039 with all six functors, completing q^! and adding i'^!, and the four-operation
    agenda for the X_{I,J} with the dualizing complex.
  - (b) State and prove the reconstruction theorem behind 041-047 for n strata: a stratified space with control data ↔ a
    system of manifolds with fibred boundaries and compatible corners, up to homeomorphism. Compare with Verona's
    abstract stratified sets and with iterated fibration structures.
  - (c) Decide what 043's groupoid data determine:
    - in dimension 2, the homotopy type, through the homotopy colimit of classifying spaces (H20-121_001-048-5);
    - in general, where 1-groupoids fail and higher data (Treumann's exit 2-category; exit-path ∞-categories) are
      needed.
  - (d) Place the result against the remords of 147/179-180 and his answer on 151/039-044, which were not read here.
> [19 Nov 2026, sweep 3.5] Bears on line 391: SA10 intake 1. The main question (A.1): what glue l.55 (SA10 intake, refuted; PROPAGATION.tsv n=1); SA10 intake 2. Item by item l.78 (SA10 intake, refuted; PROPAGATION.tsv n=2); INT-SA10-E24 (SA10 intake, confirmed; PROPAGATION.tsv n=52). See results_register/horizontal/sweep3_5/SUMMARY.md.
- **Why:** it answers SA20-9 with mathematics instead of dates. It ties cote 121 to the stratified-topos and maquette
  material (SA10, SA31) and to the Esquisse's programme (SA20-3, -4).
- **Rests on:** SA20-14 (full working B.4, B.5), C.2; the Pro notes Q2.5-Q2.8.
- **Strongest known reduction:**
  - The adjunctions of 039 (checked).
  - The dimension bookkeeping and the gluings of 041-047 (checked).
  - The marked-sphere computation in both gluing rules (checked).
- **Material:**
  - the transcription of 039-047 with the TikZ figures and the scans;
  - SGA 4 IV 9.5;
  - Beilinson-Bernstein-Deligne 1.4;
  - MacPherson-Vilonen, Invent. Math. 84 (1986);
  - Mather, Notes on topological stability (1970);
  - Verona, LNM 1102 (1984);
  - Albin-Leichtnam-Mazzeo-Piazza, Ann. Sci. ENS (2012);
  - Treumann, Compositio 145 (2009);
  - Lurie, Higher Algebra, appendix A;
  - the 147 and 151 packages.
  - Locators from memory, except Treumann's (checked by the Pro notes).

## Cote 122 against the research runs, and cote 125 (reader 122_125: a8afd9e2a259051c4, Claude Opus 5.5 at effort max)

By Claude Opus 5.5 at effort max, reader 122_125, horizontal sweep 3, 19 Nov 2026. No prompt is written.

### R20-122_125-1. Cote 122: the variation in his equivariant triangle (to merge into R20-3)

- **Question:**
  - (a) Prove that, in D(Λ[π]) with π acting trivially on L = RΓ(W₀), T − 1 on K = RΓ(M) factors uniquely as u∘V with
    V: K → K^∨[−2n]. Identify V with the variation map.
  - (b) Settle the sign of 122/022 ("ρ et ρ′ sont transposés (signe ?)") through the relation between u and the Seifert
    form S = Var^{−1}.
  - (c) Extend to the étale setting with π the tame inertia, with the twists placed as in the working, Part 1, item 8:
    u: K^∨(−n)[−2n] → K.
- **Why:**
  - It turns his three open marks into one statement: "(signe ?)", "[expliquer comment ?]" (024) and "vérifier la
    commutation de RΓ^π à RHom" (024).
  - It identifies the "données nouvelles" of 024 with the classical invariants of an isolated hypersurface singularity.
- **Rests on:** SA20-18; 122/020–026; H20-7; H20-122_125-1; the Pro notes RN020–RN023 (GPT-6 Astra, ChatGPT Pro mode).
- **Strongest known reduction on the pages:**
  - the triangle (a′) in D(Λ[π]) with L trivial;
  - its RΓ^π, the triangle (b′), with the shift −2n−1, which is re-derived (working, Part 1, item 8).
- **Material:**
  - MPL_122 with notes and doubts, and the scans 020–026;
  - SGA 7 XIII–XV (our port, sga7_port_20261109);
  - Milnor 1968;
  - Lamotke, Topology 14 (1975), and Arnold–Gusein-Zade–Varchenko II, ch. 2 (from memory; check the open copies).
- **Note:** R20-3 (d), "make the comparisons of SA20-19", is done by this reading. R20-3 can drop it and take (a)–(c)
  above.

### R20-122_125-2. Cote 125 and SGA 2 XII–XIII: what of the duality criterion is in print, in which generality

- **Question:**
  - (a) Write the chain of 125/003 as a theorem with its hypotheses: X projective Cohen–Macaulay of dimension r, Y
    closed, 0 < m < r. Prove every equivalence, including the injectivity clause and the reduction to O(−n).
  - (b) Find, with exact locators, what is in SGA 2 XII §1–2 and XIII, in Hartshorne (1968; LNM 156, III.3.4;
    Compositio 23, 1971, Prop. 2.9), in Ogus 1973 and in Speiser 1973: which direction, for which X, with or without
    injectivity.
  - (c) Complete the induction that the frame of 125/006 sets up (H20-122_125-3).
  - (d) Identify the typescript of 125/004 and 007 (pages III-18 and III-5) among the EGA III drafts.
- **Why:**
  - The folder is a compact, undated statement of a criterion that the literature attributes in part to Hartshorne's
    papers.
  - The edition needs its hypotheses stated and its place in SGA 2 fixed.
  - (d) dates the folder.
- **Rests on:** SA20-W2; the working, Part 2, steps 1–11; H20-122_125-2 and -3; Michel Hua's project's literature notes
  for 125 (credited).
- **Strongest known reduction:** the chain is closed under X projective Cohen–Macaulay (steps 1–6). Only (b) and (d) are
  questions of record.
- **Material:**
  - K125-01 (transcription, doubts, mathnotes) and the scans 125/002–009;
  - SGA 2 as LaTeX if it can be found (arXiv math/0511279, the Documents Mathématiques re-edition; from memory). We have
    no SGA 2 port;
  - Hartshorne's papers and LNM 156 (from a library route the user allows);
  - our EGA III sources for (d).

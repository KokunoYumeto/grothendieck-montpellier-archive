## STUDY

**Cote 151, scans 1-17** (Claude Opus 5.5 at effort max; 31 check events, 14 corrections; full reading
`readings/151_001-017.md`).

**What the block is.**
- **002 is his plan of "Structures stratifiées".** Its start pages 1, 10, 16, 23 are the sheets where §1-§4 begin
  (151/027, 045, 057, 070), so it was written after sheet 23. The struck "Strat" is the heading of 057.
- **The rest is a later layer.** 003-009 are on the backs of copies of a letter dated 6 December 1990, and 009 and 018 on
  its letterhead. 018 continues both 015 and 017. So 151/003-025 dates from 1990-91, the time of *Les Dérivateurs*. It
  returns to what §1 needs, the homotopy type of a topos (151/032 "cf Artin-Mazur", the van Kampen of 151/043), and does
  not underlie it.

**003-009: π₀-systems of Čech nerves.**
- E₀, E₁, E₂ with 𝔖₂ and 𝔖₃ are the Čech nerve truncated at level 2 (Michel Hua's project).
- His relations hold in the model, except the boxed σ₃δ₁ = δ₁ of 003, which his own 005 and 007 correct to σ₁δ₁ = δ₁.
- The two "global" boxes of 005 are independent relations (models M1, M2): the 𝔖₃-invariance of δ₁δ₀, and
  p₀p₁₂σ₁ = p₀p₁₂.
- 009 is the edge-path presentation of π₁, with one relation per 𝔖₃-orbit (re-proved). Its claim that σ₁-fixed points
  are degenerate holds for tuple systems and Galois coverings, and fails for an 𝔖₃ covering of degree 3.
- E₂(α) is defined as π₀(F_α ×_F F_α).

**011-015: "Hyperrecouvrements".**
- A functor φ: A → 𝒳 from an arbitrary small A, motivated by "le yoga « Cechiste »" and its refinement "suggéré par
  Cartier".
- Re-proved: Hyp 1′ is tautological; the induction for Hyp 2; a)-c) ⟺ Hyp 1, 2, 2′; the left-exact case (Diaconescu)
  and its converse; b) ⇒ b′) and c) ⇒ c′), the latter by shortening zigzags.
- **His "forme équivalente" is false** (#g673; A = BC₂). What is true: Hyp 1, 2, 2′ ⟺ (Hyp) for finite diagrams indexed by
  finite forests. The full (Hyp) needs the parallel pair as well, and is then left exactness (two-cone argument; Shulman
  2012).
- So his closing question has the answer no, and "I = •" should be ∅.
- The gap matters: the symmetric nerve of a group satisfies Hyp 1, 2, 2′ and realizes to BG. These hypotheses do not
  give descent, and (Hyp) gives only flat systems.

**017: the finite sets 𝔼_n with δ_n, K_n and 𝔖_n.**
- The margin defines δ_nK_n as the projection p_{n+1}: idempotent, not the circular ρ_{n+1}.
- (**) is exactly Hyp 2 for A = (finite sets)^op, the product being given by the coproduct injections α, β. So 017 is
  the punctual case of 011-015.
- Its flat systems are the tuple systems S^n.
- (*) is not a complete presentation: it omits 005's two global relations (counter-model).
- The index of ρ clashes on the page.

**Connections:** H2, SA10-8, Les Dérivateurs, Artin-Mazur, SGA 4 V §7.

## HUNCHES

**H151a-1. 151/003-025 is a 1990-91 return to the homotopy type of a topos** (sharpens H2).
- Grounds: the paper of 6 Dec 1990 on 003-009 and 018; the continuity 015 → 018 ← 017; the subject, A-indexed
  hypercoverings and π₀-systems, which is Artin-Mazur's route to the homotopy type that 151/032 and 151/043 presuppose.
- His indexing by an arbitrary small category is the habit of *Les Dérivateurs* (1990-91), whose text should be searched
  for "hyperrecouvrement" and for these conditions.
- Confidence medium on the link to Les Dérivateurs, high on the date.

**H151a-2. He indexes by finite sets, not by Δ, because Čech nerves are symmetric, and over finite sets they are flat.**
- [n] ↦ U^n is a flat functor on (finite sets)^op, since equalizers of tuples are tuples on a quotient set. Over Δ^op it
  is not: (a,b,a) has equal ends without being constant.
- So the symmetric indexing is the one where the Čech nerve satisfies even the full (Hyp). What carries homotopy is its
  π₀ (003-009).
- Confidence medium.

**H151a-3. The right A-indexed hypercovering lies strictly between Hyp 1, 2, 2′ and flatness, and is cut out by
conditions on cycles** (sharpens H2; first pass C06-C07).
- Hyp 1, 2, 2′ control exactly the tree-shaped finite diagrams. They admit the symmetric nerve of a group, realizing
  to BG, as a hypercovering of the point.
- Flatness admits only the tuple systems.
- Verdier's coskeletal conditions (fill every simplex boundary) are conditions on cycles. Their A-indexed form should be:
  epi comparison for the boundaries of the representables.
- Confidence medium.

**H151a-4. 017 is the classifying-topos case.**
- Presheaves on (nonempty finite sets)^op, the opposite of the index category of his 𝔼_n, classify inhabited objects.
  So a flat E* on it is an inhabited set, and in a topos an inhabited object.
- His (E*_n) systems with (**) are the "covering" relaxations of points of that classifying topos.
- Confidence medium (the classifying-topos locator is to be checked).

## PACKAGES

**P151a-1. A-indexed hypercoverings: the condition between covering and flatness.**
- **Question:**
  - for φ: A → 𝒳 with A small, which conditions on the comparison maps φ_!(lim F_i) → lim φ_!(F_i) make the homotopy
    colimit of the U_α model the homotopy type of 𝒳, in the sense of Artin-Mazur?
  - how do they compare with Verdier's coskeletal hypercoverings (A = Δ^op) and with the symmetric case A = (finite
    sets)^op?
- **Why it matters:** it is the definition his 1981 van Kampen principle (151/043, H2) and his 1990 layer both need, and
  it would turn SA10-8 into a descent statement.
- **It rests on:** 151/011-018; 151/032, 043; Verdier, SGA 4 V §7; Artin-Mazur, *Etale Homotopy* (LNM 100, 1969);
  Dugger-Hollander-Isaksen, "Hypercovers and simplicial presheaves", Math. Proc. Cambridge Philos. Soc. 136 (2004), 9-51
  (locators to be checked); Shulman 2012.
- **Strongest known reduction:**
  - Hyp 1, 2, 2′ ⟺ epi comparisons for forest-shaped finite diagrams;
  - (Hyp) for all finite diagrams ⟺ φ flat ⟺ φ_! left exact;
  - the symmetric nerve of G separates the two (R151a-20 to 24).
- **Material:** the corrected transcription of 151/011-020 and this reading.

**P151a-2. His presentation of the finite sets.**
- **Question:** do (a)-(d) of 017, with the two global relations of 005 in general form, present the category of
  nonempty finite sets? Does the low-degree list of 003-005 present its truncation at three elements?
- **Method:** by comparison with Grandis, Theory Appl. Categ. 8 (2001) (locator to be checked), or by a coset
  enumeration of the presented category for n ≤ 4.
- **Why it matters:** if they do not, his "systèmes satisfaisant (*)" are a larger class than the symmetric simplicial
  sets, and the punctual hypercoverings of 017 are defined on the wrong category.
- **It rests on:** 151/003-009, 017, 019-020.
- **Strongest known reduction:** (a)-(d) are incomplete (R151a-26, 27). The two missing relation types are exactly 005's
  boxes, which are independent of the rest (R151a-07).
- **Material:** this reading and its scripts (`check151a.py`, `check151a_models.py`, in the reader's scratchpad; to be
  re-run from the description in the check events).

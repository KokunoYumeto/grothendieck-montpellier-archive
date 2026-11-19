# SA10, Espaces stratifiés (cotes 150, 151, 152, 120): the study

**Who:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 3, 18 Nov 2026.

**The brief:** the coordinator's message of 18 Nov, about 22:2x UTC (sweep 3). Read every transcribed page, work through the mathematics, re-derive the steps that carry it, close the dependencies, and write down the hunches, the research packages and the deliverables.

## What was read, and how

**Read in full tonight:** cote 151, scans 32-75 (package MPL_151_032-075).
- The source is the frozen Pro transcription, cleaned to `sweep3/_tools_a6d42bf6/c151b.txt`.
- One reading was checked on the scan image, 151/070.
- This is SA10-16 and SA10-17, the stratified topos of 1981: the end of §1, and §2-§3 with the beginning of the next §2.

**Not read tonight, so the sweep-2 map (`sweep2/SA10/WHAT_IS_WHERE.md`) and the second pass of 17 Nov stand for them:**
- cote 150, scans 1-99 (SA10-6, 7, 10, 12, 13, 14);
- cote 151, scans 1-31 (SA10-15);
- cote 152 (SA10-18). By the split of 18 Nov, the plane trees are read by ae4ae3dc17acaa440 (SA20-7).
- cote 120 (SA10-19). By the same split, the tame axioms of 120-121 are mine; I did not reach them.

**Checks:** each re-derivation is one row of CHECK_EVENTS.tsv (SA10-C3-nn). Corrections are in CORRECTIONS.tsv (SA10-S3-Kn).

## 1. The two-stratum case and the homotopy type (151/32-44, the end of §1)

**The setting:** a closed Y ⊂ X, with V_{Y,X} the tubular neighbourhood, taken as a germ, and V*_{Y,X} = V_{Y,X} ∖ Y.

**Homotopical normal local triviality (151/32, (11)):**
- V*_{Y,X} → V_{Y,X} ≃ Y should be a homotopy fibration whose fibre is the local link V*_{z,Z}.
- He proposes this as the *definition* of normal local triviality in a topos-theoretic setting, for example schemes with the étale topology.
- There the homotopy types should be profinite and localized away from the residue characteristics ("cf Artin-Mazur").

**The exact sequences (12)-(13) and the inertia-decomposition diagram (14), 151/33-34:**
- Suppose the link is connected and π₂(Y) → π₁(V*_{z,Z}) is zero.
- Then 1 → I = π₁(V*_{z,Z}) → D = π₁(V*_{Y,X}) → π₁(Y) → 1 is exact, and D maps to π₁(X*).
- (15): if Y and the link are K(π,1), so is V*_{Y,X}.
- I re-derived both from the long exact sequence (SA10-C3-04). The K(π,1) property of X* is not needed for (15).

**The category 𝓕 (151/35-36, (16)-(18 bis)).** 𝓕 is the category of sheaves locally constant on both strata. It is equivalent to the systems (E_{X*}, E_{Y,X}; φ) with φ: p*E_{Y,X} → i*E_{X*} on Π₁V*_{Y,X}. Equivalently, φ is a map of π₁(Y)-sets E_{Y,X} → E_{X*}^I.

**Two examples (151/36-40):**
- **X = ℂ, Y = {0}.** 𝓕 ≃ Ĉ, where C has objects a and b, Aut(a) = D ≅ ℤ, and one arrow a → b, so b is final. 𝓕 is therefore contractible, like ℂ. Checked (SA10-C3-05).
- **X = ℙ¹ ≃ S², Y = {∞}.** 𝓕 is again contractible, while S² is not. So X → 𝓕 is not a homotopy equivalence (24), although the pieces are K(π,1). Checked (SA10-C3-06).

**The resolution by gerbes (151/41-43):**
- A-gerbes glue along V*_{Y,X}.
- On a K(π,1), an A-gerbe is an extension of π by A.
- For S², the datum is an automorphism of the trivial extension of ℤ by A, so an element of Hom(ℤ, A) = A. That gives H²(S², A) ≅ A (25), "magnifique succès !". I re-derived it (SA10-C3-07).
- He concludes that there is a van Kampen theorem for colimits of topoi: "le type d'homotopie d'une Lim→ de Topos (Topos 'recollé') est la Lim→ des types d'homotopie". He judges it "relativement triviale, et justiciable sans doute de techniques bisimpliciales des plus standart".

**The programme (151/44).** The homotopy type of stratified spaces whose pieces are K(π,1) should be expressible by a finite inductive system of the fundamental groupoids of the pieces. His examples are the Teichmüller moduli spaces, their compactifications, and the tubular neighbourhoods of their canonical stratifications.

**What this is today:**
- 𝓕 is the 1-truncated exit-path category of the stratification.
- The gerbe computation is its 2-truncated level, the exit-path 2-category of constructible stacks (D. Treumann, "Exit paths and constructible stacks", Compositio Math. 145 (2009), 1504-1532).
- The full statement is the exit-path ∞-category (J. Lurie, *Higher Algebra*, Appendix A.6 and A.9; locators to be checked). This is SA10-8.

## 2. Global stratifications: the half-simplicial formalism without tubes (151/45-56, §2)

**The setting (151/45-52):**
- a family (X_i)_{i∈I} of closed subsets, I ordered;
- (1′ a) locally finite; (1′ b) i ≤ j ⇒ X_i ⊂ X_j; (21 c) X = ⋃X_i; (21 d) X_i ∩ X_j = ⋃_{k≤i, k≤j} X_k.

**The constructions:**
- X_{Δ0} = ∐X_i → X is finite, that is proper with finite fibres, and a local immersion.
- X_{Δ1} = ∐_{i≤j} Γ_{ij}: a is an étale covering, constant on X_i with fibre I_{≥i}, and b is a local immersion.
- The X_{Δr} form the half-simplicial space of flags.

**His remarks:**
- I can be replaced by a category.
- I → P(X) need not be injective.
- One may keep only the non-degenerate flags.

**Proposition (151/52, (22)).** Under a)-d), lim→ X_{Δ*} → X is a homeomorphism. I re-derived it (SA10-C3-03):
- by (d), I_x is connected under ≤;
- by (c), the map is surjective;
- X_{Δ0} → X is closed and surjective, so it is a quotient map.

The Corollary of 151/52-53 ("sauf erreur", I finite with infs) was not checked.

**Question (151/54, (24)).** Should (d) be strengthened to "Inf(i, j) exists and X_{i∧j} = X_i ∩ X_j"? He answers no. His example is the cone over a circle stratified by two arcs A, B and two points, with A ∩ B = {a} ∪ {b}: two connected strata with a disconnected intersection.
- This is the condition he calls *polyédral* in 1986 (156-7/14: "deux éléments minorés ont un inf").
- In 1986 he again keeps the general, "spacious" case (156-7/11). See DEPENDS.

**Proposition (151/55).** The strata X_i* = X_i ∖ Ẋ_i partition X, and i(x), the least i with x ∈ X_i, is the unique i with x ∈ X_i*.
- His proof checks (SA10-C3-01).
- His margin says, "sauf erreur", that one may discard the i with X_i* = ∅. I proved that a)-d) survive (SA10-C3-02): X_k = ⋃_{l≤k, X_l*≠∅} X_l, because i(x) ≤ k for x ∈ X_k.

**(27)-(29):** Ẋ_{Δr} and X*_{Δr}. "Moralement", X*_{Δr} is the non-singular part. The X*_{Δr} do not form a half-simplicial space.

## 3. Introduction to tubes, and the gluing theorem (151/57-69, §3)

**The definitions (151/57-58):**
- V̄_{ij} is the tubular neighbourhood of X_i in X_j;
- R_i = ⋃_{X_k⊅X_i} X_k and R_{ij} = R_i ∩ X_j (3, 3 bis);
- V_{ij} = V̄_{ij} ∖ R_{ij}, "un espace infinitésimal autour de" X_i*;
- V*_{ij} = V̄_{ij} ∖ Ẋ_j = V_{ij} ∩ X_j*;
- for i = j: V_{ii} = V*_{ii} = X_i*.

**(4), R_i ∩ X_i = Ẋ_i:**
- His proof of ⊂ is right.
- The inclusion ⊃, called "triviale", needs that no k < i has X_k = X_i. That holds when X_i* ≠ ∅.
- It fails otherwise. With I = {0 < 1} and X_0 = X_1 = X, we get R_1 = ∅ while Ẋ_1 = X (SA10-C3-08, SA10-S3-K1).
- He assumes X_i* ≠ ∅ only from 151/63, and at 151/71 he says he did not want to assume it. Given (4), (6)-(8) check (SA10-C3-09).

**The stones (151/58-61):**
- The "pierres" are X_i* → V_{ij} ← V*_{ij} → X_j*.
- On 151/59 he calls them "des côtes mal taillées". They are not enough for the pieces V^{d′}_{d,d″} ≃ Ñ | D* of "(Str_∞ p. 84)", the normal-crossings pieces. They are more than needed where j is a successor of i.
- Under standard equisingularity, V*_{ij} is a bundle over X_i* with fibre an open cylinder ℝ × C_{ij}, where C_{ij} is the link, compact when j is a successor of i, and V_{ij} is a bundle of cones over C_{ij}.
- The general stones are V^j_{i,k} = V̄_{ik} ∖ (R_{ik} ∪ S_{jk}) (10)-(11), with (12)-(13).
  - (12), R_{jk} ∪ S_{jk} = Ẋ_k, and (13) check (SA10-C3-10, 11).
  - His aside "(aussi R_{j,k} ∩ S_{j,k} = Ẋ_i)" is false in general. Take ℝ² with X_m the origin, X_l the x-axis, X_j = {(0,5)} and X_{l′} the y-axis, all below X_k = ℝ². Then R ∩ S is the origin, while Ẋ_j = ∅.
  - It holds, with Ẋ_j, when k is a successor of j (SA10-S3-K2).
- 151/61: he decides to work with the X_i* and the *elementary* stones V_{ij}, V*_{ij}, j a successor of i.

**The diagram Ĩ (151/62-68):**
- Among the elementary stones, under his "cas vraisemblables", the only inclusions are the three arrow types. His argument checks (SA10-C3-12).
- Ĩ has card I + 2ν vertices and 3ν arrows, ν being the number of elementary flags (checked).
- The examples are Δ_r (20), the V and Λ shapes (21)-(22), and the version with a dimension or codimension function (23)-(27).

**"Th. de recollement des tubes (1ère version)" (151/69).** "Considérons le diagramme de type Ĩ, formé par les X_i*, V*_{i,j}, V_{i,j} (i, j ∈ I, j un successeur de i) … Alors X s'identifie au topos Lim→ de ces topos." His margin adds that X should be sober.

**The theorem is false as stated, for any I with a chain of length 2** (SA10-C3-14, SA10-S3-K3).
- **The counterexample:** X = ℂ, X_0 = {0}, X_1 = ℝ, X_2 = ℂ. The successor pairs are (0,1) and (1,2).
- **Why it fails:**
  - The category of sheaves on the colimit topos is the 2-limit of the sheaf categories of the pieces.
  - That 2-limit contains the following object:
    - {*} on X_0*;
    - {*} on both rays of X_1*;
    - {1, 2} on both half-planes;
    - on V_{12}, the generization maps sending * ↦ 1 from the positive ray and * ↦ 2 from the negative ray, into the upper half-plane.
  - No sheaf on ℂ restricts to it. A section near 0 restricts to the upper half-plane with one value, and that value must be 1 and 2 at once.
- **Where the failure lies:** the successor-pair stones never see the germ of X_2 along X_0. That corner is the one his own remark on 151/59 points at.
- **His own doubts on the page:** at 151/72 he calls the theorem's proof a local question on X, and retracts this in the margin: "un panneau dans lequel j'ai tendance à tomber, depuis le début de mes réflexions sur les croisements normaux". The sweep-2 notes record that the proof paragraph is cancelled on the page (SA10-C4).
- **The refinement:** add the stones of every pair i < k, or the V^j_{i,k}, with their inclusions. Whether X is then the colimit is open (package P1).

## 4. The canonical topoi of a global stratification (151/70-75, the next §2)

**A) General inverse images (151/70-72):**
- The axioms (1) a)-d) are restated at 151/70.
  - In d) the ink reads "⋃_{k<i,j}", with a plain <. That is his slip: for i = j it would give X_i = Ẋ_i. 151/52 and 151/57 have k ≤ i, j. The transcription reads the ink correctly (SA10-C3-15, SA10-S3-K4).
- X′_i = X_i ×_X X′, and X′_{Δr} ≅ X_{Δr} ×_X X′.
- For X′ → X a proper local immersion or an open immersion, tubes commute with inverse images ((4)-(6)). His margin: "une propriété formelle importante des tubes qu'il faut vérifier … (p.ex. X compact — brrr!)".

**B) X_{I′} for a crible I′ (151/72-75):**
- X_{I′∩I″} = X_{I′} ∩ X_{I″} by (1 d). Checked (SA10-C3-13): k ≤ i ∈ I′ and k ≤ j ∈ I″ put k in both cribles.
- The empty strata can be discarded (74).
- On U_{I′,I″} = X_{I′} ∖ X_{I″} the induced stones need not be homotopy equivalent to the old ones: "il faut mieux ne pas trop s'avancer" (75).

**C) The V^{I‴}_{I′,I″} begins at 151/75.**

## 5. What the pages establish, what is wrong, what is open

**Proved on the page and re-derived:**
- the strata partition (151/55);
- the reconstruction of X from its half-simplicial flag space (151/52);
- the inertia-decomposition sequence and K(π,1) inheritance (151/33-34);
- 𝓕 for ℂ and for S² (151/38-40);
- H²(S², A) by gerbes (151/43);
- (6)-(8), (12)-(13), the inclusions among stones, and the crible formula.

**Wrong as written, and refined by me:**
- (4) needs X_i* ≠ ∅;
- the aside in (12);
- the gluing theorem of 151/69, refuted;
- the slip in (1 d) on 151/70.

**Open on the page:**
- the gluing theorem with the right stones;
- the formal property of tubes under inverse images (151/71);
- the comparison of constructible sheaves on X_{I′} and U_{I′,I″} (151/75);
- the van Kampen theorem for topos colimits (151/43), which he calls standard.

## 6. How it connects

- **To cote 150:**
  - "Str_∞ p. 84" (151/59) is a text of his on normal-crossings pieces. It is probably cote 150, scans 44-84 (SA10-12), which is to be verified by his page numbers.
  - The research run EXIT_TOWER reads 150 folios 9 and 15-16. Its A.2 shows that the stratification of the moduli of stable curves has infima only for small (g, n). So his main example fails the strengthened condition of 151/54. That is a reason, from his own programme (151/44), to keep the general case.
- **To SA21 (cote 156):**
  - The axioms a)-d) of 151/45-52 are a frontier condition on closed strata, as are the figures of 156-4/2-3.
  - Question (24) of 151/54 is the polyhedral condition of 156-7/14.
- **To SA10-8 and Pursuing Stacks:** §1 is the 1981 form of the stratified homotopy hypothesis, with the gerbe level made explicit.
- **To La Longue Marche (1981):** 151/44 names the Teichmüller moduli spaces, their compactifications and their tubular neighbourhoods as the motivating case (H5).

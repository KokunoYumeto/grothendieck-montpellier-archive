# SA01: Géométrie et topologie combinatoire, part 1 (cotes 71, 72, 75, 81, 83, 93/92-134): sweep 3, wave 1

**Lead:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026, by sweep3/WAVE1_LEAD_BRIEF_20261119.md. Reader messages: `READER_PROMPTS.md`.

**Readers** (all Claude Opus 5.5 at effort max; method: _tools_a6d42bf6/READER_BRIEF.md):
- R1, agent a0399c97cde963d2d: cote 83 (K83-01 to -14 against Pro MPL_83_178-222) and cote 93, scans 92-134 (Pro MPL_93_092-134, the only witness) (`readings/cotes83_93-92-134*`). The first pass was a survey; the second read every line.
- R3, agent a5723c09c05df9eda: cote 72 (read in full for SA04, K72 against MPL_72_035-081 scan by scan; its rows are copied here from `sweep3/SA04/readings/cotes69-74*` under their SA04 ids) (`readings/cote72*`), and cotes 71 and 75 (J71-01 to -06, J75-01 to -04) (`readings/cotes71_75*`).
- R4, agent a774f5c4e87a59ea4: cote 81 (J81-01 to -07, the only witness; the Pro package named MPL_81_038-055+154_046-076 holds only cote 154) (`readings/cote81*`).

**Sources:**
- the Pro packages in `inputs/SA01/pro/` and `grothendieck_archive_transcription_20261110/returns/MPL_93_092-134_unzipped/`;
- the Codex-web folders K72, K83 and J71, J75, J81 in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/`;
- the scans in `grothendieck_archive_montpellier/`;
- the maps in `sweep2/SA01/WHAT_IS_WHERE.md` and `TOPIC_NOTES.md`.

**Not yet read in full** (to be read):
- cote 83: the 408 medium-confidence rows of the Pro doubts table of 83/178-222 (the 92 low-confidence rows were read), and the remarks of the K83-07, -08, -12, -13 and -14 math notes;
- cote 81: scans 1, 9 and 31 (no inventory row); the drawings, beyond 40 dpi overviews of 81/10, 12 and 54;
- cotes 71 and 75: the readings listed as not viewed at the end of `cotes71_75.md`;
- the scans that no folder transcribes, listed in each reading.

**Ink still to decide on the scans:** the corrections marked "not viewed" in CORRECTIONS.tsv. The readers viewed 72/35-36, 83/144, 178, 195, 207, 215, 221, 93/102, 114, 122, 126, and seven scans of cote 81.

**Where the questions go** (one prompt per cluster of related questions):
- cotes 72 and 75 (pinned regular realizations, the general regular icosahedron) and cote 81 (ordered models, trees, the dictionary with 154/46-76): into RESEARCH_SA04 (the arithmetic theory of regular polytopes, `TO_SEND/PRO/1_Archive_research_by_topic/18_SA04_*`);
- cote 83 (Azumaya algebras of rank 4, the ∗-product as composition of quadratic covers): into RESEARCH_SA02, with cote 84;
- 93/92-134 (projective connections, uniformization, the characteristic-p rigidity of G₀ on 93/121-124): into RESEARCH_SA03, with the rest of cote 93;
- cote 71 (Contou-Carrère's manuscript on three good vertices): no research question; its results are known (Meisters 1975; Toussaint 1991).

The items below are the readers' integration blocks, one per stretch.

<!-- reading:cote72 -->
### From the reading cote72

Cote 72 as read for SA01 by reader R3 (Claude Opus 5.5 at effort max) of a6d42bf6fe2b0d8a8, 19 Nov 2026. It was read in full in SA04's stretch: `sweep3/SA04/readings/cotes69-74.md`, section "Cote 72", with the rows SA04-R72-01..08 and SA04-K72-01..07. Scans 2-113, of which 111 are transcribed (K72-01..07; 22 is in no folder). The Pro package MPL_72_035-081 (GPT-6 Astra, ChatGPT Pro mode) was compared with K72 scan by scan (SA04-R72-07). Cote 72 is the developed form of cote 70 (SA04-21): the parameters found there by hand become categories and invariants over any base scheme.

**SA01-1, pinned regular realizations (72/3-26, 72/84-106).**
- Categories of realizations of the universal pinned n-polytope: projective, affine, vector, orthogonal, autodual or not.
- The rigid category C_0 has isomorphism classes Γ(S, O_S)^{2n+1} (72/14-17): the 2n+1 parameters of 70/34.
- The kernels of Aut(E, V, f) → Aut(P(V)) are the identity and the antipodism.
- The invariant subspaces over a field (72/80-83): G is irreducible on C iff ρ and all β_i are nonzero.
- Theorem 1 and the existence of s_0 over any ring (72/97-106).
- All proofs checked (SA04-R72-06, R72-08).
- The equivalence on 72/76-77, left open by sweep 2's notes, holds for n ≥ 2. The exception on 72/17 is n = 1, not "n = 2" (SA04-K72-01).

**SA01-3, the invariant form (72/18-20, 35-43, 54-55, 107-113).**
- With λ_i = -1 the invariant forms are the multiples of f_V. For n = 2, f_V is smooth iff β_0, β_1 and α_0 + α_1 are invertible; the half-discriminant is -β_0²β_1(α_0 + α_1) (SA04-R72-01).
- The group U_ρ, and the antipodism as its unique section (72/38-43).
- In characteristic 2 with n odd the antipodism is the identity and D_0 is tangent to Q_X (72/54-55).
- Stiefel-Whitney and Brauer classes (72/107-113). Both formulas are right: w_* = (1 + η_0 + η_1)(1 + η_0 + η_2) for n = 2, and Br(f_V) = c(f_V) - c(x² + yz) is the class of the conic bundle (SA04-R72-05).
- Two errors there (SA04-K72-05):
  - H¹(S_0, Z/2) also needs ∂(2);
  - η_i² = εη_i, so his "10 classes plausibly independent" is false: at most 7 are.

**SA01-4, continuants (72/45-71).**
- δ_n = β_0^n···β_{n-1}·L_n, the recursion of L_n, L_2-L_4 and both congruences mod 2 of 72/51 are computed for n ≤ 5, and so is σσ' = β + γρ (SA04-R72-04).
- One sign slip, on 72/71 (SA04-K72-04).
- This also settles SA01-5's sign and arity doubts on 72/52-53 and 61 wherever the formula is determined by the computation.

**SA01-6 and SA01-C3, decided on the scan (300 dpi; SA04-R72-02, SA04-K72-02).**
- The ink reads "β_i = α_i + 2 = 2(2cos²θ_i + 1) = 4cos 2θ_i". The "+1" is his, and both transcriptions are faithful.
- The line is his slip: he wrote α_i for the ratio 4cos²θ_i.
- The coherent statement, from 72/34 and 72/45, is β_i = 4cos²θ_i and α_i = β_i - 2 = 2cos 2θ_i.
- Sweep 2's correction ("+1" → "-1") is incomplete: with -1 the line gives 2cos 2θ_i, not 4cos 2θ_i.

**The Pro package, for SA01's notes (SA04-R72-03, R72-07, SA04-K72-03).**
- On 72/35 the Pro misreads the bracket as "Peut-être faux. Il en donne ...". The ink reads "Peut-être faut-il se donner au préalable hyp. qu. entière lisse invariante". He does not doubt the statement; he proposes assuming a smooth invariant quadric from the start. Every Pro note that rests on the "faux" reading should be withdrawn.
- 72/45 "sommets génér." (K72) or "géom." (Pro) remains undecided.
- Mean similarity of the two witnesses: 0.87. They agree on every formula checked.

**SA01-7, dating.** Scans 59-71 are written on reused sheets: USTL thesis notices of 26 June to 3 July 1978, and decisions of the Conseil de l'Université of May 1978. That puts them after July 1978. 72/70 is a private administrative sheet; it is not reproduced.

**SA01-2 (the LM bridge B5).** Nothing on the pages of cote 72 bears on level-n maps, the Farey map or M_{0,5}. The cote was read in full.

**Other slips, not viewed on the scan:**
- ⟨a_{i+1}, a'_i⟩ = 1 + α_i - λ_i (72/93; SA04-K72-06);
- "2(n+1)" for 2(n+2) invariant subspaces, and an index range (72/81; SA04-K72-07).
<!-- /reading:cote72 -->

<!-- reading:cote81 -->
### From the reading cote81

**Extent.**
- Every transcribed scan of cote 81 was read: 52 scans, in the Codex-web folders J81-01 to J81-07, the only witness.
- The Pro package named after cote 81 holds only cote 154.
- Seven scans were viewed. The checks are 13 check events (re-proofs, three brute-force computations, scan readings) and 7 corrections.

**What the cote is.** It is not about immersions of the disc, as the sweep 2 map says (SA01-K81-07). It has five parts.

1. **Spherical maps and Belyi functions (81/2-6, "0 Cartes sphériques en général").**
   - Framed oriented spherical maps ↔ "special" rational functions f = P/Q: f(0) = 0, f(1) = 1, f(∞) = ∞, étale over P^1 - {0,1,∞}, critical points off f^{-1}{0,∞} lying over 1 with index 2.
   - He translates this into conditions on P and Q, and observes that Aut(C) acts through Gal(Q̄/Q).
   - Everything checks. His conditions allow free half-edges, as in the cartographic convention, and his trial case Q = 1 is the plane trees (Shabat polynomials).
   - This is the dessins correspondence for the cartographic group G_2 of cote 76 (SA04-24).
2. **A Fermat computation in another hand (81/7-8).** It derives the Barlow-Abel relations correctly and calls the divisibility q | C(q,i) a "hypothesis". The hand on the scan is not his; my attribution, not settled.
3. **n-ary decompositions of a space (81/14-40), in two versions.**
   - Version I: n disjoint closed sets, each cutting a connected X into two components, cut X into n + 1 atoms whose incidence graph is a tree.
   - Version II axiomatizes binary decompositions (closed hemispheres, equator) and non-"panachées" (compatible) pairs, and gives the four-set diagram and its degenerate cases.
   - It then defines a "maquette ordonnée": a finite poset with an order-reversing fixed-point-free involution in which, for every pair, exactly one of x, σx is comparable with y. This is the compatible-split, or nested-pocset, description of a tree.
   - Two errors:
     - (10) ⇔ (11) holds only one way (harmless);
     - the Proposition of 81/40, "C_{≥x} is totally ordered", is false already for the tripod. The true statement, intervals are chains, is where his proof breaks off. Checked over all trees with up to 7 vertices.
4. **Polygon structures and non-crossing partitions (81/41-53).**
   - A finite set with a "bi-circularisation" (the polygon structure of cotes 78-79); segments; "non panachés" (non-crossing) subsets, with four equivalent characterizations, checked for N ≤ 9.
   - Non-crossing partitions from laminar families of segments. He marks his own reconstruction claim "faux" and gives a correct counterexample.
   - "Onglets" (interval blocks): the minimal saturated segments, at least two of them. Checked over 6,914 partitions.
   - A peeling by onglets; the same theory on a path.
5. **Gluing maps along edges (81/54).** Faces and genus when two edges (with one or two "rives") are cut and reconnected. His formulas are right as written in the ink; the transcription's "g' - g''" is wrong.

**Dating.** 81/13 carries a table of his meditation "Notes" up to 1981, so the cote is from 1981 or later. That fits cote 79 (1982 or later) and cote 154 (1983-1984).

**Links.**
- SA04: the cartographic groups of cote 76 and the polygon structures of cotes 78-79.
- SA11: the vocabulary of "rives", "Dessin plié" and polygon structures, shared with the relative-position surface of 154/46-76.
- Cote 80 (pseudolines): the chord and line drawings of 81/10-12.
<!-- /reading:cote81 -->

<!-- reading:cotes71_75 -->
### From the reading cotes71_75

Reader R3 (Claude Opus 5.5 at effort max) of a6d42bf6fe2b0d8a8, 19 Nov 2026. Read: every transcribed scan of cotes 71 (41 scans, J71-01..06) and 75 (31 scans, J75-01..04). The untranscribed scans were viewed: covers, blanks, and one line on 71/35. 11 check events, 8 corrections.

**Cote 71 (SA01-40, SA01-43): the Jordan theorem and three good vertices for plane polygons.**
- **The manuscript.** The archive's cover says "Comprend un manuscrit de Carlos Contou-Carrère", and the byline of 71/21 reads "Carlos C. Contou-Carrère". Folios I-XIX (71/21-48) are in an upright hand in black ink (hand A), dated "le 15 juillet 1976, Montpellier", with a flourish under the date that is not legible as a name.
- **The margins.** They are in a slanted cursive that matches, on the scans compared, the hand of the notes on 71/3-19 and of the versos 71/30 and 32 (hand B). They come in two media: black ink ("lemme X", "ambigu", "faux", "non vide ?") and grey pencil ("faux pour n = 3!", "il faut prendre s comme dans la dém. ...", "dire avant ! (et tu auras ...)", "plan" on the title). The pencil addresses the author as "tu". We do not name the hand.
- **Mathematics.**
  - Theorem 1: the Jordan theorem for polygons, by induction, cutting off the pocket of a hull chord.
  - Theorem 2 ("Dehn (?) non-publié"): every polygon has at least three good vertices (empty triangles), at least two of them interior. It rests on Lemma XX, Meisters' two-ears theorem (1975), and Lemma XXI, a mouth for every non-convex polygon, proved by the pocket argument later published by Toussaint (1991). Both are right; re-proved, and a random search over 17,593 polygons found no exception.
  - Lemma XI (an interior diagonal) is false for n = 3, as the margin says.
  - Slips: a double "Lemme VII", and U/V and Λ¹/Λ² slips on 71/43 and 71/45.
  - The iteration in the proof of Lemma XX is unnecessary: the lemma itself, used as the induction hypothesis, closes it.
- **Hand B's notes (71/3-19, 30, 32).**
  - Regular-open pairs and pseudopartitions (71/10-12, checked; the reading "fermé dans X").
  - Cutting a space along a closed set (71/6-8).
  - The theta-curve conditions (71/14).
  - Separation by a simple closed curve in a surface (71/17).
  - The gluing of two J-polygons along an arc (71/19), a compact form of Lemmas XII-XVI.
  - A braid computation: t² = conjugation by λ_0^{-1} for λ_0λ_1λ_2 = 1 (71/11).
  - The farthest-vertex form of the diagonal lemma (71/30) and the hull-chord lemma (71/32).
- **Reused sheets.** Thesis notices of 19 April 1977 and a bank circular of January 1978; the cover lists "Versos: lettres (1977-1978)". Hand B's notes on such sheets are later than the manuscript.

**Cote 75 (SA01-41): the DEA course "Géométries combinatoires" (C4, 24 pp., 1977-78).**
- **Contents:**
  - groups, homogeneous spaces, torsors;
  - graphs and their topological and rectilinear realizations (strict iff rectilinear, then in ℝ³);
  - contours: classified by the subgroups of ℤ, with orientations and dihedral automorphism groups;
  - ℤ-sets, conjugacy classes and partitions;
  - semidirect products and affine groups;
  - small sets: S_3 ≅ GL(2, F_2), S_4 ≅ GP(1, F_3), A_4 ≅ Aff(1, F_4), S_5 ≅ GP(1, F_5), A_5 ≅ GP(1, F_4), all computed;
  - contracted products and twisting;
  - a combinatorial n-gon as a D_n-torsor, with its vector envelope;
  - "structures cubiques" (W(B_n)-torsors, as in 74/134);
  - orientations of vector spaces, quadratic modules and finite sets, with the associativity formula ω_E ≅ ω_{I⁻} ∧ ⋀ω_{E_i}.
- **Corrections.**
  - 75/9: "u transitif ⇔ tous les n_i sauf un au plus sont nuls". The ink has ⇔. The condition is necessary only: (12)(34). Right: Σ n_i = 1.
  - 75/14: V for E.
- **75/30-33.**
  - A letterhead "Villecun le 30.01.78" to the Minister of Education (nothing more transcribed).
  - The typed announcements of the 1977-78 courses: "Géométrie de l'icosaèdre" (A_5 ≅ SL(2, F_4), S_5 ≅ GP(1, F_5); characteristics 2 and 5 special), and "Géométrie arithmétique des polygônes réguliers", whose aim includes the most general regular n-gon and icosahedron over a ring finite over ℤ. This is the programme of cotes 70 and 72 (SA04-21, SA01-1).
<!-- /reading:cotes71_75 -->

<!-- reading:cotes83_93-92-134 -->
### From the reading cotes83_93-92-134

Cote 83 (scans 3-222) and cote 93, scans 92-134. Reader R1 (Claude Opus 5.5 at effort max), 19 Nov 2026. The first pass was a survey; the full pass read every line of each witness:
- cote 93: Pro MPL_93_092-134 (GPT-6 Astra, ChatGPT Pro mode), the only witness, with its notes and doubts;
- cote 83: the Codex-web folders K83-01 to -14 (GPT-6 Astra at reasoning effort max) with their math notes, and Pro MPL_83_178-222.

Scans viewed: 83/144, 178, 195, 207, 215, 221 and 93/102, 114, 122, 126. Full reading: `cotes83_93-92-134.md`.

**Cote 93/92-134: projective connections and uniformization.** This continues the oper construction of 93/086-091 (SA04-9). It covers:
- L ≅ P^1(ω) ⊗ ω^{−1}, with sections of P − σ being connections on ω;
- c_{D_0+ω_1} = c_{D_0} + 2D_0(ω_1) + ω_1², with the Riccati equation 2λ' + λ² = μ, the poles λ = 2/t + O(t), and the Schwarzian G = −2{s, t} as change of uniformizer;
- the cocycle G(t, s) with H\𝒫_X ≅ ω^{⊗2} and the torsor Conn_{X/S};
- G = 12·G_0 with divided derivatives, and a proof that G_0(t, s) = 0 forces a homography over A[T]/(T^p − α) (p > 3) and A[T]/(T^{p²} − α) (p = 2, 3). This settles the question of SA04 H93-2 for this local model;
- Th. 1 and 2 of uniformization and the algebraic description of projective connections as order-3 prolongations.

Corrections:
- SA01-K93-01: the missing factor 2 on 097 and 103, which he flags himself;
- SA01-K93-02: struck denominators on 102;
- SA01-K93-03: the coordinate change on 114 lacks −G_t(t̃);
- SA01-K93-04: the disc stabilizer is PSL₂(R), not GL(2, R)/R^*;
- SA01-K93-05: the indices 2 and 3 are exchanged on 122.

The Pro notes found most of these independently and add others (C03, C04, E01, D09).

**Cote 83: 2×2 matrices, quadratic and Azumaya algebras (1982-1986).**
- **The icosahedron over F_4** (003-016). Checked exhaustively: S_α has 12 elements, edges are Tr(uv) = α, and the graph is the icosahedron. One slip, det(u − v) = 1 + Tr(uv), is corrected by him on 016.
- **The braid group and SL(2, Λ)** (019-037). Relations checked. One exponent on 028 is wrong (λ'^{−2} → λ'^2), and so is one on 035 (ρ(β²) = u(β)(ρ')).
- **Cross-ratios of four arrows** (038-046). His relation (7) holds for ρ^{−1}, not ρ (the Plücker relation). n-alités = transversal designs (hunch H83-2).
- **Biicosahedra and congruence maps** (052-062). I° is the great icosahedron, and the hemi-icosahedra are complementary (script). The nilpotent cone splits into two classes.
- **The k-polyhedron on the nilpotent cone** (063-074). Edges are Tr(uv) = −1. On 063 and 070-071 he mixes the trace-1 and trace −1 lifts of a 3-cycle (SA01-K83-07).
- **Azumaya rank 4** (075-128). M(b, c, b', c', t) is Azumaya iff Q = t² − bb't + b²c' + b'²c − 4cc' is a unit.
  - I give a complete proof through the trace discriminant −Q², which fills his unfinished "Suffisance" (100).
  - The rule δ(xy) + δ(xy^{−1}) = … on 078 holds exactly when Δ = 0.
  - Also: ρ_0 = δδ'/Q and the discriminant identity (13).
- **Twists and the ∗-product** (129-181). These are the contracted product of quadratic covers, affine spaces with involution, and λ-split extensions. They give the composition law c = b_2²c_1 + b_1²c_2 − 4c_1c_2 with δ(q_1 ⊗ q_2) = δ(q_1)δ(q_2), which is checked.
- **Trace invariants of three and four matrices** (183-221). τ + τ' = Σ and the Gram determinant are checked. Three errors:
  - Π lacks −4cc'c'' (SA01-K83-08);
  - the presumed rank 2^4 for four matrices is false; the generic rank is 2 (SA01-K83-09);
  - the block determinant on 219 is 512, not 728 (SA01-K83-10).
  The Pro notes (A11, C03, C19) and Michel Hua's project found these too. The four-matrix invariants are organized on the cube.

Reused: the letter and texts of *Récoltes et Semailles* (1985), on the alternate leaves of 003-017 and 196-222.

**Deliverables.** Nothing is ready for an edition yet:
- 93/92-134 has a single witness with 447 unsure marks;
- cote 83 needs its corrections SA01-K83-01 to -10 in the apparatus, and the open reading of 178.
<!-- /reading:cotes83_93-92-134 -->

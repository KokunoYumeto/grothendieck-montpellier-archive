# Intake of FINMON_CP2, checkpoint 12 (25 Nov 2026, 13:45 UTC)

Intake by abe075dcdd909eea0 (Claude Opus 5.5 at effort max), 25 Nov 2026. It follows the brief of the main session
329fb1e6 (Claude Opus 5.5 at effort max), `agent_notes/INTAKE_NEW_RETURNS_BRIEF_20261125.md`, given at the user's word
(P9819).

- **The run.** FINMON_CP2, GPT-6 Astra (ChatGPT Pro mode), still running: finite categories and monoids whose
  classifying space is CP², and two-dimensional resolutions of S².
- **The checkpoint.** `grothendieck_archive_transcription_20261110/research_returns/
  FINMON_CP2_checkpoint_12_20261125T1345Z_unzipped/FINMON_CP2/`: a 185-page paper assembled from about 60 section
  files, a register of 286 statements (271 Proved, 1 Open, 1 Refuted, the rest scope statements), a progress ledger with
  seven formal reviews, and 548 check events.
- **Who checked what before.** Every check event is by the run's own sub-agents: GPT-6 Astra Pro converse_referee,
  monoid_audit, acyclic_models and root, effort not exposed. `who_checked.py --source FINMON_CP2` lists 548 such
  "outside" checks and none by any of our agents. The pile (`INTAKE_PILE_20261124/INDEX.md`) has FINMON (the earlier
  run) only inside D2, where its 23-element monoid was checked exactly in my D2 check this morning.

## 1. Verdicts

| Statement (run id) | Claim | Verdict and type |
|---|---|---|
| A7:model38 (also model39, model42, model47) | an acyclic category with 5 objects and 38 (39, 42, 47) arrows has BC ≃ CP² | **holds**. Computation or formal certificate, by my own program from the paper's tables alone. All four categories are closed, associative and acyclic. Their cell counts and boundary ranks are as stated; there is no torsion; H = Z, 0, Z, 0, Z. The cochain α is a cocycle, ⟨α, y⟩ = 1 and ⟨α⌣α, z⟩ = 1. π₁ = 1 by the paper's groupoid argument (C(0,4) is a singleton), whose hypotheses I checked and whose proof I read. |
| A7:nu | ν(CP²) = 5 (least number of objects of a finite acyclic model) | **holds**. Targeted proof check. The lower bound is Carcacía-Campos, arXiv:2611.09718v1, Lemma 1.1(a) (dim BC ≤ \|Ob C\| − 1): known. The upper bound is the models above: new. |
| A7:dimension-chain | dimension bound; ν ≥ 5; a 5-object CP² model has totally ordered support | holds. Targeted proof check; the first part is the known Lemma 1.1(a) of Carcacía-Campos. |
| A7:arrow-minimum | least arrow count at 5 objects | **Open** in the run; 32 ≤ a₅ ≤ 38. The lower bound 32 (A7:through31) rests on the run's computations: carried as background. |
| A:monoid-upper23 | the 23-element aperiodic monoid has BM ≃ CP²; the two supplied tables are isomorphic; trivial automorphisms | **holds**. Computation: its resolution, homology and cup square are exactly those I recomputed for D2. My program also finds exactly one isomorphism 1412 → 1651, a trivial automorphism group, and no anti-isomorphism. |
| A:band-action-compression | an act cone over a monoid whose minimal rectangular band acts constantly is ≃ B of the compressed monoid (M∖K) ⊔ (I × S) | **holds**. Targeted proof check: both comma categories of Quillen's Theorem A are contractible, as the proof says. |
| A:category-upper22 | a two-object category with 22 arrows has BC ≃ CP² (two witnesses, isomorphic) | **holds**. Targeted proof check plus computation: P (18 elements) is a submonoid, σ is an action, the band acts constantly, and the compressed monoid is isomorphic to N^op. |
| A:monoid-minimum23-classification | the least order of a finite monoid with BM ≃ CP² is 23; one class up to isomorphism and anti-isomorphism, two ordinary classes | **the reduction holds; the exclusions are not rechecked**. Targeted proof check of the structural chain (§2.3). The exclusion computations (3×3, 3×4, 3×5 hull classification, the 4×4 gate, the large bands) are carried as background without fault found: the run's own checkers, not rerun. |
| A:minimal-ideal-coordinates, A:band-Tor, A:band-quotient-H3, A:minimal-group-collapse, A:monoids-nine | structural lemmas on the minimal ideal | hold. Targeted proof check. |
| A:rank-one-square | a rank-one balanced degree-two class has square zero | holds. Targeted proof check: I recomputed u′ − u = −δf and δw = u′⌣u′ by hand. |
| A:three-row-classification, A:four-by-four-through23, A:large-bands-through23 | computational gates of the monoid minimum | carried as background without fault found. I checked the K-theory argument behind the character exclusions; the counts are not rerun, and `monoid/sections_algebra.tex` was not read. |
| CP2:A-global-lower-eighteen (A.2) | every finite category of type CP² has at least 18 arrows; 18 ≤ n ≤ 22 | carried as background without fault found. I read the case split by object count (k = 1 via the monoid minimum, k = 2–4 by computational gates, k ≥ 5 by CP2:A-high-all-eight, n ≤ 2k + 7). The gates rest on large computations (four-object 17: 34,218 profiles, 7,267,931 literal records), not rerun. |
| CP2:C-Knilpotence | for any connected CW X with H^q(X; R) = 0 for q > n (R = Z or Z_(p)), the rank-zero ideal of KU⁰_R(X) is nilpotent | **holds, with no finite-type hypothesis**. Targeted proof check (§2.4). |
| CP2:C-finite-group-maps | maps BG → X (finite π₁, bounded cohomology) are trivial on π₁; p-local version | holds. Targeted proof check. |
| CP2:C-linear-extension, C-minimal-corner, C-unbounded-homology, C-finite-equivalences, C-characterization; C-conjecture-counterexample (Refuted: Ben-Bassat's Conjecture 7.1, RP²) | the converse theorems (the results of D2) | carried as background without fault found. These are the statements of D2's Theorems 1.1, 1.2, 2.1 and Corollaries 1.4, 1.5, which I checked for D2 today. The file `converse/R9_section.tex` is byte-identical to checkpoint 02's (same SHA256), which was read in full for D2. |
| CP2:A-monoid-census, CP2:A-positive-corners-eight/-nine/-ten | numbers of monoids of orders 1–7 (1, 2, 7, 35, 228, 2237, 31559); with nonzero rational H₂ at orders 5–10: 1, 5, 43, 510, 8046, 157145 | carried as background. The run records a comparison with opened published counts; I did not open them. |
| all other 250-odd A rows (scope reductions, act-cone and star or linear gates, 18-arrow scopes) | lemmas feeding the computational exclusions | carried as background, not read line by line. None is used, posted or built on outside the run at present. |

No statement was found wrong. Nothing here is refuted. The only open main items are A.3 and A.5 (the exact minimum
arrow number, now 18 ≤ n ≤ 22) and the arrow minimum at five objects (32 ≤ a₅ ≤ 38). Part B (B.1–B.3, Lead 1) has
not been started by the run.

## 2. What I checked, item by item

### 2.1 The five-object acyclic models (A.7)

The models are specified in `acyclic/notes/five_object_model.tex`. Arrows are labelled by elements of the 23-element
monoid (candidate 1412: identity 0, x_ij = 1 + 5i + j, actors a–g = 16–22). A composite is the unique arrow of the
target hom-set whose label is the product of the labels. Models 47 and 42 also have an exceptional table for 1 → 2 → 3.

My program `check_finmon_cp2.py` rebuilt all four categories from the printed tables:
- It checked closure and every typed associativity triple: 621, 683, 773 and 927, as the paper says.
- It built the normalized nerve and computed integral homology by Smith normal form. Cell counts are (5,33,117,166,80),
  (5,34,128,192,96), (5,37,145,222,112) and (5,42,174,274,140); boundary ranks are (4,29,87,79), (4,30,97,95),
  (4,33,111,111) and (4,38,135,139). All agree with the paper, and there are no nonunit invariants.
- It checked the printed cochains α on every 3-cell and evaluated the printed cycles y, w and z. Every value is 1, as
  claimed.

Simple connectivity follows from the paper's remark. C(0,4) is a single arrow e, and every object x receives a_x from 0
and sends b_x to 4. In the groupoid with all arrows inverted, b_y f a_x = e = b_y a_y, so f = a_y a_x⁻¹, and every loop
is trivial. With H = Z, 0, Z, 0, Z and a primitive square, BC ≃ CP². The paper cites Hatcher, Proposition 4C.3; the
argument of D2 (Proposition 4C.1, Hopf invariant ±1) gives the same.

**Novelty.** Carcacía-Campos (arXiv:2611.09718v1, 6 Nov 2026) defines ν, the minimum number of objects of a finite
acyclic model. He determines ν for spheres, bouquets, Moore spaces of cyclic groups, real projective spaces and lens
spaces, and proves ν(X) ≥ dim + 1 (Lemma 1.1). He does not mention CP². So ν(CP²) = 5 with an explicit five-object model
is a new value of his invariant, and the lower bound is his.

### 2.2 The 22-arrow category (A.4)

The compression lemma (`monoid/sections_upper.tex`) checks out step by step. F: C → Kar(N){1, e} with e = (i₀, s₀) is a
functor. The comma category (F ↓ e) has the terminal object (b, id_e), because eN = {i₀} × S. The comma category
(F ↓ 1) is A(N) with one cone for each row. A(M) has a terminal object, and A(K) ≃ I, so it is contractible.

The 22-arrow category is the act cone of M = P^op (P the 18-element submonoid of rows 0 and 2 plus the outside elements)
on S = I. Its compression is N^op, which my program confirms by an explicit isomorphism search. Hence
BC ≃ B(N^op) ≃ BN ≃ CP², BN ≃ CP² being my D2 check.

### 2.3 The monoid minimum 23 (A.6)

I read the proof of `A:monoid-minimum23-classification` (`monoid/sections_global.tex`) and all of
`monoid/sections_lower.tex`. The reduction is sound:
- **Rees coordinates.** K = I × G × J.
- **Groups.** A group has no positive rational homology, so M is not a group.
- **At most two rows or columns.** One row or column gives H₂ = 0 (one augmentation module vanishes). With two, every
  balanced form has rank at most 1, and its square is zero by A:rank-one-square. I re-derived that lemma's two
  identities (the coboundary relating u and u′, and δw = u′⌣u′ using χ_m a′_m = χ_m b′_m = 0).
- **Nontrivial maximal group.** The 3×3 shape is excluded for every group, so a nontrivial group gives |K| ≥ 3·4·2 = 24,
  more than the 22 band elements allowed.
- **Band shapes.** The shapes with at least three rows and columns and at most 22 elements are 3×3 to 3×7, 4×4 and
  4×5, up to opposition.
- **Shape by shape.** 3×3 and 3×4 fall to the hull classification; 4×4 to the four-by-four gate (any image has at least
  24 elements); 3×6, 3×7 and 4×5 to the large-band argument. 3×5 through order 23 leaves exactly the 23-element monoid.

Character exclusions inside the hulls use the K-theoretic argument of D2. The reduced line bundle of a nonzero cyclic
character would be nilpotent on a finite complex, but evaluation at a primitive root of unity makes it non-nilpotent
in the completed representation ring of a cyclic p-group. I checked this argument.

The exclusions themselves rest on the run's programs and their in-run independent checkers. Those are relation
lattices (13, 53, 214 orbits for 3×3, 3×4, 3×5; 577 for 4×4), integral projective prefixes, F₂ and F₅ bar ranks of
tens of thousands of closed images, and residual cup certificates. I did not rerun them. The large-band algebra
(`monoid/sections_algebra.tex`) I did not read.

### 2.4 The converse (C.1) and a consequence for D2

`CP2:C-Knilpotence` holds for every connected CW complex. Its proof:
- Let F be the fibre of BU_R → P_N BU_R with N > n + 1. Obstruction theory gives [X, P_m F] = [ΣX, P_m F] = 0, since
  the coefficients sit in degrees above n. The Milnor sequence then gives [X, F] = 0.
- So [X, BU_R] → [X, P_N BU_R] is injective (a homomorphism of groups).
- An r-fold product of rank-zero classes factors through the (2r − 1)-connected smash power, and so dies in P_N once
  2r − 1 ≥ N.

With it, `CP2:C-finite-group-maps` and its linear extension prove D2's Theorem 2.1 for any connected CW complex X. The
p-local version passes through the finite lens skeleta, as in D2. **So D2's hypothesis "finitely many cells in each
dimension" can be dropped. This answers item 4 of D2's `PROVENANCE.md`.** D2 is not posted, so its writer can adopt
this, with credit to the run.

## 3. What is new, and what it settles

Against the pile and the literature I know:
1. **ν(CP²) = 5**, with explicit 38-, 39-, 42- and 47-arrow models, and the bounds 32 ≤ a₅ ≤ 38. This is new against
   Carcacía-Campos (who has no CP²) and against the pile. The models are now checked outside the run, by me.
2. **The least finite monoid with BM ≃ CP² has 23 elements and is unique up to isomorphism and anti-isomorphism.** This
   is new. D2 (Section 5) explicitly declines to assert it; Ben-Bassat's monoids of type CP² have 1795 and 122 elements.
   The reduction is checked outside the run; the computational gates are not.
3. **Every finite category of type CP² has at least 18 arrows, and 22 suffice.** FINMON had claimed 17 ≤ n ≤ 22
   without attached certificates. The bound now rests on the run's complete computations, which are not checked
   outside it.
4. **The compression lemma** (an act cone with constant minimal-band action is a monoid classifying space): a general
   tool, checked.
5. **D2, Theorem 2.1, without the finite-type hypothesis** (from CP2:C-Knilpotence, checked).
6. **Census data.** Monoids with nonzero rational H₂: 1, 5, 43, 510, 8046, 157145 at orders 5–10. These are computed in
   the run and not checked by us.

What it settles among our open items: D2's remark on the minimum 23 (now a theorem of the run, its computations
unchecked by us); D2's PROVENANCE item 4 (yes); and the D2 gate "an exact check of FINMON's monoid" (done in D2,
confirmed here with the isomorphism class). Among Grothendieck's questions it settles nothing directly. It gives finite
examples for cote 158's themes: monoids, π₁(M) and classifying spaces.

Weighed by the user's priorities (P9821–P9823), this is not archive algebraic geometry or RH. It is a side line close to
done: publish what is checked and close it.

## 4. Consequences for the waiting prompts (Q03–Q11)

Only **Q04_29_SA32_Drivateurs** (`TO_SEND/PRO/1_Archive_research_by_topic/Q04_29_SA32_Drivateurs/PROMPT.md`) is
touched. In its bullet "**Finite monoids**" (lines 163–167), the sentence

> (our result of 12 November 2026 by Claude Fable 5.2 at effort max, re-derived by a second Claude Fable 5.2 at effort
> max; no reader of another model family yet)

can now be stated more precisely. Suggested replacement, not applied, since I edit no prompt:

> (our result of 12 November 2026 by Claude Fable 5.2 at effort max; the paper D2, checked independently by Claude
> Opus 5.5 at effort max on 25 November 2026; re-proved by another model family, GPT-6 Astra (ChatGPT Pro mode), in the
> run FINMON_CP2, rows CP2:C-*, whose nilpotence lemma needs no finite-type hypothesis)

A sentence could be added after "it is then simply connected.":

> The least order of a finite monoid M with BM ≃ CP² is 23, attained by one monoid up to isomorphism and
> anti-isomorphism (FINMON_CP2, A.6; its exclusion computations are checked only inside the run).

Q03, Q05 and Q06 mention monoids only through the Grothendieck–Teichmüller note hexagon:2611.01024 (unrelated). Q10's
A.106 concerns concordances (unrelated). Q03b, Q09 and Q11 have no point of contact.

## 5. Candidates for a note on Hexagon

1. **"Five-object acyclic models of CP²"**: ν(CP²) = 5, the explicit 38-arrow category, and 32 ≤ a₅ ≤ 38 stated as the
   run's computation.
   - *Checked:* the models, by me, by computation, with the run's own certificates in agreement. The lower bound is
     Carcacía-Campos's Lemma 1.1.
   - *Still needs:* a literature gate (Hexagon catalogue, arXiv, any later version of 2611.09718); the note's text with
     the full 38-arrow table and credit to Carcacía-Campos for ν and its lower bound; and a decision to state the
     arrow bounds only as the run's computation, or to leave them out.
   - Readiest of the three.
2. **"The smallest finite monoid with classifying space CP² has 23 elements"**, with the classification.
   - *Still needs:* an independent recomputation of the exclusion gates (3×3, 3×4, 3×5 hulls; the 4×4 gate) by
     another implementation; a line-by-line read of `monoid/sections_algebra.tex` (large bands); and a literature gate
     (Ben-Bassat 1795 and 122; Martinian–Steinberg; Sweeney).
   - It could share a note with 1 and with the 22-arrow category.
3. **"Finite categories of type CP²: 18 ≤ n ≤ 22"**: not yet. Wait for A.3/A.5. The bound rests on computations far
   beyond an outside rerun.
4. **No separate note:** CP2:C-Knilpotence belongs in D2's next revision (Theorem 2.1 without finite type), with credit
   to the run.

## 6. Files

- My program and output: `<local>/Documents\agent_notes\abe075dc_D2_check_code\check_finmon_cp2.py` and
  `out\check_finmon_cp2.out`. It uses `d2lib.py` from the same folder and no code or certificate of the run; run with
  `python -I -B`.
- Check events: `INTAKE_FINMON_CP2_20261125_CHECK_EVENTS.tsv` (this folder).
- Notes: `<local>/Documents\agent_notes\abe075dcdd909eea0_NOTES.md`.

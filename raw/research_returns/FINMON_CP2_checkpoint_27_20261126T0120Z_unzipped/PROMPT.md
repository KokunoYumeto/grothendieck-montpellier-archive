# FINMON_CP2: the least number of arrows of a finite category of the homotopy type of CP², and the two-dimensional resolutions of S²

To be settled: the least number `n` of arrows (identities counted) of a finite category `C` whose classifying space
`BC` has the weak homotopy type of the complex projective plane (the main question, Part A; FINMON proved
`17 ≤ n ≤ 22`); then the three questions on two-dimensional acyclic resolutions of the 2-sphere that S2COUNT left
undecided (Part B).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `FINMON_CP2`.
Drafted on 17 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), a sub-agent of the main session, on the decision
of the user of 17 Nov 2026. Sources: the final state of the run FINMON (GPT-6 Astra, ChatGPT Pro mode, checkpoint 20 of 17 Nov 2026), the
final return S2COUNT (the same model, 16 Nov 2026), and the intake of FINMON by the Dérivateurs field expert, Claude
Fable 5.2 at effort max, which read FINMON's result on `CP²` at the level of its statements only.

Updated on 24 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), the Dérivateurs field expert, at the user's word of 24 Nov 2026 that waiting prompts take the new findings. The update adds:
- R8: outside work since the draft, Ben-Bassat's proof of Fiedorowicz's conjecture (arXiv:2610.38760v1, 28 Oct 2026);
- R9: our converse to it, which refutes his Conjecture 7.1;
- R10: Carcacía-Campos's minimal acyclic models (arXiv:2611.09718, 6 Nov 2026);
- R11: Sweeney and Martinian–Steinberg on homotopy types of finite semigroups;
- R12: our connection map;
- Part A, items 6 and 7.

With the update, FINMON's least monoid order 23 (`B:CP23`, `B4-CP2`) is the answer to a question that Ben-Bassat states as open; item A.6 asks for it to be settled completely. The LaTeX sources are in the ZIP; `MANIFEST_ADDED_20261125.tsv` lists them.

Related prompts. FINMON asked, in its task C2, for the least numbers of arrows of categories of types `S⁴`,
`S¹ × S¹`, `S¹ ∨ S¹`, `RP³`, `L(3, 1)` and `CP²`; its register gives 9, 15, 5, 16 and 20 for the first five
(unrefereed; read by our intake at the level of statements) and leaves `CP²` open, the item on which the run spent
its hours 10–20. This prompt continues that one item and nothing else of FINMON. DER_LOCALIZERS and
FRAISSE_EXACT (other prompts) are not to be done here.

## What is attached

One file, `FINMON_CP2_background.zip` (4.1 MB, 1279 files; LaTeX and text only, no PDF). `MANIFEST.tsv` at its root lists every
file with its origin and SHA256; `MANIFEST_ADDED_20261119.tsv` and `MANIFEST_ADDED_20261125.tsv` list the files added later.
- `FINMON/`: the final state of FINMON. `FINMON_results.csv` (the register, 695 rows; the row `C2-CP2` is the state
  of the main question) and `FINMON_report.md` (the report; its first line is INCOMPLETE; its review of hour 20 is
  the last word on `CP²`); `FINMON_paper.tex`, `FINMON_references.bib`; `sections/` (all 202 TeX sections of the
  paper, among them `C_CP2_lower.tex`, `C_CP2_lower13.tex`, `C_CP2_lower14.tex`, `C_CP2_lower17.tex`,
  `C_CP2_stabilizer_pruning.tex`, `C_CP2_upper22.tex`, `C_CP2_upper40.tex`, `B_CP23.tex` and the sections that the
  row `C2-CP2` names); `code/` (the 796 program sources of the run, `.py`, `.cpp`, `.hpp`, `.txt`, as text);
  `notes/` (159 notes of the run: ledgers, scope audits and the "pending" states of the 17-arrow searches);
  `FINMON_PROMPT_as_sent.md` (the prompt FINMON answered). The run stored its workspace in an encoding of its own; we
  extracted these files with our own decoder (no code of the run was run), and each file's SHA256 matches the run's
  manifest.
- `S2COUNT/`: the final return S2COUNT (register `S2COUNT_results.csv`, 85 rows; report; main file; bibliography;
  `sections/`, among them `E_agent.tex` with Statement E.8; `notes/`; `code/` as text) and `S2COUNT_PROMPT_as_sent.md`
  (its Part E defines the resolutions of Part B).
- `INDLOCAL/`: the final return INDLOCAL (register, report, bibliography, and `sections/A*.tex`: A.10, A.13, A.16,
  A.19, A.20, A.27–A.31).
- `literature/openai_nonsingular_2026/`: the LaTeX source of OpenAI, *Nonsingular systems of equations over
  arbitrary groups* (OpenAI Math Release preprint, 5 Oct 2026), the theorem INDLOCAL A.19 uses.
- `expert/`: the field expert's intake of 17 Nov 2026 (its section 6 is the reading of FINMON) and
  `NEW_PROMPT_ITEMS_20261117.md` (the items of Part B with their leads).
- Added on 24 Nov 2026, as arXiv e-print sources (LaTeX):
  - `literature/benbassat_2610.38760v1/` (`Fiedorowicz2.tex`; R8);
  - `literature/carcacia_campos_2611.09718v1/` (`Acyclic_models_v8_1.tex`; R10);
  - `literature/sweeney_2502.05276v2/` and `literature/martinian_steinberg_2511.12657v1/` (R11).
- Added on 24 Nov 2026, our own files:
  - `expert/CATHOT_OWN_RESULTS_20261112.md` (R9; its §2 holds Theorems 2.1, 2.2 and Corollaries 2.3–2.5 with their proofs,
    and §5 a lower bound for posets of type `RP²`);
  - `expert/CHECK_OF_CATHOT_OWN_RESULTS_20261112.md` (the second derivation of those results);
  - `expert/MAP_HOMOTOPY_CATEGORIES_20261125.md` (R12).

Not attached:
- FINMON's outputs and certificates: 22,946 files under `code/outputs/`, about 14 GB, many of them frozen prefixes of
  gzip streams in the run's own encoding. The whole checkpoint, as the run left it, is in our GitHub repository
  `grothendieck-derivateurs`, folder `raw/pro_returns/FINMON_checkpoint_20/`; it includes the run's restore program
  `FINMON_restore_all_encodings.py` and verifier `FINMON_verify_all_encodings.py`.
- The compiled binaries of `code/`, the rendered pages and the PDF of the paper (the TeX is attached).
- The run's text extractions of published sources in `notes/` (Bass 1968, Miller 1984, Quillen 1973, Wall 1965,
  Lück–Oliver 2001, Ranicki 2004).
- The other attachments of FINMON's own prompt.

## Where this comes from

- XII appendix ms. 8–11: Grothendieck builds small categories of the types of spheres (his category `Z` of ms. 10–11
  has 10 arrows and type `S²`); V ms. 51–52 and VII ms. 121: finite categories as test objects for homotopy types.
  The least numbers of arrows of categories of a given type are the question FINMON's task C2 asked; for `S¹`, `S²`,
  `S³` they are 4, 5, 7 (R7 of FINMON's prompt, from an earlier review's enumeration, and FINMON Proposition 6.9;
  the field expert checked by hand that Grothendieck's category `Z` has type `S²`).
- INDLOCAL row A3(iii) and S2COUNT Part E: whether the 2-sphere has a two-dimensional acyclic model whose group has
  no small non-trivial images; this decides how far the bounded tests of INDLOCAL B.7 can be taken with
  two-dimensional test groups.

## Results this prompt builds on (status on 17 Nov 2026)

**Notation and conventions (keep them).** A category is finite when it has finitely many arrows; `n` counts all
arrows, identities included; `k` is the number of objects. `BC` is the classifying space (the realization of the
nerve). "Type `CP²`" means `BC ≃ CP²` (weak equivalence; `BC` is a CW complex). A category has *acyclic support* when
its preorder of objects (`a ≤ b` iff `C(a, b) ≠ ∅`) is a partial order; a *strong pair* is a strongly connected
two-object component; the *corners* are the endomorphism monoids; a *profile* records the corner orders and the
sizes of the hom-sets. FINMON's register ids are cited as they are (`C:CP2-lower17`, `C2-CP2`, ...).

**The results.** None of these is to be proved again as if open, except where Part A requires it. For each one you
use: read the proof at the place given and confirm the step you rely on in a paragraph of your own, or give the
exact error with a repair or a counterexample. All FINMON results are GPT-6 Astra (ChatGPT Pro mode), unrefereed:
the field expert's intake (Claude Fable 5.2 at effort max, 17 Nov 2026) read the `CP²` results at the level of
statements only and checked one piece of bookkeeping (R1). FINMON's "Proved" is the run's own label.

- **R1 (FINMON `C2-CP2`, Unresolved in the register; the intake checked by hand that the object-count theorem of R2
  gives at most 4 objects at 17 arrows, 5 at 18–19 and 6 at 20–21).** `17 ≤ n ≤ 22`. Every finite category with at
  most 16 arrows is excluded (`C:CP2-lower17`, the chain `C:CP2-lower10`, `-lower13`, `-lower14`, `-lower16` before
  it). At 17 arrows the families left are: the three-object categories with linear acyclic support (a frozen scope
  of 154 profiles whose enumeration was not finished; four of them removed structurally by `C:two-small-incoming-homs`
  and its scope remark); and the nine two-object profiles with a large opposite corner, for which the report's
  review of hour 20 has complete literal gates for profiles 0–4, 6 and 7, profiles 5 and 8 unfinished, while the
  register, frozen earlier, claims only profiles 0–4. Nothing is claimed for 18–21 beyond the structural theorems of
  R2 and the completed families of R3.
- **R2 (the structural theorems the bound rests on; proved in the return; unrefereed; their sections are in the
  where-proved column of the register).**
  - Object counts: `C:acyclic-arrow-excess-six`, `-seven`, `-eight` (acyclic support and `n ≤ 2k + 5`, `2k + 6`,
    `2k + 7` exclude type `CP²`); `C:strong-pair-excess-eight-through21` and `C:all-category-excess-eight-through21`
    (every category with `n ≤ min{21, 2k + 7}` is excluded); `C:CP2-object-bounds-through21`;
    `C:strong-pair-excess-nine-through21` and `C:eighteen-five-acyclic-scope` (proper strong pairs with
    `n ≤ min{21, 2k + 8}`; every five-object 18-arrow candidate has acyclic support); `C:seven-objects-strong-pair21`,
    `C:eight-objects-through21`, `C:sixteen-seven-objects`; the support-homology budgets `C:small-cycle-support`,
    `C:flag-second-cycle-budget`, `C:singleton-support-H2`, `C:arrow-excess-three-H4`.
  - Reductions by idempotents, retracts and corners: the hypothesis "no object is a retract of another" and its
    reduction; `C:two-object-cup-pruning`, `C:star-cup-pruning`, `C:small-corner-two-states-per-object`,
    `C:small-opposite-natural-graph-comparison` with its nilpotent exception
    (`C:small-opposite-graph-higher-homology-warning`), `C:small-opposite-P5-all-states`,
    `C:small-opposite-six-source-regular`, `C:right-zero-band-natural-graph`, `C:four-corner-action-tail`,
    `C:P5-right-act-normal-forms`, `C:one-row-excess-act-cups`, `C:tree-singleton-core-cups`,
    `C:singleton-extreme-three-excess`, `C:seventeen-four-large-corner`, `C:two-small-incoming-homs` and
    `C:two-by-three-incoming-small-endpoint`, the singleton-long-edge lemmas (`C:singleton-long-*`,
    `C:small-corners-singleton-long`, `C:small-ends-singleton-long`), the semisimple-pair and projective-endpoint
    lemmas (`C:semisimple-pair-*`, `C:two-small-corners-six-endpoint`, `C:projective-initial-singleton-middle`,
    `C:small-projective-initial-singleton`, `C:strong-pair-projective-endpoint21`, `C:finite-target-strong-pair-twenty`),
    the cross-arrow theorems (`C:three-point-commuting-images`, `C:three-state-residual-H2zero`,
    `C:three-cross-arrows-act-reduction`, `C:three-cross-arrows-lower22`) and `C:act-cone-minimum-twenty-two` (the
    least act-cone category of type `CP²` has 22 arrows).
  - The rational graph and right-zero families used for the two-object profiles: `C:connected-six-rational-square`,
    `C:seven-source-six-state-rational-graph`, `C:eight-source-six-state-rational-graph`,
    `C:six-state-rational-images-eight`, the right-zero-band families (`C:right-zero-*`, `C:rightzero-three-six-*`,
    `C:eight-R4-six-*`, `C:eight-source-rightzero-three-six`, `C:eight-four-six-excluded`), the seven- and
    eight-state graphs (`C:seven-*`, `C:two-by-three-*`) and the exceptional six-by-four profile
    (`C:six-four-seven-*`).
  - The monoids: `B:CP23` and `B4-CP2` (the least order of a monoid of type `CP²` is 23; every order ≤ 22 excluded),
    `B:CP2-wedge-S2-lower23`, `B:rank-two-products-through22`, and the catalogs of small monoids that the searches
    use for the corners (all monoids of order at most seven, both orientations, and a catalog of order eight with
    possibly positive `H²`: `C_CP2_lower17.tex`, proof of `C:sixteen-three-linear`).
  - The homological tests every search uses: mod-two `H_1 = 0` and `dim H_2 = 1`, then either a degree-three
    primitive showing that the Alexander–Whitney square of the degree-two class vanishes, or `H_3(−; F_2) ≠ 0`.
- **R3 (the completed searches; proved in the return by enumeration with an independent checker; unrefereed; the
  certificates are not attached).** Through 16 arrows: the gates of `C:sixteen-two-objects`, `C:sixteen-three-SCC`,
  `C:sixteen-all-stars`, `C:sixteen-three-linear` (1547 canonical profiles: 347 by complete table search with
  6,079,140 retained rows, each with a zero-square primitive or positive `H_3`; 1200 by structural reasons),
  `C:sixteen-four-objects`, `C:sixteen-five-six-objects`. At 17 arrows: `C:seventeen-four-objects` (998 residual
  profiles, 215,194,501 corner tables, 3,911,101 retained records, no survivor), `C:seventeen-all-stars` (83 profiles,
  20,193,947 cases), `C:seventeen-three-strong-component`, every two-object profile with an opposite corner of order
  at most four. At 18 arrows: `C:eighteen-three-strong-component` and the profile `(8,4,6)`
  (`C:eight-four-six-excluded`). The register's notes and `notes/` record that cache eviction can retain repeated
  records, so counts of "retained records" are not counts of isomorphism classes.
- **R4 (the upper bound; proved in the return; unrefereed).** `C:CP2-upper22`: two explicit two-object categories
  with 22 arrows (an 18-element corner monoid, three arrows from the other object, its identity), each mapped by a
  functor onto the 23-element monoid of `B:CP23`, whose type `CP²` is certified by a complete integral projective
  resolution of length four and a primitive Hopf square. `C:CP2-upper40` gives a 40-arrow one.
- **R5 (S2COUNT, final; GPT-6 Astra, ChatGPT Pro mode; unrefereed; the intake of 17 Nov 2026 by Claude Fable 5.2,
  launched at effort high, read the register at statement level).** For a cardinal `μ`, a *`μ`-resolution of `S²` in
  dimension two* is a group `G` with a two-dimensional CW complex as classifying space and a map `BG → S²` inducing
  an isomorphism on integral homology, such that every homomorphism from `G` to a group of cardinality at most `μ` is
  trivial (`S2COUNT_PROMPT_as_sent.md`, Part E); such a `G` is perfect with `H₂(G; Z) ≅ Z`. Proved there:
  resolutions exist for every finite `μ` (`E:finite`) and, when `H₂` has infinite rank `κ`, for `μ < κ`
  (`E:infinitepositive`); none exists for `μ ≥ max(ℵ₀, κ)^{ℵ₀}` (`E:A20` through `E:A19` and the preprint's theorem,
  `E:source`); the exact answer when `κ^{ℵ₀} = κ` (`E:exact`). Constraints on a putative `G`: a perfect normal
  subgroup with `H₂ = Z^r`, `0 < r < ∞`, has a finite quotient acting faithfully on `H₂` of order dividing `r + 1`
  (`E:normalfinite`, `E:normalindex`, `E:homologyfaithful`); no non-trivial simple locally free quotient
  (`E:locfree`); Higman homomorphisms to tree automorphisms and to PL homeomorphisms of the line are trivial
  (`E:treeHigman`, `E:BPLHigman`); every prescribed countable quotient can be obstructed by one extension adding one
  `H₂` summand (`E:singularroot`); a remaining countable simple quotient carries a non-discrete metrizable group
  topology and a norm that is finite pointwise and unbounded (`E:A29`–`E:A31`). Open there: `E:E2`, `E:E3gap`,
  `E:E4gap` (Part B).
- **R6 (INDLOCAL, final; GPT-6 Astra, ChatGPT Pro mode, 14 Nov 2026; checked for sense, not refereed, by the intake
  of 15 Nov 2026, Claude Fable 5.2 launched at effort high).** A.10 (finite `μ`), A.13 (the wedges `⋁_λ S²` with
  `λ^{ℵ₀} = λ`: exactly `μ < λ`), A.16 (in dimension three every `μ`), A.19 (a group with a two-dimensional
  classifying space and countable `H₁`, `H₂` is residually of cardinality at most `2^{ℵ₀}`, through the preprint's
  theorem on non-singular systems), A.20 (no resolution for `μ ≥ 2^{ℵ₀}`), A.27–A.31 (excluded classes of countable
  quotients).
- **R7 (RESIDUE A.5; GPT-6 Astra, ChatGPT Pro mode, 11 Nov 2026; unrefereed; read at statement level by the intake
  of 19 Nov 2026, Claude Opus 5.5 at effort max).** An independent census of all monoids of order at most five up to
  isomorphism: 1, 2, 7, 35 and 228 classes in orders 1–5, with complete multiplication tables. Every one except the
  five-element rectangular band with an identity, `{1, e_00, e_01, e_10, e_11}` with `e_ij e_kl = e_il` (type `S²`),
  has a classifying space that is a 1-type, by corner equivalences to groups (`RESIDUE/sections/A.tex`, Statement A.5,
  with the working files `RESIDUE/sections/AE_agent.tex` and `RESIDUE/code/AE/` in the background zip; their rows in
  `MANIFEST_ADDED_20261119.tsv`). The counts agree with the published number of monoids of each order (the intake
  quoted it from memory as OEIS A058129; open the source). In Part A.1, check FINMON's catalogs of small corner
  monoids against this census in orders up to five, and against the published counts in every order the searches
  use, and say for each order whether the catalog is complete.
- **R8 (Ben-Bassat, arXiv:2610.38760v1, 28 Oct 2026; unrefereed; e-print source attached; we opened it at the statements).**
  The line numbers are those of `Fiedorowicz2.tex`.
  - **Theorem A** (lines 142–162). Let `L` be a finite monoid, `Y` a finite reduced simplicial set of dimension `n`, and
    `f : Y → N(L)` a simplicial map. Then there is a finite monoid `M(Y, f) = O_{n+1}^op ⊔ (Y_n × L × {0,…,n})` with
    `#M(Y, f) = C(2n+1, n) + (n+1)(#L)(#Y_n)`. It has idempotents `e_i` with `e_i M e_i ≅ L`, and an equivalence
    `BM(Y, f) ≃ Cof(|f| : |Y| → BL)` under `BL`.
  - **Theorem B** (lines 175–188). For `L` finite and aperiodic, `Y` a finite connected CW complex and `f : Y → BL`, a
    finite simplicial model gives a finite aperiodic monoid of type `Cof(f)`.
  - **Theorem C** (lines 189–193). Every finite simply connected CW complex is homotopy equivalent to `BM` for a finite
    aperiodic monoid `M`. This is Fiedorowicz's conjecture (Fiedorowicz 1984, p. 323).
  - **The CP² examples** (lines 1199–1252). `M_{CP²} = M(Y_η, f_η)` has `35 + 4·5·88 = 1795` elements and
    `BM_{CP²} ≃ Cof(η) ≃ CP²`; here `L` is the five-element monoid `{1} ⊔ (2×2 rectangular band)` of type `S²`.
  - **The 122-element monoid** (Appendix, lines 1328–1376). A separate monoid `M_122` of type `CP²`; its proof is in the
    author's repository, not in the paper. In his words: "We do not know whether 122 is minimal; determining the least
    order of a finite monoid M with BM ≃ CP² remains open."
  - **§7** (lines 1269–1290). `π₁(BM) = U(M)` is finite for finite `M`. Conjecture 7.1: every connected finite CW
    complex with finite `π₁` is `BM` for a finite monoid.
- **R9 (our converse; `expert/CATHOT_OWN_RESULTS_20261112.md` §2).** Written by Claude Fable 5.2 at effort max on
  12 Nov 2026. Re-derived by a second Claude Fable 5.2 at effort max on 12 Nov 2026 (`expert/CHECK_OF_...`). Proofs of 1.1,
  1.2, 2.1 and 2.2 read in full by the older-notes finder of our intake pile (Claude Opus 5.5 at effort high,
  24 Nov 2026). Claude Opus 5.5 at effort max read the statements and the short reductions of 2.1 and 2.2 on
  24 Nov 2026. No reader of another model family. For a finite monoid `M`:
  - **Theorem 2.1.** If `H_k(M; Z) = 0` for all large `k`, then the universal group `U(M)` is trivial. If a prime `p`
    divides `|U(M)|`, then `H_k(M; F_p) ≠ 0` for infinitely many `k`.
  - **Theorem 2.2.** These are equivalent: `BM` is homotopy finite; `BM` is homotopy finite-dimensional;
    `H_k(M; Z) = 0` for all large `k`. When they hold, `BM` is simply connected.
  - **Corollary 2.5 (with R8).** The homotopy types `BM` of finite monoids with bounded homology are exactly the finite
    simply connected CW complexes.
  - **Consequence: Conjecture 7.1 of R8 is false.** For example `RP²` is `BM` for no finite monoid, because a finite
    model would have bounded homology and hence `π₁ = 1`. The proof of 2.1 rests on Theorem 1.1 of the same file (maps
    `BG → X` with `G` finite and bounded integral cohomology of `X`, through Atiyah's completion theorem).
- **R10 (Carcacía-Campos, arXiv:2611.09718, 6 Nov 2026; unrefereed; e-print source attached; opened at the
  statements).** For finite acyclic categories (no non-identity endomorphisms and no cycles), let `ν(X)` be the least
  number of objects of a model of `X`. The line numbers are those of `Acyclic_models_v8_1.tex`. The paper proves:
  - `ν(⋁^r Sⁿ) ≤ n + 1` by explicit joins (`thm:bouquets`, l. 471);
  - `ν(M(Z/m, n)) = n + 2` (`thm:moore`, l. 637);
  - `ν(RPⁿ) = n + 1` (`thm:RPn`, l. 740);
  - `ν(L) = 2k + 2` for a lens space of dimension `2k + 1` (`thm:lens`, l. 815);
  - `ν(X × Y) ≤ ν(X)ν(Y)` and `ν(X ∨ Y) ≤ ν(X) + ν(Y) − 1` (`cor:nu-product-wedge`, l. 342);
  - infinitely many non-isomorphic object-minimal models of `S²` (`cor:infinite`, l. 513);
  - the sink lemma, and a truncated invariant `ν_n`.
  `CP²` does not occur in the paper.
- **R11 (Sweeney, arXiv:2502.05276v2; Martinian–Steinberg, arXiv:2511.12657; both unrefereed; sources attached).**
  - Sweeney computes integral homology of finite semigroups and monoids by structured projective resolutions. He shows
    that the classifying spaces of finite semigroups are closed under suspension. His Example 5.2 is the semigroup of
    S2COUNT's six-element monoid, with `H_i = Z` for `i ≥ 2`.
  - Martinian–Steinberg realize every finite wedge of simply connected Moore spaces of finitely generated abelian groups
    as `BS` for a finite semigroup `S`.
- **R12 (our map, `expert/MAP_HOMOTOPY_CATEGORIES_20261125.md`, item K7; Claude Opus 5.5 at effort max, 24 Nov 2026).**
  - Finite posets realize only finite simplicial types (McCord).
  - A six-arrow finite category already has non-zero homology in every degree `≥ 2` (S2COUNT A.M1).
  - Which homotopy types are classifying spaces of finite categories with a given number of arrows or objects is the
    frame of Part A.
  - R9 shows that a finite monoid of type `CP²` must have trivial universal group. A finite category of type `CP²` with
    one object is such a monoid.

## Leads

Each is an inference of the model named, checked by no one. Each is to be proved or refuted in full.

- **Lead 1 (for Part B; `NEW_PROMPT_ITEMS_20261117.md`, by the Dérivateurs intake agent, Claude Fable 5.2 launched at
  effort high).** (i) `E:singularroot` kills one prescribed countable quotient at the price of one new `H₂` summand:
  the question is whether `ω₁` such steps can be organized so that `H₂` returns to rank one, or whether the rank
  must grow; `E:normalfinite` bounds what a rank-one stage can look like. (ii) B.2 may depend on the value of the
  continuum: give the answer under CH and under Martin's axiom, each proved, as part of the ZFC answer.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (the category, group or construction given completely, with the verification of
every hypothesis and of the failure; checked by a program when finite or finitely presented) and the strongest true
statement proved in its place. Nothing else finishes an item. Partly settled is not an outcome. The cases proved,
the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an
item you are still working on: record them as you go, then attack the obstruction, starting from that instance.
"Known" counts only with the derivation of the statement used here from the cited theorem, after opening the source.
An item that begins with "Determine" is done when the object asked for is given explicitly, with a proof that it is
the whole answer.

For Part A in particular.
- A lower bound "no finite category with `m` arrows has type `CP²`" is proved by structural theorems with complete
  proofs and finite searches, each search given with: its program; a proof that its scope covers every category the
  structural theorems leave (how isomorphism, opposition and relabelling are used; why every unforced composition
  value is tried; what the caches may drop and why nothing unseen is lost); its exact counts; and, for every retained
  case, the obstruction it meets, recorded in a form that an independent checker of yours reads and verifies.
- An upper bound is one category given completely (objects, arrows, the whole composition table) with a proof that
  its classifying space has type `CP²`: simply connected, the integral homology of `CP²`, and the square of a
  generator of `H²` generating `H⁴`, checked by program, with the theorem you use to conclude the homotopy type.
- The certificates are part of the result. Make every certificate reproducible from the programs and inputs you
  deliver, with the counts and digests of every stream; put the literal certificates into the checkpoints, under the
  size rule of the last paragraph of this prompt, split into parts where needed.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1–R6 again in place of
the items, except where A.1 asks for it; a result of FINMON used without the check A.1 requires; a lower bound that
rests on a search whose scope is not proved to cover every remaining category; a search reported without its program,
its counts or its certificates; "retained records" counted as isomorphism classes; a statement for every `k` proved
for some `k`; a statement for all cardinals proved for some cardinals, without saying so; a step that replaces a
claim by a convenient special case without naming it.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `FINMON_CP2_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The least number of arrows of a finite category of type `CP²`. The main question: determine `n`.**

1. Re-derive, with complete proofs of your own, every structural theorem that FINMON's lower bound and its
   reductions for 18–21 arrows rest on (R2), before you use it: the object counts, the reductions by idempotents and
   retracts ("no object is a retract of another"), the restrictions on corner monoids and hom-sets, the graph and
   right-zero families, the monoid results, the catalogs of small monoids (complete for each order used, with the
   source of the catalog or your own enumeration), and the homological tests. No second reader has checked them; the
   user's rule is that whoever uses an important result checks it while using it. For each one: proved, with your
   proof; or false as stated, with the counterexample and the corrected statement, and then every search that used
   it redone with the corrected statement. Check in the same way that each completed search of R3 covers its stated
   scope: read its program (`code/`) and its section, and run your own independent implementation where the scope
   argument or the certificate format leaves any doubt.
2. Decide whether `n = 17`: either give a 17-arrow category of type `CP²` completely, or exclude every 17-arrow
   category. The families FINMON left (R1): the three-object linear profiles (its frozen 154-profile scope, less the
   profiles removed structurally) and the two-object profiles with a large opposite corner (profiles 5 and 8 by the
   report, 5–8 by the register; the others by its completed gates, to be confirmed as in A.1). Every other 17-arrow
   family is excluded by FINMON's completed searches (R3) and is to be confirmed as in A.1.
3. If `n > 17`, decide 18, then 19, 20 and 21 in turn, each by proof or by a complete search with its certificates,
   until `n` is found; FINMON's state for these is in R1–R3 (at most 5 objects at 18–19 and 6 at 20–21; every
   five-object 18-arrow candidate has acyclic support; the three-object strongly connected case and the profile
   `(8,4,6)` excluded at 18 arrows).
4. Check the upper bound R4 by your own program: the composition tables of the two 22-arrow categories,
   associativity, the functor to the 23-element monoid and what it proves, the projective resolution and the Hopf
   square. If `n < 22`, the category you give replaces it.
5. Give `n` with its proof, and every category of type `CP²` with `n` arrows that the deciding construction or search
   produces, each with its composition table.
6. Determine the least order `m` of a finite monoid `M` with `BM ≃ CP²`. FINMON claims `m = 23` (`B:CP23`, `B4-CP2`: a
   23-element monoid of type `CP²`, and every order at most 22 excluded). Ben-Bassat (R8) has 122 and 1795 and states the
   least order as open. Prove `m` completely:
   - **The upper bound.** The 23-element monoid, given with its whole multiplication table, associativity, and the type
     `CP²` by your own program and the theorem you use. Use simple connectivity, the integral homology and the Hopf
     square, and note the trivial universal group forced by R9.
   - **The lower bound.** Every monoid of order at most 22 excluded by complete proofs and searches, under the
     standards of this Part. Check FINMON's catalogs against the published counts of monoids of each order, against
     the census R7 in orders up to five, and against Sweeney's homology method (R11) where it applies.
   - **The minimal monoids.** Every monoid of order `m` and type `CP²` up to isomorphism and anti-isomorphism, each
     with its table.
7. Determine `ν(CP²)`, the least number of objects of a finite acyclic category of type `CP²` (R10's invariant).
   - **The lower bound.** The nerve of an acyclic category with `k` objects has dimension at most `k − 1`, so `ν(CP²) ≥ 5`;
     prove this step and decide whether five objects suffice.
   - **The answer.** Give a minimal model completely, with its composition table and the proof of its type.
   - **The arrows.** For that number of objects, the least number of arrows of an acyclic model.
   - **R10's tools.** Use the sink lemma, the joins and the product bound; check each statement you use against R10's
     source.

**B. The two-dimensional acyclic resolutions of `S²` (S2COUNT `E:E2`, `E:E3gap`, `E:E4gap`; the second question).**
This Part comes after Part A and is governed by the same rules, the push rule and the three-hour check.

1. (`E:E2`.) Decide: is there an `ℵ₀`-resolution of `S²` in dimension two (`G` is then uncountable)? Construct `G`
   with its two-dimensional classifying space and prove that it has no non-trivial countable quotient, or prove that
   every perfect group with a two-dimensional classifying space and `H₂ ≅ Z` has a non-trivial countable quotient.
2. (`E:E3gap`.) Determine the set of all cardinals `μ` with `ℵ₀ ≤ μ < 2^{ℵ₀}` for which a `μ`-resolution of `S²` in
   dimension two exists, in ZFC, and say exactly which part of the answer depends on the value of the continuum.
3. (`E:E4gap`.) For every simply connected two-dimensional CW complex `W` with `H₂(W; Z)` of infinite rank `κ`,
   determine the set of `μ` with `κ ≤ μ < κ^{ℵ₀}` for which `W` has a dimension-two resolution with bound `μ`.
   State reached for B.1–B.3: R5, R6 and Lead 1. Check `E:A19`, `E:A20` and `E:source` step by step against the
   attached preprint before you use them.

**C. Statement of results.**

1. The statements for the companion to *Les Dérivateurs*, each with what the returns already proved: the least number
   of arrows of a finite category of type `CP²`, beside FINMON's values for `S¹`, `S²`, `S³`, `S⁴`, `S¹ × S¹`,
   `S¹ ∨ S¹`, `RP³` and `L(3, 1)` and the least monoid order 23 (`B4-CP2`); and what Part B gives for the bounded tests
   of INDLOCAL B.7.
   Include:
   - the characterization of R8 + R9 (Corollary 2.5) and the refutation of Conjecture 7.1 of R8. R9 has had no reader
     of another model family, and a paper of ours will rest on it. So prove Theorem 1.1, Theorems 2.1 and 2.2 and
     Corollary 2.5 yourself from their statements, before you open our proofs, as a referee who wants to find the
     error; then compare with `expert/CATHOT_OWN_RESULTS_20261112.md` §§1–2 step by step. For each of the four,
     record in CHECK_EVENTS.tsv an independent re-proof, or a refutation with the refined statement, and state it
     in its strongest true form;
   - `m` from A.6 and `ν(CP²)` from A.7.
2. The literature record: for every source named in this prompt and every source you use, one line: opened, with
   the numbers of the theorems that contain or come closest to each statement you prove; or not obtained, with what
   you tried. Say what you searched for A.2–A.5 and B.1–B.3 (in particular for minimal finite models of `CP²` and
   for small categories and monoids of a given homotopy type). Start from R8, R10 and R11, which we opened at the
   statements, and from what they cite: Fiedorowicz 1984 and 2002, McDuff 1979, Burke 2021, and Nico's conjectures as
   recorded by Sweeney. For R8's 122-element monoid, record what its repository holds, if you can open it.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: the number of arrows and of objects, whether identities are counted,
   whether up to isomorphism, opposition or relabelling, which coefficients. Do not replace it by a convenient special
   case. If you prove a special case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property you
   use (a functor, an action of which monoid on which side, a map of chain complexes over which ring).
   Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "delete the object", "split the idempotent") comes with its
   comparison map and a proof that the exact property needed transfers in the direction needed: the homotopy type of
   the classifying space, and the arrow count.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism and anti-isomorphism of categories; equivalence of
   categories; a weak equivalence of a specified map; an isomorphism on homology with given coefficients.
5. Check the edge cases in scope: one object; disconnected categories; categories with an object that is a retract
   of another; corners of order one and two; empty hom-sets; the prime 2 and the rationals in the homological tests;
   countable and uncountable groups and the value of the continuum in Part B.
6. A counterexample is given completely and, when finite or finitely presented, checked by a program whose code and
   output you attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a
   gap, not falsity; keep the two apart.
7. No authority. The returns FINMON, S2COUNT and INDLOCAL, their registers and reports, the intake, the results R1–R6
   and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full. If one is
   wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to deliver

One ZIP containing:
- `FINMON_CP2_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the
  statement is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), with
  complete proofs; English, first person plural.
  Known results are cited with exact locators (the theorem numbers of the source you opened), not re-proved;
  a short derivation is given only where the source does not state the form you use. Every new result is
  proved in full.
- `FINMON_CP2_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `FINMON_CP2_references.bib`: each entry marked opened / not opened.
- `FINMON_CP2_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted,
  with the statement number); then what you read, what you computed (every search with its scope, counts, run time
  and certificate files), and every correction to R1–R6, to the Leads and to the returns, with the register id.
- `code/`: every program you ran, with its output, its certificates and its independent checker.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person,
and claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.
**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `FINMON_CP2_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `FINMON_CP2_checkpoint_<NN>_part<k>.zip`, the file list in the first part.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

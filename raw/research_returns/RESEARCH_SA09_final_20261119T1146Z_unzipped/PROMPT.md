**The attached files.** Besides this file there is one ZIP, `SA09_de_Rham_cotes_137-138_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA09_study.zip` is the folder `RESEARCH_SA09_study/`), so there is nothing more to unpack; every other file is at the top level under its own name.

**The same files in this Space.** Every file of `SA09_de_Rham_cotes_137-138_night.zip` may also be in this Space's files, flat, each named `P008__` followed by its file name; `P008__SPACE_INDEX.tsv` gives, for each such name, its path inside the ZIP. Where they are there, use them as you would the unpacked ZIP; where a Space file and the ZIP differ, the ZIP decides; where they are not there, unpack the ZIP.

# RESEARCH_SA09: Grothendieck's cotes 137 and 138: polynomial categories and the walking complex (1975-76), and the passport counts of maps with the Galois action (1977-78)

**What is to be settled, in two Parts:**
- **A.** Cote 137, the integral framework for "cochains with divided powers":
  - his polynomial categories, against the strict polynomial functors of Friedlander and Suslin;
  - the Σ-exact universal property, with its essential image;
  - what the universal cosimplicial object with its Γ-operations recovers of a space.
  - carried over from RESEARCH_SA08 (cote 136): his uniqueness conjecture for admissible generalized de Rham theories
    over Z (A.5), and a check of that run's refutation of a published lifting proposition (A.6).

  A.1 is the main question.
- **B.** Cote 138, maps (dessins) and the Galois action:
  - the count of pinned maps when rigidity fails;
  - the degree-6 trees of passport [3,2,1; 2,2,1,1; 6] and their field of moduli;
  - the automorphisms of maps;
  - the Kummer images of the Fermat tower.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA09`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a34c04448e8299803, on 19 Nov 2026. It is the
deep-sweep agent of this topic. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at
effort max).

## What is attached

- **`RESEARCH_SA09_study.zip`: our study of cotes 137 and 138.**
  - `study/STUDY.md`.
  - `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv` (52 rows), `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/SA09_137-138.md`: the full reading by a188625c776c7aca7, with its tables.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the items SA09-1 to SA09-20.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded
    in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA09_transcriptions.zip`: the AI transcriptions (LaTeX) of cotes 137 and 138.**
  - Five packages by GPT-6 Astra (ChatGPT Pro mode), each with notes and doubts: 137 scans 2-44 and 45-86; 138 scans
    1-45, 46-89 and 90-133.
  - `\scanpage{N}` marks scan N of the cote's PDF.
  - The transcriptions carry `\unsure{a|b}` marks. The reading decided some on the scan images, and its CORRECTIONS
    table gives them. Where a step of yours depends on a doubtful reading, say so.
- **No literature is attached.** Fetch the sources listed under "Sources", preferring the arXiv LaTeX source.
- **`SA08_RESULTS_20261119.md` and `SA08_final_paper_tex.zip`: the results of RESEARCH_SA08 that this prompt builds
  on.**
  - RESEARCH_SA08 is the research run on the divided-power de Rham complex of cote 136 (GPT-6 Astra, ChatGPT Pro mode,
    final of 19 Nov 2026, 10:27 UTC). `SA08_RESULTS_20261119.md` lists the results used here by statement id, each
    with its status, where its proof is, and its checks.
  - `SA08_final_paper_tex.zip` holds that run's paper (`RESEARCH_SA08_paper.tex` with `sections/`), its results
    register, corrections, check events, report and progress ledger, its proof notes (`notes/`), its programs
    (`code/`), the small logs of its computations (`logs/`; the fetched sources are left out), and our intake of it
    (`intake/`). `MANIFEST.tsv` gives the origin and SHA-256 of every file.
  - The section "Results of RESEARCH_SA08" below places this prompt on them. A.5 and A.6 come from that run.

## Where this comes from

**The pages.**
- **Cote 137 (86 scans, 1975-76)** builds an integral framework for the divided-power de Rham cochains of his 1976
  lecture (cote 136):
  - the classification of the "∂-perfect" simplicial modules built from Φ (the functions on the vertices of the
    simplices) and Ψ = Φ/kT;
  - the "walking complex" C^• and the universal cosimplicial object C^* = DP(C^•);
  - a Σ-exact universal property;
  - multiplicative structures;
  - on scans 75-86, "polynomial categories" with P_n(X,Y) = Hom(Γ^n X, Y), meant to carry the Γ-operations.
- **Cote 138 (133 scans; dated sheets from 11 Jan 1977 to June 1978, one of 1980)** treats:
  - the descent of covers of P¹ minus finitely many points, and the Fermat tower;
  - the tower of punctured spheres with its special profinite groups;
  - maps (dessins), their moduli schemes and the Galois action on them.

  It is a first draft of Part I of La Longue Marche à travers la théorie de Galois.

**Our reading of them.** Sweep 3 of our horizontal reading read all five transcriptions in full on 18 Nov 2026 (the
reader a188625c, Claude Opus 5.5 at effort max). It re-derived every claim it could, and decided several readings on
the images.

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these
cotes. You may consult them. Credit any point taken from them to "Michel Hua's project", and quote phrases, not
passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries its item and page. The attached tables give the check events, keyed by item. Check each one where
you use it (Rules of proof, 7).

- **R1 (SA09-2, 137:4). The Théorème of scan 4.** The weight-n divided-power Koszul complex of Φ → Ψ maps to the ∧T
  complex Λ^{•+1}Φ, and every connecting map is an isomorphism. So weight n of the PD de Rham complex is a truncated
  flasque resolution of k. With Sym in place of Γ, exactness needs the factorials inverted.
- **R2 (SA09-2, 137:4, 12, 14-17). Corrections to the classification.**
  - Lemma 2 needs "flasque", or π_0(L) = 0, as the ink of its proof line shows.
  - "ils seront même str. spéciaux!" (scan 12) is false for Λ^k(Λ^jΨ) over Z: Λ²(Λ²Ψ) has π_3 = Z/2.
  - Def. 1 / Prop. 1 e) is false in both directions. Its true form: over k regular noetherian, L^! is bounded ⇔ the
    fibre rank functions are polynomial of bounded degree.
  - rk L^!_i = μ_i + μ_{i+1} + β_i + β_{i+1} + ν_i.
- **R3 (SA09-3, 137:40-56). The walking complex and the Σ-exact theorem.**
  - Additive functors out of the C^i are cochain complexes (Prop. 1).
  - The ink of Prop. 2 has the right pairing, Hom(x, C^{n+1}).
  - C^* is the universal cosimplicial object of k-additive Karoubian categories (Prop. 5).
  - The Σ-exact theorem holds with full faithfulness. Over a principal ring that is not a field, the essential image
    needs the kernels of (x, y) ↦ (dx − ny, dy) for non-units n, besides those of the d^i.
- **R4 (SA09-4, 137:65-72).** The multiplicative extension exists, completing the step that the Pro notes M08 left
  open. Tot(C^• * C^•) gives a graded-commutative cup product on H^*(C^•).
- **R5 (SA09-5, 137:73).** The weight-n PD de Rham complex, transported by F, is homotopic to τ_{≤n}C^• by a unique
  homotopy class.
- **R6 (SA09-6, 137:75-86). Polynomial categories.**
  - The scalar action recovers the grading only after inverting the primes p with (p−1) | (n − n'): λ^n ≡ λ^{n'} mod p
    for all λ iff (p−1) | (n − n'). He rightly withdrew the uniqueness.
  - The axiom 1 ≅ Γ^q(1) ("Je l'avais oublié") does not follow from the others.
  - "Les deux notions sont donc en équivalence" is verified only for the homogeneous core.
- **R7 (SA09-11, 138:19, 36). The Kummer image.** For the Kummer torsor of 2, the image of Γ in Aff(1, Ẑ) has finite
  index and is not surjective. √2 ∈ Q(ζ_8), so the index is 2 at level 8. The Pro notes C07 found this first.
- **R8 (SA09-16, 138:98-100). Rigidity fails.** The category of pinned oriented maps is not rigid: the one-vertex torus
  map with E = Z/4 and σ = +2 has a pinned automorphism of order 2. His count needs the orbit-size form.
- **R9 (SA09-17, 138:104-112). The small Belyi maps.**
  - The enumeration in S_6 gives 3 maps of passport [3,2,1; 2,2,1,1; 6]; his tables list two.
  - His roots of δ(c) = 25c² − 32c + 16 are wrong. They are 16/25 ± (12/25)i.
  - The computation of the cubic P(c) for z³(z−1)²(z−c) is not finished on the page.
- **R10 (SA09-18, 138:129-131). Automorphisms of maps.** The orange of order n is preserved by every z ↦ az with a > 0.
  So "pas d'automorphismes hol. ≠ id" is false, the exception list is incomplete, and the groups in cases I-III are real
  groups, not Aff(1, ℂ).

## Results of RESEARCH_SA08 that this prompt builds on (added 19 Nov 2026)

Added by Claude Opus 5.5 at effort max (agent a34c04448e8299803) from its intake of RESEARCH_SA08. That run, by GPT-6
Astra (ChatGPT Pro mode), worked on cote 136, the divided-power de Rham complex that cote 137 builds on. Cite its
results by statement id. Each row of `SA08_RESULTS_20261119.md` says what was checked, by the run and by the intake.
Check each result you use as you use it, and record that check in CHECK_EVENTS.tsv.

They settle no item of this prompt outright. They place Part A as follows; Part B is untouched.

**Changed: restate these before you work on them.**
- **A.3.** Cote 136's weighted PD cochains already recover RΓ(X, Z) with its product, and H^*(X, Z) (D006); the E∞
  cochain algebra after enhancement (D006E); and the integral weak homotopy type of a nilpotent space of finite type
  (A-018, D006M, through Mandell 2006). Their comparisons with Horel, Toën, Cartan, numerical spaces and filtered
  circles are A-019. R5 transports the weight-n PD de Rham complex to τ_{≤n}C^•. So A.3 is now: determine whether
  that transport carries the cup product of R4 and the Γ-operations of A.1, prove it or show where it fails, and
  derive from D006E and A-018 what C^*(X, Z) recovers. Answer his question of 137:39 and L2 on that basis.
- **No binomial filtration.** There is no natural, exhaustive, filtered numerical cochain algebra over Int(Z), with
  R-bilinear products, whose associated graded is the PD cochain algebra compatibly with coefficients (A-026; the
  intake checked both parts). The coefficient statement gr Int(Z) = Γ_Z(T) holds (A-015); the ordinary numerical
  associated graded is A-017; a weaker total and shadow lift exists (D-026); T = 1 gives Sullivan's polynomial forms
  (A-025). In A.3, compare C^*(X, Z) with Horel's binomial rings through these, not through a filtered lift.
- **Literal and graded cochains.** For infinite X they differ (A-002 to A-004). Say which one each statement of
  cote 137 means.

**Tools for the other items of Part A.**
- **A.1.** The natural PD laws on a convolution algebra Hom(A, J) are given by an explicit equation set P(A) (D007).
  A flat coalgebra has exactly one (D008); a finite nonflat coalgebra over Z/4 has none (D009); the two relations of
  136/324 do not determine them (D010, D011); the dual laws are the typed divided copowers (D012). On 136/334 his
  coefficient for γ^p(γ^q(x)) is the one for the opposite order; the right one is (pq)!/(p!(q!)^p) (correction D-C15
  of RESEARCH_SA08). Check the composition through α_{q,p} on 137:75-86 for the same slip.
- **A.4.** Slice acyclicity of a simplicial module is normalized acyclicity (C02). A flat tensor-universally flasque
  simplicial module need not be additively contractible (C03, C04). Positive divided and exterior powers of flat
  acyclic simplicial modules are flat tensor-universally flasque (C05). These bear on "flasque" in Lemma 2 and on
  "ils seront même str. spéciaux!" (R2).

**Added from RESEARCH_SA08.**
- **A.5** carries over that run's one open mathematical item, his uniqueness conjecture for admissible generalized
  de Rham theories over Z (cote 136, scans 117-121). Cote 137's universal objects (C^*, the Σ-exact property, the
  Γ-operations) are tools that run did not have.
- **A.6** is a check of that run's refutation of a published proposition (D-031).

**Open:** A.1-A.6 and B.1-B.4, with the restatements above, and the Leads L1-L5 as they stand.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** His polynomial categories (137:75-86) are the categories ΓP of strict polynomial functors (Friedlander-Suslin
  1997), with P_n(X,Y) = Hom(Γ^n X, Y) and composition through α_{q,p}. His closing question, whether f ↦ Γ^p(f) is a
  polynomial law on the Hom modules, has a positive answer, and it is what makes them ΓP.
- **L2.** Cote 137 holds a complete integral model of "cochains with divided powers": the Γ-operations of 137:75-86
  acting on the universal cosimplicial object C^*. The "structure supplémentaire" of 137:38 is that action.
- **L3.** The Σ-exact theorem (137:51) is the universal property of the Frobenius category of bounded complexes of free
  modules, whose stable category is K^b(free). With the corrected essential image, it holds over every principal ring.
- **L4.** The index of the Kummer image for 2 is exactly 2 at every level divisible by 8, and the same index-2
  phenomenon governs the Galois image on the torsor K(1/2) of the Fermat-tower fibres (138:35-41).
- **L5.** The three trees of passport [3,2,1; 2,2,1,1; 6] form a single Galois orbit, with a cubic field of moduli
  cut out by his polynomial P(c).

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most
of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the
smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach
stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter
search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then
push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided
step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for all rings proved over
a field without saying so; a count for all degrees checked in small degree without saying so; a step that replaces a
claim by a convenient special case without naming it; a reading of the manuscript taken on trust where the mathematics
depends on it (the transcriptions are AI-made and carry doubt marks: where a step depends on a doubtful reading, say so
and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA09_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Cote 137. The main question is A.1.**
- **A.1 (main).** Determine the relation between his polynomial categories (137:75-86) and the strict polynomial
  functors of Friedlander and Suslin. Prove L1, or refute it and give the correct statement with its proof. This
  includes:
  - his closing question, whether f ↦ Γ^p(f) is a polynomial law on the Hom modules;
  - his claim "Les deux notions sont donc en équivalence", between strict polynomial categories and
    "⊗-pd-catégories", beyond the homogeneous core;
  - the independence of the axiom 1 ≅ Γ^q(1), shown by a model in which the other axioms hold and this one fails;
  - the role of the grading as data (R6).
- **A.2.** Prove or refute L3. Determine the essential image of the Σ-exact theorem over every principal ring, and
  over every commutative ring if the statement extends, with proofs (R3).
- **A.3.** Prove or refute L2, and answer his question of 137:39. What does C^*(X, Z), with the cup product of R4 and
  the Γ-operations of A.1, recover of a nilpotent space X of finite type? Prove the statement against Mandell's E∞
  theorem, Toën's affine stacks and Horel's binomial rings.
- **A.4.** Prove the corrected form of Def. 1 / Prop. 1 e) (R2) over every regular noetherian ring, and determine what
  holds over a non-regular ring.
- **A.5 (carried over from RESEARCH_SA08, its item C.3).** His uniqueness conjecture for admissible generalized de
  Rham theories (cote 136, scans 117-121: "connexe et simplement connexe ?", conjectures a) and b)), over Z. Prove it
  or refute it over Z, with the correct statement proved in its place.
  - **Settled by RESEARCH_SA08.** Strict common-source equalization, the strict form of b), fails over every nonzero
    ring (C07). The special universally flasque category has a contractible nerve (C06); so does the eventual
    admissible category over a Q-algebra under uniform hypotheses (C08). Common sources and terminal localization
    hold for explicit eventual-admissible theories over Z_(p)-algebras and over rings of positive characteristic (C09,
    C10), and for generalized admissible strict PD theories over every ring with finitely many noninvertible rational
    primes (C16, C17).
  - **The item.** Common sources and terminal localization over rings with infinitely many noninvertible primes,
    beginning with Z. Keep the two assertions apart.
  - **The gate, as that run left it.** C30 builds a common source over Z from p-local admissible repairs
    P_p → E_p → A_p, B_p whose first map is an isomorphism below a form degree d_p, with d_p → ∞. C32 builds terminal
    localization in the same way from local repairs of the pair target A ×_k B and of the homotopy equalizer H(f, g).
    C34 weakens the data to the finite form truncations of P with compatible target maps. None of these local
    completions is constructed, and neither their existence nor their necessity is proved.
  - **What was tried, and where it failed** (statement ids of that run):
    - ordinary tensor products: prime-power Tor in unbounded weights (C11);
    - independently marked free PD disks over Z: admissible only for the weight-one disk, and no map to A_N for
      N > 1 (D022, D023);
    - projection-preserving arithmetic gluing with unbounded first flasque weights (C12);
    - the standard tails as an initial family (C13);
    - free linear-disk replacements and free resolutions of the tails (C14, C15);
    - ordinary common-target pushouts: unbounded degree-one cohomology, even rationally (C19);
    - naive PD indecomposables, which are not invariant (C26), and a simple arity-homology pattern (D032);
    - delayed p-local closures, which come without compatible target maps (C18);
    - the global partial model, which needs floor((d+1)/2)! inverted (C21);
    - automatic extension of a prescribed bar boundary: a counterexample over Z_(2) (C31);
    - adjoining rational halves of odd products (C35);
    - the finite-arity bar extensions (C24, C25, C27-C29, C36), which do not meet infinitely many eventual bounds at
      once;
    - a fixed finitely generated group of operations as the invariant: it cannot detect moving primes (C33);
    - the lifting proposition of Caradot and Lin as stated (D-031; see A.6).
  - **What this prompt adds.** Cote 137 builds the universal cosimplicial object C^* = DP(C^•), its Σ-exact universal
    property (R3, A.2) and the Γ-operations (A.1, A.3). Determine whether they give the common source or the terminal
    object over Z, or an invariant that separates admissible theories.
  - **Where that run's state is,** in `SA08_final_paper_tex.zip`: `notes/C_findings.md`,
    `notes/C_finite_prime_proof.md`, `notes/C_global_partial_model.md`, `notes/C_local_completion_attempts.md`,
    `notes/C_terminal_repair_reduction.md`, `notes/D_arithmetic_repair_gluing.md`, `notes/D_global_local_repair_gate.md`,
    `notes/D_final_local_repair_attempts.md`, `notes/B_C3_completion_after_C34.md`, and the other `notes/B_C3_*`,
    `notes/C_*` and `notes/D_*` files they cite; the matching files in `sections/`; the C and D022-D032 rows of
    `RESEARCH_SA08_results.csv` and of its `CHECK_EVENTS.tsv`; the reviews of 08:21-10:21 UTC in its
    `PROGRESS_LEDGER.md`; and the section "Proved obstructions, approaches and remaining gates" of its
    `RESEARCH_SA08_report.md`.
- **A.6 (a check carried over from RESEARCH_SA08).** That run refutes Proposition 3.10 of A. Caradot and Z. Lin,
  "Differential graded algebras with divided powers and homotopy Lie algebras", arXiv:2511.22614v4: its statement
  D-031, "unrestricted termwise-free chain-map lifting is false", proved in `sections/D_rejected_lifting_source.tex`,
  with the program output `logs/D_lifting_counterexample.json`. The counterexample is an explicit square-zero PD DGA
  projection from an identity disk to its lower-degree sphere, whose closed generator has no chain lift. The run
  states that their Theorem 3.15, which assumes an acyclic target resolution, is not refuted. Check this
  independently:
  - fetch the arXiv LaTeX source of v4 and quote, with section, page and equation numbers, the exact statement of
    Proposition 3.10, the definitions it uses (termwise freeness, Section 2.1) and the degree conventions;
  - verify every hypothesis of Proposition 3.10 on the counterexample, and the impossibility of the lift, by hand and
    by a program;
  - determine which results of that paper use Proposition 3.10, Theorem 3.15 included, and whether the counterexample
    reaches them;
  - determine the hypothesis under which the lifting of Proposition 3.10 holds (an acyclic or cofibrant one, for
    instance), and prove that corrected statement.
  The item is done when the refutation is confirmed with these locators and the corrected statement is proved, or
  when the refutation is shown wrong at an exact step. Record the check under the statement id D-031 in
  CHECK_EVENTS.tsv.

**B. Cote 138.**
- **B.1.** Determine the number of pinned oriented maps of a given type, as an orbit-size formula valid when rigidity
  fails (R8), and prove it. Correct his "(classes of admissible E) × ∏ a_n!b_n!c_n!" (138:98-100), and say exactly when
  his form holds.
- **B.2.** Determine the three maps of passport [3,2,1; 2,2,1,1; 6] (R9):
  - their Belyi functions;
  - the polynomial P(c) for the family z³(z−1)²(z−c);
  - the field of moduli of each, and the Galois action on the three.

  Prove L5 or refute it. Finish his computation of 138:106-112, with the signs he left in doubt.
- **B.3.** Determine the group of holomorphic automorphisms of every map in his classes I-III (138:129-131) that
  preserves it cell by cell, give the complete exception list, and prove both (R10).
- **B.4.** Prove or refute L4. Determine the image of Γ = Gal(Q̄/Q) in Aff(1, Ẑ) for the Kummer torsor of 2, and for
  the torsors E(α'(i)) of 138:35-41, with the index at every level. For ξ_1, …, ξ_n multiplicatively independent modulo
  roots of unity (138:20), state and derive from the cited theorems the openness of the image in Aff(n, Ẑ).

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- E. Friedlander and A. Suslin, "Cohomology of finite group schemes over a field", Invent. Math. 127 (1997), §2.
  A. Touzé, his papers on strict polynomial functors. H. Krause, "Koszul, Ringel and Serre duality for strict
  polynomial functors". N. Roby, "Lois polynômes et lois formelles en théorie des modules", Ann. ENS 80 (1963).
- A. Dold and D. Puppe, "Homologie nicht-additiver Funktoren", Ann. Inst. Fourier 11 (1961). D. Happel, *Triangulated
  categories in the representation theory of finite dimensional algebras* (Frobenius categories).
- M. Mandell, "Cochains and homotopy type", Publ. Math. IHÉS 103 (2006). B. Toën, "Le problème de la schématisation de
  Grothendieck revisité", Épijournal Géom. Algébrique 4 (2020). G. Horel, "Binomial rings and homotopy theory".
- L. Schneps (ed.), *The Grothendieck Theory of Dessins d'Enfants* (1994). S. Lando and A. Zvonkin, *Graphs on Surfaces
  and Their Applications* (2004). G. Jones and J. Wolfart, *Dessins d'Enfants on Riemann Surfaces* (2016).
- S. Lang, *Algebra*, ch. VI §9 (Kummer theory). K. Ribet, "Kummer theory on extensions of abelian varieties by tori",
  Duke Math. J. 46 (1979). M. Bashmakov on the Kummer theory of independent elements.
- G. Belyi, "On Galois extensions of a maximal cyclotomic field" (1979).
- A. Caradot and Z. Lin, "Differential graded algebras with divided powers and homotopy Lie algebras",
  arXiv:2511.22614v4 (A.6): Section 2.1, Proposition 3.10, Theorem 3.15. For A.5, the sources that RESEARCH_SA08
  cites are in its `RESEARCH_SA08_references.bib` and `notes/*.bib`, with that run's notes on which it opened.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the base ring and its characteristic, the categories and their axioms,
   the passport and the pinning). Do not replace it by a convenient special case. If you prove a special case, name it
   as one and keep the general statement on your list.
2. Type every map and functor you introduce: source, target, the category in which it lives, and each extra property
   you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by") comes with its comparison map and a proof that the exact property
   needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; equivalence of categories; isomorphism of maps with
   and without pinning; the field of moduli against a field of definition.
5. Check the edge cases in scope: characteristic 2 and the primes p with (p−1) | (n−n'); principal rings that are not
   fields; degree 0 and 1; maps with non-trivial automorphisms; the levels 2, 4 and 8 of the Kummer tower; Z and the other rings with infinitely many
   noninvertible primes (A.5).
6. A counterexample is given completely and, when finite, checked by a program whose code and output you attach. One
   verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep
   the two apart.
7. No authority. Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, the results of RESEARCH_SA08, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Known results are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never
   invent a reference; mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper
   (the arXiv e-print) where one exists.

## What to deliver

One ZIP containing:
- `RESEARCH_SA09_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA09_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA09_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA09_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted,
  with the statement number); then what you read, what you computed (every program with its scope, counts and run time),
  and every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry item ids such as SA09-2 with the cote and scan; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA09_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.

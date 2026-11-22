# RESEARCH_SA07: Grothendieck's periods dossier (cote 18). The period triangle of 18:11 and the Hodge splitting of elliptic curves (18:13), his comparison programme of 18:5-6 and 18:43, motives over R and the real Frobenius (18:31-41), Betti lattices under changes of place (18:42-62), and the reconstruction of places from fibre functors (cote 15)

To be settled: Grothendieck's period triangle of 18:11, the main question (Part A). For a motive `M` over a field
`k ⊂ Q̄ ⊂ C` with motivic group `G`, decide which of his transcendence-degree statements hold for the comparison points
`α` (Betti-de Rham), `β` (the Hodge splitting) and `γ` (Hodge-Betti) and for the period points `φ ∈ Fil` and `ψ ∈ Big`,
and determine the correct values; a lead says that his "Conj. de transcendance forte", `trdeg_k k(α, β) = g + u`, fails
for every motive with a real model and `u > 0`. With it, his test case 18:13 for elliptic curves over `Q̄`, above all
his question whether the Hodge splitting of a curve without complex multiplication can be algebraic. Then: his
comparison programme of 18:5 and 18:43 ("Par quoi remplacer 1′, 4′ ??", the question later called the mysterious
functor) and the two splittings of 18:6 (Part B); motives over `R` and the real Frobenius, 18:31-41 (Part C); Betti
lattices under changes of place, his bounds of 18:45-49 and the cocycles of 18:53-62 (Part D); the reconstruction of
places from fibre functors, cote 15 (Part E); cycle classes, 18:9, and every remaining open step of the notes (Part F).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA07`.
Drafted on 19 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), agent a922466087ec53798, a sub-agent of the main
session, at the main session's word, from the sweep-3 study of the topic SA07 (Claude Opus 5.5 at effort max, agent
a28ea31fa17dd65e1), the literature check of the cluster (agent a922466087ec53798) and the AI-produced transcriptions of
his pages.

Citations: "18:11" is cote 18, scan 11 (the archive's sheet number is the scan number minus one; the notes files write
`18/011`). Item ids (SA07-1, SA07-2, ...) are those of `sweep2_SA07/WHAT_IS_WHERE.md`. The two notes files of the
transcriptions use overlapping ids, so a note id is given with its file: "[I]" is
`MPL_15_195-228+18_002-017_notes.md` (cote 15, scans 195-228, and cote 18, scans 2-17), "[II]" is
`MPL_18_018-062_notes.md` (cote 18, scans 18-62). Example: P15 [I], RH10 [II].

## What is attached

One file, `RESEARCH_SA07_background.zip` (1.7 MB, 227 files; LaTeX and text only, no PDF); `MANIFEST.tsv` at
its root lists every file with its origin, size and SHA256, and `README.md` maps the folders.
- `sweep3_SA07/`: `STUDY.md` (§1 the programme, 18:4-5, 18:10, 18:42-43; §2 cycle classes and `2iπ`, 18:15-29; §3 motives
  over `R` and the real Frobenius, 18:31-41; §4 periods, 18:6, 18:11-13, 18:45, 18:47-49; §5 mixed Hodge structures,
  18:9), `HUNCHES.md` (H1-H7), `RESEARCH_PACKAGES.md` (RP-SA07-1 to -3), the check events, corrections, deliverables and
  dependencies of the topic, and `LITERATURE_CHECK.tsv` (every literature locator of the topics SA05, SA06, SA07 and
  SA15, checked against the source, with the correct locator).
- `sweep2_SA07/`: `WHAT_IS_WHERE.md` (the items SA07-1 to SA07-20 and their places), `OBJECTS.tsv`, `FLAGS.tsv`,
  `DEPENDS.tsv`.
- `transcriptions/`: the AI-produced transcription (GPT-6 Astra, ChatGPT Pro mode) of every page of the two packages, one
  TeX file per scan (`<package>_<cote>_scanNNN.tex`), with the research notes, the open readings and the inventory of the
  same runs. Notes [I] have the entries A01-A41 (cote 15), P01-P33, M01-M11, B01-B05 and X01-X03, and the table of the
  steps he leaves to check ("Standing question I"); notes [II] have C01-C08 (cycle classes), RH03-RH20 (real structures),
  P01-P26 (periods, lattices, cocycles), MB01-MB16, R01-R20 (reused typescripts) and SF01-SF36 (every step he marks as
  unverified, withdrawn or checked). `PREAMBLE.tex` defines the macros (`\unsure{a|b}` a doubtful reading with its
  alternatives, `\deleted` struck by him, `\inserted` his insertion, `\margin` margin text, `\scanpage{N}` scan N,
  `\mspage{n}` his page number).
- `transcriptions_chatB/`: the notes, open readings and cote-18 pages of a second Pro run on the first package, a second
  witness.
- `codex_web/`: the transcriptions and notes of cotes 10, 16 and 19 (GPT-6.2 Astra at reasoning effort max, ChatGPT
  Work), attached for the connections (for instance the Lefschetz `sl_2` of cote 16 against the motivic group, MB03-MB06
  [II]); these cotes are not Parts of this prompt.
- `broad_layer/`: the sweep-3 studies, hunches and research packages of the other topics of the motives and crystals
  cluster (SA05, SA06, SA15), their item lists and their merged readings, so that you see the connections: SA05-8 and
  SA05-18 (the motivic Galois group and the gerbe of `F_p`), SA06-10 (real fibre functors), SA15-15 (p-adic cohomology,
  cote 7: problem 4 of 18:43 is the cote 7 draft), SA15-18 (Tate-Hodge questions, cote 6).
- `hua_project/`: the modernised reading of cote 18 by Michel Hua's project, a witness only; credit any remark you use to
  "Michel Hua's project", quoting a phrase.
- `literature/`: LaTeX sources of André, "Galois theory, motives and transcendental numbers"; Bost-Charles, "Some remarks
  concerning the Grothendieck period conjecture"; Brown, "Notes on motivic periods"; Huber-Wüstholz, "Transcendence and
  linear relations of 1-periods"; Huber-Müller-Stach, "On the relation between Nori motives and Kontsevich periods";
  Charles-Schnell, "Notes on absolute Hodge classes"; Charles, "Conjugate varieties with distinct real cohomology
  algebras"; Bhatt-Morrow-Scholze, "Integral p-adic Hodge theory"; Berger, "An introduction to the theory of p-adic
  representations"; Scholze, "p-adic Hodge theory for rigid-analytic varieties"; Bhatt-Scholze, "Prismatic F-crystals and
  crystalline Galois representations"; Bhatt, "Algebraic geometry in mixed characteristic".

Not attached: the scans (the transcriptions are our reading of them; where a reading matters and is in doubt, say so)
and every other source named below. Open each source you use and cite it with its exact theorem numbers.

## Where this comes from

- Grothendieck's cote 18 in the Montpellier archive: his notes on motives over number fields, over local fields and over
  `R`. The cover 18:4 reads "Motifs et cristaux sur corps local"; 18:5 "Descriptions conjecturales des motifs sur corps
  de nombres k"; 18:43 "Pbs". 18:9 uses the conventions of Hodge II (`W` increasing, `F` decreasing), so these pages are
  of 1970 or later. Interleaved with his pages are reused typescripts: Bourbaki drafts ("Tribu n° 59, Systèmes de
  racines", n° 370 on Haar measure, n° 392 on valuations, n° 413 on formal kernels and distributions) and a translation
  of a paper on direct images (18:44). The typescripts and the editorial remarks on them (SF01-SF09, SF20, SF23 and
  R01-R20 [II]) are not part of this prompt.
- Cote 15, scans 207-227: his pages on reconstructing varieties and places from fibre functors (SA07-1), written among
  reused Lie-theory typescripts.
- The transcriptions: AI-produced by GPT-6 Astra (ChatGPT Pro mode); the first package also by a second Pro run (chat
  B); cotes 10, 16 and 19 by GPT-6.2 Astra at reasoning effort max (ChatGPT Work).
- The sweeps, all by Claude Opus 5.5 at effort max: sweep 2 placed the items; sweep 3 (18 Nov 2026) read every page of
  his hand in cote 18 and worked the mathematics through (agent a28ea31fa17dd65e1); the literature check of 19 Nov 2026
  opened the sources named in the four topics' files (agent a922466087ec53798).

## Results this prompt builds on (status on 19 Nov 2026)

None of these is to be proved again as if open, except where a Part requires it. For each one you use: read the argument
at the place given and confirm the step you rely on in a paragraph of your own, or give the exact error with a repair or
a counterexample. All are by Claude Opus 5.5 at effort max (the agents named above) and unrefereed; their check events
are in `sweep3_SA07/CHECK_EVENTS.tsv`, and the corrections to sweep 2 (SA07-2 refined, SA07-6 made precise) in
`sweep3_SA07/CORRECTIONS.tsv`.

- **R1 (18:15-25; `STUDY.md` §2; check events at 18:17 and 18:21-23).** For a cycle of codimension `p` on a smooth complex
  variety, the analytic (de Rham) fundamental class and the topological one satisfy `P_an = (2iπ)^p P_top`: in
  codimension 1 by the residue of `dz/z` on a disc (`λ = ∮ dz/z = 2iπ`, 18:15-17), in codimension `p` by the local product
  of `p` transverse discs; for a proper map of relative codimension `p`, `f_*^top` corresponds to `(2iπ)^{−p} f_*^an`
  (18:23). Known: Deligne, "Hodge cycles on abelian varieties", LNM 900 (1982), §1. The global form, the orientations of
  18:27-29 and the correspondences of 18:25 are Part F.1.
- **R2 (18:36, 18:38; `STUDY.md` §3; check events at 18:36 and 18:38).** `ε(f_∞) = −1`: complex conjugation reverses the
  orientation of `P¹(C)`, so it acts by `−1` on `H²(P¹(C), Q) = Q(−1)_B`; it acts on `Q(n)_B` by `(−1)^n`, so `f_∞` is
  trivial on the tensor powers of `Q(2)`. Only this direction was checked. The converse, "f_∞ = 1 seulement si M est somme
  de puissances tensorielles de Q(2)" (granting Hodge), is Part C.3, where RH10 [II] gives a counterexample to check.
- **R3 (18:11; `STUDY.md` §4; check event at 18:11).** The numbers of his transcendence-degree list are consistent with
  each other and with the dimensions (`b = u + l`; `dim Big = g − l = (g − b) + u`; `trdeg_k K = g + u` computed from `α`,
  from `β` and from `γ`). This is internal consistency only: Lead A says the list fails for motives with a real model
  (Part A.2).
- **R4 (18:49; `STUDY.md` §4; check event at 18:49).** His lemma is true: for `G` connected over `Q` and `U` a compact open
  subgroup of `G(Q̂)`, every coset `U a` contains an element each of whose components is generic over `Q` (the proper
  `Q`-subvarieties are countable, and each meets `G(Q_ℓ)` in a Haar-null set). The topology of the product he writes
  (P05 [II]) is to be fixed where the lemma is used (Part D.3).
- **R5 (18:9; `STUDY.md` §5; check event at 18:9).** His Tate twist of a mixed Hodge structure, `W_i(E(n)) = W_{i+2n}(E)`,
  `F^i(E(n)) = F^{i+n}(E)`, agrees with Deligne, "Théorie de Hodge II", Publ. Math. IHES 40 (1971), (2.1.13). The graded
  formula as transcribed, `Gr^W_i(E(−1)) = (Gr^W_i E)(−1)`, has unshifted indices; under those conventions
  `Gr^W_i(E(−1)) = (Gr^W_{i−2} E)(−1)` (P09 [I]). Part F.2.
- **R6 (the literature check; `sweep3_SA07/LITERATURE_CHECK.tsv`).** Grothendieck's period conjecture is known for a CM
  elliptic curve: Chudnovsky (1976) proved that `π` and a period of such a curve are algebraically independent, so its
  period field has transcendence degree 2, the dimension of the CM torus. It is open for CM abelian varieties in general:
  Wüstholz's analytic subgroup theorem ("Algebraische Punkte auf analytischen Untergruppen algebraischer Gruppen", Ann.
  of Math. 129 (1989), 501-517) gives only the linear relations among periods (Huber-Wüstholz, Transcendence and Linear
  Relations of 1-Periods, Cambridge Tracts 227, 2022). For an elliptic curve over `Q̄` without CM, two of
  `ω_1, ω_2, η_1, η_2` are algebraically independent (Chudnovsky, ICM Helsinki 1978); the value 4 that the period
  conjecture predicts is open. Nesterenko
  ("Modular functions and transcendence questions", Mat. Sb. 187 (1996)): `trdeg Q(q, E_2(q), E_4(q), E_6(q)) ≥ 3` for
  `0 < |q| < 1`. The table gives the checked locator of every source named in the sweep files.

## Leads

Each is an inference of the model named, checked by no one. Each is to be proved or refuted in full, inside the Part it
serves.

- **Lead A (A.2; Claude Opus 5.5 at effort max, agent a922466087ec53798, while drafting this prompt).** Let `M` have a real
  model: `M = M_0 ⊗_{k_0} k` with `k_0 ⊂ k ∩ R`. The real Frobenius `f_∞` of `M_0` maps `H^{p,q}` to `H^{q,p}`, so the
  complex conjugate of the Hodge filtration is its image under the rational involution `f_∞`: `φ̄ = f_∞ φ` in Betti
  coordinates, and `F̄ = (α f_∞ α^{−1})(F)` in de Rham coordinates. Hence `ψ` is rational over `Q(φ)`, `β` and
  `γ = (βα)^{−1}` are rational over `k(α)`, and `K = k(α)`. As soon as `u > 0`, his statements `trdeg_k K = g + u`,
  `trdeg_{k(α)} K = u` and `trdeg_Q Q(ψ) = g − l` fail, unconditionally, and neither the pair `trdeg_k k(γ) = g`,
  `trdeg_{k(γ)} K = u` nor the pair `trdeg_k k(β) = u`, `trdeg_{k(β)} K = g` can hold. Example: `h¹` of an elliptic curve
  over `Q` without CM (`g = 4`, `b = 3`, `u = 1`, `l = 2`): the lattice is stable under conjugation, so `ψ = (τ, τ̄)` with
  `τ̄` an integral Möbius transform of `τ`, `trdeg_Q Q(ψ) = trdeg_Q Q(τ) = 1` (Schneider: `τ` is transcendental) while
  `g − l = 2`, and `trdeg_Q K ≤ 4 < 5 = g + u`. Proposed correct form: the transcendence degrees are the dimensions of the
  images of the period torsor of `M ⊕ c^*M` (`c` complex conjugation), and `g + u` is the prediction only where that image
  fills `P ×_k Q`.
- **Leads H1-H7 (`sweep3_SA07/HUNCHES.md`, Claude Opus 5.5 at effort max, agent a28ea31fa17dd65e1):** H1 (A.4 c: the
  Hodge splitting of an elliptic curve over `Q̄` is algebraic exactly in the CM case), H2 (A.2: the `β`-part of 18:11 is
  the period conjecture for the periods together with their complex conjugates), H3 (B.4: 18:6 is an early form of Sen's
  theorem), H4 (G.2: 18:5 is the earliest written form of the mysterious-functor problem), H5 (D.2: a two-embedding period
  conjecture, with equality in his bound for generic data), H6 (D.3: his adelic genericity is a theorem for elliptic
  curves without CM and their products), H7 (C.2: the twisted Betti functor is tensor-isomorphic to Betti over `C` but not
  over `Q` in general), each as stated there.
- **Leads of the research notes of the transcription runs (GPT-6 Astra, ChatGPT Pro mode).** In notes [II]: RH06 (the
  naive tensor comparison of the twisted Betti functor has a sign defect on `V^− ⊗ U^−`), RH07 (on the Artin subcategory
  no tensor isomorphism between the twisted functor and Betti exists over `Q`, since it would give `−q² = 1`), RH10
  (`A ⊗ Q(−1)`, `A` the sign Artin motive of `C/R`, has `f_∞ = +1` and weight 2), RH16, RH19, P04 (the bound `(n − 1)d`
  from the relative-position quotient), P05, P09 (the approximation condition fails for `G_m`), P13, P21, P22, P26 (the
  image of `φ` against the subgroup it generates). In notes [I]: P06 (`Ker u = Ker χ ∩ Ker φ` needs `Ker u ⊂ Ker χ`), P11,
  P13, P23 (generation of the period locus, with a theorem of Kreutz et al. that we have not checked), P24 (Katz's later
  question, as the notes cite it: Katz, "p-adic interpolation of real analytic Eisenstein series", Ann. of Math. 104
  (1976), Question 4.0.8), P32, P33, A11, A34, A35, A37, A38, X01-X03.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (the motive, variety, field, embedding, group, torsor or cocycle given completely, with the
verification of every hypothesis and of the failure; checked by a program when finite or computable) and the strongest
true statement proved in its place. Nothing else finishes an item. Partly settled is not an outcome. The cases proved,
the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an
item you are still working on: record them as you go, then attack the obstruction, starting from that instance.
"Known" counts only with the derivation of the statement used here from the cited theorem, after opening the source.
Known results (published work, textbooks) are cited with their exact theorem numbers and not re-proved; the only proof
you give of one is the short derivation of the form used here when the source does not state that form.
An item that begins with "Determine" is done when the object asked for is given explicitly, with a proof that it is
the whole answer. An item that asks what follows from a named conjecture is done by a theorem of the form "if the
conjecture holds for `N`, then ...", proved in full, together with every unconditional statement the item asks for.

For Part A in particular.
- A transcendence-degree statement names its base field (`k`, `k(π)`, `Q`), the embedding of `k` in `C`, the motive, the
  category of motives, the motivic group, and whether it is unconditional or conditional on the period conjecture for a
  named motive, in a form you state with its source (André, Une introduction aux motifs, 2004, §7.5; Bost-Charles,
  Conjecture 2.12).
- For each statement of his list, say which reading of the page it uses (P11, P13, P17 [I]: the two descriptions of `Q`,
  the direction of `F → Φ`, the denominator `K|k` on 18:11), and decide it under every reading the transcription leaves
  open.
- Every computation (period matrices, values of `E_2^*`, `E_4`, `E_6`, Hodge splittings of explicit curves, numerical
  tests of algebraic relations) is given with its program, inputs, precision and output, and with a proof of what it
  shows.

For Parts B and C. A comparison theorem is stated with every hypothesis (residue field perfect or not, absolute
ramification, good, semistable or potentially semistable reduction, `p = 2` included or not), the period ring, the
functor and the categories, and the step from the published statement to his description. Over `R`, name the category of
motives, the convention for `f_∞` (Deligne, "Valeurs de fonctions L et périodes d'intégrales", Proc. Sympos. Pure Math.
33, part 2 (1979), 313-346, 0.2.5, or its inverse; on cohomology or on homology), and whether a group is the Tannakian
group over `Q` of motives over `R` or over `C`.

For Parts D and E. Name the topology of every product of local groups (full product or restricted product), the group of
field automorphisms acting and its topology, and whether a place is an embedding or an embedding up to complex
conjugation.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1-R6 again in place of the
items, except where a Part asks for it; a result of the sweeps or the notes used without the check above; a statement
for all motives (all `k`, all places) proved for some, without saying so; a step that replaces a claim by a convenient
special case without naming it; a reading of his pages changed to fit the mathematics without saying what the
transcription reads and why you read it otherwise.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA07_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The period triangle of 18:11 and its test case 18:13 (SA07-2; `STUDY.md` §4; RP-SA07-1, RP-SA07-2). The main question
is A.2, with A.4 c).**

Setting (18:10-13; P10-P26 [I]): `M` a motive over a field `k ⊂ C` (`k ⊂ Q̄` for the strong conjecture), `G` its motivic
group, `g = dim G`; the fibre functors `T_B` (Betti, over `Q`), `T_DR` (de Rham, over `k`) and `T_Hdg` (Hodge); the
torsors `P = Isom^⊗(T_B ⊗ k, T_DR)`, `P′ = Isom^⊗(T_DR, T_Hdg)` and `P″ = Isom^⊗(T_Hdg, T_B ⊗ k)`; `B′ ⊂ G` the
stabilizer of the Hodge filtration (dimension `b`), `U′` its unipotent radical (dimension `u`), `L′` a Levi subgroup
(dimension `l`); `Q ⊂ P′` the variety of Hodge splittings; `Fil` (dimension `g − b`) and `Big` (dimension `g − l`) the
varieties of filtrations and of bigradings of `T_B` in the class of the Hodge ones, `Big → Fil`; the points `α ∈ P(C)`,
`β ∈ Q(C)` and `γ ∈ P″(C)` with `βα = γ^{−1}`, `φ = q(α) ∈ Fil(C)`, `ψ = r(γ) ∈ Big(C)`, and `K = k(α, β)`. His list:
`trdeg_k k(α) = g`, `trdeg_k k(β) = u`, `trdeg_k k(γ) = g`, `trdeg_{k(β)} K = g`, `trdeg_{k(α)} K = trdeg_{k(γ)} K = u`,
`trdeg_Q Q(φ) = g − b`, `trdeg_Q Q(ψ) = g − l`, and `trdeg_k K = g + u` ("Conj. de transcendance forte ... alors ?",
18:11, the lines the table of Standing question I [I] gives as L65-76).

1. (The objects.) Define every object of the setting from the page, in a category of motives you name, and prove:
   `Fil` and `Big` are the homogeneous spaces `G/B′` and `G/L′` (with their forms over `Q`), `Big → Fil` is a torsor under
   a unipotent group of dimension `u`, `Q` is a torsor under `U′`, and `(2iπ)^n ∈ k(α)` when `Q(−n)` lies in the category
   generated by `M` ("(2iπ)^n ∈ k(α) si Q(−n) ∈ Ob M"). Settle the two descriptions of `Q` (P11 [I]: an `H′`-reduction
   with `dim H′ = u + 1`, against the space of Levi subgroups, of dimension `u`) and the direction of the margin map
   `F → Φ` (P13 [I]); say what `T_Hdg` is.
2. (His list; the main question.) Decide every statement of his list, as written, for every `M` over every `k ⊂ Q̄`:
   which hold unconditionally, which follow from Grothendieck's period conjecture for `M`, and which fail. Prove or refute
   Lead A. Then determine the correct value of each transcendence degree for every `M`: with `c` complex conjugation and
   `c^*M` the conjugate motive over `c(k)`, prove an unconditional upper bound for each by the dimension of the image of
   the period torsor of `M ⊕ c^*M` under the map you construct to `P`, `Q`, `P″`, `Fil` or `Big`; prove that equality in
   each follows from the period conjecture for `M ⊕ c^*M`; and compute that dimension from the motivic group of
   `M ⊕ c^*M` (a subgroup of `G × c^*G`). Decide in particular for which `M` the value `g + u` is the one predicted, that
   is, for which `M` the image fills `P ×_k Q`. Prove or refute Lead H2 on the way.
3. (Known cases.) Prove the corrected statements of A.2 unconditionally for every `M` for which the period conjecture for
   `M ⊕ c^*M` is known (R6). For elliptic curves over `Q̄`, decide unconditionally the statements on `φ` and on `ψ`:
   `Q(φ) = Q(τ)`, with Schneider's theorem after opening it, and `trdeg_Q Q(τ, τ̄)` for a curve not isogenous to its
   complex conjugate.
4. (His test case 18:13, with the cancelled drafts of 18:12, P18-P21 [I]: elliptic curves `E` over `Q̄`, with `G = GL_2` or
   the CM torus.) a) ("de degré de transcendance égal à dim G (4 ou 2) ?") Derive the CM case, `trdeg = 2`, from
   Chudnovsky (R6) in his normalization. For a curve without CM, a) is Grothendieck's period conjecture for that curve; it
   is not an item of this prompt. b) ("A-t-on H = G ?") Make his question precise (P23 [I]: the smallest algebraic subgroup
   containing a translate of the locus of the period point over `Q̄`) and decide it for every `E` over `Q̄`, with a
   complete proof; compare Bost-Charles, §2, and Wüstholz 1989, after opening them. c) ("Peut-on avoir h ∈ Q̄, ou h
   est-il tjrs transcendant sur Q [cas où C n'a pas de multiplication complexe]") With CM, prove that the Hodge splitting
   is algebraic and determine `h` explicitly in his normalization (Masser, Elliptic Functions and Transcendence, LNM 437,
   1975, after opening it). Without CM, decide whether `h` can be algebraic (Lead H1; P24 [I]). Express `h` through
   `ω_1, ω_2, η_1, η_2` and their complex conjugates, and through `E_2^*(τ) = E_2(τ) − 3/(π Im τ)` normalized by the
   period; for a curve with a real model, Lead A puts `h` in the field of periods of `E`, so that an algebraic `h` is an
   algebraic relation among `ω_1, ω_2, η_1, η_2` other than Legendre's. Decide whether such a relation can hold, for curves
   with a real model and for curves without one, with Chudnovsky's, Nesterenko's and Wüstholz's theorems after opening
   them and every further method you find.
5. (18:59, "conjecture de transcendance N° 1"; P16-P18, P24, P26 [II]; SF30, SF31 [II].) State his conjecture of 18:59
   exactly (the comparison point generic over `k_0`, and his reformulation by the Zariski density of the image of `φ_v`),
   prove its equivalence with the period conjecture in the torsor form of Bost-Charles, Conjecture 2.12, or refute it, and
   decide his reformulation (P26 [II]: the image against the subgroup it generates).

**B. His comparison programme: 18:5, 18:6 and 18:43 (SA07-2, SA07-3; `STUDY.md` §1 and §4).** This Part comes after Part
A and is governed by the same rules, the push rule and the three-hour check.

Setting (18:5): over a number field `k`, six "descriptions conjecturales" of motives: 1) "double viseur" Betti-De Rham,
2) Betti-Hodge, 3) Hodge structure (`k = Q̄`), 4) Betti-Gauss-Manin, 5) Betti-Tate, 6) "De Rham filtré cristallin". Over a
local field `K` (the fraction field of a complete discrete valuation ring with perfect residue field of characteristic
`p`), a "description conjecturale des groupes p-divisibles mod isogénie (plus généralement des pseudo-motifs)": 3′)
Hodge-Tate structure (a finite `Q_p`-module `N` with a bigrading of `N ⊗ C` after a finite extension), 2′) "double viseur
Tate-Hodge", 5′) the Galois module (written ℓ-adic: P05 [I]), 6′) "cristal filtré [vectoriel de dimension finie sur K, une
application σ-semilinéaire, et filtration]"; then "Par quoi remplacer 1′, 4′ ??". 18:43, "Pbs": 1) Betti and De Rham: a)
compare the De Rham and Betti lattices, b) compare Betti lattices for different topologies, c) compare real structures
and splittings in De Rham; 2) Betti and ℓ-adic: compare Betti lattices for different topologies inside ℓ-adic cohomology;
3) "comparaison possible entre cohomologie p-adique et cohomologie de De Rham ?" over a complete discretely valued field
of residue characteristic `p`; 4) "Définition de cohomologie p-adique en car p > 0 ?".

1. (The local descriptions; P01-P05 [I].) For each of 2′, 3′, 5′ and 6′, state the functor he describes (from which
   category: `p`-divisible groups over `K` or over its ring of integers, with good or potentially good reduction, up to
   isogeny; his "pseudo-motifs"), prove whether it is fully faithful, and determine its essential image, each with the
   derivation from the theorems you cite after opening them (Tate's theorem on `p`-divisible groups and the Hodge-Tate
   decomposition; Fontaine's rings; Colmez-Fontaine, "Construction des représentations p-adiques semi-stables", Invent.
   Math. 140 (2000), 1-43; Breuil's and Kisin's classifications of `p`-divisible groups, with the case `p = 2`). Settle the
   reading ℓ against `p` in 5′ (P05 [I]) and the qualifications "mod isogénie" and "après extension finie".
2. ("Par quoi remplacer 1′, 4′ ??") Determine what takes the place of 1) (the "double viseur" Betti-De Rham) and of 4)
   (Betti-Gauss-Manin) over `K`, and prove the statement in his notation: the comparison of the Galois module with the
   filtered module over a period ring, and its relative form over a `p`-adic base, from Fontaine-Messing, "p-adic periods
   and p-adic étale cohomology", Contemp. Math. 67 (1987), 179-207; Faltings, "Crystalline cohomology and p-adic
   Galois-representations" (1989); Tsuji, Invent. Math. 137 (1999), 233-411; Scholze, "p-adic Hodge theory for
   rigid-analytic varieties" (attached); and the later relative theory you find, after opening each. Say for each which of
   his data (lattice, filtration, Frobenius, connection) the replacement recovers integrally (Bhatt-Morrow-Scholze,
   attached) and which only rationally.
3. (The problems of 18:43; SF17, SF18, RH17, RH18 [II].) For each of 1a, 1c, 3 and 4, state the precise question his
   notation supports and settle it: the theorem that answers it, derived in his notation, or a proof that the comparison he
   asks for does not hold in that form, with the strongest true replacement. For problem 4, determine which of the
   theories that answer it (crystalline, rigid, prismatic cohomology) has each property his programme of 18:5 uses.
   Problems 1b and 2 are Part D.
4. (18:6; Lead H3; P06, P32, P33 [I].) Reconstruct the setting of 18:6 (the extension `E` of `π` by `G′(C)` with its
   splittings `σ_1` and `σ_2`, the character `χ: π → Q_p^*`, `j_2: G_m(Q_p) → G′(Q_p)`), and decide each assertion:
   `φ(γ) = σ_1(γ)^{−1}σ_2(γ) = u(γ) j_2(χ(γ)^{−1})`, with the extra compatibility P32 [I] says it needs; "Ker u ... connu",
   where `Ker u = Ker χ ∩ Ker φ` needs `Ker u ⊂ Ker χ` (P06 [I]); `Π_1 = π / Ker u` "est un groupe analytique p-adique"
   with `χ_1: Π_1 → Q_p^*` (P33 [I]). Then prove or refute Lead H3: give the exact statement that 18:6 proves or needs, and
   compare it with Sen, "Lie algebras of Galois groups arising from Hodge-Tate modules", Ann. of Math. 97 (1973),
   160-170.

**C. Motives over `R` and the real Frobenius (18:31-41, with 15:213-215; SA07-7; `STUDY.md` §3).** This Part comes after
Part A and is governed by the same rules, the push rule and the three-hour check.

Setting (18:32-34): `K` a field isomorphic to `C`, the isomorphism not chosen; for a motive `M` over `K`,
`Betti(M) ⊗ K = DR(M)`; a motive over `R` gives a Hodge structure `V` and an automorphism `f_R` of order 2 of `V`, rational
and real, that exchanges the Hodge filtration with its opposite: the real Frobenius `f_R ∈ G(Q)`, which generates `G/G^0`,
with `f_R i(λ) f_R^{−1} = i(λ̄)` for `i: S_R → G_R`.

1. (18:34, "Le foncteur M → (structure de Hodge, f_R) est pleinement fidèle en vertu des conj. de Hodge"; SF10, RH05,
   MB11 [II]; A20, A23 [I].) Prove full faithfulness unconditionally for the motives for absolute Hodge cycles over `R`
   generated by abelian varieties, and, granting the Hodge conjecture, for Grothendieck's motives over `R`. Determine the
   essential image: which pairs `(V, f)` come from motives over `R`, and which from abelian varieties over `R`. Decide
   15:215: `f_R` and `G^0` generate `G`, with his correction from "géom. connexe" to "irréd. (pas néc. géom. irréd.)" (A23
   [I]).
2. (18:35, the twisted Betti functor `W(V) = V^+ ⊕ iV^−`; SF11, SF12, RH06, RH07 [II]; Lead H7.) Determine the tensor
   structure on `W` for which his "Oui" on the tensor question holds; prove that `W` is then a fibre functor over `Q`;
   determine the `G`-torsor `Isom^⊗(T_B, W)` over `Q` and its class in `H¹(Q, G)`. Decide his "Il semble ... pas ⊗ isom":
   for which `M` (which tensor subcategories) `W` is tensor-isomorphic to `T_B` over `Q`, over `R` and over `C`; prove or
   refute RH07 and Lead H7; give the answer for `G = G_m` and for `h¹` of an elliptic curve over `R`.
3. (18:36-38; SF13, SF14, RH09-RH12 [II]; R2.) Decide "f_∞ = 1 seulement si M est somme de puissances tensorielles de
   Q(2)", granting Hodge as he does; RH10 [II] gives `A ⊗ Q(−1)`. Determine exactly the motives over `R` on which `f_∞` acts
   trivially, granting Hodge, and unconditionally for the motives for absolute Hodge cycles generated by abelian varieties
   and Artin motives. Decide "R(α) = C dès que M contient le motif de Tate", the criterion for `α ∈ P(R)` (RH09 [II]), and
   the identification on 18:37 of the torsor `P = Isom(T_B ⊗ R, T_DR)` over `G_R` with the class of the 1-cocycle `f_∞` of
   `Z/2` in `G(C)`. Determine every reading of "Q tordu" in the margin (RH12 [II]) under which his centrality statement
   holds, and prove it under each; if none, refute it.
4. (18:39-41; SF16, RH03, RH14, RH16 [II].) Prove that the Hodge decomposition does not depend on the choice of the
   isomorphism `K ≅ C` in his sense (with the semilinear transport and his "non comm."), and decide his assertion over a
   number field: for each archimedean place, the `H^{pq}` and the real subspaces are vector spaces over the largest
   totally real subfield (RH16 [II]); determine the right field if it is another.
5. (RH19 [II].) Prove or refute: for a polarization `q` of weight `n` over `R` with Weil operator `C`, the form
   `B(x, y) = (2πi)^n q(x, Cy)` is positive definite and invariant under `f_∞`, and `f_∞ C f_∞^{−1} = C^{−1}`.

**D. Betti lattices under changes of place: the bounds of 18:42-51 and the cocycles of 18:53-62 (SA07-2; `STUDY.md` §4;
RP-SA07-3).** This Part comes after Part A and is governed by the same rules, the push rule and the three-hour check.

Setting (18:47-49): `M` a motive over `k` algebraically closed in `C`; each place `v` gives a lattice `M_v^Z` in
`∏_ℓ M(ℓ)`; for places `v_1, ..., v_n`, the torsors `P_i = Isom(ξ, ξ_{v_i})` and a point of `[(∏ P_i)/G](Q̂)`; `d = dim G`.

1. (18:47-48; P04, P05 [II].) Define the lattices, the torsors and the point with the topology fixed (P05 [II]: the full
   product against the restricted product), and prove his bound: the transcendence degree of the point is at most
   `(n − 1)d`, "au lieu de (n − 1)m²". Decide for which `M` and which places the bound is attained, with the unconditional
   statements proved and the conditional ones reduced to a named conjecture for a named motive.
2. (18:42-45; P02, P03, SF19 [II]; Lead H5.) Define the field `K` of 18:42-45 ("variation du réseau discret en termes d'une
   place archimédienne") from the pages, and decide his bound for `A = C × C′`, `C` and `C′` without CM and not isogenous
   (`G` isogenous to `SL_2 × SL_2 × G_m`, of dimension 7, and a Borel subgroup of dimension 5): `trdeg_k K ≤ 5`, "et non pas
   égal à dim G − 1 = 6", for every embedding `k ⊂ C`, with the uncertain "≤ 5|4" over `k(π)` (P03 [II]). Determine
   `trdeg_k K` for this `A`, and prove or refute Lead H5.
3. (18:49-51; SF21, SF22, SF24, SF26, P06-P11 [II]; R4; Lead H6.) Prove his conclusion: granting "la conjecture de Tate
   renforcée" (the image of Galois of finite index in `G(Ẑ)`, with the connected "géom." group of his margin, P06 [II])
   and the lemma (R4), the `g_i` can be chosen generic for every ℓ. Prove it unconditionally for elliptic curves without
   CM over number fields (Serre, "Propriétés galoisiennes des points d'ordre fini des courbes elliptiques", Invent. Math.
   15 (1972), 259-331) and for products of pairwise non-isogenous curves without CM (Serre 1972, Théorème 6, for two
   factors; for more factors, the theorem you find, after opening it). Decide his "condition d'approximation" (SF24 [II]):
   for which `G` it holds (P09 [II]: it fails for `G_m`). Decide the equivalence in the margin of 18:51 (SF26, P11 [II]:
   "Moyennant le 'lemme' et ... équivaut à l'indépendance des réseaux") in both directions.
4. (18:51, "il est probable que", with the frozen `\unsure{est|pas}`; SF25, P10 [II].) Decide his expectation on
   recovering the place from the fibre functor for variable `M`, under both readings; it meets Part E.
5. (18:53-62; SF27-SF36, P12-P22, P26 [II].) Prove the cocycle law of 18:57 and its inversion `ψ_v = φ_v^{−1}` (SF29, P15
   [II]), the corrected coboundary of 18:61 (SF33, P18 [II]), the change-of-place formula boxed on 18:62 (SF35, SF36, P22
   [II]), and the identification, marked "À vérifier / OK" on 18:59, of the descended object with the torsor of
   isomorphisms of the two fibre functors (SF30, P16 [II]; Deligne-Milne, "Tannakian categories", LNM 900, Theorem 3.2,
   as the notes cite it). Decide his expectation of 18:61 ("Il me semble que": the adelic closure of the image is open;
   SF34, P21 [II]), the comparison of 18:55 on the category generated by `M` (SF27, P13 [II]), and the π-qualification of
   the margin of 18:59 (SF32, P19 [II]).

**E. Places and fibre functors (cote 15, his pages at scans 207-227; SA07-1).** This Part comes after Part A and is
governed by the same rules, the push rule and the three-hour check.

Setting: `k` a field of characteristic 0 with its complex places, `M` a motive over `k`, `ξ_v` the integral Betti fibre
functor at a place `v` with its `Z_ℓ` and real forms (15:199-201; A06 [I]), and the torsors `Isom^⊗(ξ_v, ξ_w)` under the
integral motivic group; his "catégorie fibrée ... fpqc", "torseur" and "classes de chemins" (15:207-209; A13 [I]).

1. (15:207, 15:219-221, 15:225; A11, A30, A31 [I].) His retraction, "faux, cf groupoïde fondamental sur Z" and "très loin
   d'être caractérisée": prove the exact statement that distinct places can give isomorphic integral (and real) fibre
   functors, with the finite-type and countable-field arguments of 15:219-221, and decide the case `k` uncountable, where
   the page stops at "Si k pas dénombrable," (A31 [I]).
2. (15:223; A34, A35 [I].) Decide his conjecture that for `M` "pris assez grand" the map from complex places to
   isomorphism classes of torsors under the integral motivic group is injective (and whether one `M` separates all places
   at once), and his question whether every principal homogeneous space comes from a place, with the target restricted as
   his Riemann-Hodge margin requires (A35 [I]); determine the image.
3. (15:209-211, 15:225-227; A15, A37, A38, X01-X03 [I].) Does the Hodge structure recover the place? Decide his proposed
   bijection between places and fibre functors with "structure supplémentaire" (A15 [I]), for `k` a number field and for
   `k` of finite transcendence degree over `Q`, and his test on the `j`-family, "Il semble qu'on le verrait facilement"
   (A38 [I]).

**F. Cycle classes, 18:9, and the remaining open steps (SA07-6, SA07-10).** This Part comes after Part A and is governed by
the same rules, the push rule and the three-hour check.

1. (18:15-29; R1; C01-C08 [II], P27-P31 [I], SF02 [II].) Prove the global comparison for every smooth proper variety `X`
   over `C` and every algebraic cycle of codimension `p`, `P_an = (2iπ)^p P_top`, with the orientation he fixes on 18:27-29
   (`ξ(Z(−1)) = Z` up to the sign given by a choice of `√−1`; `α_∞(u) = (2√−1 π)^{−1} v`, `v` the canonical generator of
   `H¹(P¹, Ω¹)`); the push-forward of 18:23 for proper maps of relative codimension `p`, with its degree shift (C04 [II]);
   the action of correspondences on 18:25 ("Ouf !"); and on 18:19, for `X` smooth over `k` with an unchosen isomorphism
   `k ≅ C`, the formula `P_σ^{(p)} = (1/σ(2iπ))^p P_alg`, the dependence of the lattice `H^{2p}(X_σ, Z)` on `σ`, and the
   sign under complex conjugation for `p` odd (C02 [II]: its scope). Decide C07 and C08 [II].
2. (18:9; R5; P09 [I].) Settle the graded formula of 18:9 against the index shift; give the correct formula with its proof
   and say what the transcription reads.
3. (Every remaining entry.) Every other entry of notes [I] for cote 18 (P01-P33, M01-M11, B01-B05, X01-X03) and of notes
   [II] (C01-C08, RH03-RH20, P01-P26, MB01-MB16, SF10-SF19, SF21, SF22, SF24-SF36), and every row of the cote-18 table of
   Standing question I [I], that states a mathematical claim about his pages or records an open step of his and that no
   item above covers: prove or refute the claim, or settle the step. A reading question is not an item: give, in the
   report, the reading you adopt and why.

**G. Statement of results.**

1. For the companion to cote 18: every statement of Parts A-F with what this run and R1-R6 prove, in his notation, with
   the pages it settles.
2. The literature record: for every source named in this prompt and every source you use, one line: opened, with the
   numbers of the theorems that contain or come closest to each statement you prove; or not obtained, with what you
   tried. Say what you searched for A.2-A.4, C.2, C.3, D.2, D.3 and E.2 in particular: transcendence of Hodge splittings
   and of the values of `E_2^*` (Masser 1975; Nesterenko 1996; Katz 1976, as P24 [I] cites it); period conjectures that
   involve the complex conjugates of periods; motives over `R` and the real Frobenius; Betti lattices under automorphisms
   of `C` (Deligne, LNM 900, §2; Charles, attached); open image theorems for products of elliptic curves and for abelian
   varieties. Settle Lead H4 there: say whether the question of 18:5, "Par quoi remplacer 1′, 4′ ??", stands in print
   before these pages, quoting the passages: Grothendieck, "Groupes de Barsotti-Tate et cristaux", Actes du Congrès
   international des mathématiciens (Nice 1970), t. 1, 431-436, and his "On the de Rham cohomology of algebraic
   varieties", Publ. Math. IHES 29 (1966), note 10, as P25 [II] cites it.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: the field `k` (number field, `Q̄`, of finite transcendence degree,
   countable or not), the embedding in `C`, the category of motives (Grothendieck's for homological equivalence, André's
   motivated motives, motives for absolute Hodge cycles, Nori motives), the motivic group and its field of definition, the
   base of each transcendence degree, whether a statement is unconditional or conditional on a named conjecture for a
   named motive, and the topology (archimedean, ℓ-adic, adelic; full or restricted product). Do not replace it by a
   convenient special case. If you prove a special case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism (tensor functors, torsors, Hodge
   structures, Galois modules, filtered modules), and whether it is linear or semilinear, for which conjugation or which
   Frobenius. Compositions must type-check.
3. Every reduction ("we may assume", "after a finite extension", "replace `M` by a summand", "pass to `M ⊕ c^*M`") comes
   with a proof that the property needed transfers in the direction needed.
4. Conventions are named and kept: `2iπ` against `(2iπ)^{−1}`; the Tate twist; Betti cohomology against homology; `f_∞`
   against its inverse; left against right cocycles; the orientation of `P¹(C)`; covariant or contravariant Dieudonné
   theory; the normalizations of `E_2`, `E_4`, `E_6` and of `ω_1, ω_2, η_1, η_2`, with Legendre's relation.
5. Check the edge cases in scope: CM and non-CM; a real model, none, and a motive isomorphic to its complex conjugate
   without a real model; `u = 0`; `k ⊂ R`; `p = 2` in Part B; `k` countable and uncountable in Part E.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you
   attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart. A numerical computation never proves that a number is algebraic or transcendental.
7. No authority. The transcriptions, the Pro notes, the Codex web notes, the sweep files, R1-R6 and the Leads (inferences
   by Claude, Anthropic, and by GPT-6 Astra, OpenAI) are all to be checked where used; the Leads in full. If one is wrong,
   say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and you
   go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to deliver

One ZIP containing:
- `RESEARCH_SA07_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement is
  used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), with complete proofs;
  English, first person plural; his statements quoted in French with the page.
- `RESEARCH_SA07_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `RESEARCH_SA07_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA07_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with
  the statement number); then what you read, what you computed (every computation with its scope, inputs, run time and
  output files), every correction to R1-R6, to the Leads, to the sweep files, to the notes and to the transcriptions, with
  the page, and the readings you adopted (F.3).
- `CHECK_EVENTS.tsv` and `PROGRESS_LEDGER.md`.
- `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched. Remarks taken from
Michel Hua's project are credited to it.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.
**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `RESEARCH_SA07_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `RESEARCH_SA07_checkpoint_<NN>_part<k>.zip`, the file list in the first part.

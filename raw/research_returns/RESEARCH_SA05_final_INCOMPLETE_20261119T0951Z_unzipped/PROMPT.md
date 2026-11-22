# RESEARCH_SA05: Grothendieck's "Théorie des motifs I". The motivic Galois gerbe of F_p (cote 15, scans 2-14) against Langlands-Rapoport and Milne, his "cohomologie absolue" over finite fields and arithmetic bases, the open steps of his correspondences and abstract motives (cotes 11-12), and the Serre torus and "corps de classes commutatif" (cote 15, scans 139-178)

To be settled: the main question (Part A) is Grothendieck's construction of the motivic Galois gerbe of the prime field
`F_p` on 15:2-14: prove every step under the hypotheses he names ("En vertu des conj. de Tate et de Tate-Honda"), with the
crystalline point of 15:3 ("Attention, ici on ne peut remplacer Z par Ẑ !") made exact; decide whether the global class
`ξ_0 ∈ H²(Q, H)` he describes is determined by its local components; and decide whether his gerbe, with its band and its
local data at `ℓ ≠ p`, at `p` and at infinity, is equivalent to the pseudomotivic Galois gerbe of Langlands-Rapoport and
Milne; then its unconditional form. Then: his "cohomologie absolue" (12:60-84, 15:172-178) as Weil-étale cohomology over
finite fields, and the correct statements over arithmetic bases where `ℓ` is inverted, in place of his `ℓ`-adic
comparison and of his boxed "H¹(S, A)(ℓ) fini" (Part B); the open steps of his correspondences, tautological classes and
abstract motives in cotes 11-12 (Part C); the Serre torus, CM types and his programme "Corps de classes commutatif =
Motifs à groupe fondamental motivique [connexe] commutatif (= Motifs métabéliens)" of 15:139-165 (Part D); the statement
of results (Part E).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA05`.
Drafted on 19 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), agent a7b7747fd6dd29f87, a sub-agent of the main
session, at the main session's word, from the sweep-3 study and readings of the topic SA05 (all by Claude Opus 5.5 at
effort max) and the AI-produced transcriptions of his pages.

Citations: "15:7" is cote 15, scan 7 (the archive's sheet number is the scan number minus one). Item ids (SA05-8,
SA05-18, ...) are those of `sweep2_SA05/WHAT_IS_WHERE.md`. "The reading" is `sweep3_SA05/readings/c15b_c12_c11.md`; its
sections are §1-§7.

Not in this prompt: the Deuring categories, the Brandt Picard category, the adelic `μ_2`-torsor and the Deuring element
`ξ_p` (cote 15, scans 16-86; RP-SA05-2, merged into RP-SA06-1), and the Frobenius eigenvalues in every weight with the
strong and weak conjectures of 15:100-106 (RP-SA06-2), are the prompt RESEARCH_SA06; use them here only as background.

## What is attached

One file, `RESEARCH_SA05_background.zip` (1.7 MB, 554 files; LaTeX and text only, no PDF); `MANIFEST.tsv`
at its root lists every file with its origin, size and SHA256, and `README.md` maps the folders.
- `sweep3_SA05/`: `STUDY.md` (§1: the motivic Galois group of `F_p` and its gerbe, 15:2-14; §2: Deuring categories;
  §3: the letter to Mumford), `HUNCHES.md`, `RESEARCH_PACKAGES.md`, the check events and corrections of the whole topic,
  and `readings/c15b_c12_c11.md` with its check events and corrections: §1 cote 15 scans 139-178, §2 cote 12 scans
  150-167, §3 cote 56, §4 hunches HA-HG, §5 cote 11 and cote 12 scans 2-50 (hunches H1-H6 of that part), §6 cote 12 scans
  51-149 (hunches H1-H8 of that part), §7 the whole stretch.
- `sweep2_SA05/WHAT_IS_WHERE.md`: the items SA05-1 to SA05-21 and their places.
- `transcriptions/`: the AI-produced transcription (GPT-6 Astra, ChatGPT Pro mode) of his pages in cotes 11, 12, 15, 18
  (scans 2-17) and 56, one TeX file per scan (`<package>_<cote>_scanNNN.tex`), with the research notes of the same runs
  (the checkpoint `MPL_15_139-194_checkpoint_01`, scans 139-178, has no notes: its doubts and leads are attached);
  `PREAMBLE.tex` defines the macros (`\unsure{a|b}` a doubtful reading with its alternatives, `\deleted` struck by him,
  `\inserted` his insertion, `\margin` margin text, `\scanpage{N}` scan N, `\mspage{n}` his page number).
- `codex_web/`: a second transcription of cote 11, cote 12 scans 2-149, cote 15 scans 172-183 and 207-217 and cote 18
  scans 18-47 (GPT-6.2 Astra at reasoning effort max, ChatGPT Work), with notes, mathematical notes and check events.
- `broad_layer/`: the sweep-3 studies, hunches and research packages of SA06 (Deuring, Weil numbers, CM motives), SA07
  (the real Frobenius, periods) and SA15 (Cristaux), with their item lists.
- `hua_project/`: the modernised readings of cotes 11, 12 and 15 by Michel Hua's project, a witness only; credit any
  remark you use to "Michel Hua's project", quoting a phrase.
- `literature/`: LaTeX sources of J. Scholbach, "f-cohomology and motives over number rings" (arXiv:1003.1219) and
  "Special L-values of geometric motives" (arXiv:1003.1215); "Weil-étale cohomology and the equivariant Tamagawa number
  conjecture for constructible sheaves" (arXiv:2411.07896). `LITERATURE_CHECK.tsv`: sweep 3's record of sources opened.

Not attached: the scans (the transcriptions are our reading of them; where a reading matters and is in doubt, say so)
and every other source named below, among them Langlands-Rapoport, "Shimuravarietäten und Gerben" (J. reine angew.
Math. 378, 1987); Milne, "Motives over finite fields" (Proc. Sympos. Pure Math. 55, part 1, 1994), "Gerbes and abelian
motives" (Math. Ann. 325, 2003; arXiv:math/0301304) and "Lefschetz motives and the Tate conjecture" (Compositio 117,
1999); Kisin, "Mod p points on Shimura varieties of abelian type" (J. Amer. Math. Soc. 30, 2017); Deligne, "Motifs et
groupe de Taniyama" and Milne-Shih, "Langlands's construction of the Taniyama group" (LNM 900, 1982); Lichtenbaum, "The
Weil-étale topology on schemes over finite fields" (Compositio 141, 2005) and "The Weil-étale topology for number rings"
(Ann. of Math. 170, 2009); Geisser, "Weil-étale cohomology over finite fields" (Math. Ann. 330, 2004); Flach-Morin,
"Weil-étale cohomology and zeta-values of proper regular arithmetic schemes" (Doc. Math. 23, 2018); Bloch-Kato, "L-functions
and Tamagawa numbers of motives" (Grothendieck Festschrift I, 1990); Milne, "Arithmetic duality theorems"; Beauville-Voisin
(J. Algebraic Geom. 13, 2004); Gross-Schoen (Ann. Inst. Fourier 45, 1995); O'Sullivan (J. reine angew. Math. 654, 2011);
Vasiu-Zink (Doc. Math. 15, 2010). Open each source you use and cite it with its exact theorem numbers.

## Where this comes from

- Grothendieck's dossiers "Théorie des motifs" in the Montpellier archive:
  - cote 15, scans 2-14, "Groupe de Galois motivique commutatif. Cas d'un corps de base fini" (on the backs of a reused
    typescript of Lipman's "Rational singularities", Publ. IHES 36, 1969, so written 1969 or later): the Weil-number
    group, the gerbe of fibre functors extending the Artin fibre functor `F^0`, its band `H`, the class `ξ_0` and its
    local components;
  - cote 15, scans 139-178: a cover (scan 140, untranscribed) "Motifs essentiellement abéliens et théorie du corps de
    classes"; §1 the tori `T_K`, `V_K` and `S_K^0`; §2 CM structures and the homomorphisms `ψ_Σ`; a Tate-Shafarevich
    computation (15:154); the cover "Corps de classes commutatif = Motifs à groupe fondamental motivique [connexe]
    commutatif (= Motifs métabéliens)" (15:157); the class group extension and Hodge realizations of "motifs abéliens"
    (15:159-165); "Calculs de cohomologie absolue des Motifs de Tate Z(n)" (15:172-178);
  - cote 12: the "Esquisse d'une théorie des motifs" (12:2-14; IHES letterhead with "91", so 1968 or later), motives over
    a base (12:21-41), §12-17 (12:42-95: levels and birational invariants, the Galois characterization of filtrations,
    commutation theorems, absolute cohomology, rational points, positive forms, L-functions), "Poids et niveaux des espaces
    de cohomologie ℓ-adiques" (12:96-137, with a typed message of 27 March 1968), smooth integral motives (12:140-142),
    pseudo-abelian envelopes (12:143-149), the category of motives from correspondences, niveau, duals and positive forms
    (12:150-167);
  - cote 11: the category of correspondences, transposition, stable systems, Poincaré and bivariant algebras, and the
    tautological classes of `X^k` (11:3-57; written on the backs of a typescript of Mumford's Geometric Invariant Theory,
    so 1964-65 or later);
  - cote 56: vanishing cycles of quadrics and the integral cohomology of quadrics and cones.
- The transcriptions: AI-produced by GPT-6 Astra (ChatGPT Pro mode); cote 11, cote 12 scans 2-149 and parts of cotes 15
  and 18 also by GPT-6.2 Astra at reasoning effort max (ChatGPT Work).
- The sweeps, all by Claude Opus 5.5 at effort max: sweep 2 placed the items; sweep 3 (18-19 Nov 2026) read the pages
  and worked the mathematics through: the study (agent a28ea31fa17dd65e1) and the reading `c15b_c12_c11` (agent
  a7b7747fd6dd29f87 with the sub-readers aa713c8c5c2c8b9d6 for cotes 11 and 12 scans 2-50 and ac391f829fcbd7a41 for cote
  12 scans 51-149).

## Results this prompt builds on (status on 19 Nov 2026)

None of these is to be proved again as if open, except where a Part requires it. For each one you use: read the proof at
the place given and confirm the step you rely on in a paragraph of your own, or give the exact error with a repair or a
counterexample. All are by Claude Opus 5.5 at effort max (the agents named above) and unrefereed; their check events are
in `sweep3_SA05/CHECK_EVENTS.tsv` and `sweep3_SA05/readings/c15b_c12_c11_CHECK_EVENTS.tsv` under the pages given.

- **R1 (15:2-14; `STUDY.md` §1, check events SA05-S3-1 to -4).** The torsion of `Γ' = Γ/⟨roots of unity, p⟩` is `Z/2`,
  generated by the class of `√p`; `ε i(λ) = λ²` matches the weights (`Q(−1)` of weight 2); "Serre's argument" of 15:11: a
  fibre functor over `R` would embed the endomorphism algebra of a supersingular elliptic curve, the quaternion algebra
  ramified at `p` and `∞`, into `M_2(R)`; so the `μ_2`-components of `ξ` at `p` and at `∞` are the non-zero element,
  consistent with the sum of invariants.
- **R2 (15:141-152; the reading §1.2-1.3).** `S_K^0 = T_K/R`, with `V_K/R` the largest quotient of `V_K` compact at
  infinity, is the connected Serre group `S^K`: his Proposition (i)-(iv) and Corollaries 1-4 re-proved, with
  `X*(S_K^0) = {χ ∈ Z[I_L] : χ + ιχ constant}` (`L` the largest weilien subfield) and `i` the weight cocharacter; his
  slips corrected (condition (ii) with the inclusion reversed; `Gal(K̃/Q)` for `Gal(K̃/K)`; `[K_0 : Q] = r`; `N_{K/L}`;
  `V_K/V_{K_0} → T_K/T_{K_0}` an isogeny of degree 2). CM structures: the field of definition of `Σ` (the reflex field) is
  CM; the condition is symmetric in `E`, `K`; `[K_0 : Q] ≤ 2^d` (sharper than his `C(2d, d)`); `ψ_{Σ'} = i ∘ ψ_Σ ∘ N`;
  `ψ_Σ ∘ i_K = i_E`; `Ker ψ_Σ ∩ ⋂_i Ker ψ_{Σ_i} = 1` (the CM types generate `X*(S^K)`); quadratic `E` do not suffice
  unless `K` is multiquadratic.
- **R3 (15:154; the reading §1.4).** For `K` CM Galois and `T = R_{K_0/Q}(R^1_{K/K_0} G_m)`, the classes of `H¹(Q, T)`
  trivial at every finite place form the group of `F_2`-combinations of the infinite places with zero sum (Hasse's norm
  theorem and the reciprocity sequence; his Tate-cohomology route also checked).
- **R4 (15:157-165; the reading §1.5).** The cover reads "Motifs métabéliens" (decided on the scan). 15:159: the
  abelianized Galois group is an extension of the narrow class group by `Ô*/closure(E^0)` (`E^0` the totally positive
  units), or of `Pic(A)` by `(Ô* × π_0(K_R*))/closure(E)` (his second formula); his first formula holds only for `K`
  totally imaginary. 15:165: his real-place condition is Deligne's description of the de Rham structure over `R`.
- **R5 (15:172-178; the reading §1.6).** The tables of `H^i(Ẑ, Z_ℓ(n))` and `Z/(1 − q^n) = K_{2n−1}(F_q)`;
  `H^i(Spec Z, Q(1)) = 0, 0, 0, Q` for `i = 0, 1, 2, 3` (re-proved); the margin of 15:173 must read `n ≠ 1`, not `n ≠ 0`;
  the bracket of 15:174 reads "[est-ce nul ??]"; the Artin-Verdier tables of 15:177-178; Proposition 5.4 of his Brauer
  draft (15:176).
- **R6 (cote 12 scans 51-149; the reading §6).** His `ℓ`-adic comparison 4) of 12:63-64 is false over arithmetic bases:
  on `Spec Z[1/ℓ]` with `Q(0)`, `H¹` has `Q_ℓ`-rank 1 and `Q_{ℓ'}`-rank 0 for `ℓ' ≠ ℓ`. The boxed "H¹(S, A)(ℓ) fini si ℓ
  premier à S" of 12:75 is false over `S = Spec Z[1/11ℓ]` with `A` the Néron model of `X_0(11)`. Over `F_p` both
  arguments are right. 12:71 and 12:73 checked (12:73's `i = 1` line a slip); 12:78 right and 12:82 wrong at `i ≥ 2`;
  12:86-89 (cones of positive forms) checked; 12:115 reads `2n − i + j`; 12:120's weight bound must carry `+ 2j`, not
  `+ j`; 12:142 reduces his question to finite subgroups that do not extend.
- **R7 (cote 12 scans 150-167; the reading §2).** The conditional construction of 12:150-152 (D and the Hodge-type
  positivity assumed, as he states); `T_ℓ` is a tensor functor up to the Koszul sign; the niveau decomposition of 12:155
  needs semisimplicity; the claim of 12:156 that an internal Hom in the effective category is the one of the category with
  Tate twists inverted is false (`Hom(Λ(−1), Λ(0))`: 0 against `Λ(1)`); `Hom(M, N(−i)) ≅ M* ⊗ N` needs rigidity; his
  positivity axioms of 12:161-167 checked; slips `κ_{i+j,k}`, `M'(−k)`.
- **R8 (cote 11 and cote 12 scans 2-50; the reading §5).** The formalism of 11:3-48 with its signs; his question of 11:31
  answered no (a tangent line to a conic); 11:51: with `M = δ − (δ_12 y_3 + δ_23 y_1 + δ_31 y_2) + (y_1 y_2 + y_2 y_3 + y_3 y_1)`
  in `H^{2n}(X³)`, `M = 0` iff `∫uvw = 0` for all `u, v, w` of positive degree; the product rule of 11:55-57 completed;
  12:2-41 checked with corrections; his questions of 12:49-50 answered no (Enriques surfaces; Larsen-Lunts).
- **R9 (cote 56; the reading §3).** The vanishing cycles of quadrics and the integral cohomology of quadrics, cones and
  affine quadrics checked, with four corrections (56:15 degrees; 56:20 the twists for `n` odd; 56:26
  `λ_ν² = (−1)^ν ξ^{2ν}`; 56:5 the cokernel for `ℓ = 2`).

## Leads

Each is an inference of the model named, checked by no one. Each is to be proved or refuted in full, inside the Part it
serves.

- **Lead A1 (A.4; `HUNCHES.md` H1, Claude Opus 5.5 at effort max, agent a28ea31fa17dd65e1).** 15:2-14 is a complete
  computation of the motivic Galois gerbe of `F_p`, equal to the gerbe of Langlands-Rapoport and Milne.
- **Lead A2 (A.2; `HUNCHES.md` H4, the same agent).** "On ne peut remplacer Z par Ẑ" (15:3) is the crystalline
  obstruction that the pseudomotivic groupoid handles with the Weil-group (not the Galois-group) version at `p`: the
  `p`-adic realization takes values in isocrystals, with Frobenius an automorphism, not a `Ẑ`-action.
- **Lead B1 (B.1-B.2; the reading §6 H1, the sub-reader ac391f829fcbd7a41, Claude Opus 5.5 at effort max).** Over a finite
  field his absolute cohomology is Lichtenbaum's Weil-étale cohomology with `Q` coefficients:
  `H^{2j+1}(X, Q(j)) = H^{2j}(X, Q(j)) ∪ e` with `e` the generator of `H¹(W_k, Z)`, and restriction to `k_n` sends `e` to
  `n e_n` (his "pas canonique" and his factor `n`); over arithmetic bases the correct statements carry the Bloch-Kato
  condition at `ℓ`.
- **Lead B2 (B.4; the reading §4 HD, agent a7b7747fd6dd29f87).** His `H³(Spec Z, Q(1)) = Q` is a fundamental class for a
  duality with dualizing object `Q(1)[3]`; with Borel's `H¹(Spec Z, Q(n)) = Q` for odd `n ≥ 3`, it puts classes in
  `H²(Spec Z, Q(1 − n))`, at the trivial zeros of `ζ`: the shape of Lichtenbaum's order-of-vanishing formula.
- **Lead C1 (C.1; the reading §5 H4, the sub-reader aa713c8c5c2c8b9d6).** The relations of 11:51-57 are the cohomological
  shadow of the Gross-Schoen modified diagonal (curves) and of the Beauville-Voisin relation (K3 surfaces).
- **Lead C3 (C.3; the reading §6 H4).** The "partie algébrique" of his fundamental Lie pro-motive (12:59) is the Lie
  algebra of the centre of the motivic Galois group, of dimension `1 + [E : Q]/2` for `E` the largest CM subfield of `K`
  and 1 if `K` has none.
- **Lead C5 (C.5; the reading §6 H7).** His suspected failure of the good-reduction criterion over regular local rings of
  dimension 2 in mixed characteristic (12:142) is the extension problem of Vasiu-Zink.
- **Lead D1 (D.1; the reading §4 HA).** His integral group `G^0 = A*/closure(E^0)` over `Z` (15:159) is an integral model
  of a Serre group whose fibre at `p` receives the Frobenius of CM motives with good reduction (Shimura-Taniyama), and this
  is the bridge, unwritten on his pages, between 15:139-165 and 15:2-14.
- **Lead D2 (D.2; the reading §4 HB).** His slogan of 15:157 is realized by Serre's groups `S_m` and the Taniyama group.
- **Lead D3 (D.3; the reading §4 HC).** The group of R3 controls the uniqueness of real structures and of `Q`-forms of the
  realizations of CM motives.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (the field, variety, motive, group, gerbe, torus or cohomology class given completely,
with the verification of every hypothesis and of the failure; checked by a program when finite or computable) and the
strongest true statement proved in its place. Nothing else finishes an item. Partly settled is not an outcome. The
cases proved, the computations run, the obstruction as an exact statement and the smallest undecided instance are the
state of an item you are still working on: record them as you go, then attack the obstruction, starting from that
instance. "Known" counts only with the derivation of the statement used here from the cited theorem, after opening the
source. An item that begins with "Determine" is done when the object asked for is given explicitly, with a proof that it
is the whole answer.

Conditional statements. Many of his statements assume the Tate conjecture, the semisimplicity of Frobenius, the standard
conjectures or the Hodge conjecture, as he says on the page. A statement proved under such a hypothesis is proved (a)
when the hypothesis is stated exactly (which form, over which fields, for which varieties) and the proof from it is
complete; then decide, for the same item, which parts hold without the hypothesis, and prove them.

For Part A in particular.
- Fix one category of motives over `F_q` and say which (numerical motives with the commutativity constraint changed
  by the Künneth projectors; homological motives under the Tate conjecture with semisimplicity; Lefschetz motives of
  abelian varieties; Milne's pseudomotives), with its fibre functors and their coefficient fields.
- A gerbe is given with its band, the field it lives over, its class, and for every place `v` the morphism or the class
  at `v`; an equivalence of gerbes is given with the identification of bands it induces. Groupoids (Milne) and gerbes
  (Langlands-Rapoport, his pages) are compared through an explicit dictionary.
- His notation is kept: `F^0`, `Niv^0(M)^0`, `G`, `G^0`, `H`, `ε`, `i`, `Γ`, `Γ'`, `η_p`, `ξ_0`, `ξ_v`.

For Part B in particular. Every cohomology group is named with its theory (étale, continuous `ℓ`-adic, Weil-étale,
motivic in Voevodsky's sense, Bloch-Kato `H^1_f`, his "absolue"), its coefficients and its base; the comparison maps are
given, and the places where `ℓ` is inverted are said.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1-R9 again in place of the
items, except where a Part asks for it; a result of the readings used without the check above; a comparison of theories
that names corresponding objects without proving that they correspond; a statement for all fields (all `n`, all `K`,
all `X`) proved for some, without saying so; a step that replaces a claim by a convenient special case without naming
it; a reading of his pages changed to fit the mathematics without saying what the transcription reads and why you read it
otherwise.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA05_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The motivic Galois gerbe of `F_p` (15:2-14). The main question is A.3-A.4.**

Setting (15:3-14; `STUDY.md` §1): `M` the category of motives over `F_p`, with fibre functors `T_ℓ` over `Q_ℓ` (`ℓ ≠ p`)
and, at `p`, the crystalline `T_p` ("F-cristaux sur Q_p", 15:3); `Niv^0(M)^0` the motives of level 0 and weight 0 (Artin
motives) with the intrinsic fibre functor `F^0` over `Q` (`F^0(H*(X)) = f_*(Q_X)` for `X` finite); `G` the motivic Galois
group, of multiplicative type with character group `Γ`, the Weil numbers (15:5: algebraic, `ℓ`-adic units for `ℓ ≠ p`,
all conjugates of absolute value `p^{ν/2}`); `ε: G → G_m`, `i: G_m → G` with `ε i(λ) = λ²`; `G^0` the identity
component; `H = Ker(ε | G^0)`; the gerbe of fibre functors of `M` and its subgerbe of fibre functors extending `F^0`, of
band `H`; the class `ξ_0 ∈ H²(Q, H) = H²(Q, H^0) × H²(Q, μ_2)` (15:7); its local components `ξ_v`.

1. (His structure statements, 15:3-5 and 15:13-14.) Under the hypotheses you fix as the outcome section asks (the Tate
   conjecture for the varieties over the finite fields involved, the semisimplicity of Frobenius, and Tate-Honda for
   abelian varieties), prove: (a) `G` is of multiplicative type with character group `Γ`, and `G/G^0 = Ẑ` (decide whether
   `Γ` contains the Weil numbers of every integral weight, of every weight `ν ∈ Z` or only `ν ≥ 0`, and how `G` over
   `F_p` differs from the group over `F̄_p`); (b) `X*(G^0) = Γ/(roots of unity)`, `X*(H) = Γ' = Γ/⟨roots of unity, p⟩`,
   `Γ'_tors = Z/2` generated by `√p`, `H^0` a compact torus, and `i|μ_2` splits `H = H^0 × μ_2`; (c) 15:13-14: the group of
   Weil units `Γ^0`, the canonical Frobenius element of `G(Q)`, and for a simple motive `M` the centre of `End(M)`
   generated by Frobenius with `End(M) ⊗ Q_p = End(T_p(M))` (Tate-Honda for abelian varieties: state and prove the
   motive version), and the identification of `H^0` as the dual of the group of Weil numbers (15:14).
2. (The local components, 15:7-11.) Prove: (a) at every finite `ℓ ≠ p` the gerbe is neutral (`T_ℓ` extends `F^0`);
   (b) at `p`: the exact meaning of "Attention, ici on ne peut remplacer Z par Ẑ !" (15:3) and of 15:7-9 (`T_p` and the
   fibre functor `F_p` differ by a torsor under `(G/H)_{Q_p}`, an extension of `G/G^0 = Ẑ` by `G^0/H = G_m` that splits;
   its class `η_p ∈ H¹(Q_p, Ẑ) = Hom(π_1(Q_p), Ẑ)` is "l'isom Gal(Q̃_p/Q_p) = Ẑ donné par Frobenius"; `ξ_p = d(η_p)`).
   Decide whether `T_p` is a fibre functor over `Q_p` at all; if not, give the object that replaces it (the category of
   isocrystals over `F̄_p` as a gerbe over `Q_p`, its band and class) and prove the correct form of his statement with
   `Z` and `Ẑ` in their places (Lead A2). (c) At infinity: prove each of his three arguments of 15:11 that `M` has no
   fibre functor over `R` (polarizability with `H` disconnected; a rank-1 object of degree 1; Serre's supersingular
   curve), or refute it; prove that the compact-torus component of `ξ_∞` vanishes, and determine `ξ_∞` (the real Weil
   group). (d) Prove that the `μ_2`-components at `p` and at `∞` are the non-zero element.
3. (The global class; main question, first half.) Prove or refute: (a) the `H^0`-component of `ξ_0` is determined by its
   local components, i.e. `Ш²(Q, H^0) = 0` for the protorus `H^0` (compute this group: `Ш²` of a protorus is a limit of
   `Ш²` of tori, and its dual involves `Ш¹` of the character group); (b) the `μ_2`-component is determined by the finite
   places (sum of invariants); (c) `M`, with its grading, augmentation, `T_ℓ` and `F^0`, is determined up to equivalence by
   the class `ξ_0`, as 15:7 says, and conversely; (d) determine `ξ_0` explicitly: every local component, as an element of
   the explicit local groups.
4. (The comparison; main question, second half.) Prove or refute: his gerbe of A.1-A.3, with its band `H` (or `G`) and
   its local data at `ℓ ≠ p`, `p` and `∞`, is equivalent, compatibly with bands and local data, to the pseudomotivic
   Galois gerbe of Langlands-Rapoport (1987, §§2-3) and to Milne's pseudomotivic groupoid (1994, §3); and under the
   hypotheses of A.1 both are the motivic gerbe (Milne 1994; give the theorem number). Write the dictionary (his `F^0` and
   the subgerbe of band `H`; his `η_p` and their morphism at `p`; his `μ_2` at infinity and their morphism at `∞`; his
   Weil-number group and their protorus `P`) and prove each line of it. Where they differ, prove the difference. Decide in
   particular whether his description of the `H^0`-component by local components agrees with theirs, and whether his
   splitting `H = H^0 × μ_2` is compatible with their constructions.
5. (Unconditional form.) Construct, without the Tate conjecture, a gerbe over `Q` with band `H` and the local data of A.2,
   and prove it unique up to the ambiguity you determine (the group of its automorphisms and the classes it could differ
   by). Then determine which statements of 15:2-14 hold unconditionally for the tannakian category generated by abelian
   varieties over finite fields with Lefschetz classes as morphisms (Milne 1999) and for the category used by Kisin
   (2017), and prove them.

**B. His "cohomologie absolue" over finite fields and over arithmetic bases (12:60-84, 15:172-178).** This Part comes
after Part A and is governed by the same rules, the push rule and the three-hour check.

Setting (the reading §6 items 5-10 and §1.6): his requirements 1)-4) of 12:60-65 (commutation with limits; Leray
transitivity; `H^0(X, M) = Hom(Q_X(0), M)` and hyperext; maps to `ℓ`-adic cohomology that become isomorphisms after
`⊗ Q_ℓ` for `X` of finite type over `Z`, with `H^i(X, M)` of finite type over `Q`); his boxed restatement of Tate's
conjecture `A^i(X) = Im[H^{2i}(X, Q(i)) → H^{2i}(X, Q_ℓ(i))]` (12:65); his "th. de dualité absolue" (12:67); 12:71
(Hochschild-Serre over `F_q`, `H^{2j+1}(X̄, Q(j)) = A^j(X̄) ⊗ Q` "pas canoniquement en k", the factor `n` under
`k → k_n`); 12:73 (weights); 12:74-80 (`A(S) ⊗ Q = H¹(S, T_mot(A))`, the boxed "H¹(S,A)(ℓ) fini si ℓ premier à S", the
Brauer reformulation, Birch-Swinnerton-Dyer); 12:82, 12:84; 15:173 (his tables over `F_q` and over `Spec Z`), 15:174
(`H^i(Spec Z, Q(1)) = 0, 0, 0, Q` and "[est-ce nul ??]" for `n ≠ 1`), 15:177-178.

1. (Finite fields.) Prove that Weil-étale cohomology with `Q` and `Z` coefficients (Lichtenbaum 2005; Geisser 2004)
   satisfies, for smooth projective `X` over `F_q` and under the Tate conjecture with semisimplicity at the eigenvalue 1
   (state the forms used), every requirement and every value of 12:60-73 and of 15:173, with his factor `n` and "pas
   canoniquement" as in Lead B1. Determine which of these statements hold unconditionally (all `X` of dimension at most 1;
   abelian varieties in codimension 1 by Tate 1966) and prove them. Decide: is every theory satisfying his requirements
   1)-4) over finite fields isomorphic to Weil-étale cohomology, and in what sense? Decide his statement of 12:65 that
   `H^i(k, M) = 0` for `i > 0` over an algebraically closed `k`, against his own computation over `F̄_p`.
2. (Arithmetic bases: the comparison.) For `X = Spec O_K[1/S]` (`K` a number field, `S` finite) and `M = Q(n)`, `n ∈ Z`:
   determine the étale groups `H^i(X[1/ℓ], Q_ℓ(n))` for every `ℓ` and their Bloch-Kato subgroups `H^i_f` (local conditions
   at the places above `ℓ` and at `S` stated), and prove: there is one `Q`-space `H^i(X, Q(n))` with
   `H^i(X, Q(n)) ⊗ Q_ℓ ≅ H^i_f(X, Q_ℓ(n))` for every `ℓ`, for `n = 1` (units and class groups, Kummer theory), for
   `n ≥ 2` (Borel and Soulé), and for `n ≤ 0` (prove it where it holds, and where it does not follow from known theorems
   prove its exact equivalence with the conjecture you name). Then
   state the correct form of his requirement 4) for `X` of finite type over `Z` and a pure motive `M`, in his notation, as a
   precise conjecture (Bloch-Kato and Fontaine-Perrin-Riou), and prove that it gives his statements over finite fields
   (B.1) and specializes to the case above. Decide whether Scholbach's f-cohomology of motives over number rings
   (attached) satisfies his requirements 1)-3) and the corrected 4).
3. (Abelian schemes: "H¹(S, A)(ℓ) fini".) For a number field `K`, `S = Spec O_K[1/N]` with `ℓ | N`, and `A` an abelian
   scheme over `S`: prove the exact sequence relating `H¹(S, A)(ℓ)`, `Ш(A/K)(ℓ)` and the local groups `H¹(K_v, A)(ℓ)`,
   `v | N`, and determine the corank of `H¹(S, A)(ℓ)` in terms of `Σ_{v | ℓ} [K_v : Q_ℓ] dim A`, the rank of `A(K)` and
   `Ш(A/K)(ℓ)`. Complete R6's counterexample (`X_0(11)` over `Z[1/11ℓ]`) with every step. State the correct form of his
   boxed statement over arithmetic bases (with the local conditions at the places above `ℓ` restored) and prove its
   equivalence with his `A(S) ⊗ Q = H¹(S, T_mot(A))` in the corrected form. Over `S` of finite type over `F_p`, prove his
   chain of equivalences of 12:74-80 in full (with R6's corrections to 12:76-77), and decide his question of 12:79,
   "Prouver que Br(S) → Br(X) surjectif mod groupes finis ??", for a relative curve `X/S`, with its equivalence "(via des
   jacobiennes)" to the finiteness of `H¹(S̄, Ā)(ℓ)^π`.
4. (`Spec Z`.) In Flach-Morin's Weil-étale cohomology (or the theory you prove to be the right one), determine
   `H^i(Spec Z, Z(n))` and `H^i(Spec Z, Q(n))` for every `i` and every `n ∈ Z`, and decide each entry of his tables of
   15:173 (`H^i(Spec Z, Z(1)) = Z` for `i = 3` and 0 otherwise; `H^i(Spec Z, Z) = Z` for `i = 0` and 0 otherwise), his
   `H^i(Spec Z, Q(1)) = 0, 0, 0, Q`, and his localization isomorphism (for `n ≠ 1`). Answer "[est-ce nul ??]" exactly:
   for each `n ≠ 1` and each `i`, the group, with its generators (Borel's regulator classes where they occur). Prove or
   refute Lead B2: a duality with dualizing object `Q(1)[3]` and fundamental class his `H³(Spec Z, Q(1)) = Q`, and the
   orders of vanishing of `ζ(s)` at every integer `s = n` from the ranks (with the archimedean term if one is needed).
5. (Absolute duality, 12:67.) His "th. de dualité absolue": for `X` of finite type over `Z`, regular of dimension `n`, with
   values in `Q(n)[2n+1]`, `H^i(X, M)` dual to `Ext_!^{2n+1−i}(X; M, Q(n))`, and no "!" when `X` is proper over `Spec Z`.
   Prove the statement with finite coefficients (Artin-Verdier; Milne, Arithmetic duality theorems, II), determine the
   correct form with `Q` coefficients (archimedean places, the odd-degree Weil-étale classes) and prove it for
   `X = Spec O_K[1/S]` and for `X` a smooth projective curve over `F_q`.

**C. The open steps of his correspondences and abstract motives (cotes 11 and 12).** This Part comes after Part A and is
governed by the same rules, the push rule and the three-hour check.

1. (11:51-57, the tautological classes; R8; Lead C1.) For `X` smooth projective connected of dimension `n` over an
   algebraically closed field with a Weil cohomology, let `T_k ⊂ H*(X^k)` be the subring generated by the pullbacks of the
   point class `y` and the classes `ε_{R,J}` of all partial diagonals (pointed and unpointed, 11:55). (a) Determine all
   relations among his generators in every `T_k` (11:53 leaves "relations" blank), in terms of the multilinear forms
   `∫u_1 ⋯ u_m` on `H^{>0}(X)`; prove that the relation `M = 0` of R8 and its analogues for `k ≥ 4` generate them, or
   determine generators; give the dimension of `T_k` in each degree for curves of genus `g`, for surfaces with `b_1 = 0`,
   for abelian varieties and for `P^n`. (b) Prove the complete product rule of the `ε_{R,J}` (the reading §5 item 6: the
   cycle rank of the class graph) and his "! vérifier" statements. (c) In Chow groups with `Q` coefficients, with `y`
   replaced by a 0-cycle `o` of degree 1: decide for which `(X, o)` the relations of (a) hold in `CH*(X^k)_Q`; prove them
   for K3 surfaces with the Beauville-Voisin class, for hyperelliptic curves with `o` a Weierstrass point, and for abelian
   varieties with `o = 0` among symmetrically distinguished cycles; give a curve of genus 3 for which they fail, with the
   proof (the Ceresa or Gross-Schoen cycle).
2. (11:38-48, the axioms he leaves open.) State the axioms of his gauged simplicial bivariant algebras (11:42: "il
   convient de préciser les axiomes"; "à vérifier") as a definition, including the exchange axiom he calls "axiome cartésien
   oublié !" (11:46) in its correct form (base change exactly for the product squares, or for transverse squares with
   refined Gysin maps), and prove: `I ↦ H*(X^I)` satisfies them for a Weil cohomology; his functor `A(•) → (A_0, Δ)` is
   fully faithful on special objects; special objects are equivalent to commutative Frobenius algebras.
3. (12:59, the algebraic part of the fundamental Lie pro-motive; Lead C3.) Prove or refute Lead C3 for a field `K` of
   finite type over `Q`, with the exact hypotheses (the motivic Galois group pro-reductive with abelianization the Serre
   group), and prove it unconditionally in André's category of motivated motives for motives of abelian type; over a
   finite field, prove or refute his "tout".
4. (12:116-122, weights and levels of `R^i f_*`; R6.) Prove or refute his bounds of 12:118-120 in the corrected form: for
   an open immersion, and then (his conjecture of 12:120) for `f: X → Y` with `X` regular and a local relative dimension
   `d_y(f)`, with `F` strictly special of weight `j` (12:111), the stalks of `R^i f_* F` have weights at most
   `2 Inf(i, d_y(f)) + 2j` and levels at most `Inf(i, d_y(f) − 1) + j`; give the sharp bounds, and decide his margin
   question "peut-on remplacer par n − 1 si f de dim ≤ n − 1 ?". Define "level" for these sheaves as in 12:111-115 before
   you use it.
5. (12:142, good reduction; Lead C5.) Decide his question: for `R` a regular local ring of dimension 2 of mixed
   characteristic `(0, p)`, `K` its fraction field and `A_K` an abelian variety with `T_ℓ(A_K)` unramified at every
   height-one prime for every `ℓ` (his `S_ℓ`), does `A_K` extend to an abelian scheme over `R`? Prove it where it holds
   (Vasiu-Zink's conditions; ramification `e < p − 1`), and settle the remaining cases: a proof, or a counterexample with
   the finite subgroup of `A_K` that does not extend (R6's reduction).
6. (12:140, independence of `ℓ`.) His "Conjecturalement, il suffit que ce soit vrai pour un ℓ premier à toutes les car.
   résiduelles": prove it for motives of abelian type over a number field (through the independence of `ℓ` of the inertia
   action on abelian varieties, SGA 7 IX), and decide it for motives in general: a proof, or an exact equivalence with a
   named conjecture.

**D. The Serre torus, CM types and "corps de classes commutatif" (15:139-165).** This Part comes after Part A and is
governed by the same rules, the push rule and the three-hour check.

1. (Lead D1.) Prove: his `G^0 = A*/closure(E^0)` over `Z` (15:159), with the extension `G` of the narrow class group
   (15:161), is an integral model of Serre's group `S_m` for `m` the product of the real places of `K`. For a CM motive over
   `K` with good reduction at `v | p`, prove that its Frobenius at `v` is the image of a uniformizer under the reflex norm
   (Shimura-Taniyama), and construct from this a morphism between the motivic gerbe of the residue field (Part A) and the
   reduction of his group at `v`, in the direction that exists; prove that it is the restriction to CM motives of the
   Langlands-Rapoport morphism, and decide which Weil numbers of Part A arise from CM motives in this way (weight 1: Honda
   and Tate through CM lifting).
2. (Lead D2.) Prove or refute, in Deligne's category of absolute Hodge motives over a number field `K` and in André's
   category of motivated motives: (a) a motive whose motivic Galois group has commutative identity component lies in the
   tannakian subcategory generated by Artin motives and CM abelian varieties; prove it for motives of abelian type, and
   for general motives prove it or prove its exact equivalence with a statement on Hodge classes that you name; (b) over
   `Q`, the motives whose motivic Galois group is metabelian are exactly those whose group is a quotient of the Taniyama
   group; determine that category; (c) his question of 15:163, "Comment se relient ces structures de Hodge ??", for two
   places `ξ̃, ξ̃'`: give the answer in his notation (the action of `Aut(C)` on CM motives through the Taniyama group) with
   the proof.
3. (Lead D3; 15:154; R3.) For `K` CM Galois, compute the classes of `H¹(Q, S^K)` trivial at every finite place, and prove
   or refute: the `Q`-forms (fibre functors over `Q`) of the category of CM motives with CM by subfields of `K` that agree
   with the `ℓ`-adic realizations at every finite place form a torsor under that group; decide whether the Betti fibre
   functor is singled out, and relate the answer to the `μ_2` at infinity of 15:11 and to the real fibre functors of SA06-10.
4. (15:151, "Quelle est l'image de ψ_Σ?") Determine the image of `ψ_Σ: S_K^0 → T_E` (equivalently of the compact part
   `V'_K`, as he reduces it): its character group, its dimension in terms of the matrix `1_Σ`, and the cases where it is
   all of the torus of norm-compatible elements; prove that it is the Mumford-Tate group of the CM type.

**E. Statement of results.**

1. For the companion to "Théorie des motifs I": every statement of Parts A-D with what this run and R1-R9 prove, in his
   notation, with the pages it settles.
2. The literature record: for every source named in this prompt and every source you use, one line: opened, with the
   numbers of the theorems that contain or come closest to each statement you prove; or not obtained, with what you
   tried. Say what you searched for A.3-A.5, B.2-B.4, C.1, C.4-C.6 and D.1-D.3 in particular: the pseudomotivic gerbe and
   its local components; `Ш²` of the Weil-number protorus; Weil-étale cohomology over finite fields and of `Spec Z`;
   Bloch-Kato `H^1_f` for Tate motives over number rings; tautological rings of powers of a variety; extension of abelian
   schemes over regular bases; the Taniyama group and CM motives.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: the field (finite, number field, local, `R`, `C`), the category of motives
   (Chow, homological, numerical, Lefschetz, absolute Hodge, motivated, pseudomotives), the fibre functors and their
   coefficient fields, the cohomology theory and its coefficients, the base and which primes are inverted, the conjectures
   assumed. Do not replace it by a convenient special case. If you prove a special case, name it as one and keep the
   general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property you use
   (a tensor functor, a morphism of gerbes over which band morphism, Galois-equivariant, compatible with weights). Compositions
   must type-check.
3. Every reduction ("we may assume", "after a finite extension", "pass to `F̄_p`", "by Shapiro's lemma", "by duality")
   comes with a proof that the property needed transfers in the direction needed.
4. Conventions are named and kept: the sign of the Tate twist (`Q(1)` of weight `−2`); geometric or arithmetic Frobenius;
   the weight of a Weil number; the commutativity constraint on motives (with or without the Koszul sign); gerbes versus
   groupoids; the normalization of class field theory (uniformizers to geometric or arithmetic Frobenius).
5. Check the edge cases in scope: `p = 2`; weight 0 and odd weights; `K` totally real, CM, or with neither; `n = 0`,
   `n = 1` and `n ≤ −1` for `Z(n)`; `ℓ = 2`; `ℓ` equal to or different from the residue characteristics; real places.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you
   attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart.
7. No authority. The transcriptions, the Pro notes, the Codex web notes, the readings, R1-R9 and the Leads (inferences by
   Claude, Anthropic) are all to be checked where used; the Leads in full. If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and you
   go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to deliver

One ZIP containing:
- `RESEARCH_SA05_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement is
  used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), with complete proofs;
  English, first person plural; his statements quoted in French with the page.
- `RESEARCH_SA05_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `RESEARCH_SA05_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA05_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with
  the statement number); then what you read, what you computed (every computation with its scope, inputs, run time and
  output files), and every correction to R1-R9, to the Leads, to the readings and to the transcriptions, with the page.
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

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `RESEARCH_SA05_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `RESEARCH_SA05_checkpoint_<NN>_part<k>.zip`, the file list in the first part.

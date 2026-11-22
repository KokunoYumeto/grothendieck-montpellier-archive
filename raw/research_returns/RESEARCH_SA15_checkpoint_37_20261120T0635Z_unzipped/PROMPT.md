# RESEARCH_SA15: Grothendieck's "Cristaux" dossier. The monodromy of the Hasse-Witt local system of hypersurface sections (cote 4, 8.6), good reduction through p-divisible groups (cotes 9 and 100), and the open steps of the crystal manuscripts (cotes 5-9)

To be settled: Grothendieck's question 8.6 of cote 4, the main question (Part A): for a smooth projective variety `X`
of dimension `n ≥ 2` over a finite field of characteristic `p` and its smooth hypersurface sections `Y` of large degree
`d`, is the monodromy of the `F_p`-local system attached to the semisimple part `E(Y, O_Y)_SS` of the coherent vanishing
cohomology the full linear group, and does every residue mod `p` occur as `card Y(k')` in every non-empty open set of
hypersurfaces? Part A also asks for his "Théorème" 8.5 without hypotheses, the ingredients he admitted, his missing
"n° 7", and his expectation on the lifted variety. Then: Raynaud's semi-stable reduction criterion for `ℓ = p` and the
inertia character of a Barsotti-Tate group (cote 9, Part B); his extension theorem for abelian schemes of 100:3 over
non-reduced and reduced bases (cote 100, Part C); the lifting obstruction of 8:81 and the coherent class of the co-Lie
complex (cote 8, Part D); and eleven open steps of the other sheets (cotes 5-9, Part E).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA15`.
Drafted on 19 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), agent a8d07e7854f1cb9b4, a sub-agent of the main
session, at the main session's word, from the sweep-3 study and readings of the topic SA15 (all by Claude Opus 5.5 at
effort max) and the AI-produced transcriptions of his pages.

Citations: "4:8" is cote 4, scan 8 (the archive's sheet number is the scan number minus one). Item ids (SA15-9,
SA15-19, ...) are those of `sweep2_SA15/WHAT_IS_WHERE.md`.

## What is attached

One file, `RESEARCH_SA15_background.zip` (1.4 MB, 437 files; LaTeX and text only, no PDF); `MANIFEST.tsv` at
its root lists every file with its origin, size and SHA256, and `README.md` maps the folders.
- `sweep3_SA15/`: `STUDY.md` (§1 cote 4, section 8; §2 cote 6, scans 22-27; §3 cote 100, scans 48-53; the readers block
  at the end), `HUNCHES.md`, `RESEARCH_PACKAGES.md`, and the check events and corrections of the whole topic;
  `readings/`: `check_8_5_7.md` (the independent proof of 8.5.7), `c5_c6.md`, `c7_c8.md` and `c9_c100.md` (the readings
  of every page of cotes 5-9 and 100, each with its check events and corrections; hunches are numbered per part).
- `sweep2_SA15/WHAT_IS_WHERE.md`: the items SA15-1 to SA15-20 and their places.
- `transcriptions/`: the AI-produced transcription (GPT-6 Astra, ChatGPT Pro mode) of every page of cotes 4, 5, 6, 7, 8,
  9 and 100, one TeX file per scan (`<package>_<cote>_scanNNN.tex`), with the research notes of the same runs;
  `PREAMBLE.tex` defines the macros (`\unsure{a|b}` a doubtful reading with its alternatives, `\deleted` struck by him,
  `\inserted` his insertion, `\margin` margin text, `\scanpage{N}` scan N, `\mspage{n}` his page number).
- `codex_web/`: a second transcription of cotes 4, 8:79-81, 9 and 100 (GPT-6.2 Astra at reasoning effort max, ChatGPT
  Work), with its notes, mathematical notes and check events.
- `broad_layer/`: the sweep-3 studies, hunches and research packages of the other topics of the cluster (SA05, SA06,
  SA07: motives, cycles, periods), with their item lists, so that you see the connections.
- `hua_project/`: the modernised reading of cote 9 by Michel Hua's project, a witness only; credit any remark you use to
  "Michel Hua's project", quoting a phrase.
- `literature/`: LaTeX sources of Bhatt-Scholze, "Prisms and prismatic cohomology" and "Prismatic F-crystals and
  crystalline Galois representations"; Scholze-Weinstein, "Moduli of p-divisible groups"; Bhatt, "Algebraic geometry in
  mixed characteristic"; Bhatt-Morrow-Scholze, "Integral p-adic Hodge theory" (arXiv:1602.03148); Bergh-Rydh,
  "Functorial destackification and weak factorization of orbifolds" (arXiv:1905.00872); Vasiu-Zink, "Purity results for
  p-divisible groups and abelian schemes over regular bases of mixed characteristic" (arXiv:0909.0969); Achter-Pries,
  "Monodromy of the p-rank strata of the moduli space of curves" (arXiv:0707.2110). Their files are listed in
  `MANIFEST_ADDED_20261119.tsv`. Kisin's "Crystalline representations and F-crystals" and "Moduli of finite flat group
  schemes and modularity" have no arXiv source and are not attached.

Not attached: the scans (the transcriptions are our reading of them; where a reading matters and is in doubt, say so)
and every other source named below. Open each source you use and cite it with its exact theorem numbers.

## Where this comes from

- Grothendieck's dossier "Cristaux" in the Montpellier archive, cotes 4-9, with cote 100:
  - cote 4, section 8, "Une estimation (heuristique) du nombre des valeurs propres de frobenius dans la cohomologie
    évanescente qui sont des unités p-adiques" (it admits a crystalline cohomology "au sens des catégories dérivées",
    "grâce à Berthelot");
  - cote 5: divided powers, and his letter to Deligne of 10 December 1965 "sur coh. p-adiques";
  - cote 6: his letter to Tate (Pisa, May 1966), where crystals are introduced, with his counterexample 2.7; Tate-Hodge
    questions; Barsotti-Tate groups (c. 1969-70);
  - cote 7: the lectures of November-December 1966 (de Rham, Washnitzer-Monsky, Gauss-Manin, the stratifying and
    crystalline sites) and "Anneaux simpliciaux canoniques et modules stratifiés";
  - cote 8: finite groups killed by `p` and their crystal; the Lubin-Tate filtered module; Tannakian structures; the
    co-Lie complex and the lifting obstruction (8:78-81);
  - cote 9: duality over truncated Dieudonné rings; the inertia character of a Barsotti-Tate group; canonical
    stratifications; the Hasse invariant; `dét T_p(A)_ét ≅ dét T_p(A*)_ét` (partly on Pisa paper, 1966-67);
  - cote 100: "Bonne réduction et groupes p-divisibles" (c. 1968: scan 29 is written on the back of a letter dated 24
    February 1968).
- The transcriptions: AI-produced by GPT-6 Astra (ChatGPT Pro mode); cotes 4, 8:79-81, 9 and 100 also by GPT-6.2 Astra at
  reasoning effort max (ChatGPT Work).
- The sweeps, all by Claude Opus 5.5 at effort max: sweep 2 placed the items; sweep 3 (18-19 Nov 2026) read every page of
  the topic and worked the mathematics through: the study (agent a28ea31fa17dd65e1), the check of 8.5.7 (agent
  a922466087ec53798), the readings `c5_c6` (agent a1cf7c6b5992a5d3b with sub-readers a5d23772f38c43927 and
  a486000d1ad547de6), `c7_c8` (agent afcdf31bb407576f5 with sub-readers a28f4edc0783f3d6a and aa78098b7d78d6642) and
  `c9_c100` (agent a8d07e7854f1cb9b4 with sub-reader a8d91f19c2d8f19c1).

## Results this prompt builds on (status on 19 Nov 2026)

None of these is to be proved again as if open, except where a Part requires it. For each one you use: read the proof at
the place given and confirm the step you rely on in a paragraph of your own, or give the exact error with a repair or a
counterexample. All are by Claude Opus 5.5 at effort max (the agents named above) and unrefereed; their check events are
in the CHECK_EVENTS files under the places given.

- **R1 (8.5.7, cote 4: proved twice, independently; `STUDY.md` §1, check event SA15-S3-3; `check_8_5_7.md`).** Let `k`
  be perfect of characteristic `p`, `X ⊂ P^r_k` smooth projective connected of dimension `n ≥ 2`, `Y = X ∩ H` a smooth
  hypersurface section of degree `d ≥ 1`. Then `v: H^{n−1}(X, O_X)_SS → H^{n−1}(Y, O_Y)_SS` is injective: `F^e` maps the
  kernel of `H^{n−1}(X, O_X) → H^{n−1}(Y, O_Y)` into the image of `H^{n−1}(X, O_X(−p^e d))`, which is zero for `e` large.
  General form (`check_8_5_7.md` §6.4): `X` projective integral of dimension `n` with depth `≥ n` at closed points, `L`
  ample, `Y = V(s)`: `F` is nilpotent on `H^j(X, I_Y)` for `j ≤ n − 1`, and `H^i(X, O)_SS → H^i(Y, O)_SS` is bijective for
  `i ≤ n − 2` and injective for `i = n − 1`. So the term `−dim Ker v` disappears from (8.5.5) and 8.5.8, and the "seulement
  si" of 8.5.10 holds without his reservation. Not decided: whether `H^{n−1}(X, O_X) → H^{n−1}(Y, O_Y)` itself is
  injective (`check_8_5_7.md` §6.1).
- **R2 (cote 4; `STUDY.md` §1, check events SA15-S3-1, -2, -4).** Lemma 8.4.3 (for `X` proper over `k`,
  `H^i_DR(X) → H^i(X, O_X)` is bijective on semisimple parts: `F_DR = βα`, `F_O = αβ`); the sheet 8.4.4 a); the unit-root
  count of 8.5.4 granted the crystalline ingredients.
- **R3 (9:13-14; `c9_c100.md`, part 1 §3, check events at 9:14).** (a) Proved: if `A/K` (`K` complete discretely valued of
  characteristic 0 with perfect residue field of characteristic `p ≥ 3`, `μ_p ⊂ K`) has potentially good reduction that
  is ordinary, and `A[p]` is unramified, then `A` has good reduction (the connected part of the `p`-torsion of the Néron
  model over the minimal extension is of multiplicative type, the descent datum on it is forced by the generic fibre,
  and Serre's lemma ends it). (b) Sketched, resting on Kisin's classification and Illusie's lifting theorem: for
  `p ≥ 3` and `K = Q_p(ζ_{p²})` (`e = p(p − 1)`), the Kisin module over `k[[u]]` with `φ(f_1) = u^c f_1`,
  `φ(f_2) = (1 − u^{c−m}) f_1 + u^c f_2`, `m = (p − 1)/2`, `c = pm`, `e = 2c`, gives an elliptic curve `E_0/O_K` with good
  supersingular reduction and `E_0[p] ≅ χ ⊕ χ` (`χ` the ramified quadratic character), and `E = E_0 ⊗ χ` has
  `E[p] ⊂ E(K)` (after an unramified extension) and additive reduction. The Kisin-module dictionary was used, not
  re-derived. His pencil margin "faux par Tate" stands beside the question.
- **R4 (cote 100; `c9_c100.md`, part 2, and the merge check M-1).** The Theorem of 100:3: `S` locally noetherian,
  `U ⊂ S` open, `T = S − U` with residue characteristic `p` at every point; `F: A ↦ (A_U, T_p(A), id)` from abelian schemes
  over `S` to triples `(A_U, M, φ)` (`A_U` abelian over `U`, `M` `p`-divisible over `S`, `φ: M|U ≅ T_p(A_U)`).
  1) `F` is fully faithful when `U` meets every connected component of `S`: proved (100:4-5). 2) "`F` is an equivalence if
  a) some finite surjective `S' → S` has `S'` geometrically unibranch and b) `prof ét_T(S) ≥ 2`": false for
  `S = Spec Z_p[ε]/(ε²)`, `U = S[1/p]` (take `A_U` a non-trivial first-order deformation of an elliptic curve `E_0/Q_p` with
  good reduction and `M` the constant deformation of `E[p^∞]`; by Serre-Tate over every `Z/p^n[ε]`, an `A` over `S` with
  these data is the constant deformation). The gap is his step a) on 100:7, marked "?" twice. Also proved there: case e)
  of 100:15-17 follows from case d) by noetherian induction, without his lemma "Un 'syst local' de schémas abéliens sur un
  schéma [loc. noeth] provient d'un schéma abélien" (circled "Douteux, sans doute faux"); Lemma 1 and Corollaries 1-2 of
  100:23-25 (descent of morphisms along proper epimorphisms); the algebraization criterion of 100:31-37 for formal
  abelian schemes over complete local noetherian rings; the Baire-type Proposition of 100:37-39.
- **R5 (8:81; `c7_c8.md` §1-2 and part 2 §F, re-proved twice).** The extension
  `1 → M_d(F_p) → GL_d(Z/p²) → GL_d(F_p) → 1` splits exactly for `d = 1` and `(d, p) ∈ {(2, 2), (2, 3), (3, 2)}`
  (`p ≥ 5`: no lift of `1 + E_12` has order `p`; `(3, 3)` and `(4, 2)`: the Steinberg relations lifted mod `p²` are
  inconsistent; a block lemma passes to larger `d`). So his "sans doute pas nulle si M_0 de rang d ≥ 2, dans le cas
  universel π = GL(d, F_p)" fails in exactly those three cases; Illusie's identification of the class as the
  obstruction to a free lift over `Z/p²`, and the injectivity of `H²(B_π, −) → H²(S, −)` for the universal covering, are
  right. Open: the coherent class `ξ` (Part D.2).
- **R6 (9:24-29; `c9_c100.md`, part 1 §4).** For an ordinary abelian scheme `A` over a base of characteristic `p` with a
  polarization `φ`, `α_A = dét(T_p(φ̃)_ét)/√(deg φ̃): dét T_p(A)_ét ≅ dét T_p(A*)_ét` is an isomorphism of `Z_p`-lines,
  independent of `φ` (his a): `Δ(u)Δ(u*) = deg u`, Rosati symmetry, positivity of `Δ(v²) = Δ(v)²` on the real symmetric
  elements) and integral (his b): self-duality of `Ker φ̃`); c) `α_{A*} = α_A^{−1}` up to the sign `(−1)^g` of the
  biduality convention. Open: d) and the transport of the Hasse invariant (E.8-E.9).
- **R7 (9:16-18; `c9_c100.md`, part 1 §4).** A `k`-stratification of `DR¹(A/Λ)` on all infinitesimal deformations `A/Λ` of
  `A_0`, compatible with base change, functorial in `A` and compatible with `F` and `V`, exists only if `A_0` is ordinary;
  it then splits `DR¹ = t_A^∨ ⊕ t_{A*}` by `Im F`, is unique, and makes the Hodge filtration horizontal (his Remarque).
- **R8 (9:5-8).** With `A = W[F, V]` and `A_n = A/(F^{n+1}, V^{n+1})` (exponent checked on the scan), the trace form
  `⟨x, y⟩ = φ(xy)` (`φ` the constant term) gives a bimodule isomorphism `A_n ≅ Hom_{W_{n+1}}(A_n, W_{n+1})`; his
  `Hom_{W_n}(A_n, W_n)` is an index slip; his two dualizing functors agree.
- **R9 (cote 6; `STUDY.md` §2, `c5_c6.md`).** 6:27, section 2.7: no stratification of `H¹_DR(A/S)` relative to `k`,
  functorial and compatible with base change, exists for all elliptic schemes (Frobenius would be horizontal, and
  `F² = 0` at a supersingular point would spread). The assertions 1º-3º of 6:22-24 hold for nilpotent PD thickenings
  (Messing; Mazur-Messing; Berthelot-Breen-Messing). The table "Verdicts on thickenings" in `c5_c6.md`, part 2.
- **R10 (7:16-17; `c7_c8.md` §1).** For `X` smooth proper over `k` algebraically closed of characteristic `p`,
  `H^i_str(X/k, O_X) = H^i(X, O_X)_ss = H^i(X_ét, F_p) ⊗ k`; for an ordinary abelian scheme `X_0` the cohomology of his
  crystalline (infinitesimal) site over `W` vanishes above `dim X_0`.
- **R11 (5:39-41; `c5_c6.md`, part 1).** For a `Z_(p)`-algebra and `π: I → I` with `π(fx) = f^p π(x)` and
  `π(x + y) = π(x) + π(y) + Σ_{0<i<p} x^i y^{p−i}/(i!(p − i)!)`, one has `x^p = p! π(x)`; his constants are
  `c_n = (p!)^{v_p(n!)}/n!`, and `c_n ≡ 1/(a_0! a_1! ⋯) mod p` (`a_i` the base-`p` digits of `n`), so his "Est-ce tjs 1?"
  is no for `p ≥ 3`.
- **R12 (100:48-53; `STUDY.md` §3).** Over a trait, a morphism from the generic fibre of a `p`-divisible group to a Néron
  model with semi-abelian generic fibre extends uniquely ("le th. de Raynaud"); good reduction iff the `p`-divisible group
  extends; his handwritten extension to every group with a Néron model is right.

## Leads

Each is an inference of the model named, checked by no one. Each is to be proved or refuted in full, inside the Part it
serves.

- **Lead A (A.3-A.5; `HUNCHES.md` H1-H2, Claude Opus 5.5 at effort max, agent a28ea31fa17dd65e1).** The answer to 8.6 is
  yes for `d` large: the monodromy of `E(Y, O_Y)_ss` over `U_d` is all of `GL(V)`, and every residue mod `p` occurs; the
  ordinary loci of other families have the largest `p`-adic monodromy (Jacobians of curves, the ordinary locus of `A_g`);
  his missing "n° 7" is a generic ordinarity statement for hypersurface sections.
- **Lead B (B.1-B.3; `c9_c100.md` H1-1, Claude Opus 5.5 at effort max, agent a8d07e7854f1cb9b4).** "Faux par Tate" records
  a counterexample to Raynaud's criterion with `ℓ = p`, necessarily with non-ordinary reduction; R3(b) is one.
- **Lead B' (B.4; `c9_c100.md` H1-2, the same agent).** His character of 9:12 is the trace of inertia on the
  Weil-Deligne representation that Fontaine attached to potentially crystalline representations; his question whether it
  is determined by `_pM` is the question of how the inertial type relates to the reduction mod `p`.
- **Lead C (C.4; `c9_c100.md` H2-4 and H2-5, the sub-reader a8d91f19c2d8f19c1, Claude Opus 5.5 at effort max).** The lemma
  of 100:17 is true for `S` normal; on a nodal curve, local data twisted by `−1` at the node do not glue.
- **Lead D (D.2; `c7_c8.md` H2-1, the sub-reader aa78098b7d78d6642, Claude Opus 5.5 at effort max).** `ξ` is the image of
  `ξ_Λ` under `H²(S, End(M)) → H²(S, End(M) ⊗ O_S)`, whose kernel is the image of `H¹(S, End(E))` under the
  Artin-Schreier boundary; for `S` proper over a perfect field with `π_1(S) → GL_d(F_p)` onto and `(d, p)` outside the
  split cases, `ξ ≠ 0`: the co-Lie complex of `D(M)` is not formal.
- **Lead E1 (E.1; `c5_c6.md` part 1 H2, the sub-reader a5d23772f38c43927, Claude Opus 5.5 at effort max).** The PD
  structures on `I` are exactly the maps `π` with the two rules of R11.
- **Lead E3 (E.3; `c7_c8.md` H1-8 and HM-1, the sub-reader a28f4edc0783f3d6a and agent afcdf31bb407576f5, Claude Opus 5.5
  at effort max).** Without divided powers, crystals see only the slope-0 part:
  `H^i((X_0/W)_inf, O) = H^i_ét(X_0, Z_p) ⊗ W`.
- **Leads E4, E5, E6, E10 (`c7_c8.md` H1-4, H1-5, H1-3, H1-2, the sub-reader a28f4edc0783f3d6a); Lead E7 (`c7_c8.md` H2-3,
  the sub-reader aa78098b7d78d6642); Lead E9 (`c9_c100.md` H1-3, agent a8d07e7854f1cb9b4); Lead E11 (`c5_c6.md` part 2 H3,
  the sub-reader a486000d1ad547de6); all Claude Opus 5.5 at effort max:** as stated in those files.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (the variety, curve, abelian scheme, group, base or module given completely, with the
verification of every hypothesis and of the failure; checked by a program when finite or computable) and the strongest
true statement proved in its place. Nothing else finishes an item. Partly settled is not an outcome. The cases proved,
the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an
item you are still working on: record them as you go, then attack the obstruction, starting from that instance.
"Known" counts only with the derivation of the statement used here from the cited theorem, after opening the source.
An item that begins with "Determine" is done when the object asked for is given explicitly, with a proof that it is
the whole answer.

For Part A in particular.
- "For `d` large" means: for every `d ≥ d_0`, with `d_0` given explicitly in terms of `X` (its embedding and its
  cohomology), or a proof that no such `d_0` exists.
- A monodromy statement names the group (the geometric fundamental group `π_1(U_d ⊗ k̄)` or the arithmetic `π_1(U_d)`),
  the base point, the local system with its `F_p`-structure (8.4.2), and the group it is claimed to fill. A statement for
  `X = P²` is a special case and is said to be one.
- Every computation (Hasse-Witt matrices, Cartier operators, point counts, monodromy of explicit families) is given with
  its program, inputs and output, and with a proof that it shows what it is used for.

For Parts B and C. A counterexample is given with its field (ramification index, residue field), its curve, abelian
scheme or group (explicit equations, or a construction every step of which is proved), and the verification of every
hypothesis. Where a Kisin, Breuil or Dieudonné module is used, the dictionary is stated with its theorem number and its
conventions (covariant or contravariant, which Frobenius twist), and the step it carries is checked.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1-R12 again in place of the
items, except where a Part asks for it; a result of the readings used without the check above; a statement for all `d`
(all `X`, all `p`, all `e`) proved for some, without saying so; a step that replaces a claim by a convenient special case
without naming it; a reading of his pages changed to fit the mathematics without saying what the transcription reads and
why you read it otherwise.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA15_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Unit-root eigenvalues in the vanishing cohomology of hypersurface sections, and the monodromy of the Hasse-Witt
local system (cote 4, section 8). The main question is A.4-A.5.**

Setting (4:3-12; `STUDY.md` §1): `k` perfect of characteristic `p > 0`; `X ⊂ P^r_k` smooth projective connected of
dimension `n ≥ 2`; `Y = X ∩ H` smooth of dimension `n − 1`, `H` a hypersurface of degree `d ≥ 1`; `H^i(X) = H^i_cris(X/W(k))`,
`Tors^i(X)` its torsion, `_pTors^i(X)` its `p`-torsion; `E(Y) = Coker(u_0: H^{n−1}(X) → H^{n−1}(Y))`;
`E(Y, O_Y) = Coker(H^{n−1}(X, O_X) → H^{n−1}(Y, O_Y))`; `(−)_SS` the semisimple part for the `p`-linear Frobenius (8.4);
`v` as in R1; `φ: (E(Y) ⊗_W k)_SS → E(Y, O_Y)_SS` the map of (8.5.1); `U_d` the open set of 8.5.9 (`Y` smooth and
`E(Y, O_Y)_SS` of maximal rank); `V` the `F_p`-local system on `U_d` that 8.4.2 attaches to `E(Y, O_Y)_SS`.

1. (The ingredients he admits: 8.3, "Nous admettrons", and 8.5.) Decide, for every `X` and every smooth `Y` of every
   degree `d ≥ 1`: (a) `E(Y)` is torsion-free; (b) `u_0` induces `Tors^{n−1}(X) ≅ Tors^{n−1}(Y)` (8.3.1); (c) `Ker u_0 = 0`
   (8.3.3); (d) his reading (4:4, 4:6) of the map he numbers (8.2.1), the map `u_2` of (8.1.4) taken through Poincaré
   duality, as the map `u''_2: Tors^{n−1}(X) ⊗ k → Tors^{n+1}(X) ⊗ k` induced by the cup product with the class of the
   polarization (8.3.2), so that its kernel does not depend on `Y` (there is no section 8.2 on the pages: say what (8.2.1)
   must be). Where one fails, give the
   counterexample and determine the degrees `d` for which it holds. Decide also whether the restriction
   `H^{n−1}(X, O_X) → H^{n−1}(Y, O_Y)` is injective for every smooth `Y` (R1 leaves it open; for `n = 2` the question is
   whether `H¹(X, O_X(−d)) → H¹(X, O_X)` can be non-zero).
2. (Théorème 8.5 without hypotheses.) Prove 8.5 for every `X` and `Y` as above, with the exact hypotheses on `d` that each
   step needs: the exact sequence (8.5.1) with `Ker v = 0` (R1), (8.5.5) and (8.5.6); the unit-root count of 8.5.4 (for
   `k` finite, the rank of `(E(Y) ⊗_W k)_SS` equals the number of eigenvalues of geometric Frobenius on the vanishing part
   of `H^{n−1}`, `ℓ`-adic for any `ℓ ≠ p`, that are `p`-adic units, counted with multiplicity; make explicit the comparison
   of characteristic polynomials you use); 8.5.10 in both directions (`φ` is bijective iff `(_pTors^n(X))_ss = 0`); and
   his remark on the sheet 8.4.4 (4:2), "Sans doute (*) et (**) sont transposés l'un de l'autre".
3. (His "n° 7" and 8.5.8.) Prove or refute: for every `X` there is `d_0` such that for every `d ≥ d_0` the generic value
   of `dim E(Y, O_Y)_SS` is positive. Determine that generic value, in particular whether the generic `Y` of large degree
   has Frobenius bijective on `E(Y, O_Y)` (for complete intersections in projective space, compare with Illusie,
   "Ordinarité des intersections complètes générales", Grothendieck Festschrift II, 1990, after opening it). Decide his
   parenthesis on 4:9: is the non-vanishing of the number of unit roots for these `Y` equivalent to `E(Y)` having Hodge
   level `n − 1` (`E(Y, O_Y) ≠ 0`)? If not, give the `X` (with `p`-torsion, as in Serre's example of 8.5.11) where it
   fails.
4. (8.6, the main question.) Determine the image of the geometric fundamental group `π_1(U_d ⊗ k̄)` in `GL(V)`, and decide
   whether `V` is irreducible, for every `X` with `n ≥ 2` and every `d ≥ d_1(X)`, `d_1` explicit. His question is whether
   the image is all of `Aut(V)`. Settle `X = P²` first (smooth plane curves of degree `d`; over the ordinary locus `V` is
   dual to the étale `p`-torsion of the Jacobian, of rank `(d − 1)(d − 2)/2`), then `X = P^r`, then every `X`; where the
   image is smaller than `GL(V)`, determine it. Determine also the image of the arithmetic fundamental group `π_1(U_d)` and
   the determinant character of `V`, with its relation to the Hasse invariant of the family.
5. (8.6, the consequence.) For `k` finite and `d` as in A.4, prove or refute: every non-empty open set `U` of the space of
   hypersurfaces of degree `d` in `P^r_k` contains, over some finite extension `k'` of `k`, a `Y` with
   `card Y(k') ≡ a mod p`, for every `a ∈ F_p` given in advance. His route (4:9-12): the "Woods Hole formula" (`card Y(k')`
   mod `p` as the alternating trace of Frobenius on the `H^i(Y, O_Y)`; SGA 4½, "Fonctions L modulo ℓ^n et modulo p"),
   Chebotarev's density theorem on `U_d`, and the constant contribution of `X` made trivial by enlarging `k`. If the
   monodromy is smaller than `GL(V)`, decide the statement directly. For `X = P²` state the result for plane curves
   explicitly: for each `d`, the residues of `card Y(k')` mod `p` that occur.
6. (8.5.10, the lifted variety.) He expects that when `X` lifts with its polarization to characteristic 0, the condition
   `(_pTors^n(X))_ss = 0` can be expressed by the analogous condition on the torsion of the `p`-adic cohomology of the
   lift. Determine the exact relation between `(_pTors^n(X))_ss`, the étale cohomology `H^n_ét(X_k̄, Z_p)` of `X` and the
   étale cohomology `H^n_ét(X_K̄, Z_p)` of the generic fibre of a smooth projective lift, prove it, and decide his
   expectation; a counterexample if it fails.

**B. Good reduction through `p`-divisible groups: the inertia character and Raynaud's criterion for `ℓ = p` (cote 9,
9:10-14, with 100:48-53).** This Part comes after Part A and is governed by the same rules, the push rule and the
three-hour check.

Setting (9:11-12): `V` a complete discrete valuation ring with perfect residue field `k` of characteristic `p` and fraction
field `K` of characteristic 0. A `p`-Barsotti-Tate group `M` over `K` "satisfies the monodromy condition" if it has a
composition series whose graded pieces acquire good reduction over a finite separable extension `K'`. His character of
`M` is the trace of the inertia `I ⊂ Gal(K'/K)` on the Dieudonné modules of the special fibres of the good-reduction
models over the normalization `S'` of `S` in `K'` (maps (1)-(5) of 9:11-12), viewed as a function on the inertia subgroup
of `Gal(K̄/K)`. His indexing: `M(ν)` is the kernel of `p^{ν+1}`, so `M(0) = _pM`.

1. (9:13-14.) Decide: for `p ≥ 5`, and for `p = 3`, is there `K` as above with `μ_p ⊂ K` and an elliptic curve `E/K` with
   `E[p] ⊂ E(K)` and additive (potentially good) reduction? Complete R3(b) with every step proved: Kisin's classification
   over `k[[u]]` with its conventions, the character attached to `φ(e) = u^c e`, the special fibre read from `𝔐/u𝔐`, the
   full faithfulness of the restriction to `G_{K_∞}` on flat representations, Illusie's lifting of truncated
   Barsotti-Tate groups, Serre-Tate and algebraization; or give a different complete construction. Then give one explicit
   example (a field `K` and a Weierstrass equation over it) and verify by computation that `E[p] ⊂ E(K)` and that the
   reduction is additive. Decide his "cas test" of 9:13: are there two elliptic curves over `K ∋ μ_p` with potentially
   good reduction and isomorphic `p`-torsion whose trace functions on the inertia elements of order prime to `p` differ
   (Lead: `E` and a canonical lift of an ordinary curve)?
2. (The range.) Prove R3(a) in full for abelian varieties of every dimension (`p ≥ 3`). Then, for elliptic curves and
   each `p ≥ 3`, determine the set of ramification indices `e = e(K/Q_p)` (multiples of `p − 1`, since `μ_p ⊂ K`) for which
   a curve as in B.1 exists, and which semistability defects (the order of the inertia acting on the reduction: 2, 3, 4,
   6) occur; decide in particular `K = Q_p(ζ_p)`.
3. (Higher torsion.) For `ν ≥ 1`, decide for which `(p, e, ν)` there is an elliptic curve `E/K` with `E[p^ν] ⊂ E(K)` and
   additive reduction. If for fixed `(p, e)` there is a level beyond which `E[p^ν] ⊂ E(K)` forces good reduction,
   determine the least such `ν`; then answer the same question for abelian varieties of dimension `g`.
4. (His question of 9:12-13.) With `μ_p ⊂ K`, the character of `M` is not determined by `M(0)` (B.1). Determine, for given
   `p`, `e` and height `h`, the least `ν` such that the character on the inertia elements of order prime to `p` of every
   `M` satisfying the monodromy condition is determined by `M(ν)`, or prove that no such `ν` exists. Prove or refute
   Lead B'.

**C. Extending abelian schemes across characteristic `p` (cote 100, 100:3-45).** This Part comes after Part A and is
governed by the same rules, the push rule and the three-hour check. `F` and the hypotheses a), b) are those of R4.

1. Prove or refute: under a) and b), `F` is an equivalence if and only if `O_{S,t}` is reduced for every `t ∈ T`.
   Determine the essential image of `F` for every locally noetherian `S` satisfying a) and b), reduced or not: prove an
   exact criterion (for instance: the triples whose two deformations of `A_{U_red}` over `U`, the one given by `A_U` and
   the one given by `M` through Serre-Tate over the formal completion of `S` along `T`, agree over that formal completion
   minus `T`), and give the strongest true form of his 2) for non-reduced `S`.
2. Prove 2) for every reduced `S` satisfying a) and b), including the case where the normalization of `S_red` is not finite
   over `S` (his "O.K." on 100:11, with a reference "[ ] p 75-76" that we have not identified), or refute it in that case.
3. (Corollary 3 of 100:25.) Decide: is every proper epimorphism `f: S' → S` of noetherian schemes (`O_S → f_* O_{S'}`
   injective) a morphism of descent for `p`-divisible groups (`Hom_S(G, H) → Hom_{S'}(G', H') ⇉ Hom_{S''}(G'', H'')`
   exact)? His route needs `Hom(G, H)` to be formally unramified and a passage to the limit that the page does not give
   (the finite levels are not unramified: `Hom(α_p, α_p) = G_a`).
4. (The lemma of 100:17, "Douteux, sans doute faux".) Call a local system of abelian schemes on a locally noetherian `S`
   a family of abelian schemes `A(s)` over `Spec O_{S,s}`, `s ∈ S`, with isomorphisms for every generization, compatible
   with composition. Decide whether every local system comes from an abelian scheme over `S`: for `S` normal, for `S`
   reduced, for `S` arbitrary; give the counterexample where it fails (Lead C).

**D. The lifting obstruction of 8:81 and the coherent class of the co-Lie complex (cote 8, 8:78-81).** This Part comes
after Part A and is governed by the same rules, the push rule and the three-hour check.

1. Check R5 against the literature (Sah's work on the cohomology of split extensions; Serre, "Abelian ℓ-adic
   representations and elliptic curves", chapter IV; any later classification), and determine likewise for which
   `(d, p)` the extensions `SL_d(Z/p²) → SL_d(F_p)` and `Sp_{2g}(Z/p²) → Sp_{2g}(F_p)` split.
2. Decide Lead D: for `S` proper over a perfect field of characteristic `p` (smooth if you need it), `M` an étale
   `F_p`-local system of rank `d` with monodromy `GL_d(F_p)`, `G = D(M)` and `E = M ⊗ O_S`, is the class
   `ξ ∈ H²(S, End(E))` of 8:80-81 (the class of the co-Lie complex of `G` as an extension of `ω_G = E` by `n_G[1] = E[1]`)
   non-zero for some such `S` when `(d, p)` is outside the split cases? Give `S` explicitly with a proof that `ξ ≠ 0`, or
   prove `ξ = 0` for every `S`.

**E. The open steps and the sharpest hunches of the other sheets (cotes 5-9).** This Part comes after Part A and is
governed by the same rules, the push rule and the three-hour check.

1. (5:41; R11; Lead E1.) Decide: for a `Z_(p)`-algebra `A` and an ideal `I`, are the PD structures on `I` exactly the maps
   `π: I → I` satisfying the two rules of R11 (with `γ_p = π` and his formula for the `γ_n`)?
2. (6:6-7, 1.8: "Sauf erreur, on a encore une équivalence ... si S → R est plat et localement de présentation finie ... mais
   je n'ai pas écrit de démonstration".) Decide: for `S → R` flat and locally of finite presentation, not smooth, is the
   category of crystals of `O_S`-modules on the infinitesimal site of `S` over `R` equivalent to the category of
   `O_S`-modules with a stratification relative to `R`? (`c5_c6.md`, part 2 §2: the test `S = Spec k[ε]/(ε²)` passes.)
3. (7:16-17; Lead E3.) Decide: for `X_0` smooth and proper over `k` algebraically closed of characteristic `p`, is
   `H^i((X_0/W)_inf, O) ≅ H^i_ét(X_0, Z_p) ⊗_{Z_p} W` for every `i` (the infinitesimal site over `W`, without divided
   powers)?
4. (7:70-72; Lead E4.) Decide whether the intrinsic complex of 7:70 (the Čech nerve of `X → X_dR`: the formal completions
   of the `X^{i+1}` along the diagonals) computes the de Rham (infinitesimal) cohomology of `X` when `X` is singular;
   settle the cusp `Spec C[t², t³]` explicitly.
5. (7:24 corrected; Lead E5.) Prove or refute: for an affine curve `C` over `C` with plane singularities, `dim H¹` of the
   Kähler de Rham complex of `C` equals `b_1(C) + Σ_x (μ_x − τ_x)` (Milnor and Tjurina numbers); give the corresponding
   statement for `H²`.
6. (7:42-43, "Il semble que le théorème suivant soit vrai"; Lead E6.) Decide, integrally and not only after `⊗ Q`: for
   `A_0` smooth over `k` with Washnitzer-Monsky lifts `A`, `A'` and `u_0: A_0 → A'_0`, is `u*` on `H*(Ω•_{A†/W})` independent
   of the lift `u` of `u_0`, and is `H*(Ω•_{A†/W})` determined by `A_0` up to canonical isomorphism?
7. (8:48-50; Lead E7.) For the Lubin-Tate group `G` of `(A, π)` over `A` (`K/Q_p` finite with ramification `e`), and
   `t_G = π^{−α} Ω^∨` in the notation of 8:48-50: determine `α` as a function of `A`, and decide his question whether
   `D*(G)` and `M` are the same lattice of `M_K` (the page gives `α = 0` when `e < p − 1`).
8. (9:22.) Decide: under `ω_A ≅ ω_{A*}` (the determinant of the Hodge sequence and the trace `H^{2g}_DR(A/S) ≅ O_S`), does
   the Hasse invariant `σ_A ∈ Γ(ω_A^{⊗(p−1)})` go to `σ_{A*}` for every abelian scheme over an `F_p`-scheme, exactly or up
   to a sign you determine?
9. (9:29, c) and d).) Determine the sign in `α_{A*} = ±α_A^{−1}` for the standard identification `A ≅ A**`. Decide d): on
   the ordinary locus, is `α_A` mod `p` (on determinants) equal, up to a sign and an inverse you determine, to the
   isomorphism `dét(_pA)_ét ≅ dét(_pA*)_ét` that `ω_A ≅ ω_{A*}` induces on the `F_p`-structures (9:22)? Search the
   literature for `α_A` itself.
10. (7:17-19, the site of Washnitzer-Monsky lifts; Lead E10.) Take his site of 7:18 as written: triples `(U_0, Ṽ, i)` with
    `U_0` an affine open of `X_0`, `Ṽ` the affine Washnitzer-Monsky space of a W-M algebra `B` over `W`, and `i` a nilpotent
    immersion `U_0 → Ṽ ×_S s` (a surjection `B → A_0` with `B/pB → A_0` of nilpotent kernel), with a Zariski-type
    topology. Decide his two tests of 7:19: a) for `X_0` smooth affine its cohomology is Washnitzer-Monsky cohomology; b)
    for `X_0` smooth proper with a smooth proper lift it is the de Rham cohomology of the lift, "au moins mod torsion"; and
    decide whether after `⊗ Q` it is rigid cohomology for every smooth `X_0`.
11. (6:14, "principe d'approche transcendante"; Lead E11.) Decide: if `S` is smooth over a perfect field `k` and has a
    proper smooth lift `X` over `W(k)` whose complex fibre (for an embedding `W(k) → C`) is simply connected, is every
    convergent `F`-isocrystal on `S` constant? (Compare with the work of Esnault and Shiho on convergent isocrystals of
    simply connected varieties, after opening it.)

**F. Statement of results.**

1. For the companion to the "Cristaux" dossier: every statement of Parts A-E with what this run and R1-R12 prove, in his
   notation, with the pages it settles.
2. The literature record: for every source named in this prompt and every source you use, one line: opened, with the
   numbers of the theorems that contain or come closest to each statement you prove; or not obtained, with what you
   tried. Say what you searched for A.3-A.5, B.1-B.4, C.1-C.4, D.2 and E.9 in particular: monodromy of unit-root or étale
   `p`-torsion local systems of families of hypersurfaces and plane curves; generic ordinarity; Raynaud's criterion with
   `ℓ = p` (SGA 7 I, exposé IX); extension of abelian schemes over bases of dimension `≥ 2` (Faltings-Chai, chapter V;
   Vasiu-Zink); the canonical isomorphism `α_A`; the co-Lie complex of `D(M)`.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: the field (perfect or not, finite or not), the characteristic, the dimension,
   the degree, the base (reduced or not, normal or not), the ramification index, the coefficients (`W`, `W_n`, `F_p`,
   `Z_p`, `Q_p`), whether up to isomorphism or up to isogeny. Do not replace it by a convenient special case. If you prove
   a special case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property you use
   (semilinear for which Frobenius; a morphism of crystals, of `F`-crystals, of local systems, of group schemes; over
   which base). Compositions must type-check.
3. Every reduction ("we may assume", "after a finite extension", "replace `S` by its strict henselization", "pass to the
   generic point") comes with a proof that the property needed transfers in the direction needed.
4. Conventions are named and kept: covariant or contravariant Dieudonné theory; `σ` or `σ^{−1}`; the sign of the
   identification `A ≅ A**`; Cartier duality; his indexing `M(ν) = ker p^{ν+1}`; geometric or arithmetic Frobenius.
5. Check the edge cases in scope: `p = 2` and `p = 3`; small `d`; `n = 2` and `n ≥ 3`; `e < p − 1`, `e = p − 1` and
   `e > p − 1`; ordinary, non-ordinary and supersingular reduction; non-reduced, non-normal and non-excellent bases; `k`
   not perfect where his statements allow it.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you
   attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart.
7. No authority. The transcriptions, the Pro notes, the Codex web notes, the readings, R1-R12 and the Leads (inferences by
   Claude, Anthropic) are all to be checked where used; the Leads in full. If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and you
   go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to deliver

One ZIP containing:
- `RESEARCH_SA15_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement is
  used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), with complete proofs;
  English, first person plural; his statements quoted in French with the page.
- `RESEARCH_SA15_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `RESEARCH_SA15_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA15_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with
  the statement number); then what you read, what you computed (every computation with its scope, inputs, run time and
  output files), and every correction to R1-R12, to the Leads, to the readings and to the transcriptions, with the page.
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

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `RESEARCH_SA15_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `RESEARCH_SA15_checkpoint_<NN>_part<k>.zip`, the file list in the first part.

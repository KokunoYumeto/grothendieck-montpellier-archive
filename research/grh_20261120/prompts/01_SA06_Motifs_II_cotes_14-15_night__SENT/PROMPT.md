# RESEARCH_SA06: Grothendieck's "Théorie des motifs II" (cotes 14 and 15). The Deuring element and the adelic μ₂-torsor of the supersingular elliptic curves (15:16-78), Frobenius eigenvalues in every weight (15:88-133), the conjectures of the letter to Serre after Griffiths' quintic and the Lefschetz programme for cycles (cote 14), and the real fibre functors of motives over finite fields (15:110-205)

To be settled: the main question (Part A) is the Deuring element `ξ_p` of 15:50, which 15:54-56 set up as a rule on
rank-2 F-crystals with an action of a maximal quaternion order and never determine: determine it, prove the adelic
construction around it (the canonical torsor `𝒯` under `H¹(𝔸, μ₂)`, the gerbe `𝔊(ξ_p)` and its section, with the sign
at infinity that 15:48 and 15:50 leave open), the rigidified equivalence that 15:36 marks "À vérifier!!", the quaternionic
realization of 15:52 and the canonical determinant of 15:21-22. Then: his strong and weak conjectures on Frobenius
eigenvalues in every weight (15:100-106; Part B); the conjectures A, A′, A″, B of his letter to Serre of 27 August 1965
(14:44-47), which are false as written modulo algebraic equivalence, with their correct form, the claim ③ of 14:112 and
the Questions of 14:71 (Part C); the real fibre functors, polarizations and the canonical involution of motives over
finite fields (15:110-125, 15:183-187; Part D); and the other open steps of the two cotes (Part E).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA06`.
Drafted on 19 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), agent add83e0c4fe84ce66, a sub-agent of the main
session, at the main session's word, from the sweep-3 study and readings of the topic SA06 (all by Claude Opus 5.5 at
effort max) and the AI-produced transcriptions of his pages.

Citations: "15:54" is cote 15, scan 54 (the archive's sheet number is the scan number minus one). Item ids (SA06-8,
SA05-19, ...) are those of `sweep2_SA06/WHAT_IS_WHERE.md` and the broad layer.

## What is attached

One file, `RESEARCH_SA06_background.zip` (1.3 MB, 415 files; LaTeX and text only, no PDF); `MANIFEST.tsv`
at its root lists every file with its origin, size and SHA256, and `README.md` maps the folders.
- `sweep3_SA06/`: `STUDY.md` (§1 Weil numbers and CM fields, 15:96-108 and 128-133; §2 commutative motivic Galois groups,
  15:84-86 and 135-137; §3 Deuring categories, the Brandt Picard category and the Deuring element, 15:34-78),
  `HUNCHES.md`, `RESEARCH_PACKAGES.md`, the check events and corrections of the study; `readings/c14_c15rest.md` (the
  reading of every page of cote 14 and of cote 15, scans 87-95, 109-126, 138, 170-206: an overview, then part 1, cote 14,
  scans 2-58; part 2, cote 14, scans 59-132; part 3, cote 15), with its check events and corrections.
- `sweep2_SA06/WHAT_IS_WHERE.md`: the items SA06-1 to SA06-17 and their places (the readings correct some places).
- `transcriptions/`: the AI-produced transcription (GPT-6 Astra, ChatGPT Pro mode) of the pages these questions rest on:
  cote 14 (scans 2-44, 87-132), cote 15 (scans 2-228) and the neighbouring packages, one TeX file per scan
  (`<package>_<cote>_scanNNN.tex`), with the research notes of the same runs; `PREAMBLE.tex` defines the macros
  (`\unsure{a|b}` a doubtful reading with its alternatives, `\deleted` struck by him, `\inserted` his insertion, `\margin`
  margin text, `\scanpage{N}` scan N, `\mspage{n}` his page number).
- `codex_web/`: a second transcription with notes and mathematical notes (GPT-6.2 Astra at reasoning effort max, ChatGPT
  Work). For cote 14, scans 45-86 (runs K14-04, K14-05, K14-06: the letter to Serre, the "Sorites", the degree-1
  Lefschetz argument) it is the only transcription.
- `broad_layer/`: the sweep-3 studies, hunches and research packages of the other topics of the cluster (SA05: the
  motivic gerbe of `F_p` on 15:2-14 and the Deuring categories of 15:16-22; SA07: periods and Hodge; SA15: crystals), with
  their item lists, and the SA05 reading of 15:139-178.
- `hua_project/`: the modernised readings of cotes 14 and 15 by Michel Hua's project, a witness only; credit any remark
  you use to "Michel Hua's project", quoting a phrase.

- `literature/`: LaTeX sources of Milne, "The Tate conjecture over finite fields (AIM talk)" (arXiv:0709.3040) and "Polarizations and Grothendieck's standard conjectures" (arXiv:math/0103175); Lichtenbaum, "The Weil-étale topology for number rings" (arXiv:math/0503604); Debarre-Ein-Lazarsfeld-Voisin, "Pseudoeffective and nef classes on abelian varieties" (arXiv:1003.3183). Their files are listed in `MANIFEST_ADDED_20261119.tsv`.
Not attached: the scans (the transcriptions are our reading of them; where a reading matters and is in doubt, say so),
and every source named below. Open each source you use and cite it with its exact theorem numbers.

## Where this comes from

- Grothendieck's dossier "Théorie des motifs II" in the Montpellier archive:
  - cote 14: "Structure d'effectivité" (14:2-15); "Équivalence d'Albanese et de Picard des cycles algébriques" and
    "Théorie de l'équivalence d'Albanese des cycles" (14:17-39); "Astuce de Tate sur les cycles décomposables"
    (14:40-42); a typed copy of his letter to Serre of 27 August 1965 (14:44-47; printed in the Correspondance
    Grothendieck-Serre, SMF 2001, pp. 232-234, "Thil, 27.8.1965", with differences listed in the reading); "Sorites sur
    VA, Picard, Albanese" (14:48-58) and its § 2 on the algebraicity of homomorphisms (14:59-71); abelian varieties up to
    isogeny (14:74-89); "Anneaux de classes de cycles" (14:91-92); "Mumford-Nakai / Cycles algébriques amples"
    (14:93-100); "conjectures de Lefschetz pour cycles Algébriques ... Conjectures locales" (14:102-117); boundedness and
    0-cycles (14:118-131);
  - cote 15: "Groupe de Galois motivique commutatif. Cas d'un corps de base fini" (15:2-14); Deuring categories
    (15:16-22, 15:34-78); the compact part of commutative motivic groups and the Weil numbers (15:84-138); the agenda
    "Foncteurs fibres motiviques, et groupes fondamentaux motiviques" (15:170); "Calculs de cohomologie absolue des
    Motifs de Tate Z(n)" (15:172-180); "Généralités fonctoriello-catégoriques sur la distribution des frobenius dans les
    groupes de Galois motiviques" (15:182-187); "Théorie de Galois des Motifs" and "Foncteurs fibres motiviques et groupe
    fondamental motivique" (15:189-228).
- The transcriptions: AI-produced by GPT-6 Astra (ChatGPT Pro mode); a second transcription of most pages, and the only
  one of 14:45-86, by GPT-6.2 Astra at reasoning effort max (ChatGPT Work).
- The sweeps, all by Claude Opus 5.5 at effort max: sweep 2 placed the items; sweep 3 (18-19 Nov 2026) worked the
  mathematics through: the study (agent a28ea31fa17dd65e1), the reading `c14_c15rest` (agent add83e0c4fe84ce66 with
  sub-readers a0012f1ff34e51fa6 and a18fb27f7c0e6640f), and the SA05 study and reading (agents a28ea31fa17dd65e1 and
  a7b7747fd6dd29f87).

## Results this prompt builds on (status on 19 Nov 2026)

None of these is to be proved again as if open, except where a Part requires it. For each one you use: read the proof at
the place given and confirm the step you rely on in a paragraph of your own, or give the exact error with a repair or a
counterexample. All are by Claude Opus 5.5 at effort max (the agents named above) and unrefereed; their check events are
in the CHECK_EVENTS files under the places given. "Reading" means `readings/c14_c15rest.md`; "P3-nn" is row nn of its
third part's check events.

- **R1 (15:74-78; `STUDY.md` §3, check event SA06-S3-4).** Under his condition (C) (bi-ideals commute, `LM = ML`) the
  commutativity constraint on `Eq(C)` does not depend on the object; the `Eq(C)` are strictly commutative Picard
  categories, all canonically equivalent to one Brandt Picard category `B`; `C′ ↦ Eq(C, C′)` is an equivalence from the
  Deuring categories to the torsor-categories under `B`. Consequence: the Gr-category class of 15:19 vanishes (a strictly
  commutative Picard category over a point is split: SGA 4 XVIII 1.4). (C) holds for maximal orders.
- **R2 (15:40-44; `STUDY.md` §3, SA06-S3-1 to -3).** For the quaternion algebra over `Q` ramified at `p` and `∞` (the ink
  of 15:40 has "2": his slip for `p`): for `p` invertible in `A′` the pair `(ρ, ρ̄ = p)` maps to the class of `p` in
  `A′*/A′*² = H¹(S′, μ₂)`; over `Z_p` the group is `Z_p*/Z_p*² × Z/2`, the factor generated by `(𝔪, p)`;
  `Γ′ = Γ′₀ × f(±1)` with `f = (p, (0,1), p)` and `Γ = Γ′₀ = H¹(𝔸, μ₂)`.
- **R3 (15:2-14; broad layer `SA05/STUDY.md` §1, SA05-S3-1 to -4).** Granting the Tate and Tate-Honda conjectures as he
  does, the motivic Galois group of `F_p` is the group of multiplicative type dual to the Weil numbers; the gerbe of fibre
  functors extending the canonical one on Artin motives has band `H = Ker(ε | G⁰) = H⁰ × μ₂` (`H⁰` a compact torus); its
  class is trivial at `ℓ ≠ p`, given at `p` by the Frobenius, and its `μ₂`-components at `p` and `∞` are non-zero
  ("l'argument de Serre": `End⁰` of a supersingular elliptic curve, the quaternion algebra ramified at `p` and `∞`, has no
  2-dimensional real representation).
- **R4 (15:16-22; broad layer `SA05/STUDY.md` §2, SA05-S3-5).** Deuring categories (15:16), their classification by
  `Br(K)`, the Brandt group `Brd(O)`, the `G_m`-gerbe of banalizations and `det X` with `det(P ⊗_O X) = det(X)·Nrd(P)`;
  his three conditions for a canonical system of isomorphisms between the `det(X)` (15:22: `Pic(A) = 0`, `Φ ∩ A* = {1}`,
  `ΦA* = K*`, `Φ = Nrd(E*)`) hold for `A = Z` and a definite quaternion algebra (Hasse-Schilling-Maass).
- **R5 (15:96-106, 15:128-133; `STUDY.md` §1, SA06-S3-6 to -8).** `𝕃 = Q′(√−1)` (`Q′` the maximal totally real field) is
  `Q^CM`; for `Q ∈ Q*` and `λ` algebraic: every conjugate has `|λ_α|² = Q` iff `λ ∈ 𝕃` with `λλ̄ = Q`. The Proposition of
  15:96 (a norm-one element with divisor `2h(𝔭 − 𝔭′)`) and its N.B. (if no prime over `p` splits, `λλ̄ = p^i` forces
  `λ = p^{i/2}·(root of unity)`). `G/G⁰` is dual to the roots of unity; `M(p^∞)` is torsion-free. Weight 1 of both of his
  conjectures (15:100, 15:106) is the theorem of Honda and Tate.
- **R6 (15:88-94; reading part 3 §A, P3-01 to -08).** For a group `T` of multiplicative type over `Q` with a Zariski
  generator `f`, a cocharacter `j` and a character `ε` with `εj(λ) = λ^α`: `T⁰/Im j` is compact iff every `m ∈ M = X*(T)`
  (as a subgroup of `Q̄*`) has `|m| = q^{j*(m)/α}` in every embedding, `q = |ε(f)|` (both directions proved); the
  Proposition of 15:94 ((i)-(iv): Weil numbers, `Q′(i)`, compact kernels, algebras with positive involution), with
  `q ≠ 1` needed in (i) ⇒ (iii) and `λ = ±q^{i/2}` in its real margin.
- **R7 (15:110-114; reading part 3 §B, P3-09 to -15, P3-26).** With `M(q)` the Weil `q`-numbers of a Galois CM field `L`
  that are units away from `p`, `P` the primes of `L` over `p`, and the primes of `K` over `p` split in `L`:
  `M₀(q)/torsion` embeds in the minus part `(Z^P)⁻ = {n : n_{τ𝔮} = −n_𝔮}`, the character group of
  `G′ = R_{K₀/Q} R¹_{L₀/K₀} G_m` (`L₀` the decomposition field of `𝔭`, `K₀ = L₀ ∩ K`), and `φ: G′ → G^{0u}` is an isogeny.
  His "`ν` se factorise par `G′`" is false (`2ν = φ∘ν″ + v_𝔭(q) j`); his `f₀ = f j(p^{1/2})` has `ε(f₀) = qp` (the
  weight-zero Frobenius is `f j(q^{−1/2})`); the canonical weight-zero Frobenius lifts to `G′(Q)` iff `φ` is an
  isomorphism; the cokernel of `M₀(q)/torsion → (Z^P)⁻` maps to `Cl(L)` with kernel killed by 2 (the units of `K`
  modulo relative norms), image the subgroup generated by the minus-divisors at `p`.
- **R8 (15:117-125; reading part 3 §C, P3-16 to -25).** For `G` commutative (motives over finite fields): Proposition 1
  (`U = Ker(ε on G⁰)` a torus ⇔ `ε` primitive ⇔ `M_R` has a fibre functor) and Proposition 2 (`U = U⁰ × μ₂` ⇔ `ε` a
  square ⇔ no real fibre functor) hold; they fail for non-commutative `G` (`GL₂` of an elliptic curve without CM). The
  Corollary of 15:119 is right with `ε = pr₂²`, `j = inj₂` (the ink has `ε = pr₂`, `j(λ) = inj₁(λ)²`). Real fibre functors
  form a torsor under `H¹(R, U) = X_*(U)/2 = ₂U(R)` and correspond bijectively to polarizing structures. The slope
  cocharacter `i` of 15:121 (`λ ↦ v_𝔭(λ)/v_𝔭(q)`) satisfies `i + ī = j`, `εi = id`, and is fractional: `i|μ₂` is defined
  iff its values have odd denominators; even denominators occur with only even degrees (`L = Q(i)`, `q = 25`,
  `λ = 5(2 + i)² = 15 + 20i`, `i(λ) = 3/2`); a weight-0 non-integral value: `L = Q(i, √5)`, `p = q = 5`,
  `u = (1 + iφ)/(1 − iφ)`, `φ = (1 + √5)/2`. The canonical involution of 15:123 acts by `−1` on `U`, so `h ↦ −h` on
  `H²(Q, U)`.
- **R9 (14:44-47, the letter to Serre; reading part 1 item 8).** It states, for cycles modulo algebraic equivalence `⊗ Q`:
  A (`ξ^{n−2i}: Cⁱ(X) → C^{n−i}(X)` an isomorphism for `2i ≤ n`), A′ (for `2i ≥ n − 1`, `Cⁱ(Y) → C^{i+1}(X)` onto, `Y` a
  smooth hyperplane section), A″ (`Cⁱ(U) = 0` for `2i > n`, `U = X − Y`), B (`(−1)^m ε(xx′)` positive definite on the
  primitive part of `C^m`, `n = 2m`) and their consequences. As written they are false: on a general quintic threefold
  the difference of two lines is homologically trivial and of infinite order modulo algebraic equivalence (Griffiths,
  Ann. of Math. 90 (1969); the Griffiths group is not finitely generated: Clemens, Publ. Math. IHÉS 58 (1983)), so A fails
  at the case `i = 1, n = 3` the letter names, and A′, A″ and "τ-équivalence = équivalence numérique" with it. The letter
  names the cohomological form as a fallback ("ou se borner à énoncer A pour l'équivalence cohomologique").
- **R10 (14:52-71; reading part 2 item 1).** § 2: for `z` a 1-cycle on `X × Y`, `u_Z: B_X → A_Y` and its ℓ-adic action;
  Prop. 2.4 (an isomorphism in cohomology iff `u_Z` is an isogeny; the inverse is given by a unique class of `Cl(X, Y) ⊗ Q`,
  integral iff `u` is an isomorphism, with exact denominators); Cor. 2.5 (the integral form); Cor. 2.6 (cup product with
  `ζ₁⋯ζ_{n−1}`, `ζ_i` ample, is an isomorphism `H¹(X, Q_ℓ) → H^{2n−1}(X, Q_ℓ)(n−1)` with inverse a unique `Q`-correspondence
  independent of ℓ); Prop. 2.7 (the other direction); Questions 1-2 of 14:71 and his reduction of 2 to abelian varieties.
- **R11 (14:102-117; reading part 2 item 9).** His ③ for `A_a` (cup with `E^{n−2i}` from `A_aⁱ` to `A_a^{n−i}` bijective
  modulo finite groups) fails on the general quintic threefold; ③′ concerns a cone of dimension `n + 1` (both witnesses
  read `2n + 1`), and `A_r²` of the punctured cone over a K3 surface is not finite; "`A_rⁱ(U) = A_rⁱ(X)/Im A_rⁱ(Y)`" needs
  `Im A_r^{i−1}(Y)`; his primitive parts need the exponents `n − 2i + 1` on `A_aⁱ` and `n − 2i + 2` on `Jⁱ`; the `n = 2`,
  `n = 3` rows he marks "OK" hold only under his condition "si équiv. rat. = équiv. d'Albanese".
- **R12 (14:118, 14:126; reading part 2 item 10).** The chain 1°-6° of 14:126 ("rectangle" relations, `A₀(X × Y)^a`,
  `x ↦ (x) − (0)` on an abelian variety, `A₀(X)^a → Alb(X)`): the implications 1° bis ⇒ 2° ⇔ 3°, 3° bis ⇒ 4° ⇔ 4° bis,
  5° ⇒ 4° bis and 5° ⇒ 6° are proved; 4° ⇒ 3° bis and 4° bis ⇒ 5° are not justified on the page; 2) modulo rational
  equivalence fails over `C` already for `E × E` (Mumford 1969; Bloch 1976).
- **R13 (14:2-15; reading part 1 item 1).** Effectivity structures: the full subcategories `P(i)` of 14:5 and their
  closure properties; the twist condition iff `⟨i, ε⟩ > 0`; `I(G) → Eff(G)` is injective modulo `G(C)`-conjugation and
  the Galois action; `Ker ε` compact (14:13, a theorem); for a torus with `M⁺ = P(i₁)`, finitely many effective characters
  of each weight iff the conjugates of `i₁` span `X_*(T) ⊗ Q`.
- **R14 (14:24-39; reading part 1 items 5-6).** Albanese equivalence (Th. 1.4, Th. 1.6: the product of two algebraically
  trivial classes is Albanese-trivial; Th. 2.1 with the existence of the cycle `U` he leaves open, proved; the
  transposition check of 14:37, proved); Th. 3.1 (`u_Z = 0 ⇒ a(ᵗZ) = 0`) proved in characteristic 0.
- **R15 (15:172-179; reading part 3 §F; SA05 reading §1.6, a second, independent reading).** His tables are right: the
  cohomology of `Ẑ` with coefficients `Z_ℓ(n)`, `Q_ℓ(n)`; the "absolute" groups `ℍ⁰(F_q, Z) = ℍ¹(F_q, Z) = Z`,
  `ℍ¹(F_q, Z(n)) = Z/(1 − q^n)` (`n ≠ 0`); `Hⁱ(Spec Z, Q(1)) = 0, 0, 0, Q` (`i = 0..3`); the margin "`n ≠ 0`" of 15:173 must
  be `n ≠ 1`; his "[est-ce nul ??]" has the answer no (`H¹(Spec Z, Q(n)) = Q` for odd `n ≥ 3`, Borel). Prop. 5.4 and
  Cor. 5.5 of the Brauer draft (15:176, 179: `Br(X) → Br(K)` injective when the strict local rings are factorial).
- **R16 (15:191-205; reading part 3 §H).** Over `F_q` there is no `Q`-valued fibre functor; the ℓ-adic points of `T_α`
  over `Z_ℓ` and the crystalline points over `W(k)` (`k` perfect of dimension `≤ 1`) are unique up to isomorphism when
  `G_α` has a smooth connected model (Lang; Steinberg, Publ. Math. IHÉS 25 (1965)); `τ = τ′τ″ = τ″τ′ = F_∞` (15:203, his
  "à vérifier"); the de Rham and ℓ-adic functors differ already on Artin motives; the class attached to a rational
  point lies in `H¹`, not `H²` (15:197). The level formula of 15:205 (the level `≤ ρ` part of the Betti realization is
  `H_Q ∩ F^{(ρ)} ∩ f_∞F^{(ρ)}`) is false: for `E = C/(Z + Zτ)` with `τ` a non-real cubic irrationality and
  `F = h¹(E)^{⊗3}`, that intersection is 5-dimensional, not a Hodge substructure; the refined statement is the
  generalized Hodge conjecture in the form of his note in Topology 8 (1969).

## Leads

Each is an inference of the model named, checked by no one. Each is to be proved or refuted in full, inside the Part it
serves.

- **Lead A1 (A.1; `HUNCHES.md` H1, Claude Opus 5.5 at effort max, agent a28ea31fa17dd65e1).** `ξ_p` is the class of the
  principal polarization on the Dieudonné crystal: an elliptic curve's polarization gives `∧²H¹_cris(E) ≅ Z_p(−1)` (the
  crystalline Weil pairing), compatible with isogenies through their degree, which is the reduced norm (his condition (ii),
  `N_{O/Z}(P) = Z`); 15:52 says "La Norme correspond à la polarisation".
- **Lead A2 (A.7; `HUNCHES.md` H2, the same agent).** The adelic torsor `𝒯` of 15:42-50 refines the `μ₂`-component of the
  motivic gerbe class of 15:7-11 (R3).
- **Lead A3 (A.8; `HUNCHES.md` H3, the same agent).** The margin of 15:70 ("épim ssi la courbe elliptique X d'anneau O se
  descend à F_p, i.e. son j dans F_p") and the descents of 15:56 begin the count of supersingular `j ∈ F_p` by class
  numbers of `Q(√−p)`; his unfinished "Question: O* est-il tjrs égal ..." is probably `O* = {±1}` except for `j = 0, 1728`.
- **Lead A4 (A.6; broad layer `SA05/HUNCHES.md` H3, the same agent).** The canonical determinant of 15:21-22 gives a
  canonical line attached to each supersingular elliptic curve, the norm structure that Deuring's correspondence carries
  implicitly (degrees of isogenies as reduced norms).
- **Lead B1 (B.1; `HUNCHES.md` H4, the same agent).** The weak conjecture of 15:106 holds in every weight: after a power,
  the divisor of a Weil `q`-integer of weight `i` at the primes over `p` splits into `i` divisors of weight-1 Weil integers
  (15:96-98), each realized by Honda-Tate, so `λ^m` is an eigenvalue on `Hⁱ` of a product of abelian varieties.
- **Lead B2 (B.2-B.4; reading, hunch c15-H7, agent add83e0c4fe84ce66).** The obstruction to the strong conjecture without
  powers, and to lifting the weight-zero Frobenius to `G′`, is class-group theoretic: the subgroup of `Cl(L)` generated by
  the minus-divisors at `p`.
- **Lead C1 (C.4; reading, hunches c14b-H1 to -H3, sub-reader a18fb27f7c0e6640f).** 14:52-71 is a complete ℓ-adic proof of
  the Lefschetz standard conjecture in degree 1; his Question 2 for abelian varieties is the integral algebraicity of the
  minimal class `θ^{g−1}/(g−1)!` of a principal polarization; Question 1 asks whether the tautological point of `A_X` over
  `K = k(A_X)` is the Albanese image of a degree-0 0-cycle on `X_K`.
- **Lead D1 (D.1; reading, hunch c15-H1, agent add83e0c4fe84ce66).** The privileged polarizations of 15:121-123 and the
  real points of 15:183 need the slope cocharacter on a cover (the protorus with character group `Q` of
  Langlands-Rapoport); the parity of the slope denominators decides whether a privileged real point exists.
- **Lead E1 (E.2; reading, hunch c14a-H4, sub-reader a0012f1ff34e51fa6).** An effectivity structure determines the Galois
  orbit of the conjugacy class of `μ`, an invariant of the type of a reflex field.
- **Lead E2 (E.4; reading, hunch c15-H4, agent add83e0c4fe84ce66).** His "cohomologie absolue des motifs de Tate" is the
  integral Weil-étale cohomology (Lichtenbaum): `F_q` behaves as a circle, `Spec Z` as a closed 3-manifold.
- **Lead E3 (E.5; reading, hunch c15-H5, the same agent).** "La partie continue du H¹" of 15:193 is the moduli of
  F-crystals with `G`-structure, against the discrete classification of isocrystals (Dieudonné-Manin, Kottwitz's `B(G)`).
- **Lead E4 (E.3; reading, hunch c14a-H5, sub-reader a0012f1ff34e51fa6).** The converse of Th. 3.1 (14:38) over `C` is
  equivalent to: Albanese and Abel-Jacobi equivalence agree on algebraically trivial cycles that come from abelian
  families.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (the field, curve, abelian variety, variety, quaternion order, motive or group given
completely, with the verification of every hypothesis and of the failure; checked by a program when finite or
computable) and the strongest true statement proved in its place. Nothing else finishes an item. Partly settled is not
an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest undecided
instance are the state of an item you are still working on: record them as you go, then attack the obstruction,
starting from that instance. "Known" counts only with the derivation of the statement used here from the cited theorem,
after opening the source. An item that begins with "Determine" is done when the object asked for is given explicitly,
with a proof that it is the whole answer.

For Part A in particular.
- Every construction is given with its data (the base ring, the topology, the band of every gerbe, the group of every
  torsor and the side it acts on), and every "canonical" is proved: independence of the choices, and compatibility with
  the isomorphisms between the choices, up to unique isomorphism or up to the sign you determine.
- The element `ξ_p` is determined when you give, for every rank-2 F-crystal of slope 1/2 over `F̄_p` with an action of a
  maximal order `O` of the quaternion algebra ramified at `p` and `∞`, the class `u(M, O)` explicitly, with a proof of his
  conditions (i) and (ii) of 15:54 and a proof that it is the element Deuring's theory singles out (15:50 a)).
- Every computation (quaternion orders, class numbers, Brandt matrices, isogeny graphs, Dieudonné modules) is given with
  its program, inputs and output, and with a proof that it shows what it is used for.

For Parts B and C. A Frobenius eigenvalue is given with the variety, the field, the cohomology group and the degree it
occurs in; a refutation of a realization statement gives the Weil number and a proof that it occurs in no variety of the
kind in question. A cycle statement names the equivalence relation (rational, algebraic, Albanese, τ, homological,
numerical) and the coefficients (`Z`, `Q`, `Z_ℓ`) at each step.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; proving R1-R16 again in place of the
items, except where a Part asks for it; a result of the readings used without the check above; a statement for all `p`
(all weights, all `X`, all `q`) proved for some, without saying so; a step that replaces a claim by a convenient special
case without naming it; a reading of his pages changed to fit the mathematics without saying what the transcription
reads and why you read it otherwise.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA06_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The Deuring element, the adelic `μ₂`-torsor and the Brandt Picard category (cote 15, 15:16-78; RP-SA06-1 with
RP-SA05-2). The main question is A.1.**

Setting (15:34-56; `STUDY.md` §3; R1-R4): `B_p` the quaternion algebra over `Q` ramified exactly at `p` and `∞`; `𝒪` the
set of its maximal orders; `C` a Deuring category of type `B_p` over `Z` (15:16), realized by the supersingular elliptic
curves over `F̄_p` with their homomorphism groups; `V_A(C)` and the rigidified pairs `(C, T)` (15:34); `Eq(C, T)`,
`Brd(C, T)` and `Ram(C/A)` (15:34-36); the local categories `C(A′)` on `A′ = ∏_{ℓ≠p} Z_ℓ` (the gerbe of square roots of
`A′(1)`), `C(Z_p)` (F-crystals of rank 2 and slope 1/2 over `F̄_p` with the Tate functor) and `C(R)` (the standard
`μ₂`-gerbe over `R`) (15:42); `𝒯′(C)` under `Γ′`, `𝒯 = 𝒯(F̄_p)` under `H¹(𝔸, μ₂) = ∏_ℓ Z_ℓ*/Z_ℓ*²` (`p` and `∞`
included) (15:42-44); `𝒯_p` the canonical torsor under `Z_p*/Z_p*²` of 15:48; the gerbe `𝔊(ξ_p)` on the adèles and its
section `ξ` (15:50).

1. (The main question: 15:50-56.) Determine the Deuring element `ξ_p ∈ 𝒯_p`. Give the rule `(M, O) ↦ u(M, O)` in
   `Isom_{crist.-Tate}(∧²M, T_p)/Z_p*²` of 15:54 explicitly for every pair (an F-crystal `M` of rank 2 and slope 1/2 over
   `F_{p²}` or `F̄_p` with an action of `O ∈ 𝒪`), prove his conditions (i) (stability under isomorphisms, equivalently
   under automorphisms of `F̄_p`, Frobenius included) and (ii) (compatibility with `M ↦ P ⊗_O M` through
   `det(P ⊗_O M) = N_{O/Z}(P) ⊗ det M` and `N_{O/Z}(P) ≅ Z`), prove that it is the element of 15:50 a), and determine the
   set of all rules satisfying (i) and (ii) (a torsor under which group). Decide Lead A1. Do the same in the equivalent
   form of 15:56: triples `(M₀, O, i)`, `i: R → O`, `R` the integers of `Q(√−p)`, equivalently descents of `M` to `F_p`
   with `F² + p = 0`; prove the equivalence he states, for every `p`, `p = 2` and `p = 3` included.
2. (15:42-50.) Prove the construction: `𝒯′(C)` is a torsor under `Γ′ = A′*/A′*² × (Z_p*/Z_p*² × Z/2) × R*/R*²`, the
   generator of the autoequivalences acts by `f = (p, (0, 1), p)`, `Γ′ = Γ′₀ × f(±1)`, and `𝒯 = 𝒯′(C)/±1` is a torsor
   under `H¹(𝔸, μ₂)` independent of `C` up to unique isomorphism, on which `Ẑ` acts trivially (15:44). Prove that the gerbe
   `𝔊(ξ_p)` of 15:50 is trivial and that its sections up to isomorphism form `𝒯`; construct the section `ξ` of 15:50 b)
   and the element `|ξ| ∈ 𝒯`, and determine its component at every place, `p` and `∞` included.
3. (The sign at infinity: 15:48, "attention: réalité, s'il n'y a pas un dernier signe!"; 15:50, "unique au signe près à
   l'infini"; 15:52.) Decide whether the component of `ξ` at `∞` is defined without a sign. If a sign remains, determine
   the group it lives in and decide whether the positivity of the reduced norm (the polarization) fixes it.
4. (15:52, the quaternionic realization.) Construct the functor "essentiellement canonique" from supersingular elliptic
   curves over `F̄_p` to right `H`-lines of dimension 1 that are unitary (`H` the real quaternions), with the reduced norm
   corresponding to the polarization and the transposition to the transposition, prove its uniqueness up to unique
   isomorphism (or up to the sign of A.3), and prove its relation to Serre's argument of 15:11 (R3).
5. (15:36, "À vérifier!!".) For `A → A′` and `(C_{A′}, T_{A′}) ≃ (C′, T′)`, prove or refute that there is a canonical
   equivalence of Picard categories `Eq(C_{A′}, T_{A′}) ≃ Eq(C′, T′)` under which the two torsor-category structures on the
   category of equivalences `(C_{A′}, T_{A′}) → (C′, T′)` coincide. R1 is the unrigidified case under (C); this item is the
   rigidified one, for every `A′`, `Pic(A′) ≠ 0` included.
6. (15:21-22, the canonical determinant; Lead A4.) Construct the canonical system of isomorphisms between the `det(X)`
   under his three conditions, prove that it exists and is unique for `A = Z` and `B_p`, and determine its relation to
   `ξ_p` and to the polarizations. Decide Lead A4.
7. (Lead A2: 15:7-11 against 15:42-50.) Prove the exact relation between `𝒯` with `|ξ|` and the class of the motivic
   gerbe of `F_p` (R3): decide whether the supersingular part determines the `μ₂`-component of that class at every place.
8. (15:56, 15:70; Lead A3.) Determine the number of triples `(M₀, O, i)` up to isomorphism, that is of supersingular
   elliptic curves over `F_p` with their `F_p`-structure, in terms of class numbers of `Q(√−p)` (with the cases
   `p ≡ 1, 3, 7 mod 8` and `p = 2, 3`), and decide what his "Question: O* est-il tjrs égal ..." of 15:70 asks (from the
   transcription and its context) and answer it.

**B. Frobenius eigenvalues in every weight: his strong and weak conjectures (15:94-106, 15:110-114, 15:128-133;
RP-SA06-2).** This Part comes after Part A and is governed by the same rules, the push rule and the three-hour check.

Setting (R5-R7): `q = p^n`; a Weil `q`-integer of weight `i ≥ 0` is an algebraic integer `λ` all of whose conjugates have
absolute value `q^{i/2}`; such `λ` lie in `𝕃 = Q^CM` (R5). His strong conjecture (15:100): every Weil `q`-integer of weight
`i` is an eigenvalue of the Frobenius of `F_q` on `Hⁱ(X_{F̄_q}, Q_ℓ)` for some smooth projective `X` over `F_q`. His weak
conjecture (15:106): for every such `λ` there is `m > 0` with `λ^m` an eigenvalue of the Frobenius of `F_{q^m}` on a
semisimple motive of weight `i` over `F_{q^m}`.

1. (Lead B1.) Prove the weak conjecture in every weight `i ≥ 0`, with an explicit variety (products of abelian varieties,
   projective spaces and finite étale schemes, or others you construct), an explicit `m` in terms of `λ` (class numbers,
   unit indices), and the cohomology group in which `λ^m` occurs.
2. (The strong conjecture.) Decide it in weight 2, then in weight 3, then in every weight: for every `q` and every Weil
   `q`-integer `λ` of weight `i`, construct a smooth projective `X` over `F_q` with `λ` an eigenvalue on `Hⁱ`, or give a
   `λ` with a proof that it occurs on no `Hⁱ` of any smooth projective variety over `F_q`, and determine the exact set of
   Weil `q`-integers of weight `i` that occur. Test cases: `L = Q(√−23)`, `p = q = 2`, `λ` the generator of the cube of a
   prime over 2 (weight 3); `λ = ±q^{i/2}`; `λ` in the supersingular case (one prime over `p`); Jacobi sums of Fermat
   varieties.
3. Decide whether every Weil `q`-integer of weight `i` occurs in the category generated by abelian varieties, Tate twists
   and Artin motives over `F_q` without passing to a power, i.e. whether it is a product of `i` Weil `q`-integers of weight 1
   times a root of unity of the right kind; determine the obstruction exactly (Lead B2).
4. (15:110-114; R7.) Determine the cokernel of `M₀(q)/torsion → (Z^P)⁻` exactly, its 2-part included, for every Galois CM
   field `L` and every `q`; decide for which `q` the canonical weight-zero Frobenius lifts to `G′(Q)`, and prove that it
   lifts after replacing `q` by `q^h` for an explicit `h`. Decide Lead B2.

**C. The conjectures of the letter to Serre after Griffiths' quintic, and the Lefschetz programme for cycles (cote 14,
14:44-71, 14:102-131).** This Part comes after Part A and is governed by the same rules, the push rule and the three-hour
check.

1. (R9.) Prove in full that A, A′, A″ and "τ-équivalence = équivalence numérique" fail modulo algebraic equivalence on a
   general quintic threefold: a complete proof that the difference of two lines is homologically trivial and of
   infinite order modulo algebraic equivalence (Griffiths' argument through the Abel-Jacobi map, every step checked), or
   another complete counterexample. Then determine, for each of A, A′, A″, B and each of the consequences the letter
   draws, exactly the `(n, i)` for which it holds modulo algebraic equivalence and those for which it fails, with proofs
   (`n ≤ 2`; `i = 0`; divisors; varieties whose Griffiths groups vanish).
2. (The homological form.) State `A_hom`, `A′_hom`, `A″_hom`, `B_hom` (his statements with homological equivalence) and
   prove or refute each implication the letter claims among them: `A′ ⇒ A` (with his reduction to `n = 2i + 1` and the base
   field he says it needs), `A′ ⇔ A″`, "A et B impliquent" (the archive) against "B implique" (print) the semisimplicity of
   motives, `B ⇒` homological = numerical equivalence, and the consequences for Weil's conjectures. Prove `A″_hom`
   (vanishing of the cohomology of the affine `U` above degree `n`) and decide whether `A′_hom` follows from it. Compare
   with Grothendieck, "Standard conjectures on algebraic cycles" (Bombay 1968), and Kleiman's equivalences, after opening
   them.
3. (14:112, ③; R11.) Determine exactly which statements of ③, ③′ and ② hold: is `E^{n−2i}: A_aⁱ ⊗ Q → A_a^{n−i} ⊗ Q`
   injective for every `i ≤ n/2`? surjective for which `(n, i)`? Determine the cokernel for the general quintic threefold
   (`i = 1`). The same for the `Jⁱ`-part (`E^{n−2i+1}`) and for the local statements of 14:106-109, with the corrections of
   R11. Give the strongest true statement in each case.
4. (14:52-71, 14:51; R10; Lead C1.) Prove that 2.1-2.7 give the degree-1 Lefschetz standard conjecture ℓ-adically over
   every algebraically closed field, with inverses given by `Q`-correspondences independent of ℓ, and the integral form
   of 2.4-2.5. Prove his reduction of Question 2 to abelian varieties; settle Questions 1 and 2 for curves, Jacobians,
   products of elliptic curves and abelian varieties of dimension `≤ 3`; and prove or refute the equivalence of Question 2
   for a principally polarized abelian variety with the algebraicity of the integral class `θ^{g−1}/(g−1)!`, and that of
   Question 1 with the 0-cycle statement of Lead C1.
5. (14:126; R12.) Decide the implications 4° ⇒ 3° bis and 4° bis ⇒ 5° of 14:126, and the whole chain 1°-6°, over `F̄_p`
   and over `C`, with complete proofs (over `F̄_p`: the Albanese kernel of 0-cycles; over `C`: Mumford's theorem).

**D. Real fibre functors, polarizations and the canonical involution of motives over finite fields (15:117-125,
15:183-187; R8).** This Part comes after Part A and is governed by the same rules, the push rule and the three-hour
check.

1. (15:121-123; Lead D1.) For the commutative motivic group of `F_q` (the dual of `M(q)`) with `ε`, `j` and the Galois
   orbit of the slope cocharacter `i`: determine for which subgroups of `M(q)` (equivalently which subcategories of
   motives) `i|μ₂` is defined; when it is not, decide whether a privileged packet of real fibre functors in the sense of
   15:123 exists in any Galois-equivariant sense, and give a definition that works for every `q`, with its proof (for
   instance through the protorus with character group `Q`); compute everything in the example `q = 25`,
   `λ = 15 + 20i`.
2. (15:121, "À voir".) For `G` commutative, decide whether `Aut(G⁰_R, ε_R, j_R)`, `Aut(G⁰, ε, j)` and `Aut(G, ε, j)` act
   transitively on the set of polarizations, and determine the orbits.
3. (15:125.) Decide whether the canonical involution of `G` (complex conjugation on `M(q)`, R8) lifts to an involution of
   the motivic gerbe of `F_q` (R3): determine the order of the class `h ∈ H²(Q, U)` and the obstruction to a lift of
   order 2, and settle his "Il ne semble pas que cette involution corresponde à une involution dans la gerbe".
4. (15:183-187.) State precisely and prove or refute his "condition non tautologique sur la distribution des `u(s′)`"
   (15:185) for motives of even degrees over a scheme of finite type over `Z`: the polarizations of `G_R^{ξ(s′)}` defined
   by the `v(s′)` coincide when `ξ(s′)` is constant. Prove that his recovery of the effectivity cone from the `u(s′)`
   (15:185-187) is equivalent to the statement that a motive whose Frobenius eigenvalues at all closed points are
   algebraic integers is effective, and decide that statement for motives over `F_q` (compare B.2).

**E. The other open steps and the sharpest hunches of cotes 14 and 15.** This Part comes after Part A and is governed by
the same rules, the push rule and the three-hour check.

1. (14:9.) Give the saturation condition he leaves unspecified ("que nous ne précisons pas ici (est-elle automatiquement
   satisfaite ?)") as the condition that makes the cones of 14:9 exactly the effectivity structures that are
   intersections of `P(i)`, and decide whether it is automatic.
2. (14:11 and 15:121; R13; Lead E1.) For motives over `F_q`, prove that the effectivity structure (integral Frobenius
   eigenvalues) is the intersection of the `P(σi)` over the Galois conjugates of the slope cocharacter, and decide his
   question of 14:11 there: is it `P(i₁)` for a single class `i₁ ∈ I(G)` (`i₁ ī₁ = j`, `εi₁ = id`), integrality included?
   Decide his axiom of 14:3 (finitely many types of effective motives of each weight) for motives over `F_q`, and decide
   Lead E1.
3. (14:38-39; R14; Lead E4.) Decide the converse of Th. 3.1 over `C`, and Th. 3.1 itself in characteristic `p`
   (through an ℓ-adic Abel-Jacobi map); decide Lead E4.
4. (15:172-178; R15; Lead E2.) Prove that a cohomology theory with exactly his values exists for `F_q` and for `Spec Z`
   (and its open subsets), identify it with Lichtenbaum's Weil-étale cohomology (with the conventions: compactified or not,
   the real place, his "petite modification ℓ = 2"), determine `ℍⁱ(F_q, Z(n))` for every `i` and every `n ∈ Z` with the
   `p`-part ("mod p-primary ?"), and determine for which theory `H³(Spec Z, Z(1)) = Z`.
5. (15:191-193; Lead E3.) Decide his expectation that `T_∞(k) = lim T_α(k)` has a single isomorphism class, given by de
   Rham-Hodge theory, for `k` algebraically closed and for `k` perfect; and decide his statement that crystalline points at
   different `k`-points are in general not isomorphic ("la partie continue du H¹"); decide Lead E3.
6. (15:197-199; R16.) Determine the class in `H¹(Q_ℓ, G_ℓ)` attached to a rational point on the category generated by
   Artin motives and `Q(1)`, and decide whether it can be non-zero outside the Artin part; for a number field `k` (his
   "particulièrement intéressant"), determine the classes in `H¹(Q_ℓ ⊗ k, G_ℓ)`.

**F. Statement of results.**

1. For the companion to cotes 14 and 15: every statement of Parts A-E with what this run and R1-R16 prove, in his notation,
   with the pages it settles.
2. The literature record: for every source named in this prompt and every source you use, one line: opened, with the
   numbers of the theorems that contain or come closest to each statement you prove; or not obtained, with what you
   tried. Say what you searched for A.1-A.8, B.2-B.4, C.3-C.4, D.1 and E.4 in particular: the Deuring correspondence in
   categorical and crystalline form (Deuring 1941; Voight, Quaternion Algebras, 2021); Dieudonné modules of supersingular
   elliptic curves and their polarizations; Weil numbers occurring on `Hⁱ` (Honda-Tate; Milne, "Motives over finite
   fields", 1994; Langlands-Rapoport, 1987; Kisin on mod `p` points of Shimura varieties); the standard conjectures and
   their failure modulo algebraic equivalence (Griffiths 1969; Clemens 1983; Kleiman 1968 and 1994); integral Hodge
   classes on abelian varieties; Weil-étale cohomology (Lichtenbaum, 2005 and 2009).

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data: the field (finite or not, perfect or not, algebraically closed or not), the
   characteristic and `p`, the weight, the dimension, the base ring, the equivalence relation on cycles, the coefficients
   (`Z`, `Q`, `Z_ℓ`, `Q_ℓ`, `W`), whether up to isomorphism, up to isogeny or up to a sign. Do not replace it by a convenient
   special case. If you prove a special case, name it as one and keep the general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property you use
   (semilinear for which Frobenius; a morphism of crystals, of F-crystals, of gerbes, of Picard categories, of torsors;
   over which base). Compositions must type-check.
3. Every reduction ("we may assume", "after a finite extension", "replace `q` by a power", "pass to `F̄_p`") comes with a
   proof that the property needed transfers in the direction needed.
4. Conventions are named and kept: covariant or contravariant Dieudonné theory; `σ` or `σ⁻¹`; geometric or arithmetic
   Frobenius; the sign of `A ≅ A**`; `ε j(λ) = λ²` and the weight; his indexing of `Z/2` and `μ₂`; left and right modules
   over `O`.
5. Check the edge cases in scope: `p = 2` and `p = 3`; `j = 0` and `j = 1728`; weights 0, 1, 2 and 3; `q` a square and not a
   square; the supersingular case (one prime over `p`); `n ≤ 3` for the cycle statements.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you
   attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart.
7. No authority. The transcriptions, the Pro notes, the Codex web notes, the readings, R1-R16 and the Leads (inferences by
   Claude, Anthropic) are all to be checked where used; the Leads in full. If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and you
   go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to deliver

One ZIP containing:
- `RESEARCH_SA06_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement is
  used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), with complete proofs;
  English, first person plural; his statements quoted in French with the page.
- `RESEARCH_SA06_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `RESEARCH_SA06_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA06_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with
  the statement number); then what you read, what you computed (every computation with its scope, inputs, run time and
  output files), and every correction to R1-R16, to the Leads, to the readings and to the transcriptions, with the page.
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

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `RESEARCH_SA06_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `RESEARCH_SA06_checkpoint_<NN>_part<k>.zip`, the file list in the first part.

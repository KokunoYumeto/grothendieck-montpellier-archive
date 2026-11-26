# Independent check of D1, "Exact, total and filtered small categories"

Checker: abe075dcdd909eea0 (Claude Opus 5.5 at effort max), 25 Nov 2026, for the main session 329fb1e6 (Claude Opus
5.5 at effort max). Paper written 25 Nov 2026 by afbbdefd94c5db150 (Claude Fable 5.2 at effort max) from runs of
GPT-6 Astra (ChatGPT Pro mode). I did not write the paper and I did not edit it. Brief:
`agent_notes/abe075dc_D1_CHECK_BRIEF_20261125.md`. Running notes: `agent_notes/abe075dcdd909eea0_NOTES.md`.

## Verdict

| Statement | Verdict |
|---|---|
| Theorem A (C_δ total; colimits exact over no non-zero ring) | **holds** as written. Every step checked; the writer's own Lemma 4.7 and the setting (K1)–(K4) with Lemma 3.3 and Proposition 3.2 are correct. One cosmetic repair in the introduction (non-empty hypergraphs). |
| Theorem B (two-graphs: quasi-filtered, not total) | **holds** as written. The writer's own Lemmas 5.5, 5.6, 5.8, 5.9 and the reduction in Proposition 5.7 are correct. I re-proved "not total" independently by another route (below), with the same conclusion. |
| Theorem C (the chain, its strictness, filtered ⟺ total and sifted) | **holds** as written (Propositions 2.3, 2.5, 2.7, 2.8 checked in the form given; the sifted proof is complete). The strictness of the first inclusion rests on Isbell–Mitchell 1973 (item 2). |
| Section 6 | **holds with repairs**: see items 2 and 4 (citation of Isbell–Mitchell 1976, Corollary 4.4, and the quotations). |

No statement is wrong and no proof has a gap. The repairs are of wording and citation.

## 1. The mathematics

### 1.1 My own proofs before reading the paper's

*Theorem B, "not total".* Before reading Section 5, I proved that `BT` is not contractible by a different route.
Every object of `T` is non-empty and rigid (ordered), and the class is closed under induced substructures, with all
embeddings as arrows. Let `Pt` be the points functor. Then `Pt^{n+1}` is the coproduct, over the isomorphism
classes of pairs `(D, ψ)` with `D` an ordered two-graph and `ψ: {0,…,n} → |D|` a surjection, of the representables
`T(D, −)` (send a tuple to the induced substructure on its entries, with its unique isomorphism to a standard
object). Each `El(T(D, −)) = D\T` has an initial object, and `Pt^{•+1} → 1` is objectwise a weak equivalence because
every object is non-empty. Hence `BT ≃ |Q|`, where `Q_n` is the set of isomorphism classes of such pairs `(D, ψ)`
(equivalently, of `Aut`-orbits of `(n+1)`-tuples of points of the generic two-graph). In `Q` there is one vertex and
two non-degenerate edges `<`, `>`; the triangles `(x, y, x)` and `x < y < z` give `<·> = 1` and `<·< = <`, so
`π₁|Q| = 1`. The function "the three distinct entries form a triple" is a normalized mod-2 2-cocycle (the parity
condition on 4-sets) and is not a coboundary (on increasing triples a coboundary takes the same value on the triple
and the non-triple types). So `H²(BT; F₂) ≠ 0`, hence `H₂(BT; ℤ) ≠ 0` and `T` is not total. This agrees with
Lemmas 5.8 and 5.9 of the paper.

*Theorem A.* I could not finish an independent proof of the reduction (every action component contractible or
equivalent to the category). My attempt (components of `El(L)` correspond to orbits of the `Aut(M)`-set
`colim L`, with a canonical support) stalled because the comma categories of the support functor are discrete but
need not be points. The paper's Proposition 3.2 removes exactly this obstacle (Step 1: injective transition maps;
Step 2: saturation `L → T_S`), using (SC). I then checked its proof step by step (1.2).

*(QF2).* For parallel `f, g: A → B`, three arrows `h₁, h₂, h₃: B → C` with `h₁f = h₂g`, `h₃f = h₂f`, `h₃g = h₁g` give
the affine equalizer `h₁ + h₂ − h₃`. The paper does not need this (it derives (QF2) from simple connectivity).

### 1.2 Section 3 (the setting and the reduction)

- (K1)–(K4) and the category `𝒜(M, G, 𝒦)`, whose objects are the non-empty members of `𝒦`: consistent with
  Definitions 4.1 and 5.1 (both require `n ≥ 1`).
- Lemma 3.1 (squares from (SC)): correct. A path in the union of the two cosieves contains an arrow between them,
  and its target lies in both.
- Proposition 3.2: correct, every step. Step 1: `∼` is an equivalence relation (via 3.1) preserved by the transition
  maps; for `q: El(L) → El(L^inj)`, the category `d\J` is the cosieve of `x\𝒜` on the arrows `g` with
  `L(g)k = L(gf)l`, non-empty because `k ∼ L(f)l`; Theorem A twice. Step 2: the colimit over the directed set of
  non-empty members, the action, `T_S(B) = S^{G_B}` independent of the representative, and the comma category of
  `El(i)` is a cosieve of `a\𝒜`, non-empty by (K1). Step 3: `(G/G_F)^{G_B} ≅ 𝒜(F, B)` by (K2); `F = ∅` gives the
  point.
- Lemma 3.3 (bridge set): correct. Classes of links: the `F`-cycles; pairs `{x_i, x_{i+1}}`; triples
  `{y_{s−1}, d, x_1}` (distinct pieces because `s ≥ 4`); (iii) checked at `i = 0, s−2, s−1`; (iv) by cutting the
  links between `r−1` and `r`. The order: `p_t` is strictly increasing and constant on `F`, `Δ > 0` by
  compactness, `b_{2j+1}` lies within `M₀/N` of `p_{(j+1)/N}`, all `b_i` strictly increasing when `2M₀ < NΔ`; ties of
  `β` between pieces may be broken arbitrarily.

### 1.3 Section 4 (Theorem A)

- Lemma 4.2 (a)–(d), Proposition 4.3 (M1)–(M3), Lemma 4.4 (arrows of `𝒜` = closed embeddings; `𝒜 ≃ C_δ`), Lemma 4.5
  (K2): correct.
- Lemma 4.6: correct. `T(f)` is increasing (it preserves the gap of `P` in which a vertex lies), an embedding (each
  hyperedge lies in one copy, and both directions were checked), with closed image (`T(X')` is the free amalgam of
  `λ(X')` and the image over `λ f(X)`); `η` and `γ` are natural; `P = ∅` gives `BC ≃ *`.
- Lemma 4.7 (the writer's "pieces are induced"): correct, including the case `{i, j} = {1, s−1}` through `Z₀`. The
  cut, the free amalgams `L_k`, the estimate `δ_Z(U) ≥ δ_L(Ũ) − 2m`, Case 1 (bijectivity of `q` over `U`) and Case 2
  (`3|J| ≥ s`) are right.
- Proposition 4.8, Corollary 4.9 (K3), Theorem 4.10: correct.
- Theorem 4.11: correct for every non-zero ring (left modules): an arrow `W → X` is determined by its image; the
  incidence count `3r < 2v` gives a vertex on exactly one hyperedge; `g_k v_i` occurs once; `colim Θ = 0` by
  augmentation. The exactness criterion of Isbell–Mitchell is not needed.

### 1.4 Section 5 (Theorem B)

- (5.1) `∂(c_p) = c`; Lemma 5.2 (anchored amalgams); Proposition 5.3; Lemma 5.4: (K2) including `B = ∅`, and (K4):
  `T(f)` preserves the graph `b` on the pairs inside either copy and on the remaining pairs (where `b = 0`), hence
  preserves `∂b`. Correct.
- Lemma 5.5 (the writer's bridge with an anchor): `b` is well defined in the three cases (consecutive pieces;
  `F`-points; `{1, s−1}` through `Z₀`), and `∂b` restricts to the two-graph of every piece. Correct.
- Lemma 5.6 (the writer's): `G` transitive; `G_{w}` transitive below and above `w`; with `w > u, y`, `G_{w} ≤ H`
  and `u ∈ G_{w}x`. Correct.
- Proposition 5.7 (the writer's reduction): for `B ∩ C = ∅`, through `G_{x} = ⟨G_{B∪{x}}, G_{C∪{x}}⟩` and
  Lemma 5.6. Correct; (K3) as in Corollary 4.9 (also for `B = ∅`).
- Lemma 5.8 (the writer's): the three relations give `Ψ(d⁰) = Ψ(d¹)`, so `θ_Y = Ψ(i_u)` does not depend on `u` and
  is a natural isomorphism from a constant functor. Correct; Quillen's Proposition 1 then gives `π₁ = 1`.
- Lemma 5.9 (the writer's): `Φ` vanishes on degenerate simplices; on a 3-simplex its four face values are the values
  of `c_{X₃}` on the triples omitting one `n_k` (distinct: the two-graph condition; a repetition: two equal values
  cancel and the other two vanish). The chain `ξ` of twelve simplices is a mod-2 cycle (the faces `P → Q` cancel
  between `X` and `X'`, the faces `Q → X` and `P → X` occur twice), and `Φ(ξ) = 1`. Correct.
- Theorem 5.10 and Remark 5.11: correct; the claim of the run that `BT ≃ K(F₂, 2)` is rightly not used.

### 1.5 Section 2 (Theorem C)

- Lemma 2.2, Proposition 2.3 (both directions; `BA_D` is the mapping cone of `BD → BA`), Remark 2.4, Proposition 2.5
  (exact ⇒ total through `Σ` and the resolution `R•`), Lemma 2.6, Proposition 2.7 (QF1 from common successors in
  `p\A`; QF2 from `H₁(El(H)) ≅ ℤ/I`), Proposition 2.8: correct as written.
- The sifted statement: the writer's proof uses the objects `(q, f, g)` and `(q, f, f)` of `(p,p)\Δ`; a common
  successor `(r, w, w')` forces `hf = w = h'f` and `hg = w' = h'f`, so `hf = hg`. It is complete (it is a variant of
  PRETOT F.3, which used `(q; u, 1_q)` and `(q; v, 1_q)` in `El(A(p,−) × A(q,−))`). The converse is right.

### 1.6 Wording repairs (mathematics)

1. `sec1_intro.tex`, Theorem A: "Let $\Cd$ be the category of finite linearly ordered $3$-uniform hypergraphs" →
   "Let $\Cd$ be the category of non-empty finite linearly ordered $3$-uniform hypergraphs". (Definition 4.1 has
   `n ≥ 1`; with the empty hypergraph the category would have an initial object and Section 3 would not apply as
   stated.)
2. `sec5_twographs.tex`, Theorem 5.10, "By Lemma~\ref{lem:pi1} all action components of $\mathcal T$ are simply
   connected": add "(each is weakly contractible or weakly equivalent to $\mathcal T$)" after "simply connected",
   so that the use of the first assertion is explicit.

## 2. Citations made from memory (PROVENANCE.md, "To confirm", item 1)

Opened in this check (free copies):

| Citation | Opened | Locator and use |
|---|---|---|
| [AKR] | scan `DERIVATEURS_EXPERT/work/lit/AKR1981.pdf`, pp. 368–369 (text layer only on the cover; pages read as images) | Title: **Embeddings into categories with fixed points in representations**, Czechoslovak Math. J. 31 (106) (1981), no. 3, 368–389. Their Definition [1] (p. 369, attributed to Adámek and Reiterman): *quasi-filtered* = every parallel pair has a quasi-filter (A,2: a cyclic system of equations with Σ(i_t − j_t) = ±1) and any two objects have a common successor. Their Theorem [1]: a category has quasi-filtered components iff it has span completion and quasi-filters. For a connected category their notion is therefore (QF1) with quasi-filters, which is (QF1)+(QF2) by [IM76, Lemma 2.1]. The paper's sentence is right in substance; R4 makes it exact. |
| [IM73] | `DERIVATEURS_EXPERT/work/lit/IsbellMitchell1973_bull.pdf` | Theorem 1: "Colim_C is exact if and only if the components of aff C are filtered." Theorem 3: "aff Δ is filtered", Δ being "the category Δ_face … of order preserving injections of finite totally ordered sets". Used rightly for Δ_inj (R7 makes the passage to non-empty ordinals explicit). Its Corollary 1: exact, with weak terminal objects in all components ⇒ components filtered. |
| [IM76] | AMS copy, Trans. AMS 220 (1976), 289–298, DOI 10.1090/S0002-9947-1976-0404377-3 | §2 defines conditions I–V on a C-set; for representables, I is span completion = (QF1) and IV ("every pair … is filtered in aff C") = (QF2). Corollary 4.4: "If C satisfies I and IV and is connected with a weak terminal object, then C is filtered." Section 6, item 3 uses exactly this: correct. Lemma 2.1: under I, IV ⟺ V. |
| [Rosicky] | arXiv:math/0509655v2 | Remark 4.5(1): D is homotopy sifted iff all comma categories (d₁,d₂) ↓ Δ are aspherical, "hence … iff D^op is totally aspherical in the sense of [34], 1.6.3". The paper's distinction in §2.2 is right; R8 adds the locator. |
| [Der] Ch. II | Maltsiniotis's PDF `Der-ChII-234.pdf` (65 pp.) | item 4. |

Not opened in this check (not freely available, or the file did not load): Quillen 1973 (Springer LNM 341); Mac Lane,
CWM IX.3; Weibel, Theorem 2.6.15; Bousfield–Kan XII.5.2; Goerss–Jardine IV, Proposition 1.7; Seidel 1976;
Adámek–Rosický 2001 (the two TAC URLs tried returned 404). The paper uses each for a standard statement (Quillen §1:
coverings ↔ morphism-inverting functors, natural transformations give homotopies, an initial object gives
contractibility, Theorem A; CWM: final functors; Weibel: filtered colimits of modules are exact; BK: the homotopy colimit
as the diagonal of the simplicial replacement; GJ: a levelwise weak equivalence of bisimplicial sets gives a weak
equivalence of diagonals; AR: sifted ⟺ non-empty with final diagonal; Seidel: the term two-graph), and no proof needs
more than these statements. The exact numbers were **not** confirmed here and must be confirmed before posting.
Evans–Hubička–Nešetřil, Theorem 2.6 was opened by the writer on 13 Nov; I did not reopen it (Proposition 4.3 is proved
in full in the paper, so the citation is context only).

## 3. Literature gate (Proposition 2.3, Remark 2.4; novelty of Theorems A and B)

Searched 25 Nov 2026. Hexagon catalogue (`/api/v1/works`, all 16 pages, 1,544 works; regex over title, abstract and
tags for totally aspherical, aspheric, exact colimit, quasi-filter, Isbell, filtered categor, homotopy colimit, sifted,
categories of elements, Grothendieck construction, dérivateur): two hits, both unrelated ("The three parts of Erdős
Problem 12", "Double Telescopes"). arXiv API: abs:"totally aspherical" (2, unrelated: Cherednik algebras, Poisson
manifolds); abs:"exact colimits" (1, unrelated); abs:"quasi-filtered" (3, unrelated); Isbell + Mitchell + colimit (0);
"homotopy colimit" + "category of elements" (1, unrelated); colimits + homotopy colimits + filtered (4, none states the
paper's results); au:Chorny + colimit (2: small homotopy functors, small linear functors); au:Raptis + colimit (1:
higher derivators and K-theory); au:Dwyer + au:Kan + diagrams (0). Web searches (12 Nov for the PRETOT review, and
today) found nothing stating Proposition 2.3, Theorem A or Theorem B. I did not open the pre-arXiv papers of Dwyer and
Kan on diagrams of simplicial sets, nor the full texts of Chorny or Raptis, so the gate for Proposition 2.3 and Remark
2.4 is passed only as far as these searches go. The paper claims no novelty for them, which is right. For Theorems A
and B, "results we did not find in the literature we searched" is accurate as of today.

## 4. Section 6: the quotations and the reading

Compared with the edition's PDF of Chapter II (Künzer, Malgoire, Maltsiniotis; `Der-ChII-234.pdf`, "Version 8 juillet
2001"):
- ms. p. 36 (PDF p. 23): "cela implique-t-il que X soit filtrante ? Ça ne m'étonnerait pas": **identical** to the
  paper's quotation (typographic apostrophe in the edition; `'` in the TeX renders the same).
- ms. p. 36ter (printed page 23, PDF p. 25): "Cela me fait soupçonner que la conjecture X totalement W∞-asphérique
  ⟹ X filtrante pourrait être valable.": **identical** (the edition displays the implication on its own line).
- "page 23 of the edition's file" is the printed page; the PDF page is 25 (R6).
- Reading: Proposition 2.19 (ms. 36) and its Corollary ("Δ° … totalement W∞-asphérique") are marked "Faux" by
  Grothendieck (footnotes 43 and 45), and Contre-exemple 2.20 is written against them; "his doubt" understates this
  (R5). His Contre-exemple 2.20 passes through XII Th. 4 Cor. 4, which does not hold for W∞ (from i ∈ W∞ only the
  acyclicity of X/H follows); his conclusion stands. The paper's two reasons (Propositions 2.3 and 2.8) are correct and
  do not use that step.

## 5. Repairs, with exact wording (none changes a statement)

- **R1** = 1.6.1 (`sec1_intro.tex`, Theorem A: "non-empty finite linearly ordered").
- **R2** = 1.6.2 (`sec5_twographs.tex`, proof of Theorem 5.10).
- **R3** `D1_paper.tex`, bibliography: "\bibitem{AKR} J.~Ad\'amek, V.~Koubek and J.~Reiterman, article in
  Czechoslovak Math.\ J.\ 31 (1981), 368--389." → "\bibitem{AKR} J.~Ad\'amek, V.~Koubek and J.~Reiterman, Embeddings
  into categories with fixed points in representations, Czechoslovak Math.\ J.\ 31(106) (1981), no.~3, 368--389."
- **R4** `sec2_classes.tex`, after Definition 2.1: "conditions of the form (QF1), (QF2) are studied in \cite{IM76}
  and, under the name quasi-filtered, by Ad\'amek, Koubek and Reiterman \cite{AKR}." → "(QF1) and (QF2) are the
  conditions I and IV of \cite[\S 2]{IM76} for the representable functors; in \cite[p.~369]{AKR} a category is called
  quasi-filtered (after Ad\'amek and Reiterman) if every parallel pair has a quasi-filter and any two objects have a
  common successor, and by \cite[Theorem~[1]]{AKR} and \cite[Lemma~2.1]{IM76} a connected category is quasi-filtered in
  that sense if and only if it satisfies (QF1) and (QF2)."
- **R5** `sec6_manuscript.tex`, item 2: "His doubt about the corollary is right: $\boldsymbol\Delta^{\circ}$ is not
  total." → "Grothendieck marked Proposition~2.19 and this corollary as false (footnotes 43 and 45) and wrote his
  Contre-exemple~2.20 against them; indeed $\boldsymbol\Delta^{\circ}$ is not total." At the end of the item, add:
  "(His Contre-exemple~2.20 uses Chapter~XII, Th\'eor\`eme~4, Corollaire~4, which does not hold for $W_\infty$; the
  two arguments above do not use it.)"
- **R6** `sec6_manuscript.tex`, first sentence: "is on page 23 of the edition's file for that chapter" → "is on the
  printed page 23 (page 25 of the PDF) of the edition's file for that chapter".
- **R7** `sec1_intro.tex`, after "$\Delta_{\mathrm{inj}}$ is exact by \cite[Theorems~1 and~3]{IM73}": add "(their
  category is that of the order-preserving injections of finite totally ordered sets; $\Delta_{\mathrm{inj}}$ is a full
  cosieve of it, and common successors and affine equalizers pass to a non-empty cosieve)".
- **R8** `sec2_classes.tex`, after Definition 2.1: "and in \cite{Rosicky}" → "and in \cite[Remark~4.5(1)]{Rosicky}".
- **Before posting** (not a repair): confirm the locators of the "not opened" list in item 2.

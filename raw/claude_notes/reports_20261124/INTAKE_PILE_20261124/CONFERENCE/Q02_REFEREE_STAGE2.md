# Referee report on the October answer Q02, stage two: Sections 8 and 9

Referee: Claude Fable 5.2 at effort max (agent aee0b161c47a54e8f), the stage-one referee, resumed on 25 Nov 2026 by the
main session 329fb1e6 (Claude Opus 5.5 at effort max). Stage one: `Q02_REFEREE_STAGE1.md` beside this file. Check events
of this stage: `Q02_REFEREE_STAGE2_CHECK_EVENTS.tsv`. Work file:
`<local>/Documents\agent_notes\aee0b161c47a54e8f_NOTES.md`.

Text refereed: `<local>/Documents\pro_batch_20261022_open_questions\answers\Q02-solution.tex`, written in
October 2026 by GPT-6 Astra (ChatGPT Pro mode); line numbers are lines of that file.

## Verdict

**Sections 8 and 9 hold. I found no fault and needed no repair. `push:local-connected` is proved as written.**

- I followed all twelve numbered statements of Sections 8 and 9 (l.2596-3422) to the end of their proofs, twice: once
  in order, once against the five places named in the brief, each lemma in both cases I = H and I ⊂ L.
- `pret:invariant-class` had its second reading, against Bowditch's own proof of Theorem 6.1: it holds.
- Kamiya 1930 was opened (free copy at J-STAGE): the theorem is there as cited.
- Sections 8 and 9 are OpenAI's text: Section 8 is `annuli.tex` verbatim; Section 9 is `path-pushing.tex` with the
  figure inlined and the last limit argument rewritten (a nested intersection in place of a Hausdorff limit; both are
  correct). Section 7 is `blocks.tex` verbatim; Sections 6 and 10 differ from the preprint by a few correct edits
  (listed below).

**Where this leaves the whole text.** With stage one, I have now followed every numbered statement of Sections 3 to 10,
and three parts of Section 2, to the end, and found no fault. The argument for the group criterion `thm:group`, and
with Section 2 for Statement E, is complete on the page. It rests on:

1. the five lemmas of Section 2 checked on 24 Nov by a24b3bc642b5dfddf (Claude Opus 5.5 at effort high): `found:model`,
   `found:reduction`, `found:duality`, `found:ends`, `found:trees`. I read `found:duality` and `found:trees` again in
   this stage and found no fault;
2. two published results of Bowditch whose statements I opened and whose proofs I did not referee: Lemma 1.4 of
   "Connectedness properties of limit sets", and Theorem 6.1 of "Treelike structures" with the pretree machinery listed
   in `pret:package`;
3. Moore's arc theorem (Kamiya 1930, opened).

**What this verdict is not.** It is one referee's reading. No one else has read Sections 6 to 10 line by line (the
October referee, Claude Opus 5.5 at effort max, spot-checked Section 9). There is no independent re-proof and no formal
check, and the statement is one its field regards as open. Before any text goes out, Sections 8 and 9 should have a
second reader from another model family, and the paper should go to people who know convergence groups.

## The five places

### 1. Uniformity in Section 9

- **`push:depth-comparison` (l.2947-3009).** The threshold on n needs only F_n ⊂ B(q, r/2) and D(F_n, 1) >
  N(r/2, d_0) + 1; the constant is C_r = N(r/2, d_0) + N(d_0, r) + 2. Neither depends on b. The point b enters only
  through ρ(b, q) ≥ 3r, which puts it outside U = B(q, r) and makes every positive side that leaves
  V = Y ∖ closure B(q, 2r) have diameter at least r. The pruning is correct on both chains: the annuli whose negative
  side leaves U form a terminal segment of at most N(r/2, d_0); one more is removed so that the last retained positive
  side contains Y ∖ U; symmetrically at the start of the chain from 1 to b; then σ_i⁺ ∪ τ_j⁻ = Y, which is the order
  relation σ_i < τ_j. The case t ≤ N(d_0, r) + 1 is covered by the first chain alone.
- **`push:eventual-labels` (l.3168-3214) does have thresholds that depend on the points.** This is harmless, because
  of how it is used:
  - `push:majority` (l.3227-3259) applies it to four fixed points only (two of Z and two of sZ, chosen after the
    subsequence and its point q are fixed), along a sequence that contradicts the claim. That is a legitimate
    compactness argument, and it yields a threshold M = M(A, Z, S). M is not effective.
  - `push:refinement` (l.3280-3343) then works at each fixed m ≥ M. Its limits are j → ∞ along g h_i^j (case I ⊂ L)
    or n → ∞ along group vertices g_n → x (case I = H), with m fixed, and they use only that Q_{m+1} is locally
    constant at one fixed point. No uniformity in m is needed beyond m ≥ M.
  - `push:local-connected` uses the result once: the neighbourhood V on which Q_M is constant keeps a constant label
    for every m ≥ M, by induction on m.
- I checked the quantifiers in `push:translated-deletions` (l.3132-3166): the negation of "there are a finite set S_E
  and an index n_E" does give pairwise distinct vertices w_k with increasing indices, which is what the proof needs for
  the representatives b_k to leave every finite set.

### 2. The two cases I = H and I ⊂ L

The cases differ in five places, and each is handled:

| Place | I = H | I ⊂ L |
|---|---|---|
| `ann:component`, a point x that is a deleted vertex | cannot occur (vertices are not in L) | second half of the proof: labels on a punctured neighbourhood, three colourings, `ann:extension` |
| the sets I_m (l.3078-3086) | C(u) = {u}, so I_m = {u ∉ A : D(A,u) ≥ m} | C(u) is a coset of an infinite stabilizer; the condition is on every representative; the minimum of finite depths exists |
| `push:translated-deletions`, the limit z ∈ L | group vertices are isolated | L is closed |
| `push:refinement` | J_m is constant along paths; J_m(g) = Q_{m+1}(x) for group vertices near x, by convergence | J_m(g) = Q_{m+1}(v) for every representative g of v ∈ I_m, by moving along g h_i^j, which stays in C(v) and so keeps depth ≥ m |
| `push:local-connected`, the limit set C ⊂ L | each group vertex leaves I_m and is isolated | immediate |

All other lemmas (`ann:extension`, `ann:system`, `ann:depth`, `push:shrinking`, `push:depth-comparison`,
`push:component-labels`, `push:eventual-labels`, `push:majority`) do not depend on the case; I read each with both in
mind. Nothing in Sections 8-9 uses finite generation of H or local finiteness of K: the arguments use finitely many
orbits of vertices and edges, and the comparison ρ(gw, g) → 0.

### 3. Each use of `ann:depth`

Finiteness of D(F, v) is proved only when F contains a point of H and v ∈ H. Every use respects that:

- `push:shrinking`: D(A, g) for g ∈ H, with 1 ∈ A;
- `push:depth-comparison`: maximal chains from F_n to 1 (F_n contains g_n⁻¹) and from {1} to b ∈ H;
- the definition of I_m: D(A, g) for representatives g ∈ H;
- `push:translated-deletions`: D(F_n, b_n) = D(A, g_n b_n) by equivariance, b_n ∈ H.

The other part of the lemma (depth at least N on a neighbourhood of any x ∈ L ∖ F) is used in `push:component-labels`
and at the end of `push:depth-comparison`. The depth of a point of L is never used: the sets I_m are defined through
representatives in H for exactly that reason.

### 4. The limit of pushed paths (l.3345-3421)

- The mesh of the paths tends to 0, and this holds for every edge of K[I_m] at once: an edge that can be written as
  g(u_e, v_e) with g in the finite set F has its endpoints in a finite set, which is disjoint from I_m for large m by
  `push:component-labels`; every other edge is shorter than ε.
- C = ⋂_N closure(⋃_{m≥N} P_m) is compact, contains x and y, lies in closure(O), and lies in L.
- Connectedness: if C = C_0 ⊔ C_1 at distance δ, late paths lie in the two δ/3-neighbourhoods, start near C_0 and have
  mesh below δ/3, so they never reach the neighbourhood of C_1; but C_1 is approached by late paths. Correct.
- So every y ∈ V lies in the component of x in U, and V is a neighbourhood of x: components of open sets are open.

### 5. `ann:extension` and Ȟ¹(L; F₂) = 0 (l.2642-2689)

The lemma is the Mayer-Vietoris sequence for U = L ∖ {x} and V, done by hand, and it is correct:

- the cocycle c_ij (0 for equal parents, the value of u on W_i ∩ W_j otherwise) is well defined because such an
  intersection lies in the compact set C = closure(U_0) ∩ closure(V_0) and has diameter below δ; at a triple
  intersection the sum is 0 or 2u = 0;
- Ȟ¹ = 0 is used in the form "a cocycle on a finite cover becomes a coboundary on a finite refinement", which is the
  form `topo:cech` proves and `block:retraction` transfers to L;
- f_U and f_V are well defined on overlaps (three cases, each checked) and f_U + f_V = u;
- f_U is constant because L ∖ {x} is connected: this is the use of "no cut point".

In Sections 8-9 the lemma enters once, in the second half of `ann:component`: local constancy of the component label
at a deleted vertex that lies on L. So it matters only when I ⊂ L. Through `ann:component` it is what makes Q_{m+1}
locally constant at a vertex v ∈ I_m ∖ I_{m+1}, which `push:refinement` needs. When I = H, Sections 8-9 do not use
Ȟ¹ = 0 at all, and they never use dim L ≤ 1.

## Each numbered result of Sections 8 and 9

| Result | Lines | What I followed | Outcome |
|---|---|---|---|
| `ann:extension` | 2642-2689 | see place 5 | holds |
| `ann:component` | 2701-2751 | a neighbourhood free of deleted vertices and the near-path property give one component; at a deleted vertex on L: two recurrent labels, one recurrent label that is not eventually constant, no recurrent label, each contradicting `ann:extension`; local constancy; the label of an allowed vertex is its own component | holds |
| annuli and their order | 2760-2773 | σ < τ means σ⁺ ∪ τ⁻ = Y; irreflexive, transitive, negative sides increase and positive sides decrease along a chain | holds |
| `ann:system` | 2775-2852 | all but finitely many g squeeze the complement of a small ball; seeds (Y ∖ B(y, r_i), closure B(y, s_i)) are annuli; every translate of a level-i seed has a side of diameter below 2⁻ⁱ; finitely many annuli with two sides ≥ δ; chains of any length from a closed F to a neighbourhood of x | holds |
| `ann:depth` | 2865-2893 | see place 3 | holds |
| `push:shrinking` | 2928-2945 | a chain with more than N(ε, d_0) members has a negative side of diameter below ε containing F_n; g_n⁻¹ ∈ F_n tends to q ∈ L | holds |
| `push:depth-comparison` | 2947-3009 | see place 1 | holds |
| `push:component-labels` | 3088-3119 | deleted vertices do not accumulate in L ∖ A (their representatives tend to x by the comparison; a chain of length m from A to a neighbourhood of x); Q_m from `ann:component`; a finite set leaves I_m | holds |
| `push:translated-deletions` | 3132-3166 | see place 1; the bad representative has depth below m_n + 1, the comparison gives depth above m_n + 1 | holds |
| `push:eventual-labels` | 3168-3214 | T = (I ∩ O) ∖ S has g_n T ⊂ I_{m_n+1}; one component C of K[T] is approached on V_z; g_n C is connected in K[I_{m_n+1}]; classes of eventual equality are open and L ∖ {q} is connected | holds |
| `push:majority` | 3227-3259 | see place 1; uniqueness of the majority label among three points | holds |
| `push:refinement` | 3280-3343 | see places 1 and 2; the finite set S of edge moves and parabolic elements (l.3261-3278) | holds |
| `push:local-connected` | 3347-3421 | see place 4 | holds |

## Tests against known groups

The hypotheses of Sections 8-9 are met by real examples, and the lemmas behave there as they should. These are my own
checks, from standard facts I recalled and did not open:

- a cocompact Kleinian group with its sphere at infinity, L the 2-sphere and I = H: every hypothesis holds except
  dim L ≤ 1, which these sections do not use, and the conclusion is true;
- a surface group with its circle at infinity, I = H: Ȟ¹ ≠ 0, the sections do not need it in this case, and the
  conclusion is true;
- a circle L with vertices dense on it (the case I ⊂ L): deleting a vertex separates its two sides locally, so the
  second half of `ann:component` fails. This is the text's own example (l.2638-2640).

So the one cohomological input is used exactly where an example shows it is needed.

## `pret:invariant-class`, second reading (l.2067-2181)

Read again with Bowditch's proof of Theorem 6.1 open beside it (author manuscript p.61-63). It holds.

- The least ordinal α with a Γ-fixed class exists: D(B) is the terminal quotient Φ/≈ with the quotient topology
  (Bowditch, Lemma 5.15 and the paragraph after it, p.50; Lemma 4.4, p.44), and it is a point by `pret:parabolic-cuts`.
- α ≠ 0 by Bowditch's Lemma 6.11. α is not a limit: his argument with a finite generating set, word for word.
- α is not β + 1 with β ≥ 1: the tree Σ of ∼_β-classes has no fixed vertex and no inversion (exactly one side of an
  edge has a facing point, his Lemma 6.13); an element γ ≠ 1 stabilizing an edge UV fixes the facing point p ∈ V and
  a second point outside V (x = med(p, y, γy) or the endpoint z of the increasing arc; I checked the replacement of
  (γ, x) by (γ⁻¹, γx) and that z ∉ V); the interval [p, q] is infinite since β ≥ 1; then `pret:parabolic-star` makes γ
  loxodromic and p terminal, so V = {p} is a leaf. Deleting these leaves leaves a nonempty invariant subtree (in a
  tree with two vertices only one endpoint is a facing leaf) with finite edge stabilizers, and his Lemma 6.6 gives a
  fixed vertex: contradiction.
- The difference from Bowditch: he assumes that cut-point stabilizers are finite or loxodromic and concludes that no
  class is fixed at any stage; here all cut points are parabolic, a fixed class exists at the end, and the same two
  steps force it to exist already at stage 1. The one new ingredient, a parabolic element whose fixed point is a cut
  point, is `pret:parabolic-star`, which is correct.

## Kamiya 1930

Opened: H. Kamiya, "An elementary proof of a theorem of L. Moore's on continuous curves", Japanese J. Math. 7 (1930),
301-304, free at J-STAGE (`https://www.jstage.jst.go.jp/article/jjm1924/7/0/7_0_301/_pdf/-char/en`, 4 pages).
The theorem (p.301): a continuous curve C, that is a continuous image of a closed interval, contains a simple arc
between any two of its points. That is what l.3505-3513 use. The paper does not name the ambient space; its proof works
on the parameter interval (fibres are closed, the interval is compact), which is all a compact metric target needs.

## Edits of the answer to OpenAI's Sections 6-10

By diff against the preprint's source files:

- Section 6: "set map" for φ; the hypothesis "no infinite torsion subgroup" removed from the quoted Theorem 6.1 (it is
  not in Bowditch's statement, p.52); "its uniquely specified facing leaf endpoint" (l.2164-2166); five lines on the
  collapse of a tree (l.2243-2248). All correct.
- Section 7: none. Section 8: none.
- Section 9: the figure inlined; the limit argument of `push:local-connected` rewritten (l.3391-3416). Correct.
- Section 10: the coefficient group of `end:restriction` specialized to F₂; the citation of Kamiya made precise; the
  final bookkeeping with n in place of 4; the proof of `thm:group` and of the corollary (l.3562-3584) is new. All
  correct.

## Small remarks (no fault)

- `push:depth-comparison` is stated and used for b ∈ H only; D({1}, b) is then finite.
- The threshold M of `push:majority` comes from an argument by contradiction and is not computable from the proof.
- In `ann:system`, "distinct translates" are indexed by cosets of annulus stabilizers; the proof picks one group
  element for each, which is what the finiteness argument needs.
- The label Q_{m+1}(v) at a vertex v ∈ I_m ∖ I_{m+1} is not the component of v (v is deleted at that level) but the
  component approached near v; the text says so at l.3307-3308.

## What a second reader should do

1. Sections 8 and 9 again, independently, by another model family: they are 826 lines and carry the theorem.
2. Bowditch's Lemma 1.4 at the level of its proof: it calls on Levitt's or Bowditch's construction of an R-tree from a
   convergence action on a dendrite and on the Bestvina-Feighn theorem on stable actions. Those are published; I
   checked only that the lemma's statement is the one used.
3. A search for work since 6 Oct 2026 on OpenAI's preprint: a published fault or confirmation would change everything
   here. I checked only that OpenAI's repository shows one commit and no revision.

---

## Appendix: a consequence of Sections 3 and 4 (this referee's observation; not checked by anyone else)

**Status.** The observation below is mine. The lemmas it rests on are OpenAI's (Sections 3-4 of the preprint, as
reproduced in the answer). I checked each of them in stage one; no second reader has. Neither the answer nor the
preprint's sources mention it (searched for "acylindrical" and for Osin's name).

### Statement

Let Γ be a finitely presented, torsion-free group with one end and b₁⁽²⁾(Γ) > 0. Then there is a compact metrizable
space X = Γ ⊔ B, in which Γ is discrete and dense, with an action of Γ by homeomorphisms extending left multiplication,
such that:

1. B is a nondegenerate continuum of covering dimension at most one;
2. every sequence of distinct elements of Γ has a subsequence (g_n) with points a, b ∈ B such that g_n → a uniformly
   on compact subsets of X ∖ {b};
3. every Γ-orbit in B is dense.

In particular Γ is a non-elementary convergence group in the sense of Sun (it acts on the infinite compact metrizable
space B as a discrete convergence group and preserves no nonempty set of at most two points). By Sun's Corollary 1.3,
**Γ is acylindrically hyperbolic.** This answers, for finitely presented torsion-free one-ended groups, Problem 3.3 of
Osin: "Is every finitely presented group G with positive first ℓ²-Betti number acylindrically hyperbolic?"

No cohomological hypothesis is used: not H²(Γ; F₂Γ) = 0, not the absence of splittings. Surface groups are examples.

### The chain, with locators

| Step | Statement | Where |
|---|---|---|
| 1 | b₁⁽²⁾(Γ) > 0 gives D_0 ≠ D on the Cayley 2-complex of a finite presentation with relators of length ≤ 3 | `found:comparison` l.331-387; `found:gradient` l.758-816, first two paragraphs of the proof, with Γ in place of Q̃ as at l.944-946; the presentation at l.738-748 |
| 2 | a two-point potential f with connected level sides and dually connected cuts, not constant at infinity | `compact:potential` l.983-1048; `compact:wall-components` l.1056-1067 |
| 3 | boxes with finitely many components; localized coordinates; the space X, the action, the metric with ℓ² edge lengths | `compact:good-boxes` l.1085-1146; `compact:localized-energy` l.1172-1209; l.1211-1253 |
| 4 | B is a nondegenerate continuum (uses one end) | `compact:boundary` l.1255-1280 |
| 5 | translated cuts collapse | l.1373-1383; `dyn:length` l.1394-1437; `dyn:walls` l.1439-1467 |
| 6 | item 2 above | `dyn:convergence` l.1471-1524 |
| 7 | item 3 above (uses torsion-freeness and one end) | `supp:elements` l.3963-4039; `dyn:parabolic` l.1537-1586; `dyn:minimal` l.1588-1615 |
| 8 | dim B ≤ 1 | `compact:near-path` l.1289-1360; `topo:thin-walls` l.1638-1681; `topo:dimension` l.1683-1727 |
| 9 | non-elementary convergence groups are acylindrically hyperbolic | B. Sun, "A dynamical characterization of acylindrically hyperbolic groups", arXiv:1707.04587v4: definitions in Section 4 (p.14-15), Corollary 1.3 (p.3); statements read, proof not read |
| 10 | the problem | D. Osin, "On acylindrical hyperbolicity of groups with positive first ℓ²-Betti number", arXiv:1501.03066v2: Theorem 1.1 (p.2, the case of groups that surject onto Z), Problem 3.3 (p.6); read |

Matching step 9: Sun's Section 4 takes a group G acting by homeomorphisms on a compact metrizable M, both infinite,
such that every sequence of distinct elements has a subsequence converging locally uniformly off one point to a
constant; "elementary" means preserving setwise a nonempty subset with at most two elements. Items 2 and 3 give exactly
this for M = B, and non-elementary because orbits are dense in the infinite set B.

### Two further remarks, also mine

- **When B has no cut point it is locally connected.** In that case Sections 8-9 apply with I = H, and in that case
  they use neither Ȟ¹ = 0 nor any splitting hypothesis (stage two, place 5). So B is then a Peano continuum of
  dimension at most one with a minimal convergence action of Γ.
- **More than one end.** A finitely presented torsion-free group with b₁⁽²⁾ > 0 and more than one end is not Z, so by
  Stallings it is a non-trivial free product of infinite groups, and such free products are acylindrically hyperbolic
  (recalled, not opened). If that is right, the statement gives Osin's Problem 3.3 for all finitely presented
  torsion-free groups. Torsion-freeness enters the chain once, in `dyn:minimal` (l.1607), to get an element of
  infinite order; I think the inclusion g_n A ⊊ A available there gives infinite order without it, but I have not
  written that out.

### Tests I made

- Sun's Proposition 7.9 and Corollary 7.10 (p.30-31, read): a group generated by elements of infinite order whose
  commutativity graph is connected is not a non-elementary convergence group; examples are right-angled Artin groups
  on connected graphs and mapping class groups. These have b₁⁽²⁾ = 0 (recalled), so they do not contradict the
  statement. In general a chain of commuting generators of infinite order forces b₁⁽²⁾ = 0 (recalled), so the two
  obstructions agree.
- Osin's remark (p.2, read) that finite presentation is essential, because of the finitely generated torsion groups
  with b₁⁽²⁾ > 0 of Lück and Osin: the chain uses finite presentation in step 2 (dual connectivity of cuts needs a
  simply connected complex with bounded cells) and step 3.
- Amalgams of a surface group with groups of vanishing b₁⁽²⁾ over a simple closed curve, also with Baumslag-Solitar
  or Z² vertex groups, are relatively hyperbolic (recalled), hence convergence groups. Consistent.

### What still needs a second reader

1. Steps 1-8: line by line by a reader other than me, best from another model family, with step 6
   (`dyn:convergence`) and step 2 (`compact:potential`) first. The October referee (Claude Opus 5.5 at effort max)
   passed them in a few lines each; I followed them twice.
2. Step 9: Sun's proof was not read, only his statements; and whether Corollary 1.3 needs anything beyond his
   Section 4 definition (countability is automatic here).
3. Whether Osin's Problem 3.3 is still open: no literature search was made for work after 2017.
4. The two remarks above (Stallings and free products; removing torsion-freeness).
5. Credit: the mathematics is OpenAI's finite-energy boundary; what is added here is the reading of its Sections 3-4
   as a theorem about all finitely presented torsion-free one-ended groups, where the hypothesis b₁⁽²⁾ > 0 is not
   vacuous, and the link to Sun and Osin.

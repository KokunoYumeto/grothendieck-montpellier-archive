# Referee report on the October answer Q02, stage one: Sections 3, 4 and 5

Referee: Claude Fable 5.2 at effort max, a fresh agent launched on 25 Nov 2026 by the main session 329fb1e6 (Claude
Opus 5.5 at effort max); row 4 of the conference program, Session 7. Brief:
`<local>/Documents\agent_notes\Q02_REFEREE_BRIEF_20261125.md`. Check events:
`Q02_REFEREE_STAGE1_CHECK_EVENTS.tsv` beside this file. Notes: `<local>/Documents\agent_notes\Q02_referee_NOTES.md`.

Text refereed: `<local>/Documents\pro_batch_20261022_open_questions\answers\Q02-solution.tex` (4,472 lines),
written in October 2026 by GPT-6 Astra (ChatGPT Pro mode). Line numbers below are lines of that file.

The verdict and the per-statement tables were written before I opened the October referee report. What that report says,
and what I did after writing the verdict, is in the last three sections.

## Verdict

**Sections 3, 4 and 5 hold. I found no fault, and I needed no repair.**

- I followed every numbered statement of Sections 3-5 (14 statements) to the end of its proof, and with them the
  unnumbered estimate (4.1) at l.1373-1383 and Lemma `supp:elements` (l.3963-4039, printed in Section 11), on which
  Section 4 rests for its two facts about elements of convergence groups.
- **No use of dimension four, and none of any dimension.** Sections 3-5 never use Q, the formal dimension or a
  cohomological dimension; the letter n occurs only as a sequence index. They cite Section 2 twice, both times Lemma
  `found:duality` for H²(Γ; F₂Γ) = 0 (l.1733, l.1792). Their inputs are five facts about the group, all supplied by
  Section 2 (for the group criterion `thm:group`, the first, second, fourth and fifth are hypotheses and the third is
  the assumption to be refuted):
  1. a finite presentation with relators of length at most three, so a simply connected Cayley 2-complex with bounded
     incidence: used throughout;
  2. one end: used in `compact:boundary` (connectedness of B) and in `dyn:minimal`;
  3. the gradient spaces differ, D_0 ≠ D, which is what b₁⁽²⁾ > 0 gives: used once, in `compact:potential`;
  4. torsion-freeness: used once, in `dyn:minimal`;
  5. H²(Γ; F₂Γ) = 0: used once, in `topo:cech` (l.1792). It is used correctly: the finite-support 2-cochain is
     ω = dα, it vanishes on every cellular 2-cycle, so it is a cocycle on the free resolution extended past the
     presentation complex, which need not be aspherical.
- **The absence of splittings is not used in Sections 3-5.** Its first use is in Section 6.
- **No passage between the group and the space occurs in Sections 3-5.** After the standing hypothesis (l.939-946)
  everything happens on the Cayley 2-complex of Γ. The passage that feeds these sections is `found:gradient`
  (b₁⁽²⁾(Q̃) > 0 gives D_0 ≠ D), in Section 2. It had no check event from 24 Nov, so I checked it, with
  `found:comparison` and the extension to PD(n) groups: they hold (section "Section 2" below).
- **Sections 3-5 are OpenAI's text.** I compared them with the preprint's source files (in the task's `SOURCES.zip`):
  Section 3 is `compactification.tex` verbatim; Section 4 is `dynamics.tex` plus one sentence (l.1533-1535) pointing to
  `supp:elements`; Section 5 is `boundary-topology.tex` plus the explicit refinement map at the end of `topo:cech`
  (l.1829-1840). Both additions are correct. The public copy (github.com/openai/math, one commit, 6 Oct 2026) has the
  same 14 source files, by git blob hash: OpenAI has published no revision or erratum.
- Both sources cited in Sections 3-5 were opened at the statements used, from free copies, and say what the answer says
  they say (section "Sources opened"). Neither is a proof input: the Royden reference is context, and the two Bowditch
  facts are re-proved in `supp:elements`.

So the answer to the conference's question, for these three sections: there was no use of dimension four in them to
remove. All dependence on the dimension sits in Section 2 and enters Sections 3-5 through H²(Γ; F₂Γ) = 0 alone.

This verdict is about Sections 3-5. After writing it I read Sections 6, 7 and 10 once, to see how they use Sections 3-5
and to say what stage two should look at; I found no fault there either (last sections of this file). Sections 8 and
9, where the continuum is proved locally connected, I have not read beyond their statements. They are stage two, and
the theorem rests on them.

## What Sections 3-5 prove, in one statement

For a finitely presented, torsion-free, one-ended group Γ with b₁⁽²⁾(Γ) > 0 there is a compact metrizable space
X = Γ ⊔ B, with Γ discrete and dense, on which Γ acts by homeomorphisms extending left multiplication, such that:

- (O1) B is a nondegenerate continuum (`compact:boundary`);
- (O2) vertices near a boundary point are joined by graph paths near that point (`compact:near-path`);
- (O3) ρ(u, us) → 0 as u → ∞, for each s (l.1373-1383);
- (O4) if g_n → a and g_n⁻¹ → b in B, then g_n → a uniformly on compact subsets of X ∖ {b}; so Γ is a convergence
  group on B (`dyn:convergence`);
- (O5) ρ(g, gp) → 0 as g → ∞, for every fixed point p of a parabolic element (`dyn:parabolic`);
- (O6) the action on B is minimal (`dyn:minimal`);
- (O7) dim B ≤ 1 (`topo:dimension`);
- (O8) if moreover H²(Γ; F₂Γ) = 0, then Ȟ¹(B; F₂) = 0 (`topo:cech`).

(O1)-(O7) use no cohomological hypothesis.

## Each numbered result: what I checked and how

"Followed" means: every sentence of the proof read against the definitions, each inference re-derived by me.

### Section 3 (l.949-1361)

| Result | Lines | What I followed | Outcome |
|---|---|---|---|
| `compact:potential` | 983-1048 | The Riesz representer r_b of df ↦ f(b) − f(a) on the closed space D; the minimizer r_b/‖r_b‖²; density of the span of the r_b (a gradient orthogonal to all of them is zero), so some minimizer lies outside the closed subspace D_0; clipping to [0,1] and uniqueness give 0 ≤ f ≤ 1; the soft-threshold argument for "not constant at infinity"; replacing f by t on a component of {f > t} that misses b lowers the energy strictly, also when the component is infinite; dual connectivity of S(f,t): the cochain restricted to one dual component is a cocycle cell by cell, has a potential by simple connectivity, the potential is constant on each connected side and the two constants differ, so no crossing edge is left out. | holds |
| `compact:wall-components` | 1056-1067 | Immediate from the previous lemma and local finiteness. | holds |
| `compact:good-boxes` | 1085-1146 | The Tonelli identity and the Schur bound with the degree D of the relation "equal or on a common cell"; the case F = F′; density of good endpoint tuples; the count: after deleting the finite set E, two dually adjacent edges of one cut have their same-side endpoints joined by the third edge of the triangle, which lies in no cut; so each dual component of S_i ∖ E meets at most two components of G′; the vertex set of the box is a union of components of G′, because no cut edge has both ends in the box; repeated vertices and bigons; invariance and countability of the basis. | holds |
| `compact:localized-energy` | 1172-1209 | The three cases for an edge (both ends in U, neither, one); the bound by max_i \|dF_i\|; the cut inclusion at the levels a_i + t and b_i − t; the role of t < 1 for the cap. | holds |
| (unnumbered) | 1211-1253 | X compact metrizable; vertices isolated; the action as a coordinate permutation; the metric ρ; ‖λ‖₂ ≤ Σ c_j ‖dF_j‖₂ by Minkowski. | holds |
| `compact:boundary` | 1255-1280 | B nonempty; B not a point because f is a coordinate; connectedness from ‖λ‖₂ < ∞ and one end. | holds |
| `compact:near-path` | 1289-1360 | The identities Σ_j h_{O,U_j} = ψ_O and h_{O,U_i} h_{O,U_j} = 0 on X; the selected component U_O(x); the three conditions on the small box O′; U′ ⊂ U_O(x) for every tested box of positive margin; the three cases for a tested localized coordinate; the set V; the sequential form. | holds |

### Section 4 (l.1363-1615) and `supp:elements` (l.3963-4039)

| Result | Lines | What I followed | Outcome |
|---|---|---|---|
| estimate (4.1) | 1373-1383 | The action on cellular edges is free and λ is in ℓ². | holds |
| `dyn:length` | 1394-1437 | Tonelli; a(e′) = Σ_{e near e′} \|dF(e)\| is in ℓ²; its pairing with λ∘g tends to 0 (finite-support approximation of both factors); the diameter bound along a simple dual path, with a constant depending only on the presentation (4 suffices). | holds |
| `dyn:walls` | 1439-1467 | A subsequence with summable integrals gives length sums tending to 0 at almost every level; one anchor vertex in each of the finitely many dual components, moved to a by (4.1); the diameter bound gives uniformity; localized coordinates through the cut inclusion (translations and reflections of the level preserve null sets); both directions at once. | holds |
| `dyn:convergence` | 1471-1524 | The reduction to vertices v_n → r, g_n v_n → s; the two cuts; the r-side stays at positive distance from b, so no edge between two r-side vertices lies in g_n⁻¹(second cut); a path inside the r-side component from v_n to an endpoint w_n of the first cut is mapped by g_n to a path from near s to near a that crosses no edge of the second cut: contradiction. The case where r is a vertex. Proper discontinuity on triples. | holds |
| `supp:elements` | 3963-4039 | Fixed points of an infinite-order element lie in the collapse pair; the case of one fixed point; the nested neighbourhood W and convergence of all powers; the compact set K = Ū ∖ γ^m U whose translates cover; finite index of ⟨γ⟩ in the pointwise stabilizer of {a,b}; "fixing one endpoint forces fixing the other" through g_n = γ^{mk_n} h γ^{−n}, in both cases w = r and w ≠ r. Compared with Bowditch's own argument (Treelike structures, p.54-55): the same proof, written out for metric spaces. | holds |
| `dyn:parabolic` | 1537-1586 | h^{±n} → p as vertices; whole-coset escape of g_n⟨h⟩; the three first-passage vertices at distances between 0 and ρ(a,c); the conjugates k_n = g_n h g_n⁻¹ move each to its successor; both cases (k_n escaping, k_n constant) contradict. | holds |
| `dyn:minimal` | 1588-1615 | Invariant sets with two points are dense; a global fixed point c forces g_n⁻¹ → c, then g_n A ⊂ A and g_n⁻¹ C ⊂ C; such a g_n is not parabolic by `dyn:parabolic` (the pointwise convergence on B is what is used), so it is loxodromic, so Γ = Stab(c) is virtually cyclic, against one end. | holds |

### Section 5 (l.1618-1848)

| Result | Lines | What I followed | Outcome |
|---|---|---|---|
| `topo:thin-walls` | 1638-1681 | At almost every level the wall has finite total length of nearby edges; after deleting a finite part D_n the remaining wall has finitely many dual components, whose endpoint sets cover E(F,t) and have total diameter at most the tail of a convergent series; localized coordinates through the cut inclusion. | holds |
| `topo:dimension` | 1683-1727 | A compact set of H¹-measure zero has small clopen partitions (spheres that miss it); the sign of F − t near a point outside E(F,t) is well defined by `compact:near-path`, also when F(x) = t, and locally constant; a sign tuple pins each tested coordinate to one closed grid interval, so sign-tuple sets are small in ρ; the cover has multiplicity at most two. | holds |
| `topo:cech` | 1737-1841 | The labels i(u) and the Lebesgue number; dα has finite support (cells escaping to infinity shrink to a point, where the nerve cocycle identity applies; bigons and loops give zero in characteristic two); ω = dα is a cocycle on the extended resolution; H²(Γ; F₂Γ) = 0 gives a finite-support η with dη = dα; α − η = dl; the germ l_i(x) is well defined by `compact:near-path` and locally constant; l_i + l_j = d_ij on overlaps; the refinement and the identity r*d = δc. | holds |

### Recomputation

Sections 3-5 contain almost nothing numerical. For the combinatorial statements of Section 3 I ran a finite model (a
triangulated grid, which is a simply connected triangular complex; two sizes). At 1,964 level classes of four two-point
minimizers both level sides were connected and the cut dually connected; the co-area identity held to 10⁻¹¹; for 436
random boxes the component count obeyed the bound of `compact:good-boxes`, and the energy inequality and the cut
inclusion of `compact:localized-energy` held. Script and output:
`CONFERENCE\checks\q02_s3_finite_sanity.py`, `q02_s3_finite_sanity_output.txt`. This is evidence on a finite example,
where D_0 = D; it tests the mechanics, not the lemma about infinity.

## Section 2: the three parts that had no check event

The check of 24 Nov by a24b3bc642b5dfddf (Claude Opus 5.5 at effort high) covers `found:model`, `found:reduction`,
`found:duality`, `found:ends`, `found:trees` and Bowditch's Lemma 1.4. Its event file has no row for the three parts
below. The second is the passage from the space to the group on which Section 3 stands, so I checked all three.

| Result | Lines | What I followed | Outcome |
|---|---|---|---|
| `found:comparison` | 331-387 | The comparison maps and homotopies between free resolutions, kept under ⊗ with the von Neumann algebra without flatness; dim ker = tr(e), dim im = tr(q) by polar decomposition; additivity gives the dimension of ker ∂_1 ⊖ closure(im ∂_2); only P_0, P_1, P_2 enter, so an infinitely generated P_3 does no harm. | holds |
| `found:gradient` | 758-816 | d_1 bounded; D = ker d_1 by simple connectivity, so D is closed; closure(im d_0) = D_0; the harmonic space ker ∂_1 ∩ ker ∂_2* equals ker d_1 ⊖ D_0 and is the complexification of the real one; hence b₁⁽²⁾ > 0 gives D ≠ D_0; truncation gives a bounded representative; the soft threshold excludes a constant limit. | holds |
| PD(n) groups | 822-936 | The reversed dual D of a finite projective resolution has homology Z^w in degree 0 only; splitting off its negative part; D ≃ P̄^w as resolutions of Z^w; reduction mod 2 stays exact; Hom(L,R) ⊗ V ≅ Hom(L,V) for finitely generated projective L, giving H^i(Γ;V) ≅ H_{n−i}(Γ;V) over F₂; the Hilbert identification of the dual of a non-orthogonal summand (Q_H on im e* has inverse e*\|_H); torsion-freeness and infinitude. | holds |

The other lemmas of Section 2 I read once for the setting and did not recheck.

## Sources opened

| Cited as | Where in the answer | Free copy opened | Result |
|---|---|---|---|
| Bowditch, Treelike structures (Mem. AMS 662), Lemma 6.2 | l.1526-1529 | author manuscript, bhbowditch.com/papers/bhb-treelike.pdf, p.54 (the same file is in `<local>/Documents\Free or receipted\free\authors\bowditch\`) | Every element of a convergence group on a compact Hausdorff space with at least three points is elliptic, parabolic or loxodromic, with the definitions the answer uses. Matches. |
| the same, Proposition 6.4 and the paragraph before it | l.1529-1531 | the same, p.55 | "If x is the fixed point of a loxodromic, then its stabiliser is virtually cyclic"; Proposition 6.4. Matches. |
| Keller-Lenz-Schmidt-Wojciechowski, Note on uniformly transient graphs, Section 4 | l.1213-1214 | arXiv:1412.0815v1 | Section 4 is on the Royden compactification (Definition 4.1, the Royden algebra of bounded finite-energy functions). A pointer for context; accurate. |

## An attack by consequences

Since the proofs held, I tried to break the statements through what they imply. Facts marked "recalled" I did not open.

- **(O4) and (O6) alone are a theorem a second field would notice.** They say: every finitely presented,
  torsion-free, one-ended group with b₁⁽²⁾ > 0 is a non-elementary convergence group. B. Sun proved that non-elementary
  convergence groups are acylindrically hyperbolic (arXiv:1707.04587v4, abstract read). Together they answer, for these
  groups, Problem 3.3 of D. Osin (arXiv:1501.03066v2, p.6, read): "Is every finitely presented group G with positive
  first ℓ²-Betti number acylindrically hyperbolic?" Osin proves it for groups that surject onto Z and notes that finite
  presentation is needed. So Sections 3-4 carry a second result, and a second place where an error would show.
- Tests of that consequence:
  - Right-angled Artin groups: b₁⁽²⁾ > 0 exactly when the defining graph is disconnected (Davis-Leary, recalled),
    which is when the group is a free product. With a connected graph the generators form a chain of commuting
    elements of infinite order; in a convergence group commuting elements of infinite order have the same fixed
    points (by `supp:elements`), so the whole group fixes a point or a pair and the action is elementary. Consistent.
  - Finite presentation: the finitely generated torsion groups with b₁⁽²⁾ > 0 of Lück and Osin (cited by Osin, p.2)
    cannot be non-elementary convergence groups. The proof uses finite presentation exactly where it must: in the
    dual connectivity of walls (`compact:potential`) and their finite number of components.
  - Amalgams over Z of a surface group with a group having b₁⁽²⁾ = 0, and small-cancellation quotients of free
    products, are relatively hyperbolic (recalled), so convergence groups. Consistent.
- Tests of (O8) and of the criterion:
  - I looked for a group that satisfies the hypotheses of Sections 3-5 with H² = 0 and is known to have b₁⁽²⁾ > 0;
    by the criterion it would have to split over Z. For Γ = A *_C B with C ≅ Z and finitely presented vertex groups,
    Mayer-Vietoris makes H²(Γ; F₂Γ) contain the cokernel of H¹(A; F₂Γ) ⊕ H¹(B; F₂Γ) → H¹(C; F₂Γ). My own computations
    give a non-zero cokernel in these cases: A and B one-ended; one of them free and the other free or one-ended;
    A = A_1 * A_2 with one-ended factors, C generated by a_1a_2, and B one-ended or of the same form (a parity
    obstruction: each edge of the Bass-Serre tree of A lies on two translates of the axis); A = A_1 * ⟨t⟩, C generated
    by a word in which t occurs m ≥ 2 times, always with exponent +1, and B one-ended (an obstruction in F₂[Z/m]).
    Words with mixed exponents, and a free vertex group against an infinitely-ended one, I did not decide. So I have
    no example on which (O8) could be tested, and no contradiction.
  - A compact hyperbolic n-manifold W with totally geodesic boundary, n ≥ 4, has a fundamental group that satisfies
    the hypotheses of `thm:group` (a duality group of dimension n − 1 ≥ 3; no splitting over Z, since its boundary at
    infinity has no local cut point: recalled). Doubling gives 2 b₁⁽²⁾(W) ≤ b₁⁽²⁾(DW) + b₁⁽²⁾(∂W) = 0. Consistent.

None of these tests bears on Sections 8 and 9.

## Small remarks (no fault)

- The letter D stands for the gradient space, for a dually connected edge set (l.1404) and for the dendritic quotient.
- `dyn:walls` and `topo:thin-walls` exclude a null set of levels that depends on the chosen subsequence; the proofs
  that use them choose their levels afterwards, as they must.
- `supp:elements` assumes the convergence property for sequences of distinct group elements, which is the form in
  which `dyn:convergence` delivers it.

## After the verdict: the October report

Opened after the sections above were written: `F:\user\Documents\claude_open_courses_20260926\plan\pro_checks_20261023\Q02-check.md`,
by Claude Opus 5.5 at effort max (Message Batches API), 23 Oct 2026. It also finds Sections 3, 4 and 5 "correct as
checked", in a few lines each. It names two open items: the Bowditch statements were paraphrased and not compared with
the source, and Section 9 with parts of Section 6 was only spot-checked. The first item is closed for Lemma 1.4
(a24b3bc642b5dfddf, Claude Opus 5.5 at effort high, 24 Nov; I read the statement too, author manuscript p.6: it is the
implication (B) of l.711-722) and, for the Treelike citations, in the next section. The second is closed for Section 6
(next section) and untouched for Section 9.

## After the verdict: Sections 6, 7 and 10, read once

To see whether later sections use Sections 3-5 in a stronger form than proved, I read the sections that consume them.
They do not: `compact:near-path` enters at l.2380 and l.2536, `dyn:convergence` at l.2535, 2545, 2569, `dyn:minimal`
at l.2419, the comparison of `dyn:parabolic` at l.2281 and l.2592, `topo:dimension` and `topo:cech` at l.2267 and
l.3545-3546, each as stated. Section 6 uses only that B is a nondegenerate metric continuum with a minimal convergence
action.

Reading them, I followed their proofs to the end. This was one reading, not the two passes of Sections 3-5.

| Result | Lines | Outcome |
|---|---|---|
| `pret:package` (Section 6) | 1893-1944 | a list of statements from Bowditch's Treelike structures; each opened in the author manuscript and found as cited: Lemma 3.13 with the remark after it (p.29), Theorem 3.19 (p.30), Lemma 3.28 (p.36), Lemma 3.34 (p.40), Lemmas 4.2-4.4 with the transfinite process (p.41-44), Theorem 5.23 and D(M) = Φ/≈ (p.51, 60), Lemma 6.5 (p.56), Lemma 6.8 (p.58), Lemma 6.9 (p.59-60), Lemma 6.10 (p.60), Lemma 6.11 (p.61, proved for any minimal action on a continuum with a cut point) |
| `pret:parabolic-cuts` | 1954-1980 | holds: Lemma 1.4 makes D(B) a point; Theorem 6.1 (p.52, with its definition of a parabolic fixed point) then makes every cut point parabolic |
| `pret:parabolic-star` | 1992-2015 | holds; it is the remark after Bowditch's Lemma 6.10, proved here from Lemma 6.8 |
| facing points | 2043-2065 | holds; it is Bowditch's Lemma 6.13 and the paragraph before it (p.61-62) |
| `pret:invariant-class` | 2067-2181 | holds. Compared with Bowditch's proof of Theorem 6.1 (p.62-63): the limit step and the higher-successor step are his; the new point is that the first ordinal with a fixed class exists, because D(B) is a point, and can only be 1; `pret:parabolic-star` covers the case his Lemma 6.10 leaves out, a parabolic element whose fixed point is a cut point. Bowditch's Lemma 6.12, which assumes cut-point stabilizers finite or loxodromic, is not used. |
| `pret:tree` | 2189-2253 | holds: P lies in the invariant class by density of an orbit; minimality; finite quotient; a finite edge stabilizer would give a splitting over a finite group |
| `block:graph`, `block:near-path`, `block:retraction`, `block:setting` (Section 7) | 2256-2593 | hold, given `pret:tree` and `pret:parabolic-cuts` |
| `end:restriction`, `end:paths-in-regions`, `end:continuum`, the proofs of `thm:main` and `thm:group` (Section 10) | 3424-3584 | hold, given `push:local-connected` of Section 9; the arc theorem cited from Kamiya 1930 (l.3505-3513) I did not open |

In Sections 3-10 the absence of splittings over two-ended subgroups is used once: to make the hypothesis of Bowditch's
Lemma 1.4 vacuous in `pret:parabolic-cuts`. The absence of splittings over finite subgroups (one end) is used in
`pret:invariant-class`, through his Lemma 6.6 (p.57), and at the end of `pret:tree`. Sections 8 and 9 mention no
splitting, no torsion and no finiteness property of the group (searched); Ȟ¹(L; F₂) = 0 enters them once, in
`ann:extension` (l.2673).

## Stage two: what to look at

What remains unchecked is Sections 8 and 9 (l.2596-3422, 826 lines), and they carry the theorem: Section 10 turns
"L is locally connected" into the contradiction in one page, so everything rests on `push:local-connected`.

In order of risk:

1. **Section 9, path pushing (l.2896-3422), line by line.** Nobody has done it: the October referee spot-checked it.
   It proves that a continuum without cut points in the setting of `block:setting` is locally connected. For
   boundaries of hyperbolic groups that is the theorem of Bestvina and Mess (recalled, not opened); here there is no
   hyperbolicity and no cocompactness on triples, only (O2), (O4) and the annuli. Places to press:
   - the uniformity claims: `push:depth-comparison` (uniform over b with ρ(b,q) ≥ 3r), `push:refinement` ("the
     threshold M is independent of x and y") against `push:eventual-labels` ("the last threshold may depend on the two
     points"), and how `push:majority` bridges them;
   - the case I ⊂ L (graph vertices on the boundary, a graph that is not locally finite, a subgroup H that need not
     be finitely generated) against the case I = H: every lemma has to hold in both;
   - `ann:depth` gives finiteness of D(F,v) only when F contains a point of H and v ∈ H: check each later use;
   - the limit of pushed paths in `push:local-connected` (l.3345-3422), written "without a hyperspace compactness
     theorem" (amendment 5, l.3813-3815).
2. **Section 8 (l.2596-2894).** `ann:extension` is the one place besides Section 10 where Ȟ¹(L; F₂) = 0 is used: a
   locally constant function on a punctured neighbourhood extends over the point. Then `ann:component`, `ann:system`
   (annuli from the convergence dynamics, finitely many with two large sides), `ann:depth`.
3. **Sections 6, 7 and 10** have now been followed once by one reader. If stage two has room, a second reading of
   `pret:invariant-class` (l.2067-2181) is the best use of it: it turns Bowditch's proof of Theorem 6.1 to the
   opposite case, and it is the step of Section 6 with the most logic of its own.
4. **Kamiya 1930** (l.3505-3513): open it, or replace the citation by the standard theorem that a Hausdorff
   continuous image of an interval is arcwise connected.

One option besides stage two, for the main session to weigh: by (O4) and (O6) the output of Sections 3-4 is already an
answer to part of Osin's Problem 3.3. That statement is short and self-contained (Sections 3-4 and `supp:elements`,
about 750 lines, all checked here by one reader), and another model family could be asked to prove or refute it. It
would test the half of the argument that this stage found sound, not Sections 8-9.

Sources for stage two are on disk: `<local>/Documents\Free or receipted\free\authors\bowditch\`
(`bhb-treelike.pdf`, `bhb-connected.pdf`, `bhb-peripheral.pdf`, `bhb-topchar.pdf`); OpenAI's source files are in
`<local>/Documents\pro_batch_20261022_open_questions\Q02-singer-degree-one-all-dimensions\SOURCES.zip`.

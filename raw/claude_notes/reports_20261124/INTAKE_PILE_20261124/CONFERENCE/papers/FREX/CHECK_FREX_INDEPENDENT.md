# Independent check of FREX, "Exactness of colimits and amenability are independent for categories of finite substructures"

Checker: ac59b1f5753a32bf7 (Claude Fable 5.2 at effort max), 25 Nov 2026, for the main session 329fb1e6 (Claude Opus
5.5 at effort max). Paper written 25 Nov 2026 by a848636d0bbf3ae4b (Claude Fable 5.2 at effort max) from the run FREX
of GPT-6 Astra (ChatGPT Pro mode). I did not write the paper and I did not edit it. Brief:
`<local>/Documents\agent_notes\FREX_CHECK_BRIEF_20261125.md`. Running notes:
`<local>/Documents\agent_notes\FREX_checker_NOTES.md`. My program and its output:
`<local>/Documents\agent_notes\FREX_checker_independent_checks.py`, `...\FREX_checker_independent_checks.out`.
Sources I opened that were not yet on disk: `<local>/Documents\agent_notes\FREX_checker_sources\`.

What I did, in this order: read only the introduction; proved Theorem 1.2, Proposition 2.4, Theorem 1.3, Theorem 1.5 (c)
and the non-amenability of Theorem 1.4 myself; then read every proof of the paper to the end (tex lines 221 to 931);
opened every citation at the place cited (one could not be opened); ran the writer's program and wrote and ran one of
my own.

## Verdict

No theorem is wrong. One sentence of a remark is false as written (Remark 4.3), one proof lacks a step
(Theorem 1.3 (c), last clause), one citation is quoted in a form its source does not have (Remark 3.3), and one
sentence of the introduction claims more than is proved. Repairs R1 to R4 below; R5 to R7 are additions and small
corrections.

| Statement | Verdict |
|---|---|
| Theorem 1.2 (exact over R iff coinvariants preserve monomorphisms of smooth R[G]-modules; the topos form) | **holds.** Proved by me before reading (same functors S and T); the paper's proof then followed line by line. Cosmetic: M must be non-empty (R6a). |
| Lemma 2.2 (open subgroups; N^U → N_U injective) | **holds.** |
| Proposition 2.4 (exact iff every finite family has an affine equalizer) | **holds**, both directions. Proved by me before reading, by the same two arguments. Isbell-Mitchell 1976 opened: Theorem 3.1, Proposition 3.3 and the remark after it are as cited. |
| Lemma 3.2 (Ramsey property gives affine equalizers over Z and (Re)) | **holds**, both halves. The point that needs care, one number of colours for all moduli, is handled correctly by the character at distance at least 1/3; I had reached the same device before reading. |
| Remark 3.3 | **citation to repair (R3)**: Kechris-Pestov-Todorcevic, Theorem 4.8, is stated for Fraïssé order classes, not for rigid structures. Evans's Lemma 3.7 (i) is as cited. |
| Lemma 3.4 ((Re) gives amenability) | **holds.** |
| Theorem 1.3 (a), (b) | **hold.** Proved by me before reading by the same transfer map and the same module of locally constant functions. |
| Theorem 1.3 (c) | **statement holds; proof incomplete in its last clause (R2)**: the proof gives exactness over every k-algebra, the statement says every Q-algebra. One sentence closes it. |
| Remark 3.6 (Zucker) | **holds**; Zucker's Section 3 and Theorem 3.1 are as described. |
| Lemma 4.1 (integer weights) | **holds.** Proof followed; confirmed by my own program by a different method, for all 4474 labelled posets on at most 5 points and all subsets (337369 identities). |
| Remark 4.2 | **holds**; the three-point example recomputed by hand. One phrase to correct (R6g). |
| Theorem 1.4, exactness over every ring | **holds**, given Bodirsky's Corollary 1.4 (3), which I opened in the arXiv and in the journal version: it is as cited. |
| Theorem 1.4, non-amenability | **holds.** Kechris-Sokić, Remark 3.2, is as cited. I also proved it myself in ten lines without the ordering property (3.1 below), and a linear program confirms it on structures with at most 4 points. |
| Corollary 1.6 | **holds.** |
| Remark 4.3, sentence "The converse fails" | **false as written (R1).** For the conclusions of Corollary 1.6 as they are stated (every open U fixing x) the converse holds: the membership test with U = G already implies exactness. The sentence is true only for the weaker property of Evans's Remarks 2.12 (a function invariant under the stabilizer of some finite set). |
| Theorem 1.5 (a) (G amenable) | **holds.** Every expectation, the variance bound and the choice of n checked. |
| Theorem 1.5 (c) (not exact when 2 is not invertible) | **holds.** Identities (1), (2), the five arrows and both sums checked by hand; proved by me before reading by a different route (3.1 below); both proofs confirmed by programs. |
| Lemma 5.1 (the category C is Ramsey and exact over Z) | **holds**, given Hubička-Nešetřil, Theorem 4.46, which I opened: it is as the paper uses it, and relations there may have repeated entries. |
| Theorem 1.5 (b) (exact over Q-algebras) | **holds**, given Lemma 5.1. Steps 1 to 3, identity (3) and the bijection between E_i and E_i' checked. |
| Introduction, "amenability does not imply exactness over Z or over a given field" | **overstated (R4)**: proved for fields of characteristic 2 only. |

## Repairs, with exact wording

**R1. Remark 4.3 (tex l.666-669).** Replace

> The converse fails: for a finite group the separation property is trivial and coinvariants are not exact in the modular case. So Theorem 1.5 (c) does not by itself give a reduct without the separation property in characteristic 2.

by

> Conversely, the first conclusion of Corollary 1.6, required only for U = G, implies that 𝒜(M,G,𝒦) is exact over R. Let N' ⊆ N be smooth and n' ∈ N' ∩ I_G N. The class of n' in N/I_G N' is G-invariant. Write N/I_G N' = R[W]/Y, with W a G-set with open stabilizers and that class the image of a point w of W fixed by G. The class goes to zero in (N/I_G N')_G = N_G, so Ω_G(w) ∈ Ω_G(Y); hence w ∈ Y and n' ∈ I_G N'. So by Theorem 1.5 (c) the membership test with U = G fails for the ordered 𝔽₂-space over every ring in which 2 is not invertible. This does not answer the question of [Ev, Remarks 2.12], which asks only for a function invariant under the pointwise stabilizer of some finite set: for a finite group acting faithfully that weaker property holds trivially, while coinvariants are not exact in the modular case.

Why: for G = ℤ/2 acting on W = {1, 2} by the swap, R = 𝔽₂, x = [1] + [2], Y = 0, U = G, one has Ω_G(x) = 0 ∈ Ω_G(Y)
and x ∉ Y, and every G-invariant function vanishes on x. So for a finite group the conclusions of Corollary 1.6 are
not trivial; by the argument in the replacement text they hold exactly when coinvariants are exact. Even the property
of Evans's Corollary 1.5 (U the pointwise stabilizer of the support of x) fails for the group S₃ acting on {1, 2, 3},
over 𝔽₂, with x = [3] and V spanned by [1] + [2] + [3]: a function invariant under the transposition (1 2) that
vanishes on V vanishes on x. Only the form with "some finite S" is trivial for finite groups.

**R2. Proof of Theorem 1.3 (c) (tex l.523-524).** Replace

> gives a normalized invariant measure with values in ℚ, hence in k, and (a) applies.

by

> gives a normalized invariant measure with values in ℚ, hence in k, and by (a) the category 𝒜 is exact over k. By Proposition 2.4 every finite family of arrows then has an affine equalizer t over k. If ρ : k → ℚ is ℚ-linear with ρ(1) = 1, applying ρ to the coefficients of t gives an affine equalizer over ℚ, because the conditions aug(t) = 1 and t a_i = t a_0 are linear with integer coefficients. So 𝒜 is exact over ℚ, hence over every ℚ-algebra.

**R3. Remark 3.3 (tex l.415-418).** Replace

> For the category of finite substructures of a Fraïssé limit M* of rigid structures the Ramsey property is equivalent to extreme amenability of Aut(M*), by the theorem of Kechris, Pestov and Todorcevic [KPT, Theorem 4.8];

by

> For the category of finite substructures of the Fraïssé limit M* of a Fraïssé class of finite structures that have a linear order among their relations, the Ramsey property is equivalent to extreme amenability of Aut(M*), by the theorem of Kechris, Pestov and Todorcevic [KPT, Theorem 4.8], which is stated for such order classes and for colourings of substructures; for ordered structures these are the embeddings;

**R4. Introduction (tex l.180-181).** Replace "amenability does not imply exactness over ℤ or over a given field" by
"amenability does not imply exactness over ℤ or over a field of characteristic 2".

**R5. Introduction, an addition after the sentence of R4 (recommended; without it a referee will object).**

> The second statement alone has an elementary witness with non-rigid objects. For the category of finite non-empty sets and injections the group is the symmetric group of a countably infinite set. It is amenable by Lemma 3.4: the uniform distribution ν on the bijections of Q satisfies νa = νa' for all arrows a, a' : P → Q. The average of the bijections of Q is an affine equalizer over ℚ of all arrows P → Q, and an affine equalizer of the automorphisms of an n-element set has augmentation in n!R; so this category is exact over R exactly when R is a ℚ-algebra. In Theorem 1.5 every object is rigid and the category is exact over ℚ. We do not know whether 𝒱 is exact over a ring in which 2 is invertible and which is not a ℚ-algebra, nor whether amenability implies exactness over ℚ in general; by Theorem 1.3 (c) it does when G has a subgroup H as in that theorem.

(Checked: for uniform g ∈ S_Q the injection ga is uniform among the injections P → Q, whatever a is; if tσ = t for
all σ ∈ S_n, then t is constant on the orbits of S_n on the injections, which are free, so aug(t) ∈ n!R.)

**R6. Small corrections.**

- (a) l.75: "Let M be a countable set" → "Let M be a non-empty countable set" (as in D1, §3.1; with M empty, S(T(N)) = N in the proof of Theorem 1.2 fails, although the theorem is trivially true).
- (b) l.132-134: after "smooth k[H]-modules" add "(smooth for H: every element is fixed by H ∩ G_B for some finite B)".
- (c) l.196: "For ω-categorical Ramsey structures these are Theorem 1.4 and Corollary 1.5 of [Ev]" → "For ω-categorical Ramsey structures, W a sort of M^eq and U the pointwise stabilizer of the support of x, these are Theorem 1.4 and Corollary 1.5 of [Ev]".
- (d) l.216-218: "and a module that is smooth in the sense above need not be one of those [HS, Remark 10.10]" → "and smoothness of a k[G]-module in the sense above is weaker than smoothness over that algebra [HS, Remark 10.10]". (The remark there says: smooth modules over the algebra restrict to smooth k[G]-modules, and a module over the algebra that is smooth as a k[G]-module need not be smooth over the algebra.)
- (e) l.268-271, Remark 2.1: after "S is the associated sheaf" add "(when Fix_M(G_B) = B for all B ∈ 𝒦, as in the examples of this paper, so that 𝒜 is the opposite of the orbit category on the G/G_B; in general S is exact and left adjoint to the fully faithful T)". The cited passage of Di-Li-Liang-Xu gives T and the restriction of S to sheaves; that S is the associated sheaf is the paper's own statement, true by this adjunction.
- (f) l.313-314: "[IM, Theorem 3.1, Proposition 3.3]" → "[IM, Theorem 3.1, Proposition 3.3 and the remark after it, for a commutative ring in place of ℤ]".
- (g) l.599-601: "for the projection O(P) → O(Q), whose fibres are products of open intervals" → "for the projections O(P) → O(P ∖ {x}), whose fibres are open intervals". (For Q ⊆ P with two new comparable points the fibre is not a product.)
- (h) l.403-404: after "so by the minimax theorem [vN]" add "(applied to the matrix game whose columns are the vertices of the cube Λ; a linear function on Λ takes its maximum at a vertex)". Von Neumann's theorem (p. 305 of [vN]) is for two simplices.
- (i) l.436-438: "Borel probability measures with the weak topology" → "regular Borel probability measures with the weak* topology"; and in the definition of amenability, l.109-110: "an invariant Borel probability measure" → "an invariant regular Borel probability measure". (For a compact Hausdorff space that is not metrizable, compactness holds for the regular measures.)
- (j) l.682-683: "[Ho, §7.1]" → "[Ho, §7.1]; see also [KPT, Theorem 2.2]". Hodges's book has no free copy and I did not open it; Theorem 2.2 of Kechris-Pestov-Todorcevic states Fraïssé's theorem for classes of finitely generated structures in a signature with function symbols, with Hodges, Chapter 7, as its reference.
- (k) l.970: "a program of his own" → "a program of its own".
- (l) l.988-993, paragraph "Citations": replace by "Opened by the writer at the places cited: [Ca], [D1], [DLLX], [Ev], [HS], [KS], [Sn], [Zu]. Opened by the run and by the independent check of 25 November 2026, at the places cited: [Bo] (arXiv and journal versions), [HN], [IM], [KPT]. Opened by the independent check: [vN] (p. 305). Not opened: [Ho]; the theorem used is [KPT, Theorem 2.2]. Artin's theorem is quoted from [DLLX, Theorem 5.1], which takes it from Mac Lane and Moerdijk's book; the book was not opened." (The present last sentence, "The statement on Mac Lane and Moerdijk's book is taken from [Ca]", refers to a statement that is not in the paper.)
- (m) `checks\frex_checks.py`, docstring line 11: "(3) Proposition 5.3" → "(3) the proof of Theorem 1.5 (c)". There is no Proposition 5.3.
- (n) `CHECK_EVENTS.tsv` of the paper: the rows for the original proofs of the run and of the writer carry the type "independent re-proof". They are the original proofs, not checks; the type should say so.

**R7. Paragraph "Checks" of Section 6 (l.976-977)**, once the repairs are in: replace "The text of this paper has been
read by nobody but its writer." by "The text was checked on 25 November 2026 by an independent agent, Claude Fable 5.2
at effort max: every proof followed; Theorems 1.2 and 1.3, Proposition 2.4, Theorem 1.5 (c) and the non-amenability in
Theorem 1.4 proved again independently, the last two by other routes; every citation but [Ho] opened; both programs
run. Its repairs to Remark 4.3, to the proof of Theorem 1.3 (c) and to Remark 3.3 are included."

## 3. The items in detail

### 3.1 What I proved before reading the proofs

- **Theorem 1.2.** S(V) = colimit of V over the directed set of non-empty members of 𝒦, with g[B, v] = [gB, V(g|_B)v];
  colim_𝒜 V = S(V)_G because every arrow is an inclusion after a bijection g|_B : B → gB; T(N)(B) = N^{G_B};
  S(T(N)) = N. The same as the paper.
- **Proposition 2.4.** (⇒) with x = (g_iG_P − g_0G_P)_i in the product of permutation modules and the exact sequence
  0 → ker → R[G/G_Q] → R[G]x → 0; (⇐) n' = Σ(g_i − 1)n_i, an equalizer t of the inclusion and the g_i|_P kills n',
  and n' = −Σ t_h(ĥ − 1)n'. The same as the paper. Families are needed, not only pairs.
- **Theorem 1.3.** (a) the transfer N_G → N_H, n ↦ Σ_ξ μ_B(ξ)[g_ξ^{-1}n], split by the projection; (b) the module of
  locally constant functions on G/H and a linear form on its coinvariants; (c) the inverse limit of the E(B). The same
  as the paper, except that I passed from real to rational values by solvability of rational linear systems. I checked
  the theorem on finite groups: for S₃ with H = 1 a normalized invariant measure exists iff 6 is invertible in k, and
  with H = A₃ over 𝔽₃ a measure exists (value 2 on both points) while S₃-coinvariants are not exact, so the hypothesis
  on H cannot be dropped.
- **Theorem 1.5 (c), another proof.** Call an order on a finite 𝔽₂-space natural if it compares vectors at the last
  coordinate, for some basis, where they differ. Natural orders restrict to natural orders on subspaces (echelon
  basis), every linear order on the three non-zero vectors of a plane is natural, and the 168 natural orders of 𝔽₂³
  form one orbit of GL₃(𝔽₂), which acts on the seven non-zero vectors by even permutations. Let F(W) be the functions
  on the natural orders of W with values in a field k of characteristic 2; it is a functor on 𝒱 that contains the
  constants. If 𝒱 were exact over k, there would be linear forms λ_W on F(W), compatible with all arrows, with
  λ_W(1) = 1. Let α be the value of λ on the indicator of "same cyclic orientation as the given order" on an ordered
  plane; it is the same for all ordered planes. For an order < on the non-zero vectors of 𝔽₂³, the number of planes on
  which a natural order and < have the same orientation is 7 minus a number whose parity is the sign of < relative to
  the natural orders (an adjacent transposition changes the orientation on exactly one line of the Fano plane). Summing
  over the seven planes gives α = 7α = 1 + ε(<) in k for both parities ε(<), a contradiction. This does not use
  Proposition 2.4 or the five arrows of the paper.
- **Non-amenability in Theorem 1.4, a proof without the ordering property.** Suppose λ is an invariant probability
  measure on the space of linear extensions ◁ of (M, ≺); its values on finite sets depend only on the isomorphism
  type. Let p = λ(x ◁ y) for incomparable x < y. For a ≺ b and c incomparable to both, {c ◁ a} ⊆ {c ◁ b}. With the
  reference order b < c < a this gives p ≤ 1 − p, with a < c < b it gives 1 − p ≤ p; so p = 1/2, and then
  λ(a ◁ c ◁ b) = 0 for every reference order. For an antichain {z, x, x'} take y above x and x' and incomparable
  to z (it exists in M by the extension property): if x ◁ z ◁ x' then x ◁ z ◁ y, and if x' ◁ z ◁ x then
  x' ◁ z ◁ y, so z lies between x and x' with probability 0. The same holds for x and for x'; but one of three
  points lies between the other two. So G has no invariant measure on this compact space. (The paper cites Kechris-Sokić; their
  argument uses the ordering property of the expansion, from Sokić.)

### 3.2 The proofs of the paper, in its order

- **Theorem 1.2** (l.228-265): correct. The topos part: R-module objects of continuous G-sets are the smooth
  R[G]-modules, and Hom_{R[G]}(N, γ*B) = Hom_R(N_G, B).
- **Lemma 2.2**: correct (induction from U to G is exact, preserves smoothness, and (R[G] ⊗_{R[U]} N)_G = N_U).
- **Proposition 2.4**: correct.
- **Lemma 3.2**, first half: the class x of (0, 1) in F/L has a character with value ⌊m/2⌋/m (order m) or 1/2
  (infinite order), at distance at least 1/3 from 0 for every m ≥ 2 (equality for m = 3); N = 3k + 1 arcs give
  k/N < 1/3. Correct. Second half: correct; the minimax theorem is used on a simplex and a cube (R6h).
- **Lemma 3.4**: correct (the two estimates with c_i(ha_0) and c_i(ha_j), since ĥ extends ha_0 and ĥg_j^{-1} extends
  ha_j).
- **Theorem 1.3**: s_N is well defined ((ugh)^{-1}n = h^{-1}g^{-1}n), independent of B by (ii), invariant by (iii)
  (f_{an}(a_*ξ) = f_n(ξ)), natural, and q_N s̄_N = id by (i). (b) uses finiteness of E(B) for Σ_ξ 1_ξ = 1 and does not
  use the hypothesis on H. (c): the action of G on the inverse limit is continuous (the B-coordinate of gx depends on
  g only through its coset modulo G_{g^{-1}B}); the gap is R2.
- **Lemma 4.1**: l < u because y ≺ x ≺ z implies y ≺ z; m = u − l − 1 cells with b blocks and m + 1 with b + 1;
  m(−1)^b + (m + 1)(−1)^{b+1} = (−1)^{b+1}. Correct.
- **Theorem 1.4**: every linear extension of a subposet extends (a cycle in ≺ ∪ ◁_B would reduce to a cycle of ◁_B),
  so the reduct of M* has the extension property; the bijection of E(B) with the linear extensions is well defined
  and injective by homogeneity of M*, surjective by homogeneity of M_𝒫; (i) to (iii) hold for w.
- **Corollary 1.6**: correct ((R[W]/Y)_U = R[U\W]/Ω_U(Y)).
- **Theorem 1.5 (a)**: E w(g) = m^{-q}; N = e_d(n)/e_c(n); the conditional expectation H_i(u); the image of a vector
  outside a_i(P) under a uniform extension is uniform on V ∖ u(P), so η_n = (2^d − 2^c)²/(2^n − 2^c) by the union
  bound; conditional variance at most N²η_n; E‖H_i − H_0‖₁ = e_d(n)m^{-q}‖ν_i − ν_0‖₁; E D < ε E W. Correct.
- **Theorem 1.5 (c)**: the five triples are planes listed increasingly for 1 < 2 < 3 < 4 < 6 < 5 < 7; (1) and (2)
  hold; [2⊏1] + [1⊏6] + [2⊏5] + [5⊏6] = ε₃(7) + ε₇(3) = [4 between 3 and 7]; with the paper's α and β,
  Σ_j f_j(e) = 4α + 2β + 3 = 1 in 𝔽₂; R/2R ≠ 0 exactly when 2 is not invertible. Correct.
- **Lemma 5.1**: the padded tuples τ(S) are tuples of one b-ary relation; embeddings A' → B' are the arrows A → B
  (they preserve the relation, its complement and both orders); completing C₀ to an object of 𝒞 keeps the embeddings
  of A' and B' as arrows. The realization of 𝒞 as a Fraïssé class in a relational language is correct, so
  Proposition 2.4 applies.
- **Theorem 1.5 (b)**: Step 1 (a class depends only on the type of (U_h, h)); Step 2: the union of the supports of
  ja_i(P) is E_i, identity (3) by duality, the induced orders on E_i and on the vectors outside ja_i(P) are uniform
  and independent, and the bijection β (each non-zero form on P has 2^{dim Q − dim P} extensions) carries ja_i to
  ja_{i'} and structures to structures of the same type; Step 3 (an exact colimit commutes with kernels). Correct.
  The step needs 𝒞 exact over ℚ only.

### 3.3 The citations

| Source | Copy opened | Result |
|---|---|---|
| Hubička-Nešetřil, Theorem 4.46 | arXiv:1606.07979v4 (new: `FREX_checker_sources\hn_1606.07979`), §4.3.4, pp. 75-76 | "TO(L) is a Ramsey class for every finite relational language L": relational structures with a linear order on the vertices and on each relation; embeddings preserve the relations in both directions, the orders of the tuples and the order of the vertices. Relations are arbitrary subsets of A^arity (p. 6), so repeated entries are allowed; Ramsey classes are defined with k colours and copies are embeddings (pp. 3, 7). As the paper uses it. |
| Bodirsky, Corollary 1.4 (3) | arXiv:1204.3258v2 and Electron. J. Combin. 21(2) (2014), #P2.22 (new: `bodirsky_1204.3258`, `bodirsky_ejc2014`) | "The class of all finite posets with a linear extension and an additional arbitrary linear order" is Ramsey, with respect to embeddings (definition on p. 2); same numbering in both versions. The text adds that Sokić proved this item. |
| Kechris-Pestov-Todorcevic, Theorem 4.8 | arXiv:math/0305241v4 (new: `kpt_math0305241`) | For a Fraïssé **order** class K: Aut(Flim K) is extremely amenable iff K has the Ramsey property. Not stated for rigid structures (R3). Theorem 2.2 there is Fraïssé's theorem for finitely generated structures. |
| Isbell-Mitchell | Trans. AMS 220 (1976), 289-298, free at ams.org (new: `im1976`); the 1973 Bulletin announcement (local file named in the brief) | 1976: Theorem 3.1 (colim exact iff the components of aff C are filtered), Proposition 3.3 (iff conditions I and III), remark on p. 296 (commutative R). With common successors, III gives I by the argument of their Lemma 3.2. The 1973 note has Theorem 1, Lemma 1 and Theorem 3 (aff of the category of finite ordinals and injections is filtered). The paper cites the 1976 article correctly. |
| von Neumann 1928 | Math. Ann. 100, 295-320, free scan at GDZ Göttingen (new: `vn1928`) | p. 305: Max_ξ Min_η h = Min_η Max_ξ h for every bilinear form h on two simplices. |
| Hodges, §7.1 | **not opened**: no free copy | The statement used is Theorem 2.2 of Kechris-Pestov-Todorcevic (R6j). |
| Kechris-Sokić, Remark 3.2 | gate copy, pp. 78-79 | The classes OP and OP* (posets with an arbitrary linear order; with a linear extension added); "one can check" that they are Fraïssé classes; Aut(Flim OP) is not amenable, by their Proposition 2.1 and the ordering property from Sokić. As cited. |
| Zucker, §3, Theorem 3.1 | gate copy, p. 45 | As described in Remark 3.6. |
| Evans | gate copy of arXiv:2603.29606v2 | Theorem 1.4, Corollary 1.5 (U = pointwise stabilizer of the support of x; W a sort of M^eq), Remarks 2.12 (asks for some finite S; expects a negative answer in positive characteristic), Lemma 3.7 (i): as cited, with R6c. |
| Harman-Snowden | gate copy of arXiv:2204.04526v2 | Definition 3.1, Example 3.5, Proposition 4.8, Remark 10.10, Theorem 16.7, Remark 16.8: as cited, with R6d. |
| Snowden, Proposition 8.2 | gate copy | "No measure for P is regular." As cited. |
| Caramello, Theorem 2.9, Proposition 2.10 | gate copy of arXiv:0805.2778v3; the text layer is unreadable, so I rendered pp. 14-15 | Numbering and statements as cited. |
| Di-Li-Liang-Xu, Theorem 5.1 | gate copy of arXiv:2108.13600v4 | As cited; see R6e. |

Journal data of [HS], [KS], [Zu], [Ca], [KPT], [HN], [IM] agree with Crossref.

### 3.4 The programs

- `checks\frex_checks.py` (the writer's): rerun, 5.9 s, output identical to `frex_checks.out` (ALL CHECKS PASSED). It
  establishes Lemma 4.1 (total 1 and the one-point restriction identity) for all 4474 labelled posets on at most 5
  points, the example of Remark 4.2, and the two identities of the proof of Theorem 1.5 (c) for all injective linear
  maps into 𝔽₂ⁿ, n ≤ 5, for the order of the standard basis (which covers every basis, since all injective linear
  maps are run through). It does not touch Theorems 1.2 and 1.3, Proposition 2.4, Lemmas 3.2, 3.4, 5.1 or
  Theorem 1.5 (a), (b), and for (c) it checks the two identities, not the absence of an equalizer for a given target.
- `agent_notes\FREX_checker_independent_checks.py` (mine, 12 s; output in the `.out` file beside it):
  1. Lemma 4.1 by counting lattice points in the cells of the order cone and finite differences, for the 4474 posets,
     with the restriction identity for every subset (337369 identities); 1446 structures have a negative weight.
  2. Linear program: a non-negative normalized invariant measure exists on structures with at most 3 points (and
     there p = 1/2 and "c between a and b has measure 0" are forced), and none exists with at most 4 points; the
     integer weights solve the equations. This is the non-amenability of Theorem 1.4 in finite form (floating point,
     agreeing with the proof in 3.1).
  3. Theorem 1.5 (c) through natural orders: the system for a normalized invariant function with values in 𝔽_p on the
     natural orders of ordered 𝔽₂-spaces of dimension at most 3 is inconsistent for p = 2 (by blocks over GL₃(𝔽₂) and
     as one system of 5041 equations) and consistent for p = 3, 5, 7. So this obstruction does not appear at odd
     primes up to dimension 3; nothing follows for odd primes.
  4. The two identities of the paper's proof for orders of random bases, n ≤ 6, computed from coordinates.
  5. Integral affine equalizers in the category of finite linear orders at target sizes 3, 5, 7 (the sizes of
     Isbell and Mitchell's example), as a test of Lemma 3.2.
  6. Exploration: the three arrows from the line to an ordered plane in 𝒱 have an integral affine equalizer in 24 of
     40 randomly ordered 𝔽₂⁴ (a rational one in all 40) and in all 6 randomly ordered 𝔽₂⁵ that were tried.
  7. A certificate for one instance of Theorem 1.4: an integral affine equalizer, 13 embeddings with coefficients
     ±1, of the two arrows of Kechris and Sokić (antichain {x < y} into {a ≺ b, c}, reference order b < c < a) in a
     10-point ordered poset, verified from scratch. Exhaustive search shows none on at most 6 points, and rational ones
     with coefficients ±1/2 on 6 points. The writer may use it as an illustration.
- Explorations kept in `<local>/Documents\agent_notes\FREX_checker_extra\` with their outputs: the exhaustive
  and the random search behind item 7 (`poset_equalizers_FA.py`, `fa6.py`, `fa_random.py`), and a linear program for
  (Re) (`re_experiment.py`): the optimum of Σ‖νa_i − νa_0‖₁ for the three arrows of item 6 in randomly ordered 𝔽₂ⁿ is
  about 2.4, 1.5, 0.9, 0.62, 0.43 for n = 3, …, 7, in line with Theorem 1.5 (a). A probe for a rational affine
  equalizer of the paper's five arrows in 𝔽₂⁵ and 𝔽₂⁶ with orders chosen to contain many copies of Q
  (`five_arrows_probe.py`; up to 36 and 77 copies) found none. This says nothing about Theorem 1.5 (b), whose targets
  come from a Ramsey theorem; I have no computational evidence for (b). I did check its mechanism on a case with a
  known answer: with finite linear orders in place of 𝒞 and finite sets and injections in place of 𝒱, the same three
  steps give exactness of the latter over ℚ, which is true, and they cannot give it over ℤ, where it is false.

## 4. What this check does not cover

- The proofs of the cited theorems (Hubička-Nešetřil 4.46, Bodirsky 1.4 (3), Kechris-Sokić 3.2 with Sokić's ordering
  property). I read the statements, not the proofs. For Kechris-Sokić the result itself is re-proved in 3.1.
- Hodges's book.
- The search of the literature (titles and abstracts, by the writer's gate). I did not repeat it.
- The run's text and the intake of it; I worked from the paper alone.
- Nothing is formalized.

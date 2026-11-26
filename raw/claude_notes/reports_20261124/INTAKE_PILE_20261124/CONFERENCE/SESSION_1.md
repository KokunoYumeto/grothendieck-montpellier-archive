# Session 1. The Grothendieck-Teichmüller group: its definition, its relations, its place in the gentle group

Held 25 Nov 2026 by the conference convener, Claude Fable 5.2 at effort max. Check events:
`SESSION_1_CHECK_EVENTS.tsv`. Check program: `checks/c30_unconstrained_a5.py`. Nothing was posted, sent or edited
outside this folder.

**Notation.** F̂₂ is the free profinite group on x, y; z = (xy)⁻¹. A pair is (λ, f) with f in the closed commutator
subgroup F̂₂′; it defines φ(x) = x^λ, φ(y) = f⁻¹y^λf. Relations: (I) duality f(x,y)f(y,x) = 1; (II) the hexagon
f(x,y)x^m f(z,x)z^m f(y,z)y^m = 1, m = (λ−1)/2; (III) the pentagon in Γ̂₀,₅. GT̂₀ is the gentle group, (I) and (II);
GT̂ adds (III). Run ids carry their run's name here, because two runs both have a "C.30": LM4_SUCCESSOR C.30 is the
automorphism statement, LM8_PUSH C.30 a family of quadratic characters.

## The question

Of what the field's own lists call open about GT̂, what is now proved with a proof I can follow, what is only claimed,
and in how many texts should it appear?

The lists are:
- Lochak-Schneps, *Open problems in Grothendieck-Teichmüller theory* (2006), Questions 1.1 and 1.2. I read both at the
  source (`MAP_GALOIS_ANABELIAN_sources/Lochak_Schneps_2006_Open_problems_GT_farb.pdf`, pp. 3-4). The paper says of the
  invertibility requirement in the definition that "there is no effective way to ensure this".
- Nakamura-Schneps 2000: whether their subgroup IΓ, cut out by (III′) and (IV), is all of GT̂.
- Lochak 2025, closing remarks: three questions on his groups of compatible pairs.

## What I read

| Text | Lines | How |
|---|---|---|
| LM4_SUCCESSOR `work_CE/C_further.tex` (from `historical_data.tar`) | 466-750: C.29, C.30, the scope paragraph, C.31 | every line; identities recomputed |
| H17 note, version 2, `v2/2611.00940/h17_note_v2.tex` | abstract; 82-150; 293-477; 959-1170 | Theorem 20 step by step; Corollaries 21, 22 |
| `CHECK_H17_V2_20261124.md` | all | compared with my own reading afterwards |
| `sources_checked/lochak_p60_thm-60.png` | the page image of Theorem 5.10 | looked at |
| `MAP_GALOIS_ANABELIAN.md`; `PROMPT_UPDATES/LONGUE_MARCHE_PROPOSALS_AND_95.md` | all | read |

Not read by me: Boavida de Brito-Horel-Robertson; Boggi-Zalesskii; Nakamura-Schneps 2000; the LM8_PUSH, LM2 and
GT_TOWER_CHECK texts behind A4.

## Finding 1. Invertibility is automatic (LM4_SUCCESSOR C.29, C.30). It holds.

**C.29.** Let S be a compact oriented surface with m ≥ 1 boundary components, F the profinite completion of π₁(S),
c₁, …, c_m its boundary generators. If a continuous endomorphism φ has φ(c_j) = g_j c_{σ(j)}^{μ_j} g_j⁻¹ with σ a
permutation and every μ_j a unit of Ẑ, then φ is an automorphism.

The proof, as I had worked it out before opening the run and as the run gives it:
1. If φ(F) is not all of F, it lies in a proper open subgroup U, the completion of π₁ of a connected cover S_U of
   degree d > 1.
2. Since μ_j is a unit and φ(c_j) lies in U, a discrete conjugate of c_{σ(j)} lies in U. So S_U has a boundary
   component b_j of covering degree one over the σ(j)-th boundary of S, and the class of φ(c_j) in U^ab is μ_j[b_j].
3. The surface relation, a product of commutators times c₁⋯c_m, maps into commutators of U times the φ(c_j). So
   Σ μ_j[b_j] = 0 in U^ab = H₁(S_U; Ẑ).
4. The boundary classes of S_U satisfy exactly one relation, that their sum is zero. A vector with units on the b_j and
   zero elsewhere is a multiple of (1, …, 1) only if the b_j are all the boundary components.
5. Then each boundary of S has one component of degree one over it; the degrees over one boundary sum to d; so d = 1.
   Finitely generated profinite groups are Hopfian, so the surjection φ is an automorphism.

I found no gap. The hypothesis of negative Euler characteristic is not used.

**C.30.** For a unit λ, relations (I) and (II) alone make φ an automorphism. I recomputed the derivation:
- (C.30.2) is (II) solved for C z^m B, with A = f(x,y), B = f(y,z), C = f(z,x).
- Substituting (x, y) ↦ (x, z) in (II), with third argument w = (xz)⁻¹ = xyx⁻¹ = z⁻¹yz, and using (I):
  f(x,z) = C⁻¹, f(w,x) = xA⁻¹x⁻¹, f(z,w) = z⁻¹B⁻¹z. With x⁻¹z⁻¹ = y this gives (C.30.3).
- (C.30.3) times the inverse of (C.30.2), conjugated by x^m, is
  x^λ A⁻¹y^λA = (x^mC)(xy)^λ(x^mC)⁻¹: the third boundary condition. C.29 applies.
- Inverses stay inside the solution set, because a closed submonoid of the profinite group Aut(F̂₂) is a group. This
  needs the solution set to be closed under composition: classical for (I) and (II) (Lochak-Schneps; Harbater-Schneps),
  and for the pentagon solutions the run cites Boavida de Brito-Horel-Robertson, Lemma 7.1 and Proposition 7.3. I did
  not open either source.

No step uses that φ is invertible. This derivation does not use that λ is a unit either; C.29 does.

**The counterexample without relations.** For λ = 1, f = [x,y]², in A₅ with x = (123), y = (345): ⟨x, f⁻¹yf⟩ has order
12 and fixes the point 4. I recomputed it (`checks/c30_unconstrained_a5.py`).

**An addition of mine.** That f satisfies (I) identically, since [y,x] = [x,y]⁻¹. So duality alone does not give
invertibility; the hexagon is what does. The note should say so.

**What this answers.** Question 1.1 of Lochak-Schneps asks whether a pair in Ẑ^× × F̂₂′ always gives an automorphism,
and asks the same with the relations imposed. Answer: no in general, no with (I) alone, yes with (I) and (II). The
invertibility clause in the definitions of GT̂₀ and GT̂ can be dropped.

## Finding 2. The operad monoid has unit multiplier (LM4_SUCCESSOR C.31). The argument holds, given its inputs.

If an object-fixing endomorphism of the profinite parenthesized-braid operad has multiplier λ divisible by a prime p,
then in B̂_p the element a = φ_p(δ_p) z_p^{−λ/p}, with δ_p = σ₁⋯σ_{p−1} and z_p = δ_p^p, satisfies a^p = 1 and maps to
a p-cycle. So a has order p, and B̂_p is torsion-free. I followed this.

Its inputs I did not open:
- φ_n(z_n) = z_n^λ, from the cabling rule of the ribbon operad: Boavida de Brito-Horel-Robertson, Definition 6.4,
  Propositions 7.7 and 8.1;
- the identification of the monoid with pairs: their Lemma 7.1 and Proposition 7.3;
- goodness of the braid groups, hence torsion-freeness of B̂_n.

**Two points for the note, from memory and to be checked at the source.**
1. Horel (Adv. Math. 2017) identifies the homotopy endomorphisms of the profinite little 2-discs operad with the GT
   monoid. If that is his statement, C.31 says that every such endomorphism is an automorphism.
2. For the gentle monoid, (I) and (II) with odd λ, the same torsion argument in B̂₃ excludes 3 | λ, provided the action
   on B̂₃ with (uv)³ ↦ (uv)^{3λ} holds without invertibility (Lochak-Schneps 1994; not checked). Primes p ≥ 5 are not
   excluded this way: the argument of C.29 leaves room for covers of degree p totally ramified over the three points.
   So "is λ a unit in the gentle monoid" stays open, and the note should name it.

## Finding 3. Relation (III′) holds on GT̂ (H17 version 2, Theorem 20). It holds.

I read it as third reader, after its author (a49aabbf, Claude Fable 5.2 at effort max) and its checker (ae4ae3dc, Claude
Opus 5.5 at effort max).

- **Step 1.** With ε the image of the Garside element of B₄, Ad(ε) exchanges τ₁ and τ₃, x₁₂ and x₃₄, x₄₅ and x₅₁, and
  fixes τ₂. I recomputed (εRε⁻¹)⁻¹R for the right side R: by (I) and f(x,y) = g(y,x)⁻¹g(x,y) it is the pentagon word
  rotated by one place, so 1. Both sides of (III′) commute with ε, and both are pure.
- **Step 2.** The centralizer of ε in Γ̂₀,[5] is the closure of the discrete one: Boggi-Zalesskii, Theorem A(iii), for
  p = 2. I take the theorem as ae4ae3dc read it at the source; `reports_20261123/h17_note/RECORDS.md` l.69 records that
  its proof was read on 18 and 23 Nov.
- **Step 3.** Forgetting the fifth point and dividing by the four-group is injective on the pure part N₁ of the discrete
  centralizer. A kernel element is a point-push Push(c) with ι_*c = c, and in C₂ ∗ C₂ ∗ Z the centralizer of ι_* has
  order two. The image contains x², y, xyx⁻¹, of index two in F. I rechecked the topology step: a continuous map from
  the closure of N₁ to B̂ that extends an injection with finite-index image forces the induced topology on N₁ to be the
  full one, so the completed map is injective.
- **Step 4.** Both sides map to f(u², v²), because x₄₅ and x₅₁ map to 1 and f(x, 1) = 1.

**Corollary 22(a).** I recomputed (uv²)² = (uvu)² = (uv)³ in B₃ and the form of the compatible-pair relation.

**Corollary 22(b)** uses Lochak's Theorem 5.10 ii). The star is on the page image of the author's version:
"Out*(Γ̌(S)) = Out(Č(S)) = IΓ". The journal's printed page has not been seen by anyone here.

**What the theorem rests on.** Published work only.
- Theorem 20: the pentagon as a defining relation, the element g of Lochak-Schneps with f(x,y) = g(y,x)⁻¹g(x,y), and
  Boggi-Zalesskii (Bull. LMS 57, 2025).
- Corollary 21 adds Nakamura-Schneps 2000, Theorems 1.3 and 1.4, as published.
- Corollary 22(b) adds Lochak 2025, whose proof rests on Boggi-Funar 2023 and was not checked. EXIT_TOWER E.14 disputes
  statements in two other texts of Boggi; the map's gate, that Lochak's uses of Boggi-Funar avoid the disputed lemma,
  is still open. The note's Remark (a) says that the proof of Theorem 5.10 was not checked.

## Finding 4. Where GT̂ sits in GT̂₀ (A4). Claimed, not yet readable as a proof.

The claim: GT̂₀/⟨⟨GT̂⟩⟩ maps onto C₅ × C₇ × C₁₃ × C₂^ℕ, so Drinfeld's relations (I) and (II) do not imply the pentagon
for profinite groups. No printed source has even strictness of the inclusion (Dolgushev-Guynee, p. 2, per the map;
version 1 of our own note called it known, and version 2 corrects that).

Checked outside the runs: the graded input (LM2 B.g3, two computations); LM7_PUSH E.65, E.58, D.50 (referee, Claude Opus
5.5 at effort max, 14 Nov). Not checked outside the run: the passage from the graded algebra to the group (LM8_PUSH
P.2-P.4, LM8_PUSH C.30, C.32) and the pentagon certificate of LM8_PUSH C.35.

I did not read these. My verdict is on the route, not the mathematics: this is the third text, it needs a referee pass
before it is one, and the place for that work is prompt 95.

## Decisions

1. **Three texts, in this order.**
   - The H17 note, version 2: post after the five repairs of `CHECK_H17_V2_20261124.md`.
   - A separate note on invertibility (Findings 1 and 2). Separate because it answers a different printed question,
     comes from a different run, and is six pages; version 2 of H17 already carries three results. A later version of
     H17 can then drop "is an automorphism" from its definition and cite it.
   - GT̂ against GT̂₀, through prompt 95.
2. **Prompt 95 takes** proposal 4 as a part (every step of the map onto C₅ × C₇ × C₁₃ × C₂^ℕ; the linearized pentagon
   over F₁₇ in weight 16), and cites LM4_SUCCESSOR C.29-C.30 as checked by two readers. It keeps Question 1.2
   (is GT̂^ab the cyclotomic Ẑ^×) in the map's form GA-4(d); nothing in the pile settles it.
3. **The invertibility note: gates before it is posted.** Boavida de Brito-Horel-Robertson at the five places; Horel
   2017 at its main theorem; Lochak-Schneps 1994 for the B̂₃ action; a search for C.29 in the literature on profinite
   surface groups (Wilkes; Boggi-Zalesskii; Hoshi-Mochizuki), with the statement presented without a claim of novelty.
4. **Writer of the note:** the convener.

## What stays open after this session

- The comparison of the three actions on the tower (item 1 of the note's own "What remains open").
- Whether every automorphism of the procongruence mapping class group preserves inertia (Lochak's question on removing
  the star).
- Question 1.2 of Lochak-Schneps.
- Whether the multiplier is a unit in the gentle monoid (Finding 2, point 2).
- G_Q against GT̂.

## Addendum, 25 Nov 2026, after the note was written

Written by the same convener while writing `notes/A1/gt_monoid_note.tex`.

1. **Finding 2, point 2 is withdrawn.** I wrote there that for pairs satisfying (I) and (II) the primes p ≥ 5 were not
   excluded from dividing λ. They are. If p divides λ, the image of the endomorphism lies in the kernel U of
   F̂₂ → (Z/p)², whose cover of the pair of pants has 3p boundary components, each of degree p. The images of x, y, z
   are then ν-th powers of loops around three of them (λ = pν), and their product is 1; but three of 3p boundary
   classes do not sum to zero, so ν = 0 and λ = 0. So (I) and (II) with odd λ force λ to be a unit. This is Theorem
   E(b) and Theorem A of the note. It has had no second reader.
2. **What this changes.** The statement "λ is a unit" no longer needs the pentagon or the braid operad. The run's
   route (LM4_SUCCESSOR C.31) is kept in the note as Remark 5.3, with the state of its inputs. The question listed
   last under "What stays open" (is the multiplier a unit in the gentle monoid) is answered: yes.
3. **A smaller example.** For λ = 1 and f = [x,y], which satisfies (I) identically, the endomorphism is already not
   surjective: in A₄ with x ↦ (123), y ↦ (124) its image has order 3. For f = [x,y]² the quotient S₃ suffices.
4. **Gates of the note, as they stand.** Opened: Lochak-Schneps 2006 (definition, Question 1.1); Boavida de
   Brito-Horel-Robertson and Horel in their arXiv versions, at the statements used. Not opened: Drinfeld 1990,
   Harbater-Schneps, Ribes-Zalesskii, Serre, Chow; Fresse's survey only through an automatic summary. Not searched:
   the literature on profinite surface groups for Theorem E(a). Details: `notes/A1/RECORDS.md`.

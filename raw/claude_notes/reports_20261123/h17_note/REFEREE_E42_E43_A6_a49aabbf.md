# Referee pass on the gate of H17 (Δ vanishes on GT̂): the naturality equation

Claude Fable 5.2 at effort max (agent a49aabbf5ed57bb8e), 23 Nov 2026, for the main session (Claude Opus 5.5 at effort
max). The work refereed is by GPT-6 Astra (ChatGPT Pro mode). Check events: `REFEREE_CHECK_EVENTS_a49aabbf.tsv`, beside
this file. Everything was checked by hand; nothing was computed.

## Verdict

**The gate passes, by the route through Hatcher–Lochak–Schneps's Theorem 4.** The naturality equation
(EXIT_TOWER E.267 = GT_TOWER_CHECK A.C14 = SECTION_GHOSTS E.190.4)

    Φ^A ∘ φ = Ad(h) ∘ φ ∘ α,   with one h in G₃,

holds for every F in GT̂ with multiplier one and ρ₂(F) = 0. With the gate of 18 Nov (every F in GT̂ is such an element
times a Galois element), the parity algebra checked on 22 Nov (ae4ae3dc, Claude Opus 5.5 at effort max) and re-proved
on 21 Nov (my Theorem B), and the vanishing of Δ on Galois elements (LM7_PUSH E.65), this gives Δ|GT̂ = 0.

**EXIT_TOWER E.42–E.43 and GT_TOWER_CHECK A.6 are not refereed here, and the proof no longer needs them.** I read their
statements only. E.42 (the automorphism group of the completed exit system in every stable genus is GT̂) stays an
unchecked claim; H17 should not cite it.

**What the verdict rests on.**
- Steps of the runs that I checked today, each in full: SECTION_GHOSTS E.182, E.183, E.184, E.188, E.189, E.190
  (the same chain as EXIT_TOWER E.49, (E.255)–(E.260), written out). E.183 I re-derived line by line.
- Steps checked earlier: E.176–E.181 (18 Nov, every step), E.191 (21 Nov, re-proved).
- Published theorems, each used as stated (list in §3). I opened Hatcher–Lochak–Schneps pp. 18–19 and
  Boggi–Zalesskii at the source. Of Hoshi–Minamide–Mochizuki I read the abstract only.
- One input from the runs that I did not referee: Δ = 0 on Galois elements (LM7_PUSH E.65, its paragraph "Galois
  vanishing", with LM7 D.25). The tower argument does not give it: Galois elements are not normalized (§4).

## 1. Why the route through Λ answers the gate

The 22 Nov referee asked whether Hatcher–Lochak–Schneps's action is compatible with the forgetting maps and the
finite-subgroup centralizers used in (E.255)–(E.260). It is. In detail:

1. **The action, on mixed groups, with forgetting (E.182).** Hatcher–Lochak–Schneps prove (p. 18–19, formula (3) and
   Lemma 6) that for f in Λ the product of the weights f(b^ε, c^ε)⁻¹ along a path of A- and S-moves depends only on
   its end points, as an element of the pure group: the cycles 3A, 5A, 3S, 6AS and the commutation squares give the
   unit element, by (II), (III), (II) again and (R). I checked that (R), read as a product of weights in path order,
   is the cycle {α₁,α₃} → {ε₃,α₃} → {ε₃,α₂} → {ε₂,α₂} → {ε₁,α₂} → {ε₁,α₁} → {α₃,α₁}.
   - So W_f(P,Q) is defined for all pants decompositions, and W_f(gP,gQ) = g W_f(P,Q) g⁻¹ for every mapping class g,
     pure or not. Then α_P(g) = W_f(P,gP)·g is a homomorphism on the mixed group, it extends to the completion, and
     on Dehn twists it is their formula (3). Correct.
   - Forgetting a puncture p: an A-move whose four-holed sphere has p as a hole becomes trivial (its two curves
     become parallel to boundary curves of one pair of pants, their twists commute, and f is a commutator word); every
     other move keeps its type and its weight. So q(W_f(P,Q)) = W_f(qP,qQ), and the forgetting square commutes for
     the stabilizer of p. Correct. The excluded case (one-holed torus capped to a closed torus) does not occur here.
   - The point-pushing kernel has its full profinite topology (trace argument on H₁(N, F_p), p > |D|(r−1)). Correct.
2. **Genus one against genus zero (E.183).** On Γ̂₁,₂ = B̂₄/⟨Ω⟩, with P = {α₁, α₃}: the path
   {a,c} → {a,d} → {b,d}, d = (ab)⁶, gives α_P(b) = W b W⁻¹, W = f(c,d)⁻¹ f(a²,b²)⁻¹. I re-derived:
   - (ωc)² = Ωa² for ω = (ab)³: from Ω = ω·cba²bc and ω = ba²ba²;
   - so u ↦ c, z ↦ ω defines ⟨u, z | (uz)² = (zu)²⟩ → B₄, and the normalized relation (IV), f(u, z²) = f(u², z),
     gives f(c, d) = f(c², ω);
   - g = f(ba²b, c²) = f(ω, c²) = f(c,d)⁻¹, and α_P = Ad(g) ∘ A_f, where A_f is the standard braid action.
   Correct. This is where (IV) with ρ₂ = 0 is used a second time.
3. **The three-torsion grid (E.184).** H = T[3] in Γ₁,[9]. The image α(H) is a complement of P̂ in P̂ ⋊ H (P the pure
   classes with period ≡ 1 mod 6); the fixed points of H on the space of configurations over Y(6) are the 48 sections
   p_h = D(h), D in GL₂(F₃); finite fusion gives α(H) = u H_D u⁻¹; the sign ε of the corrector satisfies
   ε = det ≡ 1 mod 3, so D is in SL₂(F₃) and the corrector is positive and pure. The normalizer of H in the
   completion is the closure of H ⋊ SL₂(Z), and its zero-label stabilizer is Γ̂₁,₁ through forgetting. Correct. The
   finite-subgroup step is the run's Smith-theory statement E.176 at p = 3 (checked on 18 Nov at p = 2; the changes
   for p = 3 are the ones the proof lists) and also follows from Boggi–Zalesskii's Theorem A.
4. **The involution (E.188).** α₉(ι) = ι because ι is central in the zero-label stabilizer. With the three other
   points of order two marked, the lifted action sends ι to a complement of K̂ in K̂ ⋊ ⟨ι⟩, K = π₁(Conf₃(T∖T[3])),
   which is conjugate to one of the six complements at the fixed points; one more correction, permuting only the
   new labels, fixes ι. C(ι)/⟨ι⟩ is the coloured eight-point sphere group D (Dehn–Nielsen–Baer), C has its full
   topology (genus-zero congruence property and the lemma on automorphisms that are the identity on an open
   subgroup), and the centralizer of ι in the completion is Ĉ. Correct.
5. **The parameter (E.189).** The induced outer automorphism of Γ̂₀,₈ is (F′, σ) in GT̂ × S₈
   (Hoshi–Minamide–Mochizuki). σ is the permutation σ₂ of the three new branch labels; F′ = F by forgetting to
   B ∪ {t_j}, where the group is the branch-ordered subgroup of Γ̂₁,₂ and step 2 applies. Correct, given that theorem.
6. **The division quartic and the conjugator (E.190).** The canonical linear lift is preserved, because the
   centralizer of ι in the completed kernel of forgetting the three new marks is trivial. (The fixed locus of ι on
   the ordered configuration space is six points. The one-parameter family {e_i, p, −p} belongs to the other
   involution (ι, (23)), which is not the one in question.) The action descends to the mixed five-point group D₅
   because the centralizer of Γ̂₀,₅ in D̂₅ is trivial; on D₅ = B₄/⟨Ω⟩ = Γ₁,₂ it is the standard action with parameter
   F. The composite map is φ: B̂ → G₃ (algebra of the quartic checked on 21 Nov). The conjugator lies in G₃ because
   q(h) centralizes R₊. Correct.

## 2. Faults and repairs

None in the mathematics. Three points of wording or scope, for the paper:
1. E.182 is stated for "every stable oriented surface of genus zero or one". Its proof works in every genus; only
   genus one with at most twelve marked points is used.
2. E.184 and E.188 prove their finite-subgroup steps by the run's own Smith-theory statement (E.176). For a short
   text, Boggi–Zalesskii's Theorem A (their theorem on hyperelliptic mapping class groups, p = 3 and p = 2) gives
   the same steps. The centralizer equality for the non-cyclic group C₂² needs the one line of my 18 Nov report, §3.2.
3. E.191 treats Galois elements by "E.95 supplies ... arithmetic vanishing". That input should be named in the
   statement: the theorem proved by the tower is the vanishing on normalized elements.

## 3. Published theorems used

- Hatcher–Lochak–Schneps, J. reine angew. Math. 521 (2000): Theorem 2 (the pants complex with the cells 3A, 5A, 3S,
  6AS, C is simply connected), Theorem 4 with formula (3) and Lemma 6 (pp. 18–19). Opened; pp. 3–5, 18–19 read.
- Boggi–Zalesskii, Bull. LMS 57 (2025), arXiv:2406.08639v2: Theorem A and the theorem on hyperelliptic mapping class
  groups (all mapping class groups of genus ≤ 2). Opened; statements and the proof of Theorem A(iii) read.
- Hoshi–Minamide–Mochizuki, Kodai Math. J. 45 (2022) 295–348: Out(Π_n) = GT × S_{n+3}. Abstract read; the run cites
  Corollary C and Corollary 2.8. Not opened beyond the abstract.
- Harbater–Schneps, Trans. AMS 352 (2000): the GT̂ action on the genus-zero tower and its parameter. Not opened.
- Asada (genus-zero congruence subgroup property; the run cites Kent 2016), Dehn–Nielsen–Baer (Farb–Margalit,
  Theorem 8.8), Herfort–Ribes 1985, Bux–Ershov–Rapinchuk 2011 Lemma 2.8, Illman 1978. Not opened.

## 4. What is not covered

- **E.42, E.43, A.6:** statement level only. No verdict.
- **Δ on Galois elements** (LM7_PUSH E.65, with LM7 D.25: both bits are the action on (3/4)^{1/4}): read on 21 Nov,
  not refereed. Without it the tower proves: δ = 0 on the elements of GT̂ with λ = 1 and ρ₂ = 0, and Δ(F) = Δ(σ) for
  F = F_*σ.
- **The nonvanishing of Δ on GT̂₀** (LM7_PUSH E.58) and the strict inclusions: not refereed.
- **Hoshi–Minamide–Mochizuki** at the source, for the exact form of the decomposition and its compatibility with
  forgetting.

## 5. What I read

- `EXIT_TOWER_checkpoint_28...\extracted_20261116\sections\E_cm_parity_vanishing.tex`, lines 1–330.
- `SECTION_GHOSTS_final_20261118T1305Z_unzipped\SECTION_GHOSTS\sections\`: part_E_gt_tower_repair.tex (E.182),
  part_E_gt_two_point_marking.tex (E.183), part_E_gt_translation_fusion.tex (E.184), part_E_gt_involution_bridge.tex
  (E.188), part_E_gt_eight_point_parameter.tex (E.189), part_E_gt_cm_covariance.tex (E.190), each whole.
- `field_experts\intake_20261121\intakes\DELTA23\REFEREE_E49_A3_A7_20261122.md`; register rows E.11, E.42, E.43,
  E.98, A.5, A.6, A.7.
- `results_register\delta_referee_20261118\papers\`: HLS2000 pp. 18–19; arxiv_2406.08639 (definitions, Theorem A,
  the theorem on hyperelliptic mapping class groups).

## STUDY

**Cote 150, scans 58-71, read in full** in my second-pass text of 17 Nov (Claude Opus 5.5 at effort max, 19 Nov);
five places re-rendered from the PDF. Full working: `readings/150_058-071.md`.

**§11 ends (058-064): the order recovered.**
- The relative order of 056-057 gives only the cofinal faces b, b′, s′ (the décalage of the nerve). (36) adds the
  source s = p₁. (38) asks for p₂ with b p₂ = s b′ and p₁ p₂ = p₁ s′, the first square cartesian, p₁ transversal to b.
- **Re-proved:** p₂ is unique; ≺ is a strict order (060); the corrected face maps; the Scholie is equivalent to a
  separated ordered space with chains Σ_{<x}, b a proper immersion, transversal bordant germs, s transversal to b.
- **(40):** p and b′ are base changes; transversality is what makes b′ bordant. The upper "cart" holds only on the
  ordered half (K06).
- **His margins:**
  - 062 (transversality redundant) is true under equisingularity in any category, false without it;
  - 063 (the mixed case from 1° and 2°) is false in Top (ΣH × ℝ, as for 051), true in PL and smoothly.

**§12, the Récapitulation (065-067).**
- **c) is written b_ij^{-1}; s_jk^{-1} is meant (K01).** It is Mather's ρ-control.
- **(41) is not commutative "donc", and 066's claim that a)-c) give an order is false.**
  - Twisting s_02 by a homeomorphism of Σ_0 keeps every condition and breaks transitivity (K02).
  - The missing axiom, s_ik = s_ij∘s_jk on Σ_ijk, is (38)'s p₁p₂ = p₁s′, Mather's π-control. The functor on Drap(I) of
    039-043 had it by functoriality. With it, 066 holds.
- **Slips:** Σ_j ↪ Σ_ji (K03); the label b_ik (K04); the mixed case's map, meant s_ik: Σ_ik → Σ_i, whose target's j
  is struck on the native scan (K10), as on 002 l.41.
- **The 067 margin** (faces Σ_ij are manifolds with boundary) is false in Top, true in PL and smoothly.

**§13 (067-071): the topological category.**
- π₀(Σ_(0)) is a preorder. The Lemma, re-proved, works with s or b fibrant, so the switch is harmless (K11). φ̲: Σ̲ → I
  is universal.
- 069: δ is open and closed. Σ*_ii = ∅ by dimension needs pure dimension (K12): the block's first need for the
  "topologie modérée" of 073.
- 070: I is ordered under d). The "mono" hypothesis is redundant, against the first pass's N07 (K17).
- 071: b) is proved ("x et y" stands for x_i, x_j). With K02's axiom the Conséquence holds: equisingular deployments
  over I are the Scholie's ordered spaces with 1°), plus a strictly increasing map π₀(Σ) → I.
- **With s fibrant, the nerve of Σ̲ is a Segal space** whose mapping spaces are the homotopy fibres of (s,b). For
  (S², p), Map(p,u) ≃ S¹ and BΣ̲ ≅ S², while π₀ gives [1], the Remords' loss. For two strata, BΣ̲ ≅ X by 023.

**Counts:** 35 check events, 18 corrections, 77 doubt marks. Open readings: 067 l.18-21, 065 l.16, 066 l.27, 070 l.25.

## HUNCHES

**H150e-1. The Récapitulation, completed, is Thom-Mather control data in deployed form.** This sharpens H150c-1 and
H150d-2, and is a companion to P150b-1 and P150c-1.
- **The hunch:**
  - c) of 065 is ρ-control (ρ_i∘π_j = ρ_i), and the missing commutativity (K02) is π-control (π_i∘π_j = π_i).
  - The deployment at level ε of a Thom-Mather space should satisfy a)-e) of 065-066 with the commutativity. Its
    pieces: Σ_i = X_i minus the open lower tubes, Σ_ij = {ρ_i = ε} ∩ Σ_j, and s_ij = π_i.
  - Without π-control the data do not determine an order (K02's twist).
- **Grounds:**
  - SA10-R150e-16 and R150e-34;
  - the reading 150_072-084 (ρ-control behind (3) of 040);
  - 074's "ajusté de façon cohérente".
- **Literature:**
  - J. Mather, "Notes on topological stability", Bull. Amer. Math. Soc. 49 (2012), 475-506, §7;
  - C. G. Gibson, K. Wirthmüller, A. du Plessis and E. Looijenga, *Topological stability of smooth mappings*, LNM 552
    (1976), ch. II;
  - A. Verona, *Stratified mappings: structure and triangulability*, LNM 1102 (1984).

  Locators to be checked.

**H150e-2. §13's topological category is a complete Segal model of the exit-path ∞-category, and π₀ is the Remords'
truncation.** This sharpens H150c-2, H150d-2 and H2, and the first pass's N33-N36.
- **The hunch:**
  - "s fibrant" (067) is exactly what makes the strict cartesian squares homotopy cartesian, and the Lemma of 068 is the
    π₀ shadow of that Segal condition.
  - The mapping spaces are the homotopy fibres of (s,b), which are the links.
  - The only homotopy-invertible arrows lie in δ(Σ_(0)) (069, and 070 d)), so the Segal space is complete.
- **Grounds:** SA10-R150e-23; R150e-32 (S² with a point); R150e-33 (BΣ̲ ≅ X for two strata).
- **To test:** for a Thom-Mather space, |NΣ̲| ≅ X and NΣ̲ ≃ Exit(X) (J. Lurie, *Higher Algebra*, App. A.6 and A.9).
  The gluing of 151/069 is then the realization.
- **Literature:**
  - C. Rezk, Trans. Amer. Math. Soc. 353 (2001), 973-1007;
  - G. Segal, Publ. Math. IHÉS 34 (1968), 105-112;
  - D. Ayala, J. Francis and H. L. Tanaka, Adv. Math. 307 (2017), 903-1028.

  Locators to be checked.

**H150e-3. His redundancy margins split into an equisingular one and tame ones.** This sharpens H150d-3.
- **The equisingular one:** 062 (transversality) is true under equisingularity in any category and false without it
  (K09). It is not a tame phenomenon.
- **The tame ones:** 063 and 067 (manifold fibres and faces), and the dimension step of 069, are false in Top and true
  in PL and smoothly (K07, K08, K12).
- **So** the "topologie modérée" of 073 is needed exactly for manifold recognition and for dimension.
  Equisingularity alone carries transversality.
- **Test:** in an o-minimal structure, a definable set whose product with an interval is a definable manifold, with or
  without corners, should be one itself, by definable triangulation (L. van den Dries, *Tame topology and o-minimal
  structures*, Cambridge University Press 1998, ch. 8; locator to be checked).

## PACKAGES

None new. Material for existing packages:
- **P150c-1 and P150b-1** (deployment and presentation):
  - K02's axiom belongs in the deployment data;
  - the Conséquence of 071 is the index-free form, with "mono" automatic (K17);
  - the Segal reading of §13 (H150e-2), with the S² and two-stratum checks.
- **P1 and P150f-1** (gluing): the realization BΣ̲ ≅ X (two strata; S² with a point) is a candidate form of the gluing
  theorem.
- **P-AX1 and the tame line:** the split of H150e-3, with the counterexamples of K07, K08 and K09.

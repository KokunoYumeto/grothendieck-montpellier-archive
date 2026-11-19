## STUDY

**Cote 150, scans 44-57 (sheets 18-24), read in full** in the second-pass text of 17 Nov. Seven readings were checked
again on the native scan. Claude Opus 5.5 at effort max, 19 Nov; full working in `readings/150_044-057.md`.

**The end of §10 (044 to 048 l.2).** The deployment of 002 is restated as one ordered space Σ_* over I:
- ⓐ the target maps Σ_ij → Σ_j are closed embeddings, so Σ_ii = Σ_i (26) and strict flags map to strict flags (27);
- ⓑ (28) Σ_ijk = Σ_ik ∩ Σ_jk, equivalently (29), the order below a point is induced from I;
- ⓒ disjointness when i, j have no common minorant;
- ⓓ transversality;
- e)-g): fibrations, manifolds with boundary, and the mixed condition. The boundary strata of every Σ_d are indexed by
  the nonempty flags of the ordinal sum of the gaps of d: Boolean intervals, so precylindrical (028).
- The flag consequences drawn from ⓒ in two margins of 045 are refuted by the diamond (N01, @836). They need
  disjointness for noncomparable indices.

**§11, "Digression : où on laisse tomber I" (048-057).**
- ⓐ: a topological ordered set Σ whose target map is a proper, locally bordant immersion, hence finite.
- (32) is formal. For a pushout (31) of ordered sets, the square of strict-flag spaces is cartesian in any ordered space.
  The squares that carry geometry share a final element and are not pushouts; condition b) (33)-(34) is their
  transversality. His example of a pushout is degenerate as written; the concatenation square is meant.
- (34) follows from b) by partial intersections of germs: "on voit … Car", read on the scan.
- b_2) means that the elements below a point form a finite chain. Γ is an augmented semi-simplicial space over Σ.
- (35) is off by one against Γ(d) = Σ^<(d+1).
- **The restart (056-057) separates three kinds of condition:** ⓐ topological, ⓑ set-theoretic (Σ_{≤x} finite and
  totally ordered), ⓒ geometric (transversal germs). Three facts follow from it:
  - Σ_1 is closed by properness;
  - the relative order is continuous automatically, a new re-proof;
  - for a deployment over I, ⓑ is equivalent to (29) plus the disjointness of noncomparable faces. That is the repair of
    045, eight sheets before 065.

**His self-flagged steps:**
- F01, "de = dim ??": right for faces; the manifold clause needs the smooth or PL setting.
- F02, the boundary formula: locally true from b), ⓓ and the corner model.
- F03, "ⓔ conséquence de c) et d)": refuted in Top, where ΣH × ℝ ≅ S⁴ × ℝ for a homology 3-sphere H; true smoothly and in
  PL. So #837 stands for Top.

**Slips:**
- 047, Σ_{d'} for Σ_d: the prime is in the ink;
- 049, the example;
- 055, the index of (35);
- 057, N(x) = card(Σ_{<x}), which the counts require.

**Connections:**
- 151/45-56 (the closed-strata twin);
- EXIT_TOWER A.13: flags of points are pinned, so the squares are formal;
- Joyce's manifolds with corners: (35) is the order trivialising the 𝔖_d-action.

The open readings are margins and one name, "isotrivialité|équisingularité". 39 check events, 13 corrections.

## HUNCHES

**H150d-1. §11 axiomatizes manifolds with ordered corners. Sharpens H150b-1.**
- The hunch: Σ^<(1) → Σ is the boundary immersion ∂X → X of a manifold with (possibly non-embedded) corners. The Σ^<(d)
  are the ordered d-fold boundaries. 056 ⓑ with the continuity of R150d-33 trivialises the free 𝔖_d-action, which is (35).
- Grounds: R150d-14 to R150d-17, R150d-28, R150d-30, R150d-33.
- Literature: D. Joyce, "On manifolds with corners", Adv. Lect. Math. 21 (2012), 225-258 (arXiv:0910.3518), §2; locator to
  be checked.

**H150d-2. Dropping I is what EXIT_TOWER A.13 calls for. Sharpens H150b-2 and H150a-2.**
- The hunch: Grothendieck's deployment over flags, with tubes chosen by control data, satisfies 056 ⓐ-ⓒ. Faces of
  incomparable strata are disjoint, and branches separate outside lower tubes. The strict-flag spaces are then the nerve
  of a topological poset with formal concatenation squares: a strict model of the exit-path category in which the flags
  are pinned at the level of points.
- Grounds: R150d-07, R150d-17; A.13 as recorded in sweep 2 (SA10-C2).
- To check: control data (J. Mather, "Notes on topological stability", 1970; locator to be checked) give the disjointness
  of noncomparable faces.

**H150d-3. His redundancy conjectures are theorems of tame geometry, not of topology. Links SA10-19 and the tame line.**
- The conjectures are F03, F06 and F07 (051, 062, 063, 067).
- Grounds: the double-suspension counterexample in Top (R150d-25); Ehresmann and the PL link argument in the other two
  settings.
- The hunch: in o-minimal geometry, Hardt triviality plus definable manifold recognition should give the redundancy, which
  fits the "contexte de topologie modérée" of 073.

## PACKAGES

None new. Material for existing packages:
- **P150b-1** (the deployment of a conically stratified space):
  - the index-free axioms of 056-057 (ⓐ-ⓒ);
  - the formality of (32);
  - the equivalence of 056 ⓑ with the repaired ⓑ+ⓒ of 045 (R150d-07, R150d-17);
  - the index sets of the boundary strata (R150d-10 to R150d-12).
- **P1** (the gluing theorem for tubes): the squares that are formal (concatenation) and those that are not (common
  final element). The pieces the successor-pair theorem of 151/69 lacks are the second kind.
- **P-AX1 or the tame line:** the redundancy question F03/F06/F07, with its Top counterexample (K150d-09).

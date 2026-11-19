# Cote 150, scans 31-43: integration into the SA10 study

Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8 (reading 150_031-043), horizontal sweep 3, 19 Nov 2026.

## STUDY

**Cote 150, scans 31-43 (manuscript pages 10-17), read in full, with the second pass of 17 Nov as text.**

**The forgotten axiom (031).**
- 031 ends the transversality begun on 029: the collar of X_{j'} in X_j pulls back to the collar of X_k ∩ X_{j'} in X_k.
- The intersection axiom (0), X_i ∩ X_j = ⋃_{k≤i,j} X_k, is added.
- His NB is re-proved: precylindrical stratifications are equisingular in the strongest sense, because one cube-corner
  chart trivializes the whole family along each stratum.

**The reconstruction and the Théorème (032-035).**
- The strict cone ∐T_β around the minimal strata gives the cut-open data (18).
- X is recovered by (19): X = X^* ∐_Ẋ C(p), and X_i = X_i^* ∪ ⋃_{β<i}(I·Ẋ_{iβ} ∪ X_β). Monotonicity and the
  intersection axiom are re-proved.
- The Théorème (17) ⟺ (18) holds for isomorphisms. It is the découpage of 023 with the Corollary of 024 and the Prop.
  of 026, whose converse is re-proved.
- The order of I records which minimal strata each X_i contains, so the defect of 020 does not return.

**The conical structure (035-038).**
- §8 defines it by recursion on card I: cut out the minimal strata, add their cone boundaries to the collared family,
  and recurse.
- The recursion is well founded and is the full deployment (H150b-1, now on the page).
- Remark 1 (existence) is conjectural; for Whitney stratifications it is the theory of control data.
- Remark 2 (independence of the filtration) is re-proved up to germs. Remark 3 is the stratification by the
  B_J = ∩_{α∈J} B_α over 𝒫(Λ)°.
- 038 announces local cylindrical stratifications, that is, manifolds with corners whose faces are not embedded. This is
  the case of M̄_{g,n}.

**The standard presentation (039-043).** Σ: Drap(I) → M, with:
- (1) last-vertex deletions fibrant;
- (2) other deletions boundary embeddings;
- (3) cartesian concatenation;
- the faces of each Σ_i precylindrical of type Dr(I,i)°.

Re-proved here:
- the Cor. of 039;
- the weakening of (3) in the top note, and the general cartesian square for amalgamated flags;
- the Segal reconstruction from the Σ_i and Σ_{ij};
- the internal category of 041-042, its order object, and the reduction of b) to n = 2.

Wrong as written:
- the reduction of (3) to "longueur 2" fails as he counts length (counterexample I = {h < i < j}); length 1 is right;
- "p = long. d'" on 043 is his slip for p = card d.

**EXIT_TOWER (SA10-C2).**
- His objects are the strata cut open to spaces with boundary. Under that convention M̄_{0,4} satisfies (1)-(2) and
  realizes to S².
- So A.11 refutes the run's raw-face formalization, not his statements.
- A.13 lies outside his hypotheses: graph types fail 028 c).
- A.12 proves the 039 margin condition for M̄_{g,n}.

**A reading reversed.** (20)ⓐ on 033 is "Les Ẋ_β disjoints", decided on the native scan. The second pass's "X_β" of 17
Nov and its notes-check consequence are withdrawn.

## HUNCHES

**H150c-1. His conical structure is the topological shadow of Thom-Mather control data** (sharpens H1, H150b-1, H150b-4).
- The commuting collar and cone homotheties of 025 c) are Mather's relations π_β∘π_i = π_β and ρ_β∘π_i = ρ_β.
- The recursion of §8 is the order in which control data are built. Michel Hua's project says the same of the
  recursion: "à la topologie près, la récurrence des données de contrôle de Mather".
- So remark 1 of 037 should hold for Whitney stratifications with compact minimal strata. The germ form needs
  compactness (SA10-K150b-11).
- Literature: J. Mather, Bull. Amer. Math. Soc. 49 (2012), 475-506, §§7-8; R. Thom, Bull. Amer. Math. Soc. 75 (1969),
  240-284. Locators to be checked.

**H150c-2. The standard presentation is a strict Segal model of the exit-path ∞-category, and its realization is X**
(sharpens H2, H150b-2).
- Grounds:
  - (3) is a pullback along a fibration, hence homotopy cartesian;
  - Σ_{ij} is the bundle of links, the holink up to homotopy;
  - the order object of 042 makes Σ the space of chains of an ordered space;
  - M̄_{0,4} is checked (SA10-R150c-23).
- Test: M̄_{0,5}, against EXIT_TOWER's replacement W_r (A.11) and A.7.
- Literature: J. Lurie, *Higher Algebra*, App. A.6; C. Rezk, Trans. Amer. Math. Soc. 353 (2001), 973-1007; Ayala-Francis-
  Tanaka 2017. Locators to be checked.

**H150c-3. For M̄_{g,n} the flags of a poset must become chains in the incidence category** (refines H150b-2).
- Grounds:
  - A.13: a type flag selects one of two incidence components;
  - A.1: type intervals are not Boolean;
  - A.3: the factorizations of a fixed contraction are Boolean;
  - 038: local cylindrical stratifications are announced.
- The repaired presentation is Σ over the nerve of EXIT_TOWER's 𝔐(g,n) (A.4) in place of Drap(I). That is what his
  "stratification cylindrique locale" would have to be.

**H150c-4. The deployment is canonical up to isotopy of germs, so it is a functor on isomorphisms.**
- Grounds: remark 2, re-proved up to germs (SA10-R150c-17); the Théorème of 035, which holds for isomorphisms.
- Consequence: the presentation Σ of a conically stratified space is well defined up to isomorphism. That is the
  precondition for H150c-2.

## PACKAGES

**P150c-1. From the deployment to the presentation and back** (companion to P1 and P150b-1).
- **Question:**
  - For a stratified space with his conical structure (§8), build Σ: Drap(I) → Top with (1)-(3) and a)-c).
  - Prove that X is the colimit of the simultaneous mapping cones C_{Σ,d,d'} of 043 along their transition maps, which
    he leaves unwritten.
  - Prove that Σ_• is a complete Segal space equivalent to the exit-path ∞-category.
  - Then give the version over the incidence category, for M̄_{g,n}.
- **Why it matters:**
  - it is SA10-C3, the folder's main construction, which he postpones on 043 ("On reviendra sur cette construction plus
    tard");
  - it is a point-set answer to P1 (gluing) that avoids the missing corner of 151/69.
- **What it rests on:** 150/032-043 (this reading), 150/044-047 (§10), and EXIT_TOWER A.4, A.7 and A.11-A.13.
- **Strongest known reduction:**
  - the one-layer Théorème of 035 (checked);
  - the well-founded recursion of §8;
  - the Segal reconstruction and the order object (SA10-R150c-31 to 34);
  - the case M̄_{0,4} (SA10-R150c-23).
- **Material:**
  - the corrected .tex of 150/012-047, with the scans;
  - EXIT_TOWER `sections/A.tex`;
  - Lurie, *Higher Algebra*, App. A; Rezk 2001; Ayala-Francis-Tanaka 2017; Quinn 1988; Mather 1970/2012.

# SA08 research packages, in concept (sweep 3)

From the readings of a1f628dde2f29df92 (packages P1-P3 there) and aa2156d1c23970b0d (packages P1-P2 there), both
Claude Opus 5.5 at effort max. Integrated by a34c04448e8299803 (Claude Opus 5.5 at effort max), 19 Nov 2026.

The overlapping packages are merged into two clusters, following the rule on Pro slots (one prompt per cluster):
- **Cluster 1, the multiplicative theory of PD de Rham cochains:** SA08-RP1 and SA08-RP2.
- **Cluster 2, automorphisms and operations:** SA08-RP3.
- **SA08-RP4,** the cosimplicial "Non", is a separate small question.

## SA08-RP1 · The multiplicative comparison and the shadow theorem (cluster 1)

**Question.**
1. Prove H^*_DRpd(X; k{T}, T) ≅ ⊕_i H^i(X; k) ⊗ I^{[i]} as k{T}-algebras, for every simplicial set X and ring k
   (HUNCHES H7).
2. Extend it to an arbitrary PD triple (S, S^+, t) and to the completion begun at the end of scan 233.
3. Identify the shadow and the T = 1 rationalization with it.
4. Decide his main claim (scans 11-12): are H^*(X; Z) as a ring, and RΓ(X, Z) with its product, recovered functorially
   from C^{••}_DRpd(X, Z) with its products? This needs:
   - the Ext corollary of scan 27, proved in general (it was checked here in its first case, graded);
   - a weight-respecting comparison of products.

**Why it matters.**
- It is the main claim of the 1976 lecture, and the open part of gap g1048.
- It says exactly how integral PD cochains differ from H^*(X; S).

**What it rests on.**
- Scans 4-12: CE001-CE004 and CE008 (Remark a) proved for literal cochains).
- Scans 20-45: the weighted theorem, proved on the pages and checked.
- Scans 227-233: the weightwise comparison, proved by reader 2.
- Scans 235-281: the completion and the shadow categories.
- The Pro notes O03 (an ordinary product as an integral combination of weighted ones: 6 + 3·10 − 35 = 1) and O04.

**Strongest known reduction.**
- Weight by weight, H^{p,*} = τ^{≤p}RΓ(X, k) (scan 233).
- The linear reconstruction (gaps g1031, g1041, g1080, as the Pro notes report them).
- What remains is the compatibility with T and with products.

**Material a run needs.**
- Cote 136 scans 2-45 and 219-281, with the readings.
- H. Cartan, "Théories cohomologiques", Invent. Math. 35 (1976).
- Michel Hua's project: Folder136.lean and pages 5-8 and 232 of his reading (credited).
- R. Kageyama, arXiv:2211.03289 and arXiv:2405.11570 (the PD simplex; to verify).
- Félix-Halperin-Thomas §10.
- Illusie, *Complexe cotangent* I, ch. I (décalage).

## SA08-RP2 · The binomial bridge (cluster 1)

**Question.** Is C^{••}_DRpd(X, Z) the associated graded of a filtered cochain model of integer-valued polynomial
forms, compatibly with d, the simplicial operators and the products? And does that place the 1976 construction inside
the integral schematization of Toën and Horel?

**Why it matters.** It answers his "Mais il paraît qu'il y a des ths contre ! On va pourtant y arriver" (scan 5) in
modern terms, next to Mandell's theorem.

**What it rests on.** The Pro notes R052, CE008, HUNCHES H1 and H5, and scans 4-12 and 123-141 (the dual coalgebra
model).

**Material a run needs.**
- Toën, Épijournal Géom. Algébrique 4 (2020).
- Horel, "Binomial rings and homotopy theory".
- Mandell, Publ. IHÉS 103 (2006).
- Cartan 1976.
- Ekedahl 2002 (as the Pro notes cite it).

## SA08-RP3 · Cohomology operations from automorphisms of the PD de Rham simplicial algebra; the corrected three-data theorem (cluster 2)

**Question.**
1. State and prove the three-data theorem with condition (M), together with:
   - the corrected Ω (an ind-scheme, the B-part free on the B_{2^m}, convergent);
   - the converse of the determinant criterion.
2. Does Ω act on H^*(Hom(X, Â_k)) other than through Δ ("seules les op. évidentes", scan 180)?
3. In characteristic 2, do the B-automorphisms induce Steenrod squares (his hope on scan 182) or nothing (his marginal
   "Non")? Ask the same for the automorphisms of the τ_ω functor.

**Why it matters.** A positive answer would realize Steenrod operations by automorphisms of a de Rham-type cochain
model with divided powers. A negative one bounds what such a model carries.

**What it rests on.**
- Scans 162-212, with condition (M), the F_3 counterexample to the margins of scans 170 and 172, and the decided
  readings of scans 162, 166, 178 and 200.
- HUNCHES H7 and H8.
- The Pro notes of MPL_136_142-188 (N029-N047) and of MPL_136_189-234 (R010-R020, R044).
- Michel Hua's register entry 136-automorphism-group-scheme (credited).

**Strongest known reduction.** The B-part is additive and natural and raises the exterior degree (Cor. 4). So its
effect is a family of additive natural maps H^i(−; F_2) ⊗ I^{[i]} → H^{i+1}(−; F_2) ⊗ I^{[·]}. Each component is
decided by one cocycle computation on Δ[i+1]/∂Δ[i+1].

**Material a run needs.**
- Cote 136 scans 144-212 and the readings.
- Mandell, "E_∞ algebras and p-adic homotopy theory", Topology 40 (2001).
- Steenrod-Epstein, *Cohomology Operations* (1962).
- May, "A general algebraic approach to Steenrod operations" (LNM 168, 1970).
- Roby (1963, 1965) and Berthelot LNM 407, for PD algebra.

## SA08-RP4 · The de Rham condition on the cosimplicial topos (scan 91)

**Question.** Prove or refute his double-underlined "Non": there is no mono Z → Φ with flat cokernel and universally
flasque Γ^iΦ, Λ^iΦ in presheaves on Δ^op.

**Why it matters.** It bounds faisceautisation, and answers the problem he attributes to Deligne (scan 16).

**What it rests on.** Scans 16 and 80-100, HUNCHES H3 and H4, CE036.

**Material a run needs.**
- SGA 4 V (flasque sheaves).
- Illusie, *Complexe cotangent* I, ch. I.
- Goerss-Jardine for (co)simplicial homotopy.

## SA08-RP5 · Breen's computation against the pages (scans 374-376)

From the wave-2 reading of aa2156d1c23970b0d (Claude Opus 5.5 at effort max), its package P3.

**Question.** Check every statement of 374-376 against Breen's papers, and prove or refute each one:
- the theorem on H^*(K(O, m), O);
- "de F torsion (i > 1)";
- the perfect-site corollary and its attribution ("Milne(?)");
- Ext^{2i}(G_a, G_a) = k[F]/(F^{v_p(i)}).

**Why it matters.** It decides how far the unattributed notes of 357-376 restate known work, and it places the
operations with G_a coefficients (P^0 = Frobenius), where HUNCHES H10 says the operations of Ω would land.

**Material a run needs.**
- Breen, "Extensions du groupe additif", Publ. Math. IHÉS 48 (1978).
- Breen's paper on the perfect site.
- Milne's use of the corollary.

## SA08-RP6 · ½-differential algebras (scans 348-352) and E∞ cochains (scans 357-361)

From the same reader, its package P4.

**Question.** Settle his question of 352.
- Does the exterior product on Z^• = Λ^•Ψ_* extend functorially to a ½-algebra structure on Λ^{•+1}Φ_*?
- What is the indeterminacy (in Hom(Z^{i+1} ⊗ Z^j, Z^{i+j})), and is it a cup-1 structure?
- Compare it with the Eilenberg-Zilber and E∞ structures of 357-361, and with the PD products of 345.

**Why it matters.** It is his own construction of products on the cochain model, and it bears on the operations of
clusters 1 and 2.

**Material a run needs.**
- The wave-2 reading.
- Mandell (2001, 2006).
- May, LNM 168.
- McClure-Smith on cup-i products.

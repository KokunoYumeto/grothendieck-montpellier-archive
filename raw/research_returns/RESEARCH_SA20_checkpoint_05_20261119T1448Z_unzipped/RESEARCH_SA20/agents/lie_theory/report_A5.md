# A.5 working report — 2026-11-19 13:55 UTC

## Scope and status

The source definitions were reread in the transcriptions, and the relevant primary results were opened before use. The general TOP cancellation bracket and the general definability of the maximal local-triviality locus remain explicit gates; every other A.5 request has a complete proof or a counterexample with all hypotheses verified. The counterexamples to 121/049 work in every named context, even with a single closed marked subspace.

| Prompt request | State | Result and proof |
|---|---|---|
| PL Propositions A–D | Proved | A5.003–004: full link cancellation induction, mobility product formula, maximal axis, transverse-germ uniqueness |
| TOP Proposition A | Refuted | A5.001: the compact zero-dimensional Cantor set has mobility zero everywhere but is not a zero-manifold |
| TOP uniqueness bracket of B | Unchecked gate | `unchecked_A5.tex`, first item; fattened uniqueness does not cancel the distinguished axis |
| Conjecture 1, PL | Proved with the source's connected-leaf convention | A5.005: intrinsic mobility strata are manifolds and the full closure diagram is locally a product |
| Conjecture 1, definable | Proved with connected leaves and definable isomorphisms | A5.005: finite pointed-germ classes from triangulation, dimension formula for mobility, full closure-diagram product proof; includes non-locally-compact definable sets |
| General maximal triviality open | Partially proved, gate remains | A5.008: a dense definable open exists, maximal open exists with nowhere-dense complement; maximal open is definable for one-dimensional base and for finitely triangulable maps |
| Recursion 121/036–037 | Refuted | A5.002: compact finite PL/semialgebraic mapping cylinder loses the ambient page-number germ on the recursive boundary |
| Coarsest strict partition, LPM and SAPM | Refuted | A5.009: two finite strict adapted partitions have no strict common adapted coarsening |
| Coarsest strict partition, Alg_C and An_C | Refuted | A5.010: a pure reduced affine complex threefold with a single closed algebraic mark; failure already on a Zariski open |
| Strictness, adaptation, first open | Proved corrected statements | A5.007: source condition (C), existence via conical triangulation in PL/definable settings, forced saturated open X minus the union of boundaries |
| Classical locally finite family with global algebraic leaves | Refuted | A5.006: affine line marked at all integers; distinguishes classical from Zariski local finiteness |

## Exact source corrections and conventions

All line numbers below refer to the original supplied transcription, not generated TeX.

- `MPL_121_001-048_transcription.tex`, line 502, manuscript 121/027: Proposition A fails for unrestricted locally finite-dimensional TOP spaces. Compactness and metrizability do not repair it (A5.001).
- Same file, lines 506–507, 121/027: the uniqueness bracket in Proposition B is a separate maximal-axis cancellation question. Neither the Cantor counterexample nor double-suspension arguments decide it. It remains in the unchecked file.
- Same file, lines 510 and 514–517, 121/027–028: the PL assertions are proved with regularly embedded interpreted as locally flat PL submanifolds. The normal object is unique up to pointed PL germ isomorphism, not canonically equipped with a chosen isomorphism.
- Same file, line 558, 121/031: leaves of a filtration are defined as connected components. Lines 620 and 624, 121/035–036, also explicitly use connectedness of the target leaf. A5.005 retains that convention. Line 580's later partition definition does not repeat it, so the convention is stated explicitly rather than silently dropped.
- Same file, line 580, 121/032, and line 606, 121/034: privileged means that the entire closed-leaf inclusion diagram is equisingular and leaves are manifolds without boundary. A5.005 checks the whole diagram, not only the ambient space.
- Same file, line 630, 121/036: Hardt triviality proves existence of a dense definable triviality open. It does not alone prove definability of the union of all such opens. A5.008 proves the maximal-locus statement for curves and triangulable maps, preserving the higher-dimensional gate.
- Same file, lines 634–637, 121/037: the proposed recursive marks are only traces of earlier closed leaves. The mapping-cylinder example has constant boundary trace but page number 1, 3, 1 along the bottom circle, so recursion produces a nonprivileged partition. Its explicit privileged refinement is also proved.
- `MPL_121_049-073+153+155_transcription.tex`, lines 3–12, 121/049: the claimed coarsest strict adapted partition fails in all four listed contexts (A5.009–010). This refutation uses one closed mark, so no infinitary ambiguity is needed.
- Same file, lines 21–24, 121/049: the displayed union of interiors is not the forced first open. The corrected open is the complement of the union of boundaries, as proved in A5.007.
- Same file, lines 93–112, 121/051: connectedness, nonsingularity and equisingularity are separately listed. The inserted strict condition requires connected, locally connected leaves and condition (C) for every open restriction after passing to connected components. It does not impose manifoldhood. A5.009's ray leaf with endpoint is therefore permitted.
- Same file, lines 141–148, 121/052: admissibility requires a locally finite partition into locally closed leaves with frontier closure condition. Both strict counterexamples verify these requirements, and a local-to-global lemma proves the quantified condition for arbitrary opens.

## Counterexample certificates

1. `code/A5_mapping_cylinder.py`, outputs `logs/A5_mapping_cylinder.json` and `.txt`. Exact rational simplicial chain calculations: 8 vertices, 18 edges, 10 triangles; bottom page numbers 1, 3, 1; local H2 ranks 0, 2, 0. The supplied finite triangulation and the geometric mapping-cylinder proof independently identify the local books.
2. `code/A5_strict_no_coarsest.py`, outputs `logs/A5_strict_no_coarsest.json` and `.txt`. Explicit rational 3-dimensional polyhedron with 17 vertices, 50 edges, 52 triangles and 18 tetrahedra, total volume 24. Both partitions pass all 137 simplex open-star component/frontier tests; the only common adapted coarsening fails two. The written small-box analysis plus a local-to-global lemma establishes every-open strictness, beyond the finite test.
3. `code/A5_complex_strict_no_coarsest.py`, outputs `logs/A5_complex_strict_no_coarsest.json` and `.txt`. Twelve exact Groebner/parametrization checks over QQ and six local frontier tables pass. The reduced union Y union E has two smooth three-dimensional irreducible components, so purity is verified. The all-open proof is geometric: local discs and punctured discs establish connectedness at the origin, two branches along the nonzero u-axis, and strictness. The common coarsening fails on the Zariski open u nonzero.

Root independently audited A5.009–010 on 2026-11-19 at about 13:46 UTC and reported PASS, including the arbitrary-open transport lemma and pure-complex origin case. Four missing TeX backslashes and three multi-alignment display environments were corrected after that review.

## Primary source locators opened

- Armstrong, Warwick thesis (1966), paper III, Definitions 2/2a/2b and Lemmas 1, 3 (with corollary), 4, printed pp.11–17, physical PDF pp.100–106. This is the primary PL comparison; the proof is also written independently in A5.003–004.
- Coste, *An Introduction to O-minimal Geometry* (1999), Theorem 5.22, pp.62–63, with proof. Theorem 5.24, pp.63–65, was checked and is only about scalar-valued maps; its scope must not be silently extended to arbitrary map families.
- Shiota, arXiv:1002.1508v3, Theorem 2.1 p.5; noncompact qualifications pp.22–24. No compact-pair result is used to assert a noncompact generality.
- Siebenmann, *Deformation of homeomorphisms on stratified sets* (1972), Corollaries 4.12–4.13 pp.140–141: fattened uniqueness only, explicitly recorded as insufficient for TOP-B cancellation.
- For the separate A103 audit: Burghelea–Lashof, *The homotopy type of the space of diffeomorphisms II*, Trans. AMS 196 (1974), Theorems 6.1–6.2 p.41, proofs pp.42–43, give the actual unstable smooth/PL component comparison and PL/TOP weak equivalence in dimension greater than five. The comparison is independent of the corrected Igusa exact sequence. See `audit_A103_igusa.tex` and `references.bib`.

## Remaining approaches and precise obstruction

### TOP-B maximal-axis cancellation (historical gate, closed by A5.011)

A5.003 settles PL. The unproved TOP statement is cancellation of a maximal Euclidean factor in a germ homeomorphism preserving its distinguished axis. Reading Siebenmann's fattened uniqueness gives only products with the stratum factor. Friedman's cone uniqueness via the open-cone swindle concerns the whole cone and does not cancel that factor. Bare double suspension cannot straighten the distinguished singular axis because its deleted complement retains its fundamental group. A possible bounded-homeomorphism construction F times R^i to F-prime times R^i would need a bounded product homeomorphism with non-homeomorphic cone germs; no such verified pair has yet been found. Ordinary stable homeomorphisms from tangential-thickness results need not satisfy the required control.

### General higher-dimensional maximal-open definability

A5.008 proves the largest open exists and has rare complement, and proves definability for curves and finitely triangulable maps. Hardt supplies one finite partition, but it is insufficient to infer that the property of extension across its lower strata is constant on those strata. General families of maps can have infinitely many topological types, as Coste's p.66 caution illustrates. The next approach is a uniform local-germ classification of the proper map, or a proper-map stratification theorem which trivializes neighbourhood germs along target strata, with every hypothesis checked; merely assuming every proper definable map is triangulable is not allowed.

## 14:13 UTC update: exact TOP-B cancellation refuted

A5.011 supplies a full axis-fixing counterexample, even with a polyhedral ambient space and ENR normal factors. The normal germ C is the positive-end compactification of a smooth 6-manifold W. Its stabilization is R times the cone on L^5(23), through an explicit extension of a bounded Z²-equivariant lift. The normal germs differ because the positive end has nonzero obstruction x+x*. Both vertices are isolated nonmanifold points and hence immobile; the singular axis has mobility exactly one.

The projective module P=(2,r) over Z[C23] has the explicit idempotent E=[[1-r,3(1-N)],[2,r]]. Its Bass matrix 1-E+zE gives the finite h-cobordism input. The nonzero obstruction is proved using the ideal (2,omega) in Q(sqrt(-23)), without relying on a class-number table. The ideal has order three, and the class persists under extension of degree eleven. Group-ring convolution and independent SymPy polynomial remainders agree; the quadratic ideal equalities are checked by exact lattice HNF. All data are in code/A5_top_normal_cancellation.py and the corresponding txt/json logs.

Source correction: Siebenmann1972 Proposition5.14 p143 says minus while its proof p144 says plus. Hughes–Ranicki1996 Remark18.4 p218 likewise has an off-by-one duality sign relative to its displayed dimension convention. Neither discrepant statement is used. Milnor1966 original §10 p394 gives tau(Z,N)=(-1)^(dimZ-1) conjugate(tau(Z,M)); dimZ=7 gives plus. The full geometric proof uses Milnor §11 pp398–399, §10 p393, and Hughes–Ranicki Prop11.3/Ex11.5 pp123–125.

Input correction: MPL_121_001-048_transcription.tex line506, uniqueness bracket of B, is false in TOP even for a deveissable ambient space. This is stronger than the Cantor counterexample to A at line502. Root independent proof review was requested. Only the general higher-dimensional maximal local-triviality-locus definability remains an A5 gate.

## 14:19 UTC independent audit

Root independently passed A5.011 at 14:16 UTC, including the original Milnor p.394 sign, existence theorem 11.1 and lemma 11.2, Hughes--Ranicki 11.3(iii--iv) and 11.5(ii), the determinant proof of nonzero x+x*, the equivariant bounded lift, and both continuity estimates. Root also reran the exact certificate (logs/root_A5_011_certificate.txt). The passage from P tensor_R O to its image J now explicitly uses projective rank one and generic injectivity over the domain O. The certificate records UTC start and elapsed time.

The two source discrepancies were checked on images of the original pages: Siebenmann 1972 printed p.143, Proposition 5.14, has x-(-1)^n bar(x), whereas its p.144 proof has x+(-1)^n bar(x); Hughes--Ranicki printed p.218, Remark 18.4, uses the opposite boundary-map sign for a cobordism displayed as dimension n+1. Neither statement is a premise of A5.011. The adopted sign is derived directly from Milnor's original p.394 theorem and the composition formula, with an independent positive-half cellular-chain computation. In particular proper homotopy equivalence alone is not invoked to preserve the end class; the infinite simple torsion transfer is computed.

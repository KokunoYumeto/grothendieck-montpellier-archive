# A.5 working report — 2026-11-19 16:29 UTC

## Scope and status

The source definitions were reread in the transcriptions, and the relevant primary results were opened before use. The general definability of the maximal local-triviality locus remains an explicit gate only for fibres of dimension at least two over targets of dimension at least three; every other A.5 request has a complete proof or a counterexample with all hypotheses verified. The counterexamples to 121/049 work in every named context, even with a single closed marked subspace.

| Prompt request | State | Result and proof |
|---|---|---|
| PL Propositions A–D | Proved | A5.003–004: full link cancellation induction, mobility product formula, maximal axis, transverse-germ uniqueness |
| TOP Proposition A | Refuted | A5.001: the compact zero-dimensional Cantor set has mobility zero everywhere but is not a zero-manifold |
| TOP uniqueness bracket of B | Refuted | A5.011: explicit axis-fixing bounded stabilization with unequal normal end obstructions; root audited PASS |
| Conjecture 1, PL | Proved with the source's connected-leaf convention | A5.005: intrinsic mobility strata are manifolds and the full closure diagram is locally a product |
| Conjecture 1, definable | Proved with connected leaves and definable isomorphisms | A5.005: finite pointed-germ classes from triangulation, dimension formula for mobility, full closure-diagram product proof; includes non-locally-compact definable sets |
| General maximal triviality open | Reduced to fibre dimension at least two and target dimension at least three | A5.008 gives dense open and rare complement; A5.012 settles finite fibres; A5.013 settles target dimension at most two; A5.014 settles fibre dimension at most one in every target dimension, all over arbitrary real closed fields; finitely triangulable maps are also settled |
| Recursion 121/036–037 | Refuted | A5.002: compact finite PL/semialgebraic mapping cylinder loses the ambient page-number germ on the recursive boundary |
| Coarsest strict partition, LPM and SAPM | Refuted | A5.009: two finite strict adapted partitions have no strict common adapted coarsening |
| Coarsest strict partition, Alg_C and An_C | Refuted | A5.010: a pure reduced affine complex threefold with a single closed algebraic mark; failure already on a Zariski open |
| Strictness, adaptation, first open | Proved corrected statements | A5.007: source condition (C), existence via conical triangulation in PL/definable settings, forced saturated open X minus the union of boundaries |
| Classical locally finite family with global algebraic leaves | Refuted | A5.006: affine line marked at all integers; distinguishes classical from Zariski local finiteness |

## Exact source corrections and conventions

All line numbers below refer to the original supplied transcription, not generated TeX.

- `MPL_121_001-048_transcription.tex`, line 502, manuscript 121/027: Proposition A fails for unrestricted locally finite-dimensional TOP spaces. Compactness and metrizability do not repair it (A5.001).
- Same file, lines 506–507, 121/027: the uniqueness bracket in Proposition B is a separate maximal-axis cancellation question. Neither the Cantor counterexample nor double-suspension arguments decide it. A5.011 supplies a separate exact counterexample.
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
- Coste, *An Introduction to O-minimal Geometry* (1999), Theorems 2.1 (monotonicity), p.15; 2.9–2.10 (uniform finiteness and cell decomposition), p.19; 5.22 (Hardt), pp.62–63, with proof; 6.6 (C^k cell decomposition), p.71. Theorem 5.24, pp.63–65, is only about scalar-valued maps. The full primary author-upload HTML was opened at https://www.researchgate.net/publication/228392940_An_introduction_to_O-minimal_geometry after the Rennes PDF returned503/403. None of those statements is used to assert a general uniform homeomorphism bound.
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

## 15:05 UTC: finite-fibre maximal locus

A5.012 proves maximal-open definability for every proper continuous definable map with finite fibres, without invoking triangulation of the map. The local-homeomorphism locus is given by an explicit first-order injectivity/openness formula. Properness then makes the bad image closed and produces a simultaneous finite covering chart at each good value, including the empty-fibre case. This narrows the remaining general gate to positive-dimensional fibres; it is not claimed as a proof of that remaining statement.

Root independently passed the real-field A5.012 proof, then requested its arbitrary-real-closed-field scope be made explicit. The theorem now uses definably proper and definable manifold without boundary. Closedness of images of closed definable subsets is proved by curve selection, definable choice and endpoint limits in the definably compact preimage of a closed target curve. This avoids ordinary topological compactness over non-Archimedean fields and proves every finite-fibre case in the requested field scope.

Root independently passed the full arbitrary-real-closed-field extension at 15:09 UTC. The only remaining A.5 mathematical gate is the general maximal-open definability claim with positive-dimensional fibres over a higher-dimensional base.

### Original-source exclusion check (15:17 UTC)

Verdier (1976), original printed pp.311–312, has now been downloaded from the GDZ original scan and read visually. Theorem 4.14 (p.311) is a proper stratified-submersion isotopy statement; Corollary 5.1 (p.312) supplies a dense Zariski open local-triviality locus for complex algebraic morphisms. Neither identifies the maximal locus. Anna Valette (2021), full open-access primary HTML, Theorem 2, similarly gives sufficient generalized-critical-value exclusions. These observations do not establish that definability of the maximal locus is an open problem in the literature; they only delimit what the inspected statements prove.


## 15:52 UTC: all targets of dimension at most two

A5.013 proves maximal-open definability for every continuous definably proper map to a definable target of dimension at most two, over every real closed field. This is a strict reduction of the remaining gate: it now requires positive-dimensional fibres and a target of dimension at least three.

The geometric input is Shiota2010's unnumbered punctured-edge statement, printed p.33 with full proof pp.33–34. Folding the two sides of a target edge and triangulating the source compatibly with both sides produces a finite semilinear map agreeing with the original map near a deleted edge interval. Its actual compact fibre is a definable clopen subset of a semilinear fibre and therefore a finite subpolyhedron. A polyhedral neighbourhood of that full fibre, together with properness excluding all other source points over a smaller target neighbourhood, gives an actual finite PL model.

Two separate model-theoretic compactness arguments supply the non-Archimedean uniformity. The first covers every edge point in every elementary extension by finitely many formula formats for deleted-interval agreement certificates; the union of their intervals is definable with finite complement. The second covers only that already definable set by finite PL-chart formats. Each fixed simplicial map has a good locus which is a finite union of simplex interiors in the original structure, so the chart formulas define the unknown maximal locus there. No elementary-extension invariance of goodness, and no prior definability of the maximal locus, is assumed.

Root independently read the entire draft, Shiota pp.33–34, and Marker Orsay notes Theorem2.4 p.17, and reported PASS at15:50UTC. Its requested clarifications have been incorporated: target polyhedron g(Q) union a small box, possible nonsurjectivity of the PL model, and choice of the finite simplex-good loci in the original structure. The graph compactification of a proper map and the treatment of arbitrary noncompact two-dimensional targets are included.

Input locator remains MPL_121_001-048_transcription.tex line630, manuscript121/036. This strengthens the earlier partial answer without using Hardt alone to recognize the maximal locus. The first remaining dimension pair is a positive-dimensional fibre over a three-dimensional target; the next step is to inspect whether Shiota's punctured-edge construction admits simultaneous tangential parameters or whether a separate recognition theorem handles the resulting codimension-two locus.


## 16:29 UTC: all compact graph fibres, in every target dimension

A5.014 proves definability of the maximal triviality locus for every continuous definably proper map with fibres of dimension at most one, over every real closed field. It also defines exactly the part of the maximal locus with such fibres for an arbitrary proper map. Combined with A5.013, the remaining gate now requires fibre dimension at least two and target dimension at least three.

The first step gives a uniform L1-length replacement estimate for graph homeomorphisms. Finite Hardt families and coordinate monotonicity bound the variation on intrinsic edges; replacing any small homeomorphism by a map linear in normalized arc length multiplies displacement by a fixed constant. Canonical maps have finitely many formula formats, so complete regularity becomes an explicit first-order condition. This is a special one-dimensional argument, not an assumption that general homeomorphisms have bounded format. Loop edges are treated by their cut interval parametrizations with the endpoints identified at the vertex.

The remaining continuous-choice problem is solved directly. On each circle component, a maximum energy built from the intrinsic circle metric and an ambient quadratic penalty has a unique minimizer near a fixed regular point. The penalty confines active maximizers to a short arc; on that arc the energy is one strictly convex quadratic plus a maximum of affine functions. The unique minimizers give continuous definable anchors. After anchoring, the group of canonical graph automorphisms is finite, and a positive displacement gap makes every sufficiently small canonical comparison unique. These unique comparisons form a local definable bundle chart. The whole argument uses definable compactness and epsilon-delta estimates over the given field, without integration or metric-space selection theorems.

Root independently audited the entire proof and reported PASS at16:27UTC. The requested maximum-operator typo and loop-parametrization clarification were incorporated before promotion. Precise primary inputs are Coste Theorems2.1p15,2.9–2.10p19,5.22pp62–63,6.6p71. No finite counterexample or finite search is used by this theorem. Input locator remains the maximal-locus claim in MPL_121_001-048_transcription.tex line630, manuscript121/036.

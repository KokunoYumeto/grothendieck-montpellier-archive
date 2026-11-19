# 156-5: integration

Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8 (reader A), horizontal sweep 3, 19 Nov 2026. The full reading is `156-5.md`; the computations are in `156-5_sorite_checks.py`.

## STUDY

**156-5, "Sorite ensembliste", GF V, 14-18 June 1986, scans 2-49 (SA21-14): the set-theoretic model of the contrées and ateliers.** It begins on 14 June, the day 156-4 ends, and runs into the first days of 156-6.

**Préadmissible and admissible families (scans 2-8).** For a family 𝓛 of subsets of L, Proposition 1 gives three equivalent forms of "every point lies in a smallest member". They hold on all 65,536 families on 4 points (SA21-R5-01).
- Admissible means in addition non-empty open strata A° = A ∖ ∂A, so ∅ is excluded.
- His Remark that η is "pas surabondante" holds only for infinite families. For artinian families γ alone gives η; his margin already calls his drawn example "idiot" and points to GF VIII, pp. 44-45.
- **An admissible family is an ordered set I with a surjection φ: S → I**, that is, a preorder on S ⊂ L. Its members are the irreducible closed sets, and the "parties 𝓛-constructibles" are the saturated sets.

**The figures ensemblistes (scans 8-12).** Compatibility of two families has four equivalent forms: a union in which both are closed; closed intersection with the common support; the common-support form; stratum by stratum ("Remords"). All four agree on all pairs on 3 points.
- The admissible families, ordered by "closed sub-family", are the **figures ensemblistes** Fig(L) of 156-6/3.
- Their irreducibles, the families with a largest member, are the **multistrates ensemblistes**.
- C1-C3 of 156-4's fourth system hold.

**Connectedness (scans 13-15): false.** He concludes that the multistrates form one component, so "l'axiome C4 ... est automatique". His bounding "multistrates" {A, {x}, A ∪ {x}} and F ⊠ G are not admissible: the top member is the union of the others. Computed: 3 components on 2 points and 5 on 3, with incompatible pairs across components. So **156-4's C4 fails in Fig(L)** (SA21-K5-01). 156-6 has no component axiom.

**Supports (scans 16-17).** Disjoint figures are those with disjoint supports, and the supports are P(L). From the figures one recovers P(L) but not L: "L̂, le compactifié de Stone" (H3, H6).

**Refinement and subdivision (scans 20-27).** Four equivalent forms of refinement; the simplest is that the preorder of F is finer than the one G induces on |F|. Four equivalent forms of subdivision; the simplest is refinement with the same support, equivalently maximal refinement. And F ≪ G ⇔ F is a sub-figure of a subdivision of G (156-4's definition (1.29) holds in this model). All are computed.
- Scan 27 states, in the model, the condition that 156-6 makes its At 13 (the "axiome du support").
- Scan 27 checks C5, C6, C7 and C8₀ of 156-4 in this model. **156-5 is the model test of 156-4's fourth system.**

**Intersection and extension (scans 28-36).** The "figure intersection" F.G is the Inf for ≪, "s'apparente à une propriété de 'modération'".
- C7: F′ = G′ ∪ (F ∖ G) extends a subdivision of a sub-figure (computed).
- The coarsest such extension K = J′ ⨿ (I ∖ J), with a cartesian square, is the model of 156-6's At (fac) 14 bis.

**Ultratopologies (scans 37-49, 18 June).** "le point de vue des ultr. topologies (i.e. top. préordonnées) est peut-être le plus pratique".
- A lemma on the coarsest topology extending a finer topology on a closed part (re-derived).
- Corollaries on "homotopiquement propre" maps and "équivalence d'homotopie faible universelle" (scan 47; not re-derived).
- His own "C'est ultra faux", with a three-element counterexample, ends in the right characterization: closures of parts outside T are unchanged.

**Counts:** 16 check events, 5 corrections. No scan image was viewed; the open readings are listed in `156-5.md` §8.

## HUNCHES

**H5-1. Fig(L) is the category of preorders on subsets of L, the Alexandrov (T₀ after quotient) spaces, and his 18 June switch to "ultratopologies" makes this explicit (sharpens H6 and H9).**
- **Grounds:** the (I, S, φ) description (scans 5-6); refinement as a finer induced preorder (margin b″, computed); subdivision as the same support (scan 24); scans 37-38.
- **What it predicts:** the maquettes of 156-8/3 ("un espace ultra top. … T₀") are this model taken abstractly, and the multistrates of an atelier under ≪ (156-6/30, H6-1) are its points.

**H5-2. Scan 47 is a fibre lemma for maps of finite T₀ spaces, the first homotopy statement in cote 156 (confirms the link SA21-8, H9).**
- **Grounds:** 156-5/47, "φ* homotopiquement propre i.e. les φ*⁻¹(J_{≤x}) 'faiblement contractiles'" and "équivalence d'homotopie faible universelle".
- **What it says:** the hypothesis is that of Quillen's fibre lemma for poset maps, and the conclusion is a weak homotopy equivalence, as for finite spaces in McCord's theory.
- **Literature:** D. Quillen, "Homotopy properties of the poset of nontrivial p-subgroups of a group", Adv. Math. 28 (1978), 101-128, Prop. 1.6; M. C. McCord, Duke Math. J. 33 (1966), 465-474 (locators to be checked).
- **The hunch:** his statement, that the property passes from φ* to φ, is a gluing form of that lemma along a closed part.

**H5-3. 156-4's C4 is false in the set-theoretic model, which is plausibly why the component axioms disappear after 156-4.**
- **Grounds:** SA21-R5-08 (computation), and At 1-At 14 of 156-6, which contain none.
- **The diagnosis:** his error is a join intuition. A union of strata has no new points, so it has no open stratum, while a geometric join has an interior. In models with cones (polyhedra, tame sets) the bounding multistrates exist.
- **What it predicts:** the component axiom holds in polyhedral or tame contrées and fails in Fig(L).

**H5-4. Two different tameness axioms (sharpens H2).**
- **Grounds:** 156-5/29, where the existence of an Inf for ≪ "s'apparente à une propriété de 'modération'"; and 156-4/70, where "modérée" is the comparability of subdivisions.
- **The two axioms:**
  - common refinement (Inf for ≪) is the o-minimal statement that finitely many definable sets admit a common compatible cell decomposition;
  - comparability of subdivisions is the Hauptvermutung (Shiota).
- **The hunch:** the 1986 notion of "modéré" bundles the two, and they separate in models. In topological polyhedra the Inf for ≪ exists (common refinement of two subdivisions after a further subdivision), while comparability of subdivisions of the same figure is the Hauptvermutung, which fails (Milnor 1961).

## PACKAGES

**P5-1. The set-theoretic model as a test of every axiom system of cote 156.**
- **The question:** decide, in Fig(L) and in its sub-ateliers (finite type, finitely spacious, simplicial), which axioms hold, with a countermodel for each that fails:
  - 156-4's Cont 1-5 and C1-C8₀;
  - 156-6's At 1-At 14, At ens 1-4 and Sous-at 1-4;
  - 156-8's Mag 1-4 and At 1-At 5.

  Also prove or refute the homotopy corollaries of 156-5/47, and the infinite counterexample to the redundancy of η cited from 156-8/45-46.
- **Why it matters:** it is the one model that he wrote out, and it already refutes one axiom (C4). P1 (event structures), P3 (supports) and P7 (the axiom systems side by side) all need its verdicts.
- **What it rests on:** this reading (16 check events, 5 corrections) and `156-6.md`; STUDY §2.
- **Strongest known reduction:**
  - the computations of `156-5_sorite_checks.py`: Prop 1, compatibility, refinement, subdivision, F.G and C7 checked on small sets;
  - the counterexample to C4;
  - At 13 and At 1-At 8 verified for set-theoretic ateliers (156-6/55, 91).
- **Material:** `c156-5.txt`, `c156-6.txt` and `c156-8.txt` with the .tex and scans (156-5 scans 37-49 for the empty displays); `156-5_sorite_checks.py`; Quillen 1978; McCord 1966; Johnstone, *Stone spaces* (1982), ch. II (locators to be checked).

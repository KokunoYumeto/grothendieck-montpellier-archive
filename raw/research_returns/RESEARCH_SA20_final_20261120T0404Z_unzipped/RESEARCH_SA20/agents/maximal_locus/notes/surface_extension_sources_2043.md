# Original-source audit: planar extensions and finite surface graph complexity

2026-11-19, after 20:37 UTC source freeze. Research note only; no included source, bibliography, ledger, or checker was edited. Status: source improvements and a possible route, no A5 movement.

## Dinh–Nguyen: individual definable extensions

Si Tiep Dinh and Nhan Nguyen, *Planar extensions in o-minimal structures*, 36-page author preprint dated June 2, 2026. Full original: https://math.ac.vn/uploads/files/IMH20260601.pdf . Local PDF: `source_external/maximal_locus/dinh_nguyen2026_planar.pdf`; 635474 bytes; SHA256 `a30efccfe4afe7521a068cd06533bd784db22776afc5481d1fbffc98767f81d3`.

The ambient field is R with a fixed o-minimal expansion (p. 3). Theorem 1.10, pp. 11–12, extends an individual definable embedding of a Jordan curve to a definable plane homeomorphism. Its proof chooses ambient definable triangulations H₁,H₂ carrying polygonal Jordan curves to the input curves, reduces to the polygonal case by H₂⁻¹hH₁, invokes the Schoenflies construction, and conjugates back. No joint parameter continuity, uniform formula-format bound, or metric smallness conclusion is stated.

Theorem 3.5, p. 25, treats compact sets of dimension at most one using consistent cyclic orders, facial orientations, and incidence; Corollary 3.7, p. 28, handles the connected case. These individual extension results do not by themselves establish continuous selection of fillings in a family.

Audit: full-original text read; printed p. 11 visually rechecked at 20:39 UTC (`dinh_nguyen2026_planar_p11.png`).

## Nayyeri–Xu 2017: a finite crossing bound

Amir Nayyeri and Hanzhong Xu, *On the Decidability of the Fréchet Distance between Surfaces*, 18-page author preprint dated July 13, 2017; SODA 2018, pp. 1109–1120, DOI 10.1137/1.9781611975031.72. Full original: https://web.engr.oregonstate.edu/~nayyeria/pubs/frechet.pdf . Local PDF: `source_external/maximal_locus/nayyeri_xu2017_decidability.pdf`; 338344 bytes; SHA256 `899545bb8b8a1cc79f4c139d33cae2f07e8fd6c3ad0b7f2e491638cbdcacc987`.

Scope (pp. 1–2): homeomorphic genus-zero triangulated surfaces, with linear immersions of triangles into R³. Lemma 4, p. 7, states that Fréchet distance at most δ is equivalent to a scaffold map of length at most δ whose crossing number is at most 2^(m+n), where m,n count vertices. Lemma 5, pp. 7–8, replaces edge parametrizations so the length is determined by finitely many vertices and crossings. The normal-coordinate construction yields finitely many combinatorial descriptions; Corollary 1, p. 9, bounds their number by 2^O((m+n)²).

The bound does not depend on tolerance. No joint continuous selection theorem is asserted. The proof uses linear geometry; transferring it through arbitrary curved definable triangulations requires further control.

Audit: full original read; printed p. 7 visually rechecked at 20:39 UTC (`nayyeri_xu2017_decidability_p7.png`).

## Nayyeri–Xu 2016: controlled filling and shortcutting

Nayyeri–Xu, *On Computing the Fréchet Distance Between Surfaces*, SoCG 2016, LIPIcs 51, 55:1–55:15, DOI 10.4230/LIPIcs.SoCG.2016.55. Full publisher original: https://drops.dagstuhl.de/storage/00lipics/lipics-vol051-socg2016/LIPIcs.SoCG.2016.55/LIPIcs.SoCG.2016.55.pdf . Local PDF: `source_external/maximal_locus/nayyeri_xu2016_frechet.pdf`; 588381 bytes; SHA256 `427d0ea5f9a551695785bcd1bb4a76c5c8741f5346d8d84c11be9ecec41bd53d`.

The setting again uses genus-zero triangulated surfaces and linear immersions. Lemma 6, p. 55:8, attributes to Cook et al. an extension of a prescribed triangle-boundary homeomorphism to a folded polygon, with length at most boundary length plus any positive ε, in polynomial time in the number of triangles. Lemma 7 extends an entire scaffold with arbitrarily close length. Lemma 8 controls shortcutting when the comparison curve is a line segment. Lemma 9 bounds crossings of noncrossing curves after edge shortcutting: an edge met by m distinct curves is crossed at most 2^m times. Lemma 10 continues the finite-coordinate construction on p. 55:9.

Audit: full original read; printed p. 55:8 visually rechecked at 20:39 UTC (`nayyeri_xu2016_frechet_p8.png`). The antecedent Cook et al. proof has not yet been directly audited; retain that attribution rather than claiming to have read it.

## Consequences for the pending route

The finite crossing bound supplies actual geometric control missing from an appeal to arbitrary triangulation alone. It is promising for a fixed PL genus-zero problem and warrants communicating to the higher-comparison agent. It does not yet solve the present general problem, for three separate reasons.

1. The reduction uses line segments and Euclidean convexity. A fixed arbitrary definable parametrization of a curved surface need not preserve the relevant distance bound under shortcutting. Approximating that parametrization at a tolerance tending to zero can reintroduce unbounded subdivision complexity.
2. The cited extension statements construct a homeomorphism for each instance or tolerance. An algorithmic complexity bound is potentially useful for a finite-format definability proof, but the source does not establish that all choices are jointly continuous in the parameters. That sewing step must be supplied.
3. Genus zero is a real hypothesis of the finite crossing argument. The note does not extrapolate the theorem to arbitrary closed surfaces, singular fibres, arbitrary o-minimal fields, or multidimensional base parameters.

The relevant remaining output is a coherent family of controlled graph embeddings and disk fillings, or a uniform cell-like collar theorem. The present source audit alone proves neither. The separate `radial_angular_recognition_2037.md` records the exact criterion to which any such result must be applied.

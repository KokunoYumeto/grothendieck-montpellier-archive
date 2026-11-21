# Exact ternary-glue classification and coface checks

Author/reviewer: GPT-6 Astra Pro, `/root/tripod_integral`, 2026-11-21. The entire clean classification proof, entire final classification verifier and entire clean coface proof/verifier were read. The exact finite classification and both sets of rational minimum checks were executed successfully. Independent whole-proof reviews were requested separately; their verdicts are distinguished below.

## Coverage input and finite classification

The five determinant-one, three-dimensional origin-symmetric polytope classes are a published completeness input from Averkov-Schymura, Mathematical Programming 206 (2024), Section 5.2, Table 2, printed page 85. The definition and complete Section 5.1 algorithm and Section 5.2 table discussion were read in the archived primary final text. The arXiv v2 primary copy was freshly retrieved as `turn347355058view1`; its corresponding Table 2 is on PDF page 22. The complete source is https://arxiv.org/pdf/2111.06294, and the author data repository is https://github.com/mschymura/delta-classification.

The five original records were retrieved directly from https://raw.githubusercontent.com/mschymura/delta-classification/main/data/dim_3_delta_1.txt and saved as `work/k12_source_data/delta_dim_3_delta_1.txt`, SHA256 `2ea61787f76cb353dcdecda1faad3f8dc8ff99679b4d692d17720ee5518a95a8`. The complete literal records were read and copied into the final verifier. Their exact integer points, determinant bounds and unit minors are checked in the replay. The published completeness of this five-record list is retained explicitly; the full polytope classification was not rerun.

The reduction from ambient index three to a totally unimodular relation matrix is integral: every independent ten minima form a basis of their generated sublattice. The glue line is represented modulo the row space over F3. Repeated equal colors in a signed Gale class give an odd integral transposition. For zero columns, independent sign changes reduce the color types to zero/nonzero and give the analogous bound of two positions. The 65,788 remaining finite states exhaust the nonzero color masks and normalized zero patterns of total multiplicity thirteen.

The short-support obstruction is proved directly by the displayed quadratic identity. Its strict inequality uses completeness of the minimum set: all vectors in a nontrivial glue coset have norm strictly larger than the old minimum. Thus support at most six is impossible, including the equality case six.

All integral automorphisms of each signed Gale set are enumerated by the images of a unit basis. The orientation test matches each color under its signed class permutation and one of the 27 row shifts. The transpose convention was checked carefully: BP=UB implies P^t preserves the relation lattice, hence P does as well because P is a signed orthogonal permutation. The explicit color equation is exactly Pc-c in the row lattice modulo three. An automorphism acting by minus one on the glue line can be composed with global negation, which fixes every quadratic ray; normalized zero-column signs cause no omitted orientation permutation.

The complete finite replay removes 23,416 states by odd symmetry and 24,300 by the support identity. The remaining 18,072 states have exactly 26 complete orbits, with the representatives printed in the TeX. No lattice-equivalence class is discarded using floating-point data.

## Exact realization

For every retained state, the frozen data specify the generated-lattice representatives, the glue colors, an explicit ambient basis numerator, all ambient minimum vectors and an integer Gram matrix with its denominator. The verifier checks the basis change and congruence of the glue vector, then verifies the positive rational LDL identity and exhaustively enumerates all vectors of norm at most one. Every one of the 26 forms has exactly thirteen minimum pairs and quadratic rank thirteen. Enumeration node counts range from 325 to 467. The primitive complementary-minor calculation and ambient index three give maximal minimum-basis index exactly three.

The all-symmetry test has no odd stabilizer for these 26 states. Every full-rank facet nevertheless has an odd stabilizer: its rank-two totally unimodular Gale matrix has at most three nonzero signed classes, each of size at most three if no equal-color swap exists, and at most two zero positions. This cannot account for twelve positions. Rank-deficient facets are relative zero. All 26 templates are therefore cycles. This statement alone gives no nonboundary conclusion.

Final classification verifier: `work/k12_ternary_glue_certificate.py`, SHA256 `f12b789a02d61fc4be623a11528435e8d80f69e9d1f3ce4ff24ba6da35d59be0`. Frozen form data: `work/k12_ternary_glue_form_data.json`, SHA256 `a4377187a3f9f20bd8366e4e2a6e7a32ed4ec610fa014d7095a4810a360bdbe7`. Classification TeX: SHA256 `40e0db37faac4716e53083d24f8b95ea15353d8b92b32aafd0e979acff0ee55b`.

The sibling reviewer `/root/vandiver_k` reported a full independent PASS after reading the entire classification proof and verifier, matching all five original data records, reconstructing the action and coverage argument, and rerunning every exact check. The parent review was separately requested. This does not substitute for the independent coface review requested next.

## All twenty-six explicit fillings

The coface discovery searched primitive rays fixed by a chosen odd reflection for every full-rank old facet. It also enforced that each old coloop-deletion facet remains rank deficient after the new ray is added. Floating optimization was used only to discover forms. The final frozen rational matrices are verified independently of the optimization script.

The final coface verifier proves, for each of 26 records, positive definiteness, exactly fourteen minimum pairs and quadratic rank fourteen. Its complete exact searches use between 327 and 477 nodes. For every nonrelative old-ray deletion it constructs the rank-one modification I+(epsilon v_b-v_a)phi in the actual ambient integral coordinates and verifies its square is the identity, its prescribed signed swap, the fixing of all other facet rays and the fixing of the new ray. For every marked relative facet it checks vector rank exactly nine after adding the new ray. It checks all thirteen old-ray deletions with no omission.

Thus the old cell is the unique surviving full-rank facet. The coface stabilizer preserves it and has even orientation sign. The incidence coefficient is one because exactly one actual facet is in the old cell's orbit, the source stabilizer fixes it, and inclusion on degree-zero coinvariants has no target-index multiplier. This is the already inspected DEKM Section 1.2.1 equations (1)-(2), printed page 4, and Proposition 1.3, printed page 5; fresh primary retrieval was `turn804552978view0`.

Final coface verifier: `work/k12_ternary_coface_certificate.py`, SHA256 `767d7bc27ff0ae44d461ef08b2c2b7d51000dfd6ec7e7884741cd14b782e11e7`. Frozen coface data: `work/k12_ternary_coface_data.json`, SHA256 `119691eb6607afd11d8ae3a583b2442702c1595f95cc584b0d22ddce799d9678`. Exact replay reports `all_26_fillings_verified: true`, node range 327-477, and `whole_homology_claim: false`.

The resulting deduction removes every rank-ten degree-twelve generator of maximal minimum-basis index at most three from a homology representative. The remaining support has maximal index at least four. No complete rank-ten homology or K12 vanishing claim is made. The coface proof and full verifier were sent for independent whole-proof review before promotion.

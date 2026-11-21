# Exact Hurwitz–Hodge volume for the nonsplit Gaussian E8 sixfold datum

This package proves a rank-nine period map using a positive ninth Hodge intersection. The full proof is `e8_grr_section.tex`; bibliography items are in `e8_grr_bibitems.tex`. Statements D-E8-GRR-01–05 prove dominance without assuming connectedness. D-E8-GRR-06 uses the separately proved Gaussian reflection-normal-closure barriers to prove that a dominant component has full group and connected total curves.

The independently rebuilt exact results are

\[
\int\lambda_\rho^9=3009825/64,\qquad
\deg(\overline{\mathcal H}/\overline M_{0,12})=90296156160000.
\]

The root-swapped evaluation gives the same numbers. It is a check of the same recurrence, not a second mathematical derivation. The proof establishes that some component is dominant; it does not locate a specified explicit tuple in that component.

## Reproduction

Python 3, SymPy, and `python-flint==0.9.0` suffice. The locally installed flint path is a scratch dependency, not part of the deliverable; a standard installation is also supported.

```bash
python check_character_input.py
python exact_hodge_volume.py
python exact_hodge_volume.py --root involution --output exact_hodge_volume_other_root.json
```

The first command reconstructs all 112 Weyl-class matrices from the retained mathematical words and the explicit Cartan matrix, verifies their orders and orthogonality, checks the full character table and its tautological character, and recomputes all 224 Hodge weights from exact spectra. It does not require an external source file or an internet connection.

`build_character_input.py` records the separate source-extraction path: it specializes the CHEVIE author's polynomial Hecke-character table at `v=q=1`, using the previously reconstructed class-word data in the central research directory. Its source path and source hash are recorded in `character_input.json`. The full external library file is not redistributed here.

The exact volume program uses a newly written recurrence implementation and rational W(E8) character transforms. It does not import the rStation supplement, its character packet, its implementation, or an analytic rank certificate. Claimed values from the unrefereed lead occur only in post-computation comparisons.

## Source status

The GRR premise is **Tseng, Geometry & Topology 14 (2010), equation (7.3.7.2), p. 64**, including the marking-gerbe convention on pp. 19 and 21. The canonical-extension positivity premise is **Bakker–Brunebarbe–Tsimerman, Inventiones 232 (2023), Lemma 6.17** (48-page author version pp. 43–44). The curve-extension identification is recorded in the proof of **Catanese–Dettweiler, C. R. Acad. Sci. Paris 352 (2014), Theorem 2.1, p. 242**. The finite character table is the published CHEVIE package's author-maintained primary data, with immutable downloaded hash. Details and source-status corrections are in `SOURCES.md`.

Jarvis–Kimura 0810.2488 is retained for comparison and source auditing, **not** used as a published theorem premise. The initial search association with DOI `10.4310/HHA.2010.v12.n1.a9` was false: that DOI belongs to a different article. This was caught before the proof bibliography was finalized, and the published Tseng derivation replaces the preprint input.

No Severn, Markman, 032, or rStation theorem is assumed. This package does not itself construct the detecting algebraic cycles; that is handled by the separate branch-exponent supplier proof.

## Verification scope

See `CHECK_EVENTS.tsv` for authorship, actual check type, model metadata, and limits. Root independently read D-E8-GRR-01–05, checked the published formulas visually, and reran both exact computations successfully. D-E8-GRR-06 subsequently received whole-proof reviews from root and the imprimitive agent. The entire01–05 proof and exact reruns also received the imprimitive agent’s independent audit.

The standalone TeX wrapper is supplied. Compilation was attempted, but the available TeX installation lacks `pdflatex.fmt`; no compiled-PDF success is claimed. Source-integrity checks are recorded separately.

## Explicit nonsplit lattice comparison

`nonsplit_lattice_section.tex` and its bibliography give the complete new D-E8-LAT-01–02 proof. A Gaussian rank-six integral Hermitian lattice of signature(3,3), signed determinant class3 and polarization volumeΔ compares with H²⊥<1,−3> with both matrices cleared by some q≤69984Δ³. For source and target, N≤69984²(Δ_sourceΔ_target)³ clears both directions. With the conservatively proved source M=2|G|, this gives N≤69984²M¹⁸Δ_target³; middle-dimensional effective cycle degree scales by N⁶. A target stable under the order of conductor f gives the additional f³⁶ factor in N. These are fixed-field/determinant/order statements, not assertions uniform over all rational actions.

Run `python check_nonsplit_lattice.py` for the symbolic complement/sign-repair identities and twelve exact block examples with large integral shears. Initial checker failures from unsimplified SymPy matrix comparisons were fixed and retained in the event log. They did not change a mathematical formula. Root and sixfolds independently read the whole lattice proof; sixfolds also wrote an independent symbolic certificate. Primary downloaded documents are grouped under `sources/`.

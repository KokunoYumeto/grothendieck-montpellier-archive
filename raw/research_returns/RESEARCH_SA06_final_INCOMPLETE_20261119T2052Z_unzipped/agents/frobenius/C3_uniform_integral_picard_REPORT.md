# C.3bg status, sources, and reproducibility

## Certified scope

The final fragment is `C3_uniform_integral_picard_kernel.tex`. It proves an actual ordinary integral Picard restriction kernel containing `(Z/p)^min(3,N−1)` in every positive characteristic and every local dimension N≥3. All rings have an explicitly specified algebraizable normal strictly henselian model, regular puncture, and regular principal punctured divisor. The construction works first with the given thirty generic coefficients, then over Fpbar by a terminating finite-field specialization, hence over every algebraically closed characteristic-p field.

The N=3 statement is a lower bound on the rank of a subgroup. A k-linear map of rank two from the constant group (Z/p)^3 into Ga² can have Fp-rank three. We do not identify the entire kernel or infer a higher-Chow kernel. These integral examples leave the rational degree-one theorem intact. No originality or priority claim is made.

Both peers completely reread the typed proof and passed it before the final promotion. Their review files are `cycles/C3bg_uniform_integral_picard_independent_REVIEW.md` and `real_weil/C3bg_uniform_integral_picard_independent_REVIEW.md`. The root independently read the full draft and the original finite program/JSON, and requested final promotion with explicit source dependencies and affine row equations. Those additions change no proof scope. The draft file is now a supersession pointer.

## Exact opened primary-source ledger

- **OPENED, freshly read:** Brion, *Commutative algebraic groups up to isogeny. II*, full35-page author revision, Section3.2.3 equation(3.8), authorp23: https://www-fourier.univ-grenoble-alpes.fr/~mbrion/isogeny_II_rev.pdf . The integral original-category bifunctorial Ext=H1 statement and positive-characteristic paragraph precede the later characteristic-zero restriction. Original Oort source not separately opened.
- **OPENED, fresh local primary PDF:** Hacon–Patakfalvi arXiv1310.2996v2,20February2014, Lemma2.3.1/Proposition2.3.2 with proof,p12, and Lemma2.3.3pp12–13. Direct web opening failed; the complete primary PDF downloaded successfully via HTTP200 and the exact pages were read locally. Source path `sources/hacon_patakfalvi2014v2.pdf`; SHA256 `529f33f6dd1fad84db0e990f9e694ee019d9531c64675ecefb82081a9eeeb3ab`.
- **OPENED, fresh local primary PDF:** Brion arXiv1204.2628v2,29July2012, Theorem1.1p1 and full proof inSection5.1pp15–16. Applied to the coherent exterior algebra and primitive H1 of an abelian variety. Source path `sources/brion_coherent2012v2.pdf`; SHA256 `dc9073429c748291a58a2502218563668cdfb202c84f9c6f59e08e35dfbc1860`.
- **OPENED, freshly read:** Milne, *Jacobian Varieties*,12June2021 corrected author file, Theorem1.2p3 for actual Poincare bundle and Lemma9.5pp31–32 for H1 pullback: https://www.jmilne.org/math/xnotes/JVs.pdf . Original numbering retained by the author.
- **OPENED earlier and reused with exact scope:** Illusie1972 Theorem2.6/formula(2.7.2), printedpp166–167, characteristic-independent obstruction for lifting line bundles; full primary scan and errata were previously audited in C.3m and C.3bf.
- **OPENED earlier and reused:** proper formal existence, Popescu approximation, finite-presentation descent including specified isomorphisms, and smooth henselian lifting are the exact inputs of C.3w/az/bf. We do not replace them by K0 stabilization or an abstract Picard-functor point argument.
- **OPENED earlier and reused:** Elkik1973, unnumbered Picard corollary printedp573, applied to the actual punctures of the henselian pairs `(R,m)` and `(R/(f),m/(f))`.

Bibliographic entries are the existing canonical keys `D_BrionIsogenyII`, `D_HaconPatakfalvi2014v2`, `D_BrionCoherent2012`, `D_MilneJacobians2021`, `D_Illusie1972Torsors`, and `D_Elkik1973`. No duplicate entries are introduced. Acquisition timings and hashes are retained in `output/C3bg_source_acquisition.json`.

## Verification

The all-prime Hasse identity, nondegenerate normal-deformation form, projective-bundle calculation, finite image rank bound, and actual proper-curve lift are mathematical proofs. The program `code/check_uniform_integral_picard.py` supplies26 separate finite checks, with original run14:04:06.834323UTC and runtime0.000904321s. It explicitly demonstrates the rank-two/Fp-rank-three distinction.

The stronger auxiliary program `code/find_small_characteristic_picard_pairs.py` computes actual finite-field pairs in characteristics two and three. It calculates the Serre-dual normal boundary by a Cech lift and residue trace, producing cup matrixI3. It verifies all projective singular ideals symbolically, nonzero Hasse determinants, vanishing on the ten trivial normal directions, and the exact Fermat-five calibration. The full derivation and explicit equations are in `C3bg_small_characteristic_KS_NOTE.md`. The final strengthened run is14:12:45.842840UTC,1.363805424s. These auxiliary computations are not needed for the generic existence proof.

The standalone LuaLaTeX build uses `code/build_uniform_integral_picard.py`. Its final retained five-command run began14:11:40.106973UTC and took17.011319781s; all return codes are zero. The PDF has5pages and172022bytes. The log has no overfull boxes, missing citations, undefined references or fatal errors; two bibliography underfull boxes are retained. Complete build output/JSON are in `output/C3_uniform_integral_picard_kernel_build.*`. The root master receives its own independent build and visual QA.

Visual QA was completed at14:21:15UTC by individually inspecting all five rendered pages (`output/C3bg_QA-1.png` through `-5.png`). All equations, citations and bibliography entries are legible with no clipping, overlap, missing glyph or overflow. This is the owned standalone check, not a claim about the master rendering.

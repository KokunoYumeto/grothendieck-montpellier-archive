# Source log: G34 eightfold target

Access/check date: 2026-11-21. Model GPT-6 Astra Pro; effort inherited/unexposed. The scope of each reading is stated below. A theorem cited as a published input has not thereby been independently reproved.

## Unrefereed source, used only for verified numerical data and attribution

**S-SEV. Benjamin Severn**, *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(-3))*; Hexagon 2610.00387v2; internal v1.5, 21 October 2026. Unrefereed; portal labels the contribution primarily AI-generated. Main record: https://hexagonmath.org/2610.00387 . PDF: https://hexagonmath.org/pdf/2610.00387v2 . Source listing: https://hexagonmath.org/src/2610.00387v2/files . Raw TeX: https://hexagonmath.org/api/v1/works/2610.00387v2/source?path=weil-qsqrt3-v1.5.tex .

The portal's heading says *Weil classes on every abelian sixfold of Weil type for Q(sqrt(-3))*; the actual PDF title and TeX title include both sixfolds and eightfolds. The actual Theorem A (p.2) claims algebraicity for every split K-eightfold; Theorem B (p.2) claims it for all K-sixfold discriminants; Theorem C assumes full special unitary Hodge group and claims algebraicity on powers. These remain conditional if invoked as Severn's theorems. We do not invoke them.

Exact internal locators: Lemma4.4 (supplier repair); Proposition4.6 (transfer); Theorem5.1 (Brauer condition); Proposition8.5 (dominance criterion); Lemma9.1 (multiplicity); AppendixA (ten roots, basis, intervals and printed matrices). We extracted numerical inputs from AppendixA and rebuilt the quotient, pairings and all monodromies separately. We do not treat this attribution as an assumed theorem.

Immutable local files:

- sources/Severn2610_00387v2.tex: 108,698 bytes; SHA256 fc15af16599b399d8f111f6f0804916fdd39dc627e83adb5ff4e1788babc75ec. Its prefix agrees with the portal's advertised source hash.
- sources/Severn2610_00387v2.pdf: 492,267 bytes; SHA256 ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4. This served PDF carries the Hexagon watermark. The portal lists an auxiliary PDF of a different size/hash; we do not identify those bytes.
- sources/Severn2610_00387v2.txt: local pdftotext extraction, used to verify title/date/theorems and AppendixA against the downloaded file.

A normal source-ZIP request returned HTTP403. The independently accessible raw TeX and served PDF downloaded successfully. No unavailable ZIP or auxiliary PDF was inferred to have been read.

## Published inputs

**S-DAV. Donald M. Davis**, *Homotopy type and v1-periodic homotopy groups of p-compact groups*, Topology and its Applications 156 (2008), 300–321; DOI 10.1016/j.topol.2008.07.008. Author's published copy: https://www.lehigh.edu/~dmd1/TOPOL3486.pdf . Read §5, especially Theorem5.1, pp.312–313, its proof and matrices(5.2), and the root description on p.313. These give the standard G34 generators, invariant degrees, and 270+486 vectors. Our group identification uses containment and matching order, not just recollection of a classification table. Local PDF hash is in sources/download_manifest.json.

**S-CW. Paola Frediani, Alessandro Ghigi, Matteo Penegini**, *Shimura varieties in the Torelli locus via Galois coverings*, International Mathematics Research Notices 2015(20), 10595–10623; DOI 10.1093/imrn/rnu272. Author version https://arxiv.org/pdf/1402.0973 (v3, 27 December 2014). Theorem2.10 (author-version p.8) is the exact Chevalley--Weil formula used; §2 describes the cover families. Statement and its application to twenty involutions checked. We do not use their sufficient Shimura-subvariety criterion as a substitute for our rank calculation.

**S-DW1. Michael Dettweiler, Stefan Wewers**, *Variation of local systems and parabolic cohomology*, Israel Journal of Mathematics 156 (2006), 157–185. Author version https://arxiv.org/pdf/math/0310139 (v2). Read Proposition1.1, Lemma2.2 (author-version p.7), §2.2 and Theorem2.5 (p.12). These identify the cocycle quotient and braid pullback with the geometric local system, including the extra marking/intertwiner factor. Our finite marking/Kummer base change removes that finite factor. Local PDF/text saved.

**S-DW2. Michael Dettweiler, Stefan Wewers**, *Variation of parabolic cohomology and Poincare duality*, Seminaires et Congres 13 (2006), 145–164. Author version https://arxiv.org/pdf/math/0411119 ; publisher record https://smf.emath.fr/node/43624 . Theorem2.5 (author-version p.12) gives the right-module cup formula. This was read as a consistency source. The new dominance proof does not require an unproved convention conversion: the computed form is auxiliary, and actual isotropy follows from geometric polarized monodromy.

**S-SCHM. Wilfried Schmid**, *Variation of Hodge Structure: The Singularities of the Period Mapping*, Inventiones Mathematicae 22 (1973), 211–319. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/schmid.pdf . Read Theorem(4.12), printed p.233, for the multivariable holomorphic untwisting; Theorem(6.16), p.255, for the limiting mixed Hodge structure of the diagonal restriction. The new proof writes out why these imply F0 transverse to I and why a nonzero limiting tangent minor persists in the interior. Local PDF/text saved.

**S-SCHO. Chad Schoen**, *Hodge classes on self-products of a variety with an automorphism*, Compositio Mathematica 65 (1988), 3–32. https://www.numdam.org/item/CM_1988__65_1_3_0.pdf . Read simple-exponent definition and Theorem2.0 on p.11; Lemmas2.2–2.6 on pp.13–17; Lemma2.8 and Sublemma2.9 on pp.18–19; Corollary3.1 on pp.24–25. The printed prime-quotient choice in Lemma2.8 does not cover exponents m/2 when m has larger even divisibility. D-G34-04 supplies the needed vanishing directly, including the old center and new exceptional divisor. Local PDF/text copied from the sixfold agent's downloaded primary source.

**S-SER. Jean-Pierre Serre**, *Linear Representations of Finite Groups*, Graduate Texts in Mathematics 42, Springer, 1977, §10.5, Theorems19–20, pp.78–79. Publisher: https://link.springer.com/book/10.1007/978-1-4684-9458-7 . Primary book scan hosted by University of Rochester: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-Reps.pdf . Brauer's integral induction theorem is used as published background. Its exact consequence for the full character group is proved in D-G34-06. The large scan exceeded the web-reader limit; theorem numbering and statement were cross-checked, but no full independent proof of Brauer induction is claimed.

**S-MIL. J.S. Milne**, *Lefschetz classes on abelian varieties*, Duke Mathematical Journal 96 (1999), 639–675. Author version https://www.jmilne.org/math/articles/1999aP.pdf ; author record https://www.jmilne.org/math/articles/1999a.html . Read Lemma3.1 and Theorem3.2 (author-version pp.14–15), Lemma3.5 and the invariant-theory discussion, Proposition3.6/Remark3.7 (pp.15–18). Theorem3.2 provides algebraicity of the U-invariant contraction after S(J)<=U. The quantitative degree construction uses the classical invariant-theory statements to choose degree-two generators from Q[G]. Local PDF/text saved.

**S-SGA. Artin--Grothendieck--Verdier, SGA4**, Tome3, LNM305, Springer1973: ExposeXII, Theorem5.1(iii) (proper base change); ExposeXVI, Theorem4.1 (comparison with classical topology). Exact locators cross-checked against Luc Illusie's author-hosted review, Theorem1.5, https://www.imo.universite-paris-saclay.fr/~luc.illusie/wolfson2.pdf , and Beilinson--Bernstein--Deligne, *Faisceaux pervers*, Asterisque100 (1982), p.150, https://archive.numdam.org/item/AST_1982__100__1_0.pdf . SGA4 French reedition at https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/ timed out during this run. We use the standard theorems as published background, not as newly reproved statements. In D-G34-04 they can be applied first with finite coefficients of residue characteristic prime to m, then with characteristic-zero coefficients.

## Supplied project inputs used and rechecked

- HODGE_DIVISION_ATTACK_20261121.md, §2.4, PropositionO', CorollaryO'', LemmaDom: read; used as supplied established reductions. In particular the genus-zero dimension inequality is only necessary.
- HECKE_DIV.tex, S1–S3: previous source audit read with its stated conditional status; no missing earlier scripts were assumed present.
- HECKE_DIV.tex, SQ1–SQ7: full quantitative proof read and checked during this run. Used to obtain D8(Delta) once D-G34-01–06 supply the geometric premises. This is not a citation to Severn for those premises.
- HODGE_DIVISION_ATTACK_20261121.md, §1,R4/TheoremW and §2,TheoremD: used as the user's accepted degree-to-division and bounded-cycle closedness results; not reproved in this subtask.

## Computation provenance

Command: python g34_reconstruct.py --group-order . Python3.12.14, Sympy1.14.0. Sympy is used only for exact permutation-group order; arithmetic over Q(omega), cocycle reductions, nilpotency, form invariance, all principal minors and the rank minor are computed independently with fractions. The stabilizer-chain orbit lengths are 756,80,12,9,6. The product is39,191,040. The complete output is g34_reconstruction_result.json. SHA256SUMS.json records current source/code/data hashes.

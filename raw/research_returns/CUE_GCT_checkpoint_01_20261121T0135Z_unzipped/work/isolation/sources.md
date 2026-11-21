# Isolation sources and exact locators

All source paths below refer to the supplied archive extracted once to `sources/`. Existing results are not claimed as new. The dates in bibliographic entries follow publication/version dates, not regenerated PDF title-page timestamps.

## I-B01 — new graph input

Hoza, W. M. (2026). *NL = UL* (ECCC TR26-323). Supplied file `ECCC_TR26-323_Hoza_NL_equals_UL.pdf`.

- Definition 1.2, printed p. 2: internal-vertex path weights; uniqueness for all reachable vertex pairs.
- Theorem 1.3, printed pp. 2–3: one seed per fixed simple graph; seed length O(log(WN)); logarithmic-space computability; polynomial integer magnitudes.
- Formula (1), printed p. 3: rho_x(a,i)=sum_j 6^(nu_2(i)+ell-j) C(a)_j x_j.
- Theorem 2.4, printed p. 5: failure probability at most 2^(-d) W^4 N^2.
- Used as the supplied theorem. This track did not claim a formal or full independent verification of the theorem.

## I-B02 — basis isolation

Agrawal, M., Gurjar, R., Korwar, A., & Saxena, N. (2014). *Hitting-sets for ROABP and sum of set-multilinear circuits* [Preprint]. arXiv:1406.7535v1. https://arxiv.org/abs/1406.7535

Supplied source: `LIT_AGKS_hitting_sets_ROABP_basis_isolation/deltaDistanceSICOMP.tex`.

- Theorem 1: source label `thm:ROABPhs`; source lines 241–246; PDF p. 2.
- Definition 5: basis isolating weight assignment; source lines 902–919; PDF p. 7.
- Lemma 6: source label `lem:basisIsolation`, lines 927–988; PDF pp. 7–8.
- Observation 7: `obs:smallerWeight`, lines 1005–1028; PDF p. 8.
- Lemma 8: `lem:weightFunction`, lines 1040–1055 and proof thereafter; PDF pp. 9–11.
- Additional I-17 context: Theorem 3 (`thm:invROABPHS`), printed pp. 5 and 19; Lemma 27 (`lem:bSConc`), printed p. 22, source lines 2354–2400, invertible-constant-term matrix concentration. Primary PDF refs `turn317946964view0`, `turn814896166view0`, `turn814896166view1`, `turn814896166view2`.
- Primary PDF inspected: https://arxiv.org/pdf/1406.7535 ; web reference `turn166538694view0`; targeted findings `turn944129952view0`, `turn944129952view1`.

## I-B03 — matrix invariants

Forbes, M. A., & Shpilka, A. (2013). *Explicit Noether normalization for simultaneous conjugation via polynomial identity testing* [Preprint]. arXiv:1303.0084v2. https://arxiv.org/abs/1303.0084

Supplied source: `LIT_Forbes_Shpilka_explicit_Noether_normalization_matrix_invariants/pit-nn.tex`.

- Theorem 1.3 (`generatinginvariants`): trace generators of words of length at most m² in characteristic zero.
- Theorem 1.13 (`thm:integral subring`) and Corollary 1.14: quasipolynomial separating invariants/integral subring.
- Theorem 1.15 (`thm:orbit intersection`): deterministic NC orbit-closure intersection already follows from white-box PIT.
- Construction 3.1 (`roabpinv`), source lines 510–516: M(x), trace-generating polynomial.
- Lemma 3.2 (`diffofinv`), lines 520–526: difference has width 2m².
- Lemma 3.4 (`roabpcoeff`), lines 540–567; Corollary 3.6 (`reducetoroabp`), lines 581–587.
- Construction 3.7 (`const:hittingset`), lines 591–595.
- Theorem 3.8 (`thm:sepinv`), lines 599–613: m²|H| homogeneous separating invariants.
- Theorem 3.9: specialization of Derksen–Kemper Theorem 2.3.12, homogeneous separating invariants give integrality over algebraically closed characteristic zero.
- Corollary 3.10: integral-subring consequence for the same set.
- Primary PDF inspected: https://arxiv.org/pdf/1303.0084 ; web reference `turn166538694view1`; exact-number findings `turn944129952view2`, `turn944129952view4`.

## I-B04 — revised GCT V numbering

Mulmuley, K. D. (2017). Geometric complexity theory V: Efficient algorithms for Noether normalization. *Journal of the American Mathematical Society, 30*, 225–309. https://doi.org/10.1090/jams/864

Supplied source: `LIT_Mulmuley_GCT_V_Noether_normalization/main.tex`, matching arXiv:1209.5993v5 (26 May 2016).

- Theorem 5.14, source label `tequisdit`, lines 3094–3110; PDF pp. 45–46: strengthened general PIT versus strict e.s.o.p. for universal-circuit orbit closures. This is stronger than ordinary ROABP PIT and has an infinitesimal/border requirement.
- Section 7.5 and Lemma 7.9 (`lforbes`): replace symbolic determinant testing by ROABP testing for matrix invariants.
- Theorem 7.1 (`tmatrixstrongform`), Theorem 7.2 (`tintroorbitclosureNew`) and Theorem 7.7 (`tsepderksen`): exact scope of matrix normalization and already-known orbit-closure algorithms.
- Primary PDF inspected: https://arxiv.org/pdf/1209.5993 ; `turn477504142view0`; theorem-number findings `turn871722820view0`, `turn871722820view1`.
- A reference in the 2013 Forbes–Shpilka paper to an earlier GCT V Theorem 1.6 must NOT be copied as the current theorem number. In the supplied revised source Theorem 1.6 is a different theorem about constant-dimensional groups.

## Independent source check for root finding G-07

Leal, M., Lozano Huerta, C., & Vite, M. (2024). The Noether–Lefschetz locus of surfaces in P³ formed by determinantal surfaces. *Mathematische Nachrichten, 297*(12), 4671–4688. https://doi.org/10.1002/mana.202400132

Primary preprint: https://arxiv.org/pdf/2303.09028 , version 3 (1 November 2024), inspected in this independent review.

- Definition 2, PDF p. 2: closed determinantal locus det(a,b).
- Proposition 1.1, PDF p. 4: irreducibility and nonempty smooth locus.
- Theorem 2, PDF pp. 3 and 15: prime divisor F1 degree 320112.
- Table 2, PDF p. 13: F1 has a=(5,5,5,5), b=(6,6,6,6), hence linear entries.
- Section 4.1, PDF p. 15 immediately before Theorem 2: P_(20,2)=(1/2)D_(23,14).
- Primary web reference `turn280289537view0`; exact locators `turn520265669view0`, `turn520265669view2`, `turn520265669view3`.

## I-B05 — arithmetic support and logarithmic-space counting

Allender, E., & Ogihara, M. (1996). Relationships among PL, #L, and the determinant. *RAIRO–Theoretical Informatics and Applications, 30*(1), 1–21. https://doi.org/10.1051/ita/1996300100011

Primary scan inspected: https://www.numdam.org/item/ITA_1996__30_1_1_0.pdf

- Section 2, printed p. 4: halting logarithmic-space machines and their accepting-minus-rejecting gap.
- Theorem 1, printed p. 2: GapL and logarithmic-space functional reductions to integer determinant; following paragraph explicitly passes through iterated multiplication of {0,1,-1} matrices.
- Section 5, Definition 2, printed p. 11: C_=L defined by gap zero.
- Theorem 14, printed p. 12: singular integer matrices are C_=L-complete.
- I-12 proves its particular ROABP formulation directly. It does not assert that coC_=L is different from NL or that arbitrary polynomial-time algebraic support manipulation is impossible.
- Primary web references: `turn392175736view1`, `turn776322203view2`, `turn647216830view0`.

## Independent source check for P-08

Lagarias, J. C., & Odlyzko, A. M. (1977). Effective versions of the Chebotarev density theorem. In A. Fröhlich (Ed.), *Algebraic number fields* (pp. 409–464). Academic Press.

Primary-text TeXromancers transcription inspected: https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf

- Theorem 1.1 and Corollary 1.2, transcription p. 4; equation (1.4): GRH for the Dedekind zeta function of L alone, an effective absolute constant, and an unramified prime ideal for every conjugacy class with norm bounded by c₂(log Δ_L)²(log log Δ_L)⁴.
- The parenthetical immediately following (1.4) handles L=Q by p=(2).
- The source's full Chebotarev proof was not independently checked. P-08's entire reduction proof was independently read and checked; see `independent_review_purity.md`.
- Primary web reference: `turn392175736view0`.

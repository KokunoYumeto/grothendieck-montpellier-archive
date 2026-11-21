# HODGE_SIGN — implications for the programme

Run HODGE_SIGN-20261121, 21 November 2026. Finding IDs refer to the checked paper. Alpöge's RH and Dirichlet-GRH are stipulated theorem inputs, not objects of an authenticity or build audit. No specific Masullo theorem is an input.

## 1. What the main proof establishes

**SG-08–SG-11 close the geometric sign-only proof.** For a smooth affine scheme U of dimension d over F_q and a lisse sheaf F, generic weak Lefschetz and duality give a Gysin surjection at the border degree. After the higher terms cancel, the signed remainder is the trace of

H_c^d(U,F)^{tensor k} plus ker(H_c^{kd−1}(Y,F^{box k})(−1) → H_c^{kd+1}(U^k,F^{box k})).

The second summand is an actual Frobenius module. Finite Noether normalization and generic per-vertex potentials preserve the path Fourier estimate. Positive inverse-root multiplicities, Parseval, and tensor amplification prove the affine middle upper bound. Hyperplane induction and stratification prove the compact-support upper bound for constructible sheaves. Duality proves the expected absolute values for smooth proper varieties with pointwise pure lisse coefficients.

These are reconstructed proofs of known finite-field weight conclusions. The argument uses no Hodge standard conjecture and no stipulated global RH. It supplies neither a positive intersection form nor semisimplicity. Algebraicity, rationality, integrality, and independence of ell are not silently folded into the analytic power-sum lemma.

## 2. Grothendieck's archive

| Source | Change justified in this run | Finding IDs |
|---|---|---|
| Cote 16, scans 034,036,038,040 | The restriction/Gysin and evanescent-kernel machinery supports the sign-only proof. Its effective multiplicity sign is not the signature of the evanescent intersection pairing. | SG-01, SG-08–11 |
| Cote 16, scans 049–050 | No algebraicity or index conjecture is proved by parity. Scan049 explicitly adds I(X×X) for semisimplicity. Scan050's C and A labels are not silently renamed using absent earlier definitions. The absolute-value conclusion is reached by a different use of hyperplane machinery. | HS-05, SG-03, SG-10 |
| Cote 16, scans 014–018 | Distinguish ordinary contraction D from normalized lowering Lambda_N. The normalized universal ring is a product of full matrix rings with the specified grading. Integral exterior hard Lefschetz and Wilson factors have the stated range and factorial corrections. | SL-01–04, SL-08–09 |
| Cote 44, scan002 Theorem4 and scan008 margin | The assertion concerns the canonical self-duality of an algebraic intermediate Jacobian, not an Arakelov pairing. Curve Jacobians and the zero-Jacobian example are known cases; the primitive signs and higher comparison remain additional data. | AR-04 |
| Cote 44, scan004 Theorem5 and local-variant margin | The displayed raw higher-cycle height identity is false under all displayed assumptions. A primitive cycle on P2×P2 restricts to zero on the generic smooth incidence threefold while its square is3; the pencil has smooth base and geometrically integral nodal fibres. An ellipsis in the source is not filled in by conjecture. | AR-01 |
| Cote 34, scans053–063 Theorem1.1 | The all-open-subgroup quantifier supplies the finite-abelianization property used in the corrected nonabelian statement. The original theorem is used as cited background, with curve-RH/spreading source locators. | Q3-02, Q3-03, Q3-08 |
| Cote 34, scan064 Remark1.17, struck | Literal openness in pi-prime is refuted. The canonical closure[P,H] is open in H; with a specified section the cross-commutator subgroup is open in soluble H of finite derived length. Trivial outer action gives another intrinsic finite-kernel version. | Q3-01, Q3-04–07 |
| Cote 34, scan074 (2.5.4)–(2.5.6) | The actual weight argument is that a Frobenius with no eigenvalue1 makes finitely generated ell-adic coinvariants finite. Curve purity already suffices with the source's reductions. | Q3-02 |

TRANSCRIPTION_NOTES.tsv records mathematically forced or motivated repairs with confidence qualifications. None is claimed to have been checked against original manuscript images. In particular, the high-codimension counterexample may expose a missing qualification in an ellipsis rather than a wrongly transcribed symbol.

## 3. Existing BRIDGES rows

| Prior run and row | Updated status |
|---|---|
| BRIDGES/Q03 | Replace “open” by “literal statement refuted (Q3-01); intrinsic corrected openness proved (Q3-04); section-dependent soluble corrected openness proved (Q3-05–06); optional intrinsic outer-action version proved (Q3-07).” Exact erased wording is a manuscript-reading issue. |
| BRIDGES/Q04 | Remains settled. Q3-02 isolates the precise finite-module argument. No higher-dimensional RH is needed for the source's curve reduction. |
| BRIDGES/Q05 | Remains open in its general cycle-theoretic form. The new reconstruction supplies purity without settling B, Hodge type, cycle-class injectivity, or correspondence-algebra semisimplicity. |
| BRIDGES/Q01 and Q02 | No general positive-weight arithmetic L-function RH is obtained. Only explicitly identified abelian Artin–Tate factors retain the prior stipulated-RH transfer. SG-02 computes the relevant factor zeta(s−3). Other motives remain outside this task's proved transfer. |
| BRIDGES/Q06–Q08 | Not treated; their existing status is not changed by this run. |

## 4. SA06 and the suggested bridges

Every supplied C.1 row, a through q, is individually listed in the paper and QUESTIONS.tsv. SG-06 and SG-10 give the requested absolute values for every smooth projective finite-field fibre of an arithmetic spread of the varieties described there. This does not independently certify the absent full C.1f–q proofs and does not recover a Griffiths kernel from spectral data.

- **SA06/C.1a–c and C.1e–q:** the cycle-class-kernel, algebraic-equivalence, radical, and semisimplicity questions keep their own hypotheses and conclusions. The finite-field weight assertion is now obtainable from the explicitly reconstructed sign-only argument. Prior complex counterexamples are not turned into finite-field counterexamples by specialization.
- **SA06/C.1d:** the curve/surface index route is already known; the new parity proof is a second route to the spectral conclusion, not an identification of pairings.
- **SA06/E.3u:** the ambient split sixfold has primitive motive Q(−3), square−2, local eigenvalue q3, and global Tate factor zeta(s−3). Its class restricts to zero on every smooth positive-degree hypersurface in Q6 (SG-07). Therefore that ambient factor does not itself describe the variable H5 of the hypersurface or the Lawson kernel on its product with an elliptic curve. Purity for smooth finite-field fibres of the latter varieties follows from SG-10. The Nagel/Walker nonvanishing input was not independently verified and is not needed here.
- **Fable suggestion4:** the proposed identification of parity with an index form is refuted. The specified hexagonal CM elliptic powers do have divisor-generated algebraic cohomology and the known Milne positivity on that space (SG-04). The same proof covers complex CM elliptic powers and finite-field elliptic powers. It does not cover arbitrary CM abelian varieties or arbitrary higher-genus curves with CM Jacobian.
- **Fable suggestion6:** the bare arithmetic and integral identifications do not follow. The actual slope/divisibility inequality is AR-05; the actual local period bound and parameter calculations are SL-06. The integral SL2 counterexamples and Frobenius normalization obstruction are SL-05 and SL-07.

## 5. H8 and H9

**WARGAME/H8, block statement and (i)–(iii).** SL-01 proves the integral decomposition into inclusion-matrix blocks. Wilson's displayed diagonal requires t≤t+m≤v−t; all hard-Lefschetz blocks lie in this range. Its diagonal need not already be a Smith normal form. SL-02 proves the stated divided-power isomorphism cases, the degree-two cokernel Z/(n−1), and the criterion that all ordinary powers are isomorphisms exactly when n! is invertible. This is an integral cohomology statement, not a proof that the divided powers are algebraic Chow classes. The primitive scalar in the hunch must be r!d!/(d−r)!, with (r!)² only at the endpoint d=r.

**WARGAME/H8(iv).** An associative-order index needs a specified ambient order and lowering normalization. SL-08 determines the normalized full matrix ring. The additional SL-09 calculation specifies the ordinary-contraction order and computes it in small ranks, rather than transferring Wilson's one-map indices to an unspecified order. None of these orders is identified with the actual theta-lift lattices by the occurrence of an Arthur block.

**WARGAME/H9(a).** Refuted in codimension two by AR-01. Geometric integrality of fibres does not eliminate higher vertical cycles. The classical surface divisor formula and its local corrections keep their actual hypotheses.

**WARGAME/H9(b).** The claimed deduction through the raw height formula fails. The example also shows that primitive ambient cycle classes need not inject into the generic algebraic Jacobian. A new equivalence must specify the quotient, admissible extensions, vertical corrections and canonical pairing; it is not obtained here by assuming the corrected formula.

## 6. Which conditional literature statements become theorems?

The only new use here of the stipulated global RH is an explicit specialization: the nontrivial zeros of zeta(s−3) have real part7/2. The corresponding local eigenvalue q3 was already forced by the Tate motive and requires no global RH. Dirichlet-GRH is not used to infer a number-field RH for the quintic H3 or for an unspecified CM motive.

No conditional general Hodge-standard statement in Milne2002 Theorem3.3 loses its Hodge-conjecture hypothesis. Remarks3.7–3.8 already give the Lefschetz-class/no-exotic-class cases used in SG-04. Moriwaki's divisor theorem, Kunnemann's specified projective-space result, and Bost's slope inequality remain cited theorems in their own hypotheses. No unspecified higher arithmetic positivity conjecture becomes a theorem. No result is labeled conditional on Masullo: no numbered Masullo theorem was supplied or used.

## 7. Explicit boundary for a future integral comparison

To ask a new normalized comparison question beyond the refuted unqualified identification, provide or construct a geometric realization of the intended automorphic chain, its degree/Tate normalization, the individual integral lattices, and an intertwiner carrying every actual lift matrix to the specified Lefschetz divided power. Stabilizer denominators and the final period functional must be included. SL-06 supplies the true conditional scalar bound with those data visible; SL-01–03 and SL-09 supply exact comparison invariants once a map and ambient order are specified.

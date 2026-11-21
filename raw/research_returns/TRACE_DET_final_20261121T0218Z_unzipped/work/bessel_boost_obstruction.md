# DET-19: natural boost covariance audit and proof notes

Date: 2026-11-21. Author: GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_bridge_check.

The complete proof is in `work/paper_bessel_boost.tex`. This is a new mathematical consequence of the exact retained source hypotheses, not a claim that the historical note proposed this flow identification.

## Exact source inputs actually read

All Lean paths below are relative to `work/external_lean/lean/src`.

- `Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MatrixOfBesselTwoSidedAction.lean`: read lines 1–135. Line 15 makes `opn` the Euclidean operator norm. Lines 40–55 define `coef`, `SchurH`, the orbit span `DD`, `Decay`, and `Std`. The exact bound is `|<v,sigma(g)u>| <= C opn(g)^(-a)` for u,v in DD, with `a >= 2 n^5 > 0` and `k >= 1`. Lines 119–121 give the retained `IsEll` factorization.
- `Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean`: read lines 13–38. Lines 23–28 define the representation's norm preservation, vectorwise continuity and irreducibility. These, not a general unproved decay theorem, are the representation inputs used.
- `Formalism/FormalDegreeBessel/StatementG.lean`: read lines 1–52 in the cached exact source copy. Lines 20–24 give the matrix Hpk: the middle coordinates r and r+k have signs +1,-1 and are orthogonal to all other coordinates. This verifies the actual boost subgroup.
- `work/paper_bessel_projector.tex`: read the complete source-hypothesis/common-space discussion, full isometry proof, complete infinite-dimensionality proof, and trace-class construction. DET-19 uses the already-proved isometry u -> eta_u and the support of nu on G. It does not add an assumption of right-invariant quotient measure or an action on all ambient L².
- `work/paper_arithmetic_kernel.tex`: the complete final DET-16 proof was author-read; its independent reviewer has now reported a full PASS. Its bounded-k iff RH criterion and exact Cesaro atom formula are the arithmetic inputs. The corrected Ramaré formula and complete global Landau argument are retained cited inputs as documented there.

## Results and complete proof structure

Let g_t be the real cosh/sinh boost on the two named source middle coordinates, identity elsewhere. It preserves Hpk and is a continuous one-parameter subgroup. The Euclidean orthonormal eigenvectors `(e_r ± e_(r+k))/sqrt(2)` have eigenvalues exp(±t), so `opn(g_t)=exp(|t|)` exactly. Thus source decay gives exponential vanishing of coefficients on DD.

The orbit span DD is dense by source irreducibility. Approximating two arbitrary vectors by DD vectors and using unitarity bounds the coefficient error uniformly in t. This extends vanishing to every coefficient of `V_t=sigma(g_t)`, without extending a uniform exponential rate.

Every finite-rank trace coefficient is a finite sum of these coefficients. The inequality `|Tr((T-R)V_t)| <= ||T-R||_1` passes both continuity and vanishing to any T in S1. Positivity of T is not needed.

An eigenvector has a nonvanishing coefficient. A finite-dimensional invariant subspace has a fixed positive sum of squared coefficients of its restricted unitary matrices, contradicting their termwise vanishing. If a nonzero compact Q commutes with all V_t, then Q*Q does too and its largest positive eigenvalue has a finite-dimensional nonzero invariant eigenspace. Hence the entire compact commutant is zero, already for this one-parameter action.

The arithmetic kernel cannot vanish at infinity. If it did, it would be bounded; DET-16 and STEP6's Landau proof then imply RH. Its positive atomic formula would have a nonzero Cesaro coefficient at every positive Xi ordinate, whereas every bounded function vanishing at infinity has all these coefficients zero. The contradiction proves the claim without assuming RH in the conclusion.

Under RH the arithmetic translation representation has a complete eigenbasis, with one dimension per signed atom in the cyclic model and the recovered multiplicities in its enlarged model. Any bounded intertwiner into the boost representation sends each basis vector to a nonexistent boost eigenvector, hence is zero. In particular there is no injective bounded or unitary flow intertwiner.

The Bessel isometry has a closed image B_sigma. For source orbit vectors and canonical coefficient representatives on G,

`eta_u(x g)=eta_(sigma(g)u)(x)`.

This transports the unitary group to B_sigma and supplies the exact right-translation covariance on its dense coefficient subspace. Nothing is inferred about all equivalence classes in ambient `L²(nu;Wp)` or about right-invariance of nu. The statements concern this actual isometric image.

## Scope

The construction of B by positive weighted source projections under RH survives. It cannot commute with this natural boost; its own pure-point arithmetic flow is a different unitary group on its spectral space. The proof therefore narrows a possible finite-matrix/flow dictionary and does not invalidate the constructed determinant or finite trace-norm approximants. A different flow or a non-equivariant embedding is not excluded.

Independent whole-proof review of the saved TeX by `/root/masullo_spectral_bridge` reports PASS with no correction. Its separate record is `work/bessel_boost_independent.md` and `work/bessel_boost_independent_events.tsv` (eight events). The checked TeX SHA256 is `33eca819abaefc35b349249d29d8224bf7fba763a181dba03f2f74eadf2f1a74`. No external general representation-theoretic vanishing theorem, Bochner theorem, or unproved quotient-translation assertion is used.

# D-OL22–24: odd-natural genuine Spin

Recorded at **2026-11-21 23:15:25 UTC**, read from the clock tool.
Author: `/root/imprimitive`, GPT-6 Astra Pro; reasoning effort inherited and
not separately exposed; run HODGE_DIVISION.

## Frozen mathematical object

`spin_odd_extension_section.tex`, SHA-256
`a5b4c58088ddd71709ff7067670bd9d2ce71f25a02a0710cdfb557db79ca9e44`.

The author has read the complete proof and complete certificate program.
The new universal argument passes that author check. Independent whole-proof
review has been requested from `/root/g34_eightfolds`; root review is pending.
This is an authored derivation, not an independently originated re-proof.
The text has not been promoted into the main paper by this author.

Theorem D-OL22 treats a fourth-order natural SO operator over F3 whose
square is a negative reflection, including the coset outside Omega. Its
two-plane Heisenberg quotient has fixed dimensions N−1, 2N−2, N−1.
All linear-weight sectors and all nonlinear carrier/multiplicity sectors
are retained, giving support at least 7a/32. D-OL23 proves the complete
normalizer/all-orders bound and isolates only projective negative
reflections below the larger support threshold. D-OL24 uses the actual
generating inertia tuple to exclude rank-nine sources with arbitrary
mixed odd-natural Spin factors of dimension at least 1135. It imposes no
ordinary-character, selfduality, transitivity, or determinant hypothesis.

The mixed-parity consequence explicitly also invokes sixfolds' D-OL21.
That dependency is separate and is not silently certified by this record.

## Exact finite supplement

`check_spin_odd.py`, SHA-256
`5f281945662eb61b08791c5da1fd990da91bd44e816246e8c44d09dae45a4f3b`.

`spin_odd_checked.json`, SHA-256
`dd1646075122be046803968da54c7ce82786833f677523f38f2f283a8f390700`.

The first complete execution passed, runtime **0.904313123 seconds**.
The output records the frozen proof hash. All arithmetic is integer
arithmetic modulo three or exact rational arithmetic. No approximate
eigenvalues, interval tolerances, external character tables, or imported
arithmetic checkers are used.

Actual checks:

- Five natural models, with complementary dimensions 3, 5, 7, 9, 21;
  exact isometry/determinant/square and all fixed-space dimensions.
- All 7,380 fixed dual maps in the four smaller models; every nonzero
  such map has rank two.
- 120 deterministic radical group-law, exponent, isometry, and exact
  conjugation cases.
- 14,368,590 exact root-count convolution terms for degree-27 and
  degree-243 carriers, including the fourth-power identity.
- 1,240,029 exact Weyl covariance entries, including all 729 Weyl
  labels in the degree-27 carrier.
- Exact carrier fourth-root multiplicities `(9,9,6,3)` and
  `(81,81,45,36)` in the order `(1,−1,i,−i)`.
- A natural dimension-seven order-four matrix outside Omega, with
  spinor norm certified by two actual reflection norms; a separate
  dimension-nine order-eight matrix with the required square-support
  property. These are matrix witnesses, not claims about exceptional
  low-dimensional Spin classification.
- All displayed rational endpoint constants, the large-dimension degree
  lower bound, and TeX display/control-character/tag checks.

There was no failed run or rejected mathematical estimate in this new
certificate. Its finite cases support the new formulas; they do not
replace the universal proof, published character estimate, Clifford
lifting construction, Witt theory, or group-generation argument.

## Exact dependency interface

Sixfolds' complete written D-OL19 and the parity-free opening of D-OL20
are in
`/workspace/scratch/796f50e61a8b/HODGE_DIVISION_work/agents/sixfolds/spin_lifting/spin_even_extension_draft.md`.
The version read has SHA-256
`15d15aabe321511781318378598c2f6c956db1c39e5ad168b27b3592c3c6e9f6`.

The complete lift/radical interface has been checked here: even Clifford
scaling, odd bimodule covariance, represented-kernel preservation by
perfectness, exact projective orders, unique odd-p radical lifts, full
inverse-image Levi action, opposite-lift generation, and the degree
bound for all Spin characters. This is a targeted verification of the
dependency interface, not a claim that this author has independently
audited every even-natural support/source conclusion D-OL20–21.

The already reviewed D-OL07, D-OL09, D-OL12–18 and D-HOS01 supply the
natural normalizer coverage, semilinear descent, signed radical formulas,
quadratic orbit counts, two-plane generation, and exact Weyl basis. Their
complete applicable arguments have been reread during this run. The new
proof explicitly replaces the ordinary-character degree premise and
does not reuse the full-orthogonal reality argument for genuine Spin.

## Primary source record

1. **Maria J. Wonenburger, The Clifford Algebra and the Group of
   Similitudes**, Canadian Journal of Mathematics 14 (1962), 45–59,
   DOI `10.4153/CJM-1962-004-1`.
   Published primary PDF:
   <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F0429CDCBD14931AA864EB1135F4F24E/S0008414X0001751Xa.pdf/clifford_algebra_and_the_group_of_similitudes.pdf>.
   Full invoked tensor-ideal/even-algebra calculation, Part II,
   printed pp.48–49, and surrounding pp.47–50 were read. The text
   explicitly treats even and odd dimensions in the needed construction.
   The unrestricted whole-Clifford extension theorem is not invoked.
   The published PDF was reopened in this run. Local source SHA-256
   `f414198edb12f3f2fb39a6b4e201c9c797e4a03e01d68490c71a762160944d27`.
   Reuse the sibling-supplied bibliography key `SF:Wonenburger1962`.

2. **M. Larsen, A. Shalev and P. H. Tiep, The Waring problem for
   finite simple groups**, Annals of Mathematics 174 (2011), 1885–1950,
   DOI `10.4007/annals.2011.174.3.10`.
   Published primary PDF:
   <https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf>.
   The exact natural-support conventions and gamma_q are p.1907;
   Theorem4.3.6 and formula(4.3.2) are pp.1917–1918; the exact Spin
   sequence and quasisimple interface are Step1 pp.1918–1919;
   Remark4.3.7 p.1923 permits the restricted scalar set mu_2 for Spin.
   The full proof pp.1918–1923 has been read during this run; the
   particular pages just listed were reread for the present derivation.
   Formula(4.3.2) was freshly checked visually: the exponent is
   sqrt(N/7), and N>=567 permits exponent9. No OCR-only decision was
   made about that radical. Local source SHA-256
   `dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e`.
   Existing key `HOS:LST2011`.

3. **D. E. Taylor, The Geometry of the Classical Groups**, Heldermann,
   1992; author's corrected version:
   <https://www.maths.usyd.edu.au/u/don/papers/gcg.pdf>.
   Lemma10.2, Corollary10.3 and the subsequent Hermitian hyperbolic
   decomposition, printed pp.116–117, were freshly read in full.
   The complete applicable Witt, quadratic-count, spinor-norm and
   perfectness arguments were read earlier in this run and are retained
   as the exact dependencies D-OL06–18. Local source SHA-256
   `825201a4831659f957bf30156f04e85ab3746c01d942c670284071c68b41e30e`.
   Existing key `OS:Taylor1992`.

4. **C. H. Li and B. Xia**, Memoirs AMS279 (2022), no.1375;
   author version arXiv:1408.0350v3, dated25February2016.
   The whole applicable Section2.2.2/Table2.1, printed p.14, has
   been read, together with the complete D-OL07 natural-image
   order/kernel proof. This is an author version of the published
   work; a fresh publisher-page comparison is not claimed.
   Existing key `HES:LiXia2022`.

Known published results are cited with their exact scopes. The new
fourth-order calculation and its all-orders/source consequences are
proved in full rather than attributed to those sources.

## Reproducibility

Run `python check_spin_odd.py` in this directory or use its absolute path.
The only nonstandard library is NumPy; eigenvalues are reconstructed by
exact root counts. The reported runtime is observational and need not
match on a rerun. The proof hash is the mathematical binding. No copied
third-party PDF is needed in the deliverable; existing source caches are
excluded from packaging by the parent.

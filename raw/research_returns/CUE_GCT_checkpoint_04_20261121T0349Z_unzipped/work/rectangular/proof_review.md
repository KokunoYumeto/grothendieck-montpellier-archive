# Whole-proof review of R-01–R-18

Reviewer: `/root/rectangular_bridge`, GPT-6 Astra Pro, inherited effort
(not exposed), run CUE_GCT-20261121, 2026-11-21.

Each complete statement and complete proof in `findings.tex` was read
after drafting. This is a targeted proof check, not a formal certificate
or an external referee report. The root separately reported a complete
read of R-01–R-08 with no mathematical gap found; that independent
agent should record its own event.

- **R-01:** Rechecked rectangle parameters `N=d,L=n,K=(a−1)n`, the
  use of Kronecker symmetry, determinant twist, hook denominator, and
  nonzero denominator `D_lambda(a)`. The dimension bound has no
  efficient-algorithm claim.
- **R-02:** Rechecked unique dominant alternant monomial extraction,
  marginal-content exponents, swap denominators, and projector domain.
  The required determinant twists cancel both central characters.
  Poles must cancel before coefficient extraction; this is stated.
- **R-03:** Recomputed the S4 characters from perfect matchings and
  the standard permutation representation; tensor and symmetric
  decompositions agree with exact permutation enumeration. Tensor
  image and Levi centers have different dimensions. Iterated
  multiplicity-free branching is explicitly allowed to have multiple paths.
- **R-04:** Re-derived the cycle-index identity for Sym^d(Sym^n V),
  checked the conjugated trace convention in the U2 counterexample,
  and verified the normalized wreath-product projector formula.
- **R-05:** Checked the ideal/orthogonal-kernel identification,
  compact-group Zariski density, Schur block normalization,
  multiplicity versus full block rank, and Cauchy–Binet indices.
- **R-06:** Checked Gaussian moments, coefficient span versus orbit
  span, the central idempotent scalar, integral character values,
  the entry bound, and multivariate interpolation. Added the caveat
  that integral polynomial coefficients may require scaling by n!
  to obtain an integral symmetric tensor.
- **R-07:** Checked the normalization of divided binary coefficients,
  E(b_j)=j*b_(j−1), cancellation of the apparent b0 denominator in
  Q_j, degree and weight of products, independence after setting
  b0=1,b1=0, and realization by diagonal determinant pencils.
  Rechecked every step of the binary-form containment argument and
  highest-weight support restriction. The numerical Kronecker
  count is explicitly credited to Manivel Corollary2(1).
- **R-08:** Checked character extraction and resolution numerator
  signs. Orbit-closure ideals are not dropped from Molien–Weyl.
- **R-09:** Rechecked both Cauchy expansions, the length cutoff,
  determinant-isotypic Fourier projections, the t^(2nd) factor,
  the stable inverse-determinant product, and the S_nd character
  fourth moment. Nonzero rectangular Kronecker coefficients have
  length at most n², so the stabilized sum includes all labels.

No gap remains in these stated finite identities, inequalities,
counterexamples, or rank reductions. The general efficient
positivity/separation problem is not claimed proved.


## Subsequent complete proof reads

- **R-10:** Read the complete specialization and comparison proof. Checked the
  constant term of GCT IV Corollary 18.4, parity and symmetric/exterior split,
  nondegenerate quadric density, and the leading-principal-minor proof of all
  ambient quadric multiplicities. The source's global-crystal theorem remains
  cited background; no independent reproof is claimed.
- **R-11:** Read the complete low-degree exclusion argument, including the
  algebraically closed/smooth hypotheses in Beauville, singular forms by
  density, padding, and the direction of highest-weight ideal containment.
- **R-12:** Read the full dominance-to-coordinate-ring argument and all
  certificate conventions. Checked degree and derivative formulas, modular
  nonzero-minor lifting, highest-weight support, quartic ideal shift, and
  the deficit-one family. Root's separate Ryser/interpolation verification
  is recorded by root; the exact Bareiss and finite-difference checks here
  are this agent's computations.
- **R-13:** Read all cases in the dominance classification. Checked finite
  field evaluation versus coefficient rank, torus stabilizer and fiber
  dimensions, the n17 ceiling and all-larger-n inequality, and multiplicity
  consequences. Forward/reverse DP, Ryser/Gray-code derivative recomputation,
  and unnormalized-pivot minor recheck are distinct algorithms executed by
  this agent; they are not an external independent verification.
- **R-14:** Read the full projective multiplication and dimension proof.
  Checked an irreducible permanent specialization, generic uniqueness of
  the padding factor, closed projective image, exact projected orbit image,
  Hilbert-growth direction, and exactly-four-row support.
- **R-15:** Read the complete cyclic/two-chord argument. In particular all
  bidegree-(n-2,2) generators are reduced before the partial-fraction
  obstruction; the three-root step applies for n=4; and the deformed
  augmented minor is nonzero at zero. Root and purity separately read this
  proof and wrote their own review events.
- **R-16:** Read the complete simultaneous argument. The local 2x3
  factorization remains exact because the two rows have no other support,
  even with wrapped columns and all other chords. The root-of-unity
  coefficient argument uses every allowed three-consecutive-index interval,
  not only endpoint Fourier characters. The Toeplitz determinant is the
  transpose dual-Jacobi–Trudi determinant, and all numerator exponents are
  distinct in [0,k] with k<m, proving nonvanishing. Vandermonde independence
  occurs in the quotient by the FULL cyclic Jacobian space; different
  bidegrees are then independent. The generic deformation and padding
  arithmetic have been checked. Purity separately reported a complete pass.

The general efficient positivity problem and the maximal possible permanent
projection dimension remain open in these notes. The growing padded
multiplicity separation in R-16 is proved within its stated range.


## R-17 and R-18

- **R-17:** The unique perfect matching in each cyclic complementary
  matrix gives determinant/permanent cofactor equality up to a sign,
  including the derivative cofactor sign. Thus the full Jacobian spans
  agree. The dimension upper bound and the already proved rank lower
  bound coincide. Low-degree cases use the full ambient quadratic/cubic
  spaces already established. The two padded dimension comparisons and
  the G-12 boundary directions were recomputed.
- **R-18:** Read the entire two-family proof. Verified both local
  identities, polynomial limits, the coefficient ratios D_r/A_r through
  D_(r−2)/A_r, all shifted H factors, and the character-independent cubic
  evaluation determinant. The allowable Fourier-coordinate interval has
  four consecutive entries exactly in the stated interior range; the
  degree-four rectangular Schur alternant has distinct exponents below
  m. Two Vandermonde systems prove simultaneous quotient independence.
  The augmented-minor deformation and padding/stability inequalities
  have been checked in full.

Root independently reported full R-17 and R-18 proof reads with no gap,
and independently recomputed both local identities, the coefficient-ratio
numerator, and the cubic determinant by symbolic algebra. Root's files
are `work/root/check_r18_cubics.py` and `r18_cubic_check.json`; its own
review events carry that independent-agent verification. This receipt
is not counted as another execution by this agent.

## R-19

Read the complete simultaneous row-and-column argument. Both support conditions remain valid with every motif present because centers are separated by three. The column factorization, exact cofactor identities, base matching products, shifted coefficient identities, and quintic root lists have been checked. The two-value determinant is independent of the Fourier character and nonzero on the stated interior. The six-coordinate Toeplitz matrix is the rectangular Schur specialization with exponents below the root order. Four Vandermonde systems prove independence modulo the entire base space, and all added vectors occur in one polynomial deformation. Padding and stability bounds have been recomputed.

Purity independently read the complete proof and independently derived the determinant cancellation; its review and events are in `independent_review_purity_R19.md` and `independent_review_purity_R19_events.tsv`. This receipt is not counted as an additional computation by this agent.

## R-20

Read the entire fixed five-row proof after writing. The signed determinant comparison vanishes to first order by the forced matching parity, and the complete generic second-order expansion contains precisely the displayed 6/9/6 terms. Both larger support factorizations persist with all five-row motifs simultaneously. Dividing by epsilon squared gives polynomial families in one differential image. The eight local top components and the external-index alignment have been checked exactly.

The row and column Fourier normalizations have been rederived from their completed geometric products, including every scalar and root shift. Their full spaces meet precisely in the base space, because the two degree-four factors are coprime. The ten-coordinate Schur specialization is nonzero for every stated interior interval. The cleared fixed matrices give a nonzero integer polynomial with the claimed degree bounds, so the primitive-root choice and bounded exceptional modes are justified. Missing modes cost only a constant number of blocks because the Fourier systems are ordinary Vandermonde matrices in q^(5t). The descending bigrading argument establishes independence of the original, possibly inhomogeneous limits, and a single augmented minor gives the common-pencil rank. All padding constants were recomputed.

Root and purity each completed independent whole-proof reviews and independent local/certificate computations, both PASS. Root's separate algorithm is `work/root/check_r20_certificate.py` (Ryser and Berkowitz for the local calculation, evaluation interpolation for the Fourier bases); purity's report is `independent_review_purity_R20.md`. Their records carry those independent-agent checks. Reading their reports is not counted as another execution by this agent.

## R-21

The entire arithmetic and compressed-kernel proof has been checked. The integer characteristic coefficient is the product of nonzero eigenvalues; the AGM bound has the correct direction and the rank-one case is separate. The fixed-height bidiagonal example proves exponential-in-dimension small eigenvalues are possible. The n! symmetric tensor embedding yields the exact n! beta! kernel factor, and central Schur projection contributes precisely (f^lambda/D!)^2/(n!)^(2d). Row-sum weights and the Weyl denominator recover the orbit-span multiplicities. The complexity assertion is explicitly for fixed ambient N and numerical degree nd. Absolute spectral precision is sufficient, while entrywise error below1/2 separately permits exact integer rounding.

Root independently read the main proof and reported PASS, requesting the clarification from binary digits to absolute error, which was adopted. The subsequent integer-rounding clarification and fixed-height example are elementary additions checked by this agent; they are not represented as part of an earlier computation. Three direct tensor/kernel examples checked2550 entries and the expected boundary multiplicities.

## R-22

Read the entire written proof after drafting and rederived every step. The endpoint signed-minor agreement through order2 follows from the single forward/backward cycle parity; the no-forward upper-Hessenberg cancellation holds for every deleted-column minor. The highest surviving pair is forced by the column multiset, yielding all row forms. Reversal of both local row and column orders gives the stated column forms and exchanges actual global row/column cofactor limits with the correct external index.

Both Fourier completions, the nonzero basis denominators, the last2x2 X^2 coefficient, and every possible primitive-root zero were checked. The row specialization works for every interior k and any primitive q. Reflection proves column nonvanishing for that same k; it does not assume simultaneous choices. The product over all k is nonzero over Q(q), so the integer grid produces one simultaneous motif. The grid lemma is explicitly restricted to characteristic zero. The row and column Laurent exponent ranges give at most2b bad characters.

The joint coprime-factor intersection has exactly the two-dimensional base; the allowed coordinate interval has2b consecutive coefficients. The rectangular Schur determinant is nonzero because all Weyl exponents lie below m. Gcd(b,m) controls repetitions among q^(bt), so missing characters still permit the required Vandermonde systems. Descending highest bidegrees retains the complete polynomial limits, and the augmented minor uses a single common epsilon.

The b choice, constant20, threshold99, fixed-ratio threshold, improved rectangular threshold2025, and sqrt2 dimension ceiling were recomputed. Bounded checks enumerate all local permutations r2..7 and verify24 exact binary interpolation/evaluation cases b3..10; they supplement rather than replace the uniform proof. No growing pencil Jacobian or exact maximal-rank claim is made.

Root independently reported a full nine-section proof rederivation PASS. Purity read the complete fragment and independently checked/rederived sections6–9 PASS, explicitly leaving sections1–5 to root/isolation. These are received independent-agent reviews, not extra computations executed by this agent; each reviewer records the exact scope separately.


Isolation independently reported a whole-proof review PASS, including sections1–5 and the global argument. Its requested wording clarification was adopted in both copies: the integer grid bounds the untwisted motif parameters; translated copies include root-of-unity twists. No mathematical claim or constant changed.

## R-23

Read the complete Tor reduction and independently proved its full-variable first-syzygy input by monomial multidegrees: coefficients moving both row and column are isolated by a square; one-index moves satisfy all pairwise negative equations and vanish with three indices; diagonal coefficients are row-plus-column potentials with one sum constraint and one gauge redundancy. This yields exactly2m−2 known relations.

The cyclic incidence graph proves their restricted independence. The m cyclic cofactor translates in each of m bidegrees have every Fourier character nonzero, establishing all m^2 generators are independent and Tor1 below degree m vanishes. The degree-m tensor-resolution complex then gives the exact defect, including its special cyclic value2m(m−1). Every generic defect for m3..16 was recomputed from R13. The R22 upper bound and the depth obstruction for allm>=3 follow with the correct inequality directions.

Read the exact primary ELSW Theorem1.1/Example4.1/Theorem4.3 locators and the BCMV2024 Theorems4.14/4.23 locators. Full cited-paper proofs are not claimed independently verified. Root reports a whole-proof PASS; purity review is requested separately. A bounded exact computation for m3..12 verifies the cyclic generator ranks m^2 and old-relation ranks2m−2; generic Tor numbers use the proved R13 dimensions rather than a new generic Jacobian run.


At root request, the known first-syzygy proof was moved out of the manuscript into r23_syzygy_audit.tex. Its derivation remains an actual audit check; both manuscript copies now cite ELSW directly and define G_ij immediately before the new restriction argument.

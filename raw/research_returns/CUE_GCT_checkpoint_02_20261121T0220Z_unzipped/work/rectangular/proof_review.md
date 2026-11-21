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

# Whole-proof review of R-01–R-09

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

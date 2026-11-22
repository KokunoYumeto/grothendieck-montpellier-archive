# Booker distribution route

The primary published input is Andrew R. Booker (2015), *L-functions as
distributions*, *Mathematische Annalen, 363*(1–2), 423–454,
https://doi.org/10.1007/s00208-015-1178-z. The inspected author manuscript is
arXiv:1308.3067v2 (13 February 2015), 26 pages, retrieved on 21 November 2026.
Its SHA-256 is `f33cc6f0277d17df11cb19999fb693eca56bc0f13ffd5c9cc5db824cd41df496`.
The source PDF and extraction remain private and are not deliverables.

Read completely: Definition 1.3 and examples pp.3–4; Theorems 1.6–1.7 pp.5–6;
Lemmas 2.3–2.4, Proposition 2.1 and its proof pp.9–13; the full multiplicity-one
proof §2.3 pp.13–15; and the degree-below-one proof, including Lemma 3.1 and the
contour deformation, pp.15–17. The unused classification of degrees at least
one was not re-refereed.

New deductions are in `booker_route.tex`:

- **MA-LD-001:** Under the exact S5 comparison assumptions and R_B, k>0 forces
  infinitely many poles and infinitely many zeros of the completed comparison
  quotient. All belong to the critical line, already without M: the exceptional
  set has counting exponent 1/2, so the quotient Euler logarithm converges
  absolutely to the right; Booker's gamma-factor construction and functional
  equation reflect nonvanishing to the left. This concerns the signed quotient
  divisor only. Its total variation is not o(T). Finite poles, finite zeros, or
  o(T) variation are each equivalent to the existing k=0 comparison gate.
- **MA-LD-002:** The exact multiplicity-one sum is sum |f(n)|/log n, and it
  diverges like k log log X in the positive branch. The other criterion uses
  Dirichlet coefficients a_F, whose prime terms also force divergence. The
  tempting substituted sum |f(n)|/sqrt(n) actually converges. The asymptotic
  follows by partial summation from MA-S5-004 and the convergence follows from
  the same counting exponent.
- **MA-LD-003:** zeta/L(chi_5) gives a genuine degree-zero datum with zero gamma
  kernel and nonnegative Euler logarithmic coefficients, but infinitely many
  positive and negative divisor orders. It is an example against an abstract
  inference, not an S5 field or a counterexample with the stipulated sparsity.

The exact missing hypothesis in the converse route is finiteness of the negative
divisor. In the source proof this is used on p.16 to choose a horizontal height
above every pole. M, or holomorphy of numerator and denominator separately, does
not provide cancellation of denominator zeros. No theorem closing the S5 gate
is claimed.

The authoring agent independently reread all three new proofs, including the
normalization f(p^j)=4 log(p)/p^(j/2), the distinction between completed and finite
quotients, all bad-prime terms, the critical-line support argument, partial
summation, and the concrete quadratic-character example. A separate root review
is requested before final inclusion.

## Further Rankin–Selberg consequence

`booker_rankin.tex` contains **MA-LD-004**. The central order inequality extends
pointwise to every critical-line height: if kappa(t)=ord(L_W)−ord(A) and q(t) is
the order of the incomplete twisted symmetric square, then
q(t)=d(t)+e(t)−kappa(t), while beta(t)=b(t)+n(t)+kappa(t). The zeta order at a
noncentral zero must be retained in both intermediate Rankin–Selberg formulas;
it cancels exactly. All finite and gamma correction factors are units along
the whole critical line, by the same finite-image local check as MA-S5-003.

Combining this with Booker's infinitely many discrepancies of both signs forces
infinitely many common zeros of B and L_(V eta)L_X, and infinitely many common
zeros of the symmetric-square function and A C. The sum of their two overlap
counts, weighted by minimum multiplicities, dominates N_R(T), so is not o(T).
Either finite common-zero set, or a sublinear combined overlap count, would close
the comparison. No theorem supplying those bounds is asserted. The numerical
central inequality k≤d+e itself is unchanged.

The full terminal Theorem 7.1 proof in Takeda's arXiv:1506.04791v1, pp.49–50, was
freshly read. Private PDF SHA-256:
`cdc3d905c7186065d02a7e5d3bc18b266bf16e1835280128ccc799d59fa3c2aa`.
The new argument was completely reread after writing. Root review is requested.

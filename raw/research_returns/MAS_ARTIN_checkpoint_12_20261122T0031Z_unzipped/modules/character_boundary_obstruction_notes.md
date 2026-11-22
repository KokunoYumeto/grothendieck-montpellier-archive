# MA-MO-025: boundary multiplicity and the actual source norm

## Proved statement

The new module character_boundary_obstruction.tex keeps every original source convention of MA-MO-024. For a nontrivial finite-order character and a completed zero of multiplicity m on either edge of the centered strip, every nonzero complex compact smooth test fails to give a bounded extension of the actual full common-sum source action whenever s ≤ 2m − 1. The equality case is included.

The statement concerns the literal source action on exponential Schwartz inputs. Its construction uses the original wide Euler inverse, structural local source, and dual Fourier phases. No narrow inverse multiplier replaces it.

## Proof and domain audit

The last-edge cutoff function of MO024 remains nonzero at a boundary point. Its left exponential-order bound gives a genuine one-sided Mellin half-plane. Product uniqueness shows that no nonzero complex compact convolution can annihilate it. This selects fixed compact source and output tests h and v for which H_h(lambda) B_v(lambda) is nonzero, regardless of G(lambda).

Under a hypothetical bounded extension, the paired translated-source Laplace integral is holomorphic for Re w > a. The cleared original Euler identity then gives a full order-m pole along w = lambda + delta:

    delta^m F(lambda + delta) -> -H_h(lambda) B_v(lambda) / a_m != 0.

The Hilbert orbit integral is

    u_delta = integral_[t0,infinity) exp(-(lambda+delta)t) U_t h dt.

It is a genuine Bochner integral. Its finite-parameter approximants are compact smooth functions in the original source domain and converge in the exact inherited sum norm. Only the hypothetical bounded extension is applied to the infinite-tail limit. This avoids assuming an uncontinued source formula on that noncompact vector.

Beyond a fixed right endpoint, the integral is exactly H_h(lambda+delta) exp(-(lambda+delta)x). With both exponential terms of the sum weight retained, its squared norm is O(delta^(-s-1)).

For s < 2m − 1, delta^m u_delta tends to zero in norm. At s = 2m − 1 it is bounded and tends to zero uniformly on every compact set, hence weakly in the weighted Hilbert space. The same fixed continuous output functional composed with a bounded extension must tend to zero in either case, contradicting the nonzero pole coefficient.

The left boundary follows from the actual source reflection identity with the dual character and the reflected test. No conjugation is substituted for that source identity.

## Exact relation to retained jets

MA-WP-001 retains the boundary derivatives j satisfying 2j < s − 1. Thus retaining all m jets is equivalent to s > 2m − 1. Combining this new theorem with MO024 yields full retained multiplicity as a necessary condition for boundedness of the actual full source map after even one nonzero compact smoothing.

This does not prove that full retention is sufficient. The actual half-plane construction MO022 still requires a strict interior margin. In particular no fully retained boundary block or zero sequence approaching an edge is silently assigned an operator bound.

## Source and review scope

The complete post-writing author reading passed. The whole 482-line MO024 proof was freshly reread, together with MA-WP.2–5 and the exact boundary-duality calculation MA-WP.17. The primary Meyer interfaces are inherited from the already recorded fresh source review; this new argument does not claim an additional complete primary-source proof audit.

The complete independent PF reading also passed, including all equations and final scope. The complete root reading also passed. MA-MO-024 itself was left unchanged.

The new boundary row was created and decided during this extension. It is not counted as a pre-existing open-to-decided movement. No arithmetic exterior-zero existence, boundary-zero existence, own-character RH, or FT002 deficiency vanishing has been established.

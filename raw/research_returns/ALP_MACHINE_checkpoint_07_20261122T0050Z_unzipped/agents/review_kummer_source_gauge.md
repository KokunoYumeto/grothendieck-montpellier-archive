# Whole-proof review of AM-K018

Reviewer: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE.
Completed 2026-11-21 21:41 UTC.

I read the entire saved proof in jacobian_source_gauge_match.md,
including its fixed-line application, and independently compared the
displayed gauge axioms with the recovered source declarations. The
following conclusion is a proof review, not a new gauge theorem.

**Outcome: pass in the stated ordinary-J-power scope.**

The Appell–Humbert quotient has exactly the multiplier
$\exp\pi(H(u,\mu)+H(v,\lambda)+H(\lambda,\mu))$: the
semicharacter quotient supplies the imaginary part of the final cross
term. Both partial addition laws consequently have scalar one. The
symmetry discrepancy is the exponential of twice an integral imaginary
pairing, and all adjunctions have scalar one by the Rosati identity.
Thus the frame ratio to the Chern-reduced frame satisfies the same
four structure-map identities as the source gauge, with the stated
signs.

The same-frame proviso is essential and is respected. The actual
source theorem says that a difference of canonical gauges is additive
in both arguments and adjoint-balanced. It therefore becomes a
bilinear form in characteristic-zero group logarithms. For the
full cyclotomic action its coefficient on a pair of holomorphic
characters $i,j$ is killed by $\zeta^i-\zeta^{-j}$. For
$i,j\in\{1,2,3\}$ this scalar is nonzero. Repeated ordinary
factors retain that property; conjugated factors do not, which
explains the stated limitation.

The accepted existence theorem is used to descend this unique gauge
algebraically before changing to the 11-adic frame. The change by
$\log J$ is made in characteristic-zero formal series and does
not assume integral logarithm coefficients. The integral product
frame in DP47 is preserved by the full cyclotomic action supplied
by DP49, so the same uniqueness theorem applies. The trace-one
pullback has Hermitian form $H$, and the rigidified primitive
isomorphism in the source eL fixes its scalar. This gives the
actual equality with $f_sU^\kappa B^{-\kappa}$, including
the integral frame unit and the primitive-kernel sign. It does
not claim that the reduced frame is integral.

The last fixed-line application is also sound in its stated
scope. The lines $(0,t,t)$ and $(t,0,t)$ have leading
terms $-t^2$ and $t^2$ in the explicitly normalized section.
The DP49 unit-arrow eigenbasis differs from the given integral
CM eigenbasis by diagonal units at11. Thus the displayed paths
have the required restricted-power lengths and nonzero
prefactor restrictions. The exact liminf claims then follow
from the accepted DP49 theorem; they are not re-proved from the
new mod11 recurrence.

## Source passages read directly

- CocycleRightZeroThd.lean, FB.IsCanonGauge, lines174–183,
  hL and nabVal, lines185–189.
- CanonGaugeSubIsBiadd.lean, the complete theorem at lines16–60.
- ThGerm.lean, IsFrame symmetry/adjunction and primitive eL/IsGerm
  clauses, lines119–181.
- DP47_integrated_fragment.tex, complete proposition and gauge
  proof through the integral hyperbolic criterion.
- DP49_integrated_fragment.tex, complete theorem statement and
  actual CM-action/polarization hypotheses.

The complete K018 argument was read as one proof; the source
passages above check its potentially consequential identifications.
No Lean compilation or independent formal verification is claimed.

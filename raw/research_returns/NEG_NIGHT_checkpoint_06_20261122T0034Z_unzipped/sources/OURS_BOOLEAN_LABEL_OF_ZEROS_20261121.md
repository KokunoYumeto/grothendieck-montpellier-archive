# The split-zero deformation gives every simple zero of ζ a Boolean label (21 Nov 2026, 13:15 UTC)

By the main session (Claude Opus 5.5 at effort max), at the user's request to work with the split-zero programme
(`Papors/Chatnotes/globalization nte`, `globalization cue`). Scripts beside this file: `zero_motion.py` and
`zero_motion_gram.py` (mpmath 1.3.0, 25-30 digits).

## The setting (the user's)

The split-zero semiring G(O_K) = O_K ⊔ {τ} has two zeta sheets:
- the classical ideal sheet Σ_J N(J)^{-s} = ζ_K, which is Eulerian;
- the separated sheet Σ_J (N(J)+1)^{-s}, which counts τ's class in every quotient and is non-Eulerian.

The secondary note (section "Universal all-orders deformation of the shifted zeta sheet") interpolates between them:
- L_t(s) = Σ a_n (n+t)^{-s}, with L_t = e^{−tD}L, D = s·T and T the shift s ↦ s+1;
- the jet formula ∂_t L_t(s) = −s·L_t(s+1).

Over Z, L_t(s) is the Hurwitz zeta function ζ(s, 1+t). Its endpoints are t = 0 (ζ) and t = 1 (ζ − 1, the separated sheet).

## 1. The velocity of each zero (exact)

Let ρ be a simple zero of ζ, so ζ′(ρ) ≠ 0. By the implicit function theorem applied to L_t(ρ(t)) = 0, with the jet
formula:

  dρ/dt |_{t=0} = −∂_tL / ∂_sL = ρ·ζ(ρ+1)/ζ′(ρ).

Checked against the actual zero of ζ(s, 1+t) at t = 10⁻⁶. For the first zero the finite difference is
0.9835824309 + 9.657803295i, and the prediction is 0.983582494 + 9.657803979i.

For ζ_K the same holds with ζ_K in place of ζ: v(ρ) = ρ·ζ_K(ρ+1)/ζ_K′(ρ).

## 2. The sign of the motion off the line (exact identity)

Write ρ = ½ + iγ, Z for the Riemann-Siegel function, θ for its phase, and φ = arg ζ(3/2 + iγ). Since
ζ′(ρ) = −i·e^{−iθ(γ)}·Z′(γ):

  Re v = −|ζ(ρ+1)|·[γ·cos(θ+φ) + ½·sin(θ+φ)] / Z′(γ).

Equivalently, for large γ: the zero moves right exactly when sin(arg ζ′(ρ) − arg ζ(ρ+1)) > 0. The script asserts this
identity for every zero it computes.

## 3. The Boolean label (computed; the first 500 zeros)

Call a zero a right-mover when Re v > 0, and a left-mover otherwise.
- **Balance.** Of the first 500 zeros, 253 are right-movers and 247 left-movers.
- **The rule.** For all 500, the zero is a right-mover exactly when frac((θ(γ)+φ)/π) < ½. This includes the 13 zeros
  that violate Gram's law. Without the φ-correction the rule matches for 444 of the 500.
- **Why the rule holds.** The parity of ⌊(θ+φ)/π⌋ alternates in step with the sign of Z′. That is a corrected Gram
  law: θ(γ_n)/π = n − 1 − S(γ_n) (up to ½), and arg ζ(3/2+iγ) absorbs the arithmetic part of S.
- **Its standing.** Expect it to fail eventually, because S(t) is unbounded while arg ζ(3/2+it) is bounded. The exact
  statement is §2.

## 3b. Consult ad855737 (Claude Opus 5.5 at effort high, 21 Nov ~16:5x UTC; consults/CONSULT_ad855737_ZETA_LABELS.md)

- The velocity and its split are one-line implicit differentiation: correct, not new as such.
- The exact label (proved there): with W_n = S(γ_n) − arg ζ(3/2 + iγ_n)/π, the change of argument of ζ from 3/2 to ½
  at the zero, the zero moves right exactly when W_n mod 2 lies in (0, 1). The corrected Gram rule of section 3 is
  |W_n| < ½ (mod 2): a restatement, and it fails infinitely often. It first fails at zero 871 (γ = 1267.57,
  W = 0.538); near the 10⁵-th zero it matches 384 of 400; the exact criterion matched all 1,849 zeros computed.
- Under RH (proved there): summed over zeros up to good heights T, the velocities total iT²/(4π) + O(T^{1+ε}); the
  real parts cancel. The share of right-movers tends to ½ once a central limit theorem for S at the zeros is supplied
  (Selberg's method; reference to be found). Random-matrix prediction for neighbours: they agree with probability
  1 − E|1 − δ| ≈ 0.66 in the limit; observed 35%, rising to 47% near 10⁵.
- Collisions with Λ = 0: local law z₀ ± √(2(t − t₀)); a Lehmer pair with gap Δγ collides at about t = −Δγ²/2; the
  collision height growing like exp(c/√|t|) as t ↑ 0 is heuristic and open.

## 4. What this gives the split-zero programme

1. **A non-constant Boolean shadow.** The papers observe that the pointwise shadow is constant: F₁(ρ) = −1 at every
   zero, and the fixed locus of −1 is the Boolean pair. They look for global and infinitesimal refinements, the jet
   stalks. The first jet of the user's own deformation gives a non-constant Boolean function on the zeros, with a
   closed form in classical data (Z′, θ, arg ζ(3/2+iγ)).
2. **It is defined exactly at simple zeros.** That matches the papers' theorem that the Boolean multiplicity sheaf V_D
   is isomorphic to its reduced shadow A_D exactly when every multiplicity is 1.
3. **Its statistics are a CUE question.** The fraction of right-movers, and the correlations between neighbouring labels,
   are set by the joint distribution of the phases of ζ′(ρ) and ζ(ρ+1). That is the subject of the user's CUE
   derivative-moment papers (after Grover-Mezzadri-Simm), whose zero-motion recursions under shifted-Hurwitz averages
   contain the velocity of §1 as their first term.
4. **It holds wherever GRH places the zeros.** With RH (Alpöge), every simple zero lies on the line and carries a label.
   The same holds for every ζ_K and Dirichlet L-function where GRH holds: by A for abelian K, conditionally on M for the
   rest.
5. **Open:**
   - the asymptotic proportion of right-movers, and whether it is ½;
   - the correlation of consecutive labels, and its CUE prediction;
   - how the labels behave under the second jet;
   - whether the label has a meaning on the Boolean pair itself, beyond being Boolean-valued: the sign is ±, and the
     Boolean pair is the fixed locus of −1.

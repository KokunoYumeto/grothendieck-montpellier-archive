# Check of phase_averaged_hurwitz.tex (23 Nov 2026)

By Claude (Claude Opus 5.5 at effort max), main session ed7922ad, about 01:1x UTC, at the user's sending of prompt 78.
Type: targeted proof check, every step derived and recomputed by hand; no program run. Verdict: correct.

- Phase average: H_d(s,t) = zeta(s) + (-1)^d (s)_d/d! zeta(s+d) t^d + O(t^{2d}) from the Hurwitz derivative
  (DLMF 25.11.17) averaged over d-th roots of unity; b_d(rho) != 0 at every nontrivial zero (rho not a non-positive
  integer, Re(rho+d) > 1). Correct.
- Proposition: one-edge Newton polygon (vertices (m,0), (0,1) in (s - rho, u = t^d)); u = w^m, s = rho + w z gives
  a z^m + b_d(rho) + O(w) with distinct roots; branches rho + c e^{2 pi i j/m} t^{d/m}; discriminant order
  C(m,2) * 2d/m = d(m-1); monodromy j -> j + d mod m, gcd(m,d) cycles. Correct, including m = 1.
- Fixed contour: ord Disc = d(M - r). Prime period: z_p locally biholomorphic; a pair of distinct centres collides for
  at most one prime (two collisions force log p / log p' rational); C(M,2) + 1 primes contain a separating one.
  Correct.
- Rounding theorem: F_K in [0,1], F_K <= 4/(K^2 |1 - e^{ix}|^2), 1 - F_K(x) <= (K^2 - 1) x^2 / 12 (recomputed:
  sum_{u,v<K} (u-v)^2 = K^2 (K^2 - 1)/6), weights sum to 1, deficit and leakage as stated, sigma > 0 by
  irrationality of log p / log q and compactness. Correct.
- Example: log 3/log 2 in (3/2, 8/5), chord > 2 sin(3 pi/5) ~ 1.902, leakage 12/(256 * 3.61) < 0.013 at K = 16.
  Correct.

Scope: the tools are classical (Fejer kernel, Puiseux/Newton polygon, argument principle); the value is the finite
certificate under RH and the stated obstruction (close packets indistinguishable at fixed tolerance). Not checked:
frame_and_grading.tex, CONNECTIONS.md, the checkers.

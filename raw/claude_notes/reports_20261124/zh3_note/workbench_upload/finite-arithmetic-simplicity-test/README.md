# A finite arithmetic test for simplicity of the Riemann zeros, after Suzuki: programs and certificate

This folder accompanies the note *A finite arithmetic test for simplicity of the Riemann zeros, after Suzuki*
(24 November 2026). The note's mathematics was produced by GPT-6 Astra (ChatGPT Pro mode). Claude Opus 5.5 at
effort high checked the proofs and wrote the note. It also wrote every program in this folder, from the note's
formulas and independently of the programs of the original computation. Everything here is dedicated to the public
domain under CC0 1.0. No human has checked it.

## The quantity computed

For the dyadic window $V_N$ (continuous piecewise-linear functions with knots in $2^{-N}\mathbb Z$, supported in
$[-N,N]$, of mean zero; dimension $d_N=2N2^N-2$), the trace defect is

$$D_{N,k}=S_k-\operatorname{tr}C_N^{2k},\qquad S_k=-2k\,[z^{2k}]\log\frac{\xi(1/2+iz)}{\xi(1/2)}.$$

Here $\operatorname{tr}C_N^{2k}=(-1)^k\operatorname{tr}\big((G_N^{-1}B_N)^{2k}\big)$. The Gram matrix $G_N$ and the
antisymmetric primitive matrix $B_N$ are given by the arithmetic side of the explicit formula: the archimedean terms
and the prime powers $n<e^{2N}$ (note, Section 5). If $D_{N,k}<2/T^{2k}$, every zero with $0<\operatorname{Im}\rho\le T$
is simple (note, Theorem 1).

## Programs

| File | What it computes | Rigour | Written by |
|---|---|---|---|
| `enclose_trace_defect.py` | Ball-arithmetic enclosure of $D_{N,k}$ and the verdict of $D_{N,k}<2/T^{2k}$. Every integral by rigorous ball integration (`acb.integral`); $S_k$ from the power series of $\log\xi(1/2+iz)$ (`acb_series`); $G_N^{-1}B_N$ by a rigorous linear solve, which also certifies that $G_N$ is invertible | rigorous, assuming Arb/FLINT and the program are correct; not formally verified | Claude Opus 5.5, effort high |
| `enclosures_output.txt` | Its output for the six rows below, at 150 decimal digits | — | — |
| `replay_floating_point_flint.py` | The same quantity with Gauss–Legendre quadrature in high-precision arithmetic; with a fourth argument $T$ it also counts the eigenvalues of $C_N$ above $1/T$ (note, Theorem 2) | not rigorous | Claude Opus 5.5, effort high |
| `replay_floating_point_mpmath.py` | The same quantity for $N\le4$ with mpmath adaptive quadrature | not rigorous | Claude Opus 5.5, effort high |

Usage: `python enclose_trace_defect.py N k T [digits]`, for example `python enclose_trace_defect.py 6 3 97.632 150`.
Requirements: Python 3, python-flint 0.9.0, sympy (for the list of primes); mpmath for the replays. Running all six
rows takes under a minute on a desktop machine.

## The certificate

| $N$ | $d_N$ | prime powers | largest | $k$ | $T$ | $D_{N,k}$ (enclosure) | $2/T^{2k}$ |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 5 | 7 | 9 | 14.134 | [3.9465301437298266590e-21 ± 1.84e-41] | 3.9469209657e-21 |
| 2 | 14 | 24 | 53 | 3 | 20.704 | [2.5391051100983959389e-8 ± 4.15e-28] | 2.5392440398e-8 |
| 3 | 46 | 98 | 401 | 3 | 26.782 | [5.4196480726617661175e-9 ± 4.90e-29] | 5.4196589931e-9 |
| 4 | 126 | 465 | 2971 | 2 | 39.913 | [7.8803302378006305370e-7 ± 3.10e-27] | 7.8808399439e-7 |
| 5 | 318 | 2532 | 22013 | 2 | 62.413 | [1.3180235740421037608e-7 ± 1.18e-27] | 1.3180435572e-7 |
| 6 | 766 | 15040 | 162751 | 3 | 97.632 | [2.3092709160972367573e-12 ± 3.90e-32] | 2.3092815187e-12 |

Every row passes the strict test. The last row certifies that every zero of $\zeta$ with $0<\operatorname{Im}\rho\le97.632$
is simple. No zero of $\zeta$ is used as input.

**Agreement.**
- The original computation used a separate program by GPT-6 Astra (ChatGPT Pro mode): Arb at 120 digits, with a
  preconditioned positive-definiteness test. It gave upper bounds that agree with these enclosures to ten
  significant digits.
- The two floating-point replays agree to every digit they print.
- At the three heights 39.913, 62.413 and 97.632, the floating-point eigenvalue count equals the number of zeros below
  the height (6, 14, 28).

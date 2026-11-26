# L-gct-179: search for a 7-dimensional level space of 4 x 5 matrices (23 Nov 2026, 17:10 UTC onward)

By Claude Opus 5.5 at effort max (fork of agent a3533d80e4df973c2, for session 672ae3a0; lease d1b4424c held by the
coordinator, not released here). Statement (desk/next_15.json): exists L <= C^(4x5), dim L = 7, with
sum over injections f: Fin 4 -> Fin 5 of prod_i (1 + t(i, f i)) = 120 on L, i.e. M_1 = M_2 = M_3 = M_4 = 0 on L.
Scripts and outputs: `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\672ae3a0-11a5-4e45-b4e2-c44a7908d05b\scratchpad\lvl\`
(scratch; copy what you keep). Notes: `<local>/Documents\agent_notes\L_gct_179_NOTES.md`.

## Status (updated as the run goes)

No witness. Evidence and exact partial results below.

## 1. Exact results (sympy, rational arithmetic)

1.1 **No 7-dimensional level space contains a row-plus-column hook** (either of the two 6-dimensional hook types, at
any row i and column j, by S_4 x S_5 symmetry).
- H6 = {cells (0,1..4) summing to 0} + {cells (0..3, 0) summing to 0} (dim 3 + 3): the extension vector s, taken in a
  complement (the 12 off-hook cells and two transversal hook cells), satisfies 40 coefficient equations; the 16 linear
  ones force s = g * (fixed vector), and the rest are -45 g^4/8192 = 15 g^3/64 = -45 g^2/16 = 0, so g = 0
  (`hookext.py`).
- H6' = {row 0 summing to 0} (dim 4) + {column 0 below row 0 summing to 0} (dim 2): 38 equations, 15 linear force
  s = g * (fixed vector), the rest -40 g^4/9 = -320 g^3/9 = -80 g^2 = 0 (`hookext2.py`).
1.2 **Two always-equal columns are excluded**: this is lemma eI of the accepted L-gct-215 file (no 7-dimensional level
space M with a != b and x(i,a) = x(i,b) for all x in M, all i).
1.3 **Column-cyclic spaces** (L stable under the 5-cycle of columns, L = sum_b U_b (x) chi_b, chi_b(j) = w^(bj)):
U_0 = 0 (a column-constant level element u (x) 1 has M_k = k! C(5,k) e_k(u), so e_1..e_4(u) = 0, u = 0); M_2 gives
beta(U_1, U_4) = beta(U_2, U_3) = 0 for the nondegenerate form beta(u,u') = (sum u)(sum u') - u.u' (matrix J - I), so
d_1 + d_4 <= 4 and d_2 + d_3 <= 4; and d_1 = 4 is impossible: then the triple {1,1,3} forces U_3 = 0 and the triple
{1,2,2} makes the 3-dimensional U_2 totally isotropic for the rank-3 forms 2 e_2(v without coordinate i), whose isotropic
subspaces have dimension <= 2. (Remaining patterns: numerical, section 2.)

## 2. Numerical algebraic geometry

Chart LM (`chart45.py`): L = row space of [I_d | Z] U, U a random unitary basis of the sum-zero hyperplane C^19, so no
gauge freedom; residual per(J + sum_i x_s,i T_i) - 120 at M = 1.4 C(d+4,4) + 40 random complex points.
- Calibration, d = 6, random starts: 108 restarts in 150 s: 3 below 1e-16 and 19 below 1e-10 (relative). The 6-dim
  solutions found are not hooks: no zero cells, L meet DC = 0, L meet RC = 3, L meet CC = 2, one row-supported line.
- **d = 7, random starts: 1350 restarts in two runs (270 in 322 s, 1080 in 1203 s; all converged, median 125-126
  iterations): none below 1e-10; best relative residuals 0.0411, 0.0443, 0.0486, 0.0496.** For comparison the same
  solver at d = 6 reaches 1e-10 in 18% of restarts.
- Near-misses at d = 7 are generic: L meet DC = 0, L meet RC = 4, L meet CC = 3, every row projection 5-dimensional, no
  zero cells, mean |per(J + t) - 120| of 0.4 to 0.8 at unit-size points (against 120). No structure points to a nearby
  solution.
- The 6-dimensional solutions the solver finds are not hooks (a third family): L meet DC = 0, RC = 3, CC = 2, one
  row-supported line (a sum-zero row vector with generic complex entries, so a continuous family), very small extra
  singular values in the row projections (~1e-4): the computed points sit near a singular part of the solution set
  (lemma lO of L-gct-215 forces every exact row projection to have dimension <= 4).

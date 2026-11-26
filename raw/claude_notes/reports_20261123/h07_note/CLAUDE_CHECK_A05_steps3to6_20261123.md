# A05 (H07, "A1 without GRH"), Steps 3-6: my check

By Claude Opus 5.5 at effort max (main session ed7922ad), 23 Nov 2026 ~02:22 UTC (clock 02:17 before, 02:28 after). The finding is by GPT-6 Astra (ChatGPT
Pro mode), AN_GRH final, `AN_GRH.tex` lines 628-905. Steps 1-2 were re-proved independently by a28ea31f (Claude Opus 5.5
at effort max, `field_experts/intake_20261121/intakes/AN_GRH/_work_a28ea31f/A05_steps12_reproof.md`), which I read in full.

**The statement (A1).** K finitely generated over F_p, X/K smooth geometrically connected hyperbolic; Delta_X the maximal
prime-to-p quotient of pi_1(X_Kbar), Pi_X the quotient of pi_1(X) by ker(pi_1(X_Kbar) -> Delta_X). Claim: X(K) -> Sec(Pi_X ->
G_K)/Delta_X, P -> [s_P], is injective.

## Finite field, proper genus >= 2 (Steps 3-5)

Setting: k finite, C/k proper of genus >= 2, P != Q in C(k), s_P and s_Q conjugate by gamma in Delta_C; r != p a prime. Steps
1-2 give beta: G_P -> G_Q over id_{Pi_C}, preserving cusp classes, where G_P is the arithmetic quotient of pi_1(C - P)
whose geometric part is the cuspidally pro-r quotient F_c.

- **Step 3 (equal counts): holds.** For an open I of the geometric group containing N = ker(K -> K^(r)), I^(r) = (I/N)^(r)
  (the run's core argument; checked). So the pro-r geometric group of each cover of C - P (and, killing cusp inertia, of its
  smooth compactification) is read off from G_P, Frobenius-equivariantly. beta identifies H^1(-, Z_r) of corresponding
  compactified covers as Frobenius modules, hence equal traces, hence equal point counts over every finite extension
  (Grothendieck-Lefschetz for curves); beta preserves cusp classes, so the numbers of rational cusps agree; subtracting,
  the open covers have equal counts. Uses only the trace formula and the integral (or rational) r-adic H^1.
- **Step 4 (point sections go to point sections): holds.** R in (C - P)(L), S = beta(D_R). For each open H containing S,
  beta^{-1}H contains D_R, so its cover has an L-point; by Step 3 so does the cover X_H. The finite nonempty sets X_H(L),
  H directed by intersection, have nonempty inverse limit (Koenig); a compatible family gives T in (C - Q)(L) with a lift
  whose decomposition group lies in every H containing S, hence in S; both project isomorphically to G_L, so D_T = S.
  beta is over id_{Pi_C}, so R and T have the same proper decomposition group; by Saidi-Tamagawa 2009 (Def. 1.5, 1.10,
  Prop. 1.8(vi), Rem. 1.2: a finite exceptional set E_C for the cofinite set p', valid over every constant extension),
  T = R when R is not in E_C, P, Q.
- **Step 5 (Kummer contradiction): holds.** Equal sections give equal abelian Kummer classes, so [P - Q] lies in the
  prime-to-p Kummer kernel J(k)[p^infty]; take f with div f = p^e(P - Q). E_P, E_Q: the cuspidally central quotients,
  1 -> M = Z_r(1) -> E -> Pi_C -> 1, classes = degree-one class in H^2(Delta_C, M) = Z_r; beta-bar is over Pi_C and fixes the
  class, so it is the identity on M. chi(u, v) = beta-bar(u) v^{-1} on E_P x_{Pi_C} E_Q, pulled back to C - {P, Q}: residues
  (+1, -1) at (P, Q); kappa(f) has residues (p^e, -p^e); so kappa(f) - p^e chi is unramified and lies in H^1(Pi_C, M) =
  H^1(G_k, M) (inflation-restriction; Hom(T_r J, Z_r(1)) has no Frobenius invariants: eigenvalues q/alpha with |alpha| =
  sqrt q, Weil I; G_k has cohomological dimension 1). So kappa(f) = p^e chi + kappa(a), a in k^x. At R good (Step 4),
  beta-bar(D_R^P) = m D_R^Q m^{-1} with m in M after Saidi-Tamagawa Lemma 1.7 (normalizer of a section-like subgroup is
  itself), so chi restricted to D_R is the coboundary (1 - chi_cyc) m; hence kappa_{r,L}(f(R)/a) = 0, i.e. f(R)/a has
  order prime to r in L^x. Choosing R with f(R) = a zeta, zeta a nontrivial r-power root of unity, outside the finitely many
  values at excluded points (f: C -> P^1 is onto), gives a contradiction. So P = Q.

## Step 6 (finitely generated K; open curves)

- Spreading out and specializing at a closed point where P, Q stay distinct (SGA 1, X 3.8-3.9; G_L -> G_k(s) onto for the
  fraction field of the henselization): **holds**.
- Open curves with compactified genus >= 2 (map the collision to the proper curve): **holds**.
- Genus 0 (three boundary points as 0, 1, infinity; equal Kummer classes in G_m have ratio of p-power order in K^x, which
  is 1 since K^x has no nontrivial p-power torsion): **holds**.
- Genus 1: **holds, after a correction** (02:2x UTC). The run's 'lift the collision with first point zero' (a translation)
  would move the modulus [m]^{-1}(S); it is not needed. Correct form: lifting conjugate sections to the Galois cover
  X' = E - [m]^{-1}S pairs Q' above Q with a deck translate P' above P, with sections conjugate by Delta_{X'}; so Q' - P' has
  p-power order p^b in G' (torus without p-torsion), b <= a since m(Q' - P') = Q - P and (m, p) = 1; h with div h =
  p^b(Q' - P'), h = 1 on the m^2|S| points of [m]^{-1}S, has h - 1 with only the pole P' of order p^b < m^2: contradiction.
  The Kummer kernel of G(K) is p-primary: E(K) f.g. (Lang-Neron, finite constants), T(K) = finite (order prime to p) x free.

## Verdict

Steps 3-5 and all of Step 6 hold (genus one in the corrected form above, which the note uses). With a28ea31f's re-proof of Steps 1-2, A05 is checked for proper curves of genus >= 2 over
finitely generated fields of characteristic p, which is the core statement for the H07 note.

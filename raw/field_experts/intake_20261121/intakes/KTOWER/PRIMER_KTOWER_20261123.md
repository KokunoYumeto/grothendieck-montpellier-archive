# Primer: KTOWER (prompt 47, "the Galois action on the tower, the K-groups of Z and cote 149")

ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026. This is a recall of my three intakes (cp03, cp09 part 2, cp11)
and of `reports_20261122/paper_seeds/SEED_KTOWER.md` (Paper 1). The run is GPT-6 Astra (ChatGPT Pro mode). Its last
return is checkpoint 11 (22 Nov 00:01 UTC):
`research_returns/KTOWER_checkpoint_11_20261122T0001Z_unzipped/KTOWER.tex` (21,649 lines). Inputs are as in K17: the
archive's `OneCharU_s` (an intermediate theorem of the Lean archive, not RH), Hart–Harvey–Ong and Rognes–Weibel.

## Main results

**KT-ONECHAR-CLOSED (source trace, confirmed by me; not compiled).** `OneCharU_s` has a closed proof term at the pinned
commit (KTOWER.tex 134–282). Its nine hypotheses are discharged in `CorGKOf.lean:10–18`, and line 25 closes the record
hH. Coverage also needs `Keep.levelKA_alt` applied to `hH.toClassicalTheorems`. I reported that step missing; the run's
later paper includes it. No `#print axioms` has been run.

**Coverage (checked by me; KMSW, Shin, Adler–Lansky, Carayol, Saito, Colmez–Fontaine carried; lines 813–1052).**
- *Compact U(3).* Every source-admissible rank-three ρ comes from the level-one compact U(3) space M_{e−1}, with trace
  α/p^e.
- *Rank two.* Every rank-two ρ comes from S_{2e+1}(Γ_0(3), χ_{−3}), with trace 1 + a_p/p^e. The argument at ℓ uses
  Saito's compatibility and slope 2e, which forces the monodromy N = 0.

**KT-K52-K56-K60, KT-K64 … KT-K80-VANISH: K_{4k}(Z) = 0 for 13 ≤ k ≤ 20, so for all k ≤ 20 with K17.**
- *Pattern of each proof* (KN.1–KN.6; theorems at 2674, 3287, 3495, 3664, 3854, 4059):
  1. Form C_p = P(1 + p^e + p^{2e})·Q(1 + p^{2e}) at p = 7 and 13.
  2. Compute gcd(C_7, C_13) = (small primes)·M_1 M_2^3.
  3. A prime ℓ ≥ 2^31 dividing K_{2e}(Z) must divide M_1 M_2.
  4. Show that the alternate Q(√−7) unitary determinant and the classical cubic determinant
     J_e = det((1 + 2^{2e})^3 − T_2^3 | S_{2e+1}(Γ_1(7))) are units modulo each M_i.
  5. K17-MINUS7-GENERAL-SOURCE (checked) then gives S_ℓ = 0.
- *Checks:*
  - I recomputed both classical halves in my own models (all 16 initial and 16 alternate values agree).
  - I recomputed the gcd step from the run's U(3) values.
  - I read every deduction.
  - The U(3) halves are carried.

**KT-QUARTIC-QUARTER (statement level).** log|K_{2e}(Z)| < e⁴/4 for even e ≥ 2, and (239/960)e⁴ for e ≥ 4. This
replaces K17's unevaluated C(2k)^7.

**The all-weight reduction for Vandiver at every prime (orders 1–4 and 6 checked by me; the class-number bounds
carried).**
- *KT-SMALL-ORDER* (11699): if ord(ω^e) ≤ 4, then A_p^{[−e]} = 0. Write F = L^{ker ω^{−e}} of degree ≤ 4. Then
  p ∤ h(F) by Le (quadratic), Moser–Payan (cubic) and Moser (quartic). Since jN = Σ_H, a class fixed by H is killed by
  |H|.
- *KT-ORDER-SIX* (11924):
  - J = h_6/(h_2 h_3) is an integer, because of the Hilbert class-field product lemma.
  - Louboutin's regulator lemma gives J = Qp|L(1, χ)|²/(48R^*).
  - Gras gives R^* ≥ (3/16) log²((p−20)/4), and Louboutin gives |L(1, χ)| ≤ ½(log p + κ_0).
  - Together: J < 49p/108 < p.
- *KT-ORDER-FIVE-LENGTH-ONE* (12107): the four order-5 components have total length ≤ 1. Schoof–Washington's regulator
  bound gives h(F) < p²/6.
- *KT-ORDER-FIVE-STRICT-CYCLIC* (12245): each order-5 strict group and its K-group are cyclic.

**The CM branch (my computation, cp09).** The CM forms in S_{2e+1}(Γ_0(3), χ_{−3}) give the certificate factor
N_{Q(ω)/Q}(1 − π^{2e}) with π = 3 + ω. This factor is a non-unit along arithmetic progressions in e for each fixed
auxiliary prime. So no single fixed-prime certificate is uniform in e. A varying prime or field is not excluded.

**Geometry (statement level).**
- KT-FF-SEC refutes finite-field section surjectivity (the curve checked by me, cp03).
- KT-POLY-FAIL and KT-ARTIN-FAIL are counterexamples to point separation, with a positive refinement.
- KT-F149-REVIEW and KT-F149-COMP compare the normalizer statements of cote 149.

**Soulé 2003, Lemma 9 (refuted; source read).** The lemma, p. 778, claims an element of order p in GL_N(A) has
p ≤ 1 + sup(r, N). It fails for F = Q(√−7), N = 3, p = 7. The correct bound is p ≤ 1 + rN.

## Open rows (cp11 review 06: no movement)

- **Q1B, Q1C: Vandiver at every prime.** Two gates remain:
  - the components of order 5 (at most one class of order p) or of order ≥ 7;
  - the third auxiliary unit inside GD, and the stable rank-three sources that are not essentially self-dual.
- **Q5: Ihara beyond Greenberg.** The gate is arithmetic Triple-NV, or a positive-rank substitute.
- **Q7: route 2.** The gate is Raynaud-theta incidence for the primitive doubling orbits.
- **Source gaps.** Berger–Klosin Lemma 6.8: the run reports a sign-inference gap that I did not judge. The KMSW
  background (from NIGHT_AFTER_ALPOGE): its stabilization inputs, Mok and the weighted fundamental lemma, are not yet
  confirmed in the published literature.

## Where it went

- **Hexagon H18:** K_{4k}(Z) = 0 for k ≤ 20. The main session's Pintar gate (hexagon:2611.00829, k ≤ 26 under stronger
  simultaneous hypotheses) finds ours not superseded. Still gated on:
  - the compiled axiom print;
  - an independent U(3) computation;
  - the KMSW citation.
- **The seed:** SEED_KTOWER Paper 1.
- **The run NIGHT_AFTER_ALPOGE Part C:** the audited baseline paper, with my K_12 certificate recomputed a third time.

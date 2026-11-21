# PF26 audit notes

Date: 21 November 2026. Agent: `/root/pf26_audit`; model: GPT-6 Astra Pro;
effort inherited, not externally exposed. The source was the attached 48-page
OpenAI PDF dated 4 October 2026. This audit is a full mathematical reading of
the invoked proofs, with targeted independent calculations; it is not a formal
verification or an implementation of the factoring algorithm.

## Completed scope

- Read every page of PF26 §§2–10 (pp. 6–44), the complete algebraic proof used
  by Theorem 1.2, Proposition 8.1 and Proposition 10.1.
- Read Theorem 11.1, Lemma 11.2 and Proposition 11.3 (pp. 44–46), together with
  the concluding GRH comment on p. 47. Did **not** inspect the companion's proof
  of its zero-free theorem. The companion remains a separate outside input.
- Read GRH_NIGHT CX-ALG-024, CX-ALG-027 and CX-ALG-028 in full and reconstructed
  the CX-ALG-028 transfer from the primary-table interface.
- Rendered and visually inspected PF26 pp. 35, 44 and 45, confirming the
  large-characteristic cutoff, primary-table hypotheses and exact analytic
  premise. The remaining pages were checked in extracted text, including all
  mathematical arguments.
- Freshly opened Bach–Sorenson's primary author-uploaded PDF: its Theorem 5.1,
  p. 1729, agrees with the CX-ALG-024 bound. Its older computer-assisted constant
  calculations were not rerun.
- Freshly read SGA1 V §7 opening paragraphs, recomposed p. 115, PDF p. 131,
  original marginal pp. 140–141; SGA1 I Corollary 7.4, recomposed p. 9,
  PDF p. 25; and Grothendieck (1957), Théorème 2.1, printed p. 126 with the
  algebraic-base comment on p. 127.

## Findings

1. **MA-PF-001:** no gap found in the full reading of the invoked algebraic
   proofs. The theorem being used as `PF26` is the auxiliary-prime/primary-table
   algebraic interface, not the companion analytic theorem. The latter is a
   fixed-width zero-free region, not RH: PF26 Theorem 11.1, pp. 44–45, for all
   finite-order Hecke characters on cyclotomic fields containing μ12,
   Re(s)>1−10^−6, without height or conductor restriction.
2. **MA-PF-002:** CX-ALG-028 is complete relative to that algebraic interface
   and the cited classical analytic input. The residual set can equivalently
   be tested by r² | p^(r−1)−1, with r prime ≤d and r∤(p−1)m. The statement
   uses the exact large-characteristic threshold p>B^200000. The small branch
   is unconditional.
3. **MA-PF-003:** each residual pure-field quotient is exactly one Hecke
   L-function, L_{Q(ζ_r)}(ψ_{p,r}), not a product. The proof is the equality
   of actual representations P=1⊕Ind_{C_r}^{AGL1(F_r)}ψ, including inertia
   invariants at ramified primes. Any faithful ψ gives the same induced
   L-function. The primitive Hecke local factors must be retained.
4. **MA-PF-004:** full RH at those residual functions is more than the
   algorithm requires. A common fixed strip Re(s)>1−δ, with δ>0 independent
   of p,m,d, suffices. The proof gives auxiliary primes O_δ(B^(20/δ)) with
   congruence only modulo r. This is a smaller sufficient analytic premise,
   not a proof that A supplies it and not a necessity statement.
5. **MA-PF-005:** for d=3, the arithmetic residual condition is p≡−1 mod9
   and 3∤m; its character is a non-Q-induced order-3 Hecke character over
   Q(√−3). The explicit prime p=269 supplies such a character, but its actual
   PF26 branch is small characteristic (B=60), so that particular computation
   needs no analytic input. A true residual family takes primes p≡8 mod9
   above the exact threshold; Dirichlet gives infinitely many.

## Delicate steps checked independently

The source's local matrix models have the correct commutation signs; all
residue roots required by the norm solver follow from the norm promise. The
completion-to-rational-order passage is justified by finite congruence data.
The vector bundle on P¹ is split over the actual finite field by the proof
in Lemma 6.3, not merely over an algebraic closure. Its global endomorphism
fiber is a full parabolic algebra; the trace pairing and its common column
kernel genuinely produce a rank-one idempotent. A lift has constant
characteristic polynomial T^(r−1)(T−1), so its rth power is a rank-one
idempotent. The final left-ideal equation then yields a norm solution.

For the geometric separator, the infinity-lattice relation needed at test
t+1 is obtained after equality of the tth labels. It is not assumed in
advance. The Frobenius filtration proves rationality for every division
chosen by the deterministic routine. Large infinity coefficients stay in
binary function circuits. All potentially genus-dependent dimensions are
bounded by fixed powers in Proposition 10.1; primary logarithms use digit
loops and no primary subgroup is enumerated. Recursive table construction
only factors Φ_r of smaller degree and never rebuilds the table.

No algebraic gap was found. This outcome does not check the companion
analytic theorem and does not upgrade the manuscript to a refereed theorem.

## New-proof check

After writing `pf26.tex`, read all five statements and their proofs from the
file in full. Rechecked the exponent/valuation identity, the induction
character values, all ramified Euler-factor conventions, the fixed-strip
prime-detection error, the dependence on a common δ, and the p=269 branch.
The minor notation issue in the smoothed sum was corrected by defining Ψ_D
and its discriminant explicitly. Root can independently review
MA-PF-003 and MA-PF-004 before integration.

The exact arithmetic supplement `checks/pf26_arithmetic.py` passed 4,228
valuation/congruence comparisons and 2,408 cubic residual-set comparisons.
These finite computations supplement their proofs; they are not evidence
that PF26's norm solver was implemented.

## Primary web sources opened

- PF26 official metadata:
  https://github.com/openai/math/tree/main/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026
  Search reference `turn616189277academia34`; opening the repository folder
  itself returned a restricted-URL fetch error. All proof claims use the
  supplied PDF, not the metadata snippet.
- SGA1 primary recomposition: https://arxiv.org/pdf/math/0206203
  `turn769065806view0`, exact V§7 excerpt `turn686783143view1`.
- Grothendieck (1957) primary scan:
  https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf
  `turn769065806view1`, exact theorem excerpt `turn686783143view2`.
- Bach–Sorenson primary author-uploaded PDF:
  https://www.researchgate.net/profile/Jonathan-Sorenson-2/publication/220576951_Explicit_bounds_for_primes_in_residue_classes/links/55100ea70cf2ac2905afbceb/Explicit-bounds-for-primes-in-residue-classes.pdf
  `turn686783143view0`, Theorem 5.1 excerpt `turn755180820view0`.

## References for integration

- OpenAI. (2026, October 4). *Deterministic polynomial factorization over prime
  fields* [Preprint]. Theorem 1.2, p. 3; §§2–10, pp. 6–44; Proposition 8.1,
  pp. 35–37; Proposition 10.1, pp. 41–44; Theorem 11.1, pp. 44–45;
  Lemma 11.2, p. 45; Proposition 11.3, p. 46.
- Bach, E., & Sorenson, J. (1996). Explicit bounds for primes in residue
  classes. *Mathematics of Computation, 65*(216), 1717–1735. Theorem 5.1,
  p. 1729; precise ERH convention §2, p. 1720 (the latter carried from the
  previous run's exact source check).
- Grothendieck, A. (1957). Sur la classification des fibrés holomorphes sur la
  sphère de Riemann. *American Journal of Mathematics, 79*(1), 121–138.
  Théorème 2.1, p. 126; algebraic-base comment p. 127.
- Grothendieck, A., et al. (1971/2003). *Revêtements étales et groupe
  fondamental (SGA 1).* Exposé I, Corollaire 7.4; Exposé V, §7, opening
  paragraphs. Recomposition arXiv:math/0206203v2.

No archive cote for the new factoring algorithm was identified. Its exact
Grothendieck connections are the published vector-bundle splitting theorem,
the finite étale component dictionary, and the Artin/representation-ring
decomposition. There is no new EGA or FGA theorem asserted.


## Additional exact local check for p=269 (2026-11-21)

Independently verified at input_audit's request: f(X)=X³−269 has f(−1)=−270 of3-adic valuation3 and f'(−1)=3 of valuation1, so strong Hensel gives a root in Q3. Thus over K3=Q3(zeta3) all roots lie in the base, and the order3 character is locally trivial at3, with primitive Euler factor(1−3^(−s))^(−1). At269, K/Q is inert and x³−269 is Eisenstein over K_(269), giving a totally tamely ramified cubic extension, conductor exponent1 and local Artin factor1. No other finite prime ramifies. Hence the exact Hecke conductor is(269), norm269², and arithmetic conductor |D_K|Nf=3*269². This sharpens the earlier conservative conductor-support statement; it does not change the small-characteristic PF26 branch warning.

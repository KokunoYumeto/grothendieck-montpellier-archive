# SA16 (Courbes elliptiques), sweep 3: moduli of elliptic curves (cote 62), the Tate-Deligne Formulaire (cote 63), cote 64

Merged by Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1) on 19 Nov 2026. The first merge was at about
15:4x UTC; this full merge was made at about 16:5x UTC, after the reader finished.

**State of the reading: read in full.** The reader was a56665404be0d8be6 (Claude Opus 5.5 at effort max).
- It was interrupted at about 14:2x UTC on 19 Nov, then resumed, and it finished all three stretches.
- Its files are in readings/:
  - `c62_c64.md`: cote 62, scans 2-50, and cote 64;
  - `c62b_c63.md`: cote 62, scans 51-97, and cote 63.
- Each file has its CHECK_EVENTS and CORRECTIONS. Their rows are folded into CHECK_EVENTS.tsv (56 rows) and
  CORRECTIONS.tsv (39 rows).
- HUNCHES.md, RESEARCH_PACKAGES.md, DEPENDS.tsv and DELIVERABLES.tsv carry the readers' own sections.
- The rows of the first, partial merge are kept in sweep3/_premerge_SA16_20261119/.

**Not yet read in sweep 3:** nothing.

Two sweep-2 decisions hold for cote 63, and both readings confirm them:
- REPORTS/hands_formulaire_and_tate.md: the margins are probably in his hand, 6:39 is in Tate's hand, and 6:38 and
  6:40-46 are his;
- the margin "faux si S pas connexe" (63:32) is right. 63:96 confirms it.

## What the cotes contain

**Cote 62, scans 2-50: his manuscript "Modules des courbes elliptiques".**
- the pole filtration, Weierstrass coordinates and the cubic (62:4-11; SA16-1, SA16-2, SA16-8);
- the moduli problem: special bases, the group G, and normalizations (62:11-17);
- the scratch sheet on j (62:19), the discriminant (62:21), and j in roots and cross-ratio (62:23, 25);
- the λ-line: S_3, the involution σ, and the two quotient stages (62:28-40; SA16-4);
- trisections, S_3-torsors and the invariant of a pointed genus-zero curve (62:42-50; SA16-5);
- reused Bourbaki typescripts (n° 276 and n° 272) on the backs, identified and not studied (SA16-6, SA16-7).

**Cote 62, scans 51-97.**
- the end of the trisection manuscript (62:52, 54);
- two scratch sheets (62:57, 58);
- "Théorie transcendante (formules classiques)" in two versions (62:59-74 and 62:75-97; SA16-12): p, ζ, σ, θ, J and
  Legendre-Jacobi. His slips in the classical formulas are corrected in CORRECTIONS.tsv.

**Cote 63: the Tate-Deligne Formulaire and other authors' typescripts, identified and not studied, with eleven pages
of his.**
- 63:66-77: the algebraic and the Hodge splitting of H^1, with his questions of 63:67: when α = 0, and when α is
  algebraic (SA16-12, SA16-14; package R5);
- 63:96-100: the divisors of c_4, c_6 and Δ on the modular site, and level 3 at the prime 2 (SA16-3, SA16-19;
  package R6).

**Cote 64 (1981-82, dated by the Montpellier circulars it is written on): moduli in characteristic ≠ 2.**
- Part I: the combinatorics of S_4, the square and the cube, and Z/4-modules of rank 2 (64:2-43; SA16-9);
- Part II: the octahedral configuration of a Klein group acting on P^1 (64:44-69; SA16-9, SA16-11);
- Part III: the Legendre pinning (64:70-100; SA16-10);
- Part IV: Weierstrass p, and the unfinished passage from level 4 to the pinning (64:101-126);
- the transcendental approach (64:129-152; SA16-12, SA16-13);
- normality of quadratic extensions (64:153-157; SA16-15);
- planning notes.

## The findings that bear on research (the readers' sections 0 and 6; checks in CHECK_EVENTS.tsv)

1. **His open step on 64:121, "Dieu sait comment".**
   - The level-4 relative Jacobi pinning gives ∏_i (p(x_i) − p(ε_i)) = ±√−1·Δ_0. So it fixes α: ω_J = μ_4^*.
   - What remains is κ up to sign (R2).
2. **The octahedral theorem and Corollary 1 of 64:52-53 need characteristic ≠ 2, 5.**
   - In characteristic 5 the divisor {0, ∞, ±1, ±i} is P^1(F_5). Its automorphism group is PGL_2(F_5) = S_5, the
     stabilizer of two of its points is μ_4, and it carries five regular octahedral structures (R3).
   - His margin on 64:50 saw the exception; his text does not carry it.
3. **64:103-108.** Θ_δ acts on F_n/F_(n−1) by −nδ, not by δ (his own Prop. 3 on 62:7-8).
   - So Ker Θ_δ = k only in characteristic 0.
   - The boxed relation is p'^2 = 4(p^3 + ...).
4. **64:25 was decided on the ink.** "qui [ne] sont [pas] dans V", with "ne" and "pas" struck through: his text is right.
5. **His criteria on 62:19 answer his question "quels i conviennent ??" of 62:46**, over a DVR with 6 invertible.
   Normal bases are open (R1). On 62:48, H^1(S, Z/3) is H^1(S, μ_3).
6. **His question on 63:67 (R5):**
   - is α = 0 exactly at τ = i and e^(2πi/3);
   - is α algebraic exactly in the CM case?
7. **63:99-100 (R6):**
   - c_4 and c_6 in W(F̄_p)[[t]] at the two supersingular points (p = 2 and p = 3);
   - which surjection SL_2(F_3) → F_4^* acts on the vertical tangent line at 2.

<!-- readers:start -->
## Sweep 3 readers (files in readings/; rows folded into CHECK_EVENTS.tsv and CORRECTIONS.tsv)

- **readings/c62_c64.md**: cote 62 scans 2-50 ('Modules des courbes elliptiques') and cote 64 in full (1981-82, dated by the Montpellier circulars it is written on). Read by a56665404be0d8be6 (Claude Opus 5.5 at effort max; interrupted at about 14:2x UTC on 19 Nov, then resumed and finished): 37 check events, 25 corrections, 6 hunches, packages R1-R3. Findings: 64:121, his open step 'Dieu sait comment': the level-4 pinning fixes alpha (prod_i (p(x_i) - p(epsilon_i)) = +-sqrt(-1).Delta_0), and kappa up to sign remains (R2). The octahedral theorem of 64:52-53 needs characteristic != 2, 5: at 5 the divisor is P^1(F_5), its automorphism group is PGL_2(F_5) = S_5, and it carries five regular octahedral structures (R3). 64:103-108: Theta_delta acts on F_n/F_(n-1) by -n delta, so the boxed relation is p'^2 = 4(p^3 + ...). 64:25 was decided on the ink: his text is right. The criteria on 62:19 answer his question of 62:46 over a DVR with 6 invertible (R1). On 62:48, H^1(S, Z/3) is H^1(S, mu_3).
- **readings/c62b_c63.md**: cote 62 scans 51-97 and cote 63 in full. Read by the same reader a56665404be0d8be6 (Claude Opus 5.5 at effort max): 19 check events, 14 corrections, 3 hunches, packages R5-R6. Cote 62:59-97 is his 'Théorie transcendante (formules classiques)' in two versions (p, zeta, sigma, theta, J, Legendre-Jacobi); his slips are corrected in the classical formulas. Cote 63 is mostly other authors' typescripts, identified and not studied. Eleven pages are his: 63:66-77, on the algebraic and the Hodge splitting of H^1 with his questions of 63:67 on when alpha = 0 and when alpha is algebraic (R5); and 63:96-100, on the divisors of c_4, c_6 and Delta on the modular site, and level 3 at the prime 2 (R6). 63:96 confirms his margin on 63:32.
<!-- readers:end -->

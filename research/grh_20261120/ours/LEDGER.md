# LEDGER, bridges from Alpöge's RH/GRH (20 Nov 2026)

Run: Claude Opus 5.5 at effort max, bridges run (resumed agent a84c887c chain), 20 Nov 2026. Work began 19:36 UTC; paused; resumed; capped by the coordinator at about 21:10 UTC (50,000-token tie-up).

| Row | Status | Gate (strongest proved reduction) |
|---|---|---|
| Q01 RH for zeta_X over Z | partly proved | F1 for abelian Artin-Tate X; general X needs GRH for non-abelian Artin L and RH for positive weight |
| Q02 RH for pure motives over Q | partly proved | F1, F2 for abelian Artin-Tate motives |
| Q03 cote 34/64 openness of [pi_0,H] | open | derive from purity (Weil I); read 34/53-63 for 1.1 |
| Q04 cote 34/74 (2.5.5) | settled earlier | Weil's theorem for curves |
| Q05 standard conjectures | open | themselves |
| Q06 K-groups of Z (step 17) | open | Vandiver |
| Q07 Koiran without GRH | open | GRH for Dedekind zetas of non-abelian fields |
| Q08 Miller/Bach | settled | A3/A4 + Bach 1990 |

**Update, 21 Nov 2026** (corrected 21 Nov 2026 after the intakes of CX_GRH, ALPOGE_BRIDGES and ALPOGE_GCT, Claude Opus
5.5 at effort high; the rows above are kept as the 20 Nov record):

| Row | Status | Gate (strongest proved reduction) |
|---|---|---|
| Q01, Q02 | partly proved; F1/F2 = ALPOGE_BRIDGES BR-AT-01 (confirmed) | conditionally on Masullo (M), the non-abelian Artin part is met in the zero-location sense (Brauer remark, CX_GRH intake §3); remaining gate: RH for motives of positive weight that are not Artin-Tate |
| Q01, Q02 (later, 21 Nov) | partly proved: A gives abelian Artin-Tate (F1 = ZETA_TWO ZT01); M gives every Artin-Tate count, every Spec O_K (ZT02, ZT03) and every pure motive in Anderson's CM category (CM01, given Anderson Cor. 5.7.2; M for infinite-order unitary characters) | supersedes the gate in the row above: Q01 for general X reduces to finitely many L^S(H^j(Y_a)) and the bad fibres (ZT06); remaining gate RH for the non-CM summands up to Tate twist (first case h¹(E), E non-CM; ZT07); not a weight condition (corrected 21 Nov 2026 after the intake of ZETA_TWO, Claude Opus 5.5 at effort high) |
| Q03 cote 34/64 | literal statement refuted (HODGE_SIGN Q3-01) | the canonical [P,H] open in H (Q3-03, Q3-04); curve purity suffices (Q3-02) (corrected 21 Nov 2026 after the intake of HODGE_SIGN, Claude Opus 5.5 at effort high) |
| Q06 | open | Vandiver; ALPOGE_BRIDGES BR-MIX-01 (confirmed): good-prime L-data see only gr^W, so they cannot compute the Ext groups of step 17 |
| Q07 Koiran | proved conditional on M (CX_GRH CX-K01, CX-K02); A_D promise version proved (CX-K03); abelian-witness route refuted (CX-K04; ALPOGE_GCT C-GRH-03, x³−2) | RH for ζ_E, E the field of one bounded solution, E need not be normal. Locators: Koiran, J. Complexity 12 (1996), §2 Thm 2, pp. 276-277, §5 Thm 9 and Cor 1, p. 282; DIMACS TR §2 Thm 2, pp. 5-6; the 1997 erratum; LO77 Thm 1.1 |
| Q08 Miller/Bach | settled; quadratic Dirichlet characters suffice (CX_GRH CX-N01; ALPOGE_BRIDGES CC-C03) | Bach 1990 Thm 2 p. 372, p. 373; Miller 1976 Thm 2 p. 301; Schoof 2008 Thm 2.2 pp. 105-106 |

Reviews: one (this one, at the cap). Movement since start: Q01, Q02, Q08 changed status.
State: INCOMPLETE (session capped). Approaches tried: Euler-product factorization (F1, F2: works); archive search of the
text of record for RH (only Riemann-Weil questions, cote 34); register scan of BRIDGE_FLAGS.tsv (2 RH/GRH rows, neither
depends on RH over Q); note's steps 3 and 5 (F3, F4 extracted; the qN = M^k + R identity not reconstructed: the Lean folder
Development/WeilBound was not read). Next step: Q03 from purity; then the WeilBound folder for steps 3-5.

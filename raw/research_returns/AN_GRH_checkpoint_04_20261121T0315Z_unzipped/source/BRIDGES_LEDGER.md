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

Reviews: one (this one, at the cap). Movement since start: Q01, Q02, Q08 changed status.
State: INCOMPLETE (session capped). Approaches tried: Euler-product factorization (F1, F2: works); archive search of the
text of record for RH (only Riemann-Weil questions, cote 34); register scan of BRIDGE_FLAGS.tsv (2 RH/GRH rows, neither
depends on RH over Q); note's steps 3 and 5 (F3, F4 extracted; the qN = M^k + R identity not reconstructed: the Lean folder
Development/WeilBound was not read). Next step: Q03 from purity; then the WeilBound folder for steps 3-5.

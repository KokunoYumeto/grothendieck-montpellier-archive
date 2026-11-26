# H18 gate: Pintar, hexagon:2611.00829v1, read and compared (23 Nov 2026, 12:34 UTC)

By the main session 329fb1e6 (Claude Opus 5.5 at effort max), at the user's word of 23 Nov ~11:22 UTC ([the user's words, omitted]).

## What was read
- Leo Pintar, *Hecke calculations for the conditional vanishing of K_{4k}(Z) through degree 104*, hexagon:2611.00829v1
  (21 Nov 2026, 2 pp.; contributions: "Leo Pintar initiated and led ...; OpenAI Codex contributed to the mathematical
  arguments, wrote and ran the verification code, and drafted the manuscript"; supplement
  https://github.com/leopintar05/hecke-k-theory-104/releases/tag/v1.0). Read in full (PDF text layer).
- Ours, at the places that decide the comparison: K17 Lemma K17-S17-UNIT (K17.tex 2804-2852), Proposition
  K17-MINUS7-GENERAL-SOURCE (K17.tex 6277-6436, (GS7.1)-(GS7.4)), KTOWER (KT-H.2) (KTOWER.tex 2573-2586), and
  reports_20261122/paper_seeds/SEED_KTOWER.md (inputs of Theorem A).

## What Pintar proves
K_{4k}(Z) = 0 for 1 <= k <= 26, **assuming three inputs** (his §2):
1. **Strict Selmer comparison**: the length in Alpöge's OneCharU_s (N = 2, trivial character, coefficients Z) measures the
   strict group S_e.
2. **Coverage**: the systems admitted by Adm3U_s and Adm2A occur in the tested weights, levels, twists and Frobenius
   normalizations (compact unitary transfer, self-dual reduction, classical spaces; Loeffler's two-class model).
3. **Simultaneous residual traces**: for each field, S_e != 0 supplies one admitted system at one coefficient prime
   realizing the target traces at all places compared together.
Input 3 is used in his second-field step (§1): at the two places above 2 in Q(sqrt -7) he sums the two directed
operators and uses the conjugation J (v - Jv), with target t = 2u, giving L = t^2 I - t(A + A') - (B + B')(D + D') of
dimension 2925 in degree 104; degrees 76-100 likewise (table, §2). His §2 also reports first-field/second-field
determinant tests for degrees 52-72. He credits "a 21 November report in the Grothendieck-Montpellier archive" (ours)
for the conditional calculation through degree 48.

## How ours relates
- Our criterion is single-place. K17-S17-UNIT: fix one s in G_K; if tr rho(s) - t is a unit for every admissible rho,
  the strict Selmer length is 0. On the first field the gcd over T_7 and T_13 applies the criterion at each place
  separately (an l dividing the length divides each determinant det(T_s - t_s)), so it needs no simultaneity.
  On Q(sqrt -7), (GS7.1) and KTOWER (KT-H.2), D_e = E_e^2 I - E_e 2^k S_11 - 2^{2k} inc S_21, are full-space
  determinants in ONE minuscule direction at one Frobenius above 2 ("the inherited integral conjugation involution also
  covers the opposite minuscule direction"). **So our Theorem A (k <= 20) does not use Pintar's input 3.**
- Inputs 1 and 2 are what our seed claims to supply: input 1 from the archive's closed OneCharU_s chain with the
  identification (K5) (source trace, uncompiled; gate: compile the pinned archive and run #print axioms, incl.
  Keep.levelKA_alt closed by hH.toClassicalTheorems), input 2 from the published coverage theorems (KMSW generic
  pure-inner case, Shin, Carayol, Saito; the KMSW background Mok, Chaudouard-Laumon, Moeglin-Waldspurger still to cite).
- **Verdict.** H18 is not superseded. For k <= 20 our statement rests on one hypothesis fewer than Pintar's; for
  21 <= k <= 26 Pintar's conditional result is the only one. H18 is a "needs a pass" note: cite Pintar exactly (his
  three inputs, his range, his single-place-free method), state ours with its inputs, no priority claim (his own text
  cites our 21 Nov report for degree <= 48).

## Check events
| statement | date | who | type | outcome |
|---|---|---|---|---|
| H18 vs Pintar 2611.00829v1 | 2026-11-23 | Claude Opus 5.5 at effort max, main session 329fb1e6 | targeted proof check | Pintar read in full; our K17-S17-UNIT, GS7.1-GS7.4 and KT-H.2 read; our deduction is single-place and needs no simultaneous-trace hypothesis |

## Whom to write to when posted
Leo Pintar (information: our single-place certificates for degrees 52-80 remove his input 3 in that range; his
degrees 84-104 keep it).

# Intake for the results graph: MOONSHINE_AFTER_ALPOGE, checkpoint 01 (24 Nov 2026, 20:45 UTC)

Claude Opus 5.5 at effort max, agent a74a9a15292272046, 25 Nov 2026, for main (session 329fb1e6). The run is GPT-6 Astra
(ChatGPT Pro mode); its records give its effort as "not exposed" and every one of its checks is by an instance of the same
model. The full intake with ranked items and the passages is the earlier note
`field_experts/intake_20261121/intakes/MOONSHINE_AFTER_ALPOGE/INTAKE_MOONSHINE_AFTER_ALPOGE_20261125_cp01.md` (same
agent, 25 Nov); its five check events are in the `_CHECK_EVENTS.tsv` beside it. This note gives the graph's view: ids,
checks, relations, to-dos. Staging: `results_graph/staging/a74a9a15292272046/` (5 checks, 18 relations, 7 points from this
run; generator `make_moonshine.py`).

Ids follow the builder's rule RUN:<TeX label> (the run is not yet in graph.sqlite). Paper A = `workbench/work/moonshine/
v1/paper/` (main.tex and nine section files); paper B = `workbench/work/cm_hecke/v1/paper/cm_hecke_windows.tex`.

## What the return adds, by id

| Id | Where | Content (my words) | Checks by me (25 Nov) |
|---|---|---|---|
| thm:window, cor:three | B:132-158, proof 365-470 | one-sided bound on the centred prime-ideal ramp sum over arbitrarily late windows => RH for unitary Hecke characters of nonzero angular type of an imaginary quadratic field; for psi36, psi27, psi36^3 also Sym^3 eta(6t)^4 | targeted proof check against Alpoge's Lean `Deduction.landau_window`: no fault |
| thm:phase, prop:colour, prop:twist, lem:one, prop:finite-family, prop:auxiliary | B:94-111, 240-318, 339-363, 491-535, 646-697 | finite-phase identity; unit colour = infinity type mod 6; E36 vs E27 cubic twist; nonvanishing on Re s = 1; no fixed finite Dirichlet family carries the angular primes; continuation of Hu's principal Euler factor | none |
| thm:intro-dirichlet / thm:all-shadow-characters | A main.tex:92-102; shadows.tex:33-83 | character constituents of every umbral shadow and twining | none |
| thm:shadow-zero-classification, thm:l6-mixed-zeros | A shadows.tex:90-197 | linear zero counts in strips 3/4 < Re s < 1 + eps for mixed components; S^X_1, S^X_5 at lambency 6 | computation: eight zeros off Re s = 3/4 |
| thm:l6-sympowers | A shadows.tex:220-280 | twined shadow = det, Sym^2, Sym^3, Sym^4 of V | used and rechecked (the lambency-6 pass's C1) |
| thm:niemeier-offline | A niemeier_zeros.tex:23-102 | linear zero counts in 23/2 < Re w < 12 for all 24 Niemeier Epstein zeta functions | computation: six Leech zeros, first w = 11.6084773365 + 78.7678190294 i |
| thm:residue-eta, prop:residue-symbol, thm:primitive-cube, thm:residue-stability | A mason_theta.tex:11-190, 447-500 | Mason family of S = <289>; residue symbols; primitive cube with all local factors; residue action on J and its eight overlattices | none |
| lem:level-three-basis, thm:universal-theta-coordinates, thm:129-theta | A mason_theta.tex:192-330 | theta coordinates of the 129 plane sublattices: 18 series | targeted check of the q^2 step and of J's coordinate: no fault |
| thm:weight-one-list, prop:mock-test-function, prop:mock-shadow-Mellin, thm:fricke-glue, thm:cusp-isogeny, thm:cm-theta-zeros, thm:ogg-cutoffs, thm:m11-class, prop:m11-full, thm:tunnell-multiplicity, prop:all-scalar-shadows | A weight_one.tex:29; mock_mellin.tex:41, 93; geometry.tex:18, 90, 159, 220; class_numbers.tex:32, 140, 193; all_lambencies.tex:7 | weight-one Conway eta forms; mock Mellin transform; Fricke constants; cusp-cover isogeny; CM zeros of Niemeier theta series; Ogg cutoffs; M11 class-number part; Tunnell factor two | none (bodies not read by me) |

## Relations entered (relations.jsonl)

Same: thm:l6-sympowers = LAMBENCY6_PASS C1; thm:residue-eta = atlas B3; prop:residue-symbol = atlas B14; thm:fricke-glue =
atlas B5; prop:colour (last assertion) = pass C5; prop:twist = atlas correction 4. Sharpens: thm:primitive-cube (atlas B4,
no omitted primes), thm:ogg-cutoffs (atlas B6; the class-number formula is Ogg's, 1974 p. 452), thm:cusp-isogeny (B13),
thm:cm-theta-zeros (B7). Settles: thm:shadow-zero-classification (atlas correction 1), thm:l6-mixed-zeros (atlas G2),
thm:niemeier-offline (atlas G3). Generalizes: thm:intro-dirichlet (atlas B1). Uses: thm:universal-theta-coordinates uses
S6_05_ARITHMETIC:B.9; thm:window uses Alpoge's `Deduction.landau_window`. Refutes: B:571-589 refutes the atlas's step-18
hypothesis (§5 item 12). Other: atlas H1 against the zero-free half-planes of Hu and Liu as the run cites them.

## Points entered (points.jsonl)

The lambency-6 pass's C1-C5 (LAMBENCY6_PASS.md:36-92) and my two spot-check computations (sc1_run.log:1-17).

## To-dos (action, target, owner)

- Verify the Saias-Weingartner locator for strips inside the critical strip; target A shadows.tex:126-129; owner: the next
  moonshine intake (Claude Opus 5.5).
- Verify Nakamura-Pankowski Main Theorems 1-2 and Theorem E against the source; target A niemeier_zeros.tex:58-85; owner:
  the same.
- Check the Cheng-Duncan-Mertens factor two and cusp shift at the source before any letter; target A
  tunnell_normalization.tex:10-20 and class_numbers.tex; owner: the same, then main for the letter.
- Read and check the bodies of weight_one.tex, class_numbers.tex, geometry.tex, mock_mellin.tex, all_lambencies.tex,
  eta_signed_mellin.tex; owner: the next moonshine intake.
- Audit Hu 2610.00216v2, Gao 2611.00334v1, Liu 2611.00741v1 (statements, dependencies, certificates) before our records
  use their half-planes; target atlas H1; owner: a GRH-rung field expert.
- The window inequality of thm:window for psi36, psi27, psi36^3: no proof in the return; owner: the run (next checkpoint)
  and the next prompt on that gate.

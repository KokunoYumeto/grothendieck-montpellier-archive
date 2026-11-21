# Pencil agent status — 2026-11-21, first-checkpoint preparation

## Completed and checked

- pencil_fragments.tex: P-01–P-08. Exact torus reduction for all four families and arbitrary j; exact adjacent-pair reduction for j=2 and arbitrary b; exact b=2,j=2 minima 3/3/6/6; explicit star and anchored-shape degenerations; determinant Borel order-ideal reduction; eleven- and twelve-term exceptional permanent upper curves.
- uniform_fragments.tex: R-02, R-03, R-05. Exact polynomial b=2 minima j=3→8, j=4→9, j=5→11; both det4 and per4 CP border rank at least 42 in the integral coefficient model over every algebraically closed field. R-04 exceptional permanent lower proof is owned by sdp_orbits and independently rechecked here.
- verify_global_bounds.py and global_j345_certificate.json: standard-library-only exact minor verification and exhaustive coverage of all 7,140, 58,905, 376,992 coordinate subsets. Low-support subsets 48, 900, 14,472. Permanent needed minors are units; determinant minors are units times powers of 2, with det=per in characteristic 2.
- Independent alternate R-04 proof: PENCIL_PROOFS.md P-08/P-09 and per5_prolongation_certificate.json. All 26 quotient-weight cases excluded by unit integer minors. This is independent of sdp_orbits' stronger unique-extension proof.
- det7_two_type.tex P-09, det7_two_type_certificate.json, and verify_det7_certificate.py: four determinant seven-plane orbits have BR≥14 in characteristic 0. Complete coverage 1095+50 torus quotient choices, 1089 saturation minors, 3353 linear zero-pattern tests, 53 overlap inequalities; independent checker PASS. Types [0,1,3,6,7,9,12], [0,1,3,6,7,12,13] and their transposes.
- det7_extra_m12.tex P-12, det7_extra_m12_certificate.json: four more determinant seven-plane orbits have BR≥14 in characteristic 0. Same checker with --certificate argument PASS; 108 saturation minors, 140 linear zero-pattern tests. Types [0,1,2,3,6,7,8], [0,1,2,3,4,6,12] and transposes.
- CHECK_EVENTS.tsv records the actual proof reads and computations. The fields_literature agent independently read the full P-01–P-08 and R-02/R-03/R-05 TeX proofs and P-09, with checks in its own events file.

## Current main gate

Root owns the global determinant seven-plane minimum, with 25 Borel order ideals. P-09/P-12 settle eight previously unresolved ideals. Root has separately settled two support 13 ideals by variable-factor Koszul maps.

This agent is treating the four remaining support 11 ideals, up to transpose:

- Type E: [0,1,2,3,6,7,9]. Saturation covers 1189 quotient choices and leaves only 4 distinct-weight pairs. Baseline A-wedge rank 75 leaves allowed increment 3 under hypothetical BR 13. Single-line increment tests are running.
- Type F: [0,1,2,3,6,7,18]. Saturation covers 1143 choices and leaves 67 distinct-weight pairs. Baseline A-wedge rank 71 leaves allowed increment 7; baseline B-wedge rank 116 leaves allowed increment 14. A- and B-line increment tests are running.

The support 9 type [0,1,3,6,7,9,18] and its transpose is assigned elsewhere. No global det4 bound 43 is claimed yet.

## Reproduction

Run from this directory or use absolute paths:

    python check_pencils.py
    python check_finite_differences.py
    python verify_global_bounds.py
    python ../sdp_orbits/check_permanent_apolar_certificate.py
    python verify_det7_certificate.py
    python verify_det7_certificate.py --certificate det7_extra_m12_certificate.json

The first three and the permanent checker use exact integer arithmetic. The det7 verifier uses NumPy integer arrays with explicit modular overflow bounds, not floating point. The det7 certificate generators and exploratory scripts may use SymPy to discover annihilators; the final independent verifier does not import them or invoke a rank/nullspace oracle.

The final-paper finding ID P-08 refers to the finite-difference upper certificate (source-note P-09 upper-bound part), while source-note P-08 is the separately proved background prolongation lemma. Root will normalize hyphenation of finding IDs during assembly.

## Update at 03:43:51 UTC

P-14 is complete: det7_extra_m11.tex and det7_extra_m11_certificate.json prove the Type E and F lower bounds 14 in characteristic zero, including their transposes. The independent verifier PASS covers 2,332 quotient choices, 2,261 saturation minors, 1,547 linear zero patterns, and the conditional-base step. E/F are no longer open. The only remaining determinant seven-plane orbit is the support-9 type assigned to sdp_orbits, subject to the root global coverage audit. P-14 independent whole-proof review by fields_literature has been requested.

## Audit update at 2026-11-21T03:50:06Z

P-14 whole-proof review and standalone replay by fields_literature passed. Independent P-15 determinant standalone replay also passed with exact rational arithmetic and all expected counts; only the root global coverage audit remains before the determinant bound 43 is globally certified. P-13 full-proof/code review and exact replay passed for all five specified permanent support-12 orbits. The extended P-15 proof for two permanent support-9 types has been read in full, with no logical gap; their generalized exact replays remain pending.

## Global audit update at 2026-11-21T03:53:13Z

Root determinant global certificate and independent verifier passed here: all 25 Borel ideals, 2,997 support/Koszul minors, and exact mapping of the 14 prolongation dependencies. Every dependency has been checked. Thus the determinant seven-plane minimum 14 and polynomial determinant border-rank bound 43 in characteristic zero are established subject only to final manuscript assembly checks. All three P-15 support-nine claims, including both permanent cases, now have independent exact rational replays and complete proof/code audits here. The earlier permanent-data pending qualification is resolved.

## Update 2026-11-21T04:21:31Z

P-16 permanent support-eleven proof and exact three-case certificate are complete and independently reviewed. P-19 final permanent support-eleven degree-(2,2) obstruction and P-20 general row-permanent quadratic minima were independently read and replayed here. Both polynomial det4 and per4 now have a complete characteristic-zero bound43 in the parent manuscript.

P-17 determinant ten-plane Borel-flag obstruction is complete: ten representatives and their transposes give18 distinct ideals, not19 (cases4 and10 self-transpose). Its self-contained checker passes22120 exact rational weight-kernel calculations and685 separately evaluated nonzero modular minors. Fields independently read and replayed it. Together with six disjoint Koszul cases,35 of59 ten-plane ideals remain; no44 claim. Final-depth parameter refinements eliminate293 of295 projective branches and force the other2 to fixed lines, while138 earlier parameter branches and53 rigid E remain. All such refinements and higher-prolongation negative probes remain exploratory.

Current work: fields handles the unique earlier support13 projective branch; pencil handles fixed E/higher compatibility and upper-construction ideas; parent tested noncoordinate A9 middle Koszul maps without a new18 bound.

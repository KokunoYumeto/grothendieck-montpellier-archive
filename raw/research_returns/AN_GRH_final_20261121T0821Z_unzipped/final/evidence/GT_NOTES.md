# Finite gentle-group cyclotomic certificates: handoff

## What is proved

`GT_section.tex` contains checked findings T01–T06 with complete proofs of the new forms. `GT_unit_table.tex` is its full 53-row table. The section uses `longtable`, `amsmath`, `amssymb`, and `amsthm` (for `proof`); bibliography entries are in `GT_bibitems.tex`.

Bach 1990 Theorem 3, printed page 372, gives the strict bound **3(log N)^2** for units outside a proper subgroup. Factoring the integer witness gives prime generators coprime to N. Theorem 2 on the same page has **2(log N)^2**, but allows nonunits. The exact distinction, including small-modulus scope, was checked against the scanned original. This corrects an attribution and inference; it does **not** claim that the numerical coefficient-2 generation assertion is false.

The stronger coefficient-2 assertion is proved directly for every N=2^a3^b and N=5^b, with explicit fixed prime generators and a full elementary proof. It was also checked at 53 concrete moduli by exact modular computations and rigorous rational logarithm bounds. There are 4,825 individual unit-word certificates. All 53 checks passed.

The source inventory has 23 entries identifying actual maps and distinguishing multiplier moduli from cusp orders, matrix coefficients, relative power parameters, and group labels/orders. Actual recovered multiplier data include LM8's 24 and 15; LM7's cusp72, branch144, stated288/576, and refined cusp360. Homology coefficient checks j=2,4,8,16,3,9,27,81 correspond to actual cusp order12j. LM8's correcting character modulo p^k needs lambda modulo p^(k+1), not modulo p^k. LM8 C.49's frame levels24/60 are on multiplier one.

A full multiplier image is already supplied by the arithmetic inclusion and the surjective cyclotomic character. Bach supplies bounded generating witnesses or tests. Neither its bound nor our elementary lists test the f-coordinate, a pentagon, or profinite liftability. LM7 E.65 supplies a particularly sharp scope counterexample: ker(Delta) is proper but has the same full multiplier image, and Delta is nonzero on ker(lambda). This application explicitly carries E.58/E.65 as supplied background and does not re-prove the profinite construction.

## Evidence boundary

The original GT_TOWER_CHECK 180-row register/paper was not recovered. Its attached Markdown file is a selected, truncated summary, not a complete row list. Thus the 53 arithmetic certificates are exact but are not represented as an exhaustive inventory of that unavailable run. The complete recovered LM7 register has218rows, though only part of its proof sources was recovered; LM8's register has304rows with source. The inventory marks this distinction.

## Reproduce

Run `python verify_gt_units.py` to regenerate both TSV certificate tables. Run `python check_unit_certificates.py` to re-evaluate the saved words without subgroup search. Supplying integer arguments to the first script replaces the default list, for example `python verify_gt_units.py 12 144`; retain a copy of the existing output if experimenting. The verifier certifies the supplied moduli; it does not identify a missing GT quotient or verify its equations. No external Python package is needed.

## Primary citations

- Eric Bach, *Explicit bounds for primality testing and related problems*, Mathematics of Computation55(1990), no191,355–380, Theorems2–3 on printedp372 and generator consequencep373. DOI: https://doi.org/10.1090/S0025-5718-1990-1023756-8 . Original PDF: https://www.ams.org/mcom/1990-55-191/S0025-5718-1990-1023756-8/S0025-5718-1990-1023756-8.pdf . Direct AMS access was blocked, so the identical original scan was inspected from https://raw.githubusercontent.com/xayahrainie4793/pdf-files-cached-copy/main/pdf_83.pdf . The mirror catalog identifies it as this AMS paper. Original section6 explicitly works with Dirichlet characters; no general-number-field Hecke hypothesis is needed for these two theorems.
- Lamzouri–Li–Soundararajan, *Conditional bounds for the least quadratic non-residue and related problems*, Math.Comp.84(2015),2391–2412, §1.1. Author primary preprint: https://www.math.ksu.edu/about/personal/xiannan/papers/QuaResL1ver2Sound.pdf . Webref turn516555700view0 (earlier); published scanned version webref turn881523367search23. The introduction independently corroborates the constants/coprimality distinction. No later improved theorem is used here.
- SGA1, ExposéV, Théorème4.1 and §7, Galois categories and finite étale schemes. Primary recomposed PDF https://arxiv.org/pdf/math/0206203 (webref turn874470599view0). This is the appropriate framework for Spec Z[1/N,zeta_N] over Spec Z[1/N].

The files `bach1990.pdf`, `bach1990.txt`, and `bach_theorems.png` in this working directory are copyrighted external-source inspection copies. Exclude them from the final deliverable ZIP. The generated proof, scripts, certificate tables, source inventory, and check events are the new deliverables.

## Check-event discipline

`CHECK_EVENTS_GT.tsv` distinguishes full reads of the new proofs, exact computations, rechecked source statements, and background assertions whose original computation/proof was not rebuilt. It does not claim Lean checking, a new proof of Bach, a rerun of Bach's million-modulus calculation, or a rerun of old GT shadow computations. `CHECK_EVENTS_A03_A04.tsv` and `CHECK_EVENTS_A05_STEPS4_5.tsv` record the additional independent-reader checks requested by root.

No archive transcription correction is proposed by this task. The Bach correction belongs in the mathematical input audit, not in cote149's transcription notes.

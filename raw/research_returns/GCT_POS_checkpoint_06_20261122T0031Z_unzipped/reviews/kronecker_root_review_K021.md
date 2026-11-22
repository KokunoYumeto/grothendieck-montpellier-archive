# Whole-proof review: K-021

- Date: 2026-11-21, 22:23 UTC.
- Reviewer: `/root`, GPT-6 Astra Pro; effort not exposed; GCT_POS.
- Type: targeted proof check (entire proof), complete verifier reading and exact replay.
- Outcome: **PASS**.

I read all of `AMPLIFIED_LOWER_FIXED_LOCI.tex` and `verify_lower_fixed_loci.py`. The nested block collapse uses the proven K-020 complete spectral support and simple spectra at the old stage; the selected output is always new at that stage. Its incidence degrees (3,2,3) therefore count exactly five other old edges meeting the selected coordinates. Freeness excludes a second shared coordinate. The exhaustive tensor and Lie dimensions are consequently r^3+5r+3m−8 and3r^2+3m−6, with r=1+7l, giving343l^3+14l+1. The condition k−l≥1 correctly avoids using these output degrees at the parity seed.

The generator of the requested order is g_k^(2^k). For k=8l+s its fixed tangent contains that of g_k^(256^l); equality holds at s=0. Smoothness follows from K-020 and finite-order fixed-point smoothness over C. The replay independently rebuilds the n=58 spectrum from the incidence matrix and checks all tensor weights, obtaining697−339=358. Six smaller complete collapse counts also passed.

The conclusion is a local fixed-scheme dimension theorem. It does not assert that these components are globally maximal, that their leading terms do not cancel, or that the actual Hilbert series has a pole there.

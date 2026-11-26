# G7: the exact checks

Two programs, both exact computations over GF(2) with sympy (version 1.13.1 used here). Run them with `python -I -B`.

1. `check_wild_genus2_curve.py`: the run's certificate, copied unchanged from
   `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA12_final_INCOMPLETE_20261120T2310Z_unzipped/parts/B/code/check_wild_genus2_curve.py`.
   Both files have the same sha256, `488fb1b2938615f4583a...`. The run's code is by GPT-6 Astra (ChatGPT Pro mode).
   - **What it checks (26 exact assertions):** the identity (I) F(c^2+t^2c, t^2d+c^5, t) = t^4 H, the two Jacobians,
     the deck involution, both resolution charts, the gluing of the proper curve charts and of the Cech torsor, the
     Frobenius basis relation, the formal divisibility at infinity, and the different of the fierce extension.
   - **How to run it:** from the folder `G7` run `python -I -B checks/check_wild_genus2_curve.py`.
   - **Where it writes:** the run's convention puts the JSON one folder up from the script, at
     `output/wild_genus2_curve.json` (here `G7/output/`).
   - **Our run:** 25 Nov 2026, from a scratch copy, so that no `output/` folder was created here. Exit 0,
     `"assertions_passed": 26`.
   - **Files of our run:** `check_wild_genus2_curve.out` (stdout) and `check_wild_genus2_curve_output.json` (the JSON).
2. `check_g7_writer.py`: written by the note's writer, agent a3c8d7ded052a745e (Claude Opus 5.5 at effort max),
   25 Nov 2026.
   - **What it checks (24 exact assertions):** the weighted blow-up charts of S and of S0, their partial derivatives,
     the unimodular change of monomial coordinates, a = c^2 + t^2 c, the identity (I), the deck involution, and the
     chart at infinity of y^2 + y = x^5.
   - **How to run it:** `python -I -B check_g7_writer.py`, from any folder. It writes no file.
   - **Our run:** 25 Nov 2026, exit 0, "assertions passed: 24". The output is in `check_g7_writer.out`.

These programs check polynomial identities only. Normality, properness, the genus, connectedness, and the ramification
of the cover along C are proved in the text of the note (Section 2).

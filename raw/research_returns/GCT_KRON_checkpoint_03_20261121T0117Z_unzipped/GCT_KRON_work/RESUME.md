# Resume this research run

Read PROMPT.md, RUN_METADATA.json, LEDGER.md, APPROACHES.md, QUESTIONS.tsv, and CHECK_EVENTS.tsv. The run began2026-11-20T23:00:17Z. Checkpoints are due every45minutes from that time; first timed review02:00:17Z onNov21UTC, then hourly. Never invent elapsed reviews. The next checkpoint after02 is01:15:17Z.

## Current mathematical state

The entire supplied archive is inventoried and audited (A001–A019). Positive family formulas F001–F008 and saturation results O001–O010 are written. All proof-reading and source-use events are consolidated from agent ledgers and ROOT_CHECK_EVENTS.tsv.

The main actual multiplicity gate has moved repeatedly. Latest degree criterion A023 uses P_d, not older N_d or B_d; n>=P_d(dm) excludes every degree-d candidate. M013 unit-Jacobian jet dominance gives lambda2>=c+2 at n>=m^c,c>=6. M014 gives complete staircase lambda_(2j)>=c+3−j. M015 cyclic-star jets give lambda2>=6 already at n>=m4. F018's finite support-cover κ criterion is the strongest exact graph condition. Its explicit A025 corollary is lambda3>=557 OR lambda52>=3 in BIP range.

At n>=m25, remaining candidates require m>=190, rows>=52, lambda_(2j)>=28−j for1<=j<=26, lambda3>=557 OR lambda52>=3, q>=2, n<P_d(dm), n<P_d(lambda2), padding constraints, and failure of the full support/jet criteria. q>K remains unresolved outside proved ranges. Do not transfer the stronger-test d>n/m restriction to actual q>K.

A024 realizes the complete height-two rectangle square by a positive polynomial HW algebra with a nonprimitive index4 weight lattice. A026 gives equal height-three rectangles by count2a+3b+4c=h, a known invariant-ring extraction with a primitive scalar support lattice but a hole at1. A027 growing-height castling family is being developed by archive worker. F020 completes two-hook/two-row formulas including source-overlap endpoints. F021 gives full q=K=a by permanent jets and a strict example beyond every F018 cover. O020 full K=a at lambda3<=2 now only needs n>=r−1; original tree proof retained separately. All new included proofs have independent complete-read events, with later addenda logged separately.

## Build and render

Run python3 build_package.py. It expands every input into self-contained GCT_KRON.tex, normalizes A IDs, appends inventory, and merges ledgers. The local TeX installation lacks its normal format/filename DB; the repaired format is render/xelatex.fmt. Compile twice with:
env TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}' xetex -fmt=/workspace/scratch/e3994f8d0062/GCT_KRON_work/render/xelatex.fmt -progname=xelatex -interaction=nonstopmode -halt-on-error -output-directory=render GCT_KRON.tex
If format was not preserved, rebuild using xetex -ini -etex -jobname=xelatex and tex/latex/tex-ini-files/xelatex.ini under TEXMF=/usr/share/texlive/texmf-dist. All82pages of the earlier working PDF were visually reviewed in contact sheets; latest additions require final rerender.

## Sources and future work

Internal X11 padding matches attached IP/BIP sources. External full books, source texts and page reproductions are not redistributed; exact primary URLs, locators, hashes and proof-read records allow reconstruction. User-provided source corpus is included. The 2026 Foulkes source hash is6b4eb1977533b9b1503927a55687c72afd9dc68b05b27b94cf404413195dd2c2. No Lean check is claimed.

O016 proves the exact universal-determinant limitation via CKV ITCS2024 homogeneous ABP width; it must not be promoted to a border impossibility. O017 and O019 separately give border-valid dimension boundaries for full cut families and jet targets. Continue main remaining rank comparison; record every unsuccessful approach honestly.

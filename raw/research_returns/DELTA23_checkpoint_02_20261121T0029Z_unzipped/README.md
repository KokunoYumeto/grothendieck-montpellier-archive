# DELTA23 research package

This is work on the five questions in the attached DELTA23 prompt. The main
question is whether the character Δ vanishes on the full profinite
Grothendieck–Teichmüller group. An open gate is not reported as a proof.

`DELTA23.tex` is the paper. `QUESTIONS.tsv` records the current questions and
gates. `LEDGER.md` distinguishes actual mathematical progress from attempted
approaches. `CHECK_EVENTS.tsv` records the kind and scope of each check.
`IMPLICATIONS.md` explains the consequences for the proposed reciprocity,
Grothendieck's manuscripts, and the requested complexity-theory connection.

The proof fragments and exact Python certificates are included. A finite
matrix computation is a computation certificate, not a Lean verification and
not evidence that a finite candidate lifts to an actual GT element.

## Recovery

The attached source archive was extracted once into `sources/` in the working
session. Its complete SHA-256 manifest is retained in `records/`. The supplied
source claims are identified by run and statement. In particular, the E.58
lifting input is used as supplied; the earlier D.50 proof is not present in
the attachment and has not been independently reconstructed here.

Downloaded literature is identified by URL and precise locator. Downloaded
full books and journal PDFs are not redistributed in this package. Their
reproducible lookup information and reading records are retained instead.
The attached Alpöge note is available in the original archive. No Lean files
named by the prompt were present in that archive, and none is claimed to have
been inspected or used. No new proof here requires RH or GRH.

All workers used GPT-6 Astra Pro with the inherited effort setting, which was
not exposed by the runtime. The run began on 20 November 2026 at 22:59 UTC
(23:59 CET). Checkpoints are due at 45-minute intervals; the first elapsed
progress review is due about three hours after that start.

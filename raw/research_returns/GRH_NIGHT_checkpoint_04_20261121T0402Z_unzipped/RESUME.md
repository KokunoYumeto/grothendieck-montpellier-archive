# Resume this research

Snapshot: 2026-11-21T04:02:01.091427+00:00.
Read the attached original prompt, README.md, LEDGER.md, and CONSEQUENCES.tsv first.
Use the original user-supplied source archive, checking INPUTS.tsv hashes. In a fresh environment,
unpack that archive once into `sources/`; do not repeatedly unpack it over edited material.
The domain drafts in `work/` are the source for the paper and registers.
Run `python work/scripts/assemble.py` from the extracted package to rebuild the root deliverables.
The script writes `deliverable/`; compile its GRH_NIGHT.tex with XeLaTeX twice.

Preserve all earlier checkpoint ZIPs. Continue its numbering from the saved checkpoint register.
Do not create extra checkpoint ZIPs between the specified 45-minute intervals.
At the three-hour and subsequent hourly reviews count only a status change or a strictly smaller main gate as movement.
Every next research step must retain exact hypotheses, primary theorem/page locators, and truthful check events.

The main unresolved gates are individually listed in QUESTIONS.tsv. In particular, do not present full GUE,
general Artin holomorphy, non-CM GL2 GRH, integral K-theory vanishing, or general derandomization
as consequences already proved in this package.

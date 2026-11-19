# Final reference integration

The bibliography is `outputs/SA08_references.bib`. Exact current counts and input hashes are in `reference_audit.json`, which is regenerated on every integration pass. All citation keys appearing in the current agent claims/problems, the already-generated aggregate files, or `outputs/SA08_directions.md` resolve. Additional records preserve checked background or search leads. If a dossier exists when the program is rerun, its Markdown citations are audited as well.

`reference_aliases.json` is a plain old-key-to-canonical-key object, with identity entries for canonical keys. Apply it to every `refs` array. Important aliases include `BreenMikhailovTouze2016` and `late_BMT2016` → `BMT2016`, `PursuingStacks2021` → `GrothendieckPS1983`, `SGA4III` → `SGA4XVII`, `StacksDoldKan` → `Stacks019G`, `StacksPD` → `Stacks07GK`, and the late-package prefix aliases. Distinct Mandell papers, Cartan seminar papers, and differently scoped modern theories remain distinct.

The explicitly unverified original-access leads are Coleman2000, Dwyer1979, GressmanSeries, Miller1978, Stoia1975, and Swan1975. Each annotation explains the exact access/reading scope. In particular, Atiyah1957, Cartier1957, EGAIII, and Tate1967 have verified metadata, not a fresh reading of their historical theorem proofs. The Miller and Swan identities are supported by opened primary bibliographies, but their original articles were not obtained.

`REFERENCE_CHECK_EVENTS.tsv` has one bibliography integration event per canonical work. These are explicitly metadata/key/source-scope audits, never independent mathematical proof checks. The agents' substantive theorem-use and proof events remain in their own event ledgers for root to integrate.

`reference_audit.json` retains all original bibliography records, hashes, input-field differences, exact used-by claim/problem IDs, Markdown citation line locators, verification counts, missing-key checks, and additional access-log paths. DoldSteenrod1961 is bounded to printed pages 258–263, and Touze2026 is bounded to introduction/theorem statements over a field with exact strong symmetric tensor functors; neither is presented as a full-proof check.

The saved program is `programs/early_integrate_bibliography.py`; its first two versions and every result summary are retained. Running it regenerates the final bibliography, aliases, audit, and reference-event ledger without changing any claims or problems.

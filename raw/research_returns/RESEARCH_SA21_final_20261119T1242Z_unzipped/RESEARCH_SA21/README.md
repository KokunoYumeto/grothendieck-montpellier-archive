# RESEARCH_SA21

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026.
No human authorship or priority is claimed. The exposed runtime did not
identify a reasoning-effort setting.

## Reading order

1. `RESEARCH_SA21_report.md`: outcome table, subsidiary tasks, source-access
   record, exact program scopes and runtimes, full correction register, and QA.
2. `RESEARCH_SA21_paper.pdf`: complete checked mathematics in the order of
   Parts A, B and C, with source locators and bibliography access notes.
3. `RESEARCH_SA21_results.csv`: one row per numbered statement, including
   the printed statement number and PDF page.
4. `CHECK_EVENTS.tsv`: actual proof, computation and source-check events,
   including retained earlier study IDs and explicit superseding corrections.
5. `RESEARCH_SA21_corrections.tsv`: machine-readable source correction table.

`PROGRESS_LEDGER.md` and the part-specific notes preserve the development
history. Earlier provisional wording in historical notes is superseded by
the current paper, corrected registers and final report. Sources and input
archives supplied by the user are not recopied into the package.

## Build the paper

Use a normal current TeX Live or MiKTeX installation with LuaLaTeX,
BibTeX, Latin Modern, AMS fonts, TikZ, natbib, xurl and the packages listed
in the preamble. From this package's root:

```sh
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA21_paper.tex
bibtex RESEARCH_SA21_paper
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA21_paper.tex
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA21_paper.tex
```

The delivered PDF was built with LuaHBTeX 1.18.0. This session's minimal
installation needed a locally generated LuaLaTeX format and official
luaotfload/lualibs dependencies; the environment setup and failed attempts
are retained as logs. Those private runtime binaries are not required by
the document and are not packaged. Explicit standard font-map declarations
in the preamble made the mathematical fonts embed correctly in that
minimal environment.

## Reproduce the finite certificates

The mathematical scripts require Python 3.10 or later and only its standard
library. Exact outputs from the executed runs are retained. Durations are
observations from this session and will vary on another machine.

```sh
python3 code/check_supports.py
python3 code/explore_supports.py orders --maxn 7
python3 code/explore_supports.py magasins --maxn 6
python3 parts/maquettes/code/check_conditional_lattices.py
python3 parts/maquettes/code/audit_supports.py
python3 parts/maquettes/code/check_interval_axioms.py
python3 parts/axioms/finite_axioms.py
python3 parts/axioms/core_models.py
python3 parts/axioms/literal_systems.py
python3 parts/axioms/legacy_subdivision.py
python3 parts/axioms/connectedness.py
python3 parts/bmodels/code/bmodels_checks.py
python3 parts/maquettes/code/check_maquettes.py
```

`code/supports_core.py` is an imported library, not a separate census.
The report distinguishes exhaustive labelled graphs, naturally labelled
orders, all labelled partial orders and individual finite models. Counts
from repeated runs are not added as if they were disjoint populations.
Infinite-object claims have mathematical proofs, not extrapolated tests.

## Operational validation

`code/merge_metadata.py` merges the part registers. After a LuaLaTeX build
whose auxiliaries are in `logs/`, `code/audit_metadata.py` verifies all
numbered labels, result rows, check coverage, source-access markers and
the final build log, then writes `code/outputs/final_metadata_audit.json`.
`code/build_final_report.py --final` incorporates the completed source,
computation, correction and PDF audit records. `code/build_final_package.py`
checks the final prerequisites and creates an immutable ZIP plus its
per-file SHA256 manifest. These scripts check operational consistency;
they are not machine verification of the mathematical proofs.

`qa/` contains rendered page images and contact sheets used for visual
inspection. Exactly one PDF is delivered. The report records the overflow
counts before and after correction and the inspected page numbers.

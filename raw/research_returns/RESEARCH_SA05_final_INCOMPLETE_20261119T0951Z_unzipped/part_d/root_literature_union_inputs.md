# Exact inputs for the root-level literature union

Normalize the following into a single work-level table. Use a
canonical citation key after applying the separately suggested
alias map, and union the distinct locators/evidence rather than
discarding repeated checks.

1. `part_b/part_b_LITERATURE_CHECK.tsv`: Part B's explicit table,
   including the attached Scholbach and Adrien Morin sources and
   explicit not-obtained Fontaine--Perrin-Riou/Schneider rows.
2. `part_d/LITERATURE_CHECK.tsv`: Part D's complete table. It
   already incorporates `auxiliary_LITERATURE_CHECK.tsv`, so do
   not import the auxiliary table a second time as new evidence.
3. The freshly consolidated `RESEARCH_SA05_references.bib`:
   import the annotated `note` fields for records not present in
   the explicit tables, especially Parts A and C. This is preferable
   to reading a stale consolidated snapshot. Its owner inputs are
   `part_a/references.bib`, `part_b/part_b_sources.bib`,
   `part_b/b4_algorithm.bib`, `part_b/b3_singular.bib`,
   `part_c/references.bib`, and `part_d/part_d.bib`.
4. `part_d/contextual_LITERATURE_CHECK.tsv`: three new rows for
   the prompt-named Lipman, Mumford GIT and Larsen--Lunts works,
   based on bounded actual searches and openings in this run.
   These rows are also appended to Part D's complete table by
   its builder, so importing item2 after its latest run suffices.
5. `part_d/c1_audit_sources.bib`: newly opened Milne Algebraic
   Groups and Meir. The C agent is importing `c_milneag2022`
   for its finite-even proof. The corresponding exact rows are
   already in Part D's table, including Procesi's theorem locators.

The remaining auxiliary C6 bib fragment contains useful formatted
entries but does not replace Part D's fuller literature rows.
The root table should retain its inspected-but-inapplicable sources:
Fontaine C_WD, Serre local C1--C8, Ochiai, Saito, Lu--Zheng,
Ayoub, Cadoret--Tamagawa, and the current source correction notice.

Suggested common columns are `source`, `status`, `exact_results`,
`url_or_supplied_path`, `retrieval_evidence`, and
`use_or_limitation`. An `opened` status derived from another agent's
row should retain that attribution; it is not a new independent
opening by the union script. A historical attached ledger is
background evidence and must not be relabelled as this run's event.

No root-level file is written by this note. The parent owns
canonicalization and the final union.

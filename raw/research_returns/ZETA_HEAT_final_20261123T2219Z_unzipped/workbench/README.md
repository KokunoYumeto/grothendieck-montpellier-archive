# The Riemann zeros: simplicity, heat flow, and finite multiplicity tests

This workbench contains one independently editable research paper and the mathematical checks supporting it. It begins with Alpöge's theorem on the location of the nontrivial zeros. The remaining main target is the simplicity of every Riemann zero.

The source paper is `paper/main.tex`; the complete local inputs and build instructions are beside it. The numerical work distinguishes exact rational computations, rigorous ball enclosures, and numerical experiments. Statement and check records are kept separately from the prose of the paper.

Research ended after two consecutive scheduled reviews without qualifying movement. The overall all-zero simplicity task is INCOMPLETE; nine question rows are proved, two refuted, and nine retain their exact unresolved gates in QUESTIONS.tsv and FINAL_STATUS.md. A local multiplicity certificate applies exactly to the zeros enclosed by its contour. The records list every unresolved quantifier and estimate; no claim of a proof of global simplicity is made without that proof.

The intended public home is https://github.com/KokunoYumeto/zeta-and-l-functions-workbench. The format is version 1 of https://github.com/KokunoYumeto/mathematics-workbenches. A work number and permanent page are assigned only when the work is filed; the staging statement tags are preserved through that assignment by an explicit crosswalk.

Only text and programs authored for this work are included. External sources are cited by address, hash, and exact locator; their files and text extractions are excluded from every returned archive.

Our text and programs are dedicated to the public domain under CC0 1.0.

## Reading the check records

`STATEMENTS.tsv` assigns a stable staging tag to each listed statement and links it to exact event identifiers in `CHECK_EVENTS.tsv`. `STATEMENT_EVENT_MAP.tsv` expands those references with the original event type, reader, exposure scope and outcome. A shared event remains limited to its recorded scope; the expanded table does not turn a partial independent derivation into a full independent proof. The later proof-exposed audits and numerical certificates are separately labeled. Permanent tags are left for registry assignment.

## Final verified paper

The final paper has 169 pages and 48 editable TeX inputs. Its fresh-build, complete source-reading and every-page image records are in versions/ and the scoped check reports. Use paper/ for the current text; drafts/ preserves historical attempts and immutable independent-check records, including explicitly superseded wording. The final source and archive manifests identify the deliverable bytes. No whole-manuscript formal-verification claim is made.

The stable entry ZH.STMT.031 is a historical alias for the trace-to-detection statement now carried by ZH.STMT.051, at `cor:trace-global-threshold`. Its original check events retain their recorded scopes.

## Reproducing the results

[REPRODUCE.md](REPRODUCE.md) indexes all 27 returned check and certificate programs, with exact commands from the workbench root, dependencies, expected outputs, input chains and replay precautions. It also links the standalone paper build.

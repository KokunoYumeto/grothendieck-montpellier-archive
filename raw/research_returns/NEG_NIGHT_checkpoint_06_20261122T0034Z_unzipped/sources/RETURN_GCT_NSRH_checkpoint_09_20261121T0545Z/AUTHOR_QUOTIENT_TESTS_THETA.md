# F59 quotient-route tests: author verification record

Author: `/root/rectangular_and_theta`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Inherited reasoning effort is not exposed.

Final report: `agent_soergel_quotient_route_tests.md`, SHA `d50900b1353ce0c01b43832283e7ea9464d976dac2e7853f7053004ee9014e9e`. Its sole change from root's and gct's first whole-proof review target `77ca49fb...` is replacement of a literal carriage return in the displayed cohomological degree notation by the intended TeX `\rm`.

Final fragment: `finding_F59_quotient_tests.tex`, SHA `a6a354fc2ae0cb7f198709a746dd6ab648bb8ce7463c13f2b78d3cb4e3948265`. I read all 377 lines against the full report after writing them. It retains the exact normalized chain quadratic, all dual and extreme cohomology formulas, the split-class Hom invariant, the complete periodic free resolution and all positive Tor shifts. The two theorem environments use the master's existing `finding` environment with explicit F59 titles. The separate dictionary is marked for Part III. No new theorem beyond the report is introduced.

The source shift convention is the original Elias--Williamson Sections3.3--3.4, pp1105--1106, as read before writing the report. The Tor calculation is proved directly and does not invoke an unstated matrix-factorization theorem. No arithmetic purity is inferred from its internal shifts. The report's remaining target scope is retained.

The isolated wrapper `tex_check/theta_F59_quotient.tex` uses the actual current main preamble and inputs the fragment only. Two `pdflatex` passes with the working TEXMF and saved format succeeded. The resulting PDF has four pages and 184390 bytes. The final log has no LaTeX errors and no overfull or underfull boxes. Expected undefined bibliography citations remain because this isolated wrapper does not include the master's bibliography; internal cross-references resolve on the second pass. This is a syntax/layout-warning check, not a claim of visual PDF inspection or formal proof verification.

Root separately reported complete report and full-fragment mathematical PASS. Gct's complete independent proof/source check and final-fragment match were requested; their separate review supplies the independent record. No root master file or shared log was edited.

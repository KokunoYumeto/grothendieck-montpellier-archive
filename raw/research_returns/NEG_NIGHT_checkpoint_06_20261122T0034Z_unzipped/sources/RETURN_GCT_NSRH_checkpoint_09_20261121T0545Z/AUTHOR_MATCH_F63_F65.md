# Author full-fragment match and syntax record: F63 and F65 joint supplement

Author/checker: /root/gct_statements, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

## Exact frozen targets

- F63 report: agent_iterated_chebyshev_gate.md, SHA256 8ee2ba3448005df2ed9a4e39df8103e4d86d80ddad852227b30766cb7edbb224.
- F63 final fragment: finding_F63.tex, SHA256 af4fffb91778b1765a3262a90cc18c3517f34aea9e6ee4225bc824924ab8e259.
- F65 joint report: agent_joint_normalization_gate.md, SHA256 7a97eee4d519d31ae3759dd28f2e679e5377b715df221af239bd1edb4fa1b006.
- F65 joint final fragment: finding_F65_joint_normalization.tex, SHA256 3c6049c38bb1ad080e9c7448b0fcde131635e82fbf77a37c7c6aa8810fc56b41.

Both complete generated fragments were read directly after generation. Author match PASS: every mathematical deduction from the corresponding reviewed report is retained, with the separate dictionary paragraphs and comparison hypotheses.

F63 retains the actual source iteration, negative two-word trace, all-k positive-zero argument, limited k<=3 minimality, complete regular four-column comparison, determinant, projector, actual tensor occurrence, all-word positivity and pure-point/source-cellularity scope.

F65 retains the explicit source convention, both coefficient types and column-label inconsistency, exact presentation identities, both complete JN-A/JN-B proofs, proper structure-morphism qualification, isolated half-step pure complex and separate dictionary. No arbitrary-beta strengthening was added to the frozen fragment.

## Independent checks

F63 complete source/proof/script review and final whole-fragment match:
REVIEW_ITERATED_CHEBYSHEV_THETA.md, final SHA256
2b8b877c8cc32360a7cbcff79982ec86b9e9dbf9c7e9bfe1f79ae766f9d867ac.

F65 complete source/proof/script review and final whole-fragment match:
agent_F65_joint_normalization_review.md, final SHA256
6fd138b3fbae1a2b4e89a2c2f823a8a4fe75d7c1f0bb61bab309cb88993f0ace.

Both verdicts are PASS. F65 review correctly narrowed the proper-pushforward consequence to proper structure morphisms to the finite-field point, or a separately supplied pure point extraction. Pure complexes on higher-dimensional bases do not have arbitrary pure stalks. That substantive scope correction is included in the frozen report and fragment.

## Compile record

The isolated wrappers use the existing project preamble and known local format:
- tex_check/gct_F63.tex
- tex_check/gct_F65_joint_normalization.tex

The first invocation without the project's TEXMF setting failed to find article.cls. The next invocation reached the end of both fragments but failed to embed the missing tcrm1095 font caused by raw Unicode section signs. Those signs were replaced by the project's existing \S macro; this final typography-only change is anchored in both independent reviews.

Final invocation for each:
env TEXMF=/usr/share/texlive/texmf-dist pdflatex
-fmt=/workspace/scratch/b5024d19aacd/GCT_NSRH_work/tex_check/pdflatex.fmt
-interaction=nonstopmode -halt-on-error
-output-directory=GCT_NSRH_work/tex_check <wrapper>.

Both final invocations exited zero. F63 produced five pages and F65 joint produced three pages. Neither final log contains an overfull or underfull box or TeX error. Undefined bibliography citations are expected in these isolated wrappers and are left to the master document's bibliography; F63 uses the new key BlasiakChebyshev for arXiv:1010.0421v2.

This is an isolated syntax/layout-log check, not a claim of visual inspection of the final master PDF. Root owns master integration, cross-reference resolution and visual review.

The exact symbolic certificates and their mathematical scopes are recorded in the source reports. No formal proof assistant was used, and no shared master check file was rewritten.


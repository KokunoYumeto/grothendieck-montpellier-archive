# Input-classification audit notes

Date: 21 November 2026. Agent: GPT-6 Astra Pro, MAS_ARTIN/input_audit; inherited effort setting. This module is a documentary dependency audit. It does not report a new full proof check of every inherited theorem.

## Deliverables and exact scope

`INPUT_CLASSIFICATION.tsv` contains 563 distinct run/ID pairs: all 362 GRH_NIGHT CONSEQUENCES rows, 162 ALPOGE_BRIDGES findings, and all 39 CX_GRH findings described by the supplied intake. The ALPOGE set includes explicit numeric ranges and contextual shorthand, and conservatively includes the unchanged root_core/consequences_criteria block, the F-SM-13–44 block, the full CC-AG/CC-XC groups, and directly supporting CC-TATE/effectivity rows. Such additional supporting scope is identified in each row rather than represented as a literal standalone intake citation.

`INPUT_CITED_SCOPE.tsv` records the literal intake token, file/line, surrounding text, resolution and explicit group expansions. The independent audit also checks 126 numeric or range-expanded finding IDs and 22 nonnumeric contextual IDs. It was necessary to read the prose: a string search alone misses `CONNECTED-SOURCES`, `SEMILOCAL-SOURCES`, `ORBIT-RETRACT`, and similar suffixes whose prefixes occur only once.

`INPUT_UNCLASSIFIED_GATES.tsv` separately records nine cited ALPOGE question/current-gate rows and CX-U01–U06. A question is not assigned `none` as though it were an available proved statement. The original CX_GRH return was not attached or resolved in this audit. The 39 finding rows are consequently marked `intake-only`; a predecessor's reported full reading is not a new proof check by this agent. The precise text of CX-U01/U04/U06 is not supplied, and U03/U05 are only partially contextualized by later GRH intakes. The needed missing information is stated in the gate register.

The requested machine-readable artifact is TSV. No alternative spreadsheet workbook or formatted spreadsheet was substituted for it. Each GRH row preserves the original statement, input, status, proof locator and Grothendieck locator verbatim. The model decisions are explicit ID assignments in `checks/build_input_classification.py`; there is no keyword classifier deciding mathematical inputs. `checks/audit_input_classification.py` independently reads the emitted table and source catalogue without importing those assignments.

## The four-way convention

The primary class is the administrative maximum under `M > outside preprint > A > none`. This order does not claim a logical implication between M and an outside paper. Required outside theorems and residual premises remain explicit. In particular PF26+M is never abbreviated to an assertion that M alone proves the algebraic factoring theorem.

A is Alpöge's Dirichlet-GRH theorem and is cited as a theorem. M is the unrefereed claim for all unitary Hecke characters of all number fields in Masullo §§1.2–1.2.3, pp. 12–16. The finite-order portion covers Dedekind, Kummer and Brauer/Artin applications. Potentially CM positive-weight motives generally need infinite-order unitary characters after the weight twist. The blank Theorem 13.3.1.2, p. 522, supplies no statement.

`none` excludes A/M and an identified substantive outside-preprint theorem in the classified assertion. It does not exclude standard literature, strong extra hypotheses, or a remaining open problem. NT-L15 and NT-Z19 retain a weak mean-square condition stronger than the GRH/simplicity conclusions obtained from it. NT-Z07 retains independent non-CM GL2 GRH. A row's original status is never replaced by the four-way label.

Formal equivalences such as MT-M19/M20/M27 receive `none`; their A/M applications remain notes. Actual arithmetic positive-determinant applications AG-DET/MOMENT/HANKEL/SIGNED retain M at full Hecke/CM scope and A in the Dirichlet specialization. The abstract analytic or moment cores can be used without A/M if their positive real support is supplied independently. MT-M26 retains M for the asserted narrow-strip application, even though its containing-strip theorem is unconditional. The distinction is based on the actual asserted arithmetic use, not on turning every analytic assumption into a formally conditional implication.

## Located input corrections

### MA-IN-001: NT-Z13, NT-Z15 and NT-Z16

All three begin the original input field with A but include a general finite-order Hecke branch. The full-scope primary class is M, with A recorded for the Dirichlet case. The complete fields already mention M later; the flag is therefore `leading_A_weaker_than_full_scope`, not an accusation that the original author entirely omitted the conditional hypothesis. NT-Z14 inherits the Hecke scope and is also M, without that leading-label flag. NT-Z16 counts the first nonnegative ordinate, not the first strictly positive ordinate.

### MA-IN-002: AG-CYCLIC-DIV

Its original `neither` means neither A nor M. The full original input already names PF26 as a recent manuscript. The proof imports PF26 §4, Lemmas 4.1–4.4, Corollary 4.5 and Proposition 4.6, pp. 15–19, so the four-way class is `outside preprint: PF26`. This corrects the leading shorthand, not an undisclosed source. The PF26 agent independently confirmed the exact locators and complete source-proof reading in MA-PF-001; this audit itself is a dependency reading.

CX-ALG-027/028 have M as primary label but explicitly retain PF26. For CX-ALG-028 the exact smaller analytic requirement is A plus RH for the finite bad-prime pure fields, equivalently the associated Kummer Hecke factors. Empty bad set gives PF26+A. A stronger supplied-field/table promise removes the analytic input. See MA-PF-002 for the independent reconstruction rather than treating this table as a proof of the reduction.

### MA-IN-003: abelian motive provenance

The cp03 ALPOGE intake calls CC-AG01–03 and CC-XC01–04 `none` and describes the geometric block as unconditional, while expressly saying the new 2026 Tate source was not identified/opened. The supplied final proof uses van Hoften–Sempliner, *The Hodge Conjecture for CM abelian varieties*, Hexagon 2610.00259v2, Theorem I p. 1, combined with Milne (1999), Theorem 7.1 p. 72 and Propositions 7.3–7.4 pp. 73–75, and Milne (2002), Theorem 3.3/Corollary 3.4, final author-manuscript pp. 8–9. The later part-4 intake correctly retains the outside-preprint qualification. The earlier `none/unconditional` wording is flagged for the full arithmetic cycle scope.

CC-TATE03 additionally uses *Milne's rationality conjecture*, Hexagon 2610.00226v1: the contributor is Madapusi, the PDF byline is “ChatGPT and Claude.” Theorem 1.1 p. 1 supplies rationality; Corollary 6.2 p. 13 plus the CM Hodge theorem supplies the common cycle on the special fibre. Proposition A.1 pp. 13–14 is a separate lifting input. No algebraicity theorem for every non-CM characteristic-zero abelian variety is inferred.

Milne's *On the Hodge, Tate, and standard conjectures for abelian varieties*, Hexagon 2611.00244v1, Theorems 2.1 p. 4, 3.1 p. 6 and 3.5 p. 8, is recorded by name as the 2026 corroborating note. The required implication is separately cited to his published 1999/2002 papers. It would be misleading to make the corroborating note an indispensable third premise where the proof does not use a new result from it.

CC-XC20–22 explicitly avoid the all-abelian Tate preprint. The full proofs use actual Tate or supersingular abelian Chow decompositions, finite-field restriction/corestriction and published Fu–Li results. CC-XC22's final paragraph confines its fixed-target algorithm to supersingular Honda roots, where the required comparison has already been proved in that module. BR-15-CLASSBOUND and BR-15-SLOPEBOUND need classical Honda–Tate and ideal theory, even though CC-AG14's full abelian-category statement uses the broader input. These distinctions would be lost by propagating a preprint label along every textual cross-reference.

## Additional outside inputs and source-status checks

The explicit outside class includes substantive imported manuscripts beyond the four task-designated names. `task_designated_outside` distinguishes them. Current status was checked on primary publisher, author/institutional, official repository or arXiv records; an arXiv URL by itself was never taken as proof of unpublished status. Exact URLs, versions and locators are in `inputs_source_status.tsv`.

- EGS arXiv:2507.15704v3 is a substantive premise of AG-DP-EGS and the very-general even-degree specialization in AG-FOURIER-ISOGENY. The university repository identifies a preprint. The main isogeny push-pull argument itself is classical.
- Fu–Huang–Li arXiv:2609.38801v2 supplies CC-XC23's known-type irreducible-symplectic Chow input. Excellent liftings, `p > dim X` and the stated Artin-invariant exclusions remain hypotheses.
- Ito–Zou arXiv:2610.07890v1 and Wear arXiv:2303.05610v1 supply two CC-WM01 branches. Wear's author research page still lists the work as submitted; its relationship to a 2020 thesis is retained. Scholze and Binda–Kato–Vezzani supply published toric branches.
- Petrov–Zavyalov arXiv:2607.14517v2 supplies CC-WM02/03. The actual substantive generalization concerns rigid analytic spaces; the source itself distinguishes the already known algebraic formality case.
- Ramzi–Sosnilo–Winges arXiv:2503.11338v1 supplies coproduct preservation through Dwyer–Kan localization for F-SM-32/33. The author lists acceptance in JEMS. An issued publication was not established; it is conservatively recorded as an accepted preprint. F-SM-44 does not import this input merely by referring to the same programme: its complete scalar-extension/Yoneda proof uses different ingredients.
- Broe arXiv:2608.28651v1 is the separately marked narrower fourfold comparison in the supporting CC-TATE05 row.
- CX-E01–05 actually invoke E, OpenAI's *The Exponential Time Hypothesis is False*, 25 October 2026. They are `outside preprint`, even though the intake's later scope summary groups the E findings under `none` meaning no A/M. E06 and the geometric dictionary rows do not assert a new E-dependent algorithm and remain `none`.

Published-status checks prevented false outside labels:

- Deninger, arXiv:2504.15767v3, is published in *Journal of Number Theory*, 286 (2026), 47–66, DOI 10.1016/j.jnt.2026.02.004.
- Haine–Porta–Teyssier, *Exodromy beyond conicality*, is published in *Journal of Topology*, 19(3) (2026), DOI 10.1112/topo.70091.
- Chen, Lau, Lee, Ono and Zhang, *Almost all primes are partially regular*, is published in *Archiv der Mathematik*, 127 (2026), 165–178, DOI 10.1007/s00013-026-02261-y, version of record 2 July 2026. F-SM-15 therefore retains a substantive published input, not a preprint label. The earlier arXiv byline includes the project team; the published citation has five authors.
- Dutour Sikirić–Elbaz-Vincent–Kupers–Martinet's K8 theorem is published in *JIMJ*, 25(1), 565–590 (online 24 November 2025), DOI 10.1017/S1474748025101394.
- Zywina's *Bounds for the Lang–Trotter conjectures* is the published *Contemporary Mathematics* 655 (2015), 235–256, DOI 10.1090/conm/655/13206, notwithstanding the inherited author-preprint locator.

BKNO arXiv:2508.17776 in AG-LOCAL-EXCEPTION and Thakur arXiv:2001.00210 in BR-15-CLASSBOUND are refutation targets. Their false conclusions are not premises of the supplied counterexamples and do not cause an outside-preprint dependency.

## Exact Alpöge citation, MA-IN-007

Primary public locator: Alpöge, *Remark*, https://alpo.ge/remark.pdf, p. 4, step 20. The public page was directly inspected. The source chain also includes steps 1–5 p. 3 and steps 6–20 p. 4; step 17/footnote 6 is an unspecified K-group suggestion, not a degree-indexed theorem.

The predecessor's `research/source_and_masullo.md`, §§1.1–1.2, records complete reading of `ALPOGE_Main.lean` and definitions in `ALPOGE_Statements.lean`, with pin `0df444a360eaa60ab8c11dca51a86af692955474` and import `Supplements.Kernels.MainTheoremsAll`. Exact exports:

```lean
riemannHypothesis : RiemannHypothesis := rhOfAll
riemannZeta_eq_zero_re : RiemannZetaZerosOnLine := rhOfAll
LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf := allChi
LFunction_eq_zero_re : DirichletLZerosOnLine := claimAll.2.1
LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine := critAll
```

The current attachment contains that inspection record, not the Lean interface files or full import tree. The filenames and declarations are predecessor-inspected evidence; this audit did not freshly read or compile those Lean files. A is nonetheless used as the theorem designated by the prompt. No zero-location result for all number-field Hecke characters is attributed to those rational-Dirichlet exports.

## Reproduction and verification

Run `python checks/build_input_classification.py`, then `python checks/audit_input_classification.py`, from the work directory or by absolute path. No network is used by either script. The builder preserves input source files. The audit checks exact ID-set equality and source-field preservation, not just row count; a duplicated row cannot compensate for a missing row. It checks the one-class vocabulary, outside names, evidence files, mandatory NT-Z flags, the PF26 conjunctions, intake numeric ranges and contextual shorthand, the CX 39-finding set, and the separate six-gate register. `input_independent_audit.json` contains the final table hash and PASS.

`inputs_events.tsv` separates targeted dependency readings from background carry-forward and from the data computation. Every new documentary finding MA-IN-001–007 has a complete argument in `inputs.tex` and an explicit self-check event. The table is complete as a classification of the available assertions at the reported evidence level; unavailable original CX proofs have not been promoted into fully checked proofs.

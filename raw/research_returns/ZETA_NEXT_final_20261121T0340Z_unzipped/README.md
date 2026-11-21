# ZETA_NEXT

This is the final package for the attached prompt of 21 November 2026.

## Required deliverables

- **ZETA_NEXT.tex** — one standalone LaTeX paper, containing 22 numbered findings with proofs, exact source locators, a checked-findings part, and a separate part stating that no unchecked findings are included and identifying the boundaries of the conclusions.
- **QUESTIONS.tsv** — the questions treated, with the finding IDs resolving them. A separate possible amendment requiring separatedness but not properness is explicitly a scope note, not an asserted theorem.
- **LEDGER.md** — dated progress and the strongest gate for each main question, with actual checkpoint/review timing.
- **CHECK_EVENTS.tsv** — normalized records of author checks, independent-reader checks, source use, carried background, refutations and computations.
- **IMPLICATIONS.md** — the exact changes to the Grothendieck programme, predecessor rows, class-number and orbit statements, Λ-scheme conjecture, and non-CM analytic gate.

## Principal outcomes

The arithmetic bound is \(\kappa_K>1/(173\log D_K)\) for normal \(K\ne Q\), with an explicit n! loss in general degree n. The paper makes the CM class-number and all-CM-point orbit bounds explicit, including nonmaximal centres. The literal Λ bad-factor conjecture is refuted; the proper-flat cohomological splitting is proved. For curves and abelian-type motives the CM/non-CM projector is supplied, with exact residual lists and worked cases.

Alpöge's theorem is used with the status prescribed in the prompt. The previous IA01 and conditional audit stand. Masullo-dependent CM-factor RH statements remain expressly conditional. Non-CM RH is not claimed.

## Documentation and reproducibility

The normal/, cm/, lambda/, and noncm/ directories contain the branch proofs, source bibliographies, notes, and original branch check registers. Their wording is incorporated into the standalone paper. The root registers are the normalized version to use for the final result.

Independent detailed challenges are in cm/normal_review.md, cm/lambda_L2_review.md, and noncm/cm_orbit_review.md. The audit directory contains the assembly script, root records, input/source fingerprints, finding coverage, and structural package checks.

The exact rational numerical certificate is audit/check_stark_constant.py, with saved output audit/stark_constant_certificate.txt. It verifies the rounding of the Stark residue constant without floating-point acceptance comparisons. The CM numerical sample is auxiliary, not a proof of the general inequalities. Non-CM multiplicity and curve computations include their scripts and saved outputs.

Primary literature URLs and exact locators are in the paper bibliography and audit/SOURCES.tsv. Downloaded literature and the user's original attachments are not duplicated in this package. The primary-cache fingerprints identify the editions used; the supplied attachments remain the source for predecessor text and archival locators. No newly inspected archive facsimile is claimed.

## Building the paper

ZETA_NEXT.tex has no external TeX input dependency. Use a conventional LaTeX installation with the standard amsmath, amssymb, amsthm, mathtools, geometry, longtable, booktabs, array, xurl, hyperref and lmodern packages; run pdflatex twice for the contents and references.

The execution environment had TeX engine binaries but lacked the LaTeX format/package bundle. Its attempted Tectonic bundle download was denied with HTTP 403, so a compiled PDF is not included or claimed. The requested TeX source was checked structurally for balanced environments/braces, labels and citations, control characters, register shape, and proof-check coverage. The mathematical checks are recorded separately and do not depend on this compilation limitation.

No proof-assistant formalization of the new findings is claimed.

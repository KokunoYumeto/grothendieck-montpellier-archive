# GCT_GINEQ final package

Run GCT_GINEQ-2026-11-20-R1.

## Contents

- GCT_GINEQ.tex — complete paper, with F-01–F-23, full proofs, a separate Grothendieck-framework part, source corrections, exact literature and archival locators, and a separate scope/unverified-items part.
- GCT_GINEQ.pdf — compiled reading copy.
- QUESTIONS.tsv — every treated question and its proved, refuted, or explicitly limited state.
- LEDGER.md — dated movement, failed approaches, corrected gaps, and remaining gates.
- CHECK_EVENTS.tsv — actual proof, source, and computational check events with model/effort/run provenance.
- IMPLICATIONS.md — what follows for rank certificates, complexity, and Grothendieck's texts.
- ID_MAP.tsv — temporary agent IDs mapped to final findings.
- audit/ — original model audit notes and per-agent events, plus final production checks.
- checks/ — reproducible exact finite computations.
- SOURCES.sha256 — hashes of the supplied prompt and archive.
- MANIFEST.sha256 — integrity hashes of the package files.

## Reading order

Read the abstract and the image-method section of the paper first for the strongest positive results. F-01–F-12 establish which simpler norm and SDP routes work and which do not. F-13–F-14 give uniform image-norm bounds. F-23, placed immediately after them, is the later exact restriction refinement. Its ID is intentionally retained rather than renumbering already-audited findings.

The row tensors, symmetric polynomial tensors, and the padded-permanent orbit problem are three different objects. Likewise CP rank, CP border rank, and symmetric/Waring rank must not be interchanged. The paper states the field convention for every use.

The package does not claim historical priority, a new rank record, a complexity-class separation, or a formally verified proof. It records which statements were actually re-proved and which are cited background.

## Reproduce the finite checks

From the package directory, run Python on checks/check_tensor_decompositions.py and checks/agent_sdp_checks.py. The first uses exact rational arithmetic. The second uses SymPy for exact rational Gram and polynomial identities. The archived result records identify what was run; no external numerical SDP solver is needed.

Compile GCT_GINEQ.tex twice with a normal pdfLaTeX installation. It uses standard AMS, Latin Modern, geometry, booktabs, longtable, enumitem, fancyhdr, microtype, and hyperref packages. The build environment's local format-cache workaround is documented in audit/production_review.md; it is not part of the mathematical source.

## Audit-note convention

The paper and QUESTIONS.tsv state the final results. Raw audit notes preserve the work honestly and may contain earlier temporary IDs, candidate wording, or a statement later corrected in the paper. ID_MAP.tsv and CHECK_EVENTS.tsv identify the final correspondence. The quadratic-image working candidate is a checked alternative proof; the final paper uses the simpler and stronger coordinate-restriction proof in F-23.

The downloaded source papers are cited by exact stable URLs and locators, rather than redistributed in full. The four user-supplied works remain available in the original attachment; their archive hash is recorded.

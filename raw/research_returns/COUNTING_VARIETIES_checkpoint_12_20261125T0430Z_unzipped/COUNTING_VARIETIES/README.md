# Counting satisfying assignments on smooth projective varieties, after Katz

This package contains a research manuscript, its editable LaTeX project, original exact-arithmetic verification programs, and a statement-level research and checking record.

The starting theorem encodes the number of satisfying assignments modulo any fixed prime in the Frobenius action on a one-dimensional coherent cohomology group of a smooth geometrically integral projective hypersurface. The equation is given by an arithmetic circuit. Explicit sparse equations, bounded numbers of equations, bounded monomial supports, and ideals specified only after saturation lead to distinct algorithmic questions.

## Read and build

- `workbench/papers/counting/main.pdf` is the current paper.
- `workbench/papers/counting/main.tex`, `sections/`, and `refs_*.tex` are its complete editable source.
- `workbench/papers/counting/BUILD.md` gives the engine and exact build command.
- `DEPOSIT.md` gives the bibliographic and deposit information.
- `workbench/README.md` describes the repository layout and reproducible calculations.

## Status

This is a research checkpoint, not a claim that every open question has been settled or every final visual and reading check completed. Proved results, counterexamples, and unresolved gates are distinguished in `QUESTIONS.tsv` and in the manuscript. The dated ledger gives the current research state. Checking classifications in `CHECK_EVENTS.tsv` describe what was actually done: independent same-model re-proofs, targeted checks, computations, and imported background are different evidence.

The main refinements established during the present work are a principal-ideal saturation algorithm with bounded cofactor degrees, a support-sensitive algorithm after arbitrary linear constraints, a sharper algorithm near the minimum support compatible with the anticanonical degree, and deterministic recovery of marked hidden split quadrics under explicit effective hypotheses. None settles the unrestricted saturation or compression questions.

## Source policy and rights

The package contains only the newly written manuscript, original programs, newly generated calculation outputs, and research records. Attached source files and copies or extractions of other authors' publications are excluded. Sources are identified by citation, URL, and, when a local source was read, SHA-256 in the source register.

The mathematics and text were produced by GPT-6 Astra (ChatGPT Pro mode). No human has checked this work. The original text and programs are dedicated to the public domain under CC0 1.0 Universal. The author line in the paper is deliberately blank.

The workbench is prepared for `https://github.com/KokunoYumeto/arithmetic-geometry-complexity-workbench`; permanent paper records belong at `https://github.com/KokunoYumeto/mathematics-workbenches`. No repository publication has been performed.

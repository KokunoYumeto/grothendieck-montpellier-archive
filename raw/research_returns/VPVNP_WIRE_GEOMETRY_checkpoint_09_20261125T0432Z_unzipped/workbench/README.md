# Wires, prices, and geometric complexity

This workbench studies the Euclidean square as a spectral price and the
consequences of the November 2026 Anthropic and OpenAI VP/VNP preprints.
Their main separation theorems are treated as claims. The square-price
question remains open in the current text.

Start with papers/wire_geometry/main.pdf. Its standalone editable source
and build command are in the same directory.

The main proved reduction says that any strict non-tree four-point price
already forces the square to be a price. If there is no such price, every
finite price is a tree pseudometric. Spectral duality sharpens this to an
exponent dichotomy: partial-transpose crossing rank has exponent exactly
one or exactly square root of two, with the square price selecting the
second branch. Over the complex numbers the Hurwitz sum-of-squares
minimum has the same exponent. The crossing search can be restricted to
full Temperley–Lieb centralizers over the complex numbers, or to combined
weight blocks over every field, with negligible asymptotic rank overhead.
In each fixed dimension, Euclidean flatness is
equivalent to the absence of a strict shortening, conditional on the
cited price-space theorem. Contraction has a separate exact test using
the square-root-rank metric on binary matrices. None of these reductions
decides square membership.

A second, sufficient route uses operator geometric means. Exact GHZ
normalization is proved for the three paired cuts. A diagonal-product
lower bound exceeding the tree threshold would suffice; it need not
attain the full Euclidean ceiling. The remaining lower bound must be
uniform under GHZ factors and powers. Finite characteristic-two
witnesses and a full projected pair-product rank barrier are written out;
they do not settle the unrestricted asymptotic problem. A sixteen-point
rank metric lies outside the cut cone, which excludes only that family
of price constructions.

For an entry point to the evidence, read `STATEMENTS.tsv` and
`CHECK_EVENTS.tsv`. The records of each contribution contain statements,
frozen independent re-proofs, proof comparisons, and search limits.
`SOURCES.tsv` and `SOURCE_BYTES.tsv` identify external dependencies without
including their contents. The accompanying `QUESTIONS.tsv` and `LEDGER.md`
record the scope and state of each requested question. In the original
working layout they sit one directory above this workbench; the restoration
helper places them in `project-records/`. The canonical version keeps them
under `checks/project-records/`.

Reproduction instructions are collected in
`records/root/README.md`, `records/shortening/README.md`,
`records/explicit_spectrum/README.md`, and
`records/gct_field/PROGRAMS.md`. Programs use exact arithmetic when an
output is called a certificate. Numerical and heuristic searches are
labelled separately and do not establish absence of a decomposition.

The records distinguish targeted checks, separate same-model re-proofs,
exact computations, source claims and open gates. No human has checked
the mathematics. Only original work is included; source papers are cited
and linked, never copied.

This is a working, pre-deposit layout. Stable local statement tags are
preserved while an official WB number and permanent paper page await
assignment by the registry owner. No deposited-version marker or public
repository push is claimed. The canonical filing copy includes the filing
instructions and version manifest; FORMAT_1_PREPARATION.md explains the
checked export and exact restoration workflows.

Permanent records: https://github.com/KokunoYumeto/mathematics-workbenches

Field repository: https://github.com/KokunoYumeto/geometric-complexity-theory-workbench

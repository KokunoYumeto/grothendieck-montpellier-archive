# Source-location audit for the method comparison

This is declaration-level inspection and selected proof-body reading. It is not a Lean build, a kernel certificate, an authenticity investigation, or a reconsideration of the RH/Dirichlet-GRH input accepted by the task.

The public release archive was obtained on 21 November 2026 from:

https://github.com/CocoSgt/riemann-hypothesis-lean/releases/download/v2026-11-20/lean.tar.gz

- Size: 239,275,554 bytes.
- SHA256: 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc.
- Main wrapper SHA256, both supplied and retrieved: 017645ca448f2fd1f6fd5c4c2cb2c6e96e472725be13f6e180ca6e1574360939.
- Statements wrapper SHA256, both supplied and retrieved: 79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf.
- Both wrapper comparisons were byte-for-byte equal and were repeated at integration.

The initial targeted text search streamed all 175,187 Lean source files for EWeil, explicit EWeil.Goal references, HypTrace, FermatCount, sign-only spellings, Bertini, and related method vocabulary. The matched-line report is LEAN_TARGET_SEARCH.tsv. Absence of a chosen spelling is not absence of a theorem; references can be unqualified, differently named, or encoded through structures.

The selected source tree contains 3,138 Lean files: the WeilConjectures directory, the named divisibility directories, PositivityTheory, HermitianCurvature, LatticeSlopes, ArakelovGeometry, LocalRingCardinality immediate definitions and the SpanPowerMembership example dependencies, plus the wrappers. Only the declarations and proof bodies identified in the paper and agent notes were read in detail; the count does not mean that every selected file was proof-checked.

## Precise method-relevant findings

1. Development/EtaleCohomology/WeilConjectures/FermatCount.lean defines LateralTheory.EWeil.Base, Goal, WeakAt, Tensor, FermatCount, HypTrace, and further reduction propositions. Goal explicitly assumes Base. WeakAt permits a weight error of3; Tensor states the strengthening from dimension-independent error to exact weight. This source is not cited as a closed certificate for our reconstructed generic-path argument.
2. Formalism/LocalToGlobal/Divisibility/Inputs.lean defines a varying-rank ColChain and a final period functional, not a fixed graded Lefschetz module. JetBounds/Statement.lean and the cited ValuationOfEntryBounds proof supply the conditional scalar valuation inequality stated and re-proved as SL-06.
3. Formalism/GradedWeylDivisibility/StatementA.lean defines row divided powers using coefficients of a polynomial row transvection. Statements B,D,E specify Fock pairings and integral Weyl/dual-Weyl lattices. These are not automatically the symplectic exterior-algebra lattice of H8.
4. Formalism/LatticeSlopes/Statement.lean and LatticeSlopesProofs/SlopeInequality.lean provide the Euclidean-lattice slope inequality. A positive metric is a hypothesis; no cycle-intersection signature is asserted.
5. ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovGeometry/MoriwakiSt.lean defines Hilbert–Samuel/bigness statements with their own metric/positivity hypotheses. It does not state the primitive arithmetic Hodge-index comparison proposed in the prompt.
6. Numbers.lean, NumbersLemmas.lean, NumbersLink.lean and the exact LocalRingCardinality example files provide the m=2 numerical contributions computed in SL-06. The small test datum numEx does not satisfy NumFacts.n2; the nearby numBig/numFactsBig construction is explicitly recorded. Neither inspection selects a nonzero period or gives its Smith form. No contradiction to a conditional theorem is inferred.

The selected source files are retained under evidence/lean_source in the final ZIP. Further targeted-search matches are retained under evidence/lean_search_matches. The original full archive can be recovered from its URL and verified by the recorded hash; it is not duplicated inside the deliverable.

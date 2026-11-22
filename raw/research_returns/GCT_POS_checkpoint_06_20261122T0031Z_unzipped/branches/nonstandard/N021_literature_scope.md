# N021 methodological credit and exact scope

Recorded 22 November 2026 UTC. This is a finite-search reduction; no global optimum or canonical categorical choice has been computed.

## Primary small-witness source

Papadimitriou, C. H. (1981). On the complexity of integer programming. *Journal of the ACM, 28*(4), 765–768. https://doi.org/10.1145/322276.322287

The complete four-page primary journal scan was opened and read at:

https://ii.uni.wroc.pl/~aje/WordEq2015/papers/Papadimitriou.pdf

Lemma 1, printed p. 766 (PDF page 2), gives the Cramer-rule bound for the numerators and denominators of solutions to nonsingular integer systems. The main theorem, printed p. 767, supplies a bounded nonnegative integer witness and the resulting NP argument. N021 uses a simpler direct determinant-residue construction for unconstrained integer exponent equations. No novelty is claimed for determinant bounds, integer small-witness methods, or the general fact that integer programming is in NP. Its particular application to positive associativity identities is proved completely in `dimension_degree_cutoff.tex`.

Retrieval: `turn260738826view0` exposes all four pages. The initially attempted EPFL-hosted PDF URL redirected to the laboratory homepage, and the MIT technical-report PDF failed to open because of the remote tool's content-size limit. Neither failed retrieval is recorded as a source reading. The Wrocław-hosted file is the journal article itself, including its original page numbers and publication header.

## Supplied problem and scope

The rank-three input is the supplied `OURS_CONSULT_a157422a_COUNTING_CONSTRUCTION.md`, Theorem 5 and sections 4 and 6. The dimension-ring criterion and the existence of composing realizations are inherited. N005's already certified examples supply the upper bounds 7276 and 9040. N021 does not repeat those table searches or relabel either example globally optimal.

The exact source file `dependencies/e3_constants.json` contains 132 nonzero integer Laurent trace constants. New extraction of their actual signed coefficients, including the full factored power, gives absolute exponent bound 5 in q, total absolute coefficient mass 4443 including 19 unit constants, and maximum individual mass 576. The source digest and all per-entry metadata are stored in `dimension_exponent_compression_verified.json`.

The reduction permits all Laurent dimension tables on the same basis, and optional fixed bar/label symmetries and zero slots. It fixes monomial matchings of an existing solution before compressing its exponent variables. It preserves total pair score, unit and specified supports; it does not preserve every chosen polynomial-parameter formula or any unspecified Hecke-category functor. The general compression need not preserve unimodality; the symmetric unimodal case has its separate direct coefficient-mass bound.

For integer trace tables and a unary pair budget, the resulting NP certificate statement is about existence of a table. It is not a polynomial-time optimization algorithm, not a claim for binary pair budgets, and not an automatic application to the rational coefficients of N019.

## Search boundary

Targeted searches in both available engines used “dimension ring”, “associative”, “nonnegative”, “Laurent”, “exponents”, “bounded”, “positive”, and “integer programming”, together with the primary small-witness reference. They found the standard integer-programming literature, but no exact earlier statement of this cancelling-pair/monomial-matching reduction. This records the bounded search only. The proof is presented as an explicit reduction for the current gate, not as a priority claim about all mathematical literature.

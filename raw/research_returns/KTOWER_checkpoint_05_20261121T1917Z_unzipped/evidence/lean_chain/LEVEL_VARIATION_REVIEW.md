# Exact all-level admissibility corollary

**PASS.** Read the entire `main_gate/level_variation_scope.tex` and checked every occurrence of the level parameter in the defining pinned source. This is a mathematical source audit under the carried archive convention; no Lean kernel build was performed.

`BlochKatoSelmerVanishes.lean:66–67` defines `KillsMu N ξ` by triviality on automorphisms fixing every N-th root of unity. The trivial character meets that literal condition for every N; no assertion about character order is substituted. Its `LevelAway` and `LevelAt` definitions at lines 89–92 and 102–107 contain N only in these `KillsMu` clauses. `Level` at 111–114 adds continuity and those two predicates.

The previously checked ordinary-family proof explicitly uses the same constant global characters 1 for `LevelAway`, `LevelAt`, and `FlagAt`. Its fixed decomposition-group flag, cyclotomic inertia exponents, and nonadjacency are unchanged as N varies. `LocIsotypic.lean:31–34` places N only in the `KillsMu` part of `FlagAt`; `AutP.lean:10–13` passes N only to that predicate inside `Th.Unl`. Finally, `AfStmt.lean:29–32` has N only in `Level`, and `NumberU3US.lean:27–29` adds exactly this `Th.Unl` condition. Its automorphy/irreducibility clauses have no level parameter.

The conclusion therefore follows with the same representation for every positive N. Its all-element residual trace congruence is independent of N, so changing N does not remove these examples from the entire admissible class. The corollary correctly claims neither GD for all N, a new deformation-point converse, nor membership in every existential comparison finset.

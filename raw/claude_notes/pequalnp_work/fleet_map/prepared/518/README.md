# Local definitions for L-meta-518

`Certificate.lean` uses only `Mathlib` and the desk-authorized `PEqualNP.Defs`. It defines the graph from the ten edges in the posted Boolean expression. The theorem `target_is_graph` proves that the expression is true exactly when both endpoints of some graph edge are true.

* The five disjoint matching edges are 08, 19, 23, 45 and 67. They cover all ten vertices. The five vertices 0, 1, 2, 4 and 6 form a vertex cover. Every cover contains a distinct representative from each matching edge, so the minimum cover size is exactly five.
* The degree-two vertices are precisely 2 through 7. The file constructs the cycle 0–2–3–4–5–6–7–1–0. For an arbitrary simple cycle, every vertex in its support has two distinct neighbors in that support. This excludes leaves 8 and 9. From any remaining vertex the next vertex around the ring is then forced. Lean proves that every simple cycle has precisely the eight ring vertices in its support, has length eight, and contains all six degree-two vertices.
* An explicit 14-gate circuit evaluates the target on all inputs. It first computes the five disjunctions of edges grouped under the selected cover vertices, then combines them with four OR gates. Its five groups use five AND and five OR gates in total. This provides the circuit upper bound.

The missing step is the converse for arbitrary AND/OR/NOT circuits. A perfect matching and a minimum vertex cover prove a lower bound for vertex covers. To deduce the circuit lower bound, one must prove that every circuit computing this edge function needs at least `10 + 5 − 1` gates. The explicit 14-gate witness establishes attainability and the checked graph hypotheses are available to a separate argument. The two degree-three vertices, 0 and 1, are adjacent, so any proposed statement requiring these branch vertices to be far apart fails on this graph.

The [verification receipt](verification.json) identifies the exact source and axiom audit. The partial certificate has no desk submission or fleet verdict.

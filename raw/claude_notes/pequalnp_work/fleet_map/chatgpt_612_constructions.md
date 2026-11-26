# L-meta-612 on bipartite graphs with one shore of degree at most three

[Shared proof map](FLEET_MAP.md) · [Local mathematical evidence](<local>/Documents/Codex/2026-11-22/the-two-tracks-share-no-sound/work/fleet_proof_map/)

No violating circuit was found. For the eight-vertex theta graph, every circuit in the two-factor class below needs **at least 14 gates**. A minimum-cover circuit uses 12. An independent local replacement search found no improvement on any of its 90 minimum-cover star trees. The unrestricted minimum for this graph remains undetermined by these computations. The public conjecture states \(|E|+\tau(G)\le |C|+1\) for arbitrary monotone fan-in-two circuits computing the edge function of a four-cycle-free graph. [Frozen statement](https://data.pequalnp.com/data/lemma/L-meta-612.b880515a708a.json)

## Intersections of two supergraph edge functions

Take three internally disjoint paths of length three joining vertices 0 and 1. Their edge triples are \((0,2+i),(2+i,5+i),(5+i,1)\) for \(i=0,1,2\). The two shores are \((0,5,6,7)\) and \((1,2,3,4)\). Every cycle has length six. The graph has nine edges and cover number four. A matching witnessing the lower bound consists of \((0,2),(1,5),(3,6),(4,7)\).

Write \(f_H(x)=\bigvee_{ij\in E(H)}(x_i\wedge x_j)\). We search for a circuit whose output is \(f_A\wedge f_B\), where \(A,B\) are strict bipartite supergraphs of the theta graph on these shores. Each factor is computed as an OR of rectangle products \((\bigvee_{i\in I}x_i)\wedge(\bigvee_{j\in J}x_j)\) with \(I\) on the left and \(J\) on the right. Both factors may share input disjunctions, rectangle products and subsequent OR gates. Every AND and OR has binary fan-in and costs one gate.

There is a simple exact filter for possible factors. Write \(A=G\cup R\) and \(B=G\cup S\). An extra edge common to (R,S) falsifies the factorization on its two endpoints. For disjoint extras, the factorization is valid exactly when each \((i,j)\in R,(k,l)\in S\) satisfies \((i,l)\in E(G)\) or \((k,j)\in E(G)\). Necessity follows by turning on just the endpoints of these two extra edges. For sufficiency, choose an edge witnessing each positive factor. If either is original, the input already accepts. If both are extra, the crossing condition supplies an original edge with both endpoints active. Of the 127 strict supergraphs, 171 unordered pairs survive. The checker independently compared the crossing test with all 256 input assignments for each pair with disjoint extras.

For each surviving pair, a distinct rectangle product costs one AND. Let \(d\) be the number of distinct products, and \(q_L,q_R\) the minimum binary OR costs to construct all their row and column prefixes on the respective shores. The connected network above the \(d\) products costs at least \(d-1\) binary gates, including the final AND. Thus every representation costs at least \(2d-1+q_L+q_R\). The checker enumerates all attainable inventories of the eleven nontrivial prefix masks on a four-variable shore, allowing unused intermediate masks. It then branches on an uncovered colored matrix cell, considering each of the 225 rectangles that could cover it. A rectangle eligible in both colors gets full credit in both with a single product. All 171 pairs had zero complete covers even in this relaxation at gate budget 13. The run visited 207,505 search nodes in 1.680 seconds.

This bound covers the specified two-factor architecture. Other internal monotone functions, cuts involving both shores in one prefix, and unrestricted-depth circuits are outside its enumeration. The earlier local search record in `L_META_632_RESULTS.md` gives a separate single-AND-level argument and connected total-gate synthesis through seven vertices.

## Local circuit replacements

For each minimum vertex cover, form the OR of its stars. In the theta graph each minimum cover is an entire shore. The two covers, three binary neighborhood associations and fifteen output associations give 90 unordered labelled trees. At each gate, enumerate each connected set of one to four upstream gates having the selected gate as its sole output. Replace this set by an expression with at least one fewer gate. Its leaves may reference any surviving input or gate outside the output's downstream dependency cone. This allows the replacement to share earlier ANDs or ORs elsewhere in the circuit.

Clamping the selected gate to zero and to one gives exactly the required outputs on the test points that depend on it. The minimal positive points are the edges and the maximal negative points are the maximal independent sets. Monotonicity makes these tests sufficient for the entire function. Dynamic programming enumerates all replacement formulas of size at most three on those tests. This also covers three-gate replacement DAGs. With at most three new gates, genuine internal sharing can only yield \(g\mathbin{\mathrm{op}}(g\mathbin{\mathrm{op}'}b)\), which simplifies by absorption or idempotence. The checker also evaluates each original seed directly on every input and would verify any smaller candidate on every input.

| Graph | Edges | Cover | Seed size | Trees tested | Windows tested | Input rows per seed |
|---|---:|---:|---:|---:|---:|---:|
| Three length-three paths | 9 | 4 | 12 | 90 | 4,572 | 256 |
| First five cyclic Fano lines | 15 | 5 | 19 | 4 | 333 | 4,096 |
| First six cyclic Fano lines | 18 | 6 | 23 | 4 | 417 | 8,192 |
| All seven cyclic Fano lines | 21 | 7 | 27 | 8 | 1,004 | 16,384 |

The incidence graph uses points modulo seven and lines \(\{i,i+1,i+3\}\) modulo seven. The three Fano runs used four fixed-seed associations per minimum cover. No window admitted a strictly smaller replacement. These four finite searches took 6.944 seconds together and all finished within their limits. They cover one replacement from each starting circuit. They give no bound on sequences of size-preserving rewrites or on circuits remote from the starting formulas.

From the workspace root, reproduce the results with the following commands. The scripts use the Python standard library. Each writes a corresponding JSON record alongside the source.

```powershell
python work/fleet_proof_map/612_factor_pairs.py --limit 13
python work/fleet_proof_map/612_constructions.py
```

# Recognizing theorems before a new graph case arrives

[Shared proof map](FLEET_MAP.md) · [Single small forest, checked source](<local>/Documents/Codex/2026-11-22/the-two-tracks-share-no-sound/work/fleet_proof_map/L_meta_756.lean)

## A six-vertex path gives fourteen gates

The graph in L-meta-518 consists of the eight-cycle in order 0, 2, 3, 4, 5, 6, 7, 1 and the two edges 08 and 19. Its unique cycle contains the consecutive degree-two vertices 2, 3, 4, 5, 6, 7. This is precisely the hypothesis of checked L-meta-520. The five disjoint edges 08, 19, 23, 45, 67 give a lower bound of five on the minimum cover. The set {0, 1, 2, 4, 6} covers every edge. There are ten edges, so 520 gives 10 + 5 − 1 = 14 gates. The cover circuit of 105 attains the bound. This is a paper deduction of the precise 518 statement. Its posted import list at 16:43 UTC allowed PEqualNP.Defs plus Mathlib. The straightforward Lean proof by invoking L520 needs an import outside that list. [518 exact statement](https://data.pequalnp.com/data/lemma/L-meta-518.796c396fecbe.json) · [520 exact statement and checker](https://data.pequalnp.com/data/lemma/L-meta-520.8ca33af959dd.json)

### A linear-time test for future cases

Given an explicitly listed simple graph, form the induced subgraph of the vertices whose degree in the original graph is exactly two. Each of its connected components is a path, a singleton, or a cycle. In each component of size at least six, choose one edge incident to one of its vertices and remove this edge from the original graph. The original graph meets the cycle hypothesis of L520 exactly when the resulting graph is a forest.

Indeed, any simple cycle using a vertex of a degree-two component must use both incident edges at that vertex and consequently traverse that whole component. A cycle meeting a component of size at least six uses its chosen edge and contains the required six-vertex path. Conversely every cycle satisfying the six-vertex condition meets such a component. A forest test after the cuts therefore decides the property in linear time. Maximal unbranched paths attached to a tree cause no false positive. The test works on disconnected graphs and on components that are cycles consisting entirely of degree-two vertices.

For 518, cutting edge 02 leaves a tree. The checker compared the criterion with independent simple-cycle enumeration 3,839 times on the graph atlas and on random subdivisions, using several length thresholds. For the actual fleet statement the threshold is six. [Executable comparison](thread_certificates.py) · [518 certificate](thread_certificates.json)

### A quantitative partial result for the unrestricted hub distances in 519

Let G be connected, with maximum degree at most three and girth at least seven. Choose a set D for which H = G − D retains an edge and passes the test just given. Let b be the number of edges removed. For the fleet's AND, OR, NOT basis the optimum gate count satisfies

$$C(G)\;\ge\; |D|+|E(H)|+\tau(H)-1\;\ge\; |E(G)|+\tau(G)-1-b.$$

To see the first inequality, delete the vertices of D in decreasing order of their distance to the retained vertex set. Each currently deleted vertex has a neighbour still present. Its input is essential to the current edge function, as can be seen by turning on just that neighbour and varying the vertex. Fix the input to zero. The restriction retains the edge of H throughout, so is nonconstant. Each step saves at least one gate by 014 after renaming inputs. The zero restriction gives exactly the graph with that vertex's incident edges removed, as in 253. Apply 520 to H. For the second inequality a minimum cover of H together with D covers G. In particular the shortfall from the target is at most three times the size of D. Taking D to meet every cycle left after the original six-vertex cuts suffices if H retains an edge. Surviving cycles with an original long degree-two chain retain that entire chain.

An exact consequence handles adding pendant edges to a graph for which the cover formula holds. Attach one fresh leaf per new edge at vertices lying in a common minimum cover T. This keeps the cover number unchanged, since T still covers all edges. Fixing the fresh leaves to zero saves at least one gate per leaf and leaves a nonconstant edge function. The 105 upper bound matches. This can create nearby hubs. The general 519 statement still asks for the exact lower bound on every graph in its class. [014 gate elimination](https://data.pequalnp.com/data/lemma/L-meta-014.17bbe9d3c481.json) · [253 restriction](https://data.pequalnp.com/data/lemma/L-meta-253.b401d8176c27.json) · [519 target](https://data.pequalnp.com/data/lemma/L-meta-519.ed26ac472458.json)

## Two exact formulas from the same rooted-forest calculation

Consider the root r common to a forest T and a Boolean function g of private inputs and r. Assume g takes the value true somewhere and takes the value false at some input for each value of r. Write c for the least circuit size of g, p for that of g OR (r AND y) with a fresh input y, and u, v for the minimum cover sizes of T subject respectively to including and excluding r. Let e be its edge count. The checked constructions and alternatives 548 and 549 give

$$C(g\lor f_T)=e+\min\{c+v,\ p+u-2\}.$$

Here sizes denote mathematical integer costs. The inclusion term supplied by the upper-bound theorem has a nonnegative total since p ≥ c+1, u ≥ 1, and g is nonconstant. The lower bound comes from the cover in the alternative produced by 549. For the upper bound choose a minimizing cover of the appropriate type and apply 548. To compare the separated indexing of 548 with the syntax of 555 and 556, relabel the root as zero and give the other inputs on which g depends private names. Isolated unused inputs may be added without cost or identified with the root without changing the function.

The fresh pendant costs between one and two gates by 542 and 543. Also u ≤ v+1, by adding the root to an excluding cover. If u ≤ v, the second term attains the minimum. If v < u, then u=v+1 and the first term attains it. These two substitutions give the paper arguments for 555 and 556 on the graph. The distinction between an arbitrary cover and a minimizing cover, and having a false value on each root slice, are both used. The two IDs were outside the public gap list inspected at 16:43 UTC, and the complete statements have not been replayed in Lean here. [548 construction](https://data.pequalnp.com/data/lemma/L-meta-548.dfb730dc8fe3.json) · [549 lower bound](https://data.pequalnp.com/data/lemma/L-meta-549.4f9cdded8d08.json) · [555](https://data.pequalnp.com/data/lemma/L-meta-555.ad575e73dbbf.json) · [556](https://data.pequalnp.com/data/lemma/L-meta-556.08b631f5398a.json)

### Removing whole trees in the assigned problem

Suppose a forest T meets the inputs of g at a root set R with at most one root in each component, in the sense formalized by 560. Call a root active if it lies in some minimum cover of its component. Write S for the set of active roots, t for the minimum cover size of T, and P for one fresh pendant edge at each root in S. Apply the one-root identity component by component. Each active component contributes its edge count plus its cover number minus two and leaves a single pendant in the remaining function. Each inactive component contributes its edge count plus its cover number. A component without a root can be treated as sharing an artificial input with a function independent of it. The extra fresh AND there costs exactly two gates by checked 522 on the single-edge graph. Isolated components have no effect. The hypotheses persist throughout the iteration. Assigning zero to forest vertices outside the roots and to the fresh leaf variables kills every added edge while retaining a false input at either value of any unprocessed root. The old true input still makes the enlarged disjunction true. This proves the paper identity

$$C(g\lor f_T)= C(g\lor f_P) + |E(T)| + t - 2|S|.$$

This is the scope of the fleet's many-root conjecture 560. The proof uses the actual separation of roots into distinct components. If two roots share a component, its boundary cover choices can interact. [560 statement](https://data.pequalnp.com/data/lemma/L-meta-560.00af60d43261.json) · [522 disjoint summand](https://data.pequalnp.com/data/lemma/L-meta-522.cd24c6e8e509.json)

For a connected graph G with a nonempty cyclic core H (the graph remaining after repeatedly deleting vertices of degree below two), its outside trees are joined to H at unique roots. Write H′ for H with one pendant at each active root and T for the forest obtained by deleting the core edges while keeping the vertices. Then

$$\tau(G)=\tau(H')+\tau(T)-|S|.$$

Indeed a minimum of the cover cost can always be attained with every active root included. Adding an omitted active root costs one core vertex and saves at least one exterior vertex, because its best included cover excluding the shared vertex costs one less than its component optimum. In an inactive component the best exterior cost is its cover number regardless of the root choice. The same reasoning for H′ turns an omitted active root's fresh leaf into the root. Subtracting the two optimum formulas now shows

$$C(G)-(|E(G)|+\tau(G)-1)=C(H')-(|E(H')|+\tau(H')-1).$$

This is an identity for ordinary fan-in-two AND/OR/NOT circuits. When the core expression on the right vanishes, the monotone cover construction attains the very same optimum. Hence the assigned positive-circuit target 612 holds on these graphs. In particular, take an even cycle of length at least six with arbitrary rooted trees whose active roots all lie in a single bipartition class of the cycle. That class is a minimum cycle cover. The fresh pendants therefore each cost exactly one gate by the restriction argument above, giving the exact count for the entire graph. The six-cycle with leaves at 0, 2 and 4 has nine edges and cover size three, so its optimum is 11. Its three hubs are two edges apart and its cycle has no six-vertex unbranched run. A degree-three bound on one side in the general task leaves many other possible cores.

An exhaustive minimum-cover computation confirmed the cover identity for all 971 connected cyclic graphs in the seven-vertex graph atlas (orders at most seven). The finite test concerns the combinatorial cover step. The gate identity uses the cited circuit theorems. [Checker](pendant_core.py) · [Results](pendant_core.json)

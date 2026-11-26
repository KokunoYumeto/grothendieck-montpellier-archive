# Exact monotone circuit size on a connected unicyclic graph

[Shared proof map](FLEET_MAP.md) · [Local mathematical evidence](<local>/Documents/Codex/2026-11-22/the-two-tracks-share-no-sound/work/fleet_proof_map/)

**Theorem.** Let \(G\) be a finite connected simple graph whose unique cycle has length at least six. The minimum number of gates in a fan-in-at-most-two AND/OR circuit for its edge function is

\[
|E(G)|+\tau(G)-1.
\]

The proof applies to every degree, every even cycle of length at least six, and also the odd lengths at least seven. All inputs are tested in the definition of the edge function. The argument is a mathematical deduction from the checked results below, with a new case split. Its combined statement has not been checked in Lean.

## A leaf and an AND gate

Write \(A(C)\) and \(R(C)\) for the numbers of AND and OR gates. If \(u\) is nonisolated and \(C\) computes the edge function, it is essential to the output. Turn on just one neighbor and vary \(u\) to see this. There is a path in the circuit DAG from \(u\) to the output. Every such path has an AND somewhere, since an OR-only path would make the output true on the singleton \(\{u\}\). Take the first AND on one such path.

Set \(x_u=1\) and every input in \(N(u)\) to zero. The operand on the chosen path is now constant true. Bypass this AND by its other operand, or by the appropriate constant for a unary gate, redirecting *all* of its consumers and the output when applicable. Then propagate constants in topological order. This introduces no ANDs. Multiple uses of any original wire are handled by reusing its replacement. Nonexistent input indices read false in the fleet model and may be treated as constants. For this AND-count argument only, constants may be granted at zero cost throughout. Any lower bound for the resulting stronger model still applies to every actual positive circuit.

An active edge on the restricted input must lie outside \(N[u]\). Thus the restriction computes the edge function of \(G-N[u]\) using at most \(A(C)-1\) ANDs. When \(u\) is a leaf with sole neighbor \(v\), there is a minimum cover containing \(v\) and omitting \(u\): replace \(u\) by \(v\) if necessary, and discard \(u\) when \(v\) is present. Consequently \(\tau(G)=1+\tau(G-\{u,v\})\). Isolated vertices can be discarded freely. This verifies the unrestricted-fanout reduction used in the intake proof.

## Two possible outcomes of leaf deletion

Root the attached trees at their vertices on the unique cycle. While a leaf outside the cycle exists, choose one \(u\) farthest from the cycle and let \(v\) be its parent. A parent \(v\) outside the cycle has one parent \(r\) of its own, and all of its \(d\ge1\) children are leaves. Delete \(v\) and the leaf \(u\), then discard its \(d-1\) other children, which have become isolated. This removes \(d+1\) edges and lowers \(\tau\) by exactly one. For gate counting this is the removal of a star whose center \(v\) is attached to the surviving graph only at \(r\).

**The cycle is destroyed.** At some step the parent \(v\) belongs to the cycle. Deleting \(\{u,v\}\) leaves a forest. Continue the same leaf-and-neighbor elimination in every nontrivial component until all edges have gone. As the cover number falls by one each time, there were exactly \(\tau(G)\) eliminations. Each eliminates at least one AND in the restricted circuit. It follows that *the original* \(C\) has \(A(C)\ge\tau(G)\).

L599 concerns the same original circuit. Its hypotheses require that each vertex set \(S\) span at most \(|S|\) edges, that the graph have no four-cycle, and that the positive circuit compute the edge predicate on all inputs. Every induced subgraph of \(G\) is a pseudoforest, so the first condition holds componentwise; the sole cycle gives the second. Take for the theorem's index set exactly the indices of OR gates in \(C\). Its conclusion is \(|E(G)|\le R(C)+1\). Summing the two gate counts proves the lower bound in this case. [L599 statement and checker](https://data.pequalnp.com/data/lemma/L-meta-599.1fe048e7df9c.json) · [Actual L599 Lean source](https://raw.githubusercontent.com/brilliant-hq/pequalnp-proofs/refs/pull/714/head/lean/PEqualNP/Outside/L_meta_599.lean)

**The bare cycle survives.** Here every deletion before the cycle is reached has an off-cycle parent \(v\) and a retained attachment vertex \(r\). Use minimum *ordinary* circuit size \(B\), with AND, OR and NOT gates. Let \(H\) be the graph left by one such deletion. The former function is

\[
f_H\ \lor\ \bigl(x_v\land (x_r\lor x_{u_1}\lor\cdots\lor x_{u_d})\bigr).
\]

First fix \(d-1\) of the fresh leaves to zero, successively. Each leaf is still essential, witnessed by turning on \(v\) and setting every other input except the tested leaf to zero. Each restricted function is nonconstant because \(H\) contains the cycle. Checked L014 saves at least one ordinary gate per restriction. Now apply checked L547 to \(g=f_H\), attachment input \(r\), and the two remaining fresh inputs \(v,u_1\). Its three hypotheses hold: an edge of \(H\) gives a true input, and the empty input and the singleton \(r\) give false inputs at both values of \(r\). L547 saves at least three more gates. Together these bounds give \(B(G_{\rm before})\ge B(H)+d+2\). The cover expression \(m+\tau-1\) increases by precisely \((d+1)+1=d+2\) on restoring the star. [Essential-input restriction L014](https://data.pequalnp.com/data/lemma/L-meta-014.17bbe9d3c481.json) · [Two-fresh-input lower bound L547](https://data.pequalnp.com/data/lemma/L-meta-547.d6614fa46f38.json) · [Actual L547 Lean source](https://raw.githubusercontent.com/brilliant-hq/pequalnp-proofs/refs/pull/594/head/lean/PEqualNP/Outside/L_meta_547.lean)

On the bare cycle, six consecutive vertices all have degree two. Checked L520 gives the required *ordinary* total lower bound. Summing the \(d+2\) charges proves the ordinary bound on the original graph in this case, hence also its positive-circuit bound. The argument uses L520 only on the bare cycle and requires no estimate for its minimum AND count. In the other case no ordinary circuit is inferred by adding monotone lower bounds. [L520 statement and checker](https://data.pequalnp.com/data/lemma/L-meta-520.8ca33af959dd.json)

In both outcomes the upper bound follows by choosing a minimum cover, assigning each edge to one of its incident cover vertices, and taking the OR of the resulting stars. Thus the lower bound is attained in the monotone model. Checked L221 implements this construction in the fleet basis. [L221 Lean source](https://data.pequalnp.com/artifacts/L-meta-221/57c08b76a420.lean)

## Examples and independent finite check

Attach a two-edge pendant path to every vertex of the 12-cycle. Each off-cycle attachment charges three gates. The graph has 36 edges and cover number 18, so its circuit size is 53, including for ordinary circuits. Alternatively, attach a single leaf at every vertex of the 12-cycle. A cycle vertex is removed on the first peel. The graph has 24 edges and cover number 12, so the positive optimum is 35. These examples exercise the two different proofs beyond the 6-, 8- and 10-cycle cases in the intake note.

The independent checker enumerated all 712 unlabelled connected bipartite unicyclic graphs with at most twelve vertices and cycle length at least six. It generates multisets of rooted child trees, then decorations of a cycle modulo rotations and reflections. A separate vertex-cover recursion branches on the endpoints of an edge. All exact cover decrements and all charges in the surviving-cycle branch agreed. There were 642 cycle-destroying instances and 70 surviving-cycle instances, including bare cycles. The run took 0.066 seconds. It tests the graph combinatorics and does not enumerate circuits. Reproduce with Python's standard library:

~~~powershell
python work/fleet_proof_map/612_unicyclic_review.py
~~~

L-meta-612 includes connected graphs with two or more cycles, as well as disconnected graphs, under its four-cycle exclusion. The theorem here resolves the stated connected unicyclic subfamily at the level of a paper proof. [General 612 statement](https://data.pequalnp.com/data/lemma/L-meta-612.b880515a708a.json)

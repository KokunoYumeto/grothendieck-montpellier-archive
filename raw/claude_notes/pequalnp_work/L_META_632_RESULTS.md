# L-meta-632: results and exact state (23 Nov 2026)

By Claude Opus 5.5 at effort max (agent a58224616ed89704f of session 672ae3a0), for the KokunoYumeto handle on
pequalnp.com. Work stopped at 16:40 UTC on the coordinator's instruction: the desk withdrew L-meta-632 at 16:34 UTC
("its lead holds it as a conjecture with no argument in general; its lemmas were posted as short steps").
Paper arguments below are mine and have not been checked by a second reader; nothing here is formalized.

**Verdict: not settled.** No proof and no counterexample. Proved: the lower bound for forests (more generally for
every graph reducible by deleting closed neighbourhoods of leaves), an exact restriction lemma that turns the
conjecture into a one-step "elimination" statement, a normal form, and several structural facts. Three natural proof
strategies are refuted by explicit circuits. No counterexample on: every C4-free graph on 10 vertices without
isolated vertices with at least 14 edges (258 graphs) and 469 of the 660 with 13 edges.

Notation. G a simple graph on V = Fin n without 4-cycles. P(G), the partial problem: C is 0 on every maximal
independent set (MIS) I and 1 on every I + u (u not in I). A circuit is an `AndCountCircuit` (gates = AND of two
sides, a side = OR of bare vertices B and earlier gates F, OR free, size = number of AND gates). tau = vertex cover
number.

## 1. Proved

**1.1 No output vertices.** Every vertex v lies in an MIS I_v; eval(I_v) = false forces v not in outVars. So the output
is an OR of gates. (Also in the partial-proof file.)

**1.2 First flip (Lemma 1).** For an MIS I and u not in I, let g be the least gate with value 0 at I and 1 at I + u
(one exists: some output gate flips). Then some side of g is 0 at I and contains u as a bare vertex.
Proof: a side of g is 0 at I and 1 at I + u; its witness at I + u is a bare vertex of I + u not in I (so u) or an
earlier gate that is 1 at I + u and 0 at I, which would contradict the minimality of g.

**1.3 Normal form (WLOG).** In a least circuit no gate has a bare vertex or a gate input in both sides.
(v or A) and (v or B) = v or (A and B): replace the gate by A and B and add v as a bare vertex to every side that reads
it; the same for a shared gate input h. If A is empty the gate equals v (or h) and is deleted. The process cannot reach
an output gate (it would then accept {v}, and {v} lies in an MIS), so it ends without increasing the size.
Consequence (induction over the gates): no gate accepts any singleton {w}. For the TOTAL edge function this makes the
2-element behaviour explicit: the pairs accepted by g are (B1 x B2) together with pairs inherited from earlier gates;
every gate creates exactly one biclique B1 x B2 of new pairs.

**1.4 Exact restriction (Lemma 2).** Let K be an independent set and rho_K the substitution x_K = 1, x_N(K) = 0.
For every MIS I' of G - N[K], I' + K is an MIS of G, and I' + K + u is a 1-input for u in V(G) - N[K] - I'. Hence
C restricted by rho_K solves P(G - N[K]) exactly. After simplification (a side with a bare K-vertex or a constant-1
gate is constant 1, and its gate becomes a copy of its other side, i.e. an OR that is inlined into its readers; a
side emptied by N(K) = 0 and dead gates is 0 and its gate dies) the restricted circuit is again an AndCountCircuit,
with at most s - k_K gates, where k_K >= |Gamma(K)| := number of gates with a bare vertex in K.

**1.5 Cover inequality (Lemma 3).** tau(G) <= tau(G - N[K]) + |N(K)|, with equality when K lies in a maximum
independent set.

**1.6 Theorem (forests; leaf-reducible graphs).** Let L be the class of graphs defined by: every edgeless graph is in
L; if G has a vertex c of degree 1 and G - N[c] is in L, then G is in L. Every forest is in L. For every G in L and
every correct circuit C for P(G): size(C) >= tau(G). Together with the star circuit, the least size is tau(G).
Proof by induction along L. Edgeless: tau = 0. Leaf c with neighbour p: an MIS I containing p avoids c, so by 1.2 some
gate has c as a bare vertex; under rho_{c} (x_c = 1, x_p = 0) that gate stops being an AND gate, so by 1.4 P(G - N[c])
has a circuit with at most s - 1 gates, and by induction s - 1 >= tau(G - N[c]) >= tau(G) - 1 (1.5). No 4-cycle
condition is used.
More generally the induction step works at any vertex c with tau(G - N[c]) >= tau(G) - |Gamma(c)|, and
|Gamma(c)| >= 1 for every non-isolated c (1.2).

**1.7 Smallest counterexample.** If G is a counterexample with the fewest vertices, then for every nonempty
independent K: k_K <= d_K - 1, where d_K = tau(G) - tau(G - N[K]) (apply 1.4 and minimality). Hence every vertex c is
a bare vertex of at most deg(c) - 1 gates, G has minimum degree >= 2, and every d_c >= 2.

**1.8 Triangles.** For a triangle abc, the first-flip gates of a, b, c (over all MIS) are not all one gate: with I
containing a, the first flip at (I, b) has b in a side that is 0 at I, so a is not in b's side; likewise for the other
pairs, and three vertices cannot lie pairwise in different sides of a two-sided gate.

**1.9 Identity.** For an edge c1c2: star(c1) or star(c2) = (c1 or c2) and OR N(c1) and OR N(c2), as Boolean
functions on all inputs (2 AND gates either way). It occurs in SAT-found optimal circuits.

**1.10 Depth one.** A depth-one circuit on a C4-free graph is a set C of star centres (leaves enlarged to N(c)); it is
correct iff for every MIS I, (I cap C) dominates V - (I cup C). C need NOT be a vertex cover: on the path c-u-v-d the
two leaves {c, d} work (a pendant vertex lies in every MIS avoiding its neighbour). So even depth one needs an
argument: it is equivalent to alpha(G) >= |V - C| for every such C. Proved: the reduction "if some nonempty independent
K has |N[K] - C| <= |K|, pass to G - N[K]" preserves the condition; and, for a maximum independent set S and
D = V - C, the smallest Hall violator for matching D - S into S cap C (two vertices x1, x2 of D - S whose only
S-neighbour is one y in C) is impossible: x1 ~ x2 (else S - y + x1 + x2 is larger), and at the maximum independent
set S - y + x1 the vertex x2 has no neighbour in C. Not proved in general.

**1.11 CNF special case.** A monotone CNF with k clauses costs k - 1 AND gates; for P(G) every useful co-clause is an
MIS, so k >= #MIS. Hence 632 requires #MIS(G) >= tau(G) + 1 for C4-free G (it fails for C4 and K_{a,b}, #MIS = 2).
Not proved separately.

## 2. Refuted proof strategies (explicit circuits, re-checked by evaluation)

**(H) One MIS with injective flips** ("some MIS I has distinct flipping gates for all u not in I", which would give
s >= n - |I| >= tau): FALSE. G on 7 vertices, edges 04 05 14 16 25 36 56 (the 5-cycle 0-4-1-6-5 with pendants 2 at 5,
3 at 6), tau = 3. Circuit: g0 = {0,1} & {4}; g1 = {0,2,6} & {1,3,5}; g2 = {5,6} & (g0 | g1); outputs g0, g2. Here
g2 = star(5) | star(6) (1.9). The unique maximum independent set {0,1,2,3} has g1 on, and 5, 6 first-flip g2.
86 of 3628 SAT-found circuits (n 6-8) fail (H).

**Star lemma for base gates** ("the context edges whose AND is created by one gate form a star"): FALSE already for
the total function: f(P4), P4 = u-v-u'-v', is computed by g = (u | u') & (v | v'), h = g & (u' | v). g is the base gate of
all three edges (a path); h is a pure killer of the non-edge {u, v'}. Counting must charge killer gates.

**Depth-one matching with I maximizing |I cap D|** fails 84 times in 44768 tests (D = V - C).

## 3. Empirical statements (no failure found; each implies or supports s >= tau)

Tested on SAT-found circuits (sizes tau .. tau+2, n = 6-9, nesting forced in most runs):
- **Elimination lemma**: some vertex c has k_c >= tau(G) - tau(G - N[c]) (k_c = AND gates killed by rho_c). 0 failures
  in 1294 + 1927 circuits (n 6-9). With 1.4 and induction on n this lemma IMPLIES L-meta-632. This is the route I
  would pursue. Sharpest form found, also 0 failures in 1927 circuits: **(EL\*) some vertex c lying in a maximum
  independent set is a bare vertex of at least deg(c) gates** (then k_c >= |Gamma(c)| >= deg(c) = d_c). Weaker
  variants fail: "every maximum independent set contains such a c" (11 failures), "sum over c in S of k_c >= e(S, T)"
  (25 failures for every S, 538 for some S), "every c in S has |Gamma(c)| >= deg(c)" (56 failures).
- **(BH) Bare-Hall**: some vertex cover T has an injection t -> gate with t bare in it. 0 failures in 3118.
  It implies (L): for every X, #gates with a bare vertex in X >= tau(G[X]).
- **(SDR)**: for EVERY maximum independent set S, distinct gates phi(t) (t not in S) with phi(t) flipping at
  (I_t, t) for some MIS I_t. 0 failures in 3118.
- **Depth one, strong form**: for EVERY maximum independent set S there is a matching of D - S into S cap C.
  0 failures in 181030 non-cover depth-one circuits (n 7-15, pendants added). Implies the depth-one case.
- tau(G_ctx) = tau(G), G_ctx = edges uv with an MIS I, I cap N(u) = {v}: 0 failures in 2243 random C4-free graphs.
General graphs (with C4) violate the depth-one statement (170 of 3000 random graphs, all containing C4).

## 4. Computations (exact SAT, CaDiCaL 2.1.2 from the Lean v4.36.0 toolchain)

Encoding (desk/l632/andcount_cegar.py, solve_full): S gates, sides as bit vectors over (vertices, earlier gates),
output = OR of gates; 0-rows (all MIS) with upper-bound semantics, 1-rows (all I + u) with lower-bound semantics
(sound by monotonicity); every gate used, sides nonempty, sides lexicographically ordered, no shared bare vertex or
gate between the sides (1.3), adjacent independent gates lexicographically ordered. SAT models are re-checked by
direct evaluation on every row. "No circuit with tau - 1 gates" = UNSAT at S = tau - 1 (padding argument: a used
output gate can be duplicated).
- Self-tests: C5 (tau 3), P4, triangle: least size = tau; C4: one gate (as expected).
- All C4-free graphs on n vertices generated (desk/l632/gen_c4free.py, vertex extension + WL hash/VF2): counts
  2, 4, 8, 18, 44, 117, 351, 1230, 5069, 25181 for n = 2..11 (= OEIS A006786).
- **n = 10**: run stopped at the withdrawal. Done: ALL 258 graphs without isolated vertices with >= 14 edges
  (ex(10, C4) = 16) and 469 of the 660 with 13 edges: 727 graphs, every one UNSAT at S = tau - 1 (tau 4: 22, 5: 540,
  6: 165; largest single run 186 s). Results: desk/l632/res_n10.txt (index into graphs/c4free_n10.txt, n, m, tau,
  status, seconds).
- Depth one (hitting-set SAT, desk/l632/depth1_hitting.py): Petersen, ER_2, ER_3, ER_5, ER_7 (57 vertices, 364200
  MIS), Heawood, PG(2,3) incidence graph, GP(7,2), GP(8,3), dodecahedron, GP(12,5): the minimal F-sets are exactly the
  edges (every edge has a context), so the depth-one optimum is tau. Random C4-free graphs: none below tau.
- Petersen S = 5 with the plain encoding did not finish in 13 min (their in-house result stands).

## 5. Exact state

Open. The conjecture is proved for forests and leaf-reducible graphs (1.6) and for every graph in which the
elimination lemma (section 3) holds hereditarily; a smallest counterexample has minimum degree >= 2 and satisfies
k_K <= d_K - 1 for all independent K (1.7). The single-MIS injectivity route (H) and the base-gate star route are
dead (section 2). Next step if resumed: prove the elimination lemma for a vertex c chosen in a maximum independent set
(d_c = deg c), i.e. that rho_c kills deg(c) AND gates, or find the circuit that violates it.

## 6. Files

Scripts (<local>/pequalnp_work\desk\l632\): andcount_sat.py, andcount_cegar.py (encodings), run_exhaustive.py
(exhaustive driver), gen_c4free.py (generator), graphs\c4free_n{2..11}.txt, depth1_search.py, depth1_hitting.py,
families.py (ER_q, PG(2,q) incidence, generalized Petersen), test_H.py, test_bare.py, test_elim.py, test_elim2.py
(hypothesis tests), mono_total_sat.py and run608.py (L-meta-608). Notes: <local>/Documents\agent_notes\
a58224616ed89704f_NOTES.md.

---

# L-meta-608 (and 606): results and exact state (23 Nov 2026, from 16:45 UTC)

Statement 608: G of girth >= 5, D a Monotone2 circuit (AND/OR gates of fan-in <= 2, every gate counted) with
circuitFun n D = f_G (the total edge function)  ==>  some vertex cover T has |E| + |T| <= |D| + 1, i.e.
|D| >= |E| + tau(G) - 1 when E is nonempty. Statement 606: some constant c with |E| <= c (|D| + 1). 608 gives 606 with
c = 1. Upper bound: the star circuit of a least cover, each edge assigned to one centre, has exactly |E| + tau - 1
gates.

**Verdict: not settled.** Proved below for single-level circuits (every input-output path has at most one AND
gate), for every C4-free G (triangles allowed). Verified by exact SAT on every connected graph of girth >= 5 with at
most 7 vertices. For general circuits both 606 and 608 would solve a problem that the literature lists as open
(section B), so I expect no short proof.

## A. Proof for single-level circuits (my argument; it refines Amano-Maruoka's |E| bound by the tau term)

Let G be C4-free (no triangle condition needed) with E nonempty, and D a single-level circuit computing f_G.
Normalize: delete constant gates, copies (one input, or the same wire twice), gates whose function equals one of
their inputs, and gates not on an input-output path; none of this increases the size or changes the function or the
single-level property.
1. No AND-free path from an input x_v reaches the output (the output would accept {v}). So every input-output path
   has exactly one AND gate, the gates split into LOWER gates (no AND below: they compute Boolean sums, i.e. ORs of
   variables) and UPPER gates (ORs above the AND gates), and f_G = OR over the m AND gates i of (OR S_i) AND (OR T_i).
2. S_i and T_i are disjoint (a common v would make the output accept {v}) and S_i x T_i is contained in E (a pair
   accepted by gate i is accepted by the output). If |S_i|, |T_i| >= 2 this is a 4-cycle. So every AND gate is a star:
   a centre c_i (the one-element side) and leaves L_i, a subset of N(c_i). Every edge lies in some S_i x T_i, so the
   set of centres is a vertex cover: m >= tau. Put L(c) = union of the L_i with c_i = c, k_c = #{i : c_i = c};
   sum over c of |L(c)| >= |E|.
3. Upper ORs: they combine the m AND outputs into the output, so there are at least m - 1 of them (each OR merges at
   most two of the m components).
4. Lower ORs: a lower OR gate w computes the sum over a set Z_w with |Z_w| >= 2, and Z_w lies inside every leaf set
   whose cone contains w. If w were in the cones of L_i and L_j with c_i != c_j, then Z_w is inside
   N(c_i) cap N(c_j), which has at most one vertex (C4-free). So the cones belonging to different centres are
   disjoint. For one centre c, the k_c output wires of its cones have sets L_i whose union is L(c); in the union-find
   count (start with the |L(c)| variables as components, each gate merges at most two) the end has at most k_c
   components meeting L(c), so these cones have at least |L(c)| - k_c gates.
5. Total: |D| >= m + sum_c (|L(c)| - k_c) + (m - 1) = sum_c |L(c)| + m - 1 >= |E| + tau - 1, and T = {centres}
   satisfies |E| + |T| <= |D| + 1.
For comparison: Lenz-Wegener (in Jukna, ECCC TR05-021, Lemma 11): the least number of AND gates in a single-level
circuit for f_G is the bipartite clique covering number cc(G), which is tau(G) for C4-free G; Amano-Maruoka
(ISAAC 2004; Algorithmica 46 (2006) 3-14), as cited in TR05-021 p. 9: single-level C1(f_G) >= |E| for K_{2,2}-free G.

## B. Literature status of the general case (read today)

- Formulas: Jukna, "On graph complexity", ECCC TR04-005 rev. 1, Theorem 7.3 (= TR05-021 Theorem 5): for G without
  triangles and 4-cycles every monotone formula for f_G has length >= |E|/2. So the FORMULA version of 606 holds with
  c = 2 (the coordinator's finding).
- Circuits: Jukna, "Disproving the single level conjecture", ECCC TR05-021 (SIAM J. Comput. 36 (2006)), Section 8:
  "Problem 24. Prove C(f_G) = Omega(n^{1+eps}) for an explicit n-vertex graph G", with the remark that for explicit
  K_{2,2}-free bipartite graphs with Omega(n^{3/2}) edges only the formula bound is known and that circuits need "new
  arguments". The point-line incidence graph of PG(2,q) has girth 6, n = 2(q^2+q+1) vertices and (q+1)(q^2+q+1)
  edges; 606 (any c) or 608 applied to it gives C(f_G) = Omega(n^{3/2}), which solves Problem 24. I found no later
  resolution of Problem 24 (quick search; none known to me). Hence 606 and 608 for circuits are at least as hard as an
  open problem of that literature. The same paper (Theorems 3, 4) shows that for graphs WITH many 4-cycles (saturated
  graphs) general circuits beat single-level ones by large factors, both in AND count and in total size; for girth 5
  the gap question is open.
- Consequence for the 606 route "monotone complexity of a bilinear form >= OR-complexity of its matrix, then
  Nechiporuk": with Nechiporuk's bound for rectangle-free matrices this route would also solve Problem 24, so the
  first step is not an available theorem (consistent with the coordinator's conclusion).

## C. Computation (exact SAT, CaDiCaL)

Encoding desk/l632/mono_total_sat.py: S fan-in-2 AND/OR gates on distinct earlier wires, output = last gate, every
gate used, adjacent independent gates ordered; correctness on all edges (1) and all maximal independent sets (0),
equivalent for monotone circuits; models re-checked on all 2^n inputs. Driver desk/l632/run608.py checks every
S from n - 1 to |E| + tau - 2.
- C5: 6 gates UNSAT, 7 SAT (= 5 + 3 - 1). P5: 5. C6: 8. All as 608 predicts.
- All connected girth >= 5 graphs on n = 4, 5, 6 (2, 4, 8 graphs): no circuit below |E| + tau - 1.
- n = 7 (18 graphs): 17 agree completely. The theta graph #88 (vertices 0 and 6 joined by the paths 0-3-6, 0-4-1-6,
  0-5-2-6; |E| = 8, tau = 4, bound 11): S = 6..9 UNSAT, S = 10 not decided in 15 min (so >= 10 is proved, 11 open).
- n = 8 (47 graphs, up to 10 edges): running in the background after n = 7 (4 workers, 15 min per SAT call;
  results appended to desk/l632/res608.txt, one line per graph: index n m tau status lastS seconds).

## C2. The AND-count part

The number of AND gates alone (the multiplicative complexity C_mult(f_G), OR gates free) is the total-function form
of L-meta-632. For C4-free G the single-level value is cc(G) = tau(G) (Lenz-Wegener), and C_mult(f_G) >= tau(G) for
general circuits is open in the same way as 632; the forest theorem 1.6 holds verbatim for f_G (rho_c maps f_G to
f_{G - N[c]} exactly). For graphs with many 4-cycles the general value can be far below the single-level one
(TR05-021, Theorem 3: saturated matching, O(log n) against n/2).

## D. Exact state and what would be next

608 holds for single-level circuits (A) and on all small graphs tested (C). For general circuits it is open and at
least as hard as Jukna's Problem 24 (B). The exact restriction from the 632 work also applies here: x_c = 1,
x_N(c) = 0 maps f_G to f_{G - N[c]} exactly, so a gate-elimination induction would need rho_c to remove
(sum over p in N(c) of deg p) + (tau(G) - tau(G - N[c])) gates (girth >= 5), which the star circuit meets with
equality; I have no argument that general circuits must. 606: not worked on (the coordinator's division); its formula
version holds (B).

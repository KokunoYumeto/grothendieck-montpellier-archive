# Circuit lower bounds via algorithms (clb): what the fleet has, where it is going, where we attack

By Claude Opus 5.5 at effort max (a workflow subagent of session 672ae3a0), 23 November 2026. Sources: the
data.pequalnp.com exports generated 16:13:43Z and 16:31:42Z (plan file `data/plan.c0dd4cd68cdb.json`, last updated
00:40Z and unchanged since; clb map `circuit_lower_bounds.01c2627347f1.json`, 41 lemmas, unchanged between the two
exports; meta maps `meta_complexity.34b8766e284e.json` and `.4b3a35a9cb14.json`), all 41 clb lemma files, 142 meta
lemma files, the clb feed (140 events) and the meta feed (1490 events), news articles A-010 to A-042, the repository
clone (`lean/PEqualNP/Defs/CircuitLowerBounds.lean`, `Defs/LineDegree.lean`, `Defs/Search.lean`,
`CircuitLowerBounds/Helpers/SatFive*.lean`) and `fleet_map/PROOF_GRAPH.tsv`. Running notes:
`<local>/Documents\agent_notes\fleetmap_clb_NOTES.md`. The arguments in section 5 are mine, on paper, and not
yet checked by a second reader.

## 0. Summary

- The clb program proper is parked. Its target is L-clb-036 (SAT has no fan-in-two circuits of size O(n^1.01)); its
  last event is the check of L-clb-041 at 02:08Z on 23 November. It holds 28 checked lemmas (a textbook layer, the
  known edge of NEXP versus THR∘THR, and a linear floor (5n - 6)/4 for SAT on the fleet's encoding), 10 open
  conjectures, 2 retired rows, and 18 dead attempts on the algorithmic route to NEXP ⊄ THR∘THR.
- The fleet's circuit lower bounds are now made in the meta program, and the clb seats build there (seat-clb-2 proved
  L-meta-663, refuted 656, and filed the guarded-sum rows 780, 781, 787 and the partial-function AND-count rows 775,
  777, 778, 783, 784 with about ninety small-graph rows between 793 and 898; seat-clb-1 filed the few-NOT conditionals
  L-meta-885, 890, 894, 899 and 900 and the small exact edge-function sizes from 743 on). The line has four strands: exact sizes of
  graph edge functions (the last-gate line), a ladder in the line-degree for point-line incidence, the line-ORs of
  projective planes computed with few NOT gates (the main line since the 15:00Z review), and partial-function AND
  counts (the domain of our held step L-meta-632).
- Section 5.1 proves on paper L-meta-738 (transposition at line-degree 1) and L-meta-647 (one-sided circuits for
  C4-free bipartite graphs need |E| + tau - 1 gates), from our normal form and first-AND centres together with the
  fleet's checked L-meta-663, 696 and 697. This settles the first rung of the line-degree ladder exactly, implies
  L-meta-720, and removes the only unchecked hypothesis of L-meta-739. Section 4.3 states the quantitative condition
  under which the NOT ladder could reach general circuits; the present recursion misses it.

## 1. The target and the chain as they stand, with what is checked

### 1.1 Definitions the statements use

`SIZE(s)` (Defs/CircuitLowerBounds.lean) is the class of languages decided at every length n by one circuit of AND,
OR and NOT gates of fan-in at most two with at most s(n) gates, every gate counted, inputs free, no uniformity.
`PEqualNP.Search.SAT` is the set of binary strings encoding a satisfiable CNF under `encodeCNF`: each literal is its
polarity bit followed by the binary digits of the variable, read in pairs of bits ([1, d] a digit, [0, 1] end of
literal, [0, 0] end of clause); malformed strings are outside SAT. `THRTHR(s)` is depth-two threshold circuits with at
most s(n) bottom gates and integer weights of any size.

### 1.2 The target

**L-clb-036** (in_work since 00:43Z, attempt by seat-clb-2; hard link of the plan): there is no s and c with
s(n)^100 <= c (n + 1)^101 for all n and SAT in SIZE(s). It replaced L-clb-035 (retired 00:33Z: with n^101 in place of
(n + 1)^101 the bound forced s(0) = 0, and no zero-gate circuit accepts the empty string, which is in SAT, so the row
was trivially true). The plan's reason for hardness: "No known method proves a circuit lower bound above linear size
for an explicit problem in NP." The plan records one attempt in flight and none dead; no clb event has occurred since
02:08Z. Article A-019 (03:12Z) records the parking: "the hunt for a circuit bound that outgrows every fixed multiple of
the input" was set aside when the main force moved to the last-gate problem. The program had been parked once before:
the attempt on L-clb-033 died on 22 November at 19:27Z "by strategy ruling (founder's steer) ... circuit lower bounds
parked".

### 1.3 The chain (plan.json) and its checked steps

The chain is two items: "Linear lower bounds for explicit functions by gate elimination, to be stated on our circuit
model" (no lemma id), then L-clb-036. The first item is realized by four checked lemmas, all on the encoding above.

| id | checked statement |
|---|---|
| L-meta-011 | a function depending on all n inputs needs n - 1 fan-in-two gates (textbook) |
| L-clb-037 (S1) | for q >= 2 every position of a string of length 6q can change membership in SAT (the red team found that the witness named in the description fails at one position; the checked proof does not use it) |
| L-clb-039 (S2) | for q >= 2 every AND/OR/NOT fan-in-two circuit deciding SAT at length 6q has at least 6q - 1 gates |
| L-clb-040 (S3) | there is no s with 100 s(n) <= 99 n + c for all n and SAT in SIZE(s) |
| L-clb-041 | for k >= 4 every such circuit deciding SAT at length 4k + 2 has at least 5k + 1 = (5n - 6)/4 gates: the k polarity bits of one k-literal clause are fixed one at a time, each removing two gates, and the remaining 3k + 2 positions still all matter |

The recorded `depends_on` fields are empty for these rows (PROOF_GRAPH.tsv); the S1 to S3 chain is stated in the text.
L-clb-041 is the first step beyond wire counting; its article (A-014) names the next move as richer families inside
SAT "where more bits can be pinned at a higher price each", each worth a constant, and says that passing constants is
the open part.

### 1.4 The earlier sub-program: NEXP versus THR∘THR (22 November, 13:05Z to 19:27Z)

The first non-textbook target was **L-clb-013** (open): some NEXP language has no polynomial-size THR∘THR circuits,
reached by Williams' method: **L-clb-015** (open; SAT for polynomial-size THR∘THR in time 2^n / g(n) + K, g
superpolynomial), **L-clb-024** (open; additive 2^n / r approximate counting in the same time), **L-clb-028** (open,
"the hard link of M-clb-2-02": error 2^n / p(n) for bottom weights of total size p(n) and top weights in {-1, 0, 1}),
and the transfer **L-clb-022** (open; Chen and Williams, CCC 2019, Theorem 8 and Corollary 10, unformalized, "that the
recorded form of the hypothesis matches the paper's exactly is unverified"). Its checked known edge:

| id | checked statement |
|---|---|
| L-clb-014 | parity is in THRTHR(n) (gate j tests "at least j inputs", alternating top signs) |
| L-clb-016 | Lindsey: (sum over A x B of (-1)^<x,y>)^2 <= |A| |B| 2^n |
| L-clb-018 | some language is not in THRTHR(poly) (counting, Chow parameters) |
| L-clb-019 | a threshold of gates [a_j(x) + b_j(y) >= t_j] with each a_j taking at most V values computing inner product mod 2 has 2^n <= (2 C (V + 1))^2, C the sum of absolute top weights |
| L-clb-020 | one threshold gate of any weights has correlation at most (n + 1) 2^(3n/2) with inner product |
| L-clb-021 | the same with arbitrary bottom gates: 2^n <= (2 C (n + 2))^2; inner product has no polynomial-size MAJ∘THR |
| L-clb-023 | any top weights, bottom a_j with at most V values: 2^n <= (m V + 1)^2 (Forster's sign-rank bound) |
| L-clb-025 | every threshold gate on s inputs has integer weights of total size at most (s + 2)^(s + 2) |
| L-clb-026 | if inner product is in THRTHR(s) then 2^n <= (2 (k + 2)^(k + 2) (n + 2))^2 with k = s(2n), so k log k >= about n/2 |
| L-clb-027 | THRTHR(s) circuits have encodings of length at most 100 (n + s(n) + 3)^4 |
| L-clb-017, 029, 030 | encodeThr is injective; THRTHR is closed under complement with the same gate count; XOR of two THRTHR circuits is THRTHR of size c (s1 + s2 + n + 1)^c |

ACC0 and TC0 rows: **L-clb-009** (NEXP ⊄ ACC0, Williams 2014) and **L-clb-010** (NQP ⊄ ACC0, Murray and Williams
2018) are known theorems recorded as conjectures (not formalized); **L-clb-011** (NEXP ⊄ TC0) is open; **L-clb-033**
(Beigel and Tarui modulus amplification, degree 2k - 1) was stopped mid-proof by the strategy ruling. The textbook layer
is checked: L-clb-001 to 008 (SIZE monotone, AC0 ⊆ ACC0, unary languages in P/poly, (n + 2) 2^n upper bound, a
language outside P/poly, P ⊆ P/poly, parity ∉ AC0, MOD q ∉ AC0[p]), L-clb-012 (MAJORITY ∈ TC0), L-clb-031
(non-vacuity of the AC0 model) and L-clb-032 (Smolensky's average case: AC0[p] agrees with parity on at most a
1/2 + o(1) fraction, p odd). L-clb-034 (a sanity row on the fan-in cap of SizeDepth) is open.

## 2. What is open and live

### 2.1 In clb

Open rows: L-clb-036 (hard link, nominally in work), and the conjectures L-clb-009, 010, 011, 013, 015, 022, 024, 028,
033, 034. Nothing has been proposed in clb since L-clb-041 (01:43Z) and no attempt has run on the THR∘THR rows since
22 November 18:15Z. The program's seats are seat-clb-1, seat-clb-2, seat-lib-1 and seat-redteam-1.

### 2.2 Where the circuit work is live: the meta program

(a) **Exact sizes of edge functions f_G = OR over edges uv of (x_u AND x_v)** (the last-gate line, main force from
about 03:00Z). Checked: L-meta-105 and 154 (upper bound |E| + |T| - 1 for every vertex cover T, monotone), 104
(forests, all circuits, lower bound |E| + tau - 1), 115 and 113 (long threads: monotone bound, and NOT gates never
help), 204, 521, 532 (graph classes with long threads, six-runs, peelable: |A| + |E| + tau - 1 for AND/OR/NOT
circuits), 616 (cubic C4-free: monotone circuits need n + tau), 613 (flat monotone circuits: |E| + k - 1, k the number
of AND-gate centres), 531 (monotone formulas on graphs without C3, C4: |E| + |T| leaves), 598, 599, 601 (OR-gate
counts), 718, 719 (prism and five-spoke wheel: at least 9), 444 (checked 14:01Z: a polynomial-time map sends strings
outside SAT to minimal circuits and strings in SAT to circuits exactly one gate above minimum) and 126 (the last-gate
promise problem is not in AC0[p]). Open: 602, 606, 608, 612 (monotone circuits on C4-free graphs or girth >= 5 need
|E| + tau - 1 gates, or Omega(|E|)), 651, 670, 737 (Petersen with NOT gates), 722, 723, 724, 740, 742, 744, and 687
(the last-gate promise problem is in P iff P = NP), which is a composition of the checked 444 with the checked 481
or 665.

(b) **The line-degree ladder** for point-line incidence F(x, y) = OR over incident (p, w) of x_p AND y_w (lines marked;
an AND adds degrees, an OR takes the maximum; Defs/LineDegree.lean). Checked: L-meta-629 (test lemma), 645 (honest
factor), and **649** (15:07Z): at line-degree at most 2, if no two points lie on two common lines, the number of
incident pairs is at most 48 (gates) + 2N. Checked counting tools: **663** (proved by seat-clb-2: each line w needs
|w| - 1 low-merge OR gates), **696** (incident pairs <= low-merge pairs (gate, line) + number of lines), **697** (a
wire ignoring the line inputs is a low merge at one line at most, when no two points share two lines). Open at
line-degree 1: **647**, **720**, **738**, **739**. At line-degree 3 a conjecture ("a gate marked with a line serves few
points of that line") was eliminated at 13:54Z.

(c) **Line-ORs of projective planes with few NOT gates** (named the main line at the 15:00Z review, article A-040).
Checked: 529 (known: sets meeting pairwise in at most one point need sum (|S_w| - 1) AND/OR gates), 270 (the same on
inputs of weight at most k: sum min(k, |S_i| - 1)), 640 (the seven lines of the Fano plane: joint size exactly 14 with
NOT gates allowed), 666, 667 (planes of order 2 and 3 on light inputs: 14 and 39), 669 (constant propagation), the
NOT-gate surgery 673, 675, 677, 678, 679, 709, the combinatorics 680, 686, 713, the restriction 735, and **745**
(16:18Z, conditional on 270 and 669): with m sets of d inputs pairwise meeting in at most one point, any b inputs
meeting at most kappa(b) sets, a list of AND, OR, NOT gates of fan-in two with at most s NOT gates, right on the window
above a base y of at most b inputs with at most K further true inputs, has at least G(s, b, K) gates, where
G(0, b, K) = (m - kappa b) min(K, d - 1) and G(s + 1, b, K) = max over j <= K of min(G(s, b + j, K - j), G(s, b, j)).
Open: **766** (the unconditional form of 745: a composition of three checked rows awaiting its closing file), 660,
661 (one NOT gate, orders 8 and 7: at least 98 and 70), 710, 711, 712 (conditional on the set-OR bound and constant
propagation, both now checked: order 8 with one NOT at least 292, with two at least 112), 714, 715 (one NOT gate,
conditional on 529, checked), 885 with 890, 894, 899, 900 (NOT gates reading monotone wires: order 8 with two or
three NOT gates at least 144 and 80, order 9 at least 189 and 108), the guarded sums 780, 781, 787 (outputs written
A_i OR (B_i AND NOT H_i)), 782 (promise bound when an output accepts only part of its set), the window tools 749, 750,
751, the single-index machinery 689 to 695 and 699, and 736.

(d) **Partial-function AND counts** (a well-formed AND-count circuit false at every maximal independent set I and true
at I + u). Open: **632** (held by KokunoYumeto; least size = tau on C4-free graphs), 631, 633. Checked: 634, 635
(Heawood 7, Petersen 6), 704 (star circuit of a cover), 705, and 725, 727, 728, 729, 730, 732, 733, 734 (checked
16:16Z to 16:28Z on outside runners; cover and kernel combinatorics). New since 16:21Z, all by seat-clb-2: 775, 777
(additivity over tight parts), 778 (one AND gate iff the edges form one complete bipartite graph), 783, 784 (a cover of
the edges by k complete bipartite subgraphs gives k AND gates) and about ninety small-graph rows 793 to 898.

KokunoYumeto holds L-meta-632, 608 and 606 (and L-gct-086); the desk withdrew 655 (15:41Z, replaced by the
lower-bound form 720) and 617.

### 2.3 The strategy seat's latest lines (head.json)

13:54Z: "ELIMINATED ... the conjecture that a gate marked with a line serves few points of that line, for circuits of
AND and OR gates at line-degree three. WHERE THE ANSWER CAN STILL BE: a ladder by the number of NOT gates ... joint size
above linear for the line functions of a plane at each fixed number of NOT gates". 16:11Z: L-meta-669 checked; circuits
with at most 8 gates for the prism and the wheel eliminated by script. 16:27Z: L-meta-745 checked; "WHERE WE LOOK
NEXT: its form without hypotheses ...; circuits right only on heavy inputs of a plane, a conjecture on paper."

## 3. Dead approaches, with their reasons

**Program level.** Parked on 22 November at 19:27Z ("a textbook rung no attack line needs this week") and again at
about 03:00Z on 23 November (the superlinear hunt set aside for the last-gate problem; A-014: every property the agents
invented during the night to prove L-clb-036 failed). The midnight review (A-010) declared the derandomization route
dead and reassigned its agent.

**L-clb-015** (three candidates dead): "a 1/(pi sqrt n) fraction of majority-type gates truly vary at a point even with
one live variable, so s >= c m / sqrt n; gain is only L^(1/4) in degree; bound stays n^2.5".

**L-clb-024** (seven attempts dead): regularity needs independent inputs, but more than 2n + 2 balanced threshold gates
are never pairwise uncorrelated and MAJ of gates has critical index 0; a PRG loop only shrinks the exponent, and
nondeterministic guessing needs the same SAT or CAPP to verify; a low-rank approximant always exists (rank 1), so only
deterministic construction matters, and the only constructive source is gate-output polynomials; one route yields only
a conjectured sharpening of the known n^2.5 bound to n^2.5 / log^16 n; another works only with a margin gamma at the
top gate (degree about 1 / (eps^2 gamma^4)), and the transfer produces heavy cancellation; the preprint fooling k-of-m
thresholds of halfspaces is nontrivial only within about n^(1/6) of AND or OR, so majority top gates stay open; random
restrictions keep m sqrt(p) gates on pn variables, best at p = 1, and the Littlewood-Offord bound is tight on majority
gates.

**L-clb-028** (eight attempts dead): moments E[S^k] cost (mnW)^k, so k < n / log n, while a fixed polynomial needs
degree about m at a central threshold, and probabilistic polynomials stop near m = n^2; savings for all polynomial m
are known only with AND on top, approximate-counting reductions are randomized, and MA batch evaluation needs 2^n to
verify; known seeds are linear in the number of halfspaces, and parity is MAJ∘MAJ with O(n) gates, so small bias and
bounded independence fail past m near n; each boosting step needs a rectangle correlated with the residual, which is
the same estimation problem, and Frieze-Kannan needs all N^2 entries; the sound method is accurate only with a margin
at the top gate, while the transfer's instances are exact-threshold atoms with all mass at the threshold; all methods
stall at error about sqrt(log(mW) / n) on Gaussian-central instances; dual-BCH parities match A independent bits on
all affordable moments yet acceptance differs by about 0.4 / sqrt(A); the atom problem contains the AND of m arbitrary
halfspaces, characters over F_p reach only p < n / log n while the reduction needs p above m^2, and tensor rank is full
at m = n/2. (All recorded as unchecked analyses.)

**L-clb-033** stopped by the strategy ruling. **L-clb-035** retired (trivially true, see 1.2); **L-clb-038** retired
(duplicate of 039).

**On the meta circuit line.** Refuted by the checker: L-meta-624 (AND gates plus OR gates true at two single-vertex
inputs >= |E| on C4-free graphs; the 6-cycle with leaves at alternate vertices has 9 edges and a circuit with 6 AND and
2 such OR gates, L-meta-668), L-meta-662 (AND + wide OR + 2 narrow OR >= |E| + 2 tau - 2; the net gives 9 < 10,
L-meta-721), L-meta-656 (a passenger formula for short threads; broken by a 4-cycle). Eliminated on paper or by
script: the line-degree-3 conjecture of 13:54Z; circuits with at most 8 gates for the prism and the wheel (then checked
as 718, 719); the additivity of least size over two independent parts (A-015: negations can be shared). Structural
facts that close doors: the 4-cycle needs only 3 gates where the count gives 5 (L-meta-112), so every count needs
C4-freeness; an unrestricted monotone circuit can have fewer OR gates than |E| - 1 (Petersen: 13 OR gates, L-meta-584),
so OR counting alone fails outside restricted classes.

## 4. Where the line is heading: what the latest checked lemmas make possible

4.1 **clb proper.** Nothing is scheduled. L-clb-036 has no route, and the THR∘THR algorithmic links carry eighteen
dead attempts. The open rows with proofs in the literature are L-clb-009 and 010 (Williams; Murray and Williams), 022
(Chen and Williams) and 033 (Beigel and Tarui); formalizing them is long (Williams' method needs the ACC0 normal form,
whose first step is 033, and a fast ACC0-SAT algorithm; the transfer needs PCPs of proximity), and none of them bears
on 036.

4.2 **Line-degree ladder.** The checked 663, 696 and 697 are the counting half of line-degree 1; the transposition
L-meta-738 is the other half, and L-meta-739 needs only 738 and the checked 270. Section 5.1 supplies 738 and the
exact form 647. Line-degree 2 is checked with constant 1/48 (649); line-degree 3 is open, with one conjecture
eliminated and "a variant of a checked count where an output accepts part of its set" (782) as the next tool. The top
of this ladder is 606/608/612 (all monotone circuits); for a projective plane of order q (n = 2N inputs,
N = q^2 + q + 1, |E| = N(q + 1), tau = N) it is a monotone bound of order n^(3/2). With NOT gates the single-output
question is a superlinear general lower bound for an explicit quadratic function, and nothing on the map approaches it.

4.3 **NOT ladder for the line-ORs of planes.** Since 270 and 669 are checked, 745 gives an unconditional recursion once
766 closes; 714 and 715 are conditional only on the checked 529; 710 to 712 only on facts now checked. The numbers for
the plane of order 8 (73 points, monotone value 73 x 8 = 584): one NOT gate 292 (711), two NOT gates 112 (712) or 144
when every NOT gate reads a monotone wire (890), three such NOT gates 80 (894); order 9 (monotone 819): 189 and 108
(899, 900). So at T NOT gates the bound is about c_T m q with c_1 = 1/2, c_2 about 1/4, c_3 about 1/7: superlinear for
each fixed T, with a loss factor near 1/2 per NOT gate. This matters because T = ceil(log2(n + 1)) NOT gates is the
general case: an inverter with that many NOT gates and O(n log n) gates (Beals, Nishino and Tanaka, SIAM J. Comput.
27, 1998; cited from memory, not re-read here) turns any circuit of size S into one with ceil(log2(n + 1)) NOT gates and
at most 2S + O(n log n) gates. A ladder bound c_T m q with c_T = lambda^T is, at T = log2 n, of order
n^(3/2 + log2 lambda); it exceeds n log n, and hence gives a superlinear general bound for the line-ORs, exactly when
lambda > 2^(-1/2), about 0.707. The present recursion has lambda about 1/2, which gives n^(1/2) at that point.
Two further gaps: the monotone-reads rows 885 to 900 exclude nested NOT gates, which every inverter uses; and the
window method (749, 750) needs a base y of size up to K times the number of NOT gates, while for a plane a base of b
points already removes about bq of the q^2 + q + 1 lines, which is the same trade-off in another form.

4.4 **Partial-function AND counts.** 784 (upper bound by a biclique cover of the edges) and 778 (one AND gate exactly
for a single biclique) point to the general statement "least AND count = biclique cover number", whose C4-free case is
632 (on C4-free graphs every biclique is a star, so the biclique cover number is tau). The ninety small-graph rows
793 to 898 are the fleet's test bed for it.

4.5 **The last-gate line.** With 444 checked, 687 is a composition with 481 or 665. The exact counts remain linear in
the number of inputs, as the fleet's own articles state.

## 5. Where our mathematics attacks it

### 5.1 L-meta-738 and L-meta-647, proved on paper

Setting. G is bipartite with sides X (marked, the lines) and Y (the points), with no 4-cycle and no isolated vertex.
C is a circuit of AND and OR gates of fan-in at most two computing f_G, in which no AND gate reads two X-dependent
wires (dependence syntactic). When every gate reaches the output this is exactly line-degree at most 1 with X marked:
degrees only grow along a path, and an AND of two degree-1 wires has degree 2. C is normalized as in item 0 of
`L_meta_647_PARTIAL_PROOF.md` (deleting dead gates, copies, repeated reads and constant wires never increases the size
and keeps the class).

Step 1 (normal form; items 1 to 3 of `L_meta_647_PARTIAL_PROOF.md`). Let D be the set of X-dependent wires. Wires
outside D compute monotone functions of Y. By induction over the gates, every w in D computes
F_w = OR_{v in X} (z_v AND alpha_{w,v}) OR beta_w with alpha, beta monotone in Y. For f_G no OR gate reads a D-wire and
a non-D wire: otherwise the output is 1 at the input with X all 0 and Y all 1, where f_G is 0 (after normalization
every Y-wire is non-constant and monotone, hence 1 there, and every gate on a path from that OR gate to the output is
an OR reading a D-wire or a multiplying AND, whose multiplier is 1 there, so each keeps the value 1 at this input). So the gates are P
Y-gates (P_and AND, P_or OR), M merges (OR of two D-wires) and K multiplying ANDs (a D-wire and a Y-wire m_g, the
multiplier), and alpha_{o,v} = OR over D-paths pi from z_v to the output o of Pi(pi), the AND of the multipliers on pi.
Since f_G is 0 at a single vertex, every such path carries a multiplier, and alpha_{o,v} = OR_{u in N(v)} z_u.

Step 2 (transposition; this is L-meta-738). For a D-wire w put T_w = OR over D-paths from w to o of the AND of the
multipliers on the path. Then T_o = 1, and for w != o, T_w is the OR over the D-gates g reading w of T_g (g a merge) or
of m_g AND T_g (g a multiplying AND), and T_{z_v} = alpha_{o,v}. Computing all T_w over the points, in reverse
topological order, costs the P Y-gates, at most K ANDs, and r_w - 1 ORs for each D-wire w != o read by r_w gates (fewer
after constants are simplified). The D-wires other than o are |X| + M + K - 1 in number and receive 2M + K reads, each
at least one (normalization), so the combining ORs number
  sum (r_w - 1) = 2M + K - (|X| + M + K - 1) = M - |X| + 1,
which is the excess e_D of the reads identity of `L_meta_647_PARTIAL_PROOF.md` item 5. Hence a point-only circuit D'
with at most P + K + M - |X| + 1 <= |C| - |X| + 1 gates, of which at most P_or + M - |X| + 1 are OR gates, computes
every coefficient alpha_{o,v}. For a general line-degree-1 circuit (L-meta-738's setting) the same count holds with
R OR gates reading a D-wire and a point wire (they add to beta and act as one-read merges in the recursion) and with
copy gates: the combining ORs number M_2 - N' + 1, M_2 the ORs reading two D-wires and N' the lines reaching the
output, so size(D') + N' <= size(C) + 1, and C(x, y) = C(x, no line) OR (some line w on with w in T or D'_w(x)),
T the lines with an AND-free path to the output. This is the transposition principle for circuits linear in the
lines, over the semiring of monotone functions of the points.

Step 3 (OR gates of a Boolean-sums circuit; a corollary of the checked 696 and 697). Claim: if S_1, ..., S_m pairwise
share at most one element, every AND/OR circuit of fan-in two with an output wire for each OR(S_i) has at least
sum (|S_i| - 1) OR gates, however many AND gates it has. Proof: from such a circuit D' build
F' = OR_i (y_i AND D'_i), a circuit for the incidence function of the lines S_i. By 696, the incident pairs (sum |S_i|)
are at most the low-merge pairs (gate, line) plus m. An OR gate of the final OR-tree is never a low merge: at line i
every term y_j AND D'_j with j != i is 0, so one operand has an empty alive set. The AND gates are not OR gates. Every
OR gate of D' ignores the line inputs, so by 697 it is a low merge at one line at most. Hence the OR gates of D' number
at least sum (|S_i| - 1). This strengthens the checked 529, which counts all gates.

Step 4 (centres; item 4 of `L_meta_647_PARTIAL_PROOF.md`). For each edge vu there is a D-path from z_v with u in the
set L(Pi) = {u : Pi(e_u) = 1}; its first multiplying AND g has v in Src(g), the sources with an AND-free path to g's
D-operand. Every v' in Src(g) shares that rest of the path, so L(Pi) lies in N(v') for all of them; hence vu lies in the
complete bipartite subgraph Src(g) x CN(g), CN(g) the common neighbourhood of Src(g). So the first ANDs index a cover
of E by bicliques, and K >= bc(G), the biclique cover number, for every bipartite G. Without a 4-cycle a biclique is a
star, bc(G) = tau(G), and K >= tau.

Conclusion. Step 2 gives D' with at most P_or + M - |X| + 1 OR gates computing the sums OR_{N(v)} z_u, v in X, which
pairwise share at most one point; Step 3 gives P_or + M - |X| + 1 >= |E| - |X|, that is P_or + M >= |E| - 1. With
Step 4, |C| = P_and + P_or + M + K >= |E| + tau - 1. This is L-meta-647, and the star circuit of a least cover
(L-meta-154) lies in the class and attains it, so the value is exact.

Consequences. (i) L-meta-720: the once-subdivided K4 (12 edges, tau = 4) needs 15 gates in the one-sided class, for
either side; this also answers the withdrawn search 655. (ii) The hypotheses of L-meta-739 become the checked 270 and
the 738 proved here. (iii) For a projective plane of order q, line-degree-1 circuits for incidence need exactly
N(q + 2) - 1 gates (|E| = N(q + 1), tau = N by regularity and König), of order n^(3/2) in the n = 2N inputs: the first
rung of the ladder, exact, against the constant 1/48 checked at line-degree 2. (iv) In the one-sided class the OR gates
alone number at least |E| - 1, which L-meta-584 shows can fail for unrestricted monotone circuits (on the
non-bipartite Petersen graph).

Limits. At line-degree 2 an AND of two D-wires a, b puts the product alpha_{a,v} AND alpha_{b,v} of two point functions
into the coefficient of line v, and cross terms z_v z_v' alpha_{a,v} alpha_{b,v'}; the recursion of Step 2 is then no
longer linear in the coefficients and the gate count fails. With a 4-cycle Step 4 survives (as K >= bc(G)) but Step 3
does not (K_{2,2} is computed by (x_1 OR x_2) AND (y_1 OR y_2) with 3 gates).

These steps are not held by the KokunoYumeto handle; the desk accepts proofs only of steps it hands out (our PR for
L-gct-122 was closed unchecked). Asking the desk for 738 and 647 (or 720) is the user's decision.

### 5.2 The NOT ladder

Step 3 gives an OR-only version of 529, which the window and guarded-sum rows (781, 782, 787) could use: on each
monotone region of a circuit with NOT gates (673 to 679) the OR gates alone carry the bound. It does not by itself
improve the min-max of 745, because an OR gate inside the forward cone of a NOT gate computes different functions in
the two regions and may serve different lines in each; only gates outside that cone keep a single role. The quantity to
improve is the per-NOT loss factor lambda of 4.3, which must exceed 2^(-1/2) for the ladder to reach general circuits.
None of our results supplies that; it is the precise open question on this line.

### 5.3 L-meta-606 and 608 (held)

The open regime is now narrow and explicit: 5.1 settles bipartite C4-free graphs in the line-degree-1 class (girth >= 6
there, so it is a special case of 608); the cut-and-substitute bound of the Codex note
`desk/CODEX_TO_CLAUDE_L_META_606.md` (Codex at reasoning effort ultra, the standing setting for Codex runs) gives
|E| <= |A| R <= |A| (s + 1 - k), so 606 holds for circuits with boundedly many distinct shared-gate patterns on edge
inputs; 649 gives the constant 1/48 at line-degree 2 for incidence structures. What remains is circuits of line-degree
at least 2 with unboundedly many shared-gate patterns on edges, and non-bipartite graphs.

### 5.4 L-meta-632 (held)

Our partial results (`L_meta_647_PARTIAL_PROOF.md`, section on 632): the star circuit gives the upper bound; output
gates reading only bare vertices are stars; for an edge uv the first gate flipping between I and I + u (I a maximal
independent set containing v) has a side holding u. The open part is a centre assignment for gates reading gates. Step 4
of 5.1 suggests the invariant: assign to each such first flipping gate a biclique containing uv, so that the gates
cover E by bicliques and the count is at least bc(G) = tau. The fleet's 784 and 778 fit this form, and its small-graph
rows 793 to 898 can test it. `L_META_632_RESULTS.md` was not present when this map was written.

### 5.5 What our results do not move, and why

- **L-clb-013, 015, 022, 024, 028 (THR∘THR).** Our rank-type tools (GCT_GINEQ F-13 image substitution, the BR_PENCIL
  substitution and degeneration P-01 to P-09, Kneser for codes and Lemma K) bound ranks and dimensions. The THR∘THR
  frontier is a sign-rank question: a bottom gate [a(x) + b(y) >= t] with exponential weights is a staircase matrix of
  rank up to 2^n and sign-rank 2, so rank arguments stop exactly where L-clb-023's parameter V becomes exponential, and
  the regimes rank and discrepancy reach are already checked (L-clb-021, 023, 026). Our derandomization material
  (CUE_GCT isolation I-01 to I-44, the AGHP character points P-02, Kronecker weights P-07) consists of hitting sets for
  sparse polynomials and read-once oblivious ABPs, whereas CAPP for MAJ∘MAJ must fool majorities of polynomially many
  halfspaces, the regime where the dead routes on L-clb-028 record that small bias and bounded independence fail past
  m near n; our P-09 and P-10 (weighted samplers need about (delta + 1)^n points) is the same barrier as the dead
  L2-sampler routes (`MAPPING_AGENT_RESULTS.md`, section 5). The bridge in `fleet_map/chatgpt_algorithms.md`, section 2
  (ChatGPT, through Codex at reasoning effort ultra), gives 2^(o(n)) counting only for THR∘THR circuits that compile to
  o(n sqrt(log n)) bounded fan-in gates, far below the polynomial sizes of L-clb-015.
- **L-clb-036.** No result of ours gives a superlinear lower bound for an explicit function in general circuits; 5.1 is
  superlinear only at line-degree 1 (monotone, restricted). Our Hexagon NEG row (the parity of #SAT as a Hasse-Witt
  scalar) concerns counting parity, not circuit size.
- **L-clb-009, 010, 011, 033.** No contact: our material contains no ACC0 or TC0 lower-bound machinery.

### 5.6 Order of attack

1. L-meta-738 and 647 (with 720 and an unconditional 739): proofs ready on paper (5.1); a Lean route follows the
   transposition recursion and reuses the checked 663, 696, 697. Needs the desk to hand the steps.
2. L-meta-632 (held): the biclique form of the centre argument for gates reading gates, tested on 793 to 898.
3. L-meta-606 and 608 (held): line-degree 2 with an exact constant, by extending Step 2 to coefficients that are
   products of two point functions.
4. The NOT ladder: the per-NOT loss factor of 745's recursion, which decides whether the ladder can reach
   ceil(log2(n + 1)) NOT gates and so general circuits.

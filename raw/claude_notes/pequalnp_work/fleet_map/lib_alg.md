# Library (lib) and P = NP algorithm search (alg): what the fleet has, what is live, where we attack

By Claude Opus 5.5 at effort max (workflow pequalnp-fleet-map, agent a7b09d352d28f5997, effort set at launch by the
workflow script), 23 Nov 2026, about 16:20-16:50 UTC. Read-only: no desk requests, pull requests or posts.
Sources: export d63f7be336d2c36b (head.json generated 16:13:08 UTC; plan c0dd4cd68cdb, updated 00:40 UTC); all 209
lib and 6 alg lemma files fetched 16:20-16:25 UTC at 1 request a second; the alg feed, the library feed (page 11), the
seats file and the seat files of the alg, library and route seats; the repository clone (Defs/Search.lean,
SearchQ.lean, SearchQSyn.lean, SearchQTree.lean, SearchCP.lean, SearchRUP.lean, SearchSoS.lean, TimeAlt.lean,
LineDegree.lean, CoLevel.lean, Base.lean, Classes.lean; Search/Helpers/SemanticWeakening.lean; Library/L122.lean;
Search/L00xRefutation.lean); PROOF_GRAPH.tsv/json (17:28 local); L-meta-663 and L-meta-647 from the meta mapper's
downloads; our files named in section 5. L_META_632_RESULTS.md did not exist when this was written.
Running notes: `<local>/Documents\agent_notes\fleetmap_lib_alg_NOTES.md`.

## 0. Counts and the shape of the two programs

| program | checked | conjecture | refuted | retired | not faithful (among checked) | in work |
|---|---|---|---|---|---|---|
| lib (209 lemmas) | 186 | 9 | 1 (L-lib-082) | 13 | 4 (L-lib-035, 074, 075, 091) | 0 |
| alg (6 lemmas) | 0 | 2 (L-alg-001, 006) | 3 (L-alg-002, 003, 004) | 1 (L-alg-005) | - | 0 |

- The formal dependency graph has only three cross-program edges touching lib: L-pcx-010 uses L-lib-008 and L-lib-010;
  L-meta-037 uses L-lib-086. The plan's chains cite lib lemmas narratively (meta: L-lib-053, 092, 094-099; alg:
  L-lib-089-107) without depends_on edges.
- alg is parked: no alg event since 22:00 UTC on 22 Nov. seat-alg-1 now works for gct (L-gct-083, 091, 118-121; left
  the level-space line at 00:40 UTC) and meta (L-meta-153, 468, 668, 721 checked; L-meta-624 and 662 refuted at 15:04
  and 15:40 UTC today).
- lib's own target is checked; since 23:26 UTC on 22 Nov the library holds the helper requests of other programs and
  of private route seats, and since 08:00 UTC today seat-found-1 files sanity lemmas for the definitions of other
  programs, from about 12:40 UTC those of meta's current attack (line-degree, circuit moves, low merges, affine
  planes; the last, L-lib-209, at 15:09 UTC). Route seats under the library, with private subagents and no
  public milestones: rsat-1 (11 subagents), rlift-1 (8), ralg-1, rmag-1, rfrege-1 (2 each), rderand-1, revade-1,
  rvnp-1 (1 each), rmine-1 (0). The route requests visible in public are L-lib-119-121 (derandomization route) and
  L-lib-123-125 (evasion route); L-lib-127 names no requester.

## 1. Targets and chains as they stand

### 1.1 alg: "SAT in polynomial time; nearest result: a checked kill of each candidate algorithm"

**Target L-alg-001 (conjecture):** `PEqualNP.Search.SAT ∈ PEqualNP.Library.P`. SAT is the set of binary strings
`encodeCNF φ` of satisfiable CNFs (Defs/Search.lean: a literal is a polarity digit, the binary digits of its variable
index and an end pair; machines are Mathlib's FinTM2). With L-lib-031 this is P = NP. Method: a candidate algorithm is
identified with the proof system its unsatisfiable runs live in and killed by a superpolynomial lower bound there.

**The four candidates and their kills (all dead):**
1. Width-k resolution saturation (time n^O(k)). L-alg-002 ("some k: every unsatisfiable 3-CNF has a resolution
   refutation of width at most k") REFUTED by the checker (Search/L002Refutation.lean): Tseitin formulas on split grids
   of degree 3 need width above k for every k (a Duplicator strategy: deleting k+1 edges leaves a component of more than
   half the vertices).
2. Gaussian elimination plus width-k Res(lin) over F2. L-lib-109: a Res(+) refutation with lines of at most k equations
   gives a polynomial calculus refutation over F2 of degree max(2k+2, k+w); L-lib-110 (checked): for every k some
   unsatisfiable 3-CNF forces a Res(+) line with more than k equations (graph pigeonhole on an expander,
   L-pcx-043/046/048).
3. CDCL over parities (dag-like Res(lin) over F2). L-alg-003 ("polynomial-size Res(lin) refutations for every
   unsatisfiable 3-CNF") REFUTED by the checker from L-pcx-048 (dag-like Res(+) is superpolynomial on graph-pigeonhole
   3-CNFs on an expander; formalized on the fleet's definitions from claims of unrefereed 2026 preprints,
   arXiv:2610.00837 Thm 7.2(a), ECCC TR26-316 Thm 6.5) and L-pcx-018 (list Res(lin) to Res(+), at most two lines per
   line).
4. Stabbing planes with quasipolynomial coefficients: simulated by cutting planes (cited, CCC 2021); checked CP part on
   bit pigeonhole: L-lib-105 (triangle dags for the bit-PHP search problem are superpolynomial, Beame-Whitmeyer ICALP
   2025 Thm 1.7), L-lib-106 (a CP refutation gives a triangle dag with no more nodes, Sokolov/Hrubes-Pudlak),
   L-lib-107 (CP refutations of bit PHP are superpolynomial in lines), witness L-lib-108 (CP is complete).
- CDCL itself (RUP learning, Defs/SearchRUP.lean): L-lib-111 (a run that learns t clauses and the empty clause gives a
  resolution refutation of at most c t (v+1) lines), L-lib-112 (at most t (2v+1)^2), L-lib-114 (such runs exist). The
  kill L-lib-113 is open (section 2).

**Integer linear arithmetic, R(lin) over Z (Raz-Tzameret), checked so far:** L-lib-081 (sound). L-lib-089 (Sokolov
conversion: s lines, at most w equations per line, coefficients at most M in absolute value give a rectangle dag with
at most s (8 (2NM+1)^w)^3 nodes). L-lib-090 (rectangle dags for bit PHP are superpolynomial). L-lib-091 (restricted
bound for lines of at most 4l equations and coefficients at most 2^l; NOT FAITHFUL, vacuous by L-lib-102).
**L-lib-102**: for m >= 8 every R(lin)-over-Z refutation of bit PHP with 2^(8m)+1 pigeons has a line with more than
2^m equations (width n^(1/8); a Delayer walk with the Erdos-Littlewood-Offord inequality), witness L-lib-116.
**L-lib-103**: tree-like R(lin) over Z with semantic weakening needs superpolynomially many lines on bit PHP (Delayer;
the fleet withdrew its novelty remark), witness L-lib-104.

**Hard link.** L-alg-004 (dag-like R(lin) over Z with SEMANTIC weakening is superpolynomial on bit PHP) REFUTED by
seat-meth-1 (Search/L004Refutation.lean via Search/Helpers/SemanticWeakening.lean): semantic weakening derives in one
step the line "some two pigeons sit in the same hole" (one equation per triple (i, j, hole), `agreeEq` with
coefficients +1/-1), and each equation is cut against one clause with three lines per literal; size at most a
degree-9 polynomial in 2^l. Restated as L-alg-005 (retired: mis-cited Question 1 of Garg-Goos-Kamath-Sokolov 2018) and
then **L-alg-006 (conjecture, parked, "no route"):** the same bound for R(lin) over Z with SYNTACTIC rules
(Defs/SearchQSyn.lean: Boolean axioms v = 0 or v = 1, resolution by an integer combination of the first equations of
two lines, weakening only by adding equations, dropping equations 0 = c with c nonzero). The plan file still names
the retired L-alg-005 as the hard link.

Open seat milestones: M-alg-1-04 ("Direction 3: unbounded DAG Res(lin) ... must say how the search avoids the
automation hardness"), M-alg-1-07 ("superpolynomial dag-like Res(lin over Q) lower bound; hard link: compress wide
Q-linear clauses to low PC degree").

### 1.2 lib: "SAT is NP-complete on the project's own definitions" (checked)

**Target L-lib-031 (checked):** `NPComplete PEqualNP.Search.SAT` (Cook-Levin: the tableau CNF of a micro-instruction
run, built in polynomial time). Chain: L-lib-015 (a generic NP-complete language), L-lib-073 (DTIME(t) has fan-in-two
circuits of size c (t+n+1)^3), L-lib-029 (SAT in NP), L-lib-031, L-lib-032 (`NPComplete (KSAT 3)`), L-lib-019
(Ladner: P ≠ NP implies an NP language outside P that is not NP-hard). Hard link: none of its own.

Model caveats the red team proved and every statement must respect: L-lib-021 (every decider needs n <= d t(n) + 1
steps, so sublinear DTIME classes are empty), L-lib-117 (oracle machines escape that floor), L-lib-037 (no
polynomial-time function writes satisfying assignments indexed by variable number, since indices are binary; so
L-lib-033 was retired and L-lib-036 does search-to-decision for variables below the code length).

Checked groups:
- Classes and closure: 001-010, 016-018, 020, 039-047, 049, 050, 055, 057, 066-069, 084, 085, 100, 101.
- Hierarchies and padding: 011 (P is in no DTIME(n^k + k)), 012 and 051 (P strictly inside EXP), 014/052, 044/049,
  048/050, 053 (NP strictly inside NEXP, lazy diagonalization), 088 (time hierarchy with polynomial gap for
  constructible t, replacing 013), 083 (exponential clock for k >= 1; 082 refuted at k = 0), 092, 094-099 (padding
  machinery for L-meta-016).
- SAT: 022-030 (empty clause, every-clause-positive is satisfiable, resolution sound, splitting, encoding injective,
  pure literal, Erdos-Selfridge for k-CNF with fewer than 2^k clauses, SAT in NP, 2-SAT in P), 031, 032, 036, 038.
- Barriers: relativization 058-062, 071, 072 with non-vacuity 078, 080; algebrization 063-065, 070, 076, 077 with 079;
  natural proofs 086/087 (fan-in-two distinguishers, exponential security), after 035/074/075 were shown vacuous by
  093 (one unbounded-fan-in MOD 2 gate distinguishes every generator); machines to circuits 073; Hastad 034
  (correction: its depth counts NOT gates, so the exponent is 1/d; still parity outside AC0).
- Proof systems for alg: 054, 056, 081, 089, 090, 102-112, 114-116 (above). L-lib-115: a parity system with no
  width-d refutation by adding equations has no sum-of-squares refutation of half-degree D <= d/2 (Grigoriev,
  Schoenebeck; sign encoding).
- Service lemmas for other programs: 118 (a subspace on which a nondegenerate bilinear form vanishes has at most half
  the dimension; used inline by L-gct-101; outside proof, shohamc1, PR 5), 122 (section 2), 128, 130, 131 (outside
  proofs, sanchan: a recurrence; a rational polynomial matrix specializing to a permutation matrix has independent
  rows; seven threshold inequalities for a "three-way rank argument"), 117 (dm7672).
- Definition sanity, seat-found-1 (132-209): 2k-fold subdivisions 132-139 (edges multiply by 2k + 1, degrees kept), pebbling
  140-141, co-level 142-145, the AND-count star circuit 146, peelable graphs 147-151, nested cover circuits 152-154,
  literal partitions 155-160, minimum complexes 161-166, pendant bits 167-172, borrowed cover circuits 173-176,
  line-degree 177-181, circuit moves 186-190, low merges 191 and 196-199, affine plane 200-202 (each of the q^2+q lines
  has q points; two lines share at most one point; two points lie on exactly one line), new low merges 203, 204,
  207-209.

### 1.3 Proof map of the two programs (✓ checked, ✗ refuted, ○ open, r retired)

```
L-alg-001 ○ SAT ∈ P
 ├─ cand.1  L-alg-002 ✗ (Tseitin on split grids)
 ├─ cand.2  L-lib-110 ✓ ← L-lib-109 ✓, L-pcx-043/046/048 ✓
 ├─ cand.3  L-alg-003 ✗ ← L-pcx-048 ✓, L-pcx-018 ✓
 ├─ cand.4  L-lib-107 ✓ ← L-lib-105 ✓, L-lib-106 ✓ (witness L-lib-108 ✓)
 ├─ CDCL    L-lib-113 ○ ← L-lib-111 ✓, L-pcx-013 ✓, L-pcx-048 ✓   (pure composition, see 5.3)
 └─ hard link L-alg-004 ✗ → L-alg-005 r → L-alg-006 ○ (parked)
       restricted: L-lib-102 ✓ (width), L-lib-103 ✓ (tree-like); L-lib-091 ✓ but vacuous (← 089 ✓, 090 ✓)
       semantic system trivial: L-lib-126 ○ (route given, see 5.3)
L-lib-031 ✓ ← 015 ✓, 029 ✓, 073 ✓;  L-lib-032 ✓ ← 031, 020;  L-lib-019 ✓;  L-lib-036 ✓
evasion chain C5:  L-lib-122 ✓ (FP3 p q ∧ Coll u v → False when p u^3 < q v^3) ← L-lib-088 ✓
                   L-lib-123 ○ FP3 (hard link);  L-lib-124 ○, L-lib-125 ○ (helpers)
derandomization:   L-lib-119 ○, L-lib-120 ○, L-lib-121 ○
other requests:    L-lib-127 ○ (one level of Benes routing)
```

## 2. Open and live

| id | statement | state | requested by | our read |
|---|---|---|---|---|
| L-alg-001 | SAT ∈ P | goal | - | 5.4 |
| **L-alg-006** | every syntactic R(lin)-over-Z refutation of bit PHP (2^l+1 pigeons) has size above p(2^l), for every polynomial p | the only open hard link of alg; parked, no route; "open here, no proof and no short refutation known to this project" | seat-alg-1 | 5.5 |
| L-lib-113 | for every p some unsatisfiable 3-CNF forces every RUP run reaching the empty clause to learn more than p(n) clauses | stopped 19:26 UTC 22 Nov by a strategy ruling ("textbook rung under a kill nobody downstream uses") | seat-alg-1 | composition, 5.3 |
| L-lib-119 | every g from strings of length at most n-2 to strings of length n misses at least 2^(n-1)+1 strings | open, elementary | derandomization route (density of time-bounded incompressible strings) | proof 5.3 |
| L-lib-120 | DTIME(t) closed under complement at the same bound | open, elementary | derandomization route | proof 5.3 |
| L-lib-121 | after a prefix of a member, the first accepted b-bit suffix in `sections` order exists, has length b and is accepted | open, elementary | derandomization route (immunity argument) | proof 5.3 |
| **L-lib-123** | FP3: for some 1 <= p < q, DTIME(2^(qm)) up to constants is inside three-alternation time O(2^(pm)) (SigmaV 3, blocks of length exactly K 2^(pm) + K, linear-time check) | OPEN, "may be false", "fails relative to some oracles"; with checked L-lib-122 it gives NTIME(n) ⊄ DTIME(n^(u/v)) for some u/v > 1 | the evasion route (routes/evasion, named in L-lib-124/125) | 5.5 |
| L-lib-124 | p' < q gives, for every k, some i with 2k p'^i <= q^i | open, elementary | evasion chain task T5d | proof 5.3 |
| L-lib-125 | an exponential time translation q -> p' at every scale iterates to q^i -> p'^i | open, elementary | evasion chain task T5e | proof 5.3 |
| L-lib-126 | R(lin) over Z with SEMANTIC weakening refutes every unsatisfiable CNF in size c (n + m + k + 1)^c | open; route named by the methods seat: SemanticWeakening.short_refutation | seat-alg-1 (nominated by seat-meth-1) | proof 5.3 |
| L-lib-127 | every permutation of Fin n × Bool splits into a colouring b and two permutations π0, π1 of Fin n with (π(ρ, β)).1 = (β ≠ b ρ ? π1 : π0) ρ | open, elementary | not named | proof 5.3 |

## 3. Dead approaches and their reasons

- **Candidates 1-4 and CDCL** (section 1.1). The four died within 50 minutes on 22 Nov; 2 and 4 died first by citation
  (Alekhnovich-Razborov 2001; CP lower bounds of Pudlak 1997 and Fleming-Pankratov-Pitassi-Robere 2017), and were then
  turned into checked kills (L-lib-110, L-lib-107).
- **Nine routes to L-alg-004 (14:21-17:51 UTC, 22 Nov), with the fleet's reasons:** (1) full R(lin): CP bit-PHP proofs
  need one-inequality lines (triangles), a 2-equation line covers a band needing exponentially many triangles, and
  Res(2) inside R(lin) has no monotone interpolation; (2) narrow-line route: every refutation has a line of n^Ω(1)
  equations (L-lib-102), so the rectangle conversion costs 2^(n^Ω(1)); (3) Braun's F2 route dies over Z at step 1:
  false sets of integer lines are not flats (sum x_j = v/2 has a degree-v indicator); (4) no short refutation found:
  distinctness of the hole values val_i is cheap, counting needs degree-l occupancy or enumerating used-value sets;
  (5) fat lines OR_t (sum_i x_i0 = t) survive every restriction, and the walk ignores the hole count, so it would also
  bound weak bit PHP; (6) a width-bounded Delayer is vacuous (L-lib-102), an unbounded Alon-Furedi Delayer gives only
  2^Ω(l) = poly(n); (7) false: one injective form sum 2^k x_k refutes any unsatisfiable CNF with two classes per line;
  (8) false at M = 1: a sum over a set A at its maximum pins a bit of all of A, so prefix halving refutes bit PHP with
  O(log n) classes; (9) the Efremenko-Garlik-Itsykson closure needs Pr[σ falsifies L] = 2^(-rank), true over F2 only
  (rank-q nested sums over Z are all false with probability 1/2); line-determined closure gives only width. Then the
  statement itself fell (semantic weakening).
- **Library statements that failed or were vacuous:** L-lib-033 (as stated equivalent to SAT ∉ P, negated by
  L-lib-037); L-lib-035/074/075 (vacuous hypothesis, L-lib-093); L-lib-091 (vacuous, L-lib-102); L-lib-082 (false at
  k = 0); L-lib-013 (cubic gap model dependent, replaced by 088); filing failures 129, 182-185 (terms truncated at the
  first `:=`), 192-195 (sentence and term mispaired), 205-206 (checker rejected anonymous constructors).
- **Abandoned seat targets:** M-alg-1-05 (refute L-alg-003 as first non-textbook target: overtaken by the 2026
  preprints); M-meth-1-03 (exact F2 PC degree d against width w on about 700 CNFs up to n = 20: d - w is 0 or 1
  everywhere, no asymptotic kill reachable by small n).

## 4. Where the lines are heading

- **alg** is parked on L-alg-006 with two restricted results in hand (width, L-lib-102; tree-like, L-lib-103). What
  the checked lemmas make immediately possible: L-lib-113 (CDCL kill) and L-lib-126 (the semantic system is trivial,
  closing every dag size target on Defs/SearchQ.lean) are compositions of checked material. Any further dag-like
  progress must handle lines of at least n^(1/8) equations, since L-lib-102 forbids narrow refutations and L-lib-089
  converts only narrow ones. The kill method covers only algorithms whose runs yield refutations of the original clauses
  in resolution, Res(+)/Res(lin) over F2 or CP (5.4).
- **lib** has three live directions. (a) Definitional ground for meta's attack on incidence functions of planes: the
  affine-plane lemmas 200-202, low merges 191/196-199 and new low merges 203-209, line-degree 177-181, circuit moves
  186-190. They underpin L-meta-663 (checked 14:09 UTC: in every AND/OR fan-in-two circuit for an incidence function,
  each line w has at least |w| - 1 low merges at w) and the head status at 16:11 UTC ("circuits right only on heavy
  inputs of a plane; at line-degree three, a variant of a checked count where an output accepts part of its set").
  Expect sanity lemmas for each new meta definition (the NOT-gate ladder next). (b) The evasion chain: L-lib-122 is
  checked, helpers 124/125 are open, and the hard link FP3 (L-lib-123) decides whether the chain yields a superlinear
  bound NTIME(n) ⊄ DTIME(n^(u/v)). (c) The derandomization route asks 119-121; its main step is not public.
- **New definitions without program lemmas yet:** CoLevel.lean (L-lib-142-145). It generalizes the GCT level spaces
  (5.2), so a co-level statement on the permanent may be the next gct or meta node.

## 5. Where our mathematics attacks it

### 5.1 The library's newest definitions feed L-meta-647/663, and our partial proof plus their checked L-meta-663 give an exact reduction of L-meta-647

My derivation in this session, not yet checked by a second reader; it combines our proved items in
L_meta_647_PARTIAL_PROOF.md (0 normalization, 2 no mixed OR, 4 first-AND centres form a vertex cover, 5 reads identity)
with the fleet's checked L-meta-663, read with the roles of 663's "lines" played by the side X of L-meta-647.

*Setting.* After deleting gates outside the output cone (which never adds gates), L-meta-647's class is exactly
additive line-degree at most 1 in the sense of Defs/LineDegree.lean with X marked: a wire depends syntactically on X
iff its degree is at least 1, and an AND of two such wires (y AND y included) has degree at least 2. So L-meta-647 is
the line-degree-1 rung of the fleet's ladder, whose head status is now at line-degree 3. In a normalized circuit of
that class every gate is a Y-gate (P of them: both operands independent of X), a D-merge (M: OR of two X-dependent
wires) or a multiplying AND (K: one operand of each kind); no mixed OR (our item 2). For
u in X let lm(u) be the number of low merges at u in the sense of L-meta-663 (with u playing a line, N(u) its points),
split as lm(u) = lm_Y(u) + lm_D(u) by gate kind.

*Facts.* (i) L-meta-663 (checked, all monotone fan-in-two circuits): lm(u) >= deg(u) - 1, so sum_u lm(u) >= |E| - |X|.
(ii) A Y-gate OR is a low merge at no two distinct u, u' in X: its operands do not depend on X, so their alive sets lie
in N(u) ∩ N(u'), which has at most one vertex when G has no 4-cycle, and incomparable alive sets need two. Hence
P >= sum_u lm_Y(u). (iii) Our item 4: K >= τ. (iv) Our item 5 on the D side: M = e_D + |X| - 1, with e_D >= 0 the
excess reads of D wires. Adding,

  **|C| - (|E| + τ - 1) = (P - Σ_u lm_Y(u)) + (Σ_u lm(u) - |E| + |X|) + (K - τ) + (e_D - Σ_u lm_D(u)),**

and the first three brackets are nonnegative. So **L-meta-647 holds as soon as e_D + (K - τ) (+ the other slacks)
>= Σ_u lm_D(u)**: every low-merge incidence of a D-merge must be paid by an excess D read or an AND beyond τ. The
identity is tight in both orientations of the conjectured optimum for the affine plane AG(2, q) (|X| = q^2 + q lines,
|Y| = q^2 points, |E| = q^3 + q^2, τ = q^2 by Hall, conjectured |C| = q^3 + 2q^2 - 1, attained by the point-centred
star circuit, which has line-degree 1): with X = lines, P = 0, K = q^2, each line has q - 1 low merges, all D-merges in
the final OR tree, and e_D = (q^2 + q)(q - 1) = Σ lm_D exactly; with X = points, the q OR gates of each point's tree
over its q + 1 lines are its low merges, lm_Y = q = deg - 1, and e_D = 0 = Σ lm_D. A check on a wasteful 10-gate circuit for two disjoint 2-stars (OR(h AND m3, h AND m4) with
h = (z_u1 AND (y1 OR y2)) OR (z_u2 AND (y3 OR y4)), m3 = y1 OR y3, m4 = y2 OR y4) gives e_D = 1 < Σ lm_D = 2, paid by
K - τ = 2: the D-side inequality alone is false, the K - τ term is needed. This replaces the open "excess inequality" of
L_meta_647_PARTIAL_PROOF.md (excess reads on both sides against star memberships) by a statement about the D side
only, of the same Nechiporuk type; the Y side is carried by the checked L-meta-663 and fact (ii). Two small circuits the
fleet checked today (L-meta-668, 6-cycle with three leaves; L-meta-721, the net; both refute weighted variants,
L-meta-624 and 662, and were found by seat-alg-1) are the first test cases for the D-side inequality if they are
one-sided; I have not tested them.
The library lemmas behind it: 201 (no 4-cycle in the plane's incidence graph), 191/196-199/203-209 (the root
definitions of low wire, alive set, low merge and new low merge), 146 (the star circuit computes the edge function with
|T| AND gates in the AND-count model: the upper half of L-meta-632, which we hold). For the synthesis and the
647/608/632 agent: this is the most direct use of the library's newest work, and it touches items we hold at the desk
(L-meta-608, 606, 632 per MATCHES.md).

### 5.2 L-lib-118 and the co-level definition meet our level-space results (gct)

- L-lib-118 (checked: W ⊆ W^⊥ for a nondegenerate form gives 2 dim W <= dim V) is the isotropy step of every
  quadratic-layer bound of A3, and the fact behind it (dim W^⊥ = dim V - dim W) is step 3 of our Lemma K proof
  (MAPPING_BY_READING A1: U ⊕ St ⊆ U^⊥). With the O-011 eigenvalues (Hessian ∝ (J_p - I_p) ⊗ (J_q - I_q), eigenvalues
  -(q-1), -(p-1), +1 on V_p ⊗ 1, 1 ⊗ V_q, V_p ⊗ V_q, nondegenerate on {S_1 = 0}) each of our bounds dim L <=
  floor((pq - 1)/2) (rectangular, L-gct-179/181/187/195/196/215) and dim L <= floor((n - 1)^2/2) (doubly centred,
  L-gct-182/199) is one application of L-lib-118, so a Lean version needs only the eigenvalue computation.
- CoLevel.lean: a p-unit is ∏_r (1 + l_r(y)); the co-level of a multiset A is the least N of extra p-units making the
  sum the constant |A| + N. Since perm(J + t) = Σ_σ ∏_i (1 + t_{iσ(i)}), a linear space L of n x n matrices is a level
  space (L-gct-086) iff the multiset {∏_i (1 + t_{iσ(i)}) : σ ∈ S_n}, written in coordinates of L, has co-level 0. Our
  results in MAPPING_AGENT_RESULTS 1.1-1.5 are co-level-0 statements for this multiset: S_2 = p_2/2 and S_3 = (2/3) p_3
  on the doubly centred space, LS(n) <= n^2/3 + 2n, the root-of-unity block family F_q (S_k = 0 unless q | k) and its
  hyperpermanent self-similarity, the level families of dimension n - n/q and n - 2. If a co-level node is posted, these
  transfer directly; which program will use the definition is not yet public.

### 5.3 Live lib conjectures we can prove now (ready for a Lean sub-agent if the desk hands one to us)

- **L-lib-119.** The domain Σ_{l < n-1} {0,1}^l has 2^(n-1) - 1 elements, so the image has at most that many and at
  least 2^n - 2^(n-1) + 1 = 2^(n-1) + 1 strings of length n are missed (n = 1: empty domain, 2 >= 2).
- **L-lib-120.** Mathlib's `TM2ComputableAux` carries separate `inputAlphabet` and `outputAlphabet` equivalences.
  Keep the machine and compose `outputAlphabet` with Boolean negation: the same run, in the same number of steps,
  outputs [¬ f a]. (Read in .lake/packages/mathlib/Mathlib/Computability/TuringMachine/Computable.lean, lines 142-170.)
- **L-lib-121.** b <= |x| gives x = take(|x| - b) x ++ s0 with |s0| = b, and s0 occurs in
  `(List.replicate b [false, true]).sections` (all Boolean lists of length b); f accepts it, so `find?` returns some
  s, which is accepted and has length b.
- **L-lib-124.** k = 0 or p' = 0: i = 1. Otherwise i = 2kp': (p'+1)^i >= p'^i + i p'^(i-1) = p'^i (1 + 2k), and q^i
  >= (p'+1)^i.
- **L-lib-125.** Induction on i generalizing r: q^(i+1) r = q (q^i r) and the hypothesis at s = q^i r >= 1 gives
  D(2^(q^(i+1) r m)) ⊆ D(2^(p' q^i r m)) = D(2^(q^i (p' r) m)) ⊆ D(2^(p'^i p' r m)) by the induction hypothesis at
  r' = p' r >= 1.
- **L-lib-126.** Let E have one equation `agreeEq (vars C) t_C` for each non-tautological clause C of F, t_C the
  falsifying values. F unsatisfiable means every point falsifies a clause, which is non-tautological, so E covers the
  cube; each equation falsifies every literal of its clause; equation size at most 2n + 3 (coefficients ±1, right side
  at most n). `short_refutation` gives size at most (2 + m(3k+2))(1 + (k + 1 + 2m)(2n + 3)) <= 35 N^4 <= c N^c with
  N = n + m + k + 1 and c = 35. (An empty clause gives the equation 0 = 0 and the same argument.)
- **L-lib-127.** The bipartite multigraph with an edge ρ -> (π(ρ, β)).1 for each (ρ, β) is 2-regular on both sides
  (π is a bijection), so it splits into two perfect matchings (each component is an even cycle, a double edge
  included; or Hall's theorem, then the complement). Let b ρ be the β of the edge in the first matching, π0 ρ =
  (π(ρ, b ρ)).1, π1 ρ = (π(ρ, ¬ b ρ)).1.
- **L-lib-113.** For p, apply L-pcx-048 to p'(n) = c p(n) (n + 1); a RUP run with at most p(n) learned clauses gives by
  L-lib-111 a resolution refutation of at most p'(n) lines and by L-pcx-013 a Res(+) refutation of the same length,
  which L-pcx-048 forbids.
None of these needs our research results; they are worth holding ready because the desk does hand out such
"TRACTABLE" rows (L-lib-118, 128, 130, 131 were proved by outside contributors).

### 5.4 L-alg-001: what of ours fits the program's own format (candidate, then a family that kills it)

- **A finite kill for a new candidate class** (ChatGPT, fleet_map/chatgpt_sat.md; not re-verified by me): in the
  prime-label sparse encoding of 3-CNFs, at N = 7667 an unsatisfiable and a uniquely satisfiable 3-CNF give identical
  inputs at every label probe, while their global monic gcds differ (coefficient supports {0} and {2, 3, 8} at label
  11). So the claim "satisfiability is a function of the residues of the encoding at the prime labels" is refuted by one
  pair, the same shape as the refutation of L-alg-002, and checkable by finite computation. Only the fleet can post it
  as a candidate and kill.
- **Hardness transfers, not kills** (ChatGPT, chatgpt_algorithms.md and chatgpt_sat.md; our Hexagon NEG row as recorded
  in MAPPING_OUR_RESULTS_TO_PEQUALNP.md 1.5): SAT reduces in polynomial time to one digit of a root count of a planar
  construction at threshold one; one bit of the global gcd gives exact #SAT under deterministic Turing reductions; the
  parity of #SAT is a Hasse-Witt scalar of one sparse smooth cubic (⊕P-hard). A polynomial-time evaluator for any of
  these quantities proves L-alg-001 (with Valiant-Vazirani for the parity, NP ⊆ RP). They say which quantities would
  decide SAT, not that an algorithm fails.
- **The structural point for the program's method** (ChatGPT's "failure mode", which I checked against the statements
  of L-alg-003, L-pcx-018 and L-pcx-048): every checked kill concerns algorithms whose unsatisfiable runs yield
  refutations of the original clauses in resolution, Res(+)/Res(lin) over F2 or CP. Value-only evaluators (a gcd bit,
  a coefficient digit, a Hasse-Witt scalar, an exact model count) and algorithms whose certificates live on extended
  algebraic constraints are outside every system with a checked lower bound, so the program has no tool to kill them.
  Its plan sentence "Every known algorithm family has an exponential lower bound" holds only for proof-system-shaped
  algorithms. chatgpt_algorithms.md cites an OpenAI manuscript of 25 Oct 2026 (Theorem 1.1: exact #k-SAT for fixed k in
  time poly(n + m) 2^O(n log log n / sqrt(log n))), which I have not read; if correct, it is a subexponential family of
  this outside kind (its runs cannot convert to resolution refutations with polynomial overhead, since resolution needs
  2^Ω(n) on random 3-CNF), it does not touch L-alg-001, and it falsifies that plan sentence for counting algorithms.

### 5.5 What our results do not move, with the mathematical reason

- **L-alg-006.** A proof must control lines that are disjunctions of w >= n^(1/8) integer equations (L-lib-102), whose
  falsified sets {x in {0,1}^n : a_j·x ≠ b_j for all j} are not affine subspaces; the EGI closure needs
  Pr[falsified] = 2^(-rank), false over Z; the Sokolov conversion needs w = O(log n); and anticoncentration
  (Erdos-Littlewood-Offord, used in L-lib-102) bounds Pr[a·x = b] for one equation but does not multiply over the
  equations of a line (nested sums at thresholds). Our proved tools bound dimensions of linear spaces on which
  polynomial identities hold: Lemma K and the Fermat lemmas (power sums vanishing on W ⊆ C^M, through Kneser's theorem
  for codes), the O-011 Hessian decompositions, apolarity and border substitution. On the Boolean cube the Schur powers
  of the affine-function code are all multilinear polynomials of degree at most w, so Kneser's bound reproduces only the
  trivial count. None of them gives a probability or counting bound for intersections of complements of integer
  hyperplane slices of the cube, which is the missing ingredient; a short refutation (refuting L-alg-006) would need
  R(lin) to count hole occupancy, a degree-l function of the bits, and none of our constructions supplies linear
  counting forms for it. The same holds for M-alg-1-07 ("compress wide Q-linear clauses to low PC degree").
- **L-lib-123 (FP3).** It asks for a polynomial speedup of deterministic time by three alternations with exponentially
  long blocks and a linear-time check, for machines whose space is not bounded. The known speedups do not give it:
  DTIME(t) ⊆ Σ4 TIME(t / log* t) for multitape machines (Paul-Pippenger-Szemeredi-Trotter 1983), and the time-space
  speedup DTISP(t, s) ⊆ Σ2 TIME(O(sqrt(t s))) helps only when s is small; a diagonal refutation would need to simulate
  three exponential quantifier blocks within 2^(qm). Nothing of ours concerns alternation; L-lib-122 is the standard
  alternation-trading argument with FP3 as its missing speedup half.
- **L-lib-113, 119-121, 124-127**: elementary or compositions (5.3); no research result of ours is needed.

### 5.6 Ranked use of this map (for the synthesis)

1. 5.1: L-meta-647 reduced, with L-meta-663 (checked) and our items 2, 4, 5, to the D-side inequality
   e_D + (K - τ) + slacks >= Σ_u lm_D(u); hand it to the agent on 647/608/632 and the meta map. Highest value: it uses
   the fleet's newest checked count and the library's newest definitions, and it touches items we hold.
2. 5.2: L-lib-118 shortens the Lean form of our quadratic-layer level-space bounds; watch for a co-level node, to
   which our level-space results transfer.
3. 5.3: proofs of the nine open lib rows ready if the desk hands them out; no desk request from us.
4. 5.4: ChatGPT's label-probe pair is a candidate-and-kill row the fleet could post; the value-only point should go to
   the alg seat's plan sentence if we ever write to the fleet.
5. L-alg-006 and L-lib-123: no attack from our side now (5.5).

## Files

- Downloads (scratch, may be cleared): `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\672ae3a0-11a5-4e45-b4e2-c44a7908d05b\scratchpad\libalg_dl\lemma\` (215 lemma files), `...\libalg_dl\feed\`, `...\libalg_dl\seat\`.
- Repository: `<local>/pequalnp_work\pequalnp-proofs\lean\PEqualNP\Defs\Search*.lean`, `Defs\TimeAlt.lean`,
  `Defs\LineDegree.lean`, `Defs\CoLevel.lean`, `Search\Helpers\SemanticWeakening.lean`, `Library\L122.lean`.
- Ours: `<local>/pequalnp_work\L_meta_647_PARTIAL_PROOF.md`, `MAPPING_BY_READING_20261123.md`,
  `MAPPING_AGENT_RESULTS.md`, `MAPPING_OUR_RESULTS_TO_PEQUALNP.md`, `fleet_map\chatgpt_sat.md`,
  `fleet_map\chatgpt_algorithms.md`.

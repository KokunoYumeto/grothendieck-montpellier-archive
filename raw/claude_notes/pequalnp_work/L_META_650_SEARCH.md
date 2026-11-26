# L-meta-650: search record (23 Nov 2026, 16:57 - 18:0x UTC)

By Claude Opus 5.5 at effort max (agent a58224616ed89704f, session 672ae3a0), for the KokunoYumeto handle,
lease ac02c797. Task: a Monotone2 circuit (AND/OR, fan-in <= 2, every gate counted) with at most 63 gates computing
f_G for G = the point-line incidence graph of PG(2,3) exactly as listed in the statement (points 0-12, lines 13-25,
52 edges, tau = 13). |E| + tau - 1 = 64, so a witness would refute L-meta-608.

**Outcome: no witness found.** Proved exclusions: every single-level circuit (section 1a), and every circuit that
agrees with a star circuit outside a set of 2 points (section 2.1; all pairs by symmetry, all line pairs by
duality) [k = 3, 4: see section 2.1]. Heuristic search (annealing, 1903 restarts) reached circuits with one wrong
row at best. Released with reason out_of_time.

## 1. What any witness must look like (proved)

A circuit is normalized when every gate reads two distinct wires, no gate is constant or a copy, and every gate lies
on a path to the output; normalizing never increases the size.

(a) **Not single-level.** Every monotone single-level circuit (each input-output path through at most one AND gate)
computing f_G for a C4-free graph has at least |E| + tau - 1 gates (L_META_632_RESULTS.md, part 608, section A:
the AND gates are stars, their centres form a vertex cover, OR gates building leaf sums cannot be shared between
different centres, union-find count). For this G that is 64. So a witness has an AND gate that reads, through OR
gates, the output of another AND gate on a path to the output.

(b) **Excess reads.** For a normalized circuit with all 26 inputs relevant, 2|D| = (26 + |D| - 1) + e, where e is the
total excess fan-out (sum over non-output wires of fan-out - 1). So |D| = 25 + e. The star circuits have e = 39 (each
line, or each point, read four times); a 63-gate witness has e = 38.

(c) **Window restriction.** For any set P of points, setting every input outside H_P (P and the lines through P) to
0 turns any circuit for f_G into a circuit for f_{H_P} (every edge of G inside V(H_P) is an edge of H_P). So for
every P the gates that survive this restriction (not constant, not copies) number at least C(f_{H_P}). Exact values
found: C(f_{H_P}) = 9 for |P| = 2 (S = 8 UNSAT in 40 s, the double star on 9 vertices, = |E_H| + tau_H - 1).

(d) **Correctness check used throughout.** For a monotone circuit, being 1 on the 52 edges and 0 on the 704 maximal
independent sets is equivalent to computing f_G on all 2^26 inputs (an input with an edge contains a 1-row; an
independent input lies in a maximal one).

## 2. Searches

### 2.1 Window templates, reduced to the window (exact, CaDiCaL)

Template T(P), |P| = k points: a star circuit for the 13 - k points outside P (any OR-tree shapes: 5(13 - k) - 1
gates), a FREE part of 5k - 2 gates that may read ANY earlier wire (inputs, every gate of the star part, earlier free
gates), and a final OR: 63 gates. Reduction (1c): setting the inputs outside H_P to 0 kills the AND gates and the OR
tree of the star part, and each line sum of an outside point p' becomes the OR of its lines that lie in H_P (a
"helper"). Hence a T(P) witness yields a circuit of 5k - 2 gates computing f_{H_P} from the inputs of H_P and the
helpers. desk/l650/window_reduced.py asks CaDiCaL for that circuit, with ALL subsets (size >= 2) of each outside
point's H-lines as helpers, so every OR-tree shape of the star part is covered. UNSAT excludes T(P).
Symmetry: PGL(3,3) is 2-transitive on points and transitive on collinear triples, on triangles, and on each of the
three kinds of 4-sets (4 on a line, 3 on a line + 1, quadrangle); PG(2,3) is self-dual, so point windows also cover
line windows (templates built on line stars).

| k | P | H_P | helpers | free gates | result |
|---|---|---|---|---|---|
| 2 | {0,1} | 9 vertices, 8 edges (double star) | 9 | 8 | **UNSAT** (111 s; again 108 s) ; F = 9 SAT (sanity) |
| 3 | {0,1,3} collinear | 13 vertices, 12 edges (tree) | see log | 13 | [result] |
| 3 | {0,1,2} triangle | 12 vertices, 12 edges | see log | 13 | [result] |
| 4 | {0,1,2,5} quadrangle | 14 vertices, 16 edges | 27 | 18 | [result] |
| 4 | {0,1,3,2} 3 on a line + 1 | 15 vertices, 16 edges | 47 | 18 | [result] |
| 4 | {0,1,3,9} a full line | 17 vertices, 16 edges | 99 | 18 | [result] |

The unreduced template with all 756 rows (desk/l650/window_sat.py) gave SAT for k = 2, F = 9 (a 64-gate circuit, exact
check passed) and UNKNOWN for F = 8 (800 s) and for k = 3 (900 s): the reduction is what made the exclusions
decidable.

### 2.2 AND-count bounds (exact SAT on AND-count circuits, desk/l650/andcount_650.py)

Every Monotone2 circuit is an AND-count circuit whose OR gates realize the sides. Asked: 12 AND gates (any OR
structure); 13 AND gates with no OR gate shared between sides and total size <= 63. All four runs (including the two
sanity runs that should be SAT) ended UNKNOWN after 10-15 min under the machine load: no conclusion.

### 2.3 Simulated annealing over all 63-gate circuits (desk/l650/anneal.py)

Bit-parallel evaluation on the 756 rows; moves: change one input of a gate or flip its operation; Metropolis with
linear cooling; seeds: star circuits (points or lines, random centre order) with one gate deleted, or random
circuits; edge rows weighted 1, 2 or 4. 6 processes x 25 min (16:59 - 17:30 UTC), 1903 restarts of 200k-800k moves.
Best cost 1 in every process (one wrong row: a star circuit missing one edge, or equivalent), never 0.

### 2.4 Earlier small-graph evidence (L-meta-608 runs)

No girth >= 5 graph on <= 7 vertices beats |E| + tau - 1 (exact; one 7-vertex theta graph decided only to >= 10 of
11); 21 of the 47 connected girth >= 5 graphs on 8 vertices checked, all agree.

## 3. Assessment

A witness would be a circuit of a kind not known to exist for any graph without 4-cycles: by (1a) it must nest AND
gates, and by 2.1 the nesting cannot be confined to the stars of at most two points (or [k] points) while the rest is
a star circuit. In general circuits 608 is at least as hard as Jukna's open Problem 24 (ECCC TR05-021, section 8),
so a proof that no witness exists is not expected from a search; a witness, if any, would have to restructure many
stars at once.

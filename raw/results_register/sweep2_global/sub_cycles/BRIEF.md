# Sub-agent "cycles": the cycles of the dependency graph (brief, 18 Nov 2026)

You are Claude Opus 5.5 at effort max, sweep 2, sub-agent cycles. Read
`<local>/Documents\results_register\sweep2_global\COMMON_BRIEF_FOR_SUBAGENTS.md` first. Your folder:
`<local>/Documents\results_register\sweep2_global\sub_cycles\`.

## Why you

The "uses" graph (GRAPH_EDGES.tsv, kind = uses) has 63 strongly connected components of size ≥ 2, all inside single
runs: `tools/analysis_cycles.tsv` (cycle, size, runs, members, statuses) and `tools/cycles_detail.tsv` (for each: the
edges inside it, the 2-cycles, the edges that point to a later id, the hubs with most out-edges, the fields the edges
were read from). Sizes: one of 114 rows (S6_06_BLIND), 56 and 43 (LM4_FINITE_GROUP_ACTIONS), 43 and 43 (LM7_PUSH),
30 (GT_TOWER_CHECK), 22 (ANABELIAN_149_PUSH), 15 (three), ... and 31 of size 2. A proof that cites only earlier items
cannot make a cycle, so each cycle has one of these causes:
- (a) **a summary row:** an open or main-question row whose depends_on lists the rows that bear on it, while those rows
  list it back (the hubs: LM4 C.12 with 55 out-edges, LM4 D.12 with 37, LM7_PUSH B.6, EXIT_TOWER E.23,
  ANABELIAN_149_PUSH F.9);
- (b) **a consumer listed as a dependency** (depends_on naming the row that uses it);
- (c) **an equivalence** proved in one place, with each direction citing the other;
- (d) **a parent and its sub-item** (A.4 and A.4.17);
- (e) **my parse** (a range or sub-id read wrongly: check the `how` and `evidence` columns of GRAPH_EDGES.tsv);
- (f) **a genuinely circular argument**: a proof of A that uses B, whose proof uses A. This would be a gap.

## What to do

1. Classify every cycle by its cause, by script first (hubs, fields, the direction of each edge against the order
   of the ids, the statuses), then by reading where the script cannot tell. For the big cycles, identify the few
   edges whose removal breaks the cycle and say what those edges are (which of the causes above).
2. For **every 2-cycle in which both rows are Proved** (in the cycles and inside the bigger ones; outside S6 first,
   then S6_06_BLIND as far as your budget goes), read both proofs in the return's TeX and decide: (c), (b), (d), (e) or
   (f). For each (f), state the gap exactly (which step of which proof assumes what) and whether another route in the
   return closes it.
3. Propose the register's rule that would keep summary rows from making cycles (for example: a "bears on" relation
   kept apart from "uses"), with the rows of each run it would move.

Write `CYCLES.tsv` (cycle, size, run, members, cause, the edges that close it, verdict, what you read), FINDINGS.tsv
(one line per genuine gap or wrong dependency; kind "cycle"), CHECK_EVENTS.tsv (each proof you read for this, with what
you checked) and REPORT.md, as the common brief says. CLUSTERS.tsv is not needed.

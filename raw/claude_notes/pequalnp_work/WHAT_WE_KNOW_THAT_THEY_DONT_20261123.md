# What we know that the pequalnp fleet does not, and what we can learn that it cannot (23 Nov 2026, ~17:55 UTC)

By Claude Opus 5.5 at effort max (session 672ae3a0), at the user's question: [the user's words, omitted], answered from the record of the last 48 hours, not from the desk.

Read for this: the catch-up digest task_notes/catchup_20261123_329fb1e6.md (the mathematics of 20-23 Nov),
reports_20261120/IMPLICATIONS_REPORT_20261121.md (sections 1-3, 3.9, 3.10, 9.2, 9.4), field_experts/hexagon/HEXAGON_STATUS.md
(the 66 candidates), fleet_map/JOINT_GCT_LEMMA_SPACE.md (all clusters), fleet_map/FLEET_MAP.md section 3, the Fable agent's
mirror/BIG_ONES_CONNECTIONS.md (summary), the fleet's own graph (PROOF_GRAPH.tsv, searched), and our desk record of today.

## 1. The evidence on racing (today, 15:00-17:45 UTC)
Five sketched steps, five lost: L-meta-750 (withdrawn as proved by another while our proof was building), L-meta-756
(Codex's PR 1266: "proved first by another pull request"), L-meta-782 (our clean build 17:22, theirs merged 17:17:57),
L-meta-755 (handed to us 17:19:49, withdrawn as proved 17:28:16; our file alone took 532 s to elaborate, 17.6 min in all),
L-meta-738 (checked 16:51, before we began; we had the paper proof twice). On sketched steps the fleet gets the proof
within minutes with or without us: our marginal contribution there is zero. Their machines and pipelines are faster; we
cannot change that and should not try.

## 2. What we know that their graph does not contain
**(a) The 2026 complexity breakthroughs.** Their 1,469-node graph mentions none of them (searched: ETH, exponential time,
subexponential, k-SAT, 2^o(n)):
- OpenAI, "The Exponential Time Hypothesis is False" (25 Oct 2026; recent_results_20261110/papers/378): a fixed-width #k-SAT
  counter in 2^O(n log log n / sqrt(log n)); refutes ETH, SETH and their counting and gap forms (CX-E01, E06 of our
  CX_GRH run: it touches no VP/VNP or border-hardness premise).
- OpenAI's one-tape time T in space T^(2/5) (manuscript 137), and deterministic polynomial factorization over prime fields
  (PF26, 4 Oct 2026; transfer checked in our GRH_NIGHT run, CX-ALG-027).
- Hoza, NL = UL (ECCC TR26-323, on disk).
- Alpöge's RH and GRH for all Dirichlet L-functions (20 Nov, Lean): makes unconditional Miller's test with quadratic
  characters, least nonresidues, RH for abelian zeta functions, unit generation of (Z/N)^x below 3 log^2 N (our CX_GRH,
  ZETA_TWO, AN_GRH runs); Koiran's Nullstellensatz-in-AM still needs GRH for one non-abelian field (CX-K01).
These bear on their library/evasion chain (L-lib-122/123/125), their algorithm search (L-alg) and the clb program
(algorithmic method), which run without them.

**(b) Whole fields of GCT that their board has no row for** (joint table: their rows / ours): border rank of tensors
0/264 (our BR(det_4), BR(per_4) >= 43 over C, >= 42 over every field, H03; >= 52 for the divided-power coefficient
tensors, BORDER_RANK cp14); the GCT VI/VIII positivity hypotheses 0/366 (all fail in the det-perm setting: RH, PH1, OH,
PH2, SH(a), PH3; GCT_FLIP, WB-0002, H02, H02b, H23); Kronecker and plethysm coefficients 0/321 (positive formulas in outer
degree five, H20, H21); multiplicity and occurrence obstructions 0/478 (explicit occurrence obstructions at n = m,
four-row multiplicity obstructions under padding exactly when n^2 <= 2m^2 - m + 1, and no occurrence obstruction in their
exact padding for c >= 25). Mostly this is knowledge of where obstructions cannot be, which bears on their idle
L-gct-011.

**(c) Barriers on their stuck hard links** (paper arguments, not yet second-read):
- L-gct-086: any proof needs about n/(C+1) Taylor orders (the families F_{q,r}); self-similarity with q-uniform
  hyper-permanents; amplification and prime-power defect bounds (Codex); a finite-free-probability dictionary (Fable).
- L-meta-606/608/612: any proof must use independent sets of growing size: circuits of about 28 w n gates reject every
  independent set of at most w vertices on the affine-plane incidence graph (Fable Theorem C; checked at q = 5, 7); and
  for circuits the statement contains Jukna's open n^(3/2) problem.
- L-lib-123: refuting FP3 would prove exponential SAT-oracle circuit lower bounds for E (Fable Theorem A: compressible
  step records give FP3 with the three blocks used exactly); the ETH device (378) and the one-tape simulation (137) meet at
  one obstruction (the equality predicate does not factor over blocks), and 378's interpolation saves only a sqrt(log)
  factor in the exponent.

**(d) Proofs of posted nodes the desk does not want** (stood down; nobody is waiting on them): Lemma K (L-gct-122, Lean),
L-gct-116 (Codex, Lean), L-gct-211 (Codex, paper), riffle rank exactly 6 at n = 3 and >= 2n (L-gct-139/140), 125.

## 3. What we can learn that they cannot easily
Their agents are built for minutes-long formalization of sketched steps; their own seats have left the GCT line and the
hard links are stuck. We have what the stuck links need and they do not: hours-long research runs (ChatGPT Pro, Fable,
Opus at effort max), the user's corpus and the new papers on disk, and the cross-field maps the main session is building.

## 4. So: what to do
1. Never race a sketched step again. Hold only hard links (`&hard=1`: "any number of agents may hold the same hard step";
   no one has a route, so there is no race) and searches where structure beats compute.
2. Work each hard link as research, with the barriers above as the map of what cannot work: L-lib-123 (Theorem A's
   compression route, the 137/378 obstruction), L-gct-086 (R1-R3 and the free-probability dictionary), 612 (Theorem C).
   A proof found there is formalized afterwards, at leisure: nobody else is near it.
3. Everything else goes into our mirror (local and KokunoYumeto/pequalnp-mirror) and, when checked, to Hexagon: the fleet
   reads nothing but Lean files, so the barriers and the 2026 results enter its work only as proofs of hard links.

# The fleet's GCT program: proof map, and where our mathematics attacks it (23 Nov 2026)

Written by Claude Opus 5.5 at effort max (a workflow agent of session 672ae3a0), 23 Nov 2026, from the fleet export of
16:13 UTC (head `9f9743881bf6a8bc`). Read-only: no desk requests, pull requests or posts.
Companions in this folder: `PROOF_GRAPH.tsv` (every fleet lemma; for GCT only the few edges the fleet records, see
section 1.8 for the logical edges), `chatgpt_gct.md` (Codex's overlay on L-gct-086), `FLEET_MAP.md`.

**Read for this map.** Fleet: `head.json`; program map `gct.068d3b883eca.json` (218 nodes); `plan.c0dd4cd68cdb.json`;
the graveyard; the whole GCT feed (501 events, pages 1-11); all 218 GCT lemma records (plain and formal statements,
attempts with their death notes, corrections, literature notes) from `desk/lemma_cache`; the desk's handout of
L-gct-086 to our handle (`desk/next_10.json`). Repository clone: `Defs/Gct.lean`; the Lean statements and imports of
015, 024, 045, 056, 057, 064, 070, 072, 074, 077, 079, 080, 090, 092, 094, 098, 156, 157, 158, 163, 170, 175-178, 218;
the structure of the outside proofs `Outside/L_gct_214.lean` and `desk/L_gct_215_accepted.lean`. Ours:
`MAPPING_BY_READING_20261123.md`, `MAPPING_AGENT_RESULTS.md`, `L_meta_647_PARTIAL_PROOF.md` (its methods are compared
with the GCT rows in 5.8),
`MATCHES.md`, the five `desk/CODEX_TO_CLAUDE_*` notes on GCT, Codex's `outputs/FLEET_RESEARCH_MAP.md` and
`work/lemma_source_crosswalk/gct.md`, `fleet_map/chatgpt_gct.md`, and Rossman's *Riffle Rank* (8 May 2025, section 1
and appendix C). `L_META_632_RESULTS.md` does not exist. Not opened: files named SAT_WITNESS or SAT_KRONECKER and the
prompt-74 returns. Where a statement below rests on a source I did not read myself, it says "relayed".

**Notation.** S_k(t) = sum of all k x k subpermanents of a matrix t; perm(J_n + t) = sum_k (n-k)! S_k(t) (L-gct-084).
A *level space* is a complex linear space L of p x q matrices with S_k = 0 on L for every k >= 1 (for n x n: perm(J_n +
t) = n! on L). LS(p,q) is its maximal dimension, LS(n) = LS(n,n); kappa(n) is the maximum over doubly centred (DC: row
and column sums zero) level spaces; RC = row-centred. p_k = sum of k-th powers of the entries.
**Status codes.** C = checked in Lean by a fleet seat; O = checked from an outside pull request (GitHub handle given);
J = open (conjecture); W = in work; X = retired; R = refuted. Ids are written without the prefix where unambiguous
(086 = L-gct-086).

## 0. The program in ten lines

1. 218 nodes: 135 checked (the overview counts 134 plus 081, judged not faithful), 66 open, 1 in work (036), 15 retired,
   1 refuted (016).
2. Stated target L-gct-026: the cubic lower bound on border determinantal complexity of perm_m, an unrefereed 2026 claim.
   It waits on L-gct-025, which the fleet priced "out of reach", and no seat works it.
3. Best checked lower bounds for perm_m: 2m^2 + 11 <= 3n + 10m for exact (064) and border (070) expressions; and
   border dc(perm_m) >= R m^2 for all m >= m0(R), every R (074). Line B (smooth forms) is the only line past m^2.
4. Hard link L-gct-086 ("level spaces are linear"), held by our handle since 15:45 UTC. Through 077 it would give
   m^2 - (C+2)m + C + 1. That is explicit but asymptotically below the checked 074, and the subspace method it
   serves is capped at (m-1)^2 + 1 (044).
5. The GCT line rests. At 00:40 UTC the strategy seat moved seats off the level-space line, at 09:25 UTC the hard link was
   released to outside provers, and no fleet seat has proposed a GCT row since 10:27 UTC. The newest checks are outside
   proofs of small cases (214, 216, 217 in the morning; 215 at 15:16 UTC).
6. Two open search rows are already decided, false, by checked rows with identical hypotheses: 181 by 215, 182 by 216.
7. The riffle-rank sub-line has lost its complexity payoff: the checked 097 and 218 refute Rossman's Conjecture C.2.
8. The program has no representation theory. L-gct-011 (Mulmuley-Sohoni) is open; its cases c <= 2 follow from 074.
9. What we have:
   - On 086: a barrier theorem on Taylor orders, the exact low layers and a self-similar family; Codex adds an
     amplification and a prime-power symmetry bound. No proof.
   - On 091 and the small-case table: an exact rational chart, numerical evidence, and Codex's symmetric-class bounds.
   - Proofs in hand: 116 and 211 (Codex), 122 (our Lean proof), 125 and 139 (ours), and riffle rank exactly 6 at n = 3.
   - On 036/037: the real case only.
10. Nothing of ours reaches 025/026 or the DIV hypotheses 103/104; section 5.8 gives the mathematical reason for each.

## 1. The target and the chains as they stand

### 1.1 Stated target and plan chain
- **Target L-gct-026 [J]**: there are a constant c and m0 such that every border determinantal expression of perm_m,
  m >= m0, has size at least m^3/c (the manuscript states c = 5529600e and m >= 1408). The plan says: "this project has
  not verified it and has no proof route to it at present". Assembly 027 [C, conditional on 025]: 026 follows from
  023 [C] (border expressions survive affine substitution), 024 [C] and 025 [J].
- Plan chain, in its order: 009, 015, 010, 024, 045, 035, 050, 051, 052, 062, 066, 065, 061, 064, 068, 057, 056, 067,
  069, 070, 077 (all C), then 086 [J, hard link], 025 [J], 026 [J].
- **Hard link 086** (plan): "No proof route has survived yet". The last fleet attempt, by seat-barrier-1, ended 09:25 UTC:
  "line rests (on no chain); outside provers hold leases; released so an accepted outside proof can be recorded".

### 1.2 Line A: explicit quadratic bounds (Hessians, linear spaces through a zero)
Checked:
- 009 (Mignon-Ressayre 2004): dc(perm_m) >= m^2/2. 010 (Landsberg-Manivel-Ressayre 2013): border dc >= m^2/2.
- **015**: m^2 + 2 <= 2n for every exact expression of perm_m, m >= 3 (via 021, 020 and 019; 016 was refuted and
  restated as 020). It is the program's first result past the textbooks.
- 035 (exact) and 069 (border), the subspace reduction: if at some zero y every linear L with perm_m(y + t) = 0 on L has
  dim <= k, then the size is >= m^2 - k. 050-052: the cone extension and the vanishing of every polarized Taylor
  coefficient on such L.
- 062: at Sigma_m = J - m E_11, l(Sigma_m) <= 4(m-1) + F, where F is the largest dimension of a space of (m-1) x (m-1)
  matrices killing p_2 and p_3. 061: p_2 = p_3 = 0 on W in C^M implies 3 dim W <= M (via 066 from 065, Kneser for
  codes: Mirandola-Zemor 2015, Thm 3.3). 067: p_2..p_k = 0 implies k dim W <= M. 063 is a weak form.
- **064 / 070 (= 072)**: 2m^2 + 11 <= 3n + 10m for exact and for border expressions, m >= 3. This is past m^2/2 from
  m = 19-20.
- 044, the ceiling: every zero carries a (2m-2)-dimensional linear space in the hypersurface, so the method never gives
  more than (m-1)^2 + 1.
- **087**: Sigma_4 carries an exact 7-dimensional non-real space over Q(omega); so Sigma_m is not a witness for 036/037
  at m = 4.
- 079: product-type spaces through Sigma_m have dim <= 2m - 2 (a Kneser chain). 055: the block-only case at Sigma_4 is
  <= 4. 169: the corner lemma for 7-dimensional spaces killing perm_4. 081 and 085: zeros to avoid; 081 is judged not
  faithful (its formal statement is met by y = 0).
- **077**: if LS(n) <= G, every border expression of perm_{n+1} has size N with (n+1)^2 + 1 <= G + 2(n+1) + N. It is
  proved from 069 at Sigma_{n+1}, where perm(Sigma + t) restricted to the block is -d/dc perm_n(J + cs).

Open: 036 [W] (m = 4: a zero with no 7-dimensional space; it would give dc(perm_4) >= 10), 037 [J] (every m: a zero with
<= 2m - 2; it would give (m-1)^2 + 1), 028 [J] (border MR+1, dropped), 113 and 115 (steps of 036), 078 [J] (dropped).

### 1.3 Line B: smooth forms and polar points, the only line past m^2
- **024 [C]**: a homogeneous G of degree r >= 2 in d >= 2 variables whose partials vanish together only at 0 has
  (r-1)(d-1) <= 11 n for every border expression of size n. It is proved from 034 (which uses 047, 048, 049), 040 (which
  uses 038, 039) and 041. Unrefereed 2026 papers state it with constant 1/(4e).
- 045: the same bound for power sums. 030, 042, 043, 053, 058, 059 and 060 supply persistence of simple zeros, Bezout
  counts and "Bertini-lite".
- 057: perm restricts affinely to smooth forms with (r-1)(d-1)/m^2 unbounded (block sums of r x r subpermanent sums;
  Helpers/Rung). 056: border dc(perm_m) is not O(m^2).
- **074**: for every natural R there is m0 with R m^2 <= n for every border expression of perm_m of size n, m >= m0.
  The rate is not explicit. On paper, seat-clb-1's gadget gives (r-1)d <= m^2/4 explicitly and m^2 log m generically.

Open: 025, 026; the assembly 027 is conditional on 025.

### 1.4 Line C: level spaces, the hard link's neighbourhood
Reductions and identities [C]:
- 077 (above). 092: LS(n) <= kappa(n) + 2n. 098 (Lemma I, which also follows from Lovitz-Petrov 2023, Thm 4): invisible
  row blocks have dim <= P - 1, so peelable DC spaces have dim <= 2n - 2 and 086 reduces to "cores".
- 084, 088, 089 (S_k(x y^T) = k! e_k(x) e_k(y)), 099, 118.
- 105, 106, 134: on DC matrices 2 S_2 = p_2, 6 S_3 = 4 p_3, and
  24 S_4 = 36 p_4 - 18(R_4 + C_4) + 6 tr((t t^T)^2) + 3 p_2^2. 107, 159.

Structure [C]:
- 090 (Conjecture C; follows from Lovitz-Petrov). 111 and 123: row-product and column-product level spaces have total
  dimension <= n - 1. 114: row plus column parts have total dimension <= 2n - 2.
- 110: direct sums on disjoint blocks are level.
- 119: if t(sigma i, tau j) = z t(i, j) with z^k != 1 for k <= n, then t is level. 120, 121: rank-one level lines.
- 142: if every even e_{2j} vanishes on a space, its dimension is <= 1.
- 163 (T3): the three-subspace lemma with p_4.
- 175, the column-product core: if J is in V and sum_j prod_i x_ij = q lam(x)^p on V, then dim V <= q. 176, 177: the
  append lemmas. 170, 171 (Rado).
- 202: a 4 x q level matrix (q >= 4) has no nonzero constant row.
- 158 (real case, standard): real p x q level spaces have dim <= p + q - 2.

Floor and exact values, best known lower bound against checked upper bound:

| size | lower bound (witness) | checked upper bound | open rows |
|---|---|---|---|
| 2 x q | q - 1 (108) | q - 1 (101) | none |
| 3 x q | q (row plus column) | q + 1 (156); RC: q - 1 (157) | none |
| 3 x 3 | 3 (080) | 3 (094); kappa(3) <= 1 (109) | none |
| 4 x 4 | 5 = 2n - 3 (080) | **6 (214, O visez)** | 091 (<= 5), 185 (= 6) |
| 4 x 4, DC | 3 (characters) | **3 (216, O stierms)** | 182: decided false |
| 4 x 4, RC | 5 (197, F_4) | **5 (217, O gearashi)** | none |
| 4 x 5 | 6 | **7 (215, O stierms, 15:16 UTC)** | 179 (= 7); 181: decided false |
| 4 x 5, RC / DC | 6 (180) / 4 (mode core) | none | 199 (DC = 5) |
| 4 x 6 | 7 (208) | none | 195 (<= 8), 187 (= 8), 206 (G(4)) |
| 4 x 6, RC | 7 (198) | none | 191 (= 8) |
| 4 x 7 | 8 | none | 196 (<= 9) |
| 5 x 5 | 7 (189) | none | 210 (<= 8), 190 (= 8) |
| 5 x 7 | 9 (G(5), proposed in 207, not yet checked) | none | 207 |
| n x n | 2n - 3 (080) | kappa(n) + 2n (092) | **086 (<= C n)** |

At four rows the checked values give q + 1 <= LS(4,q) <= q + 2 for q = 4, 5. RC(4,q) >= q + 1 for q = 4, 5, 6 (197, 180,
198): the three-row bound q - 1 (157) dies at four rows.

Open in this line: 086, 091, the table rows above, 116 (barrier B9), 211 (row-shift-invariant spaces at prime n), 204,
205, 113, 115, 117, 122 (Lemma K), 135, 136, 143 (conjecture S at two rows; its general form is refuted), and 162 and
165-168. These last five are build steps of 157, which was checked by another route (Rado, 171), so they unlock nothing
now.

### 1.5 Line D: Mulmuley-Sohoni, L-gct-011
- **011 [J]**: for every c >= 1 and all large m, paddedPerm(m, m^c) is not in orbitClosure(det_{m^c + 1}), as in the
  `Defs/Gct.lean` padding with the independent entry (0,0).
- Checked input: 006 (an expression puts the padded permanent in the orbit closure).
- No node mentions obstructions, multiplicities, plethysm or occurrence.
- The cases c = 1, 2 follow from 074 together with the converse of 006. The converse: orbit-closure membership gives a
  border expression of size n + 1, then substitute X_00 to 1 through the checked helper `hasBorderDetExpression_bind₁`.
  This was observed by our survey (a8d75352, Claude Opus 5.5 at effort high); it is not a node, since the posted node
  quantifies over all c.

### 1.6 Line E: the algebraic route (seat-gct-2, `routes/algebraic`)
- **103, 104 [J]**, the hypotheses DIV(3, 27/25) and DIV(4, 6/5). Take a nonzero signed sum of K <= (log_2 T)^c M-th
  powers of T-sparse integer polynomials, divisible by (X+1)...(X+N). DIV(3, 27/25) says N^25 <= T^27 (M = 3); DIV(4, 6/5)
  says N^5 <= T^6 (M = 4). "Nobody claims it; no case with K >= 2 is known proved." The reduction to the permanent is on
  paper only.
- Checked: 150 (the gap lemma).
- Tractable rows for the outside desk: 126, 127, 128 (weak Descartes), 129 (the case K = 1), 130 (two cubes), 132, 137,
  138, 141, 144-149, 154, 155, 161, 164, 172-174 (a sparse-Wronskian ladder). 148 and 155 certify nine sign changes for
  three cubes, the first open size.
- 126 (Fischer's identity at M = 3) already has a one-line `ring` proof in the public repository
  (`Outside/L_gct_126.lean`, present in our clone), while the map still lists it as open.

### 1.7 Line F: riffle rank (Rossman, Question C.1)
- Checked: 095 (n = 2: three terms), 096 (multiplicativity) and 097 (riffle(I_n (x) I_n) <= 3^{ceil(log_2 n)}, about
  n^1.585). The literature desk marks 097 known: tensor powers of the [3,2] simplex code through the PIR bridge 124. It
  also notes binary PIR codes with Theta(n) disjoint recovering sets and length O(n^{1+tau}) for every tau > 0
  (arXiv:1701.07206v2, Thm 12).
- **218 [C]**: for every c > 0 and d, riffle(I_n (x) I_n) < c n^2/(log_2 n)^d for all large n.
- Open: 124 (the PIR bridge), 125 (n = 2: not two terms), 139 (>= 2n - 1), 140 (n = 3: six terms).
- **What this means.** Rossman's Conjecture C.2 says R_riffle(I_n (x) I_n) = Omega~(n^2). 218 is its checked negation,
  and 097 refutes it more strongly. Rossman's own remark in appendix C says that an O(n^{2-eps}) bound refutes his
  Conjecture 1.2 "and render[s] Corollaries 1.4-1.6 uninteresting". Those corollaries are the route to
  VNC^1 != VBP. Only the exact value of Question C.1 remains, as pure mathematics.

### 1.8 Logical edges (child <= parents), from the statements and the Lean imports
The fleet records few `depends_on` arrays; these are the working edges.
```
026 <= 023, 024, 025              027 = assembly of 026, conditional on 025
024 <= 034, 040, 041              034 <= 047, 048, 049     040 <= 038, 039     045 <= 040, 046 (043, 030)
056 <= 023, 024, 057              074 <= 057 (Helpers/Rung/AllM), 023, 024
015 <= 021 <= 020 (016 refuted, 017 retired); 019
064 <= 035, 061, 062              061 <= 066 <= 065       067 <= 065
070 (= 072) <= 069, 075           077 <= 069 at Sigma_{n+1} (Helpers/GReduction)
086 + 077  =>  border dc(perm_m) >= m^2 - (C+2)m + C + 1
037 + 035/069 => dc >= (m-1)^2 + 1;   036 + 035 => dc(perm_4) >= 10;   044 caps both
092: LS(n) <= kappa(n) + 2n       098 <= 090              111 <= 090; 123 <= 111; 114 <= 111, 123
156 <= 157 <= 171                 178 <= 157               177 <= 175, 176; 170 = 175 at p = 3
079 <= 065                        163 <= 065               122 (open) <= 065, 061 skeleton (our Lean proof)
218 <= 097 <= 095, 096            139, 125 <= F-13 image substitution (ours)    140: a finite identity
011 for c <= 2 <= 074 + converse of 006 (not a node)
181 is false by 215; 182 is false by 216 (identical hypotheses; not recorded on the map)
```

## 2. What is open and live

### 2.1 Hard links and chain links
- **086 [J], the hard link.** There is a C with dim L <= C n for every n and every level space L of n x n matrices.
  - The desk handed it to our handle at 15:45 UTC with weight 60 and "parallel 10".
  - Desk context: 080, 092, 094 and 090 are checked, and "a proof must use Taylor orders growing with n".
  - The desk's dead list: every form of "a level space splits into a row part and a column part", arguments of bounded
    order, and the determinant analogue (which is quadratic).
  - The Lean file may import only `PEqualNP.Defs`.
- 025 [J]: the cubic smooth restriction (no seat). 026 [J]: the target.
- 036 [W]: the attempt by seat-clb-2 has been open since 22 Nov 19:14 UTC, with no event since. 037 [J]: superseded in
  purpose by 077/086. 028 [J]: dropped by strategy. 011 [J]: no seat.
- Line E: 103 and 104 [J] and their tractable rows.

### 2.2 The newest conjectures
- Fleet proposals: 195-202 at 06:53 UTC, 203-207 at 07:14, the refiles 208-217 at 07:43-07:48, and 218 at 10:27 (checked
  10:43). Still open among them: 195, 196, 199, 204, 205, 206, 207, 210, 211.
- After the 07:48 refiles the fleet's own GCT activity is 218 and two releases (091 at 09:19, 086 at 09:25). Everything
  else is outside checks: 208, 212 and 217 at 08:58, 213 at 09:02, 216 at 09:07, 214 at 10:11, 215 at 15:16.

### 2.3 Decided or done, but not recorded
- **181** ("there is a 4 x 5 level space of dim >= 8") is false: 215 [C] gives <= 7 under the same four hypotheses.
- **182** ("there is a 4 x 4 DC level space of dim 4") is false: 216 [C] gives <= 3 under the same five hypotheses.
- 126 has a `ring` proof in the public repository. 162 and 165-168 are orphaned build steps.
- Proofs of 116, 122, 125, 139 and 211 (ours or Codex's) are waiting for a desk handout, as is Codex's integer check of
  140's six-term identity (section 5).

## 3. Dead approaches, with their reasons

| approach | rows | why it died (source) |
|---|---|---|
| "The adjugate kills the radical of det's Hessian" | 016 (R), 017 (X) | False at n = 1 (M = [0]); restated for n >= 2 as 020, and 017 retired into 021 (red team, checker-accepted) |
| Border MR+1 by the route of 015 | 028 | The route needs a fixed constant part A0 across nearby zeros, but under border limits the normalized expressions diverge (at S2 for odd m, at S3/S5 for even m; the 2-jet passes, the 3-jet does not). "The limit loses exactly the two equations behind +1." Dropped by strategy (seat-barrier-1, seat-lib-2, 22 Nov) |
| The manuscript route to the cubic step | 025 | It needs spectral curves, a Severi bound and Bertini, none in the pinned library. The fleet's own gadget G_r reaches (r-1)d <= m^2/4 (explicit) or m^2 log m (generic) on paper: superquadratic only (giving 056/057/074). In the characteristic-2 Pfaffian variant the singular locus has only linear codimension (seat-clb-1, seat-clb-2) |
| Groebner/msolve charts for 036 at J - 4E_44 | 036 | 48 variables and 203 equations; an OG(7,14) chart with 27 variables in degree 8. Too slow and not Lean-certifiable; "core Bd = 0 needs a new idea" (seat-gct-1). The zero itself is moot after 087 |
| Bound 2m - 2 at Sigma_m over C | 037 | False at m = 4: 087 gives an exact non-real 7-dimensional space. The route moved to 077/086 (seat-barrier-1). The real version holds (section 5.6) |
| Zeros that carry large spaces | 078, 081, 085 | 078: for even m, zeros with no zero entry carry m^2/2-dimensional spaces, dropped as "a negative result that warns and does not advance". 081/085: the zero [[-1, e_1^T], [e_1, I]] carries (m-1)(m-2)/2; 081 is also unfaithful. The method must avoid such zeros |
| Splitting a level space into a row part and a column part | desk dead list, 143 | Exact counterexamples: eigenspace lines (119) and the circulant (1, i, -i, -1) line (193); the general conjecture S has a 4 x 4 counterexample |
| Arguments of bounded Taylor order | desk dead list | Section 5.1(c) makes it a theorem: a linear bound needs linearly many orders, up to order about n/(C+1) |
| The determinant analogy | desk dead list | At I the determinant's level spaces are the nilpotent spaces, up to n(n-1)/2 |
| Real-number evidence | plan, 158 | Real searches missed complex spaces. The real problem is easy (p + q - 2) and blind to the complex excess, which is totally non-real (section 5.1(b)) |
| Laplace descent through arbitrary base points (the method of the outside proof of 214) | 091, 210 | *Observation of this map.* The proof's lower-size steps F2 and F3 are proved for an arbitrary base point X0 (perm translation-invariant under L on L + C X0, perm(X0) != 0). That class contains X0 = I with L the strictly upper triangular matrices (perm(cI + y) = c^n), of dimension k(k-1)/2 at size k, and the proved values F2 = 1, F3 = 3 are exactly these triangular numbers. A descent through general base points therefore carries a quadratic term and cannot give a linear bound. At n = 4 it gave 6 (214), not the 5 of 091; at n = 5 the 4 x 4 general-base-point bound it would need is already >= 6 |
| Torus degenerations (our BR_PENCIL machinery) for 086 | 086 | The only torus preserving the problem moves J; torus-fixed limits fall into {perm = 0} and lose the level condition (MAPPING_AGENT_RESULTS 1.6) |
| Riffle rank as a route to VNC^1 != VBP | 097, 218 | Refuted at k = 2 by Rossman's own criterion (section 1.7) |
| Seats moved off | 091, 163, 156, 086 | At 00:40 UTC the strategy ruling moved seat-alg-1 off 091 (handover notes/gct-ls4-state.md) and seat-pcx-1 to the evasion chain, and handed 156 to seat-gct-2. 086 was released at 09:25 UTC |

## 4. Where the line is heading

**The fleet.** The GCT line rests. Its seats moved to meta-complexity: the strategy seat's status line at 16:11 UTC is
entirely about AND/OR circuits for edge functions. GCT is now fed by the outside desk: four outside proofs of small
cases (214-217) arrived between 08:58 and 15:16 UTC.

**What the newest checked lemmas make possible next:**
- **091, LS(4) = 5.** It is now the one open exact question at n = 4 and the first test of "LS(n) = 2n - 3". With 214,
  216 and 217 checked, a 6-dimensional 4 x 4 level space L would have dim(L cap DC) <= 3. Its row- and column-sum vectors
  lie in two sum-zero hyperplanes, and the image of L there has dimension >= 3; dim(L cap RC) lies between 3 and 5.
- **The four-row column.** 215 starts it: 195 (4 x 6 <= 8) and 196 (4 x 7 <= 9), the pattern q + 1 <= LS(4,q) <= q + 2;
  then 210 (5 x 5 <= 8).
- **The Mulmuley-Sohoni target.** 074 makes 011 for c <= 2 a short formalization (60-120 Lean lines on the fleet's
  helpers), once the board splits 011.
- **Riffle.** 218 closes the complexity side; the open riffle rows (124, 125, 139, 140) are now exact-value questions.
- **The algebraic route.** It is building toward the first open case of DIV, three cubes: the case K = 1 (129), two cubes
  (130), the sparse Wronskian ladder (172-174) and certified sign changes (148, 155).
- **The cubic target.** 074 has no successor row; the target waits on 025, and no seat works it.

**For us.** The hard link's payoff is bounded. It gives m^2 - O(m) through 077: an explicit constant, capped at
(m-1)^2 + 1 by 044, and asymptotically below the checked 074. The program's own target is blocked at 025. The only
rows aimed beyond polynomial bounds, 011 and 103/104, have no seat. Attacking "where it matters" therefore means:
- 086 only as far as it yields structural mathematics, plus 091 as its calibration;
- 025 if we want the fleet's own target;
- 011 if we want our representation theory to count.

## 5. Where our mathematics attacks it

### 5.1 L-gct-086 (our lease)
Our sources are `MAPPING_AGENT_RESULTS.md` section 1 (Claude Opus 5.5 at effort max, agent a3533d80e4df973c2; paper
proofs, numerically checked) and Codex's notes. I re-derived (a)-(e) while writing this map.

(a) **Exact low layers.** On DC matrices S_2 = p_2/2 and S_3 = (2/3) p_3, matching the fleet's checked 105 and 106.
- So the core K = L cap DC kills p_2 and p_3, and 061 gives 3 dim K <= n^2.
- With 092, LS(n) <= n^2/3 + 2n. Codex sharpens this to n^2/3 + 2n - 2, using S_1 = 0 (both sum vectors lie in a
  sum-zero hyperplane).
- Through 077 this gives 3N + 10m >= 2m^2 + 14: one unit above 070, by the same mechanism as 061/062. It is not a real
  gain.

(b) **The real structure.** On real DC matrices S_2 = |t|^2/2 > 0, so a real core is 0 and real level spaces have
dim <= 2n - 2 (that is 158). For a complex L, L cap conj(L) is the complexification of a real level space. Hence the whole
complex excess is totally non-real: K cap conj(K) = 0.

(c) **Barrier theorem: any proof must use linearly many Taylor orders.** This is the exact form of the desk's "bounded
order" entry.
- *Family.* For q | r <= n and omega a primitive q-th root of unity, let F_{q,r} be the matrices whose first r rows form
  r/q blocks; in block I the rows are omega^a c_I (a in Z_q, c_I in C^n free), and the other rows are 0. Then
  dim F_{q,r} = (r/q) n.
- *Claim.* S_k = 0 on F_{q,r} unless q | k and k <= r.
- *Proof.* k! S_k is the sum over distinct row k-tuples and distinct column k-tuples. Moebius inversion over the
  set-partition lattices of the row slots and the column slots writes it as a combination of unrestricted sums N(pi,
  sigma). In N(pi, sigma) each block beta of pi contributes the factor sum_a omega^{a|beta|}, which is 0 unless q
  divides |beta|. For k > r every k x k submatrix has a zero row.
- *Consequence.* Suppose a set Omega of orders has the property that S_k = 0 on L for all k in Omega forces
  dim L <= Cn. Put a = floor(C) + 1. For every q <= n/a, F_{q,aq} has dimension a n > C n, so Omega meets
  {q, 2q, ..., aq}. Hence |Omega| >= floor(n/a)/a, and max Omega >= floor(n/a).
- Codex (chatgpt_gct.md) improves the count to |Omega| >= (1/6 - o(1)) n for C = 2.
- With orders <= 3 the best possible core bound lies between n(n-1)/4 (F_4 cap DC, for 4 | n) and n^2/3 (from (a)).
- This kills every route through finitely many identities: power sums, Lemma K type bounds, the order-4 identity 134.

(d) **Self-similarity.** For t in F_q = F_{q,n} (m = n/q blocks):

  perm(J + t) = (q!)^m sum over ordered partitions (C_1, ..., C_m) of [n] into q-sets of
  prod_I (1 + (-1)^{q-1} prod_{j in C_I} c_I(j)).

(Codex derives it the same way from the checked 089.)
- So level spaces inside F_q are exactly the level spaces of the q-uniform "hyper-permanent" of the m x n array c:
  all hyper-matching sums h_k (k rows, k disjoint q-sets) vanish. q = 1 is 086 itself. q = n says that a product of
  linear forms vanishes on the space, so dim <= n - 1.
- For every q | n, supporting each row on a fixed (q-1)-set gives a level space of dimension n - n/q.

(e) **A DC family.** t = u (x) (1, z, ..., z^{n-1}), with z a primitive n-th root of unity and u in V with u_1 = 0. It is
level, since S_k = k! e_k(u) e_k(v), e_k(v) = 0 for k < n and e_n(u) = 0. Its dimension is n - 2, so kappa(n) >= n - 2
(kappa(3) = 1; kappa(4) = 3 is checked, 216).

(f) **Codex (GPT-6.2 Astra at reasoning effort ultra, per its 15:40 UTC session metadata).**
- *Amplification.* Rook polynomials multiply on block-diagonal perturbations, R_{X (+) Y} = R_X R_Y. So
  LS(m) >= floor(m/n) LS(n), and lim LS(m)/m = sup_n LS(n)/n along any unbounded sequence. 086 may be proved on
  powers of 2, and one finite counterexample propagates.
- *Prime powers.* At prime powers n, for a full row cycle T with one-step defect r = dim L - dim(L cap TL),
  dim L <= (n - 1)(r + 1). This comes from the row-translation theorem (211, extended).

**Where this leaves 086.** No proof route is in our material. Three concrete routes, each an agent task:
- **R1, q-induction.** Bound the hyper-level problem of (d) at q in terms of the problems at divisors of q (or at q = 1).
  The families F_q carry every known large truncated example, so this is where a counterexample would also live.
- **R2, a Kneser inequality for all singleton-free invariants N(pi, sigma).** These are the Moebius terms of (c). The
  checked 163 (T3) is the p_4 case; 061 and 122 are power-sum cases. We need the order-k version whose hypotheses are
  S_2 = ... = S_k = 0 on the core, for k growing with n. By (c), nothing less can work.
- **R3, symmetry with controlled defect.** Prove that a large level space has a row cycle of bounded defect r, so that
  (f) applies; or prove a defect inequality. Codex's six-row example (all matching sums 0, row-product sum 6s^4 +
  6abcd) shows that mixed orders break the row identity outside prime powers.
- First calibrate on 091 (section 5.2).

### 5.2 L-gct-091 and the small-case table
- **091.** 214, 216 and 217 cut the case analysis to spaces with dim(L cap DC) <= 3 and a sum image of dimension >= 3
  (section 4).
  - Our rational chart for n = 4 (MAPPING_AGENT_RESULTS 1.5): Klein (Walsh) coordinates t = F X F^T, X in Mat_3, in
    which, over Q, p_2 = tr(X X^T), p_3 = (3/2) perm_3(X) and perm_4(t) = (tr X X^T)^2/32 + Q(X)/16. This is the
    coordinate system for an exact certificate: isotropic-Grassmannian charts over Q, Groebner bases, Nullstellensatz
    cofactors for Lean.
  - Evidence: 0 hits at dimension 6 in 2600 complex Levenberg-Marquardt restarts (plateau 2e-4, full-rank Jacobian).
- **182 and 181** need no work: they are false (section 2.3).
- **199 and 191 (searches).** Codex (GPT-6.2 Astra at reasoning effort ultra per its session log, crosswalk `gct.md`, 15:17 UTC) proves
  bounds in the class of spaces invariant under the regular Klein four-group acting on the rows:
  - DC: exact maxima 3, 3 and 5 at widths 4, 5 and 6;
  - RC: at most 3, 4, 6 and 7 at widths 4, 5, 6 and 7.
  - Proof: project onto the characters, L = a (x) U + b (x) V + c (x) W. Since e_2(a) = -2 and e_4(a) = 1, p_2 = p_4 = 0
    on each column space, so Lemma K and its equality classification apply. The mixed cubic is 16 sum x y z and the
    mixed quartic -2(2<x,y>^2 - 6 sum x^2 y^2).
  - Consequence: witnesses for 199 and 191 must break this symmetry.
- **195, 196, 210.** No method in hand.
  - The outside methods do not scale. 214's descent is capped (section 3). 215 is a 472 KB case analysis on the ranks of
    row projections, judging from its lemma structure: pairs of rows project into <= 7 dimensions, with a case "row 0 has
    rank >= 4" and cube-root-of-unity configurations.
  - A general four-row bound needs a structural lemma. The candidates in hand are 178 (RC <= q - 1 + rank of one row),
    202 (no constant row) and Lemma K on the character modes.
- **206, 207, 194** are explicit families (G(4), G(5), the circulant plus a row): finite verifications, not research.

### 5.3 L-gct-116 and L-gct-211 (barrier rows of the 086 line)
Codex (GPT-6.2 Astra at reasoning effort ultra, per its session log; corrected 23 Nov 17:2x UTC) has proofs of both.
- **116** is proved in Lean in the exact posted form. The upstream checker accepted it locally, re-checking 1080
  constants; it has not been submitted.
- **211** has a written proof for every regular finite abelian row group of prime-power order, and for rectangular
  arrays with at most the largest prime-power divisor of the row count as columns.
  - Translation kills the nontrivial total frequencies.
  - At prime-power order the single-block partition term has strictly smaller p-adic valuation, which gives the row
    identity sum_j prod_i (s + t_ij) = n s^q.
  - The checked 175, applied to the transpose with J adjoined, gives dim <= n - 1, which is sharp.
- At six rows the identity fails: an example with four columns has row-product sum 6s^4 + 6abcd while every matching sum
  is 0.
- These proofs would move 116 and 211 the moment the desk hands them out.

### 5.4 L-gct-122 (Lemma K: p_2 = p_4 = 0 on W implies 3 dim W <= M)
- Our proof (MAPPING_BY_READING A1):
  1. Polarization makes U = W * W orthogonal to 1 and totally isotropic.
  2. The stabilizer of U is spanned by block indicators, s blocks, and 2 dim U + s <= M.
  3. Kneser (065) with S = T = W gives 2 dim W <= dim U + s.
  4. Blocks of size <= 2 are dead coordinates (strong induction on M); otherwise s <= M/3, so 3 dim W <= M.
- It builds in Lean (axioms propext, Classical.choice, Quot.sound). Our PR #874 was closed unchecked at 15:14 UTC: the desk
  had stood the step down.
- Codex adds the equality cases: after at most 7(M - 3 dim W) coordinate deletions, W is a direct sum of triple lines
  (1, omega, omega^2). The constant is sharp on the seven-coordinate plane spanned by the characters chi_1 and chi_3.
- Uses: the Klein four-group analysis (5.2) and the "self-gluable 4 x s" analysis on the 086 line.

### 5.5 The riffle rows (124, 125, 139, 140)
- Ours. F-13 image substitution (MAPPING_BY_READING A2) gives riffle(I_n (x) I_n) >= 2n - 1 for every n >= 1 over every
  field, which proves 139 and, at n = 2, 125. MAPPING_AGENT_RESULTS section 3 gives >= 2n for n >= 3, so with 140's six
  terms riffle(I_3 (x) I_3) = 6, the first exact value past n = 2.
- Codex: >= ceil((19n - 14)/8) for n >= 14, through disjoint recovering sets. 124 is a two-line bridge.
- The true order of growth lies between about 2.4 n and n^1.585 (in characteristic 2 perhaps n^{1+o(1)} through PIR codes).
  None of this has a complexity payoff (section 1.7).

### 5.6 L-gct-036 and L-gct-037
- Ours (MAPPING_AGENT_RESULTS 2). At Sigma_m the tangent Hessian quotient has signature (2m - 3, (m-1)^2). So every
  *real* linear W containing Sigma_m inside {perm_m = 0} has dim W <= 2m - 2, which is sharp against 044.
- Codex extends this to the zeros Y with first row v (sum v = 0, every v_j != 0) and all other rows 1. The inertia is
  (m - 1 + (m-2)h, m - 1 + (m-2)p, 1), and the real bound is m + (m-2) min(p, h).
- Over C the quadratic layer gives only 1 + floor((m^2 - 2)/2) at every such zero: 8 at m = 4, where 6 is needed. 087
  shows Sigma_4 fails over C.
- So 036 needs a different complex zero and the cubic and quartic Taylor layers (052 makes them available); nothing of
  ours supplies them. Its payoff is dc(perm_4) >= 10, and 037's purpose already runs through 077/086.

### 5.7 L-gct-011 (relayed: our representation-theoretic returns, read by Codex and in MAPPING_BY_READING B)
**Exclusions.**
- The final GCT_FLIP (theorem thm:new-variable-no-occurrence, as read by Codex) covers the fleet's exact padding. If
  m >= 2 and N >= (m+1)^25, or m >= 5 and N >= m^25, every irreducible representation occurring for the padded permanent
  already occurs for the determinant in the same degree. So there is no occurrence obstruction for any c >= 25, m >= 5.
- GCT_SEPARATIONS (checkpoint 14): for m = 4 and N >= 7 there is no multiplicity obstruction of height <= 4 in any
  degree. Codex reconstructed the 35 x 35 minor, 72,185,580,000 = 88 mod 101.
- H14: four-row multiplicity obstructions under padding exist exactly when n^2 <= 2m^2 - m + 1 (m >= 17).
- GCT VI and VIII positivity hypotheses PH2, SH(a) and PH3 fail (H02, H02b, H23).

**Existence at fixed sizes.**
- (8, 9): the weight b(24, 1, 1, 1) has larger multiplicity for z per_8 for every b >= 6 * 10^47. The separation of that
  pair already follows from 010 together with the converse of 006.
- Unpadded per_n against det_n: four-row multiplicity obstructions for 4 <= n <= 16 (R-12, R-13), and Hessian-bracket
  multiplicity-one obstructions for every n >= 3 (GCT_KRON).

**Net.** These results tell an obstruction search where it cannot succeed (occurrence, low height, four rows). None moves
011 for any fixed c and all large m. The cheap move on 011 is not ours: c <= 2 from 074 (section 1.5).

### 5.8 No input from us: 025/026 and 103/104, and why
- **025** asks for an *affine* restriction of perm_{11k} that is a smooth form of degree >= k/3 in >= k^2/100
  variables.
  - Our permanent results concern the dimension of the family of *linear* restrictions (CUE_GCT G-21: the
    permanent-pencil image has dimension r m^2 - 2m + 2 for m >= 17, r >= 4) and dominance onto quaternary forms for
    n <= 16 (R-12, R-13).
    The latter gives smooth forms of degree n in 4 variables, (r-1)(d-1) = 3(n-1), useless for 024.
  - Neither controls the singular locus of a restriction in about k^2 variables, which is what 024 needs.
- **103/104** ask for a bound on the integer roots -1..-N of a signed sum of K >= 2 powers of T-sparse integer
  polynomials.
  - Our hitting sets (CUE_GCT P-02, P-07) give a nonvanishing point in a small set, not a root count on a progression.
  - Our sparse-polynomial work over finite fields lives in characteristic p, where X^p - X is 2-sparse with p roots. So
    DIV has no finite-field analogue to borrow from, and none of that work transfers.
- **The circuit methods of `L_meta_647_PARTIAL_PROOF.md`** are statements about Boolean monotone circuits: the normal
  form of one-sided circuits, the vertex cover of first-AND centres, the reads identity, and a Nechiporuk-type count for
  rectangle-free relations. The only GCT rows with a covering flavour are the riffle rows, and there the Boolean
  analogue is trivial: a Boolean riffle term inside the support of [a = b][c = d] covers a single point, so the
  Boolean riffle rank is n^2. Over a field the rows are decided by linear algebra (5.5). No transfer.

### 5.9 Work queue for agents (ranked by what it would change)
1. **086 (held by us).** Routes R1-R3 of 5.1. First deliverable: set up the hyper-level problem of (d), compute it
   exactly for small (q, m, n), and look for a recursion in q.
   Read: MAPPING_AGENT_RESULTS section 1, `desk/CODEX_TO_CLAUDE_L_GCT_086.md`, `chatgpt_gct.md`.
2. **091.** An exact certificate for LS(4) = 5 in the Klein chart, with 214, 216 and 217 cutting the cases; or a
   6-dimensional space, which would refute 2n - 3 at n = 4 and settle 185.
3. **195, 196, 210.** A structural four-row lemma (178 + 202 + Lemma K on modes); or searches for 187 and 190 that break
   the Klein symmetry.
4. **025.** Read the September 2026 cubic manuscript (cited by arXiv:2610.40484 = ECCC TR26-287) and decide whether its
   smooth-restriction step can be done without spectral curves and a Severi bound. It is the only step between the fleet
   and its stated target.
5. **011.** A barrier note of section 5.7 (where obstructions cannot exist) and the formal c <= 2 case, ready for the
   board if it opens rows.
6. **Ready proofs waiting for a desk handout:** 116 (Lean, accepted locally), 211 (paper), 122 (Lean), 139 and 125
   (paper) and 140 (finite identity); 126 is already in the repository.

Bookkeeping for the shared board: 181 and 182 are decided by 215 and 216. Proofs are accepted only for steps the desk
hands out, and our handle holds at most five.

## Appendix: checked GCT ids by line (135)
- **A (Hessian / subspace / determinant basics), 47:** 001-010, 012-015, 018-022, 031, 032, 035, 044, 050-052, 055,
  061-072, 075, 076, 079, 081 (not faithful), 082, 085, 087, 169.
- **B (smooth forms), 26:** 023, 024, 027, 029, 030, 034, 038-043, 045-049, 053, 054, 056-060, 073, 074.
- **C (level spaces), 57:** 077, 080, 083, 084, 088-090, 092, 094, 098-102, 105-112, 114, 118-121, 123, 134, 142,
  151-153, 156-159, 163, 170, 171, 175-178, 180, 189, 193, 197, 198, 202, 208, 212-217. Outside proofs among them:
  105-112, 114, 118-121, 123, 134, 142, 151-153, 180, 189, 193, 197, 198, 202, 208, 212-217.
- **E (algebraic), 1:** 150. **F (riffle), 4:** 095-097, 218.
- Red-team restatements, counted in A and B: 054, 068, 073, 076, 082.

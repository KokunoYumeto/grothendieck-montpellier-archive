# The intake pile against the pequalnp.com fleet's graph

From session 672ae3a0 (Claude Opus 5.5 at effort max), 24-25 Nov 2026, for the main session's intake pile and the conference that reads it.

**Data.**
- Our mirror of data.pequalnp.com: 5645 lemmas, refreshed hourly.
- The fleet's Lean tree at upstream commit 9d8b1ae.
- Statuses and statements below are generated from that mirror, not typed.
- Any lemma can be looked up with `python -I -B <local>/pequalnp_work/fleet_mirror/fleet_lookup.py --id <id>`.

**Method.**
1. Every fleet id named in the pile and in the main session's intakes (`fleet_mirror/INTAKE_FLEET_MAPS.md`).
2. Term-weighted matching of all 530 items against all lemmas, read pair by pair (`fleet_mirror/PILE_CANDIDATES.tsv`). It found no further link: shared words, different mathematics.
3. Targeted searches of the fleet by topic:
   - L-functions, GRH and ERH;
   - finite-field construction;
   - primality and factoring;
   - counting classes;
   - the Nullstellensatz and AM;
   - identity testing;
   - multiplicities;
   - border rank;
   - read-1 circuits;
   - alternating forms;
   - Beigel-Tarui.

**The GCT overlap.** It is mapped in a4348514's MAP_COMPLEXITY.md. The gct rows here give the fleet's exact statements and statuses, to be read side by side, not a second mechanism.

## 1. What the fleet's graph does not contain

No lemma on any of these (0 hits each):
- L-functions, GRH, ERH or zero-free regions;
- finite-field construction;
- primality or factoring;
- counting classes (#P, ParityP, Mod_pP);
- the Nullstellensatz or AM;
- polynomial identity testing (its 'hitting set' nodes are about MCSP);
- Kronecker or plethysm multiplicities, or the GCT VI positivity hypotheses;
- border rank (its 'border' is border determinantal complexity).

So most of the pile has no fleet node. The following are knowledge the fleet does not have:
- Alpöge's theorem and its algorithmic consequences (CX_GRH);
- #SAT mod p as a Frobenius scalar (COUNTING_VARIETIES, NEG_NIGHT);
- the GCT VI refutations (GCT_POS, GCT_NSRH);
- the border-rank bounds (BR_PENCIL, GCT_GINEQ, GCT_OBS).

The links concentrate on four areas:
- edge-function circuits (paper 4 of SPLIT_ZERO_AFTER_FGJM);
- GCT (border determinantal complexity, level spaces, riffle rank, the DIV hypotheses);
- three proof-complexity and ACC0 nodes;
- the projective-plane families.

## 2. Open fleet nodes that our checked results settle (on paper)

**L-meta-647** (conjecture since 23 Nov 13:21 UTC, 0 attempts).
- Settled by paper 4's one-sided theorem, both runs. The first run was read step by step by a2fedc2a (Claude Fable 5.2 at effort max).
- Also settled by our own proof of 23 Nov.
- Remark (a)-(c) in the public entry X-meta-005 (pequalnp-mirror commit d1464a4) checks that the posted Lean statement falls under both.

**L-meta-2239** (conjecture since 24 Nov 07:46 UTC, 0 attempts). Planes of order q, read-1 circuits: exactly N(q + 2) - 1.
- *Lower bound.* The fleet's own L-meta-2237 (checked 24 Nov 18:29 UTC: read-1 circuits on a 4-cycle-free graph need |E| + tau - 1 gates) applied to the incidence graph, with three facts:
  - it has no 4-cycle, since two points share one line;
  - it has |E| = N(q + 1);
  - every vertex cover has at least N vertices. Each point lies on q + 1 lines, because the other q^2 + q points fall q to a line through it, so every vertex has degree q + 1.
- *Upper bound.* The star circuit on the N points (L-meta-154): for each point, an AND of it with the OR of its q + 1 lines, then an OR of the N terms. It is read-1, and N(q + 1) + N - 1 = N(q + 2) - 1.
- *Independently,* paper 4's read-one proposition (first run; thm:main in the second) proves the lower bound for every 4-cycle-free graph.
- *Checks.* The proposition was read step by step by a2fedc2a (Claude Fable 5.2 at effort max). The degree count and the read-1 check of the star circuit are mine.
- Public entry: X-meta-006, pequalnp-mirror commit f8123ad.

**L-meta-2237** (checked) states the same thing as paper 4's read-1 case. The fleet merged its Lean proof first; paper 4 should cite it.

**Sharpened, not settled: L-meta-612 and L-meta-608.**
- Paper 4's second run (thm:main, thm:twomissing, thm:threemissing; checked by the run only) shows that a circuit beating |E| + vc - 1 lifts to a polynomial in Sup(G) with at least four edges lacking a quadratic witness.
- The one-sided theorem, applied to both sides, adds that a bipartite counterexample must have a monomial with two distinct variables of each side.
- L-meta-2585 and its negation L-meta-2635 are both open. If 2585 held, then with 2237 it would give 612 for incidence graphs.

**Elementary nodes, not ours to settle.** The TRACTABLE nodes our runs use are classical or elementary and need only Lean: L-gct-126, 128, 129, 138, 149, 154; L-pcx-091, 092.
- L-gct-126 already has a merged proof in the fleet's repository (commit 7dc6cc2, PR #2, 23 Nov, `ring`), but its record still says conjecture.

**L-gct-139** (riffle rank >= 2n - 1). GCT_GINEQ F-13 is claimed to specialize to it after the atom translation PNP-MBR:A2. The translation is unchecked here and belongs to MAP_COMPLEXITY.

## 3. Per cluster

### AG_POLISH

- **SPLIT_ZERO_AFTER_FGJM, paper 4 thm:onesided (both runs)** -> L-meta-647 (conjecture). *settles (paper).* 647's AND condition is syntactic X-degree <= 1, so every monomial has at most one X-variable; one-input and constant gates removed without growth; size >= |E| + vc - 1 (remark (a)-(c) in X-meta-005). Our side: first run read step by step by a2fedc2a (Claude Fable 5.2 at effort max); our own 23 Nov proof (two derivations and a targeted step check, Claude Opus 5.5 at effort max); public: pequalnp-mirror X-meta-005, commit d1464a4.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 prop:readone (first run) = thm:main read-1 case (second run)** -> L-meta-2239 (conjecture). *settles (paper).* lower bound: the fleet's checked L-meta-2237 (or our prop:readone) on the incidence graph, which has no 4-cycle (two points share one line), |E| = N(q+1), and every vertex cover >= N (each point lies on q+1 lines, so every vertex has degree q+1); upper bound: the star circuit of the N points (L-meta-154), read-1, size N(q+2) - 1. Our side: prop:readone read step by step by a2fedc2a (Claude Fable 5.2 at effort max); the degree count and the read-1 check of the star circuit by Claude Opus 5.5 at effort max (this map).
- **SPLIT_ZERO_AFTER_FGJM, paper 4 prop:readone / thm:main read-1 case** -> L-meta-2237 (checked). *same statement (fleet checked first).* read-1 AND/OR circuits for the edge function of a 4-cycle-free graph need |E| + tau - 1 gates; the fleet's Lean proof was merged 24 Nov 18:29 UTC; paper 4 should cite it. Our side: as above.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 thm:twomissing, thm:threemissing (second run, cp08 19:40 / cp10)** -> L-meta-612 (conjecture), L-meta-608 (conjecture). *sharpens (paper).* by thm:main (Mon(f_G) = min over Sup(G) of the arithmetic complexity), a circuit with fewer than |E| + vc - 1 gates lifts to a P in Sup(G); thm:threemissing forces at least four edges with no quadratic witness in P. Our side: proved by the second run with a same-model audit; not checked by another model.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 thm:onesided applied to both sides** -> L-meta-612 (conjecture), L-meta-608 (conjecture). *sharpens (paper).* a bipartite counterexample must have a monomial with two distinct X-variables and one with two distinct Y-variables. Our side: as for 647.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 thm:threemissing** -> L-meta-2585 (conjecture), L-meta-2635 (conjecture). *consistent, neither settled.* 2585 (any circuit for 4-cycle-free incidence can be made read-1 without growth) with the checked 2237 would give 612 for incidence graphs; threemissing says a circuit beating the count is far from read-1 (>= 4 edges without a quadratic witness). Our side: second run only.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 Lemma 4.1 (OR-only Boolean sums)** -> L-meta-529 (checked). *strengthens a checked node.* sum (|S_i| - 1) OR gates even with AND gates and constants; 529 counts all gates. Our side: first run, read by a2fedc2a; also step 4 of X-meta-005.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 Thm 1.2 / thm:main** -> L-meta-606 (conjecture), L-meta-608 (conjecture), L-meta-612 (conjecture). *reformulates.* Mon(f_G) = min over Sup(G) of Arith(P): the three node questions become arithmetic questions; support criterion credited to Jukna. Our side: first run, read by a2fedc2a.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 Prop 6.1 (flat count)** -> L-meta-613 (checked). *same statement, attribution.* the literature source is the proof of Amano-Maruoka's Theorem 5. Our side: first run, read by a2fedc2a.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 Petersen example** -> L-meta-584 (checked). *explains a checked node.* four edges are covered only by monomials with a square; #OR >= |E| - 1 fails there while the total does not. Our side: recomputed by a2fedc2a.
- **SPLIT_ZERO_AFTER_FGJM, paper 4 sections 9-10** -> L-meta-608 (conjecture), L-meta-612 (conjecture), L-meta-650 (conjecture), L-meta-655 (retired), L-meta-582 (conjecture). *pruning for searches.* a minimum counterexample has no terminal product, no common mask and no private mask; with H_X 4-cycle-free every output monomial has at most three marked variables. Our side: first run, statement level in the intake.
- **POLISH_ALGEBRAIC_GEOMETRY, Paper 2 G1 (AG-05 bridge)** -> L-pcx-071 (conjecture). *parallel (constructed).* integral transvections act on quadratic refinements of the Weil pairing with two orbits (Arf 0, 1) and no fixed point for rank >= 4: route M, node M3 (Arf maps on theta characteristics). Our side: run; intake map, not graded.
- **POLISH_ALGEBRAIC_GEOMETRY, P90a, Theorem 2/3 (AG-06)** -> L-gct-025 (conjecture). *parallel (constructed).* marks where characteristic-2 vanishing fails: reduction mod 2 and specialization of smoothness. Our side: P90a v2 posted (hexagon:2611.00936); map not graded.
- **POLISH_TOPOLOGY_PERIODS, S20 note Lemma 6 (indicator power step), map M1** -> L-clb-033 (conjecture), L-clb-002 (checked), L-clb-009 (conjecture), L-clb-010 (conjecture). *parallel (constructed), input.* raising to Q^m is the amplifier x -> x^(p^k) (0/1 mod p to 0/1 mod p^(k+1), degree p^k, prime-power moduli); Beigel-Tarui have degree 2k - 1; completion: replace by the Toda polynomial and keep the degree budget. Our side: S20 posted (hexagon:2611.00937); map not graded.
- **NEG_NIGHT / COUNTING_VARIETIES, NN-C005, C023, C024; CV-THM-MAIN; CV-SP-*** -> no fleet node. *no node.* the fleet's graph has no counting-class node (#P, ParityP, Mod_pP: 0 hits); #SAT mod p as a Frobenius scalar of a smooth Calabi-Yau hypersurface would be a new node. Our side: CV-THM-MAIN core lemmas checked by the pile's intake.
- **NEG_NIGHT, NN-G032..G037 (GCT VIII E_3 lifts)** -> L-gct-011 (conjecture). *no direct node; nearest.* GCT VIII positivity is not in the graph. Our side: checked by a8d75352.
- **NIGHT_GROTHENDIECK_QUESTIONS (via its intakes), cp04 Part A; cp13 Part A** -> L-gct-126 (conjecture), L-gct-154 (conjecture), L-gct-149 (conjecture). *uses / nearest.* the ring identities of the algebraic route and the Kronecker exponent; L-gct-126 already has a merged proof in the fleet's repository (commit 7dc6cc2, PR #2, 23 Nov: ring) while its record still says conjecture. Our side: intake map.

### ALPOGE

- **CX_GRH / BEYOND_DIRICHLET / ALP_MACHINE, CX-N01..N04, N13, N15; BD-R22..R24** -> no fleet node. *no node.* the fleet's graph has no GRH-, ERH- or L-function-conditional node (0 hits) and no primality, factoring or Nullstellensatz/AM node: Miller-Bach primality, r-th nonresidues and primitive roots from A (Alpoge's theorem) are knowledge the fleet does not have. Our side: CX-N13 checked by af2a18f6 and again.
- **ALP_MACHINE, AM-S4 (cp55 intake)** -> L-gct-011 (conjecture). *parallel.* barrier-type statement toward the separation target. Our side: intake map.

### DERIVATEURS

- Everything else: no fleet node: localizers, derivators, reversible closures and free monoids have no node in a graph about circuits, proof systems and algebraic complexity.

### GCT

- **CUE_GCT, R-14 (H14)** -> L-gct-011 (conjecture). *parallel (see MAP_COMPLEXITY).* four-row multiplicity obstructions for padded permanent against determinant when c_m + 3 > 2n^2 + 2. Our side: proved; intake TPC.
- **GCT_KRON, A-030 (H13), F-025, M-008, O-018, M-013, F-021** -> L-gct-011 (conjecture). *parallel (see MAP_COMPLEXITY).* an occurrence obstruction per_n against det_n without padding (A-030); row conditions for multiplicity obstructions in the BIP range. Our side: A-030 proved, intake TPC+COMP.
- **GCT_OBS, QC-014, QC-019 (+S-025), S-004** -> L-gct-011 (conjecture). *parallel (see MAP_COMPLEXITY).* no <= 4-row multiplicity obstruction for padded per_4 against det_n, n >= 7; independent padding row cap. Our side: intake TPC(+COMP).
- **CUE_GCT, ctx-G13** -> L-gct-010 (checked), L-gct-028 (conjecture), L-gct-070 (checked), L-gct-074 (checked), L-gct-056 (checked). *correction to the run's text.* the run calls border dc(perm_m) >= m^2/2 the established bound; the fleet has Lean-checked (2m^2 - 10m + 11)/3 (070) and 'exceeds R m^2 for every R' (074, 056). Our side: intake.
- **CUE_GCT, P-02** -> L-gct-129 (conjecture), L-gct-103 (conjecture), L-gct-104 (conjecture). *parallel, undecided.* whether character-point hitting sets give DIV-type bounds. Our side: primer level.
- **GCT_GINEQ / BR_PENCIL, F-13 (border substitution); P-01** -> L-gct-139 (conjecture). *specialization claimed (see MAP_COMPLEXITY).* F-13's proof works verbatim for exact decompositions with any atoms; after the atom translation PNP-MBR:A2 it gives riffle rank of [a=b][c=d] >= 2n - 1; P-01 needs the torus degeneration to transfer to border riffle rank (PNP-MBR:A4). Our side: F-13 intake TPC+COMP; translation unchecked.
- **BR_PENCIL / GCT_GINEQ / GCT_OBS, R-05, R-08, R-10 (H03); F-23; BR-006** -> no fleet node. *no node.* the fleet's GCT has no border-rank node ('border' there is border determinantal complexity). Our side: H03 posted.
- **GCT_POS / GCT_NSRH, K-023 (H02b), F34** -> L-gct-011 (conjecture). *no direct node; nearest.* numerical PH3 (GCT VI Hyp. 3.3.4) fails for Kronecker coefficients; GCT VI Hyp. 1.6.4(2) false: the GCT VI hypotheses are not in the graph. Our side: K-023 checked by the main session and intake.
- **CUE_GCT, I-18, P-11** -> no fleet node. *no node.* the fleet's hitting-set nodes concern MCSP, not identity testing. Our side: intake TPC.

### HODGE

- **HODGE_FINISH, Q11** -> L-pcx-092 (conjecture). *parallel.* minimum rank 24 of the induced pairing on Lambda^2 V for invariant alternating four-forms on F2^4, against 2 dim U <= dim V + rank. Our side: run; statement level.
- Everything else: apart from Q11, no fleet node: Weil classes, CM fourfolds and sixfolds.

### LONGUE_MARCHE_A

- Everything else: no fleet node: Grothendieck-Teichmüller, loop equations, Fermat towers and sections.

### LONGUE_MARCHE_B

- Everything else: no fleet node: anabelian sections, Torelli chains, profinite completions.

### SWEEP3_A

- Everything else: no fleet node: local cohomology, Chow groups, Picard categories, CM comparisons.

### SWEEP3_B

- Everything else: no fleet node: Ab^2 autoduality, monodromy mod 2, orthosets, Fuglede-Kadison determinants.

### ZETA_GRH

- **GRH_ALGORITHMS / GRH_ALGORITHMS_FINISH, P144, P145, P126 (hexagon:2611.00987)** -> L-meta-606 (conjecture), L-meta-608 (conjecture), L-meta-612 (conjecture), L-meta-649 (checked), L-meta-650 (conjecture), L-meta-660 (conjecture), L-meta-661 (conjecture), L-meta-766 (conjecture), L-meta-885 (checked), L-meta-2239 (conjecture). *input (ANT-07).* succinct descriptions of the plane families over every prime power q need a presentation of F_{p^r} in time poly(r log p): Lenstra's construction problem, solved here unconditionally for small cyclotomic cofactor and under A at fixed valuation. Our side: paper posted; targeted checks.
- **GRH_ALGORITHMS_FINISH, ANT-07 (characteristic 2)** -> L-meta-664 (checked), L-meta-683 (checked). *input.* characteristic-2 quadratics. Our side: intake map.
- **ZETA_HEAT, prop:fd-certificate-size** -> L-gct-128 (conjecture), L-gct-138 (conjecture). *uses.* the run's certificate-size bound uses the Descartes bounds; both are classical and await Lean on the fleet. Our side: intake map.

## 4. Exact statements and live statuses of every fleet node named above

Open nodes first (29 open of 43).

**L-clb-009** (conjecture since 2026-11-22T13:05:12.855Z; attempts 0; seat None; used by 0): NEXP is not contained in ACC0

```
∃ L : Language Bool, (∃ (R : Set (List Bool × List Bool)) (k : ℕ), PEqualNP.Library.DecidableInPolyTime PEqualNP.Library.encodePair R ∧ ∀ x : List Bool, x ∈ L ↔ ∃ w : List Bool, w.length ≤ 2 ^ (x.length ^ k + k) ∧ (x, w) ∈ R) ∧ L ∉ PEqualNP.CircuitLowerBounds.ACC0
```

**L-clb-010** (conjecture since 2026-11-22T13:05:12.895Z; attempts 0; seat None; used by 0): NQP is not contained in ACC0

```
∃ L : Language Bool, (∃ (R : Set (List Bool × List Bool)) (k : ℕ), PEqualNP.Library.DecidableInPolyTime PEqualNP.Library.encodePair R ∧ ∀ x : List Bool, x ∈ L ↔ ∃ w : List Bool, w.length ≤ 2 ^ (Nat.log 2 x.length ^ k + k) ∧ (x, w) ∈ R) ∧ L ∉ PEqualNP.CircuitLowerBounds.ACC0
```

**L-clb-033** (conjecture since 2026-11-22T19:27:21.826Z; attempts 1; seat None; used by 0): Modulus-amplifying polynomials (Beigel and Tarui): degree 2k - 1 turns 0 and 1 mod m into 0 and 1 mod m^k

```
∀ m k : ℕ, 1 ≤ k → ∃ F : Polynomial ℤ, F.natDegree ≤ 2 * k - 1 ∧ ∀ x : ℤ, ((m : ℤ) ∣ x → (m : ℤ) ^ k ∣ F.eval x) ∧ ((m : ℤ) ∣ x - 1 → (m : ℤ) ^ k ∣ F.eval x - 1)
```

**L-gct-011** (conjecture since 2026-11-22T13:11:02.777Z; attempts 0; seat None; used by 0): Mulmuley-Sohoni separation conjecture (open target of the program)

```
∀ c : ℕ, 1 ≤ c → ∃ m₀ : ℕ, ∀ m : ℕ, m₀ ≤ m → PEqualNP.Gct.paddedPerm ℂ m (m ^ c) ∉ PEqualNP.Gct.orbitClosure (PEqualNP.Gct.detPoly ℂ (m ^ c + 1))
```

**L-gct-025** (conjecture since 2026-11-22T18:25:10.970Z; attempts 3; seat None; used by 1): The permanent of size 11k restricts to a smooth form of degree at least k/3 in about k^2/100 variables

```
∀ k : ℕ, 128 ≤ k → ∃ (r d : ℕ) (G : MvPolynomial (Fin d) ℂ) (g : Fin (11 * k) × Fin (11 * k) → MvPolynomial (Fin d) ℂ), k ≤ 3 * r ∧ k ^ 2 ≤ 100 * d + 100 ∧ G.IsHomogeneous r ∧ (∀ x : Fin d → ℂ, (∀ i, MvPolynomial.eval x (MvPolynomial.pderiv i G) = 0) → x = 0) ∧ (∀ i, (g i).totalDegree ≤ 1) ∧ MvPolynomial.bind₁ g (PEqualNP.Gct.permPoly ℂ (11 * k)) = G
```

**L-gct-028** (conjecture since 2026-11-22T19:28:35.044Z; attempts 2; seat None; used by 0): Border Mignon-Ressayre plus one: border dc(perm_m) >= m^2/2 + 1 for m >= 3 (open here)

```
∀ m n : ℕ, 3 ≤ m → PEqualNP.Gct.HasBorderDetExpression (PEqualNP.Gct.permPoly ℂ m) n → m ^ 2 + 2 ≤ 2 * n
```

**L-gct-103** (conjecture since 2026-11-22T23:23:11.213Z; attempts 0; seat None; used by 0): OPEN: divisibility hypothesis DIV(3, 27/25): a short signed sum of 3th powers of T-sparse integer polynomials has at most T^(27/25) roots at -1..-N

```
∀ c : ℕ, ∃ N₀ : ℕ, ∀ (T K N : ℕ), N₀ ≤ T → K ≤ (Nat.log 2 T) ^ c → ∀ (s : Fin K → ℤ) (g : Fin K → Polynomial ℤ), (∀ i, s i = 1 ∨ s i = -1) → (∀ i, (g i).support.card ≤ T) → (∑ i, Polynomial.C (s i) * g i ^ 3) ≠ 0 → (∏ j ∈ Finset.range N, (Polynomial.X + Polynomial.C ((j : ℤ) + 1))) ∣ (∑ i, Polynomial.C (s i) * g i ^ 3) → N ^ 25 ≤ T ^ 27
```

**L-gct-104** (conjecture since 2026-11-22T23:23:14.561Z; attempts 0; seat None; used by 0): OPEN: divisibility hypothesis DIV(4, 6/5): a short signed sum of 4th powers of T-sparse integer polynomials has at most T^(6/5) roots at -1..-N

```
∀ c : ℕ, ∃ N₀ : ℕ, ∀ (T K N : ℕ), N₀ ≤ T → K ≤ (Nat.log 2 T) ^ c → ∀ (s : Fin K → ℤ) (g : Fin K → Polynomial ℤ), (∀ i, s i = 1 ∨ s i = -1) → (∀ i, (g i).support.card ≤ T) → (∑ i, Polynomial.C (s i) * g i ^ 4) ≠ 0 → (∏ j ∈ Finset.range N, (Polynomial.X + Polynomial.C ((j : ℤ) + 1))) ∣ (∑ i, Polynomial.C (s i) * g i ^ 4) → N ^ 5 ≤ T ^ 6
```

**L-gct-126** (conjecture since 2026-11-22T23:27:26.734Z; attempts 0; seat None; used by 0): TRACTABLE: Fischer's identity at M = 3: 24 x y z = (x+y+z)^3 - (x+y-z)^3 - (x-y+z)^3 + (x-y-z)^3 in every commutative ring

```
∀ (R : Type) [CommRing R] (x y z : R), 24 * x * y * z = (x + y + z) ^ 3 - (x + y - z) ^ 3 - (x - y + z) ^ 3 + (x - y - z) ^ 3
```

**L-gct-128** (conjecture since 2026-11-22T23:27:40.882Z; attempts 0; seat None; used by 0): TRACTABLE: weak Descartes over the reals: a nonzero real polynomial has at most (number of monomials - 1) distinct positive roots

```
∀ (p : Polynomial ℝ) (S : Finset ℝ), p ≠ 0 → (∀ x ∈ S, 0 < x ∧ Polynomial.eval x p = 0) → S.card + 1 ≤ p.support.card
```

**L-gct-129** (conjecture since 2026-11-22T23:27:46.845Z; attempts 0; seat None; used by 0): TRACTABLE: the K = 1 case of L-gct-103: if (X+1)(X+2)...(X+N) divides g^M for a nonzero integer polynomial g then N + 1 <= number of monomials of g

```
∀ (M N : ℕ) (g : Polynomial ℤ), 1 ≤ M → g ≠ 0 → (∏ j ∈ Finset.range N, (Polynomial.X + Polynomial.C ((j : ℤ) + 1))) ∣ g ^ M → N + 1 ≤ g.support.card
```

**L-gct-138** (conjecture since 2026-11-22T23:31:33.010Z; attempts 0; seat None; used by 0): TRACTABLE: Descartes for real exponents: a nonzero real combination of N powers x^(a_i) has at most N - 1 distinct positive zeros

```
∀ (N : ℕ) (a c : Fin N → ℝ) (S : Finset ℝ), StrictMono a → (∃ i, c i ≠ 0) → (∀ x ∈ S, 0 < x ∧ ∑ i, c i * x ^ (a i) = 0) → S.card + 1 ≤ N
```

**L-gct-139** (conjecture since 2026-11-22T23:34:00.583Z; attempts 0; seat None; used by 0): TRACTABLE: riffle rank of [a = b][c = d] on n indices is at least 2n - 1 (the measure's identity case is known through a code bridge)

```
∀ (F : Type) [Field F] (n r : ℕ), 1 ≤ n → PEqualNP.RiffleRank.RiffleRankLe r (PEqualNP.RiffleRank.pairId (Fin n) F) → 2 * n - 1 ≤ r
```

**L-gct-149** (conjecture since 2026-11-22T23:51:00.430Z; attempts 0; seat None; used by 0): TRACTABLE: Kronecker exponent: E = sum alpha_j 2^j has binary digit sum at most sum alpha_j, and 2E <= (sum alpha_j) 2^n

```
∀ (n : ℕ) (α : Fin n → ℕ), (Nat.digits 2 (∑ j, α j * 2 ^ (j : ℕ))).sum ≤ ∑ j, α j ∧ 2 * ∑ j, α j * 2 ^ (j : ℕ) ≤ (∑ j, α j) * 2 ^ n
```

**L-gct-154** (conjecture since 2026-11-23T00:06:02.171Z; attempts 0; seat None; used by 0): TRACTABLE: (g+e)^3 + (g-e)^3 + 2(e^2 f - g)^3 = 6 e^2 g (1 + f g) - 6 e^4 g f^2 + 2 e^6 f^3 in every commutative ring

```
∀ (R : Type) [CommRing R] (g e f : R), (g + e) ^ 3 + (g - e) ^ 3 + 2 * (e ^ 2 * f - g) ^ 3 = 6 * e ^ 2 * g * (1 + f * g) - 6 * e ^ 4 * g * f ^ 2 + 2 * e ^ 6 * f ^ 3
```

**L-meta-2239** (conjecture since 2026-11-24T07:46:51.196Z; attempts 0; seat None; used by 0): Plane of order q, read-1 AND/OR circuits of fan-in exactly two for incidence: least size exactly N(q + 2) - 1, the cover term included

```
∀ (q N : ℕ) (I : Fin N → Fin N → Prop) [DecidableRel I], 2 ≤ q → N = q ^ 2 + q + 1 → (∀ l : Fin N, (Finset.univ.filter (fun p => I p l)).card = q + 1) → (∀ p1 p2 : Fin N, p1 ≠ p2 → ∃! l1 : Fin N, I p1 l1 ∧ I p2 l1) → (∀ C : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.TopForm.IsAO2 (N + N) C → (∀ z : Fin (N + N) → Bool, PEqualNP.MetaComplexity.circuitFun (N + N) C z = decide (∃ p3 l3 : Fin N, I p3 l3 ∧ z (Fin.castAdd N p3) = true ∧ z (Fin.natAdd N l3) = true)) → PEqualNP.ReadK.IsReadK (N + N) C 1 → N * (q + 2) ≤ C.size + 1) ∧ (∃ D : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.TopForm.IsAO2 (N + N) D ∧ (∀ z2 : Fin (N + N) → Bool, PEqualNP.MetaComplexity.circuitFun (N + N) D z2 = decide (∃ p4 l4 : Fin N, I p4 l4 ∧ z2 (Fin.castAdd N p4) = true ∧ z2 (Fin.natAdd N l4) = true)) ∧ PEqualNP.ReadK.IsReadK (N + N) D 1 ∧ D.size + 1 = N * (q + 2))
```

**L-meta-2585** (conjecture since 2026-11-24T09:00:58.791Z; attempts 0; seat None; used by 0): 4-cycle-free incidence: every fan-in-two AND/OR circuit for it can be replaced by a read-1 one with at most as many gates

```
∀ (P L : ℕ) (I : Fin P → Fin L → Prop) [DecidableRel I] (C : PEqualNP.CircuitLowerBounds.Circuit), (∀ p p' : Fin P, ∀ l l' : Fin L, p ≠ p' → l ≠ l' → ¬ (I p l ∧ I p l' ∧ I p' l ∧ I p' l')) → PEqualNP.TopForm.IsAO2 (P + L) C → (∀ z : Fin (P + L) → Bool, PEqualNP.MetaComplexity.circuitFun (P + L) C z = decide (∃ p : Fin P, ∃ l : Fin L, I p l ∧ z (Fin.castAdd L p) = true ∧ z (Fin.natAdd P l) = true)) → ∃ D : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.TopForm.IsAO2 (P + L) D ∧ (∀ y : Fin (P + L) → Bool, PEqualNP.MetaComplexity.circuitFun (P + L) D y = decide (∃ p : Fin P, ∃ l : Fin L, I p l ∧ y (Fin.castAdd L p) = true ∧ y (Fin.natAdd P l) = true)) ∧ D.size ≤ C.size ∧ PEqualNP.ReadK.IsReadK (P + L) D 1
```

**L-meta-2635** (conjecture since 2026-11-24T09:08:21.813Z; attempts 0; seat None; used by 0): It is false that: 4-cycle-free incidence: every fan-in-two AND/OR circuit for it can be replaced by a read-1 one with at most as many gates

```
¬ (∀ (P L : ℕ) (I : Fin P → Fin L → Prop) [DecidableRel I] (C : PEqualNP.CircuitLowerBounds.Circuit), (∀ p p' : Fin P, ∀ l l' : Fin L, p ≠ p' → l ≠ l' → ¬ (I p l ∧ I p l' ∧ I p' l ∧ I p' l')) → PEqualNP.TopForm.IsAO2 (P + L) C → (∀ z : Fin (P + L) → Bool, PEqualNP.MetaComplexity.circuitFun (P + L) C z = decide (∃ p : Fin P, ∃ l : Fin L, I p l ∧ z (Fin.castAdd L p) = true ∧ z (Fin.natAdd P l) = true)) → ∃ D : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.TopForm.IsAO2 (P + L) D ∧ (∀ y : Fin (P + L) → Bool, PEqualNP.MetaComplexity.circuitFun (P + L) D y = decide (∃ p : Fin P, ∃ l : Fin L, I p l ∧ y (Fin.castAdd L p) = true ∧ y (Fin.natAdd P l) = true)) ∧ D.size ≤ C.size ∧ PEqualNP.ReadK.IsReadK (P + L) D 1)
```

**L-meta-582** (conjecture since 2026-11-23T12:09:14.046Z; attempts 0; seat None; used by 0): Search: a circuit of AND and OR gates with at most 26 gates for the edge function of the Heawood graph

```
∃ C : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.MetaComplexity.Monotone2 C ∧ C.size ≤ 26 ∧ (∀ x : Fin 14 → Bool, (C.eval (List.ofFn x) = true ↔ ∃ u v : Fin 14, (u.val, v.val) ∈ ([(0, 7), (0, 8), (0, 10), (1, 7), (1, 9), (1, 13), (2, 8), (2, 12), (2, 13), (3, 7), (3, 11), (3, 12), (4, 10), (4, 11), (4, 13), (5, 9), (5, 10), (5, 12), (6, 8), (6, 9), (6, 11)] : List (ℕ × ℕ)) ∧ x u = true ∧ x v = true))
```

**L-meta-606** (conjecture since 2026-11-23T12:42:10.914Z; attempts 0; seat None; used by 0): Conjecture: circuits of AND and OR gates for the edge function of a graph with no cycle shorter than 5 have size linear in the number of edges

```
∃ c : ℕ, ∀ (n : ℕ) (G : SimpleGraph (Fin n)) [DecidableRel G.Adj], (∀ (v : Fin n) (p : G.Walk v v), p.IsCycle → 5 ≤ p.length) → ∀ D : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.MetaComplexity.Monotone2 D → PEqualNP.MetaComplexity.circuitFun n D = (fun x : Fin n → Bool => decide (∃ i j : Fin n, G.Adj i j ∧ x i = true ∧ x j = true)) → G.edgeFinset.card ≤ c * (D.size + 1)
```

**L-meta-608** (conjecture since 2026-11-23T12:42:20.044Z; attempts 0; seat None; used by 0): Conjecture: circuits of AND and OR gates for the edge function of a graph with no cycle shorter than 5 have at least edges + cover - 1 gates

```
∀ (n : ℕ) (G : SimpleGraph (Fin n)) [DecidableRel G.Adj], (∀ (v : Fin n) (p : G.Walk v v), p.IsCycle → 5 ≤ p.length) → ∀ D : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.MetaComplexity.Monotone2 D → PEqualNP.MetaComplexity.circuitFun n D = (fun x : Fin n → Bool => decide (∃ i j : Fin n, G.Adj i j ∧ x i = true ∧ x j = true)) → ∃ T : Finset (Fin n), (∀ i j : Fin n, G.Adj i j → i ∈ T ∨ j ∈ T) ∧ G.edgeFinset.card + T.card ≤ D.size + 1
```

**L-meta-612** (conjecture since 2026-11-23T12:42:39.115Z; attempts 0; seat None; used by 0): Graphs without a 4-cycle: every circuit of AND and OR gates for the edge function has at least |E| + tau - 1 gates

```
∀ (n t : ℕ) (G : SimpleGraph (Fin n)) (C : PEqualNP.CircuitLowerBounds.Circuit), (∃ u v : Fin n, G.Adj u v) → (∀ a b c d : Fin n, a ≠ b → a ≠ c → a ≠ d → b ≠ c → b ≠ d → c ≠ d → G.Adj a b → G.Adj b c → G.Adj c d → ¬ G.Adj d a) → (∃ S : Finset (Fin n), PEqualNP.MetaComplexity.CoverPromise.IsVertexCover G S ∧ S.card = t) → (∀ S : Finset (Fin n), PEqualNP.MetaComplexity.CoverPromise.IsVertexCover G S → t ≤ S.card) → PEqualNP.MetaComplexity.Monotone2 C → (∀ x : Fin n → Bool, (C.eval (List.ofFn x) = true ↔ ∃ u v : Fin n, G.Adj u v ∧ x u = true ∧ x v = true)) → G.edgeSet.ncard + t ≤ C.size + 1
```

**L-meta-647** (conjecture since 2026-11-23T13:21:51.353Z; attempts 0; seat None; used by 0): Bipartite graphs without a 4-cycle: circuits of AND and OR gates in which every AND has an operand free of one side need |E| + tau - 1 gates

```
∀ (n k : ℕ) (G : SimpleGraph (Fin n)) (X : Finset (Fin n)) (C : PEqualNP.CircuitLowerBounds.Circuit), (∀ u v : Fin n, G.Adj u v → (u ∈ X ↔ v ∉ X)) → (∀ a b c e : Fin n, G.Adj a b → G.Adj b c → G.Adj c e → G.Adj e a → a = c ∨ b = e) → (∀ v : Fin n, ∃ w : Fin n, G.Adj v w) → (∀ T : Finset (Fin n), (∀ i j : Fin n, G.Adj i j → i ∈ T ∨ j ∈ T) → k ≤ T.card) → PEqualNP.MetaComplexity.Monotone2 C → (∃ S : Set ℕ, (∀ l ∈ X, l.val ∈ S) ∧ (∀ (j : ℕ) (g : PEqualNP.CircuitLowerBounds.Gate), C.gates[j]? = some g → ∀ i ∈ g.inputs, i < n + j → i ∈ S → n + j ∈ S) ∧ (∀ (j : ℕ) (g : PEqualNP.CircuitLowerBounds.Gate), C.gates[j]? = some g → g.op = PEqualNP.CircuitLowerBounds.GateOp.and → ∀ a b : ℕ, g.inputs = [a, b] → a < n + j → b < n + j → ¬ (a ∈ S ∧ b ∈ S))) → (∀ x : Fin n → Bool, C.eval (List.ofFn x) = true ↔ ∃ u v : Fin n, G.Adj u v ∧ x u = true ∧ x v = true) → G.edgeSet.ncard + k ≤ C.size + 1
```

**L-meta-650** (conjecture since 2026-11-23T13:26:56.103Z; attempts 0; seat None; used by 0): Search: a circuit of AND and OR gates with at most 63 gates for the point-line graph of the projective plane of order 3

```
∃ C : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.MetaComplexity.Monotone2 C ∧ C.size ≤ 63 ∧ (∀ x : Fin 26 → Bool, (C.eval (List.ofFn x) = true ↔ ∃ u v : Fin 26, (u.val, v.val) ∈ ([(0, 13), (0, 14), (0, 16), (0, 22), (1, 13), (1, 15), (1, 21), (1, 25), (2, 14), (2, 20), (2, 24), (2, 25), (3, 13), (3, 19), (3, 23), (3, 24), (4, 18), (4, 22), (4, 23), (4, 25), (5, 17), (5, 21), (5, 22), (5, 24), (6, 16), (6, 20), (6, 21), (6, 23), (7, 15), (7, 19), (7, 20), (7, 22), (8, 14), (8, 18), (8, 19), (8, 21), (9, 13), (9, 17), (9, 18), (9, 20), (10, 16), (10, 17), (10, 19), (10, 25), (11, 15), (11, 16), (11, 18), (11, 24), (12, 14), (12, 15), (12, 17), (12, 23)] : List (ℕ × ℕ)) ∧ x u = true ∧ x v = true))
```

**L-meta-660** (conjecture since 2026-11-23T13:55:45.199Z; attempts 0; seat None; used by 0): Plane of order 8: one list of AND, OR, NOT gates of fan-in at most two with at most one NOT computing all 73 line-ORs has at least 98 gates

```
∀ (gates : List PEqualNP.CircuitLowerBounds.Gate) (out : Fin 73 → ℕ), (∀ g ∈ gates, (g.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.or ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.not) ∧ g.inputs.length ≤ 2) → (∀ i j : Fin gates.length, (gates.get i).op = PEqualNP.CircuitLowerBounds.GateOp.not → (gates.get j).op = PEqualNP.CircuitLowerBounds.GateOp.not → i = j) → (∀ (w : Fin 73) (x : Fin 73 → Bool), PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates, out w⟩ (List.ofFn x) = decide (∃ v ∈ (({0, 1, 3, 7, 15, 31, 36, 54, 63} : Finset (Fin 73)).image (fun u => u + w)), x v = true)) → 98 ≤ gates.length
```

**L-meta-661** (conjecture since 2026-11-23T13:57:46.698Z; attempts 0; seat None; used by 0): Plane of order 7: one list of AND, OR, NOT gates of fan-in at most two with at most one NOT computing all 57 line-ORs has at least 70 gates

```
∀ (gates : List PEqualNP.CircuitLowerBounds.Gate) (out : Fin 57 → ℕ), (∀ g ∈ gates, (g.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.or ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.not) ∧ g.inputs.length ≤ 2) → (∀ i j : Fin gates.length, (gates.get i).op = PEqualNP.CircuitLowerBounds.GateOp.not → (gates.get j).op = PEqualNP.CircuitLowerBounds.GateOp.not → i = j) → (∀ (w : Fin 57) (x : Fin 57 → Bool), PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates, out w⟩ (List.ofFn x) = decide (∃ v ∈ (({0, 1, 3, 13, 32, 36, 43, 52} : Finset (Fin 57)).image (fun u => u + w)), x v = true)) → 70 ≤ gates.length
```

**L-meta-766** (conjecture since 2026-11-23T16:19:39.106Z; attempts 0; seat None; used by 3): Circuits with at most s NOT gates for the ORs of a family of d-point sets need at least a recursively defined number of gates

```
∀ (n m d : ℕ) (S : Fin m → Finset (Fin n)) (kappa : ℕ → ℕ), ((∀ i : Fin m, (S i).card = d) ∧ (∀ i j : Fin m, i ≠ j → (S i ∩ S j).card ≤ 1) ∧ (∀ (b : ℕ) (y : Finset (Fin n)), y.card ≤ b → (Finset.univ.filter (fun w : Fin m => ¬ Disjoint (S w) y)).card ≤ kappa b)) → ∀ (s b K : ℕ) (y : Finset (Fin n)) (gates : List PEqualNP.CircuitLowerBounds.Gate) (out : Fin m → ℕ), y.card ≤ b → (∀ g ∈ gates, (g.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.or ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.not) ∧ g.inputs.length ≤ 2) → (∃ ι : Fin s → Fin gates.length, ∀ i : Fin gates.length, (gates.get i).op = PEqualNP.CircuitLowerBounds.GateOp.not → ∃ j : Fin s, ι j = i) → (∀ (w : Fin m) (x : Fin n → Bool), Disjoint (S w) y → (∀ p ∈ y, x p = true) → (Finset.univ.filter (fun p : Fin n => x p = true ∧ p ∉ y)).card ≤ K → PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates, out w⟩ (List.ofFn x) = decide (∃ v ∈ S w, x v = true)) → (Nat.rec (motive := fun _ : ℕ => ℕ → ℕ → ℕ) (fun b' K' : ℕ => (m - kappa b') * min K' (d - 1)) (fun (_ : ℕ) (g : ℕ → ℕ → ℕ) (b' K' : ℕ) => (List.range (K' + 1)).foldr (fun (j acc : ℕ) => max acc (min (g (b' + j) (K' - j)) (g b' j))) 0) s b K) ≤ gates.length
```

**L-pcx-071** (conjecture since 2026-11-22T21:38:04.701Z; attempts 1; seat seat-clb-1; used by 0): OPEN TARGET: dag-like Res(+) is not polynomially bounded on CNFs of constant width and constant F2 polynomial calculus degree

```
∃ w d : ℕ, ∀ p : Polynomial ℕ, ∃ (n : ℕ) (F : Finset (PEqualNP.ProofComplexity.Clause (Fin n))), (∀ C ∈ F, C.card ≤ w) ∧ PEqualNP.ProofComplexity.PCRefutable (PEqualNP.ProofComplexity.cnfSystem (↑F : Set (PEqualNP.ProofComplexity.Clause (Fin n)))) d ∧ ∀ π : List (PEqualNP.ProofComplexity.LinClause (Fin n)), PEqualNP.ProofComplexity.IsLinRefutation (↑F : Set (PEqualNP.ProofComplexity.Clause (Fin n))) π → p.eval n < π.length
```

**L-pcx-092** (conjecture since 2026-11-23T00:59:35.188Z; attempts 0; seat None; used by 0): TRACTABLE: in a nondegenerate alternating space over F2, 2 dim U is at most dim V plus the rank of the form on U

```
∀ (n : ℕ) (B : LinearMap.BilinForm (ZMod 2) (Fin n → ZMod 2)) (U : Submodule (ZMod 2) (Fin n → ZMod 2)), B.Nondegenerate → (∀ v, B v v = 0) → 2 * Module.finrank (ZMod 2) U ≤ n + (Module.finrank (ZMod 2) U - Module.finrank (ZMod 2) (U ⊓ B.orthogonal U : Submodule (ZMod 2) (Fin n → ZMod 2)))
```

**L-clb-002** (checked since 2026-11-22T13:06:22.159Z; attempts 1; seat seat-clb-1; used by 0): AC0 is contained in ACC0

```
PEqualNP.CircuitLowerBounds.AC0 ⊆ PEqualNP.CircuitLowerBounds.ACC0
```

**L-gct-010** (checked since 2026-11-22T14:59:31.265Z; attempts 1; seat seat-barrier-1; used by 1): Landsberg, Manivel and Ressayre: border dc(perm_m) >= m^2/2

```
∀ m n : ℕ, PEqualNP.Gct.HasBorderDetExpression (PEqualNP.Gct.permPoly ℂ m) n → m ^ 2 ≤ 2 * n
```

**L-gct-056** (checked since 2026-11-22T17:52:28.520Z; attempts 1; seat seat-clb-1; used by 0): Superquadratic: border determinantal complexity of perm_m is not O(m^2)

```
∀ R m0 : ℕ, ∃ m : ℕ, m0 ≤ m ∧ 1 ≤ m ∧ ∀ n : ℕ, PEqualNP.Gct.HasBorderDetExpression (PEqualNP.Gct.permPoly ℂ m) n → R * m ^ 2 ≤ n
```

**L-gct-070** (checked since 2026-11-22T18:08:15.817Z; attempts 1; seat seat-barrier-1; used by 0): TARGET: border dc(perm_m) >= (2m^2 - 10m + 11)/3, the border form of L-gct-064

```
∀ m n : ℕ, 3 ≤ m → PEqualNP.Gct.HasBorderDetExpression (PEqualNP.Gct.permPoly ℂ m) n → 2 * m ^ 2 + 11 ≤ 3 * n + 10 * m
```

**L-gct-074** (checked since 2026-11-22T18:01:56.833Z; attempts 1; seat seat-clb-1; used by 0): Border determinantal complexity of perm_m exceeds R m^2 for all large m, for every R

```
∀ R : ℕ, ∃ m0 : ℕ, ∀ m n : ℕ, m0 ≤ m → PEqualNP.Gct.HasBorderDetExpression (PEqualNP.Gct.permPoly ℂ m) n → R * m ^ 2 ≤ n
```

**L-meta-2237** (checked since 2026-11-24T18:29:06.834Z; attempts 1; seat seat-intake-1; used by 0): Read-1 AND/OR circuits of fan-in exactly two for the edge function of a 4-cycle-free graph: at least |E| + tau - 1 gates, the cover term included

```
∀ (n : ℕ) (G : SimpleGraph (Fin n)) [DecidableRel G.Adj] (C : PEqualNP.CircuitLowerBounds.Circuit), PEqualNP.TopForm.NoFourCycle G → PEqualNP.TopForm.IsAO2 n C → (∀ x : Fin n → Bool, PEqualNP.MetaComplexity.circuitFun n C x = decide (∃ u v : Fin n, G.Adj u v ∧ x u = true ∧ x v = true)) → PEqualNP.ReadK.IsReadK n C 1 → ∃ T : Finset (Fin n), (∀ u2 v2 : Fin n, G.Adj u2 v2 → u2 ∈ T ∨ v2 ∈ T) ∧ G.edgeFinset.card + T.card ≤ C.size + 1
```

**L-meta-529** (checked since 2026-11-23T10:00:42.104Z; attempts 1; seat seat-intake-1; used by 3): Boolean sums with pairwise intersections of size at most one need sum (|S_w| - 1) monotone gates (known; multi-output, AND and OR allowed)

```
∀ (n m : ℕ) (S : Fin m → Finset (Fin n)), (∀ i j : Fin m, i ≠ j → (S i ∩ S j).card ≤ 1) → ∀ (gates : List PEqualNP.CircuitLowerBounds.Gate) (out : Fin m → ℕ), (∀ g ∈ gates, (g.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.or) ∧ g.inputs.length ≤ 2) → (∀ (w : Fin m) (x : Fin n → Bool), (PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates, out w⟩ (List.ofFn x)) = decide (∃ v ∈ S w, x v = true)) → ∑ w, ((S w).card - 1) ≤ gates.length
```

**L-meta-584** (checked since 2026-11-23T12:31:16.979Z; attempts 1; seat seat-intake-1; used by 0): An explicit circuit of AND and OR gates for the edge function of the Petersen graph has 20 gates, of which 13 are OR gates

```
∀ C : PEqualNP.CircuitLowerBounds.Circuit, C = ({ gates := [⟨PEqualNP.CircuitLowerBounds.GateOp.or, [9, 5]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [0, 9]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [0, 6]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [7, 3]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.and, [1, 12]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [6, 5]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [11, 3]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [13, 1]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [14, 2]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.and, [12, 15]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.and, [4, 16]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.and, [19, 11]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [7, 21]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.and, [18, 17]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [20, 23]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [3, 15]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.and, [25, 8]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.and, [22, 10]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [27, 26]⟩, ⟨PEqualNP.CircuitLowerBounds.GateOp.or, [24, 28]⟩], output := 29 } : PEqualNP.CircuitLowerBounds.Circuit) → PEqualNP.MetaComplexity.Monotone2 C ∧ C.size = 20 ∧ (∃ A : Finset ℕ, A.card = 13 ∧ ∀ j : ℕ, j ∈ A ↔ ∃ g : PEqualNP.CircuitLowerBounds.Gate, C.gates[j]? = some g ∧ g.op = PEqualNP.CircuitLowerBounds.GateOp.or) ∧ (∀ x : Fin 10 → Bool, (C.eval (List.ofFn x) = true ↔ ∃ u v : Fin 10, (u.val, v.val) ∈ ([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9), (5, 7), (6, 8), (7, 9), (8, 5), (9, 6)] : List (ℕ × ℕ)) ∧ x u = true ∧ x v = true))
```

**L-meta-613** (checked since 2026-11-23T13:24:37.019Z; attempts 1; seat seat-intake-1; used by 0): Flat circuits of AND and OR gates on graphs without a 4-cycle: at least |E| + k - 1 gates, k the number of centres of the AND gates

```
∀ (n : ℕ) (G : SimpleGraph (Fin n)) (C : PEqualNP.CircuitLowerBounds.Circuit) (cen : ℕ → Fin n) (A : Finset ℕ), (∀ a b c d : Fin n, a ≠ b → a ≠ c → a ≠ d → b ≠ c → b ≠ d → c ≠ d → G.Adj a b → G.Adj b c → G.Adj c d → ¬ G.Adj d a) → PEqualNP.MetaComplexity.Monotone2 C → (∀ x : Fin n → Bool, (C.eval (List.ofFn x) = true ↔ ∃ u v : Fin n, G.Adj u v ∧ x u = true ∧ x v = true)) → (∀ j : ℕ, j ∈ A ↔ ∃ g : PEqualNP.CircuitLowerBounds.Gate, C.gates[j]? = some g ∧ g.op = PEqualNP.CircuitLowerBounds.GateOp.and) → (∀ j ∈ A, ∀ x : Fin n → Bool, (C.wires (List.ofFn x)).getD (n + j) false = true → (∃ u v : Fin n, G.Adj u v ∧ x u = true ∧ x v = true) ∧ x (cen j) = true) → (∀ j ∈ A, ∀ i ∈ A, ¬ Relation.TransGen (fun a b : ℕ => b < a ∧ ∃ h : PEqualNP.CircuitLowerBounds.Gate, C.gates[a]? = some h ∧ n + b ∈ h.inputs) j i) → G.edgeSet.ncard + (A.image cen).card ≤ C.size + 1
```

**L-meta-649** (checked since 2026-11-23T15:07:47.466Z; attempts 1; seat seat-lib-1; used by 2): Line-degree at most 2: circuits of AND and OR gates for point-line incidence with no two points on two common lines need (incidences - 2N) / 48 gates

```
∀ (N : ℕ) (I : Fin N → Fin N → Prop) [DecidableRel I] (C : PEqualNP.CircuitLowerBounds.Circuit), (∀ p p' l l' : Fin N, p ≠ p' → l ≠ l' → ¬ (I p l ∧ I p l' ∧ I p' l ∧ I p' l')) → PEqualNP.MetaComplexity.Monotone2 C → PEqualNP.CircuitLowerBounds.HasLineDegree (N + N) (Finset.Ico N (N + N)) C 2 → (∀ z : Fin (N + N) → Bool, PEqualNP.MetaComplexity.circuitFun (N + N) C z = true ↔ ∃ p l : Fin N, I p l ∧ z (Fin.castAdd N p) = true ∧ z (Fin.natAdd N l) = true) → (Finset.univ.filter (fun e : Fin N × Fin N => I e.1 e.2)).card ≤ 48 * C.size + 2 * N
```

**L-meta-664** (checked since 2026-11-23T14:44:34.839Z; attempts 1; seat seat-intake-1; used by 0): Anisotropic quadratic form in characteristic 2: on every affine line of F x F the values landing in an additive subgroup A number 0 or |A|

```
∀ (F : Type) [Field F] [Fintype F] [DecidableEq F] [CharP F 2] (b : F), (∀ X : F, X ^ 2 + b * X + 1 ≠ 0) → ∀ (A : AddSubgroup F) [DecidablePred (· ∈ A)] (p d : F × F), d ≠ 0 → ((Finset.univ.filter (fun t : F => (p + t • d).1 ^ 2 + b * (p + t • d).1 * (p + t • d).2 + (p + t • d).2 ^ 2 ∈ A)).card = 0 ∨ (Finset.univ.filter (fun t : F => (p + t • d).1 ^ 2 + b * (p + t • d).1 * (p + t • d).2 + (p + t • d).2 ^ 2 ∈ A)).card = Nat.card A) ∧ (p = 0 → (Finset.univ.filter (fun t : F => (p + t • d).1 ^ 2 + b * (p + t • d).1 * (p + t • d).2 + (p + t • d).2 ^ 2 ∈ A)).card = Nat.card A)
```

**L-meta-683** (checked since 2026-11-23T15:19:24.924Z; attempts 1; seat seat-intake-1; used by 0): In every finite field of characteristic 2 some quadratic X^2 + bX + 1 has no root

```
∀ (F : Type) [Field F] [Fintype F] [CharP F 2], ∃ b : F, ∀ x : F, x ^ 2 + b * x + 1 ≠ 0
```

**L-meta-885** (checked since 2026-11-23T18:44:27.684Z; attempts 1; seat seat-intake-1; used by 4): Conditional: ORs of a plane-like family by AND, OR, NOT gates with at most T NOT gates, each reading a monotone wire: an explicit lower bound

```
(∀ (n m k : ℕ) (S : Fin m → Finset (Fin n)) (C : PEqualNP.CircuitLowerBounds.Circuit) (o : Fin m → ℕ) (c : Fin m → ℕ), (∀ i j : Fin m, i ≠ j → (S i ∩ S j).card ≤ 1) → (∀ i : Fin m, 2 ≤ (S i).card) → (∀ g ∈ C.gates, (g.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.or) ∧ g.inputs.length = 2) → (∀ (i : Fin m) (p : Fin n), (C.wires (List.ofFn (fun q : Fin n => decide (q = p)))).getD (o i) false = true ↔ p ∈ S i) → (∀ (i : Fin m) (x : Fin n → Bool), (Finset.univ.filter (fun q : Fin n => x q = true)).card ≤ k → (∀ q ∈ S i, x q = false) → (C.wires (List.ofFn x)).getD (o i) false = false) → (∀ i : Fin m, c i ≤ k) → (∀ i : Fin m, c i + 1 ≤ (S i).card) → ∑ i : Fin m, c i ≤ C.size) → (∀ (n : ℕ) (gates : List PEqualNP.CircuitLowerBounds.Gate) (T Z : Finset (Fin n)), (∀ g ∈ gates, (g.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.or) ∧ g.inputs.length ≤ 2) → ∃ (gates' : List PEqualNP.CircuitLowerBounds.Gate) (r : ℕ → ℕ), (∀ g ∈ gates', (g.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g.op = PEqualNP.CircuitLowerBounds.GateOp.or) ∧ g.inputs.length = 2) ∧ gates'.length ≤ gates.length ∧ ∀ o : ℕ, (∃ x y : Fin n → Bool, PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates, o⟩ (List.ofFn (fun i => if i ∈ T then true else if i ∈ Z then false else x i)) ≠ PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates, o⟩ (List.ofFn (fun i => if i ∈ T then true else if i ∈ Z then false else y i))) → ∀ x : Fin n → Bool, PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates', r o⟩ (List.ofFn x) = PEqualNP.CircuitLowerBounds.Circuit.eval ⟨gates, o⟩ (List.ofFn (fun i => if i ∈ T then true else if i ∈ Z then false else x i))) → ∀ (nP mL qO : ℕ) (Fam : Fin mL → Finset (Fin nP)), (∀ i1 : Fin mL, (Fam i1).card = qO + 1) → (∀ i7 i8 : Fin mL, i7 ≠ i8 → (Fam i7 ∩ Fam i8).card ≤ 1) → (∀ p1 p2 : Fin nP, p1 ≠ p2 → ∃ i3 : Fin mL, p1 ∈ Fam i3 ∧ p2 ∈ Fam i3) → (∀ p3 : Fin nP, (Finset.univ.filter (fun i4 : Fin mL => p3 ∈ Fam i4)).card = qO + 1) → ∀ (tN kW : ℕ) (L : List PEqualNP.CircuitLowerBounds.Gate) (outW : Fin mL → ℕ), 1 ≤ tN → 1 ≤ kW → (∀ g1 ∈ L, (g1.op = PEqualNP.CircuitLowerBounds.GateOp.and ∨ g1.op = PEqualNP.CircuitLowerBounds.GateOp.or ∨ g1.op = PEqualNP.CircuitLowerBounds.GateOp.not) ∧ g1.inputs.length ≤ 2) → Set.ncard {i5 : Fin L.length | (L.get i5).op = PEqualNP.CircuitLowerBounds.GateOp.not} ≤ tN → (∀ (j1 : ℕ) (g2 : PEqualNP.CircuitLowerBounds.Gate), L[j1]? = some g2 → g2.op = PEqualNP.CircuitLowerBounds.GateOp.not → Monotone (fun x1 : Fin nP → Bool => (g2.inputs.map (fun i6 => (PEqualNP.CircuitLowerBounds.Circuit.wires ⟨L.take j1, 0⟩ (List.ofFn x1)).getD i6 false)).headD false)) → (∀ (w1 : Fin mL) (x2 : Fin nP → Bool), PEqualNP.CircuitLowerBounds.Circuit.eval ⟨L, outW w1⟩ (List.ofFn x2) = decide (∃ v1 ∈ Fam w1, x2 v1 = true)) → ∀ Kb : ℕ, ((tN = 1 ∧ Kb ≤ kW * mL ∧ Kb ≤ qO * mL) ∨ (Kb + kW * (tN * kW * qO + 1) ≤ kW * mL + kW * kW * qO ∧ Kb + qO * (tN * kW * qO + 1) ≤ qO * mL + qO * kW * qO)) → Kb + qO * (tN * kW * qO + 1) ≤ qO * mL → Kb ≤ L.length
```

**L-meta-655** (retired since 2026-11-23T13:30:59.470Z; attempts 0; seat None; used by 0): Search: a circuit with at most 14 gates for the subdivided K4 in which every AND gate has an operand free of one side of the bipartition

```
∃ C : PEqualNP.CircuitLowerBounds.Circuit, PEqualNP.MetaComplexity.Monotone2 C ∧ C.size ≤ 14 ∧ (∃ S : Set ℕ, ((∀ i : ℕ, i < 4 → i ∈ S) ∨ (∀ i : ℕ, 4 ≤ i → i < 10 → i ∈ S)) ∧ (∀ (j : ℕ) (g : PEqualNP.CircuitLowerBounds.Gate), C.gates[j]? = some g → ∀ i ∈ g.inputs, i < 10 + j → i ∈ S → 10 + j ∈ S) ∧ (∀ (j : ℕ) (g : PEqualNP.CircuitLowerBounds.Gate), C.gates[j]? = some g → g.op = PEqualNP.CircuitLowerBounds.GateOp.and → ∀ a b : ℕ, g.inputs = [a, b] → a < 10 + j → b < 10 + j → ¬ (a ∈ S ∧ b ∈ S))) ∧ (∀ x : Fin 10 → Bool, (C.eval (List.ofFn x) = true ↔ ∃ u v : Fin 10, (u.val, v.val) ∈ ([(0, 4), (4, 1), (0, 5), (5, 2), (0, 6), (6, 3), (1, 7), (7, 2), (1, 8), (8, 3), (2, 9), (9, 3)] : List (ℕ × ℕ)) ∧ x u = true ∧ x v = true))
```


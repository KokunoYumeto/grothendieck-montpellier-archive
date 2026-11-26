# Our results against pequalnp.com's open lemmas

By Claude Opus 5.5 at effort high (agent a8d753525905811ab, the GCT field expert), 23 Nov 2026, for session 672ae3a0
(Claude Opus 5.5 at effort max). Read only: no desk requests, pull requests or posts. Static lemma files were fetched
from data.pequalnp.com at under two requests a second.

## What was searched

**Their side:**
- All 68 open GCT lemmas, local in `desk\gct_lemmas\`, statement by statement.
- All 150 other GCT nodes (checked, retired, refuted), from data.pequalnp.com.
- The open non-GCT lemmas that their word index lists under our topic words, all of them read: meta 48, 56, 58, 60, 63,
  70, 92, 174, 315, 444, 446, 488, 639, 646; pcx 76, 77, 78, 81, 86, 89, 92; clb 22, 24, 33, 36; alg 1.
- `Defs\Gct.lean`, `Gct\L074.lean` and the helpers `Gct\Helpers\OrbitClosure.lean`, `BorderSubst.lean` and
  `BorderMR.lean`.
- The topic words were: Kronecker, plethysm, obstruction, multiplicity, border, rank, apolarity, orbit, closure,
  padding, positivity, Schur, Littlewood-Richardson, determinant, permanent, Hessian, Fano, Hasse-Witt, #SAT, parity,
  occurrence, saturation, tensor, symmetric.

**Our side:** the GCT and complexity rows of `field_experts\hexagon\HEXAGON_STATUS.md`: H02, H02b, H03, H13, H14, H20,
H21, H23, GPK08, GPK18 and NEG. Also our intakes of GCT_POS, GCT_KRON, GCT_OBS (checkpoint 15), CUE_GCT, BR_PENCIL and
GCT_GINEQ, and my own E4 and nonstandard GCT work. I opened no file named SAT_WITNESS or SAT_KRONECKER.

## The answer

**No result of ours proves, refutes or implies any open lemma on their board.** Their GCT program has no
representation theory in it. Their index has no hit in the GCT program for "obstruction", "multiplicity", "plethysm",
"Schur", "positivity" or "occurrence". "Kronecker" occurs only as the substitution x_j → X^(2^j) (L-gct-149). The open
GCT work is about:
- level spaces of the permanent;
- linear spaces in the permanent hypersurface;
- root counts of sparse polynomials (Descartes, Wronskians, the DIV hypotheses);
- riffle rank;
- the border-dc chain.

Our GCT results are about multiplicities, Kronecker and plethysm coefficients, GCT VI/VIII, and border rank of the
coefficient tensors. None of these meets their posted steps.

**The one high-value item is not ours but follows from their own checked work.** With one short new lemma, their
target L-gct-011 holds for c = 1 and c = 2 (section 1).

## 1. Ranked matches

### 1.1 L-gct-011, cases c = 1 and c = 2: provable now from their own checked L-gct-074. Usefulness: high for their board; not a result of ours

**Their lemma.** L-gct-011 (open; the target of the program):

```
∀ c : ℕ, 1 ≤ c → ∃ m₀, ∀ m ≥ m₀,
  paddedPerm ℂ m (m ^ c) ∉ orbitClosure (detPoly ℂ (m ^ c + 1))
```

**What gives it.** Their checked L-gct-074 (`Gct\L074.lean`, proved in Lean through `Gct\Helpers\Rung\AllM`):

```
∀ R, ∃ m0, ∀ m n, m0 ≤ m → HasBorderDetExpression (permPoly ℂ m) n → R * m ^ 2 ≤ n
```

**The missing link is the converse of L-gct-006.** It reads: paddedPerm ℂ m n ∈ orbitClosure (detPoly ℂ (n+1)), with
m ≤ n, implies HasBorderDetExpression (permPoly ℂ m) (n+1). It is not in their library: L-gct-006 and
`OrbitClosure.lean` prove only the other direction.

**Proof of the link.**
1. Membership in the orbit closure gives a sequence of invertible g_k. The polynomials linSubst g_k (detPoly (n+1)) are
   determinants of (n+1)×(n+1) matrices with linear entries Σ_j g_ij X_j. They are coefficientwise limits of nothing
   but themselves (use `AlgHom.map_det` through `bind₁`). So by definition HasBorderDetExpression (paddedPerm m n) (n+1).
2. Apply their checked helper `hasBorderDetExpression_bind₁` (`Gct\Helpers\BorderSubst.lean`; its hypotheses are a
   finite variable set and substitutes of total degree at most 1). Use the substitution X(0,0) ↦ 1,
   X(i+1, j+1) ↦ X(i,j) for i, j < m, and every other variable ↦ 0. As m ≤ n, padIndex misses (0,0), and the
   substitution sends paddedPerm m n to permPoly m.

**Conclusion.** For m large, every border determinantal expression of perm_m has size at least 2m². With n + 1 =
m^c + 1 ≤ m² + 1 < 2m² (c ≤ 2, m ≥ 2), the padded permanent is not in the orbit closure. This gives L-gct-011 for
c ∈ {1, 2}. Cases c ≥ 3 need a border-dc bound beyond m³. The claimed cubic bound L-gct-026 (unrefereed) would give c
= 3 at most, and only for c = 3 if its constant exceeds 1.

**What is missing.** The posted node quantifies over all c, so it can't be closed. This needs the board to split it, for
instance a node "L-gct-011 for c ≤ 2", and the converse of L-gct-006 as a node or helper. A Lean proof should be about
60 to 120 lines on their existing helpers and Mathlib (`Matrix.det` under `AlgHom`, `MvPolynomial.bind₁`, finite-type
coefficient convergence as in `BorderSubst.lean`). Nothing of ours is used. Credit it as an observation on their
nodes.

**Bearing on our records (see section 2).** Our GCT texts must not say that the best border-dc bound for the permanent
is m²/2. Their Lean-checked L-gct-074 gives every R·m² for large m.

### 1.2 L-gct-011 for c ≥ 3: our results are barriers to one route, not steps. Usefulness: low to moderate, as context

| Our result | File, id, place | Relation to L-gct-011 |
|---|---|---|
| H14 / CUE_GCT R-14 with R-13 | `research_returns\CUE_GCT_checkpoint_08_20261121T0649Z_unzipped\deliverables\CUE_GCT.tex`, R-14 from line 1238 | Four-row multiplicity obstructions for z^(n−m) per_m against det_n exist when c_m + 3 > 2n² + 2. Those with c_m = C(m+3,3) exist only for m ≤ 16. The board's summary is "gaps exactly when n² ≤ 2m² − m + 1, m ≥ 17". **Barrier:** four-row multiplicity obstructions can't reach n ~ m^c with c ≥ 1 beyond n ≈ √2·m. |
| GCT_OBS QC-014 | `reports_20261122\overnight_intake\GCT_OBS_cp15\text\GCT_OBS.tex`, around line 405; `work\quaternary\quartic_padding_containment.tex` | At (m, n) = (4, n), n ≥ 7, ℓ^(n−4) q ∈ D_(n,4) for every quaternary quartic q. So there is no multiplicity obstruction with at most four rows, in any degree. **Barrier**, same direction. |
| H13 / GCT_KRON A-030, A-034, O-030 | `research_returns\GCT_KRON_checkpoint_07_20261121T0415Z_unzipped\GCT_KRON_work\GCT_KRON.tex`: A-034 lines 9001–9330, O-030 lines 9423–9764 (per our intake) | Occurrence obstructions per_n against det_n with no padding (n = m). Under either padding every O-030 member with u > 0 has q = 0 (GCT_OBS intake, B3). **No step toward c ≥ 1:** the non-membership they witness is already given by their checked L-gct-010 (m²/2 > m). |
| GCT_OBS QC-019 | `GCT_OBS.tex` from line 92 | A multiplicity obstruction for z·per_8 against det_9, at a degree of 59 digits. It is conditional on a certificate with 156 functions. That is c = 1, m = 8 only, and their L-gct-010 already separates (32 > 9). |
| H02, H02b (GCT VI's PH2, SH(a), PH3 fail; numerical PH3 fails for Kronecker coefficients) | `research_returns\GCT_POS_final_20261122T0219Z_unzipped\GCT_POS.tex`, line 201 (H02b); P-F19, P-F31, P-F57 as on the board | **Barrier to the flip route** (Mulmuley's GCT VI) toward L-gct-011. Their program doesn't use the flip, so nothing on the board changes. |
| H23 (GCT VIII Conj. 3.2 has no minimum; unimodality fails at r = 3) | GCT_POS N-012; `reports_20261120\split_zero\consults\E4_RANK_FOUR_20261121.md`, P-F-E3-01 | An erratum to the nonstandard-quantum-group route. Not on their board. |

**Can it be stated in their Lean?** The non-membership consequences can, with orbitClosure, paddedPerm and detPoly. The
results themselves can't without a large addition: GL_N-isotypic multiplicities in coordinate rings, Schur functors,
Kronecker and plethysm coefficients. Mathlib has none of these in usable form. A Lean proof of R-14 would also need
Hilbert polynomials of projective varieties and degree comparison. QC-014's containment ℓ^(n−4)q ∈ orbitClosure(det_n)
**is statable** with their definitions, after renaming four variables into the grid. It would need an explicit
7×7 determinantal family and a limit, which is feasible but long. It would answer no posted node.

### 1.3 L-gct-028 (border dc(perm_m) ≥ m²/2 + 1 for m ≥ 3): weak

Nothing of ours bears on it. GCT_OBS S-002 and S-003 give an explicit equation Ψ separating per_3 from the orbit
closure of det_3. That is border dc(perm_3) ≥ 4, below the m²/2 = 4.5 of their checked L-gct-010.

Their own nodes settle the large-m range: L-gct-072 (checked) gives (2m² − 10m + 11)/3 > m²/2 + 1 for m ≥ 20 (the inequality is m² − 20m + 16 > 0), and
L-gct-074 gives it for m large. So only small m are open. This is an observation, not ours.

### 1.4 H03 (border rank of det_4 and per_4 at least 43 over C; BR_PENCIL R-08, R-10) and GCT_GINEQ F-23: no node

There is no border-rank node in any program: "border" in their GCT program always means border determinantal
complexity. H03 is statable (CP border rank as a limit of rank-r decompositions), but its proof is border apolarity
with 25 computer cases and the enumeration of 1.5 million subsets. That is not a Lean target now.

### 1.5 NEG (parity of #SAT as a Hasse-Witt scalar, ⊕P-hard; one sparse smooth cubic encoding #SAT): no match

The parity lemmas (meta 56, 58, 60, 63, 92, 639; pcx 78, 81, 86, 89, 92) are about MCSP reductions, circuit size of
block parities, Res(+) and F_2 linear algebra. L-clb-033 (Beigel–Tarui modulus amplification) and the "sat" hits
(clb 22, 24, 36; meta 48, 444, 446; alg 1) don't touch the NEG statements.

### 1.6 Everything else: no match

H20, H21 (plethysm formulas), GPK08 and GPK18 (Kronecker series and polytope denominators), my E4 rank-three constants
and the nonstandard Hecke results have no counterpart on any program.

The words "occurrence" (meta 315, 488) and "padding" (meta 174) are false friends: formula leaves, a graph encoding, and
AND-padding of circuits.

## 2. Their checked lemmas that bear on our open items

| Their lemma (checked) | Bears on | How |
|---|---|---|
| L-gct-074, L-gct-056 (border dc(perm_m) ≥ R m² for every R, all large m; Lean `Gct\L074.lean`, `L056.lean`) | The prompt 56 GCT write-up; the H13 and H14 framing; any sentence of ours saying "the best known bound is m²/2" | The state of the art on their board is superquadratic and Lean-checked; with 1.1 it gives Mulmuley–Sohoni non-containment for c ≤ 2. Our obstruction results must be framed as new **witnesses** (representation-theoretic certificates), not as new separations. Before citing it in a paper, read their proof route: the posted plain text calls it "ours, conjecture", with a route through L-gct-053, 024, 023. |
| L-gct-010 (LMR: border dc ≥ m²/2) | GCT_OBS's padded main questions Q1a, Q1b at (8,9) and (17,23) | Both pairs are already separated (32 > 9; 144.5 > 23). Our open item is the existence and explicitness of a representation-theoretic obstruction, not the separation. State this in the next GCT_OBS prompt. |
| L-gct-012, L-gct-020 (Hessian of det_n has rank ≤ 2n on its zero set; the adjugate kills the radical) | GCT_OBS S-003 ("f divides H on seven-variable determinant pencils, since the Hessian of det_3 has rank six at a rank-two matrix") | The rank bound is their checked L-gct-012 at n = 3. A Lean form of our step exists. |
| L-gct-006 with `Helpers\OrbitClosure.lean`; `Defs\Gct.lean` (orbitClosure, paddedPerm, detPoly) | Stating our padded results (O-030, R-14, QC-014, QC-019) formally | These definitions fix the convention: internal padding x_00^(n+1−m) on det_(n+1). Our B3 in the GCT_OBS intake distinguishes internal padding (r ≤ m²) from independent padding (r ≤ m² + 1). Their paddedPerm is internal padding with the pad variable inside the grid, so our m² cap applies. |
| L-gct-024, 029, 045 (smooth forms and power sums: border dc ≥ (r−1)(d−1)/11) | QC-014 (quaternary quartics, border dc ≤ 7 after padding) | Consistent: the bound is (3·3)/11 < 1. No conflict and no gain. |

## 3. Lines added to MATCHES.md

- L-gct-011 (c ≤ 2 only): from their checked L-gct-074 with the converse of L-gct-006. Not ours. It needs the board to
  split the node.
- Survey closed: no open lemma matched by a result of ours. Barrier context for L-gct-011 only.

## 4. Check events

```
statement_id	date	who	type	outcome
pequalnp L-gct-011 c<=2	2026-11-23	Claude Opus 5.5 at effort high, agent a8d753525905811ab	targeted proof check	follows from their checked L-gct-074 plus the converse of L-gct-006 (two-step proof above, via their helper hasBorderDetExpression_bind1); Lean not written
mapping survey	2026-11-23	Claude Opus 5.5 at effort high, agent a8d753525905811ab	carried as background without fault found	all 68 open GCT lemmas and the word-index hits read; no open lemma proved, refuted or implied by our results
```

## Correction (23 Nov 2026, 17:2x UTC; Claude Opus 5.5 at effort max, from the joint-table agent's reading of Defs/Gct.lean)
Section 2 above states the fleet's padding convention the wrong way round. Their `paddedPerm` is x00^(n+1-m) perm_m with the
permanent placed at (i+1, j+1) and `padIndex` avoiding (0,0): the pad variable is NOT a permanent variable. That is the
independent padding of our GCT_OBS S-004 (support cap m^2 + 1), not GCT_KRON's internal padding (X_11 a permanent
variable, cap m^2). S-004 says which of GCT_KRON's row bounds survive the change. Details:
fleet_map/JOINT_GCT_LEMMA_SPACE.md, the paragraph "A convention finding".

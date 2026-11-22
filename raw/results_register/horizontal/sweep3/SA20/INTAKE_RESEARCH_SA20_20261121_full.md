# Full intake of RESEARCH_SA20 (the 210 statements no intake had checked), 22 Nov 2026

By Claude Opus 5.5 at effort max, agent acf08879a01b97ed4: the sweep-3 reader of the cote 119 stretch and author of the
20 Nov intake. Done at the user's word (21 Nov ~23:5x UTC): [the user's words, omitted]. The run is RESEARCH_SA20 by
GPT-6 Astra (ChatGPT Pro mode), final package of 20 Nov 04:04 UTC:
`grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA20_final_20261120T0404Z_unzipped`.

**The list:** the 210 ids of `field_experts/INTAKE_LEDGER.md` §9, row RESEARCH_SA20. The other 57 rows were checked in
the 20 Nov intake (`INTAKE_RESEARCH_SA20_20261120.md`, 51 rows read in full).

**Events:** `INTAKE_RESEARCH_SA20_20261121_full_CHECK_EVENTS.tsv` (382 events after round 3; a row that moved up a
level has a new event, the old one is kept). Scripts and outputs are in `intake_full_work/`: `getrow.py`, `addev.py`,
`count.py`, and my computations `coxnorm.py` (D.002), `bhargava.py` (B.022), `a5011.py` (A5.011), `d021.py` and
`d021b.py` (D.021), `d025.py` (D.025), `a401.py` (A.401), each with its `_out.txt`. All scripts run with
`python -I -B`, outside the return. The running notes are in `agent_notes/acf08879a01b97ed4_NOTES.md`.

## 0. State after round 3 (22 Nov 2026): best level per statement, from the TSV by `count.py`

| Best level reached (rubric) | Rows of the 210 | Ids |
|---|---:|---|
| computation or formal certificate by my own code, with a targeted proof check | 3 | A.401, D.021, D.025 |
| targeted proof check, complete or of the main steps | 138 | all rows not listed elsewhere in this table; D.002 and A5.011 include my own computations |
| targeted proof check, partial (the steps read are listed in each event) | 30 | A.119, A.121, A.122, A.124, A.132, A.135, A.139, A.140, A.142–A.147, A.150–A.152, A.154, A.156–A.159, A.163, A5.010, A5.013, A5.014, B.035, B.059, B.067, B.078 |
| used and rechecked | 5 | A.116, B.036, B.054, D.003, D.004 |
| carried as background without fault found | 24 | A.123, A.125–A.130, A.305, A.306, A6.001–A6.003, A6.007, A6.009, B.004, B.012, B.033, B.034, C.008, C.020, D.014, D.018, D.019, D.027 |
| statement read only | 10 | A.136, A.137, A.141, A.162, A5.017, A5.018, A5.019, B.077, C.U001, C.U002 (the last two are source gates with no mathematical claim) |

Outside the list of 210, the three Hexagon candidates' rows checked on 20 Nov were raised in round 3: A.104 and A.111 by
independent re-proof (7.1, 7.2), B.022 by computation (7.3).

Sections 1 to 6 below are the round-2 record of 22 Nov and are kept as written; section 7 is round 3. Where they
differ, section 0 and section 7 hold.

## 1. What was checked, by type (one row per statement, 210 in all; round 2)

| Check type (rubric) | Rows | Ids |
|---|---:|---|
| targeted proof check (with my own re-proof or computation where noted) | 24 | D.001; D.002 (+ independent computation); D.005 (type A recomputed); D.006; D.007; D.008 (type A); D.012 (+ independent re-proof); D.013 (existence part); D.022 (classical types re-proved); C.001; C.002; C.003; C.005; C.011; C.015; B.002; B.010; B.021; B.064; B.072; B.067 (partial); A5.001; A.303 and A.304 (the argument checked in A.205) |
| used and rechecked | 3 | D.003 (partial), D.004, A.116 (through A.115) |
| carried as background without fault found | 18 | D.014, D.019, D.027, C.008, B.033, B.034, A6.001, A6.002, A6.003, A6.007, A6.009, A.305, A.306, A.123, A.125, A.127, A.128, A.129 |
| statement read only, proof not read | 165 | all the other ids, each listed in the TSV with its statement summary |

Counted with the 20 Nov intake, the 267 statements now stand at:
- 75 with a targeted proof check (51 + 24);
- 3 used and rechecked;
- 22 carried as background (4 + 18);
- 167 at the level of the statement (165, plus A.131 and A.160, which were partly read on 20 Nov).

**The independent computations of this round:**
- **D.002.** My own code (`coxnorm.py`: root systems from Cartan matrices, all intertwiners w with wc = cᵃw preserving
  the roots, W-membership by chamber reduction) recomputes the Coxeter normalizers:
  - |N_W(⟨c⟩)| = 12, 48, 48, 108 and 240 for G₂, F₄, E₆, E₇ and E₈, with exactly h lifts per unit;
  - 5 and 7 mod 12 have no involutive lift (F₄, E₆), and 7, 13, 17 and 23 mod 30 have no lift of order 4 (E₈), so the
    sequence does not split in F₄, E₆, E₈;
  - G₂ and E₇ have cyclic unit groups and lifts of matching order, so it splits there.

  This agrees with the run in every number.
- **D.012.** At the subregular X ∈ 𝔰𝔭₄, d tr(Y²) = 2 tr(C) ≠ 0 and d tr(Y⁴) = 0, so the rank is r − 1 = 1. This
  refutes the letter's guess, as the run says.
- **D.022.** The rank formula in types A, B and C (m − 1 and ⌊m/2⌋) is re-proved from d tr(Yᵏ)_e = k tr(e^{k−1}·).
- **D.005.** The pinned reversal of 𝔰𝔩_{r+1} acts on 𝔤_θ by (−1)^{r+1}, so by −1 exactly in A_{2m}.

## 2. Refuted or corrected

- **No statement of the run was refuted in this round.** Every targeted check confirmed. The run's own refutations that I
  checked hold: D.001 (char 2), D.012 (C₂), C.002 (S^n × Dⁿ), C.005 (n = 1), C.015 (positive twists), B.002 (the
  three-element semigroup) and A5.001 (the Cantor set).
- **Corrections to our own sweep-3 records** (the 20 Nov intake listed six; these add to them):
  - D.008 corrects ae4ae3dc's hunch H20-5. In type A the Borel-giving classes are one block, or two blocks of opposite
    parity, not only [n] and [n−1,1]: for example [3,2] in 𝔰𝔩₅ has weights 2, 1, 0, −1, −2.
  - D.005, now checked in type A, refines H20-4. The sign is −1 only in A_{2m}, not for every A_n.
  - D.001 confirms Grothendieck's own characteristic-two caveat on 123/007, which sweep 3 recorded.

## 3. What is new

- **Against our own results:**
  - D.002 settles his question on 123/002 ("Quelle extension de (ℤ/hℤ)* par ℤ/hℤ obtient-on ?", hunch H20-3 of sweep
    3): the extension splits in A, B, C, D, G₂ and E₇ and does not split in F₄, E₆ and E₈. Its numbers are now
    independently recomputed.
  - D.006–D.008 settle package R20-2 (c), (d).
- **Against the literature:** I made no literature search in this round (the context guard was past 70 %). Whether D.002
  is in print, for instance in the work on regular elements after Springer 1974, is open. The row-by-row "new" claims for
  Part B and for A.119–A.163 rest on the run's own source audits, which I did not repeat.

## 4. Errata and record notes

- **The sort's locators** for A.131 and A.132 point at the scope paragraph (`parametric_concordance.tex:4, :17`). The
  statements are at :2633 and :3044 (as in the 20 Nov intake).
- **D.026 is found twice:** in `agents/lie_theory/notes_D026_pending.tex:2` and in the main part, `part_D.tex`. The
  register should name the one in the paper.
- **C.U001 and C.U002** are in `unchecked_C.tex` under another macro and are not found by the standard statement
  environment. Their status, "source verification pending", stands.

## 5. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

No result of RESEARCH_SA20 passes all five tests today, and none is one gate away with strong timeliness. So there is
nothing to flag at once. Three candidates, each with its gates:

1. **Grothendieck's collar and cone conjectures in the Additif (119/148–150): A.104, A.106, A.111, A.112.**
   - I b), I c) and II b) are false through the concordance space of (S¹)⁶, II c) is true, and five of the eleven
     functors are equivalences.
   - Tests met:
     - complete;
     - self-contained (inputs: π₀C(Tᵈ) ≠ 0, Shiota 2010, Burghelea–Lashof);
     - stable (the run is final);
     - targeted check (20 Nov). My sweep-3 reading derived the I c) failure independently on 18 Nov.
   - Gates left:
     - an independent re-proof of A.104 (the EP failure) and A.111 (II b));
     - a check that the corrected cascade is not in print;
     - a post written from our reading, citing the scans and never reproducing his text.
   - Interest: the archive line, moderate.
2. **B.022 and B.023: Int(k + t^m k[[t]]) is projective, hence flat.** This answers the nonflatness that the run says
   Elliott conjectured (Presentations 2011, introduction p. 2).
   - Tests met: complete (proof checked 20 Nov) and self-contained (Milnor patching, a Bhargava-type basis).
   - Gates left:
     - open the Elliott 2011 locator;
     - search the literature since 2011 to see whether the question was settled;
     - an independent re-proof.
   - Interest: the integer-valued polynomial community, moderate.
3. **D.002: the Coxeter normalizer extension splits exactly outside F₄, E₆ and E₈.**
   - Tests met: complete, and checked (targeted check plus my independent computation).
   - Gates left:
     - a literature search (it may be known);
     - a self-contained write-up with the certificate.
   - Interest: low in general, but it answers a question in his hand (123/002).

**Not candidates:**
- E.008 (the affine-plane triality) is in Cameron 2015 §6 (E.009).
- D.012 and D.019 are known (Brieskorn, Steinberg).
- A.160 and the regularization chain A.147–A.159 are of potential interest but unchecked.
- B.082 is unchecked.

## 6. What remains for a later round

Proof reading of the 165 statement-level rows, in this order:
1. the Part B main results B.033–B.041, B.054–B.056, B.071, B.076 and B.082, and the rest of B.067 (the nonflatness and the tensor isomorphisms);
2. the chain A.147–A.159 behind A.160;
3. A5.008–A5.020;
4. A6.004–A6.010;
5. C.012–C.023;
6. D.009–D.011, D.015–D.017, D.020, D.021, D.023–D.026.

The work file records the procedure (`intake_full_work/getrow.py ID`). After a compaction the next round continues
from this list.

## 7. Round 3 (22 Nov): the Hexagon candidates first, then the statement-level rows

### 7.1 A.104, re-proved independently (Claude Opus 5.5 at effort max, acf08879a01b97ed4)

**Claim.** Let B be a closed definable (or PL) manifold and C(B) the simplicial group of definable homeomorphisms of B × I
that fix B × {1} pointwise (the concordance group, after reversing I). For the bordant pair (X, B₀) = (B × I, B × {0}),
collapsing B₀ gives a map c: G → H from G = Aut(X, B₀) to H = Aut(CB, o), with the cone base B × {1}. Then
hofib(c) ≃ C(B). So c is a weak equivalence only if C(B) is weakly contractible.

**Proof.**
1. Every g ∈ G preserves the intrinsic boundary of the manifold X, and therefore preserves its complementary end
   B × {1}. Restricting to that end gives ρ: G → Homeo(B).
   - ρ has the section f ↦ f × id_I.
   - Its kernel consists of the maps fixing B × {1} pointwise, which is C(B).
   - The map g ↦ (g ∘ (ρ(g) × id)⁻¹, ρ(g)) gives G ≅ C(B) × Homeo(B) as simplicial sets.
2. Every h ∈ H fixes the vertex o. It also preserves the base B × {1}, the boundary of the manifold CB ∖ {o}.
   Restricting to the base gives r: H → Homeo(B).
   - r has the section "cone the map".
   - Its kernel consists of the homeomorphisms of the cone fixing the base and the vertex. The Alexander contraction
     h_s = δ_s h δ_s⁻¹ on radius ≤ s, the identity outside, contracts it, and the contraction is definable.
   - So r is a weak equivalence.
3. Collapse commutes with restriction to the free end: r ∘ c = ρ. Hence hofib(c) ≃ hofib(ρ) ≃ C(B).
4. For B = (S¹)⁶ the group π₀C(B) is nonzero. Its PL, TOP and definable versions agree on π₀, by the inputs of A.103
   and A.113 (Hatcher–Wagoner and its corrections, Burghelea–Lashof, Shiota 2010).

So c is not a bijection on π₀. A nontrivial concordance f is not isotopic to the identity in G, while c(f) lies in the
contractible kernel of r. Hence the collapse PB → EP is not fully faithful at this object: it is not a Dwyer–Kan
equivalence. ∎

**Route.** The argument is the natural one: two split restrictions and the Alexander trick. It reproduces the run's
route; I found no different route. The inputs are published results.

### 7.2 A.111, re-proved independently

**Claim.** Let X = CB with radius in [0,2], vertex o and outer base B × {2}. Let C₁ be the subcone of radius ≤ 1,
H = Aut(X, o), and J ⊂ H the stabilizer of C₁. Then the component of C₁ in the derived space of strict cones,
hofib(BJ → BH), is equivalent to BC(B).

**Proof.**
1. Restriction to the outer base gives J → Homeo(B) and H → Homeo(B). Both are split by coning.
   - The kernel of the second is Alexander-contractible, as in 7.1.
   - Call the kernel of the first J₀.
2. Restricting J₀ to the shell B × [1,2] lands in the maps of the shell that fix B × {2} pointwise and preserve B × {1}.
   This group is C(B), after reversal.
   - The map is split: extend a shell map over C₁ by coning its inner face.
   - Its kernel consists of the maps of C₁ that fix its base and o, which is Alexander-contractible.
   - So J₀ ≃ C(B).
3. The inclusion J → H covers the identity of Homeo(B), and it sends J₀ into the contractible kernel of
   H → Homeo(B). From the fibre sequences BJ₀ → BJ → BHomeo(B) and BH ≃ BHomeo(B), we get hofib(BJ → BH) ≃ BJ₀ ≃ BC(B).
4. Its π₁ is π₀C(B), which is nonzero for B = (S¹)⁶. So the space of strict cones around o is not contractible, and
   II b) fails in this model. The rigidified version is the same, because EPCR → EPC is an equivalence (Alexander,
   A.105). ∎

**Route.** Again the natural argument, the same as the run's. These two re-proofs meet the "independent re-proof" part of
test 4 for candidate 1 of §5, by a different model family (Claude versus GPT-6 Astra), but by the same route.

### 7.3 B.022 and B.023 (Hexagon candidate 2)

- **B.023: targeted proof check, confirmed.**
  - R = k + t^m l[[t]] is free of rank mf over k[[t^m]]; hence it is Noetherian, local and one-dimensional.
  - The Newton basis of Int(R, V) uses mixed digits.
  - The residue functions D₀ = B/tB descend: C₀ ⊗_k l ≅ D₀.
  - The image of Int(R) in D₀ is C₀, by the F^{Q^e} trick. The kernel is t^m B. The patching then goes as in B.022.
- **B.022, computation (my own code, `intake_full_work/bhargava.py`, output `bhargava_out.txt`).** The node lemma of the
  proof holds exhaustively for (q, m) = (2,1), (2,2), (2,3), (3,1), (3,2), up to n = 40 (q = 2) or n = 30 (q = 3):
  - the valuation formula for d_n;
  - Σ_{i<n} v(x − a_i) ≥ v(d_n) for every x in R mod t^M.
- **Candidate 2 now has:** the proof check of 20 Nov; B.023's proof check; this computation. Its remaining gates are the
  Elliott 2011 locator and a literature search since 2011. A re-proof by a different route was not attempted.

### 7.4 Part B main results read in full in round 3 (each a targeted proof check)

| Row | What the proof does |
|---|---|
| B.038 | The derivation obstruction, complete. |
| B.041 | Valuation domains of every rank. The Vandermonde value on 0, a, …, a^d is d(d+1)(d+2)δ/6 (recomputed). The Newton basis gives the principal case. |
| B.055 | Localization by Noetherianity of M/R; completion by flat base change of C_j and finite evaluation kernels. |
| B.056 | C = A + D, D = eC and C ≅ D × A/I. |
| B.071 | Principal maximal ideal: reduction modulo P = ⋂πʲA to a DVR, with the elementwise lifting of tensors. Relies on B.063 (statement level). |
| B.072 | Frobenius-killed maximal ideal (with B.064 checked in round 2). |
| B.076 | Pullbacks with principal conductor in valuation rings: the two epimorphic overrings and the integer-bound exclusion of a proper factor. Relies on B.075 (statement level). |
| B.039 | Main steps: the Akizuki–Reid specialization through B.038. |

None of these failed. B.039 lacks only the membership cq ∈ Int(R) and the tail of its nonfiniteness argument.

### 7.5 The chain behind A.160 (round 3)

| Row | Check | What was read |
|---|---|---|
| A.147 | partial targeted proof check | Definable fixed points; the Hudson-type graph deformation, whose time equation is a contraction with constant cL < 1, with the explicit inverse; terminal support labels with at most k stars. The step through Mnëv's Proposition 57 was not read. |
| A.148 | targeted proof check of the pair argument, given A.147 | One shared construction keeps the two factors equal on E = A₀ × P ∪ X × ∂P; straighten the common part first, then extend separately. |
| A.150 | partial targeted proof check | McShane extension; Valette 2022 Prop. 5.7 (not opened); definable derivative bound. The reparameterization itself was not read. |
| A.151 | partial targeted proof check | The counterexample family is an explicit semialgebraic family of homeomorphisms (slopes in [7/8, 9/8]). The non-reparameterizability proof was not read. |

No step read so far fails. The chain remains the run's most important claim that is not fully checked.

Further chain rows in round 3:

| Row | Check | What was read |
|---|---|---|
| A.153 | targeted, given A.158 | Graph reparameterization by g with the straight-line homotopy. |
| A.155 | targeted, given A.154, A.134, A.113 | The real comparison triangle. |
| A.156 | partial | The PL clock normalization T_D and the mixed Lipschitz estimate. |
| A.157 | partial | The universal finite-join resolution by induction with double mapping cylinders. |
| A.158 | partial | Generic bounded parameter gradients through the Kocel-Cynk–Pawłucki–Valette extension. |
| A.154 | partial | Variation clocks from o-minimal uniform finiteness. |
| A.152G | targeted, given A.148, A.152 | The two directions of the equivalence. |
| A.149 | targeted, given A.160 | See the open point below. |

**Open point (A.149).** The run lost A.149's original proof text and replaced it by a proof from A.160. A.160's proof,
read on 20 Nov, does not use A.149. I searched the files of A.154 and A.156–A.160 for A.149 and found no reference to it (22 Nov). As far as the citations show, the chain is not circular.

- **A.152 (partial).** The compact Lipschitz resolution (Kocel-Cynk–Pawłucki–Valette 2014) and the finite-join metric.
- **A.159 (partial).** The standard-bound transfer of the auxiliary finite PL data.
  - **The crux of the all-field claim** is not verified here: over a non-Archimedean model, the forward parameter bounds
    can be made standard integers.
  - This is the step an independent check of A.159–A.160 must examine first.

### 7.6 The rest of round 3, by part (each row's event in the TSV gives the steps checked)

**A5 (definable stratifications and the maximal triviality locus).**
- Targeted, complete: A5.002, A5.005, A5.006, A5.007, A5.008, A5.009, A5.015, A5.016, A5.020, A5.CVX.pending.
- Targeted, main steps: A5.012.
- A5.011 is targeted, with my own computation of its algebraic certificate (`a5011.py`):
  - the squares mod 23 are as listed, and r² − r + 6 = 6N and r̄ = N + 1 − r hold in ℤ[C₂₃];
  - E² = E;
  - there is no element of norm 2 in ℤ[ω];
  - N(2 − ω) = 8 and h(−23) = 3.
  - So x + x* ↦ 2[J] ≠ 0, and the end-obstruction counterexample stands.
- Partial: A5.010 (the construction), A5.013 (step 1, the logical-compactness reduction), A5.014 (step 1, the
  arc-length replacement estimate with C = 4n(N + 1)).
- Statement level: A5.017, A5.018, A5.019. Their outlines were read; A5.019 is a stated reduction, not a proof of A5.

**A6 (resolution data).**
- A6.004, A6.006, A6.008 and A6.010 are targeted; A6.005 is targeted at the level of its main steps.
- A6.006's refutation was confirmed: on the suspension of ℝP¹, [r, [u:v]] ↦ [r, [ru:v]] has no continuous lift.
- A6.008's two vertex links were recomputed by hand: 3,1,1,1 against 2,2,1,1.

**Part C (singularities and duality).**
- Targeted: C.006, C.007 (Lamotke's identities as given), C.009, C.010 (the topological derivation), C.012, C.013,
  C.014, C.016, C.017, C.018, C.019, C.021, C.022, C.023.
- Background: C.020, a literature comparison whose index substitutions were checked.
- C.U001 and C.U002 are source gates, with nothing mathematical to check.
- All the run's counterexamples in this part were recomputed:
  - C.009: t = x^p/(1 + x);
  - C.017: the five literal errors;
  - C.019: C × ℙ²;
  - C.022: the cubic Veronese and k[[x, y, ε]]/(ε²);
  - C.023: ℙ² ⊔ Spec k.

**Part D (Coxeter elements and apposition quadruples).**
- Targeted: D.009 (the transfer to the base), D.010, D.011, D.015, D.016, D.017, D.020, D.023, D.024, D.026 (the
  uniform Dᵣ argument, plus consistency of the D₄ and E₆ certificates).
- Background: D.018.
- My own code for two rows:
  - D.021 (`d021.py`): the root-value norms of the primitive Coxeter eigenvector agree with the run's: G₂ {12, 36}, E₆
    {36, 144}, E₇ {1728, 5184, 15552}, E₈ {518400}. For F₄ the run's {144, 576} is the transposed-Cartan
    convention (`d021b.py`); the Bourbaki matrix gives {576, 2304}. In every case only primes dividing h occur, which is
    the claim.
  - D.025 (`d025.py`): brute-force orbit counts for n = 3 to 6 give 2, 18, 144 and 7200 classes, of which 0, 8, 0 and
    192 are outer-fixed. These equal the closed form (D25.1). n = 6 goes beyond the run's own checks, and the affine
    count S_n^aff agrees with its closed form for every even n up to 60.

**The rest of Part B (plethories on integer-valued polynomials).** Every remaining row was read.
- Targeted:
  - B.001, B.003, B.005, B.006, B.007, B.011, B.015, B.016, B.018, B.019, B.020;
  - B.024–B.032, B.042–B.053, B.057, B.058, B.060–B.066, B.068–B.070, B.073–B.075, B.079–B.081.
  - Several of these are checks of how the row assembles other rows; each event names those rows.
- Partial: B.059 and B.078.
- Background: B.004 and B.012 (Deligne 1990 and the bialgebroid literature).
- Statement level: B.077, a special case of B.078.
- Main rows checked in full:
  - B.024: every finite-conductor subring of a DVR has projective Int(R). It extends Hexagon candidate B.022.
  - B.045: the nilpotent detector. Its balanced functional and the value u^{2c−r} were recomputed.
  - B.075: infinite-residue cusps.
  - B.063 and B.070: valuation and binomial bases.
- No step read failed.

**A.1(b), A.3, A.4 (concordance spaces, axioms, reconstruction).**
- Targeted:
  - A.301, A.302, A.307, A.309, A.402, A.120 (main steps), A.133, A.134 (main steps), A.138;
  - A.161, an assembly that inherits the open crux of A.159–A.160.
- A.401: my own computation (`a401.py`) confirms that the families are closed under every injective projection up to
  arity 4, while {a} is not in M₁. The refutation stands.
- Background: A.126 (Cerf) and A.130 (Lin–Xie–Zhang 2026).
- Partial: A.119, A.121, A.122, A.124, A.132, A.135, A.139, A.140, A.142–A.146, A.163. These are the long
  four-manifold and surgery rows. Their checks are of definitions, Künneth suspensions and consistency:
  - A.139 at n = 3 reproduces A.132's Ω(TOP(4)/O(4));
  - A.135's fibre Map(B, K(ℤ/2, 1)) agrees with five-dimensional smoothing theory;
  - A.163's kernel H¹(B; ℤ/2) agrees with that fibre.
  - Their cited inputs were not opened: Igusa 2021 and 2025, Galvin 2026, Orson–Powell–Randal-Williams 2026,
    Boyle–Chen–Conway 2025, Hambleton–Milgram–Taylor–Williams 1988.
- Statement level: A.136, A.137, A.141, A.162.

### 7.7 Refuted or corrected in round 3

- **No statement was refuted by me in round 3.** No step I read failed.
- **The run's own refutations that I checked in round 3 hold:**
  - A5.006, A5.011, A6.006, A6.008;
  - C.009, C.017, C.023, and the false margin claim in C.019;
  - D.016, D.020;
  - B.011, B.016;
  - A.301, A.307, A.401;
  - A5.020, the correction of the all-parameters wording in Jelonek's introduction;
  - the obstruction parts of A5.015, B.026, B.043, B.079.
- **A.132** (π₂ P_TOP(S³) = ℤ/2) is checked only in part. Its value agrees with the 5-connectivity of
  TOP(4)/O(4) → TOP/O, from my background knowledge, which I did not reopen.
- **A convention, not an error:** the F₄ norms in D.021 use the transposed Cartan matrix.
- **Open crux, unchanged:** A.159–A.160, whether the forward parameter bounds can be made standard over a
  non-Archimedean model. A.149, A.152G and A.161 inherit it.

### 7.8 Hexagon readiness after round 3 (field_experts/HEXAGON_CANDIDATES.md)

Still no row passes all five tests: none has had the literature check, and none is pressing now. The candidates, with
their gates:

1. **The collar and cone conjectures of the Additif: A.104, A.106, A.111, A.112.**
   - Independent re-proofs of A.104 and A.111 are now done (7.1, 7.2), by a different model family but the same route.
   - Gates left: a literature check that the corrected cascade is not in print; a post from our reading.
2. **Integer-valued polynomial plethories (B.022, B.023, now with B.024 and the whole Part B classification).**
   - Round 3 checked the chain behind the classification at targeted level: B.020, B.024–B.032, B.042–B.053,
     B.057–B.075.
   - B.022 has my computation; B.024 extends it to every finite-conductor subring of a DVR.
   - Gates left:
     - the Elliott 2011 locator;
     - a literature search since 2011 (B.020 and B.042 are classical in substance: Pólya–Ostrowski ideals, Cahen–Chabert);
     - a re-proof of B.022 or B.024 by another route.
   - This is now the strongest candidate of the run.
3. **D.002 and the Coxeter apposition package: D.002, D.015, D.021, D.025, D.026.**
   - My own computations now cover D.002, D.021 and D.025.
   - Gates left: a literature search (Springer 1974 and after) and a write-up.
   - Interest is low outside the archive line, but the package answers questions in his hand (123/002, 123/035).
4. **New in round 3, weaker:**
   - A.133 (whole definable concordance spaces are invariant under elementary extension; checked; it does not depend on
     A.160);
   - A5.015 (an explicit smooth product bundle with no finite Thom a_f stratification; checked by recomputation).
   - Each still needs a re-proof by another route and a literature check.

### 7.9 What remains

- Unread proofs: A.136, A.137, A.141, A.162, A5.017–A5.019, B.077.
- The unread parts of the 30 partial rows, listed in their events. The four-manifold and surgery rows A.119–A.146 and
  A.163 need their cited sources opened.
- The crux of A.159–A.160.

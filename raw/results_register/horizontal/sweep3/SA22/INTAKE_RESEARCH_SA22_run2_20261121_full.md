# Full intake of RESEARCH_SA22_run2 (run 2), statement by statement (22 Nov 2026)

By Claude Opus 5.5 at effort max (agent af3526fc4890c92f1). Requested by the coordinator at the user's word of 21 Nov
~23:5x UTC ("I also want the full intake"). The run is GPT-6 Astra (ChatGPT Pro mode); its return is
`grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA22_run2_final_20261119T2149Z_unzipped`.

**Inputs:**
- the list: field_experts/INTAKE_LEDGER.md section 9 (202 ids of run 2);
- the earlier intake: INTAKE_RESEARCH_SA22_20261120.md. On 20 Nov that intake filed its run-2 events under run 1's
  name. Its 12 run-2 events are carried over here under this run's name.
- this file's check events: `INTAKE_RESEARCH_SA22_run2_20261121_full_CHECK_EVENTS.tsv`. Every event names the run.
  Where run 2 repeats run 1, the event says "done once with run 1's <id>"; the check itself is in the run-1 file.

**Status: complete.** All 202 ids have an event. Scripts: agent_notes/af3526fc4890c92f1_work/hinich_check.py and
rond_check.py, both run with `python -I -B` outside the return.

## 1. Counts (strongest event per id, the 202 listed ids)

| check type | ids |
|---|---|
| computation or formal certificate | 3 |
| independent re-proof (ours) | 16 |
| targeted proof check | 49 |
| used and rechecked | 0 |
| carried as background without fault found | 67 |
| statement level (read only, or read and consistent) | 67 |

- **The 3 computations:**
  - `A:hinich-explicit`, exact residues;
  - `A:SL-GL-presentations`, exact matrices;
  - `B:nonlinear-Artin`, exact orders for m = 5..8.
- **The 16 independent re-proofs:** 8 carried over from our sweeps, and these 8 new ones:
  - `A:inertia-maximality`;
  - `A:reflection-generators`;
  - `A:unordered-stack`, the coarse space at 3;
  - `B:constant-integer-rigidity`;
  - `B:descent-counterexample`;
  - `B:local-Hurewicz`;
  - `B:subject25`, the construction;
  - `B:charzero`, the Betti case.

  The 8 carried over are `A:octahedron`, `A:octahedron-certificate`, `A:fourpoint-groupoid`, `A:real-elliptic`,
  `A:pid-involutions`, `A:real-topology`, `B:betti` and `B:square`.
- About 40 rows repeat run 1 and are recorded as checked once, with run 1.

## 2. Refutations

- **No refutation by us.** No checked statement is wrong.
- **The run's own refutations:** 37 rows in the list. 26 are checked and hold.
  - Part A:
    - `A:04`, as run 1's (0,4) counterexample;
    - `A:pants-cap-dependence`, as run 1's `A2-independence`;
    - `A:MDB-forgetting-admissibility`, given `A:single-cap-with-cusps`;
    - `A:hinich-explicit`;
    - `A:inertia-maximality`;
    - `A:eigenmodule-correction`.
  - Part B:
    - `B:H0-counterexample`, `B:Lie-comparison-counterexample`, `B:constant-integer-rigidity`,
      `B:descent-counterexample`;
    - `B:local-Hurewicz`, `B:nonlinear-Artin`, `B:p-Euler`, `B:pointless`, `B:specialization`, `B:super`;
    - `B:subject16`, `B:subject24`, `B:subject25`.
  - Part C:
    - `C:counterexamples`, `C:functor-counterexamples` (part 1);
    - `C:subject21-torsion-counterexample`, given `C:Goldman-branches`.
  - Four more refuted rows have checks:
    - `A:orange`, `A:octahedron-certificate` and `B:square`, carried over from 20 Nov;
    - `B:Picard-double-fibre`, whose construction was checked today; its conclusion rests on Raynaud's criterion.
- **Refutations at statement level** (11 rows):
  - `B:Lie-comparison-integral-counterexample`, `B:finite-cover-partition-obstruction`;
  - `B:henselized-Cech-obstruction`, `B:nontorsion-rigidity`, `B:nori-base-change-counterexample`;
  - `B:uniform-partition-obstruction`;
  - `C:K-counterexample`, `C:determinant-ordinary-basechange`;
  - `B:ancona-scope` and `B:tau`, both as in run 1;
  - `C:symmetry`, which agrees with our sweep 3.

## 3. What was checked (the new checks)

### `A:hinich-explicit`
- **What the run claims:** an exact holomorphic plumbing of two three-pointed spheres with zero derivative at
  t₀ = 99/101.
- **What we confirmed:**
  - A = 420/569 solves the residue cancellation;
  - the residue sum at A and B is exactly 0;
  - the six poles are distinct, and only A and B lie inside |z| < 1 − ε;
  - the contour integral is 0 numerically.
- **Script:** hinich_check.py.

### `A:SL-GL-presentations`
- **What the run claims:** SL₂(ℤ) = ℤ/4 *_{ℤ/2} ℤ/6, and GL₂(ℤ) = SL₂(ℤ) ⋊ C₂ on orientation-reversing involutions.
- **What we confirmed:** every matrix relation holds, by exact computation.

### `A:unordered-stack`
- **What the run claims:** the coarse space of M_{0,[4]} over R = ℤ[1/2, i] is Spec R[j].
- **What we confirmed:** our reduction-mod-π argument (run-1 file, section 3) gives this at every prime, including 3.

### `A:nodal-q-test`
- **What the run claims:** the outer actions for q and q′ are isomorphic over G_ℚ only when q = q′.
- **What we confirmed:** κ(q′/q) = (1−χ)u says the Kummer class of q′/q is a coboundary, so q′ = q by Kummer
  faithfulness.
- **Not checked:** the graphicity input (Hoshi–Mochizuki), carried as background.

### `A:inertia-maximality` and `A:reflection-generators`
These are confirmed by our own arguments.
- **`A:inertia-maximality`:** the open subgroups ⟨xⁿ⟩ of an inertia group are pairwise non-conjugate.
- **`A:reflection-generators`:** choose ι with ι(c) = c. Then ιT_c is an involution, so T_c = ι(ιT_c).

### `A:canonical-log-model-product`
- **What we confirmed:** ω(E) = O(1,1) is ample on P¹×P¹.

### Smaller Part A checks
- **Rows confirmed:** `A:ordinary-nodal-loss`, `A:fold`, `A:cuspnorm`, `A:shadowdef` and `A:cap-plumbing-equation`.
- **Formulas recomputed:**
  - the horocycle length −2π/log ρ;
  - the ratio t^{−3/2};
  - the tensor Z₊Z₋ = q.

### `B:Lie-comparison-counterexample`
- **What the run claims:** π₂ = ℤ/4 against H₂(N Lie) = (ℤ/2)².
- **What we confirmed:**
  - G is the unit group 1 + at + bt² of R[t]/t³;
  - G(F₂) is cyclic of order 4;
  - the tangent law is additive;
  - K(A,2)_n = A^{C(n,2)}, with normalization A in degree 2.

### `B:local-Hurewicz`
- **What the run claims:** a counterexample to SGA 2 XIII §6 Conjecture A.
- **What we confirmed:**
  - P is the 6-vertex RP²;
  - L = ΣRP² is a Moore space M(ℤ/2,2);
  - the cone X = cL with Y = {v} has H^i_Y(ℤ) = H̃^{i−1}(L) = 0 for i ≤ 3, while π₃^Y = π₂(L) = ℤ/2;
  - the torsion-free repair follows from the Ext/Hom sequences.
- **Not checked:** that this refutes Conjecture A as worded. That rests on the run's reading of SGA 2, which we did not
  open.

### `B:nonlinear-Artin`
- **What the run claims:** Rond's 2005 counterexample.
- **What we confirmed:**
  - ord f(u_m,v_m,w_m) = m² − 4, computed for m = 5..8;
  - an exact zero has w a square;
  - ord(s² + t^p − z²) ≤ p.
- **Script:** rond_check.py.

### `B:constant-integer-rigidity`
- **What the run claims:** an explicit version of AHHR 2024, Example 3.1.
- **What we confirmed:**
  - the completion along the nodal cubic is regular and connected, hence normal, so H¹(X, ℤ) = 0;
  - the normalization sequence gives H¹(Z, ℤ) = ℤ.

### `B:descent-counterexample`
- **What we confirmed:** a G-stable open set containing an origin contains both origins, so it is not separated and
  not affine.

### `B:H0-counterexample`, `B:H1-gate`, `B:Witt-localization-witness`
- **What we confirmed:**
  - the Kummer class of t in H¹(G_m, μ_n);
  - the sheaves Hom and Isom;
  - [f]w = (f^{p^i} w_i).

### `B:p-Euler` and `B:specialization`
- **What we confirmed:**
  - the Hasse invariants in characteristic 5: −2, then 0, then 2t;
  - the discriminant t³ + 3 is a unit.

### `B:super` and `B:pointless`
- **What we confirmed:**
  - `B:super`: the swap is −1 on V ⊗ V, which forces Sym²V = 0;
  - `B:pointless`: the regular-open algebra of ℝ is atomless.

### `B:Picard-double-fibre`
- **What we confirmed:**
  - the construction: the translation (x,y) ↦ (−1/x, y/x²) is free;
  - div(t) = 2C;
  - the universal functions are A.
- **Not checked:** the conclusion, which rests on Raynaud's criterion (`B:subject17`), carried as background.

### `C:subject21-torsion-counterexample`
- **What the run claims:** a quasi-compact, quasi-separated scheme pair that is not separated and not noetherian. It
  has degree-zero comparison for every étale sheaf of sets, but H¹(X, ℤ/n) = 0 ≠ H¹(Z, ℤ/n).
- **What we confirmed:**
  - On T₀ = Spec(A_h/(d)) the element a/(a+b) is an idempotent, since ab = d = 0 there. It splits T₀ into two parts.
  - The clopen-gluing argument for finite covers is correct. W is finite and dominant, hence surjective, so it meets T₀.
  - The two Mayer–Vietoris computations are correct.
  - `C:Nagata-input`: the table of valuations of a = t²/x and b = t^{−7/4}x, recomputed; the Goldman property of N^h;
    the transfer by faithful flatness.
- **Not checked:** the proof of `C:Goldman-branches`. Nagata's ring (1952, with the 1955 correction) is carried as
  background.

### Smaller Part C checks
- **Rows confirmed:** `C:local-curve-avoidance`, `C:determinant-trace-splitting`, `C:proof-correction`,
  `C:squarezero`, `C:A2b-pants-extremes` and `C:counterexamples`.
- **Facts recomputed:**
  - dim A/p = 1;
  - the trace splitting holds iff m is invertible;
  - the exponential-difference expansion;
  - U_{d,σ}U_{e,τ} = U_{d+σe, στ};
  - the Koebe slit and the half-planes;
  - U(ε) = 2ε.

## 4. Gaps left (steps not checked)

**Cap rows of run 2:**
- the general-stratum claims of `A:alltypes` and `A:graph-pi-one`;
- `A:fullcaps`;
- the cusp case of `A:single-cap-with-cusps`;
- `C:A2b-collar`, `C:A2b-gap`, `C:A2b-support-integral` and `C:A2e-nonmonotonicity`.

**Anabelian reconstruction:**
- `A:tangential-anabelian`, beyond its final Kummer step;
- `A:polycurve-coarse-compactification`;
- `A:intrinsic-anabelian-compactification`;
- `A:real-Galois-obstruction`;
- `A:tensor-log-comparison`.

**The henselian-pair theorems of subject 21:**
- `C:henselian-horizontal-proper`, `C:henselian-flat-trait-proper` and `C:henselian-trait-comparison`;
- `C:henselian-noetherian-*`;
- `B:henselian-local-flat-proper`, which is only tested on two examples;
- `C:Goldman-branches`.

**The Knudsen–Mumford determinant rows:**
- `C:graded-determinant-sign`, `C:determinant-incidence` and `C:determinant-basechange-repair`;
- `C:determinant-ordinary-basechange`, a refutation.

**Greenberg and Witt rows:** `B:finite-Greenberg-piecewise` and the partition obstructions.

**Part C (cote 68):**
- the finite systems: `C:C3-coverage-obstruction`, `C:group-classification` and `C:integer-system`;
- `C:K-counterexample`.

**Others:**
- `B:Lie-comparison-integral-counterexample`;
- `B:nori-base-change-counterexample`: its ordinarity is checked, the base change failure is not;
- `B:nontorsion-rigidity`.

## 5. Errata and corrections

- **In the run:** none found in any checked statement.
- **Points to note:**
  - The two runs normalize the j-line differently (j = 256 J). Both are correct over ℤ[1/2, i].
  - Several rows that the run marks "Refuted" are refutations of a claim by a known counterexample:
    - `B:nonlinear-Artin` is Rond 2005;
    - `B:constant-integer-rigidity` is AHHR 2024, Example 3.1.

    The run says so in both cases. They are not new results.

## 6. What is new in run 2 (not in run 1)

- **One cap determines all lengths, with cusps too.** `A:single-cap-all-lengths` was checked on 20 Nov;
  `A:single-cap-with-cusps` is at statement level. `A:MDB-forgetting-admissibility` refutes the admissible-forgetting
  map of 67/075(b) under the cusp reading of 67/081.
- **The explicit Hinich-type critical plumbing** (`A:hinich-explicit`).
- **The arithmetic tensor test** (`A:nodal-q-test`). The bare geometric group loses q; the arithmetic tangential action
  keeps it.
- **Part B counterexamples.** These are the Lie comparison counterexamples over F₂ and over ℤ, and the conical
  counterexample to the local Hurewicz conjecture (`B:local-Hurewicz`). They also include the double-fibre Picard
  example, flat descent over an Artinian base, and the Nori base-change counterexample.
- **Subject 21.** The noetherian henselian-pair results: properness from closed points, and all-degree torsion
  comparison. With them comes the counterexample `C:subject21-torsion-counterexample`, which is not separated and not
  noetherian. The open row `U:henselian-comparison` states what remains.
- **Knudsen–Mumford sign and base-change corrections** (`C:graded-determinant-sign`, `C:determinant-*`), at statement
  level.

## 7. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests), both runs

No entry passes all five tests today.

| # | candidate | 1 complete | 2 self-contained | 3 stable / not known | 4 checked | 5 interest | gates left |
|---|---|---|---|---|---|---|---|
| S22-a | Grothendieck's (0,4) capping map on cote 67 (67/074-082) is not onto; exact image 0 < \|q\| < 16 (`A:04`, `A:04-exact-image`; run 1's `A1-global-refutation`, `A1-small-ranges`) | yes (Koebe) | yes | literature search not done; check Michel Hua's project as a witness | yes: targeted checks of 20 and 22 Nov, two independent runs, our sweep-3 Koebe check | moderate (archive line) | **one gate: a literature search** |
| S22-b | Counterexample to SGA 2 XIII §6 Conjecture A, the local Hurewicz conjecture: the cone over ΣRP² (`B:local-Hurewicz`) | yes, if the conjecture reads as the run quotes it | yes (Hatcher) | literature search not done (Hamm–Lê, Eyral); the elementary nature makes "already known" a real possibility | yes: our independent re-proof and targeted check | moderate to high (a Grothendieck conjecture) | **two gates:** compare the run's statement of Conjecture A with SGA 2's text; a literature search |
| S22-c | Degree-zero henselian comparison does not give H¹ comparison, for a qcqs pair that is not separated and not noetherian (`C:subject21-torsion-counterexample`) | depends on `C:Goldman-branches`, not read | yes (Nagata 1952/1955, Hall–Rydh, Stacks) | literature search not done (Hall–Rydh 2023's question) | targeted check only; no independent re-proof | moderate (specialists) | three gates: check `C:Goldman-branches`; an independent re-proof; a literature search |
| S22-d | The exact image of the capping map on every stable graph, and one cap determines all lengths (`A:graph-radius-domain`, `A:single-cap-all-lengths`) | the A2b-energy positivity step not checked | yes | literature search not done | partial | moderate | check the positivity step and the cusp case; a literature search |
| S22-e | The Lie comparison fails for smooth Kan simplicial schemes: π₂ = ℤ/4 against (ℤ/2)² (`B:Lie-comparison-counterexample`) | yes | yes | literature search not done; which Grothendieck claim it answers (subject and locator) to be pinned | targeted check; the run's script | low to moderate | pin the claim; a literature search; a computation of ours |

**Not candidates:**
- `A:hinich-explicit`: an explicit instance of Hinich 2010's mechanism.
- `B:nonlinear-Artin`: Rond 2005.
- `B:constant-integer-rigidity`: AHHR 2024.
- `B:p-Euler` and `B:super`: textbook counterexamples.

**Flag:**
- S22-a is one gate away (a literature search). Its interest is moderate, not strong, so the flag rule ("tests 1-4, or
  one gate away, and test 5 strong") does not require an immediate flag. It is reported to the coordinator as the
  nearest candidate.
- S22-b, if the gates clear, would be of stronger interest.

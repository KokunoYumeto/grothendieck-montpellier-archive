# Intake of ALPOGE_GCT, part 3: checkpoint 06 (21 Nov 2026)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the main session's request (Claude Opus 5.5 at
effort max). The run is GPT-6 Astra (ChatGPT Pro mode); the run says its effort is not exposed. Part 2 covered
checkpoint 05. Work file: `agent_notes\20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md`.

## 0. Return read and scope

- **Folder:** `research_returns\ALPOGE_GCT_checkpoint_06_20261121T0332Z_unzipped`, the newest present, assembled at
  03:32 UTC. The run is still going. Its second scheduled review (03:02 UTC) recorded "Movement: YES" with a zero
  no-movement count; the next review was due 04:02 UTC.
- **Read since checkpoint 05:** the LEDGER entries from 02:57 to 03:26 UTC; the QUESTIONS rows PL-Q58 to PL-Q62 and
  the states of Q-PH1, Q-PH3, Q-PH3-WEAK, Q-SH-REVISED, Q-NONSTANDARD, Q-ALPOGE-METHOD and Q-CUBIC-*; and the
  CHECK_EVENTS rows after 02:47 UTC for P-F14, P-F15, P-F19, P-F23, P-F24, P-F26, P-F27, P-F28, P-F30 and P-F31.
- **Read in full, with the proof:** the new part of P-F42, from (P-F42t) to (P-F42ak) in
  `work/positivity_cubic_average_upper.tex`, lines 367-700. I also reread P-F34's statement
  (`positivity_fourier_index_gate.tex`) to check the direction of the gate.
- **Read at statement level:**
  - P-F47 to P-F50: Fermat evaluation and Hessian-Cayley support, with PL-Q58 to PL-Q61;
  - P-F48: the SH(b) density scope;
  - P-F51: a definite-U₃ theta source for the E₆ factor;
  - P-F52: the descended positive operator in the actual nonstandard algebra, and P52q-x;
  - P-F53: K3-Hilbert-scheme coefficient spaces;
  - P-F54: polynomial full support for n ≥ 33;
  - P-F55: the cubic-fourfold discriminant from the same theta input.

## 1. Does checkpoint 06 change P-F31, its companions or the gate?

**No.**
- No check event after 02:47 UTC touches P-F31 or its inputs (P-F23, P-F24, P-F26, P-F27, P-F28, P-F30), nor P-F19,
  P-F14 or P-F15.
- The source files of all of them have exactly the sizes they had in checkpoint 05:
  - `positivity_actual_cubic_pole.tex`: 8,921 bytes;
  - `positivity_noncancellation.tex`: 9,721;
  - `positivity_full_cubic_support.tex`: 12,233;
  - `positivity_finite_lift.tex`: 10,019;
  - `positivity_chain_smoothness.tex`: 11,644;
  - `positivity_chain_residue.tex`: 9,042;
  - `positivity_graph_support.tex`: 13,966;
  - `positivity_cubic_counterexample.tex`: 11,021;
  - `positivity_torus.tex`: 10,704.
- Q-PH3 and Q-PH3-WEAK stay "refuted".
- The H02 gate is unchanged: the run's final, plus a literature search.

## 2. Verdicts on the new and changed findings

**The extension of P-F42 (P42t to P42ak): the PH2/SH gate is confined to the lower four fifths of the coefficients.**
Targeted proof check; **confirmed**.

The direction of the gate:
- P-F34 proves a necessary condition, B_n(p) ≥ |A_n(ζ)|, for the literal positivity index p, and likewise at s + 1
  for the saturation index. Here A_n(ζ) is the amplitude of the simple pole at a primitive 2^{n−1}-th root of unity,
  with log₂|A_n| = n⁴/24 + O(n³).
- I checked the Fourier argument behind it. The ζ-component of the shifted constituents is dominated, coefficient by
  coefficient, by their average.
- So a bound U_n ≤ 2^{(1/24−η)n⁴} on the coefficient norm of the pole-at-1 polynomial B_n would force both indices to
  be exponential in n. That would **refute** PH2 and SH(a) for this family.
- Upper bounds on U_n are therefore the refutation route, not a proof route.

What the extension adds, each step checked:
- (P-F42t): the coefficient-wise bound |b_{n,j}| ≤ 8n!·m^{3n}·18^a·(16n³3^n)^{a−j}·n^j/j!. It rests on feasible
  slopes: for an eventually feasible basis, C^{−1}(c1) ≥ 0 and 1ᵀC^{−1} = 1ᵀ/3, so |λ| ≤ n.
- (P-F42z) and (P-F42aa): the pure-cube block form, E = 3d′ annihilating G_J, Hadamard with column norm √5, and
  R′ = (64n⁴5^{n/2})^{−1}. Together they give limsup log₂U_n/n⁴ ≤ log₂5/12 ≈ 0.194. That is still above 1/24 ≈ 0.0417.
- (P-F42ah): the top part of the coefficients, from index ⌈θD⌉ on, has exponent at most (1−θ)log₂5/12. I checked
  this from a − J_n = (1−θ)n³/6 + O(n²) and the successive ratio nR′/(j+1) < 1. At θ = 4/5 the exponent is
  log₂5/60 ≈ 0.0387 < 1/24.
- (P-F42ai) to (P-F42ak): the signed test at polynomial arguments. If p(f_n) or s(f_n) + 1 is at most n^K, then the
  lower polynomial L_n satisfies L_n(x) ≥ (1 − 2^{−ηn⁴/2})|A_n|.

**Statement level only, no fault seen in the statements:**
- P-F47 to P-F50 and P-F54 concern the support of f_n. Every allowed stretch s ≥ ⌈g(10n)^{200}/n⌉ occurs for n ≥ 33.
  That is a statement about support, not about strict indices. P-F47 also uses the supplied Dirichlet GRH: through
  Lamzouri-Li-Soundararajan it gives an explicit p ≤ (φ(n) log n)², used only for the explicit bound. Xylouris gives
  an unconditional polynomial bound, so the support result stands without it.
- P-F48: the cubic families of P-F19 and P-F31 are exponentially sparse in both populations of SH(b) (narrow
  Hypothesis 1.6.5(b) and unified 3.3.2(b)). So they do not refute the density clause SH(b). The run says so,
  correctly.
- P-F51, P-F53, P-F55: fixed-dimensional theta and Borcherds identifications, for the cubic threefold E₆ factor, K3
  Hilbert schemes and the cubic fourfold discriminant of degree 192 (= 6·2⁵, consistent).
- P-F52: the nonstandard (GCT VII) gate is reduced to normalization, the coefficient model and product compatibility.
  P52t-x exclude a simultaneous ordinary λ-ring realization of the trace/norm coefficient objects, and exclude one
  fixed Frobenius over all finite extensions.

**Counts for part 3:** 1 read in full and confirmed (the P-F42 extension); 0 refuted; 0 gaps; 0 changed or withdrawn;
about 10 at statement level.

## 3. What PH2 and SH look like now

**PH2 and SH(a), for irreducible-inner plethysm (Q-SH-REVISED): open.**
- **Toward refutation.** On the cubic family it suffices to show that the lower four fifths of the coefficients of
  B_n have norm at most 2^{(1/24−η)n⁴}, or the signed bound sup_{x ≤ n^K} L_n(x) ≤ (1−ε)|A_n|. Unconditionally, the
  proved exponent for the whole norm is log₂5/12. For the top fifth it is already below the threshold.
- **Toward proof.** Nothing new. P-F12's implication (PH3 ⇒ PH2) has a false premise since P-F31.
- **Calibration.** n = 4 has indices 23 (P-F35, which I recomputed in part 2). That is small, and it is consistent
  with either outcome.

**SH(b), the density clause: untouched and open.** P-F48 shows that the cubic families are too sparse to bear on it.

## 4. What is new

- The P-F42 extension: an explicit, unconditional reduction of the refutation route for PH2/SH to a lower block of
  coefficients. Its tools are elementary (Brion-Vergne type partial fractions, Cauchy estimates, Hadamard). It is new
  as a statement, and refines the run's own P-F34.
- P-F54 and P-F48 are new, and they settle scope questions.
- The theta and Borcherds items are compatibilities of known constructions: Allcock-Carlson-Toledo, Looijenga, Laza,
  Borcherds, Busé-Jouanolou Example 4.10. They are not new theorems.

## 5. Scope of the two proofs

P-F47 uses Alpöge's Dirichlet GRH only to sharpen an explicit prime bound, through Lamzouri-Li-Soundararajan's
GRH-explicit least-prime bound for arithmetic progressions. That is within the theorem's scope. An unconditional
version (Xylouris) is also given. Nothing uses Masullo. No statement claims more than its input gives.

## 6. How the findings bear on the open problems, and the attack they open

1. **The next attack on PH2: bound the lower coefficients of B_n by their geometry.** B_n is the pole-at-1 polynomial
   of the Hilbert series of the cubic invariant ring, and its coefficients are equivariant Riemann-Roch
   (Todd-class) numbers on the GIT quotient P(Sym³V*)//SL_n. The lower coefficients are the lower Todd classes.
   Their size is controlled by the singularity strata of the quotient, which a Kirwan partial desingularization
   resolves. So the attack is to express b_{n,j}, for j < 4D/5, through Kirwan's resolution and the strata of
   strictly semistable cubics, and to bound each stratum's contribution. If they are below 2^{(1/24−η)n⁴}, PH2 and
   SH(a) fail for the cubic family.
2. **SH(b)** needs dense families, not sparse ones. Nothing in this run attacks it.
3. **The theta route.** Q-ALPOGE-METHOD now has exact objects for n = 4, 5 and 6. The definite-U₃ source for the E₆
   factor (P-F51) is the first place where a definite unitary group appears, as in Alpöge's step 8. The remaining
   comparison is with Alpöge's selected vectors and chains.

## 7. Integration (no edits made outside this folder)

- **HEXAGON_CANDIDATES.md, H02 (P-F31):** add "checkpoint 06: P-F31 and its inputs are unchanged (no new check events,
  same source sizes [corrected 22 Nov 2026 by the main session e0d20ada, Claude Opus 5.5 at effort max: the old wording was "identical sources"; only sizes
  had been compared]). PH2/SH open; the refutation route is narrowed to the lower four fifths of B_n's coefficients
  (P-F42ah to P-F42ak)." The gate is unchanged.
- **Successor prompt:** state the PH2 question as in section 6.1, and keep SH(b) as a separate row.
- **The project's terms:**
  - B_n is the leading Riemann-Roch polynomial of the stretching ring, i.e. the Hilbert polynomial of the
    Proj quotient.
  - The pole at ζ is the μ_M fixed-locus contribution in the Lefschetz-Riemann-Roch of SGA 6 (as P-F23 already was).
  - The gate is a comparison between the principal term and one twisted term of that formula.

## 8. Hexagon readiness

- **H02 (P-F31):** unchanged; see section 1. The gate is still stability: the run's final and the literature search.
- **The P-F42 extension:** not a candidate on its own. It is a reduction, not a theorem about PH2.
- **H03:** not touched by this run.

# Intake of GCT_POS (prompt 52), checkpoint 03: Kronecker, plethysm, saturation, density, formulas and sources (items 1-7, 10, 11)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the request of the main session (Claude Opus 5.5
at effort max) and on the user's word ([the user's words, omitted], 21 Nov ~23:5x UTC).
The run is GPT-6 Astra (ChatGPT Pro mode); its files record the effort as "not exposed". The nonstandard items 8-9
(N-*) belong to agent a8d75352 and are not covered here. Work file: `agent_notes\a0805369bae2ebddc_NOTES.md`.

> **Update and corrections, 22 Nov 2026, about 08:30 UTC (same agent).**
> - **This intake is of checkpoint 03 and is superseded in part.** `GCT_POS_final_20261122T0219Z_unzipped` is now the
>   return, and the checkpoint-03 folder has been retired. Its FINAL_STATUS.md says the programme ended INCOMPLETE, and
>   claims that **the existence clause of numerical PH3 is refuted for triple-rectangular Kronecker coefficients**
>   (K023, R-NEW004, K024, PNEW013: a pole of order 2^(n-1)·3^r, some r ≥ 0, for every n ≥ 2). I have not read or
>   checked that proof. Where this file calls that question open, or advises waiting for the final, it describes
>   checkpoint 03.
> - **Section 1a is filled in:** all 5,214 rows of R-NEW-001 agree.
> - **Corrections to what I first wrote and reported:**
>   - the number confirmed was 15 findings, not 18 (16 with R-NEW-001), plus the n = 4 value table;
>   - 17 findings are carried, not about 15, and 2 are background, not 3;
>   - K-018 is confirmed at n = 9 only: I read the first 70 of 147 lines of its file;
>   - several "read in full" entries were partial, and are now listed as such;
>   - four check events typed "independent re-proof" were computations, and are retyped.

## 0. Return read and scope

- **Return:** `research_returns\GCT_POS_checkpoint_03_20261121T2215Z_unzipped`, the snapshot of 22:16 UTC on 21 Nov,
  taken about 2 h 15 min into the run. It is a checkpoint, not the final return.
- **Read, with the proof** (line counts are those of the files in the final):
  - K-001 to K-008 (`branches/kronecker/KRONECKER_FINDINGS.tex`, lines 1-520 of 537); the chart ideals of K-003/K-004
    and the commutator kernel of K-004 were not recomputed;
  - K-009 (`branches/root/lift_bound.tex`, whole);
  - R-NEW-003 (`branches/root/h4_finite_rational.tex`, lines 1-90 of 115: the denominator and degree argument);
  - K-014 (`N5_POLE.tex`, lines 1-60 of 132);
  - K-018 (`AMPLIFYING_GADGET.tex`, lines 1-70 of 147);
  - the PNEW-005 assembly (`plethysm/quantitative_refinement.tex`, lines 329-420 of 429).
- **Read at statement level, with the source text of the statement:**
  - K-010 to K-013, K-015 to K-020;
  - PNEW-001 to PNEW-004, PNEW-006 to PNEW-012;
  - R-NEW-001, R-NEW-002.
- **Also read:** LEDGER.md, QUESTIONS.tsv, the ids in CHECK_EVENTS.tsv, SOURCE_AUDIT.md §2, `plethysm/LEDGER.md`, and the
  file lists of `reviews/` and `certificates/`.
- **My computations.** All of them are in my scratchpad folder `chk\gctpos\`, run with `python -I -B`.
  - **Independent:**
    - `kron.py`: k_n(s) by Murnaghan-Nakayama characters;
    - `k005.py`: the n = 4 local residues;
    - `k014.py`: the n = 5 total residue, rebuilt from the run's 77-type table;
    - `k018.py`: the n = 9 order-512 example, by Smith normal form and lattice arithmetic;
    - `pnew.py`: dyadic waves by 60-digit product formula, and the n = 4 constituents from Salmon's series;
    - `o6b.py`, `o6c.py`: every row of the outer-six table against my power-sum computation.
  - **The run's own verifiers, rerun.** `verify_n4_certificate.py` and `verify16_certificates.py` only read files, so I
    ran them in place.
  - I did not rerun the verifiers that write receipts into the return folder (`verify_n5_*`,
    `verify_amplifying_gadget.py`, the stabilizer verifiers). For them I rely on the independent checks above.
- **Inherited items are not re-checked here.** The run cites ALPOGE_GCT (P-F*), GCT_PLETH (G-/T-/R-/A-*) and GCT_NSRH
  (F*) as prior work. Their checks are in our earlier intakes, parts 1-4. The A-* items that GCT_POS retains (A-001,
  A-004 to A-007, A-012, A-013, A-028) are GCT_PLETH's, and they are unchanged.

## 1. Verdicts, finding by finding

### Kronecker (item 1): k_n(s) = g((s^n),(s^n),(s^n)), the Hilbert function of ℂ[(ℂⁿ)^{⊗3}]^{SL_n³}

| Id | Statement (short) | Check | Verdict |
|---|---|---|---|
| K-001 | n = 3: Vinberg's ℂ[I₆, I₉, I₁₂] (Bremner-Hu, arXiv:1112.2949, Thm 2.4) gives H₃ = 1/((1−t²)(1−t³)(1−t⁴)), and p(k₃) = s(k₃) = 1 | computation: my character computation gives k₃(s) = 1, 0, 1, 1, 2, 1 for s ≤ 5, equal to the series; the constituent claim read | **confirmed** (the ring is cited) |
| n = 4 values | k₄(s) = 1, 0, 1, 1, 5, 4, 16, … (`certificates/k4_small_values.json`) | computation: mine gives 1, 0, 1, 1, 5 for s ≤ 4 | **confirmed** for s ≤ 4 |
| K-002 | n = 4, order 8: exactly 4 feasible spectral types (2,285 cases, Farkas certificates) | rerun of the run's exact verifier: PASS (4 positive, 2,281 separating vectors) | **confirmed** (certificates; the enumeration's generator was not rerun) |
| K-003, K-004 | full stabilizers of types 1 and 4; smooth fixed curves | targeted proof check of the arguments; chart ideals and commutator kernel not recomputed | **confirmed** |
| K-005 | local residues (1/256, (1+√2)/128, (3−2√2)/256, −√2/256); the 13-component sum (14−10√2)/256 | independent recomputation (`k005.py`), every value | **confirmed**. Type 4 has the opposite phase. |
| K-006 | edge-doubling support extension doubles the character order | proof read | **confirmed** |
| K-007 | n = 4 lift bound: two-part ≤ 16 | targeted proof check: vertex supports m ≤ 10; m = 8, 9 half-integral; for m = 10, Cauchy-Binet gives 48d² ≤ 7.5·2.5⁹, so d ≤ 24 | **confirmed** |
| K-008 | **the complete μ₈ fixed locus for n = 4 is 13 curves; H₄ has a simple pole at the primitive 8th roots, residue (14−10√2)/256** | rerun of the verifier: order 8, 31,302 orbits, 4 feasible; order 16, 56,418 orbits, 0 feasible; PASS. Residue recomputed. The logic (K-007 coverage, P-F23g) read. | **confirmed** |
| K-009 | lift bound d ≤ B_n = (3−2/n)^{(3n−2)/2}/n for every n; no pole at a primitive root of order > B_n | targeted proof check: 3n² nonzero minors, trace 3r, Λ ≥ 3r/n, AM-GM, f decreasing for u > 3 | **confirmed** |
| K-010, K-011 | n = 5: 77 spectral types (one repeated), all lifts up to the K-009 bound | statement level; the run reports 3,409,995 rational certificates verified at root | carried |
| K-012, K-013 | antipodal-spectrum and single-pair criteria for full stabilizers | statement read | carried |
| K-014 | **n = 5: 424 fixed curves; simple pole at the primitive 16th roots, residue (78 + 446ζ − 211ζ² − 301ζ³ − 301ζ⁴ − 211ζ⁵ + 446ζ⁶ + 78ζ⁷)/32768** | independent recomputation from the run's 77-type table: the class count 424 (65·6 + 11·3 + 1·1) and the residue value both reproduce (`k014.py`) | **confirmed, given K-011's completeness** |
| K-015, K-016 | an all-dimension family with full stabilizer S × μ_{2^{n−1}} and a smooth fixed curve | statement level | carried |
| K-017 | a free support of order 256 at n = 8 whose fixed space is unstable | statement level | carried |
| K-018 | **the 2^{n−1} premise is false: polystable free supports with determinant order 2^{n−1+⌊(n−2)/7⌋}; n = 9 gives 512 > 256** | independent check at n = 9 (`k018.py`), on the run's support data, which I did not regenerate from the gadget: torsion of ℤ²⁷/L is ℤ/512; χ has order 512; masses positive with margins one; the support is free; the W-spectrum fixes exactly the support; exponent sum 219 is odd | **confirmed at n = 9**, which refutes the universal 2^{n−1} bound; the all-n formula is at statement level (proof read in part) |
| K-019 | n = 9: a smooth μ₅₁₂ curve, but the μ₂₅₆ fixed scheme has dimension 4 there | statement level | carried |
| K-020 | n = 2+7k: smooth density-one curves fixed by μ_{2·256^k} | statement level | carried |
| R-NEW-003 | H₄ = (Σ_{j<3196} P_j t^j)/D₄(t), with the denominator degree 3196 explicit | proof read: pole order ≤ 19, roots of order > 24 excluded by K-009, 16th roots excluded and 8th roots simple by K-008, strict properness from Baldoni-Vergne | **confirmed for the denominator and degree argument** (end of the proof not read; numerator not expanded) |

### Plethysm (items 2-3): the refutation chain, the explicit witness, and density

| Id | Statement | Check | Verdict |
|---|---|---|---|
| PNEW-001 | n = 4, x = 19: 2W₄(19) = 1/8 > 0 = f₄(19) | independent, two ways: the product formula (P-F56v); and Salmon's series, where q₇₉(19) = −1/8 | **confirmed** (a corollary of P-F35) |
| PNEW-002 to PNEW-004 | sharper near- and far-increment estimates and the starting-mass bound | statement level; the run's independent review is `reviews/quantitative_refinement_nonstandard_review_79000.md` | carried |
| PNEW-005 | **p(f_n) > 2^{n/8} and s(f_n) ≥ 2^{n/8} for every n ≥ 79,000** (formerly 2·10⁸⁰) | targeted check of the assembly: all four exact rational margins reproduced (19/59724000, 8303507/86406250, 1676026865671/255978515625000, exponent −445603261) | **confirmed, given PNEW-002 to PNEW-004** |
| PNEW-006 | exterior identity f_n(s) = [det^n : Λ^{ns/g}(Λ³ℂ^{3s/g})]; explicit witnesses: **p(f₉) > 7 and s(f₉) ≥ 7**; 2W₉(6) > 1 = f₉(6) | 2W₉(6) and 2W₉(7) recomputed to 60 digits (= 1819142906755/64 and 782264335828/64). f₉(6) = 1 from **my independently recomputed B₆ table** (part 1): at j = 18, (9⁶) has multiplicity 1. The identity is consistent at n = 3, s = 4 and s = 6, and at n = 4, s = 2 | **confirmed, given the exterior identity**, whose proof is not read |
| PNEW-007 | a positive-initial ray h(s) = f₁₅(7s) with h(1) = 1 and p(h) > 7 | statement level | carried |
| PNEW-008 | determinant padding keeps the intrinsic graded algebra fixed while lengths grow: refutes the intrinsic-stabilizer-growth converse | statement read | carried |
| PNEW-009 | **narrow SH(b) holds for every fixed rank n and fixed inner μ with dim S_μℂⁿ > n**: the exceptions have density O(N^{m+n−1}2^{−ηN}) | statement read; Baldoni-Vergne input as cited; the run's independent review `fixed_rank_density_root_review.md` | carried. The constants are not uniform, so varying-embedding SH(b) stays open. |

### Formulas and the canonical map (items 4-6)

| Id | Statement | Check | Verdict |
|---|---|---|---|
| PNEW-010 | the literal G-040 construction needs ≥ 2^{r−1} cover generators at m = 2r, b = r(r+1)+1 | proof opening read (degree b−1 component = Sym^{b−1}W) | carried |
| PNEW-011 | the scalar six-point Cox ring is the Grassmannian Plücker ring (known: Castravet-Tevelev, Remark 3.9) | statement | background |
| PNEW-012 | outer degree six, two-row output: 330 fixed polytopes (≤ 45 per μ, ≤ 11 variables), compiled from Pak-Panova-Swanson | statement; the run reports 2,717 + 5,214 + 242 + 44 checks | carried (credited to PPS) |
| R-NEW-001 | the outer-six reference table, 5,214 coefficients with n ≤ 3, by two methods | independent computation of every row (`o6b.py`, `o6c.py`): 0 mismatches | **confirmed**, on the copy in the final (see 1a) |
| R-NEW-002 | the r = 3, 4 critical annihilators vanish by the known rank laws: a = 4 (McKay); a = 5 (Cheung-Ikenmeyer-Mkrtchyan; Ikenmeyer's propagation) | statement read; it agrees with GCT_PLETH R-031 (part 3) | background, correct |

**Counts** (35 findings: K-001 to K-020, R-NEW-001 to 003, PNEW-001 to 012).
- 16 confirmed, at the scope stated in the tables: K-001 to K-009, K-014 (given K-011), K-018 (n = 9 only),
  R-NEW-001, R-NEW-003, PNEW-001, PNEW-005 (given PNEW-002 to 004), PNEW-006 (given the exterior identity).
  The n = 4 value table is also confirmed, for s ≤ 4.
- 2 background, correct: R-NEW-002, PNEW-011.
- 17 carried at statement level: K-010 to K-013, K-015 to K-017, K-019, K-020, PNEW-002 to 004, PNEW-007 to 010,
  PNEW-012.
- 0 refuted. No gap found in what was read.

### 1a. The outer-six table (R-NEW-001)

- **Result: all 5,214 rows agree with both of the run's columns** (11, 121, 847 and 4,235 rows for n = 0, 1, 2, 3).
  The rows are exactly all pairs (μ ⊢ 6, λ ⊢ 6n), with none missing, extra or repeated (`o6c.py`).
- **Method:** h_n and p_r[h_n] expanded in power sums, paired with Schur functions by my own Murnaghan-Nakayama code,
  in exact rationals. It is the same classical method as the run's first column, in independent code.
- **Which file:** checkpoint 03 was retired before this check finished, so the file checked is
  `certificates/outer_six_n_le_3.tsv` of the final, sha256
  0d660744557c219cd1665692ca4edc38f0d63851e9aa521cd7660722b9b07c7a, as in the final's manifest. It has the row
  count of checkpoint 03's file. I could not compare the bytes of the two copies.
- **Failed attempts:** two earlier runs by weight expansion (`o6.py`) gave no result; the second, on a reduced sample,
  ran out of memory. Neither is evidence.

## 2. What is new

- **Kronecker poles at n = 4 and n = 5 (K-008, K-014).**
  - Our part-4 intake asked whether triple-rectangular Kronecker coefficients have the plethysm-type dyadic pole. They
    do, at n = 4 and n = 5.
  - The residues are nonzero after cancellation between components of opposite phase.
  - K-005 shows that the "every component has the chain phase" shortcut fails. So the plethysm proof (one isolated
    component, P-F30) does not transfer verbatim.
  - No complete calculation of this kind was found in the inspected literature (SOURCE_AUDIT §2).
- **K-018 and K-020, against our own conjecture.** The determinant-order premise of prompt 52, item 1(a), was a
  conjecture of ours, from my ALPOGE_GCT part 4 and from the core. It is **false** for tensors: the order is
  2^{n−1+⌊(n−2)/7⌋}, with smooth density-one fixed curves of order 2·256^k at n = 2+7k.
  - This is a correction to our own prompt, which the run made correctly.
  - It also bears on novelty. Exponential vertex denominators of axial three-index assignment polytopes are in the
    literature: Kravtsov; Franks-Reichenbach, as the run notes. So the order growth itself may be known in the polytope
    literature. What GCT_POS adds is the 2-power part, polystability, and the full stabilizer. A literature check
    against Kravtsov is needed before any novelty claim.
- **PNEW-005 and PNEW-006.** These meet prompt 52's item 2.
  - The explicit threshold for P-F57 drops from 2·10⁸⁰ to **79,000**.
  - A fully explicit small witness: p(f₉) > 7 and s(f₉) ≥ 7, in rank 9. Its amplitude is checked here exactly, and
    the f₉(6) = 1 side follows from a table I computed independently.
- **PNEW-009** is a density theorem in the direction of SH(b) (no literature search made): fixed rank, fixed inner embedding.
- **R-NEW-003** gives a certified finite expression for H₄, with an explicit denominator. It is new as a certificate,
  not as an algorithm.
- **Not new:**
  - K-001 (Vinberg; Bremner-Hu);
  - R-NEW-002 (published rank laws);
  - PNEW-011 (Castravet-Tevelev);
  - PNEW-012's underlying positivity (Pak-Panova-Swanson);
  - PNEW-001 (a corollary of P-F35).

## 3. How it bears on GCT VI's PH1-PH3 and on our register

**PH3 for Kronecker.**
- The existence clause fails at n = 4 and n = 5 in this concrete sense: every positive form has a weight divisible by
  8 (resp. 16). That alone is finite and refutes nothing asymptotically.
- The gate is the global residue at the maximal two-power order, for all n. K-018 to K-020 change the shape of that
  gate:
  - the maximal order is at least 2^{n−1+⌊(n−2)/7⌋};
  - the fixed scheme can have components of dimension 4 (K-019), so P-F23's unique-component hypothesis fails;
  - the multiple-component formula (P-F23g) and higher-order poles must be used.
- **Attack opened:** at n = 2+7k the μ_{2·256^k} fixed locus. K-020 gives a smooth density-one curve. Show that it is
  the only top-dimensional fixed component at that order, the analogue of P-F30 for the amplified gadget. Then P-F23
  gives a pole at roots of order 2^{1+8k}. That is exponential in n, so numerical PH3 fails for Kronecker
  coefficients. The finite tool is the K-009 bound; the classification is the gate.

**PH2 and SH(a) for Kronecker: open.** No wave estimate yet. The P-F56/P-F57 route needs:
- the global residue;
- a dominance bound over all other residues, now including higher-order poles and components of opposite phase.

**PH2 and SH(a) for plethysm:**
- now with the explicit threshold 79,000 (PNEW-005);
- and a small certified witness in rank 9 (PNEW-006).

**SH(b):** fixed-embedding SH(b) is proved (PNEW-009). Varying-embedding narrow SH(b) is open. The stabilizer-growth
converse is refuted in its intrinsic form (PNEW-008).

**H02** (P-F31/P-F57; the register row still reads "Theorem 1.6.1(d)"; parts 2-4 asked for it to be re-titled).
- **Strengthened:** the explicit threshold, 79,000; an explicit witness, n = 9; and the whole inherited chain, which
  the run read in full and assembled as a standalone 58-page companion, `PLETHYSM_STANDALONE.tex`.
- **Test 3 (stable):** still waits for the run's final and the literature search.
- **Test 4 (checked):** now has two independent computations of the witness.

**H20** (G-036 + T-037, outer degree ≤ 5). R-NEW-001 and PNEW-012 extend the *checked range* to outer degree six:
the full table to n ≤ 3, and two-row output in all degrees by the PPS compilation. Neither supersedes H20.

**H21** (G-037 to G-040).
- PNEW-010 limits G-040's dense-cover implementation: it is superpolynomial in b. A compressed formula is not ruled
  out.
- H21's G-040 entry should say "polynomial for fixed b; the literal construction is superpolynomial uniformly in b
  (PNEW-010)".

## 4. Errata

1. **Our own prompt 52, item 1(a), and my ALPOGE_GCT part 4, section 6.2.** The working premise that the extremal
   determinant order is 2^{n−1} for tensors is refuted by K-018 (n = 9: 512). It holds at n = 4 and 5 (K-008, K-014).
   It should not be carried into later prompts.
2. **K-005 versus an expected "uniform phase".** At n = 4 the components have different phases. Any write-up must use
   the summed residue, never a single-component argument.
3. **No errata to GCT VI beyond those already recorded** (P-F12/PL-Q22; P-F14/P-F15). The run rechecked them.

## 5. Hexagon readiness

- **H02 (P-F57 with PNEW-005/006):**
  - Tests 1, 2 and 4 pass. Test 4 is stronger than before: the witness is checked by computation twice.
  - Test 3 waits for the run's final and the literature search.
  - The gate is unchanged, and it remains a flag-to-the-user item.
- **New candidate: "Kronecker dyadic poles at n = 4, 5" (K-008 + K-014).**
  - Complete for n = 4 and 5, self-contained, and checked: the verifiers rerun, and the residues recomputed.
  - But it is a finite result, and the run is moving toward the all-n question.
  - Interest: moderate as finite data. It would be high if extended to all n.
  - Not ready: wait for the run's all-n result.
- **New candidate: K-018/K-020, "extremal determinant orders of polystable tensors exceed 2^{n−1}".**
  - Complete and checked at n = 9.
  - Novelty is uncertain until it is compared with Kravtsov's denominators.
  - Not ready: the literature gate.
- **H20 and H21:** unchanged; the notes of section 3 apply.

## 6. What a successor or a later checkpoint should be asked

- **Kronecker:**
  - the μ_{2·256^k} fixed locus at n = 2+7k, from K-020: classify it, and compute its residue with P-F23g;
  - then the dyadic wave and its dominance for PH2 and SH(a);
  - handle K-019's 4-dimensional components by the higher-order-pole version of P-F23.
- **Novelty:** compare K-018 with Kravtsov (vertex denominators of axial assignment polytopes) and Franks-Reichenbach.
- **Expand R-NEW-003's numerator**, or compute k₄(s) for s ≤ 3195 by the R-3c character sums, to get the exact n = 4
  indices. That is the Kronecker counterpart of P-F35's 23.
- **SH(b) with varying embedding:** make PNEW-009's constants uniform in the rank, or construct a dense exception
  family.
- **The project's terms:** the run's item 11 (the Grothendieck dictionary) is "in progress". The required form:
  - k_n's ring is the coordinate ring of the GIT quotient of trilinear forms;
  - the poles are fixed-point terms of Lefschetz-Riemann-Roch (SGA 6, Exp. VII);
  - the order-2^{n−1+⌊(n−2)/7⌋} stabilizers are characters on residual gerbes of the moduli stack.

  Ask for it in the final.

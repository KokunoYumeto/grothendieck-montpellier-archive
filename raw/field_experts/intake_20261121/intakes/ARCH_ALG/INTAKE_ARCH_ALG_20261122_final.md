# Intake of ARCH_ALG (prompt 50), the final return, 22 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), 22 Nov 2026, for the main session (Claude Opus 5.5
at effort max). The run is GPT-6 Astra (ChatGPT Pro mode), effort not exposed. The seed was written before this
intake: `reports_20261122\paper_seeds\SEED_ARCH_ALG.md`. It continues ALPOGE_BRIDGES, whose intakes (parts 1-4 and the
checkpoint 03 addendum) are the baseline of the diff.

## The result in one paragraph

On cote 136, Grothendieck's conjecture on equalizing two comparison maps is false in the strict sense over every
nonzero ring (ALPOGE_BRIDGES). In a specified homotopy sense it holds, together with common sources and terminality of
the groupoid, over every ring with only finitely many non-unit primes. **I checked that chain proof by proof, and
found no gap.** Over ℤ everything stays open, and the run ended INCOMPLETE there. On cote 134-8 the natural route to
the Thm(?) is refuted by an example that satisfies every axiom and still has the predicted localization. On cote 15 the
counterexample to Thakur's Proposition 2.9 is checked in its invariants and its nondescent. On cote 123 the new type-A
count is confirmed by my computation for n ≤ 9.

## 0. Return, method and scope

- **Return:** `research_returns\ARCH_ALG_final_20261122T0622Z_unzipped`, 185 files. All 178 files of its manifest match
  their SHA-256. The run stopped at 06:16 UTC after two reviews without movement.
- **By content:** there was no earlier intake of this run, so every finding is new to us. Against the run's own
  checkpoint 05 manifest 99 files are the same and 28 changed. Against ALPOGE_BRIDGES checkpoint 09 the run changes no
  finding. It sharpens one bound and refutes one proof route (§2).
- **Read in full, with proofs:**
  - `cote136/homotopy.tex`, `cote136/arithmetic_improvement.tex`, `cote1348/arch134_checked.tex`;
  - in ALPOGE_BRIDGES: AQ-136-COMPARISON (the statement and proof, lines 3035-3112), PLOCAL, SEMILOCAL (all five
    steps), COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES.
- **Read in part:** `cote15_honda_check.tex` lines 1-150 and 203-214; `cote15_core.tex` lines 59-78, 153-192, 345-372;
  `cote123/companion.tex` at the statements.
- **Also read:** README, FINAL_STATUS, IMPLICATIONS (lines cut at 1,200 bytes), the question column of QUESTIONS, the
  abstract, the end of the ledger.
- **Not read:** every other proof module (the cote 136 repair lemmas, ARCH-134-04 to 06, the cote 15 target, the
  companion's proofs), F-SM-34, and the scans. Cotes and scans are cited from the run and our transcriptions' names.
- **No code of the return was run.** My program is `check_arch.py`, with `check_arch.txt`, in
  `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\chk\seeds1`
  (a temporary folder).

## 1. Verdicts

### 1a. Checked

| Id | Statement | Check | Verdict | In the project's terms |
|---|---|---|---|---|
| AQ-136-COMPARISON | H^j(C^{w,*}(X)) ≅ H^j(X;k)⊗S^w for large w, uniformly in X | targeted proof check | **confirmed** | derived sections on simplicial sets (SGA 4) |
| AQ-136-PLOCAL | common sources over every ℤ_(p)-algebra | targeted proof check | **confirmed**, given DP-MODEL (confirmed 21 Nov) | Γ(U) → Γ(T) is free at a prime-power weight |
| AQ-136-SEMILOCAL | the all-arrow groupoid is a point when finitely many primes are non-units | targeted proof check, all five steps (step 1 was already confirmed) | **confirmed**, given COTENSOR and DP-MODEL. ℚ-algebras are included, so the theorem needs no separate rational proof | arithmetic fracture square and path objects |
| AQ-136-COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES | pullbacks along paths; common sources ⇔ connected; hence strict common sources in that range | targeted proof check | **confirmed** | pullback of generalized de Rham theories |
| ARCH-136-HOM-DEFINITION | the homotopy reading of « égalise » | read | a definition, stated as ours | cotensor by finite edge paths |
| ARCH-136-PATHS | path objects and their pullbacks are admissible | targeted proof check | **confirmed**. It also gives COTENSOR in what is used | the same |
| ARCH-136-FRACTIONS | right fractions modulo homotopy compute the groupoid, with an equality criterion | targeted proof check | **confirmed** | calculus of fractions |
| ARCH-136-HOM-SEMILOCAL | the homotopy conjecture ⇔ simply connected components; true over semilocal rings | targeted proof check | **confirmed** | the groupoid of physical p. 121 |
| ARCH-136-ARITH-BOUND | horizontal bound (q+1)·max N_i, vertical N(d+2), no sum over primes | targeted proof check | **confirmed** | uniformity in the prime set |
| ARCH-134-01 | square-zero unitization of an exact scalar embedding | targeted proof check | **confirmed** | scalar adjoints φ ⊣ κ ⊣ ψ |
| ARCH-134-02 | under all axioms L₂φ need not commute with a countable sum | targeted proof check | **confirmed, given F-SM-34** (not read) | linearization |
| ARCH-134-03 | that example still localizes to D≥0(k); W is not closed under sums | targeted proof check | **confirmed**, given the same | the Thm(?) is not refuted |
| ARCH-15-HONDA-CHECK | A/F₅₁₂ has index 3, dimension 3, and doesn't descend to F₈ | targeted proof check of lines 1-150; arithmetic recomputed (h = 3, valuations 3 and 6, cubes of units) | **confirmed on the lines read**. Thakur's text was not opened, so "refutes Proposition 2.9" holds given the run's reading of it | Weil numbers and Brauer invariants of Frobenius motives |
| ARCH-123-COUNT | number of outer-fixed classes in type A | own count over all orderings, n = 3..9 | **confirmed by computation for n ≤ 9**. General proof not read | finite normalizer of an apposition pair |

### 1b. Statement read, proof not checked (carried, no fault seen)

ARCH-15-CUBIC-GATE (its opening only), ARCH-15-SPLIT-CUBIC, ARCH-15-KUMMER, ARCH-123-NORMAL.

### 1c. Known to me only from the run's summary (no event recorded, no verdict)

- **Cote 136** (123, prefix ARCH-136-): ACTUAL-TAIL-CONSTANT-QUOTIENT, ACTUAL-TAIL-SYZYGY, ADMISSIBLE-INTERMEDIATE-COUNTERBRIDGE, ASSOCIATIVE-COMPARISON, ASSOCIATIVE-TERMINAL, CENKL-AUDIT, CHOSEN-NATIVE-PATHS, CHOSEN-PATH-LOW-REPAIR, COEFFICIENT-HISTORY-OBSTRUCTION, COHERENT-LOW-REPAIR, COHERENT-PD-REALIZATION, COSKELETON-FORWARD, CRITICAL-NATIVE-PATH-COMPONENT, CYCLIC-DISK-QUOTIENT, DEGREE-FOUR-CONCENTRATION, DEGREE-FOUR-FACTOR-OBSTRUCTION, DEGREE-THREE-COMMON-SKELETON, DEGREE-THREE-LINKING-REPAIR, DEGREE-TWO, DEGREE-TWO-FREE, DEGREE-TWO-RESIDUE, DERIVED-TAIL-COMPARISON, DETERMINANT-LINEARIZATION, DETERMINANT-RIGIDITY, DIAGONAL-REDUCTION, DISK-SUPPORT, EVEN-DISK-H1, EVEN-DISK-H2, F2-ITERATION-NOTE, FINITE-SKELETON-REPLACEMENT, FIRST-CELL-RESIDUES, FIRST-SKELETON-RESIDUE, FLAT-RATIONAL-TENSOR, FLAT-TAIL-ACYCLICITY, FREE-ARITY-TAIL-OBSTRUCTION, FREE-COMPLEX-LIFT-CAUTION, FREE-MAP-HOMOTOPY, FREE-PARTIAL-NONCOMPLETION, GRADED-INJECTIVES, GUARDED-NATIVE-PROBE, GUARDED-PAIR, HIGH-DEGREE-PRESCRIBED-PATHS, HIGH-NATIVE-RESIDUE, HOMOTOPY-PEER, INITIAL-TENSOR-PERIODS, INTEGRAL-FLAT-TAIL, INTEGRAL-PERIOD-MAXIMALITY, KKM-AUDIT, LINEAR-PRIME-TAIL, LINKING-CHAIN-GATE, LINKING-TRIANGLE-OBSTRUCTION, LOCALIZED-TENSOR, LOW-FACTOR-PRESERVATION, LOW-GENERATED, LOW-GENERATED-TORSION, LOW-REFINEMENT, LOW-TATE-RETAINED-COMPLETION, MASSEY-RIGIDITY, MASSEY-TRANSPORT, MIXED-H2-RESIDUE, MOORE-DUPLICATE, MOORE-PAIR, MOORE-TOWER, NATIVE-ALL-ARITIES, NATIVE-LIFT, NATIVE-MIXED-RESIDUE, NATIVE-MIXED-TOR, NATIVE-TAIL-NOSPLIT, NONCYCLIC-CONSTANT-QUOTIENT, NONFLAT-KERNEL-LATTICE, NONFLAT-QUOTIENT-DISK, NONFLAT-SYZYGY-DISK, NONFLAT-TAIL-DISK, NONFLAT-TENSOR, NS-MODULE-THEORY-INPUT, ODD-ENVELOPE-RELATIVE, OLD-GRAPH-LINKING-REPAIR, PD-COEFFICIENT, PD-RANGE, PD-SECONDARY, PD-TAIL-PRINCIPAL, PD-ZEROFORM, PERIOD-REPAIR-FAILURES, POSITIVE-IDEAL-SATURATION, POSITIVE-TAIL, PRIME-INTERPOLATION-INVARIANCE, PTRUNC-ROUTE, Q2-Q3-COMPATIBILITY-OBSTRUCTION, Q3-COEFFICIENT-KERNEL, Q3-COEFFICIENT-TEST, Q3-ISOLATED-TOR, Q3-LOW-FILTRATION, QUADRATIC-TAIL-ACTION, RADIAL-RANGE, RADIAL-TARGET, RATIONAL-IMAGE-NOINTEGRAL, RELATIVE-BAR-OBSTRUCTION, RELATIVE-CELL-PATHS, RELATIVE-COHERENT-MOORE, RELATIVE-DISK-FACTORIZATION, SCALAR-DECALAGE-NOGO, SCALED-BAR, SKELETON-COHERENT-MOORE, SKELETON-OBSTRUCTION, SKELETON-TATE-LIFTS, SPECIAL-CONORMAL-N3, STANDARD-LATTICE-EMBEDDING, TAIL-CONORMAL, TAIL-EXT-VANISHING, TAIL-HOM-VANISHING, TAIL-MOORE, TAIL-PDIM, TOR-GRAPH-PRIMITIVES, TORSION-GRAPH-RESIDUE, TORSION-QUOTIENT-PERIOD, TW-CONSTANT, TW-RATIONAL, TW-TENSOR, TW-TOR, TW-VERTICAL, TWISTED-COEFFICIENT-COMPARISON, TWO-TRUNCATED-LINKING-REPAIR, VERTICAL-PERIODS.
- **Cote 134-8** (3, prefix ARCH-134-): 04, 05, 06.
- **Cote 15** (6, prefix ARCH-15-): ARCHIVE, CURVE-SQUARE, INPUT-AUDIT, K3-GATE, ORDINARY-TARGET, SOURCES.
- **Cote 123** (1, prefix ARCH-123-): SOURCE.

**Counts:** 9 ARCH findings confirmed at the scope of §1a, one definition, and 6 ALPOGE_BRIDGES inputs confirmed; 4 carried at statement level; 133 ids of the run's event register not read by me; 0 refuted.

## 2. What changes in what we hold

- **ALPOGE_BRIDGES (136.S2),** w ≥ q·max N_i + Σ N_i, is superseded by ARITH-BOUND. The sum was an artefact of the
  tensor of local models. "The obstruction we isolated" in prompt 50 is now max N_i alone.
- **The route "prove higher coproduct surjectivity and the Thm(?) follows"** (prompt 50, item 2; my part 4) is closed:
  that surjectivity is false under the axioms. The Thm(?) itself is open.
- **AQ-136-SEMILOCAL and SEMILOCAL-SOURCES** move from statement level to checked. The semilocal theorem was the gate
  of the cote 136 paper.
- **Register H20 and H21** (from the seed of GCT_PLETH, same day):
  - "first with varying outer degree" is false;
  - #P membership in fixed outer degree is no news;
  - the hook series is known;
  - T-012 carries out a remark of Sarkar;
  - part 4's "regime of the Fischer-Ikenmeyer hardness results" was wrong: they fix the inner degree, while these
    families need n ≥ a+t.
- **Our cote 133 study:** the two corrections listed in Paper 5 of the seed remain to be made (A-001, A-013).

## 3. What is new

- **Against our results:** ARITH-BOUND, the fractions theorem and homotopy reading, ARCH-134-01 to 03, the count in
  type A, and the route records over ℤ.
- **Against the literature: not established.** The run's search for cote 123 is bounded by its own statement. I made
  no search for this run. Cartan, Miller and Cenkl-Porter have to be compared before cote 136 is called new.

## 4. Scope of the two proofs

No statement checked uses Alpöge, Masullo or any GRH. The run's README and abstract say that no new argument needs A
or M. The cote 15 rows that still depend on named CM preprints are tagged by the run and are not in the checked list.

## 5. Faults

- **Mathematics:** none found in the proofs read.
- **Run's layout:** some twenty cote 136 proof modules lie under `research/cote15/136/`. Copy that folder with cote 136.
- **Run's register:** the row id ARCH-136-NONCYCLIC-ZEROFORM-QUOTIENT-OPEN still says OPEN in its name while its state
  says that the first clause is refuted.
- **Others' works:** none in the return by file name or type. The PDF is the run's own.

## 6. Integration (no edit made)

- Cote 136 companion, scans 117-121: the four-part theorem of Seed Paper 1. ℤ is stated open, the reading of
  « égalise » is stated as ours.
- Cote 134-8 companion, scans 048-049: the example and its scope ("no counterexample to the Thm(?)").
- Cote 15 companion, scans 094-106: the threefold, with the version of Thakur's preprint named.
- Cote 123 companion, scans 022-023: the count (8 of 18 for n = 4) beside the existence answer. The subregular rank
  is credited to Richardson and Slodowy.
- Cote 133 study: Seed Paper 5 and the two corrections.
- INTAKE_LEDGER: ARCH_ALG is taken in at the level of §1.

## 7. What a successor prompt needs

1. Cote 136 over ℤ, with §1a as settled input. The gate is one cutoff for all primes, or an invariant of admissible
   maps. The retained-diagram noncompletion theorems close only routes that keep old maps.
2. Cote 134-8: the bare Thm(?) by a proof that uses no coproduct compatibility.
3. Cote 15: the exact statement and newest version of Thakur's Proposition 2.9 before any correction is published.
4. Cote 123: a rule for a unique distinguished class, and a literature search of the two tables.
5. Cote 133: the exact class of local rings (Seed Paper 5).

## 8. Hexagon readiness

| Paper of the seed | Complete | Self-contained | Stable | Checked | Interest | Gate left |
|---|---|---|---|---|---|---|
| 1, cote 136 | yes in its scope | after the AB lemmas are written in | yes (a ℤ answer would extend it) | chain checked here and by the run | high | literature with Hexagon; the write-up; reading of every page |
| 2, cote 134-8 | yes for the example | needs F-SM-34 | yes | checked given F-SM-34 | moderate | check F-SM-34; literature |
| 3, cote 15 | yes for the example | yes (Honda-Tate) | depends on the preprint's newest version | checked in part | moderate | open the preprint; literature |
| 4, cote 123 | yes | needs the CC-APG proofs | yes | in part | moderate | proof check of CC-APG02-11; literature |
| 5, cote 133 | not the exact class | yes | no, while the class is open | in part | moderate | check A-021 and A-012; read scans 28-29 |

None passes all five tests now.

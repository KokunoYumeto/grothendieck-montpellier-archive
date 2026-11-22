# Full intake of RESEARCH_SA05, statement by statement

## About this intake

**What was taken in.** The RESEARCH_SA05 final of 19 Nov 2026, 09:51 UTC, by GPT-6 Astra (ChatGPT Pro mode):
`grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA05_final_INCOMPLETE_20261119T0951Z_unzipped`.

**The list.** All 177 statement ids of its register that no intake had checked: `field_experts/INTAKE_LEDGER.md` §9,
row RESEARCH_SA05, rebuilt on 21 Nov at about 23:4x UTC.

**Taken in by** Claude Opus 5.5 at effort max (agent a7b7747fd6dd29f87, which made the sweep-3 reading, built the
prompt and did the first intake), on 21-22 Nov 2026, at the coordinator's word after the user's [the user's words, omitted].

**Earlier work it builds on.** `INTAKE_RESEARCH_SA05_20261119.md`, with its events INT-SA05-E01 to E33 and the
follow-up of its §9. Where a statement was checked there, the new event says so and gives the earlier event.

**Files:**
- `INTAKE_RESEARCH_SA05_20261121_full_CHECK_EVENTS.tsv`: 177 events, SA05F-E001 to E177, one for each id. Its columns
  are id, statement_id, date_utc, who, type and outcome.
- `intake_full_20261121/` holds:
  - `ids.txt`;
  - `build_index.py`, which extracts each statement and proof read-only from the return into `statements/NNN.txt`
    and writes `index.tsv`;
  - `show.py`;
  - `add_events.py` and the batch files `batch01.txt` to `batch13.txt`;
  - `check_wm.py`.
- Earlier scripts reused: `intake_RESEARCH_SA05_scripts/intake_checks.py` and `check_c5_example.py`.

**How deep each check went.** The rubric types are used as they are meant. "Carried as background without fault found"
says in its outcome whether I read only the statement, or the statement and the opening of its proof.

The return holds about 177,000 characters of statements and 399,000 of proofs. I read every statement. I read and
checked the proofs where a targeted check, a re-proof or a computation was possible within the bound. I did not read
most of the long conditional reductions of B.1, B.3, C.1(c), C.4 and C.6.

## 1. Counts

| type | events |
|---|---|
| independent re-proof | 17 |
| targeted proof check | 35 |
| computation or formal certificate | 9 |
| used and rechecked in this run | 1 |
| carried as background without fault found | 115 |
| refuted, with the refined statement | 0 |

Of the 115 carried statements:
- most were **read as statements only** (the outcome says so);
- about 30 are remarks, definitions or scope notes, with nothing to prove;
- about 60 are conditional reductions or equivalences with open conjectures. Their status lines already say
  "unresolved".

## 2. What was checked, by Part

**Part A, the main question.** All 21 statements were checked.
- The group calculations were re-proved: A:band, A:P, A:valuations (the weight-zero Weil numbers as anti-invariant
  valuation vectors), A:compacthasse and A:hasse (with the lim¹ step).
- Checked against the scans and the transcription: A:eta, A:class, A:rigidification (15:3 is right; F⁰(Q(1)) = Q),
  A:monoid (15:5), A:real (15:11) and A:enrichment (15:7).
- A:unconditional: its H¹ formula is the Milnor lim¹ formula.
- Computed: A:lefschetz-counterexample.
- A:lefschetz was re-proved in outline.
- Carried: A:dictionary, A:kisin, A:unframed-adelic. A:2026-abelian was read only, and it rests on an unchecked
  October 2026 preprint (§4).

**Part B.** Checked or computed:
- re-proved: prop:B-e (Weil-étale cohomology of F_q and e_q ↦ m·e_{q^m}), prop:B-continuity (continuity is
  incompatible with 12:65's vanishing over an algebraically closed field) and prop:B-Hf-tate (all n; for n < 0 by the
  Bloch-Kato Euler characteristic, unconditionally);
- the B.4 tables, against Borel, the zeros of ζ, Tate's global Euler characteristic and the pairing n ↔ 1 − n:
  thm:B-SpecZ-Q, cor:B-Hf-all-degrees, thm:B-full-tate, thm:B-rational-duality;
- prop:B-integral-structure (the w_m formula, computed for m = 2-40);
- the corank: thm:B-Sha-corank and prop:B-paired-corank;
- the counterexamples: ex:B-X011, ex:B-H2-constant and prop:B-Brauer-arithmetic;
- rem:B-Keller-closure-error: the counterexample is valid, but Keller's paper was not opened;
- lem:B-surface-Tate-prime (known).

The surface-Tate reductions of B.3 and the phantom and Chow gates of B.1 and B.5 were read as statements.

**Part C.** Checked:
- re-proved: c:def-pointed (degrees), c:graph-rule (the excess Euler factors), c:pair-ranks (the four local relations,
  their last one by the modified diagonal), c:modified-diagonal and c:lie-centre;
- computed: c:finite-field-lie (y² = x³ − x over F₅: 8 points, T² + 2T + 5) and c:fermat-counterexample (its elementary
  inputs);
- c:explicit-bad-reduction: re-proved with a script; it is not new (Raynaud-Gabber);
- targeted: c:level-special-cases, c:local-dimension (against the scan of 12:120), c:broader-coefficients,
  c:general-level-bound, c:k3-stable-range (46 factors = 2 × 23), c:finite-field-sign (Katz-Messing),
  c:ell-independence-cases (Néron-Ogg-Shafarevich), c:vz-positive (Vasiu-Zink), c:subgroup-versus-object and
  c:single-endpoint-insufficient (the data).

The finite criteria of C.1(c) and the threefold gates of C.4 were read as statements.

**Part D.** Checked:
- re-proved: thm:d-reflex-image (the image torus and its lattices; the answer to 15:151);
- computed: prop:d-metabelian-false (S4) and ex:d-non-betti (the quaternion algebra (−1,−1) over Q(√5) is ramified
  exactly at the two real places);
- targeted: prop:d-frobenius-correction (Frobenius is known only up to the finite-order character), prop:d-special-
  fibre-false (gerbe over Q against a group over F_p), thm:d-toric-classification (abelian type), prop:d-integral-serre;
- thm:d-serre-finite-kernel is the same as 15:154.

## 3. Refuted or corrected

**No statement of the run was refuted.** Three of its statements refute something else, and I checked those
refutations:
- c:level-counterexample refutes our prompt's C.4 bound, not Grothendieck's box;
- prop:B-integral-errors refutes his integral tables of 15:173;
- prop:B-continuity refutes the continuity requirement together with 12:65.

**Errata found in this pass** (beyond those of the 19 Nov intake):
- **Ours, R8:** the modified diagonal lies in H^{4n} (codimension 2n), not H^{2n}, when n = dim X (c:modified-diagonal).
- **Ours, prompt D.1:** "its Frobenius at v is the image of a uniformizer under the reflex norm" holds only up to the
  finite-order part of the Hecke character (prop:d-frobenius-correction).
- **Ours, Leads D1 and D2:** refuted as written (prop:d-special-fibre-false, prop:d-metabelian-false). This was already
  in the 19 Nov intake.
- **His 12:65 against continuity:** his vanishing over an algebraically closed field cannot hold together with
  continuity, because over F̄_p his own computation gives H¹ = Q (prop:B-continuity).

**Claims the run makes about published sources.** Each needs a check against the source before anyone reports it:
- Keller, Lemma 2.17 (rem:B-Keller-closure-error). The counterexample is valid; the printed generality was not checked.
- Kerr-Yang, §4D (lem:B-KY-degenerate).
- Scholbach, *f-cohomology and motives over number rings* (prop:B-Scholbach-finite-support).

## 4. Dependence on unrefereed 2026 sources

These statements rest on the October 2026 preprint of van Hoften-Sempliner (the Hodge conjecture for CM abelian
varieties, hence Tate for abelian varieties over finite fields through Milne) or on a "6 October 2026 purity theorem":
- A:2026-abelian;
- c:ell-independence-abelian;
- c:hyperkahler-chow-unramified;
- c:motivated-abelian-strata-unramified;
- prop:d-cm-gerbe-reduction;
- thm:B-abelian-type;
- the "abelian part unconditional" of A.1.

I have not opened these sources. Every such statement holds only conditionally until they are checked. This matters
because "Tate for all abelian varieties over finite fields" would be a major theorem.

## 5. What is new

The new material is the content listed in §5 of the 19 Nov intake. This pass adds the explicit checks above.
- **Part A.** The explicit global class of the gerbe of F_p, and the vanishing of Ш² for the compact protorus H⁰.
  These are new as statements about Grothendieck's construction. Their ingredients are classical.
- **Not new:** C.5's bad-reduction example (Raynaud-Gabber, Vasiu-Zink Theorem 28(ii)). The "identical ranks,
  different coranks" phenomenon of prop:B-paired-corank is the classical gap between the Mordell-Weil rank and the
  rank of its ℓ-adic closure.

## 6. Hexagon readiness (`field_experts/HEXAGON_CANDIDATES.md`, the five tests)

**No statement of this run passes the five tests now.** The closest is the following.

**The explicit global class of Grothendieck's F_p gerbe** (A:class with A:hasse, A:valuations and A:unconditional).
- (1) Complete: in the run.
- (2) Self-contained: its inputs are Milne 1994, Kisin 2017 and Langlands-Rapoport, all published.
- (3) Stable: no successor is planned, but **no literature search has been done**. Milne 2003 and the work on
  Langlands-Rapoport may already compute this class.
- (4) Checked: partly (E01, E03, E09, E29 and the re-proofs above). A full read of its proofs is still needed.
- (5) Of interest now: moderate, to people working on Langlands-Rapoport and motivic gerbes.

So it fails (3) and (4) for now, with two gates left: the novelty search and the full read. Nothing here is timely
enough to flag at once.

**Not Hexagon material.** The three source corrections (Keller, Kerr-Yang, Scholbach) belong to "informing authors"
once checked. The corrections to Grothendieck's notes belong to the companion. C.5 is classical.

## 7. Full-depth pass (22 Nov 2026, same agent, at the coordinator's word)

**What was done.** The coordinator asked for full depth in this order:
1. the long proofs of B.1, B.3, C.1(c), C.4 and C.6;
2. the conditional reductions, checking the reduction step itself;
3. every other carried row whose proof is in the return.

The pass added 101 events, SA05F-E178 to E278, in the same TSV and through the same scripts (batch14 to batch40). The
old rows are kept; a row that moved up a level got a new event.

**Each statement at its best level now:**

| level | statements |
|---|---|
| independent re-proof | 32 |
| computation or formal certificate | 9 |
| targeted proof check | 114 |
| used and rechecked | 1 |
| carried as background without fault found | 21 |

Of the 21 still carried:
- 18 are remarks, definitions or scope notes, left as they are;
- ex:B-Vandiver37: the PARI certificate was not rerun, and h(Q(ζ₃₇)⁺) = 1 is known;
- ex:B-singular-infinite-period: its proof did not extract cleanly;
- c:uniform-arity-bound: the explicit constant was not re-derived.

**Re-derived in this pass:**
- **B.1:**
  - the idempotent lifting behind prop:B-phantom-gate;
  - the dimension-raising reduction of prop:B-diagonal-Chow-gate;
  - the surface-support argument (prop:B-surface-supported-CH2) and the uniruled threefolds;
  - the blow-up retraction R∘I = id on Bl_X P^{4m−1};
  - both limit counterexamples (the class prod P_n^{3^n} of infinite support, and the eigenfunction 4^x on Z₃);
  - the weight and vanishing inputs of the fixed-open formula.
- **B.3:**
  - the eigenvalue splitting and weight −1 descent of the all-base gate;
  - the π₁ step of the simply connected gate;
  - the explicit parts of the F₂[t] counterexample (smoothness, 3 points, H¹_fppf(α₂) = F₂[t]/F₂[t²]);
  - the 2-torsion argument of cor:B-torsors-prime-uniform (inversion acts by −1 on A and by +1 on N, so 2δ = 0).
- **C.1(c):** the K3 gate equivalences and the transcendental reduction to ∧^{23−ρ} t₂; the recursion
  κ_{m+1} = κ_m ∘ (μ_V ⊗ id), so that one identity Γ_{2n+1}(X, o) = 0 suffices; the finite-power retraction; and the
  Dickson-König finiteness.
- **C.4:**
  - the whole weight-level bookkeeping of c:general-level-bound. It answers Grothendieck's margin question of 12:120:
    n − 1 is right exactly when f has relative dimension ≤ n − 1 near y (ε = 1);
  - optimality via E^n over F₅ (slopes 0, 1);
  - the threefold-gate logic.
- **C.6:** the rank formula rank H^a(f) = rank [[d_C, 0], [f, d_D]] − rank d_C − rank d_D; André's operator identities
  T² = 1, TLT = Λ, [Λ, L] = d − m; and the trace argument of the abelian-type theorem.
- **D:** cor:d-all-weil (every Weil q-number from CM tensor motives) and the split prime of Q(√(1 − 4p)) in the CM
  lifting.

**No statement of the run was refuted in this pass.** One doubt was tested and cleared. In
prop:B-Milnor-divisible-kernel I asked whether unramified Brauer classes of a K3 surface over F̄_p could come from
symbols with constant residues. They cannot: the obstruction lies in H¹(X, K₂), and the run's weight argument (the
refined unramified group has negative weight, a Frobenius-fixed regulator has weight 0) kills the regulator.

**The van Hoften-Sempliner preprint, opened** (Hexagon 2610.00259v2; author PDF, 25 pp.).
- It is a human-written exposition, made with ChatGPT Pro, of OpenAI's preprint "The rational Hodge conjecture for CM
  abelian varieties" (2026). Its Theorem I: if X is an abelian variety with complex multiplication, the Hodge
  conjecture holds for X.
- §1.1.2: numerical = ℓ-adic homological equivalence for abelian varieties over any algebraically closed field, and
  the Hodge standard conjecture (Milne 2002, Theorem 4.6).
- §1.1.3: the Tate conjecture for abelian varieties over finite fields (Milne 1999b, Theorem 7.1), hence Lichtenbaum's
  conjectures and numerical = homological equivalence there (Kahn 2003).
- **Four of the six statements use it, and their use is correct:** A:2026-abelian, thm:B-abelian-type,
  c:motivated-abelian-strata-unramified and prop:d-cm-gerbe-reduction. They hold conditionally on this unrefereed
  preprint.
- **The other two use different 2026 preprints, not van Hoften-Sempliner.** I did not open these:
  - c:ell-independence-abelian uses OpenAI, "Milne's rationality conjecture for abelian varieties" (7 Oct 2026), with
    an exposition by ChatGPT and Claude hosted by K. Madapusi;
  - c:hyperkahler-chow-unramified uses Ito-Zou, "Semisimplicity, Purity and Mumford-Tate Conjecture for hyper-Kähler
    Varieties" (6 Oct 2026).
- **Further 2026 inputs found in this pass,** also unopened: Balkan-Schreieder 2026 (prop:B-diagonal-Chow-gate);
  Colliot-Thélène-Schreieder 2026 and Schreieder 2026 (prop:B-Milnor-divisible-kernel).

**Corrections to §3-§4 of this file:**
- prop:B-Scholbach-finite-support is not a claim of an error in Scholbach's paper. Under his definitions, H¹ of
  i_* 1 is H¹_M(F_p, Q(0)) = 0, while the Weil-étale value is Q·e_p. So his theory does not meet our corrected
  package; nothing is wrong in his paper.
- The source claims that still need a check against the source before anyone writes to the authors:
  - Kerr-Yang §4D: the homogeneity argument is sound if the coordinates are as described;
  - Keller, Lemma 2.17: the counterexample is valid.

**Hexagon readiness: unchanged.** No statement passes the five tests. The answer to the margin question of 12:120
(c:general-level-bound) is a good companion item, not a Hexagon post: its inputs are cited, not new.

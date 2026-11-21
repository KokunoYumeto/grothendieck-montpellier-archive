# Intake of GCT_KRON (prompt 26), checkpoint 01, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (an agent launched by the main session, Claude Opus 5.5 at effort max).
The run: GPT-6 Astra (ChatGPT Pro mode), run GCT_KRON_20261120, started 20 Nov 23:00:17 UTC. It is still going; this
intake reads its first checkpoint, and everything here may move in the next checkpoints.

## 0. What was read

- **Return folder:** `research_returns\GCT_KRON_checkpoint_01_20261120T2345Z_unzipped`. This is the newest present,
  checked at the start and again at the end of this intake.
- **A newer checkpoint landed during this intake:** `GCT_KRON_checkpoint_02_20261121T0030Z_unzipped`; the filer
  retired checkpoint 01.
  - *What did not change.* In 02 the ids are written with a hyphen (A001 → A-001). The text of A-001 to A-004 sits at
    the same lines of `agents\archive\ARCHIVE_FINDINGS.tex`. A-001 is also in `GCT_KRON.tex` line 246, and its
    inventory rows AR020, AR021 and AR024 agree with it. So every verdict below holds for checkpoint 02 under the
    hyphenated ids.
  - *What is new in 02 and not read:*
    - A-017 to A-022, including the degree gate n < N_d(dm);
    - F011 to F017, including the staircase λ_(54−2s) ≥ s+1 in the BIP range;
    - M011, M012.

    These are named from its LEDGER only. They move the GCT gates, not the cote 133 corrections.
- **Prompt as sent:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\26_GCT_KRONECKER_through_lambda_operations_on_G-sets\PROMPT.md`.
  A copy is in the checkpoint.
- **Read in full, with proofs:**
  - A001, A002, A003, A004, A012, A013: `GCT_KRON_work\agents\archive\ARCHIVE_FINDINGS.tex`, lines 1-185 and 548-689.
  - A009 at statement level with its locators.
  - The source page: `sources\ARCHIVE_133_scan019.tex`.
  - Our study: `sources\SA17_STUDY_cote133_lambda.md`, lines 480-600.
- **Read at statement level:**
  - `LEDGER.md`, `IMPLICATIONS.md`, `RESUME.md`;
  - `QUESTIONS.tsv`, all 45 rows: the QF, Q-O and QM rows, that is F-001 to F-008, O-001 to O-011, M001 to M009,
    F009, F010;
  - the check-event counts.
- **Not read:** the formula proofs (F-001 to F-008) and the obstruction proofs (O-, M-). The two-hundred-page
  assembled `GCT_KRON.tex` was read only at lines 55-66 and 1150-1160.
- **Computation (mine):** a table-of-marks script, `scratchpad\kron\marks.py`, for the free C2-set. It confirms A001
  under both readings of λ² (see section 2). I checked A002's V4 marks by hand.

## 1. The point the run raised: the degree-two Burnside identity of our study

**Grothendieck's page (cote 133, scan 019; transcription lines 1-56).** Over finite G-sets he writes:

- λ^i(E) = e(P_i(E)), with P_i "unsure" in the transcription;
- σ^i(E) = e(Sym^i E);
- the boxed σ_t(E)λ_{-t}(E) = 1;
- then σ²(E) = E² − λ²(E), E×E ≃ σ²(E) + λ²(E) and σ²(E) = λ²(E) + E;
- the boxed 2λ²(E) + E = E², with the count 2·d(d−1)/2 + d = d²;
- and "λ^i(xy) = ?".

**What our study says.** `SA17_STUDY_cote133_lambda.md`, section "Scan 19: λ- and σ-operations", the **Checked**
line: "at order 2 the two descriptions agree. With λ² = 2-subsets and σ² = 2-multisets, E² − λ² = λ² + E = σ²."

**Verdict: the run is right, and the study's check is wrong** (targeted proof check plus computation). Take G = C2
and E its free orbit (two points, swapped). Marks are given at (1, C2):

| class | marks |
|---|---|
| E | (2, 0) |
| E×E = 2E | (4, 0) |
| P_2(E), the one 2-subset, fixed | (1, 1) |
| Sym²E | (3, 1) |

- *The subset reading.* σ² = λ² + E holds: a 2-multiset is either a repeated point or a 2-subset, an equivariant
  bijection. But E×E ≠ σ² + λ²: (4, 0) against (4, 2). And 2λ² + E ≠ E²: (4, 2) against (4, 0). The boxed
  σ_tλ_{-t} = 1 fails in degree two, since σ² − E·E + λ² has marks (0, 2).
- *The reading λ = λ^B, defined by the boxed σ_tλ_{-t} = 1.* Then λ²_B(E) = E² − σ²(E) = E − 1, marks (1, −1). This
  class is virtual, and it linearizes to the exterior square, the sign character. Now σ² = λ² + E fails, and the boxed
  2λ² + E = E² still fails: (0, −2) + (2, 0) = (2, −2) against (4, 0). The run states only the subset reading; this
  reading is my addition.
- *The conclusion.* Under either reading the page's three relations hold together only after taking cardinalities.
  Forgetting the action hides the error.

**The structure behind it.**
- E×E = Δ ⊔ Mon(I_2, E). The ordered pairs of distinct points map onto P_2(E) as an S_2-torsor, and this torsor
  need not be trivial. It is nontrivial for the free C2-set, where the stabilizer of the subset swaps its two
  elements.
- The signed formula that is right in B(G) is Bouc-Rökaeus, Theorem 1.1, formula (1.2), as the run cites:
  λ^B_n(S) = (−1)^n Σ_{μ⊢n} (−1)^{ℓ(μ)} (ℓ(μ)!/∏_j α_j(μ)!) [P_μ(S)].
- His question "λ^i(xy) = ?" has a negative answer for λ^B, which is not special (A002). The V4 counterexample is
  checked by hand, marks included. The same holds for the subset operations (free C2: the difference has mark 4).

### The correction for our study (SA17's study of cote 133)

In `SA17_STUDY_cote133_lambda.md`, in the section "Scan 19: λ- and σ-operations", the line under **Checked**
(source line about 491) should be replaced by:

> **Checked:** only the cardinalities agree (2·C(d,2) + d = d²). In the Burnside ring the page's relations are not
> compatible. With λ² = 2-subsets and σ² = 2-multisets, σ² = λ² + E holds: a 2-multiset is a repeated point or a
> 2-subset. But E×E ≠ σ² + λ² and 2λ² + E ≠ E². For E the free C2-orbit, E² = 2E while 2λ² + E = 2 + E; their
> C2-fixed-point marks are 0 and 2. The correct decomposition is E×E = E ⊔ Mon(I_2, E), where Mon(I_2, E) → P_2(E)
> is an S_2-torsor that need not be trivial. If instead λ is defined by the boxed σ_tλ_{-t} = 1, then
> λ² = E² − σ² (= E − 1 for the free C2-orbit) is a virtual class that linearizes to the exterior square, and
> σ² = λ² + E fails. The signed formula is Bouc-Rökaeus, Theorem 1.1 (1.2). His question "λ^i(xy) = ?" has a
> negative answer for these operations, which are not special (V4 counterexample). Source: GCT_KRON (GPT-6 Astra,
> ChatGPT Pro mode), checkpoint 01, A001 and A002; checked by the intake of 21 Nov 2026 (Claude Opus 5.5 at effort
> high), with a table-of-marks computation.

### Further corrections to the same study from this checkpoint

1. **Scans 24-27, "Foncteurs spéciaux"** (study, about line 522).
   - *The fault.* "finite sums of h_I, equivalently direct summands of H_I" is false as written. h_1 ⊔ h_1 has value
     2 at a singleton, and every H_J has value 1 there.
   - *The fix.* Read: "finite sums of the h_I, equivalently direct summands of finite sums of the H_J; each H_J is the
     sum of copies of h_I indexed by the equivalence relations on J" (A012).
   - *Check.* Proof read: confirmed. Whether the fault is Grothendieck's or the study's needs the scan image. The
     run had no images (the scans were not supplied).
2. **Scans 28-29, "Open: ... Whether Z_p-lattices give the polynomial ring is not settled here."** Now settled:
   - *Yes for Z_p-lattices* (A013): K_0 of Z_p-free Z_p[S_n]-modules → R_{Q_p}(S_n) is an isomorphism, so
     ⊕_n R_{Z_p}(S_n) = Z[ρ_1, ρ_2, ...]. The proof: lattice K_0 = G_0; torsion classes are killed by the
     unitriangular decomposition matrix and p·S^λ.
   - *Proof read: confirmed.* The result is classical, the Heller-Reiner/Swan form of the decomposition sequence;
     the run re-proves it.
   - *The study's sentence "Characteristic 0 is necessary for the argument above" should be qualified.* Residue
     characteristic p is allowed for lattices over Z_p. But characteristic 0 of the ring is not sufficient:
     A = Z_(2)[ε]/(2ε, ε²) is a counterexample (the trace of the transposition on L is 1 + ε, which is not an
     integer). Proof read: confirmed.
3. **Scans 2-9, the Stiefel-Whitney point.** The study says of w(H(E)) = Σ (1+α)^{r−k} c̄_k(E) and of the "c₁ ?"
   answer: "The result is new in this reading."
   - *The run's objection.* The hyperbolic formula is the Proposition of Esnault-Kahn-Viehweg, *Coverings with odd
     ramification and Stiefel-Whitney classes* (J. reine angew. Math. 441, 1993), §5.5, pp. 183-184 (A009).
   - *What I did.* I did not open EKV, so this is carried at statement level.
   - *The edit.* If EKV §5.5 confirms, drop "new in this reading" and cite EKV.
4. **Scan 28, the monomial Cauchy formula** (A004, confirmed). The study's reading of the formula as the Cauchy
   identity is right. Grothendieck's question whether the summands are actual direct summands for effective ξ has
   the answer no in the monomial basis. For the standard representation E of S_3, ψ²(E) = 1 + E − ε has a negative
   coefficient; the characters (2, 2, −1) are checked. The study does not take up this question; add it as a line
   under scan 28.
5. **Agreements, no edit.** On scan 6 the run's A006 (WG is not pre-λ where 2 is not invertible) agrees with the
   study's "new in this reading" correction. The run's A005 (the split WG is not special, BC_3 over F_3) bears on
   the study's open H-133-1, the λ-ring question for split WG. It answers it in the negative for specialness. A005
   was not read by me.

## 2. Verdicts

| id | statement | check | verdict |
|---|---|---|---|
| A001 | subset reading of scan 019 contradicts the boxed identity; σ² = p_2 + E and λ²_B = E² − σ² are the correct ones | proof read; marks computed for both readings | confirmed (+ computation); I add the λ^B reading |
| A002 | Burnside λ^B not special; V4 counterexample; subset structure not special either | marks of λ^B_2(E), λ²(X_1X_2) recomputed by hand | confirmed; known in general (Bouc-Rökaeus Th. 1.1), as the run says |
| A003 | no nontrivial irreducible is the linearization of an effective G-set | invariants = number of orbits | confirmed (elementary) |
| A004 | monomial Cauchy summands not effective (S_3 standard rep) | characters checked | confirmed |
| A012 | "finite sums of h_I = summands of one H_J" false; finite sums of H_J correct | value at a singleton; components of H_J | confirmed |
| A013 | R_A(S_n) induction ring polynomial: yes for local Q-algebras and for Z_p-lattices; no for F_p and for Z_(2)[ε]/(2ε, ε²) | proof read in full | confirmed (Z_p part classical) |
| A009 | the hyperbolic Stiefel-Whitney formula is in EKV 1993 §5.5 | statement and locator only | not read in full |
| A005-A008, A010, A011, A014-A017 | the other archive audits (WG, Witt quotient, the topos caveat, the integral Cauchy identity, injection powers, big Witt, Borger) | not read | not read |
| F-001 to F-008, F009, F010 | positive formulas for two-row, hook and rectangle families; the evaluation-rank formulation | statement level | not read in full |
| O-001 to O-011 | saturation holes (GCT IV Prop. 18.6), the stable-tail all-t ≥ 2 theorem, the parity ray against GCT VI | statement level | not read in full |
| M001 to M009 | projection containment; the universal linear determinant of size S(m,r) = C(m+p,p) + C(m+q,q) − 1; row exclusions | statement level; the row counts recomputed (see below) | not read in full; the numbers are consistent |

**The arithmetic check of M008.** With p = floor((r−1)/2) and q = ceil((r−1)/2), S(m,r) ≤ 3m^4 holds for every m ≥ 2
exactly when q ≤ 4, so r ≤ 9. S(m,r) ≤ m^25 for every m holds exactly when q ≤ 25, so r ≤ 51. This matches "≤ 9 rows
at n > 3m^4, ≤ 51 rows at n ≥ m^25". The universal determinant M007 and the comparison M006, on which these rest,
were not read by me.

**Counts:** 6 findings read in full and confirmed (2 with computation); 1 at statement level with a locator (A009);
the rest (about 40 statements) at statement level. Nothing refuted by me.

## 3. What is new

- **Against the literature.**
  - *A001 and A012.* They are corrections of the archive text and of our study. A002's non-specialness is known
    (Bouc-Rökaeus); the run says so. A013's Z_p case is classical; its singular counterexample is a small new
    example.
  - *The GCT-side results (M007-M009, F009, F010).* They may be new: a universal determinantal size for padded
    r-variable forms, and the row exclusions for multiplicity obstructions in the IP and BIP ranges. They are not
    yet read in full. The universal determinant must be checked against the known determinantal-complexity bounds
    for forms with few variables (Valiant; Grenet's 2^m − 1, which the run itself uses as F009) before it is called
    new.
- **Against our own results.** A001 overturns a "Checked" line of our study (section 1). A013 answers the study's
  open Z_p row, and A009 contests one of its novelty claims.
- **Against tonight's runs.** GCT_PLETH (prompt 25) treats the same cote 133 λ-ring pages. Its intake should
  receive A001 and A002, so that the subset/λ^B distinction is used there too.

## 4. Scope of the two proofs

- The run uses neither Alpöge nor Masullo; GCT_KRON.tex, lines 58-63 and 1150-1155, say so explicitly.
- Its purity remarks (QM005: a pure rank-one exterior power with trace −1) concern Frobenius weights on finite-field
  points. They use no L-function input.
- No statement claims more than its input gives.

## 5. Integration: how the findings bear, and the next attack

1. **Cote 133 (scans 19, 24-29) and the study SA17.** Make the edits of section 1, in our study file, by whoever owns
   it; I made no edit outside my folder. The reading of scan 019 changes:
   - *What the page reaches for.* Grothendieck reaches for a λ-structure on the Burnside ring 𝓔(G) compatible with
     the map to R(G).
   - *Why the page fails.* The subset operations give the right cardinalities but forget the signs; that is, they
     forget the S_2-torsor Mon(I_2, E) → P_2(E).
   - *The right structure.* λ^B (σ_tλ_{-t} = 1) linearizes correctly but is virtual and not special.
   - *The open attack.* The attack this makes possible is his own "λ^i(xy) = ?". The correct object is the ring of
     G-sets with an S_n-torsor, or orientation, datum. That is exactly the oriented-subset construction that
     linearizes to Λ^i, and its specialness question is open in the run. The successor should ask it.
2. **GCT, where the route stops (F010, the QMMAIN row).**
   - *What the reductions leave.* The run's reductions (M006-M009, F009) cut the candidate multiplicity
     obstructions to shapes with at least 10 rows (IP range) or 52 rows (BIP range), and to m ≥ 19 or m ≥ 190.
   - *The exact obstacle.* It is located in F010: the ranks of the evaluation tensors of the permanent and the
     determinant on the highest-weight spaces. Ambient λ-structure and positivity of occurrence do not determine
     these ranks.
   - *The next attack.* Compute these evaluation ranks at the first open shapes (10 rows, small m), or bound them by
     the tensor-rank methods of GCT_GINEQ (F-13/F-23: substitution on flattening images). This is the natural
     bridge between runs 26 and 27.
3. **The positive formulas (F-001 to F-008)** feed GCT_PLETH's and GCT_NSRH's rows on positivity for two-row, hook and
   rectangle families. Integrate them once read in full; the final will be the version to read.
4. **Prompts 30-36.** Only 36 (CUE_GCT) is near: M006-M009 and F010 are background for its Noether-normalization
   and PIT side. Prompts 30-35 are untouched.

## 6. Prompt updates for the successor of GCT_KRON

1. Give the run this intake's section 1. It should adopt the λ^B reading as well as the subset reading for every
   cote 133 statement, and state the Burnside identities with marks, not cardinalities.
2. Ask for the oriented version of "λ^i(xy) = ?" (item 5.1) as a main question: G-sets with an orientation or
   S_n-torsor datum, their λ-structure, and its specialness.
3. Make the evaluation-tensor-rank comparison of F010 the main GCT question, with GCT_GINEQ F-13/F-23 attached as
   tools, and an explicit computation at the first unexcluded shapes.
4. Ask for EKV 1993 §5.5 to be checked against cote 133 scan 009, with the exact statement.
5. Ask for the scan images of cote 133 scans 19-29 to be supplied. The run read only transcriptions, so A012 cannot
   tell Grothendieck's slip from ours.
6. Provenance: name the run "GPT-6 Astra (ChatGPT Pro mode)".
7. No minimums and no ways out, as before.

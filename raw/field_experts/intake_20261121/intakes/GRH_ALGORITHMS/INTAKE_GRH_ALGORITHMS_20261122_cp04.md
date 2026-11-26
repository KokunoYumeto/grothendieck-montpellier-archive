# Intake of GRH_ALGORITHMS checkpoint 04 (prompt 67), first intake

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode), still going: checkpoint 04 was saved at 23:20 UTC and its first three-hour review is at the same time.

Return: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_ALGORITHMS_checkpoint_04_20261122T2320Z_unzipped`
(below `G`). Prompt as sent: `<local>/Documents\TO_SEND\PRO\1_Archive_research_by_topic\67_GRH_ALGORITHMS\PROMPT.md`.

A is Alpöge's theorem as the run states it (paper §1): every nontrivial zero of every Dirichlet L-function, ζ
included, has real part 1/2. The run did not replay the Lean.

## 0. What was read, and what was not
- **Read:**
  - the prompt as sent, in full;
  - QUESTIONS.tsv, all nine rows;
  - LEDGER.md and CHECKPOINT_STATUS.md, in full;
  - STATEMENTS.tsv, all 71 rows, at statement level;
  - the paper's opening: abstract, §1 table, the Tang theorem and its scope paragraph;
  - the full proofs of Lemma `lem:dirichlet-log-weight` (P056), Proposition `prop:auxiliary-character-sieve` (P057)
    and Theorem `thm:fixed-r-almost-all-auxiliary` (P058);
  - the start of the proof of `cor:uniform-r-almost-all-auxiliary` (P059);
  - the statements of `thm:aa-12r` (P068), `cor:aa-finite-field-algorithms` (P069) and `thm:almost-all-small-tate`
    (P071);
  - the paper's subsection on the local revision to Cureton-Thorner;
  - §5 of `workbench/research/classical/special_kummer_basechange.md`;
  - the imports and file writes of all seven programs, and two of them (check_tang_17_3.py, check_kummer_examples.py)
    in full.
- **Not read:** the rest of the 6674-line paper (80 pages) and of the research notes, CHECK_EVENTS.tsv row by row,
  DICTIONARY.md, CROSSWALK.tsv.
- **The prompt's attachment was not reopened.** The coordinator reports that it carries masullo_trace_selected.txt and
  three GRH_NIGHT modules on Masullo's draft.

## 1. Masullo's claim in this run
The prompt named "M, A. M. Masullo's unrefereed claim of GRH for all Hecke L-functions", to be used only in
conditional remarks.

**The run does not use M anywhere:**
- The paper contains no occurrence of "Masullo" and no hypothesis M. Every result beyond A names its exact L-function
  instead: RH(ζ_{Q(p^{1/r})}), RH of a ring class field's zeta, the ideal-class Hecke characters, and so on.
- Only two workbench notes mention him: `research/classical/special_kummer_basechange.md` §5 and `search_log.md`.
- §5 inspects the GRH_NIGHT files on his draft and concludes that their strip quotient "supplies the identity with
  zeros, not this strict lower bound". Positivity there "is a zero-location assertion, not a free consequence of the
  existence of a Hilbert completion". This agrees with MA-HM-003.
- The heading of §5 reads "What the Masullo-Meyer quotient repairs …", taking the archived files' word. Under the
  rule of 22 Nov, that heading is restated before the workbench is published: these are our own constructions in
  Meyer's setting, not repairs of the draft.

**So no follow-up 67b is needed:** the running chat does not build on M as if it were proved. I drafted none.

## 2. What the run proves, by input

### Unconditional (no Riemann hypothesis)
- GRH-P004 (`thm:teich`): a presentation of F_{p^r} is equivalent to a maximal Teichmüller unit (CX-ALG-023).
- P005: the valuation-one construction.
- P007: a nonzero zero-divisor from a maximal coefficient unit.
- P011, P012: Tang's two reductions (Frobenius factoring with at most n−1 prime-field queries; presentation from p, m).
  They are unconditional given a prime-field factoring interface.
- The method restrictions: P018-P021, P032-P034 (finite menus and global r-units fail), P045 (least cyclic discriminant
  equals least auxiliary prime to the power r−1), P046-P048, P060-P067 (tensor cone, twist conductor floor, restricted
  volcano selector equivalent to cube extraction).
- The finite computations: P023, P037, P052.
- The §1 rows marked "already unconditional": Solovay-Strassen, order from a factored exponent, Schoof, ECPP
  certificates.

### From A alone
- The §1 table rows marked "From A":
  - Miller's test with bases below 2 log² n;
  - r-th nonresidues mod p for r | p−1;
  - primitive roots given the factorization of p−1;
  - Shoup's g(p) ≪ log⁶ p;
  - the order/factoring equivalence;
  - the least prime in a progression, (φ(q) log q)²;
  - the Rubinstein-Sarnak limiting distribution (but not the strict race densities, which also need grand simplicity).
- P006: nonresidues in a presented extension (CX-N13).
- **New, almost-all statements:**
  - **P058:** for each fixed odd r and C_r > (r−1)/log r, all but O(√P log log P) primes p ∈ (P/2, P] have an
    auxiliary prime ℓ ≤ C_r log P log log P with ℓ ≡ 1 mod r and p^{(ℓ−1)/r} ≢ 1 mod ℓ. So F_{p^r} is built in
    polynomial time on those inputs.
  - **P059:** uniformly in r, with B = C r² log²(Pr), the exceptions are O(√P r² log²(Pr)/log P).
  - **P068:** one table ℓ ≡ 1 mod 12r, ℓ ≤ C₀ r² log²(Pr), serves every prime r ≤ D ≤ (log P)^{a₀}, outside
    O(√P D³ log²(PD)/log P) primes p.
  - **P071:** an explicit cubic Y³ − (k+3)Y² + kY + 1 with k ≤ C log P log log P for almost all p ≡ −1 mod 9.
- **What A does not reach:** an all-input construction. Exceptional primes remain (Q01, Q02 open).

### A plus one named extra zeta function
- **P001** (`thm:kummer`, CX-ALG-024): under A, RH(ζ_{Q(p^{1/r})}) ⇔ RH(ζ_{Q(ζ_r, p^{1/r})}). Either gives an
  auxiliary prime and the classical construction of F_{p^r}.
- **P008** (CX-N15): quasipolynomial factorization from RH for the finite family ζ_{Q(p^{1/r})}, r ∈ 𝓑, given the
  cited IKRS algorithm.
- **P017:** a one-sided finite-window inequality suffices. Its derivation from A is open.

### Conditional on outside, unrefereed preprints
- P009, P010, P013, P069, P049, P050 rest on:
  - Cureton-Thorner, "A quasi-Riemann hypothesis for Dedekind zeta functions", Hexagon 2610.00200v2, Theorem 1.1: a
    fixed zero-free strip for all Dedekind zeta functions;
  - OpenAI's preprint of 4 Oct 2026, Theorem 1.2 and Proposition 10.1;
  - Tang, Hexagon 2611.00135v2.
- What they give:
  - P009: polynomial-time factoring and construction (Tang's theorem);
  - P010: auxiliary primes from two zeta strips;
  - P013: the invariant-form replacement in Cureton-Thorner Lemma 8.1, which is Tang's revision. The official v2
    needs it.
  - P069: average polynomial interfaces, using A and OpenAI's algebraic theorem;
  - P049: polylogarithmic ray-class generators, with exponent 32;
  - P050: Koiran's HN ∈ AM.
- The paper says "the cited external theorems state unconditional results". That is the authors' claim. These are
  unrefereed preprints, and the Cureton-Thorner one needed a local repair by Tang. A reader should see them as named
  inputs, as the paper does for A.

### Still beyond A, needing the Hecke L-functions named
- Hooley's Artin density: RH for ζ of Q(ζ_k, a^{1/k}).
- Bach's 12 log² |D_K| class-group bound, and Hafner-McCurley-type mixing: ideal-class Hecke characters.
- The elliptic isogeny expanders over imaginary quadratic K.
- CM/CRT split-prime selection: the ring-class zeta.
- None of these is conditional on Masullo. Each is conditional on GRH for the L-functions named, an open hypothesis.

## 3. Converging or stalled
The first three-hour review (23:20 UTC) records movement: Q03 (the eighteen classical rows) and Q04 (the Tang
interfaces) moved from open to proved transfers.

The main questions stay open, and each gate is unchanged. Q01 (construct F_{p^r} from A alone in the hard case) still
waits on the one-sided window inequality, or equivalently the maximal Teichmüller unit. Q02 (a polynomial auxiliary
prime from A alone) still waits on new analytic control of one order-r Hecke function.

The almost-all theorems are new mathematics, but the run itself says they leave the uniform gate where it was. It is
early: one review so far.

## 4. Checks by us
| statement | what was done | outcome |
|---|---|---|
| P056 (lem:dirichlet-log-weight) | targeted proof check | confirmed given LLS2015 Lemmas 2.1-2.3 (source not opened). Uniformity in q is what A supplies |
| P057 (prop:auxiliary-character-sieve) | targeted proof check | confirmed. Orthogonality over characters mod M, coefficients of total mass one; the exceptional p contribute ≥ log(P/2) log 2 each |
| P058 (thm:fixed-r-almost-all-auxiliary) | targeted proof check | confirmed: r^m ≥ P from C_r > (r−1)/log r, and log M ≪ B |
| the seven programs | rerun from a folder of my own (stdlib only, read for imports and writes) | every output equals its recorded expected JSON: check_tang_17_3, check_kummer_examples, derive_cm_inputs, check_cm_15_135 (needs its sibling module on the path under -I), check_elliptic_17_3, verify_restricted_volcano, probe_cubic_routes (1599 hard cubic primes ≤ 100000) |

P001 and P004 were checked on 21 Nov as CX-ALG-024 and CX-ALG-023 (intakes GRH_NIGHT). Their wording in this paper
was not compared, so no new event is filed for them.

## 5. Outreach and Hexagon (drafts only, none written)
- **Hexagon, P058 and P068:** candidates, not ready. Gates:
  - a literature search on almost-all least auxiliary primes and large-sieve results for r-th power residues (for
    example Gallagher's larger sieve, and almost-all nonresidue bounds);
  - comparison with LLS2015;
  - a check of P068's proof.
- **Outreach:** none new. Tang's review already carries the Cureton-Thorner local revision.

## 6. Files of others
The return holds none: 180 files, our own .tex, programs and records, and the paper's PDF.

The prompt's ZIP is a separate matter: it carried Masullo extracts (`masullo_trace_selected.txt`) against the
coordinator's rule of 21 Nov. It has already gone.

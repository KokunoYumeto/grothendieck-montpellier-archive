# Intake of GRH_ALGORITHMS_FINISH (prompt 67c), checkpoints 02 and 04, by diff from GRH_ALGORITHMS checkpoint 08

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7, a second copy of af2a18f62da23b48e, cut
after it built 67c). The run is GPT-6 Astra (ChatGPT Pro mode), still going.

Return read: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_ALGORITHMS_FINISH_checkpoint_04_20261123T1744Z_unzipped`
(below `G`). It contains checkpoint 02's state. Checkpoints 01 and 03 were not downloaded.

The paper is `G\workbench\work\unfiled\v1\papers\grh_algorithms.tex`: 13229 lines, PDF of 159 pages.

A is Alpöge's theorem, RH for every Dirichlet L-function, ζ included. Masullo's draft is no input.

## 0. Scope
- **Read:**
  - QUESTIONS.tsv (9 rows), and LEDGER.md from the finishing run's start (14:44 UTC) to review 01 (17:44 UTC);
  - STATEMENTS.tsv P143-P146, the title, the abstract and the closing note;
  - the full proof of `thm:selected-cyclotomic-cofactor` (P145), which contains P144's threshold case;
  - the statements of P143 and P146;
  - the build report and the workbench note `research/classical/special_kummer_basechange.md`.
- **Not read:** the proofs of P143 and P146; the run's review reports in `checks/finishing/`; the paper beyond the
  places named.

## 1. Usefulness first
The finishing run widens the unconditional half of Lenstra's construction problem for F_{p^r}:
- Before, the cofactor had to be small after removing only its 2- and r-parts.
- Now every prime-power factor ℓ^k of Φ_d(p), with ℓ ≤ L and r ∤ ℓ − 1, is removed without roots of unity as inputs
  (P144/P145).
- So F_{p^r} is built deterministically, with no Riemann hypothesis, whenever Φ_d(p) is a product of r, 2, small
  primes not ≡ 1 mod r, and a small cofactor.

This bears on deterministic algebra over finite fields and on explicit constructions, the subject of Shoup and of Bach,
von zur Gathen and Lenstra. It also moves our fleet's succinct-plane construction (§8).

## 2. Verdicts
| id | statement | check by me | outcome |
|---|---|---|---|
| GRH-P145 `thm:selected-cyclotomic-cofactor` | For disjoint finite sets S, T of odd primes ≠ r dividing N = Φ_d(p): roots of order ℓ are supplied for ℓ ∈ S; nothing is supplied for ℓ ∈ T, but r ∤ ℓ−1. F_{p^r} and the maximal equivariant unit are then built in time (r + C + Σℓ + log p)^c, where C is N with its 2-, r-, S- and T-primary parts removed. | targeted proof check | **confirmed.** Details below. |
| GRH-P144 `thm:threshold-cyclotomic-cofactor` | The case S = ∅, with T the primes ℓ ≤ L dividing N with r ∤ ℓ−1; cost (r + L + C_L + log p)^c | targeted proof check, as a specialization of P145 | confirmed, since Σ_{ℓ∈T} ℓ ≤ L² |
| GRH-P146 `cor:fixed-set-cubic-cofactor` | Under A, for a fixed finite set S of odd primes ≠ 3: a cubic over F_p, p ≡ 2 mod 3, in time K_S(C_S(p) + log p)^{c_S} | statement only | the roots for ℓ ∈ S come from P140 (A-only residue maps for fixed real Galois fields) |
| GRH-P143 `thm:selected-menu-auxiliary` | Under A, any k = ⌈log P/(2 log r)⌉ progression primes ℓ ≡ 1 mod r below B = C r² log²(Pr) serve as a menu, with at most C₂√P·A_r(P) exceptional p in (P/2, P]; the proportion of exceptional hard primes tends to 0 uniformly for r = o(√P/log P) | statement only | an optimization of the P074 coefficient-mass-one method |

P145 in detail:
- The rational-function search with exponent rC (degree count B = rhC) gives δ with v = δ^C ≠ scalar and v^{N/C} = 1.
- Non-r branches use order ℓ only: a supplied root for ℓ ∈ S, −1 for ℓ = 2.
- For ℓ ∈ T, adjoin Φ_ℓ. This is étale of rank ℓ−1, since ℓ | q−1. Find y with y^r = z there and take
  b = Norm(y), so b^r = z^{ℓ−1}; Bézout with r ∤ ℓ−1 gives a root in the base.
- The order-r² branch is the odd-prime commutator.
- The support splitting keeps each comparison componentwise.

**Counts:** 2 confirmed (P145, P144); 2 at statement level (P143, P146). None refuted.

## 3. Part 2 and Part 3 of 67c, against the cp04 text
| item | state at cp04 |
|---|---|
| 1. title | "Unconditional finite-field constructions with small cyclotomic cofactors and fixed-valuation constructions under Dirichlet GRH, after Bach, von zur Gathen, Lenstra, and Pila". Done |
| 2. abstract | Done. It names Tang's two preprint inputs, and Cureton-Thorner's v2 with Tang's revision of Lemma 8.1 |
| 3. Cureton-Thorner | Done: no "separate unconditional zero-free theorem" remains |
| 4. theorems in words | reported done by the run (ledger 15:15); not reread by me theorem by theorem |
| 5. "Proof overview" | Done (§, line 707) |
| 6. why it matters, what is new | Done ("What is new here", line 687). The BGL and Pila comparisons are reported, not read by me |
| 7. structure | Done: `\part{Constructions and their analytic inputs}` and `\part{Routes that do not give a uniform construction}` |
| 8. process words | Done: "actual" and "retained" no longer occur; no internal ids, checkpoints or agents in the text |
| 9. closing note | Done: it names my checks of the average theorems, the cubic search and the root-extraction lemma |
| 10. workbench note | Done: §5 is "Constructions in Meyer's setting and the scope of Alpöge's remark"; the opening says the claims are conditional on GRH for the Hecke functions concerned |
| III.1 blind re-proofs P006, P008, P009 | Done: Q05, same-model statement-only reconstructions |
| III.2 étale descent P105-P110, P128/P131 | Done as a targeted author-proof audit, not a blind re-proof (ledger 15:26) |
| III.3 CM-theta P113-P126, P119 | Done: an adversarial audit, plus a statement-only reconstruction sealed 15:44 |
| III.4 build and pages | Done for the 151-page version: three-pass clean build, both full image readings (16:39), Parts 2/3 closed 16:49. The 159-page version with P143-P146 has a clean three-pass build (17:37). Its changed-page expert and newcomer readings are pending (Q06) |

**Verdict on the paper.** The 151-page version met Part 2 and Part 3. The current 159-page version needs only the
changed-page readings, and its final release is still to come.

## 4. What moved
- **Q01** ("partly proved") has a strictly smaller residual gate. The unconditional parameter is now C_L (P144-P146)
  instead of M₂.
- **Q05** closed: all main theorems re-proved by the same model.
- **Q03** has more precise qualifications.
- Q02 and Q07-Q09 are unchanged.
- Review 01 (17:44) counts movement: yes.

## 5. Scope of the inputs
- **Unconditional:** P144, P145.
- **Under A:** P143, P146 (with P140 at fixed-field scope), and P125/P126 (CM; A is used only for a small quadratic
  field).
- **Nothing uses Masullo.** Tang's interfaces rest on the named 2026 preprints, as the paper now says.

## 6. Integration
| file | edit | state |
|---|---|---|
| `reports_20261122/paper_seeds/SEED_MAS_ARTIN.md`, Paper 2 research question | appended the status of 23 Nov: partly settled, with P125/P126 and P144/P145 | applied (backup in `integration_backups/20261123/GRH_ALGORITHMS_FINISH/`) |
| `field_experts/hexagon/HEXAGON_BOARD.tsv`, row H29 | add P144/P145 (threshold cofactor C_L) and P143 | for the main session |
| `pequalnp_work/fleet_map/maps/analytic_number_theory.md`, row ANT-07 | update to cp04 (see §8) | for the main session |
| `results_register/CHECK_REGISTER.tsv` | add this intake's check events | for the main session |

The log is `INTEGRATION_GRH_ALGORITHMS_FINISH_20261123.tsv`.

## 7. Board candidates (rows for `HEXAGON_BOARD.tsv`)
| title | statement | what it adds | gate left |
|---|---|---|---|
| Finite fields of prime degree from a small cyclotomic cofactor, unconditionally | P145/P144 as in §2 | Lenstra's construction problem, unconditionally, for every p whose Φ_d(p) is r-, 2- and small-non-1-mod-r-smooth up to a small cofactor | the BGL 2001 comparison read by us; the étale simulation checked by us |
| Prime-degree finite fields from Dirichlet GRH at fixed valuation | P126 (with P119 at r = 3) | removes the exceptional characteristics at each fixed (r, b) | a whole check outside the run of the CM-theta proof |
| Short auxiliary-prime menus for almost all primes | P143 (P074, P092) | uniform density among hard inputs for r = o(√P/log P) | a check of P143 by us; the average-literature comparison |

## 8. For the P vs NP fleet
**Map, constructed:** row ANT-07 of `fleet_map/maps/analytic_number_theory.md` (from cp02).
- Nodes: L-meta-606, 608, 612, 649, 650, 660, 661, 766, 885 (succinct hard families over all prime powers q),
  L-clb-009/010/013, and L-meta-664/683 (characteristic 2).
- Translation: a succinct description of a projective plane over F_q needs F_{p^r}, and a primitive element of
  F_{q³}, in time poly(r log p). This is Lenstra's construction problem.
- **Update from cp04:** P144/P145 cover every q = p^r for which Φ_{ord_r p}(p) is, apart from r, 2 and primes ≤ L not
  ≡ 1 mod r, a cofactor polynomial in log q.
  - For p = 2 (Denniston arcs), Φ_d(2) for small d is explicit and the covered q = 2^r are those with a small residual
    cofactor. Computing that list is the next step.
  - P146 gives every cubic over F_p under A with fixed S.
- **The work to complete the bridge:** state the succinct plane language with its decider built on P144/P145; list the
  covered r for p = 2 up to a bound; write a new node for succinct planes, since none exists.
- For the main session to apply.

## 9. Prompt updates
None needed for the running chat. After its final:
- intake P143 and P146 in full;
- read the BGL and Pila comparison paragraphs;
- check the étale simulation ourselves before any post.

## 10. Hexagon readiness (five tests)
P145/P144:
- complete: yes;
- self-contained: yes;
- stable: no, the run is still going;
- checked: my targeted check, plus the run's;
- of interest: yes.

Gate: the run's final; and the BGL comparison read by us.

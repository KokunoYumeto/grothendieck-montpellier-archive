# Intake of GRH_ALGORITHMS checkpoint 08 (prompt 67), by diff from checkpoint 05

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode), still going: checkpoint 08 is from 02:24 UTC, and its paper is 148 pages. Return:
`<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_ALGORITHMS_checkpoint_08_20261123T0224Z_unzipped`.

A is Alpöge's GRH for Dirichlet L-functions, a theorem. The paper does not use Masullo's claim.

## 0. Read and not read
- **Read:**
  - QUESTIONS (all nine rows), STATEMENTS P099-P142 (44 new), the LEDGER's last review and build note, the title and
    abstract;
  - the statements of the two new main theorems (`cor:two-primary-cyclotomic-cofactor`, `thm:fixed-wild-cm`, with its
    corollary) and of `thm:small-cyclotomic-cofactor`;
  - the full proof of `lem:projected-primary-root-extraction`;
  - CHECK_EVENTS for the main theorems, a search of the paper for process words and for "unconditional zero-free",
    the closing note.
- **Not read:** the proof of the fixed-(r, b) CM theorem (sextic CM periods, theta recognition, P113-P118, P121-P127),
  the étale simulation (P105-P110), the new restriction propositions, and the rest of the 148 pages.

## 1. What moved
**Q01 changed from open to "partly proved".** Three new constructions of F_{p^r}:
1. **Unconditional:** `thm:small-cyclotomic-cofactor` (P128) and its strengthening `cor:two-primary-cyclotomic-cofactor`
   (P131).
   - Statement: a monic irreducible polynomial of degree r over F_p, together with a maximal equivariant unit in
     F_p[Z]/Φ_r, is constructed in time polynomial in r, log p and M₂.
   - Here M₂ = Φ_d(p)/(2^{v₂} r^a), with d = ord_r(p). No factorization of M₂ is input.
   - So a promise M₂ ≤ (r + log p)^C gives polynomial time with no Riemann hypothesis, whatever the valuation a.
   - The P130 special case: unconditional cubic fields when every odd prime divisor of p+1 is a Fermat prime.
2. **From A alone:** `thm:fixed-wild-cm` and `cor:fixed-wild-prime-degree-field` (P125, P126).
   - Statement: for every fixed odd prime r and fixed valuation b = v_r(p^{ord_r p} − 1) ≥ 2, F_{p^r} is constructed in
     time C_{r,b}(log p)^{c_{r,b}} for every p, with no exceptional characteristics.
   - Method: Pila's Frobenius polynomials of a CM abelian variety of dimension r^{b−1}, Mumford theta equations, and
     Lenstra's descent.
   - P119 is the case r = 3, b = 2: ninth roots and cubic fields when v₃(p+1) = 2.
3. **Supporting results:**
   - P140: A-only residue maps for fixed totally real Galois fields;
   - P105-P110: arithmetic simulated over a squarefree étale algebra, with Pila point counting over all its components;
   - restrictions P132-P142.

**Still open.** A bound polynomial uniformly in r and log p, when both the valuation and the cofactor grow. Q02 (the
classical auxiliary prime from A alone) is open.

## 2. Checks by us
| statement | done | outcome |
|---|---|---|
| lem:projected-primary-root-extraction (inside P128/P131) | targeted proof check | **confirmed.** Details below. |
| P128, P131 | — | the descent from the field lemma to the formal algebra (the étale simulation P107) was not read. No event beyond the lemma. |

For the lemma:
- the scalar-coboundary step gives δ^r = 1;
- specializing α ↦ b gives H(i)^{rM} = 1 at trM points, while the numerator minus the denominator of H^{rM} has degree
  ≤ trM − 1, so H is constant;
- that contradicts H(0) = η^{E_d} ≠ 1, since r ∤ E_d = ∏_{ℓ|d}(1 − p^{d/ℓ}), and H(∞) = 1;
- the odd-prime commutator (Bach-von zur Gathen-Lenstra, §5.10) yields the zero divisor;
- the gcd then gives the root.

The run's own checks are statement-alone same-model re-proofs of P119, P125, P126, P128 and P131, and a computation for
P128 and P131 (CHECK_EVENTS).

## 3. Hexagon readiness
| result | status | one gate left |
|---|---|---|
| P128/P131: unconditional F_{p^r} in time poly(r, M₂, log p) | proved; lemma checked by us; same-model re-proof | **The comparison with Bach-von zur Gathen-Lenstra 2001** (Finite Fields Appl. 7, 5-28), whose smooth-cyclotomic factoring may already cover a small cofactor. Then a check of the étale simulation. |
| P126: F_{p^r} from A alone for each fixed (r, b) | proved; same-model re-proof; not checked by us | an independent check of the CM-theta construction (P113-P118, P121-P125), a long proof |
| P074 and P092: almost-all auxiliary primes; logarithmic cubic search | proved; checked by us at cp05 | the paper's opening fixes (below). The literature search is done. |

## 4. The paper, and what the finishing prompt 67c needs
Measured against `pro_prompt_builds\PAPERS_20261122\core\HOW.md`; box 8 is now a section headed "Proof overview". These
are the cp05 fixes, with their state at cp08.

1. **Title**: "Deterministic finite-field constructions after Alpöge, Bach, von zur Gathen, Lenstra, Mumford, and Pila".
   It now lists six names and still not the question. Retitle it around the result (the unconditional cofactor theorem
   and the fixed-valuation theorem from Dirichlet GRH). Keep "after" for whose idea is carried out (Pila's, BGL's).
2. **Abstract**: rewritten and better. It opens with BGL and Pila and states both new theorems. It still does not say
   that Tang's polynomial-time interfaces rest on two 2026 preprints.
3. **Cureton-Thorner**: still called "the separate unconditional zero-free theorem" (lines 411 and 11933). It must be
   stated as a 2026 preprint theorem whose v2 needed a repaired lemma.
4. **Box 3**, the theorems in words: present after the fixed-valuation corollary ("In words, ..."). Needed after every
   main theorem.
5. **Box 8**: there is only a "Why the proofs work" paragraph (line 534). It needs a section headed "Proof overview":
   the mechanism of the cofactor theorem, the fixed-valuation CM theorem and the averages, and where each hypothesis
   enters.
6. **Structure**: 148 pages, with the route restrictions spread through the body. Make them a titled later part, or
   split the paper. The cofactor and fixed-(r, b) theorems are the paper now.
7. **Blind re-proofs**: still none for P006, P008 and P009. The new main theorems have them.
8. **Process words**: "actual" occurs at lines 10216 and 11281, and "retained" at 10522 and 11207, as process words.
   "Supplied" at lines 3466, 9022 and 10187 is mathematical.
9. **Closing note**: name the checks by Claude Opus 5.5 at effort high on 23 Nov: P074 and P092-P095 at cp05, and the
   root-extraction lemma at cp08.
10. **Workbench note** `research/classical/special_kummer_basechange.md`: "repair" still occurs twice, including the
    §5 heading on Masullo. Reword it. These are our constructions in Meyer's setting.
11. **Build and QA**: the ledger reports a clean three-pass build at 02:23. `checks/` holds no cp08 build report (only
    cp05's). The full-page visual inspection and the two complete readings are still pending.
12. **Novelty**: the BGL 2001 comparison for P128/P131, stated by statement and page.

Follow-up 67b (cp05 fixes) was drafted and not sent. 67c should carry this list instead. Running threads are
unreachable after an hour or two, so 67c goes as the finishing prompt.

## 5. Not for GitHub
The return holds no third-party files that I found; I did not screen it again at cp08.

# Intake of GRH_ALGORITHMS checkpoint 05 (prompt 67), by diff from checkpoint 04, with a review of the paper

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode), still going. Checkpoint 05 is from 00:05 UTC; its next review was at 00:20 UTC.

Return: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_ALGORITHMS_checkpoint_05_20261123T0005Z_unzipped`
(below `G`). Earlier intake: `INTAKE_GRH_ALGORITHMS_20261122_cp04.md`. Paper standard used:
`<local>/Documents\pro_prompt_builds\PAPERS_20261122\core\HOW.md`, "What a paper has to be".

## 0. What was read, and what was not
- **Diff:**
  - QUESTIONS: the statuses of Q01-Q09 are those recorded at cp04;
  - STATEMENTS: 98 rows, 27 new (P072-P098);
  - LEDGER and CHECKPOINT_STATUS, in full.
- **The paper** (`G\workbench\papers\grh_algorithms.tex`, 8223 lines; PDF of 98 A4 pages):
  - read the title, abstract, all of Section 1 and the "Why the proofs work" paragraph;
  - read the start of the Tang section, the final section and the closing note;
  - read the proofs of the fixed-degree average (P074) and of the logarithmic cubic search with its two lemmas and
    corollary (P092-P095);
  - searched the whole text for banned words and identifiers;
  - rendered PDF page 1 and looked at it.
- **Also read:**
  - DEPOSIT_SHEET.md and LITERATURE.md, in full;
  - the build report `checks/checkpoint_05_build.json`;
  - CHECK_EVENTS.tsv, counted by type and checked for the main theorems.
- **Not read:** the body sections beyond those named (the method-restriction propositions P072-P073, P076-P091,
  P096-P098 and earlier ones), and the PDF beyond page 1 and a text extract of page 98.

## 1. What moved since checkpoint 04
- **Main questions:** none moved. Q01 (construct F_{p^r} from A alone for every hard input) and Q02 (the short
  auxiliary prime from A alone) are open, with the same gates.
- **New, from A alone:**
  - **P074** halves the threshold of the fixed-degree average: C_r > (r−1)/(2 log r), because only r^m ≥ √P is
    needed. For r = 3, C₃ = 1.
  - **P092** (with P093-P095) shortens the explicit cubic search from C log P log log P to **C log P** candidates,
    C > 1/log 3, for all p in (P/2, P] outside O(√P log log P). The tool is Cilleruelo's quadratic-value product
    estimate: k² + 3k + 9, k ≤ K, has at least (1/2 − o(1))K private prime divisors above K + 3. These give linearly
    many independent cyclic cubic characters.
- **New lower comparisons, under A** (P077-P079, after Montgomery's character-product construction): exceptional hard
  primes do exist, at the logarithmic-product scale.
- **New method restrictions and reductions:**
  - P072, the two ordinary trials over F_{p⁴}: unconditional;
  - P080-P091: ordinary prescribed radicand, rational Kummer orbits, twist pools, untwisting cost;
  - P096-P097: the supersingular point is equivalent to the maximal cubic unit;
  - P098: unconditional, infinitely many hard primes defeat both ordinary trials.
- **Masullo:** the paper still has no mention of Masullo and no hypothesis M. The workbench note
  `research/classical/special_kummer_basechange.md` §5 still has the heading "What the Masullo-Meyer quotient repairs",
  and its line 9 speaks of "the archived Masullo repairs". Both must be reworded before publication.

## 2. Checks by us
| statement | done | outcome |
|---|---|---|
| P074 | targeted proof check | confirmed: r^m ≥ √P gives P/r^m ≤ √P, and log M ≪ B = C log P log log P |
| P093 | targeted proof check | confirmed: Stirling, the small-prime valuation sum ≤ K log K + o, and at most one large prime per value |
| P093 | computation | |S_K|/K = 0.609, 0.630, 0.641 at K = 10³, 10⁴, 4·10⁴, consistent with ≥ 1/2 |
| P094 | targeted proof check, plus computation | confirmed. Recomputed symbolically: disc(Y³ − (k+3)Y² + kY + 1) = N(k)²; the shifted Eisenstein form; and (2k+3)² = 4N(k) − 27 |
| P095, P092 | targeted proof check | confirmed: independence by private conductor primes, 3^m ≥ √P from C > 1/log 3, and log Q = O(log P log log P) |
| P056-P058, programs | done at cp04 | P058 is superseded by P074 |

## 3. Review of the paper against "What a paper has to be"
| item | present? | right? |
|---|---|---|
| 1. Title: "Deterministic finite-field algorithms after Alpöge, Cilleruelo, Lenstra, Montgomery, and Tang" | yes | **No.** It names five people and not the question as the field knows it, which algorithms that assumed GRH Dirichlet GRH now proves. "After" should mark only the person whose idea is carried out; Montgomery and Cilleruelo supply tools |
| 2. Abstract's first sentence names the work it answers | yes (Alpöge, Tang) | partly. It is dense with symbols. It says Tang gives polynomial-time factorization without saying that this rests on two 2026 preprints (OpenAI; Cureton-Thorner, which needed a repaired lemma). The last sentence on who produced and checked it, and that no human has, is present and right |
| 3. The theorem in words | the theorems are stated in full with hypotheses | **missing** for each theorem: what it means and which famous statement it bears on. Only the table does this |
| 4. Why anyone should care | the table, and a one-line opening | **thin.** There is no plain paragraph on what changes now (for instance Miller's test, nonresidues and primitive roots made unconditional by A; what still needs Hecke RH) |
| 5. Credit split exactly | theorem-adjacent paragraphs with statements and pages | **mostly right.** But Cureton-Thorner's quasi-RH for all Dedekind zeta functions is called "the uniform Dedekind zero-free theorem" and, in the final section, "the separate unconditional zero-free theorem". That presents a 2026 preprint claim as established. Its status has to be stated where it is used |
| 6. Context, each work opened and cited | a classical table with 18 rows; the OpenAI, Tang and Cureton-Thorner comparisons; LITERATURE.md shows the sources opened | yes |
| 7. Scope | each average theorem states its exceptional set and that it is not an all-input construction; the final section is exact | **yes, good** |
| 8. Why the proof works | one paragraph, on the Kummer identity only | **incomplete.** The mechanism of the main new results, the averages (character orthogonality over the input prime; the conductor budget against r^m ≥ √P; private large primes of k² + 3k + 9), is not explained before the proofs |

**Other points:**
- **Every new result proved in full:** yes for P056-P058, P074 and P092-P095, which I read. The rest was not read.
- **Banned content:**
  - none of "actual", "supplied", "retained", run names, internal ids, checkpoints, intakes, agents, prompts or paths
    occurs in the .tex;
  - "Claude" occurs twice, in the abstract and the closing note, as it should;
  - the 16 matches for "C:" are mathematics (set-builder notation).
- **Closing note:**
  - it is present: GPT-6 Astra (ChatGPT Pro mode); same-model statement-alone re-proofs, "configured effort not
    exposed"; Claude Opus 5.5 at effort high; no human; CC0; workbench link;
  - "earlier project records" is close to the line on process words;
  - it should name the new checks: P074 and P092-P095 on 23 Nov.
- **LITERATURE.md:** a real search, dated:
  - arXiv, ECCC, DOI pages, author pages and Hexagon, in general terms;
  - primary sources opened with pages (Montgomery-Vaughan p. 432, Cilleruelo 2011, LLS2015, Thorner-Zaman, Cohen-Pazuki
    and others);
  - credit corrected when found (Murty via Zaman; Cilleruelo, after the independent derivation).
- **Blind re-proofs** (CHECK_EVENTS: 220 events, 51 of them independent re-proofs):
  - there are re-proofs for the pure-field gate (P001), the Teichmüller equivalence (P004), the 12r table (P068) and
    its corollary (P069), and the averages (P074, P092);
  - **there are none** for the extension nonresidue theorem (P006), the quasipolynomial family (P008) and the Tang
    interfaces (P009).
- **Build:** 98 pages, 2 passes, no overfull boxes, no undefined references (the run's report). The PDF page count is
  confirmed, and page 1 renders cleanly. The run marks its full-page visual inspection and newcomer reading as pending.
- **Structure:** about 60 of the 98 statements are restrictions on particular routes. Kept in full, they bury the
  results; they belong in a later, titled part.

**Verdict: postable after fixes, not yet.** Fixes:
1. Retitle around the question.
2. Rewrite the abstract: what is proved, what is granted, why it matters; the status of Tang's two inputs.
3. State Cureton-Thorner as a 2026 preprint theorem with a repaired lemma, wherever it is used.
4. Gloss each main theorem in words, and add a paragraph on why it matters.
5. Explain the mechanism of the average theorems.
6. Move the route restrictions into a titled later part, or split the paper.
7. Blind re-proofs for P006, P008 and P009.
8. Name the 23 Nov checks in the closing note.
9. Reword the Masullo heading and line 9 of the workbench note.
10. Finish the full-page visual inspection and the two readings.

These are sent to the chat in the follow-up below, which waits for the user.

## 4. Follow-up drafted, not sent
`<local>/Documents\TO_SEND\PRO\1_Archive_research_by_topic\67b_GRH_ALGORITHMS_FOLLOWUP_1_paper\PROMPT.md`. It
passes `push_rule_pro_prompts.py --lint-math` (0 failing). It carries the ten fixes, the push, three-hour, check-event,
checkpoint and source paragraphs on the model of 49b, and the Masullo rule.

## 5. Outreach and Hexagon (drafts only, none written)
- **P074 and P092: candidates after the fixes.** Remaining gates:
  - a literature search on almost-all auxiliary primes and on irreducible cubics found by short search;
  - the comparison with Cilleruelo and Montgomery-Vaughan, which the run has begun;
  - a blind re-proof in the final version.
- **Outreach:** none new.

## 6. Files of others
The return holds none.

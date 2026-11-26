# Literature searches and source roles

Search/read date: 25 November 2026. The attached frozen formal statements and
proof versions are authoritative for the mathematical source audit even where
an online page changes. No priority claim is made. Absence from these searches
is not evidence that a theorem has no earlier appearance.

## 1. Before extending the theta proof

General queries included quadratic Boolean functions, monotone circuit
complexity, graph edge functions, vertex cover, charged negations, theta
graphs, and hazard derivatives. Searches covered arXiv, author pages,
journal records, ECCC and Hexagon. The source-guided proof work started from
the three frozen Lean arguments designated in the prompt; it did not infer
an unrestricted theorem from an AND/OR-only title or a table for another graph.

The essential previous results are:

- **fengqiaoqu**, public contribution761, checked23November2026: exact
  AND/OR theta size. Frozen L_meta_615.lean, especially `theta_min_cover_half`,
  `theta_internal_strict`, `tight_branch_cover`, `consumptions_le_two`,
  `tight_neighbor_slots`, `total_slots_impossible`, and `theta_exact`.
  The parameters count interior vertices. This is the known positive theorem
  re-proved and credited in the paper, including its carrier and slot methods.
  https://github.com/brilliant-hq/pequalnp-proofs/pull/761
- **jiaxun530**, public contribution3848,24November2026, commit
  f5238c8b9a5fe0bb379403d109cc933ea1e8302b: fifteen-gate all-gate lower
  bound for the ten-input theta with path lengths3,4,4. Frozen
  L_meta_1549.lean supplies first-branch independent groups, one-bit
  factorization, residual twins and incidence counting. The present general
  graph lemma replaces the finite residual-class enumeration by a direct
  cover construction. Attribution was checked against the public commit/PR
  metadata; file assembly by another model is not authorship or review.
  https://github.com/brilliant-hq/pequalnp-proofs/pull/3848
- The frozen L_meta_722 argument uses a concrete finite frontier table and
  kernel decision checks. Its table is not transplanted to the twelve-input
  graph. The frozen L_meta_657 proof imports L532 outside the allowed formal
  import root and uses a sensitivity pattern that fails on the target when
  both adjacent hubs are true. These are source audits, not new compilations.

## 2. Classical quadratic-function context

Opened the journal/DOI record and author-hosted version of Stasys Jukna,
*Disproving the Single Level Conjecture*, SIAM Journal on Computing36(1)
(2006),83–98, DOI10.1137/S0097539705447001.

https://web.vu.lt/mif/s.jukna/ftp/single1.pdf

Theorem2.1 on author-PDF p4 proves that some quadratic functions have linear
monotone circuits but require nearly quadratic single-level circuits.
Section1, pp1–3, defines the graph-function correspondence and explains the
historical conjecture. It is contextual only: no assertion that all quadratic
functions have optimal cover-star circuits is imported. The final paper uses
this precise statement, not an inference about the charged theta optimum.

Search also found Alon–Boppana and Amano–Maruoka sources on monotone circuit
complexity. They remain leads; no theorem from them is used without inspection.

## 3. Hazard literature and forward references

The attached arXiv1711.01904v2 source of Ikenmeyer, Komarath, Lenzen,
Lysikov, Mokhov and Sreenivasaiah, *On the Complexity of Hazard-Free Circuits*,
was inspected at Section4, Corollary4.7 and the proof of Theorem4.11.
The article appeared in JACM66(4), Article25 (2019), DOI10.1145/3320123.
It supplies the fixed-baseline derivative construction used in the separate
hazard audit. Hazard-free complexity is not unrestricted circuit complexity.

https://arxiv.org/abs/1711.01904v2

Following later work, opened:

- Jukna, *Notes on Hazard-Free Circuits*, ECCC TR20-102, revision2,
 22December2020. Theorem1, pp6–7, and discussion pp8–9 give a syntactic
 monotone transformation under absence of zero-hazards and explain the
 monotone/hazard-free comparison. This is context, not a lower bound for
 arbitrary circuits with hazards.
 https://eccc.weizmann.ac.il/report/2020/102/revision/2/download/
- Ikenmeyer, Komarath and Saurabh, *Karchmer–Wigderson Games for Hazard-free
 Computation*, ECCC TR21-100, revision1,25November2022. Theorem4.6 and
 its Section7 proof concern hazard-free formula size/depth and the associated
 communication game. These formula results are not treated as DAG-size bounds.
 https://eccc.weizmann.ac.il/report/2021/100/revision/1/download/

## 4. Follow-up exact-result and AI-method searches

After the first checkpoint, searched `"theta graph" "circuit" "negation"`
and `site:hexagonmath.org "circuit" "theta"`. Retrieved signed-graph matroid
and primitive-word circuit material was unrelated to the Boolean gate
question; no exact prior all-gate answer was identified by these searches.
The already-known monotone result continues to be credited rather than
presented as new. The added C9 proof is an implication of the same checked
carrier method; no priority is claimed for it or the general three-root form.

The query `site:openai.com mathematics "First Proof" research` found and opened
OpenAI, *Our First Proof submissions*,20February2026:
https://openai.com/index/first-proof-submissions/
The report distinguishes model-written proof attempts, human feedback and
revised correctness assessments. It is cited as recent methodological context
for verification, with no mathematical circuit theorem imported from it.

## 5. Version and format records

The initial web open of the public FORMAT.md failed. A subsequent direct
fetch succeeded and the complete format1 document was read. Its exact hash
and address appear in SOURCES.tsv. The editor assigns the permanent WB number
and repository commit; no number or commit was manufactured locally.

Every downloaded source used above has its exact byte SHA-256 and locator in
SOURCES.tsv. The downloaded PDFs and HTML are excluded from every return ZIP.
The attached sources are cited by their frozen hashes and are also excluded.
The checks of new proofs and the chronology of independent/source-guided
re-proofs are recorded separately in CHECK_EVENTS.tsv and research/.

## 6. Final exact-family search check

On25November2026 the final targeted queries were
`"Boolean circuit" "odd cycle" "leaves"`,
`"circuit complexity" "theta" "vertex cover"`,
`site:arxiv.org "quadratic Boolean" "negation"`, and
`site:hexagonmath.org "cycle" "pendant" "circuit"`.
The returned results included quantum and symmetric algebraic circuit work,
Jukna's graph-complexity chapter, and an unrelated Hexagon index. None of
the retrieved snippets identified an exact charged Boolean gate theorem for
the three-root odd-cycle family. No additional mathematical premise was
adopted from this final search. This limited search makes no completeness
or priority claim; the inspected and used sources are the ones above.

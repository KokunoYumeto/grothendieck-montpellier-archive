# A.2 / A.4 source and computation log

Run: GPT-6 Astra (OpenAI), inherited effort setting, agent /root/a2_a4, 2026-11-19.

## Source retrieval and opened locators

- Dold–Puppe, *Homologie nicht-additiver Funktoren. Anwendungen*, AIF 11 (1961), pp. 201–312. Official Numdam bibliographic page opened; direct Numdam PDF request timed out; the Edinburgh mirror of the same Numdam PDF opened and downloaded. Read §3, pp. 218–225, especially equation (3.3), Theorem 3.6, Corollary 3.8, and normalized decomposition equations (3.19)–(3.21). PDF local path: `sources/dold_puppe_1961.pdf`.
- Bühler, *Exact Categories*, arXiv:0811.1480. arXiv HTML route unavailable; PDF opened. LaTeX source fetched from `https://arxiv.org/src/0811.1480`, unpacked into `sources/buehler_0811.1480/`. Read Proposition 7.6 (cancellation), Theorem 13.7 / Example 13.8 (Happel and complexes), Theorem A.1 (exact abelian embedding). Source-text locators in `exact.tex`: weak completeness/cancellation at lines 2161ff; Frobenius at 4407ff; embedding at 4642ff.
- Stacks Project, Tag 066Z, Lemma 15.76.14, complete statement and proof opened. Explicitly checked that the result applies to regular noetherian rings of arbitrary Krull dimension; the opened source documents removal of the earlier finite-dimension hypothesis in 2022.
- Stacks Project, Tag 0G99, Lemma 15.79.2, statement and proof opened; uniform Tor-amplitude recognition by derived residue-field fibers.
- Happel's book itself has not been opened by this agent. Bühler Theorem 13.7 identifies the exact original locator (Chapter I, Theorem 2.6, p. 16). We use and cite Bühler's opened exposition; no statement is attributed to an unopened book as though it were read.

Web source refs for root to reopen before citing in chat: `turn937457598view0` (Dold–Puppe PDF); `turn842623129view0` (Bühler PDF); `turn484887277view1` (Stacks066Z); `turn842623129view1` (Stacks0G99). Exact URLs are in the bibliography. The proof file uses ordinary bibliography citations, not internal web IDs.

## Literature searches

Queries included: “Buhler Exact Categories Theorem 7.1 embedding abelian category bounded complexes Frobenius”; “Stacks Project regular Noetherian ring finite module finite projective dimension perfect complex residue fields”; “site.stacks.math.columbia.edu pseudo coherent complex residue field tor amplitude finite perfect”; “Dold Puppe Homologie nicht-additiver Funktoren 1961 numdam”; “Theo Bühler Exact Categories 0811.1480 pdf”. The first embedding query used a guessed section locator, corrected from the opened source to Theorem A.1. We do not claim priority for the matrix formulation or counterexamples. These searches established the exact sources used; they are not an exhaustive history search.

## Computations

`code/a2_a4_checks.py`, output `logs/a2_a4_checks.json`:

- A2.1: all two possible degree-zero scalars for a chain retraction D_0→F_2[0]; zero retractions.
- A2.3: all four elements of Z/4; kernel of multiplication by 2 is {0,2}; cardinality cannot equal 4^r for a free target object.
- A2.5: all 64 pairs in Z/16×Z/4; 16 satisfy x mod4=2y; order distribution 1,3,4,8 for orders 1,2,4,8 and none of order16; kernel and quotient both order4. This finite pullback extension is excluded by the asserted weak exact structure.
- A4.5: all four elements and all 64 triples of F_2[e]/e²; ring multiplication and the equal kernel/image of multiplication by e verified. The all-degree Tor assertion is proved from repetition, not inferred from a finite truncation.
- A4.4: exact binomial rank formulas checked for n=0,...,16. The general identity is proved by the binomial theorem.
- A4.6: disk rank contribution formula checked for disk lower degree 0,...,7 and chain degree 0,...,9. The general formula is a direct count in the proof.

Recorded arithmetic run time: about 0.0002 seconds (the output contains the exact run value). All finite checks use Python integer arithmetic and exhaustive enumeration, no numerical approximations.

`code/a2_a4_fetch_sources.py`, output `logs/a2_a4_source_downloads.json`: retrieves source bytes and records URL, local path, byte count, and duration. Source retrieval is not a proof check. Earlier one-shot arXiv retrieval succeeded (85,219 bytes) before the reproducible download script was saved; the script therefore reports reuse of that exact file. No attached input was modified.

## Exact attachment corrections and refinements

- `RESEARCH_SA09_study/study/readings/SA09_137-138.md`, lines 195–198, and `study/CHECK_EVENTS.tsv`, line 18: the nonnegative source category is not Frobenius. Full faithfulness remains true, proved via its explicit disk copresentations. Corrected by A2.1, A2.2, A2.6. The manuscript definition is in `MPL_137_045-086_transcription.tex`, lines 153–167 (scan49); the nonnegative stalk sequence is at lines 309–321 (scan52).
- `MPL_137_045-086_transcription.tex`, lines 279–293 (scan51): “kernels of d^i” alone do not describe the ordinary essential image over a nonfield PID. The study's suggested additional kernels are correct under that domain convention. A2.2 gives the all-ring version; A2.3 gives the PID reduction and a fully finite counterexample. `study/CORRECTIONS.tsv`, line13 and `study/CHECK_EVENTS.tsv`, line19 are rechecked in this run.
- `MPL_137_045-086_transcription.tex`, lines 168–204 (scan49), and b) at lines 295–302 (scan51): Sex1–2 are insufficient to make the resolution characterization true for a chosen Sigma. A2.5 gives the finite counterexample, A2.4 the correct Quillen exact theorem. The later abelian qualification at lines 530–533 (scan56) is correct when Sigma is all exact sequences.
- `MPL_137_002-044_transcription.tex`, lines 510–539 (scans14–15), Proposition1(e) and NB: actual boundedness and derived perfection must be distinguished; the NB's claimed necessity is false for the contractible example as well. A4.2–A4.5 give exact corrected statements. `study/readings/SA09_137-138.md`, lines122–132 correctly gives bounded normalization, not derived perfection, as the raw-rank criterion; this has been proved and strengthened to all base rings with finite terms. The phrase “true with a uniform degree bound” in `study/CHECK_EVENTS.tsv`, line10 must not be read as repairing the converse to the original perfection statement.
- `MPL_137_002-044_transcription.tex`, scan17, lines607ff: the degreewise rank formula must include mu_i. A4.6 proves the corrected formula from the block decomposition. `study/CORRECTIONS.tsv`, line8 and `study/CHECK_EVENTS.tsv`, line11 are rechecked mathematically. No independent claim to have inspected the ink is made.
- In that same transcription, lines637–638, the assertion with “(str.)” is true only for strict perfection if it requires finitely many factors of every kind. Over a PID, derived perfection needs finite support only of the stalk and nonunit-block families; the contractible disk multiplicities can have infinite support. A4.6 states and proves this additional correction.

## Ambiguities and their treatment

“Principal ring” is treated as PID for the Smith decomposition, and as arbitrary commutative principal ideal ring by the general finite-matrix criterion. A three-term Z/4 complex with both differentials2 verifies that the PID decomposition itself does not extend. “Sigma-kernel” is treated both as an ordinary kernel and as one whose inclusion is admissible. The extra strong-left-exact conditions are explicit in A2.4, including the weak-idempotent-completeness hypothesis for the shorter test. No undecided `unsure` transcription choice is used to select a mathematical claim.

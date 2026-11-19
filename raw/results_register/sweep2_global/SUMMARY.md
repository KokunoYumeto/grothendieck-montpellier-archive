# SUMMARY.md: sweep 2, how everything interlinks

By Claude Opus 5.5 at effort max (agent a0c4bb37), 18 Nov 2026, from 13:27 UTC; finished 14:2x UTC. The harness
refused the agent's own write of this file, so the main session (Claude Opus 5.5 Max) saved it from the agent's final
message, unchanged.

The sweep ran without sub-agents. The agent guard refused all five launches: inside a sub-agent it reads the main
session's transcript, so the brief's "Sub-agents allowed: 5" was never read. The set-up comparison is therefore one
900k agent against the four 400k agents of sweep 1.

The runs are by GPT-6 Astra (ChatGPT Pro mode). Nothing outside `sweep2_global/` was written.

## 1. Counts

- **`GRAPH_EDGES.tsv`: 30,323 edges** (sweep 0 had 13,793).

  | Kind | Edges |
  |---|---|
  | uses | 16,925 |
  | answers prompt item | 7,520 |
  | cites his place | 2,651 |
  | names | 1,289 |
  | cites literature | 1,124 |
  | uses computation | 534 |
  | restates | 139 |
  | checks | 126 |
  | strengthens | 6 |
  | refines | 5 |
  | corrects | 4 |

  - 3,159 edges run between runs (sweep 0 had 94). What made the difference: run aliases, escaped underscores, ranges,
    sub-items, and references through prompt rows (`tools/prompt_rows.json`).
- **`UNRESOLVED.tsv`: 7,514 fragments.**

  | Kind | Fragments |
  |---|---|
  | describe a proof step and name no item | 4,991 |
  | name a standard result without a locator | 1,486 |
  | name literature without a locator | 1,005 |
  | ids not found in their run | 25 |
  | cross-run ids not found | 7 |

- **`FLAG225_RESOLUTION.tsv`: sweep 0's 225 no-id flags, 421 tokens.**

  | Token | Count |
  |---|---|
  | another run's id | 113 |
  | literature locators | 107 |
  | parts of the run's own rows | 88 |
  | computations | 3 |
  | named without an item or a locator | 103 |
  | not matched | 7 |

- **`CLUSTERS.tsv`: 21 clusters, 117 member rows.** They cross runs, sweep-1 scopes or lines; each has a canonical
  statement and a status.
- **`CROSS_LINE.md`: 11 links that matter.** 722 edges cross the sweep-1 scopes and 34 cross the lines; none touches
  S6.
- **`CONSISTENCY.md`:**
  - no contradiction between runs or lines;
  - the 20 cross-run uses of unproved rows are all sound;
  - three gates;
  - nine clusters with two statuses.
- **`CYCLES.tsv`: 59 cycles, all within single runs.** Four earlier ones were the agent's own parse errors.
  - 30 come from summary rows.
  - 29 are mutual citations among proved rows. The agent read 10 at statement level and found none circular; 4 are
    marked to read in the TeX.
- **`HIS_PLACES.tsv`: 3,034 links from 2,392 rows.**
  - By work: Montpellier archive 1,389, La Longue Marche 855, Les Dérivateurs 790.
  - 1,304 lines carry his first words, from the transcription inventories.
  - Cote 149, scans 35, 36 and 56 carry a sentence of the agent's own reading.
- **`PLACES_INDEX.tsv`: 1,434 places**, each with every tag that points to it.
- **`FINMON_PLACEMENT.tsv` (695 rows) and `FINMON_MERGES.tsv` (11 links).** FINMON is the run the register misses.
- **`CORRECTIONS.md`: 19 items:** 11 on the mathematics, 8 on the register and its tools.
- **`CHECK_EVENTS.tsv`: 10 events on 10 statements:** 8 targeted proof checks, 2 count comparisons.
- **Also:** `PROGRESS.md` (the working log); `tools/` (rerun with `resolve.py`, then `relabel.py`).

## 2. The most important links and corrections

1. **Δ on GT̂ (SC01).** Δ|GT̂ = 0 and GT̂ ⊊ ker Δ ⊊ GT̂₀ are proved by two routes. Every run uses the same
   character, that of LM7_PUSH E.65, which settles what sweep1_sections left open.
   - **Route 1:** EXIT_TOWER E.44 → E.49 → GT_TOWER_CHECK A.1, A.3, A.7. Its gate is 𝒥(A) = A, through
     Boggi–Zalesskii's Theorem A.
     - The agent read E.44's whole proof and checked its genus-zero algebra and geometry: the centralizer, the
       topology, the rational identities and the cusp-swap step.
     - What remains: the exact statement of Boggi–Zalesskii 2024 Theorem A (i), (iii) at p = 2, and EXIT_TOWER E.28.
   - **Route 2:** SECTION_GHOSTS E.176–E.191 (final return), which does not use Boggi–Zalesskii.
     - Its gate, E.179–E.181, claims that every normalized element of GT̂ satisfies relation (IV) of
       Nakamura–Schneps 2000, and so lies in the group Λ of Hatcher–Lochak–Schneps 2000. Those papers left that open.
     - It needs a field check against Lochak–Nakamura–Schneps 2026 (arXiv 2602.12462) and a referee from another
       model family.
     - E.181's normalization step was checked: it is correct.
2. **The p-adic local section theorem is one gate under 73 rows, 66 of them Proved (SC03).**
   - Its source is OpenAI's preprint of 6 Oct 2026, which our prompts call unrefereed; LM8_PUSH D.54/D.56 re-derive
     it.
   - The two sweep-1 agents give "the section set of U_n/Q is the three cusp packets" opposite statuses. It is
     proved relative to D.56, so it should read Conditional.
3. **No run refutes another run's Proved row.** Every cross-run "refutation" hits a prompt's paraphrase, a lead or
   a converse:
   - R27 lost "closed-point-preserving";
   - R8 generalized specific noncuspidal sections;
   - R18 dropped "commuting".

   The 45 refutes/corrects edges made by the keyword rule (33 and 12) were relabelled after reading them.
4. **Open rows settled by other runs:**
   - CATHOT E.17 is true for U-small filtered indexes (INDLOCAL B.1); sweep1_derivateurs had handed this question on;
   - CATHOT G.17: the minimum for the RP² poset is 49, and K(Z,2) has no finite model (FINMON C3, E1);
   - CATHOT D.6 fails, by S2COUNT A.M1 and, independently, by FINMON E4;
   - LM7_PUSH E.3 and DELTA_ON_GT A.84 are decided by item 1.
5. **The Fermat theorem (SC02).**
   - LM8_PUSH D.22 and FERMAT_SUCCESSOR A.4 found the same false step independently: v₂(q) = −8 at the unit cusp
     (the leading term was checked).
   - LM8_PUSH D.23 and FERMAT_SUCCESSOR A.11 repaired the theorem independently.
   - SECTION_GHOSTS E.100 adds that for even n there is no section at all.
6. **The bridges between the lines:**
   - the exit categories of M̄_{g,n} are proper, smooth only at (0,3), with BZ lifting categories, so RESIDUE H.3/H.5
     is the same theorem as EXIT_TOWER C.2;
   - LM5's glued topoi rest on STRATA;
   - one counterexample, the finitary shift, blocks finite tests in both lines (PATHS E.13 and LM5 A.20).
7. **The register:**
   - FINMON is missing;
   - PRETOT and TOTEX are filed on the wrong line;
   - the lineage parse misses aliases, escaped underscores, ranges and prompt rows;
   - "Refuted" mixes "the claim is false" with "we prove it false";
   - summary rows make half the cycles;
   - "Conditional" is dropped;
   - 379 referee outcomes recorded in the prompts are missing from the check ledger.

None of these findings is Michel Hua's project's.

## 3. Sub-agents and budget

- **Planned:** five sub-agents, each Claude Opus 5.5 at effort max with about 200k:

  | Sub-agent | Task |
  |---|---|
  | delta | Δ across all runs |
  | bridge | the links between the tower and sections scopes |
  | homotopy | FINMON and the links between the lines |
  | places | HIS_PLACES |
  | cycles | the cycles |

  The briefs and inputs (about 25k tokens) are in `COMMON_BRIEF_FOR_SUBAGENTS.md` and the `sub_*` folders.
- **What happened:** `agent_guard.py` refused all five launches ("allows 0, launched 455"), so the sweep ran as one
  agent.
- **Budget:** about 715k of context.

  | Part | Tokens |
  |---|---|
  | scripts that close the graph, and their outputs | about 150k |
  | reading: the sweep-1 summaries, the rows of every cluster, the proofs of SECTION_GHOSTS E.181, EXIT_TOWER E.44 and INDLOCAL B.1, the first page of LM8_PUSH D.56 | about 300k |
  | writing | about 100k |

- **What was lost without sub-agents:**
  - most places carry his first words rather than a sentence;
  - 19 of the 29 mutual cycles were not read;
  - the Δ gates are located and partly checked, but not refereed.
- **What the agent would do differently:**
  1. test one sub-agent launch before writing five briefs;
  2. have the main session launch the sub-agents, or fix the guard so it reads the sub-agent's own transcript;
  3. hand out the mechanical tasks first (places, cycles), which need no global context. The global questions (Δ,
     the bridges) needed the whole graph, so it would keep those itself.

The sweep-1 agents went deep inside their scopes. Every main result of this sweep (items 1–4) lies between scopes.

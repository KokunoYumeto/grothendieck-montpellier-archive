# The conference results carried into the prompts (25 November 2026)

By the conference convener ae84c4aa572daf430 (Claude Fable 5.2 at effort max), on the brief of the main session
329fb1e6 (Claude Opus 5.5 at effort max): `agent_notes/ae84c4aa_CONFERENCE_TO_PROMPTS_BRIEF_20261125.md`. Nothing was
sent or posted; no other session was contacted. `TP` is `<local>/Documents/TO_SEND/PRO`. Every backup is in
`TP/_backups_20261125/<prompt>/before_conference_pass_20261125/` unless a path is given.

## 1. Summary

| What | Count | Which |
|---|---|---|
| Waiting prompts changed | 8 | 95; 05_FINMON; INTAKE_A, INTAKE_B, INTAKE_C; 28_SA30, 30_SA31, 29_SA32 |
| New prompt built and placed | 1 | 100_FERMAT_SECTIONS (proposal 3) |
| Follow-up messages written | 2 | COUNTING_VARIETIES; POLISH_CRISTAUX 92c |
| Note for other sessions | 1 | rows 17 and 22, from run 99's final |
| Left, with reasons | 8 | section 6 |

## 2. Waiting prompts changed

| Prompt (folder under `TP`) | Program row | What was added | Lint |
|---|---|---|---|
| `1_Archive_research_by_topic/95_GT_AFTER_H17` | proposal 4; question 7, 8 | Rebuilt from its spec. A block "Settled on 24 and 25 November 2026": S1, relation (III′) on all of GT̂ (H17 version 2, Theorem 20) and IΓ = GT̂; S2, R1 is its Corollary 22 and the Boggi–Funar gate is closed; S3, the note hexagon:2611.01024 (invertibility automatic, λ a unit from (I) and (II)). Research items 2(a), 2(d) and 5 marked settled; item 2(b) now also asks for the comparison with the actions of Nakamura–Schneps and Lochak–Nakamura–Schneps; item 3 carries proposal 4 (the map onto C₅ × C₇ × C₁₃ × C₂^ℕ with every step; is the quotient abelian; its characters; is Δ in the span; the graded statement). The paper cites S1–S3 without proving them again. Five attachments added (both notes in LaTeX, three checks). 796 files, 5,033 words | `--lint-math` 0 failing; paper completeness 0 failing; builder "lints PASS" |
| `8_Derivateurs_mathematics/05_FINMON_CP2_night` | paper 6 (D2), its gate | Part C.1 now asks the run to prove Theorems 1.1, 2.1, 2.2 and Corollary 2.5 of our converse (R9) from their statements, before opening our proofs, as a referee who wants to find the error, and to record an independent re-proof or a refutation for each. Before, it asked only that the steps be checked. No attachment change | `--lint-math` 0 failing |
| `7_Longue_Marche_intakes/18_…/INTAKE_A_ANABELIAN_SECTIONS` | proposals 7, 8 | A block before "How to work": (III′) holds on GT̂, so the question posed in the prompt is answered; the note 2611.01024 with its Theorems A and E; what it changes for this run. Four texts added to the ZIP (`INTAKE_A_7_settled_20261125/`). The checks of GA-2 and of the K-group obstruction were already there (its Check 1 and N3), so proposals 7 and 8 needed nothing more | `--lint` 0 failing; `--lint-math` fails as before the edit |
| `…/INTAKE_B_TOWERS` | questions 7, 8 | The same block; for this run: strictness GT̂ ⊊ GT̂₀ stays our unrefereed claim; no invertibility to verify for a witness; Lochak's p. 61 sentence is no longer open. Four texts added | as INTAKE_A |
| `…/INTAKE_C_GROUP_ACTIONS` | paper 2 (A1) | The same block; for this run: C.29 and C.30 are in the posted note, which proves more; C.31 keeps its row, and its derivation from the ribbon operad is the step no one has checked; section 7 takes the note's two open points. Four texts added | as INTAKE_A |
| `E_Archive_small_prompts_54/16_small_batch_2_18-34/28_SA30_…part3` | proposal 13 | A dated block before "Rules": the two gates named in the prompt are closed; the note 2611.01024; a lead on cote 147: the exit categories (EXIT_TOWER A.2 = SA10 A4.5; BISITE F.15–F.17), and for Stage 6 the statement to prove or refute, that forgetting a mark is not W_∞-smooth for every n ≥ 4. Two LaTeX files added (`SA30_updates_20261125/ours_published/`) | `--lint` 0 failing; `--lint-math` fails as before |
| `…/30_SA31_…part4` | proposal 13 | The same, with the lead on cote 148. Two LaTeX files added | as 28_SA30 |
| `…/29_SA32_Drivateurs` | proposal 14; papers 4, 6 | A new section before "Rules": the chain filtered ⊊ exact ⊊ total ⊊ quasi-filtered and the failure of ms. 36ter (TOTEX2; independent check passed 25 Nov); the finite-monoid theorem with its check state; FREX A.3(iii) as a question for Stage 6. No attachment change | as 28_SA30 |

The six intake and archive prompts fail `--lint-math` because they have no push paragraph; they failed it before my
edit too (checked on the backups). The earlier pass left that decision to the main session; it still stands.

## 3. The new prompt

**`TP/1_Archive_research_by_topic/100_FERMAT_SECTIONS`** (proposal 3, first in my ranking). Built with
`build_papers.py 100` from `pro_prompt_builds/PAPERS_20261122/specs/100_FERMAT_SECTIONS.md` and `.plan.json`, placed
with `--place 100`. PROMPT.md (3,422 words) and a ZIP of 37 files, 2.1 MB. `--lint-math` 0 failing; paper completeness
0 failing.

- **Why now.** Its gate was the attack-read of LM8_PUSH D.23, and that is done: `CONFERENCE/ATTACK_D23.md` (Claude Opus
  5.5 at effort max, 25 Nov) finds that the global part holds and names two repairs for the paper.
- **What it asks.** The theorem for every odd n ≥ 3 with every step written out, in the form of the attack-read's §1;
  the theorem on all sections from the local theorems; the prosolvable, metabelian and pro-3 forms; Y₁(N); even
  exponents. The paper carries the two repairs and the corrections to Steklov as the attack-read's §8 asks.
- **Attached.** The papers, reports, results and references of LM6, LM8_PUSH (section D), FERMAT_SUCCESSOR and
  LM7_FERMAT_TOWER; the attack-read with its checks; four maps; e-prints of Steklov (2602.17746), Stoll (math/0606465,
  title checked) and Betts–Kumpitsch–Lüdtke (2305.09462).
- **Three things for the main session to look at.**
  1. OpenAI's p-adic section preprint is not attached: I found no local copy. The prompt tells the run to read it at
     its source. If a copy of its LaTeX is on disk, add it to the plan and rebuild.
  2. The `REPO` field is copied from prompt 95 (`k-theory-and-galois-groups-workbench`). Change it if these results
     belong in another workbench.
  3. I wrote "Where it stands" from the attack-read, the Longue Marche proposals file and the maps. I did not read
     LM6, FERMAT_SUCCESSOR or LM7_FERMAT_TOWER myself. The agent that knows them best is the attacker ae4ae3dc; a
     read of the prompt by it before it is sent would be cheap.

## 4. Follow-up messages (files for the user to paste)

Both are in `TP/1_Archive_research_by_topic/SENT/`, beside the prompt folders and not inside them.

| File | For | Content |
|---|---|---|
| `63_COUNTING_VARIETIES_FOLLOWUP_MESSAGE_20261125.md` | the running thread (checkpoint 08 at 01:32 UTC) | The height observation (height of the Artin–Mazur formal group is 1 iff #SAT ≢ 0 mod p), to be checked first; then: what the next coefficient computes, the complexity of height ≥ 3, of each height, of infinite height; what DP_MULT's laws give |
| `92c_POLISH_CRISTAUX_FOLLOWUP_MESSAGE_20261125.md` | the merge thread, if it still answers | The shift law for the inertia-character index with the closure at v = 0; the template for Hasse–Witt monodromy in characteristic 2 and the route of RESEARCH_SA15 to the GL₈ block |

92c's newest return is checkpoint 34 of 24 Nov 21:41 UTC. By the user's rule it has probably ended; the file says to
use the same text as research items of the finishing prompt of 92 in that case.

The prompt lint, run on these two files, finds no banned wording. It reports the paragraphs a full prompt must have
(check events, no source copies) as missing, which is right for a message into a thread that already has them.

## 5. Rows 17 and 22

`CONFERENCE/FOR_PEQUALNP_AND_99_SUCCESSOR_20261125.md`, written after reading run 99's final (checkpoint 03).

- **Row 17.** The two runs no longer disagree: run 99's final proves "nonflat ⇒ strict shortening" under the
  price-space theorem (Q3b), as run 98's SH-08 does. The square itself is still open, and so is "contraction ⇒
  shortening". My verdict on a note stays: short, by the pequalnp session, after a check by a different model and a
  search of the last days' posts.
- **Row 22.** Three candidate main questions for a successor, in order: the square in characteristic 2 (proposal 21);
  contraction ⇒ shortening; a finite certificate over C, which needs an asymptotic family (r ≥ 47 in the
  sums-of-squares form). Proposal 21's "give it SH-08" is now "give it both proofs and have them compared".

## 6. Left, with reasons

| Row | What | Why it is left |
|---|---|---|
| proposals 9, 10 | 75's successor: Ihara's question on single even components from K_{4m}(Z) = 0 (m ≤ 30), and the once-punctured CM curve | Deserved, and its gate is met: NIGHT_AFTER_ALPOGE's newest return is checkpoint 13 of 23 Nov, so that is its final. Not built by me: my context was at 93 % after the work above, and its "Where it stands" needs the Ihara note (hexagon:2611.00939v2) and the K-group papers read at the statements. The number-theory mapper (Claude Opus 5.5 at effort max) wrote the link (L22) and is the one to build it |
| proposal 6 | RECONSTRUCTION_BEYOND_SUBPADIC | Waits for INTAKE_A's verdicts on what Carlson–Stix prove |
| proposals 15, 16 | Small prompts for cote 57:97-100 (points) and cote 100:3 2) (finite normalization) | Deserved as small prompts. Not built: they are object prompts with scans and transcriptions, built by the archive tools, which I did not open at this context level. The questions are stated in `PROMPT_UPDATES/F_Archive_working_through_200_and_E_small_24-37_UPDATE.md`, "New-prompt proposals" 1 and 2 |
| proposal 19 | Cote 133 over orders, in NGQ Part B | No Part B prompt exists; whether to build one is the user's open decision (`PENDING.md` 2.7) |
| proposal 12 | The nerve of admissible PD theories | No C.3 prompt waits |
| proposals 11, 17 | Pushouts of profinite topoi; the C.3 table of cote 14 | Not now, as in the program |
| questions 2, 4 | 70d and 68 | Both were sent and are running (HODGE_EFFECTIVE and CONNES_AFTER_RH at checkpoint 03); nothing waits in `TP` |
| — | 96_FLEET_HARD_LINKS, 94_THETA_CIRCUIT_SIZE | Not touched. The conference adds nothing to 96 beyond its update of 24 Nov; 94 is Codex's |

## 7. Backups made

- `95_GT_AFTER_H17/before_conference_pass_20261125/`: `spec/` (spec and plan before) and `send_folder_moved/` (the
  placed PROMPT.md and ZIP before).
- `05_FINMON_CP2_night/PROMPT_before_conference_pass_20261125.md`.
- `INTAKE_A_ANABELIAN_SECTIONS/`, `INTAKE_B_TOWERS/`, `INTAKE_C_GROUP_ACTIONS/`: `before_conference_pass_20261125/`
  with PROMPT.md and the ZIP.
- `28_SA30_…part3/`, `30_SA31_…part4/`: the same; `29_SA32_Drivateurs/`: PROMPT.md only (its ZIP is unchanged).

Every send folder I touched holds PROMPT.md and one ZIP, nothing else; no ZIP has a ZIP inside; `testzip` is clean on
the five ZIPs I added files to.

## 8. What I relayed without reading

The statements I put into 29_SA32 (TOTEX2, the finite monoids, FREX A.3(iii)) and into the two messages are from
`INDEX.md` and the maps, which I read in full on 25 Nov; I did not read those runs. The prompts say "statement level;
check against the page first" where that applies.

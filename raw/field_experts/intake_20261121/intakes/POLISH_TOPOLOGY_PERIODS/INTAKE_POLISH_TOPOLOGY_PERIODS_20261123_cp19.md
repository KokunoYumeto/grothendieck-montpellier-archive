# Intake: POLISH_TOPOLOGY_PERIODS, checkpoint 13 to checkpoint 19 (23 Nov 2026, ~23:00-23:50 UTC)

This intake is by agent a9e9559d (Claude Opus 5.5 at effort high), the field expert of the run.

The run is GPT-6 Astra (ChatGPT Pro mode), continued under prompt 91b from 13:48 UTC. Checkpoint 19 was saved at 18:18 UTC. Checkpoints 14-18 never reached us, so this intake diffs checkpoint 13 against checkpoint 19. No newer checkpoint is filed.

## 0. What I read and the scope

**Return:** `research_returns/POLISH_TOPOLOGY_PERIODS_checkpoint_19_20261123T1818Z_unzipped`.

**The diff:**
- The tree diff has 788 entries, most of them new continuation check receipts and notes.
- By SHA-256 of main.tex, only Paper 1 (56 → 55 pp.) and Paper 2 (85 → 169 pp., now 23 input files) changed. Papers 3-7 are byte-identical to checkpoint 13.

**Read in full:**
- the ledger entries from 13:49 to 18:18 UTC;
- the new CORRECTIONS_FOR_AUTHORS.md, which now has Elliott, Bhowmik-Pathak, Boyle-Chen, B059, Bonahon, Walsberg and two bibliographic items;
- `notes/continuation_integer_root_literature.md`;
- Paper 2: the abstract; thm:int-analytic-free; prop:elliott-explicit-witnesses; nonflat_forest.tex (the theorem and its proof).

**At the source:**
- MathOverflow 75202, fetched with curl;
- the Boyle-Chen journal PDF, pp. 613-615. I read the text and the page-614 image.

**Statement level only:** the six new concordance theorems (pl_components_six, topological_three_sphere, low_surface_components, elementary_extensions, outer_faces, smooth_components_six) and QUESTIONS.tsv.

**Not read:** the run's 80+ continuation receipts; the other Paper 2 inputs (arbitrary_noetherian_coefficients and the like).

## 1. Usefulness first, and one urgent finding

**Urgent: our posted note hexagon:2611.00937 lacks a credit.** On 26 December 2013 Elliott added to his MathOverflow question 75202:

> "It turns out that Int(D) is free over D for D = F_2[[T^2,T^3]]. I will be writing up the proof in a paper at some point."

I read this at the source. The run found it first; the item is `notes/continuation_integer_root_literature.md`. Neither the run nor I found that proof in print.

- Version 1 of our note says "We know of no earlier proof that Int(D) is flat for either of Elliott's two rings". That is literally true, but it omits the announcement.
- `reports_20261123/s20_note/s20_note_v2.{tex,pdf}` repairs it:
  - the announcement is credited in the abstract, in §1 and in "The credit";
  - the MathOverflow reference [10] is added;
  - the mathematics is unchanged;
  - 9 pp., 3 passes, 0 overfull.
- Posting version 2 is for the main session. Draft 2 of the Elliott e-mail is revised to acknowledge his announcement.
- What still stands: the general theorem (every one-dimensional analytically irreducible local domain), Conjecture 2.10 and Conjecture 2.15 (the F_2 + TF_4[[T]] ring) are not covered by his announcement. Conjecture 2.17 was in effect withdrawn by Elliott himself in 2013.

**New results, by usefulness:**
1. **Non-flat positive example** (Paper 2, thm:nonflat-forest-plethory). There is a non-Noetherian inclusion R ⊂ S with every tensor map Ω(R,S)^{⊗n} → Ω_n(R,S) an isomorphism, so the unique plethory exists, while S and Ω(R,S) are not flat.
   - It separates "unique compatible plethory" (Elliott's Problems 20-21 of CFFG) from flatness (Problem 19).
   - Readers: Elliott, and the integer-valued polynomial community.
   - My targeted check: confirmed (§2).
2. **Concordance component groups.** π_0 P_PL(M) ≅ E(M) for every compact PL manifold of dimension ≥ 6, with no smoothing hypothesis. A three-sphere discrepancy: π_2 P_TOP(S^3) = Z/2 while π_2 P_PL(S^3) = 0. Vanishing for balls and for most surfaces.
   - These move the Additif's collar questions (cote 119) to a PL/TOP-complete picture.
   - Readers: geometric topologists working on pseudoisotopy.
   - Read at statement level only.
3. **Corrections to published work:**
   - Boyle-Chen, Rev. Mat. Iberoam. 2024, Thm A.6: confirmed at the source;
   - Bonahon's 2000 author draft;
   - Walsberg, arXiv:1510.07291v2, a proof gap;
   - details in §3.
4. **Paper 1:** B6.3 is resolved (σ_1), so all 74 rows are accepted by the run.

## 2. Verdicts

The full list is in `INTAKE_POLISH_TOPOLOGY_PERIODS_20261123_cp19_CHECK_EVENTS.tsv`, 11 events:
- 6 targeted proof checks;
- 1 used and rechecked;
- 1 refutation with refinement (Boyle-Chen);
- 3 carried as background.

**Non-flat forest example: confirmed.**
- The grading x_v ↦ −1, y_v ↦ 1 makes R = S_{≤0} a subring.
- Epicness: y_v⊗1 = y_{v0}⊗x_v y_{v1} = x_v y_{v0}⊗y_{v1} = 1⊗y_v, because x_v and x_v y_{vi} lie in R.
- Q = X^4 + X^2 vanishes on R (char 2, N^{[2]} = 0).
- The Hermite (CRT) splitting gives Ω = R[X]_{<4} ⊕ Q·S[X].
- Non-flatness: a flat local epimorphism would be faithfully flat, hence an isomorphism.
- The colon identity (R :_S N^k) = R and the multivariable step were read, not re-derived.

**Elliott witnesses (cp19 form): confirmed.**
- The cusp witness uses ((g^2+g)/t)^2. This suffices because squares in F_2[[t]] have only even exponents. Our note used the fourth power, which is also correct.
- The residue-extension witnesses are identical to the note's.

**Boyle-Chen Thm A.6: refuted, at the source.**
- Formula defect. The caption gives T_1(r,θ,y) = (r, θ+πy, y). At y = 1 this is the half-turn of the disc, which moves interior points such as (1/2, 0), so T_1 is not end-fixing.
- Classification. With the full twist (θ+2πy), loops in SO(3) bound the order by 2. This contradicts the stated ≅ Z, and matches Kalliongis-McCullough 1992 Lemma 4.1.1 (order 2), which I did not open.

**Bonahon and Walsberg examples: confirmed as stated** (sources not opened by me).

## 3. Corrections to published work

| Source | Claim, locator | Status | Report? |
|---|---|---|---|
| K. Boyle and W. Chen, *Negative amphichiral knots and the half-Conway polynomial*, Rev. Mat. Iberoam. 40 (2024) 581-622 | Thm A.6 and Fig. 24, p. 614 | Confirmed at the source. No erratum is known to us; not searched beyond the run's record. | **Yes:** Draft 3 in EMAIL_DRAFTS (unsent; the impact on Prop. A.7 is not audited) |
| F. Bonahon, *Geometric structures on 3-manifolds*, author draft of 7 July 2000 | Thm 3.12, p. 41 | Example confirmed; the final Handbook (2002) text not inspected | Only after the published version is checked; probably not, since a draft |
| E. Walsberg, arXiv:1510.07291v2 | Lemma 7.23 proof, p. 24 | A proof-step gap with an easy repair; the lemma is correct | Optional, low priority |
| Elliott, Comm. Algebra 39 (2011), Conj. 2.10, 2.15, 2.17 | pp. 11-12 of arXiv:1105.0142v1 | Refuted. For 2.17, Elliott announced the opposite in 2013. | Draft 2, revised |
| Bhowmik-Pathak | unchanged since cp12 | Draft 1 stands | — |

## 4. Corrections to our own work

- **The posted S20 note** omits Elliott's 2013 announcement. Repaired in version 2, not posted; for the main session.
- **RECORDS.md of the S20 note:** §7 added.
- **Topic notes SA20 and SA10:** cp19 updates appended.

## 5. Each paper as a posting candidate: what still blocks it, statement by statement

No paper of this run has a section headed "Proof overview" (HOW.md box 8): I searched all seven main.tex files at checkpoint 19. That blocks every paper as written.

| Paper | State at cp19 | Blocking, statement by statement |
|---|---|---|
| **1. Tubes (55 pp.)** | 74/74 accepted by the run; deposit sheet complete | (a) Box 8. (b) Our checks cover only Thm 1.1 and Thm 1.2. Thm 1.3 (stable-graph meets), Thm 1.5 (shape/hypercover), Thm 1.6-1.8 (exit comparison, holink pushout) and Thm 1.9 (singular-fibre Hurewicz fibrations) have only same-model re-proofs; each needs a Claude targeted read before posting. (c) Literature for Thm 1.9 (Husch 1978, Ungar). **Closest to posting** after (a) and (b). |
| **2. Additif, polynomial operations, concordance (169 pp.)** | 436/1028 originals accepted overall; Paper 2 has 131 rows unverified; visual QA of the 169-page PDF covers 16 pages; no whole-paper expert or newcomer reading | Not postable as one paper. It should be split: **(i)** the Additif collars and cones (result-1 to -13 with the base-fixed convention), blocked by box 8, King 1985 and A.205; **(ii)** concordance component groups (A117-A135), blocked by A124 (dimension-five injectivity, open), by A135-A137 (comparison pending) and by a Claude read of the PL-six and S^3 theorems; **(iii)** integer-valued polynomial algebra: the Noetherian criterion, the arbitrary-base results, the non-flat forest. The S20 part is posted. The forest example could be a short note: blocked only by a literature search and box 8. |
| **3. Periods (84 pp., unchanged since cp12)** | 126 proved, 52 unverified | Split it: the strong-transcendence note (Thm 1.1, Cor 1.2) is blocked only by box 8 and a short write-up (board P91a). The rest is blocked by the 52 rows. |
| **4. Surgery (40 pp., unchanged since cp13)** | 22 proved, 38 scoped, 292 unverified | Blocked by the 292 rows, by the conditional nodal-q and fourfold inputs, and by the Gupta-Mj literature for the single cap. The single-cap note (P91b) is blocked only by literature and box 8. |
| **5. Relative positions (41 pp., unchanged)** | 17 proved, 8 scoped | C.06 (identity with Grothendieck's gluing); effort naming in the abstract; box 8; a Claude read of the local topology (P91c). |
| **6. Divided powers and dessins (31 pp., unchanged)** | 43/43 accepted by the run | Box 8; **no Claude check of any proof** (our intakes read statements only). That gate is mine to close in a later pass. |
| **7. Posets (45 pp., unchanged)** | 21 proved, 43 scoped, 18 unverified | The 43 scoped rows need final acceptance; Jenča's Order 40 page; box 8. |

## 6. Integration, applied

Rows are appended to `INTEGRATION_POLISH_TOPOLOGY_PERIODS_20261123.tsv`; backups are in `integration_backups/20261123/POLISH_TOPOLOGY_PERIODS/`.

**Applied:**
1. `reports_20261123/s20_note/s20_note_v2.tex` and `.pdf`: a new version, crediting the 2013 announcement.
2. `reports_20261123/s20_note/RECORDS.md` §7.
3. The EMAIL_DRAFTS file in this folder: Draft 2 revised, Draft 3 (Boyle-Chen) added.
4. `results_register/horizontal/sweep2/SA20/TOPIC_NOTES.md` and `SA10/TOPIC_NOTES.md`: cp19 updates appended.

**For the main session:**
- post version 2 of hexagon:2611.00937, or not;
- the board rows below;
- the prompt after 91b (items in `claude_math_notes/PROMPT_UPDATES.md`, unchanged, plus "split Paper 2 into three").

## 7. Board candidates (rows for HEXAGON_BOARD.tsv; for the main session)

| id (proposed) | line | result | adds | gate left |
|---|---|---|---|---|
| S20 (update) | algebra | Version 2 crediting Elliott's 2013 MathOverflow announcement | Correct credit | Posting version 2. |
| P91f | algebra | A non-Noetherian inclusion R ⊂ S with all polynomial tensor maps isomorphisms (unique plethory) but Ω(R,S) and S not flat | Flatness is not necessary for Elliott's plethory structure | Literature search (Elliott's plethory papers, Borger-Wieland, the Stacks Lazard example 06RH); independent re-proof of the colon identity; a short note. |
| P91g | topology | The three-sphere: π_2 P_TOP(S^3) = Z/2 while π_2 P_PL(S^3) = 0 | A concrete PL/TOP concordance discrepancy | A Claude targeted read; literature (Hatcher's Smale conjecture, Kirby-Siebenmann). |
| P91h | topology | π_0 P_PL(M) ≅ E(M) for compact PL M of dimension ≥ 6, without a smoothing | PL form of Hatcher-Wagoner-Igusa | A Claude read; comparison with Burghelea-Lashof-Rothenberg and Pedersen; this may be known. |
| S-BC (erratum line) | topology (erratum) | Boyle-Chen Thm A.6: the displayed generator is not end-fixing, and the group has order ≤ 2 (= 2 by Kalliongis-McCullough) | Corrects a published appendix | The e-mail first; not a post. |

## 8. For the P vs NP fleet

Nothing new maps onto the graph. Map M1 of the cp13 intake (the indicator power step to L-clb-033) is unchanged. The forest example is commutative algebra with no complexity content.

## 9. What the run has finished, what is open, and what the next prompt must carry

**Finished**, by the run's acceptance:
- Paper 1 entirely;
- the Paper 2 algebra (the S20 theorem, the Noetherian criterion, the arbitrary-base necessity, B075-B078, B082, the forest example) and most of the concordance components (A117-A123, A125-A132, A133, A134);
- Paper 6 entirely.

**Open:**
- A124 (dimension five);
- A135-A137;
- 131 rows of Paper 2, 52 of Paper 3, 292 of Paper 4, and the 43 scoped plus 18 unverified rows of Paper 7;
- C.06 of Paper 5;
- the visual QA and whole-paper readings of the 169-page Paper 2;
- box 8 everywhere.

**For the prompt after 91b's return:**
- the eight items logged at cp13 in PROMPT_UPDATES;
- split Paper 2 into three papers;
- route the Boyle-Chen, Bonahon and Walsberg records as in §3, with the published versions checked.

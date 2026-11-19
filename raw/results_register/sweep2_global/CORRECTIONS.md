# Corrections and refinements from sweep 2

Claude Opus 5.5 at effort max (sweep 2), 18 Nov 2026. The rows are by GPT-6 Astra (ChatGPT Pro mode). Each item gives:
- the rows;
- what is the case;
- the fix;
- how sure I am;
- what I read.

"Statement level" means the register rows and their dependency fields. Where I read a proof, the file and lines are
named. The checks I made are in `CHECK_EVENTS.tsv`. The items inside a single sweep-1 scope are in that scope's
CORRECTIONS.md and are not repeated here.

## A. Mathematics and statuses

**1. Δ|GT̂ = 0 is proved by two routes; the gates are named, and one of them is a strong new claim.**
- **Rows:**
  - LM7_PUSH E.3 (Open) and E.65;
  - EXIT_TOWER E.44, E.49;
  - GT_TOWER_CHECK A.1, A.3, A.7, B.2.1, B.2.3;
  - SECTION_GHOSTS (final) E.179–E.181, E.190, E.191, E.197, E.198;
  - DELTA_ON_GT A.84 (Open);
  - LM8_PUSH C.21.
- **What is the case:**
  - The character is the same in every run: GT_TOWER_CHECK A.7 uses "the character of the refereed LM7_PUSH E.65", and
    SECTION_GHOSTS E.191 uses the frames of E.95, whose check column confirms GT_TOWER_CHECK A.7.
  - Route 1 is EXIT_TOWER E.44 (𝒥(A) = A, through Boggi–Zalesskii Theorem A(iii) for C₂² in Γ_{0,[10]}) → E.49 →
    GT_TOWER_CHECK A.3, A.7.
  - Route 2 is SECTION_GHOSTS E.181 → E.190 → E.191. E.181 normalizes every GT̂ element to F_* with ρ(F_*) = 0 and
    claims that F_* satisfies relation (IV) of Nakamura–Schneps 2000 (E.179–E.180). By Schneps 2006, p. 670, F_* then
    lies in the group Λ of Hatcher–Lochak–Schneps 2000, which acts on genus 0 and 1. Route 2 does not use
    Boggi–Zalesskii.
  - Strictness: GT̂ ⊊ ker Δ ⊊ GT̂₀ (GT_TOWER_CHECK B.2.1, B.2.3; SECTION_GHOSTS E.197–E.198, with a degree-seven
    11-adic witness).
- **The fix:**
  - The handbook item (SC01) reads: proved, routes and gates named, pending an outside referee.
  - LM7_PUSH E.3 and DELTA_ON_GT A.84 get "decided by GT_TOWER_CHECK A.7 and SECTION_GHOSTS E.191".
  - The programme map's E.3 line names both routes. Sweep1_tower CORRECTIONS 1 proposed a sentence naming route 1
    only; add: "SECTION_GHOSTS (final, 18 Nov) proves it again by a route through Hatcher–Lochak–Schneps's Λ, without
    Boggi–Zalesskii."
  - E.179–E.181 claim that every normalized element of GT̂ satisfies (IV). That is the question Nakamura–Schneps and
    Hatcher–Lochak–Schneps left open, whether their subgroups are all of GT̂. Before any claim of novelty, set it
    against Lochak–Nakamura–Schneps 2026 (arXiv 2602.12462, Theorem 1.1 and §8), which SECTION_GHOSTS's bibliography
    cites, and send E.179–E.181 and EXIT_TOWER E.44 to a referee from another model family.
- **How sure:**
  - high on the records, the identity of the character, and that the routes differ;
  - E.181's normalization step checked;
  - EXIT_TOWER E.44 read in full, its genus-zero algebra and geometry checked: the ten-point configuration, the
    centralizer sequence, the topology, the rational identities of (E.217), and the commutation with the cusp swap.
    What it leaves unchecked is Boggi–Zalesskii 2024 Theorem A itself, used for the conjugacy of F(H) and for
    C_Ĝ(H) = N̂, and E.27, E.28, E.37 (CHECK_EVENTS);
  - E.179–E.180 and E.182–E.190 not checked.
  - So the route-1 gate reduces to the exact statement of Boggi–Zalesskii's Theorem A (i), (iii) for p = 2, and to
    E.28. A referee should start there.
- **Read:**
  - the rows;
  - SECTION_GHOSTS final, `sections/part_E_gt_tower_repair.tex`, lines 1–175;
  - its results rows E.176–E.202;
  - sweep1_tower SUMMARY §3 and CORRECTIONS 1–4;
  - sweep1_sections SUMMARY point 4.

**2. The p-adic local section theorem is one gate under 73 rows; the register should mark them Conditional.**
- **Rows:**
  - LM8_PUSH D.54, D.56, D.23;
  - FERMAT_SUCCESSOR A.20, A.31, A.11;
  - LM6 rows using Tool (1);
  - SECTIONS_OVER_Q rows with "uses_local_theorem: yes";
  - SECTION_GHOSTS;
  - ANABELIAN_149_PUSH D.15, D.16.

  The list is `tools/local_theorem_rows.tsv`.
- **What is the case:**
  - The theorem is claimed in OpenAI's preprint "The p-adic section conjecture" (6 Oct 2026). ANABELIAN_149_PUSH's
    prompt row R24 calls it unrefereed.
  - LM8_PUSH D.54 (prosolvable) and D.56 (full formations with two primes) re-derive it from the preprint's Sections
    3–6 and Mochizuki–Tsujimura 2024, Theorem F(i) and Proposition 2.4(iv).
  - The two sweep-1 agents give "the section set of U_n/Q is the three cusp packets" opposite statuses: sweep1_tower
    proved, sweep1_sections conditional.
- **The fix:**
  - One handbook item for the theorem (SC03), status "claimed in the literature; re-derived in LM8_PUSH; unrefereed".
  - Every row resting on it reads Conditional (G1).
  - The Selmer part of the Fermat theorem is unconditional; keep it apart (item 3).
- **How sure:**
  - high on the records;
  - the list of 73 is by script, so it may miss rows that rest on the theorem without naming it.
- **Read:** LM8_PUSH `sections/D_formation_local.tex`, lines 1–60; the rows.

**3. The Fermat Selmer theorem: one error found twice, and two independent repairs.**
- **Rows:**
  - LM6 E.8 (Known), E.12;
  - LM8_PUSH D.22, D.23;
  - FERMAT_SUCCESSOR A.3, A.4, A.11, A.16;
  - SECTION_GHOSTS E.100;
  - LM7_FERMAT_TOWER E.25.
- **What is the case:**
  - The divisibility step that LM6 E.8's proof cites from Steklov (Propositions 4.6, 5.10) is false: at the unit Fermat
    cusp q = 256⁻¹t^{2n}(1 + O(t^n)), so v₂(q) = −8.
  - LM8_PUSH D.22 (checkpoint 17, 16 Nov 02:52) and FERMAT_SUCCESSOR A.4 (checkpoint 6, 16 Nov 06:49) found it
    independently.
  - D.23 and A.11 each re-prove that every Selmer section of U_n/Q is cuspidal for odd n ≥ 3.
  - SECTION_GHOSTS E.100 proves that for even n not even the geometrically pro-2 abelian extension has a section. This
    is stronger than LM7 E.25.
- **The fix:**
  - LM6 E.8: "statement Known; the cited proof's divisibility step refuted (LM8_PUSH D.22, FERMAT_SUCCESSOR A.4);
    repaired proof FERMAT_SUCCESSOR A.3–A.6".
  - Split LM6 E.12 into three items: Selmer ⇒ cuspidal (proved, two proofs); no sections for even n (proved,
    SECTION_GHOSTS E.100); every section is Selmer (conditional on item 2).
  - The outreach item to Steklov (sweep1_sections) can name both discoveries.
- **How sure:** high. I checked the leading term of q (CHECK_EVENTS).
- **Read:** the rows; sweep1_sections CORRECTIONS 2–3; sweep1_tower CORRECTIONS 7.

**4. CATHOT E.17 is settled: true for U-small filtered indexes.**
- **Rows:**
  - CATHOT E.17 (Open);
  - INDLOCAL B.1, B.2, B.3, B.5, B.7, B.9;
  - GALOIS B.12;
  - S2COUNT E:boundedtransport.
- **What is the case:**
  - INDLOCAL's prompt row R3 gave two proofs of E.17: GALOIS B.12, and Theorem 3.2 of the Dérivateurs expert's
    OWN_RESULTS (Claude Fable 5.2 at effort max).
  - INDLOCAL B.1 checks both: for U-small filtered I, W_∞-invariance of H_K forces K ≅ (Π₁K_i) in Ind(Cat_hot).
  - The boundary: B.5 shows it fails for V-small indexes (with K(Z/2,2)); B.7 gives the exact threshold for tests with
    fewer than κ arrows; B.9 covers uniformly finite stages.
- **The fix:** CATHOT E.17 is "Proved (INDLOCAL B.1 with GALOIS B.12)", with B.5, B.7 and B.9 as its boundary. Sweep1_
  derivateurs handed this question to sweep 2.
- **How sure:** medium-high. I read B.1's proof at paragraph level; R2, the Kan–Thurston input, was not rechecked.
- **Read:** INDLOCAL `sections/B.tex`, lines 1–150; its prompt row R3; CATHOT E.17.

**5. FINMON answers two of CATHOT G.17's three questions and CATHOT D.6, and extends RESIDUE A.5.**
- **Rows:**
  - FINMON C3, E1-KZ2-category, E1-KZ2-monoid, E4, cor:E-uncountable, E5, B4-CP2, C2-CP2;
  - CATHOT G.16, G.17, D.6;
  - S2COUNT A.M1;
  - RESIDUE A.5.
- **What is the case:**
  - The RP² poset minimum is 49 arrows (FINMON C3). CATHOT G.17 left it in [28, 49].
  - K(Z,2) has no finite category and no finite monoid model (FINMON E1).
  - The six-element monoid with [BM, S²] of cardinality continuum is proved twice: S2COUNT A.M1 and FINMON E4.
  - FINMON's classification through order 6 (1,565 iso/anti-iso classes) agrees with RESIDUE A.5 (orders ≤ 5) and
    with the known enumeration of monoids.
  - The CP² monoid minimum is 23; the category minimum lies in [17, 22] (FINMON checkpoint 20).
- **The fix:**
  - Add FINMON to the register (item 13).
  - CATHOT G.17: "two of three parts answered (FINMON C3, E1); the intrinsic classification open".
  - CATHOT G.16's table: the RP² poset entry becomes 49.
- **How sure:**
  - high on the records;
  - FINMON's proofs not checked by me;
  - the counts checked against the published enumeration (CHECK_EVENTS).
- **Read:** FINMON's results and report (lines 3–12, 69, 339, 432, 489, 491); the rows.

**6. Three prompt paraphrases were wrong. The later runs refuted or corrected the paraphrase; the source rows stand.**
- **Rows:**
  - ANABELIAN_149_PUSH F.1, F.17 (against its prompt row R27, which paraphrases LM5 F.3–F.50);
  - SECTION_GHOSTS E.100 (against its R8, paraphrasing SECTIONS_OVER_Q R17, LM6 E.16 and E.31–E.34, E.38, LM7 E.25,
    E.32, LM8 F.21);
  - FERMAT_SUCCESSOR C.14 (against its R18, paraphrasing LM6 A.10, A.49, A.56–A.59, A.66, A.67).
- **What is the case:** what each paraphrase lost:
  - R27 dropped "closed-point-preserving" from "pinned";
  - R8 generalized specific noncuspidal sections to "every Fermat curve, all quotients";
  - R18 said "no lift", where the theorem is "no commuting third-derived lift".
- **The fix:**
  - No status change for LM5, LM6, LM7 or LM8.
  - Register prompt rows as items of their own (PROMPT:RUN:Rk), so that a refutation of a paraphrase attaches to it.
  - When a prompt restates a result, quote its hypotheses exactly. This is a lesson for prompt writing:
    the three errors all came from compression.
  - My script's 30 "refutes" and "corrects" edges on these rows are wrong (CONSISTENCY §1).
- **How sure:** high.
- **Read:** the rows; the prompts' rows R27, R8, R18 (`tools/prompt_rows.json`).

**7. CYCLOTOMIC_KERNEL E4 is a mixed row; its two cross-run uses are sound.**
- **Rows:** CYCLOTOMIC_KERNEL E4 (Open); ANABELIAN_149_PUSH D.2, B.15u.
- **What is the case:** H2(a) is proved; H2(b) and the R4 completion are open. D.2 (an implication) and B.15u use the
  proved half, through prompt row R15 ("Proved there except the second half of E4").
- **The fix:** split E4 into E4a (Proved) and E4b (Open).
- **How sure:** medium (statement level).
- **Read:** the rows; prompt row R15 of ANABELIAN_149_PUSH.

**8. The birational question over Q(t) stays open, with a criterion.**
- **Rows:** ANABELIAN_149_PUSH D.U2 (Unresolved); LM6 F.13; CYCLOTOMIC_KERNEL B8.
- **What is the case:**
  - LM6 F.13: a section of G_L → G_K lies in a decomposition group of a rational place iff its centralizer is
    nontrivial. It does not prove that every section has a nontrivial centralizer, so D.U2 (the birational section
    conjecture for P¹/Q) stays open.
  - LM6 F.13 confirms CYCLOTOMIC_KERNEL B8: his formulas (32)–(33) at cote 149, scan 127 are false as written.
- **The fix:** link D.U2 to F.13 as its strongest reduction. Mark his claim at scan 127 refuted twice.
- **How sure:** medium-high.
- **Read:** the rows.

**9. "Refuted" carries two meanings, and the register should split them.**
- **Rows:**
  - LM8_LIE E.11 against LM5 F.12;
  - S6_06_BLIND P2.11 against S6_02_PUSH A.3.2;
  - FINMON E1-KZ2-*;
  - the 14 cross-run uses of Refuted rows in CONSISTENCY §2.
- **What is the case:** most Refuted rows state a true counter-statement. The same mathematics appears as Proved in one
  run and Refuted in another.
- **The fix:** two linked items per refutation: the claim (refuted) and our statement (proved). Sweep1_derivateurs C8
  and sweep1_tower reached the same conclusion inside their scopes. Across scopes, this one convention explains both
  apparent contradictions.
- **How sure:** high.

**10. "Ghost" names two objects.**
- **Rows:**
  - section ghosts: SECTIONS_OVER_Q A.32, A.44, A.51; GT_TOWER_CHECK C; SECTION_GHOSTS;
  - the GT̂₀ element of EXIT_TOWER E.46, called a ghost in GT_TOWER_CHECK's prompt Lead 6.
- **The fix:** in the handbook, "section ghost" (I.4.6) and "pentagon ghost" (I.1).
- **How sure:** high.

**11. Rows that state two things, each used by the other.**
- **Rows:**
  - EXIT_TOWER E.11 ↔ E.26 (a discrete presentation and a completed one);
  - FERMAT_SUCCESSOR C.4 ↔ C.5 (C.4's CM-pair addendum uses C.5);
  - EXIT_TOWER E.37 ↔ E.44 (each states the combined conclusion "compatibility for every GT̂ element").
- **The fix:** split, so that the dependency order is linear.
- **How sure:** medium (statement level). In none of the 10 pairs I read did I find a circular argument (CONSISTENCY §3).

## B. The register and its records

**12. The register's dependency parse.**
- **What is missing:**
  - the run aliases: LM4, LM7, LM8 and their PUSH/SUCCESSOR, TOTASPH, TOTAL_EXACT(_2), F149, CK-, AS-, AP-, AN, LM5-,
    S6_02, GT, DELTA, SECTIONS;
  - LaTeX-escaped underscores (LM7\_PUSH);
  - ranges (A.4–A.9, D.2.22–26);
  - sub-items (E.97.1, D.37f);
  - prompt rows (R13 → LM7_PUSH D.50, E.58);
  - glued forms (POLESB.2B.5).
- **The fix:** adopt the alias table and the prompt-row resolution of `tools/core.py`, `tools/prompts.py` and
  `tools/resolve.py`. They raise the "uses" edges from 13,699 to 16,924 and the cross-run edges from 94 to 3,159, with
  30,323 edges of all kinds. Also
  ignore file names in where_proved: `ANABELIAN_A1_SUCCESSOR_paper.tex` parsed as the id A.1 and made four false cycles.
- **How sure:** high.

**13. FINMON is missing.**
- Its checkpoint-20 folder holds encoded files; the decoded table sits in
  `FINMON/FINMON_checkpoint_20_decoded_20261117/FINMON_results.csv` (695 rows).
- The fix: read decoded folders in `field_experts/build_check_ledger.find_returns`. My placement and merges are in
  `FINMON_PLACEMENT.tsv` and `FINMON_MERGES.tsv`.

**14. PRETOT and TOTEX are on the wrong line.**
- They are Dérivateurs mathematics: TOTAL_EXACT is TOTEX, PRESHEAF_TOTALITY is PRETOT, and their prompts sit in
  `derivateurs_companion_20261109/pro_prompts_max_20261112/ALREADY_RAN`. The register files them under the Longue
  Marche because their returns sit in that line's answers folder.
- Sweep1_derivateurs took them into its scope.

**15. Two returns have moved on.**
- SECTION_GHOSTS has a final (13:05 UTC, 228 rows).
- S6_06_BLIND checkpoint 33 was retired into checkpoint 35's `_from_earlier_checkpoints`, so the register's results
  path no longer exists.
- The fix: rebuild the register.

**16. The prompts record referee outcomes that the check ledger lacks.**
- 379 prompt rows on 329 statements carry outcomes such as "refereed: proved as claimed" (Claude Opus 5.5 at effort
  max), "checked", "followed" or "unread" (`tools/prompt_checks.tsv`).
- The fix: these are check events; add them to `field_experts/check_ledger.jsonl` with the prompt as the document.

**17. Summary rows make 30 of the 59 cycles.**
- The fix: a "bears on" relation kept apart from "uses" (CONSISTENCY §3; `CYCLES.tsv` names the hubs).

**18. Conditional is dropped.**
- Sweep 0 normalizes "Proved, conditional on the stated local theorem" (FERMAT_SUCCESSOR A.20) to Proved.
- The fix: keep "Conditional" with the condition's item; item 2 lists the rows.

**19. The guard refuses sub-agents of sub-agents.**
- This is not a register defect, but it decided how this sweep ran. `claude_tools/agent_guard.py` (nesting_budget)
  reads the transcript at the hook's `transcript_path`. Inside a sub-agent this was the main session's transcript: no
  "Sub-agents allowed" line in its first message, so 0 allowed, and 455 launches counted.
- All five sub-agent launches of this sweep were refused.
- The fix, for the main session to decide: read the sub-agent's own transcript (its `agent_id`) or the brief of the
  Agent call that launched it.
- I did not change the guard.

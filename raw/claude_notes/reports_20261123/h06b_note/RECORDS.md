# H06b note: records

Editor: Claude Fable 5.2 at effort max (agent a49aabbf5ed57bb8e), 23 Nov 2026. The mathematics and the body of the
text are by GPT-6 Astra (ChatGPT Pro mode). Nothing has been sent, posted or pushed.

- Note: `h06b_note.tex`, `h06b_note.pdf` (16 pages; pdflatex, three passes; no overfull box; every page rendered and
  read by me). Comments: `REVIEW_a49aabbf_v1.md`.
- Title: "The question of Anderson and Ihara on the pro-p Galois action on the projective line minus three points,
  at every prime satisfying Vandiver's conjecture".
- Theorem 1.1: for odd p, (a) X_p^+ finite ⟹ Ω_p* = Ω_p; (b) p ∤ h(Q(μ_p)^+) ⟹ X_p^+ = 0; (c) every odd p < 2^31.

## 1. How the note was made (reproducible)

`build\assemble.py <run's main.tex> h06b_note.tex`, with `build\opening.tex` and `build\closing.tex`.
Source: `NIGHT_AFTER_ALPOGE_checkpoint_11_20261123T1024Z_unzipped\workbench\k-theory-and-galois-groups-workbench\papers\ihara\main.tex`
(1311 lines; identical in checkpoint 13).

| Part of the note | From | By |
|---|---|---|
| Title, abstract, Sections 1–2 (question, theorem, meaning, credit, context, scope, proof overview) | `build\opening.tex` | editor |
| Sections 3–7 | the run's lines 128–1004 (its Sections 2–6) | GPT-6 Astra |
| Section 8, "What remains open" | the run's lines 1154–1183 (its Section 8), new heading | GPT-6 Astra |
| Provenance and checks | `build\closing.tex` | editor |
| References | the run's list, the 14 items cited in the note | GPT-6 Astra |

**Changes inside the run's text (five places, none mathematical; the script checks each line before changing it):**
1. line 152, "These statements hold also for p = 2.": removed;
2. lines 161–162: "At odd primes H = Gal(Ω_p/F_∞); at two H = ker(χ₂ ...)" → "H = Gal(Ω_p/F_∞).";
3. lines 190–191: the sentence on the normalization at p = 2 removed;
4. line 441: "its actual conjugates" → "its conjugates";
5. lines 1000–1001: "together with the result at 2 in the next section" removed.

**Left out:** the run's Section 1 (replaced by the editor's), its Section 7 (the prime 2, lines 1005–1153), its method
paragraph (replaced), and three references cited only there (Brown 2019, Gras–Jaulent, Mináč–Pasini–Quadrelli–Tân).

## 2. Check events (types of the check rubric)

| Statement (note) | Date | Who | Type | Outcome |
|---|---|---|---|---|
| Lemma 7.1 and X_p^+ = 0 under Vandiver (Section 7) | 23 Nov | Claude Opus 5.5 at effort high (ad85573792c61a914) | targeted proof check, present text | confirmed, every step |
| Lemma 5.1 (separation), as K17-POLE-GENERAL | 22 Nov | Claude Opus 5.5 at effort high (same agent; K17 intakes) | targeted proof check, earlier version | confirmed; not compared with the present text line by line |
| Theorem 1.1 at Vandiver primes, as the K17 Vandiver deduction | 21 Nov | Claude Opus 5.5 at effort high (K17 intakes) | targeted proof check, earlier version | confirmed; same caveat |
| Section 6 (use of Wake–Wang-Erickson and Fukaya–Kato), Lemma 4.1 in the present text | — | — | none outside the run | the run records its own same-model reread |
| Sections 3–7 | 23 Nov | Claude Fable 5.2 at effort max (a49aabbf) | carried as background without fault found | read once as editor; not checked |
| Sections 1–2, closing | 23 Nov | a49aabbf (author) | none by anyone else | unchecked |

I did not open the K17 intakes for this pass; the three Opus rows are as the cp11 intake states them
(`field_experts\intake_20261121\intakes\NIGHT_AFTER_ALPOGE\INTAKE_NIGHT_AFTER_ALPOGE_20261123_cp11_partsAC.md`, §§0 and 2).

## 3. Literature

| Work | Locator | Read by me |
|---|---|---|
| Anderson–Ihara, Ann. of Math. 128 (1988) 271–293 | p. 272, question (a) | no (the run read it through Ishii's reproduction, p. 2) |
| Ihara, Ann. of Math. 123 (1986) 43–106 | inclusion Ω_p* ⊆ Ω_p, as attributed in Sharifi 2002 p. 1 | no |
| Sharifi, Proc. Sympos. Pure Math. 70 (2002) 275–284; arXiv math/0104116 | Theorem 1.1 p. 2; Lemma 2.1; §§1, 4 (author's version) | abstract only |
| Brown, Ann. of Math. 175 (2012) 949–976 | Theorem 1.1 | no |
| Hain–Matsumoto, arXiv math/0006158v2 | Prop. 8.3, Thm 8.4; App. A.6, A.9–A.10 | no |
| Fukaya–Kato, "On conjectures of Sharifi", preprint of 15 Aug 2012 | §6.1.5; §§7.1.8–7.1.10 | no |
| Wake–Wang-Erickson, Amer. J. Math. 140 (2018); Proc. AMS Ser. B 4 (2017) | Cor. 2.1.3, Conj. 2.1.5, Cor. 8.1.3(2); Prop. 2.2.6, Lemma 5.2.7 | no |
| Ishii, arXiv:2312.04196v3 (6 Jan 2026) | Theorem 1.1, Remark 1.1.1, p. 2 | abstract only |
| Ishii, arXiv:2602.00615 (31 Jan 2026), graded Lie algebras for once-punctured CM elliptic curves | — | search summary only; not cited in the note |
| Hart–Harvey–Ong, Math. Comp. 86 (2017) 3031–3049 | §1 item (2) | no |
| Rasmussen–Tamagawa, arXiv:1803.08524 | abstract (a related rationality question) | abstract; not cited |
| Sharifi, Ann. of Math. 173 (2011) 251–300 | named in my task | **not opened** |

The run's own audit of each source it opened, with pages and SHA-256, is `SOURCE_AUDIT.md` beside its paper.
**Hexagon** (23 Nov): "Ihara": one unrelated work (2610.00558); "Vandiver": none.

**Verdict of the reading gate:** known: the equality at odd regular primes (Sharifi 2002 with Brown 2012).
Not found: the equality at any irregular prime, or the range p < 2^31. My reading was at the level of abstracts and
two searches, because the context rule stopped further reading; see REVIEW.

## 4. Before posting

1. An outside reading of Sharifi 2002 (§§1, 4) and the introduction of Sharifi 2011, for any statement on the kernel
   field at irregular primes.
2. A check of Sections 4–6 of the note in their present text, above all the application of
   Wake–Wang-Erickson Corollary 8.1.3(2) and Fukaya–Kato §7.1.10 (Section 6).
3. The user's word; the line of authors; the address of the workbench.

## 5. Whom to write to when it is posted

- Romyar Sharifi (UCLA): the regular case is his; his symbol map carries the new step.
- Takako Fukaya and Kazuya Kato; Preston Wake and Carl Wang-Erickson: their theorems are the arithmetic input.
- Francis Brown; Richard Hain and Makoto Matsumoto: the rational image.
- Shun Ishii: the analogue for CM elliptic curves; the comparison in his Remark 1.1.1.
- William Hart, David Harvey and Wilson Ong: the range 2^31.
- Yasutaka Ihara and Greg Anderson: the question.

## Main-session reading and fixes, 23 Nov 2026 13:57 UTC

Read in full by the main session 329fb1e6 (Claude Opus 5.5 at effort max). Checked in full: Lemma 7.1 (persistence: inertia of order p, its normal closure, the unramified quotient, the Frattini argument) and the deduction X_p^+ = 0 (plus parts via extension and norm); the identification of the dense subgroup in Section 3; Lemma 6.1. Followed, relying on the line-by-line check of ad85573792c61a914 (Claude Opus 5.5 at effort high, REVIEW_ad855737_v1.md): Lemmas 4.1 and 5.1 and the arithmetic of Section 6. No error found. Type: targeted proof check (Section 7, Lemma 6.1); read (the rest).

Fixes made by the main session, from REVIEW_ad855737_v1.md: abstract (the present text of Sections 4-6 checked, with FK and WWE read at the places cited); Section 1 Credit (Vandiver => Sharifi's conjecture is Wake-Wang-Erickson's, 2017, abstract and Cor. 5.1.2); Section 1 Context (Sharifi 2019, RIMS Kokyuroku 2120, p. 222, quoted: the irregular case 'a very interesting open question of Anderson and Ihara'; new bibitem Sharifi2019); Section 6 eigenlift citation now 'Lemma 4, p. 3 of arXiv:math/0104116v2' (was 'Lemma 2.1, pp. 3-4'); the provenance paragraph (the checks of 23 Nov; Milne LEC, Sharifi's notes, Iwasawa 1981 carried). Previous text kept as h06b_note_before_main_fixes_20261123.tex. h06b_note.tex is now the master: do not regenerate it with build/assemble.py. Rebuilt (pdflatex, three passes): 16 pages, no overfull box.

Before posting: Sharifi 2002 'Theorem 1.1' in the author version vs 'Theorem 1' in arXiv v2 (check the 13-page version); what Section 1 says of Anderson-Ihara 1988 and Ihara 1986 beyond the question (from the editor's memory); the run's defensive asides in Sections 3-6 (optional polish); view every rendered page; the user's word.

## Version 2 committed (24 Nov 2026, 23:14 UTC)
Main session 329fb1e6 (Claude Opus 5.5 at effort max), at the user's word of 24 Nov ~22:0x UTC (v2s welcome, sooner rather than later). Changes by a49aabbf (Claude Fable 5.2 at effort max), each at the source: Sharifi 2002 in the arXiv v2 numbering (Theorem 1 p. 2, Lemma 4 p. 3); Sharifi 2019 on p. 221 of RIMS Kokyuroku 2120, pp. 220-227 (v1: p. 222, pp. 221-228; my brief had the page wrong too); 'earlier versions' removed from the check account; new Remark 7.2 (Kurihara via Weibel VI Cor. 8.3, Thm 10.9; Mok-Zheng unrefereed, adds no prime) and Remark 8.1 (Ishii Thm A = 2.14 with its hypotheses). The main session checked the diff, the deduction in Remark 7.2 (eigenspaces omega^{-2k}, k = 1..(p-3)/2; Mok-Zheng covers all parts only for p <= 61), added one sentence on that check (a stray CR from shell escaping fixed by fix_cr.py), rebuilt (18 pp., 0 overfull, 0 undefined) and viewed pages 14-16. Hexagon: revise -> draft 8081f551; v1 source (upload ceb95515) removed; v2 uploaded as anderson_ihara_vandiver.tex (v2_upload/); metadata HEXAGON_METADATA_WB0006_v2.json (build_meta_wb0006_v2.py: METADATA_PROVENANCE_v2.txt's paragraphs, change note at the head of comments); verify-meta same; preview identical in text on all 18 pages (8,720 words). Committed 23:14:37 UTC: hexagon:2611.00939v2, sourceTreeSha256 79032640...3f5c83.

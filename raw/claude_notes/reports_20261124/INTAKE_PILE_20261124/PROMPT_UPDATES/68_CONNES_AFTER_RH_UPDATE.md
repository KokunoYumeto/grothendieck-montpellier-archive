# Prompt 68_CONNES_AFTER_RH: reworked around Connes's Lemma 3 in characteristic zero (24 Nov 2026)

Written 24 Nov 2026 by Claude Opus 5.5 at effort max (the number-theory mapper of the intake pile), for the main session
329fb1e6 (Claude Opus 5.5 at effort max), following `PROMPT_UPDATE_BRIEF.md` and the main session's instruction of 24 Nov
2026: "rework 68 around its own untried route ... Build in the literature gate first ... Keep the T51 equivalence as
background, not as the result." The prompt stays in the queue; the user decides whether it is sent.

## 1. State before the change, and why it was held

- **Send state.** `TO_SEND/PRO/1_Archive_research_by_topic/68_CONNES_AFTER_RH/` was not in `TO_SEND/PRO/SENT_PRO.tsv` (the only
  "68" there is the SA22 prompt on cotes 66-68) and not in a SENT folder.
- **How it is built.** It is builder-built from `pro_prompt_builds/PAPERS_20261122/specs/68_CONNES_AFTER_RH.md` and
  `.plan.json`.
- **Why it was held** (`field_experts/hexagon/HEXAGON_BOARD.tsv`, row H27). Its result T51, "Connes's trace formula over Q
  (explicit cutoff) is equivalent to GRH for Dirichlet L-functions", is Connes's own statement. The editor (Claude Fable
  5.2 at effort max, 23 Nov) wrote no note, and the row reads "hold; no post (the user: 'isn't that super obvious?');
  prompt 68 held". The old PROMPT.md l.25 says "No main gate moved between the two checkpoints".
- **My first verdict** (earlier today) was that the old main question, a second proof of RH from the cutoff, was not
  worth a run. The prompt already listed the right route as untried (old research item 1: "the analogue over Q of
  Connes's Lemma 3 proved with no hypothesis"). The main session then asked for the rework below.

## 2. Backups and build

- **Send folder.** It was copied to `TO_SEND/PRO/_backups_20261125/68_CONNES_AFTER_RH/` (PROMPT.md 33,049 bytes and the
  ZIP of 20,296,752 bytes, both checked identical by `cmp`). The original folder was then moved, not deleted, to
  `TO_SEND/PRO/_backups_20261125/68_CONNES_AFTER_RH_send_folder_before_lemma3/`, because the builder's `--place` refuses an
  existing target.
- **Spec and plan.** Both were copied to `pro_prompt_builds/PAPERS_20261122/specs/_backups_68_before_lemma3_20261124/`.
- **Build.** `python -I -B build_papers.py 68`: "68_CONNES_AFTER_RH | files 2777 | not attached 406 | ZIP 22.8 MB |
  prompt 6270 words | lints PASS". `--place 68`: "placed".
- **Placed folder.** PROMPT.md (40,209 bytes) and `68_CONNES_AFTER_RH.zip` (22,821,488 bytes; 2,777 members, no ZIP
  inside, `testzip` clean).
- **Lints, re-run on the placed PROMPT.md.**
  - `push_rule_pro_prompts.py --lint-math`: "files: 1 failing lint: 0".
  - `paper_completeness_lint.py`: "files: 1 failing: 0".

## 3. The changes, with their evidence

1. **The main question** (spec PUSH line, the new title, "Why this matters", research item 1). It is now Connes's Lemma 3
   in characteristic zero: the exact limit of the prolate cutoff expression T_Λ(h) of statement 2 as an explicit sum over
   all zeros of the strip, with no hypothesis, the zeros off the line entering with their own weights. This is first for
   every primitive Dirichlet character over Q, then for the Hecke characters of Q(√−3). Evidence: Connes 1999 §VIII
   (Theorem 5, Lemma 3), and the old prompt's own untried route (old l.116-118).
2. **The T51 equivalence is now background, not the result** (item 1 of "Where it stands"). It is renamed "Background,
   not the result: the equivalence". It is stated with T_Λ(h) defined, and it is to come out of the main theorem as a
   corollary. Evidence: board row H27 and the user's [the user's words, omitted].
3. **The literature gate comes first** (new section "First: what is already proved"). The run must open each source at
   its statements and record in LITERATURE.md, and in the paper's introduction, exactly what is already proved and where
   its theorem goes beyond it. The sources:
   - Connes 1999 §VI-VIII and Appendix II;
   - Connes-Consani, the archimedean place (arXiv 2006.13771);
   - Connes-Consani-Marcolli (Prop. 6.2, Cor. 6.3);
   - Meyer (Duke 2005);
   - Connes-Consani, *Spectral triples and ζ-cycles* (arXiv 2106.01715);
   - Connes-Moscovici, *Prolate spheroidal operator and Zeta* (arXiv 2112.05500);
   - Connes-Consani-Moscovici, *Zeta zeros and prolate wave operators* (arXiv 2310.18423);
   - Connes, *An essay on the Riemann hypothesis* (arXiv 1509.05576);
   - Suzuki (arXiv 2610.32704);
   - forward citations on arXiv and Hexagon, including Connes and coauthors since 2023 and Andrews-Connes-La Gatta.

   The four new arXiv ids were checked against their titles through the arXiv API before the build. The TeX of all four
   is now attached (`literature/LIT_Connes_Consani_spectral_triples_zeta_cycles/`,
   `LIT_Connes_Moscovici_prolate_spheroidal_zeta/`, `LIT_Connes_Consani_Moscovici_zeta_zeros_prolate/`,
   `LIT_Connes_essay_Riemann_hypothesis/`).
4. **The part over Q(√−3)** (research item 2). It asks for:
   - the cutoff per Hecke character, and the analogue of T50 with no hypothesis;
   - the limit formula;
   - a bound of the off-line contribution through Liu's θ_G, Hu's 7/8 or OpenAI's 7/8;
   - the statement for the cubic Kummer character of Q(√−3, ∛269);
   - a comparison with BEYOND_DIRICHLET's reduction to square-root cancellation.

   Evidence: Liu, Hexagon 2611.00741v1, abstract and pdf l.1-60; Hu, Hexagon 2610.00216v2, Cor. 9.6; Cureton-Thorner,
   Hexagon 2610.00200v2, Thm 1.1 and Cor. 1.2; OpenAI's preprint of 30 Sep 2026; BD cp10
   `research/cubic_joint_content_fragment.tex` l.119-155.
5. **New inputs in "Where it stands"** (item 7). They are stated exactly, marked unrefereed, and attached:
   - the PDFs of Liu 2611.00741v1, Hu 2610.00216v2 and Cureton-Thorner 2610.00200v2 (no TeX source found for these
     Hexagon works);
   - the TeX of OpenAI's 7/8 preprint, from `github.com/openai/math`, `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.

   The SHA-256 of each source copy is in `PROMPT_UPDATES/68_sources/`:
   - Liu: eb22f2fa…6a;
   - Hu: 116ae2b2…2e;
   - Cureton-Thorner: 46cc2c2a…26;
   - OpenAI: 42a5ee0f…a3.
6. **BEYOND_DIRICHLET inputs** (item 7; my map, NK-5 and NK-6).
   - The cubic gate.
   - γ = (θ_G − 1/2)/(2θ_G − 1/4) = 0.2494429741… once the "classical zeta RH" of jct:liu-specialization is read as
     Alpöge's theorem.
   - Borger Λ-schemes over Z[1/N] (th:category): statement 2 for every Dirichlet character is the trace formula for all
     of them.
   - The relative Frobenius lifts of Q(√−3, ∛269) over the integers of Q(√−3) (th:frobenius).

   Attached under `ours/BEYOND_DIRICHLET_cp10/`: STATEMENTS.tsv, `research/cubic_joint_content_fragment.tex` and
   `research/structural_comparisons.tex`.
7. **The intake map** is attached as `ours/structural/MAP_NUMBER_THEORY_20261124.md` and `.tsv`, marked as having no second
   reader for its new statements.
8. **The Artin primitive-root results** enter research item 4. OpenAI's marked Type II estimates, as used with a
   varying-cofactor sieve in its primitive-root preprint of 4 Oct 2026 and in Hexagon 2610.00228, 2610.00294 and
   2610.00699, are named as the published form of the "mean number of marked Type II solutions in each fixed Frobenius
   class" that item asks about. One wording change in the item: "force one actual occupied shell" (it read "force at
   least one").
9. **Kept as they were.** Items 2-6 of "Where it stands", with three additions:
   - item 4 says that T31 is the nearest existing piece of the limit formula;
   - item 4 says that the formula needs the full distribution of the prolate eigenvalues across the edge, not only
     ν ≥ 1/4;
   - item 6 says that the finite test was posted on Hexagon as 2611.00996 (24 Nov 2026) and restates the division of
     ground with the exact-limit wording.

   Research items 2, 3 and 5 of the old prompt are regrouped as the new item 3 ("Consequences inside our programme").
   The Bost-Connes bullet, which was "from memory", was dropped. The push paragraph, the three-hour ledger check, the
   checkpoint rules and CHECK_EVENTS.tsv come unchanged from `core/HOW.md`.
10. **Dates** are written as 24 Nov 2026; the placed prompt contains no "25 Nov".

## 4. What prompt 70d (HODGE_EFFECTIVE) should take from my map's item 2

70d belongs to the geometry mapper. The content is in my map (`MAP_NUMBER_THEORY.md`, NK-2, links L13-L15b, check event
E07); the main session has routed THETA3-C32 to the 70d updater as well.

**The criterion made effective.**
- Paper A's Galois-orbit criterion (`HODGE_FINISH_final_20261123T1713Z_unzipped/workbench/work/UNFILED-A/v1/paper/
  main.tex` l.3277-3304) holds without "André-Oort for every Cartesian power of S". Pila-Shankar-Tsimerman (arXiv
  2109.08788) give that qualitatively, and Jaswal's theorem effectively.
- Scanlon's ineffective B_S(H) is replaced by Jaswal's effective discriminant bound (Hexagon 2611.00339v3, Thm 1.1(ii) and
  Cor. 1.2), with Cureton-Thorner (Hexagon 2610.00200v2, Thm 1.1) supplying QRH(1/32; L) for every L. If D_D is proper,
  every relative-Weyl special point x ∈ D_D has d_{L_x} ≤ c(1/32, H(D), [F:Q]·H(D)) and α_x ≤ c(1/32, H(D),
  [F:Q]·H(D)).
- *Proof.* Paper A's own argument (l.3297-3299, via Chai-Oort Lemma 6.3) makes {x} maximal special in each component of a
  proper D_D.
- **Effective forcing.** δ_W(x) ≤ D and d_{L_x} > c(1/32, H(D), [F:Q]·H(D)) give D_D = S.
- **Effective dichotomy** (an effective HECKE_DIV R23). Either the Weil classes are algebraic on the whole family, or
  δ_W(x) > D at every relative-Weyl special point with d_{L_x} > c(1/32, H(D), [F:Q]·H(D)).
- **H15 is not needed** for this criterion: the discriminant replaces the orbit size.
- **Framing.** Milne's report (Hexagon 2611.00244v1, Thm 3.1) makes Tate a theorem at good reductions of CM points, so
  Q01(iv) is a uniform-degree version of a known Tate theorem.

**Gates left, in order.**
1. The detector at one relative-Weyl special point of large discriminant, i.e. the first open family of Paper A
   (l.3339-3343).
2. An explicit bound for H(D). It is effective in principle from explicit Chow and Hilbert parameter spaces (FGA 221;
   Kollár I.3), but not computed.
3. The size of Jaswal's constant, which is exponential in a power of its degree argument (his Remark 8.2).
4. The comparison between Paper A's embedding degree and the Baily-Borel degree.
5. The inputs' status: Jaswal is AI-produced with no human understanding declared, and Cureton-Thorner is unrefereed but
   Lean-formalized. 70d should ask for a check of Jaswal's Thm 1.1(ii) for maximal special points of dimension zero.

## 5. Proposals, and where the main session routed them

1. **Koiran's Nullstellensatz theorem without GRH** (map NK-1): being checked by a25c2acb, per the main session.
2. **The half-plane algorithmic table** (map NK-3): to a later H29 note.
3. **THETA3-C32 at index 24** (map NK-4): to the 70d updater.
4. **Anderson-Ihara on single eigenspaces** (map L22): to NIGHT_AFTER_ALPOGE Part C when that is built.

No other new prompt is proposed: the rework of 68 takes the Connes and Q(√−3) findings.

## 6. Left alone

- **Prompt 70d:** the geometry mapper's to change.
- **Prompts 69 and 97:** sent and running. My findings for them, the register reading and the half-plane status of
  MOONSHINE Q1, are for their intakes.

# Prompt 70d_HODGE_EFFECTIVE: updated with the pile's findings (24 Nov 2026)

By Claude Opus 5.5 at effort max (the geometry connection-map agent), for the main session 329fb1e6 (Claude Opus 5.5 at
effort max), following `PROMPT_UPDATE_BRIEF.md`. Work file:
`agent_notes/20261124T2142Z_Connection_map_geometry_NOTES.md`.

## State and backups

- **Not sent.** 70d is absent from `TO_SEND/PRO/SENT_PRO.tsv` and from every `SENT/` folder; 70, 70b and 70c are in `SENT/`.
- **Backups.**
  - The old send folder is in `TO_SEND/PRO/_backups_20261125/70d_HODGE_EFFECTIVE/`, identical by SHA-256:
    PROMPT.md 6c9a5198…, ZIP b88a5cf8….
  - The old spec and plan are in `pro_prompt_builds/PAPERS_20261122/specs/_backups_70d_before_pile_20261125/`.
- **Built** with `build_papers.py 70d` and **placed** with `--place 70d`.
  - New send folder: PROMPT.md 77e8d57d…, ZIP fb7f59d2…; 862 files, 18.4 MB, no ZIP inside.
- **Lints.**
  - `push_rule_pro_prompts.py --lint-math`: **PASS**. The first build failed on the word "optional", which quoted Paper
    A's section title; I rephrased it.
  - `paper_completeness_lint.py`: **PASS**.
  - The builder ran both lints, and I reran them on the placed PROMPT.md.

## Changes, with their evidence

1. **The comparison half of Q27 is now settled, and stated in the background as our deduction of 24 Nov 2026.** It
   comes from MAP_NUMBER_THEORY NK-2 and check event E07, and from §4 of `PROMPT_UPDATES/68_CONNES_AFTER_RH_UPDATE.md`.
   - André–Oort is dropped: Pila–Shankar–Tsimerman, arXiv 2109.08788.
   - Jaswal's discriminant bound replaces Scanlon's B_S(H). Jaswal, Hexagon 2611.00339v3, Thm 1.1(i)-(ii) and Cor. 1.2;
     I opened them at the statement in the number-theory mapper's download (pdf l.80-135): QRH(δ; L) is ζ_L(s) ≠ 0 for
     Re s > 1 − δ, s ≠ 1; Cor. 1.2 takes δ = 1/32 from Cureton–Thorner, and δ = 1/8 from Hu.
   - The deduction uses Paper A's own maximality step: `main.tex` l.3297-3299, Chai–Oort Lemma 6.3. I opened Paper A
     at l.3277-3283 and l.3339-3343.
   - It gives the effective forcing and the effective dichotomy.
   - H15 is not an ingredient.
   - The prompt marks the deduction as having no second reader and asks the run to check it whole.
2. **Milne's framing of Q01(iv), with its dependency.** Milne, Hexagon 2611.00244v1, 9 Nov 2026; I opened it at the
   header and at Thm 3.1, l.299: "The full Tate conjecture holds for all abelian varieties over finite fields", a report on
   OpenAI's two preprints of 6 Oct 2026.
   - (iv) is uniformity in the Tate theorem; the run is told that the degree bound is what Milne's theorem does not give.
3. **The dependency flag from my map** (MAP_GEOMETRY §3.7, TSV row "OpenAI 032").
   - Milne's Thm 3.1 and 3.5, JAC1964's Th. 4, C44_POS W06-W11 and RESEARCH_SA05's 2026-abelian rows rest on the same
     unrefereed input. In the number-theory map it is van Hoften–Sempliner, Hexagon 2610.00259, for CM Hodge; I have not
     opened that.
   - Paper A's Q01 uses published inputs only.
   - Paper C must name the input in the hypotheses of every statement that uses it.
4. **The main question is moved to the real gate,** in the order of the number-theory list. The PUSH line and item 1 now
   ask for the detector of degree ≤ D at one relative-Weyl special point with d_{L_x} > c(1/32, H(D), [F:Q]·H(D)), in the
   first open family (split eightfolds over a field other than Q(√−3), Paper A l.3339-3343, Gaussian first).
   - Paper A's own gate (principal Gaussian U⁴, invariant Ext² = 56) is one route.
   - E_D is to be written explicitly, as before.
   - The families of 48 and 36, where detectors are known, become the calibration: the criterion must reproduce them
     with every constant computed.
5. **Alpöge's theorem keeps its place** in the title and the "Why" section. Both are deductions I added, immediate from
   the definitions:
   - for abelian L, ζ_L is a product of Dirichlet L-functions, so Alpöge's theorem gives QRH(1/2; L), the best δ in
     Jaswal's constant;
   - it gives explicit least completely split primes for the one-prime test.
6. **The one-prime test is now its own item (2).**
   - The flat-detector witness of Q27 is used at the reduction of a CM point at a completely split ordinary prime.
   - The least such prime comes from Alpöge's theorem for abelian L_x, and from Hu's effective Chebotarev (Hexagon
     2610.00216, Cor. 9.6, per MAP_NUMBER_THEORY) otherwise.
   - Flatness of H_D → S is to be proved.
   - The rule against carrying bounds to inert primes is kept.
7. **The constants (item 3), as the number-theory list's gates 2-5:**
   - an explicit H(D), with Paper A's "closedness supplies no growth estimate" (l.3302) cited;
   - Paper A's projective-embedding degree against Jaswal's Baily–Borel degree;
   - Jaswal's c for δ = 1/32, 1/8 and 1/2, with his Remark 8.2;
   - a whole check of Jaswal's Thm 1.1(ii) at the step used, since the paper is AI-produced and declares no human
     understanding.
8. **THETA3 against Paper A (item 4).** From MAP_NUMBER_THEORY NK-4: C′_A = u_*(B₀ − B₂), ∫w₀² = 128,
   cl(C_A) = 24·cl(C′_A). The degree deg_θ u_*(B_j), via u*θ = 7x − δ/2 on Sym⁴H, is to be compared with Paper A's
   degree-48 detector on principal Gaussian fourfolds. That detector is in 70d's scope, so the item is in.
9. **The H15 item (now 5) is kept, with a different purpose.** The criterion no longer needs it; the run proves the
   Hodge-type extension and states the orbit form of the criterion it gives with Jaswal's bound. The coordinator's message
   called this "an option"; I made it a task, without any way out.
10. **Two Paper A fixes are named for its changes file** (item 9 and "The paper"):
    - drop André–Oort;
    - Q28: the Eisenstein eightfold input is proved without Severn in HODGE_DIVISION run A's `g34_section.tex`. This is
      the HODGE cluster's "Q28 against H19" problem (HODGE.md, HODGE_FINISH section 7), so the file is now attached.
11. **Items kept unchanged** (renumbered 6-9): detectors at the central point (Kudla–Millson / Rallis); the ghost rate; the
    Mumford block (Q08); the Schoen 2007 locator; the half-twist remark.

## New attachments (plan.json)

- `outside/jaswal_2611.00339v3/` (main.tex, jaswal.sty, refs.bib), `outside/milne_2611.00244v1/` (HTS.tex, defa.tex,
  HTS.bib, cbe.bst) and `outside/cureton_thorner_2610.00200v2/` (DedekindZeta.tex).
  - These are the LaTeX sources from `https://hexagonmath.org/src/<id>`, downloaded 24 Nov 2026 into
    `PROMPT_UPDATES/70d_sources/`, with only the TeX-family files kept.
  - SHA-256 of the archives: 2611.00339v3 620c8afd…, 2611.00244v1 5133df43…, 2610.00200v2 ef0ef5c8….
- `literature/LIT_Pila_Shankar_Tsimerman_Andre_Oort/` (arXiv e-print 2109.08788, through the builder).
- `ours/maps/` (MAP_NUMBER_THEORY.md with its check events, MAP_GEOMETRY.md).
- `ours/theta3/THETA3.tex` (THETA3 checkpoint 07).
- `ours/hodge_division/g34_section.tex` (HODGE_DIVISION checkpoint 34).
- No PDF was added; every new source has LaTeX.

## What stays

- The main questions, now with the detector gate first.
- The push paragraph (the PUSH line in the template).
- The three-hour ledger check, the checkpoint rules and CHECK_EVENTS.tsv: these are template text, unchanged.
- No minimum, way out or cheaper alternative was added. The lint passes, and I read the new text for them.

## Proposals

1. **NK3, the shift law of the inertia index:** a follow-up message to the running POLISH_CRISTAUX merge thread
   (prompt 92c, last capture cp34, 24 Nov 21:41 UTC); if that thread is unreachable, a short successor prompt after its
   final.
   - *Main question:* prove ν_min(p, (p−1)p^v k, 2) = v + ⌈(1 + log_p((p−1)k))/2⌉ for p ≥ 5 and p ∤ k.
   - *Why it matters:* it closes the merge run's gate "multipliers beyond p³+p²+p+1" in one statement. At v = 0 that gate
     is already closed by thread A's `thm:complete-prime-index`.
   - *What exists:* the bands up to p³+p²+p+1 for every v; `thm:first-wild-general`; `thm:wild-bands-exact`; and the
     canonical-iteration mechanism, which loses one torsion level per step.
   - *First open case:* v ≥ 1 and k ∈ [p³+p²+p+2, p⁴+p³+p²+p+1], with predicted value v+3.
   - *Inputs:* POLISH_CRISTAUX cp33/cp34 Paper 2 (`paper.tex` l.68-140, 6786-6940); MAP_GEOMETRY NK3.
   - No waiting prompt covers POLISH_CRISTAUX.
2. **NK4, cote 133 over orders:** a new prompt, or Part A' of the never-started Parts B/C of NIGHT_GROTHENDIECK_QUESTIONS
   (prompt 76, sent; AG_POLISH asks for a separate prompt for Parts B and C).
   - *Main question:* for which orders O of number fields is Φ_O an isomorphism? The conjecture is: exactly the maximal
     orders of class number one.
   - *What exists:*
     - SA17 `C:regular-coherent-criterion` for regular coherent rings;
     - NGQ `thm:singular-distinguished-monic`, checked by a0805369 (Claude Opus 5.5 at effort high), and the curvilinear
       classification;
     - MAP_GEOMETRY NK4, which proves the conjecture for every order of a quadratic field by a localization lemma.
   - *Open:*
     - singular primes whose completion is not curvilinear mod p (edim ≥ 2);
     - the semilocal-completion step for monogenic orders whose singular completion is not a domain;
     - non-monogenic orders.
   - *Inputs:* NGQ cp13 `papers/A133_lattices/`; SA17 `sections/C_finish_regular_coherent.tex`; MAP_GEOMETRY NK4.
   - No waiting prompt takes cote 133.
3. **The other new-knowledge items of my map**: none needs a prompt of its own now.
   - NK1 (very ample Kodaira failure in every characteristic) is a decision for the P90a v2 note.
   - NK2 (s_J) can go into POLISH_ALGEBRAIC_GEOMETRY Paper 5's v2 when that run is finished or followed up.
   - NK5 (Int(R)) can go into S20 v2.

## Left alone

- No other waiting prompt was changed: 68, 94, 95 and 96 belong to other mappers, and 78 is Codex's.

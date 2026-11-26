# RECORDS: P90a, a very ample counterexample to Kodaira vanishing on a surface

Editor: Claude Opus 5.5 at effort high (agent a018e2d2), 23 Nov 2026. Note: `p90a_note.tex` / `p90a_note.pdf`
(9 pages; three pdflatex passes; 0 overfull boxes; 1 underfull notice, badness 2435, in the method paragraph, with no
visible defect).
- PDF SHA-256 `5e7eeb02b2064887c8492a3ad0e796315243e4468485f8af6899299adef00a3c`.
- TeX SHA-256 `8aa7a88a0898c4ac5cabbe30c32a9124582e9ec09154794385ef1310084d669d`.

All 9 pages were rendered at 80 dpi and read by me; page 9 was read again after the last edit.

## 1. Source of the result

The result is a section of Paper 2 of the run POLISH_ALGEBRAIC_GEOMETRY by GPT-6 Astra (ChatGPT Pro mode), checkpoint
12 (23 Nov 2026, 10:00 UTC), `workbench/papers/paper_02/main.tex`, lines 151–322. Its theorem is Theorem 1.6 of that
paper. It goes back to SA14_SA19 A3 (`certify_A3.py`).

## 2. Literature, with locators

Each entry gives what was read at the source by me today (S), or what is taken from the run's records (R) or from
memory (M).

| Source | Locator | How read | Bearing |
|---|---|---|---|
| M. Raynaud, *Contre-exemple au « vanishing theorem » en caractéristique p>0*, C. P. Ramanujam – A Tribute, TIFR Studies 8, Springer 1978, 273–278. PDF https://mathweb.tifr.res.in/Documents/Publications/Studies/CP-Ramanujam-A-Tribute.pdf, SHA-256 a1befd2884bd9619aedf30c82ddd492bf61e56c0e2bcfa1ec0492c775b480072, physical pp. 329–335 | p. 273 (statement); §1 Tango; §2 the surface; §3 Remarques 1–4, pp. 277–278 | S | Remarque 3, p. 278: p=2, h=8, N=O_C(2∞), I=O_X(E)⊗N is generated outside E. Question: « Peut-on contre-exempler le théorème de Kodaira avec un faisceau ample, engendré par ses sections, voire très ample ? » Remarque 1: in char 2 the surface is quasi-elliptic, b₂=2. **This is the question answered.** |
| N. Lauritzen, A. P. Rao, *Elementary counterexamples to Kodaira vanishing in prime characteristic*, arXiv:alg-geom/9604012 (Proc. Indian Acad. Sci. Math. Sci. 107 (1997) 21–25 (M)) | pp. 1–2, references | S | Restates Raynaud's two questions. Lauritzen [4][5] answered both by modular representation theory. Their examples are of dimension ≥6 (3n−3, n≥3), with H⁵(L⁻¹)≠0. p. 2: smaller dimension wanted, and the failure is not inherited by hyperplane sections. |
| N. Lauritzen, *Embeddings of homogeneous spaces in prime characteristics*, Amer. J. Math. 118 (1996) (pages M); arXiv:alg-geom/9502016 (R) | — | not opened (cited via Lauritzen–Rao [4]) | Earlier very ample answer, on homogeneous spaces. |
| S. Mukai, *Counterexamples to Kodaira's vanishing and Yau's inequality in positive characteristics*, RIMS-1736 (Dec 2011); Kyoto J. Math. 53 (2013) 515–532 (M). PDF SHA-256 eced1e8f3c08bc31ab59cad86d1dc532d1ff44752733f3f5591776adfc20e67a | Thm 2, Thm 3, remark on p. 2 | S (pp. 1–3) | Thm 2: ample counterexamples in every dimension n≥2. Thm 3: vanishing for nef and big bundles holds on surfaces not of general type and not quasi-elliptic (p=2,3). p. 2: the failure survives separable covers of degree prime to p, since L⁻¹ is a direct summand. **Credited for the direct-summand step.** No very ample statement. |
| T. Ekedahl, *Canonical models of surfaces of general type in positive characteristic*, Publ. Math. IHES 67 (1988) 97–144. PDF (Numdam) SHA-256 0e53d89911bd563cdc5e8a38abc47dc4e990a75e77cbd05055812f6d63b30776 | Main theorem, p. 97; introduction, p. 99 (Thm II.1.3 and its corollary) | S (pp. 97–100) | H¹(ω^{−i})=0 for minimal surfaces of general type, except i=1, p=2, χ=1. Kodaira vanishing holds on non-general-type surfaces, except essentially Raynaud's examples. Context only. |
| F. Bernasconi, D. Valloni, *Brauer–Manin obstruction from failure of Kodaira vanishing in positive characteristic*, arXiv:2605.28278 (27 May 2026) | Thm 1.2; Props 3.11(1), 3.13, 3.14 | S (arXiv HTML) | A^{⊗p} is globally generated and separates points, restricting to a purely inseparable map of degree p on fibres (3.14 assumes p>2). The nonvanishing concerns A only. No very ampleness, no mention of Raynaud's question. **Not superseding; credited in one sentence.** |
| B. Bhatt, *Derived splinters in positive characteristic*, Compos. Math. 148 (2012) 1757–1786 | proof of Prop. 7.2, p. 1771 | R (the run opened the Cambridge PDF) | Roots of a basis, used for global generation. Credited for the covering operation. |
| X. Zheng, *Counterexamples of Kodaira vanishing for smooth surfaces of general type in positive characteristic*, JPAA 221 (2017) 2431–2444; arXiv:1509.04993 | — | R | Generalizes Raynaud's surfaces (ample). Context. |
| Y. Zhang, *Strong non-vanishing … on n-Raynaud surfaces*, arXiv:2210.00967 (v4, Jul 2025) | abstract | S (abstract) | Fujita-type pathologies; no very ample claim. Not cited in the note. |
| E. Arvidsson, *On the Kodaira vanishing theorem for log del Pezzo surfaces in positive characteristic*, arXiv:2002.00679 | abstract | S (abstract) | Big and nef bundles on log del Pezzo surfaces; not relevant. Not cited. |
| T. Murayama, arXiv:1905.03839 (thesis) | abstract | S (abstract) | No bearing. Not cited. |
| Bloch–Gieseker / Kummer covers (e.g. Lazarsfeld, *Positivity* I, Thm 4.1.10) | — | M | Standard covering construction. The note mentions it without a citation; the locator is from memory and was not opened. |
| Hartshorne, *Algebraic Geometry*, II.8.18 (Bertini) | — | M | Standard. |
| Ajit–Lee draft (ChatGPT and Claude), cited in the run's Paper 2 | Thm A, p. 2 (R) | not opened | According to the run it concerns +-regular rational surfaces with nef, non-big −K: a different failure. Left out of the note because it was not opened. |
| **Hexagon**, hexagonmath.org, 23 Nov 2026 ~13:40 UTC | front page (2611.00819–00829); searches "Kodaira" (1 hit, 2611.00330, unrelated: Kodaira–Parshin), "vanishing" (58; none relevant; nearest 2610.00447, point separation for adjoint bundles in char 0), "Raynaud" (0) | S | Nothing neighbouring. |
| Web searches (standard and extended) for very ample Kodaira-vanishing counterexamples on surfaces | — | S | No surface example found. |

**Verdict.** No very ample counterexample to Kodaira vanishing on a surface was found in print or on Hexagon.
Raynaud's question for globally generated bundles also appears not to have been answered on surfaces. The note is
**clear**.

**Gaps that remain readings:** none are open. Raynaud's original, the decisive source, was read in full. Lauritzen
1996 was not opened; its role (higher-dimensional homogeneous spaces) is stated as Lauritzen–Rao state it.

## 3. Checks the result has received

| Statement | Date | Who | Type | Outcome |
|---|---|---|---|---|
| A3 (surface, invariants 562, 1, 565) | 20–23 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode), the runs RESEARCH_SA14_SA19 and POLISH_ALGEBRAIC_GEOMETRY | computation or formal certificate | `certify_A3.py` rerun; an independent principal-parts program gives 210/186/160 |
| A3 | 23 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode), separate instance, POLISH_ALGEBRAIC_GEOMETRY | independent re-proof (same model, from the existence statement) | complete; it caught a false relative-duality display (Sym^r(E^∨) in place of (Sym^r E)^∨), fixed before cp12 without changing the theorem |
| A3 | 23 Nov 2026 | Claude Opus 5.5 at effort high (cp12 intake) | targeted proof check | confirmed; every invariant recomputed by hand (6, 1, 9, 210/186/160=556, 562, 1, 565) |
| Note, Thm 2 (roots of a general basis, any dimension and characteristic) | 23 Nov 2026 | Claude Opus 5.5 at effort high (editor) | targeted proof check | proved in the note §3; generalizes the run's special case; no fault |
| Note, Thm 1 over **every** algebraically closed k of char 2 (in place of the run's "there exists k", k an algebraic closure of 𝔽₂(λ_ij)) | 23 Nov 2026 | Claude Opus 5.5 at effort high (editor) | targeted proof check (of a strengthened statement; nothing refuted) | the run's statement stays true. The strengthening follows from Bertini over an algebraically closed field: finitely many nonempty open conditions, and rational points of a nonempty open of an affine space over an infinite field. Consequence: Y is defined over a finite field |
| Note, Prop. 6 (very ampleness of Q⁹), chart argument | 23 Nov 2026 | Claude Opus 5.5 at effort high (editor) | targeted proof check | the run's local sketch is replaced by the argument on D(b) (ψ_*O_S is generated by H⁰(D(b),M), which is generated by σ/b); no statement change |
| Note, Prop. 5 (global generation of Q; with a=1, Raynaud's own bundle, only the invariant summand has sections) | 23 Nov 2026 | Claude Opus 5.5 at effort high (editor) | targeted proof check | confirmed from Lemma 4 |

No human has checked the result. There is **no independent re-proof by a model family other than GPT**. If the user
wants one before posting, a statement-only re-proof of Theorem 2 together with Prop. 5 is the natural target; it is
short.

## 4. Whom to write to when it is posted (send nothing now)

- **Niels Lauritzen** (Aarhus) and **A. Prabhakar Rao** (UMSL): their paper asked for lower-dimensional very ample
  examples (p. 2).
- **Shigeru Mukai** (RIMS, emeritus): his p. 2 direct-summand remark is used and credited.
- **Fabio Bernasconi and Domenico Valloni**: the nearest recent work, on Raynaud surfaces; their result is credited.
- **Xudong Zheng**: Raynaud-type surfaces.
- Optional: **Christian Liedtke**, author of the survey on surfaces in positive characteristic. A separate draft about
  his table, from the cp12 intake, is waiting.
- Raynaud (d. 2018) and Ekedahl (d. 2011) cannot be written to.

## 5. What is left before posting

1. The user's read and word.
2. The author line (left as "Entered at deposit").
3. The workbench link resolves (`schemes-and-moduli-workbench`), and the A3 programs are deposited there.
4. Optional: an independent re-proof by a model of another family (see §3).

## Main-session reading, 23 Nov 2026 13:50 UTC

Read in full by the main session 329fb1e6 (Claude Opus 5.5 at effort max), every step followed and every number recomputed by hand: the curve (genus 7, div t, the identity x + t^-2 = t^-1 x^-7, dt = x^6 dx), the bundle E and its gluing, C'' and its smoothness, the triple cover, the floor lemma, Proposition 5 (sections 6, generation along T, (a_j), R^1 by relative duality, h^1(Q^-1) = 1, vanishing for n >= 2, h^1(O_S) = 9), Proposition (Q^9 very ample, 210 + 186 + 160 = 556), Theorem 2 (smoothness, connectedness, the chart argument for very ampleness), and the count 562 / 1 / 565. Type: targeted proof check. Outcome: confirmed; no gap.

Fixes made by the main session: (1) the number of sections in Theorem 2 and Section 6 is now l (it was N, which also names the line bundle O_C(2 inf)); (2) the sentence on references cited from memory is replaced: the journal data of Lauritzen (Amer. J. Math. 118 (1996) 377-387), Lauritzen-Rao (Proc. Indian Acad. Sci. Math. Sci. 107 (1997) 21-25) and Mukai (Kyoto J. Math. 53(2) (2013)) were checked against bibliographic records (MR 1385284, MR 1453823, DOI 10.1215/21562261-2081279). Previous text kept as p90a_note_before_main_fixes_20261123.tex. Rebuilt (pdflatex, three passes): 9 pages, no overfull box.

Novelty: two web searches (23 Nov) found no very ample counterexample on a surface; the known very ample ones are of dimension >= 6.

Before posting: view every rendered page; the deposit sheet; the user's word.

## 6. Addendum, 23 Nov 2026 ~19:15 UTC: Kweon's question, and a second version (not posted)

By Claude Opus 5.5 at effort high (agent a018e2d2), during the evening intake of POLISH_ALGEBRAIC_GEOMETRY
checkpoints 16–20. The run's Paper 2 at checkpoint 20 cites Kweon. I read the source:
- H. J. Kweon, *Bounds on the torsion subgroup schemes of Néron–Severi group schemes*, Adv. Math. 409 (2022) 108687;
  arXiv:2008.01908v2 (27 Sep 2021), SHA-256 6b51c49d120ff37682ddacc8e40e3ae1a64bf129b2d886476be8122b7970d9f9;
- §7, pp. 17–19, read at the source (S).

What Kweon proves and asks:
- **Thm 7.2 (pp. 17–18):** for a smooth hyperplane section H of X with dim X ≥ 2, ker(Pic X → Pic H) is a finite
  commutative group scheme with connected Cartier dual.
- **Thm 7.4:** Langer, under a W₂-lift, makes it a closed embedding.
- **Thm 7.6 (p. 18):** for a smooth ample effective D, the restriction of homomorphisms from α_p is injective iff
  H¹(X, O(−D)) = 0.
- **p. 18:** he "conjectures that Pic X → Pic H can fail to be a closed embedding if char k = p > 0, because of the
  failure of the Kodaira vanishing theorem".
- **p. 19:** he knows no very ample D with H¹(X, O_X(−D)) ≠ 0.
- **Question 7.7 (p. 19):** is Pic X → Pic H always injective? always a closed embedding?

**Consequence (new Corollary 2 in v2), checked by me.** On P90a's Y, for every smooth connected H ∈ |L|, the
restriction Pic_Y → Pic_H is not a closed immersion:
- a closed immersion is injective on tangent spaces, and the tangent kernel is H¹(L⁻¹) ≠ 0;
- by Kweon's Thm 7.6 there is moreover a nonzero α_p → Pic_Y that dies on H.

So the closed-embedding half of Kweon's Q7.7 has a negative answer (dimension 2), and his p. 18 expectation is
confirmed. Injectivity on geometric points is untouched. The run's Paper 2 (cp20, Section 1) makes the same
observation about Q7.7.

**Second version.** `p90a_note_v2.tex` / `p90a_note_v2.pdf`: 10 pages, three passes, 0 overfull boxes.
- PDF SHA-256 e0e6ff278ec43a540ca335a746ba4ff7e5ac9467dceefab9ef86fd86e9a59d7b.
- Pages 1, 2, 9 and 10 were rendered and read by me. Pages 3–8 carry the v1 text unchanged.
- Changes: one abstract sentence; a Kweon paragraph in §1; Corollary 2 with its proof; the "Picard kernels" open item
  tied to Q7.7(i); the method note; the bibliography entry [6].

v2 is **not posted**. Whether to post it as v2 of hexagon:2611.00936 is for the main session and the user.

**Whom to write to (add):** Hyuk Jun Kweon, whose Q7.7 and p. 19 remark this answers.

**Note added 23 Nov ~23:20 UTC (cp24 intake).** The run's correction dossier now holds:
- a characteristic-5 counterexample to Zheng's arXiv v1 Corollary 4.4;
- two literal corrections to Mukai RIMS-1736, pp. 15–16.

Neither touches what this note cites (Zheng as context; Mukai Thms 2–3 and the p. 2 remark). Both are unchecked by
me. When writing to Zheng or Mukai, the main session should decide whether to include them after a check.

**E-mail drafts added 23 Nov ~23:59 UTC (Claude Opus 5.5 at effort high), all pending the run's final and not sent:**
- `EMAIL_DRAFT_Zheng_20261123.md`: the P90a notice plus the characteristic-5 counterexample to arXiv v1 Cor. 4.4;
- `EMAIL_DRAFT_Mukai_20261123.md`: the P90a notice plus the two RIMS-1736 misprints;
- `EMAIL_DRAFT_Esnault_20261123.md`: two points on math/0608203v1, Lemma 2.2 and Prop. 2.5.

All three corrections were checked in full; the check events are in the cp24 CHECK_EVENTS tsv.

**Note 24 Nov 2026 (cp35 intake, Claude Opus 5.5 at effort high).** The run's dossier records a qualification to our
posted Theorem 2 (v1):
- **The issue.** Connectedness of the root cover needs dim X > 0. For X = Spec k, Q = O_X and m = 3, the cover is three
  points.
- **Checked by me.** The proof step H⁰(X, Q⁻ʳ) = 0 needs positive dimension.
- **v2 is corrected.** In Theorem 3 (the old Theorem 2) and its proof: PDF SHA-256
  159f0c94073f1a65f87264f522f5962283ad04ffe2e88e7faec457a19098d936, 10 pages, 0 overfull boxes.
- **The rest stands.** Theorem 1 and every surface statement are unaffected.
- **The run's comparison** confirms our construction and invariants against its Paper 2 and makes no priority claim.
  Paper 2 now cites hexagon:2611.00936v1, Theorem 1.

**Esnault draft.** It gained a third point (Remark 2.3(2): the étale locus is empty when p | n), checked by me.

## Version 2 committed (24 Nov 2026, 10:56 UTC)
Main session 329fb1e6 (Claude Opus 5.5 at effort max), under the standing rule hexagon-post-when-sure, every criterion
stated: (1) useful: it answers the second part of Kweon's Question 7.7 (Adv. Math. 409, 2022) negatively for surfaces
and repairs version 1's Theorem 2, which needs positive dimension (found by a018e2d2 at POLISH_AG cp35); (2) the format
of version 1; (3) background: Kweon §7 read at the source by a018e2d2, Hexagon search "Kweon" on 24 Nov: 0 works;
(4) mathematics: the corollary (tangent-space kernel H^1(Y, L^-1) != 0 against injectivity of closed immersions on
tangent spaces; the alpha_p statement by Kweon's Theorem 7.6) and the positive-dimension fix checked by a018e2d2 and by
the main session; (5) every page of p90a_note_v2.pdf (10 pp., 0 overfull) read by the main session.
- Hexagon: revise -> draft 002ac664; v1's staged source removed; v2 uploaded as kodaira_very_ample_surface.tex;
  metadata HEXAGON_METADATA_WB0003_v2.json (the v2 abstract; the change note at the head of comments; author fields kept);
  verify-meta same (formalizations [] by the server); preview HEXAGON_PREVIEW_WB0003_v2.pdf word-for-word identical to
  the local build (5,566 words, 10 pp.).
- Committed 24 Nov 10:56:23 UTC: hexagon:2611.00936v2, sourceTreeSha256 3c86e737e3b17e8f....

## Version 3 committed (24 Nov 2026, 23:01 UTC)
Main session 329fb1e6 (Claude Opus 5.5 at effort max), at the user's word of 24 Nov ~22:0x UTC ([the user's words, omitted]; [the user's words, omitted]), under hexagon-post-when-sure, every criterion stated:
(1) useful: it answers Raynaud's 1978 question on surfaces in every positive characteristic, where v2 listed odd
characteristic as open; (2) the format of v2; (3) background: the 24 Nov topicality pass and the geometry map
(MAP_GEOMETRY.md NK1) found no outside result; (4) mathematics: POLISH_CRISTAUX Paper 1 Thm 1.2 (GPT-6 Astra, ChatGPT Pro
mode), targeted check by a512cf71 (Claude Opus 5.5 at effort max, cp12), full step-by-step check for every p by a018e2d2
(Claude Opus 5.5 at effort high, 24 Nov, check events in the cp35 CHECK_EVENTS tsv), who wrote Section 7; the main session
read Section 7 step by step (genus 2g-2 = p d_0; d_0 = p(p-2)(p+1) for odd p; the eigensheaf formula; f_*Q = N + N^{p+1};
the summand (Sym^{p-2}V)^dual (x) T^{p-2} containing O_C; qn - (2g+1) = d_0 - 3 > 0); (5) every page of p90a_note_v3.pdf
(12 pp., 0 overfull, 0 undefined) read by the main session; Raynaud's quotation checked in the text layer.
- Hexagon: revise -> draft 52fc7f87-fda0-4716-aca6-661711f7e08c; v2's staged source (upload fd770ba5) removed; v3
  uploaded as kodaira_very_ample_surface.tex (v3_upload/, = p90a_note_v3.tex); metadata HEXAGON_METADATA_WB0003_v3.json
  (build_meta_v3.py: v3 title and abstract; the v3 change note at the head of comments, 1,979 chars; a version-3
  paragraph in provenance; tags at Hexagon's maximum of 10); patch-keep-author HTTP 200; verify-meta same (formalizations
  [] by the server); preview succeeded 23:01:29 UTC, HEXAGON_PREVIEW_WB0003_v3.pdf identical in text to the local build on
  all 12 pages (5,741 words).
- Committed 24 Nov 23:01:52 UTC: hexagon:2611.00936v3, sourceTreeSha256 ace43030...8bf064. State backups:
  HEXAGON_STATE_WB0003_v2_published_backup_20261124.json, HEXAGON_STATE_WB0003_v3_before_commit.json.
- Not yet done: the WB-0003 page of mathematics-workbenches does not list version 3's checks.

# HNAM note: records (not for posting)

Note: `hnam_note.tex` / `hnam_note.pdf`, "Hilbert's Nullstellensatz is in AM from a zero-free half-plane of Dedekind
zeta functions, after Koiran". Written 24 Nov 2026 (22:50-23:55 UTC) by Claude Fable 5.2 at effort max (agent
ae2754d9739e7e166) on the brief of the main session 329fb1e6 (Claude Opus 5.5 at effort max). **Not posted.** Next:
recheck by a25c2acbb3a6f11f7 (Claude Opus 5.5 at effort high), then the main session reads it and posts.

## 1. What the note is, in our terms

- The main theorem is already in our posted paper hexagon:2611.00987v1 as **Proposition 17.2** (p. 59, label
  `prop:fixed-strip-hn-am`, source lines 4730-4912) and in its Table 1. The note cites it at version 1 and says so in
  the abstract, in §1.4 and in the note on method.
- New in the note: the derivation from Hu's Cor. 9.6 (Prop. 3.1(a), Prop. 3.2), the explicit threshold x₀ (Theorem A,
  Theorem 4.1), Corollary D with the place where each source uses GRH, and the relation to Andrews-Garg-Schost.
- Crosswalk (internal ids stay out of the note): Theorem A, B, Cor. C = NK-1.1 of `MAP_NUMBER_THEORY.md`; Cor. D(1)-(3)
  = NK-1.2-1.4; Cor. D(4) = CX-K02 and D(5) = CX-K05 of CX_GRH (`CX_GRH.tex` l.433-478 and 540-638), as
  `CHECK_HN_AM_20261124.md` states them. CX-K06 and the further GCT V transfers are left out.

## 2. Three things for the recheck and for the main session

1. **Koiran's Theorem 9 for a non-monic f.** As printed it has no term for the leading coefficient a. For p dividing a
   but not Δ the count W(p) differs from the number of degree-one primes, so the bound needs + (2n+1) log₂|aΔ| (Prop.
   3.2(1)). Harmless in Koiran's application. Our 67c paper makes the same point (l.4720-4722). The check file's
   inequality "(n+1) log|Δ|" is the monic case.
2. **x₀.** With (P_η): |π_K(x) − Li x| ≤ C₀(log d_K + n_K)x^η, the note proves π_S(x) ≥ x/(2M log x) − 19C₀M³x^η for
   x ≥ 4 (Theorem 4.1), and π_S(x) ≥ B for all x ≥ x₀ = ⌈(52C₀M⁴/(1−η))^{2/(1−η)}⌉, M = L·2^{(n log₂σ)^c}. With Hu and
   η = 8/9: x₀ = ⌈(468C₀M⁴)^{18}⌉. The exponent is 2/(1−η), twice the check file's 1/(1−θ), because log x is absorbed
   crudely (log x ≤ x^δ/(eδ), δ = (1−η)/2). Every constant is derived in the proofs of Theorem 4.1 and Theorem A.
3. **A sentence to add after the recheck.** The note on method does not yet say that the text was rechecked. If the
   recheck passes, add after "...as quoted in [17].": "Claude Opus 5.5 at effort high then checked this text."

## 3. Sources: what was opened, where (by Claude Fable 5.2 at effort max unless said)

| Source | Opened at | Copy |
|---|---|---|
| Koiran, J. Complexity 12 (1996) | whole text; pp. 275-276, 281-282 as page images | scratchpad `ntmap/dl/koiran/` |
| Koiran, DIMACS TR 96-27 | abstract, §§1-5 (Thm 1, Thm 2 with proof, Thms 4, 5, 7, 8, 9, Cor. 1) | scratchpad `hnam_dl/koiran_ext/` (from his page) |
| Koiran, Erratum, 8 Aug 1997 | whole (page image) | scratchpad `hnam_dl/koiran_err/` |
| Koiran, FOCS 1997 (author's version) | abstract, §1, p. 6 (Thm 4.1), p. 9 (Thm 5.8) | scratchpad `hnam_dl/koiran_dim/` |
| Hu, hexagon:2610.00216v2 | abstract, Thm 1.1, Thm 1.2, Cor. 9.6 with proof, "AI provenance" | scratchpad `ntmap/dl/hu216.*` |
| Cureton-Thorner, hexagon:2610.00200v2 | abstract, §1 to Cor. 1.2, §15 | scratchpad `ntmap/dl/ct200.*` |
| Liu, hexagon:2611.00741v1 | abstract, Thm 7.21 (statement) | scratchpad `ntmap/dl/liu741.*` |
| OpenAI, Primitive roots (4 Oct 2026) | introduction, Thm 1.2 | scratchpad `ntmap/dl/oai/` |
| OpenAI, factorization over prime fields (4 Oct 2026) | §11 whole (Lemma 11.2 and proof) | `Codex/2026-11-22/.../inputs/OpenAI_prime_fields/` |
| Rojas, arXiv math/0301111v2 | pp. 1-7 (Thm 1, DZH, GIPIT, Thm 5; p. 7 as page image) | scratchpad `ntmap/dl/rojas/` |
| Ait El Manssour et al., arXiv 2408.13027v3 | abstract, §1, §3.3.1, §3.4 (proof of Thm 1) | same folder (`a24.*`) |
| Pak-Robichaux, arXiv 2504.03004v1 | pp. 1-5, Thm 2.1, §3.1, Lemma 3.2, Thm 3.4 with proof | same folder (`pr25.*`) |
| Pak-Robichaux, arXiv 2412.02064v3 | abstract, Thm 1.4, Thms 1.7-1.8, Lemma 1.9, §1.8 | scratchpad `hnam_dl/pr24b/` |
| Mulmuley, GCT V, arXiv 1209.5993v5 | Thm 2.10, §3 to the remarks after Thm 3.4 | scratchpad `hnam_dl/gct5/` |
| Andrews-Garg-Schost, arXiv 2602.17904v1 | abstract page; HTML §§1.1-1.2 through two fetches (summaries, not the full text) | not saved |
| hexagon:2611.00987v1 (ours) | Table 1 row, §17.2-17.3 (l.4693-4912), through `tex_read.py` only | `grh_algorithms_67c/source_v1/` |
| Lagarias-Odlyzko 1977 | **not opened**; Thm 7.1 as quoted by Rojas (Thm 5), zero count as stated in OpenAI's Lemma 11.2 proof | — |
| Boppana-Håstad-Zachos 1987 | **not opened**; as quoted by Pak-Robichaux, p. 5 | — |

Literature corpus (rule of `AGENTS_MATHEMATICS.md`): `query_corpus.py` on "Lagarias Odlyzko Chebotarev", "Koiran
Nullstellensatz", "effective Chebotarev density theorem prime ideal theorem zero-free" (24 Nov 2026): no copy of
Lagarias-Odlyzko or Koiran and nothing usable. The sources above came from the session's downloads and the authors'
pages.

Relation to arXiv 2602.17904 (opened as the brief asked): Theorem 1.1 puts HN in CH with no hypothesis, over Q,
number fields, F_q and their function fields; Theorems 1.3-1.4 give dimension and cardinality in FP^CH; §1.2 recalls
PH ⊆ CH ⊆ PSPACE (Toda). Its §1.1 cites Koiran's AM result under GRH and the HNP extension, and makes no comparison.
So AM ⊆ Π₂^P ⊆ PH ⊆ CH: our class is smaller, theirs needs no analytic input and covers positive characteristic.

## 4. The eight boxes

1. Title: names the theorem and Koiran. 2. Abstract: opens with Koiran 1996; says what is proved, what is granted
(unrefereed preprints), why it matters; ends with who produced, checked, wrote, and that no human has. 3. Theorems in
full: §1.2 (A, B, Cor. C, Cor. D). 4. Why it matters: §1.3. 5. Credit: §1.4. 6. Context: §1.5 (Andrews-Garg-Schost,
Rojas, Dirichlet RH and OpenAI's cyclotomic strip). 7. Scope: §1.6. 8. Proof overview: §1.7.

## 5. Deposit data (proposal)

- Title: as above. Subject: math.NT, cross-list math.AG (and computational complexity if Hexagon has it).
- Keywords: Hilbert's Nullstellensatz; Arthur-Merlin; polynomial hierarchy; Koiran's theorem; zero-free half-plane;
  Dedekind zeta function; effective Chebotarev; dimension problem; Schubert coefficients; Noether normalization;
  AI-generated mathematics.
- MSC: 68Q15, 11R42, 11R44, 14Q20, 13P15.
- Abstract: `ABSTRACT.txt` (the TeX abstract in plain text). Comments field: `COMMENTS_FIELD.txt`. Provenance field:
  `PROVENANCE_FIELD.txt`. Licence CC0 1.0; text origin primarily AI-generated; human understanding: none.

## 6. Whom to tell after posting (if the user agrees)

Pascal Koiran; Dean Cureton and Jesse Thorner; Boyang Hu; Baiying Liu; Rida Ait El Manssour, Nikhil Balaji, Klara
Nosan, Mahsa Shirmohammadi, James Worrell; Igor Pak and Colleen Robichaux; Ketan Mulmuley; Robert Andrews, Abhibhav
Garg, Éric Schost; J. Maurice Rojas.

## Committed (24 Nov 2026, 23:20 UTC): hexagon:2611.01018v1
Main session 329fb1e6 (Claude Opus 5.5 at effort max), under hexagon-post-when-sure, every criterion stated: (1) useful: Koiran's HN in AM without GRH, with explicit constants and the consequences (DIM, HNP, Schubert vanishing in AM cap coAM in types A-D, so not NP-hard unless PH = Sigma_2^P; Noether normalization); (2) the format of our notes; (3) background: CHECK_HN_AM_20261124.md searches (arXiv, ECCC, web, the Hexagon catalogue), the earlier statement (our 2611.00987v1 Prop. 17.2) and Andrews-Garg-Schost 2602.17904 cited; (4) mathematics: derivation by aaf57cd5 (Claude Opus 5.5 at effort max), independent check by a25c2acb (Claude Opus 5.5 at effort high), Sections 3-4 re-derived by ae2754d9 (Claude Fable 5.2 at effort max), the final text rechecked by a25c2acb (every constant recomputed); (5) every page of hnam_note.pdf (10 pp., 0 overfull, 0 undefined) read by the main session. Metadata HEXAGON_METADATA_HNAM.json (build_meta_hnam.py: comments trimmed to 1,971 characters, '25 November' corrected to the UTC date 24 November; subject cs.CC, cross-lists math.NT, math.AG); create-like from the WB-0005 draft (author block copied in memory only); source uploaded as nullstellensatz_am_half_plane.tex; verify-meta same; preview identical in text to the build on all 10 pages (5,200 words). Committed 23:20:54 UTC, sourceTreeSha256 0d693ca3...ace891f. Not yet done: a WB page in mathematics-workbenches.

## Version with the missed credits committed (25 Nov 2026, 00:33 UTC)
v1 (committed 24 Nov 23:20 UTC) was paused for corrections at the user's word ('it's still in publication, so you can hold it') before it was published: it did not cite Frei-Sofos-Widmer (arXiv:2610.18491) or Baldwin-Sivek (arXiv:2611.06705), found by a25c2acb (CHECK_LEAN_CT_AND_ZENTNER_20261124.md). v2 by ae2754d9 (Claude Fable 5.2 at effort max; v2/, make_v2.py), rechecked by a25c2acb (Claude Opus 5.5 at effort high; two corrections). Main read the v1->v2 diff (credits; Prop. 3.1(b) from FSW with L = K, C = {1}, delta = 1 - theta: c1 x^theta (log d_K/(1-theta) + n_K log x); bibliography). Metadata HEXAGON_METADATA_HNAM_v2.json (build_meta_hnam_v2.py: v2 abstract 1,955, comments 1,967, provenance with the version-2 paragraph and the corrected sentence on sources not opened). revise -> draft a643820e; v1 source (upload 2a5431b5) removed; v2 uploaded; patch-keep-author; verify-meta same; preview identical in text on all 10 pages (5,665 words). Committed 00:33:00 UTC: versionId 2611.01018v2 (the API counts the paused v1; the public number should be v1, as with Paper V), sourceTreeSha256 857d0092...499d1b.

# The GT monoid note: records (not for posting)

Note: `gt_monoid_note.tex` / `gt_monoid_note.pdf`, "The profinite Grothendieck-Teichmüller monoid is a group, on a
question of Lochak and Schneps". Written 25 Nov 2026 by Claude Fable 5.2 at effort max (the conference convener) on the
word of the main session 329fb1e6 (Claude Opus 5.5 at effort max). **Not posted.** Next, by the main session's plan:
another model checks it, then the main session reads it.

## 1. What the note is, in our terms

| In the note | In the run LM4_SUCCESSOR (`work_CE/C_further.tex`) | State |
|---|---|---|
| Theorem E(a) | C.29, l.474-506 | checked by two readers |
| Lemma 3.1; Theorem A for unit λ | C.30, l.509-579, equations (C.30.2)-(C.30.4) | checked by two readers |
| Theorem E(b); the clause "λ is a unit" of Theorem A | not in the run | **new, no second reader** |
| Proposition C (f = [x,y] in A₄; f = [x,y]² in S₃; relation (I) holds) | the run has f = [x,y]² in A₅, with no mention of (I) | **new form, no second reader** |
| Corollary D(a) | C.31's conclusion, there by braid groups and the pentagon | **new deduction, no second reader** |
| Remark 5.3 | C.31, l.606-730 | torsion argument checked by two readers; its inputs see section 3 |

Internal ids (C.29 and so on) stay out of the note.

## 2. What is new against the run, and what the next reader should attack first

1. **Theorem E(b) is the one new idea.** The run assumed λ ∈ Ẑ^× in C.30 and needed the pentagon and the whole braid
   operad (C.31) to show that an operad endomorphism has unit λ. The note gets "λ is a unit" from (I) and (II) alone:
   if p | λ, the image of φ lies in the kernel U of F̂₂ → (Z/p)², the cover has 3p boundary components, and the
   relation φ(x)φ(y)φ(z) = 1 would make ν([b₁] + [b₂] + [b₃]) vanish in H₁ of the cover, with λ = pν. **Attack this
   proof.** Points to press:
   - that φ(F) ⊂ U (it uses that U is normal and that the c_j generate; this is why the statement is for genus 0);
   - that each boundary component of the cover has degree exactly p (Lemma 2.2 with e = p);
   - that [b₁] + … + [b_m] ≠ 0 in H₁(S_U; Z) when r > m (Lemma 2.1);
   - that ν·w = 0 with w ≠ 0 integral forces ν = 0 (Ẑ is torsion-free as an abelian group, although it has zero
     divisors).
2. **Lemma 3.1 is written with relation (II) in the form of Boavida de Brito-Horel-Robertson**,
   f(z,x) z^m f(y,z) y^m f(x,y) x^m = 1. The run uses the cyclic rotation f(x,y) x^m f(z,x) z^m f(y,z) y^m = 1. They are
   conjugate. I recomputed the lemma in both forms.
3. **Theorem A does not assume f ∈ F̂₂′.** The computation never uses it.
4. **Corollary D(a).** The monoid structure is taken from the two cited definitions. The topology step: the set of
   pairs is closed in Ẑ × F̂₂, the map to Aut(F̂₂) is continuous, so the image is a closed submonoid of a profinite
   group.
5. **Session 1 of the conference said that primes p ≥ 5 were not excluded for the gentle monoid.** That remark is
   withdrawn: Theorem E(b) excludes every prime. `SESSION_1.md` carries an addendum.

## 3. Sources: what was opened, where (by Claude Fable 5.2 at effort max unless said)

| Source | Opened at | How |
|---|---|---|
| Lochak-Schneps 2006 | the definition of GT̂ in the introduction; §1, Questions 1.1 and 1.2 | text of pp. 1-5 of `MAP_GALOIS_ANABELIAN_sources/Lochak_Schneps_2006_Open_problems_GT_farb.pdf` |
| Boavida de Brito-Horel-Robertson, arXiv:1703.05143v1 | Remarks 3.7, 5.2; Definitions 6.1, 6.2, Remark 6.3; Definitions 6.9-6.12; Lemma 7.1; Definition 7.2; Proposition 7.3 with proof; Proposition 8.1; Theorem 8.4; Theorem 11.1, Corollary 11.6 | the arXiv PDF, converted to text |
| Horel, arXiv:1504.01605v2 | abstract; sketch of the proof; Remark 4.20, Proposition 4.23, Corollary 4.24; list of 5.8-5.12; Definition 7.1, Theorem 7.2, Corollary 7.3, Proposition 7.4; Theorems 8.2, 8.4, 8.13 | the arXiv PDF, converted to text |
| Fresse's survey, arXiv:1811.12536 | §2.6 | through an automatic summary of the ar5iv page, which quoted the sentence used; on 25 Nov the independent checker ae4ae3dc (Claude Opus 5.5 at effort max) found the sentence verbatim in the TeX of arXiv:1811.12536v1 |
| Dolgushev-Guynee, arXiv:2401.06870 | Definition 2.5 | not by me: by the Galois mapper (Claude Opus 5.5 at effort max) |
| Drinfeld 1990; Harbater-Schneps 2000 | Drinfeld not opened; Harbater-Schneps opened on 25 Nov by the main session 329fb1e6 at the definition of GT-hat_0 (§0.1, p. 3118, AMS PDF) | Drinfeld cited as the two operad papers cite him; the note's description of GT-hat_0 matches Harbater-Schneps |
| Ribes-Zalesskii; Serre; Chow 1948 | RZ: section titles confirmed in Springer's table of contents (§2.1 p. 19, §2.5 p. 44, §4.4 p. 132), statements not opened; Serre: numbering confirmed in the third edition (on disk), the note now cites that numbering; Chow: bibliographic data confirmed by Crossref, paper not opened (all by ae4ae3dc, 25 Nov) | standard facts |

The two arXiv PDFs were fetched on 25 Nov 2026 from arxiv.org (1504.01605: 525 KB; 1703.05143: 1.36 MB) under the
user's standing word that papers may be downloaded. They sit in the session's tool-results folder
(`<local>/.claude\projects\C--Users-user-Documents\329fb1e6-0570-47be-9060-a2a454bf3e15\tool-results\`,
`webfetch-1795564485415-xwydez.pdf` and `webfetch-1795564765088-s0zitt.pdf`). No TeX source was fetched.

**Numbering.** The note cites the two operad papers by the numbering of the arXiv versions named in the bibliography.
The published versions (Adv. Math. 321; Geom. Topol. 23) may number differently: the run's bibliography, which read
the publisher's PDF of the second, cites "Definitions 6.10-6.12, Lemma 7.1, Proposition 7.3, Definition 6.4, Propositions
7.7 and 8.1", which agrees with the arXiv numbering as far as it goes.

## 4. Sentences to change after the independent check

If the check passes:
- abstract, last sentences: "these additions have had no second reader" → name the checker;
- §1.4 "What has been checked": move Theorem E(b), the unit clause, Proposition C and Corollary D from the second
  paragraph to the first, with the checker's model and effort;
- Note on method: add the checker's sentence;
- `ABSTRACT.txt`, `COMMENTS_FIELD.txt`, `PROVENANCE_FIELD.txt`, `CHECK_EVENTS.tsv`: the same.

## 5. Literature search made, and not made

- Two web searches on 25 Nov 2026 (the monoid and its units; boundary-preserving endomorphisms of profinite free
  groups). They found the definitions (Horel; Boavida de Brito-Horel-Robertson; Fresse's survey; Dolgushev-Guynee) and
  no statement that the monoid is a group. C. D. Reid, "On endomorphisms of profinite groups" (arXiv:1112.3916), is
  general background on endomorphisms of finitely generated profinite groups and is not cited.
- The topicality pass of 24 Nov (Claude Opus 5.5 at effort high) searched Hexagon and arXiv for C.30 and C.31:
  `TOPICALITY_LONGUE_MARCHE.md` item 1.
- Searched on 25 Nov by the independent checker ae4ae3dc (three web searches: endomorphisms of profinite surface groups
  with boundary; surface words in profinite completions; inertia-preserving endomorphisms of free profinite groups):
  nothing states Theorem E(a) or E(b) (CHECK_A1_INDEPENDENT.md §5). Not searched: Wilkes; Boggi-Zalesskii;
  Hoshi-Mochizuki; Snopce-Tanushevski on test elements. The note makes no claim about Theorem E(a).
- Hexagon catalogue fetched again on 25 Nov ~00:5x UTC by the main session (API /api/v1/works, 1,530 works, newest
  published 24 Nov 17:23 UTC): no work on Question 1.1 or on the monoid; the only related hit is our own 2611.00940.

## 6. Programs

`checks/check_examples.py`, `checks/search_examples.py` (Proposition C), `checks/check_fermat_cover.py` (Theorem E(b),
the homological input), `checks/check_full_twist.py` (Remark 5.3), each with its `.out`. `checks/build_check_events.py`
writes `CHECK_EVENTS.tsv`.

## 7. Before posting (main session 329fb1e6, Claude Opus 5.5 at effort max, 25 Nov 2026)

- The independent check (ae4ae3dc) is in: every claim without a second reader holds. Its wording was applied to the
  abstract, §1.4, the Note on method, §6 item 4 and the three metadata fields; its optional clarifications too (the
  clause on the monoid of pairs in the proof of Corollary D(a), with Horel Lemma 7.5 and Proposition 7.4; the third
  edition of Serre; "has order p" in the proof of Theorem E(b)). Remark 5.3's "both readers named in Section 1.4"
  now names them. Harbater-Schneps opened at §0.1. The relations are named in the abstract (two-cycle, three-cycle,
  pentagon), as the user asked on 25 Nov.
- The main session read every proof again and every rendered page of the final build (8 pp., 0 overfull, 0 underfull,
  0 undefined; pages/p-1.png to p-8.png). Earlier build and fields: _before_main_edits_20261125/.
- The five criteria (memory hexagon-post-when-sure): (1) useful: the answer to Question 1.1 of Lochak-Schneps, with
  the operadic corollaries; (2) the format of our notes; (3) background: web searches by the writer and the checker,
  the topicality pass of 24 Nov (arXiv API, web, the Hexagon catalogue) and the Hexagon catalogue again today: no
  answer found; Fresse (2019) and Dolgushev-Guynee (2024) still treat invertibility as a condition; (4) mathematics:
  two readers on every claim used, plus the main session; (5) every page read.

## 8. Committed (25 Nov 2026, 00:55:02 UTC): hexagon:2611.01024v1

Main session 329fb1e6 (Claude Opus 5.5 at effort max). Metadata HEXAGON_METADATA_A1.json (build_meta_a1.py); create-like from the HNAM draft (author block copied in memory only); source uploaded as profinite_gt_monoid_is_a_group.tex (SHA-256 ea849add...584a, = gt_monoid_note.tex); verify-meta: every field the same (formalizations set by the server); preview HEXAGON_PREVIEW_A1.pdf identical in text to the build (8 pp., 349 lines); sourceTreeSha256 5d92bcf26e32949b4a39ade285e2740a7fde5a032e23e305c14d498e36f54dbf. State: HEXAGON_STATE_A1.json. Not yet done: a WB page and the workbench folder.

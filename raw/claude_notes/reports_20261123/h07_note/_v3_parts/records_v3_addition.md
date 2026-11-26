
## Version 3 (23 Nov 2026 12:48-13:5x UTC, editorial pass by Claude Fable 5.2 at effort max, agent a2fedc2a31aa5abb9)

Not posted. `h07_note_v3.tex` and `h07_note_v3.pdf`; `h07_note.tex` and `h07_note_v2.tex` unchanged. Review and change
log: `REVIEW_a2fedc2a_v1.md`. Built by `_v3_parts/make_v3.py` (v2 + `front_v3.tex` + `tail_v3.tex`, fifteen exact
replacements in the body). Three pdflatex passes (`build_v3_1..3.log`): 9 pages, 0 overfull, 0 underfull, 0 undefined
references. All nine pages rendered at 80 dpi and read by the editor; three sentences reworded afterwards (page 3,
page 6), page breaks unchanged, page 6 read again.

**What changed in the mathematics.**
- New: **Corollary 2** (over a finite field no closed point of the pro-cover is exceptional; Saïdi-Tamagawa's
  exceptional set is empty for the set of all primes different from p), with its proof in §4.3; the reformulation of
  Theorem 1 by covers; the remark on elliptic curves. All three are the editor's.
- Three repairs of wording in proofs, no statement changed: genus one (K' must also split the fibre above P);
  Step 5 (Lemma 1.7 cited for what it states); Step 5 (the appeal to cohomological dimension removed).

**Deposit sheet, changes.** Title unchanged. Abstract: new (in the TeX). Keywords: add "cuspidalization" (already
there), "decomposition groups", "exceptional set". Kind (SHORT_NOTE_EDITORS): **clear**.

### Check events added

| statement | date | who | type | outcome |
|---|---|---|---|---|
| Thm 3.1, Steps 1-5 (v2 text) | 2026-11-23 | Claude Fable 5.2 at effort max (agent a2fedc2a, editor) | targeted proof check | holds; Step 5 reworded twice (Lemma 1.7; cohomological dimension) |
| Sec. 4 of v3 (f.g. fields; genus >= 2, 0) | 2026-11-23 | same | targeted proof check | holds |
| Sec. 4.2 of v3 (genus one), v2 wording | 2026-11-23 | same | refuted as written (K' did not split the fibre above P, so s_P restricted to G_K' need not land in Pi_X'), refined | corrected form holds (in v3) |
| Sec. 4.2, the divisibility argument added in v2 | 2026-11-23 | same | targeted proof check | holds |
| Corollary 2 (new in v3) | 2026-11-23 | Claude Fable 5.2 at effort max (editor) | none yet: proof written by the editor, not checked by anyone else | open gate |
| Thm 1 in the form by covers; the elliptic-curve remark (new in v3) | 2026-11-23 | same | none yet (standard arguments, stated with their reason in the text) | to be read with Corollary 2 |

Related, not a check of this text: on 17 Nov 2026 two copies of this expert (Claude Fable 5.2 at effort max) read an
earlier proof of the finite-field proper case by an earlier run (`pro_intake_20261117/EXPERT_A1_SECOND_READING_PART2_20261117.md`);
no gap was found there. The correspondence of that proof's steps with this text was not re-established today.

### Literature, additions (editor, 23 Nov 2026)

| Source | Read | Bearing |
|---|---|---|
| Saïdi-Tamagawa 2009, arXiv:0801.1452 (local TeX, `Free or receipted/free/anabelian-149-20261113/arXiv_src/0801.1452/main.tex`) | at the source: Introduction (the passage on almost injectivity and on cuspidalization), Remark 1.2, Defs 1.3, 1.5, 1.6, 1.10, statements of Lemma 1.7, Prop 1.8, Cor 1.11; §2: Theorem 2.2, the fundamental extension, the cuspidally central quotient | Lemma 1.7 states: the commensurator of Z injects into G_k and equals the normalizer and the centralizer (so N(D_R) = D_R only because D_R maps onto G_L). Prop 1.8(ii), (iii) carry Corollary 2. §2 shows that the objects of Steps 1, 2, 5 are those of Mochizuki's cuspidalization |
| S. Mochizuki, Absolute anabelian cuspidalizations of proper hyperbolic curves (RIMS-1490, 2005, revised 2007; J. Math. Kyoto Univ. 47 (2007), from memory) | NOT opened; Props 1.6, 1.8, Thm 1.16 cited as Saïdi-Tamagawa §2 cite them | credit for the configuration-space construction; gate: open it once to confirm the locators and the journal reference |
| Stix, LNM 2054, chapter 7 | NOT read (no free copy) | leaves open whether the injectivity statement for prime-to-p quotients in characteristic p, or Corollary 2, is discussed there. It bears on what is known and on credit; the proof does not depend on it |
| SGA 1 (III 7.3-7.4; IX 4.10; X 3.8-3.9; XIII 2.9-2.12, 5.2), Weil I (1.5.1, Th. 1.6) | no reading on record by any checker; the locators are the run's | the note on method says so |
| Hexagon, 23 Nov 13:1x UTC | searched again: "anabelian" (only 2611.00419, Zhenyu Sun, 13 Nov, unrelated), "fundamental group section conjecture", "Tamagawa", "fundamental group curve" (0 works each) | nothing on the question |

### Whom to write to when it is posted

- Mohamed Saïdi and Akio Tamagawa, as information: the note uses their Proposition 1.8(vi) and Lemma 1.7 and concludes
  that their exceptional set is empty (Corollary 2); ask whether this is known to them.
- Jakob Stix: the question his chapter 7 would answer.
- Shinichi Mochizuki or Yuichiro Hoshi, if the user wishes: the cuspidalization credit.

### Left before posting

1. A second reader for Corollary 2 (§4.3, ten lines) and the two remarks after Theorem 1.
2. The user's look at `h07_note_v3.pdf` and their word.
3. Stix (library); Mochizuki's paper opened once; the SGA 1 and Weil I locators.

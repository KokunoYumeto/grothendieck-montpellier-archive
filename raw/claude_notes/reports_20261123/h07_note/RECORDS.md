# H07 note: build, deposit sheet, literature, checks (23 Nov 2026)

Not posted. Nothing goes to Hexagon without the user's look at the PDF and their word.

## Build

    pdflatex -interaction=nonstopmode h07_note.tex   (three passes; bibliography inline)

23 Nov 2026 02:28 UTC: 7 pages, 0 overfull boxes, 0 undefined references; every page rendered at 95 dpi and read by
Claude Opus 5.5 at effort max; four fixes from that reading (the A^1/G_m sentence, the genus-one argument, the pro-Sigma
sentence, the method note).

## Deposit sheet

- **Title:** Rational points of curves in characteristic p are separated by the prime-to-p fundamental group, on a
  question of Grothendieck
- **Subject:** math.AG (Algebraic Geometry); cross-list math.NT
- **Keywords:** anabelian geometry; section conjecture; prime-to-p fundamental group; curves over finite fields;
  Grothendieck's manuscripts; Saidi-Tamagawa exceptional set; cuspidalization; Kummer theory
- **Licence:** CC0 1.0. **Origin:** primarily AI-generated; human understanding: none.
- **The eight boxes:** title (Grothendieck's question); abstract (opens with Grothendieck and Saidi-Tamagawa, ends with
  who produced and checked it); Sec. 1.1-1.2 (question, theorem in words); 1.3 (why it matters); 1.4 (credit); 1.5
  (context); 1.6 (scope); 1.7 (proof overview).
- **Authors whose work it carries:** Mohamed Saidi and Akio Tamagawa (exceptional set; Lemma 1.7) - the board's plan:
  a note to them with the post, on the user's word; Alexander Grothendieck (the question, archive cote 149); Pierre
  Deligne (Weil I); Jakob Stix (unread monograph, the library gate).

## Literature (Claude Opus 5.5 at effort max, 23 Nov 2026; earlier search: the full intake of 22 Nov, Sec. 8)

| Source | Read | Bearing |
|---|---|---|
| Archive cote 149, scans 35-36 (our English translation, translations_en_20261117/149) | ms. pp. 17-18 | Grothendieck's question and covering form |
| Saidi-Tamagawa 2009, arXiv 0801.1452 | Intro p. 3; Rem 1.2; Defs 1.3, 1.5, 1.10; Lemma 1.7; Prop 1.8 | Step 4, Step 5; "almost injective" |
| Saidi-Tamagawa 2018, arXiv 1708.08773 | Intro pp. 4-5 | exceptional sets not even known finite for small Sigma |
| Stix, LNM 2054 | NOT read: no free copy (web search 23 Nov) | the remaining library gate |
| Hexagon (23 Nov 02:3x UTC) | searched: anabelian, section conjecture, Tamagawa, prime-to-p, fundamental group curve, exceptional set, Grothendieck section, decomposition group | nothing on the question; 2611.00419 (bounded presentations, Frobenioids) unrelated |

## Check events

| statement | date | who | type | outcome |
|---|---|---|---|---|
| Thm 2.1 Steps 1-2 (Lemma 2.2, Prop 2.3, Lemma 2.4, beta) | 2026-11-22 | Claude Opus 5.5 at effort max (agent a28ea31f) | independent re-proof | holds |
| Thm 2.1 Steps 3-5 | 2026-11-23 | Claude Opus 5.5 at effort max (session ed7922ad) | targeted proof check | holds |
| Sec. 3 (f.g. fields; genus >= 2, 0) | 2026-11-23 | same | targeted proof check | holds |
| Sec. 3 (genus one) | 2026-11-23 | same | refuted as written (translation moves the modulus), refined | corrected form holds (in the note) |

## Crosswalk

Theorem 1 = A05 (AN_GRH final, `AN_GRH.tex` lines 628-905), "A1" in our records; Hexagon board H07. Step 1 = A05 Step 1
(A05.1); Step 2 = A05 Step 2 (A05.2-A05.3); Steps 3-5 = A05 Steps 3-5 (A05.4); Section 3 = A05 Step 6. Not included: A46
(the odd cyclic cover criterion; separate gate).

## Version 2 (23 Nov 2026 12:0x UTC, main session 329fb1e6, Claude Opus 5.5 at effort max)

A full reading of h07_note.tex (every step followed) gave two edits, made in h07_note_v2.tex (h07_note.tex kept):
1. Step 4: the inverse limit is taken over the open covers V_H of C - Q (whose L-points Step 3 counts), not over the
   compactifications X_H; over X_H a compatible family could converge to a cusp above Q.
2. §3.2, genus one: the sentence "it follows that an element of G(K) divisible by every integer prime to p is torsion of
   p-power order" now carries its argument (image in E(K) is p-power torsion; p^A x = n w with w in T(K) for every n
   prime to p, using the exponents p^A of E(K)[p^inf] and N' of its prime-to-p torsion; then the case g = 0).
Statements unchanged. Built with three passes: 7 pages, 0 overfull boxes, 0 undefined references; pages 5 and 6 (the
changed passages) rendered and looked at. The Fable editorial pass (a2fedc2a) was cut by the account switch at 11:32 UTC
before it wrote anything.

## Version 3 (23 Nov 2026 12:48-13:05 UTC, editorial pass by Claude Fable 5.2 at effort max, agent a2fedc2a31aa5abb9)

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
| Hexagon, 23 Nov ~12:55 UTC | searched again: "anabelian" (only 2611.00419, Zhenyu Sun, 13 Nov, unrelated), "fundamental group section conjecture", "Tamagawa", "fundamental group curve" (0 works each) | nothing on the question |

### Whom to write to when it is posted

- Mohamed Saïdi and Akio Tamagawa, as information: the note uses their Proposition 1.8(vi) and Lemma 1.7 and concludes
  that their exceptional set is empty (Corollary 2); ask whether this is known to them.
- Jakob Stix: the question his chapter 7 would answer.
- Shinichi Mochizuki or Yuichiro Hoshi, if the user wishes: the cuspidalization credit.

### Left before posting

1. A second reader for Corollary 2 (§4.3, ten lines) and the two remarks after Theorem 1.
2. The user's look at `h07_note_v3.pdf` and their word.
3. Stix (library); Mochizuki's paper opened once; the SGA 1 and Weil I locators.

## Second reading of Corollary 2 and the remarks after Theorem 1 (main session 329fb1e6, Claude Opus 5.5 at effort max, 23 Nov 13:06 UTC)
Read in h07_note_v3.tex: the theorem, the two remarks after it, Corollary 2 and its proof (§3, last subsection). Corollary 2 holds: non-cuspidal decomposition groups meet Delta_X trivially, so D_0 maps onto G_L; in Pi_{X_L} the decomposition group of x~ equals D_0, so x_L is L-rational and the two sections have the same image; Theorem 1 over L gives x_L = x'_L, contradicting Saidi-Tamagawa Prop 1.8(iii); the 'in particular' follows since conjugate groups give D_{pi x~} = D_{x~'}. The remarks: for E the prime-to-p Kummer kernel on the finitely generated E(K) is its p-power torsion; the puncture keeps the abelianization; G_m by the Kummer argument. No gap.

| statement | date | who | type | outcome |
|---|---|---|---|---|
| Cor 2 and the remarks after Thm 1 | 2026-11-23 | Claude Opus 5.5 at effort max, main session 329fb1e6 | targeted proof check | second reader: holds (given Saidi-Tamagawa 2009 Prop 1.8(ii),(iii) as stated) |

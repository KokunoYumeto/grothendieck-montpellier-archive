# Editor's comments on `h09_note.tex` (before any change)

By Claude Fable 5.2 at effort max (agent a3ccbc11), 23 November 2026, editor under
`pro_prompt_builds\PAPERS_20261122\core\EDITOR_BRIEF.md`.

Read for this: the note's TeX in full (381 lines), with every proof followed line by line; its records (BUILD.md,
DEPOSIT_SHEET.md, LITERATURE.md, CHECK_EVENTS.tsv, CROSSWALK.tsv); "What a paper has to be" in `core\HOW.md`; the
board `field_experts\hexagon\HEXAGON_STATUS.md` (rows H01, H09, H15, H30) and the rounds of
`field_experts\HEXAGON_CANDIDATES.md` and RUNBOOK entries that mention H09. My model (versions 4 and 5 of the Deligne
note and my review of version 4) I hold from having written them; I did not reopen the files. Of the sources I have
read only Alpöge's note (20 and 21 Nov). I did not reopen Katz, Boxall, Bannai–Kobayashi, Hazewinkel, Tate, SGA 3,
Lubin–Tate or Jaswal: for those I rely on the reads recorded in LITERATURE.md by Claude Opus 5.5 at effort max.

## The two questions

**Is this what we want to say?** Yes. The note already opens with Katz's question, states the three theorems in
full, splits the credit by statement and page, compares with the neighbouring work and gives a proof overview. It
is much closer to the standard than the draft of the Deligne note was. What follows is an edit, not a rewrite.

**Whom does it not serve as it stands?**
- *The expert*: one sentence in a proof is false (comment 1), and several letters carry two meanings (comment 5).
- *The newcomer*: the abstract is a single block of some 330 words with the full formula in it, and there is no
  worked example; the point of Theorem B is easiest to see in a table (comment 2).
- *Those whose work it is*: Bannai and Kobayashi are credited in the abstract with a bound that Section 1.4 says
  follows from two of their propositions together (comment 3).

## Comments, most important first

1. **A false clause in the proof of Lemma 3.2 (rescaling).** The proof ends "… and Lemma 2.1 gives the claim,
   since v_p(n!) ≥ (n−1)/(p−1) ≥ (n−1)/(q−1)". The first inequality is false in general: v_p(n!) = (n − s_p(n))/(p−1),
   so it holds only when the digit sum of n is 1; for n = p − 1 and p ≥ 3 the left side is 0 and the right side is
   (p−2)/(p−1). The clause is also not needed. The claim follows from (D^n g)(0) = n!·[z^n] g(E(z)) and the
   containment proved just before, because n! is p^{v_p(n!)} times a unit. The lemma, as stated, and everything
   that uses it stand; in Proposition 3.3 it is applied only at powers of p, where v_p(n!) = (n−1)/(p−1) does hold.
   *Repair:* replace the clause by the correct reason. No statement changes.

2. **The abstract and the missing example.** The abstract should be shorter sentences with fewer symbols, as box 2
   of the standard asks. And the note has no example worked by hand. For p = 2 and h = 2 the two bounds, their
   maximum and Katz's value can be tabulated for n ≤ 9 in four rows; the rows for Theorem B and for Katz differ
   exactly at n = 3, 6, 9, and at n = 3 the function t³ attains the lower value. That table says what Theorem B
   means faster than its statement does.

3. **Credit to Bannai and Kobayashi.** The abstract says they "obtained" the bound c_h·n − (h−1) for Lubin–Tate
   groups over unramified bases. Section 1.4 says, more exactly, that their Propositions 3.3 and 3.5 together give
   it. The abstract should say the same. The credit to Katz (the question, the height-two bound, Corollary 1.8) and
   to Boxall is exact as it stands.

4. **The scope paragraph cannot be parsed.** "Not proved:" starts a list of three items; the first is followed by a
   long explanation with its own semicolons, after which the second and third items dangle. It should be three
   sentences.

5. **Letters with two meanings.**
   - b(n) is the recursion of Proposition 3.1 and also the bound of Theorem B; the scope paragraph then says
     "b(9) = 7" at height three. Theorem B's bound is a_2(n) of Theorem A and can be called that.
   - In the proof of Theorem C, a and b are the units −(p−1)! and −(p²)!/p^{p+1}, while a is the multi-index of
     D^a and b a multi-index in Lemma 5.1; in the proof overview b is first the coefficient of z^q and then that
     unit.
   - In Section 5.3, A and B are two power series rings, after A was the ramified valuation ring of Section 4 and B
     the number c_h(q−1).
   - "For the second theorem" introduces Theorem C, the third.

6. **The lead-in to Section 4** says that both propositions concern a ramified discrete valuation ring.
   Proposition 4.1 is stated, rightly, for any p-torsion-free W(F_q)-algebra.

7. **How the note sits with what is posted.** Jaswal's guide (hexagon:2611.00799) is treated exactly: where it
   finds step 2, and with which loss. Our posted note on the same remark (hexagon:2611.00789, footnote 3) should be
   cited in one sentence in the context section, so that a reader sees the two together. The two results that
   today's intakes put on the board (the chain length; the CM orbit bound) are not posted, and nothing of them
   belongs in this text.

8. **The words.** "A proved bound" (twice) is a process word; "gives a bound" says the same. The sentence on
   independence of the coordinate ("φ(s) ∈ (s) for every series s without constant term") needs one more step
   written out.

9. **The method note** should name the editor and say what the editor read.

## What I did not check

The sources themselves, as said above; the numerical record of the run (224 orders) and the program
`computations/dp42_check.py`; the statements of Graham–van Hoften–Howe, Kings–Sprang, Berger and Ardakov–Berger
quoted in the context section.

## Whom to write to when it is posted

As information only, with no request. After the user's word of 21 Nov on the first note, I keep the list short.
- **L. Alpöge**: the note bears on step 2 of his timeline (as with the first note).
- **M. Jaswal**: his guide treats the same step with a logarithmic loss (pp. 28–30 of his post).
- **N. Katz**: it is his question of 1977, and his Corollary 1.8 carries the proof. The user decided not to write
  to him about the first note; here the paper answers his own published question, so I list him, and it is the
  user's call.
- **K. Bannai and S. Kobayashi**: their bound for Lubin–Tate groups is the case that is extended. Optional.

The deposit sheet lists nine more names (Boxall, Berger, Ardakov, Graham, van Hoften, Howe, Kings, Sprang,
Hazewinkel, Tate, Lubin). Their work is context or a tool here; I would not write to them.

## Addendum (same day): hexagon:2611.00828

Asked to read "Three simplifications in the Alpöge–Claude argument for Dirichlet GRH" (twinheterodox). I read its
Hexagon page through the fetch tool, which showed the abstract, metadata and references, not the full text. By the
abstract the three simplifications are: a comparison of character sums at a common scale; the removal of a
logarithmic loss in the comparison of lattice slopes; a short deduction of the zero-free conclusion. The post is
conditional on the arithmetic inputs, and the construction of the lifts enters as an input. Nothing in the abstract
concerns step 2 (the divisibility of D^a θ(0)/Ω^a, invariant derivations, formal groups). LITERATURE.md records that
the main session read the post and reached the same conclusion. So it does not touch what this note answers; its
logarithmic loss is a different one. Version 2 cites it in the context section with one sentence saying so. Whether
its simplifications change the size hypotheses cannot be told from the abstract.

## Change log: `h09_note.tex` to `h09_note_v2.tex`

Made by a script from the untouched original; 12 pages; three pdflatex passes; no overfull box; every page rendered
at 95 dpi and read by me.

Mathematics:
1. Proof of Lemma 3.2: the false clause "since v_p(n!) ≥ (n−1)/(p−1) ≥ (n−1)/(q−1)" is replaced by the correct
   reason (n! is p^{v_p(n!)} times a unit), with the remark that at powers of p, the case used, the exponent is ≥ 0.
   No statement changes. Recorded in CHECK_EVENTS.tsv.
2. New Example 1.1 (p = 2, h = 2, n ≤ 9), computed by hand from Theorems A and B. Recorded in CHECK_EVENTS.tsv.

Notation, with no change of content:
3. Theorem B's bound is called a_2(n), as in Theorem A, instead of b(n), which is the recursion of Proposition 3.1.
4. In the proof of Theorem C and in the proof overview the two units are ε and ε′ instead of a and b.
5. In Section 5.3 the two power series rings are S and S′ instead of A and B.

Text:
6. Abstract: shorter sentences, fewer symbols; "results of Bannai and Kobayashi give" instead of "obtained"; the
   editor named.
7. Section 1.2: the sentence on independence of the coordinate written out. "For the third theorem".
8. Section 1.5: one sentence each on hexagon:2611.00828 and on our note hexagon:2611.00789; two bibliography items.
9. Section 1.6 (scope): three sentences for the three things not proved; "the recursion gives 7" for b(9) = 7.
10. After Proposition 3.1: "gives a bound" for "is a proved bound".
11. Section 4: the lead-in says what each proposition does.
12. Note on method: the editor, and what the editor read.

Not changed: the title, the theorems and all other proofs, the credit and context paragraphs apart from item 8, the
closing section, the bibliography apart from the two additions.

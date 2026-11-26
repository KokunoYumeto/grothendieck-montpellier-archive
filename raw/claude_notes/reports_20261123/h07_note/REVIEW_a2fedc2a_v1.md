# Editor's review of the H07 note (`h07_note_v2.tex`), and the change log of version 3

By Claude Fable 5.2 at effort max (agent a2fedc2a31aa5abb9, the Longue Marche field expert), 23 Nov 2026,
12:48-13:05 UTC (machine clock). The note is by the main session (Claude Opus 5.5 at effort max) from a proof by
GPT-6 Astra (ChatGPT Pro mode). The comments were formed before any change (they are in my notes file from 11:40 UTC
on); version 3 carries them out.

**What I read.** `h07_note.tex` and `h07_note_v2.tex` whole, every step followed; `RECORDS.md`;
`CLAUDE_CHECK_A05_steps3to6_20261123.md`; the model (`REVIEW_a3ccbc11_v4.md` whole, the opening and the closing note of
`deligne_sign_only_v5.tex`); the brief, HOW.md's "What a paper has to be", the two editors' files; H07's row on the
board and Round 9 of the candidates register. At the source: Saïdi-Tamagawa 2009 (arXiv:0801.1452, local TeX): the
Introduction, Remark 1.2, Definitions 1.3, 1.5, 1.6, 1.10, the statements of Lemma 1.7, Proposition 1.8 and
Corollary 1.11, and in §2 Theorem 2.2 and the passages on the fundamental extension. **Not read:** the run's own text
(AN_GRH A05), the re-proof of Steps 1-2 by a28ea31f, Grothendieck's two manuscript pages, SGA 1, Weil I, Mochizuki's
paper, Saïdi-Tamagawa 2018, Stix.

## The two questions

1. **Is this what we want to say?** The theorem and the proof: yes. I followed every step of v2 and found no error
   in a statement. But the note says less than it proves, and it claims as new a construction that has an author.
2. **Whom does it not serve as it stands?** Saïdi and Tamagawa (comment 1), Mochizuki and any expert who reaches
   page 3 (comment 2), the newcomer who does not know what a section is (comment 3).

**Kind of note: clear.** Hexagon searched again at about 12:55 UTC: "anabelian" gives only 2611.00419 (Zhenyu Sun, 13 Nov,
unrelated); "fundamental group section conjecture", "Tamagawa", "fundamental group curve" give nothing.

## Comments, most important first

### 1. The scope undersells the result: over a finite field the exceptional set is empty

v2 says (§1.6, §4) that separation of all closed points is not proved, "whose decomposition groups are not sections".
It follows in ten lines. Saïdi and Tamagawa's exceptional set is defined through commensurability of decomposition
groups (Definitions 1.3, 1.5). If `D_x~` and `D_x~'` are commensurate, their intersection `D_0` maps onto `G_L` for a
finite extension `L`; over `L` both points become rational, and `D_0` is the image of both sections; Theorem 1 over
`L` makes the points equal. Pairs with a cusp and pairs over one geometric point are excluded by their Proposition
1.8(ii), (iii). So their exceptional set is empty for the set of all primes different from `p`, and the map of their
Corollary 1.11 is injective. This is the statement they say they could not prove (Introduction: only "almost
injective"), and they would see the deduction at once. **In v3: Corollary 2, with its proof (§4.3).** It is a new
statement of mine and no one else has checked it.

### 2. The credit for Steps 1, 2 and 5: this is cuspidalization

v2 calls "the transport of the cusp through the configuration space of two points" new and never says
"cuspidalization" (the deposit sheet's keywords do). The configuration space, the decomposition group of the
diagonal, the quotients that are pro-r or central along the cusp, and the extension class as the Chern class of the
point are Mochizuki's theory ("Absolute anabelian cuspidalizations of proper hyperbolic curves"), which Saïdi and
Tamagawa carry over to prime-to-p groups in their §2 (Theorem 2.2 = his Theorem 1.16(iii); the fundamental extension
= his Propositions 1.6, 1.8). What the proof here adds in those steps is a direct proof of exactness for the
quotient that is pro-r along the diagonal (Lemma 3.2, Proposition 3.3) and the use of the conjugator. **In v3:** the
credit paragraph, the abstract and the overview say so; Mochizuki is in the bibliography, cited through
Saïdi-Tamagawa §2 and marked as not opened.

### 3. The theorem is not said in words

A newcomer gets "sections" and a displayed map. **In v3:** what `s_P` is; the equivalent statement by covers (two
distinct rational points are separated by a finite étale cover with a rational point above one and none above the
other); why "hyperbolic" is needed (on an elliptic curve `s_P ~ s_Q` exactly when `P - Q` has p-power order; removing
a point does not change the abelianization, and the theorem says it makes the map injective); the cases of the affine
line, the projective line and `G_m`.

### 4. The abstract and the opening

The first sentence had seventy words. "The proof uses no conjecture" is an aside from our own history. The Riemann
hypothesis for curves is Weil's, cited from Deligne. The last sentence did not name an editor. "Proof overview" was a
subsection; HOW.md asks for a section. **In v3:** rewritten; the overview is Section 2 and says where each hypothesis
is used.

### 5. Three places where the proof's wording had a gap (no statement changes)

- **Genus one (§3.2 of v2).** `K'` must also make the points of `[m]^{-1}(P)` rational; otherwise `s_P|G_K'` need not
  land in `Π_X'`, and the sentence "`s_Q|G_K'` lands in `Π_X'`, which is normal" has no ground. Repaired; the rest of
  the argument was re-derived and holds.
- **Step 5, Lemma 1.7.** The lemma as printed says that the commensurator maps injectively to `G_k` and equals the
  normalizer and the centralizer. "The normalizer of `D_R` is `D_R`" follows because `D_R` maps onto `G_L`. Now cited
  so; `D_R^P`, `D_R^Q` are introduced with a common image.
- **Step 5.** "since `G_k` has cohomological dimension one" is not needed for `H^1(Π_C, M) = H^1(G_k, M)`. Removed.

### 6. Notation

`K` was the base field and a profinite group; `Q` a point and a finite r-group; `r` the number of points at infinity
and a prime; `E_C` the exceptional set beside the group `E_c`. Fixed in v3. Left as they are: `L` (a free group in
Step 1, a field later), `R` (a subgroup in Proposition 3.3, a point later), `T`.

### 7. Sources

`RECORDS.md` lists no reading of SGA 1 or of Weil I: the locators are the run's. The note on method now says so, and
says what was read at the source and by whom.

## Change log (v2 to v3)

Made by `_v3_parts/make_v3.py` from v2: a new front, fifteen exact replacements in the body, a new end. v1 and v2 are
untouched.

1. Abstract rewritten. Title kept.
2. Section 1 rewritten: 1.1 (what a section is; the characteristic-zero argument); 1.2 (definitions, Theorem 1, the
   form by covers, the non-hyperbolic cases, **Corollary 2**); 1.3 to 1.6 (why it matters, credit, context, scope).
3. "Proof overview" is Section 2, with the difficulty, the idea and the use of each hypothesis.
4. Section 3 (finite fields): `G` for the group in `N(G)`; `W` in the proof of Lemma 3.2, and the count of lifts
   stated as a power of r; the decomposition group of the diagonal defined; Lemma 3.5 stated for `K_F`, with its
   last line; Step 4: `(G_P)_L` defined, the exceptional set written `𝓔_C` and described as in the source, the last
   sentence reworded; Step 5: the two repairs of comment 5.
5. Section 4: the genus-one repair of comment 5; new §4.3 with the proof of Corollary 2.
6. "What remains open" rewritten (closed points over a finite field are no longer open).
7. Note on method rewritten; bibliography: Mochizuki and Stix (not consulted) added.

Build: three pdflatex passes, 9 pages, no overfull or underfull box, no undefined reference. All nine pages were
rendered at 80 dpi and read. Three sentences were then reworded (one on page 3, two on page 6); the final build has
the same page breaks, and its page 6 was read again.

## Left before posting

1. A second reader for Corollary 2 and its proof (§4.3, ten lines).
2. The user's look and word.
3. Stix, LNM 2054, chapter 7: still unread. It bears on what is known and on credit, not on correctness.
4. Mochizuki's paper opened once, to confirm the three locators and the journal reference.
5. The SGA 1 and Weil I locators, which no record of ours shows as read.

## Whom to write to

- **M. Saïdi and A. Tamagawa**, when it is posted, as information: the note uses their finiteness theorem and
  concludes that their exceptional set is empty. Ask whether the statement is known to them.
- **J. Stix**, with the question his chapter would answer.
- **S. Mochizuki or Y. Hoshi**, if the user wishes, for the cuspidalization credit.

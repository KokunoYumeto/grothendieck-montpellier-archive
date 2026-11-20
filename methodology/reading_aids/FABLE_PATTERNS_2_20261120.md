# More predictable error patterns: what the sheet and GLOBAL_INFERENCE.md do not have yet

20 Nov 2026, Claude Fable 5.2 at effort max. Text only: no image was opened. Every figure is marked **[counted]** (by a
script of mine on the files named), **[estimated]** (from counted figures or from a sample) or **[guessed]**.

**Data.** `SP_CHANGES.tsv` (8,093 rows), `NOBODY_DOUBTED.tsv` (1,380), `FEATURE_RATES.tsv`, `LETTER_SWAPS.tsv`,
`SYMBOL_SWAPS.tsv`, `pilots_api_20261120/lowconf_100/scored.tsv`, and the same 559 page pairs that
`predictable_patterns.py` uses, on which I counted further features with its tokenizer and its rule for "changed"
(base rate 7.2 tokens in 100; 7.3 outside TikZ and spacing code). Ids are run, folder and scan of `SP_CHANGES.tsv`
(SP02 B10-09/126), or `lc-NNN` of the pilot.

## 1. The route: every rate here is a rate of one reader

- **All 559 measured pages are Codex web pages** (GPT-6 Astra at reasoning effort max): their folders start with A, B,
  C, H or J, and every second pass so far is a `_CW_` piece [counted].
- **The 12,931 pages without a second pass are mostly from other routes** [counted from MANIFEST.tsv]:
  - ChatGPT Work (GPT-6.2 Astra at reasoning effort max): 5,751;
  - Pro first reading (GPT-6 Astra, ChatGPT Pro mode): 4,103;
  - the API typescript route: 1,361;
  - the 13 Nov pages (Claude Opus 5.5 at effort max on a Pro first reading): 898;
  - Codex web: 751, which is 5.8 %;
  - settled by a doubt-mark run: 67.
- So the column `predicted_changes` of FEATURE_RATES.tsv, and every "in the pages without a second pass" below, carries
  Codex web's error rates over to four other readers. Whether a pattern lives in his hand or in that reader can only
  be told once a Work page and a Pro-first-reading page have been through a second pass and scored the same way.

## 2. New patterns

Each has: the count and examples; where it lives; whether a script finds its places in the pages without a second
pass, and how many; what a reader does.

### N1. A doubt mark in a formula casts a shadow on the formula
- **Count:** mathematics within 3 tokens of a doubt mark, and not inside it: 2,742 of 19,432 tokens changed (14.1 %,
  twice the base), above the base in 25 of 28 runs. Words near a doubt mark: 523 of 9,718 (5.4 %, below the base), above
  it in 7 of 28 runs [counted].
- **Lives in:** the reader. When it doubts one sign of a formula, the signs beside it are wrong twice as often; in prose
  there is no such effect.
- **Script:** yes. 332,608 such tokens in the pages without a second pass [counted].
- **Reader:** at a doubt mark inside a formula, read the whole formula again, not the marked sign alone.

### N2. Letter corrections on typescripts are records, not errors of the witness
- **Count:** 601 rows record a letter typed or written over another, and 241 more say which letter is typed and which
  is by hand: 842 of 8,093 [counted by keyword]. Of the first group SP02 on cote 10 has most, about 4 a page; cote 57
  comes next. Examples: SP02 B10-09/126 « compatibles » → `c\rlap{i}ompatibles`; SP02 B10-01/33 « deux » →
  `deu\deleted{s}\inserted{\handwritten{x}}`; SP02 B10-05/71 "handwritten f only" → `\deleted{d}\handwritten{f}`.
- **In all of these witness C had the right word.** With layout (87), line ends (29), tag side (14), specks (28) and
  the watermark, about 1,000 of the 8,093 rows record apparatus where C's word or sign stands [counted by keyword].
- **Lives in:** the typist (cotes 10, 12, 57, 36, 37, 123) and our conventions: whether the letter underneath is
  recorded.
- **Script:** it cannot find the places (C shows a normal word). It can list the typescripts: 349 pages without a
  second pass carry a `\handwritten` macro (Work 233, Codex web 116), and the API route has 1,361 [counted].
- **Reader:** one decision per run, in the prompt: record the letter underneath or not. If it is recorded, it is one
  `\deleted` letter beside an untouched word, and never a row against the witness.

### N3. Typing errors and missing accents are corrected silently by both readers
- **Count:** 118 rows where one word differs from another by one or two letters; in 64 both witnesses had the same
  word [counted]. In a sample of 26, 9 are typing errors or missing accents that the pass restored, so about 40 of the
  118 [estimated]. Examples: SP02 B10-03/55 « quotient » → « quptient »; B10-05/74 « connaiassance » →
  « connaiasance »; B10-04/61 « contraintes » → « constraintes »; B10-04/60 « Azumaya » → « Azymaya »; SP12 A57-01/6
  « fields » → « fielde »; B10-03/56 « linéaire » → « lineaire ».
- **Lives in:** the typist, and in both readers: a model writes the word it recognises.
- **Script:** no. The corrected word is correct French, so nothing marks it.
- **Reader:** on a typescript, read letter by letter the words you recognise at once; a typed word may be misspelt,
  and it stays so.

### N4. Digits written by hand, in margins or under a strike; and no pair of digits is safe
- **Count, outside TikZ code** [counted]:
  - a handwritten digit on a typescript: 133 of 1,023 changed (13.0 %; above the base in 5 of 8 runs);
  - a digit in a margin note: 50 of 395 (12.7 %; 4 of 8 runs);
  - a digit in a tikz-cd diagram: 44 of 403 (10.9 %; 4 of 6);
  - a digit in struck text: 114 of 1,088 (10.5 %; 7 of 9);
  - against a digit in prose 6.5 % and in mathematics 5.7 %.
- **Swaps:** 153 digit-for-digit swaps over 65 pairs. The commonest are 1→2 (8), 5→6 (7), 3→5 (6), 3→4 (6), 2→1 (6),
  1→0 (6), 0→1 (5, all on cote 37) [counted].
- **Lives in:** his hand, where he adds numbers by pen (cotes 57, 123, 29, 37).
- **Script:** yes. 19,393 digits in margin notes, 25,757 in struck text and 2,148 handwritten digits in the pages
  without a second pass [counted; the handwritten macro exists only in Work and Codex web pages].
- **Reader:** look at every digit written by pen on a typescript or in a margin at full size; a 5 may be a 6 or a 3.

### N5. Double-struck letters, and what the typewriter cannot type
- **Count:** a letter in `\mathbb`: 84 of 750 changed (11.2 %; above the base in 4 of 4 runs); the macro itself 126 of
  1,215 (10.4 %; 5 of 6). Calligraphic letters 2.9 %, Fraktur 1.9 % [counted]. Swaps: `\mathcal`→`\mathbb` 7 (cote
  53), `\mathscr`→`\mathfrak` 6 (cote 156-6), `\times`→ x 7 rows (SP02 B10-04/65, B10-10/136 « W\times G » →
  `W\mathrm{x}G`). The class "alphabet" of NOBODY_DOUBTED.tsv has 59.
- **Lives in:** typescripts (a doubled capital for a double-struck letter, an x for ×) and our conventions; in the
  hand, he doubles a Z in one place and not in the next (SP38's brief: "A visibly single-stroked Z can differ from a
  later doubled Z on the same page").
- **Script:** yes. `\mathbb` occurs 16,900 times and `\times` 7,815 times in the pages without a second pass [counted].
- **Reader:** on a typescript, enter the keyed form once in the notation table (doubled capital, x) and do not doubt
  each place; in handwriting, check each Z, Q, R, N, F for its second stroke.

### N6. An insertion that was struck again
- **Count:** words both inserted and struck: 62 of 359 changed (17.3 %, 3.6 times the rate of a word; above the base
  in 3 of 4 runs) [counted]. Cotes 123, 10, 12.
- **Lives in:** his hand: a second thought written small above the line, then cancelled.
- **Script:** yes. 4,785 such words in the pages without a second pass [counted].
- **Reader:** a cancelled insertion gets its own crop: it is small, above the line and under a stroke at once.

### N7. Arrows with a hook, a bar, two shafts or a label
- **Count:** 34 of 254 changed (13.4 %; above the base in 3 of 3 runs), against 10.9 % for → and 9.0 % for ⟶ [counted].
  Swaps: `\longmapsto`→`\rightsquigarrow` 2, `\xrightarrow`→`\overset` 3.
- **Lives in:** his hand: the hook, the bar and the second shaft are small strokes at the ends.
- **Script:** yes. 7,168 in the pages without a second pass [counted].
- **Reader:** look at both ends of every arrow, and take a label above it as part of it.

### N8. The paper's watermark given as his text
- **Count:** 92 pages of the text of record contain « Extra Strong »: 156-1 26, 156-3 22, 156-2 18, 126 11, 13 5, and
  10 more [counted]. On 156-3 a pass added it as doubtful text in 22 rows: SP31 J156-3-03/24 "omitted" →
  `\unsure{Strong Extra}`; J156-3-02/12 → `\unsure{ra Strong Extra}`. Pilot: lc-001, lc-002, lc-019.
- **Lives in:** the paper (the 156 cotes, 126, 13), read sideways or mirrored through the sheet.
- **Script:** yes: the 92 pages, 64 of them without a second pass (Pro first reading 44, Work 19, API 1) [counted].
- **Reader:** name the watermark once per cote in the notes; it is never transcribed and never a doubt mark.

### N9. Specks given as points
- **Count:** 34 rows add a doubtful point or comma where witness C had nothing, 26 of them in three-reader runs (SP47
  9, SP50 6, SP41 4, SP40 3, SP52 3) [counted]; 89 rows by a wider search for "small detached point" [counted by
  keyword]. Pilot: 6 of 100 are "nothing there (a speck, or no ink)", and in 3 more Claude Opus 5.5 at effort high
  kept C's text against an added `\unsure{.}` (lc-006, 020, 022, 087, 088, 091; lc-025, 032, 082).
- **Lives in:** the reader: the three-reader second passes (GPT-6 Astra, ChatGPT Pro mode).
- **Script:** yes, in the returns: a `\unsure{.}`, `\unsure{,}` or `\unsure{\cdot}` where both witnesses have nothing.
- **Reader:** a point is punctuation only on the baseline, between words, in the pen's ink; a speck gets no mark.

### N10. The direction of an accent
- **Count:** 79 rows differ by an accent only; in 44 both witnesses had the same word; 21 are firm, and the other 58
  leave a doubt or are of low confidence [counted]. Examples: SP44 A36-01/13 « régulier » → « règulier »; SP50 H134-02/150 « algébriques » → « algèbriques »;
  SP14 H48-01/3 « Schémas » → « Schèmas »; SP52 J156-4-09/67 → `\unsure{determinent|déterminent}`.
- **Lives in:** his hand: the accent is one short stroke whose slant does not tell acute from grave (cotes 134, 156-4,
  75, 81).
- **Script:** no list worth making: a word with an accent is changed at 6.2 %, a word at 5.2 % [counted].
- **Reader:** where a stroke is there, write the accent the word has in French; note a missing accent only where no
  stroke is there; never doubt the slant. [a convention for the user to confirm]

### N11. A superscript + shaped like ⊤
- **Count:** 7 rows, all SP41 on cote 81 (J81-05/35, /37, /38: `\Sigma_1^{+}` → `\Sigma_1^{\top}`), none at high
  confidence; both witnesses had + in 6 [counted].
- **Lives in:** his hand (a + whose upright stops at the bar) and in the pass, which gave the shape. The same line has
  Σ₁⁻, so the sign is a +. With F005 of the bank (a + without its upright) this is one foible: a + can lose either
  stroke.
- **Script:** yes. `\top` occurs 5 times in the pages without a second pass; a superscript + 2,289 times [counted].
- **Reader:** a bar or a T paired with a minus on the same line is a +; write + and note the shape once.

### N12. The empty set written ϕ
- **Count:** `\varnothing`→`\phi` 6 token swaps and 4 rows (SP37 J71-05/36; SP04 J156-4-07/56) [counted].
- **Lives in:** his notation (cotes 71, 156-4) and our conventions: C gives the meant sign, the pass the written
  letter.
- **Script:** yes. 2,087 empty-set signs in the pages without a second pass [counted].
- **Reader:** write what he writes and enter « ϕ : l'ensemble vide » in the notation table once.

### N13. Formula numbers stand at the left
- **Count:** `\tag*`→`\end` 25 token swaps (22 on cote 57); 28 rows "right-side tag" → "handwritten (1) at left" (SP12
  A57-01/3, /4, /8, /10, /11); a digit of a formula number or circled number: 67 of 392 changed (17.1 %) [counted].
- **Lives in:** our conventions: `\tag*` sets the number at the right. No reading changes.
- **Script:** yes: 8,258 such digits in the pages without a second pass [counted]. One left-number macro, applied by
  script, closes the class.
- **Reader:** nothing at each place.

### N14. Letters of one cote, in mathematics
- **Count:** 56 letter-for-letter swaps in mathematics over 33 pairs [counted]: G→C 3 (156-7); j→J 3 (134-2); B→D 2
  and K→k 2 (13); f→y 2 (104); x→n 2 (75); p→r 2 (53). Beside them E→ε 8 times, all on 156-3.
- **Lives in:** his hand on that cote, like g and q on cote 103 in the sheet.
- **Script:** only with care. A capital E in mathematics occurs 734 times on the 156 cotes without a second pass, but
  693 of them are on 156-9, where E is the name of the set [counted]. The habit is shown for 156-3 only.
- **Reader:** on 156-3 a capital E in a formula may be his ε: compare it with an ε of the same page.

### N15. His page numbers left out; reference numbers safe
- **Count:** 54 rows about a page number or a mark at the head of the sheet; 32 are SP02 on cote 10 ("omitted" →
  `mspage 70`, B10-05/71, /72) [counted].
- **Lives in:** the reader (the Codex web folders of cote 10 left the sheet numbers out).
- **Script:** a list to glance at: 5,487 pages without a second pass have no `\mspage` (Work 3,197, Pro first reading
  1,897, the 13 Nov pages 248, Codex web 145) [counted]; many sheets carry no number.
- **Reader:** look at the head of the sheet for his number before the first line.
- **Safe:** a digit after §, p., n° or cf. changed in 3 of 478 (0.6 %); item numbers 4.3 % [counted].

### N16. Capitalised words inside a sentence
- **Count:** 174 of 1,824 changed (9.5 %, twice the rate of a word; above the base in 9 of 20 runs) [counted]. Row
  examples are few: SP50 H134-02/152 « Ruget » → « Rüget »; SP02 B10-04/60 « Azumaya ». Michel Hua's checks have four
  names read from the page (H0126, H0132, H0466, H0362).
- **Lives in:** any reader: nothing in the sentence predicts a name.
- **Script:** yes. 29,435 in the pages without a second pass [counted].
- **Reader:** read a name letter by letter and compare it with the names of the same cote.

### N17. Two habits of single runs
- **Dots counted:** 20 rows, 10 in SP39 on cote 75 (`\ldots` → `\mathinner{\cdotp\cdotp}`) [counted]. An ellipsis is
  `\ldots` whatever the number of dots.
- **Line ends of typescripts:** 35 rows, 19 in SP02 (`opéra-\linebreak tions`; B10-02/43 « quasi-\linebreak -séparé »)
  [counted]. Line ends are not recorded; where a word is divided at its own hyphen, one hyphen stays.

### Tested and not confirmed
- **The first page of a session folder:** 8.2 % against 7.1 % on later pages, but higher in only 14 of 26 runs
  [counted].
- **The head of the page:** the first tenth has 8.2 % against 6.4 to 7.8 % below, but its words are at 5.1 %: the
  excess is in numbers and marks (N15), not in words [counted].
- **Short pages:** under 400 tokens 8.3 %, over 1,500 tokens 6.1 % [counted]; 1,960 such pages have no second pass.

### Where a reader need not spend a crop (changed less than the base of 7.2 %) [counted]
- commas 3.3 %; parentheses and brackets 4.0 %; underlined words 4.0 %;
- letters in an index 3.9 % (6,001 tokens, braces counted); digits in an exponent 3.7 %;
- calligraphic and Fraktur letters 2.9 % and 1.9 %; ∩ 2.1 %, ∪ 3.0 %, Σ 1.6 %, ∃ 1.3 %;
- reference numbers 0.6 %.

## 3. What the new data contradicts

1. **Sheet, item 1, first line: "ξ and ζ, γ and Γ, ρ and p, δ and λ, Λ and A, Δ and 2".** On witness C these letters are
   not error-prone: ξ 5.1 %, δ 8.1 %, ρ 3.8 %, Γ 3.3 %, Δ 1.0 %, λ 0.8 % (FEATURE_RATES.tsv), at or below the base. The
   list comes from Michel Hua's checks of witness H, so it describes H's first reader (an AI transcription of Hua's
   project). C's letters are Φ 53 %, Π 29 %, φ 23 %, γ 20 %, ψ 17 %, π 16 %. Only γ is on both lists.
2. **Sheet, item 1: "Small digits, primes and exponents".** A prime is changed at 3.3 %, a digit in an index at 5.4 %,
   a letter in an index at 3.9 %, a digit in an exponent at 3.7 %; a letter in an exponent at 8.1 %, above the base in
   1 of 6 runs [counted, braces included]. They are many in the tables because formulas are many. The 667 doubt marks
   on a prime are doubts, not errors.
3. **Sheet, item 2, and G11: endings.** A word ending in s is changed at 5.6 %, any word at 5.2 % (above the base in 6
   of 28 runs). That the grammar does not decide stands; that endings are a place of error in C does not show.
4. **Sheet, item 3, and G2: "the hardest word on the page".** A short inserted word is changed at 10.1 %, any inserted
   word at 13.4 %, a word in a doubt mark at 30 %. The 5 of 10 was measured on witness H.
5. **G7 and rank 8 of my plan: "an arrow is often a dash".** Among the 300 commonest sign swaps there is no dash for an
   arrow or arrow for a dash (one `\longrightarrow`→`\relbar`), and no + for − or − for +. The sign − is changed at
   5.8 %. The 1,278 marks − | → are doubts C raised itself; the test of 50 marks in the plan still decides them.
6. **My plan: "2,508 firm reading corrections".** About 1,000 rows of the larger table record apparatus (N2). Counted
   again: 4,096 rows give another reading, 2,448 of them firm; 724 of the firm ones (30 %) are at a doubt mark of C,
   and 241 (10 %) are places where C and H agreed and neither doubted. The share at a doubt mark was 28 % in the plan;
   it holds.
7. **FEATURE_RATES.tsv, `predicted_changes`, and the sheet's "tokens changed per 100":** one route only (section 1).

## 4. The 100 low-confidence places: what a second model narrows

Claude Opus 5.5 at effort high, blind to the pass, from the saved crop; verdicts as `scored.tsv` has them now
[counted]: one of the pass's readings 40; a reading of its own 28; witness C's reading 11; witness H's reading 11;
nothing there 6; the pass gave a description 4. Its own confidence: high 4, medium 52, low 44.

**It narrows:**
- **Doubts the pass made itself about points.** 9 places: 6 specks and 3 added `\unsure{.}` (N9). It removes them.
- **A choice between forms that differ in shape.** In about 16 places it gives one of the pass's readings, alone, at
  medium or high confidence [estimated from the list]: « : » against < and ∈ (lc-036), * against ∂ and ∅ (lc-027),
  e_1 against e_i (lc-031), 𝔓 against 𝒫 (lc-041), « spacieux » (lc-047), « classes » against « choses » (lc-055),
  « le » against « la » (lc-083).
- **A change of the pass that C did not need.** 11 places, 3 at high confidence: F∥G (lc-029), Z''(t_0) where the pass
  wrote t_o (lc-034), « viennent » (lc-064).

**It does not narrow:**
- **Struck text.** Of the 15 deletion-state places: its own reading 5, the pass's 3, C's 3, H's 4. Under a strike it
  repeats the doubt (`\deleted{\unsure{…}}`, lc-003, 007, 009, 013, 014) or adds a third reading.
- **Ink the pass half read.** Of the 9: its own reading 4, illegible 3 (then it is with H), the pass's 2.
- **Its own readings.** 28 places, 16 at low confidence: a third candidate, so the place is wider than before.
- **Drawings and descriptions.** 6 and 4 places: nothing to compare.

**Two cautions.** It agrees with H as often as with C (11 and 11), and H is the same family, so its agreement with H
is not a second opinion. And it identified the watermark (lc-001) where the passes had doubtful text.

**In numbers:** about 36 of 100 come out narrower (9 + 16 + 11), about 64 stay open or get wider [estimated]. At
$0.87 for 100, a narrowed place costs about 2.4 cents [estimated]. The cheap gain is to send it only signs, short
words and added points, and to keep struck text and half-read ink out.

## 5. Scripts these patterns allow, with their counts in the pages without a second pass

| script | finds | count | then |
|---|---|---|---|
| watermark | « Extra Strong » given as text | 64 pages (92 in all) | mark as watermark, drop the doubt marks |
| formula numbers | digits in `\tag` and `\textcircled` | 8,258 digits | one left-number macro |
| empty set | `\varnothing`, `\emptyset` | 2,087 | notation table, per cote |
| added points | `\unsure{.}` and the like where both witnesses have nothing | 34 rows in the returns | remove after one look |
| the shadow of a doubt mark | formulas holding a doubt mark | 332,608 tokens near a mark | the formula as the unit of every doubt-mark check |
| struck insertions | `\inserted` inside `\deleted` or the reverse | 4,785 words | a crop each in the full pass |
| digits by pen | digits in margins, in struck text, in `\handwritten` | 19,393; 25,757; 2,148 | a look at full size |
| special arrows | ↪ ↦ ⟼ ⇉ and labelled arrows | 7,168 | both ends checked |
| names | capitalised words inside a sentence | 29,435 | compared within the cote |
| typescript pages | pages with `\handwritten`, and the API route | 349 and 1,361 | the decision of N2 and N5 before their pass |

## 6. Limits

- The rates are Codex web's (section 1). They say where that reader fails, not where the others do.
- "Changed" means the pass wrote something else; it does not mean the pass is right. N9 and N11 are cases where it is
  not, and nobody has checked a sample of the changes on the scan.
- The counts "by keyword" come from the wording of the collation rows, which is free text; they can be off by a tenth.
- The pilot is 100 places, and I sorted its 16 "narrowed" places by reading the list once.

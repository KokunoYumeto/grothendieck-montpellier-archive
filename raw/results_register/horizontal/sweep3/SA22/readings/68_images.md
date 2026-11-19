# Cote 68: image decisions (004, 013, 015-022)

By Claude Opus 5.5 at effort max, reader 122_125, horizontal sweep 3, wave 2, 19 Nov 2026, for agent ae4ae3dc17acaa440
(Claude Opus 5.5 at effort max). The ink decides; Michel Hua's project is a witness only.

**Sources:**
- the Pro transcription MPL_66+68_002-032 (GPT-6 Astra, ChatGPT Pro mode) and its doubts file, rows as cited;
- the scans of `68.pdf` (section 10), rendered at 8-24x and read. The crops are in my scratchpad (`r122_125/q0*.png`)
  and were not kept;
- witness H: Michel Hua's project, `68/68.modern.tex` and `68/batch-01.fr.tex`. His page p is our scan p + 1.

## 68/004 (SA22-1, Th. 1, proof of the second "⟸"): "[en garder|en gardant]"

- **The ink:**
  - An interlinear insertion above "On va ( définir", tied by a long arc to the "(" after "On va".
  - It reads "en", a hyphen-like joint, "g" (his z-shaped g, as in "gagnante" on the same face), "a", a reduced "r",
    "d" with a looped ascender, and one reduced final stroke with a descending hook.
  - The insertion has no "t" cross and no Σ.
- **Decision: "en gardant".**
  - The ink fixes "en gard…".
  - The ending is a single reduced stroke and does not separate "-er" from "-ant". Only the gerund is French here: "On
    va, en gardant [Σ], définir une j-stratégie Σ′ x-gagnante ainsi".
  - Confidence medium.
- **The mathematics agrees:** Σ′(z) = Σ(z) for z ≠ x and Σ′(x) = {y}, so Σ is kept everywhere except at x.
- **Witness H** reads "(en changeant Σ)".
  - The ink excludes it: the insertion has no "ch" and no Σ.
  - Hua's phrase describes the same construction from the other side, but it is not what is written.

## 68/013 (SA22-1, "? Th 3"), left margin: "[et n'existe de]"

- **The ink**, rotated by about 38°, reads in six lines:
  - "Si C fini" (underlined, with an ink blot on the f);
  - "et si n'existe de";
  - "partie infinie";
  - "Plus généralement";
  - "si C = ∪C_i";
  - "cf §2".
- **Decision: "et si n'existe de".**
  - The first word is "et" (his looped e joined to a crossed t), not "ou".
  - Then comes a short "si" (his r-like s and a dotted i), which the Pro reading dropped. Then "n'existe de".
  - It stands for "et s'il n'existe pas de partie infinie", abbreviated by him.
  - Confidence: high for "et", medium for "si".
- **The mathematics agrees with "et":**
  - C finite and no infinite play give C = C_{N−1} (his §2, 002–003). That is a special case of the "plus généralement"
    C = ∪C_i, under which the margin's proof of G_∞(j) = G(j) goes through (SA22 STUDY, 3.1).
  - With "ou", the margin would also assert Th 3 for C infinite with no infinite play. That fails, and Michel Hua's
    project gives the counterexample itself: a position whose successors start forced chains of lengths 1, 2, …
  - So the ink removes the defect that witness H found in its own reading ("ou s'il n'existe pas de").

## 68/015 (SA22-2, the scratch sheet): "[dissociés|bons]", "[bons|donnés]", "[bons|donné]", "élémentaire ?"

- **The ink:** the three adjectives are one word.
  - Each begins with his crossed t: a tall stem with a horizontal loop through it, like the t of "translation" two lines
    below.
  - It is not a b, which in his hand is a tall loop closed by a bowl (as in "stable" on the same face). It is not a d,
    whose round bowl sits at x-height.
  - Then come a small a, a reduced "ss" (two short humps), an é with its accent, and, in the first occurrence, a final
    s. The first occurrence is partly overwritten at its start.
- **Decision:**
  - "(E_{2n} ∗ E_2) tassés sss [E_2 ss-gp (élémentaire ?); E_{2n} stable par translation de E_2]";
  - "E_{2n+1}, E_2 tassé {…}";
  - "E_3 E_3 tassé 3222".
  - Confidence: medium for the first (its start is overwritten), medium-high for the other two.
- **The mathematics agrees** (re-derived). "Tassé" is the §4 notion of 021: f′∗g′ ≺ f∗g for all rearrangements.
  - Even case. Take E_2 = {0, a} a subgroup and E_{2n} stable under +a. Then 1_{E_{2n}} ∗ 1_{E_2} = 2·1_{E_{2n}}, with
    mass 4n and maximum 2. So it majorizes every 1_{A′} ∗ 1_{B′} with |A′| = 2n and |B′| = 2: the partial sums are at
    most min(2k, 4n).
  - Odd case. Take E_{2n+1} = E′_{2n} ⊔ {x} with E′_{2n} stable under +a. The convolution is 2 on 2n points and 1 on
    {x, x+a}. That is the most packed profile for odd size, since a set of odd size cannot be stable under an
    involutive translation.
  - E_3 ∗ E_3 with profile 3,2,2,2 is the packed profile of V_1 ∪ {x} in a group of order 4 (mass 9). The profile is
    Michel Hua's project's computation, re-checked here.
  - A refinement of his "sss" (not an ink question). For general E_2 = {b₁, b₂}, maximal packing holds iff E_{2n} is
    stable under translation by b₂ − b₁. "E_2 ss-gp" is the normalised case, b₁ = 0 and 2(b₂ − b₁) = 0. So the "sss"
    holds as stated only with that normalisation: in ℤ/4, E_2 = {0, 1} and E_4 = ℤ/4 are also packed. His
    "(élémentaire ?)" is his own doubt at this point.
- **"élémentaire ?":**
  - The ink is "(", é, a tall l, é, a reduced "men", a short t, a reduced "aire", "?" and ")".
  - It is consistent with "élémentaire" letter by letter at the tall strokes. Confidence medium-low.
  - The "?" is his.
- **Witness H** names no word on this face ("calculs sans phrases"). Its reading of the line ("E_2 est un sous-groupe et
  E_{2n} est stable par translation par E_2") agrees.

## 68/020-022 (SA22-2): "pritorisé(s)|priorisé(s)" and "bon(s)|tassé(s)"

- **The ink of "pritorisés|priorisés"**, at every occurrence:
  - The letters are p, r, an é whose accent is drawn as a tick or a dot (the Pro pass read it as the dot of an i), the
    crossed t, a small a, a reduced "ss", an é with a clear acute accent, and s where plural.
  - That is nine glyphs for the plural, the count of "prétassés". "Pritorisés" needs ten, and "priorisés" has no t.
  - "Privilégiés", the doubts file's other alternative, would need a v, a tall l and a g descender. None of them is
    there.
  - The six occurrences:
    - 020, title: "3 Couples prétassés";
    - 020, Déf: "le couple (f,g) est prétassé";
    - 020, Cor: "(f,f) est prétassé";
    - 021, line 2: "la condition (f,g) prétassé";
    - 021: "Cela implique que (f,g) est prétassé" (the accent on "pré" is clear here);
    - 022, margin: "les couples ∈ S×S sont prétassés".
- **The ink of "bon(s)":** the same crossed t, a, reduced ss and é(s) as on 015, with no b anywhere.
  - 021, title: "4. Couples tassés." The Pro text has "bons" here without a doubt mark.
  - 021, Cor a): "∀ (f,g) ∈ S×S sont tassés".
  - 022, d): "A′∗B′ ≺ A∗B i.e. (A,B) tassé".
  - 022, the two right-hand brackets: "[(f,f) tassé]" and "[(f,A) tassé pour A ∈ S₀]". "Pré" is written above "tassé"
    with an insertion arc, so the final text is "prétassé". The Pro pass read a struck "bon" with an inserted "pri";
    "tassé" is not struck.
- **Decision:**
  - "prétassé(s)" for all six;
  - "tassé(s)" for the four occurrences of "bon(s)";
  - "prétassé" in the two brackets of 022.
  - Confidence: high for the 021 title and for "Cela implique que … prétassé", medium-high elsewhere.
- **The mathematics agrees** (re-derived):
  - "Prétassé" (§3) is |f, g| = ‖f∗g‖_∞. "Tassé" (§4) is f′∗g′ ≺ f∗g for all f′ ≺ f and g′ ≺ g.
  - Tassé implies prétassé.
    - Always ‖f∗g‖_∞ ≤ |f, g|, because (f∗g)(s) = ⟨f, ε_s∗ǧ⟩ and ε_s∗ǧ ∼ g.
    - Conversely, |f, g| = sup over f′ ∼ f of (f′∗ǧ)(e), which is at most sup ‖f′∗g′‖_∞ = ‖f∗g‖_∞ when the pair is
      tassé.
    - That is his "Cela implique que (f,g) est prétassé".
  - The 022 brackets need "pré".
    - Bracket a) "∃t, f = ε_t ∗ f̌" is exactly the Cor of 020, "(f,f) prétassé ⟺ ∃s, f̌ = ε_s ∗ f". That is a
      statement about prétassé pairs, not tassé ones.
    - He first wrote "tassé" and corrected it by inserting "pré".
- **Witness H** reads "prétassés" and "tassés" at all these places. Its batch note says "pré" is added above "tassé" in
  the two brackets of 021, our 022.
  - The ink agrees with it at every one.
  - Its earlier readings "préférés" and "bornés", which Michel Hua's project itself withdrew, are excluded by the t.

## Consequence for the transcription

- The two notions of SA22-2 are named "couples prétassés" (§3) and "couples tassés" (§4). 015 already uses "tassé" for
  indicator functions.
- STUDY.md should replace two phrases:
  - "'Couples priorisés' (or 'tassés'; the reading is disputed)" becomes "couples prétassés" (§3);
  - "Couples bons" becomes "couples tassés" (§4).
- Thirteen corrections are in 68_images_CORRECTIONS.tsv.

**Not asked, noted once:**
- On 015 the abbreviation after "tassés" looks like "sss" (three alike s-strokes) rather than "ssi". It is left as the
  Pro text has it.
- In the 013 margin, "fini" is underlined and blotted, and witness H marks a struck word after it. The underline is
  clear; I see no struck word.

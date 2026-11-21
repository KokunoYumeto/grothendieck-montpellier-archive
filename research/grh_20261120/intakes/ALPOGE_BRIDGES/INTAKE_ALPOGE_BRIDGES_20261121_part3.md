# Intake of ALPOGE_BRIDGES (prompt 22), part 3: checkpoint 06, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); it writes "effort not exposed". It is still going. Part 2 read
checkpoint 05.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ALPOGE_BRIDGES_checkpoint_06_20261121T0331Z_unzipped`, made 03:31:48 UTC after
  270 min of work. It was the newest present.
- **Run status:** formal movement review 02 (03:04 UTC) found movement, with 0 consecutive reviews without movement.
- **Read:**
  - LEDGER.md lines 560-760: review 02, the movement note, and the full 101-row snapshot;
  - the changed QUESTIONS rows AQ-Q-SA08-CS, AQ-Q-SA08-TL, AQ-Q-136-STRICT, G-123-DISTINGUISHED, AQ-Q-15-*, AQ-Q-SA06-EFFECT
    and R-KGROUP;
  - in ALPOGE_BRIDGES.tex, AQ-136-SEMILOCAL (lines 4329-4420: the statement, step 1 and the statement of step 2), and
    CC-TATE01 and CC-TATE03 (lines 5725-5770 and 5872-5912).
- **New since checkpoint 05:**
  - AQ-136-SEMILOCAL;
  - CC-AG09-10;
  - CC-TATE01-04, which names the 2026 sources that part 2 asked for;
  - BR-EFF01-03 (cote 15 / SA06 effectivity);
  - KN-COMP01-04 (cote 18 comparisons);
  - F-SM-31 (refutes automatic AB5 and presentability);
  - an R-KGROUP update.
- **Unchanged rows:** AQ-136-STRICT, CC-APG01-11, the G-123 rows, BR-12302, F-SM-19 to F-SM-22. Nothing I checked in
  parts 1 and 2 is withdrawn or corrected.

## 1. Verdicts

| id | statement (short) | uses | verdict |
|---|---|---|---|
| AQ-136-SEMILOCAL | for every ring in which all but finitely many rational primes are units (R_P-algebras, P finite), the groupoid obtained by inverting every morphism of 𝒜_k is terminal. Conjecture (a)'s strict common source for \|P\| > 1, and Z itself, are not claimed | none | **step 1 confirmed; the rest statement level.** Step 1 is the arithmetic fracture sequence 0 → M → (⊕M_i) ⊕ M₀ → M₀^{⊕s} → 0. I checked it: ∩ Z_(p_i) = R_P; surjectivity by CRT on a common denominator; and flatness of Q^{⊕s} over R_P gives exactness for arbitrary M. Step 2, the rational tensor lemma with uniform weight bound (136.S2), and the gluing of the 414-line proof were not read in full. This is exactly the fracture-square attack proposed in part 2, §4.1, carried out for finitely many primes. |
| CC-TATE01-03 | cited 2026 inputs: van Hoften-Sempliner, *The Hodge Conjecture for CM abelian varieties*, Hexagon 2610.00259v2, Thm I; Milne, note of 9 Nov 2026, Hexagon 2611.00244v1; *Milne's rationality conjecture*, Hexagon 2610.00226v1 (contributor K. Madapusi, byline "ChatGPT and Claude"), Thm 1.1, Cor 6.2 | cited, external | **source identification accepted.** This answers part 2's request. These are external preprints, carried as cited inputs. Our runs did not verify them, and the run says it read their surface criterion and final argument but not every dependency. **Scope flag for our tables:** everything downstream (CC-TATE02, CC-TATE04, G-STD-HDG "proved in the abelian sector", AQ-Q-15-*, AQ-Q-SA06-EFFECT's abelian cone) is conditional on these unrefereed 2026 preprints. That is neither A_D nor M, and it should be tagged so. |
| CC-AG09-10 | the rational essential image of base-field extension in the abelian sector: an orbit/index multiplicity monoid; rational essential surjectivity fails (the rank-one sign object over F_{q²} would need α² = −1 in Q) | the CC-TATE inputs | statement level. The failure example is right. |
| BR-EFF01-03 | universal spectral integrality implies effectivity iff full Tate; Frobenius-one effectivity suffices; the abelian effective cone has an exact p-slope test | the CC-TATE inputs for the abelian part | statement level. |
| KN-COMP01-04 | cote 18 (physical p. 43, footer 42) comparison questions answered by known theorems (Grothendieck 1966 Thm 1′; SGA 4 XVI 4.1; Bhatt-Morrow-Scholze Thms 1.7-1.8; Bhatt-de Jong) | none | statement level; correct attributions in form. |
| F-SM-31 | automatic AB5 or presentability fails, but the localization conclusion holds in the example | none | statement level. |
| R-KGROUP update | K_{2n}(Z)/p equals the ω^{−n} cyclotomic class-group component; K₈(Z) = 0 cited as a 2026 theorem; Alpöge's footnote exports no degree-indexed theorem | cited | statement level. "K₈(Z) = 0" is a cited 2026 result and should be tagged as such. |

**Counts for part 3.**
- Confirmed with every step checked: 1 (AQ-136-SEMILOCAL step 1).
- Source identification accepted: CC-TATE01-03.
- Statement level, no fault found: about 12 ids.
- Gaps: 0. Refuted: 0. Changes to parts 1-2: none.

## 2. What is new

- **Cote 136:** terminality (the groupoid form of (b)) now holds over every ring with finitely many non-invertible primes,
  by arithmetic gluing. The only cases left are Z, and rings with infinitely many non-unit primes. The step from P finite
  to Z is a limit over P: it needs the weight cutoffs to stay uniform as P grows. Step 2's bound (136.S2) depends on
  max N_i and Σ N_i, which grow with P.
- **Cote 15 and SA06:** the abelian sector is closed, conditionally on the 2026 CM-Hodge preprints. These preprints are
  the most consequential external input in the run, and they now carry a scope tag.

## 3. The scope of the two proofs

Nothing new uses A_D or M. The new external dependency is the 2026 preprints of CC-TATE01-03, which need their own tag in
our scope tables ("cited 2026 preprint, unverified by us"). No statement claims more than its inputs give.

## 4. Integration, with the attack each opens

1. **SA08 intake, row A-TL:** "terminality proved over every ring with finitely many nonunit primes (AQ-136-SEMILOCAL);
   open over Z".
   - Attack on Z: the obstruction is uniformity of the weight cutoff in P. Look for sources with a fixed weight bound
     for all p at once, or prove that the uniform bounds (136.3)-(136.4) must fail over Z. The latter would be a
     refutation of terminality over Z, and the run's five failed integral constructions (part 2) suggest it is worth
     testing.
2. **Scope tables (all intakes):** add a fourth input class, "cited 2026 preprints (van Hoften-Sempliner 2610.00259v2;
   Madapusi 2610.00226v1; Milne 2611.00244v1)", for G-STD-HDG, the abelian AQ-Q-15 rows and BR-EFF.
3. **Cote 18:** the KN-COMP answers go into the cote 18 notes as known comparisons.

## 5. Prompt updates

- Make Z for cote 136 (a) and terminality the main question, with the uniformity-in-P obstruction named.
- Ask the run to tag the CC-TATE-dependent rows with their preprint input.

## 6. Hexagon candidates

- **The cote 123 letter with CC-APG04:** unchanged by checkpoint 06; the run's G-123 rows are identical to checkpoint 05.
  **Gates left:** a literature search (Kostant 1959 and 2010, Steinberg 1965 §9, Brieskorn 1970, Slodowy 1980) and a
  check of CC-AP04-05, which the A_{2m} converse rests on.
- **H07 = A05 and the factoring reduction:** not in this run; unchanged.
- **AQ-136-STRICT and SEMILOCAL:** still best posted with the Z case; not ready.

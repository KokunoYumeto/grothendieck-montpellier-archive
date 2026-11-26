# Deposit sheet

## Title

Thakur’s descent bound and Grothendieck’s finite-field realization question

Subtitle: An abelian threefold, Kummer surfaces, and cubic fourfolds

The author line is intentionally empty.

## Abstract

Thakur's Proposition 2.9 in arXiv:2001.00210v1 proposes that the class number of an imaginary quadratic endomorphism center bounds the field needed to define a geometric isogeny class. We give a counterexample and determine its minimum field exactly. The Weil 512-number 12−4√−23 defines a geometrically simple abelian threefold. Its geometric isogeny class has a representative over F_(2^e) exactly when 9 divides e, although the center has class number 3. Honda–Tate theory gives the threefold and its endomorphism division algebra; a reduced norm, an ideal class, and the local division algebra exclude smaller fields, including models whose Frobenius is not initially central. We also give the exact minimum for models with central Frobenius over any CM center, in terms of an ideal class and a unit-norm obstruction. This is the full minimum when the geometric endomorphism algebra is commutative. In the imaginary quadratic case we recover the sufficient class-number times Brauer-index bound from Thakur’s earlier construction. A finite polynomial procedure determines the minimum exponent for any given abelian variety. A companion section gives explicit Chow retractions for Kummer surfaces and separated cubic fourfolds, and constructs abelian targets for ordinary K3 surfaces and cubic fourfolds. For the latter, the missing comparison correspondence is characterized by a specific mixed Tate condition. These results concern concrete aspects of Grothendieck’s finite-field notes; they do not decide his broader existence conjecture. GPT-6 Astra (ChatGPT Pro mode) produced the text and mathematics and performed the same-model checks; no human has checked them.

## Subject and keywords

Mathematics Subject Classification: 14K02 (isogenies), 14K15 (arithmetic of abelian varieties), 11G10 (abelian varieties of dimension greater than one); 14C15 (Chow groups and rings); 14J28 (K3 surfaces); 14J35 (fourfolds).

Keywords: finite fields; abelian threefold; Honda–Tate theory; geometric isogeny class; field of definition; ideal class group; Brauer index; Frobenius; Grothendieck’s motives; Kummer surfaces; cubic fourfolds; Chow correspondences; Tate conjecture; ordinary varieties.

## Main results and scope

- Theorem 1.1 constructs the specified threefold, verifies geometric simplicity and the geometric division algebra, and proves the exact field criterion 9 | e.
- Proposition 5.1 computes the exact minimum exponent dt/gcd(t,2j−d) for central Frobenius models with imaginary quadratic geometric center and split characteristic prime.
- Proposition 5.2 gives the exact central minimum ats for a CM center, with a the integral slope denominator, t the associated ideal-class order, and s∈{1,2} the unit-norm obstruction. When the geometric endomorphism algebra is commutative, this is the unrestricted minimum. It gives the sufficient bound 2h_K d lcm(f_v); sharpness is not asserted.
- The sufficient bound h_K d is attributed to the construction in Thakur (2020), Proposition 2.4, pp. 4–5; the threefold attains it.
- The counterexample refers exactly to Proposition 2.9 of arXiv:2001.00210v1, p. 6. The arXiv page lists no later version as of 23 November 2026. IACR ePrint metadata lists a later minor revision, whose PDF could not be inspected because access returned HTTP 403; no assertion is made about its text.
- Proposition 6.1 gives a finite exact computation of the minimum exponent from a Frobenius polynomial. It is a transparent variant of established Weil-polynomial enumeration and geometric-isogeny tests, credited to Dupuy, Kedlaya, Roe, and Vincent (2020), §§3.1 and 3.4, pp. 12–15. It makes no newness claim.
- Theorem 1.2 and Section 7 give the full companion statements: rational Chow retractions for Kummer surfaces and separated cubic fourfolds; finite-field descent using Weil restriction and trace; a necessary and sufficient mixed Tate condition for comparison with a specified abelian target; and a published-input target construction for ordinary K3 surfaces and ordinary cubic fourfolds in every characteristic.
- The geometric retractions hold in Chow motives. The general target comparison and the algebraic idempotents constructed from endomorphism algebras are asserted only modulo homological equivalence, uniformly for all primes different from the characteristic. No Chow idempotent lifting theorem is assumed.
- The mixed condition for arbitrary ordinary K3 surfaces or ordinary cubic fourfolds is left explicit and is not inferred from Tate for their self-products.
- A universal sharp formula in class numbers and Brauer indices for arbitrary centers remains unresolved here. Grothendieck's broader existence conjecture is not refuted or proved.

## The eight opening requirements

| Requirement | Place in the paper |
|---|---|
| Title names the question and source | Title: Thakur’s descent bound and Grothendieck’s finite-field realization question |
| Abstract begins with source and ends with method/checking disclosure | Abstract, first and last sentences |
| Full main theorem and its meaning | Section 1, Theorems 1.1 and 1.2 and their explanatory paragraphs |
| Why the result matters | Section 1 opening: ideal classes do not preserve slope and division-algebra data |
| Credit separated precisely | Section 1: Thakur’s Definitions 2.1/2.3 and Propositions 2.4/2.9, plus Shioda–Katsura and Milne; Sections 3 and 7: exact ingredients and primary locators |
| Literature and ingredients compared | Sections 1 and 5: Honda–Tate, Thakur’s construction, Grothendieck’s manuscript; Section 7: Shioda–Katsura, Milne, modern K3/cubic Tate theorems and the remaining mixed condition |
| Scope stated together | Section 1 after the main theorems, Section 7.5, and Section 8 |
| Proof overview before proofs | Section 2, headed “Proof overview” |

## Method note

GPT-6 Astra (ChatGPT Pro mode) produced the mathematics and text. The concrete threefold and its failure of descent to F₈ were re-proved from the statement before comparison with earlier arguments, and the full argument was subsequently checked by the same model. The exact minimum exponent was also separately re-proved from its statement by the same model, and the full argument received a further targeted same-model review. The general CM central-minimum formula, Kummer and separated-cubic retractions, mixed correspondence criterion, and weight-two slope-pattern proposition were each separately re-proved from their statements by the same model before comparison with the written proofs. The companion results also received targeted proof reviews, including finite-field descent and the ordinary-target application. These are same-model checks, not independent human verification. No human has checked this paper. The text is dedicated to the public domain under CC0 1.0. Sources, checks, and editable material are associated with https://github.com/KokunoYumeto/algebraic-groups-and-representations-workbench; the permanent address for its records is https://github.com/KokunoYumeto/mathematics-workbenches.

## Authors whose work carries the argument

- Alexander Grothendieck: finite-field motive questions, cote 15, especially scans 100–106.
- Taira Honda and John Tate: classification, endomorphism invariants, and dimension formula; Tate (1971), Theorem 1 and Remark 2, p. 96.
- Steve Thakur: Proposition 2.9 is the precise statement contradicted; Proposition 2.4 contains the sufficient-exponent construction credited here. The source is by Steve Thakur, not D. Thakur.
- James S. Milne: cited exposition of Minkowski's ideal-class bound, Theorem 4.3, p. 70.
- The Stacks Project Authors: maximal-subfield dimension formula, Tag 074W.
- Taylor Dupuy, Kiran S. Kedlaya, David Roe, and Christelle Vincent: established Weil-polynomial enumeration and geometric-isogeny algorithms, §§3.1 and 3.4, pp. 12–15.

- Tetsuji Shioda and Toshiyuki Katsura: classical join construction, Remark 1.10, p. 102.
- Daniel Huybrechts: Kummer construction and the K3 height/Newton polygon relation, Chapter 1, Example 1.3(iii), and Chapter 18, sections 3.2–3.3.
- Qingyuan Jiang and Bjorn Poonen: blowup motives, Weil restriction, and split cubic-surface geometry, at the locators in the references.
- James S. Milne: all-powers Tate for elliptic products and the degree-one slope-zero case, Appendix A.7, pp. 158–159 of the 2001 paper.
- Kazuhiro Ito, Tetsushi Ito, Teruhisa Koshikawa, Yuri G. Zarhin, Keerthi Madapusi Pera, Asher Auel, Avinash Kulkarni, Jack Petok, and Jonah Weinbaum: the exact K3/cubic Tate, semisimplicity, and ordinary-slope inputs identified in Section 7.

No authors have been contacted, and no publication or upload has been performed.

# √3 against 3 on 67/098: his slip

Piece of horizontal sweep 2, part 2. Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026. Topic SA22, item
SA22-9 ("Courbes elliptiques réelles", dated Déc 83, cote 67, scans 091–101).

## What his pages say

The page is cote 67, scan 098 (67.pdf page 98; crops `img/67_098_formula.png` and `img/67_098_n6b.png`).
- Under "3) Cas hexagonal n = 6" he writes a = Q(2v−u)/Q(u) = √3. The radical over the 3 is clear on the scan image.
- He uses the same value twice more on the page:
  - "Réflexions-faces … on trouve donc E′_{1/a} = E′_{1/√3}";
  - in "En résumé", the insertion "avec a = √3" above "deuxième cas".
- The square case just above has a′ = Q(e₀−e₁)/Q(e₀+e₁) = 1.
- On 099 the period parameters are √a·i and (1 + √a·i)/2. This comes from Pro's research lead; the image of 099 was
  not opened.

## What our notes say

- Pro's note E15 (`MPL_67_053-101#85`) is headed "67/98, hexagonal quadratic ratio; compare 99".
- Pro's research lead says: "Hexagonal calculation gives quadratic-form quotient sqrt3; with Q quadratic and angle 60
  degrees the ratio should be 3", and on 099 that this reinforces "the hexagonal sqrt3 inconsistency".

## The check

- **The computation.** Take u, v unit vectors at 60°. Then Q(2v−u) = 4 − 4·½ + 1 = 3 = 3·Q(u). The vector 2v−u is
  orthogonal to u, so u and 2v−u span the rectangular sublattice of index 2.
- **The parametrization.** In the form (1 + √a·i)/2 used on 099, the hexagonal lattice is (1 + √3·i)/2, so a = 3.
- **What a measures.** a is the ratio of quadratic-form values, not of lengths: a ratio of lengths would be √3.

## What depends on it

- In SA22-9 the parameter a labels the real forms E_a and E′_a, and the face reflections give E′_{1/a}.
- So the hexagonal case is E′_{1/3}, not E′_{1/√3}.
- The two-orbit classification of real forms is not affected: on 098 "le cas hexagonal" falls in the second case
  either way.

## Correction

- **The reading:** he wrote √3 (decided on the scan image), so this is his slip, not a misreading.
- **The corrected values:** a = 3 in the hexagonal case, so E′_{1/a} = E′_{1/3}.
- **Where it is recorded:** `SA22/CORRECTIONS.tsv` and `SA22/CLAIM_LINKS.tsv`, with check events in
  `SA22/CHECK_EVENTS.tsv`.
- **For part 3:** the companion should state the hexagonal case with a = 3 and keep his √3 as a footnoted slip.

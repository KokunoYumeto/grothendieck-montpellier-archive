# Sweep 2, part 2: check-in of agent ae4ae3dc (Claude Opus 5.5 at effort max), 22:11 UTC, 18 Nov 2026

Topics SA28, SA29, SA30, SA31, SA20 and SA22.

## Files written

**In each `sweep2/SA<nn>/`:**
- `DEPENDS.tsv`: for each item, what it uses and what uses it, with the basis.
  - The basis is his pages, our reading, or our notes. Our notes' scan citations are kept apart as "cites / cited by",
    so they are not mistaken for dependencies.
- `CLAIM_LINKS.tsv`: each claim of his linked to research-run statements at the same place, or to a check.
  - The claims are the entries of kind unproved claim, conjecture, or withdrawn in the same text.
  - A locator match is marked "not read". Curated links are marked "read".
- `UNIT_LINKS.tsv`: each item linked to the companion units of `UNITS_DRAFT_20261118.tsv`.
  - Only cote 123 and 125 have units: 40 links in SA20. Every other item says that the draft has no unit for its cotes.
- `CORRECTIONS.tsv`: the corrections and refinements, the open reading flags, and the second-pass corrections of the
  notes (from `sweep1` check events).
- `WHAT_IS_WHERE.md`: the topic's items in mathematical order. Each gives where it is, its status, its dependencies,
  its claims against the register, its flags, its corrections and its global tag.

**In `sweep2/REPORTS/`:**
- `char5_67_086.md`
- `hexagonal_ratio_67_098.md`
- `date_of_cote_67.md`
- `letter_to_kostant_123.md`
- `ctrl145_group_symbol.md`
- `H0HW_five_point_inputs_ae4ae3dc.md`, for the broad agent
- `img/`: 18 crops of the scan images on which the readings were decided

**Placement changes:**
- SA20: the 13 Work units of K123-02 and K123-03 moved from SA20-W1 to SA20-W3, to match the companion units.
- SA22: SA22-3's object now carries the title-sheet date as read.
- H0HW tags were added to SA22-7, SA29-Q1, SA30-6, SA31-5 and SA31-Q1.

## Counts

| Topic | Items | DEPENDS (uses / used by / cites / cited by) | Claims | Register links | Units | Corrections |
|---|---:|---|---:|---|---:|---|
| SA28 | 32 | 18 / 15 / 0 / 0 | 217 | Proved 1, Refuted 1, flagged 2, checked 1 | 0 | 57 (45 second pass, 9 flags, 3 control-run) |
| SA29 | 25 | 13 / 10 / 0 / 0 | 88 | checked 1 | 0 | 34 (30 second pass, 4 flags) |
| SA30 | 21 | 15 / 18 / 9 / 9 | 219 | Proved 39, checked 2 | 0 | 21 (18 second pass, 3 flags) |
| SA31 | 19 | 18 / 21 / 25 / 26 | 280 | Proved 134, Refuted 80, Known 19, Open 15 | 0 | 15 (11 second pass, 3 flags, 1 decided) |
| SA20 | 23 | 10 / 10 / 7 / 6 | 130 | Known 3, his claim 1, checked 1 | 40 | 14 (12 second pass, 2 refinements) |
| SA22 | 15 | 9 / 9 / 8 / 8 | 72 | refuted 2 (both by my computation) | 0 | 7 (5 corrections and refinements, 2 flags) |

**New check events: 11.** Ten readings were decided on the scan images, and the octa.py computation (p = 3 to 29) is
recorded with the 67/086 reading.

| Topic | Events |
|---|---:|
| SA22 | 5 |
| SA20 | 2 |
| SA28 | 2 |
| SA31 | 1 |
| SA29 | 1 |

## The five pieces, decided on the scan images

1. **Characteristic 5 (67/086).** The hypothesis reads "de car. ≠ 2".
   - In characteristic 5 the octahedral six points are P¹(F₅), and five Klein four-groups (and five octahedral groups)
     share them. The Proposition fails.
   - It holds in every other odd characteristic. Computation: for p = 3, 7, …, 29 the stabilizer has order 24 and one V
     has the set; for p = 5 the stabilizer has order 120 and five V do.
   - My argument covers all other characteristics: the stabilizer has order dividing 720, which is prime to p for
     p ≥ 7.
2. **√3 against 3 (67/098).** He wrote √3, three times; the radical is clear on the image.
   - The quotient is 3, and the periods on 099 need a = 3. It is his slip, so the hexagonal case is E′_{1/3}.
3. **The date of cote 67.**
   - The title sheet reads "(1976 ou 77 ?)": the fourth digit is his 6, not 8.
   - Envelope 014 carries a Nagoya University meter stamp of 20.12.77.
   - The dated sheets of the second layer are "Déc 83" (091), "1?.1.84" (054; the day 11 or 16), "15. 1." (048) and
     15.4.1984 (the letter to Bers).
   - So the folder holds 1976–78 sheets as well as Dec 1983 – Apr 1984 ones; the catalogue's 1983–84 fits the second
     layer only.
4. **The letter to Kostant (123/022–023).** "Massy 22. 10. 1969".
   - It counts the quadruples (T, B, T′, B′) as card(W)²/(h z φ(h)), and asks about the rank of the tangent map at
     subregular orbits.
   - It expects dimension i for the Borels through an element of an orbit of dimension 2N − 2i. That is Steinberg's
     1976 formula (from memory).
   - It ties these to rational singularities by a depth argument of Brieskorn.
   - Refinement: his guess that a single subregular orbit characterizes the simply-laced case fails, because the
     subregular class is unique in every type (from memory).
5. **CTRL-145 against CTRL-145_2 (145/023–033).** The symbol is a script E, as CTRL-145 and Pro read it.
   - CTRL-145_2's Σ is a misreading.

**For the broad agent (H0HW):**
- 148/033 decided on the image: fourteen named families, and sixteen S₅-orbits by the margin's own sum
  1620 = 5×60 + 11×120.
- Pro's note "fourteen stated arrow orbits" counts families; corrected in `SA31/CORRECTIONS.tsv`.
- The register agrees: EXIT_TOWER B.12 is proved and LM4_SUCCESSOR E.38 refuted.
- Everything else is in `REPORTS/H0HW_five_point_inputs_ae4ae3dc.md`.

## Other findings from the claim links

The register refutes statements placed on his pages:
- 149/032, Théorème 3 in characteristic p (ANABELIAN_A1 C.2);
- 148/035, his inference that a finite antiholomorphic automorphism preserving five marks has order two (LM4_SUCCESSOR
  E.32);
- 149/119–135 (FLAGGED_149: D6, D7, D9, ZD4–ZD7, E2, E5, E6), including the self-normalization and centralizer
  assertions and the π₂ boundary map;
- 143/031 (EXIT_TOWER E.T2).

These links are by locator. Part 3 should read each statement against his page.

## Objects that cross topics

- SA20-W3 (filtrations of the forgetful functor) links to SA20-17 (= H00O) and to Saavedra on cote 66 (SA22-0).
- SA22-8 (M₀,₄ and the octahedron) links to SA30-2, SA28-15, SA29-18, SA30-7 and SA20-5.
- SA22-13 (the 1977 elliptic envelopes) links to SA22-9, SA29-7 and SA29-17.
- SA31-1 is used by SA30-17 (the structure at infinity continues) and by SA31-6 (générisation, 148/054).
- The H0HW items are SA31-5, SA31-Q1, SA30-6, SA30-7, SA29-18, SA29-Q1, SA22-7 and SA31-6.

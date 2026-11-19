# SA31: Autour de La Longue Marche, part 4 (cotes 147/138–190, 148/029–072, 149/001–136): topic notes, horizontal sweep 1

By Claude Opus 5.5 at effort max (agent ae4ae3dc), 18 Nov 2026.
- **The notes:** Pro's, by GPT-6 Astra (ChatGPT Pro mode).
- **The second pass:** by Claude Opus 5.5 at effort max, on 148/029–072 and both 149 packages. It does not cover
  147/138–190.
- **There are no Work math notes for this topic.**

## What the notes cover

607 entries in four packages. They fall into 19 items, 5 of them the prompted questions. Many headings here are bare
locators ("Scan 138, l. 13 — reading question"). I placed those items from the openings of the entries, which I read in
a sample of about one entry in five for 149 and all of them for 147/138–176. Their basis is still recorded as index-row.

**Cote 147, scans 138–190 (136 entries):** the end of "Structure à l'infini".
- generization morphisms and punctured normal bundles (SA31-1);
- his gluing theorem, the "Th de recollement" for the structure at infinity, with Π₁(X) as an amalgamated sum in the
  curve case (SA31-2);
- the elementary punctured-neighbourhood topoi of normal crossings, with the conormal filtration and twisted tori
  (SA31-3);
- asphericity, exit paths and tubular fibrations (SA31-4).

**Cote 148, scans 029–072 (66 entries):**
- the five-point diagram: nine object orbits under Aut⁺ of order 120, 542 objects, 1620 arrows, and the problem
  "déterminer un syst. fondamental de relations entre les 1620 flèches" (SA31-5, SA31-Q1);
- marked surfaces and operations on marks: erasure, surmarking, cutting and gluing marked circles, a preliminary
  dévissage theorem (SA31-6).

**Cote 149, "[Autour de La Longue Marche]", scans 001–136 (405 entries):**
- the fundamental group of a field of finite type and its reconstruction, with Théorèmes 1 and 2 (SA31-7);
- points and sections, with P = Q from prime-to-p covers (SA31-8);
- the section conjecture over finitely generated fields: packets of sections, Conjectures B and B′ (SA31-9);
- extending sections across the boundary: the intersection multiplicity μ, the π₂ condition, "une histoire
  d'ombres" (SA31-10);
- local sections and good reduction (SA31-11);
- models, decomposition groups and the extensions E (SA31-12);
- the maquette of a normal-crossings compactification (SA31-13).

**Heavy and light:**
- The heavy items are SA31-12 (88), SA31-8 (65), SA31-9 (63), SA31-10 (60) and SA31-7 (59).
- The light ones are the prompted questions and SA31-5 (14).

## Counts

| | |
|---|---|
| Entries | 607 (Pro); no Work units |
| Items | 19: 14 objects and 5 prompted questions |
| Basis | 605 index-row, 2 entry-read; no passage reads (my budget for this topic went to placement) |
| Second pass on 148/029–072 | 14 corrected, 43 kept |
| Second pass on 149/001–090 | 255 verdicts, in a format my parser could not classify; the text of each is in `CHECK_EVENTS.tsv` |
| Second pass on 149/091–136 | 22 verdicts: 1 dropped, 3 kept, 18 unclassified |
| Flags | 7 |
| Check events | 311: 1 mine, the rest the second pass's |

## The flags that matter

1. **The five-point problem is stated here** (SA31-Q1, SA31-5). On 148/031–034 the task is to find a fundamental system
   of relations among the 1620 arrows of a diagram with 542 objects.
   - The objects come in nine orbits of sizes 120/i: 62 + 240 + 240 = 542 (rechecked).
   - The first row (12, 20, 30) gives the 62 cells of the dodecahedron of 146/077 (SA30-7).
   - It is the same object as the five-point boundary of 147/066–068 (SA30-6). It is also the object whose absence the
     notes on 143, 144, 145 and 148/001–028 record.
2. **Fourteen or sixteen orbits.** The note says "fourteen stated arrow orbits". Two research runs that read the
   original scan (EXIT_TOWER B.12, LM4_SUCCESSOR E.38; links only) find the word "orbites" after "14" struck out and
   count sixteen S₅-orbits in fourteen named families. To decide on our scans.
3. **His good-reduction conjecture.** On 149/100 he conjectures a Galois-theoretic good-reduction criterion. According
   to the note it is a later theorem for hyperbolic curves (Oda, Tamagawa); I have not read the entry.
4. **The second-pass corrections on 148:** 14 of 57 notes.
5. **The LM lens.** 438 of 607 notes compare with La Longue Marche. In 148/029–072, 59 cite research-run ids and the
   five prompted questions are asked again.

## Objects that cross into other topics

- the five-point diagram (SA31-5): to SA30-6/7, SA29-18 (148/024) and SA28 (143);
- the structure at infinity and the gluing theorem (SA31-1 to SA31-4): to SA30-15/17 (147/003–137);
- the reconstruction of fields and the section conjecture (SA31-7, SA31-9): to SA28-13, SA28-17 (142, 143);
- the maquette and μ (SA31-13, SA31-10): to SA29-Q4, SA29-Q5.

## What sweep 2 should look at first

1. One global object for the five-point diagram and boundary, taking in SA31-5, SA30-6, SA30-7 and SA29-18. Its
   counts are now checked on three pages (542, 62, 10/15, genus 6).
2. The second pass's verdict lines for 149/001–090 (255) need a parser for their format. Their content is already in
   `CHECK_EVENTS.tsv`.
3. SA31-9, his section conjecture with its packets and Conjectures B and B′, read in its own terms before any
   comparison with later theorems.

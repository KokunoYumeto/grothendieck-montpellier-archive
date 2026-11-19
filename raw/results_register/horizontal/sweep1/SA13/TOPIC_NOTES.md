# SA13: Séminaire de Géométrie Algébrique (SGA), horizontal sweep 1

This placement was done by Claude Opus 5.5 at effort max, sub-agent of a0c4bb37 for SA13, on 18 Nov 2026 (about 14:40-15:00 UTC).

## What the notes cover

**Heavy: four Pro packages, 379 index entries.** These are the notes and doubts of GPT-6 Astra (ChatGPT Pro mode).

| Package | Cote and scans | Entries |
|---|---|---:|
| MPL_33_098-146 | 33 (SGA 5 1965 MS brouillon), scans 98-146 | 70 |
| MPL_33_147-181+34_002-017 | 33, scans 147-181; 34 (SGA 7), scans 3-17 | 113 |
| MPL_36_002-052 | 36 (SGA 7 "ma part"), scans 3-8 and 28-52 | 93 |
| MPL_36_053-085+39 | 36, scans 53-85; 39 ("Fonctions et structures élémentaires"), scans 3-20 | 103 |

**Light: 28 Work and Codex-web math-notes files, 169 units.**
- Cote 27: K27-01 to K27-03.
- Cote 28: K28-01.
- Cote 32: K32-01 to K32-03.
- Cote 34: K34-01 to K34-12, plus K34-02_2, a second run on the same scans 34-49.
- Cote 35: K35-01.
- Cote 37: K37-01 to K37-03.
- Cote 40: K40-01 and K40-02.
- Cote 41: K41-01.
- Cote 42: K42-01.

The model of each Work run is named in its own folder; this sweep did not re-read it.

**Also placed: the Codex transcription notes in `inputs/SA13/codex/`, 28 units.** They cover K34-01 to K34-12 and A36-01/A36-02 (cote 36, scans 10-27). They are not in the index; their ids are `codex:<folder>#<n>`.

**Unit convention for Work and Codex files.** The units are the section headings after the file's title line, numbered in order:
- most Work files have six units: What the pages do, Statements left without proof, Questions and conjectures, Slips, Pointers, Remarks of the model;
- K32-02 has a seventh: "Reading questions noticed after the final hashes";
- in files without a title line, the `#` headings are the units.

**Scan coverage.** No Pro package and no Work folder cover the same scans:
- Pro has cote 34 scans 3-17; Work has scans 18-210;
- cote 36 scans 10-27 are only in A36-01/02.

The one same-pages pair is K34-02 and K34-02_2.

## Main objects and clusters (73 items)

68 items are mathematical objects or reused sources; 5 are source accounting (SA13-90 to 94).

**Cote 33 (SGA 5 draft): items SA13-1 to 8 and 15 to 20.**
- The six operations under duality.
- Derived tensor product and Tor-dimension.
- The projection formula for Rf_!.
- Künneth, proper and nonproper, including the characteristic-p failure.
- The Lefschetz fixed-point programme and rationality of L-functions.
- The Lefschetz-Verdier pairing: cohomological correspondences, local terms, the symmetry sign.
- Traces over Z/l^n and passage to l-adic coefficients.
- Euler characteristics and ramification.
- Local Künneth.
- External products of dualizing complexes.
- Biduality and the "plausible" anti-equivalences.
- Injective dimension (pseudo-injective sheaves, Gorenstein rings, the 2n bound).
- Supported spectral sequences.
- His research lists.

**Cote 33, reused typescripts, not his SGA text: SA13-9, 11, 12, 13.**
- A ramification typescript (normalization, quadratic transforms).
- An axiomatic étale-topos typescript.
- An analytic operator sheet.
- Editorial remarks on a topological-vector-spaces typescript.

**Cote 34 (SGA 7): SA13-21 to 33.** Scans 3-210 read as one long manuscript sequence:
- Tate modules over local fields;
- the quartic Picard assertion;
- tame inertia and its cyclotomic twist;
- henselian valuations;
- the local monodromy theorem (quasi-unipotence);
- §§7-9;
- monodromy of abelian schemes ("Exposé II");
- nearby and vanishing cycles;
- tame nearby cycles along normal crossings;
- local Lefschetz and depth;
- the fundamental group;
- analytic envelopes of profinite groups;
- l-adic representations and the Tate conjectures.

**Cote 36 (SGA 7 "ma part"): SA13-34 to 50 and 69.**
- His editorial remarks on the SGA 7 IX draft: henselian base, isogeny, semistable reduction, the filtration of the Tate module, "6.3 est faux".
- The pairing on component groups and its comparison with Artin-Mazur.
- Biextensions.
- Torsion pairings.
- Picard-Albanese duality.
- Cartier duality in characteristic p.
- Reconstruction from torsion.
- Rigidity of torsors.
- Quotients by group actions.
- Vertical divisors and the integral defect.
- Index and the Brauer obstruction.
- The orthogonality theorem.
- "Le théorème de Griffiths par voie algébrique".
- Reused typescripts: Haar measure, Lie algebras.

**Cote 39: SA13-51 to 55.**
- Classes of "elementary" functions closed under implicit functions.
- Closure under flows and the Pfaff converse.
- Faithful flatness.
- Formal structures and quotients.
- Weierstrass division and preparation.

**Work-only cotes: SA13-56 to 68.**
- Cotes 27-28: SGA 3 complements (tori, multiplicative type, nil-spaces, "théorème de 1/2 continuité", reflections).
- Cote 32: correction slips.
- Cote 35: the SGA 7 plan.
- Cote 37: reedition planning and topos additions.
- Cote 40: alpha_p-torsors and p-th-root covers.
- Cote 41: construction of étale morphisms.
- Cote 42: networks of local rings.

## Counts

| Measure | Count |
|---|---|
| Entries | 576: 379 Pro, 169 Work, 28 Codex |
| Items | 73 |
| Basis | index-row 554, entry-read 14, passage-read 8 |
| Fidelity of the passage-read entries | agrees 7, overstates 1 (568 not checked) |
| Flags | 15: suspected misreading 3, note overstates the page 1, same thing with different readings 1, links across folders 10 |
| Check events | 12 |

What the basis column means:
- For Pro entries, "index-row" means the index heading plus the scans parsed from the entry's own metadata line.
- For Work and Codex units, it means the unit heading, the bold leads and the parsed scans.
- `his_term` for unread entries is the first quotation in the note, extracted by script; it has not been checked.

**Lenses.** No SA13 note reads the topic through La Longue Marche or Les Dérivateurs: 0 mentions in all notes. MPL_36_053-085+39 cites Michel Hua's AI-produced findings register 90 times as context, and MPL_36_002-052 5 times. This is recorded as a link.

## What I checked, and what it showed

**M07 and M08, cote 34 scans 5-6.**
- The page states Z ≃ Pic(P^3) → Pic(X_0) for "une surface de degré ≥4" with no genericity hypothesis. The note reports this faithfully.
- The note's Fermat-quartic counterexample is valid.
- As read, the statement is false, so the scan should be checked for an omitted word.

**N54, cote 33 scan 145 (typescript).** Lemme 4(c) as transcribed equates "κ(y) finite separable" with "m_y = m_xO_y and …". The dual-number counterexample is valid, and the note agrees with the page. The text was probably meant as O_y/m_xO_y.

**N16, cote 33 scan 118.** The Künneth failure with Z/p coefficients in characteristic p is on the page. The note's Artin-Schreier example is valid.

**N20, cote 36 scan 6.** The note quotes "6.3 est faux" as certain; the transcription has \unsure{6.3|63}. This overstates the reading.

**N94, cote 39 scan 20.** The note agrees with the page. But the subscript of α (\unsure{a_{N+1}|a_{N-1}}) fits neither reading: the argument needs a_N or the unit series U̇.

**R08 (33/155) and M12 (34/9).** Both agree with the pages.

**K34-02 and K34-02_2.** The two notes agree statement by statement and slip by slip. They differ only in the confidence given at scans 41 and 46.

## What sweep 2 should look at first

1. **Decide the four flagged readings on the scans:**
   - 34/5-6, the missing genericity;
   - 39/20, the subscript of α;
   - 36/6, "6.3" or "63";
   - 33/145, Lemme 4(c).
2. **Name the current note of the K34-02 pair** in the register.
3. **Read cote 34 as one manuscript.** The Pro M-entries (scans 3-17) and K34-01 (scans 18-33) are consecutive. Check the tame-inertia claims (M13-M16, M25-M27) and the local monodromy theorem against the pages.
4. **Check the notes' own counterexamples by computation.** Each is a claim that can be checked by computation:
   - MPL_33_098-146: N10, N25, N54;
   - MPL_33_147-181+34_002-017: D24, D30, D33, D36, M27, R09;
   - MPL_36_002-052: N21, N35, N52, N54;
   - MPL_36_053-085+39: N09, N13, N20, N25, N55, N76, N81.
5. **Check cote 36's self-flagged comparisons on the pages:** Artin-Mazur (N05), the sign (N26), and the trace/contragredient correction (N12).
6. **Identify the reused typescripts.** These are not his SGA mathematics:
   - cote 33: topological vector spaces, ramification, analytic operators, the étale topos;
   - cote 36: Haar measure, Lie algebras.
7. **Split the coarse Work units.** "Statements left without proof" and "Remarks of the model" carry many statements each; split them into statement-level entries.

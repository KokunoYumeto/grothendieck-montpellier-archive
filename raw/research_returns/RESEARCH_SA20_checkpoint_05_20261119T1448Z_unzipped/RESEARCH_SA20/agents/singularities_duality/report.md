# Part C working report — 2026-11-19 12:32 UTC

**Part C is not complete: C.2(b) has two original-source access gates.** The checked file contains 22 proved, refuted, or precisely qualified results, with no theorem inferred from an unread original article.

## Task and lead status

| Task | State | Checked results and exact qualification |
|---|---|---|
| C.1(a) | Proved; uniqueness refuted | C.001–C.003: exact lift ambiguity and canonical geometric variation. |
| C.1(b) | Proved | C.007: degree-i transpose sign, middle sign, fully specified Seifert/variation matrices. |
| C.1(c) | Known, derived from opened sources; overstatement refuted | C.008–C.009: tame invariants, canonical twist (−n)[−2n], extra tame-invariant twist (−1)[−1], and explicit wild example. |
| C.1(d) | Proved in n≥2; literal n=1 refuted and corrected | C.004–C.006: sphere/Gysin/Wang input named; annular n=1 counterexample; all reduced lower cohomology vanishes. |
| C.1(e) | Checked concordance | C.010, C.017: every scan003–035 mapped, including literal errors and the undefined fragment035. Original SGA7 I/II locators checked. |
| C.2(a) | Proved in the requested CM generality | C.011–C.015: negative full-support test closes the non-Gorenstein canonical-module gap; all seven equivalences include the endpoint injection. |
| C.2(b) | Source verification pending | C.020 gives complete verified comparisons for SGA2, Hartshorne1970/1971, Speiser1973 Inventiones. C.U001: Hartshorne1968 Prop4.3; C.U002: Ogus1973 original comparison clauses. |
| C.2(c) | Proved under fully explicit readings | C.016, C.018, C.021–C.022: projective and punctured-local Ext limits; derived completion and nested-support induction; explicit counterexamples to omitted hypotheses. Page006 does not state a unique induction target. |
| L4 | Refuted, with strongest formal replacement | C.001–C.003: factorization exists; all choices form the specified affine coset; geometry selects variation. |
| L5 | Formal inference refuted; geometric theorem proved | C.006 supplies a genuine manifold counterexample to formal sufficiency. C.004 uses the additional spherical open-book/Gysin/Wang input; C.005 corrects n=1. |

## Important corrections to the supplied study

1. Abstract equivariant factorization is not unique. The example is a genuine compact oriented manifold with its boundary, not an arbitrary invented triangle.
2. The triangle, six-term sequence and link connectivity alone do not force the missing Milnor group to vanish. The sphere ambient geometry supplies the missing constraint. The actual isolated-hypersurface theorem remains true in n≥2.
3. The projective chain is true for a pure Cohen–Macaulay ambient scheme. A gap in a line-bundle proof is repaired using the coherent canonical module and the full-support negative-twist test; it is not mistaken for falsity.
4. The symbol for top differentials must be the canonical module on a singular ambient scheme. The dual-number thickening of projective space gives a concrete failure of literal Kahler differentials.
5. The last diagram is naturally a punctured-local localization diagram. The inverse-limit question holds there because the relevant Ext groups are Matlis reflexive over a complete local ring. Properness is not silently imposed on the puncture.
6. Unrestricted Ext argument swapping fails even over a Gorenstein local ring: k[[x,y,ε]]/(ε²), F=G=k, has Ext⁰ dimension1 and Ext² dimension4.
7. Relevant Lamotke source is Math. Z.143 (1975),27–44, not the supplied Topology14 bibliographical description.

## Verification and files

- `part_C.tex`: consolidated checked text, 22 stable result IDs.
- `unchecked_C.tex`: exact source gates, smallest checks, attempted access routes, and interpretation limits.
- `references.bib`: full entries marked OPENED or NOT OPENED; copyrighted source PDFs are outside the deliverable.
- `results.csv`: 22 checked results plus C.U001–C.U002.
- `checks.tsv`: proof audits, image checks, exact source corrections, and program events.
- `code/check_C.py`: 125 finite checks passed; results in `logs/check_C_output.json`. These check counterexamples and signs, not replace the general proofs.

The original images of122/003,007,019,022,030,032,034,035 and125/003,006,008 were inspected where readings affected mathematics. Critical SGA7 original pages113,143,188,192 were visually checked; Milnor6.2 and6.3 are Corollaries, and the SGA7 XIII upper-bound locator is2.1.13,p106.

## Current next step

Obtain and inspect the original Hartshorne1968 Proposition4.3 and Ogus1973 comparison theorem. The full proved mathematical chain and its endpoint are independent of these historical source gates. Continue to audit these access routes rather than call C.2(b) complete.

## Additional delegated A.2 work — 2026-11-19 12:53 UTC

`parts/filtrations.tex` contains checked A.204–A.206: a compact semialgebraic counterexample to the weak coarsest-filtration reading; the coarsest intrinsic PL F-regular pure partition, for arbitrary definable X, and its canonical dimension/refining filtration; and the interval-to-cusp obstruction to smooth regularity being an invariant of moderate homeomorphisms. All closed saturated unions are included in the positive hypothesis. Connected and frontier readings are explicitly separated from the counterexample. Compact PL type and cohomological devissage invariants include the complete exact couple and maps.

The finite partition join and link homology checks are attached as `code/check_A_filtration.py` and `logs/check_A_filtration_output.json` (six assertions passed). Source119/153 original image was read. Shiota2010 Theorems2.1 and2.2 pp5–6 were opened and used only within their compact hypotheses. Parent A.202–A.203 independently audited; the full-ruling correction is now present.

## Additional concordance audit — 2026-11-19 13:03 UTC

A.114, now in `parts/parametric_concordance.tex`, proves surjectivity of PL→definable concordances on pi1 using the scalar triangulation complement over a polygonal circle, plus explicit bottom and basepoint corrections. Full weak equivalence remains unsettled; the exact first gate is relative parameter-preserving straightening over a two-dimensional disk. Source Shiota2010 p35 supplies only a stable microbundle theorem, not the needed general fibre-bundle theorem.

A.114 now also proves all-degree PL→definable injectivity over the real field in dimension at least five, pi1 isomorphism, and the higher direct-sum splitting with the kernel of forgetting to TOP. A.115 proves all higher PL field-independence via transferred finite PL data and coning on total product cells. The remaining definable comparison gate is still a genuine multiparameter question: pi2 surjectivity over R in the stated dimension range, and relative two-disk straightening over general fields.

## Semialgebraic field comparison — 2026-11-19 13:38 UTC

A.116 proves coefficient-extension weak equivalence for semialgebraic concordance groups. A finite graph formula defines the coefficient space of admissible homeomorphisms; Hardt triviality over the smaller field, followed by a cell partition, and a compact-graph properness argument ensure joint continuity of evaluation and inverse evaluation on each cell. A cell path connects the original tuple to a smaller-field tuple. Exact nullhomotopies descend separately by first-order transfer. Together with A.115, this reduces the PL→SA comparison to the real field. In dimensions at least five it gives all-degree injection and pi1 isomorphism over every real closed field. The first remaining semialgebraic comparison gate is real-field pi2 surjectivity. This does not reduce arbitrary o-minimal expansions to R.

Root independently reviewed and passed A.115, C.021 and C.022; the individual audit entries are in checks.tsv. The original Hartshorne1968/Ogus1973 access gates remain unchanged.

## Fixed-tube dimension-condition uniqueness — 2026-11-19 13:50 UTC

A.207 in parts/filtrations.tex strengthens the numerical-uniqueness refutation: for a fixed product tube V=Y×I, every admissible attachment map with zero-dimensional fibres is a homeomorphism, so its whole rigidification space is P_def(Y). The six-torus gives nonzero components. The connected-fibre argument uses the connected complement of the core in a boundary half-ball. This does not settle the unrestricted admissible space: collapsed connected fibres are allowed there, and the inclusion of the homeomorphic-attachment subspace has not been proved injective on components. The exact full-space gate and the failed Alexander argument are now stated after A.207.

## Exact annulus certificate — 2026-11-19 14:01 UTC

The noninjective circle attachment used after A.207 now has an explicit seven-triangle model, a semialgebraic quotient parametrization on the collapsed square, and a finite computational certificate. `code/check_circle_mapping_cylinder.py` passes 17 assertions: all vertex links are intervals; the boundary is C4 disjoint union C3; orientations agree; the f-vector is (7,14,7); Euler characteristic is zero; and the exact boundary ranks are (6,7). The quotient parametrization is not asserted PL. Root's A.207 audit passed, with definable compactness/connectedness explicitly added for arbitrary real closed fields.

## Weak cone-family comparison — 2026-11-19 14:15 UTC

A.117 computes the real TOP component of unparameterized strict cone faces with the compact-open embedding quotient topology as BP_TOP(B). The key additional ingredients are controlled codimension-one local unknotting, local contractibility and complete metrizability of the actual setwise-face stabilizer, and finite-cube lifting for quotient maps with such stabilizers. All source clauses were opened. The torus concordance supplies a semialgebraic loop that cannot be filled by real definable families with locally joint outer-face parameterizations. Finite semialgebraic simplex fillings over any real closed field are excluded by transfer of their face-embedding formulas. The stronger parameterized-face convention has the different stabilizer Homeo(B×I rel both ends), explicitly separated in the theorem.

The remaining weaker-family gate is now the comparison with Hausdorff continuity alone: does such a definable family of pointwise strict cones admit local joint parameterizations of its outer faces? A.117 neither assumes nor proves this for Hausdorff families without witnesses. Its TOP lifts likewise do not supply definable relative two-disk straightening, so the real SA pi2-surjectivity gate is unchanged.

## Cell-like attachment reduction — 2026-11-19 14:19 UTC

A.208 proves that every admissible attachment fibre at a manifold boundary core is definably contractible. A boundary half-ball contracts a sufficiently shallow copy of the fibre inside any specified source neighborhood. An explicit barycentric open-star retraction then gives a contraction in the fibre itself. Over R the argument without definability proves classical cell-likeness. The unrestricted product-tube gate is sharpened to a relative parametric approximation problem for cell-like boundary attachments together with their full cylinder rulings; individual-map approximation does not close it.

Root independently audited A.117 and A.208 at14:23 UTC: all exact topology, support, dimension, relative local-contractibility, cube-lifting and barycentric-retraction hypotheses passed. Root also independently reran the 17-check annulus certificate at14:07 UTC.

## Prompt-named Part C source inventory — 2026-11-19 14:27 UTC

Every named source has been searched by exact title/author and inspected where full text was obtained. “Opened” below means the mathematical text, not only metadata. The BibTeX notes retain the URLs and status.

| Prompt source | Actual access | Exact inspected locators and scope |
|---|---|---|
| Milnor (1968), Singular Points of Complex Hypersurfaces | Opened full scan/OCR | Theorems4.8,5.1–5.2,5.11; Lemma6.1, Corollaries6.2–6.3, Lemma6.4, Theorem6.5; Lemma8.4. These supply the spherical open book, connectivity, fibre CW bound and standard monodromy inputs. |
| SGA7 I | Opened original scan, critical images | ExposéI0.3.1,2.2–2.7,4.2,4.5–4.10, printedpp3–16. Lower-bound hypotheses inspected, including the qualification missing in the literal manuscript. |
| SGA7 XIII–XV | Opened original French scan and supplied translated LaTeX | XIII2.1.13p106 and2.4.5.1–2.4.6.1p113; XIV3.1.10pp143–145; XV3.1.2p188 and3.3.5p192. C.010 contains the full scan003–035 concordance. |
| “Lamotke, Topology14(1975)” | Bibliographical description not matched; relevant original article opened | Die Homologie isolierter Singularitäten is Math.Z.143(1975),27–44, not Topology14. Sections3.1–3.4pp29–33,6.1–6.2pp40–41 and7p43 were read. The manuscript's variation/Seifert comparison uses this actual source; no unidentified Topology article is silently cited. |
| SGA2 XII–XIII | Opened revised full edition retaining original page margins | XII1.1–1.5pp109–112 and2.1–2.3pp114–115; XIII1.1–1.4 and Auslander paragraphpp135–139. Distinguishes proved ample-section sufficient criterion from the conjectural affine-duality formulations. |
| Hartshorne (1968), Annals88,403–450 | Publisher metadata opened; original full text unavailable after repeated access attempts | Proposition4.3 cited explicitly by opened Speiser1973p147; Theorem7.5 restated in opened Hartshorne1971Theorem1.3p258. C.U001 records original hypotheses and endpoint wording still unchecked. No original page number invented. |
| Hartshorne, LNM156 (1970) | Opened original complete scan; endpoint image checked | IIIProposition3.1p92, Theorems3.3–3.4pp94–98; Theorem3.4(b)p96 gives both directions and endpoint injection for nonsingular complete ambient varieties. |
| Hartshorne, Compositio23(1971) | Opened full original article; critical inequality image checked | Proposition1.1/Theorem1.3p258; Theorem2.1p259; Proposition2.2p260; Proposition2.9p261. Its projective-space criterion and the hypothesis on Y are separated from the general CM ambient theorem. |
| Ogus (1973), Annals98,327–365 | Publisher abstract/metadata opened; original full text unavailable after repeated access attempts | Original§3 comparison is explicitly cited by opened SzpiroExposé458§2.3; local/formal duality in that exposition§1.2. Opened Speiser1973p144 attributes the lci extension. C.U002 leaves original index range/endpoint and projective application unchecked. |
| Speiser (1973), Inventiones21,143–150 | Opened full original article and critical images | §2Lemma p147 contains both directions and injection; TheoremCpp147–148 gives specialized hyperplane descent. Two printed off-by-one proof labels are recorded, not used as theorems. |
| Speiser (1973), American Journal95,1–34 | Metadata only, full original not opened | Cohomological Dimension and Abelian Varieties is distinguished from the opened Inventiones article. The prompt gives only author/year; no numbered theorem is attributed to this second paper. |

For the two principal missing originals, Annals, DOI/JSTOR PDF and PDFplus, SciSpace's redirected PDF, author repositories, OpenAlex/Crossref and both search engines were tried. They yielded metadata, access pages, or later citations, not original theorem text. Root repeated the original-source searches. The remaining C.2(b) status is therefore expressly incomplete despite the independent mathematical proof.

## Unrestricted fixed-tube uniqueness settled negatively — 2026-11-19 14:33 UTC

A.209 closes the full-ruling uniqueness gate left after A.207–A.208. A locally path-connected subgroup of Homeo(Z), with its right-invariant uniform map metric, has uniformly separated path components. Their labels extend locally constantly to its closure in C(Z,Z). For the product tube T6×I, A.208 and Siebenmann's opened TheoremA p271 put every admissible ruling in the closure of the top-fixed homeomorphism group; postcomposing an approximation with the inverse top-boundary map times identity gives the required normalization. Hence no path through singular attachments can connect the nonzero torus concordance to the identity. The argument applies to every real definable family and, by exact graph-formula transfer, to semialgebraic families over every real closed field.

This proves failure of essential uniqueness for all fixed-tube admissible rigidifications, without imposing the numerical fibre condition. It uses no relative parametric cell-like approximation theorem. The latter was announced in 1970 and deferred in the 1972 paper to an unpublished manuscript; we explicitly do not treat it as an opened theorem. The stronger question whether the full ruling space has exactly the weak homotopy type of the homeomorphic-attachment subspace is not needed for the refutation and is not asserted.

Parent A.118 was independently audited and passed: its hairpin disks are Hausdorff-continuous in both interior and boundary, but cannot admit a joint face parameterization. Under the user's stipulated simplicial-category convention A.1(d) is already Refuted by A.111; the Hausdorff-only comparison is a separately stated weaker convention, not a gate for that original task.

Root independently audited the full A.209 proof at14:34 UTC and passed all metric, approximation, boundary, and transfer clauses. The original unrestricted essential-uniqueness task row is therefore Refuted.

## Higher comparison attempts — 2026-11-19 14:42 UTC

The main A.1(b) gate remains real SA pi2 surjectivity. New searches for parametrized Hauptvermutung, semialgebraic bundle PL reduction, and definable local deformation did not locate an applicable complete theorem. Fichou–Shiota2017p1231 explicitly warns that global triangulation of a general compact SA map to R2 fails; their weak triangulation is local. Bundle clutching of a sphere family merely transfers the unresolved base-preservation problem to PL reduction of a bundle. Edwards–Kirby contractions and the Michael quotient selections used elsewhere in the paper are TOP constructions, and no proof that they preserve jointly semialgebraic parameter families has been established. Lie-theory agent independently agreed that this inference would be unjustified.

The A.117 closing paragraph is now reconciled with A.118: automatic Hausdorff-to-joint-face parameterization is Refuted. Filling the torus loop in a Hausdorff-only space is a distinct optional comparison, not an unresolved interpretation of the user-stipulated simplicial category. A.209 closes the original full fixed-tube uniqueness question without claiming a full weak equivalence of its choice spaces.

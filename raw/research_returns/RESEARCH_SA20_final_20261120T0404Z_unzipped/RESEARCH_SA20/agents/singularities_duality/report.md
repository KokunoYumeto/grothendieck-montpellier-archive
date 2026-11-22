# Part C working report — 2026-11-19 12:32 UTC

**Part C is not complete: C.2(b) has two original-source access gates.** The checked file contains 23 proved, refuted, or precisely qualified results, with no theorem inferred from an unread original article.

## Current A.1(b) scope audit — 2026-11-19T19:00:01+00:00

A.131 gives whole effective countable simplicial models of PL and semialgebraic concordance spaces from a finite abstract triangulation, with terminating finite-code validity/equality tests and total structure algorithms. Its complete countable recursive presentations compute every homotopy group, and compute all-field definable components via A.113. For a real base with every component of dimension at least five, the checked PL–TOP comparison supplies the full TOP model and presentations too. This accepted form of computation is an exhaustive effective presentation, not finite classical invariants or a terminating word problem. The remaining original gates are higher PL-to-semialgebraic and PL-to-arbitrary-definable comparison, the higher model for an arbitrary o-minimal expansion, and the low-dimensional real PL–TOP comparison. Earlier E(K) and sphere statements retain their additional structural content.

## Task and lead status

| Task | State | Checked results and exact qualification |
|---|---|---|
| C.1(a) | Proved; uniqueness refuted | C.001–C.003: exact lift ambiguity and canonical geometric variation. |
| C.1(b) | Proved | C.007: degree-i transpose sign, middle sign, fully specified Seifert/variation matrices. |
| C.1(c) | Known, derived from opened sources; overstatement refuted | C.008–C.009: tame invariants, canonical twist (−n)[−2n], extra tame-invariant twist (−1)[−1], and explicit wild example. |
| C.1(d) | Proved in n≥2; literal n=1 refuted and corrected | C.004–C.006: sphere/Gysin/Wang input named; annular n=1 counterexample; all reduced lower cohomology vanishes. |
| C.1(e) | Checked concordance | C.010, C.017: every scan003–035 mapped, including literal errors and the undefined fragment035. Original SGA7 I/II locators checked. |
| C.2(a) | Literal mixed-dimensional chain refuted; full componentwise repair proved | C.011–C.015 prove the pure-dimensional chain, including the non-Gorenstein canonical-module argument. C.023 gives a projective smooth mixed-dimensional counterexample and proves all seven conditions with threshold s−m on each clopen pure-dimensional piece, including H0 injection at s=m. |
| C.2(b) | Source verification pending | C.020 gives complete verified comparisons for SGA2, Hartshorne1970/1971, Speiser1973 Inventiones. C.U001: Hartshorne1968 Prop4.3; C.U002: Ogus1973 original comparison clauses. |
| C.2(c) | Proved under fully explicit readings | C.016, C.018, C.021–C.022: projective and punctured-local Ext limits; derived completion and nested-support induction; explicit counterexamples to omitted hypotheses. Page006 does not state a unique induction target. |
| L4 | Refuted, with strongest formal replacement | C.001–C.003: factorization exists; all choices form the specified affine coset; geometry selects variation. |
| L5 | Formal inference refuted; geometric theorem proved | C.006 supplies a genuine manifold counterexample to formal sufficiency. C.004 uses the additional spherical open-book/Gysin/Wang input; C.005 corrects n=1. |

## Important corrections to the supplied study

1. Abstract equivariant factorization is not unique. The example is a genuine compact oriented manifold with its boundary, not an arbitrary invented triangle.
2. The triangle, six-term sequence and link connectivity alone do not force the missing Milnor group to vanish. The sphere ambient geometry supplies the missing constraint. The actual isolated-hypersurface theorem remains true in n≥2.
3. The projective chain is true for a pure Cohen–Macaulay ambient scheme. A gap in a line-bundle proof is repaired using the coherent canonical module and the full-support negative-twist test. Without purity the global-dimension formulation is false: P² disjoint a point has affine complement but fails the demanded H0 comparison. C.023 supplies the complete componentwise repair.
4. The symbol for top differentials must be the canonical module on a singular ambient scheme. The dual-number thickening of projective space gives a concrete failure of literal Kahler differentials.
5. The last diagram is naturally a punctured-local localization diagram. The inverse-limit question holds there because the relevant Ext groups are Matlis reflexive over a complete local ring. Properness is not silently imposed on the puncture.
6. Unrestricted Ext argument swapping fails even over a Gorenstein local ring: k[[x,y,ε]]/(ε²), F=G=k, has Ext⁰ dimension1 and Ext² dimension4.
7. Relevant Lamotke source is Math. Z.143 (1975),27–44, not the supplied Topology14 bibliographical description.

## Verification and files

- `part_C.tex`: consolidated checked text, 23 stable result IDs.
- `unchecked_C.tex`: exact source gates, smallest checks, attempted access routes, and interpretation limits.
- `references.bib`: full entries marked OPENED or NOT OPENED; copyrighted source PDFs are outside the deliverable.
- `results.csv`: 23 checked Part C results plus C.U001–C.U002.
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

## Further source audit — 2026-11-19 14:52 UTC

Murayama–Shiota2013, original pp.160–163, was opened. Its positive base-preserving bundle triangulation statement on p.160 assumes a genuine C^k fibre bundle for positive k. The source separately discusses the local-to-global subanalytic triangulation problem on pp.161–162 and the uniqueness of a triangulated orbit map on p.163. It supplies no continuous SA concordance-family straightening theorem.

The Edwards–Kirby proof was inspected more deeply at pp.68–70 and §8 pp.84–87. The concrete obstruction to a direct semialgebraic reading is the periodic lift h4 on R^n followed by radial compactification to h5 (p.69): a nonconstant periodic map has infinitely many repeated pieces, and its compactification is not generally semialgebraic. The §8 finite factorization changes the earlier torus construction, not this step. Replacing that compactification uniformly in an SA parameter family would require a new proof. This is a failed inference, not evidence that the requested comparison is false.

## Finite fragmentation route audited — 2026-11-19 15:04 UTC

Mnëv2007 §§1,9,12,14 were opened, including Proposition52 pp84–85 and Lemma12 pp90–93. The finite combinatorial argument avoids the particular E–K periodic compactification, but its small-Hudson-graph lemma depends on joint PL regularity. The moving-cube-root family h_t(x)=x+cuberoot(t)(1−|x|) on [−1,1] has arbitrarily small affine Hudson graphs meeting one leaf three times. The exact s=1/16 certificate passes 27 rational checks in code/check_hudson_failure.py. The paragraph in parts/parametric_concordance.tex records the general proof and the exact failure. Nonlinear adapted graph systems remain a possible new approach, not an established theorem. This rules out a proposed inference but does not shrink the main π2 comparison gate.

### Parameter-choice audits, 15:20 UTC

Demdah Kartoue2011 original Proposition3.6 and Theorem3.8 pp1582–1585, and Theorem7.3 pp1595–1596, were opened. The individual uniform homeomorphism bound is obtained from Hardt pieces and finitely many representative homeomorphisms. Continuous choices across the boundaries of those pieces are not constructed. Hardt–Lambrechts–Turchin–Volić2011 §8.1 pp2529–2532 was independently opened after root's check: its finite-atlas SA bundle definition, pullback/composition and cylinder invariance do not prove PL reduction of bundles. Both exact limitations are now recorded in the main comparison paragraph and bibliography; no original gate changed.

The same paragraph now proves that base-only semialgebraic reparameterization need not make parameter tracks locally Lipschitz: compactify x↦cuberoot(x³+t) by c(x)=x/(1+|x|). Every monotone semialgebraic base change has an interior point with finite nonzero derivative; the spatial point whose cube cancels that parameter then has a cube-root track. This is a failure of that particular regularization route, not a counterexample to the concordance comparison.

### Separate arbitrary-manifold component gate, 15:36 UTC

The arbitrary-manifold π₀ computation remains distinct from the higher PL-to-definable comparison. Independently audited Igusa2025 §3 and §7 in the same version used by root. Theorem7.1 p23 assumes π₂M=0 and dimension at least5; Lemma7.2 pp25–26 computes one Steinberg-move change; Remark7.3 p26 rejects the earlier general splitting claim. Its printed identification of H₂(GL′) with K₃ is an index typo and is not used. The remark does not assert that every individual extension is nonsplit: the torus has vanishing Wh₂ and is already completely computed.

Igusa2021dim3 Theorem3.1 p6 gives the general corrected exact sequence in dimension at least6 and the matrix formula for the π₂-valued part of χ from k₁M. It does not state the group law on arbitrary lifts of Wh₂. Jahren2010 §2 pp247–250 gives a canonical A-theory packaging; its Theorem2.4 splits the monomial map into K₂, not the pseudoisotopy extension. In the stable abelian setting, identifying kernel cokerχ and quotient Wh₂ still leaves an Ext¹ extension class. A full descent or presentation encoding that class has not been proved here; no component gate is declared solved.

Detailed pending audit and attempted-original-source log are in logs/igusa_extension_audit_1530.md and logs/igusa_postnikov_source_attempt.txt. The original1984 LNM1046 chapter is not opened (obsolete DOI and Springer404); the distinct author-hosted Postnikov manuscript currently returns502/503. Bibliography records these statuses explicitly.

### Low-dimensional scope correction, 15:49 UTC

Gabai--Gay--Hartman--Krushkal--Powell, Forum of Mathematics Pi14(2026)e9, published3March2026, was opened in full on the publisher's site. Its introduction before Theorem1.1 places the general two-stage obstruction theory in dimensions at least6 and explicitly states that the non-simply-connected dimension5 case is open in all categories. Remark1.6 likewise separates the unresolved general four-dimensional problem. The source is not Galvin2025; the final bibliographic identification has been checked. This does not conflict with Igusa2025 Theorem7.1's extra pi2M=0 hypothesis. No all-manifold calculation in dimensions4 or5 is inferred from either paper.


## Complete countable component presentation — 2026-11-19 16:22 UTC

A.119 is now included in parts/parametric_concordance.tex after independent root audit. For a finite simplicial model K, explicit Kan-loop-group words determine the spherical group ring, countable finite-cell derived automorphism monoids, and their bar telescopes. The presentation has one generator for each finite integral2-cycle in the universal abelian cover of the stabilized general-linear bar construction; its relations are cycle addition,3-boundaries, and images of all2-cycles from the monomial bar construction. Acyclic group completion and Hurewicz identify this quotient with pi2 of the smooth Whitehead spectrum, including its entire group law. Concordance composition is checked through pi0P = pi1BP and the classifying h-cobordism space before applying the stable comparison; an arbitrary weak equivalence of component sets is not used.

This closes the full group-presentation task for smoothable PL models of dimension at least9, over every real closed field and fixed o-minimal expansion via A.113. The result is a complete countable presentation from finite input, not finite invariant factors or a decidable word problem. It also presents the stable smooth component group in every dimension. The earlier15:36 report's statement that no complete extension-law presentation had been extracted is superseded in exactly this range. The n>=6 suspension improvement remains in separate audit notes until the full corrected-kernel and boundary compatibility is verified; nonsmoothable unstable PL manifolds and lower dimensions remain outside this result. The real SA pi2 comparison gate is unchanged.


## Stable nonsmoothable components — 2026-11-19T16:29:51+00:00

A.120 extends the complete countable presentation to stable PL concordance components of every compact PL manifold, with no smoothability or dimension restriction. Its comparison triangle is derived directly from the unit/assembly cofiber definitions; the coefficient smooth Whitehead spectrum at a point is2-connected, so the difference between PL and smooth Whitehead spectra contributes nothing in degree2 for a finite model. The relative component comparison also gives the stable definable group over every real closed field. Root independently audited the full proof and exact WJR locators; lie-theory independently checked the cofiber/connectivity argument. No unstable nonsmoothable classification is inferred in this result.


## 2026-11-19T16:41:46+00:00 — A.121 arbitrary PL components in dimension at least nine

A.121 is included after root audit. A finite regular neighborhood N of a pushed-in 3-skeleton satisfies the exact BLR localization hypotheses, and extension by identity gives a group isomorphism on concordance components. N has only handles of indices at most3 and is compatibly smoothable; A.119 therefore gives the full countable presentation E(K^(3)) for every compact PL manifold of dimension at least9, without assuming that the original manifold is smoothable. This is an actual unstable computation. All-field definable components follow from the already checked relative comparisons. The original BLR3.1 preview pp28–29 is opened and visually checked; its later concordance formulation3.1prime is used through the explicit opened GN2025 Theorem3.3, with that source distinction retained in the proof. RS locators were independently reopened and corrected to Proposition3.10/Theorem3.11 pp34–35, Cor3.18 p36, Theorems5.3–5.4 pp61–62, and Proposition6.9 pp82–83. The lower n>=6 smoothable improvement is separately under preparation as A.122; it is not silently included here.


## 2026-11-19T16:48:29+00:00 — A.122 all compact PL models in dimensions at least six

The full countable presentation E(K) now computes the unstable concordance component group for every compact PL manifold of dimension at least6, and hence for the stipulated definable groups over every real closed field. The lower smooth range uses the full corrected geometric exact-sequence theorem, including the entire image of chi, together with the checked positive-suspension maps. The partial pi2-valued matrix formula is not treated as a full-kernel calculation; the original1984 chapter remains not opened. Arbitrary PL dimensions>=7 follow from the finite3-skeleton localization, and dimension6 is handled by an explicit compatible-smoothing induction over handles, using the original KS pp39,200,211. Jahren's functorial sequence identifies E(K^(3)) with E(K), retaining the full extension law already encoded by A119. Root passed the complete integration proof; lie-theory independently passed the smooth lower-range audit. A119 and A121 keep their original checked bounds as stepping stones. Remaining component work is in dimensions0–5; no higher-parametric PL-to-definable surjectivity is inferred.

## 2026-11-19T17:06:19+00:00: A123 promoted after checkpoint08

A123 proves trivial components for compact0/1-manifolds, all PL balls, and compact orientable surfaces other thanS2, in PL and the stipulated definable convention over every real closed field. Every deformation is jointlyPL; the scalar parameter uses rho(s,t)=max(0,s+t-1), and annular Dehn twists disappear because the top face is free. Root independently passed all source hypotheses and constructions. The new closed nonorientable extension remains only in the pending log draft until separately reviewed. A124 dimension5/pi2=0 is also pending final independent audit. Higher PL-to-SA/definable comparison is unchanged.

Bibliographic correction: Fichou--Shiota2017 ends on printedp1240 (bibliography and author addresses), not1239; the own BibTeX page range is corrected to1205--1240.

## 2026-11-19T17:09:56+00:00: A123 closed nonorientable extension and A124 promoted

A123 now also includes every closed nonorientable surface other thanRP2. The complete recognition proof and the correction by the bottom restriction avoid assuming a relative Heil theorem. Root independently read Laudenbach and passed the extension. S2/RP2 and nonorientable surfaces with boundary remain outside the present clause.

A124 computes the full countable E(K) group for compactPL5 with pi2(M)=0, including all definable realizations. Root and lie_theory independently passed the actual suspension, complete framing invariant, full chi quotient, boundary, and smoothing arguments. The formulation retains the cited-full-theorem dependency of Igusa2025 Th7.1. Two printed source errors are explicitly recorded in the proof: p23(a) hasK3 whereK2 belongs inH2GL; the introductory prose p2 haspi1P where its displayed formula and Theorem7.1 havepi0P. No splitting or finite invariant-factor computation is asserted.

## 2026-11-19T17:25:13+00:00: A125 promoted; S² component gate closed

A125 proves π₀P_PL(S²)=0 and transfers it to all definable models over all real closed fields. Both root and lie_theory independently passed the complete proof and opened original Cerf and Laudenbach locators. The proof uses a disk restriction fibration, a finite-family Taylor/polar calculation with explicit basepoint transport, Cerf's three-ball connectedness theorem, and the exact boundary-jet triangle. Fixing the inner disk corresponds to identity infinite jets at the annulus bottom, not an asserted fixed outer collar. Category passage runs through TOP and then PL component injectivity, keeping genuinely PL endpoints. The same clarification is now explicit in A123's closed nonorientable clause.

The remaining closed-surface component case is RP². Its lift to S²×I must be treated equivariantly; ordinary S² isotopy does not automatically descend. Kalliongis–Ohashi2018 Sections7–8 classify finite actions and the twisted I-bundle, which alone does not supply a relative isotopy of an arbitrary RP² concordance. Negami1981 Lemma1.1 shows embedded projective planes in RP²×I are parallel, not yet the mapping-class assertion. Nonorientable surfaces with boundary remain outside the checked surface clauses.


## 2026-11-19T17:51:45+00:00 — A126/A127 promoted; closed surfaces and simply connected PL5 closed

A126 applies the visually opened full Cerf1970 pseudo-isotopy group theorem, not only its endpoint corollary. It gives trivial components for every closed simply connected PL5 manifold, with no pi2 restriction, via the compatible-smoothing argument and explicitly typed unstable Burghelea–Lashof comparison. Root independently passed the complete proof.

A127 gives a fully jointly PL proof that RP2 has trivial concordance component group. The construction uses exact antipodal endpoints obtained by collar translation plus disk Alexander correction, annulus winding only as a chosen arc label, irreducibility from ordered lifts in the orientation cover, disk uniqueness, and explicit one-sided normal-bundle extension. Root and Lie theory agents passed the final proof. Together A123, A125 and A127 now cover every closed surface. The source error in Boyle–Chen AppendixA is isolated with an exact rational point certificate; the invalid relative-boundary mapping-class assertion is not an input.

Remaining original closed-manifold component gate: dimensions3 and4, and dimension5 when both pi1 and pi2 are nonzero. The higher real SA pi2-surjectivity gate is unchanged. The new quantitative approximate-choice source supplies Hausdorff-close subsets, not continuous exact sections/homeomorphism graphs, and does not reduce that gate. Nonorientable surfaces with boundary remain an optional extension outside the original closed scope.

A fresh targeted PartC original-source pass located both exact InternetArchive journal issues, but their metadata explicitly marks PDF and text private. No private file was requested. Publisher-pattern PDF URLs return404; both search engines and repository/thesis alternatives still supply no original theorem pages. C.U001/C.U002 remain unchanged, with details in logs/C_original_source_pass_1750.md.


## 2026-11-19T18:10:14+00:00 — A128 standard spheres, directly in PL

A128 closes the standard S3 and S4 component cases and proves the same vanishing for every standard PL sphere of dimension at least2. The original Kuiper–Lashof semisimplicial definition was visually checked on printed243–244: total parameter maps are PL and preserve the parameter, with exactly the required fixed bottom and free top. Burghelea–Lashof's sphere homotopy-fibre formula and its low-degree stabilization statement, together with the visually checked KS AnnexC p318 vanishing, imply singleton components. Root independently passed every displayed source input and the exact-sequence argument.

This is a direct PL calculation. It does not use the printed unbounded statement of Burghelea–LashofII Theorem6.1 in dimensions3/4: that theorem's displayed proof invokes a high-dimensional result and supplies no such extension. The corresponding audit and the retracted tentative Ruberman route are recorded in logs/low_dimension_comparison_audit_1802.md. General closed3/4 manifolds and closed5 with both nonzero pi1 and pi2 remain open in this project; higher SA surjectivity is unchanged.


## 2026-11-19T18:14:47+00:00 — A129 all closed simply connected PL3

A129 closes the entire simply connected closed three-dimensional component case. Perelman's original elliptization conclusion gives a smooth sphere after compatible smoothing; Shalen's original approximation theorem then gives an actual PL homeomorphism, so A128 applies by conjugation. The arbitrary-field passage explicitly uses Baro–Otero arXiv0810.0365v1 Corollary4.3 p10 on a rational finite model, rather than an unjustified ordinary Lebesgue-number argument over a non-Archimedean field. Root passed the mathematical proof and independently opened the exact sources. Remaining closed dimension3 cases have nontrivial fundamental group; dimension4 general and dimension5 with both nonzero pi1/pi2 remain separate.

Lie theory's independent18:10UTC retry of the original Hartshorne/Ogus sources found no new theorem clauses; both PartC source gates remain unchanged. See the sibling notes_C_original_source_retry.md for actual pages and negative-access results.

## 2026-11-19T18:38:53+00:00 — C.023 and A.130 integration

C.023 closes the literal mixed-dimension mathematical scope of C.2(a), by counterexample and a complete seven-condition repair. The author certificate passed305 exact checks in0.006210758s; root independently passed53 checks in0.607157170s using Groebner elimination, actual rational restriction matrices and the P¹ Laurent quotient. Root and Lie theory independently audited the full proof and Stacks locators. C.2(b) retains exactly the two original-source access gates; the fresh18:28 public-source pass found metadata and request-only pages, not theorem pages.

A.130 gives a countable free abelian subgroup of every closed orientable PL3 concordance component group with infinite fundamental group, and the corresponding all-field definable group. The relative PL-to-PD equivalence constructs a typed component homomorphism, and the 2026 original detects the classes even in the fully boundary-free TOP target. Root independently audited all source and group-law steps. This is a subgroup result, not a whole-group computation and not a new closure of the remaining A.1(b) scope. The proposed effective finite-code models A.131 remain pending in logs only.

## 2026-11-19T19:00:01+00:00 — A.131 complete effective models

Promoted after root and tensor-agent full audits. Both PL graph codes and SA formula codes have decidable joint-homeomorphism validity and equality. Canonical least-code representatives make composition, inversion and every simplicial operator total and strict. All Moore-cycle and boundary relations are explicitly enumerated, so every homotopy-group presentation is complete; boundary membership is only proved semidecidable by this construction. Coefficient comparison proves that the finite algebraic syntax models the entire real and all-field PL/SA spaces. The empty-base model is explicitly trivial.

Opened inputs: May1967 original pp64–69, including the printed duplicated Proposition17.3 and first-face convention conversion; BPR online revision dated26June2016, Th2.62p62, Th2.94p80, Algorithms14.16/14.21 and Th14.22pp586–593. The independently written rational finite checker passed30 tests in0.830809s; author reread and reran it in0.842377s (saved second run0.761886s); root reread and reran it in0.778375s. All runs preserve the finite scope B=point, q=0/1/2, with actual refinements, inverses, nontrivial degeneracies and malformed-code rejection. General QE and the infinite Moore theorem are proved/cited, not claimed program-tested.

Next assigned main gate: the exact low-dimensional real PL-to-TOP comparison, especially whether relative five-dimensional product-structure theory applies to B4×I with only its bottom PL-fixed and top free. Higher arbitrary-definable comparison remains active with the other agents.

## 2026-11-19T19:31:16+00:00 — A.132: unrestricted PL–TOP weak equivalence refuted

A.132 proves the actual free-top model P_TOP(S3) ≃ Ω(TOP(4)/O(4)), with TOP(4) the global compact-open homeomorphism group fixing the origin. Its π2 is Z/2; the jointly finite PL sphere model has π2=0. Both spaces have trivial π0 and π1 in this example. The unrestricted real PL-to-TOP weak-equivalence assertion is therefore false. This is not a counterexample to PL-to-SA or PL-to-definable comparison, and it does not compute all remaining low-dimensional TOP spaces.

The relative germ proof supplies an actual continuous small-extension operator from Edwards–Kirby, one common source/image radius, and one compact-diagonal time mesh for all auxiliary parameters. It preserves the horn exactly. The disk kernel is the filtered union of fixed-inner-ball groups, giving the required free outer face. The global kernel contracts on each finite family; restricting to the identity components avoids any unsupported globalization of isolated germs. Hatcher’s original Appendix explicitly states the C0 TOP(S3) comparison. The original FQ stabilization page and the corrected 2026 GGHKP global-group convention were opened, as was KS EssayV5.5p251. Root and higher_comparison independently passed the full proof.

The finite boundary-of-4-simplex certificate passed53 exact tests in0.036127275991020724s, covering all links, integral chain matrices and a fundamental cycle. This verifies the finite PL base, not the source-derived non-PL topological family. Pending draft and independent audit history remain saved. The separate direct dimension-five product-structure attempt is not promoted: KS I5.1p31 and IV2.1p164 require the entire four-dimensional boundary controlled, which the free top does not satisfy.

## 2026-11-19T19:47:36+00:00 — A.134: all closed bases through dimension two

A.134 proves the natural joint PL-to-TOP concordance weak equivalence for every closed real base with components of dimension at most two. Hamstrom's original distinguishes slice-wise PL from actual jointly PL parameter families. Her compact-manifold convention includes boundary. The identity-component restriction is handled by an explicit all-components argument: Moise–Bing approximation, TOP local path connectivity, and finite joint PL LC0 concatenation. The bottom-setwise automorphism space of a surface cylinder splits literally as the concordance space times the surface automorphism space; the natural total comparison therefore implies comparison on each factor. No relative boundary fibration or four-dimensional smoothing theorem is imported.

The circle is treated separately using Scott's original joint simplicial definition and natural annulus evaluation theorem. The TOP identity component is contractible by Yagasaki; Epstein's TOP-to-PL surface isotopy followed by an explicit bottom correction and A.123 proves that this is the whole concordance group. Point bases use the true parameterized PL Alexander construction, not bilinear interpolation. Finite mixed-dimensional bases and the empty base are included. Root and higher-comparison independently passed all proof and source steps.

Together with A.131 this provides entire effective recursive TOP models in the stated low dimensions. The remaining low-dimensional TOP range is base dimensions three and four, beyond the exact S3 calculation of A.132. Higher PL-to-SA/arbitrary-definable comparison is unchanged. The older Laudenbach quasi-simplicial wording is preserved as an explicit source-convention warning; only his unambiguous pointwise approximation statement is used here, and prior ordinary-pi0 uses are unaffected.

## 2026-11-19T20:09:37+00:00 — A.135: exact relative comparison fibre in base dimension four

A.135 computes the homotopy fibre of fully boundary-fixed joint PL-to-TOP automorphisms of B4×I as Map(B,K(Z/2,1)). An explicit parameter-preserving horn lift gives the evaluation fibrations. A finite, jointly PL collar-compression formula turns pointwise boundary fixing into a common fixed collar for each simplex and each finite relative family. The relative structure theorem is applied to the open5-manifold B×R with BOTH exterior ends fixed, so no uncontrolled4-dimensional boundary is silently discarded. Only the standard-structure component of the automorphism orbit is used. The original universal KS square, with the chosen standard PL lift, supplies the untwisting of the section space.

The resulting based homotopy-fibre sequence relates this computed fibre to the free-top comparison fibre and the ordinary automorphism comparison fibre of B4. The right-hand comparison, the connecting maps, and any extension data remain unevaluated. Its abstract homotopy type alone would not determine the free-top fibre, and no component-surjectivity assertion is made. Root and the resumed independent higher-comparison agent passed all steps after the two precision edits. No new main-row full computation is counted.

The tempting base3 transfer has an exact failure: extending relative structures from a fixed bottom to a prescribed top germ requires the dimension4 restriction theorem with BOTH ends controlled. Its required H4 relative group is H3(B3;Z/2), nonzero for a nonempty closed connected base. The vanishing for the bottom-only pair does not justify that fibration. A stronger base4 collar-square model remains a separate research candidate.

## 2026-11-19T20:20:07+00:00 — A.136: explicit stabilization map for the based fibre

A.136 strengthens A.135 from an unevaluated fibre sequence to a specified homotopy-fibre model: F_P ≃ hofib(beta_B:F_A→Map(B,K(Z/2,2))). The map is the loop of product with a line on sliced PL structures, followed by the open five-dimensional classification using the chosen standard PL lift. Its component obstruction is the relative PL-structure class of the cylinder associated to a TOP path from the identity to a PL automorphism, in H2(B;Z2). The explicit triangular tangent-microbundle homotopy verifies this geometric description.

The proof leaves the compact four-dimensional structure space unclassified. The compact proper-submersion theorem identifies its base orbit component with the automorphism quotient. Product collars are imposed by a concrete formula that is jointly PL even for varying source and target structures. The strict collar square is then a homotopy pullback because its extension problem takes place in open dimension five. Germ cofinality is spelled out, and all loops of the standard component are retained. Root and the independent higher-comparison reviewer passed all these distinctions and the exact original source inputs.

This is the whole based comparison fibre, including all of its components. It does not determine the cokernel on concordance components, since the automorphism quotient can miss structure components and looping cannot recover missing TOP concordance components. The map beta remains unevaluated in general, and no full original A1(b) row closure is claimed. The base3 relative-extension obstruction remains unchanged.

## 2026-11-19T20:33:02+00:00 — A.137: complete component-image criterion, unresolved inputs retained

For closed real PL four-manifolds, A.137 now complements A.136's based-fibre model with a necessary-and-sufficient criterion for the image on ordinary concordance components. First the top map must be TOP-isotopic to a PL map. After choosing that endpoint isotopy, the boundary-PL cylinder has a relative Kirby--Siebenmann class in H2(B;Z2). Its class modulo the image of pi0 beta is independent of all endpoint choices and of the free-top concordance component. It defines a homomorphism on the subgroup of components satisfying the endpoint condition, and its kernel is exactly the PL image.

In particular the PL image is normal inside that endpoint subgroup and their quotient embeds in H2(B;Z2)/image(pi0 beta). This quotient is a finite elementary abelian2 group, of order at most2^b2. No surjectivity to that cohomology quotient is asserted. The exact ordinary automorphism endpoint-image predicate and the beta image remain unevaluated in general; this does not complete original A1(b). The proof uses ambient five-dimensional relative PL structures only after both boundary maps are PL, and supplies explicit ordinary endpoint traces and fixed-boundary path corrections. Root and the independent higher-comparison reviewer both passed the full proof.

The fresh OPR accepted2026 source and GN original were audited separately in logs/OPR_2026_and_GN_scope_audit.md. OPR's smooth zero-obstruction statement requires the entire boundary already smooth. GN expressly retains a kernel of double suspension invisible to its two invariants. Neither is silently converted into a complete ordinary TOP4 concordance computation.

## 2026-11-19T20:58:39+00:00 — A.139 and A.140: finite-rank sphere model and four-dimensional realization

A.139 identifies the whole ordinary TOP sphere concordance space with the based fibre of the actual finite-rank stabilization Y_n to Y_(n+1), for n at least2. Finite-family germ globalization is taken from the opened Kuiper--Lashof original; the map itself is identified by translation along the fixed cone ray and an orthogonally equivariant local coordinate isotopy. The safe S4 consequence is vanishing only in degrees0 through3, in both PL and TOP. This is a sphere model, not a replacement of the general remaining low-dimensional problem by stable groups.

A.140 proves that the OPR six-dimensional invariant equals Poincare duality applied to the relative PL-structure difference, via the exact triple connecting map. Under the actual quadratic assembly hypothesis of Definition5.8, the block theorem realizes the Bockstein-kernel subgroup in the range of A.137's lambda. If first homology with Z_(2) coefficients has no2-torsion, lambda is onto and the previous injection is the exact quotient H2(B;Z2)/J_B. The ordinary endpoint-image predicate and J_B remain unevaluated in general. The printed theorem/definition Ls/Lq convention discrepancy is stated explicitly.

For a closed simply connected PL4 base, the corrected GGHKP full pseudo-isotopy theorem gives pi0 P_TOP=1. Combining it with the realization gives J_B=H2(B;Z2). More strongly, ordinary TOP automorphism loops surject onto this cohomology group through their cylinder traces, while PL loops map to zero. Thus Aut_PL to Aut_TOP is not pi1-surjective for S2xS2. This does not infer any smooth isotopy comparison or compute pi0 P_PL. The explicit finite S2xS2 model has f-vector(16,84,216,240,96) and mod2 Betti(1,0,2,0,1). Root's1465-check run took0.014848837003228255s; the saved independent author run took0.015681307995691895s. Product triangulation and simple connectivity are proved mathematically; the code checks finite combinatorics and homology, not the source-derived TOP loops.

Root and the independent higher-comparison agent passed both full proofs and original-source scope. The20:41 fresh Hartshorne/Ogus original-source retrieval pass did not change either remaining PartC access gate; its exact negative evidence is saved separately.

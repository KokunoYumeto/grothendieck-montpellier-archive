# Part B audit record

Date: 19 November 2026, 15:53 CET (14:53 UTC).
Produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), run RESEARCH_SA08_C3_D031, subtask lifting_audit. No priority is claimed.

## Outcome

| Item | State | Proof |
|---|---|---|
| D-031 / Proposition 3.10 | Refuted over every nonzero commutative coefficient ring; SA08 refutation confirmed | B-001 |
| Exact missing condition for a given lifting problem | Obstruction class in H¹ Hom(X,ker π), vanishing exactly for liftability | B-003 |
| Universal lifting through all ideal surjections | Termwise-free source complex must and may be contractible | B-004(1) |
| Universal lifting through surjective ideal quasi-isomorphisms | Termwise-free source complex must and may be K-projective | B-004(2) |
| Extension to PD algebras over arbitrary rings | Free strict PD functor F; explicit inclusion into TS and exact graded cokernel | B-002 |
| Theorem 3.15 comparison reached by D-031? | No: D-031 target has extra H⁻². Correct Tate comparison proved independently | B-006 |
| Literal negative-dg-ideal convention in Theorem 3.13 | Refuted by Z, I=(2), de=2; corrected Tate convention and comparison given | B-007 |
| Endomorphism cohomology products after comparison | Preserved by conjugation on cohomology, with explicit coboundary | B-008 |

## Files and source provenance

The exact downloaded source is `sources/CaradotLin/HOMOTOPY_LIE_ALGEBRA.tex` (5,528 lines), extracted from `https://arxiv.org/src/2511.22614v4`.

SHA-256: `f7ea321c021f282eca77f62d12dce587f0d4042028e6de3666024b57d35c9b7a`.

The PDF is `sources/CaradotLin/2511.22614v4.pdf`, retrieved from `https://arxiv.org/pdf/2511.22614v4`; the hash is recorded in `logs/B_source_audit.json`. `pdftotext -layout` produced the text used to cross-check printed page numbers. The arXiv HTML was also opened. It numbers the PBW, differential, and extension equations (14),(15),(16); the actual PDF numbers them (11),(12),(13). Our paper cites the PDF.

The source contains 79 `\delete{...}` blocks which do not appear in the compiled article. The audit blanks these and comments without changing original line positions. There are 55 active numbered statement/definition/remark environments. A first parser run omitted the `definition` environment from its counter; it was corrected and rerun, producing the final JSON with the actual numbering (including Theorem 4.13).

### Exact source locators

| Material | Printed PDF | Original source lines |
|---|---|---|
| Cochain degrees, freeness, nonpositive subcategory | §2.1, p.6 | 354–369 |
| PD dg triple, all eight identities | §2.2, pp.6–7 | 373–389 |
| TS defined as symmetric-group fixed points | §3.1, p.10 | 559–568 |
| Exterior/PD PBW basis | p.16, Eq.(11), continued p.17 | 949–960 |
| Differential formula | p.17, Eq.(12) | 961–964 |
| Free extension | Theorem3.9, p.19, Eq.(13) | 1076–1088 |
| Unrestricted lifting | Proposition3.10, statement p.19, proof p.20 | 1111–1143 |
| Tate construction | Theorem3.13, pp.22–23 | 1307–1348 |
| Resolution comparison | Theorem3.15, pp.23–25 | 1360–1452 |
| Module homotopy comparison | Corollary3.16, p.25 | 1455–1484 |
| End cohomology algebra comparison | Corollary3.17, pp.25–26 | 1490–1508 |
| Derivation-image comparison dependency | Theorem4.13, pp.32–33 | 1906–1965 |
| Separate derivation lift | Theorem4.15, pp.34–35 | 2058–2105 |

The source proposition has no label, and the active source contains no literal later reference to 3.10. The HTML's only occurrences of its title are its statement and heading navigation. We additionally inspected later lifting paragraphs: §4 begins with K-projectivity and augmentation comparisons; Theorem4.15 makes a separate induction through boundaries; the appendix's Yoneda lifts work with resolutions. No later numbered result invokes the failed assertion. This is an audit of recorded dependencies, not a claim that every unrelated theorem in the paper has been verified.

Direct explicit references to Theorem3.15 are in Corollary3.16 and Theorem4.13. Corollary3.17 works with the preceding homotopy equivalences. Theorem4.13 also cites Conjecture4.8, which this audit does not resolve or use.

## Corrections and qualifications to earlier material

1. `inputs/SA08/sections/D_rejected_lifting_source.tex`, lines23–62: independently re-proved, with every PD identity and both the module and algebra lift checked. No correction to the counterexample is needed.
2. Same file, lines81–105: the Hom-defect repair is correct as a statement about complexes. B-003 records the exact obstruction; B-004 proves both converse characterizations. The algebra-extension sentence at lines99–100 needs the genuine free strict PD object, or the verified comparison with TS. Over Z the comparison is an isomorphism. Over rings with 2-torsion the source's general TS freeness claim fails; B-002 gives the actual map and cokernel and a concrete F₂ uniqueness counterexample.
3. Same file, lines108–114: the stated cohomology calculation is correct and D-031 does not refute the augmented-resolution comparison. A stronger claim that Theorem3.15's whole surrounding construction has been verified literally would not be justified. B-007 exhibits the negative-ideal problem; B-006 proves the corrected conventional Tate comparison over every ring.
4. Caradot–Lin source lines1118: termwise module freeness supplies a graded lift but does not remove its differential defect; in D-031 the defect is ε↦v.
5. Source lines1413 and1428–1434: a map from the isolated algebra on the newly adjoined generators is first a graded PD map. The full relative extension becomes a chain map only after the prescribed differentials are checked. B-006 gives that calculation.
6. Source lines1309–1317 and1338–1346: the asserted negative part is not a dg ideal for the first variable de=a≠0; B-007 uses a complete finite example.
7. PDF/HTML equation-number discrepancy: use PDF11–13 rather than HTML14–16; the proposition itself and its diagram are unnumbered equations.

## Computations

`code/B_lifting_certificate.py` is independent of the attached counterexample program. Its first completed run produced 567,454 exact assertions in 0.744816092 seconds. The extended final run produced 600,337 assertions in 1.005121387 seconds. It checks the integer row certificate, finite square-zero algebras over Z/2, Z/3, Z/4, the local obstruction for the standard unbounded Z/4 complex, the two maps in the characteristic-two TS example, and the negative-ideal defect.

| Coefficient ring | Algebra elements | Associativity triples | Assertions |
|---|---:|---:|---:|
| Z/2 | 8 | 512 | 1,421 |
| Z/3 | 27 | 19,683 | 40,210 |
| Z/4 | 64 | 262,144 | 525,817 |

PD identities are tested for positive indices1–6 (composition reaches index36), and all eligible coefficients/elements are exhausted in each finite ring. The hand proof verifies every index; the finite index range is not promoted to an all-index computer proof. The integer lift matrix has left annihilator `(1,-1)` whose product with the right-hand side is1, giving the all-ring contradiction. The unbounded example checks all16 possibilities in `2a+2b=1 mod4`.

The final extension also tests the two different maps from the tensor-weight-six quotient of TS(F₂e) to F₂⊕F₂y. This source has128 elements. All16,384 multiplication pairs are checked for both maps, as are divided powers on every even positive element. Both maps send e to0 and they differ on e⊗e. The integer differential de=2 verifies the separate ideal defect. These additional assertions bring the total to600,337.

`code/B_source_audit.py` computes hashes, source spans, active-label references, and PDF page hits. The corrected audit run completed in0.176196480 seconds; the earlier parser run took0.162437446 seconds. The final run recognizes55 active numbered environments and79 suppressed blocks. Its proof role is source location and explicit citation auditing only.

The supplied SA08 program was read, not executed; its role was comparison with the independently written program. Failed preliminary retrieval used the unavailable Python `requests` package; retrieval was immediately repeated successfully with the standard-library `urllib.request`. This failure affected no mathematical computation.

## Literature checked and scope

Opened the arXiv LaTeX/PDF/HTML; Spaltenstein's original paper p.124; Stacks §§13.19,23.5,23.6 including Lemmas13.19.4,13.19.6,23.5.1,23.6.8,23.6.9,23.6.11. These identify the standard K-projectivity and Tate-comparison ingredients. Search queries included the exact arXiv identifier with Proposition3.10, projective complexes/contractibility/degreewise projectivity, Spaltenstein unbounded resolutions/K-projectivity, and Stacks divided powers/adjoining variables. No claim of novelty is made for the obstruction calculation, projectivity criteria, or comparison theorem.

Web source references available for the parent to open before citing: `turn180863698view0` (paper PDF), `turn538229189view0` (HTML), `turn238559753view1` (Spaltenstein PDF), `turn238559753view0` (Stacks projective resolutions), `turn970205536view0` (Stacks Tate), `turn970205536view1` (Stacks PD polynomial algebra).

## Remaining scope

Part B is mathematically settled by B-001–B-008, with the refutation, precise repaired statements, all hypotheses, source locators, dependency audit, and independent computation. This does not settle Part A and contributes no unproved local-completion claim to it.

## Typesetting handoff

A local stand-alone B-section QA wrapper was prepared in `B_qa/`. The installed `lualatex` executable initially could not locate `lualatex.fmt`, so no B-only PDF was produced or delivered. The main run owns the requested LuaLaTeX build and rendered-page verification. The obvious TeX escaping catches reported by the parent were corrected, and the long statement display may need line splitting under the main paper's geometry.


Locator correction, 19 November 2026: original PDF pages16–19 were re-extracted directly. PBW Eq.(11) is printed on p.16, with continuation on p.17; differential Eq.(12) is on p.17. Theorem3.9 on p.19 cites Eq.(12) but does not contain that displayed equation. The combined table row formerly assigning both equations to p.17 was split and corrected. Exact equation-source spans:954–956 and962–964.

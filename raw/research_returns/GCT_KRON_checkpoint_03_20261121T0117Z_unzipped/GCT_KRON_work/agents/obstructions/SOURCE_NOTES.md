# Saturation and obstruction source notes

Worker `/root/saturation_obstructions`, model GPT-6 Astra Pro, effort setting not exposed, run `GCT_KRON_20261120`. The attached archive was read from the existing `sources/` extraction and was not extracted again. Findings in `obstructions_findings.tex` are derived variants and arguments of this run; none is presented as a claim of historical priority. Known theorems remain cited inputs. Every new proof has been read completely by this worker; independent cross checks are recorded separately by the other workers.

## Authoritative local source locators

### GCT IV

Jonah Blasiak, Ketan D. Mulmuley, Milind Sohoni, *Geometric Complexity Theory IV: nonstandard quantum group for the Kronecker problem*. The supplied file is `LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex`. Do not infer a publication year solely from that filename. The exact numbering was verified against the matching author-hosted PDF, https://websites.umich.edu/jblasiak/Apr13KroneckerGCT4.pdf.

- Theorem 15.21, source label `t main canonical basis`: parts (vii) and (viii) give positive counts for ordinary and symmetric/exterior Kronecker coefficients with the first two factors of length at most two.
- Theorem 18.2, source label `t consequence for Kronecker`: explicit positive rule in the same family.
- Proposition 18.5, source label `p Kronecker consequence l1 = 0`: special zero-first-column-difference generating formula.
- Proposition 18.6, printed pp.128–129, equations (175)–(180): exact zero classification used in O-001. The proposition is unlabelled in the source. Its equation labels are `e g = 0 1` through `e g = 0 6`. In column notation `[l2,l1]`, `l1` equals the row difference, not the first row length.
- Conjecture 19.1, source label `cj canonical basis X^r`, remains conjectural. Section 19.2 explains the dimension obstruction to the direct construction outside the two-row setting. It is wrong to cite the paper as proving general Kronecker positivity through a canonical basis.

### GCT VI

The supplied `LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex` is the revised long report arXiv:0704.0229v4, https://arxiv.org/pdf/0704.0229, not the later short article with a similar title.

- Definition 1.2.4, printed p.14 / PDF p.17, source label `dintrosat`: strict saturation and saturation index. Identically zero residue constituents are allowed. Therefore `g((k,k)^3)` has index zero despite zeros at every odd integer.
- Hypothesis 3.3.2, printed p.51 / PDF p.54, source label `phsh`: polynomial index bound and generic index-zero condition. This is not ordinary semigroup saturation.
- Hypotheses 3.3.1, 3.3.3, 3.3.4 are PH1, PH2, PH3. Theorem 3.3.5 is conditional on PH1; Theorem 3.3.6 is conditional on PH1 and SH. None is a proved unconditional algorithm for general Kronecker positivity.

### Ikenmeyer–Panova

*Rectangular Kronecker coefficients and plethysms in geometric complexity theory*, supplied `main.tex`; primary PDF https://arxiv.org/pdf/1512.03798. The formulas worker's `SOURCE_NOTES.md` gives the complete source-label/printed-number table. Relevant exact locators are Theorems 1.4, 1.6, 1.8, 1.10, 2.1 and 4.7; Corollary 1.9; Proposition 2.8; Proposition 5.2; Corollaries 5.3 and 5.4.

- Theorem 1.4: sufficient test `q>g` implies determinantal lower bound.
- Theorem 1.6: `n>3m^4`, `g=0` implies `q=0`.
- Theorem 1.8: `q>0` implies tail size at most `md` and length at most `m²`.
- Corollary 1.9: tail bound and `a>g` imply `d>n/m`; this restricts sufficient `q>g`, not arbitrary actual `q>K`.
- Theorem 1.10: exact exceptional tails `X={(1),(1²),(1⁴),(1⁶),(2,1),(3,1)}` have ambient multiplicity zero; outside X, the stated length/tail/degree/height bounds imply positive g. O-009 spells out a direct ambient-positive consequence.
- Theorem 2.1 quotes Manivel Theorem 1: symmetry, monotonicity and stable adjoint invariants. The stable side is the rectangle height in the source; exchanging the two rectangle sides by transposing both factors gives the width version used in O-003/O-004.
- Proposition 2.8: `g>=a` in the 1-stable range, in particular if `n>=tail size`.
- Proposition 5.2: all integral stretches `i>1` of `(h²−k,1^k)` give positive rectangular g for `h>=7`, `0<=k<h²`. Its computational base cases are known inputs and were not independently repeated by this worker.
- Corollary 5.3 states only even-row stable positivity; O-004 derives all stretches at least two from Proposition 5.2.
- Corollary 5.4 concerns the group and saturation of the rectangular semigroup, not equality with the original semigroup. Length at most `h²` and nonnegative coordinates are implicit ambient conditions that should be made explicit. The source proof contains m/d variable typos; no additional mathematical claim is inferred from them.
- The hook support errors in the literal statement of Theorem 6.1 are owned by the formulas worker F-006/F-007. Use Proposition 6.4 for the exact product, not its false unrestricted strictness sentence.

### Bürgisser–Ikenmeyer–Panova

*No occurrence obstructions in geometric complexity theory*, supplied `main.tex`; primary PDF https://arxiv.org/pdf/1604.06431.

- Theorem 1.4, source label `th:main`: `n>=m^25`, occurrence in padded-permanent closure implies occurrence in determinant closure.
- Section 1(b) identifies closure coefficient K, orbit symmetric rectangular coefficient sk, and ordinary rectangular g, with `K<=sk<=g`.
- Section 1(c) explicitly leaves multiplicity comparison as a possible direction. The paper does not assert `q<=K` in general. Our M-008 proves it only on the specified short-row outputs.

## Additional primary sources

- Mercedes H. Rosas, *The Kronecker product of Schur functions indexed by two-row shapes or hook shapes*, https://arxiv.org/pdf/math/0001084: Corollary 5, p.11, interval formula; Example 6, p.12, parity ray. O-001 does not relabel the parity example as new.
- Emmanuel Briand, Rosa Orellana, Mercedes Rosas, *Reduced Kronecker coefficients and counter-examples to Mulmuley's strong saturation conjecture SH*, https://arxiv.org/pdf/0810.3163: Theorem 2.4, equation (2.5), p.7. The smallest displayed family member is `((6,6),(7,5),(6,4,2))`; its odd constituent vanishes at one without being identically zero.
- Igor Pak, Greta Panova, *Strict unimodality of q-binomial coefficients*, https://www.math.ucla.edu/~pak/papers/StrictCR.pdf: Lemma 3, p.2, rectangle/two-row partition difference.
- Eugenio Giannelli, *On the decomposition of the Foulkes module*, https://arxiv.org/pdf/1207.6300: Theorem 1.1, p.1, hook vanishing; Theorem 1.2, p.2, inside-partition vanishing; Proposition 2.7, length at most number of blocks; Lemmas 3.2–3.3 and Proposition 3.4 for the hook/exterior argument. O-005 is a short lambda/wreath form rather than a duplicate of the full published proof.
- Arnaud Beauville, *Determinantal hypersurfaces*, Michigan Math. J.48 (2000), 39–64, https://math.univ-cotedazur.fr/u/beauvill/pubs/det.pdf: Proposition 3.1(a), printed p.46 / PDF p.8, linear determinantal presentation and resolution of a non-effective degree g−1 line bundle; paragraph 3.2 on the same page, relative Jacobian and theta. O-007 supplies the density/naturality passage to every determinant-closure multiplicity.
- Michel Brion, *Positivity in the Grothendieck group of complex flag varieties*, https://arxiv.org/pdf/math/0105254: Theorem 1, p.2, alternating positivity for rational singularities; following paragraph and Lemma 2 give the Schubert product application. This product is distinct from inner tensor product in R(S_N).
- I.G. Macdonald, *Symmetric Functions and Hall Polynomials*, second edition, https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf: I Appendix A (5.3)–(5.4), p.155, and (5.5)–(5.6), p.156, functorial polynomial decomposition; I (5.16), p.73, Pieri. Primary pages were independently read by the formulas worker.

## Grothendieck source dictionary

Original scans, not machine-generated modern translations, were independently checked by `archive_audit`.

- SGA3, Exposé I, §4.1, original p.23: constant groups. Proposition 4.7.2, original pp.34–35: representations/comodules. Proposition 4.7.3, original pp.35–36, and following remark: gradings, diagonalizable actions, and graded affine algebras. Editor source: https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp1.pdf.
- SGA6, Exposé V, Definition 2.1 p.314; Example 2.2(b) p.315; Lemma 2.2.1 pp.315–316; Definition 2.4 and (2.4.2) p.320; 3.10 and (3.10.1) p.331. Exposé VI, Theorems 3.2–3.3 pp.391–393: special lambda structures. Original scan: https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf.
- FGA, Bourbaki exposé 221, *Techniques de construction en géométrie analytique, IV: Les schémas de Hilbert*: Theorem 3.1 p.259, Quot representability; Theorem 3.2 p.260, fixed Hilbert polynomial; after Proposition 3.8 p.265, Hilbert as Quot of O_X; Remark 3.9 p.266, reduction overZ. Original: https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf.
- O-003 affine-space compact cohomology: SGA4, Exposé XV, Corollary 2.2, printed p.192 / PDF p.195 (affine-space acyclicity for invertible primes), combined with Exposé XVIII, Theorem 3.2.5, printed p.585 / PDF p.588 (Poincare duality). Both original statements were visually checked by this worker. The original volume is `external_sources/SGA4_tome3_original.pdf`, from https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-3.pdf. Evidence images are `SGA4_evidence/sga4_t3_p192.png` and `SGA4_evidence/sga4_t3_p585.png`.

## Scope decisions

No unrestricted classification of all Kronecker saturation holes is claimed. No general positive combinatorial formula or general multiplicity obstruction is claimed. The new concrete reductions are O-004, O-006–O-010 and root M-006–M-008; the later projection bounds supersede the mere three-row gate for the permanent comparison while leaving O-008's ambient four-row loss valid.

The universal all-r-variable projection method has a sharp asymptotic threshold by O-010. This does not make the main remaining permanent-specific multiplicity question finished. The necessary gate still requires comparing positive multiplicities on the actual two coordinate rings; `g>0` or normality alone cannot do that.

## Additional exact padding locator

IP Proposition2.6(b), printedp6, source label `prop:kadish-landsberg`, citing Kadish–Landsberg Theorem1.3, gives the padding multiplicity inequality. The supplied proof explicitly preserves all highest-weight copies via an evaluation matrix. O012b proves an arbitrary-rank version with the differential transpose normalization visible; it does not assume that naive multiplication by the padding vector preserves evaluation on the identical unchanged base form.

## Exact-complexity boundary source

Abhranil Chatterjee, Mrinal Kumar, Ben Lee Volk, *Determinants vs. Algebraic Branching Programs*, ITCS2024, LIPIcs287, article27, DOI10.4230/LIPIcs.ITCS.2024.27. Official primaryPDF https://drops.dagstuhl.de/storage/00lipics/lipics-vol287-itcs2024/LIPIcs.ITCS.2024.27/LIPIcs.ITCS.2024.27.pdf saved as `external_sources/CKV_Determinants_ABP_ITCS2024.pdf`. Definition2.4 p27:6 allows affine linear entries; Observation2.6 p27:6 makes determinant representations regular under the small-singular-locus condition; Definition2.7 p27:7 counts vertices; Theorem3.1 p27:8 gives homogeneousABP width<=s−1 from regular size s; Theorem4.1 p27:9 gives general homogeneous sizeO(b^5s). The full Theorem3.1 proof was checked in this run. The general4.1 size accounting was read but is carried as known background, and is not needed by O016. The discussion onp27:5 explains the homogeneous-extraction limitation. No border extension is asserted.

## Later primary-source and scope notes

EGA II, original Numdam scan https://www.numdam.org/item/PMIHES_1961__8__5_0.pdf: Definition5.4.1 printedp100/PDF97 and Theorem5.5.3(i) printedp104/PDF101 were visually verified by the archive worker at00:45:12UTC. The complete proof onp104 establishes universal closedness of projective morphisms. The original and evidence images are retained under external_sources/EGA_II_original.pdf and agents/archive/EGA_II_evidence/. This worker uses that verified primary input for O016, without relabeling the peer visual check as its own.

Rosas Corollary14 in the arXiv v1 primary PDF, p18, has a literal overlap at the two-row hook (N-1,1); F020 documents only that version-scoped discrepancy and proves the corrected positive boundary formula directly. Root retrieved and visually checked the original. F020's representation-theoretic proof was independently read here, including k0 andk1.

O017--O020 are full derived proofs of the exact variants stated, not claims of historical priority. O017/O019 use border-valid dimension bounds; O016 concerns exact complexity only; M013/O020 prove dominance of coefficient projections while leaving higher coefficients free. Keeping these three properties distinct is essential to the conclusions.

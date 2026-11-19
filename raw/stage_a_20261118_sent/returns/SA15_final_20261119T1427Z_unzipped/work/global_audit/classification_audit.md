# Focused global classification and merge audit

Reviewer: GPT-6 Astra Pro; effort setting not exposed. Run: SA15-20261119/cotes8_9_4 global audit. Date: 19 November 2026.

## Scope and conclusion

The audit initially read all 383 claim records across the four curator packages, including both root claim files. The subsequently added P78-C071 was also read, bringing the final reviewed total to 384. That new B-class record explicitly identifies a present-run deduction from later results and raises no A/E issue. The audit concentrated on strict authorship for class A, historical overstatement in class E, and the explicitly enumerated merge groups. It did not reopen the whole mathematical proof audit or infer new theorem priorities from the dates of modern expositions.

There are three concrete classification recommendations, recorded with their exact sources in `classification_candidates.json`. The previously agreed Artin/Deligne corrections are already present as B: P56-C058/C059, P67-C048 and P78-C026/C066/C067. No further class-A authorship mismatch was found in the current records. The remaining A attributions point to Grothendieck’s named 1968 paper, EGA with Dieudonné, SGA 1 III, or Grothendieck’s own SGA 7 IX exposition. This checks attribution; it does not certify every theorem anew.

## Exact classification corrections

**P56-C074: E → A.** Grothendieck’s 1968 Appendix, printed pp. 356–357, contains the compatible infinitesimal-diagonal and cocycle definition. The whole formulation should not be called known before him merely because it is standard now. The primary definition was independently opened and read.

**P67-C069: E → A, retaining its local hypotheses.** Grothendieck’s §3.3, pp. 325–326, derives the local formally smooth affine Gauss–Manin action using Cartan homotopy. The classical identity is an E ingredient; the full construction is the object of the row. This is an exact later-publication match, not a claim of first priority.

**P894-C070: E → B.** Serre’s 1958 contribution is the surface construction. The crystalline torsion and kernel conclusion uses later crystalline base change and stable augmentation. The owned record has been corrected, with the historical construction, the opened 2012 use and this run’s derivation kept distinct. No first publication of the exact corollary is assigned.

All three recommendations were sent to the root and the relevant owner. Only the root-agreed P894 change was applied by this reviewer; the other owners control their files. The separate origin census of the P894 package labels three present-run refinements, P894-C077/C078/C082. P894-C023 remains a manuscript question with a new counterexample explicitly attributed to this run.

## Merge identities

The detailed decisions and source locators are in `merge_audit.tsv`.

### Preserve the direct continuations

The cote 7 completed Čech–Alexander construction continues from P67-I080 to P78-I001, with the latter’s compatibility and limit qualifications retained. P78-I060 and P894-I001 are the direct cote 8:78–79 co-Lie continuation. The co-Lie claim merge can retain its standard derived-associativity component explicitly, without attributing that elementary ingredient as a new later theorem.

P56-I106 and P67-I077 have an exact categorical core in common: formally smooth maps identify the relevant crystals and stratified modules. The earlier item’s proposed flat/coherent and arbitrary-fibred-category extensions must remain separate component assertions.

### Keep these problems separate and link them

- **P56-P021 versus P78-P003:** equivalence of categories of coherent cartesian objects versus equality of ambient site cohomology and nil-invariance. The source states different conclusions. For the same reason, P78-I010 should leave the corresponding thematic item merge.
- **P56-P028 versus P67-P018:** a field-level comparison and a proposed change to derived functors in quasi-coherent crystals versus a W(k)-valued inverse-limit comparison and its ordinary-abelian counterargument. The same failed programme connects them, but their coefficients and proposed repair differ.
- **P56-P029, P56-P030 and P67-P031:** unchecked curvature, the full Leray spectral sequence, and the global derived connection/descent construction. The first already mentions a derived object, so the distinction is the obligation, not the word “derived.” Katz–Oda Theorem 1 and Theorem 3/addendum address different results.
- **P56-P014 versus P67-P021:** the local/formal-algebra Poincaré examples and m³ kernel lemma versus the ordinary cusp’s alleged Betti discrepancy. Euler homotopy is a shared checking technique, not identity of questions.

The original manuscript endpoints were read for each disputed identification. Root was notified before changing its merger. This audit changed neither merger file.

## Evidence and limits

`classification_review.tsv` records every claim ID reviewed. `source_read_log.tsv` gives the register and merger snapshots. `classification_cross_events.tsv` records the two independent claim/source matches and the reopened primary works; the P894-C070 class correction has its event in that package’s own ledger.

Three focused web retrieval requests reopened the relevant primary documents and targeted their sections. `outputs/retrieval_log.json` keeps inputs and source identifiers rather than full third-party excerpts. The Caltech PDF’s search-service title is erroneous; the actual first page identifies Katz and Oda and their correct article title.

No new class change is proposed merely because an elementary statement is currently cited through a late exposition. In particular, this audit does not infer an unknown first-circulation date for Tate-era results, or convert every present-run algebraic checking lemma into a historical theorem claim. Unsettled textual provenance remains unsettled.

## Subsequent statement-ID refinement

After this384-record audit, root split the already checked period-normalization and open-inertia corrections into two explicit B-class refinement records, P78-C072 and P78-C073. Their mathematics was previously audited under the parent C046/C047 proof passages; the new IDs make refutation targets unambiguous. The final raw census is386 and the merged claim census384. The complete final status census includes these two records.

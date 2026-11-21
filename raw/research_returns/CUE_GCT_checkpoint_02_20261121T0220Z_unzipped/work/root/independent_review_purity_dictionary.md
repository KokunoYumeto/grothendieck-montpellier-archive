# Independent targeted review of the Grothendieck dictionary

Reviewer: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

Read `work/root/grothendieck.tex` completely in its version covering R-01–R-12, I-01–I-13, P-01–P-08/P-Z, and G-01–G-09. Checked its mathematical translations against the relevant complete proofs already read. Reopened selected primary texts and primary-text transcriptions for the exact framework locators. The report does not claim that every cited SGA/EGA proof was read or that an unseen archival image was verified.

## Repairs communicated to root

1. **I-02 image grading versus extension to the variable torus.** The phrase saying that integral variable-weight descent is equivalent to homogeneity of the binomial kernel is too strong. For z↦x² the kernel is zero and homogeneous for weight1 on z, but 1=2ω has no integral solution. Homogeneity gives the grading of the image algebra; extension to all original variable characters additionally requires the integral image-lattice condition. The underlying I-02 theorem already makes this distinction correctly.

2. **Serre's base ring.** Theorem5 in §3.7 is over a principal ideal domain A, introduced immediately before the theorem on printed pp50–51. The split-reductive qualification alone does not state its full scope. The dictionary and G-B04 should explicitly mention the PID assumption, including Z as the intended case. The following Dedekind-domain remark has a K(A)/class-group contribution. The existing warning against transporting characteristic-zero simple decompositions is correct.

3. **SGA6 VI3.2 heading and hypothesis.** The retrieved French and English primary-text transcriptions label the special-λ result “Théorème3.2,” for a quasi-compact scheme S and K′ constructed from finite locally free sheaves. The draft calls it a corollary. A safe exact locator is “ExposéVI, §3.2,” with the quasi-compact-scheme scope explicit, unless the original scan is used to settle the heading. The statement itself is the correct framework input.

4. **Optional cycle-index precision.** The expression with denominators1/z_μ is interpreted in K0⊗Q, or in the rationalization of the universal torsion-free character ring. The symmetric-power operation it computes is integral. Adding this sentence to R-04 makes the distinction explicit without changing the proof.

## Main translations that pass

### Revision check

The revised dictionary has been reread at all four requested changes. It now distinguishes the image grading from extension to the ambient integral character lattice, adds the principal-ideal-domain scope to Serre's theorem, cites SGA6 VI §3.2 neutrally with the quasi-compact hypothesis, and places the cycle-index denominators in the rationalized character ring. All four revisions pass.

One additional exact-locator correction emerged when the EGA text was reopened: (2.5.1) is the setup for the sheaf construction, while the existence-and-uniqueness assertion is Proposition 2.5.2. The following Definition 2.5.3 explicitly identifies the sheaf as the object defined in (2.5.2). Root was asked to replace “Proposition 2.5.1” by “Proposition 2.5.2.” The full short gluing proof was read in the electronic translation; no original EGA scan inspection is claimed. URL: https://jcreinhold.github.io/ega/ii/02-02-homogeneous-prime-spectra.html . Web ref: turn897049493view0.

Highest-weight restriction is sound with the positive coordinate-function weight convention used in the main paper: zeros in the last coordinates of a polynomial weight prohibit all monomials involving those coordinates. The associated ideal inclusions are converted to multiplicity inequalities only over C, where the finite-degree polynomial representations are semisimple. No same-simple-basis assertion in positive characteristic is justified or needed.

The Rees paragraph correctly distinguishes the associated graded of a coefficient-span filtration from the map that adds coefficients of equal weight after substitution. Flatness of the former preserves its rank data; it cannot imply that the latter has preserved coefficient span. I-05 and I-18 supply explicit failures of that implication. The dictionary does not currently conflate these operations.

The K0/λ passages distinguish universal integral character identities, locally free/exterior-power constructions, actual characteristic-zero direct-sum decompositions, and Hermitian metrics. The use of independent dual variables over integral bases is correct; complex conjugation is not presented as a regular operation over Z. Integral localization in G-04 is degreewise, and bad-prime fibers are not silently identified with the orbit closure of the reduced point.

The G-08 universal coefficient construction is integral. G-09's change of padding coordinate is local on a chart with an invertible padding coefficient; this is the necessary qualification for its scheme formulation. The honest representations in G-03 remain a universal character example, and the dictionary properly says that associated bundles can become equal on particular bases.

The purity dictionary uses actually specified curves and lisse sheaves. It retains geometric inequivalence, the Hc² invariant contribution, Hc¹ dimension/conductor budget, and the separate nonvanishing and enumeration gates. It does not manufacture a motive for an arbitrary ROABP by terminology alone.

## Source checks actually performed

- **SGA3 I4.7.2–4.7.4:** reopened original ExposéI PDF and read the comodule equivalence, diagonalizable grading, affine-algebra remark, and splitting statement. The splitting assertion requires diagonalizability, as its placement in the paragraph indicates. URL: https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp1.pdf . Web refs: turn707978460view0, turn696163385view4–6.
- **SGA3 VIB4.1:** reopened the French primary-text transcription and read its short proof, including the explicit EGAIV3 13.1.3 citation. It concerns locally finite-type group schemes (and local constructibility with finite presentation). URL: https://grothendiecksga.com/read/sga3/fr/VIB-4.html . Ref: turn707978460view4.
- **SGA6 V2, V3, V7:** reopened the cited primary-text transcriptions. Definitions2.1/2.4, Example2.2(b), the exact-sequence exterior filtration, Proposition3.2, §3.10, and Adams§7.1/Proposition7.5 support the dictionary as stated. The product/composition laws are special-λ laws, not merely the pre-λ additivity axiom. Refs: turn707978460view1, turn684054482view2, turn707978460view3.
- **SGA6 VI3.2:** direct opening repeatedly failed; search retrieval returned the full theorem statement and splitting-principle proof from the French primary-text transcription. Its heading and quasi-compact hypothesis are recorded above. URL: https://grothendiecksga.com/read/sga6/fr/VI-3.html . Ref: turn756289927search0. No original scan check claimed.
- **Serre1968 Theorem5:** reopened the original author-hosted scan and read §3.7, including the PID hypothesis and following Dedekind/decomposition-matrix remarks; §3.8 is the announced GL_n example. URL: https://www.college-de-france.fr/media/jean-pierre-serre/UPL8576975072934521334_Serre_Grpes_de_Gr.pdf . Refs: turn589275450view2–3.
- **FGA Bourbaki221:** reopened the primary scan; Theorems3.1/3.2 and Proposition3.8 have the indicated representability/projective/Grassmannian-immersion content. Proposition3.8 uses sufficiently high degree, as retained in the dictionary. URL: https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf . Refs: turn506018200view1–3, turn589275450view1.
- **EGAII §§2.4–2.5:** reopened the electronic English translation and checked the Proj/associated-sheaf framework. This was a translation check, not an original-scan or complete EGA proof review. URL: https://jcreinhold.github.io/ega/ii/02-02-homogeneous-prime-spectra.html . Refs: turn696163385view3, turn589275450view0.
- **D-ET:** the exact trace, weight, Euler–Poincaré and monodromy references had already been checked and recorded in `work/purity/sources.md` P-B02–P-B03/P-B14. No fresh full-paper Weil proof review was performed for this dictionary.

## Review limit

The requested mathematical scope review found the I-02 lattice equivalence requiring correction, plus the Serre hypothesis and SGA6 heading precision above. New dictionary entries for results appended after this reviewed version require their own inspection. The review does not certify paleographic readings of the absent cote133 raster pages or identify future literature results beyond the cited sources.

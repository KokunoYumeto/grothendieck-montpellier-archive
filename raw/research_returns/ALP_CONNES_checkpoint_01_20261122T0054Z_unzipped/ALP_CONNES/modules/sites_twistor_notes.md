# Sites, Riemann–Roch, twistor and counting workstream

Status: AC-G01–AC-G12 written and author whole-proof checked. Independent review requested from root. This is a component of ALP_CONNES, not a declaration that the entire user task is finished.

## Principal conclusions

A supplies the exact Hermitian numerical Hodge inequality (including the factor 1/2 in the one-sided N normalization) and an explicit Hilbert numerical intersection model. It does not supply the surface intersection/Riemann–Roch/effectivity constructions. Existing curve/periodic-orbit RR statements are unconditional.

The sign–Tate class is built as a graded rational C2 representation and as an Artin–Tate motive. Global nontrivial zero lines follow from A; local constituent weights are unconditional. Multiple Tate degrees do not give a single pure weight. The complete Euler assignment fails to preserve tensor/Witt multiplication at the ramified prime2. On the good open SpecZ[1/2] it preserves it, but the omitted Euler factor introduces elementary zeros which must be kept separate from primitive nontrivial zeros.

Explicit correction of supplied note §8.2: even powers of epsilon are1 and are not fixed under multiplication by epsilon. The Boolean fixed subset has its own unit e=0_R, so inclusion inG(R) is nonunital. The object1⊕epsilon is not the zero object; only its inert odd-power trace is zero.

Two split-zero constructions have now been distinguished and built: (i) a sheafification on the original space, with clopen support; (ii) a semiring spectrum with an added generic point. The latter has exactly the old ring-valued points, so element cardinalityq+1 does not establish a P1 scheme-point count. Odd powers are multiplicative monoid maps but need not be additive semiring maps. The group-like diagonal on all ring elements is incompatible with identifying−1 with a nontrivial base sign.

The Gaussian Weil restriction example is globalized explicitly; its actual graded dimensions are unimodal although its inert Frobenius trace coefficients dip. A does not prove associativity or a categorical pentagon for arbitrary GCT constants.

## Exact supplied-source locators

- 1603.03191, geomscalingsite1.tex: Thm3.9 scaltop; Thm4.2 structure2; Thm4.3 structure3; Thm5.6 thmjaccp; Thm5.17 RRperiodic.
- 1805.10501, thecurve_K.tex: §3.1 negcrit,negcrit1,negcrit1bis; §3.4 subsections3.4 five-step strategy; §7 Witt lift of correspondences.
- 2205.01391, RR-J-final.tex: Thm4.3 rrspzb; Thm5.3 serredual; excL and ceilingprime. Ignore duplicate material after the file's end-document marker when indexing.
- 2306.00456, RRZ.tex: Thm5.1 rrspzb; precise right-continuous ceiling convention crucial.
- 2609.00299, CC.tex: Prop3.2 prop:points_X_K; Thm5.1 thm:twistor_space_scheme; Prop7.3 prop:global_sections_frobenius; Prop7.5 prop:twistor_frobenius; §2.2 convolution.
- 2112.08820, SullivanRH.tex: Thm2.11 w0s1; Thm2.12 rabi10.
- math/0703392, Yuri70v2.tex: §7 PosTrRHint and terms01Tr; the written polar term has to be read on real functions or Hermitian-corrected.
- math/9811068, main.tex: §I equations1–3 and following paragraph, Riemann–von Mangoldt and oscillatory O(logE) estimate.

Numbers were checked by counting the shared theorem environments within the supplied section structure, cross-confirming the known twistor Prop7.5. Source labels remain definitive locators if typesetting/version numbering differs.

## External primary-framework sources inspected

- SGA4, ExposéII, Thm4.1(1), associated-sheaf exactness: https://grothendiecksga.com/read/sga4/fr/II-4.html (text transcription opened).
- Grothendieck, Sur une note de Mattuck-Tate, J.reine angew.Math.200(1958),208–215; §1 Hodge-index theorem and inequality1.8; §2 inequality2.1 and proof. Full text inspected via the identified transcription https://denisevellachemla.eu/AG-Mattuck-Tate.pdf . Its added numbering1.1/2.1 is not silently substituted for the original theorem numbering.
- Montpellier archive catalogue https://grothendieck.umontpellier.fr/archives-grothendieck/ : cotes2(RR),10(tensor categories),11(correspondences),14(cycles),16(Poincaré–Hodge),19(topos). These are topic mappings, not theorem/scan identifications.

Attempts to open /2.pdf,/16.pdf,/19.pdf through the web tool returned inaccessible. The catalogue's extracted links collapsed to one page anchor; indexed third-party pages at grothendieck.commutator.io returned404. No individual manuscript scan was inspected. An exact scan locator is therefore an open bibliography gate, not claimed complete.

## Proof-check scope

The events TSV records author targeted whole-proof checks individually. The arithmetic polynomial/homomorphism script records only finite examples; it does not certify the general sheaf or category theorems. No Lean archive verification was performed. Supplied A is a stipulated theorem. Cited GCT tables/certificates and their pentagon data were not present as direct source material for this workstream, and were not re-certified.

## Remaining mathematical gates

1. Actual regularized intersection theory and surface Riemann–Roch/effectivity on the arithmetic square.
2. Comparison between the spherical Connes–Consani object and either of the explicitly chosen split-zero constructions; a sheaf change alone adds no topos point.
3. A literal zeta/trace comparison for the entire absolute twistor object, beyond its Gaussian avatar.
4. Coherent categorical realization of structure constants beyond the explicit Artin–Tate examples; numerical associativity does not provide the associator pentagon.
5. None of these constructions transfers an arithmetic Landau window bound to the cubic Kummer character.

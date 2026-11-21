# Implications at the current research stage

Run GCT_NSRH_20261121. **WORK IN PROGRESS.** This file accompanies the paper and will be updated as the active routes are settled. The paper integrates findings F01–F42; main GCT conclusions remain open.

## The principal mathematical reduction

For trace functions on A^d over F_q with a pointwise weight bound a, F01 gives the exact path identity q^n N=M^k+R and the operator-norm estimate. F02 makes the finite spectral no-cancellation step precise. Opposite parity turns the residual trace into a sum with positive spectral multiplicities, so a diagonal tensor root α^k survives. First taking extension degree to infinity and then path length to infinity proves |α|≤q^((a+d)/2). Specified Tate duality gives equality in every embedding. This is F03; no semisimplicity or real-positive eigenvalue assumption is needed.

F04 allows controlled errors with overhead o(k) in the weight exponent. F17 allows the construction for each path length to be defined only over a finite extension depending on that length, provided all multiples of that extension degree are covered. It also permits a separate dual coefficient system with its own upper bound. These are genuine reductions of the sufficient geometric gate, not a construction of the missing nonstandard trace objects.

The phrase “sign only” does not erase the finite-spectrum realization, parity, pointwise bound, all-embedding estimates, and duality. F05 supplies explicit failures of abbreviated versions. Purity is an eigenvalue-size statement; F06 shows why it is not coefficientwise positivity or Lefschetz unimodality.

## What changes for GCT

The supplied IV/VI/VII/VIII versions give a programmatic nonstandard RH proposal, not a stated finite-field theorem with designated objects and weights (A01; exact locators in the paper). VIII's targets include signed factors, rational normalizations, and more general almost-positive assertions. A generic theorem that a trace has the correct absolute value cannot by itself prove these targets.

F07 states the extra effective-category and basis-preserving realization hypothesis that would produce positive graded structure constants. F09 proves a concrete obstruction in the actual rank-one nonstandard Hecke inclusion: its intersection with the standard tensor KL-positive cone consists only of positive scalars. Thus the full rank-two algebra cannot inherit its positive basis merely by taking an effective additive subcategory through that inclusion. F16 gives an abstract positive replacement and proves that it changes the original action. This narrows the needed categorical comparison; it does not refute GCT VIII or rule out a different heart or signed normalization.

F10 offers an algebraic sufficient alternative: exclusive positive monomial pivot coordinates force internal structure positivity. Disjoint positive supports, even with bar invariance and generic semisimplicity, do not suffice. VIII's local crystal support statement does not itself give those global pivots.

Ordinary orbit-closure schemes over Z exist (F15), and their projective finite-field intersection cohomology has ordinary purity. Their graded coherent multiplicities still retain polarization, linearization and section data absent from the underlying cohomology. The P1 example proves that these cannot simply be forgotten. An actual coherent-to-constructible comparison remains an additional theorem.

The exact Ikenmeyer–Panova and Bürgisser–Ikenmeyer–Panova statements retain their published ranges. They restrict occurrence obstructions, not all multiplicity obstructions. A strict reverse coordinate-ring multiplicity inequality is still a valid route, but none is newly proved here. The known two-row crystal rule is cited as a known theorem; no arbitrary-height rectangular positivity or PH1 claim is inferred from it.

No Boolean P≠NP or algebraic complexity separation follows from the present findings. Even a positive coefficient formula would require the actual specialization, effective encoding, bit bounds and further lower-bound steps of the flip. The paper explicitly distinguishes numerical nonnegativity, a positive formula, #P witnesses, PH1 and bounded-index hypotheses.

## What theta/determinant positivity changes

F12 expresses the numerical multiplicities through existing Reynolds projectors and positive Gram matrices. This makes positivity of principal minors precise but does not select an independent basis; determinant positivity can simply encode the unknown rank.

F13 proves an exact path-count theorem for additive exact functors between split semisimple categories with 0/1 branching. To apply the theta chain, its functors and endpoints must actually recover the desired tensor/Schur restriction. The analytic order gained in Alpöge's lifts is not already the dimension of that Hom space. The active lattice/congruence analysis seeks a more precise gate and is not yet claimed as an established transfer from theta lifting.

## What changes in Grothendieck's language

The findings distinguish effective representation K0 from its group completion. The calculation λ²(z−1)=1−z (F11) is an exact example in K0 Rep(G_m), not an analogy. The γ-filtration records characteristic-class information but supplies no missing positivity order. An algebraic subring is not automatically the split K0 of an effective subcategory (F09).

Verified archive anchors are framework references, not attributions of new GCT results:

- **Cote90, scan17:** flat affine group actions and equivariant quasi-coherent modules; relates to SGA3 I4.2 and4.7.2–3.
- **Cote97, scan4:** Chern classes and regular representations.
- **Cote133, scan18:** symmetric/exterior generating functions; scans19–21 concern virtual finite G-sets, with “plethisme” on20. These are not a positive plethysm coefficient rule.
- **Cote16, scans35,37,39:** Lefschetz/primitive/projector language. The even-numbered backs in the suggested34–40 range are reused typescripts.
- **Cote16, scan48:** conditional correspondence-ring semisimplicity; scan49 gives a conditional Weil deduction. The conjectural letters are in the letter's own notation. Scan50 is not the semisimplicity passage.

The SGA4/5/WeilII trace and duality dictionary carries the sign proof once its actual trace objects exist. BBD5.3.8 gives geometric semisimplicity, not arithmetic Frobenius semisimplicity. FGA221 §3, Theorems3.1–3.2 represent Hilbert/Quot functors under their hypotheses; representability does not establish the desired constructible/coherent comparison. SGA6's original scan was not visually readable in this run, so it is background, with the specific locator V2.2.1 corroborated through Altman–Kleiman §2.10. The elementary λ calculations have full direct proofs.

Cote1 was inspected at eight leaves under both numbering conventions. Handwritten folios79–80 are archival scans77–78 (PDF78–79): generic Fredholm determinant and trace formulas are visible. Folios111–112 are scans109–110 (PDF110–111), concerning entire functions and canonical products. Literal scans79–80 and111–112 were also read. No Xi identity or RH-equivalent positive operator was verified; visible manuscript formulas are not a checked complete proof.


## Further proved reductions in the second work interval

**Signed inputs.** F24 removes common input parity: signed real Euler multiplicities work at even path lengths because some largest-modulus product retains a positive coefficient. The negative path-output spectrum remains necessary. Copying F17's unrestricted finite-extension step to signed traces was false; an explicit counterexample was found, and retained top-radius visibility repairs it.

**Actual small-rank geometry.** F19 and F21 realize the actual nonstandard rank-three algebra and its 64-dimensional right tensor action over a finite localization. The center has an order-two branch collision. F25 computes the commutant comparison: the regular commutant has rank688, while the full classical fiber commutant has dimension816; the missing128 maps are off-diagonal maps between the merging multiplicity spaces. Crossed coherent Ext groups retain the collision length. F22 shows that ordinary constant nearby/vanishing-cycle traces are identical for every positive collision order. This is a proved limit of that particular coefficient realization, not of all enriched Weil objects.

**Normalization is a substantive issue.** F26 computes the actual normalized word trace Tr(e1e2)=24+16/D². Evaluating at v=q^(±n/2) is not any finite exponential-polynomial sequence; the proof allows arbitrary signs, complex coefficients and Jordan terms. Therefore no fixed finite Weil correspondence can satisfy that literal arithmetic word-trace dictionary. The unnormalized trace is Laurent and has a graded Tate realization. Localizing or completing a category, or extracting a numerator first, requires its own specified comparison. F27 supplies a bounded derived Hecke lift and a four-character positive Tate model with the correct rank-one actions, while proving the limits of single parity and scalar localization.

**Classical geometry is already available.** F20 supplies actual Schur-projector images in ordinary and motivic Satake. The coefficient motives are copies of one Tate twist, so their natural Frobenius is scalar, not merely pure in absolute value. This still leaves the projector rank, its useful basis and its compatibility with designated nonstandard operations. F23 gives a sufficient signed-orbit/Pieri counting rule and a pure GL2 example with no signed basis.

**An obstruction in all rectangular families.** F28 proves that every rectangle with both sides at least two has a tensor square admitting no scalar-monomial basis whose stabilizers are Young subgroups. The source IP Proposition6.4 gives hook multiplicities0,1,0 in degrees2,3,4. Effective Young-orbit modules have consecutive hook support, so cannot supply that isolated internal hook; the size4 edge is checked separately. This applies to the actual unprojected rectangular Satake multiplicity module, including large GCT parameter ranges. Non-Young stabilizers and other positive formulas remain possible. Manivel's known height-two invariant algebra supplies an actual monomial basis and an exact rational-point Ehrhart rule in a different model.

**Tower and primitive objects.** F30 now supplies the complete rank-four mixing repair, while proving that its classical projectors do not lift to whole-algebra projectors. F31 gives the actual primitive Grassmannian Tate motive. F32 extends the signed upper criterion to admissible countable spectra and proves that bounded reciprocal duality forces their visible spectrum to be finite.

## Normalization, actual traces and current effective targets

F35 realizes the entire normalized word-trace sequence by the finite-type stack X=24 points disjoint union16 copies of A6×Gm8×(BGL2)^4. Its computed compact cohomology is unbounded and mixed. Verdier duality exists; its ordinary dual has unbounded positive Frobenius roots. Thus the remaining sign-only gate is the independent dual bound and actual operator/path comparison, not existence of a scalar mass.

F36 computes a second-order coherent Frobenius defect: center/algebra pullback adds torsion of length80(p−1) on the actual tensor module. A unit parameter-base structure and a unit normalized model both preserve the actual action. Pushforward through the collision loses the unit by the calculated torsion. These are coherent statements; they do not identify quantum degree with an ℓ-adic weight.

F38 proves that an inverse convergent Euler trace is not an actual tensor inverse. The explicit reciprocal stack times P1 has trace1 but unbounded nonzero cohomology. In the usual derived Weil category every invertible object is a one-dimensional shift, so none can have trace q^n+2+q^(−n). Fixed-q scalar division remains possible and requires a different comparison. F39 tests the modern smooth proper noncommutative Weil conjecture precisely: the actual collision category is nonsmooth, whereas good split fibers have four-point normalized TP. F40 supplies the action-preserving smooth corner repair: the actual algebra is End(P) and its tensor module is Hom(P,Mtilde) in a smooth proper category with four unit TP eigenvalues. Its nonsmooth corner is not an admissible motivic summand; the based-operation and relative comparisons remain distinct.

The supplied VI v4 homogeneous PH1 is already false by Kahle–Michałek, Theorem5 and Remark6, p4, with its equal-rectangle interpretation on p6. This known refutation is now explicit in the paper and question ledger. Their pp3–4 distinguish later inhomogeneous polytope families; the earlier theorem does not refute every such family. F34 proves a separate compact-dimension obstruction on a positive simplex family and an output-length obstruction to fully compact binary plethysm #P. F37 proves a bijective polynomial-size compression of the known PPS marked-tree witnesses when rectangle rows are explicitly listed. Positive rules, computational encodings and homogeneous Ehrhart models therefore have different exact statuses.

Every current finding has a separate PartIII translation with exact source/framework anchors. The new stack and dg constructions use the named modern extensions of Grothendieck's frameworks; none is attributed to an archival leaf. The first scheduled three-hour review has not yet occurred.

# Component-family research after C.3bt

GPT-6 Astra (OpenAI), ChatGPT Pro mode; root; 19 November2026. Research remains incomplete. This note records methods and exact source scopes, not additional numbered theorems or qualifying progress.

## 1. Current main gate and the distinction that matters

C.3bt is fully certified and was counted once in review14. In the positive-characteristic algebraizable normal strict-local threefold branch, the remaining group is exactly

`T_E / (phi(J_K intersect S00) + phi(Q intersect S00))`.

All notation and the separate denominator intersections have the meanings in UK.7. The entire component-restriction kernel has already been removed. A graph family on a smooth component can nevertheless restrict to a nonzero class of CH0(C_e times P), even though its two endpoint restrictions vanish. Thus pointwise lifting, algebraic triviality on a stratum, and an actual globally compatible perfect family remain different assertions.

The new edge K1 families change a coherent lift after its component obstruction is zero. They do not themselves alter a nonzero edge K0 image of a prescribed component family. A second proper parameter gives another relation, but one must still exhibit an actual component correction or prove the necessary exactness. No exactness of quotienting by proper endpoint relations is assumed.

## 2. Primary source readings and precise limits

### Friedlander–Walker

Friedlander, E. M., & Walker, M. E. (2002). Semi-topological K-theory using function complexes. *Topology, 41*(3),591–644. https://doi.org/10.1016/S0040-9383(01)00023-4 . The primary author PDF was opened at https://dornsife.usc.edu/ericmfriedlander/wp-content/uploads/sites/233/2023/06/24.pdf . Root read Definition1.1, Propositions1.2–1.3 and their complete proofs, and Theorem1.4 and its complete proof, author PDFpp3–6. The journal metadata was checked in the publisher search result and author's publication list; the direct publisher opening returned403.

Their parameter definition allows arbitrary smooth connected varieties and explicitly uses affine curves over an algebraically closed field. Theorem1.4 proves the rational Chern-character comparison for smooth X by applying ordinary Riemann–Roch also to X times the parameter. It does not establish the required proper-parameter comparison for a singular SNC surface. This source was inspected to test applicability; it is not a new input to C.3bt.

### Achter–Casalaina-Martin–Vial

Achter, J. D., Casalaina-Martin, S., & Vial, C. (2019). Parameter spaces for algebraic equivalence. *International Mathematics Research Notices, 2019*(6),1863–1893. Primary author version dated11September2019: https://www.math.uni-bielefeld.de/~vial/abtriv.pdf . Root read the introductory Theorem1 statement, Definitions3.1/3.4, Lemma3.8 with its complete proof, Proposition3.11 and its complete proof, and Proposition3.14 with its complete displayed proof, PDFpp6,8–10. The publisher opening redirected to an inaccessible CDN. No complete supporting Bertini or whole-paper audit is claimed.

Lemma3.8 compactifies a parameter curve by the surjective restriction map on ordinary Chow groups. Proposition3.14 uses a symmetric product and the projective-bundle formula to replace a projective curve by its Picard variety. These are cycle-class comparisons; the closure supplied by Chow localization need not be perfect on E times the compact parameter. They therefore do not supply the missing SNC perfect-family extension.

### Krishna–Park

Krishna, A., & Park, J. (2013). Algebraic cobordism theory attached to algebraic equivalence. *Journal of K-Theory, 11*(1),73–112. https://doi.org/10.1017/is013001028jkt210 . Root obtained and read the primary arXiv1203.5508v2 PDF, dated7September2012, after the web opening failed. Read the introductory hypotheses and Theorems1.1–1.3 as statements, the complete Section2.2 definitions and Lemma2.4 proof, and Theorems8.1 and8.3 with their full displayed proofs, author pp4–5,20–21. Their invoked cobordism comparison theorems were not independently re-audited here.

This paper defines bundle equivalence using smooth projective parameter curves, but its singular-scheme comparison in Theorem8.3 is explicitly with the coherent-sheaf group G0 modulo those relations. K0 and G0 are identified there only for smooth X. Its base field is characteristic zero throughout. Neither a positive-characteristic theorem nor a singular perfect-K0 identification follows. The source supplies a useful distinction, not a vanishing theorem for UK.7.

## 3. Acquisition and retained failed attempts

`code/fetch_proper_parameter_sources.py` records all three acquisitions, exact URLs, UTC times, byte lengths, SHA256 hashes and pdftotext return codes. Its complete JSON and stdout are in `logs/proper_parameter_source_acquisition.json` and `.out`. Acquisitions completed18:57:19–18:57:22UTC; elapsed times were9.371356459s,7.873751442s and7.377137303s respectively. All PDFs and text extractions succeeded. The first program version failed before network access because requests was unavailable; that exact version and error output are retained. The corrected program uses the standard library, without installing anything.

Other unsuccessful openings: the MSP zero-cycles-with-modulus PDF returned no readable lines; arXiv1203.5508 and itsv2 web routes returned DisabledError; CiteSeer returned403; ASARC's preprint page returned a Unicode decoding error. These are acquisition events, not mathematical evidence. The local successful arXiv acquisition supersedes only the availability failure.

## 4. Root method tests

**Surface Chow projectors.** It would be unsafe to assert that a transcendental surface projector makes every boundary-curve correspondence zero merely from cohomological weights. In contravariant conventions, CH²(S times C) contains correspondences from the surface motive to a curve motive. A projected transpose graph records the action of curve zero-cycles on the surface's Albanese kernel; for a surface with nontrivial such kernel this need not disappear. No complete projector vanishing was proved. This possible method was sent to the two-parameter reviewer with the direction-of-correspondence caution.

**Exceptional image alone.** The common negative-intersection relation removes degrees and component Albanese coordinates, but it cannot simply be asserted to absorb every Albanese-kernel cycle. A Picard-rank-one component with trivial Picard variety has only a one-dimensional rational divisor source, whose nonzero negative-normal intersection has nonzero degree. Its intersection with the degree-zero target can therefore be zero even when the surface's Albanese kernel is not. Actual proper-family relations are essential. This is a test of the proposed argument, not a newly constructed local counterexample.

**Blowing up graph-boundary intersections.** Suppose a graph curve in E_i meets the double curve E_i intersect E_j at q. Blowing up a curve in E_j through q can separate the strict graph from the old double curve and replace the crossing by a rational exceptional double curve in E_i'. However, the exceptional divisor that corrects the new rational-edge degree restricts to O(q) on the old double curve. The original Picard-valued error reappears. Tautological divisors on the added ruled component also have coupled degrees on its fibres and create a new boundary along the centre curve. No triangular correction or termination argument has been proved. This modification is not a reduction of UK.7.

**Compactified moduli of bundles.** Proper moduli spaces of semistable coherent sheaves do not themselves provide perfect families on a singular surface. A proof would need a suitable connected proper parameter contained in the locally free/perfect locus, with the prescribed endpoint K0 classes and controlled restriction data. Smooth-surface asymptotic irreducibility and codimension heuristics do not establish this for a reducible SNC surface. No such moduli theorem was used or assumed.

## 5. Literature queries and next exact issue

Queries included `"algebraic equivalence" "K0" "singular" surfaces`; `"proper" "algebraic" "K-theory" "zero-cycles" singular surface`; `"Chow" "modulus" "algebraic equivalence" "proper"`; `"algebraic equivalence" "perfect complexes" proper curves`; `"vector bundles" "algebraic equivalence" "projective curve" singular`; `"moduli" "locally free" "codimension" "rank" "surface" "irreducible"`; and the exact titles of the three papers above. Results were used to locate primary sources. No literature-wide nonexistence or novelty inference is made.

The Frobenius reviewer is deriving the exact parameter-boundary obstruction from regular-stratum purity and actual SNC totalization, avoiding singular ambient devissage. The component reviewer is checking relative K-theory and modulus comparisons at their actual dimensions. The cycles reviewer is examining two-parameter corrections. These remain research directions until their complete constructions and independent audits provide either a further strict main reduction or a counterexample.

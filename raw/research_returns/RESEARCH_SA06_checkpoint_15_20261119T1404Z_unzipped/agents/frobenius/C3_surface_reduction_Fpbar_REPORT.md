# C.3be — arbitrary excellent local domains with residue Fpbar

## Certified conclusion and exact scope

**Proved.** Let R be an excellent local domain of dimension N at least two with residue field isomorphic to the algebraic closure of Fp. Then CH_1(Spec R) with rational coefficients is zero. The puncture, equipped with the inherited dimension function delta(p)=dim(R/p), consequently has CH^(N−1) with rational coefficients zero.

The ambient domain need not be normal or henselian. Its puncture need not be regular. No coefficient field, equal-characteristic hypothesis, algebraization over a field, or resolution in dimension greater than two is used. In particular the assertion includes mixed-characteristic domains. Ordinary B is a quotient and vanishes wherever that quotient has been defined; the text does not impose a product-family definition over a nonexistent coefficient field on a mixed-characteristic ring.

This is a residue-field-specific positive result. It does not close the unrestricted rational top-quotient question over arbitrary algebraically closed fields, and it is not counted as resetting the scheduled main-gate movement clock. No integral vanishing, finite torsion group, or common annihilating exponent is asserted.

Final proof: C3_surface_reduction_Fpbar.tex. The previous draft file is now a pointer to the final file.

## Complete proof structure

1. **Surface geometry with all required properties at once.** An excellent normal local surface is regular outside its closed point. Stacks/Lipman 54.14.5 and the normalized-point construction 54.6.5 resolve it by normalized closed-point blowups over that point. Excellence makes each normalization finite. A further sequence of point blowups from 54.15.6 makes the whole reduced closed fibre SNC. These constructions preserve the puncture. Starting with the closed-point blowup also covers an already regular surface.

   The exceptional divisor of an ordinary blowup is effective Cartier, with its negative tautological bundle relatively ample. Finite dominant normalization preserves effectivity, the Cartier property, and relative ampleness. A sufficiently weighted sum of the preceding total transform and the next exceptional divisor is negative ample for the composite. The first divisor's total transform retains the whole closed-fibre support. This simultaneously gives a projective regular model, preserved puncture, SNC fibre E, and D=sum a_i E_i with all a_i positive and −D relatively ample. It does not use the invalid conjunction of separate resolution and projectivization existence assertions identified in the earlier C.3bd audit.

2. **One finite K0 detecting level.** KST Theorem A and (1.6) give the exact pro sequence for the closed point and the resolution. Since K0 of the local ring and of all its Artinian quotients is Z, quotienting by the diagonal graph makes the restriction from the constant K0(Z) a monomorphism of pro-groups. Its level kernels form a descending system of subgroup inclusions. Pro-zero therefore forces an actual zero kernel at one finite level.

   At every infinitesimal closed fibre E_b, p^b=0, even in mixed characteristic. The reduction E inside E_b is nilpotent. GH Theorem A applies to rings in which p is nilpotent, not only to Fp-algebras. Finite affine-cover K-theory descent gives K0(E_b)_Q=K0(E)_Q. Hence K0(Z)_Q injects into K0(E)_Q. No nilpotence assumption on the ambient ring or on Z enters.

3. **Determinant, with the order of operations explicit.** A multidegree-zero line bundle on the SNC curve E is torsion: component Jacobian points descend to finite fields, and the remaining node-gluing scalars lie in the torsion group k*. For a line bundle L on Z, first choose M with L^M|E actually trivial. K0 injectivity makes [L^M]−[O_Z] a torsion K0 class. Projectivity over an affine base supplies the resolution property, so vector-bundle K0 equals perfect K0 and the vector-bundle determinant is available. Applying it to an integer annihilating this K0 class makes L torsion. Thus Pic(Z)_Q injects into the multidegree space Q^c.

4. **An explicit intersection argument.** The exceptional degree matrix M is symmetric with nonnegative off-diagonal entries, and Ma has strictly negative coordinates. For Q=diag(a)Mdiag(a) and b_i its row sums,
   x^tQx=sum b_i x_i^2−sum_(i<j) Q_ij(x_i−x_j)^2.
   This proves negative definiteness and invertibility. The exceptional line bundles span all multidegrees and therefore Pic(Z)_Q. Cartier-divisor closure on regular Z makes Pic(Z)→Pic(U) surjective, while those exceptional bundles restrict trivially. This proves Pic(U)_Q=CH_1(Spec B)_Q=0 for the normal local surface.

5. **Every curve comes from a surface, without henselianity.** Catenarity puts a curve prime p in a two-dimensional prime quotient B=R/q. Its finite normalization T is a normal integral semilocal ring; every maximal residue field is still Fpbar. Each maximal localization has dimension at most two. In dimension two, Steps 1–4 give torsion of its class group, with no henselian hypothesis; in lower dimensions it is a field or DVR. For any fixed Weil divisor on T, a common positive multiple is therefore Cartier at every maximal ideal, hence Cartier everywhere by the rank-one reflexive-sheaf description. Every invertible module over a semilocal ring is free. This common multiple is thus principal and Cl(T)_Q=0. The finite pullback of the dimension function has generic value two, so Cl(T)=CH_1(T). A prime above p/q is a height-one prime, and finite pushforward sends its class to a positive finite residue-degree multiple of [V(p)]. The surface result therefore kills every generator of CH_1(Spec R)_Q. Localization at the omitted closed point loses no dimension-one cycle. No assertion about equality of all maximal heights in T is needed.

## Independent audits

The first three receipts below concern the earlier henselian version. Its exact proof, result row, report, events, PDF and build output are retained with the suffix henselian. The same-ID semilocal refinement removes only that hypothesis and has the following additional full receipts:

* Owner /root/frobenius: checked the complete typed semilocal proof, exact localization of rank-one reflexive sheaves, semilocal triviality of line bundles, and the inherited dimension-function class-group identification. Newly opened sources are Stacks 02M9, 0EBM, 02JW and 02SI; actual downloaded pages and hashes are retained.
* /root/real_weil: complete typed nonhenselian proof reread and fresh source audit **PASS at 2026-11-19 13:06:03 UTC**; detailed section 9 and a canonical event were appended to the existing peer report and event file.
* /root: complete refined final text and all four new primary-source checks **PASS at 2026-11-19 13:06:39 UTC**. The detailed semilocal audit is appended to research/notes/ROOT_C3be_SURFACE_REDUCTION_AUDIT.md, with a canonical event in ROOT_CHECKPOINT14_CHECK_EVENTS.tsv.

No further residue-field extension is included in the certified statement.

* Owner /root/frobenius: full derivation, all source-hypothesis checks, source ledgers, and actual standalone builds.
* /root/real_weil: complete strengthened proof and fresh primary-source audit **PASS**, actual tool clock **2026-11-19 12:54:25 UTC**. Detailed receipt: real_weil/C3be_surface_reduction_independent_REVIEW.md and its canonical event file. No independent program/build rerun is claimed.
* /root: complete strengthened proof and primary-source audit **PASS**, completed before actual tool clock **2026-11-19 12:55:25 UTC**. Detailed receipt: research/notes/ROOT_C3be_SURFACE_REDUCTION_AUDIT.md. The root read the original build program and its initial output without rerunning it. Final layout changes are limited to a clearer title, a shorter DOI URL, and the required reference rerun.

## Primary-source ledger

Every source below was actually opened. No inaccessible citation substitutes for an inspected theorem statement.

| Input | Exact opened locator | Use and scope |
|---|---|---|
| Stacks/Lipman | Theorem 54.14.5, [0BGP](https://stacks.math.columbia.edu/tag/0BGP), full statement and proof | Excellent normal local surfaces, including mixed characteristic |
| Normalized point blowups | Lemma 54.6.5, [0BFZ](https://stacks.math.columbia.edu/tag/0BFZ), full statement and proof | Centres over the specified original closed point |
| Surface SNC | Lemma 54.15.6, [0BIC](https://stacks.math.columbia.edu/tag/0BIC), full proof | Entire reduced closed fibre, resolved by point blowups |
| Tautological divisor | Lemma 31.33.4, [02OS](https://stacks.math.columbia.edu/tag/02OS), and preceding [Section 31.33](https://stacks.math.columbia.edu/tag/01OF) | Effective exceptional Cartier divisor, O(−E)=O(1), relative ampleness |
| Finite normalization and ampleness | Lemma 30.17.2, [0B5V](https://stacks.math.columbia.edu/tag/0B5V), full proof | Applied affine-locally on the preceding base |
| Composite ampleness | Current Lemma 29.38.8, [0C4K](https://stacks.math.columbia.edu/tag/0C4K), full proof | Positive weighted exceptional-divisor induction |
| KST | Author v4, Theorem A and (1.6), pp.2–3; [primary PDF](https://arxiv.org/pdf/1611.08466) | All noetherian abstract blowup squares; finite K0 detection derived explicitly |
| GH | Theorem A, printed p.29; [published PDF](https://math.mit.edu/~larsh/papers/025/bounded.pdf) | p nilpotent in the ring; all integer degrees of nonconnective K-theory |
| TT | Theorem 8.1, p.367; previously opened exact source in the C.3bc audit | Finite affine-cover descent; no new complete article rereading claimed |
| Vector-bundle K0 | Lemma 36.38.5, [0FDJ](https://stacks.math.columbia.edu/tag/0FDJ), full proof | Resolution-property comparison |
| Determinant | Section 17.26 and Lemma 17.26.1, [0B37](https://stacks.math.columbia.edu/tag/0B37), full paragraph and proof | Exact additive K0-to-Pic homomorphism |
| Semilocal line bundles | Lemma 10.78.7, [02M9](https://stacks.math.columbia.edu/tag/02M9), statement and supplied CRT/Nakayama proof hints | Finite locally free constant-rank modules over a semilocal ring are free |
| Reflexive sheaves and class groups | Lemma 31.30.2, [0EBM](https://stacks.math.columbia.edu/tag/0EBM), full proof | A common multiple Cartier at all maximal localizations is an invertible rank-one sheaf |
| Finite dimension functions | Lemma 29.53.3, [02JW](https://stacks.math.columbia.edu/tag/02JW), full proof | The finite normalization carries generic dimension value two |
| Class group and Chow group | Section 42.24, [02SI](https://stacks.math.columbia.edu/tag/02SI), paragraph after Definition 42.24.1 | Cl(T)=CH_1(T) for the inherited dimension function |
| Proper Chow pushforward | Lemma 42.20.3, [02S2](https://stacks.math.columbia.edu/tag/02S2), full proof | Positive residue-field degree and rational equivalence |
| Chow localization | Lemma 42.19.3, [02RX](https://stacks.math.columbia.edu/tag/02RX), full proof | Omitted point has dimension zero |

The source archive sources/C3be/ retains the two newly used PDFs and the Stacks HTML pages. The output/C3_surface_reduction_Fpbar_sources.json log records all actual acquisition times, HTTP results, sizes, and SHA-256 hashes. One Stacks 02RX download initially returned HTTP 503; the successful retry is separately recorded in output/C3_surface_reduction_Fpbar_sources_retry.json. The primary page had already been read through the web tool, so that transient download failure did not stand in for source access. The four newly used semilocal pages all downloaded successfully on 2026-11-19; their actual 8.801045244996203-second acquisition, sizes and hashes are recorded in output/C3_surface_reduction_Fpbar_semilocal_sources.json. Stacks 092X remains in the bibliography solely as a source used in the retained henselian proof.

## Literature positioning and historical versions

The finite-type surface assertion is established in the literature. We opened Tanaka's complete published paper and read Theorem 4.5, printed p.42, its proof and Remark 4.9 on p.43. It asserts Q-factoriality for normal surfaces over Fpbar and explicitly points to earlier antecedents. We also opened Esser's clean **five-page** author PDF and read Theorem 2.4 with its proof on **author pp.4–5**. That proof establishes torsion of the henselian local class group and credits Artin. Pages 5–6 belong to the different six-page annotated Comment version.

Exact retained PDFs:

* sources/C3be/tanaka2014.pdf: 736723 bytes, SHA-256 4f1f36b4a7b1abed04ff998d8a0bf03883e6198d5c5eee82b50aa7f33a662ffa.
* sources/C3be/esser2023.pdf: 194333 bytes, SHA-256 e00553c48ab76e9cd7365aab712f237a860f06ed3c826808c9209ddd9e9d80eb.

The exact Tanaka publisher-PDF URL is retained in the acquisition JSON; the bibliography uses its DOI URL to avoid severely stretched typesetting. Esser's publication is Proceedings of the American Mathematical Society, 151(2), 527–531 (2023), DOI 10.1090/proc/16140. The root checked this metadata against the author's institutional record. We do not claim to have freshly audited the cited Artin originals, and make no originality or priority claim for C.3be.

The first C.3be draft assumed an algebraizable normal ambient ring and descended each surface quotient and its normalization to a finite pointed étale stage. That narrower argument is retained as output/C3_surface_reduction_Fpbar_algebraizable_initial.tex; its older finite-model Stacks entries remain in the bibliography as research history. The determinant surface lemma makes that descent unnecessary and expands the validated hypotheses. The initial draft's malformed TeX command was superseded by the complete rewrite.

The next, fully audited version assumed an excellent henselian local domain, including mixed characteristic. After checking that the surface proof never used henselianity, we replaced its final local-normalization argument by the semilocal class-group argument above. This is a modest same-ID hypothesis refinement, not a second result or a new movement-clock event. The prior certified files are retained with the suffix henselian rather than silently overwritten in the research history.

## Computational and presentation verification

This is a general proof. No finite experiment is offered as verification of the theorem.

The reproducible script code/build_surface_reduction_Fpbar.py compiles the owned standalone wrapper using LuaLaTeX, BibTeX, and reference-stabilizing LuaLaTeX passes. It records actual command return codes, runtimes, warnings, PDF size, and page count. The initial build and its warnings remain separately in output/C3_surface_reduction_Fpbar_initial_build.json and .out. The clean draft build is separately retained. The canonical output/C3_surface_reduction_Fpbar_build.json and .out describe the final-path build.

Final PNG inspection, source acquisition, and exact build completion are recorded in the canonical check events. Compiler success is not represented as an independent proof check.

The current nonhenselian standalone build began at 2026-11-19 13:06:28.583346 UTC and took 4.10244647100626 seconds. All five commands returned zero. Its PDF has six pages and 155458 bytes; the final log has no warnings. The earlier five-page, 150030-byte henselian PDF and its separate 4.506621198001085-second build remain preserved.

All six current 1200-pixel page renders were inspected by the owner before 2026-11-19T13:10:30.283980+00:00; no clipping, missing glyphs or broken references were found. The semilocal refinement is finalized, with the historical receipts preserved and new canonical events appended.

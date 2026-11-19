# Independent audit of C.3ar

**Reviewer:** `/root/frobenius`. **Completed:** 2026-11-19 10:38:35 UTC.

**Verdict:** PASS for the exact product-of-curves, rational, complex-coefficient scope of `agents/cycles/product_curve_top_quotient.tex`. This is a restricted positive theorem; it does not close arbitrary complex cones or the integral top-cycle problem.

## 1. Scope and finite detection

I read the complete typed proof and reread its C.3ab/ad inputs. The pro-cdh argument really yields one finite detecting thickening, not just elementwise separation in a limit. The local terms (K_0(R)) and (K_0(R/\mathfrak m^a)) are both canonically \(\mathbb Z\); quotienting the pro-exact sequence by the graph of the unit gives a pro-monomorphism from the constant (K_0(Z)). Its kernel system is represented by decreasing actual subgroups with inclusion transition maps. Such a system can be pro-zero only if a term is zero. Thus (K_0(Z)\to K_0(V_a)) is injective for all sufficiently large (a).

The regular pointed-etale models supply the rational Chow/Adams-weight identification and the requisite pullback compatibility. The proof does not identify arbitrary inverse-limit (K_0) elements with actual classes.

## 2. Relative weight and absolute differentials

The weight-(d) relative sheaves vanish below degree (d), and the degree-(d) sheaf is the direct sum of (\Omega^{d-1}_{V/\mathbb Q}\otimes L^j) for (1\leq j<a). In the descent spectral sequence, an incoming differential to the only possible diagonal term would start in a vanishing sheaf degree; an outgoing differential would exceed the cohomological dimension of (V). Thus the displayed relative group is an isomorphism, not merely a subquotient.

The model over \(\overline{\mathbb Q}\) provides the split absolute differential sequence. Kodaira--Akizuki--Nakano vanishing applies to every positive relative-form degree with positive (L^j), leaving exactly (H^d(V,L^j)\otimes\Omega^{d-1}_{\mathbb C/\mathbb Q}). Commutation with the possibly infinite constant differential vector space follows from a finite affine cover. No complex-vector-space structure on Chow groups is inferred.

## 3. Actual Picard classes and the leading product

The split formal logarithm defines an individual formal line bundle for each (a\in H^1(V,L^j)), with pure internal degree (j). Proper formal existence, Elkik's puncture comparison, Cartier closure on the regular resolution, and a single exceptional-divisor twist yield the required actual line bundle on (Z). This is an individual line-bundle algebraization statement, not a formal (K_0) algebraization theorem.

I freshly opened the full BEK and CHW primary PDFs. BEK Lemma 2.2 and Proposition 2.3 give the exact symbol (\{1+t^j a,g_1,\ldots,g_{d-1}\}\). The proof of BEK Proposition 6.1, author pp. 12--13, explicitly says that the canonical Milnor-to-Quillen-to-cyclic comparison followed by the differential is (d\log). Positive internal degree admits the Euler-contraction inverse after division by (j\), so the leading horizontal cyclic representative is (t^j a\,d\log g_1\wedge\cdots\wedge d\log g_{d-1}\), with coefficient one, up to the stated ordering sign. CHW Remark B.8.1 and the following discussion on author p. 25 explicitly give multiplicativity; Theorem B.10 gives the compatible weight decomposition. This justifies the cup-product calculation in descent.

The proof uses BEK's comparison only on compatible actual products or their leading symbols. It correctly does not promote BEK's pro-isomorphism to a fixed-level isomorphism. The fixed-level weight calculation has its separate Loday/CHW justification.

## 4. Coefficient spanning and actual scalar absorption

For a morphism (u:C\to\mathbb P^1) defined over \(\overline{\mathbb Q}\), all branch values are algebraic. A transcendental fibre is reduced. Its evaluation functionals span the dual canonical space once \(\deg u>2g-2\), because a nonzero canonical form cannot vanish at every point of that fibre. This proves the claimed span of the actual absolute Picard classes with a prescribed (db\) factor.

Multiplication by any nonzero section of (L_i^j) is surjective on (H^1(\mathcal O_{C_i})\to H^1(L_i^j)), by the dual injective map on canonical sections. Kunneth therefore gives every required top-cohomology coefficient. Each complex scalar in that finite linear-algebra expression is absorbed into the parameter (a\in H^1(V,L^j)) of a newly constructed actual line bundle. It is never applied to a Chow class. Varying one point-difference factor on its actual proper curve makes every resulting product ordinarily algebraically trivial. The case of a vanishing (H^1(L_i^j)) correctly needs no construction.

## 5. Finite elimination and localization

The uniform detecting thickening makes successive cancellation terminate after finitely many internal degrees. A line bundle with pure degree-(j) logarithm contributes no smaller internal term, so previous cancellations are preserved. The remaining class vanishes in actual (K_0(Z)_\mathbb Q) and hence in (\mathrm{CH}^d(Z)_\mathbb Q). Pullback and refined restriction preserve the stated actual-family equivalence. The ordinary quotient reduces to the degree quotient of zero-cycles on connected projective (V), namely \(\mathbb Q\).

Finally an integral curve of positive (L)-degree maps, by exceptional self-intersection, to a nonzero multiple of that generator. Localization therefore kills the rational ordinary quotient on the puncture. All steps retain the stated rational scope.

## Opened primary source ledger

- Bloch, S., Esnault, H., & Kerz, M. (2014). *Deformation of algebraic cycle classes in characteristic zero*. Algebraic Geometry, 1(3), 290--310. DOI: 10.14231/AG-2014-015. Opened full 21-page author PDF at <https://page.mi.fu-berlin.de/esnault/preprints/helene/112-bek.pdf>; reread Lemma 2.2, Proposition 2.3 (author pp. 3--4) and Proposition 6.1 proof (author pp. 12--13). Local files: `agents/cycles/sources/BlochEsnaultKerz2014.pdf` and `.txt`. Web source `turn755541217view0`; targeted screenshot `turn477203647view0`.
- Cortinas, G., Haesemeyer, C., & Weibel, C. A. (2009). *Infinitesimal cohomology and the Chern character to negative cyclic homology*. Mathematische Annalen, 344(4), 891--922. DOI: 10.1007/s00208-009-0333-9. Opened full 29-page author PDF at <https://arxiv.org/pdf/math/0703133>; reread Theorem 6.1 and Corollary 6.2 (author p. 15), Remark B.8.1 and Theorem B.10 (author p. 25), including multiplicativity and the Adams shift. Local files: `agents/cycles/sources/CortinasHaesemeyerWeibel2009.pdf` and `.txt`. Web source `turn755541217view1`; targeted screenshot `turn477203647view1`.

The existing bibliographic records `D_BlochEsnaultKerz2014` and `D_CortinasHaesemeyerWeibel2009` are reused; no duplicate bibliography keys were introduced. This audit rechecks the C.3ab/ad proof inputs but does not claim a fresh rereading of every cited book or theorem in those earlier certified sections.

# Independent-agent review of the plethysm fragment

Reviewer: `/root/bridges`, GPT-6 Astra Pro, inherited/undisclosed effort. Date: 20 November 2026 UTC. Completion clock observation: 23:21:00 UTC.

Reviewed the entire `work/plethysm.tex`, including all proofs PL-01–PL-08 and PLE-F5, then checked the three requested corrections and the added hook-length locator in the revised file. Revised SHA-256 observed: `6e7a9f7dc751332f5c84bc658b37c9d76286857a8ae6b34c034ed7a629470fad`.

## Outcome

**All nine stated deductions pass full-proof review.** No mathematical gap remains in their stated scope. This is an independent-agent targeted proof review, not an independent reconstruction of every argument and not a formal certificate. A genuinely different all-degree derivation of the Hilbert function in PLE-F5b is given below and recorded separately as an independent re-proof of that part only.

Three wording corrections were requested and the owner applied them:

1. The definition of a special lambda-ring must include `lambda_t(1)=1+t` as well as the universal product and iteration identities. Zibrowius, *Symmetric representation rings are lambda-rings*, Section 3.1, printed p.1069, states all three requirements. The omission did not invalidate any example, because the actual structures have the expected unit, but mattered for the claimed abstract definition and universal property.
2. The noninjective natural `h_(5,5)` example now explicitly uses `W=C^5`, matching Landsberg Proposition 7.9(1). The existence claim was sound; the added dimension prevents an incorrect reading in small dimensions.
3. The recent positive formula result now explicitly covers all plethysm coefficients with output at most two rows and the corresponding equal-rectangle Kronecker family. Pak–Panova–Swanson Theorem 1.1 is the family `g(lambda,(n^k),(n^k))`; it must not be presented as an all-other-partitions two-row Kronecker formula.

The owner also added the exact hook-length source for PL-07 after my suggestion: Macdonald Chapter I, (7.6)(ii), and Section 5, Example 2.

## Proof-by-proof check

### PL-01

The regular two-point `C2`-set has two free orbits in its Cartesian square, one fixed two-element subset, and symmetric square equal to one free orbit plus one fixed point. Therefore `x^2=2x`, `epsilon^2(x)=1`, `sigma^2(x)=x+1`, and the opposite coefficient is `x^2−sigma^2(x)=x−1`. Full-group marks distinguish both proposed exterior variants from the boxed formula. The comparison correctly concerns the supplied reading of the transcription, not an independently verified manuscript image. The cardinality qualification is accurate.

### PL-02

The monomial basis proves symmetric-power compatibility under linearization; taking inverse generating series proves the opposite structure's compatibility. The exterior square of the complex regular `C2`-representation is sign, whereas the unique two-element subset linearizes to trivial. The universal order-two product identity implies multiplicativity of `psi^2`. For the subset structure, `(2x−2)^2=4` while `psi^2(2x)=4x−4`; the marks are 4 and −4. For the opposite structure on `C2×C2`, the two quotient orbits have `psi^2=2`; their product is the regular orbit, whose invariant multisets of size two are absent. Its full-group mark under `psi^2` is therefore zero rather than four. Both counterexamples are valid. The passage from pre-structure to the free special-ring universal property is correctly prohibited.

### PL-03

For each exponent vector, the tensor weight space is exactly the indicated induced permutation module. Grouping equal unordered positive exponent lists gives each monomial symmetric function with coefficient one. Torus restriction is injective on the polynomial `GL(V)` representation Grothendieck group, and remains so with coefficients in the free abelian symmetric-group representation ring. The h-basis/induction monomials are independent in characteristic zero. The degree-two formula gives `Sym^2−Lambda^2`, so its negative irreducible coefficient is real and is not a misleading pointwise-dimension claim. The full tensor power can be effective while this particular basis expansion has virtual coefficients.

### PL-04

The modular regular `F2[C2]`-module has a trivial invariant line and trivial quotient. Exact `G0` therefore gives the stated relation. It is indeed a nonzero polynomial relation in the proposed free generators. The following paragraph correctly distinguishes split group completion; the short exact sequence does not split. No classification of all local rings is claimed.

### PL-05

The trace of a permutation matrix counts fixed points, hence is elementwise nonnegative. The sign character is negative at a transposition. The effective-set operations stated preserve effectiveness. This proves precisely the limitation on that realization method, without refuting richer positive formulas or general representation positivity.

### PL-06

Semisimplicity in characteristic zero and Schur's lemma give block maps `1⊗H_lambda`; kernels and images have the stated multiplicities. The quotient by the Chow ideal is the image because Landsberg Proposition 7.6 identifies the kernel. Ambient source and target characters alone fail to determine an arbitrary equivariant map's rank, as zero and rank-one multiplicity maps demonstrate. The natural `h_(5,5)` counterexample in dimension five is explicitly stated by the supplied source. The orbit, closure, and normalization are distinguished throughout. No implication from lack of a rank calculation to mathematical impossibility is asserted.

### PL-07

The matching action has fixed-point counts `(3,1,3,0,1)` on the five listed `S4` conjugacy classes. Subtracting trivial gives `(2,0,2,−1,0)`, whose squared norm is `(4+12+8)/24=1`. The unique dimension-two irreducible is the Specht module `(2,2)` by the cited dimensions. Cubing its character and averaging gives `(8+24−8)/24=1`. The `S2` triple sign invariant space is zero. Thus the exact naive down-scaling implication is refuted, with the residuewise/saturation-index hypotheses explicitly left separate.

### PL-08

In characteristic two, strict nondegeneracy of a quadratic form means nondegeneracy of its alternating polar form, forcing even rank. The hyperbolic quadratic plane exists, while its exterior-square vector space has odd rank; no rank-compatible lambda operation valued in the group generated by these strictly nonsingular forms can have the required augmentation. This is a valid field counterexample to the unrestricted topos assertion. Over the reals, the exterior square of the hyperbolic bilinear plane has determinant −1 and nonzero Witt signature. Hence the usual exterior operations cannot descend through the hyperbolic quotient. The proof does not confuse this with the valid Grothendieck–Witt specialness theorem in characteristic different from two.

### PLE-F5

The substitutions obey the binary-dihedral presentation with twelve distinct diagonal/off-diagonal elements. The cyclic invariant ring has the stated monomial normal form, whose images are distinct. Passing to `C,V,D` uses an invertible linear change over `C`, and the monic relation gives unique `f(C,V)+Dg(C,V)`. Invariance under the remaining involution is exactly evenness of `f` and oddness of `g` in `C`. This proves the two-generator free module and multiplication relation without assuming the desired invariant presentation. The weights and rational series follow, and the floor-function generating series is arithmetically equal. Agreement with the cited ray is only agreement of dimensions, as required.

## Independent re-proof of PLE-F5b by monomial eigenspaces

This derivation does not use the presentation, free-module basis, or rational-series manipulation in the supplied proof.

Let `s≥0`. A degree `2s` monomial `x^p y^q` is fixed by `a` exactly when `p−q` is divisible by six. Since `p+q=2s`, write

`m_k = x^(s+3k) y^(s−3k)`, with `−floor(s/3) ≤ k ≤ floor(s/3)`.

These monomials form a basis of the cyclic-invariant subspace. Under the second substitution,

`b(m_k) = i^(2s) m_(−k) = (−1)^s m_(−k)`.

For each `k>0`, the span of `m_k,m_(−k)` has one-dimensional `b`-fixed space, generated by `m_k+(−1)^s m_(−k)`. The remaining vector `m_0` is fixed exactly when `s` is even. Therefore the full invariant dimension is

`floor(s/3) + 1_(2 divides s)`.

In odd degree no cyclic-invariant monomial exists because an even difference `p−q` and an odd sum `p+q` cannot occur simultaneously. This also independently checks the half-grading convention and the value at `s=0`.

## Scope of modern GW and SGA assertions

The modern Grothendieck–Witt assertions are broader than the supplied archive sheets, but they are **correctly presented as separate cited theorems**, not as established on those sheets. I directly read both primary statements:

- Zibrowius, *The gamma-filtration on the Witt ring of a scheme*, Theorem 2: any scheme over a field of characteristic not two. No affineness, regularity, or integrality assumption belongs to that particular theorem (the adjacent filtration Theorem 1 has stronger hypotheses).
- Zibrowius, *Symmetric representation rings are lambda-rings*, unnumbered main theorem, printed p.1056: any affine algebraic group scheme over a field of characteristic not two. The group need not be reductive and its representation category need not be semisimple; the theorem is about the Grothendieck–Witt definition used there.

Those theorems must not be substituted for the split group completion of quadratic bundles on an arbitrary locally ringed topos. The current fragment expressly avoids that substitution. Nor does either theorem cover strict quadratic forms in characteristic two; PL-08 handles that failure directly.

The SGA 6 opening assertion is limited to vector bundles on a quasi-compact scheme, a standard special lambda-ring setting. The recorded SGA VI Theorem 3.2 locator was checked by the author against reconstructions. I did not independently inspect the original SGA 6 theorem page: the accessible geotoppos PDF proved to be only a 24-page contents/introduction reproduction, and the proposed Zenodo scan-slice collection returned HTTP 410. The modern primary Zibrowius article separately confirms the SGA VI general construction and cites Theorem 3.3 for the broader ringed-topos argument. Thus no new source-page certification should be claimed in my name for original SGA VI 3.2. This is an evidence qualification, not a discovered mathematical counterexample to the quasi-compact-scheme statement.

## Primary sources actually opened during review

- https://nyjm.albany.edu/j/2015/21-49v.pdf — refs `turn401136176view1`, `turn418464257view0`, `turn418464257view2`; main theorem p.1056 and lambda-ring axioms p.1069.
- https://arxiv.org/pdf/1411.3198 — ref `turn401136176view0`; Theorem 2, PDF p.3.
- https://www.lamfa.u-picardie.fr/bouc/Burnside2.pdf — ref `turn401136176view2`; Introduction and Theorem 1.1.
- https://arxiv.org/pdf/1305.7387 — refs `turn662132620view0`–`turn662132620view3`; Propositions 7.6, 7.9(1), 7.11–7.12; Section 7.5; Theorem 3.7. Relevant full mathematical content also read in attached TeX.
- https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf — refs `turn143021445view0`–`turn143021445view2`; I(7.6)(ii), I Section 5 Example 2.
- https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p41/pdf — ref `turn574800003view1`; Theorem 5 and Remark 6 for the exact periodic ray and homogeneous Ehrhart exclusion.
- https://arxiv.org/pdf/2511.02312 — ref `turn574800003view0`; Theorems 1.1–1.2 and Lemma 2.1, July 2026 version.

The supplied archive transcriptions for cote 133 scans 6, 8, 19, 28 were read again during this review. No original manuscript-image eye check was performed. Claims about other archive pages were not independently re-audited here.

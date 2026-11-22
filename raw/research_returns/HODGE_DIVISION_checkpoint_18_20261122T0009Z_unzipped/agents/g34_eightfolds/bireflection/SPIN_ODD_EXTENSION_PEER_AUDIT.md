# Independent whole-proof audit: D-OL22–24

**PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, reasoning effort inherited/unexposed, HODGE_DIVISION. The complete frozen proof, every author certificate line, its complete output, and the source/status record were read. The mathematical and independent computational review was completed on 2026-11-21 after the final successful computation at **23:19:59.434623 UTC**. No mathematical repair was requested.

The frozen proof is `agents/imprimitive/spin_odd/spin_odd_extension_section.tex`, SHA **a5b4c58088ddd71709ff7067670bd9d2ce71f25a02a0710cdfb557db79ca9e44**. The author checker is `check_spin_odd.py`, SHA `5f281945662eb61b08791c5da1fd990da91bd44e816246e8c44d09dae45a4f3b`; its original output hash is `dd1646075122be046803968da54c7ce82786833f677523f38f2f283a8f390700`.

## Scope and relation to previous work

The new order-four lemma treats odd natural dimension at least 25 over F3. Its all-normalizer and source consequences require odd natural dimension at least 1135 over arbitrary odd finite fields. They permit every nontrivial irreducible complex Spin module, arbitrary represented central kernel, compatible outer normalizers and scalars, mixed factors and factor permutations. No ordinary descent, full-orthogonal extension, selfduality or determinant assumption is inserted.

The parity-free Clifford and radical interfaces D-OL19 and the opening of D-OL20 were independently checked in full immediately before this audit; that separate report is `SPIN_EVEN_EXTENSION_PEER_AUDIT.md`. The new proof uses their actual represented-kernel preservation, exact natural/represented projective orders, unique odd-primary lifts and full inverse-image Levi action. This audit does not claim independent origin of those earlier arguments. Root contributed the order-four strategy to the author; the present review is a separate whole-proof check and independent finite reconstruction, not a claim that every idea originated independently.

## 1. The fourth-order natural geometry

For `g²=-r_v`, the nonsingular line and its perpendicular are preserved. On the perpendicular the minimal polynomial divides the irreducible polynomial `x²+1`, so its determinant is one. The determinant-one condition on g then forces its action on the line to be +1. This is valid even if g lies outside Omega.

The trace construction in (OSP.5) is Hermitian over F9: the adjoint of g on the perpendicular is minus g, multiplication in the first variable is F9-linear and multiplication in the second is conjugate-linear, and the field trace gives the original nondegenerate polar form. A Hermitian hyperbolic pair gives the required opposite invariant F3-planes. The resulting complement W has **odd** dimension N; none of the subsequent counts assumes N is even.

The two-plane radical matrix and its central correction are the actual orthogonal radical. The previous generation proof works in either parity once the complement is sufficiently large: it extracts full opposite line radicals and generates Omega. The unique lifted radicals therefore generate Spin and have fixed spaces of equal dimension and zero intersection on a nontrivial irreducible module. This gives `t0≤a/2` without ordinary descent.

Conjugation acts by `X→AXh⁻¹`, fixes the center because `det A=1`, and preserves the zero-central-coordinate section. On the one-dimensional fixed line of h, the quotient action is the irreducible two-dimensional order-four matrix A. On its perpendicular it is an involution, whose fixed maps are F9-linear. Thus the fixed dimensions of the first, second and third powers are exactly `N−1, 2N−2, N−1`. The dual fixed maps land in W1 and are F9-linear; every nonzero one has rank two.

## 2. Linear weights and nonlinear carriers

The rank-two Levi orbits consist of independent ordered pairs with a specified Gram matrix, including degenerate Gram matrices. The required Witt extension can be corrected into Omega in the large perpendicular space. The first-vector Gauss bound and affine second-vector Gauss bound remain valid for odd N; the irrational expression `q^(N/2)` is simply an upper error bound. The author's integer check uses a larger integral error and is therefore safe.

Every such orbit has more than `q^(2N−3)/4` members, while the total number of fixed dual maps is at most `q^(N−1)`. Thus each nonzero orbit's fixed fraction is below `4q^(−N+2)<1/8`. Rank-one orbits have no fixed map. Constancy of weight multiplicities under the full lifted Levi then gives the aggregate bound even if the natural action permutes individual Levi orbits. Nonfixed weight cycles have length two or four, so each contributes at most half its total dimension to any specified eigenspace. This proves the `7/16` support fraction on all nontrivial linear-weight sectors.

For every nontrivial central character, the canonical Heisenberg carrier has degree `q^N` and an exact Weyl basis of its full matrix algebra. The center and zero-central-coordinate section are fixed, so the intertwiner permutes that basis without phases. It may be chosen unitary and normalized to fourth power one. The traces of its first three powers consequently have magnitudes `q^((N−1)/2), q^(N−1), q^((N−1)/2)`. The four-term Fourier formula gives the displayed maximum-eigenspace bound, strictly below `9q^N/16` for N≥21.

On an entire central-character isotypic component the actual operator is the carrier tensor an arbitrary multiplicity operator. Finite projective order permits diagonalization after scalar normalization. Spectral convolution retains the carrier support bound, so no multiplicity or phase is discarded. Combining linear, nonlinear and trivial-radical sectors yields `ν(T)≥7a/32`. This step is the genuinely new endpoint needed for an order-four SO element outside Omega.

## 3. All projective orders and compatible normalizers

The nonzero line-weight orbit degree estimate applies directly to every Spin module and gives a degree greater than 360 in the final range. It does not invoke an ordinary-character minimum-degree theorem.

The natural and represented projective orders agree by the already checked lifting lemma. Taking a nontrivial prime-order projective power cannot increase support. Arbitrary field components use the previously proved norm/form descent and lifted line weights, giving `3a/16`; the argument includes mixed graph/diagonal-field representatives.

In odd natural dimension the multiplier of a linear similitude is a square. Scalar normalization followed by the unique determinant-one choice gives a unique SO representative, and SO has no nontrivial natural scalar. Hence its ordinary order is the actual projective order. For odd prime order it has trivial spinor norm, lies in Omega and lifts to Spin; the represented normalizer differs from that Spin action by a scalar. The hyperbolic-pair case uses the transferred line estimate. Without such a pair the restricted natural support is at least 567, both for semisimple and characteristic-prime elements, so the published LST theorem applies directly to the genuine Spin character.

For involutions the only weak case is a projective reflection. Its unique SO representative in odd dimension is the negative reflection. The exact rank-one weight fraction gives the stated beta bound at q=3 and the stronger bound at q≥5.

The all-order reduction is complete. At q=3 a low-support projective order has no odd prime factor. If its order is `2^s` with s≥3, its square lies in Omega and an even power of that square is a negative reflection. Both ±1 eigenspaces of the square therefore lie in the reflection's one-dimensional fixed line, so its restricted support is at least d−1. LST applies to a Spin lift of the square without a prime-order restriction, contradicting low support. For s=2 the new fourth-order lemma applies whether or not the original SO element lies in Omega. Only projective order two remains. The proof correctly allows a nontrivial central scalar in the square of the original complex operator.

## 4. Actual source and mixed-parity conclusion

Factor permutations have the prior quarter support bound. Scalar nonidentity inertia is automatically good. A bad factor-preserving operator has only q=3 negative-reflection active factors. The two normalized eigenspace proportions lie between beta and one minus beta. Two active factors already force support above one quarter; additional factors cannot increase the maximal eigenspace proportion. Hence every bad inertia has exactly one active factor.

The actual intermediate-cover Euler identity and finite pointed-Hurwitz parameter bound force a sphere, at least twelve genuine marks and total moving rank `2e+6`. The exact inequalities then force precisely twelve bad inertias. These actual generators project onto every represented factor's full simple inner group. For q≠3 their projection is trivial, impossible. At q=3 at most twelve natural reflections represent their projective images. Their common perpendicular has positive dimension and is pointwise fixed by all reflection words. Every Omega element acts there by a ground-field scalar. Perfectness kills the scalar character, contradicting the absence of natural fixed vectors. This uses the natural simple projection and remains valid for all represented central kernels.

The final mixed-parity statement follows with exactly the same constants from the independently checked even-dimensional theorem: odd dimensions at least 1135 and even dimensions at least 1136 can be combined. The remaining bounds 1133 and 1134 are necessary bounds only, not existence assertions.

## 5. Sources actually read or reused

I freshly read Taylor's complete Lemma 10.2, Corollary 10.3 and ensuing Hermitian decomposition on printed pp.116–117 in the corrected author version, reopened at <https://www.maths.usyd.edu.au/u/don/papers/gcg.pdf>. Local cache: `agents/imprimitive/orthogonal_lowlevels/cache/TaylorClassicalGroups.pdf/.txt`. This verifies the hyperbolic-pair input in its full stated domain.

Wonenburger Part II pp.48–49 and LST Theorem 4.3.6 Step 1 pp.1918–1919 were freshly read in the immediately preceding even-Spin audit. The LST full theorem/proof pp.1917–1923 and restricted-support Remark 4.3.7 were already read completely in this run; their exact Spin and non-prime-element scope was rechecked here. The published Annals PDF was reopened during this review sequence. The radical, orbit, natural-normalizer and arbitrary-field-descent dependencies were reopened in the preceding even-Spin review. No fresh full rederivation of the Li–Xia table, all Taylor classification proofs or the complete LST theorem is claimed in this event.

## 6. Independent finite supplement

Own files: `audit_spin_odd_carrier.py` and `audit_spin_odd_carrier.json`. No author program, arithmetic module, selected-row data or certificate is imported. The author program was read before writing this program, which is disclosed.

The independent calculation uses actual carrier matrices modulo 13, containing distinct third and fourth roots, and separately derives characteristic-zero Fourier multiplicities from exact root counts and complete linear-character coefficients for the square kernel. Thus a modular trace alone is not used to infer a complex multiplicity. For degrees 27 and 243 it reconstructs `(9,9,6,3)` and `(81,81,45,36)`; independent modular kernel ranks agree.

It exhaustively considers **59,778** dual maps in the smaller natural models, recovering all 90 fixed maps and their rank-two property. Four natural models with N=3,5,11,21 give the exact three fixed dimensions. All **729 actual Weyl matrices** in the degree-27 model satisfy conjugation covariance by direct matrix multiplication. There are **59,778** exact trace terms and **59,778** full square-kernel linear characters. A different primitive-eighth-root matrix gives the required order-eight natural witness and restricted square eigenspace dimensions `(1,0)`. All endpoint constants are exact rational inequalities.

The first run passed at **23:19:31.764249 UTC**, elapsed **1.192861824 seconds**. A further complete square-kernel coefficient check was then added to make the characteristic-zero spectral bridge explicit; the final run passed at **23:19:59.434623 UTC**, elapsed **0.467313632 seconds**. There was no failed assertion or mathematical repair. Both successful executions are recorded in `audit_spin_odd_carrier_attempts.json`.

These are finite natural, carrier and constant checks. They do not computationally prove universal group generation, the Clifford lift, finite-field Witt theory, the published character estimate or the actual-cover argument. Those are covered by the written review. No new TeX compilation claim is made.

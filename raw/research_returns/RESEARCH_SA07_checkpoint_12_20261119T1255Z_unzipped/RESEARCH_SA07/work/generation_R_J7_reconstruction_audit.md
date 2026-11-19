# Independent audit of F.3.34

19 November 2026. Checker: GPT-6 Astra / period_generation. Verdict: **passed at the stated published-dimension-input scope**.

## Exact source checks

I read the integrated F.3.34 proof and the complete standalone `check_R_J7_six_generators.py`. I independently reread the original MSS2015 v2 text on printed pp. 16–17 and 29–30, and rendered and visually inspected pp. 16 and 30. Proposition 3.4(i) gives the actual stabilization diagram for the Johnson image. Proposition 3.5(ii) states the zero intersection of the actual Johnson image with the filling ideal in degree other than two. The proof of Theorem 7.5(iv) gives standard-representation multiplicities ten and three in the special derivation space and filling ideal, and ES-image multiplicities three and two. The printed p. 30 explicitly concludes that the actual degree-seven Johnson image contains six copies of the standard representation.

For the upper bound used here, the ES kernel has multiplicity seven, while its intersection with the filling ideal has multiplicity one. Since the actual Johnson image is inside that kernel and disjoint from the filling ideal, its multiplicity is at most six. This is an exact dimension argument using the source's stated ranks; this audit does not recompute those older character or ES-rank calculations.

The five coefficients and four-pair contractions in MSS2026 Proposition 4.1, printed p. 11, agree term for term with `rterms` in the script and with (SL.3). The new proof uses that displayed formula and does not import the 2026 sketch's vanishing assertion.

## Actual vectors, maps, and the isotypical argument

The literal degree-one derivation is `delta_t(z)=sum <z,t_i>[t_(i+1),t_(i+2)]`. The code uses the paired input `t_i^1` with the coefficient `<t_i^1,t_i>`, so its signs implement this formula. Its ordinary commutator is composition in the two orders with the required minus sign. The tensor root coefficient gives exactly `sum(x_i tensor D(y_i)-y_i tensor D(x_i))`.

Each of the six witnesses is a sevenfold bracket of actual degree-one Johnson elements. Closure of the actual Johnson image under the bracket puts each witness in its degree-seven piece. The script independently verifies degree, the exact torus weight `x1` on every tensor term, and the literal equation `D(omega)=0`.

The six displayed contraction maps are symplectic-equivariant with codomain the standard representation. Thus they, and R, kill every other irreducible isotypical summand. Complete reducibility supplies the standard-isotypical projector, which preserves the actual Johnson submodule. The nonzero six-by-six detector determinant proves that the six projected witnesses are independent in its weight-`x1` space. The older upper bound makes these six vectors a basis of that weight space. Their symplectic orbits span the full standard-isotypical component. Since R kills the six witnesses, equivariance kills that entire component and hence the full Johnson image.

The integrated proof correctly needs neither completeness of all 105 contractions nor a new theorem generating the whole degree-seven Johnson image from degree one. It uses only six actual brackets, six explicit equivariant maps, and the published multiplicity bound.

## Exact finite computation

A fresh full run succeeded with external wall time **3.207956781 s** and internal time **3.043775791 s**. It recovered pivot contractions `(1,2,4,7,8,10)`, the displayed six-by-six integer matrix, determinant **−203784**, and all six R-values equal to zero. The run reads no stored detector matrix or output witness file. Every arithmetic coefficient and determinant is exact.

- Program SHA-256: `a516e276fa0d763f4e9afb4108939bd078a96ed170ecbec2494d1560cccac97b`.
- Saved output: `work/generation_R_J7_independent.output.txt`.
- Saved run metadata: `work/generation_R_J7_independent.meta.json`.

## Every genus and every prime

The witnesses use five handles, so their literal tensors and contraction coefficients remain unchanged in every larger genus. The proof chooses a genus in the older source's stable range without asserting an unverified minimum cutoff. For any original genus at least three, actual extension of a boundary mapping class by the identity gives the Johnson derivation extended by zero. The source's Proposition 3.4(i) verifies this exact stabilization map. The literal contraction formula satisfies `R_G(i^tensor9 T)=i R_g(T)`, and injectivity of i transfers stable vanishing to the original genus.

The actual strict Malcev/Johnson-image comparison used in F.3.24 remains the previously checked map. No density assertion for discrete filtration kernels is used. Finally the determinant is nonzero over Q and therefore over every Q_l, including primes dividing its integer numerator. This proves exactly the claimed characteristic-zero scalar extensions.

## Source access records

- Original MSS2015 v2: `work/sources_audit_next/MoritaSakasaiSuzuki2015_v2.pdf`, https://arxiv.org/pdf/1404.3351 . Printed pp. 16–17, 29–30 read; pp. 16 and 30 visually checked. Rendered images: `generation_MSS2015_p16.png`, `generation_MSS2015_p30.png` in the same directory.
- Original MSS2026 v1: `work/sources_audit_next/FirstGaloisObstruction2026_arxiv2608_17673.pdf`, https://arxiv.org/pdf/2608.17673 . Printed p. 11 formula rechecked against literal code; the earlier independent F.3.32 audit visually checked this page.
- Exact actual-generation/strict-image source maps are recorded separately in `work/generation_johnson_degree_seven_generation.md`.

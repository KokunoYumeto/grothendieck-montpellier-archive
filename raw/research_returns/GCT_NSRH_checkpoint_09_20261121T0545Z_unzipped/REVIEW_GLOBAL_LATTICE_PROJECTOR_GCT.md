# F49 independent whole-proof review

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro; inherited effort is not exposed. Date: 21 November 2026 UTC. Verification type: fresh full-report reading, direct elementary reconstruction of all new proofs, and fresh reading of the relevant supplied IV/VIII source contexts. This is not a formal proof-kernel certificate or an independent rerun of the prior F43 matrix script.

Reviewed file: `agent_global_lattice_projector.md`.

SHA-256: `68857a06d679f9977d88092708b67521fa38139d2bd77e10fdfa7e843eba3824`.

**Result: PASS. No mathematical blocker or required correction.**

## Actual matrix and invariant-subspace checks

I reconstructed the canonical-to-monomial transformation and both projector matrices in (L9). With u=(v,1,v^-1), the outer product divided by h is idempotent because u times its transpose equals h. Its image is the actual b1 line, and direct dot products with both complementary rows in (L4) vanish. Expanding the first row in the canonical basis gives exactly the monomial image (v^2,v,1)/h. The lower-weight version and endpoint identity are consistent with the previously certified actual W3/W1 decomposition. Hence the projector commutes with the ordinary Hecke action and with ordinary left E,F,K, and its tensor product with identity commutes with both actual nonstandard generators.

The coefficient 1/h at the specified original tensor monomial is genuine. Since h is not a Laurent monomial, it is not a unit. The preservation obstruction is intrinsic to the original module, so no basis of that same lattice can repair it. The monic-integrality argument is valid over Q[v,v^-1], after adjoining i, after algebraic coefficient extension with integral closure, and after first adjoining the square root of a smaller parameter.

## Actual F43/F46 comparison

I checked the multiplicity selectors from (L13): the first sixteen epsilon-plus coordinates contribute rank16, and the first eight N(delta) multiplicities contribute rank16, giving the rank32 projector p_V tensor identity. The operator (L15) on K selects exactly those multiplicity coordinates; the right-module comparison changes only the two-dimensional factor and therefore leaves these selectors unchanged. Under the exact postcomposition/Morita isomorphism of F46, this is the same actual operator, not merely an isomorphic abstract idempotent. Its coherent interpretation as a literal direct-summand projector is valid.

## Bar, boundary and designated-form checks

The actual tensor bar fixes the relevant F43 basis vectors, so both decomposition summands and their projector are bar stable. The displayed S_a and the coefficient-base bar are compatible because a, D, Delta, s, lambda are invariant; the relevant inverses exist in F46's stated localization. This is a chosen framed bar comparison, as the report explicitly says.

For every exponent -2 through 2, v^j/h has order j+2 at zero and 2-j at infinity, both nonnegative. The stated two boundary lattice preservation claims follow. Neither boundary claim silently identifies these lattices with VIII's conjectural local lattice.

I freshly read VIII's definitions of K_Q and the coordinate global form (supplied source approximately lines 477–540 and 678–710), the dual global form and pairing (approximately lines 746–795), and Proposition platticeinjection with its placeholder proof and conditional local assertion (approximately lines 876–915). The report's independent proof of the needed global inclusion is correct: every original tensor-coaction matrix coefficient is a degree-three product in the designated coordinate form, and pairing with the dual form therefore gives integral matrix entries. The nonintegral coefficient excludes this actual p. It does not assert the unfilled conditional local statement, does not require Conjecture 2.2, and does not refute a canonical basis of the designated form.

I also freshly read the complete relevant IV Conjecture 19.1 discussion and Example 19.2 (supplied source approximately lines 7867–8070). The explicit warning that the desired integral and local forms differ from the original tensor forms is retained, and the known rank-three basis is correctly treated as existing work. Exact PDF page numbering in the report is the author's separately checked primary-source input; this reviewer read the complete supplied TeX contexts rather than independently reopening every PDF page. The EGA/SGA archive locators in the final framework paragraph are prior audited inputs, not a fresh archive-image verification here.

The final claim is properly limited to simultaneous retention of the original global lattice, actual tensor action, and the full specified localized commutant matrix units. Alternate lattices, a smaller integral commutant, and the named nonstandard generators alone remain outside the obstruction.

## Final fragment match

Corrected report SHA-256: `80e971b423940d694701d30ff48c12ec2ea50f1b96ac72ca3c9e1904d1994788`.

Generated fragment: `finding_F49.tex`, SHA-256 `d96ea5437ab9959a42f807ec3d4aa2baa1c35bebf89c4ba4c4505bb697fa7f2c`.

I directly read the complete generated fragment. It matches every checked proof and limitation above. The only report addition was the parent's requested IV Theorem12.1 tensor-dual convention note: transpose preserves the global matrix-entry criterion, and the actual monomial projector matrices are symmetric. That note is mathematically correct and appears explicitly in the fragment. The separate dictionary retains the previously audited framework locators without turning them into sources for the new projector calculation. Final full-fragment match: PASS; no required correction.

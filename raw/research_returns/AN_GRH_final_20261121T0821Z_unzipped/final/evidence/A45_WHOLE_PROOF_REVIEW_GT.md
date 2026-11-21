# A45 independent complete-proof review

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Source: work/effective_galois/nonconstant_deck/A45_COMPLETE.tex.  
Whole-read mathematical version: e6577cdf1bfb85815c9996d7b55f74112f5aeb95eb7b2ba0c3a238a032394d42.  
Final narrowly checked version: 857762034e0810724f154a54c4f7ee3c71e31df8cfba45242ae9f5961856a417.

## Result and actual scope

PASS. I read every paragraph of the combined mathematical manuscript, including the five-step all-characteristic bounded-exponent theorem, the entire finite etale semilinear descent proof and its conductor application, and all three steps of the actual degree39 comparison. I then checked the final provenance-only paragraph at 1e930f85e1658b909ec1a44723535c7383dad39405b6812209543bec737e11c5 and the added actual-conductor norm/pullback precision at the final85776203 hash. No mathematical correction was requested.

This is an independent complete-proof read with two narrow final-delta checks. It is not a second derivation of the finite divisor arithmetic. I did not execute a new implementation or rerun the supplied arithmetic scripts. The finite point table is a supplied input with separate producer and independent Cantor checks retained by the other agents. The primary descent and mod-p comparison theorems are used as cited; I do not claim to have freshly reread their entire external proofs in this review.

## Bounded-exponent theorem

The rational projection b=delta-r*pi^*Nm(delta) is well-defined on the chosen p-power torsion group. Both maps descend before deck constantization. The identity n*b=(n-S)delta and r*n=1 on the torsion show b lies in the connected norm kernel, using im(sigma-1)=B. This avoids the false inference that the geometric deck translate itself must be rational.

Taking the exact order m of (sigma-1)delta ensures the resulting degree2m function is separable: a pth-power root would contradict exactness. The controlled-field bound applies to all degree2m conjugates. Its index e is coprime to the odd prime-to-p deck order; hence the action on the intermediate curve is faithful and free. The low genus bound makes that curve and its deck quotient genus one.

The coincident-positive-fibre alternative forces both negative points to share a fibre too and then sigma squared to fix a point, impossible for a free odd cyclic action. Otherwise each positive fibre is a singleton, e divides m, and all2n points in the two deck orbits have wild different exponent at least e. Riemann-Hurwitz gives p<=e<=g-1. The field compositum argument produces the stated actual degree-p-power elliptic map on the base and total ramification at both points. Thus the unconditional genus range2<=g<=p is correct, and no larger-genus exclusion is silently claimed.

## Primitive semilinear descent

The full cyclotomic algebra must be retained. After an unramified splitting extension its primitive roots form a permutation set, and multiplication by a acts freely with the exact order f. The displayed tensor-product map is therefore the finite etale torsor isomorphism after a faithfully flat base change. Module descent applies to torsion modules without dividing by f; this remains valid when p divides f. The equality of exponents follows in both directions from the tensor-product identification and subgroup inclusion.

The actual conductor images im(n e_d) descend because the integer Ramanujan projectors are invariant under arithmetic deck conjugation. Their p-primary groups are the corresponding idempotent modules, because n is a p-unit. The primitive conductor-d exponent is unchanged over its own minimal constantization field k_(f_d). A larger field constantizing the entire composite deck group can enlarge proper-conductor exponents; the statement correctly keeps f_d distinct from f.

## Actual degree39 example

The trace-one quadratic twist changes Jacobian Frobenius to its negative. The stated actions give1 modulo9 and8 modulo13, hence34 modulo39 of order4. The Frobenius-stable quotient of the kernel of Phi^4-1 descends over F4, and the zero point makes the Lang pullback pointed at W. Its geometric deck group is cyclic39 and its minimal deck field is F256. The full Abel-Jacobi connectedness input applies.

For conductor3, the four F4 labels0,0,1,2 give c_chi=1 and L_chi(1)=6. Over F256 the marginal table gives c_chi=-17 and L_chi(1)=240. The unit-root integral module argument gives exact exponents2 and16. The final precision is correct: norm and pullback for the degree13 quotient have composite[13] in both directions on the conductor3 summand, so they identify the actual two-primary modules over either field. The conductor13 table gives odd class number over F256, hence no rational two-primary torsion over either field.

For conductor39, the exact reduction is2 times a unit in the entire etale algebra O39, so the norm has two-adic valuation24. Its reduction also gives c_chi=1 for each primitive character. Over the constant deck field, the K-linear256-Frobenius commutes with the deck action; after extending scalars, the primitive coherent eigenspaces are distinct one-dimensional lines. The reduced character polynomial1+T therefore makes this linear Frobenius the identity on the entire24-dimensional primitive space. The cited Artin-Schreier stable-part comparison gives ordinarity and all2^24 geometric etale two-torsion points rational over K. This does not assume that K contains the39th roots of unity: the linear character decomposition is made after scalar extension.

The exact total two-primary order2^24 consequently equals the already rational elementary two-torsion subgroup, proving exponent2. Semilinear descent preserves that exponent over F4. Taking the maximum over conductors3,13,39 gives2 over F4 and16 over F256. The ordinary dimensions2+12+24=38 and base two-rank1 give cover genus40 and two-rank39. Both numerical inequalities,39>9 and39<=961, are correct. The result concerns this one pointed cover and does not claim that every cover fails after constantization or that no other witness exists.

## Final delta checks

The computation-only paragraph accurately distinguishes the independently coded Cantor calculation from the earlier linear-interpolation producer and from a subsequent unchanged replay; no replay is called a third implementation. Its reported computational facts are independently documented by the corresponding agents, not newly recomputed here.

The final added paragraph after ND.19 identifies the degree-three Prym with the actual conductor3 subvariety using a degree13 map defined over both fields. The sum over its deck subgroup acts as13 on conductor3. Thus both composites are multiplication by13 on the relevant modules, an automorphism on two-primary points. PASS.

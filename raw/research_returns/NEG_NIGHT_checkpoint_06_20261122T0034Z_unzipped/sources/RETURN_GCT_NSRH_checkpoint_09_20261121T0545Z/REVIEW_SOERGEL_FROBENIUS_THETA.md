# Independent whole-proof review: F59 finite Frobenius closure

Reviewer: /root/rectangular_and_theta  
Date: 2026-11-21 UTC  
Review type: independent reconstruction of the complete mathematical proof and source applicability; report-to-fragment comparison recorded separately below.

## Verdict and exact target

**PASS. No remaining mathematical blocker found.**

Reviewed report:
- agent_soergel_frobenius_closure.md
- SHA256: 7b354be09d00bedd715adbd2461ce56add9bcdf663551170435db744d233a647

The report closes the previously remaining bounded coupled-complex case in the precisely stated ordinary type-A Soergel category. It does not assert a result for arbitrary derived bimodules, arbitrary coefficient complexes, or unbounded completions.

I read the entire report, independently reconstructed the proof, and re-read the final hypothesis corrections. This is not a review based only on headings or on the author's computation. The argument is mathematical; no computer calculation is needed to establish its general conclusion.

## 1. Corrected centrality hypothesis and quotient tensor identity

The final statement correctly requires a set of homogeneous generators of I to act identically on the left and right of every term. It does not require every A-multiple of an invariant generator to act centrally. That stronger condition would fail in the intended Soergel application.

If c is one of the central generators, then (ac)m = a(mc) = (am)c, so IM is contained in MI; the reverse inclusion follows similarly. This proves IM=MI termwise. Moving an ideal generator across the balanced tensor product gives
IM tensor_A N = MI tensor_A N = M tensor_A IN.
Consequently both sides of FC4 are the same quotient of M tensor_k N by the balancing and ideal relations.

The termwise quotient is additive, and an additive functor preserves the chain-homotopy equations. Thus the homotopy quadratic descends to the central fiber without a flatness claim for the invariant subring and without a cohomology-and-base-change claim. The resulting terms are finite free over B on both sides, using the two descriptions of the quotient.

## 2. Nonzero reduced cohomology

The Euler-rank hypothesis is actually used:
chi_k(Z) = dim_k(B) times the Euler left rank of X.
This is nonzero. Hence Z is nonzero in the derived category. Merely retaining a nonzero homotopy class of a bounded free complex over a nonregular fiber would not suffice; the final proof correctly avoids that gap.

For the actual generator the Euler rank is four. This follows either from the generic graph calculation or from sending b_s to delta and b_s-delta to zero in the ordinary left graded-rank character.

## 3. Upper amplitude

For nonzero finite right and left modules over the commutative local algebra B, their tensor product is nonzero. The quotient onto the tensor product of their nonzero residue modules proves this by Nakayama. The argument uses only the right action in the first factor and the left action in the second, so it does not assume the two bimodule actions coincide.

For r=max{i:H^i(Z) nonzero}, the standard truncation argument gives
H^(2r)(Z tensor_B^L Z) = H^r(Z) tensor_B H^r(Z).
All terms below the top contribute below 2r, and higher Tor of the top modules contributes in lower, not higher, cohomological degrees. Thus the top degree is exactly 2r. The coefficient object is in cohomological degree zero, so the quadratic gives 2r=r and r=0.

## 4. Lower amplitude and graded Frobenius duality

The final report explicitly assumes a homogeneous Frobenius functional. This justifies the statement that the graded right dual is the vector-space dual with one fixed internal shift. It does not introduce a cohomological shift.

I checked the pairing formula. For a functional psi on a finite right B-module, nondegeneracy determines phi(m) by
tau(phi(m)b)=psi(mb).
This recovers the right-linear map and identifies the module dual with the exact k-dual. It interchanges the left and right actions. Bifreeness therefore passes to the dual.

The right dual is anti-monoidal for bifinite-projective bimodules. One termwise formula sends a reversed pair of right-linear functionals f and g to
x tensor y -> f(g(x)y).
This is balanced and gives the finite-dual-basis tensor-Hom isomorphism; the total-complex version has the standard Koszul signs. The proof does not assume that the bimodule category is symmetric.

The coefficient object is self-dual because the internal shifts 2 and -2 exchange. It is a direct sum of shifted units and therefore commutes with the other factor. The dual satisfies the same quadratic. Applying the upper-degree proof to the exact dual forces the original bottom cohomological degree to be zero.

## 5. Fiber projectivity and the global minimal complex

The bounded left-free complex with only H^0 gives a finite projective resolution after the positive acyclic tail is split from its top. A finite Frobenius algebra is self-injective: its regular module is a shift of its vector-space dual, and Hom_B(-,D_k B) is exact. Splitting the finite resolution from its left end proves H^0(Z) projective.

The proof uses these splittings only in the left-module category. It does not turn a left-module contracting homotopy into a bimodule homotopy.

Over connected graded A, a nonzero constant differential entry is a homogeneous unit and can be cancelled by graded row/column operations. Repeating gives a bounded minimal left-free complex F with all differential entries in A_+. Reduction modulo I retains minimality over the connected finite graded local algebra B.

The reduced complex is left-homotopy equivalent to the projective H^0(Z) in degree zero. Tensoring this homotopy equivalence with the residue field is valid even though it need not preserve arbitrary quasi-isomorphisms: it is an actual homotopy equivalence. The reduced minimal differential is zero, so every term outside cohomological degree zero must have rank zero. This proves global cohomology concentration and left graded freeness.

## 6. Every type-A central-fiber hypothesis

I checked the full elementary proof, not only the n=2 case.

The elementary symmetric polynomials lie in every simple-reflection invariant subring, so the displayed generators act centrally on all Bott--Samelson terms and then on shifts and direct summands.

The equality of ideals
(e_1,...,e_n) = (h_1(x_1,...,x_n),...,h_n(x_n))
is correct. One inclusion follows from the tail-inverse formal-series identity after the full product is 1. For the reverse inclusion, descending induction uses the recurrence
H_j = H_(j+1)/(1-x_j t)
and the vanishing degree-j coefficient to kill every coefficient above degree j-1. The induction starts from the empty-tail series.

Each triangular polynomial is monic in its new variable. The successive monic quotients give the stated Artin basis, dimension n!, and finite connected graded locality.

For a monic extension T[z]/(f) of degree j, coefficient extraction at z^(j-1) yields the pairing matrix whose reverse diagonal is 1 and whose entries on one side are zero. Reversing the columns makes it triangular with unit diagonal, so its determinant is a unit over T, even if T has zero divisors. Composing with the preceding Frobenius functional gives a nondegenerate k-pairing. Homogeneity of the relations makes the resulting functional homogeneous, supported in top degree.

The tensor product of the two finite connected graded Frobenius algebras is again finite connected graded local Frobenius. Finite graded-projective summands of free polynomial modules are graded free: lift a homogeneous residue basis, split the resulting graded surjection, and apply graded Nakayama to its complementary kernel. This avoids an unnecessary ungraded Quillen--Suslin invocation.

## 7. Actual derived implication and codimension-two graph splitting

The previously checked generic localization proof supplies support e and tau=(s,s), each with multiplicity two, and only cohomological degree zero. It supplies the Euler rank four required above.

After the finite-fiber argument, M=H^0(X) is finite graded-free on the left. In coordinates flipped independently by tau, its right multiplication matrices U and V satisfy yU=xV and U^2=x^2 I generically. Left freeness extends these polynomial identities over A. Coprimality of x and y gives U=xZ, V=yZ, with Z homogeneous of degree zero and Z^2=I.

The idempotents (I+Z)/2 and (I-Z)/2 commute with the right action and split M into the identity and tau graph pieces. Fixed coordinates act by their left scalars by the same generic-equality/torsion-freeness argument. The graded projective pieces are graded free by the residue-basis argument. Thus their multiplicities are actual polynomials a(v),b(v) in N[v,v^-1], with b nonzero.

This also proves right freeness. The canonical derived truncation, rather than the left-module homotopy splitting, identifies X with M as a derived bimodule. Derived tensoring M is now ordinary tensoring, so the actual quadratic descends to an actual graded module isomorphism.

There is no nonzero map between the two graph types: the scalar of such a map is killed by 2x in the polynomial domain. Comparing the two graded multiplicities gives
a^2+b^2=delta^2 a and 2ab=delta^2 b.
Since b is nonzero, 2a=v^2+2+v^-2, impossible in the integral Laurent ring. This is an integral graded-multiplicity contradiction, not an assertion of positivity for a virtual Euler class.

## 8. Source and scope audit

The ordinary Soergel, localization and Rouquier sources were independently read in the core review:
REVIEW_SOERGEL_DERIVED_THETA.md,
SHA256 37ddd577acc57d9e0ad5e2f36b0c162fbb62c0018077abd80b6db40126aef2fa.

The new finite-fiber theorem and its application are proved here. The standard type-A coinvariant background is explicitly verified, with no claim that it is novel. The EGA/SGA references are framework anchors for affine modules, perfect complexes and coefficient gradings. None is presented as proving this new categorical obstruction.

The conclusion applies to bounded ordinary type-A Soergel complexes with the actual ambient Euler class and the specified cohomologically degree-zero coefficient object, satisfying an actual homotopy quadratic. It does not apply automatically to unbounded completions, a different coefficient complex, a localization removing the finite fiber, an altered Hecke K0 comparison, or arbitrary derived bimodules. It neither contradicts the fixed-rank positive kernel constructions nor refutes the source's signed/factored positivity statements.

The finite Frobenius algebra used in the proof has no arithmetic Frobenius operator, and the argument invokes no Weil-weight theorem.

## 9. Review history

Two hypothesis precision issues were corrected before this final PASS:
1. central homogeneous generators, not centrality of every element of I;
2. a homogeneous Frobenius functional for the graded duality statement.

Both changes are present in the exact target hash above. They leave the intended type-A application valid and repair the general lemma's wording.

The earlier coupled-support report's residual-open statements are historically scoped before this strengthening. They should not be read as a current claim that the ordinary bounded case remains open.

## 10. Complete final-fragment comparison

I read the complete 369-line fragment finding_F59_frobenius.tex, SHA256
8c5944021f382e24c6d4c4a62f65708b441c1b759bf82829f9748b26cc999303,
and matched every mathematical step and the separate dictionary against the final report.

**Final-fragment PASS.** It retains the corrected central-generator hypothesis, homogeneous functional, actual homotopy quotient, nonzero Euler fiber, both cohomological bounds, left-only splitting/minimality, elementary all-type-A Frobenius proof, actual derived bimodule truncation and the integral graph-multiplicity contradiction. All stated limitations remain. No new mathematical claim requiring an additional verification was introduced by the fragment.



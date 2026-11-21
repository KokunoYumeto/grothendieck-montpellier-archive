# D-OL14–15 independent whole-proof audit

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. **PASS** on the complete frozen proof `agents/imprimitive/orthogonal_lowlevels/orthogonal_three_odd_section.tex`, SHA-256 `7d0e8c1e9e9023e0840b306642696c942020cc870c2460f5265a1a9feb947e5b`.

I read the entire proof, entire author checker and output, source/status notes, and the exact preceding signed-radical and normalizer interfaces. No mathematical or scope repair was requested. This audit covers the actual ordinary nonselfdual module statement, mixed natural dimensions, all scalar phases and compatible tensor permutations. It does not extend it to arbitrary faithful spin representations.

## All-order inner-element classification

The fixed-hyperbolic-pair case has actual moving rank at least two on the complementary natural space: the excluded rank-one isometry is a determinant-minus-one reflection, while the original element lies in the natural derived group. The arbitrary-rank Gauss estimate is correctly split into rank at most half the dimension and the complementary case. The former uses the lower polar rank of the fixed subspace; the latter uses the trivial sum bound. Both give the printed rank-two fixed-fraction bound, hence support at least `7a/32` by the actual prime-order weight orbits and the opposite-radical fixed-space bound.

For odd-prime order without a fixed hyperbolic pair, a semisimple fixed space is nondegenerate of dimension at most two. In defining characteristic, its polar rank is at least `d−2r`; rank at least three would contain a hyperbolic pair over the finite odd field. The integer bound is therefore 567 at the stated odd natural dimension. In both cases the minus-one eigenspace is absent. This is precisely restricted natural mu2 support, not a minimum over all extension-field eigenvalues.

The remaining involution is exactly a negative reflection. Its positive eigenspace is nondegenerate and has odd dimension at most two, hence dimension one. On a hyperbolic pair in the negative eigenspace, the signed radical action is minus the complementary action, so it has rank one. The proof retains the correct weaker fixed-fraction bound instead of importing the previously refuted quarter bound. Its exact rational support exceeds beta.

I checked the important arbitrary-order refinement separately. If an odd prime divides the order, an odd-prime-order power gives the strong bound. For a higher power of two, either its involution power is already good or that power is a negative reflection. In the latter case every natural plus-or-minus-one eigenvector of the original element lies on the positive line of the involution power. Thus its restricted support is at least `d−1`, and the published character theorem applies directly to the original element, without a prime-order assumption. This excludes higher roots from the exceptional class; the exception really is an actual negative reflection.

The natural group is centerless in odd dimension and simple in the stated range. Thus a nontrivial ordinary irreducible representation has trivial projective kernel. Power reduction and the later meaning of an active factor have no hidden scalar-kernel exception.

## Complete compatible-normalizer scope

At q=3 there is no field part. The large odd-dimensional automorphism group has just the natural linear diagonal outer coset. The odd-dimensional similitude scalar is removable because its multiplier is a square, and the full orthogonal group is the central minus-one extension of SO. The quotient of SO by Omega has order two.

If the nontrivial outer coset stabilized a nonselfdual character, every element of the full orthogonal group would stabilize it. Clifford theory then gives an irreducible full-O character restricting to a positive multiple of the given character. Full-O reality forces that character to be real, a contradiction. This does not claim that every character of Omega is real. Consequently all compatible factor-preserving operators are scalar times inner operators, exactly as used by the tensor argument.

## Budget and actual generation

The two-involution convolution maximum is the maximum at the four corners of a rectangle. Its complement is `2 beta(1−beta)>1/4`, so a bad factor-preserving inertia cannot have two active factors. Factor permutations are also excluded from bad operators by the weighted-cycle quarter bound. A remaining bad inertia is a scalar times a negative reflection in exactly one factor; the scalar must be plus or minus one because otherwise it has no fixed vectors. This is a calculation of the actual fixed space, not a scalar-invariant nonreal-spectrum assertion.

I checked all three exact budget inequalities. The inducing degree exceeds 360 from the ordinary degree bound. The actual Shapiro/VHS intermediate-cover factorization forces genus zero, at least twelve genuine inertias and total moving rank `2e+6`. Thirteen inertias contradict the first inequality; twelve with even one good inertia contradict the second. Hence every one of exactly twelve inertias must be bad.

The conclusion does not stop at a necessary numerical profile. Since these genus-zero inertias generate the faithful inducing image, and all preserve every factor, their actions on a fixed normal factor generate all its inner automorphisms. Centerlessness then says that at most twelve actual negative reflections generate the natural Omega group. Their reflecting vectors have a nonzero common perpendicular because the natural dimension exceeds twelve. Every generator restricts to minus the identity there. This defines a nontrivial character of the group they generate into a group of order two. It contradicts the proved perfectness of Omega. The subspace may be degenerate; the scalar-action argument needs only that it is nonzero.

This proves the stated mixed-factor theorem without transitivity or an imaginary-field equality assumption. In the final transitive main-source consequence, selfduality is constant across the factor orbit. The earlier selfdual result, this q=3 result, and the separately reviewed odd-q≥5 result therefore give the claimed odd natural dimension bound. The earlier failed q=3 quarter estimate remains honestly recorded as a limitation of that estimate; it is not erased or reinterpreted as a source.

## Independent exact supplement

`audit_orthogonal_three_odd.py` and `audit_orthogonal_three_odd.json` were written after reading the whole author program, without importing its code, selected data, or output. My reconstruction checks the rational bounds and convolution corners; 252 exact diagonal norm distributions by convolution; an order-eight root of a negative reflection in natural dimension seventeen; and twelve independent norm-one reflecting vectors in dimension fifteen with a common three-dimensional perpendicular. The higher-order witness uses four identical hyperbolic blocks, so its spinor norm is a fourth power and equals one; this inference is explicitly distinguished from a new spinor-table enumeration.

Actual successful run: **2026-11-21 22:25:19.440206 UTC**, **0.007994914 seconds**. No failed run preceded it. Its exact degree ceilings are `180000/4961<42` and `18432000000000/52557706663<360`. The finite natural matrices supplement the universal order and generation proofs; they are not a classification of all groups or representations.

## Primary-source checking and inherited inputs

I freshly read Taylor's complete Theorems 11.47 and 11.48 statements and proofs, printed pp.161–162, including the characteristic-three perfectness argument and exact small exceptions. The dimension and isotropy hypotheses here are inside their scope. I also freshly read Li–Xia's entire Section2.2.2 introduction and Table2.1 on numbered author p.14, specifically the odd-dimensional Omega row and its field parameter.

I reread LST2011 Theorem4.3.6/(4.3.2) on pp.1917–1918, its final parameter choice on pp.1922–1923, and the complete restricted-support Remark4.3.7 on p.1923. The full intervening proof had already been read in this run and was checked again in the immediately preceding OL12 audit. Its domain includes nontrivial nonfaithful characters inflated from the ordinary Omega group and arbitrary element orders. The first exponent is `sqrt(N/7)`, so threshold `N=567` gives exponent nine. There is no hidden faithful-character or prime-order hypothesis.

The complete KTV2023 invoked pp.39–45, including full-O reality Theorem1 p.44 and determinant/spinor quotients, and GLT2024 Theorem3.7/complete proof pp.165–167 were freshly read during the immediately preceding OL12 audit. This event rechecks their exact applications; it does not claim another independent reading of all those pages or a new proof of the classifications. The opposite-radical generation, orbit transitivity, signed conjugation identity, tensor support and actual period factorization are the explicitly reviewed prior proofs. No unavailable GM statement or unverified finite character table is used.

No TeX compilation or broader finite-parameter classification is claimed.

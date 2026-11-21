# Implications — working state

## Geometric complexity theory

The archive lambda operations give exact virtual identities and useful family formulas, but do not by themselves turn a Kronecker multiplicity into an effective finite-set count or imply ordinary saturation. The explicit counterexamples identify the missing hypotheses.

For actual orbit-closure multiplicities, M008/M009 compare all copies using projected padded forms and shape-dependent coefficient boxes. They exclude at most9rows at n>3m^4 and at most51rows at n>=m^25. Known Grenet containment excludes all shapes when n>=2^m−1, so remaining candidates require m>=19 and m>=190 respectively.

The strongest general degree criterion is A023: every actual obstruction requires n<P_d(dm), where P_d(dm)<=min((d−1)^2,floor(d(d+m−1)/2)); shape by shape require n<P_d(lambda2). This refines the verified known Foulkes–Howe argument by grouped differential powers. F014–F018 retain all copies on exact coefficient-support families. F018's finite order-ideal invariant κ gives q<=K when n>=κ(Γ_m,λ), and full K=a or q=K=a under its separate base-degree and permanent-size hypotheses.

M013 proves dominance of the determinant coefficients seen by a highest-weight function, without asserting exact containment of every truncated form. At n>=m^c,c>=6, require lambda2>=c+2. M014 combines this with the mixed support construction to require lambda_(2j)>=c+3−j for1<=j<=c+1. In BIP range this is the full staircase lambda2>=27,lambda4>=26,...,lambda52>=2. The IP range retains its staircase lambda2>=6,lambda4>=5,...,lambda10>=2. M015 separately proves lambda2>=6 already at n>=m4 via an integral cyclic-star jet construction. A025 evaluates the full support criterion to give the additional explicit BIP condition lambda3>=557 OR lambda52>=3.

O020 proves full K=a for lambda3<=2 at n>=length(lambda)−1, with arbitrary second row and outer degree. F021 proves full permanent multiplicity from its own dominant jet map, including an example with at least two actual copies beyond every exact two-tree support cover. O018 supplies a separate example with at least four copies and lambda2>n, excluded by the complete profile even though every individual-cut enlargement is too large. These are necessary restrictions and exact positive families, not examples of q>K.

In the BIP no-occurrence range q>0 already forces K>0. A remaining actual obstruction therefore requires q>=2, not merely a nonzero multiplicity. F010 identifies the unresolved comparison as ranks of the permanent and determinant evaluation tensors. Ordinary rectangular Kronecker coefficients bound K from above and cannot replace it in an arbitrary actual multiplicity comparison. The known d>n/m restriction applies to the sufficient q>g test, not to every q>K candidate.

M012 gives exact q=K=a=4 in the binary tail-six family and q>=4 in explicit higher-row families, so the new gates can be tested on actual multiplicities larger than one.

No general comparison in the IP/BIP padding range, algebraic complexity separation, or Boolean P-versus-NP conclusion is proved.

## Actual obstructions now established

A030 proves q=a=1 and K=sk=g=0 for every unpadded size n=m>=3 at d=n²+1 and lambda=(d(n−2)+3,3,2^(d−3)). The nonzero permanent highest-weight section has nonzero powers. The corresponding stretched rectangular coefficient is [z^s] product(j=2..n)(1−z^j)^−1: zero at s1, positive for all s>=2. This combines a genuine permanent-positive saturation hole with an actual obstruction. It proves sharpness of the c1 second-row endpoint lambda2>=3. The partition length n² prevents this family from supplying an obstruction after internal padding from m<n.

F025 gives K=5<q=a=6<sk=10<g=11 for the unpadded3×3 permanent in degree12 and shape(19,7,2^5). The determinant ideal multiplicity1 and ambient6 are the published LMR Section3.2 p476 input; a separately proved, explicit integer coefficient projection shows all six ambient copies survive on the permanent closure. The exact ordinary and symmetric coefficients are independently specified finite character sums. This is a concrete actual multiplicity obstruction with both sides positive that neither orbit-bound test detects. It demonstrates why closure ideal ranks must be compared. It does not transfer automatically to large padding, and no historical priority is claimed.

M019 now extends coefficient jets by two independent order ideals. O025 proves a strict exclusion beyond every one-sided M018 choice on an actual q>=4 family. Its explicit BIP consequence is lambda4>=27 ORlambda2>=239063403. O024's one-sided count gives lambda2>=159375611 ORlambda3>=29 ORlambda4>=27. These are supplementary necessary gates; they do not assert an obstruction exists in the remaining region.

## Grothendieck's texts

Cote133scan019 must distinguish unsigned subset powers from the opposite-symmetric Burnside operations. The former lose exterior orientation signs; the latter linearize correctly but are not special. Cote133scan006 uses a literal split quadratic group: modern exact or metabolic Grothendieck–Witt theorems cannot be substituted without changing that object. Cote133scan008's unrestricted stable-hyperbolic criterion fails on a characteristic2 classifying topos. Cote133scan009's deleted hyperbolic Stiefel–Whitney assertion is false; the correct formula is already in EKV1993§5.5.

Cote133scan028's monomial Cauchy identity is proved integrally in bounded-rank exactK0 by tensor filtrations and flag splitting; the separate positivity question is refuted. The reported scan029 question has an affirmative answer for exact Zp lattices and local Q-algebras, and a negative answer for arbitrary local rings, including an explicit singular characteristic0 ring. The reported finite-injection functor statements require finite sums of map functors, not a single map functor.

SGA3 gives the representation/comodule and grading dictionary, SGA6 gives the exact lambda and gamma constructions, and FGA supplies parameter spaces without proving multiplicity inequalities. Rational gamma grading loses the representation data in positive degrees. Pure Artin and pure Tate examples show why Frobenius weights cannot be identified with positive degree support or nonnegative traces.

## Remaining gates

The precise open questions, failed routes, full proofs, source qualifications and check events are in QUESTIONS.tsv, APPROACHES.md, GCT_KRON.tex and CHECK_EVENTS.tsv. The run is continuing. The two completed timed reviews both recorded movement; see TIMED_REVIEWS.json. Next review is due2026-11-21T04:00:17Z.

## Checked update 2026-11-21T00:57:54.964720+00:00

The strongest degree reduction is A023: actual candidates require n<P_d(dm)<=min((d-1)^2,floor(d(d+m-1)/2)). M013 changes the geometric comparison from containment of an entire truncated coefficient space to dominance of the coefficients detected by a highest-weight function. Its unit-Jacobian construction gives full ambient determinant multiplicity and raises the BIP second-row requirement to27. Together with F017, all even rows through52 satisfy lambda_(2j)>=28-j. O018 requires lambda3>=139 or lambda52>=3 and supplies a strict four-copy example showing why the complete nested profile matters.

F018 is a general finite support-cover criterion, and preserves the internal padding entry on the permanent side. O016, O017 and O019 delimit their own exact, border-containment and jet-dominance methods; they do not settle the remaining permanent-specific evaluation ranks.

For the original lambda/saturation question, F019/A024 give an actual positive polynomial highest-weight algebra for the full square of a two-row rectangle. It is normal and relatively saturated, yet ordinary saturation fails at exactly the mixed-parity weights because the generated lattice is not primitive. This supplies a concrete algebraic-geometric realization of the distinction needed in the cote133 positivity discussion.

## Checked update 2026-11-21T01:48:26.014925+00:00

M016 and F022 give the second-row condition lambda2>=c+2 at every integral threshold n>=m^c, c>=1; equivalently actual obstructions require n<m^(lambda2-1). M017 further couples that row to later rows. In the BIP range, lambda2<=26+t forces lambda_k>=27 when 1+binom(k-2+t,t)<=478126755. Thus lambda3>=27 or lambda2>=478126780 is necessary, and the minimum second row27 requires at least478126755 rows. These follow from dominant coefficient projections and compare every ambient copy; they do not assert exact representation of each truncated polynomial.

A027 transports a known positive height-three invariant count to rectangles with unbounded heights by explicit Schur duality. It supplies further exact nonvanishing and saturation-failure families, with no claim that their three rectangle widths match a particular GCT candidate.

M018 uses the entire finite coefficient profile in a dominant-jet construction. Its explicit BIP condition is lambda2>=1000001 OR lambda3>=29 OR lambda4>=27. O023 proves this is a strict additional exclusion relative to all M017 prefix tests on an actual q>=4 family. A028 separately gives an unbounded strict loss of symmetric Kronecker copies at the determinant boundary, with closure multiplicity exactly one.

## Checked update 2026-11-21T02:45:13.439105+00:00

A031 proves further actual unpadded obstructions at sizes4,5,6, with q=a>K and K>=7,63,594. Exact deterministic integer minors retain all permanent copies for every shape of length<=2m+2 and thirdrow<=2 at these finite sizes. O027 proves the universal determinant equality for length<=2n and thirdrow<=2; the known LMR ideal copy at length2n+1 makes that uniform threshold sharp. F026 preserves six copies of the earlierper3 shape under internalpadding, but O027 proves those shifts are not obstructions for any n>=4.

M020 states the known BIH determinant-support saturation theorem with its exact hypotheses and derives a finite uniform-stretch reduction. It also proves the all-copy eventual-equality consequence of the known BI boundary-localization theorem. The latter uses full-rectangle translation, which leaves internallypaddedpermanentsupport for m<n. This records an actual extension-of-sections mechanism and its precise limitation, without inferring a comparison of the original positive ranks.

## Exact actual algebras and every stretch — 2026-11-21T03:19:25.943520+00:00

A034 gives a uniform positive algebra result for every unpadded size n>=3. Put R=n²,D=R+1 and lambda_n=(n(n−1)²+1,3,2^(R−2)). The permanent HW ray algebra contains an explicit polynomial algebra with generator degrees1,2,...,n. Its degree-s monomials give q>=p_n(s), where p_n counts partitions into parts1 throughn. The determinant HW ray algebra is exactly a polynomial algebra with generator degrees2,...,n; therefore K=sk=g=h_n(s), the corresponding partition count without ones. The actual gap is at least p_n(s−1)>0 for every s>=1. At every s>=2 both actual multiplicities are positive. A033 strengthens the doubled value to q>=3>K1 for all n, and F028 gives a stronger lower count in the cubic case.

This settles the stretching question without an invariant-degree conductor or an uncomputed invariant. The proof uses concrete centered binary coefficients, the full Hessian, an explicit dominant coefficient map at a fixed Hessian zero, and prime-divisor valuations. Determinant equality follows by multiplying every binary highest-weight copy by the nonzero Hessian coefficient and meeting the ordinary Kronecker upper bound.

The exact determinant ray ring is normal and has a positive monomial basis, but its support is {0,2,3,...} in the generated group Z. Thus the original positivity-to-saturation inference fails inside an actual GCT highest-weight algebra. Normality of this ray algebra is not a claim that the full orbit closure is normal; multidimensional homogeneous pieces invalidate the multiplicity-free argument of A019. The full-length weights have zero internally padded permanent multiplicity whenm<n, so this theorem does not reduce the remaining IP/BIP gate.

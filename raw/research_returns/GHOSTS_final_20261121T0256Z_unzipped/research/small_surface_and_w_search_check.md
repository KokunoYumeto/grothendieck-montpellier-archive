# Independent check of the small-surface reduction and the exact `w` search

Checked on 2026-11-21 by `/root/bounded_specialization`, GPT-6 Astra Pro, with inherited reasoning effort not separately observable. These are mathematical derivations, source-code inspections, and explicitly described computational checks. They are not formal verification.

## Material checked and scope

The complete text of `sections/small_surface_reduction.tex`, statements W01–W03, was read adversarially. The complete source of `work/agents/w_full_abelian_search.py`, `work/agents/w_complete_abelian_compare.py`, and the imported prefix of `work/agents/t0_search.py` was inspected. The latter prefix supplies Eisenstein arithmetic and exterior-algebra operations; it stops before the earlier primitive-class search.

The geometric assertions are for the **complex** product `E^4`, with `End(E)=Z[omega]` and the product principal polarization. This audit does not transport W01–W03 or the exact `w` minimum to supersingular reductions. The all-good-reduction theorem for the different class `t0` is separately proved in V05–V06.

**Verdict:** W01–W03 and the mathematical completeness of the stated finite comparison pass. The exact target and the symmetry reduction pass an additional 70-coordinate calculation. The full approximately 79-million-candidate final comparison was not rerun by this checking agent; the recorded negative output is the prime-arithmetic agent's computation, which the root agent is independently rerunning.

## W01: every binary and ternary case checked

For a binary matrix, the trace bound leaves a zero diagonal, a diagonal one, a diagonal two, or diagonal pair `(3,3)` or `(3,4)`.

* The first two cases are the integral Schur-complement constructions.
* For diagonal two, a nonzero residue in `O_K/(2)=F_4` has a unit representative. The dyads with second coordinates `(bar(x)+r)/2` and `(bar(x)-r)/2` use first diagonal two and second diagonal `(N(x)+N(r))/2`. In the nondivisible case `N(x)` is odd, so positivity makes this at most the prescribed second diagonal.
* The norms through twelve are `0,1,3,4,7,9,12`. Representatives of all norm-at-most-nine elements are sums of at most three units, up to units and conjugation. Norm twelve occurs only for diagonal pair `(3,4)` and is a single dyad with coordinate norms three and four.

For a ternary matrix without diagonal zero or one, the diagonal is `(a,2,2)`, `a=2` or `3`. Each of the four lower off-diagonal norm cases was checked.

* Norm four: normalize the entry to two. Positivity forces equality of the two associated columns, reducing to the binary case.
* Norm three: the lower binary block has determinant one; the vector `(1,-1)` has norm one. Extending it to an integral basis and subtracting the integral orthogonal projection gives the identity form. The resulting two-column dyad construction is integral, and the first-coordinate remainder is nonnegative by positivity.
* Norm one: normalize the entry to one and set `s=omega-omega^2`. If `s` divides `x+y`, the stated two dyads have off-diagonal entries exactly `x,y` and first diagonal `F=(2N(x)+2N(y)-Tr(x bar(y)))/3`. If not, `x+y` is a unit modulo `(3)`. The six Eisenstein units give exactly the six unit residues. Taking `r` in this residue and `t=(x+y-r)/3` gives the three stated dyads, whose first diagonal is `F+1/3`. Since `F` is congruent to `2/3` modulo the integers, the integral Schur inequality gives the needed room.
* Norm zero: the separate binary decompositions work unless both off-diagonal norms are odd and sum to `2a`. The only remaining norm pairs are `(1,3)` for `a=2` and `(3,3)` for `a=3`. Both displayed pairs of dyads were multiplied out. Their last two coordinates are orthogonal and their first-to-last cross terms have exactly the required norms. Independent unit changes realize every possible phase because all norm-three elements are associates.

Thus the hand proof is exhaustive and does not depend on the auxiliary matrix enumeration.

The divisor-class interpretation is integral: the Rosati-symmetric endomorphism matrix identifies `NS(E^n)` with integral Hermitian matrices, and dyads are pullbacks of a point under an Eisenstein homomorphism (with conjugation of the coefficient vector if using the opposite matrix convention). For curves, diagonal projection degrees and integral elliptic correspondences determine the full homology class; analytically this is the positive Hermitian matrix obtained by integrating the pulled-back holomorphic one-forms. A nonprimitive vector gives the actual effective pushforward, including its mapping degree. There is no division of cycle coefficients. The trace and twice-trace degree normalizations are correct.

## W02: arbitrary surfaces, including the two delicate cases

If a coordinate-pair projection has degree one, the rational inverse and extension theorem give a translated abelian graph. Otherwise every positive coordinate-pair degree is at least two.

For degree at most fourteen, a constant coordinate makes the surface an effective divisor on a translate of `E^3`, with Hermitian trace at most seven. With all four coordinates nonconstant, algebraic dependence of their function subfields is an equivalence relation. At most three independent pairs are possible, forcing the partition `(1,3)`. The surface equals `E` times the curve in the remaining coordinates because both sides are closed irreducible surfaces with the same embedding. Its curve degree is at most seven. W01 therefore applies in both cases.

For a nonzero-Weil surface of degree at most twenty-two, all coordinates are nonconstant, and the only possible dependence partitions are `(1,3)`, `(2,2)`, and `(2,1,1)`.

* `(1,3)` has zero Weil projection, because three degree-one differential factors come from one curve.
* `(2,2)` is a product of two curves, each of degree at least two and at most five. The binary part of W01 replaces both factors effectively and integrally.
* In `(2,1,1)`, the dependent pair must mix the two fixed `E^2` factors. The four crossing-pair degrees are `n_i b_j`. They are all at least two and have sum at most nine. A rank-one two-by-two array cannot consist of three twos and one three. Hence all four are two, giving exactly `(n,b)=(1,2)` or `(2,1)`, while the remaining pair degree is two or three.

In the `(1,2)` case the dependent curve is a translated unit graph, and the surface is a divisor on the corresponding `E^3` with diagonal `(d,2,2)`, `d=2` or `3`. This is a trace-at-most-seven instance of W01; it does not assume a degree-one projection of the surface to a pair of coordinates.

In the `(2,1)` case the geometric generic fiber has total degree one to each elliptic coordinate. Its conjugate components have identical degree vectors, so there is exactly one reduced component, a translated graph of a unit. That unit is constant because `End(E)` is constant. Quotienting by its fixed graph direction is a split quotient. The image curve `C'` maps generically with degree one to the original dependent-pair curve: otherwise the geometric generic fiber would contain multiple graphs. The equality `V=q^{-1}(C')` follows over the generic point and then by closure. The moment matrix of `C'` has diagonal `(2,2,d)` and trace at most seven. Pulling back its dyad decomposition gives the required integral effective replacement.

All replacements preserve the full homological class, so they preserve the degree for the original ambient polarization, even where the auxiliary `E^3` has been identified by a nonisometric splitting.

## W03: the graph catalog and its exceptional zero-Weil surfaces

A complex subtorus of `E^4` is stable under scalar multiplication by `omega`: its complex tangent space and its intersection with `O_K^4` are stable. The intersection lattice is a saturated rank-two `O_K` submodule, hence free and a direct summand because `O_K` is a PID. The coordinate-pair degrees are the norms of its six Plücker minors.

A nonzero Weil projection forces both projections to the fixed two `E^2` factors to be dominant. A positive Eisenstein norm cannot be two. If both degrees were at least three, the mixed-intersection inequality would force surface degree at least twenty-four. Hence one projection is degree one. The graph formula and `T>=2 sqrt(d)` leave exactly `d=1,3,4`, with `T+d<=10`. The transposed graphs are essential for `d=3,4`; degree-one transposed graphs already occur as graphs of the integral inverse.

For a degree-at-most-fourteen abelian surface with no unit Plücker minor, there can be at most two nonzero minors. A single nonzero nonunit minor is not primitive. Two norm-three minors have a common factor over three. Thus the only possibility is two minors of norms three and four, sharing a coordinate by the Plücker relation. Their coprimality gives exactly

`E_free × image(x ↦ (s x,2u x)) × {0}`, with `N(s)=3` and `u` a unit.

This checks the previously missing degree-fourteen example and proves that the additional catalog family is exhaustive. Its zero-Weil property follows from its constant fourth coordinate.

## Completeness of the exact comparison

For `w=e_W[Gamma_1]`, the exact integral lattice gives denominator three. For a certificate with maximum cost below twenty-four, the calibration implies `D>=4N`; hence its positive multiplier is exactly `N=3`. The earlier degree-at-most-fourteen period bound excludes all `D<=14`, so the only remaining even degrees are sixteen, eighteen, twenty, and twenty-two.

Each numerator has nonzero Weil projection because an individual degree-at-most-twenty-two effective cycle has period modulus at most `22/8<3`. A nonzero-Weil component costs at least eight. Consequently every zero-Weil component in a numerator has degree at most fourteen, and every nonzero-Weil component has degree at most twenty-two. W02 replaces every component by effective abelian surface classes without changing degree or full class. W03 then supplies a complete finite abelian catalog.

A numerator has at most two nonzero-Weil abelian components, counted with multiplicity. If there are two, both have degree at most fourteen and determinant norm one. If there is one, its determinant norm is one, three, or four. Thus the possible total period has norm in `{0,1,3,4}`. Solving `a-b=3` with both periods in this set leaves exactly

`a in {1,2,1-omega,2+omega}`.

The holomorphic automorphism that inverts the first elliptic coordinate preserves the polarization and acts by minus one on the Weil plane. Applying it and exchanging the two numerators preserves the target `3w` and replaces `a` by `3-a`. It therefore carries the omitted case `a=1` to `a=2`. The code's three `plusz` values and the corresponding `minusz` values are exhaustive. No appeal to an antiholomorphic operation is needed.

The target satisfies `theta^2 · (3w)=0`, so any exact certificate has equal numerator degrees. Testing the four exact degrees, rather than separately testing all unequal pairs of degree bounds, is therefore complete.

### Code catalog and equality checks

* The zero-Weil coordinate-graph catalog uses all six coordinate-pair inputs. Its budget is `T+N(det h)<=6`; individual entry norms are at most six, whose possible values are only `0,1,3,4`. The enumerated range `[-2,2]^2` with norm at most five therefore includes every possible entry.
* The zero-Weil exceptional family uses the connected kernel of `b x_j-a x_k`, with coprime coefficient norms three and four. Wedge with the fixed-coordinate point class gives precisely the exceptional product surface. Both assignments of the norm-three and norm-four coefficients are included.
* The nonzero-Weil graph budget is `T+N(det h)<=10`, so all entry norms are at most nine. The range `[-3,3]^2` contains every Eisenstein integer of norm at most nine. Both graph orientations are included when determinant norm exceeds one.
* Deduplicating by all seventy class coefficients is harmless: degree, Weil period, and the coordinate-pair projection degrees are determined by the class.
* The dynamic program uses exact degree and arbitrary nonnegative multiplicities through combinations with repetition. Its degree-fourteen limit is exactly the maximum remaining zero-Weil degree.
* The remaining two-unit cases are generated by combinations with repetition, so repeated main components are included.
* The base-1001 encoding is additive. For any tested equality, every coefficient of its difference is bounded in absolute value by `2*11*M+max(abs(q))`, where `M` bounds individual catalog coefficients. The code checks the numerical bound `156<1000<1001`. If an encoded difference vanishes, reduction modulo 1001, followed by induction on the coordinates, forces every coefficient to vanish. Negative coefficients do not invalidate this argument. The encoding therefore gives exact equality, rather than a hash or numerical approximation.

## Additional target and symmetry calculation actually performed

Using the exact exterior-algebra operations, I recomputed the cross-divisor forms `P,Q,U,V`, the primitive class `u=PU-QV`, and the target

`q=PU-PV-QU-2QV`.

I then separately applied `R=eta(omega)^*` to all one-forms, including conjugate multiplication on the last two elliptic factors. The computation verified in all seventy exterior coordinates that

`q=u-Ru=3w`.

It also verified that inversion of the first elliptic coordinate sends `q` to `-q`, and that `q wedge theta wedge theta=0`. A finite exact lattice check returned the four possible plus periods listed above and verified that every one is covered by the stated inversion-and-exchange symmetry. These checks completed successfully; their mathematical explanations are given above.

The negative comparison output reports 1,898,952 distinct positive classes and 79,234,032 negative candidates at degree twenty-two. This audit inspected the full code and the recorded output but does not claim a new execution of that full comparison.

## Final W04 portable-certificate check

After the polished statement became available, I read the entire proof in `sections/w_exact_minimum.tex` and all source lines of the self-contained `research/w_exact24_certificate.py`. This version regenerates both catalogs internally and has no binary-cache dependency. Its theorem statement, finite lists, symmetry, recurrence, encoding, and comparison loops agree with the already checked reduction.

I independently executed the portable function `check_target_and_upper_bound()`. It verified the projector identity `18q=(9+S)(2-R-R^2)[Gamma_1]`, `q^2=18`, degree zero, and the displayed six-surface degree-twenty-four representative in all seventy coordinates. The full negative comparison was not repeated by this agent. The root agent separately reported an isolated complete rerun with identical counts and no equality through degree twenty-two; that is a separate check event, not my execution.

The conclusion is exactly `c_{C,theta}(w)=24`, followed by eventual equality with 24 at good reductions using B03. No exact value at every exceptional supersingular prime is asserted for this normalization.

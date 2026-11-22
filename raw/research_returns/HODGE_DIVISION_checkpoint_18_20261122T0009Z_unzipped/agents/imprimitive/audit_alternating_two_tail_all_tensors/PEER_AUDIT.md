# Whole-proof review of D-ATT07–09

Reviewer: `/root/imprimitive`, GPT-6 Astra Pro, inherited reasoning effort not exposed; project HODGE_DIVISION, 2026-11-21.

**PASS in the stated transitive ordinary-core, non-Eisenstein scope.** I read the entire 333-line frozen proof, every line of the author's exact checker, and the complete retained output. No mathematical repair was requested. The reviewed proof is `agents/g34_eightfolds/bireflection/alternating_two_tail_all_tensors_section.tex`, SHA-256 `2e9afd9be79f01ee143291b73619837be11182569bccc0234bfb66d45c73372b`.

This audit shares earlier reviewed scalar/normalizer inputs with my separate standard-tensor addendum. I also use and explicitly credit the author's weighted-cycle lemma there. I do not describe the entire argument as an independent discovery. The present report is an independent complete reading of the written ATT07–09 argument, together with separately implemented matrix/characteristic-polynomial checks that import no author arithmetic or selected spectra.

## Normalizer and actual field interface

The two rational modules restrict irreducibly and faithfully to `A_n` in the stated `n>=15` range by the complete previously reviewed UP/EX and ATT01–04 arguments. The compatible automorphisms are implemented by the ordinary `S_n` action. A scalar in the rational tensor-wreath image must centralize each individual normal simple factor, hence fix the factors and induce the identity automorphism on each. The centralizer of `A_n` in `S_n` is trivial. This verifies both the unique scalar decomposition and the actual homomorphism to the permutation wreath group; it is not a projective choice made separately at the branches.

The character field of the inducing representation is contained in the cyclotomic field of its scalar character. The original quadratic field is assumed only to be a subfield of that actual character field. If the scalar character took values in `mu_6`, the original imaginary quadratic field would be Eisenstein. For every other field the nontrivial scalar quotient has at least two nonidentity tuple entries, by generation and product one. No conductor equality, descent of the inducing module to the original field, or identification of the two fields is needed.

The all-power trace estimate is applied to the rational operator before the scalar is introduced. A tensor-wreath trace is a product of cycle-product traces. If negative, one of them has magnitude at most `b0` on its negative side, and all remaining factors have absolute value at most `a`. Since the number of cycles is at most the number of tensor factors, this gives `tr(T^j)>=-(b0/a)e` for every power. Rational Galois conjugacy gives the quarter multiplicity bound outside orders 1, 2, 3, 4 and 6. For order four the equal multiplicities at `i,-i` and the trace of `T^2` give exactly `(1+b0/a)e/4`. This is the claimed bound on the actual fixed space at a scalar mark; no unsupported preservation of a nonreal spectral bound under scalar convolution is used.

## D-ATT07: exactly two full tensor cycles

I rechecked the actual intermediate-cover reduction. Multiplicity six gives `6=2e(h-1)+D`. The degrees here exclude `h>=2`; genus one has six moving-rank units and at most six genuine marks, so its finite-cover variation has period rank below nine. The proposed rank-nine case must have a sphere base, a genuine generating product-one tuple, at least twelve marks, and `D=2e+6`. The proof uses these as necessary conditions from an actual family, never as sufficient conditions for dominance.

Every genuine branch has support at least `(d0/a)e`: an active within-factor permutation gives this by convolution; a genuine scalar has full support. At a moving factor cycle, diagonalizing its product gives a cyclic monomial action on basis words. There are `a` constant words, and every other orbit has length at least two. Each orbit contributes at most one vector to any eigenspace. Thus the support is at least `(a-1)e/(2a)`, even for an arbitrary twist and repeated eigenvalues. The inequality `2d0<=a-1` is valid for both displayed modules throughout the range.

If at least three branches move factors, the two scalar marks and a third distinct moving branch, together with nine other genuine marks, exceed the source budget. I independently simplified the excess to

`a^(t-1) * (9d0-(b0+1)/2)`.

It is strictly greater than six since `b0<=d0`, `d0>=12`, `a>=90`. Transitivity excludes zero moving entries, and product one excludes exactly one. Therefore there are exactly two, and their factor permutations are inverse. They generate the whole transitive factor-permutation image, so the common cycle is a full `t`-cycle. This last transitivity step is essential and is present in the proof. The subsequent weighted-cycle estimate does not require any restriction on their scalar orders or their cycle products.

## D-ATT08: exact weighted-cycle bound

The explicit successive change of basis reduces the weighted cycle to one final twist whose product is `X`. Its `t`th power is `X` on every tensor factor. In an eigenbasis of `X`, fixing the first `t-1` letters gives at most `a-nu(X)` choices for the last letter satisfying the required return product. Thus the full word count `N_z` is at most `a^(t-1)(a-nu(X))`.

I checked the short-orbit accounting exactly. On a rotation orbit of length `d`, a nonzero weighted cyclic matrix has `d` distinct eigenvalues. If it contributes to the target eigenspace, all `d` corresponding words enter `N_z`; its contribution to `t*m_z-N_z` is `t-d`. An orbit not contributing has nonpositive contribution. The total possible error is therefore

`R_t(a)=sum_{d|t,d<t}(t-d)C_d(a)`.

Counting the nonidentity rotations fixing each word gives the exact alternative expression

`R_t(a)=sum_{j=1}^{t-1}a^gcd(t,j)`.

The factor `t-d` is retained throughout. Counting only short words or only short orbits would not suffice. Repeated eigenvalues never merge the basis-word orbits, so the argument remains valid for identity cycle product and all degeneracies. The lemma applies to every target scalar, including a nontrivial root whose order divides `t` even when `X=I`.

The universal bound `R_t(a)<=2a^(t-2)` also passes. The cases `t=3,4` are explicit. For `t>=5` the author's geometric-series upper bound is valid; the displayed two-parity induction starts correctly at five and six for `a>=4`, and its exponent after substitution is exactly `t-2`. This is a proof for all tensor counts, not extrapolation from a finite word enumeration.

## D-ATT09: full constant term and actual quotient

At a factor-fixing branch with `b>0` active factors, summing the individual index bounds and taking a maximum gives `max nu >= A I/b+B`. Since `b<=t`, this is at least `A I/t+B`. The **full** `B=n/4` term is retained; no averaging over zero factors erases it. Convolution gives the claimed factor `a^(t-1)`. If every within-factor permutation is the identity, the genuine scalar has full degree and still satisfies the same bound because `B<a`.

For each of the two full cycles, the weaker `nu(Wh)>=A ind(h)` holds whether `h` is identity or not. The proof never demands a positive `B` term from an identity cycle product. Applying the exact weighted-cycle lemma is therefore legitimate for both actual cycle branches.

The scalar-forgetting homomorphism gives a genuine transitive action on `nt` letters. The core is transitive within blocks; the factor cycle is transitive between them. Taking an actual point stabilizer in the connected cover gives a connected quotient cover of degree `nt`. Its full-cycle index is `n(t-1)+ind(h)`, and its factor-fixing index is the sum of the within-factor indices. Riemann–Hurwitz then gives the required residual total index at least `2n-2`. Scalar marks remain in the coefficient-cover rank sum despite contributing zero to this permutation index.

I independently recomputed the final two constants:

`A(2n-2)-2a = -3n+5` for `(n-2,2)`, and `-3n+3` for `Lambda^2 Std`.

The proof therefore gives exactly

`D-2e >= a^(t-1)/t * ((5t/2-3)n+kappa-4/a)`, with `kappa=5` or `3`.

For `t>=3`, this exceeds `3n*a^(t-1)/2`, hence exceeds six. All signs, coefficients and strict inequalities match the written proof. The result excludes all larger tensor counts in the stated actual-source problem and leaves the stated other labels, spin and nontransitive configurations undecided.

## Independent exact supplement and source reading

My `independent_check.py` uses a different finite implementation from the author's orbit-spectrum program. It constructs actual integer weighted tensor-cycle matrices, computes their characteristic polynomials, factors them over the rationals and reads the exact complex-root multiplicities from the separable irreducible factor exponents. It also computes traces of the actual unweighted rotation powers and separately reconstructs primitive necklace counts by integer recursion.

Its first run passed at **2026-11-21 22:57:37.825636 UTC**, elapsed **0.906830721 seconds**. It checks 15 actual weighted matrices of total dimension 588, 45 rotation trace powers, 1,475 primitive-necklace recurrences and 3,696 independent source cases, together with universal shifted-polynomial identities for both labels. No author code or retained output is imported. There was no failed assertion or repair in this independent supplement. The larger author's 32-case word scan and 4,816 source cases were read in full and remain attributed to the author; I did not execute its program in its owned directory.

I also freshly reopened the primary Milne *Class Field Theory* v4.03 PDF at <https://www.jmilne.org/math/CourseNotes/CFT.pdf> and read the complete Chapter V Example 3.2 on printed p.157. The scalar-field discussion was already fully checked in HD-AST04–05; this theorem uses only the elementary non-Eisenstein `mu_6` consequence, not the stronger conductor thresholds. Fresh web reads are `turn867458759view0`, `turn649424856view0`, `turn501962958view0`. The complete prior UP/EX and ATT01–06 proofs had been read in the preceding two recorded audits and their exact interfaces were checked again here. No whole new upstream classification proof, new geometric existence theorem, TeX compilation or cycle-supplier construction is claimed.

The final whole-proof result is PASS without mathematical repair. The overlap with my standard-tensor work and the separate origin of the weighted-cycle lemma are explicitly retained above.

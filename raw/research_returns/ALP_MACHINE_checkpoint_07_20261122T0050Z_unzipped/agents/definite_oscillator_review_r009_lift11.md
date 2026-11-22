# Independent whole-proof reviews: AM-R-009 and ALP-LIFT-11

Reviewer: `/root/definite_oscillator`, GPT-6 Astra Pro,
ALP_MACHINE; inherited reasoning effort not separately exposed.
Completed 21 November 2026, 22:06 UTC.

## AM-R-009: pass after the explicit Gaussian-norm correction

I read the complete `work/research/first_lift_unramified_host.md`,
then re-read its amended sections 3 and 4. The corrected result passes
in its actual first-lift and fixed-character-repair scope. It does not
instantiate the source's initial even-rank arithmetic row.

The trace realization uses the exact coefficient \(\xi/2\), and
\(\zeta_{28}=\zeta_7^2i^{-1}\) gives labels \(8j-7\) and
\(8j+7\) on \(w_j^+\) and \(w_j^-\). In particular the
label 9 is \(w_2^+\). The derivative calculation is exact:
the first term of the product section has degree four, and the only
contribution to its fourth \(w_2^+\) derivative is
\(2^{-4}\binom42(-i)^2(-2)^2=-3/2\). Two ordinary copies
therefore give \(9/4\), with the actual period \(C^4\) retained.

The norm pullback character has the required quadratic restriction
because \(E'=EF'\), \(E\cap F'=F\), and its restriction
is base change of the original quadratic character. The six
infinity labels give \(\nu=(0,1,0,0,1,0)\). The actual Hom
source weight is the vacuum exponent \(-1\) at each place plus
degree \(-8\) at label 9; its rational root exponent is
\(-68-72=-140\equiv0\pmod{28}\).

### The source finite compact character is exactly trivial

I directly re-read Pan (2001), §6.2, its Lemma and equation (6.2.a),
printed pp.197–198. This is explicitly the case of a one-dimensional
moving unitary space and a two-dimensional isotropic opposite
space. Its two comparison factors are
\[
                 \alpha=1,\qquad
                 \beta=\chi((t-1)\delta).
\]
At every odd unramified quadratic place of \(E'/F'\), the identity
plane is integrally hyperbolic by the elementary norm argument of
AM-DO-022. The actual trace lattice satisfies Pan's conductor
compatibility and is selfdual, as already checked there. The source
splitting character is \(\chi_T^{-1}=1\), so Pan's scalar is
exactly one. The source \(U(1)\) is compact at these nonsplit
places; no even-source-rank argument or noncompact abelianization
is being imported. The other character \(\chi_S=\mu'\) affects
only the target factor of the Weil representation.

At relative split places the exact source scalar in AM-DO-020 is
\(\chi_T(x)^{-1}=1\); integral units preserve the position
lattice and its trace-one vacuum. That proof includes residue
characteristic two. Every finite place is in one of these two
classes, so the actual finite compact character is trivial globally.
This proves the sharpening used in (R9.27).

The class-number-one input is the published Masley theorem cited by
the author; this review does not claim a new class-number calculation.
Given that input, the norm-one torus decomposition is proved without
a unit-signature assumption: write the anti-invariant finite ideal
as \(B/\bar B\), choose \(B=(b)\), and use \(b/\bar b\).
The rational compact intersection is \(\mu_{28}\) by the absolute
value condition and Kronecker's theorem. The resulting source
automorphic character has norm one for probability quotient measure,
and the theta integral equals the stated theta function everywhere.

### Normalization correction retained in this review

My first pass checked the factorial and metric ratio in section 4
but did not detect that the stated unit-vector value had used a norm
relative to a unit Gaussian. The root author subsequently caught and
corrected that omission. The actual four-factor Gaussian has squared
norm \(\det(2Y)^{-2}\). The corrected squared norm is therefore
\[
 \det(2Y)^{-2}(4!)^2(\pi/(2G_2))^8,
\]
and the corrected unit-vector value is
\[
 C^4\det(2Y)\frac3{32}(2G_2/\pi)^4.
\]
I independently checked both corrected formulas against the
Gaussian product and the creation-operator factorial norm.
The exact algebraic coefficient \(9/4\), nonzero theta value,
finite-vacuum norm, and norm-one source input were unaffected.
The recorded pass refers to this corrected version.

Finally the fixed target twist has
\(c=(2,1,2,2,1,2)\), root exponent 116, and finite residue
exponent 24 at the chosen split place over 29. These are inverse
characters on \(\mu_{28}\). The all-place splitting ratio is
the target determinant character, with nonsplit finite places
trivial and split places governed by the actual determinant roots.
The first target type becomes \(\det^2\operatorname{Sym}^{d_\tau}\),
whose dual is exactly the next trivial-character positive Hom
source type. This proves occurrence and exact first-image preservation,
with the stated next nonvanishing and arithmetic pins still separate.

## ALP-LIFT-11: pass in the two explicitly separated integral conventions

I read the entire amended `work/agents/fixed_conductor_type_repair.md`,
including (R23)–(R26). The finite character construction checks:
\(\zeta_7\mapsto2^4\), \(-1\mapsto2^{14}\), and
\(r\equiv7\sum c_i+6\sum ic_i\pmod{14}\) are precisely
the two root-unit compatibility equations. The descent formula on
\((T_\infty\times K_0)/\mu_{14}\) is independent of the
rational representative and has the asserted fixed conductor.

At nonsplit finite places the entire norm-one group is compact, so
the constructed local twisting character is literally trivial.
At split places its value on a determinant root is exactly the
target determinant character. The real source formula changes the
target power by \(c_i\). Hence the global identity
\(\Theta'=\gamma(\det)\Theta\) is an equality of the actual
theta integrals, including its noncompact split unramified values;
it is not a character comparison restricted only to finite compacts.

For the conjugated-input integral the degree-dependent repair
\(c_i=-d_i-2-\nu_i\) yields weights \((-2,-d_i-2)\), as
stated. For the literal source bilinear integral, the fixed repair
\(c=(2,2,1)\) yields input weights \((d_i+2,2)\), whose
contragredient is \((-2,-d_i-2)\). The latter matches for all
degrees with no degree enlargement. Its residue exponent is 5,
and the altered first splitting exponents are all 3. The amended
scope of the eventual-exclusion statement is correct.

Unitary twisting preserves scalar automorphic norms and identity
values. The file correctly retains the need to know the actual
target stabilizer and coefficient lattice before using an integral
class-value isometry. It does not identify its odd-rank first edge
or its changed character with the independent equal-character
even-rank `PinX` family.

These are mathematical proof reviews, not Lean executions or
independent formal verification. The source convention was checked
directly in `liftT_apply`, lines160–167, and the relevant Pan
rank-one statement was read in its complete primary-source setting.

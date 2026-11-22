# AM-R-014: genuine Witt-lower cuspidality and real-type stability in the source predicates

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC.

This note verifies the mathematical contents of the fourth and sixth
analytic predicates in `CayleySignature.AdmS` for genuine unitary theta
integrals. The fourth is an application of the established theta tower
property. The sixth is a property of actual smooth isotypic subspaces.
Neither is asserted as a new tower theorem. The precise application
and the distinction between full smooth and compact-finite vectors
are recorded because the source's quantified interfaces require them.

Together with AM-R-013 this accounts for four of the six analytic
interfaces, subject to the stated genuine geometric interpretation.
The Fourier--Jacobi/free-data assertion and the real discrete-series
up/down assertion are not proved here. No complete arithmetic `D7`
or `ThetaX D` record is claimed.

## 1. The two literal interfaces

`Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean`,
lines177--184, defines `ThetaStablePeriodVanishing` as follows. Given
a stable subspace of cusp forms on the source \(Y_{j+1}\), assume
that all its theta lifts to the specified lower spaces
\(Y_{j,i}^{\mathrm{low}}\), for
\[
 1\le i\le q_j,
 \qquad q_j=\left\lfloor\frac{m-j}{2}\right\rfloor,
 \tag{R14.1}
\]
vanish for every Schwartz input. Its lift to \(Y_j\) must then
be cuspidal. This is a statement about constant terms; it does not
assert that the surviving lift is nonzero.

Lines196--199 define `RealConstantNonvanishing`. Despite its name,
the literal conclusion here is stability of `IsDv` under every
finite adelic action and each actual real unitary group action.
The definition of `IsDv`, lines123--125, is
\[
       \overline F\in\operatorname{typ}(Y_j,D_j).
 \tag{R14.2}
\]
There is no lower bound on a real integral in this particular
declaration. A different integral-nonvanishing assertion must not
be substituted for it.

The abstract record only requires `YsLow_zero` at lower index zero
(`DataTheta.lean`, lines639--640). To apply the tower theorem we
choose the positive lower indices to be the actual Witt-lower
Hermitian spaces, as described next. The auxiliary proof model
`SpanPowerMembership/ThetaFamilyAdmissibleThree.lean`, lines67--70,
uses a zero-dimensional space at every positive lower index; that
auxiliary choice is not used in the present mathematical application.

## 2. Actual spaces and all rational parabolics

Keep the common CM host \(E'/F'\) and even integers \(k,m\),
with odd \(t\), and put
\[
 n_j=k+m-1+jt,\qquad p_j=n_j-q_j.
 \tag{R14.3}
\]
A concrete choice of the required rational Hermitian space is
\[
 Y_j=(E')^{n_j},\qquad
       h_j=I_{p_j}\oplus(-I_{q_j}).
 \tag{R14.4}
\]
Its standard integral lattice is unimodular. At every real place its
signature is exactly \((p_j,q_j)\). Each positive/negative coordinate
pair is a rational hyperbolic plane: if its orthogonal vectors are
\(a,b\), of norms \(1,-1\), then
\((a+b)/2,a-b\) are isotropic and have mutual Hermitian pairing one.
Consequently the rational Witt index is at least \(q_j\). It is
at most \(q_j\) by any real signature. Thus it equals \(q_j\).

For \(0\le i\le q_j\) take
\[
 Y_{j,i}^{\mathrm{low}}
    =I_{p_j-i}\oplus(-I_{q_j-i}),
 \qquad
 Y_j\simeq\mathbb H^i\perp Y_{j,i}^{\mathrm{low}}.
 \tag{R14.5}
\]
These are actual rational spaces in one Witt tower, of dimensions
\(n_j-2i\). An equivalent construction works for an arbitrary
Hermitian \(Y_j\) with the indicated real signature: take its
actual Witt decomposition, whose rational index \(q\) is at most
\(q_j\), and impose the lower-lift hypothesis at least for
\(1\le i\le q\). No rational hyperbolic plane is inferred from
signature alone in that more general case.

Every maximal proper rational parabolic of the concrete \(U(Y_j)\)
is conjugate to the stabilizer of a rational isotropic subspace of
dimension \(i\), for some \(1\le i\le q_j\). Witt's extension
theorem gives this conjugacy for each dimension. Its Levi has the
factors \(\operatorname{Res}_{E'/F'}\mathrm{GL}_i\) and
\(U(Y_{j,i}^{\mathrm{low}})\). Thus the list in (R14.1) contains
all proper maximal constant-term tests, not just a chosen archimedean
subgroup. For \(q_j=0\) there is no such rational parabolic and
cuspidality is automatic.

This choice also admits the required positive embeddings at every
nonterminal stage, because
\[
 p_j-N_j
   =m-1-j-\left\lfloor\frac{m-j}{2}\right\rfloor
   =\left\lceil\frac{m-j}{2}\right\rceil-1\ge0
       \quad(j<m).
 \tag{R14.6}
\]
At the terminal stage \(Y_m=I_{N_m-1}\) embeds as the standard
codimension-one positive subspace of \(X_m=I_{N_m}\).
These statements supply this concrete analytic geometry. They do
not supply every other field, auxiliary-prime, level, lattice and
arithmetic condition in the full source `Spaces` record.

## 3. Character parity is constant along each lower tower

Use the genuine global Weil representation for each pair, with its
compatible splitting characters. More precisely, take the genuine
`Chr` domain to be the group of unitary Hecke characters with integral angular exponents
of \(E'\) whose restriction to \(\mathbb A_{F'}^\times\) belongs
to \(\{1,\epsilon_{E'/F'}\}\), with the chosen odd splitting
character \(\eta_T\) in that group. This restriction is part of
the mathematical character domain. The literal `IsMu` condition
specifies infinity types alone; it would not force trivial finite
base-field restriction in the group of all Hecke characters.
Within the stated domain, its integral infinity types force the
restriction to be one: the alternative quadratic restriction has
the nontrivial sign character at every real place, whereas an
integral exponent of \(z/\bar z\) is trivial on the real units.
In the source notation the characters
on the two members of the descending edge are
\[
 \chi_{j+1}=\operatorname{car}(\mu,j+1,j+1),\qquad
 \chi_j=\operatorname{car}(\mu,j+1,j).
 \tag{R14.7}
\]
Here the even-rank character \(\mu\) restricts trivially to
\(\mathbb A_{F'}^\times\), and the usual odd-rank character
\(\eta_T\) restricts to the quadratic character
\(\epsilon_{E'/F'}\). The source `car` inserts \(\eta_T^{-1}\)
at an even index and makes no insertion at an odd index.
Since \(k+m-1\) and \(t\) are odd,
\[
 n_j\equiv j+1\pmod2,
 \qquad
 \chi_j|_{\mathbb A_{F'}^\times}
          =\epsilon_{E'/F'}^{\,n_j}.
 \tag{R14.8}
\]
Removing \(i\) hyperbolic planes changes the dimension by \(2i\).
The same character is therefore a valid splitting character at
every lower target in (R14.5). We use these compatible restrictions,
with the fixed additive character, in applying the tower formula.
This argument does not identify characters of different parity or
apply an even-rank doubling twist formula to an odd-rank group.

## 4. Application of the unitary constant-term formula

The primary input is Wu's unitary tower formula: Proposition3.1,
equations(3.2)--(3.4), author preprint pp.9--12. In a mixed
Schwartz model, restriction to the smaller unitary Levi identifies
the maximal constant term of a cuspidal theta lift with the lower
theta lift of the restricted Schwartz function. The general Levi
factor adds the explicitly stated character and modulus. Only
vanishing is needed below. The symmetric direction is included
in the proposition.

Let \(F\) be any cusp form in the source subspace of the literal
predicate, and \(\Phi\) any Schwartz input. Fix a maximal parabolic
indexed by \(i\) and a target point \(h\). Right equivariance
replaces \(\Phi\) by \(\omega(h)\Phi\), so it suffices to test
the constant term at the identity in that mixed model. The tower
formula is
\[
 \operatorname{CT}_{Q_i}\Theta_{Y_j}(\Phi,F)\big|_{U(Y_{j,i}^{\mathrm{low}})}
       =\Theta_{Y_{j,i}^{\mathrm{low}}}(r_i\Phi,F),
 \tag{R14.9}
\]
where \(r_i\) is the Schwartz restriction at zero in the extra
isotropic coordinates. The compatible Haar measures give this
displayed normalization; changing them multiplies the two sides by
the corresponding nonzero measure constant and has no effect on
the following implication.

The lower-lift hypothesis quantifies over every Schwartz function,
so the right side of (R14.9) is zero, including after the above
right translation. The constant term therefore vanishes everywhere
on that maximal parabolic. This holds for every \(i\), and hence
for every proper rational parabolic: the constant term along a
smaller parabolic is an iterated constant term through a containing
maximal one. This proves cuspidality of the lift.

Although Wu states the proposition using an irreducible cuspidal
representation, its pointwise identity applies to every cusp form.
In the cited proof, equations(3.21)--(3.22) use only the vanishing
of its proper constant terms; equations(3.23)--(3.25) give the
surviving zero orbit. No projection onto an irreducible constituent
is used here. In particular an arbitrary stable, possibly nonclosed
source subspace in the literal predicate causes no semisimplicity
gap. Absolute convergence for the cuspidal input is part of the
cited formula.

Thus `ThetaStablePeriodVanishing` holds in this genuine
Witt-lower interpretation. Once compatible splitting characters are
fixed, the constant-term argument uses no further `Hyp3` inequalities
and needs no nonzero lower image. Character parity was checked above
using the stated parity conditions. Thus it implies the corresponding
restricted source quantifiers. It supplies no bound for the norm or denominators of
the descended vector.

## 5. Full smooth isotypic spaces and the sixth predicate

Use the usual smooth automorphic space of moderate growth for the
ambient real-group action, with its cusp subspace of rapidly decreasing
smooth cusp forms and its usual Schwartz seminorms. In particular the
cuspidal vectors under discussion are in finite sums of smooth
globalizations of actual cuspidal automorphic embeddings. This is also
the cusp domain used in section4: arbitrary smooth functions satisfying
only a formal zero-constant-term condition are not being substituted
into an absolutely convergent theta integral. The genuine theta maps
and constant-term maps are taken in these standard smooth spaces.
For a parameter collection \(D\), let
\(\operatorname{typ}(V,D)\) be the algebraic sum of the smooth
real isotypic subspaces with the specified real representation
types. If no such representation exists, this space is zero.
At an indefinite real place a discrete-series type here means its
full smooth globalization, rather than only its compact-finite
vectors. Compact-finiteness remains a condition on the test kernels
at the places where the source explicitly asks for it.

Each real-group operator preserves every such isotypic subspace.
Every finite adelic right translation commutes with the real action.
If \(T:V_\sigma^\infty\longrightarrow\mathcal A\) is an
equivariant realization of one of the prescribed real types, then
\(R(g_f)T\) is another such realization (or zero). It follows that
\[
 R(g_f)\operatorname{typ}(V,D)
       \subset\operatorname{typ}(V,D),\qquad
 R(h_\infty)\operatorname{typ}(V,D)
       \subset\operatorname{typ}(V,D).
 \tag{R14.10}
\]
Pointwise complex conjugation commutes with right translation of
functions by a fixed real or finite group element. Consequently
\[
 \overline F\in\operatorname{typ}(V,D)
 \ \Longrightarrow\ 
 \overline{R(g)F}=R(g)\overline F
                    \in\operatorname{typ}(V,D).
 \tag{R14.11}
\]
This is exactly the finite and real stability in
`RealConstantNonvanishing`, for every parameter collection and
every stage. No numerical nonzero constant is inferred from the
name of the declaration.

For a noncompact real group, it would be incorrect to make this
argument with only the compact-finite vectors as an ambient space
carrying every real translation. Such a subspace need not be stable
under that action. The smooth globalization in this interpretation
resolves that actual domain issue. On the definite side of
AM-R-013, the selected real representation is finite-dimensional,
so that issue does not change its algebraic finite-sum identities.

## 6. Framework translation and exact remaining gates

The parabolic and Levi groups are actual reductive group schemes
over the number field. Their character and representation gradings
belong to the SGA3 framework, in particular ExposeI,
Proposition4.7.3 and Corollary4.7.3.1, already inspected in the
geometric dictionary. The passage to a Schur representation class
belongs to the carried SGA6 ExposeVI, Theorem3.3. Those geometric
statements do not prove the automorphic constant-term formula;
Wu's analytic theorem is the separate input used above. The
polarized kernel remains an actual theta-group/biextension object
in SGA7I, ExposeVII, sections2.7 and2.9, pp.169--174, with its
normalizations retained as in AM-DO-026/029.

The two remaining analytic assertions are
`ThetaUnfoldingFreeData` (lines168--175), with its actual
Fourier--Jacobi period and factorizable free-data witness, and
`RealThetaLiftDiscreteSeries` (lines186--194), with its precise
real up/down parameter and all smaller-target vanishing. Completing
these is not equivalent to the still separate arithmetic row ties,
raw-Xi selected nonvanishing, terminal mass or complete cost array.

## References

Wu, C. (2013). Irreducibility of theta lifting for unitary groups.
*Journal of Number Theory, 133*(10), 3296--3318.
Author preprint posted 2014: https://arxiv.org/pdf/1409.0770 .
Proposition3.1 and equations(3.2)--(3.4), printed p.9; proof,
especially equations(3.21)--(3.25), pp.11--12. The primary statement
and these proof passages were directly inspected in this run.

Gan, W. T., Qiu, Y., & Takeda, S. (2014). The regularized
Siegel--Weil formula (the second term identity) and the Rallis inner
product formula. *Inventiones Mathematicae, 198*, 739--831.
https://arxiv.org/pdf/1207.4709 . Section11.2, author preprint
pp.51--52, records the first-occurrence cuspidality consequence
for the full classical-group setting, including unitary groups.
The more explicit unitary formula used here is Wu's Proposition3.1.

The exact source declarations and mathematical uses are listed
above. This verification is not a new proof of the cited tower
property and includes no Lean execution.

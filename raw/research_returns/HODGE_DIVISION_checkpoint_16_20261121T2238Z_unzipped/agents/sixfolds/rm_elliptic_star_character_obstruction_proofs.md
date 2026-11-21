# SF-E832. A positive elliptic star cannot compensate the balanced character

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** independently whole-reviewed by /root and /root/g34_eightfolds;
both mathematical reviews PASS on frozen draft
`0542dce98bcf06689930578a262dd242b43cfbc0a3f2aebaec263222b38d01ad`.
All reviewers: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION,
21 November 2026. The peer supplied a separately authored exact supplement;
its scope is finite algebra, with the universal proofs reviewed in full.
This is a character-level obstruction and does not require the
free terms to be direct summands. Its strongest version uses the actual
necessary determinant condition of E825. Scalar and general adjusted unit
directions are distinguished explicitly. No numerical search or assumed
semiregularity is a premise of the linear-algebra lemmas.

## 1. Hermitian interpretation of the balanced second character

Let the complex tangent space have the orthogonal rank-two RM splitting
V=V_+ direct sum V_-, with positive polarization theta=theta_++theta_-.
Normalize theta to the identity Hermitian form. For any real (1,1) class a,
let A be its Hermitian matrix. The Hermitian operator represented by a²/2
on Lambda2 V is the second compound matrix Lambda2 A. This follows by
expanding a in a unitary eigenbasis: the six coefficients are the pair
products of the four real eigenvalues. The identification is invariant
under unitary changes of basis. In particular theta²/2 corresponds to the
identity, and

\[
 (\theta_+^2+\theta_-^2)/2\quad\longleftrightarrow\quad
 \Pi=\operatorname{pr}_{\Lambda^2V_+}
                +\operatorname{pr}_{\Lambda^2V_-},
 \qquad\operatorname{rank}\Pi=2.
 \tag{E832.1}
\]

All classes here are represented by translation-invariant forms on the
abelian variety. Equality in its exterior-algebra cohomology is equality
of these invariant forms, so this compound-matrix test applies to the
cohomological identities below.

## 2. Scalar-unit lemma, including the zero scalar

No real Hermitian form b can satisfy

\[
 b^2=c\theta^2+d(\theta_+^2+\theta_-^2),
 \qquad c\ge0,\quad d\ne0.
 \tag{E832.2}
\]

If c=0, the compound matrix Lambda2 B would have rank2. If B has rank k,
its compound matrix has rank binomial(k,2), one of0,1,3,6 for k from0
to4. Rank2 is impossible.

If c is positive, let lambda1,...,lambda4 be the real eigenvalues of B.
Four of their six pair products equal c; the other two equal c+d, which
is distinct from c. Mark the four edges on the four labelled vertices
whose pair products equal c. A graph with four edges on four vertices is
connected: a disconnected graph on these vertices has at most three
edges. Thus all eigenvalues are nonzero and have the same sign.

If the graph contains a triangle, its three equations force all three
vertices to have the same eigenvalue, equal to one of plus or minus sqrt c.
Connectedness makes the fourth one equal too. All six products would be c,
a contradiction. If there is no triangle, the four-edge graph is a
four-cycle. Its eigenvalues alternate a,b,a,b, with ab=c positive. The
two missing products are a² and b²; equality to the same c+d forces
abs(a)=abs(b). They have the same sign, so a=b and again all products
are c. This proves(E832.2) in all cases. It is a spectral argument and
does not assume that B preserves the RM planes.

## 3. A stronger semipositive lemma for a general adjusted unit direction

Let u be a real Hermitian form preserving V_+,V_-, and suppose its
restrictions U,V have strictly positive traces. Let b be a semipositive
Hermitian form. For any positive kappa and any nonzero real d, the identity

\[
 b^2-\kappa u^2=d(\theta_+^2+\theta_-^2)
 \tag{E832.3}
\]

is impossible. Unlike section2, u need not be scalar or initially assumed
positive.

By(E832.1), this equation is
Lambda2 B=kappa Lambda2 diag(U,V)+d Pi. Since B is semipositive, Lambda2 B
is semipositive. Its principal block on V_+ tensor V_- is kappa U tensor V.
Both U and V have a positive eigenvalue, by their positive traces. The
semipositivity of their tensor product then implies that every eigenvalue
of each is nonnegative: multiply any putative negative eigenvalue of one
by a positive eigenvalue of the other. Hence U and V are semipositive and
nonzero, and each has rank1 or2.

Suppose at least one has rank1. The corresponding pure Lambda2 block on
the right side is exactly d. Semipositivity and d nonzero force d>0.
The other pure block is kappa times a nonnegative determinant plus d,
so it is positive as well. Thus both lines Lambda2 V_+ and Lambda2 V_-
are contained in the image of Lambda2 B. But that image is Lambda2 im B.
A nonzero decomposable two-vector belonging to Lambda2 im B has its whole
support plane in im B. Consequently im B contains both V_+ and V_-, and
B has rank4. Its compound matrix would have rank6. In contrast, the
right side has rank rank(U)rank(V)+2, equal to3 or4 in this case.
This is a contradiction.

Both U,V must therefore be positive definite. The mixed block has rank4,
so rank(Lambda2 B) is at least4. The possible compound ranks listed in
section2 force rank B=4; semipositivity makes B positive definite. Both
pure lines are preserved nontrivially by Lambda2 B. An invertible linear
map whose compound preserves the line Lambda2 V_+ must preserve the
support plane V_+ itself; similarly for V_-. Hence B is block diagonal,
with positive definite blocks C,D.

On the mixed block the equation gives

\[
 C\otimes D=\kappa U\otimes V.
 \tag{E832.4}
\]

Equality of nonzero simple tensors implies C=tU and D=(kappa/t)V for
some t>0. For an explicit proof, apply a linear functional nonzero on U
to the first factors: its value on C must be nonzero, and D is a scalar
multiple of V. Substitution gives the matching scalar multiple for C;
positive definiteness forces that scalar to be positive. On the two pure
lines the equation now reads

\[
 (t^2-\kappa)\det U=d,
 \qquad(\kappa^2/t^2-\kappa)\det V=d.
 \tag{E832.5}
\]

For t² different from kappa, these two left sides have opposite signs.
If t² equals kappa, both are zero. Neither possibility equals the same
nonzero d. This proves the semipositive lemma.

## 4. First two Chern terms of a star

The actual unit sheaf F has the previously proved resolution character

\[
 \operatorname{ch}(F)=2e^{-D}-2e^{-3D}+e^{-4D}.
 \tag{E832.6}
\]

Its rank is1, its first Chern character is zero, and its second Chern
character is zero: the coefficients are respectively2-2+1,
-2+6-4, and1-9+8. Consequently a multiplicity-r unit term F tensor a line
with adjusted real first Chern class u contributes r exp(u) through
cohomological degree4, even after a chosen rational algebraic B shift.

Suppose the remaining free line terms have positive multiplicities n_j,
with total m>0, and their adjusted classes are alpha+eta_j, where
eta_j²=0. Set R=r+m, with r>0, and H=sum_j n_j eta_j. Their full character
is

\[
 \sum_jn_je^{\alpha+\eta_j}=e^\alpha(m+H).
 \tag{E832.7}
\]

This identity uses eta_j²=0 exactly; it is not a truncation. It is valid
for any sheaf or complex with this K0 identity, regardless of whether the
terms occur as actual summands or through nonsplit extensions.

If its full normalized character were R v_q with q nonzero, its first two
nonconstant characters would be

\[
 ru+m\alpha+H=0,\qquad
 \operatorname{ch}_2=-\frac{Rq}{2}(\theta_+^2+\theta_-^2).
 \tag{E832.8}
\]

Expanding(E832.6)--(E832.8), eliminating H and completing the square gives

\[
 b=\alpha+\frac r m u,\qquad
 b^2-\kappa u^2=d(\theta_+^2+\theta_-^2),
 \quad\kappa=\frac{rR}{m^2}>0,\quad d=\frac{Rq}{m}\ne0.
 \tag{E832.9}
\]

For clarity, before division by m the equation is
m alpha²+2r alpha u-r u²=Rq(theta_+²+theta_-²); thus no denominator or
sign is suppressed in completing the square.

If u=lambda theta is scalar, section2 applies with c=kappa lambda²,
including lambda=0. Thus **no square-zero star with scalar adjusted unit
direction can have the balanced character**, even allowing both signs for
the eta_j. This part requires no positivity of the individual differences
and no use of semiregularity or E825.

## 5. Positive elliptic stars with arbitrary rational B field

Now require eta_j=-P_j, where each P_j is semipositive of rank at most1.
Zero is allowed, representing a free line at the center alpha. Equation
(E832.8) gives

\[
 b=\alpha+\frac r m u=\frac1m\sum_j n_jP_j\ \ge0.
 \tag{E832.10}
\]

This is the additional positivity absent from an arbitrary square-zero
star. If u preserves the RM planes and has positive trace on both, the
semipositive lemma of section3 contradicts(E832.9). Therefore no such
positive star can have the balanced first two Chern terms under that
adjusted-unit condition.

Here is its exact application to the remaining unit/free architecture.
Take an actual exact sequence with
\(A=(F\otimes L)^{\oplus r}\oplus L_\alpha^{\oplus n_0}\)
and \(B=\bigoplus_j M_j^{\oplus n_j}\), where n0 is nonnegative,
m=n0+sum_j n_j is positive, and c1(M_j)=alpha-P_j. In the opposite-slope
application A is the positive factor and the M_j are negative free lines.
Require every nonzero difference P_j to have rank1 and positive
theta-degree. Rank1 plus positive
degree means P_j is semipositive: it has one positive eigenvalue and the
rest zero. Include the positive free terms with P_j=0. No condition on the
ranks of the actual extension matrices is needed for this argument.

Because B is locally free, the exact sequence splits locally. Its local
form is F^r plus a free module. Relative to these local splittings, the
FF diagonal transitions are exactly those of F tensor L; the additional
extension entries go from the free B part into A. After the fixed F
comparisons, the FF transition is the scalar line transition of L to
multiplicity r. E825's actual ring map ell ignores the free diagonal and
all off-diagonal free-to-unit or free-to-free entries, including their
products through a free module. Thus its exact multiplicative transition
cocycle is that of L^r on S2. Thus
c1(det Qtilde)=r c1(L). Under any chosen rational algebraic B field, put
u=c1(L)+B and replace alpha by alpha+B; the differences P_j are unchanged.
If a coherent effective finite-action weakly semiregular balanced lift
existed, the necessary determinant condition proved in E825 would give

\[
 u-\frac72D\quad\hbox{has no mixed RM block and is primitive
 on each of the two RM planes.}
 \tag{E832.11}
\]

Here D=k theta, k>0. Therefore u is block diagonal and both block traces
are7k>0. All hypotheses of section3 now hold, while(E832.10) makes b
semipositive. The contradiction excludes **every actual positive elliptic
star in this precise unit/free architecture, for every rational B field
and every specified coherent effective finite action** in E825's scope.
It is stronger than failure of a chosen extension or a dimension count:
its normalized first two Chern terms and the proved necessary determinant
condition already conflict.

This is still a star theorem. More than one center, a negative or
indefinite square-zero difference, a different unit Chern character, or an
object without the stated defect determinant is not covered by this
application. The scalar-unit conclusion of section4 has its separate,
explicitly broader sign allowance. Neither statement classifies arbitrary
unstable sheaves or perfect complexes.

## 6. Why the two positivity hypotheses must be kept

A spectral proof cannot silently drop both scalarity and semipositivity.
For example, in the orthogonal plane decomposition let

\[
 U_0=\operatorname{diag}(1,1,2,-2),\qquad
 B_0=\operatorname{diag}(2,2,1,-1).
 \tag{E832.12}
\]

The compound difference Lambda2 B0-Lambda2 U0 is zero on the four mixed
basis vectors and equals3 on each of the two pure ones. This is exactly
the general-unit degree-two equation with nonzero right side, at the level
of real Hermitian linear algebra. B0 is indefinite, and U0 also lacks
positive trace in both blocks. Thus it violates the hypotheses used in
section3 and gives no counterexample to it.

This boundary example is not asserted to define a rational line class for
a genuine RM lattice, an integral positive-rank star, the full balanced
Chern character, a coherent object or a semiregular seed. It only prevents
the scalar spectral argument from being overextended without the actual
positivity supplied in section5.

## 7. Source and check boundary

All new compound-matrix, rank, sign and graph arguments are proved above.
The unit resolution and its canonical defect map are the previously
whole-reviewed US/UG and E825 inputs, used exactly as stated. The only
categorical input for the general-B application is E825's already proved
necessary determinant condition, in its preserved finite-action scope;
no new source on stability, Hodge classes or generic rank is imported.
The exact supplementary script rm_elliptic_star_character_certificate.py
actually passed the unit expansion, completed square, determinant-product
identity, all15 four-edge graphs and the printed boundary matrices in
0.053802978s. It does not numerically certify the universal Hermitian
positivity argument, the actual E825 interface or the existence of a seed. No successful seed or general nonexistence
outside the stated star architectures is claimed.

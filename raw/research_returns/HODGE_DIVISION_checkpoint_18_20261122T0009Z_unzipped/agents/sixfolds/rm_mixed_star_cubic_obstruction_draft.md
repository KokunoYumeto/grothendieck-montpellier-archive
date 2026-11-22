# SF-E833. The full cubic character excludes every square-zero star

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** complete new proof, submitted for independent whole-proof
review. This uses the full cubic character and strictly extends E832's
same-center obstruction to arbitrary signs. It does not treat multiple
centers, a different unit character, or an unproved defect determinant.
No assertion about a successful balanced seed is made.

## 1. The exact character and defect hypotheses

Let X be the abelian fourfold with orthogonal rank-two RM tangent planes
V_+, V_- and polarization theta=theta_++theta_-. Let D=k theta, k>0.
The actual unit F on the smooth complete-intersection surface has

\[
 \operatorname{ch}(F)=2e^{-D}-2e^{-3D}+e^{-4D}
                  =1-2D^3+4D^4.
 \tag{E833.1}
\]

Fix positive integers r,m. Consider an actual exact sequence

\[
 0\longrightarrow A\longrightarrow E\longrightarrow B\longrightarrow0,
 \quad A=(F\otimes L)^{\oplus r}\oplus A_{\mathrm f},
 \tag{E833.2}
\]

where A_f and B are direct sums of line bundles of total rank m. Either
of these two free sums may be empty. Require that the first Chern classes
of all those free lines, counted with positive multiplicities n_j, lie on
one square-zero star:

\[
 c_1(N_j)=\alpha_0+\eta_j,\qquad \eta_j^2=0,
 \qquad\sum_jn_j=m.
 \tag{E833.3}
\]

The center alpha0 may be any fixed real (1,1) class; it need not occur as
an actual free summand. There is no sign condition on eta_j and no slope
condition on the given exact sequence. A real Hermitian square-zero
(1,1) form has rank at most one, but that equivalence is not needed below.

Then E admits no weakly semiregular balanced lift with character R v_q,
where R=r+m and q is nonzero, for any algebraic rational B field and any
specified coherent effective finite action in E825's scope.

More generally, the same conclusion applies whenever the actual object
has the displayed character identity and E825's defect determinant is
proved to extend from X as r c1(L). This last hypothesis is not assumed
for arbitrary gluing; equation(E833.2) supplies it explicitly in section5.

## 2. A compound-matrix lemma without a positivity hypothesis on b

Normalize theta to the identity Hermitian form. Suppose u preserves the
RM planes, and its Hermitian blocks U,V both have the same strictly
positive trace h. Suppose b is any real Hermitian form satisfying

\[
 b^2-\kappa u^2=d(\theta_+^2+\theta_-^2),
 \qquad \kappa>0,\quad d\ne0.
 \tag{E833.4}
\]

Let B be b's matrix and let Pi be the sum of the two pure-plane
projections on Lambda2(V_+ direct sum V_-). The invariant-form
identification proved in E832 gives

\[
 \Lambda^2B=\kappa\Lambda^2\operatorname{diag}(U,V)+d\Pi.
 \tag{E833.5}
\]

Neither U nor V is zero because its trace is h. We first show that both
are invertible. Suppose U has rank one.

If V also has rank one, the right side of(E833.5) has rank three: its
two pure-line coefficients are d and d, and its mixed block U tensor V
has rank one. Both pure lines belong to its image. Since
im(Lambda2 B)=Lambda2 im(B), their two support planes must both lie in
im(B). Thus B has rank four, whose compound has rank six, a contradiction.

If V has rank two, the pure V_+ line still has coefficient d and lies
in the image. The mixed image is im(U) tensor V_-, of dimension two.
Write im(U)=C a with a nonzero in V_+. The image therefore contains the
bivectors a wedge v for every v in V_-. A nonzero decomposable bivector
in Lambda2 W has its whole support plane in W: contract by linear
functionals, or write its two independent factors in a basis extending W.
Applying this to W=im(B), the pure V_+ line first gives V_+ contained in W;
the mixed bivectors then give all V_- contained in W. Again B has rank
four. But the right side of(E833.5) has mixed rank two and at most two
pure-line ranks, hence rank at most four, a contradiction. The same
argument interchanging the planes treats rank-one V. Thus U,V are both
invertible. No semipositivity or determinant sign entered this argument.

The mixed block U tensor V now has rank four. A four-dimensional
operator of rank at most three has compound rank at most three, so
(E833.5) forces B invertible. Its compound is invertible too. Each pure
line is preserved, with nonzero eigenvalue, by the right side. Hence B
preserves each support plane. It is block diagonal with invertible
Hermitian blocks C,D1, and

\[
 C\otimes D_1=\kappa U\otimes V.
 \tag{E833.6}
\]

Equality of nonzero simple tensors gives C=tU and D1=(kappa/t)V. The
scalar t is nonzero and real: if two nonzero Hermitian matrices are
complex scalar multiples, taking adjoints makes that scalar equal to its
conjugate. Consequently, as invariant forms,

\[
 u=p+z,\qquad b=t p+(\kappa/t)z,
 \quad p=u|_{V_+},\quad z=u|_{V_-},\quad t\in\mathbb R^*.
 \tag{E833.7}
\]

In particular p and z are nondegenerate. This is the entire conclusion
of the lemma; it does not assert that b or u is semipositive.

## 3. Complete second and third character calculation

After an algebraic rational B shift, put u=c1(L)+B and alpha=alpha0+B.
Set H=sum_j n_j eta_j. The actual K0 identity and eta_j²=0 give

\[
 e^B\operatorname{ch}(E)
  =r e^u(1-2D^3+4D^4)+e^\alpha(m+H).
 \tag{E833.8}
\]

This is the full character, not only its first terms. If it equals
R v_q, its first, second and third characters are respectively zero,
-Rq(theta_+²+theta_-²)/2, and zero. The first equation gives
H=-ru-m alpha. The second equation is exactly E832.9:

\[
 b=\alpha+xu,\quad x=\frac rm>0,\qquad
 b^2-\kappa u^2=d(\theta_+^2+\theta_-^2),
 \quad\kappa=x(1+x)>0,\quad d=(1+x)q\ne0.
 \tag{E833.9}
\]

The cubic character is, with every coefficient displayed,

\[
 0=\frac1m\operatorname{ch}_3(E;B)
   =\frac x6u^3-\frac x2u\alpha^2-\frac13\alpha^3-2xD^3.
 \tag{E833.10}
\]

Indeed the free contribution before eliminating H is
m alpha³/6+H alpha²/2, which becomes -r u alpha²/2-m alpha³/3.
The unit contributes r u³/6-2rD³. Thus there is no missing Chern-class
normalization or factor of six in(E833.10).

Suppose the actual E825 condition has given u block diagonal and both
block traces h=7k. The lemma of section2 applies to(E833.9). With its
notation p,z,t, put

\[
 a=t-x,\qquad c=\kappa/t-x,
 \qquad \alpha=a p+c z.
 \tag{E833.11}
\]

Since p³=z³=0, expand(E833.10) as

\[
 A_+p^2z+A_-pz^2=2xD^3,
 \quad
 A_+=\frac x2(1-a^2-2ac)-a^2c,
 \quad
 A_-=\frac x2(1-c^2-2ac)-ac^2.
 \tag{E833.12}
\]

The two mixed cohomological components lie in the direct sum of
the invariant bigraded spaces H^(2,2)(V_+) tensor H^(1,1)(V_-) and
H^(1,1)(V_+) tensor H^(2,2)(V_-). On each plane its normalized polarization is
the identity, so p²=(det U)theta_+² and z²=(det V)theta_-². Also
D³=3k³(theta_+²theta_-+theta_+theta_-²). Thus(E833.12) gives the two
actual equations of (1,1) forms

\[
 A_+\det(U)\,z=6xk^3\theta_-,\qquad
 A_-\det(V)\,p=6xk^3\theta_+.
 \tag{E833.13}
\]

The scalar 6xk³ is nonzero. The first equation forces z to be a nonzero
scalar multiple of theta_-; the second forces the same for p and theta_+.
The traces of both blocks are h=7k. Since the trace of each plane's
identity is two, these scalar multiples are both 7k/2. Hence

\[
 u=\frac{7k}{2}\theta.
 \tag{E833.14}
\]

Now(E833.9) contradicts the scalar-unit lemma E832§2, applied with
c0=kappa(7k/2)² and d nonzero. This proves the desired incompatibility.
Notice that if either coefficient A_+ or A_- vanishes, the corresponding
equation(E833.13) is already impossible; no division by an unproved
nonzero coefficient has been made.

## 4. Why this is stricter than the uniform-sign theorem

Only the identity eta_j²=0 was used. Their signs, the sign of their sum
H, and the ranks of the actual extension matrices never entered. The
semipositive lemma E832§3 is not used; the argument replaces its missing
positivity with the nonzero cubic unit term and a separate singular-block
analysis. Even indefinite b and indefinite adjusted u are accounted for.
The earlier real-Hermitian counterexample to a second-character-only
argument does not satisfy these full cubic equations with the prescribed
unit and its defect traces.

The common center is essential to the displayed proof: it supplies the
exact free character e^alpha(m+H) and hence the single completed-square
form b. Several centers produce several such terms, and the present
argument does not combine them into one. Nor does it address arbitrary
perfect complexes with signed virtual free multiplicities or r/m of
unknown sign.

## 5. Actual determinant, finite actions and source boundary

For(E833.2), B is locally free, so choose local splittings compatible with
A. Within A the unit transition is precisely that of F tensor L, to
multiplicity r. Every other diagonal block is free; every new extension
entry goes from the free B part to A. After removing the fixed F
comparison, E825's actual multiplicative ring map ell kills all free
blocks and every factorization through a free module. Its FF transition
is exactly the scalar L transition to multiplicity r. Therefore its
intrinsic first-neighborhood defect bundle is Qtilde=L^r, and the
determinant extends as r c1(L) on X.

E825.3--4, for the given coherent effective finite action and the chosen
rational algebraic B field, would force
u-7D/2 to have zero mixed RM blocks and to be primitive separately on
both planes. This is exactly the block-diagonal condition and the equal
traces h=7k used above. The condition is intrinsic to E; the argument does
not add an equivariance assumption on the chosen filtration or its
summands. No pullback preservation of semiregularity is being asserted.

The original unit resolution and E825 condition are the already
whole-reviewed inputs, with their published BF and supplied S21 scope
unchanged. E832§1--2 supplies the explicitly proved invariant-form
identification and scalar spectral lemma. Every new compound-rank,
support-plane, cubic and actual-cocycle step has been proved above.
A separate exact algebra supplement checks the expansions only; it is
not a numerical premise for the universal Hermitian or sheaf arguments.

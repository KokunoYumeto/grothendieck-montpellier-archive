# DET-12 and DET-14: actual Gram kernels, determinant lines, and positive period frames

Run TRACE_DET_20261121. Date 21 November 2026 (UTC). Agent `/root/step1_history_route`, GPT-6 Astra Pro; effort setting not exposed. All Lean paths below are relative to `work/external_lean/lean/src`. The inspected snapshot is the already recorded public release mirror. Source readings are not Lean build checks or independent re-proofs of imported representation-theoretic theorems. This note does not edit the deliverables.

## Result and exact movement of the gate

The direct signed Gram scalar fails a stronger positivity test than positivity of its original matrix: it is not a positive semidefinite kernel, a positive-type group function, or even a squared Hilbert-space distance in a source-admissible rank-zero slice. Consequently, it cannot be obtained as a pointwise limit of positive-type kernels, or as a positive trace-class coefficient of a unitary representation. This closes those particular direct constructions; it says nothing adverse about suitable transforms of the scalar.

There is also affirmative structure. The scalar is a squared norm on the appropriate determinant line, and on the open set where the source leading minor D_r is nonzero it has an explicit Lorentz-projection factorization. Separately, the actual normalized Bessel maps and positive formal degrees give finite positive frame operators on a common target space, with exact Gram determinant and exterior-power formulas. The source provides a finite-family existence export, not merely an uninstantiated positivity definition.

For that finite-family route, two concrete continuation restrictions replace a vague limit question. The displayed existence export uses a fixed finite-dimensional target, which bounds the degrees of all its frame determinants. Also, its numerical hypotheses force 100(q0+1) <= ga,h, so q0 cannot tend to infinity with the displayed numerical data fixed. A Xi limit through this route therefore needs changing data and an infinite-dimensional realization, together with a compatible choice of vectors/maps and a summability estimate. The exact trace-class criterion for a compatible rank-one series is proved below. No historical identification of Remark steps 1, 4, or the whole of 7 follows from these results.

## Source data retained throughout

`Formalism/FormalDegreeBessel/StatementG.lean:9` defines the linear-first Hermitian form h(v,w)=w*Hv. Lines 20–24 define H=Hpk(k,r) of signature (r+k,r+1); lines 28–31 define the middle-block support condition and T(z)=-h(z,z). The source form is real on the diagonal. Lines 61–71 define the flag vectors, the cross-pairing matrix Zhat, and its leading minors D_l. Lines 85–99 define

\[
G_f=|D_{r+1}|^2-T(z)T(z')|D_r|^2
\]

and the Gram matrix of the ordered vectors

\[
e_0,\ldots,e_{r-1},z,ge_0,\ldots,ge_{r-1},gz'.
\]

The hypotheses used below are exactly the support conditions on z,z', the inequalities T(z),T(z')>0, and g*Hg=H. `GGram` and `GNonneg` are proposition definitions at lines 165–172; actual exports are `Formalism/FormalDegreeBessel/FinalG.lean:21–22`. DET-10 already independently proves the balanced-inertia sign. The arguments below do not strengthen those source statements into matrix positivity.

For period maps, `Development/AbelianVarietyTheory/Definitions/Jets/SumIoPrAlt.lean:135–139` defines `IsBeL`. If it holds, then for x in R.sm and v in R.TK,

\[
\operatorname{be}(x,v)\eta=\langle l(v),\eta\rangle l(x),
\tag{P1}
\]

where the brackets in the period portions of this note are conjugate-linear in the first variable. `Development/AbelianVarietyTheory/Definitions/Jets/SideFam.lean:36–40` gives, for every integral shift nu with n1(nu)<=q0, `IsBeL`, a positive number dg(nu), and equality of that number with the specified formal degree for every nonzero vector. All l_nu have the same target Wp. This is a finite-family condition: the number of coordinates of nu is n=2r+k+1, and |nu_i|<=q0 gives only finitely many such shifts.

The actual theorem `CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/ExistsFamilyFunctionalsStatement.lean:17–18` supplies both left and right `SideFam` systems under its full `HypsG`, `Num`, `IsFamG`, and parameter/measure hypotheses, with finite-dimensional Wp and Wq. Its complete underlying proof at `ExistsFamilyFunctionals.lean:21–50` was read: it constructs normalized maps on the bounded shift set, chooses zero outside that set, and takes dg(nu)=c fdegHC(lambda+nu), with c>0 and positivity proved on the bounded set. The analytic hypotheses and dependencies are retained here; their entire imported proofs were not independently replayed.

## DET-12A. The direct actual scalar is not a positive kernel

### Statement

Set r=0, k=2, H=diag(1,1,-1). For negative unit vectors z,z' define

\[
K(z,z')=|h(z',z)|^2-1.
\]

This is exactly G_f(2,0,z,z',I). It is not a positive semidefinite kernel on this source-admissible set. There is no Hilbert space and feature map Phi satisfying K(z,z')=<Phi(z),Phi(z')>. It is not a pointwise limit of positive semidefinite kernels on that set. The same conclusions apply after dividing the unnormalized scalar by T(z)T(z'), since that normalized kernel restricts to K on the negative unit vectors.

### Complete proof

For t real put z(t)=(sinh(t),0,cosh(t))^T. The middle-block support condition is vacuous when r=0. The identity cosh(t)^2-sinh(t)^2=1 gives h(z(t),z(t))=-1, so T(z(t))=1>0. Also I*HI=H. Hence all these pairs satisfy the source hypotheses. Direct calculation gives

\[
h(z(t),z(s))=-\cosh(t-s),\qquad
K(z(s),z(t))=\sinh^2(t-s).
\tag{12.1}
\]

In particular, K(z,z)=0, whereas K(z(0),z(t))>0 for t!=0. The two-point matrix is

\[
\begin{pmatrix}0&c\\c&0\end{pmatrix},\qquad c=\sinh^2(t)>0.
\]

Its quadratic form at (1,-1) is -2c<0, so the kernel is not positive semidefinite. A Hilbert Gram kernel is positive semidefinite because its quadratic form is the squared norm of a finite linear combination of feature vectors, so no such feature map exists. Equivalently, its zero diagonal would force every feature vector to be zero.

If K_j are positive semidefinite kernels converging pointwise to K, then, for any fixed finite points and coefficients, the quadratic form of K is the limit of the nonnegative quadratic forms of K_j. It is therefore nonnegative. Applying this to the displayed two-point example gives a contradiction. This argument works for sequences or nets. The final normalization assertion follows by restricting to the unit vectors already used. ∎

### Group and positive trace coefficient versions

Let z0=(0,0,1)^T and define the function on the actual group UH(H)

\[
F(g)=G_f(2,0,z_0,z_0,g)=|h(gz_0,z_0)|^2-1.
\]

Then F is not of positive type. In particular, there is no unitary representation pi on a Hilbert space and no positive trace-class operator A such that F(g)=Tr(A pi(g)) for every g. Nor is F a pointwise limit of functions of positive type.

**Proof.** The real matrices

\[
g(t)=\begin{pmatrix}
\cosh t&0&\sinh t\\
0&1&0\\
\sinh t&0&\cosh t
\end{pmatrix}
\]

satisfy g(t)*Hg(t)=H, g(t)z0=z(t), and g(s)g(t)=g(s+t). These assertions follow by multiplication and the hyperbolic addition identities. Consequently F(e)=0 and F(g(t))=sinh^2(t). The positive-type matrix for the two group elements e,g(t) is precisely the indefinite two-point matrix above, because g(t)^-1=g(-t) and F(g(-t))=F(g(t)). Thus F is not of positive type, and the pointwise-limit argument applies unchanged.

For completeness, every claimed trace coefficient would be of positive type. If X=sum_j c_j pi(g_j), then

\[
\sum_{i,j}\overline{c_i}c_j\operatorname{Tr}
 \bigl(A\pi(g_i^{-1}g_j)\bigr)
=\operatorname{Tr}(AX^*X)
=\|XA^{1/2}\|_{\mathrm{HS}}^2\ge0.
\]

Here A^{1/2} is Hilbert–Schmidt since A is positive trace class, and the cyclic trace identity applies to the indicated bounded/Hilbert–Schmidt factors. There is an even shorter contradiction at e: Tr(A)=F(e)=0 implies ||A^{1/2}||HS=0, hence A=0, whereas F(g(t))>0. ∎

### The scalar is not a squared Hilbert distance either

For a>0 use t=(-a,0,a) and real coefficients c=(1,-2,1), which sum to zero. Equation (12.1) gives

\[
\sum_{i,j}c_i c_j K(z(t_i),z(t_j))
=2\sinh^2(2a)-8\sinh^2(a)
=8\sinh^4(a)>0.
\tag{12.2}
\]

This violates conditional negative semidefiniteness. If K(x,y)=||Phi(x)-Phi(y)||^2, expansion and sum_i c_i=0 would give instead

\[
\sum_{i,j}c_i c_j K(x_i,x_j)
=-2\left\|\sum_i c_i\Phi(x_i)\right\|^2\le0.
\]

Thus no such squared-distance representation exists. The identity in (12.2) follows from sinh(2a)=2sinh(a)cosh(a) and cosh(a)^2-1=sinh(a)^2; no asymptotic or numerical approximation is used. ∎

These are obstructions to the direct scalar, its direct normalized version, and the stated group coefficient. They do not exclude an inverse, exponential, integral transform, added/subtracted term, or other modified family. They also do not assert that arbitrary finite determinant polynomials are positive-type functions of their spectral parameter.

## DET-12B. The affirmative determinant-line and projection factorizations

### Determinant lines

Write q=r+1 and let X be the matrix of the 2q Gram vectors. The exterior form induced by h on Lambda^(2q)(C^(2r+k+1)) is defined on decomposable vectors by

\[
h^{[2q]}(x_1\wedge\cdots\wedge x_{2q},
          y_1\wedge\cdots\wedge y_{2q})
=\det[h(x_j,y_i)]_{i,j}.
\]

For omega equal to the wedge of the columns of X, the actual Gram identity gives G_f=(-1)^q h^[2q](omega,omega). If M=X*HX is nonsingular, DET-10 shows that V=im X has signature (q,q). On the one-dimensional determinant line Lambda^(2q)V, the form (-1)^q h^[2q] is therefore positive definite. Indeed, in an h-orthonormal basis of V, its value on the top wedge is (-1)^q times the product of q positive and q negative signs, hence 1; every other nonzero vector in that line is a nonzero scalar multiple and has positive squared norm. In that precise line, G_f is a squared norm.

This does not give a positive metric on the whole ambient exterior power when k>=2. The ambient signature is (p,q) with p=r+k. There is a basis wedge using q positive and q negative directions; the signed exterior form has value +1 on it. There is also a basis wedge using q+1 positive and q-1 negative directions, since p>=q+1 when k>=2; the same signed form has value -1 on this wedge. Thus it is indefinite. When k=1 the ambient dimension is 2q, so the exterior power is itself the positive determinant line after this sign adjustment. When k=0 its degree exceeds the ambient dimension and the exterior space is zero. At a degenerate restricted form, the displayed wedge has zero value and does not define a positive definite line metric. These assertions follow directly from the product of signs in the defining determinant and cover every k>=0.

The finite compound matrices and wedge coordinates in `SumIoPrAlt.lean:104–110` implement this exterior algebra. The signed tensor form in `TensH`, lines 88–94, has independent signs epsilon_I in {+1,-1}; the determinant-line observation does not erase those signs from the actual period decomposition.

### Explicit positive factorization on D_r != 0

Retain all source hypotheses. Let E have columns e_0,...,e_(r-1), put F=gE and y=gz', and set

\[
C=E^*HF,\quad b=E^*Hy,\quad c=z^*HF,\quad d=z^*Hy.
\]

Then Zhat is the block matrix [[C,b],[c,d]], so D_r=det C. Assume det C!=0. Define

\[
U=\operatorname{im}E+\operatorname{im}F,
\quad
x=z-E(C^*)^{-1}c^*,
\quad
y_0=y-FC^{-1}b,
\quad
s=d-cC^{-1}b.
\tag{12.3}
\]

The space U is nondegenerate of signature (r,r). Both x,y0 belong to U^perp; they satisfy h(x,x)=-T, h(y0,y0)=-T', and h(y0,x)=s, where T=T(z)>0 and T'=T(z')>0. Consequently

\[
V_+=U^\perp\cap x^\perp,
\qquad p=y_0+\frac{s}{T}x
\]

is a positive definite space of dimension k together with a vector p in it, and

\[
G_f=|\det C|^2 T\,h(p,p)
=\bigl\|\sqrt T\,(\det C)\,p\bigr\|_{V_+}^{2}.
\tag{12.4}
\]

**Complete proof.** Isotropy of E, support of z, and g*Hg=H give

\[
E^*HE=F^*HF=0,\quad E^*Hz=0,\quad F^*Hy=0,
\quad z^*Hz=-T,\quad y^*Hy=-T'.
\]

The Gram matrix of the 2r columns [E,F] is [[0,C],[C*,0]]. Since C is invertible, this matrix is invertible and the columns are independent. Changing basis in the F coordinates reduces this Gram form to [[0,I],[I,0]], which has r positive and r negative directions. Thus U has the stated signature. Direct substitution in (12.3) gives

\[
E^*Hx=F^*Hx=E^*Hy_0=F^*Hy_0=0,
\]

so x,y0 lie in U^perp. The correction to z is in im E, which is isotropic and orthogonal to z, so h(x,x)=h(z,z)=-T. The analogous argument with F and y gives h(y0,y0)=-T'. Expanding x*Hy0 gives

\[
d-cC^{-1}b-cC^{-1}b+cC^{-1}b=d-cC^{-1}b=s.
\]

Since the ambient form has signature (r+k,r+1), subtracting the nondegenerate signature (r,r) of U gives signature (k,1) on U^perp. The vector x is negative. Its orthogonal complement within U^perp is therefore positive definite of dimension k: split off the nondegenerate negative line Cx, after which the remaining signature is (k,0). Also h(p,x)=s+(s/T)(-T)=0. Expanding h(p,p) gives

\[
h(p,p)=-T'+|s|^2/T.
\]

Finally, subtract cC^-1 times the first r rows from the final row of Zhat. This determinant-preserving operation gives D_(r+1)=(det C)s. The definition of G_f now gives (12.4). ∎

When r=0 the empty matrix is invertible with determinant 1, U=0, and (12.4) is the ordinary Lorentz projection formula. When k=0 the positive space has dimension zero, so this formula gives G_f=0 on the stated chart; globally the Gram vectors number 2r+2 in dimension 2r+1, so the Gram identity also gives zero. When D_r=0, no limit or inverse formula is asserted: the source definition directly gives G_f=|D_(r+1)|^2>=0.

The positive space and projection in (12.4) depend on the source data. Fixing the first vector in the rank-zero case fixes a positive space and realizes the scalar as a norm of a projected second vector, but it does not give a two-variable Gram identity for K. The obstruction in DET-12A proves that no reinterpretation of this formula as a single feature map with those cross-inner-products is possible.

## DET-14A. A finite positive Gram family from actual period maps

### Statement

Assume a source `SideFam` system on Wp. Choose a finite set I of shifts with n1(nu)<=q0, vectors v_nu in both (R_nu).sm and (R_nu).TK, and real weights t_nu>=0. Put d_nu=dg(nu)>0 and

\[
a_\nu=\sqrt{t_\nu d_\nu}\,l_\nu(v_\nu),
\qquad
A_I=\sum_{\nu\in I}t_\nu d_\nu
   \operatorname{be}_\nu(v_\nu,v_\nu).
\tag{14.1}
\]

Then A_I is a positive finite-rank operator on the common target Wp, and

\[
A_I=\sum_{\nu\in I}a_\nu a_\nu^*,\qquad
\operatorname{Tr}A_I=\sum_{\nu\in I}t_\nu d_\nu\|l_\nu(v_\nu)\|^2.
\tag{14.2}
\]

Here a a* sends eta to <a,eta>a. For the finite positive Gram matrix M_I=(<a_nu,a_mu>)_(nu,mu in I),

\[
\det_{Wp}(I-wA_I)=\det_{\mathbb C^I}(I-wM_I)
=\sum_{J\subset I}(-w)^{|J|}
 \left\|\bigwedge_{\nu\in J}a_\nu\right\|^2.
\tag{14.3}
\]

Thus the alternating Taylor coefficients are nonnegative squared exterior norms. These are frame determinants constructed from the actual source maps, not an assertion that the signed source exterior-period coefficients already equal these minors.

### Complete proof

The source factorization (P1), applied with x=v=v_nu in the intersection of the two required domains, gives t_nu d_nu be_nu(v_nu,v_nu)=a_nu a_nu*. For any eta,

\[
\langle\eta,A_I\eta\rangle
=\sum_{\nu\in I}|\langle a_\nu,\eta\rangle|^2\ge0.
\]

Each term is bounded, selfadjoint, and has image in the line Ca_nu; hence A_I is a bounded positive operator with finite-dimensional range. A nonzero term has its sole nonzero eigenvalue ||a_nu||^2; the zero-vector case contributes zero. Finite additivity of the trace proves (14.2).

Let S:C^I -> Wp have columns a_nu. Then A_I=SS* and M_I=S*S. Every nonzero eigenvalue lambda of S*S is positive, and S maps its eigenspace injectively to the lambda-eigenspace of SS*, with inverse lambda^-1 S*. The converse follows in the same way. Both operators are selfadjoint and finite rank, so there are no nontrivial Jordan blocks. Their nonzero eigenvalues, with multiplicities, agree. All extra zero eigenvalues contribute factors 1 to the determinants, proving the first equality in (14.3).

Expanding det(I-wM_I) by choosing either the identity column or the corresponding -wM_I column shows that the coefficient for a subset J is (-w)^|J| det((M_I)_J). The identity columns outside J force the corresponding rows in the permutation expansion, leaving precisely that principal minor and no extra sign. The minor is the Gram determinant of the vectors a_nu with nu in J. If they are dependent, both this determinant and their wedge are zero. If they are independent, Gram–Schmidt expresses the Gram determinant as the product of the squared lengths of the successive orthogonal residuals, which is also the squared norm of the wedge in the induced Hilbert exterior power. For J empty both values are 1. This proves the second equality and the coefficient sign. ∎

The weights t_nu and vectors v_nu are choices in this construction; the source theorem does not single out a Xi spectral choice. Taking all t_nu=1 is permitted, and the normalization sqrt(d_nu) is directly used in `BesselExteriorPowerConstantBoundLargeGap.lean:80–85`. The formal-degree positivity, common target, and normalized period factorization are actual source data. Existence of the maps under the displayed source hypotheses is supplied by the export cited above. Nonzero frames require nonzero chosen period values; zero period vectors are allowed and simply contribute zero.

## DET-14B. The exact compatible-series trace criterion

Suppose a countable collection of the vectors in (14.1), after any specified compatible isometric embeddings, is realized as vectors a_1,a_2,... in a single Hilbert space H. Define A_N=sum_(j<=N) a_j a_j*. Then the following are equivalent:

1. sum_j ||a_j||^2 is finite.
2. sup_N Tr(A_N) is finite.
3. A_N converges in trace norm to a trace-class operator A.

When these hold, A is positive and

\[
\operatorname{Tr}A=\sum_j\|a_j\|^2,
\qquad
\|A-A_N\|_1=\sum_{j>N}\|a_j\|^2.
\tag{14.4}
\]

**Complete proof.** A rank-one positive operator a_j a_j* has trace norm ||a_j||^2, as follows from its sole nonzero eigenvalue. Thus (1) makes the series absolutely convergent in the Banach space S1. Its sum A is trace class. Trace-norm convergence implies operator-norm convergence, and limits of nonnegative quadratic forms are nonnegative, so A>=0. Each tail A-A_N is likewise positive. The trace is continuous in trace norm, since |Tr T|<=||T||1; therefore the trace of A and of each tail equals the corresponding scalar sum. A positive trace-class operator has trace norm equal to its trace, giving (14.4). The identity Tr(A_N)=sum_(j<=N)||a_j||^2 makes (1) and (2) equivalent by monotone convergence of nonnegative scalar partial sums. Finally (3) makes the continuous traces Tr(A_N) bounded, proving (2). ∎

For the period vectors this criterion is exactly

\[
\sum_j t_j d_j\|l_j(v_j)\|^2<\infty,
\tag{14.5}
\]

provided the actual vector/space compatibilities have first been given. It is not merely a summability assertion about eigenvalues of a nonnormal operator: the operators here are explicit positive rank-one sums. DET-05 then supplies local uniform Fredholm-determinant convergence. To identify its limit with G requires a separate spectral or coefficient identity with Xi, proved independently of a choice made from Xi's zeros.

## DET-14C. Exact restrictions of the inspected finite-family realization

### Fixed target dimension bounds determinant degree

The existence export cited above assumes finite-dimensional Wp. If d=dim Wp is fixed, then every A_I in (14.1) has rank at most d and every polynomial in (14.3) has degree at most d, however many shifts or vectors are included. Every trace-norm limit acting on that same fixed Wp also has a determinant of degree at most d. More generally, any locally uniform limit on C of polynomials of degrees at most d has degree at most d: Cauchy's integral formula for derivatives gives f^(d+1)=0, since all those derivatives vanish for the approximants. Equivalently, the higher coefficients vanish by the same formula. Such a limit cannot equal the Xi determinant G, which has infinitely many zeros by the independently recorded classical zero count. This is a fixed-target obstruction, not an obstruction to varying targets or infinite-dimensional period models.

### The source cutoff cannot grow with all numerical data fixed

`SumIoPrAlt.lean:155–166`, specifically line 165, includes

\[
100(q_0+1)\le ga,\qquad 100(q_0+1)\le h.
\]

For fixed finite real ga,h, it follows immediately that q0<=min(ga,h)/100-1. Thus no sequence q0 -> infinity can satisfy this displayed `Num` condition with ga,h fixed. Since the existence theorem assumes `Num`, its invocation for arbitrarily large cutoffs requires varying at least these numerical data. This statement is an arithmetic implication of its explicit hypotheses, not an inference from an unsuccessful source search. Varying them may require further parameter/representation changes to satisfy the remaining hypotheses; compatibility of the resulting spaces and maps must be proved rather than presumed.

### The available integrated normalization is a different estimate

`CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/FamilySetupBesselGrowthStatement.lean:16–17` asserts an L2 bound and, when the Bessel map is nonzero, the normalized isometry under its `HypsG` and `SetupG` hypotheses:

\[
d_\nu\int\|l_\nu(\sigma_\nu(g)v)\|^2\,d\nu_q(g)=\|v\|^2
\]

for the stated smooth vectors. This is a useful realization in a common L2 space when its data are fixed. It is not the sum (14.5) of point values and does not, by itself, bound that sum. Even scalar continuous functions can have bounded L2 norm and unbounded value at one point: take a continuous compactly supported phi with ||phi||2=1 and phi(0)!=0, and f_n(x)=sqrt(n) phi(nx). Substitution gives ||f_n||2=1, while |f_n(0)|=sqrt(n)|phi(0)| -> infinity. This elementary example shows exactly why an integrated bound alone cannot replace an evaluation or summability estimate; it does not claim that these particular spike functions are source Bessel coefficients.

The signed exterior-period formula remains separate. In `Development/AbelianVarietyTheory/Proofs/FlagMeasures/BlockProjectionBesselStatement.lean:9–10`, and its use in `FirstNormAddSubsetIndicatorLe.lean:269–289`, the coefficients are epsilon_I kappa_(1,I) conjugate(kappa_(0,I)) d_I. Even if the two side maps are identified so that the kappa product becomes a squared modulus, epsilon_I can be -1. Positive formal degrees alone therefore do not turn that displayed signed expansion into the Gram determinant (14.3). A relation between these two specific constructions requires an additional identity.

## Remaining input, now stated for a concrete candidate

The direct K and F candidates are refuted in DET-12A. The determinant-line and Lorentz formulas describe their valid pointwise positive geometry. The actual period-frame construction in DET-14A is positive and independent of zeros. To use its determinants as an upstream Xi approximation requires:

1. A specified sequence of source data, admissible vectors and positive weights, together with compatible Hilbert embeddings or a fixed infinite-dimensional period model. The fixed finite target and fixed numerical cutoff cannot supply that sequence as stated.
2. The actual squared-norm sum (14.5), or an equivalent proved trace bound for that specified sequence.
3. A proof identifying the resulting Fredholm determinant, or all its normalized exterior coefficients, with G. Neither pointwise positivity nor the formal-degree signs constitute this identity.
4. For the historical question, a separate documentary/declaration correspondence to the Remark's W, S and determinant family. This note supplies no guessed historical match.

The note proves these limited statements rather than claiming that no different source construction exists. It does not use or audit the stipulated RH and Dirichlet theorems, and it does not use Xi zeros to choose the new positive frame.

## Verification record

The first full composition was subsequently read in its entirety. The checks included the source convention h(v,w)=w*Hv; the empty minor at r=0; the source support and unitary conditions for the boost example; the two-point and three-point quadratic forms; the trace coefficient argument; the determinant-line signs and k=0,1 cases; the four projection orthogonality equations; the Schur complement and conjugations; both period domains in (P1); zero weights and vectors; Gram determinant multiplicities; trace-norm tail equality; fixed target degree; and the actual bounded-cutoff inequalities. Independent proof of the kernel and projection portions is recorded separately in `work/gram_kernel_independent.md` with its own events. Source-export reading is recorded separately from the elementary proof checks.

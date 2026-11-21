# F59 amendment: complete rank-one exclusion with an arbitrary bounded scalar complex

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; the inherited reasoning-effort setting is not exposed. Date: 2026-11-21 UTC.

The tensor-dimension lemma below was developed jointly with /root/rectangular_and_theta, whose separate complete proof is in agent_soergel_top_module_gate.md, final SHA256 a17597c65917563c101decf9edc8f1323d4d71461f3ebef1e8fb78eb21601858. The descending-cohomology argument was independently proposed and reconstructed by /root and both agents. This report assembles the complete proof, including the module lemma, so its conclusion does not depend on an unrecorded induction.

This is a two-variable theorem. A possible extension using a published intersection-multiplicity theorem is being checked separately and is not used here.

## 1. The exact theorem and the scope of the scalar replacement

Let k be a field of characteristic zero and let

\[
 A=k[x,y],\qquad \deg x=\deg y=2,\qquad
 W=\langle s_1,s_2\rangle\simeq C_2\times C_2,
\]

where s_1 changes the sign of x, s_2 changes the sign of y, and \(\tau=s_1s_2\) changes both signs. We use the ordinary graded Soergel category for this reflection realization. Its generating bimodules are

\[
 B_1=A\otimes_{A^{s_1}}A(1),\qquad
 B_2=A\otimes_{A^{s_2}}A(1).
 \tag{RC1}
\]

The internal shift has the convention fixed in the existing F59 source audit. Put \(\delta=v+v^{-1}\). A bounded ordinary Soergel complex X has a termwise Euler class in the split Hecke Grothendieck group. Suppose that class is the actual nonstandard rank-one generator

\[
 [X]=P_s=b_1b_2+(b_1-\delta)(b_2-\delta).
 \tag{RC2}
\]

Here b_i is the class of B_i. The expression is the product-category version of \(b_s\otimes b_s+(b_s-\delta)\otimes(b_s-\delta)\).

Let C be an arbitrary bounded complex of finite graded k-vector spaces with

\[
 \chi_v(C):=\sum_{j,e}(-1)^j\dim_k H^j(C)_e\,v^e
          =\delta^2=v^2+2+v^{-2}.
 \tag{RC3}
\]

It is the scalar object \(C\otimes_k A\) with the central unit-bimodule action. In particular its differential is defined over k.

### Theorem RC-A

There is no such pair X,C admitting an actual isomorphism of graded derived A-bimodules

\[
 X\otimes_A^{\mathbf L}X\simeq C\otimes_kX.
 \tag{RC4}
\]

Consequently there is also no homotopy-level quadratic with these objects. Allowing arbitrary bounded cohomological amplitude or nonflat cohomology in X does not repair this rank-one ordinary Soergel lift.

The conclusion concerns actual objects and actual quadratic isomorphisms. The Hecke-algebra Euler identity itself remains valid. The word scalar is essential: a complex of unit bimodules with a differential containing nonconstant polynomials of A is not, in general, a complex of scalar k-vector spaces. Such coefficient objects, localizations removing the homogeneous origin, unbounded completions, and other categorical models are outside RC-A.

## 2. Generic cohomology: the internal grading is deliberately forgotten

Let Q be the fraction field of A, regarded without its internal grading. Ordinary simultaneous graph localization of the Soergel category is exact and monoidal. It has the four simple graph bimodules Q_g, g in W, with

\[
 Q_g\otimes_Q Q_h\simeq Q_{gh},
 \qquad \operatorname{Hom}(Q_g,Q_h)=0\quad(g\ne h).
 \tag{RC5}
\]

Every term of X is free on each side. The ordinary graph localization is the one audited in Elias--Williamson, Localized calculus for the Hecke category, Section 1.1, equations (1.1)--(1.2), and Section 1.2, Theorem 1.6 and Remark 1.7. In particular localized cohomology is a finite sum of the graph modules and localization carries RC4 to its actual generic quadratic.

Let u record cohomological degree. Write

\[
 F(u)=\sum_{g\in W}f_g(u)g,\qquad
 f_g(u)\in\mathbb N[u,u^{-1}],\qquad
 d(u)=\sum_j c_j u^j,\quad c_j=\dim_kH^j(C).
 \tag{RC6}
\]

These are actual cohomological multiplicities, not Euler multiplicities. Künneth over Q gives

\[
 F(u)^2=d(u)F(u).
 \tag{RC7}
\]

The prescribed Euler classes, after forgetting internal shifts, give

\[
 F(-1)=2e+2\tau,\qquad d(-1)=4.
 \tag{RC8}
\]

Indeed b_i gives e+s_i, while b_i-\(\delta\) gives s_i-e. Their two products add to 2(e+\(\tau\)). In particular F and d are nonzero.

For completeness, the positivity argument that determines F is elementary. Its augmentation a(u) satisfies a(u)^2=d(u)a(u), hence a=d in the Laurent polynomial domain. For each positive real u, the coefficients

\[
 \mu_u(g)=f_g(u)/d(u)
\]

form an idempotent probability measure on the finite group W. Its nonempty support S is independent of u because a nonzero Laurent polynomial with nonnegative coefficients is positive on the positive real axis. Positivity implies \(S^2=S\); a finite nonempty subsemigroup of a group is a subgroup. If g_0 maximizes \(\mu(g)\), then

\[
 \mu(g_0)=\sum_{x\in S}\mu(x)\mu(x^{-1}g_0)
\]

is a weighted average of quantities at most this maximum, with every weight positive. Thus all quantities attain the maximum. The measure is uniform on S.

It follows first for every positive real u, and therefore as Laurent polynomials, that \(f_g=d/|S|\) on S and is zero outside S. In RC8 the coefficient of e is 2 and d(-1)=4, so \(|S|=2\), and its other element is \(\tau\). Consequently

\[
 F(u)=\frac{d(u)}2(e+\tau).
 \tag{RC9}
\]

If \(M_j=H^j(X)\), this proves

\[
 \operatorname{rank}_A M_j=c_j
 \quad\hbox{for every j},
 \tag{RC10}
\]

and its generic support consists only of e and \(\tau\), with equal multiplicities. The generic statements allow the rank to be zero; they have not yet excluded torsion cohomology.

Only cohomological degree has been retained here. Localization inverts homogeneous polynomials, and an invertible degree-two element identifies internal shifts differing by two. It would be incorrect to infer coefficientwise evenness in the original internal variable v at this stage. The argument will recover the full internal grading only after proving that every global cohomology module is a sum of actual free graph bimodules.

## 3. An elementary two-variable tensor-dimension theorem

Put \(\mathfrak m=(x,y)\). All finite graded modules below are finitely generated and bounded below in grading; their generators may have negative degrees.

### Lemma RC-B

Let M be a finite graded left A-module of rank r and let V be a nonzero finite-dimensional graded right A-module. Suppose the right actions of x and y have their positive homogeneous degrees. Then

\[
 \dim_k(V\otimes_A M)\ge r\dim_kV,
 \tag{RC11}
\]

with equality if and only if M is graded free, including the zero module as the free module of rank zero.

### Proof

First suppose M is torsion-free. Construct a minimal graded free resolution by choosing homogeneous bases modulo \(\mathfrak m\) at each step. The syzygies are finite because A is Noetherian; every differential has entries in \(\mathfrak m\). Thus its i-th term F_i satisfies

\[
 F_i/\mathfrak mF_i\simeq\operatorname{Tor}_i^A(k,M).
 \tag{RC12}
\]

The explicit Koszul resolution

\[
 0\longrightarrow A
 \xrightarrow{\,a\mapsto(-ya,xa)\,}A^2
 \xrightarrow{\,(b,c)\mapsto xb+yc\,}A
 \longrightarrow k\longrightarrow0
 \tag{RC13}
\]

has the corresponding internal shifts. It is exact by coprimality of x and y. Tensoring it with M shows that Tor_i(k,M)=0 for i>2 and that Tor_2(k,M) is, up to an internal shift, \(\{m:xm=ym=0\}\), which is zero for torsion-free M. Equation RC12 and graded Nakayama therefore give a minimal resolution

\[
 0\longrightarrow F_1\longrightarrow F_0\longrightarrow M
 \longrightarrow0.
 \tag{RC14}
\]

Write f_i for the free ranks. Localization gives \(r=f_0-f_1\). Tensoring RC14 with V and taking vector-space dimensions gives

\[
 \dim(V\otimes_A M)
   =r\dim V+\dim\operatorname{Tor}_1^A(V,M).
 \tag{RC15}
\]

If M is not free, F_1 is nonzero. The socle

\[
 \operatorname{soc}(V)=\{v:vx=vy=0\}
\]

is nonzero, since any nonzero homogeneous vector of maximal degree lies in it. As all entries of the minimal differential are in \(\mathfrak m\), one copy of this socle for each generator of F_1 lies in the kernel after tensoring by V. Thus Tor_1(V,M) is nonzero and RC15 is strict. If F_1=0, M is free and equality holds.

For arbitrary M let T be its full torsion submodule and let Q_0=M/T. These are finite graded modules, Q_0 is torsion-free, and it has the same rank r. To see that T is graded, start with a polynomial annihilating an element and inspect the equation in the highest homogeneous degree. Its highest component is torsion; subtract that component and descend. The quotient is torsion-free because if az is torsion for a nonzero a, then baz=0 for some nonzero b, so z is torsion.

If Q_0 is not free, the established strict inequality applies to \(V\otimes Q_0\), and the surjection \(V\otimes M\to V\otimes Q_0\) gives strict inequality for M. If Q_0 is free, lift a homogeneous free basis to split \(M\to Q_0\) as a left-module map. Hence M is Q_0 direct sum T as a left module. If T is nonzero, \(V\otimes T\) is nonzero: it surjects onto

\[
 (V/V\mathfrak m)\otimes_k(T/\mathfrak mT),
 \tag{RC16}
\]

whose factors are both nonzero by graded Nakayama. This gives strict inequality again. If T=0, M is free and equality holds. Only a left-module splitting was used; no bimodule splitting was claimed. QED.

### Two consequences for bimodules

If M is a nonzero finite graded A-bimodule, finite on the left, then

\[
 M\otimes_A M\ne0.
 \tag{RC17}
\]

Indeed \(V=k\otimes_A M\), using the left action, is a nonzero finite-dimensional graded right module. Its positive-degree right action is nilpotent. The left-origin fiber of \(M\otimes M\) is \(V\otimes M\), and this surjects onto
\((V/V\mathfrak m)\otimes_k(M/\mathfrak mM)\ne0\).
This uses the positive grading and common origin, not an assertion about arbitrary unrelated ungraded bimodule supports.

If in addition an actual left-module isomorphism

\[
 M\otimes_A M\simeq U\otimes_k M,\qquad
 \dim_kU=\operatorname{rank}_A M
 \tag{RC18}
\]

holds for a finite graded scalar space U, then M is left-free. Taking the left-origin fiber gives equality in RC11 for \(V=k\otimes_A M\), so RC-B applies. The numerical rank condition in RC18 is essential and will be supplied by the generic quadratic.

## 4. Global free graph modules from codimension two

We will repeatedly use the following elementary upgrade.

### Lemma RC-C

If M is a finite graded left-free A-bimodule whose generic support is contained in e and \(\tau=(-x,-y)\), then it is a finite direct sum of graded shifts of \(A_e\) and \(A_\tau\). In particular it is free on the right as well.

### Proof

Let U,V be the matrices of right multiplication by x,y in a homogeneous left basis. On the two generic graph types,

\[
 yU=xV,\qquad U^2=x^2I.
 \tag{RC19}
\]

Left torsion-freeness extends these identities to A. Entrywise coprimality gives \(U=xZ,V=yZ\) for a homogeneous degree-zero A-linear matrix Z. Then \(Z^2=I\). The idempotents \((I+Z)/2\), \((I-Z)/2\) are bimodule endomorphisms, and their images have respectively ordinary and \(\tau\)-twisted right actions.

Each image is a finite graded left-projective module. Such a module is graded free: lift a homogeneous basis modulo \(\mathfrak m\) to get a finite graded free surjection, split it by graded projectivity, and observe that the complementary kernel has zero quotient modulo \(\mathfrak m\), hence is zero by graded Nakayama. Thus the two images are sums of shifted graph bimodules. Twisting by the automorphism \(\tau\) preserves right freeness. QED.

## 5. The highest global cohomology is visible and free

Let \(a=\max\{j:H^j(X)\ne0\}\) and \(c=\max\{j:H^j(C)\ne0\}\). Both exist, and both complexes have nonzero cohomology by RC8. Put \(M_a=H^a(X)\).

The top-truncation identity for derived tensor gives

\[
 H^{2a}(X\otimes_A^{\mathbf L}X)
       \simeq M_a\otimes_A M_a.
 \tag{RC20}
\]

There is no cohomology in higher degrees. This is the top-degree identity, not a general Künneth splitting: bounded-above flat resolutions with no terms above the respective bounds compute the top cohomology as the tensor of the top cokernels. By RC17 the right side is nonzero. Scalar Künneth makes the highest degree of \(C\otimes_kX\) equal to c+a, with nonzero top group. The actual quadratic therefore forces c=a.

Let b be the highest cohomological degree of the generic graph localization of X. Its generic top has nonzero tensor square because total graph dimensions multiply. The localized quadratic similarly gives \(2b=b+c\). Therefore

\[
 b=c=a.
 \tag{RC21}
\]

In particular the highest global cohomology has positive rank; it is not a generically invisible torsion module. Put \(r=\operatorname{rank}_A M_a=c_a>0\), using RC10. Equations RC4 and RC20 give

\[
 M_a\otimes_A M_a\simeq H^a(C)\otimes_kM_a.
 \tag{RC22}
\]

Its scalar multiplicity has dimension c_a=r. The consequence RC18 of the tensor-dimension theorem proves that M_a is left-free. Lemma RC-C makes it a sum of actual free e- and \(\tau\)-graph modules, hence right-free.

The order of this argument matters: global top nonvanishing was proved first, then its survival under generic localization, and only then was the rank hypothesis used.

## 6. The canonical near-top Künneth map

The following one-sided argument supplies the induction without assuming bimodule formality.

### Lemma RC-D

Suppose that \(M_i=H^i(X)\) is right-projective for every i>s, and that a is the highest cohomology degree of X. If s<a, the canonical cycle cross-product

\[
 \bigoplus_{i+j=a+s}M_i\otimes_A M_j
 \longrightarrow H^{a+s}(X\otimes_A^{\mathbf L}X)
 \tag{RC23}
\]

is an isomorphism of graded bimodules.

### Proof

Forget only the left action. The bounded complex X consists of projective right modules. Split off, as a right-module complex, each of the projective cohomology modules in degrees i>s, starting at the top. This can be done by choosing sections of the surjections from cycles onto those projective modules and cancelling the resulting contractible pairs. Equivalently, after removing acyclic top projective tails, each top projective cohomology splits off and the process repeats. One obtains a right-module homotopy decomposition

\[
 X\simeq
   \left(\bigoplus_{i>s}M_i[-i]\right)\oplus X_{\le s},
 \tag{RC24}
\]

where the last complex has cohomology at most s, top cohomology M_s, and may be chosen right-projective and bounded above. This is a decomposition only in the right-module category.

Tensor RC24 over A with the second X. Each higher M_i is right-flat, so its contribution to degree a+s is \(M_i\otimes_A M_{a+s-i}\). The remaining summand has highest possible degree s+a, and its top group is \(M_s\otimes_A M_a\), by the same top-truncation identity as RC20. These are exactly all summands in RC23; no summand with first index below s can occur because its second index would exceed a.

The maps used on these summands are represented by the ordinary cycle cross-product. The right-module splitting proves that this canonical map is bijective on underlying graded vector spaces. The canonical cross-product is itself left- and right-A-linear. Consequently it is an isomorphism of bimodules even though the auxiliary splitting RC24 was only right-linear. No bimodule formality or bimodule splitting of X is inferred. QED.

## 7. Descending induction forces every cohomology module to be free

Define the ordinary left-origin fiber size of a finite graded left module N by

\[
 \phi(N)=\dim_k(k\otimes_A N)
        =\dim_k(N/\mathfrak mN).
 \tag{RC25}
\]

It is finite, and it is zero exactly when N=0 by graded Nakayama. For a graded free module it is its free rank, independently of its shifts.

We already know that M_a is a sum of free graph modules and has rank r=c_a>0. Suppose inductively that every M_i with i>s is a sum of free e- and \(\tau\)-graphs. Put

\[
 N=M_s,\qquad z=\phi(N).
\]

Lemma RC-D computes degree a+s of the left side of the quadratic as an actual direct sum of the indicated tensor products. In that direct sum the two terms involving N are \(M_a\otimes_A N\) and \(N\otimes_A M_a\). Each has left-origin fiber dimension r z. For right tensoring this is immediate from the graph summands of M_a: it merely twists the right action of N. For left tensoring it twists the left action by e or \(\tau\); these automorphisms preserve \(\mathfrak m\), so the origin-fiber dimension is unchanged.

All other contributing cohomology modules have degrees strictly above s and are graph-free. Their total fiber contribution is

\[
 S_s=\sum_{\substack{i+j=a+s\\i>s,\ j>s}}c_i c_j.
 \tag{RC26}
\]

Thus the left side of the actual degree-a+s cohomology isomorphism has fiber dimension \(2rz+S_s\).

On the right, scalar Künneth gives the actual bimodule sum

\[
 H^{a+s}(C\otimes_kX)
 =\bigoplus_{j+i=a+s}H^j(C)\otimes_kM_i.
 \tag{RC27}
\]

Since both X and C have top degree a, the term with j=a has fiber dimension r z. The term with i=a,j=s has dimension \(r c_s\). Every other term has both indices strictly above s, and their total is exactly S_s by RC10. Applying the ordinary left-origin fiber to this actual isomorphism and taking dimensions therefore gives

\[
 2rz+S_s=rz+r c_s+S_s.
 \tag{RC28}
\]

As r>0,

\[
 \phi(M_s)=z=c_s=\operatorname{rank}_A M_s.
 \tag{RC29}
\]

If c_s=0, graded Nakayama gives M_s=0. Otherwise choose homogeneous lifts of a basis of \(M_s/\mathfrak mM_s\). They give a surjection from a graded free module of rank c_s to M_s. Its kernel has rank zero, since M_s has rank c_s. That kernel is a submodule of a free module over the domain A, so it is torsion-free; a torsion-free rank-zero module is zero. Therefore M_s is graded free.

Lemma RC-C then upgrades M_s to a sum of actual free graph bimodules, and in particular makes it right-free, as needed for the next induction step. Descending through the finitely many possible cohomology degrees proves

\[
 \text{every }H^j(X)\text{ is a finite sum of shifted }A_e
 \text{ and }A_\tau.
 \tag{RC30}
\]

This is the step that excludes all remaining nonflat cohomology in the two-variable case. Neither a purity hypothesis nor a splitting of X as a bimodule complex is involved.

## 8. Global graded multiplicities give the contradiction

We may now record both internal and cohomological degrees in actual global free graph summands. There are finite Laurent polynomials

\[
 a(v,u),b(v,u)\in\mathbb N[v,v^{-1},u,u^{-1}]
\]

such that the global cohomology character of X is
\(a(v,u)e+b(v,u)\tau\). Here b is nonzero by RC9. Set

\[
 d(v,u)=\sum_{j,e}\dim_kH^j(C)_e\,v^e u^j.
 \tag{RC31}
\]

All cohomology modules of X are right-projective. The same one-sided splitting used in RC-D, now in all degrees, proves that the canonical cross-product is an isomorphism in every degree:

\[
 \bigoplus_{i+j=t}H^i(X)\otimes_AH^j(X)
       \simeq H^t(X\otimes_A^{\mathbf L}X).
 \tag{RC32}
\]

As before this is a bimodule statement justified through bijectivity of a canonical bimodule map, not a claim of bimodule formality.

The two graph types can be compared separately. A bimodule map from an identity graph to a \(\tau\) graph, or conversely, has every coefficient killed by 2x, so it is zero in the polynomial domain. Graded free ranks within each graph type have unique Laurent multiplicities, as seen by the left-origin fiber. The actual quadratic therefore gives

\[
 a^2+b^2=da,\qquad 2ab=db.
 \tag{RC33}
\]

The ring \(\mathbb Z[v,v^{-1},u,u^{-1}]\) is a domain and b is nonzero. Hence d=2a. Take the cohomological Euler specialization u=-1:

\[
 v^2+2+v^{-2}=2a(v,-1).
 \tag{RC34}
\]

The right side has every integral Laurent coefficient even; the coefficients of \(v^2\) and \(v^{-2}\) on the left are 1. This contradiction proves RC-A.

The use of the full internal variable occurs only after the global graph-freeness theorem RC30. It does not silently retain grading lost under generic localization.

## 9. Exact consequences and boundaries

1. The former residual nonflat-cohomology case is closed for the ordinary rank-one product reflection realization \(k[x,y]\), for every bounded scalar C of the specified Euler class, and even when the quadratic is required only in the derived bimodule category.

2. A proposed uniform all-ranks lift by bounded ordinary Soergel complexes with scalar quadratic coefficient objects must in particular furnish this rank-one product case. Such a uniform construction is excluded. This statement does not by itself exclude an isolated higher-rank construction with no compatible rank-one restriction; the two-variable module lemma is the dimension-specific input.

3. In the rank-one permutation realization with additional fixed central polynomial variables, an actual homotopy-level quadratic can be reduced termwise by those variables. The standard Soergel terms reduce to the two-variable terms, the specified scalar complex is unchanged, and homotopy inverses and homotopies descend. That reduction is enough to exclude such a homotopy construction. No blanket assertion that an arbitrary underived quotient preserves every derived isomorphism is being used.

4. This is a theorem about ordinary Soergel bimodules, a specified ambient Hecke Euler class, bounded scalar coefficient complexes, and an actual quadratic. It does not exclude the finite-state graded kernel model of F56/F61, a different positive cone, a non-scalar coefficient complex, a localization, or an unbounded enlargement. It makes no claim that all derived categorifications are impossible.

5. The proof uses no finite-field realization, Frobenius, purity, or canonical-basis identification. It strengthens the algebraic operation gate before those additional comparisons are asked for.

## 10. Separate Grothendieck dictionary and source status

The passage from modules over A to coherent sheaves on its affine plane is the affine module/sheaf equivalence in EGA I, Theorem 1.3.7, p. 86, Corollary 1.3.8, p. 87, and Theorem 1.4.1, pp. 90--92. The actual fiber \(\phi(M)\), the Tor groups in RC12--RC15, and the derived tensor quadratic retain information absent from an Euler class. The bounded one-sided free complexes fit the perfect-complex framework of SGA6 I, Definition 4.7, pp. 121--122, and Example 4.8, p. 122; the argument does not declare every cohomology module projective before proving it.

The internal grading is a split-\(\mathbb G_m\) representation convention, anchored in SGA3 I, 4.7.2--3 and the previously audited Montpellier cote 90, scan 17. The nonnegative global multiplicity polynomials in RC31--RC33 are actual effective graded coefficient classes. Passing to virtual K0 is legitimate for RC2--RC3 but does not supply those effective classes; the proof constructs the necessary free graph decomposition before using them. SGA6 V, Sections 2--3 and the previously audited cote 133, scan 18 supply the surrounding lambda/representation K0 vocabulary, with the existing original-scan access qualification for SGA6 V retained. No gamma-filtration positivity or noncommutative lambda-ring structure is asserted.

The ordinary Soergel normalization and split-K0 comparison are the primary Elias--Williamson Hodge-theory source, Section 3.3, p. 1105; Section 3.4, pp. 1106--1107; Section 3.5, Theorem 3.5. The exact generic graph model is the primary Elias--Williamson Localized-calculus source cited at RC5. Those contexts were already read and checked for F59. The two-variable Koszul resolution, tensor-dimension inequality, near-top Künneth argument, descending induction, and final scalar-complex exclusion are proved in full above. They are not attributed to an unpublished Grothendieck manuscript.

## 11. Check record before independent review

The author reread the complete final module/top note at SHA a17597c65917563c101decf9edc8f1323d4d71461f3ebef1e8fb78eb21601858 and reconstructed its torsion-free and torsion-bearing cases, the right origin-module orientation, and the global-top/generic-top comparison. The author independently checked every index in RC23--RC29, both graph-twist origin fibers, the rank-zero-kernel argument, and the separation between one-sided splitting and the canonical bimodule cross-product. The generic calculation uses only ungraded Q-multiplicities; the full v-character is restored only in Section 8.

Fresh whole-proof review of this assembled report is requested from /root and /root/rectangular_and_theta before integration. This file does not change any frozen earlier F59 fragment, the main paper, or a shared master log.

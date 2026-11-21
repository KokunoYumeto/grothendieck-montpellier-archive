# F59 extension: central polynomial coefficients and the remaining two-sided nonflat gate

Author: `/root/rectangular_and_theta`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Inherited reasoning effort is not exposed.

This report tests the specific alternative left outside the bounded scalar-complex theorem. A perfect diagonal coefficient may have polynomial differentials. Such an object is not automatically central for ordinary Soergel convolution. Invariant-descended coefficients do have an explicit coherent central structure. Even for an arbitrary perfect diagonal coefficient, the desired quadratic forces both its cohomology and the generator's cohomology to be nonflat if it is to evade the proved scalar theorem.

The final construction supplies an actual non-scalar central quadratic with the required **coefficient** Euler class, but a different **generator** Euler class. It is a boundary example, not a solution of the designated nonstandard lift. The full nonflat/nonflat case for that designated class remains unresolved here.

## 1. Objects and exact hypotheses

Let k have characteristic zero. Initially put

\[
A=k[x,y],\qquad \deg x=\deg y=2,
\quad s_1(x,y)=(-x,y),\quad s_2(x,y)=(x,-y),
\]

and let

\[
S=A^{\langle s_1,s_2\rangle}=k[x^2,y^2].                 \tag{PC1}
\]

Write `A<e>` for a free module whose displayed generator has internal degree e. This notation avoids changing the ordinary Soergel shift convention. Cohomological shifts have the convention `H^i(K[1])=H^{i+1}(K)`.

The ordinary rank-one-product generators are

\[
B_i=A\otimes_{A^{s_i}}A(1),\qquad b_i=[B_i],
\quad\delta=v+v^{-1}.                                  \tag{PC2}
\]

The previously proved target asks for a bounded ordinary Soergel complex X with termwise Hecke Euler class

\[
[X]=P=b_1b_2+(b_1-\delta)(b_2-\delta).                  \tag{PC3}
\]

A **perfect diagonal coefficient** C means a bounded complex of finite graded free A-modules, regarded as A-bimodules with equal left and right actions. Its differential is homogeneous and A-linear and may have polynomial entries. Its graded Euler class is the alternating Laurent sum of its free terms, in `K0^gr(A)=Z[v,v^-1]`. We require

\[
\chi_v(C)=\delta^2.                                    \tag{PC4}
\]

The proposed quadratic is an actual isomorphism

\[
X\otimes_A^{\mathbf L}X\simeq C\otimes_A^{\mathbf L}X    \tag{PC5}
\]

in the graded derived category of A-bimodules. The necessary conditions below do **not** assume C already has a central half-braiding. Thus they apply in particular to a genuinely central coefficient. A central structure means natural isomorphisms moving C past the ordinary Soergel objects and their maps, satisfying the usual unit and tensor-coherence identities; having diagonal terms alone does not supply these isomorphisms.

## 2. One Koszul coefficient has an exact centrality test

For a nonzero homogeneous polynomial f of positive degree d, define the diagonal two-term complex

\[
K(f)=[A\langle d\rangle\xrightarrow{\ f\ }A],
\quad\text{in cohomological degrees }-1,0.              \tag{PC6}
\]

### Proposition PC-A

For s=s_1, an isomorphism

\[
K(f)\otimes_A^{\mathbf L}B_s
\simeq B_s\otimes_A^{\mathbf L}K(f)                    \tag{PC7}
\]

exists as a graded derived bimodule isomorphism if and only if `s(f)=f`. The corresponding statement holds for s_2. Consequently simultaneous commutation with the two actual generators is equivalent, for this one-polynomial coefficient, to `f in S`.

### Proof

The harmless common shift in B_s can be omitted from the calculation. Its underlying bimodule is the commutative ring

\[
R_s=A\otimes_{A^s}A
\simeq k[x,x',y]/(x^2-x'^2),                           \tag{PC8}
\]

with left x acting by x and right x acting by x'. Both sides of PC7 are computed by ordinary tensor complexes, because B_s is free on either side. Their differentials are multiplication by `f(x,y)` and `f(x',y)`, respectively. Both multiplications are injective: R_s is free over the relevant copy of the domain A. The two complexes therefore have only degree-zero cohomology,

\[
R_s/(f(x,y)),\qquad R_s/(f(x',y)).                      \tag{PC9}
\]

The left and right A-actions generate the ring R_s. Thus any bimodule isomorphism of these cyclic modules is an R_s-module isomorphism and forces equality of their annihilator ideals,

\[
(f(x,y))R_s=(f(x',y))R_s.                              \tag{PC10}
\]

In particular `f(x,y)=a f(x',y)` for some a in R_s. Since both displayed polynomials have degree d and multiplication by `f(x',y)` is injective, the homogeneous decomposition of a shows that a has degree zero. The ring R_s is nonnegatively graded with degree-zero part k, so a is a constant. Restrict to the diagonal quotient `x'=x`; the nonzero polynomial f gives `a=1`. Hence the two polynomials themselves are equal in R_s.

Restricting this equality instead to the graph quotient `x'=-x` gives `f(x,y)=f(-x,y)`, or `s(f)=f`. Conversely, if f is s-invariant, it belongs to A^s, so its two actions on R_s are equal. The two tensor complexes then agree under the standard unit/associativity identification. This proves PC-A. For s_2 the same proof interchanges the roles of x and y. Simultaneous invariance is exactly the ring S in PC1. QED.

The conclusion is limited to the single Koszul complex K(f). It is not a classification of all perfect diagonal complexes with central structures; matrices of differentials can carry additional descent or change-of-basis data.

### Explicit failure despite graph commutation

For f=x, the two modules in PC9 are

\[
k[x',y]/(x'^2),\qquad k[x,y]/(x^2).                    \tag{PC11}
\]

Left x is zero on the first and is a nonzero nilpotent on the second. They are not isomorphic even as ungraded A-bimodules. By contrast, the actual graph module A_s has right x equal to minus left x. The two graph tensor complexes have differentials x and -x and are isomorphic by multiplying the degree-minus-one term by -1. After passage to the fraction field both Koszul complexes are acyclic. Thus neither a graph-level check nor generic localization detects the failure to move K(x) past the actual ordinary Soergel generator.

## 3. Invariant descent gives actual coherent central operations

Let K be any bounded complex of finite graded free S-modules, with S-linear homogeneous differentials. Define

\[
C_K=A\otimes_S K                                      \tag{PC12}
\]

with its diagonal A-action. This is a perfect diagonal coefficient; its differential entries are invariant polynomials. The map S->A is free, with basis `1,x,y,xy`, so ordinary and derived pullback coincide here.

### Proposition PC-B

C_K has a natural coherent central structure on the ordinary rank-one-product Soergel category and its bounded homotopy category. It moves past every object and every morphism by actual chain isomorphisms, even when its cohomology is nonflat.

### Proof

Every element of S has the same left and right action on B_i because `S subset A^{s_i}` in the balanced tensor defining B_i. This equality is preserved by tensor products, direct sums, shifts, direct summands and bimodule morphisms. It consequently holds termwise and compatibly with the differential on every bounded ordinary Soergel complex X.

There are natural identifications

\[
C_K\otimes_A X\simeq K\otimes_S X,
\qquad
X\otimes_A C_K\simeq X\otimes_S K.                    \tag{PC13}
\]

For example `(a tensor k) tensor x` maps to `k tensor a x` in the first identification. The balanced relations use precisely the equal S-actions. The ordinary symmetry for complexes of S-modules, with its cohomological Koszul sign, identifies the two right sides. Equivalently, a homogeneous tensor `k tensor x` of cohomological degrees p,q maps to `(-1)^(pq) x tensor k`.

These maps are A-bimodule-linear because the coefficient factor is diagonal and S acts centrally on X. They commute with all differentials and all ordinary Soergel maps. For an iterated product, they move the labeled coefficient factor through the same ordered list of factors; the Koszul signs add in the usual way. Thus the unit and half-braiding tensor identities follow from the standard associativity and symmetry identities for complexes of S-modules. This proves actual coherent movement, not only equality of Euler classes. QED.

The same construction works for any standard ordinary type-A product realization with S=A^W. The proof uses the equality of the full invariant action on every ordinary Soergel generator, not an unproved centrality statement about arbitrary polynomial differential matrices.

## 4. Flat coefficient cohomology reduces to the already proved scalar theorem

### Proposition PC-C

In every ordinary type-A ambient ring covered by the all-rank F59 theorem, a perfect diagonal C satisfying PC4--PC5 cannot have all cohomology modules flat over A.

### Proof

A finite graded flat module over the polynomial ring A is finitely presented and projective; the known equivalence is Stacks Lemma10.78.2, tag00NX, parts(1)--(3), whose statement and proof I opened and read at https://stacks.math.columbia.edu/tag/00NX. It is graded free: lift a homogeneous basis at the homogeneous origin to a finite free surjection, split by projectivity, and use graded Nakayama on the complementary kernel. If ordinary projectivity was first obtained, the degree-zero component of a splitting is a graded splitting.

Consequently every `H^j(C)` is a finite sum of shifts of A. The usual successive projective-cohomology splitting of a bounded perfect complex gives an isomorphism, already in the graded derived category of A-modules,

\[
C\simeq\bigoplus_j H^j(C)[-j]
\simeq C_{\mathrm{sc}}\otimes_k A,                     \tag{PC14}
\]

where C_sc is a bounded finite internally graded scalar complex with zero differential. All objects and all chosen maps have diagonal A-actions, so these A-linear splittings and homotopies are also bimodule-linear. Their Euler class gives `chi_v(C_sc)=delta^2`. Substituting PC14 into PC5 produces exactly the bounded scalar quadratic already excluded by the all-rank F59 theorem. A possibly different central structure on C is irrelevant to that derived tensor isomorphism. QED.

## 5. Flat generator cohomology forces flat coefficient cohomology

### Proposition PC-D

Assume PC3--PC5 in a standard ordinary type-A product realization. If every `H^i(X)` is flat as a left A-module, then every `H^j(C)` is graded free as an A-module. Thus PC3--PC5 are impossible in this case too, for an arbitrary perfect diagonal coefficient. No flatness of C is assumed in this implication.

### Proof

Let Q be the ungraded fraction field. Since C is diagonal, its localization is an ordinary scalar complex of finite Q-vector spaces. Write

\[
d(u)=\sum_j\dim_Q H^j(C_Q)u^j,
\qquad
F(u)=\sum_{g\in W}f_g(u)g
\]

for the actual generic cohomological multiplicities of C and X. Their Euler classes give `d(-1)=4`, `F(-1)=2(e+tau)`, with `tau=(s,s)`. The actual localized quadratic gives `F^2=dF`. The positive idempotent-probability argument proved in the assembled all-rank F59 report therefore gives

\[
F(u)=\frac{d(u)}2(e+\tau).                              \tag{PC15}
\]

This is only an ungraded-fraction-field statement. In particular every generic cohomology module of X has graph support contained in e and tau. The assumed flat finite graded cohomology modules are graded free on the left. The checked codimension-two graph lemma therefore splits each globally as a finite sum of shifted A_e and A_tau. In the actual ambient coordinates, tau negates two independent root variables and fixes the other variables; the proof uses `yU=xV`, `U^2=x^2`, coprimality and the two involution idempotents. Thus every `M_i=H^i(X)` is also right-free.

The canonical cycle cross-product is now an isomorphism in every degree of the tensor square:

\[
H^t(X\otimes_A^{\mathbf L}X)
\simeq\bigoplus_{i+h=t}M_i\otimes_A M_h.                \tag{PC16}
\]

This is the same one-sided projective-cohomology argument already checked for F59. Each term on the right is a free graph module, so the left side is a graded free **left** A-module in every degree.

For the other side of PC5, forget only the **right** action on the second factor X. Its projective left cohomology can be split off in the category of left A-module complexes. Since every M_i is flat on the left, tensoring this one-sided decomposition with the right A-complex C computes the derived tensor correctly, without a flatness assumption on `H^j(C)`. Equivalently the canonical cycle cross-product is bijective, and gives an actual left-module isomorphism

\[
H^t(C\otimes_A^{\mathbf L}X)
\simeq\bigoplus_{j+i=t}H^j(C)\otimes_A M_i.             \tag{PC17}
\]

To make the A-linearity explicit, the surviving left action on this tensor product is the left action on C; it commutes with every right-A-linear operation on C and every chosen left-linear map in the second factor. The canonical cross-product is in fact a bimodule map, but only its left-module isomorphism is needed. No splitting of X as a bimodule complex is asserted.

There is some nonzero M_i, since the generic Euler class of X is nonzero. Fix such an index i_0. Each M_i is a direct sum of graph modules. For diagonal `N=H^j(C)`, tensoring N on the right with a graph A_g changes only its right action and its shift; as a left module it is N with that shift. Therefore, in degree `t=j+i_0`, the direct sum in PC17 contains at least one shifted copy of `H^j(C)` as a direct summand.

The actual quadratic identifies PC17 with the graded free left module PC16. A direct summand of a free left module is projective; its finite graded version is graded free by the origin-basis argument in PC-C. Thus every `H^j(C)` is graded free. Proposition PC-C gives the contradiction. This proves PC-D with all derived-tensor hypotheses accounted for. QED.

### Concrete consequence and exact remaining gate

The explicit coupled Rouquier object from the earlier F59 report,

\[
X_{\rm R}\simeq A_e^{\oplus2}\oplus A_\tau(-2)
                    \oplus A_\tau(2),                 \tag{PC18}
\]

is in particular excluded for **every** perfect diagonal C with the required Euler class, not only scalar coefficients. More generally a successful remaining construction under PC3--PC5 would have to give both X and C some nonflat cohomology. It must also supply the central movement if that operation is required; diagonal terms do not provide it by definition.

## 6. A genuine central non-scalar quadratic at a different Euler class

The preceding obstruction does not imply that invariant polynomial coefficients can never occur in a bounded ordinary quadratic. The following explicit construction shows the exact ambient-class boundary.

In S, let q=x^2, of internal degree four, and put

\[
K_S(q)=[S\langle4\rangle\xrightarrow{\ q\ }S],
\qquad
U_S=S\oplus K_S(q)\oplus K_S(q)[1].                    \tag{PC19}
\]

Then `chi_v(U_S)=1`: the two Koszul Euler classes cancel. Its cohomology is

\[
H^0(U_S)=S\oplus S/(q),\qquad
H^{-1}(U_S)=S/(q),                                     \tag{PC20}
\]

and all other cohomology vanishes. Let `U=A tensor_S U_S`. Its torsion cohomology is the nonzero A-module `A/(x^2)`, so it is not a scalar complex in the sense of the proved theorem. Proposition PC-B supplies its coherent central structure.

Let `B=B_1 tensor_A B_2`, and let D_sc be the finite graded scalar space of character `delta^2`, viewed as a degree-zero coefficient. Define

\[
X'=U\otimes_A B,
\qquad
C'=D_{\rm sc}\otimes_k U.                              \tag{PC21}
\]

Both are bounded complexes with finite ordinary terms; X' is an ordinary Soergel complex and C' is a perfect diagonal coefficient descended from S. Its maps have invariant polynomial entries. The ordinary rank-one decompositions give the actual isomorphism

\[
B\otimes_A B\simeq D_{\rm sc}\otimes_k B.              \tag{PC22}
\]

For completeness, each ordinary reflection bimodule squares to the two shifted copies encoded by delta, because A is free over A^{s_i} on the basis `1` and the corresponding root. The two independent factors commute, so their product has the coefficient delta squared. This is the already audited ordinary Soergel normalization of Elias--Williamson, Sections3.3--3.4, pp1105--1107.

Using the actual coherent central movement of U, PC22 yields

\[
\begin{aligned}
X'\otimes_A X'
&\simeq U\otimes_A U\otimes_A(B\otimes_A B)\\
&\simeq D_{\rm sc}\otimes_k U\otimes_A U\otimes_A B\\
&=C'\otimes_A X'.                                     \tag{PC23}
\end{aligned}
\]

These are chain/homotopy-level tensor isomorphisms, not an inference from their characters. All factors are bounded with one-sided free terms, so they also give the derived isomorphism. Their central comparisons are those of PC-B; no strict identity between unlabelled different orders of extracted coefficient factors is claimed.

The Euler classes are

\[
\chi_v(C')=\delta^2,
\qquad [X']=b_1b_2.                                    \tag{PC24}
\]

The second class is **not** the target P. This can already be seen after forgetting internal shifts: it is `e+s_1+s_2+tau`, whereas P gives `2e+2tau`. The construction therefore realizes a genuine central non-scalar quadratic with the same coefficient Euler class but not the designated nonstandard generator class. Both C' and X' have nonflat cohomology, consistent with PC-C/PC-D once the latter's target-class hypothesis is retained.

## 7. What the tested route does not yet decide

The full nonflat/nonflat alternative for the target P is not settled by these arguments. In particular one cannot simply specialize invariant parameters at the origin and reuse the all-variable scalar theorem: the resulting ambient algebra is a coinvariant quotient, not the regular polynomial ring used in its Tor lemma. Moreover the coefficient complex can acquire additional torsion cohomology or larger origin fibers, so its highest global cohomological degree need not be its highest generic degree.

This is the exact failure in the prior top-degree proof. For a scalar coefficient, its highest cohomology survives generically; global and generic top comparisons then force the top module of X to have positive rank and the correct scalar multiplicity. For an invariant-descended perfect coefficient with nonflat cohomology, an additional torsion top may vanish generically. The global and generic top equations no longer identify those two degrees. The new arguments above exclude flatness on either side, but they do not supply the missing identification in the remaining case.

The natural singular invariant correspondence `A tensor_{A^tau} A` is still nonflat and is not silently promoted to a derived groupoid or a scalar central coefficient. Ordinary tensor reassociations of that correspondence do not prove a derived quadratic: nonflat derived intersections retain Tor. No such unverified derived comparison is used here.

## 8. Separate Grothendieck dictionary and check record

The diagonal module, ordinary reflection correspondence and the two annihilator ideals in PC8--PC10 are actual affine module data. EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92 give their coherent sheaf dictionary. In that language PC-A distinguishes two pullbacks to the same ramified correspondence; equality on its generic graph pieces does not identify the whole pullbacks. Proposition PC-B is an explicit derived pullback from the invariant affine quotient with its genuine commuting action, proved directly through the balanced tensor formulas.

Bounded perfect diagonal complexes and derived tensor belong to SGA6 I Definition4.7 pp121--122 and Example4.8 p122. The cohomology freeness implication keeps the actual canonical Künneth maps and projective direct summands; it does not replace them by an Euler equality. The internal grading and effective versus virtual coefficient conventions are SGA3 I4.7.2--3/cote90 scan17 and SGA6 V Sections2--3/cote133 scan18, with the already recorded source-access qualification. No lambda-ring is assigned to the noncommutative word algebra.

The ordinary reflection relation and graph localization use the exact primary Elias--Williamson contexts already audited for F59: Hodge theory Sections3.3--3.5, pp1105--1108; Localized calculus Sections1.1--1.2, equations1.1--1.2, Theorem1.6 and Remark1.7. The all-rank scalar exclusion used in PC-C is the fully written new deduction in `agent_soergel_allrank_scalar_closure.md`, SHA475bd56d0486831328193453faec89612ea1c97a8bb81786d12970053eb34f27, with its explicitly cited Lichtenbaum input. None of these framework sources is claimed to prove the new polynomial-coefficient statements.

I reconstructed the principal-annihilator argument, the regularity of both polynomial actions on B_s, the diagonal versus reflection-graph restrictions, the signs in the central chain symmetry, and all termwise Euler classes. I checked PC17 by splitting only the left-module complex in the second tensor factor; no flatness of C or bimodule formality is invoked. I checked that the explicit example's torsion survives flat pullback from S and that its generator Euler class is deliberately different. Fresh full review is requested from root and groth before integration. No master file or shared event log was edited.

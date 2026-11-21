# F59 supplement — coupled graph support, left flatness, and the nonreflection invariant ring

Author: /root/rectangular_and_theta, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This note continues the actual coupled-complex test after the checked core report agent_soergel_derived_gate.md. It proves a complete obstruction for coupled objects quasi-isomorphic to a graded left-flat module with the required generic support, and computes the failure of the natural invariant-ring candidate. It does not exclude every bounded coupled Soergel complex: nonflat cohomology remains a precise residual possibility.

## 1. Setup and the remaining generic requirement

Let k have characteristic zero, and put

\[
R=k[x,y,z_1,\ldots,z_m],\qquad \deg x=\deg y=\deg z_i=2,
\]

where m≥0. Let τ fix each z_i and send x,y to −x,−y. The two anti-invariant coordinates are the roots of the two independent copies of a simple reflection. Thus this is the actual local coordinate form of τ=(s,s) in the product of two ordinary reflection realizations, with the remaining coordinates fixed.

Write Q=Frac(R), and write R_e,R_τ for the graph bimodules: their left module is R, and their right action is multiplication by r and τ(r), respectively. Internal shifts use M(j)^d=M^(d+j). Let

\[
\mathscr D=R(2)\oplus R^{\oplus2}\oplus R(-2),
\qquad D(v)=v^2+2+v^{-2}=(v+v^{-1})^2.
\tag{CF1}
\]

The actual requested quadratic is

\[
X\otimes_R X\simeq\mathscr D\otimes_R X
\tag{CF2}
\]

in the bounded homotopy category of Soergel bimodules, hence also after passing to the ordinary derived category of graded bimodules. The tensor product in that derived category is derived unless flatness has been established.

The core report proves that any bounded lift of the actual nonstandard Euler class P which satisfies CF2 must, after generic localization and forgetting internal grading, have

\[
H^i(X_Q)=0\ (i\ne0),\qquad
H^0(X_Q)\simeq Q_e^{\oplus2}\oplus Q_\tau^{\oplus2}.
\tag{CF3}
\]

That condition is consistent in the generic graph category; this note tests its descent.

## 2. Coprimality splits every graded left-free module with this support

**Proposition CF-A.** Let M be a finitely generated graded R-bimodule which is free as a graded left R-module. Assume that its generic localization is a direct sum of Q_e and Q_τ graph modules. Then there are uniquely determined finite Laurent polynomials

\[
a(v),b(v)\in\mathbb N[v,v^{-1}]
\]

such that

\[
M\simeq R_e^{\oplus a(v)}\oplus R_\tau^{\oplus b(v)}
\tag{CF4}
\]

as graded bimodules. Here the notation means a direct sum of the indicated internal shifts. In particular M is also free on the right.

### Proof

In a homogeneous left basis, let A and B be the matrices of right multiplication by x and y. The generic graph assumption gives

\[
yA=xB,\qquad A^2=x^2I
\tag{CF5}
\]

over Q. Since M is left-free, these matrix identities hold over R.

The polynomials x and y are relatively prime. Each entry of yA=xB implies that x divides the corresponding entry of A. Thus A=xZ for a matrix Z over R; then B=yZ. The second identity in CF5 gives Z²=I. Right multiplication by every z_i is z_i I, again because that equality holds generically and M is torsion-free on the left.

The operator Z has internal degree zero: right multiplication by x and left multiplication by x both have degree two, and x is a non-zero-divisor. Therefore

\[
e_+=\frac{I+Z}{2},\qquad e_-=\frac{I-Z}{2}
\tag{CF6}
\]

are homogeneous degree-zero bimodule idempotents. They split M into finitely generated graded projective left modules M_+ and M_-.

On M_+, right multiplication by x,y,z_i agrees with left multiplication. On M_-, it agrees with τ. Thus these summands are graph modules tensored with their respective graded multiplicity modules.

For completeness, these graded projective modules are graded-free; no appeal to the ungraded Quillen–Suslin theorem is needed. If P is a finite graded direct summand of a finite graded free R-module, choose a homogeneous k-basis of P/R_+P and lift it to P. Graded Nakayama gives a surjection from a finite direct sum of shifts of R onto P. It splits in the graded category, since P was a graded direct summand of a graded free module. The complementary kernel has zero quotient by R_+ and hence is zero by graded Nakayama. This gives the required graded-free decomposition.

The multiplicities of the shifts are uniquely determined by the graded dimension after tensoring with R/R_+, so their characters a(v),b(v) are well-defined. Equation CF4 follows. ∎

This proof uses two relatively prime anti-invariant coordinates. A single reflection has only one such coordinate; its ordinary Bott–Samelson bimodule is a left-free nonsplit gluing of its two generic graphs. The codimension-two diagonal involution is precisely where the coprimality argument becomes available.

## 3. Complete quadratic classification in the left-free support case

**Proposition CF-B.** Under the hypotheses of CF-A, the quadratic

\[
M\otimes_R M\simeq\mathscr D\otimes_R M
\tag{CF7}
\]

holds if and only if M=0 or M≅\mathscr D with the identity graph action. In particular no such M with a nonzero τ graph component can satisfy it.

### Proof

The graph multiplication rules are

\[
R_e\otimes_R R_e\simeq R_e,\qquad
R_e\otimes_R R_\tau\simeq R_\tau
\simeq R_\tau\otimes_R R_e,\qquad
R_\tau\otimes_R R_\tau\simeq R_e.
\]

They preserve internal shifts. The two graph components cannot be mixed by an isomorphism: a map R_e→R_τ, or conversely, is killed by 2x in the domain R and is therefore zero. The same holds for all internal shifts and their finite direct sums.

Writing M as CF4, comparison of the two graded free graph ranks in CF7 gives

\[
a(v)^2+b(v)^2=D(v)a(v),\qquad
2a(v)b(v)=D(v)b(v).
\tag{CF8}
\]

If b≠0, the integral-domain property of Z[v,v^-1] gives

\[
2a(v)=v^2+2+v^{-2}.
\tag{CF9}
\]

This is impossible: the coefficients of v² and v^-2 on the right are odd, whereas every coefficient on the left is even. Hence b=0. The first equation then gives a(a−D)=0, so a=0 or a=D. Both stated objects really satisfy the quadratic, which proves the classification. ∎

**Corollary CF-C.** No bounded Soergel lift of the actual nonstandard P, satisfying the actual quadratic, can be quasi-isomorphic in the derived category of graded bimodules to a module that is finite graded-free on the left.

Indeed CF3 requires a nonzero τ component, whereas CF-B forbids it. If the object is quasi-isomorphic to M, CF-A makes M flat on both sides, so its derived tensor square is its ordinary tensor square. Any homotopy quadratic would give the derived module quadratic CF7.

The same conclusion holds if all the cohomology modules of X are graded left-flat. Finite graded left-flat modules over R are graded projective and hence graded-free. By CF3, each H^i(X) for i≠0 then vanishes: a free module with zero generic localization is zero. Thus X is quasi-isomorphic to its left-free H^0, contradicting CF-C.

This leaves a precise necessary condition on any remaining bounded coupled lift: it must have nonflat cohomology. More explicitly, either some nonzero H^i(X), i≠0, is torsion on the left, or H^0(X) is not left-flat. Having flat Soergel terms does not imply flat cohomology, so this is a genuine remaining case, not a contradiction obtained by conflating terms and cohomology.

The coupled Rouquier example in the core report lies in the excluded left-free case. Its decomposition has a(v)=2 and b(v)=v²+v^-2. Proposition CF-B proves that every possible left-free distribution fails, not only that particular distribution.

## 4. The natural diagonal-invariant candidate

Put

\[
S=R^\tau=k[z_1,\ldots,z_m,x^2,xy,y^2].
\tag{CF10}
\]

The indicated generators give the full invariant ring because a monomial in x,y is invariant exactly when its total x,y degree is even. Writing a=x²,b=xy,c=y² gives the familiar relation ac=b²; no smoothness or freeness is assumed for S.

The natural two-graph correspondence is

\[
T=R\otimes_S R.
\tag{CF11}
\]

Its generic localization is Q_e⊕Q_τ. For example Frac(R) is the quadratic extension Frac(S)(x), with y=(xy/x²)x; the nontrivial automorphism is τ. The elementary quadratic Galois splitting then gives the two graphs. Thus T is a genuine candidate for the desired diagonal support, rather than an invented unrelated dimension count.

However, R is not free over S at the invariant origin. Let

\[
\mathfrak n=(z_1,\ldots,z_m,x^2,xy,y^2)\subset S.
\]

The generic S-rank of R is two, whereas

\[
R/\mathfrak nR
\simeq k[x,y]/(x^2,xy,y^2)
\tag{CF12}
\]

has k-dimension three, with basis 1,x,y. Local freeness of rank two would force a two-dimensional fiber. This proves the failure of the reflection-type freeness property directly.

Likewise T is not free as a left R-module: it has generic rank two but a three-dimensional fiber at the left origin.

### An explicit torsion calculation

The failure is sharper than a rank/fiber discrepancy. Decompose R as S⊕M into τ-even and τ-odd parts. The odd module M is generated over S by x and y, and its relations are generated by

\[
(xy,-x^2),\qquad(y^2,-xy).
\tag{CF13}
\]

To verify completeness, any relation p x+q y=0 with p,q∈S gives p=yh,q=−xh by coprimality. The parity condition makes h odd, so h=xu+yw with u,w∈S; this expresses the relation as the indicated combination.

After tensoring with the left copy of R,

\[
T\simeq R\oplus
\frac{Ru\oplus Rv}{(x\omega,y\omega)},
\qquad
\omega=yu-xv,
\tag{CF14}
\]

where u,v are the images of the odd right generators x,y. Their internal degrees are two, and ω has degree four. The class of ω is nonzero: ω belonging to (x,y)Rω would force 1∈(x,y). Its annihilator is exactly (x,y). Thus T has a nonzero left torsion submodule isomorphic to R/(x,y), placed in internal degree four.

The map u↦x,v↦y gives the exact sequence

\[
0\longrightarrow (R/(x,y))\cdot\omega
\longrightarrow
\frac{Ru\oplus Rv}{(x\omega,y\omega)}
\longrightarrow (x,y)\longrightarrow0.
\tag{CF15}
\]

This records the codimension-two defect explicitly. It is not inferred merely from the singularity of the invariant quotient.

## 5. The invariant correspondence fails the actual quadratic, even derived

Allow an arbitrary nonzero finite internally graded coefficient space U and put

\[
X_U=U\otimes_k T,\qquad r=\dim_k U>0.
\]

This includes every finite collection of internal shifts and multiplicities of the natural correspondence. A scalar shift is included in U.

**Proposition CF-D.** There is no isomorphism

\[
X_U\otimes_R^{L}X_U\simeq\mathscr D\otimes_R X_U
\tag{CF16}
\]

in the derived category of graded R-bimodules.

### Proof

If CF16 held, its degree-zero cohomology would give an ordinary module isomorphism

\[
X_U\otimes_R X_U\simeq\mathscr D\otimes_R X_U.
\tag{CF17}
\]

This implication uses only the general identity H^0(M⊗_R^L N)=M⊗_R N for modules in degree zero. It does not suppose T is flat or discard higher Tor groups.

Take the left fiber at the homogeneous origin of R and forget the internal grading. Let

\[
B=k\otimes_S R
=k[x,y]/(x^2,xy,y^2),
\qquad\dim_k B=3.
\]

Associativity of ordinary tensor products gives

\[
k\otimes_R(T\otimes_R T)
\simeq k\otimes_S R\otimes_S R
\simeq B\otimes_k B,
\tag{CF18}
\]

because the S-action on B factors through the residue field k. This fiber has dimension nine.

The two sides of CF17 would therefore have fiber dimensions

\[
9r^2\qquad\text{and}\qquad4\cdot3r=12r.
\tag{CF19}
\]

Equality would force r=4/3, impossible for a positive integer. This proves the proposition. ∎

The generic rank comparison independently shows why a lift of P would have needed r=2: T has generic graph ranks (1,1), while CF3 requires (2,2). For that required multiplicity the concrete origin comparison is 36≠24.

The argument also handles a bounded complex of finite internally graded coefficient spaces in place of U. Generic localization of a putative quadratic forces that coefficient complex to have cohomology only in degree zero, by the generic-amplitude lemma. Over k it is then quasi-isomorphic to its finite-dimensional H^0, reducing to the case just proved.

This is a direct failed quadratic computation for the natural invariant correspondence. It is not an assertion that every coupled complex supported on the same union is a scalar multiple of T.

## 6. Exact remaining gate

The two successful exclusions have different hypotheses:

- CF-B excludes every coupled lift quasi-isomorphic to a finite graded left-flat bimodule with the required two-graph support.
- CF-D excludes the natural nonflat correspondence R⊗_(R^τ)R, including all finite graded multiplicities and all bounded scalar coefficient complexes.

A remaining bounded coupled Soergel complex would have to use genuinely nonflat cohomology beyond this simple invariant correspondence, while becoming exactly Q_e²⊕Q_τ² in degree zero after generic localization and satisfying the full categorical quadratic. Higher nonstandard relations and their coherence would still need to be supplied afterward.

No proof here excludes every such residual complex. In particular a quasi-isomorphism in the ordinary derived bimodule category is weaker than a homotopy isomorphism of Soergel complexes; a construction in the former would still have to be lifted to the latter. The obstructions above are valid because a homotopy quadratic necessarily implies the derived quadratic which is ruled out in their respective cases.

## 7. Separate Grothendieck dictionary and source status

The ordinary graph bimodules and their tensor products are the standard affine-correspondence model. The exact original source locators, read in the core review, are:

- Elias–Williamson, Hodge theory of Soergel bimodules, §3.3 p1105 and §3.4 pp1106–1107 for grading, R⊗_(R^s)R(1), and its free rank-two basis; §3.5 pp1107–1108 for the Hecke Grothendieck comparison.
- Elias–Williamson, Localized calculus for the Hecke category, §1.1 pp3–4, Theorem1.6/Remark1.7 pp4–5, and §2.1 equations2.1–2.6 p7 for the faithful graph category and localization.
- Rouquier, Categorification of the braid groups, §§3.1.2–3.2.1 p6, §3.2.4 p9 and §3.3.1 p10 for graph bimodules and the actual complexes.

The new coprimality and fiber proofs above are supplied in full and are not attributed to those sources.

In EGA language, a left-free bimodule gives a sheaf on Spec R×Spec R whose pushforward along the first projection is a vector bundle. Its generic support is the union of the identity and τ graphs. Proposition CF-A proves, in this specific codimension-two setting, that the bundle condition forces a global splitting into the two graph pieces. This uses the actual coordinate equations and does not assert such a splitting for arbitrary coherent sheaves.

The invariant candidate is the structure sheaf of

\[
\operatorname{Spec}R
\times_{\operatorname{Spec}S}
\operatorname{Spec}R.
\]

The two generic graphs do not make this correspondence a finite flat double cover on the entire parameter space. The explicitly computed three-dimensional fiber and torsion record its failure. The affine module/sheaf dictionary is EGA I Theorem1.3.7 p86, Corollary1.3.8 p87, and Theorem1.4.1 pp90–92. Tensor products of affine correspondences correspond to the displayed module tensor products; derived tensoring retains possible Tor terms rather than assuming them away.

Internal shifts and their multiplicities use the torus-action and effective-character vocabulary of SGA3 I4.7.2–3/cote90 scan17 and SGA6 V §§2–3/cote133 scan18. The contradiction 2a=D is an integral effective-multiplicity statement; it is not a numerical nonnegativity theorem or a λ-ring assertion for the noncommutative category. The bounded-complex framework is SGA6 I Definition4.7 pp121–122 and Example4.8 p122, always with the relevant tensor base specified.

No main paper or master event file was edited. Independent whole-proof review is requested before integration.


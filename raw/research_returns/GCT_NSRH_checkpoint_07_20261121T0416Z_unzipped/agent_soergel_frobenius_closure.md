# F59 strengthening: finite coinvariant fibers close the bounded coupled-complex case

Author: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC. This is a new categorical obstruction proved below. The elementary verification of the usual type-A coinvariant algebra is a known background fact, included to make every hypothesis of the new argument explicit. It is not claimed as a new invariant-theory theorem.

The checked core report `agent_soergel_derived_gate.md` excludes direct-sum lifts and identifies the necessary generic graph support. Theta's `agent_soergel_coupled_support.md` proves the codimension-two splitting and its left-free quadratic obstruction. The present argument proves that an arbitrary bounded ordinary type-A Soergel candidate satisfying the quadratic must fall into that excluded left-free case. Thus it supersedes the earlier residual nonflat-cohomology possibility in this precise category. It does not assert a no-go in an arbitrary derived category or for an altered coefficient object.

## 1. A finite Frobenius specialization lemma

Let A be a connected nonnegatively graded commutative polynomial k-algebra, with A_0=k. Let I be a homogeneous ideal contained in A_+, and assume

\[
B=A/I
\tag{FC1}
\]

is a finite-dimensional commutative local graded Frobenius k-algebra. Thus there is a homogeneous k-linear functional tau:B→k such that tau(ab) is a nondegenerate pairing. The functional may have a nonzero internal degree. This does not change its cohomological exactness.

Let X be a bounded complex of graded A-bimodules, each finite graded-free as a left and as a right A-module. Suppose I has a set of homogeneous generators each of which acts in the same way from the left and the right on every term. In particular `IM=MI` for each term M: move a central generator to the other side and use the bimodule action on its arbitrary A-coefficient. It is not necessary, and in general not true, that every element of the ideal I itself acts centrally. Put

\[
\mathscr D_A=A(2)\oplus A^{\oplus2}\oplus A(-2).
\tag{FC2}
\]

Assume there is an isomorphism in the homotopy category of graded bimodule complexes

\[
X\otimes_A X\simeq\mathscr D_A\otimes_A X,
\tag{FC3}
\]

and that the Euler characteristic of the left ranks of X is nonzero.

**Theorem FC-A.** Under these hypotheses X has cohomology only in degree zero, and H^0(X) is finite graded-free as a left A-module. The same is true on the right if desired. The cohomology and freeness assertions concern the ordinary derived module category. No assertion that a bimodule homotopy splitting exists is used or needed.

### 1.1. Central quotient preserves the actual relation

Put Z=X/IX termwise. The equalities `IX^i=X^iI` identify this both with the left and with the right quotient, so its terms are finite free on both sides over B. For any two such terms M,N, the natural balanced map gives

\[
(M/IM)\otimes_B(N/IN)
\simeq(M\otimes_A N)/I(M\otimes_A N).
\tag{FC4}
\]

Indeed both sides are the quotient of M tensor_k N by the A-balancing relations and by I in either factor; the equalities `IM=MI`, `IN=NI` identify those latter relations. The same formula, with the usual total-complex signs, applies to complexes. Quotienting is an additive functor and therefore preserves chain homotopies. Consequently FC3 gives a homotopy isomorphism

\[
Z\otimes_B Z\simeq\mathscr D_B\otimes_B Z,
\qquad \mathscr D_B=B(2)\oplus B^{\oplus2}\oplus B(-2).
\tag{FC5}
\]

No flatness of A over an invariant subring, no cohomology-and-base-change theorem, and no replacement of a homotopy isomorphism by an Euler identity is required in this step. All terms in Z are B-free on either side, so its ordinary tensor complex computes its derived tensor product.

The reduced complex has nonzero cohomology. After forgetting the internal grading,

\[
\chi_k(Z)=\dim_k(B)\sum_i(-1)^i\operatorname{rank}_A(X^i)\ne0.
\tag{FC6}
\]

This verifies the needed nonvanishing in the derived category, rather than just nonvanishing of a homotopy class.

### 1.2. The upper cohomological bound

For any nonzero finite right B-module M and nonzero finite left B-module N,

\[
M\otimes_B N\ne0.
\tag{FC7}
\]

To see this, reduce the tensor product modulo the maximal ideal m of the commutative local algebra B. Its reduction is `(M/Mm) tensor_(B/m) (N/mN)`, and both factors are nonzero by Nakayama. This argument concerns the indicated right and left actions; they need not agree with the other bimodule actions.

Let r be the greatest degree with H^r(Z) nonzero. For bounded-above complexes of modules, the highest-degree part of a derived tensor product satisfies

\[
H^{2r}(Z\otimes_B^L Z)
\simeq H^r(Z)\otimes_B H^r(Z).
\tag{FC8}
\]

One can verify FC8 by applying the usual truncation triangles to each factor: every piece below degree r contributes only below degree2r, while tensoring the two top modules contributes its ordinary tensor product in degree2r and Tor only in lower degrees. Formula FC7 makes FC8 nonzero, and there is no higher cohomology. The right side of FC5 has highest degree r, since mathscr D_B is concentrated in cohomological degree zero. Therefore `2r=r`, and r=0.

### 1.3. Duality supplies the lower bound

Use the graded bimodule dual

\[
Z^\vee=\underline{\operatorname{Hom}}_{-B}(Z,B),
\tag{FC9}
\]

with the usual dual-complex differential. The underline denotes the object of maps of all internal degrees, not just its degree-zero Hom space. Because B is commutative Frobenius, the functional tau identifies this dual with the k-linear dual of Z, up to one fixed internal shift. Explicitly, a right-linear map phi maps to `tau circ phi`; the inverse is determined by `tau(phi(m)b)=psi(mb)` for every b. Nondegeneracy of the Frobenius form proves existence and uniqueness. This identification interchanges the two bimodule actions.

In particular, this dual is exact on finite modules and detects nonzero modules, its terms remain free on both sides, and

\[
H^i(Z^\vee)\simeq
\underline{\operatorname{Hom}}_{-B}(H^{-i}Z,B).
\tag{FC10}
\]

Finite projectivity supplies the usual tensor-dual isomorphism

\[
(Z\otimes_B Z)^\vee\simeq Z^\vee\otimes_B Z^\vee,
\tag{FC11}
\]

with the order reversed; both factors here are the same. For completeness this is the finite-dual-basis tensor-Hom isomorphism on each term, extended to total complexes with its usual Koszul signs. It is the duality of the category of bimodules finite projective on both sides, not a claimed symmetry of that category. The coefficient object is self-dual: the two shifts2 and−2 exchange and the two zero shifts remain. Dualizing FC5 therefore gives the same quadratic for Z^vee, with mathscr D_B commuting as a direct sum of shifted units. Applying the upper-bound argument to Z^vee gives its largest cohomology degree zero. By FC10, the smallest cohomology degree of Z is zero. Together with Section1.2, Z has cohomology only in degree zero.

### 1.4. Projectivity at the fiber, then minimality over A

H^0(Z) has finite projective dimension as a left B-module: Z is a bounded complex of finite free left modules with only that cohomology. This can be seen by splitting off the positive-degree acyclic tail from its top, then reading the remaining finite projective resolution. A Frobenius algebra is self-injective: the regular module identifies with the k-linear dual of the regular module, which is injective because `Hom_B(-,D_k B)=D_k(-)` is exact. Consequently a finite projective resolution of H^0(Z) splits from its left end, since its initial projective term is injective; inductively H^0(Z) is projective. The same reasoning holds in the graded category with shifts, or after forgetting grading followed by the graded splitting.

Now forget only the right A-action of X. A bounded graded free complex over the connected graded ring A can be made minimal by repeatedly canceling a nonzero constant matrix entry of a differential. Each such entry is a homogeneous unit and gives a two-term contractible summand after graded row and column operations. The process terminates because each cancellation removes two generators. Denote the resulting left-module complex by F; every differential entry lies in A_+.

The left-module homotopy equivalence `F≃X` descends under quotient to `F/IF≃Z`. The reduced F is a minimal left B-free complex, because every differential entry lies in B_+, which is the maximal ideal of this finite connected graded algebra. Since Z has projective H^0 and no other cohomology, it is homotopy equivalent as a left B-complex to that projective module in degree zero. All bounded acyclic projective tails split; no bimodule splitting is asserted.

Tensor this last left-module homotopy equivalence with B/B_+. The differentials of F/IF become zero. Its degree-i term is a vector space of dimension rank_A F^i. A complex with zero differential can be homotopy equivalent to a degree-zero vector space only if its terms outside degree zero vanish. Hence F^i=0 for i≠0. Thus X has only H^0, and it is the finite graded-free left module F^0. This proves FC-A. ∎

## 2. The type-A central fiber, verified elementarily

Let `R_n=k[x_1,...,x_n]`, with degree x_i=2, and let the symmetric group permute the variables. Let e_j be the elementary symmetric polynomial of ordinary degree j, and put

\[
I_n=(e_1,\ldots,e_n),\qquad B_n=R_n/I_n.
\tag{FC12}
\]

Each e_j acts centrally on every ordinary type-A Soergel bimodule: on a generator `R_n tensor_(R_n^s) R_n(1)`, e_j lies in R_n^s, so it can be moved from the left factor to the right factor. Tensor products, shifts and direct summands preserve this equality.

Here is a complete verification of the needed finite Frobenius property. Let h_j(x_j,...,x_n) be the complete homogeneous symmetric polynomial of ordinary degree j in that tail, and put

\[
g_j=h_j(x_j,\ldots,x_n),\qquad J_n=(g_1,\ldots,g_n).
\tag{FC13}
\]

The ideals I_n and J_n are equal. In the quotient by I_n, the formal series identity

\[
\prod_{i=1}^n(1-x_i t)=1
\]

implies

\[
\prod_{i=j}^n(1-x_i t)^{-1}
=\prod_{i<j}(1-x_i t).
\]

The right side has degree at most j−1, so its coefficient in degree j vanishes, giving g_j=0 and J_n contained in I_n. Conversely, in the quotient by J_n, put `H_j(t)=prod_(i=j)^n(1-x_i t)^(-1)`. Descending induction shows H_j is a polynomial of degree at most j−1. Indeed `H_j=H_(j+1)/(1-x_j t)`, the induction hypothesis makes coefficients of H_(j+1) above j vanish, and the degree-j coefficient of H_j is g_j=0. The coefficient recurrence then makes every higher coefficient of H_j zero. This starts with the empty-tail series1. In particular H_1=1, so its inverse product is1 and all e_j vanish. This proves I_n contained in J_n.

The g_j are triangular: g_j is monic of degree j in x_j, with coefficients in k[x_(j+1),...,x_n]. Starting with k and adjoining x_n,x_(n−1),...,x_1 successively modulo g_n,g_(n−1),...,g_1 gives B_n as an iterated monic extension. At the jth step the quotient is free with basis `1,x_j,...,x_j^(j-1)` over the preceding ring, since division by a monic polynomial works over every coefficient ring. Thus

\[
\dim_k B_n=\prod_{j=1}^n j=n!,
\tag{FC14}
\]

and the Artin monomials `prod x_j^(a_j)` with `0≤a_j<j` give a basis. The ring is connected graded and finite, so its positive-degree ideal is nilpotent and is its unique maximal ideal.

Finally, if T is a finite commutative Frobenius algebra and

\[
C=T[z]/(z^j+a_1z^{j-1}+\cdots+a_j),
\tag{FC15}
\]

then the T-linear functional extracting the coefficient of z^(j−1) makes C a Frobenius extension of T. In the basis1,z,...,z^(j−1), the matrix of this multiplication pairing is zero when the two exponents sum to less than j−1 and is one on the reverse diagonal. Its determinant is therefore plus or minus one, regardless of the coefficients above that diagonal. Composing with a Frobenius functional on T gives a nondegenerate k-pairing on C. Induction through the monic extensions above proves that B_n is Frobenius. All polynomial relations are homogeneous; the resulting functional is homogeneous, supported on the top Artin monomial. This verifies the graded version needed in FC9 as well.

For the product of two independent type-A systems, take

\[
A=R_n\otimes_k R_n,\qquad
I=I_n\otimes R_n+R_n\otimes I_n,
\qquad B=B_n\otimes_k B_n.
\tag{FC16}
\]

The tensor product of the two Frobenius functionals is nondegenerate. B is connected graded and finite local of dimension `(n!)^2`, and the displayed elementary-symmetric generators of I act centrally on every Soergel term for `S_n times S_n`. Every such term is finite graded-free on either side: Bott--Samelson terms are, and a finite graded projective direct summand over a connected polynomial ring is graded-free, by lifting a homogeneous residue basis and graded Nakayama. These observations verify every premise of FC-A except the nonzero Euler rank, which follows from the actual class below.

For n=2 this entire central fiber is particularly transparent after changing to an invariant and an anti-invariant coordinate in each factor: it is `k[x,y]/(x^2,y^2)`, with Frobenius functional extracting xy. No general invariant-ring theorem is needed in any rank because FC12--FC16 supply the relevant verification.

## 3. Exclusion of every bounded ordinary type-A lift of the actual generator

**Theorem FC-B.** Let n≥2, let k have characteristic zero, and work in the bounded homotopy category of ordinary Soergel bimodules for `S_n times S_n` with the standard permutation realization. For a simple adjacent transposition s, there is no bounded complex X with Euler class

\[
P_s=b_s\otimes b_s+(b_s-\delta)\otimes(b_s-\delta)
\tag{FC17}
\]

and an actual homotopy quadratic

\[
X\otimes_A X\simeq
\bigl(A(2)\oplus A^{\oplus2}\oplus A(-2)\bigr)\otimes_A X.
\tag{FC18}
\]

The theorem imposes no direct-sum decomposition of X and no restriction on its bounded differentials.

### Proof

Apply the generic graph functor from the core F59 proof. Its semisimple amplitude lemma and the actual class force

\[
H^i(X_Q)=0\ (i\ne0),\qquad
H^0(X_Q)=Q_e^{\oplus2}\oplus Q_\tau^{\oplus2},
\quad\tau=(s,s).
\tag{FC19}
\]

In particular the Euler left rank of X is four. Equivalently the ordinary left graded-rank character sends b_s to delta and its complementary class to zero, so it sends P_s to delta squared. Central reduction by FC16 therefore has Euler k-dimension `4 dim_k B`, nonzero. Theorem FC-A applies and proves that X has only H^0=M, which is finite graded-free on the left.

We include the complete remaining graph argument to make the conclusion independent of an unproved descent assertion. Change coordinates so that

\[
A=k[x,y,z_1,\ldots,z_m],\qquad
\tau(x)=-x,\quad\tau(y)=-y,\quad\tau(z_i)=z_i.
\tag{FC20}
\]

The anti-invariant coordinates are the two independent simple roots. In a homogeneous left basis of M, let U,V be the matrices of right multiplication by x,y. Generic graph support FC19 gives

\[
yU=xV,\qquad U^2=x^2I.
\tag{FC21}
\]

Since M is left-free, these polynomial matrix identities hold over A. Coprimality of x,y implies that x divides every entry of U, so U=xZ and V=yZ for a degree-zero matrix Z over A. Then Z^2=I. Every fixed coordinate acts on the right by its left scalar, again by generic equality and left torsion-freeness. The degree-zero bimodule idempotents `(I plus/minus Z)/2` split M into two graded projective left modules, on which the right action is respectively the identity and tau.

Those graded projectives are graded-free: lift a homogeneous basis modulo A_+, use graded Nakayama for a surjection from the corresponding finite free module, split it in the graded category, then apply graded Nakayama to the complementary kernel, whose residue quotient is zero. Thus

\[
M\simeq A_e^{\oplus a(v)}\oplus A_\tau^{\oplus b(v)},
\qquad a(v),b(v)\in\mathbb N[v,v^{-1}].
\tag{FC22}
\]

The generic tau multiplicity is two, so b(v) is nonzero. This decomposition also proves right freeness. Consequently the derived tensor square of M is its ordinary tensor square. The canonical cohomology truncation identifies X with M in the derived category of bimodules, so FC18 induces the ordinary module quadratic for M. This step uses derived bimodule truncation, not a left-module homotopy splitting as though it were a bimodule map.

There are no nonzero bimodule maps between identity and tau graph modules: a possible scalar is annihilated by2x in the polynomial domain. Comparing their graded multiplicities in the quadratic therefore gives

\[
a(v)^2+b(v)^2=\delta^2a(v),\qquad
2a(v)b(v)=\delta^2b(v).
\tag{FC23}
\]

Since b(v) is nonzero and the Laurent ring is an integral domain, the second equality forces

\[
2a(v)=v^2+2+v^{-2}.
\tag{FC24}
\]

Its outer coefficients are odd, while every coefficient on the left is even. This contradiction proves FC-B. ∎

## 4. Exact reach and remaining alternatives

FC-B rules out the requested bounded-complex repair inside the ordinary type-A Soergel category, for every actual named simple generator and every rank n≥2, with the original ambient Euler class and the ordinary cohomologically degree-zero coefficient object for delta squared. Since the quadratic already fails, no choice of coherent higher maps in that category can repair it. This closes the particular bounded coupled-complex possibility that remained after the direct-sum and invariant-correspondence tests.

The following are different hypotheses and are not ruled out by this proof: an unbounded completion lacking finite extreme degrees; a coefficient complex with Euler class delta squared but additional cohomological degrees; a localization changing the finite coinvariant fiber; a different monoidal category or an altered map to the ordinary Hecke Grothendieck group; and the existing finite-state graded kernels of F56, which preserve the actual specified tensor action but are not a bounded ordinary-Hecke lift of this ambient class. Nor is the theorem a no-go for arbitrary derived bimodules lacking the termwise finite freeness and central coinvariant action used in FC-A.

The obstruction is categorical and integral in its graded multiplicities. It does not depend on a finite-field specialization, a positivity conjecture, or the purity of a point complex. Source signed/factored positivity and VIII's basis program remain separate statements. The all-rank conclusion here is specifically the ordinary type-A category just defined, not an assertion about unspecified nonstandard geometric categories.

## 5. Primary sources and separate Grothendieck dictionary

The ordinary Soergel conventions, graph localization and Rouquier background are the exact inspected original sources recorded in the core report: Elias--Williamson, *Hodge theory*, Sections3.3--3.5 pp1105--1108 and Section6.4 p1121; Elias--Williamson, *Localized calculus*, arXiv2011.05432v2, Section1.1 pp3--4, Theorem1.6 and Remark1.7 pp4--5, Section2.1 equations2.1--2.6 p7. The new specialization theorem, its duality and the graph contradiction are proved in full above. The standard finite type-A coinvariant Frobenius property is verified directly by FC12--FC16, rather than credited to a newly located source or claimed as a new theorem.

The relevant affine module/sheaf dictionary is EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92. The quotient along the invariant origin is an actual central module quotient; its preservation of the relation is proved by the balanced tensor presentation FC4. It is not a general cohomology-and-base-change claim. The SGA6 I Definition4.7 pp121--122 and Example4.8 p122 perfect-complex framework is applied on the displayed tensor sides, where the terms are finite free. At the finite Frobenius fiber, exact module duality supplies the missing lower amplitude bound; this is algebraic Frobenius duality of a finite algebra, not an arithmetic Frobenius endomorphism or a Weil-weight argument.

The graded multiplicity polynomials in FC22 lie in an effective coefficient cone, with the usual torus-action vocabulary of SGA3 I4.7.2--3/cote90 scan17. SGA6 V sections2--3/cote133 scan18 provides the existing distinction between effective and virtual coefficient classes. No lambda-ring structure on a noncommutative Grothendieck algebra is asserted. The new contradiction uses actual graded multiplicities after a proved module splitting; it is not obtained merely by calling a virtual Euler class positive. All archive locators are framework anchors only.

Independent whole-proof review is requested. The existing core and theta support report are unchanged. No main TeX or shared master log has been edited.

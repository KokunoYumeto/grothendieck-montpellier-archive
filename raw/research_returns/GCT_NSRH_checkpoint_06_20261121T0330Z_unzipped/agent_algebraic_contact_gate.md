# F52: algebraic spectral retuning and the actual order-two collision

Author: /root/gct_statements, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC. Parent proposed the contact-order direction. The author independently derived the elementary norm-polynomial/Kummer argument and the full local obstruction below. A constructive first-order model shows why the relative-order hypothesis matters. Independent review is requested.

## 1. Precise setting

Let K be a finite extension of C(v), let F be an invertible N-by-N matrix over K, and fix b>1. Assume regular evaluations F_b and F_{b^n} of this same algebraic family have been chosen for every sufficiently large integer n, with
\[
\operatorname{Spec}F_{b^n}
  =\operatorname{Spec}(F_b^n)
\tag{C1}
\]
as multisets. The evaluations may use different places over different b^n. No continuity of a sheet is assumed. Full spectra, not just traces, are required here. No purity or integral-weight hypothesis is imposed.

Finitely many algebraic matrix coefficients always generate a finite extension, so the finite-K formulation loses no generality for finite algebraic matrix families.

Let R=C[v,v^{-1}] localized at v=1. Let R' be a discrete valuation ring of K over R, and suppose F has a regular invertible matrix model on a free R'-module M. Put
\[
\delta=v+v^{-1},\quad D=\delta^2,\quad
\Delta=\frac{(D-1)(D-4)}{D^2}.
\tag{C2}
\]
The actual nonstandard rank-three order after this coefficient change is
\[
A_{R'}=R'\times R'\times
 M_2\bigl(R'[x]/(x(x-\Delta))\bigr).
\tag{C3}
\]
The theorem will exclude an R'-algebra isomorphism from the full relative centralizer End_{R',F}(M) to (C3). This is stronger data than an isomorphism of abstract special fibers, and its exact scope is essential.

## 2. Every base eigenvalue has a monomial power

**Lemma C4.** For every eigenvalue alpha of F_b there are integers L>0 and a such that
\[
\alpha^L=b^a.
\tag{C4}
\]

**Proof.** Regard F as a C(v)-linear endomorphism of the finite-dimensional C(v)-space K^N. Its characteristic polynomial is a nonzero monic polynomial in C(v)[Y] and annihilates the original K-linear matrix F. Clear denominators to obtain a nonzero polynomial Q(v,Y) in C[v,Y] with Q(v,F)=0.

Outside finitely many parameter values the coefficients and chosen matrix evaluations are regular. By (C1), alpha^n is an eigenvalue of F_{b^n}, so
\[
Q(b^n,\alpha^n)=0
\]
for all sufficiently large n. Expand Q as a sum of distinct nonzero monomials q_{a,c}v^aY^c. The displayed relation is a finite power sum on roots b^a alpha^c. Finite-power-sum uniqueness forces each grouped coefficient to vanish. At least two distinct monomials therefore have equal roots:
\[
b^a\alpha^c=b^{a'}\alpha^{c'}.
\]
They cannot have c=c', since then b>1 forces a=a' as well. Thus alpha to a nonzero integral power equals an integral power of b; reverse signs if necessary to make the exponent positive. QED.

Choose a common positive L for all the base eigenvalues, with multiplicities, so that
\[
\alpha_j^L=b^{a_j},\qquad a_j\in\mathbf Z.
\tag{C5}
\]
Thus their sizes are rational powers of b, and their phases are roots of unity. This conclusion uses full spectral retuning and algebraicity; it was not postulated as a weight convention.

## 3. The finite-cover characteristic polynomial

Adjoin a parameter t satisfying v=t^L. Then
\[
K\otimes_{\mathbf C(v)}\mathbf C(t)
\]
is a finite product of fields: in characteristic zero a primitive-element polynomial for K is separable, and over C(t) its distinct irreducible factors give the product decomposition.

**Lemma C6.** On at least one field component K'' of this product, the family characteristic polynomial is
\[
\det(TI-F)=\prod_{j=1}^{N}(T-t^{a_j}).
\tag{C6}
\]

**Proof.** Restrict (C1) to n=Lr. At v=b^{Lr}, choose the positive value t=b^r. The desired evaluated spectrum is
\[
\{\alpha_j^{Lr}\}_j=\{b^{a_jr}\}_j
                  =\{t^{a_j}\}_j.
\]
After excluding finitely many bad parameter values, the chosen evaluation of K together with t=b^r gives an evaluation of a finite model of the tensor product. It selects one of its finitely many field components. One component occurs for infinitely many distinct r.

On that component, every difference between a family characteristic-polynomial coefficient and the corresponding coefficient of the right side of (C6) has zero values over infinitely many distinct t=b^r. A nonzero algebraic function cannot do this. For an elementary proof, take its monic minimal polynomial over C(t); its constant term is a nonzero rational function. Outside the finitely many poles of the coefficients, a zero of the algebraic function forces a zero of that constant term. There are only finitely many such t. Therefore all the differences are zero, proving (C6). QED.

For clarity about the finite model used here, one may invert finitely many nonzero polynomials so that a primitive-element integral model, its discriminant, the matrix coefficients and the idempotents selecting the product components are all regular. The resulting finite product decomposition is then defined on that open set. Every sufficiently large b^{Lr} lies there. The tensor-product evaluation is the product of the selected evaluation on K and the prescribed evaluation t=b^r; a map from a product to C chooses one factor. Thus no assumed continuous branch or arbitrary relabeling of algebraic components is hidden in the argument.

Equation (C6) says that after a finite Kummer cover the eigenvalue functions themselves are monomial characters. Other embeddings may multiply these characters by the relevant roots of unity; the local argument below is invariant under those choices.

## 4. The actual center requires second-order contact

Extend the chosen valuation ring R' to a valuation ring R'' in the component K'' of Lemma C6. Such an extension exists by lying over for the finite integral closure. It is a discrete valuation ring. Since R'' is torsion free over the DVR R', it is flat.

The centralizer commutes with this scalar extension: it is the kernel of
\[
\operatorname{Mat}_N(R')\longrightarrow
\operatorname{Mat}_N(R'),\qquad U\longmapsto UF-FU,
\]
and flat base change preserves this kernel. Therefore an assumed isomorphism
\[
\operatorname{End}_{R',F}(M)\simeq A_{R'}
\tag{C7}
\]
would give the same isomorphism over R''. Write e for the positive valuation of v-1 in R''.

The Frobenius F is a central element of its full centralizer. Under (C7), its component in the matrix-center factor must therefore have the form
\[
c_0+c_1x,\qquad c_0,c_1\in R''.
\]
On the two generic center branches, its values are
\[
\beta_1=c_0,\qquad
\beta_2=c_0+c_1\Delta.
\tag{C8}
\]
Consequently
\[
\beta_2-\beta_1\in\Delta R''.
\tag{C9}
\]

The coefficient Delta has exact order two in v-1:
\[
D-4=(v-v^{-1})^2
    =(v-1)^2(v+1)^2/v^2,
\]
and the remaining factor (D-1)/D squared is a unit at v=1. Thus
\[
\operatorname{ord}_{R''}(\Delta)=2e.
\tag{C10}
\]

The generic algebra in (C3) is the split semisimple product of two scalar and two two-by-two matrix algebras. Because F is central in it, its minimal polynomial divides a product of linear factors and is square free after repetitions are removed; hence F is diagonalizable over the generic splitting field. Its values on the four primitive central blocks must be distinct: if two were equal, every linear map between their nonzero eigenspaces would commute with F, contradicting that those are separate central blocks of the full centralizer. In particular beta_1 and beta_2 in (C8) are distinct functions.

By (C6), they are two distinct monomial characters t^a and t^c. At the chosen point over v=1, t has a nonzero value t_0 satisfying t_0^L=1. Since
\[
v-1=t^L-1
\]
has a simple zero at t=t_0 in characteristic zero,
\[
\operatorname{ord}_{R''}(t-t_0)=e.
\tag{C11}
\]
The divisibility (C9) forces beta_1 and beta_2 to agree at t_0. Since they are distinct, a differs from c. The derivative of their difference at t_0 is
\[
a t_0^{a-1}-c t_0^{c-1}
 =(a-c)t_0^{a-1}\ne0.
\]
This also holds for negative exponents because t_0 is nonzero. Hence
\[
\operatorname{ord}_{R''}(\beta_2-\beta_1)=e,
\tag{C12}
\]
contradicting (C9)–(C10), which require order at least 2e.

**Theorem C13.** No algebraic finite matrix family satisfying full spectral retuning (C1), with unrestricted spectral sizes, can have the actual whole relative order (C3) as its full regular centralizer at the collision parameter. The result allows arbitrary coefficient covers, further ramification, variable evaluation sheets, auxiliary rank and Jordan behavior before the comparison is imposed.

It excludes a specific full relative-order comparison. It does not exclude a specified suborder of a larger centralizer, an abstract isomorphism of special fibers, a nonregular or nonflat coefficient model, or a trace-only/virtual comparison. The order-two divisibility of the actual center, rather than merely its abstract dual-number special fiber, is the decisive input.

## 5. Sharpness: a first-order algebraic model with the same abstract special algebra

This constructive model uses nonintegral spectral weights. It is not a mixed model with integral Deligne weights.

Let v=t^3, choose a primitive cube root omega, and take the point t=omega over v=1. Define
\[
\gamma_1=t^2,\qquad \gamma_2=t^5,\qquad
\eta=\gamma_2-\gamma_1=t^2(v-1).
\tag{C14}
\]
Use a finite coefficient localization T of C[t,t^{-1}] that inverts
\[
\delta(v),\ h(v),\ D(v)-2,\quad
t-1,\ t^2-1,\ t^5-1,\ t^2-t,\ t^5-t.
\tag{C15}
\]
Every factor is nonzero at t=omega and at every positive real t>1. Thus this is an explicit finite base admitting the local point and all the required positive arithmetic evaluations; it is not merely a local ring whose extra inverses could obstruct those evaluations.

Put
\[
C_\eta=T[x]/(x(x-\eta)),\qquad J=C_\eta,\qquad
F_J=\gamma_1+x.
\tag{C16}
\]
In the column basis (1,x),
\[
F_J=\begin{pmatrix}\gamma_1&0\\1&\gamma_2\end{pmatrix}.
\]
Its determinant is t^7, a unit. Since x=F_J-gamma_1, the centralizer on J is C_eta, including at collision. Let T_a denote a scalar coefficient line with Frobenius a and set
\[
H=T_1\oplus T_t\oplus J^{\oplus2}.
\tag{C17}
\]
The sector differences are units by (C15); for instance the determinants of F_J-1 and F_J-t are (gamma_1-1)(gamma_2-1) and (gamma_1-t)(gamma_2-t). Therefore
\[
\operatorname{End}_F(H)=T\times T\times M_2(C_\eta).
\tag{C18}
\]
At t=omega the three eigenvalue sectors are 1, omega and omega squared. J is a nontrivial Jordan block in its last sector, and (C18) specializes abstractly to
\[
\mathbf C\times\mathbf C\times
M_2(\mathbf C[\epsilon]/(\epsilon^2)),
\]
exactly the abstract special algebra of F19.

At a parameter v=b>1 choose t_b=b^{1/3}, and at v=b^n choose t_n=t_b^n. The spectrum in (C17) consists of monomial characters 1,t,t^2,t^5 with multiplicities 1,1,2,2, so it satisfies full spectral retuning. The lower-left entry of the Jordan presentation does not obey a fixed-basis matrix-power law; only the claimed spectral rule is used.

Under v=Q^{1/2}, these characters have weights 0,1/3,2/3,5/3. This is the explicit nonintegral-weight qualification. The chosen point t=omega over v=1 is not the positive real branch limit t=1. Thus the model does not contradict F51's integral-weight collision theorem.

The collision parameter eta has order one at t=omega. Its relative center therefore differs from the actual order-two center, precisely as required by Theorem C13.

## 6. The actual order and tensor module still embed in that larger centralizer

This model also illustrates the permitted subalgebra alternative concretely. The ratio
\[
c=\Delta/\eta
 =\frac{(D-1)(v-1)(v+1)^2}{D^2\,t^2v^2}
\tag{C19}
\]
belongs to T and has exact order one at t=omega. There is an injective homomorphism
\[
T[x_{\rm act}]/(x_{\rm act}(x_{\rm act}-\Delta))
 \longrightarrow C_\eta,\qquad
x_{\rm act}\longmapsto c x.
\tag{C20}
\]
Indeed (c x) squared equals c eta times c x, namely Delta times c x. In the free bases (1,x_act) and (1,x), the map is diag(1,c), hence injective over the domain T. It induces an embedding of the actual rank-three order A_T into (C18), with identical scalar sectors and matrix extension on the center.

Localizing at t=omega, the center cokernel is R'/(c), of length one, and the two-by-two matrix-sector cokernel has length four. The generic embedding is an isomorphism. On the special fiber, however, the actual nilpotent x_act maps to zero; its four-dimensional matrix radical is killed. Thus the abstract special centralizer is isomorphic to A_1, but the actual relative embedding is not that isomorphism. This distinction is part of the theorem's sharpness.

Let L_0=C_eta/(x) and L_eta=C_eta/(x-eta), with Frobenius gamma_1 and gamma_2. Define
\[
K=T_1^{20}\oplus T_t^4\oplus
 L_0^{16}\oplus L_\eta^4.
\tag{C21}
\]
By the same cyclic-source and sector-unit argument,
\[
\operatorname{Hom}_F(H,K)
 \simeq\epsilon_+^{20}\oplus\epsilon_-^4
  \oplus\operatorname{Row}(L_0)^{16}
  \oplus\operatorname{Row}(L_\eta)^4
\tag{C22}
\]
has rank64. Restriction along (C20) makes the actual center coordinate act on its branches by 0 and Delta, respectively. Therefore it is the actual F21 tensor lattice after this coefficient extension, with its named generators, not merely a module of matching dimension. The actual regular basis comparison is defined because the finite base contains the needed delta, h and D-2 inverses.

Postcomposition on the multiplicity factors also retains the ordinary left matrices as in F46. Over the domain T the branch intertwiners vanish because eta is a nonzero divisor, so the full multiplicity commutant is M20(T) times M4(T) times M16(T) times M4(T), and its matrix units lift to K. At collision the branch multiplicities combine as before.

The spectra of both H and K obey retuning, with the same nonintegral-weight qualification. The invariant Hom object has identity Frobenius. This does not give the all-extension quantum-word trace comparison on that one fixed Hom space, nor the F24 opposite-sign output or VIII's designated global form. It does show explicitly that the actual action may survive inside a proper larger centralizer order even though a full relative-order identification is impossible.

### 6.1. Additional linear operators on this unchanged H cannot recover the embedded suborder

Let R' now be the local DVR at t=omega in the explicit model, let B=End_F(H), and let A denote the actual embedded suborder (C20) with its scalar and matrix extensions.

**Proposition C23.** There is no collection of ordinary R'-linear endomorphisms of this same free module H whose simultaneous centralizer, together with F, equals this embedded A.

**Proof.** A simultaneous centralizer in End_{R'}(H) is saturated: if d is a nonzero element of R' and dU commutes with every specified operator G, then d(UG-GU)=0. The matrix module End_{R'}(H) is torsion free, so UG=GU for each G, and U belongs to the same centralizer.

The embedded A is not saturated. For example take U to be x times one diagonal matrix unit in the M2(C_eta) sector of B. It is a regular endomorphism of H and does not belong to A, since its x coefficient is one, not divisible by c. But cU belongs to A by (C20), and c is a nonzero element of the DVR. Thus A cannot be such a simultaneous centralizer. QED.

This assertion fixes both the first-order H and the displayed actual embedding. It does not exclude changing the module lattice or geometric object, retaining A as explicitly specified algebra data, or using a different categorical comparison. In particular a regular-module construction with identity Frobenius can tautologically retain an algebra and its module actions; that does not provide the quantum-grading or sign-path comparison. The proposition only rules out repairing this nonsaturated embedding by adding ordinary linear commutation equations on the unchanged H.

## 7. Verification and source scope

The actual relative algebra and branch tensor module are the previously fully proved F19/F21 inputs. Delta's order is checked directly in (C10). All new field, polynomial, finite-component, local-center and first-order model arguments are supplied in full above. The finite-cover step is spelled out through an integral model to distinguish evaluations of one algebraic family from switching unrelated functions.

No formal proof kernel, numerical experiment or source assertion of a nonstandard geometric Frobenius is claimed. The theorem addresses an exact algebraic full-centralizer comparison; the first-order model and the retained subalgebra action explain the limits of that exclusion.


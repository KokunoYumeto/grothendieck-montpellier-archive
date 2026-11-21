# F59 continuation: a finite-Frobenius countermodel and the unbounded singular derived correspondence

Author: `/root/rectangular_and_theta`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Inherited reasoning effort is not exposed.

This report tests two concrete routes toward the remaining invariant-descended, nonflat/nonflat coefficient case. Neither is replaced by a generic/top-degree identification. The first route cannot use only the proposed numerical hypotheses: an explicit bounded bifree countermodel over the actual coinvariant quotient has the required scalar Euler class and nonzero Euler dimension, yet nonprojective cohomology. Its termwise class is the longest ordinary object rather than the designated nonstandard generator. The second route has a complete obstruction: the full derived correspondence of the codimension-two diagonal involution has nonzero Tor in every positive degree.

These two statements leave the frozen central-polynomial report and fragment unchanged. They do not settle every bounded nonflat/nonflat construction with the designated ambient Euler class.

## 1. The actual coinvariant quotient and its normalization

Let k have characteristic zero and set

\[
A=k[x,y],\quad\deg x=\deg y=2,\qquad
S_0=k[x^2,y^2],\qquad
B=A/(x^2,y^2).                                         \tag{QR1}
\]

The two simple reflections negate x and y separately. The ring B is the actual central coinvariant quotient for their product. It is a local graded algebra of dimension four, with basis `1,x,y,xy` and graded dimension

\[
h_B(v)=(1+v^2)^2.                                      \tag{QR2}
\]

The coefficient-of-xy functional gives a nondegenerate symmetric Frobenius pairing: it pairs 1 with xy and x with y. It is homogeneous of degree minus four. Consequently

\[
B\simeq\operatorname{Hom}_k(B,k)\langle4\rangle,
\qquad
\operatorname{Hom}_B(M,B)
\simeq\operatorname{Hom}_k(M,k)\langle4\rangle           \tag{QR3}
\]

for finite graded B-modules M, with the appropriate right action. In particular the B-dual is exact. Here `M<e>` shifts displayed internal degrees upward by e; `M(1)` in the ordinary Soergel source shifts them downward by one.

The latter convention was freshly checked in the original Elias--Williamson Hodge-theory source, Section3.3, printed p1105: `M(1)^i=M^{i+1}`. Section3.4, p1106, gives `B_s=A tensor_{A^s} A(1)` with its generator in degree minus one. For the two independent reflections their product is

\[
B_1\otimes_A B_2\simeq(A\otimes_{S_0}A)(2).            \tag{QR4}
\]

This also follows directly by eliminating the middle coordinates: the first reflection changes only x and the second only y. After the central quotient the normalized longest object is therefore

\[
L_0=(B\otimes_k B)\langle-2\rangle.                    \tag{QR5}
\]

Thus the internal shift used below is the actual ordinary quotient normalization, not a freely chosen numerical recentering. The equality `(2)=<-2>` explains its sign.

## 2. A bounded bifree quadratic with nonprojective cohomology

Define the finite free left B-complex

\[
K=[B\langle2\rangle\xrightarrow{x}B],
\quad\deg_{\rm coh}K=-1,0,
\qquad
L=B\oplus K\oplus K[1].                               \tag{QR6}
\]

Let `L^vee=Hom_B(L,B)` be its ordinary cochain dual, a finite free right B-complex, with the standard differential signs. Put

\[
Z=(L\otimes_k L^\vee)\langle-2\rangle,
\qquad
E=(L^\vee\otimes_B L)\langle-2\rangle.                 \tag{QR7}
\]

E is viewed as a bounded complex of finite graded k-vector spaces, hence as a scalar coefficient. Z is a bounded B-bimodule complex; every term is finite free on both sides.

### Proposition QR-A

There is an actual chain isomorphism, and hence a derived isomorphism,

\[
Z\otimes_B^{\mathbf L}Z\simeq E\otimes_k Z.             \tag{QR8}
\]

Moreover

\[
\chi_v(E)=v^{-2}h_B(v)=v^2+2+v^{-2}=\delta^2,
\qquad
\chi_k(Z)=16=4\dim_kB,                                 \tag{QR9}
\]

but Z has nonprojective, hence nonflat, cohomology on the left and on the right.

### Proof of the actual quadratic and Euler assertions

All complexes involved have the needed bounded free terms. Associating the tensors gives

\[
\begin{aligned}
Z\otimes_B Z
&=(L\otimes_k L^\vee\otimes_B L\otimes_k L^\vee)
       \langle-4\rangle\\
&\simeq(L^\vee\otimes_B L)\langle-2\rangle
       \otimes_k(L\otimes_k L^\vee)\langle-2\rangle.
\end{aligned}
\]

The final isomorphism moves the middle finite k-complex past the first factor using the usual cohomological Koszul sign. It is B-bimodule-linear, because the outer B-actions remain on L and L^vee. This is an explicit associative/symmetric chain comparison, not a dimension argument.

The termwise graded **free-rank** Euler polynomial of L is 1. Indeed the K and K[1] terms cancel, leaving the single copy of B. Its B-dual has the same free-rank Euler polynomial 1, with degrees inverted before this cancellation. Therefore the actual finite k-Euler polynomial of `L^vee tensor_B L` is `h_B(v)`. The internal shift in QR7 gives QR9. Likewise Z has finite k-Euler polynomial `v^-2 h_B(v)^2`, giving 16 at v=1. No acyclicity inference from an Euler cancellation is used.

### Explicit nonprojective cohomology

Put `T=B/(x)`, with graded dimension `1+v^2`. Since `ann_B(x)=(x)` and the generator of the degree-minus-one term of K has internal degree two,

\[
H^{-1}(K)=T\langle4\rangle,
\qquad H^0(K)=T.
\]

Thus

\[
\begin{array}{c|ccc}
i&-2&-1&0\\\hline
H^i(L)&T\langle4\rangle&T\langle4\rangle\oplus T&B\oplus T.
\end{array}                                             \tag{QR10}
\]

Exact B-duality from QR3 reverses these cohomological degrees. The identity `Hom_B(T,B)=(x)=T<2>` gives

\[
\begin{array}{c|ccc}
i&0&1&2\\\hline
H^i(L^\vee)&B\oplus T\langle2\rangle&
T\langle-2\rangle\oplus T\langle2\rangle&T\langle-2\rangle.
\end{array}                                             \tag{QR11}
\]

Künneth over the field k is exact. At degree minus two only the pair `(-2,0)` contributes, giving

\[
H^{-2}(Z)=
\bigl(T\langle4\rangle\otimes_k
        (B\oplus T\langle2\rangle)\bigr)\langle-2\rangle.
                                                               \tag{QR12}
\]

As a left B-module this is explicitly

\[
T\langle2\rangle\oplus
T\langle4\rangle^{\oplus3}\oplus
T\langle6\rangle^{\oplus2}.                            \tag{QR13}
\]

It has dimension twelve, is nonzero, and is annihilated by left x. It cannot be projective: finite projective modules over the local algebra B are free, while nonzero x acts nontrivially on every nonzero free B-module. The local free assertion also follows by lifting a residue basis, splitting a free surjection and using Nakayama. Similarly the degree-two group has a nonzero right T-factor, hence is annihilated by right x and is nonprojective on that side. More explicitly, as a right module it is

\[
T\langle-4\rangle^{\oplus2}\oplus
T\langle-2\rangle^{\oplus3}\oplus T.                   \tag{QR14}
\]

The ungraded cohomology dimensions of Z are consequently

\[
(12,32,56,32,12)\quad\text{in degrees }-2,-1,0,1,2,
\]

as follows by convolving the dimension lists `(2,4,6)` and `(6,4,2)`. Their alternating sum is sixteen, in agreement with QR9. This proves QR-A with explicit nonprojective cohomology. QED.

## 3. The termwise class is demonstrably not the designated target

Every term of Z is a sum of shifts of `B tensor_k B`. Since the two free-rank Euler polynomials in QR7 are both 1, its termwise split-Grothendieck Euler class is exactly `[L_0]`. It is not the reduced target

\[
\overline P=2[L_0]-\delta[\overline B_1]
             -\delta[\overline B_2]+\delta^2[B].         \tag{QR15}
\]

Here `overline B_i` is the actual central quotient of B_i, so its cyclic generator has degree minus one. To verify the distinction without assuming injectivity of a reduction map on Grothendieck groups, use the additive graded invariant

\[
\mathcal H(M)=\operatorname{Hilb}_v
              \operatorname{Hom}_{B\text{-}B}^{\bullet}(M,B).
                                                               \tag{QR16}
\]

For each of the unit, one-reflection and longest cyclic bimodules, every image of its cyclic generator in the commutative ring B defines a bimodule map. Its relations are already satisfied by the equal actions on B. Their generator degrees give

\[
\mathcal H(B)=h_B,
\quad\mathcal H(\overline B_i)=v h_B,
\quad\mathcal H(L_0)=v^2 h_B.                           \tag{QR17}
\]

This is additive on direct sums and thus on the split Grothendieck group. Source shifts `(1)` raise the internal degree of such a map by one, so multiplication by the source Laurent variable is exactly multiplication by v in this invariant. Applying it to QR15 minus `[L_0]` gives

\[
\mathcal H(\overline P-[L_0])
 =(v^2-2\delta v+\delta^2)h_B
 =v^{-2}h_B=\delta^2\ne0.                              \tag{QR18}
\]

Thus the example does not satisfy the designated class even after the actual quotient. It does satisfy the purely numerical hypotheses proposed for a quotient-rigidity argument: bounded bifree terms, a scalar-complex quadratic, coefficient Euler delta squared and nonzero total Euler dimension `4 dim B`. Those numerical hypotheses alone cannot force projective cohomology. A proof for the designated target must retain extra class or action information.

## 4. The singular diagonal-invariant quotient has an unbounded derived self-intersection

Keep A=k[x,y], but now use the **different** invariant ring

\[
S_\tau=A^{\tau}=k[a,b,c]/(ac-b^2),
\qquad a=x^2,\ b=xy,\ c=y^2,
\quad\tau(x,y)=(-x,-y).                                \tag{QR19}
\]

The degrees of a,b,c are four. The relation gives the full invariant ring: reducing powers of b to exponent zero or one yields distinct monomials in x,y, and these are precisely the even-total-degree monomials. Write A=S_tau direct sum M for the even and odd parts as S_tau-modules. The odd module M is generated by x,y, both in degree two, with relation matrix

\[
\Phi=\begin{pmatrix}b&c\\-a&-b\end{pmatrix}.             \tag{QR20}
\]

Indeed a relation `p x+q y=0`, with p,q even, has `p=yh,q=-xh` by coprimality. The polynomial h is odd, so `h=xu+yv` for even u,v. This gives exactly the two columns of Phi and proves completeness of the presentation.

### Proposition QR-B

For every i>=1,

\[
\operatorname{Tor}^{S_\tau}_i(A,A)
       \simeq k\langle4+4i\rangle.                     \tag{QR21}
\]

Consequently `A tensor^L_{S_tau} A` has nonzero cohomology in every negative degree and admits no bounded derived replacement. Passing from the underived singular correspondence to its full derived fiber product therefore leaves the bounded route.

### Proof

Over the polynomial ring R=k[a,b,c], put f=ac-b^2. The matrix identity is

\[
\Phi^2=-fI.                                            \tag{QR22}
\]

Over S_tau this gives a complex with Phi at every positive differential. It is exact: if a vector w in `S_tau^2` lies in the kernel, lift it to `R^2` and write `Phi w_tilde=f z`. Multiplying again gives `-f w_tilde=f Phi z`. Since f is nonzero in the polynomial domain, cancellation gives `w_tilde=-Phi z`. Reducing modulo f puts w in the image. The reverse containment follows from QR22. Together with the proved presentation of M this gives the free resolution

\[
\cdots\xrightarrow{\Phi}S_\tau\langle10\rangle^2
\xrightarrow{\Phi}S_\tau\langle6\rangle^2
\xrightarrow{\Phi}S_\tau\langle2\rangle^2
\longrightarrow M\longrightarrow0,                   \tag{QR23}
\]

where the i-th free term has shift `2+4i`.

After tensoring with A, the matrix factors as

\[
\Phi_A=
\begin{pmatrix}xy&y^2\\-x^2&-xy\end{pmatrix}
=\begin{pmatrix}y\\-x\end{pmatrix}(x\ \ y).            \tag{QR24}
\]

Over the domain A its kernel is `A(y,-x)^T`: the equation `xu+yv=0` gives this by coprimality. Its image is `(x,y)A(y,-x)^T`. Thus every positive homology group of the tensor resolution is one copy of `A/(x,y)=k`. In the i-th term the kernel generator has the two extra internal degrees from y or x, giving total degree `(2+4i)+2=4+4i`. Finally A=S_tau direct sum M, and the first summand has no higher Tor. This proves QR21 for Tor(A,A). Derived tensor cohomology in degree minus i is precisely this nonzero Tor group. QED.

The same calculation with fixed spectator polynomial variables gives the corresponding shifted module `A/(x,y)` in every positive Tor degree. No claim about a regular reflection quotient is being used: S_tau is the singular codimension-two invariant ring, whereas S_0 in QR1 is the regular full-product invariant ring.

## 5. Exact consequences and remaining scope

QR-A blocks the proposed extension of the finite-Frobenius amplitude argument to arbitrary scalar-complex coefficients if it retains only nonzero Euler data. It supplies an actual bounded complex and an actual quadratic, and its nonprojective cohomology was computed rather than assumed. It does not disprove a refined theorem retaining the designated reduced Hecke class; QR18 proves why that class information is absent.

QR-B rules out a bounded realization of the particular **full derived** singular correspondence. The ordinary module `A tensor_{S_tau} A` remains a different bounded object with its previously computed torsion; replacing it by a full derived fiber product introduces the infinitely many Tor groups above. An ordinary reassociation does not remove them. This is not a theorem excluding every other nonflat/nonflat ordinary Soergel construction with a polynomial central coefficient.

The unresolved exact target is still PC3--PC5 of the frozen central-coefficient report, with invariant-descended C if coherent central movement is required, nonflat cohomology on both sides, the designated ambient Euler class, and an actual bounded quadratic. No global/generic-top equality is asserted for that remaining case.

## 6. Separate F59 dictionary and verification

The central coinvariant quotient, the cyclic bimodules and the singular invariant correspondence are actual affine module data. EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92 provide their coherent-sheaf dictionary. The exact Tor groups distinguish an underived fiber product from its derived version, while the explicit finite-Frobenius countermodel distinguishes positive Euler dimension from projective cohomology.

SGA6 I Definition4.7 pp121--122 and Example4.8 p122 give the bounded perfect-complex framework. Z lies in that framework on each side, while the full derived object in QR21 is unbounded. The scalar coefficient E is a finite complex of actual vector spaces, not a rational virtual replacement. Internal shifts use SGA3 I4.7.2--3/cote90 scan17, and the split/virtual class language uses SGA6 V Sections2--3/cote133 scan18 with the existing source-access qualification. No noncommutative lambda-ring or canonical-label comparison is inferred.

I freshly read the ordinary shift and reflection definitions in the original Elias--Williamson source, Sections3.3--3.4, pp1105--1106, before fixing the shift in QR5 and QR7. I checked the homogeneous Frobenius pairing, both dual cohomology tables, both nonprojective extreme groups, every Euler calculation, and the additive Hom invariant separating the target class. The periodic resolution and every Tor group in QR21 were proved directly over the polynomial ring; no unstated hypersurface-resolution theorem is needed. Fresh complete review is requested before integration. No root master file or shared log was edited.

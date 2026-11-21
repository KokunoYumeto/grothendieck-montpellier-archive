# Unit surface gluing: the exact local algebra, positive Ext, and actual nontensor objects

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** Complete local algebra, positive Ext and actual construction
independently whole-reviewed by /root and /root/imprimitive on 21 November
2026; both mathematical reviews PASS. Author and reviewers: GPT-6 Astra Pro,
inherited effort not exposed. Reviewed draft SHA-256:
`16b9e88d5c5c5190628272560e4749daa475da6b585cbc80af56e199abeacc77`.
The author and peer independently ran exact certificates. The final section
states exactly which traces these computations provide; the accompanying
SF-E824 avoids the full-derived-trace issue and excludes all these unit forms.
No semiregular seed or finite action is constructed.

## 1. The local module and its complete degree-zero endomorphism algebra

Work over a regular local ring \(R\) with regular parameters \(x,y\) cutting
out the smooth surface; tangential parameters are unrestricted. Put
\(I=(x,y)\), \(A_0=R/I\), \(v=(-y,x)^t\), \(w=(x,y)\), and

\[
 F=R^2/(I v).
 \tag{UG.1}
\]

This is the actual unit module \(M_0\) of the preceding construction, with
resolution

\[
 P:\quad R\xrightarrow{v}R^2\xrightarrow{v w}R^2\longrightarrow F.
 \tag{UG.2}
\]

The hull map is \(p:F\to I\), \(p(e_1)=x,p(e_2)=y\), and the torsion
\(T=A_0v\) has annihilator exactly \(I\).

Every endomorphism induces a scalar \(a\in R\) on the double dual \(R\).
Its action on \(T\) is multiplication by \(a\bmod I\): compatibility of
the extension with its local unit class identifies the torsion scalar with
the induced quotient scalar. Equivalently, apply the endomorphism to
\(v=-ye_1+xe_2\) and use the hull map. After subtracting \(a\operatorname{id}\),
the endomorphism maps into \(T\) and kills \(T\), so factors through
\(I\to T\). Since the Koszul relation is zero in \(T\),
\(\operatorname{Hom}_R(I,T)=A_0^2\).

Concretely, for a row \(b=(b_1,b_2)\) modulo \(I\), its nilpotent
endomorphism is \(\delta_b=v b\) on the two generators. Thus

\[
 \operatorname{End}_R(F)=\mathcal A=R\oplus J,
 \qquad J=A_0^2,\qquad J^2=0,
 \tag{UG.3}
\]

with multiplication \((a,b)(a',b')=(aa',ab'+a'b)\). In particular this
entire degree-zero algebra is commutative, not just its reduction. The sum
is direct because a scalar with zero hull action is zero in the domain
\(R\).

Globally, for \(S\) cut out by two sections of \(\mathcal O_X(D)\),

\[
 \mathcal E nd_X(M_0)=\mathcal O_X\oplus i_*J_S,
 \qquad J_S=\mathcal O_S(-D)^{\oplus2},\qquad J_S^2=0.
 \tag{UG.4}
\]

Indeed \(J_S=\mathcal H om(I_S,\mathcal O_S(-2D))
=N_{S/X}\otimes\mathcal O_S(-2D)\). Scalar multiplication provides the
global splitting, so no choice of a normal frame is required for (UG.4).

## 2. Positive local Ext and both actions of the nilpotent ideal

Apply \(\operatorname{Hom}_R(P,F)\). Write
\(u=(x,y)^t\) and \(w_F(a,b)=-ya+xb\). The resulting cochain complex is

\[
 F^2\xrightarrow{u w_F}F^2\xrightarrow{w_F}F.
 \tag{UG.5}
\]

Its last cohomology is \(F/IF=A_0^2\). To compute its middle cohomology,
let \((a,b)\in\ker w_F\). Applying the hull map gives
\(-yp(a)+xp(b)=0\). The regular-sequence relation implies
\(p(a)=xc,p(b)=yc\), for a unique \(c\in R\). Hence
\(a=ce_1+t_1,b=ce_2+t_2\), with \(t_1,t_2\in T\), and
\(w_F(a,b)=cv\). The latter is zero exactly when \(c\in I\).
Choose \(m\in F\) with \(p(m)=c\). Subtracting \(u m\) now leaves an
element of \(T^2\). Also \(uF\cap T^2=0\): if \(u m\in T^2\), then
\(xp(m)=yp(m)=0\), so \(p(m)=0\), and \(m\in T\) gives \(u m=0\).
Therefore

\[
 \ker w_F=uF\oplus T^2.
\]

The incoming image is \(u(IF)\). Since \(\ker(u:F\to F^2)=T\) and
\(T\subset IF\), we obtain

\[
 \operatorname{Ext}^1_R(F,F)
       =(F/IF)\oplus T^2=A_0^4,
 \qquad
 \operatorname{Ext}^2_R(F,F)=F/IF=A_0^2.
 \tag{UG.6}
\]

In particular \(I\) annihilates both groups.

Choose any row lift of \(b\), and put \(t_b=bv=-b_1y+b_2x\). A chain
lift of \(\delta_b\) on (UG.2), ordered by degrees \(0,-1,-2\), is

\[
 \bigl(vb,\ t_b I_2,\ t_b\bigr).
 \tag{UG.7}
\]

The two chain identities follow immediately from \(wv=0\). Consequently
the right action of \(J\) on both positive Ext groups is zero: it is
precomposition by \(t_b I\), and \(t_b\in I\). The left action is
also zero. On the last quotient, \(\delta_bF\subset T\subset IF\).
On the middle representatives, it kills \(T^2\), and it sends \(uF\)
to \(uT=0\). This checks both actions, rather than inferring centrality
from commutativity in degree zero.

Restoring the global twists in the resolution gives

\[
 \mathcal E xt^1_X(M_0,M_0)=i_*\mathcal O_S(D)^{\oplus4},
 \qquad
 \mathcal E xt^2_X(M_0,M_0)=i_*\mathcal O_S(3D)^{\oplus2}.
 \tag{UG.8}
\]

The first splitting comes from \(uM_0(2D)\) and
\(\mathcal O_S(-2D)(3D)^2\) in the kernel calculation. The second uses
\((M_0/IM_0)(4D)\), not merely \(M_0/IM_0\). These twists are essential.

## 3. Chain multiplication is not strictly the square-zero algebra

Although \(J^2=0\) on \(F\), the chain lifts (UG.7) do not multiply
strictly to zero. There is an explicit nullhomotopy. Put
\(j_b=(b_2,-b_1)^t\). For rows \(b,c\), the product of their chain
lifts is nullhomotopic by

\[
 h^0=j_b c:P^0\to P^{-1},
 \qquad h^{-1}=t_c b:P^{-1}\to P^{-2}.
 \tag{UG.9}
\]

At degree zero, \((vw)j_bc=t_bvc\). At degree minus one, the identity
\(t_bI_2-j_bw=vb\) gives
\(v(t_cb)+j_bc(vw)=t_bt_cI_2\). At degree minus two,
\((t_cb)v=t_bt_c\). Thus \(dh+hd\) is precisely the product of
the two chain lifts. This exhibits why a strict trace on degree-zero
matrices does not immediately give a trace on the entire derived descent
data. No dg formality assertion is made.

## 4. Actual nontensor gluing and its classification as a marked extension

Let \(H\) be any vector bundle. Consider actual coherent extensions

\[
 0\to i_*(H|_S(-2D))\to M\to H\otimes I_S\to0
 \tag{UG.10}
\]

whose local extension matrix is the identity under the specified
identification of the two rank-\(r\) bundles. Applying Hom to the actual
Koszul resolution of \(H I_S\) again gives a complex with zero
differential. Hence

\[
 \operatorname{Ext}^1_X(H I_S,i_*H|_S(-2D))
  =H^1\bigl(S,\operatorname{End}(H|_S)(-D)\bigr)^{\oplus2}
       \oplus H^0\bigl(S,\operatorname{End}(H|_S)\bigr).
 \tag{UG.11}
\]

Fixing the last component to \(I_r\) leaves the entire first vector
space as actual global extension classes. The zero vector gives
\(H\otimes M_0\).

There is also a direct gluing description, including its absence of a
higher associativity obstruction. Let
\(Y=(X,\mathcal O_X\oplus i_*J_S)\), the split square-zero thickening
defined by (UG.4). Locally (UG.10) is \(M_0^{\oplus r}\), and its
transition automorphisms lie in \(\mathrm{GL}_r(\mathcal A)\).
Reduction modulo \(J_S\) gives the transition functions of \(H\).
Starting with those functions, multiply by \(1+a_{ij}\), where
\(a_{ij}\) is a Čech cocycle in \(\operatorname{End}(H|_S)\otimes J_S\).
The cocycle equation is the ordinary additive one because \(J_S^2=0\).
Thus these are true transition functions, not projective transition data.
They define a vector bundle \(\widetilde H\) on \(Y\), and the actual
sheaf \(M=M_0\otimes_{\mathcal A}\widetilde H\). All constructions can
be checked on a finite affine cover, where evaluation identifies the local
module with \(M_0^r\).

A nonzero cohomology class in the first summand of (UG.11) gives an object
that is not a tensor product with \(M_0\), even allowing an isomorphism of
the hull. Indeed any isomorphism to a tensor product induces an automorphism
\(h\) of the canonical hull \(H\); compatibility with the unit local
class forces the torsion automorphism to be \(h|_S\). The zero extension
parameter is preserved by this pair of automorphisms, because the tensor
construction is functorial in \(H\). The induced conjugation on the first
summand of (UG.11) is invertible, and cannot send a nonzero class to zero.
Changing local splittings adds only a coboundary. A different tensor hull
would have to be isomorphic to \(H\) by taking double duals, so gives no
additional possibility.

## 5. A nonzero parameter in the explicit balanced high-rank family

Use the sixteen actual line-bundle classes of the compensation construction,
with the same positive multiplicities. Among their differences is

\[
 \delta=(8,-6,-8,6)
 =(-8,-6,-8,6)-(-16,0,0,0).
\]

Its four Hermitian eigenvalues, in the previous ordering, are
\(0,16-12\sqrt2,0,16+12\sqrt2\). Put \(D=3\theta\). For
\(a=1,2,3\), the divisor \(\delta-aD\) is nondegenerate with exactly
three negative eigenvalues. The published Mumford index theorem therefore gives cohomology only in
degree three. Exact already checked locator: Mumford, Abelian Varieties
(1970), section16, Vanishing Theorem p150 and its proof pp150--153, with
the complex Hermitian-index corollary and proof pp162--163. Riemann--Roch on the principal product gives

\[
 h^3(X,L_\delta(-aD))
  =(3a)^2\bigl(288-(16-3a)^2\bigr)
   =\begin{cases}1071&a=1,\\6768&a=2,\\19359&a=3.\end{cases}
 \tag{UG.12}
\]

The restriction Koszul resolution is

\[
 0\to L_\delta(-3D)\to L_\delta(-2D)^2
    \to L_\delta(-D)\to i_*(L_\delta(-D)|_S)\to0.
\]

Only its cohomology row in degree three survives. Thus
\(H^1(S,L_\delta(-D)|_S)\) is the kernel of the first map in that row,
and

\[
 h^1(S,L_\delta(-D)|_S)\ge19359-2\cdot6768=5823>0.
 \tag{UG.13}
\]

This is a dimension inequality valid for every chosen smooth complete
intersection here; no rank claim about the multiplication map is needed.
It proves the existence of a nonzero gluing parameter in (UG.11) for the
explicit compensating hull. The resulting \(M\) is actual coherent,
perfect and ordinarily gluable; its character is unchanged by the extension
parameter and is exactly \(522387689472\,v_{1/2}\). It is genuinely
nontensor by section4. Neither indecomposability, a finite action nor weak
semiregularity is asserted.

## 6. What descends, and why a full derived trace is not assumed

Since \(J_S\) acts by zero on both sides of the positive Ext groups,
conjugation by a transition matrix in \(\mathrm{GL}_r(\mathcal A)\)
acts on those groups only through its reduction in
\(\mathrm{GL}_r(\mathcal O_X)\). Consequently the positive self-Ext
sheaves of every (UG.10) are

\[
 \mathcal E xt^q_X(M,M)
 =\operatorname{End}(H|_S)\otimes
       \mathcal E xt^q_X(M_0,M_0),\quad q=1,2.
 \tag{UG.14}
\]

Their ordinary matrix traces therefore give global maps to the corresponding
self-Ext sheaves of \(M_0\). In degree zero, commutativity of \(\mathcal A\)
gives the ordinary bundle trace
\(\mathcal E nd_X(M)=\mathcal E nd_{\mathcal A}(\widetilde H)\to\mathcal A\).

Furthermore \(H^1(S,J_S)=0\). Indeed the restriction resolution of
\(\mathcal O_S(-D)\) has three negative ample line bundles in degrees
\(-2,-1,0\); their cohomology is only in degree four by Mumford's index
theorem, so its first possible hypercohomology degree is two. Thus the trace
of every gluing parameter in (UG.11) is zero in cohomology, and the exact
unit sequence \(1+J_S\to\mathcal O_Y^\times\to\mathcal O_X^\times\)
shows \(\operatorname{Pic}(Y)\to\operatorname{Pic}(X)\) is injective.
The scalar splitting makes it surjective. In particular
\(\det\widetilde H\) is the pullback of \(\det H\).

These facts do **not** establish a partial trace on global derived Ext.
One must still check compatibility with the local-to-global spectral-sequence
differentials and the actual Atiyah/characteristic cocycle. The chain lifts
(UG.7) multiply only up to the explicit homotopies (UG.9); positive cohomology
centrality alone does not supply all their higher compatibilities. The
ordinary partial trace of SF-E823 uses an actual \(\mathcal O_X\)-locally
free tensor factor and cannot simply be imported to a bundle over \(Y\).
The adjoining SF-E824 avoids this full-derived-descent issue by proving
exactly the trace identity for the first overlap obstruction. That separate
argument excludes all the global unit forms constructed here. Neither this
local algebra calculation nor that first-overlap argument assumes dg formality
or an asserted deformation of the hull. Other local models remain outside
the stated theorem.

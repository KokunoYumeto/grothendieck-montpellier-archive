# ALP-LIFT-22: the two prescribed sharp G kernels compose on their actual middle level

Author: GPT-6 Astra Pro, ALP_MACHINE /root/lift_accounting.
Date: 22 November 2026 UTC. Inherited reasoning effort is not exposed.

This result closes a further local gate for the literal m=2 sharp
coupled construction. The raw first G kernel does not require an
intermediate generic projector, an arbitrary translate, or a new
finite Schwartz choice before the second edge. Its actual image
already has the middle level forced by ChIdx.Ok. The prescribed
sharp terminal G kernel is injective on that image. The coupled
Y-variable has only one possible G residue class, so no local
sum over Y can cancel this component.

The result is local at G, with a fixed Haar normalization of the
actual small-theta quotient models. It leaves the globally pinned
quotient scalars, the other places, global Y-summation, and the
exact arithmetic automorphic row lattice separate.

## 1. The literal middle source level

Use LIFT21's notation
\[
 m=2,\quad d=t+1,\quad r=k+1,\quad b=k+d,\quad N=b+d.
 \tag{CG1}
\]
The place is degree one and relative split, with residue
\(\kappa=\mathbf F_q\), \(q\ne11\), and the two actual tame
characters \(\eta_0,\eta_1\) have distinct nontrivial residues.
All source references below use the recovered commit
7cbf7a0c32fca1badf05931879a37c3f8a2b03b4.
Let FS abbreviate
Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean.

For m2=0 the coupled middle index is one. The source forces
\[
             c_1=0,\qquad h_1=1.
 \tag{CG2}
\]
The first is the literal cOf definition; the second is
ChIdx.Ok.last_h (FS1025–1026). Thus the following calculation
does not choose a new intermediate frame.

When c=0, every Ufl in FS468 is the whole space and each
extra coordinate vector eN(n,n+i) is zero. Therefore the
conditions defining R1 are automatic:
\[
  R1=\mathrm{GL}_b,\qquad N1=\{1\},\qquad n1Arg=0,
  \qquad \operatorname{prCat}(1,P,1)=\operatorname{Jat}(1,P).
 \tag{CG3}
\]
The inclusion inX is the identity, proving the last equality
from Cbe and prX. These are the exact definitions FS470–541,
not a hypothesis about a new model.

For the actual sharp flag, Jat is JGsym. Since rS=0,
symIdx is the identity. At c=0 the lattice flag in flagS is
the usual residue prefix flag, except at index k: bd5(k,0,k)=0,
so its lattice is \(qO^b\). The conditions in flagU therefore
give the following exact residue subgroup:
\[
 H^\sharp=
 \left\{\begin{pmatrix}u&A\\0&h\end{pmatrix}:
       u=\operatorname{diag}(u_k,1),\ u_k\in U_k(\kappa),
       A\in M_{k+1,t}(\kappa),\ h\in\mathrm{GL}_t(\kappa)
 \right\}.
 \tag{CG4}
\]

Here are the individual flag checks. For s<k, the condition
on the s-th basis vector makes its diagonal entry one and
its lower entries zero. At s=k it fixes the *entire* column
to e_k because the modified lattice is qO^b. Preservation
of the prefix flag at r=k+1 gives the upper parabolic block
shape. The next listed index is r+t=b and adds no condition;
later indices also add none. Preservation of the ordinary
lattice gives invertibility. Conversely every lift of(CG4)
satisfies these conditions. Thus the local subgroup is the
full inverse image \(J^\sharp\) of \(H^\sharp\).
The flag definitions are FS738–766, with
LevGSym.lean11–13 and its entrywise membership lemma108–141.

The grpG and chrG clauses of ChIdx.Ok (FS1072–1083)
now force the actual middle levG group to be \(H^\sharp\).
The n1Arg part of chiInv is one by(CG3); lamRow on this
group is
\[
        \psi_0\!\left(\sum_{i=0}^{k-2}(u_k)_{i,i+1}\right)
                                          \chi_0(\det h).
 \tag{CG5}
\]
Hence the actual adelic middle type, with the inverse
convention of RecLevel.lean50–52, is
\[
 \lambda^\sharp=
        \psi_{U_k}^{-1}\,\bar\eta_0(\det h).
 \tag{CG6}
\]
All character values are the actual residue values;
the determinant inverse has not been dropped.

This middle type is not the generic ColV1 type.
The source distinction is explicit: ColForms.lean105–114
defines MfV=ColV0, and FS1408–1417 imports that initial
space by startC. The actual coupled kernel uses
midGSD=(chF ... 1).mem (FS1220) and ChKer.cp on that
space (FS1236–1237). In chF the group is FrmG of
L.levG and L.levQ (FS1090–1102). It therefore uses the
type(CG6), not a substituted ColV1. No assertion that
the whole ChIdx.Ok record has been constructed is made.

## 2. The coupled G residue class is forced

The allowed G classes of Y are \(q^{-1}O^b/O^b\).
Before choosing any class, the first sharp raw kernel
reads the matrix \([X,qy]\), by LIFT20(RG4).
Its PhiGS condition fixes the last source column,
which is column k in this specialization, to e_k
in every target row. Therefore
\[
 \PsiAt_{\rm sharp}(X,y)\ne0
       \quad\Longrightarrow\quad qy=e_k\pmod q.
 \tag{CG7}
\]
The diagonal condition fixes the k-th entry; the
special sharp condition fixes all entries above it;
the remaining lower and external-row conditions
fix all entries below it. These include all b
target coordinates.

Thus exactly one G residue class can contribute:
\[
                         y=q^{-1}e_k\pmod{O^b}.
 \tag{CG8}
\]
For that class the first kernel is exactly LIFT20's
\[
 f_U(X)=
 \begin{cases}
    \psi_{U_k}(u),&X\in M_{b,k}(O),\
                       \bar X=[I_k;0]u,\ u\in U_k(\kappa),\\
    0,&\text{otherwise}.
 \end{cases}
 \tag{CG9}
\]
A representative change by an integral vector does
not affect either first or terminal G factor.
The same allowed class is used on both coupled
edges. A local coupled sum over Y therefore
has only this G term. Distinct global Y classes
can still differ at other places; this statement
does not remove their global summation.

## 3. The first raw output is an identity-parabolic section

Let \(\pi_0\) be an actual initial constituent
with unramified cuspidal support and a finite
Steinberg type as in LIFT19/LIFT20. Put
\[
 V_0=\pi_0^{J_0,\psi_{U_k}^{-1}},\qquad
 J_0=\operatorname{red}^{-1}U_k(\kappa),\qquad
 a_q=\operatorname{vol}(J_0)
                =\frac{|U_k(\kappa)|}{|\mathrm{GL}_k(\kappa)|}.
 \tag{CG10}
\]
This is precisely the initial MfV local type. It
contains the explicit nonzero Steinberg generic vector.

The full-rank integral of LIFT21(TG13)–(TG16), now
on the edge k to b with character eta0, identifies
the actual first small theta quotient with
\[
                      \pi_1=
          \operatorname{Ind}_{Q_{(k,d)}}^{\mathrm{GL}_b}
                 (\pi_0\boxtimes\eta_0\det_d).
 \tag{CG11}
\]
Its boundary is excluded exactly as in LIFT21:
after removing eta0, every source inertia line
is the nontrivial residue of eta0 or its inverse.
The induction is irreducible by LIFT19. Thus the
compact integral is a fixed Haar normalization
of the actual quotient, with the same explicit
global-normalization caveat.

Define \(s(v)\) in the compact induced model
to be supported on the identity parabolic cell
\(Q(O)K_b^1\), with
\[
 s(v)\!\left(\begin{pmatrix}A&C\\0&D\end{pmatrix}\right)
                 =\pi_0(A)\eta_0(\det D)v
                         \qquad\text{on }Q(O).
 \tag{CG12}
\]
Here v is \(K_k^1\)-fixed. The expression is
well-defined on the compact cell and extends
to normalized induction by Iwasawa. Its identity
value is v.

The first fixed raw kernel has the exact image
\[
                  {\cal T}_0(f_U,v)=a_q\,s(v)
                                      \qquad(v\in V_0).
 \tag{CG13}
\]
To prove this, its residue columns span only
the standard k-plane. The compact target section
therefore vanishes on every other parabolic
quotient point. At identity the source integral
is supported on J0; the source character is
trivial on its determinant, and
\(\psi_{U_k}(u)\pi_0(u)v=v\). It equals
\(a_qv\). Target parabolic covariance determines
its values on the only remaining cell, yielding
(CG13). No compact projector onto a different
target type was applied.

The image s(v) has precisely(CG6). Indeed
\(H^\sharp\subset Q_{(k,d)}(\kappa)\), and
its Levi entries in that parabolic are u_k
and a block with determinant det h. Right
translation of the identity-cell section thus
acts by \(\psi_{U_k}^{-1}\bar\eta_0(\det h)\).
Its support is preserved since this subgroup
is contained in the parabolic. Therefore
\[
                     s(V_0)\subset
                      \pi_1^{J^\sharp,\lambda^\sharp}.
 \tag{CG14}
\]

For precision, s(v) is invariant under the
joining root \(1+cE_{k-1,k}\), which lies
in the Q radical. A projector requiring
a nontrivial generic character on that root
would kill it. This is an obstruction only
to imposing that different compact type on
this particular output. The actual sharp
coupled middle level is(CG6), so that
projector is not part of the present source
construction.

## 4. The actual terminal raw kernel preserves this exact image

Let \(\Phi^\sharp_y\) be the actual terminal
PhiTop/ftY function with the same class(CG8).
The sharp proof of LIFT21(TG19), (TG22),
and(TG24) uses only the restricted character
of \(J^\sharp\), not an extension to the
larger generic group J. It consequently
applies to every vector in
\(\pi_1^{J^\sharp,\lambda^\sharp}\).
Explicitly its identity integral is
\[
          {\cal T}_1(\Phi_y^\sharp,w)(1)
                            =v_{J^\sharp}w,
     \qquad w\in\pi_1^{J^\sharp,\lambda^\sharp},
 \tag{CG15}
\]
since on Jsharp the raw character times
eta1's source determinant inverse is
lambda-sharp inverse. On every graph-plane
representative h_z it is
\(v_{J^\sharp}\psi_0(-z_k)w\), and it is
zero on the other finite parabolic cells.
The same boundary-rank proof identifies it
with the actual second small theta quotient.

Combining(CG13)–(CG15) proves the exact
composed identity
\[
 \boxed{\quad
  \bigl[{\cal T}_1(\Phi_y^\sharp,
                 {\cal T}_0(f_U,v))(1)\bigr](1)
                         =a_q v_{J^\sharp}v
                          \qquad(v\in V_0).\quad}
 \tag{CG16}
\]
There are two identity evaluations, in the
nested induced models. Since both scalar
volumes are nonzero, the two *fixed raw*
G kernels compose injectively on the whole
initial generic type V0. No local Hecke
rotation, new Schwartz input, or intermediate
projection is required.

The residue class(CG8) is forced by the
first raw kernel, so this is also the
only possible local sharp coupled G term.
This assertion does not replace the
global coupled sum, its mass factors,
or its other-place kernels.

## 5. Exact norms and natural integral content

Put \(n_U=k(k-1)/2\) and use the Gaussian
parabolic indices \({\cal J}_{u,v}(q)\)
defined in LIFT21. The first identity-cell
insertion satisfies
\[
 \|s(v)\|^2={\cal J}_{k,d}(q)^{-1}\|v\|^2,\qquad
 \|f_U\|^2=q^{-bk}|U_k(\kappa)|.
 \tag{CG17}
\]
The raw second factor has
\(\|\Phi^\sharp_y\|^2=q^{-Nb+b}|H^\sharp|\).
The exact composite induced-model norm is
\[
 \boxed{
 \|{\cal T}_1(\Phi^\sharp_y,{\cal T}_0(f_U,v))\|^2
   =\frac{q^b(a_qv_{J^\sharp})^2}
                {{\cal J}_{k,d}(q){\cal J}_{b,d}(q)}
                                                \|v\|^2.}
 \tag{CG18}
\]
The first norm is a single cell of the
compact quotient; the second is the
q^b graph cells of LIFT21. This proves
the formula for every vector in V0,
not only a norm-one test vector.

If both finite raw kernels are unit-normalized,
the squared scaling constant on V0 becomes
\[
 \boxed{
 \frac{q^{bk}|U_k|}
          {|\mathrm{GL}_k(\kappa)|^2{\cal J}_{k,d}(q)}
 \cdot
 \frac{q^{Nb}|H^\sharp|}
          {|\mathrm{GL}_b(\kappa)|^2{\cal J}_{b,d}(q)}.}
 \tag{CG19}
\]
No real selected-polynomial norm, global
class mass, or automorphic quotient scalar
is absorbed into this formula.

Fix an integral finite Steinberg lattice
inside the actual \(\pi_0^{K_k^1}\), and
use its natural finite induced lattices
on both subsequent representations.
Its initial generic intersection is
saturated. The normalized first insertion
\(a_q^{-1}{\cal T}_0(f_U,-)=s\) is integral,
and identity evaluation returns the input.
The normalized second map has only zero
or root-of-unity multiples of that input
among its finite graph values. Consequently
\[
 (a_qv_{J^\sharp})^{-1}
        {\cal T}_1(\Phi_y^\sharp,{\cal T}_0(f_U,-))
 \tag{CG20}
\]
is a primitive saturated injection of
the initial generic lattice into the
second natural induced lattice. The
saturation proof is the identity-evaluation
argument of LIFT21, applied twice; it
uses no integral isotypic averaging.

With the valuation normalized by
\(v_{11}(11)=1\), the exact scalar content
change in these lattices is
\[
 \begin{split}
 v_{11}(a_qv_{J^\sharp})
   &=-\sum_{i=1}^{k}v_{11}(q^i-1)
     -\sum_{i=t+1}^{b}v_{11}(q^i-1),\\
 a_qv_{J^\sharp}
   &=\frac{q^{k(k-1)+(k+1)t}
                       |\mathrm{GL}_t(\kappa)|}
           {|\mathrm{GL}_k(\kappa)|
                       |\mathrm{GL}_b(\kappa)|}.
 \end{split}
 \tag{CG21}
\]
Thus this local raw two-edge map introduces
exactly its displayed Haar denominator
and no hidden additional content on the
natural induced generic lattice.
The comparison with the global arithmetic
row lattice and its period normalization
is still necessary before identifying
this with a DP44 gain.

## 6. Scope

This theorem uses the actual sharp middle
level forced by the source's coupled
ChIdx structure, not the separate
generic ColV1 level. It closes the
two fixed G-edge interaction, including
the local Y-variable, for the m=2 route.
It applies place by place to every
degree-one G prime of a repaired host
once its actual first constituent and
literal stage characters are supplied.

It does not construct the complete
ChIdx.Ok record, prove global nonvanishing
of the sum over all remaining Y data,
calibrate the local quotient maps by one
global pinned theta period, or establish
the row-lattice comparison at11. The
actual T/Q factors and the other places
must be handled with their own tests.
The original quadratic-type wrapper and
other global constructor conditions are
also outside this local calculation.

## 7. Proof checks and references

The actual first raw factor is LIFT20.
The full-rank quotient construction,
published boundary theorem, and sharp
terminal graph values are LIFT21.
Their hypotheses and normalization
limitations are retained. The new source
readings are R1 at c=0, last_h,
grpG/chrG, the precise middle chF
definition, and the distinction between
that space and ColV1.

The finite diagnostic composed_raw_sharp_g_certificate.py
checks the forced class, the modified
middle flag, first-output character,
and the exact norm/content factors.
The author has completed the whole-proof reading,
including the exact middle source definitions,
the unique G residue class, both actual quotient
identifications, the identity-parabolic insertion,
the larger sharp eigenspace, all composed norms,
and the saturated lattice argument. The separate
TSV records its time.

The finite diagnostic passed206 first-class
tests and1,958 middle flag/character tests.
It also checks that the different joining-root
generic projector kills the particular identity
section, while the actual sharp type fixes it.
The displayed Haar content formula gives
local composite valuations -10 at each of the
two K031 G primes for k42,t1759; for the K032
prime pair and k168,t1633 it gives -73 and-184.
These are local model scalars, not global DP44
gains. Small finite geometry cases are diagnostic,
not full admissible Ranks examples.

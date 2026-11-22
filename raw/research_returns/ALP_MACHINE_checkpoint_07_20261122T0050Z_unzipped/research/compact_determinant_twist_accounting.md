# AM-R-008: compact-determinant representatives and the exact cost of an automorphic determinant twist

Author: `/root`, GPT-6 Astra Pro; effort not externally exposed;
ALP_MACHINE, 21 November 2026 UTC.

This result refines AM-R-007 for explicit unitary levels whose determinant images equal the source torus level in ALP-LIFT-10. It does not identify those levels with the target stabilizer of the actual first lift.
It determines the effect of a specified automorphic determinant
character on the integral class-value module and its mass norm. It
does not claim that changing a splitting character preserves the
source's pinned coefficient data or the next theta kernel.

## 1. Exact class representatives

Let \(E=\mathbf Q(\zeta_7)\), (F=E^+),
(G=U(I_n)), \(n\ge2\), and (T=U(1)(E/F)).
Write \(K_0\subset G(\mathbb A_{F,f})\) for the full stabilizer
of the standard Hermitian lattice and \(K_{T,0}=\det K_0\).
For (M=29^e), \(e\ge1\), define \(K\subset K_0\) by:

- at each of the three places over 29, \(g\equiv I_n\pmod{29^e}\);
- at the ramified place over 7, the residue of \(\det g\) is (+1);
- at every other finite place, \(g\in K_{0,v}\).

This is a normal subgroup of \(K_0\). Its determinant image is exactly
the torus subgroup \(K_M\) of ALP-LIFT-10, equation (O21). Inclusion
in that subgroup follows from the definitions. For the reverse
inclusion, the section \(t\mapsto\operatorname{diag}(t,1,\ldots,1)\)
belongs to the indicated group level whenever \(t\in K_M\).

Choose representatives \(a\in K_{T,0}\) for the finite quotient

\[
\mathcal A=K_{T,0}/(\mu_{14}K_M).
\tag{R8.1}
\]

Each representative can be chosen to be 1 outside 7 and 29, since
the local factors of \(K_M\) equal (K_{T,0,v}) elsewhere. Put
\(s(a)=\operatorname{diag}(a,1,\ldots,1)\in K_0\). Then

\[
\boxed{
G(\mathbb A_{F,f})
 =\bigcup_{a\in\mathcal A}G(F)\,SU(I_n)(F_{v_{11}})\,s(a)K .}
\tag{R8.2}
\]

Thus every finite lattice class has a representative whose determinant
is a compact norm-one idele supported at 7 and 29. Noncompact motion
may be confined to the determinant-one group at 11. The set in
(R8.2) need not be a disjoint union, and the theorem does not give a
bound for the determinant-one matrix at 11.

### Proof

ALP-LIFT-09 proves \(T(\mathbb A_{F,f})=T(F)K_{T,0}\), with
\(T(F)\cap K_{T,0}=\mu_{14}\). For \(g\in G(\mathbb A_{F,f})\),
write

\[
\det g=t_0\,a\,k_T,
\qquad t_0\in T(F),\quad a\in\mathcal A,\quad k_T\in K_M.
\tag{R8.3}
\]

The root of unity needed to choose \(a\) is absorbed in \(t_0\).
Lift \(k_T\) to \(k\in K\) by the determinant section, and set

\[
h=s(t_0)^{-1}gk^{-1}s(a)^{-1}\in SU(I_n)(\mathbb A_{F,f}).
\tag{R8.4}
\]

The strong approximation argument of AM-R-007, with the omitted
split place (v_{11}), gives

\[
h=\delta u_{11}k_1,
\qquad \delta\in SU(I_n)(F),\quad
u_{11}\in SU(I_n)(F_{v_{11}}),\quad k_1\in K\cap SU(I_n)(\mathbb A_{F,f}).
\tag{R8.5}
\]

In the more general proof one uses the conjugate of \(K\) by (s\(a\)).
Here it is the same subgroup because \(s(a)\in K_0\) and \(K\) is
normal in \(K_0\). Substituting (R8.5) in (R8.4), with the factors
in their actual order, gives

\[
g=s(t_0)\delta\,u_{11}s(a)\,
       \bigl(s(a)^{-1}k_1s(a)\bigr)k.
\tag{R8.6}
\]

The last factors lie in \(K\), proving (R8.2). The determinant of
(u_{11}s\(a\)) is \(a\), so it is compact. This proves every
assertion about the representatives.

### Extension to any compatible target compact level

Let \(K\) now be any open compact subgroup of \(K_0\), and set
\(D=\det K\). The group \(D\) is open in \(K_{T,0}\): the
preimage of \(K\) under the continuous local determinant section
is an open neighborhood of 1 contained in \(D\).
Choose representatives \(a\) of \(K_{T,0}/(\mu_{14}D)\).
The same conclusion (R8.2) holds with these representatives and
this \(K\), without a normality assumption.

To prove it, write \(\det g=t_0ak_D\), and choose \(k\in K\)
with \(\det k=k_D\). This lift exists by the definition of \(D\);
it need not be the diagonal section. Set \(h\) as in (R8.4).
Apply strong approximation to the actual conjugated compact
\[
 L=s(a)Ks(a)^{-1}\cap SU(I_n)(\mathbb A_{F,f}).
 \tag{R8.16}
\]
It gives \(h=\delta u_{11}\ell\), with \(\ell\in L\).
The exact factor order is then
\[
 g=s(t_0)\delta\,u_{11}s(a)
                \bigl(s(a)^{-1}\ell s(a)\bigr)k.
 \tag{R8.17}
\]
The last two factors belong to \(K\). This proves the assertion.
The representatives still have compact determinant; their support
need not be confined to 7 and 29.

Every assertion of section 2 consequently holds with \(D\) in place
of \(K_M\), provided \(\gamma_f|_D=1\). This supplies the exact
twist isometry for any compatible actual target level. Refining a
given level to make it compatible is a different operation; its
index and norm conventions must still be retained. This extension
was supplied and whole-proof checked by /root/lift_accounting in
agents/review_root_compact_twist.md and read in full by /root.

## 2. Exact integral and metric effect of a determinant character

Let \(\gamma=\gamma_\infty\gamma_f\) be a continuous unitary
automorphic character of \(T(F)\backslash T(\mathbb A_F)\), and
assume

\[
\gamma_f|_{K_M}=1.
\tag{R8.7}
\]

Fix a finite set (g_i=u_i s(a_i)) of representatives of the
class set used to present the automorphic space. Formula (R8.2)
allows that choice for every class. No new class-number or mass
formula is assumed in making this choice. Put

\[
\Gamma_i=G(F)\cap g_iKg_i^{-1}.
\tag{R8.8}
\]

For a positive definite unitary group these stabilizers are finite:
the corresponding rational matrices preserve a fixed integral lattice,
and their real embeddings lie in a compact group. A discrete lattice
in the resulting finite-dimensional real matrix space meets a compact
set in a finite set. This supplies the elementary stabilizer finiteness
used below.

To avoid an implicit convention change, present coefficient-valued
automorphic forms as functions satisfying

\[
f(\delta gk)=\rho(\delta_\infty)f(g),
\qquad \delta\in G(F),\quad k\in K.
\tag{R8.9}
\]

Define

\[
f^{\gamma}(g)=\gamma_f(\det g)f(g),\qquad
\rho^{\gamma}(z)=\gamma_\infty(\det z)^{-1}\rho(z).
\tag{R8.10}
\]

Then \(f^\gamma\) satisfies (R8.9) with \(\rho^\gamma\).
Indeed \(\gamma_f(\det k)=1\) by (R8.7), while rational
triviality of the global character gives

\[
\gamma_f(\det\delta)=\gamma_\infty(\det\delta_\infty)^{-1}.
\tag{R8.11}
\]

For \(\delta\in\Gamma_i\), its finite determinant belongs to
\(K_M\), because conjugation does not change a determinant. Equations
(R8.7)–(R8.11) therefore imply

\[
\gamma_\infty(\det\delta_\infty)=1,
\qquad V^{\Gamma_i}_{\rho}=V^{\Gamma_i}_{\rho^\gamma}.
\tag{R8.12}
\]

These are equal subspaces in the same underlying coefficient vector
space, not just spaces with equal dimensions. On class values the map
is the diagonal matrix

\[
\bigl(f(g_i)\bigr)_i\longmapsto
       \bigl(\gamma_f(a_i)f(g_i)\bigr)_i.
\tag{R8.13}
\]

Every \(\gamma_f(a_i)\) is a root of unity. The image of the compact
group (K_{T,0}) under a smooth character is finite: its kernel is
open and hence has finite index. In particular the displayed scalar
is an algebraic unit at every finite place and has absolute value one
under every complex embedding.

Let \(\mathcal V\subset V\) be the specified coefficient lattice
over a number ring containing these finitely many roots of unity.
Use the same underlying lattice for the twisted coefficient space.
Then (R8.12)–(R8.13) give an exact isomorphism

\[
\boxed{
\bigoplus_i\mathcal V^{\Gamma_i}_{\rho}
\ \xrightarrow{\ \sim\ }
\bigoplus_i\mathcal V^{\Gamma_i}_{\rho^\gamma}.}
\tag{R8.14}
\]

No denominator is introduced. All local contents of a vector are
preserved, including those at 2, 7, 11 and 29. The same statement
holds for a specified submodule transported by this actual map; it
does not identify that transported submodule with an independently
prescribed arithmetic row.

With any fixed Hermitian metric on \(V\), the character is unitary
and the underlying metric may be used unchanged. Thus the map is
also an exact isometry for the class mass norm

\[
\|f\|_{\rm mass}^2
   =\sum_i w_i\|f(g_i)\|^2,
\qquad w_i>0,
\tag{R8.15}
\]

including \(w_i=|\Gamma_i|^{-1}\) and any fixed common Haar
normalization. It preserves the class-value supremum norm as well.
There is no added logarithmic norm or denominator cost for this
specified twist map in this presentation.

## 3. Scope of the zero-cost statement

The subgroup K_M in ALP-LIFT-10 is a source torus stabilizer. The target U(2) stabilizer, its index and its mass have not thereby been computed. The theorem here applies to the displayed U(n) level once a vector belongs to its class module; that membership is an additional hypothesis for any first-lift application. Independently of a finite class presentation, multiplication by a unitary determinant character preserves the scalar automorphic L2 norm. A refinement to a compatible target level must still retain the cost of that refinement.


The result removes a possible artificial height penalty coming from
poorly normalized representatives of a determinant twist. It does
not make a change of theta datum free in every other sense. The
splitting characters, archimedean coefficient representation and
source covariance pins have changed. To use the twist in a proposed
lift chain, one must show that the new theta kernel has precisely
these input/output characters, that the prescribed row submodules
are the transported submodules in (R8.14), and that the subsequent
pairing is nonzero. None of those assertions follows from an
isometry of the ambient class-value modules.

There is also no new equality between the \(E\)-host first lifts
and AM-DO-022's \(E'=\mathbf Q(\zeta_{28})\)-host kernels. The
present theorem stays over \(E\). Applying it over \(E'\) would
require the corresponding torus class calculation and compact
determinant presentation; the old proof is not silently transplanted.

The geometric object is an associated coefficient bundle on the
finite class presentation of a definite unitary quotient. Tensoring
its representation by a rank-one character is an operation in the
representation Grothendieck group, but (R8.13)–(R8.14) are actual
integral maps with a metric, stronger than a virtual-class identity.
The framework locators are SGA 3 I, 4.7.2–4.7.3 and SGA 6 VI,
Theorem 3.3, as carried in the geometric dictionary. The arithmetic
input is ALP-LIFT-09 (V2–V6), and the approximation theorem is the
same Rapinchuk (2013), Theorem 2.3, p. 281, used in AM-R-007.

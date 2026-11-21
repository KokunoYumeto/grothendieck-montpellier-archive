# SF-E824: the first overlap obstruction excludes every global unit form

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** Complete proof independently whole-reviewed by /root and
/root/imprimitive on 21 November 2026; both mathematical/source reviews PASS.
Author and reviewers: GPT-6 Astra Pro, inherited effort not exposed.
Reviewed draft SHA-256:
`f42a0232fbbcfbd21a1aa66516888b3d142658d7b3d1aff16c27df7d3f8c1ffe`.
This uses a trace only on the first overlap obstruction, not an unproved trace
on global derived Ext. The complete local algebra and actual nontensor family
are proved in the adjoining unit-gluing analysis, independently reviewed in
full by the same two reviewers.

## 1. Statement

Let \(X\) be a complex abelian fourfold with the balanced RM data of
SF-E823. Let \(D=k\theta\) be an integral ample divisor, \(k>0\), and
let \(S\) be a smooth complete intersection of two divisors in \(|D|\).
Let \(F=M_0\) be the actual unit extension

\[
 0\to\mathcal O_S(-2D)\to F\to I_S\to0,
 \qquad \operatorname{ch}(F)=1-2D^3+4D^4.
 \tag{E824.1}
\]

Suppose \(M\) is a coherent sheaf locally isomorphic to \(F^{\oplus r}\),
with \(r>0\), and

\[
 e^B\operatorname{ch}(M)=r v_q,
 \qquad B\in\operatorname{NS}(X)_{\mathbf Q},\quad q>0.
 \tag{E824.2}
\]

Then \(M\) is not weakly semiregular for any specified effective coherent
finite translation/tensor action of supplied S21. This covers all global
unit forms, including the actual nontensor extensions constructed in the
adjoining analysis. It assumes no global tensor factor, simplicity, stability,
or equivariant decomposition.

The local algebra already proved there is

\[
 \mathcal A=\mathcal E nd(F)=\mathcal O_X\oplus i_*J,
 \quad J=\mathcal O_S(-D)^2,\quad J^2=0,
 \tag{E824.3}
\]

and \(\mathcal B=\mathcal E xt^1(F,F)=i_*\mathcal O_S(D)^4\).
The two actions of \(\mathcal A\) on \(\mathcal B\) agree and factor
through \(\mathcal O_S\); in particular \(J\) acts by zero on both
sides. Also \(\mathcal E xt^j(F,F)=0\) for \(j>2\).

## 2. The first obstruction class and its exact filtration meaning

Fix an invariant holomorphic bivector \(\pi\). The first-order sheaf of
algebras

\[
 \mathcal O_{X,\pi}=\mathcal O_X\oplus\varepsilon\mathcal O_X,
 \qquad a*b=ab+\tfrac{\varepsilon}{2}\pi(da,db),
 \quad\varepsilon^2=0,
 \tag{E824.4}
\]

is defined globally. It is associative to this order by the biderivation
identity. The explicit local homotopies of the compensation construction give
flat local module deformations of \(F\), and hence of \(M\).

For \(N=F\) or a local form of \(F^{\oplus r}\), set
\(C_N=R\mathcal H om(N,N)\). Its local characteristic class is zero, so
\(\rho_N(\pi)\in\operatorname{Ext}^2(N,N)\) belongs to the first
filtration piece \(F^1\), the kernel of its map to
\(H^0(\mathcal E xt^2(N,N))\). The truncation triangles

\[
 \tau_{\le1}C_N\to C_N\to\mathcal E xt^2(N,N)[-2],
 \qquad
 \mathcal E nd(N)\to\tau_{\le1}C_N
                   \to\mathcal E xt^1(N,N)[-1]
 \tag{E824.5}
\]

give a canonical map

\[
 F^1\longrightarrow H^1(\mathcal E xt^1(N,N)),
 \tag{E824.6}
\]

whose kernel is the image of \(H^2(\mathcal E nd(N))\). Indeed the first
triangle identifies \(H^2(\tau_{\le1}C_N)\) with \(F^1\), since the
preceding group is \(H^{-1}(\mathcal E xt^2)=0\); the assertion then
follows from the second triangle. Write \(\kappa_N(\pi)\) for the image
of \(\rho_N(\pi)\) under (E824.6).

This class has a direct overlap interpretation. Choose local deformations
\(N_{i,\varepsilon}\) on an affine or sufficiently small analytic cover.
On each intersection, the obstruction to lifting the original transition
isomorphism is an element of the local \(\operatorname{Ext}^1\) sheaf.
The resulting Čech one-cocycle represents \(\kappa_N(\pi)\). To check
this identification, represent \(\rho_N(\pi)\) in a Čech resolution of
the self-Hom complex. The local nullhomotopies remove its Čech-degree-zero,
internal-degree-two component. The remaining degree-(1,1) component is the
difference of those nullhomotopies after transition; its class is exactly
the morphism-lifting obstruction. The total cocycle equation makes it a
Čech cocycle modulo internal boundaries. This is precisely the map from
the two truncation triangles, and uses no degeneration of a spectral sequence.

## 3. The unit module has a nonzero first obstruction

Let \(\pi=\pi_+\), and put
\(\eta_+=\pi_+\mathbin{\lrcorner}(\theta_+^2/2)\). The degree-one
component of the full semiregularity morphism is a derived map

\[
 \sigma_F^1:C_F\longrightarrow\Omega_X^1[1],
\]

inducing \(\operatorname{Ext}^2(F,F)\to H^3(\Omega_X^1)\). Its
restriction along \(\mathcal E nd(F)\to C_F\) is zero. On the scalar
summand \(\mathcal O_X\) of (E824.3), that restriction is
\(\operatorname{ch}_1(F)=0\). On \(i_*J\), the target morphism group is
\(\operatorname{Ext}^1_X(i_*J,\Omega_X^1)=0\): the two-element Koszul
resolution of the regular immersion gives local Hom and local Ext-one
equal to zero against the locally free target, and thus the global group
is also zero. This last assertion follows directly from the low-degree
local-to-global Ext sequence; neither possible total-degree-one term
survives.

It follows that \(\sigma_F^1\) kills the image of
\(H^2(\mathcal E nd(F))\). But published BF gives

\[
 \sigma_F^1\rho_F(\pi_+)
    =\pi_+\mathbin{\lrcorner}\operatorname{ch}_3(F)
    =-12k^3\eta_+\theta_-\ne0,
 \tag{E824.7}
\]

with exactly the normalization checked in SF-E823. Since
\(\rho_F(\pi_+)\) is locally zero, (E824.5)--(E824.6) now show

\[
 \kappa_F(\pi_+)\ne0
       \quad\hbox{in }H^1(X,\mathcal B).
 \tag{E824.8}
\]

This proves nonvanishing of the specific first overlap class, not just of
an unspecified global Ext class.

## 4. The endomorphism-lifting derivation

We give the exact first-order algebra needed for the trace. Work on a small
open set and pass to its affine section modules, or work on stalks. Choose
one local deformation of \(F\), and choose a splitting of its reduction
as a complex vector space; flatness identifies the underlying dual-number
module with \(F\oplus\varepsilon F\). No global or
\(\mathcal O_X\)-linear splitting is being assumed. Write its action as
\(\rho_0+\varepsilon\rho_1\). For \(a\in\mathcal A\), the obstruction
to lifting the endomorphism \(a\) is represented in the bar Ext-one
complex by

\[
 r\longmapsto a\rho_1(r)-\rho_1(r)a.
 \tag{E824.9}
\]

It is a one-cocycle because the two associativity equations have the same
fixed multiplication perturbation (E824.4), which commutes with the original
\(R\)-linear endomorphism. Changing a lift of the endomorphism adds a bar
boundary. Changing the module deformation changes (E824.9) by
\(a\beta-\beta a\), where \(\beta\in\mathcal B\) is the difference
class of the two deformations. This change is zero in \(\mathcal B\),
by its central \(\mathcal A\)-module structure.

Consequently (E824.9) defines a **global**, choice-independent derivation of
sheaves of complex vector spaces

\[
 \partial_\pi:\mathcal A\longrightarrow\mathcal B,
 \qquad
 \partial_\pi(ab)=a\partial_\pi(b)+\partial_\pi(a)b.
 \tag{E824.10}
\]

The Leibniz equation follows by expanding the commutator with \(ab\).
This derivation need not be \(\mathcal O_X\)-linear. It kills complex
constants, which is the property used below. Formula (E824.9) may be made
using any linear splitting; the boundary and difference-class calculations
show that its Ext class is independent of that choice.

## 5. The normalized matrix overlap formula

Choose local identifications \(M|_{U_i}=F|_{U_i}^{\oplus r}\), with
transition matrices \(G_{ij}\in\mathrm{GL}_r(\mathcal A)\). Their
reductions define the locally free hull \(H=M^{\vee\vee}\). Choose
local deformations \(F_{i,\varepsilon}\), and use their direct sums for
\(M\). Let \(k_{ij}\in\mathcal B\) be the obstruction to lifting the
identity between the two local deformations of \(F\), with the sign
chosen as \(\rho_{1,i}-\rho_{1,j}\). Use this same Čech sign in
(E824.6); reversing all overlap signs changes neither vanishing nor the
trace argument.

The obstruction to lifting \(G_{ij}\), normalized back into the source
endomorphism group by multiplication by \(G_{ij}^{-1}\), is

\[
 k_{ij} I_r+G_{ij}^{-1}\partial_\pi(G_{ij}).
 \tag{E824.11}
\]

Indeed its bar cochain is
\(G\rho_{1,i}-\rho_{1,j}G
=(G\rho_{1,i}-\rho_{1,i}G)+(\rho_{1,i}-\rho_{1,j})G\).
The centrality of \(\mathcal B\) makes conjugation of the second term
by \(G\) trivial. This proves (E824.11) as an Ext-one identity; it is
not an assertion that the matrices lift or satisfy higher descent equations.

Since \(\mathcal A\) is commutative and \(\mathcal B\) is a central
module, the usual polynomial determinant identity is valid for the derivation
(E824.10):

\[
 \operatorname{tr}(G^{-1}\partial_\pi G)
       =\det(G)^{-1}\partial_\pi(\det G).
 \tag{E824.12}
\]

For completeness, differentiate the permutation expansion of \(\det G\).
Each differentiated entry has its signed cofactor; their sum is
\(\operatorname{tr}(\operatorname{adj}(G)\partial_\pi G)\).
Multiply by the inverse determinant. Centrality permits the required
reordering of the undifferentiated entries with the module-valued derivative.

The positive self-Ext sheaf of \(M\) is
\(\operatorname{End}(H|_S)\otimes\mathcal B\), as proved in the adjoining
analysis. Hence its ordinary matrix trace is a globally defined sheaf map.
Taking Čech cohomology of (E824.11)--(E824.12) gives

\[
 \operatorname{tr}\kappa_M(\pi)
     =r\kappa_F(\pi)
       +[\det(G_{ij})^{-1}\partial_\pi(\det G_{ij})]
       \quad\hbox{in }H^1(X,\mathcal B).
 \tag{E824.13}
\]

This is the only trace descent required in the proof.

## 6. The determinant correction vanishes when the hull has zero first Chern class

Let \(Y=(X,\mathcal A)\). The adjoining analysis proves
\(H^1(S,J)=0\) by the negative-ample Koszul resolution and the published
Mumford index theorem. The split unit sequence
\(1+J\to\mathcal A^\times\to\mathcal O_X^\times\), with
\(1+J\simeq J\), therefore gives
\(\operatorname{Pic}(Y)\simeq\operatorname{Pic}(X)\). The determinant
of the \(\mathcal A\)-bundle with transition matrices \(G_{ij}\) is
accordingly the pullback of \(\det H\).

If \(c_1(H)=0\), the line bundle \(\det H\in\operatorname{Pic}^0(X)\)
has a flat unitary description, so has locally constant complex transition
functions on a sufficiently fine analytic cover. Here is the elementary
Hodge justification: the exponential sequence identifies \(\operatorname{Pic}^0\)
with \(H^1(\mathcal O_X)/H^1(X,\mathbf Z)\); projection of purely
imaginary real harmonic one-forms onto type \((0,1)\) is an isomorphism
of real vector spaces. A representative is therefore a flat unitary
connection on the corresponding line bundle. The integral cohomology of an
abelian variety is torsion-free, so zero rational first Chern class gives
exactly this \(\operatorname{Pic}^0\) case.

After changing local determinant frames in \(\mathcal A^\times\), the
cocycle \(\det G_{ij}\) is thus represented by constants. The derivation
\(\partial_\pi\) kills them. A change of frame changes the logarithmic
derivative by a Čech coboundary, by the ordinary Leibniz rule. Consequently

\[
 [\det(G_{ij})^{-1}\partial_\pi(\det G_{ij})]=0,
 \qquad
 \operatorname{tr}\kappa_M(\pi)=r\kappa_F(\pi).
 \tag{E824.14}
\]

## 7. Contradiction for B zero

Suppose first that \(B=0\) in (E824.2). The unit form has the same
rank and first Chern class as its hull \(H\): in its hull sequence the
torsion and defect are supported in codimension two, so their first Chern
characters vanish. Thus \(c_1(H)=c_1(M)=0\), and (E824.14) applies.

The balanced cap kernel contains \(\xi_+=\pi_++q\eta_+\). Weak
semiregularity, published BF composition, and supplied S21 invariant/forgetting
compatibility give \(\rho_M(\xi_+)=0\) in ordinary Ext. The second
term \(q\eta_+\operatorname{id}_M\) comes from
\(H^2(\mathcal E nd(M))\), so its first overlap class is zero by
(E824.5)--(E824.6). Therefore \(\kappa_M(\pi_+)=0\).
Taking its trace and using (E824.14) contradicts
\(r\kappa_F(\pi_+)\ne0\) from (E824.8).

## 8. Rational B without assuming semiregularity survives an isogeny

For general rational algebraic \(B\), choose a positive integer \(m\)
such that \([m]^*B=m^2B\) is the first Chern class of a line bundle
\(L_B\). Write \(f=[m]\), \(X'=X\), and

\[
 M'=f^*M\otimes L_B,
 \qquad F'=f^*F,
 \qquad D'=f^*D,\quad\theta'=f^*\theta.
 \tag{E824.15}
\]

The map is finite étale. The pullback surface is smooth, and its negative-ample
Koszul resolution gives \(H^0(\mathcal O_{S'})=\mathbf C\), so it is
connected and hence integral. The pullback unit extension is exactly the same
unit construction for \(D'\); tensoring by a line bundle preserves the
property of being locally a direct sum of \(F'\). Its new hull is
\(H'=f^*H\otimes L_B\), with \(c_1(H')=0\), and
\(\operatorname{ch}(M')=r v_q(\theta'_+,\theta'_-)\).

It remains to justify the vanishing needed for section7, rather than asserting
any preservation of semiregularity. Use the étale pullback bivector
\(\pi'_+=m^{-2}\pi_+\); since \(\theta'_\pm=m^2\theta_\pm\),

\[
 \eta'_+=\pi'_+\mathbin{\lrcorner}(\theta_+'{}^2/2)
         =m^2\eta_+=f^*\eta_+.
 \tag{E824.16}
\]

Atiyah classes pull back under an étale map, and tensoring by \(L_B\)
adds \(f^*B\operatorname{id}\). The exact B-shear evaluation formula
of SF-E823 consequently identifies
\(\rho_{M'}(\pi'_++q\eta'_+)\) with the pullback of
\(\rho_M(\xi_B)\), under the line-tensor identification of self-Ext.
The latter is zero by the original weak semiregularity assumption and the
balanced kernel. Thus the ordinary vanishing used in section7 holds on
\(X'\), and the same contradiction follows there. No finite action is
transported and no injectivity of a pulled-back semiregularity map is assumed.

## 9. Scope

The argument excludes every global form locally isomorphic to the full-rank
unit module \(M_0^r\) on a smooth ample two-divisor complete intersection.
It therefore closes the non-tensor gluing escape for this particular local
model. It does not assert the same result for an added locally free summand,
different torsion or quotient ranks, an extension matrix with zeros, singular
or nonreduced support, different degree twists, or arbitrary perfect complexes.
The genuine remaining seed gate is preserved in those other scopes.

The only derived filtration used is explicitly (E824.5). Matrix trace on the
first positive Ext sheaf, the endomorphism-lifting derivation and the determinant
identity suffice. A trace on the entire derived endomorphism complex is neither
constructed nor needed.

## 10. Exact source and check scope

The ordinary characteristic/trace identities are the directly published
Buchweitz--Flenner2008 inputs located in SF-E823: author-copy Theorem5.1.3,
Proposition5.2.2 and Corollary5.2.3, pp24--27, and Proposition6.2.1,
Corollary6.3.2, Theorem6.4.2 with Proposition6.4.4, pp29--33. The complete
invoked proofs were read in the preceding checks; no fresh whole-paper audit
is asserted here. The first-overlap, derivation, determinant and truncation
arguments are proved completely above. Supplied DEG_L S21 equation(S21.6),
the paragraph following(S21.7), and the invariant-evaluation paragraph before
(S21.8) are used only for coherent invariant/forgetting compatibility. The
negative-ample vanishing and explicit parameter construction use the published
Mumford section16 source exactly located in the adjoining analysis. No new
unrefereed theorem or all-order deformation assertion is used.

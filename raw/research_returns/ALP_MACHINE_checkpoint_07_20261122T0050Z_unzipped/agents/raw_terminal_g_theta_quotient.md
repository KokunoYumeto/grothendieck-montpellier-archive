# ALP-LIFT-21: the raw terminal G factor survives the actual previous theta constituent

Author: GPT-6 Astra Pro, ALP_MACHINE /root/lift_accounting.
Date: 22 November 2026 UTC. Inherited reasoning effort is not exposed.
The rank-filtration reduction in section4 was suggested independently
by /root while the explicit full-rank intertwiner was being derived.

This theorem concerns the actual terminal local G factor of
XiCpl2 for m=2, with the same allowed coupled class used in
LIFT20. It proves nonvanishing in the actual small theta quotient
of each LIFT19 first constituent. It proves more than occurrence
of a compatible compact type: the fixed raw terminal Schwartz
vector is injective on the entire prescribed first-column type.
In a specified Haar-normalized induced model its norm and its
effect on a natural integral coefficient lattice are computed.

The normalization of that local induced model is explicit. Its
comparison with a globally pinned automorphic coefficient model
is not supplied by uniqueness of the local theta correspondence.
No assertion about the final MainX row, all six AdmS identities,
or the full DP44 cost follows merely from the local theorem.

## 1. Ranks, actual raw factor, and its compact groups

Fix a degree-one relative split G place of residue characteristic
different from11. Write \(F_v\) for its local field, \(O\) for its
ring of integers, and \(\kappa=\mathbf F_q\) for its residue field,
with the rational prime \(q\) a uniformizer. Normalize multiplicative
Haar measure by \(\operatorname{vol}(\mathrm{GL}_n(O))=1\), and
additive matrix measure by \(\operatorname{vol}(M_{u,v}(O))=1\).

Take the literal source ranks with \(m=2\). Put

\[
 d=t+1,\quad r=k+1,\quad b=k+d=r+t,\quad N=b+d=k+2d.
 \tag{TG1}
\]

Thus the terminal edge is \(U(b)\to U(N)\). Every actual Ranks
datum has enough coordinates for the following blocks. The
argument uses \(t\ge1\), so in particular applies to the larger
values required by the source.

The source locators are relative to the pinned recovered tree
work/research/alpoge_source, commit
7cbf7a0c32fca1badf05931879a37c3f8a2b03b4:

* Formalism/LocalRingCardinality/Params.lean, definitions of
  r, N, rS, and cOf in the column file.
* Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean
  (FS), PhiG/PhiGS780–810, PhiTop1141–1147,
  ftY1150–1155, and XiCpl2 1160–1167.
* Development/AbelianVarietyTheory/Definitions/GlobalTwisting/IntegralGLSuccEmbeddingMemParahoricTimesPrincipa.lean,
  entB_top420–441 and the terminal rank identity.
* Checked DO031, equations(DO31.1)–(DO31.5), identifies
  those exact raw functions and their actual terminal frames.

No Lean execution is claimed. We use the definitions and the
proved finite model in DO031 with its stated scope.

Write a terminal matrix in its actual local frames as

\[
 X=\begin{pmatrix}Z\\ \ell\end{pmatrix}\in M_{N,b}(F_v),
 \qquad Z\in M_{N-1,b}(F_v),\quad \ell\in M_{1,b}(F_v).
 \tag{TG2}
\]

The terminal top function has no remaining auxiliary-column
power: cOf(m-1)=0, so entB_top makes it read \(Z\) itself.
The last-row factor is the actual integral character function
in DO31.4. In the convention of that equation it is

\[
             1_{O^b}(\ell)\psi_v(-\ell y),\qquad
                y\equiv q^{-1}e_k\pmod{O^b}.
 \tag{TG3}
\]

The class of \(y\) is exactly LIFT20(RG3), now in the rank-b
middle space. If the last row is instead written before the
source's piT unit rescaling, a fixed unit multiplies the
argument in(TG3). Every proof below keeps the resulting root
of unity, and all support, norm, and content assertions are
unchanged. We use DO031's already-rescaled convention.

Let \(\eta_0,\eta_1\) be the actual tame selected-half characters
on the first and second edges. Their residue characters are
nontrivial and distinct, and the literal pin is
\(\bar\eta_i=\chi_i^{-1}\). Denote the finite groups

\[
 \begin{split}
 H&=\left\{
   \begin{pmatrix}u&A\\0&h\end{pmatrix}:
       u\in U_r(\kappa),\ A\in M_{r,t}(\kappa),\
       h\in\mathrm{GL}_t(\kappa)\right\},\\
 H^\sharp&=\{g\in H:g e_k=e_k\}.
 \end{split}
 \tag{TG4}
\]

The index \(k\) is zero-based, so it is the last of the first
\(r=k+1\) coordinates. Thus \(H^\sharp\) has
\(u=\operatorname{diag}(u_k,1)\), with \(u_k\in U_k\),
while \(A,h\) are unchanged. Write \(J,J^\sharp\) for their
inverse images in \(\mathrm{GL}_b(O)\). Their cardinalities
and Haar volumes are

\[
 \begin{split}
 h_q&=|H|=q^{r(r-1)/2+rt}|\mathrm{GL}_t(\kappa)|,\\
 h_q^\sharp&=q^{-k}h_q,\qquad
 v_J=\frac{h_q}{|\mathrm{GL}_b(\kappa)|},\qquad
 v_{J^\sharp}=q^{-k}v_J.
 \end{split}
 \tag{TG5}
\]

Put

\[
 \lambda(g)=
   \psi_0\!\left(-\sum_{i=0}^{r-2}u_{i,i+1}\right)
                         \bar\eta_0(\det h)\qquad(g\in H).
 \tag{TG6}
\]

This is exactly the inverse adelic first-column character
from LIFT19(T1)–(T5), in the \(j=1=m-1\) fully generic branch.
The source RecLevel.lean50–52 gives the inverse convention.
We use the same notation for its inflation to \(J\) and its
restriction to \(J^\sharp\).

### Exact raw support and phase

Let \(\Phi,\Phi^\sharp\) denote the actual nonsharp and sharp
terminal local factors, including(TG3). They vanish unless
\(X\) is integral and, modulo \(q\), has the form

\[
 \bar X=\begin{pmatrix}B\\0_{(d-1)\times b}\\w\end{pmatrix},
 \qquad
 B=\begin{pmatrix}u&A\\0&h\end{pmatrix}\in H
       \text{ or }H^\sharp,\qquad w\in\kappa^b.
 \tag{TG7}
\]

On that support,

\[
 \begin{split}
 \Phi(X)&=
  \psi_0\!\left(\sum_{i=0}^{r-2}u_{i,i+1}-w_k\right)
                       (\bar\eta_1\bar\eta_0^{-1})(\det h),\\
 \Phi^\sharp(X)&=
  \psi_0\!\left(\sum_{i=0}^{k-2}u_{i,i+1}-w_k\right)
                       (\bar\eta_1\bar\eta_0^{-1})(\det h).
 \end{split}
 \tag{TG8}
\]

An empty sum is zero. For the source ranks the sums are
nonempty; this convention also gives the small diagnostic.

We verify the raw predicates. In PhiTop the internal
variable a=r+(m-1)t is \(b\), the full source width. Its
integrality condition makes every entry of \(Z\) integral.
The subsequent row condition makes the rows below its
first \(b\) rows zero modulo \(q\). The first \(r\) columns
have unitriangular leading block and zeros below. The
remaining \(t\) columns give an arbitrary upper-right
rectangle and a square bottom-right block. If its
determinant is zero, unitV and its inverse give zero,
so the function vanishes. Otherwise that block is \(h\)
in(TG7).

For rS=0, symIdx k 0 is the identity. The additional
PhiGS condition fixes column \(k\) to \(e_k\), precisely
\(H^\sharp\). The determinant term is
\(\chi_0(\det h)\chi_1(\det B)^{-1}\), with
\(\det B=\det h\), giving the factor in(TG8).
The additive term is the full \(U_r\) character for
PhiG; in PhiGS it is the \(U_k\) character because its
second root sum has length r-k-1=0. Finally(TG3)
contributes \(\psi_0(-w_k)\). Changing \(y\) by an
integral vector does not affect it. This proves(TG7)–(TG8)
from the actual raw definitions.

Both functions are therefore supported in the full-rank
open subset of \(M_{N,b}(F_v)\): the leading \(b\) by \(b\)
minor is a unit. Their support is compact in that open set.
They are fixed by the target principal congruence \(K_N^1\).
Indeed its determinant character is trivial and it changes
integral matrix entries only modulo \(q\).

Their exact additive Schwartz norms are

\[
 \Gamma_{\rm raw}=q^{-Nb+b}h_q,\qquad
 \Gamma_{\rm raw}^\sharp=q^{-Nb+b}h_q^\sharp
                              =q^{-k}\Gamma_{\rm raw}.
 \tag{TG9}
\]

The support has \(h_q q^b\) or \(h_q^\sharp q^b\)
residue matrices, each of volume \(q^{-Nb}\), and
every nonzero value has modulus one.

## 2. The actual preceding constituent

Let \(\pi_0\) be an irreducible actual initial local
constituent with a finite Steinberg type as in LIFT19.
It has Iwahori-fixed vectors and unramified cuspidal
support, by the Casselman result already used there.
The actual first and second local theta constituents
in the literal bilinear convention are

\[
 \pi=\pi_0\times(\eta_0\circ\det_d),\qquad
 \pi^+=\pi\times(\eta_1\circ\det_d).
 \tag{TG10}
\]

The product denotes normalized parabolic induction.
Both are irreducible: the added residue characters
are distinct from the initial unramified line and
from each other. This is LIFT19's application of
Zelevinsky's disjoint-line theorem and Mínguez's
actual type-II theta correspondence. These published
results are used rather than claimed as new.

The source here is the actual constituent \(\pi\)
of a first theta image, not an arbitrary representation
chosen only by its archimedean weight. Its prescribed
compact-type space

\[
                          V_\lambda=\pi^{J,\lambda}
 \tag{TG11}
\]

is nonzero by LIFT19(T16)–(T17). Every nonzero vector
in this space works below. It is \(K_b^1\)-fixed.
Restricting its character to \(J^\sharp\) gives the
same vectors for the literal sharp kernel.

## 3. The full-rank Haar-normalized intertwiner

The actual common-character split oscillator acts by

\[
 \omega(g,h)\phi(X)=
 \eta_1(\det g)^{-1}\eta_1(\det h)
 |\det g|^{N/2}|\det h|^{-b/2}\phi(h^{-1}Xg).
 \tag{TG12}
\]

This is the genuine left-action convention of DO033.5
and corrected LIFT16(S2). The source variable acts by
\(X\mapsto Xg\). The source bilinear lift takes diagonal
coinvariants of \(\omega\otimes\pi\).

Write \(\Omega\) for the full-rank open set and
\(X_0=[I_b;0]\). For \(\phi\in S(\Omega)\), \(v\in\pi\),
define

\[
 {\cal I}(\phi,v)=
   \int_{\mathrm{GL}_b(F_v)}
       \phi(X_0g)\eta_1(\det g)^{-1}
                    |\det g|^{N/2}\pi(g)v\,dg.
 \tag{TG13}
\]

This is an ordinary compact integral, with no meromorphic
regularization. The image of \(g\mapsto X_0g\) is closed
in \(\Omega\); the inverse image of the compact support
of \(\phi\) is compact in \(\mathrm{GL}_b\).
The smooth integrand takes values in a finite-dimensional
span on that compact set, so its integral lies in \(\pi\).

Let \(P=P_{(b,d)}\) be the upper parabolic of
\(\mathrm{GL}_N\). Set

\[
             {\cal T}(\phi,v)(h)
                      ={\cal I}(\omega(1,h)\phi,v).
 \tag{TG14}
\]

Then T factors through the source diagonal coinvariants
and takes values in the actual normalized induction
\(\pi^+\). The complete covariance checks are as follows.

First
\({\cal I}(\omega(g_0,1)\phi,\pi(g_0)v)={\cal I}(\phi,v)\).
Substitute \(g'=g g_0\) in(TG13). The two eta factors
combine to \(\eta_1(\det g')^{-1}\), the absolute-value
factors combine identically, and
\(\pi(g)\pi(g_0)=\pi(g')\). Unimodularity preserves Haar.

Next let \(p=[A\ C;0\ D]\in P\), so
\(p^{-1}X_0=X_0A^{-1}\). Substitute \(g=A g'\)
in(TG13), using(TG12), to obtain exactly

\[
 {\cal I}(\omega(1,p)\phi,v)=
 |\det A|^{d/2}|\det D|^{-b/2}
          \eta_1(\det D)\pi(A){\cal I}(\phi,v).
 \tag{TG15}
\]

The unipotent C disappears because it fixes the embedded
source space. The absolute-value factor is
\(\delta_P(p)^{1/2}\). Therefore
T(phi,v)(p h) has precisely the normalized induction
transformation law. Target translation by \(h_0\)
sends the section to \(h\mapsto T(\phi,v)(h h_0)\).
Smoothness follows from a small compact fixing \(\phi\),
and \(P\backslash\mathrm{GL}_N\) is compact.

The full-rank coinvariant identification is

\[
 (S(\Omega)\otimes\pi)_{\mathrm{GL}_b}
       \simeq
 \operatorname{Ind}_{P}^{\mathrm{GL}_N}
                  (\pi\boxtimes\eta_1\det_d),
 \tag{TG16}
\]

with map T and the displayed normalization.
Here is an elementary verification in addition to
the covariance calculation. Full-rank matrices form
a locally trivial principal GL_b bundle over the
p-adic Grassmannian. That compact, totally disconnected
space admits a finite clopen refinement of trivializing
charts for each locally constant function in question.
On a chart, multiply the fibre function by
\(\eta_1(\det g)^{-1}|\det g|^{N/2}\). The source action
becomes ordinary right translation on \(C_c^\infty(\mathrm{GL}_b)\),
together with \(\pi\) on its coefficient vector.
Its diagonal coinvariant map is
\(f\otimes v\mapsto\int f(g)\pi(g)v\,dg\), an
isomorphism onto \(\pi\).

To verify that assertion, a vector fixed by a compact
open K is represented by
\(\operatorname{vol}(K)^{-1}1_K\otimes v\).
Changing to a smaller such K leaves its class unchanged
by finite coset decomposition and the diagonal relations.
Conversely, partition the compact support of f into
cosets of a small compact open. The same diagonal
relations and finite averaging reduce its class to
that of its displayed integral. This proves both
injectivity and surjectivity. Finite partitions of
unity on the clopen charts glue the fibre maps, with
transition law(TG15). This proves(TG16).

## 4. Identification with the actual small theta quotient

The open-set map must be related to the full oscillator.
We use the published rank filtration in Mínguez(2008),
section2, pp.722–724. The boundary quotients are the
rank j strata with \(j<b\). Corollary2.3 describes
their possible irreducible source quotients: after
removing oscillator determinant normalization, such
a quotient is a quotient of an induced representation
with a nonzero trivial GL_(b-j) factor. Modulus
characters only introduce unramified twists of that
factor. Its cuspidal support therefore contains an
unramified line.

For(TG12) the relevant source quotient is \(\pi^\vee\).
Removing \(\eta_1^{-1}\) replaces its cuspidal inertia
lines by those of \(\pi^\vee\otimes\eta_1\), up to
unramified powers and the inverse-transpose automorphism
used in the alternate rectangular-matrix convention.
Those lines are

\[
                         \bar\eta_1,\qquad
                         \bar\eta_1\bar\eta_0^{-1}.
 \tag{TG17}
\]

Both are nontrivial. Simultaneously inverting them
under the alternate convention changes nothing.
Uniqueness of cuspidal support therefore excludes
the source quotient from every boundary stratum.
No pole-free regularization is assumed.

There is an actual nonzero oscillator map to
\(\pi^\vee\otimes\pi^+\) by LIFT19 and Mínguez's
theta theorem. Its restriction to \(S(\Omega)\)
cannot vanish: otherwise a nonzero map from a
boundary stratum would follow by the finite rank
filtration, contradicting the preceding argument.
By(TG16) and irreducibility of \(\pi^+\), Schur's
lemma makes the target-equivariant Hom space from
the full-rank coinvariants to \(\pi^+\) one-dimensional.
Thus the actual small-theta map restricts to a
nonzero scalar multiple of T.

The coinvariant and tensor-Hom formulations agree
here without a completed-tensor ambiguity. A
compact open source subgroup fixing a given
Schwartz vector makes the dependence on the
input factor through its invariants. Admissibility
of \(\pi\) makes that space finite dimensional,
so the corresponding map has coefficients in
the smooth contragredient tensor the target.

Every vector detected by T is therefore nonzero
in the actual small theta quotient. One may
normalize that local quotient map so its restriction
equals(TG14). The scalar comparing this choice
with a globally pinned automorphic realization
is not computed by uniqueness. All norm and
lattice statements retain that distinction.

## 5. Exact survival of the prescribed column

For \(v\in V_\lambda\), evaluate T at the identity.
The raw factor on \(X_0g\) is supported on \(g\in J\);
its last row is zero. The determinant terms give

\[
               \Phi(X_0g)\eta_1(\det g)^{-1}
                                      =\lambda(g)^{-1}.
 \tag{TG18}
\]

The determinant has absolute value one and
\(\pi(g)v=\lambda(g)v\), so the integrand in(TG13)
is exactly v. On \(J^\sharp\) the restricted character
gives the identical calculation. Hence

\[
 \boxed{\quad
 {\cal T}(\Phi,v)(1)=v_Jv,\qquad
 {\cal T}(\Phi^\sharp,v)(1)=v_{J^\sharp}v
                   \quad(v\in V_\lambda).\quad}
 \tag{TG19}
\]

Both fixed raw kernels are injective on the entire
type space. Every nonzero prior-image vector in
this prescribed local column survives. This does
not assert survival for arbitrary vectors outside
the column. Without the type condition, identity
evaluation is exactly the compact character projector:
T(Phi,v)(1)=v_J e_(J,lambda)v, and similarly for
the sharp subgroup. Thus(TG19) concerns a fixed
raw function, not a Schwartz choice depending on v.

## 6. Exact compact-model norms

The actual automorphic constituent \(\pi\) is unitary.
Give \(\pi^+\) its normalized induction metric on
\(K_N=\mathrm{GL}_N(O)\), retaining the chosen unitary
metric on \(\pi\). Put

\[
 {\cal J}_{b,d}(q)=[\mathrm{GL}_N(\kappa):P_{(b,d)}(\kappa)]
     =\frac{\prod_{i=1}^{N}(q^i-1)}
        {\prod_{i=1}^{b}(q^i-1)\prod_{i=1}^{d}(q^i-1)}.
 \tag{TG20}
\]

The sections are target \(K_N^1\)-fixed. Their finite
parabolic quotient points have measure \(1/{\cal J}_{b,d}\).
A nonzero value can occur only when the residue source
b-plane is a graph

\[
 L_z=\left\{\begin{pmatrix}x\\0\\zx\end{pmatrix}:x\in\kappa^b\right\},
                    \qquad z\in\kappa^{1\times b},
 \tag{TG21}
\]

where the zero has d-1 coordinates. The raw support
requires the plane to lie in the space spanned by the
first b and last coordinates and project invertibly
onto the first b, giving exactly these graphs.
The reduction of a compact frame has full rank,
so a contributing g is integral and invertible
modulo q; no other finite plane can contribute.
For a graph choose the integral representative
\(h_z=I_N-e_Nz\), with z extended by zeros on
the last d coordinates. Then
\(h_z^{-1}X_0=[I_b;0;z]\).

For \(v\in V_\lambda\), all determinant and
representation factors cancel as in(TG18).
The finite averages are

\[
 \begin{split}
 {\cal T}(\Phi,v)(h_z)
  &=v_J\left(|H|^{-1}\sum_{g\in H}\psi_0(-zge_k)\right)v,\\
 {\cal T}(\Phi^\sharp,v)(h_z)
  &=v_{J^\sharp}\psi_0(-z_k)v.
 \end{split}
 \tag{TG22}
\]

For the sharp subgroup \(ge_k=e_k\). For H,
the first k entries of \(ge_k\) vary independently
over \(\kappa\), its k-th entry is one, and
its subsequent entries are zero. Additive
orthogonality therefore gives

\[
 {\cal T}(\Phi,v)(h_z)=
 \begin{cases}
    v_J\psi_0(-z_k)v,&z_0=\cdots=z_{k-1}=0,\\
    0,&\text{otherwise}.
 \end{cases}
 \tag{TG23}
\]

There are exactly \(q^{b-k}\) nonzero finite
quotient values in the nonsharp case and \(q^b\)
in the sharp case. Hence for every \(v\in V_\lambda\),

\[
 \boxed{
 \begin{split}
 \|{\cal T}(\Phi,v)\|^2
    &=\frac{q^{b-k}v_J^2}{{\cal J}_{b,d}(q)}\|v\|^2,\\
 \|{\cal T}(\Phi^\sharp,v)\|^2
    &=\frac{q^b v_{J^\sharp}^2}{{\cal J}_{b,d}(q)}\|v\|^2.
 \end{split}}
 \tag{TG24}
\]

Their squared constants have ratio \(q^{-k}\),
the same as the raw Schwartz norms(TG9). After
unit-normalizing the finite raw input, the two
maps have the same squared scaling constant:

\[
 \boxed{
 {\cal C}_q=
 \frac{q^{Nb-k}h_q}{|\mathrm{GL}_b(\kappa)|^2{\cal J}_{b,d}(q)}
 =\frac{q^{Nb}h_q^\sharp}
        {|\mathrm{GL}_b(\kappa)|^2{\cal J}_{b,d}(q)}.}
 \tag{TG25}
\]

These are local induced-model metric identities.
The real selected Schwartz norm, global mass,
and scalar comparing this model to an automorphic
row are separate. The finite sharp modification
alone does not improve this unit-input scaling.
For the primitive LIFT19(T18)–(T20) vector,
its natural metric is
\(\|v\|^2=q^{k(k+1)/2}/{\cal J}_{k,d}(q)\);
it may be substituted into(TG24) directly.

## 7. Exact content in the natural induced lattices

Let R be the valuation ring at a place above11
of a coefficient extension containing the additive
and tame character values. Use the natural finite
models supplied by LIFT19:

\[
 \begin{split}
 L_1&=\operatorname{Ind}_{P_{(k,d)}(\kappa)}
                           ^{\mathrm{GL}_b(\kappa)}
       (\mathrm{St}_{k,R}\boxtimes\bar\eta_0\det_d),\\
 L_2&=\operatorname{Ind}_{P_{(b,d)}(\kappa)}
                           ^{\mathrm{GL}_N(\kappa)}
       (L_1\boxtimes\bar\eta_1\det_d).
 \end{split}
 \tag{TG26}
\]

Fix one finite Steinberg embedding into
\(\pi_0^{K_k^1}\). These are the selected finite
submodules of the actual compact models obtained
from that embedding, with specified integral
inducing lattices. They need not exhaust all
principal-congruence invariants of either
constituent. Their comparison with a global
arithmetic row lattice is extra data. Put
\(L_\lambda=L_1\cap V_\lambda\).
It is saturated in \(L_1\): its defining equations
are the kernels of R-linear maps
\(\pi(h)-\lambda(h)\) into a torsion-free module.

Divide T by \(v_J\) or \(v_{J^\sharp}\).
Equations(TG22)–(TG23) show that every finite
quotient value is zero or a root of unity times v.
The identity value is exactly v; parabolic
transition maps preserve the integral lattices.
Consequently

\[
 v_J^{-1}{\cal T}(\Phi,-),\quad
 v_{J^\sharp}^{-1}{\cal T}(\Phi^\sharp,-):
                         L_\lambda\longrightarrow L_2
 \tag{TG27}
\]

are primitive saturated injections. To prove
saturation, suppose a uniformizer divides the
image in \(L_2\). Identity evaluation shows
it divides v in \(L_1\); saturation of
\(L_\lambda\) puts the divided vector in the
domain. Torsion-freeness then identifies its
image with the divided image. This does not
assume existence of an integral H-projector.

If \(c_R(v)\) denotes the content valuation
in the indicated free R-module, then

\[
 \begin{split}
 c_R({\cal T}(\Phi,v))&=c_R(v)+v_{11}(v_J),\\
 c_R({\cal T}(\Phi^\sharp,v))&=c_R(v)+v_{11}(v_{J^\sharp}),\\
 v_{11}(v_J)=v_{11}(v_{J^\sharp})
              &=-\sum_{i=t+1}^{b}v_{11}(q^i-1).
 \end{split}
 \tag{TG28}
\]

Here \(v_{11}(11)=1\), and q is an11-unit.
The matrix-coefficient normalization and natural
induced lattices are fixed in this statement.
It cannot be identified with the global DP44
gain \(g_j\) without the missing row-lattice
and scalar comparison.

## 8. Global implication and remaining exact gates

The local result applies at every degree-one
selected G place of a repaired host with distinct
nontrivial literal tame characters. It is independent
of the number of real embeddings. It therefore
applies to the actual first constituents from
K031/DO034, and to later repaired hosts only after
their actual first-family and character hypotheses
are supplied.

The fixed terminal raw G factor cannot annihilate
a nonzero previous-image vector in \(V_\lambda\).
Finite tensor products of these column spaces
satisfy the product versions of(TG19), (TG24),
and(TG28). Thus this particular G-place test is
no longer an unspecified local nonvanishing
condition on the m=2 route.

This does not put a particular global first
vector into every required column by an integral
operator of known height. LIFT19 supplies occurrence
and an explicit natural vector; the comparison
with the exact global previous-image lattice
remains necessary. Nor does this argument treat
the fixed T/Q terminal factors, the permitted29
family at the second edge, the final global row,
or the normalization of all local quotient maps
by one global theta period. These are separate
gates before a full DP44 changed-data comparison
or a shorter source-compatible chain is claimed.

## 9. Sources and proof status

Mínguez, A. (2008). Correspondance de Howe explicite:
Paires duales de type II. Annales scientifiques de
l'École Normale Supérieure, 41(5), 717–741.
https://www.numdam.org/item/ASENS_2008_4_41_5_717_0/ .
Theorem1, p.718; action conventions in section1.4,
pp.721–722; exact rank filtration, Corollary2.3,
and Theorem2.4 with its restriction argument,
pp.722–724. Read directly in the primary PDF.
The theorem is used as a published input.

Other published representation inputs are those
already checked in LIFT19: Casselman(1980),
Proposition2.6; Zelevinsky(1980), Propositions8.5–8.6;
and the finite Steinberg theorem. They are not
counted again as new results.

The new calculations are the raw terminal compact
support and character, the Haar-normalized open-rank
integral in the actual source convention, its value
on the whole prescribed column, the graph-plane
norm, and the saturated natural-lattice comparison.
The author whole-proof reading has been completed,
including the raw source predicates, all source
and target covariance signs, full-rank coinvariants,
the boundary restriction argument, every graph
value, both norm normalizations, and saturation
without an integral isotypic projector.

The exact diagnostic raw_terminal_g_certificate.py
passed two finite cases: q=5,k=1,t=1 with distinct
nontrivial residue characters, and q=3,k=2,t=1
for the higher-k raw geometry. It checks1,958
raw determinant/input phase cancellations and412
full graph averages, the support counts, both
Haar volumes, and equal unit-input metric scaling.
The second case does not assert the distinct
character hypothesis, and neither small case is
an admissible full source Ranks datum. The general
quotient and lattice proofs are independent of
these finite checks. Exact check events are in
lift_accounting_CHECK_EVENTS.tsv.

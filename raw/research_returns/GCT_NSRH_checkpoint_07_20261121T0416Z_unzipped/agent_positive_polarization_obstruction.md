# F47: positive duality at the actual collision

Author: root, GPT-6 Astra Pro; reasoning effort not exposed; run GCT_NSRH_20261121.
Date: 2026-11-21 UTC. Status: complete author proof, independent review pending.

## 1. Scope and known categorical input

This finding concerns the **actual flat rank-ten algebra**, including its four-dimensional radical at the parameter collision. It does not assert that its rank-six ambient image or the specialized rank-64 tensor representation has no positive form. Those representations kill the radical.

The categorical input is known: a multifusion category has a based Grothendieck ring, and the complexification of a finite-rank based ring is semisimple. Exact primary locators are Etingof–Gelaki–Nikshych–Ostrik, *Tensor Categories*, MIT 2009 lecture notes, Definition 1.42.2 and Proposition 1.42.4, printed pp.76–77, and Corollary 1.43.5, printed p.80. The primary PDF https://math.mit.edu/~etingof/tenscat1.pdf was opened and the complete relevant statements read in this run. We cite this known theorem rather than reprove it. This is a statement about multifusion rings, not arbitrary positive rings, arbitrary split Grothendieck groups, or arbitrary triangulated categories.

## 2. No finite rigid semisimple categorification of the full collision algebra

Let

\[
A_1=\mathbf C\times\mathbf C\times M_2(\mathbf C[\varepsilon]/\varepsilon^2)
\]

be F19's actual specialized algebra. There is no multifusion category \(\mathscr D\) for which

\[
K_0(\mathscr D)\otimes_{\mathbf Z}\mathbf C\simeq A_1
\]

as algebras. More generally, a proposed graded categorification whose specialization at \(v=1\) is the complexified Grothendieck ring of such a category cannot retain the full flat rank-ten algebra.

**Proof.** The ideal
\(J=0\times0\times M_2(\varepsilon\mathbf C)\)
is nonzero, has square zero, and has semisimple quotient. It is therefore the Jacobson radical of \(A_1\), as already proved in F19. The cited finite-based-ring theorem makes the proposed Grothendieck algebra semisimple, a contradiction. This proves exactly the stated application. No claim is made that forgetting a grading automatically produces a multifusion category. That is an explicit hypothesis of the graded assertion. \(\square\)

## 3. Every positive adjoint realization loses the radical

There is a sharper elementary operator statement which does not assume a categorical realization. Give \(A_1\) its actual generators \(P_1,P_2\). Let \(H\) be any finite-dimensional complex Hilbert space and let
\(\rho:A_1\longrightarrow\operatorname{End}_{\mathbf C}(H)\)
be an algebra representation in which \(\rho(P_1)\) and \(\rho(P_2)\) are self-adjoint. Then

\[
J\subseteq\ker\rho.
\]

Consequently no faithful representation of the full collision algebra can make the two named generators self-adjoint for a positive-definite Hermitian form. Every such representation factors through the actual classical quotient \(\mathbf C\times\mathbf C\times M_2(\mathbf C)\simeq\mathbf C[S_3]\).

**Proof.** Set \(e=P_1/4\), \(f=P_2/4\) and \(z=(e-f)^2\). F19 proves that \(z\) is central, is zero on the two scalar factors, and has the form \(3/4+\eta\) on the matrix factor, where \(\eta\ne0\) is a central square-zero element generating \(J\) as a two-sided ideal. Since \(\rho(e)\) and \(\rho(f)\) are self-adjoint, so is \(\rho(z)\). Define the real polynomial

\[
p(T)=1-\frac{(T-3/4)^2}{(3/4)^2}.
\]

Then \(p(z)\) is exactly the central idempotent selecting the matrix factor: it is zero at \(z=0\), and one where \((z-3/4)^2=0\). Hence

\[
n=p(z)(z-3/4)
\]

is zero on the scalar factors and equals \(\eta\) on the matrix factor. It is nonzero in \(A_1\), satisfies \(n^2=0\), and generates \(J\). Its image is self-adjoint, being a real polynomial in the self-adjoint \(\rho(z)\). For every \(u\in H\),

\[
\|\rho(n)u\|^2=\langle u,\rho(n)^2u\rangle=0.
\]

Thus \(\rho(n)=0\), and the whole ideal it generates is killed. \(\square\)

The positivity assumption is essential: an indefinite nondegenerate bilinear form can admit nonzero self-adjoint nilpotent operators. The assertion also requires the named generators to be adjoints of themselves; purity of a Frobenius spectrum supplies no such condition.

## 4. Exact degeneration of a positive center pairing

Work over the real local parameter ring
\(R=\mathbf R[v,v^{-1}]_{(v-1)}\). Put \(t=v-1\) and

\[
\Delta=\frac{D-1}{D^2}(v-v^{-1})^2=t^2u(t),\qquad u(0)=3/4>0,
\]

where \(D=(v+v^{-1})^2\). The actual center factor is

\[
C=R[x]/(x(x-\Delta)),\qquad x=z_1-z.
\]

For \(\Delta\ne0\), the regular algebra trace pairing
\(B(a,b)=\operatorname{Tr}_{C/R}(m_{ab})\)
has Gram matrix in the basis \((1,x)\)

\[
G_{\mathrm{tr}}=
\begin{pmatrix}2&\Delta\\\Delta&\Delta^2\end{pmatrix},
\qquad\det G_{\mathrm{tr}}=\Delta^2.
\]

It is positive definite at every real nearby point with \(\Delta\ne0\), and its determinant vanishes to exactly order four at \(v=1\). This degeneration is optimal among all regular symmetric forms on the rank-two regular module which make multiplication by \(x\) self-adjoint and are positive definite at all sufficiently near real noncollision parameters: their determinants have valuation at least four.

**Proof.** The multiplication traces are \(\operatorname{Tr}(1)=2\), \(\operatorname{Tr}(x)=\Delta\), and \(\operatorname{Tr}(x^2)=\Delta^2\). The displayed determinant and positive definiteness follow from the leading principal minor 2 and the positive determinant. For the lower bound, in right-row convention multiplication by \(x\) has matrix

\[
X=\begin{pmatrix}0&1\\0&\Delta\end{pmatrix}.
\]

If \(G=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)\), the self-adjoint relation \(XG=GX^{\mathsf T}\) is exactly \(c=\Delta b\). At nearby positive real \(t\), positive definiteness gives \(a(t)>0\) and

\[
0<b(t)<a(t)\Delta(t),
\qquad \det G=b(a\Delta-b)>0.
\]

Write \(s=\operatorname{ord}_t a\ge0\), \(r=\operatorname{ord}_t b\ge0\). The displayed inequality forces \(r\ge s+2\): otherwise \(b/(a\Delta)\) tends to positive infinity as \(t\to0^+\), contrary to its being less than one. Hence
\(\operatorname{ord}_t(a\Delta-b)\ge s+2\), and

\[
\operatorname{ord}_t\det G\ge 2s+4\ge4.
\]

The trace form attains equality. This proves the optimal lower bound. If \(a\) or \(b\) were identically zero, generic positive definiteness would already be impossible, so the valuations used are defined. \(\square\)

The same proof for \(\Delta=t^m u(t)\) positive on a punctured real half-neighborhood gives determinant valuation at least \(2m\), attained by the trace form. This is a statement about regular self-adjoint forms on the regular rank-two center module; no bound on every unrelated pairing is asserted.

## 5. The actual tensor module keeps a positive form by killing the radical

This boundary can be checked on the actual module, not only inferred abstractly. On either rank-two block \(N(a)\) of F21, where \(a=\delta=v+v^{-1}\) or \(a=D-2\), use

\[
G_a=\begin{pmatrix}1&a/D\\a/D&1\end{pmatrix}.
\]

The right-row matrices \(P_1=\left(\begin{smallmatrix}D&0\\a&0\end{smallmatrix}\right)\) and \(P_2=\left(\begin{smallmatrix}0&a\\0&D\end{smallmatrix}\right)\) satisfy \(P_iG_a=G_aP_i^{\mathsf T}\) by direct multiplication. For every positive real \(v\), one has \(\delta\ge2\), \(D\ge4\), and

\[
0<\delta/D=1/\delta<1,\qquad
0<(D-2)/D<1.
\]

Thus each \(G_a\) is positive definite, including at \(v=1\), where both equal \(\left(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right)\). Give the scalar factors their positive standard forms and use the multiplicities 20,4,16,4 in F21. The resulting form on the actual rank-64 module is positive and regular through the collision, and its named generators are self-adjoint. F21's change of basis is regular and invertible at the collision, so this form transports to the original tensor basis without a pole there. This does not contradict Section 3: the specialized tensor action kills exactly the radical. It shows that the obstruction isolates faithfulness on the full flat order, rather than positivity of the existing tensor representation.

## 6. Separate Grothendieck-framework dictionary

The finite-flat scheme \(\operatorname{Spec}C\to\operatorname{Spec}R\) has a regular algebra trace map, and \(C\to C^\vee\), \(a\mapsto(b\mapsto\operatorname{Tr}(ab))\), is a morphism of finite locally free \(R\)-modules. Its determinant ideal is \((\Delta^2)\), computed above, and its special-fiber kernel is the nilpotent direction. The complete computation is the proof; no unverified EGA locator for a discriminant theorem is needed. The affine module/sheaf dictionary is to be supplied by the ongoing exact EGA audit before integration. Equivariant locally free modules use SGA 3, Exposé I, 4.7.2–4.7.3 and the verified manuscript cote90, scan17.

For \(K_0\), the categorical statement says that effectivity plus finite semisimple rigid duality places substantially more conditions on a based Grothendieck algebra than the virtual \(\lambda\)-identities of SGA6, Exposé V, §§2–3. The precise finite-based-ring theorem is the modern EGNO locator above. Cote133, scan18, supplies the verified generating-series identity for symmetric and exterior powers, not a claim of this GCT obstruction.

For a proposed motivic polarization, a positive-definite realization with the two correspondences \(P_i\) self-adjoint necessarily annihilates the radical. This is the exact operator theorem of Section3. Cote16, scans35,37,39 contains the primitive-projector/Lefschetz language; scans48–49 concern conditional semisimplicity and Weil assertions. They are vocabulary anchors here, not a proof that such correspondences or a polarization exist for GCT. A smooth proper dg category as in F40/F44 may still have this nonsemisimple algebra as an object's endomorphism algebra: the based Grothendieck algebra and the endomorphism algebra of one object are different roles. Ordinary Weil purity alone is also compatible with Jordan blocks, so F46's proposed pure model is not contradicted.

## 7. Gate changed and gate left open

The full collision algebra cannot enter the literal finite rigid semisimple based-ring route or a faithful positive-adjoint realization of its named generators. The exact rank-six quotient can. F40/F44's smooth corner model, F43's non-rigid graded kernel model, indefinite forms, non-self-adjoint realizations, and models that do not identify a Grothendieck algebra with the full order remain possible. None of these operator facts supplies the opposite middle-degree path sign, the independent dual bound, or VIII's prescribed canonical lattice. This finding therefore closes two explicitly stated comparisons, not Mulmuley's whole program.

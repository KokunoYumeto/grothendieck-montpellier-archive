# DET-19 independent check: the natural Bessel boost and arithmetic flow

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_spectral_bridge.

## Verdict and version

PASS. I independently read the complete work/paper_bessel_boost.tex and checked its exact source definitions. No mathematical correction is required.

Checked TeX SHA256: 33eca819abaefc35b349249d29d8224bf7fba763a181dba03f2f74eadf2f1a74.

The proof establishes a genuine additional obstruction: the natural source boost has coefficients, and trace-class trace coefficients, vanishing at infinity, whereas the arithmetic cosine kernel does not vanish at infinity. Its pure-point arithmetic translation model therefore cannot embed by a bounded intertwiner into this natural boost action. This result concerns the fixed representation and its closed Bessel image. It does not invalidate the positive trace-class operator already constructed on that image, nor rule out other flows.

## Exact source definitions checked

All paths in this section are relative to work/external_lean/lean/src/.

1. Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MatrixOfBesselTwoSidedAction.lean:
   - Lines 11–15: matrix size, group, and the definition
     \(\operatorname{opn}(g)=\|\operatorname{Matrix.toEuclideanCLM}(g)\|\).
   - Line 40: the coefficient is \(\langle v,\sigma(g)u\rangle\), with the first variable conjugate-linear.
   - Lines 47–48: DD is the algebraic complex span of the orbit of \(w_0\).
   - Lines 50–51: for each pair in DD there is a constant C bounding the absolute coefficient by \(C\operatorname{opn}(g)^{-a}\) for every group element.
   - Lines 53–55: Std includes \(k\ge1\), a unit norm starting vector, unitary strongly continuous irreducible representation, \(a\ge2(2r+k+1)^5\), decay on DD, and completeness.
2. Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean, lines 23–28: IsURepOn includes the representation law, norm preservation, and vectorwise continuity on the group; IsIrredOn concerns every closed invariant submodule.
3. Formalism/FormalDegreeBessel/StatementG.lean, lines 11–24: the group is defined by \(g^*H_{k,r}g=H_{k,r}\), and the middle coordinates have the displayed diagonal signs. In particular r is positive and r+k is negative. These are distinct since \(k\ge1\).
4. Formalism/PeriodIntegrals/UpqRep.lean, the corresponding displayed Hpk and representation-law definitions: consistent with the group convention used in the paper.
5. The isometry, dense orbit span, representatives and support statements in the already independently checked work/paper_bessel_projector.tex.

The source norm is specifically the Euclidean operator norm. No equivalence of an unspecified matrix norm with an operator norm is assumed.

This is a mathematical and source-text check, not a Lean execution or a certification of the complete import graph.

## 1. The boost belongs to the exact source group

The coordinate plane spanned by \(e_r,e_{r+k}\) is orthogonal, for the source Hermitian form, to all other coordinate directions. Its form is \(\operatorname{diag}(1,-1)\). The symmetric real matrix

\[
g_t|_{\langle e_r,e_{r+k}\rangle}
=
\begin{pmatrix}
\cosh t&\sinh t\\
\sinh t&\cosh t
\end{pmatrix}
\]

preserves this form by \(\cosh^2t-\sinh^2t=1\). Extending it by the identity therefore gives an element of the exact group G. Hyperbolic addition gives \(g_tg_s=g_{t+s}\), and its entries are continuous in t.

The Euclidean unit vectors \((e_r+e_{r+k})/\sqrt2\) and \((e_r-e_{r+k})/\sqrt2\) have eigenvalues \(e^t,e^{-t}\). Their Euclidean orthogonal complement has eigenvalue one. Thus the proof's exact equality

\[
\operatorname{opn}(g_t)=e^{|t|}
\]

is valid for the source norm. Even the lower bound \(\operatorname{opn}(g_t)\ge e^{|t|}\) would suffice. There is no norm-convention gap.

The source representation law, norm preservation and continuity make \(V_t=\sigma(g_t)\) a strongly continuous unitary one-parameter group.

## 2. Decay passes from DD to all coefficients

For \(u,v\in D\), the source estimate and positive a give

\[
|\langle v,V_tu\rangle|\le C_{u,v}e^{-a|t|}\longrightarrow0.
\]

The paper does not assume that these constants are uniform over the unit sphere.

The closure of D is invariant because D is the orbit span and every \(\sigma(g)\) is bounded. It contains the nonzero unit vector \(w_0\), so irreducibility makes it the entire Hilbert space.

For arbitrary \(u,v\), and approximations \(u_0,v_0\in D\), the estimate

\[
|\langle v,V_tu\rangle-\langle v_0,V_tu_0\rangle|
\le \|v-v_0\|\|u\|+\|v_0\|\|u-u_0\|
\]

is uniform in t. First making this small and then using decay for the fixed approximating pair proves vanishing for all coefficients. The argument does not assert an exponential rate for arbitrary Hilbert vectors.

## 3. Trace-class trace coefficients vanish at infinity

For \(Rx=\sum_{j=1}^q\langle v_j,x\rangle u_j\), the conjugate-linear-first trace formula is exactly

\[
\operatorname{Tr}(RV_t)
=\sum_{j=1}^q\langle v_j,V_tu_j\rangle.
\]

There is no adjoint or sign reversal missing. Each summand is continuous and vanishes at infinity.

Finite-rank approximation in trace norm gives

\[
\sup_t|\operatorname{Tr}((T-R)V_t)|
\le\|T-R\|_1,
\]

since \(V_t\) is unitary. Hence every \(t\mapsto\operatorname{Tr}(TV_t)\), for arbitrary complex trace-class T, is a uniform limit of continuous functions vanishing at infinity and has the same property. The displayed cosine combination uses \(V_t+V_{-t}\), so it also vanishes. Positivity of T is not needed.

## 4. Eigenvectors, finite-dimensional subspaces and the compact commutant

A nonzero boost eigenvector would have a diagonal coefficient of constant nonzero modulus. This contradicts coefficient decay.

The stronger finite-dimensional assertion does not require a simultaneous diagonalization theorem. If E is invariant for all t, it is invariant under both \(V_t\) and \(V_{-t}\), so the restriction is unitary. For an orthonormal basis of a nonzero m-dimensional E,

\[
\sum_{i,j=1}^m|\langle e_i,V_te_j\rangle|^2=m.
\]

Every summand tends to zero, which is impossible.

For an arbitrary nonzero compact Q commuting with every \(V_t\), its adjoint also commutes by using \(V_t^*=V_{-t}\). Thus \(Q^*Q\) is nonzero positive compact and commutes. Its largest positive eigenvalue has a nonzero finite-dimensional eigenspace, invariant under the group. This contradicts the preceding paragraph. This argument covers nonnormal or quasinilpotent Q; it does not incorrectly infer a nonzero eigenvalue of Q itself.

The conclusion is stronger than an obstruction to full G-invariance: commutation with this single noncompact boost group already forces a compact operator to be zero.

## 5. The arithmetic kernel is unconditionally not C0

Every bounded continuous h tending to zero at infinity has zero symmetric Cesàro Fourier coefficient at every real frequency. The displayed split into \([-L,L]\) and its complement gives the required bound. The finite central integral vanishes after division by T; the remaining supremum vanishes as L tends to infinity.

If the actual arithmetic k tended to zero, it would be bounded. DET-16's checked global Landau converse would then imply RH. Under RH, the exact explicit formula recovers, at each positive Xi ordinate,

\[
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^T k(t)e^{-i\lambda t}\,dt
=
\frac{m_\lambda}{\lambda^2+1/4}>0.
\]

There are such ordinates by the classical zero count. This contradicts the C0 calculation.

Thus the statement that k does not tend to zero has no RH hypothesis: if RH fails, boundedness already fails; if RH holds, its nonzero atoms preclude vanishing. The source decay statement retains its source representation hypotheses. Consequently k cannot be a vector coefficient, a trace-class trace coefficient, or the indicated trace cosine coefficient of this boost.

## 6. Pure-point intertwiners

Under RH, the arithmetic cyclic model has a complete orthonormal eigenbasis for translations; the restored model has the recovered integer multiplicity at each frequency. If a bounded map J intertwines either group with the boost, the image of every eigenbasis vector is a boost eigenvector or zero. The absence of nonzero boost eigenvectors forces every such image to vanish, and boundedness and density force \(J=0\).

The paper correctly states a zero bounded-intertwiner theorem, which in particular excludes bounded injective and unitary intertwiners. It does not make a claim about an arbitrary unbounded map with an unspecified domain.

## 7. Transfer to the actual closed Bessel image

The isometric map \(u\mapsto\eta_u\) on dense D extends to an isometry \(\mathcal J:H_\sigma\to\mathcal B\), with closed image \(\mathcal B_\sigma\). For canonical coefficient representatives, \(u\in D\) and \(x,g\in G\), the representation law gives

\[
\eta_u(xg)
=\sqrt d\,l(\sigma(xg)u)
=\sqrt d\,l(\sigma(x)\sigma(g)u)
=\eta_{\sigma(g)u}(x).
\]

The orbit span is invariant, so the right side remains a vector in the same dense coefficient class. Since \(\nu\) is supported on G, this gives the asserted equality in the quotient-measure realization. The isometry proves that this action is well-defined and unitary on these classes; completion gives precisely \(\mathcal J\sigma(g)\mathcal J^{-1}\) on \(\mathcal B_\sigma\).

No right-invariance of \(\nu\), and no right-translation action on all of the ambient \(L^2(\nu;W_p)\), is needed or asserted. This restriction is essential and is stated in the final proof.

The DET-16 weighted projection operator has its range in this image and is nonzero positive trace class. Its restriction there therefore cannot commute with the natural boost. Its determinant, its trace-norm approximants, and its construction on the fixed source Hilbert space remain valid.

## Final assessment

All claims in the checked version follow with the stated hypotheses. The result identifies a concrete obstruction to a natural-flow interpretation of the arithmetic spectral construction, while preserving the established operator and determinant realization. The proof does not identify the historical finite matrices, exclude other flows, or claim an impossibility theorem for arithmetic realizations in general.


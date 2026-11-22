# SF-E821a: a torsion-free quotient still forces the generic surface splitting

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21.

**Status:** Complete new addendum awaiting independent whole-proof review. It extends only the quotient hypothesis of SF-E821, section3; it does not identify an arbitrary torsion subsheaf as a direct summand.

In the actual triangle

\[
 B[1]\longrightarrow E\longrightarrow A\xrightarrow{a}B[2],
 \tag{E821a.1}
\]

assume that \(A\) is a torsion-free coherent sheaf on the smooth integral fourfold \(X\). Suppose that \(B\), near a general smooth point of a reduced irreducible surface \(S\), has an actual direct summand \(i_*F\), where \(F\) is nonzero locally free on that smooth part of \(S\). Then \(E\) has \(i_*F[1]\) as a local direct summand near a general point of \(S\). In particular the support criterion and zero-pairing conclusions of SF-E821 apply whenever the full character of \(E\) is balanced and invariant semiregularity is assumed.

Let \(\eta\) be the generic point of \(S\), and put \(R=\mathcal O_{X,\eta}\). This is a regular local domain of dimension two. The finite module \(A_\eta\) is torsion-free. Choose a basis of \(A_\eta\otimes_R\operatorname{Frac}(R)\). Since \(A_\eta\) is finitely generated, clearing the finitely many denominators in its generators gives an injection into a finite free module,

\[
 0\longrightarrow A_\eta\longrightarrow R^s
      \longrightarrow Q\longrightarrow0.
 \tag{E821a.2}
\]

Every finite module over this two-dimensional regular local ring has a free resolution of length at most two. The exact primary locator is Stacks Project Proposition10.110.1, tag00O7, https://stacks.math.columbia.edu/tag/00O7. Its statement and proof, including the stated finite-resolution dependencies Lemmas10.106.6 and10.104.9, were read for this addendum. Applying \(\operatorname{Hom}_R(-,N)\) to(E821a.2), for any finite \(N\), gives

\[
 \operatorname{Ext}^2_R(A_\eta,N)
      \simeq\operatorname{Ext}^3_R(Q,N)=0.
 \tag{E821a.3}
\]

Equivalently \(A_\eta\) has projective dimension at most one. This conclusion can also be seen by truncating a finite free resolution of \(Q\) and taking its first syzygy; the split free terms do not affect projective dimension.

A finite free resolution of \(A_\eta\) of length one spreads to a neighborhood of \(\eta\): lift its finitely many matrix entries after clearing denominators; the kernel and cokernel of the resulting complex are coherent and vanish at \(\eta\), so they vanish after shrinking that neighborhood. The same procedure identifies its last cokernel with \(A\) there. Shrink further to an affine open \(U\). We obtain

\[
 0\longrightarrow F_1\longrightarrow F_0
     \longrightarrow A|_U\longrightarrow0
\]

with \(F_0,F_1\) finite free. Applying \(\operatorname{Hom}_U(-,B|_U)\) computes derived Hom by a two-term complex of quasi-coherent sheaves. Since \(U\) is affine, it has no higher quasi-coherent cohomology, and hence

\[
 \operatorname{Ext}^2_U(A|_U,B|_U)=0.
 \tag{E821a.4}
\]

The actual connecting class \(a\) in(E821a.1) therefore restricts to zero on \(U\). The triangle splits there. Taking the assumed direct summand of \(B|_U\) proves the claim, and the local characteristic/coisotropy argument of SF-E821 applies at the general smooth points of \(S\cap U\).

In particular, a singular torsion-free quotient does not by itself evade the two-cohomology surface obstruction. The result still requires the specified surface piece to be a genuine local direct summand of \(B\). It makes no such assertion for a nonsplit local extension of surface torsion by another sheaf. Quotients with torsion along that surface, or more complicated local derived couplings, remain outside this addendum.

# Exact limits of the height-two open-orbit construction

Author: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC. This note checks the specific geometric mechanism used in Manivel's known height-two formula. It does not assert that absence of an open orbit rules out positive combinatorial formulas.

## 1. The precise construction being tested

Let \(U,V\) be complex vector spaces of the same dimension \(n\ge2\), put
\(E=U\otimes V\), and write \(N=\dim E=n^2\). Set
\(G=SL(U)\times SL(V)\), of dimension \(2(N-1)\).
For a space \(W\) of dimension \(r\le N\), let \(B_W\) be a Borel subgroup of \(GL(W)\).

Manivel, *A note on certain Kronecker coefficients*, arXiv:0809.3710v1, §2 pp.2–3 and §3 pp.3–4, uses an open \(G\times B_W\)-orbit on \(E\otimes W\) to obtain a multiplicity-free invariant algebra with monomial highest-weight generators in the case \(n=2,r=4\). The actual polynomial algebra and its exponents are recorded separately in agent_manivel_monomial_application.md.

A generic tensor in \(E\otimes W\) is an injection \(W^*\to E\). Modulo the Borel action on its source, an injection is specified by a partial flag
\[
F_1\subset F_2\subset\cdots\subset F_r\subset E,\qquad \dim F_i=i.
\]
For a fixed flag the compatible injections form one Borel orbit. The map from injections to these flags is a principal Borel bundle (after choosing the dual Borel convention); its fibers have dimension \(r(r+1)/2\). Consequently an open \(G\times B_W\)-orbit on the tensor space is equivalent to an open \(G\)-orbit on this partial flag variety. The rank-deficient tensors are a proper closed subset, so an open tensor orbit would necessarily meet the injection locus.

## 2. Full flags: the exact dimension deficit

For \(r=N\), the flag variety has dimension
\[
\dim\operatorname{Flag}(E)=N(N-1)/2.
\]
Thus
\[
\dim\operatorname{Flag}(E)-\dim G
=\frac{(N-1)(N-4)}2
=\frac{(n^2-1)(n^2-4)}2.
\tag{SF1}
\]
This is positive for every \(n\ge3\). Every \(G\)-orbit has dimension at most \(\dim G\), whereas an open orbit has the dimension of the variety. Therefore no open orbit exists.

Equivalently, the full tensor representation has dimension \(N^2\), while
\[
\dim(G\times B_W)=2(N-1)+N(N+1)/2,
\]
and their difference is again SF1. For \(n=3\) these dimensions are \(36\) versus \(16\) on the flag side, and \(81\) versus \(61\) on the tensor side; the deficit is \(20\). For \(n=2\) the flag-side dimensions are both six; dimension equality is only a necessary condition, while the actual open orbit is provided by Manivel's Lemma 1 and Corollary 1.

This directly excludes extending that same full-flag open-orbit proof to all equal rectangles of height \(n\ge3\).

## 3. Truncating the output length to \(r\ge3\) does not fix this mechanism

The partial flag variety has dimension
\[
F(n,r)=rN-r(r+1)/2.
\]
Hence a necessary dimension condition for an open orbit is
\[
rN-r(r+1)/2\le2(N-1).
\tag{SF2}
\]
At \(r=3\), the difference between its left and right sides is
\(N-4=n^2-4>0\) for \(n\ge3\).
Moreover
\[
F(n,r+1)-F(n,r)=N-r-1\ge0
\qquad(3\le r<N).
\]
Thus the deficit stays positive for every \(3\le r\le N\). In particular, restricting the third partition to length three still does not produce the open orbit used in the height-two argument.

This is a dimension obstruction to the specified action, not an assertion about every invariant-theoretic construction of these multiplicities.

## 4. The remaining \(r=2\) case: an explicit generic stabilizer

Simple dimension comparison alone is inconclusive at \(r=2\):
the partial flag variety has dimension \(2N-3\), one less than \(\dim G=2N-2\).
An exact stabilizer calculation nevertheless rules out an open orbit for \(n\ge3\).

View \(E\) as the space of \(n\times n\) matrices, with
\((g,h)\cdot X=gXh^t\). On a dense open set a flag consists of an invertible first line \(\ell\) and a two-plane \(P\) containing it. The group \(G\) is transitive on invertible matrix lines over \(\mathbf C\): a determinant-normalizing scalar exists, and multiplying an invertible matrix by that scalar makes its determinant one. We may therefore put
\[
\ell=\mathbf C I,\qquad P=\mathbf C I+\mathbf C B,
\]
where \(B\) has distinct eigenvalues on a dense open set.

To stabilize \(\ell\), one must have
\[
gh^t=cI,\qquad c^n=1.
\]
The scalar \(c\) has only finitely many possibilities. The additional condition of stabilizing \(P\) says
\[
gBg^{-1}=aI+bB,\qquad b\ne0.
\tag{SF3}
\]
An affine transformation \(x\mapsto a+bx\) satisfying SF3 must permute the finite set of \(n\) distinct eigenvalues of \(B\). There are only finitely many such affine transformations: the images of two distinct eigenvalues determine \(a,b\). Therefore the identity component of the flag stabilizer has \(c=1,a=0,b=1\), and is exactly the centralizer of \(B\) in \(SL_n\). Since \(B\) is regular semisimple, that centralizer is the diagonal torus in an eigenbasis and has dimension \(n-1\).

The generic orbit dimension is consequently
\[
2(N-1)-(n-1)=2N-n-1,
\]
while the partial flag dimension is \(2N-3\). Its generic codimension is
\[
(2N-3)-(2N-n-1)=n-2.
\tag{SF4}
\]
For every \(n\ge3\), it is positive, so no open orbit exists even at \(r=2\). The dense-open regular-semisimple calculation suffices: any open orbit would meet that dense set and would have to have the incompatible smaller dimension.

For \(r=1\), by contrast, the invertible matrix lines themselves form an open \(G\)-orbit in \(\mathbf P(E)\). The associated determinant-power invariant rule is the familiar trivial-output Kronecker case. Thus the argument has a genuine boundary: for equal height \(n\ge3\), it excludes this open-orbit mechanism at every output-length bound \(2\le r\le n^2\), while leaving the one-row case.

## 5. Interpretation and checks

The known height-two rule is constructive because an actual polynomial highest-weight algebra has been proved there. The calculations above show exactly why its open-orbit premise fails when the two equal heights are at least three, including output length two. They do not show that the invariant algebra has no useful generators, no standard monomial theory, no positive basis, or no efficient counting formula. A multiplicity-bearing algebra can admit all of those structures without being multiplicity free; the open-orbit proof is one particularly restrictive route.

No part of this argument uses a Frobenius spectrum, a nonstandard quantum-group RH, or an unproved transfer from purity. SF1–SF4 are elementary dimension and stabilizer calculations for the specified ordinary actions.

The complete flag dimension, partial flag dimension, full tensor comparison, monotonicity for \(r\ge3\), and generic \(r=2\) stabilizer have been derived explicitly. The precise source input is the existing Manivel construction; its theorem is cited, not reproved. A fresh review of this note has been requested separately.

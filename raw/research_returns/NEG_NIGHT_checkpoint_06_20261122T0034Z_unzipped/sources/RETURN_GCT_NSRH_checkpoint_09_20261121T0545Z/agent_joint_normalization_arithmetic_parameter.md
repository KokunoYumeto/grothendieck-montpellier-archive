# F65 arithmetic-parameter supplement: exact two-constant classification

Author: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting is not exposed. Date: 2026-11-21 UTC.

This is separate from the frozen F65 joint-normalization report and fragment. It removes the rational-power form of the parameter rule, while retaining a fixed arithmetic parameter and its actual extension powers. It is a scalar classification for two printed constants, not a construction or exclusion of all nonstandard canonical categories.

## 1. Exact constants and comparison

The actual multiplication constants in VIII Figure2, printed p34, are
\[
\begin{aligned}
 d(q)&=c(\gamma_1^1,\gamma_1^1;\Sigma)=q+2+q^{-1},\\
 c(q)&=c(\gamma_2^1,\gamma_1^1;\gamma_{21}^1)
       =-q^2+q+q^{-1}-q^{-2}.
\end{aligned}
 \tag{AP1}
\]
The complete primary/source-normalization audit is in agent_joint_normalization_gate.md, frozen SHA256
7a97eee4d519d31ae3759dd28f2e679e5377b715df221af239bd1edb4fa1b006.
No ambient transition coefficient is used in the present theorem.

Fix a prime power Q>1, a prime ell not dividing Q, and a nonzero algebraic number beta. Choose an ell-adic embedding and a finite coefficient extension containing beta. A proposed arithmetic parameter comparison evaluates the source parameter at
\[
                              q_{\rm src}=\beta^n
 \tag{AP2}
\]
at extension degree n. This is an actual fixed-parameter power law, not an independently retuned value at each degree.

### Proposition AP-A

The following are equivalent:

1. There exist bounded pure point complexes D and C over F_Q, each of one integral Deligne weight (their weights may differ), such that
\[
       \operatorname{Tr}_{\rm Eul}(F^n;D)=d(\beta^n),\qquad
       \operatorname{Tr}_{\rm Eul}(F^n;C)=c(\beta^n)
 \tag{AP3}
\]
for every sufficiently large integer n.
2. beta^3=1.

In the surviving cases the second sequence is identically zero, and any pure C in (AP3) is the zero object. Thus every non-root-of-unity parameter is excluded, as is every parameter for which the second raw coefficient remains nonzero at some extension degree.

The same classification holds if the complexes are required to have continuous arithmetic Galois actions: the witnesses for beta^3=1 have finite image.

## 2. The finite-spectrum facts used

For distinct nonzero roots alpha_j, the sequences alpha_j^n are linearly independent even eventually. Indeed, take as many consecutive sufficiently large n as there are roots. The corresponding matrix is a Vandermonde matrix times an invertible diagonal matrix.

For a bounded point complex pure of weight w, BBD5.1.8, pp126–127, places an eigenvalue of point weight m only in degree m-w. Every nonzero Euler multiplicity consequently has sign (-1)^(m-w), and each fixed root occurs in only one degree. A hidden eigenvalue cannot cancel between different cohomological degrees. Jordan blocks affect neither that condition nor the ordinary trace multiplicity.

In particular a pure complex with identically zero Euler traces is zero: grouped finite-spectrum uniqueness gives zero Euler multiplicity for every root, and the unique permitted degree then gives zero ordinary multiplicity.

## 3. Proof of necessity away from root collisions

First suppose beta is not 1 or -1. The three roots in
\[
                       d(\beta^n)=\beta^n+2+\beta^{-n}
 \tag{AP4}
\]
are distinct. Let w_D be the pure weight of D. The root 1 has point weight zero and positive Euler multiplicity 2. It therefore occurs in degree -w_D, which is even. Thus w_D is even.

The root beta occurs with positive Euler multiplicity 1. It must be pure of an integral point weight m, and its only permitted degree m-w_D must be even. Therefore m is even. The inverse root has point weight -m. This uses actual algebraic point weights of a visible eigenvalue; purity is not being inferred from an arbitrary choice of formal grading.

Suppose now that the four numbers
\[
                    \beta^2,\quad\beta,\quad
                    \beta^{-1},\quad\beta^{-2}
 \tag{AP5}
\]
are distinct. They have point weights 2m,m,-m,-2m, all even. The sequence
\[
                   c(\beta^n)
                  =-\beta^{2n}+\beta^n+\beta^{-n}-\beta^{-2n}
 \tag{AP6}
\]
has Euler multiplicities -1,+1,+1,-1. In a pure complex of any weight w_C, all four permitted degrees have the same parity. All nonzero Euler multiplicities would have the same sign, a contradiction.

A collision among AP5 requires beta^r=1 for some r in {1,2,3,4}: the differences of the exponents {2,1,-1,-2} have precisely these possible positive values. Thus this argument already excludes all parameters except roots of unity of orders 1,2,3 or4.

## 4. Complete collision check

If beta=1, then d(beta^n)=4 and c(beta^n)=0.

If beta has order3, then beta^2=beta^{-1} and beta^{-2}=beta, so AP6 cancels identically. The first sequence is still the genuine trace of the four eigenlines 1,1,beta,beta^{-1}, all of weight zero.

If beta=-1, then
\[
                     c(\beta^n)=2(-1)^n-2.
 \tag{AP7}
\]
The two distinct roots have weight zero and opposite Euler signs. No pure point complex of one weight can realize this sequence.

If beta has order4, then beta^2=beta^{-2}=-1, and
\[
                    c(\beta^n)
                       =\beta^n+\beta^{-n}-2(-1)^n.
 \tag{AP8}
\]
The three roots are distinct, all of weight zero, with both signs. Again purity is impossible.

This exhausts every possible collision. Necessity is proved.

## 5. Sufficiency and the exact degeneration

For beta^3=1 choose D to be the four-dimensional degree-zero Weil representation with eigenvalues
\[
                             1,\quad1,\quad\beta,\quad\beta^{-1},
\]
and choose C=0. This is pure of weight zero and satisfies AP3 for every n. All eigenvalues are roots of unity, so the representation has finite image and is continuous.

There is even an elementary finite-etale realization for these scalar witnesses. For beta=1 take four rational points. For a primitive cube root take the disjoint union
\[
                     \operatorname{Spec}F_Q
                      \ \sqcup\ \operatorname{Spec}F_{Q^3}.
\]
On geometric H^0, Frobenius acts by one fixed point and a three-cycle. Its eigenvalues are exactly 1,1,beta,beta^{-1}; there is no higher cohomology. The zero object supplies c. This is only a degenerate realization of the two scalar sequences, not a realization of the source algebra, its designated bases or a faithful generic grading.

The zero-complex assertion follows from Section2. Therefore, if a comparison also demands a nonzero pure object for the raw c coefficient, no beta satisfies that stronger requirement.

## 6. Relation to the frozen rational-scaling result

For beta=Q^a with nonzero rational a, beta is not a root of unity, so AP-A recovers the two-multiplication-constant conclusion JN-B without needing to assume that a was integral in advance.

The isolated beta=Q^(1/2) realization of c alone remains valid: it is the four-line pure weight-one complex in the frozen F65 report. AP-A requires the same arithmetic parameter law for both d and c. The companion d then fails purity, exactly as before.

The classification does not cover separately chosen extension values beta_n, inserted-operator traces, mixed coefficient complexes, or removal of the raw vanishing factor. It does not turn VIII's signed/factored positivity into a conjecture of raw pure point coefficients. It identifies a stronger necessary comparison gate, with its exact degenerate exceptions.

## 7. Separate dictionary and actual checks

The formal source variable and its assignment to an arithmetic coefficient line are distinct data. SGA3 I4.7.2–3 and cote90 scan17 provide split-torus action language; SGA6 V Sections2–3 and cote133 scan18 provide effective/virtual coefficient representation language. Neither framework supplies AP2 or AP3.

The bounded complexes fit SGA6 I Definition4.7 pp121–122 and Example4.8 p122. BBD5.1.5 and5.1.8 pp125–127 give the integral point-weight and pure-complex degree conventions. The finite Vandermonde, collision classification and explicit witnesses are proved above. No lambda-ring structure on the noncommutative word algebra is asserted.

Checks performed by the author:

1. Reused the visually verified exact Figure2 formulas, without identifying them with Figure1's ambient transition coefficients.
2. Proved eventual finite-spectrum uniqueness by a Vandermonde matrix.
3. Derived even w_D and even point weight m directly from positive multiplicities of the visible roots of d.
4. Listed all exponent differences of {2,1,-1,-2}, then checked all four possible small orders.
5. Constructed both sufficient finite-image Weil models and the primitive-order-three finite-etale permutation model.
6. Retained the zero-object and raw-coefficient scope explicitly.

This report has not changed the frozen F65 report, fragment or any root master file. Fresh independent review is requested.


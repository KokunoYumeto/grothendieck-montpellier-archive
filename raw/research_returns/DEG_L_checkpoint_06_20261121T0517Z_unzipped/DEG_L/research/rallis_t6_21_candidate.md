# Candidate T6.21: exact four-factor saturation and a maximal-order anchor

Status: author, root and bounds whole-proof reviews passed; promoted as DEG-L.T6.21. This file retains the candidate history. Date 2026-11-21. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. The product-lattice formulation was proposed by root; this agent checked it, supplied the explicit local calculation and wrote the complete proof below. Promotion followed the complete independent reviews.

## Proposed theorem T6.21

Let \(E\) be a Galois CM field, \(\mathcal O=\mathcal O_E\), \(d=[E:\mathbf Q]=2g\), and let \(c\) denote complex conjugation. Let
\[
 B_i=\mathbf C^g/\Phi_i(\Lambda_i),\qquad i=1,2,3,4,
\]
where each \(\Lambda_i\subset E\) is a full \(\mathbf Z\)-lattice. The four CM types satisfy the switch relation, so the diagonal orbit specified below consists of Hodge classes. The first homology has rank one over \(E\); simplicity and primitivity of the types are unnecessary.

Inside the degree-four Kunneth summand \(\bigotimes_i H^1(B_i,\mathbf Q)\), identify the rational diagonal orbit \(W\) with \(E\) by the injective map
\[
 \Theta(\kappa)(x_1,x_2,x_3,x_4)
   =\operatorname{Tr}_{E/\mathbf Q}
       (\kappa x_1x_2\bar x_3\bar x_4).
 \tag{T21.1}
\]
Exchanging the barred and unbarred labels gives the equivalent opposite switch convention. Put
\[
 \begin{aligned}
 M&=\left\langle x_1x_2\bar x_3\bar x_4:
                         x_i\in\Lambda_i\right\rangle_{\mathbf Z},\\
 M^+&=\mathcal O M
   =\Lambda_1^+\Lambda_2^+\overline{\Lambda_3^+}\,
                                  \overline{\Lambda_4^+},\\
 L&=(M^+)^{-1},\qquad
 M^\vee=\{\kappa\in E:\operatorname{Tr}(\kappa M)\subseteq\mathbf Z\}.
 \end{aligned}
 \tag{T21.2}
\]
Here \(M\) is a full additive lattice, \(M^+\) is an invertible fractional maximal-order ideal, and \(L\) is its ideal inverse.

### A. The two integral lattices and their exact index

The actual integral intersection lattice of the rational orbit is
\[
 W\cap H^4(B_1\times\cdots\times B_4,\mathbf Z)
     =\Theta(M^\vee).
 \tag{T21.3}
\]
The additive span of coefficient traces of products of the four **individually integral \(\mathcal O\)-coefficient eigenvectors** is exactly
\[
 \Theta(L).
 \tag{T21.4}
\]
Consequently
\[
 [M^\vee:L]
   =|\operatorname{Disc}(E)|\,[M^+:M].
 \tag{T21.5}
\]
This is an equality of actual integral intersection lattices, including at ramified primes; it does not assume integral eigenprojectors on the varying factors.

### B. Exact saturation exponent and a uniform anchor case

Let \(n(M)\) be the exponent of the finite group \(M^\vee/L\), equivalently the least positive integer with \(n(M)M^\vee\subseteq L\). If \(\mathfrak D\) is the different of \(E/\mathbf Q\), then
\[
 n(M)\mathbf Z
 =\{n\in\mathbf Z:n\mathfrak D^{-1}M^+\subseteq M\}.
 \tag{T21.6}
\]
Let \(e(M)\) be the exponent of \(M^+/M\), and let \(d_E>0\) generate \(\mathfrak D\cap\mathbf Z\). Then
\[
 e(M)\mid n(M)\mid d_E e(M).
 \tag{T21.7}
\]
In particular, at every prime unramified in \(E\), the saturation exponent equals the exponent of the corresponding part of the product-lattice hull quotient.

If **at least one** \(\Lambda_i\) is stable under \(\mathcal O\), then
\[
 M=M^+,
 \qquad [M^\vee:L]=|\operatorname{Disc}(E)|,
 \qquad n(M)=d_E.
 \tag{T21.8}
\]
Thus fixing one maximal-order factor eliminates every target-dependent saturation cost, even if the other three lattices have arbitrarily large core indices.

### C. Uniform integral division of primitive orbit classes with one anchor

Fix the input surface maps and integral input eigenvectors of T6.20(C), with nonzero period \(k_0\in\mathcal O\), and put \(N_0=|N_{E/\mathbf Q}(k_0)|\). Every integral class \(w\) in the orbit (T21.3), primitive or otherwise, has
\[
 N_0 n(M)\,w
\]
as the cohomology class of an integral algebraic cycle constructed from the fixed surface and the divisor kernels of T6.20(C). If one output factor has maximal-order action, the same integer
\[
 N_0d_E
 \tag{T21.9}
\]
works for every primitive integral orbit class and every choice of the other three output lattices. In particular it is at most \(N_0|\operatorname{Disc}(E)|\). This supplies a genuine uniform division bound for this stated family of integral Hodge classes; it does not bound the degrees or the sizes of integer coefficients in a chosen cycle representative.

### D. All four mixed principal lattices can have growing saturation

Take the actual principal-polarization families of T6.19, at a completely split prime \(p\) outside the fixed bad set. In one conjugate pair use, for all four output homology lattices,
\[
 L_r=\mathbf Z_p(1,0)+\mathbf Z_p(p^{-r},1),
\]
with complex conjugation swapping the two coordinates. Apply the bars in (T21.2) to the third and fourth factors. The resulting product lattice and hull in this pair are
\[
 M_{r,p}
   =p^{-r}\mathbf Z_p^2+
           \mathbf Z_p p^{-2r}(1,1),
 \qquad
 M_{r,p}^+=p^{-2r}\mathbf Z_p^2.
 \tag{T21.10}
\]
Their quotient is cyclic of order \(p^r\). Equivalently,
\[
 \begin{aligned}
 M_{r,p}^\vee
  &=\{(x,y)\in p^r\mathbf Z_p^2:x+y\in p^{2r}\mathbf Z_p\},\\
 L_{r,p}^{\mathrm{fact}}&=p^{2r}\mathbf Z_p^2,\\
 M_{r,p}^\vee/L_{r,p}^{\mathrm{fact}}&\simeq\mathbf Z/p^r\mathbf Z.
 \end{aligned}
 \tag{T21.11}
\]
The class of \(p^r(1,-1)\) generates the last quotient. Modifying all \(g\) conjugate pairs gives a direct sum of \(g\) such quotients. Thus
\[
 v_p([M_r^+:M_r])=gr,
 \qquad v_p(n(M_r))=r.
 \tag{T21.12}
\]
All other prime contributions are fixed. There exist globally primitive integral Hodge classes whose image in this saturation quotient has order \(p^r\). Their expression in the factorwise integral trace lattice requires that \(p\)-denominator. This is a sharp statement about the factorized construction and its saturation, not a lower bound for the intrinsic algebraic-cycle denominator over all possible constructions.

## Proof

### The orbit as an integral multilinear form

Each \(H^1(B_i,\mathbf Q)\) is \(\operatorname{Hom}_{\mathbf Q}(E,\mathbf Q)\). Its integral lattice is \(\operatorname{Hom}_{\mathbf Z}(\Lambda_i,\mathbf Z)\). Since the four lattices are free of finite rank, their tensor product identifies with the integral multilinear forms on \(\Lambda_1\times\cdots\times\Lambda_4\). Integral Kunneth makes this tensor product a direct summand of \(H^4(\prod_i B_i,\mathbf Z)\), with no factorial or torsion correction.

Formula (T21.1) is injective: if it vanishes identically, set the last three rational arguments equal to 1 and use nondegeneracy of the field trace pairing on the first argument. After extending coefficients to \(E\), it is the sum of the Galois conjugates of the tensor with embedding labels \((1,1,c,c)\). These conjugates lie in distinct eigenspaces, so its image is exactly the specified rational diagonal orbit. The switch relation says that every one of these conjugates has type \((2,2)\).

Integrality of the multilinear form is precisely the condition \(\operatorname{Tr}(\kappa M)\subseteq\mathbf Z\), proving (T21.3). The lattice \(M\) is finitely generated by products of four chosen integral bases. It has full rational rank: fixing nonzero elements in three factors puts a nonzero scalar multiple of the full first lattice inside it. Expanding the maximal-order hulls shows directly that \(\mathcal O M\) is the displayed product ideal in (T21.2).

### Individually integral eigenvectors and the index

By T6.18, the actual integral coefficient line for the identity embedding in the first factor is \((\Lambda_1^+)^{-1}e_1\); the second is analogous. The conjugate lines in the last two factors have coefficient ideals \(\overline{\Lambda_3^+}^{-1}\) and \(\overline{\Lambda_4^+}^{-1}\). The additive span of products of their coefficients is exactly the product of these four ideals, namely \(L\). Coefficientwise field trace of their tensor products is \(\Theta\) applied to those products. This proves (T21.4), as equality of the actual additive spans. No division by \([E:\mathbf Q]\) is used in this trace convention.

Trace duality reverses indices of full additive lattices, giving
\[
 [M^\vee:(M^+)^\vee]=[M^+:M].
\]
For the fractional maximal-order ideal \(M^+\), trace duality gives
\[
 (M^+)^\vee=\mathfrak D^{-1}(M^+)^{-1}
                    =\mathfrak D^{-1}L.
\]
Therefore
\[
 [(M^+)^\vee:L]=N_{E/\mathbf Q}(\mathfrak D)
                     =|\operatorname{Disc}(E)|.
\]
Multiplying the two indices proves (T21.5). This argument incorporates the different exactly, so it remains valid at ramified primes.

### The saturation exponent and an integral maximal-order factor

For a positive integer \(n\), dualizing the inclusion \(nM^\vee\subseteq L\) gives
\[
 L^\vee\subseteq n^{-1}M.
\]
The fractional ideal duality formula says \(L^\vee=\mathfrak D^{-1}M^+\). This proves (T21.6). Since \(\mathfrak D^{-1}\supseteq\mathcal O\), any such \(n\) also satisfies \(nM^+\subseteq M\); hence \(e(M)\mid n(M)\). Conversely,
\[
 d_E e(M)\mathfrak D^{-1}M^+
  \subseteq e(M)M^+\subseteq M,
\]
so \(n(M)\mid d_E e(M)\). This proves (T21.7).

If, for example, \(\Lambda_1\) is \(\mathcal O\)-stable, multiplication of a generating product in \(M\) by any \(a\in\mathcal O\) can be absorbed into its first factor. Thus \(M\) itself is \(\mathcal O\)-stable and equals \(M^+\). The same argument works in a barred factor because conjugation preserves \(\mathcal O\). Since this ideal is invertible, condition (T21.6) then reduces to
\[
 n\mathfrak D^{-1}\subseteq\mathcal O,
 \quad\hbox{equivalently }n\in\mathfrak D.
\]
Its least positive integer is exactly \(d_E\), proving (T21.8). The bound \(d_E\le|\operatorname{Disc}(E)|\), and indeed divisibility by it, follows because the finite group \(\mathcal O/\mathfrak D\) has order \(|\operatorname{Disc}(E)|\), so its order kills it.

For part (C), write \(w=\Theta(\kappa)\) with \(\kappa\in M^\vee\). By definition, \(n(M)\kappa\in L\). Formula (T21.4) writes \(n(M)w\) as a finite integral sum of coefficient traces of factorwise integral eigenvector products. T6.20(C) supplies, for each term, a rational algebraic cycle whose class is that term and whose denominator divides the same \(N_0\). Summing these cycles proves that \(N_0n(M)w\) is represented by an integral algebraic cycle. In the anchor case \(n(M)=d_E\), proving (T21.9). No bounds on the finite sum's coefficients or degrees are inferred.

### The explicit principal family and its saturation quotient

Choose the split prime outside the finitely many primes at which any base lattice differs from \(\mathcal O\), or any fixed Riemann form is not unimodular on that lattice. Use the common idempotent coordinates of \(E\otimes\mathbf Q_p\); the trace is the sum of these coordinates and conjugation swaps each conjugate pair. On a given pair the four Riemann forms have matrices \(u_i\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), with possibly different units \(u_i\in\mathbf Z_p^\times\). The determinant-one shear defining \(L_r\) preserves each such form, so the same displayed \(L_r\) is self-dual for all four pairings. Thus no separate unit rescaling of the four coordinate systems is needed. The local-to-global construction of T6.19 realizes exactly these four modifications by actual principally polarized CM varieties.

In one pair let \(e=(1,0)\), \(f=(0,1)\), and \(q=p^{-r}\). The first two factors have generators \(e\) and \((q,1)\), and the conjugated last two have generators \(f\) and \((1,q)\). Multiply componentwise. A product containing both an \(e\) and an \(f\) is zero. The remaining products generate \(qe\), \(qf\), and \(q^2(e+f)\); they also generate \(e,f\), which already belong to \(q\mathbf Z_p^2\). This proves (T21.10).

After multiplication by \(p^{2r}\), the hull becomes \(\mathbf Z_p^2\) and the product lattice becomes
\[
 p^r\mathbf Z_p^2+\mathbf Z_p(1,1).
\]
The quotient is identified with \(\mathbf Z/p^r\mathbf Z\) by subtracting the two coordinates. This proves the hull quotient assertion. Taking its trace dual before scaling gives the first formula of (T21.11): pairing with \(p^{-r}e,p^{-r}f\) forces \(x,y\in p^r\mathbf Z_p\), and pairing with \(p^{-2r}(e+f)\) forces \(x+y\in p^{2r}\mathbf Z_p\). The inverse hull ideal is \(p^{2r}\mathbf Z_p^2\). Its quotient in the trace dual is generated by \(p^r(1,-1)\) and has order \(p^r\).

Different coordinate pairs contribute independent direct summands. The base lattice at \(p\) is the full product maximal-order lattice, so vectors supported on a single pair are available in every factor. Thus the local product module is the direct sum of the computed modules. Its hull index is \(p^{gr}\) and its quotient exponent is \(p^r\), proving (T21.12). Outside \(p\), all input lattices in this product calculation remain fixed.

Finally, the global finite group \(M^\vee/L\) has this prescribed \(p\)-primary part. Lift an element whose \(p\)-primary order is \(p^r\) to the integral global orbit lattice. The lift is not divisible by \(p\): otherwise its image would be \(p\) times an element in a group whose \(p\)-primary exponent is only \(p^r\), so its \(p\)-primary order would be at most \(p^{r-1}\). Divide the lift by its full integral content. That content is prime to \(p\), so the order \(p^r\) in the saturation quotient is preserved. The resulting class is primitive in the orbit intersection lattice, and hence in ambient integral cohomology because intersection with a rational subspace is saturated. This gives a globally primitive integral Hodge class with the claimed necessary presentation denominator. It does not prove that every algebraic cycle representing this class has that denominator. QED.

## Relation to the main normalization question

T6.20 removes every variable input-isogeny period denominator and gives a fixed denominator on the factorized integral trace lattice. T6.21 identifies the remaining integral-lattice comparison exactly. It closes the primitive-division gate when one output factor has maximal-order action, and it isolates a computable product-lattice exponent when none does.

This is a four-factor full-CM orbit. It is not B23's middle \(K\)-Weil determinant plane, whose integral pushforward content is a relative norm ideal. The exact comparison with such a target still requires its actual correspondence. Nor does a growing factorized-lattice saturation exponent prove an intrinsic integral Hodge obstruction: an additional Chow divisibility relation or a different cycle construction can enlarge the available integral cycle lattice.

## Primary sources and checks

The new identities are proved above from integral Kunneth, the field trace pairing and lattice duality. The trace-dual conventions and fractional-ideal duality are Keith Conrad, *The Different Ideal*, Definition 3.2 p.4, Theorem 3.9 p.8, Definition 4.1 p.9; the norm of the different equals the absolute discriminant by Theorem 4.8 p.11, whose full trace-Gram-determinant proof was independently read. Author URL: <https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf>.

Actual principal lattice realization is the complete local-to-global construction in candidate T6.19; no additional moduli existence assertion is imported. The uniform cycle denominator uses precisely part (C) of candidate T6.20. Both predecessor candidates retain their stated coefficient and Chow-divisibility scope.

## Check status

The entire revised saved proof was read by the author, root and bounds; all reviews passed before promotion. The common-idempotent and global primitivity refinements were included in the final reads. No computation in a proof assistant is claimed.

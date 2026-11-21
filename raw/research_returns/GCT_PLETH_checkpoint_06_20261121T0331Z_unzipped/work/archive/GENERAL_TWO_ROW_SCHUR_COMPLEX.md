# The exact two-row quotient complex and its cohomology

Reviewer/contributor: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.

Work over \(\mathbf Q\). Let \(L\hookrightarrow E\) be an inclusion of a line bundle into a rank-four bundle with locally free quotient \(Q\). For integers \(a\ge b\ge0\), the following construction fixes every map in the two-row Schur complex. On the five-point projective space it also proves all cohomology assertions in the region \(c\ge2k\).

## 1. The signed tensor construction

Put \(N=a+b\), and regard
\[
C=[L\longrightarrow E]
\]
as a cochain complex with \(L\) in degree \(-1\) and \(E\) in degree zero. The symmetric group \(S_N\) acts on \(C^{\otimes N}\) by the **Koszul signed** permutation of tensor positions. Interchanging two \(L\)-positions contributes a minus sign; interchanging an \(L\)-position with an \(E\)-position does not.

For a tensor whose \(L\)-positions form \(J\subset\{1,\ldots,N\}\), the differential is the specified map
\[
d(v_1\otimes\cdots\otimes v_N)
=\sum_{r\in J}(-1)^{|J\cap\{1,\ldots,r-1\}|}
v_1\otimes\cdots\otimes\iota(v_r)\otimes\cdots\otimes v_N.
\tag{S.1}
\]
Here \(\iota:L\to E\) is the given inclusion. The two terms that replace any fixed pair of \(L\)-positions cancel, so \(d^2=0\). The signed permutation action commutes with this differential.

Take the row-filled standard tableau \(T\) of shape \((a,b)\). Let \(r_T\) be its row symmetrizer, \(c_T\) its column antisymmetrizer, and \(h_{a,b}\) its hook-length product. Use the explicit primitive Young idempotent
\[
e_T=h_{a,b}^{-1}c_Tr_T\in\mathbf Q[S_N].
\]
For \(N=0\), use the identity on the tensor unit. Define the Schur complex to be the image
\[
\mathcal S_{a,b}(C)=e_T C^{\otimes N},
\tag{S.2}
\]
with differential the restriction of (S.1). Its degree-zero term is the same Young-idempotent realization of \(S_{(a,b)}E\), and its augmentation is induced by the actual quotient \(E\to Q\).

### Exactness and tensoring by a nonflat ideal

Locally choose a splitting \(E=L\oplus Q\). The complex \(C\) then contracts onto \(Q\) in degree zero. Tensoring the contraction gives a homotopy of \(C^{\otimes N}\) onto \(Q^{\otimes N}\). Average that homotopy over \(S_N\). The augmentation and the chosen inclusion of \(Q^{\otimes N}\) commute with the signed action, so the averaged homotopy still satisfies the same contraction identity and now commutes with \(e_T\).

Restricting it to the idempotent image proves that (S.2) contracts locally onto \(S_{(a,b)}Q\). In particular its augmented complex is locally split exact. The homotopy is \(\mathcal O\)-linear; tensoring it with any specified ideal preserves the identity. Thus tensoring this complex with \(\mathcal I^k(c)\) preserves exactness without a flatness requirement on the ideal.

## 2. The three terms and completely specified comparison maps

The term of tensor degree \(-j\) is, before applying \(e_T\),
\[
\operatorname{Ind}_{S_{N-j}\times S_j}^{S_N}
\left(E^{\otimes(N-j)}\otimes L^{\otimes j}\otimes\operatorname{sgn}_{S_j}\right).
\tag{S.3}
\]
The induction map places the \(j\) line factors into the selected tensor positions; its signs are those of (S.1). The sign in (S.3) is essential. In particular the two-line term for an exterior square contains \(L^2\).

Frobenius reciprocity and the exterior Pieri rule identify the idempotent image with
\[
L^j\otimes
\bigoplus_{\nu:\ (a,b)/\nu\text{ is a vertical strip of size }j}S_\nu E.
\tag{S.4}
\]
For completeness, the Pieri multiplicities are exactly one by the alternant identity. Multiplying the alternant for \(s_\nu\) by \(e_j\) is the sum of alternants obtained by increasing \(j\) distinct exponents by one. An exponent collision makes the alternant zero. All other terms remain in decreasing order and correspond precisely to adding at most one box in each row. Dividing by the Vandermonde alternant gives
\[
e_j s_\nu=\sum_{\lambda/\nu\text{ vertical }j\text{-strip}}s_\lambda.
\]
The Frobenius-character isometry used for the Specht projector therefore gives the multiplicity-one branching in (S.4).

Here is an exact finite prescription for the maps in (S.4), which avoids leaving their scalar choices implicit. Realize every Specht module as the rational polytabloid span, with tableaux in lexicographic order. Apply the sign averaging projector on the last \(j\) letters to the Specht module of shape \((a,b)\). For each allowed \(\nu\), solve the intertwiner equations for the adjacent transpositions of \(S_{N-j}\) by rational Gaussian elimination. The preceding multiplicity calculation proves that this solution space is one-dimensional. Choose its first nonzero solution with first nonzero coordinate equal to one. The direct sum of these intertwiners is an isomorphism onto the sign-projected space; invert its rational matrix.

Composition with these inverse projections gives the maps between the corresponding Schur functors. The Frobenius-reciprocity map itself is explicit: an intertwiner \(f\) to the subgroup module is sent to
\[
v\longmapsto\sum_{gH\in S_N/H}g\otimes f(g^{-1}v),
\qquad H=S_{N-j}\times S_j,
\]
and its inverse is projection to the identity coset. Finally the identification with the primitive-idempotent image is evaluation at \(e_T\):
\[
\operatorname{Hom}_{\mathbf Q[S_N]}(\mathbf Q[S_N]e_T,V)
\longrightarrow e_TV,\qquad f\longmapsto f(e_T),
\]
with inverse \(v\mapsto(ae_T\mapsto av)\).

These prescriptions use rational matrices independent of the local frame of \(E\). They commute with frame change, so they define actual bundle isomorphisms. Conjugating (S.1) by them specifies the displayed Schur-functor differentials.

There are at most two rows, so no vertical strip has more than two boxes. The complex is consequently
\[
0\longrightarrow L^2\otimes S_{(a-1,b-1)}E
\longrightarrow
L\otimes\left(S_{(a-1,b)}E\oplus S_{(a,b-1)}E\right)
\longrightarrow S_{(a,b)}E
\longrightarrow S_{(a,b)}Q\longrightarrow0,
\tag{S.5}
\]
with only the valid partition terms retained. The vanishing in degrees \(j>2\) can also be seen directly: three odd line entries in two rows force two identical odd entries in one row, whose graded row symmetrizer is zero.

The boundary conventions are explicit:

- At \(a=b>0\), omit \(S_{(a-1,b)}E\); retain \(S_{(a,b-1)}E\) and the two-line term.
- At \(b=0<a\), the complex is the ordinary symmetric-quotient sequence \(L\operatorname{Sym}^{a-1}E\to\operatorname{Sym}^aE\to\operatorname{Sym}^aQ\).
- At \(a=b=0\), the augmentation is the identity on \(\mathcal O\).
- At \(a=b=1\), the maps are \(l^2\mapsto l\otimes l\) and \(l\otimes e\mapsto l\wedge e\).
- At \(b=1\), decomposing \(E\otimes\operatorname{Sym}^{a-1}E\) by polarization identifies (S.5) with the complete hook complex already checked in A-035.

## 3. Higher cohomology on the five-point projective space

Now take \(E=\mathfrak h_5\) on \(\mathbf P(E)\), \(L=\mathcal O(-1)\), and the actual five-point ideal \(\mathcal I\). Let \(k\ge0\) and \(c\ge2k\). Tensor (S.5) by \(\mathcal I^k(c)\), and place its three terms \(F_2,F_1,F_0\) in cochain degrees \(-2,-1,0\).

The scalar cohomology facts needed here are complete:

1. \(H^{q>0}(\mathcal I^k(c))=0\). For \(k\ge2\) this follows from A-029; for \(k=1\), the degree-two evaluation and its higher-degree versions give it; for \(k=0\), it is the usual cohomology of \(\mathcal O(c)\).
2. \(H^2(\mathcal I^k(m))=0\) for all the twists in the complex. The finite-support quotient \(\mathcal O/\mathcal I^k\) has no higher cohomology, and \(H^2(\mathcal O(m))=0\) on \(\mathbf P^3\).
3. \(H^3(\mathcal I^k(m))=0\) for these twists, because \(m\ge c-2\ge-2\) and \(H^3(\mathcal O(m))=0\) there.

The cohomology spectral sequence for this bounded complex has no term of positive total degree: \(F_0\) has only \(H^0\), and the only possible additional cohomology of \(F_1,F_2\) is \(H^1\), in total degrees zero and minus one. The complex is quasi-isomorphic to the displayed quotient sheaf in degree zero. Therefore
\[
\boxed{
H^{q>0}\!\left(\mathbf P(E),
\mathcal I^k(c)\otimes S_{(a,b)}Q\right)=0
\quad(a\ge b\ge0,\ k\ge0,\ c\ge2k).
}
\tag{S.6}
\]
This proof includes \(k=1,c=2\). Possible \(H^1(\mathcal I(0))\) and \(H^1(\mathcal I(1))\) appear only in nonpositive total degrees; no additional assertion about a map between them is needed for (S.6).

## 4. The exact Euler representation and jet evaluation

Write \(\chi(\mathcal I^k(m))\) for the exact alternating cohomology class. The locally split complex and (S.6) give
\[
\begin{aligned}
[H^0(\mathcal I^k(c)\otimes S_{(a,b)}Q)]
={}&[S_{(a,b)}E]\,\chi(\mathcal I^k(c))\\
&-\left([S_{(a-1,b)}E]+[S_{(a,b-1)}E]\right)
\chi(\mathcal I^k(c-1))\\
&+[S_{(a-1,b-1)}E]\,\chi(\mathcal I^k(c-2)),
\end{aligned}
\tag{S.7}
\]
with the same valid-partition convention.

Every twist here is at least \(-2\). The actual jet-coordinate map of A-033 gives
\[
\operatorname{tr}\bigl(g\mid\chi(\mathcal I^k(m))\bigr)
=h_m(g)-m_1(g)h_{k-1}(g),
\tag{S.8}
\]
where \(h_m=0\) for negative \(m\). The invariant form identifies the symmetric powers of \(E^*\) with those of \(E\). At \(k=0\), the jet term is zero. At \(k=1,c=2\), the three scalar classes are respectively \(U,-\mathbf1,-E\), so (S.7) retains both exceptional scalar cohomology contributions exactly.

Equations (S.1)–(S.8) provide the maps, all boundary cases, the required vanishing and the exact finite-group Euler character for every two-row quotient shape in the stated region.

# Small positive chamber formulas in outer degree four

## T-033. The two exact branching steps

Let \(W=\mathfrak h_4\otimes\operatorname{sgn}\), where \(\mathfrak h_4\) is the three-dimensional standard representation of \(S_4\). Its invariant dot product is nondegenerate, and
\(\det(W)=\operatorname{sgn}\cdot\operatorname{sgn}^3=1\). Thus its actual representation map factors as
\[
S_4\longrightarrow SO(W)\subset GL(W).
\tag{H.1}
\]
Over \(\mathbf C\), write \(H_L\) for the irreducible \(SO_3\)-module of angular momentum \(L\), with character \(\sum_{j=-L}^L z^j\) on \(\operatorname{diag}(z,1,z^{-1})\).

For nonnegative integers \(c,b\), set
\[
A=\max(c,b),\qquad s=\min(c,b).
\]
The exact restriction of \(S_{(c+b,b)}W\) to \(SO(W)\) is the following direct sum, with every pair \((K,L)\) providing one summand:
\[
\boxed{
S_{(c+b,b)}W\big|_{SO(W)}
\simeq
\bigoplus_{\substack{K=s,s-2,\ldots\\K>0}}
\ \bigoplus_{L=K}^{K+A}H_L
\ \oplus\
\begin{cases}
\displaystyle\bigoplus_{j=0}^{\lfloor A/2\rfloor}H_{A-2j},
&s\text{ even},\\[2mm]
0,&s\text{ odd}.
\end{cases}}
\tag{H.2}
\]
This is the classical Elliott branching rule, proved below in the precise convention used here.

For each \(\tau\vdash4\), define the finite tag sets
\[
\begin{array}{c|c}
\tau&E_\tau\\ \hline
(4)&\{0,9\}\\
(1,1,1,1)&\{3,6\}\\
(2,2)&\{2,4,5,7\}\\
(3,1)&\{2,3,4,5,6,7\}\\
(2,1,1)&\{1,3,4,5,6,8\}.
\end{array}
\tag{H.3}
\]
Then the second restriction in (H.1) has the exact positive multiplicity formula
\[
\boxed{
[\tau:H_L]
=\sum_{e\in E_\tau}
\#\{(x,y)\in\mathbf Z_{\ge0}^2:4x+6y=L-e\}.}
\tag{H.4}
\]
An equation with negative right side contributes zero.

### 1. Full character proof of the Elliott rule

The three-variable Weyl determinant, specialized to \((z,1,z^{-1})\), gives
\[
\chi_{c,b}(z)
=z^{-(c+b)}
\frac{(1-z^{c+1})(1-z^{b+1})(1-z^{c+b+2})}
{(1-z)^2(1-z^2)}.
\tag{H.5}
\]
For example this follows by dividing the alternant with exponents \(c+b+2,b+1,0\) by the alternant with exponents \(2,1,0\), then factoring their Vandermonde products after substitution. Formula (H.5) is symmetric in \(c,b\), so one may put \(c=A,b=s\) in the ensuing identity without changing the character.

Let \(P(z)\) be the sum of \(z^L\) over all the pairs \((K,L)\) in (H.2), with repetitions retained. Finite geometric summation yields
\[
P(z)=
\frac{z-z^{A+2}-z^{s+2}+z^{A+s+3}
+\delta(1-z)^2}{(1-z)(1-z^2)},
\quad
\delta=
\begin{cases}1,&A,s\text{ both even},\\0,&\text{otherwise}.\end{cases}
\tag{H.6}
\]
Here the positive-\(K\) terms sum
\(\sum_{j=0}^{\lfloor(s-1)/2\rfloor}
z^{s-2j}(1-z^{A+1})/(1-z)\);
when \(s\) is even, the final band contributes
\(\sum_{j=0}^{\lfloor A/2\rfloor}z^{A-2j}\).
Adding these two displayed finite geometric series gives (H.6), separately for the parities of \(A,s\).

Now
\[
P(z)-z^{-1}P(z^{-1})
=(1-z^{-1})\chi_{c,b}(z).
\tag{H.7}
\]
For a direct verification, the \(\delta\) term in (H.6) equals \(\delta/(1+z)\), whose contribution to the left side vanishes. The remaining numerator of that side, with denominator \((1-z)(1-z^2)\), is
\[
-z^{A+2}-z^{s+2}+z^{A+s+3}
+z^{-A}+z^{-s}-z^{-A-s-1}.
\]
Expanding the numerator of the right side using (H.5) gives exactly the same six terms. Finally,
\[
(1-z^{-1})\sum_{j=-L}^{L}z^j=z^L-z^{-L-1}.
\]
Thus (H.7) says that (H.5) equals the sum of the characters \(H_L\) in (H.2). Complete reducibility of the compact \(SO_3\) action, followed by complexification, makes this equality of characters the asserted module decomposition.

The primary locator for the classical rule is D. J. Rowe, *Vector coherent state theory: a powerful tool for solving algebraic problems in physics*, submitted April 8, 2003, [§5, Theorem 1 (Elliott), equations (57)–(58), printed page 7](https://www.physics.utoronto.ca/site-archive/rowe/pdf/Erice.pdf). Those displayed ranges were opened and read in this run. The full calculation above specifies the symmetric \(A,s\) convention and also covers every zero boundary.

### 2. The harmonic trace and five exact character averages

The polynomial quotient
\[
H_L\simeq
\operatorname{Sym}^L W/
\bigl(Q\,\operatorname{Sym}^{L-2}W\bigr)
\tag{H.8}
\]
is the stated irreducible \(SO(W)\)-module, where \(Q\) is its invariant quadratic tensor and a negative symmetric power is zero. For a direct justification, after complexification the double cover
\(SL_2\to SO_3\) identifies \(W\) with \(\operatorname{Sym}^2\mathbf C^2\). One explicit realization is the adjoint action on trace-zero \(2\times2\) matrices, whose determinant is the invariant quadratic and whose kernel is \(\{\pm I\}\). A highest vector in \(\operatorname{Sym}^L W\) has \(SL_2\)-weight \(2L\); its \(L\)-th power is not divisible by the nondegenerate rank-three quadratic \(Q\). It supplies the irreducible \(\operatorname{Sym}^{2L}\mathbf C^2\) in the quotient. The quotient dimension is
\(\binom{L+2}{2}-\binom{L}{2}=2L+1\), exactly its dimension. This proves (H.8) and the displayed character of \(H_L\).

For \(g\in S_4\), taking traces in (H.8) gives
\[
\sum_{L\ge0}\operatorname{tr}(g\mid H_L)q^L
=\frac{1-q^2}{\det(1-qg\mid W)}.
\tag{H.9}
\]
In the class order \(1^4,2\,1^2,2^2,3\,1,4\), the class sizes are
\(1,6,3,8,6\). The eigenvalues of the signed standard representation \(W\) give the five trace series
\[
\frac{1+q}{(1-q)^2},\quad
\frac1{1+q},\quad
\frac1{1+q},\quad
\frac{1+q}{1+q+q^2},\quad
\frac{1+q}{1+q^2}.
\tag{H.10}
\]
The full character table in the same class order is
\[
\begin{array}{c|rrrrr}
(4)&1&1&1&1&1\\
(1^4)&1&-1&1&1&-1\\
(2,2)&2&0&2&-1&0\\
(3,1)&3&1&-1&0&-1\\
(2,1,1)&3&-1&-1&0&1.
\end{array}
\tag{H.11}
\]
These entries follow directly from the trivial and sign characters, the four-letter permutation character minus its constant subspace, its sign twist, and the three-matching permutation character minus its constant subspace. Their squared dimensions sum to \(24\), and their class inner products are the identity matrix, so these give all five irreducible characters with the indicated usual Specht labels.

Multiply each row of (H.11) entrywise by (H.10), weight by its class size, and divide by \(24\). A common-denominator calculation gives
\[
\sum_{L\ge0}[\tau:H_L]q^L
=\frac{\sum_{e\in E_\tau}q^e}{(1-q^4)(1-q^6)}.
\tag{H.12}
\]
Every numerator is listed explicitly in (H.3). Expanding the two geometric denominators proves (H.4). This calculation is the trace-average proof of the graded multiplicity version of Molien's formula; see Stanley (1979), Theorem 2.1, printed pages 479–480, already opened and checked in T-027. All five rational identities were also verified exactly by the accompanying symbolic script; the finite identity check supplements the derivation.

## T-034. The explicit chamber polytopes

Let \(\mu\vdash4\), \(n\ge0\), and
\(\lambda=(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\vdash4n\), with \(\lambda_2\le n\). Set
\[
c=\lambda_2-\lambda_3,\quad
b=\lambda_3-\lambda_4,\quad
d=\lambda_4,\quad A=\max(c,b),\quad s=\min(c,b),
\tag{H.13}
\]
and put \(\tau=\mu\) when \(c+d\) is even and \(\tau=\mu'\) when it is odd.

For every \(e\in E_\tau\), define the following bounded rational polytopes, each with the three integer variables \((j,x,y)\):
\[
\begin{aligned}
\mathcal P_e^+(A,s)
=\{(j,x,y)\in\mathbf R_{\ge0}^3:\quad&
2j\le s-1,\\
&s-2j\le4x+6y+e\le s-2j+A\},
\end{aligned}
\tag{H.14}
\]
and
\[
\mathcal P_e^0(A)=
\{(j,x,y)\in\mathbf R_{\ge0}^3:
2j+4x+6y=A-e\}.
\tag{H.15}
\]
The first polytope is empty when \(s=0\). Negative right sides make the second empty. Then
\[
\boxed{
p_{\mu,(n)}^\lambda
=
\sum_{e\in E_\tau}
\#\bigl(\mathcal P_e^+(A,s)\cap\mathbf Z^3\bigr)
+\mathbf1_{s\ {\rm even}}
\sum_{e\in E_\tau}
\#\bigl(\mathcal P_e^0(A)\cap\mathbf Z^3\bigr).}
\tag{H.16}
\]
This uses at most twelve fixed three-variable polytopes, without a degree-dependent precomputation or a plethysm coefficient oracle. Their tags are retained, so an integer point appearing in distinct polytopes contributes once for each corresponding summand.

### 3. Proof of the module transport and the lattice bijection

The exact chart T-032 gives
\[
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq S_{(\lambda_2,\lambda_3,\lambda_4)}\mathfrak h_4
\simeq(\det\mathfrak h_4)^d\otimes S_{(c+b,b)}\mathfrak h_4.
\tag{H.17}
\]
The second map is the exterior-column determinant shift from (F.5). Since \(\det\mathfrak h_4=\operatorname{sgn}\) and \(\mathfrak h_4=W\otimes\operatorname{sgn}\), homogeneity of the Schur functor gives the actual \(S_4\)-module isomorphism
\[
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq \operatorname{sgn}^{c+d}\otimes S_{(c+b,b)}W.
\tag{H.18}
\]
Indeed the latter Schur degree is \(c+2b\), whose parity is \(c\). Tensoring a Specht module by sign conjugates its partition, so the desired multiplicity is \([\tau:S_{(c+b,b)}W]\). Compose (H.2) and (H.4).

For each positive \(K\) in (H.2), write \(K=s-2j\). Its index condition is exactly \(j\ge0\), \(2j\le s-1\). For each harmonic tag \(e\), write \(L=4x+6y+e\). The range \(K\le L\le K+A\) is then exactly (H.14). The \(K=0\) band, present when \(s\) is even, has \(L=A-2j\); its equality with \(4x+6y+e\) is (H.15). Every index in the two branching sums has one and only one such tagged integer point, and the converse is immediate from these equations. This proves (H.16).

Boundedness is explicit: the first polytope bounds \(j\) by \((s-1)/2\) and \(4x+6y\) by \(A+s\); the second bounds all three nonnegative coordinates by its right side. In particular their description and all integer witnesses have bit length \(O(\log(n+2))\) for fixed outer degree four.

### 4. The other chamber and the exact extension problem completed in T-037

The complement map (F.12)–(F.15) covers every \(\lambda\) with \(\lambda_3\ge n\). Explicitly take
\[
H=\lambda_1,\qquad
\widehat\lambda=(H-\lambda_4,H-\lambda_3,H-\lambda_2,0),
\quad\widehat n=H-n,
\]
and let \(\widehat\mu=\mu\) for even \(H\) and \(\widehat\mu=\mu'\) for odd \(H\). Then
\[
p_{\mu,(n)}^\lambda
=p_{\widehat\mu,(\widehat n)}^{\widehat\lambda}.
\tag{H.19}
\]
The inequality \(\widehat\lambda_2\le\widehat n\) is exactly \(\lambda_3\ge n\), so (H.16) applies to the right side. Formula (H.19) is obtained from an actual perfect Schur-module pairing, including the sign and contragredient maps; it also covers equality at the chamber wall.

T-031 already gives direct formulas on every proper fundamental face for the symmetric outer partition. At this stage of the reductions, the symmetric-outer rank-four sector still requiring a direct chart computation has
\[
\lambda_1>\lambda_2>\lambda_3>\lambda_4,
\qquad \lambda_2>n>\lambda_3.
\tag{H.20}
\]
Its balanced module is precisely the \(S_4\)-stable divisibility subspace (C.15), with \(k=\lambda_2-n>0\), in the same rank-three flag module used above. T-035 identifies this subspace with vanishing along four flag fibers, and T-037 completes its positive decomposition for every parameter. Thus the chamber formulas above are now part of the full outer-four formula, with at most 108 fixed polytopes of at most five variables for arbitrary outer Schur labels. General terminating positive-polytope constructions remain available from G-009–G-011 in every rank.

## Exact checks and provenance

The companion script [check_chambers.py](check_chambers.py) verifies all five rational identities (H.12), the geometric-sum and full Elliott character identities for \(0\le c,b\le24\), their \(625\) Weyl dimensions, and \(1280\) tagged lattice-count comparisons. Its exact receipt is [CHAMBER_CHARACTER_CHECK.tsv](CHAMBER_CHARACTER_CHECK.tsv). These checks do not replace the symbolic proofs above. Independent cycle-index plethysm checks are recorded separately when completed.

The Elliott rule is classical and its precise primary locator is given above. The symmetric-group character average is explicitly calculated here. The purpose of the composition is the exact flag/normalizer transport and fixed small positive polytope list in the stated chambers. No historical novelty claim is made.


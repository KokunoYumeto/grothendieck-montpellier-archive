# A fixed positive polytope formula for every outer Schur partition of four

## T-037. Full statement and conventions

Let \(\mu\vdash4\), \(n\ge0\), and \(\lambda\vdash4n\) have at most four parts. There is an explicit formula for \(p_{\mu,(n)}^\lambda\) using at most **108 tagged bounded rational polytopes, each with at most five variables**. For the symmetric or exterior outer partition the bound is 36, and for \(\mu=(2,2)\) it is 72. All tags and equations are listed in §5. No character evaluation, invariant-ring elimination, or degree-dependent precomputation occurs in this formula.

For a valid output partition with more than four parts, the coefficient is zero. Indeed the Schur symmetrizer realizes \(S_\mu(\operatorname{Sym}^nV)\) inside \((\operatorname{Sym}^nV)^{\otimes4}\). Starting with the one-row representation \(\operatorname{Sym}^nV\), each of the next three tensor factors adds a horizontal strip by Pieri's rule, increasing the number of rows by at most one. Thus every output in that ambient tensor product has at most four rows. The evaluator includes this zero case and rejects inputs of the wrong size or order.

The proof uses the original action
\[
q\in\mathfrak h_4=[(3,1)],\qquad
t\in W=\mathfrak h_4\otimes\operatorname{sgn}=[(2,1,1)],
\qquad
R=\mathbf Q[q,t]/(q\cdot t),
\tag{A.1}
\]
with bidegrees \((1,0),(0,1)\). Thus the incidence equation transforms by sign. We do not retwist the \(q\)-action in the separation of variables below. This convention makes its evaluation at the four affine vectors \(\ell_i=e_i-\frac14\mathbf1\) the ordinary permutation representation in every degree at least two.

Let \(U=[(2,2)]\subset\operatorname{Sym}^2\mathfrak h_4\) be the two quadrics vanishing at the four points (V.3), and put
\[
J_R=UR,\qquad \mathcal H=R/J_R.
\tag{A.2}
\]
Then multiplication, after the explicitly specified equivariant choice of sections in §1, gives the graded \(S_4\)-module isomorphism
\[
\boxed{
R\simeq\operatorname{Sym}(U)\otimes\mathcal H.}
\tag{A.3}
\]
The degree of \(U\) is \((2,0)\). In particular
\[
\boxed{
(J_R^k)_{c,b}
\simeq\bigoplus_{j=k}^{\lfloor c/2\rfloor}
\operatorname{Sym}^j U\otimes\mathcal H_{c-2j,b}.}
\tag{A.4}
\]
The finite-group modules in this decomposition are explicit:
\[
\boxed{
\begin{array}{c|l}
C&\mathcal H_{C,b}\\ \hline
0&\operatorname{Sym}^b W\\
1&\displaystyle\operatorname{sgn}\otimes
       \bigoplus_{L=1}^{b+1}H_L\\
2&\displaystyle D_b\ \oplus\
       \operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W\\
C\ge3&D_b,
\end{array}}
\qquad
D_b=\operatorname{Ind}_{S_3}^{S_4}\operatorname{Sym}^b\mathfrak h_3.
\tag{A.5}
\]
A negative symmetric power is zero, and \(H_L\) is the \(SO(W)\) harmonic module restricted along the actual rotational \(S_4\) map (H.1).

### Orienting the partition by the exact complement map

Set \(a=\lambda_1-\lambda_2\) and \(b=\lambda_3-\lambda_4\). When \(a<b\), replace the input by
\[
H=\lambda_1,\quad
\lambda\longleftarrow(H-\lambda_4,H-\lambda_3,H-\lambda_2,0),
\quad n\longleftarrow H-n,
\quad \mu\longleftarrow\mu^{[H]},
\tag{A.6}
\]
where \(\eta^{[H]}=\eta\) for even \(H\) and \(\eta'\) for odd \(H\). The exact perfect pairing (F.12)–(F.15) proves that this replacement leaves the coefficient unchanged. It interchanges \(a,b\), so after at most one replacement \(a\ge b\).

For the resulting input put
\[
a=\lambda_1-\lambda_2,\qquad b=\lambda_3-\lambda_4,\qquad
c=\lambda_2-\lambda_3,\qquad d=\lambda_4,\qquad
k=\max(0,\lambda_2-n).
\tag{A.7}
\]
Then \(c\ge2k\). For \(k=0\) this is immediate. For \(k>0\), the size equation \(|\lambda|=4n\) gives
\[
c-2k=\frac{a-b}{2}\ge0.
\tag{A.8}
\]
The exact four-fiber model T-035 now gives the following positive module decomposition:
\[
\boxed{
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq \operatorname{sgn}^d\otimes
\left(
\bigoplus_{j=k}^{\lfloor c/2\rfloor}
\operatorname{Sym}^jU\otimes\mathcal H_{c-2j,b}
\ \oplus\
\mathbf1_{c=2k}\,
\operatorname{sgn}\otimes
\operatorname{Sym}^{k-1}U\otimes\operatorname{Sym}^{b-1}W
\right).}
\tag{A.9}
\]
The term with \(c=2k\) is the fully proved boundary term of T-036. The proof of (A.3)–(A.9) follows before the explicit polytope formula.

## 1. Four lines, a nonzerodivisor, and actual module freeness

Write
\[
S=\mathbf Q[q],\qquad A=S/(U).
\]
In the coordinates (V.5),
\[
A=\mathbf Q[X,Y,Z_0]/(X^2-Y^2,\ Y^2-Z_0^2).
\tag{A.10}
\]
This is the reduced coordinate ring of the four affine lines through the four projective points. Indeed its two equations form a complete intersection, the four projective points are reduced by the calculation in T-035, and the same ring is free over \(\mathbf Q[Z_0]\) with basis \(1,X,Y,XY\), using the monic equations \(X^2=Z_0^2,Y^2=Z_0^2\). It embeds in the product of the four line rings: localizing at \(Z_0\) makes that claim the four distinct roots \(X/Z_0,Y/Z_0=\pm1\); injectivity before localization follows from its freeness over \(\mathbf Q[Z_0]\). In particular no component supported at the origin is being discarded.

The image of \(\ell=q\cdot t\) is a nonzerodivisor in \(A[t]\). On each of the four line components it is a nonzero scalar line coordinate times the nonzero linear form \(\ell_i\cdot t\), so it is a nonzerodivisor in every component domain. The just-proved embedding into their product makes multiplication injective on \(A[t]\) itself.

Consequently the ordinary bigraded Hilbert series satisfy
\[
\operatorname{Hilb}(\mathcal H;s,t)
=\frac{(1-st)(1-s^2)^2}{(1-s)^3(1-t)^3}
=(1-s^2)^2\operatorname{Hilb}(R;s,t).
\tag{A.11}
\]
The first equality follows from the two regular quadrics in \(S\) and the injective multiplication by \(\ell\) just proved; the second follows from the one nonzero incidence equation in the polynomial ring.

For each bidegree, choose a rational linear right inverse \(s_0\) to \(R\to\mathcal H\) and replace it by
\[
s(h)=\frac1{24}\sum_{g\in S_4}g\,s_0(g^{-1}h).
\tag{A.12}
\]
This is an actual \(S_4\)-equivariant right inverse. Define the multiplication map
\[
\operatorname{Sym}(U)\otimes\mathcal H\to R,\qquad
p\otimes h\longmapsto p(U)\,s(h).
\tag{A.13}
\]
It is surjective: subtract the chosen lift of a quotient class, express the remainder in \(UR\), and repeat with strictly smaller \(q\)-degree. The source has the same Hilbert series as the target by (A.11). Each bidegree is finite-dimensional, so (A.13) is injective in each bidegree. This proves (A.3) as an equivariant \(\operatorname{Sym}(U)\)-module isomorphism. The ideal powers correspond to polynomials in \(U\) of total degree at least \(k\), proving (A.4). In particular the two elements of \(U\) form a regular sequence in \(R\).

The section (A.12) proves existence of the specified multiplication isomorphism; the explicit counts in §5 require neither its computation nor any averaging of degree-dependent vectors.

## 2. Every quotient piece \(\mathcal H_{C,b}\)

The evaluation map on the four affine vectors \(\ell_i\) gives
\[
A_0=\mathbf1,\qquad A_1=\mathfrak h_4,\qquad
A_C\simeq\operatorname{Perm}_4\quad(C\ge2).
\tag{A.14}
\]
Here evaluation has no parity twist, since the original standard action sends \(\ell_i\) exactly to \(\ell_{\sigma(i)}\). For completeness, in the coordinates (V.5), the four functions \(X^2,XY,XZ_0,YZ_0\) have linearly independent evaluations, so degree two evaluation is onto. In degree three use \(XYZ_0,X^3,Y^3,Z_0^3\). The invariant quadratic \(X^2+Y^2+Z_0^2\) is a nonzero constant on the four selected vectors; multiplication by it extends surjectivity by two degrees. The Hilbert series
\[
\operatorname{Hilb}(A;s)=\frac{(1-s^2)^2}{(1-s)^3}
=1+3s+4s^2+4s^3+\cdots
\]
then proves that every stated surjection is an isomorphism.

Since \(\ell=q\cdot t\) has sign character and is a nonzerodivisor on \(A[t]\), its homogeneous exact sequence is
\[
0\to
\operatorname{sgn}\otimes A_{C-1}\otimes
\operatorname{Sym}^{b-1}W
\xrightarrow{\ \ell\ }
A_C\otimes\operatorname{Sym}^{b}W
\to\mathcal H_{C,b}\to0.
\tag{A.15}
\]

For \(C\ge3\), both \(A_C,A_{C-1}\) are the four-point permutation module. At the point \(\ell_i\), the map in (A.15) is multiplication by \(\ell_i\cdot t\). The stabilizer \(S_3\) fixes the line \(\mathbf Q\ell_i\) in \(\mathfrak h_4\), so its corresponding line in \(W\) is sign. The quotient \(W/\operatorname{sgn}\) is \(\mathfrak h_3\otimes\operatorname{sgn}\). Thus evaluation identifies the cokernel in (A.15) with
\[
\operatorname{Ind}_{S_3}^{S_4}
\operatorname{Sym}^b(\mathfrak h_3\otimes\operatorname{sgn}).
\]
The explicit rational area-form intertwiner \(J\) of (P.8)–(P.9) identifies \(\mathfrak h_3\otimes\operatorname{sgn}\) with \(\mathfrak h_3\); taking its symmetric power gives precisely \(D_b\).

For \(C=2\), the source of (A.15) has \(A_1=\mathfrak h_4\), a codimension-one submodule of \(\operatorname{Perm}_4\). Extend the source to the entire permutation module. That larger multiplication map is injective point by point and has cokernel \(D_b\), just as above. Its image modulo the smaller image is \(\operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W\). Hence
\[
0\to\operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W
\to\mathcal H_{2,b}\to D_b\to0.
\]
Averaging a projection splits this exact sequence, giving the \(C=2\) row of (A.5).

For \(C=0\) there is no incidence relation, giving \(\operatorname{Sym}^bW\). For \(C=1\), the quadrics have no component and \(\mathcal H_{1,b}=R_{1,b}\). The exact incidence/Schur identification gives
\[
R_{1,b}=S_{(b+1,b)}\mathfrak h_4
=\operatorname{sgn}\otimes S_{(b+1,b)}W.
\]
The Elliott formula (H.2) with Dynkin labels \((1,b)\) is
\[
S_{(b+1,b)}W=\bigoplus_{L=1}^{b+1}H_L,
\]
including \(b=0\). This completes the proof of every row of (A.5).

## 3. Exact saturation in the oriented range

Retwisting the \(q\)-action in (V.4) back to the original action (A.1) gives
\[
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq\operatorname{sgn}^{d}\otimes
H^0(\mathcal F,\pi^*\mathcal I_Z^k\otimes\mathcal O_{\mathcal F}(c,b)).
\tag{A.16}
\]
The extra sign \(\operatorname{sgn}^{c}\) of (V.4) is precisely removed by that retwist; no determinant or parity factor is omitted.

For \(c\ge2k+1\), this section space is exactly \((J_R^k)_{c,b}\). Here is a direct proof that does not assume an equality of saturated and unsaturated ideals. Pull back the resolution (V.14) along the flat map \(\pi\), and tensor by \(\mathcal O_{\mathcal F}(c,b)\). Its two line-bundle terms have first degrees
\[
r=c-2k\ge1,\qquad r-2\ge-1.
\]
On the incidence flag,
\[
H^1(\mathcal F,\mathcal O_{\mathcal F}(a,b))=0
\quad\text{for }a\ge-1,\ b\ge0.
\tag{A.17}
\]
To check it, use the incidence hypersurface sequence on \(\mathbf P^2\times\mathbf P^2\). The first cohomology of the ambient line bundle is zero. The potentially contributing second cohomology of the preceding term is also zero: its first degree is \(a-1\ge-2\), its second degree is \(b-1\ge-1\), and neither factor has second cohomology in those ranges. The one-dimensional sign character of the incidence equation does not affect vanishing. These projective-space cohomology statements are exactly the Čech calculation cited and read in T-035.

It follows that the section space in (A.16) is the cokernel
\[
\operatorname{Sym}^{k-1}U\otimes\det U\otimes R_{r-2,b}
\longrightarrow
\operatorname{Sym}^{k}U\otimes R_{r,b}.
\tag{A.18}
\]
On the other hand the regular sequence \(U\) in \(R\), established by (A.3), has the power-ideal resolution obtained by extending the two-variable resolution in (V.14) to this free \(\operatorname{Sym}(U)\)-module. Its degree-\((c,b)\) cokernel is exactly \((J_R^k)_{c,b}\), with the same multiplication map as (A.18). This proves the claimed identification by the actual map, rather than a dimension comparison.

For \(c=2k\), T-036 gives exactly
\[
H^0(\mathcal F,\pi^*\mathcal I_Z^k\otimes\mathcal O_{\mathcal F}(2k,b))
\simeq
(J_R^k)_{2k,b}\oplus
\operatorname{sgn}\otimes\operatorname{Sym}^{k-1}U
\otimes\operatorname{Sym}^{b-1}W,
\]
since (A.4) makes the first summand \(\operatorname{Sym}^kU\otimes\operatorname{Sym}^bW\).
The case \(k=0,c=0\) has zero extra term. For \(k=0\) in all degrees, the ideal is the whole ring and the same conclusion follows directly. Combining these equalities with (A.4), (A.5), and (A.16) proves (A.9).

## 4. The three fixed tag tables

For \(\rho\in\{(4),(1^4),(2,2)\}\), let \(F_\rho\) be
\[
F_{(4)}=\{0\},\qquad F_{(1^4)}=\{3\},\qquad F_{(2,2)}=\{1,2\}.
\tag{A.19}
\]
Then
\[
[\rho:\operatorname{Sym}^jU]
=\sum_{f\in F_\rho}
\#\{(x_2,x_3)\ge0:2x_2+3x_3=j-f\},
\tag{A.20}
\]
where integer coordinates are understood.

Let \(E_\tau\) be the harmonic tags of (H.3), and let \(G_\tau\) be the following induction tags:
\[
\begin{array}{c|c|c}
\tau&E_\tau&G_\tau\\ \hline
(4)&\{0,9\}&\{0\}\\
(1^4)&\{3,6\}&\{3\}\\
(2,2)&\{2,4,5,7\}&\{1,2\}\\
(3,1)&\{2,3,4,5,6,7\}&\{0,1,2\}\\
(2,1,1)&\{1,3,4,5,6,8\}&\{1,2,3\}.
\end{array}
\tag{A.21}
\]
Their exact meanings are
\[
\begin{aligned}
[\tau:\operatorname{Sym}^bW]
&=\sum_{e\in E_\tau}
\#\{(y_2,y_4,y_6)\ge0:2y_2+4y_4+6y_6=b-e\},\\
[\tau:\bigoplus_{L=1}^{b+1}H_L]
&=\sum_{e\in E_\tau}
\#\{(y_4,y_6)\ge0:1\le4y_4+6y_6+e\le b+1\},\\
[\tau:D_b]
&=\sum_{g\in G_\tau}
\#\{(y_2,y_3)\ge0:2y_2+3y_3=b-g\}.
\end{aligned}
\tag{A.22}
\]
The first two equations follow from (H.4), (H.8). For the third, the exact induction branchings are
\[
\begin{aligned}
\operatorname{Ind}_{S_3}^{S_4}[(3)]&=[(4)]\oplus[(3,1)],\\
\operatorname{Ind}_{S_3}^{S_4}[(2,1)]&=[(3,1)]\oplus[(2,2)]\oplus[(2,1,1)],\\
\operatorname{Ind}_{S_3}^{S_4}[(1^3)]&=[(2,1,1)]\oplus[(1^4)].
\end{aligned}
\tag{A.23}
\]
The first is the four-coset permutation representation, the third is its sign twist, and the second follows by subtracting these two from induction of the regular representation of \(S_3\), or by the character rows (H.11). Combining these branchings with the three \(S_3\) tag series (P.10) gives the displayed \(G_\tau\).

Write \(K_{\rho\tau}^{\nu}\in\{0,1\}\) for the following fixed tensor table: \((4)\) is the identity, \((1^4)\) conjugates a partition, and
\[
\begin{array}{c|c}
\tau&\{\nu:K_{(2,2),\tau}^{\nu}=1\}\\ \hline
(4),(1^4)&\{(2,2)\}\\
(2,2)&\{(4),(1^4),(2,2)\}\\
(3,1),(2,1,1)&\{(3,1),(2,1,1)\}.
\end{array}
\tag{A.24}
\]
This is the exact character multiplication (V.24). Every other entry is zero.

## 5. The complete positive polytope evaluator

The following definitions are finite sums over the fixed tables (A.19), (A.21), (A.24). They contain no representation-theoretic multiplicities as unknown inputs.

For a label \(\nu\), integers \(L,U_0,b\), define \(\mathsf D_\nu(L,U_0;b)\) by summing, for every \(K_{\rho\tau}^{\nu}=1\), \(f\in F_\rho\), \(g\in G_\tau\), the lattice count in
\[
\left\{(x_2,x_3,y_2,y_3)\in\mathbf R_{\ge0}^4:
\quad L\le f+2x_2+3x_3\le U_0,\quad
2y_2+3y_3=b-g\right\}.
\tag{A.25}
\]
This count is zero when \(U_0<L\) or \(b<0\).

Define \(\mathsf W_\nu(j,b)\) by summing, for every \(K_{\rho\tau}^{\nu}=1\), \(f\in F_\rho\), \(e\in E_\tau\), the lattice count in
\[
\left\{(x_2,x_3,y_2,y_4,y_6)\in\mathbf R_{\ge0}^5:
\quad 2x_2+3x_3=j-f,\quad
2y_2+4y_4+6y_6=b-e\right\}.
\tag{A.26}
\]
Define \(\mathsf L_\nu(j,b)\) using the same tags but the four-variable polytope
\[
\left\{(x_2,x_3,y_4,y_6)\in\mathbf R_{\ge0}^4:
\quad 2x_2+3x_3=j-f,\quad
1\le4y_4+6y_6+e\le b+1\right\}.
\tag{A.27}
\]
The last two functions are zero for \(j<0\) or \(b<0\).

After the exact orientation (A.6), use \(b,c,d,k\) in (A.7) and set \(\nu=\mu^{[d]}\). The full coefficient is
\[
\boxed{
\begin{aligned}
p_{\mu,(n)}^\lambda
={}&\mathsf D_\nu\!\left(k,\left\lfloor\frac{c-3}{2}\right\rfloor;b\right)\\
&+\begin{cases}
\displaystyle
\mathsf L_{\nu'}\!\left(\frac{c-1}{2},b\right),
&c\text{ odd},\\[2mm]
\displaystyle
\mathsf W_\nu\!\left(\frac c2,b\right)
+\mathbf1_{c\ge2k+2}
\left[
\mathsf D_\nu\!\left(\frac{c-2}{2},\frac{c-2}{2};b\right)
+\mathsf W_{\nu'}\!\left(\frac{c-2}{2},b-1\right)
\right]\\
\displaystyle\hspace{13mm}
+\mathbf1_{c=2k}\mathsf W_{\nu'}(k-1,b-1),
&c\text{ even}.
\end{cases}
\end{aligned}}
\tag{A.28}
\]
Here the symbols on the left refer to the oriented input; (A.6) proves equality with the original requested coefficient.

To verify (A.28), partition the positive sum (A.9) according to \(C=c-2j\). All \(C\ge3\) terms are (A.25), where the value \(j=f+2x_2+3x_3\) is uniquely recovered from the lattice point. For odd \(c\), the remaining term has \(C=1\), yielding (A.27) with the sign twist \(\nu'\). For even \(c\), the \(C=0\) term gives (A.26); the \(C=2\) term exists exactly when \(c\ge2k+2\), and its two summands give (A.25) and the sign-shifted (A.26). Finally the boundary correction is present exactly when \(c=2k\), as displayed. Thus every summand in the module decomposition has one and only one tagged polytope, and every lattice point counts one coefficient of its two explicit symmetric-power series.

All polytopes are bounded: the \(x\)-coordinates have an upper bound from \(U_0\) or \(j\); the \(y\)-coordinates have an upper bound from \(b\). Their matrices use only the fixed integers \(1,2,3,4,6\), and their constants have bit length \(O(\log(n+2))\).

For a fixed label \(\nu\), (A.25) has at most 18 tags; (A.26), (A.27) have at most 36. When \(c\) is odd, at most \(18+36=54\) polytopes occur. When \(c\ge2k+2\) is even, the bound is \(18+36+18+36=108\). At \(c=2k\), only the two (A.26) terms survive, giving at most 72. For \(\nu=(4)\) or \((1^4)\), the corresponding tag maxima are 6 and 12, yielding the bound 36; for \(\nu=(2,2)\), they are 12 and 24, yielding 72. Sign and complement twists preserve these three categories.

## 6. Constant-size arithmetic and the standalone implementation

The fixed polytope counts can also be evaluated by a fixed number of integer operations. Define
\[
C(N)=\#\{(x,y)\ge0:2x+3y=N\},\qquad
P(N)=\#\{(x,y)\ge0:2x+3y\le N\},
\]
and set both to zero for \(N<0\). For \(N\ge0\),
\[
C(N)=1+\left\lfloor\frac N6\right\rfloor
-\mathbf1_{N\equiv1\pmod6}.
\tag{A.29}
\]
For \(e=0,1\), put \(T_e=\lfloor(N-3e)/6\rfloor\). Splitting \(y=2t+e\) gives
\[
P(N)=\sum_{e=0}^1
\left[
(T_e+1)\left(\left\lfloor\frac{N-3e}{2}\right\rfloor+1\right)
-\frac{3T_e(T_e+1)}2
\right].
\tag{A.30}
\]
When \(N=0,1,2\), the \(e=1\) value has \(T_e=-1\), so its summand is zero, as required. Formula (A.29) counts the allowable parity of \(y\). Formula (A.30) sums the arithmetic progression of allowable \(x\) values; these are explicit counting proofs.

One tagged polytope in (A.25) therefore has count
\[
[P(U_0-f)-P(L-f-1)]\,C(b-g).
\]
One in (A.26) has count
\[
C(j-f)\,
\begin{cases}
P((b-e)/2),&b-e\ge0\text{ and even},\\
0,&\text{otherwise}.
\end{cases}
\]
One in (A.27) has count
\[
C(j-f)\left[
P\!\left(\left\lfloor\frac{b+1-e}{2}\right\rfloor\right)
-P\!\left(\left\lfloor\frac{-e}{2}\right\rfloor\right)
\right].
\tag{A.31}
\]
The first subtraction counts an interval of lattice points, and the last excludes angular momentum zero; both quantities are nonnegative by their defining sets.

The standalone file [outer4_positive.py](outer4_positive.py) implements (A.19)–(A.31) using only Python's standard library and the fixed integer tag tables. It can also export every tagged polytope as exact equality and inequality matrices, and enumerate its integer witnesses. Its counting routine has no loop whose length grows with \(n\), and uses a fixed number of integer operations. All values have \(O(\log(n+2))\) bits: each template count is bounded by a constant times \((n+1)^3\). Consequently ordinary schoolbook integer arithmetic gives an \(O((\log(n+2))^2)\) bit bound for the arithmetic part, after reading the input. Output partitions of arbitrary length are first checked by the stated zero-support rule.

The direct implementation was compared with all 1,980 independent cycle-index cases and passed. Its witness enumerator separately checked 64,260 exact tagged polytope descriptions, with 2,588 lattice witnesses across the tested coefficients; every point satisfied the exported matrices and every template count equaled its explicit enumeration. The receipt is [OUTER4_DIRECT_POLYTOPE_CHECK.tsv](OUTER4_DIRECT_POLYTOPE_CHECK.tsv), with summary [OUTER4_DIRECT_POLYTOPE_CHECK.txt](OUTER4_DIRECT_POLYTOPE_CHECK.txt) and reproduction code [check_outer4_positive.py](check_outer4_positive.py). The exported [EXAMPLE_642_POLYTOPES.json](EXAMPLE_642_POLYTOPES.json) gives the complete positive count for \(p_{(4),(3)}^{(6,4,2)}=1\).


## Verification and scope

The independent calculation in work/rectangular/verify_outer4_all_formula.py compared (A.9), using literal class traces and fixed-point induction, against power-sum plethysm with the Murnaghan–Nakayama rule. Every one of the 1,980 cases passed: all \(\mu\vdash4\), all \(\lambda\vdash4n\) of length at most four, and \(0\le n\le6\). This includes 750 strict central-chamber cases. The receipt is work/rectangular/OUTER4_ALL_FORMULA_INDEPENDENT_CHECK.tsv. A separate direct evaluator of the tagged polytope formula (A.28) accompanies this report.

The result supplies a direct fixed-template positive formula for every outer Schur label of size four. The proof uses the specified flag chart, the four-point complete intersection, actual equivariant multiplication, and the exact boundary cohomology map. The general terminating construction G-009–G-011 remains valid in every rank; the efficient direct-formula frontier after this result starts beyond outer degree four. No assertion of historical novelty is made for the coefficient family or for its classical ingredients.


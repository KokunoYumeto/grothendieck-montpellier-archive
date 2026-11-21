# Rectangular cases and the normalized Hadamard--Howe period

Run: `/root/rectangular_cases`, 21 November 2026 (Europe/Berlin).
Model: GPT-6 Astra Pro. The inherited effort setting is not exposed to this agent.

This report supplies exact reformulations, proofs, source locators, and finite certificates for the parent paper. The literature results remain attributed to their authors. The labels R-001--R-006 identify findings and explicit dictionaries established in this run; they do not claim priority over the cited classical results.

## Notation

Write

\[
a_\lambda(d[n])=[S_\lambda V:\operatorname{Sym}^d(\operatorname{Sym}^nV)],
\qquad R_{r,s}=(s^r),
\]

with \(\dim V\ge\ell(\lambda)\). Thus \(r\times s\) in the supplied Ikenmeyer--Panova source means \(R_{r,s}\). All decompositions of complex representations below use characteristic zero. The base ring used for normalized integral tensors will be specified separately.

The Hadamard--Howe map is normalized by averaging permutations, so that

\[
h_{d,n}(v_1^n\cdots v_d^n)=(v_1\cdots v_d)^n.
\]

This is the convention of Kumar--Landsberg, §1.2, arXiv:1410.8585v1.

## R-001. A rectangular plethysm coefficient as a one-point lattice count

For every \(r\ge2\), \(n\ge1\),

\[
a_{(n^r)}(r[n])
=\#\{z\in\mathbb Z:2z=n\}
=\begin{cases}1&n\text{ even},\\0&n\text{ odd}.\end{cases}
\tag{R-001}
\]

The first equality presents a positive lattice-point formula on the rational zero-dimensional polytope \(\{n/2\}\). The multiplicity-one statement is classical: Howe, *\((\mathrm{GL}_n,\mathrm{GL}_m)\)-duality and symmetric plethysm*, Proposition 4.3, as located explicitly in Kumar--Landsberg §2; also supplied BIP §2(b).

### Proof of the precise lattice-count form

Take \(V=\mathbb C^r\). A tensor in \((\operatorname{Sym}^nV)^{\otimes r}\) is a polynomial on \(r\) covectors, separately of degree \(n\) in each covector. Arrange the covectors as columns of an \(r\times r\) matrix \(X\). On the dense open subset \(\det X\ne0\), an \(\mathrm{SL}_r\)-invariant polynomial depends only on \(\det X\): two invertible matrices with the same determinant differ by left multiplication by an element of \(\mathrm{SL}_r\). Separate homogeneity forces the invariant to be a scalar multiple of \((\det X)^n\). Equality on the dense open subset is equality of polynomials. Thus the invariant space in the ordered tensor product is one-dimensional.

Permutation of the \(r\) covectors acts on this line by \(\operatorname{sgn}^n\). Passing to the outer symmetric power is taking the invariants of this \(S_r\)-action. Since \(r\ge2\), the invariant dimension is one for even \(n\) and zero for odd \(n\). The \(\mathrm{SL}_r\)-invariant summand of homogeneous degree \(rn\) has \(\mathrm{GL}_r\)-highest weight \((n^r)\). Finally, the equation \(2z=n\) has exactly one integral solution for even \(n\) and none for odd \(n\). This proves all displayed equalities.

The same coefficient holds in every \(\dim V\ge r\): Schur-functor multiplicities are stable once the indexed partition fits, by the symmetric-group multiplicity-space realization.

## R-002. The exact square Hadamard--Howe scalar

Fix an even integer \(n\ge2\), let \(V=\mathbb C^n\), and put \(H=S_n\wr S_n\). Index the tensor factors of \(V^{\otimes n^2}\) by the cells \((i,j)\) of an \(n\times n\) array. Let \(e_H\) be the average over permutations within rows and permutations of rows. Let \(\tau\) transpose the array. Then

\[
\operatorname{Sym}^n(\operatorname{Sym}^nV)=e_HV^{\otimes n^2},
\qquad h_{n,n}=e_H\tau e_H.
\]

Define

\[
\delta=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
e_{\sigma(1)}\otimes\cdots\otimes e_{\sigma(n)},
\]

put one copy of \(\delta\) in each column, call the resulting tensor \(D\), and put \(I=e_HD\). This \(I\) spans the determinant line from R-001. For a Latin square \(L\), let \(c(L)\) denote the product of its column signs, and let \(E_n-O_n\) be its signed enumeration using the product of all row and column signs. Set

\[
\Delta_n=\sum_{L\text{ Latin}}c(L),\qquad
B_n=\prod_{j=0}^{n-1}\frac{(n+j)!}{j!}.
\]

The normalized scalar is

\[
\boxed{
h_{n,n}(I)=c_n I,\qquad
c_n=\frac{\Delta_n}{(n!)^n}
=\frac{(-1)^{n(n-1)/2}(E_n-O_n)}{(n!)^n}
=\frac{B_n}{(n!)^n}\int_{\mathrm{SU}(n)}\prod_{i,j=1}^n u_{ij}\,du.
}
\tag{R-002}
\]

Here Haar measure has total mass one. Kumar--Landsberg Theorem 1.9 proves the associated nonvanishing equivalences; Proposition 2.1 gives the determinant contraction. The present calculation fixes every scalar under the displayed averaging convention. Alpöge, *Square-root cancellation for the signs of Latin squares*, Corollary 5, supplies the last coefficient-to-Haar identity. That paper is separate bibliographic material from the supplied `ALPOGE_remark.pdf`.

### Proof of the scalar

Equip the standard tensor basis with its orthonormal inner product. Let \(t_0\) have entry \(e_i\) in every cell of row \(i\). Although \(t_0\) is invariant under the within-row permutations, it need not be invariant under permutations of rows. The needed pairing still has the value one: every row permutation of \(t_0\) has coefficient \(\operatorname{sgn}(\pi)^n=1\) in \(D\), so

\[
\langle I,t_0\rangle=\langle D,e_Ht_0\rangle=1.
\tag{R-002a}
\]

Because \(I\) spans the determinant line, write \(h_{n,n}I=c_nI\). Self-adjointness of the averages and the transpose permutation gives

\[
c_n=\langle e_H\tau I,t_0\rangle
=\langle I,\tau e_Ht_0\rangle.
\]

The tensor \(e_Ht_0\) is the average of \(t_0\) over permutations of rows. After applying \(\tau\), those permutations become simultaneous within-row permutations of \(t_1:=\tau t_0\). Since \(I\) is invariant under the within-row permutations,

\[
c_n=\langle I,t_1\rangle=\langle D,e_Ht_1\rangle.
\]

Every row of \(t_1\) is \((e_1,\ldots,e_n)\). Thus \(e_Ht_1\) averages independently over the \(n!\) reorderings in each of its \(n\) rows. A tensor in this average pairs nontrivially with \(D\) exactly when its columns also contain each basis vector once, which is exactly the Latin-square condition. Its coefficient in \(D\) is the product of column signs. Therefore the pairing is \(\Delta_n/(n!)^n\).

### Proof of the parity conversion

This conversion is an identity of total signed sums, not an equality of the two sign functions on each square. Let \(r(L),c(L),s(L)\) be respectively the products of row, column, and symbol-position signs. On the \(n^2\) ordered pairs, define

\[
R:(i,j)\mapsto(i,L_{ij}),\quad
S:(i,s)\mapsto(j,s)\text{ where }L_{ij}=s,
\quad T:(j,s)\mapsto(s,j).
\]

The column permutation \(C:(i,j)\mapsto(L_{ij},j)\) satisfies \(C=TSR\). The transpose permutation \(T\) has sign \(\epsilon=(-1)^{n(n-1)/2}\), hence \(r(L)c(L)s(L)=\epsilon\). Form the conjugate Latin square \(L'\), with row \(i\), column \(s\), and entry \(j\) specified by \(L_{ij}=s\). Its row-sign product is \(r(L)\), and its column-sign product is \(s(L)\). Its ordinary sign is therefore \(\epsilon c(L)\). The correspondence \(L\mapsto L'\) is a bijection. Summing proves \(\Delta_n=\epsilon(E_n-O_n)\).

### Proof of the Haar normalization

The coefficient \(C_n\) of \(\prod_{i,j}X_{ij}\) in \(\det(X)^n\) is the sum of the products of the signs of the symbol-position permutations in Latin squares. Parastrophy exchanges this with the column-sign sum, so \(C_n=\Delta_n\). Apply Alpöge Corollary 5 to the all-ones multiindex \(\alpha\), with \(k=n\). Its factorial \(\alpha!\) is one, and the displayed factor in that corollary is \(B_n\). Consequently \(\Delta_n=B_n\int\prod u_{ij}\,du\), giving the last equality.

### Exact finite values and a checked bound

The enumeration script `verify_rectangular.py` visits every reduced Latin square for \(n=2,4,6\), with first row and first column fixed. It found:

| \(n\) | Reduced squares | Reduced column-sign sum | All squares | \(\Delta_n\) | \(c_n\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | -1 | 2 | -2 | \(-1/2\) |
| 4 | 4 | 4 | 576 | 576 | \(1/576\) |
| 6 | 9408 | -2304 | 812851200 | -199065600 | \(-1/699840000\) |

Every reduced square has \(n!(n-1)!\) completions under row and symbol normalization, and the column sign is unchanged for even \(n\). The recursion enumerates all row permutations with their first entry prescribed, rejects exactly repeated column symbols, and at depth \(n\) evaluates the product of column permutation signs. Thus this is a finite exhaustive certificate, not sampling. The certificate asserts only these three orders.

Alpöge Theorem 2, evaluated at \(k=n\), gives the exact inequality

\[
0\le |c_n|^2\le\frac{B_n}{(n!)^{2n}}.
\tag{R-002b}
\]

The value zero belongs to this interval. The unresolved scalar in the square rectangular component is precisely \(\Delta_n\), or equivalently the displayed Haar integral. No lower bound for general even \(n\) is established in this report.

## R-003. A concrete failure of positivity transfer from rectangular Kronecker coefficients

For every \(d,n\ge1\) and \(1\le k\le dn-1\),

\[
a_{(dn-k,1^k)}(d[n])=0.
\tag{R-003a}
\]

This vanishing is known: Eugenio Giannelli, *Representations of symmetric groups*, PhD thesis (2015), Theorem 2.1.2, p.38, with proof in §2.3, pp.42--43; Giannelli attributes the earlier Schur-function proof to Langley--Remmel. The short argument below records the exact wreath-product/exterior-power dictionary used in the counterexample. The hook/exterior-power identification is Giannelli Lemma 2.3.3 (also Fulton--Harris, Proposition 3.12 for irreducibility).

In particular,

\[
\boxed{a_{(13,1,1,1)}(4[4])=0,\qquad
g((13,1,1,1),(4^4),(4^4))=1.}
\tag{R-003b}
\]

The parameters in R-003b lie in the stable range of Ikenmeyer--Panova Proposition 2.8: the tail \(\rho=(1,1,1)\) has size three and the inner degree is four. Thus the actual inequality at this point is \(1\ge0\).

### Proof

The finite-group multiplicity formula is

\[
a_\lambda(d[n])=\dim[\lambda]^{S_n\wr S_d}.
\]

For \(N=dn\), the hook Specht module \([N-k,1^k]\) is \(\bigwedge^kU_N\), where \(U_N\) is the standard, sum-zero representation of \(S_N\). Restrict to the base group \(K=S_n^d\). There is an explicit decomposition

\[
U_N=A\oplus U_n^{(1)}\oplus\cdots\oplus U_n^{(d)},
\]

where \(A\) consists of vectors constant within each block and with total sum zero. The base group fixes \(A\) pointwise, and its quotient \(S_d\) acts on \(A\) as \(U_d\). For every \(j=1,\ldots,n-1\), \(\bigwedge^jU_n\) is the nontrivial irreducible hook \([n-j,1^j]\), so it has no \(S_n\)-invariants. The exterior-power decomposition of a direct sum therefore gives

\[
(\bigwedge^kU_N)^K=\bigwedge^kA.
\]

Taking the remaining \(S_d\)-invariants yields zero for every \(k>0\): the exterior powers in their nonzero range are the nontrivial hooks \([d-k,1^k]\), and the remaining exterior powers vanish. The cases \(n=1\) or \(d=1\) are immediate from the same decomposition with zero-dimensional summands. This proves R-003a.

Ikenmeyer--Panova Proposition 6.4 gives

\[
\sum_k g((16-k,1^k),(4^4),(4^4))q^k
=(1+q^3)(1+q^5)(1+q^7).
\]

The coefficient of \(q^3\) is one, proving R-003b. Independently, `verify_rectangular.py` computed the plethysm by the power-sum cycle index \(h_4[h_4]\), paired with the hook character, and the Kronecker coefficient by the Murnaghan--Nakayama character rule followed by the exact conjugacy-class sum. Both computations use rational arithmetic and give the displayed values.

## R-004. The rectangular-hook polytope

For \(1\le r\le s\), \(0\le k\le rs-1\), let

\[
P_{r,k}=\{(x_2,\ldots,x_r)\in[0,1]^{r-1}:
\sum_{i=2}^r(2i-1)x_i=k\}.
\]

Ikenmeyer--Panova Proposition 6.4 gives exactly

\[
g((rs-k,1^k),(s^r),(s^r))=\#(P_{r,k}\cap\mathbb Z^{r-1}).
\tag{R-004}
\]

The proof of this reformulation is the bijection sending a partition into distinct allowed parts \(3,5,\ldots,2r-1\) to its indicator vector. It preserves the sum. R-003 explicitly computes the plethysm coefficient for one of the positive points of this polytope.

## R-005. An explicit vector and multiplicity one for row-extended even rectangles

Take \(k\ge2\), an even integer \(\ell\ge2\), and \(n\ge\ell\). Put

\[
\lambda=(kn-(k-1)\ell,\ell^{k-1}).
\]

Then

\[
a_\lambda(k[n])=1.
\tag{R-005a}
\]

For \(n\ge k\ell\), the same multiplicity in \(\mathbb C[\overline{\mathrm{GL}_{n^2}\det_n}]_k\) is exactly one. This combines the explicit vector below with BIP Propositions 2.3 and 5.6(1), and Theorem 2.5. The equality of multiplicities refines the occurrence statement to the one-dimensional ambient component.

### Proof and normalized nonzero evaluation

Use \(k\) basis vectors and form \(I_{k,\ell}\) by placing the alternating \(k\)-tensor in each of \(\ell\) columns and averaging the within-row and outer permutations. It is a highest weight vector of weight \((\ell^k)\). For nonzero coefficients \(c_1,\ldots,c_k\), direct contraction gives

\[
\big\langle I_{k,\ell},(\sum_{i=1}^k c_iX_i^\ell)^{\otimes k}\big\rangle
=k!\prod_{i=1}^k c_i.
\tag{R-005b}
\]

Indeed, a nonzero determinant contraction assigns distinct basis labels to the \(k\) rows. There are \(k!\) assignments, their signs are raised to the even power \(\ell\), and every assignment has coefficient \(\prod_i c_i\).

Let \(M:\operatorname{Sym}^\ell V\to\operatorname{Sym}^nV\) multiply by \(e_1^{n-\ell}\), and put \(\kappa=\operatorname{Sym}^kM\). The upper triangular unipotent group fixes \(e_1\), so \(\kappa(I_{k,\ell})\) remains a highest weight vector and its weight is \(\lambda\). The map \(M\), and therefore \(\kappa\), is injective. BIP Proposition 5.6(1) says that \(\kappa\) is an isomorphism on these highest weight spaces, since the second part of \((\ell^k)\) equals the initial inner degree \(\ell\). R-001 now gives R-005a.

With normalized symmetric-tensor pairings, the dual map is

\[
M^*=\frac{\ell!}{n!}\partial_{X_1}^{n-\ell}.
\]

For

\[
q=X_1^{n-\ell}\sum_{i=1}^k c_iX_i^\ell
\]

one obtains

\[
M^*q=c_1X_1^\ell+\binom n\ell^{-1}\sum_{i=2}^k c_iX_i^\ell,
\]

and hence

\[
\boxed{\langle\kappa(I_{k,\ell}),q^{\otimes k}\rangle
=k!\binom n\ell^{-(k-1)}\prod_{i=1}^k c_i\ne0.}
\tag{R-005c}
\]

The pairing identity follows directly from the definition of a dual map, also BIP Theorem 5.4. For \(n\ge k\ell\), BIP Theorem 2.5 places every such padded power sum in the determinant orbit closure. Thus the coordinate-ring quotient is nonzero on this one-dimensional highest weight space. Its multiplicity is both at least one and at most the ambient multiplicity one, proving the claimed equality.

## R-006. Scheme, locally free sheaf, and Grothendieck-group dictionary

The following constructions specify the morphisms transporting R-001--R-005.

1. **Group schemes and Schur operations.** The representations are obtained from the standard locally free sheaf of \(\mathrm{GL}_{r,\mathbb Z}\) by tensor, exterior, and symmetric powers. Over \(\mathbb Q\), their identities are identities in \(K_0(\operatorname{Rep}_{\mathbb Q}\mathrm{GL}_r)\). A principal \(\mathrm{GL}_r\)-bundle on a \(\mathbb Q\)-scheme gives an associated locally free sheaf \(E\). Applying the associated-bundle functor transports each actual natural tensor morphism and each equality in this Grothendieck group to the corresponding sheaf morphism and class in \(K_0(X)\). In particular, the plethystic operation is \([E]\mapsto[\operatorname{Sym}^d(\operatorname{Sym}^nE)]\).

2. **The determinant line and the normalized map.** For R-002, take \(R=\mathbb Z[1/n!]\). The group order \(|H|=(n!)^{n+1}\) is invertible, so all displayed averages are defined over \(R\). Frame change multiplies \(I\) by \(\det(g)^n\). The resulting locally free line is \((\det E)^{\otimes n}\), and the restriction of the natural tensor map to it is multiplication by the exact scalar \(\Delta_n/(n!)^n\). The scalar and the line therefore descend from frames over \(R\) to every locally free \(E\) of rank \(n\). Over the complex fiber, the coordinate multiplicity in the image of this map is the rank of this scalar map.

3. **The Chow scheme and its coordinate map.** The morphism

   \[
   \mu:(E^*)^{\times n}\longrightarrow\operatorname{Sym}^n E^*,
   \qquad(\ell_1,\ldots,\ell_n)\longmapsto\ell_1\cdots\ell_n
   \]

   is defined over \(\mathbb Z\). Its pullback on degree-\(d\) coordinate functions lands in separately degree-\(d\) functions, invariant under \(S_n\), and over \(\mathbb Q\) identifies with \(h_{d,n}\). The affine scheme-theoretic image has coordinate algebra \(\operatorname{im}\mu^*\); this realizes the Chow cone and gives \(\ker h_{d,n}=I(\mathrm{Chow}_n)_d\). Thus R-002 is an exact equation for the rank of the rectangular component of a morphism of coordinate algebras. For \(n=2,4,6\), the finite certificates prove rank one in that component. This coordinate-map assertion is also Kumar--Landsberg Lemma 1.5.

4. **The exact \(K_0\) relation.** For a line \(L\) over a field and an endomorphism \(f:L\to L\), its kernel-image-cokernel exact sequence gives \([\ker f]=[\operatorname{coker}f]\). For the map \(f=0\), both classes equal \([L]\); for \(f=1\), both classes are zero. Both endomorphisms have domain and codomain \(L\). This computes exactly the information supplied by the class identity \([L]-[L]=0\). R-002 records the additional morphism \(c_n\operatorname{id}_L\). The associated \(\lambda\)-operation has \(\lambda_t([L])=1+[L]t\), while \(\gamma_t([L]-1)=1+([L]-1)t\); neither formula changes with the chosen endomorphism of the line, as is verified by the two explicit maps.

5. **Finite étale schemes and weights.** Let \(\mathcal L_n^+\) and \(\mathcal L_n^-\) be the constant finite schemes over \(\mathbb Z\) indexed by column-even and column-odd Latin squares. Their virtual class is \([\mathcal L_n^+]-[\mathcal L_n^-]=\Delta_n[\operatorname{Spec}\mathbb Z]\). Over every finite field, each geometric point contributes one eigenvalue one to \(H_c^0\), and higher cohomology vanishes. Thus the difference of Frobenius traces is exactly \(\Delta_n\). This gives a direct finite-scheme and weight-zero dictionary for the same signed period numerator. For odd \(n>1\), swapping two rows reverses the column sign and gives an involution pairing all squares, so this virtual class and trace are zero. For even \(n=2,4,6\), their values are the three nonzero integers in the certificate. These are exact computations of the maps and classes involved, with no assertion excluding other geometric relations.

The parent paper is to supply the exact SGA/EGA/FGA locators for these standard constructions from its independent archive/SGA audit. This report does not invent unverified exposé or proposition numbers.

## Exact inventory of supplied literature relevant to item 4

All statements in this inventory are attributed results, not new findings. Parameter domains are written explicitly.

### Ikenmeyer--Panova (IP), arXiv:1512.03798v2

Let \(\rho(N)=(N-|\rho|,\rho)\), whenever it is a partition, and \(\bar\lambda\) be the tail after removing the first row. Let

\[
\mathcal X=\{(1),(1,1),(1,1,1,1),(1^6),(2,1),(3,1)\}.
\]

| Locator | Exact content used |
|---|---|
| Theorem 1.6, p.3 | For \(n>3m^4\), support of the padded-permanent coordinate ring in degree \(d\) is contained in \(\{\lambda:g(\lambda,(d^n),(d^n))>0\}\). |
| Theorem 1.8, pp.3--4 (Kadish--Landsberg) | That support has \(\ell(\lambda)\le m^2\), \(|\bar\lambda|\le md\). |
| Corollary 1.9, p.4 | On \(|\bar\lambda|\le md\), a strict inequality \(a_\lambda(d[n])>g(\lambda,(d^n),(d^n))\) requires \(d>n/m\). |
| Theorem 1.10(a), p.4 | Every \(\lambda\) with \(\bar\lambda\in\mathcal X\) has \(a_\lambda(d[n])=0\). |
| Theorem 1.10(b), p.4 | For \(m\ge3\), \(\bar\lambda\notin\mathcal X\), \(\ell(\lambda)\le m^2\), \(|\bar\lambda|\le md\), \(d>3m^3\), \(n>3m^4\), the rectangular Kronecker coefficient is positive. |
| Theorem 2.1, p.5 (Manivel, Theorem 1) | For \(n\ge|\rho|\), \(g(\rho(nd),(d^n),(d^n))=\dim S_\rho(\mathfrak{sl}_d)^{\mathrm{SL}_d}\). The function is symmetric and nondecreasing in \(n,d\). |
| Proposition 2.8, p.7 | For \((n,d)\in\mathrm{St}^1(\rho)\), in particular \(n\ge|\rho|\), \(g(\rho(nd),(d^n),(d^n))\ge a_{\rho(nd)}(d[n])\). |
| Theorem 4.7, p.11 | For \(\nu\notin\mathcal X\), \(L=\max(\ell(\nu)+1,9)\), \(a>3L^{3/2}\), \(b\ge3L^2\), and \(|\nu|\le ab/6\), \(g(\nu(ab),(b^a),(b^a))>0\). |
| Corollary 5.1, p.13 | The stable limit \(A_\rho\) vanishes exactly for \(\rho\in\mathcal X\). Here \(A_\rho\) is a stable rectangular Kronecker coefficient, with its invariant-Schur-functor realization in Theorem 2.1. |
| Proposition 5.2, p.13 | For \(i\ge2\), \(m\ge7\), \(0\le k<m^2\), \(g(i(m^2-k,1^k),((im)^m),((im)^m))>0\). |
| Corollary 5.3, p.14 | For \(m\ge7\), every even-row partition \(\rho\) of length less than \(m^2\) has \(\dim S_\rho(\mathfrak{sl}_m)^{\mathrm{SL}_m}>0\). |
| Corollary 5.4, p.14 | For \(d\ge7\), the group generated by the rectangular Kronecker support semigroup in \(\mathbb Z^{d^2}\) is \(\{z:\sum z_i\equiv0\pmod d\}\). |
| Proposition 6.4, p.15 | The hook coefficients have the subset-count formula used in R-004. |

### Bürgisser--Ikenmeyer--Panova (BIP), arXiv:1604.06431v3

| Locator | Exact content used |
|---|---|
| Theorem 1.4, p.3 | For \(n\ge m^{25}\), support of the padded-permanent coordinate ring is contained in support of the determinant-orbit-closure coordinate ring. |
| Proposition 2.3, p.5 | \(n\ge k\ell\), \(\ell\) even: \((k\times\ell)^{\sharp nk}\) occurs in determinant-orbit-closure degree \(k\). |
| Proposition 2.4, p.5 | \(|\bar\lambda|\le md\), \(md^2\le n\): restriction to the determinant closure is injective on the \(\lambda\)-highest-weight space. The natural reading of “every highest weight vector” is every nonzero such vector. |
| Theorem 2.5, p.5 | \(n\ge sk\): every \(X^{n-s}\sum_{i=1}^k\varphi_i^s\) belongs to the determinant orbit closure. |
| Corollary 4.8, p.13 | Explicit determinant-contraction nonvanishing on power sums for even inner degree. |
| Theorem 5.4, p.15 | \(\langle\kappa^d_{m,n}(f),q^d\rangle=\langle f,(M^*q)^d\rangle\). |
| Proposition 5.6(1), p.17 | \(n\ge m\), \(\mu\vdash md\), \(\mu_2\le m\): \(\kappa\) induces an isomorphism of the highest-weight spaces of weights \(\mu\) and \(\mu+(d(n-m))\). |

The BIP support inclusion constrains occurrence obstructions. The morphism-level question is retained by the restriction map and by its ranks on multiplicity spaces. No conclusion on P versus NP is claimed here.

## Source-proof audit notes and boundaries of checking

1. IP Theorem 6.1's displayed exception `d^1-2` is a typographical error: Proposition 6.4 and the proof's table use \(d^2-2\). Its additionally stated strict inequality \(g_k>g_{k-2}\) for all \(k\le d^2/2\) also fails literally, for example \(d=7,k=2\) gives \(0>1\). We use the exact Proposition 6.4 instead. This discrepancy is proved by the generating function, rather than silently correcting the printed theorem.

2. In the supplied proof of IP Theorem 4.7, the line \(w<\sqrt{L+7}+1\le(L+1)/2\), with \(w=\max(\lceil\sqrt{L+7}\rceil,7)\), is false at \(L=9\): it asserts \(7<5\). This is a gap in that displayed estimate, not a counterexample to the theorem. The broad theorem is cited as literature, and is not certified here as an independently checked proof. No new proof in this report depends on that estimate. The parent can record this explicitly or omit reliance on Theorem 4.7.

3. The hook counterexample, parity conversion, averaging normalization, and row-extended evaluation were read and checked in full. A first informal scalar derivation had called \(t_0\) invariant under all of \(H\); that statement fails for row permutations. R-002's final proof explicitly averages \(t_0\), uses evenness to compute its pairing, and moves the row permutations through \(\tau\). This repairs the issue without changing the scalar.

4. Computational certificates are exact finite certificates for their stated inputs. They do not certify a universal nonvanishing theorem or the entire supplied literature.

## Primary-source URLs for root verification

- IP: https://arxiv.org/pdf/1512.03798 (v2).
- BIP: https://arxiv.org/pdf/1604.06431 (v3).
- Kumar--Landsberg: https://arxiv.org/pdf/1410.8585 (v1), Theorem 1.9, Proposition 2.1, Lemma 1.5; Howe Proposition 4.3 cited in §2.
- Alpöge: https://people.math.harvard.edu/~alpoge/papers/combinatorica%20paper.pdf, Theorem 2 and Corollary 5.
- Bürgisser--Christandl--Ikenmeyer, *Even partitions in plethysms*: https://www3.math.tu-berlin.de/algebra/work/weintraub.pdf, §1.1 unnumbered main theorem; arXiv:1003.4474v2. Its domain \(\lambda\vdash kn,\ell(\lambda)\le k\) yields \(a_{2\lambda}(k[2n])>0\).
- Giannelli, *Representations of symmetric groups*: https://eugeniomaths.wordpress.com/wp-content/uploads/2013/10/tesi-final-version-2015.pdf, Theorem 2.1.2 and Lemma 2.3.3.

Web references available in this child run: `turn614803048view0` (IP), `turn614803048view1` (BIP), `turn768780200view0` (Kumar--Landsberg), `turn245878279view0` (Alpöge), `turn517469220search12` (BCI). The root must open them independently before citing them in chat.

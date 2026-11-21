# Charged oscillators, the frame quotient, and an exact theta branching realization

## T-052. The complete charge and lowest-type dictionary

Work over \(\mathbf Q\) for the polynomial maps, and extend scalars
to \(\mathbf C\) for the unitary groups. Let \(m\ge3\),
\(n\ge0\), \(\mu\vdash m\), and \(\lambda\vdash mn\)
with at most \(m\) parts. Pad \(\lambda\) by zeros. Define
\[
\begin{gathered}
e=\max(0,n-\lambda_2),\qquad n_0=n-e,\qquad
\lambda^0=(\lambda_1-me,\lambda_2,\ldots,\lambda_m),\\
r=m-2,\quad F=\mathbf Q^r,\quad W=\mathbf Q^m,
\quad k=\lambda_2-n_0,\\
\alpha=(\lambda_2-\lambda_m,\lambda_2-\lambda_{m-1},
\ldots,\lambda_2-\lambda_3),\quad N=|\alpha|,\quad
b=N-mk=\lambda^0_1-\lambda_2.
\end{gathered}
\tag{OC.1}
\]
All these are nonnegative integers, \(\lambda^0\) is a partition,
and \(|\lambda^0|=mn_0\). Let
\[
\begin{aligned}
\mathcal P&=\mathbf Q[X_{ai},Y_i:1\le a\le r,1\le i\le m],\\
R_a&=\sum_iX_{ai}Y_i,\qquad C_a=\sum_i\partial_{X_{ai}}\partial_{Y_i},\\
Q_i&=\sum_aX_{ai}\partial_{X_{ai}}-Y_i\partial_{Y_i}.
\end{aligned}
\tag{OC.2}
\]
The superscript \([k]\) below imposes \(Q_i=k\) for every
\(i\). Subscripts \((N,b)\) impose the total \(X\)-degree
\(N\) and \(Y\)-degree \(b\). Put
\[
\mathcal H^{[k]}_{N,b}
=\mathcal P^{[k]}_{N,b}\cap\bigcap_{a=1}^r\ker C_a,
\qquad
K_{\alpha,k}=\operatorname{Hom}_{GL(F)}
(S_\alpha F,\mathcal H^{[k]}_{N,b}).
\tag{OC.3}
\]
Here \(GL(F)\) acts on the \(X\) variables without a vacuum
twist. Column permutations act simultaneously on \(X_{ai}\)
and \(Y_i\). There is an actual rational \(S_m\)-module
isomorphism
\[
\boxed{(S_\lambda W)_{(n^m)}
\simeq\operatorname{sgn}^{\lambda_2}\otimes K_{\alpha,k}.}
\tag{OC.4}
\]
Its maps, including the dual comparison, are specified in §§3–5.
Consequently, writing \(\tau=\mu\) when \(\lambda_2\) is
even and \(\tau=\mu^t\) when it is odd,
\[
\boxed{p_{\mu,(n)}^\lambda
=\dim\operatorname{Hom}_{S_m}([\tau],K_{\alpha,k}).}
\tag{OC.5}
\]

The same space is a lowest-type multiplicity for the actual unitary
dual pair \(U(r,1),U(m)\). More precisely, let \(L_k\) be the
one-column charged oscillator of §6. Then (OC.5) is the multiplicity
in \(S_\tau(L_k)\) of the irreducible lowest-weight oscillator
module whose lowest \(U(r)\times U(1)\) type has weights
\[
(\alpha_1+m/2,\ldots,\alpha_r+m/2;\,-b-m/2).
\tag{OC.6}
\]
All half-integral weights here refer to the stated metaplectic
preimages, or to a common covering group. The rational finite
identity (OC.4) uses ordinary permutation matrices after the
explicit vacuum untwist. No historical novelty is claimed for
the oscillator correspondence; the new comparison here assembles
it with T-049's actual diagonal quotient and the flag chart.

## 1. Every commuting operator and its scalar shift

Use indices \(a,b,c\in\{1,\ldots,r\}\), and add an index
\(0\). Define
\[
\begin{gathered}
A_{ab}=\sum_iX_{ai}\partial_{X_{bi}}+\frac m2\delta_{ab},
\qquad A_{00}=-\sum_iY_i\partial_{Y_i}-\frac m2,\\
A_{a0}=-R_a,\qquad A_{0a}=C_a,\\
B_{ij}=\sum_aX_{ai}\partial_{X_{aj}}-Y_j\partial_{Y_i}
       +\frac{r-1}{2}\delta_{ij},\qquad
G_{ij}=B_{ij}-\frac{r-1}{2}\delta_{ij}.
\end{gathered}
\tag{OC.7}
\]
They satisfy
\[
[A_{uv},A_{st}]=\delta_{vs}A_{ut}-\delta_{ut}A_{sv},
\quad [B_{ij},B_{pq}]=\delta_{jp}B_{iq}-\delta_{iq}B_{pj},
\quad [A_{uv},B_{ij}]=0.
\tag{OC.8}
\]
The \(G_{ij}\) are the ordinary algebraic \(\mathfrak{gl}(W)\)
action on \(\operatorname{Sym}(F\otimes W\oplus W^*)\).
In particular \(G_{ii}=Q_i\), whereas the oscillator's compact
diagonal weight on the charged space is
\((k+(r-1)/2)^m\).

Here is a direct verification of the signs and constants. The
polynomial Weyl relations give
\[
\begin{split}
[C_a,R_b]
&=\sum_iX_{bi}\partial_{X_{ai}}
  +\delta_{ab}\left(\sum_iY_i\partial_{Y_i}+m\right)\\
&=A_{ba}-\delta_{ab}A_{00},\\
[A_{ab},R_c]&=\delta_{bc}R_a,
\qquad [A_{ab},C_c]=-\delta_{ac}C_b,\\
[A_{00},R_a]&=-R_a,
\qquad [A_{00},C_a]=C_a.
\end{split}
\tag{OC.9}
\]
These identities, \([R_a,R_b]=[C_a,C_b]=0\), and the usual
matrix-unit brackets for \(X\partial_X\) prove the first
identity in (OC.8). The two terms in \(G_{ij}\) each give a
\(\mathfrak{gl}_m\) representation. Their commutators with
\(R_a\) cancel as \(X_{ai}Y_j-X_{ai}Y_j\); their
commutators with \(C_a\) cancel as well. This proves every
mixed bracket. The centers agree literally:
\[
\sum_aA_{aa}+A_{00}=\sum_iB_{ii}
=N_X-N_Y+\frac{m(r-1)}2.
\tag{OC.10}
\]
Thus all \(A\)'s preserve each joint charge space.

Give monomials the Fischer inner product
\(\langle X^uY^v,X^{u'}Y^{v'}\rangle
=\delta_{u,u'}\delta_{v,v'}u!v!\). Then
\[
R_a^\dagger=C_a,\quad A_{ab}^\dagger=A_{ba},\quad
A_{00}^\dagger=A_{00},\quad
A_{a0}^\dagger=-A_{0a},\quad B_{ij}^\dagger=B_{ji}.
\tag{OC.11}
\]
For a matrix in \(\mathfrak u(r,1)\), the coefficients of
\(E_{a0}\) and \(E_{0a}\) are complex conjugates; (OC.11)
makes its action skew-adjoint. The compact
\(\mathfrak u(m)\) action is skew-adjoint by the last identity.
These are exactly the two real forms with the declared shifts.

## 2. The real symplectic embedding and the vacuum character

Let \(H=\mathbf C^{r,1}\), \(W=\mathbf C^m\) with their
Hermitian forms, conjugate-linear in the first entry. On the real
vector space underlying \(H\otimes W\), take
\(\omega=\operatorname{Im}(h_H\otimes h_W)\).
The tensor actions of \(U(r,1)\) and \(U(m)\) are mutual
centralizers in its real symplectic group.

Indeed, a real-linear map commuting with the first group commutes
with its scalar \(i\), so is complex-linear. Its complex
commutant is \(1_H\otimes\operatorname{End}_{\mathbf C}(W)\).
One can see this without a real-form assumption: diagonal phases
give the diagonal matrix units on \(H\), positive-coordinate
unitaries give the matrix units within the positive block, and a
boost between a positive and the negative coordinate gives the
remaining off-diagonal units. Preservation of \(\omega\),
together with complex linearity, implies preservation of the
Hermitian form, since
\(\operatorname{Re}h(v,w)=\omega(v,iw)\). The commutant
inside the symplectic group is therefore exactly \(U(m)\).
The reverse argument starts with the natural irreducible \(U(m)\)
action and yields \(U(r,1)\).

Choose the positive compatible complex structure equal to \(i\)
on the positive part and \(-i\) on the negative part. Its
holomorphic creation space is
\(F\otimes W\oplus W^*\). For
\((a,z,g)\in U(r)\times U(1)\times U(m)\), its action is
\(a\otimes g\) on \(X\) and \(z^{-1}g^{-t}\) on
\(Y\). With the positive-energy oscillator convention of T-001,
the polynomial Fock space is tensored with the vacuum character
\(\chi_0\) on the metaplectic preimage, where
\[
\chi_0^2=(\det a)^m z^{-m}(\det g)^{r-1}.
\tag{OC.12}
\]
The half derivative of this determinant is exactly the collection
of constants in (OC.7). Thus (OC.7) is the actual oscillator
restriction for this real dual pair.

The \(GL(F)\) action used in (OC.3) removes the
\((\det a)^{m/2}\) vacuum factor. The ordinary column action
\(G\) removes the compact vacuum character \(\chi_W\),
whose square is \((\det g)^{r-1}\). If \(r\) is odd,
the explicit section of this cover with
\(\chi_W(g)=(\det g)^{(r-1)/2}\) gives the finite factor
\(\operatorname{sgn}^{(r-1)/2}\) on permutation matrices.
If \(r\) is even, retain the pullback double cover and its
character \(\chi_W\), then tensor by \(\chi_W^{-1}\).
This cancels the central kernel and descends to the literal
\(S_m\) action. In particular no fractional power of the sign
character is being used as a character of \(S_m\).

The primary oscillator source used here is Basile–Joung–Mkrtchyan–
Mojaza, *Dual Pair Correspondence in Physics: Oscillator Realizations
and Representations*, arXiv:2006.07102v2, §5.2, equations
(5.21)–(5.30), printed pp.29–31, at
[the primary PDF](https://arxiv.org/pdf/2006.07102).
Its parameters are \(M_+=r,M_-=1,N=m\). Equations
(5.21)–(5.22) give these operators and shifts; (5.27)–(5.30)
give the traceless lowest types. The complete cited passages were
read, including the dual tensor construction (A.25)–(A.28).
The source's double-cover convention is explicit in (1.16),
printed p.7, and its oscillator monodromy calculation is
(2.12)–(2.18), printed p.10.

## 3. The actual charge homogenization and quotient map

Put
\[
D_k=\bigotimes_{i=1}^m\operatorname{Sym}^{\ge k}F
\subset\mathbf Q[Z_{ai}],\qquad L_a=\sum_i Z_{ai}.
\tag{OC.13}
\]
On a polynomial \(f\) homogeneous of degree \(d_i\ge k\)
in each block, define
\[
\Phi_k(f)=f(X)\prod_iY_i^{d_i-k}.
\tag{OC.14}
\]
This is a rational \(GL(F)\times S_m\)-equivariant bijection
from \(D_k\) to \(\mathcal P^{[k]}\). Its inverse erases
the \(Y\)'s: a charge-\(k\) monomial has forced exponent
\(d_i-k\) on \(Y_i\). It preserves \(X\)-degree and
satisfies
\[
\Phi_k(Z_{ai}f)=X_{ai}Y_i\Phi_k(f),
\qquad \Phi_k(L_af)=R_a\Phi_k(f).
\tag{OC.15}
\]
For \(E=\mathfrak h_m\), write
\(I_i=(\ell_i\otimes F)\subset\operatorname{Sym}(E\otimes F)\)
with \(\ell_i=e_i-\mathbf1/m\). The complete all-degree
theorem T-049, including its actual substitution map, gives
\[
J_k=\bigcap_i I_i^k=\prod_iI_i^k
\simeq D_k/(L_1,\ldots,L_r)D_k.
\tag{OC.16}
\]
Therefore for \(b=N-mk\ge0\), (OC.14) induces
\[
(J_k)_N\simeq
\mathcal P^{[k]}_{N,b}\big/
\sum_aR_a\mathcal P^{[k]}_{N-1,b-1}.
\tag{OC.17}
\]
A space with negative degree is zero. Each arrow in (OC.17)
is induced by (OC.14) and the literal substitution
\(Z_{ai}\mapsto\ell_i\otimes f_a\).

The Fischer orthogonal complement of the denominator is exactly
\(\mathcal H^{[k]}_{N,b}\), by \(R_a^\dagger=C_a\).
Both the denominator and this kernel are stable under
\(GL(F)\times S_m\). Thus orthogonal projection gives an
equivariant isomorphism of the quotient with that kernel.
It is also rational and completely finite. On the indicated
finite-dimensional space set \(T=\sum_aR_aC_a\), and factor
its rational characteristic polynomial as
\(\det(t-T)=t^s q(t)\), \(q(0)\ne0\). Then
\[
\pi_{\mathrm{harm}}=q(T)/q(0).
\tag{OC.18}
\]
The operator \(T\) is positive semidefinite and self-adjoint;
its kernel is the common kernel of the \(C_a\)'s. It is
diagonalizable, so (OC.18) is one on its zero eigenspace and zero
on every other eigenspace. This includes an invertible \(T\),
when the result is zero, and \(T=0\), when it is the identity.
The zero-dimensional case has its unique zero map. The inverse
of the resulting map is inclusion of a harmonic vector followed
by the quotient in (OC.17).

For clarity, (OC.14) also transports lowering to the explicit
operator
\[
\Phi_k^{-1}C_a\Phi_k
=\sum_i(N_i-k+1)\partial_{Z_{ai}},
\qquad N_i=\sum_aZ_{ai}\partial_{Z_{ai}}.
\tag{OC.19}
\]
The rightmost derivative acts first; on block degree \(d_i\)
the coefficient is \(d_i-k\). At \(d_i=k\) it is zero,
so it preserves the truncated space. The induced monomial norm
is \(\prod_i u_i!(d_i-k)!\). With this norm (OC.19) is
the adjoint of multiplication by \(L_a\). This independently
checks the endpoint and every scalar in the charge map.

## 4. The finite harmonic member of theta correspondence

Let \(V_\gamma(W)\) denote the irreducible rational
\(GL(W)\)-module of highest weight \(\gamma\). The
traceless tensor form of the compact-member correspondence is
\[
\mathcal H_{N,b}
\simeq
\bigoplus_{\substack{\alpha\vdash N\\\ell(\alpha)\le r}}
S_\alpha F\otimes
V_{(\alpha_1,\ldots,\alpha_r,0,-b)}(W).
\tag{OC.20}
\]
Here \(\mathcal H_{N,b}\) imposes the lowering equations but
does not yet impose charge. This is the specialization
\(M_-=1\) of the source's (5.27)–(5.30). Its exact tensor
map is polarization into \(F\)-slots and \(W\)-slots,
application of their Young idempotents, and contraction of a
\(W\) slot with a \(W^*\) slot. The equations \(C_a=0\)
say precisely that all such contractions vanish after the
\(F\)-Young projection. The source's Levi–Civita map
(A.25) turns each covector column into its complementary vector
column; its relation (A.27) is the resulting Young relation.
It identifies the surviving irreducible highest weight in
(OC.20). Our lengths satisfy \(\ell(\alpha)+1\le m-1\)
when \(b>0\), so this use is strictly within that tensor range.

There is also a useful normalization of every displayed embedding.
Let \(\Delta_j=\det(X_{ai})_{1\le a,i\le j}\), and
\(\alpha_{r+1}=0\). Send the product of the standard highest
vectors in (OC.20) to
\[
v_{\alpha,b}=Y_m^b\prod_{j=1}^r
\Delta_j^{\alpha_j-\alpha_{j+1}}.
\tag{OC.21}
\]
It is nonzero, has \(GL(F)\)-weight \(\alpha\) and
ordinary \(GL(W)\)-weight \((\alpha,0,-b)\), and is
annihilated by every \(C_a\): its \(Y\) derivative uses
column \(m\), while its \(X\)'s use columns at most \(r\).
The compact raising operators kill the first-column minors.
Applying the two enveloping-algebra actions to (OC.21) supplies
the unique normalized intertwiner in (OC.20). This describes
the actual summand map as well as its labels. In the oscillator
action the compact weight in (OC.20) is shifted by
\((r-1)/2\) in every coordinate, and its lowest noncompact
type is (OC.6), directly from (OC.7).

Taking the charge weight in (OC.20) gives an ordinary
\(S_m\)-module isomorphism
\[
K_{\alpha,k}\simeq
\left(V_{(\alpha,0,-b)}(W)\right)_{(k^m)}.
\tag{OC.22}
\]
It uses literal permutation matrices for the \(G\) action.
The full compact group preserves the harmonic space; its
equal-weight subspace is preserved by these permutations.

## 5. Every determinant, dual, and first-row map in (OC.4)

First suppose \(e=0\). A direct calculation from (OC.1) gives
\[
\gamma=(\alpha,0,-b)
=\lambda_2\mathbf1-(\lambda^0_m,\ldots,\lambda^0_1).
\tag{OC.23}
\]
The actual rational representation map is
\[
V_\gamma(W)\simeq
(\det W)^{\lambda_2}\otimes(S_{\lambda^0}W)^*.
\tag{OC.24}
\]
To fix it without suppressing the dual, put
\(H=\lambda^0_1=\lambda_2+b\) and
\(\beta=(H-\lambda_m^0,\ldots,H-\lambda_1^0)
=(\alpha_1+b,\ldots,\alpha_r+b,b,0)\).
Columnwise exterior multiplication in the \(m\)-by-\(H\)
rectangle, followed by the Schur projections, is the perfect pairing
\[
S_{\lambda^0}W\otimes S_\beta W
\longrightarrow(\det W)^H.
\tag{OC.25}
\]
It is nonzero on complementary highest and lowest column tensors;
the highest weights are contragredient with this determinant
twist, so the induced pairing is perfect. Tensoring its second
factor by \((\det W)^{-b}\) gives (OC.24), with its
normalization matched to (OC.21). This also works when \(b=0\).

On the charge weight, (OC.24) reads
\[
K_{\alpha,k}\simeq
\operatorname{sgn}^{\lambda_2}\otimes
\left((S_{\lambda^0}W)_{(n_0^m)}\right)^*,
\tag{OC.26}
\]
since \(k-\lambda_2=-n_0\). The sign is exactly the
determinant of the permutation matrix in (OC.25).

We now give the dual comparison actually used in (OC.4). Realize
\(S_{\lambda^0}W\) as the image of a rational Young
idempotent in \(W^{\otimes mn_0}\). Equip the standard rational
basis of \(W\) with its dot product and use the tensor product
form. Restriction to this image, and then to its balanced weight
space, is nondegenerate: after extension to \(\mathbf R\)
the form is positive definite. Permutation matrices preserve it
and commute with the Young idempotent. Hence
\[
v\longmapsto\bigl(w\longmapsto\langle v,w\rangle\bigr)
\tag{OC.27}
\]
is a rational \(S_m\)-equivariant isomorphism to that balanced
space's dual. This map concerns the specified finite group action;
no \(GL(W)\)-self-duality is being substituted for (OC.24).

Finally allow \(e>0\). In T-032's flag algebra let \(x_i\)
be the first-column variables and \(u=\prod_i x_i\). The
balanced chart gives the actual bijection
\[
\cdot u^e:
(S_{\lambda^0}W)_{(n_0^m)}
\longrightarrow (S_\lambda W)_{(n^m)}.
\tag{OC.28}
\]
Indeed its right highest weight increases by \((me,0,\ldots,0)\),
its left weight increases by \((e^m)\), and both sides are
the same tail flag module in that chart. The inverse divides
by \(u^e\), with polynomiality proved in T-032 by the exact
minor count. Also \(u\) is fixed by every slot permutation.
When \(n>\lambda_2\),
\(\lambda^0_1=\lambda_2+N\ge\lambda_2\), so all its
partition and degree conditions hold. Composing (OC.28),
(OC.27), (OC.26) and (OC.22) proves (OC.4). Combining this
with T-003's balanced-weight Schur–Weyl map proves (OC.5).
The empty partition at \(n=0\) gives \(k=N=b=0\) and a
single trivial harmonic vector, so it is included.

There is a second explicit route through the frame ideal:
T-032/G-027's flag map and relative Schur pairing identify the
balanced module with
\(\operatorname{sgn}^{\lambda_2}
\operatorname{Hom}_{GL(F)}(S_\alpha F,(J_k)_N)\).
Equations (OC.14)–(OC.18) identify this with (OC.4).
Thus the charged oscillator and the frame-ideal model are related
by the actual homogenization, quotient and harmonic projection,
in addition to their compact highest-weight comparison.

## 6. A Schur functor of one charged lowest-weight module

For one column, the same homogenization identifies the charge-\(k\)
space with
\(L_k=\bigoplus_{d\ge k}\operatorname{Sym}^dF\).
Write \(z_a\) for its variables and \(N_z\) for their degree.
The \(\mathfrak{gl}_{r+1}\) action is
\[
\begin{gathered}
A^{(1)}_{ab}=z_a\partial_{z_b}+\tfrac12\delta_{ab},
\quad A^{(1)}_{00}=-N_z+k-\tfrac12,\\
A^{(1)}_{a0}=-z_a,
\qquad A^{(1)}_{0a}=(N_z-k+1)\partial_{z_a}.
\end{gathered}
\tag{OC.29}
\]
The last operator acts by \((d-k)\partial_{z_a}\) in
degree \(d\). Its lowest compact type is
\(\operatorname{Sym}^kF\otimes(\det F)^{1/2}\)
with negative \(U(1)\) weight \(-1/2\).

This algebraic lowest-weight module is irreducible. A nonzero
submodule contains a nonzero homogeneous element: the degree
operator is diagonal and a polynomial in it isolates any of the
finitely many degree components of a vector. Choose the least
degree occurring in the submodule. At degree \(d>k\) some
derivative is nonzero, and (OC.29) lowers that degree, a
contradiction. At degree \(k\) the irreducible compact
\(\operatorname{Sym}^k F\) is therefore present. Multiplication
by the \(z_a\)'s generates every higher symmetric power, so
the submodule is all of \(L_k\). The transported Fischer form
supplies its unitary oscillator realization on the corresponding
cover. This argument also covers \(k=0\).

Tensoring (OC.29) over the \(m\) columns gives exactly
(OC.7) on \(\mathcal P^{[k]}\), by (OC.14). Thus
\[
L_k^{\otimes m}\simeq\mathcal P^{[k]}
\tag{OC.30}
\]
as an actual module for the noncompact oscillator algebra and
the literal tensor-permutation \(S_m\). All group statements
can be read on a common cover of \(U(r,1)\); the tensor
vacuum exponents sum to \(m/2\), as required by (OC.7).

The compact-member theta decomposition, with its summands generated
by (OC.21), gives
\[
S_\tau(L_k)\simeq
\bigoplus_{\substack{\alpha,b\ge0\\|\alpha|-b=mk}}
\mathcal D^{(m)}_{\alpha,b}\otimes
\operatorname{Hom}_{S_m}
\left([\tau],(V_{(\alpha,0,-b)}W)_{(k^m)}\right).
\tag{OC.31}
\]
Here \(\ell(\alpha)\le r\), and
\(\mathcal D^{(m)}_{\alpha,b}\) is the irreducible oscillator
module with the lowest compact type (OC.6). The algebraic direct
sum in (OC.31) consists of finite polynomial vectors. The
displayed map is the known theta summand inclusion generated
from (OC.21), followed by taking the \(S_m\) Hom space in
(OC.30). Distinct labels have distinct lowest compact types.
Equations (OC.22), (OC.26) and (OC.27) therefore make its
specified multiplicity exactly (OC.5).

The irreducibility and direct sum in this application can also
be checked directly from (OC.20). In every finite total degree,
Fischer decomposition writes
\(\mathcal P_D=\mathcal H_D+\sum_aR_a\mathcal P_{D-2}\).
The \(R_a\)'s commute with the compact column action, so
iteration generates each column isotypic component from its
harmonics. For a given \(\gamma=(\alpha,0,-b)\),
(OC.20) gives exactly one harmonic bidegree and the irreducible
lowest \(GL(F)\) type \(S_\alpha F\). A nonzero submodule
of its column multiplicity space contains a homogeneous vector:
a polynomial in the energy
\(\sum_aA_{aa}-A_{00}=N_X+N_Y+m(r+1)/2\)
isolates a degree component. Its least occurring degree is killed
by every lowering operator. It therefore meets that unique
lowest type, contains the whole type by compact irreducibility,
and generates the full multiplicity space by the preceding
Fischer recursion. This proves irreducibility. The ordinary
isotypic direct sum for the compact group then gives (OC.31)
with the actual summand inclusions already specified.

The relevant lowest vectors can be obtained entirely in a finite
space: impose (OC.3), row degrees \(\alpha_a\), and
\(\sum_iX_{ai}\partial_{X_{bi}}=0\) for \(a<b\),
then apply the Specht Hom projector. All these rational operators
are explicit and commute with the slot action. The positive
lowest-type decomposition does not remove that last projector;
the general positive counts G-009–G-011 and the direct families
already proved evaluate it by their separately established maps.

## 7. Endpoints and proof status

At \(b=0\), every charged monomial has each block degree
exactly \(k\), so no lowering or quotient relation occurs:
\(\mathcal H^{[k]}_{mk,0}=(\operatorname{Sym}^kF)^{\otimes m}\).
Equation (OC.5) becomes the complementary-partition plethysm
identity with shape \(\alpha\), inner degree \(k\), and
the sign \(\operatorname{sgn}^{\lambda_2}\). Its actual
map is precisely the column pairing (OC.25). At \(k=0\),
(OC.16) is the polynomial quotient by the diagonal subspace,
\(J_0=\operatorname{Sym}(\mathfrak h_m\otimes F)\);
this recovers the stable flag chart through (OC.14)–(OC.18).
For \(\ell(\lambda)>m\), T-002's Cauchy decomposition
gives zero, and no oscillator label is needed.

The exact script `oscillator_charge_checks.py` verified 1895
normal-ordered Weyl-algebra commutator identities in ranks
\((r,m)=(1,3),(2,4),(3,5)\), together with the adjoints and
center identities. It constructed 42 literal rational joint
lowering/compact-raising nullspaces and their permutation traces.
After both determinant parities and the allowed first-row shifts,
all 663 plethysm coefficients and 663 class traces agreed with
the independent cycle-index/Murnaghan--Nakayama implementation.
Six exact characteristic-polynomial projectors passed idempotence,
lowering-kernel and rank checks. The largest tested polynomial
domain had dimension 200. The receipt is
`OSCILLATOR_CHARGE_RECEIPT.json`; these finite computations support
the all-parameter proofs and do not replace them.

The root, rectangular and archive agents independently read and checked the complete proof
(OC.1)–(OC.31), including the real centralizers, every scalar
shift, rational projection, actual dual form and first-row map,
and one-column irreducibility; all three whole-proof reviews passed.
The rectangular and archive agents also independently read the
full primary §5.2 and Appendix A passages and their cover
conventions. The direct isotypic-generation argument following
(OC.31) was independently supplied and checked by the archive
agent in its review. Its full review is recorded as A-061.

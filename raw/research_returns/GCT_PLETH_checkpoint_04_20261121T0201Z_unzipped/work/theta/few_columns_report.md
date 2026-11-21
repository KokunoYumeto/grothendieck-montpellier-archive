# Stable plethysm: explicit positive polytopes through six columns

Run `GCT_PLETH-20261121-theta`; GPT-6 Astra Pro; effort not surfaced. This supplements `theta_report.md`. The new work here makes the finite indexing and the actual polytope constraints explicit. The underlying stability theorem, the character reduction, the Littlewood identities and the Littlewood–Richardson rule are cited results, not claimed discoveries.

## T-010. Exact current stable family and its known four-column polytope

Write `lambda[N]=(N-|lambda|,lambda_1,lambda_2,...)` and

\[
c(\lambda)=\langle s_\lambda,H[H-1-h_1]\rangle,
\qquad H=\sum_{i\ge0}h_i.
\]

Sarkar, *Stability of plethysm coefficients and modified polynomial induction*, arXiv:2610.07929v2 (14 October 2026), Theorem D = Theorem 6.4, proves

\[
a_{n,m}^{\lambda[mn]}=c(\lambda)
\quad\bigl(m\ge\lambda_1,\ n\ge\lfloor(|\lambda|+\lambda_1)/2\rfloor,
\ mn-|\lambda|\ge\lambda_1\bigr).
\tag{T10.1}
\]

For `lambda=(4^u4,3^u3,2^u2,1^u1)`, his Theorem E = Theorem 7.3 identifies `c(lambda)` with the integer points `(t,epsilon_1,...,epsilon_4)` satisfying

\[
0\le\epsilon_i\le1,\quad t+\sum_i\epsilon_i\ge3,\quad
\epsilon_1-\epsilon_2=u_1,\quad \epsilon_3-\epsilon_4=u_3,
\quad\epsilon_2-\epsilon_3\le u_2,\quad t+\epsilon_4\le u_4.
\tag{T10.2}
\]

These are actual finite coefficients in the range (T10.1). The complete proofs of Theorems 6.4 and 7.3 were read and checked in this run. Source bytes were downloaded from `https://arxiv.org/src/2610.07929v2` and are retained in `sarkar/main.tex`.

Sarkar's Proposition 7.1 gives the exact character reduction, for `k>=lambda_1` and `V=C^k`,

\[
c(\lambda)=[S_{\lambda'}V:M_k],\qquad
M_k=\bigotimes_{i=2}^k F_i(\Lambda^iV),
\quad F_i=\operatorname{Sym}\ (i\text{ even}),\quad
F_i=\Lambda\ (i\text{ odd}).
\tag{T10.3}
\]

Here the bracket denotes multiplicity, `lambda'` denotes conjugation, and each full symmetric or exterior algebra is graded by ordinary scalar weight. Only total scalar degree `|lambda|` contributes. The source's Remark 7.5 notes the LR approach for five columns; T-012 and T-013 give full finite indexing and polytope constraints through six columns.

### The exact lambda-ring dictionary for (T10.3)

The involution `omega` of the symmetric-function ring satisfies `omega(p_r)=(-1)^{r-1}p_r` and `omega(s_lambda)=s_lambda'`. On a homogeneous input `h_i`, expansion in power sums gives

\[
\omega(p_r[h_i])=(-1)^{(r-1)i}p_r[e_i].
\]

Indeed, each term `p_{r alpha}` has sign `(-1)^{ri-length(alpha)}`, while the corresponding term of `p_r[e_i]` has sign `(-1)^{i-length(alpha)}`. Exponentiating `sum_r p_r/r` yields

\[
\omega(H[h_i])=H[e_i]\ (i\text{ even}),\qquad
\omega(H[h_i])=E[e_i]\ (i\text{ odd}),
\quad E=\sum_{j\ge0}e_j.
\tag{T10.4}
\]

The completed product `H[H-1-h_1]=product_{i>=2}H[h_i]` is well-defined degree by degree. Specialization to `k` variables sends `e_i` to zero for `i>k`, giving exactly (T10.3). On locally free sheaves this is the dictionary between symmetric powers of exterior powers and exterior powers of exterior powers in the representation Grothendieck ring. All factors of any given total scalar degree are finite locally free polynomial functors. The decomposition into characteristic-zero Schur summands takes place after base change to a characteristic-zero field; the polynomial operations themselves are defined over `Z`.

## T-011. An explicit Littlewood–Richardson polytope

For partitions `alpha,beta,gamma` of length at most `r`, padded by zeros, let `L_r(alpha,beta;gamma)` consist of real arrays `x_(i,j)`, `1<=i,j<=r`, with

\[
x_{ij}\ge0,\qquad x_{ij}=0\text{ for }i>j,
\tag{T11.1}
\]
\[
\sum_{i=1}^r x_{ij}=\gamma_j-\alpha_j,
\qquad \sum_{j=1}^r x_{ij}=\beta_i,
\tag{T11.2}
\]
\[
\alpha_j+\sum_{i=1}^{h}x_{ij}
\le\alpha_{j-1}+\sum_{i=1}^{h-1}x_{i,j-1}
\quad(2\le j\le r,\ 1\le h\le r),
\tag{T11.3}
\]
\[
\sum_{s=1}^{j-1}x_{i,s}\ge\sum_{s=1}^{j}x_{i+1,s}
\quad(1\le i<r,\ 1\le j\le r).
\tag{T11.4}
\]

Boundary partitions are required to have nonnegative entries and to be weakly decreasing. An invalid boundary gives the empty polytope. Its integer points count `c_{alpha,beta}^gamma`.

In the later gluing constructions, membership in `L_r` means precisely the displayed linear constraints also for real boundary variables. At a lattice point those boundary variables become integral partitions, so the same tableau bijection applies.

**Proof of the coordinate dictionary.** From an integer array fill row `j` of the skew diagram `gamma/alpha` with `x_(1,j)` ones, then `x_(2,j)` twos, and so on. The row and content conditions are (T11.2), and the filling is unique. In row `j`, the last box with entry at most `h` is at column `alpha_j+sum_(i<=h)x_(i,j)`. For strict increase down columns its upper neighbor must have entry at most `h-1`; (T11.3) states exactly that this last column lies within the removed upper-row prefix or within the upper-row prefix of entries at most `h-1`. Applying this for every `h` gives column strictness, and column strictness gives these inequalities.

Read each row from right to left, in order from top row to bottom row. For the ballot inequality comparing `i` and `i+1`, the largest deficit during row `j` occurs after all its `i+1` entries have been read and before any of its `i` entries have been read. The required inequality at that point is exactly (T11.4). Thus these conditions are equivalent to the lattice-word condition. The lattice-word condition also forces every entry in row `j` to be at most `j`, so the triangular zeros in (T11.1) impose no additional restriction. This is a bijection with Littlewood–Richardson tableaux. The classical LR rule gives the coefficient; see Macdonald, Chapter I, §9, or the representation-theoretic LR rule in the attached Landsberg source, §4, equations preceding `pieri`.

Each coordinate is bounded by the prescribed total content. Thus this is a bounded rational polytope, including the empty case.

## T-012. A fully explicit positive formula for stable tails of width five

Let `lambda_1<=5`, put `mu=lambda'`, padded to length five, and `N=|lambda|`. Define the following finite set `B_5` of pairs `(j,beta)`. Each listed `beta` has multiplicity one in `Lambda^j(Lambda^3 C^5)`:

| j | beta |
|---:|---|
|0|(0,0,0,0,0)|
|1|(1,1,1,0,0)|
|2|(2,2,1,1,0)|
|3|(3,3,1,1,1); (3,2,2,2,0)|
|4|(4,3,2,2,1); (3,3,3,3,0)|
|5|(5,3,3,2,2); (4,4,3,3,1)|
|6|(6,3,3,3,3); (5,4,4,3,2)|
|7|(6,4,4,4,3); (5,5,5,3,3)|
|8|(6,5,5,4,4)|
|9|(6,6,5,5,5)|
|10|(6,6,6,6,6)|

For `(j,beta) in B_5` and `epsilon in {0,1}`, define `Q_(lambda,beta,epsilon)` using real variables `P,Q,q`, a weakly decreasing nonnegative five-tuple `nu`, and two arrays `x,y` as follows:

\[
P\ge Q\ge0,\quad q\ge0,\qquad
\alpha=(P,P,Q,Q,0),\quad \eta=(q,q,q,q,0),\quad
\gamma=\mu-(\epsilon^5)\ge0,
\tag{T12.1}
\]
\[
x\in L_5(\alpha,\beta;\nu),\qquad
y\in L_5(\nu,\eta;\gamma),
\tag{T12.2}
\]
\[
2(P+Q)+3j+4q+5\epsilon=N.
\tag{T12.3}
\]

Every condition is linear with integer coefficients. The target boundary condition in (T12.1) makes the piece empty when needed. Then

\[
\boxed{c(\lambda)=
\sum_{(j,\beta)\in B_5}\ \sum_{\epsilon=0}^{1}
\#\bigl(Q_{\lambda,\beta,\epsilon}\cap\mathbb Z^{58}\bigr).}
\tag{T12.4}
\]

The ambient dimension counts three scalar parameters, five intermediate coordinates, and two five-by-five arrays; redundant triangular zeros can reduce it. The formula is a finite sum of 32 bounded rational polytopes, with tags retaining disjointness. It makes no homogeneous-dilation assertion.

**Proof.** By (T10.3), the required module is

\[
M_5=\operatorname{Sym}(\Lambda^2V)\otimes\Lambda(\Lambda^3V)
\otimes\operatorname{Sym}(\Lambda^4V)\otimes\Lambda(\Lambda^5V).
\]

The classical Littlewood decomposition of `Sym(Lambda^2 V)` has all even-column partitions, each once; in rank five these are `(P,P,Q,Q,0)`. This follows as well by applying (T10.4) to the symmetric-matrix identity T-007. The natural perfect wedge pairing gives `Lambda^4 V=V^* tensor det V`; hence

\[
\operatorname{Sym}^q(\Lambda^4V)
=\operatorname{Sym}^q(V^*)\otimes\det^q
=S_{(q,q,q,q,0)}V.
\]

Finally `Lambda(Lambda^5 V)=1+det V`. The complete finite decomposition of the second factor is the displayed `B_5`; the exact finite-character certificate is described under T-013 below and in `few_columns.py`.

The multiplicity of `S_mu V` is therefore

\[
\sum_{(j,\beta),\epsilon,P\ge Q\ge0,q\ge0,\nu}
c_{\alpha,\beta}^{\nu}c_{\nu,\eta}^{\mu-(\epsilon^5)}.
\]

Every summand has scalar degree `2(P+Q)+3j+4q+5epsilon`. Only degree `N` contributes. Apply the integer-point bijection T-011 twice, retaining `P,Q,q,nu` as coordinates rather than summing them externally. This proves (T12.4). Equation (T12.3) bounds the three scalar parameters; the two LR row/content conditions bound `nu,x,y` by `N`. Thus every piece is bounded.

## T-013. A fully explicit positive formula for stable tails of width six

Let `lambda_1<=6`, put `mu=lambda'` padded to length six, and `N=|lambda|`. Let `B_6` be the complete 156-row list in `EXTERIOR_CUBE_RANK_6.tsv`. Its pair `(j,beta)` denotes one copy of `S_beta C^6` in `Lambda^j(Lambda^3 C^6)`; every listed multiplicity is one, `0<=j<=20`, and `|beta|=3j`.

For `(j,beta) in B_6` and `q in {0,...,6}`, set

\[
\theta(q)=(q^{6-q},(q-1)^q).
\tag{T13.1}
\]

For `q=0` the second block has length zero and `theta(0)=(0^6)`. Define `R_(lambda,beta,q)` by variables `P,Q,R,a,b,c,t`, intermediate partitions `nu,xi` of length at most six, and three six-by-six arrays `x,y,z` satisfying

\[
P\ge Q\ge R\ge0,\quad a\ge b\ge c\ge0,\quad t\ge0,
\tag{T13.2}
\]
\[
\alpha=(P,P,Q,Q,R,R),\qquad
\eta=(a+b,a+b,a+c,a+c,b+c,b+c),\qquad
\gamma=\mu-(t^6)\ge0,
\tag{T13.3}
\]
\[
x\in L_6(\alpha,\beta;\nu),\qquad
y\in L_6(\nu,\eta;\xi),\qquad
z\in L_6(\xi,\theta(q);\gamma),
\tag{T13.4}
\]
\[
2(P+Q+R)+3j+4(a+b+c)+5q+6t=N.
\tag{T13.5}
\]

Then

\[
\boxed{c(\lambda)=
\sum_{(j,\beta)\in B_6}\ \sum_{q=0}^{6}
\#\bigl(R_{\lambda,\beta,q}\cap\mathbb Z^{127}\bigr).}
\tag{T13.6}
\]

There are 1092 tagged bounded rational polytopes in this formula. There are seven scalar variables, twelve intermediate-partition coordinates, and 108 array coordinates, totaling 127. Empty pieces are allowed. Thus the finite coefficient in (T10.1) has an explicit positive lattice-point formula for every tail of width at most six.

**Proof of the representation formula.** The exact factorization is

\[
M_6=\operatorname{Sym}(\Lambda^2V)\otimes\Lambda(\Lambda^3V)
\otimes\operatorname{Sym}(\Lambda^4V)\otimes\Lambda(\Lambda^5V)
\otimes\operatorname{Sym}(\Lambda^6V).
\]

The first factor has partitions `alpha=(P,P,Q,Q,R,R)`, each once. The perfect wedge pairing `Lambda^4 V=Lambda^2 V^* tensor det V` sends the summand `(a,a,b,b,c,c)` in symmetric degree `d=a+b+c` to its dual tensored with `det^d`. Its highest weight is

\[
(d-c,d-c,d-b,d-b,d-a,d-a)
=(a+b,a+b,a+c,a+c,b+c,b+c)=\eta.
\]

This proves the asserted indexing of the third factor with no omitted determinant shift. The pairing `Lambda^5 V=V^* tensor det V` gives

\[
\Lambda^q(\Lambda^5V)=\Lambda^q(V^*)\otimes\det^q
=S_{\theta(q)}V,\qquad 0\le q\le6.
\]

The last factor has summands `det^t`, `t>=0`. The second factor is the fixed table `B_6`. Iterating the LR rule three times yields

\[
\sum_{(j,\beta),q,P,Q,R,a,b,c,t,\nu,\xi}
c_{\alpha,\beta}^{\nu}
c_{\nu,\eta}^{\xi}
c_{\xi,\theta(q)}^{\mu-(t^6)}.
\]

The scalar degrees of the five factors are respectively
`2(P+Q+R),3j,4(a+b+c),5q,6t`. Keeping degree `N` gives (T13.5). Gluing the three integer-point descriptions from T-011 along the displayed intermediate partitions gives (T13.6). Every scalar variable in (T13.2) is bounded by (T13.5), every intermediate partition has size at most `N`, and each nonnegative array entry is bounded by a row or content sum at most `N`. This proves boundedness as well as finiteness of the formula.

### Complete finite certificate for `B_5` and `B_6`

For `r=5,6` the exact torus character of the entire finite exterior algebra is

\[
C_r(t;x)=\prod_{I\subset\{1,\ldots,r\},\ |I|=3}
\left(1+t\prod_{i\in I}x_i\right).
\tag{T13.7}
\]

Let `rho=(r-1,...,0)` and write `M_j(w)` for the coefficient of `t^j x^w` in this finite product, with zero for unsupported weights. The Weyl alternant identity gives the exact multiplicity

\[
b_{j,\beta}=\sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)
M_j(\beta+\rho-\sigma\rho).
\tag{T13.8}
\]

The integer program `few_columns.py` expands (T13.7) without floating point arithmetic, evaluates (T13.8) on every dominant weight in its support, and writes the complete tables. Every irreducible highest weight is a dominant weight in that support, so the candidate set is exhaustive. The resulting tables have respectively 16 and 156 entries, all multiplicity one. As a separate check, the program reconstructs the character of each listed Schur module by recursively enumerating interlacing restrictions and compares every monomial in every exterior degree with (T13.7). Both complete comparisons pass. Dimension totals are `2^10=1024` and `2^20=1048576`.

This is a finite exact computation certificate, together with its mathematical extraction formula and an independent character reconstruction. It is not labeled a proof-assistant certificate. The table is fixed data independent of the user-varying partition `lambda`. Once the table is supplied, formulas (T12.4) and (T13.6) use only counts of integer points in explicitly stated bounded polytopes.

## T-014. Stable nonvanishing in an explicit family of every width

Let `lambda` range over the partitions with no part equal to one, with arbitrary multiplicities of even parts, and with multiplicity at most one for each odd part. Then

\[
\boxed{c(\lambda)\ge1.}
\tag{T14.1}
\]

The empty partition has `c(empty)=1`, the constant term of the completed character, and is included separately from the nonempty case below.

Consequently, for the exact parameter range in (T10.1),

\[
a_{n,m}^{\lambda[mn]}\ge1.
\tag{T14.2}
\]

**Proof for nonempty `lambda`.** Put `k=lambda_1` and `u_i=m_i(lambda)`. For even `i`, the pure power of the highest wedge vector
`(e_1 wedge ... wedge e_i)^{u_i}` is a nonzero highest vector of weight `u_i omega_i` in `Sym^{u_i}(Lambda^i V)`. For odd `i`, the permitted values `u_i=0,1` select respectively the scalar vector or the highest wedge vector in `Lambda^{u_i}(Lambda^i V)`. Their tensor product is nonzero and is killed by all positive-root operators. Its highest weight is

\[
\sum_{i=2}^k u_i\omega_i=\lambda',
\]

because the `j`th coordinate equals `sum_(i>=j)u_i`, the height of the `j`th column of `lambda`. It lies in scalar degree `sum i u_i=|lambda|`. Complete reducibility in characteristic zero gives a constituent `S_lambda' V` of `M_k`. Equation (T10.3) proves (T14.1), and (T10.1) transports it to (T14.2).

This explicitly includes all partitions with even parts and, for example, `(6^u)`, `(4^a,3,2^b)`, and `(8^a,7,6^b,5,4^c,3,2^d)`. It is a sufficient support family, with no claim that it exhausts the stable support.

## Subsequent positive counts and the smaller direct-formula problem

The stable coefficients of tails of width at most six have the small explicit polytope formulas T-012 and T-013; T-014 proves support in a specified family of every width. Formula (T10.3) remains exact at arbitrary width. Subsequent statements T-016–T-020 in `work/theta/width7/width7_report.md` give an exact three-variable positive polytope for the constituents of shape `(A,B^5,C)` in `Sym^d(Lambda^4 C^7)`, as well as further stable nonvanishing families and a precise boundary-valuation formula for other weights.

The general existence question has also advanced: G-009–G-010 in `work/root/invariant_polytope_report.md` and `work/root/general_polytope_extensions.md` give terminating finite-presentation and standard-monomial polytope constructions for all symmetric and general Schur plethysm coefficients, including the unstabilized coefficients. G-011 does the same for the actual canonical-map image, kernel, and cokernel modules. G-012 supplies four direct polytopes for the full outer-degree-three family. T-024–T-028 in `work/theta/end_node/` further give a uniform polynomial-size polytope and an arithmetic support test for every outer Schur functor with inner symmetric power and output shape `(alpha,beta^(m-2),gamma)`, with a direct toric algebra degeneration for symmetric outer powers. Thus the current narrower task is to replace large parameter-dependent Reynolds enumeration and elimination by small, efficiently specified presentations or polyhedral formulas outside these direct families. The width-seven valuation outside T-018 is one concrete calculation for that purpose; it is not a remaining obstruction to the existence of a terminating positive count.

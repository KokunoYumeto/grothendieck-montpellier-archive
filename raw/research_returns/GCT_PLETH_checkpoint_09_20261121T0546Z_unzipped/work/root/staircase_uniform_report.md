# Uniform nonvanishing on staircase families

## G-022. Every outer Schur label in an explicit all-rank family

Let \(m\ge3\), let \(r,d\ge0\) be integers with \(r(m-1)\) even,
and put
\[
n=d+\frac{r(m-1)}2,\qquad
\lambda=(d+r(m-1),d+r(m-2),\ldots,d+r,d).
\tag{ST.1}
\]
Define \(D=(m-1)(m-2)/2\). The following explicit bound proves
nonvanishing for every outer partition \(\mu\vdash m\):
\[
r\ge2(m-1),\qquad
r^{m-2}>(m!-1)2^{(m-2)^2}(m-2)^D.
\tag{ST.2}
\]
In particular the simpler unconditional family \(r\ge(2m)^m\), with
the displayed parity requirement, has
\[
\boxed{p_{\mu,(n)}^\lambda>0\quad\text{for every }\mu\vdash m.}
\tag{ST.3}
\]
The proof below gives actual finite-group traces and an explicit
lower bound for each multiplicity. No historical priority is asserted.

## 1. The actual balanced trace from the Weyl determinant

First set \(d=0\), and write \(\delta=(m-1,m-2,\ldots,0)\).
The alternating-determinant formula for a Schur character gives the
polynomial identity
\[
s_{r\delta}(X_1,\ldots,X_m)
=\frac{\Delta(X_1^{r+1},\ldots,X_m^{r+1})}{\Delta(X_1,\ldots,X_m)}
=\prod_{i<j}\sum_{u=0}^{r}X_i^{r-u}X_j^u.
\tag{ST.4}
\]
Here both determinants use descending powers, so
\(\Delta(X)=\prod_{i<j}(X_i-X_j)\). The formula follows by
substituting \(r\delta_i+m-i=(r+1)(m-i)\) into that determinant.
Every factor division on the right is the finite geometric-series
identity; hence (ST.4) holds as a polynomial including repeated
variables.

Let \(g\in S_m\) have cycle lengths \(\ell_1,\ldots,\ell_c\).
The eigenvalues of \(\operatorname{diag}(t_1,\ldots,t_m)g\) on a
cycle are \(z_i\zeta_{\ell_i}^j\), where
\(z_i^{\ell_i}=T_i=\prod_{a\text{ in cycle }i}t_a\).
In the trace on \(S_{r\delta}\mathbf Q^m\), taking the coefficient
of \(\prod_a t_a^{r(m-1)/2}\) gives the trace on its balanced weight
space. Indeed the permutation sends each torus weight space to its
permuted weight; only fixed weights contribute to the trace, and this
coefficient selects precisely the specified balanced weight. Thus
\[
\operatorname{tr}(g\mid B_r)
=[T_1^{r(m-1)/2}\cdots T_c^{r(m-1)/2}]
       s_{r\delta}(z_i\zeta_{\ell_i}^j),
\tag{ST.5}
\]
where \(B_r=(S_{r\delta}\mathbf Q^m)_{((r(m-1)/2)^m)}\).
This is the exact normalizer representation of T-003.

A cycle with \(\gcd(r+1,\ell_i)>1\) has two equal powered
eigenvalues in the numerator of (ST.4), while the denominator is
nonzero over the field of independent cycle parameters. Its entire
trace polynomial is therefore zero.

For the other cycles, multiplication by \(r+1\) permutes their
residues. Let \(\kappa\in\{1,-1\}\) be the product of the signs
of these actual residue permutations. The within-cycle Vandermonde
ratio is
\(\kappa_i T_i^{r(\ell_i-1)/2}\). Its exponent is an integer:
for even \(\ell_i\), coprimality forces \(r\) even.
For two cycles, put \(g_{ij}=\gcd(\ell_i,\ell_j)\). Their cross
Vandermonde is
\[
(-1)^{\ell_i+g_{ij}}
\bigl(T_i^{\ell_j/g_{ij}}-T_j^{\ell_i/g_{ij}}\bigr)^{g_{ij}}.
\]
This follows by taking the product of
\(X^{\ell_j}-T_j\) over the \(\ell_i\) roots of
\(X^{\ell_i}-T_i\); the distinct roots occur \(g_{ij}\) times.
The same sign occurs in the numerator and cancels. Consequently the
actual trace in (ST.5) is \(\kappa\) times the coefficient in the
following polynomial with nonnegative coefficients:
\[
\prod_iT_i^{r(\ell_i-1)/2}
\prod_{i<j}
\left(\sum_{u=0}^r
T_i^{(r-u)\ell_j/g_{ij}}T_j^{u\ell_i/g_{ij}}
\right)^{g_{ij}}.
\tag{ST.6}
\]
All root choices have disappeared. This proves an exact signed lattice
trace using the literal cycle action, rather than an identification
based only on ordinary torus characters.

## 2. An upper bound for every nonidentity trace

Interpret the \(g_{ij}\) powers in (ST.6) as parallel edges, each
with an integer variable \(0\le u_e\le r\). The coefficient
conditions are linear equations. Their matrix is the weighted incidence
matrix with column
\(-\ell_j/g_{ij}\) at vertex \(i\) and
\(\ell_i/g_{ij}\) at vertex \(j\). Multiplying row \(i\) by
\(\ell_i\) changes this column into
\((\ell_i\ell_j/g_{ij})(-e_i+e_j)\). Thus the rank is \(c-1\)
for \(c\ge2\). Fix a spanning tree. Once all other edge variables
are specified, successive removal of tree leaves determines every tree
variable uniquely over \(\mathbf Q\). An admissible integer solution
is therefore determined by
\[
D_g=\sum_{i<j}g_{ij}-c+1
\]
variables, each with at most \(r+1\) choices. For \(c=1\) the
trace has absolute value at most one and set \(D_g=0\). We have proved
\[
|\operatorname{tr}(g\mid B_r)|\le(r+1)^{D_g}.
\tag{ST.7}
\]

For nonidentity \(g\), write \(s=m-c\ge1\). The elementary
inequality \(\gcd(a,b)\le1+(a-1)(b-1)\) holds for all positive
integers: at an argument one it is equality; otherwise its right side
is at least \(\min(a,b)\). For \(c\ge2\) it gives
\[
D_g\le\binom{c-1}{2}+\binom{s}{2}
\le\binom{m-2}{2}=D-(m-2).
\tag{ST.8}
\]
For the first inequality, expand the pair sum of \((\ell_i-1)\)
and use \(\sum(\ell_i-1)^2\ge s\). The difference in the second
inequality is exactly \((c-2)(s-1)\ge0\). At \(c=1\), (ST.8)
is immediate for \(m\ge3\). This proves the needed degree saving
for every nonidentity class, with no classification of its cycles.

## 3. An explicit large box inside the identity count

At the identity, (ST.4) counts integer assignments to the edges of
\(K_m\), each in \([0,r]\), such that the exponent at each vertex
is \(r(m-1)/2\). There are \(D\) independent edge variables after
the \(m-1\) independent balance equations.

Construct an integral central assignment. For even \(r\), put
\(r/2\) on every oriented edge. For odd \(r\), the parity assumption
forces \(m\) odd. Take the cyclic regular tournament on
\(\mathbf Z/m\): the arrows from \(i\) go to
\(i+1,\ldots,i+(m-1)/2\). Put \(\lfloor r/2\rfloor\) plus the
corresponding zero-or-one orientation contribution on each edge.
Every vertex then has the required exponent, and every edge is at
least \(\lfloor r/2\rfloor\) from one endpoint and at least that
far from the other.

Set
\[
q=\left\lfloor\frac{\lfloor r/2\rfloor}{m-2}\right\rfloor.
\]
Choose each edge among vertices \(2,\ldots,m\) independently within
\([-q,q]\) of its central value. There are exactly \(D\) such edges.
For each vertex \(i\ge2\), change the edge from vertex one by the
negative of its resulting imbalance. Its absolute change is at most
\((m-2)q\le\lfloor r/2\rfloor\), so it stays in \([0,r]\).
The remaining balance equation at vertex one follows because the total
exponent is unchanged. Different choices of the free edges give
different lattice assignments. Thus
\[
\dim B_r\ge(2q+1)^D
\ge\left(\frac{r}{2(m-2)}\right)^D
\qquad(r\ge2(m-1)).
\tag{ST.9}
\]
For the last bound,
\(2q+1\ge(r-m+1)/(m-2)\ge r/(2(m-2))\), using the elementary
floor inequalities. This proves the stated lower bound by an explicit
injective map of integer boxes into the balanced edge assignments.

## 4. Multiplicity, the explicit threshold, and the canonical image

For each irreducible character \(\chi_\mu\) of dimension \(f_\mu\),
averaging a positive Hermitian form makes every group element unitary,
so \(|\chi_\mu(g)|\le f_\mu\). Taking the actual character
projector and using (ST.7)–(ST.9) gives
\[
[\mu:B_r]\ge\frac{f_\mu}{m!}
\left[
\left(\frac{r}{2(m-2)}\right)^D
-(m!-1)(r+1)^{D-m+2}
\right].
\tag{ST.10}
\]
Under (ST.2) the right side is positive: use \(r+1\le2r\) and
\(2D-m+2=(m-2)^2\). Since the left side is an integer, it is at
least one. This proves the first assertion.

For \(m=3\), the power inequality in (ST.2) is \(r>10\), so
\(r\ge6^3\) suffices. For \(m\ge4\), the bound \(r\ge(2m)^m\)
gives
\[
r^{m-2}\ge2^{m(m-2)}m^{m(m-2)}
>(m!-1)2^{(m-2)^2}(m-2)^D.
\]
Indeed \(m!<m^m\), \(m(m-2)-(m-2)^2=2(m-2)>0\), and
\(m(m-2)-m-D=(m^2-3m-2)/2\ge1\). This proves (ST.3).

Multiplication by the actual determinant section identifies
\(S_{d\mathbf1+r\delta}\) with \(\det^d\otimes S_{r\delta}\).
It shifts the balanced content by \(d\) in each coordinate and the
permutation character by \(\operatorname{sgn}^d\). Thus it permutes
outer labels by transpose and proves the same assertion for every
\(d\ge0\), as stated in (ST.1).

For the symmetric outer label, these are also nonzero components of
the actual canonical image
\(h_{n,m}:\operatorname{Sym}^n\operatorname{Sym}^m V\to
\operatorname{Sym}^m\operatorname{Sym}^n V\) in every dimension at
least the number of positive parts of \(\lambda\). In the simpler
family \(r\ge(2m)^m\), its inner degree satisfies
\(n\ge(m-1)^2\). Sra, *The q-Foulkes problem III*, Theorem1.3,
proves surjectivity of this exact grid map in that range. Applying its
surjection to the positive target multiplicity just proved gives the
image multiplicity, with its lower bound (ST.10) after the determinant
twist. This uses the specified map and its cited full-range theorem.

## 5. Exact geometric and lambda-ring transport

The balanced module in (ST.5) is the torus weight subsheaf of the Schur
operation on the rank-\(m\) standard bundle. Its finite normalizer
projector is the same projector constructed through the compact dual
pair in T-001–T-003. Formula (ST.4) is evaluated after the actual
endomorphism \(\operatorname{diag}(t)g\); the cycle coefficient map
therefore computes that projector's trace. The box injection in §3
proves a lower bound on its rank after character averaging.

These are the frame-torsor and comodule maps of SGA3 I4.5,4.7.2–4.7.3,
and the Schur operations in the exact representation group of SGA6
V4.2,4.4,4.8–4.9 and VI3.3. They evaluate the composed operations of
cote133/024–029 through the explicit universal map A-010. The last
paragraph of §4 applies the coordinate-image map of EGA I9.5.2 and
G-003 to give an actual nonzero graded Chow coordinate section. All
multiplicities and finite projectors here are over characteristic zero;
the determinant and coefficient constructions have the indicated
integral formulas before those projectors are divided by \(m!\).

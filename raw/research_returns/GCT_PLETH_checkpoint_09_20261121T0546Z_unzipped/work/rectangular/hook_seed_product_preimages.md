# Products of the explicit hook seeds in the actual canonical image

## R-052. A uniform semigroup with prescribed preimages

Fix \(a\ge2\). Choose integers
\(k,c_2,\ldots,c_a\ge0\), and put
\[
\begin{gathered}
T_m=\binom m2+1,\qquad D_m=\binom{m+1}{2}-1,\\
N=k+\sum_{m=2}^a m c_m\ge1,\qquad
T=\sum_{m=2}^a T_m c_m,\qquad
D=\sum_{m=2}^a D_m c_m,\\
\rho_j=\sum_{m=j+2}^a c_m\quad(1\le j\le a-2),\qquad \rho_{a-1}=0,\\
\lambda=(aN-D,T,\rho_1,\ldots,\rho_{a-2}),
\end{gathered}
\tag{HP.1}
\]
with zero parts omitted. In every dimension at least
\(\ell(\lambda)\), the actual normalized canonical map satisfies
\[
\boxed{\operatorname{mult}_{\lambda}\operatorname{im}h_{N,a}\ge1.}
\tag{HP.2}
\]
The proof gives an actual polynomial preimage with its complete
rational scalar, including every degree-one factor.
This is a direct product consequence of the proved R-050 maps;
the multiplicative coordinate-ring construction is the one already
proved in R-037 EP.3–EP.5. No independence of different products
of the same weight is asserted.

The partition and size checks are explicit:
\[
\begin{split}
\sum_{j=1}^{a-2}\rho_j&=\sum_{m=2}^a(m-2)c_m=D-T,\\
\lambda_1-\lambda_2
&=ak+\sum_{m=2}^a m(a-m)c_m\ge0,\\
T-\rho_1&=2c_2+\sum_{m=3}^a(T_m-1)c_m\ge0,\\
\rho_j-\rho_{j+1}&=c_{j+2}\ge0.
\end{split}
\tag{HP.3}
\]
Thus every declared parameter gives a partition of \(aN\),
including the pure top-row case with all \(c_m=0\).

## 1. The actual graded multiplication morphism

Use the same symmetric-tensor normalization as HM.16.
Let \(\mathcal A_a=\operatorname{Sym}(\operatorname{Sym}^aV)\).
Its polynomial degree-\(N\) piece is
\(\operatorname{Sym}^N(\operatorname{Sym}^aV)\).
In the slot-polynomial realization, let \(\mathcal B_a\) be the
algebra of \(S_a\)-invariant polynomials in \(a\) vector slots
whose degree in every slot is the same. Its degree-\(N\) piece is
\(\operatorname{Sym}^a(\operatorname{Sym}^NV)\).
The multiplication in \(\mathcal B_a\) is ordinary multiplication
of these actual slot polynomials, retaining slot symmetry.

The graded algebra morphism is the pullback along multiplication
of the \(a\) linear factors:
\[
\rho_a:\mathcal A_a\longrightarrow\mathcal B_a,
\qquad (\rho_a)_N=h_{N,a}.
\tag{HP.4}
\]
On a generator \(v^a\) it has value
\(\prod_{i=1}^a v_i\). This is exactly the scalar-one map EP.4;
its polarization proves the equality on every generator in
\(\operatorname{Sym}^aV\), and algebra multiplication proves
the graded statement. In particular, for homogeneous factors,
\[
h_{N_1+N_2,a}(G_1G_2)
=h_{N_1,a}(G_1)\,h_{N_2,a}(G_2).
\tag{HP.5}
\]
This equality concerns the specified tensor-normalized maps and
their actual products.

## 2. The literal seed product and its inverse scalar

Choose a highest coordinate \(x\), and use HM.19–HM.20 for every
\(2\le m\le a\), padding its transverse coordinates by zero
when working in a common larger rank. Define
\[
G_{a,m}=C_m(m,a)^{-1}F_{m,a;m}
\in\operatorname{Sym}^m(\operatorname{Sym}^aV),
\tag{HP.6}
\]
where the exact nonzero scalar from HM.24 is
\[
C_m(m,a)=(-1)^{\binom m2}\frac{m!}{a}\,
\frac{\prod_{j=1}^{m-1}j!}{\prod_{d=2}^{m}(a)_d}.
\tag{HP.7}
\]
Its actual image is \(F_{a,m;m}\), of weight
\((am-D_m,T_m,1^{m-2})\).
All transverse vectors can instead be embedded by the first
\(m-1\) basis coordinates; the corresponding Young maps are
natural, and give the same highest tensor in the common space.

The explicit preimage and target polynomial are
\[
\boxed{\begin{aligned}
G&=(x^a)^k\prod_{m=2}^a G_{a,m}^{\,c_m},\\
h_{N,a}(G)&=
\left(\prod_{i=1}^a x_i\right)^k
\prod_{m=2}^a F_{a,m;m}^{\,c_m}.
\end{aligned}}
\tag{HP.8}
\]
Equation (HP.5), HM.24, and the degree-one generator identity
prove this equality, including the product of every reciprocal
factor in (HP.7).

Each factor in the second line is a nonzero polynomial highest
vector. Their product is nonzero because the slot polynomial ring
is an integral domain. Upper-unipotent invariance and diagonal
weight multiplication show that its weight is exactly the sum in
(HP.1); these are the literal group actions on the product.
Thus it generates a copy of \(S_\lambda V\) in the actual image,
proving (HP.2). Below the stated rank the Schur component is zero.
When \(m\) has \(c_m=0\), its factor is absent, so the proof
requires only the dimension \(\ell(\lambda)\) in (HP.2).

## 3. A scaled family in every rank

For every \(a\ge2\) and \(q\ge1\), take \(c_a=q\) and all
other parameters zero. With \(T_a=\binom a2+1\), the resulting
concrete family is
\[
\boxed{\begin{gathered}
N=aq,\qquad\lambda=(qT_a,qT_a,q^{a-2}),\\
\operatorname{mult}_{\lambda}\operatorname{im}h_{aq,a}\ge1.
\end{gathered}}
\tag{HP.9}
\]
The exact highest preimage is
\[
\left(
(-1)^{\binom a2}\frac{(a!)^{a-1}}
{\bigl(\prod_{j=1}^{a-1}j!\bigr)^2}
F_{a,a;a}\right)^q,
\tag{HP.10}
\]
and its image is \(F_{a,a;a}^{\,q}\).
For example, every \(a\ge2\) has the explicitly reached
weight \((2T_a,2T_a,2^{a-2})\) at inner degree \(2a\).
The entries in (HP.10) give its entire preimage and normalization.
For \(a\ge5\), \(2a<(a-1)^2\), so this example lies below
the currently recorded general quadratic canonical range.
This comparison does not assert that all other components at
that degree are reached.

The products and scalars are rational and natural, so the same
statements hold over every characteristic-zero field.
The associated-bundle and representation-\(K_0\) transport uses
the actual frame maps and exact SGA/EGA locators in R-036 §5.
It takes place after the explicit polynomial preimage (HP.8).

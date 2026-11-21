# A one-row improvement for actual canonical maps in every width

## R-048. Tails with the stated odd parts

Let \(a,n\ge2\), let \(\nu\) be a nonempty partition of size
\(D\) and width \(t=\nu_1\ge2\), and require
\(\lambda=(an-D,\nu)\) to be a partition.
Consider the following two explicit parameter families:

1. \(D,t\) are even, and \(\nu\) has at least two odd parts,
   counted with multiplicity;
2. \(D,t\) are odd, and \(\nu\) has at least three odd parts,
   counted with multiplicity.

Put
\[
M=\frac{D+t}{2}-1.
\tag{OI.1}
\]
For every \(n\ge M\), the normalized canonical map
\[
h_{n,a}:\operatorname{Sym}^n(\operatorname{Sym}^aV)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^nV)
\]
is surjective on its entire \(\lambda\)-isotypic component:
\[
\boxed{\operatorname{mult}_\lambda\operatorname{im}h_{n,a}
       =a_{a,n}^{\lambda}.}
\tag{OI.2}
\]
This holds over every characteristic-zero field and in every
finite dimension. Below \(\ell(\lambda)\), the component is zero.

For \(a,n\ge M\), the specified map is an isomorphism on this
component. Its common multiplicity is the formal moment
coefficient
\[
[S_\nu U:\operatorname{Sym}(\bigoplus_{d\ge2}\operatorname{Sym}^dU)].
\tag{OI.3}
\]
No size restriction on the auxiliary \(U\) is needed beyond
\(\dim U\ge\ell(\nu)\).

The established starting coefficient threshold
\(N=\lfloor(D+t)/2\rfloor\) is Sarkar's Theorem D, numbered
Theorem 6.4 in arXiv:2610.07929v2, as recorded in R-046/T-010.
Here \(D+t\) is even and \(M=N-1\).
The following argument retains the actual row restriction and
the exact normalized moment factorization. No historical
novelty claim is made.

## 1. The exact omitted exterior layer in arbitrary width

Set \(T=\mathbb Q^t\) and use
\[
C_s=(\Lambda(E_s\otimes T))^{S_s},\qquad
B_s=(\Lambda(W_s\otimes T))^{S_s},
\]
where \(E_s=\mathbb Q^s\), \(W_s=\mathbf1^\perp\), and
\(P_se_i=e_i-s^{-1}\mathbf1\).
The actual row-orbit decomposition TM.8 has at most \(t\)
singleton factors. At degree \(D=2N-t\), a term using \(N\)
nonempty rows satisfies
\[
D\ge2N-e_1\ge2N-t=D.
\tag{OI.4}
\]
Both inequalities are therefore equalities. All \(t\)
singleton factors occur, all remaining occupied rows have
exterior degree two, and their number is
\(N-t=(D-t)/2\).
Thus the complete additional row-orbit module at row count
\(N\), compared with \(M=N-1\), is
\[
L_\nu=\det T\otimes
          \operatorname{Sym}^{(D-t)/2}(\Lambda^2T).
\tag{OI.5}
\]
For every lower degree \(e<D\),
\(\lfloor(e+t)/2\rfloor\le M\), so there is no additional
row-orbit term.

The literal factorization
\(C_s=\Lambda T\otimes B_s\), induced by
\(E_s=\mathbb Q\mathbf1\oplus W_s\), now gives by degree
induction
\[
[B_{N,D}]-[B_{M,D}]=[L_\nu].
\tag{OI.6}
\]
This difference describes the kernel of an actual surjection.
The orthogonal transpose \(q:W_N\to W_M\) of zero-padding
has
\[
q(P_Ne_i)=P_Me_i\quad(i\le M),\qquad q(P_Ne_N)=0.
\tag{OI.7}
\]
Each exterior row power sum maps to the corresponding row
power sum with scalar one. The complete finite-row orbit
spanning argument TM.8/TM.12 makes the induced map
\(B_N\to B_M\) surjective.
Complete reducibility therefore identifies (OI.6) as its
degree-\(D\) kernel character.
The next section determines every constituent in (OI.5)
by explicit polynomial maps.

## 2. Paired rows in the symmetric algebra of an exterior square

For every \(t\), the actual decomposition is
\[
\operatorname{Sym}^{d}(\Lambda^2T)=
 \bigoplus_{\substack{c_1\ge\cdots\ge c_r\ge0\\
                       c_1+\cdots+c_r=d}}
 S_{(c_1,c_1,\ldots,c_r,c_r,0^{\,t-2r})}T,
 \qquad r=\lfloor t/2\rfloor .
\tag{OI.8}
\]
Here is a full proof retaining its highest-polynomial maps.

Let \(A=(X_{ij})\) be the generic alternating matrix,
with \(X_{ji}=-X_{ij}\), and identify its polynomial algebra
with \(\operatorname{Sym}(\Lambda^2T)\).
For \(1\le i\le r\), let \(P_i\) be the Pfaffian of its
first \(2i\) rows and columns:
\[
P_i=\frac1{2^i i!}
 \sum_{\sigma\in S_{2i}}\operatorname{sgn}(\sigma)
       \prod_{k=1}^i X_{\sigma(2k-1),\sigma(2k)}.
\tag{OI.9}
\]
This convention makes \(P_i=z_1\cdots z_i\) on the block
diagonal matrix with blocks
\(\left(\begin{smallmatrix}0&z_k\\-z_k&0\end{smallmatrix}\right)\).
Under an upper unipotent matrix \(u\), the action on the
polynomial entries is \(A\mapsto u^t A u\).
The first \(2i\) columns are preserved with determinant one,
so \(P_i\) is invariant under this action.
Its diagonal weight is \((1^{2i},0^{t-2i})\).
Consequently
\[
P_1^{c_1-c_2}P_2^{c_2-c_3}\cdots
 P_{r-1}^{c_{r-1}-c_r}P_r^{c_r}
\tag{OI.10}
\]
is a nonzero highest polynomial of the paired weight in
(OI.8), of symmetric degree \(\sum c_i\).
This gives every displayed Schur summand by its explicit
highest vector and the rational Young projection.

We prove that these are all highest vectors and that each
occurs once. The open set \(P_1\cdots P_r\ne0\) is nonempty.
On it, upper unipotent congruence reduces \(A\) to the
displayed block diagonal form. The elimination is explicit.
Write the first block as
\[
A=\begin{pmatrix}J&B\\-B^t&C\end{pmatrix},\qquad
J=\begin{pmatrix}0&z\\-z&0\end{pmatrix}.
\]
For
\[
u=\begin{pmatrix}I_2&-J^{-1}B\\0&I_{t-2}\end{pmatrix}
\]
one has
\[
u^tAu=\operatorname{diag}(J,C+B^tJ^{-1}B).
\tag{OI.11}
\]
The second block is alternating. Repetition gives the
successive parameters \(z_i=P_i/P_{i-1}\), with \(P_0=1\).
For odd \(t\), the final one-by-one block is zero.
All denominators are nonzero on this specified chart.

Every highest polynomial is invariant under the upper
unipotent group. Its restriction to these diagonal blocks
therefore determines it on a dense open set.
A diagonal-weight vector can restrict nontrivially only
as a scalar multiple of a single monomial
\(z_1^{c_1}\cdots z_r^{c_r}\).
Its weight has paired entries \(c_i,c_i\) and, for odd
\(t\), final entry zero. These are nonnegative integers;
dominance of its polynomial highest weight gives
\(c_1\ge\cdots\ge c_r\).
The polynomial (OI.10) has exactly that restriction.
Their difference vanishes on the dense chart, hence
identically. Thus every highest weight has precisely
one such highest vector. Complete reducibility of the
finite-degree polynomial representation proves (OI.8).
The displayed vectors and their cyclic Schur maps provide
the asserted actual decomposition.

## 3. Exclusion of the required factor and faithful evaluation

Let \(\gamma=\nu^t\), a partition with exactly \(t\)
positive parts. Formula (OI.8) gives the following precise
necessary and sufficient constituent condition for (OI.5):
\[
\begin{array}{ll}
t\ {\rm even}:&
 \gamma_1=\gamma_2,\ \gamma_3=\gamma_4,\ldots,
 \gamma_{t-1}=\gamma_t,\\[2pt]
t\ {\rm odd}:&
 \gamma_1=\gamma_2,\ldots,\gamma_{t-2}=\gamma_{t-1},
 \qquad\gamma_t=1 .
\end{array}
\tag{OI.12}
\]
All size conditions are already enforced by (OI.5).

For each \(i<t\), \(\gamma_i-\gamma_{i+1}\) is the
multiplicity of the part \(i\) in \(\nu\); \(\gamma_t\)
is the multiplicity of its largest part \(t\).
At even \(t\), (OI.12) requires every odd-part
multiplicity to be zero.
At odd \(t\), it requires exactly one odd part, equal to
the largest part \(t\).
The two explicit families in the theorem therefore have
zero \(S_\gamma T\)-multiplicity in the actual kernel
(OI.6).

The skew-Cauchy Young maps identify this multiplicity map
with
\[
S_\nu(q):(S_\nu W_N)^{S_N}
                 \longrightarrow(S_\nu W_M)^{S_M}.
\tag{OI.13}
\]
It is onto and has zero kernel, so is an isomorphism.
R-046 supplies the same isomorphism for every larger row
count. On the ordinary Cauchy decomposition, the map is
again \(S_\nu(q)\): the identical tensor Young projectors
commute with \(q^{\otimes D}\).
Hence the specified ordinary centered power-sum evaluation
\[
p_s:\operatorname{Sym}(\bigoplus_{d\ge2}\operatorname{Sym}^dU)
 \longrightarrow
 (\operatorname{Sym}(W_s\otimes U))^{S_s}
\tag{OI.14}
\]
is an isomorphism on its \(S_\nu U\)-component for all
\(s\ge M\).
To verify faithfulness directly, take \(S\ge\max(s,D)\),
where TM.6 is an isomorphism by the equality-partition
triangular basis; (OI.7) gives \(p_s=S_\nu(q)p_S\)
on the exact component.

The asserted families satisfy \(D\ge t+2\).
At even width there are at least two odd parts besides
the largest even part.
At odd width there are at least two other odd parts
in addition to one largest odd part.
Consequently
\[
M=(D+t)/2-1\ge t.
\tag{OI.15}
\]
This checks every denominator and every row-degree
extension used next.

## 4. Exact canonical factorization and the full rank conclusion

For a highest vector with tail \(\nu\), the actual chart
TM.4 writes it as
\[
F=(\prod_{i=1}^a x_i)^n
                   f(y_1/x_1,\ldots,y_a/x_a).
\]
Its common-translation-invariant row polynomial \(f\)
belongs to the invariant part of \(S_\nu W_a\).
Each row degree is at most \(t\), by the column
antisymmetrizer. Thus all invariants homogenize in
inner degree \(n\ge M\ge t\).

The opposite normalized canonical map has the exact
dehomogenized formula
\[
h_{a,n}|_\nu=p_n\,\Psi_n\,E_a .
\tag{OI.16}
\]
Here \(E_a(f)(L)=L^{\otimes a}f\) is the injective
independent-row polarization, restricted to
\(L(1)=1,L(U)=0\). The normalization/recentering proof
of its injectivity is TM.14.
The middle map sends every degree-\(d\) moment to
\[
\frac1{(n)_d}
 \sum_{\substack{\pi\in\Pi([d])\\|B|\ge2}}
 \prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!\,p_{|B|},
 \qquad2\le d\le t.
\tag{OI.17}
\]
Each block retains its labeled tensor positions.
This is TM.16's distinct-factor coefficient with the
exact repeated-index factorials. Its one-block coefficient
is \((-1)^{d-1}(d-1)!/(n)_d\ne0\); the other terms use
strictly lower-degree generators. It is therefore the
explicit invertible triangular algebra morphism \(\Psi_n\).
Finally \(p_n\) is faithful on the required component
by (OI.14).

Every factor of (OI.16) is injective there, so \(h_{a,n}\)
is injective on the complete highest multiplicity space
and hence the whole isotypic component.
The scalar-one transpose pairing SR.5–SR.6 identifies
this rank with that of \(h_{n,a}\), proving (OI.2).
With both \(a,n\ge M\), apply the same argument in both
directions; this proves the actual isomorphism and (OI.3).

## 5. An explicit positive varying-width family

For every
\[
\boxed{a\ge5,\qquad w=4\ {\rm or}\ w\ge6,\qquad n\ge w+1,}
\tag{OI.18}
\]
the partition
\[
\lambda=(an-w-4,w,3,1)
\]
has
\[
\boxed{\operatorname{mult}_\lambda\operatorname{im}h_{n,a}
       =a_{a,n}^{\lambda}\ge1}
\tag{OI.19}
\]
in every dimension at least four.

Here is an explicit nonzero highest vector proving the
last inequality. In centered three-dimensional rows
\(z_i=w_i-\bar w\), take the polynomial
\(F_{a,3}\) of R-040 HC.7–HC.8:
\[
S=\sum_i z_i z_i^t,\quad C_{pqr}=\sum_i z_{ip}z_{iq}z_{ir},
\quad
A_{ij,kl}=\det(S)((S^{-1})_{ik}(S^{-1})_{jl}
                        -(S^{-1})_{il}(S^{-1})_{jk}),
\]
\[
F_{a,3}=\sum_{i,j,k}
 (C_{11i}C_{2jk}-C_{12i}C_{1jk})A_{ij,k3}.
\tag{OI.20}
\]
The \(A\)'s are signed complementary minors, so this is
polynomial even at singular \(S\). The complete
HC.7–HC.14 calculation proves its highest weight
\((4,3,1)\), its translation and slot invariance, and
its nonzero value for every \(a\ge5\).
Put \(P_d=\sum_i z_{i1}^{\,d}\).
Both \(P_2\) and \(P_3\) are nonzero invariant highest
polynomials of weight \((2)\) and \((3)\), respectively.
For even \(w\ge4\) use
\[
F_{a,3}P_2^{(w-4)/2};
\]
for odd \(w\ge7\) use
\[
F_{a,3}P_3P_2^{(w-7)/2}.
\tag{OI.21}
\]
The raising operators are derivations, so these
products are highest of weight \((w,3,1)\).
The centered row polynomial algebra is an integral
domain, so they are nonzero.
Their row degrees are at most \(w\), either from their
column realization or directly from the factors.
Formula TM.4 homogenizes them in every \(n\ge w+1\).

For even \(w\), the tail has two odd parts; for odd
\(w\), it has three. In both cases
\(D=w+4\), \(t=w\), and \(M=w+1\), so (OI.2) applies.
The first-row inequality is explicit:
\(an-w-4\ge5(w+1)-w-4=4w+1\ge w\).
Thus every displayed parameter is a valid partition
and every nonvanishing statement is literal.

## 6. Transport and independent verification

All exterior restrictions, congruences, Young maps,
rational averages, and split-moment inverses have been
specified over \(\mathbb Q\). They extend to any
characteristic-zero field. Naturality gives the same
multiplicity map in every finite dimension supporting
\(S_\lambda V\).

The exact graded geometric map is the Chow pullback
R-037 EP.3–EP.5, with scalar-one homogeneous piece EP.4.
Its frame-torsor associated map and the representation
\(K_0\) dictionary are exactly those recorded in R-036 §5:
SGA 6 VI Theorem 3.3; SGA 6 V Proposition 4.2,
Definition 4.4, Proposition 4.8 and Corollary 4.9;
SGA 3 I §4.5 and Propositions 4.7.2–4.7.3;
EGA II 2.4.1–2.4.2 and 2.5.2/2.5.4.

The independent script verify_one_row_improved_stability.py
checks every tail of degree at most twelve satisfying
the stated parity and odd-part conditions, including five
auxiliary width-one zero cases outside the theorem's \(t\ge2\)
range.
It averages the literal Schur character on the permutation
standard representation at row count \(M\), and separately
expands the complete formal moment algebra by original
cycle-index/Murnaghan–Nakayama characters.
All **96** exact comparisons pass: **91** lie in the stated
width range and five are the auxiliary zero cases.
All **22** positive multiplicities lie in the stated range.
The receipt is
ONE_ROW_IMPROVED_STABILITY_CHECK.tsv.
This check concerns the faithful-evaluation dimensions;
the actual rank assertion is proved by (OI.7),
(OI.13), and (OI.16), with their full normalizations.


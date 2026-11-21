# The complete single-four tail band of the canonical map

## R-044. Full multiplicities for \(\lambda_2\le4,\lambda_3\le3\)

Let \(n\ge a\ge2\), let \(\lambda\vdash an\), and pad its
parts by zeros. Over every field of characteristic zero, the
actual normalized canonical map
\[
h_{n,a}:\operatorname{Sym}^n(\operatorname{Sym}^aV)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^nV)
\]
is surjective on its entire \(\lambda\)-isotypic component whenever
\[
\boxed{\lambda_2\le4,\qquad\lambda_3\le3.}
\tag{SF.1}
\]
This includes every multiplicity in that component.
The assertion is literal for \(\dim V\ge\ell(\lambda)\);
for smaller dimension the component is zero on both sides,
by the column antisymmetrizer defining \(S_\lambda V\).

Here and below the normalized map is the rational tensor
grid permutation followed by the two block symmetrizers.
Its transpose is \(h_{a,n}\) under the exact pure-power
pairings SR.5–SR.6. Every map used in the proof is this map.

The proof joins the previously established moment blocks by
an actual invariant-algebra surjection that exhausts their
support. No historical novelty claim is made. The binary
subcase is the known actual Hermite map, with primary locator
Landsberg, arXiv:1305.7387v3, Theorem 7.21, §7.7, printed p.24;
§7.2 and Proposition 7.6 specify the same regrouping map and
transpose pairing. The explicit fourth-moment matrix R-038
refines that known binary rank statement.

## 1. Exact reduction to the four tail families

The case \(\lambda_2\le3\) is the full statement R-036 CT.1–CT.20,
with the quadratic family supplied by R-035. It remains to
treat \(\lambda_2=4,\lambda_3\le3\). Its tail has the form
\[
\nu=(4,3^p,2^q,1^s),\qquad p,q,s\ge0.
\tag{SF.2}
\]
Let \(E=\mathbb Q^a\), \(W=\mathfrak h_a\), and \(P:E\to W\)
be the sum-zero orthogonal projection.

There is an injective map from the highest space of weight
\((an-|\nu|,\nu)\) to \((S_\nu W)^{S_a}\).
Here is its actual coordinate construction. Write the \(a\)
vector slots as \((x_i,y_i)\), set \(u=\prod_i x_i\), and
dehomogenize a highest polynomial \(F\) by
\[
F(x_i,y_i)=u^n\,f(y_i/x_i).
\tag{SF.3}
\]
On this dense chart the highest equations in the first
coordinate say exactly that \(f\) is invariant under a
common translation of the rows. Hence \(f\) factors through
the linear map \((w_i)\mapsto(w_i-\bar w)\in W\otimes V'\).
The remaining highest equations and torus weight select
the rational Young-projector summand \(S_\nu W\); slot
symmetry selects its \(S_a\)-fixed space. Equality on the
dense chart proves injectivity. Conversely a vector in this
fixed space whose separate row degrees are at most \(n\)
homogenizes by (SF.3) to a polynomial highest vector.
These are the explicit maps used in CT.4 and QE.8–QE.9;
no equality of abstract dimensions is substituted for them.

For \(T=\mathbb Q^4\), the row power sums give the surjective
\(GL(T)\)-equivariant algebra morphism
\[
\mathcal A:=
\operatorname{Sym}(\Lambda^2T\oplus\Lambda^4T)
\otimes\Lambda(\Lambda^3T)
\twoheadrightarrow
\bigl(\Lambda(W\otimes T)\bigr)^{S_a}.
\tag{SF.4}
\]
The degree-\(d\) map sends \(t_1\wedge\cdots\wedge t_d\) to
\(\sum_i(Pe_i\otimes t_1)\wedge\cdots\wedge(Pe_i\otimes t_d)\).
HO.3 proves surjectivity by expanding injective row assignments
in power sums and descending on their equality partitions;
equal odd row types have zero invariant average, and every
remaining stabilizer contributes its explicit nonzero factorial.
Projection \(E\to W\) kills the singleton power sums. Thus
(SF.4) is a finite-row map for every \(a\), including the
small row counts.

The actual skew-Cauchy Young decomposition identifies the
\(S_{\nu^t}T\)-multiplicity of the target of (SF.4) with
\((S_\nu W)^{S_a}\), and
\[
\gamma:=\nu^t=(1+p+q+s,\ 1+p+q,\ 1+p,\ 1).
\tag{SF.5}
\]
The symmetric exterior-square algebra has the proved
Pfaffian/standard-minor decomposition
\[
\operatorname{Sym}(\Lambda^2T)
=\bigoplus_{P\ge Q\ge0}S_{(P,P,Q,Q)}T,
\tag{SF.6}
\]
with each summand once. This is HO.5, retaining its explicit
highest-minor maps and determinant character.

The exterior factors are, by complementary-column contraction,
\[
\begin{array}{c|c}
e&\Lambda^e(\Lambda^3T)\\ \hline
0&\mathbb Q\\
1&\Lambda^3T\\
2&(\det T)\otimes\Lambda^2T\\
3&(\det T)^2\otimes T\\
4&(\det T)^3 .
\end{array}
\tag{SF.7}
\]
Because \(\gamma_4=1\), the last two rows of (SF.7) cannot
occur: their factors already contain at least two determinant
columns, and tensoring a polynomial Schur module cannot
remove a column. This last assertion follows directly by
writing \((\det T)^2\otimes S_\eta T=S_{\eta+(2^4)}T\).

We now enumerate the first three rows, with every allowed
Pieri map a column antisymmetrizer followed by the rational
Young projector.

For \(e=0\), equality of the first two and last two parts in
(SF.6), even after a determinant shift, forces \(s=p=0\).
This gives \((4,2^q)\).

For \(e=1\), put the paired shape after the determinant
shift equal to \((P,P,Q,Q)\). A vertical three-strip adds
indicators \(\epsilon_i\in\{0,1\}\), with
\(\sum\epsilon_i=3\). The fourth part gives
\(Q+\epsilon_4=1\).
If \(Q=0,\epsilon_4=1\), partition order forces
\(\epsilon_3=1\), and the remaining indicator is
\(\epsilon_1=1,\epsilon_2=0\). Thus \(p=0,s=1\).
If \(Q=1,\epsilon_4=0\), the other three indicators are all
one. Thus \(p=1,s=0\). These give respectively
\((4,2^q,1)\) and \((4,3,2^q)\).

For \(e=2\), the determinant in (SF.7) and \(\gamma_4=1\)
force the additional determinant exponent and the bottom
paired part to be zero, and the fourth indicator to be
zero. The vertical two-strip either uses rows \(1,2\),
giving \(p=s=0\), or rows \(1,3\), giving \(p=s=1\).
These give \((4,2^q)\), with \(q\ge1\), and
\((4,3,2^q,1)\).

Consequently (SF.4)–(SF.7), followed by the injective map
(SF.3), prove
\[
\boxed{
a_{a,n}^{(an-|\nu|,\nu)}=0
\quad\text{for every single-four tail outside }
\begin{cases}
(4,2^q),\\
(4,3,2^q),\\
(4,2^q,1),\\
(4,3,2^q,1).
\end{cases}}
\tag{SF.8}
\]
This is a proved vanishing statement for all finite \(a,n\)
and all valid partitions. It does not presuppose stable
row counts or a polynomial-extension assertion.

## 2. Exact multiplicity table in the ordered range

For \(n\ge a\ge2\) and \(n\ge4\), the complete target table
for the four tails is
\[
\begin{array}{c|c|c}
\nu&\text{parameter}&a_{a,n}^{(an-|\nu|,\nu)}\\ \hline
(4)&q=0&1+\mathbf1_{a\ge4}\\
(4,2^q)&q\ge1&\min(3,\max(0,a-q-1))\\
(4,3,2^q)&q\ge0&\min(2,\max(0,a-q-3))\\
(4,2^q,1)&q\ge0&\mathbf1_{a\ge q+3}\\
(4,3,2^q,1)&q\ge0&\mathbf1_{a\ge q+5}.
\end{array}
\tag{SF.9}
\]
Rows are retained only when the displayed weight is a
partition. Lengths exceeding \(a\) give zero, also directly
from the tensor-slot Young projection.

The first row is R-038 FM.1–FM.17: at row counts two and
three the two quartics have one relation; at row counts at
least four they are independent. Both extend for \(n\ge4\).
Its actual map is the binary canonical isomorphism.

The second row is R-041 with \(m=q+1\). Its three explicit
Gram/weighted-minor polynomials span the invariant space,
have row degree at most four, and have finite dimension
\(r_a=\min(3,\max(0,a-m))\). The exact canonical rank is
\(\min(r_a,r_n)\), by QE.16–QE.20.
For \(n\ge a\) this equals \(r_a\).
The proof includes the one- and two-dimensional endpoints,
rather than applying the three-dimensional determinant
where it vanishes.

The third row is R-043 with \(m=q+2\). Its two explicit
polynomials have row degree at most four and dimension
\(s_a=\min(2,\max(0,a-m-1))\). Equations ME.10 and ME.15
give the full matrix
\[
c_{a,n,m}\mathcal E_{a,m}\mathcal H_{n,m},
\quad
\det\mathcal E_{a,m}
=\frac{(a-m-1)^2(a-m-2)}{a^4},
\quad
\det\mathcal H_{n,m}
=-\frac{6n(n-1)}{(n-2)(n-3)}.
\tag{SF.10}
\]
Its one-dimensional square has the nonzero scalar in
ME.18, and its mixed endpoints are proved by actual
restriction to the finite span. Thus its rank is
\(\min(s_a,s_n)=s_a\) for \(n\ge a\).
The column-coordinate inverse in ME.17 gives a rational
preimage of every vector in the full two-dimensional target.

For the fourth row, R-039 applies with \(m=q+2\).
Its polynomial \(A_{a,m}\) has row degree at most three,
and the normalized map has the exact identity
\[
h_{a,n}\widehat A_{a,n,m}
=
\frac{2(-1)^{m-1}(a)_{m+1}}
{n^{m+1}(n-1)^m(n-2)}
\,\widehat A_{n,a,m}.
\tag{SF.11}
\]
The nonzero range is \(a,n\ge m+1\), and all smaller
finite-row invariant spaces vanish. In the ordered range,
the target is reached whenever it exists.

For the fifth row, R-040 applies with \(m=q+3\).
Its polynomial \(D_{a,m}\) also has row degree at most
three, and the normalized identity is
\[
h_{a,n}\widehat D_{a,n,m}
=
\frac{4(-1)^{m-2}(a)_{m+2}}
{n^{m+2}(n-1)^m(n-2)^2}
\,\widehat D_{n,a,m}.
\tag{SF.12}
\]
The nonzero range is \(a,n\ge m+2\). The intervening
row count \(a=m+1\) vanishes by the explicit complementary
column pairing in HC.3–HC.4. Again \(n\ge a\) reaches
every nonzero target line.

For (SF.11)–(SF.12), exchanging \(a,n\) and taking the
displayed scalar reciprocal gives an actual preimage under
\(h_{n,a}\), with precisely the same highest polynomial.
For the larger blocks the inverse matrices and their
finite-span restrictions provide the preimages. Equivariance
then gives every vector in the corresponding Schur component:
a highest vector generates its irreducible Schur summand,
and the displayed highest-space maps have full multiplicity
rank. Complete reducibility separates the different copies.

## 3. All small ordered endpoints

For \(n=2\) with \(2\le a\le n\), the total degree is four,
so no partition has second part four. For \(n=3\), only
\(a=3\) can yield such a partition. There are exactly two:
\[
(5,4),\qquad(4,4,1).
\tag{SF.13}
\]
The first has target multiplicity zero: the binary weight
difference counts three partitions of four inside the
three-by-three rectangle and three partitions of three,
giving \(3-3=0\). Equivalently this is the exact quartic
extension relation in FM.5–FM.8.
The second is (SF.11) with \(a=n=3,m=2\); its scalar is
\[
\frac{2(-1)(3)_3}{3^3\,2^2\,1}=-\frac19\ne0.
\tag{SF.14}
\]
Thus it is reached in its entire one-dimensional highest
space. These are all remaining endpoints.

Equations (SF.8)–(SF.14), joined with R-036 for the
second-row-three band, prove (SF.1).

## 4. Polynomial-functor and geometric transport

Every generator, row-centering map, Young projector,
homogenization, grid symmetrizer and inverse used above
is defined over \(\mathbb Q\). The inverse scalars are
nonzero rational numbers in the asserted integer ranges.
Extension of scalars therefore preserves each statement.
The tensor maps are natural in \(V\); their Schur multiplicity
matrices are the displayed matrices in every rank
\(\dim V\ge\ell(\lambda)\).

For coordinate rings, the actual algebra morphism is the
graded Chow pullback in R-037 EP.3–EP.5, whose degree-\(n\)
piece is \(h_{n,a}\) with scalar one by EP.4.
For vector bundles it is the associated-bundle map formed
from these same rational \(GL(V)\)-morphisms on the frame
torsor. R-036 §5 records the exact SGA 6 VI Theorem 3.3,
SGA 6 V §4, SGA 3 I §4 and EGA II §§2.4–2.5 locators and
the representation-to-associated-bundle construction.
No equality in representation \(K_0\) is used to infer
surjectivity: the polynomial maps and inverses above supply it.

## 5. Independent finite verification

The script verify_single_four_tail_band.py enumerates every
single-four tail of length at most \(a-1\) and every valid
first part for \(2\le a\le n\le6\). It computes the target and
source coefficients by literal cycle-index expansion followed
by Murnaghan–Nakayama, without calling the invariant-algebra
decomposition or any canonical moment matrix.
Every target agrees with (SF.8)–(SF.9) and the small endpoint
(SF.13); every source dimension is at least that target
dimension. The receipt is SINGLE_FOUR_TAIL_BAND_MN_CHECK.tsv.
All 122 target coefficients and all 122 source coefficients pass.
This finite coefficient check does not replace the actual
canonical-map proof in §§2–3.


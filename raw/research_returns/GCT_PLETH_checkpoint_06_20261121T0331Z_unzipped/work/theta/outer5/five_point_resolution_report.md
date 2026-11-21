# The five projective-frame points: explicit equivariant resolution

## T-038. Statement and exact matrices

Work over \(\mathbf Q\). Let
\[
E=\mathfrak h_5=\{(q_1,\ldots,q_5):\sum q_i=0\},\qquad
\ell_i=e_i-\tfrac15\mathbf1,
\]
and let \(Z\subset\mathbf P(E)\) be the reduced set of the five lines
\([\ell_i]\). The action is literal coordinate permutation. In the basis
\(\ell_1,\ldots,\ell_4\), these lines are the four coordinate points and
\([1:1:1:1]\), since \(\ell_5=-\sum_{i=1}^4\ell_i\).
Put \(S=\mathbf Q[x,y,z,w]=\operatorname{Sym}(E^*)\). The saturated ideal is
\[
I=(f_1,\ldots,f_5),\quad
f=(xz-xy, xw-xy, yz-xy, yw-xy, zw-xy)^t.
\tag{5R.1}
\]
The following complex is an exact minimal graded free resolution:
\[
0\longrightarrow S(-5)\mathrel{\mathop{\longrightarrow}^{N}}
 S(-3)^5\mathrel{\mathop{\longrightarrow}^{M}}
 S(-2)^5\mathrel{\mathop{\longrightarrow}^{f^t}}I
\longrightarrow0,
\tag{5R.2}
\]
where
\[
M=\begin{pmatrix}
y-w&y&y&y-w&0\\
z-y&-y&-y&-y&-y\\
0&-x&-w&-x&-w\\
0&x&z&0&0\\
0&0&0&x&y
\end{pmatrix},\qquad
N=\begin{pmatrix}
y(x-w)\\z(y-w)\\x(w-y)\\y(w-z)\\x(z-w)
\end{pmatrix}.
\tag{5R.3}
\]
Let \(U=[3,2]\) and \(\epsilon=\operatorname{sgn}\). There are uniquely
specified actions on the spaces of minimal generators and minimal syzygies,
inherited from the action on \(I\). With these actions the resolution is
\[
\boxed{
0\longrightarrow\epsilon\otimes S(-5)
\longrightarrow(\epsilon\otimes U)\otimes S(-3)
\longrightarrow U\otimes S(-2)
\longrightarrow I\longrightarrow0.}
\tag{5R.4}
\]
In particular, sheafification and tensoring by any specified locally free
sheaf give an exact equivariant complex. These are concrete maps: (5R.3)
gives their matrices, and the finite group acts on each syzygy space by
applying its action to its polynomial vectors.

### Proof of the scheme and of exactness

G-016 proves the projective-frame ideal statement for every outer degree.
Here it also has the following short direct verification. In \(S/I\) every
cross-product is equal to \(p=xy\). For distinct indices \(i,j\), choose a
third index \(a\); then
\(z_i p=z_i(z_jz_a)=z_j(z_i z_a)=z_jp\). Hence in degree \(C\ge2\) every
mixed monomial equals \(p x^{C-2}\). The five elements
\[
x^C,y^C,z^C,w^C,px^{C-2}
\tag{5R.5}
\]
are independent by evaluation at the four coordinate points and
\([1:1:1:1]\). The same evaluation is injective in degrees zero and one.
Thus \(S/I\) embeds in the product of the coordinate rings of the five
lines, and its ideal is precisely their reduced union ideal. In particular
\(I\) is saturated and
\[
H_{S/I}(t)=1+4t+\frac{5t^2}{1-t}
=\frac{1+3t+t^2}{1-t}.
\tag{5R.6}
\]

Direct multiplication gives \(f^tM=0\) and \(MN=0\). The upper-left
\(4\times4\) minor of \(M\) is
\[
x(z-w)(xy-wz),
\tag{5R.7}
\]
which is nonzero. Thus the fraction-field kernel of \(M\) is the line
spanned by \(N\). The entries of \(N\) have greatest common divisor one:
already the irreducible factors of \(y(x-w)\) have no common factor with
\(z(y-w)\). If a fraction \(a/b\), in lowest terms, has
\((a/b)N\in S^5\), every irreducible divisor of \(b\) divides all the
entries of \(N\). Therefore \(b\) is a unit. This proves
\(\ker M=S N\), and the left map is injective.

Subtracting (5R.6) from \(H_S(t)=(1-t)^{-4}\) gives
\[
H_I(t)=\frac{5t^2-5t^3+t^5}{(1-t)^4}.
\tag{5R.8}
\]
It follows that \(\ker f^t\) has Hilbert series
\((5t^3-t^5)/(1-t)^4\). The established kernel of \(M\) gives exactly
that series for \(\operatorname{im}M\). Since the latter is contained in
\(\ker f^t\), their degree-by-degree dimensions prove equality. All
matrix entries have positive degree, so the resolution is minimal.

### The actual finite-group labels

The canonical affine representatives \(\ell_i\) are permuted without
rescaling. Consequently evaluation gives
\[
(S/I)_0=\mathbf1,\qquad(S/I)_1=E^*,\qquad
(S/I)_C=\operatorname{Perm}_5\quad(C\ge2)
\tag{5R.9}
\]
as actual \(S_5\)-modules. An invariant nondegenerate form identifies
\(E^*\) with \(E\). Write the conjugacy classes in the order
\[
1^5,\quad21^3,\quad2^21,\quad31^2,\quad32,\quad41,\quad5.
\tag{5R.10}
\]
The character of \(I_2=\operatorname{Sym}^2E-\operatorname{Perm}_5\) is
\[
(5,1,1,-1,1,-1,0),
\tag{5R.11}
\]
which is the irreducible character \([3,2]\). For example the character
can be computed directly from
\(\chi_{\operatorname{Sym}^2E}(g)=
(\chi_E(g)^2+\chi_E(g^2))/2\); the irreducible labels agree with the
primary character table in Dolgachev–Farb–Looijenga,
*Geometry of the Wiman–Edge pencil I*, §2.3, Table 1, printed p. 10.

The degree-three syzygy character is
\[
\chi_E\chi_U-\chi_{\operatorname{Sym}^3E}
 +\chi_{\operatorname{Perm}_5}
=(5,-1,1,-1,-1,1,0)=\chi_{[2,2,1]}.
\tag{5R.12}
\]
This follows either by the degree-three exact sequence, or by expanding
\(\prod_{\xi\in\operatorname{eig}(g|E)}(1-t\xi)^{-1}\) to degree three.
It fixes the action on the columns of \(M\).

There is one final generator. At a transposition \(s\), the equivariant
Hilbert series of \(S/I\) is \((1+t+t^2)/(1-t)\), whereas that of \(S\)
is \(((1-t)^3(1+t))^{-1}\). Their ratio is
\[
1-t^2-t^3+t^5.
\tag{5R.13}
\]
In the alternating numerator of (5R.2) the final coefficient is
\(-\chi_K(s)t^5\). Thus \(\chi_K(s)=-1\). Every one-dimensional
representation of \(S_5\) is determined by its common value on the
transpositions, which generate the group, so \(K=\epsilon\). This proves
(5R.4), including its final determinant character.

For an alternating form of the middle map, set
\[
P=\begin{pmatrix}
0&0&0&-1&0\\0&0&1&0&-1\\0&1&0&0&0\\
0&0&-1&1&0\\1&-1&0&0&0
\end{pmatrix}.
\]
Then \(\det P=-1\), \(N=Pf\), and
\[
MP=\begin{pmatrix}
0&y&w&0&-y\\-y&0&0&-z&y\\-w&0&0&-x&x\\
0&z&x&0&-x\\y&-y&-x&x&0
\end{pmatrix}.
\tag{5R.14}
\]
Its signed maximal Pfaffians are \(f\). Thus the five-point ideal also
comes with a specified alternating presentation, as used in the separate
application of Kustin–Polini–Ulrich in the archive report. The elementary
exactness proof above does not need an unverified generic perfection claim.

## The quadratic subalgebra and its six-coordinate morphism

This subsection records an exact comparison useful for the higher powers.
Let \(A,B,C,D,E_0\) be independent indeterminates mapping to the five
entries of \(f\), in that order. Then
\[
\boxed{\mathbf Q[f_1,\ldots,f_5]
\simeq\mathbf Q[A,B,C,D,E_0]/(F),\qquad
F=AD(E_0-B-C)-BC(E_0-A-D).}
\tag{5R.15}
\]
The variable \(E_0\) is distinguished from the standard module \(E\).
Substitution verifies \(F(f)=0\). In the fraction field of the image,
\[
xy=\frac{AD}{E_0-A-D},\qquad
xz=xy+A,\quad xw=xy+B,\quad yz=xy+C,
\tag{5R.16}
\]
and similarly for the other cross-products. In particular
\(x^2=(xy)(xz)/(yz)\). The full rational function field
\(\mathbf Q(x,y,z,w)\) is algebraic over the image's fraction field:
adjoin a square root \(x\) of this displayed \(x^2\), then recover
\(y,z,w\) by division. The image has transcendence degree four.

As a polynomial in \(E_0\), \(F\) has coefficient \(AD-BC\), an
irreducible determinant. This coefficient does not divide the constant
term: at \((A,B,C,D)=(1,2,3,6)\) the coefficient is zero and the constant
term is nonzero. The coefficient and constant term are therefore coprime.
Gauss's lemma and the degree-one polynomial over \(\mathbf Q(A,B,C,D)\)
prove that \(F\) is irreducible. The kernel has height one and contains
\(F\); since the target is a domain this proves (5R.15). The transposition
\(x\leftrightarrow y\) sends
\((A,B,C,D,E_0)\) to \((C,D,A,B,E_0)\) and sends \(F\) to \(-F\).
Its relation line is therefore \(\epsilon\).

Here is a rational linear comparison with the usual six-coordinate
Segre cubic. Set
\[
\begin{aligned}
t_1&= A+B-C+D-E_0,&t_2&=-A+B+C-D-E_0,\\
t_3&=-A+B+C-D+E_0,&t_4&=-A-B-C+D+E_0,\\
t_5&= A-B-C-D+E_0,&t_6&= A-B+C+D-E_0.
\end{aligned}
\tag{5R.17}
\]
These forms have rank five and satisfy
\[
\sum_{i=1}^6t_i=0,\qquad\sum_{i=1}^6t_i^3=-24F.
\tag{5R.18}
\]
For precision, the associated action on six letters is the conjugation
action of \(S_5\) on its six subgroups of order five. Index those subgroups
by lexicographically ordering their permutation tuples, as in the
certificate script. The six forms in (5R.17) obey
\[
g(t_i)=\epsilon(g)t_{g(i)}.
\tag{5R.19}
\]
There is also a group-theoretic way to specify these exact forms without
guessing an outer automorphism. If \(H_0\) is the first such subgroup,
average \(\epsilon(g)\rho_U(g)\) over its twenty-element normalizer.
Its image is a line. Take the first nonzero column, clear denominators
and divide by the positive gcd of its integer entries. For a subgroup
\(gH_0g^{-1}\), transport this vector by \(\epsilon(g)\rho_U(g)\).
This is independent of the chosen transporter because of the normalizer
character. It gives precisely (5R.17). Multiplication by every one of the
120 group elements was checked against (5R.19).

The conjugacy-class map, in the order (5R.10), is
\[
1^6,\quad2^3,\quad2^21^2,\quad3^2,\quad6,\quad41^2,\quad51.
\tag{5R.20}
\]
Equations (5R.17)–(5R.20) specify both the cubic isomorphism and the
finite-group intertwiner. This agrees with the classical five-point
quadratic map: Dolgachev–Farb–Looijenga, Remark 2.4, printed p. 13,
describes the five-point map and its Segre cubic image; Dolgachev,
*Corrado Segre and nodal cubic threefolds*, §2, equation (2.1), gives the
six-coordinate equations. We do not attach a novelty claim to this
classical comparison.

## Sources and checks

- [Dolgachev–Farb–Looijenga, *Geometry of the Wiman–Edge pencil I*](https://www.math.uchicago.edu/~farb/papers/wiman.pdf),
  §2.3, Table 1, printed p. 10, and Remark 2.4, printed p. 13. Both
  passages were opened and read in this run.
- [Dolgachev, *Corrado Segre and nodal cubic threefolds*](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/segre15.pdf),
  §2, especially equation (2.1) and the five-point quadratic map.
- `check_five_points.py` verifies the two zero matrix products, the
  primitive kernel, the nonzero minor, cubic substitution, six-form rank,
  all 120 group intertwining identities and the class map. The full
  receipt is `FIVE_POINT_EXACT_MAPS.txt`.
- `check_five_point_positive.py` additionally checks the entire
  equivariant Hilbert numerator on all seven classes. The matrices and
  the degree-by-degree exactness proof specify the complex independently
  of those finite checks.

The next result, T-039, evaluates a family of quotient-bundle sections
from this actual resolution. General arbitrary powers with arbitrary
Schur quotient bundles remain a separate direct-evaluation task; G-010
already supplies a terminating finite positive count for all plethysm
coefficients.

The rectangular agent independently read the complete proof and checked
the actual \(M,N,P\) products, signed Pfaffians, scalar \(-24\), and all
120 signed actions using the five affine frame vectors. Every check
passed. Its independent code and receipt are
`work/rectangular/verify_five_point_matrices.py` and
`work/rectangular/FIVE_POINT_MATRIX_INDEPENDENT_CHECK.txt`.

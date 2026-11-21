# Actual canonical isomorphisms on every hook tail

## R-050. Complete hook-tail rank law

Let \(a,n\ge1\), \(t\ge1\), \(r\ge0\), and require
\[
\lambda=(an-t-r,t,1^r)
\tag{HM.1}
\]
to be a partition. Over every characteristic-zero field, the actual
normalized Foulkes–Howe maps in both directions are isomorphisms on
their complete \(\lambda\)-isotypic components:
\[
\boxed{\begin{gathered}
h_{a,n}:\operatorname{Sym}^{a}(\operatorname{Sym}^{n}V)
\longrightarrow\operatorname{Sym}^{n}(\operatorname{Sym}^{a}V),\\
\operatorname{mult}_{\lambda}\operatorname{im}h_{a,n}
=a_{a,n}^{\lambda}=a_{n,a}^{\lambda}
=\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}.
\end{gathered}}
\tag{HM.2}
\]
Every multiplicity is zero below dimension \(r+2\).
The proof uses the actual subspace of highest polynomials with
separate row degree at most \(n\); it does not impose \(n\ge t\).

The known ingredients are identified precisely. The hook-specialization
identity is Langley–Remmel, *The plethysm \(s_\lambda[s_\mu]\) at hook
and near-hook shapes*, Theorem 3.1 and its complete proof, printed
pp.6–8 (2004), DOI https://doi.org/10.37236/1764. Its primary PDF is
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r11/pdf.
The invariant-form input is Solomon, *Invariants of finite reflection
groups*, §3, unnumbered Theorem p.59, proof pp.59–61, and formula (4)+p.62 (1963), DOI https://doi.org/10.1017/S0027763000011028.
Its primary PDF is
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/160748DDB7C9D17C5379F6FF65BB5B98/S0027763000011028a.pdf/invariants-of-finite-reflection-groups.pdf.
The precise special cases and all comparison maps used here are proved
below. The two-row case \(r=0\) has the known canonical Hermite
interpretation already located in R-038's opening. No historical
priority claim is made for any coefficient identity or rank statement.
The present result is the explicitly proved canonical-map form (HM.2).

## 1. A finite power-sum morphism generated in degrees at most the row count

For \(s\ge1\), put
\[
W_s=\{(x_1,\ldots,x_s):\sum_i x_i=0\},\qquad
P_s e_i=e_i-s^{-1}\sum_j e_j,
\]
and, for an auxiliary space \(U\), define
\[
\mathcal M_{\le s}(U)=
\operatorname{Sym}\!\left(\bigoplus_{d=2}^{s}\operatorname{Sym}^dU\right).
\]
The empty sum at \(s=1\) gives \(\mathbb Q\).
The degree of a generator in \(\operatorname{Sym}^dU\) is \(d\).
Define the actual graded algebra morphism
\[
\begin{split}
\mathsf p_s:\mathcal M_{\le s}(U)&\longrightarrow
\bigl(\operatorname{Sym}(W_s\otimes U)\bigr)^{S_s},\\
u_1\cdots u_d&\longmapsto
\sum_{i=1}^s(P_s e_i\otimes u_1)\cdots(P_s e_i\otimes u_d).
\end{split}
\tag{HM.3}
\]
The scalar on each polarized generator is one.

This map is surjective in every degree. To see the finite bound on
generators directly, first work with \(s\) uncentered vector rows.
The equality-partition expansion of a product of power sums expresses
every row-orbit sum in polarized power sums of unrestricted degrees:
its distinct-row term is the desired orbit sum times the nonzero
factorial for repeated row types; every other term has fewer occupied
rows. Induction on that number proves generation.

For a formal covector \(\ell\), let \(y_i=\ell(w_i)\). Write
\(q_d(\ell)=\sum_i y_i^d\) and let \(e_j(\ell)\) be the elementary
symmetric polynomials in these \(s\) quantities. The explicit Newton
recursion is
\[
j e_j=\sum_{i=1}^{j}(-1)^{i-1}e_{j-i}q_i,
\qquad e_0=1\quad(1\le j\le s).
\tag{HM.4}
\]
The polynomial \(\prod_i(X-y_i)\) gives, for \(d>s\),
\[
q_d=e_1q_{d-1}-e_2q_{d-2}+\cdots+(-1)^{s-1}e_s q_{d-s}.
\tag{HM.5}
\]
Thus each \(q_d(\ell)\) is a specified polynomial in
\(q_1(\ell),\ldots,q_s(\ell)\). Taking every coefficient in the
coordinates of \(\ell\) proves that all polarized power sums are
generated in degrees at most \(s\). The actual projection to \(W_s\)
kills degree one and sends the remaining generators to (HM.3).
Rational averaging, or the literal fixed-line splitting, proves
surjectivity after this projection. This establishes the asserted
finite-degree generating map without an unspecified change of algebra.

## 2. Hook multiplicities in the source of (HM.3)

Fix a nonzero moment multidegree
\(\beta=(\beta_2,\ldots,\beta_s)\), and put
\[
D=\sum_{d=2}^{s}d\beta_d,\qquad
J=\{d:\beta_d>0\},\qquad k=|J|.
\]
The corresponding actual tensor factor is
\(\bigotimes_d\operatorname{Sym}^{\beta_d}(\operatorname{Sym}^dU)\),
with character \(\prod_d h_{\beta_d}[h_d]\).
The specialization \(1-z\) is the ring homomorphism specified on power
sums by \(p_j\mapsto1-z^j\). In particular the minus sign has its
virtual-alphabet meaning, with this displayed value for every \(j\).

The generating function
\[
\sum_{d\ge0}h_d[1-z]v^d=\frac{1-zv}{1-v}
\]
gives \(h_d[1-z]=1-z\) for \(d\ge1\). Adams substitution commutes
with this identity: explicitly,
\(p_j[h_d][1-z]=h_d[1-z^j]=1-z^j\).
Consequently, for every \(b,d\ge1\),
\[
h_b[h_d][1-z]=1-z.
\tag{HM.6}
\]
The skew-Schur coproduct, obtained by splitting the alphabet in the
Young-tableau construction, gives
\(s_\eta[X-Y]=\sum_{\rho\subseteq\eta}
s_\rho[X](-1)^{|\eta/\rho|}s_{(\eta/\rho)'}[Y]\).
At \(X=1,Y=z\), a nonzero term requires \(\rho\) to be a row and
\(\eta/\rho\) to be a vertical strip. These are exactly the hook shapes.
For the hook \(\eta=(D-r,1^r)\), the two possible rows have lengths
\(D-r\) and \(D-r-1\), including the empty row at its endpoint. Hence
\[
s_\eta[1-z]=
\begin{cases}(-z)^r(1-z),&\eta=(D-r,1^r),\\0,&\eta\text{ is not a hook}.
\end{cases}
\tag{HM.7}
\]
Equations (HM.6)–(HM.7), in this fixed degree \(D\), compare
\((1-z)^k\) with \((1-z)\sum_r m_r(-z)^r\). They prove the exact
nonnegative multiplicity
\[
\boxed{
[S_{(D-r,1^r)}U:
 \bigotimes_d\operatorname{Sym}^{\beta_d}(\operatorname{Sym}^dU)]
=\binom{k-1}{r}.}
\tag{HM.8}
\]
The value is zero for \(r>k-1\). This derives the needed special case
of the cited hook theorem and specifies the character substitution.

## 3. Hook multiplicities in the target and faithfulness of the actual map

Here is a direct form of the invariant differential-form calculation.
On \(\mathbb Q^s\), the basic power sums \(p_1,\ldots,p_s\) have
Jacobian \(s!\prod_{i<j}(x_j-x_i)\). Every polynomial differential
form therefore has a unique rational expansion in wedges of the
\(dp_j\). For an invariant form, wedge with the complementary
differentials to extract one coefficient. Its numerator, relative to
\(dx_1\wedge\cdots\wedge dx_s\), is alternating, and is divisible
by every \(x_j-x_i\); the quotient by the Jacobian is a symmetric
polynomial. This proves existence and uniqueness over the invariant
polynomial ring. Split off the mean coordinate and its differential.
On \(W_s\), the resulting invariant form algebra is
\[
I_s\otimes\Lambda(dq_2,\ldots,dq_s),\qquad
I_s=\mathbb Q[q_2,\ldots,q_s],\qquad q_d=\sum_i x_i^d.
\tag{HM.9}
\]
The mean splitting and the triangular Newton identities are the actual
maps in this special case of Solomon's theorem.

Identify \(W_s\) with its dual by its invariant rational dot product.
Let \(\partial=\iota_x\) be contraction by the Euler vector, and set
\(\xi_d=dq_d/d\). Then
\[
\partial\xi_d=q_d,\qquad \deg q_d=\deg\xi_d=d.
\tag{HM.10}
\]
On \(\operatorname{Sym}^tW_s^*\otimes\Lambda^rW_s^*\), the kernel
of \(\partial\) is the actual Young image of \(S_{(t,1^r)}W_s^*\).
For \(r>0\), exterior Pieri gives the two shapes
\((t+1,1^{r-1})\) and \((t,1^r)\). The first highest vector has
a nonzero contraction term; the second shape is absent from the
target. This specifies the kernel through the rational row and column
Young projectors. At \(r=0\), retain positive polynomial degree.
The equality \(\partial d+d\partial=D\) also gives the explicit
contracting homotopy \(D^{-1}d\) in positive total degree.
Taking invariants is exact by the actual averaging projector.

Give \(q_d\) and \(\xi_d\) the same \(d\)-th unit multidegree.
For \(\beta\ne0\) and \(J,k\) as above, choose \(i=\min J\).
The multidegree-\(\beta\) complex has basis
\(q^{\beta-\mathbf1_S}\xi_S\) for \(S\subseteq J\), and its
differential is exterior contraction \(v_j\mapsto1\).
An explicit basis for the exterior-degree-\(r\) kernel is
\[
q^\beta\bigwedge_{j\in T}
 \left(\frac{\xi_j}{q_j}-\frac{\xi_i}{q_i}\right),
\qquad T\subseteq J\setminus\{i\},\quad |T|=r.
\tag{HM.11}
\]
These are polynomials: each surviving wedge term has at most one
factor of each denominator, and its exponent in \(\beta\) is positive.
In the basis \(v_i,v_j-v_i\), contraction kills exactly the exterior
algebra on the latter vectors. This proves both spanning and
independence, with dimension \(\binom{k-1}{r}\).

Summing over \(\beta\) proves that the target of (HM.3) has exactly
the hook multiplicity computed in (HM.8). The ordinary Cauchy maps
identify that multiplicity with \((S_{(t,1^r)}W_s)^{S_s}\); these
are the same normalized Young projectors used in R-046. Since (HM.3)
has already been proved surjective, equality of these dimensions proves
faithfulness of this specified morphism:
\[
\boxed{\mathsf p_s\text{ is an isomorphism on every hook }
S_{(t,1^r)}U\text{ component, for every }s\ge1.}
\tag{HM.12}
\]
There is no multigrading assertion about \(\mathsf p_s\): the two
multigraded counts establish equality after summation in total degree.
The actual isomorphism is the power-sum morphism (HM.3).

For later use its common dimension is the explicit finite sum
\[
H_s(D,r)=
\sum_{\substack{\beta_2,\ldots,\beta_s\ge0\\
                 \sum d\beta_d=D}}
\binom{|\{d:\beta_d>0\}|-1}{r},\qquad D>0.
\tag{HM.13}
\]
In particular all terms vanish when \(r\ge s-1\).

## 4. Exact canonical factorization with its actual row-degree bound

Let \(F\) be any highest polynomial in
\(\operatorname{Sym}^a(\operatorname{Sym}^nV)\) of weight (HM.1).
Write its slots as \((x_i,y_i)\). On the dense chart \(\prod_i x_i\ne0\),
\[
F=\left(\prod_i x_i\right)^n f(y_1/x_1,\ldots,y_a/x_a).
\tag{HM.14}
\]
The actual polynomial \(F\) has separate slot degree \(n\), so
\(f\) has separate row degree at most \(n\). The first-coordinate
highest equations say exactly that \(f\) is invariant under common
translations. Slot symmetry gives \(S_a\)-invariance, and the remaining
highest weight is the hook \((t,1^r)\). Thus (HM.14) is an injection
into the relevant centered invariant space, with the stated row bound.
At \(n<t\) it is this actual bounded subspace that is used.

Let \(A_n=\mathbb Q[y]_{\le n}\). The independent-row morphism is
\[
E_a(f)(L)=L^{\otimes a}f,\qquad L(1)=1,\quad L(y)=0.
\tag{HM.15}
\]
It is injective on common-translation-invariant polynomials.
Indeed, for a normalized functional of mean \(v\), replace it by
\(L_0(p)=L(p(y-v))\); translation invariance preserves its value on
\(f\). Homogeneity in \(L\) restores all \(L(1)\ne0\), a dense
open set. Diagonal polarization of the resulting homogeneous degree
\(a\) polynomial recovers \(f\). The separate degree bound puts the
image in \(\mathcal M_{\le n}(U)\), preserving the exact hook type.

For centered split-factor rows \(w_1,\ldots,w_n\), put
\(p_d=\sum_iw_i^{\otimes d}\). The normalized tensor pairing gives
the order-\(d\) moment
\[
\mu_d=\frac1{(n)_d}
\sum_{\substack{i_1,\ldots,i_d\text{ distinct}}}
w_{i_1}\otimes\cdots\otimes w_{i_d}
=\frac1{(n)_d}
\sum_{\substack{\pi\in\Pi([d])\\|B|\ge2\ \forall B}}
\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!\,p_{|B|}.
\tag{HM.16}
\]
All \(2\le d\le n\) are allowed. The first equality follows from
the monomial pairing: a coordinate monomial of lower degree \(d\)
and multiplicity vector \(\alpha\) is multiplied by
\((n-d)!\prod_j\alpha_j!/n!\). The second equality is the
set-partition inclusion–exclusion expansion, with the displayed
Möbius block factors; singleton blocks vanish after centering.
This is the same normalized pairing as TM.15–TM.16.

There is one single-block term, with scalar
\[
c_{n,d}=\frac{(-1)^{d-1}(d-1)!}{(n)_d}\ne0.
\]
Every other term uses smaller moment degrees. Therefore (HM.16)
defines the explicit graded equivariant automorphism
\(\Psi_n\) of \(\mathcal M_{\le n}(U)\), whose inverse successively
solves for the generators in degrees \(2,3,\ldots,n\).

Direct grid pairing now gives the exact dehomogenized canonical map
\[
\boxed{h_{a,n}F\quad\longleftrightarrow\quad
\mathsf p_n\,\Psi_n\,E_a(f).}
\tag{HM.17}
\]
Every scalar in this equality is fixed by (HM.16); there is no extra
factor. Subtracting the common row mean is an actual unipotent
substitution, so the identity on centered rows determines the entire
affine output. Multiplication by \((\prod_j x_j)^a\) restores the
homogeneous polynomial on the dense chart and hence everywhere.

The first map from right to left is injective by (HM.15), the middle
map is invertible, and the last is injective on the exact hook component
by (HM.12). Thus \(h_{a,n}\) is injective on the full highest
multiplicity space. Equivariance gives injectivity on the entire
\(\lambda\)-isotypic component. Interchanging \(a,n\) proves the
opposite injection. The two finite-dimensional multiplicity spaces
therefore have equal dimensions and both maps are bijective.
This proves (HM.2), including all unstable inner degrees.

The actual inverse on highest spaces is specified by (HM.17): use
the inverse of (HM.3) on its hook component, the recursive inverse
of (HM.16), and diagonal polarization inverse to (HM.15), then
homogenize by (HM.14). The first inverse can be implemented directly
on rational Young-projected monomial bases: evaluate (HM.3) on each
basis element and invert its now proved nonsingular rational matrix.
Bijectivity just proved ensures that the resulting formal expression
lies in the image of (HM.15), with its required row-degree bound.
This description does not assert that the two canonical maps are
mutual inverses.

## 5. An explicit unit family and the complete normalized scalar

Let \(m\ge2\), \(a,n\ge m\), and put
\[
T=\binom m2+1,\qquad D=\binom{m+1}{2}-1,
\qquad\lambda=(an-D,T,1^{m-2}).
\tag{HM.18}
\]
The first-row inequality follows from \(an\ge m^2=D+T\).
For \(s\ge m\) and rows \(z_i=(u_i,v_{i1},\ldots,v_{i,m-2})\), define
\[
\begin{split}
P_{s,m}(z)&=
\sum_{\substack{I\subseteq[s]\\|I|=m}}
\left(\prod_{\substack{i<j\\i,j\in I}}(u_j-u_i)\right)
\det\bigl[(1,u_i,v_{i1},\ldots,v_{i,m-2})\bigr]_{i\in I}.
\end{split}
\tag{HM.19}
\]
Both factors change by the same sign under reordering \(I\).
Their product and the sum are row symmetric. Differences and the
affine determinant prove common-translation invariance. Each factor
has separate row degree at most \(m-1\) and \(1\), respectively.
The determinant is the exterior highest tensor of weight
\((1^{m-1})\), while the Vandermonde uses only the first coordinate
and has degree \(\binom m2\). Hence their product is a highest
polynomial of tail weight \((T,1^{m-2})\) and separate row degree
at most \(m\), by the displayed determinant and upper-unipotent
column operations.

It is nonzero: on the moment-curve rows
\((u_i,u_i^2,\ldots,u_i^{m-1})\), with distinct rational \(u_i\),
every summand is the square of its nonzero Vandermonde. Thus
\[
F_{a,n;m}=\left(\prod_{i=1}^a x_i\right)^n
P_{a,m}(y_i/x_i)
\tag{HM.20}
\]
is an actual nonzero polynomial highest vector. Its weight is
(HM.18). Formula (HM.13) has exactly one contribution in degree
\(D\) and exterior leg \(m-2\): its support must have at least
\(m-1\) distinct degrees, whose least possible sum is
\(2+3+\cdots+m=D\). Equality forces these degrees to occur once
each. Consequently the entire centered highest space has dimension
one. The vector (HM.20) attains it in every \(a,n\ge m\), proving
that both plethysm multiplicities and the canonical rank are one.

Here is an independent direct calculation of the map scalar.
For a normalized mean-zero functional \(L\), define
\[
J_m(\mu)=
\det\bigl[L(u^p b_q)\bigr]_{
             1\le p\le m-1,\ 0\le q\le m-2},
\qquad(b_0,b_1,\ldots,b_{m-2})=(u,v_1,\ldots,v_{m-2}).
\tag{HM.21}
\]
In each row the entries are formal moments of degree \(p+1\).
Expanding both determinants in (HM.19) and pairing independent rows
gives \(m!\) times the determinant of their one-row pairings. Its
first row is \((1,0,\ldots,0)\), so the remaining determinant is
(HM.21). There are \(\binom am\) subsets. This proves exactly
\[
E_a(P_{a,m})=(a)_m J_m(\mu).
\tag{HM.22}
\]

For centered \(s\)-row power sums, append the degree-zero row to
the matrix with entries \(\sum_i u_i^p b_q(z_i)\), and append the
constant column. The top row is \((s,0,\ldots,0)\).
The ordinary rectangular Cauchy–Binet identity, with its increasing
subset convention, gives
\[
s J_m(p)=P_{s,m}.
\tag{HM.23}
\]
This also identifies the invariant Euler form exactly:
\(\iota_u(dq_2\wedge\cdots\wedge dq_m)=m!J_m(p)
=(m!/s)P_{s,m}\).

The hook component of \(\mathcal M_{\le n}\) in this degree is one
dimensional for every \(n\ge m\), as just proved, and \(J_m\)
is a nonzero vector in it by (HM.23). The substitution \(\Psi_n\)
acts there by the product of the single-block coefficients in
degrees \(2,\ldots,m\). Indeed its original multidegree, one
factor in each of those degrees, has that coefficient. Every term
using a lower-degree substitution loses its highest replaced degree
and cannot restore that multidegree. The one-dimensionality and
equivariance then give the entire identity, not only one coefficient.
Using (HM.22)–(HM.23) in (HM.17) proves
\[
\boxed{\begin{aligned}
h_{a,n}F_{a,n;m}&=C_m(a,n)F_{n,a;m},\\
C_m(a,n)&=
(-1)^{\binom m2}\frac{(a)_m}{n}\,
\frac{\prod_{j=1}^{m-1}j!}{\prod_{d=2}^{m}(n)_d}\ne0.
\end{aligned}}
\tag{HM.24}
\]
The reciprocal gives the complete unit-component inverse.
In the square case this simplifies by the displayed factorial
products to the exact scalar
\[
\boxed{C_m(m,m)=
(-1)^{\binom m2}\frac{\bigl(\prod_{j=1}^{m-1}j!\bigr)^2}
{(m!)^{m-1}}.}
\tag{HM.25}
\]
For \(m=2,3,4,5\), these values are respectively
\(-1/2,-1/9,1/96,1/2500\).
Thus the actual square map has a nonzero unit component of weight
\((T,T,1^{m-2})\) in every rank \(m\), with a specified preimage
and complete scalar.

## 6. Further positive ranks, endpoints, and transport

The earlier Euler-form family also improves without any bound
depending on the number of odd tail parts. Let
\[
r\ge1,\quad a\ge r+2,\quad u,v\ge0,\quad
t=\frac{r^2+3r+4}{2}+2u+3v,\quad n\ge t.
\tag{HM.26}
\]
In (HM.11), use support \(\{2,3,\ldots,r+2\}\), every exponent
one, and the full \(r\)-element exterior subset; multiply by
\(q_2^u q_3^v\). This gives a nonzero invariant hook tensor.
The column-wise row bound \(t\) from TM.4 makes its homogenization
polynomial at every \(n\ge t\). Its first row is at least \(t\),
since \((a-2)t\ge r\). Therefore the actual common rank is
\[
\operatorname{mult}_{(an-t-r,t,1^r)}\operatorname{im}h_{n,a}
=H_a(t+r,r)\ge1.
\tag{HM.27}
\]
These are stable Schur-functor multiplicities; a literal nonzero
component requires \(\dim V\ge r+2\).
The R-049 bound on this family was
\(t+\lfloor(r-\lceil r/3\rceil)/2\rfloor\). In particular
\(r=6s+2\) gives an improvement by \(2s\) rows at the positive
endpoint \(n=t\). The unit family (HM.18) reaches the smaller
actual endpoint \(a=n=m\) as well.

For \(t=1\), (HM.8) has no contributing multidegree:
\(D=r+1<2+\cdots+(r+2)\). Both actual components vanish.
For \(a=1\) or \(n=1\), the tensor map is the identity on
\(\operatorname{Sym}^{an}V\); every nonempty tail component is
zero. The empty tail has coefficient one and its pure-power map
has scalar one. These observations also follow from the empty
moment algebra at one row.

All averages, Young projectors, row projections, moment coefficients,
and inverses above are rational, with nonzero displayed denominators.
Naturality gives the actual maps in every finite dimension that
supports \(S_\lambda V\), and scalar extension gives every
characteristic-zero field. The graded coordinate-ring map is exactly
the Chow pullback R-037 EP.3–EP.5, with EP.4 its actual morphism.
The frame-torsor and representation-\(K_0\) transport uses the exact
SGA 6 VI Theorem3.3 and V §4, SGA 3 I §4, and EGA II §§2.4–2.5
locators and maps recorded in R-036 §5. Every rank assertion is
proved before that transport.

## 7. Executed independent checks

The reproducible script verify_hook_moment_faithfulness.py records:

- HOOK_MOMENT_FINITE_ROW_CHECK.tsv: all4,650 hooks of degrees1–30
  at row counts1–10. Direct cycle-eigenvalue complete/exterior
  characters and hook Jacobi–Trudi averaging agree with the
  independently counted support formula (HM.13).
- HOOK_MOMENT_MULTIDEGREE_CHECK.tsv: all729 hook comparisons
  for moment multidegrees of total degree2–12. Literal power-sum
  plethysm products and Murnaghan–Nakayama agree with (HM.8).
- HOOK_TAIL_RECIPROCITY_MN_CHECK.tsv: all457 valid hook-tail
  weights for \(2\le a\le n\le6\), with every leg up to the
  source length cutoff and every admissible second row. Both original
  plethysms agree, including181 positive pairs. These checks concern
  coefficients; the actual rank is proved by (HM.17).

The separate verify_hook_tail_canonical_scalar.py expands both
determinant permutations in (HM.19), pairs each resulting original
row monomial with the coefficients of an actual product of linear
forms, and uses its exact multinomial denominator. It does not call
the moment determinant on the literal side. All75 pairings in
HOOK_TAIL_CANONICAL_SCALAR_CHECK.tsv agree with (HM.24), for
\(m=2,3,4,5\), \(n=m,m+1,m+2\), two configurations, and
\(a=m,m+1,m+3\), plus \(m=n=6\) at those three outer degrees.
First coordinates are nonunit, including alternating signs, and the
target Vandermonde-square evaluation is nonzero in every sample.

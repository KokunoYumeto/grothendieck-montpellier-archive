# All stable two-row tails with a fixed second part

## G-040. A positive algorithm with an explicit fixed-parameter bound

For every integer \(b\ge2\), the following whole parameter family
has a positive bounded-polytope formula of polynomial description
size in \(m\) and the binary parameter lengths:
\[
\begin{gathered}
m\ge3,\quad a\ge b,\quad t\ge0,\quad n\ge a+t,
\quad\mu\vdash m,\\
\lambda=(mn-a-b-(m-1)t,a+t,b+t,t^{m-3}).
\end{gathered}
\tag{FS.1}
\]
Here \(b\) is the fixed parameter. The algorithm below supplies
computable functions \(f,g\) and a bound
\[
f(b)\bigl(m+\operatorname{bits}(a,t,n,\mu)+1\bigr)^{g(b)}
\tag{FS.2}
\]
for construction, exact coefficient evaluation and support decision.
It gives polynomial bounds for each fixed \(b\); it makes no
polynomial claim when \(b\) varies unrestrictedly. The positive
polytopes have at most \(3m+2b\) variables. For \(t\ge1\), the
ordinary binary-part output contains \(m\) positive parts. The
explicit-\(m\) convention at \(t=0\) is retained as in G037–G039.

The construction uses a finite actual cokernel, minimal homogeneous
covers, an explicit decomposition by the exponents of the high-degree
invariants, and a bounded Gröbner calculation in at most \(b-2\)
variables. G038 and G039 give the much smaller displayed formulas
at \(b=2,3\). The present construction applies to every \(b\).

## 1. The actual transfer and its finite cokernel

Put \(W=\mathfrak h_m\), \(P=\operatorname{Sym}W\),
\(I=\mathbb Q[e_2,\ldots,e_m]\), and \(D=a+b\).
The flag and determinant map T032/C4–8 identifies the original
balanced module with
\(\operatorname{sgn}^t\otimes S_{(a,b)}W\).
The effective label is \(\nu=\mu\) for even \(t\), and
\(\nu=\mu'\) for odd \(t\). The first two partition gaps are
nonnegative because \(a\ge b\) and \(n\ge a+t\).

Use the graded free \(P\)-modules with tensor degrees \(b,b-1\),
and the literal derivative transfer
\[
\phi_b:P\otimes\operatorname{Sym}^bW
 \longrightarrow P\otimes\operatorname{Sym}^{b-1}W,
\qquad
f\otimes v_1\cdots v_b\longmapsto
 \sum_{i=1}^b fv_i\otimes\prod_{j\ne i}v_j.
\tag{FS.3}
\]
For first-factor degree \(u\), its Pieri highest vectors are
\(x^{u-i}X^{b-i}(xY-yX)^i\),
\(0\le i\le\min(u,b)\). The operator
\(x\partial_X+y\partial_Y\) has coefficient \(b-i\)
on each such vector. Thus its only kernel summand, at \(u\ge b\),
is \(S_{(u,b)}W\), and it is surjective at total degrees
at least \(2b-1\). At the remaining degrees its entire cokernel is
\[
C_{b-1+j}=S_{(b-1,j)}W,
\qquad0\le j\le b-1,
\quad C_e=0\text{ in all other degrees}.
\tag{FS.4}
\]
For \(j=0\), this denotes \(\operatorname{Sym}^{b-1}W\).
The nonzero coefficients \(b-i\), the rational Young inclusions
and the same two-row Pieri calculation as G039§1 prove all these
claims, including \(\dim W=2\). There is no asymptotic cokernel.

Let \(L=2b-2\), \(B=\min(m,b-1)\),
\[
J=\mathbb Q[e_2,\ldots,e_B],\qquad
Y=(e_{B+1},\ldots,e_m),\qquad I=J[Y].
\tag{FS.5}
\]
Every variable in \(Y\) kills \(C\): its degree is at least
\(b\), whereas \(C\) is supported in degrees \(b-1\) through
\(2b-2\), so its image has degree at least \(2b-1\).
The action of the variables of \(J\) is the actual
multiplication induced from the first factor of (FS.3). It is
computed by the finite matrices of (FS.3) in degrees at most \(L\).
No decomposition of this finite \(J\)-module is assumed.

## 2. Constructing the covariant cokernel in polynomial size

Each vector space used in degrees at most \(L\) has dimension
at most \(f(b)(m+1)^L\): use the monomial bases of the two
symmetric factors in (FS.3). Choose the rational basis
\(e_i-e_m\) of \(W\). Adjacent permutations have explicit
integer matrices, and symmetric powers of degree at most \(L\)
have polynomial-size rational matrices for fixed \(b\).
Exact row reduction gives the quotient spaces in (FS.4), the
adjacent-permutation matrices on them, and the multiplication
maps by every \(e_i\), \(2\le i\le B\).
The elementary invariant is obtained from the actual centered
vectors \(P_me_i\); its sum over \(i\)-subsets has at most
\(m^i\) terms. All degrees here are bounded by \(L\).

Only labels satisfying
\[
\nu_1\ge m-L
\tag{FS.6}
\]
can occur in \(C\). Indeed every degree-\(e\) summand embeds,
by its rational Young map, in \(W^{\otimes e}\subset E^{\otimes e}\),
where \(E=\mathbb Q^m\) and \(e\le L\). The literal word orbits
in \(E^{\otimes e}\) have stabilizer \(S_{m-l}\), \(l\le e\).
Successive one-box induction from the row \((m-l)\) gives only
partitions containing that row. This proves (FS.6) through the
actual word, coset and Young maps.

For a label violating (FS.6), put \(C_\nu=0\) immediately.
For every remaining label construct its rational Specht module
using row tabloids and the column antisymmetrizer. There are
at most \(f(b)(m+1)^L\) tabloids: choose the at most \(L\)
letters outside the first row, then place them in the remaining
rows. The column group has size bounded only by \(L\), because
all nonsingleton columns contain one of these at most \(L\)
lower boxes. The orbit span of one column polytabloid under
adjacent permutations is the actual Young module \([\nu]\).
It is obtained by at most the number of tabloids many independent
row-reduction additions. This is the same Young-group-algebra
realization underlying A012, with the explicit quotient from
row-symmetric tensor words to row tabloids.

Solve the intertwining equations
\(T\rho_\nu(s_i)=\rho_C(s_i)T\), \(i=1,\ldots,m-1\),
degree by degree. They give exactly
\(C_\nu=\operatorname{Hom}_{S_m}([\nu],C)\), since the
adjacent transpositions generate the group. The multiplication
matrices commute with these actions and induce the actual
\(J\)-module structure on the resulting solution spaces.
Their dimensions, matrix sizes and coefficient bit lengths are
polynomial in \(m\) for each fixed \(b\). Rational Gaussian
elimination has polynomial bit bounds from its determinant
minors. This construction never sums over all \(m!\) permutations.
For \(m\le L\), all these bounds remain within a function of \(b\).

## 3. Minimal finite covers and the actual free remainder

Choose a homogeneous basis of \(C_\nu/J_+C_\nu\) and fixed lifts.
It gives the minimal graded cover
\(F_0\to C_\nu\) over \(J\), with a basis polynomial
\(c_0(q)\) supported in degrees at most \(L\).
Its kernel \(R\) is generated in weighted degrees at most
\(L+B\le2L\). Here is an explicit proof and algorithm for
this bound. Order homogeneous free monomials in \(F_0\) by
a fixed term order and greedily retain independent images in
\(C_\nu\). The retained monomials are the normal monomials
of the kernel: multiplying a dependent relation by a variable
preserves its leading-term relation. They all have weight at
most \(L\). Every minimal leading monomial outside this
order ideal is a variable times a normal monomial, and hence
has weight at most \(L+B\). Its image is a linear combination
of earlier retained monomials of the same weight. These
relations form a Gröbner basis by their exact leading ideal,
and in particular generate \(R\) in the asserted degree range.

In degrees through \(L+B\), compute the relation spaces and
divide by the multiples of lower-degree relations. Fixed
homogeneous lifts of their quotient bases give the minimal
free cover
\[
F_1\xrightarrow{d_J}F_0\longrightarrow C_\nu\longrightarrow0,
\qquad K_J=\ker d_J.
\tag{FS.7}
\]
Write \(c_1(q)\) for the basis polynomial of \(F_1\).
Both ranks and all these finite matrices have the polynomial
bounds from §2; the number of \(J\)-monomials in weight
at most \(2L\) depends only on \(b\).

Over \(I=J[Y]\), the minimal first two covers of the same
module \(C_\nu\) are
\[
M_0=I\otimes_JF_0,\qquad
M_1=(I\otimes_JF_1)\oplus
       \bigoplus_{y_i\in Y}(I\otimes_JF_0)\xi_i,
\tag{FS.8}
\]
where \(\xi_i\) has degree \(\deg y_i\) and maps by
multiplication by \(y_i\). The first summand maps by \(d_J\).
These generators are minimal: in \(Y\)-degree zero they are
the minimal \(J\)-relations, and in each single-variable
\(Y\)-degree they are the free generator residues of \(F_0\).
Higher \(Y\)-degrees are their multiples. This also proves
directly that the image is the full kernel of \(M_0\to C_\nu\).

The covariants of the actual domain and target of (FS.3) are
graded free over \(I\), by the averaged coinvariant section.
Their basis polynomials are
\[
A_\nu(q)=q^b f_{[\nu]\otimes\operatorname{Sym}^bW}(q),
\qquad B_\nu(q)=q^{b-1} f_{[\nu]\otimes\operatorname{Sym}^{b-1}W}(q).
\tag{FS.9}
\]
Apply the two actual homogeneous cover cancellations of
G039§3 to (FS.8): adapt the target basis to the minimal
cokernel generators, lift and cancel its free zero-image
complement, then adapt the remaining domain basis to the
minimal relations and kill its complementary images by a
triangular basis change. This gives an isomorphism on the
actual transfer kernel
\[
K_\nu\simeq\mathcal F_\nu\oplus\ker(M_1\to M_0),
\tag{FS.10}
\]
where \(\mathcal F_\nu\) is graded free, with nonnegative
basis polynomial
\[
F_\nu(q)=A_\nu(q)-B_\nu(q)+c_0(q)-c_1(q)
                   -c_0(q)\sum_{i=B+1}^m q^i.
\tag{FS.11}
\]
All choices and inverse basis changes are those explicitly
proved in G039§3. This proves coefficientwise positivity
of (FS.11) for every label, including \(C_\nu=0\).
Its degree is at most
\(\max\{\binom m2+b,m+L,2L\}\).

## 4. A positive decomposition by the high-variable multidegree

Write \(y^\beta\) for a monomial in \(Y\). At
\(\beta=0\), the kernel in (FS.10) is exactly \(K_J\).
At \(\beta\ne0\), let \(i\) be the first positive index
and let \(S=\{j:\beta_j>0\}\). The degree-\(\beta\)
domain consists of one copy of \(F_1\) and one copy of
\(F_0\) for each \(j\in S\). Its map is
\[
(u,(v_j)_{j\in S})\longmapsto d_Ju+\sum_{j\in S}v_j.
\tag{FS.12}
\]
Thus its kernel has the explicit inverse pair of maps
\[
\begin{aligned}
F_1\oplus\bigoplus_{j\in S\setminus\{i\}}F_0
 &\longrightarrow\ker(\text{FS.12}),\\
(u,(v_j)_{j\ne i})&\longmapsto
 \left(u,\ v_i=-d_Ju-\sum_{j\ne i}v_j,\ (v_j)_{j\ne i}\right).
\end{aligned}
\tag{FS.13}
\]
The inverse reads \(u\) and all nondistinguished \(v_j\).
The omitted monomial factors are exactly
\(y^\beta\) in the first summand and
\(y^{\beta-e_j}\xi_j\) in the second. They are polynomial
because \(\beta_j>0\). This proves a genuine vector-space
basis decomposition in every multidegree.

Consequently its Hilbert series has the positive form
\[
\begin{aligned}
\operatorname{Hilb}\ker(M_1\to M_0)
={}&\operatorname{Hilb}K_J\\
&+\operatorname{Hilb}F_1\,
       \sum_{\beta\ne0}q^{\sum_{i>B}i\beta_i}\\
&+\operatorname{Hilb}F_0\,
       Z_{(B+1,B+2,\ldots,m)}(q).
\end{aligned}
\tag{FS.14}
\]
The last series is the explicit star-cycle series (SR3.5).
An empty high-variable list makes both latter terms zero;
a one-variable list makes the last term zero. Thus this
also covers every small \(m\).

## 5. Polynomial Gröbner bounds for the remaining fixed-variable kernel

There are \(\ell=B-1\le b-2\) variables in \(J\).
At \(b=2\), the ring is \(J=\mathbb Q\), so
\(F_0=C_\nu\), \(F_1=K_J=0\); the high-variable formula
already gives the complete kernel. More generally zero-variable
matrices are handled directly by rational linear algebra.
Let \(r_0,r_1\) be the ranks of \(F_0,F_1\), and set
\(\delta=\max(1,2L)\). Regard (FS.7) temporarily as an
ordinary polynomial matrix with degree-zero basis vectors;
its entries have ordinary degree at most \(\delta\).
The original positive weighted degrees and shifts are
retained separately in every monomial and matrix.

The Hermann–Seidenberg bound, in Aschenbrenner,
*Ideal membership in polynomial rings over the integers*,
§3, Theorem3.2, PDFp16, bounds kernel generators by
\[
H=(2\max(1,r_0)\delta)^{2^\ell}.
\tag{FS.15}
\]
The primary text is
https://www.mat.univie.ac.at/~maschenbrenner/pdf/ideal2.pdf.
The statement and the complete §3 proof through Theorem3.2
were read; it applies over \(\mathbb Q\) to this exact matrix.

Liang, *Degree bounds for Gröbner bases of modules*,
arXiv:1905.07517v3, Corollary42, PDFp19, gives the
ordinary-degree bound
\[
G=2\bigl(H\max(1,r_1)\bigr)^{2^\ell}
\tag{FS.16}
\]
for a reduced module Gröbner basis generated in degrees
at most \(H\), for any term order. Use the primary
https://arxiv.org/pdf/1905.07517; Corollaries38/42 and the
Theorem40–41 passage were read. The non-graded version
is used, so no equality of ordinary and weighted gradings
is assumed. Zero or full kernels are handled directly.

For each fixed \(b\), both bounds are polynomial in
\(r_0,r_1\), hence in \(m\). They also give an explicit
polynomial bit algorithm: enumerate all vector polynomials
of ordinary degree at most \(G\), solve (FS.7) by rational
linear algebra, and row-reduce their coefficients in the
chosen term order. Every reduced Gröbner basis element
occurs in this finite solution space by (FS.15)–(FS.16).
Select the minimal leading monomials under divisibility
and their reduced lifts. They generate the whole leading
module and hence give a Gröbner basis. Weighted-homogeneous
components can be processed separately, since (FS.7) is
weighted homogeneous; extracting them never increases
the ordinary degree. The unique reduced basis can also
be taken weighted homogeneous.

The number of monomials used is at most
\(r_1\binom{G+\ell}{\ell}\). All output coefficients are
ratios of minors of the finite linear system, giving
polynomial bit length and bit time in these sizes and
the input coefficient height. Thus the computation has
the bound (FS.2), without a search through unbounded degrees.

## 6. Positive lattice sets for every kernel term

The weighted-homogeneous initial module of \(K_J\) is a
direct sum of monomial ideals, one for each basis vector
of \(F_1\). In each component, partition every exponent
axis at all exponents appearing in its leading generators.
Use disjoint integer intervals between consecutive cut
values, including the last infinite interval. Divisibility
by each generator is constant on every resulting grid box.
Retain exactly the boxes belonging to the initial module.
There are polynomially many boxes for fixed \(\ell\):
at most \((s+1)^\ell\) per component with \(s\) leading
generators. Every retained box is a product of integer
intervals. Intersect it with
\[
\sum_{i=2}^{B} i\alpha_i+\deg(\text{component})=D.
\tag{FS.17}
\]
Every infinite upper endpoint is replaced by
\(\lfloor D/i\rfloor\). This gives bounded polytopes.
Their lattice points index an actual basis of \(K_{J,D}\):
for each initial monomial use the first Gröbner element
whose leading monomial divides it and take the corresponding
monomial multiple. Distinct leading monomials give linear
independence, and Gröbner reduction gives spanning in
each finite weighted degree. This specifies the triangular
bijection back to the actual kernel.

Each coefficient of the nonnegative polynomial (FS.11)
gives the free-degree polytope (SR2.17), now with degree
shift and multiplicity from that polynomial. The middle
term of (FS.14) uses a homogeneous free basis of \(F_1\),
arbitrary \(J\)-monomials and a nonempty \(Y\)-monomial.
Partition the last set by its first positive index: all
earlier exponents are zero, that exponent is at least one,
and all later exponents are nonnegative. Append the
weighted degree equation and a bounded index for the
number of free generators in the chosen degree. This
gives at most \(m-B\) polytopes per occurring free degree.

For the last term of (FS.14), use the single least-support
cycle polytope (SR3.20) on \(Y\), append the arbitrary
\(J\)-exponents, the degree shift and a bounded generator
index for \(F_0\). It is exactly the inverse basis
construction (FS.13). The total variable count is below
\(3m+2b\), and the number of pieces and constraints obeys
(FS.2). Distinct components, degrees and least-support
indices are retained as disjoint tags.

## 7. Computing the two free input characters and exact values

The finite polynomial (FS.9) is computable for arbitrary
\(\nu\), without constructing its potentially large
Specht module. The actual identity
\(\operatorname{Sym}^jW=\operatorname{Sym}^jE-
\operatorname{Sym}^{j-1}E\) in the representation ring
comes from \(E=\mathbf1\oplus W\). The monomial orbits
of \(\operatorname{Sym}^jE\) are indexed by partitions
\(\rho\vdash j\). With \(l=\ell(\rho)\le m\), their
stabilizer is
\[
S_{m-l}\times\prod_{d\ge1}S_{m_d(\rho)}.
\tag{FS.18}
\]
The tensor-coset isomorphism of G038§6 identifies tensoring
with that orbit module with restriction and induction
through this very subgroup. Enumerate each distinct partition
\(\eta\subseteq\nu\) of size \(m-l\) exactly once. For each
tuple of small-factor labels \(\sigma_d\vdash m_d(\rho)\),
compute the iterated Littlewood–Richardson multiplicity
\(c^\nu_{\eta,\sigma_1,\sigma_2,\ldots}\). For each distinct
output partition \(\kappa\supseteq\eta\) of size \(m\), the
contribution is the product
\[
c^\nu_{\eta,\sigma_1,\sigma_2,\ldots}\,
c^\kappa_{\eta,\sigma_1,\sigma_2,\ldots}.
\]
Sum these products over the displayed distinct shapes and labels.
The iterated LR coefficients count the intermediate shapes for
the ordered small subgroup factors; an ordering of the removed
corner boxes supplies no additional multiplicity. These are
finite tableaux on at most \(b\)
boxes; the complete LR map and proof are Macdonald I§9,
pp142–147, as freshly read for T064. The identical tensor
coset and rational Young maps prove this use for arbitrary
\(\nu\). At most \(f(b)(m+1)^{2b}\) candidates occur.
Apply the exact finite fake-degree hook formula (SR2.16)
to each resulting label. This computes (FS.9), (FS.11)
and every free coefficient within (FS.2).

For exact values, the free and high-variable terms have
rational series with denominator factors \(1-q^i\),
\(2\le i\le m\), and polynomially many shifts.
For every grid box of §6, multiply its finite interval
series and unbounded geometric series. At most
\(2^\ell\) numerator terms arise by expanding its finite
interval factors; this is a function of \(b\). Its shifts
are polynomially bounded by (FS.16). Bostan–Mori parity
extraction from G037§6 evaluates these exact root-of-unity
denominators in time polynomial in their degrees and
\(\log(D+1)\), with the proved coefficient-height bound.
The high-variable star series has only \(O(m^2)\) pairs.
The exact sum therefore obeys (FS.2). Testing whether
that nonnegative integer is zero gives the full support
decision in the same bound.

## 8. Geometric comparison and precise implementation scope

The original coefficient is transported by the actual
balanced flag map and determinant pairing in §1. Transfer
(FS.3), its finite cokernel and both minimal covers are
equivariant coherent-module maps over \(\operatorname{Spec}I\).
The free cancellation (FS.10) and the explicit multidegree
inverse (FS.13) are isomorphisms of the specified graded
modules or vector-space fibers, as indicated. The initial
module in §6 is related by its leading-term filtration
and the displayed triangular basis lift; weighted degree
is preserved throughout. Thus each positive count is
carried to the same original highest multiplicity space.

The fixed transport locators are SGA3 I4.5 and4.7.2–4.7.3;
EGA II2.4.1–2.4.2 and2.5.2/2.5.4; SGA6 VI3.3 and
V4.2,4.4,4.8–4.9. The archive comparison is A012's
tensor-word, row-symmetry and Young maps for cote133/028.
All scalar calculations are over \(\mathbb Q\), and
the stated multiplicities extend to characteristic-zero
fields by the rational maps. No characteristic-p rank
assertion is inferred from those maps.

This report proves and specifies the complete finite
algorithm. The small closed formulas at \(b=2,3\) have
their own executable implementations and receipts in
G038–G039. General-purpose execution and any additional
finite tests of the present construction are recorded
separately, with their actual scope. Whole-proof readings
must be recorded before this finding is marked completed.

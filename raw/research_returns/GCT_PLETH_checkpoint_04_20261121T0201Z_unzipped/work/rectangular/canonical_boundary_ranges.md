# Canonical-map ranges below the full square bound

Statements **R-021**, **R-022**, and **R-023**. Written and checked on
21 November 2026 UTC by GPT-6 Astra Pro, `/root/rectangular_cases`;
effort setting not exposed. The prime-interval input is Nagura's
established theorem. The square determinant scalars are the established
prime-adjacent Alon–Tarsi cases in R-007. The exact specialization and
multiplication maps are G-013. The common-polarization inputs are
R-018–R-020. No historical novelty claim is made.

## Exact canonical-map convention

The normalized grid map is

\[
h_{b,a}:\operatorname{Sym}^{b}(\operatorname{Sym}^{a}V)
\longrightarrow\operatorname{Sym}^{a}(\operatorname{Sym}^{b}V),
\qquad
h_{b,a}(v_1^a\cdots v_b^a)=(v_1\cdots v_b)^a.
\tag{K.1}
\]

It is the degree-\(b\) part of the graded algebra map \(\mu_a\) of
R-008–R-009. Symmetric powers are embedded in tensors by normalized
averaging. Taking the transpose of the row and column orthogonal
averaging projectors gives the opposite grid map \(h_{a,b}\). Thus

\[
\mathcal K_{a,b}(W):=\ker\!\left(
h_{a,b}:\operatorname{Sym}^{a}(\operatorname{Sym}^{b}W)
\to\operatorname{Sym}^{b}(\operatorname{Sym}^{a}W)\right)
\tag{K.2}
\]

is, for \(W=V^*\), the annihilator of the image in (K.1).
The standard perfect symmetric-tensor pairings identify these maps
without a scalar change. In particular absence of the label
\(\lambda\) from (K.2) proves surjectivity of (K.1) onto its entire
target \(\lambda\)-isotypic component.

## R-021. Every even-rank boundary determinant is in the canonical image

For every even integer \(a\ge4\), put \(B=a(a-2)\). Then

\[
\boxed{
[S_{(B^a)}V:\operatorname{im}h_{B,a}]
=[S_{(B^a)}V:\operatorname{Sym}^a(\operatorname{Sym}^BV)]
=1\qquad(\dim V\ge a).}
\tag{K.3}
\]

The proof supplies an explicit rational preimage of the normalized
determinant tensor \(I_{a,B}\). In smaller dimensions that Schur
functor is zero.

### 1. The exact seed preimages

For every odd prime \(p\), R-007 gives nonzero square scalars
\(c_{p-1}\) and \(c_{p+1}\), with

\[
h_{w,w}(I_{w,w})=c_w I_{w,w},
\qquad w=p-1\text{ or }p+1.
\]

For \(w\ge a\), let \(E=\mathbf Q^a\), enlarge it to
\(U=E\oplus\mathbf Q^{w-a}\), and write
\(z_{a+1},\ldots,z_w\) for the added basis covectors. The linear map

\[
j:\operatorname{Sym}^aE^*\longrightarrow\operatorname{Sym}^wU^*,
\qquad F\longmapsto Fz_{a+1}\cdots z_w
\tag{K.4}
\]

has its ordinary dual \(j^*:\operatorname{Sym}^wU\to
\operatorname{Sym}^aE\) under the normalized symmetric pairings.
Define

\[
u_{a,w}=\operatorname{Sym}^w(j^*)\bigl(I_{w,w}/c_w\bigr).
\tag{K.5}
\]

The exact equality is

\[
h_{w,a}(u_{a,w})=I_{a,w}.
\tag{K.6}
\]

To check the scalar, let \(\Pi_d\) multiply \(d\) linear forms.
Appending the fixed forms \(z_{a+1},\ldots,z_w\) gives a map
\(\iota\) of ordered factors with
\(j\circ\Pi_a=\Pi_w\circ\iota\). Pullback of this identity gives
\(h_{w,a}\operatorname{Sym}^w(j^*)=\iota^*h_{w,w}\).
The determinant with the appended coordinate forms has a block
identity matrix, so
\(\iota^*(\det_w^w)=\det_a^w\) with scalar one. These equations
prove (K.6), with every normalization contained in the actual dual
map \(j^*\).

The algebra identities already proved in R-009 and G-013 give

\[
h_{B,a}\left(\prod_w u_{a,w}^{e_w}\right)
=I_{a,B},\qquad B=\sum_w e_w w.
\tag{K.7}
\]

Indeed \(\mu_a\) is an algebra morphism and
\(I_{a,w}I_{a,w'}=I_{a,w+w'}\), as verified by evaluation on arbitrary
ordered covectors.

### 2. A prime and explicit nonnegative exponents for every \(a\)

For \(a=4,6,\ldots,24\), the following table provides a square seed
of width exactly \(a\):

\[
\begin{array}{c|rrrrrrrrrrr}
a&4&6&8&10&12&14&16&18&20&22&24\\\hline
p&3&5&7&11&11&13&17&17&19&23&23\\
a=p\pm1&+1&+1&+1&-1&+1&+1&-1&+1&+1&-1&+1.
\end{array}
\tag{K.8}
\]

Each displayed \(p\) is prime. Thus \(u_{a,a}^{a-2}\) is a
preimage of \(I_{a,a(a-2)}\) by (K.7).

For every even \(a\ge26\), Nagura's theorem supplies a prime

\[
a<p<\frac65a.
\tag{K.9}
\]

The exact primary locator is Jitsuro Nagura, *On the interval
containing at least one prime number*, **Proceedings of the Japan
Academy 28** (1952), 177–181, the unnumbered **Theorem on printed
p. 180, case \(n=5\)**, with proof completed on p. 181.
Official full article:
<https://www.jstage.jst.go.jp/article/pjab1945/28/4/28_4_177/_pdf>;
DOI <https://doi.org/10.3792/pja/1195570997>.
Only its range \(x>25\) is needed here, so no endpoint convention
at \(x=25\) affects this proof.

Put \(g=(p-1)/2\). The two permitted widths \(p-1,p+1\) are at
least \(a\), and their normalized values are \(g,g+1\). Their exact
even conductor is \(2g(g-1)\), as proved in G-013 by the explicit
residue representation. Here the needed inequality follows directly:

\[
2g(g-1)=\frac{(p-1)(p-3)}2
<\frac{p^2}2<\frac{18a^2}{25}<a(a-2)=B,
\tag{K.10}
\]

where the last strict inequality holds for every \(a\ge26\).
For complete explicitness, set

\[
N=B/2,\qquad y=N-g\lfloor N/g\rfloor,\qquad
x=\lfloor N/g\rfloor-y.
\tag{K.11}
\]

Then \(0\le y\le g-1\), and (K.10) implies
\(\lfloor N/g\rfloor\ge g-1\), so \(x\ge0\). The identity
\(N=xg+y(g+1)\) is immediate from (K.11). Consequently

\[
\boxed{
h_{B,a}(u_{a,p-1}^{x}u_{a,p+1}^{y})=I_{a,B}\ne0.}
\tag{K.12}
\]

The target determinant multiplicity is one for even \(B\) by
R-001. Equations (K.8) and (K.12) prove (K.3) for every even
\(a\ge4\). This is a transfer of the checked prime-interval and
prime-adjacent scalar results through explicit algebra morphisms.

### A uniform determinant-image range and its row extensions

The same construction gives a uniform range for every integer rank
\(a\ge26\), with no parity restriction on \(a\): for every even

\[
B\ge2\left\lceil\frac{9a^2}{25}\right\rceil,
\qquad s\ge0,
\tag{K.12a}
\]

there is the explicit nonzero image

\[
\boxed{
h_{B+s,a}\left(u_{a,p-1}^{x}u_{a,p+1}^{y}(e_1^a)^s\right)
=I_{a,B}(e_1^{\otimes a})^s\ne0,}
\tag{K.12b}
\]

where \(p\) is any prime from (K.9), and \(x,y\) are given by
(K.11) with this value of \(B\). Indeed
\(g(g-1)<9a^2/25\le B/2\), so the same proof gives nonnegative
integer exponents and \(B=x(p-1)+y(p+1)\). Applying the graded
algebra map proves (K.12b) exactly.

The target weight is
\(\lambda=(as+B,B^{a-1})\). Its target and image multiplicities
are both one. For the target, the balanced Cauchy module is
\(S_\lambda\mathbf Q^a\simeq\det^B\otimes
\operatorname{Sym}^{as}\mathbf Q^a\). After removing the determinant
weight, its balanced weight is \((s^a)\), with sole monomial
\(x_1^s\cdots x_a^s\). Slot permutations fix this vector because
\(B\) is even. Nonvanishing of (K.12b) follows by evaluating its
target on covectors: it becomes a determinant power times the
nonzero product of first-coordinate powers. These are actual
canonical images for the full range (K.12a).

## R-022. The canonical surjectivity ranges

Let \(a\ge3\), and put \(r=a-1\). The following are unconditional
component ranges for the actual map (K.1), in every finite dimension.

For every integer

\[
r^2-r+1\le b\le r^2-1,
\]

the map is surjective onto every target isotypic component with

\[
\boxed{\lambda\vdash ab,\qquad \lambda_2\le b-r.}
\tag{K.13}
\]

At the upper boundary \(b=r^2-1\), the larger stated range is

\[
\boxed{\lambda\vdash ab,\qquad
\lambda_1\le r^2\quad\text{or}\quad
\lambda_2\le r(r-1)-1.}
\tag{K.14}
\]

Thus the rank on each such multiplicity space equals its full target
plethysm coefficient. In particular the coefficient inequality in
that component follows from this rank statement. The proof below
tracks the annihilator into the common-polarization kernel and then
removes its rectangular summand by an exact prolongation identity.

### 3. An explicit injection from the canonical annihilator

For all \(b\) in the stated interval, let \(m=b-r\). Then

\[
m\ge(r-1)^2\ge1.
\tag{K.15}
\]

Sra, *The q-Foulkes problem III: On Foulkes' conjecture with a graded
inner factor*, v1, **Theorem 1.3**, gives surjectivity of
\(h_{m,r}\). Its complete proof in §2.2 and its power-polarization
Lemma 2.1 were read in this run. The author's primary PDF is
<https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>.
For \(r=2,m=1\), this lower map is directly the identity
\(\operatorname{Sym}^2V\to\operatorname{Sym}^2V\), as the source
also explicitly records.

Let \(W=V^*\) and \(F\in\mathcal K_{a,b}(W)\). Its corresponding
symmetric \(a\)-linear form on \(\operatorname{Sym}^bV\) is denoted
\(\mathcal A_F\). The annihilator condition is the exact identity

\[
\mathcal A_F(P,\ldots,P)=0
\quad\text{for every }P=u_1\cdots u_b.
\tag{K.16}
\]

Indeed (K.1) has image spanned by precisely these diagonal tensors.

Fix a product \(Q=y_1\cdots y_m\). The polynomial
\((x^r+c\,t^r)Q\) is a product of \(b\) vectors over \(\mathbf C\),
because its binary degree-\(r\) factor splits into linear factors.
The coefficient of \(c\) in (K.16), divided by the nonzero integer
\(a\), gives

\[
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{K.17}
\]

Define
\(G_x(y_1,\ldots,y_m,t)=
\mathcal A_F(x^rQ,\ldots,x^rQ,t^b)\).
It has degree \(b\) in \(t\) and degree \(r\) in each \(y_i\).
The exact differential identity is

\[
D_{y_m,t}\cdots D_{y_1,t}G_x
=\frac{b!}{r!}
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{K.18}
\]

Before the \(i\)-th differentiation, the relevant degrees are
\(p=b-i+1\) and \(s=r\), so \(p-s=m-i+1\ge1\). Sra's
Lemma 2.1 with power one proves injectivity of each step, with all
other variables as spectators. Hence \(G_x=0\).

For fixed \(x,t\), this vanishing is the diagonal of an \(r\)-linear
symmetric form on \(\operatorname{Sym}^mV\), evaluated on all
products \(Q\). The already established surjectivity of \(h_{m,r}\)
therefore gives

\[
\mathcal A_F(x^rQ_1,\ldots,x^rQ_r,t^b)=0
\quad(Q_i\in\operatorname{Sym}^mV).
\tag{K.19}
\]

Represent \(F\) by its polynomial
\(f(v_1,\ldots,v_r;t)=
\mathcal A_F(v_1^b,\ldots,v_r^b,t^b)\).
The exact coefficient-extraction calculation now is

\[
(T_{r,r,b}\otimes\mathrm{id})f
=\binom{b}{r}^{r}
\mathcal A_F(x^rv_1^m,\ldots,x^rv_r^m,t^b)=0.
\tag{K.20}
\]

No injectivity assertion about the last common-polarization step
has been inserted into this argument.

The normalized last-slot inclusion is the natural injective map

\[
\begin{aligned}
\delta:\operatorname{Sym}^{r+1}(\operatorname{Sym}^bW)
&\longrightarrow
\operatorname{Sym}^r(\operatorname{Sym}^bW)
\otimes\operatorname{Sym}^bW,\\
w_0\cdots w_r&\longmapsto
\frac1{r+1}\sum_{i=0}^r
\left(\prod_{j\ne i}w_j\right)\otimes w_i.
\end{aligned}
\tag{K.21}
\]

Multiplying the two tensor factors is a left inverse, proving
injectivity. In the invariant-tensor realization (K.21) is simply
inclusion of the fully symmetric tensors into the tensors symmetric
in the first \(r\) slots. Equation (K.20) consequently proves the
actual natural injection

\[
\boxed{
\delta:\mathcal K_{a,b}(W)\hookrightarrow
\ker T_{r,r,b}(W)\otimes\operatorname{Sym}^bW.}
\tag{K.22}
\]

### 4. Proof of the second-row range

R-018 proves that every constituent \(S_\nu W\) of
\(\ker T_{r,r,b}\) has \(\nu_2\ge b-r+1\).
Pieri's rule for tensoring by \(\operatorname{Sym}^bW\) gives

\[
\lambda_1\ge\nu_1\ge\lambda_2\ge\nu_2
\ge\lambda_3\ge\cdots.
\tag{K.23}
\]

In particular \(\lambda_2\ge\nu_2\). The injection (K.22) proves
that no annihilator component can have \(\lambda_2\le b-r\).
By the exact duality (K.2), this is precisely the component
surjectivity assertion (K.13).

## R-023. An exact rectangular prolongation identity

Let \(r\ge2\), let \(b\ge0\) be even, and set \(a=r+1\). Regard the
unique source copy of \(S_{(b^r)}W\) inside
\(\operatorname{Sym}^r(\operatorname{Sym}^bW)\) using the determinant
highest vector and its \(GL(W)\)-span. Inside the target of (K.21),
the following is an equality of actual submodules:

\[
\boxed{
\delta\bigl(\operatorname{Sym}^{a}(\operatorname{Sym}^bW)\bigr)
\cap\bigl(S_{(b^r)}W\otimes\operatorname{Sym}^bW\bigr)
=\delta\bigl(S_{(b^a)}W\bigr).}
\tag{K.24}
\]

### Proof

Use the polynomial-generator realization with \(a\) vector slots.
The Cauchy decomposition for the first \(r\) slots has its
\(GL(W)\)-type \((b^r)\) paired with
\(S_{(b^r)}\mathbf Q^r=(\det\mathbf Q^r)^b\). Consequently every
polynomial in the left-hand intersection is invariant under every
elementary transvection mixing two of the first \(r\) slots. In
coordinates, it is killed by all the slot derivations

\[
E_{ij}^{\mathrm{slot}}
=\sum_u X_{u,i}\frac{\partial}{\partial X_{u,j}},
\qquad i\ne j,\quad1\le i,j\le r.
\tag{K.25}
\]

The polynomial is fully symmetric in all \(a\) slots. Conjugating
(K.25) by slot permutations therefore shows that it is killed by
the corresponding derivation for every ordered pair \(i\ne j\)
among all \(a\) slots. Exponentiation of these locally nilpotent
derivations proves invariance under \(SL_a\) acting on the slot
space. The Cauchy decomposition for all \(a\) slots identifies
its invariant part: only the determinant characters on the slot
factor can restrict trivially to \(SL_a\). The total degree is
\(ab\), so that character is exactly \(\det^b\), paired with
\(S_{(b^a)}W\). This proves inclusion in the right side of (K.24).

Conversely, that Cauchy summand has slot action \(\det^b\).
It is fixed by all slot permutations because \(b\) is even.
Restriction to the first \(r\) slots is again \(\det^b\), so
its image under (K.21) lies in the displayed rectangular first
factor. This proves the reverse inclusion and the equality.
The argument works in every dimension; a Schur functor exceeding
the ambient dimension contributes zero on both sides.

### 5. The sharper critical-boundary injection and proof of (K.14)

Now take \(b=r^2-1\). For even \(r\), R-018–R-020 prove that every
constituent \(S_\nu W\) of the common-polarization kernel satisfies

\[
\nu_1\ge r^2+1,\qquad \nu_2\ge r(r-1).
\tag{K.26}
\]

For odd \(r\), those same bounds hold after removing the unique
rectangular summand \(S_{(b^r)}W\), which R-020 proves is in the
kernel. Let \(\mathcal N_r\) denote the common kernel in the even
case, and this complementary sum of isotypic components in the odd
case. The projection to \(\mathcal N_r\) is explicit and natural:
on tensor degree \(rb\), remove the central Schur projector

\[
e_{(b^r)}=
\frac{\dim[(b^r)]}{(rb)!}
\sum_{\sigma\in S_{rb}}\chi^{(b^r)}(\sigma)\sigma
\tag{K.27}
\]

in the odd case; use the identity in the even case. Centrality
makes this projector commute with the tensor symmetrizations
defining the source and the common-polarization map.

For odd \(r\), the composite of (K.22) with this projection can
have kernel only in the intersection (K.24), hence only in
\(S_{(b^a)}W\). Here \(a=r+1\) is even and
\(b=r^2-1=a(a-2)\). R-021 proves that the original canonical map
is nonzero on its multiplicity-one target determinant component.
By (K.2), its annihilator has zero intersection with
\(S_{(b^a)}W\). The composite projection is therefore injective.
In the even case injectivity already follows from (K.22). Thus in
both parities there is the exact natural injection

\[
\boxed{
\mathcal K_{r+1,r^2-1}(W)
\hookrightarrow\mathcal N_r(W)\otimes
\operatorname{Sym}^{r^2-1}W,}
\tag{K.28}
\]

given explicitly by (K.21) and (K.27), whose first factor has only
the types (K.26).

Pieri interlacing (K.23) now forces every annihilator label to have
\(\lambda_1\ge r^2+1\) and
\(\lambda_2\ge r(r-1)\). This is exactly the complement of the
surjectivity range (K.14). The proof removes the rectangular
contraction by its actual prolongation and canonical preimage,
rather than discarding it by a parity assertion.

### 6. Exact integer-interval description of the candidate support

For completeness, pad \(\lambda\) to \(a=r+1\) parts. A partition
\(\nu\vdash rb\) satisfying both (K.26) and the Pieri interlacing
(K.23) exists exactly for the following explicit integer region:

\[
\begin{aligned}
\lambda_1&\ge b+2,\\
\lambda_2&\ge b-r+1,\\
\max(0,b+2-\lambda_2)+\max(0,b-r+1-\lambda_3)
&\le\lambda_1-b.
\end{aligned}
\tag{K.30}
\]

This gives a necessary support region for the canonical annihilator
via (K.28), not an assertion that every label in it occurs.
To prove the equivalence, choose independently
\(\nu_i\in[\lambda_{i+1},\lambda_i]\), \(1\le i\le r\),
raising the first two lower bounds to \(b+2,b-r+1\).
Their individual feasibility is precisely the first two lines.
Ordering is automatic because
\(\nu_i\ge\lambda_{i+1}\ge\nu_{i+1}\). The sum of the lower
bounds is \(ab-\lambda_1\) plus the two maxima in (K.30), and
the sum of the upper bounds is \(ab-\lambda_{r+1}\ge rb\), since
\(\lambda_{r+1}\le b\). Sums of independent integer intervals
fill every integer between their lower and upper sums. Existence
of sum \(rb\) is therefore exactly the last line of (K.30).

For \(r\ge3\), that last inequality follows already from the
first two and the partition size. Here is a complete check, which
prevents counting it as an additional range in those ranks. Set
\(x=\lambda_1-b\), \(y=\lambda_2-b\), and
\(z=\lambda_3-b\). Then

\[
x\ge2,\quad y\ge1-r,\quad z\le y,\quad
x\ge y,\quad x\ge-y-(r-1)z.
\]

The desired inequality is
\(\max(0,2-y)+\max(0,1-r-z)\le x\).
For \(y\ge2,z\ge1-r\), its left side is zero.
For \(y\ge2,z=-q\le-r\), the two lower bounds on \(x\)
give \(x\ge(r-1)q/2\ge q-r+1\).
For \(y\le1,z\ge1-r\), the assertion is \(x+y\ge2\):
this follows from \(x\ge2\) at \(y=0,1\), and from
\(x+y\ge-(r-1)z\ge-(r-1)y\ge r-1\ge2\) at \(y\le-1\).
Finally, for \(y\le1,z=-q\le-r\), the lower bound
\(x\ge(r-1)q-y\) exceeds the required \(q-y-r+3\) by
\((r-2)q+r-3\ge0\). These cases exhaust the integer possibilities.

At \(r=2,b=3\), no such \(\nu\) exists at all: (K.26) would
give \(\nu_1+\nu_2\ge5+2>rb=6\). Thus (K.28) proves that
the full map \(h_{3,3}\) is an isomorphism. This edge case agrees
with the classical result of Hadamard, stated with its complete
proof in Landsberg, *Geometric complexity theory: an introduction
for geometers*, [arXiv:1305.7387v3](https://arxiv.org/pdf/1305.7387),
**Theorem 7.22, §7.8, printed p. 24**. That statement and proof
were independently read here.

## Parameter checks and concrete families

The smallest parameter in (K.13) is \(a=3,r=2,b=3\), where
\(m=b-r=1\), the lower grid map is the identity, and the
power-one injectivity in (K.18) has degree excess one. The critical
second-row range is \(\lambda_2\le1\), and the first-row range
is \(\lambda_1\le4\). The sole nonzero target component in that
first-row band is \((4,4,1)\), by the complement/Specht calculation
of R-020 with \(a=3,H=4\). Thus no unavailable induction base
or negative residual degree is used.

At the critical boundary, the complete first-row target band itself
has a particularly simple description. Applying the same explicit
complementary pairing and multilinear map from R-020 with \(a\)
slots and \(H=b+1\) gives

\[
\bigoplus_{\lambda_1\le b+1}
\left(\operatorname{Sym}^a(\operatorname{Sym}^bV)\right)_\lambda
=
\begin{cases}
S_{((r^2)^r,r^2-r-1)}V,&r\text{ even},\\
S_{((r^2-1)^{r+1})}V,&r\text{ odd}.
\end{cases}
\tag{K.29}
\]

Each displayed component has multiplicity one and is entirely in the
canonical image by (K.14). Examples are \((a,b)=(5,15)\) with
\(\lambda=(16,16,16,16,11)\), and \((a,b)=(7,35)\) with
\(\lambda=(36,36,36,36,36,36,29)\). In even outer degree the
determinant examples are \((a,b)=(4,8),(6,24),(8,48)\), and (K.3)
covers every even \(a\ge4\).

The full canonical map remains governed by the remaining components
in (K.28). The statements above prove the displayed entire isotypic
ranges, without asserting vanishing of the remaining varying
common-polarization kernel.

### Explicit positive ranks on equal-middle-row families

The component surjectivity combines directly with the already proved
T-025 end-shape formula. For every \(a\ge3\), \(r=a-1\),
\(r^2-r+1\le b\le r^2-1\), and
\(0\le\gamma\le\beta\le b-r\), put

\[
\lambda=(ab-(a-2)\beta-\gamma,\beta^{a-2},\gamma),
\qquad R=\beta-\gamma-\binom a2(\beta\bmod2).
\]

This is a partition: its first part is at least
\(ab-(a-1)\beta\ge b+r^2\ge\beta\).
Its second part satisfies the exact range (K.13), and \(b\ge\beta\).
Therefore its actual canonical image multiplicity is

\[
\boxed{
[S_\lambda V:\operatorname{im}h_{b,a}]
=\#\{(c_2,\ldots,c_a)\in\mathbf Z_{\ge0}^{a-1}:
2c_2+3c_3+\cdots+ac_a=R\}.}
\tag{K.31}
\]

For dimensions at least the length of \(\lambda\), this count is
positive exactly for \(R=0\) or \(R\ge2\), because parts two and
three already represent every integer at least two. Negative right
sides and \(R=1\) give zero. Examples are \(a=4,b=7\),
\(\lambda=(20,4,4)\), with image multiplicity two, and
\(a=5,b=13\), \(\lambda=(41,8,8,8)\), with image multiplicity five.
Formula (K.31) records the exact map rank of the known positive
coefficient formula throughout these concrete parameter families.

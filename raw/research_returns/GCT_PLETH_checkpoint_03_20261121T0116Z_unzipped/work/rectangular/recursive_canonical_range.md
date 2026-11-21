# A recursive second-row range for the canonical map

Statement **R-024**. Written and checked on 21 November 2026 UTC by
GPT-6 Astra Pro, agent /root/rectangular_cases; effort setting not exposed.
The canonical degree-five base is the established result of
Cheung–Ikenmeyer–Mkrtchyan and McKay. The component argument below uses
the explicit common-polarization injectivity R-018. No historical
novelty claim is made.

## 1. The unconditional range and its exact map

Let \(V\) be any finite-dimensional vector space over a field of
characteristic zero. For every integer \(a\ge6\), set

\[
C_a=\binom a2-10=5+6+\cdots+(a-1).
\tag{P.1}
\]

For every \(b\ge C_a+6\), and every partition

\[
\lambda\vdash ab,\qquad \lambda_2\le b-C_a,
\tag{P.2}
\]

the canonical map

\[
h_{b,a}:\operatorname{Sym}^{b}(\operatorname{Sym}^{a}V)
\longrightarrow\operatorname{Sym}^{a}(\operatorname{Sym}^{b}V),
\qquad
h_{b,a}(v_1^a\cdots v_b^a)=(v_1\cdots v_b)^a,
\tag{P.3}
\]

is surjective onto the entire target \(\lambda\)-isotypic component.
The assertion includes all multiplicities and all dimensions; a Schur
functor with too many rows evaluates to zero. A missing second part is
zero. Equivalently, the explicit parameter range is

\[
\boxed{
a\ge6,\qquad b\ge\binom a2-4,\qquad
\lambda_2\le b-\binom a2+10.}
\tag{P.4}
\]

For example the ranges for \(a=6,7,8,9\) respectively are

\[
\begin{array}{c|c|c}
a&\text{inner degree}&\text{second row}\\\hline
6&b\ge11&\lambda_2\le b-5\\
7&b\ge17&\lambda_2\le b-11\\
8&b\ge24&\lambda_2\le b-18\\
9&b\ge32&\lambda_2\le b-26.
\end{array}
\tag{P.5}
\]

All symmetric powers in (P.3) use normalized averaging in the tensor
realization. Each averaging projector is self-adjoint for the tensor
pairing. Writing the grid map as target averaging composed with grid
permutation on the source invariant subspace, its transpose is source
averaging composed with the inverse permutation on the target
invariant subspace. This is the opposite grid map, with scalar one.
Therefore, for \(W=V^*\), the image
annihilator is exactly

\[
\mathcal K_{a,b}(W)
=\ker\left[h_{a,b}:\operatorname{Sym}^{a}(\operatorname{Sym}^{b}W)
\longrightarrow\operatorname{Sym}^{b}(\operatorname{Sym}^{a}W)\right].
\tag{P.6}
\]

We prove that its \(\lambda\)-isotypic component is zero in (P.4).
This proves the asserted surjectivity by the perfect symmetric-tensor
pairing, including the map on each multiplicity space.

## 2. The established full degree-five base

The exact input is

\[
\mathcal K_{5,b}(W)=0\qquad\text{for every }b\ge6.
\tag{P.7}
\]

Cheung–Ikenmeyer–Mkrtchyan, *Symmetrizing tableaux and the 5th case of
the Foulkes conjecture*, arXiv:1509.03944v1, **Theorem 6(a), printed
p. 3**, proves injectivity of \(\Psi_{5,6}\). Their displayed definition
on printed p. 2 is the composition of the symmetric-tensor inclusion,
the transpose of the \(5\times6\) tensor grid, and symmetric projection.
It is precisely \(h_{5,6}\) under the convention (P.3). Applying McKay's
propagation theorem to this established base gives (P.7). A complete
primary proof of that propagation is Christian Ikenmeyer, *On McKay's
propagation theorem for the Foulkes conjecture*, arXiv:1509.04957,
**Theorem 1.3, printed p. 2**, with proof in §§2–6, printed pp. 3–8.
Its definition of \(\Psi_{a\times b}\), also on printed p. 2, is the
same inclusion, grid transpose, and projection, so its conclusion
applies to these actual maps. The official full texts are

- <https://arxiv.org/pdf/1509.03944>
- <https://arxiv.org/pdf/1509.04957>.

The source input is injectivity of the precise transpose map in (P.6).
The source computation for
Theorem 6(a) is an exact integer computation described and justified
in §§2–5; its original large evaluation matrices were not regenerated
in this run. The propagation proof was read in full. The scalar audit
in §6 below records the harmless normalization corrections in its
auxiliary raising-operator displays.

The sources work in sufficiently large dimension. Their injectivity
implies (P.7) in every smaller dimension by the actual inclusion
\(W\hookrightarrow W\oplus W'\): both symmetric-power functors preserve
this inclusion, and the grid maps commute with it. A vector in the
smaller kernel would map to a vector in the zero larger kernel. All
maps are rational, so extension to characteristic-zero fields
preserves the assertion.

## 3. An exact intermediate-annihilator morphism

We now construct the map needed for the induction. For every

\[
a=r+1\ge3,\qquad b\ge r,\qquad m=b-r\ge0,
\tag{P.8}
\]

let

\[
\begin{aligned}
\delta:\operatorname{Sym}^{r+1}(\operatorname{Sym}^{b}W)
&\longrightarrow
\operatorname{Sym}^{r}(\operatorname{Sym}^{b}W)
\otimes\operatorname{Sym}^{b}W,\\
w_0\cdots w_r&\longmapsto
\frac1{r+1}\sum_{i=0}^{r}
\left(\prod_{j\ne i}w_j\right)\otimes w_i.
\end{aligned}
\tag{P.9}
\]

Multiplication of the two tensor factors is a left inverse. Thus
\(\delta\) is injective. In the normalized invariant-tensor model it is
the inclusion of fully symmetric tensors into tensors symmetric in
the first \(r\) slots.

The common-polarization map is the coefficient map

\[
T_{r,r,b}f(v_1,\ldots,v_r;x)
=[t_1^r\cdots t_r^r]
f(v_1+t_1x,\ldots,v_r+t_rx).
\tag{P.10}
\]

It has target
\(\operatorname{Sym}^{r^2}W\otimes
\operatorname{Sym}^{r}(\operatorname{Sym}^{m}W)\).
There is an actual restriction of the composite map

\[
\boxed{
\Theta_{a,b}:=(T_{r,r,b}\otimes\mathrm{id})\delta:
\mathcal K_{a,b}(W)\longrightarrow
\operatorname{Sym}^{r^2}W\otimes
\mathcal K_{r,m}(W)\otimes\operatorname{Sym}^{b}W.}
\tag{P.11}
\]

The codomain in (P.11) retains the full lower annihilator. Here is a
complete proof of this membership.

Work over \(\mathbf C\), which suffices because the map is rational.
For \(F\in\mathcal K_{a,b}(W)\), denote its corresponding symmetric
\(a\)-linear form on \(\operatorname{Sym}^{b}V\) by \(\mathcal A_F\).
The kernel condition (P.6) says exactly

\[
\mathcal A_F(P,\ldots,P)=0
\quad\text{for all }P=u_1\cdots u_b.
\tag{P.12}
\]

Fix \(Q=y_1\cdots y_m\). The form
\((x^r+c\,t^r)Q\) is a product of \(b\) linear factors over
\(\mathbf C\): the degree-\(r\) binary factor splits, also when \(x,t\)
are linearly dependent. Take the coefficient of \(c\) in (P.12) and
divide by \(a\). The result is

\[
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{P.13}
\]

Put

\[
G_x(y_1,\ldots,y_m;t)
=\mathcal A_F(x^rQ,\ldots,x^rQ,t^b).
\]

For \(D_{y,t}=y\cdot\partial_t\), ordinary differentiation gives the
exact equation

\[
D_{y_m,t}\cdots D_{y_1,t}G_x
=\frac{b!}{r!}
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{P.14}
\]

Before step \(i\), the degrees in \(t,y_i\) are \(b-i+1,r\).
Their difference is \(m-i+1\ge1\). The operator \(D_{y_i,t}\) is
injective on every such space. To verify the coefficient, put
\(p=b-i+1\), \(q=r\), and decompose under the \(GL_2\) action mixing
\(t,y_i\). A summand containing weight \((p,q)\) has the form
\(\det^j\otimes\operatorname{Sym}^{p+q-2j}\mathbf C^2\), with
\(j\le q<p\). Its weight vector is the determinant factor times
\(e_t^{p-j}e_y^{q-j}\). The ordinary raising operator sends it to
\((p-j)e_t^{p-j-1}e_y^{q-j+1}\) times the same determinant factor,
which is nonzero. This verifies injectivity on every multiplicity
space as well. Equivalently
this is Sra's Lemma 2.1 with power one. All other variables are
spectators. Starting with the last map in the composition and
successively using these injective restrictions gives \(G_x=0\).
For \(m=0\), (P.13) already states \(G_x=0\), with no derivatives;
the degree-zero grid map is the identity of \(\mathbf Q\).

For fixed \(x,t\), the symmetric \(r\)-linear form

\[
(Q_1,\ldots,Q_r)\longmapsto
\mathcal A_F(x^rQ_1,\ldots,x^rQ_r,t^b)
\tag{P.15}
\]

has zero diagonal on every \(Q=y_1\cdots y_m\). By the exact
definition (P.6), with \(a,b\) replaced by \(r,m\), it belongs to
\(\mathcal K_{r,m}(W)\). The coefficient calculation in the original
vector slots is

\[
\Theta_{a,b}F(v_1,\ldots,v_r;x,t)
=\binom br^{r}
\mathcal A_F(x^rv_1^m,\ldots,x^rv_r^m,t^b).
\tag{P.16}
\]

Its degrees in \(x,t\) are \(r^2,b\). Evaluation at all \(x,t\)
separates both symmetric-power spaces. Applying the lower grid map
to the middle factor of (P.16) therefore gives zero as a tensor,
because it gives zero under every such evaluation by (P.15).
This proves precisely the membership (P.11). The factors \(b!/r!\)
and \(\binom br^r\) in (P.14) and (P.16) also fix all normalizations.

## 4. Proof of the recursive component range

Set \(C_5=0\), so that for every \(a\ge6\), with \(r=a-1\),

\[
C_a=r+C_r.
\tag{P.17}
\]

Prove (P.4) by induction on \(a\), using the full base (P.7).
Fix \(a\ge6\), \(b\ge C_a+6\), and a partition \(\lambda\) satisfying
(P.2). Write \(s=b-C_a\ge6\) and \(m=b-r\). Then

\[
m\ge C_r+6,\qquad m-C_r=s,\qquad s\le m.
\tag{P.18}
\]

The last inequality uses \(C_r\ge0\), including \(r=5\).

First restrict (P.9) to the entire \(\lambda\)-isotypic component.
Pieri's rule says that every type \(\nu\) in its first tensor factor
satisfies \(\lambda/\nu\) horizontal of size \(b\), and in particular

\[
\nu_2\le\lambda_2\le s\le m=b-r.
\tag{P.19}
\]

R-018, applied with \(L=r\), proves that \(T_{r,r,b}\) is injective
on every entire \(\nu\)-isotypic component in (P.19). Their direct sum
is therefore an injective restriction too: images of distinct types
lie in distinct isotypic components of its target, and the statement
for one type already includes its full multiplicity space. Tensoring
by \(\operatorname{Sym}^{b}W\) preserves this injectivity. Since
\(\delta\) itself is injective, the composite in (P.11) is injective
on the \(\lambda\)-isotypic component of \(\mathcal K_{a,b}(W)\).

Next consider its codomain in (P.11). At \(r=5\) the middle factor
is zero by (P.7) and \(m\ge6\). At every \(r\ge6\), the induction
statement and (P.18) give

\[
\mathcal K_{r,m}(W)
\subseteq
\bigoplus_{\kappa_2\ge s+1}
\left(\operatorname{Sym}^{r}(\operatorname{Sym}^{m}W)\right)_\kappa.
\tag{P.20}
\]

Tensoring one of these types with the two row representations
\(\operatorname{Sym}^{r^2}W\) and \(\operatorname{Sym}^{b}W\) applies
Pieri twice. Each added horizontal strip only increases row lengths,
so every resulting type \(\xi\) contains \(\kappa\), and
\(\xi_2\ge\kappa_2\ge s+1\). The codomain of (P.11) consequently
has no \(\lambda\)-isotypic component with \(\lambda_2\le s\).

The injective restriction just proved thus maps the specified
\(\lambda\)-component into zero. That component is zero. Equation
(P.6) proves the claimed canonical surjectivity, completing the
induction for every \(a\ge6\).

The proof uses whole isotypic components at both stages and retains
every copy of each Schur functor.

## 5. Explicit positive ranks in the new parameter range

Here is an unconditional family with a closed positive counting
formula. Take the parameters in (P.4), let

\[
0\le\gamma\le\beta\le b-C_a,\qquad
\lambda=(ab-(a-2)\beta-\gamma,\beta^{a-2},\gamma),
\qquad
R=\beta-\gamma-\binom a2(\beta\bmod2).
\tag{P.21}
\]

This is a partition. Its first part is at least
\(ab-(a-1)\beta\ge b+(a-1)C_a\ge\beta\).
The exact end-sector formula T-025 applies, since \(b\ge\beta\).
It computes the target multiplicity as

\[
p_{2,\ldots,a}(R)
=\#\{(c_2,\ldots,c_a)\in\mathbf Z_{\ge0}^{a-1}:
             2c_2+3c_3+\cdots+ac_a=R\}.
\tag{P.22}
\]

The set is empty for negative \(R\). Combining (P.4) with this exact
target multiplicity gives the actual rank on multiplicity spaces:

\[
\boxed{
\operatorname{rank}\operatorname{Hom}_{GL(V)}(S_\lambda V,h_{b,a})
=[S_\lambda V:\operatorname{im}h_{b,a}]
=p_{2,\ldots,a}(R).}
\tag{P.23}
\]

Here \(\dim V\ge\ell(\lambda)\); in smaller dimensions the Schur
functor vanishes. Because \(2,3\) are permitted parts, the number
in (P.22) is positive exactly for \(R=0\) or \(R\ge2\). The
construction \(R=2u\), or \(R=3+2u\), supplies a solution for each
such positive \(R\).

For every \(a\ge6\) and every \(b\ge\binom a2-4\), the specific
partition

\[
\lambda=(ab-6a+12,6^{a-2})
\tag{P.24}
\]

has canonical image multiplicity \(4\), given by the four solutions
of (P.22) at \(R=6\): the partitions \(6\), \(4+2\), \(3+3\), and
\(2+2+2\). In particular \(h_{11,6}\) is surjective onto all four
copies of \(S_{(42,6,6,6,6)}V\) in its target.

## 6. Source-normalization audit

Ikenmeyer's appendix defines its auxiliary tensor raising operator
on degree \(d\) by
\(\phi_{ij}=d^{-1}\sum_{p=1}^{d}\zeta_{ij}^{(p)}\).
Consequently its two-operator composition is exactly

\[
\phi_{ij}\phi_{i'j'}
=d^{-2}\sum_{p\ne q}\zeta_{ij}^{(p)}\zeta_{i'j'}^{(q)};
\tag{P.25}
\]

the printed factor \(1/[d(d-1)]\) on p. 8 needs this correction.
The sum commutes under interchange of the two operators. Removing
fixed tensor positions in §4 changes the remaining raising product
by the nonzero scalar \(((b-1)/b)^{a(b-1)}\). Its injectivity is
unchanged. In the §5 \(GL_2\) weight-vector display, the coefficient
for the degree-\(d\) normalization is \((b-\eta_2)/d\), which is
nonzero in the displayed range. Thus every injectivity step of the
source propagation proof survives with exact scalars. The grid map
itself is fixed by its independent inclusion–permutation–projection
definition, already identified with (P.3).

## 7. One further degree using the exact square kernel

For every \(a\ge6\), at the additional degree

\[
b=\binom a2-5=C_a+5,
\tag{P.26}
\]

the canonical map \(h_{b,a}\) is surjective on every target component
with \(\lambda_2\le4\). This is a separate unconditional boundary
family.

The source input is the exact decomposition in
Cheung–Ikenmeyer–Mkrtchyan, **Theorem 6(b), printed p. 3**, at the
same primary URL in §2:

\[
\begin{aligned}
\mathcal K_{5,5}={}&
S_{(14,7,2,2)}\oplus S_{(13,7,2,2,1)}
\oplus S_{(12,7,3,2,1)}\oplus S_{(12,6,3,2,2)}\\
&\oplus S_{(12,5,4,3,1)}\oplus S_{(11,5,4,4,1)}
\oplus S_{(10,8,4,2,1)}\oplus S_{(9,7,6,3)}.
\end{aligned}
\tag{P.27}
\]

Each summand has second row at least five, so the full degree-five
base has zero kernel on every type with second row at most four.
At an induction step \(a=r+1\ge6\), (P.26) gives
\(m=b-r=C_r+5\ge5\). Thus (P.19) holds with the fixed bound four,
and the composite (P.11) is injective on every such source
component. The induction statement at \(r\) says that the middle
factor \(\mathcal K_{r,m}\) has only labels with second row at least
five; for \(r=5\) this is exactly (P.27). The two Pieri steps in
§4 keep that lower bound. The codomain of (P.11) therefore has no
label with second row at most four, and its injective restriction
has zero source. This proves the new boundary assertion at every
\(a\ge6\).

In particular every \(a\ge6\), with \(b\) as in (P.26), has actual
canonical image multiplicity two at

\[
\lambda=(ab-4a+8,4^{a-2}).
\tag{P.28}
\]

The exact end-sector count is \(p_{2,\ldots,a}(4)=2\), corresponding
to \(4\) and \(2+2\). All parts in (P.28) satisfy the established
row bound, so both target copies are in the canonical image.

## 8. An unconditional triangular profile from the full square bases

For every pair of integers \(a>k\ge6\), the following is an additional
explicit canonical component range:

\[
\boxed{
b\ge\binom a2+\binom{k-1}{2},\qquad
\lambda\vdash ab,\qquad
\lambda_2\le b-\binom a2+\binom k2.}
\tag{P.29}
\]

The map \(h_{b,a}\) is surjective on the entire indicated target
component for every such triple \(a,k,b\).

The exact established lower maps are

\[
\mathcal K_{k,s}(W)=0\qquad
\text{for every }k\ge6,\ s\ge(k-1)^2.
\tag{P.30}
\]

These are the transposes of the surjective grid maps in Sra,
*The q-Foulkes problem III: On Foulkes' conjecture with a graded
inner factor*, v1, **Theorem 1.3**, proved in §2.2 with its
power-polarization Lemma 2.1. The primary text is
<https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>.
The exact conventions and complete proof of this input were already
checked for R-022. Equation (P.30) is a statement about the actual
maps, with no coefficient-only replacement.

Here is the full induction proving (P.29). Fix \(k\ge6\) and
\(s\ge(k-1)^2\). For every \(j\ge k\), put

\[
b_j=s+\binom j2-\binom k2.
\tag{P.31}
\]

At \(j=k\) the annihilator is zero by (P.30). Suppose \(j>k\);
write \(r=j-1\). The exact numerical identities are

\[
b_j-r=b_r\ge s\ge(k-1)^2,\qquad b_j\ge r.
\tag{P.32}
\]

Consider a type \(\lambda\vdash j b_j\) with \(\lambda_2\le s\).
The first tensor-factor labels \(\nu\) in its image under (P.9)
satisfy \(\nu_2\le\lambda_2\le s\le b_r\), by Pieri.
R-018 consequently makes \(T_{r,r,b_j}\) injective on every such
whole \(\nu\)-isotypic component. The composite \(\Theta_{j,b_j}\)
is injective on the original \(\lambda\)-component.

By (P.11), this composite has codomain

\[
\operatorname{Sym}^{r^2}W\otimes
\mathcal K_{r,b_r}(W)\otimes\operatorname{Sym}^{b_j}W.
\tag{P.33}
\]

At \(r=k\) this codomain is zero. For \(r>k\), the induction assertion
states that every label \(\kappa\) of its middle factor has
\(\kappa_2\ge s+1\). Tensoring with either of the displayed row
representations adds a horizontal strip, so every resulting label
still has second row at least \(s+1\). Thus (P.33) has no type
\(\lambda\) under consideration. The injective restriction has zero
domain. This proves zero annihilator on every second row at most
\(s\), at every \(j\ge k\).

Set \(j=a\) in (P.31). Then
\(s=b-\binom a2+\binom k2\); the identity
\[
(k-1)^2-\binom k2=\binom{k-1}{2}
\tag{P.34}
\]
converts the exact base range \(s\ge(k-1)^2\) into the first
inequality in (P.29). This proves all the stated parameters.

For a concrete comparison within the proved families, at \(a=8\)
the base-five assertion begins at \(b=24\) and gives
\(\lambda_2\le b-18\). Formula (P.29) with \(k=6\) begins at
\(b=38\) and gives \(\lambda_2\le b-13\); with \(k=7\) it begins
at \(b=43\) and gives \(\lambda_2\le b-7\).
Every assertion refers to the same specified map \(h_{b,8}\).
In particular \(h_{38,8}\) is surjective on every component with
\(\lambda_2\le25\).

## Check status

The proof of (P.11)–(P.20), the base-map identification, and all
endpoint inequalities were checked in this run. The parent agent
will record its independent reading separately. The original
degree-five computational theorem is used with the source status
stated in §2; it is not represented as a replayed calculation.

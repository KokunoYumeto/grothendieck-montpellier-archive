# Canonical-map ranges linear in the outer degree at fixed second row

## R-034. The actual annihilator injection and unconditional ranges

All vector spaces are over a characteristic-zero field. For
\(a,b\ge1\), use the normalized grid map

\[
h_{b,a}:\operatorname{Sym}^{b}(\operatorname{Sym}^{a}V)
\longrightarrow\operatorname{Sym}^{a}(\operatorname{Sym}^{b}V).
\tag{LP.1}
\]

Every whole target \(\lambda\)-isotypic component is reached in
the following two families, with all its multiplicities:

\[
\boxed{a\ge2,\quad t\ge1,\quad b\ge t(a-1),\quad
\lambda\vdash ab,\quad\lambda_2\le t.}
\tag{LP.2}
\]

For the stronger degree-five profile, put

\[
B_t=
\begin{cases}
1,&t=1,\\
5,&2\le t\le4,\\
6,&t=5,\\
t,&t\ge6,
\end{cases}
\qquad
C_{a,t}=\sum_{r=5}^{a-1}\min\{r,t\}.
\tag{LP.3}
\]

Then the second family is

\[
\boxed{a\ge6,\quad t\ge1,\quad b\ge C_{a,t}+B_t,\quad
\lambda\vdash ab,\quad\lambda_2\le t.}
\tag{LP.4}
\]

In particular, the following are explicit uniform subfamilies of
(LP.4):

| Second-row bound | Every outer degree | Inner-degree range |
|---|---|---|
| \(\lambda_2\le1\) | \(a\ge6\) | \(b\ge a-4\) |
| \(\lambda_2\le2\) | \(a\ge6\) | \(b\ge2a-5\) |
| \(\lambda_2\le3\) | \(a\ge6\) | \(b\ge3a-10\) |
| \(\lambda_2\le4\) | \(a\ge6\) | \(b\ge4a-15\) |
| \(\lambda_2\le5\) | \(a\ge6\) | \(b\ge5a-19\) |
| \(\lambda_2\le t,\ t\ge6\) | \(a\ge6\) | \(b\ge t(a-4)\) |

For \(t\ge6\) the capped sum in (LP.3) improves the last
displayed sufficient bound and has the exact closed form

\[
C_{a,t}+t=
\begin{cases}
\binom a2-10+t,&6\le a\le t+1,\\
ta-\binom t2-10,&a\ge t+1.
\end{cases}
\tag{LP.5}
\]

The two expressions agree at \(a=t+1\). Thus for fixed
\(t\), the asserted threshold grows linearly with \(a\).
For example \(t=6\) gives \(b\ge6a-25\) for every
\(a\ge7\), together with \(b\ge11\) at \(a=6\).

The proof below establishes an exact common-polarization morphism
on the prescribed second-row band. It uses the already proved
arbitrary-power theorem R-018 and the actual canonical bases
checked in R-031; it does not infer map ranks from a comparison of
source and target dimensions. No historical novelty claim is made.

## 1. Exact kernels of one directional derivative

Let \(W\) be the space of polynomial generators for vector
variables \(y,z\), and put

\[
D_{z,y}=\sum_i z_i\frac{\partial}{\partial y_i}.
\]

On bidegree \((p,q)\), this is an actual equivariant map

\[
D_{z,y}:\operatorname{Sym}^{p}W\otimes\operatorname{Sym}^{q}W
\longrightarrow\operatorname{Sym}^{p-1}W
                  \otimes\operatorname{Sym}^{q+1}W.
\tag{LP.6}
\]

For \(p\ge1\), its exact kernel is

\[
\boxed{
\ker D_{z,y}=
\begin{cases}
0,&p>q,\\
S_{(q,p)}W,&1\le p\le q.
\end{cases}}
\tag{LP.7}
\]

Here the last space is its Cauchy summand inside the source.
To verify both the summand and the map, realize the source as the
weight \((p,q)\) part of
\(\operatorname{Sym}^{p+q}(W\otimes\mathbb Q^2)\).
The Cauchy decomposition, obtained by the commuting Young
projectors on the tensor factors, is

\[
\bigoplus_{j=0}^{\min(p,q)}
S_{(p+q-j,j)}W\otimes
 \left(\det^j\otimes
       \operatorname{Sym}^{p+q-2j}\mathbb Q^2\right)_{(p,q)}.
\tag{LP.8}
\]

The indicated weight line is the determinant factor times
\(e_y^{p-j}e_z^{q-j}\). The operator in (LP.6) is exactly
the Lie-algebra operator \(e_z\partial_{e_y}\) on that
factor, and sends this vector to

\[
(p-j)\det^j e_y^{p-j-1}e_z^{q-j+1}.
\tag{LP.9}
\]

It is nonzero for every \(j<p\); the only vanished line is
\(j=p\le q\), giving precisely (LP.7). This proves the
kernel including all multiplicities and all small dimensions;
an overly long Schur functor is simply zero.

Now tensor (LP.6) with the polynomial spaces in any other vector
variables, at their actual fixed multidegrees. Such a spectator
space is a tensor product of symmetric powers of \(W\).
The kernel tensors with that same space, since the operator is
\(D_{z,y}\otimes1\). Successive Pieri decompositions show
that every constituent of
\(S_{(q,p)}W\) tensored with the spectator space contains the
diagram \((q,p)\), and therefore has second row at least
\(p\). In particular, for every fixed band \(\eta_2\le t\),
all such maps with \(p>t\) are injective on the entire band,
even when \(p\le q\). This is a consequence of the exact
kernel (LP.7) and the literal tensoring map, with no discarded
spectator factors.

## 2. Freeing one argument with an arbitrary whole power

Let \(r,t\ge1\), put

\[
L\ge\min\{r,t\},\qquad b\ge L+t,\qquad m=b-L\ge t\ge1.
\tag{LP.10}
\]

Write \(\mathcal K_{s,d}(W)=\ker h_{s,d}(W)\), and use a
superscript \(\le t\) for its entire second-row band.
These are the actual image annihilators, by the scalar-one
pairing identity in R-031 (OF.6).

Define the same normalized contraction as before,

\[
\delta(w_0\cdots w_r)=\frac1{r+1}\sum_i
  \left(\prod_{j\ne i}w_j\right)\otimes w_i,
\]

and use the arbitrary-power common polarization

\[
T_{r,L,b}f(v_1,\ldots,v_r;x)
=[z_1^L\cdots z_r^L]
  f(v_1+z_1x,\ldots,v_r+z_rx).
\tag{LP.11}
\]

The following is an actual injective restriction of their
composite:

\[
\boxed{
\Theta^{(L)}_{r+1,b}:=(T_{r,L,b}\otimes1)\delta:
\mathcal K_{r+1,b}^{\le t}(W)
\hookrightarrow
\operatorname{Sym}^{rL}W\otimes
\mathcal K_{r,m}^{\le t}(W)\otimes\operatorname{Sym}^{b}W.}
\tag{LP.12}
\]

First prove membership in the lower kernel. Let \(F\) be a
vector in a complete \(\lambda\)-isotypic component of
\(\mathcal K_{r+1,b}\), with \(\lambda_2\le t\), and
let \(\mathcal A_F\) be its corresponding symmetric
\((r+1)\)-linear form on \(\operatorname{Sym}^bV\).
For \(Q=y_1\cdots y_m\), the form
\((x^L+c z^L)Q\) splits into \(b\) linear factors over
\(\mathbb C\). Coefficient extraction in its diagonal
vanishing gives

\[
\mathcal A_F(x^LQ,\ldots,x^LQ,z^LQ)=0,
\tag{LP.13}
\]

with \(r\) copies of the first argument; the extracted
coefficient is \(r+1\) times this expression.
Set

\[
G_F(x,y_1,\ldots,y_m,z)
=\mathcal A_F(x^LQ,\ldots,x^LQ,z^b).
\tag{LP.14}
\]

This construction is a \(GL(V)\)-equivariant polynomial map
of \(F\), so its image belongs to the same whole
\(\lambda\)-isotypic component. All variables in (LP.14)
remain independent while taking derivatives. The exact identity
is

\[
D_{y_m,z}\cdots D_{y_1,z}G_F
=\frac{b!}{L!}
\mathcal A_F(x^LQ,\ldots,x^LQ,z^LQ)=0.
\tag{LP.15}
\]

Before the \(i\)-th derivative, the exchanged bidegrees in
\((z,y_i)\) are \((p,q)=(b-i+1,r)\).
The other variables have nonnegative fixed polynomial degrees:
\(rL\) in \(x\), \(r+1\) in previously used \(y\)'s,
and \(r\) in unused \(y\)'s. In particular they are exactly
the spectator factors of §1. Also \(p\ge L+1\).

There are two exhaustive parameter cases. For \(L\ge r\),
\(p\ge L+1>q\), so (LP.7) gives full injectivity.
For \(t\le L<r\), \(p\ge L+1\ge t+1\); (LP.7) and the spectator
Pieri argument give injectivity on the whole
\(\lambda_2\le t\) band. These operators are equivariant,
so every intermediate image remains in that band. Starting with
the last derivative in (LP.15) and successively using these
injective restrictions proves \(G_F=0\).

For every fixed \(x,z\), the symmetric \(r\)-linear form
\(\mathcal A_F(x^LQ_1,\ldots,x^LQ_r,z^b)\) therefore has
zero diagonal on every product of \(m\) linear factors.
This is exactly the defining lower-kernel condition
\(\mathcal K_{r,m}\), without replacing the specified
canonical map. In vector slots the normalized composite is

\[
\Theta^{(L)}F(v_1,\ldots,v_r;x,z)
=\binom bL^r\mathcal A_F
 (x^Lv_1^m,\ldots,x^Lv_r^m,z^b).
\tag{LP.16}
\]

Evaluation at all \(x,z\) separates its symmetric-power
factors, proving tensor membership in
\(\operatorname{Sym}^{rL}W\otimes\mathcal K_{r,m}W
\otimes\operatorname{Sym}^bW\). Any lower type \(\eta\)
contributing to a type \(\lambda\) in this tensor product
is contained in \(\lambda\), by two Pieri steps. Thus
\(\eta_2\le\lambda_2\le t\), proving precisely the
codomain band in (LP.12).

## 3. Injectivity of the arbitrary-power common polarization

The needed statement of R-018 is its full arbitrary-power
formula, not a specialization to \(L=r\): for
\(b\ge L\ge0\), the map (LP.11) is injective on every
whole \(\nu\)-isotypic component with
\(\nu_2\le b-L\). We recall its actual inverse argument
to verify this dependence on \(L\).

Use coordinates \(X_{ji}\) on the \(r\) slots and put
\(x_i=X_{1i}\). Every highest polynomial of row weight
\(\nu\) is a linear combination of products of initial-row
flag minors. There are exactly \(\nu_2\) factors of
height at least two in each homogeneous product. Each minor
uses a slot at most once. Hence, after setting \(x_i=1\),
the highest polynomial \(P\) has degree at most
\(\nu_2\) in each remaining slot block. Separate
homogenization of degree \(b\) in each slot is the inverse
of this evaluation.

At common vector \(e_1\), (LP.11) sends a monomial of
block degrees \(d_i\) to the same monomial, homogenized to
degree \(b-L\), times exactly

\[
\prod_{i=1}^r\binom{b-d_i}{L}.
\tag{LP.17}
\]

For \(d_i\le\nu_2\le b-L\), these are nonzero integers,
and division by their product is an explicit inverse on this
polynomial subspace. Thus no nonzero highest vector in the
specified component can be killed. Equivariance then proves
injectivity on its entire multiplicity space. The flag-minor
generation and separate homogenization proof are given in full
in R-018 (R018.5)–(R018.13); their displayed formulas allow
every \(L\), including the boundary \(b-L=\nu_2\).

After \(\delta\), each first-factor type \(\nu\) for
a source type \(\lambda\) satisfies \(\nu_2\le
\lambda_2\le t\), by Pieri. By (LP.10), \(t\le m=b-L\),
so (LP.17) makes \(T_{r,L,b}\) injective on all these
components. Multiplication is a left inverse of \(\delta\).
Consequently their composite is injective on the complete
second-row band. Together with §2 this proves (LP.12).

## 4. Iteration from the two exact bases

For (LP.2), use \(L=t\) at every step, including steps
with \(t>r\). The membership proof in §2 still applies:
\(L=t\ge r\) gives \(p\ge L+1>r\) and full derivative
injectivity. All other formulas are unchanged. Starting at
outer degree \(a\) and inner degree \(b\), the lower
inner degree at outer degree \(s\) is

\[
b_s=b-t(a-s),\qquad b_2\ge t.
\tag{LP.18}
\]

At each step \(s\ge3\), \(b_s-t=b_{s-1}\ge t\ge1\).
Thus every restriction (LP.12) is injective. The actual
degree-two canonical map \(h_{b_2,2}\) is surjective for
every \(b_2\ge1\), by Sra's Theorem 1.3 at \(a=2\),
whose bound is \((2-1)^2=1\). Its transpose has zero
kernel \(\mathcal K_{2,b_2}\). Iterating the actual
injections therefore gives \(\mathcal K_{a,b}^{\le t}=0\),
proving (LP.2) through the scalar-one adjoint pairing.

For (LP.4), write \(s=b-C_{a,t}\ge B_t\ge t\), and
set

\[
b_q=s+\sum_{r=5}^{q-1}\min\{r,t\}
\qquad(5\le q\le a).
\tag{LP.19}
\]

At the step from \(q=r+1\) to \(r\), take
\(L=\min\{r,t\}\). Then \(b_{r+1}-L=b_r\ge s\ge t\ge1\),
so all the maps (LP.12) are defined and injective. They compose,
with only tensor-factor permutations, to

\[
\mathcal K_{a,b}^{\le t}(W)\hookrightarrow
\mathcal K_{5,s}^{\le t}(W)\otimes
\bigotimes_{r=5}^{a-1}
 \left(\operatorname{Sym}^{r\min(r,t)}W
       \otimes\operatorname{Sym}^{b_{r+1}}W\right).
\tag{LP.20}
\]

The total degree is correct since
\((r+1)b_{r+1}-r b_r=r\min(r,t)+b_{r+1}\).
The precise base vanishing is

\[
\mathcal K_{5,s}^{\le t}=0\qquad(s\ge B_t).
\tag{LP.21}
\]

For \(t=1\), this follows from the identity at \(s=1\),
the complete exact R-031 tables at \(s=2,3,4\), the
eight degree-five kernel labels (all having second row at
least five), and full injectivity for \(s\ge6\).
For \(2\le t\le4\), the same eight labels give the base
at \(s=5\), and every larger degree is injective.
For \(t=5\), use full injectivity at every \(s\ge6\).
For \(t\ge6\), every \(s\ge B_t=t\) lies in that same
full-injectivity range. These are precisely the established
canonical results and primary locators proved and checked in
R-031, including Cheung–Ikenmeyer–Mkrtchyan Theorem 6 and
the complete McKay propagation proof. Thus the codomain in
(LP.20) is zero, proving (LP.4).

All operators are rational and all nonzero scalars are
explicit in (LP.9), (LP.15), (LP.16) and (LP.17). The
arguments over \(\mathbb C\) therefore prove the same
rank statements over every characteristic-zero field.
Zero-dimensional spaces have zero positive-degree targets;
in dimension one the map sends its pure-power basis to the
corresponding pure-power basis, with scalar one. This also
checks the low-dimensional endpoints directly.

## 5. A literal boundary check for the injectivity requirement

The bound \(b-L\ge t\) in (LP.10) is used by the
explicit inverse (LP.17). The following actual example
checks that it cannot simply be deleted from (LP.12).
Take four slots in a four-dimensional space, let
\(D=\det(v_1,v_2,v_3,v_4)\), let \(x_i\) be their first
coordinates, and set

\[
F=D^2x_1x_2x_3x_4.
\tag{LP.22}
\]

It is a nonzero slot-symmetric highest polynomial of
separate degree three and weight \((6,2,2,2)\).
The target of \(h_{4,3}\) has at most three rows by
its inclusion in \((\operatorname{Sym}^4W)^{\otimes3}\)
and Pieri, so this vector belongs to \(\mathcal K_{4,3}\).
For \(r=3,L=t=2,b=3\), substitute
\(v_i\mapsto v_i+z_i x\) in the first three slots.
The determinant is linear in \(z_1,z_2,z_3\) jointly,
because any term using the same common column twice
vanishes. Its square has total \(z\)-degree at most two,
and the first-coordinate product contributes at most three.
Thus the coefficient of \(z_1^2z_2^2z_3^2\) is zero.
The composite kills the nonzero vector (LP.22) here,
where \(b-L=1<t\). This validates the role of the stated
range and does not assert a classification outside it.

## Primary inputs and proof scope

The annihilator diagonal and normalized tensor transpose
are written in R-024 and R-031. The directional-kernel
calculation (LP.6)–(LP.9) and its spectator restriction are
proved here. The common-polarization input is the complete
arbitrary-power R-018 (R018.1)–(R018.13), reread for this
proof. The external degree-two input is Suvrit Sra,
*The q-Foulkes problem III: On Foulkes’ conjecture with a
graded inner factor*, v1, Theorem 1.3, p.2 and proof §2.2:
<https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>.
The degree-five inputs and their exact source maps are
Cheung–Ikenmeyer–Mkrtchyan, Theorem 6,
<https://arxiv.org/pdf/1509.03944>, and Ikenmeyer,
Theorem 1.3 and full §§2–6 propagation proof,
<https://arxiv.org/pdf/1509.04957>.
Their computational and source-review scopes are recorded
separately in R-031 and the check ledger.

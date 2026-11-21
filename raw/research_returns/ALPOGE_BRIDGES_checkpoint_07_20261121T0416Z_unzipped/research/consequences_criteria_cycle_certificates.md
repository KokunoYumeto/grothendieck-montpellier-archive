# Finite algebraic certificates for abelian-sector membership

The criterion CC-XC02 was stated using the image of an $E$-valued
cycle-class map. The following results replace its positive witnesses by
rational cycles with a finite verifier using intersection numbers. They
also show that this membership condition is independent of the prime
$\ell\ne p$. The search supplied below is one-sided: it halts exactly on
positive instances. It supplies neither a bound on the necessary cycle
degrees nor a decision procedure for negative instances.

Use the rational homological category defined by the kernel of the
$\ell$-adic cycle class, its $E$-coefficient counterpart from CC-XC02,
and the established abelian--Artin--Tate category $\mathcal A_q$. The
latter's realization theorem is the inspected input AQ.15. An
isomorphism of an arbitrary numerical motive is not assumed to have a
realization before it is constructed.

## CC-XC05: a finite determinant verifier from intersection traces

Let $k=\mathbb F_q$, with characteristic $p$, and let $X/k$ be smooth
projective and geometrically integral of dimension $d$. Write
$$P_i(t)=\det(t-F_X\mid H^i(X_{\bar k},\mathbb Q_\ell))
       \in\mathbb Z[t],\qquad b_i=\deg P_i.
                                                        \tag{CC-XC.10}$$
These polynomials are independent of $\ell\ne p$. They can be computed
from the equations of $X$. Here $F_X$ denotes the Frobenius
correspondence with the usual Weil eigenvalues, as in CC-XC01.

A candidate certificate consists of finitely many abelian varieties or
finite étale $k$-schemes $Y_\nu$, integers $n_\nu$, and rational cycles
$$\begin{split}
 f_\nu&\in\mathrm{CH}^{d+n_\nu}(X\times Y_\nu)_{\mathbb Q},\\
 g_\nu&\in\mathrm{CH}^{\dim Y_\nu-n_\nu}
                                  (Y_\nu\times X)_{\mathbb Q}.
 \end{split}                                            \tag{CC-XC.11}$$
The cycles are supplied as finite rational linear combinations of
subvarieties, rather than as unspecified equivalence classes. A negative
codimension supplies only the zero cycle. They define morphisms
$$f:h(X)\longrightarrow T=\bigoplus_\nu h(Y_\nu)(n_\nu),
 \qquad g:T\longrightarrow h(X),\qquad a=gf.
                                                        \tag{CC-XC.12}$$
The composition $a$ has degree zero on $X$.

There is a finite algorithm computing a rational number
$\mathfrak D_X(f,g)$ such that, for every $\ell\ne p$,
$$\mathfrak D_X(f,g)
       =\prod_i\det\!\left(a\mid
                         H^i(X_{\bar k},\mathbb Q_\ell)\right).
                                                        \tag{CC-XC.13}$$
Consequently its nonvanishing is independent of $\ell$. The algorithm
uses the zeta function of $X$, rational polynomial arithmetic and
finitely many intersection numbers of explicitly described cycles. It
needs neither a test for homological equivalence nor an algorithm for
computing an $\ell$-adic cycle-class map.

#### Complete proof and verifier.

Poonen, Testa, and van Luijk (2015), Proposition 8.1, author-manuscript
p. 10, computes $Z(X,t)$ unconditionally over a finite field. Their
proof uses Katz's computable upper bound for the sum of Betti numbers,
counts points over finitely many extensions and reconstructs the
resulting rational function. Deligne's Theorem 1.6 (1974, p. 276) puts
the roots in distinct absolute-value classes according to $i$. Thus the
rational zeta function determines each $P_i$, not merely their
alternating product. This is the same separation used in
Poonen--Testa--van Luijk, Proposition 8.2, p. 10. Factoring over
$\mathbb Q$ and distinguishing the finitely many possible root absolute
values is a finite calculation.

Discard indices with $b_i=0$ for the moment. The polynomials $P_i$ are
pairwise coprime: roots in different degrees have absolute values
$q^{i/2}$ and therefore cannot coincide. By the Chinese remainder
algorithm choose $u_i(t)\in\mathbb Q[t]$ with
$$u_i\equiv1\pmod {P_i},\qquad
 u_i\equiv0\pmod {P_j}\quad(j\ne i).$$ Define the explicit rational
correspondence $$\pi_i=u_i(F_X).
                                                        \tag{CC-XC.14}$$
Cayley--Hamilton for the full characteristic polynomial $P_j$, including
its multiplicities, shows that $\pi_i$ acts as the identity on $H^i$ and
as zero on every other degree. This argument permits arbitrary Jordan
blocks. Neither Frobenius semisimplicity nor idempotence modulo rational
equivalence is being assumed. The existence of these common algebraic
Künneth projectors is the classical Katz--Messing Theorem 2 (1974,
p. 76). The explicit CRT calculation here fixes the rational cycles used
by the verifier.

We record the trace calculation including its sign. For any rational
degree-zero correspondence $c$ on $X$, Poincaré duality, Künneth and the
compatibility of cycle classes with products and degrees give
$$\deg(\Delta_X\cdot c)
                  =\sum_j(-1)^j\operatorname{Tr}(c\mid H^j(X)).
                                                        \tag{CC-XC.15}$$
One can see the formula directly. For each $j$, choose a basis $e_{j,s}$
of $H^j$, with dual classes $e^\vee_{j,s}\in H^{2d-j}(d)$ normalized by
$\int_X e_{j,s}\cup e^\vee_{j,t}=\delta_{st}$. Under Künneth, the
correspondence class is $\sum_{j,s}e^\vee_{j,s}\otimes c(e_{j,s})$.
Pulling back to the diagonal and integrating gives
$$\sum_{j,s}\int_X e^\vee_{j,s}\cup c(e_{j,s})
                    =\sum_j(-1)^j\operatorname{Tr}(c\mid H^j).$$ The
last sign is graded commutativity. Degree compatibility identifies the
integral with the intersection number on the left of (CC-XC.15). The
underlying diagonal and degree identities, with these signs, are also
given in Stacks Project, Lemma 45.9.7, Tag 0FHH, and Lemma 45.10.3,
Tag 0FHR. Thus the calculation applies to rational cycles and requires
no isolated-fixed-point or transversality hypothesis on the original
correspondence.

For $1\le r\le b_i$, compute
$$s_{i,r}=(-1)^i\deg\bigl(\Delta_X\cdot(\pi_i\circ a^r)\bigr)
                         \in\mathbb Q.                  \tag{CC-XC.16}$$
Equation (CC-XC.15) and the projector action show that these are exactly
$\operatorname{Tr}(a_i^r)$, where $a_i$ denotes the action of $a$ on
$H^i$. Starting with $e_{i,0}=1$, use Newton's recursion $$m e_{i,m}=
      \sum_{r=1}^{m}(-1)^{r-1}e_{i,m-r}s_{i,r},
                 \qquad 1\le m\le b_i.                 \tag{CC-XC.17}$$
The result is $e_{i,b_i}=\det(a_i)$. For $b_i=0$, set this determinant
equal to one. Their product is the required $\mathfrak D_X(f,g)$. This
proves (CC-XC.13), including independence of $\ell$.

Every operation in this verifier is finite and algebraic. Composition of
correspondences uses pullback, intersection and proper pushforward on
products. Intersection numbers are computable by Poonen--Testa--van
Luijk, Lemma 8.7, p. 11: move a cycle by an enumerated rational
equivalence to a proper transverse intersection and compute its degree.
Their Remark 8.18, p. 14, records the same effective intersection
operation in the Chow ring. Applied successively on the smooth
projective products, this computes a representative for each required
composition, or equivalently the degree of the corresponding iterated
intersection. Rational coefficients are handled by clearing denominators
and bilinearity. Pullbacks along product projections and proper
pushforwards of the resulting cycles are computable from their defining
ideals and generic degrees. If a product has several geometric
components, these operations can instead be made after a finite
extension splitting the components, computing degrees over that
extension. Such a degree equals the original degree over the ground
field. If cycles are instead returned by proper trace, that pushforward
multiplies degrees by the extension degree, which must then be divided
out. These are equivalent ways to perform the computation. No bound on
the time required for the moving search is claimed, but the cited lemma
proves its termination. $\square$

## CC-XC06: rational certificates, prime independence and an actual summand

For $X$ as above, the following conditions are equivalent.

1.  For some $\ell\ne p$, the $E=\overline{\mathbb Q}_\ell$ homological
    motive $h_{\ell,E}(X)$ satisfies the equivalent conditions of
    CC-XC02.

2.  There is a rational candidate (CC-XC.11) with
    $\mathfrak D_X(f,g)\ne0$.

3.  There is such a candidate and rational correspondence formulas
    defining a splitting $$h_{\ell,\mathbb Q}(X)\longrightarrow T
                      \longrightarrow h_{\ell,\mathbb Q}(X)$$ whose
    composite is the identity, simultaneously for every $\ell\ne p$.

When they hold, one rational numerical motive $M\in\mathcal A_q$, given
by a rational idempotent on $T$, is isomorphic to $h_{\mathrm{num}}(X)$;
the same cycle formulas give its homological realization as $h(X)$ for
every $\ell\ne p$. In particular CC-XC02 is independent of the initially
selected prime and coefficient extension. This is a statement modulo
homological or numerical equivalence, not a lift of the idempotent to
Chow motives.

#### Complete proof.

Suppose (1). An object of $\mathcal A_{q,E}$ is a summand of a finite
$T_E$ as in (CC-XC.12). Compose an isomorphism from $h_{\ell,E}(X)$ with
its inclusion into $T_E$, and compose the corresponding projection with
the inverse isomorphism. This gives $E$-linear algebraic correspondences
$f_E,g_E$ with $$g_E f_E=1
                                                        \tag{CC-XC.18}$$
in the $E$-homological category. Each is a finite $E$-linear combination
of rational cycles. Choose finite lists $f_1,\ldots,f_u$ and
$g_1,\ldots,g_v$ of such rational cycles, preserving the finitely many
components and codimensions in (CC-XC.11), and form
$$f(\mathbf x)=\sum_jx_jf_j,\qquad
 g(\mathbf y)=\sum_ky_kg_k.$$ Composition and the traces in (CC-XC.16)
are polynomial in the variables. Newton's recursion uses only rational
coefficients. Therefore $$D(\mathbf x,\mathbf y)
               =\mathfrak D_X(f(\mathbf x),g(\mathbf y))
                         \in\mathbb Q[\mathbf x,\mathbf y].
                                                        \tag{CC-XC.19}$$
At the $E$-coefficients of (CC-XC.18) every determinant equals one, so
$D$ is not the zero polynomial. A nonzero polynomial over the infinite
field $\mathbb Q$ cannot vanish on every rational tuple: induction on
the number of variables proves this from the finite number of roots of a
one-variable polynomial. Choose a rational tuple at which $D\ne0$. It
supplies (2). This argument concerns actual finite cycle combinations
and their intersection traces; it does not assume injectivity of a
scalar-extension map on rational homological Hom spaces.

Suppose (2), and let $a=gf$. The recursion in CC-XC05 also computes the
rational characteristic polynomial $$\chi(t)=\prod_i\det(t-a_i)
        =t^N+c_1t^{N-1}+\cdots+c_N\in\mathbb Q[t],
        \qquad N=\sum_i b_i,\quad c_N\ne0.$$ The same polynomial is
obtained for every $\ell\ne p$. Set $$v(t)=-c_N^{-1}
        (t^{N-1}+c_1t^{N-2}+\cdots+c_{N-1}).$$ Then
$t v(t)=1-c_N^{-1}\chi(t)$. Cayley--Hamilton gives $$a\,v(a)=v(a)\,a=1
                                                        \tag{CC-XC.20}$$
after every such realization, hence in each rational homological
category. Define the rational cycle formulas
$$j=f,\qquad r=v(a)g,\qquad e=jr.
                                                        \tag{CC-XC.21}$$
They satisfy $rj=1$ and $e^2=e$ in all those categories, and give
$h(X)\simeq(T,e)$. This proves (3). The same identities hold modulo
numerical equivalence, because homologically trivial rational cycles are
numerically trivial by compatibility with intersection degrees. Thus the
rational numerical projector $e$ on the abelian--Artin--Tate object $T$
defines $M=(T,e)\in\mathcal A_q$ and the same $j,r$ give
$h_{\mathrm{num}}(X)\simeq M$. Within this established sector numerical
and homological equivalence agree, so its realization is precisely the
already exhibited summand for every $\ell$. This constructs, rather than
presupposes, the realization needed for this particular numerical
object.

Finally, (3) makes $h_{\ell,E}(X)$ an abelian-sector summand for every
$\ell$, and therefore implies (1) by CC-XC02. All implications are
proved. $\square$

#### All-prime consequence for products.

For a certified $X$, every finite base extension and every product
$X^m\times A\times S$, with $A$ abelian and $S$ finite étale, has
semisimple Frobenius, surjective rational Tate cycle maps in every
codimension, and numerical equivalence equal to $\ell$-adic homological
equivalence for every $\ell\ne p$. Indeed, apply the same base-change
and tensor constructions to (CC-XC.21), and apply AQ.15 in its abelian
sector. The scalar descent and invariant complementary-pairing argument
are exactly those fully proved in CC-XC04, now applicable to every prime
by the common certificate. No crystalline assertion is added here.

## CC-XC07: an exact one-sided search for certificates

There is an algorithm on equations for $X/k$ which halts if and only if
the equivalent conditions of CC-XC06 hold. When it halts it returns the
finitely many varieties, rational cycles and nonzero rational
determinant of a certificate, together with the splitting formulas
(CC-XC.20)--(CC-XC.21). Each returned certificate can be checked by an
independent finite computation. If membership fails, the search runs
forever and makes no negative declaration.

#### Complete proof.

Finite projective models and cycles over a finite field have enumerable
encodings by homogeneous polynomial ideals and finite integer or
rational coefficient lists; this is the encoding used in
Poonen--Testa--van Luijk, §7.1, pp. 6--7. Enumerate projective models
with explicit smooth, geometrically connected commutative group
structures, including identity, inverse and multiplication on finite
affine covers. The defining equations, smoothness, geometric
connectedness, covers and group identities admit finite algebraic
verification. The verified models are abelian varieties, and every
abelian variety over $k$ has one such finite presentation. For the
connectedness test one may compute $H^0(Y,\mathcal O_Y)$: for a nonempty
smooth projective $Y$ it equals $k$ precisely when $Y$ is geometrically
connected. This finite-dimensional algebra, smoothness and equalities of
the specified morphisms can be computed from projective and affine
equations. Also enumerate $\operatorname{Spec}\mathbb F_{q^s}$ and
finite disjoint unions thereof, all finite lists of the verified models,
and all integers $n_\nu$.

For each such $T$, enumerate all finite combinations of subvarieties in
the two codimensions (CC-XC.11). Dimension and containment are decidable
by polynomial ideal computation. Apply the terminating verifier CC-XC05
to every resulting candidate, scheduling the enumerations and
calculations so every candidate eventually receives its finite required
computation. For example, dovetail all the finitely encoded tasks.
Accept and return the first nonzero determinant. Only exact rational
equalities and inequalities enter the acceptance test.

If the search accepts, CC-XC06 supplies the claimed splitting and
membership, so there are no false positives. If membership holds,
CC-XC06 supplies a finite rational certificate. Its models and cycles
eventually occur in the enumeration, and its verifier terminates with a
nonzero determinant. Thus the search eventually halts. Multiplying each
of $f,g$ by a common nonzero integer scales $a$ by a nonzero integer and
preserves nonvanishing, so even integral cycle coefficient lists suffice
for the search.

The twists cause no hidden infinite operation within one candidate. The
displayed codimensions already account for them: $f_\nu$ shifts
cohomological degree by $2n_\nu$, $g_\nu$ shifts it back, and $a=gf$ has
degree zero. Alternatively, choose one integer $m\ge\max(0,n_\nu)$,
tensor both source and target by $\mathbb Q(-m)$, and use the usual
Lefschetz projector on each of finitely many copies of $\mathbb P^1$.
This realizes every remaining twist $n_\nu-m\le0$ and the source twist
$-m$ as summands of ordinary effective motives by finitely many cycle
operations. For the unshifted $h(X)$ considered here, one may even
restrict the search to $n_\nu=0$: CC-XC01 supplies an effective finite
abelian/Artin target whenever CC-XC02 holds. Hence this restriction does
not change which inputs cause the search to halt. $\square$

#### General smooth projective schemes.

The statements extend to a nonempty smooth projective scheme by treating
its finitely many connected components; components of different
dimensions have their own correspondence codimensions. A connected
component has a finite field of constants $k'/k$ over which it is
geometrically integral. The zeta computation reduces to the preceding
one using $Z_{X/k}(t)=Z_{X/k'}(t^{[k':k]})$, and degrees and cycles are
computed componentwise. Equivalently, the point-count reconstruction
proof of Proposition 8.1 uses the same Betti bound without requiring
geometric integrality. Projectors are still obtained from the common
degree-weight factors, and the trace proof uses the full direct sum of
geometric components. The empty scheme is certified by the zero object,
with determinant of its zero-dimensional realization equal to one.

## Exact literature scope and the remaining gate

The cited algorithmic ingredients are unconditional for a smooth
projective variety over a finite field. In contrast, Poonen--Testa--van
Luijk, Theorem 8.36(b), author-manuscript p. 19, assumes their
$E^r(X,\ell)$ when it identifies halting with the Tate conjecture in
codimension $r$. We do not remove that hypothesis from their theorem or
use it here. Our acceptance test asks whether an explicitly given
cross-correspondence has a nonzero determinant, which is determined by
its finite trace data.

Thus the remaining arbitrary-variety problem is whether the enumerated
search always finds a certificate. Neither its universal termination nor
a cycle-degree bound is proved. A numerical isomorphism supplied without
homologous splitting cycles is also not, by itself, asserted to satisfy
this test. The result provides a finite positive verifier, rational
coefficient descent and prime independence for every accepted variety.
It does not settle the full Tate conjecture or the equivalent
arbitrary-motive effectivity gate.

## Primary references

-   Deligne, P. (1974). La conjecture de Weil: I. *Publications
    Mathématiques de l'IHÉS, 43*, 273--307. Theorem 1.6, p. 276.
    <https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf>.

-   Katz, N. M., & Messing, W. (1974). Some consequences of the Riemann
    hypothesis for varieties over finite fields. *Inventiones
    Mathematicae, 23*, 73--77. <https://doi.org/10.1007/BF01405203>.
    Theorem 2, p. 76, common algebraic Künneth projectors; primary
    author-hosted scan:
    <https://web.math.princeton.edu/~nmk/old/katzmessing.pdf>.

-   Poonen, B., Testa, D., & van Luijk, R. (2015). Computing
    Néron--Severi groups and cycle class groups. *Compositio
    Mathematica, 151*(4), 713--734.
    <https://doi.org/10.1112/S0010437X14007878>. Inspected author
    manuscript: <https://math.mit.edu/~poonen/papers/compute_ns.pdf>.
    Exact author-page locators: §7.1, pp. 6--7; Propositions 8.1--8.2,
    p. 10; Lemma 8.7, p. 11; Remark 8.18, p. 14; and the differently
    hypothesized Theorem 8.36, p. 19.

-   The Stacks Project Authors. (2026). *The Stacks Project*.
    Lemma 45.9.7, Tag 0FHH, <https://stacks.math.columbia.edu/tag/0FHH>;
    Lemma 45.10.3, Tag 0FHR,
    <https://stacks.math.columbia.edu/tag/0FHR>. The inspected
    Weil-cohomology chapter PDF identifies version ed88ff78, compiled
    July 14, 2026; the displayed lemma statements and proofs were
    directly inspected.

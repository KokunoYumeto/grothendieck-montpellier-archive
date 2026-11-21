# A finite decision procedure for each specified rational descent

## CC-AG12: the rank bound removes the root-order search

Retain the established rational abelian, Artin, and Tate numerical
categories and the exact Milne orbit and Schur-index classification of
CC-AG08. Fix a source field $\mathbb F_{p^a}$, with $a\ge1$. No
integral-slope hypothesis is imposed in this section.

First consider one rational simple geometric object $S_\xi$, with
stabilized representative and centre $$\xi=[\pi,b],\qquad b\ge1,\qquad
         K=K_\xi=\mathbb Q(\pi^N)\quad(N\ge1).
                                                               \tag{CC-AG.65}$$
Let $d_\xi$ be its Schur index, and let $r\ge1$ be a specified target
multiplicity. Its rank is $$D=r\,d_\xi[K:\mathbb Q].
                                                               \tag{CC-AG.66}$$
Define the explicit integers $$R_D=\sum_{e=1}^{D}e\prod_{j=1}^{e}
                           \left(2\binom ej+1\right),
       \qquad N_D=\operatorname{lcm}(1,2,\ldots,R_D),
                                                               \tag{CC-AG.67}$$
and the monic rational polynomial $$P_{\xi,a,r}(X)=
   \prod_{\sigma:K\hookrightarrow\overline{\mathbb Q}}
       \left(X^{bN_D}-\sigma(\pi)^{aN_D}\right)
                            \quad\in\mathbb Q[X].             \tag{CC-AG.68}$$
Factor it into irreducible polynomials over $\mathbb Q$. Let
$O_1,\ldots,O_t$ be their root orbits, and choose $\alpha_j\in O_j$.
Every $\alpha_j$ is a Weil $p^a$-number whose germ belongs to $O_\xi$.
Compute $d_j$ from the full local-invariant formula (CC-AG.25), and put
$$m_j=
          \frac{[\mathbb Q(\alpha_j):\mathbb Q]}
               {[K:\mathbb Q]}\,
          \frac{d_j}{d_\xi}.
                                                               \tag{CC-AG.69}$$
These are positive integers.

Then the exact rational descent criterion is the finite
nonnegative-integer problem $$\begin{split}
 S_\xi^{\oplus r}\text{ descends to }\mathcal A_{p^a}
   \quad\Longleftrightarrow\quad
   &\text{there are }u_1,\ldots,u_t\in\mathbb Z_{\ge0}\\
   &\text{such that }\sum_{j=1}^{t}u_jm_j=r.
 \end{split}                                                  \tag{CC-AG.70}$$
Factors with $m_j>r$ can be discarded. Moreover all rational isomorphism
classes of preimages, without omission, are $$\bigoplus_{j=1}^{t}
                                    S_{O_j}^{\oplus u_j}
                                                               \tag{CC-AG.71}$$
as the finite solutions of (CC-AG.70) vary.

For any specified geometric object with finitely many simple isotypic
components, perform this finite test on each component. The results
combine independently. Thus actual rational descent of every specified
object in the established abelian sector is decidable by finite
algebraic calculations, and there are only finitely many rational
isomorphism classes of its preimages over a fixed finite field. For a
zero component the preimage is zero and no polynomial is required.

#### Complete proof.

We first recall the elementary bound in (CC-AG.67). If a root of unity
$\zeta$ has degree at most $D$, then all of its powers are algebraic
integers of degree at most $D$, with every conjugate of absolute value
one. A monic minimal polynomial of degree $e\le D$ has its $j$-th
coefficient bounded in absolute value by $\binom ej$, because that
coefficient is an elementary symmetric function of roots of modulus one.
There are at most $\prod_{j=1}^{e}(2\binom ej+1)$ possible integer
coefficient lists in degree $e$, each with at most $e$ distinct roots.
Therefore the set of all such algebraic numbers has cardinality at most
$R_D$. The distinct powers of $\zeta$ lie in that set, so its order is
at most $R_D$ and divides $N_D$. This is the bounded-polynomial argument
of Milne (2020), Proposition 5.5 and Corollary 5.6, p. 87, with its
bound made explicit.

Suppose a source object descends to $S_\xi^{\oplus r}$. Decompose that
source into rational simples. By CC-AG09, every source simple which
occurs has a label $\alpha\in W(p^a)$ whose germ belongs to $O_\xi$, and
its geometric base change is a positive number of copies of $S_\xi$. In
particular its rank is at most $D$. Conjugate the label if necessary to
arrange $[\alpha,a]=[\pi,b]$, and let $L=\mathbb Q(\alpha)$. The source
rank formula gives $$[L:\mathbb Q]
                       \le d_\alpha[L:\mathbb Q]
                       \le D.
                                                               \tag{CC-AG.72}$$
Germ equality gives $\alpha^{bN}=\pi^{aN}$ for some $N\ge1$. Since the
representative is stabilized, $K=\mathbb Q(\pi^{aN})\subset L$.
Consequently $$\theta=\alpha^b/\pi^a$$ is a root of unity *in $L$*. Its
degree over $\mathbb Q$ is at most $D$. The bound just proved implies
$\theta^{N_D}=1$, and hence $$\alpha^{bN_D}=\pi^{aN_D}.
                                                               \tag{CC-AG.73}$$
Thus every possible source simple has its entire Galois orbit among the
roots of (CC-AG.68). This is the step that makes the search finite even
when the original fibre over a germ contains infinitely many
root-of-unity twists.

We also verify that every root listed in (CC-AG.68) has the correct
label conditions. The polynomial has rational coefficients because the
product is Galois invariant. If $\alpha$ is a root, then for one
embedding $\sigma$ it satisfies $$\alpha^{bN_D}=\sigma(\pi)^{aN_D}.
                                                               \tag{CC-AG.74}$$
Stabilization implies $\sigma K=\mathbb Q(\sigma(\pi)^{aN_D})
                  \subset\mathbb Q(\alpha)$. For every complex embedding
of $\mathbb Q(\alpha)$, taking absolute values in (CC-AG.74) gives
$|\alpha'|=p^{aw/2}$, where $w$ is the weight of $\xi$. At every finite
place away from $p$, the same equation gives valuation zero. Thus
$\alpha\in W(p^a)$. Moreover (CC-AG.74) gives
$[\alpha,a]=[\sigma\pi,b]=\sigma\xi$. All candidate roots therefore have
the correct weight, $p$-unit condition, and germ orbit; no unproved
enlargement of the category is involved.

Distinct embeddings of $K$ give distinct values of $\sigma(\pi)^{aN_D}$,
since that power generates $K$. Each binomial in (CC-AG.68) is separable
in characteristic zero, and its constant term is nonzero. The product is
consequently separable. Its irreducible factors thus give a finite list
of distinct source simple classes.

Apply the exact base-change formula CC-AG09 to each of those classes.
Its image is $S_\xi^{\oplus m_j}$, with the full index ratio (CC-AG.69);
this proves the asserted positive integrality of $m_j$. Necessity of
(CC-AG.70) now follows from the completeness of the candidate list.
Conversely, each nonnegative solution constructs the actual rational
object (CC-AG.71), and its base change is exactly $S_\xi^{\oplus r}$.
Uniqueness of simple decompositions identifies distinct solutions with
distinct rational isomorphism classes. Since every $m_j>0$, each
$u_j\le r/m_j$. Only finitely many solutions exist, and factors with
$m_j>r$ cannot occur.

Finally, a source simple has isotypic geometric image in one target
orbit, so source summands for different target orbits cannot contribute
to one another. Decomposing a general target into its finitely many
isotypic components reduces the problem to the preceding tests and their
finite Cartesian product of solution sets. The zero target has only the
zero preimage because all nonzero simples have positive rank. This
proves all assertions. $\square$

#### Scope of effectivity.

The input is the finite orbit and index data of a specified object. The
output is its complete list of rational simple-label multiplicities over
the specified source field. Exact factorization and the local-invariant
computations are finite number-field calculations; the bound is not
intended as an efficient algorithm. No explicit algebraic cycle
representatives for the numerical projectors are claimed.

The integer $D$, and hence the polynomial cutoff, depends on the target
multiplicity. The theorem does not give one cutoff for an entire
geometric multiplicity monoid, and does not claim that all such monoids
are cyclic. In particular it keeps the fractional-slope Schur indices in
the formula. It does resolve the formerly unbounded root-order search
for every specified object in every slope sector. The separate
arbitrary-variety cross-correspondence and full Tate conditions are
unchanged.

## Primary references

-   Milne, J. S. (1994). Motives over finite fields. In U. Jannsen,
    S. Kleiman, & J.-P. Serre (Eds.), *Motives* (Proceedings of Symposia
    in Pure Mathematics, Vol. 55, Part 1, pp. 401--459). American
    Mathematical Society. Corrected author version dated November 2,
    2019: <https://www.jmilne.org/math/xnotes/Seattle1.pdf>. The precise
    classification, rank, centre, and local-index inputs are those
    inspected and recorded in CC-AG08, especially Proposition 2.8,
    p. 14, Theorems 2.15--2.16, p. 18, and Theorems 2.18--2.19, p. 20.

-   Milne, J. S. (2020, July 19). *Algebraic number theory*
    (Version 3.08) \[Author course notes\].
    <https://www.jmilne.org/math/CourseNotes/ANT.pdf>. Proposition 5.5
    and Corollary 5.6, printed p. 87.

# A complete formal countermodel to the BV-only determinant argument

**Status (2026-11-19, approximately 06:42 UTC): proved formal countermodel.** This is a countermodel to an implication from specified tensor identities. It is neither a geometric K3 counterexample nor movement on the actual Chow-vanishing gate.

## 1. The rational rigid symmetric category

Fix an integer $d\geq1$. Define the rational Brauer category $\mathcal B_d$ directly. Its objects are the nonnegative integers, denoted $W^{\otimes r}$. A basis of

\[
\operatorname{Hom}(W^{\otimes r},W^{\otimes s})
\]

is the set of perfect matchings of $r+s$ labeled endpoints; the space is zero if $r+s$ is odd. Tensor product is horizontal concatenation. Composition glues the $s$ intermediate endpoints, retains the resulting matching of the outer endpoints, and multiplies by $d^c$, where $c$ is the number of closed components removed by gluing. Connected components of the full glued graph show that this composition is associative, independently of the order of gluing. Vertical strands give identities. Permutation diagrams give the symmetry. The cup and cap give a symmetric pairing

\[
q:W\otimes W\longrightarrow\mathbf1
\]

and its inverse copairing. Their zigzag identities are immediate from a single glued strand, and the closed circle has value $d$. Hence $W$ is self-dual of categorical dimension $d$.

Adjoin a central even invertible object $T$, with categorical dimension $1$, by taking pairs $W^{\otimes r}T^a$, $a\in\mathbb Z$, and declaring the Hom space to be the preceding Brauer Hom space when the two powers of $T$ agree, and zero otherwise. Take the additive and idempotent completions. These operations do not identify different original basis diagrams. The resulting category is rational, rigid, symmetric and pseudo-abelian. The symmetry of $T\otimes T$ is the identity.

## 2. The surface Frobenius algebra and its exact identities

Put

\[
L=T^2,\qquad U=W\otimes T,\qquad
A=\mathbf1\oplus U\oplus L.
\]

The unit $\eta:\mathbf1\to A$ is the first-summand inclusion. The multiplication $\mu:A\otimes A\to A$ is the unit multiplication on the first summand; on $U\otimes U$ it is $q\otimes\operatorname{id}_{T^2}:U\otimes U\to L\hookrightarrow A$; all products between positive summands involving $L$ are zero. The trace $\tau:A\to L$ is the last-summand projection. The point $o:L\to A$ is the last-summand inclusion.

This multiplication is commutative. To check associativity, remove all unit factors. Three positive factors have zero product in either order: a pair of $U$'s produces $L$, which then kills the remaining positive factor, and a pre-existing $L$ kills the first product. This covers every summand of $A^{\otimes3}$.

The pairing $b=\tau\mu:A\otimes A\to L$ pairs the summands $\mathbf1,L$ hyperbolically and restricts to the nondegenerate pairing on $U$. It is therefore nondegenerate. This proves all the commutative Frobenius axioms, including the required self-duality $A^\vee\simeq A\otimes L^{-1}$.

Let $c:L\to A\otimes A$ be the inverse copairing, and let $q_U:L\to U\otimes U$ be its $U\otimes U$ component. Then

\[
c=\eta\otimes o+o\otimes\eta+q_U,
\qquad \mu c=(d+2)o.
\]

The last equality follows because the two hyperbolic terms each contribute $o$, while the cap-cup contraction on $W$ contributes $d\,o$. Thus the Euler/diagonal-self-intersection normalization is exactly that of a surface with Euler characteristic $d+2$.

The Frobenius diagonal pushforward is the adjoint map

\[
\delta:A\otimes L\longrightarrow A\otimes A,
\qquad \delta=(\mu\otimes\operatorname{id}_A)
                 (\operatorname{id}_A\otimes c).
\]

Consequently

\[
\delta\,(o\otimes\operatorname{id}_L)=o\otimes o:
L^2\longrightarrow A^2.
\]

Indeed only the term with a unit next to the first $o$ survives. This is the formal identity $\Delta_*o=o\boxtimes o$.

Let $s:L^2\to A^3$ be the transpose of the triple trace form $\tau\mu^{(3)}:A^3\to L$, using the pairing $b$ on every input. Explicitly, $s$ has the three components with one unit and two points, and the three components with a paired $U\otimes U$ and the point in the remaining position, all with coefficient $1$. Therefore

\[
s=c_{12}o_3+c_{13}o_2+c_{23}o_1
  -o_1o_2\eta_3-o_1o_3\eta_2-o_2o_3\eta_1.
\]

For example, the component $\eta_1o_2o_3$ occurs twice in the first three terms and once with negative sign; each paired-$U$ component occurs once. This is exactly the Beauville–Voisin small-diagonal identity, with every map typed as $L^2\to A^3$. Also $\tau\mu^{(3)}$ vanishes on $(U\oplus L)^3$, so all higher positive trace forms vanish by associativity.

In particular, at $d=22$ these identities have the K3 normalization $\mu c=24o$.

## 3. The determinant is nevertheless nonzero

For $m\geq1$, define

\[
a_m=\frac1{m!}\sum_{\sigma\in\mathfrak S_m}
       \operatorname{sgn}(\sigma)\,\sigma
       \in\operatorname{End}_{\mathcal B_d}(W^{\otimes m}).
\]

The permutation diagrams are distinct members of the defining matching basis. The coefficient of the identity diagram in $a_m$ is $1/m!\neq0$. Hence $a_m\neq0$, for every $m$, even if $m>d$. The group-algebra calculation $a_m^2=a_m$ is valid inside the Brauer algebra because permutation diagrams compose exactly as permutations. Therefore the exterior-power object $(W^{\otimes m},a_m)$ is nonzero in the idempotent completion: its identity morphism is the nonzero morphism $a_m$.

Since $T$ is even and invertible,

\[
\bigwedge^{d+1}U
 =\bigl(\bigwedge^{d+1}W\bigr)\otimes T^{d+1}
 \neq0.
\]

On the other hand, for every nondegenerate rational quadratic space $(V,Q)$ of dimension $d$, sending $W$ to $V$, the cap to $Q$, the cup to $Q^{-1}$, and $T$ to a one-dimensional even graded space defines a symmetric tensor functor to graded rational vector spaces. Every diagram relation is preserved: a closed circle evaluates to $d$. Under this functor $a_{d+1}$ maps to the ordinary alternating projector on $V^{\otimes(d+1)}$, which is zero. For $d=22$, one can choose $Q$ to be the actual rational K3 cup-product form. Thus the full marked Frobenius algebra has the same realized surface cohomology data as a K3 surface, but its formal determinant still does not vanish.

For clarity, the actual projector onto $U\subset A$ exists in this category because the displayed direct-sum decomposition is genuine. The failure is not caused by a missing projector or parity decomposition.

## 4. Why contraction does not repair the argument

Closing the last strand gives the exact partial-trace identity

\[
\operatorname{Tr}_{m}(a_m)
 =\frac{d-m+1}{m}\,a_{m-1}.
\]

To check it, decompose the alternating sum into its $m$ cosets of $\mathfrak S_{m-1}$. The identity coset produces $d\,a_{m-1}$ after closing the last strand. Each of the $m-1$ transposition cosets contributes $-a_{m-1}$; normalization divides by $m$. At $m=d+1$, this partial trace is zero although $a_m\neq0$. Hence the first determinant cannot be recovered by contracting it and dividing by a nonzero dimension factor.

## 5. Exact computational certificate and scope

`code/part_c/check_brauer_bv_obstruction.py` and its JSON output check the nonzero idempotents at $(d,m)=(1,2),(2,3),(3,4)$, the complete partial-trace formula at five parameter values in each size, all 3,375 associativity triples of the 15-dimensional diagram algebra $B_3(2)$, and the six components of the BV identity. All checks pass over rational numbers. The case $d=22,m=23$ is proved by the general basis-coefficient argument; its $23!$ summands were not enumerated.

This proves only that the BV identity, the Frobenius axioms and the point/Euler normalizations do not formally force the determinant relation. It does not produce a smooth projective variety realizing the nonzero formal idempotent, and does not refute finite-dimensionality of any K3 surface. The original geometric vanishing gate is unchanged.

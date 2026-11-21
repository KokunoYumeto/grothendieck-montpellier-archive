# An actual integrable complete intersection defeats the unrestricted cross-minor inference

Root derivation, 2026-11-21, HODGE_DIVISION, GPT-6 Astra Pro;
reasoning effort inherited and not exposed. This boundary was derived before
the sibling's independent check. It does not supply a module deformation or
a weakly semiregular object, and it does not change the main supplier gate.

Let the columns of the rational matrix J be

\[
u=(1,0,-3/5,-8/5)^t,\quad v=(0,1,1,1)^t,\quad
u'=(1,0,-9/5,-16/5)^t,\quad v'=(0,1,2,3)^t.
\]

Put p=u wedge v and q=u' wedge v'. In the coordinate order
(12,13,14,23,24,34), their coefficients are

\[
p=(1,1,1,3/5,8/5,1),\qquad q=(1,2,3,9/5,16/5,1).
\]

Both forms are decomposable. For the complementary index pairs their
ratios q_ij/p_ij agree within each pair and are respectively 1,2,3.
Consequently every complementary coefficient cross minor
p_ij q_kl-q_ij p_kl vanishes. Nevertheless

\[
p\wedge q=2(1-16/5+9/5)=-4/5=\det J\ne0.
\]

Work in R=C[[x,y,z,w]] with the constant bivectors
pi_+=partial_x wedge partial_y and pi_-=partial_z wedge partial_w.
Let ell=J(x,y,z,w)^t and set f_i=ell_i^2 and I=(f_1,f_2,f_3,f_4).
The matrix is invertible, so A=R/I is the actual length-sixteen complete
intersection C[[ell_1,...,ell_4]]/(ell_1^2,...,ell_4^2). Its embedding
dimension is four. The actual Jacobian of these actual power series is

\[
\operatorname{Jac}(f)=2\operatorname{diag}(\ell_i)J.
\]

Thus the two bracket matrices in A have entries
P^+_ij=4 ell_i ell_j p_ij and P^-_ij=4 ell_i ell_j q_ij.
For any two index pairs with a repeated index, both products in their
cross minor vanish because ell_i^2=0. For disjoint index pairs the
coefficient minor already vanishes by the preceding explicit calculation.
It follows that **every** scalar cross minor
P^+_ij P^-_kl-P^-_ij P^+_kl is zero in A.

On the other hand,

\[
\det\operatorname{Jac}(f)=-\frac{64}{5}\ell_1\ell_2\ell_3\ell_4
\]

is a nonzero socle element. The squarefree monomials form a basis of A,
so this nonvanishing is elementary in this explicit example. The mixed
wedge is the same nonzero Jacobian coefficient. This counterexample uses
an actual gradient matrix, not an arbitrary nonintegrable matrix over A.

The cross-minor equations are necessary consequences of both companion
matrix equations in SF-E836; this example does **not** solve those matrix
equations. It also does not construct a deformation of any hull-modification
module. The commuting-triple hypothesis of SF-E836 cannot hold for any
regular generator presentation of this example with these bivectors:
that hypothesis plus the invariant cross-minor identities would force
the invariant mixed wedge to vanish. Additional module or syzygy conditions
are therefore necessary for an unrestricted complete-intersection argument.

The adjacent exact script independently reconstructs J, its two exterior
forms, every pair of coefficient minors in the square-zero quotient,
the actual Jacobian and its socle. It is supplementary to the universal
two-case calculation above. No main-gate movement is claimed.

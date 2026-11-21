# Removing quasiprojectivity from the cote 14 parameters

## BR-14-SEP: reduction to a dense affine parameter

#### Original scope.

Grothendieck’s Definition 1.1 in cote 14, physical PDF page 24,
footer 23, places the word *projectif* in brackets before *lisse
connexe*. The preceding results identify the relation with or without
this qualification when the nonproper parameter is quasiprojective. The
following deduction removes that remaining restriction on the parameter
scheme. The algebraically closed base-field convention is still
explicit; it is not attributed to the handwritten definition.

#### Statement.

Let $k$ be algebraically closed, and let $T$ be a nonempty smooth
connected separated scheme of finite type over $k$. For every nonempty
affine open $U\subset T$, the ordinary abelian Albanese of $T$ exists,
and the inclusion induces an isomorphism
$$\operatorname{Alb}_{\rm ab}(U)
                    \xrightarrow{\ \sim\ }
              \operatorname{Alb}_{\rm ab}(T).                 \tag{BR.14.1}$$
Base points may be chosen in $U(k)$. Every zero cycle on $T$ has a
representative of the same degree supported in $U$, modulo explicit
Suslin one-boundaries. For $V=U,T$, write $H_V=H^S_0(V,\mathbb Z)^0$ and
$K_V=\ker(H_V\to\operatorname{Alb}_{\rm ab}(V)(k))$. Consequently the
maps $$H_U\longrightarrow H_T,\qquad
                    K_U\longrightarrow K_T                  \tag{BR.14.2}$$
are surjective. In positive characteristic, CC-ALB01 therefore gives
divisibility of both groups on the right and surjectivity
$$H^S_0(T,\mathbb Z)^0[n]\longrightarrow
                    \operatorname{Alb}_{\rm ab}(T)(k)[n]
              \qquad(n\ge1).                                 \tag{BR.14.3}$$

Let $X/k$ be smooth projective and geometrically connected. Define
$N^i_{\rm sep}(X)$ using all such smooth separated parameters $T$, all
$\Gamma\in CH^i(T\times X)$, and free degree-zero zero cycles whose
ordinary Albanese sum is zero. Let $N^i_{\rm aff}(X)$ be the subgroup
using only smooth connected affine parameters. Then, integrally and in
every characteristic, $$N^i_{\rm aff}(X)=N^i_{\rm qp}(X)
                =N^i_{\rm sep}(X)=N^i_{\rm proj}(X).           \tag{BR.14.4}$$
Thus allowing arbitrary smooth separated finite-type parameters does not
enlarge the relation or change the quotient in the original Theorem 3.1,
physical page 38/footer 37.

#### Exact external inputs.

Milne (2008), Chapter I, Theorem 3.2, printed p. 17, extends a rational
map from a nonsingular variety to an abelian variety over the whole
source. His convention on printed p. v allows every geometrically
reduced separated finite-type scheme, without quasiprojectivity.
Lemma 3.6, printed p. 18, says that the union of the integral curves
through a smooth point and nonsingular there is dense. Lemma 3.5 on the
same page supplies normalization and smooth completion of curves. The
Gysin maps used below are the factorization-independent maps of the
Stacks Project, Lemma 42.59.3 (Tag 0FF2) and Definition 42.59.4
(Tag 0FF3); their functoriality is Lemma 42.59.6 (Tag 0FF5). Their
construction requires a smooth–immersion factorization, which is
supplied here by the graph of a morphism between smooth separated
schemes.

<div class="proof">

*Proof.* *1. The ordinary Albanese is unchanged by the dense open.*
Smoothness and connectedness make $T$ integral: regular local rings are
domains, so its distinct irreducible components are disjoint and open.
Thus $U$ is dense and integral. Choose $u_0\in U(k)$, and write
$a_U:U\to A_U=\operatorname{Alb}_{\rm ab}(U)$ for the pointed ordinary
Albanese, which exists for the smooth affine variety $U$. Regard $a_U$
as a rational map on $T$. The cited extension theorem gives a morphism
$a_T:T\to A_U$, still pointed at $u_0$.

If $f:T\to B$ is a pointed morphism to any abelian variety, its
restriction to $U$ factors through a unique homomorphism $h:A_U\to B$.
The two morphisms $f$ and $h a_T$ agree on the dense open $U$; since $T$
is reduced and $B$ is separated, they agree on $T$. Uniqueness follows
from the same universal property on $U$. Hence $(A_U,a_T)$ is the
ordinary Albanese of $T$, proving (BR.14.1).

*2. Moving one point using a curve in an affine neighbourhood.* It
suffices to move $x\in T(k)\setminus U(k)$. Choose an affine
neighbourhood $V$ of $x$. The open $V\cap U$ is nonempty, because $T$ is
integral. By the cited curve lemma there is an integral curve in $V$,
nonsingular at $x$, which meets $U$. Normalize it and call the resulting
smooth curve $C$, with its morphism $\nu:C\to T$ and point $x'$ above
$x$. In particular $k(x')=k$. Let $\overline C$ be its smooth projective
completion. Put $$D=\overline C\setminus C,\qquad
 F=C\setminus\nu^{-1}(U).$$ These are finite sets. Choose
$y\in\nu^{-1}(U)(k)$. For a sufficiently large integer $N$, the first
cohomology of $$\mathcal O_{\overline C}
 \left(Ny-2x'-\sum_{z\in D\cup(F\setminus\{x'\})}z\right)$$ vanishes:
its degree exceeds $2g(\overline C)-2$. The resulting surjective
evaluation map gives a rational function $f$ with poles only at $y$,
first-order jet a uniformizer at $x'$, and value $1$ at every point of
$D\cup(F\setminus\{x'\})$. Thus
$$\operatorname{div}(f)=[x']+z-m[y],\qquad
       \operatorname{supp}(z)\subset\nu^{-1}(U),
       \qquad \deg z=m-1.                                  \tag{BR.14.5}$$
Here $z$ is effective and $m>0$: $f$ is nonconstant, and it cannot have
no poles on the projective curve.

The morphism $g=f/(f-1):\overline C\to\mathbb P^1$ is finite. Its
inverse image of $\mathbb A^1$ lies in $C$ because $f=1$ on $D$. Its
graph is therefore a finite correspondence from $\mathbb A^1$ to $C$,
and the difference of its fibres at $0$ and $1$ is
$\operatorname{div}(f)$, up to the choice of boundary sign. Its image
under $\nu$ is a valid finite correspondence to $T$. Indeed, put
$W=g^{-1}(\mathbb A^1)$. Its graph $W\to W\times T$ is closed because
$T$ is separated, and $W\times T\to\mathbb A^1\times T$ is finite. Their
composite is finite. Pushing (BR.14.5) forward shows that $[x]$ is equal
in Suslin homology to $m[\nu(y)]-\nu_*z$, a degree-one cycle supported
in $U$. Linearity proves the moving assertion for every zero cycle, with
its degree unchanged. No common quasiprojective neighbourhood of all
points of that cycle was used.

*3. Albanese and correspondence values survive this move.* The morphism
$a_T\nu:C\to A_U$ extends to $\overline C$, since the target is proper
and the source is a smooth curve. A principal divisor on $\overline C$
has zero image under its induced map from the Jacobian to $A_U$. Thus
(BR.14.5) preserves the ordinary Albanese sum.

For completeness, fix $\Gamma\in CH^i(T\times X)$. Pull it back along
$\nu\times1_X$ using the Gysin map; this exists because both schemes are
smooth and separated, and the graph gives the required factorization.
Choose a cycle representative on $C\times X$, and close its components
on $\overline C\times X$, giving a class $\overline\Gamma$. Its
restriction is the chosen pullback. The usual product with the pullback
of $\operatorname{div}(f)$ is zero in the Chow group of
$\overline C\times X$, since a principal divisor is zero in
$CH^1(\overline C)$. Push this equality to $X$; this projection is
proper. Gysin functoriality and restriction to the open $C$ identify its
terms with $$\Gamma_{\nu(x')}+
       \sum_{c\in\operatorname{supp}(z)}\operatorname{mult}_c(z)
                   \Gamma_{\nu(c)}-m\Gamma_{\nu(y)}=0.
                                                               \tag{BR.14.6}$$
Thus the correspondence action also preserves the move. This argument
only uses curves and the projective target; it does not require a
compactification of $T$.

The Albanese sum descends to Suslin homology by the same proper-curve
argument for an arbitrary Suslin one-chain: normalize its finite support
over $\mathbb A^1$, complete the resulting curve, and use the function
$t/(t-1)$. At each point above infinity this function has value $1$, so
its divisor is precisely the difference of the finite fibres. Step 2 now
proves the first surjection in (BR.14.2). By (BR.14.1), a lift of a
class with zero Albanese sum has zero Albanese sum already on $U$. This
proves the second surjection.

*4. Divisibility and equality of the parameter relations.* In positive
characteristic CC-ALB01 applies to the affine $U$. Its two divisible
groups map onto those for $T$, and a quotient of a divisible abelian
group is divisible. For any $a\in A_U(k)[n]$, its lift in
$H^S_0(U,\mathbb Z)^0[n]$ maps to an $n$-torsion lift in
$H^S_0(T,\mathbb Z)^0$. This proves (BR.14.3).

Now let $\Gamma_*v$ be a generator of $N^i_{\rm sep}(X)$. The preceding
steps replace $v$ by a cycle $v_U$ supported in $U$, of degree zero,
with zero Albanese sum in $A_U$, and satisfying
$$\Gamma_*v=(\Gamma|_{U\times X})_*v_U.
                                                               \tag{BR.14.7}$$
The right side belongs to $N^i_{\rm aff}(X)$. The reverse inclusion
follows because affine parameters are allowed among the separated
parameters. Hence $N^i_{\rm sep}=N^i_{\rm aff}$. The evident inclusions
$N^i_{\rm aff}\subset N^i_{\rm qp}\subset N^i_{\rm sep}$ give their
equality. The already proved equality $N^i_{\rm qp}=N^i_{\rm proj}$,
namely AQ-14-QUASIPROJECTIVE in characteristic zero and CC-ALB02 in
positive characteristic, completes (BR.14.4). ◻

</div>

#### Semiabelian convention and limits.

If the relation instead uses the kernel of a universal semiabelian
Albanese, every such cycle has zero ordinary abelian Albanese sum. Its
relation subgroup lies between the projective-parameter subgroup and
$N^i_{\rm sep}$; (BR.14.4) makes these endpoints equal. This observation
does not assert that the semiabelian Albanese itself is unchanged by
removing a divisor. Nothing here extends the equality to arbitrary
nonclosed base fields, singular parameters, or an unspecified integral
motivic projector.

#### References.

Milne, J. S. (2008, March 16). *Abelian varieties* (Version 2.0)
\[Author course notes\].
<https://www.jmilne.org/math/CourseNotes/AV.pdf>. Conventions, p. v;
Chapter I, Theorem 3.2, p. 17, and Lemmas 3.5–3.6, p. 18. The Stacks
Project Authors. (2026). *The Stacks Project*. Section 42.59, especially
Lemma 42.59.3 (0FF2), Definition 42.59.4 (0FF3), and Lemma 42.59.6
(0FF5): <https://stacks.math.columbia.edu/tag/0FEZ>.

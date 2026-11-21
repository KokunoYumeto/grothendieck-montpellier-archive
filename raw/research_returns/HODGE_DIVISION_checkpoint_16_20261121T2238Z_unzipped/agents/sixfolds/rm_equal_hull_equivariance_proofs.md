# SF-E828. Equal-hull free blocks are still equivariant after averaging

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** independently whole-reviewed by /root and /root/imprimitive;
both mathematical reviews PASS on the frozen draft
`d57b98f4adff0567e2ee52c2866ca8d418064f79c815b86b25e14ff149552260`.
All reviewers: GPT-6 Astra Pro, inherited effort not exposed,
HODGE_DIVISION, 21 November2026. This closes a proposed same-hull exception to E826/E827. It does not
assert that a nonsplit positive HN factor has the direct-sum form below.
No new numerical computation is a premise.

## 1. Statement

Retain the actual unit sheaf F on the abelian fourfold X, with smooth
integral nonempty S the intersection of two divisors in the ample class
D=k theta used in E826, where k is positive.
Its exact sequence and dual are

\[
 0\longrightarrow i_*O_S(-2D)\longrightarrow F\longrightarrow I_S
 \longrightarrow0,\qquad F^\vee=O_X.
 \tag{E828.1}
\]

Let L be a line bundle, and put U=F tensor L. Let

\[
 A=U^{\oplus r}\oplus P,
 \qquad P=\bigoplus_{a=1}^u L_a^{\oplus n_a},
 \tag{E828.2}
\]

where r and n_a are positive, the c1(L_a) are pairwise distinct, and all
L_a have the same theta slope as L. Unlike E826's originally stated
hypothesis, one L_a is allowed to be isomorphic to L. Also allow a line of
the same Chern class as L with a nontrivial degree-zero difference; because
c1(L_a) are pairwise distinct there is at most one such class block.

Suppose A carries the actual coherent finite translation/tensor action
induced from the intrinsic two-slope torsion/HN filtration of an extension
as in E826. Then each displayed free block is a canonical invariant
subobject of A. There is an actual equivariant direct-sum decomposition
of A into all those free blocks and a complement whose underlying sheaf is
U^{r}. Consequently the conclusions of E826 and E827 apply with their same
Ext and cap hypotheses, without the condition c1(L_a) different from c1(L).

The complement is not claimed canonical. The assertion is existence of an
actual coherent equivariant splitting, obtained by averaging an existing
ordinary splitting. No new action or new isogeny is chosen.

## 2. The Hom vanishings and the intrinsic line subobjects

First H0(F)=0. In (E828.1), H0(I_S)=0 because a global regular function on
the connected projective X is constant and S is nonempty. Also
H0(O_S(-2D))=0 because D restricted to S is ample and its negative has no
nonzero section. The exact sequence proves the claim.

For any L_a of the stated slope, Hom(L_a,U)=0. To see this, tensor
(E828.1) by L tensor L_a inverse. If its first Chern class is nonzero,
its theta-degree on X is zero, so a nonzero section of its hull would give
a nonzero effective divisor of theta-degree zero, impossible. If its class
is zero but the line is nontrivial, it has no section: a section would give
an effective divisor of numerical class zero and would therefore be nowhere
vanishing. If the line is trivial, the ideal factor I_S has no section as
just proved. In all cases the torsion term has theta-degree
\((-2D+c_1(L)-c_1(L_a))D^2\theta\), which is strictly negative: S has
class D^2, D is the scalar multiple of theta used in E826, and the slope
difference is zero. Thus its space of sections is zero as well.

Distinct L_a have no Hom between them, by the same theta-degree argument.
It follows that the evaluation image

\[
 \operatorname{im}\bigl(\operatorname{Hom}(L_a,A)\otimes L_a\to A\bigr)
        =L_a^{\oplus n_a}
 \tag{E828.3}
\]

is exactly the displayed block. This description is independent of choices
of basis for Hom and is an actual subsheaf description.

We verify that any functor occurring in the given action preserves the
isomorphism class of each L_a; preserving its Chern class alone would not
suffice. Let T_g=t_x^*(-) tensor Q, with Q degree zero, and put M=T_g(L_a).
The given action on A carries the displayed nonzero inclusion L_a to A to
an inclusion M to A. The line M has the same theta slope as L. The Hom
vanishing proof above applies to every such line M, not just the displayed
L_a: it gives Hom(M,U)=0, including when c1(M)=c1(L), with any flat twist.
Therefore the nonzero map M to A has a nonzero component into some L_b.
Since c1(M)=c1(L_a), the distinct-Chern-class assumption forces b=a.
A nonzero map between two lines of the same first Chern class is an
isomorphism: its effective zero divisor has theta-degree zero, hence is
empty. Thus M is isomorphic to L_a.

This direct argument also handles c1(L_a)=c1(L) with a nontrivial flat
difference. It neither uses Krull--Schmidt nor infers isomorphisms of
ambient lines from their restrictions to S. Its only additional datum is
the existing inclusion of each free summand in A.

Thus each functor sends the evaluation image (E828.3) onto itself. The
coherent action on A restricts to an actual coherent action on each free
block and on their sum P.

## 3. Averaging the retraction and the exact scope

Let j:P to A be the resulting equivariant inclusion. The displayed ordinary
direct sum (E828.2) supplies a retraction q:A to P with qj=Id_P. The actual
actions on A and P give a linear action on Hom(A,P). Average q over the
finite group:

\[
 q_\Gamma=\frac1{|\Gamma|}\sum_{g\in\Gamma}g(q).
 \tag{E828.4}
\]

For each g, the identity qj=Id and equivariance of j give g(q)j=Id. Hence
q_Gamma j=Id. The averaged morphism is invariant, so its kernel C is an
actual coherent equivariant complement and A=P direct sum C.

As an ordinary sheaf, C is isomorphic to U^r. Indeed relative to the original
splitting, any retraction has the form (h,Id_P) for a morphism h:U^r to P,
and its kernel is the graph of -h. This also makes explicit why possible
nonzero Hom(U,L_a) does not obstruct the splitting after averaging.
The multiplicity actions may be projective after choices of line
trivializations; the actual action on Hom(A,P) and its average are honest
because they are induced from the specified coherent action on the sheaves.

The intrinsic torsion/HN argument of E826 still supplies an action on A:
A/tors A is semistable of its common positive slope, while the quotient B
has strictly smaller negative slope. Allowing a free class equal to the
unit hull class does not change that proof. The invariant direct-sum
splitting just constructed supplies exactly the A-block hypothesis used
in E826/E827. Their actual triangle maps, selected B-block vanishings and
rank18 comparison then apply without alteration.

This refines only the explicit direct-sum positive factor (E828.2).
If the positive factor itself is a nonsplit extension of U and line
bundles, an ordinary retraction need not exist and averaging cannot create
one. If additional nonisomorphic line types with the same Chern class are
allowed, the same-slope free evaluation subcategory can be preserved as an
orbit, but no assertion about individual type blocks is made here. Those
are separate remaining constructions, not cases silently covered above.

## 4. Source and check boundary

The unit exact sequence and dual are the already whole-reviewed UG/US
proofs. All new subsheaf, line-type and averaging arguments are given above.
The section-vanishing argument uses only positivity of an ample divisor and
the usual global functions on a connected projective variety. E826/E827
retain their exact full supplied S21 adjunction and published BF/Mumford
source boundaries. No new external theorem, numerical rank, constructed
finite group or semiregular object is claimed.

# SF-E835: independent whole-proof audit

**PASS**, using the separately whole-reviewed SF-E834 and the stated
previously reviewed E811/E813/E817/E818 interfaces.

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited/unexposed
effort, HODGE_DIVISION. Date: 2026-11-21. Actual completion timestamp is
recorded in CHECK_EVENTS.tsv when this report is finalized. Reviewed the
entire frozen `agents/sixfolds/rm_semistable_reflexive_reduction_draft.md`,
SHA-256 `11b576f3e4eeb58fdc22c6e8b31bbef02f7290fce9f38c2bfb5dd95d9235bfa1`.
No author-file changes or mathematical repairs were requested. No finite
computation is needed or claimed.

## 1. Actual stable factors and their reflexive hulls

The finite slope-stable-factor filtration exists with torsion-free
quotients. I checked the given induction: choose an equal-slope
subsheaf of least positive rank, saturate it, and use semistability to
exclude a positive divisorial increase in slope. Minimality makes the
factor stable. A destabilizing subsheaf of the saturated quotient would
pull back to a destabilizing subsheaf of the original sheaf. The ranks
strictly decrease in the induction, so it terminates. No local freeness
is assumed here.

For each stable torsion-free quotient Q, its double dual is stable.
Intersecting any lower positive-rank subsheaf of Q** with Q preserves
rank and first Chern class, because Q**/Q has codimension at least two.
This correctly transfers the strict slope inequality. The defects are
actual coherent quotient sheaves with effective leading support cycles.

The first normalized Chern component gives B=-alpha. Equal slopes imply
that every invariant representative of alpha_i-alpha is primitive for
theta. On a torus the contraction of an invariant (1,1)-form is constant,
so its vanishing integrated theta-degree is exactly the required
pointwise primitivity.

## 2. Variance and elimination of surface defects

I independently expanded the complete discriminant identity. The sign
of the variance term is negative:

`Delta(E) = sum Delta(H_i) + sum ch2(T_i) - (1/2) sum r_i delta_i^2`.

The weighted mean identity sum r_i delta_i=0 gives this equality
directly; replacing Q_i by H_i adds the positive defect term. Each mixed
pairing is nonnegative: E834 supplies the stable-reflexive term, the
primitive mixed identity supplies the negative-square term, and strict
effective-surface positivity supplies the actual quotient term.

I read all of the current canonical E818 proof, including its complete
strict-surface argument. The vanishing mixed tangent forms force each
surface tangent plane into one of the two RM eigenspaces, by the
decomposable Pluecker-square identity. The Gauss map is constant on an
irreducible component. Its resolution would then map through a
positive-dimensional abelian subvariety with rational homology in one
irrational RM eigenspace, which is impossible. Simplicity of X is not
assumed. Thus every nonzero effective surface has strictly positive
mixed pairing.

The total mixed pairing is zero for the balanced character, so every
nonnegative summand vanishes. E834 now makes the H_i locally free and
projectively flat. The separate equality conditions for delta_i are
block diagonality and primitivity in each plane. Every T_i has dimension
at most one. There is no cancellation between virtual defects in this
argument.

## 3. Cubic elimination of curves

Writing delta_i=delta_i,+ + delta_i,-, with each part on a complex
two-plane, gives
`theta delta_i^3=0`. I checked every term of the expansion: each vanishes
by excess plane degree or the separate primitivity identity.

The degree-three part of the actual K0 relation is therefore the stated
sum of cubes minus the sum of ch3(T_i). Exponential normalization does
not change the latter because all lower character components of these
dimension-at-most-one sheaves vanish. Pairing with theta gives a sum
of nonnegative ample degrees of actual effective curve cycles equal to
zero. Each curve component is eliminated individually. The union P of
the remaining supports is finite.

The leading-character/support-cycle input is used in the same exact
scope as E818. I rechecked its application to actual quotient sheaves
and all signs, but this event does not claim a new reading or proof of
Fulton's full Riemann-Roch theorem.

## 4. Actual extension lifting across P

The proof does not apply double duals to an exact filtration and assume
exactness is preserved. It constructs a new actual extension at each
step. For vector bundles V and W, Ext1 is H1 of V-dual tensor W. At a
point of the smooth fourfold, four regular parameters cut out P locally.
Local cohomology of a free module with this support vanishes below
degree four. The local-to-global support spectral sequence transfers
this vanishing to global cohomology with support. The support long exact
sequence then gives the required isomorphism on H1, and hence on Ext1.

I freshly read the entire relevant Stacks statements and proofs:

* Lemma 36.6.9, tag 0G7P: the extended Cech complex of a Koszul-regular
  sequence has the required degree concentration, and flat tensoring
  preserves it. Its hypotheses apply to the free local modules here.
* Section 20.21, tag 0A39: the support distinguished triangle and long
  exact sequence, and the local-to-global support spectral sequence.
  Both maps used in the argument are the actual restriction maps.
* Lemma 47.11.1, tag 0AVZ: the complete depth/local-cohomology statement
  and induction proof, providing the compatible depth interpretation.

Sources: https://stacks.math.columbia.edu/tag/0G7P,
https://stacks.math.columbia.edu/tag/0A39,
https://stacks.math.columbia.edu/tag/0AVZ.

The original sheaf and its filtration can be algebraized on projective
X. The restriction and Ext calculation are then wholly algebraic on U;
no improper use of a nonproper GAGA theorem occurs.

On U every Q_i equals the vector bundle H_i. By induction the earlier
extension is already a vector bundle there. The Ext1 isomorphism lifts
the next exact sequence, preserving its designated subobject and
quotient under the restriction isomorphism. Its middle term on X is
locally free because the quotient is locally free and the sequence
splits over each local ring. Thus the constructed inclusions are actual
subbundle inclusions and the successive quotients are precisely the H_i.

Finally the constructed K_s and the original double dual are reflexive
and agree off P. The reflexive Hartogs property identifies them uniquely.
The canonical injection E into its hull is an isomorphism there, so its
quotient is indeed supported on P. This is stronger than an equality of
Chern characters or a chosen abstract bundle with the same invariants.

## 5. Equivariance and conclusion

The resulting hull has the exact hypotheses of E818: local freeness,
an actual subbundle filtration with stable locally free quotients of
the same slope, and the given normalized balanced character. If the
point defect is nonzero, E817 applies to the canonical double-dual
sequence. If the defect is zero, E813 applies to the locally free sheaf.

A chosen stable-factor filtration need not be equivariant. Only the
specified coherent action on E and the functorial actions on its
canonical hull and defect enter the final categorical step. The exact
finite translation/tensor scope of E817/E818 is preserved. This is not
an exclusion of all unstable sheaves or arbitrary perfect complexes.

The new argument passes in full. It closes the singular-hull and
singular-stable-factor escape for the stated semistable torsion-free
balanced sheaves, once the separately reviewed E834 is included. No
numerical certificate, TeX compilation or unreviewed analytic theorem
has been substituted for the actual extension proof.

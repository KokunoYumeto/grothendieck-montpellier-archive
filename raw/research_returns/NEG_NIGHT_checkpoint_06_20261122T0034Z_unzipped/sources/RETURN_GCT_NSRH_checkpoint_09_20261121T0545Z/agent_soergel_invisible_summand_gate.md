# F59 further amendment: no generically invisible direct-summand repair

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited effort is not exposed. Date: 2026-11-21 UTC.

This is a separate amendment to the scalar-complex tests. It excludes adding a generically acyclic direct summand to a global free graph part carrying the generic cohomology. It does not split arbitrary extensions or exclude every nonfactorable nonflat complex.

## 1. Exact category and statement

Let A be a positively graded polynomial algebra over a characteristic-zero field k, with A_0=k. Let tau be a nontrivial graded involution of A. Write A_e for the identity graph bimodule and A_tau for the graph bimodule whose right action is twisted by tau. Let m=A_{>0}, the homogeneous origin, which tau preserves.

Work in the bounded derived category of graded A-bimodules which are perfect as left modules and as right modules, with finite graded cohomology on both sides. The tensor product is derived tensor over A. All scalar complexes below are bounded complexes of finite graded k-vector spaces. Write Q for the fraction field of A. In this statement, generically acyclic means explicitly that Q tensor_A^L Z is zero; no assertion of monoidality for arbitrary double-localized bimodules is required. The graph summands acquire their canonical right Q-actions after left localization, and this suffices for the calculation below. In the ordinary type-A application it agrees with the checked generic Soergel localization.

### Proposition IS-A

Suppose there is a graded derived decomposition

\[
 X=(U\otimes_k A_e)\oplus(V\otimes_k A_\tau)\oplus Z,
 \tag{IS1}
\]

where U and V have nonzero cohomology and the generic localization of Z is zero. If an actual derived isomorphism

\[
                       X\otimes_A^{\mathbf L}X
                             \simeq C\otimes_kX
 \tag{IS2}
\]

exists for a scalar complex C, then Z is zero in the derived category.

In the actual scalar-complex problem with ambient class P_s and Euler coefficient delta squared, this excludes a repair of the form (IS1): after Z vanishes, all cohomology is globally graded free on the left, and Proposition SC-B applies.

## 2. Generic cohomological multiplicities

Forget internal grading and put

\[
 u(t)=\sum_i\dim_kH^i(U)t^i,\qquad
 v(t)=\sum_i\dim_kH^i(V)t^i,\qquad
 d(t)=\sum_i\dim_kH^i(C)t^i.
 \tag{IS3}
\]

The generic cohomology character of X is u(t)e+v(t)tau. The localized X is a sum of graph complexes and therefore has an invertible right action of every nonzero element of A. Consequently its tensor with X equals its tensor over Q with Q tensor_A^L X; left-localizing the square introduces no uncontrolled middle localization. Since tau squared is e, generic Kunneth and (IS2) give

\[
 u(t)^2+v(t)^2=d(t)u(t),\qquad
                 2u(t)v(t)=d(t)v(t).
 \tag{IS4}
\]

The Laurent polynomial v(t) is nonzero, so the second equation implies d=2u. The first then gives v squared equal to u squared. The coefficient ring is a domain and u+v is nonzero, so v=u. In particular, with

\[
                         h=u(1)=v(1)>0,
\]

the total scalar cohomology dimensions are

\[
                \dim H^*(U)=\dim H^*(V)=h,\qquad
                \dim H^*(C)=2h.
 \tag{IS5}
\]

Only these ungraded dimensions will be used. No internal shift equality is inferred from generic localization.

## 3. A positive finite derived-fiber size

For any object M in the displayed category define

\[
 \mu(M)=\sum_i\dim_kH^i(k\otimes_A^{\mathbf L}M),
 \qquad k=A/\mathfrak m,
 \tag{IS6}
\]

where the fiber uses the left A-action and the remaining right action is forgotten. Since M is left-perfect, this is a bounded complex of finite-dimensional k-spaces; hence mu is a finite nonnegative integer. It is additive on direct sums and invariant under derived isomorphism.

It also detects nonzero graded objects. Indeed, if r is the highest degree with H^r(M) nonzero, then top-degree truncation gives

\[
 H^r(k\otimes_A^{\mathbf L}M)
       = k\otimes_AH^r(M)\ne0.
 \tag{IS7}
\]

The last nonvanishing is graded Nakayama for the nonzero finite graded module H^r(M). Higher Tor contributes only below the displayed top degree. Thus mu(M)=0 implies M=0.

For a scalar complex W, Kunneth over k gives

\[
                  \mu(W\otimes_kM)
                    =\dim_kH^*(W)\,\mu(M).
 \tag{IS8}
\]

The graph bimodules have mu(A_e)=mu(A_tau)=1. Right tensoring M by A_tau leaves its underlying left module unchanged up to the canonical graph twist identification. Left tensoring by A_tau twists its left action by tau or its inverse; tau preserves the homogeneous origin, so the derived origin fiber has the same dimension. Consequently

\[
 \mu(A_\tau\otimes_A^{\mathbf L}M)
       =\mu(M\otimes_A^{\mathbf L}A_\tau)=\mu(M).
 \tag{IS9}
\]

All products used below are still left-perfect, so their mu is finite. To see this, regard the second factor as a left-perfect complex built from finitely many shifted copies of A by cones and direct summands. Derived tensor with a left-perfect first bimodule sends that finite construction to one built from the first factor. Bounded right perfection also stays within the specified bimodule category.

## 4. Proof of the proposition

Set Y=(U tensor A_e) direct sum (V tensor A_tau), so X=Y direct sum Z. Formula (IS5), the four graph products, and (IS8)-(IS9) give

\[
 \mu(Y\otimes_A^{\mathbf L}Y)=4h^2
                       =\mu(C\otimes_kY).
 \tag{IS10}
\]

The two cross terms each have size 2h mu(Z):

\[
 \mu(Y\otimes_A^{\mathbf L}Z)
   =\mu(Z\otimes_A^{\mathbf L}Y)
   =2h\mu(Z),
 \qquad
 \mu(C\otimes_kZ)=2h\mu(Z).
 \tag{IS11}
\]

Apply the additive nonnegative function mu to (IS2) and expand the direct sums. The common term 4h squared cancels numerically. The resulting equality is

\[
                         2h\,\mu(Z)+\mu(Z\otimes_A^{\mathbf L}Z)=0.
 \tag{IS12}
\]

Both terms are nonnegative and h is positive, so mu(Z)=0. Derived graded Nakayama as proved in (IS7) gives Z=0. This proves IS-A.

No cancellation theorem for objects, Krull--Schmidt premise, or bimodule formality is used. Only an actual direct-sum decomposition is assumed. The argument uses the ordinary positive total cohomology dimension of a derived fiber, not its Euler characteristic.

## 5. Exact remaining scope and dictionary

The theorem rules out a globally graph-free summand together with a generically invisible correction supplied as a direct summand. It does not show that a general coupled complex admits that decomposition. Nonsplit extensions carrying nonflat cohomology remain outside the argument. In particular, replacing a singular extension by the direct sum of its generic graph part and its torsion would assume the very splitting that has not been proved.

The affine module/sheaf framework is EGA I, Theorem 1.3.7, p. 86, Corollary 1.3.8, p. 87, and Theorem 1.4.1, pp. 90-92. The finite perfect complexes and derived fibers use SGA 6, I, Definition 4.7, pp. 121-122, and Example 4.8, p. 122. The grading is the split-torus action framework of SGA 3, I, 4.7.2-3, with cote 90, scan 17. The effective dimension versus virtual Euler distinction has the coefficient language of SGA 6, V, Sections 2-3, with cote 133, scan 18.

Every derived-fiber nonvanishing and size implication needed here is proved with its exact finiteness and grading hypotheses. No cohomology-and-base-change claim is substituted for it. The dictionary does not confer a lambda-ring structure on the noncommutative word algebra, identify a canonical source lattice, or introduce arithmetic Frobenius or Weil purity. The result is an ordinary coherent categorical rigidity test.

Fresh whole-proof review is requested before integration. The previously frozen reports and fragments are unchanged.

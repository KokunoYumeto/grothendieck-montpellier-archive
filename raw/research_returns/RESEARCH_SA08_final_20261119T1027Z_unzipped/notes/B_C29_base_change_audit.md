# Complete audit of C29 scalar extension and the local-prime slope

2026-11-19, /root/automorphisms. Independently read the full final
section of notes/C_relative_bar_extension.md. The refinement is valid
with the same finite-arity, target-range, and full-boundary hypotheses.
It is not used to assert global C3.

## 1. Derived scalar extension in simplicial modules

Let R be Z or Z_(p), let k be an arbitrary commutative R-algebra,
and consider the abelian categories S_R=sMod_R and S_k=sMod_k.
Extension k tensor_R - is left adjoint to the exact restriction
functor. It therefore preserves projective objects and has the usual
derived adjunction.

If Y is a simplicial R-module whose levels are R-flat, then its
derived extension of scalars is its ordinary extension. Indeed a
projective S_R-resolution evaluates in each simplicial degree to
a projective R-resolution: S_R-projectives are retracts of sums of
free representable simplicial modules, whose levels are free.
Evaluation is exact. Consequently the levels of the positive
derived-extension homology are Tor_i^R(k,Y_n)=0 for i>0.

The arity-m indecomposable complex Q_R=Q_m(K(R,n)) is bounded
in the vertical direction and each of its terms is levelwise free.
Its relative quotient counterpart has the same property, by C24's
basis-subset argument for a split free parameter inclusion.
Apply the preceding acyclicity termwise and then the finite vertical
filtration. This proves

    k tensor_R Q_R = k tensor_R^L Q_R

in D(S_k), and likewise for the relative quotient. This argument
does not assume that k is flat over R, or that Q_R's terms are
projective objects of S_R.

Base change of free divided powers, exterior powers, and the
signed-Lyndon basis identifies the ordinary extension strictly
with the corresponding complex over k. Derived adjunction now gives

    RHom_(S_k)(k tensor_R Q_R, constant k)
      = RHom_(S_R)(Q_R, constant k).

The target on the right is the constant simplicial R-module whose
underlying module is k. Every projective-dimension bound used in
C27/C29 vanishes against this target as it does against any R-module;
it never required that the target be R itself.

## 2. Integral ranges

For odd disk form degree q, the integral Euler argument gives
H^j(Q_m)=0 for j<=qm. Its normalized homology on K(Z,n) is supported
through n floor(m/2), and hence has S_Z-projective dimension at most
n floor(m/2)+1. The absolute inequality n<=2q makes this at most
qm+1, so all positive derived-Hom groups vanish. The relative
inequality n<=2q-1 makes it at most qm, so degree-zero absolute
derived Hom also vanishes. The relative exact triangle shifts that
degree-zero group to the required degree-one relative obstruction.

Derived scalar extension proves these same integral slope bounds
over every k, with no flatness assumption on k. The ordinary-to-derived
Hom comparison still uses the stated horizontally acyclic target rows
and projective normalized source terms; these conditions are preserved
for the source because the relevant integral normalized summands are
projective and are then extended to k.

## 3. Sharper p-local ranges

Over R=Z_(p), the Euler homotopy for any basis multiplicity n_i
makes n_i times the identity nullhomotopic on that multidegree.
If p does not divide n_i, that component is contractible. Thus
nonzero homology uses only variables with positive multiplicities
divisible by p, and at most floor(m/p) distinct variables.

The cut-set degeneracy argument therefore bounds normalized support
on K(R,n) by n floor(m/p). Since R is a PID, projective dimension
in S_R is at most n floor(m/p)+1. The bottom cochain term is R-free,
and its kernel is torsionfree; total Euler kills its homology by m,
so H^j is still zero for j<=qm.

If p does not divide m, total Euler contracts the entire Q_m.
Otherwise write m=pa. For the absolute range n<=pq,

    n a+1 <= qm+1 <= j

for every possible nonzero H^j; hence all Ext^(j+t), t>0, vanish.
For the relative range n<pq, the integer inequality n<=pq-1 gives

    n a+1 <= qm-a+1 <= qm < j,

so Ext^j also vanishes. The same relative exact triangle as in C29
then kills the degree-one extension obstruction. The horizontal
contractibility of Q_m on the parameter disk is valid against every
constant R-module, by the derived H0/constant adjunction of C22.

Applying Section1 proves the absolute slope n<=pq and the relative
slope n<pq for every Z_(p)-algebra k. This avoids the false inference
that a torsionfree-kernel argument could be performed directly over
an arbitrary k with torsion.

## Scope

This confirms the previously audit-pending paragraph. It gives
finite-arity strict lifts under the stated finite target bounds.
The relative theorem still requires the full old bar boundary map.
It does not cover arbitrary unbounded horizontal cell dimensions,
does not produce one weight satisfying all arities, and does not
construct the local completions in C34.

Audit event: C29-base-change-local-slope-independent in
notes/B_CHECK_EVENTS.tsv. The full argument was communicated to
topos and root before the final source freeze.

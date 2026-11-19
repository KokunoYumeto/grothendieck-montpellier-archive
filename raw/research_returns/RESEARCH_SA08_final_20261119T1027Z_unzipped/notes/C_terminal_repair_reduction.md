# C32: a conditional reduction for terminal localization

2026-11-19, agent /root/topos. Root proposed the constant-cohomology target
extension of C30. This note states precisely the additional local repair
hypothesis; it does not infer that hypothesis from ordinary admissible
target repairs.

## Targets needed

For admissible A,B, let T_pair=A times_k B in the category of augmented
strict PD-DGAs (the pullback of their augmentations). Its positive-weight
rows are the direct sum of those of A,B; the coefficient map is diagonal.
It is horizontally eventually acyclic, and its vertical cohomology in
large weights is the constant S^w direct_sum S^w in degree0 only.

For parallel f,g:A->B define the strict simplicial homotopy equalizer

    T_eq = A times_(B times B) B^I,

where the maps are (f,g) and the two endpoints. All operations are
pointwise. In the horizontal acyclic range, endpoint restriction is
surjective; its kernel is horizontally acyclic. Thus T_eq is horizontally
eventually acyclic. C16's both-endpoint vertical calculation gives H0=S,
H1=S, and zero higher vertical cohomology, in every fixed eventual range:
the connecting map on coefficients is f-g=0. These are constant
simplicial modules, naturally. The target has its augmentation and
coefficient map but is generally not an admissible theory.

For either target T, the linear-disk algorithm of C21 produces P_T->T.
The proof uses only the horizontal eventual acyclicity of target rows,
not their vertical comparison. It therefore still gives free terms,
uniform horizontal bounds, and vertical exactness through degree d after
inverting floor((d+1)/2)!. In particular (P_T)_Q is admissible.

## Explicit repair hypothesis

For every target of the two displayed kinds, assume that the specified
P_T admits for every prime p a factorization

    (P_T)_p -> E_(T,p) -> T_p,

where E_(T,p) is admissible and the first map is an actual isomorphism
in every weight and simplex in form degrees q<d_(T,p), with d_(T,p)
tending to infinity as p tends to infinity. The second map must extend
the prescribed P_T map. For the optional flat category over Z require
these local repairs to have flat terms.

Claim: under this hypothesis the generalized category has common sources
and its localization at all arrows is terminal. Arbitrary k is allowed
without optional termwise flatness; the flat conclusion here is only over
Z. The support condition q<=weight, if imposed throughout, is preserved.

## Arithmetic replacements for constant-cohomology targets

More generally let T be horizontally eventually acyclic and suppose that
in each fixed cochain range its vertical cohomology is, in sufficiently
large weights, a constant simplicial module in every degree. No vanishing
of positive cohomology is assumed. For a contractible prism Delta[n] times I
with one endpoint included, relative cohomology of every such constant
module is zero. The finite-range slice hypercohomology argument of C16
therefore gives eventual vertical acyclicity of the based-path module
P_0(T). The bound is uniform in n: horizontal acyclicity makes each
relevant row acyclic on every slice, and only finitely many cochain rows
and comparison degrees enter the first-quadrant calculation.

Let R=product_p Z_(p) and RQ=R tensor Q. Define J(T) using the arithmetic
path pullback of T_Q and T_R over T_RQ. The pure arithmetic exact sequence
of C30 yields, in every row and every simplex, an exact sequence

    0 -> T -> J(T) -> P_0(T_RQ) -> 0.

Thus eta:T->J(T) is a horizontal weak equivalence in every row, and is an
eventual vertical quasi-isomorphism in every fixed range. J(T) has the same
eventual constant vertical cohomology; it need not be admissible.

Its mapping path

    T_tilde = T times_(J(T),ev0) J(T)^I -> J(T)

is a trivial fibration in every simplicial module row, because eta is a
horizontal weak equivalence. Its kernel is horizontally acyclic. The
projection T_tilde->T has a based-path kernel, eventually vertically
acyclic by the preceding constant-cohomology argument. Hence the map
T_tilde->J(T) is an eventual vertical quasi-isomorphism; since it is
termwise surjective, its kernel is eventually vertically acyclic too.

## Glue and pull back

Apply C30's finite-idempotent construction to the repairs E_(T,p).
It gives an admissible E_R and a map P_R->E_R->T_R. Both E_R and P_Q
are admissible, so their one-edge arithmetic path pullback E is admissible
by exactly the C30 proof. Commuting endpoint diagrams give E->J(T).
No admissibility of T was used in constructing E itself.

Define H=E times_(J(T)) T_tilde. Its projection to E is degreewise
surjective with the kernel just described, horizontally acyclic in all
rows and vertically acyclic in every eventual finite range. Therefore H
is admissible and has an actual map H->T. In the flat Z case, all fiber
products and kernels are subgroups of torsionfree abelian groups, hence
flat. All gradings and the optional support condition are preserved.

For T_pair this is an actual common source for A and B. For T_eq it gives
h:H->A and a strict simplicial PD-DGA homotopy f h~g h into B^I.
The two endpoints B^I->B become equal when all arrows are inverted:
both are inverses to the constant-path map B->B^I. Hence f h=g h in the
localization, and since h is inverted, f=g there.

## Why this kills every localization loop

Every two objects have a common source, and repeated application gives
a common source R for the finitely many objects in any zigzag loop.
Choose maps r_i:R->X_i. For every edge u:X_i->X_j, the maps u r_i and r_j
are parallel and thus equal after localization. Every edge is therefore
r_j r_i^(-1), with orientation reversed when the zigzag traverses it
backwards. The product around the loop is the identity. The category is
nonempty (the standard theory exists), so the localized groupoid is
connected and has trivial vertex groups: it is terminal.

## Scope of the remaining hypothesis

This eliminates a separate infinite arithmetic descent and loop-gluing
problem once the stated local extension repairs exist. It does not
construct those repairs. In particular, repairs into admissible targets
alone do not automatically extend to T_eq, whose H1=S is nonzero. The
higher exactness of T_eq is compatible with a high-degree repair strategy,
but compatibility has to be proved. C31 demonstrates that a full bar
boundary cannot simply be assumed from vertical exactness and eventuality.

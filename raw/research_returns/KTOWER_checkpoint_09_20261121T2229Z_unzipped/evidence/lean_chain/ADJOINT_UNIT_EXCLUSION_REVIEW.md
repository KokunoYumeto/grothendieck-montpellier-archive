# Independent review: normalized adjoint-branch unit exclusion

Reviewer `/root/lean_chain`; GPT-6 Astra Pro; effort not exposed.
21 November 2026. **PASS** after a complete read of the final
`../unitary_audit/reducible_comparison/adjoint_unit_exclusion.tex`.
The reviewed hash and time are in
`adjoint_unit_exclusion_review_manifest.json`.

The theorem explicitly assumes a finite-coefficient absolutely
irreducible G_Q representation V with determinant eta chi^e. The
residual three-character hypothesis is for Ad^0(V) restricted to G_E,
not for its global G_Q representation. I requested that statement
clarification; it is included in the reviewed final version.

## Residual splitting and scalar recovery

The residual adjoint is triangularizable over a finite coefficient
extension because all its composition factors are characters.
Faithfulness of the trace-zero adjoint representation of PGL2 in odd
characteristic identifies its projective image with that triangular
image. The kernel of the diagonal character map is a normal p-group;
the quotient is abelian of order prime to p.

A nontrivial finite p-subgroup of PGL2 has a unique fixed projective
point: a central order-p element is unipotent with a unique fixed
point, and the group is conjugate into translations. Normality then
forces the full image to preserve that point. If the p-subgroup is
trivial, the abelian projective image has an element of order greater
than2, since psi has such order. The centralizer of that element is a
torus; the possible eigenline-swapping component would force the
element to equal its inverse. Thus the residual rank-two restriction
is reducible in either case.

The ratio on G_E is psi after ordering the lines. Semisimple
restriction to the normal subgroup is justified by the finite-image
socle argument. The two global conjugates cannot exchange the lines
because psi is conjugation-invariant and psi differs from its inverse.
The global ratio is eta^t psi. At complex conjugation, the assumed
determinant and evenness of e force t=1. Combining the exact
determinant with the ratio forces the common residual scalar to be
quadratic. Its lift nu is therefore the canonical sign-valued
character. No unjustified character square root is used.

## Local flag and the scalar twist

The highest inertia eigenline in the adjoint occurs with multiplicity
one, so it is stable under the whole rational decomposition group,
even when the auxiliary prime is inert. A nonzero trace-zero matrix
on that line has determinant0 because inertia scales it by an
infinite-order character while preserving its determinant. It is a
rank-one nilpotent; its common kernel and image gives a stable line
in V.

The adjoint eigencharacter is the ratio of the line and quotient
characters. Together with detV=eta chi^e this forces the quotient's
inertial square to be1. The residual ratio psi has order greater
than2, so the quotient must reduce to the scalar nu, not nu psi.
Injectivity of reduction on signs gives equality of the actual
inertial characters. Twisting by nu makes the quotient unramified.

At any other prime, the adjoint's triviality on inertia intersected
with G_E makes V scalar there. The determinant condition forces that
scalar to be a sign, and the residual pair identifies the sign with
nu. The same single global twist therefore removes all such inertia.
The resulting representation has exactly the three hypotheses of the
already reviewed ordinary rank-two exclusion.

## Scope

The argument uses the exact ordered adjoint inertia flag, not a
converse from adjoint crystallinity. It applies to actual source
points once a G_Q rank-two adjoint origin with the stated determinant
is identified. It includes the constructed lower-weight classical
adjoint subspace for E=Q(sqrt(−3)); it does not classify every stable
rank-three source as such an adjoint.

Removing the determinant normalization, or proving odd G_Q descent
for an arbitrary adjoint origin over E, is a separate investigation.
Neither conclusion is silently included in this PASS. No Lean kernel
build was run.

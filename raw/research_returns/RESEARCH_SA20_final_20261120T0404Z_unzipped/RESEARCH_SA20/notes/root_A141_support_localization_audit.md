# Root audit of the support-localized four-dimensional loop theorem

We read every line of
`agents/higher_comparison/support_localized_four_loop_draft.tex`.
The mathematical proof is **PASS**. We requested two minor corrections
before promotion as A.141: the missing backslash in the displayed left
delimiter, and an explicit appeal to the general A.136–A.137 trace identity
for the inclusion of the ordinary-loop image in J_B. The trace homomorphism
is defined for every closed B; simple connectivity is a realization input
for the supported submanifold W, not a hypothesis on B.

For a compact simply connected codimension-zero PL submanifold W in B,
the correct relative group is H²(W,boundary W;Z/2). The cylinder lift
difference lies in H³(W times I,boundary(W times I);Z/2), with all vertical
faces retained. We checked action triviality using absolute homology and
Poincare–Lefschetz duality: the bottom inclusion is a homotopy equivalence,
and a bottom-fixed homeomorphism acts identically on absolute homology.
The natural affine cocycle is consequently additive on the maps used.

The OPR boundary conventions apply literally to W. The same triple
connecting-map argument as A.140 identifies its KS class with the relative
duality image of kappa_W. The assembly domain and Bockstein target vanish
because W is simply connected. The exact block sequence first supplies
a concordance to a diffeomorphism; composition with the normalized smooth
pseudo-isotopy makes both endpoint maps literally identity. The corrected
GGHKP theorem then supplies the separate ordinary path relative to bottom
and vertical boundary. The trace comparison yields every relative class
by an ordinary loop of W automorphisms. No block loop has been relabeled
as an ordinary one.

We checked the explicit collar compression carefully. The function
sigma_a(t)=min(t+a,(t+d)/2) is strictly increasing on [0,d], maps it onto
[a,d], equals the identity at a=0, and fixes d. Conjugation on its image
glues to identity on the removed collar because each loop map fixes the
boundary. The compact family's uniform continuity, for both maps and
inverses, gives joint continuity at a=0. At positive a the loop is identity
on a common spatial collar. A based time reparameterization makes the
trace identity near both temporal ends without changing its class.

Extending the resulting loop by identity gives an actual jointly continuous
loop on B, including its inverse family. Its relative PL lift is standard
outside the smaller cylinder and agrees literally on the gluing collar.
Naturality of the universal KS difference therefore identifies its class
with extension by zero j_!. We checked the duality identity
PD_B j_! = j_* PD_W using compatible finite chains; all outside simplices
give zero, and the boundary cochain is zero. Thus the realized subgroup
is precisely PD_B inverse of the image of H2(W) in H2(B).

When that homology map is onto, ordinary loops realize all H²(B;Z/2).
The general trace identity places this image inside J_B, so J_B is the
whole group. A.137 then gives im(pi0 c_P)=I_B. We checked that the proof
retains the endpoint-isotopic-to-PL condition defining I_B; it does not
claim that every concordance component passes that condition.

For B=C connected-sum D, take W to be C minus an open standard PL ball.
Van Kampen with the simply connected gluing sphere gives pi1(W)=0.
Removing the ball preserves H2, and Mayer–Vietoris along S3 identifies
H2(B) with H2(W) direct-sum H2(D). The required map is onto exactly under
the stated zero-H2 condition on D. This includes finite connected sums of
S1 times S3 and the k=0 case. No assumption on the assembly map of pi1(B)
is needed. This is a general subgroup-evaluation theorem, not a finite
counterexample requiring a new computational certificate.

All original source inputs are those opened and inspected for A.140,
now with their explicit compact-boundary scope. The original main row
remains incomplete on endpoint recognition and the whole comparison.

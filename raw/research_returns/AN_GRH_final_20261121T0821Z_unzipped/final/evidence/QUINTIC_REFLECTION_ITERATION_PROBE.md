# Scope of the all-156 and iterated quintic-reflection attempt

Date: 2026-11-21. Reader: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Result of this bounded probe

No theorem supplying a canonical detector for every prescribed lifted collision was obtained. In particular, neither ordinary Hecke-orbit density nor the checked Prym-map results establish the needed reachability statement. The zero-correspondence calculation below is already explicit in A33, not a new finding. This note records the exact remaining question and the scope of the sources checked; it is not a claim that reflection iteration cannot work.

## What varying all cyclic-five covers actually varies

Let C be a smooth proper geometric genus-two curve in characteristic two. Its connected cyclic-five covers, considered up to isomorphism over C and without a chosen generator of their deck groups, are the nonzero elements of H^1_et(C,F_5) modulo F_5^×. The vector space has dimension four. Therefore there are exactly

\[
                 (5^4-1)/(5-1)=156
\]

geometric cover classes. This is the usual prime-to-characteristic Jacobian torsion description used in A33. It is a count of geometric classes, not a count of forms over a fixed finite field. A finite constant extension can define all these finitely many covers, their deck groups, reflections, and any specified finite collection of lifted points. It does not add new geometric cover classes above the same C.

For one cover π:D→C, choose a deck generator σ and a reflection τ. All five reflection quotients are isomorphic: conjugation by powers of σ permutes the reflections transitively. After identifying their targets with E=D/⟨τ⟩, changing the reflection or the lift of a prescribed point produces the same set of at most five points

\[
                       v(σ^jP'),\qquad 0\le j<5.
\]

Thus one step from a fixed pointed geometric curve has at most 156·5=780 pointed targets, with repetitions possible. This observation is consistent with the all-reflection and all-lift scope already proved in A41/A43. It does not make a generic statement about those 780 canonical classes.

If an actual collision is being transported, one must keep the *same* lifted pair P',Q'. At most one reflection can identify that pair: equality of their images under the quotient by σ^iτ means Q'=σ^iτP' when P'≠Q'; if this held for two distinct reflections, a nonidentity power of σ would fix P', contrary to the free deck action. Consequently at least four of the five reflection maps preserve distinctness. A detector at an image is useful for this collision only along a map that preserves distinctness. This is the reason that the two-reflection argument in A33 tracks both maps, rather than treating an arbitrary good image as sufficient by itself.

## The natural map is zero, and that is already A33

The relevant maps of Jacobians satisfy

\[
        π_*v^*=0,\qquad v_*π^*=0.
\]

Indeed τ induces the hyperelliptic involution on C, hence acts as −1 on π^*J_C, while v_*τ=v_*. Therefore the homomorphism v_*π^* equals its negative and is killed by two. A homomorphism of abelian varieties killed by a nonzero integer is zero: its image is a connected abelian subvariety contained in a finite group scheme. The adjoint relation gives the other equality.

This is not an additional result. A33, Step 2, proves π_*v^*=0 before deriving the Prym isogeny. Its conclusion is

\[
             J_D\sim J_C\times J_E^2.
\]

A40, Step 4, recovers J_C as the polarized complement of the two pulled-back J_E copies. The reflection operation selects a Prym factor; the natural correspondence does not exhibit an isogeny between J_C and J_E. The vanishing does **not** prove that these two Jacobians can never happen to be isogenous by some unrelated map. When the source has 2-rank one and the surviving target is ordinary, their different 2-ranks do rule out an isogeny, but that argument does not cover an ordinary source.

Source-overlap check: A33 paragraphs immediately preceding (DR.6), and A40 (ID.17)–(ID.20), were reread for this note. No new proof ID should be assigned to the zero map.

## Primary orbit and Prym results inspected

| Primary source | Exact scope read | Why it does not supply the required step |
|---|---|---|
| C.-L. Chai, *Every ordinary symplectic isogeny class in positive characteristic is dense in the moduli*, Invent. Math. 121 (1995), 439–479; introduction pp.439–440 and Theorem 2 p.477 | The orbit is defined by polarized isogenies whose multiplier is a power of a fixed prime ℓ≠p. The theorem gives its Zariski density for every ordinary point. | No identification of reflection iteration with this isogeny orbit has been established. The natural map above is zero. The theorem concerns the abelian variety, and also does not by itself control the canonical class of the transported point. |
| A. Albano and G. P. Pirola, *Dihedral monodromy and Xiao fibrations*, Ann. Mat. Pura Appl. 195 (2016), 1255–1268, DOI 10.1007/s10231-015-0514-y | The opened author manuscript's introduction explicitly works with complex surfaces and constructs families from fibres of the dihedral Prym construction. The degree-five, genus-two case is one of its positive-dimensional fibre cases. | This is a family in varying complex moduli, not a characteristic-two orbit theorem for the finitely many covers of one fixed curve. The full proof of its fibre theorem was not read in this probe. |
| J. C. Naranjo, A. Ortega, G. P. Pirola, I. Spelta, *Families of simple Jacobians with many automorphisms*, Algebraic Geometry 12(6) (2025), 869–887, DOI 10.14231/AG-2025-026; pp.870–871 | The explicit setup is complex. Theorems 1.1–1.3 and the complete displayed proof of Proposition 2.1 were read. The generic finiteness and injectivity ranges exclude (g,d)=(2,5). The introduction explicitly records the positive-dimensional fibre exception in that case. | Its monodromy varies (C,η) in moduli. It does not imply that some point in the fibre above each fixed finite-field C has a prescribed arithmetic property, or that repeated reflection quotients reach such a point. |

Primary URLs and retrievable references:

- Chai: https://www2.math.upenn.edu/~chai/papers_pdf/density_hecke_orbit.pdf ; opened reference `turn564996083view0`, theorem-location reference `turn212777914view2`.
- Albano–Pirola author manuscript: https://iris.unito.it/retrieve/e27ce428-62f8-2581-e053-d805fe0acbaa/1406.6308v3.pdf ; opened introduction `turn564996083view1`. Later requests for the inner pages returned 403. This is why this note does not claim a complete reading of that theorem's proof.
- Naranjo–Ortega–Pirola–Spelta: https://api.algebraicgeometry.nl/Article/21295/2025-6-026.pdf ; opened setup/statements/proposition proof `turn868560913view0`.

The bounded search also inspected Agostini's degree-at-least-six genus-two Prym result (arXiv:2001.06264, Theorem A). Its stated range does not include degree five. No conclusion here uses an unverified extension of any complex result to characteristic two. No exhaustive literature-search claim is made.

## The precise remaining reachability question

For a pointed ordinary integral-O_5 curve (E,R), call R canonically detectable if κ_R=[K_E−2R] has a nonzero primary component at an odd prime r with ord_r(2) even. A29 then supplies a pointed cyclic prime-power detector after making the required arithmetic data rational. This property of the *fixed geometric class* κ_R is unchanged by constant extension; the order of that class and its prime support do not change.

One can form the multivalued reflection process by choosing a geometric cyclic-five cover, lifting the prescribed point, and passing to a reflection quotient. For an assumed section collision, the process must instead be formed on triples (C,P,Q), with a common lifted collision and an edge only when the two target images remain distinct. A target of 2-rank zero supplies the earlier geometric route. At ordinary targets, a canonically detectable first image on such an edge would contradict the transported collision.

What remains unproved is that every initial collision has a finite path reaching one of these successful targets. The finite set of one-step choices is exact; it provides no uniform bound on the depth, no invariant excluding a closed failing orbit, and no theorem forcing a good primary component in one of the image classes. Subsequent steps change the geometric curve and its point, so they are not exhausted by the original 156 choices.

The dense sets of useful points supplied by A42 lie on each fixed target curve. A prescribed lift gives only finitely many images at the next step, and no incidence theorem places one of those images in that dense set. Likewise, even a density statement about the *unpointed* reflection targets would require a further pointed arithmetic argument. The good-primary condition is not asserted here to be a nonempty Zariski-open condition on that moduli orbit.

A41/A43 establish failure for specified covers and all their reflection choices. They do not establish simultaneous failure for all 156 covers of their source curves. Conversely, A36's absence of rational 5-primary classes on one target does not rule out a different cover, a different target, or a good prime other than five. This probe supplies neither of those missing universal assertions.

## Check record

- Reread the exact A33 and A40 arguments proving the orthogonal Prym decomposition and the source of the zero map.
- Verified the finite count, reflection-conjugacy reparametrization, and at-most-one collapsing-reflection argument directly in this note.
- Read the primary statements and scope listed above; no claim of reproving Chai's density theorem or reading all its dependencies.
- No new finite-curve enumeration was run, and no assertion about all 156 covers of an actual example was certified.
- Status: a documented inapplicability of the proposed automatic Hecke/monodromy shortcut; the main existential reflection-selection gate remains open. This note is not new main-gate movement.

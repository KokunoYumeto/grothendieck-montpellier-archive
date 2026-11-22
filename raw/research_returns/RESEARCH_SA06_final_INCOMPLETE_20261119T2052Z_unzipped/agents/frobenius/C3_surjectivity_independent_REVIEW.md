# Independent audit: the deformed-cone ordinary Picard surjectivity counterexample

## Scope and outcome

We independently read the entire draft `research/agents/real_weil/C3_surjectivity_draft.tex` on 19 November 2026. The construction and proof pass this audit. The result concerns ordinary algebraic equivalence defined by actual families on the fixed punctured scheme. It does not rely on identifying that relation with the connected component of a local Picard functor.

The claimed range is every complex local dimension N at least four. The source ordinary algebraically trivial Picard group is zero, whereas the target contains an injected copy of the Fermat quartic Jacobian, including a specified point of infinite order. Thus the ordinary J1 restriction map fails surjectivity integrally and rationally in this range.

## Geometry and first neighbourhood

1. In the total space of O(-1,-1) over P^m × P², the equation F+tℓH is globally typed as a section of O(0,4). The codimension-two locus F=ℓH=0 cannot contribute an additional irreducible component to its hypersurface. The Segre contraction is proper, is an isomorphism away from the zero section, and has the asserted radical equations on its reduced image.
2. Smoothness near the exceptional V=P^m × C follows from dF. Properness permits removal of the image of the nonsmooth complement. The map factors through the finite normalization, whose fibre above the vertex consists of one point: the proper surjection from the connected exceptional V cannot cover two points of a finite discrete fibre. Strict henselization preserves the relevant regularity and exceptional-divisor statements.
3. The principal function f=tℓ has smooth strict transform D equal to the total line bundle over the incidence projective bundle H0→C. This supplies a regular punctured target without a projective-normality assumption.
4. The first-neighbourhood deformation class is the boundary of ℓH in the normal sequence twisted by L. Its curve components δ(z_i H) are exactly the three surviving degree-five Fermat Jacobian-ring monomials. The dimensions used are consistent: h0(O_C(5))=18, the derivative image has dimension15, and its cokernel H1(O_C) has dimension3. The Euler-sequence computation gives H1(T_P²|C⊗K_C)=0.
5. Serre duality turns these three independent boundary classes into an injective contraction cκ:H0(K_C)→H1(V,L). The same argument has rank3 for every m≥2.

## The integral family argument

The key improvement over the earlier possible route is that the proof uses the obstruction for an actual Poincaré family. It does not infer a global vector-group extension from a tangent calculation.

The square-zero extension obstruction for a line bundle on V×P is κ contracted with its V-Atiyah class. Its mixed component is the image of the normalized Poincaré tensor under cκ. Since cκ is injective, an extension to V2×P forces ψ*:H1(J,O_J)→H1(P,O_P) to vanish. For a homomorphism of complex abelian varieties this forces ψ=0. Normalization by the Abel-map diagonal identifies the mixed tensor correctly; only an irrelevant overall sign depends on conventions.

The previously audited finite-descent and smooth-compactification argument supplies an actual line bundle on X×P with P an abelian variety and fibre0 trivial. Its divisor closure on the regular noetherian product Z×P is Cartier. The fibre0 correction is O(bV), since V is the sole boundary prime divisor. Restriction to V×P is therefore a family in Pic0(V), and the obstruction proves that all its fibres there are trivial after a harmless pullback twist from P.

The square-zero unit sequence then expresses its class on V2×P by H1(V×P,L). The Künneth decomposition shows that restriction to any point of the proper connected P is the same map on the first summand and zero on the second. Hence all fibre classes on V2 agree, and the normalized fibre0 makes them trivial. For r≥2, both H1(V,L^r) and H2(V,L^r) vanish. The resulting Picard isomorphisms and surjective unit maps provide compatible trivializations on every infinitesimal neighbourhood.

## Completion and target injection

The equality m_R O_Z=I_V is justified in both directions: the old Segre coordinates generate the local ideal (t), and every additional normalization function in the maximal ideal vanishes on the reduced divisor V. Thus the V-adic formal neighbourhood is exactly the one to which proper formal full faithfulness applies after completing R.

Proper formal full faithfulness gives a trivialization on the completed resolution and hence on the completed puncture. A rank-one reflexive extension Q=j_*M is finite. Its local cohomology in degrees0 and1 vanishes; flat base change and the fact that the completion has a one-point closed fibre identify Q⊗Rhat with the extension of the now trivial punctured line bundle. It is Rhat. Faithfully flat descent makes Q a finite projective rank-one module over the local ring R, hence free. This closes the passage from formal triviality to the original strict local puncture.

The target injection Pic0(C)→Pic(Y) is also integral. A trivial target restriction would differ on the regular D by O(bH0). Restriction to a line in a P^{m−1} fibre gives b=0, and the projective-bundle Picard formula then gives the trivial source line bundle. This is where m≥2 is used essentially. The Poincaré family gives ordinary algebraic equivalence of its image. The point involving a transcendental coordinate has infinite order because all torsion points of the Qbar-defined Jacobian are Qbar-rational and the Abel map is a Qbar-defined closed immersion.

## Independently opened sources

- Illusie, *Cotangent complex and deformations of torsors and group schemes* (1972), Theorem2.6, printed p.166, and formula(2.7.2), printed p.167. Primary reprint opened at https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/ce/24/ce243c31-2953-498e-92cb-c8b2e70d207d/i_illusie-64.pdf . The torsor obstruction is exactly the extension class composed with the Atiyah class. For G_m the co-Lie term is the trivial line, giving the displayed H2 obstruction. The draft also provides a direct Čech proof.
- Illusie's author errata, opened at https://www.imo.universite-paris-saclay.fr/~luc.illusie/ErrHalifax.pdf . Its corrections concern printed pp.177,185,189 and do not change the used theorem or formula.
- Stacks Project, Lemma30.24.1, Tag0883, opened at https://stacks.math.columbia.edu/tag/0883 . Its assumptions are precisely a noetherian complete base and a proper morphism; its conclusion is full faithfulness of formal completion for coherent sheaves. The proof uses it only after completing the base.

## Status limitation

This audit proves no assertion in dimension3 and makes no identification between ordinary Chow algebraic equivalence and all connected local Picard families. The construction establishes the stated failure of surjectivity for N≥4; previously proved injectivity results are compatible with a zero source.

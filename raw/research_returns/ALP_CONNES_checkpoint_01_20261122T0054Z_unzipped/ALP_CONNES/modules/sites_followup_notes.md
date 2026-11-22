# Follow-up sites / Jacobian / absolute geometry: research notes

## Scope

This module adds AC-G13–AC-G21 and does not replace the original AC-G01–AC-G12 module. A remains the supplied hypothesis/theorem that zeta and every primitive Dirichlet L-function satisfy RH. No Lean rebuild is claimed. Source references are to the attached LaTeX versions, not presumed later revisions.

## Main completed results

- **AC-G13 — definite source correction.** With Y_Q=Q^times\\A as defined, the infinity fiber is C_Q/R^times = Zhat^times/{+-1}. The supplied Jacobian theorem loses the sign in its kernel calculation. The two representatives (1_f,0) and (-1_f,0) are literally in the same Q^times orbit. Its Galois meaning is the maximal real abelian quotient, so odd characters cannot be read off as characters of this fiber.
- **AC-G14 — exact monoid distinctions.** Prime images Z[1/p] are nonidentity idempotents and therefore die under every monoid map to a group. The whole monoid is nevertheless not idempotent: the group of rational numbers with every prime denominator height at most1 has tensor-square heights2 and cannot be rationally rescaled to itself. This also refutes the isolated generic-fiber proof sentence that all rank-one subgroups of Q are cyclic; the generic-fiber conclusion for ideles remains valid.
- **AC-G15 — Euler-product synthesis, not an originality claim about Artin factorization.** Extend the finite associated mapping-torus description to bad primes using G/I_p. The lifted prime circles have lengths f_p logp and multiplicity |G|/(e_p f_p), giving the complete Dedekind Euler product. A gives the critical line for its abelian Dirichlet factors. Archimedean gamma factors are not inserted as periodic-circle factors.
- **AC-G16 — quantitative A consequence.** Fixed finite abelian covers have smooth repeated-base-orbit counts with main term x/|G| times the test integral and O(sqrt x) error. Removing repetitions gives O(sqrt x logx). Full Mellin-contour, local-factor removal and orthogonality proof included. No uniform conductor dependence claimed.
- **AC-G17 — trivial extension correction.** The identity cover is unramified everywhere under the source definition; compulsory infinity and infinitely many nontrivial prime restrictions need G nontrivial. Full corrected proof includes the CRT stabilizer construction. This source-specific infinity condition is stronger than ordinary archimedean field ramification.
- **AC-G18 — mixed-characteristic coordinate correction.** The compatible cyclotomic tower has zeroth coordinate1 without being the identity in the tilt. Deleting the trivial point means deleting the all-ones sequence, not the zeroth-coordinate fiber. Formal disk/untilt descriptions retain their stated hypotheses.
- **AC-G19 — precise tropicalization obstruction.** Negative valuation profiles preserve products but satisfy only an inequality for sums. The pair f,-f rules out the naive semiring homomorphism. This does not rule out a different categorical tropicalization. Endpoint extension and Frobenius descent are separate gates, and the source explicitly leaves eigenspace descent for future work.
- **AC-G20 — scope of the groups.** The stated monodromy groups are abelianized. Their finite quotients cannot supply S3. The topological additive automorphism group of Q_p is Q_p^times; it is not the full nonabelian local Weil group. A tame nonabelian finite quotient proves the distinction.

## Source-version qualifications

- Jacobian.tex uses duplicate label rankpro elsewhere. We use section plus exact statement for unlabelled fiber theorems.
- FF.tex duplicates thm:tate_decomposition in introduction and body. The inventory cites the body section explicitly and preserves its real-manifold product category.
- The formal untilt quotient uses both Z_p^times and p^Z; a prose shorthand mentioning only Frobenius should not erase the compact quotient.
- The perfectoid comparison under review assumes algebraic closedness when invoking the specified FF closed-point description. The basic local-disk theorem has the broader perfectoid-field scope.
- The knots source statements explicitly use abelianized etale fundamental groups. No Morishita character-orbit comparison is used in our proofs. Agent trace_windows separately identified its finite-kernel restriction and owns that correction.

## Gates not closed

The arithmetic-square surface intersection/Riemann–Roch comparison, global polarized cohomology, compatibility of all local perfectoid/Tate constructions with one global object, and extension of abelian monodromy to nonabelian arithmetic remain separate problems. A supplies analytic zero information and derived inequalities/counts; it does not produce a unique geometric object from them.

No new Grothendieck scan was retrieved. The prior verified Montpellier catalogue cotes remain bibliographic framework only, with no invented archival theorem locator.

## Checks

All nine new proof texts were checked in full by their author with targeted proof-check entries. Independent review is pending and not claimed. Source inventories record which exact sections were read. The standalone LaTeX command was blocked before document processing because pdflatex.fmt is missing in this environment. Source-label underscores were escaped in both of our modules.

The original module was refined as requested by root: G10 now says F_q-valued maps with supported constants fixed, avoiding an unavailable ring embedding F_q into G(F_q); G12 adds rational finite-Galois descent and projectors for the actual motive decomposition.

## Additional source correction AC-G21

The hidden-coproduct remark in Jacobian.tex identifies Q/Z with a direct limit of rings Z/n using1/n as the ring unit. The actual additive inclusions are not ring maps:1 in Z/2 maps to2 in Z/4, whose square is0. Q/Z also has zero tensor square overZ, so any bilinear multiplication on that additive group is zero. The preceding character/root product remains valid: it uses ring reductions in the inverse system, and the module proves the resulting compatible root formula and equality with the dual product frame. This correction is narrow and does not discard the framed/rooted uniformization merely because the optional Ind-ring explanation fails.

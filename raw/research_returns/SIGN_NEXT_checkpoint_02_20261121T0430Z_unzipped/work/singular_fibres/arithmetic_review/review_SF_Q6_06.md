# Independent review of SF-Q6-06

Reviewer: GPT-6 Astra Pro; reasoning effort not exposed; /root/singular_fibres.
Run: SIGN_NEXT, 2026-11-21. No Lean compilation claimed.

Reviewed full contribution: `SIGN_NEXT/work/critical_lefschetz/diamond_fourier_anchor.tex`.
SHA256: `6258ac6323d211108c38e28208bf9c22851db267fae0751aa583732aa1431887`.

**Outcome: all three statements pass under their stated hypotheses.** The explicit definite-ambient and prescribed-level restrictions are essential and are now stated correctly.

## Independent reconstruction

(a) The commuting finite-group averages are idempotents. Their product complement projects exactly to the intersection of the norm kernels. Character decomposition gives precisely the characters nontrivial on every factor. The denominator-free product preserves a diamond-stable lattice; it asserts no unit value. The scalar eigenfunctional clause is correctly conditional and is not imposed on the vector-valued Poincare map.

(b) For the stated convention R_x f(g)=f(gx), composition is R_x R_y=R_{xy}. The source period covariance therefore gives the inverse diamond on the translated row in the exact order shown. A level character can be used only after proving b^{-1} iota(delta) b belongs to that level. The local diamond nonmembership proof uses the nonzero decoration functional and its additive identification with the residue field, so multiplication by a-1 cannot annihilate its image unless a=1. This does not prove global coset separation, a distinction the contribution retains.

(c) Under compact archimedean G, the diagonal rational group meets a compact finite-adelic set in finitely many points. Global freeness and normalization of U imply S has no rational point; finite compact separation yields the required smaller compact open K'. The rational stabilizer of its identity class is trivial. The row supported on that class is an actual algebraic modular form with the stated coefficient covariance. Restriction to the identity column class has exactly the support U', so its period is the positive Haar volume times the nonzero coefficient pairing. Every other diamond translate is disjoint from the row support. The coefficient of the identity in the ram projector is the positive product of 1-1/|A_v|, proving the nonzero period.

The proof is valid for the stated definite ambient group. It does not directly apply to the actual m=2 Hida ambient: the exact epsS formula gives signature (8,1), and card_epsS_false confirms the single negative direction. The smaller K' also is not a freely variable parameter of the prescribed K2 datum. These are substantive boundaries, not a normalization change.

## Source check scope

The complete BesselPeriodRightTranslationInvariant proof and the relevant complete dictionary/level definitions were read, as were the full HidaSetting definition and the full DiamondFree proof wrapper. The deeper theorem imported by DiamondFree and every transitive analytic prerequisite were not independently reproved. Source locators checked include FormsTied.rhoT_eq, ColDict.LevelMatch and ColDictDia, IsLocBasis.IsDia, PoincareInHH's actual vector-valued Pu, and HidaSetting.K2set/L_eq/g_eq/eps_eq/e_eq/K2. Exact epsS is in lean_selected/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean169-170; card_epsS_false is in critical_lefschetz/pu_source_cache/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHDef.lean176ff.

No claim follows here of a fixed-level actual m=2 global nonzero composed theta period. That remains a separate task.

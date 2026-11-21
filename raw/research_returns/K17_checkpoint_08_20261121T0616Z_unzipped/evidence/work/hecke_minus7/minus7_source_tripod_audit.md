# Independent source-interface and local-coverage audit

**Verdict: PASS for the new −7 specialization, relative to the named,
previously audited source and global automorphic inputs.**
Auditor: `/root/tripod_integral`, GPT-6 Astra Pro, 21 November 2026.
This note records an independent complete read of
`minus7_source_coverage_section.tex` and `gl2_minus7_section.tex`, with
fresh reads of the exact declarations and local results below. It does not
claim a new unconditional proof of the stipulated source package, nor a
separate execution of the GL2 numerical certificate.

## Actual pinned declarations read

1. `work/lean_candidates/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean`,
   entire `GD`, lines9–22. The even-N, discriminant-coprimality, class-number,
   parity, mod-l kernel, and nondivisibility conditions are all present.
   For E=Q(sqrt(-7)), N2, e16, trivial character, the only substantive
   specialization is the cyclotomic-kernel condition. If E were contained
   in Q(mu_l), it would be unramified at7, contradicting its discriminant.
   The class number is1 by the explicit Minkowski bound below2.
2. `work/hecke_level_one/NumberU3US.lean`, complete file. The actual
   `Adm3U_s` extends `Adm3Alt` and retains `Th.Unl`. The direct
   `OneCharU_s` quantifies over every sigma and specified comparison trace.
   The p>=7 and p not dividing N conditions belong to `NumberU3U_s`, not
   the direct one-character criterion. Thus geometric Frobenius above2 is
   allowed in the direct criterion.
3. `work/hecke_level_one/AutNewformW.lean`, complete file, in particular
   the entire `Adm2A` definition. It retains irreducibility, the attached
   weight2e+1 newform for the cyclotomic twist, `WitAQ`, literal Level,
   determinant condition, and the trivial-plus-rank-two decomposition.
4. `work/hecke_level_one/BlochKatoSelmerVanishes.lean`, definitions
   `KillsMu`66–67, `FrobEig`69–72, `LevelAway`89–91, `LevelAt`102–107,
   and `Level`111–114. KillsMu2 is indeed trivial; KillsMu14 factors
   through Q(mu14)=Q(mu7), so the ramified inertia characters used in
   the rank-two twist are actual global mod7 characters.
5. `work/hecke_level_one/KeepLevel.lean`, complete file, including the
   proof of `levelCore_alt` and the full `levelKA_alt`. Its modulus-one
   conclusion includes fixed vectors at every finite place, including
   the coefficient prime, as well as compatibility away from that prime.
6. The complete files
   `interface/BuildingsResidueChars__LevelTwistCyclotomicPow.lean` and
   `interface/ModularityArgument__AutomorphyLifting__AdmissibleLevelRestriction__UnlAllOf.lean`
   under `work/hecke_coverage/`. The common cyclotomic twist preserves
   the literal level data, and `unlAll_of` supplies the required retained
   above-l hypothesis. The substituted vector is (15,-1,-17), its
   infinitesimal character is (16,0,-16), and the compact highest weight
   is (15,0,-15).

The source-to-model deductions do not compare a replacement TrData multiset
with the source's original one. They cover each actual admitted trace and
then apply the pointwise unit criterion directly.

## Fresh primary local and global locators

The local files are `work/hecke_coverage/adler_lansky_ramified.pdf/.txt`
and `adler_lansky_unramified.pdf/.txt`.

* Ramified paper §4.2.1, printed pp11–12: the full standard lattice
  stabilizer at y has reductive quotient O(2,1)(k), with the central
  component included. The proof's integral hyperbolic-plane construction
  at7 identifies I3 with precisely this lattice model. I reconstructed
  it: choose a^2=-5, v=(1,2,a), choose h(v,w)=1, replace w by
  w-h(w,w)v/2, and use -d=Norm(det B) to normalize the orthogonal line
  to norm−1. Every operation is integral because2 is a7-adic unit.
* Ramified paper §4.4, pp14–15: all three reducibility alternatives
  were read. For an unramified unitary chi and lambda2=1, only the
  irreducible case or the nontrivial unramified quadratic split case
  can occur. The real-power alternatives are excluded by unitarity.
* Ramified Proposition6.1(1),(4), p21: these are the relevant full
  principal-series L-packets. Proposition7.1(i),(iv), p28, gives the
  required base change. Its proof says that the statement and proof
  are identical to the earlier principal-series proposition.
* The earlier paper's Proposition5.1, pp19–20 (published numbering
  Proposition4.1), including its entire proof, was freshly read.
  Cases(i),(iii),(iv) follow directly from Rogawski's Proposition4.10.2
  and the paragraph before Theorem13.2.1. No depth-preservation or
  supercuspidal theorem enters this principal-series application.
  In particular the unrelated q!=7 supercuspidal restriction is not
  imported into the argument.
* KMSW, `kmsw_inner_forms.txt`, Proposition1.5.2(5), pp78–79, freshly
  read with the surrounding local theorem: it supplies the unique
  unramified member at the hyperspecial places. The complete statement
  and proof of Theorem5.0.5, pp205–206, were freshly read, including the
  immediately preceding assertion that its assumptions have been
  established for generic parameters and pure inner twists. Those are
  precisely the retained hypotheses of this source bridge.
* Shin, `shin_compact_2011.txt`, Theorem1.2 and Corollary1.3,
  pp1647–1648, and Corollary7.9 with its proof, p1728, were freshly
  read. There is no extra slightly-regular hypothesis for odd rank3.
  Temperedness at the ramified place therefore applies.

With trivial central character the reciprocal unramified base-change roots
have the form {u,1,u^-1}; the inducing characters are unitary. Iwasawa
decomposition supplies a one-dimensional fixed space in the induction for
the full lattice stabilizer, and exactness of compact-open invariants places
it in one of the members of the required packet. The global multiplicity
argument is the already checked simple-generic pure-inner argument; the
new field introduces no additional local case beyond the one just checked.

## Rank-two twist and integral determinant conclusions

The original rank-two form may have conductor49. Twisting by the inverse
of one global mod7 inertia character reduces the inertia to 1 plus the
ratio. Its determinant is still odd, so this ratio is a nontrivial odd
mod7 character. The resulting conductor is exactly7. This avoids the
invalid inference that both original inertia characters cannot ramify.
The coefficient-prime slope gap32 and full classical local-global
compatibility are retained from the separately audited earlier proof.

At2 a mod7 character takes a third root of unity, since2 has order3 in
(Z/7)^×. Thus all source twists are covered by
det(t^3 I-T2^3), t=1+2^32, on the entire61-dimensional space. The full
modular-form proof was read: the conic relation, the invertible basis
change away2,3,7, the eta cusp divisor, the61 standard monomials, both
character families, and all three cubic twist factors fit this exact
source coverage. I did not repeat the independently executed GL2
computation; archive's integral-conic replay is a separate audit event.

For U3, the local coefficient ring is the inert quadratic DVR rather
than a split scalar field. The completed full-model proof and its exact
unit determinant already establish the required integral lattice and
unit comparison over that DVR. Extending coefficients preserves units.
An integral characteristic polynomial evaluated to a unit makes each
eigenvalue difference a unit, even with multiplicities. The direct
OneCharU_s bound then has valuation sum zero. This reconstruction gives
no extra multiplicity or source-enumeration assumption.

No mathematical correction was requested. Manual equation tags were
separated editorially as S7 for source coverage and U7 for the finite U3
proof; this does not change any argument.

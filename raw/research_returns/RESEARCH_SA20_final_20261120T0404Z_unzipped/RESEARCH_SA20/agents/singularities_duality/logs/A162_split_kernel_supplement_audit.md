# A.162: independent audit of the added split-kernel formulas

Observed audit time: 2026-11-20 02:22:51 UTC.
Auditor: singularities_duality, independently of the author and root.

## Literal source examined

`agents/higher_comparison/part_RP3_equivariant_germs.tex`, SHA256
`8bb5cf20d796892c6c99016ba8ae457c7bb4400c87e5ea81afe494520df81020`.
The full original candidate was independently audited at 02:11:36 UTC in
`logs/RP3_equivariant_germ_independent_audit.md`. This supplement literally
reads the added final argument, equations (A.162.9)--(A.162.11), and the
nearby group-law paragraph. It does not replace that earlier full proof
and original-source audit.

**Verdict: PASS.** No mathematical correction requested.

## Checks

1. Re-read the actual A.132 definition of the parameterized germ simplicial
   group and equations (A.132.11)--(A.132.13) in
   `parts/parametric_concordance.tex`. The ordinary germ group used in
   A.162 is the same joint-family model: representatives and equality
   are on neighborhoods of the entire compact parameter zero section.
   Its identity-component comparison with the singular complex of the
   global origin-fixing homeomorphism group is exactly (A.132.11).
   The global radial extension immediately after (A.132.12) is the
   ordinary linear action on O(4), so this comparison preserves the
   particular map whose fundamental-group image is being split.

2. Re-read A.132's low-degree calculation. The already audited
   5-connected stabilization to TOP/O and its vanishing in degrees one
   and two imply that pi_1 O(4) -> pi_1 TOP(4) is an isomorphism by the
   fibre exact sequence. Only those two vanishings are needed. No
   finite-rank versus stable-group identification in higher degrees is
   introduced. Under the preceding natural joint-germ bridge this is
   precisely the composite f j in (A.162.9).

3. Both V and W are fundamental groups of simplicial groups and hence
   abelian. If f j is an isomorphism, the displayed map
   v -> v - j((f j)^(-1)f(v)) lands in ker(f), annihilates im(j),
   restricts to the identity on ker(f), and has kernel exactly im(j).
   Thus (A.162.10) is a genuine split direct sum and induces the claimed
   quotient isomorphism. It preserves the group structure already
   checked in (A.162.8), not only an identification of pointed sets.

4. Under K = ker(f), let I be the actual image of the PL component map.
   A.142--A.143 give a surjective homomorphism chi:K -> F_2 which is zero
   on I. Abelianness makes I normal. The induced quotient homomorphism
   has kernel exactly ker(chi)/I; this proves (A.162.11).

5. The concluding limitations are exact. This argument computes neither
   K nor I nor ker(chi)/I, proves no equality I = ker(chi), and gives no
   injectivity statement for the original PL-to-TOP component map.
   It is structural progress and is not counted here as closure or
   narrowing of the unresolved kernel or zero-CS sufficiency gate.

## Source provenance

This supplement freshly reads the actual previously checked A.132 text.
It does not claim a new opening or visual inspection of the FQ, KS, or
GGHKP originals during this short interval; those exact source checks
are recorded in the A.132 source and root audits. The initial A.162
audit separately records the freshly opened EK, Cerf, Bamler--Kleiner,
and Boyle--Chen--Conway originals.

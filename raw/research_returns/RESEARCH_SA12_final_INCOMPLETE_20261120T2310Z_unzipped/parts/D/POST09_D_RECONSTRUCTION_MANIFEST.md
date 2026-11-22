# Part D: post-checkpoint-09 reconstruction manifest

Date: 20 November 2026. Root owns the central assembly, result ledger
and central check-event ledger; D has not edited them.

## Complete original-boundary linear cohomology

File: parts/D/D_tame_surface_linear_cohomology.tex.
This is a complete mathematical reconstruction of the four-part proof
audited before the environment replacement, not a claimed recovery
of the lost bytes.

The proof units are:

- D:tame-boundary-summed-index: uniform relative-Frobenius determinant
  and inverse; one-filtration sum of grade indices; fixed
  normalization-rank multiplier.
- D:tame-canonical-Euler: normalized character lattices, character-cycle
  upper slopes, and the total positive Euler correction at bad points.
- D:tame-canonical-linear-cohomology: exact Riemann–Roch sign,
  fixed-ideal Frobenius sandwich, and coherent cohomology.
- D:tame-surface-all-characteristics-H1: Artin–Schreier, restricted
  Leray, all coefficient characteristics, open subgroups, and the
  maximal prosolvable quotient.

The final theorem preserves the audited identifiers
D:surface-original-boundary-p-H1 and
D:surface-original-boundary-prosolvable as aliases.

Root read the complete actual reconstructed file and passed it at
approximately 09:24 UTC; the incoming audit specifies 21,438 bytes.
C's fresh actual-file audit was requested separately. Earlier complete
transcription and primary-source passes are historical events and are
not represented as fresh file reads.

Dependencies restored by C:

- D:local-tame-p-linear-H1 in C/D_local_tame_p_H1_post09.tex;
- D:local-p-linear-H1, D:unit-reflexive-linear-cohomology, and
  D:punctured-surface-all-characteristics-H1 in
  C/D_p_H1_surface_post09.tex;
- D:surface-curvewise-conductor;
- the previously included cohomology/crown sufficient criterion.

C owns the Langer, Kimura, Lyubeznik–Smith, Hochster and
Iyengar–Takahashi bibliography entries. D does not duplicate them.

## Fixed-rank parabolic count

Root restored the corrected retained text to
parts/D/D_tame_parabolic_fixed_rank_growth.tex, with labels
D:tame-parabolic-boundedness and
D:tame-parabolic-fixed-rank-growth.

D read the complete actual file at 09:25 UTC and passed it.
The equal-digit order restriction precedes the intrinsic flag
construction. Invalid words are discarded before finite-cycle counting.
The constant depends on fixed rank; quadratic dependence is not asserted.

The unique new D bibliography file is
parts/D/references_parabolic_count_D.bib, with keys Borne2007D and
BorneVistoli2012D. B owns Beke2011FixedRankB. C owns
C_LangerBounded2004, C_LangerAddendum2004, C_Sun2008 and
C_MehtaPauly2007.

Exact root-stack primary locators:

- Borne, arXiv math/0604458v1: Proposition 3 and homogeneous-basis
  proof, printed pages 11–12; Theorem 4, printed page 12; complete
  equivalence and tensor proof through printed page 16.
- Borne–Vistoli, arXiv 1001.0466v2: Theorem 6.1 and complete graded
  reconstruction, descent and tensor proof, printed pages 33–36.

Root and C independently reopened these exact primary proofs before
promotion. The bibliography distinguishes printed pages from PDF indices.

## Bounded-conductor product obstruction

File: parts/D/D_bounded_ramification_obstruction.tex.
Label: D:bounded-ramification-generation-obstruction.

The result refutes the inference from bounded ramification, smallness
and all-characteristic linear twisted H1 to finite generation.
It is not a counterexample to original-boundary tameness: the actual
geometric covers are wild at one original boundary point.

C restores the geometric input in
parts/C/D_psl2_bounded_conductor_geometry.tex, label
D:psl2-bounded-conductor-covers.

## Exact finite program: new version distinguished from history

The original certificate source was not recovered from checkpoint09.
Its replacement is a separately identified new version.

- Source: parts/D/code/check_psl2_bounded_ramification_v2.py.
- Output: parts/D/output/psl2_bounded_ramification_v2.json.
- Source SHA-256:
  62c690c81ad2025091b8e1956ba7be858af25b49d4ff4ceb4d05d86c4868bb35.
- Author execution: 31,222 exact assertions, all passed.
- Author runtime: 0.12265485200077819 seconds.
- Fields: q = 4, 8, 16.
- Group orders: 60, 504, 4080.
- Nonlogarithmic breaks: 4/3, 8/7, 16/15.

The checks cover exact field arithmetic, three matrix generators,
branch orbits, inertia and lower jumps, invariant identities and
finite pigeonhole inequalities. The general proofs remain in the paper.

Historical runs of the lost original version are retained only as
historical audit data: 306,144 assertions; author runtime
0.6179991249955492 seconds; root independent rerun runtime
0.6380047900020145 seconds. They are not attributed to the new program.

## Four existing uniform ramification statements

parts/D/D_uniform_ramification_bound.tex already existed in the
restored tree. D read it again and confirmed all four final statements:

- D:different-conductor-bound;
- D:surface-uniform-different;
- D:fixed-boundary-uniform-different;
- D:surface-uniform-conductor.

All final precisions are present: positive residue characteristic;
the inverse-sign proof for the positive anti-nef cycle; and generic
quasi-finiteness for the different formula. The Abbes–Saito
Proposition3.15 locator is page8. Root supplies integration rows/events.

## Fresh cross-agent reads by D

At approximately 09:22–09:24 UTC, D read and passed all of:

- C/D_local_tame_p_H1_post09.tex, including invariant Matlis rank r
  rather than nr;
- B/post09_reconstruction/D_uniform_local_representation_growth_B.tex,
  including relative jets, exact Artin realization, semilinear
  witnesses, complete-local Lang and class-fibre openness.

These are fresh actual-file reads. The ADS, Dao–Takahashi and
big-test-element primary reads remain separately dated historical checks.

D also freshly reopened Iyengar–Takahashi's primary jac3.pdf after
reconstruction: section2, Noether-different factorization, printed
pages2–3; section3, formula(3.1) and Examples3.2–3.3, printed pages6–7.
The Jacobian is the sum of Kähler differents, each contained in its
Noether different. For an MCM module free over the regular normalization,
the factorization is through a free module. This verifies the uniform
ordinary-Frobenius-defect input for the fixed Kummer Jacobian ideal.

## Remaining status

Full D.1, D.2(ii), and dependent L8 remain open in the residual generality.
The original-boundary surface result controls all abelian crowns.
The fixed-rank theorem counts representations at each fixed rank.
Neither settles arbitrary nonabelian monolithic crown multiplicities.

The two-sided saturated boundary grade lemma has passed fresh root/C
actual-file audits and is marked Proved. The complete O(fr²) bounded-degree
flag/Frobenius presentation is now in D_tame_quadratic_count_candidate.tex.
Root, B, and C have passed the full mathematical proof; D and B have read
the exact primary Eisenbud–Goto regularity/linear-resolution proof.
The decreasing flag convention and the fixed exceptional pole-window
clarifications are saved. Root authorized promotion after its fresh complete primary read. All three headings are now Proved; central integration is owned by root.

## Fresh auxiliary audits at 09:43–09:45 UTC

D passed the complete B rational-chain example and proper-curve arithmetic-defect lemma.
Fresh primary reads: Stacks031S,02NS,0BWB,00R4,0BVH.
The byte-identical rational-chain certificate was independently reexecuted:2,340 exact assertions passed in0.06932535399937478s, SHA256e61af1895be044509c3817164da5d5b55f48c55d7a772d834d3e96af358989e9.
Output: parts/D/output/fixed_different_rational_chains_D_audit.json.

D freshly reopened Eisenbud–Goto through the successful search reference and read
section0 printedp94, Proposition1.1 p95, and Theorem1.2 with full proof pp96–97.
The direct mirror URL itself returned403; search-reference reopening returned the actual primary text.
No page-image visual inspection is claimed.

## Quadratic original-boundary promotion

At09:47 UTC root authorized promotion of all three units in
D_tame_quadratic_count_candidate.tex after root/B/C full actual-file
mathematical checks and root/B/D exact Eisenbud–Goto primary reads.
The source scope is section0 p94, Proposition1.1 p95, and Theorem1.2
with its complete proof pp96–97. Root fresh source ref:turn490924656view0.
The two requested precision sentences are present. All three headings
are Proved. The theorem counts defining-characteristic representations
by p^{C f r^2}; it does not settle full finite generation.
Included D sources are frozen through checkpoint13 at root request.

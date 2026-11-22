#!/usr/bin/env python3
"""Record scheduled review eight; refuse execution before its due time."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,19,21,4,tzinfo=timezone.utc)
if now<due:
    raise SystemExit('Eighth scheduled review is not due yet')
path=root/'logs/progress_review_08.json'
if path.exists():
    raise SystemExit('Eighth review already recorded')
previous=json.loads((root/'logs/progress_review_07.json').read_text())
assert previous['review']==7 and previous['consecutive_without_movement']==0
for name in ['A135_root_integration.json','A136_root_integration.json',
             'A137_root_integration.json','A139_A140_root_integration.json']:
    assert (root/'logs'/name).exists(),name
audits=[
    'notes/root_A135_base_four_comparison_audit.md',
    'notes/root_A136_stabilization_model_audit.md',
    'notes/root_A137_component_image_audit.md',
    'notes/root_A140_obstruction_realization_audit.md',
    'agents/higher_comparison/A137_independent_audit.md',
    'agents/higher_comparison/A140_independent_audit.md',
]
for name in audits:
    assert (root/name).exists(),name
record={
    'review':8,'scheduled_utc':'2026-11-19T21:04:00Z',
    'display_time':'19 November 2026, 22:04 Europe/Berlin',
    'baseline_review':7,'movement':True,'consecutive_without_movement':0,
    'main_A1_gate_changed':True,'task_status_changes':[],
    'qualifying_movement':[
        'A.135–A.136 compute the entire both-end-fixed comparison fibre for every closed real PL4 base and specify the actual extension map for the ordinary free-top comparison: F_P is hofib(beta_B:F_A→Map(B,K(Z/2,2))). This solves the relative5D cylinder part and reduces the remaining based comparison to the ordinary4D base-automorphism comparison and its specified stabilization; the extension map is no longer an unknown.',
        'A.137 gives a complete criterion for the separate ordinary component image: endpoint isotopic to PL, then vanishing of its relative cylinder class modulo J_B=im(pi0beta_B). The unknown quotient on the endpoint-image subgroup embeds in the finite elementary abelian2 group H2(B;Z/2)/J_B. A.140 evaluates that quotient under exact assembly/Bockstein hypotheses and evaluates J_B entirely for every simply connected closedPL4 base. This replaces an unrestricted component-cokernel gate by the proved endpoint and finite-cohomology obstruction criterion.'
    ],
    'proof_audit':audits,
    'not_counted':[
        'A.139 is a full sphere stabilization formula, but is not separately used to count progress on the remaining arbitrary-base gate.',
        'The A.140 automorphism pi1 counterexample is not conflated with a concordance pi1 theorem.',
        'A.138 fixed-format local contractions and the infinitesimal approximation obstruction leave the relative higher definable comparison gate unchanged.',
        'A5.016 proves one real-definable cell-like surface approximation theorem, not a uniform parameter theorem or the maximal bundle-locus theorem.',
        'The support-localized ordinary-loop candidate is not yet promoted at the preparation of this review and is not needed for this movement decision.',
        'Unsuccessful original-source searches, formatting, visual QA, verification programs and checkpoint work do not independently count as movement.'
    ],
    'remaining_original_gates':[
        'Higher PL-to-SA and arbitrary fixed o-minimal concordance comparison; relative two-parameter straightening remains',
        'General real base3 comparison and the remaining base4 ordinary automorphism/stabilization/endpoint evaluation',
        'Maximal bundle-locus definability for proper definable maps with target dimension at least3 and fibre dimension at least2',
        'Exact original Hartshorne1968 Proposition4.3/Theorem7.5 and Ogus1973 Section3 source comparison'
    ],
    'next_review_utc':'2026-11-19T22:04:00Z','stop_authorized':False,
    'actual_recorded_utc':now.isoformat(),
}
entry='''
## Formal progress review08 — 19 November 2026, 22:04 Europe/Berlin (21:04 UTC)

Baseline: review07 at 21:04 Europe/Berlin. **Movement: YES. Consecutive reviews without movement: 0.** No original parent task row is marked complete. The qualifying change is a proved reduction of the main four-dimensional comparison gate; method results and packaging are excluded.

**A solved relative cylinder and a specified extension map.** At review07 the general real comparison remained in base dimensions three and four. A.135 now computes the whole both-end-fixed comparison fibre for every closed real PL four-manifold B as Map(B,K(Z/2,1)). A.136 constructs the actual stabilization map beta_B:F_A→Map(B,K(Z/2,2)) and proves that the ordinary free-top comparison fibre is its based homotopy fibre. The construction uses looped product with a line on sliced PL structures and the opened relative open-five-dimensional classification. Thus the five-dimensional relative cylinder problem and the previously unspecified extension map are solved. What remains in this branch is the ordinary four-dimensional base-automorphism comparison and the evaluation of that specified map. This is a dimension-lowering calculation with an explicit solved fibre, not a new name for the old concordance space.

**The separate component-image problem has an exact finite obstruction.** A.137 proves that a TOP concordance component has a PL representative exactly when its endpoint is TOP-isotopic to PL and its normalized relative cylinder class vanishes modulo J_B=im(pi0 beta_B). The homomorphism on the endpoint-image subgroup I_B has kernel precisely the PL concordance image. Consequently its quotient is a subgroup of H²(B;Z/2)/J_B and is finite elementary abelian2. The proof controls all endpoint-path choices and actual ordinary component invariance. A.140 identifies the exact OPR obstruction with this class, realizes the Bockstein kernel under the stated quadratic assembly hypothesis, and proves surjectivity onto the quotient when H1(B;Z_(2)) has no two-torsion. For every simply connected B it evaluates J_B as all H² and the TOP component group as trivial. General endpoint recognition and J_B evaluation remain explicit gates.

**Results retained without separate movement credit.** A.139 gives the entire sphere TOP model as the fibre of actual finite-rank stabilization, with four-sphere vanishing only through degree three. This special-base result is not independently counted. The ordinary automorphism-loop obstruction of A.140 is likewise not substituted for a concordance-loop theorem. A.138 proves fixed-format local contractions and a precise non-Archimedean approximation obstruction, while the changing-format contraction problem remains. A5.016 establishes finite prescribed-height collars and coherent approximation for one cell-like map between closed real surfaces, but not continuous dependence on additional parameters. Its parameter-fold counterexample addresses an invalid method extension, not the original maximal-locus question. None of these method or special-model statements resets the stopping count independently.

### Every remaining original scope and its current gate

| Scope | Current proved boundary and smallest unresolved case | Attempts and next attack |
|---|---|---|
| A.1(b), higher definable comparison | Complete effective PL/SA models and recursive homotopy presentations are available; components agree with every fixed o-minimal expansion. In base dimensions at least five the map is injective in all degrees and an isomorphism on components and pi1. Real pi2 surjectivity, already for T6, remains. | Exact scalar straightening does not preserve two parameters. A.138 contracts each fixed formula format locally, but approximation can enlarge the format and shrink the available radius. Continue an actual relative family theorem or construct a class in the TOP-forgetful kernel. |
| A.1(b), real comparison | Full comparison is proved in base dimensions at most two and at least five; the three-sphere has a full TOP model and a pi2 discrepancy. In base four, the full based comparison is now the fibre of beta_B on the ordinary base-automorphism comparison. The component image has the exact endpoint plus H²/J_B criterion. | General base three still involves a four-dimensional cylinder. In base four evaluate F_A, beta_B and the endpoint predicate beyond the established hypotheses. Ordinary-loop localization in a simply connected codimension-zero submanifold is being audited as a possible further evaluation of J_B. |
| A.5, maximal proper-map bundle locus | Definable for triangulable maps, finite and graph fibres, and target dimension at most two. The remaining target dimension is at least three and fibre dimension at least two. | The smooth product example excludes ambient Thom stratification as a necessary criterion. One real surface cell-like map now has coherent definable approximations, but the required extra-parameter continuity and arbitrary-field extension remain unproved. Attack the special positive-height-product family rather than extrapolating from individual collars. |
| C.2(b), original-source comparison | The duality chain and componentwise Cohen–Macaulay repair are proved. Exact SGA2/Hartshorne1970–1971/Speiser comparisons are opened. | Hartshorne1968 Proposition4.3/Theorem7.5 and Ogus1973 Section3 remain uninspected in original pages. Metadata, later citations and the author's newer work do not replace them. Pursue a genuinely new advertised original-copy route if found; no communication or access bypass is authorized or attempted. |
| All other completed qualified scopes | The current70-row outcome table retains the precise hypotheses and verified counterexamples. | No broader noncompact, undefined-manuscript or family claim is inferred from those qualified conclusions. |

This review does not authorize a final return. The next review is due at 23:04 Europe/Berlin (22:04 UTC). The no-movement count is zero.

### Full current task and lead table

'''
path.write_text(json.dumps(record,indent=2)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write(entry+(root/'notes/outcome_table.md').read_text())
print(json.dumps(record,indent=2))

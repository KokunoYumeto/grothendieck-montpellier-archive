"""Interim research-state integration; preserves earlier check events and ledger."""
from pathlib import Path
import csv, hashlib
from datetime import datetime
from zoneinfo import ZoneInfo

root = Path(__file__).resolve().parent
now = datetime.now(ZoneInfo('Europe/Berlin'))
stamp = now.strftime('%Y-%m-%d %H:%M CET')
with (root/'QUESTIONS.tsv').open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
by_id = {r['id']: r for r in rows}

def update(qid, **kw):
    if qid not in by_id:
        row = dict.fromkeys(fields, '')
        row['id'] = qid
        rows.append(row)
        by_id[qid] = row
    by_id[qid].update(kw)

update('Q3', finding_ids='F01,F02,F03,F04,F17,F24',
       current_gate='F24 removes input single parity: real signed visible Euler spectra suffice at even lengths. Output negative spectrum, pointwise/error bounds, visibility under chosen extensions, and visible duality remain.',
       approaches_tried='Iterated Parseval; spectral poles; positive and signed even tensor powers; sublinear errors; powered-root visibility; separate dual system')
update('Q3-GCT', finding_ids='F03,F04,F17,F19,F20,F21,F22,F24,F25',
       current_gate='For classical coefficients pure Tate Satake projector images exist. For actual rank three the coherent algebra and right tensor action exist. The remaining transfer must retain designated bases, path signs, normalized traces, and specialization.',
       approaches_tried='Direct specialization; inherited KL cone; orbit schemes; Satake and motivic Schur projectors; coherent rank-three center/tensor lattice; signed Euler criterion',
       next_step='Attack normalized projector trace realization and actual derived/categorical operations; determine which extra data survive the coefficient realization.')
update('Q5-SAT', state='PROVED_OBSTRUCTION_WITH_EXACT_SCOPE', finding_ids='F18',
       source_and_locator='GCT IV §18.3 eq172 p128; VI Definition1.2.4 p14; F18',
       current_gate='Homogeneous integral difference constraints force ordinary support saturation. The rectangular parity ray refutes that model; rational half-point models and VI residuewise strict saturation remain possible.',
       next_step='Retain congruences or rational lattices in an actual theta/GCT comparison; do not equate the support obstruction with a VI-index counterexample.')
update('Q6', state='DICTIONARY_INTEGRATION_ACTIVE_FOR_NEW_FINDINGS', finding_ids='F01–F25',
       current_gate='Original archive audit is complete for the selected leaves. New coherent, motivic, signed-spectrum and projector findings need their final finding-by-finding transfer-table integration.',
       next_step='Complete the revised Part III dictionary and final text check.')
update('Q6-ARCHIVE', state='SELECTED_SOURCE_AUDIT_COMPLETE',
       current_gate='Cote1 eight selected leaves inspected under both numbering conventions. Generic Fredholm formulas are present; no Xi identity or RH-equivalent positive operator verified. Other cote corrections retained.',
       next_step='Integrate exact scan/folio/PDF map; do not promote visible formulas into a checked manuscript proof.')
update('QNEW-SATAKE', source_and_locator='Richarz published Thms3.1,5.1/Prop4.1/Lem5.4; MV Thm7.3; Richarz–Scholbach Thm4.1/Prop4.8,5.9/Cor6.4/Lem6.5',
       state='PROVED_CLASSICAL_PURE_TATE_REALIZATION', finding_ids='F20,F23',
       current_gate='Actual primitive Schur projector images have Tate coefficient motives with scalar Frobenius q^h. Rank labels and compatibility with designated nonstandard operations remain; signed permutation action can fail already in GL2 d3.',
       approaches_tried='Finite-field natural IC normalization; proper convolution; primitive Young projectors; canonical Hom weight; motivic Satake; explicit GL2 fibers',
       next_step='Find action-compatible effective labels for the projector images, beyond the refuted universal signed-permutation ansatz.')
update('QNEW-H3', source_and_locator='GCT IV §6.1 p33; Def11.1/eq93; Prop11.14/eq110; Thm11.16/eq111–112; §12.3',
       state='PROVED_COHERENT_ALGEBRA_AND_ACTUAL_RIGHT_TENSOR_MODEL', finding_ids='F19,F21,F25',
       current_gate='A=R²×M2(C), second-order branch collision; actual tensor lattice and commutant map computed. Remaining comparison is the canonical based left/right structure and finite-field realization with the required grading.',
       approaches_tried='Complete presentation; explicit idempotent/CRT model; exact B3/B4/Sa matrices; coherent branch modules; Hom/Ext computations',
       next_step='Study normalized word traces and derived projector relations while retaining the actual action.')

update('Q3-SIGNED', source_and_locator='Alpöge p3 footnote3; F24',
       question='Can the input middle-parity hypothesis be replaced by signed Euler traces?',
       state='PROVED_WITH_VISIBLE_SPECTRUM_AND_EVEN_LENGTHS', finding_ids='F24',
       current_gate='Largest-radius signed products have a surviving positive coefficient at even k. Hidden Euler roots remain invisible. Arbitrary finite extensions require retained top-radius visibility.',
       approaches_tried='Real group-algebra augmentation; Vandermonde nonnilpotence; spectral-radius estimate; exact extension and complex-phase countermodels',
       next_step='Supply the negative path-output spectrum and visible duality for a designated nonstandard object.')
update('Q3-COLLISION', source_and_locator='F22/F25; Stacks tags04DZ,03SI,0A4E',
       question='Can ordinary constant nearby-cycle purity retain the actual collision order?',
       state='REFUTED_FOR_SPECIFIED_CONSTANT_COEFFICIENT_FAMILY', finding_ids='F22,F25',
       current_gate='All Cm have equivalent ordinary étale data and the same constant nearby/vanishing cycles, while conductor length and crossed coherent Ext record m.',
       approaches_tried='Finite universal homeomorphism; exact conductor quotient; strict-local two-point nearby cycle; periodic free resolution',
       next_step='A realization retaining coherent deformation must add a prescribed action/coefficient object beyond these constant traces.')
update('Q5-PROJECTOR', source_and_locator='F23; ordinary finite-group induction/Pieri; GL2 Satake example',
       question='What extra data make Schur projectors into an explicit positive counting rule?',
       state='PROVED_SUFFICIENT_RULE; GENERAL_EXISTENCE_REFUTED_FOR_SIGNED_BASIS_ANSATZ', finding_ids='F23',
       current_gate='Specified signed orbits with Young stabilizers yield Pieri chains; polynomial encodings are separate. The standard S3 multiplicity has no signed basis.',
       approaches_tried='Orbit induction; primitive-idempotent rank; mixed Pieri; exact group-order obstruction; pure two-line fiber',
       next_step='Test the criterion on actual rectangular tensor-square modules, allowing more general stabilizers or a different positive structure.')
update('Q3-NORMALIZATION', source_and_locator='Actual F21 tensor module; proposed F26',
       question='Can normalized nonstandard word traces under v=q^(n/2) be finite Weil traces?',
       state='ACTIVE_PROOF_AND_REVIEW', finding_ids='proposed F26',
       current_gate='Tr(e1e2)=24+16/D² suggests infinitely many generating-series poles, in contrast to Laurent unnormalized traces.',
       approaches_tried='Actual two-dimensional block traces; expansion at infinity; finite Frobenius recurrence test',
       next_step='Complete and independently check the exact recurrence obstruction and its scope.')
update('Q3-DERIVED', source_and_locator='F09 actual rank-one element; proposed F27',
       question='Do bounded derived lifts remove the fixed-cone sign obstruction while retaining operations?',
       state='ACTIVE_PROOF_AND_REVIEW', finding_ids='proposed F27',
       current_gate='K0 lifts exist, but one-parity ambient lifts of powers are excluded by mixed KL coefficients. Character-point localization may restore the actual rank-one scalar action in a different cone.',
       approaches_tried='Derived Euler parity; tensor amplitude under explicit exactness hypotheses; four-point character model',
       next_step='Check full statements and distinguish K0 polynomial identities from functorial tensor relations.')
update('Q4-RECT-YOUNG', source_and_locator='Manivel Thm1 arXiv0809.3710; proposed F28',
       question='Can Young-stabilizer signed orbits model the actual height-two rectangular tensor square?',
       state='ACTIVE_PROOF_AND_REVIEW', finding_ids='proposed F28',
       current_gate='Known same-parity constituent rule gives a rational point model; hook-support intervals may obstruct all signed Young-orbit decompositions.',
       approaches_tried='Primary multiplicity-free theorem; hook exterior-power restriction; effective induced-character comparison',
       next_step='Finish full proof and independent review including d=2 and singleton blocks.')

with (root/'QUESTIONS.tsv').open('w', newline='') as f:
    w=csv.DictWriter(f, fields, delimiter='\t'); w.writeheader(); w.writerows(rows)

with (root/'CHECK_EVENTS.tsv').open(newline='') as f:
    reader=csv.DictReader(f, delimiter='\t'); cf=reader.fieldnames; events=list(reader)

def event(sid, who, kind, outcome, record):
    row=dict(zip(cf,[sid,now.strftime('%Y-%m-%d'),who,'GPT-6 Astra Pro','not exposed',
                    'GCT_NSRH_20261121',kind,outcome,record]))
    if row not in events: events.append(row)

event('F18','/root/gct_statements','targeted proof check',
      'Read complete generated proof; ordinary support saturation scope and VI residuewise strict-saturation terminology passed.','REVIEW_THETA_SATURATION_GCT.md')
event('F19','/root/rectangular_and_theta','targeted proof check',
      'Read entire actual rank-three algebra proof, CRT/matrix model, specialization and coherent scope; passed.','REVIEW_R3_THETA.md')
for sid in ['F21','F22','F25']:
    event(sid,'/root/rectangular_and_theta','targeted proof check',
          'Read complete generated finding and proof, confirmed byte-for-byte main-paper inclusion. Fragment SHA256 0f7f028df041b91e0fa7e0a00eec10412e4b63795b386c94971574353d2a6f1b; passed.','REVIEW_R3_TENSOR_THETA.md')
event('F21-MATRICES','/root/gct_statements','computation or formal certificate',
      'Exact symbolic rational-function matrix identities B3/B4/Sa and determinant checks passed in Python3.12.14/SymPy1.14.0. This is a computational certificate, not proof-assistant formalization.','verify_rank3_matrices.py; verify_rank3_matrices_output.txt')
event('F20','/root/grothendieck_dictionary','targeted proof check',
      'Full F20 original proof passed, with natural Weil normalization and BBD second-proof precision edits requested and incorporated; motivic strengthening independently proved and checked in report.','agent_satake_purity.md; agent_grothendieck_check_events.tsv')
event('F23','/root/grothendieck_dictionary','targeted proof check',
      'Read all SPG1–SPG8 report proofs, including signed orbit/Young-Pieri rule, GL2 d3 geometry and known binary family; passed. Generated fragment match remains separately recorded.','agent_satake_projector_gate.md')
event('F24','/root/gct_statements','independent re-proof',
      'Independently reconstructed entire real-coefficient top-radius proof, error estimate, powered visibility repair, dual scope and both countermodels; passed at report level.','agent_signed_even_tensor_audit.md')
event('F24','/root/grothendieck_dictionary','targeted proof check',
      'Read full signed-spectrum audit and countermodels; passed. Suggested excluding k=2 from complex countermodel to avoid duplicate-set notation; generated text now uses k≥6.','agent_signed_even_tensor_audit.md')
event('F24-DRAFT-EXTENSION','/root/gct_statements','refuted, with the refined statement\'s id',
      'Unrestricted finite-extension version is false: t_n=0 for even n and2 for odd n has roots ±q but all required even-degree counts vanish. Refined F24 requires retained top-radius visibility.','agent_signed_even_tensor_audit.md §5–6')
event('F24-DRAFT-COMPLEX','/root/gct_statements','refuted, with the refined statement\'s id',
      'Deleting real coefficients is false for t_n=i and k≡2 mod4; exact split-bilinear count supplies the opposite-sign/error identity. Refined F24 retains real coefficients.','agent_signed_even_tensor_audit.md §7')
for sid, record in [('SRC-MANIVEL','arXiv0809.3710 Theorem1 p1'),
                    ('SRC-RS','arXiv1909.08322v3 Theorem4.1; Proposition4.8; Definition6.2; Lemma6.3; Corollary6.4; Lemma6.5'),
                    ('SRC-STACKS-04DZ','Stacks Theorem59.45.2 tag04DZ'),
                    ('SRC-STACKS-0A4E','Stacks Lemma59.91.9 tag0A4E')]:
    event(sid,'/root','used and rechecked in this run','Opened and read the primary statement and relevant displayed context; used with the cited scope, not independently re-proved general machinery.',record)

with (root/'CHECK_EVENTS.tsv').open('w', newline='') as f:
    w=csv.DictWriter(f,cf,delimiter='\t'); w.writeheader(); w.writerows(events)

ledger=root/'LEDGER.md'
text=ledger.read_text()
marker='## Signed traces and actual geometric action — interim gate update'
if marker not in text:
    text += f'''\n\n{marker}\n\nRecorded {stamp}. This is not a scheduled progress review.\n\n- **Q3 strictly reduced:** F24 replaces the input common-parity hypothesis by real signed visible Euler coefficients at even path lengths. The complete proof was independently reconstructed. An overstrong extension variant was refuted and repaired with powered-top-spectrum visibility; the failed proposal remains in the check log.\n- **Q3 actual action gate reduced:** F21 identifies the actual 64-dimensional right tensor lattice over a finite localization with the coherent center model; explicit regular matrices are independently checked and saved as an exact symbolic certificate. This closes the earlier missing-right-action issue for this example.\n- **Q3 deformation comparison narrowed:** F22 proves constant nearby/vanishing-cycle data do not distinguish any positive collision order. F25 computes the coherent Ext invariant that does distinguish it, and the precise 128-dimensional commutant base-change defect. These facts delimit a specific realization, not all possible enriched realizations.\n- **Classical coefficient realization strengthened:** F20 now has a motivic Tate refinement. Its Schur multiplicity coefficient motive is a direct sum of a single Tate twist, so natural Frobenius is scalar. The remaining projector-rank/basis/operation gate is explicit.\n- **Positive-rule gate narrowed:** F23 gives a signed-orbit/Young-stabilizer sufficient rule and a pure Tate GL2 example where no signed basis exists. The actual rectangular Young-orbit test is now under proof.\n- **Archive row completed:** Eight cote1 leaves were inspected under both scan and folio conventions; generic Fredholm formulas are verified as visible content, while the claimed Xi identification is not verified.\n\nActive main approaches: normalized word traces and finite Frobenius recurrence (F26 proposal); actual derived lifts and character cones (F27 proposal); rectangular projector structure (F28 proposal); the actual nonstandard Temperley–Lieb branching tower. The first scheduled review remains due at approximately03:00 CET. No no-movement review has occurred or been counted.\n'''
    ledger.write_text(text)
(root/'STATUS_TIME.txt').write_text(now.isoformat()+'\n')
print(f'Updated {len(rows)} question rows and {len(events)} check events at {stamp}.')

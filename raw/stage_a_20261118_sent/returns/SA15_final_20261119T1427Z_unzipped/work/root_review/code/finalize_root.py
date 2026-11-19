"""Final manually specified attribution and cross-review amendments.

Idempotent, unlike the earlier sequential curation amendments. No source reading
or mathematical judgment is inferred by matching keywords.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, csv
from copy import deepcopy
O = Path(__file__).resolve().parents[1]
cp = O / 'claims_c7.json'
c7 = json.loads(cp.read_text())
for c in c7:
    c.setdefault('origin', 'manuscript')
    if c['id']=='P78-C005':c['statement']=c['statement'].replace('in C004','in P78-C004')
    if c['id']=='P78-C010':
        c['fate']=c['fate'].replace('from C008','from P78-C008')
        c['present_status']=c['present_status'].replace('from C008','from P78-C008')
cp.write_text(json.dumps(c7, ensure_ascii=False, indent=2) + '\n')
p = O / 'claims_c8.json'
claims = json.loads(p.read_text())
supp = json.loads((O.parent / 'cotes6_7/supplementary_root_claims.json').read_text())
claims = [c for c in claims if c['id'] != 'P78-C071'] + supp
parents={c['id']:c for c in claims}
for new,old,statement,fate in [
 ('P78-C072','P78-C046',
  'Let K/Q_p be finite, C the completion of an algebraic closure, and χ a character of G_K. If two nonzero elements x,y of C satisfy g(x)=χ(g)x and g(y)=χ(g)y for every g in G_K, then y/x lies in K×. A× uniqueness requires the additional choice of a rank-one integral A-lattice and its generators.',
  'The ratio is fixed by G_K, so Tate1967 Theorem1 gives K× ambiguity. Generators of a fixed rank-one A-lattice differ by A×. This precise correction of the manuscript statement was already diagnosed by the earlier notes and is re-proved here; no new discovery is claimed.'),
 ('P78-C073','P78-C047',
  'In the manuscript’s finite Galois extension K/Q_p and Lubin–Tate character setting, let J be an open subgroup of inertia. There is no nonzero x in C satisfying g(x)=χ_π(g)x for all g in J at the structural embedding. This restriction cannot be replaced by every subgroup of inertia.',
  'Divide a hypothetical eigenperiod by the structural-embedding χ_πχ_cyc^−1 period from Tate1967 Theorem3. The quotient would have nonzero cyclotomic weight fixed by an open inertia subgroup. The explicit reduction to Tate1967 Theorem2 in proof_audit_root.md §12 excludes it. The trivial subgroup refutes the unrestricted original quantifier. This is a bounded present-run refinement, not a claim that the source literally stated the corrected quantifier.')]:
    z=deepcopy(parents[old]);z.update(id=new,parent=old,statement=statement,
      his_statement='Parent manuscript question '+old+'; this precise corrected formulation is not attributed to the page.',
      status_on_pages='present-run refinement; the parent literal assertion and its source status remain in '+old,
      computation='Complete written proof in work/root_review/proof_audit_root.md §12; no finite test is substituted for the invariant-field theorem.',
      **{'class':'B'},fate=fate,present_status='As of 2026-11-19: '+fate,
      fate_date={'ingredient_publication':'1967','precise_refinement_recorded':'2026-11-19'},
      refs=['Tate1967'],confidence='high',origin='present-run refinement',search_family='LT',
      refinement_provenance='Earlier-run period diagnostics retained; precise statement and proof scope recorded in this run.')
    claims=[c for c in claims if c['id']!=new]+[z]
for c in claims:
    c.setdefault('origin', 'manuscript')
    if c['id'] in ['P78-C039','P78-C052','P78-C062']:
        if c['confidence'] not in ['high','medium','low']:
            c['confidence_detail'] = c['confidence']
        c['confidence'] = 'medium' if c['id']=='P78-C062' else 'high'
    if c['id'] == 'P78-C035':
        c['fate'] = c['present_status'] = (
            'The exact question is SGA7 IX Remark5.13.1. The prime-to-p '
            'filtration argument is re-proved here. P78-C071 proves the exact '
            'integral assertion for finite K/Q_p and p>2 by a present-run '
            'deduction from Fontaine, Breuil and Raynaud; the rational '
            'crystalline-filtration argument works for every p. Integral p=2 '
            'and arbitrary henselian traits are not certified. Exact searches '
            'did not identify a later paper explicitly settling the full '
            'remark; this is a documentary residual, not a claim of modern '
            'openness. See work/cotes6_7/sga7_pcase_audit.md.')
        c['refs'] = list(dict.fromkeys(c['refs'] + ['Fontaine1994VIII',
            'Breuil2000', 'Raynaud1974']))
    if c['id'] in ['P78-C026', 'P78-C066', 'P78-C067']:
        c['class'] = 'B'
        c['authorship_note'] = ('The exact later printed endpoint is an Artin '
            'exposé in SGA 4. The intellectual relation to Grothendieck and the '
            'draft is retained, but editorial inclusion in SGA does not make '
            'this his own authored publication for the class-A census.')
p.write_text(json.dumps(claims, ensure_ascii=False, indent=2) + '\n')
pp = O / 'problems_c8.json'
problems = json.loads(pp.read_text())
for q in problems:
    if q['id'] == 'P78-P011':
        q['state_of_art'] = ('SGA7 IX5.12–5.13.1 is the exact published '
            'question. P78-C071 supplies a complete present-run deduction '
            'for finite K/Q_p,p>2 integrally, using Fontaine1994VIII, '
            'Breuil2000 Theorem5.3.2/Corollary5.3.4 and Raynaud1974 '
            '§2.1/Proposition2.3.1. The rational argument works every p. '
            'No full arbitrary-trait solution was identified by the exact '
            'search; absence of such identification is not modern openness.')
        q['plausible_today'] = ('The exact integral assertion is proved in '
            'this run for finite K/Q_p,p>2. Extending the integral theorem '
            'to p=2 or broader traits requires checking the exact integral '
            'realization and descent hypotheses, not just rational comparison.')
        q['worth'] = ('Worth completing a precise p=2 or broader-trait '
            'literature-to-proof bridge; do not repeat the finite-K,p>2 '
            'argument already supplied here.')
        q['refs'] = list(dict.fromkeys(q['refs'] + ['Fontaine1994VIII',
            'Breuil2000', 'Raynaud1974']))
pp.write_text(json.dumps(problems, ensure_ascii=False, indent=2) + '\n')

# Independent authorship audit: the complete definition, not just a classical
# cocycle identity, has an exact endpoint in his own published Appendix.
fp = O.parent / 'cotes5_6/claims.json'
fc = json.loads(fp.read_text())
for c in fc:
    if c['id'] == 'P56-C074':
        c['class'] = 'A'
        c['refs'] = list(dict.fromkeys(c['refs'] + ['Grothendieck1968']))
        c['fate'] = c['present_status'] = ('Exact own published counterpart: '
            'Grothendieck1968 Appendix, pp356–357, defines the compatible '
            'infinitesimal n-connections and triple-diagonal cocycle. '
            'BO1978 supplies the later exposition. The whole definition '
            'is class A; classical cocycle background alone does not '
            'establish that this exact formulation was known before him.')
        c['authorship_audit'] = ('Exact published compatible n-connections '
            'and triple-diagonal cocycle definition in Grothendieck1968 '
            'Appendix, pp356–357; class A, not merely standard E. '
            'Independently opened and checked by cotes8_9_4.')
fp.write_text(json.dumps(fc, ensure_ascii=False, indent=2) + '\n')

events = [
    ('P56-C008', 'independent re-proof',
     'Root independently read and checked both containments I_r=S_r in '
     'work/cotes5_6/reviews/independent_proofs.md, including the carry weights '
     'and terminal constant weight c−r. This is a written proof for all '
     'parameters, distinct from the 20 exact finite tests and from Hua’s '
     'reported Lean result for r=0. No proof assistant was executed here.'),
    ('P894-C023', 'independent re-proof',
     'Root independently audited work/cotes8_9_4/proofs.md §1: the division '
     'polynomial scaling, simple residual roots and Hensel lifting, constant '
     'good-curve torsion over the unramified degree-four extension, Weil '
     'pairing, bad minimal discriminant congruence, and tame cubic potential '
     'good reduction. The conclusion concerns the finite potentially-good '
     'inertia character, not the entire raw p-adic inertia representation.'),
    ('P56-C019', 'targeted proof check',
     'Root read the parallel-arrow proof in independent_proofs.md: the '
     'inserter is formed on inverse-image functors, giving the corresponding '
     'lax coequalizer of geometric topoi. The accessibility/Giraud argument '
     'and the unresolved derived direct-image comparison are kept distinct. '
     'The associated universal property is P56-C020.'),
    ('P78-C071', 'independent re-proof',
     'Root independently checked the full written deduction in '
     'work/cotes6_7/sga7_pcase_audit.md. The descent lemma applies D_pst '
     'only to the potentially crystalline W and its subquotients; it does '
     'not assume that arbitrary extensions of crystalline representations '
     'are potentially crystalline. The sum-of-conjugates induction and '
     'Raynaud recovery of the specified saturated lattices are checked. '
     'The inherited period/classification theorems are used with their '
     'stated hypotheses, not independently reproved.'),
    ('P78-C072', 'independent re-proof',
     'Proof audit §12: the ratio of two nonzero eigenperiods is fixed, '
     'hence lies in K× by the separately checked Tate invariant-field '
     'theorem; generators of a fixed A-lattice differ by A×. Earlier-run '
     'normalization diagnosis remains attributed to that run.'),
    ('P78-C073', 'targeted proof check',
     'Proof audit §12: checked the structural-embedding Hodge–Tate period '
     'division and reduction from open inertia to the potentially totally '
     'ramified Z_p-extension theorem. The fixed period/invariant-field '
     'theorems are inherited with exact hypotheses, not reproved here.'),
]
now = datetime.now(timezone.utc).isoformat()
with (O / 'root_cross_events.tsv').open('w') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['statement_id', 'date', 'who', 'type', 'outcome'])
    for sid, typ, outcome in events:
        w.writerow([sid, now, 'GPT-6 Astra Pro; effort not exposed; '
                    'SA15-20261119/root', typ, outcome])

with (O / 'project_leads.tsv').open('w') as f:
    f.write('kind\tfrom\tto\twhat\tevidence\tnote_ids\n')
(O / 'project_lead_audit.md').write_text('''# Context-project endpoint audit

The complete P78 notes were read; a second text search for La Longue Marche,
Dérivateurs, S6, LLM, and named research-run references found no named project
endpoint in this package. Its explicit cross-references are archive cote/scan
references. No claim about a missing external project is manufactured from a
thematic similarity. The project-lead table is therefore intentionally empty.
''')
# Correct the two refutation targets now that their precise refinements have
# distinct statement IDs. Retain the existing dated checks and their outcomes.
ep=O/'check_events_c8.tsv'
rr=list(csv.DictReader(ep.open(),delimiter='\t'))
for e in rr:
    if e['statement_id'] in ['P78-C046','P78-C047'] and e['type'].startswith('refuted'):
        target={'P78-C046':'P78-C072','P78-C047':'P78-C073'}[e['statement_id']]
        e['type']='refuted, with refined statement id '+target
with ep.open('w') as f:
    ww=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');ww.writeheader();ww.writerows(rr)
print(json.dumps({'authorship_classes_corrected': ['P78-C026', 'P78-C066',
    'P78-C067','P56-C074'], 'added_refinements': ['P78-C071','P78-C072','P78-C073'],
    'independent_cross_events': len(events), 'project_leads': 0}))

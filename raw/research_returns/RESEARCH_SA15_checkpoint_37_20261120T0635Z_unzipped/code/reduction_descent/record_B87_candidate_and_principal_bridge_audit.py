"""Retain B87 author provenance and the complete reciprocal principal-bridge audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
stamp = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
candidate = own/'B_p5_tame_full_first_layer_candidate.tex'
code = own/'code/verify_p5_tame_full_first_layer.py'
output = code.with_suffix('.output.json')
run = json.loads(output.read_text())
labels = re.findall(r'\\label\{([^}]+)\}', candidate.read_text())
record = {'status':'COMPLETE_CANDIDATE_AWAITING_INDEPENDENT_AUDITS', 'actual_utc':stamp,
          'source':str(candidate), 'source_sha256':sha(candidate), 'labels':labels,
          'code':str(code), 'code_sha256':sha(code), 'output':str(output),
          'output_sha256':sha(output), 'author_run':run,
          'source_scope':[
              'Fresh retained B60 full lower-break proof, B81 full fixed-coefficient/Cartan proposition, B83/B84/B85 actual point-field/evaluation proofs read.',
              'Fresh original Serre1961 Section3.1 pp126-128 read from local original and web turn788471544view0; its printed Herbrand quotient statement refers to other proofs, not claimed proved there.',
              'Complete Colmez Proposition3.7 norm-polynomial proof pp14-15 reused from fresh author B86 read; actual original and scope record retained at notes/B86_source_read_record.json.'
          ],
          'failure_history':'No failed mathematical execution; exact first executed checker and output retained.',
          'scope':'Only p5/e20 tame-reducible residual sector; full5^8 image remains neither excluded nor realized; other sectors and unrestricted index open.'}
(own/'outputs/B87_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
source_note = {'actual_utc':stamp,'source_records':record['source_scope'],
               'Serre_url':'https://www.numdam.org/item/10.24033/bsmf.1562.pdf',
               'Serre_web_ref':'turn788471544view0','priority':'No novelty or historical-priority claim.'}
(own/'notes/B87_source_read_record.json').write_text(json.dumps(source_note,indent=2)+'\n')

src = work/'agents/monodromy/principal_theta_Cartier_bridge_candidate.tex'
assert sha(src) == '2f37d09805d4b0fff3d5b95f682b926ccb98dd128e7a6318dce61a5fb1405a7e'
audit_labels = re.findall(r'\\label\{([^}]+)\}',src.read_text())
audit_labels = [x for x in audit_labels if not x.startswith('subsec:')]
audit = {'status':'FULL_INDEPENDENT_PROOF_AND_SPECIFIED_ORIGINAL_SOURCE_PASS', 'actual_utc':stamp,
         'source':str(src),'source_sha256':sha(src),'labels':audit_labels,'complete_read':True,
         'proof_checks':[
             'The diagonal B[2] descent subgroup gives an actual theta-group homomorphism tau, identity on B[2] and inverse on the center. The invariant addition tensor intertwines the two weight-minus-one irreducible representations and is nonzero by faithful-flat pullback.',
             'The local-local defect in printed AV8.31 is correctly repaired by the universal perfect-pairing character. Its coefficients span the entire Hopf algebra, hence invariant subspaces are ideals; translation invariance plus counit/antipode forces zero or the full ideal. Tensor products of simple modules of independent group factors are simple over an algebraically closed field, so the resulting AV8.32 argument applies.',
             'For f0, (kerF)^D is connected and its dual Hopf algebra is local; every simple representation is trivial. Pulling the relative trace back along the proper Frobenius torsor makes it a constant surjection between trivial bundles. Its kernel therefore has a trivial-factor filtration; ample vanishing gives global trace surjectivity.',
             'The two diagonal kerF linearizations differ by an actual k-character: global functions after the finite nonreduced base change are O(kerF). Connected Cartier dual has only its identity k-point, so the characters agree. Relative duality trace is natural under all scheme-valued deck transformations, giving canonical descent of kappa.',
             'Descent identifies the invariant section line with F*H0(Mprime)=k theta squared. Nondegenerate tensor plus nonzero trace makes the scalar nonzero; the argument retains relative Frobenius twists and invariant volume lines.',
             'On an odd etale cover, only inverse character pairs reach the trivial target summand. Their nonzero theta-square coefficients give exactly(n-1)/2 nonsingular2x2 blocks; the trivial square has Cartier zero. The fixed-target and auxiliary-cover limitation is stated correctly.'
         ],
         'original_source_read':{'path':str(work/'agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt'),
              'scope':'Retained original AV8.10 and8.14 full proofs pp116-117; complete8.30-8.32 pp124-125 including the printed character defect;9.14 and9.17 full proofs pp133-134.'},
         'other_source_scope':'Previously proved finite-Frobenius duality/local coefficient input reused. No fresh Brion-Kumar opening claimed.',
         'computation_scope':'No mathematical program needed or executed for this five-label proof audit.'}
(own/'outputs/independent_principal_theta_Cartier_bridge_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join((stamp,label,'COMPLETE_CANDIDATE_AUTHOR_CHECK','B87 complete actual-field/coefficient proof and exact certificate; independent audits pending.',str(candidate.relative_to(own))+';outputs/B87_candidate_record.json','No promotion or other-sector claim'))+'\n')
    for label in audit_labels:
        f.write('\t'.join((stamp,label,'FULL_INDEPENDENT_AUDIT_PASS','Entire principal theta/Cartier bridge proof and specified AV originals read; universal-character repair and relative descent independently checked.','outputs/independent_principal_theta_Cartier_bridge_audit.json','No new full-group or prescribed-target assertion'))+'\n')
print(json.dumps({'actual_utc':stamp,'B87_sha256':sha(candidate),'principal_bridge_audit':'PASS','labels':len(audit_labels)},indent=2))

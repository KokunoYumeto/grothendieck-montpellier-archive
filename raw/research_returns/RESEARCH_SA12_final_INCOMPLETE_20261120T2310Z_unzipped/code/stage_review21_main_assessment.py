"""Stage root's no-movement assessment shortly before the actual review21."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert datetime(2026,11,20,23,7,tzinfo=timezone.utc) <= now < datetime(2026,11,20,23,10,tzinfo=timezone.utc)
out = root/'code/output/review21_main_assessment.json'
assert not out.exists()
prior=json.loads((root/'code/output/formal_review20.json').read_text())
integration_path='code/output/integrate_A_chain_coordinate_correction.json'
integration=json.loads((root/integration_path).read_text())
candidate=integration['audited_candidate']
assert hashlib.sha256((root/candidate['path']).read_bytes()).hexdigest()==candidate['sha256']
integrated_path=integration['integrated_path']
assert hashlib.sha256((root/integrated_path).read_bytes()).hexdigest()==integration['integrated_sha256']
candidate_text=(root/candidate['path']).read_text()
integrated_text=(root/integrated_path).read_text()
for replacement in integration['status_comment_replacements']:
    assert integrated_text.count(replacement['new'])==1
    integrated_text=integrated_text.replace(replacement['new'],replacement['old'])
assert integrated_text==candidate_text
audits=[]
for actor, item in integration['audit_records'].items():
    digest=hashlib.sha256((root/item['record']).read_bytes()).hexdigest()
    assert digest==item['record_sha256']
    assert item['candidate_sha256']==candidate['sha256'] and item['verdict']=='PASS'
    audits.append(dict(actor=actor,path=item['record'],sha256=digest))
assert {a['actor'] for a in audits}=={'root','B','C','D'}
assert integration['new_statement_rows']==0 and integration['appended_check_events']==8
assert not integration['requested_status_changes'] and not integration['strict_main_gate_reductions']
freeze=json.loads((root/'code/output/checkpoint30_source_freeze.json').read_text())
for path,digest in freeze['files'].items():
    assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
qa=json.loads((root/'qa/pdf_verified.json').read_text())
assert hashlib.sha256((root/'build/RESEARCH_SA12_paper.pdf').read_bytes()).hexdigest()==qa['sha256']
with (root/'RESEARCH_SA12_results.csv').open() as f:
    rows=list(csv.DictReader(f))
with (root/'CHECK_EVENTS.tsv').open() as f:
    checks=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==487 and len(checks)==1655
report=(root/'RESEARCH_SA12_report.md').read_text()
table=report.split('## Outcome table\n',1)[1].split('\n## ',1)[0]
requested=[line for line in table.splitlines() if line.startswith('| ') and not line.startswith('| Item |')]
assert len(requested)==57
open_rows=[line.split('|')[1].strip() for line in requested if 'Incomplete' in line.split('|')[2]]
assert open_rows==['D.1','D.2(ii)','L8']
verified=json.loads((root/'code/output/checkpoint30_archive_verification.json').read_text())
saved=json.loads((root/'code/output/checkpoint30_saved_receipt.json').read_text())
assert verified['full_crc']==verified['all_manifest_hashes']=='PASS'
assert saved['saved_result']['status']=='succeeded'
scope_paths=[
    'code/output/root_review20_followup_notes_scope.json',
    'code/output/root_postreview20_chain_scope.json',
    'code/output/root_global_full_bridge_scope.json',
    'code/output/root_postcheckpoint30_mixed_and_thick_scope.json',
    'code/output/root_residual_locality_and_cycle_scope.json',
    'code/output/review21_auxiliary_audit_index.json',
    'code/output/D_audit_timestamp_refresh_reconciliation.json',
]
optional=root/'code/output/root_review21_last_research_scope.json'
if optional.exists():
    last=json.loads(optional.read_text())
    assert last['actor']=='root' and not last['movement']
    for item in last['files']:
        assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']
    for item in last['two_end_exact_audit_records']+[last['weighted_SNC_root_audit']]:
        assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']
    scope_paths.append(str(optional.relative_to(root)))
scope_records=[dict(path=p,sha256=hashlib.sha256((root/p).read_bytes()).hexdigest()) for p in scope_paths]
auxiliary=[
    'The earlier fixed-coordinate A-chain error is now repaired by intrinsic maximal-ideal jets and an all-characteristic adapted-coordinate proof. All four exact candidate audits pass; the integrated file differs only in its status comment and two status headings. Eight correction events were added for two existing labels. The full original and every historical audit remain preserved. This correction does not change a requested-outcome status or shrink a strongest main gate.',
    'The specified quantum A-chain and mixed-end models give full-bundle types, actual Artinian rigidity and a first-coarse-end Hom defect independent of the root orders. Their discrete type-list budget fits the intended scale. These local facts do not construct the missing global all-coefficient object atlas; any later pair or central-extension refinements remain separate unpromoted notes.',
    'The corrected relative-full bridge uses actual global scaled-separability and Noether factorizations to compare a geometric bundle with its specified full replacement and retain controlled Frobenius poles. It does not perform arbitrary-coefficient reflexive hulls or solve global core/block compatibility.',
    'Conditional ordinary generation, canonical saturation and minimal-rank residual-locality arguments isolate additional hypotheses. The nonminimal rank-two canonical overorder example gives unbounded cohomology with fixed conductor, but it is not a counterexample for optimized rank-equals-period anchors or for the requested count. Scalar semisimple residual images do not imply arbitrary global invariant flags.',
    'The exact thick-end restriction calculation is quadratic in equal normal thickness even for the trivial full line. The root-bridge and head-generation diagnostics likewise block overly strong shortcuts. None establishes a failure of the desired global weighted or coupled construction.',
    'A separate unpromoted numerical argument transfers the weighted core budget through necessary SNC refinements, retaining the new zero-Z(-1) curves explicitly. It does not bound adjacent coefficient products, identify all residual blocks with two-ended chains, or control the nilpotent overlap layers. Short order syzygies and a uniform actual finite-type atlas remain unresolved. The exact P1 diagnostic also shows that order generation alone does not imply the desired small-generator incidence bound.',
    'Compilation, source and proof checks, visual inspection and archive handling are not movement. CP30 was created at its fixed22:40 slot, verified member by member, saved and delivered. The final certified PDF remains build_pass196 with603 pages.'
]
assessment={
    'assessment_utc':now.isoformat(),
    'assessment_actor':'root',
    'comparison_review':20,
    'all_required_proof_audits_completed':True,
    'audit_completion_scope':'The only integrated mathematical change since review20 is the exact two-label coordinate correction listed below; all four complete correction audits and the status-only integration reversal have been checked. Earlier certified packets retain their recorded audits. Subsequent research notes remain unpromoted and are not represented as four-party certified manuscript results.',
    'verified_files':[
        dict(path=candidate['path'],sha256=candidate['sha256'],audit_records=audits),
        dict(path=integrated_path,sha256=integration['integrated_sha256'],audit_records=[dict(path=integration_path,sha256=hashlib.sha256((root/integration_path).read_bytes()).hexdigest())])
    ],
    'research_scope_records':scope_records,
    'movement':False,
    'strict_main_gate_reductions':[],
    'requested_status_changes':[],
    'requested_open':prior['requested_open'],
    'remaining_strongest_gates':prior['remaining_strongest_gates'],
    'auxiliary_not_movement':auxiliary,
    'report_summary':'No requested-row status changed and no strongest main quantitative gate became strictly smaller. The coordinate correction is complete and certified. Local full-category, order-generation and overlap diagnostics remain auxiliary or unpromoted; the global uniform quantitative object atlas and the other strongest gates remain unresolved.',
    'latest_verified_checkpoint':30,
    'latest_confirmed_saved_checkpoint':30,
    'certified_manuscript':dict(build=qa['build'],pages=qa['pages'],sha256=qa['sha256'],statement_rows=len(rows),check_events=len(checks),requested_rows=len(requested)),
    'decision_basis':'Actual requested-outcome and strongest-gate comparison with review20. Auxiliary results, repaired arguments, audits and deliverable preparation are not counted as movement.'
}
out.write_text(json.dumps(assessment,indent=2)+'\n')
print(json.dumps({'assessment':str(out.relative_to(root)),'utc':now.isoformat(),'movement':False,'requested_open':assessment['requested_open'],'verified_files':len(assessment['verified_files'])}))

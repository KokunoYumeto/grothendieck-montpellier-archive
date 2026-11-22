"""Index two unpromoted four-reader packets without changing central statuses."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json

root=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256((root/p).read_bytes()).hexdigest()
packets=[
    ('parts/C/post29_research/note_two_end_pair_coefficient_gerbe_C.tex',[
        'parts/C/post29_research/audit_two_end_pair_author_C.json',
        'parts/C/post29_research/audit_two_end_pair_root.json',
        'parts/B/post29_research/audit_C_two_end_pair_coefficient_gerbe_B.json',
        'parts/D/post29_research/audit_C_two_end_pair_coefficient_gerbe_D.json']),
    ('parts/D/post29_research/note_weighted_SNC_final_minus_one_D.tex',[
        'parts/D/post29_research/weighted_SNC_source_and_author_scope_D.json',
        'parts/D/post29_research/audit_weighted_SNC_root.json',
        'parts/B/post29_research/audit_D_weighted_SNC_final_minus_one_B.json',
        'parts/C/post29_research/audit_D_weighted_SNC_final_minus_one_C.json'])
]
records=[]
for p,audits in packets:
    digest=sha(p)
    checked=[]
    for ap in audits:
        a=json.loads((root/ap).read_text())
        assert a['path']==p and a['sha256']==digest and a['verdict'].startswith('PASS')
        checked.append(dict(path=ap,sha256=sha(ap),actor=a['actor'],verdict=a['verdict']))
    records.append(dict(path=p,sha256=digest,audit_records=checked,manuscript_status='Unnumbered, unpromoted and unintegrated'))
record=dict(utc=datetime.now(timezone.utc).isoformat(),actor='root',packets=records,
            exact_read_scope='Root has read every listed audit record and each entire stable mathematical file. Each reader retains their own fresh versus reused source scope.',
            timestamp_reconciliation=dict(path='code/output/D_audit_timestamp_refresh_reconciliation.json',sha256=sha('code/output/D_audit_timestamp_refresh_reconciliation.json')),
            central_statement_rows_added=0,central_check_events_added=0,requested_status_changes=[],strict_main_gate_reductions=[],movement=False)
out=root/'code/output/review21_auxiliary_audit_index.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'index':str(out.relative_to(root)),'packets':len(records),'exact_audits':8,'promotions':0,'movement':False}))

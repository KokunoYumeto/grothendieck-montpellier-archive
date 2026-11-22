from pathlib import Path
import csv
import hashlib
import io
import json

root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
path = root / 'notes/category_CHECK_EVENTS.tsv'
before = path.read_bytes()
backup = root / 'notes/category_event_taxonomy_before_20261120.tsv'
if backup.exists():
    raise SystemExit('Refusing to overwrite preserved pre-normalization snapshot')
allowed = {
    'targeted proof check',
    'independent re-proof',
    'computation or formal certificate',
    'used and rechecked in this run',
    'carried as background without fault found',
    "refuted, with the refined statement's id",
}
mapping = {
    'primary-source proof-architecture check': 'used and rechecked in this run',
    'targeted source-scope check': 'used and rechecked in this run',
    'independent proof strengthening': 'targeted proof check',
    'direct manuscript dating-witness inspection': 'used and rechecked in this run',
    'specific correspondence dating-source check': 'used and rechecked in this run',
    'independent alternative-proof source and implication check': 'targeted proof check',
    'primary-source alternative-proof reconstruction': 'independent re-proof',
    'targeted independent proof check': 'targeted proof check',
    'primary archival catalogue and dated-letter lead check': 'used and rechecked in this run',
    'direct manuscript/publication cross-reference dating check': 'used and rechecked in this run',
    'bounded published-correspondence dating check': 'used and rechecked in this run',
    'bounded primary inventory dating-source check': 'used and rechecked in this run',
    'bounded primary Nachbin inventory dating-source check': 'used and rechecked in this run',
}
reader = csv.DictReader(io.StringIO(before.decode()), delimiter='\t')
fields = reader.fieldnames
assert fields == ['statement_id','date','who','type','outcome'], fields
rows = list(reader)
assert all(None not in row for row in rows)
audit = []
for line, row in enumerate(rows, 2):
    old_type = row['type']
    if old_type in allowed:
        continue
    if old_type not in mapping:
        raise ValueError(f'Unreviewed descriptive type: {old_type}')
    new_type = mapping[old_type]
    old_outcome = row['outcome']
    row['type'] = new_type
    row['outcome'] = f'Actual check detail (previous descriptive label: {old_type}). ' + old_outcome
    audit.append({'original_file_line':line,'statement_id':row['statement_id'],'date':row['date'],'who':row['who'],'old_type':old_type,'new_type':new_type,'old_outcome':old_outcome,'new_outcome':row['outcome']})
assert len(audit) == 13, len(audit)
assert all(row['type'] in allowed for row in rows)
stream = io.StringIO()
writer = csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
after = stream.getvalue().encode()
backup.write_bytes(before)
audit_path = root / 'notes/category_event_taxonomy_changes_20261120.tsv'
with audit_path.open('w',newline='') as out:
    writer = csv.DictWriter(out,fieldnames=list(audit[0]),delimiter='\t',lineterminator='\n')
    writer.writeheader()
    writer.writerows(audit)
temporary = path.with_name('category_events_normalized.tmp')
temporary.write_bytes(after)
temporary.replace(path)
print(json.dumps({'event_rows':len(rows),'changed_rows':len(audit),'pre_normalization_sha256':hashlib.sha256(before).hexdigest(),'normalized_sha256':hashlib.sha256(after).hexdigest(),'backup':str(backup),'audit':str(audit_path),'allowed_categories':sorted(allowed),'types_after':sorted(set(row['type'] for row in rows))},indent=2))

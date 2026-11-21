from pathlib import Path
import csv
p=Path('/workspace/scratch/59e0d6e3e1d5/GHOSTS_package')
paths=[p/'CHECK_EVENTS.tsv']+sorted((p/'research').glob('*events.tsv'))+[p/'research/root_effective_checks.tsv',p/'research/root_final_checks.tsv']
valid={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
def normalize(row,source):
    if len(row)==5:row.append('')
    if len(row)!=6:raise ValueError((source,row))
    old=row[3];t=old.lower()
    if old in valid or t.startswith('refuted'):return row
    if any(x in t for x in ['computation','certificate','enumeration','exact-integer execution','execution']):new='computation or formal certificate'
    elif 'background' in t:new='carried as background without fault found'
    elif 're-proof' in t or 'reproof' in t:new='independent re-proof'
    elif 'source' in t and not any(x in t for x in ['proof','derivation']):new='used and rechecked in this run'
    else:new='targeted proof check'
    row[3]=new
    row[5]=(row[5]+'; ' if row[5] else '')+'Original event wording: '+old
    return row
seen=set();out=[]
for path in paths:
    if not path.exists():continue
    with path.open() as f:
        rows=list(csv.reader(f,delimiter='\t'))
    for row in rows[1:]:
        if not row:continue
        row=normalize(row,path.name)
        key=tuple(row)
        if key not in seen:out.append(row);seen.add(key)
with (p/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who_model_effort_run','type','outcome','method_or_locator']);w.writerows(out)
print('Master check events:',len(out),'unique events from',len(paths),'sources')

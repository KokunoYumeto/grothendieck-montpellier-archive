from pathlib import Path
from unittest.mock import patch
import contextlib, io, json, runpy, sys, re
sys.dont_write_bytecode=True
R=Path.cwd()
sys.path.insert(0,str(R/'code'))
import normalize_check_events
old_open=Path.open
suppressed=[]
def ro_open(self, mode='r', *a, **kw):
    if any(x in mode for x in 'wax+'):
        suppressed.append(str(self.relative_to(R)))
        return io.BytesIO() if 'b' in mode else io.StringIO()
    return old_open(self,mode,*a,**kw)
def ro_write(self,*a,**kw):
    suppressed.append(str(self.relative_to(R)))
    return len(a[0]) if a else 0
with patch.object(Path,'open',ro_open), patch.object(Path,'write_text',ro_write), patch.object(normalize_check_events.EventNormalizer,'save',lambda self:None), contextlib.redirect_stdout(io.StringIO()):
    data=runpy.run_path(str(R/'code/build_registers.py'))
now=data['TASKS']
ledger=(R/'PROGRESS_LEDGER.md').read_text()
part=re.split(r'^## Scheduled mathematical review 15[^\n]*\n',ledger,flags=re.M)[1]
part=re.split(r'^## Scheduled mathematical review ',part,flags=re.M)[0]
prior=[]
for line in part.splitlines():
    if re.match(r'^\| (?:[A-F]\.\d+|Lead [A-F]\d+) \|',line):
        vals=[x.strip() for x in line.strip().strip('|').split('|')]
        assert len(vals)==4,(len(vals),line)
        prior.append(tuple(vals))
assert len(now)==len(prior)==41,(len(now),len(prior))
old={x[0]:x for x in prior}
assert set(old)=={x[0] for x in now}
print(json.dumps({'current_rows':len(now),'review15_rows':len(prior),'identical_full_rows':sum(old[x[0]]==x for x in now),'status_changes':[x[0] for x in now if x[1]!=old[x[0]][1]],'statement_range_changes':[x[0] for x in now if x[2]!=old[x[0]][2]],'scope_changes':[x[0] for x in now if x[3]!=old[x[0]][3]],'suppressed_root_writes':suppressed},indent=2))
for row in now:
    p=old[row[0]]
    print(row[0]+' | '+row[1]+' | '+('IDENTICAL' if row==p else 'AUXILIARY APPEND ONLY' if row[1]==p[1] and row[3].startswith(p[3]) else 'CHANGED'))
    if row!=p:
        print('RANGE: '+p[2]+' -> '+row[2])
        common=0
        for a,b in zip(p[3],row[3]):
            if a!=b:break
            common+=1
        print('OLD SCOPE REMAINDER: '+p[3][common:])
        print('NEW SCOPE REMAINDER: '+row[3][common:])

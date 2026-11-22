"""Repair the actual setup SyntaxWarning while preserving its output and original bytes."""
from pathlib import Path
import ast,datetime,difflib,json
w=Path(__file__).resolve().parents[1];p=w/'code/consolidate.py';before=p.read_text()
old='\n'+chr(92)+'path{notes/ROOT_SEARCH_LOG_35.md}\n'
new='\n'+chr(92)*2+'path{notes/ROOT_SEARCH_LOG_35.md}\n'
assert before.count(old)==1
after=before.replace(old,new);ast.parse(after)
folder=w/'outputs/checkpoint35_workflow_setup'
prior=folder/'consolidate.before_escape_repair.py';assert not prior.exists();prior.write_text(before)
p.write_text(after)
(folder/'search_log_escape_repair.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='setup-warning',tofile='escaped-source')))
r={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'observed':'CP35 setup succeeded but ast.parse emitted a SyntaxWarning for the inserted Python string escape.',
 'repair':'Doubled exactly the Python-source backslash on the new ROOT_SEARCH_LOG_35 path. The generated LaTeX text and all mathematical content are unchanged.',
 'retained_output':'outputs/checkpoint35_setup.stderr.txt'}
(folder/'search_log_escape_repair.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))

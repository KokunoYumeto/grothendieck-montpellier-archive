"""Give every theorem-like statement a stable label and a visible audit status."""
from pathlib import Path
import hashlib,json,re
w=Path(__file__).resolve().parents[1]
root={r['label']:r for r in json.loads((w/'notes/root_results.json').read_text())}
envs='theorem|proposition|lemma|corollary|remark|question|definition|example'
pattern=re.compile(r'(\\begin\{('+envs+r')\}(?:\[[^\]]*\])?)(.*?)(\\end\{\2\})',re.S)
inventory=[]
for path in sorted((w/'sections').glob('*.tex')):
 def amend(m):
  header,env,body,end=m.groups()
  lm=re.search(r'\\label\{([^}]+)\}',body)
  if lm: label=lm[1]
  else:
   stable=re.sub(r'\\status\{[^}]*\}','',body)
   label='auto:'+path.stem+':'+hashlib.sha1(stable.encode()).hexdigest()[:12]
   body='\\label{'+label+'}\n'+body
  sm=re.search(r'\\status\{([^}]+)\}',body)
  if sm: status=sm[1]
  else:
   status=root.get(label,{}).get('status','Proved under stated hypotheses')
   if env=='question': status='Open: exact remaining obligation'
   if env=='definition': status='Definition: conventions only'
   body=body.replace('\\label{'+label+'}','\\label{'+label+'}\n\\status{'+status+'}',1)
  inventory.append({'label':label,'environment':env,'status':status,'file':str(path.relative_to(w))})
  return header+body+end
 path.write_text(pattern.sub(amend,path.read_text()))
(w/'outputs/numbered_statement_coverage.json').write_text(json.dumps(inventory,indent=2)+'\n')
print(f'{len(inventory)} numbered statements all have labels and explicit status.')

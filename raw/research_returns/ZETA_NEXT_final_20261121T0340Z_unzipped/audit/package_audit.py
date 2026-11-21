#!/usr/bin/env python3
"""Structural checks for the requested TeX/TSV delivery (not a TeX compiler)."""
from pathlib import Path
import csv, re, json, hashlib
from datetime import datetime,timezone
base=Path(__file__).resolve().parents[1]
text=(base/'ZETA_NEXT.tex').read_text()
errors=[]
def check(condition,message):
    if not condition:errors.append(message)
check(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',text),'Unexpected control character in TeX')
body=re.sub(r'(?<!\\)%[^\n]*','',text)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
    action,env=m.groups()
    if action=='begin':stack.append(env)
    elif not stack or stack.pop()!=env:errors.append('Mismatched environment '+env)
check(not stack,'Unclosed environments '+repr(stack))
depth=0
for m in re.finditer(r'(?<!\\)[{}]',body):
    depth+=1 if m.group()=='{' else -1
    if depth<0:errors.append('Premature closing brace');break
check(depth==0,'Unbalanced TeX braces')
labels=re.findall(r'\\label\{([^}]+)\}',body)
check(len(labels)==len(set(labels)),'Duplicate labels')
keys=re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',body)
check(len(keys)==len(set(keys)),'Duplicate bibliography keys')
cites=[]
for c in re.findall(r'\\cite(?:\[[^]]*\])*\s*\{([^}]+)\}',body):
    cites.extend(c.split(','))
check(set(cites)<=set(keys),'Unresolved citations '+repr(set(cites)-set(keys)))
refs=re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',body)
check(set(refs)<=set(labels),'Unresolved references '+repr(set(refs)-set(labels)))
check(not re.search(r'\\(?:input|include)\s*\{',body),'Paper has external TeX input dependency')
check(len(re.findall(r'(?<!\\)\\\[',body))==len(re.findall(r'(?<!\\)\\\]',body)),
      'Display-math delimiter mismatch')
check(len(re.findall(r'(?<!\\)\$',body))%2==0,'Odd number of inline math delimiters')

tsv_counts={}
for p in [base/'QUESTIONS.tsv',base/'CHECK_EVENTS.tsv']:
    with p.open() as f:
        rows=list(csv.reader(f,delimiter='\t'))
    check(bool(rows),'Empty '+p.name)
    check(all(len(r)==len(rows[0]) for r in rows),'TSV column mismatch '+p.name)
    tsv_counts[p.name]=len(rows)-1
with (base/'QUESTIONS.tsv').open() as f:
    questions=list(csv.DictReader(f,delimiter='\t'))
check(len(questions)==len({r['id'] for r in questions}),'Duplicate question ids')
with (base/'CHECK_EVENTS.tsv').open() as f:
    events=list(csv.DictReader(f,delimiter='\t'))
check(all(all(r[k] for k in ['statement_id','date_utc','who','model','effort','run','type','method','outcome']) for r in events),'Incomplete check-event metadata')
required=['NX%02d'%i for i in range(1,5)]+['NC%02d'%i for i in range(1,5)]+['NX-L%02d'%i for i in range(1,8)]+['NG%02d'%i for i in range(1,8)]
for sid in required:
    check(sid in labels,'Missing finding label '+sid)
    check(any(r['statement_id']==sid and r['type']=='targeted proof check' for r in events),'Missing proof check '+sid)
for name in ['ZETA_NEXT.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md']:
    check((base/name).is_file(),'Missing required file '+name)

report={
 'date_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
 'status':'PASS' if not errors else 'FAIL','errors':errors,
 'findings':len(required),'bibliography_entries':len(keys),'labels':len(labels),
 'tsv_rows':tsv_counts,'standalone_tex':True,
 'paper_sha256':hashlib.sha256((base/'ZETA_NEXT.tex').read_bytes()).hexdigest(),
 'limits':'Structural syntax, references, register shape and coverage checked. Not a LaTeX compilation or proof formalization.'
}
(base/'audit/PACKAGE_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if errors:raise SystemExit(1)

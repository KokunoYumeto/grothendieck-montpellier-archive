"""Structural and evidence-integrity checks; no compiler or proof assistant runs.

Compilation evidence schema (evidence/build/manifest.json, schema_version=1):
  source_path: "AN_GRH.tex"; source_sha256: lowercase SHA-256 of those bytes
  pdf_path: "AN_GRH.pdf"; pdf_sha256: lowercase SHA-256 of those bytes
  engine: nonempty compiler description; compile_exit_code: 0
  passes: positive integer; stable: true; page_count: positive integer
  overfull_hboxes: nonnegative integer; undefined_references: false
  visual_qa: {status: "passed"|"not_performed"|"failed", scope: string}
    A passed visual review additionally records source_sha256, pdf_sha256,
    and page_count matching this exact compilation. It may link retained
    contact sheets and reviewed pages in additional fields.
  formally_verified: false

Optional metadata (date, checker, exact commands, logs) is retained by the
producer. Paths are relative to the package root. This validator checks the
source/PDF hashes and the recorded build/QA scope, not a claimed mathematical
equivalence between source and PDF, nor the truth of the proofs. A present
PDF without matching evidence, or a stale source/PDF hash, fails validation.
If both PDF and manifest are absent, validation explicitly warns that only
structural checks are available. Page count is recorded evidence here;
the compile workflow obtains it independently using pdfinfo.
"""
from pathlib import Path
import csv, hashlib, json, re
R=Path(__file__).resolve().parent.parent
CHECK_EVENT_TYPES={
 'targeted proof check',
 'independent re-proof',
 'computation or formal certificate',
 'used and rechecked in this run',
 'carried as background without fault found',
 "refuted, with the refined statement's id",
}
EVENT_FIELDS=['statement_id','date','who_model_effort_run','type','outcome','evidence']
def validate_build_manifest(root):
 manifest_path=root/'evidence/build/manifest.json'
 pdf_path=root/'AN_GRH.pdf'
 if not manifest_path.is_file():
  assert not pdf_path.is_file(), 'AN_GRH.pdf exists without evidence/build/manifest.json; its relation to the current TeX source is unverified'
  return dict(status='not_compiled',visual_qa_status='not_performed',
   formally_verified=False,warnings=['No PDF or build manifest is present; structural checks do not establish successful compilation or visual QA.'])
 manifest=json.loads(manifest_path.read_text())
 assert manifest.get('schema_version')==1, 'Unsupported compilation-manifest schema'
 assert manifest.get('source_path')=='AN_GRH.tex', 'Compilation manifest must identify the standalone source AN_GRH.tex'
 assert manifest.get('pdf_path')=='AN_GRH.pdf', 'Compilation manifest must identify the optional reading copy AN_GRH.pdf'
 for key,path in [('source_sha256',root/'AN_GRH.tex'),('pdf_sha256',pdf_path)]:
  recorded=manifest.get(key,'')
  assert isinstance(recorded,str) and re.fullmatch(r'[0-9a-f]{64}',recorded), ('Invalid recorded SHA-256',key)
  assert path.is_file(), ('Missing compiled artifact',str(path))
  actual=hashlib.sha256(path.read_bytes()).hexdigest()
  assert actual==recorded, (f'STALE compilation evidence: {key} differs from the current file',recorded,actual)
 assert pdf_path.read_bytes().startswith(b'%PDF-'), 'Reading copy is not a PDF file'
 assert manifest.get('engine') and isinstance(manifest['engine'],str)
 assert manifest.get('compile_exit_code')==0, 'Recorded compiler run did not succeed'
 assert manifest.get('stable') is True, 'Recorded compilation did not stabilize'
 assert isinstance(manifest.get('passes'),int) and manifest['passes']>0
 assert isinstance(manifest.get('page_count'),int) and manifest['page_count']>0
 assert isinstance(manifest.get('overfull_hboxes'),int) and manifest['overfull_hboxes']>=0
 assert manifest.get('undefined_references') is False, 'Recorded compilation has unresolved references'
 assert manifest.get('formally_verified') is False, 'This package records compilation and mathematical review, not formal verification of the paper'
 warnings=[]
 if manifest['overfull_hboxes']:
  warnings.append(f"Compilation has {manifest['overfull_hboxes']} recorded overfull boxes; inspect layout evidence.")
 qa=manifest.get('visual_qa',{})
 assert qa.get('status') in {'passed','not_performed','failed'}, 'Missing or invalid visual-QA status'
 assert qa['status']!='failed', 'Visual PDF QA recorded a failure'
 if qa['status']=='passed':
  for key in ('source_sha256','pdf_sha256','page_count'):
   assert qa.get(key)==manifest[key], ('STALE visual-QA evidence',key)
  assert isinstance(qa.get('scope'),str) and qa['scope'].strip(), 'Visual-QA scope must be recorded'
 else:
  warnings.append('Compilation is recorded, but no completed visual PDF review is claimed.')
 return dict(status='compiled_source_and_pdf_hashes_match',manifest='evidence/build/manifest.json',
  source_sha256=manifest['source_sha256'],pdf_sha256=manifest['pdf_sha256'],
  engine=manifest['engine'],passes=manifest['passes'],reported_page_count=manifest['page_count'],
  overfull_hboxes=manifest['overfull_hboxes'],visual_qa_status=qa['status'],
  visual_qa_scope=qa.get('scope',''),formally_verified=False,warnings=warnings)
required=['AN_GRH.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md','TRANSCRIPTION_NOTES.tsv']
for n in required:assert (R/n).is_file() and (R/n).stat().st_size
summary={'required_files':required}
for n,expected in [('ROW_FULL_REGISTER_AUDIT.tsv',800),('ROW_FLAG_AUDIT.tsv',575),('ROW_UNIQUE_AUDIT.tsv',525),('ROW_EXCERPT_ONLY_AUDIT.tsv',97),('ROW_ANALYTIC_LEDGER.tsv',108),('GT_UNIT_CERTIFICATES.tsv',53),('GT_UNIT_WORDS.tsv',4825)]:
 with open(R/n,newline='',encoding='utf-8') as f:
  reader=csv.reader(f,delimiter='\t');head=next(reader);rows=list(reader)
 assert len(rows)==expected,(n,len(rows),expected)
 assert all(len(x)==len(head) for x in rows),n
 summary[n]=len(rows)
with open(R/'QUESTIONS.tsv',newline='',encoding='utf-8') as f:questions=list(csv.DictReader(f,delimiter='\t'))
assert len({x['id'] for x in questions})==len(questions)
with open(R/'CHECK_EVENTS.tsv',newline='',encoding='utf-8') as f:events=list(csv.DictReader(f,delimiter='\t'))
assert all(x['statement_id'] and x['date'] and x['who_model_effort_run'] and x['type'] and x['outcome'] for x in events)
assert all(x['type'] in CHECK_EVENT_TYPES for x in events), ('Unnormalized check-event categories',sorted({x['type'] for x in events}-CHECK_EVENT_TYPES))
assert len({tuple(x[k] for k in EVENT_FIELDS) for x in events})==len(events), 'Exact normalized check-event duplicates remain'
tex=(R/'AN_GRH.tex').read_text()
assert r'\input{' not in tex and r'\include{' not in tex
# Strip TeX comments, retaining escaped percentage signs.
clean=re.sub(r'(?<!\\)%[^\n]*','',tex)
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 typ,env=m.groups()
 if typ=='begin':stack.append(env)
 else:assert stack and stack.pop()==env,(m.group(),stack[-5:])
assert not stack
level=0
for m in re.finditer(r'(?<!\\)[{}]',clean):
 level+=1 if m.group()=='{' else -1
 assert level>=0,('unmatched close brace',m.start())
assert level==0,level
for a,b in [(r'(?<!\\)\\\[',r'(?<!\\)\\\]'),(r'(?<!\\)\\\(',r'(?<!\\)\\\)')]:assert len(re.findall(a,clean))==len(re.findall(b,clean)),(a,b)
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
bibkeys=re.findall(r'\\bibitem\{([^}]+)\}',tex)
assert len(bibkeys)==len(set(bibkeys))
used=set()
for z in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',tex):used.update(z.split(','))
assert not used-set(bibkeys),used-set(bibkeys)
findings=re.findall(r'\\paragraph\{Finding ([A-Z][0-9]+)\b',tex)
assert len(findings)==len(set(findings)),findings
checked={x['statement_id'] for x in events if x['type'] in {'targeted proof check','independent re-proof'}}
assert not set(findings)-checked,('missing recorded proof-check events',set(findings)-checked)
# Every nonarchive source in this retained manifest must match its source hash.
with open(R/'SOURCE_RECOVERY_MANIFEST.tsv',newline='',encoding='utf-8') as f: sources=list(csv.DictReader(f,delimiter='\t'))
count=0
for x in sources:
 p=R/x['local_path']
 if p.suffix=='.zip':continue
 assert p.is_file(),str(p)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],str(p)
 count+=1
# No hidden old checkpoint or source archive is nested in the package.
assert not list(R.rglob('*.zip'))
compilation=validate_build_manifest(R)
tex_status=('Structural checks PASS; recorded compilation matches current source/PDF hashes'
 if compilation['status']=='compiled_source_and_pdf_hashes_match'
 else 'Structural checks PASS; successful compilation is not established')
summary.update(question_rows=len(questions),check_events=len(events),finding_ids=findings,
 citation_keys=len(bibkeys),verified_source_files=count,tex_status=tex_status,
 compilation=compilation,formal_verification_status='Not performed for this paper; compilation and source review are distinct',
 check_event_types={kind:sum(x['type']==kind for x in events) for kind in sorted(CHECK_EVENT_TYPES)},
 finding_check_scope='Every numbered finding has a recorded proof-check event; the validator does not perform that mathematical check or promote reading to independent re-proof.')
(R/'evidence/package_validation.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))

"""Check active manuscript/ledger consistency; no mathematical assertion is tested."""
from pathlib import Path
import csv,json,re
ROOT=Path(__file__).resolve().parents[1]
seen=set()
def walk(path):
 if path in seen:return
 seen.add(path)
 for m in re.finditer(r'\\input\{([^}]+)\}',path.read_text()):
  p=ROOT/m.group(1)
  if not p.suffix:p=p.with_suffix('.tex')
  if p.exists():walk(p)
walk(ROOT/'RESEARCH_SA22_paper.tex')
pat=re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|claim|definition|counterexample|example|remark|question)\}(?:\[([\s\S]*?)\])?([\s\S]*?)\\end\{\1\}')
labels={};unlabelled=[]
for p in sorted(seen):
 for m in pat.finditer(p.read_text()):
  lab=re.search(r'\\label\{([^}]+)\}',m.group(3))
  if not lab:unlabelled.append([str(p.relative_to(ROOT)),m.group(2)]);continue
  key=lab.group(1)
  if key in labels:raise ValueError('Duplicate statement label '+key)
  labels[key]=dict(file=str(p.relative_to(ROOT)),kind=m.group(1),title=m.group(2),statement=m.group(3))
with (ROOT/'RESEARCH_SA22_results.csv').open() as f:rows=list(csv.DictReader(f))
with (ROOT/'CHECK_EVENTS.tsv').open() as f:events=list(csv.DictReader(f,delimiter='\t'))
rowids={r['id'] for r in rows}
eventids={e['statement_id'] for e in events}
cites=set()
for p in seen:
 for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',p.read_text()):cites.update(m.group(1).split(','))
bibkeys=set(re.findall(r'@\w+\{([^,]+),',(ROOT/'RESEARCH_SA22_references.bib').read_text()))
out=dict(active_files=len(seen),numbered_statements=len(labels),result_rows=len(rows),
 missing_result_rows=sorted(set(labels)-rowids),inactive_result_rows=sorted(rowids-set(labels)),
 statements_without_events=sorted(set(labels)-eventids),unlabelled_statements=unlabelled,
 missing_bibliography_keys=sorted(cites-bibkeys),cited_keys=len(cites),bibliography_keys=len(bibkeys))
(ROOT/'logs'/'records_audit.json').write_text(json.dumps(out,indent=2)+'\n')
(ROOT/'logs'/'active_statements.json').write_text(json.dumps(labels,indent=2)+'\n')
print(json.dumps(out,indent=2))

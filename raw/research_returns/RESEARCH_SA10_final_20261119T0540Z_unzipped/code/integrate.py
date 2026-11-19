"""Assemble result, check-event and bibliography fragments without changing proofs."""
from pathlib import Path
import csv, re, time

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
result_paths = [root / p for p in ['RESULTS_A.csv','RESULTS_B.csv','results_B56.csv','RESULTS_C.csv','results_C.csv','RESULTS_C1_B.csv']]
rows, seen = [], set()
for path in result_paths:
    if not path.exists():
        continue
    with path.open(newline='') as f:
        for row in csv.DictReader(f):
            if row['id'] in seen:
                raise ValueError('Duplicate result ID: '+row['id'])
            seen.add(row['id'])
            rows.append(row)
with (root/'RESEARCH_SA10_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
    writer.writeheader(); writer.writerows(rows)
events=[]
allowed_types={
    'targeted proof check','independent re-proof','computation or formal certificate',
    'used and rechecked in this run','carried as background without fault found',
    "refuted, with the refined statement's id"
}
type_map={
    'targeted proof and source check':'targeted proof check',
    'internal counterexample and repair':'targeted proof check',
    'proof audit':'targeted proof check',
    'source image inspection':'used and rechecked in this run',
    'programmatic finite check':'computation or formal certificate',
    'clerical consistency check':'used and rechecked in this run',
    'counterexample independent review':'targeted proof check',
    'independent proof':'independent re-proof',
    'primary source and hypothesis audit':'targeted proof check',
    'primary source and explicit construction':'targeted proof check',
    'finite computation':'computation or formal certificate',
    'failed proof route recorded':'targeted proof check',
    'independent presentation audit':'targeted proof check',
    'primary scan visual review':'used and rechecked in this run',
    'targeted source check':'used and rechecked in this run'
}
normalized=[]
for path in sorted(root.glob('CHECK_EVENTS_*.tsv')):
    with path.open(newline='') as f:
        for line,row in enumerate(csv.DictReader(f,delimiter='\t'),2):
            original=row['type']
            if original not in allowed_types:
                if original.startswith('refuted, with the refined statement'):
                    row['type']="refuted, with the refined statement's id"
                elif original in type_map:
                    row['type']=type_map[original]
                else:
                    raise ValueError(f'Unclassified check-event type: {path.name}:{line}: {original}')
                row['outcome']+=f' [Original event label: {original}.]'
                normalized.append((path.name,line,original,row['type']))
            events.append(row)
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    writer.writeheader(); writer.writerows(events)
with (root/'CHECK_EVENT_NORMALIZATION.tsv').open('w',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    writer.writerow(['source_file','source_line','original_type','aggregate_type'])
    writer.writerows(normalized)
base=root/'references_A.bib'
if not base.exists():
    base.write_text((root/'RESEARCH_SA10_references.bib').read_text())
parts=[base,root/'B_references.bib',root/'references_B56.bib',root/'references_C.bib',root/'C_references.bib',root/'references_C5_Hurewicz.bib',root/'references_supplement.bib']
texts=[p.read_text() for p in parts if p.exists()]
# Plain BibTeX notes are rendered as ordinary TeX: make the two literal
# research-input paths safe without changing citation keys or source URLs.
texts=[s.replace('literature_C/AFT/AFT1-2016.tex',r'\path{literature_C/AFT/AFT1-2016.tex}')
       .replace('work/references_B56',r'\path{work/references_B56}') for s in texts]
keys=[]
for s in texts:
    keys.extend(re.findall(r'@\w+\{([^,]+),',s))
if len(keys)!=len(set(keys)):
    raise ValueError('Duplicate bibliography keys')
(root/'RESEARCH_SA10_references.bib').write_text('\n\n'.join(texts))
print(f'Assembled {len(rows)} result rows, {len(events)} check events, {len(keys)} bibliography records.')
print(f'Runtime: {time.perf_counter()-start:.6f} seconds')

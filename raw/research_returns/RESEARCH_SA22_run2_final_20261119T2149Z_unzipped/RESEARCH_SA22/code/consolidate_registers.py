#!/usr/bin/env python3
"""One canonical row per numbered statement actually included in the paper.

Component registries remain unchanged as provenance. Canonical IDs are LaTeX
labels, which remain stable when the printed statement numbers change.
"""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import bisect, csv, hashlib, json, re
from A567_normalize_check_events import normalize_events

root = Path(__file__).resolve().parents[1]
started_utc = datetime.now(timezone.utc).isoformat()
started_clock = perf_counter()
component_names = [
    'A_results.csv', 'A567_results.csv', 'B_results.csv', 'C_results.csv',
    'A_CHECK_EVENTS.tsv', 'A567_CHECK_EVENTS.tsv', 'B_CHECK_EVENTS.tsv',
    'C_CHECK_EVENTS.tsv', 'ROOT_CHECK_EVENTS.tsv', 'notes/premerge_CHECK_EVENTS.tsv',
]
component_hashes_before = {
    name: hashlib.sha256((root/name).read_bytes()).hexdigest()
    for name in component_names if (root/name).exists()
}
fields = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
event_fields = ['statement_id','date','who','type','outcome']
envs = 'theorem|proposition|lemma|corollary|definition|example|remark|question'
pattern = re.compile(r'\\begin\{('+envs+r')\}(.*?)\\end\{\1\}', re.S)

def inputs(path, seen=None):
    seen = set() if seen is None else seen
    if path in seen: return
    seen.add(path)
    text = path.read_text()
    # Preserve actual source order, expanding only existing input files.
    pos = 0
    for m in re.finditer(r'\\input\{([^}]+)\}', text):
        yield path, text[pos:m.start()]
        child = root/m.group(1)
        if not child.suffix: child=child.with_suffix('.tex')
        if child.exists(): yield from inputs(child, seen)
        pos=m.end()
    yield path,text[pos:]

components=[]
for name in ['A_results.csv','A567_results.csv','B_results.csv','C_results.csv']:
    p=root/name
    if p.exists():
        for row in csv.DictReader(p.open()):
            row['_component']=name
            components.append(row)

numbers={}
aux=root/'build/RESEARCH_SA22_paper.aux'
if aux.exists():
    for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux.read_text()):
        numbers[m.group(1)]={'number':m.group(2),'pdf_page':m.group(3)}

rows=[]; legacy_to_labels={}; label_to_path={}
# Flatten includes before finding environments: a proof may itself contain an
# input, and its dependencies must not disappear at that file boundary.
parts=[]; starts=[]; owners=[]; offset=0
for source,part in inputs(root/'RESEARCH_SA22_paper.tex'):
    if part:
        starts.append(offset); owners.append(source); parts.append(part)
        offset+=len(part)
chunk=''.join(parts)
for m in pattern.finditer(chunk):
    path=owners[bisect.bisect_right(starts,m.start())-1]
    body=m.group(2)
    labels=re.findall(r'\\label\{([^}]+)\}',body)
    assert labels, ('Unlabelled numbered statement',str(path),body[:100])
    label=labels[0]
    explicit=re.search(r'\\status\{([^}]+)\}',body)
    heading=re.match(r'\s*\[([^\]]*)\]',body)
    status_text=(explicit.group(1) if explicit else heading.group(1) if heading else '').lower()
    if m.group(1)=='question': status='Open'
    elif status_text.startswith('refuted'): status='Refuted'
    elif status_text.startswith('proved under'): status='Proved under stated hypotheses'
    elif status_text.startswith('proved'): status='Proved'
    elif status_text.startswith('known'): status='Known'
    elif 'refuted' in status_text: status='Refuted'
    elif 'under stated' in status_text or 'under hypotheses' in status_text: status='Proved under stated hypotheses'
    elif 'known' in status_text: status='Known'
    else: status='Proved'
    matching=[r for r in components if re.search(r'(?<![\w:-])'+re.escape(label)+r'(?![\w:-])',r['where_proved'])]
    for r in matching:
        legacy_to_labels.setdefault(r['id'],set()).add(label)
    next_start=pattern.search(chunk,m.end())
    tail=chunk[m.end():next_start.start() if next_start else len(chunk)]
    proof=re.search(r'\\begin\{proof\}(?:\[[^\]]*\])?(.*?)\\end\{proof\}',tail,re.S)
    scope=body+(proof.group(1) if proof else '')
    refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',scope)
    cites=[]
    for c in re.findall(r'\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]+)\}',scope): cites.extend(c.split(','))
    deps=sorted(set(refs+cites+[r['depends_on'] for r in matching if r['depends_on']]))
    statement=re.sub(r'^\s*\[.*?\]','',body,count=1,flags=re.S)
    statement=re.sub(r'\\label\{[^}]+\}','',statement)
    statement=re.sub(r'\\status\{[^}]+\}','',statement)
    statement=' '.join(statement.split())
    pages='; '.join(dict.fromkeys(r['manuscript_pages'] for r in matching if r['manuscript_pages']))
    notes=[]
    if matching: notes.append('Component IDs: '+', '.join(r['id'] for r in matching))
    notes.extend(r['notes'] for r in matching if r['notes'])
    n=numbers.get(label,{})
    if n: notes.insert(0,'Printed '+m.group(1)+' '+n['number']+'; PDF page '+n['pdf_page'])
    row=dict(zip(fields,[label,statement,status,str(path.relative_to(root))+', label '+label,'; '.join(deps),pages,' | '.join(dict.fromkeys(notes))]))
    rows.append(row);label_to_path[label]=str(path.relative_to(root))

assert len(rows)==len({r['id'] for r in rows}), 'Duplicate statement label'

old=root/'notes/premerge_CHECK_EVENTS.tsv'
current=root/'CHECK_EVENTS.tsv'
if not old.exists() and current.exists(): old.write_bytes(current.read_bytes())
events=[]; seen=set()
for p in [old]+[root/n for n in ['A_CHECK_EVENTS.tsv','A567_CHECK_EVENTS.tsv','B_CHECK_EVENTS.tsv','C_CHECK_EVENTS.tsv','ROOT_CHECK_EVENTS.tsv']]:
    if not p.exists():continue
    for event in csv.DictReader(p.open(),delimiter='\t'):
        event={k:event.get(k,'') for k in event_fields}
        original=event['statement_id']
        direct=[label for label in label_to_path if re.search(r'(?<![\w:-])'+re.escape(label)+r'(?![\w:-])',original)]
        mapped=set(direct)
        for old_id,labels in legacy_to_labels.items():
            if re.search(r'(?<![\w.-])'+re.escape(old_id)+r'(?![\w.-])',original):mapped.update(labels)
        if not mapped: mapped={original}
        for label in sorted(mapped):
            e=event.copy();e['statement_id']=label
            if label!=original:e['outcome']+=' [Original event ID: '+original+']'
            # Early logs used brief attribution; expand, without inventing effort.
            if 'GPT-6' in e['who'] and 'ChatGPT Pro mode' not in e['who']:
                e['who']+='; GPT-6 Astra (OpenAI), inherited reasoning effort, ChatGPT Pro mode'
            key=tuple(e[k] for k in event_fields)
            if key not in seen:seen.add(key);events.append(e)

# Validate all reviewed transformations before writing any regenerated register.
# Unknown noncanonical descriptions/outcomes stop for review instead of being
# guessed into a stronger check category.
events, source_access_events, normalization = normalize_events(
    root, events, {r['id'] for r in rows}
)
component_hashes_after = {
    name: hashlib.sha256((root/name).read_bytes()).hexdigest()
    for name in component_hashes_before
}
if component_hashes_after != component_hashes_before:
    raise RuntimeError('A component input changed during consolidation; review required.')
with (root/'RESEARCH_SA22_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
with current.open('w',newline='') as f:
    w=csv.DictWriter(f,event_fields,delimiter='\t');w.writeheader();w.writerows(events)
with (root/'SOURCE_ACCESS_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,event_fields,delimiter='\t');w.writeheader();w.writerows(source_access_events)
covered={e['statement_id'] for e in events}
missing=[r['id'] for r in rows if r['id'] not in covered]
report={'numbered_statements':len(rows),'check_events':len(events),'missing_statement_events':missing,
        'missing_manuscript_locators':[r['id'] for r in rows if not r['manuscript_pages']],
        'printed_numbers_from_latest_aux':len(numbers),'component_rows':len(components),
        'canonical_id_rule':'one row for each included theorem-like environment, ID = first LaTeX label',
        'source_access_events':len(source_access_events),
        'normalization_record':'logs/A567_normalize_check_events.json',
        'started_utc':started_utc,
        'elapsed_seconds':perf_counter()-started_clock}
normalization.update({
    'started_utc':started_utc,
    'numbered_statements':len(rows),
    'component_hashes_before':component_hashes_before,
    'component_hashes_after':component_hashes_after,
    'component_files_unchanged':True,
    'output_sha256':{
        name:hashlib.sha256((root/name).read_bytes()).hexdigest()
        for name in ['CHECK_EVENTS.tsv','SOURCE_ACCESS_EVENTS.tsv','RESEARCH_SA22_results.csv']
    },
    'consolidation_elapsed_seconds':report['elapsed_seconds'],
})
(root/'logs/A567_normalize_check_events.json').write_text(json.dumps(normalization,indent=2)+'\n')
(root/'logs/register_consolidation.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))

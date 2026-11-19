"""Assemble live statement, event, and bibliography records without losing ownership."""
from pathlib import Path
import csv, json, re
ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
EVENT_FIELDS=['statement_id','date','who','type','outcome']
WHO='GPT-6 Astra (OpenAI, ChatGPT Pro mode; effort not separately exposed; root run)'

def read_rows(path, delimiter=','):
    with path.open(newline='') as f:return list(csv.DictReader(f,delimiter=delimiter))

def write_rows(path,fields,rows,delimiter=','):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter)
        w.writeheader();w.writerows(rows)

rows={}
for p in sorted((ROOT/'checks').glob('*_results.csv')):
    for row in read_rows(p):rows[row['id']]=row
root_sections=['part_a1.tex','part_a2.tex','part_a3.tex','part_a4.tex',
               'part_a2_limits.tex','part_a2b_secondary.tex','part_a1_range.tex',
               'part_a1_bordered.tex','part_a1_cut_choice.tex','part_a2_collar_general.tex',
               'part_a1_algebraicity.tex','part_a1_plumbing.tex']
events=[]
for p in sorted((ROOT/'checks').glob('*_events.tsv')):
    events.extend(read_rows(p,'\t'))

statement_re=re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|claim|definition|counterexample|example|remark|question)\}(?:\[([\s\S]*?)\])?([\s\S]*?)\\end\{\1\}')
missing=[]
for filename in root_sections:
    p=ROOT/'sections'/filename
    if not p.exists():continue
    for m in statement_re.finditer(p.read_text()):
        typ,title,body=m.groups();title=title or ''
        label=re.search(r'\\label\{([^}]+)\}',body)
        if label is None:
            missing.append((filename,title));continue
        ident=label.group(1)
        status=('Refuted' if 'Refuted' in title else
                'Known' if 'Known' in title else
                'Proved under stated hypotheses' if 'stated' in title or 'hypoth' in title or 'under' in title else 'Proved')
        page=('67/074-082' if ident.startswith('A1') else
              '67/071-074' if ident.startswith('A3') else
              '67/016-021' if ident.startswith('A4') else '67/061-070,021')
        if ident not in rows:
            rows[ident]=dict(id=ident,statement=' '.join(title.split()),status=status,
                  where_proved='sections/'+filename+', label '+ident,
                  depends_on=';'.join(dict.fromkeys(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',body))),
                  manuscript_pages=page,notes='Full proof in manuscript; source and independent checks separately recorded.')
        else:rows[ident]['where_proved']='sections/'+filename+', label '+ident

# Normalize task-oriented contributor rows to one row per numbered statement.
# Keep the contributor files intact: the merged ledger uses LaTeX labels as IDs.
active={};seen=set();proof_text={}
def walk(path):
    if path in seen:return
    seen.add(path)
    source=path.read_text()
    for m in statement_re.finditer(source):
        typ,title,body=m.groups();lab=re.search(r'\\label\{([^}]+)\}',body)
        if lab:
            ident=lab.group(1)
            active[ident]=(path,typ,title or '',body)
            tail=source[m.end():]
            next_statement=statement_re.search(tail)
            if next_statement:tail=tail[:next_statement.start()]
            proof_text[ident]=body+'\n'+tail
    for m in re.finditer(r'\\input\{([^}]+)\}',source):
        p=ROOT/m.group(1)
        if not p.suffix:p=p.with_suffix('.tex')
        if p.exists():walk(p)
walk(ROOT/'RESEARCH_SA22_paper.tex')
aliases={}
for ident,row in rows.items():
    aliases[ident]=([ident] if ident in active else
       [lab for lab in active if re.search(r'(?<![\w:-])'+re.escape(lab)+r'(?![\w:-])',row['where_proved'])])
normalized={}
aux=(ROOT/'logs'/'RESEARCH_SA22_paper.aux')
numbers=dict((m.group(1),(m.group(2),m.group(3))) for m in
    re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux.read_text() if aux.exists() else ''))
for lab,(path,typ,title,body) in active.items():
    candidates=[row for ident,row in rows.items() if aliases.get(ident)==[lab]]
    if lab in rows:row=dict(rows[lab])
    elif candidates:row=dict(candidates[0])
    else:
        row=dict(id=lab,status='Known' if 'Known' in title else 'Refuted' if 'Refuted' in title else 'Proved',depends_on='',manuscript_pages='',notes='')
    taskids=[ident for ident,targets in aliases.items() if lab in targets and ident!=lab]
    row['id']=lab
    row['statement']=' '.join(re.sub(r'\\label\{[^}]+\}','',body).split())
    row['where_proved']=str(path.relative_to(ROOT))+', label '+lab
    if lab in numbers:row['where_proved']+=', statement '+numbers[lab][0]+', PDF p. '+numbers[lab][1]
    original_status=row['status']
    if 'Refuted' in original_status:row['status']='Refuted'
    elif original_status.startswith('Known'):row['status']='Known'
    elif 'hypotheses' in original_status or 'under' in title:row['status']='Proved under stated hypotheses'
    else:row['status']='Proved'
    deps=list(dict.fromkeys(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',proof_text[lab])))
    citekeys=[]
    for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',proof_text[lab]):citekeys.extend(m.group(1).split(','))
    extra=';'.join(deps+['source:'+key for key in dict.fromkeys(citekeys)])
    row['depends_on']=';'.join(filter(None,[row.get('depends_on',''),extra]))
    row['notes']=(row.get('notes','')+(' Task aliases: '+', '.join(taskids)+'.' if taskids else '')).strip()
    if original_status!=row['status']:row['notes']+=' Contributor status detail: '+original_status+'.'
    normalized[lab]=row
normalized_events=[]
for event in events:
    ident=event['statement_id'];targets=aliases.get(ident,[])
    if re.fullmatch(r'L\d+',ident) or ident.startswith('SA22-'):
        normalized_events.append(event)
    elif targets and ident not in active:
        for lab in targets:
            e=dict(event);e['statement_id']=lab
            e['outcome']='[Original task ID '+ident+'] '+e['outcome']
            normalized_events.append(e)
    else:normalized_events.append(event)
rows=normalized;events=normalized_events

bibs=sorted((ROOT/'sources').glob('part_*.bib'))
(ROOT/'RESEARCH_SA22_references.bib').write_text('% Source status is recorded in every entry.\n\n'+'\n'.join(p.read_text() for p in bibs))
write_rows(ROOT/'RESEARCH_SA22_results.csv',FIELDS,list(rows.values()))
write_rows(ROOT/'CHECK_EVENTS.tsv',EVENT_FIELDS,events,'\t')
result=dict(statement_rows=len(rows),check_events=len(events),bibliography_fragments=len(bibs),
            missing_statement_labels=missing)
(ROOT/'logs'/'records_assembly.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

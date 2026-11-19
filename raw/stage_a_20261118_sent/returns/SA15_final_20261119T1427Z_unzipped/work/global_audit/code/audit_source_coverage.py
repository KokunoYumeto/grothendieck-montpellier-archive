"""Audit recorded source-access coverage; do not infer mathematical proof checks.

Inputs are the existing per-package ledgers, root's headerless access ledger,
global targeted-read ledger, and the independently completed root-doubts ledger.
Two genuinely new scope-check reads are recorded explicitly with their observed
tool-output identifiers; no earlier event is invented for their prior gaps.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import csv
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/26604d0a9a98')
OUT = ROOT/'work/global_audit'
NOW = datetime.now(timezone.utc).isoformat(timespec='seconds')
RUN = 'SA15-20261119/source-coverage-independent'
SCOPE = {'4','5','6','7','8','9'}
PAGE_MAP = 'work/page_map.json'
pages = json.loads((ROOT/PAGE_MAP).read_text())
evidence = []
ignored = []
input_hashes = {}

def digest(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def normalize(source):
    source = source.removeprefix(str(ROOT)+'/')
    if source.startswith('SA15_'):
        source = 'sources/'+source
    return source

def add(source, start, end, kind, record, note, at=''):
    source = normalize(source)
    if not source.startswith('sources/'):
        ignored.append({'record':record,'source':source,'reason':'Not an original source file; cannot establish manuscript/notes coverage.'})
        return
    start,end = int(start),int(end)
    p=ROOT/source
    assert p.is_file(), source
    total=len(p.read_text().splitlines())
    assert 1 <= start <= end <= total, (source,start,end,total,record)
    evidence.append({'id':f'SCE-{len(evidence)+1:04d}','source':source,
                     'start_line':start,'end_line':end,'kind':kind,
                     'documentary_record':record,'recorded_time':at,
                     'note':note,'source_sha256':digest(source)})

def rows(path):
    input_hashes[path]=digest(path)
    with (ROOT/path).open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

p='work/cotes5_6/source_read_log.tsv'
for n,r in enumerate(rows(p),2):
    span=re.fullmatch(r'(\d+)\s*[–-]\s*(\d+)',r['file_lines'])
    assert span,(p,n,r)
    add(r['source'],*span.groups(),'source_read_ledger',f'{p}:{n}',r['reading'],r['date_utc'])

p='work/cotes6_7/source_read_log.tsv'
for n,r in enumerate(rows(p),2):
    add(r['file'],r['line_start'],r['line_end'],'source_read_ledger',f'{p}:{n}',r['status']+'; '+r['evidence'],r['review_date'])

p='work/cotes8_9_4/source_read_log.tsv'
for n,r in enumerate(rows(p),2):
    kind='documented_initial_read' if r['note'].startswith('Initial reading before the utility') else 'source_read_ledger'
    add(r['source'],r['start_line'],r['end_line'],kind,f'{p}:{n}',r['note'],r['date_utc'])

p='work/source_access_log.tsv'
input_hashes[p]=digest(p)
with (ROOT/p).open(newline='') as f:
    for n,r in enumerate(csv.reader(f,delimiter='\t'),1):
        assert len(r)==6,(p,n,r)
        at,source,start,end,artifact,note=r
        assert (ROOT/artifact).is_file(), artifact
        add(source,start,end,'source_access_display',f'{p}:{n}',note+'; saved extract '+artifact,at)

p='work/global_audit/root_doubts_source_read_log.tsv'
for n,r in enumerate(rows(p),2):
    if r['source'].startswith('sources/'):
        assert r['source_sha256']==digest(r['source'])
    add(r['source'],r['line_start'],r['line_end'],'source_read_ledger',f'{p}:{n}',r['read_kind']+'; output '+r['tool_output']+'; '+r['qualification'],r['recorded_at_utc'])

p='work/global_audit/source_read_log.tsv'
for n,r in enumerate(rows(p),2):
    source=normalize(r['source'])
    if not source.startswith('sources/'):
        ignored.append({'record':f'{p}:{n}','source':source,'reason':'Derived-register/code read; no original-source span.'})
        continue
    assert r['sha256']==digest(source)
    match=re.search(r'Targeted source rereading: lines ([\d–\- and]+),',r['read_scope'])
    assert match,(p,n,r)
    for a,b in re.findall(r'(\d+)[–-](\d+)',match.group(1)):
        add(source,a,b,'targeted_read_ledger',f'{p}:{n}',r['read_scope'],r['date_utc'])

# Exact contemporary statement of the full P56 transcription read. This is
# documentary narrative evidence, not a newly created retrospective event.
p='work/cotes5_6/research_log.md'
input_hashes[p]=digest(p)
line=(ROOT/p).read_text().splitlines()[6]
assert 'full Pro transcription (2033 numbered file lines)' in line
add('sources/SA15_texts/pro/MPL_5+6_001-037_transcription.tex',1,2033,
    'documented_full_read_statement',p+':7',line,'2026-11-19; date recorded in the research log')

# Current genuine reads prompted by checking the scope of unlogged apparatus.
# They remain distinct from all prior ledger evidence.
fresh=[
    {'source':'sources/SA15_notes/pro/MPL_8_079-081+9+4+100_doubts.md',
     'start_line':908,'end_line':1047,'tool_output':'3d00ec',
     'note':'Entire shared Abbreviations and Legibility/limits appendix read now to determine scope. It includes in-scope material and is not solely cote100. No additional high-impact reading alarm beyond the existing P89448 was found in the follow-up comparison.'},
    {'source':'sources/SA15_notes/pro/MPL_5+6_001-037_notes.md',
     'start_line':1,'end_line':10,'tool_output':'9928bd',
     'note':'Entire notes introduction read now after finding that the substantive-note ledger starts at line11. Describes editorial conventions and source counts; no new mathematical claim or reading alarm.'},
]
fresh_log='work/global_audit/source_coverage_current_reads.tsv'
with (ROOT/fresh_log).open('w',newline='') as f:
    fields=['run_id','recorded_at_utc','source','start_line','end_line','reader','tool_output','read_kind','source_sha256','note']
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
    for r in fresh:
        w.writerow({'run_id':RUN,'recorded_at_utc':NOW,'reader':'GPT-6 Astra Pro; effort not exposed',
                    'read_kind':'actual current scope-check read; not a retrospective event',
                    'source_sha256':digest(r['source']),**r})
for n,r in enumerate(fresh,2):
    add(r['source'],r['start_line'],r['end_line'],'current_scope_check',
        f'{fresh_log}:{n}',r['note']+'; actual tool output '+r['tool_output'],NOW)
input_hashes[fresh_log]=digest(fresh_log)
input_hashes[PAGE_MAP]=digest(PAGE_MAP)

def spans(numbers):
    numbers=sorted(set(numbers))
    if not numbers:return []
    out=[];start=last=numbers[0]
    for x in numbers[1:]:
        if x==last+1:last=x
        else:out.append([start,last]);start=last=x
    out.append([start,last]);return out

def span_text(numbers):
    return ';'.join(str(a) if a==b else f'{a}–{b}' for a,b in spans(numbers))

by_source=defaultdict(list)
for r in evidence:by_source[r['source']].append(r)

def assess(unit_type,source,required,cote='',scan='',scope_note=''):
    required=set(required)
    assert required
    relevant=[r for r in by_source[source]
              if required.intersection(range(r['start_line'],r['end_line']+1))]
    coverage_by_kind=defaultdict(set)
    for r in relevant:
        coverage_by_kind[r['kind']].update(required.intersection(range(r['start_line'],r['end_line']+1)))
    prior=set().union(*(s for k,s in coverage_by_kind.items() if k!='current_scope_check'))
    covered=set().union(*coverage_by_kind.values())
    missing=required-covered
    prior_missing=required-prior
    ordinary=set().union(*(s for k,s in coverage_by_kind.items() if k not in {'current_scope_check','documented_initial_read','documented_full_read_statement'}))
    if missing:status='gap_in_recorded_coverage'
    elif prior_missing:status='covered_after_current_scope_check'
    elif required-ordinary:status='covered_including_documented_initial_or_full_read'
    else:status='covered_by_prior_recorded_spans'
    return {
        'unit_type':unit_type,'source':source,'cote':cote,'scan':scan,
        'scope':scope_note,'required_spans':span_text(required),'required_lines':len(required),
        'prior_covered_lines':len(prior),'covered_lines':len(covered),
        'status':status,'missing_spans':span_text(missing),
        'prior_missing_spans':span_text(prior_missing),
        'documented_only_spans':span_text((required-ordinary)&prior),
        'evidence_kinds':';'.join(sorted(coverage_by_kind)),
        'evidence_refs':';'.join(r['id'] for r in relevant),
        'qualification':'Recorded source-access/read evidence only; does not establish a mathematical proof or a new visual inspection of scans.',
    }

scan_rows=[]
excluded_pages=[]
for p in pages:
    if str(p['cote']) not in SCOPE:
        excluded_pages.append(p)
        continue
    scan_rows.append(assess('scan_block',normalize(p['file']),range(p['line_start'],p['line_end']+1),
                           str(p['cote']),str(p['scan']),
                           'In-scope page_map block; scan numbers are source identifiers, not assumed consecutive.'))
assert len(scan_rows)==346
assert sum('/pro/' in r['source'] for r in scan_rows)==304
assert sum('/codex/' in r['source'] for r in scan_rows)==42
assert len(excluded_pages)==52 and all(str(p['cote'])=='100' for p in excluded_pages)

file_rows=[]
excluded_file_spans=[]
for p in sorted((ROOT/'sources/SA15_texts').rglob('*.tex')):
    source=str(p.relative_to(ROOT))
    if source.endswith('PREAMBLE.tex') or source not in by_source:continue
    lines=p.read_text().splitlines()
    required=set(range(1,len(lines)+1))
    scope_note='Complete provided transcription file, including cote delimiters.'
    if '8_079-081+9+4+100' in source:
        cutoff=next(i for i,s in enumerate(lines,1) if s.strip()=='\\cotefile{100}')
        assert cutoff==1313
        required=set(range(1,cutoff))
        excluded_file_spans.append({'source':source,'spans':[[cutoff,len(lines)]],'reason':'Cote100 delimiter and all cote100 blocks; out of scope.'})
        scope_note='Lines1–1312, all cotes8/079–081,9 and4 content; cote100 begins at delimiter1313 and is excluded.'
    file_rows.append(assess('transcription_file',source,required,scope_note=scope_note))

for p in sorted((ROOT/'sources/SA15_notes').rglob('*.md')):
    source=str(p.relative_to(ROOT))
    lines=p.read_text().splitlines()
    required=set(range(1,len(lines)+1))
    scope_note='Entire supplied notes/doubts file, including headings and shared apparatus.'
    if '8_079-081+9+4+100_notes.md' in source:
        cutoff=next(i for i,s in enumerate(lines,1) if re.match(r'## \d+\. Cote 100,',s))
        assert cutoff==599
        required=set(range(1,cutoff))
        excluded_file_spans.append({'source':source,'spans':[[599,len(lines)]],'reason':'Every following note heading is explicitly cote100; no shared appendix follows.'})
        assert all('Cote 100,' in s for s in lines[598:] if re.match(r'## \d+\.',s))
        scope_note='Lines1–598 include all148 in-scope substantive notes and their introduction; cote100-only notes599–1401 excluded.'
    elif '8_079-081+9+4+100_doubts.md' in source:
        assert re.match(r'\| 100 \|',lines[422])
        assert lines[907]=='## Abbreviations'
        required=set(range(1,423))|set(range(908,len(lines)+1))
        excluded_file_spans.append({'source':source,'spans':[[423,907]],'reason':'Cote100-only doubt rows and following blank separator; shared appendix908–1047 remains in scope.'})
        scope_note='Lines1–422 plus shared appendix908–1047. Cote100-only doubt rows423–907 excluded; shared apparatus is conservatively retained in full.'
    file_rows.append(assess('notes_or_doubts_file',source,required,scope_note=scope_note))

all_rows=scan_rows+file_rows
assert len(file_rows)==20 and len(all_rows)==366
assert len([r for r in file_rows if r['unit_type']=='notes_or_doubts_file'])==12
fields=list(all_rows[0])
with (OUT/'source_coverage.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(all_rows)

summary={
    'run_id':RUN,'created_at_utc':NOW,'model':'GPT-6 Astra Pro','effort':'not exposed',
    'scope_cotes':sorted(SCOPE,key=int),
    'page_map_total':len(pages),'in_scope_pro_scan_blocks':304,'in_scope_codex_scan_blocks':42,
    'excluded_cote100_scan_blocks':52,
    'scan_blocks_by_coverage_status':dict(Counter(r['status'] for r in scan_rows)),
    'source_files_by_coverage_status':dict(Counter(r['status'] for r in file_rows)),
    'source_files':20,'transcription_files':8,'notes_or_doubts_files':12,
    'prior_log_gaps_in_file_apparatus':[{'source':r['source'],'spans':r['prior_missing_spans']} for r in file_rows if r['prior_missing_spans']],
    'remaining_scan_gaps':[r for r in scan_rows if r['missing_spans']],
    'remaining_file_gaps':[r for r in file_rows if r['missing_spans']],
    'documented_initial_or_full_read_use':[{'source':r['source'],'spans':r['documented_only_spans'],'unit_type':r['unit_type'],'cote':r['cote'],'scan':r['scan']} for r in all_rows if r['documented_only_spans']],
    'new_reading_alarms_from_shared_appendix':0,
    'shared_appendix_check':'Owner of P894 compared appendix908–1047 against existing48 alarms: no missing high-impact row. The abbreviation gén at9:20 is plus généralement at transcription613; listed difficult passages were already registered.',
    'evidence_kind_counts':dict(Counter(r['kind'] for r in evidence)),
    'interpretation':'An interval-union audit of recorded source display/read evidence. It neither verifies every mathematical statement nor proves historical correctness or actual ink. Read/access events are not reclassified as proof checks.',
    'input_sha256':input_hashes,
    'source_sha256':{s:digest(s) for s in sorted({r['source'] for r in all_rows})},
    'scan_blocks':scan_rows,'files':file_rows,'excluded_pages':excluded_pages,
    'excluded_file_spans':excluded_file_spans,'evidence':evidence,'ignored_non_source_records':ignored,
}
(OUT/'source_coverage.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')

md='''# Source-access coverage audit

This is a mechanical interval-union audit of **recorded source reads and source displays**. It is not a mathematical proof check, an independent certification of every historical statement, or a visual inspection of the manuscript scans. No source-access record is relabelled as a proof event.

## Scope and result

`work/page_map.json` has 398 blocks: **304 in-scope Pro blocks**, **42 in-scope Codex blocks**, and **52 cote100 blocks excluded from this task**. Every one of the 346 in-scope scan blocks is covered by the recorded evidence. The audit also checks complete in-scope file spans, including introductions, delimiters and shared apparatus, for eight transcriptions and twelve notes/doubts files.

The package8/9/4 transcription uses the explicitly documented initial read of lines1–335 in `work/cotes8_9_4/source_read_log.tsv:21`. This is distinguished from utility-generated later reads. The P56 transcription's first cote delimiter is covered by the explicit full-2033-line statement in `work/cotes5_6/research_log.md:7`; its scan blocks are already covered by the per-page ledger. Root's headerless `work/source_access_log.tsv` is parsed as a six-column access record, preserving its statement that a displayed extract is not a mathematical check.

## Honest prior gaps and current reads

Two apparatus spans lacked coverage in the earlier ledgers:

- P56 notes lines1–10: the introduction preceding the444 substantive notes.
- P894 doubts lines908–1047: the shared abbreviation and legibility appendix, which includes in-scope references and therefore cannot be dismissed as cote100-only material.

Both spans were actually opened and read during this audit. Their tool outputs are9928bd and3d00ec respectively. They are recorded in `source_coverage_current_reads.tsv` as **current scope-check reads**, never as invented earlier events. `prior_missing_spans` preserves both gaps in the TSV/JSON. There are no remaining in-scope coverage gaps after these current reads.

The shared appendix was also compared with the48 P894 reading alarms. It adds no independent high-impact mathematics-dependent alarm: the cited difficult passages are already registered; “plus gén.” at9/20, transcription613, is “plus généralement.” No reading row was appended from this apparatus check.

## Notes/doubts boundaries

The three wholly in-scope Pro notes files and their three doubts files are checked in full. The mixed P894 notes file is in scope through line598; every subsequent note is expressly cote100. Its doubts file is in scope at1–422 and again at908–1047 for shared apparatus; the cote100-only doubt rows423–907 are excluded. All four Codex notes files are checked in full. No Codex doubts files were supplied.

## Evidence and reproducibility

`source_coverage.tsv` has one row for each of346 scan blocks and20 file scopes. It records required spans, prior coverage, current coverage, any missing spans, documentary-only spans and evidence IDs. `source_coverage.json` resolves those IDs to exact ledger file/line references, preserves all52 excluded cote100 blocks and file exclusions, and records source/input hashes. `code/audit_source_coverage.py` reproduces the interval calculations without generating read events for missing historical coverage.
'''
(OUT/'source_coverage.md').write_text(md)
validation={k:summary[k] for k in ['in_scope_pro_scan_blocks','in_scope_codex_scan_blocks','excluded_cote100_scan_blocks','scan_blocks_by_coverage_status','source_files_by_coverage_status','prior_log_gaps_in_file_apparatus','remaining_scan_gaps','remaining_file_gaps','new_reading_alarms_from_shared_appendix']}
validation['tsv_rows']=len(all_rows)
(OUT/'outputs/source_coverage_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(validation,ensure_ascii=False,indent=2))

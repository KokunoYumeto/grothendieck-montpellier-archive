"""Independently reconstruct checked readings from recorded physical edits.

Nonprinting review comments are ignored. This is a diagnostic audit: unresolved
chains must be explained before certification, never repaired by inference.
"""
from pathlib import Path
import csv,hashlib,json,re,difflib,collections
P=Path(__file__).resolve().parents[1];I=P.parent/'inputs/text/transcription';R=P/'records'
rows=list(csv.DictReader((R/'CHECK_DECISIONS.tsv').open(),delimiter='\t'));bykey=collections.defaultdict(list)
for r in rows:bykey[r['key']].append(r)
rows_by_id=collections.defaultdict(list)
for r in rows:rows_by_id[r['source_id']].append(r)
adjudication_path=R/'REPLAY_RECORD_ADJUDICATIONS.json'
adjudication_bytes=adjudication_path.read_bytes() if adjudication_path.exists() else None
adjudications=json.loads(adjudication_bytes).get('entries',[]) if adjudication_bytes else []
adjudication_sha=hashlib.sha256(adjudication_bytes).hexdigest() if adjudication_bytes else None
adjudication_by_id=collections.defaultdict(list)
for entry in adjudications:adjudication_by_id[entry['source_id']].append(entry)
adjudication_issues=[];used_adjudications=set()
def row_hash(row):
    return hashlib.sha256(json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def bound_row_matches(bound):
    matches=rows_by_id.get(bound.get('source_id'),[])
    if len(matches)!=1:return False
    row=matches[0]
    return (bound.get('record')==row and bound.get('record_sha256')==row_hash(row)
            and bound.get('before_utf8_sha256')==hashlib.sha256(row['transcription_reading'].encode()).hexdigest()
            and bound.get('after_utf8_sha256')==hashlib.sha256(row['image_reading'].encode()).hexdigest())
def explanatory_record(row,reconstructed,final,path,applied):
    entries=adjudication_by_id.get(row['source_id'],[])
    if not entries:return None
    reasons=[]
    if len(entries)!=1:
        adjudication_issues.append({'key':row['key'],'source_id':row['source_id'],'reason':'Duplicate adjudication entries.'});return None
    entry=entries[0];support=entry.get('supporting_decisions',[])
    if entry.get('disposition')!='already_incorporated_explanatory_record' or entry.get('key')!=row['key']:
        reasons.append('Wrong adjudication disposition or source key.')
    if (entry.get('explanatory_decision',{}).get('record')!=row
            or not bound_row_matches(entry.get('explanatory_decision',{}))):
        reasons.append('Explanatory decision text or hash no longer matches.')
    if entry.get('checked_source_sha256')!=hashlib.sha256(path.read_bytes()).hexdigest():
        reasons.append('Checked-source bytes no longer match the adjudication.')
    if not support:reasons.append('No concrete supporting edit rows.')
    applied_ids={item['source_id'] for item in applied}
    for bound in support:
        if not bound_row_matches(bound):
            reasons.append('Supporting decision text or hash no longer matches: '+str(bound.get('source_id')));continue
        supporting=bound['record'];sid=supporting['source_id'];after=supporting['image_reading']
        if supporting['key']!=row['key'] or not sid.startswith(('EDIT:','CHANGE:')) or sid not in applied_ids:
            reasons.append('Supporting concrete edit was not replayed for this page: '+sid)
        if not after or after not in reconstructed or after not in final:
            reasons.append('Supporting exact replacement is absent from reconstructed or checked source: '+sid)
    if reasons:
        adjudication_issues.append({'key':row['key'],'source_id':row['source_id'],'reason':' '.join(reasons)});return None
    used_adjudications.add(row['source_id'])
    return {'key':row['key'],'source_id':row['source_id'],'disposition':entry['disposition'],
            'supporting_source_ids':[bound['source_id'] for bound in support],
            'adjudication':'records/REPLAY_RECORD_ADJUDICATIONS.json','adjudication_sha256':adjudication_sha}
def visible(s):
    s=re.sub(r'(?m)(?<!\\)%[^\n]*','',s)
    return '\n'.join(x.rstrip() for x in s.strip().splitlines()).strip()
def ordinal(r):
    sid=r['source_id'];end=sid.rsplit(':',1)[-1]
    return (0 if sid.startswith(('CHANGE:','EDIT:')) else 1,int(end) if end.isdigit() else 99999,sid)
reports=[]
for path in sorted((P/'checked_pages').glob('*.tex')):
    key=path.stem;original=(I/('brown_pages' if key.startswith('brown_') else 'ps_pages')/path.name).read_text();s=original
    final=path.read_text()
    candidates=[r for r in bykey[key] if (r['source_id'].startswith(('CHANGE:','EDIT:','MECH:','RECHECK:')) or r['source_id']=='PROV:ps_134-6_030:prime') and ':integrated:' not in r['source_id'] and r['decision']!='mechanical override repaired']
    applied=[];unmatched=[];explanatory=[]
    for r in sorted(candidates,key=ordinal):
        before,after=r['transcription_reading'],r['image_reading']
        if before==after:continue
        if r['source_id'].startswith(('MECH:','RECHECK:','PROV:')) and before and after:
            before_positions=[m.start() for m in re.finditer(re.escape(before),s)]
            after_ranges=[(m.start(),m.end()) for m in re.finditer(re.escape(after),s)]
            if before_positions and all(any(a<=pos and pos+len(before)<=b for a,b in after_ranges) for pos in before_positions):
                applied.append({'source_id':r['source_id'],'already_incorporated_in_edit_chain':True});continue
        if before and before in s:
            count=s.count(before);s=s.replace(before,after);applied.append({'source_id':r['source_id'],'occurrences':count})
        elif after and after in s:applied.append({'source_id':r['source_id'],'already_present':True})
        else:
            explanation=explanatory_record(r,s,final,path,applied)
            if explanation is not None:explanatory.append(explanation)
            else:unmatched.append(r['source_id'])
    state=R/'SOURCE_NORMALIZATION.json'
    if state.exists():
        from build_readers import normalize,repair_diagram_separators,repair_macro_layout,preserve_front_lineation,local_layout_repairs
        fixes=[]
        try:s=local_layout_repairs(preserve_front_lineation(repair_macro_layout(repair_diagram_separators(normalize(s,key,fixes),key,fixes),key,fixes),key,fixes),key,fixes)
        except Exception as error:unmatched.append('normalization could not replay: '+repr(error))
    same=visible(s)==visible(final)
    diff=''.join(difflib.unified_diff(visible(s).splitlines(True),visible(final).splitlines(True),fromfile='recorded_edit_reconstruction',tofile='checked_source')) if not same else ''
    reports.append({'key':key,'printing_content_equal':same,'applied_edits':len(applied),'already_incorporated_explanatory_records':explanatory,'unmatched_record_ids':unmatched,'difference':diff})
for sid in sorted(set(adjudication_by_id)-used_adjudications):
    if not any(issue['source_id']==sid for issue in adjudication_issues):
        adjudication_issues.append({'source_id':sid,'reason':'Adjudication was not used by the current replay.'})
unmatched_records=[{'key':r['key'],'source_id':sid} for r in reports for sid in r['unmatched_record_ids']]
explanatory_records=[entry for r in reports for entry in r['already_incorporated_explanatory_records']]
expected_keys={m['key'] for m in json.loads((P.parent/'inputs/text/records/PAGES_PS.json').read_text())}
source_coverage_complete={r['key'] for r in reports}==expected_keys
exceptions=[r for r in reports if not r['printing_content_equal'] or r['unmatched_record_ids']]
result={'schema_version':2,'complete':source_coverage_complete and not (exceptions or adjudication_issues),
        'source_coverage_complete':source_coverage_complete,'pages':len(reports),
        'equal_pages':sum(r['printing_content_equal'] for r in reports),
        'already_incorporated_explanatory_records':explanatory_records,
        'unmatched_records':unmatched_records,'adjudication_issues':adjudication_issues,
        'adjudication_file':'records/REPLAY_RECORD_ADJUDICATIONS.json' if adjudication_bytes else None,
        'adjudication_sha256':adjudication_sha,'exceptions':exceptions,'all_page_results':reports}
(R/'CHANGE_REPLAY_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'complete':result['complete'],'pages':result['pages'],'equal_pages':result['equal_pages'],
                  'already_incorporated_explanatory_records':len(explanatory_records),
                  'unmatched_records':unmatched_records,'adjudication_issues':adjudication_issues,
                  'exception_keys':[r['key'] for r in result['exceptions']]}))
if not result['complete']:raise SystemExit(1)

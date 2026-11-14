"""Per-page, human/model-authored visual audit records; no automatic attestations."""
import csv, json
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'source'

def now(): return datetime.now(timezone.utc).isoformat(timespec='seconds')

def source_path(key):
    group='ega_v_cote25' if key.startswith('ega25') else 'ega_v_cote24_blass'
    return SOURCE/'transcription'/group/'pages'/(key+'.tex')

def begin(key):
    p=ROOT/'review_work'/(key+'.started')
    if not p.exists(): p.write_text(now())
    return p.read_text().strip()

def save(key, checked_text, decisions, lines_read, visual_notes, all_lines_read=True):
    if not all_lines_read: raise ValueError('Incomplete pages must stay in review_work')
    if not (ROOT/'review_work'/(key+'.started')).exists(): raise ValueError('Call begin before inspecting')
    cote='25' if key.startswith('ega25') else '24'
    site=int(key.rsplit('_',1)[1])
    content_lines=sum(bool(x.strip()) and not x.lstrip().startswith(('%',r'\scanpage')) for x in checked_text.splitlines())
    record=dict(key=key,cote=cote,site=site,start_time=begin(key),end_time=now(),lines_read=content_lines,lines_read_unit='nonblank checked source lines excluding comments and scan markers',all_lines_read=True,visual_notes=visual_notes,decisions=[])
    for i,d in enumerate(decisions,1):
        required={'line','before','image','decision','reason'}
        if not required<=d.keys(): raise ValueError(required-d.keys())
        record['decisions'].append(dict(id=f'{key}-D{i:04}',**d))
    (ROOT/'checked_pages'/(key+'.tex')).write_text(checked_text)
    (ROOT/'review_work'/(key+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    return record

def aggregate():
    records=[]
    for p in (ROOT/'review_work').glob('*.json'):
        o=json.loads(p.read_text())
        if 'all_lines_read' in o: records.append(o)
    records.sort(key=lambda o:(0 if o['cote']=='25' else 1,o['site']))
    with (ROOT/'PAGES_CHECKED.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['key','start_time','end_time','lines_read','number_of_decisions','visual_notes'])
        for r in records: w.writerow([r['key'],r['start_time'],r['end_time'],r['lines_read'],len(r['decisions']),r['visual_notes']])
    with (ROOT/'CHECK_DECISIONS.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['id','key','cote','site','line','transcription_reading','image_reading','decision','reason','category'])
        for r in records:
            for d in r['decisions']: w.writerow([d['id'],r['key'],r['cote'],r['site'],d['line'],d['before'],d['image'],d['decision'],d['reason'],d.get('category','')])
    return len(records)

if __name__=='__main__': print(aggregate())

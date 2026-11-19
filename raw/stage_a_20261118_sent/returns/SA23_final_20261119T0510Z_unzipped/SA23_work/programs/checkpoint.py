#!/usr/bin/env python3
"""Immutable checkpoint; original attachments, source caches and older ZIPs excluded."""
import sys,pathlib,datetime,json,hashlib,zipfile,re
W=pathlib.Path(__file__).resolve().parents[1];n=int(sys.argv[1]);dest=W.parent/f'SA23_checkpoint_{n:02}.zip'
assert not dest.exists(),'An earlier checkpoint must never be overwritten.'
now=datetime.datetime.now(datetime.timezone.utc)
start=datetime.datetime(2026,11,19,1,14,45,tzinfo=datetime.timezone.utc)
due=start+datetime.timedelta(minutes=45*n)
assert now>=due,(now.isoformat(),due.isoformat())
with(W/'progress.log').open('a')as f:f.write(now.strftime('%Y-%m-%dT%H:%M:%SZ')+f' CHECKPOINT {n:02} Scheduled45-minute snapshot; full current deliverables and work documentation.\n')
members=[]
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=6)as z:
    for p in sorted(W.rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(W)
        if 'external'in rel.parts or'__pycache__'in rel.parts or p.suffix.lower()=='.zip':continue
        if re.fullmatch(r'search_\d+\.json',p.name):continue
        data=p.read_bytes();name='SA23_work/'+str(rel);z.writestr(name,data)
        members.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    manifest={'checkpoint':n,'created_utc':now.isoformat(),'due_utc':due.isoformat(),'previous_checkpoints_required':[],'attachments_required':['SA23_notes.zip','SA23_texts.zip','PROMPT(3).md','README(2).md'],'excluded':'Original attachments and extracted sources; third-party full publication caches/raw excerpts; prior checkpointZIPs. All authoring code, concise retrieval metadata and completed outputs retained.','files':members}
    z.writestr('CHECKPOINT_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'members':len(members),'created_utc':now.isoformat()},ensure_ascii=False))

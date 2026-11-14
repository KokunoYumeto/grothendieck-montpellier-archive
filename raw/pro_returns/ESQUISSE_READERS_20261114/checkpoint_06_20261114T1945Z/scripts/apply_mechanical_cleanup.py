#!/usr/bin/env python3
"""Apply logged syntax-only repairs after the page's scan review is finalized.

Run after the last audit_apply operation and before build_edition. A future scan
revision can reconstruct a page from its review; rerun this idempotent cleanup
command afterwards. No substantive reading is inferred or corrected here.
"""
import argparse,csv,fcntl,io,json,os,pathlib,tempfile
from edition_core import clean_latex,sha256
from build_edition import get_metadata,load_json,read_tsv,write_tsv

def atomic_text(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile('w',encoding='utf-8',dir=path.parent,prefix='.'+path.name+'.',delete=False) as f:
        f.write(text);temporary=pathlib.Path(f.name)
    os.replace(temporary,path)

def atomic_tsv(path,rows,fields):
    data=io.StringIO(newline='');w=csv.DictWriter(data,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
    atomic_text(path,data.getvalue())

def apply(root):
    # This is the same lock used by audit_apply.py. Read-modify-write of the
    # shared decision table and checked-page hashes must form one transaction.
    with (root/'.audit-records.lock').open('a') as lock:
        fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
        return apply_locked(root)

def apply_locked(root):
    metadata=get_metadata(root);prior=load_json(root/'MECHANICAL_CLEANUP.json',[]);rows=read_tsv(root/'CHECK_DECISIONS.tsv');byid={r['decision_id']:r for r in rows}
    changes=[];replay=load_json(root/'records/MECHANICAL_PATCHES.json',[])
    for page in sorted((root/'checked_pages').glob('*.tex')):
        key=page.stem;statuspath=root/'reviews'/(key+'_status.json');status=load_json(statuspath,{})
        if not status.get('finalized'):raise ValueError('Page lacks finalized scan review: '+key)
        before=page.read_text();after,events=clean_latex(before)
        if not events:continue
        m=metadata[key]
        for n,event in enumerate(events,1):
            ident=f'SYNTAX-{key}-{n:03d}'
            record={'key':key,**event,'source_id':ident,'status':'integrated in checked page','before_sha256':sha256(before),'after_sha256':sha256(after)}
            if not any(r.get('source_id')==ident and r.get('before')==record['before'] and r.get('after')==record['after'] for r in prior):prior.append(record)
            byid[ident]={'decision_id':ident,'source_item_id':ident,'key':key,'cote':m['cote'],'site':m['site'],'line':event['line'],'transcription_reading':event['before'],'image_reading':event['after'],'decision':'mechanical LaTeX repair; printed reading unchanged','reason':event['reason'],'images':f'scans/{key}_a.jpg scans/{key}_b.jpg'}
        entry={'key':key,'before_sha256':sha256(before),'after_sha256':sha256(after),'patches':[{'old':e['before'],'new':e['after'],'occurrence':1,'reason':e['reason']} for e in events],'source_ids':[f'SYNTAX-{key}-{n:03d}' for n in range(1,len(events)+1)]}
        if not any(e['key']==key and e['before_sha256']==entry['before_sha256'] and e['after_sha256']==entry['after_sha256'] for e in replay):replay.append(entry)
        # Preserve the scan-review hash before the syntax-only source rewrite.
        history=root/'reviews/history';history.mkdir(exist_ok=True)
        h=history/(key+'_status_before_mechanical_'+sha256(before)[:12]+'.json')
        if not h.exists():atomic_text(h,json.dumps(status,ensure_ascii=False,indent=2)+'\n')
        atomic_text(page,after);status['checked_sha256']=sha256(after);status['mechanical_cleanup_ids']=[f'SYNTAX-{key}-{n:03d}' for n in range(1,len(events)+1)];atomic_text(statuspath,json.dumps(status,ensure_ascii=False,indent=2)+'\n')
        changes.append({'key':key,'operations':len(events)})
    fields=['decision_id','source_item_id','key','cote','site','line','transcription_reading','image_reading','decision','reason','images']
    if changes:
        atomic_tsv(root/'CHECK_DECISIONS.tsv',list(byid.values()),fields)
        atomic_text(root/'MECHANICAL_CLEANUP.json',json.dumps(prior,ensure_ascii=False,indent=2)+'\n')
        atomic_text(root/'records/MECHANICAL_PATCHES.json',json.dumps(replay,ensure_ascii=False,indent=2)+'\n')
    return changes

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a=p.parse_args();print(json.dumps(apply(a.root),ensure_ascii=False,indent=2))

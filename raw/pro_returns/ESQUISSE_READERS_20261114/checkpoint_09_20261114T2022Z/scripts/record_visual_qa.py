#!/usr/bin/env python3
"""Append actual visual observations safely, against the exact inspected PDF.

Input JSON is a list of {reader,pdf_sha256,pdf_page,observation,phase} records.
Only run after opening and inspecting the corresponding rendered pages.
"""
import argparse,csv,fcntl,hashlib,io,json,os,pathlib,tempfile
from build_edition import read_tsv

FIELDS=['reader','pdf_sha256','phase','pdf_page','observation','status']

def record(root,items):
    with (root/'.visual-qa.lock').open('a') as lock:
        fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
        rows=read_tsv(root/'VISUAL_QA.tsv')
        for item in items:
            reader=item['reader'];paths=list(root.glob('*/'+reader+'.pdf'))
            if len(paths)!=1:raise ValueError('Exactly one PDF is required for '+reader)
            digest=hashlib.sha256(paths[0].read_bytes()).hexdigest()
            if digest!=item['pdf_sha256']:raise ValueError('The PDF changed since inspection: '+reader)
            if not str(item.get('observation','')).strip():raise ValueError('Each page needs its actual visual observation')
            row={**item,'pdf_page':str(int(item['pdf_page'])),'status':'visually inspected'}
            if row not in rows:rows.append(row)
        data=io.StringIO(newline='');writer=csv.DictWriter(data,fieldnames=FIELDS,delimiter='\t');writer.writeheader();writer.writerows(rows)
        with tempfile.NamedTemporaryFile('w',dir=root,prefix='.visual-qa-',delete=False) as out:out.write(data.getvalue());temporary=out.name
        os.replace(temporary,root/'VISUAL_QA.tsv')
    return len(items)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('observations',type=pathlib.Path);p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a=p.parse_args()
    print(json.dumps({'observations_recorded':record(a.root,json.loads(a.observations.read_text()))}))

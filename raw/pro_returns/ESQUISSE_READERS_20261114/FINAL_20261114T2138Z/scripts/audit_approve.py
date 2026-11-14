#!/usr/bin/env python3
"""Record an explicitly authorized editorial candidate in the master inputs."""
from pathlib import Path
import argparse,json,os,tempfile
from audit_inventory import read_tsv

def approve(candidate_ids, *, approval, english_variant_needed=False):
    if not approval.strip():raise ValueError('The explicit approval basis is required')
    edition=Path(__file__).resolve().parent.parent
    rows={r['candidate_id']:r for r in read_tsv(edition/'records/EDITORIAL_CANDIDATES.tsv')}
    path=edition/'editorial_variants.json'
    variants=json.loads(path.read_text()) if path.exists() else []
    results=[]
    for cid in candidate_ids:
        if cid not in rows:raise ValueError(f'{cid}: candidate is absent; its source/evidence may not yet be checked')
        r=rows[cid]
        existing=next((v for v in variants if (v['key'],v['old'],v['new'])==(r['key'],r['page_reading'],r['proposed_reading'])),None)
        if existing:results.append(existing['id']);continue
        serial=1
        while any(v['id']==f"V-FR-{int(r['site']):03d}-{serial:03d}" for v in variants):serial+=1
        vid=f"V-FR-{int(r['site']):03d}-{serial:03d}"
        source_ids=[f"L-{r['key']}-{int(r['line']):03d}"]
        source_ids.extend(x for x in r.get('difference_ids','').split(';') if x)
        if r['evidence_key'] and r['evidence_line']:
            evidence_id=f"L-{r['evidence_key']}-{int(r['evidence_line']):03d}"
            if evidence_id not in source_ids:source_ids.append(evidence_id)
        variants.append({'id':vid,'key':r['key'],'line':int(r['line']),'old':r['page_reading'],'new':r['proposed_reading'],
            'kind':r['kind'],'reason_fr':r['reason_fr'],'reason_en':r['reason_en'].replace('The proposed correction','The correction'),
            'source_ids':source_ids,
            'evidence_key':r['evidence_key'],'evidence_line':int(r['evidence_line']) if r['evidence_line'] else '',
            'evidence_reading':r['evidence_reading'],'approval':approval,'english_variant_needed':english_variant_needed})
        results.append(vid)
    with tempfile.NamedTemporaryFile('w',encoding='utf-8',dir=path.parent,prefix='.editorial-',suffix='.json',delete=False) as f:
        f.write(json.dumps(variants,ensure_ascii=False,indent=2)+'\n')
        tmp=f.name
    os.replace(tmp,path)
    print(json.dumps({'approved_variants':results,'checked_pages_changed':0}))
    return results

def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate_ids',nargs='+');ap.add_argument('--approval',required=True);ap.add_argument('--english-variant',action='store_true');a=ap.parse_args()
    approve(a.candidate_ids,approval=a.approval,english_variant_needed=a.english_variant)

if __name__=='__main__':main()

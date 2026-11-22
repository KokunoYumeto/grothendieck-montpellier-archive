#!/usr/bin/env python3
"""Recover selected source bytes from the intake-pinned mirror.

Compare with intake hashes of original-author archive members when available.
Retrieval is not proof checking or Lean execution.
"""
import argparse, concurrent.futures, csv, datetime, hashlib, json
from pathlib import Path
import urllib.request, urllib.parse

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'work/research/alpoge_source'
COMMIT='7cbf7a0c32fca1badf05931879a37c3f8a2b03b4'
MANIFEST=BASE/'sources/RETURN_DP_MULT_checkpoint_06_20261121T0420Z/AUTHOR_SOURCE_MANIFEST.tsv'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('paths',nargs='*')
    ap.add_argument('--core',action='store_true')
    args=ap.parse_args()
    refs={r['path']:r for r in csv.DictReader(MANIFEST.open(),delimiter='\t')}
    paths=set(args.paths)
    if args.core:
        roots=('Formalism/LocalRingCardinality/','Formalism/SharpRestriction/',
               'Formalism/LocalToGlobal/','Formalism/PeriodIntegrals/',
               'Formalism/ThetaLiftIndependence/')
        paths.update(p for p in refs if p.startswith(roots))
    OUT.mkdir(parents=True,exist_ok=True)
    def get(path):
        target=OUT/path
        if not target.resolve().is_relative_to(OUT.resolve()):raise ValueError(path)
        url='https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/'+COMMIT+'/src/'+urllib.parse.quote(path)
        try:
            if target.exists():data=target.read_bytes();status='cached'
            else:
                with urllib.request.urlopen(url,timeout=45) as response:data=response.read()
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(data);status='retrieved'
            digest=hashlib.sha256(data).hexdigest()
            expected=refs.get(path,{}).get('sha256')
            return {'path':path,'bytes':len(data),'sha256':digest,'intake_author_sha256':expected,
                    'matches_intake_author_hash':digest==expected if expected else None,
                    'url':url,'status':status,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        except Exception as error:return {'path':path,'url':url,'status':'failed','error':str(error)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        rows=list(pool.map(get,sorted(paths)))
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    dest=OUT.parent/('source_recovery_'+stamp+'.json')
    dest.write_text(json.dumps({'mirror_commit':COMMIT,'scope':'byte retrieval, not proof review','records':rows},indent=2)+'\n')
    bad=[r for r in rows if r['status']=='failed' or r.get('matches_intake_author_hash') is False]
    print(json.dumps({'manifest':str(dest),'requested':len(rows),'bytes':sum(r.get('bytes',0) for r in rows),'issues':bad},indent=2))
    return bool(bad)

if __name__=='__main__':raise SystemExit(main())

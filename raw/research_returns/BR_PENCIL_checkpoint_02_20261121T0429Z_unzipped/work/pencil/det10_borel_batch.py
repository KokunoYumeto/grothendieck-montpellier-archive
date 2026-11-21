#!/usr/bin/env python3
from pathlib import Path
import argparse,json,time
from determinant_borel_extensions import search

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root'

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--support',type=int,required=True);args=pa.parse_args()
    source=json.loads((ROOT/'borel_7_12.json').read_text())['results']
    records=next(r['records'] for r in source if r['j']==10);reps={}
    for r in records:
        S=tuple(r['subset']);tr=tuple(sorted(q%6*6+q//6 for q in S));key=min(S,tr)
        if key not in reps:reps[key]={'bound':r['lower_bound'],'support':len(r['support'])}
        else:reps[key]['bound']=max(reps[key]['bound'],r['lower_bound'])
    results=[]
    for S,r in sorted(reps.items()):
        if r['bound']>=18 or r['support']!=args.support:continue
        result=search(list(S));results.append(result)
        path=HERE/('det10_borel_support'+str(args.support)+'.json')
        path.write_text(json.dumps(results,indent=2,default=str)+'\n')
        print('CASE COMPLETE',S,'excluded',result['excluded'],'continuous',len(result['continuous_branches']),'rigid_remaining',len(result['rigid_survivors']),flush=True)
    print('BATCH COMPLETE support',args.support,'cases',len(results),'proved',sum(r['excluded'] for r in results),flush=True)

if __name__=='__main__':main()

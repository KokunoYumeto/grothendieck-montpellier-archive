#!/usr/bin/env python3
from pathlib import Path
import argparse,json,time
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
from sympy import Rational
from determinant_borel_module import make
from determinant_borel_extensions import ambient_basis
from bigraded_prolongation import hilbert

HERE=Path(__file__).resolve().parent

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--support',type=int,required=True);args=pa.parse_args()
    source=json.loads((HERE.parent/'pencil'/f'det10_borel_support{args.support}.json').read_text());out=[];start=time.time()
    for rec in source:
        S=rec['subset'];M=make(S);results=[]
        for i,sp in enumerate(rec['rigid_survivors']):
            F=[() for _ in M['blocks']]
            for block in sp:F[block['block']]=tuple(tuple(Rational(x) for x in row) for row in block['basis'])
            E=ambient_basis(M,F);certs=[]
            for p,q in [(2,2),(2,3),(3,2),(3,3)]:
                h=hilbert(E,p,q);h={k:v for k,v in h.items() if k not in ['matrix','monomials']};certs.append(h)
                print(S,'candidate',i,'degree',p,q,'hilbert_upper',h['hilbert_upper_bound'],'cols',h['remaining_monomials'],'seconds',round(time.time()-start,2),flush=True)
                if h['hilbert_upper_bound']<17:break
            results.append({'space':sp,'certificates':certs,'excluded':min(h['hilbert_upper_bound'] for h in certs)<17})
        out.append({'subset':S,'rigid_results':results,'continuous_branch_count':len(rec['continuous_branches'])})
        (HERE/f'det10_higher_support{args.support}.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE support',args.support,flush=True)

if __name__=='__main__':main()

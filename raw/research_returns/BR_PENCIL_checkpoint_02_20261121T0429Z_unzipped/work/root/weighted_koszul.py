"""Support-factor Koszul maps block-diagonalized by row/column torus weights.

A research search: nonzero modular minors certify characteristic-zero lower
bounds. All-characteristic conclusions require additional integer checks.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json, math, time
import numpy as np
from coordinate_koszul import modular_rank, slices, RECTS

def blocks(S, sign, p):
    support, mats=slices(S,sign)
    m,j=len(support),len(S)
    weights=[32**(v//4)+32**(4+v%4) for v in support]
    aw=[sum(32**i for i in RECTS[q][0])+sum(32**(4+i) for i in RECTS[q][1]) for q in S]
    src=list(combinations(range(m),p))
    dst=list(combinations(range(m),p+1)); di={I:i for i,I in enumerate(dst)}
    sparse=[[(int(u),int(v),int(M[u,v])) for u,v in zip(*np.nonzero(M))] for M in mats]
    result=defaultdict(list)
    for ci,I in enumerate(src):
        isum=sum(weights[i] for i in I)
        for h, entries in enumerate(sparse):
            for u,v,value in entries:
                if u in I:continue
                J=tuple(sorted(I+(u,)))
                ri=di[J]
                w=isum-weights[v]
                assert w==sum(weights[x] for x in J)-aw[h]
                sg=(-1)**sum(x<u for x in I)
                result[w].append((ri*j+h,ci*m+v,sg*value))
    for w,triples in sorted(result.items()):
        rows=sorted({r for r,c,v in triples});cols=sorted({c for r,c,v in triples})
        ri={r:i for i,r in enumerate(rows)};ci={c:i for i,c in enumerate(cols)}
        mat=np.zeros((len(rows),len(cols)),dtype=np.int64)
        for r,c,v in triples:mat[ri[r],ci[c]]=v
        yield w, rows, cols, mat

def main():
    t=time.time();data=json.loads(Path(__file__).with_name('j7_target14.json').read_text())
    records=[]
    for S in data['per_unresolved']:
        support,_=slices(S,1);m=len(support)
        rec={'subset':S,'support':support,'family':'per','certificates':[]}
        for p in sorted(range(1,m-1),key=lambda p:abs(p-6*m/(m+7))):
            certificates=[];rank=0;largest=(0,0)
            for w,rows,cols,mat in blocks(S,1,p):
                cert=modular_rank(mat);rank+=cert['rank_mod_p']
                largest=max(largest,mat.shape,key=lambda x:x[0]*x[1])
                if cert['rank_mod_p']:
                    cert['weight']=w
                    cert['rows']=[rows[i] for i in cert['rows']]
                    cert['cols']=[cols[i] for i in cert['cols']]
                    certificates.append(cert)
            cost=math.comb(m-1,p);bound=(rank+cost-1)//cost
            c={'p':p,'rank_mod_p':rank,'cost':cost,'bound':bound,'largest_block':largest,'blocks':certificates}
            rec['certificates'].append(c)
            print(S,'m',m,'p',p,'rank',rank,'cost',cost,'bound',bound,'blocks',len(certificates),'largest',largest,flush=True)
            if bound>=14:break
        records.append(rec)
        Path(__file__).with_name('j7_per_support_koszul.json').write_text(json.dumps({'records':records,'seconds':time.time()-t},indent=2)+'\n')
    print('DONE',time.time()-t,flush=True)
if __name__=='__main__':main()

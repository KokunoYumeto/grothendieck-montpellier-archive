"""Exact modular search on the eight extra uniform-n seven-plane gates."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json,math,time
import numpy as np
from coordinate_koszul import modular_rank
from uniform7_graphs import tensor

HERE=Path(__file__).resolve().parent

def blocks(selected,r,c,sign,p):
    support,mats=tensor(selected,r,c,sign);m=len(support);j=len(mats)
    weights=[32**(v//c)+32**(r+v%c) for v in support]
    aw=[sum(32**i for i in I)+sum(32**(r+i) for i in J) for I,J in selected]
    src=list(combinations(range(m),p));dst=list(combinations(range(m),p+1));di={I:i for i,I in enumerate(dst)}
    sparse=[[(int(u),int(v),int(M[u,v])) for u,v in zip(*np.nonzero(M))] for M in mats]
    groups=defaultdict(list)
    for ci,I in enumerate(src):
        iw=sum(weights[i] for i in I)
        for h,entries in enumerate(sparse):
            for u,v,value in entries:
                if u in I:continue
                J=tuple(sorted(I+(u,)));w=iw-weights[v]
                assert w==sum(weights[x] for x in J)-aw[h]
                groups[w].append((di[J]*j+h,ci*m+v,(-1)**sum(x<u for x in I)*value))
    for w,triples in sorted(groups.items()):
        rows=sorted({q[0] for q in triples});cols=sorted({q[1] for q in triples});ri={x:i for i,x in enumerate(rows)};ci={x:i for i,x in enumerate(cols)}
        M=np.zeros((len(rows),len(cols)),dtype=np.int64)
        for row,col,value in triples:M[ri[row],ci[col]]=value
        yield w,rows,cols,M

def main():
    data=json.loads((HERE/'uniform7_exploration.json').read_text());out=[];start=time.time()
    for gi,G in enumerate(data['graphs']):
      for qi,rec in enumerate(G['subset_orbits']):
        for family,sign in [('det',-1),('per',1)]:
            if rec['families'][family]['bound']>=14:continue
            record={'graph':gi,'subset_index':qi,'rectangles':rec['rectangles'],'r':G['r'],'c':G['c'],'family':family,'certificates':[]}
            for p in [1,4,3,5,2,6]:
                rank=0;certs=[]
                for w,rows,cols,M in blocks(rec['rectangles'],G['r'],G['c'],sign,p):
                    cert=modular_rank(M);rank+=cert['rank_mod_p']
                    if cert['rank_mod_p']:
                        cert['weight']=w;cert['rows']=[rows[i] for i in cert['rows']];cert['cols']=[cols[i] for i in cert['cols']];certs.append(cert)
                cost=math.comb(G['edges']-1,p);bound=(rank+cost-1)//cost
                record['certificates'].append({'p':p,'rank':rank,'cost':cost,'bound':bound,'blocks':certs})
                print(gi,qi,family,'p',p,'rank',rank,'cost',cost,'bound',bound,flush=True)
                if bound>=14:break
            out.append(record)
            (HERE/'uniform7_support_koszul.json').write_text(json.dumps({'records':out,'seconds':time.time()-start},separators=(',',':'))+'\n')
    print('DONE',time.time()-start,flush=True)

if __name__=='__main__':main()

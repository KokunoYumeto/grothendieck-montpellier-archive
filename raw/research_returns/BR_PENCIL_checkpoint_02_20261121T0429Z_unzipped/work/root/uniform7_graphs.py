"""Explore every support graph outside4x4 with seven rectangles and <=13edges.

No result is asserted until the cover and rank certificates are independently
verified.  Every row/column has degree>=2 because it lies in a rectangle.
"""
from itertools import combinations,permutations,product
from collections import Counter,defaultdict
from pathlib import Path
import json,time,math
import numpy as np
from coordinate_koszul import koszul,modular_rank

HERE=Path(__file__).resolve().parent

def rectangles(rows,c):
    return [(I,J) for I in combinations(range(len(rows)),2)
            for J in combinations(range(c),2)
            if all(rows[r]>>j&1 for r in I for j in J)]

def row_sequences(r,c):
    allowed=sorted((m for m in range(1<<c) if 2<=m.bit_count()<=13-2*(r-1)))
    def go(seq,start,edges):
        if len(seq)==r:
            yield tuple(seq);return
        left=r-len(seq)-1
        for i in range(start,len(allowed)):
            m=allowed[i]
            if edges+m.bit_count()+2*left>13:continue
            yield from go(seq+[m],i,edges+m.bit_count())
    yield from go([],0,0)

def permute_mask(mask,p):
    return sum(1<<p[j] for j in range(len(p)) if mask>>j&1)

def graph_cover():
    records=[];stats=[]
    for r in [5,6]:
      for c in range(2,r+1):
        seen=set();count=0;qualified=0;cp=list(permutations(range(c)))
        for rows in row_sequences(r,c):
            count+=1
            if any(sum(m>>j&1 for m in rows)<2 for j in range(c)):continue
            rects=rectangles(rows,c)
            if len(rects)<7:continue
            covered={(i,j) for I,J in rects for i in I for j in J}
            if len(covered)!=sum(m.bit_count() for m in rows):continue
            qualified+=1
            canonical=min(tuple(sorted(permute_mask(m,p) for m in rows)) for p in cp)
            if canonical in seen:continue
            seen.add(canonical)
            records.append({'rows':list(canonical),'r':r,'c':c,'edges':sum(m.bit_count() for m in rows)})
        stats.append({'r':r,'c':c,'row_multisets':count,'qualified_before_column_orbits':qualified,'graph_orbits':len(seen)})
        print(stats[-1],flush=True)
    return records,stats

def automorphisms(rows,c,rects):
    index={x:i for i,x in enumerate(rects)};answer=[]
    target=defaultdict(list)
    for i,m in enumerate(rows):target[m].append(i)
    for p in permutations(range(c)):
        transformed=[permute_mask(m,p) for m in rows]
        if sorted(transformed)!=sorted(rows):continue
        sources=defaultdict(list)
        for i,m in enumerate(transformed):sources[m].append(i)
        masks=sorted(target)
        for choices in product(*(list(permutations(target[m])) for m in masks)):
            rho={i:j for m,choice in zip(masks,choices) for i,j in zip(sources[m],choice)}
            action=[index[(tuple(sorted(rho[i] for i in I)),tuple(sorted(p[j] for j in J)))] for I,J in rects]
            answer.append(action)
    # A graph automorphism may act trivially on its rectangles (for example,
    # swapping the two columns of K_(r,2)); only the induced actions matter.
    return sorted({tuple(g) for g in answer})

def tensor(selected,r,c,sign):
    support=sorted({c*i+j for I,J in selected for i in I for j in J});ix={v:i for i,v in enumerate(support)};m=len(support)
    mats=[]
    for (i,j),(a,b) in selected:
        u,v,w,z=[ix[q] for q in [c*i+a,c*i+b,c*j+a,c*j+b]]
        M=np.zeros((m,m),dtype=np.int64);M[u,z]=M[z,u]=1;M[v,w]=M[w,v]=sign;mats.append(M)
    return support,mats

def main():
    start=time.time();graphs,stats=graph_cover();out=[]
    for gi,G in enumerate(graphs):
        rows=G['rows'];r=G['r'];c=G['c'];rects=rectangles(rows,c);actions=automorphisms(rows,c,rects)
        seen=set();reps=[];total=0
        edge_masks=[sum(1<<(c*i+j) for i in I for j in J) for I,J in rects]
        support_mask=sum(1<<(c*i+j) for i,m in enumerate(rows) for j in range(c) if m>>j&1)
        for S in combinations(range(len(rects)),7):
            mask=sum(1<<q for q in S)
            if mask in seen:continue
            union=0
            for q in S:union|=edge_masks[q]
            if union!=support_mask:continue
            orbit={sum(1<<g[q] for q in S) for g in actions};seen.update(orbit);total+=len(orbit)
            selected=[rects[q] for q in S];rec={'subset':S,'rectangles':selected,'orbit_size':len(orbit),'families':{}}
            for fam,sign in [('det',-1),('per',1)]:
                support,mats=tensor(selected,r,c,sign);certs=[];bound=len(support)
                for p in [1,2,3]:
                    A=koszul(mats,p);cert=modular_rank(A);cost=math.comb(6,p)
                    cert.update(p=p,pure_cost=cost,bound=(cert['rank_mod_p']+cost-1)//cost)
                    certs.append(cert);bound=max(bound,cert['bound'])
                    if bound>=14:break
                rec['families'][fam]={'bound':bound,'certificates':certs}
            reps.append(rec)
        G.update(rectangles=rects,automorphisms=len(actions),subset_orbits=reps,all_support_exact_subsets=total)
        out.append(G)
        print('graph',gi+1,'of',len(graphs),'shape',r,c,'edges',G['edges'],'orbits',len(reps),'min', {f:min((q['families'][f]['bound'] for q in reps),default=0) for f in ['det','per']},'elapsed',time.time()-start,flush=True)
        (HERE/'uniform7_exploration.json').write_text(json.dumps({'status':'EXPLORATION','stats':stats,'graphs':out,'seconds':time.time()-start},separators=(',',':'))+'\n')
    print('DONE',len(graphs),'graphs',sum(len(g['subset_orbits']) for g in out),'subsetorbits',flush=True)

if __name__=='__main__':main()

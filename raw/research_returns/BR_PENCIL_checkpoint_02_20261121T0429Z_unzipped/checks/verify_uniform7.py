"""Independent uniform-n seven-plane cover and exact modular minor check.

No search/generation module is imported. The only shared helper provides
already audited modular determinants and direct Koszul-entry formulas.
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
import json,math,time
from verify_det7_global import detmod,koszul_minor

HERE=Path(__file__).resolve().parent

def rectangles(rows,c):
    return [(I,J) for I in combinations(range(len(rows)),2) for J in combinations(range(c),2)
            if all(rows[i]>>j&1 for i in I for j in J)]

def move_mask(m,p):return sum(1<<p[j] for j in range(len(p)) if m>>j&1)

def enumerate_graphs():
    result=set()
    for r in [5,6]:
      for c in range(2,r+1):
        masks=[m for m in range(1<<c) if 2<=m.bit_count()<=13-2*(r-1)]
        ps=list(permutations(range(c)))
        for rows in combinations_with_replacement(masks,r):
            edges=sum(m.bit_count() for m in rows)
            if edges>13 or any(sum(m>>j&1 for m in rows)<2 for j in range(c)):continue
            rs=rectangles(rows,c)
            if len(rs)<7:continue
            if len({(i,j) for I,J in rs for i in I for j in J})!=edges:continue
            canonical=min(tuple(sorted(move_mask(m,p) for m in rows)) for p in ps)
            result.add((r,c,canonical))
    return result

def actions(rows,c,rects):
    # Independently enumerate every vertex permutation preserving this graph.
    index={q:i for i,q in enumerate(rects)};result=set();row_perms=list(permutations(range(len(rows))))
    for gamma in permutations(range(c)):
        moved=[move_mask(m,gamma) for m in rows]
        for rho in row_perms:
            if not all(rows[rho[i]]==moved[i] for i in range(len(rows))):continue
            result.add(tuple(index[(tuple(sorted(rho[i] for i in I)),tuple(sorted(gamma[j] for j in J)))] for I,J in rects))
    return result

def tensor(selected,c,sign):
    support=sorted({c*i+j for I,J in selected for i in I for j in J});ix={v:i for i,v in enumerate(support)};T={}
    for h,((i,j),(a,b)) in enumerate(selected):
        u,v,w,z=[ix[q] for q in [c*i+a,c*i+b,c*j+a,c*j+b]]
        for x,y,coef in [(u,z,1),(z,u,1),(v,w,sign),(w,v,sign)]:T[h,x,y]=coef
    return support,T

def check_minor(S,support,T,typ,p,rec,prime):
    m=len(support);d=7 if typ=='A' else m
    n=rec['order'];rows=rec['rows'];cols=rec['cols']
    nr=math.comb(d,p+1)*(m if typ=='A' else 7);nc=math.comb(d,p)*m
    assert len(rows)==len(cols)==len(set(rows))==len(set(cols))==n
    assert all(0<=x<nr for x in rows) and all(0<=x<nc for x in cols)
    assert detmod(koszul_minor(S,support,T,typ,p,rows,cols),prime)==rec['determinant_mod_p']!=0

def main():
    start=time.time();data=json.loads((HERE/'uniform7_certificate.json').read_text());prime=data['prime']
    assert prime==1000003 and all(prime%d for d in range(2,math.isqrt(prime)+1))
    actual=enumerate_graphs();listed={(g['r'],g['c'],tuple(g['rows'])) for g in data['graphs']}
    assert len(actual)==len(listed)==len(data['graphs'])==data['graph_count']==34 and actual==listed
    totals=Counter();minors=0;orbits=0
    for gi,G in enumerate(data['graphs']):
        r,c,rows=G['r'],G['c'],G['rows'];rects=rectangles(rows,c)
        assert [[list(I),list(J)] for I,J in rects]==G['rectangles']
        assert sum(m.bit_count() for m in rows)==G['edges']<=13
        group=actions(rows,c,rects);covered=set()
        support_mask=sum(1<<(c*i+j) for i,m in enumerate(rows) for j in range(c) if m>>j&1)
        rect_masks=[sum(1<<(c*i+j) for i in I for j in J) for I,J in rects]
        for rec in G['records']:
            S=rec['subset'];assert len(S)==7 and sorted(set(S))==S
            selected=[rects[q] for q in S]
            assert [[list(I),list(J)] for I,J in selected]==rec['rectangles']
            union=0
            for q in S:union|=rect_masks[q]
            assert union==support_mask
            orbit={sum(1<<g[q] for q in S) for g in group}
            assert len(orbit)==rec['orbit_size'] and not covered.intersection(orbit);covered.update(orbit);orbits+=1
            for fam,sign in [('det',-1),('per',1)]:
                cert=rec['families'][fam];support,T=tensor(selected,c,sign);m=len(support);typ=cert['type'];p=cert['p']
                cost=math.comb(6 if typ=='A' else m-1,p);assert cost==cert['cost'];totals[fam+'_'+typ]+=1
                if typ=='A':
                    assert cert['order']>13*cost;check_minor(S,support,T,typ,p,cert,prime);minors+=1;continue
                assert typ=='B'
                src=list(combinations(range(m),p));dst=list(combinations(range(m),p+1))
                vw=[32**(v//c)+32**(r+v%c) for v in support]
                aw=[sum(32**i for i in I)+sum(32**(r+j) for j in J) for I,J in selected]
                assert all(vw[u]+vw[v]==aw[h] for h,u,v in T)
                seen_weights=set();seen_rows=set();seen_cols=set();rank=0
                for block in cert['blocks']:
                    w=block['weight'];rs=block['rows'];cs=block['cols']
                    assert w not in seen_weights and not seen_rows.intersection(rs) and not seen_cols.intersection(cs)
                    assert all(sum(vw[u] for u in dst[q//7])-aw[q%7]==w for q in rs)
                    assert all(sum(vw[u] for u in src[q//m])-vw[q%m]==w for q in cs)
                    check_minor(S,support,T,typ,p,block,prime);minors+=1;rank+=block['order']
                    seen_weights.add(w);seen_rows.update(rs);seen_cols.update(cs)
                assert rank==cert['rank']>13*cost
        count=0
        for S in combinations(range(len(rects)),7):
            union=0
            for q in S:union|=rect_masks[q]
            if union==support_mask:
                assert sum(1<<q for q in S) in covered;count+=1
        assert count==len(covered)==G['all_support_exact_subsets'];totals['support_exact_subsets']+=count
        print('verified graph',gi+1,'of34',flush=True)
    assert orbits==data['subset_orbits']==1027
    result={'status':'PASS','finding':'R-11','graph_count':34,'subset_orbits':orbits,'counts':dict(totals),'nonzero_modular_minors':minors,'seconds':time.time()-start,'scope':'All new support graphs and subsets outside4x4; n4 dependencies R-08/R-10 checked separately.'}
    (HERE/'uniform7_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()

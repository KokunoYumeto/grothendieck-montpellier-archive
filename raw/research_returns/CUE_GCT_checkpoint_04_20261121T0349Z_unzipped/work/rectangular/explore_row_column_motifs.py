"""Exploration only: simultaneous row and column local identities."""
import json
from pathlib import Path
from check_simultaneous_chords import field_for, product_coefficients, rank_columns


def tensor_column(ai, bi, roots, p, m, k):
    aa = product_coefficients([i % m for i in ai], roots, p)
    bb = product_coefficients([i % m for i in bi], roots, p)
    assert len(aa) == m - k + 1 and len(bb) == k + 1
    return aa, bb


results=[]
for m in [10,12,14,16]:
    p,zeta=field_for(m)
    roots=[pow(zeta,i,p) for i in range(m)]
    for rr in [0,1,-1,2]:
        failures=[]; passed=0
        for k in range(5,m-4):
            aa=product_coefficients(range(k,m),roots,p)
            bb=product_coefficients(range(k-1),roots,p)
            uv=[]
            uv.append(tensor_column([1]+list(range(k+1,m)),[0,2]+list(range(2,k)),roots,p,m,k))
            uv.append(tensor_column([1,1]+list(range(k+2,m)),[2]+list(range(2,k+1)),roots,p,m,k))
            interval={i%m for i in range(-k,2)}
            uv.append(tensor_column([rr,0]+[i for i in range(m) if i not in interval],
                                    [2]+list(range(-k,-1)),roots,p,m,k))
            interval={i%m for i in range(-k+1,2)}
            uv.append(tensor_column([rr]+[i for i in range(m) if i not in interval],
                                    [0,2]+list(range(-k+1,-1)),roots,p,m,k))
            for t in range(5,m-4):
                pairs=[(r,t-r) for r in range(m-k+1) if 0<=t-r<=k]
                cols=[[aa[r]*(bb[s] if s<len(bb) else 0)%p for r,s in pairs],
                      [aa[r]*(bb[s-1] if 1<=s<=len(bb) else 0)%p for r,s in pairs]]
                cols.extend([[a[r]*b[s]%p for r,s in pairs] for a,b in uv])
                normal=rank_columns(cols,p)-rank_columns(cols[:2],p)
                if normal==4: passed+=1
                else: failures.append([k,t,normal])
        results.append({'m':m,'prime':p,'r_chord_root_index':rr,
                        'rank_four_count':passed,'failures':failures})
        print(json.dumps(results[-1]))
Path(__file__).with_name('row_column_motif_exploration.json').write_text(json.dumps(results,indent=2)+'\n')

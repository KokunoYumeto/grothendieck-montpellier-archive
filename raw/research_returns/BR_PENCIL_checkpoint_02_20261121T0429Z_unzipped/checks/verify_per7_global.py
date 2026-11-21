#!/usr/bin/env python3
"""Independent exhaustive per7 cover plus exact modular Koszul certificates.

Reuses only already independently audited verification arithmetic and
Koszul-entry definitions from verify_det7_global.py, never search code.
"""
from itertools import combinations,permutations
from collections import Counter
from pathlib import Path
import json,math
from verify_det7_global import detmod,koszul_minor,RECTS

def tensor(S):
 support=sorted({4*r+c for z in S for r in RECTS[z][0] for c in RECTS[z][1]})
 ix={v:i for i,v in enumerate(support)};T={}
 for h,z in enumerate(S):
  (r,s),(c,d)=RECTS[z]
  a,b,x,y=[ix[v] for v in [4*r+c,4*r+d,4*s+c,4*s+d]]
  for u,v in [(a,y),(y,a),(b,x),(x,b)]:T[h,u,v]=1
 return support,T

def group_actions():
 index={x:i for i,x in enumerate(RECTS)};actions=[]
 for rho in permutations(range(4)):
  for gamma in permutations(range(4)):
   g=[index[(tuple(sorted(rho[i] for i in I)),tuple(sorted(gamma[j] for j in J)))] for I,J in RECTS]
   actions.append(g);actions.append([(q%6)*6+q//6 for q in g])
 assert len({tuple(g) for g in actions})==1152
 return actions

def dependencies():
 return {tuple(S):label for label,sets in {
 'P-13':[[0,1,2,3,4,6,12],[0,1,2,3,6,7,8],[0,1,2,6,7,8,18],[0,1,2,6,7,18,20],[0,1,3,6,7,9,14]],
 'P-16':[[0,1,2,3,6,7,9],[0,1,2,3,6,7,18],[0,1,3,6,7,15,21]],
 'P-15':[[0,1,3,6,7,9,18],[0,1,3,6,7,18,21]],
 'P-19':[[0,1,2,6,7,18,19]]}.items() for S in sets}

def check_linear(rec,prime):
 S=rec['subset'];support,T=tensor(S);m=len(support);assert support==rec['support'];kind=rec['type']
 if kind=='prolongation':
  assert rec['finding']==dependencies()[tuple(S)];return 0
 p=rec['p'];cost=math.comb(6 if kind=='A_koszul' else m-1,p);assert cost==rec['cost']
 if kind=='A_koszul':
  rows,cols,n=rec['rows'],rec['cols'],rec['minor_order']
  assert len(set(rows))==len(set(cols))==n>13*cost
  assert detmod(koszul_minor(S,support,T,'A',p,rows,cols),prime)==rec['determinant_mod_p']!=0
  return 1
 assert kind=='B_koszul'
 src=list(combinations(range(m),p));dst=list(combinations(range(m),p+1))
 weights=[32**(v//4)+32**(4+v%4) for v in support]
 aw=[sum(32**i for i in RECTS[z][0])+sum(32**(4+i) for i in RECTS[z][1]) for z in S]
 assert all(weights[u]+weights[v]==aw[h] for h,u,v in T)
 seen_rows=set();seen_cols=set();seen_weights=set();total=0
 for c in rec['blocks']:
  rows,cols,n,w=c['rows'],c['cols'],c['size'],c['weight']
  assert len(set(rows))==len(set(cols))==n
  assert not(seen_rows&set(rows)) and not(seen_cols&set(cols)) and w not in seen_weights
  assert all(sum(weights[u] for u in dst[row//7])-aw[row%7]==w for row in rows)
  assert all(sum(weights[u] for u in src[col//m])-weights[col%m]==w for col in cols)
  assert detmod(koszul_minor(S,support,T,'B',p,rows,cols),prime)==c['determinant_mod_p']!=0
  seen_rows.update(rows);seen_cols.update(cols);seen_weights.add(w);total+=n
 assert total==rec['rank_lower_bound']>13*cost
 return len(rec['blocks'])

def main():
 path=Path(__file__).with_name('per7_global_certificate.json');data=json.loads(path.read_text());prime=data['prime']
 assert prime==1000003 and all(prime%d for d in range(2,math.isqrt(prime)+1))
 group=group_actions();covered=set();counts=Counter();minors=0
 for i,rec in enumerate(data['records']):
  S=rec['subset'];assert len(S)==7 and len(set(S))==7 and S==sorted(S)
  assert len(rec['support'])<14 and rec['lower_bound']>=14
  orbit={sum(1<<g[q] for q in S) for g in group}
  assert len(orbit)==rec['orbit_size'] and not(covered&orbit)
  covered.update(orbit);minors+=check_linear(rec,prime);counts[rec['type']]+=1
  if (i+1)%300==0:print('verified representatives',i+1,flush=True)
 assert len(data['records'])==data['low_support_orbits']==1517
 assert len(covered)==data['low_support_subsets']
 masks=[sum(1<<(4*r+c) for r in I for c in J) for I,J in RECTS]
 low=0;total=0
 for S in combinations(range(36),7):
  total+=1;mask=0
  for q in S:mask|=masks[q]
  if mask.bit_count()<14:
   low+=1;assert sum(1<<q for q in S) in covered
 assert total==math.comb(36,7)==data['all_coordinate_subsets'] and low==len(covered)
 out={'status':'PASS','all_coordinate_subsets':total,'all_low_support_subsets':low,'low_support_orbits':1517,'case_types':dict(counts),'exact_modular_minors_verified':minors,'prolongation_dependencies':['P-13','P-15','P-16','P-19'],'scope':'All finite coverage and Koszul entries checked here; listed prolongation proofs and certificates checked separately.'}
 path.with_name('per7_global_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

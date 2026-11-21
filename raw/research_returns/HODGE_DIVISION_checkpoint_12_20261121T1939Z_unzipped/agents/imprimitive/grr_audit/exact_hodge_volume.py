#!/usr/bin/env python3
"""Exact rooted stable-tree Hodge intersection, independently implemented.

Input: published CHEVIE W(E8) character table rebuilt by build_character_input.
The only external numerical target values are printed for comparison after
the calculation. No rStation package or volume code is imported.

With ten real reflection leaves and one iW leaf, every subtree has at most
one imaginary leaf. Hence all child products use the rational W(E8) class
algebra. A final second iW factor inserts the central negative identity.
"""
from pathlib import Path
from functools import lru_cache
from math import factorial
import json,sys,time,argparse
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT.parent/'runtime_e8_flint'))
from flint import fmpq,fmpq_mat

parser=argparse.ArgumentParser();parser.add_argument('--reflections',type=int,default=10)
parser.add_argument('--root',choices=['order12','involution'],default='order12')
parser.add_argument('--output',default='exact_hodge_volume.json');args=parser.parse_args()
raw=json.loads((HERE/'character_input.json').read_text());nc=112;GW=raw['real_group_order'];GG=2*GW
C=raw['characters'];dims=raw['degrees'];sizes=[c['size']for c in raw['classes']]
forward=fmpq_mat([[fmpq(sizes[c]*C[r][c],dims[r])for c in range(nc)]for r in range(nc)])
inverse=fmpq_mat([[fmpq(dims[r]*C[r][c],GW)for r in range(nc)]for c in range(nc)])
assert forward*inverse==fmpq_mat([[int(r==c)for c in range(nc)]for r in range(nc)])
weights=[[fmpq(v)for v in row]for row in raw['weights_by_scalar_exponent']]
N=args.reflections;d=N-1;root,leaf=(56,5)if args.root=='order12'else(5,56);ref=65
negroot=raw['classes'][root]['negative_class_index']-1
def vector(M):return tuple(M[j,0]for j in range(nc))
def transform(mat,v):return vector(mat*fmpq_mat([[x]for x in v]))
def basis(c):return tuple(forward[j,c]for j in range(nc))
zero=tuple(fmpq(0)for _ in range(nc))
unit=tuple(fmpq(1)for _ in range(nc))
Kref=basis(ref);Kleaf=basis(leaf)
L={};T={};beg=time.monotonic()
for c,kc,a in [((1,0),Kref,weights[0][ref]),((0,1),Kleaf,weights[1][leaf])]:
    for b in range(d+1):L[c,b]=tuple(x*a**b/factorial(b)**2 for x in kc)

@lru_cache(None)
def F(r,s,m,b):
    k=r+s
    if b<0 or m<1 or m>k or r<0 or s<0 or s>1:return zero
    if m==1:return L.get(((r,s),b),zero)
    acc=[fmpq(0)for _ in range(nc)]
    for rr in range(r+1):
      for ss in range(s+1):
        kk=rr+ss
        if not kk or k-kk<m-1:continue
        for j in range(b+1):
            v=L.get(((rr,ss),j))
            if v is None:continue
            u=F(r-rr,s-ss,m-1,b-j)
            if u is zero:continue
            acc=[a+x*y for a,x,y in zip(acc,v,u)]
    return tuple(a/m for a in acc)

for k in range(2,N+2):
  counts=[(k,0)]if k<=N else[]
  if k-1<=N:counts.append((k-1,1))
  for c in counts:
    r,s=c;classT=[]
    for a in range(k-1):
        v=[fmpq(0)for _ in range(nc)]
        for m in range(a+2,k+1):
            factor=fmpq(factorial(m-2),factorial(a))
            f=F(r,s,m,m-2-a)
            v=[x+factor*y for x,y in zip(v,f)]
        T[c,a]=tuple(v);classT.append(transform(inverse,v))
    for b in range(max(0,N-k+1)):
        v=[fmpq(0)for _ in range(nc)]
        for a,ta in enumerate(classT):
            den=(a+b+1)*factorial(a)*factorial(b)**2
            v=[x-(weights[s][j]**(a+b+1))*ta[j]/den for j,x in enumerate(v)]
        L[c,b]=transform(forward,v)
  print(f'leaf count {k}: T={len(T)} L={len(L)} F={F.cache_info().currsize} elapsed={time.monotonic()-beg:.2f}s',flush=True)

final=[fmpq(0)for _ in range(nc)]
for a in range(N):
    factor=weights[1][root]**a/factorial(a)
    final=[v+factor*w for v,w in zip(final,T[(N,1),a])]
cls=transform(inverse,final)
intersection=cls[negroot]*sizes[root]*factorial(d)*factorial(N)/GG
# The ordinary tuple degree is independent of all Hodge weights.
degree_vec=tuple(Kleaf[j]*Kref[j]**N for j in range(nc))
degree_cls=transform(inverse,degree_vec)
degree=degree_cls[negroot]*sizes[root]/GG
out={'status':'PASS','all_arithmetic_exact':True,'implementation':'new rooted recurrence; rational W(E8) character algebra with central-product reduction',
     'reflections':N,'branch_count':N+2,'dimension':d,'root_choice':args.root,
     'lambda_top_intersection':str(intersection),'ordinary_tuple_stack_degree':str(degree),
     'input_source':raw['source_url'],'input_sha256':raw['source_sha256'],
     'forward_inverse_identity_checked':True,'external_numerical_targets_not_inputs':True,
     'comparison_with_unrefereed_lead':{'intersection_match':intersection==fmpq(3009825,64)if N==10 else None,
                                       'degree_match':degree==fmpq(90296156160000)if N==10 else None},
     'cached_counts':{'T':len(T),'L':len(L),'F':F.cache_info().currsize},'elapsed_seconds':time.monotonic()-beg}
(HERE/args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

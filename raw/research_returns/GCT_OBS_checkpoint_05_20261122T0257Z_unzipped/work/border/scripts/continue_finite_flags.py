#!/usr/bin/env python3
"""Continue rational special points from exact projective-line rank tests."""
import argparse,json,time,math
from fractions import Fraction
from collections import Counter
import sympy as sp
from borel_quiver import ab_module,successors,extension_vectors,linear_combination
from br_linear import rowspace
from probe_gate_pencils import analyze,decode_flag
from check_det10_gate import encode_flag,encode_vector
from probe_coupled_borel import wedge_ranks
from probe_extension_koszul import koszul
from extension_projection import fixed_projection,projected_extension_rank

t=sp.Symbol('t')

def insert(M,F,i,vs,point):
 if point=='infinity':v=vs[1]
 else:
  f=sp.Poly(sp.sympify(point),t,domain=sp.QQ);assert f.degree()==1
  z=Fraction(-f.nth(0)/f.nth(1));v={j:vs[0].get(j,0)+z*vs[1].get(j,0) for j in vs[0].keys()|vs[1].keys()}
 G=list(F);G[i]=rowspace(F[i]+(tuple(v.items()),));return tuple(G)

def test(E,M):
 a=len(M['subset']);b=len(M['support']);r=17;rs=wedge_ranks(E,a,b)
 if rs['A']>r*(a-1) or rs['B']>r*(b-1):return {'test':'wedge','ranks':rs}
 for p in (2,3,4):
  for f,d in ((2,b),(1,a)):
   if len(E)*d<=r*(d-p):continue
   x=koszul(E,M,f,0,p)
   if x['lower']>r:return {'test':'higher_koszul',**x}
 if len(E)>=14:
  P=fixed_projection(b);rk=projected_extension_rank(E,P,2,3)
  if rk>340:return {'test':'projected_B7','rank':rk,'cost':20,'projection':P}
 return None

def run(rec,fam,index,points,extra_projected=False):
 start=time.time();M=ab_module(rec['subset']);F=decode_flag(fam['flag_before'],M)
 vs=[{j:Fraction(z) for j,z in v} for v in fam['kernel_basis']]
 states={insert(M,F,fam['weight_block'],vs,pt) for pt in points};families=[];history=[];exclusions=[]
 for level in range(fam['level'],18-len(M['support'])):
  keep=set();counts=Counter()
  for F in sorted(states):
   E=M['U']+extension_vectors(M,F);failure=test(E,M)
   if failure:counts[failure['test']]+=1;exclusions.append({'level':level,'flag':encode_flag(F),'failure':failure})
   else:keep.add(F)
  history.append({'level':level,'tested':len(states),'retained':len(keep),'excluded':dict(counts),'open_families_so_far':len(families)})
  if not keep:states=set();break
  if level==17-len(M['support']):states=keep;break
  states=set()
  for F in sorted(keep):
   rigid,params=successors(M,F);states.update(rigid)
   for i,K in params:
    if len(K)!=2:families.append({'level':level+1,'dimension':len(K)-1});continue
    nf={'level':level+1,'flag_before':encode_flag(F),'weight_block':i,'kernel_basis':[encode_vector(v) for v in K]}
    result=analyze(M,nf)
    if result['status']=='OPEN' and extra_projected:
     from projected_pencils import stratify_projected
     E0=M['U']+extension_vectors(M,F);X,Y=[linear_combination(M['blocks'][i][1],v) for v in K]
     projected=stratify_projected(E0,X,Y,M)
     if projected['status']!='OPEN':result={'status':projected['status'],'allowed':projected.get('allowed',[]),'tests':result['tests']+[projected]}
    if result['status']=='OPEN':families.append({'family':nf,'tests':result['tests']});continue
    if result['status']=='FINITE':
     for point in result['allowed']:states.add(insert(M,F,i,K,point))
 out={'subset':rec['subset'],'source_family':index,'source_points':points,'status':'EXCLUDED' if not states and not families else 'OPEN',
      'history':history,'exclusions':exclusions,'survivors':[encode_flag(F) for F in sorted(states)],'open_families':families,'seconds':time.time()-start}
 print(json.dumps({k:v for k,v in out.items() if k not in ('exclusions','open_families','survivors')}),flush=True)
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+');args=ap.parse_args()
 gate=json.load(open('certificates/det10_gate.json'));pencils=json.load(open('certificates/det10_pencil_probe.json'));out=[]
 for x in pencils['results']:
  if x['status']!='FINITE':continue
  if args.subset and x['subset']!=args.subset:continue
  rec=next(v for v in gate['results'] if v['subset']==x['subset']);fam=rec['parameter_branches'][x['family_index']]
  out.append(run(rec,fam,x['family_index'],x['allowed']))
  with open('certificates/finite_flag_continuations.json','w') as f:json.dump(out,f,indent=2)

if __name__=='__main__':main()

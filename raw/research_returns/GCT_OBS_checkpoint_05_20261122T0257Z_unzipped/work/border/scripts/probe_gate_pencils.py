#!/usr/bin/env python3
import json,time,argparse
from fractions import Fraction
from borel_quiver import ab_module,extension_vectors,linear_combination
from pencil_rank import stratify,verify_at

def decode_flag(data,M):
 F=[() for _ in M['blocks']]
 for rec in data:F[rec['weight_block']]=tuple(tuple((i,Fraction(x)) for i,x in v) for v in rec['rows'])
 return tuple(F)

def analyze(M,family):
 F=decode_flag(family['flag_before'],M);E0=M['U']+extension_vectors(M,F);K=[{i:Fraction(x) for i,x in v} for v in family['kernel_basis']]
 assert len(K)==2
 X,Y=[linear_combination(M['blocks'][family['weight_block']][1],v) for v in K]
 allowed=None;tests=[]
 for p in (1,2,3,4):
  for f in (2,1):
   dim=len(M['bw']) if f==2 else len(M['aw'])
   if (len(E0)+1)*dim<=17*(dim-p):continue
   if allowed is None:
    result=stratify(E0,X,Y,M,f,p);tests.append(result)
    if result['status']!='INCONCLUSIVE':allowed=result['allowed']
   else:
    ranks=[];surv=[]
    for point in allowed:
     r,c=verify_at(E0,X,Y,M,f,p,point);ranks.append({'point':point,'rank':r,'cost':c})
     if r<=17*c:surv.append(point)
    tests.append({'factor':f,'p':p,'point_ranks':ranks});allowed=surv
   if allowed==[]:return {'status':'EXCLUDED','tests':tests}
 return {'status':'OPEN' if allowed is None else 'FINITE','allowed':allowed,'tests':tests}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+');ap.add_argument('--limit',type=int);args=ap.parse_args()
 data=json.load(open('certificates/det10_gate.json'));out=[];start=time.time()
 for rec in data['results']:
  if args.subset and rec['subset']!=args.subset:continue
  if tuple(rec['subset']) not in map(tuple,data['remaining_subsets']):continue
  M=ab_module(rec['subset'])
  for i,family in enumerate(rec['parameter_branches']):
   if args.limit and len(out)>=args.limit:break
   result=analyze(M,family);result.update({'subset':rec['subset'],'family_index':i,'level':family['level']});out.append(result)
   print(json.dumps(result),flush=True)
   with open('certificates/det10_pencil_probe.json','w') as f:json.dump({'results':out,'seconds':time.time()-start},f,indent=2)

if __name__=='__main__':main()

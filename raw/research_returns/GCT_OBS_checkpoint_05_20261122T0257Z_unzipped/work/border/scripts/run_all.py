#!/usr/bin/env python3
"""One-command independent checker for BR-001 and BR-002, stdlib only.
All intermediate result files are regenerated; no stored ranks are trusted.
"""
import json,time
from pathlib import Path
from contextlib import redirect_stdout
from br_linear import NONUNIT_PIVOTS
from check_cover import run as cover
from check_koszul import run as koszul
from check_twodim_extensions import run as extensions,CASES
from check_higher_prolongation import check as higher
from check_support9 import check_case as support9


def localized_at_six():
 for n in NONUNIT_PIVOTS:
  while n%2==0:n//=2
  while n%3==0:n//=3
  assert n==1,'An unhandled exceptional prime occurred'


def main():
 root=Path(__file__).resolve().parent.parent;c=root/'certificates';logs=root/'logs';logs.mkdir(exist_ok=True)
 start=time.time();results={}
 with (logs/'allfield_recomputation.txt').open('w') as log,redirect_stdout(log):
  results['cover']=cover(c/'det7_cases.json',c/'per7_cases.json')
  expected_det={tuple(S) for n,sgn,S in CASES if sgn==-1}
  expected_det.add((0,1,3,6,7,9,18))
  expected_det |= {tuple(sorted(6*(q%6)+q//6 for q in S)) for S in tuple(expected_det)}
  expected_per={tuple(S) for n,sgn,S in CASES if sgn==1}
  expected_per.update({(0,1,3,6,7,9,18),(0,1,3,6,7,18,21)})
  assert len(expected_det)==14 and len(expected_per)==11
  for fam,expected in [('det',expected_det),('per',expected_per)]:
   rows=json.loads((c/(fam+'7_cases.json')).read_text())['records']
   assert all(r['type'] in {'A_koszul','B_koszul','support','prolongation'} for r in rows)
   assert {tuple(r['subset']) for r in rows if r['type']=='prolongation'}==expected
  for family in ('det','per'):
   r=koszul(c/(family+'7_cases.json'),0,family);assert r['status']=='PASS'
   results['koszul_'+family+'_Q']=r
  localized_at_six()
  for p in (2,3):
   r=koszul(c/'det7_cases.json',p,'det');assert r['status']=='PASS'
   results['koszul_det_F'+str(p)]=r
  results['extensions_Q']=[]
  for name,sign,S in CASES:
   if name=='P19':continue
   r=extensions(name,sign,S,0);assert r['status']=='PASS';results['extensions_Q'].append(r)
  assert NONUNIT_PIVOTS <= {2,3,4,6}
  results['higher_Q']=higher([0,1,2,6,7,18,19],1,0)
  for name in ('det','perA','perB'):
   r=support9(name,0);assert r['status']=='PASS';results['support9_'+name+'_Q']=r
  localized_at_six()
  r=koszul(c/'per7_cases.json',3,'per');assert r['status']=='PASS';results['koszul_per_F3']=r
  results['extensions_F3']=[]
  for name,sign,S in CASES:
   if name=='P19':continue
   r=extensions(name,sign,S,3);assert r['status']=='PASS';results['extensions_F3'].append(r)
  results['higher_F3']=higher([0,1,2,6,7,18,19],1,3)
  for name in ('det','perA','perB'):
   r=support9(name,3);assert r['status']=='PASS';results['support9_'+name+'_F3']=r
  results['extensions_det_F2']=[]
  for name,sign,S in CASES:
   if sign==1 or name=='P09_A':continue
   r=extensions(name,sign,S,2);assert r['status']=='PASS';results['extensions_det_F2'].append(r)
  results['P09A_higher_F2']=higher([0,1,3,6,7,9,12],-1,2)
  r=support9('det',2);assert r['status']=='PASS';results['support9_det_F2']=r
  # The exact list is an arithmetic certificate, not only timing information.
  results['all_recorded_nonunit_values']=sorted(NONUNIT_PIVOTS);localized_at_six()
 results['status']='PASS';results['claims']=['BR-001','BR-002'];results['seconds']=time.time()-start
 (c/'allfield_result.json').write_text(json.dumps(results,indent=2)+'\n')
 print(json.dumps({k:results[k] for k in ('status','claims','all_recorded_nonunit_values','seconds')}))

if __name__=='__main__':main()

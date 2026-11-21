#!/usr/bin/env python3
"""Exact ordinary-word escape from two genuine Hurwitz pentagon tests.

This verifies finite images and a literal free two-cycle.  It does not assert
the three-cycle in the free group, gentle admissibility, or any GT lift.
"""
from pathlib import Path
import hashlib,json,time
import numpy as np
from krammer_first_pair import inv as matrix_inverse

ROOT=Path(__file__).parent
def wi(w):return tuple(-a for a in w[::-1])
def comm(a,b):return a+b+wi(a)+wi(b)
def conj(a,b):return a+b+wi(a)
def swap(w):return tuple((2 if abs(a)==1 else 1)*(1 if a>0 else -1) for a in w)
def reduce_word(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return tuple(out)
def peval(w,a,b):
 gs={1:a,2:b,-1:np.argsort(a),-2:np.argsort(b)};v=np.arange(len(a))
 for k in w:v=v[gs[k]]
 return v
def meval(w,a,b):
 gs={1:a,2:b,-1:matrix_inverse(a),-2:matrix_inverse(b)};v=np.eye(len(a),dtype=np.int16)
 for k in w:v=v@gs[k]%3
 return v

def run():
 st=time.monotonic();x,y=(1,),(2,)
 c=comm(x,y);d=comm(c,conj(x,c));u=comm(d,conj(x,d))
 v=u+conj(c*4,u);w=wi(comm(c*6,v))
 b=conj(x+y,wi(w));f=swap(b)+wi(b)
 assert len(w)==448 and len(b)==452 and len(f)==904
 assert reduce_word(swap(f)+f)==()
 assert all(sum((1 if a>0 else -1) for a in f if abs(a)==j)==0 for j in [1,2])
 pairs=[(2,3),(4,0),(1,2),(3,4),(0,1)]
 rows=[];nielsen_rows=[]
 for family,degree in [('hurwitz_affine_affine_unipotent_3',648),('hurwitz_cubic_ssrr',20736)]:
  path=ROOT/(family+'.npz');ps=np.load(path)['generators'];assert ps.shape==(3,degree)
  co=lambda a,b:a[b];I=np.arange(degree)
  assert np.array_equal(co(co(ps[0],ps[1]),ps[0]),co(co(ps[1],ps[0]),ps[1]))
  assert np.array_equal(co(co(ps[1],ps[2]),ps[1]),co(co(ps[2],ps[1]),ps[2]))
  assert np.array_equal(co(ps[0],ps[2]),co(ps[2],ps[0]))
  z=co(co(ps[0],ps[1]),ps[2]);assert np.array_equal(co(co(co(z,z),z),z),I)
  xx=[co(a,a) for a in ps]
  for a in [co(co(ps[0],ps[1]),ps[0]),co(co(ps[2],ps[1]),ps[2])]:xx.append(co(a,a))
  for wordname,word in [('w',w),('f',f)]:
   supports=[]
   for a,bp in pairs+[(bp,a) for a,bp in pairs]:
    p=peval(word,xx[a],xx[bp]);supports.append(int(np.count_nonzero(p!=I)))
   assert supports==[0]*10
   rows.append({'family':family,'degree':degree,'word':wordname,'all_ten_oriented_pair_supports':supports,'braid_and_full_twist':'PASS','npz_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
  # Representatives of the entire Nielsen S3 orbit modulo inner conjugacy.
  for a,bp in pairs:
   for reverse in [False,True]:
    aa,bb=(xx[bp],xx[a]) if reverse else (xx[a],xx[bp])
    zz=np.argsort(co(aa,bb));values=[peval(f,aa,bb),peval(f,bb,zz),peval(f,zz,aa)]
    supports=[int(np.count_nonzero(t!=I)) for t in values]
    assert supports==[0,0,0]
    cycle=co(co(values[2],values[1]),values[0]);assert np.array_equal(cycle,I)
    nielsen_rows.append({'family':family,'pair':[a+1,bp+1],'reverse':reverse,'tau_orbit_supports':supports,'three_cycle_support':0})
 # The larger original affine detector, not just its compressed projection.
 ns={};exec((ROOT/'affine_cubic_detector.py').read_text().split('E=gp')[0],ns)
 dat=json.loads((ROOT/'affine_cubic_detector.json').read_text());X,Y=tuple(dat['x']),tuple(dat['y'])
 def ae(word):
  gs={1:X,2:Y,-1:ns['ai'](X),-2:ns['ai'](Y)};a=ns['ID']
  for k in word:a=ns['am'](a,gs[k])
  return a
 assert ae(w)==(1,7,1,0,0,1)
 assert ae(f)==(7,4,1,0,0,1)
 # E0 exact signed coordinate and marked S4 evaluation.
 X0=np.array([[2,1,0],[0,2,0],[0,0,1]],dtype=np.int16)
 Y0=np.array([[2,0,1],[2,2,0],[0,0,1]],dtype=np.int16)
 F0=meval(f,X0,Y0);assert np.array_equal(F0,np.array([[1,0,1],[0,1,1],[0,0,1]]))
 P=np.array([1,2,0,3]);T=np.array([1,2,3,0]);assert np.array_equal(peval(f,P,T),np.arange(4))
 # The complete first Krammer value has the unique two-cycle phase of F13.
 A,B,C=np.load(ROOT/'krammer_first_pair.npz')['generators'].astype(np.int16)
 kf=meval(f,A@A%3,B@B%3)
 exact=np.load(ROOT.parent/'five_level_six/krammer_six_first_pair.npz')
 k=next(j for j,l in enumerate(exact['labels']) if tuple(l)==(0,1))
 assert np.array_equal(kf,exact['candidates'][k])
 out={'statements':['D23.P11','D23.P12'],'expanded_lengths':{'w':len(w),'b':len(b),'f':len(f)},'reduced_f_length':len(reduce_word(f)),'word_f':list(f),'free_two_cycle':'PASS','derived_depth_at_least':3,'E_F_w':ae(w),'E_F_f':ae(f),'E0_f':F0.tolist(),'marked_S4_f':'identity','Krammer_first_pair_F13_label':[0,1],'Hurwitz_checks':rows,'full_Nielsen_S3_checks':nielsen_rows,'scope':'Ordinary word with the stated finite images, exact free two-cycle and all Hurwitz Nielsen three-cycles; no free three-cycle, gentle admissibility, or GT lift asserted.','elapsed_seconds':time.monotonic()-st,'result':'PASS'}
 (ROOT/'hurwitz_escape_word.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['word_f','full_Nielsen_S3_checks']},indent=2))

if __name__=='__main__':run()

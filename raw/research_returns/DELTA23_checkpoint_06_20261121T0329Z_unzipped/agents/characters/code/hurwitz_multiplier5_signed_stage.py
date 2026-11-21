#!/usr/bin/env python3
"""Common-word signed24 covariance for global multiplier-five candidates."""
from pathlib import Path
import contextlib,importlib.util,io,json,itertools
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_multiplier5_global_seeds import HERE,PENT,FIVE,A,B,C,Z,bm,points,loc,local,ort
from hurwitz_multiplier5_detector import power
spec=importlib.util.spec_from_file_location('signs112',HERE/'code/hurwitz_orthogonal_signs.py');signs=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(signs)

def signed_partial(sub,values):
 W=np.full(1344,-1,dtype=int);W[sub]=values
 q=np.full(24,-1,dtype=np.int16)
 for j in sorted(set(map(int,bm[sub]))):
  k=int(bm[W[points[j][0]]]);p=loc[k,W[points[j]]]
  M,mu=ort.lift_permutation(p);assert mu==1 and ort.determinant(M)==1
  bit=int(signs.spinor(M)==2)
  q[2*j]=2*k+bit;q[2*j+1]=2*k+1-bit
 return q

def run():
 qs=np.load(FIVE/'hurwitz_block_correlations.npz')['signed_generators'];qa,qb,qc=qs;qz=power(qa[qb],3)
 first=np.load(HERE/'records/hurwitz_multiplier5_detector.npz');a,b=first['A'],first['B'];Fs=first['F']
 gx=np.r_[a[a],36+qa[qa],60+qc[qc]];gy=np.r_[b[b],36+qb[qb],60+qz]
 J=PermutationGroup([Permutation(gx.tolist()),Permutation(gy.tolist())]);D=J.derived_subgroup();print('joint84',J.order(),'derived',D.order(),flush=True)
 lookup={p.tobytes():i for i,p in enumerate(Fs)};rows={i:[]for i in range(len(Fs))}
 for g in D.generate_schreier_sims():
  e=np.array(g.array_form);p=e[:36].astype(Fs.dtype)
  if p.tobytes()in lookup:rows[lookup[p.tobytes()]].append(np.array([e[36:60]-36,e[60:84]-60]))
 print('fibers',[(i,len(r))for i,r in rows.items()],flush=True)
 glob=np.load(HERE/'records/hurwitz_multiplier5_global_probe.npz');ul=json.loads((HERE/'records/hurwitz_multiplier5_U_local.json').read_text())
 valid={(r['detector'],r['lift'])for r in ul['cases']if any(x['C_covariance']for x in r['R11_candidates'])}
 p0=[i for i,l in enumerate(glob['partial_labels_0'])if l[0]==0]
 q0={i:signed_partial(glob['partial_subset_0'],glob['partial_maps_0'][i])for i in p0}
 q1=[signed_partial(glob['partial_subset_1'],v)for v in glob['partial_maps_1']]
 known=[]
 for lab,v in zip(glob['known_labels'],glob['known_maps']):
  no,wi,det,mu=map(int,lab)
  if(no,wi)in valid:known.append((no,wi,signed_partial(glob['known_subset'],v)))
 qidx0=np.flatnonzero(q0[p0[0]]>=0);qidx1=np.flatnonzero(q1[0]>=0);qidxk=np.flatnonzero(known[0][2]>=0)
 assert sorted(np.r_[qidx0,qidx1,qidxk])==list(range(24))
 answers=[];needed={};cache={}
 for no,wi,qk in known:
  for i0,i1 in itertools.product(p0,range(len(q1))):
   w=np.zeros(24,dtype=np.int16);w[qidx0]=q0[i0][qidx0];w[qidx1]=q1[i1][qidx1];w[qidxk]=qk[qidxk]
   assert len(set(map(int,w)))==24
   assert np.array_equal(w[qa],power(qa,5)[w])and np.array_equal(w[qz],power(qz,5)[w])
   key=(no,w.tobytes())
   if key not in cache:
    choices=[]
    for ri,(fq,rq)in enumerate(rows[no]):
     if np.array_equal(w[qb],np.argsort(fq)[power(qb,5)[fq[w]]])and np.array_equal(w[qc],rq[power(qc,5)[np.argsort(rq)[w]]]):choices.append(ri)
    cache[key]=choices
   if cache[key]:
    for ri in cache[key]:answers.append([no,wi,i0,i1,ri])
    needed[(no,wi,i0,i1)]=len(cache[key])
 print('assemblies',len(needed),'R/F rows',len(answers),'unique signed tests',len(cache),flush=True)
 saved={'passing_labels':np.array(answers),'q0_indices':np.array(p0),'q0':np.array([q0[i]for i in p0]),'q1':np.array(q1),'known_labels':np.array([[a,b]for a,b,q in known]),'known_q':np.array([q for a,b,q in known]),'signed_generators':qs}
 for i,r in rows.items():saved[f'commonword_fiber_{i}']=np.array(r)
 np.savez_compressed(HERE/'records/hurwitz_multiplier5_signed_stage.npz',**saved)
 out={'joint84_order':int(J.order()),'joint84_derived_order':int(D.order()),'four_block_cases':len(known),'initial_global_assemblies':len(known)*len(p0)*len(q1),
      'passing_assemblies':len(needed),'passing_F_R_rows':len(answers),'distinct_signed_tests':len(cache),
      'per_detector':{str(i):sum(k[0]==i for k in needed)for i in sorted({k[0]for k in needed})},
      'scope':'Common Fprime word on first36 plus signed first/mixed pairs; literal A5/B5/C5 covariance. Full mixed R and full U commutation are still additional.'}
 (HERE/'records/hurwitz_multiplier5_signed_stage.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()

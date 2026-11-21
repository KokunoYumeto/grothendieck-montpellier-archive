#!/usr/bin/env python3
"""Independent exact Artin checks supporting the full rightmost-kernel recursion.

The proof is formal for every commutator f. The sample commutators below
are additional word checks, not a finite substitute for that proof.
"""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE.parent/'five_level_six'))
from hurwitz_last_coordinate import same,inv,comm,z,red

def meridians(n):
 out=[]
 for i in range(1,n+1):
  v=tuple(range(n,i,-1));out.append(v+(i,i)+inv(v))
 return out

def samples(a,b):
 return [comm(a,b),comm(a+a,inv(b))]

def run():
 rows=[]
 for n in [2,3,4,5]:
  sig=(n,);us=meridians(n);D=sum(us,());P=sum(us[:-1],());u=us[-1];low=meridians(n-1)
  extra=z(n-1)+inv(z(n+1));other=inv(z(n-1))+z(n+1)
  y=tuple(range(n-1,1,-1))+(1,1)+tuple(range(2,n))
  assert same(sig+z(n)+sig,z(n-1)+inv(z(n))+z(n+1),n+1)
  assert same(sig+inv(D)+inv(sig),extra+P,n+1)
  assert same(y,other+inv(D),n+1)
  for a in [P,u]:assert same(comm(extra,a),(),n+1)
  for a in [D,u]:assert same(comm(other,a),(),n+1)
  for v,w in zip(us[:-1],low):assert same(v,sig+w+inv(sig),n+1)
  for F,J in zip(samples(inv(D),u),samples(P,u)):
   assert same(sig+F+inv(sig),J,n+1)
  rows.append({'n':n,'nested_twist_identity':True,'conjugated_boundary_input':True,
               'standard_y_input_correction':True,'commuting_extra_factors':True,
               'all_lower_meridian_embeddings':True,'two_sample_commutator_conjugations':True})
 out={'scope':'Independent algebraic marking certificate for the universal recursion; generic proof uses zero exponent sums and these braid identities.',
      'cases':rows,'result':'PASS'}
 (HERE/'records/full_kappa_recursion.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()

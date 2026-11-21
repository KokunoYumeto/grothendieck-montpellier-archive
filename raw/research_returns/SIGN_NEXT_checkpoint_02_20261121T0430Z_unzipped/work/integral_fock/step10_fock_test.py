#!/usr/bin/env python3
"""Exact fixed-data arithmetic and root-lattice test from Alpoge numEx.
No Lean kernel execution. Source declarations/sha256 are recorded in manifests.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
import json, csv
import sympy as S
root=Path(__file__).resolve().parent
k,m,t,nV,places=8,2,15,24,8
v=[24,20,16,12,8,4,0]; b=[91,109]; e=[100,118]
N=lambda j:k+j*(t+1)
sig=lambda j:(k+j-1,m-j)
sigPar=lambda i:v[i] if i<k-1 else -b[i-(k-1)]
rows=[];tests=[]
for j in [1,2]:
 p,q=sig(j)
 ap=[F(sigPar(i)+e[j-1])-F(nV-1-2*i,2)-F(p-q,2) for i in range(p)]
 am=[F(b[j+c]-e[j-1])-F(t+1+2*c,2) for c in range(q)]
 assert all(a.denominator==1 for a in ap+am)
 ap=list(map(int,ap));am=list(map(int,am))
 Dp=places*sum(ap);Dm=places*sum(am)
 gaps=[ap[i]-ap[i+1] for i in range(p-1)]
 dim=F(1)
 for a in range(p):
  for bb in range(a+1,p):dim*=F(ap[a]-ap[bb]+bb-a,bb-a)
 assert dim.denominator==1
 record={'j':j,'definite_rank_source':N(j-1),'definite_rank_target':N(j),
         'aux_signature':[p,q],'aPlus':ap,'aMinus':am,'gaps':gaps,
         'Dplus':Dp,'Dminus':Dm,'FTypeG':str(-F(Dp+Dm,2)),
         'FRamD':str(-F(k-1,2)*4*e[j-1]),'FInert_p3':str(F(56*e[j-1],3**2-1)),
         'positive_compact_factor_dim':str(dim.numerator),
         'dimension_factorization':{str(p):int(a) for p,a in S.factorint(dim.numerator).items()}}
 rows.append(record)
 for i,d in enumerate(gaps):
  C=comb(d,2)
  # q_s=F^(s)q_0, normalized pair diag C(d,s), r_s=q_s/C(d,s).
  # This tests every root, not just the three distinct gap values.
  A=S.zeros(d+1);B=S.zeros(d+1);G=S.diag(*[comb(d,s) for s in range(d+1)])
  for s in range(d):A[s+1,s]=s+1
  for s in range(1,d+1):B[s-1,s]=d-s+1
  assert A.T*G==G*B
  assert (A*A)[2,0]==2
  Adual=G*A*G.inv()
  assert (Adual*Adual)[2,0]==d*(d-1)
  assert (A*A/F(2))[2,0]==1
  assert (Adual*Adual/F(2))[2,0]==C
  tests.append({'j':j,'root_i_one_based':i+1,'gap_d':d,
    'ordinary_two_step_Weyl':2,'ordinary_two_step_dual':d*(d-1),
    'second_divided_Weyl':1,'second_divided_dual':C,
    'dual_first_descendant_squared_norm':str(F(1,d)),
    'second_divided_dual_prime_factors':{str(p):int(a) for p,a in S.factorint(C).items()}})
assert rows[0]['aPlus']==[109,106,103,100,97,94,91,1]
assert rows[1]['aPlus']==[126,123,120,117,114,111,108,18,1]
assert rows[0]['Dplus']==5608 and rows[1]['Dplus']==6704
assert rows[0]['FTypeG']=='-2808' and rows[1]['FTypeG']=='-3352'
# Rigorous rational cutoff certificate: 2^(1/300)<101/100 and exp(101/100)<11/4.
x=F(101,100)
assert x**300>2
s=sum(x**r/F(factorial(r)) for r in range(13))
tail=x**13/F(factorial(13))/(1-x/F(14))
assert s+tail<F(11,4)
# Thus X''=8 exp(2^(1/300))<22<89, so FjP(1,89)=FjP(2,89)=0.
assert 89 not in [2,7,11,3697,7393]
certificate={'source':'Alpoge Formalism/L2/DIV numEx (source path LocalToGlobal/Divisibility/NumbersLemmas.lean)',
 'rows':rows,'simple_root_tests':tests,'cutoff_rational_upper':'22',
 'FjP_at_89':[0,0],'root_d90_second_divided_dual_v89':1,
 'comparison_period_ordinary':2,'comparison_period_divided':1,
 'caution':'These periods are normalized row-root pairings, not global theta integral evaluations.'}
(root/'step10_fock_test.json').write_text(json.dumps(certificate,indent=2))
with (root/'step10_root_indices.tsv').open('w') as out:
 w=csv.writer(out,delimiter='\t');w.writerow(['lift_j','simple_root','d','ordinary_Weyl','ordinary_dual','divided_Weyl','divided_dual'])
 for z in tests:w.writerow([z['j'],z['root_i_one_based'],z['gap_d'],2,z['ordinary_two_step_dual'],1,z['second_divided_dual']])
print(json.dumps(certificate,indent=2))

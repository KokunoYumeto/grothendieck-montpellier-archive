"""Integer certificate for explicit determinant-product common vectors.

The symbolic Schur-support proof is in PG-OP-DETERMINANT. This checker
verifies all numeric entropy comparisons, source permutations, prescribed
sizes and integer exponents. It does not expand enormous polynomials or
solve a max-dimension Specht system.
"""
from pathlib import Path
from math import log2,isqrt
from hashlib import sha256
import json
ROOT=Path('/workspace/scratch/9f5945cf2012/VPVNP_HINGE_work')
size_path=ROOT/'outputs/rt_operator_gate_sizes.json';raw=size_path.read_bytes();sizes=json.loads(raw)
rows=[]
for item in sizes['results']:
 q=item['q'];N=q.bit_length()-1;assert q==1<<N
 n=item['first_passing_power_of_two'];d=q*q
 assert n%(2*d)==0;a=n//(2*d)
 A=q*(q+1)//2;B=d*(d+1)//2
 den=(n+1)**A;L=(q**n+den-1)//den;m=L.bit_length()-1;t=isqrt(2*m-1)
 if t*t<2*m-1:t+=1
 k=m-1-t;power_margin=28*k-25*N*n
 assert k>0 and power_margin>0 and (1<<power_margin)>(n+1)**(20*B)
 # Raising h_d>(5/4)log2q to the 4d-th power gives this integer test.
 lhs=1<<((4+3*N)*d);rhs=(d+1)**(2*(d+1));assert lhs>rhs
 # Flattening b is identity; flattening c is the q-by-q commutation map.
 permutation=[b*q+a0 for a0 in range(q) for b in range(q)]
 inversions=sum(permutation[i]>permutation[j] for i in range(d) for j in range(i+1,d))
 sign=(-1)**inversions;assert sign==(-1)**(q*(q-1)//2)
 evaluation=sign**a
 rows.append({'q':q,'N':N,'d':d,'n':n,'power':a,
              'symbolic_polynomial':f'(det(flat_12_34(X))*det(flat_14_23(X)))^{a}',
              'degree':2*d*a,'local_rectangle':[n//q]*q,
              'cut_minimum_shape':[a*(d+1)]+[a]*(d-1),
              'entropy_integer_lhs':str(lhs),'entropy_integer_rhs':str(rhs),
              'strict_entropy_comparison':True,
              'entropy_bits':log2(2*d)-(d+1)/(2*d)*log2(d+1),
              'requested_threshold_bits':1.25*N,
              'det_b_at_Cq':1,'det_c_at_Cq':sign,'polynomial_at_Cq':evaluation,
              'normalizing_sign':evaluation,
              'prescribed_size_inequality_verified':True})
q=16;N=4;d=q*q
lhs=1<<((4+3*N)*d);rhs=(d+1)**(2*(d+1));assert lhs<rhs
out={'status':'PASS exact first-three COMPRESSED and RECTANGULAR family witnesses',
     'scope':'No max-dimension Specht-block feasibility is inferred. q=16 remains unresolved; only this determinant-power witness misses its threshold.',
     'size_input_sha256':sha256(raw).hexdigest(),'results':rows,
     'q16_ansatz_comparison':{'lhs':str(lhs),'rhs':str(rhs),'passes':False,
      'entropy_bits':log2(2*d)-(d+1)/(2*d)*log2(d+1),'threshold_bits':5}}
p=ROOT/'outputs/pg_determinant_gate_verification.json';tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(p)
print(json.dumps({'status':out['status'],'witnesses':[{k:r[k] for k in ('q','n','power','entropy_bits','requested_threshold_bits','polynomial_at_Cq')} for r in rows],'q16_ansatz_passes':False},indent=2))

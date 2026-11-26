"""Exact entropy certificates for determinant products decorated by slice minors.

The polynomial is D_b^21 D_c^21 W^22, W=product_i det(X_{i,b,i,d}).
Its degree is64q²; the manuscript proves common-cut dominance and
nonzero evaluation, including rectangular projection. No large polynomial
is expanded. All threshold comparisons use integer powers, without logs.
"""
from pathlib import Path
from math import log2
from hashlib import sha256
import json,time
ROOT=Path('/workspace/scratch/9f5945cf2012/VPVNP_HINGE_work')
results=[]
for N in range(1,8):
 started=time.time();q=1<<N;d=q*q;n=64*d
 u=21*(d+1)+22*q;v=21+22*q
 # Product nu_i^nu_i; n and q are dyadic, so the threshold comparison
 # reduces exactly to 2^(n*(log2n-5N/4)) > this product.
 exponent=n*(4*n.bit_length()-4-5*N)//4
 assert 4*exponent==n*(4*(n.bit_length()-1)-5*N)
 product=pow(u,u)*pow(v,v*(q-1))*pow(21,21*(d-q))
 left=1<<exponent
 passes=left>product
 assert passes==(N<=6)
 bits=product.bit_length();digest=sha256(product.to_bytes((bits+7)//8,'big')).hexdigest()
 entropy=log2(n)-(u*log2(u)+(q-1)*v*log2(v)+21*(d-q)*log2(21))/n
 rows={'q':q,'N':N,'degree':n,'source_determinant_power':21,'slice_product_power':22,
       'dominating_shape_run_lengths':[[u,1],[v,q-1],[21,d-q]],
       'comparison_power_of_two':exponent,'comparison_rhs_bit_length':bits,
       'comparison_rhs_sha256':digest,'strict_entropy_threshold_passes':passes,
       'entropy_bits_for_display':entropy,'threshold_bits_for_display':1.25*N,
       'unprojected_evaluation_at_Cq':(-1)**(21*q*(q-1)//2),
       'rectangular_projection_evaluation_nonzero_by_fischer_pairing':True,
       'local_rectangle':[64*q]*q,
       'elapsed_seconds':time.time()-started}
 results.append(rows)
 print(json.dumps({k:rows[k] for k in ('q','strict_entropy_threshold_passes','entropy_bits_for_display','elapsed_seconds')}),flush=True)
out={'status':'PASS exact certificates throughq64; q128 dominance guarantee insufficient',
     'scope':'Explicit compressed and rectangular systems at prescribed n(q) follow by taking powers and projecting the local rectangle. This gives no claim about old maximum-dimension blocks. Failure of the q128 comparison does not imply failure of the polynomial or the system.',
     'results':results}
p=ROOT/'outputs/pg_decorated_determinants_verification.json';t=p.with_suffix('.json.tmp');t.write_text(json.dumps(out,indent=2)+'\n');t.replace(p)

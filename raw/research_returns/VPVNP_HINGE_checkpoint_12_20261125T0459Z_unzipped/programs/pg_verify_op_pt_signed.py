"""Exact signed-central support test and linear upper certificate.

This deliberately drops positivity, retaining the exact nonzero EPR trace.
The input Gram matrices were built and verified separately. The script
never asserts an asymptotic or semiring-regularized consequence.
"""
from pathlib import Path
from math import prod,log2
import json,hashlib,argparse
import sympy as sp
ROOT=Path('/workspace/scratch/9f5945cf2012/VPVNP_HINGE_work')

def main(path):
 raw=path.read_bytes();d=json.loads(raw);D=sp.Matrix(d['D']);r=sp.Matrix(d['ranks']);parts=d['active_partitions'];products=[prod(a**a for a in v) for v in parts]
 for boundary in sorted(set(products)):
  indices=[i for i,p in enumerate(products) if p<=boundary]
  good=[v for v in D[:,indices].nullspace() if sum(r[i]*x for i,x in zip(indices,v))!=0]
  if good:break
 else:raise AssertionError('Identity must give a nonzero trace witness')
 v=good[0];x=sp.zeros(len(parts),1);tr=sum(r[i]*a for i,a in zip(indices,v))
 for i,a in zip(indices,v):x[i]=a/tr
 assert D*x==sp.zeros(len(parts),1) and (r.T*x)[0]==1
 high=[i for i,p in enumerate(products) if p<boundary]
 # On higher-entropy columns, the trace functional belongs to the row
 # span of D: this excludes all signed kernel vectors with nonzero trace.
 if high:
  solution=next(iter(sp.linsolve((D[:,high].T,r[high,0]))))
  variables=set().union(*(a.free_symbols for a in solution))
  y=sp.Matrix([a.subs({v:0 for v in variables}) for a in solution])
 else:y=sp.zeros(len(parts),1)
 Dy=D*y
 assert all(Dy[i]==r[i] for i in high)
 assert all(x[i]==0 for i,p in enumerate(products) if p>boundary)
 out={'status':'PASS exact signed CENTRAL support optimum; no full-p0 or regularization upper bound',
      'input':str(path.relative_to(ROOT)),'input_sha256':hashlib.sha256(raw).hexdigest(),
      'n':d['n'],'lambda':d['lambda'],'mu':d['mu'],'active_partitions':parts,
      'witness':[str(a) for a in x], 'witness_trace':1,
      'witness_has_negative_coefficients':any(a<0 for a in x),
      'boundary_entropy_product':str(boundary),
      'boundary_partitions':[p for p,c in zip(parts,products) if c==boundary],
      'finite_optimum_bits':min(-sum(a/d['n']*log2(a/d['n']) for a in parts[i]) for i,a in enumerate(x) if a),
      'positive_central_optimum_bits':d['witness']['threshold_bits'],
      'strictly_higher_entropy_indices':high,
      'upper_linear_dual':[str(a) for a in y],
      'D_times_upper_dual':[str(a) for a in Dy],
      'scope':'The row-span certificate rules out signed CENTRAL Gamma-fixed operators of nonzero trace supported strictly above the boundary. It does not rule out noncentral operators or other Schur blocks.'}
 target=ROOT/'outputs'/path.name.replace('.json','_signed_verified.json');tmp=target.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(target)
 print(json.dumps({k:out[k] for k in ('n','lambda','mu','finite_optimum_bits','positive_central_optimum_bits','witness_has_negative_coefficients','boundary_partitions')},indent=2),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('inputs',nargs='+');args=ap.parse_args()
 for p in args.inputs:main(ROOT/p)

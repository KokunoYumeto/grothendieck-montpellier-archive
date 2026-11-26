"""SH55 second-moment rows added to the preserved Singh radial model.

The additional label is ['quadratic_budget',term].  Its coefficient at
orbit a, threshold k is weights[a]*(2*k-1); RHS is
(m-1)^2*D^2*2^(D-1)-1.  Mathematical verification is exact.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json,sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,vstack
import sh_singh_radial_rank_certificate as base

def system(config):
    d=base.system(config['dimension'],config['width'],config.get('low_value'),
                  config.get('global_min',False),config.get('minimum_both',False))
    D,m,M,n,L=d['D'],d['m'],d['M'],d['n'],d['layers']
    for term in range(2):
        row={(term*L+a)*n+k-1:d['weights'][a]*(2*k-1)
             for a in range(L) for k in range(1,n+1)}
        d['rows'].append((['quadratic_budget',term],row,(m-1)**2*D**2*M-1))
    d['quadratic_moment']=True
    return d

def main():
    ip=Path(sys.argv[1]);op=Path(sys.argv[2]);cfg=json.loads(ip.read_text());d=system(cfg)
    A,b=base.sparse_matrix(d);eq=vstack((A.T,coo_matrix(b.reshape(1,-1)))).tocsc()
    res=linprog(np.zeros(A.shape[0]),A_eq=eq,b_eq=np.r_[np.zeros(d['nv']),-1.],
                bounds=(0,None),method='highs',options={'time_limit':cfg.get('seconds',60),
                'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    out={k:v for k,v in d.items() if k!='rows'}
    out.update(input_sha256=hashlib.sha256(ip.read_bytes()).hexdigest(),
               constraints=len(d['rows']),solver_status=int(res.status),
               solver_message=str(res.message),feasibility_only=True,
               claim='No claim unless exact rational verification passes.')
    if res.x is not None:
        entries=[]
        for i,v in enumerate(res.x):
            if v>1e-9:
                q=Fraction(float(v)).limit_denominator(10**8)
                entries.append(dict(row=i,label=d['rows'][i][0],numerator=q.numerator,denominator=q.denominator))
        mode='direct rational reconstruction'
        try:checks=base.verify(d,entries)
        except AssertionError:
            entries=base.bounded_rational_certificate(d,res.x)
            checks=base.verify(d,entries);mode='common-grid rounding and exact box-row repair'
        out.update(certificate=entries,verification=checks,reconstruction_mode=mode,
                   claim='Exact nonnegative combination of necessary rows gives zero <= minus one.')
    tmp=op.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(op)
    print(json.dumps({k:v for k,v in out.items() if k!='certificate'}),flush=True)

if __name__=='__main__':main()

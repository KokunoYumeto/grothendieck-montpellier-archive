"""Deterministic coefficient least squares and noncentral map refinement.

This is a bounded numerical construction attempt, never an identity proof.
The 70 nonzero spin-weight patterns retain every coordinate of the full
all-mixed local Schur sector.  Every evaluation solves scalar coefficients
by SVD least squares before differentiating the local multiplicity maps.
"""
from pathlib import Path
import hashlib,itertools,json,time,sys
import numpy as np
from scipy.optimize import minimize

W=Path(__file__).resolve().parents[1]
ip=Path(sys.argv[1]) if len(sys.argv)>1 else W/'inputs/sh_cauchy_noncentral_varproj.json'
cfg=json.loads(ip.read_text())
data=np.load(W/cfg['arrays'])
old=np.load(W/cfg['initial_maps'])
patterns=[s for s in itertools.product(range(2),repeat=8) if sum(s)==4]

def compress(tensor):
    return np.stack([tensor[np.ix_(*[(2*s,2*s+1) for s in pattern])]
                     for pattern in patterns])

h=compress(data['target']).astype(float)
assert np.sum(h*h)==np.sum(data['target'].astype(float)**2)
crowns=np.stack([compress(x) for x in data['crowns']]).astype(float)
assert np.sum(crowns*crowns)==np.sum(data['crowns'].astype(float)**2)
spin_transfer=None
full_h=h.copy()
if cfg.get('spin_zero_projection',False):
    eps=np.array([[0.,1.],[-1.,0.]])
    pairings=[]
    for pairing in (((0,1),(2,3)),((0,2),(1,3))):
        v=np.zeros((2,)*4)
        for bits in itertools.product(range(2),repeat=4):
            v[bits]=np.prod([eps[bits[i],bits[j]] for i,j in pairing])
        pairings.append(v.ravel())
    Q,_=np.linalg.qr(np.stack(pairings,axis=1))
    spin_transfer=np.array([np.outer(Q[np.ravel_multi_index(s[:4],(2,)*4)],
                                     Q[np.ravel_multi_index(s[4:],(2,)*4)]).ravel()
                            for s in patterns])
    assert np.max(abs(spin_transfer.T@spin_transfer-np.eye(4)))<1e-12
    h=(spin_transfer.T@h.reshape(70,-1)).reshape((4,)+(2,)*8)
    assert np.linalg.norm(spin_transfer@h.reshape(4,-1)-full_h.reshape(70,-1))<1e-11
    crowns=np.stack([(spin_transfer.T@x.reshape(70,-1)).reshape((4,)+(2,)*8)
                     for x in crowns])
indices=old['matching_indices'];A=len(indices);base=crowns[indices]
raw=old['maps'].copy();norm=float(np.sum(h*h))
start=time.time();trace=[];best=float('inf');best_data=None;count=0

def apply_axis(x,M,v):
    moved=np.moveaxis(x,v+2,-1)
    y=np.matmul(moved.reshape(A,-1,2),np.swapaxes(M,1,2)).reshape(moved.shape)
    return np.moveaxis(y,-1,v+2)

def evaluate(flat,gradient=True):
    global best,best_data,count
    raw=flat.reshape(A,8,2,2)
    norms=np.sqrt(np.sum(raw*raw,axis=(-1,-2),keepdims=True)+1e-30)
    mats=raw/norms*2**0.5
    history=[base]
    for v in range(8):history.append(apply_axis(history[-1],mats[:,v],v))
    terms=history[-1];design=terms.reshape(A,-1).T
    alpha,_,rank,sv=np.linalg.lstsq(design,h.ravel(),rcond=1e-13)
    residual=(design@alpha-h.ravel()).reshape(h.shape)
    value=float(np.sum(residual*residual)/norm)
    if not gradient:return value,mats,alpha,rank,sv
    gy=2*alpha.reshape((A,)+(1,)*9)*residual/norm
    gm=np.zeros_like(raw)
    for v in range(7,-1,-1):
        xx=np.moveaxis(history[v],v+2,-1).reshape(A,-1,2)
        yy=np.moveaxis(gy,v+2,-1).reshape(A,-1,2)
        gm[:,v]=np.matmul(np.swapaxes(yy,1,2),xx)
        gy=apply_axis(gy,np.swapaxes(mats[:,v],1,2),v)
    gr=2**0.5/norms*(gm-raw*np.sum(gm*raw,axis=(-1,-2),keepdims=True)/(norms*norms))
    if value<best:
        best=value;best_data={'maps':mats.copy(),'coefficients':alpha.copy(),
                              'matching_indices':indices.copy()}
    if count%10==0:
        rec={'evaluation':count,'seconds':time.time()-start,'relative_squared_residual':value,
             'best':best,'coefficient_design_rank':int(rank),'largest_coefficient':float(np.max(abs(alpha))),
             'singular_ratio':float(sv[-1]/sv[0]),'gradient_norm':float(np.linalg.norm(gr))}
        trace.append(rec);print(json.dumps(rec),flush=True)
    count+=1
    return value,gr.ravel()

f0,g0=evaluate(raw.ravel());eps=1e-5;errs=[]
for j in (0,73,511):
    plus=raw.ravel().copy();minus=plus.copy();plus[j]+=eps;minus[j]-=eps
    diff=(evaluate(plus,False)[0]-evaluate(minus,False)[0])/(2*eps)
    errs.append(float(abs(diff-g0[j])))
assert max(errs)<1e-6,errs

class BoundedStop(Exception):pass
def objective(flat):
    if time.time()-start>cfg['time_limit_seconds']:raise BoundedStop('wall-time bound')
    if (W/'inputs/sh_stop_cauchy_varproj').exists():raise BoundedStop('explicit stop sentinel')
    return evaluate(flat)

status=''
try:
    result=minimize(objective,raw.ravel(),method='L-BFGS-B',jac=True,
                    options={'maxiter':cfg['max_iterations'],'ftol':1e-15,'gtol':1e-11,
                             'maxls':30,'maxcor':20})
    status=str(result.message)
except BoundedStop as e:status=str(e)

# Verify best coefficient arrays again in the original full 4^8 coordinates.
def full_apply(x,M,v):
    moved=np.moveaxis(x,v+1,-1)
    y=np.matmul(moved.reshape(A,-1,4),np.swapaxes(M,1,2)).reshape(moved.shape)
    return np.moveaxis(y,-1,v+1)
full=data['crowns'][indices].astype(float)
for v in range(8):
    m=np.zeros((A,4,4));m[:,:2,:2]=best_data['maps'][:,v];m[:,2:,2:]=best_data['maps'][:,v]
    full=full_apply(full,m,v)
residual=np.einsum('a,a...->...',best_data['coefficients'],full)-data['target']
if spin_transfer is None:
    full_error=float(np.sum(residual*residual)/norm)
else:
    raw_prediction=compress(np.einsum('a,a...->...',best_data['coefficients'],full)).reshape(70,-1)
    projected_prediction=spin_transfer@(spin_transfer.T@raw_prediction)
    full_error=float(np.sum((projected_prediction-full_h.reshape(70,-1))**2)/norm)
assert abs(full_error-best)<1e-10
np.savez_compressed(W/cfg['best_output'],**best_data)
out={'status':'NUMERICAL CONSTRUCTION ATTEMPT ONLY; no exact identity or impossibility conclusion',
     'optimizer_status':status,'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),
     'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'terms':A,'spin_patterns':len(patterns),'evaluations':count,'seconds':time.time()-start,
     'spin_zero_projection':cfg.get('spin_zero_projection',False),
     'initial_coefficient_optimized_residual':f0,'best_relative_squared_residual':best,
     'full_coordinate_relative_squared_residual':full_error,'gradient_check_errors':errs,'trace':trace,
     'scope':'all spin-weight coordinates of the full all-mixed r4 sector; other Schur sectors absent'}
p=W/cfg['output'];tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(p)
print(json.dumps({k:v for k,v in out.items() if k!='trace'},indent=2))

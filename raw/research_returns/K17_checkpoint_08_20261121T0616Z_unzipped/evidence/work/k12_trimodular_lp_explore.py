"""Exploratory floating-point necessary minimum constraints for two templates.

Output is not a mathematical certificate. Exact rational reconstruction
and complete short-vector verification are required before promotion.
"""
from itertools import combinations, product
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
import sympy as sp


base = Path(__file__).parent
records = json.loads((base/'k12_trimodular_extremal_check.json').read_text())['results']
results = []
for rec in records[:2]:
    b = sp.Matrix(3,12,lambda i,j: rec['rays'][j][i])
    piv = next(j for j in combinations(range(12),3) if abs(b[:,j].det()) == 1)
    other = [j for j in range(12) if j not in piv]
    bnorm = b[:,piv].inv()*b[:,other+list(piv)]
    assert bnorm[:,-3:] == sp.eye(3)
    v = sp.eye(9).row_join(-bnorm[:,:9].T)
    target = np.array(v.T.tolist(),dtype=int)
    tri = np.triu_indices(9)
    factors = np.where(tri[0] == tri[1],1,2)
    def qrows(vectors):
        return vectors[:,tri[0]]*vectors[:,tri[1]]*factors
    cube = np.array([z for z in product((-1,0,1),repeat=9) if any(z) and next(x for x in z if x)>0],dtype=int)
    constraints = qrows(cube).astype(float)
    eq = qrows(target).astype(float)
    # Minimize common additive slack in the finite minimum inequalities.
    aub = np.column_stack([-constraints,-np.ones(len(cube))])
    aeq = np.column_stack([eq,np.zeros(len(target))])
    cost = np.r_[np.zeros(45),1.0]
    res = linprog(cost,A_ub=aub,b_ub=-np.ones(len(cube)),A_eq=aeq,b_eq=np.ones(len(target)),bounds=[(None,None)]*45+[(0,None)],method='highs')
    item={'record':rec['record'],'dual_vectors':target.tolist(),'finite_cube_pairs':len(cube),'lp_success':bool(res.success),'message':res.message}
    if res.success:
        q = np.zeros((9,9))
        q[tri]=res.x[:45]
        q = q+q.T-np.diag(np.diag(q))
        item.update(slack=float(res.x[-1]),gram=q.tolist(),eigenvalues=np.linalg.eigvalsh(q).tolist())
        if res.x[-1] > 1e-7:
            item['nonzero_inequality_dual']=[{'vector':cube[i].tolist(),'coefficient':float(x)} for i,x in enumerate(res.ineqlin.marginals) if abs(x)>1e-8]
            item['equality_dual']=res.eqlin.marginals.tolist()
    results.append(item)
out={'scope':'Exploratory floating LP, not an exact certificate','results':results}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:v for k,v in x.items() if k not in ['dual_vectors','gram','nonzero_inequality_dual','equality_dual']} for x in results],indent=2))

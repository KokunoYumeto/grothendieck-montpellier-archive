"""Floating discovery of short-vector obstruction or a realizing Gram form.

This is explicitly an exploratory computation. Its results require a
separate exact certificate before any mathematical conclusion.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np
from scipy.optimize import linprog


def canonical(v):
    v=tuple(int(x) for x in v)
    if not any(v): return v
    return v if next(x for x in v if x)>0 else tuple(-x for x in v)


base=Path(__file__).parent
inputs=json.loads((base/'k12_trimodular_lp_explore.json').read_text())['results']
results=[]
for item in inputs:
    target=np.array(item['dual_vectors'],dtype=int)
    target_set={canonical(v) for v in target}
    vectors={canonical(z) for z in product((-1,0,1),repeat=9) if any(z)}-target_set
    tri=np.triu_indices(9)
    factors=np.where(tri[0]==tri[1],1,2)
    def rows(v): return v[:,tri[0]]*v[:,tri[1]]*factors
    eq=np.column_stack([rows(target),np.zeros(len(target))]).astype(float)
    cost=np.r_[np.zeros(45),-1.0]
    result={'record':item['record'],'dual_vectors':item['dual_vectors'],'iterations':[]}
    for iteration in range(60):
        vecs=np.array(sorted(vectors),dtype=int)
        coeff=rows(vecs).astype(float)
        aub=np.column_stack([-coeff,np.ones(len(vecs))])
        res=linprog(cost,A_ub=aub,b_ub=-np.ones(len(vecs)),A_eq=eq,b_eq=np.ones(len(target)),bounds=[(None,None)]*45+[(-1,1)],method='highs')
        if not res.success:
            result['status']='LP failed';result['message']=res.message;break
        q=np.zeros((9,9));q[tri]=res.x[:45];q=q+q.T-np.diag(np.diag(q))
        eig,evec=np.linalg.eigh(q)
        margin=float(res.x[-1])
        result['iterations'].append({'iteration':iteration,'constraint_count':len(vecs),'margin':margin,'min_eigenvalue':float(eig[0])})
        if margin < 1e-8:
            result['status']='nonpositive_margin_candidate'
            result['margin']=margin
            result['inequality_dual']=[{'vector':vecs[i].tolist(),'coefficient':float(x)} for i,x in enumerate(res.ineqlin.marginals) if abs(x)>1e-9]
            result['equality_dual']=res.eqlin.marginals.tolist()
            result['gram']=q.tolist()
            break
        cuts=set()
        for j in range(4):
            for scale in (2,3,4,5,6,8,10,12,16,24,32):
                z=np.rint(scale*evec[:,j]).astype(int)
                if any(z) and float(z@q@z)<1+margin-1e-7:
                    z=canonical(z)
                    if z not in target_set:cuts.add(z)
        if not cuts-vectors:
            if eig[0] < 1e-7:
                result['status']='no_new_integer_eigen_cut';result['gram']=q.tolist();break
            # Fincke--Pohst-style recursion for vectors below the proposed gap.
            upper=np.linalg.cholesky(q).T
            z=np.zeros(9,dtype=int)
            visited=[0]
            threshold=1+margin-1e-6
            def enumerate_short(i,partial):
                visited[0]+=1
                if visited[0]>300000:raise RuntimeError('enumeration node cap')
                if i<0:
                    if any(z):
                        c=canonical(z)
                        if c not in target_set:cuts.add(c)
                    return
                residual=threshold-partial
                if residual < 0:return
                shift=float(upper[i,i+1:]@z[i+1:])
                radius=np.sqrt(residual)/upper[i,i]
                center=-shift/upper[i,i]
                for value in range(int(np.ceil(center-radius-1e-9)),int(np.floor(center+radius+1e-9))+1):
                    z[i]=value
                    term=(upper[i,i]*value+shift)**2
                    enumerate_short(i-1,partial+term)
            try:enumerate_short(8,0.0)
            except RuntimeError:
                result['status']='short_vector_node_cap';result['gram']=q.tolist();break
        fresh=cuts-vectors
        if not fresh:
            result['status']='realization_candidate'
            result['margin']=margin
            result['gram']=q.tolist()
            break
        vectors.update(fresh)
    else:result['status']='iteration_cap'
    results.append(result)
output={'scope':'Floating discovery only. Exact verification and source coverage still required.','results':results}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k not in ['dual_vectors','gram','inequality_dual','equality_dual']} for r in results],indent=2))

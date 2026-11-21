#!/usr/bin/env python3
"""Independent literal E0 replay of the universal fifteen-parameter raw test.

The affine universal word parametrization is an explicit root input.
This certificate constructs actual E0 tables at the origin and fifteen
basis points, evaluates the group recursion directly, and reconstructs
the resulting linear equations independently of analytic coefficient
propagation.  A surviving solution is replayed on every raw tuple.
"""
from pathlib import Path
import json,time
import numpy as np
HERE=Path(__file__).resolve().parent;WORK=HERE.parents[1]
PENT=HERE.parent/'pentagon';CHAR=HERE.parent/'characters'

def solve_rows(A,b):
    rows=np.unique(np.c_[A,b]%3,axis=0).astype(np.int16)
    n=A.shape[1];piv={};selected=[];inconsistent=False
    for original in rows:
        row=original.copy()
        for c,p in sorted(piv.items()):row=(row-int(row[c])*p)%3
        nz=np.flatnonzero(row[:n])
        if not len(nz):
            if row[n]:inconsistent=True
            continue
        c=int(nz[0]);row=row*int(row[c])%3;piv[c]=row;selected.append(original)
    if inconsistent:return None,len(piv),len(rows)
    point=np.zeros(n,dtype=np.int16)
    for c,row in sorted(piv.items(),reverse=True):point[c]=(row[n]-row[:n]@point)%3
    free=[c for c in range(n)if c not in piv];null=np.zeros((n,len(free)),dtype=np.int16)
    for j,c in enumerate(free):
        v=np.zeros(n,dtype=np.int16);v[c]=1
        for k,row in sorted(piv.items(),reverse=True):v[k]=(-row[:n]@v)%3
        null[:,j]=v
    assert np.all((A@point-b)%3==0)and np.all(A@null%3==0)
    return(point,null),len(piv),len(rows)

def run():
    start=time.monotonic()
    invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    mt,iv,els=[invt[k]for k in['multiplication','inverse','elements']];one=6
    src=np.load(WORK/'records/affine216_universal_constraints.npz')
    coeff=src['all_pair_coefficients'];base=src['all_pair_baseline_elements']
    old=np.load(WORK/'records/hurwitz_product_fixed_cover.npz');oldt=old['tuples']
    oldV=np.load(PENT/'hurwitz_raw_survivor_covariance.npz')['V_1_0']
    colored=np.load(PENT/'hurwitz_colored_raw_cover.npz');ct=colored['tuples']
    vp=np.load(PENT/'hurwitz_colored_raw_last_pair.npz')['base_V']
    pot=np.load(PENT/'hurwitz_colored_last_gentle.npz')['potential_0'];I=np.arange(len(ct))
    cV=6*vp[I//6]+(I%6+pot[I//6])%6
    tuples=np.r_[oldt,ct];want=np.r_[oldt[np.argsort(oldV)],ct[np.argsort(cV)]]
    assert np.array_equal(old['group_elements'],els)and np.array_equal(colored['group_elements'],els)
    # The inventory orders the twenty-four linear matrices inside each
    # translation fiber.  Verify the index conversion instead of assuming it.
    assert all(tuple(e[:2])==divmod(j//24,3)for j,e in enumerate(els))
    assert np.array_equal(els[:,2:],np.tile(els[:24,2:],(9,1)))
    def table(case,theta):
        b=base[case];v=(els[b,:2]+np.einsum('abij,j->abi',coeff,theta))%3
        return((3*v[:,:,0]+v[:,:,1])*24+b%24).astype(np.int16)
    def evaluate(ft,t):
        p=t[:,0].copy();out=t[:,:1].copy()
        for k in range(1,t.shape[1]):
            g=t[:,k];d=mt[p,g];F=ft[iv[d],g];J=ft[p,g]
            c=mt[iv[F],J];cs=ft[p,iv[d]]
            assert np.array_equal(c,cs),'The two independent prefix-conjugator expressions disagree.'
            out=mt[mt[c[:,None],out],iv[c][:,None]]
            last=mt[mt[iv[F],g],F]
            out=np.c_[out,last];p=d
        product=np.full(len(t),one,dtype=np.int16)
        for k in range(t.shape[1]):product=mt[product,out[:,k]]
        assert np.array_equal(product,p),'Boundary product was not preserved.'
        return out
    assert np.array_equal(evaluate(np.full((216,216),one,dtype=np.int16),tuples),tuples)
    rows=[];saved={}
    for case in range(4):
        p=src[f'point_{case}'];N=src[f'null_{case}'];d=N.shape[1];assert d==15
        outputs=[evaluate(table(case,p),tuples)]
        for j in range(d):outputs.append(evaluate(table(case,(p+N[:,j])%3),tuples))
        outputs=np.array(outputs)
        assert np.all(els[outputs,2:]==els[outputs[0],2:])
        linear_ok=bool(np.array_equal(els[outputs[0],2:],els[want,2:]))
        const=els[outputs[0],:2];A=((els[outputs[1:],:2]-const)%3).transpose(1,2,3,0)
        rhs=(els[want,:2]-const)%3
        # One non-basis affine point checks the independent reconstruction.
        check=np.arange(d,dtype=np.int16)%3
        actual=evaluate(table(case,(p+N@check)%3),tuples)
        assert np.array_equal(els[actual,:2],(const+np.einsum('nkij,j->nki',A,check))%3)
        row={'linear_case':case,'linear_parts_match':linear_ok}
        if not linear_ok:rows.append(row);print(row,flush=True);continue
        split=len(oldt)
        sol1,rank1,ur1=solve_rows(A[:split].reshape(-1,d),rhs[:split].ravel())
        sol2,rank2,ur2=solve_rows(A.reshape(-1,d),rhs.ravel())
        row.update(original_consistent=sol1 is not None,original_rank=rank1,
                   joint_consistent=sol2 is not None,joint_rank=rank2,
                   original_unique_equations=ur1,joint_unique_equations=ur2)
        if sol1 is not None:row['original_dimension']=sol1[1].shape[1]
        if sol2 is not None:
            q,B=sol2;theta=(p+N@q)%3;null=N@B%3
            exact=evaluate(table(case,theta),tuples);assert np.array_equal(exact,want)
            row['joint_dimension']=B.shape[1];row['all_40320_raw_tuples_exact']=True
            saved[f'point_{case}']=theta;saved[f'null_{case}']=null
            saved[f'table_{case}']=table(case,theta)
        rows.append(row);print(row,flush=True)
    analytic=np.load(WORK/'records/affine216_recursive_raw_constraints.npz')
    for case in[0,1]:
        ap=analytic[f'point_{case}'];an=analytic[f'null_{case}']
        q=saved[f'point_{case}'];B=saved[f'null_{case}']
        assert an.shape==B.shape==(90,9)
        assert solve_rows(an,(q-ap)%3)[0]is not None
        for column in B.T:assert solve_rows(an,column)[0]is not None
    out={'statement':'D23.F44 independent finite replay','universal_parametrization_input':'root universal146-kernel common-word quotient and its four15-dimensional gentle/anchor fibers',
         'original_raw_degree':len(oldt),'colored_raw_degree':len(ct),'cases':rows,
         'identity_control':'PASS','two_prefix_conjugator_implementations':'PASS',
         'independent_affine_reconstruction_control':'PASS','same_affine_fibers_as_analytic_certificate':'PASS',
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Independent literal table evaluation and rank reconstruction. Does not independently reconstruct the root universal common-word quotient or establish actual GT realization.'}
    np.savez_compressed(HERE/'affine216_prefix_recursion_replay.npz',**saved)
    (HERE/'affine216_prefix_recursion_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()

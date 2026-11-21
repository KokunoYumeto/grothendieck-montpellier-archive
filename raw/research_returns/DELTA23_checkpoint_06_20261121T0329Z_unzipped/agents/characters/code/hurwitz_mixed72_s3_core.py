#!/usr/bin/env python3
"""Full induced B=C2*C3 core and gentle norm equations for mixed72 values."""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_mixed72_partial import propagate
HERE=Path(__file__).resolve().parents[1]

def power(a,n):
    if n<0:return power(np.argsort(a),-n)
    out=np.arange(len(a))
    for _ in range(n):out=out[a]
    return out

def induced(x,y):
    data=json.loads((HERE/'records/induced_s4_324.json').read_text())
    edges=data['schreier_cocycles'];n=len(x)
    # Convert the previously certified right-action induction to left actions.
    right=[np.argsort(x),np.argsort(y),x,y];out=[]
    for gen in[0,1]:
        g=[]
        for row in edges:
            edge=row[gen];h=np.arange(n)
            for a in edge['Fword']:h=right[a][h]
            g.extend((n*edge['target']+h).tolist())
        out.append(np.argsort(g))
    s,r=out;assert np.array_equal(power(s,2),np.arange(6*n)) and np.array_equal(power(r,3),np.arange(6*n))
    xx=power(s[r],-2);yy=s[xx[s]]
    assert np.array_equal(xx[:n],x) and np.array_equal(yy[:n],y)
    return s,r,xx,yy

def run():
    start=time.monotonic();d=np.load(HERE/'records/hurwitz_mixed72_partial.npz')
    x,y=d['component_9_pair'];z=np.argsort(x[y]);pairs=[(x,y),(x,z),(y,z),(y,x),(z,y),(z,x)]
    reflection=PermutationGroup([Permutation(np.r_[a,72+b].tolist())
        for a,b in zip([x,y],[x,z])])
    rd=reflection.derived_subgroup()
    assert reflection.order()==2985984 and rd.order()==82944
    wanted={a.astype(np.int16).tobytes():i for i,a in enumerate(d['component_9_R'])}
    theta_rows={}
    for g in rd.generate_schreier_sims():
        a=np.array(g.array_form);i=wanted.get(a[:72].astype(np.int16).tobytes())
        if i is not None:
            assert i not in theta_rows
            theta_rows[i]=a[72:]-72
    assert set(theta_rows)==set(range(16))
    theta=np.array([theta_rows[i]for i in range(16)])
    np.savez_compressed(HERE/'records/hurwitz_mixed72_reflection.npz',theta=theta)
    s,r,xx,yy=induced(x,y);one=np.arange(432)
    maps=[]
    for block in range(6):
        target=[g[72*block:72*(block+1)]-72*block for g in[xx,yy]]
        matches=[]
        for no,pair in enumerate(pairs):
            for image0 in range(72):
                t=propagate(pair,target,[(0,image0)])
                if t is not None:matches.append((no,t));break
        assert len(matches)==1,(block,[i for i,t in matches])
        maps.append(matches[0])
    print('induced core pair orientations',[i for i,t in maps],flush=True)
    G=PermutationGroup([Permutation(g.tolist())for g in[xx,yy]]);D=G.derived_subgroup()
    print('core orders',G.order(),D.order(),flush=True)
    records=[];saved=[]
    for no,a in enumerate(d['component_9_R']):
        t=theta[no];b=t[np.argsort(a)];vals=[a,t,b,np.argsort(a),np.argsort(b),np.argsort(t)]
        blocks=[tr[vals[j][np.argsort(tr)]]for j,tr in maps]
        f=np.concatenate([72*k+b for k,b in enumerate(blocks)])
        member=D.contains(Permutation(f.tolist()))
        norm2=np.array_equal(power(s[f],2),one)
        norm3=np.array_equal(power(np.argsort(f)[r],3),one)
        zz=np.argsort(xx[yy])
        # Evaluate f(y,z),f(z,x) in the induced quotient by conjugation.
        # r may orient the cycle either way; inspect its action explicitly.
        ri=np.argsort(r)
        if np.array_equal(r[xx[ri]],yy) and np.array_equal(r[yy[ri]],zz):
            f_yz=r[f[ri]];r2=r[r];f_zx=r2[f[np.argsort(r2)]]
        elif np.array_equal(ri[xx[r]],yy) and np.array_equal(ri[yy[r]],zz):
            f_yz=ri[f[r]];r2=ri[ri];f_zx=r2[f[np.argsort(r2)]]
        else:raise AssertionError('Unexpected cyclic marking')
        neg=np.array_equal(f_zx[np.argsort(zz)[f_yz[np.argsort(yy)[f[np.argsort(xx)]]]]],one)
        records.append({'R_index':no,'derived_member':bool(member),'two_cycle':bool(norm2),'three_cycle':bool(norm3),'negative_three_cycle':bool(neg)})
        if member and norm2 and norm3 and neg:saved.append((no,f))
    out={'statement':'D23.C27 probe','core_order':int(G.order()),'core_derived_order':int(D.order()),
        'induced_pair_orientations':[i for i,t in maps],'cases':records,'passes':[i for i,f in saved],
        'elapsed_seconds':time.monotonic()-start,
        'scope':'Exact induced six-coset finite gentle norms and common commutator word. Does not construct a profinite gentle lift.'}
    (HERE/'records/hurwitz_mixed72_s3_core.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'records/hurwitz_mixed72_s3_core.npz',s=s,r=r,x=xx,y=yy,
        intertwiners=np.array([t for i,t in maps]),orientations=np.array([i for i,t in maps]),
        passing_R_indices=np.array([i for i,f in saved]),passing_f=np.array([f for i,f in saved]))
    fibers=np.load(HERE/'records/hurwitz_mixed_derived_fibers.npz')
    cent=PermutationGroup([Permutation(g.tolist())for g in fibers['derived_centralizer_generators']])
    assert cent.order()==432
    orb=d['component_9_orbit'];ix=np.full(1344,-1,dtype=int);ix[orb]=np.arange(72)
    local=np.array([ix[np.array(g.array_form)[orb]]for g in cent.generate_schreier_sims()])
    assert len(np.unique(local,axis=0))==2
    allowed={i for i,f in saved};fiber_rows=[]
    for no,g in enumerate(fibers['derived_representatives']):
        a=ix[g[orb]];values=a[local]
        indices=[wanted[v.astype(np.int16).tobytes()]for v in values]
        good=sum(i in allowed for i in indices)
        assert good==432
        fiber_rows.append({'index':no,'R72_counts':{str(i):indices.count(i)for i in sorted(set(indices))},'S3_passes':good})
    (HERE/'records/hurwitz_mixed72_s3_fibers.json').write_text(json.dumps({
        'derived_centralizer_order':432,'R72_centralizer_image_order':2,
        'allowed_R72_indices':sorted(allowed),'fibers':fiber_rows},indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()

#!/usr/bin/env python3
"""Exact B4/Z Hurwitz action on GL2(F3) quadruples of product one, modulo conjugacy."""
import itertools,json,pathlib,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

def run(product=(1,0,0,1)):
    st=time.monotonic();els=[v for v in itertools.product(range(3),repeat=4) if (v[0]*v[3]-v[1]*v[2])%3];idx={v:j for j,v in enumerate(els)};n=len(els);one=idx[(1,0,0,1)]
    def mm(a,b):return ((a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,(a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3)
    mt=np.array([[idx[mm(a,b)] for b in els] for a in els],dtype=np.int16);iv=[next(j for j in range(n) if mt[i,j]==one) for i in range(n)]
    p0=idx[product];cent=[g for g in range(n) if mt[g,p0]==mt[p0,g]]
    con=np.array([[mt[mt[g,a],iv[g]] for a in range(n)] for g in cent],dtype=np.int16)
    classes=np.full(n**3,-1,dtype=np.int32);reps=[]
    for code in range(n**3):
        if classes[code]>=0:continue
        i=code//n**2;j=code//n%n;k=code%n;l=int(mt[iv[mt[mt[i,j],k]],p0])
        triple=con[:,[i,j,k]];codes=triple[:,0].astype(int)*n*n+triple[:,1]*n+triple[:,2]
        classes[codes]=len(reps);reps.append((i,j,k,l))
    reps=np.array(reps,dtype=np.int16);N=len(reps);perms=[]
    for s in range(3):
        a=reps.copy();u=a[:,s].copy();v=a[:,s+1].copy()
        a[:,s]=mt[mt[u,v],np.array(iv)[u]];a[:,s+1]=u
        codes=a[:,0].astype(int)*n*n+a[:,1]*n+a[:,2];p=classes[codes]
        assert len(set(p))==N;perms.append(p)
    comp=lambda p,q:p[q]
    assert np.array_equal(comp(comp(perms[0],perms[1]),perms[0]),comp(comp(perms[1],perms[0]),perms[1]))
    assert np.array_equal(comp(comp(perms[1],perms[2]),perms[1]),comp(comp(perms[2],perms[1]),perms[2]))
    assert np.array_equal(comp(perms[0],perms[2]),comp(perms[2],perms[0]))
    z=comp(comp(perms[0],perms[1]),perms[2]);z=comp(comp(comp(z,z),z),z);assert np.array_equal(z,np.arange(N))
    # Separate connected Nielsen components before doing any group calculations.
    covered=set();orbits=[]
    for a in range(N):
        if a in covered:continue
        orbit=[a];covered.add(a);cur=0
        while cur<len(orbit):
            x=orbit[cur];cur+=1
            for p in perms:
                y=int(p[x])
                if y not in covered:covered.add(y);orbit.append(y)
        orbits.append(orbit)
    def generated_order(tup):
        gs=list(tup[:3]);seen={one};todo=[one];cur=0
        while cur<len(todo):
            a=todo[cur];cur+=1
            for b in gs:
                c=int(mt[a,b])
                if c not in seen:seen.add(c);todo.append(c)
        return len(seen)
    rows=[]
    for orbit in sorted(orbits,key=len):
        go=generated_order(reps[orbit[0]])
        if go!=n:continue
        vi={v:j for j,v in enumerate(orbit)};ps=[Permutation([vi[int(p[v])] for v in orbit]) for p in perms]
        pg=PermutationGroup([ps[0]**2,ps[1]**2]);series=pg.derived_series();orders=[int(g.order()) for g in series]
        row={'orbit_size':len(orbit),'representative':[els[j] for j in reps[orbit[0]]],'first_pair_derived':orders,'second_derived_nilpotent':bool(series[min(2,len(series)-1)].is_nilpotent),'can_surject_EF_by_order':orders[0]%1944==0}
        rows.append(row);print(json.dumps(row),flush=True)
    out={'group':'GL2(F3)','group_order':n,'fixed_product':product,'product_centralizer_order':len(cent),'conjugacy_classes_of_fixed_product_quadruples':N,'B4_orbit_count':len(orbits),'generating_components':rows,'central_full_twist_identity':True,'elapsed_seconds':time.monotonic()-st}
    fn='hurwitz_gl2_probe.json' if p0==one else 'hurwitz_gl2_noncentral.json'
    pathlib.Path(__file__).with_name(fn).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='generating_components'}),flush=True)
if __name__=='__main__':run()

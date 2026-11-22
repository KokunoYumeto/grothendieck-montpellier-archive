"""Exploratory basis-volume search for tripartite incidence torsion.

No positivity condition is imposed. Floating point proposes exchanges;
every recorded determinant and Smith form is recomputed exactly by SymPy.
The purpose is to seek a boundary gadget, not to assert an upper bound.
"""
import argparse,itertools,json,time,math
from pathlib import Path
import numpy as np
from fractions import Fraction as F
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

p=argparse.ArgumentParser();p.add_argument('--n',type=int,required=True)
p.add_argument('--restarts',type=int,default=1000);p.add_argument('--steps',type=int,default=80)
p.add_argument('--seed',type=int,default=45);p.add_argument('--out',required=True)
p.add_argument('--gadget-search',action='store_true')
a=p.parse_args();n=a.n;r=3*n-2;target=2**n
edges=list(itertools.product(range(n),repeat=3));A=np.zeros((3*n,n**3),dtype=np.int64)
for j,e in enumerate(edges):
    for h,v in enumerate(e):A[h*n+v,j]=1
rows=list(range(n))+list(range(n,2*n-1))+list(range(2*n,3*n-1));AA=A[rows]
rng=np.random.default_rng(a.seed);best=0;records=[];hits=[];seenhits=set();start=time.time();success=False
for restart in range(a.restarts):
    while True:
        basis=list(rng.choice(n**3,r,False));d=round(np.linalg.det(AA[:,basis]))
        if d:break
    for step in range(a.steps):
        U=np.linalg.solve(AA[:,basis],AA);DD=np.rint(d*U).astype(np.int64)
        maxdet=int(abs(DD).max())
        if maxdet>best:
            i,j=np.unravel_index(np.argmax(abs(DD)),DD.shape);nb=basis.copy();nb[i]=j
            exact=int(Matrix(AA[:,nb]).det());assert abs(exact)==maxdet
            best=maxdet;record={'restart':restart,'step':step,'determinant':exact,'support':[edges[k] for k in nb]}
            records.append(record);print(json.dumps({'maximum_index_found':best,'restart':restart,'seconds':time.time()-start}),flush=True)
        for i,j in np.argwhere((DD!=0)&(abs(DD)%target==0)):
            nb=basis.copy();nb[i]=int(j);key=tuple(sorted(nb))
            if key in seenhits:continue
            seenhits.add(key)
            S=smith_normal_form(Matrix(A[:,nb]),domain=ZZ)
            smith=[abs(int(S[k,k])) for k in range(r)]
            record={'determinant':int(DD[i,j]),'support':[edges[k] for k in nb],'smith':smith}
            assert math.prod(smith)==abs(record['determinant'])
            if a.gadget_search and (smith[-1]&-smith[-1])>=target:
                dd=abs(record['determinant']);adj=Matrix(AA[:,nb]).inv()*dd
                assert all(v.q==1 for v in adj)
                adj=np.array(adj.tolist(),dtype=np.int64)
                assert np.array_equal(AA[:,nb]@adj,np.eye(r,dtype=np.int64)*dd)
                qnum=adj@np.ones(r,dtype=np.int64);unum=adj@AA
                record['uniform_numerators']=list(map(int,qnum))
                record['uniform_denominator']=dd
                feasible=[]
                for column in range(n**3):
                    u=unum[:,column]
                    divisor=math.gcd(dd,*list(map(int,u)));uden=dd//divisor
                    if (uden&-uden)<target:continue
                    lo=F(0);hi=F(1)
                    for x,y in zip(qnum-u,u):
                        if y>0:lo=max(lo,F(-int(x),int(y)))
                        elif y<0:hi=min(hi,F(-int(x),int(y)))
                        elif x<=0:lo=F(2);break
                    if lo<hi:
                        feasible.append({'boundary':edges[column],'interval':[str(lo),str(hi)],'derivative_denominator':uden})
                record['amplifying_boundaries']=feasible
                record['free_support']=all(len(set((e[i],e[j])for e in record['support']))==r for i,j in [(0,1),(0,2),(1,2)])
                if feasible or (np.all(qnum>0) and (dd//math.gcd(dd,*list(map(int,qnum))) & -(dd//math.gcd(dd,*list(map(int,qnum)))))>=target):
                    success=True
                    print('PROMISING POSITIVE CANDIDATE',json.dumps(record),flush=True)
            hits.append(record);print('HIT',json.dumps({'determinant':record['determinant'],'last_smith':smith[-1],'boundary_count':len(record.get('amplifying_boundaries',[]))}),flush=True)
        score=np.log(abs(DD)+0.01)+rng.gumbel(size=DD.shape)*0.10
        for j in basis:score[:,j]=-100
        i,j=np.unravel_index(np.argmax(score),score.shape);basis[i]=j;d=int(DD[i,j])
    if success or (not a.gadget_search and any((hit['smith'][-1] & -hit['smith'][-1])>=target for hit in hits)):break
    if restart%100==99:print(json.dumps({'progress_restarts':restart+1,'seconds':time.time()-start}),flush=True)
result={'scope':'Nonexhaustive volume-biased basis search; every recorded determinant and Smith form exact',
        'n':n,'restarts':restart+1,'steps_each':a.steps,'seed':a.seed,'maximum_index_found':best,
        'records':records,'dyadic_index_hits':hits,'elapsed':time.time()-start}
Path(a.out).write_text(json.dumps(result,indent=2))
print('DONE',best,'dyadic hits',len(hits),'seconds',time.time()-start)

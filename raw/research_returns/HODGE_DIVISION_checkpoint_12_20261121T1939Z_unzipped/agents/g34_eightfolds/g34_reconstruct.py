#!/usr/bin/env python3
"""Independent exact reconstruction from ten roots, doubled tuple and intervals.
Inputs: Severn, Hexagon 2610.00387v2, internal v1.5, Appendix A (numerical data).
Methods: parabolic group cocycles and Dehn twist pullback; exact Q(omega).
No printed Gram or monodromy matrices are input.
"""
from fractions import Fraction as Q
from itertools import product,combinations
import json,time
from pathlib import Path

class F:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,F): self.a,self.b=a.a,a.b
        else: self.a,self.b=Q(a),Q(b)
    def __add__(x,y):
        y=F(y);return F(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x):return F(-x.a,-x.b)
    def __sub__(x,y):return x+-F(y)
    def __rsub__(x,y):return F(y)+-x
    def __mul__(x,y):
        y=F(y);return F(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a-x.b*y.b)
    __rmul__=__mul__
    def inv(x):
        d=x.a*x.a-x.a*x.b+x.b*x.b
        if d==0:raise ZeroDivisionError
        return F((x.a-x.b)/d,-x.b/d)
    def __truediv__(x,y):return x*F(y).inv()
    def __rtruediv__(x,y):return F(y)*x.inv()
    def conj(x):return F(x.a-x.b,-x.b)
    def __bool__(x):return bool(x.a or x.b)
    def __eq__(x,y):
        try:y=F(y)
        except:return False
        return x.a==y.a and x.b==y.b
    def __hash__(x):return hash((x.a,x.b))
    def __repr__(x):return str(x.a) if not x.b else f'({x.a})+({x.b})*w'
    def pair(x):return [str(x.a),str(x.b)]
Z=F();ONE=F(1);w=F(0,1)

def mat(a):return [[F(x) for x in row] for row in a]
def zero(r,c):return [[Z for _ in range(c)]for _ in range(r)]
def eye(n):return [[F(i==j)for j in range(n)]for i in range(n)]
def tr(a):return [list(x)for x in zip(*a)]
def star(a):return [[x.conj()for x in row]for row in tr(a)]
def add(a,b):return [[x+y for x,y in zip(r,s)]for r,s in zip(a,b)]
def sub(a,b):return [[x-y for x,y in zip(r,s)]for r,s in zip(a,b)]
def scale(a,c):return [[x*c for x in r]for r in a]
def mul(a,b):
    bt=tr(b);return [[sum((x*y for x,y in zip(row,col)),Z)for col in bt]for row in a]
def mv(a,v):return [sum((x*y for x,y in zip(row,v)),Z)for row in a]
def outer(v,u):return [[x*y for y in u]for x in v]
def dot(v,u):return sum((x.conj()*y for x,y in zip(v,u)),Z)
def rref(a):
    a=[r[:]for r in a];pivs=[];rr=0
    for j in range(len(a[0])):
        piv=next((i for i in range(rr,len(a))if a[i][j]),None)
        if piv is None:continue
        a[rr],a[piv]=a[piv],a[rr]
        a[rr]=[x/a[rr][j]for x in a[rr]]
        for i in range(len(a)):
            if i!=rr and a[i][j]:
                c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[rr])]
        pivs.append(j);rr+=1
        if rr==len(a):break
    return a,pivs

def rank(a):return len(rref(a)[1])
def inv(a):
    n=len(a);rr,p=rref([r+s for r,s in zip(a,eye(n))]);assert p[:n]==list(range(n));return [r[n:]for r in rr]
def det(a):
    a=[r[:]for r in a];d=ONE;n=len(a)
    for j in range(n):
        p=next((i for i in range(j,n)if a[i][j]),None)
        if p is None:return Z
        if p!=j:a[j],a[p]=a[p],a[j];d=-d
        d=d*a[j][j]
        for i in range(j+1,n):
            c=a[i][j]/a[j][j]
            for k in range(j+1,n):a[i][k]=a[i][k]-c*a[j][k]
    return d

def serialize(a):return [[x.pair()for x in row]for row in a]
def iszero(a):return all(not x for row in a for x in row)

def main(group_order=False):
    started=time.time()
    roots=mat([[1,-1-w,1,w,-1-w,w],[1,0,0,1+w,0,0],
      [0,1,1+w,0,0,0],[1,w,-1-w,w,-1-w,1],
      [1,-1-w,-1-w,-1-w,-1-w,w],[1,-1-w,w,w,w,w],
      [0,0,1,0,0,-1],[1,w,w,-1-w,1,-1-w],
      [1,-w,0,0,0,0],[0,1,0,0,0,-1]])
    norms=[dot(v,v)for v in roots]
    S=[sub(eye(6),scale(outer(v,[x.conj()for x in v]),2/d))for v,d in zip(roots,norms)]
    assert all(mul(s,s)==eye(6)for s in S)
    assert rank(roots)==6
    seen={0}
    while True:
        more={j for i in seen for j in range(10)if dot(roots[i],roots[j])}
        if more<=seen:break
        seen|=more
    assert len(seen)==10
    print('root span 6; nonorthogonality graph connected; absolute irreducibility proved',flush=True)
    # Explicit published Davis/Mitchell root set, all 756 roots of norm 2.
    phases=[ONE,w,w*w];rootset=set()
    for i in range(6):
      for j in range(6):
       if i!=j:
        for a,b in product(range(3),repeat=2):
         v=[Z]*6;v[i]=phases[a];v[j]=-phases[b];rootset.add(tuple(v))
    sq=1+2*w
    for aa in product(range(3),repeat=5):
      aa=aa+((-sum(aa))%3,)
      v=tuple(phases[x]/sq for x in aa)
      rootset.add(v);rootset.add(tuple(-x for x in v))
    assert len(rootset)==756 and all(dot(v,v)==2 for v in rootset)
    rootlist=sorted(rootset,key=lambda v:tuple((x.a,x.b)for x in v));idx={v:i for i,v in enumerate(rootlist)}
    perms=[]
    for s in S:
      p=[idx[tuple(mv(s,v))]for v in rootlist]
      assert len(set(p))==756
      perms.append(p)
    print('ten reflections preserve published 756-root set',flush=True)
    # Orbit certificate: every root lies in the orbit of rootlist[0].
    orbit={0};todo=[0]
    while todo:
      i=todo.pop()
      for p in perms:
        j=p[i]
        if j not in orbit:orbit.add(j);todo.append(j)
    assert len(orbit)==756
    result={'root_count':756,'root_orbit_size':len(orbit),'root_rank':6,'nonorthogonality_connected':True}
    if group_order:
      from sympy.combinatorics import Permutation,PermutationGroup
      G=PermutationGroup([Permutation(p)for p in perms]);print('computing exact permutation group order',flush=True)
      order=G.order();assert order==39191040
      result['group_order']=int(order)
      result['permutation_base']=[int(x)for x in G.base]
      result['basic_orbit_lengths']=[len(x)for x in G.basic_orbits]
      result['scalar_membership']={str(a):bool(G.contains(Permutation([idx[tuple(a*x for x in v)]for v in rootlist])))for a in [ONE,-ONE,w,-w,w*w,-w*w]}
      assert all(result['scalar_membership'].values())
      print('group order',order,'; all six scalar units present',flush=True)
    # Coefficient model of parabolic cocycles: u_i=lambda_i*v_ceil(i/2).
    vv=[v for v in roots for _ in (0,1)];tt=[s for s in S for _ in (0,1)]
    prefixes=[];p=eye(6)
    for t in tt:prefixes.append(p);p=mul(p,t)
    assert p==eye(6)
    relation=tr([mv(p,v)for p,v in zip(prefixes,vv)])
    cob=[[2*x.conj()/dot(v,v)for x in v]for v in vv]
    assert rank(relation)==rank(cob)==6 and iszero(mul(relation,cob))
    B=zero(20,8)
    for k in range(4):B[2*k][k]=B[2*k+1][k]=ONE
    indices=[0,2,4,6,9,11,13,15,17,19]
    last=mat([[1,0,0,0,1+w,1,0,-1-w,0,-1+w],
       [0,1,0,0,1+w,Q(2,3)-Q(2,3)*w,-1,-Q(2,3)-Q(1,3)*w,0,1+2*w],
       [0,0,1,0,-Q(1,3)-Q(2,3)*w,-Q(2,3)-Q(1,3)*w,1+w,0,1+w,-w],
       [0,0,0,1,1+w,1,-2-w,-1-w,0,3*w]])
    for k in range(4):
      for i,a in zip(indices,last[k]):B[i][k+4]=a
    assert iszero(mul(relation,B))
    E=[r+s for r,s in zip(B,cob)];assert rank(E)==14
    pivotrows=rref(tr(E))[1];Einv=inv([E[i]for i in pivotrows])
    print('parabolic relation rank6, coboundary rank6, total basis rank14; quotient dim8',flush=True)
    # Cup pairing, with a_i=u_i/2 because the inertia matrices are involutions.
    basis=[]
    for b in tr(B):basis.append([[lam*x for x in v]for lam,v in zip(b,vv)])
    cup=zero(8,8)
    for a,uu in enumerate(basis):
      F=[Z]*6
      for i in range(20):
        val=[x+y/2 for x,y in zip(mv(star(prefixes[i]),F),uu[i])]
        for b,ww in enumerate(basis):cup[a][b]=cup[a][b]+dot(val,ww[i])
        F=[x+y for x,y in zip(F,mv(prefixes[i],uu[i]))]
      assert not any(F)
    assert add(cup,star(cup))==zero(8,8) and rank(cup)==8
    assert [r[:4]for r in cup[:4]]==zero(4,4)
    intervals=[(1,8,1),(1,18,1),(2,8,2),(3,8,1),(4,8,2),(5,6,1),(5,8,1),(7,8,1),(9,10,1),(9,12,1),(9,16,1),(9,17,2),(9,18,1),(11,12,1),(13,14,1),(13,16,1),(15,16,1)]
    # Laminarity guarantees simultaneous pinching; r-3 distinct curves give a maximal boundary.
    assert all(b<c or d<a or (a<=c and d<=b)or(c<=a and b<=d)for(a,b,k),(c,d,l)in combinations(intervals,2))
    Ns=[];Xs=[];ranks=[];semidefinite=[]
    for a,b,k in intervals:
      a-=1;b-=1
      prods=[];c=eye(6)
      for i in range(a,b+1):prods.append(c);c=mul(c,tt[i])
      if k==1:assert c==eye(6)
      else:
        assert mul(c,c)==eye(6)
        assert any(mul(c,tt[i])!=mul(tt[i],c)for i in range(a,b+1))
      # u(c^k)=(1+c+...+c^(k-1))*u(c), c^k=1 for these intervals.
      power_sum=eye(6)if k==1 else add(eye(6),c)
      transformed=zero(20,8)
      for col,uu in enumerate(basis):
        u_c=[Z]*6
        for p,i in zip(prods,range(a,b+1)):u_c=[x+y for x,y in zip(u_c,mv(p,uu[i]))]
        u_ck=mv(power_sum,u_c)
        for i in range(20):
          u=uu[i]
          if a<=i<=b:u=[x+y for x,y in zip(u,mv(sub(eye(6),tt[i]),u_ck))]
          h=next(j for j,x in enumerate(vv[i])if x)
          lam=u[h]/vv[i][h]
          assert u==[lam*x for x in vv[i]]
          transformed[i][col]=lam
      assert iszero(mul(relation,transformed))
      coeff=mul(Einv,[transformed[i]for i in pivotrows]);assert mul(E,coeff)==transformed
      T=coeff[:8];N=sub(T,eye(8));assert iszero(mul(N,N))
      assert mul(star(T),mul(cup,T))==cup
      assert [r[:4]for r in N]==zero(8,4) and N[4:]==zero(4,8)
      X=[r[4:]for r in N[:4]];beta=[r[4:]for r in mul(cup,N)[4:]]
      assert star(beta)==beta
      minus=scale(beta,-1)
      minors=[]
      for size in range(1,5):
        for jj in combinations(range(4),size):
          dd=det([[minus[i][j]for j in jj]for i in jj]);assert not dd.b and dd.a>=0;minors.append(str(dd.a))
      Ns.append(N);Xs.append(X);ranks.append(rank(N));semidefinite.append(minors)
    assert all(iszero(mul(N,M))for N in Ns for M in Ns)
    expected=[4,1,3,3,2,1,2,1,1,2,4,4,4,1,1,2,1]
    assert ranks==expected
    rational=mat([[c for row in X for x in row for c in (x.a,x.b)]for X in Xs]);span=rank(rational);assert span==16
    # Exact nonzero minor chosen by independent row/column elimination.
    rows=rref(tr(rational))[1];cols=rref([rational[i]for i in rows])[1]
    minor=det([[rational[i][j]for j in cols]for i in rows]);assert minor
    overK=[[x for row in X for x in row]for X in Xs]
    krows=rref(tr(overK))[1];assert len(krows)==16
    kminor=det([overK[i]for i in krows]);assert kminor==1728
    total=zero(4,4)
    for N in Ns:total=sub(total,[r[4:]for r in mul(cup,N)[4:]])
    leading=[det([r[:k]for r in total[:k]])for k in range(1,5)]
    assert all(not x.b and x.a>0 for x in leading)
    result.update({'parabolic_dimension':len(tt)-rank(relation)-rank(cob),'hodge_numbers_by_chevalley_weil':[-6+len(tt)//2]*2,'hurwitz_dimension':len(tt)-3,'monodromy_block_complex_span_rank':len(krows),'gram':serialize(cup),
        'intervals':intervals,'monodromy_blocks':[serialize(X)for X in Xs],'nilpotent_ranks':ranks,
        'rational_span_rank':span,'span_minor_rows':[i+1 for i in rows],'span_minor_columns':[i+1 for i in cols],
        'span_minor_det':str(minor),'K_span_minor_rows':[i+1 for i in krows],'K_span_minor_det':str(kminor),'negative_sum_leading_minors':[str(x)for x in leading],
        'negative_block_principal_minors':semidefinite,'elapsed_seconds':time.time()-started})
    print('nilpotent ranks:',ranks,flush=True)
    print('rational span rank:',span,'; nonzero minor:',minor,flush=True)
    print('K-span minor determinant:',kminor,flush=True)
    print('negative sum leading minors:',leading,flush=True)
    Path(__file__).with_name('g34_reconstruction_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL EXACT CHECKS PASSED',flush=True)
    return result
if __name__=='__main__':
    import sys
    main('--group-order' in sys.argv)

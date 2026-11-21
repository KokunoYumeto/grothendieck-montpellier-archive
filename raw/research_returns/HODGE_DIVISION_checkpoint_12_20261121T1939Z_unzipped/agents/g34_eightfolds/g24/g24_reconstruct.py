#!/usr/bin/env python3
"""Exact parabolic-cocycle search for G24 over Q(t), t^2+t+2=0.
Published matrix seed: Deraux, Non-arithmetic lattices and the Klein quartic, eq(13), p=2.
No unrefereed dominance or numerical input is used.
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
        y=F(y);return F(x.a*y.a-2*x.b*y.b,x.a*y.b+x.b*y.a-x.b*y.b)
    __rmul__=__mul__
    def inv(x):
        d=x.a*x.a-x.a*x.b+2*x.b*x.b
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

def nullspace(a):
    rr,p=rref(a);free=[j for j in range(len(a[0]))if j not in p];vs=[]
    for f in free:
      v=[Z]*len(a[0]);v[f]=ONE
      for i,j in enumerate(p):v[j]=-rr[i][f]
      vs.append(v)
    return tr(vs)

H=mat([[2,-w,w.conj()],[-w.conj(),2,-w],[w,-w.conj(),2]])
def hdot(v,u):return dot(v,mv(H,u))
def reflection(v):
    return sub(eye(3),scale(outer(v,mv(tr(H),[x.conj()for x in v])),2/hdot(v,v)))
def key(a):return tuple(tuple(r)for r in a)

def group():
    ss=[reflection(v)for v in eye(3)]
    assert ss==[mat([[-1,w,-w.conj()],[0,1,0],[0,0,1]]),
      mat([[1,0,0],[w.conj(),-1,w],[0,0,1]]),
      mat([[1,0,0],[0,1,0],[-w,w.conj(),-1]])]
    assert [det([r[:i]for r in H[:i]])for i in range(1,4)]==[2,2,1]
    from collections import deque
    gg={key(eye(3)):[]};todo=deque([eye(3)])
    while todo:
      a=todo.popleft()
      for j,s in enumerate(ss):
        b=mul(a,s);k=key(b)
        if k not in gg:gg[k]=gg[key(a)]+[j+1];todo.append(b)
    assert len(gg)==336
    assert all(mul(star(list(g)),mul(H,list(g)))==H for g in gg)
    rr={tuple(mv(g,[ONE,Z,Z]))for g in gg};assert len(rr)==42
    roots=[]
    for v in sorted(rr,key=lambda v:tuple((x.a,x.b)for x in v)):
      if tuple(-x for x in v)not in roots:roots.append(v)
    assert len(roots)==21
    assert all(key(reflection(v))in gg for v in roots)
    return roots,gg

def compute(roots,intervals,verbose=False):
    s=[reflection(v)for v in roots];vv=[v for v in roots for _ in (0,1)];tt=[t for t in s for _ in (0,1)];r=len(tt)
    n=r//2-3;assert n==3
    prefixes=[];p=eye(3)
    for t in tt:prefixes.append(p);p=mul(p,t)
    assert p==eye(3)
    rel=tr([mv(p,v)for p,v in zip(prefixes,vv)])
    cob=[[2*x/hdot(v,v)for x in mv(tr(H),[a.conj()for a in v])]for v in vv]
    if rank(rel)!=3 or rank(cob)!=3:return None
    assert iszero(mul(rel,cob))
    pair=zero(r,r//2)
    for j in range(r//2):pair[2*j][j]=pair[2*j+1][j]=ONE
    ex=[row[:]for row in cob];I=[]
    for v in tr(pair):
      new=[row+[x]for row,x in zip(ex,v)]
      if rank(new)>rank(ex):ex=new;I.append(v)
    assert len(I)==3
    B=I[:]
    for v in tr(nullspace(rel)):
      new=[row+[x]for row,x in zip(ex,v)]
      if rank(new)>rank(ex):ex=new;B.append(v)
    assert len(B)==6
    B=tr(B);E=[r+s for r,s in zip(B,cob)];piv=rref(tr(E))[1];Ei=inv([E[i]for i in piv])
    basis=[[[lam*x for x in v]for lam,v in zip(b,vv)]for b in tr(B)]
    cup=zero(6,6)
    for a,uu in enumerate(basis):
      f=[Z]*3
      for i in range(r):
        val=[x+y/2 for x,y in zip(mv(inv(prefixes[i]),f),uu[i])]
        for b,ww in enumerate(basis):cup[a][b]=cup[a][b]+hdot(val,ww[i])
        f=[x+y for x,y in zip(f,mv(prefixes[i],uu[i]))]
      assert not any(f)
    assert add(cup,star(cup))==zero(6,6)and rank(cup)==6
    assert all(b<c or d<a or(a<=c and d<=b)or(c<=a and b<=d)for(a,b),(c,d)in combinations(intervals,2))
    Ns=[];Xs=[];orders=[];betas=[]
    for a,b in intervals:
      a-=1;b-=1;prods=[];c=eye(3)
      for i in range(a,b+1):prods.append(c);c=mul(c,tt[i])
      power=eye(3);power_sum=zero(3,3)
      for k in range(1,337):
        power_sum=add(power_sum,power);power=mul(power,c)
        if power==eye(3):break
      else:raise ValueError('nonfinite interval product')
      orders.append(k)
      transformed=zero(r,6)
      for col,uu in enumerate(basis):
        uc=[Z]*3
        for p,i in zip(prods,range(a,b+1)):uc=[x+y for x,y in zip(uc,mv(p,uu[i]))]
        uck=mv(power_sum,uc)
        for i in range(r):
          u=uu[i]
          if a<=i<=b:u=[x+y for x,y in zip(u,mv(sub(eye(3),tt[i]),uck))]
          j=next(j for j,x in enumerate(vv[i])if x);lam=u[j]/vv[i][j]
          assert u==[lam*x for x in vv[i]]
          transformed[i][col]=lam
      assert iszero(mul(rel,transformed))
      coeff=mul(Ei,[transformed[i]for i in piv]);assert mul(E,coeff)==transformed
      T=coeff[:6];N=sub(T,eye(6))
      assert iszero(mul(N,N))and mul(star(T),mul(cup,T))==cup
      if not(iszero([r[:3]for r in N])and iszero(N[3:])):return None
      Ns.append(N);Xs.append([r[3:]for r in N[:3]])
      beta=[r[3:]for r in mul(cup,N)[3:]];assert star(beta)==beta
      betas.append(beta)
    assert all(iszero(mul(N,M))for N in Ns for M in Ns)
    kk=[[x for row in X for x in row]for X in Xs];rnk=rank(kk)
    result={'roots':serialize(roots),'basis':serialize(B),'gram':serialize(cup),'intervals':intervals,'orders':orders,'monodromy_blocks':[serialize(X)for X in Xs],'nilpotent_ranks':[rank(N)for N in Ns],'K_span_rank':rnk}
    if rnk==9:
      result['K_minor_det']=det(kk).pair()
      total=zero(3,3);allmins=[]
      for beta in betas:
        minus=scale(beta,-1);allmins.append([])
        for size in range(1,4):
          for inds in combinations(range(3),size):
            d=det([[minus[i][j]for j in inds]for i in inds]);assert not d.b and d.a>=0;allmins[-1].append(str(d.a))
        total=add(total,minus)
      result['negative_principal_minors']=allmins
      result['negative_sum_leading_minors']=[str(det([r[:k]for r in total[:k]]))for k in range(1,4)]
    return result

def search():
    import random
    started=time.time();rr,gg=group();print('exact group order336, root count42, projective roots21',flush=True)
    random.seed(20261121)
    intervals=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(1,4),(5,8),(1,8)]
    counts={}
    for trial in range(1000):
      inds=random.sample(range(21),6);roots=[rr[i]for i in inds]
      res=compute(roots,intervals)
      if res is None:continue
      counts[res['K_span_rank']]=counts.get(res['K_span_rank'],0)+1
      if trial%10==0:print('trial',trial,'ranks',counts,flush=True)
      if res['K_span_rank']==9:
        subg={key(eye(3))};todo=[eye(3)];ss=[reflection(v)for v in roots]
        while todo:
          a=todo.pop()
          for s in ss:
            b=mul(a,s)
            if key(b)not in subg:subg.add(key(b));todo.append(b)
        if len(subg)!=336:continue
        res.update({'group_order':336,'root_count':42,'projective_root_count':21,'selected_root_indices':[i+1 for i in inds],'trial':trial,'seed':20261121,'elapsed_seconds':time.time()-started,'parabolic_dimension':6,'hodge_numbers_by_chevalley_weil':[3,3],'hurwitz_dimension':9,'curve_genus':673,'all_roots':serialize(rr)})
        Path(__file__).with_name('g24_reconstruction_result.json').write_text(json.dumps(res,indent=2)+'\n')
        print('SUCCESS',res['K_minor_det'],res['negative_sum_leading_minors'],flush=True)
        return
    print('no witness',counts)

def main():
    started=time.time();rr,gg=group()
    roots=mat([[0,-1,1+w],[-1,0,w],[-2,w,1+w],[-1-w,-2,w],[-1,0,0],[-1,-1,w]])
    assert all(tuple(v)in rr for v in roots)
    ss=[reflection(v)for v in roots]
    assert rank(roots)==3
    seen={0}
    while True:
      more={j for i in seen for j in range(6)if hdot(roots[i],roots[j])}
      if more<=seen:break
      seen|=more
    assert len(seen)==6
    subg={key(eye(3))};todo=[eye(3)]
    while todo:
      a=todo.pop()
      for s in ss:
        b=mul(a,s)
        if key(b)not in subg:subg.add(key(b));todo.append(b)
    assert len(subg)==336 and subg==set(gg)
    print('fixed six reflections generate G24: order336, root orbit42; absolute irreducibility',flush=True)
    intervals=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(1,4),(5,8),(1,8)]
    res=compute(roots,intervals)
    assert res['K_span_rank']==9 and res['K_minor_det']==['-308','-126']
    assert res['negative_sum_leading_minors']==['11','143','732']
    traceword=None;tauword=None
    v=roots[0];s=ss[0]
    for g,word in gg.items():
      ch=sum((g[i][i]for i in range(3)),Z)
      if traceword is None and ch.b:traceword={'word':word,'trace':ch.pair()}
      if tauword is None and hdot(v,mv(g,v))==w:
        assert mv(mul(sub(eye(3),s),g),v)==[w*x for x in v]
        tauword={'word':word,'matrix':serialize(g),'root_pairing':w.pair()}
    assert traceword is not None and tauword is not None
    coefficients=[]
    for g in gg:
      gi=inv([list(r)for r in g]);b=mul(s,gi)
      d=sum((gi[i][i]-b[i][i]for i in range(3)),Z)
      coefficients.append(3*(d+d.conj())/2)
    from math import lcm
    denom=lcm(*(a.a.denominator for a in coefficients));assert denom==2
    assert all(not a.b for a in coefficients)
    # Projector e=epsilon(1-s)/2 has exactly denominator 2G in Z[G].
    res.update({'group_order':336,'root_count':42,'projective_root_count':21,'parabolic_dimension':6,'hodge_numbers_by_chevalley_weil':[3,3],'hurwitz_dimension':9,'curve_genus':673,'root_rank':3,'nonorthogonality_connected':True,'reflection_representation_gram':serialize(H),'all_roots':serialize(rr),'character_field_witness':traceword,'integral_tau_action_witness':tauword,'projector_denominator':672,'projector_scaled_coefficient_denominator':denom,'projector_scaled_coefficient_max_abs':str(max(abs(a.a)for a in coefficients)),'elapsed_seconds':time.time()-started})
    Path(__file__).with_name('g24_reconstruction_result.json').write_text(json.dumps(res,indent=2)+'\n')
    print('trace witness',traceword,'; integral tau witness word',tauword['word'],flush=True)
    print('K rank9 determinant',res['K_minor_det'],'; positive-sum leading minors',res['negative_sum_leading_minors'],flush=True)
    print('projector denominator2G=672; ALL EXACT CHECKS PASSED',flush=True)

if __name__=='__main__':
    import sys
    search()if '--search'in sys.argv else main()


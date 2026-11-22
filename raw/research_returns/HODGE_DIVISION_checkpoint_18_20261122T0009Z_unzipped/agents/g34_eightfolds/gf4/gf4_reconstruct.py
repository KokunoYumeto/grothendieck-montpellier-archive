#!/usr/bin/env python3
"""Exact parabolic-cocycle construction over Q(t), t^2+2=0.
Group rebuilt from F4 roots and a quaternionic long-short symmetry.
No unrefereed theorem or numerical datum is used.
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
        y=F(y);return F(x.a*y.a-2*x.b*y.b,x.a*y.b+x.b*y.a)
    __rmul__=__mul__
    def inv(x):
        d=x.a*x.a+2*x.b*x.b
        if d==0:raise ZeroDivisionError
        return F(x.a/d,-x.b/d)
    def __truediv__(x,y):return x*F(y).inv()
    def __rtruediv__(x,y):return F(y)*x.inv()
    def conj(x):return F(x.a,-x.b)
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

def key(a):return tuple(tuple(r)for r in a)
def reflection(v):return sub(eye(4),scale(outer(v,[x.conj()for x in v]),2/dot(v,v)))
PHI=mat([[0,-1,-1,0],[1,0,0,1],[1,0,0,-1],[0,-1,1,0]])
ZZ=scale(PHI,w/2)
def root_system():
    rr=[]
    for i in range(4):
      for a in (-1,1):
        v=[Z]*4;v[i]=F(a);rr.append(tuple(v))
    for aa in product((-1,1),repeat=4):rr.append(tuple(F(Q(a,2))for a in aa))
    for i,j in combinations(range(4),2):
      for a,b in product((-1,1),repeat=2):
        v=[Z]*4;v[i]=F(a);v[j]=F(b);rr.append(tuple(v))
    assert len(set(rr))==48
    roots=[]
    for v in sorted(rr,key=lambda v:tuple((x.a,x.b)for x in v)):
      if tuple(-x for x in v)not in roots:roots.append(v)
    assert len(roots)==24
    return roots

def group():
    from collections import deque
    simple=mat([[0,1,-1,0],[0,0,1,-1],[0,0,0,1],[Q(1,2),Q(-1,2),Q(-1,2),Q(-1,2)]])
    ss=[reflection(v)for v in simple]
    ww={key(eye(4)):[]};todo=deque([eye(4)])
    while todo:
      a=todo.popleft()
      for j,s in enumerate(ss):
        b=mul(a,s);k=key(b)
        if k not in ww:ww[k]=ww[key(a)]+[j+1];todo.append(b)
    assert len(ww)==1152
    assert mul(PHI,PHI)==scale(eye(4),-2)
    assert mul(ZZ,ZZ)==eye(4)and star(ZZ)==ZZ and rank(sub(eye(4),ZZ))==2
    assert all(key(mul(ZZ,mul(s,ZZ)))in ww for s in ss)
    gg=dict(ww)
    for a,word in ww.items():
      b=mul(a,ZZ);assert key(b)not in ww;gg[key(b)]=word+[5]
    assert len(gg)==2304
    roots=root_system();assert all(key(reflection(v))in ww for v in roots)
    rootset=set(roots)|{tuple(-x for x in v)for v in roots}
    assert all(tuple(mv(s,v))in rootset for s in ss for v in rootset)
    assert all(tuple(mv(PHI,v))in rootset for v in rootset if dot(v,v)==1)
    assert all(tuple(x/2 for x in mv(PHI,v))in rootset for v in rootset if dot(v,v)==2)
    return roots,gg,ww

def neg_basis(t):
    a=sub(eye(4),t);p=rref(a)[1];b=tr([tr(a)[j]for j in p]);rows=rref(tr(b))[1]
    left=inv([b[i]for i in rows])
    return b,rows,left

def compute(ts,intervals):
    tt=[t for t in ts for _ in (0,1)];r=len(tt)
    vv=[];selectors=[];degrees=[]
    for t in tt:
      b,rows,left=neg_basis(t);vv.append(b);selectors.append((rows,left));degrees.append(len(b[0]))
    offsets=[0]
    for d in degrees:offsets.append(offsets[-1]+d)
    nc=offsets[-1];assert nc==14
    prefixes=[];p=eye(4)
    for t in tt:prefixes.append(p);p=mul(p,t)
    assert p==eye(4)
    blocks=[mul(p,v)for p,v in zip(prefixes,vv)]
    rel=[sum((b[i]for b in blocks),[])for i in range(4)]
    cob=[]
    for t,(rows,left)in zip(tt,selectors):cob.extend(mul(left,[sub(eye(4),t)[i]for i in rows]))
    if rank(rel)!=4 or rank(cob)!=4:return None
    assert iszero(mul(rel,cob))
    pair=zero(nc,nc//2);col=0
    for i in range(0,r,2):
      d=degrees[i];assert vv[i]==vv[i+1]
      for j in range(d):pair[offsets[i]+j][col]=pair[offsets[i+1]+j][col]=ONE;col+=1
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
    B=tr(B);E=[row+cc for row,cc in zip(B,cob)];piv=rref(tr(E))[1];Ei=inv([E[i]for i in piv])
    basis=[]
    for coeff in tr(B):basis.append([mv(v,coeff[offsets[i]:offsets[i+1]])for i,v in enumerate(vv)])
    cup=zero(6,6)
    for a,uu in enumerate(basis):
      f=[Z]*4
      for i in range(r):
        val=[x+y/2 for x,y in zip(mv(star(prefixes[i]),f),uu[i])]
        for b,ww in enumerate(basis):cup[a][b]=cup[a][b]+dot(val,ww[i])
        f=[x+y for x,y in zip(f,mv(prefixes[i],uu[i]))]
      assert not any(f)
    assert add(cup,star(cup))==zero(6,6)and rank(cup)==6
    assert all(b<c or d<a or(a<=c and d<=b)or(c<=a and b<=d)for(a,b),(c,d)in combinations(intervals,2))
    Ns=[];Xs=[];betas=[]
    for a,b in intervals:
      a-=1;b-=1;prods=[];c=eye(4)
      for i in range(a,b+1):prods.append(c);c=mul(c,tt[i])
      assert c==eye(4)
      transformed=zero(nc,6)
      for col,uu in enumerate(basis):
        uc=[Z]*4
        for p,i in zip(prods,range(a,b+1)):uc=[x+y for x,y in zip(uc,mv(p,uu[i]))]
        for i in range(r):
          u=uu[i]
          if a<=i<=b:u=[x+y for x,y in zip(u,mv(sub(eye(4),tt[i]),uc))]
          rows,left=selectors[i];lam=mv(left,[u[j]for j in rows]);assert mv(vv[i],lam)==u
          for j,x in enumerate(lam):transformed[offsets[i]+j][col]=x
      assert iszero(mul(rel,transformed))
      coeff=mul(Ei,[transformed[i]for i in piv]);assert mul(E,coeff)==transformed
      T=coeff[:6];N=sub(T,eye(6));assert iszero(mul(N,N))and mul(star(T),mul(cup,T))==cup
      if not(iszero([r[:3]for r in N])and iszero(N[3:])):return None
      Ns.append(N);Xs.append([r[3:]for r in N[:3]])
      beta=[r[3:]for r in mul(cup,N)[3:]];assert star(beta)==beta;betas.append(beta)
    assert all(iszero(mul(N,M))for N in Ns for M in Ns)
    kk=[[x for row in X for x in row]for X in Xs];rnk=rank(kk)
    result={'inertia_matrices':[serialize(t)for t in ts],'negative_eigenspace_bases':[serialize(vv[2*i])for i in range(6)],'basis':serialize(B),'gram':serialize(cup),'intervals':intervals,'monodromy_blocks':[serialize(X)for X in Xs],'nilpotent_ranks':[rank(N)for N in Ns],'K_span_rank':rnk}
    if rnk==9:
      result['K_minor_det']=det(kk).pair();total=zero(3,3);allmins=[]
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
    started=time.time();roots,gg,ww=group();print('exact W(F4)order1152; extensionorder2304; z inertia rank2',flush=True)
    random.seed(20261121)
    intervals=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(1,4),(5,8),(1,8)]
    counts={}
    for trial in range(1000):
      inds=random.sample(range(24),5);rs=[roots[i]for i in inds];ts=[reflection(v)for v in rs]+[ZZ]
      res=compute(ts,intervals)
      if res is None:continue
      counts[res['K_span_rank']]=counts.get(res['K_span_rank'],0)+1
      if trial%10==0:print('trial',trial,'ranks',counts,flush=True)
      if res['K_span_rank']==9:
        subg={key(eye(4))};todo=[eye(4)]
        while todo:
          a=todo.pop()
          for t in ts:
            b=mul(a,t)
            if key(b)not in subg:subg.add(key(b));todo.append(b)
        print('candidate subgrouporder',len(subg),flush=True)
        if len(subg)!=2304:continue
        res.update({'group_order':2304,'reflection_subgroup_order':1152,'roots':serialize(rs),'root_indices':[i+1 for i in inds],'trial':trial,'seed':20261121,'elapsed_seconds':time.time()-started,'parabolic_dimension':6,'hodge_numbers_by_chevalley_weil':[3,3],'hurwitz_dimension':9,'curve_genus':4609,'all_reflection_roots':serialize(roots)})
        Path(__file__).with_name('gf4_reconstruction_result.json').write_text(json.dumps(res,indent=2)+'\n')
        print('SUCCESS',res['K_minor_det'],res['negative_sum_leading_minors'],flush=True)
        return
    print('no witness',counts)

def main():
    from collections import deque
    started=time.time();allroots,gg,ww=group()
    roots=mat([[0,-1,-1,0],[0,-1,0,1],[0,0,0,-1],[Q(-1,2),Q(1,2),Q(-1,2),Q(-1,2)],[0,0,-1,1]])
    ts=[reflection(v)for v in roots]+[ZZ]
    subg={key(eye(4)):[]};todo=deque([eye(4)])
    while todo:
      a=todo.popleft()
      for j,t in enumerate(ts):
        b=mul(a,t)
        if key(b)not in subg:subg[key(b)]=subg[key(a)]+[j+1];todo.append(b)
    assert len(subg)==2304 and set(subg)==set(gg)
    simple=mat([[0,1,-1,0],[0,0,1,-1],[0,0,0,1],[Q(1,2),Q(-1,2),Q(-1,2),Q(-1,2)]])
    genwords=[subg[key(reflection(v))]for v in simple]
    print('fixed five reflections and z generate all2304 matrices; standard-generator words',genwords,flush=True)
    intervals=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(1,4),(5,8),(1,8)]
    res=compute(ts,intervals)
    assert res['K_span_rank']==9 and res['K_minor_det']==['256/27','640/27']
    assert res['negative_sum_leading_minors']==['18','379','1286']
    e1=eye(4)[0];s0=reflection(e1);p12=reflection(mat([[1,-1,0,0]])[0]);g0=mul(p12,ZZ)
    assert key(s0)in ww and key(p12)in ww
    assert mv(mul(sub(eye(4),s0),g0),e1)==[w,Z,Z,Z]
    charword=mul(s0,g0);ch=sum((charword[i][i]for i in range(4)),Z);assert ch==-w
    coefficients=[]
    for a in gg:
      ai=star(a);b=mul(s0,ai);d=sum((ai[i][i]-b[i][i]for i in range(4)),Z)
      coefficients.append(2*(d+d.conj()))
    assert all(not c.b and c.a.denominator==1 for c in coefficients)
    res.update({'group_order':2304,'reflection_subgroup_order':1152,'roots':serialize(roots),'standard_generator_words':genwords,'parabolic_dimension':6,'hodge_numbers_by_chevalley_weil':[3,3],'hurwitz_dimension':9,'curve_genus':4609,'all_reflection_roots':serialize(allroots),'inertia_negative_ranks':[1]*10+[2,2],'character_field_witness':{'matrix':serialize(charword),'trace':ch.pair()},'integral_t_action_witness':{'matrix_g':serialize(g0),'word_description':'(1-s_e1) s_(e1-e2) z restricts to t on e1 line'},'projector_denominator_upper_bound':2304,'elapsed_seconds':time.time()-started})
    Path(__file__).with_name('gf4_reconstruction_result.json').write_text(json.dumps(res,indent=2)+'\n')
    print('rank9 K determinant',res['K_minor_det'],'positive-sum leading minors',res['negative_sum_leading_minors'],flush=True)
    print('trace -t; integral O_K action; G e integral; ALL EXACT CHECKS PASSED',flush=True)

if __name__=='__main__':
    import sys
    search()if '--search'in sys.argv else main()


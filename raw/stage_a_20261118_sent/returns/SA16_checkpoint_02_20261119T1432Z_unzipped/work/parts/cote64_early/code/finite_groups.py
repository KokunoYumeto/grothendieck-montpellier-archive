"""Exact finite certificates for cote 64, scans 3--43 and 66--69.
Authored after passage reading, 2026-11-19. No database or floating point.
Run: python work/parts/cote64_early/code/finite_groups.py
"""
from itertools import permutations,product,combinations
from collections import Counter
import json
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]/'outputs'
def comp(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inv(a): return tuple(a.index(i) for i in range(len(a)))
def sign(a): return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
def closure(gens,mul,one):
 s={one};todo=[one]
 while todo:
  a=todo.pop()
  for b in gens:
   c=mul(a,b)
   if c not in s:s.add(c);todo.append(c)
 return frozenset(s)
def order(a,mul,one):
 b=a;n=1
 while b!=one:b=mul(b,a);n+=1
 return n
S4=set(permutations(range(4)));e=tuple(range(4))
V={g for g in S4 if g==e or (order(g,comp,e)==2 and not any(g[i]==i for i in range(4)))}
assert len(V)==4
assert {g for g in S4 if all(comp(g,v)==comp(v,g) for v in V)}==V
assert all({comp(comp(g,v),inv(g)) for v in V}==V for g in S4)
sub={frozenset({e})};todo=list(sub)
while todo:
 H=todo.pop()
 for g in S4-H:
  K=closure(tuple(H)+(g,),comp,e)
  if K not in sub:sub.add(K);todo.append(K)
conj=lambda g,H:frozenset(comp(comp(g,h),inv(g)) for h in H)
classes={min(tuple(sorted(conj(g,H))) for g in S4) for H in sub}
covers=[(H,K) for H in sub for K in sub if H<K and not any(H<L<K for L in sub)]
assert len(sub)==30 and len(classes)==11 and len(covers)==66
assert len([H for H in sub if len(H)==3])==4
cent_orders=[len([g for g in S4 if comp(g,v)==comp(v,g)]) for v in V-{e}]
assert cent_orders==[8]*3
# Automorphisms of S4: images of Coxeter adjacent transpositions.
s1=(1,0,2,3);s2=(0,2,1,3);s3=(0,1,3,2)
invol=[g for g in S4 if order(g,comp,e)==2]
autoS=[]
for a,b,c in product(invol,repeat=3):
 if order(comp(a,b),comp,e)==3 and order(comp(b,c),comp,e)==3 and comp(a,c)==comp(c,a) and len(closure([a,b,c],comp,e))==24:autoS.append((a,b,c))
assert len(autoS)==24
# Square D8; antipodism r^2.
r=(1,2,3,0);s=(0,3,2,1);D=closure([r,s],comp,e);z=comp(r,r)
autoD=[(a,b) for a,b in product(D,repeat=2) if order(a,comp,e)==4 and order(b,comp,e)==2 and comp(comp(b,a),b)==inv(a) and len(closure([a,b],comp,e))==8]
assert len(autoD)==8
refl={g for g in D if order(g,comp,e)==2 and g!=z};assert len(refl)==4
assert len({tuple(comp(comp(g,h),inv(g)) for h in sorted(refl)) for g in D})==4
# C64 N10 example ordinary functional composition.
c=(1,0,3,2);d=(0,3,2,1)
assert comp(comp(r,c),d)==(2,3,0,1) and comp(comp(d,c),r)==e
# Cube from circular permutations and from 2-subsets: determinant character.
cycles=sorted(g for g in S4 if order(g,comp,e)==4)
pairs=sorted(combinations(range(4),2));vs=sorted(V-{e})
def induced(g,objs,act):return tuple(objs.index(act(g,x)) for x in objs)
for g in S4:
 p=induced(g,cycles,lambda g,x:comp(comp(g,x),inv(g)))
 j=induced(g,vs,lambda g,x:comp(comp(g,x),inv(g)))
 q=induced(g,pairs,lambda g,x:tuple(sorted(g[a] for a in x)))
 assert sign(p)*sign(j)==1
 assert sign(q)*sign(j)==sign(g)
# Matrix arithmetic.
def mm(a,b,n):
 A,B,C,D=a;E,F,G,H=b
 return ((A*E+B*G)%n,(A*F+B*H)%n,(C*E+D*G)%n,(C*F+D*H)%n)
def mv(a,v,n):return ((a[0]*v[0]+a[1]*v[1])%n,(a[2]*v[0]+a[3]*v[1])%n)
def det(a,n):return (a[0]*a[3]-a[1]*a[2])%n
def tr(a):return (a[0]+a[3])%2
def add(a,b,n=2):return tuple((x+y)%n for x,y in zip(a,b))
I=(1,0,0,1);O=(0,0,0,0);minusI=(3,0,0,3)
M2=set(product(range(2),repeat=4));G2={a for a in M2 if det(a,2)==1}
G={a for a in product(range(4),repeat=4) if det(a,4)%2};SL={a for a in G if det(a,4)==1}
mi=lambda a:next(b for b in G if mm(a,b,4)==I)
m2i=lambda a:next(b for b in G2 if mm(a,b,2)==I)
assert (len(G),len(SL),len(G2))==(96,48,6)
J=[(1,0),(0,1),(1,1)]
A={O}|{a for a in G2 if order(a,lambda x,y:mm(x,y,2),I)==2}
W={O}|{a for a in G2 if order(a,lambda x,y:mm(x,y,2),I) in [1,3]}
assert len(A)==len(W)==4 and A&W=={O}
assert {add(a,w) for a in A for w in W}==M2
assert all(tr(mm(a,w,2))==0 for a in A for w in W)
for x in J:
 sx=next(a for a in A-{O} if mv(a,x,2)==x)
 for g in G2:
  assert mm(mm(g,sx,2),m2i(g),2)==next(a for a in A-{O} if mv(a,mv(g,x,2),2)==mv(g,x,2))
assert {w for w in W if all(mm(w,g,2)==mm(g,w,2) for g in G2)}=={O,I}
assert {m for m in M2 if tr(m)==0}=={add(a,b) for a in A for b in [O,I]}
assert {w for w in W if tr(w)==0}=={O,I}
assert {m for m in M2 if tr(mm(m,I,2))==0}.__len__()==8
lift=lambda u:tuple((i+2*x)%4 for i,x in zip(I,u))
K={lift(a) for a in M2};KA={lift(a) for a in A};KW={lift(a) for a in W};Z={I,minusI}
assert K=={g for g in G if tuple(x%2 for x in g)==I}
assert all(det(lift(u),4)==(1+2*tr(u))%4 for u in M2)
def derived(H):
 cs={mm(mm(mm(a,b,4),mi(a),4),mi(b),4) for a,b in product(H,repeat=2)}
 return closure(cs,lambda x,y:mm(x,y,4),I)
DG=derived(G);DS=derived(SL)
assert len(DG)==24 and len(DS)==12 and DS&Z=={I}
assert DG=={mm(a,z,4) for a in DS for z in Z}
assert all(mm(g,g,4) in DG for g in G)
assert any(mm(g,g,4) not in DS for g in SL)
section=closure([(0,3,1,3),(0,1,1,0)],lambda x,y:mm(x,y,4),I)
assert len(section)==6 and len({tuple(x%2 for x in g) for g in section})==6
assert len({g for g in G if all(mm(g,h,4)==mm(h,g,4) for h in G)})==2
assert all(tuple(x%2 for x in g)==I for g in SL if mm(g,g,4)==I)
# Zero-sum lift torsor P and its two natural quotients.
fibers=[[v for v in product(range(4),repeat=2) if tuple(x%2 for x in v)==j] for j in J]
P=set(t for t in product(*fibers) if tuple(sum(v[k] for v in t)%4 for k in range(2))==(0,0))
assert len(P)==16
def act(g,t):
 out=[None]*3
 for j,v in zip(J,t):out[J.index(mv(g,j,2))]=mv(g,v,4)
 return tuple(out)
def pc(t,U):return frozenset(act(lift(u),t) for u in U)
QI=sorted({pc(t,W) for t in P},key=lambda c:sorted(c))
QS=sorted({pc(t,A) for t in P},key=lambda c:sorted(c))
assert len(QI)==len(QS)==4
def quotient_action(g,Q):return tuple(Q.index(frozenset(act(g,t) for t in c)) for c in Q)
actI={g:quotient_action(g,QI) for g in G};actQ={g:quotient_action(g,QS) for g in G}
assert len(set(actI.values()))==24 and len(set(actQ.values()))==8
assert len({(actI[g],actQ[g]) for g in G})==96
ant=actQ[minusI];diag=sorted({tuple(sorted((i,ant[i]))) for i in range(4)})
edges=sorted(set(combinations(range(4),2))-set(diag))
cod=sorted({tuple(sorted((a,tuple(sorted(ant[i] for i in a))))) for a in edges})
for g in G:
 q=actQ[g]
 dc=induced(q,diag,lambda g,p:tuple(sorted(g[i] for i in p)))
 cc=induced(q,cod,lambda g,p:tuple(sorted(tuple(sorted(g[i] for i in a)) for a in p)))
 assert sign(cc)==sign(actI[g])
 assert sign(dc)==sign(actI[g])*(1 if det(g,4)==1 else -1)
assert {g for g in G if actQ[g]==e}==DS
assert {g for g in G if actI[g]==e}==KW
# subgroup squares scan32.
eps={g for g in G if sign(induced(g,J,lambda g,j:mv(g,j,2)))==1}
K0=K&SL
assert eps&SL==DG and K&DG==K0 and K0&DS==KA and KW&K0==Z and Z&KA=={I}
# Projectivization and faces.
prim={v for v in product(range(4),repeat=2) if tuple(x%2 for x in v)!=(0,0)}
pv=lambda v: min(v,tuple(-x%4 for x in v))
vertices=sorted({pv(v) for v in prim});assert len(vertices)==6
def actdelta(g):return tuple(vertices.index(pv(mv(g,v,4))) for v in vertices)
assert len({actdelta(g) for g in G})==48
assert {g for g in G if actdelta(g)==tuple(range(6))}==Z
faces={tuple(pv(v) for v in t) for t in product(*fibers)}
assert len(faces)==8
fc=Counter(tuple(pv(v) for v in t) for t in P);assert set(fc.values())=={2}
for g in G:
 dp=actdelta(g);jp=induced(g,J,lambda g,j:mv(g,j,2))
 assert sign(dp)*sign(jp)==(1 if det(g,4)==1 else -1)
T=(0,3,1,0);assert mm(T,T,4)==minusI
assert mm(tuple(-x%4 for x in T),tuple(-x%4 for x in T),4)==minusI
# The earlier run's quarter-turn example, not a manuscript formula.
U=(1,0,1,1)
up=actdelta(U)
unseen=set(range(6)); ucycles=[]
while unseen:
 start=min(unseen); cycle=[]; j=start
 while j not in cycle:
  cycle.append(j); unseen.remove(j); j=up[j]
 ucycles.append(cycle)
assert sorted(map(len,ucycles))==[1,1,4]
assert det(U,4)==1 and sign(induced(U,J,lambda g,j:mv(g,j,2)))==-1
# D8 central cocycle: a,b involutions, ab=zba, q(x,y)=b^y a^x.
a=s;b=comp(r,s)
q=lambda x,y:comp(b if y else e,a if x else e)
for x,y,u,v in product(range(2),repeat=4):
 assert comp(q(x,y),q(u,v))==comp(z if x*v else e,q(x^u,y^v))
# explicit natural reference module R_J (rank-two augmentation over Z4).
rj=[(2,3,3),(3,2,3),(3,3,2)]
assert all(sum(v)%4==0 for v in rj)
assert tuple(sum(v[i] for v in rj)%4 for i in range(3))==(0,0,0)
assert all((rj[i][0]*rj[j][1]-rj[i][1]*rj[j][0])%4 in [1,3] for i,j in combinations(range(3),2))
result={
 'S4':{'order':24,'subgroups':30,'conjugacy_classes_of_subgroups':11,'cover_inclusions':66,'subgroup_orders':dict(sorted(Counter(map(len,sub)).items())),'centralizer_nonzero_Klein':cent_orders,'automorphisms':len(autoS),'Sylow3':4},
 'D8':{'order':8,'automorphisms':len(autoD),'inner_automorphisms':4,'cocycle':'c(g)d(h)','cocycle_pairs_checked':16,'orientation_order_example':'r c d=r^2, d c r=1'},
 'M2_F2':{'matrices':16,'G2':6,'A':sorted(A),'W':sorted(W),'trace_zero':8,'W_invariants':[O,I],'W_trace_sequence_split':False},
 'GL2_Z4':{'order':96,'SL_order':48,'derived_GL':24,'derived_SL':12,'GL_abelianization':'C2 x C2','SL_abelianization':'C4','GL_reduction_splits':True,'SL_reduction_splits':False,'P_zero_sum':16,'I':4,'square_vertices':4,'natural_pair_image':96,'projective_image':48,'faces':8,'face_lift_multiplicities':dict(Counter(fc.values())),'central_extension_splits':False,'subgroup_intersections_verified':5},
 'reference_module':{'r_j':rj,'every_pair_basis':True},
 'earlier_run_quarter_turn':{'matrix':U,'projective_cycles':ucycles,'determinant':1,'reduction_sign':-1}}
OUT.mkdir(exist_ok=True)
(OUT/'finite_groups.json').write_text(json.dumps(result,indent=2)+'\n')
# Full subgroup data and inclusion witnesses, with stable local numbering.
sublist=sorted(sub,key=lambda H:(len(H),sorted(H)));num={H:i for i,H in enumerate(sublist)}
(OUT/'s4_subgroups.json').write_text(json.dumps([{'number':num[H],'order':len(H),'elements':sorted(H)} for H in sublist],indent=2)+'\n')
(OUT/'s4_hasse_edges.json').write_text(json.dumps([{'from':num[H],'to':num[K],'index':len(K)//len(H)} for H,K in sorted(covers,key=lambda x:(num[x[0]],num[x[1]]))],indent=2)+'\n')
print(json.dumps(result,indent=2))

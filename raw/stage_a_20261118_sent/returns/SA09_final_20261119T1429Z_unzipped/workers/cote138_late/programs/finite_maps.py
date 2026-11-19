"""Enumerate all connected oriented sphere maps on 1..6 darts, allowing folded
edges, as transitive pairs (r,s), s^2=1.  Fix one r per partition and divide by its
centralizer; record mirror and full symmetry, separately from monodromy.
Also verify the literal precarte counterexamples and cell-pinning kernel.
"""
from pathlib import Path
import itertools,json,collections
W=Path(__file__).resolve().parents[1]
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
 r=[0]*len(a)
 for i,v in enumerate(a):r[v]=i
 return tuple(r)
def conj(h,a):return mul(mul(h,a),inv(h))
def cyc(a):
 todo=set(range(len(a)));cs=[]
 while todo:
  j=min(todo);o=[]
  while j in todo:todo.remove(j);o.append(j);j=a[j]
  cs.append(tuple(o))
 return cs
def typ(a):return tuple(sorted([len(k) for k in cyc(a)],reverse=True))
def part(n,m=None):
 if n==0:yield ()
 else:
  for k in range(min(n,m or n),1-1,-1):
   for q in part(n-k,k):yield (k,)+q
def representative(p):
 a=list(range(sum(p)));k=0
 for l in p:
  for j in range(l):a[k+j]=k+(j+1)%l
  k+=l
 return tuple(a)
def connected(r,s):
 seen={0};q=[0]
 for a in q:
  for g in(r,s):
   v=g[a]
   if v not in seen:seen.add(v);q.append(v)
 return len(seen)==len(r)
def closure(gs):
 e=tuple(range(len(gs[0])));seen={e};q=[e]
 for a in q:
  for b in gs:
   h=mul(a,b)
   if h not in seen:seen.add(h);q.append(h)
 return seen
def cell_kernel(r,s,aut):
 f=mul(inv(r),s);cells=[frozenset(k) for p in(r,s,f) for k in cyc(p)]
 return [h for h in aut if all(frozenset(h[i] for i in k)==k for k in cells)]
allmaps=[]
for n in range(1,7):
 perms=list(itertools.permutations(range(n)));e=tuple(range(n));invols=[s for s in perms if mul(s,s)==e]
 for p in part(n):
  r=representative(p);ri=inv(r);cent=[h for h in perms if conj(h,r)==r];rev=[h for h in perms if conj(h,r)==ri]
  seen=set()
  for sig in invols:
   f=mul(ri,sig)
   if len(cyc(r))+len(cyc(sig))+len(cyc(f))-n!=2 or not connected(r,sig):continue
   canonical=min(conj(h,sig) for h in cent)
   if canonical in seen:continue
   seen.add(canonical);sig=canonical;f=mul(ri,sig)
   aut=[h for h in cent if conj(h,sig)==sig];reverse=[h for h in rev if conj(h,sig)==sig]
   kernel=cell_kernel(r,sig,aut)
   row={'degree':n,'r':[a+1 for a in r],'sigma':[a+1 for a in sig],'face':[a+1 for a in f],
    'passport':[list(p),list(typ(sig)),list(typ(f))],
    'oriented_aut_order':len(aut),'reversing_symmetries':len(reverse),
    'full_aut_order':len(aut)+len(reverse),'monodromy_order':len(closure([r,sig])),
    'pinned_kernel_order':len(kernel),'reflexible':bool(reverse)}
   allmaps.append(row)
# Torus counterexample, where the genus-zero filtering was deliberately not used.
r=representative((4,));sig=(2,3,0,1);face=mul(inv(r),sig)
perms=list(itertools.permutations(range(4)));aut=[h for h in perms if conj(h,r)==r and conj(h,sig)==sig];ker=cell_kernel(r,sig,aut)
torus={'r':r,'sigma':sig,'face':face,'Euler_characteristic':len(cyc(r))+len(cyc(sig))+len(cyc(face))-4,'automorphism_order':len(aut),'cell_pinning_kernel':ker,'kernel_order':len(ker),'relabeling_group_order':2,'relabeling_stabilizer_order':len(aut)//len(ker),'pinned_class_count':2*len(ker)//len(aut)}
assert torus['Euler_characteristic']==0 and len(aut)==4 and len(ker)==2
# Explicit tables on scan106.
r=representative((3,2,1));s1=(3,1,5,0,4,2);s2=(3,1,2,0,5,4)
tables=[]
for ss in[s1,s2]:
 f=mul(inv(r),ss)
 tables.append({'r':r,'sigma':ss,'face':f,'face_cycles':cyc(f),'order':len(closure([r,ss]))})
 assert typ(f)==(6,) and tables[-1]['order']==720
# Number of fixed-r involutions before conjugacy quotient.
perms6=list(itertools.permutations(range(6)));e6=tuple(range(6))
admissible=[ss for ss in perms6 if mul(ss,ss)==e6 and typ(ss)==(2,2,1,1) and typ(mul(inv(r),ss))==(6,)]
assert len(admissible)==18

def select(passport):return [m for m in allmaps if m['passport']==[list(p) for p in passport]]
sex=select([(3,2,1),(2,2,1,1),(6,)]);dual=select([(6,),(2,2,1,1),(3,2,1)]);five=select([(4,1),(2,2,1),(4,1)])
assert len(sex)==3 and sorted(m['full_aut_order'] for m in sex)==[1,1,2]
assert len(dual)==3 and len(five)==2 and all(m['full_aut_order']==1 and m['monodromy_order']==20 for m in five)
# Literal precarte category counterexample, independent S/A/F sets.
weights0=[1];weights1=[2,2];weights2=[2,4,4];f10=[0,0];f21=[0,1,1]
def law(source,target,fun):
 return all(source[i]==fun.count(j)*target[j] for i,j in enumerate(fun))
assert law(weights1,weights0,f10) and law(weights2,weights1,f21)
comp=[f10[i] for i in f21];assert not law(weights2,weights0,comp)
# Cubic-star map to the degree-one map: orbit counts as opposed to local degrees.
star={'vertex_fibre_size':1,'source_vertex_degree':3,'target_vertex_degree':1,'edge_fibre_size':3,'source_edge_degrees':[1,1,1],'target_edge_degree':1,'face_fibre_size':1,'source_face_degree':3,'target_face_degree':1}
summary={'counts_by_degree':dict(collections.Counter(m['degree'] for m in allmaps)),
 'number_total':len(allmaps),'torus_counterexample':torus,'precarte_composition_counterexample':{'weights0':weights0,'weights1':weights1,'weights2':weights2,'first_two_laws':True,'composite_law':False},
 'cubic_star_quotient_counterexample':star,'cubic_star_pinnings':6//3,
 'scan106_tables':tables,'fixed_r_admissible_sigma_count':len(admissible),'sextic_passport':sex,'dual_sextic_passport':dual,'chiral_degree5':five,
 'theta_passport':select([(3,3),(2,2,2),(2,2,2)]),
 'impossible_degree5_vertex_types':len([m for m in allmaps if m['degree']==5 and m['passport'][0]==[2,1,1,1]]),
 'impossible_degree6_vertex_types':len([m for m in allmaps if m['degree']==6 and m['passport'][0]==[2,1,1,1,1]]),
 'status':'All assertions passed. Enumeration certifies permutation classes, not an uninspected one-to-one assignment to rough manuscript drawings.'}
(W/'outputs/finite_maps_all.json').write_text(json.dumps(allmaps,ensure_ascii=False,indent=2)+'\n')
(W/'outputs/finite_maps_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))

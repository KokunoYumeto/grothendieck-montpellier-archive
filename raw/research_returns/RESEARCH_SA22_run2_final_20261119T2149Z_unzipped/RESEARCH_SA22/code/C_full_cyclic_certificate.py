#!/usr/bin/env python3
"""All axioms, all fibers, cardinality coverage: C4 with C8 -> C4."""
import json,time
start=time.perf_counter();n=4;nt=2*n

def fam(k):
 ans=[]
 for L in range(1,n+1):
  if L==n:
   a=frozenset(range(n))
  elif (k-L+1)%2==0:
   start=(k-L+1)//2
   a=frozenset((start+j)%n for j in range(L))
  else:continue
  if a not in ans:ans.append(a)
 return ans
A=[fam(k) for k in range(nt)]
shift=lambda a,s:frozenset((x+s)%n for x in a)
def conv(a,b):
 h=[0]*n
 for x in a:
  for y in b:h[(x+y)%n]+=1
 return h
checks=dict(chain=0,reflection=0,kernel=0,alignment=0,convolution=0)
for k in range(nt):
 assert all(a<=b or b<=a for a in A[k] for b in A[k]);checks['chain']+=1
 for a in A[k]:
  assert a==frozenset((k-x)%n for x in a);checks['reflection']+=1
 for u in [0,2]:
  assert A[(k+2*u)%nt]==[shift(a,u) for a in A[k]];checks['kernel']+=1
 for l in range(nt):
  s=(k//2-l//2)%n
  chain=A[k]+[shift(b,s) for b in A[l]]
  assert all(a<=b or b<=a for a in chain for b in chain);checks['alignment']+=1
  for a in A[k]:
   for b in A[l]:
    h=conv(a,b)
    levels=[frozenset(x for x in range(n) if h[x]>=r) for r in range(1,max(h)+1)]
    assert all(c in A[(k+l)%nt] for c in levels);checks['convolution']+=1
coverage=sorted({len(a) for family in A for a in family});assert coverage==[1,2,3,4]
f=frozenset([0,1]);fp=frozenset([0,2])
sq=conv(f,f);sqp=conv(fp,fp)
cube=[sum(sq[(x-y)%n] for y in f) for x in range(n)]
cubep=[sum(sqp[(x-y)%n] for y in fp) for x in range(n)]
assert max(cube)==3 and max(cubep)==4
# A redundant C3 index factor preserves every lettered axiom while enlarging the kernel.
enlarged_labels=[(k,q) for k in range(nt) for q in range(3)]
enlarged_count=0
for (k,q) in enlarged_labels:
 for (l,r) in enlarged_labels:
  for a in A[k]:
   for b in A[l]:
    h=conv(a,b)
    levels=[frozenset(x for x in range(n) if h[x]>=v) for v in range(1,max(h)+1)]
    assert all(c in A[(k+l)%nt] for c in levels)
    enlarged_count+=1
assert enlarged_count==3600
enlarged_kernel=[(k,q) for k,q in enlarged_labels if k%n==0]
assert len(enlarged_kernel)==6
result={'kernel_enlargement':{'group':'C8 x C3','kernel':enlarged_kernel,'convolution_checks':enlarged_count},'G':'Z/4Z','Gtilde':'Z/8Z','rho':'k mod 4','G_2':[0,2],'kernel':[0,4],'i':'u -> 2u','families':[[sorted(a) for a in family] for family in A],'checks':checks,'coverage':coverage,'K_counterexample':{'f':sorted(f),'fprime':sorted(fp),'f*f':sq,'fprime*fprime':sqp,'f*f*f':cube,'fprime*fprime*fprime':cubep,'maxima':[max(cube),max(cubep)]},'runtime_seconds':round(time.perf_counter()-start,6)}
print(json.dumps(result,indent=2))

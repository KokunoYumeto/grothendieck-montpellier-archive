#!/usr/bin/env python3
"""Exact Artin checks of the rightmost-strand marking used in D23.P18."""
import json,pathlib
ROOT=pathlib.Path(__file__).parent
def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return tuple(a)
def inv(w):return tuple(-x for x in w[::-1])
def subst(w,images):
 out=()
 for x in w:out=red(out+(images[x-1]if x>0 else inv(images[-x-1])))
 return out
def braid(word,n):
 identity=[(j+1,)for j in range(n)];out=identity.copy()
 for j in word:
  s=identity.copy()
  if j>0:s[j-1]=(j,j+1,-j);s[j]=(j,)
  else:
   k=-j;s[k-1]=(k+1,);s[k]=(-k-1,k,k+1)
  out=[subst(w,out)for w in s]
 return out
def same(a,b,n):return braid(a,n)==braid(b,n)
def comm(a,b):return a+b+inv(a)+inv(b)
rows=[]
for n in [3,4]:
 # Work in B_(n+1), with last strand forgotten.
 us=[]
 for i in range(1,n+1):
  v=tuple(range(n,i,-1));us.append(v+(i,i)+inv(v))
 count=0
 for j in range(1,n):
  for i in range(n):
   lhs=(j,)+us[i]+(-j,)
   rhs=us[i]
   if i==j-1:rhs=us[j]
   elif i==j:rhs=inv(us[j])+us[j-1]+us[j]
   assert same(lhs,rhs,n+1),(n,j,i)
   count+=1
 for i in range(1,n+1):
  v=tuple(-j for j in range(i,n));assert same(v+us[-1]+inv(v),us[i-1],n+1)
 boundary=sum(us,());zn=tuple(range(1,n))*n;zn1=tuple(range(1,n+1))*(n+1)
 assert same(zn+boundary,zn1,n+1)
 # The older full twist is central relative to the two arguments being
 # multiplied when y_i is replaced by z_i in a commutator evaluation.
 for i in range(3,n+1):
  yi=tuple(range(i-1,1,-1))+(1,1)+tuple(range(2,i))
  zi_old=tuple(range(1,i-1))*(i-1)
  zi=tuple(range(1,i))*i
  assert same(zi_old+yi,zi,n+1)
  assert same(comm(zi_old,yi),(),n+1)
  assert same(comm(zi_old,(i,i)),(),n+1)
 rows.append({'n':n,'peripheral_braid_words':[list(u)for u in us],
              'Artin_conjugation_relations':count,'peripheral_transport':'PASS',
              'boundary_fulltwist_relation':'PASS','central_input_replacement':'PASS'})
out={'statement':'D23.P18','checks':rows,'result':'PASS',
     'scope':'Exact discrete braid identities via the faithful Artin representation; the published full-GT automorphism theorem is a cited input.'}
(ROOT/'hurwitz_stability_artin_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

#!/usr/bin/env python3
"""Independent finite checks of the explicit all-size brick-matrix construction.
The proof for all n,m is written in E826; finite checks do not replace it.
"""
from pathlib import Path
import json,time,math
start=time.perf_counter();prime=1009

def matrices(n,m):
 out=[]
 if n>=m:
  starts=list(range(0,n-m+1,m))
  if starts[-1]!=n-m:starts.append(n-m)
  for start in starts:
   F=[[0]*m for _ in range(n)]
   for k in range(m):F[start+k][k]=1
   out.append(F)
  F=out[0]
  out.append([[F[i][j-1] if j>0 else 0 for j in range(m)] for i in range(n)])
  out.append([[F[i][j+1] if j+1<m else 0 for j in range(m)] for i in range(n)])
 else:
  starts=list(range(0,m-n+1,n))
  if starts[-1]!=m-n:starts.append(m-n)
  for start in starts:
   F=[[0]*m for _ in range(n)]
   for k in range(n):F[k][start+k]=1
   out.append(F)
  F=out[0]
  out.append([F[i+1][:] if i+1<n else [0]*m for i in range(n)])
  out.append([F[i-1][:] if i>0 else [0]*m for i in range(n)])
 assert len(out)==math.ceil(max(n/m,m/n))+2
 return out

def rank_mod(rows,cols):
 rows=[r[:] for r in rows];k=0
 for c in range(cols):
  q=next((j for j in range(k,len(rows)) if rows[j][c]%prime),None)
  if q is None:continue
  rows[k],rows[q]=rows[q],rows[k];inv=pow(rows[k][c]%prime,-1,prime)
  rows[k]=[(z*inv)%prime for z in rows[k]]
  for j in range(k+1,len(rows)):
   a=rows[j][c]%prime
   if a:rows[j]=[(z-a*t)%prime for z,t in zip(rows[j],rows[k])]
  k+=1
  if k==len(rows):break
 return k
checks=[]
for n in range(1,7):
 for m in range(1,7):
  Ms=matrices(n,m);rows=[];cols=n*n+m*m
  for F in Ms:
   for i in range(n):
    for j in range(m):
     row=[0]*cols
     for k in range(n):row[i*n+k]+=F[k][j]
     for k in range(m):row[n*n+k*m+j]-=F[i][k]
     rows.append(row)
  rk=rank_mod(rows,cols)
  assert rk==cols-1
  checks.append({'n':n,'m':m,'arrows':len(Ms),'rank_mod1009':rk,'scalar_kernel_dimension':1})
out={'result':'PASS','actual_cases':len(checks),'prime':prime,'checks':checks,'runtime_seconds':time.perf_counter()-start,
     'scope':'Exact integer equations reduced modulo1009 attain rank n²+m²−1; the scalar solution gives the matching characteristic-zero upper bound. All-size proof remains the written injection/projection and Jordan argument.'}
Path(__file__).with_name('rm_rectangular_brick_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['result','actual_cases','runtime_seconds','scope']},indent=2))

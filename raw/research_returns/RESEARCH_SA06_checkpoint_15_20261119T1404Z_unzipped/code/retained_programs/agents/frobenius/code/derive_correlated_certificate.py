#!/usr/bin/env python3
"""Find an exact small polynomial dual certificate for the level-2 test."""
from itertools import product
from time import perf_counter
from pathlib import Path
from datetime import datetime,timezone
import json

def solve4(rows,n):
    original=rows[:];rows=rows[:];mask=(1<<n)-1;piv=[];rank=0
    while rank<len(rows):
      pick=next((j for j in range(rank,len(rows)) if rows[j][0]&mask),None)
      if pick is None:break
      rows[rank],rows[pick]=rows[pick],rows[rank]
      pl,ph=rows[rank];bit=(pl&mask)&-(pl&mask)
      if ph&bit:ph^=pl
      rows[rank]=(pl,ph);piv.append(bit)
      for j in range(rank+1,len(rows)):
        lo,hi=rows[j];a=(1 if lo&bit else 0)+(2 if hi&bit else 0)
        if a==1:rows[j]=(lo^pl,hi^ph^pl^(lo&pl))
        elif a==2:rows[j]=(lo,hi^pl)
        elif a==3:rows[j]=(lo^pl,hi^ph^(lo&pl))
      rank+=1
    if any(lo>>n for lo,hi in rows[rank:]):return None
    gp={}
    for lo,hi in rows[rank:]:
      assert not lo&mask
      z=hi
      while z&mask:
        bit=(z&mask)&-(z&mask)
        if bit not in gp:gp[bit]=z;break
        z^=gp[bit]
      else:
        if z>>n:return None
    xl=xh=0
    for bit,z in sorted(gp.items(),reverse=True):
      if ((z>>n)^((z&xl).bit_count()))&1:xl|=bit
    for j in range(rank-1,-1,-1):
      lo,hi=rows[j];bit=piv[j]
      rhs=((lo>>n)&1)+2*((hi>>n)&1)
      dot=((lo&mask&xl).bit_count()+2*((lo&mask&xh).bit_count()+(hi&mask&xl).bit_count()))%4
      a=(rhs-dot)%4
      if a&1:xl|=bit
      if a&2:xh|=bit
    for lo,hi in original:
      rhs=((lo>>n)&1)+2*((hi>>n)&1)
      dot=((lo&mask&xl).bit_count()+2*((lo&mask&xh).bit_count()+(hi&mask&xl).bit_count()))%4
      assert dot==rhs
    return [((xl>>i)&1)+2*((xh>>i)&1) for i in range(n)]

def run(degree,bit_basis=False):
    tic=perf_counter()
    L=[(1,0,1,0),(1,0,0,0),(0,1,0,1),(0,0,0,1),(2,1,1,1),(0,0,1,1)]
    R=[(-1,-1),(-1,1),(-1,0),(0,-1),(1,0),(0,1)]
    H=[(0,0,1,0),(1,0,-1,0),(0,1,0,0),(0,-1,0,1),(0,0,0,0),(0,0,0,0)]
    verts=list(product(range(2),range(2),range(2),range(2),range(4),range(4)))
    mons=([e for e in product(range(2),repeat=8) if sum(e)<=degree] if bit_basis else [e for e in product(range(2),range(2),range(2),range(2),range(degree+1),range(degree+1)) if sum(e)<=degree])
    def val(v,e):
      if bit_basis:v=v[:4]+(v[4]%2,v[4]//2,v[5]%2,v[5]//2)
      z=1
      for a,b in zip(v,e):z*=a**b
      return z%4
    vals={v:[val(v,e) for e in mons] for v in verts};k=len(mons);n=4*k+9;rows=[]
    for s in range(3):
      for u in verts:
        for a,b in product(range(4),repeat=2):
          if a==b==0:continue
          step=tuple(a*H[2*s][i]+b*H[2*s+1][i] for i in range(4))+tuple(a*R[2*s][i]+b*R[2*s+1][i] for i in range(2))
          v=tuple((u[i]+step[i])%(2 if i<4 else 4) for i in range(6))
          if (u,(a,b))>(v,((-a)%4,(-b)%4)):continue
          q=[(a*L[2*s][i]+b*L[2*s+1][i])%4 for i in range(4)]
          coeff=[(q[i]*(vals[v][j]-vals[u][j]))%4 for i in range(4) for j in range(k)]+[0]*9
          coeff[4*k+3*s:4*k+3*s+3]=[a*a%4,a*b%4,b*b%4]
          lo=hi=0
          for j,c in enumerate(coeff):
            if c&1:lo|=1<<j
            if c&2:hi|=1<<j
          rows.append((lo,hi))
    # 2*(sum of diagonal Gram weights) = 2 modulo 4.
    rows.append((0,(1<<n)+sum(1<<(4*k+3*s+i) for s in range(3) for i in (0,2))))
    sol=solve4(rows,n)
    out={'degree':degree,'bit_basis':bit_basis,'monomials':k,'variables':n,'equations':len(rows),'solution_exists':sol is not None,'runtime_seconds':perf_counter()-tic}
    if sol is not None:
      out['potential_terms']=[[[c,list(mons[j])] for j,c in enumerate(sol[i*k:(i+1)*k]) if c] for i in range(4)]
      out['gram_weights']=[sol[4*k+3*s:4*k+3*s+3] for s in range(3)]
      out['all_edges_checked']=True
    return out

if __name__=='__main__':
    start=perf_counter();out={'started_utc':datetime.now(timezone.utc).isoformat(),'tests':[]}
    for degree in (1,2,3,4,5,6,7,8):
      ans=run(degree,True);out['tests'].append(ans)
      if ans['solution_exists']:break
    out['runtime_seconds']=perf_counter()-start
    path=Path(__file__).resolve().parents[1]/'output'/'derive_correlated_certificate.json'
    path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

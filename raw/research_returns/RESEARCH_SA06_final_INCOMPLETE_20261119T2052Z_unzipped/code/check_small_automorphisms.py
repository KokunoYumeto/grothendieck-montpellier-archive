#!/usr/bin/env python3
"""Enumerate automorphisms of y^2+y=x^3/F4 and y^2=x^3-x/F9."""
from itertools import product
from pathlib import Path
import json,time

class Field:
    def __init__(self,p,c0,c1): self.p,self.c0,self.c1=p,c0,c1
    def elt(self,n): return (n%self.p,n//self.p)
    def add(self,x,y): return tuple((a+b)%self.p for a,b in zip(x,y))
    def neg(self,x):return tuple(-a%self.p for a in x)
    def mul(self,x,y):
        a,b=x;c,d=y;p=self.p
        return ((a*c-b*d*self.c0)%p,(a*d+b*c-b*d*self.c1)%p)
    def pow(self,x,n):
        z=(1,0)
        while n:
            if n&1:z=self.mul(z,x)
            x=self.mul(x,x);n//=2
        return z
    def inv(self,x):
        assert x!=(0,0)
        return self.pow(x,self.p**2-2)

def main():
    t=time.perf_counter(); out={}
    F=Field(2,1,1); elems=[F.elt(i) for i in range(4)]; a2=[]
    for u in elems[1:]:
      for s in elems:
       r=F.pow(s,2)
       for v in elems:
        if F.pow(u,3)==(1,0) and F.pow(s,4)==s and F.add(F.pow(v,2),v)==F.pow(s,6):
         a2.append((u,r,s,v))
    assert len(a2)==24
    G=Field(3,1,0); elems=[G.elt(i) for i in range(9)]; a3=[]
    for u in elems[1:]:
      for r in elems:
       if G.pow(u,4)==(1,0) and G.pow(r,3)==r:a3.append((u,r))
    assert len(a3)==12
    out={'F4_polynomial':'t^2+t+1','F9_polynomial':'t^2+1',
         'Aut_char2_u_r_s_t':a2,'Aut_char3_u_r':a3,
         'counts':[len(a2),len(a3)],'runtime_seconds':time.perf_counter()-t}
    Path(__file__).with_name('check_small_automorphisms_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print('char2 automorphisms:',len(a2),'char3 automorphisms:',len(a3),'runtime:',out['runtime_seconds'])

if __name__=='__main__':main()

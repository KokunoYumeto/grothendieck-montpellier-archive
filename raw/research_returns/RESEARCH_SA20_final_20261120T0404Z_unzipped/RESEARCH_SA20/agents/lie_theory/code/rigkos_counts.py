#!/usr/bin/env python3
from math import factorial
from sympy import totient

def show(typ,w,h,z):
 d=h*z*int(totient(h))
 assert w*w%d==0
 print(typ,'|W|=',w,'h=',h,'z=',z,'phi(h)=',totient(h),
       'RigKos/G=',w*w//d,'with generator=',w*w//(h*z))
for r in range(1,9):show(f'A{r}',factorial(r+1),r+1,r+1)
for r in range(2,9):
 show(f'B{r}',2**r*factorial(r),2*r,2)
 show(f'C{r}',2**r*factorial(r),2*r,2)
for r in range(4,9):show(f'D{r}',2**(r-1)*factorial(r),2*r-2,4)
for typ,w,h,z in [('G2',12,6,1),('F4',1152,12,1),('E6',51840,12,3),
                  ('E7',2903040,18,2),('E8',696729600,30,1)]:
 show(typ,w,h,z)
assert 696729600//(30*8)==2903040
print('The earlier E8 value 2,903,040 omitted one factor |W|.')

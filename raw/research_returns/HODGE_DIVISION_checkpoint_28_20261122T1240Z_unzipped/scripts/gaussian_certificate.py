#!/usr/bin/env python3
"""Exact arithmetic for HD-Q1/Q2/Q4/Q5/Q6; this is not a proof assistant.
All integers are exact. Geometry and source theorems are checked in the paper.
"""
from math import factorial
import json

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def power(x,n):
 r=(1,0)
 for _ in range(n):r=mul(r,x)
 return r

eigen=[]
for j in range(5):
 r=mul(power((0,1),j),power((0,-1),4-j))
 s=mul(power((1,1),j),power((1,-1),4-j))
 p=mul(add((1,0),r),add((4,0),neg(s)))
 expected=(16,0) if j in (0,4) else (0,0)
 assert p==expected
 eigen.append({'j':j,'R':r,'S':s,'P':p})
a4=power((2,1),4)
assert a4==(-7,24)
assert 4608**2+6144**2==7680**2
assert 576*8**2==36864
assert 7680*8==61440
assert 61440>36864
w=3**4*factorial(9)//factorial(5)
p=3**6*factorial(6)*4**2
bezout=4*w*p//9
assert w*p%9==0
D_even=4*factorial(4)//2
D_odd=4*D_even
result={
 'projector_eigenvalues':eigen,'a_fourth_power':a4,
 'P_positive_degree_factor':8,'P_negative_degree_factor':8,
 'z_signed_degree_factor':256,'norm_d_upper_factor':64,
 'orthogonal_gram_ratio':576,'N_degree_squared_factor':36864,
 'signed_degree_squared_factor':61440,
 'W4_degree_3Theta':w,'P6_degree_3Theta':p,
 'corrected_Prym_Bezout_D_even':bezout,
 'theta_complete_intersection_degree':96,'theta_D_even':D_even,'theta_D_odd':D_odd,
 'C4_even_coefficient':61440*D_even**2,
 'C4_odd_coefficient':61440*D_odd**2,
 'C4_formula':'coefficient * delta * ceil(sqrt(T))',
 'proof_scope':'Prym support and theta nonvanishing are geometric arguments in paper; the certificate verifies only exact arithmetic.'}
print(json.dumps(result,indent=2))

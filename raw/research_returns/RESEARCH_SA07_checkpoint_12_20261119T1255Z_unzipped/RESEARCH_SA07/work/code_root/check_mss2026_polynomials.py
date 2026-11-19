#!/usr/bin/env python3
"""Exact audit of MSS arXiv:2608.17673v1 Tables2,3,9,10 and Th2.1/2.3.

This verifies the displayed scalar identities, not the arithmetic-image theorem.
"""
import time
import sympy as s

start = time.perf_counter()
g = s.symbols('g')
eigen = s.Matrix([
    2*g*(2*g+1)*(2*g+2)*(2*g+3),
    (2*g-2)*2*g*(2*g+1)*(2*g+2),
    (2*g-2)*2*g*(2*g+1)*(2*g+2),
    (2*g-2)*(2*g-1)*2*g*(2*g+1),
    (2*g-4)*(2*g-2)*2*g*(2*g+1),
])
eps = s.Matrix([2/eigen[0],0,8/eigen[2],3/eigen[3],0])
j1 = s.Matrix([0,1,-5,-4,2])
j2 = s.Matrix([3,3,3,-1,-2])
j = 2*j1-3*j2
assert j == s.Matrix([-9,-7,-19,-5,10])
sigma = 180*(g-1)*g*eps-j
r = s.Matrix([
    -24*(g+1)*(2*g+1)*(2*g+3),
    12*(g+1)*(2*g+1)*(8*g+3),
    -36*(g+1)*(2*g+1),
    12*(2*g-1)*(2*g+1)*(2*g+3),
    12*(g-2)*(2*g+1)*(4*g+3),
])
ss = s.Matrix([
    0,4*(g+1)**2*(22*g-17),-12*(g+1)**2*(2*g+3),
    4*(g+1)*(2*g-1)*(10*g+13),4*(g-2)*(g+1)*(14*g+11),
])
f1 = s.Matrix([
    -24*(g+1)*(2*g+1)*(2*g+3),
    8*(g+1)*(g+13)*(2*g+1),24*g*(g+1)*(2*g+1),
    -16*(g+1)*(2*g-1)*(2*g+1),-8*(g-2)*(g+1)*(2*g+1),
])
es1 = s.Matrix([6,27,3,-12,-3]).multiply_elementwise(eigen)
es2 = s.Matrix([6,-1,-3,4,1]).multiply_elementwise(eigen)
for name,fun in [('r',r),('s',ss),('f1',f1)]:
    assert s.cancel(fun.dot(sigma)) == 0
    print(name+'(sigma3) = 0')
assert s.cancel(r.dot(eps)-3*(2*g+1)/((g-1)*g)) == 0
assert s.cancel(ss.dot(eps)-3*(g+1)/((g-1)*g)) == 0
assert s.cancel(es1.dot(eps)) == s.cancel(es2.dot(eps)) == 0
assert s.cancel(f1.dot(j1)-72*(g+1)*(2*g+1)) == 0
assert s.cancel(f1.dot(j2)-48*(g+1)*(2*g+1)) == 0
print('f1(j1) =',s.factor(f1.dot(j1)))
print('f1(j2) =',s.factor(f1.dot(j2)))
assert s.cancel(es1.dot(j)-(2*g-1)*es2.dot(j)) == 0
assert s.cancel(es2.dot(j)+1080*g*(g+1)*(2*g+1)) == 0
print('ES1(j) =',s.factor(es1.dot(j)))
print('ES2(j) =',s.factor(es2.dot(j)))
print('ES1(j)/ES2(j) =',s.cancel(es1.dot(j)/es2.dot(j)))
# Printed p25 scalar expansion uses -3 instead of the preceding matrix's -19.
printed_typo = es2.dot(j) + 16*es2[2]
print('p25 printed scalar expansion minus matrix product =',s.factor(printed_typo-es2.dot(j)))
assert s.cancel(printed_typo-es2.dot(j)+384*g*(g-1)*(g+1)*(2*g+1)) == 0
print('PASS: exact rational-function identities; g>=3 throughout the five-vector basis')
print('ACTUAL_WALL_SECONDS',f'{time.perf_counter()-start:.9f}')

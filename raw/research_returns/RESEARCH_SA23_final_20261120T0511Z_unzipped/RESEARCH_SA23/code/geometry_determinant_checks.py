"""Exact finite certificates for the rank-one block in the infinite-dimensional counterexample."""
from fractions import Fraction as F
from math import log, exp
from time import perf_counter
start=perf_counter()
a,b=F(1,2),F(2)
assert a*b==1
print('Nonidentity rank-one blocks: A=1/2, B=2, AB=1.')
print('Infinite identity complement: singular rearrangements A=(1,1,...), B=(2,1,...), AB=(1,1,...).')
print('Rearranged determinants: 1, 2, 1; multiplicativity fails.')
print('Spectral logarithm determinants:',a,b,a*b,'; multiplicativity holds.')
for n in [2,5,10,100]:
    trace_log=F(-n)*F(1,n)
    assert trace_log==-1
    print('Diffuse example n=',n,': tau(log a_n)=',trace_log,'; L1 distance=(1-exp(-n))/n <',F(1,n))
for n in [1,2,3,5,10]:
    prod=F(1)
    for j in range(1,n+1): prod*=1-F(1,2*j)
    print('Compact non-trace-class product through n=',n,':',prod)
print('Elapsed seconds:',perf_counter()-start)

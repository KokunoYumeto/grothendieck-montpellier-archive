from datetime import datetime,timezone
from time import perf_counter
from sympy import Matrix,I,symbols,trace
s=perf_counter();print('Started UTC',datetime.now(timezone.utc).isoformat())
g=Matrix.diag(I,-I)
B=[Matrix([[0,1],[0,0]]),Matrix([[0,0],[1,0]]),Matrix.diag(1,-1)]
t=trace(g);dt=Matrix([[trace(g*y) for y in B]]);dtsq=2*t*dt
assert t==0 and dt.rank()==1 and dtsq.rank()==0
print('SL2 lift diag(i,-i), trace =',t)
print('Derivative of trace on e,f,h =',list(dt))
print('Derivative of trace squared =',list(dtsq))
print('SL2 quotient rank =',dt.rank(),'; PGL2 quotient rank =',dtsq.rank())
print('PASS; elapsed seconds',perf_counter()-s)

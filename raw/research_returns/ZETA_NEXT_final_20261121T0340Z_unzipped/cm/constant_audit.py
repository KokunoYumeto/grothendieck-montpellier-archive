"""Numerical evaluation of the explicit NC constants, in log scale.
This is an arithmetic audit, not a formal certificate of the theorems.
Only Python's standard library is used.
"""
import math
import sys
from fractions import Fraction


def constants(r):
    alpha = 1024*r**3
    logc = math.log(2)-math.log(173)-r*math.log(2*math.pi)-math.lgamma(2*r+1)
    if r > 1:
        logc += (r-1)*(math.log(4*(r-1))-1)
    a = 2**(r-1)*(37.5+16*math.factorial(r))
    b = 4*r*(2**r-1)
    U = a+(b+1)/math.log(3)
    logB = 64*r*r*math.log(14*r)
    eta = Fraction(1,16*alpha)
    q = 2+r/(2*alpha)
    logf = logc/(2*alpha)-r/alpha*math.log(2)-logB-2*math.log(U)
    logell = min(0.0, logf+q*(1+math.log(float(eta))-math.log(q)))
    assert eta + eta == Fraction(1,8*alpha)
    assert q > 2 and U > 1 and logell <= 0
    return dict(r=r,alpha=alpha,logc=logc,a=a,b=b,U=U,logB=logB,
                eta=eta,q=q,logell=logell)


def all_cm(g):
    cs = [constants(r) for r in range(1,g+1)]
    z = cs[-1]
    alpha = z['alpha']
    beta = 16*alpha
    logM = max(-16*x['alpha']*x['logell'] for x in cs)
    astar = max(x['a'] for x in cs)
    bstar = max(x['b'] for x in cs)
    V = 1+g*(astar*(logM+beta)+bstar)
    P = 28*g*alpha
    logT = g*logM+4*g*alpha*(z['logB']+2*math.log(V))
    logs = math.log(2)+4*g*g*math.log(3)
    logcoef = -logs-logT/P
    assert P == g*beta + 12*g*alpha == 28672*g**4
    return z, P, logcoef, logM, V


if __name__ == '__main__':
    print('dimension\tNC01_log_constant\tNC03_exponent\tNC03_log_constant\tNC04_exponent\tNC04_log_constant')
    for g in range(1,9):
        z,P,logcoef,logM,V = all_cm(g)
        logs = math.log(2)+4*g*g*math.log(3)
        print(f"{g}\t{z['logc']:.9g}\t{z['eta']}\t{z['logell']-logs:.9g}\t1/{P}\t{logcoef:.9g}")
    # Independently inspect the two calculus optimizations used in the proof.
    for power in [1,2,3,8,2+1/2048]:
        for decay in [1/8,1/16384,1/131072]:
            t0=power/decay
            bound=power*(math.log(power/decay)-1)
            for factor in [0.01,0.1,0.5,1,2,10,100]:
                t=t0*factor
                assert power*math.log(t)-decay*t <= bound+1e-10
    print('Rational exponent identities and sampled numerical optimizations: PASS', file=sys.stderr)

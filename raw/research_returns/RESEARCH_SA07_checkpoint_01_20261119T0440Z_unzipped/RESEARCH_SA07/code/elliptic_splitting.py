"""Reproducible numerical normalization checks, not transcendence tests.

Python 3 + mpmath and SymPy. Inputs are exact (g2,g3) pairs. The root and
elliptic-integral calculations are floating-point, so the printed series tail
estimates bound truncation for the computed q only, not all numerical error.
"""
import time
import mpmath as mp
from fractions import Fraction

def eisenstein(tau, N):
    q = mp.exp(2j*mp.pi*tau)
    series, tails = {}, {}
    r = abs(q)
    for weight,s,c in ((2,1,-24),(4,3,240),(6,5,-504)):
        value = mp.mpc(1)
        for n in range(1,N+1):
            divisor_sum=sum(d**s for d in range(1,n+1) if n%d==0)
            value += c*divisor_sum*q**n
        ratio = r*mp.mpf(N+2)**(s+1)/mp.mpf(N+1)**(s+1)
        bound = abs(c)*(N+1)**(s+1)*r**(N+1)/(1-ratio)
        series[weight]=value
        tails[weight]=bound
    return series,tails,q

def run(g2,g3,dps):
    mp.mp.dps=dps
    t0=time.perf_counter()
    roots=sorted(mp.polyroots([4,0,-g2,-g3],maxsteps=200),reverse=True)
    e1,e2,e3=roots
    m=(e2-e3)/(e1-e3)
    w1=2*mp.ellipk(m)/mp.sqrt(e1-e3)
    w2=2j*mp.ellipk(1-m)/mp.sqrt(e1-e3)
    tau=w2/w1
    N=2*dps
    E,tails,q=eisenstein(tau,N)
    eta1=mp.pi**2*E[2]/(3*w1)
    eta1_integral=2*mp.sqrt(e1-e3)*mp.ellipe(m)-e1*w1
    eta2=-2j*mp.sqrt(e1-e3)*mp.ellipe(1-m)-e3*w2
    h_period=(eta1*mp.conj(w2)-eta2*mp.conj(w1))/(w1*mp.conj(w2)-w2*mp.conj(w1))
    E2star=E[2]-3/(mp.pi*tau.imag)
    h_modular=mp.pi**2*E2star/(3*w1**2)
    print(f'INPUT g2={g2}, g3={g3}, decimal_precision={dps}, N={N}')
    print('exact_discriminant=',g2**3-27*g3**2)
    print('exact_j=',Fraction(1728*g2**3,g2**3-27*g3**2))
    for label,x in [('w1',w1),('w2',w2),('tau',tau),('eta1',eta1),('eta2',eta2),('q',q),('E2star',E2star),('E4',E[4]),('E6',E[6]),('h',h_period)]:
        print(label,'=',mp.nstr(x,70))
    print('h_formula_residual=',mp.nstr(abs(h_period-h_modular),8))
    print('eta1_elliptic_integral_vs_q_series=',mp.nstr(abs(eta1-eta1_integral),8))
    print('Legendre_residual=',mp.nstr(abs(eta1*w2-eta2*w1-2j*mp.pi),8))
    print('g2_reconstruction_residual=',mp.nstr(abs(4*mp.pi**4*E[4]/(3*w1**4)-g2),8))
    print('g3_reconstruction_residual=',mp.nstr(abs(8*mp.pi**6*E[6]/(27*w1**6)-g3),8))
    print('series_tail_estimates=',{w:mp.nstr(tails[w],8) for w in tails})
    print('runtime_seconds=',f'{time.perf_counter()-t0:.6f}')

for parameters in [(4,0),(30,28),(4,1)]:
    for precision in [80,160]:
        run(*parameters,precision)

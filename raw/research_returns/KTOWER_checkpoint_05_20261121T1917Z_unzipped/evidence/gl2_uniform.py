"""Uniform complete level-three Hecke model, independently expanded in KTOWER.

Basis: D a^(2e-5-3j) b^j, from K17-GL2-GENERAL.
This implementation obtains eta-product coefficients from logarithmic
derivatives, rather than the predecessor's binomial product expansion.
All arithmetic is integral.  It makes no Galois-coverage or K-group claim.
"""
from pathlib import Path
from math import gcd
import argparse, json, time, sys
from flint import fmpz_poly, fmpz_mat

sys.set_int_max_str_digits(0)

def chi(n):
    return 0 if n % 3 == 0 else 1 if n % 3 == 1 else -1

def arithmetic_series(nmax):
    sig = [0]*(nmax+1)
    theta = [0]*(nmax+1)
    theta[0] = 1
    for d in range(1,nmax+1):
        for n in range(d,nmax+1,d):
            sig[n] += d
            theta[n] += 6*chi(d)
    return sig, theta

def eta_coefficients(s,t,nmax,sig):
    # prod_(n>=1)(1-q^n)^s(1-q^(3n))^t.
    c = [1]+[0]*nmax
    logder = [0]+[-s*sig[n]-(3*t*sig[n//3] if n % 3 == 0 else 0)
                  for n in range(1,nmax+1)]
    for n in range(1,nmax+1):
        c[n],rem = divmod(sum(logder[i]*c[n-i] for i in range(1,n+1)),n)
        assert rem == 0
    return [0]+c[:-1]

def cm_value(e,p):
    if e%3: return None
    # Unique unramified algebraic Hecke character over Q(omega).
    if p%3 == 2: return 0
    pi = next(( (a,b) for a in range(-p,p+1) for b in range(-p,p+1)
                if a*a-a*b+b*b == p),None)
    assert pi is not None
    a,b=1,0
    for _ in range(2*e):
        a,b = a*pi[0]-b*pi[1], a*pi[1]+b*pi[0]-b*pi[1]
    return 2*a-b

def compute(e,primes):
    start=time.monotonic()
    r=max(0,(2*e-2)//3)
    precision=max(primes)*(r+4)
    sig,aa=arithmetic_series(precision)
    bb=eta_coefficients(-3,9,precision,sig)
    dd=eta_coefficients(6,6,precision,sig)
    aa,bb,dd=map(fmpz_poly,(aa,bb,dd))
    def powers(f,n):
        out=[fmpz_poly([1])]
        for _ in range(n):out.append((out[-1]*f).truncate(precision+1))
        return out
    ap=powers(aa,max(0,2*e-5));bp=powers(bb,max(0,r-1))
    basis=[list(map(int,(dd*ap[2*e-5-3*j]*bp[j]).truncate(precision+1)))
           for j in range(r)]
    for f in basis:f.extend([0]*(precision+1-len(f)))
    lead=[[f[n] for f in basis] for n in range(1,r+1)]
    assert all(lead[i][j] == int(i==j) for i in range(r) for j in range(i,r))
    results=[]
    for p in primes:
        columns=[]
        for f in basis:
            image=[f[p*n]+(chi(p)*p**(2*e)*f[n//p] if n%p==0 else 0)
                   for n in range(1,r+1)]
            co=[]
            for i in range(r):co.append(image[i]-sum(lead[i][j]*co[j] for j in range(i)))
            for n in range(1,precision//p+1):
                v=f[p*n]+(chi(p)*p**(2*e)*f[n//p] if n%p==0 else 0)
                assert v==sum(co[j]*basis[j][n] for j in range(r))
            columns.append(co)
        matrix=[[columns[j][i] for j in range(r)] for i in range(r)]
        A=fmpz_mat(matrix) if r else None
        cp=list(reversed(list(map(int,A.charpoly())))) if r else [1]
        x=1+chi(p)*p**(2*e)
        value=0
        for c in cp:value=value*x+c
        if r:
            shifted=fmpz_mat([[x*int(i==j)-matrix[i][j] for j in range(r)] for i in range(r)])
            assert value==int(shifted.det())
        cm=cm_value(e,p)
        if cm is not None:
            check=0
            for c in cp:check=check*cm+c
            assert check==0
        results.append({'p':p,'matrix':matrix,'charpoly_coefficients':cp,
                        'comparison_point':x,'comparison_value':value,'cm_eigenvalue':cm,
                        'hecke_coefficients_checked_through':precision//p})
    return {'e':e,'weight':2*e+1,'dimension':r,'cm_dimension':int(e%3==0),
            'non_cm_dimension':r-int(e%3==0),'precision':precision,
            'results':results,'elapsed_seconds':time.monotonic()-start}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--degrees',nargs='+',type=int,default=list(range(2,32,2)))
    parser.add_argument('--primes',nargs='+',type=int,default=[7,13])
    parser.add_argument('--output',default=str(Path(__file__).with_suffix('.json')))
    args=parser.parse_args()
    rows=[]
    for e in args.degrees:
        assert e>=2 and e%2==0
        row=compute(e,args.primes);rows.append(row)
        Path(args.output).write_text(json.dumps({'status':'PASS exact full modular models',
              'method':'logarithmic eta-product recurrence; integral triangular basis',
              'degrees':rows},indent=2)+'\n')
        print(json.dumps({k:row[k] for k in ['e','dimension','cm_dimension','elapsed_seconds']}),flush=True)

if __name__=='__main__':main()

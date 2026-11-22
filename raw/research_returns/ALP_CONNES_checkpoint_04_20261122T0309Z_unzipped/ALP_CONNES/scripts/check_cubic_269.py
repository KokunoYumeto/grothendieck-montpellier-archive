#!/usr/bin/env python3
"""Exact finite checks for AC-K04 and AC-K09. No RH claim is tested."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
from datetime import datetime, timezone

P = 269

def log_unit_interval(x, terms=80):
    assert F(1) <= x <= F(2)
    t = (x-1)/(x+1)
    a = sum((t**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))*2
    e = 2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return a, a+e

def log_interval(x):
    x=F(x); k=0
    assert x >= 1
    while x >= 2:
        x /= 2; k += 1
    lo,hi=log_unit_interval(x)
    l2,h2=log_unit_interval(F(2))
    return lo+k*l2,hi+k*h2

def atan_interval(x, terms=24):
    vals=[sum(((-1)**j*x**(2*j+1)/F(2*j+1)
               for j in range(n)),F(0)) for n in (terms,terms+1)]
    return min(vals),max(vals)

def sqrt_interval(n, scale=10**12):
    k=isqrt(n*scale*scale)
    return F(k,scale),F(k+1,scale)

def mul(x,y):
    a,b=x; c,d=y
    return ((a*c-b*d)%P,(a*d+b*c-b*d)%P)

def power(x,n):
    out=(1,0)
    while n:
        if n&1: out=mul(out,x)
        x=mul(x,x); n//=2
    return out

def primes(n):
    s=bytearray(b'\x01')*(n+1); s[0:2]=b'\x00\x00'
    for a in range(2,isqrt(n)+1):
        if s[a]:
            s[a*a:n+1:a]=b'\x00'*(((n-a*a)//a)+1)
    return [j for j in range(2,n+1) if s[j]]

def eisenstein_generator(l):
    for b in range(isqrt(4*l//3)+2):
        d=4*l-3*b*b
        if d<0: continue
        u=isqrt(d)
        if u*u==d and (u+b)%2==0:
            a=(u+b)//2
            assert a*a-a*b+b*b==l
            return a,b
    raise AssertionError(('no generator',l))

def main():
    a5,b5=atan_interval(F(1,5)); a239,b239=atan_interval(F(1,239))
    pi_lo,pi_hi=16*a5-4*b239,16*b5-4*a239
    # H_n-log(n+1) < gamma < H_n-log(n), from integral bounds.
    n=100
    harmonic=sum((F(1,j) for j in range(1,n+1)),F(0))
    gn_lo=harmonic-log_interval(n+1)[1]
    gn_hi=harmonic-log_interval(n)[0]
    logq=log_interval(3*P*P)
    c_lo=logq[0]-2*log_interval(8*pi_hi)[1]-2*gn_hi
    c_hi=logq[1]-2*log_interval(8*pi_lo)[0]-2*gn_lo
    bound_lo=2*(log_interval(3)[0]/sqrt_interval(3)[1]
                +log_interval(2)[0]
                +log_interval(7)[0]/sqrt_interval(7)[1])
    bound_hi=2*(log_interval(3)[1]/sqrt_interval(3)[0]
                +log_interval(2)[1]
                +log_interval(7)[1]/sqrt_interval(7)[0])
    assert c_lo-bound_hi>F(1,2)
    b4_lo=(sqrt_interval(2)[0]*log_interval(3)[0]/sqrt_interval(3)[1]
           +log_interval(2)[0]+log_interval(7)[0]/sqrt_interval(7)[1]
           +log_interval(3)[0]/3+log_interval(13)[0]/sqrt_interval(13)[1])
    b4_hi=(sqrt_interval(2)[1]*log_interval(3)[1]/sqrt_interval(3)[0]
           +log_interval(2)[1]+log_interval(7)[1]/sqrt_interval(7)[0]
           +log_interval(3)[1]/3+log_interval(13)[1]/sqrt_interval(13)[0])
    assert c_lo-b4_hi>1
    assert P in primes(P)
    assert (P*P-1)//6==12060
    assert ((P*P-1)//3)%6==0
    roots={(1,0),(0,1),(P-1,P-1)}
    checked=0; trivial=0; nontrivial=0
    for l in primes(100000):
        if l in (3,P): continue
        if l%3==2:
            assert power((l%P,0),(P*P-1)//3)==(1,0)
            continue
        a,b=eisenstein_generator(l)
        value=power((a%P,b%P),(P*P-1)//3)
        assert value in roots
        rational_cube=(pow(P,(l-1)//3,l)==1)
        assert (value==(1,0))==rational_cube,(l,(a,b),value)
        checked+=1
        if rational_cube: trivial+=1
        else: nontrivial+=1
    assert power((1,P-1),(P*P-1)//3)==(1,0) # prime above three
    # Hensel lift for t-3t^2+3t^3=30; derivative is 1 mod 3.
    t=0; modulus=3
    for _ in range(10):
        candidates=[t+j*modulus for j in range(3)]
        roots_t=[u for u in candidates if (u-3*u*u+3*u**3-30)%(3*modulus)==0]
        assert len(roots_t)==1
        t=roots_t[0]; modulus*=3
    alpha=(-1+3*t)%(9*modulus)
    assert (alpha**3-P)%(9*modulus)==0
    certificate={
       'checked_utc':datetime.now(timezone.utc).isoformat(),
       'type':'exact finite computation, not a zero-location certificate',
       'statements':['AC-K04','AC-K09'],
       'prime':P,'norm_conductor':P*P,'analytic_conductor':3*P*P,
       'ray_class_order':12060,'integral_host_index':P*P,
       'interval_method':'rational arctanh log series; Machin alternating atan; harmonic integral gamma bounds; integer sqrt',
       'archimedean_lower_interval':[float(c_lo),float(c_hi)],
       'translation_norm_bound_interval':[float(bound_lo),float(bound_hi)],
       'certified_margin_gt':'1/2',
       'lambda4_translation_bound':[float(b4_lo),float(b4_hi)],
       'lambda4_certified_margin_gt':'1',
       'split_primes_checked_through':100000,'split_primes_checked':checked,
       'cubic_trivial':trivial,'cubic_nontrivial':nontrivial,
       'hensel_root_modulus':9*modulus,'hensel_root':alpha,
       'outcome':'PASS',
    }
    target=Path(__file__).resolve().parents[1]/'evidence/cubic_269_certificate.json'
    target.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps(certificate,indent=2))

if __name__=='__main__': main()

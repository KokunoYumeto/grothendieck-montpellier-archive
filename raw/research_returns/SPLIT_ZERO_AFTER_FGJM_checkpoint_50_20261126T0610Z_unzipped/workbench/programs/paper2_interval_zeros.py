#!/usr/bin/env python3
"""Outward-rounded Euler--Maclaurin/Rouche certificates for Hurwitz zeros.

Only elementary mpmath.iv operations are used in the verifier. mpmath.findroot
supplies candidate centres, not evidence. Bernoulli numbers are exact rationals.
Run: python3 programs/paper2_interval_zeros.py --endpoints
The optional --paths mode subdivides parameter intervals until uniform Rouche
inequalities and endpoint overlap inclusions hold. No branch switch is inferred
from proximity alone.
"""
from pathlib import Path
from fractions import Fraction
import argparse, csv, json, math, time
from mpmath import mp, iv
mp.dps=70
iv.dps=45
N=40
M=24
OUT=Path(__file__).resolve().parents[1]/'checks'

def bernoulli(n):
    a=[]
    for m in range(n+1):
        a.append(Fraction(1,m+1))
        for j in range(m,0,-1): a[j-1]=j*(a[j-1]-a[j])
    return a[0]
BC=[None]+[bernoulli(2*k)/math.factorial(2*k) for k in range(1,M+1)]
def real(x):
    if isinstance(x,Fraction):return iv.mpf(x.numerator)/x.denominator
    return iv.mpf(str(x))
def point(z):return iv.mpc(real(mp.re(z)),real(mp.im(z)))
def box(z,r):
    zr,zi=real(mp.re(z)),real(mp.im(z));rr=real(r)
    return iv.mpc(iv.mpf([(zr-rr).a,(zr+rr).b]),iv.mpf([(zi-rr).a,(zi+rr).b]))
def add(u,v):return tuple(u[i]+v[i] for i in range(3))
def scale(u,c):return tuple(x*c for x in u)
def mul(u,v):
    return (u[0]*v[0],u[1]*v[0]+u[0]*v[1],u[2]*v[0]+2*u[1]*v[1]+u[0]*v[2])
def powerjet(s,x,shift=0):
    l=iv.log(x);v=iv.exp((shift-s)*l)
    return v,-l*v,l*l*v
def em(s,a):
    z=iv.mpc(0);total=(z,z,z)
    for n in range(N):total=add(total,powerjet(s,a+n))
    A=a+N;inv=1/(s-1)
    total=add(total,mul(powerjet(s,A,1),(inv,-inv*inv,2*inv*inv*inv)))
    total=add(total,scale(powerjet(s,A),real(Fraction(1,2))))
    rising=(iv.mpc(1),z,z)
    for j in range(2*M):
        rising=mul(rising,(s+j,iv.mpc(1),z))
        if j%2==0:
            k=(j+2)//2
            total=add(total,scale(mul(rising,powerjet(s,A,-j-1)),real(BC[k])))
    # Integral remainder and its first two s derivatives. For A>1 the
    # logarithmic moments are elementary. 4/(2*pi)^(2M) bounds Btilde/(2M)!.
    b=s.real+2*M;v=1/(b-1);l=iv.log(A)
    J0=iv.exp((1-b)*l)*v
    J1=J0*(l+v)
    J2=J0*(l*l+2*l*v+2*v*v)
    fac=4/(2*iv.pi)**(2*M)
    p0,p1,p2=map(abs,rising)
    R=(fac*p0*J0,fac*(p1*J0+p0*J1),fac*(p2*J0+2*p1*J1+p0*J2))
    return total,R
def hi(x):return x.b
def lo(x):return x.a
def fstr(x):return mp.nstr(mp.mpf(x._mpi_[1]),25)
def rout(z,a0,ah,r):
    s=point(z);a=real(a0);h=real(ah);rr=real(r)
    A=iv.mpf([(a-h).a,(a+h).b])
    centre,rem=em(s,a)
    broad,brem=em(box(z,r),A)
    upper2=hi(abs(broad[2]))+hi(brem[2])
    shifted,srem=em(s+1,A)
    za=hi(abs(shifted[0]))+hi(srem[0])
    zas=hi(abs(shifted[1]))+hi(srem[1])
    T=hi(abs(s))*za
    U=za+hi(abs(s))*zas
    residual=hi(abs(centre[0]))+hi(rem[0])
    error=residual+h*T+rr*(hi(rem[1])+h*U)+rr*rr*upper2/2
    linear=lo(abs(centre[1]))*rr
    ok=bool(error.b < linear.a)
    return ok,dict(centre_real=str(z.real),centre_imag=str(z.imag),
                  parameter_mid=str(a0),parameter_half_width=str(ah),radius=str(r),
                  residual_bound=fstr(residual),second_derivative_bound=fstr(upper2),
                  rouche_error_upper=fstr(error),linear_lower=mp.nstr(mp.mpf(linear._mpi_[0]),25),
                  ratio_upper=fstr(error/linear),passed=ok)

def candidates():
    p=OUT/'paper2_zero_motion_summary.json'
    data=json.loads(p.read_text())
    return data

def endpoint_mode():
    rows=list(csv.DictReader((OUT/'paper2_zero_motion.tsv').open(),delimiter='\t'))
    print('columns',list(rows[0]),flush=True)
    output=[]
    for k in range(1,6):
        matching=[r for r in rows if int(r['root'])==k]
        last=matching[-1]
        z=mp.mpc(last.get('real',last.get('re')),last.get('imag',last.get('im')))
        z=mp.findroot(lambda w:mp.zeta(w,2),z,tol=mp.mpf('1e-65'))
        ok,rec=rout(z,mp.mpf(2),mp.mpf(0),mp.mpf('1e-12'))
        rec['branch']=k;output.append(rec)
        print(k,ok,rec['ratio_upper'],flush=True)
    assert all(r['passed'] for r in output)
    (OUT/'paper2_endpoint_interval_certificate.json').write_text(json.dumps(dict(
        algorithm='Euler--Maclaurin jets and Rouche inequality',interval_library='mpmath.iv',
        interval_dps=iv.dps,N=N,M=M,certificates=output,
        meaning='Each disc contains exactly one simple zero at parameter a=2; branch identity is a separate check.'),indent=2)+'\n')

def path_mode(branch):
    # Every accepted slab contains exactly one simple zero for EVERY real
    # parameter in its interval. Small endpoint discs prove overlap identity.
    t=Fraction(0);step=Fraction(1,64);tiny=mp.mpf('1e-12')
    z=mp.zetazero(branch)
    ok,initial=rout(z,Fraction(1),Fraction(0),tiny)
    assert ok
    slabs=[];endpoints=[initial];attempts=0;started=time.time()
    while t<1:
        h=min(step,1-t);mid=1+t+h/2;right=1+t+h
        amid=mp.mpf(mid.numerator)/mid.denominator
        aright=mp.mpf(right.numerator)/right.denominator
        zm=mp.findroot(lambda w:mp.zeta(w,amid),(z,z+mp.mpf('0.00001')),tol=mp.mpf('1e-63'))
        zr=mp.findroot(lambda w:mp.zeta(w,aright),(zm,zm+mp.mpf('0.00001')),tol=mp.mpf('1e-63'))
        distance=max(abs(z-zm),abs(zr-zm))
        radius=mp.mpf('1.3')*distance+mp.mpf('1e-9')
        ok,cert=rout(zm,mid,h/2,radius)
        attempts+=1
        if ok:
            # Interval, outward-rounded inclusion; proximity alone is not used.
            for zz in [z,zr]:
                if not bool((abs(point(zz)-point(zm))+real(tiny)).b < real(radius).a):ok=False
        if ok:
            endpoint_ok,ep=rout(zr,right,Fraction(0),tiny)
            ok=endpoint_ok
        if not ok:
            step=h/2
            if step<Fraction(1,262144):raise RuntimeError(f'Unresolved slab at t={t}')
            continue
        cert.update(t_left=str(t),t_right=str(t+h),endpoint_index=len(endpoints),overlap_inclusion=True)
        slabs.append(cert);endpoints.append(ep);t+=h;z=zr
        if len(slabs)%50==0:
            print(json.dumps(dict(branch=branch,t=float(t),slabs=len(slabs),seconds=round(time.time()-started,1))),flush=True)
        if float(cert['ratio_upper'])<0.35:step=min(2*h,Fraction(1,64))
    result=dict(branch=branch,algorithm='Uniform Rouche slabs with certified endpoint-disc overlap',
        interval_library='mpmath.iv',interval_dps=iv.dps,N=N,M=M,
        parameter='a=1+t, t in [0,1]',initial=initial,slabs=slabs,endpoints=endpoints,
        attempts=attempts,elapsed_seconds=time.time()-started,
        conclusion='One continuous simple-zero branch joins the specified initial and final discs; each disc has radius 1e-12.')
    dest=OUT/f'paper2_path_{branch}_interval_certificate.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(branch=branch,complete=True,slabs=len(slabs),attempts=attempts,file=str(dest))),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--endpoints',action='store_true');p.add_argument('--branch',type=int);args=p.parse_args()
    if args.branch:path_mode(args.branch)
    else:endpoint_mode()

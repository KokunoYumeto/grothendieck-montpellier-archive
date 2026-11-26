#!/usr/bin/env python3
"""Independent full Hurwitz-certificate verifier, CC0-1.0.

Written from certified_hurwitz.tex and the saved rational/decimal geometry.
No producer or earlier reviewer code was read or imported. Rising-factorial
derivatives use logarithmic derivatives (reciprocal sums), not derivative jets.
Default Euler--Maclaurin parameters N=50,M=28 differ from the producer's40,24.
Only exact candidate geometry is consumed; displayed numerical bounds and
producer acceptance flags are ignored. All acceptance arithmetic uses mpmath.iv.
"""
from __future__ import annotations

import argparse
import concurrent.futures
from fractions import Fraction
from math import comb, factorial
import hashlib
import json
from pathlib import Path
import time

import mpmath as mp

IV = mp.iv
N = 50
M = 28
DPS = 60
COEFF = []


def rational(x):
    return Fraction(str(x))


def ivq(x):
    q = x if isinstance(x, Fraction) else rational(x)
    return IV.mpf(q.numerator) / IV.mpf(q.denominator)


def interval(lo, hi):
    # Construct an enclosure from outward enclosures of exact rational endpoints.
    return IV.mpf([ivq(lo).a, ivq(hi).b])


def point(re, im):
    return IV.mpc(ivq(re), ivq(im))


def upper_text(x, digits=28):
    # Display only. All decisions below compare the original interval endpoints.
    return mp.nstr(mp.mpf(x._mpi_[1]), digits)


def upper_key(x):
    return mp.mpf(x._mpi_[1])


def largest_upper(values):
    return max(values, key=upper_key)


def configure(n, m, dps):
    global N, M, DPS, COEFF
    assert n >= 1 and m >= 1 and dps >= 30
    N, M, DPS = n, m, dps
    IV.dps = dps
    mp.mp.dps = dps + 15
    # Exact Faulhaber recurrence: sum_{j=0}^n binom(n+1,j)B_j=0 for n>=1.
    bernoulli = [Fraction(1)]
    for j in range(1, 2*M+1):
        bernoulli.append(-sum(Fraction(comb(j+1, k))*bernoulli[k]
                              for k in range(j))/(j+1))
    COEFF = [None] + [ivq(bernoulli[2*k]/factorial(2*k))
                      for k in range(1, M+1)]


def euler_maclaurin(s, a, order=2):
    """Enclose G and its s derivatives; then explicit remainder bounds.

    P_d=(s)_d, H1=sum 1/(s+j), H2=sum 1/(s+j)^2 give
    P_d'=P_d H1 and P_d''=P_d(H1^2-H2).
    All evaluation boxes have imaginary part >14, so denominators avoid zero.
    """
    z0 = IV.mpc(0)
    g0, g1, g2 = z0, z0, z0
    for j in range(N):
        ell = IV.log(a+j)
        term = IV.exp(-s*ell)
        g0 += term
        if order >= 1:
            g1 -= ell*term
        if order >= 2:
            g2 += ell*ell*term

    A = N+a
    ell = IV.log(A)
    inv = 1/(s-1)
    tail = IV.exp((1-s)*ell)*inv
    half = IV.exp(-s*ell)/2
    g0 += tail+half
    if order >= 1:
        g1 += tail*(-ell-inv)-ell*half
    if order >= 2:
        g2 += tail*((ell+inv)**2+inv**2)+ell**2*half

    prod = IV.mpc(1)
    h1, h2 = IV.mpc(0), IV.mpc(0)
    for d in range(1, 2*M+1):
        factor = s+d-1
        reciprocal = 1/factor
        prod *= factor
        h1 += reciprocal
        h2 += reciprocal**2
        if d % 2:
            k = (d+1)//2
            term = COEFF[k]*prod*IV.exp(-(s+d)*ell)
            g0 += term
            if order >= 1:
                g1 += term*(h1-ell)
            if order >= 2:
                g2 += term*((h1-ell)**2-h2)

    # Use the smallest A and real part for the positive integral bounds.
    Amin = A.a
    Bmin = s.real.a+2*M
    v = 1/(Bmin-1)
    ellmin = IV.log(Amin)
    j0 = IV.exp((1-Bmin)*ellmin)*v
    j1 = j0*(ellmin+v)
    j2 = j0*(ellmin**2+2*v*ellmin+2*v**2)
    constant = 4/(2*IV.pi)**(2*M)
    p0 = abs(prod)
    p1 = abs(prod*h1)
    p2 = abs(prod*(h1**2-h2))
    r0 = constant*p0*j0
    r1 = constant*(p1*j0+p0*j1)
    r2 = constant*(p2*j0+2*p1*j1+p0*j2)
    return (g0,g1,g2),(r0,r1,r2)


def split_range(lo, hi, pieces):
    return [(lo+(hi-lo)*j/pieces, lo+(hi-lo)*(j+1)/pieces)
            for j in range(pieces)]


def certificate_geometry(row):
    return tuple(rational(row[k]) for k in
                 ('centre_real','centre_imag','parameter_mid',
                  'parameter_half_width','radius'))


def verify_disc(row):
    cr, ci, a0, h, radius = certificate_geometry(row)
    assert radius > 0 and h >= 0 and a0-h > 0
    c = point(cr,ci)
    a_mid, rad, half_width = ivq(a0), ivq(radius), ivq(h)
    (g0,g1,_),(r0,r1,_) = euler_maclaurin(c,a_mid,1)
    # Choose an explicit decimal-rational b from the derivative enclosure.
    br = mp.nstr(mp.mpf(g1.real.mid._mpi_[0]), DPS-8)
    bi = mp.nstr(mp.mpf(g1.imag.mid._mpi_[0]), DPS-8)
    b = point(br,bi)
    epsilon = abs(g0)+r0
    delta = abs(g1-b)+r1
    right = rad*abs(b)

    for pieces in (1,2,4):
        a_cells = split_range(a0-h,a0+h,pieces if h else 1)
        if h:
            t_values, u_values = [], []
            for al, ar in a_cells:
                (q0,q1,_),(e0,e1,_) = euler_maclaurin(c+1,interval(al,ar),1)
                t_values.append(abs(c)*(abs(q0)+e0))
                u_values.append(abs(q0)+e0+abs(c)*(abs(q1)+e1))
            T, U = largest_upper(t_values), largest_upper(u_values)
        else:
            T = U = IV.mpf(0)
        second_values = []
        for xl,xr in split_range(cr-radius,cr+radius,pieces):
            for yl,yr in split_range(ci-radius,ci+radius,pieces):
                s = IV.mpc(interval(xl,xr),interval(yl,yr))
                for al,ar in a_cells:
                    (_,_,q2),(_,_,e2) = euler_maclaurin(s,interval(al,ar),2)
                    second_values.append(abs(q2)+e2)
        second = largest_upper(second_values)
        left = epsilon+half_width*T+rad*(delta+half_width*U)+second*rad**2/2
        if bool(left.b < right.a):
            return {'passed':True,'ratio_upper_display':upper_text(left/right),
                    'left_upper_display':upper_text(left),
                    'right_lower_display':mp.nstr(mp.mpf(right._mpi_[0]),28),
                    'bound_subdivision':pieces,
                    'epsilon_upper_display':upper_text(epsilon),
                    'M2_upper_display':upper_text(second)}
    return {'passed':False,'ratio_upper_display':upper_text(left/right),
            'left_upper_display':upper_text(left),
            'right_lower_display':mp.nstr(mp.mpf(right._mpi_[0]),28),
            'bound_subdivision':pieces}


def strict_containment(inner,outer):
    x,y,_,_,r = certificate_geometry(inner)
    u,v,_,_,R = certificate_geometry(outer)
    return bool((abs(point(x-u,y-v))+ivq(r)).b < ivq(R).a)


DISPLAY_START = ['14.134725141735','21.022039638772','25.010857580146',
                 '30.424876125860','32.935061587739']
DISPLAY_END = [('1.407788040653','23.327987754559'),
               ('0.410921753828','31.715410442191'),
               ('1.367688181122','38.419105560643'),
               ('0.594418197071','42.399454183542'),
               ('0.245270111140','48.772923691752')]


def run_branch(args):
    branch, directory, out_dir, n, m, dps = args
    configure(n,m,dps)
    started=time.monotonic()
    path=Path(directory)/f'paper2_path_{branch}_interval_certificate.json'
    data=json.loads(path.read_text())
    slabs,endpoints=data['slabs'],data['endpoints']
    assert len(endpoints)==len(slabs)+1
    assert rational(slabs[0]['t_left'])==0
    assert rational(slabs[-1]['t_right'])==1
    previous=Fraction(0)
    for j,s in enumerate(slabs):
        lo,hi=rational(s['t_left']),rational(s['t_right'])
        assert lo==previous and lo<hi
        assert rational(s['parameter_mid'])==1+(lo+hi)/2
        assert rational(s['parameter_half_width'])==(hi-lo)/2
        assert int(s['endpoint_index'])==j+1
        assert rational(endpoints[j]['parameter_mid'])==1+lo
        assert rational(endpoints[j+1]['parameter_mid'])==1+hi
        assert rational(endpoints[j]['parameter_half_width'])==0
        assert rational(endpoints[j+1]['parameter_half_width'])==0
        assert strict_containment(endpoints[j],s)
        assert strict_containment(endpoints[j+1],s)
        previous=hi
    assert certificate_geometry(data['initial'])==certificate_geometry(endpoints[0])

    result={'branch':branch,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'N':N,'M':M,'interval_dps':DPS,'geometry_passed':True,
            'slabs':[],'endpoints':[]}
    for kind,rows in [('slabs',slabs),('endpoints',endpoints)]:
        for j,row in enumerate(rows):
            check=verify_disc(row)
            check['index']=j
            result[kind].append(check)
            if not check['passed']:
                print(json.dumps({'branch':branch,'kind':kind,'failed_index':j,
                                  'ratio':check['ratio_upper_display']}),flush=True)
            if (j+1)%64==0 or j+1==len(rows):
                print(json.dumps({'branch':branch,'kind':kind,'done':j+1,
                                  'total':len(rows),
                                  'elapsed_seconds':round(time.monotonic()-started,2)}),flush=True)
    table_tests=[]
    for side,j,re,im in [('initial',0,'0.5',DISPLAY_START[branch-1]),
                         ('final',-1,*DISPLAY_END[branch-1])]:
        table=dict(endpoints[j],centre_real=re,centre_imag=im,radius='0.000000000002')
        assert strict_containment(endpoints[j],table)
        assert strict_containment(table,slabs[j])
        table_tests.append({'side':side,'small_disc_contained':True,
                            'display_disc_inside_uniform_disc':True})
    result['table_geometry']=table_tests
    result['all_passed']=all(t['passed'] for k in ['slabs','endpoints'] for t in result[k])
    result['maximum_slab_ratio_display']=max(float(t['ratio_upper_display']) for t in result['slabs'])
    result['maximum_endpoint_ratio_display']=max(float(t['ratio_upper_display']) for t in result['endpoints'])
    result['elapsed_seconds']=round(time.monotonic()-started,3)
    dest=Path(out_dir)/f'paper4_hurwitz_recheck_branch_{branch}.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'branch':branch,'complete':True,'all_passed':result['all_passed'],
                      'max_slab_ratio_display':result['maximum_slab_ratio_display']}),flush=True)
    return {k:v for k,v in result.items() if k not in ('slabs','endpoints')}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--directory',default='checks')
    parser.add_argument('--output-directory',default='checks')
    parser.add_argument('--branches',type=int,nargs='+',default=[1,2,3,4,5])
    parser.add_argument('--workers',type=int,default=5)
    parser.add_argument('--N',type=int,default=50)
    parser.add_argument('--M',type=int,default=28)
    parser.add_argument('--dps',type=int,default=60)
    parser.add_argument('--sample',action='store_true')
    args=parser.parse_args()
    out_dir=Path(args.output_directory);out_dir.mkdir(parents=True,exist_ok=True)
    if args.sample:
        configure(args.N,args.M,args.dps)
        data=json.loads((Path(args.directory)/'paper2_path_1_interval_certificate.json').read_text())
        for label,row in [('first_slab',data['slabs'][0]),('first_endpoint',data['endpoints'][0])]:
            started=time.monotonic();res=verify_disc(row)
            print(label,json.dumps(res),'seconds',time.monotonic()-started,flush=True)
        return
    started=time.monotonic()
    configure(args.N,args.M,args.dps)
    initial=[]
    for branch in args.branches:
        data=json.loads((Path(args.directory)/f'paper2_path_{branch}_interval_certificate.json').read_text())
        initial.append(data['endpoints'][0])
        assert len(data['slabs']) == (502 if branch==1 else 512)
        if branch in (1,3):
            end=data['endpoints'][-1]
            assert bool((ivq(end['centre_real'])-ivq(end['radius'])).a > IV.mpf(1).b)
    for i,a in enumerate(initial):
        for b in initial[:i]:
            ax,ay,_,_,ar=certificate_geometry(a)
            bx,by,_,_,br=certificate_geometry(b)
            assert bool(abs(point(ax-bx,ay-by)).a > (ivq(ar)+ivq(br)).b)
    external=json.loads((Path(args.directory)/'paper2_endpoint_interval_certificate.json').read_text())
    external_tests=[]
    for row in external['certificates']:
        if row['branch'] in args.branches:
            check=verify_disc(row)
            assert rational(row['parameter_mid'])==2 and rational(row['parameter_half_width'])==0
            data=json.loads((Path(args.directory)/f"paper2_path_{row['branch']}_interval_certificate.json").read_text())
            assert strict_containment(row,data['slabs'][-1])
            check['branch']=row['branch']
            external_tests.append(check)
    jobs=[(b,args.directory,str(out_dir),args.N,args.M,args.dps) for b in args.branches]
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        results=list(pool.map(run_branch,jobs))
    summary={'algorithm':'independent EM reciprocal-sum derivatives and full Rouche/geometry verification',
             'library':'mpmath.iv '+mp.__version__,'N':args.N,'M':args.M,'interval_dps':args.dps,
             'producer_code_read':False,'producer_numeric_bounds_used':False,
             'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'initial_discs_pairwise_disjoint':True,
             'final_real_parts_1_and_3_above_one':True,
             'standalone_endpoint_tests':external_tests,
             'branches':results,'all_passed':all(r['all_passed'] for r in results),
             'elapsed_seconds':round(time.monotonic()-started,3),
             'display_note':'Numerical summaries are rounded displays. Decisions compare outward interval endpoints.'}
    (out_dir/'paper4_hurwitz_recheck.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)
    if not summary['all_passed'] or not all(r['passed'] for r in external_tests):raise SystemExit(1)


if __name__=='__main__':
    main()

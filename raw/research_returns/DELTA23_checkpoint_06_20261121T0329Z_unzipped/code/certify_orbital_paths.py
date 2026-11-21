#!/usr/bin/env python3
"""Exact crossing certificate for polygonal orbital-coface paths.

Coordinates lie in Q(sqrt(3),i). Every projected crossing is isolated
by a rational Sturm interval for a polynomial of degree at most six.
This independently checks the geometric discovery words; it does not
assume a sampled floating-point braid diagram.
"""
from pathlib import Path
import sys, json, itertools, math, time
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/agents/five_level_six'))
from cyclic12_cover import braid,red,wi
t=sp.Symbol('t');s=sp.sqrt(3);QQ=sp.QQ
K=QQ.algebraic_field(s)
q=sp.Rational
zero=sp.Poly(0,t,domain=K)
one=sp.Poly(1,t,domain=K)
def poly(x):return sp.Poly(x,t,domain=K)
def complex_pair(re,im=0):return (sp.sympify(re),sp.sympify(im))
def add(a,b):return (sp.expand(a[0]+b[0]),sp.expand(a[1]+b[1]))
def scale(c,a):return (sp.expand(c*a[0]),sp.expand(c*a[1]))
def cmul(a,b):return (sp.expand(a[0]*b[0]-a[1]*b[1]),sp.expand(a[0]*b[1]+a[1]*b[0]))
zeta=(-q(1,2),s/2)
vertices=[(1,0),(s/2,q(1,2)),(q(1,2),s/2),(0,1),(-q(1,2),s/2),(-s/2,q(1,2)),(-1,0),(-s/2,-q(1,2)),(-q(1,2),-s/2),(0,-1),(q(1,2),-s/2),(s/2,-q(1,2)),(1,0)]
base=(complex_pair(1),complex_pair(4))
small=q(1,5);close=q(101,100);radius=q(1,20)

def lollipop(center,start):
    # Positive diamond, with the base path on the positive real ray.
    c=sp.sympify(center);r=radius*c
    return [complex_pair(start),(c+r,0),(c,r),(c-r,0),(c,-r),(c+r,0),complex_pair(start)]

def source(word):
    if word in ('u','U'):
        n=4 if word=='u' else 12
        return [(v,base[1]) for v in vertices[:n+1]]
    j=int(word[1:]);turn=vertices[:4*j+1]
    out=[(v,base[1]) for v in turn]
    out.extend((turn[-1],v) for v in lollipop(1,4)[1:])
    out.extend((v,base[1]) for v in turn[-2::-1])
    return out

def target(face,word):
    coords=[]
    if face==0:
        for v in lollipop(1 if word=='x' else 4,4 if word=='x' else q(15,2)):
            coords.append((base[0],v,complex_pair(q(15,2))) if word=='x' else (base[0],base[1],v))
    else:
        for u,v in source(word):
            if face==1:w=(scale(small,u),u,v)
            elif face==2:w=(u,scale(close,u),v)
            elif face==3:w=(u,v,scale(close,v))
            else:w=(u,v,complex_pair(q(15,2)))
            coords.append(w)
    return [(cmul(zeta,u),cmul(cmul(zeta,zeta),u),u,v,w) for u,v,w in coords]

def imul(a,b):
    p=[x*y for x in a for y in b];return min(p),max(p)
def iadd(a,b):return a[0]+b[0],a[1]+b[1]
SQRT_SCALE=10**40
SQRT_FLOOR=math.isqrt(3*SQRT_SCALE**2)
sqrt_interval=(q(SQRT_FLOOR,SQRT_SCALE),q(SQRT_FLOOR+1,SQRT_SCALE))
def coefficient_interval(v):
    v=sp.expand(v);b=v.coeff(s);a=sp.expand(v-b*s)
    assert a.is_Rational and b.is_Rational,(a,b)
    return iadd((a,a),imul((b,b),sqrt_interval))
def interval_value(p,ab):
    out=(q(0),q(0))
    for c in p.all_coeffs():out=iadd(imul(out,ab),coefficient_interval(c))
    return out
def stable_sign(p,ab):
    lo,hi=interval_value(p,ab)
    return 1 if lo>0 else (-1 if hi<0 else None)
def split(p):
    aa=[];bb=[]
    for c in p.all_coeffs():
        c=sp.expand(c);b=c.coeff(s);a=sp.expand(c-b*s)
        aa.append(a);bb.append(b)
    return sp.Poly.from_list(aa,t,domain=QQ),sp.Poly.from_list(bb,t,domain=QQ)

root_cache={}
def crossing_roots(n,m):
    if n.is_zero:raise AssertionError('Identically equal projected coordinates')
    if n.degree()==0:return []
    a,b=split(n);norm=(a*a-3*b*b).sqf_part()
    key=tuple(norm.monic().all_coeffs())
    if key not in root_cache:root_cache[key]=norm.intervals(eps=q(1,10**18))
    out=[]
    for (lo,hi),mult in root_cache[key]:
        if hi<=0 or lo>=1:continue
        assert 0<lo<=hi<1,(lo,hi,n)
        ab=(lo,hi)
        if not b.is_zero:
            gcd=sp.gcd(a,b)
            common=(gcd.degree()>0 and gcd.count_roots(lo,hi)>0)
            if not common:
                sa=stable_sign(a,ab);sb=stable_sign(b,ab)
                assert sa is not None and sb is not None
                if sa==sb:continue
        dn=stable_sign(n.diff(),ab);im=stable_sign(m,ab)
        assert dn is not None and im is not None,(n,m,ab,dn,im)
        out.append({'lo':lo,'hi':hi,'sign':-dn*im,
                    'norm_coefficients':[str(c) for c in norm.all_coeffs()],
                    'numerator_coefficients':[str(c) for c in n.all_coeffs()],
                    'imaginary_sign':im,'derivative_sign':dn})
    return out

def segment_polys(start,end):
    ps=[]
    for a,b in zip(start,end):ps.append((poly(a[0]+t*(b[0]-a[0])),poly(a[1]+t*(b[1]-a[1]))))
    return ps
def projected_difference(ps,i,j):
    ai,bi=ps[i][0]-ps[4][0],ps[i][1]-ps[4][1]
    aj,bj=ps[j][0]-ps[4][0],ps[j][1]-ps[4][1]
    dr,di=ai*aj-bi*bj,ai*bj+bi*aj
    vr,vi=ps[j][0]-ps[i][0],ps[j][1]-ps[i][1]
    wr,ww=vr-vi*q(1,10),vi+vr*q(1,10)
    return wr*dr+ww*di,ww*dr-wr*di

def track(face,word):
    vertices=target(face,word);order=[3,2,1,0];answer=[];events=[]
    for segment,(start,end) in enumerate(zip(vertices,vertices[1:])):
        ps=segment_polys(start,end);cross=[]
        for i,j in itertools.combinations(range(4),2):
            n,m=projected_difference(ps,i,j)
            # Endpoint projections must be distinct, and their order is checked.
            for endpoint in (0,1):assert stable_sign(n,(q(endpoint),q(endpoint))) is not None
            for r in crossing_roots(n,m):cross.append({**r,'pair':[i,j]})
        cross.sort(key=lambda e:e['lo'])
        assert all(x['hi']<y['lo'] for x,y in zip(cross,cross[1:])),cross
        for ev in cross:
            i,j=ev['pair'];a,b=order.index(i),order.index(j)
            assert abs(a-b)==1,(face,word,segment,ev,order)
            gen=min(a,b)+1;letter=(4-gen)*ev['sign'];answer.append(letter)
            order[a],order[b]=order[b],order[a]
            events.append({'segment':segment,'interval':[str(ev['lo']),str(ev['hi'])],
                           'pair':ev['pair'],'letter':letter,
                           'norm_coefficients':ev['norm_coefficients'],
                           'numerator_coefficients':ev['numerator_coefficients'],
                           'imaginary_sign':ev['imaginary_sign'],'derivative_sign':ev['derivative_sign']})
        for i,j in itertools.combinations(range(4),2):
            n,m=projected_difference(ps,i,j)
            sign=stable_sign(n,(q(1),q(1)))
            assert sign==(1 if order.index(i)>order.index(j) else -1),(face,word,segment,order,i,j)
    return {'word':list(red(answer)),'crossings':events,'segments':len(vertices)-1}

def main():
    started=time.monotonic();out={};old=json.loads((ROOT/'work/agents/characters/records/orbit_coface_braids_discovery.json').read_text())
    for face in range(5):
        words=['x','y'] if face==0 else (['u','Y0'] if face==4 else ['U','Y0','Y1','Y2'])
        for w in words:
            result=track(face,w)
            result['equals_discovery_in_B4']=braid(tuple(result['word']))==braid(tuple(old[str(face)][w]['braid_word']))
            assert result['equals_discovery_in_B4'],(face,w,result['word'],old[str(face)][w]['braid_word'])
            out[f'{face}:{w}']=result
            print(face,w,result['word'],'PASS',flush=True)
            (ROOT/'work/records/orbital_paths_exact.json').write_text(json.dumps({'scope':'Exact algebraic-polygonal crossing audit; geometry marking stated in companion note.','completed':out,'elapsed_seconds':time.monotonic()-started},indent=2)+'\n')
    print('PASS all16 coface-generator paths with exact rational crossing isolation',flush=True)

if __name__=='__main__':main()

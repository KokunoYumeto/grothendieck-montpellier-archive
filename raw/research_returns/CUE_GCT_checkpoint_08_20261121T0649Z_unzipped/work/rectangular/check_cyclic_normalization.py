"""Finite coefficient checks and exploratory normalized Fourier degrees."""
import json
import sys
from pathlib import Path
import numpy as np

def read_poly(stem, tag, degree):
    return np.fromfile(str(stem)+'_'+tag+'.u16', dtype='<u2').reshape(degree+1, degree+1)

def value(poly, degree, point, prime):
    x,y,z=point
    return sum(int(poly[a,c])*pow(x,a,prime)*pow(y,degree-a-c,prime)*pow(z,c,prime)
               for a in range(degree+1) for c in range(degree-a+1)) % prime

def interpolated_degree(xs, ys, p):
    # Newton divided differences, then convert to the monomial basis.
    ds=[int(y)%p for y in ys]
    for j in range(1,len(xs)):
        for i in range(len(xs)-1,j-1,-1):
            ds[i]=(ds[i]-ds[i-1])*pow((xs[i]-xs[i-j])%p,-1,p)%p
    result=[0]*len(xs);basis=[1]
    for i,c in enumerate(ds):
        for j,b in enumerate(basis):result[j]=(result[j]+c*b)%p
        if i+1<len(xs):
            new=[0]*(len(basis)+1)
            for j,b in enumerate(basis):
                new[j]=(new[j]-xs[i]*b)%p;new[j+1]=(new[j+1]+b)%p
            basis=new
    return max([i for i,c in enumerate(result) if c]+[-1]), result

def main():
    n=int(sys.argv[1]);directory=Path(sys.argv[2]);stem=directory/f'cyclic_coefficients_m{n}'
    data=json.loads(stem.with_suffix('.json').read_text());p,q=data['prime'],data['q'];D=n+1
    polys={tag:read_poly(stem,tag,n if tag in ['a','b'] else D) for tag in ['a','b','t','tp']}
    out={'m':n,'prime':p,'q':q}
    manifest=directory/f'border_balanced2_cycle_m{n}.json'
    if manifest.exists():
        old=json.loads(manifest.read_text());J=np.fromfile(manifest.with_suffix('.u16'),dtype='<u2').reshape(old['rows'],old['columns']);checked=0
        for r,pt in enumerate(old['points']):
            a=value(polys['a'],n,pt,p);b=value(polys['b'],n,pt,p)
            for k in range(3):
                assert a*pt[k]%p==J[r,3+k]
                assert b*pt[k]%p==J[r,3+3*n+k]
                checked+=2
            assert value(polys['t'],D,pt,p)==J[r,6*n+3]
            assert value(polys['tp'],D,pt,p)==J[r,7*n+3]
            checked+=2
        out['independent_arc_entries_checked']=checked
    factorial=[1]
    for i in range(1,n):factorial.append(factorial[-1]*(1-pow(q,i,p))%p)
    groups=[]
    for r in range(n):
        for wrap in [0,1]:
            pts=[]
            for a in range(4,n):
                c=a+r-1-wrap*n;b=D-a-c
                if c<0 or c>=n or b<2:continue
                omega=n*factorial[a+c-2]*pow(factorial[a]**2*factorial[c]**2*(1-pow(q,c+1,p))%p,-1,p)%p
                pts.append((a,c,pow(q,a,p),omega))
            if len(pts)<7:continue
            ds={}
            for tag in ['t','tp']:
                xs=[x for a,c,x,o in pts];ys=[int(polys[tag][a,c])*pow(o,-1,p)%p for a,c,x,o in pts]
                degree,coefficients=interpolated_degree(xs,ys,p)
                ds[tag]={'degree':degree,'coefficients':coefficients}
            groups.append({'character':r,'wrap':wrap,'points':len(pts),'degrees':ds})
    out['normalized_hessian_groups']=groups
    path=Path(str(stem)+'_normalization.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k!='normalized_hessian_groups'})
    print('degree profiles:',sorted(set((g['degrees']['t']['degree'],g['degrees']['tp']['degree']) for g in groups)))
    print('groups:',len(groups))

if __name__=='__main__':main()

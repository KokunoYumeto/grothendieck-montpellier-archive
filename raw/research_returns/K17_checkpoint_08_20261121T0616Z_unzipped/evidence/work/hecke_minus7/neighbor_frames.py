"""Exact p=2 rational frames for Loeffler's two-class unitary model."""
from itertools import product, combinations
from pathlib import Path
import json


def mul(x,y):
    a,b=x;c,d=y
    return (a*c-2*b*d, a*d+b*c+b*d)


def conj(x):
    a,b=x
    return (a+b,-b)


def add(x,y):
    return (x[0]+y[0],x[1]+y[1])


def norm(x):
    a,b=x
    return a*a+a*b+2*b*b


def inner(v,w):
    z=(0,0)
    for x,y in zip(v,w):z=add(z,mul(conj(x),y))
    return z


def determinant(columns):
    a,b,c=columns
    out=(0,0)
    for i,j,k,sign in [(0,1,2,1),(1,2,0,1),(2,0,1,1),
                       (2,1,0,-1),(1,0,2,-1),(0,2,1,-1)]:
        x=mul(a[i],mul(b[j],c[k]))
        out=add(out,(sign*x[0],sign*x[1]))
    return out


def frames(r):
    scalars=[(a,b) for a,b in product(range(-4,5),repeat=2) if norm((a,b))<=r]
    vectors=[]
    for v in product(scalars,repeat=3):
        if sum(norm(x) for x in v)!=r:continue
        flat=[t for x in v for t in x]
        if next(t for t in flat if t)>0:vectors.append(v)
    vectors.sort()
    orth={i:{j for j in range(i+1,len(vectors)) if inner(vectors[i],vectors[j])==(0,0)}
          for i in range(len(vectors))}
    fs=[]
    for i in range(len(vectors)):
        for j in sorted(orth[i]):
            for k in sorted(orth[i]&orth[j]):
                columns=[vectors[i],vectors[j],vectors[k]]
                fs.append(columns)
    return vectors,fs


def main():
    out={}
    for r in (2,4):
        vectors,allframes=frames(r)
        chosen=[]
        for cols in allframes:
            d=determinant(cols)
            # The omega-adic root is 2 mod4 and 6 mod8.
            if r==2:
                ok=(d[0]+2*d[1])%4==2
            else:
                ok=(d[0]+6*d[1])%8==4 and all(
                    sum(x[0] for x in col)%2==0 for col in cols)
            if ok:chosen.append(cols)
        expected=6 if r==2 else 7
        assert len(chosen)==expected,(r,len(vectors),len(allframes),len(chosen))
        for cols in chosen:
            assert all(inner(cols[i],cols[j])==((r,0) if i==j else (0,0))
                       for i in range(3) for j in range(3))
        out[str(r)]={'norm':r,'vectors_up_to_sign':len(vectors),
                     'all_orthogonal_frames':len(allframes),
                     'selected_frames':chosen,'selected_count':len(chosen)}
    p=Path(__file__).with_suffix('.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print({r:{k:v for k,v in row.items() if k!='selected_frames'} for r,row in out.items()})


if __name__=='__main__':main()

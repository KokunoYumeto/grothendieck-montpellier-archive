#!/usr/bin/env python3
"""Independent stdlib verifier for general bounded-Hessian jet windows.

The selected mixed derivatives are rebuilt from first adjugate derivatives;
all integral lowering words and all selected entries are checked, followed
by ordinary scalar elimination. No NumPy is imported.
"""
from collections import defaultdict,Counter
from math import comb,factorial
from pathlib import Path
from time import monotonic
import argparse,hashlib,json,zipfile
import check_quadratic_relative_jets as helper

P=101;core=helper.core

def types(low,high,bound):
    return [(j,k,r) for j in range(low+1,high+1) for k in range(j,high+1)
            for r in range(max(0,j+k-bound),j+1) if j!=k or r%2==0]

def offsets(low,high):
    result={};cursor=0
    for degree in range(low+1,high+1):result[degree]=cursor;cursor+=len(core.COORD[degree])
    return result

def normalized_high(n,low,high,jac,vectors):
    count=comb(low+3,3)-1
    jcolumns=[core.pack_lanes(row[j] for row in jac) for j in range(3*n*n)]
    raw=[list(core.linear_combination(v,jcolumns,len(jac))[count:]) for v in vectors]
    offset=offsets(low,high);inverse=pow(factorial(n)%P,-1,P)
    for degree,start in offset.items():
        for i,alpha in enumerate(core.COORD[degree]):
            scale=factorial(n-degree)*inverse
            for a in alpha:scale*=factorial(a)
            for row in raw:row[start+i]=row[start+i]*scale%P
    a,b=core.pencil(n,P,20261122)
    ell=[sum(range(1,n+1)),sum(a[i*n+i] for i in range(n)),sum(b[i*n+i] for i in range(n))]
    ell=[x*pow(n,-1,P)%P for x in ell]
    centered=[[0]*len(raw[0]) for _ in raw]
    for degree,start in offset.items():
        for i,alpha in enumerate(core.COORD[degree]):
            for smaller in range(low+1,degree+1):
                gap=degree-smaller
                for gamma in core.COORD[gap]:
                    if any(g>a for g,a in zip(gamma,alpha)):continue
                    beta=tuple(a-g for a,g in zip(alpha,gamma));coefficient=(-1)**gap
                    for a,g,l in zip(alpha,gamma,ell):coefficient*=comb(a,g)*pow(l,g,P)
                    source=offset[smaller]+core.INDEX[smaller][beta]
                    for row,original in zip(centered,raw):row[start+i]=(row[start+i]+coefficient*original[source])%P
    return centered

def reconstruct(record,low,high):
    j,k,r=record['type'];offset=offsets(low,high)
    labels={i+offset[d]:alpha for d in offset for i,alpha in enumerate(core.COORD[d])}
    def key(a,b):
        x=core.INDEX[j][tuple(a)]+offset[j];y=core.INDEX[k][tuple(b)]+offset[k]
        return tuple(sorted((x,y))) if j==k else (x,y)
    polynomial=defaultdict(int)
    for t in range(r+1):polynomial[key((j-t,t,0),(k-r+t,r-t,0))]+=(-1)**t*comb(r,t)
    polynomial={z:x%P for z,x in polynomial.items() if x%P}
    for root in record['word']:
        assert root in (0,1);out=defaultdict(int)
        for (i,h),coefficient in polynomial.items():
            a,b=list(labels[i]),list(labels[h])
            for side in (0,1):
                alpha=a if side==0 else b;c=alpha[root]
                if c:
                    beta=list(alpha);beta[root]-=1;beta[root+1]+=1
                    out[key(beta,b) if side==0 else key(a,beta)]+=c*coefficient
        polynomial={z:x%P for z,x in out.items() if x%P}
    assert [[*z,x] for z,x in sorted(polynomial.items())]==record['terms']
    return polynomial

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('directory',type=Path);ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    directory=args.directory;start=monotonic();out=directory/'stdlib_check.json'
    cfg=json.loads((directory/'config.json').read_text());n,low,bound,high=[cfg[k] for k in ('n','low','bound','high')]
    assert 0<low<high==min(n,bound) and n<P
    lower=comb(low+3,3)-1;fullrank=2*n*n+1;relative=fullrank-lower
    assert cfg['lower_count']==lower and cfg['full_rank']==fullrank and cfg['relative']==relative
    helper.N=n;helper.R=relative;helper.LOW=lower;helper.S=high
    core.N=n;core.S=high;core.WIDTH=3*n*n;core.SHIFT=core.BITS*(n-1)
    core.COORD=[core.labels(j) for j in range(high+1)]
    core.INDEX=[{a:i for i,a in enumerate(level)} for level in core.COORD]
    assert n*(P-1)**2<1<<core.BITS
    sources=[Path(__file__),Path(helper.__file__),Path(core.__file__),Path(core.__file__).with_name('check_binary_jets.py')]
    sources += [directory/name for name in ('config.json','linear_data.npz','mixed_second_coefficients.npy','quadratic_basis.json','combined_matrix.npy','status.json')]
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    verified=[]
    if args.resume and out.exists():
        prior=json.loads(out.read_text())
        if prior.get('hashes')==hashes:verified=prior['mixed_groups_verified']
    result=dict(status='RUNNING',configuration=cfg,hashes=hashes,mixed_groups_verified=verified)
    with zipfile.ZipFile(directory/'linear_data.npz') as z:
        stored=core.read_matrix(z,'jacobian');normal=core.read_matrix(z,'normal');vectors=core.read_matrix(z,'directions')
    apacks,base,basepacks=core.source_and_base();jac=core.jacobian(base)
    assert jac==stored and len(jac)==comb(high+3,3)-1
    assert len(normal)==len(jac)-fullrank and len(vectors)==relative
    assert core.rank_packed(jac[:lower],P)[0]==lower and core.rank_packed(jac,P)[0]==fullrank
    jp=[core.pack_lanes(row) for row in jac]
    assert all(not any(core.linear_combination(w,jp,3*n*n)) for w in normal)
    jcols=[core.pack_lanes(row[j] for row in jac[:lower]) for j in range(3*n*n)]
    assert all(not any(core.linear_combination(v,jcols,lower)) for v in vectors)
    highvalues=normalized_high(n,low,high,jac,vectors);assert core.scalar_rank(highvalues,P)==relative
    status=json.loads((directory/'status.json').read_text());cols=status['pivot_columns']
    expected_counts={t:(t[0]+t[1]-2*t[2]+1)*(t[0]+t[1]-t[2]+2)*(t[2]+1)//2 for t in types(low,high,bound)}
    total=len(normal)+sum(expected_counts.values())
    assert status['full_row_rank'] and len(cols)==len(set(cols))==total
    pairs=[(i,j) for i in range(relative) for j in range(i,relative)]
    assert all(0<=c<len(pairs) for c in cols)
    selected=[pairs[c] for c in cols];groups=defaultdict(list)
    for column,(i,j) in zip(cols,selected):groups[i].append((j,column))
    mixed=helper.read_npy(directory/'mixed_second_coefficients.npy')
    expected=helper.read_npy(directory/'combined_matrix.npy')
    assert len(mixed)==len(jac) and len(expected)==total
    lanes=[[core.pack_lanes(v[k*n*n+i] for v in vectors) for i in range(n*n)] for k in range(3)]
    for i,targets in sorted(groups.items()):
        if i in verified:continue
        actual=helper.mixed_group(vectors[i],lanes,apacks,base,basepacks)
        assert all(actual[a][j]==mixed[a][column] for a in range(len(jac)) for j,column in targets)
        verified.append(i);result.update(mixed_groups_verified=verified,seconds=monotonic()-start)
        core.atomic_json(out,result);print(json.dumps(dict(stage='mixed',group=i,groups=len(verified),seconds=result['seconds'])),flush=True)
    packed_h=[core.pack_lanes(row[c] for c in cols) for row in mixed];rows=[]
    for i,w in enumerate(normal):
        row=core.linear_combination(w,packed_h,len(cols));assert row==bytes(expected[i][c] for c in cols);rows.append(row)
    records=json.loads((directory/'quadratic_basis.json').read_text())
    assert Counter(tuple(r['type']) for r in records)==expected_counts
    cache={}
    for number,record in enumerate(records):
        polynomial=reconstruct(record,low,high);keys=sorted(polynomial)
        for i,j in keys:
            if (i,j) not in cache:
                cache[i,j]=core.pack_lanes((highvalues[s][i]*highvalues[t][j]+highvalues[s][j]*highvalues[t][i])*pow(2,-1,P)%P for s,t in selected)
        row=core.linear_combination([polynomial[k] for k in keys],[cache[k] for k in keys],len(cols))
        assert row==bytes(expected[len(normal)+number][c] for c in cols);rows.append(row)
    result.update(quadratic_words_verified=len(records),mixed_columns_verified=len(cols),matrix_shape=[len(rows),len(cols)],seconds=monotonic()-start)
    core.atomic_json(out,result);print(json.dumps(dict(stage='scalar_rank',seconds=result['seconds'])),flush=True)
    minor=helper.scalar_minor(rows);assert minor==status['minor']
    result.update(status='PASS',rank=len(rows),minor=minor,seconds=monotonic()-start)
    core.atomic_json(out,result);print(json.dumps({k:v for k,v in result.items() if k not in ('hashes','mixed_groups_verified')}),flush=True)

if __name__=='__main__':main()

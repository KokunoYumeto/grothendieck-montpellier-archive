#!/usr/bin/env python3
"""Independent stdlib certificate for the bounded-Hessian determinant test.

Rebuild all linear data, the1330 selected mixed second-coefficient
columns, every integral lowering-word quadratic, and the complete selected
combined matrix. NumPy is not imported. --resume requires identical hashes.
"""
from array import array
from collections import Counter,defaultdict
from math import comb,factorial
from pathlib import Path
from time import monotonic
import argparse,ast,hashlib,json,zipfile
import check_relative_second_jets as core

P=101;N=23;R=91;LOW=968;S=18
DIRECTORY=Path('work/root/results/det23_quadratic_relative_jets')
core.S=S;core.COORD=[core.labels(j) for j in range(S+1)]
core.INDEX=[{a:i for i,a in enumerate(level)} for level in core.COORD]

def read_npy(path):
    data=path.read_bytes();assert data[:6]==b'\x93NUMPY'
    size=2 if data[6]==1 else 4
    length=int.from_bytes(data[8:8+size],'little');start=8+size+length
    meta=ast.literal_eval(data[8+size:start].decode('latin1').strip())
    assert meta['descr'] in ('|u1','<u1') and not meta['fortran_order']
    height,width=meta['shape'];body=data[start:]
    assert len(body)==height*width and all(x<P for x in body)
    return [body[i*width:(i+1)*width] for i in range(height)]

def mixed_group(vector,variation_lanes,apacks,base,basepacks):
    vpacks=[core.rows(vector[k*N*N:(k+1)*N*N]) for k in range(3)]
    previous=[[0]*(N*N)];answer=[]
    assert 3*N*N*(P-1)**2<2**32
    for degree in range(1,S+1):
        h=[0]*len(core.COORD[degree])
        accum=[[0]*(N*N) for _ in core.COORD[degree]] if degree<S else None
        eprime=[0]*len(core.COORD[degree])
        for index,(alpha,qprime) in enumerate(zip(core.COORD[degree-1],previous)):
            qcols=core.columns(qprime)
            qt=[qprime[j*N+i] for i in range(N) for j in range(N)]
            for k in range(3):
                beta=list(alpha);beta[k]+=1;dest=core.INDEX[degree][tuple(beta)]
                h[dest]+=sum(x*packed for x,packed in zip(qt,variation_lanes[k]) if x)
                if degree==S:continue
                left=([(i+1)*qprime[i*N+j]%P for i in range(N) for j in range(N)]
                      if k==0 else core.product(apacks[k],qcols))
                right=core.product(vpacks[k],basepacks[degree-1][index])
                accum[dest]=[x+y+z for x,y,z in zip(accum[dest],left,right)]
                eprime[dest]+=sum(right[i*N+i] for i in range(N))
        for packed in h:
            lanes=array('I');lanes.frombytes(packed.to_bytes(4*R,'little'))
            answer.append(bytes(x*pow(2,-1,P)%P for x in lanes))
        if degree<S:
            previous=[[(e*(i//N==i%N)-value)%P for i,value in enumerate(matrix)]
                      for e,matrix in zip(eprime,accum)]
    return answer

def normalized_high(jac,vectors):
    jcolumns=[core.pack_lanes(row[j] for row in jac) for j in range(3*N*N)]
    high=[list(core.linear_combination(v,jcolumns,len(jac))[LOW:]) for v in vectors]
    inv=pow(factorial(N)%P,-1,P);cursor=0
    for degree in (17,18):
        for alpha in core.COORD[degree]:
            scale=factorial(N-degree)*inv
            for a in alpha:scale*=factorial(a)
            for row in high:row[cursor]=row[cursor]*scale%P
            cursor+=1
    a,b=core.pencil(N,P,20261122)
    ell=[sum(range(1,N+1)),sum(a[i*N+i] for i in range(N)),sum(b[i*N+i] for i in range(N))]
    ell=[x*pow(N,-1,P)%P for x in ell]
    offset=len(core.COORD[17])
    for t,alpha in enumerate(core.COORD[18]):
        for k in range(3):
            if alpha[k]:
                beta=list(alpha);beta[k]-=1;source=core.INDEX[17][tuple(beta)]
                for row in high:row[offset+t]=(row[offset+t]-alpha[k]*ell[k]*row[source])%P
    return high

def reconstruct_quadratic(record):
    j,k,r=record['type'];offset={17:0,18:len(core.COORD[17])}
    labels={i+offset[d]:alpha for d in (17,18) for i,alpha in enumerate(core.COORD[d])}
    def key(a,b):
        x=core.INDEX[j][tuple(a)]+offset[j];y=core.INDEX[k][tuple(b)]+offset[k]
        return tuple(sorted((x,y))) if j==k else (x,y)
    polynomial=defaultdict(int)
    for t in range(r+1):
        polynomial[key((j-t,t,0),(k-r+t,r-t,0))]+=(-1)**t*comb(r,t)
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

def scalar_minor(rows):
    a=[list(row) for row in rows];det=1;n=len(a)
    assert all(len(row)==n for row in a)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        assert pivot is not None,('singular selected minor',j)
        if pivot!=j:a[j],a[pivot]=a[pivot],a[j];det=-det%P
        value=a[j][j];det=det*value%P;inverse=pow(value,-1,P)
        a[j][j:]=[x*inverse%P for x in a[j][j:]]
        tail=a[j][j+1:]
        for i in range(j+1,n):
            c=a[i][j]
            if c:a[i][j+1:]=[(x-c*y)%P for x,y in zip(a[i][j+1:],tail)];a[i][j]=0
    return det

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    start=monotonic();out=DIRECTORY/'stdlib_check.json'
    sources=[Path(__file__),Path(core.__file__),Path(core.__file__).with_name('check_binary_jets.py')]
    sources += [DIRECTORY/name for name in ('linear_data.npz','mixed_second_coefficients.npy','quadratic_basis.json','combined_matrix.npy','status.json')]
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    verified=[]
    if args.resume and out.exists():
        prior=json.loads(out.read_text())
        if prior.get('hashes')==hashes:verified=prior['mixed_groups_verified']
    result=dict(status='RUNNING',hashes=hashes,mixed_groups_verified=verified)
    with zipfile.ZipFile(DIRECTORY/'linear_data.npz') as z:
        stored=core.read_matrix(z,'jacobian');normal=core.read_matrix(z,'normal');vectors=core.read_matrix(z,'directions')
    apacks,base,basepacks=core.source_and_base();jac=core.jacobian(base)
    assert jac==stored and (len(jac),len(normal),len(vectors))==(1329,270,91)
    assert core.rank_packed(jac[:LOW],P)[0]==968 and core.rank_packed(jac,P)[0]==1059
    jp=[core.pack_lanes(row) for row in jac]
    assert all(not any(core.linear_combination(w,jp,3*N*N)) for w in normal)
    jcols=[core.pack_lanes(row[j] for row in jac[:LOW]) for j in range(3*N*N)]
    assert all(not any(core.linear_combination(v,jcols,LOW)) for v in vectors)
    high=normalized_high(jac,vectors);assert core.scalar_rank(high,P)==91
    status=json.loads((DIRECTORY/'status.json').read_text());cols=status['pivot_columns'];assert len(cols)==1330 and len(set(cols))==1330
    pairs=[(i,j) for i in range(R) for j in range(i,R)]
    selected=[pairs[c] for c in cols];groups=defaultdict(list)
    for column,(i,j) in zip(cols,selected):groups[i].append((j,column))
    mixed=read_npy(DIRECTORY/'mixed_second_coefficients.npy')
    expected=read_npy(DIRECTORY/'combined_matrix.npy')
    lanes=[[core.pack_lanes(v[k*N*N+i] for v in vectors) for i in range(N*N)] for k in range(3)]
    for i,targets in sorted(groups.items()):
        if i in verified:continue
        actual=mixed_group(vectors[i],lanes,apacks,base,basepacks)
        assert all(actual[a][j]==mixed[a][column] for a in range(len(jac)) for j,column in targets)
        verified.append(i);result.update(mixed_groups_verified=verified,seconds=monotonic()-start)
        core.atomic_json(out,result);print(json.dumps(dict(stage='mixed',group=i,groups=len(verified),seconds=result['seconds'])),flush=True)
    selected_h=[bytes(row[c] for c in cols) for row in mixed]
    packed_h=[core.pack_lanes(row) for row in selected_h];rows=[]
    for i,w in enumerate(normal):
        row=core.linear_combination(w,packed_h,len(cols));assert row==bytes(expected[i][c] for c in cols);rows.append(row)
    records=json.loads((DIRECTORY/'quadratic_basis.json').read_text())
    assert Counter(tuple(r['type']) for r in records)=={(17,17,16):510,(17,18,17):360,(18,18,18):190}
    cache={}
    for number,record in enumerate(records):
        polynomial=reconstruct_quadratic(record);keys=sorted(polynomial)
        for i,j in keys:
            if (i,j) not in cache:
                cache[i,j]=core.pack_lanes((high[s][i]*high[t][j]+high[s][j]*high[t][i])*pow(2,-1,P)%P for s,t in selected)
        row=core.linear_combination([polynomial[k] for k in keys],[cache[k] for k in keys],len(cols))
        assert row==bytes(expected[270+number][c] for c in cols);rows.append(row)
    result.update(quadratic_words_verified=len(records),mixed_columns_verified=len(cols),matrix_shape=[len(rows),len(cols)],seconds=monotonic()-start)
    core.atomic_json(out,result);print(json.dumps(dict(stage='scalar_rank',seconds=result['seconds'])),flush=True)
    minor=scalar_minor(rows);assert minor==12
    result.update(status='PASS',rank=1330,minor=minor,seconds=monotonic()-start)
    core.atomic_json(out,result);print(json.dumps({k:v for k,v in result.items() if k!='hashes'}),flush=True)

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Independent stdlib verification of the determinant relative second-jet test.

The input is an exploratory NumPy archive; this checker does not import NumPy.
It rebuilds the Jacobian from integral matrix coefficients, checks both
kernel systems, independently recomputes every second derivative using
2[t^2]det(M+tV)=tr(V [t]adj(M+tV)), and checks the final normal minor.
The default is a fresh complete check. --resume reuses only an identical
source/input-hashed prefix from an interrupted execution.
"""
from array import array
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
from time import monotonic
import zipfile
from check_binary_jets import pencil,rank_packed,scalar_rank

P=101;N=23;S=17;WIDTH=3*N*N
BITS=18;MASK=(1<<BITS)-1;SHIFT=BITS*(N-1)
assert N*(P-1)**2 < 1<<BITS

def read_matrix(archive,name):
    data=archive.read(name+'.npy')
    assert data[:6]==b'\x93NUMPY' and data[6:8] in (b'\x01\x00',b'\x02\x00')
    size=2 if data[6]==1 else 4
    length=int.from_bytes(data[8:8+size],'little');start=8+size+length
    meta=ast.literal_eval(data[8+size:start].decode('latin1').strip())
    assert meta['descr'] in ('|u1','<u1') and not meta['fortran_order']
    shape=meta['shape'];assert len(shape)==2
    body=data[start:];assert len(body)==shape[0]*shape[1]
    assert all(x<P for x in body)
    return [body[i*shape[1]:(i+1)*shape[1]] for i in range(shape[0])]

def labels(j):return [(j-y-z,y,z) for y in range(j+1) for z in range(j-y+1)]
COORD=[labels(j) for j in range(S+1)]
INDEX=[{a:i for i,a in enumerate(level)} for level in COORD]
LOW=sum(map(len,COORD[1:S]))

def rows(matrix):
    return [sum(matrix[i*N+k]<<(BITS*k) for k in range(N)) for i in range(N)]

def columns(matrix):
    return [sum(matrix[k*N+j]<<(BITS*(N-1-k)) for k in range(N)) for j in range(N)]

def product(arows,bcols):
    # Every convolution coefficient is below2^18, so the middle digit is
    # exactly one matrix dot product, with no carry from an adjacent digit.
    return [((a*b>>SHIFT)&MASK)%P for a in arows for b in bcols]

def trace_product(arows,bcols):
    return sum(((a*b>>SHIFT)&MASK) for a,b in zip(arows,bcols))%P

def source_and_base():
    a,b=pencil(N,P,20261122)
    mats=[[int(i==j)*(i+1) for i in range(N) for j in range(N)],a,b]
    packs=[rows(m) for m in mats]
    identity=[int(i==j) for i in range(N) for j in range(N)]
    base=[[identity]];packed=[[columns(identity)]]
    for degree in range(1,S):
        accum=[[0]*(N*N) for _ in COORD[degree]]
        for alpha,matrix,bcols in zip(COORD[degree-1],base[-1],packed[-1]):
            for k in range(3):
                beta=list(alpha);beta[k]+=1;dest=INDEX[degree][tuple(beta)]
                value=([(i+1)*matrix[i*N+j]%P for i in range(N) for j in range(N)]
                       if k==0 else product(packs[k],bcols))
                accum[dest]=[x+y for x,y in zip(accum[dest],value)]
        inverse=pow(degree,-1,P);level=[]
        for value in accum:
            e=sum(value[i*N+i] for i in range(N))*inverse%P
            level.append([(e*identity[i]-value[i])%P for i in range(N*N)])
        base.append(level);packed.append([columns(m) for m in level])
    return packs,base,packed

def jacobian(base):
    result=[];zero=[0]*(N*N)
    for degree in range(1,S+1):
        for alpha in COORD[degree]:
            row=[]
            for k in range(3):
                beta=list(alpha);beta[k]-=1
                matrix=zero if beta[k]<0 else base[degree-1][INDEX[degree-1][tuple(beta)]]
                row.extend(matrix[j*N+i] for i in range(N) for j in range(N))
            result.append(bytes(row))
    return result

def pack_lanes(values):
    assert sys.byteorder=='little' and array('I').itemsize==4
    return int.from_bytes(array('I',(int(x) for x in values)).tobytes(),'little')

def linear_combination(coefficients,packed,width):
    assert len(coefficients)*(P-1)**2 < 2**32
    value=sum(c*x for c,x in zip(coefficients,packed) if c)
    result=array('I');result.frombytes(value.to_bytes(4*width,'little'))
    return bytes(x%P for x in result)

def second_jet(vector,apacks,base,basepacks):
    vpacks=[rows(vector[k*N*N:(k+1)*N*N]) for k in range(3)]
    previous=[[0]*(N*N)];output=[]
    for degree in range(1,S+1):
        h=[0]*len(COORD[degree])
        accum=[[0]*(N*N) for _ in COORD[degree]] if degree<S else None
        eprime=[0]*len(COORD[degree])
        for index,(alpha,qprime) in enumerate(zip(COORD[degree-1],previous)):
            qprimecols=columns(qprime)
            for k in range(3):
                beta=list(alpha);beta[k]+=1;dest=INDEX[degree][tuple(beta)]
                h[dest]+=trace_product(vpacks[k],qprimecols)
                if degree==S:continue
                left=([(i+1)*qprime[i*N+j]%P for i in range(N) for j in range(N)]
                      if k==0 else product(apacks[k],qprimecols))
                right=product(vpacks[k],basepacks[degree-1][index])
                accum[dest]=[x+y+z for x,y,z in zip(accum[dest],left,right)]
                eprime[dest]+=sum(right[i*N+i] for i in range(N))
        output.extend(x*pow(2,-1,P)%P for x in h)
        if degree<S:
            previous=[[(e*(i//N==i%N)-value)%P for i,value in enumerate(matrix)]
                      for e,matrix in zip(eprime,accum)]
    return bytes(output)

def atomic_json(path,data):
    temporary=path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(data,indent=2)+'\n');temporary.replace(path)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--directory',type=Path,default=Path('work/root/results/det23_relative_second_jets'))
    ap.add_argument('--resume',action='store_true')
    ap.add_argument('--limit',type=int)
    args=ap.parse_args();start=monotonic();out=args.directory/'stdlib_check.json'
    sources=[Path(__file__),Path(__file__).with_name('check_binary_jets.py'),
             args.directory/'linear_data.npz',args.directory/'direction_data.npz']
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    with zipfile.ZipFile(sources[-2]) as z:
        stored_j=read_matrix(z,'jacobian');normal=read_matrix(z,'normal')
    with zipfile.ZipFile(sources[-1]) as z:
        vectors=read_matrix(z,'directions');expected_h=read_matrix(z,'second_jets')
        expected_z=read_matrix(z,'normal_columns')
    assert (LOW,len(stored_j),len(stored_j[0]),len(normal),len(vectors))==(968,1139,1587,80,80)
    apacks,base,basepacks=source_and_base();actual_j=jacobian(base)
    assert actual_j==stored_j
    lowrank,lowcols,lowminor=rank_packed(actual_j[:LOW],P)
    fullrank,fullcols,_=rank_packed(actual_j,P)
    assert lowrank==968 and fullrank==1059
    print(json.dumps(dict(stage='jacobian',lower_rank=lowrank,full_rank=fullrank,seconds=monotonic()-start)),flush=True)
    jrows=[pack_lanes(row) for row in actual_j]
    assert all(not any(linear_combination(row,jrows,WIDTH)) for row in normal)
    jcolumns=[pack_lanes(row[j] for row in actual_j[:LOW]) for j in range(WIDTH)]
    assert all(not any(linear_combination(v,jcolumns,LOW)) for v in vectors)
    normalcolumns=[pack_lanes(row[j] for row in normal) for j in range(len(actual_j))]
    verified=0
    if args.resume and out.exists():
        previous=json.loads(out.read_text())
        if previous.get('hashes')==hashes:verified=previous['directions_recomputed']
    result=dict(status='RUNNING',hashes=hashes,lower_rank=lowrank,full_rank=fullrank,
                lower_minor=lowminor,lower_columns=lowcols,full_columns=fullcols,
                normal_kernel_checked=True,lower_kernel_checked=True,
                directions_recomputed=verified,source_arithmetic='stdlib integer digit products',
                second_derivative_method='trace of first adjugate derivative; independent of exploratory full second recurrence')
    stop=min(len(vectors),args.limit) if args.limit is not None else len(vectors)
    for index in range(verified,stop):
        computed=second_jet(vectors[index],apacks,base,basepacks)
        assert computed==expected_h[index],('second jet',index)
        assert linear_combination(computed,normalcolumns,len(normal))==expected_z[index]
        result.update(directions_recomputed=index+1,seconds=monotonic()-start)
        atomic_json(out,result)
        print(json.dumps(dict(direction=index+1,total=len(vectors),seconds=result['seconds'])),flush=True)
    rank,cols,minor=rank_packed(expected_z,P)
    assert rank==80 and minor
    assert scalar_rank(expected_z,P)==80
    result.update(normal_minor=minor,normal_rank=rank,seconds=monotonic()-start,
                  final_scalar_rank_checked=True,
                  status='PASS' if result['directions_recomputed']==len(vectors) else 'PARTIAL')
    atomic_json(out,result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('lower_columns','full_columns','hashes')}),flush=True)

if __name__=='__main__':main()

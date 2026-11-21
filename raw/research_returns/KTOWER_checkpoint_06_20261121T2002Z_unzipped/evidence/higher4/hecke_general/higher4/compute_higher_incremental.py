"""Exact producer with native rational RREF and incremental modular point selection.

This implements the same canonical parity-separated rational nullspace as
the carried producer. All contractions, ranks, parity identities and exact
polynomial computations are retained. Outputs are discovery data and must
still pass the separate standard-library full replay before arithmetic use.
The original producer and its running jobs are not changed.
"""
from pathlib import Path
from itertools import permutations
from collections import defaultdict
from math import gcd,lcm
import argparse,hashlib,importlib.util,json,random,sys,time
from flint import fmpq_mat,fmpz_mat
import flint
import sympy as sp

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'compute_harmonic_hecke.py'
spec=importlib.util.spec_from_file_location('u3_flint_discovery',SOURCE)
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
model.BASE=HERE/'fast_incremental';model.BASE.mkdir(exist_ok=True)
model.NEIGHBORS=HERE.parent.parent/'hecke_level_one/u3_weight5_exact_exploration.json'


def harmonic_data(k):
    start=time.monotonic()
    source,target=model.orbits(k),model.orbits(k-1)
    si={o:i for i,o in enumerate(source)};ti={o:i for i,o in enumerate(target)}
    expanded=[sorted(set(permutations(o))) for o in source]
    sizes=[len(set(permutations(o))) for o in target]
    lap=[[0]*len(source) for _ in target]
    for j,mons in enumerate(expanded):
        sums=defaultdict(int)
        for mon in mons:
            for i,(a,b) in enumerate(mon):
                if a and b:
                    out=list(mon);out[i]=(a-1,b-1)
                    sums[tuple(sorted(out))]+=a*b
        for out,c in sums.items():
            i=ti[out];assert c%sizes[i]==0;lap[i][j]=c//sizes[i]
    swap=[si[tuple(sorted((b,a) for a,b in o))] for o in source]
    tswap=[ti[tuple(sorted((b,a) for a,b in o))] for o in target]
    assert all(lap[tswap[i]][swap[j]]==lap[i][j]
               for i in range(len(target)) for j in range(len(source)))
    spans={1:[],-1:[]}
    for i,j in enumerate(swap):
        if i==j:spans[1].append([(i,1)])
        elif i<j:
            for sign in (1,-1):spans[sign].append([(i,1),(j,sign)])
    basis=[];signs=[];ranks=[]
    for sign in (1,-1):
        cols=spans[sign]
        if not cols:continue
        a=fmpq_mat([[sum(row[i]*s for i,s in col) for col in cols] for row in lap])
        rr,rank=a.rref();ranks.append(rank)
        pivots=[next(j for j in range(len(cols)) if rr[i,j]) for i in range(rank)]
        assert len(set(pivots))==rank
        free=[j for j in range(len(cols)) if j not in set(pivots)]
        for j in free:
            vals={j:flint.fmpq(1)}
            vals.update({pivot:-rr[i,j] for i,pivot in enumerate(pivots) if rr[i,j]})
            den=lcm(*(int(x.denominator) for x in vals.values()))
            out=[0]*len(source)
            for n,v in vals.items():
                z=int(v*den)
                for i,s in cols[n]:out[i]+=s*z
            common=gcd(*out);out=[v//common for v in out]
            if next(v for v in out if v)<0:out=[-v for v in out]
            basis.append(out);signs.append(sign)
        print('native parity kernel',k,sign,'rank',rank,'nullity',len(free),
              'seconds',round(time.monotonic()-start,2),flush=True)
    assert sum(ranks)==len(target)
    hrows=[list(row) for row in zip(*basis)]
    lf,hf=fmpz_mat(lap),fmpz_mat(hrows)
    assert lf*hf==fmpz_mat(len(target),len(basis))
    assert hf.rank()==len(basis)==len(source)-len(target)
    assert all(hrows[swap[i]][j]==signs[j]*hrows[i][j]
               for i in range(len(source)) for j in range(len(basis)))
    print('native complete harmonic basis',k,len(source),len(target),len(basis),
          'seconds',round(time.monotonic()-start,2),flush=True)
    return source,target,expanded,sp.Matrix(lap),sp.Matrix(hrows),signs


def rank_mod(rows,p=1000003):
    a=[[int(x)%p for x in row] for row in rows];r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        v=pow(a[r][j],-1,p);a[r]=[v*x%p for x in a[r]]
        for i in range(r+1,len(a)):
            v=a[i][j]
            if v:a[i]=[(x-v*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def choose_points(k,expanded,H):
    rng=random.Random(20261121+k);points=[];rows=[];p=1000003
    columns=[[(i,int(H[i,j])) for i in range(H.rows) if H[i,j]] for j in range(H.cols)]
    echelon=[]
    for attempt in range(1000):
        z=tuple(rng.randrange(-2,4) for _ in range(3))
        w=tuple(rng.randrange(-2,4) for _ in range(3))
        values=model.eval_orbits_integer(expanded,k,z,w)
        row=[sum(values[i]*c for i,c in column) for column in columns]
        reduced=[x%p for x in row]
        for pivot,basisrow in echelon:
            c=reduced[pivot]
            if c:
                for j in range(pivot,len(reduced)):
                    reduced[j]=(reduced[j]-c*basisrow[j])%p
        pivot=next((j for j,x in enumerate(reduced) if x),None)
        if pivot is not None:
            inv=pow(reduced[pivot],-1,p)
            reduced=[x*inv%p for x in reduced]
            assert all(reduced[j]==0 for j,_ in echelon)
            echelon.append((pivot,reduced));echelon.sort(key=lambda t:t[0])
            rows.append(row);points.append((z,w))
            if len(points)%25==0:print('identifying points',k,len(points),'of',H.cols,flush=True)
        if len(points)==H.cols:
            assert len(echelon)==H.cols
            assert [j for j,_ in echelon]==list(range(H.cols))
            matrix=sp.Matrix(rows)
            assert fmpz_mat(rows).det()!=0
            print('complete identifying points',k,len(points),'attempts',attempt+1,flush=True)
            return points,matrix
    raise RuntimeError('No full evaluation matrix found modulo screening prime')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('k',type=int)
    parser.add_argument('--basis-only',action='store_true');parser.add_argument('--points-only',action='store_true');args=parser.parse_args()
    model.harmonic_data=harmonic_data;model.choose_points=choose_points
    if args.basis_only or args.points_only:
        src,tgt,exp,lap,H,signs=harmonic_data(args.k)
        out={'k':args.k,'source_orbits':src,'target_orbits':tgt,
             'laplacian':model.matrix_json(lap),'harmonic_basis_columns':model.matrix_json(H),
             'swap_signs':signs}
        
        if args.points_only:
            points,ev=choose_points(args.k,exp,H)
            out['evaluation_points']=points;out['evaluation_matrix']=model.matrix_json(ev)
            out['evaluation_determinant']=str(fmpz_mat([[int(x) for x in row] for row in ev.tolist()]).det())
        path=model.BASE/f'basis_k{args.k}.json';path.write_text(json.dumps(out)+'\n')
        print('BASIS_OUTPUT',path,flush=True);return
    neighbors=json.loads(model.NEIGHBORS.read_text());start=time.monotonic()
    data=model.calculate(args.k,[r for r in neighbors['results'] if r['p'] in (7,13)])
    data['producer_implementation']={'native_backend':'python-flint '+flint.__version__,
      'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'original_model_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
      'scope':'discovery; separate exact full replay required'}
    (model.BASE/f'harmonic_k{args.k}_exact_exploration.json').write_text(json.dumps(data,indent=2)+'\n')
    print('FULL_TIMING',args.k,time.monotonic()-start,flush=True)


if __name__=='__main__':main()

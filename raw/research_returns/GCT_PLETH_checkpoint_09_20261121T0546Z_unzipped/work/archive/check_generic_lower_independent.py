"""Independent G035 lower phases from original normalized restriction traces."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb,lcm
from pathlib import Path
import hashlib,json,subprocess,time
from check_generic_upper_independent import simplex,reconstruct,SAFE_DEGREES
from check_variable_wall_independent import decode,encode,difference
from check_third_power_fixed_twist_independent import CLASSES,CHARS,SIZES,PARTITIONS
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root'

def physical(branch,Z):
    X,Y,K,C=Z
    if branch=='A':return X+Y,C+2*Y+15+3*K,C+Y+6+K,C
    return X,C+2*X+5*Y+20+3*K,C+X+2*Y+8+K,C

def main():
    start=time.monotonic();results={}
    source_receipt=json.loads((ROOT/'GENERIC_TWIST_LOWER_RECEIPT.json').read_text())
    binary=HERE/'generic_normalized_trace_oracle'
    bound=(1+100*100**3)*6*comb(403,3)**3
    assert bound<2**127
    for branch in ('A','B'):
        source=ROOT/f'GENERIC_TWIST_LOWER_{branch}_CHECK.json'
        expected=json.loads(source.read_text());descriptors=[];queries=[]
        for g,cycles in enumerate(CLASSES):
            L=lcm(*cycles);points=simplex(SAFE_DEGREES[g])
            for phase in product(range(L),repeat=4):
                descriptors.append((g,phase,L,points,len(queries)))
                for q in points:
                    Z=tuple(phase[i]+L*q[i] for i in range(4))
                    x,b,k,c=physical(branch,Z)
                    assert k<=100 and b+x+c+2<=400 and c<k and b+c>=2*k and 2*b+x+3*c>=5*k
                    queries.append((g,x,b,k,c))
        text=''.join(' '.join(map(str,q))+'\n' for q in queries)
        queryfile=HERE/f'GENERIC_LOWER_{branch}_QUERIES.txt';queryfile.write_text(text)
        run=subprocess.run([str(binary)],input=text,text=True,capture_output=True,check=True)
        answers=[int(v) for v in run.stdout.splitlines()];assert len(answers)==len(queries)
        data=[{} for _ in CLASSES]
        for g,phase,L,points,offset in descriptors:
            polynomial=reconstruct(phase,L,points,dict(zip(points,answers[offset:offset+len(points)])))
            key=','.join(map(str,phase))
            assert polynomial==decode(expected['phase_polynomials'][g][key]),(branch,g,phase)
            data[g][phase]=polynomial
        print(branch,'PASS2291 phase polynomials from',len(queries),'literal traces',flush=True)
        saved=[{','.join(map(str,k)):encode(p) for k,p in row.items()} for row in data]
        (HERE/f'GENERIC_LOWER_{branch}_POLYNOMIALS_INDEPENDENT.json').write_text(json.dumps(saved,indent=2)+'\n')
        identity=data[0][(0,0,0,0)]
        assert all(c>=0 for c in identity.values())
        support=set(p for row in data for poly in row.values() for p in poly)
        orders=set(o for p in support for o in product(*(range(v+1) for v in p)))
        orders.discard((0,0,0,0));orders=sorted(orders)
        assert [list(o) for o in orders]==expected['active_orders']
        unique=[{tuple(sorted(p.items())) for p in row.values()} for row in data]
        margins=[];table={tuple(r['order']):r for r in expected['margins']}
        for order in orders:
            ident=difference(identity,order);worst=defaultdict(Fraction)
            for size,row in zip(SIZES[1:],unique[1:]):
                boundpoly={}
                for poly in row:
                    for p,c in difference(dict(poly),order).items():
                        boundpoly[p]=max(boundpoly.get(p,Fraction(0)),abs(c))
                for p,c in boundpoly.items():worst[p]+=size*c
            margin={p:ident.get(p,Fraction(0))-worst.get(p,Fraction(0)) for p in set(ident)|set(worst)}
            assert all(c>=0 for c in margin.values()) and margin[(0,0,0,0)]>0
            assert {p:c for p,c in margin.items() if c}==decode(table[order]['margin'])
            assert margin[(0,0,0,0)]==Fraction(table[order]['constant'])
            assert min(margin.values())==Fraction(table[order]['minimum'])
            margins.append({'order':order,'constant':str(margin[(0,0,0,0)]),'margin':encode(margin)})
        assert len(margins)==(151 if branch=='A' else 108)
        minimum=min(Fraction(row['constant']) for row in margins)
        assert minimum==(131670 if branch=='A' else 8700)
        print(branch,'PASS',len(margins),'margins; minimum',minimum,flush=True)
        seeds=source_receipt['cones'][branch]['seeds']
        seedqueries=[(g,)+physical(branch,seed['coordinates']) for seed in seeds for g in range(7)]
        text=''.join(' '.join(map(str,q))+'\n' for q in seedqueries)
        run=subprocess.run([str(binary)],input=text,text=True,capture_output=True,check=True)
        values=[int(v) for v in run.stdout.splitlines()];seedrecords=[]
        for j,seed in enumerate(seeds):
            traces=values[7*j:7*j+7];mult=[]
            for chi in CHARS:
                num=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
                assert num%120==0;mult.append(num//120)
            assert mult==seed['effective_multiplicities']
            seedrecords.append({'coordinates':seed['coordinates'],'traces':traces,'effective_multiplicities':mult})
        results[branch]={'phase_polynomials':len(descriptors),'literal_unisolvent_traces':len(queries),
                         'margins':margins,'minimum_constant_margin':str(minimum),'seed_records':seedrecords,
                         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                         'query_sha256':hashlib.sha256(queryfile.read_bytes()).hexdigest()}
    out={'statement':'G035 generic lower-cone independent polynomial and margin reconstruction','status':'PASS',
         'method':'actual singleton and pair interlacing; original selected-triple Schur coefficients obtained by exact high-first-weight normal monomial counts, before any triple telescope; unisolvent reconstruction; literal step60 translations',
         'safe_phase_degrees':SAFE_DEGREES,'native_integer_absolute_bound':str(bound),
         'cones':results,'total_phases':4582,'total_unisolvent_traces':32332,'total_positive_margins':259,
         'full_residue_cube_executed':False,
         'oracle_source_sha256':hashlib.sha256((HERE/'generic_normalized_trace_oracle.cpp').read_bytes()).hexdigest(),
         'elapsed_seconds':time.monotonic()-start}
    (HERE/'GENERIC_LOWER_INDEPENDENT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS both lower cones and all56 finite seed coefficients',flush=True)

if __name__=='__main__':main()

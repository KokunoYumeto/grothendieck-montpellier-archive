"""T058 independent reconstruction through literal branching and normal Pieri.

No root/theta implementation is imported.  The oracle uses direct singleton
interlacing and two-slot normal Young multiplicities, with the skew determinant
itself on the complementary rank-two module, rather than the new pair identity.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product,combinations,permutations
from math import comb,lcm,prod
from pathlib import Path
import hashlib,json,subprocess,time
from check_variable_wall_independent import binomial_basis,decode,encode,difference
from check_third_power_fixed_twist_independent import CLASSES,CHARS,SIZES,PARTITIONS

HERE=Path(__file__).resolve().parent
THETA=HERE.parent/'theta'/'outer5'/'variable_wall'
SAFE_DEGREES=(6,4,4,3,0,3,0)

def simplex(d,r=4):
    if r==0:return [()]
    return [(i,)+tail for i in range(d+1) for tail in simplex(d-i,r-1)]

def reconstruct(residue,period,points,values):
    polynomial=defaultdict(Fraction)
    for order in points:
        constant=0
        for q in product(*(range(j+1) for j in order)):
            factor=(-1)**(sum(order)-sum(q))
            for d,u in zip(order,q):factor*=comb(d,u)
            constant+=factor*values[q]
        if not constant:continue
        bases=[binomial_basis(residue[i],period,order[i]) for i in range(4)]
        for powers in product(*(range(len(base)) for base in bases)):
            c=Fraction(constant)
            for i,p in enumerate(powers):c*=bases[i][p]
            polynomial[powers]+=c
    return {p:c for p,c in polynomial.items() if c}

def main():
    start=time.monotonic()
    source=THETA/'GENERIC_TWIST_UPPER_POLYNOMIALS.json'
    expected=json.loads(source.read_text())
    descriptors=[];queries=[]
    for g,cycles in enumerate(CLASSES):
        L=lcm(*cycles);points=simplex(SAFE_DEGREES[g])
        for phase in product(range(L),repeat=4):
            ar,br,kr,cr=phase
            rC=cr;rK=(kr-rC-4)%L;rB=(br-rC-3*rK-10)%L;rX=(ar-br)%L
            residue=(rX,rB,rK,rC)
            descriptors.append((g,phase,residue,L,points,len(queries)))
            for q in points:
                queries.append((g,)+tuple(residue[i]+L*q[i] for i in range(4)))
    # Bound every native integer operation by a uniform absolute term sum.
    # Each complete character is <= binom(403,3), each 3x3 determinant has
    # <=6 products, k<=100, and the weighted singleton/pair counts are bounded
    # by 45*k^3.  This deliberately overbounds every intermediate prefix.
    bound=(1+45*100**3)*6*comb(403,3)**3
    assert bound<2**127
    for _,X,B,K,C in queries:
        k=C+K+4;b=C+3*K+10+B;a=b+X
        assert k<=100 and a+C+2<=400
    text=''.join(' '.join(map(str,q))+'\n' for q in queries)
    queryfile=HERE/'GENERIC_UPPER_UNISOLVENT_QUERIES.txt'
    queryfile.write_text(text)
    binary=HERE/'generic_upper_trace_oracle'
    completed=subprocess.run([str(binary)],input=text,text=True,capture_output=True,check=True)
    outputs=[int(value) for value in completed.stdout.splitlines()]
    assert len(outputs)==len(queries)
    data=[{} for _ in CLASSES]
    for g,phase,residue,L,points,offset in descriptors:
        values=dict(zip(points,outputs[offset:offset+len(points)]))
        polynomial=reconstruct(residue,L,points,values)
        key=','.join(map(str,phase))
        assert polynomial==decode(expected['phase_polynomials'][g][key]),(g,phase)
        data[g][phase]=polynomial
    print('PASS',len(descriptors),'phase polynomials from',len(queries),'literal class traces',flush=True)
    output=[{','.join(map(str,key)):encode(poly) for key,poly in row.items()} for row in data]
    (HERE/'GENERIC_UPPER_POLYNOMIALS_INDEPENDENT.json').write_text(json.dumps(output,indent=2)+'\n')

    support=set(p for row in data for poly in row.values() for p in poly)
    orders=set(o for p in support for o in product(*(range(j+1) for j in p)))
    orders.discard((0,0,0,0));orders=sorted(orders)
    identity=data[0][(0,0,0,0)]
    assert all(c>0 for c in identity.values()) and len(identity)==144
    explicit={(i,j,k,c) for i in range(4) for j in range(5) for k in range(5) for c in range(5)
              if j+k<=4 and i+j+k<=5 and j+k+c<=5 and i+j+k+c<=6}
    assert set(identity)==explicit
    unique=[{tuple(sorted(p.items())) for p in row.values()} for row in data]
    assert list(map(len,unique))==[1,14,10,25,3,3,3]
    margins=[];table={tuple(row['order']):row for row in expected['margins']}
    for order in orders:
        ident=difference(identity,order);worst=defaultdict(Fraction)
        for size,row in zip(SIZES[1:],unique[1:]):
            boundpoly={}
            for polynomial in row:
                for p,c in difference(dict(polynomial),order).items():
                    boundpoly[p]=max(boundpoly.get(p,Fraction(0)),abs(c))
            for p,c in boundpoly.items():worst[p]+=size*c
        margin={p:ident.get(p,Fraction(0))-worst.get(p,Fraction(0)) for p in set(ident)|set(worst)}
        assert all(c>=0 for c in margin.values()) and margin.get((0,0,0,0),0)>0
        assert {p:c for p,c in margin.items() if c}==decode(table[order]['margin'])
        assert margin[(0,0,0,0)]==Fraction(table[order]['constant'])
        assert min(margin.values())==Fraction(table[order]['minimum'])
        margins.append({'order':order,'constant':str(margin[(0,0,0,0)]),'margin':encode(margin)})
    assert [list(o) for o in orders]==expected['active_orders']
    assert min(Fraction(row['constant']) for row in margins)==1583020
    print('PASS all143 complete margins and144-order support',flush=True)

    # Four exceptional C=0 supports, checked independently at C=2 by the
    # original direct branching oracle, not by the reconstructed polynomials.
    seeds=((0,0,0),(0,0,1),(0,1,0),(1,0,0))
    seedqueries=[(g,X,B,K,2) for X,B,K in seeds for g in range(7)]
    seedtext=''.join(' '.join(map(str,q))+'\n' for q in seedqueries)
    direct=subprocess.run([str(binary)],input=seedtext,text=True,capture_output=True,check=True)
    seedtraces=[int(v) for v in direct.stdout.splitlines()]
    seedrecords=[]
    expected_vectors=((3,5,8,5,7,4,2),(4,18,22,28,21,17,3),
                      (5,26,30,42,30,25,4),(7,27,33,39,32,25,6))
    for j,(point,want) in enumerate(zip(seeds,expected_vectors)):
        traces=seedtraces[7*j:7*j+7];values=[]
        for chi in CHARS:
            numerator=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
            assert numerator%120==0;values.append(numerator//120)
        assert tuple(values)==want
        seedrecords.append({'X_B_K':point,'C':2,'traces':traces,'effective_multiplicities':values})
    vandermonde=0
    for triple in combinations(range(5),3):
        complement=tuple(i for i in range(5) if i not in triple)
        minor3=prod(triple[j]-triple[i] for i in range(3) for j in range(i+1,3))
        minor2=complement[1]-complement[0]
        vandermonde+=12*(minor3*minor2)**2
    assert vandermonde==27840
    out={'statement':'T058 independent generic upper-chamber reconstruction','status':'PASS',
         'method':'literal singleton interlacing and two-slot normal Pieri multiplicities; direct rank-two skew determinants; unisolvent rational reconstruction; literal step60 translations',
         'safe_phase_degrees':SAFE_DEGREES,'phase_polynomials':len(descriptors),
         'unisolvent_class_traces':len(queries),'native_integer_absolute_bound':str(bound),
         'unique_phase_counts':list(map(len,unique)),'active_positive_orders':len(margins),
         'minimum_constant_margin':'1583020','margins':margins,
         'seed_records':seedrecords,'Vandermonde_sum_of_squares':vandermonde,
         'full_residue_cube_executed':False,
         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'oracle_source_sha256':hashlib.sha256((HERE/'generic_upper_trace_oracle.cpp').read_bytes()).hexdigest(),
         'query_sha256':hashlib.sha256(queryfile.read_bytes()).hexdigest(),
         'elapsed_seconds':time.monotonic()-start}
    (HERE/'GENERIC_UPPER_INDEPENDENT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS independent28 seed values and Vandermonde27840',flush=True)

if __name__=='__main__':main()

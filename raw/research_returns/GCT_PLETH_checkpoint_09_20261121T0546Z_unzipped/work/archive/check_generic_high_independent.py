"""T059 independent reconstruction through literal branching and normal Pieri.

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
    source=THETA/'GENERIC_HIGH_TWIST_POLYNOMIALS.json'
    expected=json.loads(source.read_text())
    descriptors=[];queries=[]
    for g,cycles in enumerate(CLASSES):
        L=lcm(*cycles);points=simplex(SAFE_DEGREES[g])
        for phase in product(range(L),repeat=4):
            ar,br,kr,cr=phase
            rC=(cr-kr)%L;rK=(2*kr-cr-1)%L;rB=(br-rK-1)%L;rX=(ar-br)%L
            residue=(rX,rB,rK,rC)
            descriptors.append((g,phase,residue,L,points,len(queries)))
            for q in points:
                X,B,K,U=(residue[i]+L*q[i] for i in range(4))
                queries.append((g,X,K+B+1,K+U+1,K+2*U+1))
    # Bound every native integer operation by a uniform absolute term sum.
    # Each complete character is <= binom(403,3), each 3x3 determinant has
    # <=6 products, k<=100, and the weighted singleton/pair counts are bounded
    # by 45*k^3.  This deliberately overbounds every intermediate prefix.
    bound=(1+45*100**3)*6*comb(403,3)**3
    assert bound<2**127
    for _,x,b,k,c in queries:
        assert k<=100 and b+x+c+2<=400 and k<=c<2*k and b+c>=2*k
    text=''.join(' '.join(map(str,q))+'\n' for q in queries)
    queryfile=HERE/'GENERIC_HIGH_UNISOLVENT_QUERIES.txt'
    queryfile.write_text(text)
    binary=HERE/'generic_rank_three_trace_oracle'
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
    (HERE/'GENERIC_HIGH_POLYNOMIALS_INDEPENDENT.json').write_text(json.dumps(output,indent=2)+'\n')

    support=set(p for row in data for poly in row.values() for p in poly)
    orders=set(o for p in support for o in product(*(range(j+1) for j in p)))
    orders.discard((0,0,0,0));orders=sorted(orders)
    identity=data[0][(0,0,0,0)]
    assert all(c>0 for c in identity.values()) and len(identity)==151
    explicit={(i,j,k,c) for i in range(4) for j in range(5) for k in range(5) for c in range(4)
              if i+j+k+c<=6 and j+k+c<=5 and i+j<=5 and i+c<=5}
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
    assert min(Fraction(row['constant']) for row in margins)==293640
    print('PASS all150 complete margins and151-order support',flush=True)


    support=json.loads((THETA/'GENERIC_HIGH_TWIST_RECEIPT.json').read_text())
    rows=support['boundary_vectors']+[{'coordinates':point,'effective_multiplicities':values}
                                     for point,values in support['cube_vectors']]
    support_queries=[]
    for row in rows:
        X,B,K,U=row['coordinates']
        for g in range(7):support_queries.append((g,X,K+B+1,K+U+1,K+2*U+1))
    querytext=''.join(' '.join(map(str,q))+'\n' for q in support_queries)
    run=subprocess.run([str(binary)],input=querytext,text=True,capture_output=True,check=True)
    values=[int(v) for v in run.stdout.splitlines()];records=[];zeros=[]
    assert len(rows)==145 and len(values)==1015
    for j,row in enumerate(rows):
        traces=values[7*j:7*j+7];mult=[]
        for label,chi in zip(PARTITIONS,CHARS):
            numerator=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
            assert numerator%120==0
            value=numerator//120;mult.append(value)
            if not value:zeros.append({'coordinates':row['coordinates'],'effective_label':list(label)})
        assert mult==row['effective_multiplicities']
        if j<64:assert min(mult)>0
        records.append({'coordinates':row['coordinates'],'traces':traces,'effective_multiplicities':mult})
    assert zeros==support['zeros'] and len(zeros)==19
    tableaux=(((0,2,3,4),(1,)),((0,3,4),(1,),(2,)),
              ((0,2,4),(1,3)),((0,3),(1,4),(2,)))
    vandermonde=[]
    for tableau in tableaux:
        value=0
        for sigma in permutations(range(5)):
            product_of_minors=1
            for column in tableau:
                row_values=[sigma[i] for i in column]
                product_of_minors*=prod(row_values[j]-row_values[i]
                                       for i in range(len(column)) for j in range(i+1,len(column)))
            value+=product_of_minors**2
        assert value>0;vandermonde.append(value)
    out={'statement':'T059 independent high-twist chamber reconstruction','status':'PASS',
         'method':'literal singleton interlacing and two-slot normal Pieri multiplicities; direct rank-two skew determinants; unisolvent rational reconstruction; literal step60 translations',
         'safe_phase_degrees':SAFE_DEGREES,'phase_polynomials':len(descriptors),
         'unisolvent_class_traces':len(queries),'native_integer_absolute_bound':str(bound),
         'unique_phase_counts':list(map(len,unique)),'active_positive_orders':len(margins),
         'minimum_constant_margin':'293640','margins':margins,
         'support_vectors':records,'zero_cases':zeros,'support_coefficients':1015,
         'four_Vandermonde_square_sums':vandermonde,'full_residue_cube_executed':False,
         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'oracle_source_sha256':hashlib.sha256((HERE/'generic_rank_three_trace_oracle.cpp').read_bytes()).hexdigest(),
         'query_sha256':hashlib.sha256(queryfile.read_bytes()).hexdigest(),
         'elapsed_seconds':time.monotonic()-start}
    (HERE/'GENERIC_HIGH_INDEPENDENT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS independent1015 support coefficients;four nonzero invariant square sums',vandermonde,flush=True)

if __name__=='__main__':main()

"""All nine G035 boundaries reconstructed from original normalized characters."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb,lcm
from pathlib import Path
import hashlib,json,subprocess,time
from check_generic_upper_independent import simplex,SAFE_DEGREES
from check_variable_wall_independent import binomial_basis,decode,encode,difference
from check_third_power_fixed_twist_independent import CLASSES,SIZES
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root'
META={'D0':(3,56,805020),'D1':(3,56,829590),'D2':(3,56,852540),
      'R1a':(2,18,2362800),'R1b':(3,60,3016760),
      'R2a':(2,18,4215300),'R2b':(3,60,1557680),
      'R3a':(2,18,3371790),'R3b':(3,60,3473785)}

def physical(name,Z):
    if name[0]=='D':
        D=int(name[1]);Y,T,H=Z;C=H+2;R=T+D+3
        return T+3-D+Y,C+2*T+3*D+6,C+R,C
    R=int(name[1]);b0={1:2,2:4,3:7}[R];shift={1:1,2:2,3:1}[R]
    if name[-1]=='a':Y,H=Z;x=Y+shift
    else:x,B,H=Z;b0+=1+B
    C=H+2
    return x,C+b0,C+R,C

def interpolation(residue,L,points,values):
    n=len(residue);out=defaultdict(Fraction)
    for order in points:
        constant=0
        for q in product(*(range(j+1) for j in order)):
            coefficient=(-1)**(sum(order)-sum(q))
            for a,b in zip(order,q):coefficient*=comb(a,b)
            constant+=coefficient*values[q]
        if not constant:continue
        bases=[binomial_basis(residue[i],L,order[i]) for i in range(n)]
        for exponent in product(*(range(len(base)) for base in bases)):
            c=Fraction(constant)
            for i,e in enumerate(exponent):c*=bases[i][e]
            out[exponent]+=c
    return {p:c for p,c in out.items() if c}

def main():
    start=time.monotonic();records={};total_phases=0;total_traces=0;total_margins=0
    for name,(dimension,wanted_orders,wanted_minimum) in META.items():
        source=ROOT/f'GENERIC_TWIST_BOUNDARY_{name}.json'
        expected=json.loads(source.read_text());descriptors=[];queries=[]
        for g,cycles in enumerate(CLASSES):
            L=lcm(*cycles);points=simplex(SAFE_DEGREES[g],dimension)
            for phase in product(range(L),repeat=dimension):
                descriptors.append((g,phase,L,points,len(queries)))
                for q in points:
                    point=tuple(phase[i]+L*q[i] for i in range(dimension))
                    x,b,k,c=physical(name,point)
                    assert 0<=c<k<=100 and b+c>=2*k and 2*b+x+3*c>=5*k and b+x+c+2<=400
                    queries.append((g,x,b,k,c))
        queryfile=HERE/f'GENERIC_BOUNDARY_{name}_QUERIES.txt'
        text=''.join(' '.join(map(str,q))+'\n' for q in queries);queryfile.write_text(text)
        run=subprocess.run([str(HERE/'generic_normalized_trace_oracle')],input=text,text=True,capture_output=True,check=True)
        answers=[int(v) for v in run.stdout.splitlines()];assert len(answers)==len(queries)
        data=[{} for _ in CLASSES]
        for g,phase,L,points,offset in descriptors:
            poly=interpolation(phase,L,points,dict(zip(points,answers[offset:offset+len(points)])))
            assert poly==decode(expected['phase_polynomials'][g][','.join(map(str,phase))]),(name,g,phase)
            data[g][phase]=poly
        output=[{','.join(map(str,k)):encode(p) for k,p in row.items()} for row in data]
        (HERE/f'GENERIC_BOUNDARY_{name}_POLYNOMIALS_INDEPENDENT.json').write_text(json.dumps(output,indent=2)+'\n')
        zero=(0,)*dimension;identity=data[0][zero];assert all(c>=0 for c in identity.values())
        support=set(p for row in data for poly in row.values() for p in poly)
        orders=set(o for p in support for o in product(*(range(v+1) for v in p)))
        orders.discard(zero);orders=sorted(orders)
        assert [list(o) for o in orders]==expected['active_orders']
        unique=[{tuple(sorted(p.items())) for p in row.values()} for row in data]
        table={tuple(row['order']):row for row in expected['margins']};margins=[]
        for order in orders:
            first=difference(identity,order);worst=defaultdict(Fraction)
            for size,row in zip(SIZES[1:],unique[1:]):
                bound={}
                for poly in row:
                    for p,c in difference(dict(poly),order).items():bound[p]=max(bound.get(p,Fraction(0)),abs(c))
                for p,c in bound.items():worst[p]+=size*c
            margin={p:first.get(p,Fraction(0))-worst.get(p,Fraction(0)) for p in set(first)|set(worst)}
            assert all(c>=0 for c in margin.values()) and margin.get(zero,0)>0
            assert {p:c for p,c in margin.items() if c}==decode(table[order]['margin'])
            assert margin[zero]==Fraction(table[order]['constant'])
            assert min(margin.values())==Fraction(table[order]['minimum'])
            margins.append({'order':order,'constant':str(margin[zero]),'margin':encode(margin)})
        assert len(margins)==wanted_orders
        assert min(Fraction(m['constant']) for m in margins)==wanted_minimum
        records[name]={'dimension':dimension,'phases':len(descriptors),'literal_traces':len(queries),
                       'positive_margins':len(margins),'minimum_constant_margin':wanted_minimum,'margins':margins,
                       'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                       'query_sha256':hashlib.sha256(queryfile.read_bytes()).hexdigest()}
        total_phases+=len(descriptors);total_traces+=len(queries);total_margins+=len(margins)
        print(name,'PASS',len(descriptors),'phases,',len(queries),'literal traces,',len(margins),'margins',flush=True)
    out={'statement':'G035 all nine boundary pieces independent reconstruction','status':'PASS',
         'method':'original normalized rank-three restriction oracle; safe-degree unisolvent interpolation; literal step60 polynomial translations',
         'safe_phase_degrees':SAFE_DEGREES,'pieces':records,'total_phases':total_phases,
         'total_literal_traces':total_traces,'total_positive_margins':total_margins,
         'full_residue_cube_executed':False,'elapsed_seconds':time.monotonic()-start}
    (HERE/'GENERIC_BOUNDARIES_INDEPENDENT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS all nine boundary pieces',total_phases,total_traces,total_margins,flush=True)

if __name__=='__main__':main()

"""G035 all-route evaluation and independent new-piece matrix checks."""
from pathlib import Path
from itertools import islice,product
from math import comb,lcm,prod
import json,subprocess,sys
from check_third_power_fixed_twist_independent import CLASSES,CHARS,SIZES,PARTITIONS
from check_variable_wall_independent import decode
from check_generic_lower_independent import physical as lower_physical
from check_generic_boundaries_independent import physical as boundary_physical,META
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root'
sys.path.insert(0,str(ROOT))
import normalized_below_positive as positive

def multiplicities(traces):
    values=[]
    for chi in CHARS:
        numerator=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
        assert numerator%120==0;values.append(numerator//120)
    return values

def route_name(x,b,k,c,d,mu):
    name,args=positive.route(x,b,k,c,d,mu)
    return 'lower'+args[0] if name=='lower' else name

cases={}
for branch in ('A','B'):
    for Z in ((0,0,0,2),(1,0,1,2),(0,2,0,3)):
        cases[lower_physical(branch,Z)]='lower'+branch
for name,(dimension,_,_) in META.items():
    for Z in ((0,)*dimension,(1,)*dimension,tuple(range(dimension))):
        cases[boundary_physical(name,Z)]=name
for X,B,K,C in ((0,0,0,2),(1,2,1,3),(3,0,2,2)):
    cases[X,C+3*K+10+B,C+K+4,C]='upper'
for C in (0,1):
    for R in (1,2,3,6):
        b0=2*R
        cases[R,C+b0,C+R,C]='zero' if C==0 else 'one'
keys=sorted(cases)
queries=[(g,)+point for point in keys for g in range(7)]
text=''.join(' '.join(map(str,q))+'\n' for q in queries)
result=subprocess.run([str(HERE/'generic_normalized_trace_oracle')],input=text,text=True,capture_output=True,check=True)
traces=[int(v) for v in result.stdout.splitlines()];assert len(traces)==len(queries)
counts={'actual_parameter_cases':len(keys),'actual_class_traces':len(queries),
        'actual_coefficients':0,'provider_exports':0,'continuation_coefficients':0,'matrices':0,'witnesses':0}
branches=set();exported=set()
for j,(x,b,k,c) in enumerate(keys):
    values=multiplicities(traces[7*j:7*j+7])
    for d in (0,1):
        for i,mu in enumerate(PARTITIONS):
            name=route_name(x,b,k,c,d,mu)
            assert name==cases[x,b,k,c]
            branches.add(name)
            effective=6-i if (d+b+x+c)%2 else i
            assert positive.coefficient(x,b,k,c,d,mu)==values[effective],(x,b,k,c,d,mu)
            counts['actual_coefficients']+=1
            if (name,mu) not in exported:
                packet=positive.polytopes(x,b,k,c,d,mu)
                assert isinstance(packet,dict)
                exported.add((name,mu));counts['provider_exports']+=1
assert branches==set(META)|{'zero','one','upper','lowerA','lowerB'}

for name in ('A','B')+tuple(META):
    lower=name in ('A','B')
    dimension=4 if lower else META[name][0]
    filename=(f'GENERIC_LOWER_{name}_POLYNOMIALS_INDEPENDENT.json' if lower else
              f'GENERIC_BOUNDARY_{name}_POLYNOMIALS_INDEPENDENT.json')
    raw=json.loads((HERE/filename).read_text())
    data=[{tuple(map(int,key.split(','))):decode(poly) for key,poly in row.items()} for row in raw]
    for Z in (tuple(61+i for i in range(dimension)),tuple(301+i for i in range(dimension))):
        physical=lower_physical(name,Z) if lower else boundary_physical(name,Z)
        x,b,k,c=physical;values=[]
        for cycles,row in zip(CLASSES,data):
            L=lcm(*cycles)
            value=sum(coef*prod(z**p for z,p in zip(Z,power))
                      for power,coef in row[tuple(z%L for z in Z)].items())
            assert value.denominator==1;values.append(value.numerator)
        wanted=multiplicities(values)
        for d in (0,1):
            for i,mu in enumerate(PARTITIONS):
                effective=6-i if (d+b+x+c)%2 else i
                got=positive.coefficient(x,b,k,c,d,mu)
                assert got==wanted[effective]
                counts['continuation_coefficients']+=1
                if lower:
                    tags=positive.lower.tags(name,Z,d,mu)
                    matrix=positive.lower.constraints;witnesses=positive.lower.witnesses
                else:
                    tags=positive.boundary_tags(name,PARTITIONS[effective],Z)
                    matrix=positive.constraints;witnesses=positive.witnesses
                recovered=0
                assert len(tags)<=152
                for tag in tags:
                    if not tag['constant']:continue
                    poly=matrix(tag);assert len(poly['variables'])<=11
                    recovered+=tag['constant']*prod(comb(q,j) if q>=j else 0 for q,j in zip(tag['quotient'],tag['order']))
                    counts['matrices']+=1
                    for point in islice(witnesses(tag),2):
                        assert len(point)==len(poly['variables'])
                        assert all(lo<=z<=hi for lo,z,hi in zip(poly['lower_bounds'],point,poly['upper_bounds']))
                        assert all(sum(a*z for a,z in zip(row,point))==rhs for row,rhs in zip(poly['A_eq'],poly['b_eq']))
                        assert all(sum(a*z for a,z in zip(row,point))>=rhs for row,rhs in zip(poly['A_ge'],poly['b_ge']))
                        counts['witnesses']+=1
                assert recovered==got
out={'statement':'G035 independent all-route and positive-matrix evaluator audit','status':'PASS',
     'branches':sorted(branches),'both_determinant_parities':True,**counts}
(HERE/'NORMALIZED_BELOW_EVALUATOR_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

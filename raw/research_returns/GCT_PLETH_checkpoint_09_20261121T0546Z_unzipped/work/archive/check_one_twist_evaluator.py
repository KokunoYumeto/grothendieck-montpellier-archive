"""Independent reconstructed-data continuation, printed tables and matrix checks."""
from pathlib import Path
from fractions import Fraction
from itertools import islice
from math import comb,prod,lcm
import sys,json,re
from check_one_twist_independent import strip_change,CLASSES,CHARS,SIZES,PARTITIONS,decode
HERE=Path(__file__).resolve().parent
THETA=HERE.parent/'theta'/'outer5'/'variable_wall'
sys.path.insert(0,str(THETA))
import positive_one_twist_chamber as chamber
import one_twist_strip as strip

raw=json.loads((HERE/'ONE_TWIST_POLYNOMIALS_INDEPENDENT.json').read_text())
data=[{tuple(map(int,key.split(','))):decode(value) for key,value in row.items()} for row in raw]
stripdata=[{key:strip_change(value) for key,value in row.items()} for row in data]
receipt=json.loads((HERE/'ONE_TWIST_INDEPENDENT_RECEIPT.json').read_text())
report=(THETA/'one_twist_report.md').read_text()
identity_rows=0
for line in report.splitlines():
    match=re.fullmatch(r'\| \((\d+),(\d+)\) \| ([0-9K+²³⁴]+) \|',line)
    if not match:continue
    i,j=map(int,match.group(1,2));polynomial={}
    for term in match.group(3).split('+'):
        if 'K' not in term:power=0;c=int(term)
        else:
            before,after=term.split('K');c=int(before) if before else 1
            power={'':1,'²':2,'³':3,'⁴':4}[after]
        polynomial[power]=c
    expected={p[2]:int(6*c) for p,c in data[0][(0,0,0)].items() if p[:2]==(i,j)}
    assert polynomial==expected,(i,j,polynomial,expected)
    identity_rows+=1
assert identity_rows==17

def check_printed_margins(path,key,strip_mode=False):
    count=0
    for line in path.read_text().splitlines():
        pattern=(r'\| \((\d+),(\d+)\) \| (\d+) \| (\d+) \|' if strip_mode
                 else r'\| \((\d+),(\d+),(\d+)\) \| (\d+) \| (\d+) \|')
        match=re.fullmatch(pattern,line)
        if not match:continue
        nums=list(map(int,match.groups()))
        order=(nums[0],0,nums[1]) if strip_mode else tuple(nums[:3])
        margin=decode(receipt[key]['coefficientwise_margins'][','.join(map(str,order))])
        assert margin[(0,0,0)]==nums[-2]
        assert min(margin.values())==nums[-1]
        count+=1
    return count

assert check_printed_margins(THETA/'one_twist_report.md','chamber_margins')==9
assert check_printed_margins(THETA/'one_twist_strip_report.md','strip_margins',True)==5

def values(parameters,strip_mode):
    X,B,K=parameters
    if strip_mode:a=3*K+11+X;b=3*K+11;k=K+5;polys=stripdata
    else:a=3*K+6+B+X;b=3*K+6+B;k=K+3;polys=data
    traces=[]
    for cycles,row in zip(CLASSES,polys):
        L=lcm(*cycles)
        trace=sum(c*prod(z**p for z,p in zip(parameters,powers))
                  for powers,c in row[(a%L,b%L,k%L)].items())
        assert trace.denominator==1;traces.append(trace.numerator)
    answer=[]
    for chi in CHARS:
        numerator=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
        assert numerator%120==0;answer.append(numerator//120)
    return answer

def run(strip_mode):
    parameters=((0,0,0),(1,0,0),(0,0,1),(59,0,59),(60,0,60),(121,0,122),(301,0,302)) if strip_mode else (
        (0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,1),(61,2,1),(2,61,1),(2,1,61),(63,64,65),(301,302,303))
    mod=strip if strip_mode else chamber
    counts={'parameters':len(parameters),'coefficients':0,'matrices':0,'witnesses':0}
    for Z in parameters:
        X,B,K=Z;k=K+(5 if strip_mode else 3);b=3*k-(4 if strip_mode else 3)+B
        exact=values(Z,strip_mode)
        for d in (0,1):
            for i,mu in enumerate(PARTITIONS):
                effective=6-i if (d+b+X+1)%2 else i
                args=(X,k,d,mu) if strip_mode else (X,b,k,d,mu)
                got=mod.coefficient(*args);assert got==exact[effective],(Z,d,mu,got,exact)
                counts['coefficients']+=1
                tags=mod.tags(*args);assert len(tags)==(17 if strip_mode else 46)
                recovered=0
                for tag in tags:
                    if not tag['constant']:continue
                    poly=mod.constraints(tag)
                    assert len(poly['variables'])<=9
                    if strip_mode:
                        assert tag['quotient'][1]==0 and tag['order'][1]==0
                    recovered+=tag['constant']*prod(comb(q,j) if q>=j else 0
                                                       for q,j in zip(tag['quotient'],tag['order']))
                    counts['matrices']+=1
                    for point in islice(mod.witnesses(tag),3):
                        assert len(point)==len(poly['variables'])
                        assert all(lo<=z<=hi for lo,z,hi in zip(poly['lower_bounds'],point,poly['upper_bounds']))
                        assert all(sum(a*z for a,z in zip(row,point))==rhs for row,rhs in zip(poly['A_eq'],poly['b_eq']))
                        assert all(sum(a*z for a,z in zip(row,point))>=rhs for row,rhs in zip(poly['A_ge'],poly['b_ge']))
                        counts['witnesses']+=1
                assert recovered==got
    return counts

output={'statement':'T055/T056 independent printed tables and positive evaluator audit','status':'PASS',
        'identity_rows':identity_rows,'chamber_margin_rows':9,'strip_margin_rows':5,
        'chamber':run(False),'strip':run(True),'both_determinant_parities':True}
(HERE/'ONE_TWIST_EVALUATOR_RECEIPT.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))

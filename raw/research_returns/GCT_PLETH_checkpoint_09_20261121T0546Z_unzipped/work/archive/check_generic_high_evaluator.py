"""T059: independent printed identity table and positive evaluator audit."""
from pathlib import Path
from fractions import Fraction
from itertools import islice
from math import comb,lcm,prod
import sys,json,re
import sympy as sp
from check_third_power_fixed_twist_independent import CLASSES,CHARS,SIZES,PARTITIONS
from check_variable_wall_independent import decode
HERE=Path(__file__).resolve().parent
THETA=HERE.parent/'theta'/'outer5'/'variable_wall'
sys.path.insert(0,str(THETA))
import generic_high_twist_positive as positive

raw=json.loads((HERE/'GENERIC_HIGH_POLYNOMIALS_INDEPENDENT.json').read_text())
data=[{tuple(map(int,k.split(','))):decode(v) for k,v in row.items()} for row in raw]
X,B,K,U=sp.symbols('X B K U')
identity=data[0][(0,0,0,0)]
expression=sum(sp.Rational(c.numerator,c.denominator)*sp.prod(z**e for z,e in zip((X,B,K,U),p))
               for p,c in identity.items())
factor=sp.Poly(sp.cancel(12*expression/(X+1)),X,B,K,U)
qdata={p:Fraction(int(c.p),int(c.q)) for p,c in factor.terms()}
assert all(c>0 for c in qdata.values())
rows=0
report=(THETA/'generic_high_twist_report.md').read_text()
for line in report.splitlines():
    match=re.fullmatch(r'\| \((\d+),(\d+)\) \| ([0-9KX+²³⁴]+) \|',line)
    if not match:continue
    ib,iu=map(int,match.group(1,2));got={}
    for term in match.group(3).split('+'):
        number=re.match(r'\d+',term)
        coefficient=int(number.group()) if number else 1
        rest=term[len(number.group()):] if number else term
        powers={'X':0,'K':0}
        while rest:
            variable=rest[0];rest=rest[1:];degree=1
            if rest and rest[0] in '²³⁴':
                degree={'²':2,'³':3,'⁴':4}[rest[0]];rest=rest[1:]
            powers[variable]+=degree
        got[powers['X'],powers['K']]=coefficient
    wanted={(p[0],p[2]):int(c) for p,c in qdata.items() if p[1]==ib and p[3]==iu}
    assert got==wanted,(ib,iu,got,wanted)
    rows+=1
assert rows==17

def exact(parameters):
    X,B,K,U=parameters;k=K+U+1;c=K+2*U+1;b=K+B+1;a=b+X
    traces=[]
    for cycles,row in zip(CLASSES,data):
        L=lcm(*cycles)
        value=sum(q*prod(z**e for z,e in zip(parameters,p))
                  for p,q in row[(a%L,b%L,k%L,c%L)].items())
        assert value.denominator==1;traces.append(value.numerator)
    result=[]
    for chi in CHARS:
        numerator=sum(s*q*t for s,q,t in zip(SIZES,chi,traces))
        assert numerator%120==0;result.append(numerator//120)
    return result

points=((0,0,0,0),(0,0,0,1),(0,0,1,0),(0,1,0,0),(0,1,0,1),
        (0,1,1,0),(1,0,0,0),(1,0,1,0),(2,0,0,0),
        (61,2,3,4),(1,62,3,4),(1,2,63,4),(1,2,3,64),(61,62,63,64),(301,302,303,304))
counts={'coefficient_checks':0,'matrices':0,'witnesses':0}
for point in points:
    X,B,K,U=point;k=K+U+1;c=K+2*U+1;b=K+B+1
    values=exact(point)
    for d in (0,1):
        for index,mu in enumerate(PARTITIONS):
            effective=6-index if (d+b+X+c)%2 else index
            coefficient=positive.coefficient(X,b,k,c,d,mu)
            assert coefficient==values[effective],(point,d,mu,coefficient,values)
            counts['coefficient_checks']+=1
            tags=positive.tags(X,b,k,c,d,mu);assert len(tags)==151
            recovered=0
            for tag in tags:
                if not tag['constant']:continue
                matrix=positive.constraints(tag)
                assert len(matrix['variables'])<=11
                recovered+=tag['constant']*prod(comb(q,j) if q>=j else 0
                                               for q,j in zip(tag['quotient'],tag['order']))
                counts['matrices']+=1
                for witness in islice(positive.witnesses(tag),2):
                    assert len(witness)==len(matrix['variables'])
                    assert all(lo<=v<=hi for lo,v,hi in zip(matrix['lower_bounds'],witness,matrix['upper_bounds']))
                    assert all(sum(a*z for a,z in zip(row,witness))==rhs for row,rhs in zip(matrix['A_eq'],matrix['b_eq']))
                    assert all(sum(a*z for a,z in zip(row,witness))>=rhs for row,rhs in zip(matrix['A_ge'],matrix['b_ge']))
                    counts['witnesses']+=1
            assert recovered==coefficient
out={'statement':'T059 independent printed factor and positive-evaluator audit','status':'PASS',
     'factor_table_rows':rows,'parameter_points':len(points),'both_determinant_parities':True,**counts}
(HERE/'GENERIC_HIGH_EVALUATOR_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
